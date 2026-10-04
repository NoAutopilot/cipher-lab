# BIR87-ALIGN results (4 Oct 2026, 15:52-16:1x UTC, account-3 worker)

Brief `.claude/briefs/runs/2026-10-04-acct3-bir87-align.md`. Prereg `PREREG.md` pushed at 8a78f226 before any alignment run
(its clock time was corrected from "16:1x" to "15:5x" in the next commit, rule 6; nothing else changed). Disk only: 0 requests,
0 vision calls, 0 subagents. Scripts: `relabel.py` (step 1), `run.py` (step 2, ~8 min), `../ownersort/ownersort.py` with new options
`--corrections`, `--pile-values`, `--pv-moved-only`, `--tag` (step 3, outputs `../ownersort/v4_*/`). One shared-script change:
`../align87/build_pairs.py --cipher-dir` (+ "P:<pile>" codes); default output byte-identical to the committed `pairs.tsv` (checked).

## Step 1: sequences (`relabel_counts.json`)
no.87, 853 tokens. Primary `cipher_owner/`: **205 owner-labelled** (186 kept, 18 moved, 1 not-letter), **648 atlas/line-read**
(31 sorter tiles have no token, 9 map 2:1/1:2, 3 bad-cut: committed label kept). Sensitivity `cipher_moved/`: 19 owner-labelled
(18 moved + 1 not-letter), 834 committed. Owner piles reached in no.87: T45 54, T60 43, T37 42, T19 36, T89-b 10, X_NEW-l 7,
T24-b 6, T86 2, T60-d 1, T85-b 1, T85 1, T33 1. T19-d, T83-b, T37-b tiles did not map 1:1 and are not in the sequence.
4 Oct sort: `corrections.tsv` (8 rows) applied to `settled_labels.tsv` -> `settled_corrected.tsv`, 7 tiles changed (the
f144r_L04.1_07 UNPLACED row is superseded by its later T60-e row).

## Step 2: clerk-sheet alignment (`summary.json`, `piles.tsv`, `null.tsv`)
| sequence | real 'agrees' | shuffled-sheet mean / max (20 seeds) | gate |
|---|---|---|---|
| committed labels (NEVBIR-87ALIGN re-run) | 0.896 | 0.351 / 0.376 | pass (reproduces) |
| **owner piles (primary)** | **0.848** | 0.318 / 0.338 | **pass** |
| owner moves only (sensitivity) | 0.890 | 0.349 / 0.374 | pass |

Per owner pile, primary (C = n>=2, agree>=2, share>=0.6 and share above the pile's own shuffled max):
| pile | n | clerk value | agree | share | null max | grade |
|---|---|---|---|---|---|---|
| T45 | 52 | e | 43 | 0.827 | 0.278 | C |
| T60 | 43 | n | 37 | 0.860 | 0.214 | C |
| T37 | 42 | a | 29 | 0.690 | 0.317 | C |
| T19 | 36 | o | 31 | 0.861 | 0.306 | C |
| X_NEW-l | 7 | o | 6 | 0.857 | 0.571 | C |
| T89-b (word) | 10 | che | 4 | 0.400 | 0.200 | M |
| T24-b | 6 | f | 3 | 0.500 | 0.667 | M |
| T86 | 2 | n | 1 | 0.500 | 1.000 | M |
| T60-d, T85-b, T85, T33 | 1 each | g, a, a, u | 1 | -- | -- | no evidence |
Sensitivity (moves only): T37 a 5/6 C, T60 n 4/5 C, T24-b f 2/3 M (not above null), the rest no evidence.

**Every C value equals the printed 1572 value of the pile's family** (T45 e, T60 n, T37 a, T19 o). No pile gets a value the printed
table lacks.

**Split families.** T19 vs X_NEW-l: both C, both o -> **over-split, merge recommended (not applied)**; caveat: all 7 no.87 X_NEW-l
tiles are `kept` (the sorter's seed, 6 of them committed T19), so this is a test of the seed pile, not of an owner move.
T60 vs T60-d (1 tile), T85 vs T85-b (1), T24-b (parent absent), T86, T83-b, T19-b/c/d, T60-c/e: **no evidence** (< 2 aligned
occurrences, or no C on one side). No REAL homophone split is supported.

**Where the owner pile and the committed label differ** (`disagreements.tsv`, 60 tokens): on the 53 `kept` tokens the seed had put in
another pile, the clerk sides with the committed label 30, with the pile 1, both 11, neither 11; on the 7 `moved` tokens, committed 2,
owner 2, both 2, neither 1. The seed's re-pilings the owner left in place are mostly wrong by the clerk; the owner's own moves split
evenly at this N. The primary run's lower agreement (0.848 vs 0.896) is mainly these seeded kept tiles.

## Step 3: re-decode gate (BIR-OWNER random-change control, 200 draws, seed 20261004; `../ownersort/v4_*/score.json`)
C piles (T19, T37, T45, T60, X_NEW-l) with corrections applied, `--new-piles-unknown`. Two applications reported: as pre-registered
(kept + moved tiles in a C pile take its value, `v4_bir87`) and moves only (`v4_bir87_moved`, BIR-OWNERSORT's own kept = no change
rule: the pre-registered wording re-imports the documented kept bug -- kept tiles whose start pile differs from the mapped base sign).
Both reported; the verdict does not depend on the choice.
| leaf | a (current) | v2 b (owner sort, before) | corrections only | **b, C values, moves only** | p95 | rank /201 | gate |
|---|---|---|---|---|---|---|---|
| f.117r (fr) | -1.215 | -1.361 | -1.350 | **-1.337** | -1.296 | 39 | FAIL |
| f.144r (it16dip) | -1.418 | -1.376 (PASS, rank 5) | -1.638 | **-1.655** | -1.472 | 61 | FAIL |
| f.168 (it16dip) | -1.149 | -1.674 | -1.674 | **-1.583** | -1.293 | 194 | FAIL |
| pooled | -1.239 | -1.435 | -1.473 | **-1.449** | -1.398 | | FAIL |
As pre-registered (kept included): f.117r -1.376 (rank 70), f.168 -1.583 (193), f.144r -1.655 (58), pooled -1.472: FAIL.

Judge on the moves-only b texts (`tools/judge_plaintext.py <spec> --file ../ownersort/v4_bir87_moved/text_b_<leaf>.txt`):

    f117  b FAIL language: score=-1.337, null_p99=-1.778, real_p05=-0.912, real_median=-0.783, mode=both, N=245
    f144r b FAIL language: score=-1.655, null_p99=-1.584, real_p05=-0.997, real_median=-0.82,  mode=both, N=70
    f168  b FAIL language: score=-1.583, null_p99=-1.616, real_p05=-0.96,  real_median=-0.822, mode=both, N=97

**The gate does not move.** The C values change only the X_NEW-l tiles ('?' -> o; T19-family moves into X_NEW-l now cost nothing):
small gains on f.168 (-1.674 -> -1.583) and f.117r, still FAIL. f.144r loses its v2 PASS, and the loss comes from the owner's own
7 corrections (corrections only: -1.376 -> -1.638; three f.144r tiles: L04.1_07 e -> '?', L05_19 '?' -> t, L06_17 e -> n), not from
the C values. f.144r b now scores below its own shuffled null p99.

## Verdict
The owner's no.87 piles align to the clerk's sheet far above the shuffled null, and the four large piles take exactly the printed
values. The clerk alignment, a second instrument with no LM, finds no key-value error in the 1572 table for any pile it can test.
It also finds no homophone split. So BIR-ADJ's conflict (the owner is right about shape, yet the key values make the texts worse) is
**not explained by wrong key values for the piles no.87 can test**. What is left is the tile-to-position mapping on f.117/f.144r/f.168
(BIR-ADJ's own next step), or the small new piles that never occur in no.87 (T60-c/-e, T19-b/c/d, T83-b, T85-b...: no evidence, not
refuted). No key file, exceptions file or reading changed. `proposals_C.tsv` holds the C rows (all "confirms printed", plus the
X_NEW-l -> T19 merge recommendation).
Next (not done): BIR-ADJ's mapping check on the 98 owner-right tiles (~USD 2); a verifier on this alignment (ROOM line).
