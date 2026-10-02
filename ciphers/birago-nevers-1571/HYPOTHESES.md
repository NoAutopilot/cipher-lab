# birago-nevers-1571 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 2 Oct 2026 22:27 | homophonic | N=476 K=64 restarts=8 corpus=bub_gb_ZJMxff7r4LUC.txt.gz+bub_gb_laRnTtJmsDAC.txt.gz+gri_33125010469852.txt.gz+letterediprincip01char.txt.gz+letterediprincip02char.txt.gz+letterediprincip03char.txt.gz profile=target | 1 | 0.896 (0.809-0.960) | -1191.336 | FAIL language: score=-1.272, null_p99=-1.77, real_p05=-0.959, real_median=-0.819, mode=both, N=476 | yes (gate 0.6) | BIRAGO-NUM pooled f.119+f.100r, phase.py pairs, clean control |
| 2 Oct 2026 22:28 | homophonic | N=476 K=64 restarts=8 corpus=bub_gb_ZJMxff7r4LUC.txt.gz+bub_gb_laRnTtJmsDAC.txt.gz+gri_33125010469852.txt.gz+letterediprincip01char.txt.gz+letterediprincip02char.txt.gz+letterediprincip03char.txt.gz profile=target,noise=0.25 | 1-3 | 0.249 (0.195-0.311) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | BIRAGO-NUM pooled, control noise 0.25 (phase error at K=64) |
| 2 Oct 2026 22:53 | crib drag (12 pre-registered cribs, PMI context score, 200-permutation null) | pooled f.119+f.100r 473 pairs; synthetic control 476 pairs, 30/40/55 cells, 5% strays, 10 trials | 7, 11, 12 (control); 20261002 (target) | power: 10-letter crib accepted 0-5/10, <=8 letters 0-2/10; wrong placement accepted ~1/10 | 1/12 accepted (maesta p 0.005), void: 17/300 decoy words reach its score at the same hot spot | - | no (no power gate met; weak, anti-conservative accept rule) | BIRAGO-NUM2 num/crib/, not a negative |
| 2 Oct 2026 22:53 | joint phase+key anneal seeded by crib values | - | - | not run | not run | - | - | BIRAGO-NUM2 step 2 skipped: <8 crib-fixed types |
