# Sign tags for key no.60 passes (LANE R5 F2, 24 Sept 2026) -- shared by fr3986 f.198 and fr3987 f.66

Both leaves are copies in clear French cursive with runs of cipher no.60 (Tomokiyo's numbering; table BnF fr.3995
ff.109-111, transcribed by Daniel Bourdeau, `nevers1593/key60.txt`). A pass writes one line per crop line:

    <line id> TAB <tokens separated by single spaces>

line id = crop prefix without the segment, e.g. `f66_L07` (read `_s1` then `_s2`, s2 overlaps s1 by ~150 px:
do not write the overlap twice). Tokens:

- A run of clear French: one token `w:` + the legible words joined by `_` (e.g. `w:donne`, `w:la_nouvelle`); an
  unread clear run is `w:...`. Clear text is context only; do not spend effort on it.
- Cipher signs, one token each, left to right, using these tags:
  - figures: write the number as written; digits written close together as one group are ONE token (`10`, `42`,
    `20`); a lone digit is its own token (`4`, `7`, `9`, `3`, `2`, `1`, `6`, `8`).
  - crosses: `+` single cross; `++` one upright with two crossbars; `#` two uprights with two crossbars (renamed `dbl` at reconciliation, since a leading '#' reads as a comment in key.tsv);
    a letter or digit carrying a cross joined to it: base then `+`, e.g. `2+ 4+ 8+ a+ g+ d+ u+ q+`.
  - Latin letter shapes as seen: `a b c d e f g h i l m n o p q r s t u v x y z` and capitals
    `A B C E F G H I L M N O P Q R S T V X Z`.
  - special shapes: `pi` (π, two legs and a bar), `lam` (λ), `del` (∂, round d whose stem curls back left),
    `alpha` (∝, open fish/loop 'co'), `inT` (⊥, inverted T), `pl` (p whose descender carries a loop or cross-stroke,
    ꝑ), `ls` (long s ſ, tall descender), `oo` (∞ or two joined o's), `tri` (Δ triangle), `phi` (φ circle with a
    stroke through), `theta` (θ crossed o), `//`, `///`, `=`, `~`.
  - a mark above a sign (dot, stroke, apostrophe) : append `'` to the tag (`o'`, `8'`).
- Uncertain sign: append `?` (`g?`). Illegible sign: `?`.
Do not guess plaintext; do not normalise to what a key would like. Transcribe what the ink shows.
