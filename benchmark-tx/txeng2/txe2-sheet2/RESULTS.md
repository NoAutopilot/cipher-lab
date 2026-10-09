# TXE2-SHEET2 (PREREG benchmark-tx/PREREG-txeng2-4.md X1b) -- declared Spinelli gate MET (8/14 at 14.9%), carried mostly by the readers' own NEW flags; f152r 0/5, eval_heldout 5/15

Worker TXE2-SHEET2 (account 4, Opus) for LANE TX-ENGINEER-2, 9 Oct 2026, 17:48-17:5x UTC by date -u. Cost: the
orchestrator's get_session reading.

**Read-free.** No vision call, no reader, no subagent, no network beyond git; no truth file edited. The three tables
below are **flag-vs-error recall tables, NOT eval looks**: no instrument output is scored, only the overlap between the
detector's flagged positions and the baseline's existing errors (as TXE-O's eval tables did). No eval look and no S2 look
was spent. The grown-sheet READ is not part of this job and was not run.

## What ran (configuration unchanged from X1: q = 0.15, knn = 3; no tuning after scoring)

`tools/tx_offsheet.py detect` on the three items X1b names (`items/*.json`): Spinelli confirm (crops
`txeng/confirm/crops`, skeleton and readers `outputs/spinelli-c1519-confirm/passA_txeq` + `passB_txeq`,
`--label-map txeng/confirm/collapse_map.tsv`), birago1572-f152r (`txeng2/f152r/crops`, readers passA/passB), no.87
eval_heldout (harvest f178v L13-23 + f179r L01-03 crops, readers no.87 passA/passB). Band by row profile on all three
(null band; segmentation sanity before scoring, read-free: tiles 248/94/402, median tile width 82/62/65 px, tiles
wider than 2.2x median 15/7/3). Detect outputs, configs and overlays committed in **3683f133f BEFORE `recall` ran**;
`detect.sha256` holds their sha256 (room.py rebase folds can lose hashes, TX-RED F7).
Baselines: Spinelli passZ_pipeline, f152r passZ_pipeline, eval_heldout L (`txeng/units/labels_eval_heldout.tsv`) --
the ERRORMAP baselines. `recall` gained `--exclude-flagged` (tx_bench convention, Amendment 2 F2 binds the
flagged-excluded count) and a reader-flag / score-only split; offline test extended.

## Recall tables (`recall.jsonl`; gate declared on Spinelli: recall >= 0.5 at <= 15% flagged)

| item (baseline) | tiled | flagged (share tiled / scored) | errors | caught | recall | of which reader NEW/X_/? flag | score only | chance P(>= caught) at scored share |
|---|---|---|---|---|---|---|---|---|
| **spinelli-c1519-confirm** (Z) | 248 | 37 (0.149 / 0.140) | 14 (2 untiled: deleted h) | **8** | **0.571** | 7 | 1 | 0.0002 |
| same, flagged excluded | | | 14 (no flag column) | 8 | 0.571 | 7 | 1 | |
| birago1572-f152r (Z) | 94 | 14 (0.149 / 0.137) | 5 | 0 | 0.00 | 0 | 0 | 1.0 |
| same, flagged excluded | | | 2 | 0 | 0.00 | 0 | 0 | |
| no.87 eval_heldout (L) | 402 | 60 (0.149 / 0.117) | 15 | 5 | 0.333 | 1 | 4 | 0.024 |
| same, flagged excluded | | | 10 | 4 | 0.40 | 1 | 3 | |
| pooled as measured | 744 | 111 | 34 | 13 | 0.38 | 8 | 5 | |

**Declared gate on Spinelli: MET** (0.571 >= 0.5 at 0.149 <= 0.15). Per X1b this licenses a PREREG for the grown-sheet
READ as the campaign's first eval look, as a separate amendment reviewed by TX-RED first. It does not license anything
else, and the detector does not carry the other two hands (f152r 0/5; eval_heldout 0.33, 0.40 flagged-excluded).

## What carries the pass (diagnostics after scoring; post hoc, no re-tune)

- **Reader flags alone** (the 10 scored positions where pass A wrote NEW:, share 0.052) catch **7 of 14** -- by
  themselves at the gate line. The detector's shape score adds 1 caught error over them (1 of the 5 tiled non-reader
  errors, at a 0.094 non-reader flag share: P(>= 1) = 0.39, chance). TXE-Q's RESULTS already said this: "passA flagged
  both as NEW (5 + 3 positions)". What X1b adds is that the instrument as declared reaches the gate on that leaf.
- **Score alone** (top 15% by off-sheet score, reader flags ignored; post hoc): Spinelli 6/14, f152r 0/5, eval_heldout
  5/15. On Spinelli the off-sheet shapes do score off-sheet (the tall-l-bottom-loop tiles at rank share 0.02, 0.06,
  0.08; median error rank share 0.25 vs 0.49 for all scored), unlike Dinteville in X1 (0.76 / 0.57). So the sheet-gap
  premise holds on Spinelli, where TXE-Q saw it, and only there.
- Spinelli's 6 misses: 2 deleted h (untiled) and 4 consensus tiles (both readers EIGHT, SIX, THREE, PHI: a consensus
  misread becomes an exemplar of the wrong cell, the tool's stated blind spot). One caught SIX sits at score rank 0.95
  and is caught only through its reader flag. f152r: 3 of 5 errors are consensus tiles, median
  error rank share 0.84 (on-sheet look-alikes, the X1 shape). eval_heldout: 9 of 15 consensus tiles; reader flags
  cover 2 scored positions (0.005).

## Sibling-leaf tile census (new material; value-blind, `census_siblings.tsv`, `census_ownleaf.tsv`)

`tools/tx_offsheet.py census` (new subcommand): every glyph-size component on the 22 sibling images on disk
(beinecke_10844888/89/91, 7 pages; bundle17296147, 15 images) counted when it lies within the item's median within-cell
distance (1.25) of a flagged tile, and of a consensus cell. No label, no value is read or shown.

| pages | components | near a flagged tile | near a cell | near a flagged tile, no closer cell |
|---|---|---|---|---|
| 22 sibling images | 6909 | 0.288 | 0.600 | 0.166 |
| control: the item's own leaf (beinecke3811294 p1-p3) | 1534 | 0.241 | 0.600 | 0.132 |

The census does not separate the sibling pages from the cipher leaf: plain-script components match the flagged tiles
at least as often as the leaf's own components do, so its "near" counts are generic pen-stroke similarity, not a
cipher-sign source. That agrees with the folder's own direct looks on file (`ciphers/spinelli-beinecke-c1515/NOTES.md`
H19, H19b, H20b-c, 27-28 Sept 2026): every sibling page on disk is plain Italian, and the digitised bundle ends in 1509,
before the cipher years. **The sibling leaves on disk give 0 cipher tiles for a grown sheet.** A grown-sheet READ would
grow from the confirm leaf's own flagged tiles (and the enciphered ff. 2571-87, not online, are reproduction request
H17).

## Reading

X1b's declared gate is met on Spinelli, so a grown-sheet READ PREREG is licensed (TX-RED review first). The adversarial
point for that review: 7 of the 8 catches are positions the reader already marked NEW. So the pass shows the reader
flags are worth keeping and turning into sheet cells. It does not show that the shape detector finds sheet gaps the
readers miss: its own added catch is 1, at chance. On the two Birago hands the errors are on-sheet look-alikes and
consensus misreads (X1's finding again), and the detector does not carry them. If the READ is run, the result applies
to Spinelli only. The sibling pages cannot give it new exemplars.

## Files and commands

`items/*.json`, `detect_*.tsv`, `detect.sha256`, `debug/*_tiles.png` (3683f133f, before recall); `recall.jsonl`,
`census_*.tsv`, this file. Commands:
`python3 tools/tx_offsheet.py detect benchmark-tx/txeng2/txe2-sheet2/items/<item>.json --out .../detect_<item>.tsv --debug-dir .../debug`;
`python3 tools/tx_offsheet.py recall <cfg> --det <detect> --base <baseline> [--exclude-flagged]`;
`python3 tools/tx_offsheet.py census <spinelli cfg> --det <detect> --pages <images> --out <tsv>`.
Tool: `tools/tx_offsheet.py` (+ `census`, recall `--exclude-flagged`), `tools/tests/test_tx_offsheet.py` ALL PASS;
SYSTEM.md and tool_shelf.tsv rows updated (system_map_check ok). scipy + scikit-learn pip-installed in the container.
