# PREREG TXE-M2: feature-first in two calls, with a compliance gate (LANE TX-ENGINEER, idea M24 retest; 9 Oct 2026, 08:2x UTC by date -u; pushed BEFORE any read)

Brief `.claude/briefs/runs/2026-10-09-account4-txe-m2.md`; binds `benchmark-tx/PREREG-txeng-2.md` (units, blindness, Amendment:
single-instrument gate p < 0.01, one eval look). Why: TXE-M (RESULTS.md) was a non-test -- one call saw the sheet and the
table, and the reader named the cell first and filled the features backwards. Here the two acts are two calls, and
compliance is measured before any cell is named. Tool: `tools/tx_features.py` extended (tiles, task1, comply, task2), not forked.

## Unit and material
dev_tune = f178v L01-L12, pass A's crops `ciphers/nevers-birago-fr3251-1572/harvest/f178v/f178v_L01..L12_s1..s3.jpg`,
grouped as pass A (L01-06, L07-12, 18 crops each). Readers: Opus 5.5 subagents (`model: opus`), one call each.

## Call 1: features only (no sheet, no cell table, no sign name in the task)
Tasks `m2/task1_c1.md`, `m2/task1_c2.md` (tools/tx_features.py task1): the crops, the overlap rule of the 1572 blind brief
(its wording, sheet references removed), the seven-feature vocabulary of TXE-M (desc, asc, bars, loops, dots, lean, tail)
with the same definitions, one row per sign: `passage pos desc asc bars loops dots lean tail conf note`.
Raw: `reads/m2_features_c1.tsv`, `reads/m2_features_c2.tsv`, committed and pushed before any further call.

## Control (gate c): the same task on the printed sheet's 51 cells
`m2/control_tiles.png` (tools/tx_features.py tiles, seed 20261009): the 51 cells cut from `sign_sheet_blind_1572.png`
WITHOUT their labels, renumbered 1..51 in a seeded order, 2x; tile -> cell map `m2/control_tile_map.tsv` (never given to a
reader). Task `m2/task1_control.md` (task1 --tiles): the same vocabulary and definitions. Raw `reads/m2_features_control.tsv`.

## Compliance gate (read-free; `tools/tx_features.py comply`; run before any cell call; exit 0 = compliant)
- (a) on every one of the 12 lines, call 1's sign count is within 10% of pass A's (`units/passA_dev_tune.tsv`).
- (b) feature variety: every feature column has at least two values each used on >= 10% of rows. Registered deviation
  from the brief's wording, decided on the cell table alone before any read: a column that is itself constant by this
  test in the cell table is exempt -- `dots` is 0 on 50 of 51 cells (one value only), so an honest ink read can be
  expected to fail it; the other six columns all pass it in the table (desc, asc, bars, loops, lean 3 values; tail 2).
- (c) control: tiles whose written features differ from `cell_features.tsv` in AT MOST ONE of the seven features
  (the same one-feature tolerance as call 2's `mismatch` rule) >= 70% of the 51 tiles. Exact 7/7 agreement and
  per-feature agreement are reported, not gating.
Any of (a), (b), (c) fails -> stop; log "non-test: no compliant feature read"; no cell call, no score.

## Call 2: cell naming from the reader's own features
Tasks `m2/task2_c1.md`, `m2/task2_c2.md` (tools/tx_features.py task2): the crops, the sheet, the cell-feature table and
call 1's rows for those lines pasted as TSV; "for each position, name the cell whose table features match the written
features; where none matches within one feature, write the nearest cell and flag `mismatch`"; one output row per input
row. Raw `reads/m2_cells_c1.tsv`, `_c2.tsv`, committed and pushed before scoring; normalised (tx_features.py norm) ->
`benchmark-tx/outputs/birago1572-no87/passU2_feature_dev_tune.tsv`.

## Gate (fixed now)
`python3 tools/tx_bench.py benchmark-tx/outputs/birago1572-no87/passU2_feature_dev_tune.tsv --bench BENCHMARK-TX.tsv --item
birago1572-no87 --paired benchmark-tx/txeng/units/passA_dev_tune.tsv`: PASS iff fixed > broken and p < 0.01. Vs
`labels_dev_tune.tsv` reported. Met -> eval_heldout once (four calls: two feature, two cell; compliance (a)(b) re-run on
eval), paired vs passA_eval_heldout.tsv, the one eval look. Not met -> FAIL, no eval.

## Secondary (descriptive, after commit)
Do the `mismatch` flags predict U2's wrong positions? Recall of wrong positions among flagged rows vs the flag share
(wrong positions from tx_taxonomy err rows, after the reads are pushed). `tools/tx_taxonomy.py` on U2 vs A and L.

## Calls and stops
Dev 5 (control 1, features 2, cells 2), eval 4 at most. Cap 8, box 08:11-09:41 UTC; stop before a call that would cross
80% of either (6.4; 09:23).
