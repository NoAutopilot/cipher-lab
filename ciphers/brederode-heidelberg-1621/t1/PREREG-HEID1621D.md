# PREREG-HEID1621D -- first cheap test, unit inventory vs a Dutch word list (written 15 Oct 2026, 18:2x UTC, before any measurement)

Target: ciphertext.tsv (NA 1.01.02 inv. 6021 scan 379), 45 units (41 pairs + 4 longer units, structure_6021.json), all grade M.
No decode, no key, no reading: the test asks only whether the unit inventory looks like a word-level code at this N.

## Units
Primary: a unit = its numeral tuple (letters excluded: they are M and co-vary with the pair). Variant (reported, not gated):
numeral tuple + trailing letter. Both counted by `t1/inventory.py` straight from ciphertext.tsv (first reading, `alt` ignored).

## Frozen pool (fixed before the target statistic is computed; seed 1621)
nl16 (tools/data/nl16, 1569-1589 Dutch prose; era caveat: 1621 diplomatic letters are later and a different register).
Pool files: marn001bien01, marn001trou01, coor001zede01, spie001twes01. Held out for controls: coor001boev01.
- W-pool: 2000 windows of N consecutive words (N = the target's unit count); statistic K_w = distinct words.
- L-pool: 2000 windows of N consecutive letters; statistic K_l = distinct letters.
- S-pool (rough syllable proxy): 2000 windows of N consecutive vowel-group chunks (each word split after each vowel group); K_s.

## Statistic
K = distinct units at N; also the top-unit share and the hapax count. Target placement = its percentile in each pool.

## Matched control and gate (rule 3; control first)
C1 discrimination: 300 held-out windows each of word, syllable-proxy and letter codes from coor001boev01 at the same N;
classify each by nearest pool median of K. Gate: word-vs-letter accuracy >= 0.90. If C1 < 0.90: stop, "non-test at this N".
C2 (brief's control, a synthetic word code of the same length and unit count): held-out word windows at N whose K is within
+-2 of the target's K (if fewer than 20 such windows, take the 20 with K closest); enciphered as a one-to-one word code;
rank-match the units to the frozen W-pool word-frequency list (top 300 words). Score = share of tokens recovered. Gate: mean
>= 0.50. If C2 < 0.50, the rank-match step is not run on the target (a non-test at this N), and nothing is decoded.

## What counts
- Target K inside the W-pool central 90% -> inventory consistent with a word code (lead, M).
- Target K below the W-pool 5th percentile and inside the L- or S-pool 90% -> a word code at N is unlikely on inventory alone;
  the unit is smaller than a word (or the code repeats more than prose), named as such.
- Anything else: undecided.
A one-sided outcome is a lead about the design class, never a reading.
