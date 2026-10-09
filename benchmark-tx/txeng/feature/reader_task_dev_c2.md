# Blind transcription pass, fr.3251 cipher lines (LIKELY-3, 2 Oct 2026)

You are one of two independent readers of the cipher signs on crops of a 16th-century Italian letter (Lodovico
Birago to the Duke of Nevers, BnF fr.3251). The pass is VALUE-BLIND: you match each hand-drawn sign to a cell of
`sign_sheet_blind_1572.png` by shape only. You do not know, and must not look up, what any sign means.

Read ONLY these files: the crops named in your task, and `sign_sheet_blind_1572.png` (51 cells labelled T10..T98).
Do not open any other file in this repository (no NOTES.md, no key files, no `sign_id_map_1572.json`, no other pass
file); the pass is void if you do.

## What to transcribe

- Each crop is one horizontal segment of one manuscript line (f.178v, a page that is cipher throughout), upscaled 2x; segments s1, s2, s3 of a line overlap by about 100 px at the 2x scale (50 px native), so a sign that appears at the right edge of s1 and again at the left edge of s2 is ONE sign -- count it once. Segments s1, s2, s3 of a line run left to right; continue the sign count across them, counting an overlap-duplicated sign once.
- Transcribe cipher signs only, left to right. This page carries no prose: every mark is a cipher sign. Small marks that look like punctuation are often cipher signs: "=", "+", a slash between two dots,
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
- `sign_id`: the best-matching cell (`T##`), or `X_K` / `X_A` / `X_EQ` / `X_S` / `X_NEW` / `?`.
- `alt`: a second candidate cell if two fit, else blank.
- `conf`: H (clear match), M (plausible, one look-alike), L (guess).
- `note`: a few words on the shape; on the first row of each passage also quote the prose word just before the
  run (or "line start") and, on the last row, the prose word just after it (or "line end"), so the passages can
  be aligned.

No other output file. When done, report in a short paragraph: sign count per passage, how many X_ and ? rows,
which cells you found hardest to tell apart. Do not decode, do not guess at meanings, do not describe the
letter's content.

## Features first, then the cell

For every sign, look at the ink FIRST and write its features in a `features` column, BEFORE you choose the cell. Then choose the cell whose features (table below, measured by script on the printed sheet) match what you wrote; where two cells share the features, decide by the rest of the shape. If the ink clearly disagrees with every cell's features, say so in the note. The output header becomes:

    passage	pos	features	sign_id	alt	conf	note

Write `features` exactly as seven key=value pairs separated by spaces, in this order and vocabulary:

    desc=none|short|long asc=none|short|long bars=0|1|2 loops=0|1|2 dots=0|1|2+ lean=left|upright|right tail=none|left|right

- desc / asc: ink below / above the main body of the sign, compared with the body's height (none: under a quarter; short: under three quarters; long: more).
- bars: long horizontal strokes running across most of the sign's width (a flat loop top counts).
- loops: closed loops (enclosed holes).
- dots: separate small marks (dot, tick, accent) apart from the main stroke.
- lean: the sign's main axis tilts left, stands upright, or tilts right.
- tail: the lowest part of the ink ends to the left or right of the sign's centre, or is centred (none).

Cell features (from the printed sheet):

| cell | desc | asc | bars | loops | dots | lean | tail |
|---|---|---|---|---|---|---|---|
| T10 | none | none | 0 | 2 | 0 | left | right |
| T11 | none | short | 0 | 2 | 0 | upright | none |
| T13 | short | long | 1 | 0 | 0 | right | none |
| T15 | long | long | 0 | 0 | 1 | left | none |
| T17 | none | none | 2 | 0 | 0 | left | right |
| T18 | long | none | 2 | 2 | 0 | upright | none |
| T19 | none | none | 1 | 0 | 0 | upright | left |
| T24 | none | short | 1 | 0 | 0 | left | none |
| T25 | short | long | 0 | 0 | 0 | left | none |
| T26 | long | none | 0 | 1 | 0 | left | none |
| T27 | long | none | 2 | 1 | 0 | upright | none |
| T29 | short | none | 1 | 1 | 0 | right | none |
| T33 | short | long | 1 | 0 | 0 | left | none |
| T36 | long | none | 2 | 1 | 0 | upright | none |
| T37 | short | long | 1 | 2 | 0 | upright | none |
| T38 | none | none | 0 | 1 | 0 | upright | none |
| T42 | long | none | 1 | 0 | 0 | right | none |
| T45 | none | long | 1 | 1 | 0 | upright | none |
| T46 | none | short | 0 | 2 | 0 | right | none |
| T49 | long | none | 2 | 1 | 0 | upright | none |
| T50 | none | long | 0 | 0 | 0 | right | left |
| T51 | short | none | 1 | 0 | 0 | upright | none |
| T52 | short | none | 0 | 0 | 0 | left | right |
| T53 | none | none | 2 | 2 | 0 | upright | none |
| T54 | none | none | 1 | 1 | 0 | upright | none |
| T55 | short | short | 2 | 0 | 0 | upright | left |
| T56 | long | long | 1 | 0 | 0 | upright | none |
| T57 | long | short | 0 | 1 | 0 | upright | none |
| T58 | none | none | 2 | 2 | 0 | upright | none |
| T60 | short | short | 2 | 1 | 0 | upright | none |
| T63 | short | none | 0 | 0 | 0 | upright | none |
| T64 | short | none | 1 | 0 | 0 | left | right |
| T65 | long | none | 1 | 2 | 0 | upright | none |
| T66 | none | none | 1 | 1 | 0 | left | right |
| T70 | none | none | 1 | 1 | 0 | upright | none |
| T76 | none | none | 2 | 1 | 0 | right | left |
| T78 | none | none | 1 | 0 | 0 | right | left |
| T80 | none | none | 1 | 1 | 0 | upright | none |
| T81 | none | none | 0 | 0 | 0 | left | none |
| T83 | none | none | 1 | 1 | 0 | left | none |
| T84 | short | long | 2 | 1 | 0 | upright | none |
| T85 | long | long | 1 | 0 | 0 | upright | none |
| T86 | long | long | 1 | 0 | 0 | upright | none |
| T88 | none | none | 2 | 1 | 0 | right | none |
| T89 | none | none | 1 | 2 | 0 | left | right |
| T90 | none | long | 2 | 1 | 0 | upright | none |
| T92 | none | none | 1 | 0 | 0 | right | none |
| T95 | long | none | 2 | 1 | 0 | right | none |
| T96 | none | short | 1 | 1 | 0 | right | none |
| T97 | none | long | 2 | 2 | 0 | upright | none |
| T98 | long | short | 2 | 1 | 0 | upright | none |

## Your task

The sheet: /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/sign_sheet_blind_1572.png

The crops (18 images, 2x, s1 s2 s3 of each line in order; the passage id is the L number in the file name):
/home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178v/f178v_L07_s1.jpg
/home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178v/f178v_L07_s2.jpg
/home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178v/f178v_L07_s3.jpg
/home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178v/f178v_L08_s1.jpg
/home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178v/f178v_L08_s2.jpg
/home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178v/f178v_L08_s3.jpg
/home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178v/f178v_L09_s1.jpg
/home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178v/f178v_L09_s2.jpg
/home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178v/f178v_L09_s3.jpg
/home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178v/f178v_L10_s1.jpg
/home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178v/f178v_L10_s2.jpg
/home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178v/f178v_L10_s3.jpg
/home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178v/f178v_L11_s1.jpg
/home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178v/f178v_L11_s2.jpg
/home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178v/f178v_L11_s3.jpg
/home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178v/f178v_L12_s1.jpg
/home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178v/f178v_L12_s2.jpg
/home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178v/f178v_L12_s3.jpg

Write your TSV to: /home/user/cipher-lab/benchmark-tx/txeng/feature/reads/passU_raw_dev_c2.tsv
