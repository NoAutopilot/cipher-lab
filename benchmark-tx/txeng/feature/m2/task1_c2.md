# Feature read of hand-drawn signs (TXE-M2 call 1)

You describe the SHAPE of every mark on the images named below, one row per mark. You are not asked what the marks are or mean, and you get no list of sign names. Read ONLY the images named below; do not open any other file in this repository. Write only the TSV named below.

The images are horizontal segments of manuscript lines (a 16th-century cipher page; every mark is a cipher sign, upscaled 2x). Segments s1, s2, s3 of a line run left to right and overlap by about 100 px at the 2x scale (50 px native), so a sign that appears at the right edge of s1 and again at the left edge of s2 is ONE sign -- count it once, and continue the count across the segments. Small marks that look like punctuation ("=", "+", a slash between two dots, "3", "2", a crossed or barred stroke, a lone "o") are signs too; take every mark as a sign unless it is clearly a pen slip. A sign's own dots or ticks belong to it.

`passage` = the line id (L01, L02 ... from the file name), `pos` = 1-based position in the line, left to right.

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

The images (18, s1 s2 s3 of each line in order):
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

Write your TSV to: /home/user/cipher-lab/benchmark-tx/txeng/feature/reads/m2_features_c2.tsv
