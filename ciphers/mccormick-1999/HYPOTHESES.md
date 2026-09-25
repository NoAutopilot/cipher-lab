# mccormick-1999 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 25 Sept 2026 18:41 | masc | N=746 K=24 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1 | 0.994 (0.989-0.999) | -2190.651 | PASS - mccormick-1999 (a PASS is a gate for a verifier, not a reading; rule 10) | yes (gate 0.6) | LANE B2 bMCC2 test2: masc vs default English corpus |
| 25 Sept 2026 18:42 | masc | N=746 K=24 restarts=8 corpus=pg1661_holmes_vdrop.txt+pg2701_mobydick_vdrop.txt | 1 | 0.985 (0.983-0.989) | -1958.813 | PASS - mccormick-1999 (a PASS is a gate for a verifier, not a reading; rule 10) | yes (gate 0.6) | LANE B2 bMCC2 test2: masc vs vowel-dropped English corpus |
