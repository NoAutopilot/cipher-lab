# A2-RAA10 stronger bottom-digit statistics -- pre-registration (3 Oct 2026, pushed before any scoring)

Hypothesis H_rv (row x vowel-column table): each leaf-2 cell (data/masc/cells_370.txt) is top = row, bottom = vowel
column over {e,i,a,o}; the row carries the consonant written before that vowel. A2-RAA8's vowel-bigram G was a
non-test (POS 9/20 at N=370). Two stronger, order-dependent statistics, each label-free or maximised over labels:

- **T (trigram):** max over the 24 bijections bottom->{e,i,a,o} of per-token [log P(V_i | V_{i-2}, V_{i-1}) - log P(V_i)],
  vowel trigram model from tools/data/nl20 with pg10820 held out (same vowel fold as A2-RAA8: ij, y -> i; u dropped),
  add-0.5 smoothing. Bottom digit only.
- **X (cross-cell, bottom conditioned on top):** plug-in mutual information I(b_{i-1}; t_i) + I(b_{i-1}; b_i) over the
  sequence (previous cell's vowel column predicting the next cell's row and column). Label-free (invariant to any
  relabelling of rows or columns), uses both digits.

Null per sequence: 200 permutations of whole cells (each (top,bottom) pair kept, counts of both digits fixed), so both
statistics can differ only through order -- the control can differ from the target on each statistic.
p = (1 + #perm >= real)/201.

Controls at N=370, scored before the target (seed 20261003, fresh starts):
- POS (H_rv true by construction): 20 held-out pg10820 windows; for each of the first 370 vowels (as above), bottom =
  vowel index, top = row of the nearest preceding consonant in the same word under a random partition of the
  consonants into 6 rows (row 7 = no preceding consonant in the word); partition redrawn per window.
- ALT (H_rv false): 20 one-cell-per-letter ciphers on a random 7x4 table, exactly as A2-RAA8.

**Power gate (lane brief): a statistic is used on the target only if its POS gives p < 0.05 in >= 18/20.** If neither
reaches 18/20: non-test at N=370, the target is not scored as a result, and the bottom-digit and cell-substitution gaps
become too-short for this item (A2-RAA9: N cannot rise from invnr 209). If both pass, the target p is Bonferroni x2.
Target verdicts (per passing statistic): "consistent with H_rv" = target p < 0.05 AND target statistic within POS
[min,max] AND above ALT p90; "against H_rv" = target p >= 0.05; otherwise "cannot decide". ALT pass rate is reported
as the design's false-positive rate. No reading is produced either way.
