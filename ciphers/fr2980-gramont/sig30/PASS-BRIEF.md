# Blind transcription pass, one manuscript line of a 1530 cipher letter (SIG-GRA30)

You transcribe invented cipher signs from images into codes. You do not decode; there is no plaintext to find, and you
must not try to read meaning into the signs.

Reference (Read both images first, and again whenever a sign is unclear):
- /home/user/cipher-lab/ciphers/fr2980-gramont/atlas/atlas_f29.png -- the shared atlas: each row = one code (left) with
  up to 3 exemplars from the same scribe's cipher.
- /home/user/cipher-lab/ciphers/fr2980-gramont/atlas/atlas_f30add.png -- extra codes (FL, HASH, BOX, ss2 arch, INF, TRI,
  QQ, ST, A2, CROSS, Rt).
Extra codes with no picture (use them when the shape fits):
- zb: a '2' with a bar through or under it (plain '2' has a tick above it instead).
- nq: a square-root-like N with a hook. n: a small r/2-shaped sign that often follows nq, or a free-standing n shape.
- nr: an r with a dot.  Sx: a crossed S (distinct from 5 and sl).  re: an r-hook joined to an e (distinct from eh).
- ehx: an open c-bowl with a crossed stroke above it (eh without the cross is eh).  ev: like oi but a v-ending.
- v: a plain v shape (distinct from yt's curled t).  lz: a small l joined to a z.  B8: a figure 8 with a cross stroke.

The line is cut into an 'a' (left) and 'b' (right) image that do not overlap. Neighbouring lines' ascenders and
descenders intrude at the top and bottom; transcribe only the signs on the line's own middle line. A sign cut by the
a/b boundary: write it in the half that holds most of it.

Rules:
1. Left to right, one code per sign, single spaces, ONLY codes from the atlas images or the extra list above. Codes are
   case-sensitive ('H' vs 'h', 'T' vs 'Tb', 'g' vs 'g2' vs '9' vs 'q').
2. A sign that matches no code: NEW:<3-6 word shape description>.
3. A sign you can see but doubt: your best code + '?', e.g. 'g?'.
4. A free-standing small dot between signs: '.'. Ignore flourishes/underlines that are parts of signs.
5. Two long strokes joined at the top like an arch is ss2; two SEPARATE long strokes side by side are 'sl sl'.
6. Some lines begin or end with ordinary clear handwriting (Latin-script words); skip those words.
7. Do not skip signs and do not guess from context: you are recording shapes only. Zoom by re-reading the image.
Output: RETURN (do not write any file) exactly two lines, nothing else:
<row>a<TAB>codes
<row>b<TAB>codes
