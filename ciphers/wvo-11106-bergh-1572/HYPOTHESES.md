# wvo-11106-bergh-1572 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 8 Oct 2026 17:32 | homophonic | N=820 K=41 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz profile=target,noise=0.10 | 1 | 0.616 (0.332-0.856) | -2201.288 | FAIL language: score=-1.332, null_p99=-1.867, real_p05=-0.876, real_median=-0.782, mode=both, N=820 | yes (gate 0.6) | FAM-11106T PREREG gate 1 |
| 8 Oct 2026 17:32 | homophonic | N=820 K=41 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz profile=target,noise=0.10 | 2 | 0.856 (0.856-0.856) | -2216.743 | FAIL language: score=-1.432, null_p99=-1.867, real_p05=-0.876, real_median=-0.782, mode=both, N=820 | yes (gate 0.6) | FAM-11106T exploratory target seed 2 (not PREREG) |
| 8 Oct 2026 17:33 | homophonic | N=820 K=41 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz profile=target,noise=0.10 | 3 | 0.332 (0.332-0.332) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | FAM-11106T exploratory target seed 3 (not PREREG) |
| 8 Oct 2026 17:33 | homophonic | N=820 K=41 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz profile=target,noise=0.10,shuffle_target=1 | 1 | 0.660 (0.660-0.660) | -2333.740 | FAIL language: score=-1.457, null_p99=-1.867, real_p05=-0.876, real_median=-0.782, mode=both, N=820 | yes (gate 0.6) | FAM-11106T exploratory shuffled-target floor (not PREREG) |
