# Sign sorter, Oldenbarnevelt 2442 blocks A and C2 (R7-OLDSORT, 6 Oct 2026)

For the owner. Built, not published: the lane orchestrator (LANE-RUN7-account-2) files the ASKS row and publishes it
(capabilities {"db": {}}, as for `ciphers/matignon-mayenne-1586/sorter/README.md`). Why: R7-OLDA's two blind machine passes
of blocks A and C2 split on 19.0% of signs (15.1% after folding vowel-letter/digit notation; NOTES.md section 13); by
CLAUDE.md Usage 6 / TRANSCRIPTION.md a split over 10% goes to a person, not a third machine pass.

What is in it: Nationaal Archief 1.01.02 inv. 2442, block A (folio 54, leaf 001, 11 lines) and block C2 (folio 56, leaf 006,
8 lines plus the word written under line 8), cut from the deskewed line crops R7-OLDA already made (`images/crops_AC2/`; no
new request). 692 tiles on 20 line strips (`pages/`). Piles are R7-OLDA's reconciled draft sign labels
(`transcription/reconciled_AC2_R7OLDA.tsv`, 30 piles); the draft is itself uncertain (36 of 165 words). No plaintext
reading or key values are in this folder beyond those sign labels.

Build (no network, a few seconds; needs pillow and numpy): `sh ciphers/na-oldenbarnevelt-2442-1605/sorter/build.sh <out dir>`
from the repo root -> `oldenbarnevelt_AC2_sorter.html` (about 2.9 MB; 30 piles, 692 tiles, 103 focus tiles, 61 provisional
`--auto-clusters 3` clusters). Rendered headless 6 Oct 2026: 797 images, 0 page errors.

Limits (read before trusting a pile):
- This is a joined cursive hand: an ink profile cannot find the sign boundaries. Words are laid out along each line's ink
  extent in proportion to their sign counts (a word space = one sign width) and each word is cut at proportional positions
  snapped to the lightest column nearby. A tile is often a sign off, or half of two signs; the context view shows the
  whole strip. A bad cut goes to BAD-CUT, not a pile. (Breaking at the widest ink gaps was tried first and put whole
  words in the wrong box, so it was dropped; `fit.tsv` records words per line and the ink blobs found.)
- Strips are three overlapping crops pasted at their manifest offsets; the deskew is per line, so a join can be a few px
  off vertically. Interlinear words (C2 line 6 `+d8b8nd8`) and punctuation are not tiled.

"Check these first" (`focus.tsv`, 103 tiles): every tile where blind pass A or pass B (`transcription/passF_*`, `passG_*`)
wrote another sign than the draft once vowel-letter/digit notation is folded (u/v/2, e/8, a/4, o/7, i/y/3, final 5 = s,
6 = b), each with what the two passes wrote, unfolded. Order: the brief's look-alike pairs (10 tiles: v/r, and the G-shaped
ligature drawn l/c/b/6; 9/q, f/p, l/t and G/t, the B/C1 pairs of section 11, did not occur as A/C2 splits), then R7-OLDA's own
split pairs (32 tiles: d/8 for the looped d, 5/s, p/g/l, c/t, m/n/r), then the other splits (61).

Apply after the owner's pass: `ArtifactData list` for piles/moves/newpiles, then
`python3 tools/sign_sorter_apply.py --labels sorter/labels.tsv --db DIR --out sorter/settled_labels.tsv --summary sorter/summary.json`;
then step (a'') of NOTES.md's Verdict (machine passes against the settled labels, decode, grade, judge).
