# PREREG TXE4-4 SELF-CHECK (account 3, Fable 5.1 worker, session_018VT8VUvHJFdoz3ymcCoQAm, 12 Oct 2026 01:2x UTC by date -u; pushed BEFORE any read or score)

One of the TXE4 experiments the account-3 parent launched on 12 Oct 2026 (brief `.claude/briefs/runs/2026-10-11-acct3-txe4-4.md`,
commit 93b7bb321; TXE4-0 REPAIR landed at 6f84c5af, the R4a prerequisite). Question: can ONE blind reading check itself -- a
classifier trained only on that reading's own signs at the boxes of the page's OTHER lines, calibrated once on dev truth, flags and
flips the signs that look unlike their siblings -- and does the flip rule fix more of pass A's errors than it breaks on held-out
lines? The brief's common TXE4 rules R1-R10 bind. Read-free: no reader, no vision call, no subagent, no network beyond git, no owner
evidence, no labels.json in any tested arm. Truth and flags are opened only by `tools/tx_bench.py` (scoring) and by the new
`tools/tx_selfcheck.py fit` subcommand, which imports `tx_bench.read_tsv`/`align`/`is_flagged` and reads ONLY the no.87 truth
rows of the dev_tune lines (f178v L01-12) to fit the isotonic map -- the same declared exception as TXE4-9's `tx_calibrate.py
feedback`. The f152r truth and the eval_heldout truth rows are never read outside tx_bench. No *.truth.tsv, flags or BENCHMARK-TX.tsv
row is edited; the frozen confirm items are never opened; nothing is published, nobody contacted.

## Hypothesis
H1: a leave-one-line-out kNN on pass A's own labels (no truth, no other reader, no owner), with an isotonic calibration fitted on
dev_tune and a flip rule frozen on dev_tune, fixes more pass-A position errors than it breaks on the eval pool (no.87 eval_heldout +
f152r), by the gate below, and beats a shuffled-label chance null.
H0 (a result): it does not -- a classifier trained on A's own labels learns A's systematic misreads (the ceiling stated in the brief:
it can only catch A's INCONSISTENT reads, never a sign A misreads the same way everywhere) and at this N the inconsistent share of
A's errors is too small to clear the gate, or the flips break as many as they fix.
Ceiling: pass A on eval_heldout is 18/376 position errors (0.048) and on f152r 6/73 (0.082): neither is near ceiling. The pool holds
about 24 pass-A errors. The classifier can at best fix the subset of those where A read the same shape differently elsewhere on the
page; every error A makes consistently is out of reach by construction.

## Nearest prior (register rows) and what differs from them
- TXE3-7 PROPAGATE (`benchmark-tx/txeng3/7/RESULTS.md`, RESCORE.md, rescored on the label-aware map a4ccb93d1): a kNN trained on
  SIBLING-leaf tiles (machine or owner labels) that overrode the line read fixed 0 / broke 0 (machine) and 0 / 4 (owner, p 0.125)
  on no.87 -- it never fixed a sign. Differs: the training labels here are the SAME pass's own reads on the SAME page (own ink),
  not sibling leaves; the override is gated by a calibrated probability on both the candidate AND the current sign, not by a
  unanimous vote; and the join is made by `tools/box_token_align.py` with the shift check and bound (R4a), never the old map.
- TXE2-PAIR2 X2b (`benchmark-tx/txeng2/pair2/RESCORE.md`): own-ink training, dev 3 fixed / 1 broken (p 0.63) after the map fix --
  the right direction, under the gate. Differs: X2b was one confusion pair with a pair model; this is every sign, one kNN.
- TXE3-10 PAIR (`benchmark-tx/txeng3/10/RESULTS.md`, RESCORE.md): a T18/T98 topology discriminator, eval 6 fixed / 0 broken, p 0.031
  on the corrected tiles (verifier's ruling on the upgrade pending). Differs: hand-built pair features on one pair with a pooled
  training set that included owner and dev-truth tiles; here no owner, no truth tile trains anything, and the features are
  `glyph_atlas.py`'s own HOG+PCA ("today's features"; TXE4-3's A2 setting has not landed at 01:2x UTC, so it is not used).
- TXE2-CONF X4 (`benchmark-tx/txeng2/conf/RESULTS.md`): the READER's own top-3 probabilities were miscalibrated (ECE 0.159, truth in
  the top-3 at 3 of 12 errors). Differs: this calibrates the MACHINE's vote share, not the reader's self-report, on the same dev
  lines, and reports ECE on dev and eval.
- TXE3-4 CALIB (NULL): err_2reader cannot see the agreed-wrong half; retired as a predictor. This job's check looks at the tile, not
  at agreement; err_2reader is not used anywhere.
- MQS-CLASSIFY-ROUNDS (`glyph_atlas.py --train-labels`, weak): sibling-sorted piles did not move no.87 because its kNN neighbours are
  its own tune tiles. That finding is the premise here: the useful neighbours are the page's own tiles, so train on them.
Retired instruments named in R4 (':' mark rule, transcribe-and-decode crossword, look-alike pass as accuracy, exemplar compare layout,
M24 feature-first, err_2reader as predictor) are not used. The forbidden joins (atlas/no87_box_token.tsv, txeng3/7/f152r_box_token.tsv,
txeng/compare/box_pos.tsv, pair/*/box_pos.tsv, the width-DP copies) and the forbidden inputs (labelaware map's sorter labels,
labels.json, owner piles, settled_labels, owner_map, passX20*, key_pins.tsv, L74 oracle answers, confirm items) are not opened by any
arm. `benchmark-tx/txeng/compare/box_pos_bta.tsv` (TXE4-0) is also not used: it is steered by L's labels, and the arm must see only
pass A. prior_work.py: not run as a gate -- this is a benchmark re-scoring of committed passes on existing benchmark items, not an
item step (the tool answers "item 'no87' is not a row of items.tsv"; TXE4-0 and TXE4-9 did not run it either); logged here.

## Fixed inputs (frozen now; nothing below changes after a number is seen)
- Pass A, no.87: `benchmark-tx/outputs/birago1572-no87/passA.tsv` (f178r L01-03, f178v L01-23, f179r L01-03; Sonnet, 2 Oct 2026),
  with the unit files `benchmark-tx/txeng/units/passA_dev_tune.tsv` (f178v L01-12, 343 scored, 21 position errors as measured) and
  `passA_eval_heldout.tsv` (f178v L13-23 + f179r L01-03, 376 scored, 18 position errors).
  Pass A, f152r: `benchmark-tx/outputs/birago1572-f152r/passA.tsv` (Opus, L01-L04, 95 tokens; 6/73 as measured).
  Pass B (`passB.tsv` of each item), passC (no.87) / passZ_pipeline (f152r) and L (`labels_*.tsv`) are BESIDE only.
- Atlas: `ciphers/nevers-birago-fr3251-1572/atlas/{signs.tsv,bitmaps.npz}` (4,209 tiles, 18 pages). Features: `glyph_atlas.feats`
  on the whole atlas, pca_scale unit, size_w 3.0 (HOG 9x(8x8)x(2x2) -> StandardScaler -> PCA 40 -> unit scale, + 3 x log rh, log rw),
  fitted unsupervised on all tiles, imported from tools/glyph_atlas.py unchanged. kNN k = 5, weights 1/(d + 1e-6), pool 40 for the
  top-3 ranking (glyph_atlas's own vote). No label of any kind enters the features.
- Atlas line <-> read line: no.87 f178r/f178v/f179r read L<nn> = atlas line nn (as `atlas/no87_map.py` and TXE4-0's box_pos_bta use;
  f178r included, per line, with the per-line gate deciding whether it stands). f152r read L01-L04 = atlas lines 2-5 with the
  geometric prose bounds of `txeng3/7/rescore/map_f152r_la.py` (L01 centre x > 2520, L04 centre x < 2460; geometry only, no label).
- Joins (R4a, step 2 of the brief, with the declared change below): per item, round 1 = `box_token_align.build_map` at lam 0 (width
  only, seed only); a LOLO kNN on pass A's labels at the round-1 1:1 boxes gives every box of the item a top-3 (the line being
  classified never trains); round 2 = build_map with those top-3 as labels (k1 1.0, k2/k3 0.5), lam 1.5, neutral 0.5, loo on;
  check labels = the same top-1 (steered -> leave-one-out row) through `tools/join_check.py evaluate` (B1/B2/B3, 20 permutations,
  seed 20261012). A box enters the arm only if it is op 1:1 at the same position in BOTH rounds, on a line that PASSES B1 (per line)
  with the whole-item verdict PASS. FAIL: drop the failing lines, list them, re-check once; still FAIL -> nothing from that item is
  scored. UNCHECKABLE -> that item is a declared non-test. The rows and verdicts are pasted in the addendum below and in RESULTS.
  DECLARED CHANGE from the brief's step 2a/2b: the brief seeds the item maps with a kNN trained on SIBLING-leaf tokens (two rounds
  on the sibling harvest reads). No truth-free file on disk joins the sibling harvest passages (L01, R02, V01, L04.1 ...) to atlas
  lines -- `atlas/secure_tokens.py`'s join runs through labels.json, which step 2 forbids -- and building that correspondence is a
  unit of its own that the 120-minute box does not hold beside the tool build. R4a allows "--topk or the brief's own kNN": the
  steering labels here are the brief's own kNN (pass A, other lines, LOLO), which is at least as independent of a line's own read as
  a sibling kNN, and the leave-one-out check row is what the gate reads. The sibling-seeded map is the named next step, not run.
- Classifier (step 3): per item, for each line, a kNN on pass A's signs at the kept 1:1 boxes of the item's OTHER lines (all three
  no.87 pages are one item; f152r's three other lines for f152r). Output per box: k1..k3, 1/d-weighted vote shares s1..s3, nearest
  distances d1..d3, and for pass A's own sign at that box its share s_A and nearest distance d_A (0 share, d_A = none when A's sign
  is absent from the pool).
- Calibration (step 4): score u(c) = share(c) + 0.25 x m(c), m(c) = (d_other - d_c) / (d_other + d_c) with d_other the nearest
  distance of the best candidate other than c (m in [-1, 1]; an absent candidate has share 0 and m = -1). Isotonic regression (pool-
  adjacent violators, increasing) of y = [k1 in the truth set at that position] on u(k1) over the unflagged scored dev_tune 1:1
  boxes joined to truth by tx_bench.align (G 0.75, truth sets); applied as a step function with linear interpolation between knots.
  The same map f gives p1 = f(u(k1)) and pA = f(u(A's sign)). Fitted once, written to benchmark-tx/txeng4/4/calib_fit.json, never
  refitted. ECE (10 equal-width bins on p1) is reported on dev and on eval, beside.
- Flip rule (step 5): A' = A with sign <- k1 at a kept 1:1 box when p1 >= tau AND pA <= eps (k1 != A's sign follows, since f is
  monotone and tau > eps). Grid frozen: tau in {0.6, 0.7, 0.8, 0.9} x eps in {0.05, 0.1, 0.2}. Choose on dev_tune the setting with
  the maximum net (fixed - broken, position McNemar vs pass A, as measured) subject to broken <= 1; ties -> the larger tau, then the
  smaller eps. STOP before eval if dev net <= 0 at every setting (declared reading: dev-FAIL, the own-ink check cannot catch A's
  slips on this hand at this N).
- Tool: new `tools/tx_selfcheck.py` (subcommands map / classify / fit / apply / null), offline test `tools/tests/test_tx_selfcheck.py`
  (LOLO never trains on the classified line; the isotonic map is monotone; the flip rule respects tau and eps). The brief's
  `glyph_atlas.py classify --self-labels/--calibrate` options are NOT added to the shared tool in this job: R7 (siblings touching
  tools/glyph_atlas.py this hour) and the box; tx_selfcheck.py imports glyph_atlas's feature code so the features are the shared
  ones, and the option is named as a follow-up in RESULTS. The run arguments are committed as benchmark-tx/txeng4/4/run.sh.

## Arms
- A (base): pass A as committed.
- A' (target): pass A with the frozen flip rule applied to its kept 1:1 boxes, classifier trained on A's own labels (LOLO).
- Control (a), the gate's chance null: pass A's labels permuted across the item's kept 1:1 tiles (within the item, seeds 1-20)
  before training; the same LOLO kNN, the same frozen f, the same frozen (tau, eps). Fixed and broken counted per seed.
- Control (b), beside: random flips of pass A to the classifier's top-2 (k1 if k1 != A else k2) at the same count as the real arm's
  flips, on randomly chosen kept 1:1 positions, seeds 1-20.
- Beside, not gated (run only if the box allows, in this order): A' vs passC on eval_heldout (non-inferiority, 15/376 as measured);
  the same frozen rule applied to pass B (its own map and own-label classifier) and to L.

## Endpoint
`tools/tx_bench.py --item <item> --exclude-flagged --paired <pass-A unit file> [--coverage-diagnostic for no.87 eval_heldout]`
on A' restricted to the unit's lines: err_true as measured AND flagged-excluded with Wilson 95% (never the second alone), unit-cost
edits and S/D/I, --strict beside; the paired position McNemar fixed / broken / exact two-sided p vs pass A. no.87 eval_heldout
(376) and f152r (73) each reported separately AND pooled (fixed and broken summed; exact two-sided binomial p on the pooled counts).

## Gate
PASS iff pooled fixed > broken against pass A with exact two-sided p < 0.05, AND the real pooled net (fixed - broken) exceeds the
95th percentile of control (a)'s pooled net over its 20 seeds. Otherwise FAIL (dev-FAIL if stopped before eval). Power:
tools/tx_power.py on the pool (pass A eval_heldout + f152r) at fix 0.3 and 0.5, alpha 0.05, quoted in RESULTS (PREREG-txeng2-0's
audit gives about 0.9 for a clean 30% fixer at p < 0.05 on a pool of this size).

## Controls and why they can vary
(a) Permuting A's labels across the tiles changes every vote, so the top-1, p1, pA and therefore the set of flipped positions
differ from the real arm's; its fixed and broken can be anything from 0/0 to many/many. It is the shuffled-label chance null R4a
requires for a classifier arm, and it sits inside the gate. (b) Random flips at the real count can fix a position only by chance
(the top-2 at an error position holds the truth some of the time), so its net is the chance net of flipping that many signs. Both
are counted BEFORE any truth is read for the real arm's score (their outputs are committed with sha256 in the same prescore list).
Neither control is identical to the target by construction: the statistic (fixed/broken at flipped positions) depends on the labels
(a) and on which positions are flipped (b).

## Units, stop rule, declared readings
Box 120 min from the claim (01:19 -> 03:19 UTC), unit-start limit 02:55 UTC; cap USD 15, running-estimate limit USD 12 (Fable floor
about 9-10 + units). Units and estimates (brief): map with shift checks 25 min, tool build 35 min, dev grid 10 min, eval and scoring
15 min. A unit is not started if it would cross the limit.
- Only the map unit done (no classifier): "map built and checked; untested" -- no result, the join rows are the deliverable.
- Map + tool + dev grid, no eval (box or STOP rule): "dev-FAIL" if dev net <= 0 everywhere, else "dev result only, eval not
  looked" with the dev numbers; no eval look is spent, LOOKS.tsv gains no row.
- Eval scored: PASS or FAIL by the gate above; a FAIL with the real net above control (a)'s p95 but p >= 0.05 is "weak at this N",
  never a pass. A null is a result.
- An item whose join FAILs after the re-check or is UNCHECKABLE: non-test for that item; the gate is then read on the other item
  alone and said so.

## Addendum (filled before step 3 runs; join rows pasted verbatim)
(appended below, in the commit that lands the maps, before any classification is scored)

## Addendum (01:3x UTC 12 Oct 2026 by date -u, before step 3): join rows and verdicts, pasted from the sidecars
`tools/tx_selfcheck.py map` (round 1 lam 0 -> LOLO kNN on the round-1 tokens -> round 2 lam 1.5 loo -> join_check on the
leave-one-out positions, check labels = the steering top-1, 20 permutations, seed 20261012). Kept = 1:1 at the same position in
both rounds on a line that passed B1. Columns: placed, matches at 0/-1/+1/+-2/none, line verdict, kept of tokens (boxes).

**birago1572-no87 (pass A)**: leave-one-out n 773: {'0': 639, 'none': 117, '+1': 5, '-1': 6, '+-2': 6}; share0 0.827 (null p95 0.049), share+-1 0.014 (bound 0.093); B1 True B2 True B3 True; in-sample {'0': 648, 'none': 117, '+1': 4, '-1': 2, '+-2': 6}; **VERDICT PASS**; dropped lines: none; kept 616 boxes.

```
f178r_L01: placed 25 11/0/0/0/14 PASS | kept 17 of 31 (33 boxes)
f178r_L02: placed 31 18/1/2/0/10 PASS | kept 30 of 31 (31 boxes)
f178r_L03: placed 19 15/0/0/0/4 PASS | kept 0 of 26 (46 boxes)
f178v_L01: placed 26 21/0/0/1/4 PASS | kept 26 of 27 (28 boxes)
f178v_L02: placed 26 21/0/0/1/4 PASS | kept 26 of 27 (28 boxes)
f178v_L03: placed 25 21/0/0/0/4 PASS | kept 25 of 26 (27 boxes)
f178v_L04: placed 27 24/0/1/0/2 PASS | kept 27 of 28 (29 boxes)
f178v_L05: placed 29 23/0/0/0/6 PASS | kept 29 of 31 (33 boxes)
f178v_L06: placed 27 24/0/0/1/2 PASS | kept 21 of 30 (30 boxes)
f178v_L07: placed 27 27/0/0/0/0 PASS | kept 25 of 30 (32 boxes)
f178v_L08: placed 28 22/0/0/0/6 PASS | kept 28 of 30 (32 boxes)
f178v_L09: placed 26 21/1/0/0/4 PASS | kept 12 of 29 (29 boxes)
f178v_L10: placed 29 21/1/1/0/6 PASS | kept 28 of 32 (32 boxes)
f178v_L11: placed 27 23/0/0/0/4 PASS | kept 8 of 32 (31 boxes)
f178v_L12: placed 31 29/0/0/0/2 PASS | kept 31 of 32 (33 boxes)
f178v_L13: placed 27 24/0/0/0/3 PASS | kept 2 of 29 (28 boxes)
f178v_L14: placed 27 24/0/0/1/2 PASS | kept 27 of 27 (27 boxes)
f178v_L15: placed 28 26/0/0/0/2 PASS | kept 28 of 30 (29 boxes)
f178v_L16: placed 29 26/0/0/0/3 PASS | kept 29 of 31 (30 boxes)
f178v_L17: placed 27 24/0/0/0/3 PASS | kept 13 of 29 (28 boxes)
f178v_L18: placed 27 24/0/0/0/3 PASS | kept 27 of 27 (27 boxes)
f178v_L19: placed 28 24/0/0/0/4 PASS | kept 28 of 29 (30 boxes)
f178v_L20: placed 26 22/0/0/0/4 PASS | kept 26 of 27 (28 boxes)
f178v_L21: placed 23 20/0/0/0/3 PASS | kept 6 of 27 (27 boxes)
f178v_L22: placed 28 22/0/0/1/5 PASS | kept 28 of 28 (28 boxes)
f178v_L23: placed 29 23/1/0/1/4 PASS | kept 28 of 29 (29 boxes)
f179r_L01: placed 25 20/1/0/0/4 PASS | kept 22 of 31 (37 boxes)
f179r_L02: placed 26 24/0/0/0/2 PASS | kept 12 of 31 (33 boxes)
f179r_L03: placed 20 15/1/1/0/3 PASS | kept 7 of 27 (31 boxes)
```

**birago1572-f152r (pass A)**: leave-one-out n 84: {'0': 41, 'none': 36, '+-2': 4, '-1': 3}; share0 0.488 (null p95 0.072), share+-1 0.036 (bound 0.180); B1 True B2 True B3 True; in-sample {'0': 42, 'none': 37, '+-2': 4, '-1': 2}; **VERDICT PASS**; dropped lines: none; kept 74 boxes.

```
f152r_L01: placed 7 5/0/0/0/2 PASS | kept 7 of 7 (7 boxes)
f152r_L02: placed 28 11/1/0/3/13 PASS | kept 23 of 30 (32 boxes)
f152r_L03: placed 31 14/1/0/1/15 PASS | kept 31 of 33 (35 boxes)
f152r_L04: placed 18 11/1/0/0/6 PASS | kept 13 of 25 (29 boxes)
```

Both items PASS on the leave-one-out row; no line failed B1; no re-check needed; both items are scored. Coverage note (declared
before any score): the "1:1 in both rounds" rule drops most boxes on the lines the width-only seed shifts (no.87 f178v L09, L11,
L13, L17, L21, f179r L02, L03; f178r L03 entirely), so the classifier reaches 616 of 845 no.87 tokens and 74 of 95 f152r tokens;
a pass-A error on an unreached token cannot be fixed and is counted as such in the paired score (it stays wrong in A' as in A).
