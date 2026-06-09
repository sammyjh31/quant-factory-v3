# Long Context Judgment Live Pilot 003 Stop Condition

Status: Goal 14A planning/admission record
Historical status: pre-run admission record; current run status is owned by `labs/long_context_judgment/EXPORTS/run_record.live_pilot_003.json`.

Goal 14A stops after admission packet creation and verification.

Goal 14B must stop before any model call if any pre-call condition in `labs/long_context_judgment/PLANNING/live_llm_pilot_002/stop_condition.md` fails, with these pilot-003 substitutions:

* the run must use `deepseek-v4-pro` with thinking **enabled** (recorded as `thinking: {"type": "enabled"}`); stop if thinking cannot be enabled,
* the output cap is `4000` tokens; stop if the request cannot set it,
* the output contract remains the five approved sections from the pilot 002/003 template; stop if it expands.

All other conditions carry over unchanged: approved source hash present and ignored, `DEEPSEEK_API_KEY` present, `$3` budget cap, no model substitution, stream and tools disabled, no model-emitted offsets or hashes, trace storage only under ignored paths, no authority-claiming post-run records.

No retry is allowed unless the provider call fails before producing output.
