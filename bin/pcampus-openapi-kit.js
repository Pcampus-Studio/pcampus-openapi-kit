#!/usr/bin/env node

const { spawnSync } = require('node:child_process');
const fs = require('node:fs');
const path = require('node:path');

const ROOT = path.resolve(__dirname, '..');

const TEMPLATES = {
  crud: 'resource-crud.yaml',
  auth: 'auth-service.yaml',
  webhook: 'webhook.yaml',
  event: 'event-driven.yaml',
};

function usage() {
  console.log(`pcampus-openapi-kit — OpenAPI toolkit by Pcampus Studio

Usage:
  pcampus-openapi-kit lint [paths...]       Lint specs with Spectral rules
  pcampus-openapi-kit validate [paths...]   Validate OpenAPI structure and refs
  pcampus-openapi-kit init <template>       Scaffold a new spec from a template

Templates:
  crud, auth, webhook, event

Init options:
  --name <resource>   Resource name (default: resource)
  --out <directory>   Output directory (default: ./my-api)

Examples:
  pcampus-openapi-kit lint
  pcampus-openapi-kit validate specs/billing/openapi.yaml
  pcampus-openapi-kit init crud --name customers --out ./customers-api
`);
}

function defaultSpecPaths() {
  return ['specs/**/*.yaml', 'templates/**/*.yaml'];
}

function expandGlobPatterns(patterns) {
  const results = [];

  for (const pattern of patterns) {
    if (!pattern.includes('*')) {
      if (fs.existsSync(path.resolve(ROOT, pattern))) {
        results.push(path.resolve(ROOT, pattern));
      }
      continue;
    }

    const baseDir = pattern.split('*')[0].replace(/\/$/, '') || '.';
    const walk = (dir) => {
      const absDir = path.resolve(ROOT, dir);
      if (!fs.existsSync(absDir)) {
        return;
      }

      for (const entry of fs.readdirSync(absDir, { withFileTypes: true })) {
        const rel = path.join(dir, entry.name);
        if (entry.isDirectory()) {
          walk(rel);
        } else if (entry.name.endsWith('.yaml') || entry.name.endsWith('.yml')) {
          results.push(path.resolve(ROOT, rel));
        }
      }
    };

    walk(baseDir);
  }

  return [...new Set(results)].sort();
}

function runLint(args) {
  const targets = args.length > 0 ? expandGlobPatterns(args) : expandGlobPatterns(defaultSpecPaths());

  if (targets.length === 0) {
    console.error('No OpenAPI files found to lint.');
    process.exit(1);
  }

  const spectralBin = path.join(ROOT, 'node_modules', '.bin', 'spectral');
  const ruleset = path.join(ROOT, 'tooling', 'lint', 'spectral.yaml');

  let failed = false;

  for (const target of targets) {
    const result = spawnSync(spectralBin, ['lint', target, '--ruleset', ruleset, '--fail-severity', 'error'], {
      cwd: ROOT,
      stdio: 'inherit',
    });

    if (result.status !== 0) {
      failed = true;
    }
  }

  if (failed) {
    process.exit(1);
  }

  console.log(`Lint passed for ${targets.length} file(s).`);
}

async function runValidate(args) {
  const SwaggerParser = require('@apidevtools/swagger-parser');
  const targets = args.length > 0 ? expandGlobPatterns(args) : expandGlobPatterns(defaultSpecPaths());

  if (targets.length === 0) {
    console.error('No OpenAPI files found to validate.');
    process.exit(1);
  }

  let failed = false;

  for (const target of targets) {
    try {
      await SwaggerParser.validate(target);
      console.log(`Valid: ${path.relative(ROOT, target)}`);
    } catch (error) {
      failed = true;
      console.error(`Invalid: ${path.relative(ROOT, target)}`);
      console.error(error.message);
    }
  }

  if (failed) {
    process.exit(1);
  }

  console.log(`Validation passed for ${targets.length} file(s).`);
}

function copyDirectory(src, dest) {
  fs.mkdirSync(dest, { recursive: true });

  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);

    if (entry.isDirectory()) {
      copyDirectory(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

function replacePlaceholders(content, replacements) {
  let result = content;

  for (const [key, value] of Object.entries(replacements)) {
    result = result.replaceAll(key, value);
  }

  return result;
}

function runInit(args) {
  const templateKey = args[0];

  if (!templateKey || !(templateKey in TEMPLATES)) {
    console.error(`Unknown template "${templateKey ?? ''}". Choose: ${Object.keys(TEMPLATES).join(', ')}`);
    process.exit(1);
  }

  let resourceName = 'resource';
  let outDir = './my-api';

  for (let i = 1; i < args.length; i += 1) {
    if (args[i] === '--name' && args[i + 1]) {
      resourceName = args[i + 1];
      i += 1;
    } else if (args[i] === '--out' && args[i + 1]) {
      outDir = args[i + 1];
      i += 1;
    }
  }

  const plural = resourceName.endsWith('s') ? resourceName : `${resourceName}s`;
  const Pascal = resourceName
    .split(/[-_]/)
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join('');
  const snake = resourceName.replace(/-/g, '_');
  const snakePlural = plural.replace(/-/g, '_');

  const absOut = path.resolve(process.cwd(), outDir);
  const templateFile = path.join(ROOT, 'templates', TEMPLATES[templateKey]);
  const templateContent = fs.readFileSync(templateFile, 'utf8');

  const openapiContent = replacePlaceholders(templateContent, {
    '/resources': `/${plural}`,
    '/resources/{resource_id}': `/${plural}/{${snake}_id}`,
    resource_id: `${snake}_id`,
    Resources: Pascal === 'Resource' ? `${Pascal}s` : `${Pascal}s`,
    Resource: Pascal,
    list_resources: `list_${snakePlural}`,
    create_resource: `create_${snake}`,
    get_resource: `get_${snake}`,
    update_resource: `update_${snake}`,
    delete_resource: `delete_${snake}`,
    PaginatedResourceList: `Paginated${Pascal}List`,
    ResourceCreateRequest: `${Pascal}CreateRequest`,
    ResourceUpdateRequest: `${Pascal}UpdateRequest`,
  });

  fs.mkdirSync(absOut, { recursive: true });
  fs.mkdirSync(path.join(absOut, 'shared'), { recursive: true });

  fs.writeFileSync(path.join(absOut, 'openapi.yaml'), openapiContent);
  copyDirectory(path.join(ROOT, 'specs', 'shared'), path.join(absOut, 'shared'));

  const openapiForLocalRefs = openapiContent.replaceAll('../specs/shared/', './shared/');
  fs.writeFileSync(path.join(absOut, 'openapi.yaml'), openapiForLocalRefs);

  console.log(`Created ${absOut}/openapi.yaml from template "${templateKey}".`);
  console.log(`Shared schemas copied to ${absOut}/shared/`);
  console.log('\nNext steps:');
  console.log(`  pcampus-openapi-kit lint ${outDir}/openapi.yaml`);
  console.log(`  pcampus-openapi-kit validate ${outDir}/openapi.yaml`);
}

const [command, ...rest] = process.argv.slice(2);

switch (command) {
  case 'lint':
    runLint(rest);
    break;
  case 'validate':
    runValidate(rest).catch((error) => {
      console.error(error.message);
      process.exit(1);
    });
    break;
  case 'init':
    runInit(rest);
    break;
  case undefined:
  case '-h':
  case '--help':
    usage();
    break;
  default:
    console.error(`Unknown command: ${command}\n`);
    usage();
    process.exit(1);
}
