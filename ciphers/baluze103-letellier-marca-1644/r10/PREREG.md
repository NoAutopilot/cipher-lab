# PREREG -- R10-BAL103C, 9 shape split (g-tail vs short), 6 Oct 2026

Written 6 Oct 2026 by worker R10-BAL103C (LANE LANE-RUN10-account-1) before any 9 crop was cut or read on this job.

- Shape classes: G = 9 with a long looped g-like descender; S = short 9 (body on the line, no long tail). Defined on the f.171r
  control 9s (calib/, values known from the f.172r period decipherment), then applied to the 42 f.50 i|r|s tokens only if the gate passes.
- Statistic: accuracy of the best map {G,S} -> {i, r|s} on the control 9s. Null: label permutation over the same control tokens
  (shape classes fixed), exact enumeration. Gate: observed accuracy > null p95. Fail or untestable -> NON-TEST, key.tsv and
  exceptions.tsv untouched.
- Power check first (r10/power9.py, before any shape read): the control on disk is calib/sign_table.tsv's 9 row, N = 3 aligned
  occurrences, values s, s, i (k = 1 of value i). With 3 label arrangements, a perfect split reaches 1.000 and the null p95 is also
  1.000 (P(null >= obs) = 0.333). The gate cannot pass at N = 3 whatever the shapes are, so the shape read is not run.
- Smallest passable control: N = 7 with at least 2 i-valued 9s (null p95 0.714, P = 0.048); r10/power9.tsv lists the rest.

## Addendum -- R10-BAL103D, 6 Oct 2026 10:12 UTC (by date -u), written before the f.171r L12-L18 pass was read

The gate above is unchanged. This fixes only what counts as a "known" control 9, which PREREG left to calib/'s rule.
Disclosure: written after the L05-L11 pass had been aligned (r10/nines.tsv, first version) and before the L12-L18 pass.
- Alignment: r10/enlarge9.py (calib.py's unit-cost semi-global DP), all f.171r blind passes in page order against
  r10/f172r_decipherment_ext.txt; clear words in [brackets] enter as their letters.
- **Primary (strict) known 9:** aligned decipherment letter in {i, r, s} AND the two letters on each side of the 9 match the
  decipherment contiguously (column `known` = yes). Value classes for the gate: i vs r|s.
- Secondary (calib's loose rule, descriptive only): aligned letter in {i, r, s}, neighbours ignored.
- If the strict set reaches N >= 7 with >= 2 of value i (r10/power9.tsv "perfect_can_pass" = yes), the shape read runs: one blind
  subagent call given a crop around each control 9 (no values), classifying G (long looped g-like descender) vs S (short); then
  the exact label-permutation test as registered. Otherwise NON-TEST at the enlarged N, stop.
