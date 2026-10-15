# PREREG test 4d -- erba-2006 (ERBA-SWAP, LANE DEFAULT-A2-0209-15, account 2; written 15 Oct 2026 02:27 UTC by date -u, before any score)

Second search-side attempt at test 4c's design, per NOTES.md "## Next step (ERBA-CASE, 14 Oct 2026)". Design unchanged; search
change only. Rule 3's third-attempt clause: if this control still misses, the K=13 design is logged "untested by this instrument"
and not re-briefed on the same instrument.

- Ciphertext, N, design: identical to test 4c (`transcription_bERB.txt` 22 lines + `ciphers/erba-2006/ciphertext_siblings_2013.txt`,
  press transcription only, rule 2; 21 words / 120 letters on xs = word space; 13 case-kept token types cu, Cu, mi, Mi, fi, Fi, un, Ro,
  ne, Ne, NE, Pi, me as K = 13 letter classes; surjective polyphonic key over the 21 folded Italian letters).
- Dictionary, score, nulls, seeds: unchanged from test 4c (it21news 2005-10 folds, top 40,000 types; held-out 2011-26 fold for
  controls; unmatched word = log 0.01; control seeds 1000-1004, target 2000, nulls 2001-2010; control plaintexts from
  random.Random(44), the same word lists as tests 4b and 4c; 4 processes).
- Search change (the only change): (a) a letter-swap move -- with probability 0.5 a move exchanges the classes of two letters in
  different classes, otherwise test 4c's single-letter reassignment; (b) 16 restarts instead of 8 (x 16,000 moves each, budget 4).
  32 restarts was the brief's example; 16 is chosen so control plus target and nulls fit the 50-minute box on 4 CPUs.
- Command: `python3 test4_wordconstrained.py --siblings --case --budget 4 --jobs 4 --swap 0.5 --restarts 16 > test4d_output.txt`.
- Gate (control first, rule 3): 5 primary control seeds, matched design; EVERY seed's solver letter accuracy >= 0.60. Any miss:
  CONTROL BELOW GATE, target and nulls not run; the K=13 design is logged "untested by this instrument" (second search-side attempt,
  rule 3 third-attempt clause), not refuted.
- Target moves only if its score exceeds all 10 shuffled-token nulls AND >= 60% of its 21 words find a dictionary match. A move is a
  grade-S candidate needing judge + verifier, never a reading. A non-move is a control-backed negative for this design only.
