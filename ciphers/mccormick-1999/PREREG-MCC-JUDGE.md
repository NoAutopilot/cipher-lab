# PREREG-MCC-JUDGE (15 Oct 2026, 08:2x UTC by date -u; pushed before any null draw or judge score)

Worker MCC-JUDGE (account 1, LANE DEFAULT-A1-0740-15). Follow-ups named by MCC-SUFX (NOTES.md "MCC-SUFX", PREREG-MCC-SUFX.md,
commit 335740320): (1) tools/judge_plaintext.py on the MCC-SUFX decode; (2) a null that also keeps NCBE's stem, to size how much of
the target's margin over the type-mark null is the single type NCBE. Script: `ciphers/mccormick-1999/families/judge/ncbe_null.py`
(selftest OK before this file). MCC-SUFX's instrument is reused unchanged (token_anneal.fit_marks, pool 3,000, alpha 3.0, beam 200).

## Null (fixed now)
- `ncbe`: MCC-SUFX's type-mark null (letters of the 99 distinct code types permuted across types, each type keeps its length and
  final mark SE/BE/E, repeats stay repeats), with every NCBE span held in place as well: NCBE x11 and the 7 NCBE spans inside
  run-on types (18 spans, 72 of the 750 code letters) are never moved; the rest are permuted. Map re-fitted on every draw.
  200 draws, rng seeds 7000-7199.
- `tm`: MCC-SUFX's own type-mark null re-run at 200 draws (seeds 8000-8199) on the same machine, for the share figure only.
- The target is re-fitted in the same run; if its coverage or score per letter differs from MCC-SUFX's (0.497, -2.940) by more
  than 0.001, stop and report a reproducibility failure, no null read.
- Can the null differ from the target on the statistic? Yes: coverage and score per letter depend on which stem strings exist,
  and the shuffle changes every non-NCBE, non-mark letter (678 of 750).

## Margin rule (fixed now)
Statistics: coverage (C) and LM score per code letter (S). p = (1 + draws >= target) / 201 per statistic against `ncbe`.
- C and S both above the `ncbe` maximum -> "with NCBE held fixed, the rest of the target's stems still fit beyond a shuffle:
  the MCC-SUFX margin is not carried by NCBE alone".
- p >= 0.05 on both -> "the MCC-SUFX margin over the type-mark null is carried by the single type NCBE: with it held fixed the
  remaining stems do not fit beyond a shuffle" (a control-backed negative for the non-NCBE stems under this scheme only).
- anything else -> "mixed", no stronger wording.
- Share of the margin carried by NCBE, per statistic: s = (mean_ncbe - mean_tm) / (target - mean_tm), reported as a number.

## Judge (fixed now)
`python3 tools/judge_plaintext.py specs/mccormick-1999.json --file F` (spec judge block: letters 700-800, language en,
min_word_cover 0.6). Renderings of the decode: A = read words as words, unread segments as their own code letters (lower case),
numbers dropped (all 750 code letters represented); B = read words only. Shuffled controls (rule 3, ARM-C1): the same two
renderings of the decode of draw 7000 (`ncbe`) and draw 8000 (`tm`). A PASS on either control voids the judge as a gate for
this family at this N. The `en` corpus has a leave-one-file-out spread of 0.44-0.64 (tools/data/en/README.md): any PASS or FAIL
is of unknown reliability, and is reported as such. Expected (stated before running): A FAILs (half its letters are unread
consonant strings); B fails length (about 370 letters < 700).
The target stays `open` (rule 5) whatever the outcome; no part of the decode is offered as a reading.
