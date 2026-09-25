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
