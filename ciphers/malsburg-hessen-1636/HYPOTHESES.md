# malsburg-hessen-1636 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 26 Sept 2026 05:34 | masc | N=352 K=95 restarts=8 corpus=composed_enhg.txt | 1 | 0.987 (0.980-1.000) | -780.425 | FAIL language: score=-1.472, null_p99=-1.618, real_p05=-0.457, real_median=-0.431, mode=both, N=352 | yes (gate 0.6) | bMAL3 masc vs de16 |
| 26 Sept 2026 05:34 | homophonic | N=352 K=95 restarts=8 corpus=composed_enhg.txt profile=target | 1-3 | 0.392 (0.318-0.511) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | bMAL3 homophonic profile=target vs de16 (nomenclator K=95) |
