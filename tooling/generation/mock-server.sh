#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SPEC="${1:-$ROOT/specs/billing/openapi.yaml}"
OUT="${2:-$ROOT/generated/mocks}"

if ! command -v npx >/dev/null 2>&1; then
  echo "npx is required to generate mocks."
  exit 1
fi

mkdir -p "$OUT"

echo "Generating mock server stub from: $SPEC"
npx --yes @stoplight/prism-cli@5 mock "$SPEC" --port 4010 &
PRISM_PID=$!

echo "$PRISM_PID" > "$OUT/prism.pid"
echo "Mock server running at http://127.0.0.1:4010 (PID $PRISM_PID)"
echo "Stop with: kill \$(cat $OUT/prism.pid)"
