# R11-SURY pre-registration (6 Oct 2026, written before any tile is scored)

Question: do the 21 [y-fam] tokens of NA 1.05.03 inv. 373 scans 0692-0693 (align_words.tsv, R10-SUR693) split by a visible
feature into the gloss's m (12 positions) and n (9 positions)? Key reference: key_period_nieuw.tsv / the Nieuw sheet gives
M = y and N = dotted ij.

Features (scored per token, on anonymised tiles of the cipher line only, gloss line excluded, tile order shuffled, seed 1781):
- F1 (primary): two dots (or a diaeresis-like mark) above the sign: dotted / undotted / unreadable.
- F2 (secondary): two-part "ij" form (separate short i-stroke before the descender stroke) vs one-part "y": ij / y / unreadable.
Prediction from the sheet: F1 dotted -> n, undotted -> m; F2 ij -> n, y -> m.

Statistic: agreement = share of readable tokens whose feature-predicted letter equals the gloss letter.
Control: the 21 gloss labels permuted over the tokens, 10,000x, seed 1781; agreement recomputed on the same readable set.
This control can vary on the statistic (it changes which token carries which label; the feature reads are fixed).
Majority-class floor reported beside it (12/21 m), and a per-class breakdown (m-tokens dotted share, n-tokens dotted share).
Gate: PASS = agreement > control p99 AND at least 15 of 21 tokens readable on that feature. Otherwise: no split at this
resolution (not a negative on the key; the y = d question stays M).
Consequence for the map key's y = d (M): a PASS on F1 or F2 bears on which form the map readers' y is; it is recorded as a
witness (rule 4), never applied by majority. A FAIL leaves y = d at M.
Reader: this worker's own eye on anonymised tiles (no subagent, cap 3). Caveat stated in advance: the reader has seen the
crops in R10's notes; the anonymised shuffled tiles are the blinding.
