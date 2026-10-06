# PREREG -- spec cheap test 3: fixed discrete alphabet structural check (R12D-CYL3, 6 Oct 2026)

Written and pushed before the scored run (rule 3). Script: `structural_test3.py` (seeded, deterministic).
Disclosure: before writing this file the worker printed the per-page sequence once (to see the layout) and noticed by eye
that rows `TAP FJN` recur on pp.6 and 16. The statistics below were chosen for the spec's question, not tuned to that.

## Data (fixed before scoring)
- Main sequence = Rotering's standard-alphabet pages: p.1 (A P; p.3 is its exact duplicate and is counted once), pp.5-16
  (p.17-19 have no transcribed sign). Per page: header sign then grid rows left-to-right, top-to-bottom.
- p.20 is excluded from the scored sequence (its own 6-wide layout and the C D E G H I K L variant signs that occur nowhere
  else); reported descriptively only.
- N, K = token and type count of that sequence (computed by the script). Transcription is Rotering's (2015), one page eye-checked
  (R12D-CYLOB): every result is conditional on his partition into signs (rule 2).

## Statistics
- S1 index of coincidence (unigram skew).
- S2 repeated within-page trigram tokens: windows of 3 consecutive signs inside one page's reading order (header+grid), count
  of window occurrences whose trigram occurs >= 2 times in the whole sequence.
- S3 repeated grid rows: number of 3-sign grid rows identical to at least one other grid row.
- Descriptive: type-growth (new types in the second half of the sequence), bigram repeat count.

## Controls and nulls (same N, same page/row skeleton, same K)
- (a) English, fixed alphabet: random contiguous letter windows of length N from tools/data/en (Gatsby, Huck Finn, Pride and
  Prejudice), enciphered with one random fixed many-to-one map 26 letters -> K signs per seed (K < 26, so homophony is
  impossible at this inventory; the map is polyphonic, each sign >= 1 letter), poured into the target's skeleton. 300 seeds.
- (b) uniform random null: K signs drawn uniformly, same skeleton. 2000 draws.
- (c) order-shuffle null: the target's own tokens permuted, same skeleton (preserves unigrams; S1 is invariant under it by
  construction, so (c) is used only for S2/S3). 2000 draws. For power, each English seed also gets its own 200-shuffle null.

## Gates (pre-registered)
- G0 power (control first): English seeds must beat (b)'s p95 on S1 in >= 80% of seeds, and beat their own shuffle p95 on S2
  in >= 80% of seeds. A gate whose G0 fails is a non-test for that statistic (reported, not read as a negative).
- G1 alphabet skew: target S1 > (b) p95.
- G2 sequential structure: target S2 > (c) p95 (and S3 reported vs (c) p95).
- Verdict words: G1 & G2 pass -> "discrete alphabet with sequential repetition beyond unigram chance (cipher-compatible, also
  compatible with a formulaic/pattern design); test 4 may be briefed". G1 pass, G2 fail -> "skewed alphabet, no order
  structure detected". G1 fail -> "flat inventory". Additionally, target S2 or S3 above the English control's p99 is reported as
  "more repetitive than enciphered English at this N" (a design pointer, not a language verdict).
