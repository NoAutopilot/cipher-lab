# Blind pass brief: NA 1.05.03 inv. 86 scan 0003 (GAPS14, 2 Oct 2026)

You are one of two independent blind readers. Do not look at any other file in this folder except the crops named.
Crops (read every one, Read tool, nothing else):
- Left page (5 bands top to bottom): images/crops_inv86_0003/v86L_L01.jpg .. v86L_L05.jpg
- Right page column (3 bands top to bottom): images/crops_inv86_0003/v86R_L01.jpg .. v86R_L03.jpg

The left page is an 18th-century Dutch cipher-key page: a 3-line heading, then a column of rows "LETTER. sign. sign. ..."
(A to Z), and beside the upper rows a second column of SYMBOL + WORD pairs (a code list). The right page is a single
column of rows "signs ... LETTER".

Write a TSV to the path you are given, with header `block	row	field	reading	confidence` where
- block = `head` (heading lines, row 1-3, field `text`, reading = the words as written, keep spelling),
  `alpha` (left alphabet; row = plain letter as written; one TSV line per cipher sign, field = sign position 1,2,3..,
  reading = a short shape description: for ordinary letters/digits write the character exactly as it looks
  (case matters: script capital vs lowercase), for others a bracketed name e.g. [delta], [psi], [lambda], [hash],
  [pi], [omega-bar], [amp-like], or describe briefly),
  `code` (code list; row = 1..n top to bottom; two lines per row: field `symbol` (describe the symbol precisely) and
  field `word` (the word(s), keep spelling)),
  `rev` (right page; row = the plain letter at the right; one line per sign as for alpha).
- confidence = high / medium / low.
Read each sign; do not normalise to what a key "should" be; if a sign is unclear, give your best reading with low.
Return only a 5-line summary: counts per block and the lines you were least sure of.
