const { pattern, schema, truthy } = require('@stoplight/spectral-functions');

module.exports = {
  rules: {
    'pcampus-operation-id-snake-case': {
      description: 'operationId must use snake_case.',
      message: '{{property}} must be snake_case (e.g. list_invoices).',
      severity: 'error',
      given: '$.paths[*][get,post,put,patch,delete,head,options].operationId',
      then: {
        function: pattern,
        functionOptions: {
          match: '^[a-z][a-z0-9_]*$',
        },
      },
    },
    'pcampus-operation-description-min-length': {
      description: 'Operation descriptions must be explicit enough for humans and AI agents.',
      message: '{{property}} should be at least 40 characters and mention failure cases when applicable.',
      severity: 'warn',
      given: '$.paths[*][get,post,put,patch,delete].description',
      then: {
        function: pattern,
        functionOptions: {
          match: '^.{40,}',
        },
      },
    },
    'pcampus-mutation-agent-hints': {
      description: 'Mutating operations should declare x-agent-hints.',
      message: 'Add x-agent-hints for POST, PUT, PATCH, and DELETE operations.',
      severity: 'error',
      given: '$.paths[*][post,put,patch,delete]',
      then: {
        field: 'x-agent-hints',
        function: truthy,
      },
    },
    'pcampus-agent-hints-shape': {
      description: 'x-agent-hints must include safe_to_retry, destructive, and requires_confirmation.',
      message: 'x-agent-hints must include safe_to_retry, destructive, and requires_confirmation.',
      severity: 'error',
      given: '$.paths[*][get,post,put,patch,delete].x-agent-hints',
      then: {
        function: schema,
        functionOptions: {
          schema: {
            type: 'object',
            required: ['safe_to_retry', 'destructive', 'requires_confirmation'],
            properties: {
              safe_to_retry: { type: 'boolean' },
              destructive: { type: 'boolean' },
              requires_confirmation: { type: 'boolean' },
              workflow_hint: { type: 'string' },
            },
          },
        },
      },
    },
  },
};
