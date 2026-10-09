# TXE-M2: feature-first in two calls, with a compliance gate (LANE TX-ENGINEER, idea M24 retest; account 4, Opus 5.5; cap 8, box 90 min)

Read `.claude/briefs/runs/2026-10-09-account4-txe-COMMON.md` first, then `benchmark-tx/txeng/feature/RESULTS.md` (TXE-M:
a NON-TEST -- one reader script-filled the features from the cell it had already picked, 167/167 rows matching the cell
table; the other wrote features that matched the table on 35/185 and said it had not read them from the ink) and
`benchmark-tx/PREREG-txeng-2.md` (units, blindness, Amendment: gate p < 0.01). Why this job exists: the idea was never
tested, because a single call that sees the sheet and the feature table lets the reader name the cell first and fill the
features backwards. The retest separates the two acts into two calls and measures compliance before any score.

## Pre-registration (write `benchmark-tx/txeng/feature/PREREG-M2.md` and push it BEFORE any read)
- Unit: dev_tune (f178v L01-12), the ordinary line crops (harvest/f178v/f178v_L01..L12_s?.jpg). Reuse TXE-M's
  `tools/tx_features.py` (cells table, norm, consist) -- extend, do not fork.
- Call 1 (features only; NO sheet, NO cell table, NO sign names in the task): per line crop set, the reader writes one row
  per sign: pos, descender (none/short/long), ascender (none/short/long), bars (0/1/2), loops (0/1/2), dots (0/1/2+), lean
  (left/upright/right), tail (none/left/right), conf. Two Opus 5.5 subagent calls (L01-06, L07-12). Raw to
  `benchmark-tx/txeng/feature/m2_features_*.tsv`, committed.
- Compliance gate (read-free, before any cell call): (a) the feature rows' sign count per line within 10% of pass A's; (b)
  the written features are not constant (every column has at least two values used on >= 10% of rows); (c) on the 51 sheet
  cells' own printed shapes, run the SAME call-1 task once on `sign_sheet_blind_1572.png` cut into cell tiles (a control: a
  reader writing features from ink should match the script-derived cell table on >= 70% of cells). If (a), (b) or (c)
  fails: stop, log "non-test: no compliant feature read", no cell call.
- Call 2 (cell naming): the reader gets the crops, the sheet, the cell-feature table AND its own call-1 feature rows
  (pasted as a TSV), with the task "for each position, name the cell whose table features match your written features;
  where none matches within one feature, write the nearest cell and flag `mismatch`". Two calls. Raw committed; normalise
  -> `benchmark-tx/outputs/birago1572-no87/passU2_feature_dev_tune.tsv`.
- Gate: `tools/tx_bench.py passU2_feature_dev_tune.tsv ... --paired benchmark-tx/txeng/units/passA_dev_tune.tsv` fixed >
  broken, p < 0.01; vs labels_dev_tune.tsv reported. Met -> eval_heldout once (four calls), the eval look. Not met -> FAIL.
  Secondary: do `mismatch` flags predict L's wrong positions (recall at flag share; a sorter signal)?

## Report
`benchmark-tx/txeng/feature/RESULTS-M2.md`: the compliance table (a, b, c), the gate lines, the mismatch table,
`tools/tx_taxonomy.py` on passU2 vs A and L (after commit), task texts, calls (dev 5 incl. the control, eval 4 at most).
Results-log row in research/TX-IDEAS-2026-10-09.md (id M24-retest; rebase before editing); shelf regrade of tx_features.py
from the result. Cap 8; stop before a call that crosses 80% of cap or box. Report in a short paragraph (first line:
compliance a/b/c, then dev fixed/broken/p vs A) and stop.
