# PREREG MONL-C269B (20 Oct 2026, 10:2x UTC by date -u; account 2, Opus): addendum to PREREG-MONL-C269A.md (d8b8c1d1f)

Written and pushed before any c269 L11-L22 fetch, read or score. Everything in PREREG-MONL-C269A.md holds (crops, passes, reconciliation
rules, statistic, control, gate shape, grading rules) except what this addendum names.

**Question.** Are c269 (f.138v) lines 11-22 the cipher of the clear text continuing from where c269 L10 placed (f.140v L03, "...beaucoup
de faulte quil aye de lar-")?

**Line range.** c269 L11-L22 (12 lines). One openapi.bnf.fr native region on f269 below the L01-L10 region, levelled the same way
(rotation from left/right ink-profile peaks, centre +-95 px, s1 x 0-1700, s2 x 1400-2510, cut before the gutter), `tools/iiif_lines.py
--debug` overlay checked first; top-band identity checked against the L10 band (overlap with the old region).

**Passes.** Two blind passes, strongest model, one call per 6 lines per pass (4 calls: A L11-L16, A L17-L22, B L16-L11, B L22-L17, pass B
reversed), MONL-C269A's prompts with paths and line labels changed. Reconciliation by c269/reconcile_c269.py's rules (agree -> H; split
-> folder conventions or eye, M) into c269/c269b_reconciled.tsv, before any decode or clear text is looked at for these lines.

**Statistic (registered).** `c269/score_c269.py c269/c269b_reconciled.tsv --window f.140v:L03-f.141r:L11` (expected clear window:
the clear letter from f.140v L03 onward to the end of the letter; draws 200, seed 2690, unchanged). Also: L11-L16 and L17-L22 apart, whole-
letter span, f.139 other-letter control.

**Calibration before the L11-L22 score** (same script, committed tokens): wrong window = c269 L01-L10 (c269_reconciled.tsv, committed)
against f.140v:L04-f.141r:L11 must FAIL the gate (its own clear ends at f.140v L03); power = MONL-C269A's run (c269 L01-L10 against
f.140r:L26-f.141r:L11, 0.509 vs p95 0.422) re-run and reproduced. If the wrong window passes or the power run does not reproduce, stop:
non-test, no grades.

**Gate.** PASS iff the L11-L22 real share is above the control p95 AND 0/200 draws are at or above it AND the whole-letter span starts on
f.140v L03 or L04. Otherwise: no grades for this range, no fold into decode.json.

**If PASS: grades.** c269/align_c269.py extended: L01-L10 aligned exactly as now (their grades unchanged); L11-L22 aligned against the
clear letter after c269 L10's own aligned end (no clear letter counted twice), same C/M/U rules, same votes rule; written into the same
decode.json job c269 outputs. key.tsv unchanged (only the target's --try rules may change it, none run here). Counts before/after (C/M/U).

## Decision
Belief: c269 L11-L22 are the cipher of the clear text from f.140v L03 onward
Would change it: L11-L22 at or below the placed-shuffled p95, any of 200 draws at or above it, or the whole-letter span not starting at f.140v L03-L04
Observed: calibration wrong window FAIL (c269 L01-L10 vs f.140v:L04-f.141r:L11 0.408 vs p95 0.418, 39/200), power reproduced (0.509 vs p95 0.422, 0/200); pass agreement 292/358 = 0.816; L11-L22 0.647 vs placed-shuffled p95 0.425 (mean 0.403, max 0.443, 0/200), L11-L16 0.677 vs p95 0.453 (0/200), L17-L22 0.616 vs p95 0.451 (0/200), f.139 0.398; whole-letter span f.140v L02 - L10 (registered: start L03 or L04)
Decision: stop -- gate NOT met as registered (span clause): no grades, no fold into decode.json; control beaten by a wide margin, so the placement is put to the parent as a re-registration question, not graded here
Lesson: a span clause typed from the previous band's reported span inherits that band's end error; register the span relative to the previous band's own aligned end, computed by the script, and let the next band's placement be able to revise that end
