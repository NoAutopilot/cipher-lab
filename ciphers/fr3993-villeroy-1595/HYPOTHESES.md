# fr3993-villeroy-1595 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

Note (A1-VILL-HOMO, 3 Oct 2026): the 11:32 row's judge cell is a crash (spec judge.corpora pointed at a directory, since removed); the same decode run by hand through `tools/judge_plaintext.py specs/fr3993-villeroy-1595.json --file` gives FAIL language -1.35 (null_p99 -1.868, real_p05 -0.873), word cover 0.842. See NOTES.md, A1-VILL-HOMO.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 3 Oct 2026 11:32 | homophonic | N=740 K=53 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz profile=target | 1 | 0.764 (0.358-0.981) | -1919.132 | IsADirectoryError: [Errno 21] Is a directory: 'tools/data/fr16' | yes (gate 0.6) | A1-VILL-HOMO (account 1), K removed as null N3, PREREG-VILL-HOMO |
| 3 Oct 2026 11:43 | homophonic | N=740 K=53 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz profile=target,shuffle_target=1 | 1 | 0.981 (0.981-0.981) | -2000.352 | FAIL language: score=-1.404, null_p99=-1.868, real_p05=-0.873, real_median=-0.789, mode=both, N=740 | yes (gate 0.6) | A1-VILL-HOMO (account 1), shuffled-target floor, PREREG-VILL-HOMO |
