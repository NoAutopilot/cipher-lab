# R9-HUNT context-fill pre-registration (written 6 Oct 2026 06:16 UTC by date -u, before any fill or control was run)

Worker R9-HUNT (LANE LANE-RUN9-account-1). Nothing below has been computed yet; the script does not exist at push time.

## Method (fill/context_fill.py, deterministic, no model in the loop)
- Key without the blanked code (leave-one-code-out). The key is a one-part code (values rise roughly alphabetically with the
  code: 298 of 387 adjacent key pairs in order, measured before this file).
- Bracket: the 3 nearest keyed codes below and the 3 above; lower bound = median (sorted) of the lower three values, upper bound
  = median of the upper three (accents stripped, lower case). Candidates = fr18 corpus word types (count >= 3) plus every key
  value, inside [lower, upper]. If fewer than 5 candidates, widen to the 2nd-lowest/2nd-highest of the six.
- Score = log P(candidate + right context | left context) under a character 6-gram model (interpolated, add-0.1) trained on
  tools/data/fr18 with spaces and accents removed; context = key values of up to 15 characters each side, stopping at an
  unkeyed or blanked token. Prediction = argmax; margin = top1 - top2 score.
- Correct = prediction equals the column's own gloss (accents stripped, apostrophes removed).

## Control (BLA185, the brief's named control)
- Every BLA185 column with conf H, a gloss, and a code that is in key.tsv (leave-one-code-out: that code removed from the key
  and from the context wherever it occurs). In addition 11% of the other columns of BLA185 are blanked at random (the target's
  own unkeyed share, 18 of 165 BLA186/191 tokens), seeds 1, 2, 3.
- Shuffled-context control (can differ: the score depends on context): same columns, but the left/right context taken from a
  random other BLA185 position, seeds 1, 2, 3.

## Gate (both must hold, means over the 3 seeds)
1. Control top-1 recovery >= 0.40.
2. Control minus shuffled-context recovery >= 0.10.

## Grading if the gate passes
- t* = smallest margin such that control precision (pooled over the 3 seeds) among columns with margin >= t* is >= 0.70 on
  >= 15 columns. Target fills with margin >= t* are graded S; the rest M. If no t* exists, every fill is M.
## If the gate fails
- No fill enters reading_tokens.tsv; the 18 groups stay U. The candidate lists go to fill/ as ungraded output only.
