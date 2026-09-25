# Transcription pass summary — ANTT PT/TT/MSLIV/0638 cipher appendix (m0280–m0296)

Date of pass: 25 Sept 2026. Read directly from the 17 leaf images listed in the brief, in leaf order,
at 3–9x zoomed crops (see method note below). Literal transcription only — no decoding, no key-building.

## Totals

- **Entries transcribed: 39**, covering all 17 leaves (m0280–m0296).
  - 15 leaves carry a new "Carta Nº"/"Passage" heading (m0280–m0294); m0295 and m0296 carry **no new
    heading** — both are pure continuation of Carta 123's plaintext (see "Spanning entries" below), so
    they contribute 0 new rows of their own to the two TSVs, by design, not by omission.
- **Total cipher tokens: 1702**
  - Numeric (`num`): 1364
  - Letter-code (`ltr`): 338
- **Uncertain tokens flagged with `±`: 18** (listed below), plus a handful of uncertain plain words in
  `deciffrada_line` also marked `±` (abbreviations/proper names that were hard to read with confidence,
  e.g. "Buzquingoan±", "exSort.±", "patranha±", "bornex±").

## Entries that could not be read at all

**None.** Every entry on every leaf yielded a transcription. A number of individual tokens/words within
otherwise-readable entries are uncertain and flagged; see below.

## Spanning entries (one logical entry, cipher/plaintext split across a page turn)

The appendix regularly runs a cipher block or its "Deciffrada" plaintext across a leaf boundary. Per the
brief's row structure (one `leaf` per entry), each such entry is filed under the leaf where its heading
("Carta Nº n" / "Passage nª") first appears, and the `cipher_line`/`deciffrada_line` text is the full,
merged text including the part physically on the next leaf(s):

- **Carta 61** — filed under `m0282`; cipher line's last ~13 tokens are physically on `m0283`.
- **Carta 70** — filed under `m0283`; deciphered text's last clause ("...nas mãos da Rainha V.Sa") is
  physically on `m0284`.
- **Carta 123** — filed under `m0294`. This entry has **no cipher block at all** — the appendix goes
  straight from the "Carta Nº 123" heading to "Deciffrada" and quotes plaintext only. That plaintext runs
  continuously through the rest of `m0294`, all of `m0295`, and the first third of `m0296` (ending "...7 de
  9bro de 1713", with the Torre do Tombo archive stamp below it — the last content on the last leaf).
  `cipher_line` for this row is therefore an empty string; `token_type` counts include 0 tokens for it.

## Method note (glyph disambiguation)

The cipher mixes plain Portuguese words with two kinds of code symbol: Arabic numerals (mostly 2 digits,
occasionally 3, e.g. "300") and single roman code-letters (a b c d e f g h m q x y z). Two pairs of symbols
are easy to confuse at low resolution and were disambiguated by re-zooming to 6–9x on representative
instances each time they recurred:
- numeral **7** (written with a horizontal top stroke, diagonal, and a small mid-stroke crossbar) vs.
  letter **z** (a plain flowing diagonal/zigzag, no crossbar);
- a small "4" (open loop) vs. the ordinary digits;
- a large, ornamental looped capital form used for some code-letters (read as **y** at word-final position,
  where it matches the plain cursive "y" elsewhere in the same hand, but flagged `±` at a few other
  positions where it could not be pinned to a single letter of the given alphabet with confidence).

A few tokens fell outside the letter set given in the brief (a,b,c,d,e,f,g,h,m,q,x,y,z) on my best reading —
e.g. what reads as "p" in Carta 74/92 — these are kept as transcribed and flagged `±` rather than forced
into the nearest listed letter.

## Full list of `±`-flagged cipher tokens

| leaf | entry | token |
|---|---|---|
| m0280 | Carta 13 | 9± (×2) |
| m0281 | Carta 15 | g±, z±, g±, b±, 4± |
| m0283 | Carta 70 | b±, 310±, 400± |
| m0285 | Carta 72 | 12± |
| m0286 | Carta 74 | 4± |
| m0289 | Carta 89 | 38±, 58± |
| m0289 | Carta 92 | y± (×2), 56± |
| m0294 | Passage 2a | 107± |

(`p±` in Carta 74/92, though outside the given letter list, was not separately re-flagged with `±` in the
token text since it is already an unusual reading — see method note.)

## Files written

- `ciphertext_appendix.tsv` — 1702 token rows (leaf, entry_label, position, token, token_type).
- `plaintext_appendix.tsv` — 39 entry rows (leaf, entry_label, cipher_line, deciffrada_line).
