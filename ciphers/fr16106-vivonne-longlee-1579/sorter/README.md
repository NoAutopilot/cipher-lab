# Sign sorter, Longlee 1580, f.101v (LONGLEE-SORTER, 4 Oct 2026)

For the owner. Built, not published: the account-3 orchestrator publishes it (capabilities {"db": {}}, as for
`ciphers/debosnys-1883/sorter/README.md`). Why: VIV-T's first test on this letter was a NON-TEST because the two blind
machine readers of f.101v split on 58% of signs (err_2reader 0.576) against an unsettled 29-label inventory
(`tx/SIGNS.md`); by Usage 6 / TRANSCRIPTION.md the next pass is the owner's, not a third machine read.

What is in it: BnF fr.16107 canvas 107 left page, f.101v, Saint-Gouard to the King, Madrid, 2 Mar 1580 (the first of
the letter's five cipher pages, f.101v-103v; f.102r-103v are not cut yet). 1,493 tiles from 33 cipher lines, cut from
the PUBLIC Gallica native region already on disk (ark btv1b9009661v, f107, region 550,550,3800,5350); one strip per
line in `pages/f101v_L<nn>.jpg`, all at the region's full width so the sorter draws lines above and below at the same
x window. No sign values or plaintext appear anywhere in this folder: pile names are VIV-T's shape labels.

Build (no network, about 15 s): `bash ciphers/fr16106-vivonne-longlee-1579/sorter/build.sh <scratch dir>` from the repo
root -> `longlee_f101v_sorter.html` (about 2.6 MB; 70 piles, 1,493 tiles, 40 focus tiles; rendered headless on
4 Oct 2026 with no page errors, context view and neighbour lines checked).

How the piles were made (`build_inputs.py` docstring has the detail):
- **Lines.** The page has **33** cipher lines, not 32: VIV-T's horizontal `iiif_lines.py` bands 30-32 straddle lines
  30-33 at the foot (the lines slope up to 100 px across the leaf). Strips here follow each line's own trace.
- **Lines 1-29:** tiles are ink-profile blobs fitted to that line's number of aligned columns in `tx/ciphertext_draft.tsv`
  (pass A vs pass B, `tools/reconcile_passes.py`); per-line blob vs column counts are in `fit.tsv` (within -13..+3).
  Pile `x` = both readers read x; `a/c` = A read a, B read c (pairs seen 4+ times; rarer splits in `split-rare`);
  `c+1r` = only one reader saw a sign there (4+ times; rarer in `one-reader`). A pile's family is reader A's label.
- **Lines 30-33:** no reader row belongs to one of them alone, so their 177 tiles sit in `foot-unplaced`.
- Tiles are **approximate**: a tile can be one or two positions off the column its label came from (touching signs,
  readers who took signs from neighbouring lines). Use the context view; a bad cut goes to BAD-CUT, not a pile.
- `--auto-clusters 4` adds provisional shape clusters inside each pile (k-means on the tiles, no atlas yet).

"Check these first" (`focus.tsv`, 40 tiles): up to three tiles for each of the 14 most frequent reader splits
(a/c x32, t/d x19, D/A x11, s/c x9, ...). The owner's answer on those says which reader's label is a real sign.

Apply after the owner's pass: `ArtifactData list` for piles/moves/newpiles, then
`python3 tools/sign_sorter_apply.py --labels sorter/labels.tsv --db DIR --out sorter/settled_labels.tsv --summary sorter/summary.json`
(from this folder). Then the settled labels become the inventory for a machine pass on f.101v-103v (NOTES.md "Remaining gaps").

## v3 re-cut (LL-RECUT, 4 Oct 2026): one tile = one sign, straight lines

Owner, on the v2 page (the Pisany complaint): tiles straddled two signs or cut one in half, because v2 fitted ink-profile
blobs to the readers' column COUNT, and the sloping lines put the wrong line in the context strip. `recut.py` replaces
`build_inputs.py` in `build.sh`, using the Pisany method now shared as `tools/sorter_recut.py` (Pisany's `recut.py` and
`small_pile.py` call it too and reproduce their committed outputs byte for byte; `build_inputs.py` here now runs only as a
script, its `traces()` imported, outputs unchanged):
- **Deskew.** Each strip is sheared along `build_inputs.traces()`, re-centred per 300 px window on the strip's own ink, so
  `pages/f101v_L<nn>.jpg` (245 px tall, full region width) is one straight line and the lines above/below are the right ones.
- **Tiles from each sign's own ink** (components owned by the line, x-overlapping strokes joined, wide groups split at ink
  minima; over-splits a little on purpose). **1,834 tiles, 44-64 per line**, vs the readers' 37-53 columns on lines 1-29
  (`fit_recut.tsv`); v2 had 1,493 tiles fitted to the column count from 33-46 ink blobs per line (`fit.tsv`).
- **Starting piles, value-blind**: tiles aligned in x order (DP) to the reader columns, positioned at the v2 tile centres;
  1,258 tiles within 30 px of a column take its pile (same names as v2). The other 576 (and every tile of lines 30-33, which
  have no reader row) start in the pile their shape cluster (k-means, 100 clusters, `clusters.tsv`) most often holds, a
  named pile preferred over `split-rare`/`one-reader` when it holds 3+ and 20%+ of the cluster. Caveat: the column
  positions are the v2 approximations and the readers agree on 42%, so "aligned" is a starting guess, not a check.
- **SMALL** (`small_pile.py`): 185 tiles under 18 px tall or under 60 ink px (dots, specks, a few real small signs) in one
  pile, out of the focus box. **Focus**: 30 (`focus30.tsv`, one-line captions), unaligned tiles, most frequent shapes first.
- Build: 70 piles, 1,834 tiles, 168 provisional clusters, 2.8 MB page. `run_all.sh` with the page: 13/14 suites ok; test_qa fails only "no page errors", on the synthetic fixture as well as this page, from ERR_CERT_AUTHORITY_INVALID (Google Fonts through the container proxy; certutil absent here), as on Pisany: environment, not the page.
- Spot check (40 random tiles, seed 20261004, montage by eye): 31 hold exactly one sign, 7 are specks (dots, a fragment;
  most already in SMALL), 2 are bad (a loop of the line above joined to a small o; half an x with a stroke below).
- The v2 cut is kept for the record: `signs_v2.tsv`, `labels_v2.tsv`, `focus_v2.tsv` (x/y refer to the v2 sloped `pages/`,
  in git history before this commit). No owner moves were made on v2, so nothing to carry over.

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

## Whole page view (SORTER-PAGEVIEW, 4 Oct 2026)

Owner on Longlee f101v_L32_49: the larger view's neighbour lines were trimmed slices with separators that cut ascenders and
descenders. `recut.py` now also writes `region.json` (each line's centre trace on the Gallica region) and `build.sh` passes
`--region`: the larger view opens on the original region around the tile, continuous, about three lines above and below at
zoom 3, the tile's box drawn as it sits on the page ("Whole page"; "Line strips" switches back). Fix the cut works on the page
image and still saves strip pixels, so `tools/sorter_apply_recuts.py` is unchanged. `build.sh` writes
`<out stem>_region.jpg` beside the HTML (long side 4000 px); publish it with the page as a supporting file of the same name.

