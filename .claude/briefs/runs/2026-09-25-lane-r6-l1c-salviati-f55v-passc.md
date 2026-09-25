LANE R6 L1c -- fr2933-salviati-1525 f.55v: third pass on the disagreements only, then settle (Sonnet, cap $6, box 45 minutes; disk only).
Common: 2026-09-25-lane-r6-common.md. Intake gate (live, 25 Sept 16:18 UTC): "fr2933-salviati-1525: open (line 1) -- edition/page or
full-text-search citation found within 6 lines" (exit 0).
State: passA_f55v.tsv and passB_f55v.tsv are complete; `recon_box.py` gate FAILED at 286/369 = 77.5 percent base codes; 87 rows in
recon_box_f55v/disagreements.tsv. CLAUDE.md Usage 6 allows a third pass when two disagree on more than a tenth of rows.
Job: (1) restore glyphs/crops/ as the leaf brief says (2026-09-25-lane-r6-l-salviati-leaf.md "Setup"; never commit atlas files); (2) YOU do
pass C on the 87 disagreement positions only, blind to both passes' calls (write a script that lists line,pos and crops each box at 5x from
glyphs/crops/f55v.png with its neighbours; read the crops against glyphs/atlas_part1.png/atlas_part2.png and the confusable pairs in the
leaf brief); passC_f55v.tsv (line, pos, code, marks, conf, note), committed every ~30 rows; no subagent. (3) Majority vote per row: 2 of 3
agree -> that call; three-way split -> settle from the crop with a reason, conf L. Recompute agreement as "rows where C agrees with A or B"
and report the three-way split count. (4) Write recon_box_f55v/settled.tsv and ciphertext_f55v.tsv exactly as ciphertext_f55r.tsv (grade AB,
AC, BC, settled). (5) Notes to ciphers/fr2933-salviati-1525/leafnotes/f55v.md ("## Leaf f.55v completed (25 Sept 2026, LANE R6 L1c)");
not NOTES.md. ROOM done: "for LANE R6: salviati f55v pass C, <n>/87 majority, <k> three-way, <tokens> sign tokens". No solving.
