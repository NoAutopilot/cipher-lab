# Sign sorter, Matignon/Mayenne f.110 (R7-MATSORT, 6 Oct 2026)

For the owner. Built, not published: the lane orchestrator (LANE-RUN7-account-2) files the ASKS row and publishes it
(capabilities {"db": {}}, as for `ciphers/debosnys-1883/sorter/README.md`). Why: D2B-MATF110's two blind machine passes
of f.110 lines 1-5 agreed on only 58.5% of positions (split 41.5%) and kept BOX, z, T and U apart from every keyed shape;
by Usage 6 / TRANSCRIPTION.md a split over 10% goes to a person, not a third machine pass.

What is in it: BnF fr.15572 f.110 (Gallica btv1b9061879d, canvas 116), image lines 1-6, cut from the line crops already
on disk (`images/f110/`, D2B-MATF110; no new request). 318 tiles: 284 on image lines L01, L02, L04, L05, L06 (=
ciphertext.txt f110-1..5) and 34 on L03, which straddles two rows and matches no transcribed line (pile `L03-unplaced`).
Piles are the existing transcription's shape labels; no sign values or plaintext appear in this folder.

Build (no network, a few seconds; needs pillow and numpy): `sh ciphers/matignon-mayenne-1586/sorter/build.sh <out dir>`
from the repo root -> `matignon_f110_sorter.html` (about 0.8 MB; 39 piles, 318 tiles, 54 focus tiles, 61 provisional
`--auto-clusters 3` clusters). Rendered headless 6 Oct 2026: 374 images, 0 page errors.

Limits (read before trusting a pile):
- Strips are the native bands, only ~52 px tall: a tall sign or an ascender/descender mark can be clipped; the tile is the
  whole band height around the sign, and the context view shows the neighbouring lines.
- Tiles are ink-profile blobs fitted to the transcribed token count (`fit.tsv`: 74->62, 59->57, 67->62, 54->45, 64->58
  blobs->tiles), so where signs touch or a sign is in pieces a tile can be one or two positions off its label. A bad cut
  goes to BAD-CUT, not a pile.
- The crop window (canvas x 4780-8110) is D2B-MATF110's; whether it holds each line's full length was not re-checked.

"Check these first" (`focus.tsv`, 54 tiles): every tile labelled BOX (17), z (20), T (5), U (5), w (4) or 4 (3), each
with what blind pass A and pass B wrote at that position. The owner's answer says whether these are separate signs or
unmarked variants of keyed ones (4/4+, w/w-, T/T=, BOX/BOX2), which the machine passes could not settle.

Apply after the owner's pass: `ArtifactData list` for piles/moves/newpiles, then
`python3 tools/sign_sorter_apply.py --labels sorter/labels.tsv --db DIR --out sorter/settled_labels.tsv --summary sorter/summary.json`
(from the target folder). A settled label is still a shape decision (grade I), not a value: it feeds the next key-
constrained decode of f.110 (NOTES.md "Remaining gaps", gap 2).

## Tile check (R7-MATQA, 6 Oct 2026, 01:56-02:0x UTC): NOT fit to hand on

Sorter rule (LANE-RUN7-account-2, 6 Oct 2026): 5+ random tiles checked against the line images. Method: the six band
strips (`pages/f110_L01..L06.jpg`, contiguous native bands canvas y 429-758) stacked into one 3330 x 329 image with the
band edges drawn, and each tile's box drawn on that stack (random.seed(20261006); no network).

What the stack shows: the region holds **five** written lines, not six, and they slope upward to the right (about one
band over the strip's width), while the bands are flat and only 51-60 px against a line pitch of about 66 px. So each
band cuts across lines: written line 1 sits at the bottom of L01 on the left and the top of L01 on the right; line 2
straddles L02/L03 on the left; line 3 straddles L03/L04; lines 4 and 5 fall mostly in L05 and L06. L03 is not an odd
line, it is the cut between lines 2 and 3, and the other bands carry pieces of their neighbours.

| tile | label | what the box holds |
|---|---|---|
| f110_L03_32 | L03-unplaced | the descender tail of a sign of written line 2 (right third), not a sign |
| f110_L03_06 | L03-unplaced | a 9 px sliver of a line-2 descender (the stem of a q-shape), not a sign |
| f110_L01_44 | w- | a fragment under the struck-through stretch at the right of line 1, not a w- |
| f110_L06_19 | m | a 34 x 13 px strip of faint ink between two signs, not an m |
| f110_L04_17 | e | a 9 x 4 px speck, no sign |
| f110_L05_12 | o | an 81 x 60 px box over two signs (a 5-shape and a T-shape), not an o |

6 of 6 off their label. Template: `build.sh` calls the current `tools/sign_sorter.py`, but without `--region`, so the
larger view cannot show a tile on the original page and a cut cannot be checked or fixed there.

Fix (not done here, over this job's cap): re-cut with `tools/sorter_recut.py` (deskew + one-tile-one-sign, as LL-RECUT /
PIS-RECUT): one Gallica fetch of the native region (canvas 116, x 4780-8110, y 300-860, the source of `images/f110/`, not
kept on disk), five line traces, reader columns from ciphertext.txt f110-1..5, rebuild with `--region`, then this check
again; about $3. Until then the sorter must not be published or put on the owner's card.

## Re-cut (R8-MATCUT, 6 Oct 2026, from 03:16 UTC): preflight PASS, tile check passed -- ready for the account-3 orchestrator to publish

What changed: `recut.py` (tools/sorter_recut.py, as Oldenbarnevelt R7-OLDFIX) replaces `build_inputs.py`'s flat bands;
`build.sh` now runs it and passes `--region region.json`. The v1 cut's tables are kept as `signs_v1.tsv`, `labels_v1.tsv`,
`focus_v1.tsv`, `fit_v1.tsv` (the v1 strip images `pages/f110_L0*.jpg` are dropped; `build_inputs.py` regenerates them).
- Region: Gallica btv1b9061879d canvas 116, x 4780-8110, y 300-860, native, fetched once (1 request, 6 Oct 2026, HTTP 200)
  as `region.jpg` (3330 x 560, 243 KB) -- the source D2B-MATF110 had cut its bands from and deleted.
- Lines: five traces that follow the written lines (row-ink peak per 200 px window, tracked from the left margin), checked
  by eye against the region; the lines rise ~25 px over the left two-thirds and 50-90 px over the last third. Pages
  `f110_W1..W5` = written lines 1-5. Strips 93 px (pitch 66, half 46).
- Cut: one tile per sign from the sign's own ink (rel 0.88, minpix 100, merge 0.25, x 25-3240 to keep off the margin and
  the page edge): 333 tiles (67, 70, 68, 64, 64) for 274 transcribed signs plus the untranscribed right ends of lines 1
  and 5 and the struck-through stretch of line 2.
- Starting piles: Bourdeau's ciphertext.txt labels placed by a shape-EM alignment (per-label prototype bitmaps, monotone
  DP per segment, 6 rounds): 232 of 274 tokens placed on a tile, 253 tiles within 30 px of a column; the rest start in
  the pile their shape cluster mostly holds. Segments (layout inference, grade I, see recut.py's docstring): at the right
  edge each written line's rising tail carries the END of the transcribed line above -- written line 2's right end is
  f110-1's tail "t m o h e BOX z q BOX 7 s n 1 e", line 3's is f110-2's "n 7 BOX q o ff z M o z ff", line 4's is f110-3's
  "e h z o d e U ff 7 6 z ff"; the right ends of written lines 1 ("... I x S T I ... w q 8 o t A v o ...") and 5
  ("... e w h ff t o m Y o T") match no transcribed line, and f110-5's tail "m Ze t 6 w- 7 z m f o" sits on written line 6
  (not tiled). So Bourdeau's f110-1..5 follow flat rows, not the written lines, at the right edge -- a transcription-layout
  observation for whoever next reads f.110, not settled here.
- Focus (36): 20 aligned tiles on the split labels BOX, z, T, U, w, 4 (in turn), then 16 shape-cluster tiles.

Preflight (`python3 tools/sorter_preflight.py <out>/matignon_f110_sorter.html --cipher-lines sorter/cipher_lines.tsv`):

    PASS template: ok, Fix the cut present, marker 2026-10-06.1
    PASS answerable: 36 focus tiles, 38 named piles of 38, 0 unanswerable
    PASS right line: 333 tiles; 0 tile(s) off the cipher lines, 5 of 5 listed lines have tiles; shape: 0 wide (>2.5x median 37 px), 2 strip-height boxes, 13 ink outside 3-60% of 333 measured; 14 = 4.2% (limit 5%)
    PASS contact sheet: 24 tiles beside their line strips (seed 20261006)
    preflight: PASS

Tile check (lane rule, 5+ random tiles against the line image): the preflight's own 24-tile contact sheet (seed 20261006),
opened tile by tile by this worker. **Cut: 22 of 24 hold one whole sign on the right written line**; 2 hold part of a sign
(W3_35 a sliver of the f before w; W2_62 part of a faint loop). **Starting pile: about 15 of 24 match the transcription's
sign at that place** (e.g. W3_26 o, W1_26 BOX, W3_34 f, W5_35 ff, W3_46 w, W4_53 z, W3_01 4+, W3_48 o, W3_49 z, W5_62 o);
off by one position or started by shape: W1_50 [Ze] holds a w, W4_10 [T] the 8-shape before the T, W4_59 [7] the H
before the 7, W4_37 [BOX] an m, W3_56 [4+] an o; W1_54 [t] and W1_57 [8] sit on line 1's untranscribed right end (shape
start). The v1 cut was 6 of 6 off. Piles are starting suggestions for the owner to move; a cut is fixed with Fix the cut.

Build: `sh ciphers/matignon-mayenne-1586/sorter/build.sh <out dir>` (no network; needs pillow, numpy, scipy, scikit-learn;
~5 s) -> `matignon_f110_sorter.html` (1.39 MB, 38 piles, 333 tiles, 59 provisional clusters) + `_region.jpg` + `.json`.
Publish (account-3 orchestrator): capabilities {"db": {}} as before; the apply step above is unchanged.
