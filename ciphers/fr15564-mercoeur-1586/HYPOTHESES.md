# fr15564-mercoeur-1586 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 3 Oct 2026 15:30 | homophonic | N=220 K=48 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz profile=target,noise=0 | 1-3 | 0.742 (0.409-0.977) | not run (control-only) | - | yes | MERC151B control only, reconciled f.151 read, noise 0 (err_2reader 0.288) |
| 3 Oct 2026 15:31 | homophonic | N=220 K=48 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz profile=target,noise=0.30 | 1-3 | 0.148 (0.109-0.191) | not run (control-only) | - | no | MERC151B control only, reconciled f.151 read, noise 0.30 (err_2reader 0.288) |
| 7 Oct 2026 13:47 | lasry-key cells (partial_key_test --cells) | sheet-matched cells lasry_cells_f151_sheet.tsv, 32 classes, keys=500 within=10 width=400 min-run=4 seed=342 key-seed=3420 | 1 | shuffled target: gain -0.0318 vs p95 0.1877, no signal | gain 0.1474 vs permuted-key p95 0.2348 (77/500 >= real) | - | no (FAIL) | D4-MERC rerun of MERC151B with shared-scale glyph-sheet matching (PREREG-D4MERC.md) |
