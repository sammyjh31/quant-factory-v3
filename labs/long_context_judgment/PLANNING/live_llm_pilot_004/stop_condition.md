# Long Context Judgment Live Pilot 004 Stop Condition

Status: Goal 14C planning/admission record
Historical status: pre-run admission record; current run status is owned by `labs/long_context_judgment/EXPORTS/run_record.live_pilot_004.json`.

Goal 14C stops after admission packet creation and verification.

Goal 14D must stop before any model call if any pre-call condition in `labs/long_context_judgment/PLANNING/live_llm_pilot_002/stop_condition.md` fails, with these pilot-004 substitutions:

* thinking **enabled** (`thinking: {"type": "enabled"}`); stop if it cannot be enabled,
* output cap `12000` tokens; stop if the request cannot set it,
* the contract remains the five approved sections; stop if it expands.

All other conditions carry over unchanged (approved source hash, ignored source, `DEEPSEEK_API_KEY`, `$3` cap, no substitution, stream/tools disabled, no model-emitted offsets/hashes, ignored trace paths only, no authority-claiming records).

No retry is allowed unless the provider call fails before producing output.
