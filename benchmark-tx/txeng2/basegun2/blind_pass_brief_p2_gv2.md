# Blind transcription pass, WVO 8246 MS p.2 (TX-POOL-LEAF, 9 Oct 2026)

You are one of two independent readers of the cipher signs on crops of a 16th-century German letter (one manuscript page,
25 cipher lines). The pass is VALUE-BLIND: you label each hand-drawn sign by its SHAPE only, from the label list below. You do
not know, and must not look up, what any sign means.

Read ONLY the files named in this brief and your task: the 25 crops `crops/p2_L01.jpg` .. `crops/p2_L25.jpg`, the 10
calibration crops `sheet/p1cal_L01.jpg` .. `sheet/p1cal_L10.jpg` and `sheet/calibration.tsv` (all under
benchmark-tx/txpool/gunther8246-p2/). Do not open any other file in this repository (no NOTES.md, no key, no other pass, no
other image of this letter, no build script); the pass is void if you do.

## The crops

25 crops, one per cipher line, top to bottom of the page (L01 = top line). Each crop is the whole line. Pieces of the line
above or below may show at the crop's edge (a descender, an ascender); they belong to the neighbouring line: ignore them.
The crops are about 1050 px wide with signs about 25-40 px tall: do not resize them (no enlarging, no re-cutting,
no image processing): view each crop as it is, and read in short stretches, left to right. Signs are separated by spaces; a label can
cover several letter-like strokes written together (cc, ps, aaa, 88): one label = one space-separated sign group.

Crop note (written by tools/iiif_lines.py --overlap-note):
- p2: each line is one crop (no segments, no overlap).

## Calibration (shape names, from another page of the same letter)

`sheet/calibration.tsv` gives, for each calibration crop (MS p.1, a different page; you are NOT transcribing it), the labels
an earlier reader gave its signs, left to right. Use it only to learn which shape each label names. It is not a key and says
nothing about meaning.

## Labels (shape only; use these exact labels)

Signs that look like letters or digits are labelled with the letters/digits they look like, written as one group:
- digit groups as seen: `01` `101` `3` `33` `34` `44` `48` `53` `58` `60` `67` `7` `77` `8` `87` `98` `4000` (the 4 is often
  written with a crossed stem; 60 often looks like "6o"). A digit group struck through or underlined: see decorations below.
- letter groups as seen: `f` (long f/s with a cross-bar: the most common sign), `r`, `m`, `v`, `a`, `c`, `t`, `z`, `x`,
  `cc`, `oo`, `or`, `rr`, `zz`, `dd` (two d's, often with a bar), `ii`, `aa` (two a's, no bar), `aaa` (three a's),
  `p` (a long descending looped p alone, no s joined), `ps` (a long descending p joined to s), `hs` (h joined to s), `xr` (x joined to r; may look like "xv"), `rf` (a small t or r
  joined to an f; looks like "tf"), `of`, `rp`, `vt`, `vi`, `ut`, `xn` (x followed by ii/n, looks like "XII"), `xm` (x followed
  by m or iii, looks like "xııı"), `xy`, `lx`, `tn`, `cro`, `bbb`.
Signs with a special shape:
- `d`  an uncial d: a round bowl with a stem leaning back over it to the left (like ∂ / ð)
- `d6` a 6-like or ɓ-like sign: a bowl at the bottom, the stem rising and curving over to the right
- `b`  a large looped sign like a reversed 6 / a b whose loop opens to the left (often taller than its neighbours)
- `6`  a small o with a tail rising to the upper right (σ / ơ-like), smaller than d6
- `g`  a 9-like sign: a small bowl with a long tail descending below the line
- `q`  a small circle sitting on a straight descending stem (a lollipop, ♀ without the cross)
- `phi` a circle with a vertical stroke through it reaching below the line (φ)
- `th` an o / 0 crossed by a horizontal stroke (θ); the stroke often runs out beyond the o on both sides
- `ob` a small o / 0 with a horizontal bar above it (often a second bar below it)
- `od` a circle with a dot in its centre (⊙)
- `o`  a plain small o (no bar, no dot, no tail)
- `x+` an x with a vertical stroke through its centre (asterisk-like ✱)
- `xb` an x with a bar above it; `x_` an x with a bar below it (underlined)
- `Ib` a capital I with cross-bars at top and bottom (a Roman I, ⌶); `Ib+` the same with an extra stroke through it
- `]`  a square bracket open to the LEFT (⊐: top and bottom bars joined on the right)
- `L`  a square bracket open to the RIGHT (⊏: like a square C)
- `sq` a small square box □; `sqt` a small square with a vertical stem standing on its top
- `tau` a c- or e-like hook with a long curling tail
- `ro` a large open horizontal loop (a v or w that curls round into a loop on the left)
- `Ol` a large looped scribble like a cursive "Ol" with a comma-like stroke after it
- `fb` an f joined to a b-like loop; `tb` a b with a cross on its top
Decorations (add to the label of the plain sign): struck through by a horizontal stroke -> `x` suffix only for 88 (`88x`);
a bar ABOVE two a's -> `aab` (āā); underlined digits or letters -> `_` suffix (`44_`, `xr_`, `x_`).
- `BLOT` an ink blot covering a sign.

A sign that fits none: `NEW:<short description>` (e.g. `NEW:hook-with-cross`), and use the same description every time you
meet that shape. Unreadable mark: `?`. A sign struck through by the writer (other than 88x): still give it a row, write
`struck` in note.

## Output

Write exactly one TSV file at the path your task names, header exactly:

    passage	pos	sign_id	alt	conf	note

- `passage`: L01..L25 as the crop names; `pos`: 1-based position within the line.
- `sign_id`: a label above, or `NEW:...`, or `?`. `alt`: a second label if two fit, else blank.
- `conf`: H (clear), M (plausible, one look-alike), L (guess). `note`: a few words on the shape when useful.

No other output file in the repository. When done, report in a short paragraph: sign count per line, how many NEW: and ?
rows, which labels you found hardest to tell apart. Do not decode, do not guess at meanings, do not describe the content.
