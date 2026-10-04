You are transcribing a 16th-century drawn-symbol cipher (BnF fr.16142, letters of the French ambassador at Constantinople, 1574) sign by sign. This is a blind pass: do not decode, do not guess plaintext, just name every sign you see.

REFERENCE TABLE: read the image TABLE_PATH (S. Tomokiyo's reconstruction of this cipher). Top row = letters a b c d e f g h i l m n o p q r s t u x y z, then "double" and "nulls". Under each letter, its symbols are stacked top to bottom: the 1st symbol under a letter is row 1, the 2nd row 2, etc. The lower three bands are nomenclator (whole-word) signs with the word printed above each.

LABELS (one token per sign):
- cipher letter sign: letter + row number, e.g. a1 (caret ^), a2 (inverted T), a3 (alpha loop), d1 (theta with a tail), x1 (X cross).
- the plain hash # (it stands under both o row 1 and e row 2): write o1/e2.
- double-letter signs (column "double"): D1, D2, D3 (top to bottom).
- nulls: N1..N16, reading the nulls block left to right, top row first (row 1: N1-N4, row 2: N5-N8, row 3: N9-N13, row 4: N14-N16).
- nomenclator signs: W:<word as printed>, e.g. W:roy, W:le, W:que, W:par, W:ont, W:qui, W:faict, W:sieur, W:vous.
- Label conventions already settled for this hand (use them): 2-with-stem-circle = n1; 6-with-a-cross-above = t2; a box hanging from the top bar with the stem running down = W:le (W:roy has a cross above its box); loop-S = e3; cup-on-stem = s2; theta-with-tail = d1.
- if you cannot match a sign to the table: ?{short description}. If you match it but are unsure, append ? to the label (e.g. n1?).
- ignore ticks, flourishes, dashes at the ends of lines, ink blots, and any cursive clear (plain-language) words.

CROPS: each manuscript line is cut into two images, LINE_s1.jpg (left half) and LINE_s2.jpg (right half), which overlap. A thin RED vertical line is drawn on each: on _s1 near the right edge, on _s2 near the left edge. Transcribe on _s1 only the signs whose centre is LEFT of the red line, and on _s2 only the signs whose centre is RIGHT of the red line; then each sign is counted once. Line L00 is a single image with no red line (the cipher tail of a line that begins in clear text; transcribe only the cipher signs).

Read these lines, in this order: LINES
Crop files are in CROP_DIR, named c510_<line>_s1.jpg / c510_<line>_s2.jpg (L00: c510_L00_s1.jpg only). Look at every image with the Read tool; zoom-in is not available, so look carefully at each sign.

OUTPUT: write the file OUT_PATH with one row per manuscript line: the line id (e.g. L05), a TAB, then that line's signs left to right separated by single spaces (s1 part then s2 part, joined). No header, no comments, nothing else. Then reply with just: the number of lines written and the total number of signs.
