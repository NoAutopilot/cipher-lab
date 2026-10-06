# R7-SUR2 pre-registration (account 2, 6 Oct 2026, addendum to passes/signcmp_r7sur/prereg.md; written and pushed before the call)

Why: R7-SUR's single-sign Sonnet call failed its own control (c2 F1 0.45 < 0.6; c1 F2 0.7). Changed instrument, two knobs at
once as the brief names them: (1) 2-3-sign context tiles (the same 14 boxes widened 45 native px each side, 3x, red marker over
the centred sign; `cut_ctx_tiles.py`, `images/crops_r7sur2/`, seed 20261007, `blind_key.json`), (2) an Opus reader (Agent tool,
model opus), 1 call, blind: no values, codes or words, labels only Q1-Q6 / R1-R8.
Known confound, stated before the call: q1 (L08:51) and q2 (L10:30) sit in the same word ("noo_e"), so their context tiles show
the same neighbours; the reader is told to judge only the marked sign. Any Q-Q grouping of q1 with q2 is therefore not evidence.

Questions, answers, rule: identical to R7-SUR's prereg (best R or none, 0-1 confidence, runner-up; Q-Q same-form groups).

## Gate (unchanged threshold)
c1 -> an F2 ref (rl1/rl2) at >= 0.6 AND c2 -> an F1 ref (rg1/rg2) at >= 0.6. Otherwise non-test, no token changed.

## What each answer changes (only on gate PASS) -- unchanged from R7-SUR's prereg
q1/q2 -> F2 >= 0.6: no change (l H stands). -> F1 >= 0.6: token downgraded to M g|l (value l kept, exceptions row, grade M);
never a new H value from an image call. Otherwise no change. q3/q4: descriptive only (one sign vs two look-alikes; which
class the shape resembles), no exceptions row, no value change (both stay M under GAPS23's rule).

## On gate FAIL (brief's rule 3 clause)
This is the second attempt at this question with the sign-tile instrument family. Logged "[retired] instrument (sign tiles,
LLM blind read) for this question" only if every control number moved the wrong way relative to R7-SUR: c1's F2 confidence
< 0.7 (or c1 matched a non-F2 ref) AND c2's F1 confidence < 0.45 (or c2 matched a non-F1 ref). Otherwise logged "non-test",
not retired, and stop.

decode_key --check exit 0 after any change; 2077 before H 538 C 10 M 61 U 49.
