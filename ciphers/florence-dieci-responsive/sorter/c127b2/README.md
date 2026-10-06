# Sign sorter inputs, Florence Dieci c.127 lines L02-L18 (R10-FLOR2, 6 Oct 2026) -- NOT PUBLISHED

Second sorter for ASFi, Dieci di Balìa, Responsive filza 8 c.127 (DECODE R3766, 26 Dec 1430): the 17 cipher lines of the
main block, crops `images/c127b2/c127b2_L02..L18_s1/s2` (GAPS106). The first sorter (`../README.md`, ASKS 107) covers only
the pilot lines 6-9. 625 tiles in 30 piles; 71 attached marks; 22 tiles in "Check these first".

**Piles are provisional machine shape clusters** (`tools/glyph_atlas.py cluster`, k=30, fixed seed), named k01..k30.
No machine or model pass has read these lines; no label is a sign name and nothing here carries a value. The owner
merges, splits and renames the piles into the leaf's signs (the pilot sorter's names, `../../c127_signs.md`, are the
natural target).

Boxes: `glyph_atlas.py segment --mark-h 0.7 --min-area 0.25 --median-h pool` (the shared scale added by R10-FLOR2;
pool = 48.5 px over these 33 crops, whose own medians ran 4-72 px). Clear text removed by eye: L02_s1 before x 420
("ghalio"), L18_s1 from x 1045 (the "/" and "...medite delcquan..."), all of L18_s2. The 100 px s1/s2 overlap is split at
its middle so a boundary sign is one tile. Boxes touching the crop's top or bottom edge (144) are trimmed to the ink
run holding the line centre (a neighbour line's descender otherwise rides along). Lines L03-L17 were not eye-checked
for clear words beyond GAPS106's note; L08_s1 has letter-like forms ("a b a b") asked about in the focus box.

Build and gate (run from `ciphers/florence-dieci-responsive`):

    python3 sorter/c127b2/build_inputs.py <scratch>    # signs, labels, marks, focus, cipher_lines (.tsv); deterministic
    python3 ../../tools/sign_sorter.py --signs sorter/c127b2/signs.tsv --labels sorter/c127b2/labels.tsv \
      --marks sorter/c127b2/marks.tsv --pages images/c127b2 --focus sorter/c127b2/focus.tsv \
      --clusters sorter/c127b2/labels.tsv --title "Florence c.127 Lines 2-18 Sorter" \
      --lede "Dieci di Balia, Responsive filza 8 c.127 (26 Dec 1430), cipher lines L02-L18 of the main block. Piles are provisional machine shape clusters (k01-k30), not readings: merge, split and rename them into the signs of the leaf." \
      --out <scratch>/florence-c127-L02-L18-sorter.html
    python3 ../../tools/sorter_preflight.py <scratch>/florence-c127-L02-L18-sorter.html --cipher-lines sorter/c127b2/cipher_lines.tsv

Preflight, 6 Oct 2026 (page 6.0 MB, built headless; not published):

    PASS template: ok, Fix the cut present, marker 2026-10-06.1
    PASS answerable: 22 focus tiles, 30 named piles of 30, 0 unanswerable
    PASS right line: 625 tiles; 0 tile(s) off the cipher lines, 33 of 33 listed lines have tiles; shape: 6 wide (>2.5x median 75 px), 7 strip-height boxes, 14 ink outside 3-60% of 625 measured; 27 = 4.3% (limit 5%) [list: sorter/c127b2/cipher_lines.tsv]
    PASS contact sheet: 24 tiles beside their line strips -> florence-c127-L02-L18-sorter.preflight.png (seed 20261006; eye it before publishing)
    preflight: PASS

The first build failed the right-line check at 6.1% (20 strip-height boxes, neighbour-line strokes); the trim step
brought it to 4.3%. Contact sheet eyed by R10-FLOR2: cuts sit on single signs; two misfits seen (a dot fragment on
L08_s1, a speck before the "/" on L18_s1), both BAD-CUT material for the owner.

**Before publishing** (account-3 orchestrator, the publisher of the first sorter): the same image-terms check as
`../README.md` (R3766 scan from DECODE; no RESTRICTED.md in the folder), and publish from the owner account
(`--expect-owner-account`, ASKS 145) or say which account it is private to.
