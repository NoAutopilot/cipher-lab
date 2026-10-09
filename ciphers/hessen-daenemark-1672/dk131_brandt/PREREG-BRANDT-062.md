# PREREG-BRANDT-062 (9 Oct 2026, written 03:3x UTC by date -u, before any decode or score below is computed)

Target: Friedrich von Brandt to Hedwig Sophie, HStAM 4 f Staaten D Dänemark 131. Job BRANDT-062, LANE FAMILY-A2e (account 2).

## What the leaves hold (eye check at 1/4 and native, before this file)
- 0062 right page: the cipher block of the letter dated "Koppenhagen den 3. Aug. 1672" (signature Friedrich von Brandt): 6 numeral
  lines with a small interlinear gloss in a second hand above most groups (letters over groups, and words such as "zehen", "verehrt").
  So 0062 is a GLOSSED leaf: its tokens are known-answer, scored as BRANDT-UP did.
- 0063 and 0064 left page, and 0050's slip head: mirror-image show-through (the writing reads reversed): 0063/0064 of 0062's cipher
  block, 0050 of 0049's slip (the "on138" mark and the 0049 slip groups visible reversed). Not cipher writing on those leaves.
  So there are no UNGLOSSED cipher tokens on 0062-0064/0050 to decode, and the brief's unglossed statistic has no data.

## Known-answer test (identical design to PREREG-BRANDT-UP.md)
Frozen key: `values_gate.tsv` rows with grade C (16 values), unchanged. Data: `ciphertext_0062.tsv`, reconciled from two blind Sonnet
passes with tools/reconcile_passes.py, splits settled from the image; gloss column = the gloss over each group ("^" = continuation of the
word above the previous group). Gloss normalisation as BRANDT-UP: lowercase, ä->ae ö->oe ü->ue ß->ss, a-z only, [?] dropped.
Statistic (primary, the gate): per cipher line, LCS between the C-letter sequence of that line's groups (non-C groups removed) and the
concatenated gloss letters of that line; summed over the 6 lines.
Control: uniform random permutation of the letters among the 16 C values, n = 2000, seed 20261009. The control can differ from the target
(re-assigned letters change the C sequence matched against the fixed gloss; nothing in the statistic is invariant under it -- rule 3).
Gate: PASS if real > control p99 AND p = (1 + #{control >= real}) / 2001 < 0.01. Non-test if fewer than 10 C-value tokens.
Secondary (reported, not a gate): per-token agrees -- C tokens whose gloss field is a single letter equal to the C letter.

## What each outcome licenses
- PASS: glossed C-value tokens LCS-matched to their line's gloss grade C; other glossed tokens M (gloss recorded as an M observation);
  unglossed tokens decoded by a C value grade M (no unglossed gate here: fewer than 30 such tokens expected, too few for a de17 test).
- FAIL / non-test: no grade C from this leaf; all tokens M. values_gate.tsv unchanged either way.
Script: `score_062.py` (committed with this file; reads only values_gate.tsv and ciphertext_0062.tsv).
