# Blind transcription pass, fr.3252 f.47r cipher block, all 17 lines (NEVBIR-47, 2 Oct 2026; from harvest/blind_pass_brief.md)

You are one of two independent readers of the cipher signs on crops of a 16th-century Italian letter (BnF fr.3252 f.47r).
The pass is VALUE-BLIND: you match each hand-drawn sign to a cell of the sign sheet by shape only. You do not know, and
must not look up, what any sign means.

Read ONLY: the 51 crops `/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/images/f47/recut/f47r_L01_s1.jpg` ...
`f47r_L17_s3.jpg` (lines L01-L17, segments s1-s3), the sheet
`/home/user/cipher-lab/ciphers/ceppo-nevers-fr3251-1570s/harvest/sign_sheet_blind.png` (cells S10..S97), and three
reference tiles `/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f47/ref/ref_W1.jpg`, `ref_W2.jpg`, `ref_W3.jpg`
(same cipher, another letter; IGNORE the small letters written above the signs in those tiles). Open no other file in
the repository (no NOTES.md, no key, no map, no other pass); the pass is void if you do.

## Extra cells (forms not on the sheet, drawn from the reference tiles)

- `X_DSLASH`: a DIAGONAL slash (lower-left to upper-right) with one dot on each side (ref_W1, the right-hand sign).
  The sheet's S30/S49/S73 are HORIZONTAL or vertical bars with dots; use X_DSLASH for the diagonal form.
- `S97`: a lambda with a curled top and NO dot (ref_W1, the left-hand sign).
- `X_DCARET`: a caret / lambda / A-form with a DOT between or under its legs (ref_W2, ref_W3, the sign right of the "C").
  A lambda without a dot is S97; with a dot inside/under it is X_DCARET.
- `X_TRI`: a plain closed triangle (Δ) with no crossbar or tail (the sheet's S16/S42 have extra strokes).
- `X_DOTS`: a group of dots alone (two or three dots, no stroke); note how many.
- `X_THETA2` oval/circle crossed by TWO parallel horizontal bars; `X_POUND` a £/lb-like loop with crossing stroke;
  `X_NEW` anything else (describe it); `?` illegible.

## What to transcribe

- Segments s1, s2, s3 of a line run left to right and OVERLAP by a few signs: at the start of s2 and s3, skip the signs
  you already counted at the end of the previous segment (match them by shape). Continue the count across segments.
- Cipher signs only, left to right. Skip ordinary Italian prose words (the first lines and the last line mix prose and
  cipher). Small marks are often cipher signs ("=", "+", a slash with dots, "3", a barred stroke, a lone "o"): take every
  mark in a cipher run as a sign unless clearly a pen slip. A sign's dots or ticks belong to it when the cell has them;
  compare carefully: several cells differ only by a dot, a tick, one bar vs two, or the direction of a stroke.

## Output

Write exactly one TSV at the path your task names, header `passage	pos	sign_id	alt	conf	note`, one row per sign:
`passage` = line id L01..L17 (prose splitting a line into two cipher runs: L03.1, L03.2 ...); `pos` 1-based within the
passage; `sign_id` a cell id or X_ id or `?`; `alt` a second candidate or blank; `conf` H/M/L; `note` a few words on the
shape; on the first row of each passage quote the prose word just before the run (or "line start"), on the last row the
prose word just after (or "line end").

Work line by line and append to the file as you go (so partial work survives). When done, report in one short
paragraph: signs per line, count of X_ and ? rows, hardest cells to tell apart. Do not decode or describe content.
