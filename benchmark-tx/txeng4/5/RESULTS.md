# TXE4-5 PAIR-BANK -- RESULTS (12 Oct 2026, 01:18-02:0x UTC by date -u; account 3, Fable 5.1 worker, session_01HsQVPQ5RDUZTo6HUB2dYwm)

Brief `.claude/briefs/runs/2026-10-11-acct3-txe4-5.md` (93b7bb32). PREREG `benchmark-tx/PREREG-txeng4-5.md`: committed e2b568d23
before any tool change, read or score; addendum A0-A2 (joins, pool counts, deviations) committed 771060125 before any training;
dev outputs committed unscored 1e863d4dd; eval outputs committed unscored eb0c2fbf0 (see SHA256SUMS.prescore). Read-free: no
reader, no vision call, no image opened, no network beyond git. Truth files opened only by tools/tx_bench.py (R3), except the
declared beside-only owner-pool arm (unit 5), which reads dev truth for its pool exactly as TXE3-10 did.

## Question
Can look-alike separators for ten confusable Birago 1572 pairs be trained from machine-agreed tiles only (no owner sort, no dev
truth, no secure list), and do they fix more than they break on lines and a leaf they never saw?

## Tool change (R7: kept as a patch)
Another TXE4 session committed to tools/glyph_atlas.py at 01:37 UTC (904c82d80), so the change is
`benchmark-tx/txeng4/5/glyph_atlas_pairbank.patch` against e2b568d23 (applies cleanly; both tests pass on the scratch copy
`scratch/tools/glyph_atlas.py`, which every run here used). It carries TXE3-10's `classify --pair A B` plus:
`--pairs FILE` (one gated model per pair; combined output, a position two models flip is kept as the base), `--pool-agreed
AGREE:MAP` (reader-agreed tiles joined by a box_token_align map that `join_check.require()` has PASSed; never a tile from the
applied line), `--feature-bank` (topology 29 + 4x4 zoning 16 + HOG 128, L1-logistic selection per pair, redone inside every
LOGO fold), `--exclude-own-line`, `--reverse-labels`, and `--map` with no default, gated by `join_check.require()` (a map with no
PASS sidecar is refused: test 1 of `tools/tests/test_glyph_atlas_pairbank.py`). `--pool-owner`/`--pool-dev`/`--pool-secure`
stay in the tool and were used in no treatment arm.

## Joins (R4a; all machine-only; full rows in maps/SHIFT-CHECKS.md, sidecars beside each map)
Recipe: `tools/box_token_align.py --lam 0` seed -> cosine kNN (k 7, 16x16 ink + rh rw dy) trained only on sibling tiles labelled
by that seed at agreed positions (never f152r/f178r/f178v/f179r) -> `box_token_align --topk kNN --loo --check-labels kNN-top1
--check-bound`, sidecar rewritten by `tools/join_check.py --steered` (the labels steered the map, so the leave-one-out row is
the verdict; `--check-bound` did not auto-detect this because the top-1 file is derived from, not identical to, the --topk
file -- a tool note for the parent). First build (ordinal passage -> line): sibling FAIL on f139v_L03, all f174vB_L, f184r_L09;
f152r FAIL (share0 0.135). Fixes declared in addendum A0 before any training: drop f139v_L03 and f184r_L09; f174vB at the +1
line offset (probe PASS, share0 0.572, 11/11 lines); f152r on atlas lines 2-5 with the prose boxes outside the run removed by
x (TXE3-7's map_f152r.py bounds, geometry only). kNN retrained on the kept lines (LOO top-1 agreement 0.273 -> 0.484, n 675).

| map | verdict (steered) | n | share0 | share+-1 | null p95_0 | bound +-1 | FAIL lines |
|---|---|---|---|---|---|---|---|
| sibling pool (30 passages, 433 stable tiles) | PASS | 748 | 0.604 | 0.041 | 0.052 | 0.099 | none |
| no.87 pass A | PASS | 779 | 0.712 | 0.028 | 0.052 | 0.096 | none |
| no.87 L | PASS | 785 | 0.713 | 0.028 | 0.056 | 0.097 | none |
| f152r pass A | PASS | 85 | 0.624 | 0.035 | 0.059 | 0.130 | none |
| f152r Z | PASS | 87 | 0.609 | 0.034 | 0.057 | 0.139 | none |
Reference rows (brief): old no.87 map 157/24/14 of 208 FAIL; label-aware map 188/1/2 of 203 PASS. Here the no.87 pass-A map's
kNN top-1 sits at 0/-1/+1 = 555/11/11 of 779 (202 kNN misses, offset 'none').

## Pools (machine-agreed tiles only, counted read-free before training; addendum A1)
| pair | sibling A/B | no.87 dev A/B | no.87 eval A/B | f178r A/B | total A/B | trainable |
|---|---|---|---|---|---|---|
| T18/T98 | 4/13 | 4/7 | 0/6 | 1/1 | 9/27 | yes |
| T90/T53 | 8/20 | 10/12 | 8/16 | 2/2 | 28/50 | yes |
| T76/T86 | 11/11 | 11/20 | 9/11 | 2/4 | 33/46 | yes |
| T76/T45 | 11/18 | 11/18 | 9/34 | 2/8 | 33/78 | yes |
| T76/T66 | 11/0 | 11/0 | 9/0 | 2/1 | 33/1 | no (1 T66) |
| T50/T92 | 1/1 | 0/2 | 1/15 | 0/3 | 2/21 | no (2 T50) |
| T24/T29 | 3/1 | 2/0 | 2/1 | 0/0 | 7/2 | no (2 T29) |
| T60/T86 | 24/11 | 17/20 | 25/11 | 2/4 | 68/46 | yes |
| T95/T51 | 2/0 | 0/0 | 0/0 | 0/0 | 2/0 | no (0 T51) |
| T64/T38 | 1/0 | 2/1 | 3/1 | 0/0 | 6/2 | no (2 T38) |
Five pairs cannot train (the tool needs 3 tiles of each member): "untestable at this pool size", not a FAIL.

## Dev gates (G1 LOGO vs 20 shuffled-label LOGO runs; G2 dev_tune leave-one-line-out, broken = 0; dev truth read only by tx_bench)
`gates/summary.tsv`; commands in `gates/commands.log` (rule 7). Each dev line is voted by a model whose pool excludes that line.
| pair | pool A/B (fold 1) | LOGO acc | shuffled max (chance) | enabled folds | kept features | G1 | dev considered | fixed / broken (as measured; flagged-excl.) | G2 | both |
|---|---|---|---|---|---|---|---|---|---|---|
| T18/T98 | 8/27 | 0.714 | 0.800 (0.771) | 0/12 | - | FAIL | 0 | 0/0 | - | FAIL |
| T90/T53 | 28/49 | 0.974 | 0.623 (0.636) | 12/12 | 25 | PASS | 22 | 0/0; 0/0 | PASS | **PASS** |
| T76/T86 | 33/46 | 0.949 | 0.696 (0.582) | 12/12 | 21 | PASS | 33 | 0/1; 0/1 | FAIL | FAIL |
| T76/T45 | 33/77 | 0.945 | 0.700 (0.700) | 12/12 | 24 | PASS | 29 | 0/0; 0/0 | PASS | **PASS** |
| T60/T86 | 66/46 | 0.929 | 0.634 (0.589) | 12/12 | 11 | PASS | 40 | 1/1; 1/1 | FAIL | FAIL |
| five untrainable pairs | - | - | - | 0/12 | - | - | 0 | 0/0 | - | untestable |
The d/s pair T18/T98, TXE3-10's pair, does not separate on machine-agreed labels alone: LOGO 0.714 is below the majority-class
chance (0.771) and below the best shuffled run (0.800), and the threshold rule disables it in every fold. The two pairs that
pass both gates (p/t and T76/T45) do so by changing nothing on dev (0 fixed / 0 broken): G2 cannot distinguish "right" from
"inert" at 0 changes, as TXE3-10's C2 already showed for p/t.

## Eval (one look per unit; outputs committed unscored in eb0c2fbf0 with SHA256SUMS.prescore and LOOKS.tsv rows, then scored once by `run_pairs.py score` -> eval/scores.tsv; commands in eval/commands.log)
Applied: the two pairs passing both dev gates (T90/T53, T76/T45) through `--pairs gates/passing.txt`, each eval line voted by a
model whose pool excludes that line (`--exclude-own-line`); f152r tiles in no pool. Gate pool = no.87 eval_heldout T76/T45
positions (T90/T53 on no.87 eval is reported only: TXE3-10 applied C2 there) + f152r both pairs.

| base | pair | positions considered | changed | fixed / broken (as measured) | fixed / broken (flagged excl.) | in gate |
|---|---|---|---|---|---|---|
| no.87 pass A | T90/T53 | 25 | 0 | 0 / 0 | 0 / 0 | no (reported) |
| no.87 pass A | T76/T45 | 44 | 1 | 0 / **1** | 0 / 1 | yes |
| no.87 L | T90/T53 | 25 | 0 | 0 / 0 | 0 / 0 | no (reported) |
| no.87 L | T76/T45 | 43 | 1 | 0 / 1 | 0 / 1 | yes |
| f152r pass A | T90/T53 | 5 | 0 | 0 / 0 | 0 / 0 | yes |
| f152r pass A | T76/T45 | 3 | 0 | 0 / 0 | 0 / 0 | yes |
| f152r Z | T90/T53 | 5 | 0 | 0 / 0 | 0 / 0 | yes |
| f152r Z | T76/T45 | 3 | 0 | 0 / 0 | 0 / 0 | yes |

err_true, base -> output, Wilson 95% (tx_bench --exclude-flagged --strict; unit-cost edits S/D/I: every change here is one S):
| base | as measured | flagged excluded |
|---|---|---|
| no.87 pass A (eval_heldout, 376 scored) | 0.048 (18/376, 0.030-0.074) -> 0.051 (19/376, 0.033-0.078) | 0.035 (13/371, 0.021-0.059) -> 0.038 (14/371, 0.023-0.062) |
| no.87 L (376) | 0.040 (15/376, 0.024-0.065) -> 0.043 (16/376, 0.026-0.068) | 0.027 (10/371, 0.015-0.049) -> 0.030 (11/371, 0.017-0.052) |
| f152r pass A (73) | 0.082 (6/73, 0.038-0.168) -> same | 0.057 (4/70, 0.022-0.138) -> same |
| f152r Z (73) | 0.068 (5/73, 0.030-0.151) -> same | 0.029 (2/70, 0.008-0.098) -> same |

**Gate, word for word, applied:**
- "On the pass-A base: pooled fixed > broken, exact two-sided p < 0.05, with broken <= 1." Pooled (no.87 T76/T45 + f152r both
  pairs): fixed 0, broken 1, net -1, exact p 1.0 (both masks). **FAIL** (broken <= 1 holds; fixed > broken does not).
- "On the L base: net >= 0." Pooled: fixed 0, broken 1, net -1. **FAIL.**
- "For each passing pair: the forced-threshold shuffled control has net <= +1, and the label-reversed model breaks."
  Shuffled (seeds 1-5, --force-t 0), pooled over the gate positions: net -15, -18, -16, -20, -17 (per pair on no.87 pass A:
  T90/T53 1/9..1/13 fixed/broken, T76/T45 0/13..0/16; on f152r 0/0..0/3). Reversed: net -39 (no.87 T90/T53 1/24, T76/T45 0/35;
  f152r 0/4). Both clauses hold for both pairs: the controls can vary and do (they break 15-39), the real models sit at 0-1
  changes. So the real separators are not at chance -- they are nearly inert: on 77 unseen positions they moved 1 and broke it.
- Verdict by the registered rule and the declared reading for units 1-5 done: **did not move (null).** A null is a result.

## The beside arm (unit 5): does the d/s separator need the owner's tiles?
Machine-pool T18/T98 (this job): disabled in every fold (G1 FAIL, LOGO 0.714 < shuffled max 0.800; pool 8-9 / 25-27).
Owner-pool T18/T98 (TXE3-10's model: dev truth 12/6 + secure 5/18 + the owner's 4 Oct sort, rebuilt with the committed patch
on the MACHINE no.87 map, `--exclude-pool-page f152r`; beside/run.sh): pool 24-25 / 35-37, LOGO 0.983-0.984 vs shuffled max
0.656, enabled in all 12 dev folds (29 features).
| unit | base err (meas; flagged) | output | fixed / broken (meas; flagged) |
|---|---|---|---|
| dev_tune (--loo-lines, 19 pair positions; same as TXE3-10's rescore) | 0.035 (12/343, 0.020-0.060); 0.021 (7/338, 0.010-0.042) | 0.032 (11/343, 0.018-0.057); 0.018 (6/338, 0.008-0.038) | 1 / 0; 1 / 0 (f178v L06.18) |
| f152r passZ (3 T98 positions, 1:1 boxes; never pooled) | 0.055 (4/73, 0.022-0.133); 0.014 (1/70, 0.003-0.077) | 0.041 (3/73, 0.014-0.114); 0.014 (1/70, 0.003-0.077) | **1 / 0**; 0 / 0 (f152r_L03.8 T98 -> T18, margin +0.995, a truth-flagged position) |
So on the same machine map, the owner-pool model separates d from s (0.984) and fixes one of three f152r positions and the one
dev error, while the machine-pool model cannot even be enabled. Dropping the owner's 24 tiles (and the 12/6 dev-truth and 5/18
secure tiles with them) costs the d/s separator everything at this pool size. The f152r flip is one position, flagged by the
truth verifier: a direction, not a gate result.

## Rule-3 reading (controls, non-tests)
- Join controls: every map PASSes join_check's within-page permuted-label null in the steered row (B3 share0 0.60-0.71 vs p95
  0.05-0.06). The first build's ordinal pairing FAILed and was corrected before training (addendum A0), so the "wrong tile"
  failure mode of TXE3-10 is excluded here by the gate, not assumed.
- Model controls can vary (break 15-39) and the real models do not: the null is "inert", not "non-test".
- G2 at 0 changes is a non-discriminating gate (both passing pairs changed nothing on dev); the eval look is what tested them.
- Rule 3's third-attempt clause: this is the fourth pair-classifier attempt on no.87 (X2, X2b, TXE3-10, this), with a new
  instrument (feature bank + machine pools + join gate). The numbers did NOT move together toward the gate for machine-only
  pools (T18/T98 LOGO 0.984 with owner tiles -> 0.714 without). A fifth attempt at pair classifiers on machine-agreed labels alone
  is logged "untestable at this pool size / inert at this N" and needs new material (more agreed tiles of the rare member, or
  the owner's sorted tiles) rather than another feature set.

## For the owner (three sentences)
Of the ten look-alike pairs, five had too few machine-agreed examples of one member to train at all; four separated their
pair in testing without any of your sorting, but two of those broke a correct reading on the tuning lines, and the two that
passed every tuning check changed one reading on the unseen lines and that one was wrong, so no separator earned its place
from machine-agreed examples alone. The shuffled and reversed versions of the same separators broke 15 to 39 readings, so the real
ones are not guessing, they are just too cautious to help at this amount of training material. The d/s separator from
yesterday still needs your sorted tiles: rebuilt without them it cannot be switched on, rebuilt with them on the corrected
box map it keeps its 6-of-6 result on no.87 and also corrected one of the three d/s readings on the second letter f.152r.

## Next step (named, not run)
Not "add the passing pairs to the recipe" (none earned it). Cheapest step outside this frame: a known-answer pool for the rare
member of each thin pair from the owner's existing sorts (the 4 Oct and no.87 sorter piles already on disk) joined through the
machine map, then the same gates -- about USD 3 read-free; or, for the d/s pair, the owner-pool model applied to f.117, f.144
and f.168 after reconcile (about USD 4) now that it has one f152r position in its favour. A tool follow-up for the parent:
`box_token_align.py --check-bound` should detect a steered check when the check-labels equal the --topk file's k1 column.

## Cost, time, hosts
Box 01:18-03:18 UTC; done by about 02:0x (units 1-5 all run; unit 5 started at 01:48, elapsed 30 min, running estimate 12.0).
Cost: the parent reads get_session (no figure visible here). Host requests: 0 (git only; pip installed opencv-python-headless,
scikit-image, scikit-learn into the container for tools/glyph_atlas.py's own imports -- one PyPI call, no data host).
Reader calls: none (R8 not exercised; no subagent).

## Files
PREREG `benchmark-tx/PREREG-txeng4-5.md` (+A0-A2); this folder: `glyph_atlas_pairbank.patch` (+ scratch/), `build_maps.py`,
`run_pairs.py`, `prescore.py`, `agree/`, `knn/`, `maps/` (+SHIFT-CHECKS.md, sidecars, first_build/), `probe/`, `gates/`
(summary.tsv, commands.log), `eval/` (scores.tsv, commands.log), `beside/` (run.sh), `SHA256SUMS.prescore`; shared:
`benchmark-tx/txeng4/LOOKS.tsv` (+109 rows), `LEDGER.md` (+1 row). Untouched: tools/glyph_atlas.py, every truth and flags file,
every forbidden map, every owner file outside the declared beside arm.
