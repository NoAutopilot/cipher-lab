# erba-2006 test 4 pre-registration (R12D-ERBA4, 6 Oct 2026, written before any scored run)

Instrument (new, per rule 3's third-attempt clause: not more restarts of test 3's bigram anneal): a **word-level constrained
decoder** for the letter-class (polyphonic) design. xs = word space (test 2's supported segmentation); the 8 other case-folded
token types (cu mi fi un ro ne pi me) are 8 letter classes; key = assignment of the 21 Italian letters to the 8 classes (all
used). A cipher word may decode only into an Italian dictionary word whose class pattern equals it.
Dictionary/unigram: tools/data/it21news folds y2005_06..y2009_10, top 40,000 word types, letters folded as in test 3.
Score(key) = sum over cipher words of log(sum of frequencies of dictionary words matching the pattern), unmatched word = log(0.01).
Search: simulated annealing over the key (8 restarts x 4000 moves). Decode: most frequent matching word per cipher word.
Target words: the image-checked transcription_bERB.txt, three streams split on xs (main/right/left as in tests 2-3), empty
segments dropped; 15 words, 100 letters (lengths as test 2).

Matched control (gate): 5 seeds. Held-out fold y2011_26 (not in the dictionary): for each target word, a random running-text
token of the SAME length (so N, word count and word-length profile equal the target's exactly), enciphered under a random
8-class partition, same solver. Statistic: letter accuracy of the decode vs the true plaintext.
Secondary control (reported, not gated): a contiguous held-out window of 100 letters with its real word boundaries.
Also reported: true-key (oracle) accuracy and how often the solver's score >= the true key's score (identifiability).

GATE: control mean letter accuracy >= 0.60. Below it: CONTROL BELOW GATE, target not decoded ("untestable by this instrument
at this N"). At or above it: run the target, plus 10 nulls = target tokens shuffled within the cipher (same word lengths).
Target "moves" only if its score exceeds all 10 null scores AND >= 60% of its words are matched; otherwise a negative under
this design at the control's measured power. Any decode is grade S at most, M per word unless the gate and null both pass.
