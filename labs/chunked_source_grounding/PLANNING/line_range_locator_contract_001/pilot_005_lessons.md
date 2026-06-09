# Pilot 005 Lessons

Status: planning only

pilot 005 asked for line ranges and char offsets in one direct locator-emission contract.

Strict manual locator review found:

- line ranges `3/3` valid and reviewer-useful;
- char offsets `3/3` syntactically valid but `0/3` evidence-valid;
- quote hashes `3` computed locally and mechanically valid but not support-valid;
- exact labels `0`;
- approximate labels `2`;
- broad labels `1`;
- overclaimed exactness `0`.

The useful signal is that line ranges reduced reviewer reconstruction. The failure signal is that char offsets and quote-hash support validity were not reliable.

## Line-Range-First Hypothesis

The line-range-first hypothesis is the next bounded contract question.

The line-range-first hypothesis is that the next pilot should ask only for line-range support candidates, then let local review decide whether offsets and hashes should be computed.

Do not rerun pilot 005's broader locator contract unchanged.

This is not proof that line-range-first locator candidates will pass. It is a narrower next contract shaped by the pilot 005 failure.
