# Sign inventory for the blind cipher passes (N5-VIVK, 4 Oct 2026)

The Saint-Gouard 1572-74 cipher is written in signs that look like Latin cursive letters, digits and a few marks.
Transcribe each sign as the keyboard token it LOOKS LIKE, from this list. You are not deciphering: a sign that looks
like "m" is written m, whatever it means.

Plain lowercase letters, as they look: a b c d e g h i j k l m n o p r s t w x y z
  - m = three humps, n = two humps. Write "oo" as two signs: o o.
  - d = round body with an ascender curling back to the left (like the round Greek delta / ∂).
  - y = also the long swash y / ꝩ that starts with a lead-in stroke from the left.
  - p = p with a descender (may look like "ꝑ").
Special tokens (each is ONE sign):
  tz   t joined to a z-like descender (very common: "tzmp", "tz#")
  to   the joined "to" sign (t followed by a closed loop, e.g. at the start of "to2m")
  3    round-topped 3 with descender (write z only for a flat-topped z)
  #    the double-crossed sign like # / H / ‡
  :    two dots side by side on the line ("..")
  P    pi-like sign, two uprights with a top bar (like Roman II / π)
  S    long s ſ: tall stroke descending below the line, no crossbar
  f    f with a crossbar
  A    capital A
  @    a with a large curling loop or flourish on its left, like "(a" or ⓐ
  V    a long backslash / V stroke (often joined to the next sign, e.g. "\b", "\m")
  R    r-like sign with a loop, like R / Ꝛ / "rt"
  L    capital L or ℓ
  Z    capital Z, as it looks
  J    capital J, as it looks
  H    capital H with ONE crossbar, as it looks (write # for the double-crossed sign)
  2 4 6 7 8   digits as they look
  {word}  any other sign: 1-3 words of description in braces, e.g. {curl}, {cross}, {omega}
  ?    after a token you are unsure of (e.g. "z?"); [...] for a stretch you cannot read at all
Plain-language words written in ordinary script (e.g. "Il non", "Je baise ...") go as [PLAIN:words].
Word spacing is not significant; ignore it.

## Changelog (TXE2-VIV102-BASE, 9 Oct 2026, PREREG-txeng2-14 DV1b; committed before any read)
- Base: ../s2read/sheet_SIGNS.md (sha256 5e5090094fa51de7498885c647374f6192312b5d2ff931679f1db743533df41e), otherwise verbatim.
- Added as tokens the 6 committed labels that S2-NOTE (../s2note/RESULTS.md section 4) found missing from the S2 sheet
  (13 signs in the f.103r committed stream): t, i, w (to the plain lowercase list), Z, J, H (special tokens; H was named
  only as a look of #). Labels only, no values; no other line changed.
