# PAGEMAP -- every region of every public page image (DEB-SWARM-E, 29 Sept 2026)

Public copies only: the seven PNGs in `images/` (Schmeh, Cipherbrain / scienceblogs.de, fetched 25 and 28 Sept 2026;
`images/manifest.json`). Nothing here comes from the museum's restricted scans (RESTRICTED.md).
Pixel boxes are `x0,y0,x1,y1` in the image's own pixels. Cipher-line boxes are computed from the segmentation
(`glyphs/signs.tsv` + `glyphs/pages.json`) by `line_boxes.py` -> `line_boxes.tsv` (all 56 lines, exact);
every pictogram-class box is in `pict_boxes.tsv` (raw box labels; the settled drafts differ in a few places, below).
Drawing and clear-text boxes are read by eye on crops of the same PNGs, accurate to about +-10 px (marked ~).
Medium: "ink" = dense black line; "pencil" = grey graphite shading; judged by tone on the scan, grade M.
Grades: H seen plainly; M probable; L a guess.

## Cryptogram 1 -- Debosnys-Cryptogram-1.png (1111 x 481; a crop of a larger sheet)

| region | kind | box | medium | notes | grade |
|---|---|---|---|---|---|
| c1_L01-L06 | cipher, 6 lines | 470,37,1105,407 (per line: line_boxes.tsv) | ink | lines sit to the right of the portrait; every line's left edge is the portrait's right edge (x ~470) | H |
| portrait | drawing, man, bust, head turned to viewer's left, dark hair, moustache, goatee, jacket, bow tie | ~120,85,440,481 | ink, pen hatching | on this page, not show-through (NOTES.md item 4 calls it a faint pencil bleed-through; the scan shows a dense ink drawing). Beside all six cipher lines | H |
| signature | clear text "H.D. Debosnys" (two dots flank it) | ~600,410,965,470 | ink | under line 6, centred on the cipher block | H |
| in-line pictures | horse (L01 pos 17), sun with face (L02 pos 1), small face (L02 pos 20), running/flying figure (L03 pos 23), tree (L04 pos 9) | pict_boxes.tsv | ink | the horse faces a small standing figure/post drawn just right of it (L01 ~1010-1030) | H |
| show-through | faint rows of cipher-like signs from the reverse | top strip ~440,0,1111,25; right margin ~1000,100,1111,300 | -- | the reverse of this sheet carries cipher-like writing. If c2b is the reverse (next row), this is c2b's text mirrored | M |

## Cryptogram 2, page a -- Debosnys-Cryptogram-2a.png (1053 x 1527)

| region | kind | box | medium | notes | grade |
|---|---|---|---|---|---|
| page number | clear "N: 9" | ~815,25,895,70 | ink | | H |
| show-through, top | faint mirrored "No 10" | ~560,55,700,100 | -- | read mirrored on an autocontrast crop: "No 10", the heading of the c3 page. With the next row, evidence that No.9 (c2a) and No.10 (c3) are the two sides of one leaf | M |
| still life | cube with the digits 6 (left face), 1 (top), 5 (front); an ornate pitcher; a small tumbler | cube ~752,165,848,242; pitcher ~868,160,945,250; tumbler ~955,210,985,245 | ink (pitcher densely stippled) | above the right half of L01. The cube shows 6 and 1 as neighbouring faces, which a real die cannot (they are opposite); it is a device for the digits 1, 5, 6. Same three digits as the clear "516" in L02 | H |
| portrait | drawing, a figure in a wide-brimmed bonnet with a plume, head and shoulders, cut off by the left edge of the scan | ~0,0,260,690 | pencil | beside L01-L06, whose left ends step right to avoid it (L02 x0 203, L03 206 vs L08 2). Letters on the shoulder, ~60,600,170,670, read "oLvrip." or "Olwrip." (L; not settled) | H (drawing), L (letters) |
| c2a_L01-L17 | cipher, 17 lines | 2,240,1052,1527 | ink | | H |
| L02 clear digits | "516" | L02 boxes 14-16 (clear_spans.tsv) | ink | right after the sun; the cube above shows the same digits | H |
| L09 clear capitals | "H.D.D.L.M.F." with dotted underlining | L09 boxes 7-14 (clear_spans.tsv), ~275,860,545,905 | ink | | H |
| L03 start | eagle, wings spread | 206,404,281,479 | ink | PICT-EAGLE in the drafts | H |
| L04 start | wavy horizontal drawing ending in a hook with a small "venus" mark: a serpent or cord | ~240,490,370,530 | ink | boxes 1-4 are `_` in the settled draft, so the drafts carry no sign for it; L04 is a pictogram-initial line not counted by H31 | M |
| L05 start | house | 245,555,288,603 | ink | PICT-HOUSE | H |
| L07 | tree (pos 17), arrow, figure, three stars | pict_boxes.tsv | ink | | H |
| L08 | crossed tools/sticks (pos 11) | 247,783,314,827 | ink | PICT-CROSSED | H |
| L10 interior | bird in flight, wings raised | ~130,905,240,975 | ink | no box in the segmentation (between box 4 at x 112 and box 5 at x 198); the drafts carry no sign for it | H |
| L10, L12 | sun (L10 pos 9), fish (L10 pos 16), barrel (L10 pos 20), leaf (L12 pos 18), jug (L12 pos 35, line end) | pict_boxes.tsv | ink | | H |
| L13 | tree, house with a wavy line "XIX" above it, a cup with a "W" inside at line end | pict_boxes.tsv; cup ~990,1155,1030,1200 | ink | the cup is BUCKET in the drafts | H |
| L15 start | anchor, then a church with a tower beside a palm or willow, a fence of short strokes "IIIIIXO" drawn under it | anchor 40,1292,84,1351; church+tree ~155,1275,290,1350; caption ~160,1345,215,1362 | ink | the church and tree have no box; the caption strokes are boxes 4-8, coded BLOB BAR-SOLID BAR-SOLID BAR-SOLID BAR-THIN in the settled draft. Two of the three BAR-SOLID BAR-SOLID pairs in the whole text (H41's excess bigram, 3 vs 0.4) are this caption | H |
| L16 | "W" monogram (two interlaced chevrons, a dot below) | 127,1375,177,1431 | ink | PICT-CROWN in the drafts. The same mark stands alone in the left margin of c4a | H |
| L17 | anchor (pos 6), bird with long tail (line end) | anchor 173,1458,248,1499; bird 923,1430,1023,1498 | ink | the anchor is MULTI in the settled draft (dropped as punctuation class by H31); the bird is PICT-BIRD | H |
| right edge | page-edge bar | x 1028-1052 on most lines | -- | coded `_` except c2a_L02 pos 28 = DASH-V (5 px wide at x 1047): an edge artefact carried as a sign; it hides the cup (BUCKET) as L02's last sign | H |
| stains | brown water/ink stains | ~600,110,720,190; ~870,120,980,160 | -- | above the still life | H |

## Cryptogram 2, page b -- Debosnys-Cryptogram-2b.png (1103 x 831)

| region | kind | box | medium | notes | grade |
|---|---|---|---|---|---|
| c2b_L01-L09 | cipher, 9 lines | 94,6,1103,760 | ink | L08 and L09 are short and centred | H |
| L01 interior | mason's trowel | 237,42,323,93 | ink | coded PICT-LEAF (pos 7) in the drafts: a label error; the shape is a trowel (handle, triangular blade) | H |
| L02 interior | long-handled hammer or pick, head at right; then three linked rings | hammer ~245,105,375,160 (no box); rings 382,124,473,150 | ink | the hammer has no box; the rings are CHAIN (pos 5), outside the pictogram class of h3/H31 | H |
| L03, L07 | sun with face (L03 pos 12; L07 pos 1) | pict_boxes.tsv | ink | | H |
| L07 start | dove with an olive sprig, flying toward the sun | ~45,420,140,520 | pencil | no box; L07 therefore opens with the dove, then the sun | H |
| faint portrait | man, frontal, dark hair and beard, jacket | ~470,300,900,831 | faint | the cipher of L05-L09 is written over it. Only the hair, moustache and goatee are dark; the rest is faint. A mirrored copy of the c1 ink portrait matches it in head size (~300 px), hair mass and beard shape: probably show-through of the c1 portrait, so c1 and c2b are probably the two sides of one sheet | M |
| L09 left | handshake: two hands clasped, cuffed sleeves | ~20,700,260,800 | pencil | the boxes 1-7 of L09 (`_`) fall on this drawing | H |
| clear capitals | "L.M.F." | ~265,785,390,815 | ink | beside the handshake, at the foot of the page | H |
| L09 end | arrow-like sign after "*o" | 850,623,899,678 | ink | PICT-ARROW | H |
| show-through | faint rows of cipher-like writing, left margin | ~0,280,450,700 | -- | from the reverse | M |

## Cryptogram 3 -- Debosnys-Cryptogram-3.png (1107 x 1375)

| region | kind | box | medium | notes | grade |
|---|---|---|---|---|---|
| page number | clear "No 10" | ~150,35,290,75 | ink | | H |
| couple | man in top hat and woman in a long dress, walking arm in arm, seen from the side | ~65,130,165,305 | ink | beside cipher lines 1-2 | H |
| c3_L01-L04 | cipher, 4 lines | 150,172,1107,416 | ink | L01 opens with a running/flying figure (PICT-RUNNER); L04 ends "?...." | H |
| L02 end | a cup with "M" inside | ~1055,250,1080,290 | ink | BOX-M in the drafts | H |
| faint portrait | a young figure with a round bonnet/halo, shoulders | ~580,60,940,540 | faint | under L01-L04 and poem lines 1-3. Probably show-through of the c2a bonnet portrait (c2a shows c3's "No 10" mirrored) | M |
| clear poem | French, 14 lines, "Oh! mes amis je vous supplie en grâce ..." (clear_poems.tsv) | ~50,480,930,1340 | ink | | H |
| owl | owl perched on a branch | ~900,655,1010,910 | ink | beside poem lines 4-9 ("montrez moi un peu d'humanité" to "Ah! offrez moi vos mains en bons amis?") | H |
| arrow | arrow pointing right | ~965,1245,1055,1275 | ink | beside poem line 13; with "No 11 (next page la suite)" | H |
| continuation note | "No 11. (next page la suite)" | ~790,1300,1100,1335 | ink | a page No 11 exists or was planned; it is not among the public scans | H |
| patch | grey rectangle (paper, tape or repair) | ~940,0,1107,130 | -- | | H |

## Cryptogram 4, page a -- Debosnys-Cryptogram-4a.png (1107 x 1493)

| region | kind | box | medium | notes | grade |
|---|---|---|---|---|---|
| monogram | bird (eagle or hawk) holding a key (or a cross-hilted key) in its beak, a banner above "HENRY.D.DEBOSNYS", a second banner below with the same name upside down | ~360,10,720,265 | ink | above the title, not beside any line | H (bird, banners); M (key vs cross) |
| title | clear "monographe. verse." (the ph written with a long-s-like stroke) | ~510,290,1085,370 | ink | | H |
| margin mark | "W" monogram, two interlaced chevrons with a small circle below | ~10,335,90,415 | ink | same shape as the in-line PICT-CROWN of c2a L16. Beside the title/first verse line | H |
| show-through | faint mirrored "(Gre[ek translation])" and "EIII" | ~180,225,300,260 and ~745,225,800,260 | -- | the verso's heading and first Greek word; confirms c4a/verso are one leaf (as Schmeh's composite shows) | H |
| c4a0_L01, c4a_L01-L14 | cipher verse, 15 lines (Schmeh's red numbers 1-15) | 304,375,941,1485 | ink | line-initial pictures: heart (verse line 2), sun (4), leaf (13), anchor (14) | H |
| L10 | leaping/flying figure (pos 4), house or hut (pos 11) | pict_boxes.tsv | ink | inside the stained band | H |
| stain/tape | horizontal band of tape or paste | ~90,1130,1107,1340 | -- | over verse lines 11-13; a small standing figure at ~690,1190,725,1235 sits inside it, read by nobody yet | M |
| fold | vertical fold | x ~440 | -- | runs through every verse line | H |

## Cryptogram 4, page b -- Debosnys-Cryptogram-4b.png (1105 x 563)

| region | kind | box | medium | notes | grade |
|---|---|---|---|---|---|
| c4b_L01-L05 | cipher verse, 5 lines (Schmeh 16-20) | 356,26,902,395 | ink | | H |
| signature | clear "Hênêcos Debosnostys." | ~530,475,1095,525 | ink | | H |
| fold | vertical fold | x ~440 | -- | continues c4a's | H |

## Verso -- Debosnys-Poem-verso.png (1655 x 1332)

Schmeh's composite, not a single page: left half is the cipher verse (4a+4b) with red line numbers 1-20 added by
Schmeh; right half (x ~830-1655) is the reverse of the 4a leaf.

| region | kind | box | medium | notes | grade |
|---|---|---|---|---|---|
| heading | clear "( GreeK translation. )" | ~1280,65,1630,110 | ink | Debosnys's label: he calls the Greek the verse's translation | H |
| Greek poem | 20 lines, Greek, beginning "Ἐπὶ ῥοδίνοις τάπησι" (Moore's Greek preface ode to his Anacreon, per Sektu 2017; altered, cut before the end) | ~900,70,1260,1185 | ink | one Greek line per cipher line in Schmeh's alignment | H |
| end mark | "?" | ~1225,1140,1245,1185 | ink | after Greek line 20 | H |
| show-through | "W" monogram; anchor; leaf; cipher rows | W ~1455,150,1510,215; anchor ~1430,915,1460,955; leaf ~1430,860,1460,900 | -- | c4a's margin mark and verse lines 13-14 seen from behind | H |
| margin line | vertical ruled line | x ~1528 | ink | | H |

## Which cipher line sits next to which picture (margin and page drawings, not in-line signs)

| picture | page | lines beside it |
|---|---|---|
| man, ink portrait | c1 | c1 L01-L06 (all) |
| bonnet portrait | c2a | c2a L01-L06 |
| cube 6/1/5, pitcher, tumbler | c2a | above c2a L01 (right half); L02 carries the clear "516" |
| couple walking | c3 | c3 L01-L02 |
| owl | c3 | clear poem lines 4-9 |
| arrow | c3 | clear poem line 13-14 (to "No 11") |
| dove with olive sprig | c2b | opens c2b L07, next to the sun |
| handshake + "L.M.F." | c2b | below/left of c2b L09 (page foot) |
| faint frontal man (show-through?) | c2b | under c2b L05-L09 |
| bird with key + name banners | c4a | above the title, over verse line 1 |
| "W" monogram | c4a margin | beside verse line 1 |

## Corrections for the merge (nothing in the drafts is edited here; transcriptions are never silently repaired)

1. Drawings inside cipher lines that the settled drafts do not carry as a pictogram token: c2a L04 start (wavy
   serpent/cord, boxes 1-4 `_`), c2a L10 bird in flight (no box), c2a L15 church with tree (no box; its caption strokes
   are five ordinary-looking tokens), c2a L17 anchor (MULTI, dropped by H31's punctuation filter), c2b L02 hammer (no
   box), c2b L07 dove (no box). Mislabelled: c2b L01 trowel as PICT-LEAF; c2b L02 three linked rings as CHAIN
   (outside the pictogram class). `pict_tests.py` E2 re-runs H31 with these corrections: line-initial 12 of 56 vs
   band 0-7 (mean 3.2), p < 0.0001 -- H31 holds and gains one line (c2a L04).
2. c2a L15 boxes 4-8 (BLOB BAR-SOLID BAR-SOLID BAR-SOLID BAR-THIN) are the church drawing's caption, not cipher; they
   supply two of the three BAR-SOLID BAR-SOLID bigrams H41 lists among its excess pairs.
3. c2a L02 pos 28 DASH-V is the page edge (x 1047, 5 px wide). Every other edge box is `_`.
4. NOTES.md item 4 (LANE B2): the c1 portrait is an ink drawing on the page, not a pencil bleed-through; the c2b
   drawing is a handshake (two clasped hands), not "a hand holding a scroll".
5. Leaf pairs (M): c2a/c3 (No.9/No.10, mirrored "No 10" on c2a, bonnet portrait show-through on c3) and c1/c2b (the
   c1 portrait showing through on c2b). If both hold, cryptogram 2 runs across two leaves whose other sides are
   cryptograms 3 and 1: a physical order c1|c2b and c2a|c3, which a transcription pass could check on the museum's
   originals only (not ours to request here).
