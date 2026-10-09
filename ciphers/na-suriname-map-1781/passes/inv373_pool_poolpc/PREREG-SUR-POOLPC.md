# PREREG SUR-POOLPC (9 Oct 2026, 04:3x UTC by date -u; pushed BEFORE any synthetic draw or real pooled SPLIT score; poolpc.py pushed with it, unchanged after)
LANE FAMILY-A2f (account 2), job SUR-POOLPC. Question (SUR-SPLITPC's next): at the pooled N of the three held-out units (0744 L, 0744 R,
0745 L), does score.py (b)'s SPLIT statistic have the power (detection >= 0.80) to read LEANS n when the y-family carries n only? CPU only.

## Step 1 (counted before this file, `poolpc.py --selftest`, no SPLIT verdict computed)
Real y-family tokens DP-aligned to gloss m|n (0745 L score.py load()/stats() unchanged, one loader for all three units; 0744 L's own loader
differs only in also reading `ÿ` as y-family):
pass A: 0744 L 21 lines m 15 n 40; 0744 R 22 lines m 18 n 58; 0745 L 22 lines m 15 n 38 -> pooled 65 lines, m 48 n 136 (184 tokens)
pass B: 0744 L 21 lines m 14 n 38; 0744 R 22 lines m 19 n 62; 0745 L 22 lines m 14 n 39 -> pooled 65 lines, m 47 n 139 (186 tokens)
(0745 L alone: about 53; pooled is about 3.5x.)

## Design (poolpc.py)
- SUR-SPLITPC's scaffold unchanged in logic, built per pass from the 65 pooled lines: gloss lines bootstrapped; per-letter facing
  distributions from the real steered DP alignment; real deletion (A 0.090, B 0.090) and insertion (A 0.108, B 0.110) rates.
- H1 planted full split (every m drawn as [y-fam] is written `Mx`, not in T; S_true = 1.0); H0 real facing distributions.
- Statistic and verdict rule exactly score.py (b) / splitpc.py: S = n/(m+n), K = 300 deranged-gloss C1 draws per synthetic unit,
  LEANS n iff S > p99.5, non-test iff m+n < 10, < K/2 usable draws, or p0.5 == p99.5. Master seed 20261010.
- Exact speed-up: per-line (m, n) counts are computed once for every (cipher line, gloss line) pair and each derangement is a sum over that
  matrix; `--selftest` asserts equality with score.py's stats() on 5 deranged draws (passed before this file).
- Ladder: synthetic units of 22 lines (0745 L's size), 44 lines and 65 lines (the pooled N); 200 H1 units per pass scaffold at each;
  H0 50 units per scaffold at 65 lines (false-LEANS rate, reported not gated).

## Gate
**Detection (share of the 200 H1 units at 65 lines reading LEANS n) >= 0.80 on both scaffolds -> PASS**; then, and only then,
`poolpc.py --real` scores the real pooled units (pass A and pass B, each 65 lines) with 10,000 deranged-gloss C1 draws (seed 20261010),
same verdict rule, unit verdict needs both passes to agree. **< 0.80 on either -> FAIL**: no real pooled SPLIT is run; report the line
count (and m|n token count) at which detection would reach 0.80, extrapolated from the 3 ladder points (linear fit of detection on log N
lines, per scaffold, stated as an extrapolation) and stop.
Stated limits: only the full split is planted; the facing distributions come from the steered aligner (the control inherits the steer as
the target does); a 300-draw p99.5 is noisier than 10,000; the 22-line point re-estimates SUR-SPLITPC's 0.570/0.510 on the pooled scaffold
(not the same scaffold, so not a reproduction).

## Consequences
Whatever the result: no edit to key.tsv, key_period_*.tsv, conflicts.tsv, any transcription file, token grade, any earlier score.out, or
N-class. HYPOTHESES.md row with both numbers, NOTES section "SUR-POOLPC (9 Oct 2026)", gaps_check. Rule 10: report only.
