# TXE-P results: ink-density split flags (M8), dint-f128-print (dev), 9 Oct 2026

Verdict: **FAIL** -- recall 1/11 (0.09) of pass F's 9 insertions + pass A's 2 deletions at a pooled A+F flag share of
15/360 (4.2%); gate recall >= 0.6 at <= 15% flagged. Chance at F's 7.1% share and A's 1.1% expects about 0.7 caught, so
the one catch is chance level, and it is itself an alignment artifact (F L05: 'o' deleted at 29|30 and 0' inserted at 31
is one misread that tx_bench's aligner scores as a deletion plus an insertion). 0 vision calls; no eval item has this hand.

Flags committed before truth: 221d819db (README.md there carries the scoring rule, fixed before tx_bench was run).
Tool: `tools/tx_split_groups.py` (build; `--score` after the commit); test `tools/tests/test_tx_split_groups.py` (4 tests).

## Gap sweep (pieces per stitched line, core rows, ink < 120; s1+s2 stitched by manifest boxes, 1100 px overlap dropped)

| line | g2 | g3 | g4 | g5 | g6 | g8 | g10 | g12 | A | B | F | gap = A / B / F |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L02 | 35 | 29 | 25 | 22 | 20 | 20 | 18 | 16 | 9 | 8 | 8 | none (unfit: band holds non-cipher ink) |
| L03 | 49 | 45 | 40 | 37 | 34 | 25 | 20 | 16 | 56 | 56 | 58 | none / none / none (nearest g2) |
| L04 | 45 | 41 | 38 | 35 | 33 | 25 | 19 | 16 | 60 | 61 | 60 | none / none / none (nearest g2) |
| L05 | 61 | 55 | 51 | 48 | 42 | 36 | 28 | 25 | 61 | 62 | 65 | 2 / none / none |

Read-free finding before any truth: on L03 and L04 no gap in 2..12 opens the ink to any pass's count (even gap 1 gives
55 and 48): this hand joins signs with no blank column at all, so a blank-column profile cannot count them. Only L05
reaches a pass count.

## Flags (benchmark-tx/txeng/split/flags.tsv): A 2 (1.1%), B 4 (2.2%), F 13 (7.1%), all kind 'over'

## Scoring (tx_split_groups.py --score, tx_bench align, label-mapped; benchmark-tx/txeng/split/events.tsv)

| pass | tx_bench (whole item) | inserted caught (fitted lines) | deleted caught | flag share |
|---|---|---|---|---|
| A | err_true 0.247, wrong 12 deleted 2 inserted 7 | 0 / 6 | 0 / 2 | 0.011 |
| B | err_true 0.188, wrong 11 deleted 0 inserted 5 | 0 / 5 | -- | 0.022 |
| F | err_true 0.271, wrong 13 deleted 1 inserted 9 | 1 / 9 | 1 / 1 | 0.071 |

Gate set (F inserted 9 + A deleted 2): caught 1 of 11, recall 0.09, at 4.2% pooled flag share. FAIL.

## What the errors are (why the instrument misses)
F's 9 insertions are 5 dots ('.'), 2 primed zeros (0'), 'c' and a dash -- extra small marks, not a glued digit group
split in two; A's 2 deletions are a dot and an 'f'. The taxonomy's class 3 ("segmentation of glued digit groups") is,
on these events, a *dot and diacritic* class: whether a small mark is a sign. Column ink profiles count wide ink, not
dots (a dot either sits in a gap or overlaps its neighbour's columns), so the instrument is aimed at the wrong unit.

Follow-up (one line, not started): a dot/mark detector (small connected components by area and baseline height, from
the line crop) would aim at what F actually inserts; the lane decides.

Call count: 0 vision calls, 0 subagents.
