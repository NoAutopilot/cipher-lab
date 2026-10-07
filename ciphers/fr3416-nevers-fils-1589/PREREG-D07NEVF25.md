# PREREG D07-NEVF25 -- sibling key-no.25 letter for the L05 pairing (account 1 for LANE DEFAULT-account-1-20261007-0042, 7 Oct 2026, written 01:2x UTC by date -u, before any sibling digit is read)

Question (AUDIT 3): L05 `... 4 5 7 9 ...` pairs as `45 79` (e + null; committed, frame from the run's first digit) or `4 57 9`
(m with two one-digit orphans; "et moiens" with L06). Does key-no.25 practice include stray single digits?

Sibling chosen: BnF fr.4715 f.27r (no.9, "Evesque" to Nevers, 2 Dec 1589; Gallica btv1b52509819x canvas f67, located with
`tools/gallica_folio.py btv1b52509819x --folio 27`). Overview (1000 px, one request) shows a wholly enciphered letter of ~40
figure lines with a period interlinear decipherment -- far beyond this job; only a sample is read.
Sample: 4 consecutive figure lines from the middle of the leaf, chosen by position from the iiif_lines output before any read
(the lines whose crops are numbered 10-13 counting from the top of the figure block; if segmentation merges lines, the next 4).
Free context already on disk (no new read): fr.4715 f.38v foot (46 tokens, Tomokiyo + NV02-READ image check: all pairs);
fr.3416 f.38 (SAME writer as f.35r) passes F and FB both read ". 9 . 0 ." dot-separated single figures in band 1 (low confidence).

Reading: 2 blind Sonnet passes on the line crops only (no key, no other pass), then my reconciliation (1 unit). Digits where the
passes disagree and the crop does not settle are marked '?'.

Statistic: frame switches per reconciled line. Decode each line under keys/key_no25.tsv at frame 0 (pairs from the first digit)
and frame 1 (skip one digit). Non-code pairs decode to '#'. Score windows of 8 pairs (step 4) by fr16 4-gram mean
(same scorer family as decode_f35.py). A switch is a point where the leading frame changes and the new frame leads by >= 0.3
for >= 2 consecutive windows. Also counted: any single figure both passes mark as standing alone (dots or a gap).
Control (can vary on the statistic): 20 trials, each inserts one random digit at a random position into one reconciled sample
line; the detector must flag a switch within 4 pairs of the insertion in >= 14/20, and must flag 0 switches on the 4 lines as
read. Control below either -> NON-TEST, nothing concluded from the sample.

Outcomes:
 A. >= 1 switch or isolated single figure in the f.27r sample, with both passes agreeing on the digits around it ->
    key-no.25 practice (another writer) does include orphan figures.
 B. 0 switches over >= 150 sample digits, control passing -> no orphan in this sample; practice evidence for frame continuity.
 C. control fails or < 150 digits -> non-test.
Grade rule, fixed now: f.27r is "Evesque"'s hand, not the f.35r writer's, and f.35r itself already carries four single-figure
M tokens (L03 '1', L04 '0', L07 '9', L10 '4'). So **no outcome moves tokens 45 or 79 from M**: A removes the "key no.25 has
no one-digit code" objection as a matter of practice (4 57 9 admissible), B weighs only weakly for 45 79. A grade move needs
same-writer material read at H (fr.3416 f.38's ". 9 . 0 ." or f.35r's own stray figures settled by a person). The reading of
f.27r beyond the sample is not attempted (a next step with a cost goes to NOTES.md).
