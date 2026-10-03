# Pre-registration: GAPS-matignon-mayenne-1586 gap 1 (3 Oct 2026, account-4), written and pushed before any scoring

Step: the bMATBEAM beam's second (and last) target attempt, M-only, per leaf, on the seven read-leaves
fr.15572 ff.143r, 143v, 150, 154, 173, 196, 201. Script: `mu_leaf_beam.py` (same LM, same `emit`/`viterbi_line`
and `build_control` as `mu_beam.py`; nothing tuned). U is held fixed as a placeholder (`TOK`: resets the letter
context, costs one average character) on control and target alike; H fixed; each M occurrence chosen among its own
key.tsv candidates by exact per-line Viterbi. Deterministic (no U search, no restarts).

Rendering for the judge (both arms, identical to `judge_leaves.py`): key values per token, M -> the chosen
alternative (baseline arm: the first alternative, as `reading_letters.txt`), U and '*' dropped; judge = the spec's
fr16 model (`specs/matignon-mayenne-1586.json`, catheri01), mean log10 4-gram per letter. Note: the beam LM trains
on catheri01 too, so the judge will reward the beam on any text; the shuffle null below is what controls for that.

**Gate 1 -- known-answer control (A), per leaf (run first).** `build_control` with that leaf's own lines as the
structure (its N, line lengths, H/M/U counts and M candidate sets), held-out catheri02 text, seeds 1, 2, 3.
(a) M-occurrence accuracy, mean of 3 seeds, >= frequency baseline + 0.10 (the bMATBEAM M gate).
(b) Ceiling check (rule 3): the first-candidate baseline accuracy and the frequency baseline are reported; if
either is >= 0.95 the leaf is a non-test. (c) Power of the gain statistic: on each control seed, compute the gain
statistic of gate 2; the leaf is testable only if gate 2's criterion passes on >= 2 of 3 control seeds.
A leaf failing (a), (b) or (c) is "non-test at this N" and its target is not scored. If fewer than 4 of 7 leaves are
testable, the whole step stops: "non-test at this N", beam neither licensed nor retired by this step.

**Gate 2 -- per-leaf judge gain (target, testable leaves only).** gain = judge(beam M) - judge(first-candidate M).
Null: 20 within-line token shuffles of the leaf (seeds 1..20; each M token keeps its own candidates), the same
gain computed on each. Leaf PASS iff gain > max of the 20 null gains AND gain >= +0.010.
Overall PASS iff at least 4 of the testable leaves PASS (and at least half of them). Otherwise FAIL: the beam is
retired for this target (CLAUDE.md rule 3, third-attempt clause; bMATBEAM pooled was attempt 1, bMAT1C commit
attempt 2 by reversal), logged "untested-by-this-tool" for the M values, not refuted.

No value is committed to key.tsv/exceptions.tsv by this step either way; a PASS only licenses a separate
commit-and-judge step with its own control.
