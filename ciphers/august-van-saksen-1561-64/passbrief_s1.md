# S1 blind pass brief: 53 p1 postscript and 57 p3 cipher block (24 Sept 2026)

Crops: `images/crops_s1/53_L01.png` .. `53_L12.png` (12 lines, from images/00053_p1.png) and `57_L01.png` ..
`57_L07.png` (7 lines, from images/00057_p3.png). Each crop is one cipher line; a crop may show slivers of the
lines above/below -- transcribe ONLY the main line running through the vertical middle. Read left to right. If a
crop is ambiguous, you may open the full page image for context (53: y 895-1365, x 355-1090; 57: y 588-760,
x 218-670). Do NOT read any other file in this folder (no NOTES.md, no key, no other pass).

Output: long format TSV, header `line	pos	sign	conf`, one row per sign; line = `53_L01` etc., pos from 1;
conf H (sure) or M (doubtful). Write the file after EVERY line (append), so nothing is lost.

Code book (use exactly these codes; a sign that fits none gets `NEW1`, `NEW2`... and a one-line description in a
comment row `#NEW1 <description>` at the end of the file):
- digits `0`-`9` as themselves. NB `1` is a short upright stroke; `6` may be a closed loop with a rising stroke.
- `σ`-shape (small open loop with a stroke up to the right, like Greek final sigma/6 leaning, often read "6" or "σ"):
  code `SG` when it is clearly not a normal digit 6; if you cannot tell, write `6` with conf M.
- plain letters as themselves: `X` `V` `Z` `T` `S` `E` (capital E), `K`, etc.
- `Xk` X with an extra horizontal bar or star-like crossing (✱, Ӿ).
- `Zb` Z with a crossbar (ƶ). A large Z/Ʒ-like capital with two or three bars (E-like with bars, ⵉ, Ẕ) = `ZZb`.
- `F` long s / f with crossbar (ƒ).
- `G1` Λ (capital tent, no base); `G7` λ (smaller lambda with a tail / the first stroke longer). If unsure which, G1 + M.
- `G2` Δ (closed triangle).  `G3` ϖ (w-like loop squiggle, "ϖ" / "ѡ").  `G4` π (bar with 2-3 legs).
- `G6` ε (small backward-c / epsilon; distinguish from 3).
- `THE` Θ-like circle with a cross or plus above it (⊕ with a stem, ♁).  `OQ` circle with a tail/loop (Q/Œ ligature-like).
- `BOX` a square □.  `RAD` radical-like √ tick (often before G3).  `Z3` a 3 / ʒ with a bar through it.
- Punctuation: a dot `.` -> sign `DOT`; a colon `:` -> `COL`; a closing flourish/paraph at line end is NOT a sign.

Stop when both letters are done. Report one line: rows written per letter and the NEW codes used.
