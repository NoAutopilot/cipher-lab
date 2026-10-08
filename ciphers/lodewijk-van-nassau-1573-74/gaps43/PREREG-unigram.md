# SIG-4612 pre-registration: fr16 word-unigram objective (8 Oct 2026, account 1, LANE SIG-1; committed before the pre-check, control or target runs)

Step: NOTES.md Remaining gaps "4612 cipher body", named next step: a global anneal under an fr16 word-frequency language
model, admitted only after key_full beats its own null-start optimum on the 5811 cut, then the 20%-perturbed >= 0.90 gate.

## Third-attempt check (rule 3)
Hypothesis H-S unchanged. GAPS43's word-segmentation cost failed its control because its optimum was the wrong key
(true key 52.8 vs 17.6). This objective is different: each word is priced by its own corpus frequency, not a flat 0.1, so
a chain of frequent short words is no longer free. Attempt 1 of this objective; allowed once by the lane brief.

## Objective (fixed; no tuning after the first scored run)
- Lexicon: folded fr16 corpus words (tools/french16_ngram.corpus_words), every length (single letters included, since the
  corpus tokenises elisions as L, D, QV ...), corpus count >= 2: 23,565 words, max length 20, P(w) = count / 939,272 tokens.
- Cost of a decoded run: min over segmentations (Viterbi) of sum -log2 P(w) over words + OOV_BITS per character left outside
  any word. OOV_BITS = 2 x the corpus's own mean bits per character (2.430) = 4.860, computed from the corpus, not the cipher.
- Search, alphabet, run breaks, nulls 121-138 dropped, 60000 iterations x 6 restarts, T 1.5 -> 0.05, swap share 0.3: all as
  GAPS43 (PREREG.md), unchanged. Script: word_anneal.py `--objective unigram` (this commit); test
  tools/tests/test_word_anneal_unigram.py.

## Disclosure
Before this commit one timing run was made on the 5811 cut (2000 iterations, 1 restart, key_full start): key_full cost
2635.3, the short run ended at 2486.5. It was run to size the box; no parameter above was changed after it. It already
suggests the pre-check may fail; the pre-check below is the decision, not this timing run.

## 1. Pre-check (decides whether anything else runs)
5811 cut to N=833 (word_share_check_v3.load_runs, as GAPS43). Anneal from unperturbed key_full (seed 0) and from three
uniformly random keys over the 23 letters (seeds 1-3). PASS iff key_full's cost <= the lowest annealed cost of all four
(ties pass). FAIL -> stop: H-S "untested-by-this-tool" for this objective, control and target not run.
The pre-check can differ either way: an anneal can land above key_full (local optimum) or below it.

## 2. Control gate (only on pre-check PASS)
As GAPS43: the same 20%-perturbed key_full starts (seeds 1-3, same perturbation RNG), recovery >= 0.90 in each seed.

## 3. Target (only on control PASS)
4612 v3 (ciphertext_4612_v3.tsv) from key_full and from 3 perturbed starts; report the French-word share (fr16 words >= 3
letters, word_share_check_v3) against the shuffle max 60.6% and the 79.2% bar, and the fr16 judge. Reassigned codes are
grade S at best; key_full.tsv and readings are not changed by this job.
