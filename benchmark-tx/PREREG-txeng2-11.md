# PREREG TX-ENGINEER-2 round 11 (lane incarnation 3, session_01P46fwsU5VTc1oJiV1sayg5, 9 Oct 2026 22:2x UTC by date -u; pushed BEFORE any read or score; Amendment 9; the S2 score and any pool look are the lane's)

Rules as PREREG-txeng2-5's preamble. `tools/tx_register.py --check` passes on this file before any spawn.

## B3b Gunther calibration sheet corrected on its two shape slips + fresh two-pass baseline (TXE2-BASE-GUN2; Opus 5.5; cap 8; box 80 min; a baseline change, never a gain; Amendment 9 option (b); TX-RED F35)
Nearest prior: B3 / TXE2-BASE-GUN (stopped at step 1: the print-letter relabel conflicted with the image on 4 of 6), GS1 /
TXE2-GUNSHEET (the value-level cross), B1/B2 (sheet correction + baseline re-read on Spinelli), TX-POOL-LEAF (the original
read protocol). What is different: the treatment -- only the two exemplars whose SHAPE is mislabelled are relabelled, to
shape labels that fit both image and key (p1cal_L08.15 xb -> x; p1cal_L09.14 ps -> p); the four tiles whose shape label is
right and whose key value disputes the print (d6 L03.16, L06.14; Ib L05.14; 34 L06.17) stay as drawn, listed in
sheet/SHEET-CHANGELOG.md as "shape correct, value disputed", and the dispute is handed to ciphers/gunther-van-schwarzburg-1561/
NOTES.md as one line (no key edit). Then exactly B3's read: the corrected calibration.tsv committed with sha256 and the
changelog BEFORE any read; the brief = blind_pass_brief_p2.md with only the sheet changed (diff committed); two blind Opus
5.5 passes on the same committed p.2 crops, one call per <= 8 lines, do not resize, readers never see truth, decodes, the old
passes or the key; reconcile_passes.py + ONE Sonnet adjudication in packet shape (<= 16 rows per call, each row's crop
viewed, viewed recorded per row), passZ_gv2.tsv with sha256; ONE score (`tx_bench --exclude-flagged --paired
passZ_pipeline.tsv`, both figures; old -> new fixed/broken reported as a baseline change; openings 1). The pool's gunther
count follows B3b in a dated Amendment 9 line. Priced: 2 passes x 4 calls + 2 adjudication calls + 1 reconciliation unit.

Costs this round: 8. Eval looks this round: 0 by workers. Openings: B3b 1 (the baseline score).
