# cipher-lab -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 27 Sept 2026 14:51 | homophonic | N=522 K=38 restarts=2 corpus=donquijote00cervuoft.txt.gz+vidadelbuscn01quevuoft.txt.gz | 1-3 | 0.965 (0.948-0.973) | not run (control-only) | - | yes | BENCH-FREEZE U2 design-class control (homophonic, N=522 K=38) |
| 27 Sept 2026 14:52 | masc | N=364 K=20 restarts=2 corpus=composed_enhg.txt | 1-3 | 0.435 (0.077-0.975) | not run (control-only) | - | no | BENCH-FREEZE U2 design-class control (masc/alphabet-substitution, N=364 K=20) |
