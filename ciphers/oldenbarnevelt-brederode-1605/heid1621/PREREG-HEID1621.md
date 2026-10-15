# PREREG-HEID1621 (15 Oct 2026, 14:2x UTC by date -u; worker HEID-1621, account ytbiz, for LANE VIV-KEYSTONE account 4)

Pushed before any count is taken on the scan-379 groups. Brief: .claude/briefs/runs/2026-10-15-acct4-depth-steps.md, JOB HEID-1621.
Material: NL-HaNA 1.01.02 inv. 6021 scan 379 (left page, numeral block, 15 line crops cut by tools/iiif_lines.py from a native
region 730,1640,1960,1420 of a 5180x4100 image); scans 378 and 380 at 1200 px for the sender. No key, no reading, no family_run.

## Transcription protocol
Two blind Sonnet readers (text only, line crops only, no values or expectations given beyond "digits, dots, single letters, Dutch
words"), one reconciliation by this worker against the crops. Output heid1621/ciphertext_6021_379.tsv, one row per token
(line, pos, kind = num|let|word, text, grade M). Disagreements kept as alternatives in a column; the reconciled reading is graded M.

## Units
A unit is a maximal run of numeral tokens inside a cipher stretch, plus the single letter that immediately follows it, if any.
A "pair" is a unit of exactly two numerals.

## Statistics (computed on the reconciled transcription only)
S1 consecutive share: of pairs, the share with second = first + 1. Also the share over ALL adjacent numeral tokens in token order.
S2 distinct pairs: number of distinct pairs (by first value), total pairs, repeats.
S3 trailing-letter alphabet: distinct trailing letters, their counts, share of units carrying a letter.
S4 unit density vs Dutch: units per numeral-only line (a line with no Dutch word) against words per clear line and syllables
   (vowel groups, this worker's own reading of the clear lines L01, L15 and the clear lines of the same page at 1200 px, M) per
   clear line. Lead "unit ~ word" if the mean units/line is within +-25% of words/line; "unit ~ syllable" if within +-25% of
   syllables/line; neither or both = indeterminate.

## Controls
C1 (design control, the brief's): S1-S3 on obred187/tokens_92.txt (121 groups of no. 92, printed edition) -- adjacent-token
consecutive share and distinct values; no. 92 has no letters, so S3 there is 0 by construction (stated, not a test).
C2 (order null, can differ from the target because S1 is order-sensitive): S1 over all adjacent numeral tokens on the 379 tokens
with the numeral order shuffled 10,000 times (seed 1621); report the null mean and p99.
S4 has no matched control on no. 92 (a printed edition carries no manuscript line widths); it is reported as a lead only.

## Decision (lead, M; no class above M)
- "pairs always (n, n+1)" if S1 pair share >= 0.95 and the C2 p99 is below 0.5.
- Design-class lead read off S1-S4 together and written as a lead, never a reading.
- Stop rule: if the two readers disagree on more than a tenth of numeral tokens, the transcription is reported as unsettled and S1-S4
  are reported with that caveat (TRANSCRIPTION.md: a third pass is a person's, not a machine's).
