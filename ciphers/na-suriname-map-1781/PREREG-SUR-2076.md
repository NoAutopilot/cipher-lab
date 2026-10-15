# PREREG SUR-2076 (15 Oct 2026, account 2, Opus worker for LANE DEFAULT-A2-1109-15)

Written and pushed before any score; only `align_2077_crib2076.py --dry` (entry segmentation, no alignment) has run.

**Question.** Does 4.VEL 2076's plain-Dutch title and legend A-S (same fort Zeelandia, Juny 1780/81, plain script), used as known
plaintext, pin any U/M token of 4.VEL 2077's cipher title + Explicatie legend -- in particular the five [d-hook] tokens
(L01:22, L02:17, L06:35, L14:40 U/M; L13:3 C e from GAPS23)?

**Crib.** `crib_2076_legend.tsv`: read by this worker by eye from `images/2076_overview.jpg` (2500 px, on disk; disk-only job, no native
fetch). One reader; words not read with confidence are omitted (fragment boundary). Folding both sides: lower case, diacritics off,
ij/ei -> y, non-letters dropped.

**Instrument** (`align_2077_crib2076.py`, a different instrument from the retired nl18-vocabulary anchor test). 2077 is cut into its
title block and legend entries at the plain entry markers ({a}, {b}, ... {z.}, Greek). Cipher tokens H/C known; U and M (and two-valued)
are wildcards; plain words on 2077 enter as known letters. Each 2077 entry is aligned (Smith-Waterman, match +2, mismatch -3, gap -3,
wildcard 0) against every 2076 entry; the best crib entry is kept if unique and the pair is ACCEPTED when known matches >= 6, identity
>= 0.85 and gaps <= 1 (fixed, not tuned). A wildcard aligned inside an accepted pair is pinned to the crib letter.

**Controls.**
1. Known-H (must pass): leave-one-out over every H cipher token: mask it, re-align, compare the pin (if any) to the H value. Gate: >= 10
   pins and precision >= 0.90.
2. Letter-shuffled crib (must fail): each 2076 entry's letters permuted (20 seeds), full procedure rerun. Gate: mean accepted pairs <= 1.0
   and mean correct leave-one-out pins <= 0.2 x the real count. (The shuffle changes letter order, which the alignment score depends on,
   so this control can differ from the target.)

**Decision.** Instrument VALID only if both gates pass; otherwise non-test, no pin used. If VALID: a pin is reported; a [d-hook] pin (or any
other U/M pin) becomes C only where the crib's own word gives the letter in an accepted pair; key edits only through the folder's key
path (exceptions_nieuw_image.tsv) with `tools/decode_key.py ciphers/na-suriname-map-1781 --check`. No pin -> "2076 does not reach that
entry", recorded as coverage, not a negative on the value. No changes to thresholds after the run.
