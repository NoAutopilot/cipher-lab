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
