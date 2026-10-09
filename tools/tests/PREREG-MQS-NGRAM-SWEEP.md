# PREREG MQS-NGRAM-SWEEP: n-gram order x score norm on the matched homophonic control

Written 9 Oct 2026, 06:51 UTC by date -u, by MQS-NGRAM-SWEEP (LANE MQS-2, account 4), before any accuracy below is
read (one timing-only run at N=400, seed 9, output discarded, sized the grid). Brief stub:
`.claude/briefs/runs/2026-10-09-ytbiz-mqs-next-ngram-sweep.md`; research row M13 (research/MARY-STUART-TALK-2026-10-09.tsv).
Credit: Lasry, Biermann and Tomokiyo 2023 (Cryptologia 47:2) App. A pp.195-196 (S = sum N_g log F_g / sum N_c^2 with
5-grams). Builds on MQS-SOLVER's `--norm nc2paper` (no code change planned to tools/homophonic_anneal.py); runner
`tools/tests/mqs_ngram_sweep.py`, results `tools/tests/MQS-NGRAM-SWEEP-controls.tsv`. No target is run; no
`ciphers/<slug>` folder is a known answer, so the prior-work step has no item (stated, not skipped).

## Known answer

MQS-SOLVER's matched design exactly (tools/tests/PREREG-MQS-SOLVER.md): plaintext `zcat
tools/data/fr16/lettresdecatheri02cathuoft_djvu.txt.gz | dd bs=1 skip=1200000 count=40000` (held out), corpus fr16 t.1
+ Marguerite de Valois, `make_marked_control` K=40 letter signs, 1-2 homophones per letter, `--marked 0.3:60`, marked
signs deleted (`--marked-mode skip`), 8 restarts, 40,000 iters, seeds 1-3 (seed sets control instance and solver).
Accuracy = letter tokens right / all letter tokens (MQS-SOLVER's denominator).

**Headroom (rule 3).** At N=800 this design already reads 96.5% blind at order 3 (MQS-SOLVER-controls.tsv base), so
the sweep cannot run there. N rule, fixed now: try N=500 then N=300; use the larger whose base cell (order 3, plain
add-k Model, norm none, uni-weight 1) mean is in [0.20, 0.85]; if neither, N=200; if none qualifies, "no headroom at
these N", every cell still reported, no gain read.

## Cells (3 seeds each)

Orders: o3 (plain Model, the tool default), o3b, o4b, o5b (`--backoff`, BackoffModel; o4/o5 are not run without
backoff: add-k sparsity on a 2 MB corpus, the tool's own docstring). Per order five objectives: `none u1` (default),
`none u0`, `nc2 u1`, `nc2paper u1`, `nc2paper u0` (u = --uni-weight). 20 cells, plus `base_r16` (o3 none u1,
16 restarts: the restarts-alone bar).

Expected before running: o4b/o5b none u1 at or above base (longer context should help most at short N); nc2paper u0 and
nc2 well below base at every order, as at N=800 (6.3% and 12.4%): with log-probabilities below 0, dividing by
sum N_c^2 rewards concentrating letters on few signs, and higher order does not remove that.

## Null (can fail differently, rule 3)

Per cell, the same solver and settings on the same control with the letter-sign sequence's token order permuted
(seeded, seeds 1-3); accuracy read against the gold permuted identically. The statistic is positional letter accuracy
under an n-gram objective, which depends on token order; the permutation destroys the n-gram context while keeping
every sign's count, so the null can read only what sign frequency alone recovers and can differ from the target cell.

## Gates

- **Licence (per cell):** cell mean > null max over its 3 seeds + 0.10. A cell failing it is "no signal" at this N.
- **Gain (per cell vs base):** bar = max(base_r16 mean - base mean, 2 x base SD, 0.03). A cell's gain counts only if
  licence passes, gain > bar, and base mean < 0.95.
- **Shelf:** an order/norm setting with a counted gain is graded `controlled-only` (one synthetic control, no target);
  everything else `weak` with both numbers. Nothing is run on a target from this job; a miss is not re-briefed.
- No amendment after the first accuracy is read except a stated deviation (logged here, dated) for a run that crashes.

## Deviation 1 (9 Oct 2026, 06:52 UTC by date -u; a crash, the only kind allowed above)

N rule result: N=500 base o3 none u1 = 0.9457, 0.9565, 0.9375 (mean 0.9466) -- above 0.85, no headroom. N=300 crashes
in `make_marked_control` for every seed ("40 signs cannot fit 19 letters at most 2 per letter": only 19 letters occur
in 300 tokens of this stretch), so N=200 is infeasible too. No N qualifies: per the rule above, "no headroom at these
N", every cell is still run and reported at N=500 (the largest feasible N tried), and **no gain is read**. The licence
gate against the permuted null is still applied per cell (it can fail differently at any N). All shelf grades `weak`.

## Results (appended 9 Oct 2026, 07:02 UTC by date -u; numbers in tools/tests/MQS-NGRAM-SWEEP-controls.tsv)

Run: `python3 tools/tests/mqs_ngram_sweep.py --n 500 --cells all --out tools/tests/MQS-NGRAM-SWEEP-controls.tsv`
(514 s, 4 processes). N=500, 368 letter tokens, marked share 0.264. Base o3 none u1 0.9466 (SD 0.0078); base_r16
0.9466 (16 restarts add nothing). Bar = max(0.0000, 0.0156, 0.03) = 0.03. **No gain read (Deviation 1).**

| cell | mean | null max | licence (> null max + 0.10) | vs base (not a gain) |
|---|---|---|---|---|
| o3 none u1 (base) | 0.9466 | 0.3288 | PASS | -- |
| o3 none u0 | 0.3415 | 0.0707 | PASS | -0.6051 |
| o3 nc2 u1 | 0.1033 | 0.1332 | FAIL | -0.8433 |
| o3 nc2paper u1 | 0.2563 | 0.2908 | FAIL | -0.6903 |
| o3 nc2paper u0 | 0.0707 | 0.0707 | FAIL | -0.8759 |
| o3b none u1 | 0.9565 | 0.2690 | PASS | +0.0099 |
| o3b none u0 | 0.3034 | 0.0707 | PASS | -0.6432 |
| o3b nc2 u1 | 0.0725 | 0.1332 | FAIL | -0.8741 |
| o3b nc2paper u1 | 0.2346 | 0.2636 | FAIL | -0.7120 |
| o3b nc2paper u0 | 0.0707 | 0.0707 | FAIL | -0.8759 |
| o4b none u1 | 0.9828 | 0.1087 | PASS | +0.0362 |
| o4b none u0 | 0.0707 | 0.0707 | FAIL | -0.8759 |
| o4b nc2 u1 | 0.1286 | 0.0842 | FAIL | -0.8180 |
| o4b nc2paper u1 | 0.3225 | 0.2473 | FAIL | -0.6241 |
| o4b nc2paper u0 | 0.0670 | 0.0707 | FAIL | -0.8796 |
| o5b none u1 | 0.2763 | 0.1440 | PASS | -0.6703 |
| o5b none u0 | 0.0707 | 0.0707 | FAIL | -0.8759 |
| o5b nc2 u1 | 0.0888 | 0.0897 | FAIL | -0.8578 |
| o5b nc2paper u1 | 0.2808 | 0.2174 | FAIL | -0.6658 |
| o5b nc2paper u0 | 0.0670 | 0.0707 | FAIL | -0.8796 |

Against expectation: (1) the paper's score (nc2paper) fails the licence at every order 3-5, with or without the unigram
term; at u0 it reads 0.067-0.071 at every order, identical to its permuted null (the anneal collapses onto one letter,
order-independent), so longer n-grams do not rescue it, the M13 question answered negatively for this solver and
design. (2) o5b none u1 collapses (0.276; restarts disagree) where o4b reads 0.983: at 40,000 iters x 8 restarts the
5-gram backoff landscape is not searched to its optimum at N=500 -- a search-budget limit of this anneal, not evidence
about 5-grams under a better search (the paper used a different, longer annealer). (3) o4b none u1 sits +0.036 over
base, above the 0.03 bar, but base is 0.947, inside the no-headroom band: recorded, not read as a gain.
Shelf: every setting `weak`. Nothing is run on a target from this job and the miss is not re-briefed.
