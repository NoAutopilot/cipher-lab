# MAT-F91B blind transcription pass

You are transcribing a 1586 French cipher (BnF fr.15572, Mayenne to Henri III) from line images. Signs are letter-like
figures, digits and a few special marks. Use the SAME label set as the reference chart.

REFERENCE: REF_IMG shows three lines of the same cipher system (a different leaf, f.78v), each given as its left half above its right half (thin grey rule between halves; the halves may overlap by a few signs), lines separated by thick
black rules. Their labels, sign by sign, left to right:
L1: me w- U d 7 L m h 14 E t f T h d q f q oo t 14 2 7 c e U d B h L U 7 T s R d E o H .v. q
L2: h L D2 oo t w- h y X z d U T n o w- q e d o L q B h w- h u BOX2 o E L h c e X H t D 13 A y h
L3: Ze o h B t .v. m 13 d 7 .v. E o D2 d Ze U n o q o E 6 m lam D2 d o h t f q s oo H .v. m U E
Label notes: `.v.` = v between two dots; `D2` = triangle; `BOX2` = small square; `oo` = infinity-like loop; `Ze` = Z-like
sign; `w-` = barred w; `4+` = crossed 4 (plain `4` if not crossed); `ff` = double-f form; `T` vs `t`; `he`; `lam` = lambda;
`U` = the x/cross-like sign; `th`, `yy`, `fh`, `dd` = ligature forms; digits as digits; a multi-digit number is ONE token
(e.g. `13`, `14`, `24`, `26`, `104`). If a sign matches no label, write `?{short description}` (e.g. `?hooked-s`).
Never guess from context: do not try to read French or "decode" anything.

TARGET: for each line image, transcribe ONLY the line in the vertical middle (neighbour lines may be clipped at top or
bottom: ignore them). Ignore ordinary cursive handwriting (clear French words, e.g. at the start or end of a line, or
bits of margin text at the far left edge): transcribe only cipher signs. Note in the uncertain column if the line
begins or ends with clear words.

OUTPUT: write a TSV to OUT_PATH with header `line\ttokens\tuncertain\tnote` and one row per line (line id = the image
file stem, e.g. `A1`): space-separated tokens, comma-separated 1-based positions you are unsure of, and a short note.
Append after each line so partial work survives. Reply with just the file path and the number of lines written.
Work only with the image files named here; do not open any other file in the repository.
