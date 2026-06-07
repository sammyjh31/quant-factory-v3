# AGENTS.md - Docs

Docs should clarify current direction, not accumulate contradictory history.

Do not append new current guidance below stale guidance.

When direction changes:

1. rewrite the owning current doc,
2. delete obsolete text when safe,
3. archive only if the old text has learning value,
4. avoid creating a second truth source.

Be sure to look into the files in docs/agent-checklists/ for further direction as well.

README owns project purpose.
PORTFOLIO_CURRENT owns active portfolio state.
PROTOCOL_CURRENT owns protocol version and schema inventory.
LAB_REGISTRY owns lab status.
GRADUATION_LEDGER owns graduation status.

Generated synthesis summaries must not be copied into docs as authority.

Milestone-one constraints are phase-local. Do not write docs that make them sound like permanent V3 doctrine.

## Supersession Convention

When stale current guidance is kept for historical value, mark it clearly:

```text
Superseded by: <owning current doc>
Status: historical / archived / no longer current
```

If the old text has no learning value, delete it instead of preserving it.

Do not create a new doc merely because guidance changed; first update stale text directly, delete it, or archive it with supersession markers.
