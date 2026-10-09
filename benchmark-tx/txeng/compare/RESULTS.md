# TXE-A: compare, don't recall -- RESULTS (LANE TX-ENGINEER round 2, instrument A; 9 Oct 2026, account 4, Opus 5.5)

**Verdict: FAIL on dev_tune.** Fixed 4, broken 16 (sign test p = 0.0118, in the wrong direction), against the gate
"fixed > broken, p < 0.01" (PREREG-txeng-2.md, as amended at 1e23073e). Eval_heldout was **not run**, following the PREREG
("Not met -> FAIL, no eval"). Fable arm not run (the Opus dev gate was not met). Shelf: weak.

## Pre-registered gate
benchmark-tx/PREREG-txeng-2.md "Instrument A" and its "Amendment": dev_tune fixed > broken with paired sign test p < 0.01 vs
L_dev_tune (`benchmark-tx/txeng/units/labels_dev_tune.tsv`); if met, eval_heldout once. Show rule unchanged from the PREREG:
shown when atlas top-1 != L sign, or top-1 share < 0.6, or L merged confidence M/L.

## What was built
- `tools/tx_compare.py` (map / build / resolve / lattice-out), test `tools/tests/test_tx_compare.py` (offline, passes).
- Candidates: `glyph_atlas.py classify --topk 3 --holdout f178r_ --holdout f178v_ --holdout f179r_` ->
  `topk_no87_allheld.tsv`. Box <-> position: `box_pos.tsv`, made by the label-blind width DP of atlas/no87_map.py, run against
  the line read's positions (798 1:1, 39 2:1, 16 1:2). No truth column was read.
- Merged confidence: harvest/f178v/passC_agreement.tsv (L01-10), **plus harvest/f178v/passC_L11-23_agreement.tsv** (L11-23;
  the brief named only the first file, which stops at L10), plus harvest/f179r/passC_agreement.tsv. Each file is aligned to
  the line read per line with difflib. A position with no merged confidence on file counts as M (doubtful).
- Exemplars: atlas/sheet_truth/sheet.tsv "hand" tiles. A code with fewer than 2 such tiles is filled from boxes on
  non-no.87 pages labelled by cluster (labels.json "signs" only, never "override"). A code with neither shows a blank grey tile.
- Deviations: (1) the context tile is scaled so the target sign is 90 px tall, capped at 4x, instead of a flat 4x. At native
  resolution (signs about 68 px), a flat 4x on 16 rows made a 5,800 px sheet that the reader would see heavily downscaled.
  (2) Vertically, the context tile keeps the target's own band, marks above included. (3) Sheets are saved as greyscale PNG.
  (4) A shown position with fewer than 2 distinct candidates (L sign == the only non-'_' top-3 code) is counted as
  "undecidable" and not shown: dev 15, eval 4.

## Counts
| unit | positions | shown | sheets | unmapped | undecidable |
|---|---|---|---|---|---|
| dev_tune | 354 | 165 | 11 | 8 | 15 |
| eval_heldout | 402 | 167 | 11 (built, never read) | 8 | 4 |

The brief estimated about 3 sheets per unit. The lane raised the cap to 25 (box 150) and kept the show rule unchanged.
Dev shown, by reason: conf only 65, top1 only 52, top1+conf 25, top1+share 12, top1+share+conf 5, share 5, share+conf 1.

Reads (dev, 165 rows): pick H 81 / M 52 / L 8; none 24 (H 1, M 12, L 11). Resolve: kept L's sign 93, changed 48, none 24.

## Reader task text (one Opus 5.5 subagent call per sheet, `model: opus`)
> Read only <abs path>/benchmark-tx/txeng/compare/dev_tune/sheet_NN.png. For each numbered row, which numbered candidate (1..k)
> matches the boxed sign in the leftmost tile, or none? Write <abs path>/benchmark-tx/txeng/compare/dev_tune/reads_NN.tsv:
> row, pick, conf (H/M/L), note. Do not open any other file.
>
> (Format: a tab-separated file with header line "row	pick	conf	note"; pick is a candidate number or "none". Do not commit
> or push. Reply with one line when done.)

Calls: 11 (dev), 0 eval, 0 Fable. Subagent tokens from the task notifications: 1,066,351 in total (95.7k-97.7k per call,
almost all of it session context rather than the image). Raw reads were committed at 3dcf4f7ee (sheets 1-8) and then in the
"dev_tune raw reads complete" commit, both before any resolve or score.

## tx_bench (dev_tune, paired vs L_dev_tune)
```
birago1572-no87 [eval] err_true 0.093 (32/343) 95% 0.067-0.129 | wrong 20 deleted 6 inserted 6 | excluded 11 | lines missing 17
  top confusions (truth value <- read): s<-T50 x3, i<-T38 x3, e<-T36 x2, e<-T76 x2, e<-<deleted> x2, g<-T42 x1, h<-T13 x1, t<-T90 x1
split eval: err_true 0.093 (32/343) 95% 0.067-0.129
paired passG_compare_dev_tune.tsv vs labels_dev_tune.tsv on birago1572-no87: 343 common scored signs; base wrong 14, output wrong 26; fixed 4, broken 16; sign test p = 0.0118
```
(tx_bench labels the split "eval"; the lines are the dev_tune unit, f178v L01-12.)

Secondary, reported only (`key_decode_lattice.py decode dev_tune/topk_weighted.tsv --key harvest/key_1572_sheet.tsv --lang it
--lam 4`, converted with `tx_compare.py lattice-out`):
```
paired passG_compare_dev_tune_lattice.tsv vs labels_dev_tune.tsv on birago1572-no87: 343 common scored signs; base wrong 14, output wrong 31; fixed 4, broken 21; sign test p = 0.0009
```

## Which class moved (tools/tx_taxonomy.py, dev_tune/taxonomy.md; run after the reads were committed)
- The shown set did hold most of L's errors: **11 of 14 were shown**. The atlas+reader fixed 4 of them: two where L read T98
  (-> T18, truth set T18|T63, a d/s case; -> T36, truth set T36|T50), one p/t (L T92 -> T53) and one T60 -> T86. Class 1 moved a little in the right direction.
- The cost was larger. All **16 broken positions were shown positions** where L was right and the reader picked another
  shown candidate: T80 -> T38 x3 (i <- T38), X_CE/T92 -> T50 x3 (s <- T50), T64 -> T13, T60 -> T86, T24 -> T19 and others.
  Some appear as `<deleted>` because tx_bench's realignment scores a changed sign as delete plus insert. The reader prefers a
  candidate whose clean exemplar resembles a degraded or ligature form. When L, which saw the whole line, was right, a forced
  choice among look-alike exemplars overrode it.
- Still wrong in both L and G: 10 positions, including n/e T76 x4. These are the floor positions; the atlas top-3 did not
  carry the truth there, so the reader could not choose it.
- The error-correlation table shows G repeats 10 of L's 14 errors (8 with the same wrong sign).

## Shelf
`tx_compare.py`: weak. Dev FAIL, fixed 4 / broken 16 (p 0.0118 against), lattice fixed 4 / broken 21. Eval not run.

## Follow-ups (one line each, not done)
- Untested here (not pre-registered): let a pick override L only at H confidence, and/or only at top1-disagreement rows
  (not conf-only rows); and show L's own rendered sign as a candidate tile so "keep" is a visible choice.
