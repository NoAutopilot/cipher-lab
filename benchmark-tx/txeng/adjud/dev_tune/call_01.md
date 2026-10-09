You are adjudicating between two readings of hand-drawn cipher signs in a 16th-century manuscript. The task is
VALUE-BLIND: you match shapes to cells of a sign sheet; you do not know and must not try to find out what any sign means.

Look only at these images (open each with your image reader) and no other file:
- /home/user/cipher-lab/benchmark-tx/txeng/adjud/dev_tune/sheet_01.png
- /home/user/cipher-lab/benchmark-tx/txeng/adjud/dev_tune/sheet_02.png
- /home/user/cipher-lab/benchmark-tx/txeng/adjud/dev_tune/sheet_03.png
- /home/user/cipher-lab/benchmark-tx/txeng/adjud/dev_tune/sheet_04.png
- the sign sheet, 51 cells labelled T10..T98: /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/sign_sheet_blind_1572.png

Each item on the sheets is a strip of one manuscript line, upscaled 2x. A dark-blue bracket above and below the strip marks
a stretch (usually one sign, sometimes two). Two earlier readers disagreed about that stretch. For each item, decide which
option matches the ink inside the bracket, by shape against the sheet cells (dots, ticks, bars, loops and lean matter; a
stretch may hold one sign or two, and "a mark matching no cell" means no sheet cell fits).

Items 1-18:
Item 1: option 1 = T95 | option 2 = T51
Item 2: option 1 = T51 | option 2 = T95
Item 3: option 1 = T60 | option 2 = T86
Item 4: option 1 = T50 | option 2 = T92
Item 5: option 1 = T81 | option 2 = T83
Item 6: option 1 = T92 | option 2 = T50
Item 7: option 1 = T11 | option 2 = a mark matching no cell then a mark matching no cell (two signs)
Item 8: option 1 = T92 | option 2 = T50
Item 9: option 1 = a mark matching no cell | option 2 = T42
Item 10: option 1 = T13 | option 2 = T64
Item 11: option 1 = T86 | option 2 = T60
Item 12: option 1 = T50 | option 2 = T92
Item 13: option 1 = T29 | option 2 = T24 then T88 (two signs)
Item 14: option 1 = T46 | option 2 = a mark matching no cell
Item 15: option 1 = T29 | option 2 = T24 then T88 (two signs)
Item 16: option 1 = T18 | option 2 = T98
Item 17: option 1 = T18 | option 2 = T98
Item 18: option 1 = T92 | option 2 = T50

Answer for every item with exactly one of: 1, 2, a different cell or cell sequence you see instead (e.g. T44, or T24 T88),
or ? if you cannot tell. Write one TSV file at the path the task gives you, with header

item	answer	conf	note

conf = H (clear), M (plausible), L (guess); note = a few words on the shape that decided it. No other output. Report in two
lines: how many items answered 1 / 2 / other / ?.
