# f.130r blind pass instructions (A2-DIN2, 3 Oct 2026)

Leaf: BnF fr.3621 f.130r (Gallica btv1b52524472n canvas f269), Dinteville to Nevers, Langres, 3 July 1592.
French letter with inline cipher passages (NO decipherment on this leaf). Crops in ../images/f130_Lnn_sN.jpg, cut by
tools/iiif_lines.py following the line slope: each crop shows 2-3 rows; the line to transcribe is the one
running through the VERTICAL MIDDLE of the crop. Rows at the very top or bottom belong to neighbouring lines; ignore them.
Each line is cut into two segments: s1 = left (page x 0-1760 of the region), s2 = right (x 1600-3360). The last
~160 px of s1 reappear at the start of s2: transcribe each sign ONCE -- in s2, skip the signs already in the
right edge of s1 (write the overlap you skipped in the note column).

Lines and segments that carry cipher (anchor = how the middle row starts, so you can find it):
  L01 s2 only: the short cipher tail at the far right end of the line "...dy retourner et" (signs after "et"); may be
       partly cut at the crop top -- transcribe what is visible, mark ? for lost signs.
  L02 s1+s2: whole line cipher, ends in the clear words "vous suppliant"(?) (record clear words as CLEAR:...)
  L03 s1+s2: clear "aussi si vous plaist Monseigneur" then cipher, ends in clear "que la ... Lorraine"
  L04 s1+s2: clear "se fortifie ... de Strasbourg" then cipher to the end of the line
  L05 s1+s2: cipher from the start, then clear "Messieurs de la ville ..." -- stop at the clear words
  L06 s2 only: clear text, then cipher at the right end after "leur dy"(?)
  L07, L08, L09, L10 s1+s2: whole line cipher
  L11 s1+s2: cipher, ending in the clear words "pour luy"

Sign labels (use these exact labels; if a sign fits none, write NEW:<short description>; unreadable = ?):
  II   two vertical strokes (Roman two)          #    double-barred cross / hash
  1    single vertical stroke                    .    a raised or baseline dot written between signs (a separate sign)
  0    round zero / o, full size                 o    small round o (clearly smaller than 0)
  0'   zero with a stroke or accent over it      plus a + / cross written as a sign
  t    cross with a lower bar (like a dagger)    T    pi/tau shape (bar with two legs, like π)
  a    plain a shape                             al   alpha (α, open loop with a tail, distinct from a)
  c    c shape                                   3    figure 3
  zh   bare z-tail / ʒ (no m in front)           z    z shape (small)
  4    figure 4                                  D    triangle with a flag (Δ)
  9    figure 9                                  f    f / long s with a cross-bar (like ƒ, £, or ≠ written upright)
  p    p / rho with a loop                       y    psi/phi shape (Y with a cross stroke, ψ)
  w    w / omega shape (ϖ)                       m    m with a z-tail (ɱ / m3)
  v    v / downward triangle (∇)                 v'   v with an ascender/cross stroke above it
  sq   small square (□)                          L    inverted T (⊥)
  x    x shape                                   div  division sign (÷)
  r    r-like sign with a curl                   h    h-like sign with a hooked tail (ɧ)
  B    barred B-like sign                        n    n shape
Overbars or strokes that sit ON a sign as part of it: write them as a suffix ' (prime), e.g. 0' or v'.

Output: write ONE file, TSV, header exactly:
line	seg	order	signs	note
One row per crop segment you transcribe (L01 s2, L02 s1, L02 s2, ...), signs space-separated in order, left to right;
clear French words inside a cipher line go inline as CLEAR:<word> tokens. note: anything uncertain ("sign 7 could be 3 or zh").
Do not guess from language: record what the image shows.
