# PREREG CLIN-SIB3 (15 Oct 2026, written before any blind pass is read and before any score is computed)

Job CLIN-SIB3, LANE DEFAULT-A1-0206-15 (account 1). Item: B.147 p.244 (H-1649 Image 888, IIIF c0dj58d8cb3c; BL Add MS 21807 fo.207),
the closing page of the cipher copy of item 3050 (PRO 30/55/26/2; Clinton to Haldimand, New York, 2 Oct 1780; cipher pp.242-244 =
Images 886-888). p.242 was checked by GAPS12 (cols 1-3, 66/66) and CLIN-SIB2 (cols 4-6, B2 PASS 14/14); p.243 by CLIN-SIB (B2 PASS
17/18). p.244 holds three columns of figure cells (about 30, 27 and 8 rows), a few clear words, "H C" and the endorsement below.
Seen before this file: one 1:4 overview, one 1:2 layout look of the column block, one crop montage (to set the boxes). Expected to sit
near the runs_ge3 floor of 10 (CLIN-SIB2's PREREG said so); the floor is kept as registered, not lowered: under 10 = NON-TEST.
Text known: the period decipherment B.147 p.245 (Image 889), read at H by GAPS12 (passes/p245_reading.txt) -- the known answer.
Everything below is CLIN-SIB's design unchanged (PREREG-CLIN-SIB.md, 59a9ce589; as reused by PREREG-CLIN-SIB2.md, 7d90ea286): key as
printed (variant a) GATED, variant (b) reported; the same cell classes; the same statistic B2 (substring of the p.245 letters); the
same page-permuted-key control (1000 seeds, seed 123); the same prechecks (can-differ >= 0.99, runs_ge3 >= 10, else NON-TEST);
**the same gate: B2 share >= 0.60 AND hits > control max.**

Transcription: Image 888 at 3200 px to the scratchpad (not committed); each column cut as ONE crop with tools/iiif_lines.py --image
(--region per column, --centres every 35.8 px, --lines-per-crop 30) so there is no crop seam inside a column (CLIN-SIB2's lesson);
command pasted in NOTES before the first subagent call. Two blind Sonnet passes on the three crops only (no key, no p.245 text, no
other page's data, not told the question), then one worker reconciliation on the crops of every A/B disagreement.
passes/p244_reconciled.tsv; a cell still open after reconciliation is graded M (and so drops out of the >= 3 all-H runs).
Scorer: passes/check_p244.py (CLIN-SIB2's check_p242c46.py with the input and output names changed; --check exits 1 when
check_p244.json is stale, rule 7). A PASS says only that the 1778 key reads these runs as the p.245 text beyond the permuted-key
control; no reading changes, AUDIT.md is not touched. A FAIL or NON-TEST is logged as such, with both numbers. p.247 is not started.
