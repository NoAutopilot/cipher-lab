# TXE2-SORT: X6 sorter value curve + X20 owner decisions on file (LANE TX-ENGINEER-2, 9 Oct 2026)

Worker TXE2-SORT (account 4, Opus 5.5) for LANE TX-ENGINEER-2; PREREG `benchmark-tx/PREREG-txeng2-1.md` X6/X20 (S4
measurement, no gate). Read-free: no vision call, no reader; the benchmark truth is used only as the oracle inside
`tools/tx_sorter_curve.py` and through `tools/tx_bench.py`. **The eval_heldout curves below are read-free simulations, not
eval looks**: no instrument was scored on eval_heldout, and the X20 eval figure was not taken (the lane takes it).
err_true here is wrong-or-deleted / scored positions (`tx_bench.position_errors`; insertions are not position-level).
`x` = flagged truth rows excluded (`--exclude-flagged`), `m` = as measured; both are on file, never one alone.

## X6 -- how many owner decisions to reach 2%?

Tool `tools/tx_sorter_curve.py` (test `tools/tests/test_tx_sorter_curve.py`). L = `benchmark-tx/outputs/birago1572-no87/labels.tsv`;
box<->position map `atlas/no87_box_token.tsv` (sid, line, pos, op; its truth column is never read; 1:1 boxes only);
clusters `atlas/clusters.tsv` (140-cluster deliberate over-split). Orderings: (a) tx_doubt n_signals descending,
(b) cluster size descending (one representative per cluster nearest its centroid first), (c) random, 10 seeds,
(d) greedy oracle (upper bound within the propagation model). k = 0..200. Files: `curve_birago1572-no87_<unit>_<mode>_<x|m>.tsv`
and `summary_<unit>_<mode>_<x|m>.json`; regenerate with the loop in this folder's git history commit message / the
command block at the end.

Propagation models: **cluster** = the PREREG rule (first decision on an atlas cluster sets every undecided tile of the
cluster on the unit); **pile** (added, labelled as an addition) = the cluster's tiles whose current sign equals the shown
tile's; **none** = per tile. Measured cluster impurity on no.87 (683 scored 1:1 tiles in 92 clusters): only 77.3% of tiles
carry their cluster's majority value, 31 of 92 clusters are value-pure -- so whole-cluster propagation overwrites up to
~155 minorities against 17-27 baseline errors.

Decisions-to-2% (k; "nr" = not reached by k=200) and errors removed by the first 10 / 20 decisions (negative = net
broken). Random: seeds reaching 2% out of 10 (range of k) and mean removed at 10 / 20 (band at 20).

| unit | base | mode | (a) doubt | (b) size | (c) random | (d) oracle |
|---|---|---|---|---|---|---|
| dev_tune x | 7/338 0.021 | cluster | nr; -8 / -6 | nr; -20 / -33 | 0/10; -11.5 / -21.5 [-37,-11] | 1; 4 / 4 (stops at 4) |
| dev_tune x | | pile | 1; 0 / 2 | 70; 0 / 0 | 10/10 (8-67); 0.2 / 0.4 | 1; 7 / 7 |
| dev_tune x | | none | 1; 3 / 5 | -- | 10/10 (8-67); 0.2 / 0.4 | 1; 7 / 7 |
| dev_tune m | 12/343 0.035 | cluster | nr; -11 / -9 | nr; -20 / -33 | 0/10; -15.2 / -24.0 [-41,-18] | nr; 5 / 5 (stops at 5) |
| dev_tune m | | pile | 99; 0 / 2 | 190; 0 / 0 | 6/10 (133-195); 0.2 / -0.2 | 6; 8 / 8 |
| dev_tune m | | none | 17; 4 / 6 | -- | 6/10 (125-183); 0.3 / 0.8 | 6; 10 / 12 |
| eval_heldout x | 10/371 0.027 | cluster | nr; -31 / -49 | nr; -46 / -55 | 1/10 (k=1); -19.1 / -34.8 [-68,-20] | 1; 7 / 7 |
| eval_heldout x | | pile | 3; 6 / 6 | 196; 0 / 0 | 10/10 (1-145); 1.1 / 1.5 | 1; 9 / 9 |
| eval_heldout x | | none | 16; 2 / 3 | -- | 9/10 (36-172); 0.3 / 0.6 | 3; 10 / 10 |
| eval_heldout m | 15/376 0.040 | cluster | nr; -31 / -49 | nr; -46 / -55 | 0/10; -21.6 / -34.2 [-60,-24] | 4; 9 / 9 |
| eval_heldout m | | pile | 47; 6 / 6 | nr; 0 / 0 | 9/10 (40-184); 0.8 / 1.5 | 3; 13 / 13 |
| eval_heldout m | | none | 32; 2 / 4 | -- | 7/10 (80-199); 0.5 / 0.8 | 8; 10 / 15 |
| whole x | 17/709 0.024 | cluster | nr; -40 / -50 | nr; -42 / -67 | 0/10; -35.6 / -60.5 [-100,-37] | 1; 9 / 9 |
| whole x | | pile | 5; 8 / 2 | nr; 0 / 0 | 8/10 (29-147); 0.1 / 0.4 | 1; 14 / 15 |
| whole x | | none | 5; 4 / 5 | -- | 8/10 (77-197); 0.1 / 0.4 | 3; 10 / 17 |
| whole m | 27/719 0.038 | cluster | nr; -40 / -53 | nr; -42 / -67 | 0/10; -38.7 / -58.8 [-106,-28] | nr; 12 / 12 (stops at 8) |
| whole m | | pile | 166; 8 / 2 | nr; 0 / 0 | 0/10; 0.2 / 0.5 [-11,5] | 8; 15 / 20 |
| whole m | | none | 44; 4 / 6 | -- | 0/10; 0.5 / 0.8 [0,2] | 13; 10 / 20 |

whole = the 26 mapped no.87 lines (f178v L01-23, f179r L01-03 = dev_tune + eval_heldout); f178r has no box map and its
truth rows are span-excluded, so it is not in any unit here.

dint-f128-print (per tile, no cluster map for f.128: the dint sorter folder is f.23r cards, no tile<->position map for
f.128; no tx_doubt signals, so (a) and (b) not run): base passA 23/85 0.271 -- (d) removes 10 / 20 in the first 10 / 20
decisions, 2% not reached by k=200 (3 errors are not showable: aligned deletions); random 0/10 reach 2%, mean 2.7 / 5.7.
passB 21/85 0.247 -- (d) 2% at k=20; random 10/10 at k=72-84, mean 2.2 / 4.9. Per tile the sorter cannot beat one
decision per error: at a 25% hand that is about one decision per four signs.

Reading (measurement, no gate):
1. **Whole-cluster propagation (the PREREG / TRANSCRIPTION.md item 6 model) is destructive on this atlas.** Every
   non-oracle ordering, on every unit and both truth conventions, ends worse than L: the doubt feed (a) breaks a net 6-53
   positions in its first 20 decisions, size order (b) 33-67, random 21-61. Even the oracle stops after 3-8 decisions with
   errors left, because every remaining fix sits in a cluster whose first decision would break more than it fixes. The
   140-cluster atlas is too impure (77% majority share) to carry a decision to its members unchecked.
2. **Pile x cluster propagation is about neutral, per tile is safe.** With propagation limited to tiles of the same
   current sign, the doubt feed (a) reaches 2% in 1-5 decisions on the x convention (base already 2.1-2.7% on the
   units) and removes 6-8 errors in its first 10 on eval_heldout / whole; size order (b) wastes its first 20 (0 removed).
   Per tile, (a) removes 3-6 of 7-27 errors in 20 decisions; random removes under 1.
3. **The value of the first 20 decisions, doubt feed vs upper bound (x, per tile):** dev 5 of 7 vs 7; eval 3 of 10 vs 10;
   whole 5 of 17 vs 17. The feed's ranking finds about a third to two thirds of what a perfect ranking would in the
   same owner time; on the m convention 4-6 vs 12-20. tx_doubt's recall is the limit, not the number of decisions.
4. Implication for the sorter (not a gate, a suggestion for the lane): never propagate an owner decision to a whole atlas
   cluster on this family; propagate within pile x cluster at most, and show the doubt feed's top tiles first.

## X20 -- the owner's 4 Oct 2026 decisions on top of L for no.87

Script `x20_owner.py` (`--check` regenerates and exits 1 if stale; never reads a truth file). Two sources, both 4 Oct:
- **A, family sort** (`sorter/owner-sort-2026-10-04/`, 488 tiles of f.117 / f.144r / f.168 + 9 corrections). Through
  `tools/sign_sorter_apply.py --atlas-labels` alone it moves no no.87 tile: the save has no `clusters` collection (no
  cluster decision), and its per-tile overrides are the owner's own tiles, none on no.87. Made cluster-level explicitly:
  438 owner tiles placed in atlas clusters via `sorter/no87/owner_map.tsv` (one-to-one boxes); a decision "cluster c:
  F -> C" when >= 2 owner tiles of c started in pile family F and >= 2/3 ended in one other family C. **4 cluster
  decisions** (121: T51->T65 2/2; 60: T65->T80 2/2; 62: T95->T65 2/3; 86: T65->T60 4/5); **1 no.87 position moves**
  (f178v_L01 pos 8, T95->T65, cluster 62).
- **B, no.87 sort** (`sorter/no87/owner-sort-2026-10-04/settled_no87.tsv`, the owner's direct decisions on 248 no.87
  tiles; `moved` rows only, family of the final pile): 21 moved, **5 change L** (f178v_L02 8 T42->T60, L11 20 T19->T24,
  L12 23 X_A->T85, L13 20 T98->T37, L21 13 T85->T60); the rest agree with L or end in a non-T pile.
- Owner split piles are scored at their family (T60-e -> T60): the benchmark scores atlas codes.

Output `benchmark-tx/outputs/birago1572-no87/passX20_owner.tsv` (A + B, all no.87 lines, 6 positions changed; components
`passX20a_family.tsv`, `passX20b_no87sort.tsv`; changes listed in `x20_changes.tsv`).

Dev_tune ONLY (`tools/tx_bench.py <dev lines of the file> --paired benchmark-tx/txeng/units/labels_dev_tune.tsv
--exclude-flagged`; 4 of the 6 changed positions are on dev lines, 2 on eval lines):

| output | err_true as measured | flagged excluded | paired vs L (343) | p |
|---|---|---|---|---|
| L (labels_dev_tune) | 0.035 (12/343) | 0.021 (7/338) | -- | -- |
| passX20_owner | 0.044 (15/343) | 0.030 (10/338) | fixed 0 / broken 3 | 0.25 |
| passX20a_family | 0.038 (13/343) | 0.024 (8/338) | fixed 0 / broken 1 | 1.00 |
| passX20b_no87sort | 0.041 (14/343) | 0.027 (9/338) | fixed 0 / broken 2 | 0.50 |

Prediction registered ("a few positions move; the owner's labels are one strong reader, not truth") held: 6 positions
move, and on dev every scored move breaks a right L sign (one of them, f178v_L02 pos 8, is the TX-TRUTH-VERIFY CORRECT row
where the printed key's T42 = g stands; the owner put that tile in T60-d). Not a null result: the owner's decisions do
touch no.87, at 4 dev positions, all wrong-way or unscored. eval_heldout: written, committed, not scored (the lane's look).

## Regenerate

    A=ciphers/nevers-birago-fr3251-1572/atlas; U=benchmark-tx/txeng/units; D=benchmark-tx/txeng/doubt
    python3 tools/tx_sorter_curve.py --truth benchmark-tx/birago1572-no87.truth.tsv \
      --base benchmark-tx/outputs/birago1572-no87/labels.tsv --lines $U/labels_dev_tune.tsv \
      --map $A/no87_box_token.tsv --clusters $A/clusters.tsv --signals $D/dev_tune_signals.tsv \
      --propagate cluster --exclude-flagged --out benchmark-tx/txeng2/sorter/curve_birago1572-no87_dev_tune_cluster_x.tsv
    (units dev_tune / eval_heldout / whole = both unit files and both signal files; --propagate cluster|pile|none;
    with and without --exclude-flagged; 10 seeds, kmax 200 by default)
    python3 benchmark-tx/txeng2/sorter/x20_owner.py --check
