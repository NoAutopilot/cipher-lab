# rubin-1953 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 25 Sept 2026 19:14 | masc | N=39 K=39 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1-3 | 0.521 (0.103-0.897) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | bRUB2 test2: masc N=305 letters_AD |
| 25 Sept 2026 19:15 | masc | N=305 K=26 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1 | 0.989 (0.974-0.997) | -844.061 | FAIL language: score=-1.475, null_p99=-1.98, real_p05=-0.882, real_median=-0.809, mode=both, N=305 | yes (gate 0.6) | bRUB2 test2: masc N=305 letters_AD |
| 25 Sept 2026 19:15 | masc | N=293 K=26 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1 | 0.974 (0.928-0.997) | -815.390 | FAIL language: score=-1.618, null_p99=-2.0, real_p05=-0.879, real_median=-0.815, mode=both, N=293 | yes (gate 0.6) | bRUB2 test2: masc N=293 letters_AD minus DULLES/CONANT |
