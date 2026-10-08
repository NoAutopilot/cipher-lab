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

## Round 1 outcome and round 2 (added 08:50 UTC 8 Oct 2026, before sheet 2 was viewed)
Round 1 (reads cc1ccb01c; local commit 099dc47b4 made before the key was opened, but the push was rejected and landed after
the key was opened -- disclosed): control FAILS as written. Decoy D (L09.5 +70 px) was called BARRED-8; on unblinding it is the
L09.5 8 itself: the stored centre in cut_r8_tiles.py (x 650) sits on the neighbour sign, and target tile E (L09.5 at x 650) was
called NOT-8. The other 4 decoys NOT-8, 2/2 plain PLAIN-8, 2/2 barred BARRED-8, 4/5 targets BARRED-8.
Round 2 (`verify/d4v/blind_sheet2.jpg`, key `blind_key2.json`, seed 82): 5 targets (L09.5 re-centred to x 720 from round 1),
2 plain refs, 7 decoys at random leaf positions on the band centres at least 110 px from any recorded 8 centre (a decoy may
still land on an unrecorded 8 or another barred sign; called as seen). Pass: no plain ref called BARRED-8, and every decoy
called BARRED-8 is, on unblinding, a sign whose passD label is S80 (checked by strip context). If round 2 passes: targets called
BARRED-8 hold S; else M. L09.5 additionally needs strip P to show the 8 between S53 and S23 (passD L09.4-6); otherwise M.
The targets are no longer blind to this reader (seen in round 1); round 2 is blind for the decoys and refs only.
