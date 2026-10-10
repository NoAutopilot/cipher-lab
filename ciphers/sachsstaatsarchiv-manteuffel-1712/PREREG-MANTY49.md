# PREREG-MANTY49 (10 Oct 2026, written and pushed before any crop is read; LANE FAMILY-A2q account 2)

Question: do blind readers, shown only the committed native line strips (no key, gloss text, transcription or codes),
read the 4|9 digit of this cipher correctly where a gloss fixes it -- and so can a blind read settle the y-shaped digit
(MANT-YCEN / FIX-YEYE asked this unblinded; MANT-FIX found two blind reads not separating a y-shaped 4 from 9)?

Census (y49/census49.py, script only, no image read; y49/census.tsv): every token carrying a digit 4 or 9 in the
settled transcription of the 694/08 leaves with token-level TSVs and committed crops: 0089, 0136, 0309, 0312, 0314,
0317, 0474, 0490 (R and L), 0494. 213 tokens (194 with exactly one 4/9 digit).

Known-answer subset (y49/known.tsv, 77 slots: 30 known-4, 47 known-9; 50 committed strips, none missing): a single-4/9
token inside a committed gloss span (period gloss as read by the leaf jobs' blind gloss passes; 0309-0317 both G1 and
G2, conflicting witnesses dropped) where (a) a letter-level DP alignment of the span's key values to the gloss gives
>= 0.60 agreement on the span's non-4/9 tokens, (b) the slot aligns to a gloss letter that key.tsv gives for exactly
one of its 4-variant and 9-variant codes, and (c) at least one adjacent keyed neighbour matched; or a one-code span
whose gloss (first 3 letters) names exactly one variant's key name (198 Stan:, 191 Steinbock, 292 Pol.). The label is
the digit that fits. 694/09 has no token-level leaf in this set (0063 is line-format): no 694/09 known slot.
No hand attribution is recorded on disk; per-hand split = per leaf and per volume (all known slots are 694/08).

Probe (unknown) slots, scored separately and never pooled with the gate: 694/09 0063 slot01-04 (f0063_09/crops,
the per-hand question MANT-EYE63R left) and the code-19 slots 0398 s02 p17, 0410 s02 p3/p8 (mant0608/fix19 crops).

Blind protocol: y49/sheets.py packs the 50 known strips (order shuffled, seed 49, labelled S01..) onto sheets at
native scale, max 1300 x 1400 px, plus one probe sheet (probe crops at 3x, labelled P01..). Two independent Sonnet
subagent passes (A, B); each call gets exactly one sheet and the instruction to transcribe every number group on
every labelled strip, left to right, groups separated by spaces, '?' for an unreadable digit, with no key, gloss,
transcription, code list or purpose beyond "transcribe numerals in a historical cipher". A pass is (one call per sheet).
Reader groups per strip are aligned to the strip's settled token sequence by edit distance (a group equal to the
settled code up to 4<->9 costs 0); the digit read at the slot's 4/9 position is the pass's read (4, 9, other, or
missing when unaligned).

Statistic, per pass: balanced accuracy BA = (recall on known-4 + recall on known-9)/2 over known slots with a 4 or 9
read; reads of other digits or missing count as wrong (denominator = all 77). Control: the known labels permuted across
the 77 slots, 10,000 draws, seed 1712, BA of the same reads recomputed; report mean and p99. The control can differ:
a reader that does not separate 4 from 9 scores ~0.5 under either label set; only a reader whose reads track the
gloss-fixed labels exceeds the permuted p99.
Gate: PASS if, for BOTH passes, BA > permuted p99 AND BA >= 0.80. Also reported (not gated): per-class recall, per
leaf, the y-candidate slots (known 9 but settled 4 in the transcription, and the reverse), and the 198-name slots apart.

Consequence on PASS: (i) a known slot whose settled digit disagrees with its label is edited only where both blind
passes read the label digit; (ii) a probe slot is edited only where both blind passes agree on a digit different from
the transcription; every such edit graded M, decode --check re-run. On FAIL: no edit; the y-glyph question is logged
"untestable by blind reading of these strips" (rule 3, a second attempt at MANT-FIX's blind-read approach).
Units: 2 passes x sheets (Sonnet) + 1 reconciliation by this worker; cap 3.5. If the sheet count exceeds 3, only the
first 3 sheets (fixed by the seed) are read and the subset scored is stated.
