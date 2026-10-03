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
