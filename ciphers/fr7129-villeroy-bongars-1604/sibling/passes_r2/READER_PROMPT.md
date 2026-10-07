READER PASS, f.260r (BnF fr.7129), D4-VILL2, 7 Oct 2026.
Each crop (ciphers/fr7129-villeroy-bongars-1604/sibling/f260r_crops/p260_L<NN>_s<1|2>.jpg) shows TWO rows: on top, a
clerk's plaintext decipherment written letter by letter (French, c.1604; it sometimes writes a whole word above a number);
below it, the cipher row. s1 is the left part of the line, s2 the right part; they overlap by about 120 px (about 3-5
signs), so do not write the overlapping signs twice: in s2, start with the first sign that lies to the right of the
last sign you wrote from s1 (compare the shapes at the seam).
Job: for every cipher sign, left to right, write the sign id (from the inventory below) and the clerk's letters written
directly above that sign. You SHOULD use the gloss to keep your place, but name each cipher sign by its own SHAPE, never by
the letter above it (the cipher signs often look like ordinary letters and their values differ from their shapes).
Numbers: a run of digits written together is one token, written as is (26, 99, 155). Look at EVERY number for a
horizontal bar over it and prefix ^ when there is one (^25). A stand-alone single digit is its own token.
Gloss column: the clerk letters above that sign, exactly (keep & and abbreviations), '-' when nothing is above it. Every
gloss letter of the row must land on exactly one sign; joined left to right, the gloss column must give back the
whole gloss row. If a gloss word sits above a group of signs, give it to the first sign of the group and '-' to the rest,
and write 'grp' in the note.
Confidence: H (sure of the shape), M, L. Write '?' as id for a sign you cannot match.
Output: one TSV file per line, path given below, columns: line, seg (s1/s2), pos (1..n across the whole line),
sign, gloss, conf, note. First a header row. Then, in your final message, only: lines done, sign count per line, and
any crop you could not read.
Do not look at any other file in the repository (no other pass, no key, no NOTES). Read only the crops named.
SIGN INVENTORY (choose ids only from this list; the pictures ref_f228.jpg and ref_f275_A/B.jpg show the period sign forms)
Numbers: write multi-digit numbers exactly as written, e.g. 26, 99, 155. A number with a horizontal bar over it: prefix ^ (e.g. ^25).
A single stand-alone digit is also a sign: 3 (flat 3), 4, 6, 7, 8, 9 -- write the digit.
Letter-like signs (id = description):
 y = y-shaped sign            x = x              Zt = tailed 3 / yogh-like sign
 Hr = large open hook enclosing an r            Hu = large open hook enclosing n/u
 Hun = large open hook enclosing minims          HZ = Z with a large hook
 Ch = large C-hook standing alone                Cx = circle with a cross on top
 pH = p with a hook       ab = small cross / crossed stroke     u, v
 ls = long s (tall s)     r = r rotunda (2-shaped r)            q, o, s, p, i, k, e, c, a, b, m, t, f
 g = 9-shaped g           x4 = crossed 4                        ss = double long s
 qo = q+o ligature        fh = f with ligature stroke           un = four minims (mm/un)
 mt = m with a tail       cc = two c's                          do = d with hook
 ff = double f            xff = crossed ff / pi-like ligature   d = round (uncial) d
 Z = Z-shaped sign        od = circle with a dot inside         tt, co, ba, dd, oo, ri, sin, bb, ut, ur, w
Marks: a letter sign with a dot or two dots (umlaut) over it: append '.' (e.g. a.). A letter sign with a bar over it: append '~'.
Anything that matches nothing above: ? . Keep digits apart from letter signs.
