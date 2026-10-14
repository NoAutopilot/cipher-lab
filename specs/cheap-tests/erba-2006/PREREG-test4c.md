# PREREG test 4c -- erba-2006 (ERBA-CASE, LANE DEFAULT-A2-2209-14, account 2; written 14 Oct 2026 ~23:22 UTC, before any score)

A different design on test 4b's instrument, per NOTES.md "## Next step (ERBA-SIB, 14 Oct 2026)": case-sensitive letter classes.
Not a third attempt at the case-folded design (test 4 / 4b).

- Ciphertext: identical to test 4b (`transcription_bERB.txt` 22 lines + `ciphers/erba-2006/ciphertext_siblings_2013.txt`, press
  transcription only, rule 2): 21 words / 120 letters on xs = word space, lengths [2,7,6,10,1,12,11,11,8,9,4,3,1,6,3,2,4,5,6,2,7].
- Design: xs = word space; every case-kept token type is its own letter class: cu, Cu, mi, Mi, fi, Fi, un, Ro, ne, Ne, NE, Pi, me
  (K = 13; `ro` and `pi` never occur lower-case, `Fi` occurs only in the 2013 siblings, `Cu` once, `NE` twice, `Ne` twice). A key is
  a surjective map of the 21 folded Italian letters onto the 13 classes (polyphonic). Trailing hyphens stripped as before; the 8
  open me/ne calls of Cheap test 1 are taken as transcribed in `transcription_bERB.txt` (conditional, rule 2).
- Instrument, dictionary, score, nulls, budget: unchanged from test 4b (it21news 2005-10 folds, top 40,000 types; held-out 2011-26
  fold for controls; unmatched word = log 0.01; 8 restarts x 16,000 moves; 4 processes; control seeds 1000-1004, target 2000, nulls
  2001-2010; control plaintexts drawn from random.Random(44), so the control word lists are the same draws as test 4b's). Only
  change besides K: random keys are drawn surjective directly (rejection sampling is impractical at K=13 over 21 letters).
- Command: `python3 test4_wordconstrained.py --siblings --case --budget 4 --jobs 4 > test4c_output.txt`.
- Gate (control first, rule 3; identifiability at K=13): 5 primary control seeds, matched design (random surjective 13-class key on
  held-out tokens at the target's exact word-length profile); EVERY seed's solver letter accuracy >= 0.60. Any miss: CONTROL BELOW
  GATE, target and nulls not run; logged "untestable by this instrument at K=13, N=120" (first attempt of this design), not refuted.
- Target moves only if its score exceeds all 10 shuffled-token nulls AND >= 60% of its 21 words find a dictionary match. A move is a
  grade-S candidate needing judge + verifier, never a reading. A non-move is a control-backed negative for this design only.
