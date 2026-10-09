# Gloss read, fr.3619 f.98v (TXP-D98 step 4, 9 Oct 2026)

You read a period hand's interlinear decipherment: small French words written ABOVE six cipher lines of a 1591 letter
(BnF fr.3619 f.98v). Each crop shows one gloss row (the cipher row below it has been masked out; stray strokes may remain).
Crops: G01..G06 (gloss above cipher lines L01..L06), each in two segments s1 (left) and s2 (right) at 2x; segments overlap
by 200 px in the image (about 8 letters): read the overlapping ink once.

Transcribe the letters as written, left to right, words separated by single spaces, keeping the period spelling (u/v, i/j as
written, no accents added). Expand nothing: write abbreviations as written, letters only. Where the decipherer wrote "+" or
"|" (a sign he left unexpanded) write that character. Where a word is unreadable write "?" for it, and "?" for single
unreadable letters inside a word. A word struck through: write it inside square brackets [like this]. G01 sits only over
the right part of its line; some rows may start with a word in a larger text hand at the far left: transcribe it too and
mark it with a leading "*" (e.g. *word).

Output: one TSV at the path in your task, header exactly
line	text	conf
one row per gloss row (line = G01..G06), conf H/M/L for the row as a whole. Do not guess at meaning beyond the ink, do not
consult anything else. Report only the six rows' word counts.
