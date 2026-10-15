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

## Addendum CLIN-3004B (15 Oct 2026, 08:4x UTC by date -u; written before any blind pass on p.230 or p.231 and before any score)

Job CLIN-3004B, LANE DEFAULT-A1-0740-15 (account 1). Two further pages of the same cipher, each scored ON ITS OWN with the design above
unchanged: **B.147 p.230** (H-1649 Image 874, IIIF c0707wm9qt6b) and **B.147 p.231** (Image 875, IIIF c03775v2325j). pp.232-233 are
named, not done. Seen before this addendum: one 1600 px montage of Images 874+875 (to place the four figure columns per page; clear words
seen on it: p.230 "but the", "A small Vessel going to Quebec gives me an opportunity of repeating to you the above Intelligence and of
transmitting to your Excellency the", "to have", "We have since heard that an additional", "would be", "which I have reason to believe the
intended"; p.231 "Success in", "which being", "and against", "But it is highly probable that they will", "The Operation[s]", "greatly",
"and a considerable") and one look at Image 879 (p.235, the second page of the period decipherment) at 2400 px.
**Known answer, both pages:** p234_reading.txt BODY..END followed by p235_reading.txt BODY..END (read by this worker before any pass),
letters only, spaces and punctuation removed, '&' kept, spelling as on the page. The clear words above place p.230 in p.234's text and
p.231 across the p.234/p.235 join; the concatenation is fixed now, for both pages, and not changed after scoring.
Per page: one 3200 px fetch, each figure column cut as ONE crop (tools/iiif_lines.py --image --region --centres, command pasted in NOTES
before the first subagent call); two blind Sonnet passes on that page's crops only (no key, no decipherment, no other page's data, not
told the question; pass B reads the columns in reverse order); one worker reconciliation unit on the crops of every A/B disagreement;
passes/p230_reconciled.tsv, p231_reconciled.tsv; a cell still open after reconciliation is graded M and excluded from runs (rule R0).
Scorers passes/check_p230.py, check_p231.py (check_p229.py with input, output and known-answer names changed; --check exits 1 when stale).
Same rule R0 classes, same B2 statistic, key variant (a) GATED and (b) reported, same page-permuted-key control (1000 seeds, seed 123),
same prechecks (can-differ >= 0.99, runs_ge3 >= 10, else NON-TEST), **same gate per page: B2 share >= 0.60 AND hits > control max.**
Threshold not re-tuned. p.231 runs only if the job is under 80% of its cap after p.230; if not, it is named as not done.

## Addendum CLIN-3004C (15 Oct 2026, 12:0x UTC by date -u; written before any look at p.232 or p.233 and before any pass or score)

Job CLIN-3004C, LANE DEFAULT-A1-1140-15 (account 1). The last two pages of the same cipher, each scored ON ITS OWN with the design above
unchanged: **B.147 p.232** (H-1649 Image 876, IIIF c0zk55f78w96; CLIN-3004 saw a crossed-out block on it at 1000 px) and **B.147 p.233**
(Image 877, IIIF c0tt4fn9n48x; ends "H C", "Cypher L. Initialled" and the endorsement). Seen before this addendum: only CLIN-3004's 1000 px
frame montages (CLIN-3004 section of NOTES.md); nothing of these two pages at reading size.
**Known answer, both pages:** the same fixed concatenation as Addendum CLIN-3004B, p234_reading.txt BODY..END followed by p235_reading.txt
BODY..END (both already committed; not re-read, not changed), letters only, '&' kept, spelling as on the page.
**One change of method, by the job brief (not by any result):** ONE blind Sonnet pass per page (not two), on that page's figure-column
crops only (no key, no decipherment, no other page's data, not told the question; the pass is asked to mark every cell it is unsure of).
Reconciliation, one worker unit per page, BEFORE any decode or score: the worker reads every cell the pass flagged plus every underline,
and re-reads each column on 2x zooms of the 3200 px frame against the pass, from the image only; a cell still open after that is graded M
(excluded from runs, rule R0). No cell is changed after the scorer is first run.
**Crossed-out block (p.232):** figure cells inside a struck-through block are kind `struck` (not `letter`): they end any run and are not
scored, whatever they decode to; the block's extent is fixed in the reconciled TSV before the scorer is run.
Per page: one 3200 px fetch, each figure column cut as ONE crop (tools/iiif_lines.py --image --region --centres, command pasted in NOTES
before the first subagent call). Scorers passes/check_p232.py, check_p233.py (check_p231.py with input, output and source names changed;
--check exits 1 when stale). Same rule R0 classes, same B2 statistic, key variant (a) GATED and (b) reported, same page-permuted-key
control (1000 seeds, seed 123), same prechecks (can-differ >= 0.99, runs_ge3 >= 10, else NON-TEST; p.233 is expected to be short, and
a NON-TEST there is logged as NON-TEST, not merged with p.232), **same gate per page: B2 share >= 0.60 AND hits > control max.**
Threshold not re-tuned. p.233 runs only if the job is under 80% of its cap and box after p.232; if not, it is named as not done.
