# PREREG CLIN-247 (15 Oct 2026, written before any blind pass is read and before any score is computed)

Job CLIN-247, LANE DEFAULT-A1-0447-15 (account 1). Item: B.147 p.247 **columns 3-8** (H-1649 Image 891, IIIF c01c1tf8862f; BL Add MS
21807 fo.210), the cipher copy of item 3077 (PRO 30/55/26/30; Clinton to Haldimand, New York, 18 Oct 1780). Opening in clear; columns
1-2 were checked by GAPS12 (52/52 cells). Columns 3-8 (about 150 figure cells with clear words and runs between them) were never
transcribed. Seen before this file: one 1:4 overview of the frame and one 2:3 look at the column block (to set the boxes).
Text known: the period decipherment B.147 p.246 (Image 890), read at H by GAPS12 (passes/p246_reading.txt) -- the known answer.
Everything below is CLIN-SIB's design unchanged (PREREG-CLIN-SIB.md, 59a9ce589; reused by PREREG-CLIN-SIB2.md and -SIB3.md), with the
known answer switched from p.245 to p.246: key as printed (variant a) GATED, variant (b) reported; the same cell classes; the same
statistic B2, a run being a hit when its decoded string is a substring of the p.246 decipherment letters (body from the line after
"Sir" up to "H C", spaces and punctuation removed, '&' kept; the P.S. excluded); the same page-permuted-key control (1000 seeds,
seed 123); the same prechecks (can-differ >= 0.99, runs_ge3 >= 10, else NON-TEST); **the same gate: B2 share >= 0.60 AND hits >
control max.** Threshold not re-tuned.

Transcription: Image 891 at 3200 px to the scratchpad (not committed); each of columns 3-8 cut as ONE crop with tools/iiif_lines.py
--image (--region per column, --centres every ~33 px, --lines-per-crop large enough for the whole column) so there is no seam inside a
column (CLIN-SIB2's lesson); command pasted in NOTES before the first subagent call. Two blind Sonnet passes on the six crops only (no
key, no p.246 text, no other page's data, not told the question), then one worker reconciliation on the crops of every A/B
disagreement. passes/p247c38_reconciled.tsv; a cell still open after reconciliation is graded M (and drops out of the all-H runs).
Scorer: passes/check_p247c38.py (check_p244.py with the input, output and known-answer names changed; --check exits 1 when
check_p247c38.json is stale, rule 7). A PASS says only that the 1778 key reads these runs as the p.246 text beyond the permuted-key
control; no reading changes, AUDIT.md is not touched. A FAIL or NON-TEST is logged as such, with both numbers.
