# TXE3-1 sorter question order -- RESCORE (11 Oct 2026, 17:5x UTC by date -u)

**Measurement correction: box-to-position map fixed (off by one), not a new gate look.** The eval rows are read-free simulations
(the benchmark truth plays the owner), as in RESULTS.md.

Job BOXMAP-RESCORE (others) for the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M). Script-only: no vision call, no reader, no
image viewed, no network beyond git. No truth file, BENCHMARK-TX.tsv row or confirm item touched.

TXE3-1 ran `tools/tx_sorter_curve.py --map atlas/no87_box_token.tsv`: the map places each atlas box's cluster at a position (pile and
cluster propagation) and joins the atlas top-k to positions (the margin order). It is one token off on 10 of 26 lines
(`ciphers/nevers-birago-fr3251-1572/atlas/RESCORE.md`). **Only `--map` changed** (to `atlas/no87_box_token_labelaware.tsv`), every
other argument as in VERIFY.md's reproduce line, every committed setting:

    bash benchmark-tx/txeng3/1/rescore_boxmapLA/run.sh            # -> rescore_boxmapLA/{eval,dev}/ (curves, summaries, eval pile k-dumps)
    python3 benchmark-tx/txeng3/1/rescore_boxmapLA/table.py       # before/after per order, rescore_t31.json

The disagree, lattice and a_doubt orders do not read the map; under pile or cluster propagation their curves move only because the
clusters a decision spreads to are now the right tiles. Atlas clusters on eval: 89 (381 tiles) -> 82 (373).

## Eval (no.87 eval_heldout), primary model pile: wrong signs at k = 10 / 20 / 50 / 100, questions to 3% and to 2%

| order | conv | before | **after** |
|---|---|---|---|
| disagree | x | 3/2/2/0; 0; 7 | **3/2/2/0; 0; 2** |
| lattice | x | 10/5/5/4; 0; 16 | **10/4/4/4; 0; 16** |
| margin | x | 10/5/4/1; 0; 12 | **10/4/3/1; 0; 13** |
| a_doubt | x | 4/4/3/1; 0; 3 | **4/4/3/1; 0; 1** |
| disagree_margin | x | 2/2/2/2; 0; 1 | **3/2/2/2; 0; 1** |
| b_size | x | 10/10/8/8; 0; 196 | **10/10/2/2; 0; 23** |
| random 20 seeds, k=20 min / mean / max; 2% median | x | 4 / 8.9 / 11; 53 | **4 / 8.2 / 11; 43** |
| disagree | m | 7/6/5/2; 7; 10 | **7/6/5/2; 2; 10** |
| lattice | m | 12/7/7/5; 14; 19 | **12/6/6/5; 14; 19** |
| margin | m | 15/10/9/6; 12; 100 | **15/9/9/6; 13; 98** |
| a_doubt | m | 9/9/7/4; 3; 47 | **9/9/7/5; 1; 47** |
| random k=20; 2% median | m | 9 / 13.8 / 15; 100 | **7 / 12.9 / 15; 93** |

Per tile (none): only margin and disagree_margin move (margin x to 2%: 52 -> 96; m 187 -> 184); disagree, lattice, a_doubt and random
are identical. Cluster model, k=20 wrong (x / m), before -> after: disagree 57 / 59 -> **5 / 9**; lattice 35 / 43 -> **8 / 10**;
margin 59 / 64 -> **19 / 24**; a_doubt 59 / 64 -> **4 / 9**; random mean 45.9 / 55.9 -> **12.1 / 16.6** (min 30 / 39 -> 6 / 7); base
10 / 15. Dev (pile x): disagree, lattice and random unchanged (7, 7, 10 / 13.0 / 14 at k=20); dev cluster x: disagree 28 -> 21,
a_doubt 15 -> 8, random mean 33.5 -> 16.7 against base 14. Full table: `python3 rescore_boxmapLA/table.py`.

The tx_doubt signal tables (`n_signals`, behind a_doubt) also join boxes through the old width DP. Rebuilt on the label-aware map
(`benchmark-tx/txeng/rescore_boxmapLA/doubt/`, `disagree` and `latt` columns unchanged; `bash rescore_boxmapLA/run.sh OUT
benchmark-tx/txeng/rescore_boxmapLA/doubt`, summaries in `rescore_boxmapLA/newsig/`), a_doubt's wrong count at k=10/20 moves by at
most 3 and its questions to 2% by up to 8, mostly earlier (dev pile x 42 -> 34; eval pile x stays 1); disagree, the gate's order, is
unaffected by construction.

## Gate (PREREG), re-applied to the corrected measurement

Primary eval, pile, x: disagree 2 wrong at k=20 against the random 20-seed minimum 4 (before: 2 vs 4); questions to 3% 0 at the
random median 0. **Disagree beats random, unchanged.** Lattice and margin now leave 4 at k=20 (before 5), equal to the random
minimum, so by the registered rule (below the minimum) they still do not beat random; they now beat the random mean by more. Winner
unchanged: disagree. Disagree now reaches 2% in 2 questions instead of 7 (random median 43, was 53): the five-tile T98/T18 pile
VERIFY.md traced is one of the clusters the old map had scattered.

## Does the conclusion change?

- **The gate verdict does not change**: disagree beats random; lattice and margin do not, by the registered rule; the
  recommendation (reader-disagreement tiles first) stands, with a stronger number (2 questions to 2% under x, 10 under m).
- **The propagation clause changes.** "Cluster -- every order under whole-cluster propagation ends far worse than doing nothing" and
  "qualified: pile or per-tile propagation only, never whole-cluster" rested on the shifted joins: with the right map, disagree and
  a_doubt under whole-cluster propagation end at or below the base on eval (5 and 4 against 10 at k=20, x), random orders cost about
  2 errors on eval instead of 36; on dev, cluster propagation still ends above the base for most orders (disagree 21, random 16.7
  against 14). "Never whole-cluster" is no longer supported as a measurement; "pile first" still is (pile is at least as good on every
  unit and safer on dev). Same change as X6 (`benchmark-tx/txeng2/sorter/RESCORE.md`).
