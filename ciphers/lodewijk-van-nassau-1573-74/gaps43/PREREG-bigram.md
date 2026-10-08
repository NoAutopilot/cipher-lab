# SIG-4612B pre-registration: fr16 word-bigram objective, PRE-CHECK ONLY (8 Oct 2026, account 1, LANE SIG-1; committed before the pre-check runs)

Step: NOTES.md Remaining gaps "4612 cipher body", the step SIG-4612 named after its unigram pre-check FAIL: a word-bigram objective
(word order priced) behind the same pre-check.

## Third-attempt check (rule 3)
Third LM objective for the same global anneal (GAPS43 segmentation cost: control FAIL; SIG-4612 word unigram: pre-check FAIL). Under
rule 3's third-attempt clause this job runs the PRE-CHECK ONLY. If it FAILs, the global LM-anneal instrument is [retired] for 4612
(H-S "untested-by-this-tool", not refuted); the next step needs new material or a different instrument. If it PASSes, the 20%-perturbed
control (3 seeds, >= 0.90 each) and only then the 4612 v3 target, exactly as PREREG-unigram.md sections 2-3.

## Objective (fixed; no tuning after the first scored run)
- Lexicon and OOV cost: exactly PREREG-unigram.md (folded fr16 corpus words, count >= 2, 23,565 words, max length 20; OOV_BITS 4.860).
- Bigrams: consecutive corpus tokens (tools/french16_ngram.corpus_words order) both in the lexicon; a token outside the lexicon breaks
  the chain. 267,758 distinct pairs, 23,461 contexts.
- P(w | v) = max(c(v,w) - D, 0) / c(v) + lambda(v) x P_uni(w), D = 0.75, lambda(v) = D x (distinct followers of v) / c(v)
  (interpolated absolute discounting; normalised). The first word of a run, and any word directly after an OOV character, take
  -log2 P_uni(w).
- Cost of a decoded run: Viterbi minimum over (position, previous word) of the summed bits.
- Search, alphabet, run breaks, nulls 121-138 dropped, 60000 iterations x 6 restarts, T 1.5 -> 0.05, swap share 0.3: as GAPS43 and
  SIG-4612, unchanged. Script: word_anneal.py `--objective bigram` (this commit); test tools/tests/test_word_anneal_bigram.py.

## Disclosure
Before this commit one timing run was made on the 5811 cut (2000 iterations, 1 restart, key_full start): key_full bigram cost 2559.6
(its unigram cost is 2635.3), the short run ended at 2416.9 (recovery 0.942). It was run to size the box; no parameter above was changed
after it. It already shows a key below key_full; the pre-check below, at the full schedule, is the decision.

## 1. Pre-check (decides whether anything else runs)
5811 cut to N=833 (word_share_check_v3.load_runs, as GAPS43). Anneal from unperturbed key_full (seed 0) and from three uniformly
random keys over the 23 letters (seeds 1-3, same random-key RNG as SIG-4612). PASS iff key_full's cost <= the lowest annealed cost of
all four (ties pass). The anneal can stop above key_full (local optimum), so the test can go either way.
