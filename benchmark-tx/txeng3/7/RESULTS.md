# TXE3-7 PROPAGATE results (11 Oct 2026, 05:4x-06:1x UTC by date -u; account 3, worker session_01N6wTuin3FG55h6UUkN9Kpo)

Prereg `benchmark-tx/PREREG-txeng3-7.md` (c351e72e / ecde11e9) pushed before any score; every arm output committed (65a3c574) before
`score.py` ran. Disk only: 0 network requests, 0 vision calls, 0 subagents. Scorer: `tools/tx_bench.py --exclude-flagged --paired`
(the fixed scorer of 10 Oct; the line read of record re-scores 0.069 on f152r where TXP-152's file figure was 0.082).

## Question
Does the owner's Birago 1572 sort, as committed, lower err_true on a letter he never sorted -- and is any gain his decisions or
just labelled tiles?

## Setup (as pre-registered; deviations stated)
- Owner decisions: `harvest/bir87align/settled_corrected.tsv` (4 Oct sort + corrections; 488 tiles on f.117r/f.144r/f.168).
  Mapped 1:1 to atlas boxes by `sorter/no87/owner_map.tsv`: **438 boxes** (prereg said 445: 7 of those are aside/bad-cut/empty and
  were dropped as the prereg's rule says). Owner and machine labels differ on **121** of the 438 after the pre-registered family
  stripping (T60-c -> T60), not 206: 54 of the mapped moves are within-family splits that the stripping removes. 175 of the 438
  carry `moved`.
- Instrument: `tools/glyph_atlas.py classify --only-train-labels` (new option, offline test added, 5552b57e): the 438 sorted
  tiles are the only voters, labels.json contributes nothing. kNN 5, HOG+PCA features of the whole atlas (unsupervised).
- Arms: A0a cluster-name atlas (labels.json names, no per-tile overrides, no no.87 box voting on no.87, target page excluded on
  f152r); A1 machine labels (start piles); A2 owner labels (final piles); A3 owner labels permuted, seeds 1-20.
  Two outputs each: *atlas* (every 1:1-mapped token takes the kNN top-1) and *override* (line read, kNN code substituted only
  where the 5 votes are unanimous and differ from it).
- Targets: P f152r (never sorted; 73 scored; box map `f152r_box_token.tsv`, 90/96 tokens 1:1, L01 run 7 boxes = 7 tokens);
  S no.87 f178v+f179r (714 mapped tokens through `atlas/no87_box_token.tsv`; f178r unmapped, keeps the line read in every arm;
  figures below are over the whole item, 803 scored).
- Can-vary (counted before scoring, `can_vary.json`): A1 and A2 top-1 differ on **19 of 90** f152r boxes and **125 of 714** no.87
  boxes; A2 differs from each null on 80-90 / 642-700. The control can fail differently from the target: a real test.

## Numbers (`results.tsv`, `results.json`; Wilson 95%; "fe" = flagged excluded, never quoted alone)

| target | output | err_true as measured | flagged excluded | paired base | fixed / broken | sign p |
|---|---|---|---|---|---|---|
| f152r | line read of record (passZ_pipeline) | 0.069 (5/73) 0.030-0.151 | 0.029 (2/70) 0.008-0.098 | -- | -- | -- |
| f152r | A0a cluster-name atlas | 0.192 (14/73) 0.118-0.297 | 0.171 (12/70) | A1 atlas | 16 / 5 | 0.027 |
| f152r | **A1 machine labels, atlas** | **0.384 (28/73) 0.281-0.498** | 0.371 (26/70) 0.268-0.489 | line read | 1 / 20 | <0.001 |
| f152r | **A2 owner labels, atlas** | **0.356 (26/73) 0.256-0.471** | 0.343 (24/70) 0.242-0.460 | A1 atlas | **4 / 3** | **1.0** |
| f152r | A3 null (20 seeds), atlas | 0.781-0.918 | -- | A1 atlas | -- | -- |
| f152r | A1 override | 0.069 (5/73) | 0.029 (2/70) | line read | 0 / 0 | 1.0 |
| f152r | A2 override | 0.069 (5/73) | 0.029 (2/70) | line read | 0 / 0 | 1.0 |
| no.87 | line read of record (passC) | 0.051 (41/803) | 0.038 (30/792) | -- | -- | -- |
| no.87 | A0a cluster-name atlas (names partly from no.87's own tune lines; not gated) | 0.138 (111/803) 0.116-0.164 | 0.126 (100/792) | A1 atlas | 189 / 36 | <0.001 |
| no.87 | **A1 machine labels, atlas** | **0.343 (275/803) 0.310-0.376** | 0.336 (266/792) 0.304-0.369 | line read | 15 / 227 | <0.001 |
| no.87 | **A2 owner labels, atlas** | **0.329 (264/803) 0.297-0.362** | 0.322 (255/792) 0.290-0.355 | A1 atlas | **41 / 33** | **0.416** |
| no.87 | A3 null (20 seeds), atlas | 0.726-0.793 | -- | A1 atlas | -- | -- |
| no.87 | A1 override | 0.066 (53/803) 0.051-0.085 | 0.053 (42/792) | line read | 0 / 11 | 0.001 |
| no.87 | A2 override | 0.080 (64/803) 0.063-0.100 | 0.067 (53/792) | line read | 0 / 22 | <0.001 |

Gate "transfers" (A2 <= A1 - 0.02 AND fixed > broken at p < 0.05 AND gain > null p95): **f152r FAIL** (gain +0.027 but 4 fixed /
3 broken, p 1.0); **no.87 FAIL** (gain +0.014, 41 / 33, p 0.42). Null gains are all deeply negative (f152r p95 -0.41, no.87 -0.39):
both A1 and A2 carry real shape information against a permuted null; the owner's labels are not distinguishable from the
machine's start labels on either letter.

Gain per owner decision: f152r net +2 signs of 73 over 206 decisions (0.010 signs per decision; 19 decisions reached the target
at the kNN, 4 fixed / 3 broken); no.87 net +11 of 803 over 206 (0.053 per decision; 125 reached, 41 / 33). Pooled P+S: fixed 45 /
broken 36, sign p = 0.37 (two-sided binomial) -- a null.

What the owner's labels change, by confusion (A2 vs A1 top confusions, no.87): e<-T60 x23 in both; a<-T60 8 -> 15 and o<-X_NEW
0 -> 12 appear under the owner's labels (his T60 and X_NEW-* piles absorb a- and o-valued tiles), while a<-T92 x6 and d<-T98 x7
drop out. The owner's decisions move errors between classes about as much as they remove them.

The override outputs: on f152r neither arm's unanimous votes ever disagree with the line read (0 / 0); on no.87 every unanimous
disagreement is wrong (A1 0 fixed / 11 broken, A2 0 / 22). A kNN on 438 sorted tiles, owner-labelled or not, has no sign it can
correct in a 5%-error line read.

## Reading
1. **The rule has now been measured, and the measured transfer is null.** The owner's Birago 1572 sort, carried to a letter he never
   sorted through the family atlas, reads the same as the machine's own start labels on the same 438 tiles (f152r 0.356 vs 0.384,
   4 fixed / 3 broken; no.87 0.329 vs 0.343, 41 / 33). What transfers is *labelled tiles of the hand*, not the owner's corrections:
   either label set beats a permuted null by 0.4 err_true, and the two differ by noise.
2. **Both are far below the product.** A kNN from the sorted tiles alone reads at 0.33-0.38, the cluster-name atlas at 0.14-0.19,
   the line read at 0.05-0.07. Propagating any tile labels through the atlas cannot improve a line read on this hand; as an
   override it only breaks (0 fixed / 33 broken pooled).
3. This agrees with BIR-OWNERSORT (the sort makes his own leaves' decodes worse) and BIR87-ALIGN (his piles take the family
   values and support no split), and it removes MQS-CLASSIFY-ROUNDS's caveat: that run's zero gain was blamed on no.87's own tune
   tiles out-voting the owner's; with the owner's tiles as the ONLY voters the gain is still within noise.
4. Limits: value-level err_true (homophone swaps invisible); f152r has 73 scored signs (0.02 = 1.5 signs), so P alone could only
   show a large effect; the no.87 figure pools f178v L01-12 (the atlas's tune lines) with the held-out lines, which does not touch
   arms A1-A3 (labels.json never votes there) but means A0a on no.87 is reported, not gated; one tile-to-box map (centre shift,
   label-blind) and one classifier (kNN 5, the atlas's features) were tested -- a different classifier is a different instrument.

## What it means for the owner (three plain sentences)
Your 4 Oct Birago sort, applied through the family atlas to a letter you never sorted, reads no better than the machine's starting
labels on the same tiles: your corrections neither help nor hurt there, within noise. Reusing your sorts family-wide is therefore
safe but, by this measurement, not a gain; the atlas route it rides on reads five to seven times worse than the line reads on this
hand, so the rule should be stated as "owner decisions are carried forward so you are never asked twice", not as an accuracy step.
The place your sorting did move a number stays the no.87 clerk-sheet alignment (BIR87-ALIGN), and the next owner session worth your
ten minutes is one where the tiles you settle are scored against a benchmark the same day.

## For the rule (TRANSCRIPTION.md, "Owner sorts are reused family-wide")
Keep the reuse (it costs nothing and avoids asking twice) but drop any expectation of an err_true gain from it until a classifier
on this hand reads below the line reads; a brief that promises "apply the owner's decisions first" as an accuracy step cites this
null. The sorter's value is where a decision feeds a key-value alignment or a lookalike question, not the atlas classifier.

## Next step and cost
The one instrument not yet tried for transfer is *decision-level* propagation without the atlas: carry each owner move as a
(line-read sign A -> sign B) relabel rule for tiles whose kNN neighbours are owner-moved tiles, applied to the line read, and score
paired fixed/broken on no.87 + f152r -- about USD 4, disk only, 45 min, Sonnet. Expected: small, because 141 of his 206 moves cross a
family and BIR87-ALIGN found the clerk siding with the committed label on most seeded re-pilings. A second Birago 1572 letter with a
known answer beyond f152r (nos.71/73/82/85/86/90 have none) would add power; none can be built without new material.
