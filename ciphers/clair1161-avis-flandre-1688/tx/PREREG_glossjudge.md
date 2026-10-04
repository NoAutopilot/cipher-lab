# PREREG-C1161GJ: gloss-and-judge value test of the contested key letters (RUN4-C1161GJ, 4 Oct 2026)

Written and pushed before any score below is computed. Disk only. Script: `two/glossjudge.py` (committed with or before
the first scored row). Outputs: `two/glossjudge.tsv` (one row per sign x value x key) and `two/glossjudge_gate.tsv`.

## Signs and alternatives (from NOTES.md RUN3-C1161MS / Remaining gaps item 1)

| sign | A = key.tsv value (grade) | B = 10-seed consensus letter | tokens (all six leaves) | tokens in c186R block |
|---|---|---|---|---|
| 2  | r (M) | t | 10 | 1 |
| tz | e (M) | l | 20 | 3 |
| qb | a (S) | e | 187 | 14 |
| 4  | o (S) | e | 224 | 12 |
| S  | u (S) | n | 275 | 14 |

Each sign is tested on its own, every other sign held at its key.tsv value (no joint test is gated; a joint B-for-all row
is reported as information only).

## Statistics
- **G (gloss match):** `glossctl/glossctl.py`'s statistic unchanged -- decode the 220-sign c186R block, difflib matching-
  block letters against the 170 gloss letters of `align/pairs_c186R_v0.tsv`, divided by 170.
- **J (judge language score):** `tools/judge_plaintext.py`'s `NgramModel.score` (mean log10 4-gram probability, fr16
  corpora of the spec's judge block) on the letters-only decode of all 3389 signs (3375 letters; reproduces
  `two/full_decode.txt` byte-for-byte under key.tsv). Used as a **relative** score only: AUDIT records the gloss itself
  PASSes the judge (-0.808) while the decode FAILs (-1.233), so the judge's absolute PASS/FAIL is not a gate here
  (rule 3, ZX-DEC349 paragraph); only differences between keys are read.
- For each sign: dG = G(B) - G(A), dJ = J(B) - J(A).

## Nulls
1. **Shuffled-key null.** The 50 keys of RUN3-C1161MS's shuffled controls (`two/cons/key_shuf{1-5}_s{1-10}.tsv`: anneals
   on five token-order-shuffled four-leaf streams). In each, set the sign to A and to B (signs absent from that key take
   their key.tsv value) and record dG_s, dJ_s. **Why it can differ from the real dG/dJ:** the gain of B over A at the
   sign's positions depends on the letters decoded around those positions; under a shuffled-order anneal key those
   neighbours are different letters, so a gain that only reflects B being a commoner letter than A (unigram frequency)
   appears in the null too, while a gain that depends on the real key's context does not. The statistic is computed on
   the same positions and the manipulation (the key's other values) changes the very n-grams and alignments counted,
   so the control is not orthogonal to the statistic.
2. **Letter null.** The sign set to each of the 26 letters a-z (others at key.tsv); rank of B (and of A) on G and on J.

## Gate (per sign; a value "passes" only if every clause holds)
For value V in {B, A} with W the other one:
- (i)  G(V) > G(W) and J(V) > J(W) (strict);
- (ii) the real d (V minus W) exceeds the shuffled-key null's p95 of the same d on BOTH G and J
       (p95 = 48th of 50 sorted values; strictly greater);
- (iii) V ranks in the top 2 of the 26-letter null on BOTH G and J (at most one other letter strictly better).
- Gloss floor: a sign with fewer than 3 tokens in the c186R block cannot pass the G half (one token moves G by at most
  1/170): sign `2` is "untestable by gloss at this N" and cannot pass whatever J says.

## Actions (pre-registered)
- B passes: key.tsv value -> B, grade S, source note "RUN4-C1161GJ gate PASS"; `tools/decode_key.py` regenerates the
  reading; the reading changes, so a rule-7 re-derivation and an AUDIT.md propagation are owed (not done by this worker).
- A passes: value unchanged; M signs (2, tz) M -> S; S signs keep S with the source note "RUN4-C1161GJ: key value
  confirmed against consensus letter".
- Neither passes: nothing changes in key.tsv; S signs are named "contested (single-seed S, gloss/judge undecided)" in
  NOTES.md, not regraded (brief: regrade only signs that clear the gate).
