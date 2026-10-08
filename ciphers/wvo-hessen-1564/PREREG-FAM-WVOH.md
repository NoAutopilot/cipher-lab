# PREREG-FAM-WVOH -- reference-strip blind eye read of the 33 conflict/unaligned C tiles (f.23)

Written 8 Oct 2026 16:3x UTC (date -u), before any panel or strip is built or looked at. Worker FAM-WVOH (account 2, LANE FAMILY).
Attempt count for this step (per-row eye alignment of the 33 tiles): attempt 2. Attempt 1 = D2-WVO (PREREG-D2-WVO.md, decoy gate
FAIL 7/10, all misses k22 d read as g). D4-WVO was a different instrument (crib placement). The changed instrument here is the
letter-form reference strip; reader, panel format, targets and gate are otherwise D2-WVO's.

Targets: the same 33 tiles as PREREG-D2-WVO (`realign/tile_letters.tsv`, grade_after C, gloss_letter_realign != value_after).
These already include k11 "taush" (f23_C07_01_016, C07 idx 14) and the C03 "voans sp" span (C03 targets idx 6, 8, 10, 13, 19,
20, 23, 25, 27, 28), so both fold in with no extra panel.

Reference strip (shown to the reader, labelled with the letter): panels in the same format as the targets, cut over AGREE tiles
chosen by this worker before the read and excluded from the decoy pool:
- d (looped secretary d, k22): f23_C10_01_005 and f23_C07_01_012 (D2-WVO's decoys P28/P42, context "worden"/"vnd")
- g (k19): f23_C07_01_006 and f23_C05_01_006
- h (k08): f23_C03_01_003 and f23_C07_01_003
- i (k13): f23_C06_01_006
- s (k09): f23_C04_01_016

Known-answer control (rule 3; it can differ from the target since the reader is not told which panels are decoys): 10 fresh
decoys from the 159 AGREE tiles, excluding D2-WVO's 10 decoys and the 8 exemplar tiles: 2 drawn with random.Random(1613) from the
remaining k22 d AGREE tiles (the letter form that failed attempt 1; this makes the gate harder, not easier), 8 drawn with the same
generator from all other remaining AGREE tiles. Targets and decoys shuffled together (Random(1613)) into panels Q01-Q43.

Reader: one Opus vision subagent call, blind (asked only which gloss letter stands directly above the red box, '-' none, '?'
illegible, with the reference strip), then this worker's reconciliation of the reader's misses/doubts against the same panels
(the reconciliation does not change the gate score).

Gate: >= 8 of 10 decoys read as their AGREE letter. Below 8/10: counts reported, no class used, eye alignment non-test at this
reader accuracy; as this is attempt 2, the step is not retired by this run alone (rule 3 third-attempt clause).

Classes, key change rule and reported figure: exactly as PREREG-D2-WVO (AGREE / CONFLICT / NONE; a C key row changes value only if
>= 2 target tiles of that sign in >= 2 different rows read CONFLICT with the same letter AND the gate passes; eye-adjusted AGREE =
159 + targets read AGREE, out of 257).
