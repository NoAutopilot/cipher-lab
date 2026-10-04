# PREREG: two-instrument grading and the Noailles-1571 known-key test (N4-C1, 4 Oct 2026)

Written 04:2x UTC 4 Oct 2026 by N4-C1 (account 2 worker, for LANE-NEAR4), pushed before either statistic is computed.
Script: `two/two_instr.py` (written after this file). Stream = every cipher token of `ciphertext.tsv` AFTER this job's
c188L re-pass merge (clear words `[PLAIN:..]` and `/` excluded; every NEW*/blot/sign label kept as its own sign).

## A. Two instruments

- **Instrument 1** = `key.tsv` as it stands at commit time (READ2-C1161B strict-repair key: fitted on c185R + c186R block only;
  held-out PASS on the four other leaves, NEAR3-C1POOL (a)).
- **Instrument 2** = a blind homophonic anneal on the **four non-training leaves only** (c186L, c187L, c187R, c188L, in leaf
  order, as merged): `homophonic_anneal.solve`, fr16 order 3 (spec corpora), restarts 32, iters 40000, **seed 1**, uni_w 1.0,
  **nothing held** (no C signs fixed, no init). It never sees c185R or the c186R block, nor key.tsv. Seeds 2 and 3 are run too and
  reported for stability only; they do not choose the instrument.
- **Control** = the same recipe (seed 1) on the four-leaf stream **order-shuffled** (`random.Random(k).shuffle`, k = 1..5).
  Each control key is compared with instrument 1 by the identical statistic. Unigram counts are unchanged by the shuffle, so a
  control can reach any agreement that sign frequency alone explains; only order information separates the real arm.

**Statistic.** Agreement A = share of cipher-token occurrences in the full six-leaf stream, excluding the 6 C signs
(a, d, e, ee, p, sd) and excluding signs either key lacks, whose instrument-1 letter equals the instrument-2 letter.
Also reported (not gated): type-weighted agreement, and per-leaf A on c185R+c186R (instrument 2's held-out leaves).

**Gate.** PASS if A(real seed 1) > max over the 5 shuffled controls. If FAIL, no grade is upgraded on this evidence: every
non-C keyed sign is graded M ("one instrument only"), and that is reported as the result.

**Grades if PASS (per sign, carried to every token by `tools/decode_key.py`):**
- C: the 6 gloss-attested signs (unchanged).
- S: instrument 1 and instrument 2 (seed 1) give the same letter.
- M: they differ, or instrument 2 has no value for the sign (sign absent from the four leaves). key.tsv keeps instrument 1's
  value; the source cell names instrument 2's letter.
- U: signs neither key has (NEW*, blot, sign, spiralG, Sorn ...): unkeyed, no value added.
- Token transcription conf M still downgrades a token to M (decode_key's existing rule).

## B. Known key: fr16142 Noailles (Dax) Constantinople key, Tomokiyo's reconstruction

`tools/key_crossmatch.py` matches code labels, and the two folders label pen signs with private names (ours: tx/labels_v2.md;
fr16142: Tomokiyo's drawn glyphs as worded in its key.tsv), so a label-level run cannot compare them. Shape-level test instead.
The mapping below is fixed here from the two shape descriptions only (labels_v2.md vs fr16142 key.tsv glyph words), before
the comparison is computed. A Tomokiyo glyph used for two letters, or with no counterpart in labels_v2, is left out.

| Tomokiyo glyph (letter) | our label |
|---|---|
| E/epsilon (p) | e |
| 4 (p) | 4 |
| 7 (f) | 7 |
| 9-like (c) | 9 |
| x (d) | x |
| triple-bar, iii crossed (r) | iii |
| e-loop (r) | ee |
| f-cross (y) | f |
| caret ^ (a) | NEW_c188L_2 |
| alpha-like fish (t) | NEW_c187R_2 |
| triangle (l) | tri |
| z-crossed (n) | z |
| long-s variant (e) | ls |
| Y (s) | y |
| rectangle (g) | box |
| open square U (f) | sqc |

Excluded as ambiguous: # (Tomokiyo e and o both) vs iib; phi (o) vs phi-stem (s); theta-with-tail (d) vs our barred theta;
6/delta (e) vs 6 also a Tomokiyo null; d-loop (null).

**Statistic.** M = number of mapped labels whose value in instrument 1 (key.tsv) equals Tomokiyo's letter (labels unkeyed in
key.tsv count as non-matches). **Control:** 10,000 random permutations of key.tsv's values over its keyed signs (seed 1),
same count. **Gate:** the key "fits" only if M exceeds the permutation p99. Also reported: the same count under instrument 2.
Whatever the result, it is a shape-description comparison, not a decode; a FAIL means "this key family's letters are not
those of our key", conditional on the worded glyph descriptions (the table image is the authority, not on disk).
