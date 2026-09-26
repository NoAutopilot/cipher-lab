# blitz-ciphers -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 25 Sept 2026 19:57 | masc | N=581 K=25 restarts=8 corpus=pg1661_holmes.txt | 1-3 | 0.999 (0.998-1.000) | not run (control-only) | - | yes | bBLZ test1 masc control-only (case-folded, N=581 K=25) |
| 25 Sept 2026 19:57 | homophonic | N=581 K=25 restarts=8 corpus=pg1661_holmes.txt | 1-3 | 0.751 (0.260-0.998) | not run (control-only) | - | yes | bBLZ test1 homophonic control-only (case-sensitive, N=581 K=48) |
| 25 Sept 2026 19:58 | homophonic | N=581 K=48 restarts=8 corpus=pg1661_holmes.txt | 1-3 | 0.996 (0.995-0.998) | not run (control-only) | - | yes | bBLZ test1 homophonic control-only (case-sensitive, N=581 K=48) |
| 25 Sept 2026 19:59 | periodic_vigenere | N=581 K=25 restarts=8 corpus=pg1661_holmes.txt | 1-3 | 1.000 (1.000-1.000) | not run (control-only) | - | yes | bBLZ test1 periodic_vigenere control-only (case-folded, N=581 K=25, period auto-scanned) |
| 25 Sept 2026 21:38 | masc | N=581 K=25 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1 | 0.994 (0.985-1.000) | -1846.088 | FAIL language: score=-1.685, null_p99=-2.041, real_p05=-0.858, real_median=-0.806, mode=both, N=581 | yes (gate 0.6) | B4 bBLZ2 |
| 25 Sept 2026 23:24 | homophonic | N=581 K=48 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt profile=target | 1 | 0.971 (0.933-0.995) | -1654.478 | FAIL language: score=-1.518, null_p99=-2.041, real_p05=-0.858, real_median=-0.806, mode=both, N=581 | yes (gate 0.6) | B4 bBLZ3 test3a homophonic case-sensitive K=48 |
| 25 Sept 2026 23:25 | masc | N=581 K=25 restarts=8 corpus=pg15736_Der_Mann_von_vierzig_Jahren.txt.gz+pg36905_Schach_von_Wuthenow.txt.gz+pg41051_Peter_Camenzind.txt.gz+pg41907_Demian.txt.gz+pg43987_Die_drei_Spruenge_des_Wang_lun.txt.gz+pg46184_Frau_Jenny_Treibel.txt.gz+pg5323_Effi_Briest.txt.gz | 1 | 0.956 (0.869-1.000) | -1760.976 | FAIL language: score=-1.768, null_p99=-1.632, real_p05=-0.45, real_median=-0.43, mode=both, N=581 | yes (gate 0.6) | B4 bBLZ3 test3b masc German (control de20, judge de16 default -- era mismatch, rule 3) |
| 26 Sept 2026 01:06 | masc | N=581 K=25 restarts=8 corpus=pg15736_Der_Mann_von_vierzig_Jahren.txt.gz+pg36905_Schach_von_Wuthenow.txt.gz+pg41051_Peter_Camenzind.txt.gz+pg41907_Demian.txt.gz+pg43987_Die_drei_Spruenge_des_Wang_lun.txt.gz+pg46184_Frau_Jenny_Treibel.txt.gz+pg5323_Effi_Briest.txt.gz | 1 | 0.956 (0.869-1.000) | -1760.976 | FAIL language: score=-1.509, null_p99=-2.048, real_p05=-0.82, real_median=-0.782, mode=both, N=581 | yes (gate 0.6) | B5 bBLZ4 de20 judge |
