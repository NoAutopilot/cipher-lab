# TXE2-SHEETAUDIT: reader sheets crossed against the truth files, Spinelli sheet corrected, eval errormap re-run

LANE TX-ENGINEER-2 incarnation 2, account 4, Opus; PREREG benchmark-tx/PREREG-txeng2-6.md A1 (TX-RED pass 3 F18 ii, F19);
9 Oct 2026 19:13-19:2x UTC by date -u. No reader, no subagent, no host request, no Spinelli cipher read, no pass run.
This is not an instrument: the sheet fix is a baseline change (Amendment 4), and the baseline under atlas_v4 is B1's job.

Openings of eval truth: 2 (exemplar cross-check, errormap re-run)

The exemplar cross-check read truth rows only at exemplar positions: Spinelli (atlas v3 + atlas_v2 tiles) and f152r (the
12 f152r tiles of the TX-SHEET sheet), one scripted pass, counted as the one opening.

## 1. Every reader sheet in use on a BENCHMARK-TX item

| sheet | items | kind | crossable? | verdict |
|---|---|---|---|---|
| ciphers/nevers-birago-fr3251-1572/harvest/sign_sheet_blind_1572.png (= birago-fr3252-1571-72/harvest/f117/ copy, byte-identical) | birago1572-no87 (A, B, C, L), birago1572-f152r, f178r | printed key: cut from Tomokiyo's NeversBirago.png by `cut_sign_sheet.py`, one blob per key column, no tile from a letter | no box ids | clean by construction |
| ciphers/ceppo-nevers-fr3251-1570s/harvest/sign_sheet_blind.png | ceppo-f21v-S, ceppo-f87-S, ceppo-f36v-gloss | printed key: the 55 cells of Tomokiyo's nevers_add1.png, relabelled | no box ids | clean by construction |
| dint-f128-print: `f128/pass_instructions.md` inventory | dint-f128-print | text list | no | clean by construction |
| bir1591 / dint-f98v / f113 / f89 `blind_pass_brief_*.md` shape vocabularies | bir1591-f23r-gloss(-jk), dint-f98v/f113/f89-gloss(-kp, -kp2) | text lists (value-blind shape labels), no tiles | no | clean by construction |
| ciphers/fr16104-vivonne-spain-1572/tx/SIGNS.md labels | vivonne1573-f103r-confirm2 | text list | no | clean by construction |
| **ciphers/spinelli-beinecke-c1515/glyphs/atlas.png (v3)** | spinelli-c1519-confirm (the confirm passes' sheet) | atlas-built: 24 rows, 152 tiles cut from the letter's own boxes | yes (box -> passes/p{1,2}_reconciled_v4.tsv -> v6 position -> truth line/pos) | **3 MISLABELLED** (table 2) |
| ciphers/spinelli-beinecke-c1515/glyphs/atlas_v2.png | named in the Spinelli row's notes as the reader vocabulary (H38/H40 splits) | atlas-built: 34 rows | yes | **5 MISLABELLED** (after folding v2 sub-codes to their v3 cells; 29 before folding, all HOOK sub-code grain) |
| ciphers/nevers-birago-fr3251-1572/atlas/sheet_truth/sheet_01-04.png (TX-SHEET, 4 Oct) | birago1572-no87 pass E only (a non-baseline covering pass in ERRORMAP; the instrument FAILed and is retired) | atlas-built: 33 cells, 185 tiles from sibling leaves (no no.87 leaf by construction) | only its 12 f152r tiles (f152r is an eval item); the 173 others are on leaves with no truth file | **1 MISLABELLED** (table 3) |
| benchmark-tx/txeng/hints/hints_sheet.png, txeng/adjud/*/sheet_NN.png | instruments (X-series hints, adjudication tiles of positions) | not a reader sheet of a baseline | -- | out of scope (instrument inputs, not exemplar sheets) |

## 2. Spinelli atlas v3 exemplars vs the truth (full table: spinelli_atlas_v3_cross.tsv, 154 rows)

107 OK, 44 no-truth (excluded row or box not in the committed reconciliation), **3 MISLABELLED**:

| sheet | cell | box id | truth position | committed code | truth value | verdict |
|---|---|---|---|---|---|---|
| atlas.png v3 | SIX | p1_01_025 | p1c_L01.14 | ESS | ESS (h) | MISLABELLED (V2's finding, confirmed) |
| atlas.png v3 | OMEGABAR | p1_03_017 | p1c_L03.18 | OMEGADOT | OMEGADOT, PHI_G (g) | MISLABELLED (the dotted omega in the OMEGABAR row's last tile) |
| atlas.png v3 | TEE | p1_03_001 | p1c_L03.1 | PLUS | PLUS (b) | MISLABELLED (plus with a foot) |

Read-free context (no truth used): SIX's 9th and 10th tiles (p1_05_010, p1_08_030) are h-shaped by eye (V2 called the last
".h."); p1_05_010 is an excluded row (no truth value) and p1_08_030 is in no committed reconciliation (no truth position).
Two more tiles whose committed code differs from their cell, both on excluded rows (undecidable by the truth, not removed):
PHI p1_05_019 (committed HOOK), THETA p1_05_013 (committed PHI).

atlas_v2 adds two (spinelli_atlas_v2_cross.tsv): OMEGA2 p1_08_021 (p1c_L08.22, committed OMEGABAR, truth PI|THETA = d) and
STROKE p2L2_01_003 (p2c_L02.3, committed HOOK, truth DEE|ENN|TWO_S2 = s); v2 is not corrected here (v3 is the sheet in use).

## 3. TX-SHEET sheet, f152r tiles vs the f152r truth (txsheet_f152r_cross.tsv)

12 tiles; mapping check ref_sign == tile code 12/12; 10 OK, 1 no-truth (slip dot), **1 MISLABELLED**: cell T36, box
f152r_03_018, truth position f152r_L02.18, truth T45|T66|T86 (e). That position is also f152r's one remaining baseline error
(e <- T36, all-same-wrong): the f152r readers used the printed-key sheet, not this one, so the tile did not cause it; the
TX-SHEET secure-token rule took the two readers' agreement as the label, which is the same shared misread. Not corrected
(the sheet is a retired instrument's; it is the baseline sheet of no item).

## 4. Spinelli sheet corrected read-free: atlas_v4

`ciphers/spinelli-beinecke-c1515/glyphs/build_atlas_v4.py` (tile surgery on v3, `--check` passes): removed SIX p1_01_025,
SIX p1_05_010, OMEGABAR p1_03_017, TEE p1_03_001; moved the h-shaped SIX p1_08_030 to ESS (the published key's h is ESS,
key.tsv H; that box has no truth position). No replacement tile was chosen by looking up an eval position's truth; no tile
was added from the published key image (sources/cryptiana/web/img/spinelly1515.png is Tomokiyo's redrawing, not
Domnina 2016's table, and its h cell's shape could not be matched to the letter's h with confidence, so pasting it would add
an unverified shape). Re-cross of atlas_v4: 107 OK, 43 no-truth, 0 MISLABELLED. Rows now: SIX 7 tiles (all 6-shaped),
ESS 3 (two S/5 forms + the h form), OMEGABAR 9, TEE 3. Cluster counts in the row labels are v3's, unchanged. v3
`atlas.png` untouched. Changelog: `glyphs/README.md`.

## 5. Errormap re-run after V1/V2

Appended as a dated section to benchmark-tx/txeng2/ERRORMAP-2026-10-09.md. Eval pool as ERRORMAP defined it
(eval_heldout + Spinelli) 22 (was 29); Amendment 4's pool 29 (10 + 6 + 12 + 1, agreeing with Amendment 4): majority-wrong
10, all-wrong-split 10, all-same-wrong 6, minority-wrong 3; tool classes other 12, look-alike 11, crop 5, thin 1; with V2's
correction 3 of Spinelli's 12 are the sheet's (2 h <- SIX, 1 SEVEN_E deleted). Untested hint for B1: Spinelli's r <- SIX x4
(tall bottom-loop signs, the other reader's NEW:tall-l-bottom-loop) may also be taught by the h-shaped SIX tiles; B1's
fresh baseline will show it either way, and this job draws no conclusion.

## Commits and sha256 (commit 3fc0ee02b238a89b1f45c88e7417b9ffc29848ea on origin/main; 893912e2 before the rebase onto origin/main)

| file | sha256 |
|---|---|
| ciphers/spinelli-beinecke-c1515/glyphs/atlas_v4.png | 4ad8c0484ccf65c8ea8b59e326f4d1d64c98b1605bea046c752b5a654e28b67f |
| ciphers/spinelli-beinecke-c1515/glyphs/atlas_v4.tsv | fa033ab7d050ccfefb0b050f313418254a71633a4155a76a0f39ec976cdce7d6 |
| ciphers/spinelli-beinecke-c1515/glyphs/build_atlas_v4.py | 8beceb1eed9dbd2b64ec903dee5e88d01cfe9b4d75458a1e9cda79b30315841f |
| ciphers/spinelli-beinecke-c1515/glyphs/atlas.png (v3, untouched) | 1141042e722da4b7d9955616cb6ebf634668662d48cac2950ad7f65cd54d46f4 |
| benchmark-tx/txeng2/sheetaudit/spinelli_atlas_v3_cross.tsv | ced320c8c5cd11c2db1a6a6af279a04f385f7f9abb3335fff0a1dcc6937e3554 |
| benchmark-tx/txeng2/sheetaudit/spinelli_atlas_v2_cross.tsv | a9373671912571306aa0cf45b4b9e5d23848bb579ad9d38a9e29749d2e428a64 |
| benchmark-tx/txeng2/sheetaudit/txsheet_f152r_cross.tsv | 6c013680d516f2dfa4469b07d5d812000d9a14531808f6058e2a7ba1eb8bc828 |
| benchmark-tx/txeng2/sheetaudit/cross_spinelli.py | f1149cd9310e1f54e4e774b276ebce5e4f49650c2d82d9d8ad0ba55d20cea9a5 |
| benchmark-tx/txeng2/sheetaudit/cross_txsheet_f152r.py | 3c874a91eb0384ec0d2a190658a411866c33101f3f8ef1b6b3aa21e2c6a59176 |
| benchmark-tx/txeng2/sheetaudit/errormap/pools_flagged.md | edf96ae5d8554ebfae48696b1a26e3b28bf2bd0f993c6c619a99b246f468bc65 |

Folder sizes: sheetaudit/ 248 KB; atlas_v4.png 131 KB added to ciphers/spinelli-beinecke-c1515, which was already 43 MB
before this job (images/ 29 MB) -- over the 30 MB line by earlier jobs, flagged, not shrunk here (not this brief).
Requests: 0 network. Subagents: 0. No *.truth.tsv edited.
