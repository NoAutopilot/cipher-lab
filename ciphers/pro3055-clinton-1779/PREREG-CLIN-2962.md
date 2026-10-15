# PREREG CLIN-2962 (15 Oct 2026, written before any blind pass is run and before any score is computed)

Job CLIN-2962, LANE DEFAULT-A1-0447-15 (account 1). Item: B.147 p.226 (H-1649 Image 870, IIIF c0r20rs09w8b; BL Add MS 21807
fo.193), the cipher copy of item 2962 (PRO 30/55/25/18; Clinton to Haldimand, New York, 14 Aug 1780; "Cypher L. Initialled",
"H C"). One page, seven ruled columns of figure entries (about 180 cells) with a few clear words ("Said", "and" seen on the layout
look). Never transcribed by this project. Seen before this file: a 1000 px look at Images 869-870 (to find the frames), one
1200x1200 px layout look at the p.226 column block (to set the boxes), and one look at the p.225 decipherment (to read the known answer).
Known answer: the period decipherment B.147 p.225 (Image 869), passes/p225_reading.txt, read by this worker before any pass; the
lines between BODY and END, spaces and punctuation removed, '&' kept (spelling as on the page: "Terney", "twelfth").
Everything below is CLIN-SIB's design unchanged (PREREG-CLIN-SIB.md; reused by -SIB2, -SIB3 and -247), with the known answer switched
to p.225: key as printed (variant a) GATED, variant (b) reported; the same cell classes (rule R0); the same statistic B2, a run (>= 3
all-H letter cells, not crossing a column, ended by an underline or a non-letter cell) being a hit when its decoded string is a
substring of the p.225 letters; the same page-permuted-key control (1000 seeds, seed 123); the same prechecks (can-differ >= 0.99,
runs_ge3 >= 10, else NON-TEST); **the same gate: B2 share >= 0.60 AND hits > control max.** Threshold not re-tuned. The known answer is
short (about 230 letters), which makes chance substring hits likelier on both sides; the control carries that, and no threshold moves.
If the decoded runs do not read the p.225 text (gate FAIL with the share near the control), the item is logged as not shown on the
1778 key on this page and the job stops (brief).

Transcription: Image 870 at 3200 px to the scratchpad (not committed); each of the seven columns cut as ONE crop with tools/iiif_lines.py
--image --region per column --centres (no seam inside a column); command pasted in NOTES before the first subagent call. Two blind
Sonnet passes on the seven crops only (no key, no p.225 text, no other page's data, not told the question), then one worker
reconciliation on the crops of every A/B disagreement. passes/p226_reconciled.tsv; a cell still open after reconciliation is graded M.
Scorer: passes/check_p226.py (check_p247c38.py with the input, output and known-answer names changed; --check exits 1 when
check_p226.json is stale, rule 7). A PASS says only that the 1778 key reads these runs as the p.225 text beyond the permuted-key
control; no reading changes, AUDIT.md is not touched. A FAIL or NON-TEST is logged as such, with both numbers.
