# PREREG-GAPS205 (account-4, 3 Oct 2026, written 19:03 UTC (clock read) before any statistic below was computed)

Worker GAPS205-pollaky-1865-1875 (account-4). Step: pollaky-1865-1875 gap 3 Verdict, "run catokwacopa-1875's own
cheapest step there (copy ... ads 3-4 text with attribution, Ernst's pair segmentation, pairing permutation test with
a synthetic-line control)". The copy, the segmentation (pairs.tsv, 0/29 mismatches vs Bourdeau's ads.py, i.e. Ernst's
2018 comment-#29 division) and the LENGTH pairing test (S = sum |len a - len b| = 33, 0/100,000, coin/half control
power 0.80/1.00) were already run by NEXT-CAT (account 2, 2 Oct 2026). This step re-runs `pairs.py --check` to
reproduce them, and adds the pairing permutation test on a second, CONTENT axis that the length statistic cannot see.
Credit: line pairs and segmentation are Thomas Ernst's (Cipherbrain, 2018); the length test is David Bourdeau's
(cyphersolver catokwacopa, MIT); the design (order-preserving split of one phrase across the 8 and 20 May ads, with
letters dropped) is the published community reading (Schmeh/Cipherbrain post 8 and comments).

Statistic. For the 24 letter lines of pairs.tsv, M[i][j] = best order-preserving interleave (merge) of 8 May half a_i
with 20 May half b_j, scored as total log10 probability under an English letter bigram model (first letter unigram)
built from tools/data/en pg76_huckfinn.txt + pg64317_gatsby.txt (add-0.5 smoothing). DP state (i, j, last letter from
a or b). T = sum_i M[i][i]. Null: the 20 May halves re-paired at random (20,000 permutations, seed 205);
p = (#{T_perm >= T_obs} + 1)/(N + 1). The number of bigram transitions is fixed (letters - lines) under re-pairing,
so T is not a length statistic.

Controls (rule 3), same 24 total line lengths, same corpus, same synth() as pairs.py (0-3 letters dropped), 20 texts
per arm, 2,000 permutations each:
  P-coin, P-half: true pairs dealt by pairs.py's coin and half dealers (positive controls; power = share with p < 0.001).
  U-half: unpaired -- a_i from one synthetic text, b_i from an independent one (negative control; false-positive rate
  = share with p < 0.05). The controls can differ from the target on T by construction (content changes it).

Gate (decided now):
  - Valid test only if max(P-coin, P-half) power >= 0.5 and U-half FPR <= 0.15. Otherwise: non-test at this N.
  - Valid and target p < 0.001: content-axis pairing supported (independent of S).
  - Valid and target p >= 0.05: content axis does not detect W.'s pairing (control-backed for this statistic only);
    no bearing on any reading.
  - Otherwise inconclusive.
No reading is attempted; nothing is graded (no plaintext tokens, rule 4 n/a).

## Addendum A (19:07 UTC, written after the T run above and before variant T' was computed)

Result of T as registered: target p 0.00045, P-coin/P-half power 1.0/1.0, but U-half FPR 0.75 (> 0.15): **non-test**
by the gate above. Cause: the best-merge score grows with the number of interleavings C(n+m, n), which depends on the
two lengths, so T leaks the length pairing that S already measures. One variant, registered now, one run only:
T' = sum_i (M[i][i] - E[len a_i][len b_i]), where E[n][m] is the mean merge score of 40 pairs of independent corpus
halves (pairs.synth 'half' dealer on two independent phrases) of lengths n and m (seed 2050). Same null, same three
control arms (the control strings get E from the same table, extended to their lengths), same gate and verdict words.
If T' also fails its gate, the content axis is logged untestable-by-this-instrument at N = 24 lines; no third variant.
