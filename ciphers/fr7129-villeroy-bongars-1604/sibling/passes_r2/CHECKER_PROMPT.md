CHECKER PASS, f.260r (BnF fr.7129), D4-VILL2, 7 Oct 2026.
A reader has transcribed each crop (ciphers/fr7129-villeroy-bongars-1604/sibling/f260r_crops/win/w<LL>_<kk>.jpg, line LL in 7 windows enlarged 2x, red tick = where the previous window ended;
top row = a clerk's letter-by-letter plaintext decipherment, below it = the cipher row; windows overlap
) into sibling/passes_r2/R_L<NN>.tsv: per cipher sign, the sign id by SHAPE (inventory below) and the
clerk letters written directly above that sign. Your job is to check it against the crop, row by row, left to right.
For each row decide: ok (sign id and gloss both right), fix (you change the sign id and/or the gloss), del (the row is
not a cipher sign, or duplicates a sign across a window seam), unsure (you cannot tell; keep the reader's values).
Add a row with verdict ins where the reader skipped a sign (give it a pos like 12.5 to place it).
Check above all: the overbar on every number (^ prefix); runs of digits split or joined wrongly; the 9-shaped g vs a
stand-alone 9; y vs other forms; f, u, the d family (d, do, Zt, ls); ff vs xff; and whether each gloss letter sits above
the sign it is given to. Name signs by their own shape, never by the letter above them. Open every window as an image; never generate rows by script; never spread gloss proportionally -- the gloss of a row is the ink straight above that sign.
Output: one TSV per line, path given below, columns: line, win, pos, sign, gloss, conf, note, chk  -- i.e. the reader's
rows with your corrected values in place and the verdict in chk (every reader row appears once, plus your ins rows).
In your final message only: lines done, and per line the counts of ok/fix/del/ins/unsure.
Do not look at any other repository file (no key, no NOTES, no other pass) besides the crops and the R_L files named.
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
