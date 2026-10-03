# Blind gloss-to-cipher transcription pass (A2-HAR6, 3 Oct 2026; f.90r run crops and reply-text output A2-HAR7, 3 Oct 2026)

Two Elizabethan manuscript pages (BL Harley 287 f.84r and f.90r, 1588). Each has lines of a symbol cipher, and above each cipher
run a contemporary decipherer wrote the plain English (the "gloss") letter by letter. On f.84r every line pair is gloss (upper,
small cursive) over cipher (lower, symbols). On f.90r the letter mixes ordinary clear English (not glossed, ignore it) with
cipher runs; the gloss sits just above each cipher run (sometimes in a margin-left position for a run at the start of a line).

Crops (read them in order, each band once): images/f84r/f84r_L01_s1.jpg, _s2.jpg ... L15 (s1 = left half, s2 = right half,
about 120 px overlap -- do not count overlapping signs twice). images/f90r_runs/f90r_R01_L01.jpg ... R18 (A2-HAR7: one crop per
glossed cipher run, gloss above, cipher below; R03, R06 and R18 have two segments _s1/_s2 with 120 px overlap). For f.90r the
band column is the run id (R01..R18) and pair is 1, unless one crop clearly holds two separately glossed runs. Ignore clear
English words at the crop edges (not glossed). R18's cipher row is cut at the bottom edge: read what is visible, ? the rest.

Write one TSV row per cipher run (a run = the cipher signs that one continuous gloss phrase sits over; on f.84r one row per
band, split into several rows only if a band clearly has separate glossed runs):

    page<TAB>band<TAB>pair<TAB>gloss<TAB>cipher

- page: f84r or f90r; band: L01..; pair: 1, 2, ... within the band (left to right).
- gloss: the gloss letters exactly as written, spelling kept (e.g. "the answers brought us by norice after three"), words
  separated by single spaces; lowercase; write an unreadable gloss letter as ?. If a run has no gloss write -.
- cipher: one token per cipher SIGN, tokens separated by single spaces, and " / " between cipher words (where the scribe
  leaves a gap). Use this sign code (D. Bourdeau's ASCII code for this cipher):
    U  cup / u-shape                 A  caret ∧ (inverted v)           +  plus / cross
    8  figure 8                       D  ∞ (lying 8, infinity)          T  t with a bar / ŧ
    7  figure 7                       H  H with a bar                   G  Ӿ (x with a bar)
    h  stem with a bowl               I  ⊥ (inverted T)                 k  ω (omega)
    l  circle on a stem ϕ             m  ∽ (lying s)                    #  double cross ǂǂ / #
    z  2-shape / z                    d  d-shape                         c  c-shape (open left-facing curve)
    p  loop with a tail ϑ / þ-like    V  v / r-shape                    y  γ (gamma)
    :  two dots (on their own, or ".." over/before a sign: write it as its own token :)
    w  dot + stroke                   X  plain x                        Q  reversed c ɔ
    L  L-shape                        K  K-shape                        -  a short dash / horizontal stroke used as a sign
    ?  any sign you cannot identify (never guess a code you are unsure of)
  A sign not in this list: write ? and describe it in the notes column.
- Optional 6th column notes (free text, e.g. "sign 5 unclear between z and c").

Do NOT use any outside knowledge of this cipher or any key; read only what is on the crops. Do not look at any other file in the
repository. Return the TSV (with a header row page, band, pair, gloss, cipher, notes) as the text of your final reply, inside one
```tsv fenced block, and write NO file (A2-HAR7: auto mode refused A2-HAR6's passes at the file write; the worker writes it).
