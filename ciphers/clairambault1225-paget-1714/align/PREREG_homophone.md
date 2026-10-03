# Pre-registration: open-codes homophone/null pass (READ2-PAG, 3 Oct 2026)

Written and committed before any run of `homophone_pass.py`. Disk only (align/pairs.tsv, the period interlinear gloss read
off the images by NEXT-PAG/A2-PAG2/A2-PAG3). Aligner: tools/interlinear_align.py through align/evaluate.py (the shared DP/hard-EM
tool; no private aligner), NEXT-PAG's settings fixed on training data on 2 Oct 2026: floor 1, max-chunk 4, seg-bonus 0.5,
len-prior 0.5. Letters: L1 = f60R f61L f61R f65L (8 Apr 1714, 17 pairs); L2 = f65R f66L f66R (28 Aug 1714, 39 pairs).

## Hypothesis classes
- **one-unit**: each code stands for one plain unit (a syllable or short word); its chunk recurs across both letters.
- **homophones**: several codes stand for the same plain unit. This is a property of the key (many codes -> one value), not of the
  per-code test: a homophonic code still holds one value in both letters. It is read off the result as the number of distinct values
  among codes supported in both directions (codes / values); it does not get its own statistic.
- **nulls**: some codes absorb no gloss. Tested by alignment configuration C2 below, where a code may take an empty chunk at no cost
  and the empty chunk counts as a value ('' = null) for agreement.
Configurations: **C1** null-cost -3 (NEXT-PAG, primary); **C2** null-cost 0 (nulls free; '' a value). Nothing else is varied.

## Statistic: held-out agreement, both directions
Align each letter ALONE. For letter A, key_A[c] = c's most frequent folded chunk in A's own alignment, kept only if unique (no tie
for first). Direction A->B: over B's aligned code tokens whose code is in key_A, the share whose own B chunk equals key_A[c]
(C1: tokens with an empty chunk are excluded from both counts and empty is never a key value; C2: empty counts as the value '').
Reported for L1->L2 and L2->L1, per configuration.

## Control
The same procedure with the gloss texts (plain_raw) permuted across the pairs WITHIN each letter (per-letter shuffle; each letter's
own gloss material stays in that letter), 200 seeds (seed 0-199, random.Random(seed), L1 shuffled then L2 from the same generator).
It can differ from the target: held-out agreement depends on which gloss sits over which cipher run, which is exactly what the
permutation changes.

## Pass gate
Per configuration: held-out agreement above the shuffle p95 in BOTH directions. Two configurations are tested; both are reported
whatever they show.

## Per-code promotion (only from a configuration that passes)
A code is "supported in both directions" when key_L1[c] == key_L2[c] (both unique tops) and the value is non-empty. The count of
such codes is also computed for every shuffle seed; codes are promoted from a passing configuration only if its real count exceeds
that configuration's shuffle p95 count, and the shuffle mean count is reported as the expected number of chance agreements. A
promoted code must also equal the value key.tsv already holds (the full-run alignment); a mismatch is logged, not promoted. If both
configurations pass and give a code different values, it is not promoted. Null codes (C2 '' in both letters) are reported, never
put in the key.
Grades: a promoted code's key row (only rows now graded M) becomes S (never H: the value is chosen by this test). Per token: S where
the token's own aligned chunk (votes.tsv) agrees with the value or it has none, M where it disagrees, M on a transcription-doubtful
digit (decode_key's existing rule). Rows already H/C are untouched. Then `tools/decode_key.py ciphers/clairambault1225-paget-1714
--check`, H/C/S/M/I/U counts in NOTES.md. Judge: run only if specs/clairambault1225-paget-1714.json exists (it does not on 3 Oct 2026).

## If it fails
Target and control numbers side by side in NOTES.md and HYPOTHESES.md; the 428 M tokens stay M; logged as an instrument result
under rule 3's third-attempt clause, with the count of instruments tried on these codes.
