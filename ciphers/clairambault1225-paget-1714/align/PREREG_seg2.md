# Pre-registration: a different segmentation instrument for the 420 M tokens (RUN1-PAG, 4 Oct 2026)

Written and committed before any run of `gibbs_pass.py` on the target pairs. Disk only (align/pairs.tsv, the period
interlinear gloss read off the images by NEXT-PAG/A2-PAG2/A2-PAG3). Letters: L1 = f60R f61L f61R f65L (8 Apr 1714,
17 pairs); L2 = f65R f66L f66R (28 Aug 1714, 39 pairs).

## Why this is a different instrument (rule 3 third-attempt clause)
tools/interlinear_align.py (four tests on these pairs, a fifth configuration closed) is hard-EM: each iteration commits
every pair to its single best chunking and re-counts, so a wrong early boundary can feed itself. The new instrument,
`tools/gibbs_align.py`, is a collapsed Gibbs sampler: each code's chunk distribution has a Dirichlet-process prior
(base = chunk-length prior x letter unigrams of the gloss material), a pair's boundaries are SAMPLED from their posterior
given every other pair (forward-filter backward-sample), gloss letters no code carries are an explicit insertion state,
null codes are a length-0 chunk under the same prior (not a free option as in C2), and values are read from posterior
modes over the kept half of the sweeps. Nothing is chosen from or initialised by the earlier alignments. Its offline
test (tools/tests/test_gibbs_align.py: synthetic homophonic syllabary with nulls and inserted gloss words) recovers
1.000 of planted values on the true pairing and 0.028 on a shuffled pairing.

## Settings (fixed now, tool defaults, never tuned on these pairs)
iters 200 (anneal temperature 3 -> 1 over the first 100, keep the last 100), alpha 1, max-chunk 4, ins 0.02,
len-weights 0.05,0.3,0.4,0.18,0.07 for lengths 0-4. Gloss folding: interlinear_align.fold + y->i. Sampler seed 0 for
each real run.

## Statistic: held-out agreement, both directions (identical definition to PREREG_homophone.md C1)
Sample each letter ALONE. Per token, its modal chunk over kept sweeps. key_A[c] = c's most frequent non-empty modal
chunk in A, kept only if unique. Direction A->B: over B's code tokens with a non-empty modal chunk whose code is in
key_A, the share whose modal chunk equals key_A[c]. Reported L1->L2 and L2->L1.

## Step 1: matched known-answer control (run first; the target is not scored unless it passes)
Synthetic gloss on the REAL code sequences of both letters (same N = the 56 runs, same code frequencies, same split):
each code gets a planted value, 10% of codes are nulls (empty), values drawn from a 60-chunk inventory (lengths 1-3 by
the len-weights, letters by the real gloss's unigrams, Zipf weights so several codes share a value: homophones), and
15% of runs get an inserted 3-6 letter word. 10 synthetic seeds. Reported: held-out agreement both directions (mean),
and planted-value recovery of non-null codes seen >= 2 times. **Control gate: mean held-out agreement >= 0.50 in both
directions.** Below it: CONTROL BELOW GATE, logged as a non-test, target not scored. The synthetic gloss is cleaner than
the real one (no spelling drift beyond insertions); a pass says the instrument has power at this N, not that the
real gloss is as clean.

## Step 2: null (shuffle) control, then the target
Null: the gloss texts (plain_raw) permuted across the pairs WITHIN each letter, 200 seeds (seed s: random.Random(s)
permutes L1 then L2; sampler seed s). It can differ from the target: held-out agreement depends on which gloss lies
over which code run, which is exactly what the permutation changes (and the statistic is not at ceiling under it: the
READ2-PAG aligner's shuffle mean was 0.03-0.05).
**Gate: real held-out agreement above the shuffle p95 in BOTH directions.**

## Per-code promotion (only if the gate passes)
A code is "supported in both directions" when key_L1[c] == key_L2[c] (unique non-empty tops). Its count is computed for
every shuffle seed too; codes are promoted only if the real count exceeds the shuffle p95 count (shuffle mean reported
as expected chance agreements). A supported code whose key.tsv row is graded M and whose value EQUALS key.tsv's value
becomes S (note "Gibbs pass S", via align/make_key.py; decode.json s_words then grades each token S where its own aligned
chunk agrees or is absent, M where it disagrees). A supported code whose value DIFFERS from key.tsv's is logged in
gibbs_codes.tsv and NOTES.md, not promoted and not changed (two instruments disagreeing is not a value). H/C rows are
untouched. Then `tools/decode_key.py ciphers/clairambault1225-paget-1714 --check`, H/C/S/M/I/U counts in NOTES.md.

## If it fails
Target and control numbers side by side in NOTES.md and HYPOTHESES.md; the M tokens stay M; the Gibbs sampler is
logged as instrument 2 on these codes (one test).
