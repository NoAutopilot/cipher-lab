READER PASS v2, f.260r (BnF fr.7129), D4-VILL2, 7 Oct 2026.
Images: ciphers/fr7129-villeroy-bongars-1604/sibling/f260r_crops/win/w<LL>_<kk>.jpg -- line LL cut left to right into 7
windows (kk = 01..07), each enlarged 2x. Each window shows, on top, a clerk's plaintext decipherment written letter by
letter (French, c.1604; sometimes a whole word over a number) and, below, the cipher signs. Windows overlap: the RED TICK
at the top-left of windows 02..07 marks where the previous window ended; signs whose left edge is left of the tick were
already written from the previous window -- skip them.
Job: open EVERY window (Read it as an image; never generate rows with a script). For each cipher sign left to right:
its id by SHAPE from the inventory below, and the clerk letter(s) whose ink stands DIRECTLY ABOVE that sign (look straight
up from the sign). Write '-' where nothing stands above it. Do NOT distribute the gloss evenly or proportionally: a row
whose gloss you did not see above that sign is wrong. If a gloss letter stands between two signs, give it to the one it
overlaps more and note 'between'.
Name each sign by its shape, never by the letter above it (shapes and values differ). Numbers: a digit run written together
is one token (26, 99); look at EVERY number for a bar over it and prefix ^ (^25). A stand-alone digit is its own token.
conf: H sure of shape and of the gloss position, M, L.
Output per line: sibling/passes_r2/R_L<LL>.tsv, header then rows; columns: line, win, pos, sign, gloss, conf, note
(pos = 1..n across the whole line). Final message only: lines done, signs per line, glossed signs per line.
Do not read any other repository file (no other pass, no key, no NOTES, no other R_/C_ files).
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
