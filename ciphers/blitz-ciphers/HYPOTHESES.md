# blitz-ciphers -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 25 Sept 2026 19:57 | masc | N=581 K=25 restarts=8 corpus=pg1661_holmes.txt | 1-3 | 0.999 (0.998-1.000) | not run (control-only) | - | yes | bBLZ test1 masc control-only (case-folded, N=581 K=25) |
| 25 Sept 2026 19:57 | homophonic | N=581 K=25 restarts=8 corpus=pg1661_holmes.txt | 1-3 | 0.751 (0.260-0.998) | not run (control-only) | - | yes | bBLZ test1 homophonic control-only (case-sensitive, N=581 K=48) |
| 25 Sept 2026 19:58 | homophonic | N=581 K=48 restarts=8 corpus=pg1661_holmes.txt | 1-3 | 0.996 (0.995-0.998) | not run (control-only) | - | yes | bBLZ test1 homophonic control-only (case-sensitive, N=581 K=48) |
| 25 Sept 2026 19:59 | periodic_vigenere | N=581 K=25 restarts=8 corpus=pg1661_holmes.txt | 1-3 | 1.000 (1.000-1.000) | not run (control-only) | - | yes | bBLZ test1 periodic_vigenere control-only (case-folded, N=581 K=25, period auto-scanned) |
