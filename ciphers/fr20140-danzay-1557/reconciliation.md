# Reconciliation of passA / passB for f.35 (24 Sept 2026, solver session)

**How it was settled.** The two passes cannot be compared sign by sign. Most of their tokens are
`unkN`/`unk-<shape>` labels that each pass made up on its own (NOTES.md "Passes"), so a sign-level match rate
would mean nothing. So the final transcription (`ciphertext.txt`) is a third reading, done directly from the
images: `images/native_f70.jpg`, cut into one strip per line at native resolution (line centres found by a
dark-pixel row profile, 29 lines, spacing about 145 px), and `images/f69_cipher.jpg` for the recto. Each glyph
was named against Tomokiyo's legend (`sources/cryptiana/web/danzay_1557.png`). A glyph that matches no legend
cell got its own code, described in `inventory.tsv`. Signs whose identity is doubtful are marked `M`.
The passes served as a check on line numbering and token counts per line, and on the clear-hand words.

**Line alignment.** Pass A's line numbering (R1-R8, V1-V29) matches the final line for line. Its token count
per line is within 3 of the final on 33 of 37 lines. Pass B covers R1-V16 only and records roughly half as many
tokens on cipher lines, because it groups strokes. Its V17-V29 are missing.

**Settled from the image, by type:**
- Every seam between the two half-line strips was checked for duplicated signs (the strips overlap by 150 px).
  Duplicates were dropped, e.g. V1 `pd eq`, V2 `ae`, V5 `pp x`, V19 `x H`.
- Pass A's "Dannemarch" label (21 uses) covers several different glyphs. The script-L glyph is coded `LRD`
  (Tomokiyo's "le Roy de Dannemarch"). The loop-in-circle glyph is coded `circ` (unkeyed).
- The barred figure-8 (`x8`, 16 uses) and the ringed T/7 (`ringT`, `ring7`) are not in Tomokiyo's table. They
  are kept as their own codes rather than forced into a legend cell.
- One interlinear gloss in cipher signs sits above V18 (`x8 O T mu lam pd r2`). Neither pass recorded it. It is
  transcribed as line V18g.
- The clear-hand words (V13-V16, V21-V22 and the runs inside cipher lines) agree between the passes apart from
  spelling. The final keeps one spelling per word, read from the image.

## Per-line table

A_words / B_words = how many of the pass's `word:` labels also appear as clear words in the final.

| line | passA tok | passB tok | final tok | final cipher | final clear | A words in final | B words in final |
|---|---|---|---|---|---|---|---|
| R1 | 5 | 6 | 6 | 6 | 0 | - | - |
| R2 | 26 | 20 | 26 | 25 | 1 | 1/1 | 1/1 |
| R3 | 29 | 15 | 16 | 5 | 11 | 6/6 | 6/10 |
| R4 | 24 | 17 | 24 | 22 | 2 | 2/2 | 1/1 |
| R5 | 22 | 15 | 19 | 15 | 4 | 1/2 | 0/3 |
| R6 | 23 | 14 | 23 | 21 | 2 | 2/2 | 1/1 |
| R7 | 23 | 12 | 22 | 21 | 1 | 0/1 | 1/1 |
| R8 | 24 | 13 | 22 | 19 | 3 | 2/2 | 1/1 |
| V1 | 25 | 14 | 24 | 24 | 0 | - | - |
| V2 | 26 | 16 | 26 | 25 | 1 | 1/1 | 1/1 |
| V3 | 28 | 12 | 26 | 24 | 2 | 1/1 | 1/1 |
| V4 | 21 | 12 | 21 | 17 | 4 | 1/3 | 3/3 |
| V5 | 25 | 13 | 26 | 24 | 2 | 2/2 | 1/1 |
| V6 | 22 | 12 | 23 | 22 | 1 | 0/1 | 0/1 |
| V7 | 18 | 12 | 18 | 11 | 7 | 3/7 | 5/7 |
| V8 | 20 | 12 | 21 | 16 | 5 | 2/4 | 4/4 |
| V9 | 21 | 10 | 22 | 20 | 2 | 2/2 | 1/2 |
| V10 | 23 | 12 | 24 | 20 | 4 | 3/4 | 2/4 |
| V11 | 20 | 13 | 19 | 15 | 4 | 0/3 | 1/3 |
| V12 | 28 | 10 | 27 | 24 | 3 | 0/3 | 1/1 |
| V13 | 12 | 12 | 12 | 0 | 12 | 4/12 | 9/12 |
| V14 | 11 | 11 | 11 | 0 | 11 | 2/11 | 8/11 |
| V15 | 12 | 11 | 11 | 0 | 11 | 4/12 | 9/11 |
| V16 | 13 | 13 | 12 | 0 | 12 | 8/13 | 9/13 |
| V17 | 26 | - | 27 | 24 | 3 | 3/3 | - |
| V18 | 25 | - | 26 | 24 | 2 | 2/2 | - |
| V18g | - | - | 7 | 7 | 0 | - | - |
| V19 | 26 | - | 27 | 27 | 0 | - | - |
| V20 | 21 | - | 21 | 17 | 4 | 0/4 | - |
| V21 | 9 | - | 10 | 0 | 10 | 1/9 | - |
| V22 | 15 | - | 14 | 0 | 14 | 9/15 | - |
| V23 | 25 | - | 26 | 24 | 2 | 0/3 | - |
| V24 | 19 | - | 19 | 12 | 7 | 2/7 | - |
| V25 | 22 | - | 22 | 19 | 3 | 2/3 | - |
| V26 | 27 | - | 28 | 28 | 0 | 0/1 | - |
| V27 | 25 | - | 26 | 25 | 1 | - | - |
| V28 | 26 | - | 27 | 27 | 0 | - | - |
| V29 | 29 | - | 29 | 28 | 1 | - | - |

The low figures in the word columns (e.g. V13-V15 pass A) are spelling differences, such as "comodement" for
"commodement", not disagreements about the text.

**Limit.** This is one careful reading, not a pair of agreeing independent readings. The `M` rows (61) and
the unkeyed codes are where a second reader working from the same strips should look first.
