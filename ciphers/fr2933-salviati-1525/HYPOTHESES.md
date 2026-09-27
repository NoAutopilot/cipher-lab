# fr2933-salviati-1525 -- hypothesis families

Append-only. CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row whose gate is
not met reports a control that could not read its own design, and the target was not run. Rows written by hand by LANE R6
CM2 (25 Sept 2026) in `tools/family_run.py`'s column order; the code+mark family is not one of family_run.py's families,
so its runs go through `control/codemark_curve.py` (env `CM_RESTARTS`, `CM_NOISE`, `CM_TOL`, `CM_ROBUST`) and the rows
of `control_curve.tsv`. Earlier code+mark and vowel-indicator runs (LANE R4 P, LANE R6 CM) are in NOTES.md and
`control_curve.tsv`, not repeated here.

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 25 Sept 2026 19:04 | code+mark, erasure-tolerant solve (tools/homophonic_anneal.py --noise 0.1) | N=2820 K=223 restarts=24 CM_NOISE=0.1 CM_TOL=0.1 corpus=it16 (5 files) | 1-3 | token acc 0.341 (0.273-0.394); key-only 0.348 | not run (CONTROL BELOW GATE) | - | no (gate 0.6 on 2 of 3) | LANE R6 CM2 (Fable, session_01AtRe8LEF72DEuye52Rg7Pi); plain solver on the same control read 0.347 (0.265-0.429), LANE R6 CM |
| 25 Sept 2026 19:04 | code+mark, erasure-tolerant solve (--noise 0.2) | N=2820 K=223 restarts=24 CM_NOISE=0.2 CM_TOL=0.2 corpus=it16 | 1-3 | token acc 0.270 (0.131-0.403); key-only 0.277 | not run (CONTROL BELOW GATE) | - | no | LANE R6 CM2; plain solver 0.252 (0.237-0.265), LANE R6 CM |
| 25 Sept 2026 19:13 | code+mark, bounded-loss scoring (tools/homophonic_anneal.py --robust 0.1) | N=2820 K=223 restarts=24 CM_NOISE=0.1 CM_ROBUST=0.1 corpus=it16 | 1-3 | token acc 0.475 (0.415-0.583) | not run (CONTROL BELOW GATE) | - | no (gate 0.6 on 2 of 3; best seed 0.583) | LANE R6 CM2; plain solver on the same streams 0.347 (0.265-0.429), LANE R6 CM |
| 25 Sept 2026 19:13 | code+mark, bounded-loss scoring (--robust 0.2) | N=2820 K=223 restarts=24 CM_NOISE=0.2 CM_ROBUST=0.2 corpus=it16 | 1-3 | token acc 0.310 (0.253-0.378) | not run (CONTROL BELOW GATE) | - | no | LANE R6 CM2; plain solver 0.252 (0.237-0.265), LANE R6 CM |
| 25 Sept 2026 19:22 | code+mark read through merged symbols (design cmc: base code + mark class none/dot/digit-led/other, 106-111 symbols, ceiling 0.809 on the noisy stream) | N=2820 K=223->111 restarts=24 CM_NOISE=0.1 corpus=it16 | 1-3 | token acc 0.491 (0.471-0.515) | not run (CONTROL BELOW GATE) | - | no (gate 0.6 on 2 of 3) | LANE R6 CM2; plain cm solver on the same streams 0.347 (0.265-0.429) |
| 25 Sept 2026 19:22 | cmc | N=2820 K=223->107 restarts=24 CM_NOISE=0.2 corpus=it16 | 1-3 | token acc 0.173 (0.027-0.308) | not run (CONTROL BELOW GATE) | - | no | LANE R6 CM2; plain cm solver 0.252 (0.237-0.265) |
| 25 Sept 2026 19:23 | code+mark, bounded-loss scoring, mixture weight sweep (--robust 0.05) | N=2820 K=223 restarts=24 CM_NOISE=0.1 CM_ROBUST=0.05 corpus=it16 | 1-3 | token acc 0.481 (0.427-0.571) | not run (CONTROL BELOW GATE) | - | no | LANE R6 CM2; with q=0.1 0.475 (0.415-0.583), q=0.3 next row |
| 25 Sept 2026 19:23 | code+mark, bounded-loss scoring (--robust 0.3) | N=2820 K=223 restarts=24 CM_NOISE=0.1 CM_ROBUST=0.3 corpus=it16 | 1-3 | token acc 0.363 (0.128-0.542) | not run (CONTROL BELOW GATE) | - | no | LANE R6 CM2; the mixture weight has no setting that passes: 0.05 / 0.1 / 0.3 read 0.48 / 0.48 / 0.36 on the 10% control, plain 0.35 |
| 25 Sept 2026 19:26 | cmc under bounded-loss scoring (--robust 0.1) | N=2820 K=223->111 restarts=24 CM_NOISE=0.1 CM_ROBUST=0.1 corpus=it16 | 1-3 | token acc 0.292 (0.166-0.416) | not run (CONTROL BELOW GATE) | - | no | LANE R6 CM2; stacking the two lifts loses both (cmc alone 0.491, bounded loss alone 0.475, plain 0.347) |
| 25 Sept 2026 21:31 | code+mark, plain trigram solver, MEASURED error mix (CM_ERR: deletions 46.5%, insertions 33.1%, base-code confusions 20.4% of errors; #/+, g/y, bh/g, #/Z, f/y, bh/phi) | N=2820 K=223 restarts=24 CM_ERR=0.05 (the measured residual, NOTES "CM3" sec.1) corpus=it16 | 1-3 | token acc 0.765 (0.617-0.860); score/symbol -2.38 to -2.51 | seeds 1-6 (r24): -7490.9 to -7552.9 = -2.656 to -2.678/symbol; cross-seed agreement 1-20%; no Italian | no reading, judge not applicable | **yes (3 of 3 >= 0.6)** | LANE R7 CM3 (Fable); target below every control seed; control-backed negative for letter-per-type cm at the measured error, conditional on the error estimate and the design (NOTES CM3 sec.5) |
| 25 Sept 2026 21:35 | code+mark, plain trigram solver, measured mix at the bracket top | N=2820 K=223 restarts=24 CM_ERR=0.07 corpus=it16 | 1-3 | token acc 0.625 (0.472-0.794); score/symbol -2.43 to -2.57 | same target runs, -2.656 to -2.678/symbol | - | **yes (2 of 3 >= 0.6: 0.794, 0.608)** | LANE R7 CM3; target still 0.09/symbol below the worst control seed |
| 25 Sept 2026 21:35 | code+mark, interpolated 5-gram backoff model (tools/homophonic_anneal.py --backoff, CM_ORDER=5 CM_BACKOFF=1) | N=2820 K=223 restarts=24 CM_ERR=0.05 corpus=it16 | 1-3 | token acc 0.150 (0.067-0.223); found -3.01 to -3.04/symbol vs true key -2.40 | not run (CONTROL BELOW GATE) | - | no | LANE R7 CM3; a search failure under the backoff landscape at t0=4, 120k iters (true key scores 1,640-1,680 nats above the anneal's best), not a model verdict; schedule owed |

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 25 Sept 2026 22:37 | syllabary | N=2820 K=223 restarts=6 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.05 | 1 | 0.950 (0.950-0.950) | -10229.499 | FAIL language: score=-1.365, null_p99=-1.857, real_p05=-0.911, real_median=-0.822, mode=both, N=3714 | yes (gate 0.6) | LANE R8 DSN (Fable): partial syllabary, control seed 1 at the measured 5% error then target seed 1 |
| 25 Sept 2026 22:37 | syllabary | N=2820 K=223 restarts=6 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.05 | 2 | 0.940 (0.940-0.940) | -10300.548 | FAIL language: score=-1.367, null_p99=-1.857, real_p05=-0.911, real_median=-0.822, mode=both, N=3714 | yes (gate 0.6) | LANE R8 DSN (Fable): partial syllabary, control seed 2 at the measured 5% error then target seed 2 |
| 25 Sept 2026 22:37 | syllabary | N=2820 K=223 restarts=6 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.05 | 3 | 0.930 (0.930-0.930) | -10264.154 | FAIL language: score=-1.365, null_p99=-1.857, real_p05=-0.911, real_median=-0.822, mode=both, N=3714 | yes (gate 0.6) | LANE R8 DSN (Fable): partial syllabary, control seed 3 at the measured 5% error then target seed 3 |
| 25 Sept 2026 22:39 | syllabary | N=2820 K=223 restarts=6 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0 | 1-3 | 0.982 (0.976-0.993) | not run (control-only) | - | yes | LANE R8 DSN (Fable): partial syllabary 0%-error ceiling (rule 3 headroom check) |
| 25 Sept 2026 22:41 | syllabary | N=2820 K=223 restarts=6 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.05,assign=irregular | 1 | 0.177 (0.177-0.177) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | LANE R8 DSN (Fable): syllabary, IRREGULAR assignment (a vowel per marked type), control seed 1 at 5% error then target seed 1 |
| 25 Sept 2026 22:41 | syllabary | N=2820 K=223 restarts=6 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.05,assign=irregular | 2 | 0.242 (0.242-0.242) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | LANE R8 DSN (Fable): syllabary, IRREGULAR assignment (a vowel per marked type), control seed 2 at 5% error then target seed 2 |
| 25 Sept 2026 22:41 | syllabary | N=2820 K=223 restarts=6 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.05,assign=irregular | 3 | 0.229 (0.229-0.229) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | LANE R8 DSN (Fable): syllabary, IRREGULAR assignment (a vowel per marked type), control seed 3 at 5% error then target seed 3 |
| 25 Sept 2026 22:42 | syllabary | N=2820 K=223 restarts=6 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.07 | 1-3 | 0.881 (0.836-0.913) | not run (control-only) | - | yes | LANE R8 DSN (Fable): partial syllabary at the error bracket top 7% |
| 25 Sept 2026 22:42 | syllabary | N=2820 K=223 restarts=24 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.05,assign=irregular | 2 | 0.242 (0.242-0.242) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | LANE R8 DSN (Fable): syllabary, IRREGULAR assignment, 24 restarts, control seed 2 at 5% error then target seed 2 |
| 25 Sept 2026 22:42 | syllabary | N=2820 K=223 restarts=24 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.05,assign=irregular | 1 | 0.783 (0.783-0.783) | -9985.150 | FAIL language: score=-1.311, null_p99=-1.857, real_p05=-0.911, real_median=-0.822, mode=both, N=3714 | yes (gate 0.6) | LANE R8 DSN (Fable): syllabary, IRREGULAR assignment, 24 restarts, control seed 1 at 5% error then target seed 1 |
| 25 Sept 2026 22:42 | syllabary | N=2820 K=223 restarts=24 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.05,assign=irregular | 3 | 0.852 (0.852-0.852) | -9977.045 | FAIL language: score=-1.298, null_p99=-1.857, real_p05=-0.911, real_median=-0.822, mode=both, N=3714 | yes (gate 0.6) | LANE R8 DSN (Fable): syllabary, IRREGULAR assignment, 24 restarts, control seed 3 at 5% error then target seed 3 |
| 25 Sept 2026 23:26 | syllabary | N=2820 K=223 restarts=24 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.05,bases=8,boundary=1 | 3 | 0.838 (0.838-0.838) | -13967.073 | FAIL language: score=-1.355, null_p99=-1.857, real_p05=-0.911, real_median=-0.822, mode=both, N=3714 | yes (gate 0.6) | LANE R8 DSN2 (Fable): V3 regular syllabary + run-edge boundary symbol, control marks on the 8 most-marked bases, control seed 3 at 5% error then target seed 3 |
| 25 Sept 2026 23:26 | syllabary | N=2820 K=223 restarts=24 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.05,bases=8,boundary=1 | 1 | 0.943 (0.943-0.943) | -14016.232 | FAIL language: score=-1.35, null_p99=-1.857, real_p05=-0.911, real_median=-0.822, mode=both, N=3714 | yes (gate 0.6) | LANE R8 DSN2 (Fable): V3 regular syllabary + run-edge boundary symbol, control marks on the 8 most-marked bases, control seed 1 at 5% error then target seed 1 |
| 25 Sept 2026 23:26 | syllabary | N=2820 K=223 restarts=24 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.05,bases=8,boundary=1 | 2 | 0.725 (0.725-0.725) | -13978.338 | FAIL language: score=-1.404, null_p99=-1.857, real_p05=-0.911, real_median=-0.822, mode=both, N=3714 | yes (gate 0.6) | LANE R8 DSN2 (Fable): V3 regular syllabary + run-edge boundary symbol, control marks on the 8 most-marked bases, control seed 2 at 5% error then target seed 2 |
| 25 Sept 2026 23:25 | syllabary | N=2820 K=223 restarts=24 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.05,marks=mixed | 3 | 0.958 (0.958-0.958) | -10957.807 | FAIL language: score=-1.446, null_p99=-1.857, real_p05=-0.911, real_median=-0.822, mode=both, N=3714 | yes (gate 0.6) | LANE R8 DSN2 (Fable): V1 marks mixed (numerals=vowel, ~=n/m, others=doubling), control seed 3 at 5% error then target seed 3 |
| 25 Sept 2026 23:25 | syllabary | N=2820 K=223 restarts=24 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.05,marks=mixed | 2 | 0.939 (0.939-0.939) | -10974.709 | FAIL language: score=-1.475, null_p99=-1.857, real_p05=-0.911, real_median=-0.822, mode=both, N=3714 | yes (gate 0.6) | LANE R8 DSN2 (Fable): V1 marks mixed (numerals=vowel, ~=n/m, others=doubling), control seed 2 at 5% error then target seed 2 |
| 25 Sept 2026 23:25 | syllabary | N=2820 K=223 restarts=24 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.05,marks=mixed | 1 | 0.934 (0.934-0.934) | -10982.004 | FAIL language: score=-1.467, null_p99=-1.857, real_p05=-0.911, real_median=-0.822, mode=both, N=3714 | yes (gate 0.6) | LANE R8 DSN2 (Fable): V1 marks mixed (numerals=vowel, ~=n/m, others=doubling), control seed 1 at 5% error then target seed 1 |
| 25 Sept 2026 23:28 | syllabary | N=2820 K=223 restarts=24 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.05,marks=mixed,boundary=1 | 2 | 0.948 (0.948-0.948) | -14817.760 | FAIL language: score=-1.461, null_p99=-1.857, real_p05=-0.911, real_median=-0.822, mode=both, N=3714 | yes (gate 0.6) | LANE R8 DSN2 (Fable): V2 marks mixed + run-edge boundary symbol, control seed 2 at 5% error then target seed 2 |
| 25 Sept 2026 23:28 | syllabary | N=2820 K=223 restarts=24 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.05,marks=mixed,boundary=1 | 1 | 0.951 (0.951-0.951) | -14908.960 | FAIL language: score=-1.495, null_p99=-1.857, real_p05=-0.911, real_median=-0.822, mode=both, N=3714 | yes (gate 0.6) | LANE R8 DSN2 (Fable): V2 marks mixed + run-edge boundary symbol, control seed 1 at 5% error then target seed 1 |
| 25 Sept 2026 23:28 | syllabary | N=2820 K=223 restarts=24 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.05,marks=mixed,boundary=1 | 3 | 0.883 (0.883-0.883) | -14883.134 | FAIL language: score=-1.435, null_p99=-1.857, real_p05=-0.911, real_median=-0.822, mode=both, N=3714 | yes (gate 0.6) | LANE R8 DSN2 (Fable): V2 marks mixed + run-edge boundary symbol, control seed 3 at 5% error then target seed 3 |
| 25 Sept 2026 23:39 | syllabary | N=2820 K=223 restarts=6 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0,bases=8,boundary=1 | 1-3 | 0.955 (0.939-0.984) | not run (control-only) | - | yes | LANE R8 DSN2 (Fable): V3 regular + boundary + 8 bases, 0%-error ceiling (rule 3 headroom) |
| 25 Sept 2026 23:39 | syllabary | N=2820 K=223 restarts=6 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0,marks=mixed | 1-3 | 0.947 (0.884-0.990) | not run (control-only) | - | yes | LANE R8 DSN2 (Fable): V1 marks mixed, 0%-error ceiling (rule 3 headroom) |
| 25 Sept 2026 23:39 | syllabary | N=2820 K=223 restarts=6 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0,marks=mixed,boundary=1 | 1-3 | 0.981 (0.977-0.985) | not run (control-only) | - | yes | LANE R8 DSN2 (Fable): V2 marks mixed + boundary, 0%-error ceiling (rule 3 headroom) |
| 26 Sept 2026 09:57 | syllabary | N=2820 K=223 restarts=6 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.10 | 1-3 | 0.889 (0.872-0.902) | not run (control-only) | - | yes | LANE R8 SALV-DIAG (Sonnet): syllabary control error sweep extension, 10 pct |
| 26 Sept 2026 10:00 | syllabary | N=2820 K=223 restarts=6 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.12 | 1-3 | 0.636 (0.261-0.884) | not run (control-only) | - | yes | LANE R8 SALV-DIAG (Sonnet): syllabary control error sweep extension, 12 pct |
| 26 Sept 2026 10:05 | syllabary | N=2820 K=223 restarts=6 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.14 | 1-3 | 0.845 (0.832-0.865) | not run (control-only) | - | yes | LANE R8 SALV-DIAG (Sonnet): syllabary control error sweep extension, 14 pct |
| 26 Sept 2026 12:29 | syllabary | N=2839 K=236 restarts=6 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.064 | 1 | 0.646 (0.153-0.921) | -10344.002 | FAIL language: score=-1.337, null_p99=-1.849, real_p05=-0.944, real_median=-0.831, mode=both, N=3757 | yes (gate 0.6) | LANE B11 bSALR (Opus): DSN regular re-run on pass-C spec at measured 6.4% error |
| 26 Sept 2026 12:33 | syllabary | N=2839 K=236 restarts=6 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.064,shuffle_target=1 | 1 | 0.609 (0.117-0.921) | -10693.792 | FAIL language: score=-1.414, null_p99=-1.849, real_p05=-0.944, real_median=-0.831, mode=both, N=3757 | yes (gate 0.6) | LANE B11 bSALR (Opus): DSN regular, shuffled-target judge floor at 6.4% |
| 26 Sept 2026 12:47 | syllabary | N=2839 K=236 restarts=24 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.064,marks=mixed | 1 | 0.854 (0.818-0.921) | -11082.797 | FAIL language: score=-1.481, null_p99=-1.849, real_p05=-0.944, real_median=-0.831, mode=both, N=3757 | yes (gate 0.6) | LANE B11 bSALR (Opus): DSN2 V1 marks mixed at measured 6.4% |
| 26 Sept 2026 13:01 | syllabary | N=2839 K=236 restarts=24 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.064,bases=8,boundary=1 | 1 | 0.850 (0.809-0.889) | -14141.931 | FAIL language: score=-1.362, null_p99=-1.849, real_p05=-0.944, real_median=-0.831, mode=both, N=3757 | yes (gate 0.6) | LANE B11 bSALR (Opus): DSN2 V3 bases 8 + boundary at measured 6.4% |
| 26 Sept 2026 13:49 | syllabary | N=2839 K=236 restarts=24 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.064 | 1 | 0.777 (0.546-0.921) | -10305.386 | FAIL language: score=-1.349, null_p99=-1.849, real_p05=-0.944, real_median=-0.831, mode=both, N=3757 | yes (gate 0.6) | LANE B11 bSALR2: DSN regular 24 restarts, target seed 1, measured err |
| 26 Sept 2026 14:02 | syllabary | N=2839 K=236 restarts=24 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.064 | 2 | 0.910 (0.864-0.945) | -10246.726 | FAIL language: score=-1.31, null_p99=-1.849, real_p05=-0.944, real_median=-0.831, mode=both, N=3757 | yes (gate 0.6) | LANE B11 bSALR2: DSN regular 24 restarts, target seed 2, measured err |
| 26 Sept 2026 14:16 | syllabary | N=2839 K=236 restarts=24 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.064 | 3 | 0.928 (0.919-0.945) | -10263.072 | FAIL language: score=-1.32, null_p99=-1.849, real_p05=-0.944, real_median=-0.831, mode=both, N=3757 | yes (gate 0.6) | LANE B11 bSALR2: DSN regular 24 restarts, target seed 3, measured err |
| 26 Sept 2026 14:30 | syllabary | N=2839 K=236 restarts=24 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.064,marks=mixed,boundary=1 | 1 | 0.879 (0.872-0.890) | -15116.439 | FAIL language: score=-1.478, null_p99=-1.849, real_p05=-0.944, real_median=-0.831, mode=both, N=3757 | yes (gate 0.6) | LANE B11 bSALR2: DSN2 V2 marks=mixed boundary=1, measured err |
| 26 Sept 2026 16:17 | syllabary | N=2839 K=236 restarts=24 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.064,assign=irregular | 1-3 | 0.467 (0.125-0.722) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | LANE B11 bSALI: DSN irregular 24 restarts, target seed 1, measured err |
| 26 Sept 2026 17:51 | wordcode | N=2839 K=236 restarts=4 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0 | 1-3 | 0.562 (0.143-0.782) | not run (control-only) | - | no | bSALW LANE B12: 0% error ceiling |
| 26 Sept 2026 17:54 | wordcode | N=2839 K=236 restarts=8 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0,iters=80000 | 1-3 | 0.687 (0.402-0.830) | not run (control-only) | - | yes | bSALW LANE B12: 0% error ceiling, 8x80k |
| 26 Sept 2026 17:58 | wordcode | N=2839 K=236 restarts=8 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.064,iters=80000 | 1 | 0.633 (0.391-0.759) | -7254.226 | FAIL language: score=-1.061, null_p99=-1.858, real_p05=-0.875, real_median=-0.821, mode=both, N=4164 | yes (gate 0.6) | bSALW LANE B12: 6.4pct measured error, 8x80k |
| 26 Sept 2026 18:00 | wordcode | N=2839 K=236 restarts=8 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.064,iters=80000,shuffle_target=1 | 1 | 0.757 (0.757-0.757) | -7586.972 | FAIL language: score=-1.098, null_p99=-1.869, real_p05=-0.916, real_median=-0.833, mode=both, N=4045 | yes (gate 0.6) | bSALW LANE B12: shuffle floor |
| 26 Sept 2026 18:02 | wordcode | N=2839 K=236 restarts=8 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.064,iters=80000 | 3 | 0.759 (0.759-0.759) | -7334.167 | FAIL language: score=-1.108, null_p99=-1.863, real_p05=-0.903, real_median=-0.824, mode=both, N=4042 | yes (gate 0.6) | bSALW LANE B12: target seed 3 |

## wordcode + context, SALV-CTX control (26 Sept 2026, LANE SALV)

Pre-registered gate (written 26 Sept 2026 before any context run, from the job brief
.claude/briefs/runs/2026-09-26-lane-salv-j2a-context.md): context "adds a reproducible margin" if the code-class token
accuracy rises by at least 0.10 on the 3-seed mean AND is higher on each of the 3 seeds, with blended accuracy not lower
on the mean; the blind code-class mean must be under 0.70 (headroom check, rule 3 Salviati paragraph; if not, stop). A
gate met at ctxshare=0.5 licenses job 2b on the four transcribed leaves; met only at 1.0, job 2b waits for all eight.
Settings for all three runs: `tools/family_run.py specs/fr2933-salviati-1525.json --family wordcode --control-only
--seeds 3 --restarts 8 --corpus tools/data/it16dip --param err=0.064 --param iters=80000` (bSALW's 6.4% row; codes=marked,
codeletters=0 are the defaults), control seeds 1-3 in every run; (ii)/(iii) add `--param context=control --param
ctxshare=1.0|0.5`. Control only; the target is not run.

family_run.py rows (control-only, written to a scratch --out per run so three parallel runs could not interleave their appends, copied here verbatim):

| date (UTC) | family | parameters | seed(s) | control recovery | target | judge | gated | label |
|---|---|---|---|---|---|---|---|---|
| 26 Sept 2026 21:38 | wordcode | N=2839 K=236 restarts=8 corpus=bub_gb_ZJMxff7r4LUC.txt.gz+bub_gb_laRnTtJmsDAC.txt.gz+gri_33125010469852.txt.gz+letterediprincip01char.txt.gz+letterediprincip02char.txt.gz+letterediprincip03char.txt.gz err=0.064,iters=80000 | 1-3 | 0.755 (0.596-0.854) | not run (control-only) | - | yes | SALV-CTX (i) blind, it16dip |
| 26 Sept 2026 21:38 | wordcode | N=2839 K=236 restarts=8 corpus=bub_gb_ZJMxff7r4LUC.txt.gz+bub_gb_laRnTtJmsDAC.txt.gz+gri_33125010469852.txt.gz+letterediprincip01char.txt.gz+letterediprincip02char.txt.gz+letterediprincip03char.txt.gz err=0.064,iters=80000,context=control,ctxshare=1.0 | 1-3 | 0.800 (0.766-0.840) | not run (control-only) | - | yes | SALV-CTX (ii) context ctxshare=1.0, it16dip |
| 26 Sept 2026 21:38 | wordcode | N=2839 K=236 restarts=8 corpus=bub_gb_ZJMxff7r4LUC.txt.gz+bub_gb_laRnTtJmsDAC.txt.gz+gri_33125010469852.txt.gz+letterediprincip01char.txt.gz+letterediprincip02char.txt.gz+letterediprincip03char.txt.gz err=0.064,iters=80000,context=control,ctxshare=0.5 | 1-3 | 0.798 (0.772-0.841) | not run (control-only) | - | yes | SALV-CTX (iii) context ctxshare=0.5, it16dip |

Per seed (token accuracy; codes split by whether the clean truth word occurs once (hapax) or more as a code token in
that control; stdout "per class" lines, logs of 26 Sept 2026 21:36-21:38 UTC):

| run | seed | blended | letters | codes | codes-hapax | codes-repeated |
|---|---|---|---|---|---|---|
| (i) blind | 1 | 0.854 | 0.952 | 0.392 | 0.000 (n=124) | 0.523 (n=373) |
| (i) blind | 2 | 0.816 | 0.945 | 0.513 | 0.000 (n=103) | 0.584 (n=745) |
| (i) blind | 3 | 0.596 | 0.757 | 0.000 | 0.000 (n=101) | 0.000 (n=502) |
| (i) blind | mean | 0.755 | 0.885 | **0.302** | 0.000 | 0.369 |
| (ii) context, ctxshare=1.0 | 1 | 0.840 | 0.952 | 0.316 | 0.000 | 0.421 |
| (ii) context, ctxshare=1.0 | 2 | 0.794 | 0.933 | 0.468 | 0.000 | 0.533 |
| (ii) context, ctxshare=1.0 | 3 | 0.766 | 0.882 | 0.338 | 0.000 | 0.406 |
| (ii) context, ctxshare=1.0 | mean | 0.800 | 0.922 | **0.374** | 0.000 | 0.453 |
| (iii) context, ctxshare=0.5 | 1 | 0.841 | 0.952 | 0.318 | 0.000 | 0.424 |
| (iii) context, ctxshare=0.5 | 2 | 0.780 | 0.912 | 0.469 | 0.000 | 0.534 |
| (iii) context, ctxshare=0.5 | 3 | 0.772 | 0.890 | 0.337 | 0.000 | 0.404 |
| (iii) context, ctxshare=0.5 | mean | 0.798 | 0.918 | **0.375** | 0.000 | 0.454 |

Headroom check: blind code-class mean 0.302 < 0.70, so the gate could be tested.
Gate: code-class mean rises +0.072 (1.0) and +0.073 (0.5), under the +0.10 required; per seed it FALLS on seeds 1 and 2
(0.392 -> 0.316/0.318, 0.513 -> 0.468/0.469) and rises only on seed 3, which is the blind run's search failure (codes
0.000, letters 0.757) -- the context terms changed that seed's anneal trajectory, not the code assignment on seeds
that searched well. Blended mean not lower (0.755 -> 0.800/0.798).

**Verdict: gate not met at ctxshare 1.0, not met at ctxshare 0.5.** The context option adds no reproducible margin on
the code class in this control; job 2b is not licensed by this control.

Diagnostics (same controls rebuilt at err=0, no solve, 26 Sept 2026 21:39 UTC):
- Hapax code tokens are 0.000 in every arm. Only 36-48 of 101-124 hapax truth words (0.35-0.48) are in the solver's
  1,000-word list at all (repeated: 0.92-0.99); the other half cannot be read by any setting, and the reachable half
  was not read either -- one word bigram at a run edge does not pin a type seen once.
- The control's own context is right: e.g. seed 1 runs 1-3 carry (uoleua | come), (come | piu), (piu | signorie),
  the withheld words on either side, shared between neighbouring runs across a one-word gap.
- Design mismatch to name (rule 3 Salviati paragraph): on it16dip the control's code token share is 0.175 / 0.299 /
  0.212 against the target's 0.323 (on it16, bSALW matched 0.28-0.33). The bisection on the common-word part does
  not reach the share with this noisier vocabulary. Both arms share the mismatch, so the blind-vs-context comparison
  stands, but a control at the target's code share is not yet run; a rerun there (or on `it`) is the named check
  before this negative is read as a design statement about context scoring.

## wordcode + context at the target's code share, SALV-CTX2 (26 Sept 2026, LANE SALV)

Worker SALV-CTX2 (Sonnet), the share-matched rerun named above, on the default `it` corpus (bSALW's own six
tools/data/it16 files, spec judge.language "it"), not it16dip. Same command and gate as SALV-CTX, `--corpus`
dropped so family_run.py resolves the spec's own judge corpus. **This is the last attempt with this instrument
(CLAUDE.md rule 3, repeated-attempt paragraph): the context option is retired for this target after this run,
whatever the outcome, not re-briefed for a further knob change.**

Pre-registered gate (unchanged, copied from the SALV-CTX section above before this section's runs): context "adds
a reproducible margin" if the code-class token accuracy rises by at least 0.10 on the 3-seed mean AND is higher on
each of the 3 seeds, with blended accuracy not lower on the mean; the blind code-class mean must be under 0.70
(headroom check, rule 3 Salviati paragraph; if not, stop). Control only; the target is not run.

Command: `python3 tools/family_run.py specs/fr2933-salviati-1525.json --family wordcode --control-only --seeds 3
--restarts 8 --corpus tools/data/it16 --param err=0.064 --param iters=80000` for (i), plus `--param
context=control --param ctxshare=1.0` for (ii). Run serially (not in parallel, to avoid the GOLD-K3 CPU-sharing
lesson); rows written to a scratch --out per run, copied here verbatim.

| date (UTC) | family | parameters | seed(s) | control recovery | target | judge | gated | label |
|---|---|---|---|---|---|---|---|---|
| 26 Sept 2026 22:04 | wordcode | N=2839 K=236 restarts=8 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.064,iters=80000 | 1-3 | 0.633 (0.391-0.759) | not run (control-only) | - | yes | SALV-CTX2 (i) blind, it corpus |
| 26 Sept 2026 22:08 | wordcode | N=2839 K=236 restarts=8 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt err=0.064,iters=80000,context=control,ctxshare=1.0 | 1-3 | 0.721 (0.666-0.777) | not run (control-only) | - | yes | SALV-CTX2 (ii) context ctxshare=1.0, it corpus |

Code token share per seed, confirmed from stdout before either run counted (target 0.323; brief's 0.28-0.36
bracket): seed 1 0.326, seed 2 0.309, seed 3 0.28 -- all within bracket (both arms use the same control layout per
seed, so the shares are identical across (i)/(ii)). This clears the SALV-CTX design mismatch (it16dip read
0.18-0.30); no bisection tuning was done to force it.

Per seed (token accuracy; codes split hapax/repeated as in the SALV-CTX table; stdout "per class" lines, logs of
26 Sept 2026 22:02-22:08 UTC):

| run | seed | blended | letters | codes | codes-hapax | codes-repeated |
|---|---|---|---|---|---|---|
| (i) blind | 1 | 0.747 | 0.838 | 0.560 | 0.000 (n=123) | 0.646 (n=802) |
| (i) blind | 2 | 0.391 | 0.462 | 0.233 | 0.000 (n=132) | 0.274 (n=745) |
| (i) blind | 3 | 0.759 | 0.900 | 0.399 | 0.000 (n=136) | 0.481 (n=659) |
| (i) blind | mean | 0.633 | 0.733 | **0.397** | 0.000 | 0.467 |
| (ii) context, ctxshare=1.0 | 1 | 0.777 | 0.898 | 0.526 | 0.000 (n=123) | 0.607 (n=802) |
| (ii) context, ctxshare=1.0 | 2 | 0.666 | 0.767 | 0.440 | 0.000 (n=132) | 0.518 (n=745) |
| (ii) context, ctxshare=1.0 | 3 | 0.721 | 0.870 | 0.337 | 0.000 (n=136) | 0.407 (n=659) |
| (ii) context, ctxshare=1.0 | mean | 0.721 | 0.845 | **0.434** | 0.000 | 0.511 |

Headroom check: blind code-class mean 0.397 < 0.70, so the gate could be tested.
Gate: code-class mean rises +0.037 (0.397 -> 0.434), under the +0.10 required -- smaller than SALV-CTX's own
+0.072/+0.073 on the design-mismatched it16dip control, i.e. matching the target's code share did not move the
number toward the gate. Per seed it FALLS on seeds 1 and 3 (0.560 -> 0.526, 0.399 -> 0.337) and rises only on
seed 2 (0.233 -> 0.440), the blind run's weakest seed -- the same one-seed-only-rises shape as SALV-CTX (there it
was the blind run's search-failure seed 3; here it is blind's weakest seed 2), not every number moving together
toward the bet. Blended mean not lower (0.633 -> 0.721).

**Verdict: gate not met.** Per CLAUDE.md rule 3's repeated-attempt paragraph (the design-share knob was the bet
this re-brief made, and the gate still fails, in the same shape as before, on a control that no longer carries
the design mismatch): **context option untested-by-this-tool at N=2839 for this target (two controls, it16dip
and it, both below gate); not refuted.** No further context re-brief on this target without a different
instrument or new material (a decode script or a differently-scored context term, not another corpus swap).

## Old split (SALV2 J2, 27 Sept 2026)

Every row above, dated at or before 27 Sept 2026 01:25 UTC (the last is 26 Sept 2026 22:08; checked directly
against the table, none falls between then and the cutoff), ran on the pre-27-Sept plain/sign split: about 98
sign boxes among the leaves' plain-labelled positions were mislabelled plain by the spec's `row_pattern` (SALV-
SPLIT, 71.5% flagged sign-rate vs an 11.7% matched control), and 63 run boundaries were consequently wrong. Every
row above is re-labelled **on the old split**: neither refuted nor confirmed on the corrected text (2,932 tokens,
251 types, 327 runs, 1,121 plain boxes; SALV2-J2, this target's NOTES.md). No row above is edited (append-only,
CLAUDE.md rule 3/7); this section is the re-label. New runs on the corrected split are appended below, dated after
this line.

## cm rerun, corrected split (SALV2-J2, 27 Sept 2026)

Control first (rule 3, family_run.py's own discipline): both levels FAIL their own gate on the corrected split's
larger key inventory (K=251, up from 223 -- 8 individually-unread `?` boxes now hapax types, 7 more real code+mark
combinations job 1's transcription surfaced), so the target step is not run at either level.

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 27 Sept 2026 03:02 | code+mark, plain trigram solver, measured mix, corrected split | N=2932 K=251 restarts=24 CM_ERR=0.07 corpus=it16 | 1-3 | token acc 0.363 (0.284-0.439); score/symbol -2.543 to -2.548 (true plaintext -2.302) | not run (CONTROL BELOW GATE) | - | no (gate 0.6 on 2 of 3; 0 of 3 met) | SALV2-J2 (Sonnet); the same setting passed 2 of 3 (0.794, 0.608) on the old split's K=223 (25 Sept 21:35 row) -- the corrected split's +28-type larger key inventory (K=251) is the difference |
| 27 Sept 2026 03:02 | code+mark, plain trigram solver, measured mix, corrected split | N=2932 K=251 restarts=24 CM_ERR=0.08 corpus=it16 | 1-3 | token acc 0.529 (0.247-0.859); score/symbol -2.362 to -2.591 (true plaintext -2.302) | not run (CONTROL BELOW GATE) | - | no (gate 0.6 on 2 of 3; 1 of 3 met, seed 2 only) | SALV2-J2 (Sonnet); required second level per the job brief (job 1's own +job2's recomputed ~6.8-6.9% estimate brackets both 0.07 and 0.08); still fails 2-of-3 -- CONTROL BELOW GATE at both settings this job could run, letter-per-type cm on the corrected split is a non-test, not a design exclusion, until the control passes its own gate (rule 3) |
