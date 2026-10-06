# Sign sorter, Oldenbarnevelt 2442 blocks A and C2 (R7-OLDSORT, re-cut R7-OLDFIX, 6 Oct 2026)

For the owner. Built, not published: the lane orchestrator (LANE-RUN7-account-2) files the ASKS row and publishes it
(capabilities {"db": {}}, as for `ciphers/matignon-mayenne-1586/sorter/README.md`; publish the page with its
`oldenbarnevelt_AC2_sorter_region.jpg` beside it). Why a sorter: R7-OLDA's two blind machine passes of blocks A and C2 split
on 19.0% of signs (NOTES.md section 13); by CLAUDE.md Usage 6 / TRANSCRIPTION.md a split over 10% goes to a person.

## R7-OLDFIX re-cut (6 Oct 2026) -- replaces the withdrawn R7-OLDSORT build

The first build (artifact withdrawn by the account-3 orchestrator) laid each line's words out by sign count and cut at
proportional positions with boxes the height of the whole strip, so tiles reached into the line above or below; and it
tiled the clear Spanish opening of line A1 ("labreuedad que desseo y espero,"), which is not cipher. Tile A_L01_001 was that
clear "l". The line map itself was right: R7-OLDA's `--centres` sit on the 11 block-A and 8 block-C2 cipher lines (NOTES.md
section 15). That cut is kept for the record as `signs_v1.tsv`, `labels_v1.tsv`, `focus_v1.tsv`, `fit_v1.tsv`
(`build_inputs.py`); its x/y refer to the v1 strips, which `pages/` no longer holds (except `pages/C2_L09.jpg`, v1 only).

What is in it now: `recut.py` (tools/sorter_recut.py, the shared Pisany/Longlee method): the two leaf regions stacked into
`region.jpg`; each line deskewed along the line through the centres of R7-OLDA's three crops of it (line A11: slope -0.07
anchored by eye, its own fit ran under the text), re-centred on the strip's ink; one tile per ink group (joined strokes,
wide groups split at ink minima). **689 tiles on 19 line strips, cipher text only**: line A1 is tiled from "8l s8cr8t4r37
fran" on (22 tiles dropped: the clear opening of A1, and A11 right of "8n8" where the trace meets the clear line below).
Starting piles: 589 of them line up within 30 px with a sign of R7-OLDA's reconciled draft (at the v1 tile positions) and
start in that sign's pile; the rest start in the pile their shape cluster mostly holds. 27 piles. Not tiled: the word
under C2 line 8 ("p8n4n", R7-OLDA's hand-cut C2_L09), the interlinear "+d8b8nd8" over C2 line 6, punctuation.

"Check these first" (`focus.tsv`, 24 tiles, kept short for the phone layout): 18 tiles where the two blind passes wrote
different signs (v1 order: the look-alike pairs v/r and the G-shaped ligature first, then R7-OLDA's d/8, 5/s, p/g/l, c/t,
m/n/r, then others), each with the draft and both readers' signs; then 6 tiles no draft sign lined up with.

Limits: a joined cursive hand. Ink groups still join two signs (a ligature, a word written in one stroke) or split one;
C2 line 8 has 26 tiles for 39 draft signs (joined strokes). Use Fix the cut or BAD-CUT. Starting piles are a draft's, not
a reading.

Build (no network, a few seconds; needs pillow, numpy, scipy, scikit-learn):
`sh ciphers/na-oldenbarnevelt-2442-1605/sorter/build.sh <out dir>` from the repo root -> `oldenbarnevelt_AC2_sorter.html`
(about 3.2 MB) + `oldenbarnevelt_AC2_sorter_region.jpg` (page view of the two regions, 1930x2580).

Checks run 6 Oct 2026 (current `tools/sign_sorter/template.html`, Chromium headless):
- `tools/sign_sorter/browser_tests/test_qa.js` on this page: ALL PASS (141 checks, desk and phone, no page errors).
- "Fix the cut": `test_recut_quad.js` run on this page (its fixture pile `X` swapped for pile `8`): edit opens, corner drag,
  brush mask, save writes the db `recuts` row, tile keeps its pile with badge and redrawn thumbnail, reload, phone touch drag,
  page view -- all ok; one check failed, "corner arrows nudge one corner 2 px a tap" (the nudge moved the box by 2 px, the
  test's expected corner differs on this page's geometry), no page errors. The template's own fixtures pass test_recut.js and
  test_recut_quad.js in full. (`test_recut.js`'s plain-box checks do not apply: the current template edits a box as four
  corners.)

Five random tiles against the line images (sorter rule, seed 20261006, four from all tiles and one from A_L01; each drawn on
`region.jpg` with 200 px above and below):

| tile | pile | what it shows |
|---|---|---|
| C2_L04_02 | 7 | the "7" of "d7", first word of C2 line 4 ("d7 4lg2n4 7cc4ss37n") -- on the line |
| A_L03_30 | l | first part of the G-shaped ligature "l7" before "d8s3g28nc4", A line 3 -- on the line |
| A_L09_02 | 4 | inside "r34", start of A line 9 (the 3/4 join) -- on the line; sign for the owner |
| A_L09_04 | l | the "4" / "l" of "4lg7", A line 9 -- on the line; sign for the owner |
| A_L01_38 | m | the "an" of "fran", end of A line 1 (cipher part, after "s8cr8t4r37") -- on the line; pile by shape, likely wrong |

None sits on a clear line above or below.

Apply after the owner's pass: `ArtifactData list` for piles/moves/newpiles/recuts, then
`python3 tools/sign_sorter_apply.py --labels sorter/labels.tsv --db DIR --out sorter/settled_labels.tsv --summary sorter/summary.json`;
then step (a'') of NOTES.md's Verdict (machine passes against the settled labels, decode, grade, judge).
