# berthier-napoleon-1812 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 27 Sept 2026 07:27 | homophonic | N=325 K=207 restarts=8 corpus=memoiresdemonsie01torc.txt.gz+memoiresdemonsie02torc.txt.gz+mmoiresduducde01invill.txt.gz+mmoiresduducde02vill.txt.gz+mmoiresetlettre01margoog.txt.gz+lagazettedefran01unkngoog.txt.gz | 1-3 | 0.061 (0.058-0.062) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | BER-HOMO 27 Sept 2026: rule-3 control-then-target homophonic run, N=325 K=207 (spec's own N/K; spec's own ciphertext field is a pointer string, not data -- overridden with structure/flat.txt per BER-KWIC's settled 325-token reading) |
