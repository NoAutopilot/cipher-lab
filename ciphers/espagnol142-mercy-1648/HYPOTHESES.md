# espagnol142-mercy-1648 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 28 Sept 2026 00:32 | wordcode | N=522 K=38 restarts=4 corpus=donquijote00cervuoft.txt.gz+vidadelbuscn01quevuoft.txt.gz codes=marked,context=ciphers/espagnol142-mercy-1648/families/h5/context.tsv,err=0.047 | 1 | 0.852 (0.808-0.904) | -1231.158 | FAIL language: score=-1.091, null_p99=-1.901, real_p05=-0.894, real_median=-0.82, mode=both, N=524 | yes (gate 0.6) | campaign H5 (account-2 runner): nomenclature-range codes 48/52/65/72/box/frac as code-capable types, merged cross-line runs, clear context words |

## MERCY-M33 (15 Oct 2026; decode_key.py --try in-process, es17c, PREREG-MERCYM33.md)

| hypothesis | n | control at that n (power / false) | target stat | verdict |
|---|---|---|---|---|
| T6: code-6 M glyphs r18:6, r23:2, r24:4, r24:15 = s | 4 | 16/22 / 0/22 (PASS, secondary rule) | +17.0 bits vs NULL, above both p95 | accept (M pending verifier) |
| T2: code-2 M glyphs = o | 4 | 16/22 / 0/22 | +1.4, below null-1 p95 3.1 | undecided |
| K25: code 25 = u (4 occ.) | 4 | 16/22 / 0/22; true rejected 4/22 | -2.4 vs NULL | reject (weak: control rejects true letters 4/22) |
| K14x: open-14 glyphs = c (6 occ., 3 names) | 6 | 18/22 / 0/22 | -29.2 vs NULL | reject (names outside the model) |
| T4, T8, T5, T17, T3: transcription-M groups = current letter | 2-3 | 7-13/22 (FAIL) | +5.5 to +31.6 | non-test at n <= 3 |
| K15: code 15 = z | 2 | 7/22 (FAIL) | -18.1 vs i | non-test at n = 2 |
| K9, FRAC, R1008, R1013, T18 | 1 | n/a | +4.3 to +12.8 | undecided (n = 1) |
