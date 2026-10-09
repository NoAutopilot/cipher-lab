You are adjudicating between two readings of hand-drawn cipher signs in a 16th-century manuscript. The task is
VALUE-BLIND: you match shapes to cells of a sign sheet; you do not know and must not try to find out what any sign means.

Look only at these images (open each with your image reader) and no other file:
- /home/user/cipher-lab/benchmark-tx/txeng/adjud/dev_tune/sheet_04.png
- /home/user/cipher-lab/benchmark-tx/txeng/adjud/dev_tune/sheet_05.png
- /home/user/cipher-lab/benchmark-tx/txeng/adjud/dev_tune/sheet_06.png
- /home/user/cipher-lab/benchmark-tx/txeng/adjud/dev_tune/sheet_07.png
- /home/user/cipher-lab/benchmark-tx/txeng/adjud/dev_tune/sheet_08.png
- the sign sheet, 51 cells labelled T10..T98: /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/sign_sheet_blind_1572.png

Each item on the sheets is a strip of one manuscript line, upscaled 2x. A dark-blue bracket above and below the strip marks
a stretch (usually one sign, sometimes two). Two earlier readers disagreed about that stretch. For each item, decide which
option matches the ink inside the bracket, by shape against the sheet cells (dots, ticks, bars, loops and lean matter; a
stretch may hold one sign or two, and "a mark matching no cell" means no sheet cell fits).

Items 19-36:
Item 19: option 1 = T42 | option 2 = a mark matching no cell
Item 20: option 1 = T42 | option 2 = a mark matching no cell
Item 21: option 1 = T92 | option 2 = T50
Item 22: option 1 = T18 | option 2 = T98
Item 23: option 1 = T51 | option 2 = T95
Item 24: option 1 = T98 | option 2 = T18
Item 25: option 1 = T29 | option 2 = T24 then T88 (two signs)
Item 26: option 1 = T18 | option 2 = T98
Item 27: option 1 = T46 | option 2 = a mark matching no cell
Item 28: option 1 = T18 | option 2 = T98
Item 29: option 1 = T50 | option 2 = T92
Item 30: option 1 = T98 | option 2 = T18
Item 31: option 1 = T46 | option 2 = a mark matching no cell
Item 32: option 1 = T95 | option 2 = T66
Item 33: option 1 = T88 | option 2 = T45
Item 34: option 1 = T86 | option 2 = T60
Item 35: option 1 = T96 then T95 (two signs) | option 2 = T95 then T96 (two signs)
Item 36: option 1 = T95 | option 2 = T66

Answer for every item with exactly one of: 1, 2, a different cell or cell sequence you see instead (e.g. T44, or T24 T88),
or ? if you cannot tell. Write one TSV file at the path the task gives you, with header

item	answer	conf	note

conf = H (clear), M (plausible), L (guess); note = a few words on the shape that decided it. No other output. Report in two
lines: how many items answered 1 / 2 / other / ?.
