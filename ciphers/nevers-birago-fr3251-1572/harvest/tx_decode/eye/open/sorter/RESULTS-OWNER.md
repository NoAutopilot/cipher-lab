# BIR-OWNER results (3 Oct 2026, 18:38-18:50 UTC, account-3 worker)

Prereg `PREREG-OWNER.md` pushed at 8bbb3861 before any score. One post-prereg fix, made before any result was read: line alignment for
lines with equal tile and position counts is identity (difflib had mis-mapped 4 tiles on f117 L03, where the sorter's own labels differ from the
current transcription at 10 positions); the prereg's tile->position sentence was amended in the same commit. Vision 0, network 0.

`tools/sign_sorter_apply.py --labels owner-2026-10-03/labels.tsv --db owner-2026-10-03 --out owner_settled.tsv` ran unchanged on the flat dump
(488 tiles: kept 346, moved 68, taken-out 58, bad-cut 11, aside 5; 21 new piles; T60 pile verdict "same"). `score_owner.py` -> `owner_positions.tsv`,
`owner_score.json`; `sort_next.py` -> `sort_next.tsv`.

| leaf | owner changes (value / U) | S / M | (a) base | (b) owner picks | (b-S) S+U only | (c) control p95 (median) | (b) rank in 201 | gate |
|---|---|---|---|---|---|---|---|---|
| f.117r (fr) | 14 / 10 | 3 / 11 | -1.215 | -1.320 | -1.217 | -1.234 (-1.311) | 118 | FAIL |
| f.168 (it16dip) | 10 / 4 | 1 / 9 | -1.149 | -1.418 | -1.280 | -1.146 (-1.262) | 199 | FAIL |
| f.144r (it16dip) | 8 / 9 | 1 / 7 | -1.418 | -1.266 | -1.282 | -1.346 (-1.537) | 2 | PASS |
| pooled | | | -1.239 | -1.333 | -1.244 | -1.255 | | FAIL |

Agreement of owner moves with each blind instrument where both read the position: f.117r VERIFY 3/18, BIR-OPEN 5/24, A1-BIR-EYE 1/13;
f.168 VERIFY 2/6, BIR-OPEN 3/10, EYE 0/6; f.144r VERIFY 1/13, BIR-OPEN-144 1/13, EYE 1/6. On the T65/T95/T51 conflicts the owner mostly
picked T65 or a new pile, a third answer that neither machine gave.
Focus tiles: 25 (the focus file said L09.30 had no tile, but tile f117_L09_29 is position 30, since the missing L09 tile is position 21). The owner
touched 21: moved 15, aside 5, bad-cut 1. Untouched 4: f117 L07.21, L05.18, L06.13, L08.23.
Applied: f.144r only (gate PASS), in `exceptions_owner_f144r.tsv` / `decode_owner144.json` -> `reading_f144r_owner.txt`, decode --check exit 0,
f.144r H 0 C 0 S 39 M 32 I 0 U 19 (was S 42 M 34 U 14). Nothing changed on f.117r or f.168.
