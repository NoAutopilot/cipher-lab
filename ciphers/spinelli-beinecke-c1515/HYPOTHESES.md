# spinelli-beinecke-c1515 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 28 Sept 2026 00:47 | masc | N=262 K=25 restarts=8 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt | 1-3 | 0.959 (0.927-0.989) | not run (control-only) | - | yes | H16 prerequisite: plain-substitution control at N=262 K=25, it16 |
| 28 Sept 2026 00:48 | masc | N=262 K=25 restarts=8 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt | 1 | 0.959 (0.927-0.989) | -701.887 | FAIL language: score=-1.259, null_p99=-1.753, real_p05=-0.964, real_median=-0.813, mode=both, N=262 | yes (gate 0.6) | H16 masc on the 262-code letter: DESIGN-MISMATCHED (HOOK = one symbol for several letters, ~17% nulls), a non-test for the letter, run to put its number beside the control |
