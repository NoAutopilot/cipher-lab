# TXE4-6 TIEBREAK -- RESULTS (12 Oct 2026, 01:18-01:5x UTC by date -u)

Worker TXE4-6 (account 3, Fable 5.1, session_01H8mDJE4tM3AC15746vPvQh), brief `.claude/briefs/runs/2026-10-11-acct3-txe4-6.md`
(93b7bb321). PREREG `benchmark-tx/PREREG-txeng4-6.md` (d22f86db, before any read or score). Read-free: no reader call, no
vision call, no network beyond git; 0 requests to any host. Truth opened only by tools/tx_bench.py and by `dev_sweep.py` through
tx_bench.align on the dev lines (declared). Every output hashed in `SHA256SUMS.prescore` before its score (1a1091ee6, 9f68a6c7c,
53f12b027). No truth or flags edited, no confirm item, no owner page, nothing published.

**Verdict: gate FAIL (null result).** Pooled over no.87 eval_heldout (376) + f152r (73), the agreed-tile tiebreak fixed 2 and
broke 2 scored positions against the committed Sonnet adjudication (exact two-sided p = 1.0, both masks); its net (0) beats the
permuted-label null's 95th percentile (-1; mean -3.2), so the agreed ink carries real information, but as-measured err_true rose
on f152r (6/73 vs 5/73). On no.87 dev_tune (safety only, declared) it moved the right way: fixed 6 / broken 1 (p 0.125). Gunther is
a non-test for this instrument (see unit 1). The committed adjudicator already sits at the oracle-adjudication bound on the Birago
eval rows, so there was little to fix there.

## Three sentences for the owner
1. A free check of a disputed sign against the signs both readers agreed on elsewhere on the same page did NOT settle the readers'
   disagreements better than the paid third reader: on the held-out Birago lines it fixed 2 positions and broke 2.
2. The numbers: no.87 held-out 14/376 errors against the adjudicator's 15/376 (fixed 2, broken 1); f152r 6/73 against 5/73 (fixed 0,
   broken 1); pooled p = 1.0; a shuffled-label control averaged 3 positions worse, so the check is not noise, just not better than
   the adjudicator; on the tuning lines it was better (6 fixed, 1 broken), which did not carry over.
3. The adjudication call cannot be dropped on this evidence; on Gunther (the second hand) the machine could not even place a box on
   7 of the 11 disputed signs, so the question is untested there.

## Unit 1 -- boxes and maps (own-page two-round recipe for all three items; PREREG Deviation 1)
`build_maps.py` (0001de9fc). Per item: `reconcile_passes.py A B --method nw`; the draft is the read; round 1 `box_token_align`
lam 0 (seed only); train labels = round-1 1:1 boxes at agreed columns (A == B, not L); `glyph_atlas.py classify
--only-train-labels --topk 3 --knn 5 --page all` (a box never votes for itself); round 2 lam 1.5, own-label leave-one-out, check
labels = that kNN's top-1 (steered -> leave-one-out positions) through `join_check.evaluate`; tiles kept = 1:1 at the same
(line, pos) in both rounds. No sorter status, seed, settled label, owner map or labelaware map was read.

| item | reconcile | round-1 ops | train tiles | join check (steered, leave-one-out) 0 / -1 / +1 / +-2 / none of n | verdict | tiles kept | split rows / reachable / boxed |
|---|---|---|---|---|---|---|---|
| no.87 (f178r, f178v, f179r) | 852 draft signs, agree 777/852 = 91.2%, 75 disagreement columns | 1:1 783, 2:1 90, 1:2 22 | 717 | 634 / 8 / 5 / 7 / 118 of 772; share0 0.821 (null p95 0.058), share+-1 0.017 (bound 0.091); every line passes B1 | **PASS** | 588 of 762 1:1 | 75 / 66 / 45 (0.68) |
| f152r (atlas lines 2-5 = L01-L04, txeng3/7 x-bounds) | 96 draft signs, agree 90/96, 6 columns | 1:1 90, 2:1 12 | 84 | 51 / 2 / 0 / 2 / 30 of 85; share0 0.600 (null p95 0.059); share+-1 0.024 (bound 0.130) | **PASS** | 79 of 84 1:1 | 6 / 5 / 4 (0.80) |
| gunther L01-L17 (fresh segment, 353 boxes on 17 crops, `--median-h pool`) | 13 disagreement columns (rec_gun as TXE3-3) | 1:1 164 | 93 | attempt 1 FAIL: g05, g06, g10, g16 fail B1; attempt 2 (13 lines) 55 / 6 / 6 / 6 / 44 of 117, share0 0.470 (null p95 0.129), share+-1 0.103 (bound 0.240) | PASS after drop | 86 of 116 1:1 | 13 / 11 / **4 (0.36 < 0.70)** |

Per-line rows are in the unit-1 commit's stdout and `map_<item>.tsv.joincheck.json`. Gunther: fewer than 70% of its reachable
split rows got a 1:1 box kept in both rounds (the segmenter cuts a joined German secretary hand into 353 pieces for about 250
signs, and the four lines carrying most splits failed B1) -> STOP for gunther as the brief says; it is not pooled and not scored
by the tiebreak. Its reference figures stay those of TXE3-3/VERIFY (passC 14/214, oracle 8/214).

## Unit 2 -- the tool
`tools/tx_tiebreak.py` (c65c73c8b), shipped as its own tool (PREREG Deviation 3: reconcile_passes.py has no image or atlas input).
At each A != B row with both candidates non-blank: d(c) = mean distance (glyph_atlas classify features, HOG + PCA(40) + log size,
'unit' scaling, fitted on the item's atlas) to the min(5, available) nearest agreed tiles of class c on OTHER lines of the page;
margin m = (d_far - d_near) / d_near; the nearer class is written when m > t; no box, no tile of one class, or a base gap keeps
the base. The map must carry a join_check PASS sidecar (`require()`). `--permute-seed` permutes the agreed labels within the
page (control a); `--coin-seed --coin-from` flips a coin at the target's own applied rows (control b). Test
`tools/tests/test_tx_tiebreak.py` (4 cases: planted splits settled, margin above every row writes nothing, permuted labels change
picks and the coin lands only on applied rows, a map without a checked join is refused). `tools/tx_bench.py --pair A B` (same
commit, fix 1a1091ee6: truth set only, as position_errors), test `test_tx_bench.py::test_pair`. TXE3-10's topology features are
not on main (Deviation 2) and were not used.

## Unit 3 -- pair report (read-free; `pair_report.txt`)
| item | mask | scored | both right | agreed-wrong | both-wrong-different | one-reader-wrong (A only / B only) = reachable share | A wrong / B wrong | oracle-adjudication bound (Wilson 95%) |
|---|---|---|---|---|---|---|---|---|
| no.87 (whole, 29 lines) | as measured | 803 | 716 | 32 | 5 | 50 (15 / 35) = 0.062 | 52 / 72 | 37/803 = 0.046 (0.034-0.063) |
| no.87 | flagged excluded | 792 | 716 | 23 | 3 | 50 (15 / 35) = 0.063 | 41 / 61 | 26/792 = 0.033 (0.022-0.048) |
| f152r | as measured | 73 | 67 | 3 | 0 | 3 (2 / 1) = 0.041 | 5 / 4 | 3/73 = 0.041 (0.014-0.114) |
| f152r | flagged excluded | 70 | 67 | 1 | 0 | 2 (2 / 0) = 0.029 | 3 / 1 | 1/70 = 0.014 (0.003-0.077) |
| gunther L01-L17 | as measured | 214 | 199 | 7 | 1 | 7 (5 / 2) = 0.033 | 13 / 10 | 8/214 = 0.037 (0.019-0.072) |
| gunther L01-L17 | flagged excluded | 206 | 199 | 1 | 0 | 6 (4 / 2) = 0.029 | 5 / 3 | 1/206 = 0.005 (0.001-0.027) |

The gunther row reproduces VERIFY-3's re-derivation exactly (A 13 / B 10 sign errors, 8 shared of which 7 flagged, 7 one-reader
events, oracle 8/214 as measured and 1/206 flagged-excluded). On no.87 the committed passC (41/803) is already within 4 of the
oracle bound (37/803): the adjudicator took the right reader at 46 of the 50 one-reader-wrong positions.

## Unit 4 -- dev (no.87 dev_tune, f178v L01-L12; safety only; `dev_sweep.txt`)
35 reachable split rows on dev; 21 decided at t = 0 (20 on scored truth positions). Tiebreak right 18/20 = 0.900 at t = 0; the
committed adjudicator right at the same 20 rows 13/20 (TXE-K's 35/36 is item-level against the better of A/B, not against truth);
coin 0.500. Agreement with the committed adjudication: same 13, override 8 (overrides right 6/8, one override broke a right base).
Sweep: t = 0.00 decided 20 (coverage 0.60) accuracy 0.900; 0.05 -> 19 (0.57) 0.947; 0.35 -> 11 (0.31) 0.909; 0.40 -> 8 (0.23) 1.000.
**Frozen t = 0.00** (the smallest t with accuracy >= 0.90 at coverage >= 0.30), so the target arm T equals the replacement arm R.
Dev paired score (safety, beside): fixed 6 / broken 1, p 0.125; unit-cost edits 19 -> 14 of 343 as measured, 14 -> 9 of 338 flagged
excluded (`eval_tx_bench.txt`).

## Unit 5 -- eval (`summary.txt`, `eval_tx_bench.txt`, `eval.json`, `eval_eh.json`)
Scored with `tools/tx_bench.py --exclude-flagged --paired <base> --strict` (no.87 subsets with `--coverage-diagnostic`). Overrides
written on no.87: 12 of 37 picked rows (8 on dev lines, 4 on eval lines: f178v L19.6, L19.16, L19.24, L20.15); f152r: 1 (L03.32).

| unit | mask | T = R err_true (Wilson 95%) | base err_true | unit-cost edits base -> T (S/D/I) | fixed / broken, exact p | strict err_true T |
|---|---|---|---|---|---|---|
| no.87 eval_heldout (f178v L13-23 + f179r, 376) | as measured | 14/376 = 0.037 (0.022-0.062) | 15/376 = 0.040 | 15 -> 14 (14/0/0) | 2 / 1, p 1.0 | 3/376 |
| no.87 eval_heldout | flagged excluded | 9/371 = 0.024 (0.013-0.045) | 10/371 | 10 -> 9 | 2 / 1, p 1.0 | 3/371 |
| no.87 eval 17 lines incl. f178r (460) | as measured | 21/460 = 0.046 (0.030-0.069) | 22/460 | 22 -> 21 | 2 / 1, p 1.0 | 3/460 |
| no.87 eval 17 lines | flagged excluded | 15/454 = 0.033 (0.020-0.054) | 16/454 | 16 -> 15 | 2 / 1, p 1.0 | 3/454 |
| f152r (73) | as measured | 6/73 = 0.082 (0.038-0.168) | 5/73 = 0.068 | 4 -> 5 (5/0/1) | 0 / 1, p 1.0 | 2/73 |
| f152r | flagged excluded | 3/70 = 0.043 (0.015-0.119) | 2/70 | 1 -> 2 | 0 / 1, p 1.0 | 2/70 |
| no.87 whole item (beside) | as measured | 35/803 = 0.044 (0.032-0.060) | 41/803 = 0.051 | 41 -> 35 | 8 / 2, p 0.109 | 12/803 |
| no.87 whole item | flagged excluded | 24/792 = 0.030 (0.020-0.045) | 30/792 | 30 -> 24 | 8 / 2, p 0.109 | 11/792 |
| no.87 dev_tune (safety) | as measured | 14/343 = 0.041 | 19/343 | 19 -> 14 | 6 / 1, p 0.125 | 9/343 |

Controls (20 seeds each, same t = 0, pooled net = fixed - broken over no.87 eval_heldout + f152r, identical under both masks):
- (a) permuted agreed-tile labels: net per seed [-2, -6, -1, -2, -3, -3, -3, -4, -1, -4, -5, -2, -3, -3, -3, -4, -2, -8, -2, -3],
  p95 -1, mean -3.20. It varied (the brief's requirement): permuting which agreed tile carries which label changes which
  candidate is nearer, hence the overrides. The real labels' net (0) sits above every seed.
- (b) coin flip at T's own applied rows and count: net per seed mean -0.65 (range -2 to 0).
- (c) the committed adjudicated output is the base.

Gate, word for word, on the registered pool (no.87 eval_heldout 376 + f152r 73; gunther non-test, not pooled):
- "pooled fixed > broken against the committed adjudicated output, exact two-sided p < 0.05": fixed 2, broken 2, p = 1.0000 -> **FAIL**.
- "AND the real net > the 95th percentile of control (a)": 0 > -1 -> PASS.
- "AND as-measured err_true is not higher on any of the three items": no.87 14/376 vs 15/376 (not higher); f152r 6/73 vs 5/73
  (**higher**); gunther untested -> **FAIL**.
Verdict: **FAIL** (null). The same three lines on the 17-line no.87 set (460) give the same answer. Beside: the replacement arm
R is the same output (t = 0).

Eval looks (R6): LOOKS.tsv rows for this job: birago1572-no87 eval_heldout 1 (no87_R.tsv 368e7916...), birago1572-f152r 1
(f152r_R.tsv 4a32280d...); TXE4 rows on these units before this job: 0 (TXE4-3's row is dev_tune). 11 Oct TXE3 looks: TXE3-7 and
TXE3-9 on the whole of no.87, TXE3-10 on no.87 eval_heldout, TXE3-7 on f152r, TXE3-3 on gunther. Gunther: no look taken here.

## Reading
The page's own agreed ink separates the readers' look-alike pairs well enough to beat a shuffled label (every permuted seed is
worse than the real labels), and on dev it reaches 0.90 decided accuracy and a 6 / 1 paired count -- the same right-way dev signal
X2b and TXE3-10 saw from own-ink classifiers. It does not carry to the held-out lines (2 / 1) or to f152r (0 / 1), and the reason is
in the pair report: on no.87 the committed Sonnet adjudication is already within 4 positions of the oracle-adjudication bound
(41 vs 37 of 803), so a tiebreak has almost nothing left to fix, and the few eval overrides are as likely to break as to fix. The
owner's time is not touched by this result. Under rule 3's third-attempt clause this is the first attempt of this instrument;
it is logged dev-right-way / eval-null, not retired.

## Next step (not run)
- Not the wiring the brief named (it did not pass). The read-free census the brief named is cheap and informative: run
  `tx_bench.py --pair` over every committed pass pair on BENCHMARK-TX (about USD 2) to answer the second-reader-diversity question
  (how often the reachable share is worth a third reader at all; on these three items it is 3-6% of scored positions with the
  adjudicator already near the oracle bound).
- For gunther, the instrument needs a box map first: a segmenter for a joined secretary hand (TXE3-6's --split-wide, or a
  cursive-mode strip pass) and a re-run of unit 1's join check; about USD 4, read-free.

## Costs and requests
Cost: from the parent's get_session (cap USD 15; estimate 12). Box 01:20-03:20 UTC; done well inside it. Requests per host: 0
(pip install of scikit-learn, scikit-image and opencv-python-headless from PyPI through the container proxy, one call, is the only
network use). Shared tools touched: tools/tx_bench.py (--pair, additive; last other commit on it 00:37 UTC, outside the one-hour
rule), new tools/tx_tiebreak.py; glyph_atlas.py, reconcile_passes.py, box_token_align.py and join_check.py unchanged.
