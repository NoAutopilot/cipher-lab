# PREREG test 4b -- erba-2006 (ERBA-SIB, LANE DEFAULT-A2-2209-14, account 2; written 14 Oct 2026, before any score)

Second attempt at R12D-ERBA4's instrument (test 4, PREREG-test4.md), per NOTES.md "## Next step (R12D-ERBA4, 6 Oct 2026)".

- Ciphertext: the 22-line image-checked transcription (`transcription_bERB.txt`, 17 words / 100 letters on xs = space) plus the two
  2013 sibling phrases (`ciphers/erba-2006/ciphertext_siblings_2013.txt`), each as its own segment: 21 words / 120 letters, lengths
  [2,7,6,10,1,12,11,11,8,9,4,3,1,6,3,2,4,5,6,2,7]. The siblings are a PRESS transcription only (il Giornale and Tgcom24, 18 June 2013,
  agreeing token for token); no image of the sheet was reachable on 14 Oct 2026 (tgcom24 article 404; il Giornale page carries an
  unrelated photo; web.archive.org CDX connection reset twice, host stopped). Every result is conditional on it (rule 2).
- Design, dictionary, score, null construction: unchanged from test 4 (xs = word space; 8 case-folded token types = 8 letter classes;
  it21news 2005-2010 folds as dictionary; held-out 2011-26 fold for controls; unmatched word = log 0.01).
- Budget: 4x test 4's anneal (8 restarts x 16,000 moves, was 4,000). Parallel in 4 processes, per-job seeds (control 1000-1004,
  target 2000, nulls 2001-2010; control plaintext draws from random.Random(44)).
- Command: `python3 test4_wordconstrained.py --siblings --budget 4 --jobs 4 > test4b_output.txt`.
- Gate (control first, rule 3): 5 primary control seeds at the target's exact word-length profile (120 letters); EVERY seed's solver
  letter accuracy must be >= 0.60 (stricter than test 4's mean gate). If any seed misses: CONTROL BELOW GATE, target not run; logged
  per rule 3's third-attempt clause as the second miss of this instrument -- "untested by this instrument at this N", not refuted; the
  next step then needs a different instrument or more material, not a further budget increase.
  (The secondary contiguous-window control of test 4 is dropped to fit the box; it was never gated.)
- Target moves only if its score exceeds all 10 shuffled-token nulls AND >= 60% of its 21 words find a dictionary match (unchanged).
  A move is a grade-S candidate needing judge + verifier, never a reading.
