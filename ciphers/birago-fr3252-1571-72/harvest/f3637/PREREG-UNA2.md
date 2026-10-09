# UNA2-BIR3252 pre-registration (9 Oct 2026, 10:1x UTC by date -u; written and pushed BEFORE any tile is re-cut or read)

Brief `.claude/briefs/runs/2026-10-09-account4-orch-unassigned-2.md` (UNA2-BIR3252), for the account-4 orchestrator.
**This is attempt 2 of the UNA-BIR3252 design** (PREREG-UNA.md): same rules, same known-answer tiles, same gate, same controls; the
only change is the location of the target tiles. A third attempt at this design (same instrument, one more knob) would be closed by
rule 3's third-attempt clause and is not to be briefed; the step after this one needs a different instrument or new material.

## Targets (the tiles UNA-BIR3252 left UNDECIDED for location reasons, tiles_key.tsv rows 1, 19, 20, 21, 22, 24, 31)
The brief and the Verdict say "6"; the Remaining-gaps line names 7 rows. All 7 are re-cut (the 7th costs one tile, no more units):
v36top_L02.37 (R-hash, mislocated), r36_L02.37 (R-8, edge), r36_L01.1 (R-6, mislocated), v36top_L05.26 (R-6, mislocated),
r36_L04.4 (R-dot, edge), r36_L08.8 (R-8, edge), v36top_L05.16 (R-hash, mislocated).
Not re-tiled: the blot (v36top_L04.37), the ligature (v36mid_L03.3), the known-answer conflict (v36top_L03.2), the no-rule pair
(v36top_L04.19) -- their blocker is not location.

## Location (the only change)
x and y of each target set by this worker's eye on 1x/2x strips of the native band (`../../../ceppo-nevers-fr3251-1570s/harvest/
witness_f36/`), locating the sign by its passD_v4 neighbour sequence, with an x/y ruler; no row-ink peak search (that is what put
three tiles on the L04 row). Same tile geometry as attempt 1: 150 x 80 native px, autocontrast cutoff 1, 4x LANCZOS. Disk only, no
network (Gallica 403 on 9 Oct). Before reading, a location check per tile: the tile's centre shows a sign and its left and right
neighbours (wider 1x context strip, not the 4x tile) match passD_v4; a tile that fails is UNDECIDED (location), not re-cut a third time.
The location strips are seen before the tiles; they are 1x and the deciding feature is not judged on them.

## Known answer (Gate 1, unchanged)
The same 6 known-answer tiles K1-K6 (same x,y as attempt 1, re-cut by the same code), shuffled with seed 32522 among the 7 targets
into one 13-tile set; map written to `tiles2/tiles_key.tsv`, not opened until `reads_una2_blind.tsv` is written and pushed. Caveat:
this reader has seen attempt 1's reads_una.tsv (which tiles were known answers and what the gloss says); the shuffle hides which tile
is which, not the KA label distribution. Gate: >= 5 of 6 rule label == gloss-implied label; UNDECIDED counts as wrong. If the gate
fails: stop, log a non-test, apply nothing.

## Rules (unchanged, PREREG-UNA.md): R-8, R-hash, R-6, R-bar, R-dot; a feature not visible at 4x -> UNDECIDED.

## Apply
`passD_v5.tsv` = passD_v4 with each DECIDED target set to its rule label (passD_v4 itself kept as attempt 1's candidate, so its
recorded controls stay reproducible). No C from this job; ciphertext_f36_v2.tsv, decode inputs and grades unchanged.

## Measures (unchanged)
E = (40 + splits not decided) / 700, before 0.293. Key control `decode_control.py passD_v5.tsv --shuffles 200 --windows 20 --err 0.286
--extra X_THETA2=r --seed 1,2,3`, Gate 2 rank 1/201 every seed. Placement control `una_placement_control.py` against passD_v5 (k =
all rows changed from passD_v3), n 500 seed 1; reported beside attempt 1's p 0.242 ("both ways"); also the 7-row increment alone
against random members of the same pairs on top of passD_v4 (n 500 seed 1).
