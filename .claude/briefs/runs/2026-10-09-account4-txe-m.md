# TXE-M: feature-first reading protocol (LANE TX-ENGINEER, idea M24; account 4, Opus 5.5; cap 7, box 90 min)

Read `.claude/briefs/runs/2026-10-09-account4-txe-COMMON.md` first, then `benchmark-tx/PREREG-txeng-2.md` (units, blindness,
Amendment: gate p < 0.01) and research/TX-IDEAS-2026-10-09.md (row M24 and the Results log: eleven instruments so far; the
only one that moved is crop geometry, on pixels the reader never saw; every change to WHAT the reader sees beside the glyph
-- exemplars, hints, upscaling -- failed; the reader's errors sit in the glyph). Why this job exists: nothing yet has changed
HOW the reader decides. Today it names a cell; a palaeographer first names the features (descender below the line? one bar
or two? loop open or closed? dot present?) and only then the letter. This job makes the reader write the deciding features
of each sign before the cell, on the ordinary line crops, with nothing added to the image.

## Pre-registration (write `benchmark-tx/txeng/feature/PREREG.md` and push it BEFORE any read)
- Crops and sheet: the unchanged dev_tune line crops (harvest/f178v/f178v_L01..L12_s?.jpg) and `sign_sheet_blind_1572.png`;
  the unchanged `harvest/blind_pass_brief_1572.md` with ONE added output rule: the TSV gains a `features` column written
  BEFORE sign_id for every sign, in a fixed vocabulary derived by `tools/tx_pair_hints.py` style from the sheet cells
  themselves (not from the hand, not from truth): descender (none/short/long), ascender (none/short/long), bars (0/1/2),
  loops (0/1/2), dots (0/1/2+), lean (left/upright/right), tail (none/left/right). The reader is told to fill the features
  from the ink first, then pick the cell whose sheet-cell features match. A table of the sheet cells' features (derived
  by script from the printed sheet, committed as `benchmark-tx/txeng/feature/cell_features.tsv`) is appended to the brief.
- Reader: one blind Opus 5.5 pass on dev_tune in two calls (L01-06, L07-12), as pass A's grouping. Raw reads committed
  before scoring; normalise as build_birago87.py does -> `benchmark-tx/outputs/birago1572-no87/passU_feature_dev_tune.tsv`.
- Gate (fixed now): `tools/tx_bench.py passU_feature_dev_tune.tsv --bench BENCHMARK-TX.tsv --item birago1572-no87 --paired
  benchmark-tx/txeng/units/passA_dev_tune.tsv`: fixed > broken, p < 0.01; vs labels_dev_tune.tsv reported. Met ->
  eval_heldout once (two calls), paired vs passA_eval_heldout.tsv and labels_eval_heldout.tsv (the eval look). Not met ->
  FAIL, no eval. Secondary, read-free after commit: do the written features predict the errors? (share of wrong signs whose
  written features contradict the chosen cell's features -- a self-consistency flag for the sorter.)

## Report
`benchmark-tx/txeng/feature/RESULTS.md`: the gate lines, the feature-vocabulary table, the self-consistency table,
`tools/tx_taxonomy.py` on passU vs A and L (after commit), reader task text, calls. Tool: the cell-feature derivation and
the self-consistency check as `tools/tx_features.py` with --help and an offline test; shelf and SYSTEM rows (grade from the
result); Results-log row in research/TX-IDEAS-2026-10-09.md (id M24; rebase before editing). Vision calls: dev 2, eval 2 at
most; cap 7; stop before a call that crosses 80% of cap or box. Report in a short paragraph (first line: dev and eval
fixed/broken/p vs A) and stop.
