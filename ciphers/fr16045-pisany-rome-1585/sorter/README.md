# Sign sorter, Pisany 1585, f.75r (PISANY-SORTER, 4 Oct 2026)

For the owner. Built, not published: the account-3 orchestrator publishes it (capabilities {"db": {}}, as for
`ciphers/fr16106-vivonne-longlee-1579/sorter/README.md` and `ciphers/debosnys-1883/sorter/README.md`). Why: PIS-T's first
test on this letter was a NON-TEST because the two blind machine readers of f.75 split on 43% of signs (err_2reader 0.430,
480 disagreement columns) against an unsettled 67-cell inventory (`tx/SIGNS.md`); by Usage 6 / TRANSCRIPTION.md the next
pass is the owner's, not a third machine read.

What is in it: BnF fr.16045 f.75r, Gallica canvas 156 (ark btv1b9060906j), Pisany to Henry III, Rome, 17 June 1585, the
22 cipher lines PIS-T transcribed (the clear opening and the cipher tail of clear line 6 are not included). 1,115 tiles,
cut from the PUBLIC Gallica native region already on disk (`images/src_ark_12148_btv1b9060906j_f156_680_1830_3060_3520.jpg`);
one strip per line in `pages/f75_L<nn>.jpg`, all at the region's full width so the sorter draws lines above and below at the
same x window. Pile names are the cells of Tomokiyo's 1585 table as PIS-T labelled them (S01-S67, shape labels); no sign
value or plaintext is in this folder.

Build (no network, about 15 s): `bash ciphers/fr16045-pisany-rome-1585/sorter/build.sh <scratch dir>` from the repo root
-> `pisany_f75_sorter.html` (2.2 MB; 59 piles, 1,115 tiles, 40 focus tiles, 141 provisional clusters). Rendered headless
on 4 Oct 2026: no page errors (the one console error is the Google Fonts stylesheet blocked by the container's TLS proxy);
the context view shows the tile in brackets with the lines above and below. HTML not committed.

How the piles were made (`build_inputs.py` docstring has the detail):
- **Lines.** The lines slope steeply down to the right (about 160 px across the region) and flatten a little. Each line's
  trace runs through two anchors taken from PIS-T's own s1/s2 crop boxes (the crops the readers read; L08 s2 and L09 from
  `images/fix_f75_L08_L09.py`), snapped to the ink within +-16 px. Peak-following alone slid one line down at the right
  edge (evenly spaced lines make a one-pitch slip score as well as the truth), so it was not used.
- **Tiles** are ink-profile blobs fitted to that line's number of aligned columns in `tx/ciphertext_draft.tsv` (pass A vs
  pass B, `tools/reconcile_passes.py`): blobs merged while too many, the widest split at its ink minimum while too few.
  Signs touch, so the blobs are far fewer than the columns (16-41 vs 46-55 per line, `fit.tsv`): tiles are
  **approximate** and can sit one or two positions off their label. Use the context view; a bad cut goes to BAD-CUT.
- **Piles.** `S15` = both readers read S15; `S10/S41` = A read S10, B read S41 (pairs seen 4+ times; rarer splits in
  `split-rare`, 133 tiles); `S21+1r` = only one reader saw a sign there (4+ times; rarer in `one-reader`). A reader's
  trailing `?` is dropped; `?[shape]` (no matching cell) became `NOCELL`. A pile's family is reader A's label.
  L02: reader A read only 29 signs to B's 54, so much of that line sits in `+1r` / `one-reader`.
- `--auto-clusters 4` adds provisional shape clusters inside each pile (k-means on the tiles, no atlas yet).

"Check these first" (`focus.tsv`, 40 tiles): up to three tiles for each split inside the four look-alike groups both
readers named (S15/S40/S13/S61, S10/S41/S02, S36/S42/S23, S46/S48/S25; largest S10/S41 x72, S36/S42 x66, S15/S40 x36), then
the other most frequent splits (S48/S21 x25, S64/S20 x13, ...).

Apply after the owner's pass: `ArtifactData list` for piles/moves/newpiles, then
`python3 tools/sign_sorter_apply.py --labels sorter/labels.tsv --db DIR --out sorter/settled_labels.tsv --summary sorter/summary.json`
(from this folder). Then re-run `test1.py` unchanged on the settled f.75 transcription (NOTES.md "Remaining gaps", 1585 letters row).

## v3 re-cut (PIS-RECUT, 4 Oct 2026): one tile = one sign, straight lines

Owner, on the v2 page: many tiles straddled two signs or cut one in half (f75_L08_02 = looped l + b), because v2 fitted
ink-profile blobs to the readers' column COUNT; and the sloping lines put the line above in the context strip. `recut.py`
(docstring has the method) replaces `build_inputs.py` + `tighten_tiles.py` in `build.sh`:
- **Deskew.** Each line strip is sheared along `build_inputs.traces()`, re-centred per 300 px window on the strip's own
  row-ink peak (the v2 trace sat ~50 px high on L08), so `pages/f75_L<nn>.jpg` (241 px tall, full region width) is one
  straight line and the context view's lines above/below are the right ones.
- **Tiles from the sign's own ink**: connected components owned by the line, x-overlapping strokes joined (pairwise),
  groups wider than 1.45 x the line's median sign width split at column-ink minima. Over-splits a little on purpose
  (dots stay their own tile). 1,290 tiles, 44-72 per line, vs the readers' 46-55 columns (`fit_recut.tsv`); v2 had
  1,115 tiles fitted to the column count from 16-41 ink blobs (`fit.tsv`).
- **Starting piles, value-blind**: tiles and reader columns (positioned at the v2 tile centres) aligned in x order by DP;
  1,067 tiles within 30 px of a column take that column's pile (same names as v2). The other 223 start in the pile
  their shape cluster (k-means, 60 clusters over the page, `clusters.tsv`) mostly holds; the focus box (40) is those,
  most frequent shapes first, at most two per shape.
- Spot check (20 random tiles, seed 20261004, eye on the overlay): 17/20 hold exactly one sign (one half sign, one
  half X, one d+3 pair). Build: 59 piles, 1,290 tiles, 2.0 MB page. `run_all.sh` with the page: 13/14 suites ok; test_qa fails only its "no page errors" check, on the synthetic fixture as well as this page, from ERR_CERT_AUTHORITY_INVALID (Google Fonts through the container proxy, as v2): environment, not the page.
- The v2 cut is kept for the record: `signs_v2.tsv`, `signs_tight_v2.tsv`, `labels_v2.tsv`, `focus_v2.tsv` (their x/y refer
  to the v2 sloped `pages/`, in git history before this commit). No owner moves were made on v2, so nothing to carry over.

## Fix the cut (SORTER-NUDGE, 4 Oct 2026)

Owner, on tile f101v_L03_04 (Longlee, pile split-rare): "If you give me the ability, I can nudge the 'bad cut' to be good
cuts." In the larger view (hold a tile), **Fix the cut** makes the box editable: drag an edge or the whole box (mouse or
touch; the page does not scroll while you drag), or use the arrow buttons (2 source pixels a tap, for phones). **Save cut**
stores the box in db collection `recuts` (doc id = tile id: sid, page, x y w h in this folder's `pages/` pixels, old box,
at); **Cancel** leaves the cut as it was; Undo takes a saved cut back. The tile keeps its pile, shows a "recut" badge and
its thumbnail is redrawn at the new box. A tile already in BAD-CUT, once recut, offers "Put it back in <home pile>" (one
tap). There is no "split here": for a box holding two signs, fit it to the first and mark the second "Bad cut" as now.
Apply: `ArtifactData list` recuts with the other collections; `tools/sign_sorter_apply.py` writes `recuts.tsv` beside its
`--out`; `python3 tools/sorter_apply_recuts.py --recuts sorter/recuts.tsv --signs sorter/signs.tsv --pages sorter/pages
--tiles sorter/tiles` re-crops those tiles (old crop kept as `<id>.orig.jpg`) and updates signs.tsv. `build.sh` re-runs
`recut.py`, which rewrites signs.tsv: run sorter_apply_recuts.py again after any rebuild (it is idempotent and skips, exit
2, a row whose old box no longer matches).
