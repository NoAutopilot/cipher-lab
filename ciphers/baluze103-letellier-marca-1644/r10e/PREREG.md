# PREREG -- R10-BAL103E: fr17 test of "9 = s everywhere" on f.50, written and pushed before any r10e score is computed

Worker R10-BAL103E (account 1, LANE LANE-RUN10-account-1), 6 Oct 2026, written ~10:31 UTC by `date -u`.

Disclosure (on file before this PREREG): R9-BAL103 already judged an "all-s" variant of f.50 at fr17 -1.487 against the committed
(R9 context rule) -1.445 (r9/judge_v_alls.txt, r9/judge_v_rule.txt). So clause G1 below is expected to FAIL from that number; this
run cannot hide that. The committed rule chose each 9's letter with the same fr17 4-grams the judge scores with, so "all-s vs
committed" is biased toward the committed decode by construction. The controls below exist to say whether s at the 9 positions is
distinguishable from s (or any letter) placed at random, which the R9 numbers do not say.

Input: reading_tokens.tsv as committed; letters = first value of each token, U and '?' dropped (tx/r7b/judge_input.py's rule).
The 42 tokens whose value set is {i, r, s} are the "9 positions" (their committed first value is the R9 lean).
Model: tools/judge_plaintext.py NgramModel over the spec's fr17 corpora (all of fr17, as the judge uses); statistic S = model.score
of the whole folded letter string (the judge's own score). Seed 1644, 2,000 draws per null.

Variants scored: committed; all-s; all-i; all-r (every 9 position set to that letter).
Statistic D_v = S(variant) - S(committed), for v in {s, i, r}. Changed positions = the 9 positions whose committed letter != v (m_v).
Control 1 (random positions, varies on position/context -- the axis under test): m_v positions drawn uniformly from the
  non-9 letter positions whose committed letter != v, set to v; D_null1 = S - S(committed). It can differ from D_v because the
  statistic is context-dependent.
Control 2 (shuffled value at the 9 positions): each of the m_v changed 9 positions gets a letter drawn from f.50's own committed
  letter frequencies (excluding the 9 positions); D_null2 = S - S(committed). It varies on value, the other axis.

Gate for a key/exceptions change ("9 = s" replaces the R9 lean as first value of the 42): G1 D_s >= 0 AND G2 D_s > p95 of
  D_null1(s) AND G3 D_s > p95 of D_null2(s). All three or no change. (G1 is expected to fail; see disclosure.)
Descriptive, registered here, licensing nothing on f.50: percentile of D_v in each null for v in s, i, r; which constant
  has the highest percentile against Control 1. A D_s at or above D_null1's p95 while G1 fails would say s fits the 9 positions
  better than s fits random positions, but not better than the R9 lean.
Either way: decode_key --check; key.tsv and exceptions.tsv untouched unless G1-G3 all pass.
