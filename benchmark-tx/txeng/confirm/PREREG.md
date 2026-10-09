# TXE-Q pre-registration: the confirm item read ONCE with today's pipeline (9 Oct 2026, written 08:31 UTC by date -u)

Job TXE-Q, worker of LANE TX-ENGINEER (account 4, Opus 5.5), brief `.claude/briefs/runs/2026-10-09-account4-txe-q.md`;
PREREG-txeng-3 "Decision" (round 3 item 3, Amendment 2 guard 2). Pushed before any read.

## Item and what was opened
BENCHMARK-TX.tsv row `spinelli-c1519-confirm` (split=confirm, Beinecke GEN MSS 109 Filza 163, Tommaso Spinelli,
Barcelona c.1519; 10 lines p1c_L01-08, p2c_L01-02; 259 ref signs, 193 scored). Opened before scoring: the row, the
builder's docstring (`benchmark-tx/build_spinelli_confirm.py` lines 1-60: vocabulary and line ids), the folder's file
listing, NOTES.md sections on crops/blind protocol (H29b/H29c, H33b, H38/H40 method paragraphs), `glyphs/atlas.png`,
`glyphs/atlas_v2.png`, the code column of key.tsv and atlas*.tsv, the folder's crop overlays. **Disclosure:** a grep of
NOTES.md for v2 code names printed NOTES lines 357-359, an early (v1, Sonnet) transcription of p1 L1 and part of L2 in
a superseded vocabulary; the worker saw it, the readers never do (readers get crops and the sheet only). NOT opened:
the truth TSV, `benchmark-tx/outputs/spinelli-c1519-confirm/*` (committed.tsv opened only at scoring, for --paired),
ciphertext_v6.tsv, passes/*, any decode or reading.

## Crops (step 2)
The folder's own crops (`images/p1c_*`, `p2c_*`) are flat bands whose s1/s2 segments overlap by 1800 of 2400 px, and the
tool's slope fit on the same sources measures -77 to -142 px drift on 9 of 10 lines (L05 -10 px). So all lines are
re-cut, with follow-slope (the round-2 crop rule) plus the S0 options the brief names, into this job's own folder:
```
python3 tools/iiif_lines.py --image ciphers/spinelli-beinecke-c1515/images/src_2_10867298_450_440_3000_1740.jpg \
  --out benchmark-tx/txeng/confirm/crops --prefix p1c --max-width 1600 --overlap 120 --follow-slope 400 \
  --band-extent 0.1 --mask-neighbours --overlap-note --debug
python3 tools/iiif_lines.py --image ciphers/spinelli-beinecke-c1515/images/src_2_10867299_360_1997_3055_456.jpg \
  --out benchmark-tx/txeng/confirm/crops --prefix p2c --max-width 1600 --overlap 120 --follow-slope 400 \
  --band-extent 0.1 --mask-neighbours --overlap-note --debug
```
20 crops (10 lines x s1/s2, overlap 200 px p1 / 145 px p2 per crops_note.md); overlays checked: one green fit per line.
Known crop residue: neighbour-line fragments survive the mask at a few line ends (L04 top, L05 s2 right) -- the readers
are told to read the one full-width line only.

## Sheet, readers, grouping (step 3)
Sheet: `ciphers/spinelli-beinecke-c1515/glyphs/atlas.png` (atlas v3, 23 codes, exemplars only, no values) -- the sheet
of the folder's own blind Opus protocol H29b/H29c (93.1% pair agreement), with JHOOK offered by description as H29c did
("bold vertical stroke turning left at the foot") and `NEW:<description>` for any shape outside the sheet; `A/B?` for an
uncertain first choice with alternative. Two blind Opus 5.5 reader subagents (passA, passB), each ONE call with the
sheet plus all 20 crops; task text names only the sheet, the crops, the overlap rule and the output path; output long
TSV line, pos, sign, conf (H/M/L). The plain words at the start of p1 L01 are skipped (readers told: Latin-script words
are not cipher). No relabel map for shapes is made.

## Reconciliation (step 3)
`python3 tools/reconcile_passes.py passA.tsv passB.tsv --crops benchmark-tx/txeng/confirm/crops --out-dir
benchmark-tx/txeng/confirm/rec --keep-alts`; disagreements.tsv + uncertain.tsv go to ONE Sonnet third-reader call
(crops + sheet, each row with its agreed left/right neighbours as landmarks, choose among the passes' readings or
`NEW:`), applied mechanically by the worker -> `benchmark-tx/outputs/spinelli-c1519-confirm/passZ_pipeline.tsv`
(line, pos, sign). Raw passes, reconciliation and passZ committed and pushed before scoring.

## Vocabulary and the label map (declared before any read)
Truth members are key.tsv codes, which are atlas v3 codes plus the H38/H40 split suffixes (CODE_CELL, build_v5_split /
build_v6_split naming): the readers, given the v3 sheet, cannot write a split code. Per tx_bench's own --label-map
doc ("a reader given a coarser label inventory than the reconciler ... scored on glyph identity"), scoring uses
`benchmark-tx/txeng/confirm/collapse_map.tsv`, built mechanically: every key.tsv code containing '_' maps to the part
before its first '_' (HOOK_A->HOOK, SEVEN_I_M2->SEVEN, EIGHTBAR_C->EIGHTBAR, TEE_P1->TEE, JHOOK_M2->JHOOK, ...). It
renames notation only; no shape is reassigned. Both numbers are reported; the HEADLINE is the mapped one. A `NEW:`
sign or a v2-only shape (DEE, MU, OMEGA2, STROKE, EPSILON) at a scored position counts wrong (lower-bound honesty:
the pipeline's own vocabulary limit is part of its error).

## Gate (one look)
Score ONCE: `python3 tools/tx_bench.py benchmark-tx/outputs/spinelli-c1519-confirm/passZ_pipeline.tsv --bench
BENCHMARK-TX.tsv --item spinelli-c1519-confirm --label-map benchmark-tx/txeng/confirm/collapse_map.tsv --paired
benchmark-tx/outputs/spinelli-c1519-confirm/committed.tsv`, then the same unmapped; also passA and passB alone
(reported, not a second look at the pipeline); then `tools/tx_taxonomy.py` on passZ. No threshold is attached: the
number is the campaign's confirm figure (guard 2) for this leaf only, never a result for the hand beyond it. Nothing is
re-read or re-adjudicated after scoring.

Budget: 2 Opus calls + 1 Sonnet call; cap 12 USD, box 08:26-10:26 UTC (80% 10:02).
