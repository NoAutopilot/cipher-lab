# PREREG-FAIR-CRED: full-credit-text marker schemes, fair-game-2010 (14 Oct 2026, FAIR-CRED, account 4)

Written and pushed before any target score is computed. Instrument: `ciphers/fair-game-2010/cred/cred_sweep.py` (our own
code; imports D2-FAIR's `marker/marker_sweep.py` judge, sequence variants, Pride windows and word pool unchanged). Idea
for "first letter of the next name" cited from aaymeloglu/unsolved-ciphers SHORTLIST.md (no licence, nothing copied).

## Data
`cred/credit_lines.tsv`: the credit row carrying each mark (the cell holding the mark: role column, name column, or a
single-column row) and the next fully visible row, from two blind passes on line crops of Rossignol's 25 screenshots
(pass A worker, pass B Sonnet subagent; 65 strips, 67 marks; reconciled by `cred/reconcile_credits.py`: text identical,
one marked-cell split settled by GF4-BATCH22's colour blob). Row 4 (hidden) dropped. Mark position in the cell from
D2-FAIR's word index; second HAIR for idx 11 (read from the crop). Apostrophes, hyphens and full stops join words.

## Schemes (fixed list)
Per mark: C1 first letter of the next credit (next row's name, else its role); C2 first letter of the marked cell;
C3 letter after the mark in the cell, crossing word boundaries; C4 letter before, same; C5 first letter of the other
column of the same row; C6 first letter of the next row's role; C7 first letter of the word after the marked word in
the cell; C8 initial of the cell's last word; C9 last letter of the cell; C10 the letter at the same position in the
next row's same column. A mark with no letter under a scheme is dropped (lengths: C1 59, C2 67, C3 66, C4 63, C5 44,
C6 40, C7 30, C8 67, C9 67, C10 51). Sequence variants (reverse, decimation n=2..L-1, two-line interleave) on C1 and
C3. Both credit-block orders (scroll = spec, column = Schmeh 2026).
Not run: "capitals" as a case signal (3 of 67 marks are lower case: s, u, w; too few to carry a 67-letter message,
nothing to plant); logged only.

## Judge and gates (as PREREG-D2-FAIR, unchanged)
Language PASS = score > null_p99 and > real_p05 (en, 200 controls per N), words PASS = cover >= 0.6, no length check.
Control: for each of C1-C10 and C1+reverse, C1+interleave, C3+decim2, 5 trials planting different 67-letter
Pride-and-Prejudice windows (seed 20261014) into decoy records built from random pool words; the full sweep runs on
each decoy. G1: recovered >= 4/5 per scheme; a scheme below G1 is a non-test for the target. Null: 20 order shuffles of
the target's records + 20 random-record decoys; G2: family-wise false-pass rate <= 0.10, else the target is not run.
Target verdict: a PASS under a G1 scheme with G2 met is "worth a verifier" (never "right"); none = control-backed
negative for these schemes at N<=67, both orders. No tuning after the target is scored. en corpus caveat (EN-FOLDS).
