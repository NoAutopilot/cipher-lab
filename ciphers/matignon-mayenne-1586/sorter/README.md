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
