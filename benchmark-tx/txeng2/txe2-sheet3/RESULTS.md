# TXE2-SHEET3 (PREREG benchmark-tx/PREREG-txeng2-8.md X1b-v4) -- Spinelli off-sheet recall against the passZ_v4 baseline: 5 of 6 flagged-excluded errors caught, all 5 through the readers' NEW: flags; 1 consensus misread on-sheet

Worker TXE2-SHEET3 (account 4, Opus) for LANE TX-ENGINEER-2 incarnation 2, 9 Oct 2026, 20:45-20:5x UTC by date -u.
Cost: the orchestrator's get_session reading.

Openings of eval truth: 1 (recall table)

**Read-free.** No vision call, no reader, no subagent, no network beyond git, no new instrument, no truth file edited.
This is a flag-vs-error recall table, not an eval look at an instrument. It has no gate (PREREG-8 X1b-v4). Spinelli only.
The f152r and eval_heldout baselines have not changed, so X1b's rows for them stand.

## What ran
- The config is X1b's `txe2-sheet2/items/spinelli-c1519-confirm.json` with exactly three paths changed:
  skeleton_pass passA_txeq -> passA_v4, and passes passA_txeq/passB_txeq -> passA_v4/passB_v4
  (`items/spinelli-c1519-confirm.json`). Crops, label map (`txeng/confirm/collapse_map.tsv`), band (null), q = 0.15 and
  knn = 3 are unchanged. passA_v4/passB_v4 are TXE2-BASE-SPIN's reads against `ciphers/spinelli-beinecke-c1515/glyphs/atlas_v4.png`.
  The atlas enters only through those reads, because `tx_offsheet.py detect` takes no sheet argument.
- Environment check before the run: re-running X1b's own config here reproduces its committed
  `detect_spinelli-c1519-confirm.tsv` byte for byte (cmp equal).
- `python3 tools/tx_offsheet.py detect benchmark-tx/txeng2/txe2-sheet3/items/spinelli-c1519-confirm.json --out
  .../detect_spinelli-c1519-confirm.tsv --debug-dir .../debug` reported 250 tiled positions, 37 flagged, 22 consensus
  cells, and 7 reader-flagged positions.
  These outputs were committed in **5fdd0ba99** (5fdd0ba99b1bb99235d1506e29c78da10e7c20a1) **before recall ran**.
  Their sha256 values are in `detect.sha256` (itself sha256 1945de65f9d51e00443fb11c825e21855cd678cd8d8b5d54dd2e960d12baadcc).
  The two key files: detect TSV 9113bfdc94cb94c6b80c895bb66086b3255129ce19af5c5ff5cc39b14d288bfc, config
  d4a5131b27e04e1c545d0a33ab2cb56445390cd5d7b43a429911c555431144c1.
- Recall ran once, in one process: `python3 benchmark-tx/txeng2/txe2-sheet3/recall_detail.py`. It calls
  `tx_offsheet.recall` as measured and with `--exclude-flagged` against baseline `outputs/spinelli-c1519-confirm/passZ_v4.tsv`.
  The truth's flag column is TXV-SPIN's V2 verdicts from `benchmark-tx/spinelli-c1519-confirm.flags.tsv`, already
  applied in the truth (2 FLAG rows: p1c_L01.5 reading-doubtful, p1c_L03.16 label-doubtful).
  The same process lists the errors (`errors_v4.tsv`). Chance P is binomial P(>= caught) at the scored flagged share,
  X1b's convention.

## Recall table, beside X1b's

| baseline (reads, sheet) | tiled | flagged (share tiled / scored) | errors | caught | recall | of which reader NEW/X_/? flag | score only | chance P(>= caught) |
|---|---|---|---|---|---|---|---|---|
| X1b: passZ_pipeline (passA/B_txeq, atlas v3), as measured | 248 | 37 (0.149 / 0.140) | 14 (2 untiled) | 8 | 0.571 | 7 | 1 | 0.0002 |
| X1b: same, flagged excluded (no flag column then) | | | 14 | 8 | 0.571 | 7 | 1 | |
| **X1b-v4: passZ_v4 (passA/B_v4, atlas_v4), as measured** | 250 | 37 (0.148 / 0.140) | 8 (0 untiled) | 5 | 0.625 | 5 | 0 | 0.0021 |
| **X1b-v4: same, flagged excluded (V2 flags)** | 250 | 37 (0.148 / 0.141) | **6** (0 untiled) | **5** | **0.833** | **5** | **0** | 0.0003 |

## The six flagged-excluded errors (`errors_v4.tsv`; positions are tx_offsheet's alignment)

| line.pos | truth | reads (A, B) | rank share | flagged | class |
|---|---|---|---|---|---|
| p1c_L02.26 | g | PHI, NEW:circle-on-stem | 0.376 | yes | reader NEW flag |
| p1c_L02.27 | u | JHOOK, NEW:long-s-crossbar | 0.464 | yes | reader NEW flag |
| p1c_L06.21 | u | JHOOK, NEW:long-s-crossbar | 0.144 | yes | reader NEW flag |
| p2c_L01.17 | g | PHI, NEW:circle-on-stem | 0.368 | yes | reader NEW flag |
| p2c_L02.3 | s | NEW:large-looped-H-flourish, JHOOK/NEW:long-slant-stroke? | 0.004 | yes | reader NEW flag (also the top score) |
| p2c_L02.7 | n | PHI, PHI | 0.380 | no | consensus misread, on-sheet |

**The sentence X1c needs.** Against the current baseline (passZ_v4, atlas_v4, V2 flags excluded), 5 of the 6 remaining
Spinelli errors are reachable by a sheet-grown read: all 5 sit at positions a reader marked NEW:. Those 5 are three
recurring shapes: circle-on-stem = g twice, long-s-crossbar = u twice, and one looped-H flourish = s. None of the 5 is
reachable by the off-sheet shape score alone, because the score adds 0 catches beyond the reader flags. The 6th
(p2c_L02.7, truth n) is a consensus misread on-sheet: both readers wrote PHI. The detector's blind spot holds here, and
no grown sheet built from flagged tiles reaches it.

## Reading
Moving to the v4 baseline halves the error pool (14 -> 6 flagged-excluded). Recall rises because the errors atlas_v4 fixed
were mostly consensus and untiled misses (X1b's 2 deleted h and 3 of its 4 consensus tiles are gone), not because the
detector improved. Score-only catches went from 1 to 0. As in X1b, the readers' own NEW: flags carry the result, here
completely. Spinelli only, never a figure for the hand beyond it. N = 6 errors, so the recall's interval is wide.
