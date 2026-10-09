# TXE2-SAME: same-sign retrieval strips (PREREG-txeng2-3 X7; 9 Oct 2026, 17:13-17:2x UTC by date -u)

LANE TX-ENGINEER-2, account 4, Opus 5.5 worker. Brief `.claude/briefs/runs/2026-10-09-account4-txe2-round3.md`.
6 Opus 5.5 reader calls (3 main, 3 control), 0 network. **No eval look**: only dev_tune lines (f178v_L01-12) were scored;
eval_heldout untouched. No truth file edited.

**Verdict: dev FAIL.** Paired against L_dev_tune: **fixed 5, broken 4, sign test p = 1.00** (gate: fixed > broken, p < 0.05).
Output wrong 11 of 343 (L 12): err_true 0.032 (95% 0.018-0.057) against L's 0.035. **The registered control fails as it should**:
with the strips swapped between candidates it **fixed 3 and broke 28** (p < 0.0001, wrong way), wrong 37 of 343 (err_true
0.111). So the readers do match the tile to the strip by shape, but at these positions that matching is no better than L's own read.

Order kept: tool, test, sheets and both keys committed 05048acb3 before any read; main reads + control part 1 cf4e7adc6, part 3,
part 2 + merged df938e308, all before the first `tx_bench` call.

## Build (`tools/tx_same_strip.py build`, test `tools/tests/test_tx_same_strip.py` ok)
- Positions: the X9 combo feed on dev_tune (`latt OR vote OR selfcons` from `txeng2/doubt/dev_tune_signals3.tsv`, truth-free):
  54 positions -> `positions_dev_tune.tsv`. Shown: 48. Not shown (L kept): 5 unmapped (no single 1:1 atlas box in
  `txeng/compare/box_pos.tsv`, the label-blind width DP), 1 with only one candidate strip.
- Candidates per row: L's sign; the lattice runner-up (best `txeng2/latt/topk_d.tsv` candidate != L's sign); the taxonomy pair
  partner (`tx_pair_reread.PAIRS`, highest count in `harvest/confusion_1572.tsv`). Duplicates dropped.
- Strips: up to 6 other occurrences of that sign on **f178v only, as L reads it** (L positions on f178v L01-23 mapped 1:1 to an
  atlas box; cut from the f178v page image through atlas `pages.json`); the tile's own position and its two neighbours never in
  a strip; seeded random choice (seed 0) and seeded random A/B/C order per row. No printed cell, no other leaf, no sign names.
- Tile: `tx_compare.context_tile`, target framed, +-1 neighbour, scale 4x (cap 1100 px wide). One PNG per row, greyscale.
- Control (`--swap-seed 1`): same rows, same letter order; each row's strips cyclically shifted by a seeded nonzero amount
  between candidates while the key keeps the unshifted letter -> sign map.
- Reader: Opus 5.5 subagent, 16 rows per call, given only the row images and the question ("which strip does the framed sign
  belong to, or neither"; pick, H/M/L, note). Resolve: pick -> that strip's sign; neither -> L.

Deviation, disclosed: the PREREG says the control is "one call on the same rows"; it was run in the same 3 x 16 batching as the
main arm so the two arms differ only in the swap. One control row (23) came back "file does not exist; not read" (the file is on
disk, 141,821 bytes): recorded as `neither`, L kept (L is right there, so it moves no count).

## Counts (`breakdown.tsv`: per row pick, conf, outcome)
| arm | picks | neither | changed | fixed | broken | stayed wrong | output wrong / 343 | p |
|---|---|---|---|---|---|---|---|---|
| L (base) | | | | | | | 12 | |
| X7 same-page strips | 44 | 4 | 12 | 5 | 4 | 5 | 11 | 1.00 |
| control, strips swapped (seed 1) | 43 | 5 | 35 | 3 | 28 | 7 | 37 | < 0.0001 (wrong way) |

The 48 shown rows hold 10 of L's 12 dev errors.
- Fixed (main): L05.1 T76->T66, L10.4 T76->T66, L11.5 T76->T66 (the n/e family), L06.18 T98->T18 (d/s), L10.1 T92->T53.
- Broken (main): three **L-confidence** picks of T13->T64 (L01.26, L07.25, L09.9; the reader's own notes: "both strips m,
  indistinguishable") and one H pick L11.22 T42->T83.
- Stayed wrong: L05.4 (T90 kept), L05.9 (T64 kept), L06.27 (T76 kept; the truth is not among the candidates per X3), L10.31
  (picked T18, still wrong), L11.29 (neither).
- Post hoc, not a gate: dropping L-confidence picks gives fixed 5, broken 1 (p = 0.22); declared after the score, so it is a
  lead for a registered rule, not a result.

## Reading (against the PREREG's stated difference from the retired compare family)
TXE-A's foreign/printed exemplars pulled the reader the wrong way (fixed 4, broken 16, p = 0.012). With every exemplar the hand's
own page as L reads it, the wrong-way pull is gone (5 vs 4), and the swapped control shows the picks follow the strips. That is
consistent with the PREREG's "a right-way result says the pull came from foreign exemplars", but the right-way margin is one sign
and p = 1.00, so this is not a pass and it adds no signs. Most broken picks are T13/T64 rows where L's own reading of the
page puts near-identical m-like forms in both strips: same-page strips inherit L's own label noise for that pair.

## Follow-ups (one line each, not started)
- A registered "act on H/M picks only" rule on a fresh dev unit (the post-hoc 5/1 above).
- T13/T64: the strips cannot separate them while L's own labels for that pair on f178v are mixed; a sorter question, not a reader one.

Files: `positions_dev_tune.tsv`, `sheets_main/`, `sheets_swap/`, `key_main/key.tsv`, `key_swap/key.tsv` (never given to a
reader), `reads_main.tsv`, `reads_swap*.tsv`, `passX7_dev_tune.tsv`, `passX7swap_dev_tune.tsv`, `breakdown.tsv`.
Cost: the orchestrator's get_session reading.
