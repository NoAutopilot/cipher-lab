# siena-concistoro-2308 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 26 Sept 2026 07:00 | homophonic | N=3689 K=73 restarts=8 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt profile=target | 1 | 0.992 (0.988-0.996) | -10287.999 | FAIL language: score=-1.372, null_p99=-1.847, real_p05=-0.925, real_median=-0.822, mode=both, N=3689 | yes (gate 0.6) | bSIE2 nos 6/24 pool, ciphertext-only homophonic, it16 control (era mismatch flagged) |
| 26 Sept 2026 07:02 | homophonic | N=4932 K=86 restarts=8 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt profile=target | 1 | 0.842 (0.555-0.997) | -14090.341 | FAIL language: score=-1.384, null_p99=-1.852, real_p05=-0.954, real_median=-0.814, mode=both, N=4932 | yes (gate 0.6) | bSIE2 nos 20/23 pool, ciphertext-only homophonic, it16 control (era mismatch flagged) |
