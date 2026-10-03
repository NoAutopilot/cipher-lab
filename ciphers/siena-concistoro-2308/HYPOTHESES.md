# siena-concistoro-2308 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

## READ2-SIENA, 3 Oct 2026: known-key transfer, Bourdeau keys 25/14/4 onto the pooled systems (prose row)

Script `specs/cheap-tests/siena-concistoro-2308/run_test_pools.py`. The statistic is the it 4-gram per-letter score in order. The CONTROL
numbers are the value-shuffled mean over 200 keys and the order-shuffled mean over 20 seeds, written beside the TARGET (the real key).
Positive-control power is given at the covered count.

| pool | key | TARGET | CONTROL value-shuffled mean (max), n>=target | CONTROL order-shuffled mean (max) | power | verdict |
|---|---|---|---|---|---|---|
| 6+24 | no25 | -2.240 | -2.162 (-1.742), 151/200 | -2.220 (-2.138) | 0.60 | negative |
| 6+24 | no14 | -2.106 | -1.962 (-1.580), 171/200 | -2.072 (-2.013) | 1.00 | negative |
| 6+24 | no04 | -1.945 | -2.115 (-1.878), 11/200 | -1.973 (-1.922) | 1.00 | negative (judge FAIL) |
| 20+23 | no25 | -2.132 | -2.170 (-1.763), 58/200 | -2.112 (-2.058) | 1.00 | negative |
| 20+23 | no14 | -2.073 | -1.957 (-1.591), 157/200 | -2.129 (-2.096) | 1.00 | negative |
| 20+23 | no04 | -2.098 | -2.130 (-1.728), 67/200 | -2.113 (-2.087) | 0.75 | negative |

The sign matching is by name across transcribers, so a shape-level concordance is not excluded (see NOTES.md READ2-SIENA).

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 26 Sept 2026 07:00 | homophonic | N=3689 K=73 restarts=8 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt profile=target | 1 | 0.992 (0.988-0.996) | -10287.999 | FAIL language: score=-1.372, null_p99=-1.847, real_p05=-0.925, real_median=-0.822, mode=both, N=3689 | yes (gate 0.6) | bSIE2 nos 6/24 pool, ciphertext-only homophonic, it16 control (era mismatch flagged) |
| 26 Sept 2026 07:02 | homophonic | N=4932 K=86 restarts=8 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt profile=target | 1 | 0.842 (0.555-0.997) | -14090.341 | FAIL language: score=-1.384, null_p99=-1.852, real_p05=-0.954, real_median=-0.814, mode=both, N=4932 | yes (gate 0.6) | bSIE2 nos 20/23 pool, ciphertext-only homophonic, it16 control (era mismatch flagged) |
