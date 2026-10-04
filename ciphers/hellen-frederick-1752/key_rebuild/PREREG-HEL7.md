# PREREG-HEL7 -- context-fit key-rebuild of R1953 codes 1-800 (N5-HEL7, account 2 worker for LANE-NEAR5, 4 Oct 2026)

Written and pushed before any anneal, control or target statistic is computed. Disk only. Cryptanalytic: grade S at best, never H.
The retired period tables (R4370, R4372) are not used anywhere in this job.

## 0. Tool fix first (N4-HEL6 tool note)
`sibling_michell/test_sibling.py` `bigram()` gains `oov_floor=False`; with `oov_floor=True` an out-of-vocabulary LEFT word scores at
the unseen-pair floor log(0.3) = -1.204 instead of 0. Default unchanged, so every committed output (READ2-HEL, NEAR3-HEL4, N4-HEL6)
stays reproducible. Offline test `key_rebuild/test_oov.py` (synthetic counts, no corpus): OOV left word -> floor; unseen pair -> floor;
seen pair -> above floor; default mode keeps the old 0.

## 1. Data
- Stream: `key_r4369/reading_R1953_tokens.tsv` (846 tokens). Sign cleaned of `_` and `^`.
- **Free codes (target):** every token whose cleaned sign is an integer <= 800 (349 tokens, 201 distinct codes; occurrence profile
  1:133, 2:38, 3:10, 4:9, 5:4, 6:2, 7:2, 8:1, 10:2).
- **Known context:** tokens graded H or S whose value has at least one word (`words()` of test_sibling.py); a junction uses the last
  word on the left and the first word on the right. Every other token (M, U 801+, non-numeric) breaks the chain.
- **Candidate vocabulary V:** the 800 most frequent word types of `tools/data/fr18/*.txt.gz` (all files, `words()` tokeniser), single
  words only. Not built from any key. The Fagel 5177 clear pages are not transcribed on disk, so they are not used (stated, not run).
  Consequence, stated in advance: a true value that is a syllable, an abbreviation, a multi-word phrase or a word outside V cannot be
  recovered; the control reports this ceiling.

## 2. Objective (two arms, each gated on its own control)
Sum over every junction (adjacent pair) in which at least one side is a free code and both sides carry a word (known or assigned):
- **Arm P** (the brief's objective): N4-HEL6 Part B junction PMI, `pmi(a, c)` from `bigram(oov_floor=True)`.
- **Arm L**: log conditional probability of the right word given the left, same interpolation (0.7 bigram + 0.3 unigram, add-0.5
  unigram); OOV left word -> log unigram of the right word. Arm L exists because PMI alone rewards rare words; it is gated the same way.

## 3. Anneal (identical for control and target)
Gibbs sampling over V for every free code, initialised uniformly at random; 80 sweeps, temperature geometric 1.5 -> 0.05, then 5
greedy (ICM) sweeps. Seeds 1, 2, 3. Script `key_rebuild/rebuild.py`, `--check` exits non-zero when the committed output is stale.

## 4. Control first (rule 3; subsampled/matched to the target)
The 183 codes 801+ with at least one H/S token in R1953 are split at random (per seed) into 10 folds. Per fold, that fold's codes
are blanked (made free, in addition to the 201 target codes, which stay free exactly as in the target run), the anneal runs, and
each blanked code's assignment is compared with R4369's value: **exact recovery** = the true value's `words()` is exactly the one
assigned word. Blanking one tenth at a time keeps the context density at the target's (the target run has the same 201 free codes and
all H/S context present). Matching to the target's occurrence profile: recovery r_n per occurrence bin n in R1953 (1, 2, 3, 4, 5+);
**profile-weighted recovery R_w = sum_n w_n r_n**, w_n = the target's share of distinct codes in bin n (133, 38, 10, 9, 11 of 201).
Also reported: unweighted recovery, token-weighted recovery, and the ceiling (share of blanked codes whose true value is one word in V).
**Shuffled-assignment baseline:** per fold, 200 permutations of the anneal's own assigned values among that fold's blanked codes,
recovery profile-weighted the same way; mean over permutations and folds.

**Gate (per arm):** mean over seeds 1-3 of R_w >= 0.20 **and** >= 3 x the mean shuffled baseline. If an arm misses, no target run on
that arm. If both miss: stop, log "untestable by this instrument (context-fit anneal over fr18 top-800) at this N" in HYPOTHESES.md
with target and control side by side; no target run, no reading change.

## 5. Target run (only for an arm whose control passed)
Same anneal on the 201 target codes, seeds 1-3. Report per code: value per seed, occurrences. **S candidate** = same value on all three
seeds. The reading is refreshed only for a token whose code is an S candidate AND whose two neighbours are both known context words AND
both junctions are attested bigrams in fr18 (count > 0), in that token's own order. Such tokens are graded S; nothing is graded H.
Nothing is called a reading of the letter beyond those tokens.
