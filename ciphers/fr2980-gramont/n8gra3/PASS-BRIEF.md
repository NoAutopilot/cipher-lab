# Blind transcription pass, BnF fr.3040 no.6 f.18v / f.19r (cipher, 1530) -- N8-GRA3

You transcribe invented cipher signs from images into codes. You do not decode; there is no plaintext to find, and you
must not try to read meaning into the signs.

Reference (Read these two images first, and again whenever a sign is unclear):
- /home/user/cipher-lab/ciphers/fr2980-gramont/atlas/atlas_f29.png -- the shared atlas: each row = one code (left) with
  up to 3 exemplars from the same scribe's cipher.
- /home/user/cipher-lab/ciphers/fr2980-gramont/atlas/atlas_f30add.png -- extra codes (FL, HASH, BOX, ss2 arch, INF, TRI,
  QQ, ST, A2, CROSS, Rt).
Rows: each manuscript line is cut into an '_a' (left) and '_b' (right) image that do not overlap; the files are
/home/user/cipher-lab/ciphers/fr2980-gramont/images/fr3040_f18/<row>.jpg. Neighbouring lines' ascenders and descenders
intrude at the top and bottom; transcribe only the signs on the row's own middle line. A sign cut by the a/b boundary:
write it in the half that holds most of it.

Rules:
1. Left to right, one code per sign, single spaces, ONLY codes from the two atlas images. Codes are case-sensitive
   ('H' vs 'h', 'T' vs 'Tb', 'g' vs 'g2' vs '9' vs 'q').
2. A sign that matches no atlas code: NEW:<3-6 word shape description>.
3. A sign you can see but doubt: your best code + '?', e.g. 'g?'.
4. The long oblique separator stroke between groups: write '/'. A free-standing dot: '.'.
5. Two long strokes joined at the top like an arch is ss2; two SEPARATE long strokes side by side are 'sl sl'.
6. Some rows begin with ordinary clear handwriting (French words in Latin script); skip those words entirely and start
   at the first cipher sign.
7. Do not skip signs and do not guess from context: you are recording shapes only.
Output: RETURN (do not write any file) a TSV block with header 'row<TAB>codes' and one line per row id, in the order
given, nothing else after it.
