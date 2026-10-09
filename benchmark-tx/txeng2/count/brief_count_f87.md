# TXE2-COUNT step 1, leaf ceppo-f87 (fr.3251 f.87): COUNT the cipher signs per line (PREREG-txeng2-3 X12)

You are counting, not reading. Read ONLY the 18 crop files named in your task, `sign_sheet_blind.png` (the sign
vocabulary: 55 cells S10..S97, shape only) and this brief; open no other file.

The leaf is a 16th-century Italian letter; five cipher lines L01..L05. L01 begins with ordinary Italian prose (ending
"... per alcuni suoi particolari"); count only the cipher run after it. Each crop is one horizontal segment of one line,
upscaled 2x; the segments s1, s2, s3 (s4) of a line run left to right and do NOT overlap: add their counts.
Count cipher signs only, left to right. Small marks that look like punctuation are often cipher signs: "=", "+", a slash
between two dots, "3", "2", a crossed or barred stroke, a lone "o" all have cells on the sheet: take every mark in a
cipher run as a sign unless it is clearly a pen slip. A sign's dots, ticks or bars belong to it when its sheet cell has
them (a dot or tick on a sign is not a separate sign). Marks that match no cell (e.g. an oval crossed by two bars, a
pound-like loop) still count as one sign each. Writing that clips in from the line above or below is not counted.

Output: write ONE TSV file at the path your task names, header exactly:
line	count	doubtful	note
one row per line L01..L05: count = number of cipher signs on the line (all segments); doubtful = how many of them you
are unsure exist or are one sign vs two (0 if none); note = where (segment and rough position). Also add, after the five
line rows, rows `L0n_sK` with the per-segment count in `count` (doubtful/note may be blank). Do not name sign
identities, do not decode. Report the five counts in one short paragraph.
