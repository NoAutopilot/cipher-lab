# Blind transcription pass brief (LANE R2 worker J1, 24 Sept 2026)

You transcribe the numeral cipher groups of Willem van Oranje / Jan van Nassau letters (1572-1575; French, or German
for 5549) from the page images. You are one of two independent passes: do not open any other pass file, any
align_*.tsv, key or reading; do not decode; do not use the network.

Images: ciphers/jan-van-nassau-1572-75/images/<briefnr>_p<N>.jpg (150 dpi). Zoom with
`python3 ciphers/jan-van-nassau-1572-75/crop.py IMG OUT.png --yfrac 0.40 0.52 --xfrac 0.05 0.95 --scale 1.6`
(OUT under /tmp/<yourname>/). Read digits only from zoomed crops (3-5 manuscript lines per crop), never from the
whole page.

Output: ciphers/jan-van-nassau-1572-75/passes/pass<A|B>_<briefnr>.tsv, header `line	pos	group	conf	note`, one row
per cipher group in reading order. `line` = `<briefnr>p<page>L<nn>` with nn the manuscript line on that page counting
every written line of the main text from the top (01, 02, ...; marginal notes are not lines); `pos` = 1-based position
of the row within that line; `group` = the number as written, digits only; a sign that is not a number (a letter,
a symbol such as a crossed h, '&', a superscript, a flourish between dots) is written as `s:<short description>`
(e.g. `s:a`, `s:h-crossed`, `s:o-superscript`); clear (non-cipher) words inside or between cipher runs go in ONE row
per stretch as `w:<the clear words, as read>` (it keeps the positions honest). `conf` = H sure, M one digit unsure,
L unreadable or guessed (use `?` for an unreadable digit, e.g. `3?`). Pages with no cipher at all: one row
`w:NO CIPHER` for the page.

Write the file incrementally: append each page's rows as soon as that page is done, so nothing is lost if you are
interrupted. Finish with a 4-line report: pages and lines done, groups transcribed, count of M/L rows, anything odd
(a second hand, interlinear decipherment, a key table, numbers above 100).
