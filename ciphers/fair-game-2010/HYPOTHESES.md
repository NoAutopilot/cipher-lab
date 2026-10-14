# fair-game-2010 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

R12D-FAIR (6 Oct 2026): the first `masc_words` row (label "R12D-FAIR word-constrained order=scroll", control 0.567) is
void as a test of the word term -- the control's training text reached the family space-free, so the lexicon was empty
and the run was masc plus an n-gram polish. Fixed in tools/families/masc_words.py (make_control keeps word boundaries;
tools/tests/test_masc_words_family.py); the "lexicon-fix" rows are the pre-registered test (r12d/PREREG-R12D-FAIR.md).

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 3 Oct 2026 09:38 | masc | N=67 K=21 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1-5 | 0.537 (0.179-0.791) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | GAPS71 test2 order=scroll |
| 3 Oct 2026 09:38 | masc | N=67 K=21 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1-5 | 0.537 (0.179-0.791) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | GAPS71 test2 order=column |
| 3 Oct 2026 09:39 | masc | N=67 K=21 restarts=32 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1-5 | 0.591 (0.179-0.791) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | GAPS71 test2 r32 order=scroll |
| 3 Oct 2026 09:40 | masc | N=67 K=21 restarts=32 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1-5 | 0.591 (0.179-0.791) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | GAPS71 test2 r32 order=column |
| 3 Oct 2026 09:41 | masc | N=67 K=21 restarts=32 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1 | 0.591 (0.179-0.791) | -150.915 | FAIL language: score=-0.985, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.5) | GAPS71 test2 r32 gate0.5 order=scroll |
| 3 Oct 2026 09:42 | masc | N=67 K=21 restarts=32 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=7 | 1 | 0.591 (0.179-0.791) | -151.632 | FAIL language: score=-1.336, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.5) | GAPS71 test2 shuffle7 order=scroll |
| 3 Oct 2026 09:43 | masc | N=67 K=21 restarts=32 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1 | 0.591 (0.179-0.791) | -151.553 | FAIL language: score=-1.29, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.5) | GAPS71 test2 r32 gate0.5 order=column |
| 3 Oct 2026 09:44 | masc | N=67 K=21 restarts=32 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=7 | 1 | 0.591 (0.179-0.791) | -153.721 | FAIL language: score=-1.113, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.5) | GAPS71 test2 shuffle7 order=column |
| 3 Oct 2026 09:45 | masc | N=67 K=21 restarts=32 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=8 | 1 | 0.591 (0.179-0.791) | -149.454 | FAIL language: score=-1.152, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.5) | GAPS71 shuf8 scroll |
| 3 Oct 2026 09:46 | masc | N=67 K=21 restarts=32 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=8 | 1 | 0.591 (0.179-0.791) | -145.249 | FAIL language: score=-1.174, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.5) | GAPS71 shuf8 column |
| 3 Oct 2026 09:47 | masc | N=67 K=21 restarts=32 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=9 | 1 | 0.591 (0.179-0.791) | -148.088 | FAIL language: score=-1.378, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.5) | GAPS71 shuf9 scroll |
| 3 Oct 2026 09:49 | masc | N=67 K=21 restarts=32 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=9 | 1 | 0.591 (0.179-0.791) | -151.441 | FAIL language: score=-1.267, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.5) | GAPS71 shuf9 column |
| 3 Oct 2026 09:50 | masc | N=67 K=21 restarts=32 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=10 | 1 | 0.591 (0.179-0.791) | -147.001 | FAIL language: score=-1.118, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.5) | GAPS71 shuf10 scroll |
| 3 Oct 2026 09:51 | masc | N=67 K=21 restarts=32 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=10 | 1 | 0.591 (0.179-0.791) | -144.952 | FAIL language: score=-1.137, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.5) | GAPS71 shuf10 column |
| 3 Oct 2026 09:52 | masc | N=67 K=21 restarts=32 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1 | 0.591 (0.179-0.791) | -150.915 | FAIL language: score=-0.985, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.5) | GAPS71 SCROLL final |
| 6 Oct 2026 15:50 | masc_words | N=67 K=21 restarts=16 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1-5 | 0.567 (0.179-0.791) | not run (CONTROL BELOW GATE) | - | no (gate 0.7) | R12D-FAIR word-constrained order=scroll |
| 6 Oct 2026 15:54 | masc_words | N=67 K=21 restarts=16 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1 | 0.707 (0.075-0.955) | -346.837 | FAIL language: score=-0.984, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.7) | R12D-FAIR word-constrained lexicon-fix order=scroll |
| 6 Oct 2026 15:58 | masc_words | N=67 K=21 restarts=16 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=8 | 1 | 0.707 (0.075-0.955) | -343.192 | FAIL language: score=-1.086, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.7) | R12D-FAIR lexfix shuf8 scroll |
| 6 Oct 2026 15:58 | masc_words | N=67 K=21 restarts=16 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1 | 0.707 (0.075-0.955) | -394.154 | FAIL language: score=-1.37, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.7) | R12D-FAIR word-constrained lexicon-fix order=column |
| 6 Oct 2026 15:58 | masc_words | N=67 K=21 restarts=16 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=7 | 1 | 0.707 (0.075-0.955) | -372.873 | FAIL language: score=-1.283, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.7) | R12D-FAIR lexfix shuf7 scroll |
| 6 Oct 2026 16:00 | masc_words | N=67 K=21 restarts=16 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=10 | 1 | 0.707 (0.075-0.955) | -349.767 | FAIL language: score=-1.178, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.7) | R12D-FAIR lexfix shuf10 scroll |
| 6 Oct 2026 16:00 | masc_words | N=67 K=21 restarts=16 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=11 | 1 | 0.707 (0.075-0.955) | -335.957 | FAIL language: score=-0.98, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.7) | R12D-FAIR lexfix shuf11 scroll |
| 6 Oct 2026 16:00 | masc_words | N=67 K=21 restarts=16 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=9 | 1 | 0.707 (0.075-0.955) | -359.474 | FAIL language: score=-1.203, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.7) | R12D-FAIR lexfix shuf9 scroll |
| 6 Oct 2026 16:38 | masc_inj | N=67 K=21 restarts=1 corpus=pg1661_holmes.txt+pg2701_mobydick.txt beam=1000 | 1-5 | 0.576 (0.060-1.000) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | R12D-FAIR2 injective order=scroll |
| 6 Oct 2026 16:38 | masc_inj | N=67 K=21 restarts=1 corpus=pg1661_holmes.txt+pg2701_mobydick.txt beam=1000,shuffle_target=8 | 1-5 | 0.576 (0.060-1.000) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | R12D-FAIR2 shuf8 scroll |
| 6 Oct 2026 16:38 | masc_inj | N=67 K=21 restarts=1 corpus=pg1661_holmes.txt+pg2701_mobydick.txt beam=1000,shuffle_target=7 | 1-5 | 0.576 (0.060-1.000) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | R12D-FAIR2 shuf7 scroll |
| 6 Oct 2026 16:38 | masc_inj | N=67 K=21 restarts=1 corpus=pg1661_holmes.txt+pg2701_mobydick.txt beam=1000 | 1-5 | 0.576 (0.060-1.000) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | R12D-FAIR2 injective order=column |
| 8 Oct 2026 08:01 | marker_sweep (S0-S12, 118 candidates) | N=67 planted Pride-and-Prejudice windows, en judge minus length check | 5 trials x 12 plantable schemes | 60/60 recovered (5/5 each scheme; top-ranked 58/60); null family-wise false-pass 0/40 | best S0+S12 interleave -1.721 | FAIL (0 of 118 pass; CLI: language -1.721 vs real_p05 -0.92, cover 0.478) | yes (G1 0.8, G2 <=0.10) | D2-FAIR order=scroll, marker/PREREG-D2-FAIR.md |
| 8 Oct 2026 08:01 | marker_sweep (S0-S12, 118 candidates) | same | same control | 60/60; null 0/40 | best S0+S11 decim10 -1.835 | FAIL (0 of 118 pass; CLI: -1.835, cover 0.433) | yes | D2-FAIR order=column |
| 14 Oct 2026 19:23 | transposition | N=68 K=22 restarts=4 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1 | 0.889 (0.000-0.985) | -189.775 | FAIL language: score=-1.589, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-TRANS scroll68 (account 1) |
| 14 Oct 2026 19:24 | transposition | N=67 K=21 restarts=4 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1 | 0.942 (0.000-1.000) | -197.232 | FAIL language: score=-1.502, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-TRANS column67 (account 1) |
| 14 Oct 2026 19:24 | transposition | N=67 K=21 restarts=4 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1 | 0.942 (0.000-1.000) | -197.817 | FAIL language: score=-1.592, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-TRANS scroll67 (account 1) |
| 14 Oct 2026 19:24 | transposition | N=68 K=22 restarts=4 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1 | 0.889 (0.000-0.985) | -190.354 | FAIL language: score=-1.541, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-TRANS column68 (account 1) |
| 14 Oct 2026 19:24 | transposition | N=68 K=22 restarts=4 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=7 | 1 | 0.985 (0.985-0.985) | -196.321 | FAIL language: score=-1.781, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-TRANS shuffle floor scroll68 (account 1) |
| 14 Oct 2026 19:24 | transposition | N=68 K=22 restarts=4 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=8 | 1 | 0.985 (0.985-0.985) | -194.747 | FAIL language: score=-1.665, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-TRANS shuffle floor scroll68 (account 1) |
| 14 Oct 2026 19:24 | transposition | N=68 K=22 restarts=4 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=9 | 1 | 0.985 (0.985-0.985) | -190.498 | FAIL language: score=-1.592, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-TRANS shuffle floor scroll68 (account 1) |
| 14 Oct 2026 19:24 | transposition | N=68 K=22 restarts=4 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=10 | 1 | 0.985 (0.985-0.985) | -189.713 | FAIL language: score=-1.618, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-TRANS shuffle floor scroll68 (account 1) |
| 14 Oct 2026 19:25 | transposition | N=68 K=22 restarts=4 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=11 | 1 | 0.985 (0.985-0.985) | -195.656 | FAIL language: score=-1.632, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-TRANS shuffle floor scroll68 (account 1) |
| 14 Oct 2026 19:25 | transposition | N=68 K=22 restarts=4 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=12 | 1 | 0.985 (0.985-0.985) | -200.896 | FAIL language: score=-1.729, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-TRANS shuffle floor scroll68 (account 1) |
| 14 Oct 2026 19:25 | transposition | N=68 K=22 restarts=4 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=13 | 1 | 0.985 (0.985-0.985) | -197.387 | FAIL language: score=-1.662, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-TRANS shuffle floor scroll68 (account 1) |
| 14 Oct 2026 19:25 | transposition | N=68 K=22 restarts=4 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=14 | 1 | 0.985 (0.985-0.985) | -194.451 | FAIL language: score=-1.678, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-TRANS shuffle floor scroll68 (account 1) |
| 14 Oct 2026 19:25 | transposition | N=68 K=22 restarts=4 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=15 | 1 | 0.985 (0.985-0.985) | -198.239 | FAIL language: score=-1.559, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-TRANS shuffle floor scroll68 (account 1) |
| 14 Oct 2026 19:26 | transposition | N=68 K=22 restarts=4 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=16 | 1 | 0.985 (0.985-0.985) | -185.581 | FAIL language: score=-1.496, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-TRANS shuffle floor scroll68 (account 1) |
| 14 Oct 2026 19:26 | transposition | N=68 K=22 restarts=12 corpus=pg1661_holmes.txt+pg2701_mobydick.txt widths=9-12,iters=15000,ctrl_designs=colK:9;colK:10;colK:11;colK:12 | 1 | 0.868 (0.515-0.985) | -185.549 | FAIL language: score=-1.531, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-TRANS wide-width search scroll68 (account 1) |
| 14 Oct 2026 19:26 | transposition | N=68 K=22 restarts=12 corpus=pg1661_holmes.txt+pg2701_mobydick.txt widths=9-12,iters=15000,ctrl_designs=colK:9;colK:10;colK:11;colK:12 | 1 | 0.868 (0.515-0.985) | -190.779 | FAIL language: score=-1.532, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-TRANS wide-width search column68 (account 1) |
| 14 Oct 2026 19:28 | transposition | N=68 K=22 restarts=12 corpus=pg1661_holmes.txt+pg2701_mobydick.txt widths=9-12,iters=15000,ctrl_designs=colK:9;colK:10;colK:11;colK:12,shuffle_target=8 | 1 | 0.985 (0.985-0.985) | -191.357 | FAIL language: score=-1.594, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-TRANS shuffle floor wide-width scroll68 (account 1) |
| 14 Oct 2026 19:28 | transposition | N=68 K=22 restarts=12 corpus=pg1661_holmes.txt+pg2701_mobydick.txt widths=9-12,iters=15000,ctrl_designs=colK:9;colK:10;colK:11;colK:12,shuffle_target=10 | 1 | 0.985 (0.985-0.985) | -192.829 | FAIL language: score=-1.566, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-TRANS shuffle floor wide-width scroll68 (account 1) |
| 14 Oct 2026 19:28 | transposition | N=68 K=22 restarts=12 corpus=pg1661_holmes.txt+pg2701_mobydick.txt widths=9-12,iters=15000,ctrl_designs=colK:9;colK:10;colK:11;colK:12,shuffle_target=7 | 1 | 0.985 (0.985-0.985) | -188.844 | FAIL language: score=-1.59, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-TRANS shuffle floor wide-width scroll68 (account 1) |
| 14 Oct 2026 19:28 | transposition | N=68 K=22 restarts=12 corpus=pg1661_holmes.txt+pg2701_mobydick.txt widths=9-12,iters=15000,ctrl_designs=colK:9;colK:10;colK:11;colK:12,shuffle_target=9 | 1 | 0.985 (0.985-0.985) | -188.405 | FAIL language: score=-1.525, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-TRANS shuffle floor wide-width scroll68 (account 1) |
| 14 Oct 2026 22:10 | transposition | N=68 K=22 restarts=4 corpus=worksofjohnkn01knox.txt.gz+worksofjohnkn02knox.txt.gz+adiurnalremarka00thomgoog.txt.gz+historielifeofki00colvuoft.txt.gz+registerofprivyc0002jjoh.txt.gz | 1 | 0.884 (0.000-0.985) | -199.847 | FAIL language: score=-1.808, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-LANG supplementary scroll68 (account 4) |
| 14 Oct 2026 22:12 | transposition | N=68 K=22 restarts=4 corpus=lettresdecatheri01cathuoft_djvu.txt.gz | 1 | 0.954 (0.632-0.985) | -195.010 | FAIL language: score=-1.809, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-LANG supplementary scroll68 (account 4) |
| 14 Oct 2026 22:13 | transposition | N=68 K=22 restarts=4 corpus=marn001bien01.txt.gz+marn001trou01.txt.gz+coor001zede01.txt.gz+spie001twes01.txt.gz+coor001boev01.txt.gz | 1 | 0.958 (0.618-0.985) | -198.233 | FAIL language: score=-2.114, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-LANG supplementary scroll68 (account 4) |
| 14 Oct 2026 22:14 | transposition | N=68 K=22 restarts=4 corpus=worksofjohnkn01knox.txt.gz+worksofjohnkn02knox.txt.gz+adiurnalremarka00thomgoog.txt.gz+historielifeofki00colvuoft.txt.gz+registerofprivyc0002jjoh.txt.gz | 1 | 0.884 (0.000-0.985) | -199.705 | FAIL language: score=-1.771, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-LANG supplementary column68 (account 4) |
| 14 Oct 2026 22:16 | transposition | N=68 K=22 restarts=4 corpus=lettresdecatheri01cathuoft_djvu.txt.gz | 1 | 0.954 (0.632-0.985) | -199.826 | FAIL language: score=-2.064, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-LANG supplementary column68 (account 4) |
| 14 Oct 2026 22:17 | transposition | N=68 K=22 restarts=4 corpus=marn001bien01.txt.gz+marn001trou01.txt.gz+coor001zede01.txt.gz+spie001twes01.txt.gz+coor001boev01.txt.gz | 1 | 0.958 (0.618-0.985) | -190.808 | FAIL language: score=-1.91, null_p99=-1.837, real_p05=-0.92, real_median=-0.802, mode=both, N=67 | yes (gate 0.8) | FAIR-LANG supplementary column68 (account 4) |

### FAIR-LANG (account 4, LANE DEFAULT-A4-2135-14, 14 Oct 2026, 22:07-22:1x UTC): per-language letter-count rank (L0) and transposition --langs (L1)

L0: target letter-count log-likelihood per letter vs 2000 word-start N=67 windows of the language's own corpus (the control), and 200 uniform-random strings for scale. `lang/lang_rank.py --check`, `lang/lang_rank.json`. Pre-registered gate (lang/PREREG-FAIR-LANG.md, 6c4ac8376): pct_rank < 0.01 excludes a pure transposition of that language.

| lang | target ll/letter | rank among own windows | own p01 | own median | uniform-random median | L0 verdict |
|---|---|---|---|---|---|---|
| sco16 | -3.1474 | 0.0045 | -3.1045 | -2.8876 | -3.8774 | below p01: excluded |
| fr | -3.4834 | 0.0025 | -3.0801 | -2.8164 | -3.9963 | below p01: excluded |
| nl16 | -3.2729 | 0.002 | -3.1278 | -2.8306 | -3.7877 | below p01: excluded |
| fr1810 | -3.3889 | 0.002 | -3.0944 | -2.7822 | -3.9645 | below p01: excluded |
| nl18 | -3.2937 | 0.0015 | -3.1262 | -2.8122 | -3.8342 | below p01: excluded |
| pl18 | -3.301 | 0.0015 | -3.1645 | -2.962 | -3.8815 | below p01: excluded |
| en | -3.1626 | 0.001 | -3.0843 | -2.8935 | -3.8869 | below p01: excluded |
| en18 | -3.171 | 0.001 | -3.0658 | -2.8706 | -3.8699 | below p01: excluded |
| fr16 | -3.4496 | 0.0005 | -3.0734 | -2.8098 | -3.9581 | below p01: excluded |
| da19 | -3.4599 | 0.0005 | -3.1045 | -2.7893 | -4.1592 | below p01: excluded |
| es17c7 | -3.4729 | 0.0005 | -3.033 | -2.7953 | -4.1039 | below p01: excluded |
| de1600 | -3.2884 | 0.0005 | -3.107 | -2.8313 | -4.0167 | below p01: excluded |
| de | -3.336 | 0.0 | -3.0588 | -2.8491 | -4.0674 | below p01: excluded |
| it | -3.4805 | 0.0 | -3.0447 | -2.7858 | -4.1423 | below p01: excluded |
| it16dip | -3.4319 | 0.0 | -3.006 | -2.7942 | -4.1545 | below p01: excluded |
| it15 | -3.5074 | 0.0 | -3.0113 | -2.7814 | -4.18 | below p01: excluded |
| it19 | -3.5708 | 0.0 | -2.9351 | -2.77 | -4.3247 | below p01: excluded |
| it21news | -3.4485 | 0.0 | -3.0093 | -2.7601 | -4.1905 | below p01: excluded |
| pt | -3.3246 | 0.0 | -3.102 | -2.7698 | -4.0286 | below p01: excluded |
| pt18 | -3.3072 | 0.0 | -3.1024 | -2.7888 | -3.9789 | below p01: excluded |
| fr18 | -3.3468 | 0.0 | -3.0794 | -2.8136 | -3.9426 | below p01: excluded |
| fr1840 | -3.4182 | 0.0 | -3.022 | -2.7618 | -4.0507 | below p01: excluded |
| fr17 | -3.5084 | 0.0 | -3.0156 | -2.7994 | -4.0417 | below p01: excluded |
| es | -3.5161 | 0.0 | -2.9971 | -2.8 | -4.1117 | below p01: excluded |
| es17c | -3.4792 | 0.0 | -3.025 | -2.793 | -4.1086 | below p01: excluded |
| es18 | -3.4172 | 0.0 | -3.0223 | -2.8096 | -4.0121 | below p01: excluded |
| es18p | -3.3827 | 0.0 | -3.0359 | -2.8237 | -3.9697 | below p01: excluded |
| es17a | -3.4162 | 0.0 | -3.0297 | -2.8103 | -4.0408 | below p01: excluded |
| es1600 | -3.5305 | 0.0 | -2.956 | -2.7919 | -4.1901 | below p01: excluded |
| la | -3.3802 | 0.0 | -3.1198 | -2.8541 | -3.9731 | below p01: excluded |
| la18 | -3.3802 | 0.0 | -3.1198 | -2.8541 | -3.9731 | below p01: excluded |
| la17 | -3.3554 | 0.0 | -3.0905 | -2.8595 | -3.9725 | below p01: excluded |
| de17 | -3.272 | 0.0 | -3.0903 | -2.8386 | -3.9853 | below p01: excluded |
| sv17 | -3.2887 | 0.0 | -3.0669 | -2.8858 | -3.9138 | below p01: excluded |

L1 (declared supplementary, outside the registered gate: none of the 34 qualified, so the three highest L0 ranks were run anyway for scale): `family_run.py --family transposition --langs sco16,fr,nl16`, seeds 28, restarts 4, gate 0.80; control in that language's corpus; target judged in its own language (margin = score - real_p05). The en-judge column of the six rows above is the spec's English judge; the own-language numbers are here.

| lang | control mean (gate 0.80) | scroll68 own-language score / real_p05 / margin | column68 own-language score / real_p05 / margin | verdict |
|---|---|---|---|---|
| sco16 | 0.884 | -1.656 / -0.951 / -0.705 | -1.800 / -0.951 / -0.849 | FAIL both orders (control gated) |
| fr | 0.954 | -1.724 / -0.978 / -0.746 | -1.680 / -0.978 / -0.702 | FAIL both orders (control gated) |
| nl16 | 0.958 | -1.712 / -0.875 / -0.837 | -1.626 / -0.875 / -0.751 | FAIL both orders (control gated) |

