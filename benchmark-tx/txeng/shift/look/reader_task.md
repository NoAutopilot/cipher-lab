# Third look at doubtful signs, fr.3251 cipher lines (TXE-N, 9 Oct 2026)

You compare hand-drawn cipher signs with the cells of a sign sheet by SHAPE ONLY. The task is value-blind: you do not
know, and must not look up, what any sign means. Open ONLY the files named here: the sheet, the table file, and the
16 row images it lists. Open no other file in this repository.

The sheet: /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/sign_sheet_blind_1572.png (51 cells T10..T98).
The table: /home/user/cipher-lab/benchmark-tx/txeng/shift/look/sheet_01.md

Each row image shows the same short stretch of one manuscript line twice, cut from two differently placed crops
(view a above, view b below), magnified 4x. A red caret marks the estimated position of the doubtful sign; the estimate
can be off by about one sign, so use the table's neighbours: the doubtful sign lies between the sign matching the
"left neighbour" cell and the sign matching the "right neighbour" cell ("line start"/"line end" when at an end).
Two earlier readers disagreed there; their readings are option 1 and option 2 (a cell id, or "no sign here", meaning
one reader saw no separate sign between the neighbours). Small marks above or below a sign may belong to it when the
sheet cell has them; a stray dot may be a pen mark rather than a sign.

For each row decide: option 1, option 2, a different cell (give its T## id) if neither fits, or ? if you cannot tell.

Write exactly one TSV file at /home/user/cipher-lab/benchmark-tx/txeng/shift/look/answers_01.tsv with header

    row	pick	conf	note

pick = 1, 2, a cell id T##, or ?; conf = H, M or L; note = a few words on the shape that decided it.
Report in two lines: how many rows you answered 1 / 2 / other cell / ?. Do not decode or describe the letter's content.
