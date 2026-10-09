# TXE-S: cross-target exemplar library, two-reader-agree compare -- RESULTS (LANE TX-ENGINEER, ideas O7 + O8; 9 Oct 2026, account 4, Opus 5.5)

**Verdict: FAIL on dev_tune.** Two-reader-agree rule: **fixed 0, broken 7** (sign test p = 0.0156, in the wrong direction)
against the gate "fixed > broken, p < 0.01" (PREREG.md da11d0e6d). Eval_heldout was **not run** (looks 0). This was the third
compare run at TXE-A's show rule (TXE-A, the M1b re-resolutions, TXE-S), so under rule 3's third-attempt clause **the compare
family is retired**. Owner's items 7 (cross-target library) and 8 (sibling-leaf tiles in a compare layout) now have a tested
verdict on Birago no.87: the library is built and works as a tool, but shown in this layout it does not correct the line read.
Shelf: weak.

## Pre-registered gate
benchmark-tx/txeng/library/PREREG.md (pushed at da11d0e6d, before any sheet existed): `passG2_library_dev_tune.tsv --paired
labels_dev_tune.tsv`, fixed > broken and p < 0.01. Met: eval once. Not met: FAIL, no eval, compare family retired.

## tx_bench (dev_tune, paired vs L_dev_tune)
```
birago1572-no87 [eval] err_true 0.073 (25/343) 95% 0.050-0.105 | wrong 17 deleted 4 inserted 4 | excluded 11 | lines missing 17
paired passG2_library_dev_tune.tsv vs labels_dev_tune.tsv on birago1572-no87: 343 common scored signs; base wrong 14, output wrong 21; fixed 0, broken 7; sign test p = 0.0156
```
Single readers by the TXE-A rule (any pick overrides L), information only:
```
paired passG2_library_dev_tune_r1.tsv vs labels_dev_tune.tsv: base wrong 14, output wrong 20; fixed 1, broken 7; sign test p = 0.0703  (err_true 0.070)
paired passG2_library_dev_tune_r2.tsv vs labels_dev_tune.tsv: base wrong 14, output wrong 22; fixed 0, broken 8; sign test p = 0.0078  (err_true 0.076)
```
(tx_bench labels the split "eval"; the lines are the dev_tune unit, f178v L01-12.)

## Library (per-code tiles: printed cell + secure tiles / secure pool on non-no.87 pages with an image on disk)
`tools/tx_compare.py library --out-dir benchmark-tx/txeng/library/lib`: 51 codes, 151 tiles, 31 codes with the full 4.
```
T10:1/0 T11:1/0 T13:2/1 T15:1/0 T17:2/1 T18:4/5 T19:4/33 T24:1/0 T25:4/35 T26:4/5 T27:4/6 T29:3/2 T33:4/28 T36:4/19 T37:4/44
T38:1/0 T42:1/0 T45:4/36 T46:1/0 T49:4/4 T50:4/4 T51:1/0 T52:4/3 T53:4/33 T54:4/3 T55:4/28 T56:1/0 T57:4/5 T58:4/29 T60:4/39
T63:4/12 T64:1/0 T65:4/9 T66:1/0 T70:4/13 T76:4/16 T78:1/0 T80:4/16 T81:4/6 T83:4/11 T84:1/0 T85:4/42 T86:4/23 T88:1/0
T89:4/9 T90:4/8 T92:1/0 T95:2/1 T96:4/31 T97:3/2 T98:4/17
```
Printed cells: sources/cryptiana/web/img/NeversBirago.png (Tomokiyo's reconstruction of the 1572 key), cut at the boxes in
harvest/sign_id_map_1572.json. Secure tiles: atlas/secure_tokens.tsv (S grade), farthest-point on glyph_atlas classify
features, trim 0.2. Other family targets with H/C box tiles: none found (PREREG). **Deviation:** 57 of the 636 secure tiles sit
on f184v (45) and f185r (12), whose page images are not on disk (atlas/pages/ is gitignored and absent), so no tile can be cut
from them; the pool is 579. 20 codes have only the printed cell (T38, T64, T92 among them, which TXE-A's broken rows involved).

## Counts
dev_tune positions 354, shown 165 (unmapped 8, undecidable 15); first 5 sheets read = 120 positions (45 shown positions past
sheet 5 keep L, as pre-registered). 10 reader calls (R1 x 5, R2 x 5), Opus 5.5, about 105k subagent tokens each.

## Two readers: agreement table (120 read rows)
| R1 \ R2 outcome | same pick | both none | different |
|---|---|---|---|
| rows | 104 | 13 | 3 |

Agreement 117/120 = 97.5%. Under the agree rule: kept L 81, changed 23 (10 of them on scored positions after tx_bench
alignment; the rest are on excluded positions or are realignment artefacts of the same change). Two of the ten scored changes
went to another sign in the truth set (T42 -> T17 x2, neither fixed nor broken); one moved an already-wrong L to another wrong
sign (L05.9 T64 -> T13); seven broke a right L read (T19 -> T83, T10 -> deleted, T60 -> T37, X_CE -> deleted, T86 -> T60,
T86 -> deleted, T90 -> deleted).
Near-total agreement means the second reader is not independent in the way that matters: both are pulled by the same
exemplar resemblance, so requiring agreement did not filter the look-alike pulls that sank TXE-A.

Sorter signal (read-free after commit): among the 117 scored read rows, L was wrong at 1 of the 10 rows where the joint pick
differs from L (10%) and at 5 of the 107 where it keeps L (4.7%). No usable signal at this N. 6 of L's 14 dev errors were in the
read set; the joint pick fixed none of them.

## Which class moved (tools/tx_taxonomy.py, taxonomy.md / taxonomy_positions.tsv; run after the reads were committed)
- G2 repeats **all 14** of L's errors (13 with the same wrong sign) and adds 7. R1 and R2 each repeat 13-14 of L's errors.
- Class 1 (inventory look-alikes, n/e T76 x3, d/s, p/t) did not move: the floor positions stay wrong in every pass (13 positions
  wrong in all four passes). The new errors are look-alike substitutions at positions where L was right (T60 -> T37, T86 -> T60,
  T19 -> T83), which is the TXE-A failure again under the stricter rule.

## Reader task text (one Opus 5.5 subagent call per sheet, `model: opus`; R1 writes to reads_r1/, R2 to reads_r2/)
> Read only <abs>/benchmark-tx/txeng/library/dev_tune/sheet_NN_a.png and <abs>/benchmark-tx/txeng/library/dev_tune/sheet_NN_b.png
> (one sheet in two halves; rows numbered continuously). For each numbered row, which numbered candidate (1..k) matches the boxed
> sign in the leftmost tile, or none? Write <abs>/benchmark-tx/txeng/library/dev_tune/reads_rX/reads_NN.tsv: row, pick, conf
> (H/M/L), note. Do not open any other file.
>
> (Format: a tab-separated file with header line "row	pick	conf	note"; pick is a candidate number or "none". Do not commit or
> push. Reply with one line when done.)

Commits: PREREG da11d0e6d; tool + library + sheets 03826820b (before any read); raw reads 542d0ffcf (before resolve or score).

## What was built
`tools/tx_compare.py library` (cross-target library: printed cell + spread secure tiles, `--extra` for other family targets),
`build --library DIR --per-cand N --split N --max-sheets N`, `resolve --agree DIR1 DIR2` and `--reads-dir DIR`; offline test
`tools/tests/test_tx_compare.py::test_library_and_agree` passes. Shelf row `tx_compare.py library` (weak), SYSTEM.md row.

## Follow-ups (one line each, not done)
- The library itself (151 tiles, printed cell + spread hand tiles) is reusable as a sorter reference sheet for the owner; its 20
  print-only codes would need f184v/f185r page images restored (57 tiles) before it is complete.
