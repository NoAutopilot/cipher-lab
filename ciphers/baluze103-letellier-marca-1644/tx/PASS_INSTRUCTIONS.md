# Blind transcription pass, Baluze 103 f.50 (R7A-BAL103, 6 Oct 2026)

You transcribe a 1644 French cipher letter sign by sign. Do NOT decode, do not guess plaintext, do not read other passes.

Reference: `tx/key_sheet_3x.png` (S. Tomokiyo's table of the cipher's signs) and `key.tsv` (column 1 = the NAME to write for
each sign; column 4 describes its shape; the table image shows each shape under its letter column, numeral row first).

For every crop listed in your task, open it with the Read tool (one crop at a time; never open the full page image) and write
the signs left to right as space-separated tokens:
- Numerals: write the number as the clerk grouped it, e.g. `14`, `9`, `7`, `13`, `22`. The clerk writes 9 like a cursive `g`
  -- write it `9`. Two-digit numbers 10-23 are single tokens (`19`, not `1 9`). A lone 3, 4, 5, 6, 7, 8 or 9 is its own token.
- A number or sign with a bar over it: prefix `=`, e.g. `=11`, `=12`, `=9`, `=32`.
- Graphic signs: the NAME from key.tsv column 1 whose shape matches (e.g. `u`, `a`, `t`, `mt`, `delta`, `theta`, `hz`, `ct`,
  `xbar`, `eps`, `mm`, `y`, `f`, `P`, `l`, `n`). If two names fit, write both joined by `|`, best first (`x|xc`).
- A sign that matches nothing in the table: `?` plus a few-word description in braces, e.g. `?{loop like 2}`.
- Ordinary French written in clear among the cipher (e.g. "et tous"): write it in square brackets `[et tous]`.
- Ignore dots, commas and line-end dashes that are punctuation. Ignore ink bleeding through from the other side (faint, mirrored).

Output: a TSV file, one row per crop: `<crop id>\t<tokens>`, crop id = the file name without `.jpg` (for split lines write
`_s1` and `_s2` rows separately; signs in the overlap between s1 and s2 appear in both -- mark the first sign of s2 that is NOT
in s1 by prefixing it with `|>`). End with a line `# notes:` listing signs you were unsure of.
