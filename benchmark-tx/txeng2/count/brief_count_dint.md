# TXE2-COUNT step 1, leaf dint-f128 (fr.3621 f.128r): COUNT the cipher signs per line (PREREG-txeng2-3 X12)

You are counting, not reading. Read ONLY the 8 crop files named in your task and this brief; open no other file.

The leaf is a French letter with an inline cipher passage. A period hand wrote a decipherment (gloss) in small letters
ABOVE each cipher line; ignore the gloss entirely. Clear French words are also written inside the cipher lines ("et",
"Il ha laisse", the opening words of L02, the closing word at the end of L05): do NOT count clear words or their letters.

Crops: each line is cut in two OVERLAPPING segments, s1 = left, s2 = right, with about 150 px of overlap: the last signs
of s1 reappear at the start of s2. Count each sign ONCE (find the overlap by matching the shapes at s1's right end and
s2's left end). In each crop the cipher line is the middle row; the writing at the very bottom belongs to the NEXT line.
  L02: only the right part of L02 is cipher (after the clear word "et").
  L03, L04, L05: whole line cipher (L05 ends in a clear word, not counted).

What counts as one sign (the sign vocabulary of this hand): II (two vertical strokes, ONE sign), 1 (single stroke),
0, o (small o), 0' (zero with stroke/accent over it), #, ., +, t (dagger-like cross), T (pi/tau), a, c, 3, z, Z, 4, 9,
f, p, y, w, m (m with z-tail, ONE sign), v, sq (small square), L (inverted T), x, -:- (division sign, ONE sign).
A raised or baseline dot written between signs is a SEPARATE sign. Overbars or dots sitting ON a sign are part of it.

Output: write ONE TSV file at the path your task names, header exactly:
line	count	doubtful	note
one row per line L02..L05: count = number of cipher signs on that line; doubtful = how many of them you are unsure
exist or are one sign vs two (0 if none); note = where the doubt is (e.g. "near the end of s1: a dot or a blot").
Do not name sign identities beyond what the note needs; do not decode. Report the four counts in one short paragraph.
