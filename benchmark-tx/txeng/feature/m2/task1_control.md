# Feature read of hand-drawn signs (TXE-M2 call 1)

You describe the SHAPE of every mark on the images named below, one row per mark. You are not asked what the marks are or mean, and you get no list of sign names. Read ONLY the images named below; do not open any other file in this repository. Write only the TSV named below.

The image: /home/user/cipher-lab/benchmark-tx/txeng/feature/m2/control_tiles.png

It shows numbered tiles, each holding one printed sign (the number is written above the tile). Write one row per tile: `passage` = TILES, `pos` = the tile number.

Output: one TSV with this header and one row per sign:

    passage	pos	desc	asc	bars	loops	dots	lean	tail	conf	note

Each feature column holds exactly one value from its vocabulary:

    desc=none|short|long  asc=none|short|long  bars=0|1|2  loops=0|1|2  dots=0|1|2+  lean=left|upright|right  tail=none|left|right

- desc: ink below the main body of the sign, compared with the body's height (none: under a quarter; short: under three quarters; long: more).
- asc: ink above the main body, same scale.
- bars: long horizontal strokes running across most of the sign's width, 0, 1 or 2 (a flat loop top counts).
- loops: closed loops (enclosed holes), 0, 1 or 2.
- dots: separate small marks (dot, tick, accent) apart from the main stroke, 0, 1 or 2+.
- lean: the sign's main axis tilts left, stands upright, or tilts right.
- tail: the lowest part of the ink ends to the left or right of the sign's centre, or is centred (none).
- conf: H (features clear), M (one feature uncertain), L (hard to see).
- note: a few words on the shape (optional).

Look at the ink of each mark and write what you see. Do not name, classify or compare the marks with any sign list. When done, report in one short paragraph: rows per passage and how sure you were.

Write your TSV to: /home/user/cipher-lab/benchmark-tx/txeng/feature/reads/m2_features_control.tsv
