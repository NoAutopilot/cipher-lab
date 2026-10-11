# TXE2-SORT X6 sorter value curve -- RESCORE (11 Oct 2026, 17:5x UTC by date -u)

**Measurement correction: box-to-position map fixed (off by one), not a new gate look.** (X6 had no gate: S4 measurement.)

Job BOXMAP-RESCORE (others) for the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M). Script-only: no vision call, no reader,
no image viewed, no network beyond git. X20's rescore (same folder) is in RESULTS.md "RESCORE" (job x20-and-9) and is not repeated.

X6 (`tools/tx_sorter_curve.py --map`) puts each atlas box's cluster on a no.87 position through `atlas/no87_box_token.tsv`; the
cluster and pile propagation models then spread a decision to the other tiles of the cluster. That map is one token off on 10 of 26
lines (`ciphers/nevers-birago-fr3251-1572/atlas/RESCORE.md`). **Only `--map` changed** (to `atlas/no87_box_token_labelaware.tsv`):

    bash benchmark-tx/txeng2/sorter/rescore_boxmapLA/run.sh                     # 12 cluster/pile runs -> rescore_boxmapLA/
    python3 benchmark-tx/txeng2/sorter/rescore_boxmapLA/table.py                # the table below, rescore_x6.json
    python3 benchmark-tx/txeng2/sorter/rescore_boxmapLA/impurity.py             # the impurity figure, both maps

With the old map, today's tool reproduces every committed summary's a-d orderings exactly (checked; the tool has since gained
TXE3-1's orders, which add rows to the curve files). The `none` (per-tile) curves never read the map and are unchanged.

## The impurity figure behind reading 1

"Measured cluster impurity on no.87 (683 scored 1:1 tiles in 92 clusters): only 77.3% of tiles carry their cluster's majority value,
31 of 92 clusters are value-pure" -- reproduced exactly by `impurity.py` on the old map. On the label-aware map: **669 tiles in 86
clusters, 94.6% majority share, 63 pure.** Split by line: on the 16 lines the fix did not touch, 94.8% under both maps; on the 10 it
moved, 48.8% under the old map and 94.3% under the new. The atlas clusters were never 77% pure; half the tiles on the shifted lines
were scored against the neighbouring token's letter.

## Curves (decisions to 2%; errors removed by decision 10 / 20; "nr" = not reached by k=200)

| unit | mode | mask | base | (a) doubt before -> after | (b) size before -> after | (c) random before -> after | (d) oracle before -> after |
|---|---|---|---|---|---|---|---|
| dev_tune | cluster | x | 7/338 | nr; -8 / -6 -> **1; 1 / 1** | nr; -20 / -33 -> **14; -1 / -2** | 0/10; -11.5 / -21.5 [-37, -11] -> **1/10; -1.8 / -3.0 [-8, 2]** | 1; 4 / 4 -> **1; 5 / 5** |
| dev_tune | cluster | m | 12/343 | nr; -11 / -9 -> **188; -3 / -3** | nr; -20 / -33 -> **nr; -1 / -2** | 0/10; -15.2 / -24.0 [-41, -18] -> **0/10; -2.8 / -4.7 [-15, 1]** | nr; 5 / 5 -> **6; 7 / 7** |
| dev_tune | pile | x | 7/338 | 1; 0 / 2 -> **1; -1 / 1** | 70; 0 / 0 -> **69; 0 / 0** | 10/10; 0.2 / 0.4 [0, 2] -> **10/10; 0.2 / 0.4 [0, 2]** | 1; 7 / 7 -> **1; 7 / 7** |
| dev_tune | pile | m | 12/343 | 99; 0 / 2 -> **106; -1 / 1** | 190; 0 / 0 -> **188; 0 / 0** | 6/10; 0.2 / -0.2 [-5, 2] -> **6/10; 0.2 / -0.3 [-5, 2]** | 6; 8 / 8 -> **6; 8 / 8** |
| eval_heldout | cluster | x | 10/371 | nr; -31 / -49 -> **1; 6 / 6** | nr; -46 / -55 -> **23; -3 / -3** | 1/10; -19.1 / -34.8 [-68, -20] -> **5/10; -1.5 / -3.1 [-8, 2]** | 1; 7 / 7 -> **1; 9 / 9** |
| eval_heldout | cluster | m | 15/376 | nr; -31 / -49 -> **127; 6 / 6** | nr; -46 / -55 -> **nr; -3 / -3** | 0/10; -21.6 / -34.2 [-60, -24] -> **2/10; -1.5 / -1.7 [-11, 8]** | 4; 9 / 9 -> **2; 12 / 12** |
| eval_heldout | pile | x | 10/371 | 3; 6 / 6 -> **1; 6 / 6** | 196; 0 / 0 -> **23; 0 / 0** | 10/10; 1.1 / 1.5 [-1, 6] -> **10/10; 1.8 / 1.7 [-1, 6]** | 1; 9 / 9 -> **1; 9 / 9** |
| eval_heldout | pile | m | 15/376 | 47; 6 / 6 -> **47; 6 / 6** | nr; 0 / 0 -> **49; 0 / 0** | 9/10; 0.8 / 1.5 [0, 5] -> **9/10; 1.4 / 2.7 [0, 8]** | 3; 13 / 13 -> **2; 12 / 12** |
| whole | cluster | x | 17/709 | nr; -40 / -50 -> **5; 9 / 4** | nr; -42 / -67 -> **6; 1 / 2** | 0/10; -35.6 / -60.5 [-100, -37] -> **1/10; -4.1 / -6.7 [-21, -3]** | 1; 9 / 9 -> **1; 13 / 13** |
| whole | cluster | m | 27/719 | nr; -40 / -53 -> **nr; 9 / 0** | nr; -42 / -67 -> **nr; 1 / 2** | 0/10; -38.7 / -58.8 [-106, -28] -> **0/10; -1.5 / -5.2 [-13, 1]** | nr; 12 / 12 -> **7; 16 / 18** |
| whole | pile | x | 17/709 | 5; 8 / 2 -> **5; 8 / -1** | nr; 0 / 0 -> **nr; 0 / 0** | 8/10; 0.1 / 0.4 [0, 1] -> **7/10; 0.1 / 0.3 [0, 1]** | 1; 14 / 15 -> **1; 14 / 14** |
| whole | pile | m | 27/719 | 166; 8 / 2 -> **173; 8 / -1** | nr; 0 / 0 -> **nr; 0 / 0** | 0/10; 0.2 / 0.5 [-11, 5] -> **0/10; 0.3 / 0.4 [-12, 6]** | 8; 15 / 20 -> **7; 16 / 18** |

Second-order input, reported beside: the tx_doubt signal tables that order (a) also join atlas boxes through the same width DP
(`benchmark-tx/txeng/compare/box_pos.tsv`). Rebuilt on the label-aware map (`benchmark-tx/txeng/rescore_boxmapLA/doubt/`; `run.sh
MAP OUT benchmark-tx/txeng/rescore_boxmapLA/doubt`), (a)'s errors removed by decision 10 / 20 move by at most 2 and its decisions to
2% by up to 14 (whole pile m 173 -> 159) (`rescore_boxmapLA/newsig/`); nothing above changes in kind.

## Does the conclusion change?

**Reading 1 changes.** "Whole-cluster propagation is destructive on this atlas. Every non-oracle ordering, on every unit and both
truth conventions, ends worse than L ... The 140-cluster atlas is too impure (77% majority share)": with the right join the atlas is
about 95% pure, the doubt feed (a) under cluster propagation removes 6 of eval's errors in its first 10 decisions (as under pile)
and 9 on the whole letter (4 and 0 net by decision 20, x and m), random orders cost about 1.7-6.7 errors by decision 20 instead of
21-61, and size order (b) costs at most 3 by decision 20 (gains 2 on the whole letter) instead of 33-67. Cluster propagation is now roughly neutral-to-mildly-harmful for blind orders and about as good as pile
propagation for the doubt feed; it is not "destructive" in the sense measured.

**Readings 2-4 stand in direction.** Pile propagation is still about neutral and per-tile safe; the doubt feed's first 20 decisions
remove about what they did (pile x, net removed by decision 20: dev 2 -> 1, eval 6 -> 6, whole 2 -> -1). Reading 4's suggestion "never propagate an owner
decision to a whole atlas cluster on this family" was drawn from the destructive figure; the evidence for "never" is gone, though
"pile x cluster at most" remains the cautious choice (cluster still loses to pile on dev and for random orders on every unit).
