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

- no. 7 gloss conflict (R8-SIENA7, 6 Oct 2026): the L08 gloss gives 2=e (C); the L04 small "o" sits over the 4/2 junction, so it gives
  either 2=o (conflicting with L08) or 4=o. Both witnesses are on the same leaf in the same glossing hand. Graded M and left unsettled
  until a closer crop or a second reader places it (glosses_no07.tsv).
- R8-SIENA19, 6 Oct 2026 (prose row; PREREG-R8-SIENA19.md, run_test_no19.py): no. 19 vs the no. 13/16 alignment (TRI=b, 3=l, CT=r;
  V2 adds 0=a, TT=r). TARGET S1 -6.812 / S2 -1.814 (P); CONTROL value-shuffled mean S1 -2.379 (p 0.939), S2 -1.589 (p 0.702);
  order-shuffled S2 mean -1.375. V2: TARGET -6.818 / -1.753, CONTROL -2.673 (p 0.924) / -1.553 (p 0.710), order-shuffled -1.378.
  Positive-control power <= 0.78 in every cell: non-test at this N (pre-registered), not a negative. Post hoc: TRI 10/118 vs 1.13
  expected for b; 0/100 H1 passages as low on S1.

- R9-SIENA15, 6 Oct 2026 (prose row; PREREG-R9-SIENA15.md pushed in cc19de4a4, concordance_R4764_no15.tsv, run_test_no15.py): no. 15
  vs key R4764 through a shape concordance. Statistic S2 = mean it16 bigram log10 prob inside valued stretches. P (14 signs valued, 71
  tokens; 6 null signs, 27 tokens): TARGET -1.354; CONTROL value-shuffled mean -1.484 (p95 -1.252, p 0.267), order-shuffled mean
  -1.402 (p95 -1.285). Power 0.63 < 0.8: non-test at this N (pre-registered), not a negative. V (P + 11 looser rows, 110 valued, 34
  null): TARGET -1.508; CONTROL value-shuffled mean -1.529 (p 0.478), order-shuffled mean -1.443 (p95 -1.351). Power 0.96: a
  control-backed negative for the V mapping (not for R4764 as a key: 88 (V) to 134 (P) of 232 tokens have no shape counterpart on the sheet).
| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 6 Oct 2026 05:52 | homophonic, 7 C gloss values fixed (R9-SIENA7) | no. 7 N=363 K=45, restarts=20 iters=60000 order 3, model it16dip minus gri_33125010469852 (held out for control text) | control 1-5, target 1-3 | 0.916 anchored (0.884-0.959); blind 0.875 (0.722-0.959); post hoc injected error 10/20/30%: 0.597/0.425/0.346 | -907.1 | FAIL language: score=-1.242, null_p99=-1.764, real_p05=-0.932, real_median=-0.816, mode=both, N=363 (shuffled-target decodes -1.411/-1.326/-1.345, all FAIL) | yes (gate 0.6) | no. 7 anchored fit: control reads error-free, target does not; control falls below gate at ~10% sign error, no. 7's own error unmeasured -- negative conditional on the transcription, not a design exclusion (PREREG-R9-SIENA7.md) |

R9-SIENA7B (6 Oct 2026, 06:2x UTC): transcription-error check for the R9-SIENA7 row. Pass B (blind Sonnet, legend only) vs agent J:
33.3% token disagreement on L02-L11 (sub 23.2%, ins 4.0%, del 6.1%; tx_error_no07.py), almost all pass-B collapses of legend
distinctions; worker arbitration of every split on L03+L08 gives agent J 0-3 errors in 72 tokens (0-4.2%, CP95 upper 5.0-11.7%),
below the control's ~10% crossover. The R9-SIENA7 negative stands as control-backed at that estimate (2 of 11 lines arbitrated).

R10-SIENA7C (6 Oct 2026, 09:5x UTC): arbitration of every agent J / pass B split on the other nine lines (L02, L04-L07, L09-L11;
L12 checked token by token) on 3-6x zooms of the image, extending R9-SIENA7B's L03/L08: agent J error 3/327 to 23/327 events on
L02-L11 (0.9-7.0%; CP95 of the high figure 4.5-10.4%; 6.6%, CP95 upper 9.7% with L12). Under PREREG-R10-SIENA7C.md: control-backed
at the point estimate, not at the 95% bound. The R9-SIENA7 negative (plain homophonic, seven C anchors) stands as control-backed on
the whole letter at the measured error (arb_error_no07.py).
