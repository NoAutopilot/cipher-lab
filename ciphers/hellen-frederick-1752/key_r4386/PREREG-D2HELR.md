# PREREG-D2HELR -- words-level frequency-fit test of R4386 (BL Add MS 32276 f.75) on the 1763 letters' 1201-2000 band

Written and pushed 6 Oct 2026, about 00:00 UTC by `date -u`, by D2-HELR (account 1 worker, LANE DEFAULT-account-1-20261005-2217),
BEFORE the R4386 images are fetched in this session and before any word is read. Rule 3. N7-HEL86's blank-cell test was a NON-TEST
at N=121 (sheet blank rate too low); this is the different instrument it named.

## What is read
The word (as written) in each of the 163 cells of `cells.tsv` (63 target codes = the 121 clean 1763 tokens in 1201-2000, and the
100 null codes drawn in N7-HEL86), same tiles (`crop_cells.py`, attribution of PREREG-N7HEL86 addendum A unchanged). Two blind
Sonnet passes (one call each), one reconciliation by this worker. Blank cells (N7-HEL86 state B/X) keep their state; an illegible
word is `?`. Result per cell in `words_read.tsv`.

## Statistic
Word score f(w) = log10((count of w in tools/data/fr18, lower-cased, apostrophe-elided forms split as written, + 1) / total tokens);
blank, `?`, "zero" or a multi-word entry with no corpus form scores the floor log10(1/total). For a multi-word entry the first word
counts. S = token-weighted mean of f over the 121 tokens (each token takes its code's word).

## Null (value shuffle, can differ from S because token multiplicities differ across codes)
10,000 permutations of the 163 read words over the 163 cells; S recomputed each time. Report null median, p95, p99 and P(null >= S).

## Positive control (rule 3, subsampled to the target's N)
R4369 on R1953 (`../key_r4369/reading_R1953_tokens.tsv`, H/S tokens with their read values; R4369 is the period key that reads
R1953). 200 subsamples: draw distinct codes of R1953 at random until their token multiplicities reach about 121 tokens, add 100
other in-key codes of `../key_r4369/key.tsv` (left value) as null cells, compute the same S and the same 1,000-permutation null.
Power = share of subsamples with S above its own null p99. **Power gate: >= 0.80, else NON-TEST at this N.** Also run once with
the R4369 values themselves permuted (a wrong key of the same design): its rate of S > p99 must be <= 0.05.

## Pass rule (fixed now)
- power OK and S > null p99 -> PASS: R4386 is a candidate key for the 1763 band; next a full decode of that band.
- power OK and P(null >= S) >= 0.50 (S at or below the null median) -> FAIL: R4386 retired for the 1763 1201-2000 band
  (instrument: words-level frequency fit).
- otherwise inconclusive, numbers logged, no third pass.
No threshold, corpus or floor is changed after words are read.

Correction (6 Oct 2026, 00:01 UTC by `date -u`): the header time is wrong -- `date -u` read 23:58 UTC on 5 Oct 2026 just before this
file was written and pushed (02115fd90), before the images were fetched (23:59) and before any word was read. Nothing else changed.
Control run before any word was read (`words_test.py --control`, `words_control.txt`): power 1.000, wrong key 0.005 -- gate met.
