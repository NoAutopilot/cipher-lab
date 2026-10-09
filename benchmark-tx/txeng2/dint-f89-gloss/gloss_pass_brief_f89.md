# Blind gloss read, BnF fr.3619 f.89 (TXP-D89, 9 Oct 2026)

A French letter of 1591 has lines of cipher signs; a period decipherer wrote the plain text in small, darker letters
just ABOVE each cipher line, roughly word over word. You read only that small interlinear writing. You open ONLY this
brief and the crop files named in your task; nothing else in the repository, no other file, no web.

The crops `f89g_L01.jpg` ... `f89g_L14.jpg` are each about 1290 px wide at the scan's resolution (small: you may make
enlarged copies in your own scratchpad, Python PIL 3x LANCZOS, halves). In each crop the small interlinear writing runs
through the upper-middle of the crop; below it lies the cipher line itself (odd signs and ordinary larger French words,
which are NOT the gloss: ignore them); fragments at the very top belong to the line above: ignore them. Over a stretch of
the line written in ordinary words there is usually no gloss. The gloss can be faint, cramped or partly struck through.

Transcribe the gloss letters exactly as written, period spelling (u/v, i/j, y as written; no accents added), words
separated by single spaces, left to right. Where a word is unreadable write ? for each unreadable letter group; where
the decipherer wrote a + or | (a sign left unexpanded) write + or |. Do not modernise, do not complete words from sense,
do not add words that are not written. Struck-through gloss: give it in [brackets].

Output TSV, header exactly
line	text	conf	note
one row per crop (line = L01 ... L14), conf H/M/L for the line as a whole, note for anything doubtful.
Write nothing but your output file.
