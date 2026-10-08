# PREREG-BERGH-STRIP (LANE FAMILY, account 2, 8 Oct 2026, written 22:2x UTC by `date -u`, pushed before any strip is read)

Question: do box-numbered strip reads give each GLY-11106 atlas box (atlas/signs.tsv) the right sign, where the width/position
alignment (atlas/map_tx.py -> atlas/boxmap.tsv) gave 5/19 right on GLY-11106's eye-checked contact sheet
(sorter/sorter.preflight.jpg, tools/sorter_preflight.py seed 20261006, 24 tiles, 19 carrying a mapped label)?

## Known answers (the 19 eye-checked boxes; truth = GLY-11106's eye check, re-eyed on the same sheet by this worker before any read)

| # | box | old mapped label | truth | accepted labels |
|---|---|---|---|---|
| 1 | L15_01_013 | g | 3 | 3 |
| 2 | L11_01_020 | s | fragment | FRAG |
| 3 | L12_01_044 | f | r | r |
| 4 | L20_01_006 | g | 4 | 4 |
| 5 | L02_01_038 | h | fragment | FRAG |
| 6 | L06_01_020 | m | fragment | FRAG |
| 7 | L06_01_004 | 7 | y | y, yx (y/yx is a listed look-alike pair) |
| 8 | L20_01_036 | b | b | b |
| 9 | L06_01_026 | 7 | 7 | 7 |
| 10 | L07_01_009 | r | fragment | FRAG |
| 11 | L18_01_018 | yx | r-like, uncertain in GLY-11106 | r, yx |
| 12 | L22_01_007 | u | B | B |
| 13 | L10_01_037 | A | s | s, 5 (s/5 is a listed look-alike pair) |
| 14 | L14_01_018 | e | e | e |
| 15 | L18_01_007 | s | fragment | FRAG |
| 16 | L15_01_031 | B | 3 | 3 |
| 17 | L21_01_015 | s | s | s, 5 |
| 18 | L11_01_019 | s | fragment | FRAG |
| 19 | L08_01_026 | u | u | u, n (n/u listed look-alike pair) |

FRAG = the reader marks the box as not a whole sign (a speck, a stroke or a piece of a neighbouring sign, or a neighbour line's tail).
Look-alike pairs are accepted as each other because the gate tests the box -> sign mapping, not the look-alike decision (that is the
owner's sorter's job); the pairs accepted are only those already listed in tx/focus.tsv split classes.

## Method (fixed before reading)

- Strips: one window strip per gate box, cut from images/crops/p2_Lxx.jpg (the committed line crops), about 640 px of the line around
  the box, upscaled 2x, every atlas box whose centre falls in the window outlined and numbered with a window-local number; the sid of
  each number is held in a key file the readers never see; the gate box is not marked out from its neighbours. Strip width <= 2500 px.
- Two blind Sonnet passes (A, B), each over every strip, <= 4-line-equivalents of strip per call; B gets the strips in reverse order.
  Readers get the sign list tx/signlist.md and the strip paths only, never tx/, atlas/boxmap.tsv or any earlier label.
- Score per gate box on the **pass-agreed label only**: A and B agree and the label is in the accepted list = hit; A/B split = miss
  (no reconciler arbitration on the 19 gate boxes, since this worker has seen the answers). Boxes appearing in two windows are read in
  the window where they are the gate box.

## Gate

- PASS: >= 17/19 hits. Then (budget permitting) the all-box pass, atlas/box_sign.tsv for all 875 boxes, and sorter/ inputs rebuilt.
- FAIL: <= 16/19. Stop at the gate, write the reason, do not run the all-box pass.
- Baseline it must beat: the alignment mapping, 5/19 (6/19 counting #11 as r/yx). Reader self-consistency is reported beside it
  (A/B agreement on every numbered box in the strips, gate boxes and neighbours), so a pass with low A/B agreement is visible.
