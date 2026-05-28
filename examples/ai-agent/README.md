# AI Agent Examples

Examples showing how AI agents should consume specs from this repository.

## Read-only discovery script

```bash
python examples/ai-agent/discover.py
```

The script reads `specs/billing/openapi.yaml` and prints:

- available operations
- `x-agent-hints` metadata
- a recommended read-only discovery order

## Recommended agent flow

1. Run `discover.py` or read `docs/agent-consumption.md`
2. Call safe read-only endpoints first (`safe_to_retry: true`)
3. Ask for human confirmation before destructive or mutating operations
4. Branch on `error.code`, not HTTP status alone

## Planned additions

- scripted mutation workflow with explicit confirmation checkpoints
- MCP tool wrapper for billing invoice discovery

See [docs/agent-consumption.md](../../docs/agent-consumption.md).
