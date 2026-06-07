# AGENTS.md - Protocol Package

This package owns protocol validation tooling and schema loading.

The canonical protocol authority is the hand-authored JSON Schema files.

Python code is tooling, not truth.

Do not add lab-specific runtime logic here.

Do not add fields to the protocol just because one lab wants them.

Before adding a protocol field, check whether an existing schema field, `payload`, `notes`, or a lab-local record can own the role.

Protocol changes require evidence and ADR.

Keep this package boring:

* load schemas,
* validate records,
* report errors,
* expose a CLI.

Do not implement live LLM calls, lab methods, graph logic, product logic, strategy logic, or synthesis claims here.
