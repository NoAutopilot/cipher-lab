# PREREG-D4V (verifier D4V-CEPPO, 8 Oct 2026, written 08:5x UTC before any tile was viewed)

Audit of D22-CEPPO21's five f.21v M -> S tokens: L04.17, L06.2.1, L06.2.6, L07.9, L09.5 (all S80 = a, R-8 "barred").

Blind sheet `verify/d4v/blind_sheet.jpg` (14 tiles, labels A-N, order shuffled with seed 8 by a script; the mapping is in
`verify/d4v/blind_key.json`, not opened until all 14 reads are written to `verify/d4v/blind_reads.tsv`):
5 targets; 2 plain-8 references (L01.32, L11.9); 2 barred-8 references (L03.20, L07.31); 5 decoys = tiles cut 70 native px
left or right of a target (the centred sign is a neighbour: S47/S89/S56/S97/S23/S53 or similar, never an 8), from the same leaf and
the same cut code. Each tile is called: BARRED-8 (bar through the waist out past both sides), PLAIN-8, NOT-8, UNDECIDED.

Control (rule 3; it can fail differently from the targets): the R-8 call, made blind, PASSES if no decoy and no plain reference is
called BARRED-8 and at least one barred reference is called BARRED-8. If it fails, all five targets go back to M.
Per token, if the control passes: BARRED-8 -> hold S; anything else -> lower to M.
Score side is not re-run as a gate (D22's own placement control, p 0.449, already shows the score cannot localise et among the 8s);
the S rests on shape. Rule 7: decode_key --check exit 0 at start (S 195, M 60, I 7, U 5).
