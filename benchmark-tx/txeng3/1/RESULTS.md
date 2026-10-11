# TXE3-1: which questions should the owner's sorter ask first? (account 3, Fable, session_01NGr4EgD9Bhbmri2omj7nn5; 11 Oct 2026, written 06:07 UTC 11 Oct 2026 by date -u)

PREREG: `benchmark-tx/PREREG-txeng3-1.md` (committed f03c4f25 at 05:54 UTC, dev choice lam 1 added 93b1b8bd at 06:00, before any eval
run). Read-free: no image, no reader, no model call; the benchmark truth plays the owner only inside `tools/tx_sorter_curve.py`
(TXE2-SORT's simulator, 9 Oct 2026) and is scored only through `tools/tx_bench.py`. Nothing published, no owner page touched, no
truth file edited, no confirm item opened. **The eval_heldout rows are read-free simulations, not eval looks** (as X6).

## What was built
`tools/tx_sorter_curve.py` gained the three orders the brief names, as options (CLAUDE.md Usage 8; test
`tools/tests/test_tx_sorter_curve.py::test_txe3_orders`): `--lattice TOPK --key KEY [--lang] [--lam]` (the live sorter's
`--rank-lattice` value, `sign_sorter.value_from_lattice`, one decode per line), `disagree` (the `disagree` column of the
tx_doubt signals: passes A and B differ), `--margin ATLAS_TOPK` (d2 - d1 ascending), the declared exploratory `disagree_margin`,
plus `--at`, `--thresholds` and `--dump-dir` (the simulated output at each k, for tx_bench). X6's a_doubt (the sorter feed today,
n_signals), b_size, c_random and d_oracle run beside.

## Setup
Base C = `benchmark-tx/outputs/birago1572-no87/passC.tsv` (reconciled two passes). Units: dev_tune f178v L01-12 (tuning),
eval_heldout f178v L13-23 + f179r L01-03 (the report). Map `atlas/no87_box_token.tsv` (1:1 boxes), clusters `atlas/clusters.tsv`
(140-cluster over-split; 89 clusters on eval). Lattice `harvest/tx_decode/no87_topk.tsv` (TX-DECODE from-passes on the C skeleton),
key `harvest/key_1572_sheet.tsv`, it16dip LM, lam 1 (dev chose lam 1 over lam 4: 7 vs 10 wrong at k=20). Margin from
`atlas/topk/no87_heldout.tsv` (held-out lines out of the vote; the dev margin is truth-contaminated via the atlas's tune-line
overrides and is a sanity check only). Random = 20 seeds. Propagation: **pile** (primary, X6 reading 4), cluster (the brief's literal
model), none. err_true = position errors (wrong-or-deleted / scored), identical to tx_bench's figure on these outputs (checked:
base 15/376 m, 10/371 x both ways; `eval/tx_bench_dumps.tsv` reproduces every k-dump cell below). x = flagged excluded, m = as
measured; both always.

## Eval (no.87 eval_heldout), primary model pile -- wrong signs after k questions, err_true, Wilson 95% from tx_bench

Base C: m 15/376 = 0.040 (0.024-0.065); x 10/371 = 0.027 (0.015-0.049). Under x the base is already below 3%, so "questions to 3%" is 0
for every order there and the informative threshold is 2%.

| order | conv | k=10 | k=20 | k=50 | k=100 | to 3% | to 2% |
|---|---|---|---|---|---|---|---|
| **disagree** (b) | x | 3 = 0.008 (0.003-0.024) | **2 = 0.005 (0.001-0.019)** | 2 = 0.005 | 0 = 0.000 (0.000-0.010) | 0 | **7** |
| lattice (a) | x | 10 = 0.027 (0.015-0.049) | 5 = 0.013 (0.006-0.031) | 5 = 0.013 | 4 = 0.011 (0.004-0.027) | 0 | 16 |
| margin (c) | x | 10 = 0.027 | 5 = 0.013 (0.006-0.031) | 4 = 0.011 | 1 = 0.003 (0.000-0.015) | 0 | 12 |
| random, 20 seeds (d) min / mean / max | x | 5 / 9.0 / 10 = 0.0135 / 0.0243 / 0.027 | **4 / 8.9 / 11 = 0.0108 / 0.0239 / 0.0296** | 3 / 7.2 / 10 | 2 / 4.3 / 10 | 0 | median **53** (20 of 20 reach) |
| a_doubt (X6 feed, beside) | x | 4 = 0.011 | 4 = 0.011 (0.004-0.027) | 3 = 0.008 | 1 = 0.003 | 0 | 3 |
| disagree_margin (exploratory) | x | 2 = 0.005 | 2 = 0.005 (0.001-0.019) | 2 | 2 = 0.005 | 0 | 1 |
| d_oracle (upper bound, stops at 4) | x | 1 | 1 | 1 | 1 | 0 | 1 |
| **disagree** | m | 7 = 0.019 (0.009-0.038) | **6 = 0.016 (0.007-0.034)** | 5 = 0.013 | 2 = 0.005 (0.001-0.019) | **7** | **10** |
| lattice | m | 12 = 0.032 | 7 = 0.019 (0.009-0.038) | 7 | 5 = 0.013 | 14 | 19 |
| margin | m | 15 = 0.040 | 10 = 0.027 (0.015-0.048) | 9 | 6 = 0.016 | 12 | 100 |
| random min / mean / max | m | 10 / 14.4 / 15 | **9 / 13.8 / 15 = 0.0239 / 0.0366 / 0.0399** | 6 / 10.9 / 15 | 5 / 8.0 / 13 | median 48 (20 reach) | median 100 (19 reach) |
| a_doubt | m | 9 | 9 = 0.024 | 7 | 4 | 3 | 47 |
| disagree_margin | m | 7 | 6 = 0.016 | 6 | 6 | 1 | 10 |
| d_oracle (stops at 8) | m | 2 | 2 | 2 | 2 | 1 | 3 |

Other propagation models, k=20 wrong (x / m): **none** -- disagree 5 / 9, lattice 7 / 9, margin 9 / 14, a_doubt 7 / 11, random min
8 / 13 (mean 9.4 / 14.2); **cluster** -- disagree 57 / 59, lattice 35 / 43, margin 59 / 64, a_doubt 59 / 64, random min 30 / 39
(mean 45.9 / 55.9), base 10 / 15: every order under whole-cluster propagation ends far worse than doing nothing, as X6 found.
Files: `eval/curve_eval_<mode>_<x|m>_lam1.tsv`, `eval/summary_*.json`, `eval/dump_pile_*/` (k-dumps), `eval/tx_bench_dumps.tsv`
(`score_dumps.py`); dev in `dev/`.

## Gate (PREREG), applied
Primary eval, pile, x: disagree's err_true at k=20 (0.0054, 2 wrong) is below the random 20-seed minimum (0.0108, 4 wrong) and its
questions-to-3% (0) is at the random median (0): **disagree BEATS random**. Lattice and margin (5 wrong) do not clear the random
minimum (4). Winner among the informed orders: **disagree** (2 at k=20; next a_doubt 4, lattice 5, margin 5). The m convention
(disagree 6 vs lattice 7, random min 9) and the none model (5 vs 7 / 9; 9 vs 9 with the k=10 tiebreak 10 vs 12) do not reverse it;
the cluster model reverses everything (no order beats the base), so the recommendation is **qualified: pile or per-tile
propagation only, never whole-cluster** (X6 reading 4, confirmed on C with three more orders).

## Dev (pile, x; base C 14/338 = 0.041) for the record
k=20 wrong: disagree 7, lattice 7 (lam 1; 10 at lam 4), a_doubt 9, margin 12, disagree_margin 7, random min / mean / max 10 / 13.0 / 14;
to 2%: disagree 28, lattice 52, a_doubt 30, margin not reached, random median 134 (17 of 20 reach). Same ranking as eval.

## By how much, and the owner minutes it implies
At k=20 under pile x, disagree leaves 2 wrong where the random mean leaves 8.9 (6.9 errors fewer on 371 signs); it reaches 2% in 7
questions against a random median of 53 (46 questions fewer); under m 10 against 100 (90 fewer). At the owner's measured
**8.6 min per 100 flagged boxes** (L74 Vivonne box check, 10 Oct 2026 -- a BOX-CHECK rate, not a sorter rate; a sorter decision
may well take longer), that is about 0.6 min instead of 4.6 min to 2% on this leaf (x), or 0.9 instead of 8.6 min (m). Flag recall:
the disagree signal marks 19 of 371 eval tiles and holds 5 of C's 10 x errors (precision 0.26, recall 0.50; dev 8 of 14 among 30,
0.27 / 0.57) -- the other half of the errors are agreed-on wrong signs (LESSONS.md "Look-alike pass"), which only pile propagation
and the later reading-order questions reach (0 wrong at k=100 under x).

Why the live ranking loses: the `--rank-lattice` value is highest where the decode wants to override the readers, and TX-DECODE
found that override raises err_true on no.87 -- its first ten questions fixed nothing (10 wrong at k=10, both conventions). The
classifier margin asked ten before its first fix too; the atlas top-1 is at 0.162 on this hand. The exploratory disagree_margin
fixed 5 at its first question (a pile propagation) but broke 2 at k=4 and sits at 2 to k=100: the margin tiebreak does not help
beyond that one tile, so it is not the recommendation.

## For the owner, in three plain sentences
When you sort no.87 tiles, look first at the tiles where our two readers disagreed: fixing those, in page order, took 7 of your
decisions to bring the leaf under 2% error, where a random order took about 53. At your box-check pace that is under a minute
instead of about five, on one 376-sign leaf and with the known answer standing in for you, so a real session will be slower and
less clean. The sorter's own "most useful" ranking and the computer's shape-confidence margin each asked ten questions before fixing
anything, so the "Check these first" box should list reader-disagreement tiles first, and a decision should spread only to tiles
already in the same pile, never to a whole shape cluster.

## Recommendation for the live sorter's "Check these first" box
Order: (1) tiles where passes A and B disagree, in reading order (about 20 per 400 signs); (2) then the rest of the doubt feed's
signals (a_doubt is close behind and reaches 2% in 3 questions under x); never `--rank-lattice` first on this family. Propagation:
`--propagate pile` semantics (same pile x cluster), never whole cluster. Caveats: one leaf, 10-15 errors, an oracle owner (X20 found
the owner's real decisions broke 3 fixed 0 on dev); the lattice and margin orders were run at the live defaults only.

## Next step and cost
Wire the disagree-first order into the Birago sorter's focus.tsv build (`ciphers/nevers-birago-fr3251-1572/sorter/no87/build.sh`,
read-free, about USD 1) and score the owner's next real no.87 session against BENCHMARK-TX the X20 way (about USD 2 + one owner
session): the oracle curve says 7 questions; the owner's real curve is the number that matters. Not started (brief: no follow-ups).

Verdict: measured: disagree beats random on eval under pile and none; lattice and margin do not; cluster propagation destructive.
