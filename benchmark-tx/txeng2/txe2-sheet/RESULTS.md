# TXE2-SHEET (PREREG benchmark-tx/PREREG-txeng2-2.md X1) -- detector gate FAIL; the blind read was not run

Worker TXE2-SHEET (account 4, Opus) for LANE TX-ENGINEER-2, 9 Oct 2026, 16:33-16:4x UTC by date -u. Read-free: no
vision call, no model read, no eval item scored, no truth file edited. Cost: the orchestrator's get_session reading.

## What ran

`tools/tx_offsheet.py detect` on the two dev items the PREREG names (configs in `items/`):

- tiles: each line crop binarised (Otsu), the cipher band taken from the row-ink profile (f.89) or a fixed band
  0.47-0.72 of crop height (f.128, set from the debug overlay after the profile band took gloss and next line, BEFORE
  scoring), connected components merged by x-overlap; f.128's s1/s2 joined at the best column-profile overlap.
  Blobs aligned to a skeleton read that keeps its CLEAR rows (f.128: `f128/passA.tsv`; f.89: `passA.tsv`), then mapped
  to the reference positions with `tx_bench.align`. Overlays: `debug/*_tiles.png` (one-off shifts are visible in places;
  this is a stated limit).
- sheet cells: no Dinteville sheet image exists (the pass brief's sheet is a text list), so each cell is represented
  by its consensus tiles (both readers give that label at that position): 20 cells on f.128, 21 on f.89.
- off-sheet score: min over cells of the mean correlation-plus-orientation distance to the cell's 3 nearest consensus
  tiles (self excluded). Flagged: every reader NEW:/X_/? position, then the top scores, 15% of tiled positions in all
  (q caps the union, fixed in the tool before scoring).
- `detect_*.tsv` + overlays committed in c9daaeb50 BEFORE `recall` was run.

Only `line`, `pos` and `ref_sign` (the reconciled read) of each item's truth file are read by detect; truth values are
read only by `recall` (`tx_bench.position_errors`).

## Result (gate: >= 0.5 of the baseline's errors at <= 15% flagged)

| item (baseline) | tiled | flagged | share tiled / scored | baseline errors | caught | recall |
|---|---|---|---|---|---|---|
| dint-f128-print (pass B, `--label-map`) | 180 | 27 | 0.150 / 0.153 | 11 | 0 | 0.00 |
| dint-f89-gloss (passZ_pipeline) | 559 | 83 (44 reader-flagged) | 0.148 / 0.083 | 10 | 0 | 0.00 |
| pooled | 739 | 110 | 0.149 | 21 | 0 | **0.00** |

`python3 tools/tx_offsheet.py recall items/dint-f128-print.json --det detect_dint-f128-print.tsv --base benchmark-tx/outputs/dint-f128-print/passB.tsv`:
`{"errors": 11, "caught": 0, "errors_untiled": 0, "tiled": 180, "flagged": 27, "share_tiled": 0.15, "scored": 85, "flagged_scored": 13, "share_scored": 0.153}`
`python3 tools/tx_offsheet.py recall items/dint-f89-gloss.json --det detect_dint-f89-gloss.tsv --base benchmark-tx/txeng2/dint-f89-gloss/passZ_pipeline.tsv`:
`{"errors": 10, "caught": 0, "errors_untiled": 0, "tiled": 559, "flagged": 83, "share_tiled": 0.148, "scored": 240, "flagged_scored": 20, "share_scored": 0.083}`

**FAIL.** Chance at this share is about 3 of 21 (binomial(21, 0.15) gives P(0) = 0.033), so the detector does a little
worse than random. Per the brief, `grow` and the single blind Opus read with the grown sheet were NOT run (gate unmet);
the grow code is in the tool and covered by the offline test only.

## Why (diagnostic, after scoring; no re-tune)

- The baseline's errors are on-sheet tiles: median rank share of the error positions 0.76 on f.128 (all scored 0.55) and
  0.57 on f.89 (0.53), i.e. the misread tiles look MORE like an existing cell than the average tile. They are look-alike
  confusions inside the vocabulary (i<-x, n<-0, n<-4 on f.128; d<-#, n<-0', r<-1 on f.89), not off-inventory signs.
- 8 of f.89's 10 errors and 3 of f.128's 11 are positions where both readers gave the same label (consensus tiles), the
  stated blind spot: such a tile becomes an exemplar of the wrong cell.
- The off-sheet positions the readers DID mark (f.89: 44 X_/NEW positions) are excluded from f.89's truth (class
  off-sheet), and reader flags caught 0 errors on either item; on f.128 the readers marked none. So on these two items
  the D/al/zh inventory gap does not show up as errors at scored positions: the truth rule excludes it or the label map
  absorbs it (D->4, al->a, zh->m).

Reading: the sheet-incompleteness premise is not where these dev errors live; an off-sheet detector, however good, has
no headroom here. This is a result about the error population, not only about this tool's segmentation (which is
imperfect: some tiles shift by one sign).

## Limits

One configuration, as pre-registered (q = 0.15, knn = 3); no tuning after scoring. Segmentation and blob-to-position
alignment are heuristic (overlays in `debug/`). Dinteville has no sheet image, so cells are consensus tiles, not drawn
exemplars. Two dev items, 21 errors.

## Next step (suggestion, not run)

An error-population check before any further sheet instrument: the share of each pool's baseline errors at positions a
reader marked off-sheet or that the truth rule excludes as off-sheet. If it is near zero on the eval pool too, X1's
family is retired for this campaign as untested-by-this-tool / no headroom, not as refuted.

Files: `tools/tx_offsheet.py`, `tools/tests/test_tx_offsheet.py` (ALL PASS), `items/*.json`, `detect_*.tsv`,
`debug/*_tiles.png`; SYSTEM.md and tool_shelf.tsv rows (system_map_check ok).
