# fr15564-mercoeur-1586 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 3 Oct 2026 15:30 | homophonic | N=220 K=48 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz profile=target,noise=0 | 1-3 | 0.742 (0.409-0.977) | not run (control-only) | - | yes | MERC151B control only, reconciled f.151 read, noise 0 (err_2reader 0.288) |
| 3 Oct 2026 15:31 | homophonic | N=220 K=48 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz profile=target,noise=0.30 | 1-3 | 0.148 (0.109-0.191) | not run (control-only) | - | no | MERC151B control only, reconciled f.151 read, noise 0.30 (err_2reader 0.288) |
