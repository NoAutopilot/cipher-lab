# PREREG CLIN-3004 (15 Oct 2026, written before any blind pass is run and before any score is computed)

Job CLIN-3004, LANE DEFAULT-A1-0740-15 (account 1). Item: B.147 p.229 (H-1649 Image 873, IIIF c0br8md7ck90;
images/h1649/seq_to_iiif.tsv row 873), the OPENING page of the cipher copy of item 3004 (PRO 30/55/25/60; Clinton to Haldimand,
New York, 9 Sept 1780; "New York Septr 9th 1780", "Sir", margin "See a decoded copy ... p.234"). The cipher runs over pp.229-233
(Images 873-877; p.233 ends with "H C", "Cypher L. Initialled" and the endorsement "From Sir Henry Clinton 1780 N. York the 9th
September, in Cypher. Recd by Lieut. Schieffly the 18th Octr"); per the brief only p.229 is done this job; pp.230-233 are named, not done.
p.229 mixes clear text (a long clear run "informing you of the Arrival of a French Armament ... it was not") with figure columns.
Never transcribed by this project. Seen before this file: 1000 px looks at Images 873-880 (two montages, to find the frames) and one
look at the p.234 decipherment (Image 878 at 2400 px, two crops of the same fetch, to read the known answer).
Known answer: the period decipherment B.147 p.234 (Image 878), passes/p234_reading.txt, read by this worker before any pass; the
lines between BODY and END, spaces and punctuation removed, '&' kept (spelling as on the page). p.235 (the rest of the decipherment)
not read: p.229's figures sit inside p.234's text, by the clear words on pp.229-230.
Everything below is CLIN-SIB's design unchanged (PREREG-CLIN-SIB.md; reused by -SIB2, -SIB3, -247 and -2962), with the known answer
switched to p.234: key as printed (variant a) GATED, variant (b) reported; the same cell classes (rule R0); the same statistic B2, a
run (>= 3 all-H letter cells, not crossing a column, ended by an underline or a non-letter cell) being a hit when its decoded string
is a substring of the p.234 letters; the same page-permuted-key control (1000 seeds, seed 123); the same prechecks (can-differ >= 0.99,
runs_ge3 >= 10, else NON-TEST); **the same gate: B2 share >= 0.60 AND hits > control max.** Threshold not re-tuned. If the decoded runs
do not read the p.234 text (gate FAIL with the share near the control), the page is logged as not shown on the 1778 key and the job stops.

Transcription: Image 873 at 3200 px to the scratchpad (not committed); each figure column cut as ONE crop with tools/iiif_lines.py
--image --region per column --centres (no seam inside a column); command pasted in NOTES before the first subagent call. Two blind
Sonnet passes on the column crops only (no key, no p.234 text, no other page's data, not told the question), then one worker
reconciliation on the crops of every A/B disagreement. passes/p229_reconciled.tsv; a cell still open after reconciliation is graded M.
Scorer: passes/check_p229.py (check_p226.py with the input, output and known-answer names changed; --check exits 1 when
check_p229.json is stale, rule 7). A PASS says only that the 1778 key reads these runs as the p.234 text beyond the permuted-key
control; no reading changes, AUDIT.md is not touched. A FAIL or NON-TEST is logged as such, with both numbers.
