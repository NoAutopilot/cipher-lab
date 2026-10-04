# clair1161-avis-flandre-1688 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

**Gloss-match controls (READ2-C1161B, 4 Oct 2026, prereg 252c32a8, glossctl/results.tsv).** Target: key.tsv decodes the c186R block to the period gloss at 0.594. Control (a), same homophonic recipe on token-order-shuffled ciphertext, 20 seeds: max 0.312. Control (b), real decode vs 200 fr16 windows: p95 0.335. PASS. Gloss-seeded repair (glossctl/repair.tsv): c185R judge -1.128 vs shuffled-gloss repairs -1.177/-1.210/-1.243, still FAIL (real_p05 -0.949).

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 3 Oct 2026 23:34 | homophonic | N=924 K=49 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz noise=0.10,profile=target | 1-3 | 0.387 (0.141-0.787) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | READ2-C1161 test 1 (noise 0.10 = c185R err_2reader) |
| 3 Oct 2026 23:36 | homophonic | N=924 K=49 restarts=32 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz noise=0.10,profile=target | 1 | 0.749 (0.594-0.864) | -2281.390 | FAIL language: error=language code 'fr16' has no corpus in LANG_CORPORA; wire it or use 'corpora' | yes (gate 0.6) | READ2-C1161 test 1b (noise 0.10, restarts 32) |
| 3 Oct 2026 23:39 | homophonic | N=924 K=49 restarts=32 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz noise=0.10,profile=target,shuffle_target=1 | 1 | 0.749 (0.594-0.864) | -2539.183 | FAIL language: score=-1.31, null_p99=-1.72, real_p05=-0.924, real_median=-0.816, mode=both, N=924 | yes (gate 0.6) | READ2-C1161 shuffled-target control 1 |
| 3 Oct 2026 23:42 | homophonic | N=924 K=49 restarts=32 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz noise=0.10,profile=target,shuffle_target=2 | 1 | 0.749 (0.594-0.864) | -2546.611 | FAIL language: score=-1.328, null_p99=-1.72, real_p05=-0.924, real_median=-0.816, mode=both, N=924 | yes (gate 0.6) | READ2-C1161 shuffled-target control 2 |
