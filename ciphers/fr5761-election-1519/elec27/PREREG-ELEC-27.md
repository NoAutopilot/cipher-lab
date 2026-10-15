# PREREG ELEC-27 (15 Oct 2026, written 17:4x UTC by date -u, before any fetch)

Question: is the f.84r l.27 sign (fr.3897 item 39 = Kluckhohn nr. 356, paired with Mayence; ELEC-39 labelled it 4, ELEC-356 left it 4|flag)
the same shape as the f.116r "4" (l.11, l.29; = Palatin, M) or the f.116r "flag" (l.32; = Mayence, M)?

Material: openapi.bnf.fr btv1b90096539 f142 full/2400 (f.116r = right half), f106 full/2000 (f.84r = right page). 2 requests, >= 3 s apart.
Crops of the four signs at the same scale (f.84r scaled to the f.116r pixel height of a line), placed side by side, read by one reader
(this worker, Opus, non-blind: the reader knows the print names Mayence at l.27).

Features scored per sign (each yes/no against each reference):
 F1 closed triangle or pennant at the top (flag) vs open angle with a vertical (4);
 F2 a horizontal cross-bar through the stem below the head (4 per ELEC-PAIR "4-like sign with cross-bar");
 F3 a single straight stem descending below the head (both may have; recorded, not decisive);
 F4 the head lies to the right of the stem (flag pennant) vs the diagonal starts top-right and runs down-left to the bar (4);
 F5 overall height relative to x-height of neighbouring letters.

Decision rule (fixed before looking):
 - "flag": F1 = pennant AND F2 = no AND F4 = pennant-right, matching l.32 on F1, F2, F4.
 - "4": F1 = open angle AND F2 = cross-bar present AND F4 = diagonal, matching l.11 or l.29 on F1, F2, F4.
 - Anything else (split on F1/F2/F4, or an image too poor to score F1 or F2) = "unsettled", label stays 4|flag.
Outcome handling: "flag" -> the slot joins flag = Mayence as a second both-sided pair (flag 2 pairs; grade by ELEC-PAIR rule 4 unchanged,
shuffle via elec356/pair_control.py only if the lane re-runs it; this job does not move any grade). "4" -> a logged conflict with
4 = Palatin in HYPOTHESES.md (rule 4: recorded, not resolved by frequency); 4 = Palatin stays M with the conflict noted. "unsettled" -> unchanged.
No key.tsv change in any outcome. If the l.11/l.29 "4"s and the l.32 flag themselves fail to differ on F1/F2/F4, the test is a non-test
(rule 3: the references cannot discriminate) and is logged so.

Step (2), item 37 between f.74r and f.81v, runs only if this step leaves the job under 60% of the USD 3 cap: one opening request, say whether
name signs (set A shapes) appear, M, no pairing.
