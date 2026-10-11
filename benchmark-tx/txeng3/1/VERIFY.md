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

## Second check (11 Oct 2026, written about 16:4x UTC by the account-3 parent from the second verifier's report; workflow wf_35ed2244-0e6)

A second, independent agent ruled on each objection and non-holds verdict above, re-running the commands itself. Where it disagrees with this file, this section governs.

### Rulings on the first verifier's objections

- **agree**: Re-derivation: every eval and dev curve, summary and k-dump reproduces byte for byte.
  - Evidence: I re-ran tools/tx_sorter_curve.py at origin/main 7106556de (20 seeds). The eval pile, none and cluster runs (each x and m) and the dev pile x runs at lam 1 and lam 4 all match the committed files byte for byte (cmp). I re-derived the per-seed list itself: pile x to 2% per seed is 145,27,10,68,52,48,21,85,1,15,108,31,59,53,1,43,66,165,68,82, with an upper median of 53. Pile m: 19 of 20 seeds reach 2%, upper median 100, range 26 to not reached. Pile x at k=20, seeds sorted: 4,5,5,5,8,9,9, then 10 eleven times, then 11,11. The disagree flag on eval covers 19 of 371 tiles holding 5 of 10 x errors, and 20 of 376 holding 6 of 15 under m. C and L are identical on the eval lines: 0 of 402 signs differ.
- **agree**: Claim 1 / RESULTS 'For the owner': '7 vs about 53' quotes the flagged-excluded (x) figure alone; as measured it is 10 vs 100 (breaks TRANSCRIPTION.md:36). The 7 is mostly one five-tile T98-for-T18 pile. The scope is the eval lines only, with an oracle owner.
  - Evidence: TRANSCRIPTION.md line 36 reads 'Never quote the flagged-excluded figure alone.' Pile m gives disagree to 2% at q10 against a random upper median of 100 (summary_eval_pile_m_lam1.json). My trace of the disagree order (pile x) shows question 7 is tile f178v_L19 pos 6, cluster 102, read T98 where the truth is T18. Pile propagation moved 5 tiles and wrong went from 8 to 3; under m the same question took it from 13 to 8. The x base is 10/371 = 2.7%, so 'under 2%' (the tool tests <=2%, i.e. <=7 wrong) means a net 3 fixed. The unit is eval_heldout (371 x / 376 m of no.87's 803 scored rows). The oracle plays the owner (true_sign from the truth file). X20's real-owner row on dev reads fixed 0 / broken 3 (txeng2/sorter/RESULTS.md:99).
- **partly**: Claim 2a: 'the lattice ranking did no better than random' is wrong. It missed the bar by one sign in the primary setting, beat 16 of 20 seeds there, and cleared the same bar in pile m, none x, none m and dev.
  - Evidence: Every number checks:
- Pile x at k=20: lattice 5 beats 16 seeds, ties 3, loses 1.
- The other settings (lattice vs random minimum): pile m 7 vs 9, none x 7 vs 8, none m 9 vs 13, dev pile x 7 vs 10. Lattice beats all 20 seeds in each.
- To 3%: lattice 14 vs 48 (pile m), 14 vs 80 (none m), 10 vs 64 (dev).
- Paired against disagree at k=20: 3 vs 0 under x (p 0.25) and 4 vs 3 under m (p 1.0).

So the owner sentence is false at the registered endpoint: 5 against a random median of 10 is not 'no better'.

Two cautions the verifier left out:
1. The PREREG applies the beats-random test only to eval pile x; the other settings only test whether the winner reverses. 'The same registered rule says lattice BEATS random' in those settings applies the rule outside its registered scope. The registered verdict is still 'does not beat random'.
2. In the primary setting the lattice is at random level outside k=20-50. At k=10 it is 10 wrong, the random maximum (13 ties, 7 seeds better). At k=100 it is 4 against a random mean of 4.3 (beats 8, ties 2, loses 10). Its k=20 edge is one question (q16) hitting the same cluster-102 pile, after q15 broke 2 tiles through a T24-to-T45 pile in cluster 132. That is the same mechanism the verifier used to discount margin.

Its per-tile edge (none x, k=20: 7 vs a minimum of 8) is real but one sign wide.
- **partly**: RESULTS: lattice 'asked ten questions before a first fix ... both conventions' holds only under x; under m it fixed 3 in its first ten (15 to 12).
  - Evidence: Literally right. Pile m lattice fixes at q1 (f178v_L13 pos 7), q3 (f178v_L15 pos 24) and q6 (f178v_L21 pos 21), giving 15 to 12. However, all three positions carry truth flag 'alignment-doubtful', so they are not showable under x. On unflagged signs the 'nothing in the first ten' statement holds. Margin fixes nothing before q12 in both conventions, as RESULTS says.
- **agree**: Claim 2b: 'nor did the classifier-margin order' is overstated. It missed the bar by one sign everywhere, its first 11 questions fixed nothing, it is at random level per tile, and it beat 16-17 of 20 seeds under pile only through hitting the pile at q12.
  - Evidence: - Margin vs the random minimum: 5 vs 4 (pile x), 10 vs 9 (pile m), 9 vs 8 (none x), 14 vs 13 (none m).
- Against all 20 seeds at k=20: pile x beats 16, ties 3, loses 1; pile m 17/2/1.
- Q12 is f178v_L19 pos 6 (cluster 102); under x it took 10 wrong to 5.
- Per tile it is at random level: none x k=20 beats 11, ties 6, loses 3 (random range 8-10); none m 9/7/4 (range 13-15).
- One thing the verifier did not mention: under pile x at k=100 margin (1 wrong) beats all 20 seeds. Under pile it is not simply random.

'Overstated' is the right grade. In the primary setting margin and lattice score identically at k=20; they differ only per tile.
- **partly**: Claim 3a: 'Check these first should list disagreements first' is overstated. The lead over the current doubt feed is 2-3 tiles and not separable from chance. The recommended 'disagreements then the rest of the doubt feed' order was never simulated. In the verifier's exploratory run that hybrid 'matches or beats both components from k=20 on'.
  - Evidence: Confirmed:
- Disagree is the registered winner. At k=20 it beats all 20 random seeds in all four non-cluster settings.
- Paired against a_doubt: 2 vs 0 under x (p 0.5) and 4 vs 1 under m (p 0.375).
- a_doubt reaches 2% first under pile x (q3 vs q7), and is ahead per tile at k=50/100 (none x 2/1 vs 5/3; none m 5/3 vs 8/5).
- The tool's disagree order falls back to reading order, so the recommended order was not simulated.
- I re-ran the hybrid and its figures match: pile x 5/2/2/0 (2% at q2), pile m 9/6/6/3 (2% at q14), none x 6/5/2/0, none m 11/9/5/2.

The verifier's 'matches or beats both components from k=20 on' is false under pile m:
- k=50 and k=100: hybrid 6 and 3 vs disagree 5 and 2.
- To 2%: hybrid q14 vs disagree q10.

What does hold (exploratory, unregistered): the hybrid is at or better than the current a_doubt feed everywhere except pile x at k=10 (5 vs 4).
- **partly**: Claim 3b: 'spread only within its own pile' is overstated. The pile gain is mostly one five-tile pile. Pile propagation also breaks tiles: lattice broke 2 through a T24-to-T45 pile in cluster 132, and 'one random seed ended at 11'. All of it uses an oracle owner.
  - Evidence: Confirmed, pile vs per tile at k=20 under x: disagree 2 vs 5, lattice 5 vs 7, margin 5 vs 9, a_doubt 4 vs 7. For random orders the mean barely moves (8.85 vs 9.4 under x; 13.75 vs 14.25 under m).

Correction: two random seeds, not one, end at 11 (seeds 5 and 16).
- Each first showed the one truly-T45 tile of the 3-tile T24 pile in cluster 132.
- Each broke 2 correct tiles, even with a perfect oracle.
- The pile is not truth-homogeneous, so a correct decision can still break tiles. That risk is independent of how good the owner is.

'At most within the pile, never whole cluster' is supported. 'Spread within the pile' as a clear gain rests on cluster 102.
- **agree**: Claim 3c: 'never spread across a whole shape cluster' holds for this atlas on this hand, but it restates X6 rather than adding new evidence.
  - Evidence: Cluster runs reproduce byte for byte. At k=20 under x:
- named orders: 35 (lattice) to 65 (b_size, which the verifier omitted from its 35-59 range)
- random: 30 to 78, mean 45.9
- base: 10

Under m the named orders are 43-70 against a base of 15. C = L on all 402 eval signs, and the 140-cluster atlas is the same, so the result restates X6 (txeng2/sorter/RESULTS.md:37-42).
- **agree**: Gate: the questions-to-3% clause was vacuous on the primary convention (x base 2.7%), and this was knowable at registration from X6's published eval x base of 10/371.
  - Evidence: Every order and all 20 seeds have to_pct 0.03 = 0 in summary_eval_pile_x_lam1.json. X6 RESULTS.md:37 (committed 9 Oct) gives 'eval_heldout x | 10/371 0.027', and C = L there. The PREREG quoted only the whole-leaf C figure (0.038 x), which probably hid this. No verdict changes: lattice and margin fail on the k=20 clause, and disagree passes both.
- **partly**: Held-out freshness: TXE-O had already measured the disagree flag's precision on these lines, and the PREREG's 'Nearest prior' omits it, so the eval figure re-expresses a known statistic.
  - Evidence: TXE-O (benchmark-tx/txeng/doubt/measure_eval_heldout.md:8, f1d6eed84, 9 Oct) gives 'disagree | 6/15 | 0.400 | 20/376' on exactly these lines. 'Nearest prior' cites only X6; TXE-O appears in the PREREG only as an LM user under Material. That is a fair caveat: per tile, 5 of 10 errors in 19 tiles predicts the k=20 result. It is not a rule breach. Nothing was tuned on eval, the dev choice (lam 1, 7 vs 10) was committed at 06:00:50 before the eval scores, and TRANSCRIPTION's 'tune on dev, report on eval' was followed.
- **partly**: Traceability: the ROOM done line cites commit fe169bdb, which is not on origin; the real one is 5192ca9d0. The verifier filed this as rule 7.
  - Evidence: `git cat-file -t fe169bdb` gives 'Not a valid object name'. 5192ca9d0 (06:07:23 UTC) is the results commit. The fact is right, but rule 7 concerns regenerating readings, and the reading regenerates byte for byte. This is a ROOM-line accuracy nit, not a rule-7 failure.
- **agree**: Undeclared narrowings: only the pile k-dumps were scored by tx_bench, and the random orders were never dumped.
  - Evidence: score_dumps.py loops only `for mode in ('pile',)`, and eval/ holds only dump_pile_x_lam1 and dump_pile_m_lam1. The PREREG Endpoint says every k-dump is scored by tools/tx_bench.py. Sim.score calls tx_bench.position_errors, the same function, so the figures are unaffected. This is minor.
- **agree**: Pre-registration order and cost/box.
  - Evidence: Commit times:
- f03c4f252 (PREREG): 05:54:48
- 93b1b8bd3 (tool + test + Addition 1): 06:00:50, PREREG, test and tool only
- 5192ca9d0 (results + LEDGER): 06:07:23

The dev outputs were committed with the results, but the dev numbers were already written into Addition 1 at 06:00.

LEDGER.md row 4251 gives 9.76 USD against the 15 USD cap; the work ran 05:47-06:07 against the 2 h box. No novelty words are used.

### Final verdict on each claim told to the owner (11 Oct ~07:05 UTC)

- **overstated**: 1. Showing the owner the reader-disagreement tiles first got no.87 under 2% error in 7 of his decisions; a random order needed about 53.
  - Evidence: - 7 and 53 are the x figures; as measured they are 10 vs 100 (TRANSCRIPTION.md:36).
- The scope is the eval lines only (371/376 of 803 signs).
- The oracle stands in for the owner.
- The x base is already 2.7%.
- q7 alone fixed a five-tile T98-for-T18 pile (cluster 102), 8 wrong to 3.
- Random's range is 1-165 (x) and 26 to never (m).
  - Corrected: In a simulation on the held-out part of no.87 (about 375 of 803 signs), with the known answer playing you, showing reader-disagreement tiles first reached 2% error in 7 questions with flagged signs excluded and in 10 as measured. Random orders needed a median of about 53 and 100 (ranges 1-165 and 26 to never). Most of the gain was one question that fixed a five-tile T98-for-T18 pile.
- **wrong**: 2a. The sorter's own 'most useful' (lattice) ranking did no better than random.
  - Evidence: - At the registered endpoint (eval pile x, k=20) the lattice left 5 wrong against a random median of 10 and mean of 8.9, beating 16 of 20 seeds. It missed only the strict best-of-20 bar (4), by one sign.
- It beat all 20 seeds at k=20 under pile m, none x, none m and dev.
- In the primary setting it is at random level at k=10 (it fixed nothing in its first ten unflagged questions) and at k=100 (4 vs mean 4.3).
- Its k=20 edge there is one pile hit at q16, after it broke 2 at q15.
- It trails disagree by 3 tiles at k=20, p 0.25.
  - Corrected: The lattice ranking missed the pre-set bar by one sign in the main setting: it beat most random orders at 20 questions but fixed nothing in its first ten. It trailed the disagreement order by 3 signs, which one leaf cannot separate from chance.
- **overstated**: 2b. Nor did the classifier-margin order (do better than random).
  - Evidence: - Per tile it is at random level: none x k=20 9 vs random 8-10; none m 14 vs 13-15.
- Under pile it beat 16-17 of 20 seeds at k=20, through one pile hit at q12, and all 20 at k=100 under x.
- Its first 11 questions fixed nothing in either convention.
- It missed the bar by one sign in every setting.
  - Corrected: The shape-margin order fixed nothing in its first eleven questions and, deciding tile by tile, did no better than random. With pile spreading it beat most random orders only because one question hit the five-tile T98/T18 pile.
- **overstated**: 3a. 'Check these first' should list reader-disagreement tiles first.
  - Evidence: - Disagree is the registered winner at k=20 in all four non-cluster settings, beating all 20 random seeds each time.
- Its lead over the current doubt feed is 2 vs 0 tiles (x, p 0.5) and 4 vs 1 (m, p 0.375).
- The current feed is ahead per tile at k=50-100 and reaches 2% sooner under pile x (3 vs 7).
- The 'then the rest of the doubt feed' order was not tested by TXE3-1. An unregistered re-run of it on already-inspected lines is at or better than the current feed in every cell except pile x k=10, but not uniformly better than disagree alone (pile m k=50/100: 6/3 vs 5/2).
  - Corrected: Putting reader-disagreement tiles at the top was the best of the registered orders for the first 20 questions on this one leaf, 2-3 signs ahead of the current doubt feed, within chance. Keeping the rest of the doubt feed after them is untested by TXE3-1, though an unregistered re-run suggests it is at least as good as today's feed.
- **overstated**: 3b. A decision should spread only within its own pile.
  - Evidence: - Pile beat per-tile for every informed order at k=20 (x: 2 vs 5, 5 vs 7, 5 vs 9, 4 vs 7), mostly through cluster 102.
- For random orders the mean gain is about 0.5 sign.
- Even with a perfect oracle, pile spreading broke 2 correct tiles: in the lattice order, and in two random seeds (5 and 16) via a mixed T24/T45 pile in cluster 132.
- Real-owner wrong calls spreading across a pile are untested.
  - Corrected: With the known answer playing you, spreading a decision within its pile helped, mostly through one five-tile pile. Even a correct decision broke 2 correct signs when a pile mixed two true signs, and spreading your real decisions is untested. 'At most the pile' is supported; 'always spread within the pile' is not.
- **holds**: 3c. Never spread a decision across a whole shape cluster.
  - Evidence: Cluster runs reproduce byte for byte. At k=20 every non-oracle order ends far worse than the base: x named orders 35-65 and random 30-78 vs 10; m 43-70 vs 15. This replicates X6 on the same atlas and the same base signs (C = L, 0 of 402 differ). It is not new evidence.
  - Corrected: On no.87 with the current 140-cluster atlas, spreading a decision to a whole shape cluster made every order worse, as X6 had already found. Another atlas or hand needs its own check.

### Sentence the parent may give the owner

In a simulation on the held-out part of no.87 (about 375 of its 803 signs), with the known answer standing in for you, putting the tiles where our two readers disagreed first reached 2% error in 7 questions with flagged signs excluded and 10 as measured, against a median of about 53 and 100 for random orders (ranges 1-165 and 26 to never). Most of that was one question that fixed a five-tile T98-for-T18 pile, and it led the current doubt feed by only 2-3 signs at 20 questions. The lattice ranking missed the pre-set bar by one sign while still beating most random orders. Spreading a decision across a whole shape cluster made every order worse, as found before. None of this has yet been tried with your real decisions.
