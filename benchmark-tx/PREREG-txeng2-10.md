# PREREG TX-ENGINEER-2 round 10 (lane incarnation 2, session_011EV9AKeJ4YuU9jjghdUy6F, 9 Oct 2026 22:1x UTC by date -u; pushed BEFORE any read or score; Amendment 8; the S2 score and any pool look are the lane's (incarnation 3), after these jobs)

Rules as PREREG-txeng2-5's preamble. `tools/tx_register.py --check` passes on this file before any spawn.

## S2-ADJ The frozen step-3 adjudication on the S2 reads, as a protocol repair (TXE2-S2ADJ; Opus 5.5 worker, Sonnet adjudicator; cap 8; box 70 min; TX-RED F33 (a))
Nearest prior: S2-READ / TXE2-S2READ (steps 1-4; its step 3 not executed as frozen), TXE-Q (the packet-shape adjudication
that did view its rows), B1/B2 (adjudication units). What is different: nothing new is read -- the same queue and crops; the
adjudication is re-run in the frozen shape (packets <= 16 rows, each crop viewed, viewed recorded per row, 208 disagree rows
about 13 Sonnet calls, 167 agreed-uncertain kept), writing passZ_S2b.tsv + its sha256; no score, no truth, no decode.
Openings: 0.
## B3 Gunther calibration sheet corrected from the p.1 print alignment + fresh two-pass baseline (TXE2-BASE-GUN; Opus 5.5; cap 8; box 80 min; a baseline change, never a gain; TX-RED F35)
Nearest prior: B1/B2 (sheet correction + baseline re-read on Spinelli), GS1 / TXE2-GUNSHEET (the 6 mislabelled exemplars),
TX-POOL-LEAF (the original read protocol: blind_pass_brief_p2.md, crops, adjud_task.txt). What is different: the item --
the 6 mislabelled p.1 exemplars (d6 -> c x2, Ib -> s, 34 -> e, xb -> a, ps -> f) are relabelled from the p.1 print alignment
through the key (p.1 is outside the scored p.2: no opening), the corrected sheet committed with sha256 and a changelog
BEFORE any read; the brief = the original with only the sheet changed; two blind Opus passes on the same p.2 crops, reconcile +
one Sonnet adjudication in packet shape, passZ_gv2.tsv; ONE score (--exclude-flagged, both figures; old -> new fixed/broken as
a baseline change; openings 1). The pool's gunther count follows B3 in Amendment 9.

Costs this round: 8 + 8 = 16. Eval looks this round: 0 by workers.
