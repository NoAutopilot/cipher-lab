# VERIFY TXE3-1 (sorter question order): verifier's audit, 11 Oct 2026 (written 14:5x UTC by date -u)

Verifier: an Opus 5.5 subagent of the account-3 parent's workflow (parent session_0198Cv8ypBfBVfRToKVWx33M). It did not
run TXE3-1 (session_01NGr4EgD9Bhbmri2omj7nn5) and does not protect its conclusions. Method: committed files only, at
origin/main b466fda83. The committed `tools/tx_sorter_curve.py` and `tools/tx_bench.py` were re-run into a scratch
directory. No model reading pass, no image, no network beyond git. No owner sorter page, L74 oracle answer or frozen
confirm item was opened. The experiment's own files are unchanged; this file is the only one added.

## Verdict in one line
The numbers reproduce byte for byte and the registered gate was applied correctly. Two of the three owner-facing sentences
overstate it, and one is wrong. "Lattice did no better than random" is wrong: the lattice order missed the registered bar
by one sign in the primary setting, cleared the same bar in the other three non-cluster settings and on dev, and did better
than most random orders in every one of them. "7 decisions vs about 53" quotes the flagged-excluded figure alone; the
as-measured figure is 10 vs about 100. The 7 is mostly one decision that fixed a five-tile T98-for-T18 pile at once.

## 1. Re-derivation (committed tool, committed inputs, 20 seeds, kmax 200)
All six eval runs (pile / none / cluster, each x and m) and the dev pile-x runs at lam 1 and lam 4 regenerated
**byte-identical** curve TSVs and summary JSONs. All 56 eval k-dumps were identical, and re-scoring them with
`tools/tx_bench.py` through a copy of `score_dumps.py` that writes elsewhere gave a `tx_bench_dumps.tsv` identical to the
committed one, row for row. The inputs used are unchanged since 3-10 Oct. `key_decode_lattice.py` changed at 05:57 UTC 11 Oct
(TXE3-9 `--pins`), and the lattice order still reproduces at HEAD.

Eval, no.87 eval_heldout (f.178v L13-23 + f.179r L01-03), wrong signs. Base C is 10/371 (x) and 15/376 (m).

| figure | reported | re-derived |
|---|---|---|
| disagree, pile x, k=10/20/50/100 | 3 / 2 / 2 / 0 | 3 / 2 / 2 / 0 |
| disagree, pile x, to 2% | 7 | 7 (one decision at q7 fixed 5: k=6 8 wrong -> k=7 3 wrong) |
| disagree, pile m, k=20; to 3%; to 2% | 6; 7; 10 | 6; 7; 10 |
| lattice, pile x / m, k=20 | 5 / 7 | 5 / 7 (broken 2 at k=20 in both) |
| lattice, pile x / m, to 2% | 16 / 19 | 16 / 19 |
| margin, pile x / m, k=20; to 2% | 5 / 10; 12 / 100 | 5 / 10; 12 / 100 |
| a_doubt (current feed), pile x / m, k=20; to 2% | 4 / 9; 3 / 47 | 4 / 9; 3 / 47 |
| random 20 seeds, pile x, k=20 min/mean/max | 4 / 8.9 / 11 | 4 / 8.9 / 11; per seed sorted 4,5,5,5,8,9,9,10x11,11,11 |
| random, pile x, to 2% median | 53 | 53 (upper median; lower 52); per seed 1,1,10,15,21,27,31,43,48,52,53,59,66,68,68,82,85,108,145,165 |
| random, pile m, k=20 min/mean; to 2% median | 9 / 13.8; 100 (19 reach) | 9 / 13.8; 100 (upper; lower 96); range 26 to not reached |
| none x / m, k=20: disagree, lattice, margin, random min | 5/9, 7/9, 9/14, 8/13 | same |
| cluster x / m, k=20: disagree, lattice, margin, random min / mean | 57/59, 35/43, 59/64, 30/39 / 45.9/55.9 | same |
| dev pile x, lattice k=20 lam 1 / lam 4 | 7 / 10 | 7 / 10 (so lam 1, as registered) |
| disagree flag on eval: tiles, C errors held | 19 of 371, 5 of 10 (x) | 19 / 5 of 10 (x); 20 / 6 of 15 (m) |

Not committed: the random orders' simulated outputs. The tool dumps only the named orders, so the random band is scored
inside the simulator (with the same `tx_bench.position_errors`), not by an external tx_bench call. The tool regenerates it
deterministically, so this is not a rule-7 failure. The ROOM done line (06:07) names commit `fe169bdb`, which does not exist
on origin. The real commit is 5192ca9d0.

## 2. Pre-registration order
The PREREG was committed as f03c4f252 at 05:54:48 UTC. Addition 1 (the dev lam choice) and the tool changes went in
together as 93b1b8bd3 at 06:00:50. The eval k-dumps were scored at 06:04 (`tx_bench_dumps.tsv` header). Results and the
LEDGER row followed at 06:07:23. The PREREG came before every committed score. The code that produced the dev scores was
committed only with them, so git cannot prove that nothing was scored before 05:54; nothing suggests it was. Addition 1
applies a rule registered at 05:54 (lower dev k=20 under pile x; lam 1 7 vs lam 4 10, re-derived). It is not a deviation,
and nothing else was tuned.

Undeclared narrowings, both minor. The PREREG says every k-dump is scored by tx_bench; that was done for pile only, while the
none and cluster figures come from the simulator's internal scorer, which is the same function. The random orders are never
dumped.

## 3. Gate
Registered: "Primary: eval_heldout, pile, x. An informed order BEATS random when its err_true at k=20 is below the random
20-seed minimum at k=20 AND its questions-to-3% is at or below the random median ... Winner among the informed orders: lowest
err_true at k=20; tiebreak err_true at k=10, then questions-to-3%, then k=50. The m convention and the other two propagation
models ... must not reverse the winner for the recommendation to stand unqualified; if they do, the recommendation is
qualified by model."

How the numbers come out:
- disagree: 2/371 (0.0054) is below the random minimum of 4/371 (0.0108), and its questions-to-3% is 0, at or below the
  median of 0. **It beats random.**
- lattice and margin: 5/371 (0.0135) each, not below 0.0108, so neither beats random.
- winner: disagree.
- other settings: m (6 vs 7 vs 10), none x (5 vs 7 vs 9) and none m (9 vs 9 vs 14, decided by the k=10 tiebreak, 10 vs 12)
  keep disagree. Cluster reverses it: lattice 35 is best there, so the recommendation is qualified by model.

The reported verdict follows from the gate.

Two weaknesses in the gate:
1. The second clause was vacuous on the primary convention. Under x the eval base is already 2.7% (10/371), so every order,
   random included, has questions-to-3% of 0, and the gate reduces to the k=20 clause. This was knowable at registration:
   on these lines C is identical to L (0 of 402 signs differ), and X6 had already published the eval x base, 10/371 0.027
   (`benchmark-tx/txeng2/sorter/RESULTS.md`, table row "eval_heldout x"). The owner-facing 2% figure is a registered
   endpoint, but it is not the gate statistic.
2. The "below the best random seed" bar is one sign wide here (4 vs 5). Whether an order clears it depends on whether it
   reaches the single five-tile pile (atlas cluster 102, T98 read for T18) within 20 questions, plus one or two other tiles.

## 4. Control
The control is random order with 20 seeds: the same showable tiles, base, truth, propagation and simulator, with only the
order changed. It can vary on the statistic, and it did. Under pile x it left 4 to 11 wrong at k=20 and needed 1 to 165
questions to reach 2%. Under pile m it left 9 to 15 wrong at k=20 and needed 26 questions or more (not reached) to reach 2%.
So rule 3's cannot-differ shape does not apply.

What the control shows: exactly the 4 random seeds that hit the cluster-102 pile within 20 questions (at q1, q1, q10, q15) land at 4-5 wrong, and
2 seeds reach 2% at question 1. The control is matched, and its spread is large because one pile holds half the x errors.

## 5. Split
Dev (dev_tune) was used only for the lam choice. Eval was run once per declared configuration and nothing was re-tuned after
it. That is correct. The eval unit was not fresh for this question, though:
- **On these lines C = L.** The new-base claim ("from ... C rather than L") makes no difference on eval. The a_doubt,
  b_size, oracle and random curves duplicate X6's eval curves; random now uses 20 seeds instead of 10.
- **The disagree signal's eval precision was already on file.** TXE-O (9 Oct, `benchmark-tx/txeng/doubt/measure_eval_heldout.md`)
  reports disagree flags 20/376 holding 6/15 errors on these exact lines, which this verifier re-derives on C. An order whose
  first 20 tiles hold 30% errors, against a 4% base rate, beats random at k=20 almost by construction.

This is not tuning on eval, but the eval figure is a re-expression of a known statistic, not an independent held-out
confirmation. The PREREG's "Nearest prior" section cites X6 and omits TXE-O.

## 6. Claims as told to the owner

| # | claim | verdict |
|---|---|---|
| 1 | disagreement tiles -> no.87 under 2% in 7 of his decisions; random about 53 | overstated |
| 2a | the lattice ("most useful") ranking did no better than random | wrong |
| 2b | nor did the classifier-margin order | overstated |
| 3a | "Check these first" should list disagreements first | overstated |
| 3b | a decision should spread only within its own pile | overstated |
| 3c | never across a whole shape cluster (cluster propagation destructive) | holds (scoped) |

**1 (overstated).**
- It quotes the flagged-excluded figure alone; as measured it is 10 vs about 100 (TRANSCRIPTION.md: never alone).
- It covers the eval part only, 371-376 of no.87's 803 signs, not "no.87".
- The decisions were simulated with the known answer standing in for the owner. They were not his; X20 found his real
  4 Oct decisions broke 3 and fixed 0 on dev.
- The x base was already 2.7%, so "under 2%" means 3 of 10 errors fixed.
- The 7 is the question at which the order first shows a tile of the five-tile T98/T18 pile. That one decision fixed 5.
- Random's "about 53" is the median of a 1-165 spread, and 2 of 20 random orders got there in 1 question.
- In an exploratory verifier run, merely re-ordering the same disagreement tiles by the doubt feed's signal count moves 7 to
  2 (x) and 10 to 14 (m).

Corrected: "In a simulation on the held-out part of no.87 (about 375 of 803 signs), with the known answer playing you,
showing the reader-disagreement tiles first reached 2% error in 7 questions with flagged signs excluded and 10 as measured,
against a median of about 53 and 100 for 20 random orders (spread 1-165 and 26 to not reached). Most of that is one
question that fixed a five-tile T98-for-T18 pile."

**2a (wrong).**
- In the primary setting (pile x) the lattice order left 5 errors at k=20 against the best random seed's 4. It beat 16 of
  20 random orders, tied 3 and lost 1, and it reached 2% in 16 questions against a random median of 53.
- The registered rule, applied unchanged, says the lattice order **beats random** in pile m (7 vs a random minimum of 9;
  14 vs 48 to 3%), none x (7 vs 8; 0 vs 0), none m (9 vs 13; 14 vs 80) and on dev pile x (7 vs 10; 10 vs 64). It beats all
  20 seeds at k=20 in each of those.
- Against disagree at k=20 the paired difference is 3 tiles vs 0 under x (exact sign p 0.25) and 4 vs 3 under m (p 1.0).
- RESULTS' "ten questions before a first fix ... both conventions" holds only under x. Under m the lattice order fixed 3 in
  its first ten (15 -> 12).

Corrected: "The lattice ranking missed the pre-registered bar by one sign in the primary setting, but it did better than most
random orders there and cleared the same bar in the three other non-cluster settings and on dev. At 20 questions it trails
the disagreement order by 3 tiles, a difference this one leaf cannot separate from chance."

**2b (overstated).**
- Margin missed the bar by one sign in every setting: 5 vs 4, 10 vs 9, 9 vs 8, 14 vs 13.
- Under pile propagation it still beat 16-17 of 20 random orders, because its 12th question hit the five-tile pile. Its
  first eleven questions fixed nothing in either convention.
- Per tile it was at the random level: 9 vs a random range of 8-10 (x), and 14 vs 13-15 (m).

Corrected: "The classifier-margin order missed the bar by one sign everywhere. Its first eleven questions fixed nothing,
and per tile it did no better than random."

**3a (overstated).**
- Disagree is the registered winner at k=20 in all four non-cluster settings, so "disagreements first" for the first ~20
  questions is supported, by 2-3 tiles on one leaf.
- Against the current doubt feed (a_doubt) the k=20 difference is 2 vs 0 tiles under x (p 0.5) and 4 vs 1 under m (p 0.375).
  The current feed reached 2% sooner under pile x (3 vs 7) and is ahead at 50-100 questions per tile (none x 2/1 vs 5/3;
  none m 5/3 vs 8/5).
- The recommended order, "disagreements, then the rest of the doubt feed", was not simulated by TXE3-1: its disagree order
  falls back to reading order.
- Verifier exploratory run, unregistered, on an already-inspected unit, using the tool's own simulator: that order gives
  pile x 5/2/2/0 at k 10/20/50/100 and 2% at q2; pile m 9/6/6/3 and 2% at q14; none x 6/5/2/0; none m 11/9/5/2. It matches
  or beats both components from k=20 on, but it is not a registered result.

Corrected: "Listing the reader-disagreement tiles first was the best of the registered orders for the first 20 questions on
this one leaf, ahead of the current doubt feed by 2-3 tiles net. The 'disagreements, then the rest of the doubt feed' order it
recommends was not itself tested."

**3b (overstated).**
- Pile propagation beat per-tile for every informed order at k=20 (x: disagree 2 vs 5, lattice 5 vs 7, margin 5 vs 9,
  a_doubt 4 vs 7). Most of that gain is the one cluster-102 pile.
- Pile propagation also breaks tiles: the lattice order broke 2 at k=20 through a T24->T45 pile in cluster 132, and one
  random seed ended at 11 against a base of 10.
- All of this is with an oracle owner. With real decisions, a wrong call spreads across the pile too, and that is untested.

Corrected: "With the known answer playing you, spreading a decision within its pile beat deciding tile by tile, mostly
through one five-tile pile. It can also spread a wrong call, which was not tested with your real decisions."

**3c (holds, scoped).**
- Under whole-cluster propagation every order ended far worse than the starting read at k=20 (x: 35-59 wrong vs 10 to start;
  random mean 45.9).
- This replicates X6 on the same leaf, the same atlas (140-cluster over-split) and, on these lines, the same base signs
  (C = L). It is the same evidence restated, not new evidence.
- "Never" is supported for this atlas on this hand. Another atlas would need its own check.

## 7. Rule issues
- TRANSCRIPTION.md "Never quote the flagged-excluded figure alone": RESULTS' "For the owner, in three plain sentences" and
  the parent's sentence 1 give 7 vs 53 (x) without 10 vs 100 (m).
- Rule 3: the control is matched and can vary, so no breach. The gate's second clause was vacuous on the primary convention,
  and that was knowable from X6's published eval base (section 3).
- Held-out freshness: the eval lines were already read for this very signal (TXE-O) and these very curves (X6), and the PREREG
  omits TXE-O (section 5).
- Cost: LEDGER row 9.76 USD against a 15 USD cap; box 05:47-06:07 UTC against 2 h. Within both.
- Novelty wording (rule 10): none used.
- Rule 7 traceability: the ROOM done line cites a commit hash (`fe169bdb`) that is not on origin.

## 8. Safe sentence for the owner
"On the held-out part of no.87, in a simulation with the known answer playing you, listing the tiles where our two readers
disagreed first reached 2% error in 7 questions with flagged signs excluded and 10 as measured, against a median of about
53 and 100 for random orders. Most of that came from one decision that fixed a five-tile T98/T18 pile. The lattice ranking
also beat most random orders and missed the strict bar by one sign. Whole-cluster spreading made things worse every time,
as X6 had already found."

## Reproduce (from the repo root; sparse paths benchmark-tx, tools, ciphers/nevers-birago-fr3251-1572/{atlas/topk,harvest/tx_decode})
    C=ciphers/nevers-birago-fr3251-1572
    python3 tools/tx_sorter_curve.py --truth benchmark-tx/birago1572-no87.truth.tsv \
      --base benchmark-tx/outputs/birago1572-no87/passC.tsv --lines benchmark-tx/txeng/units/labels_eval_heldout.tsv \
      --map $C/atlas/no87_box_token.tsv --clusters $C/atlas/clusters.tsv --signals benchmark-tx/txeng/doubt/eval_heldout_signals.tsv \
      --margin $C/atlas/topk/no87_heldout.tsv --lattice $C/harvest/tx_decode/no87_topk.tsv --key $C/harvest/key_1572_sheet.tsv \
      --lang it16dip --lam 1 --propagate pile --seeds 20 --exclude-flagged --dump-dir OUT/dump --out OUT/curve.tsv --json OUT/s.json
(then diff against eval/curve_eval_pile_x_lam1.tsv). The per-seed figures, the paired sign tests and the hybrid order use the
tool's own `Sim`, `run_order`, `oracle_rows` and `random.Random(seed).shuffle(show)`, seeds 0-19, with no change. The hybrid's
sort key is `(-disagree, -n_signals, reading order)`.
