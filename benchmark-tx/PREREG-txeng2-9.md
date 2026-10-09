# PREREG TX-ENGINEER-2 round 9 (lane incarnation 2, session_011EV9AKeJ4YuU9jjghdUy6F, 9 Oct 2026 21:3x UTC by date -u; pushed BEFORE any read or score; pool 28 under Amendment 7; S2 frozen; the S2 look and the first pool look are the lane's, after the verifiers)

Rules as PREREG-txeng2-5's preamble. `tools/tx_register.py --check` passes on this file before any spawn.

## S2-READ The frozen S2 pipeline's reads on vivonne1573-f103r-confirm2, no score (TXE2-S2READ; Opus 5.5; cap 18; box 110 min)
Nearest prior: PREREG-txeng2-S2 FROZEN (the pipeline), TXE-Q (the Spinelli confirm reads: the protocol), B1 (brief diff
committed before any read). What is different: the item itself -- the one confirm2 leaf, never opened by the lane; this job
runs steps 1-4 of the frozen pipeline exactly, commits every output with sha256, and NEVER runs tx_bench or opens the truth
(the lane scores once after V-VIV). Priced: 10 Opus calls + 2 adjudication units + the crop/overlap check. Openings: 0.
## V-VIV Verifier pass on confirm2's align-conflict flags (TXV-VIV; Opus 5.5; cap 4; a verifier session, never a reader of the cipher)
Nearest prior: V1 / TXV-152, V2 / TXV-SPIN (flags decided through the build script's flag column from the witness image).
What is different: the item (confirm2), the witness (the clerk's decipherment on fr.16105 ff.104r-108v, read by N4-VIV2 in two
blind passes, images on disk) and the key (Tomokiyo's published table): every position build_vivonne_confirm2.py flags
align-conflict is decided FLAG / CORRECT / KEEP; the verifier never sees any pass on f.103r. Openings: a verifier pass on
the eval item's truth (1).
## V3 Verifier pass on gunther8246-p2's 15 align-conflict flags (TXV-GUN; Opus 5.5; cap 3; verifier, never a reader)
Nearest prior: V1, V2, V-VIV. What is different: the witness is a 1934 print (Japikse no.316) and the key is ours (rebuilt
from 5109): each of the 15 flagged positions (th=o x3, Ib=s x2, d6=c x2, x=f x2, ...) is decided FLAG (key gap: the label
lumps two glyphs; or encipherer's slip) / CORRECT / KEEP from the WVO scan, the print and the sibling key, through
build_gunther8246p2.py's flag column; the pool recount follows in Amendment 8. Openings: 1.
## GS1 Gunther calibration-sheet cross, read-free (TXE2-GUNSHEET; Opus 5.5; cap 2; TX-RED F31 c)
Nearest prior: A1 / TXE2-SHEETAUDIT, A2 / TXE2-SHEETS-ALL (the cross method). What is different: the p.1 calibration sheet
(txpool/gunther8246-p2/sheet/, labelled by the committed reading) is crossed against the whole-letter Japikse alignment
through the key, exemplar by exemplar, as A1 did for Spinelli; mislabelled exemplars listed; no correction (a correction is
B-class, pre-registered separately). Openings: 0 (p.1 is outside the scored p.2 positions; the alignment is read at p.1 only).
## B2 Spinelli sheet v5 from Domnina's published table + fresh two-pass baseline (TXE2-BASE-SPIN2; Opus 5.5; cap 6; a baseline change, never a gain; TX-RED F30)
Nearest prior: B1 / TXE2-BASE-SPIN (atlas_v4 baseline), A1 (the sheet correction method), X1c (retired, Amendment 7).
What is different: the three forms the readers marked NEW: (circle-on-stem, long-s-crossbar, looped-H) are looked up in
Domnina 2016's published table (keys/key_domnina_2016_atlasmap*.tsv, the published cell drawings) -- if the table carries a
cell of that shape, it is added to the sheet as atlas_v5 with the cell's published name, never with a tile chosen through
a truth position and never with the value the truth gives; if the table has no such cell, the sheet is unchanged and the
job stops after saying so. Then B1's exact protocol (brief diff committed before any read, two blind Opus passes, reconcile,
one adjudication, commit with sha256), and ONE score as the new baseline (an opening, counted; no paired instrument claim;
old -> new fixed/broken reported as a baseline change). The pool's Spinelli count follows B2 in Amendment 8.

Costs this round: 18 + 4 + 3 + 2 + 6 = 33. Eval looks this round: 0 by workers; the lane's S2 look and any first pool look follow the verifiers.
