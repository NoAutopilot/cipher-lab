# Blind transcription pass, fr.3251 cipher lines (LIKELY-3, 2 Oct 2026; TX-SHEET variant 4 Oct 2026: the per-hand exemplar sheet replaces the 51-cell sheet, nothing else changed)

You are one of two independent readers of the cipher signs on crops of a 16th-century Italian letter (Lodovico
Birago to the Duke of Nevers, BnF fr.3251). The pass is VALUE-BLIND: you match each hand-drawn sign to a row of
the four sheet images `sheet_01.png` .. `sheet_04.png` by shape only. You do not know, and must not look up, what any sign means.

Read ONLY these files: the crops named in your task, and the four sheet images `sheet_01.png` .. `sheet_04.png` (51 rows
labelled T10..T98). Each row shows the sign's printed form (left of the grey divider) and then, for 33 of the signs, up to
six examples of the same sign as written by THIS hand on other letters, chosen to show its range of shapes (cramped,
wide, line-end and variant forms; some tiles show neighbouring ink at their edges -- the sign is the one in the centre).
A row with no examples has the printed form only. Match each mark to the row whose examples (or printed form) it fits best.
Do not open any other file in this repository (no NOTES.md, no key files, no `sign_id_map_1572.json`, no `sheet.tsv`, no other pass
file); the pass is void if you do.

## What to transcribe

- Each crop is one horizontal segment of one manuscript line (f.178v, a page that is cipher throughout), upscaled 2x; segments s1, s2, s3 of a line overlap by about 100 px at the 2x scale (50 px native), so a sign that appears at the right edge of s1 and again at the left edge of s2 is ONE sign -- count it once. Segments s1, s2, s3 of a line run left to right; continue the sign count across them, counting an overlap-duplicated sign once.
- Transcribe cipher signs only, left to right. This page carries no prose: every mark is a cipher sign. Small marks that look like punctuation are often cipher signs: "=", "+", a slash between two dots,
  "3", "2", a crossed or barred stroke, a lone "o" all have rows on the sheet. Take every mark in a cipher run
  as a sign unless it is clearly a pen slip.
- A sign's dots or ticks belong to it when the sheet row has them (compare carefully: several rows differ only
  by a dot, a tick, one bar vs two, or lean).
- A sign that matches NO row: give sign_id `X_K` for a Latin capital K, `X_A` for a capital A, `X_EQ` for two short
  parallel horizontal strokes (=), `X_S` for a plain long-s / s shape, `X_NEW` for anything else, and describe the shape
  in the note. Use `?` when you cannot make out the mark at all.

## Output

Write exactly one TSV file at the path your task names, with this header and one row per sign:

    passage	pos	sign_id	alt	conf	note

- `passage`: the line id (`L01`, `L02` ...). If prose separates two cipher runs on one line, number the runs
  `L03.1`, `L03.2` ... in order.
- `pos`: 1-based position within the passage.
- `sign_id`: the best-matching row (`T##`), or `X_K` / `X_A` / `X_EQ` / `X_S` / `X_NEW` / `?`.
- `alt`: a second candidate row if two fit, else blank.
- `conf`: H (clear match), M (plausible, one look-alike), L (guess).
- `note`: a few words on the shape; on the first row of each passage also quote the prose word just before the
  run (or "line start") and, on the last row, the prose word just after it (or "line end"), so the passages can
  be aligned.

No other output file. When done, report in a short paragraph: sign count per passage, how many X_ and ? rows,
which rows you found hardest to tell apart. Do not decode, do not guess at meanings, do not describe the
letter's content.
