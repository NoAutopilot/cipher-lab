# R11A-AVS53 blind pass brief: WVO 53 cipher postscript at native resolution (6 Oct 2026)

Crops: `images/crops_r11a53/53n_L01.jpg` .. `53n_L10.jpg` (p1, f.266r, 10 lines) and `53p2n_L01.jpg` .. `53p2n_L03.jpg`
(p2, f.266v, 3 lines), cut by `tools/iiif_lines.py --image --deskew` from the native page JPEGs inside Huygens PDF 00053
(p1 2633x4175 gray, region 600,2240,2000,1220; p2 2567x4187, region 640,170,1820,400). Each crop is one cipher line;
slivers of neighbouring lines may show -- transcribe ONLY the main line through the vertical middle, left to right.
On p2 L03 the cipher ends at a dot followed by a large flourish and German handwriting: stop at that dot. On p1 L09 a
small looped flourish (~) between signs is NOT a sign. Open only your assigned crop files. Do NOT read any other file in
this repository (no NOTES, no key, no other pass, no earlier transcription).

Output: long-format TSV, header `line	pos	sign	conf`, one row per sign; line = `53_L01` .. `53_L10` (p1) or `53p2_L01` ..
`53p2_L03` (p2); pos from 1; conf H (sure) or M (doubtful). Append after EVERY line so nothing is lost.

Code book (use exactly these codes; a sign that fits none gets `NEW1`, `NEW2`... plus a comment row `#NEW1 <description>`):
- digits `0`-`9` as themselves. `1` is a short upright stroke. In this hand `5` and an S-shape are the same sign: write `5`.
- `X` a plain x / saltire. `Xk` an x with an extra bar or star-like crossing (✱). Two x's side by side are two `X` rows.
- `V` a v / small check shape.
- `Z` a z, with or without a bar through it (Ƶ); in this hand it can look like a 2 with a bar: if barred, `Z`.
- `F` a long s / f with crossbar (ƒ), a tall sign with a loop on top and a bar.
- `G1` Λ (capital open tent, both legs equal, no base). `G7` λ (lambda: one long stroke from top-left to bottom-right
  and a short leg off it). If unsure which, `G1` with conf M.
- `G2` Δ (closed triangle). `G3` ϖ (w-like loop squiggle under a bar, "ϖ"). `G4` π (bar with 2-3 legs).
- `G6` ε (small epsilon / backward 3; distinguish from the digit 3).
- `SG` σ-shape: a small open loop with a stroke out to the upper right (like Greek final sigma or a leaning 6),
  when it is clearly not a normal digit 6. If you cannot tell, write `6` with conf M.
- Punctuation: a dot `.` -> `DOT`; a colon `:` -> `COL`. A closing flourish is NOT a sign.

Stop when your assigned lines are done. Report one line: rows written and the NEW codes used.
