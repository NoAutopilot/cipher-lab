# PREREG-D2-FAIR: marker-scheme sweep, fair-game-2010 (8 Oct 2026, D2-FAIR, account 2)

Written and pushed before any target score is computed. Instrument: `ciphers/fair-game-2010/marker/marker_sweep.py`
(our own code). The marker-scheme idea is cited from aaymeloglu/unsolved-ciphers SHORTLIST.md ("Enumerate marker
schemes (next letter, previous letter, first letter of next name, offsets) and check for an English sentence"); no code
copied (no licence).

## Data
`reconcile_2026-10-03.tsv` (GF4-BATCH22, image-checked): 67 visible marked letters with the credit word each sits in.
Row 4 (redacted surname) dropped. Index of the marked letter inside its word: taken from Mulliss's capitalised
transcription (`specs/cheap-tests/fair-game-2010/credits_words.py`) when his word is the same word; otherwise the unique
occurrence of the letter in the word; if the letter occurs more than once and Mulliss does not settle it, the first
occurrence, counted and reported as "ambiguous index". Both credit-block orders: scroll (spec/ATS) and column (Schmeh 2026).

## Schemes (fixed list)
Per-mark schemes, both orders:
- S0 marked letter itself; S1 next letter in the word (Halpin); S2 previous letter; S3 +2; S4 -2;
- S5 first letter of the marked word; S6 last letter of the marked word;
- S7 index of the mark in its word as A1Z26; S8 index from the word's end as A1Z26; S9 word length as A1Z26.
  (A mark at a word edge with no letter at the offset yields nothing for that mark: dropped, count reported.)
Sequence schemes on S0 and on S1, both orders: S10 reversed; S11 decimation, every n-th letter cyclically, n = 2..L-1
(start 0); S12 the two credit lines interleaved (line1[i] line2[i]).
Not testable from disk: "first letter of the next credit name" and "letters after a marker sign" outside the marked
word, and "capitals" (the full credit text is not on disk, only the marked word per mark); logged as not run.

## Judge and score
`tools/judge_plaintext.py specs/fair-game-2010.json` logic in-process (en corpus, 200 controls per N, language PASS =
score > null_p99 and > real_p05, words PASS = cover >= 0.6), without the 65-69 length check (schemes that drop edge
marks are shorter). A candidate PASSes when language and words both pass. The best candidate per sweep is the highest
language score. The CLI is re-run on the target's top 3 and pasted into NOTES.md. en corpus caveat (EN-FOLDS): a
PASS/FAIL against en is of unknown reliability.

## Controls
(a) Planted-message control, N=67: for every plantable scheme (S0-S6 per-mark; S10-S12 sequence on S0), 5 trials, each
plants a different 67-letter window of real English from `tools/data/en/pg1342_pride.txt` (not a judge-corpus file) in a
decoy of the same length: per mark a random word from the credit-word pool plus Pride-and-Prejudice words (3-12 letters,
upper case) and a mark index chosen so the scheme yields the planted letter; sequence schemes plant the inverse
permutation. The full sweep runs on each decoy. Recovery = the planted scheme PASSes. S7-S9 (A1Z26 on word positions /
lengths) cannot produce letters past the longest word's length; they are reported as non-plantable, and the target's
values are reported directly (if every value is <= 15 the scheme spells only A-O).
(b) Null, family-wise false-pass rate: 20 sweeps on the target's own (word, index) rows shuffled in order (seeds 1-20),
and 20 sweeps on random-mark decoys (random pool word, random index; seeds 101-120). False-pass = any candidate in the
sweep PASSes.

## Gates (fixed now)
G1 control: planted recovery >= 0.8 (4 of 5) for a scheme; a scheme below G1 is a non-test, not a negative.
G2 null: family-wise false-pass rate over the 40 null sweeps <= 0.10; above that, a target PASS licenses nothing.
Target verdict: a target candidate that PASSes under a scheme meeting G1, with G2 met, is "worth a verifier" (rule 7/10,
never "right"). No PASS under any G1 scheme with G2 met = control-backed negative for those schemes at N=67, both orders.
No tuning after the target is scored.
