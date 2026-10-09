# TXE-C: thin-stroke targeted re-read (LANE TX-ENGINEER round 2, instrument C; account 4, Opus 5.5; cap 8, box 100 min)

Read `.claude/briefs/runs/2026-10-09-account4-txe-COMMON.md` first, then `benchmark-tx/PREREG-txeng-2.md` "Instrument C".
Why this job exists: on Birago no.87 the thin third of the hand's strokes carries half of every reader's errors at a 29%
base (research/TX-TAXONOMY-2026-10-09.md class 3: pass A 8.5% error on thin vs 4.2% on mid/heavy; 5 of A's 8 d T18 / s T98
confusions are thin). The crops are native resolution, about 40 px a sign; the tick or tail that separates a look-alike pair
fades first. TX-VIEWS showed a whole re-pass repeats the first reader's errors (phi 0.71-0.76); UNA-BIR3252 (9 Oct 2026,
`ciphers/birago-fr3252-1571-72/harvest/f3637/PREREG-UNA.md`) read 5 of 6 known-answer splits right from per-sign 4x tiles.
So: a second look ONLY at thin signs whose line-read sign is in a named pair, shown as a pair of exemplar rows, asked
"A, B or neither" -- never a re-pass.

## Build `tools/tx_pair_reread.py` (subcommands select, build, resolve; --help; test tools/tests/test_tx_pair_reread.py)
Inputs (disk only, folder `ciphers/nevers-birago-fr3251-1572`): `atlas/signs.tsv` boxes, the page images (`atlas/crops/`
regenerable per atlas/README.md, else harvest `src_*.jpg` via `atlas/pages.py`), the line read L
(`benchmark-tx/outputs/birago1572-no87/labels.tsv`), exemplar tiles from `atlas/sheet_truth/sheet.tsv` (secure tiles on
non-no.87 leaves; for a code it lacks, boxes of non-no.87 pages by cluster label), and the pair list fixed in the PREREG:
T18/T98, T90/T53, T76/T66, T76/T86, T76/T45, T64/T95, T64/T51, T50/T36, T92/T95, T92/T98, T83/T24, T60/T86, T13/T64.
1. `select --unit dev_tune|eval_heldout`: map boxes to line positions label-blind (sequence alignment of boxes to the line
   read by order and x, as `atlas/no87_map.py` does -- never its truth column; write box_pos.tsv). Stroke measure per box =
   share of ink surviving a 3x3 erosion on the page image (`tools/tx_taxonomy.py` erosion_share: import it, do not copy);
   thin = the page's lowest tercile over all its boxes. Selected = thin AND L sign in a listed pair (a sign in several pairs
   gets the partner with the highest pair count in `harvest/confusion_1572.tsv`, or every partner as rows B and C -- choose
   one rule, state it, keep it). Print counts: boxes, thin, selected, per pair.
2. `build`: row = the sign at 4x, autocontrast, with one neighbour each side (box grown 50%) | exemplar row A: 3 secure
   tiles of the L sign | exemplar row B: 3 of the partner; A/B assignment seeded random per row, the row -> (A code, B code)
   key written to `benchmark-tx/txeng/pair/<unit>/sheet_NN.tsv` (not given to the reader). Sheets of at most 16 rows,
   `sheet_NN.png`, with a one-line legend "pick the exemplar row that matches the boxed sign".
3. Reader: one Opus 5.5 subagent call per sheet, task text: "Read only <sheet png>. For each numbered row, does the boxed
   sign in the leftmost tile match exemplar row A, row B, or neither? Write <path>: row, pick (A/B/neither/?), conf (H/M/L),
   feature seen. Do not open any other file." Raw reads to `benchmark-tx/txeng/pair/<unit>/reads_NN.tsv`; commit and push
   the unit's reads before resolving or scoring.
4. `resolve --unit U` -> `benchmark-tx/outputs/birago1572-no87/passJ_pair_<unit>.tsv` (line, pos, sign: A/B -> that
   code, neither/? -> L's sign).
5. Score (PREREG): dev first, `tools/tx_bench.py passJ_pair_dev_tune.tsv --bench BENCHMARK-TX.tsv --item birago1572-no87
   --paired benchmark-tx/txeng/units/labels_dev_tune.tsv`; gate fixed > broken, p < 0.05. Met -> eval_heldout once against
   labels_eval_heldout.tsv. Not met -> FAIL, no eval. Then `tools/tx_taxonomy.py` on L vs J (after the reads are committed)
   to say which pairs moved, each way. Also report, per pair, picks A / B / neither and how many changed L.

Offline test: a synthetic page with three boxes of known erosion share (a hairline, a mid stroke, a blob) and a line read
in which the hairline's sign is in a listed pair: select returns exactly that box; build writes one sheet and its key;
resolve applies A/B and keeps L on neither. Shelf and SYSTEM rows (grade from your own result). Vision calls: dev about 2,
eval about 2, x about 1.5; cap 8; stop before a call that crosses 80% of cap or box. Report in a short paragraph (first
line: the verdict with dev and eval fixed/broken/p and the selected count) and stop.
