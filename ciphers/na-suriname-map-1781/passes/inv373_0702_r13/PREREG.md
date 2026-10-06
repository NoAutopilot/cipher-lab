# PREREG R13-SUR702 (6 Oct 2026, ~13:45 UTC by date -u; committed and pushed BEFORE the blind pass is read or score.py is run)
Material: NA 1.05.03 inv. 373 scan 0702 (IIIF 167f4f68-...0294.jp2, native 4904x4017), two pages of cipher lines each with a lighter
interlinear plain Dutch line above (R13-SURSWP4's hit). 42 gloss+cipher pair crops (left page 22, right page 20), cut by
tools/iiif_lines.py (crops/manifest.tsv). Crops not committed (folder over 30 MB); regenerate with the commands in crops/manifest.tsv.
Question: does 0702's cipher use the same sign system as the map key / the 0692-0693 Texier letter?
Reader: ONE blind Sonnet pass per page (crop paths only; reader-code vocabulary given, NO values, NO key) -> passA_sonnet_blind.tsv.
The worker then reconciles the GLOSS text only (spelling as written) with the image in view -> gloss_reconciled.tsv. The worker
does NOT alter the blind cipher tokens used for the primary statistic (any eye corrections to cipher tokens go to a separate
column and are reported as a secondary figure only).
Positions: per pair, cipher words = the blind pass's tokens split on '|' (or spaces between groups as the reader marked them);
punctuation and plain numerals (-12-, 24) dropped; gloss words = reconciled gloss split on spaces, punctuation dropped. If a pair
has the same number of cipher and gloss words they are paired in order; otherwise the pair is skipped. A word pair is used only
when its sign count equals its letter count (gloss 'ij' counted as one letter). '?' tokens are skipped as positions.
Statistic S1: share of positions whose blind code is keyed in key_period_codes_nieuw.tsv at which the key value equals the gloss
letter (classes i=j=y=ij, u=v; 'a|b' agrees if either). Blind-code aliases normalised only by: [ij]/y-with-dots/ÿ -> [y-fam]
(counts as agreeing with m or n, the 0693 sign table's values; reported separately), [lambda] -> λ, [d-loop] -> [ezh-dot].
Statistic S2: same positions, agreement with the 0693 sign table (passes/inv373_0693_r10/sign_table.tsv: a code agrees if the
gloss letter is among that code's letters_seen).
Control (can vary on both statistics): gloss letters permuted across all used positions, 1,000 permutations, seed 702.
Gate: SAME SYSTEM if S1 >= 0.60 AND S1 > control p99. Otherwise 'not shown'. S2 descriptive, reported with its control too.
Per-code table descriptive; conflicts with an H/C key value seen >= 2 times go to conflicts.tsv as a rule-4 data row (no key edit).
No key.tsv / key_period_codes_nieuw.tsv edit in this job; candidate values go to candidates_0702.tsv for a verifier.
