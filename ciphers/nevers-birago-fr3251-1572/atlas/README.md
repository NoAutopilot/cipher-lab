# Birago 1572 family sign atlas (TX-ATLAS-B72, 3 Oct 2026, account 2 for the account-3 orchestrator)

One `tools/glyph_atlas.py` atlas for every Birago 1572 letter (TRANSCRIPTION.md steps 2-5), built from native Gallica
region images already on disk (no refetch): BnF fr.3251 nos.71 (f139v), 73 (f144r), 77 (f152r), 82 (f162r), 85 (f168r,
f168v), 86 (f174r, f174v, f174vB, f175r, f175v), 87 (f178r, f178v, f179r), 90 (f184r, f184v, f185r) and fr.3252 f.117r
(`pages.py` lists the sources; f184v/f185r are re-assembled from their line crops). Sibling letters reuse this folder:
classify a new page against `signs.tsv`/`bitmaps.npz`/`labels.json` after adding it with `segment` (re-run all pages).

Regenerate (repo root; crops/, pages/, debug_*.jpg and sheet_*.png are gitignored and come back from these commands):

    A=ciphers/nevers-birago-fr3251-1572/atlas
    python3 tools/glyph_atlas.py segment $(python3 $A/pages.py) --out $A --debug
    python3 tools/glyph_atlas.py cluster --out $A --k 140 --k-marks 16
    python3 $A/no87_map.py                 # label-blind box<->token map on no.87 (f178v L01-23, f179r L01-03)
    python3 $A/name_clusters.py            # clerk-sheet names (tune lines f178v L01-12) + named_by_model.json
    HO=$(for i in $(seq 13 23); do echo -n " --holdout f178v_${i}_"; done; for i in 01 02 03; do echo -n " --holdout f179r_${i}_"; done)
    python3 tools/glyph_atlas.py classify --out $A --labels $A/labels.json --page all --tsv /tmp/ho.tsv --topk 3 $HO
    python3 $A/score_no87.py /tmp/ho.tsv   # = score_no87.txt
    python3 tools/glyph_atlas.py classify --out $A --labels $A/labels.json --page all --tsv /tmp/all.tsv --topk 3   # split per letter -> topk/<letter>.tsv
    python3 tools/glyph_atlas.py atlas --out $A --labels $A/labels.json --per 10 --prefer f178v

Files: `signs.tsv` 4,209 boxes, `marks.tsv` 474, `clusters.tsv` 140 sign clusters (deliberate over-split),
`cluster_names.tsv` (76 named by verified no.87 tune tiles, 64 by four Sonnet exemplar-sheet reads, `named/reads.tsv`,
sheets `named/sheet_0N.jpg`, prompt `named/prompt.md`; MIXED read as `_`), `labels.json` (cluster names + 309
known-answer per-tile overrides), `atlas.tsv`/`atlas.jpg` (45 codes), `topk/<letter>.tsv` (k1 d1 s1 .. k3 d3 s3 per
box, full atlas, for TX-DECODE), `topk/no87_heldout.tsv` (no.87 boxes classified with the held-out lines kept out of
the vote), `no87_box_token.tsv` (box <-> line-read token <-> clerk letter).

Headline, tools/tx_bench.py (tx_bench_atlas.txt, eval split, 15 held-out lines): atlas top-1 err_true 0.162 (61/376,
95% 0.128-0.203) vs the committed line reads 0.040 (15/376) on the same lines. Label-blind scorer (score_no87.txt): on 376 held-out no.87 signs, atlas top-1 err_true 0.322 against the line-read
reconciliation's 0.056 on the same signs (one value map, no exceptions); the truth is outside the atlas top-3 on 0.261.
The atlas does not replace the line reads on this hand. See NOTES.md "TX-ATLAS-B72" for limits.

## Label-aware box map (BOXMAP-LA, 11 Oct 2026, account 3)

`no87_box_token.tsv` above is label-blind (box widths only) and shifts whole stretches of a line by one token where it
maps an extra box 1:1: on f178v L06 the owner's NOT-LETTER tile f178v_06_009 takes token 9 and the next tiles land one
late (TXE3-9 second check, benchmark-tx/txeng3/9/VERIFY.md). It is kept unchanged because it is cited. The replacement is

    python3 ciphers/nevers-birago-fr3251-1572/atlas/no87_map.py --label-aware [--check]

-> `no87_box_token_labelaware.tsv` (sid fol line pos idx sign op split labels status loo_pos old_pos; NO truth column) and
`no87_box_token_labelaware_lines.tsv` (per line: skipped boxes, ops, tiles moved with old>new position, old 1:1 tiles
that are no longer one-token). Tool: `tools/box_token_align.py` (same DP and width costs; the owner's sorter statuses --
not-letter skipped, bad-cut never 1:1 -- and truth-blind labels against the line read L: classify top-3 with every no.87
page held out, `benchmark-tx/txeng/compare/topk_no87_allheld.tsv`, and the sorter seed pile's family or the owner's pile
where he moved the tile; lam 1.5; a box whose place changes when its own label is hidden is `unsure`, not `1:1`). Same
scope as the old map: f178v L01-23 and f179r L01-03 (f178r not mapped).

Truth-free check (label = seed.tsv `atlas`, the tile's atlas k1; read sign at the mapped position): old map 157 of 208
at 0, 24 at -1, 14 at +1, 0 at +-2, 13 none; new map 188 of 203 at 0, 1 at -1, 2 at +1, 0 at +-2, 12 none (leave-one-out,
own label hidden: 187 / 2 / 2 / 0 / 12). Cross-checks that do not use the checked label: a run steered by the sorter labels
alone raises the held-out atlas k1's agreement with the read at the mapped box from 485/695 to 577/688; a run steered by the
atlas top-3 alone raises the seed family's from 142/201 to 173/196. Tiles moved: 124 on 10 lines (f178v L06 6, L07 2, L09 12,
L11 18, L13 24, L17 13, L21 17; f179r L01 5, L02 14, L03 13); 16 other lines unchanged. 1:1 700, unsure 3, bad-cut 2, 2:1 25
pairs, 1:2 13 boxes. Use the new file for any join of sorter tiles or atlas boxes to line-read positions; a result built
on the old file (X20, TX-ATLAS-B72 naming/scoring, BIR87-ALIGN relabel, TXE3-1/2/7/9/10, the MQS-SHEETS/SORTER tests,
tx_pair_clf, tx_sorter_curve, tx_taxonomy) rests on shifted joins wherever it touches those 10 lines. The same width DP
also built `benchmark-tx/txeng/compare/box_pos.tsv` and `benchmark-tx/txeng/pair/dev_tune/box_pos.tsv` (tx_compare.py
`map`, tx_pair_reread.py), which share the defect and are not rebuilt here.
