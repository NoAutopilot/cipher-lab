# PREREG MONL-C269C (20 Oct 2026, 11:2x UTC by date -u; account 2, Opus): PREREG v3 for c269 (f.138v), a generic span rule tested prospectively on L23-L33

Written and pushed before any c269 L23-L33 fetch, read, decode or score. PREREG-MONL-C269A.md (d8b8c1d1f) and PREREG-MONL-C269B.md
(a690865da) hold for crops, passes, reconciliation conventions, statistic, control and grading letters, except what this file names.
Why v3: MONL-C269B's span clause was typed from MONL-C269A's reported span end ("start on f.140v L03 or L04") and failed by one line
(L11-L22 start f.140v L02) while the content placement beat its control widely (0.647 vs p95 0.425, 0/200). Re-registering a clause for
L11-L22 after seeing it would let the data choose the rule, so the rule below is generic and is tested first where nobody has looked:
c269 L23-L33.

**Bands.** B1 = c269 L01-L10 (c269_reconciled.tsv, graded by MONL-C269A), B2 = L11-L22 (c269b_reconciled.tsv, read, ungraded),
B3 = L23-L33 (c269c_reconciled.tsv, to be read here).

**Span rule (generic, mechanical; `c269/span_rule.py`, committed with this file).** Clear lines numbered in reading order over
clear_f140.tsv (f.140r L01 = 1 ... f.141r L11 = 67). For band K: prev_end = the clear line of the last clear letter a band K-1 token takes
in ONE joint alignment (align_c268.py's DP, scores, folds, key.tsv unchanged) of bands 1..K-1 concatenated, against the clear letter
after c268's own aligned end, free start and end; indep_start = the clear line of the first clear letter a band K token takes when band
K alone is aligned against the whole clear letter (free start; score_c269.py's whole-letter span). PASS iff |indep_start - prev_end| <= 1.
Chance level for a uniformly placed start: 3/67 = 0.045.
Design note, before any L23-L33 data: a first draft took prev_end from the joint alignment of bands 1..K (band K included, so it could
revise band K-1's end). Its own specificity check passed a wrong band (c268 L01-L10 placed after c269 L01-L10: delta 1, PASS), because
band K dragged band K-1 to itself; prev_end is therefore taken without band K. Span-rule calibration as committed (`span_rule.py --calib`):
power c268 L21-L30 after c268 L01-L20 delta 0 PASS; power c269 L01-L10 after c268 L01-L30 delta 0 PASS; wrong band c268 L01-L10 after
c269 L01-L10 delta -26 FAIL.

**Score window for B3 (computed now, from committed B1+B2 only):** `span_rule.py --bands c269_reconciled.tsv,c269b_reconciled.tsv
--window-only` -> B2 joint end f.140v L10, window **f.140v:L09-f.141r:L11** (from prev_end - 1 to the letter's end). Statistic and control
unchanged: `score_c269.py c269/c269c_reconciled.tsv --window f.140v:L09-f.141r:L11` (confirm share of keyed tokens, 200 placed-shuffled
windows, seed 2690); also L23-L28 and L29-L33 apart, f.139 other-letter control.

**Calibration before the B3 score (placed-shuffled instrument, committed tokens):** power = c268 L21-L30 against f.140r:L19-f.141r:L11
must pass the gate (MONL-C269A: 0.650 vs p95 0.417); wrong window = c269 L01-L10 against f.140v:L04-f.141r:L11 must FAIL (MONL-C269B:
0.408 vs p95 0.418). If either misbehaves: stop, non-test, no grades. The span-rule calibration above must reproduce too.

**Crops and passes.** One openapi.bnf.fr native region on f269 below the L11-L22 region (y from ~3250), levelled as regen_monlc269b.sh
(rotation -2.3 deg, per-segment centres from the row ink profile, +-95 px, s1 x 0-1700, s2 x 1400-2510), `tools/iiif_lines.py --debug`
overlay checked, top-band identity checked against L22 (the overlap). Two blind passes, strongest model, one call per 5-6 lines per pass
(4 calls: A L23-L28, A L29-L33, B L28-L23, B L33-L29; B reversed), MONL-C269B's prompts with paths and lines changed. Reconciliation by
reconcile_c269b.py's rules into c269/c269c_reconciled.tsv before any decode or clear text is looked at for L23-L33. If the band holds
fewer than 11 cipher lines (the closing clear line apart), the band is what is there.

**Gate for B3.** PASS iff B3 real > placed-shuffled p95 AND 0/200 draws at or above it AND the span rule passes for K = 3
(`span_rule.py --bands c269_reconciled.tsv,c269b_reconciled.tsv,c269c_reconciled.tsv`).

**Decision rule.** Grade B3 only if it passes. Then, and only then, apply the identical rule to B2: span rule for K = 2
(`span_rule.py --bands c269_reconciled.tsv,c269b_reconciled.tsv`) plus the placed-shuffled score of B2 on its rule-computed window
(`span_rule.py --bands c269_reconciled.tsv --window-only`), same gate; grade B2 if it passes too. If B3 fails, grade neither, and the
B2 rule verdict is not computed here.

**Grades (if any band passes).** align_c269.py extended to one joint alignment of B1+B2+B3 after c268's own aligned end (B2 tokens stay
in the stream for placement even if B2 is not graded); C where the aligned clear letter equals the table letter and the clear word is
unbracketed, M otherwise, U unkeyed with no fill (no fills); grades written only for B1 and the bands that passed. B1's grades come from
the same joint alignment (its L10 tail was stretched in MONL-C269A's B1-only alignment); every B1 grade change is counted and reported.
decode.json job c269 as now; `tools/decode_key.py . --check` passing; target C/M/U before and after. key.tsv unchanged (only the target's
--try rules may change it; none run here).

## Decision
Belief: c269 L23-L33 are the cipher of the clear text from about f.140v L10 to the letter's end, continuing L11-L22 without a gap
Would change it: B3 at or below the placed-shuffled p95 on f.140v:L09-f.141r:L11, any of 200 draws at or above it, or |indep_start - prev_end| > 1 lines
Observed: <pending>
Decision: <pending>
Lesson: <pending>
