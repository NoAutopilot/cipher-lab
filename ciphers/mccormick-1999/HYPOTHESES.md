# mccormick-1999 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 25 Sept 2026 18:41 | masc | N=746 K=24 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1 | 0.994 (0.989-0.999) | -2190.651 | PASS - mccormick-1999 (a PASS is a gate for a verifier, not a reading; rule 10) | yes (gate 0.6) | LANE B2 bMCC2 test2: masc vs default English corpus |
| 25 Sept 2026 18:42 | masc | N=746 K=24 restarts=8 corpus=pg1661_holmes_vdrop.txt+pg2701_mobydick_vdrop.txt | 1 | 0.985 (0.983-0.989) | -1958.813 | PASS - mccormick-1999 (a PASS is a gate for a verifier, not a reading; rule 10) | yes (gate 0.6) | LANE B2 bMCC2 test2: masc vs vowel-dropped English corpus |
| 25 Sept 2026 19:13 | homophonic | N=746 K=24 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1 | 0.999 (0.999-0.999) | not run (control-only) | - | yes | - |
| 25 Sept 2026 19:14 | homophonic | N=746 K=24 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1 | 0.998 (0.997-0.999) | -2190.651 | FAIL language: score=-1.48, null_p99=-2.071, real_p05=-0.864, real_median=-0.813, mode=both, N=746 | yes (gate 0.6) | LANE B3 bMCC3 test3: homophonic vs default English corpus |
| 25 Sept 2026 19:15 | homophonic | N=746 K=24 restarts=8 corpus=pg1661_holmes_vdrop.txt+pg2701_mobydick_vdrop.txt | 1 | 0.652 (0.058-0.992) | -1958.813 | FAIL language: score=-2.329, null_p99=-2.071, real_p05=-0.864, real_median=-0.813, mode=both, N=746 | yes (gate 0.6) | LANE B3 bMCC3 test3: homophonic vs vowel-dropped English corpus |
| 25 Sept 2026 19:18 | homophonic | N=746 K=24 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=1 | 1 | 0.998 (0.997-0.999) | -2547.687 | FAIL language: score=-1.807, null_p99=-2.071, real_p05=-0.864, real_median=-0.813, mode=both, N=746 | yes (gate 0.6) | LANE B3 bMCC3 test3: homophonic false-positive floor, target letters shuffled seed 1, default English corpus |
| 25 Sept 2026 19:18 | homophonic | N=746 K=24 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=2 | 1 | 0.998 (0.997-0.999) | -2569.063 | FAIL language: score=-1.839, null_p99=-2.071, real_p05=-0.864, real_median=-0.813, mode=both, N=746 | yes (gate 0.6) | LANE B3 bMCC3 test3: homophonic false-positive floor, target letters shuffled seed 2, default English corpus |
| 25 Sept 2026 19:19 | homophonic | N=746 K=24 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=3 | 1 | 0.998 (0.997-0.999) | -2559.700 | FAIL language: score=-1.896, null_p99=-2.071, real_p05=-0.864, real_median=-0.813, mode=both, N=746 | yes (gate 0.6) | LANE B3 bMCC3 test3: homophonic false-positive floor, target letters shuffled seed 3, default English corpus |
| 25 Sept 2026 19:20 | homophonic | N=746 K=24 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1 | 0.998 (0.997-0.999) | -2190.651 | FAIL language: score=-1.48, null_p99=-2.071, real_p05=-0.864, real_median=-0.813, mode=both, N=746 | yes (gate 0.6) | LANE B3 bMCC3 test3: homophonic vs default English corpus (rerun to preserve decode file separately from the vowel-dropped run, which shares the same output path) |

MCC-SWEEP (11 Oct 2026, 20:0x UTC by date -u, account 1, LANE DEFAULT-A1-1840; hand-written note outside the tool
table): token/nomenclator char-4-gram anneal (`specs/cheap-tests/mccormick-1999/token_anneal.py`), control-only length
sweep, PREREG-MCC-SWEEP.md. CONTROL type recovery mean 0.004 / 0.002 / 0.001 / 0.001, token recovery 0.003 / 0.036 /
0.001 / 0.010 at 132 / 500 / 2,000 / 8,000 tokens (3 seeds each; shuffled-order null token max 0.000-0.055); with the
temperature on the total log-prob scale (addendum 1): type 0.008 / 0.001 / 0.001 / 0.000, token 0.037 / 0.001 / 0.030 /
0.000. Gate 0.5 (type and token) met at no N; TARGET not run. Untestable by this instrument (as designed) at N <= 8,000;
not too-short, not refuted. Next: a word-level code-word anneal, control first (NOTES.md MCC-SWEEP).

MCC-WORD (14 Oct 2026, 22:28-22:42 UTC by date -u, account 2, LANE DEFAULT-A2-2209-14; hand-written note outside the tool
table): token/nomenclator family, second instrument -- word-level code-word anneal (`token_anneal.py --objective
wordbigram`: whole-word bigram LM, total-scale Gibbs anneal, code types from a 1,000-word pool), control-only sweep,
PREREG-MCC-WORD.md (e57f59f5f). Primary arm (LM held out from the control's source): CONTROL token recovery mean 0.069 /
0.108 / 0.104 / 0.106, type 0.020 / 0.007 / 0.003 / 0.002 at 132 / 500 / 2,000 / 8,000 tokens (3 seeds; shuffled-order
null token max 0.060 / 0.107 / 0.042 / 0.031; token ceiling 0.64-0.79). Diagnostic arm (LM in-sample): token 0.063 /
0.095 / 0.096 / 0.086, null max 0.129 / 0.109 / 0.101 / 0.092. Found total > truth total on all 24 runs: the objective's
optimum is not the truth (search not the limit). Read gate (token >= 0.5 and above null max) met at no N; TARGET not
run. Untestable by this instrument at N <= 8,000; not too-short, not refuted.
