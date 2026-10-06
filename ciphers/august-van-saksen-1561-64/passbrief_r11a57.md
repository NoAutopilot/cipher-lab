# R11A-AVS57 blind pass brief: WVO 57 p3 cipher block at native resolution (6 Oct 2026)

Crops: `images/crops_r11a57/57n_L01.jpg` .. `57n_L07.jpg`, cut by `tools/iiif_lines.py --image` from the native page JPEG
inside Huygens PDF 00057 (p3, 1932x3247, about 295 dpi; region 380,1740,1420,520). Each crop is one cipher line; slivers
of the neighbouring lines may show -- transcribe ONLY the main line through the vertical middle, left to right.
Open only your seven crop files. Do NOT read any other file in this repository (no NOTES, no key, no other pass, no
earlier transcription).

Output: long-format TSV, header `line	pos	sign	conf`, one row per sign; line = `57_L01` .. `57_L07`; pos from 1;
conf H (sure) or M (doubtful). Append after EVERY line so nothing is lost.

Code book (use exactly these codes; a sign that fits none gets `NEW1`, `NEW2`... plus a comment row `#NEW1 <description>`):
- digits `0`-`9` as themselves. `1` is a short upright stroke. `0` may carry a slash through it: still `0`.
- `X` a plain x / saltire. `XX` two x's written as one joined pair. `Xk` an x with an extra bar or star-like crossing (✱).
  `Xy` an x with a descending tail (y-like).
- `V` a v / small check shape. `VmV` one joined group V + a w-like loop + V (read as one sign).
- `Z` a z (in this hand it can look like a 2). `Zb` a z with one crossbar. `ZZ` a z with two bars / a double-barred z.
- `T` a capital T. `S` a capital S. `J` a J / long hooked stroke. `TL` T and L joined as one sign. `F` long s / f with
  crossbar (ƒ).
- `G1` Λ (open tent, no base). `G1h` a tent with a hook at its right foot. `G2` Δ (closed triangle). `G3` ϖ (w-like
  loop squiggle, "ϖ"/"ѡ", may carry a tick or radical-like stroke in front -- the whole thing is one G3). `G4` π (bar
  with 2-3 legs). `G6` ε (small epsilon / backward 3; distinguish from the digit 3).
- `EL` a large capital-height sign like a barred E / Ʒ with two or three bars (bigger than the other signs).
- `THE` a circle under a cross (orb, ♁). `OQ` a circle with a tail / loop (Q-like). `BOX` a square □.
- Punctuation: a dot `.` -> `DOT`; a colon `:` -> `COL`. A closing flourish at the end of the block is NOT a sign.

Stop when the seven lines are done. Report one line: rows written and the NEW codes used.
