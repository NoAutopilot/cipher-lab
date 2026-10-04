# Blind cipher-only transcription pass, gloss masked (RUN1-HAR, 4 Oct 2026)

One Elizabethan manuscript page (BL Harley 287 f.84r, 1588) written in a symbol cipher. You see only the cipher lines;
everything above and below each line has been painted white. Read each crop in order, each line once:
images/f84r_masked/f84rM_L01_s1.jpg, f84rM_L01_s2.jpg, ... f84rM_L15_s2.jpg (s1 = left half, s2 = right half of the same
line, with about 120 px overlap: do not count the overlapping signs twice). L10_s2 is blank. Strips are sheared to follow
the line's slope; sign strokes that run above or below the kept band may be clipped -- read what is visible.

Write one TSV row per line: page<TAB>band<TAB>cipher<TAB>notes
- page f84r; band L01..L15.
- cipher: one token per cipher SIGN, separated by single spaces, and " / " between cipher words (where the scribe leaves a
  gap). Use this sign code (D. Bourdeau's ASCII code for this cipher):
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
- notes: free text (optional).

Do NOT use any outside knowledge of this cipher or any key; read only the crops; open no other file. Return the TSV (header
row page, band, cipher, notes) as the text of your final reply inside one ```tsv fenced block, and write NO file.
