# TXE2-CELLS: lattice-proposed cells, image-checked at 4x, no exemplar (PREREG-txeng2-3 X13; 9 Oct 2026, 17:14-17:2x UTC by date -u)

LANE TX-ENGINEER-2, account 4, Opus 5.5 worker. Brief `.claude/briefs/runs/2026-10-09-account4-txe2-round3.md`. Dev only
(dev_tune, f178v_L01-12); **no eval look**, no truth file edited, no tool in `tools/` changed (harness here only).

**Verdict: FAIL (dev), the wrong way.** Real arm vs L_dev_tune: fixed 2, broken 14, sign test p = 0.0042 (output wrong 24 vs
base 12; err_true 0.070 vs 0.035). Registered control (alternative replaced by a random sheet cell, seed 1): fixed 0,
broken 0, p = 1.00 -- does not pass, as required. The control is what makes the failure informative: offered L and a
random cell, the reader never picked the random cell (A/B picks 35, all L; neither 12, ? 2); offered L and the lattice's
top alternative, it moved 19 of 49 and was wrong at 14 of those moves.

Order kept: row images + keys committed e785fb59b before any read; real reads 5e1be8bd9 and control reads ece18953c committed
before scoring; resolved outputs 79da9cba3 before tx_bench.

## Rows (`build_cells.py build`)
- Positions: the X9 combo feed (latt OR vote OR selfcons in `txeng2/doubt/dev_tune_signals3.tsv`) = 54; 5 have no 1:1 atlas
  box in TXE-C's label-blind DP (`txeng/pair/dev_tune/box_pos.tsv`) and keep L unseen (L03.24, L08.26, L09.29, L10.22,
  L11.32); 0 lack a lattice alternative. **49 rows**, 44 of them scored by tx_bench; L is wrong at 10 of the 44 (of its 12
  dev errors; the other 2 sit outside the feed or at an unboxed position).
- Row image (`rows/<arm>/row_NN.jpg`): the boxed tile at 4x (zoom 4.0, autocontrast) with +-1 neighbour
  (`tx_pair_reread.context_tile`), and the printed names "A = T##, B = T##" (A/B order seeded per row). Cell B/A = L's sign
  and lattice d's best candidate != L (`txeng2/latt/topk_d.tsv`). Off-sheet names (X_CE, X_NEW) print as "off-sheet form
  (no cell)". Reader reference: `harvest/sign_sheet_blind_1572.png` only; no exemplar tiles, no values.
- Control: the alternative replaced by `random.Random(1).choice` over the 51 sheet ids minus L and the alternative, in row
  order; identical tiles and A/B order rule.

## Calls (Opus 5.5 subagents, value-blind)
Real: 4 calls (rows 1-13, 14-25, 26-37, 38-49). Declared deviation: the PREREG said "<= 16 rows per call (3 calls)"; 49 rows
need 4 calls at <= 16, the <= 16 bound was kept. Control: 1 call on all 49 rows, as registered ("one call") -- so the control
call carried 3-4x the rows of a real call; a heavier call could only make the control noisier, and it moved nothing.
Subagent tokens reported: real 113.9k / 115.4k / 113.8k / 114.5k, control 163.2k. Cost: the orchestrator get_session reading.

## Score (tx_bench, dev_tune, vs `txeng/units/labels_dev_tune.tsv`)
```
passX13_real    err_true 0.070 (24/343) 95% 0.048-0.102 | paired vs L: 343 common; base wrong 12, output wrong 24; fixed 2, broken 14; p = 0.0042
passX13_control err_true 0.035 (12/343) 95% 0.020-0.060 | paired vs L: 343 common; base wrong 12, output wrong 12; fixed 0, broken 0; p = 1.0000
```
Picks (resolve): real A/B -> L 22, -> alternative 19, neither 6, ? 2; control A/B -> L 35, -> random cell 0, neither 12, ? 2.

## Movement (post-hoc `diag.py` -> `movement_real.tsv`, `movement_control.tsv`; after the scores, not a gate)
- Fixed (2): L06.18 T98 -> T18 (d), L10.1 T92 -> T53.
- Neutral moves (2): L01.3 and L01.8 T95 -> T51 (both in the truth set); L10.31 T98 -> T18 wrong either way.
- Broken (14): **5 x X_CE -> T50** (the curled Ce s, L01.23 L03.4 L04.4 L08.10 L10.5: the same three-plus breaks TXE-E and
  TXE2-LATT took -- the off-sheet s has no cell, and its nearest named cell wins whenever it is offered); **3 x T13 -> T64**
  (L01.26 at H, L07.25, L09.9; readers said the superscript placement decides); **3 x T42 -> X_NEW** (L05.7, L08.3, L08.5: a
  t-like form read as off-sheet against T42's flat bar); T26 -> T76 (L01.13), T56 -> T85 (L11.11, H), T42 -> T83 (L11.22, H).
- L's 10 wrong rows: 2 fixed, 1 moved still wrong, 7 kept (4 x T76 vs T86/T26 kept L, incl. 2 at H; T60 vs T86 "neither" at H;
  T90 vs T53 kept T90 at H; T64 vs T13 kept T64).
- Confidence does not separate: H moves 3, all broken; M 13 moves; L 3 moves.

So the cell names plus the blind sheet do not let the reader choose between L and a look-alike the lattice proposes: the
choice it makes is close to a coin toss biased toward the alternative (19 of 41 A/B picks), and since L is right at 34 of the
44 scored rows, any such move rate breaks more than it fixes. The control shows the reader does reject an unrelated cell, so
the failure is discrimination between near look-alikes at sheet resolution (51 cells on a 990 x 660 sheet, about 100 px per
cell against a 4x tile), not inattention.

## Follow-up (one line, not done)
The sheet cell is the limit: any further cell-choice instrument on no.87 needs a reference rendered at the tile's scale (or the
off-sheet X_CE made a keyed cell, TXE2-LATT's follow-up) -- a different instrument, not another pass at this one.

Calls 5 Opus vision (4 real, 1 control); 0 network requests; 0 eval items scored.
