# PREREG-R9-ZESCH2: R9-ZESCH's word-parse objective under a stronger search (6 Oct 2026, account-4, LANE-RUN9-account-4)

Written and pushed 6 Oct 2026 (about 06:26 UTC by date -u) before any control accuracy or target statistic was computed.
The only runs before this file are two `wordseg_pt.py --time` timings (seed 2191, 400 and 2,400 moves per replica),
which print elapsed seconds only; no accuracy or J value was printed or read.

## What is unchanged
- Objective: `wordseg_syllabary.py`'s `WordLM.llr` (word-parse Viterbi minus letter-unigram background, 20-token chunks,
  OOV -2.0, words seen >= 2 times, length <= 14), injective key, 7 pins fixed. Imported by `wordseg_pt.py`, not copied.
- Corpora: fr1810 (1800-1811 official correspondence, ~30 years before the 1841-42 letters, not era-exact) and de19.
- Matched control: `wordseg_syllabary.build_control()` unchanged (2,666 tokens, K = 98, 7 pins, 1 pct digit error,
  held-out fr1810 `lettresindites01napo` / de19 `pg31538`), so its true-key J is R9-ZESCH's 1181.7.
- Statistic: mean non-pin token accuracy over 3 seeds. **Gate 0.60, unchanged.**

## What is different (the search; R9-ZESCH: random start, one cooling chain 2.0 -> 0.05, 2 restarts x 50,000 moves)
1. Crib-free frequency-rank initialisation: non-pin codes ranked by ciphertext count matched to candidate units ranked
   by expected frequency (training text tokenised by greedy longest match over a unit list built by the control
   generator's own design rule: 26 letters + Bourdeau's multi-letter pin units + commonest training bigrams/trigrams up
   to K). Uses no plaintext of the cipher. Caveat stated in advance: the unit list encodes the design hypothesis the
   control was built on; if the real cipher's unit set differs, the target's initialisation is weaker than the control's.
2. Parallel tempering: 5 replicas at fixed T = 0.05, 0.15, 0.4, 1.0, 2.0, each started from the frequency-rank key plus 10
   random code-code swaps, adjacent replicas exchanging every 400 moves (Metropolis on the J difference).
3. Moves: half code-code swaps (frequency-preserving), half R9-ZESCH's code->unit move.
- Budget: 50,000 moves per replica = 250,000 per seed (2.5x R9-ZESCH's 100,000). Seeds 2191, 2192, 2193.
- Reported beside accuracy: each seed's best J and the initial key's J and accuracy, against the true key's 1181.7.

## Stop rules
- Control mean < 0.60: CONTROL BELOW GATE; target not run; logged "untested-by-this-tool at this N" in HYPOTHESES.md.
  This is the second attempt at this objective (R9-ZESCH was the first); the NOTES.md entry states whether a third
  would be rule 3's third-attempt case (it is, if a third attempt changed only search settings, since this job already
  changed the search family once).
- Control >= 0.60: run the target (same seeds/settings) and the digit-shuffled target through the same search (rule 3
  ARM-C1); judge both decodes with `tools/judge_plaintext.py` (fr1810, era caveat above); every token M at most.
- Cap 4 USD, box 06:20-07:30 UTC (80% 07:16): a run that cannot finish by 07:16 is not started.
