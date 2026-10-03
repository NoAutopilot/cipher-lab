# la-garde-1577 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 26 Sept 2026 19:27 | syllabary | N=239 K=48 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz err=0.23 | 1-3 | 0.385 (0.159-0.603) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | WC-LAGARDE2 stuck-rule try |
| 26 Sept 2026 19:29 | wordcode | N=239 K=48 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz codes=marked,err=0.23 | 1-3 | 0.321 (0.096-0.586) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | WC-LAGARDE2 stuck-rule try |
| 3 Oct 2026 00:04 | masc | N=229 K=26 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz | 1 | 0.969 (0.948-0.983) | -572.867 | FAIL language: score=-1.208, null_p99=-1.601, real_p05=-0.96, real_median=-0.806, mode=both, N=229 | yes (gate 0.6) | A2-LAG3 masc on base codes (marks stripped, MARK dropped), clean control |
| 3 Oct 2026 00:06 | masc | N=229 K=26 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz noise=0.23 | 1-3 | 0.367 (0.031-0.563) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | A2-LAG3 masc base codes, control noise=0.23 |
| 3 Oct 2026 00:06 | masc | N=229 K=26 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz noise=0.20 | 1-3 | 0.565 (0.332-0.777) | not run (control-only) | - | no | A2-LAG3 masc base codes, control noise=0.20 |
| 3 Oct 2026 00:07 | masc | N=229 K=26 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz noise=0.26 | 1-3 | 0.338 (0.297-0.406) | not run (control-only) | - | no | A2-LAG3 masc base codes, control noise=0.26 |
| 3 Oct 2026 14:55 | IC design check (masc / running_key / homophonic K=26) | N=229 K=26 base codes, fr16 x3, noise 0.23 profile+uniform | 300 windows (homophonic 40 seeds) | masc IC 0.0779 (worst-case noise p05 0.0565, min 0.0507); running_key 0.0409; homophonic 0.0464 | target IC 0.0420 | below all 300 masc controls; running_key pct 0.45-0.90; homophonic pct 0.075 | n/a (statistic, not a solver) | GAPS145: masc on base codes excluded by IC; families/ic_design_check.py |
