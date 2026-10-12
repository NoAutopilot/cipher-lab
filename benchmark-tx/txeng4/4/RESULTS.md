# TXE4-4 SELF-CHECK -- RESULTS (12 Oct 2026, 01:19-01:4x UTC by date -u; account 3, Fable 5.1 worker, session_018VT8VUvHJFdoz3ymcCoQAm)

PREREG `benchmark-tx/PREREG-txeng4-4.md` (dc3efcd3 before any read or score; the join addendum e2ee38ee before any classification
was scored). Brief `.claude/briefs/runs/2026-10-11-acct3-txe4-4.md` (93b7bb321). Read-free: no reader, no vision call, no subagent,
no network beyond git (0 requests to any other host). No owner evidence, no labels.json, no sibling labels in any arm. Truth opened
only by tools/tx_bench.py and by `tools/tx_selfcheck.py fit`/`ece` on the dev_tune lines (the declared exception). **No eval look
was taken: no eval output exists, LOOKS.tsv gained no row.**

## Verdict (by the registered rules): dev result only, eval not looked -- the frozen choice rule has no feasible setting

The registered selection rule ("maximum dev net subject to broken <= 1") is infeasible: every cell of the frozen grid breaks 3 or
6 correct dev signs. The registered STOP rule ("dev net <= 0 everywhere") did NOT fire (net +3 at every tau >= 0.7), so by the
declared readings this is **"dev result only, eval not looked"**: the gate (pooled eval fixed > broken, p < 0.05, above control
(a)'s p95) was never reached. A null at the choice step is a result; it is not a dev-FAIL in the registered sense and not a pass.

## What was built (tools/tx_selfcheck.py, offline test tools/tests/test_tx_selfcheck.py, 3 cases pass)
- `map`: round 1 `box_token_align.build_map` at lam 0 (width only, seed) -> a leave-one-line-out (LOLO) kNN on the pass's own
  signs at the round-1 1:1 boxes -> round 2 steered by that top-3 (lam 1.5, loo) -> `join_check.evaluate` on the leave-one-out
  positions (check labels = the steering top-1). Kept = 1:1 at the same position in both rounds on a line that passed B1.
- `classify`: LOLO kNN (k 5, 1/d votes, pool 40) with `glyph_atlas.feats` unchanged (HOG -> PCA 40 -> unit + 3 x log size),
  own-sign share/distance beside; `--permute SEED` for control (a). `fit`: isotonic PAV of [k1 in truth set] on
  u = share + 0.25 x distance margin, dev lines only. `apply`: the flip rule (p1 >= tau AND pA <= eps), `--random N` for control (b).
- Not done (R7, declared in the PREREG): the brief's `glyph_atlas.py classify --self-labels/--calibrate` options. TXE4-3 committed to
  tools/glyph_atlas.py at 01:37 UTC (904c82d8) while this job ran; tx_selfcheck.py imports the shared feature code instead and
  reproduces its no.87 classification byte-identically after rebasing onto that commit (checked 01:39 UTC). Adding the two options
  to classify is the named tool follow-up.

## Joins (R4a; rows pasted in the PREREG addendum; sidecars `no87_joincheck.json`, `f152r_joincheck.json`)
| item | round-2 ops | leave-one-out check (0 / -1 / +1 / +-2 / none of n) | share0 vs null p95 | share+-1 vs bound | verdict | kept boxes |
|---|---|---|---|---|---|---|
| no.87 pass A (f178r, f178v, f179r) | 1:1 767, 2:1 74, 1:2 30, unsure 10 | 639 / 6 / 5 / 6 / 117 of 773 | 0.827 vs 0.049 | 0.014 vs 0.093 | **PASS**, every line passes B1 | 616 of 845 tokens |
| f152r pass A (L01-L04, prose bounds) | 1:1 83, 2:1 16, 1:2 2, unsure 2 | 41 / 3 / 0 / 4 / 36 of 84 | 0.488 vs 0.072 | 0.036 vs 0.180 | **PASS**, every line passes B1 | 74 of 95 tokens |
| no.87 pass B (beside) | 1:1 770, 2:1 70, 1:2 36, unsure 10 | 625 / 8 / 5 / 8 / 777 | 0.804 vs 0.055 | 0.017 vs 0.090 | PASS | 611 |
| no.87 L (beside) | 1:1 767, 2:1 84, 1:2 32, unsure 12 | 637 / 7 / 5 / 6 / 775 | 0.822 vs 0.049 | 0.015 vs 0.083 | PASS | 615 |

Coverage cost of the "1:1 in both rounds" rule (declared before scoring): on the lines the width-only seed shifts (f178v L09, L11,
L13, L17, L21; f179r L02, L03; f178r L03) most boxes move between rounds and are not kept, so the no.87 classifier reaches 283 of
the 376 eval_heldout tokens and 286 of the 343 dev_tune scored positions. The reference maps (BOXMAP-LA's label-aware 188/1/2 of
203; old 157/24/14 FAIL) are not comparable in n: this map is checked on 773 own-top-1 labels, not 203 sorter tiles.

## Dev grid (no.87 dev_tune, f178v L01-12; `dev_grid.tsv`; scored by tx_bench --paired vs passA_dev_tune.tsv; Wilson 95%)
Base pass A: as measured 0.064 (22/343) 0.043-0.095; flagged excluded 0.050 (17/338) 0.032-0.079; 21 position errors (16 unflagged).

| tau | eps | flips | fixed | broken | net | exact p | A' as measured | A' flagged excluded |
|---|---|---|---|---|---|---|---|---|
| 0.6 | 0.05 / 0.1 / 0.2 | 15 | 6 | 6 | 0 | 1.0 | 0.064 (22/343) | 0.050 (17/338) |
| 0.7, 0.8, 0.9 | 0.05 / 0.1 / 0.2 | 11 | **6** | **3** | **+3** | 0.51 | **0.055 (19/343) 0.036-0.085** | **0.041 (14/338) 0.025-0.068** |

S/D/I beside: base S 22 D 0 I 0 -> A' S 19 D 0 I 0 (unit-cost edits 22 -> 19). eps never binds: at every kept box where the rule
fires, pass A's own sign is absent from the five voters (sA 0, so pA = 0 by the monotone map); 18 of 286 dev kept boxes are of that
kind. The 12 grid cells collapse to two flip sets (tau 0.6: 15 flips; tau >= 0.7: 11). Choice rule: none feasible (broken 3 > 1).

The 11 flips at tau >= 0.7, labelled after the score (`dev_flips_labelled.txt`): 6 FIXED (T50 -> T92 four times at an 's'; T92 ->
T53 at a 't'; T98 -> T36 at a 'c'), 3 BROKEN (T64 -> T13, T86 -> T85, T86 -> T90: three correct 'e'/'d' signs flipped to a
look-alike the page's other lines happened to vote), 1 both-wrong (T53 -> T65 where truth is T27|T53|T65 -- the set admits T53, so
this one reads as a break under tx_bench, counted above), 1 on a flagged position (not scored).
Reach: of the 15 unflagged dev positions pass A reads wrong (with a token), 13 sit on kept boxes; the classifier's top-1 is in
the truth set at 9 of those 13 (top-3: 10). Consistent misreads (A's wrong sign is also the classifier's vote) on the reachable
set: 0 of 13 -- on this hand pass A's errors are NOT the systematic kind the ceiling argument feared; the own-ink classifier sees
them, and what stops the rule is the breaks, not the reach. The 4 reachable errors it did not flip have p1 under tau (shares
0.31-0.67: T76 -> T26/T36 'e' cases and T98 -> T18).

Calibration: dev ECE 0.001 in sample (154-knot isotonic map on 272 dev boxes, top-1 right 249/272 = 0.915 -- a within-sample
figure, not a calibration result; the eval ECE the PREREG promised was never computed because no eval look was taken). Two fits
exist: `calib_fit_v1_lenient.json` (its truth set admitted the committed reference sign, under-counting dev errors 8 for 15) and
the corrected `calib_fit.json` (the truth column only, exactly tx_bench.position_errors); both grids are identical cell for cell
(`dev_grid_v1_lenient.tsv` = `dev_grid.tsv`), the fix is in the tool's docstring, and it landed before any eval look.

## Controls on dev (at tau 0.8 eps 0.1, the same 11-flip set as every tau >= 0.7 cell; `dev_controls.json`, 20 seeds each)
| arm | flips | fixed (mean) | broken (mean) | net min / mean / p95 / max | seeds with net >= +3 |
|---|---|---|---|---|---|
| real A' | 11 | 6 | 3 | **+3** | -- |
| (a) permuted own labels | 11.0 | 0.00 | 1.45 | -4 / -1.45 / 0 / 0 | 0 of 20 |
| (b) random flips to the top-2, same count | 11 | 0.25 | 9.10 | -11 / -8.85 / -6 / -6 | 0 of 20 |

Both controls can and do vary (nets 0 to -4; -6 to -11). The real dev net (+3) is above control (a)'s p95 (0) and far above (b)'s:
the own-ink classifier carries real signal on dev; the sign test does not reach significance (6 / 3, p 0.51), and the breaks
exceed the registered tolerance.

## Beside (dev only, same frozen fit and rule; never gated)
| base | base dev as measured | after | fixed / broken | flagged excluded |
|---|---|---|---|---|
| pass B (own map, own labels) | 0.093 (32/343) 0.067-0.129 | 0.090 (31/343) | 4 / 3, p 1.0 | 0.080 (27/338) -> 0.077 (26/338) |
| L (labels.tsv) | 0.035 (12/343) 0.020-0.060 | 0.035 (12/343) | 2 / 2, p 1.0 | 0.021 (7/338) -> 0.021 (7/338) |
A' vs passC: not run (eval only). Pass-B and L beside rows use the fit calibrated on A's scores, as "the same frozen rule" says.

## Eval (not looked)
Eval pool power (tools/tx_power.py, pass A eval_heldout 18/376 + f152r 6/73 -> E 23, N 449): clean 30% fixer 0.730, clean 50%
fixer 0.993 at alpha 0.05 (the no.87 unit alone 0.461 / 0.956; f152r alone 0.000 at E 5). TXE4 LOOKS.tsv row count for both
items: 0 (this job spent none). Prior TXE3 looks (11 Oct): TXE3-7 and TXE3-9 on the whole of no.87, TXE3-10 on no.87 eval_heldout,
TXE3-7 on f152r, TXE3-3 on gunther.

## Three sentences for the owner
1. Yes, a single blind reading can see some of its own slips with no second reader: a classifier trained only on that reading's
   signs elsewhere on the page put the right sign first at 9 of the 13 dev errors it could reach, and its flips beat both chance
   nulls -- but it also flipped three correct signs to look-alikes.
2. On the tuning lines it fixed 6 and broke 3 of pass A's reads (0.064 -> 0.055, not significant at this N), and the rule that
   was supposed to protect correct signs (the pass's own sign must look unlikely) never bound, because wherever the rule fires the
   pass's sign had no vote at all.
3. The two-reader step cannot be dropped on this evidence: the pre-registered choice rule allowed at most one break and every
   setting broke three, so no held-out look was taken and the second reader stays.

## Procedural notes (R3, R6, R7)
- Dev outputs (the 12 grid cells, 40 control files, the B and L beside files) were scored by the committed scripts
  (`grid.py`, `dev_controls.py`) in the same run that wrote them and committed afterwards with their sha256 in
  `SHA256SUMS.prescore` -- a deviation from R3's "commit before score" on the DEV (tuning) set only, disclosed here; every file
  regenerates from the committed inputs (`run.sh`), and no eval output was ever written.
- Shared tools: tools/glyph_atlas.py untouched (TXE4-3's 904c82d8 landed mid-job; reproduction after rebase byte-identical);
  tools/box_token_align.py and tools/join_check.py used as library calls, unchanged.
- The brief's step 2a/2b (a sibling-leaf-seeded map) was replaced, as declared in the PREREG before any run, by the brief's own
  kNN (pass A, other lines, LOLO) as the steering labels; the sibling-seeded map is a named next step.

## Next steps (named, not run)
1. The registered rule with a break guard that can bind: require pass A's own sign to be present among the k voters with a
   calibrated p under eps (today pA is 0 by absence at every flip), or raise k to 9 so the own sign can vote; re-register, dev
   first, then one eval look on the same pool (about USD 8 Fable, read-free).
2. Sibling-seeded map (the brief's step 2a/2b) once a truth-free passage-to-atlas-line file exists (about USD 6).
3. `glyph_atlas.py classify --self-labels PASS --box-map MAP` and `--calibrate FIT` as options on the shared tool, once
   TXE4-3's edits have settled (about USD 3, read-free).
4. Only if 1 clears dev with broken <= 1: gunther's single passes (about USD 6) and Vivonne (about USD 6), as the brief names.

## Files
PREREG-txeng4-4.md (with addendum); no87_* and f152r_* (round1, round2, seedtopk, kept, joincheck.json); no87B_*, no87L_* (beside);
topk/ (real, 20 permuted seeds per item, B, L); calib_fit.json, calib_fit_v1_lenient.json; dev/ (12 grid cells + B + L, each with
.flips.tsv); dev_ctrl/ (a_perm1-20, b_rand1-20); dev_grid.tsv, dev_grid_v1_lenient.tsv, dev_choice.json, dev_controls.json,
dev_controls_v1_lenient.json, dev_B.json, dev_L.json, dev_flips_labelled.txt; grid.py, dev_controls.py, run.sh; SHA256SUMS.prescore.
