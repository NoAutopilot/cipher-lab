# Blind transcription pass with alternatives, fr.3251 cipher lines (TX-ALTS, 4 Oct 2026; from LIKELY-3's brief + the a/b? rule)

You are one of two independent readers of the cipher signs on crops of a 16th-century Italian letter (Lodovico
Birago to the Duke of Nevers, BnF fr.3251). The pass is VALUE-BLIND: you match each hand-drawn sign to a cell of
`sign_sheet_blind_1572.png` by shape only. You do not know, and must not look up, what any sign means.

Read ONLY these files: the crops named in your task, and `sign_sheet_blind_1572.png` (51 cells labelled T10..T98).
Do not open any other file in this repository (no NOTES.md, no key files, no `sign_id_map_1572.json`, no other pass
file); the pass is void if you do.

## What to transcribe

- Each crop is one horizontal segment of one manuscript line (f.178r or f.179r; the crop is the cipher run of the line), upscaled 2x; segments s1, s2, s3 of a line overlap by about 100 px at the 2x scale (50 px native), so a sign that appears at the right edge of s1 and again at the left edge of s2 is ONE sign -- count it once. Segments s1, s2, s3 of a line run left to right; continue the sign count across them, counting an overlap-duplicated sign once.
- Transcribe cipher signs only, left to right. If a crop shows clear prose words, skip them; inside the cipher run every mark is a cipher sign. Small marks that look like punctuation are often cipher signs: "=", "+", a slash between two dots,
  "3", "2", a crossed or barred stroke, a lone "o" all have cells on the sheet. Take every mark in a cipher run
  as a sign unless it is clearly a pen slip.
- A sign's dots or ticks belong to it when the sheet cell has them (compare carefully: several cells differ only
  by a dot, a tick, one bar vs two, or lean).
- A sign that matches NO cell: give sign_id `X_K` for a Latin capital K, `X_A` for a capital A, `X_EQ` for two short
  parallel horizontal strokes (=), `X_S` for a plain long-s / s shape, `X_NEW` for anything else, and describe the shape
  in the note. Use `?` when you cannot make out the mark at all.

## Output

Write exactly one TSV file at the path your task names, with this header and one row per sign:

    passage	pos	sign_id	alt	conf	note

- `passage`: the line id (`L01`, `L02` ...). If prose separates two cipher runs on one line, number the runs
  `L03.1`, `L03.2` ... in order.
- `pos`: 1-based position within the passage.
- `sign_id`: the best-matching cell (`T##`), or `X_K` / `X_A` / `X_EQ` / `X_S` / `X_NEW` / `?`. **Alternatives rule
  (DECRYPT convention, Megyesi 2020):** whenever you hesitate at all between cells, write every cell you hesitated
  between, best first, separated by `/` and ending in `?` -- e.g. `T18/T98?` or `T45/T89/T86?` (at most three). Never
  write a single guess for a sign you are unsure of: a sign you would mark M or L must carry at least two cells. A
  sign you are sure of is written alone (`T33`). Every sign is transcribed somehow; none is left out.
- `alt`: leave blank (alternatives go in `sign_id` as above).
- `conf`: H (clear match), M (plausible, one look-alike), L (guess).
- `note`: a few words on the shape; on the first row of each passage also quote the prose word just before the
  run (or "line start") and, on the last row, the prose word just after it (or "line end"), so the passages can
  be aligned.

No other output file. When done, report in a short paragraph: sign count per passage, how many X_ and ? rows,
which cells you found hardest to tell apart. Do not decode, do not guess at meanings, do not describe the
letter's content.
