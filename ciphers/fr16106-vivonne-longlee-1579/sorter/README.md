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
- **Lines 30-33:** no reader row belongs to one of them alone, so their 171 tiles sit in `foot-unplaced`.
- Tiles are **approximate**: a tile can be one or two positions off the column its label came from (touching signs,
  readers who took signs from neighbouring lines). Use the context view; a bad cut goes to BAD-CUT, not a pile.
- `--auto-clusters 4` adds provisional shape clusters inside each pile (k-means on the tiles, no atlas yet).

"Check these first" (`focus.tsv`, 40 tiles): up to three tiles for each of the 14 most frequent reader splits
(a/c x32, t/d x19, D/A x11, s/c x9, ...). The owner's answer on those says which reader's label is a real sign.

Apply after the owner's pass: `ArtifactData list` for piles/moves/newpiles, then
`python3 tools/sign_sorter_apply.py --labels sorter/labels.tsv --db DIR --out sorter/settled_labels.tsv --summary sorter/summary.json`
(from this folder). Then the settled labels become the inventory for a machine pass on f.101v-103v (NOTES.md "Remaining gaps").
