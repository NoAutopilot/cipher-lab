# PREREG TXE3-7 PROPAGATE (account 3, worker session_01N6wTuin3FG55h6UUkN9Kpo; written 11 Oct 2026 06:0x UTC by date -u, pushed BEFORE any score)

One of ten TXE3 transcription experiments (account-3 parent, 11 Oct 2026). Work folder `benchmark-tx/txeng3/7/`. Disk only:
no network, no vision calls to a model, no owner page touched, no confirm item scored, no *.truth.tsv edited. Cap USD 15 / 2 h.

## Question
TRANSCRIPTION.md's rule since 5 Oct 2026: "owner sorts are reused family-wide". Never measured. Does the owner's Birago 1572
sort, exactly as committed, lower err_true on a letter he never sorted? And is any gain his *decisions*, or just labelled tiles?

## What is on file and is not re-run (read first)
- MQS-CLASSIFY-ROUNDS (9 Oct 2026, tools/tests/PREREG-MQS-CLASSIFY-ROUNDS.md): the 3 Oct owner sort (448 boxes) layered as
  `--train-labels` ON TOP of `atlas/labels.json` moved no.87 held-out err_true 0.162 -> 0.162 (gain 0.000; the same-hand
  positive control gained 0.010 under a 0.02 gate). Its own reading: the kNN vote on a no.87 box is dominated by no.87's own
  309 clerk-truth tune-tile overrides, so labels added elsewhere never reach it. That is a design in which the owner's tiles
  could not vote, not a test of transfer. This experiment changes the instrument (the person's tiles are the ONLY voters;
  labels.json contributes nothing) and the target (f152r, never sorted), so rule 3's third-attempt clause does not bite.
- BIR-OWNERSORT / BIR87-ALIGN (4 Oct 2026): the owner's sort fails the key-decode gate on his own three leaves (every leaf below
  the random-change control p95); on no.87 his big piles align to the clerk sheet at exactly their family's printed value
  (T45 e, T60 n, T37 a, T19 o); no homophone split supported. Nothing was applied.
- "reconciled plus the owner's sorted labels 0.042" (the brief): that figure is output L = committed passC + the X_CE relabels of
  NO87-LABELS, a value-blind *Sonnet* read of 42 no.87 tiles (T50/T46/T98/T52) cut from no.87 itself
  (`harvest/lookalike_87/no87_labels/mk.py`). It is not an owner decision, it was cut from the eval leaf (leakage if used as
  training for no.87), and TXP-152 found none of its relabels apply on f152r. It is NOT used here. The owner's own no.87 sort
  (4 Oct, `sorter/no87/owner-sort-2026-10-04/settled_no87.tsv`: 21 moved, 217 kept = the computer's seeds) has never been scored
  as err_true against the benchmark; it is a target-leaf sort, so it is not training here either.

## Owner decisions used (as committed)
`ciphers/nevers-birago-fr3251-1572/harvest/bir87align/settled_corrected.tsv` = `sorter/owner-sort-2026-10-04/settled_labels.tsv`
with `corrections.tsv` applied (the ASKS 118 page, DHiLGFWiqrHxQYzLrFNh6s, exported 4 Oct 2026): 488 tiles on f.117r (fr.3252),
f.144r, f.168r/v; kept 274, moved 206, aside 5, bad-cut 3. Of the 206 moves 141 change family and 65 are splits within a family.
Tile -> atlas box: `sorter/no87/owner_map.tsv` (label-blind centre shift; 445 map 1:1, 34 share a box, 9 unmatched). Only the 445
1:1 boxes are used; aside / bad-cut / empty labels are dropped. A pile name's family suffix is stripped (T60-c -> T60, X_NEW-l ->
X_NEW) because BIR87-ALIGN found every testable owner pile carries its family's printed value and tx_bench scores values.

## Targets (both BENCHMARK-TX eval items; no confirm item)
- **P, primary: birago1572-f152r** (no.77, no.87's hand, 73 scored / 24 excluded, 3 flagged). The owner never sorted it and it
  was on no sorter page. Baseline of record: `outputs/birago1572-f152r/passZ_pipeline.tsv` 0.082 (6/73); committed 0.069.
  Box -> token: a new label-blind width-DP map (the DP of `atlas/no87_map.py`, unchanged) on atlas page f152r lines 2-5 =
  letter L01-L04, after removing prose boxes by an x bound read from the line image (L01: cipher run right of x = 2520 src px,
  after "...et che bisogna"; L04: left of x = 2460, before ", con uolermi"); 1:1 boxes only.
- **S, secondary: birago1572-no87**, f178v L01-23 + f179r L01-03 through `atlas/no87_box_token.tsv` (1:1 rows; f178r is not
  in that map). The owner's later no.87 piles are excluded from training, so with respect to the decisions tested this is also
  a letter he had not sorted; it is the atlas's tune leaf for cluster names, which matters only for arm A0-atlas.

## Instrument
`tools/glyph_atlas.py classify` gains `--only-train-labels`: with it, every box without a `--train-labels` row is treated as
held (never votes, no cluster code), so the kNN is built from the person's sorted tiles alone and labels.json contributes
nothing. Offline test in tools/tests/test_glyph_atlas.py. Settings fixed: `--knn 5 --pca-scale unit --topk 3 --page <target>`
(features are the atlas's own unsupervised HOG+PCA fit, no labels). Scoring: `tools/tx_bench.py --exclude-flagged --paired`.

## Arms (the same 445 boxes in every arm; only the labels change)
- **A0** the pipeline without any person's labels: the line read of record (f152r passZ_pipeline; no.87 passC) and, beside it,
  the family atlas's cluster-name classifier (labels.json `signs` cluster names only, the 309 per-tile overrides removed,
  `--exclude-page`; on no.87 those names came partly from its own tune lines, so A0-atlas is reported there, not gated).
- **A1 MACHINE control**: kNN from the 445 boxes labelled `old_sign` (the start piles = the reconciled machine read after the
  look-alike pass). Same tiles, same count, no owner decision.
- **A2 OWNER**: kNN from the same 445 boxes labelled `new_sign` (corrected). A1 and A2 differ at exactly the 206 moved tiles
  (+7 corrections): the difference A2 - A1 is the owner's decisions and nothing else.
- **A3 null**: A2 with `new_sign` permuted among the 445 boxes, seeds 1-20 (same codes, same count, correctness destroyed).
Each arm gives two outputs per target: **atlas** -- every token with a 1:1 box takes the kNN top-1 (a `_` top-1 keeps the line
read), tokens without a box keep the line read's sign (identical in every arm, so they cancel in paired scoring); **override** --
the line read with the kNN code substituted only where the 5 votes are unanimous (share 1.00), the code is a cipher sign and it
differs from the line read (a fixed rule, nothing tuned: no dev item of this hand exists).

## Control proof that the statistic can vary (rule 3)
A1 and A2 carry different labels on 206 of 445 voters. Before any truth is read, count the target boxes whose top-1 differs
between A1 and A2 (and between A2 and each A3 seed). If that count is 0 on a target, the decisions never reach it: logged as
a NON-TEST for that target, not a negative. The permutation null varies for the same reason.

## Endpoint and gate
err_true from tx_bench per target and arm, as measured AND flagged-excluded, Wilson 95%; `--paired` A2 vs A1 (fixed / broken,
sign p); A2 vs A0 line read likewise. Gain per owner decision = (A1 errors - A2 errors) / 206, and per decision that reached
the target (boxes whose top-1 changed). **Transfers** on a target iff A2 err_true <= A1 - 0.02 AND fixed > broken with sign
p < 0.05 AND the gain exceeds the p95 of the 20 null gains. Anything else is a null result (reported as such). Pooled P+S
figures reported beside. Power, stated now: f152r's 73 scored signs make 0.02 = 1.5 signs and a sign test needs >= 5 net fixes --
P can show only a large transfer; S (~700 mapped scored signs) carries the power.

## Expected (written before scoring)
|A2 - A1| < 0.02 on both targets (BIR-OWNERSORT: the moves make the decoded texts worse; MQS-CLASSIFY-ROUNDS: no gain), the
override outputs break more than they fix (atlas top-1 0.16-0.32 vs line reads 0.04-0.05). A null is a result.

## Stop rule
No vision calls at all. If the f152r DP map gives fewer than 78 of 97 tokens a 1:1 box, or the mapped run falls on the prose
side of the x bounds, f152r is logged "unmapped" and only S is scored. Stop before any unit that would cross 80% of cap or box.
