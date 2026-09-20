# Lodovico Birago to the Duke of Nevers (13 November 1571)

- **Source:** BnF fr.3251, f.119. Letter in Italian. One paragraph is in a numerical cipher that the keys reconstructed for Birago's other 1570-1572 letters do not solve. Image: https://gallica.bnf.fr/ark:/12148/btv1b9060248g/f120.item
- **Status:** Open.
- **Transcription:** `ciphertext.txt` (Tomokiyo's). Note his warning: the diacritics (÷ ¯ ¨ + and letters n, f, c, m, a, l) should be placed over the following one or two characters. Check the Gallica image before trusting any parse.
- **Background page:** `sources/cryptiana/web/nevers.htm` (section BnFfr3251).
- **Ideas:** Digits run continuously without separators, so the first problem is tokenisation. Try two-digit groups, then variable-length. The diacritics probably modify the following digit pair (syllable vs. letter, or a vowel change). Plaintext is Italian.
- **Solver status (19 Sept 2026):** Closed-negative by Bourdeau (cyphersolver/birago), 16 Sept 2026, after glyph-level re-transcription from Gallica (the "+" signs are superscript crosses). Variable-length designs excluded against controls; the only consistent design is beyond the annealer at this length. Needs a sibling letter or a crib.
