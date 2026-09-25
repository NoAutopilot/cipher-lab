# test2 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 25 Sept 2026 19:15 | periodic_vigenere | N=44 K=21 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt tabula=vig,period_max=8 | 1-3 | 0.053 (0.023-0.068) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | - |
| 25 Sept 2026 19:15 | periodic_vigenere | N=44 K=21 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt tabula=beau,period_max=8 | 1-3 | 0.061 (0.023-0.091) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | - |
| 25 Sept 2026 19:15 | periodic_vigenere | N=44 K=21 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt tabula=varbeau,period_max=8 | 1-3 | 0.061 (0.023-0.091) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | - |
| 25 Sept 2026 19:15 | periodic_vigenere | N=44 K=21 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt tabula=vig,period=1 | 1 | 1.000 (1.000-1.000) | -3.973 | FAIL cribs: missing=['GRENADE', 'PIN', 'PINS', 'REINFORCEMENT', 'REINFORCEMENTS', 'PULL', 'THROW', 'ENEMY', 'POSITION', 'ATTACK', 'TANK', 'MG'], count=12 | yes (gate 0.6) | - |
| 25 Sept 2026 19:15 | periodic_vigenere | N=44 K=21 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt tabula=beau,period=1 | 1 | 1.000 (1.000-1.000) | -3.898 | FAIL cribs: missing=['GRENADE', 'PIN', 'PINS', 'REINFORCEMENT', 'REINFORCEMENTS', 'PULL', 'THROW', 'ENEMY', 'POSITION', 'ATTACK', 'TANK', 'MG'], count=12 | yes (gate 0.6) | - |
| 25 Sept 2026 19:15 | periodic_vigenere | N=44 K=21 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt tabula=varbeau,period=1 | 1 | 1.000 (1.000-1.000) | -3.973 | FAIL cribs: missing=['GRENADE', 'PIN', 'PINS', 'REINFORCEMENT', 'REINFORCEMENTS', 'PULL', 'THROW', 'ENEMY', 'POSITION', 'ATTACK', 'TANK', 'MG'], count=12 | yes (gate 0.6) | - |
