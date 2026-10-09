# PREREG TX-ENGINEER-2 round 8 (lane incarnation 2, session_011EV9AKeJ4YuU9jjghdUy6F, 9 Oct 2026 20:4x UTC by date -u; pushed BEFORE any read or score; pool 23 under Amendment 6, no eval look possible this round)

Rules as PREREG-txeng2-5's preamble. `tools/tx_register.py --check` passes on this file before any spawn. TXE2-REGFIX
(a tool fix, TX-RED F25) runs from the round-8 brief only; it is not an experiment.

## X1b-v4 Off-sheet recall tables re-derived against the passZ_v4 baseline, read-free (TXE2-SHEET3; Opus 5.5; cap 2; TX-RED F24)
Nearest prior: X1b / TXE2-SHEET2 (Spinelli recall 8/14 at 14.9% against passZ_pipeline, 7 of 8 carried by pass A's NEW
flags), B1 / TXE2-BASE-SPIN (the new baseline: 6 flagged-excluded errors, 3 of them adjudicated NEW: shapes). What is
different: no new instrument -- the same `tools/tx_offsheet.py detect` + `recall --exclude-flagged` re-run with passZ_v4
(and passA_v4 / passB_v4) as the baseline passes and the flags file of V2, so X1c's reachability sentence rests on the
current baseline; also the reader-NEW-flag share of the catches under atlas_v4. Spinelli only (f152r and eval_heldout
baselines are unchanged). Gate: none (a recall table; openings of eval truth: 1). Output: benchmark-tx/txeng2/txe2-sheet3/
RESULTS.md with the table beside X1b's, sha256 beside every commit hash.

## A2 Reader-sheet audit across every folder, read-free (TXE2-SHEETS-ALL; Opus 5.5; cap 3; owner's question of 20:2x via the orchestrator)
Nearest prior: A1 / TXE2-SHEETAUDIT (benchmark items only: Spinelli atlas v3 3 mislabelled; every other benchmark sheet
printed-key or text list), V2 (the finding), X1 (sheet inventory as an instrument -- this is not one). What is different:
scope -- every reader sheet or atlas in use anywhere under ciphers/ (sign_sheet*.png, atlas*.png/tsv, glyphs/*, sorter
exports) classified printed-key / text-list / atlas-built-from-boxed-tiles; for every atlas-built sheet whose folder holds
a known-answer truth of any grade (a *.truth.tsv, a clerk sheet alignment, an H-graded decode with a period key), cross
each exemplar's box id against that truth and list every exemplar whose value is not the cell it illustrates; where no
truth exists, list the sheet as "unverifiable, atlas-built" with its tile count. No sheet is corrected in this job (a
correction is a per-folder baseline change, pre-registered by the folder's own lane); no reader, no host. Openings of eval
truth: 0 (benchmark eval items are covered by A1 and are not re-opened). Output: benchmark-tx/txeng2/sheets-all/RESULTS.md
with one row per sheet and the list of mislabelled exemplars, sha256 beside every commit hash.

Costs this round: 2 + 3 + REGFIX 3 = 8. Eval looks this round: 0.
