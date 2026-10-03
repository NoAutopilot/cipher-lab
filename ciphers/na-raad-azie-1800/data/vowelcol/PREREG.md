# A2-RAA8 vowel-column order test -- pre-registration (3 Oct 2026, pushed before any scoring)

Hypothesis Hv: the bottom digit (1-4) of each leaf-2 cell is the vowel column of a grid table, so the bottom-digit
sequence of the 370 cells (data/masc/cells_370.txt; the one "?2" cell keeps bottom 2) is the Dutch vowel sequence
over {e,i,a,o} under some bijection.

Statistic G (order-dependent, frequency-free): for each of the 24 bijections bottom->{e,i,a,o}, the per-token
log-likelihood of the sequence under a vowel-bigram model minus its log-likelihood under the matching vowel-unigram
model; G = the maximum over the 24 bijections. Model: vowel sequence of tools/data/nl20 (fold as
tools/judge_plaintext.py; 'ij' and 'y' -> i; u and consonants dropped), add-0.5 smoothing; the windows used as
controls are cut from one file (pg10820) that is held out of the model.

Null per sequence: 200 order permutations of that same sequence (counts fixed; G depends only on order, so a
permuted sequence can score differently from the original -- the control can differ). p = (1 + #perm G >= real G)/201.

Controls (scored before the target, same N=370, same G, same 200 permutations each):
- POS: 20 held-out nl20 windows, bottom = vowel index of the first 370 vowels of the window (Hv true by construction).
- ALT: 20 synthetic one-cell-per-letter ciphers: 370 nl20 letters, a random one-to-one map of the 24 commonest
  letters onto the 28 cells of the 7x4 table (others onto the remaining cells), bottom = the cell's column (Hv false).

Gate: POS must give p < 0.05 in >= 16/20 (power >= 0.8); otherwise the test is a non-test at N=370 and the target is
not scored as a result. ALT reports how often a non-vowel layout also passes (false-positive rate of the design).

Target verdicts:
- "consistent with Hv": target p < 0.05 AND target G within POS [min,max] AND target G above ALT's 90th percentile.
- "against Hv": gate met AND target p >= 0.05.
- otherwise "cannot decide" (e.g. target p < 0.05 but ALT also passes / G in the ALT range).
Seed 20261003. No reading is produced either way.
