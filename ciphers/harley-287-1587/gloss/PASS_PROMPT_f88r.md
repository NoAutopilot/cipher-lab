# Blind sign-by-sign transcription pass, f.88r (A4-RFHAR, 5 Oct 2026)

One Elizabethan manuscript page (BL Harley 287 f.88r, 1588), a letter in ordinary English handwriting with runs of a
symbol cipher mixed into the lines. There is no interlinear decipherment. Your job: copy every cipher run sign by sign.

Crops (read them in order, each band once): images/f88r/f88r_L01_s1.jpg, f88r_L01_s2.jpg ... f88r_L23_s2.jpg
(23 lines; s1 = left part, s2 = right part of the same line, about 120 px overlap -- do not count overlapping signs
twice). Lines slope slightly; the crop is centred on its own line, ignore fragments of the lines above and below.

Write one TSV row per cipher run (a run = consecutive cipher words between pieces of clear English):

    band<TAB>pair<TAB>before<TAB>cipher<TAB>after<TAB>notes

- band: L01..L23; pair: 1, 2, ... left to right within the band.
- before / after: the one or two clear English words immediately before / after the run, as you read them (- if none
  on this line). Number words or numerals written in plain digits are clear text, not cipher.
- cipher: one token per cipher SIGN, separated by single spaces, and " / " between cipher words (where the scribe
  leaves a gap). Sign code:
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
  A sign not in this list: write ? and describe it in notes. A struck-through run: copy it and write "struck" in notes.
- notes: optional free text.

Do NOT use any outside knowledge of this cipher or any key; read only what is on the crops. Do not open any other file.
Return the TSV (header row band, pair, before, cipher, after, notes) as the text of your final reply inside one ```tsv
fenced block, and write NO file.
