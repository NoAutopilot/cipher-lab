# Pass brief: Dupuy 452 f.24 (Nicolas Raince to Monseigneur [Robertet], Rome, 24 Oct 1525)

Written 24 Sept 2026 by the f.24 transcription worker. One brief, given unchanged to two blind readers
(pass A and pass B). The letter uses the same cipher as the Raince-to-Madame letter (ff.28-29), whose
reconciled sign set has 50 types. Your codes must be those 50 codes, so that the two letters can be read
against one inventory.

## What you may open

- The crop images: `images/crops/f24r_L01_s1.jpg` ... `f24r_L21_s2.jpg` (42 files) and
  `images/crops/f24v_L01_s1.jpg` ... `f24v_L14_s2.jpg` (28 files), plus the gutter crops
  `images/gutter/f24v_L01_s3.jpg` ... `f24v_L09_s3.jpg` (9 files).
- The legend image `glyphs/contact_sheet.jpg` (one row per type, in the order of the table below; the
  row label is the code and its count on ff.28-29; left block = typical exemplars, right block = odd ones).
- This brief.

## What you must not open

`ciphertext.txt`, `ciphertext_*.txt`, `passA.tsv`, `passB.tsv`, any `pass*_f24.tsv` other than your own,
`reconciliation*.md`, `NOTES.md`, and everything under `glyphs/` except `contact_sheet.jpg`. Do not decode,
guess plaintext, or look anything up online.

## Crops

All paths are relative to `ciphers/dupuy452-carpi-1520/`.

- Each `_Lnn` crop is a **band of two physical lines** (line 1 = upper, line 2 = lower). `f24v_L14` holds one
  line. If a band shows three lines, or a line only partly, say so in the note and number the lines you see
  1, 2, 3 from the top.
- Each band is cut into **two overlapping segments**: `_s1` (left) and `_s2` (right). They overlap by about
  700 px, so the last 8-12 signs of `_s1` reappear at the start of `_s2`. **Read every sign in every crop
  file, including the overlap**, both lines. The duplicates are removed later by position; do not try to
  remove them yourself. (A previous reader read only line 1 of `_s1` and lost a fifth of a letter.)
- For f.24 verso, lines in bands L01-L09 run past the right edge of `_s2`. The `_s3` gutter crop shows the
  last ~850 px of the line, overlapping `_s2` by about 600 px. Read it the same way, both lines, every sign.
- A sign cut in half by the crop edge: record it as best you can and put `cut` in the note.

## Plain text and cipher

f.24 recto starts with about eight lines of plain French ("Monseigneur ..."), then cipher. f.24 verso starts
with cipher, then plain French paragraphs, the date and the signature. Some lines switch from plain to cipher
part-way.

- A plain line or plain stretch: one token `[PLAIN: "..."]` with your best reading of the French (mark
  doubtful words `(?)`). Do not spend long on the French; one pass is enough.
- A blank line or a line of pure margin marks: one token `[BLANK]` or `[MARGIN: "..."]`.
- Cipher: one token per sign, left to right.

## Codes (the 50 types, plus how to mark doubt and new shapes)

| code | shape | code | shape |
|---|---|---|---|
| psi | trident on a stem (ψ) | lamL | large lambda with a tail |
| l | cursive l-loop with crossed tail (figure-of-eight / ribbon) | m | m |
| v | v / check stroke | A | A |
| arr | arrowhead on a stem (upward wedge with a foot) | pi | ω with a bar above (ϖ) |
| lam | open caret Λ | yogh | tall 3 with a descender |
| f | long f with crossbar | L | script L loop |
| db | dagger (short cross high on a stem) standing on a small o | cross4 | cross with a loop at three ends |
| o | small plain o | K | K |
| I | I with serifs | zslash | z with a long diagonal (lightning) |
| rho | ρ: loop with a long tail curling left under the previous sign | x | single curly x (kappa-like) |
| q | ball on a plain straight stem (lollipop) | plus | plus sign |
| z | z | dash_o | short dash joined to an o (-o) |
| box | small rectangle with a dot inside | three | 3 (ordinary height) |
| T | T | U | U with a loop on each arm |
| X | double / starred X | Tbox | tall T over an o |
| n | n | oplus | circle with a cross inside |
| 7 | 7 | hash | triple bar crossed by a stem |
| E | E / ε | heart | heart |
| S | S | bz | b joined to z |
| ankh | ball on a stem with a crossbar (♀) | diamond | diamond with a dot |
| sq | a-like loop with a diagonal stroke | box3 | three small boxes in a row |
| th | θ, o with a horizontal bar | y | y |
| R | R | Del | closed triangle Δ |
| dbar | o under a long horizontal bar with a short stem | H | H (left stem sometimes faint) |
| w | ω / w | six | 6 (reversed 6 / G-like loop) |

**Pairs that readers merged last time; keep them apart:**
- `q` (ball on a plain stem, no tail) vs `rho` (loop whose tail curls left under the previous sign) vs
  `ankh` (ball on a stem with a crossbar).
- `psi` (three prongs) vs `arr` (solid arrowhead, no middle prong).
- `l` (loop ribbon) vs `lam` (bare caret) vs `lamL` (large caret with a tail).
- `db` (short cross high on the stem, o at the foot) vs `dbar` (long flat bar, short stem, o below).
- `box` (single dotted rectangle) vs `X` (double x); `w` vs `pi` (bar above); `three` vs `yogh` (descender);
  `th` (barred o) vs `o` vs `oplus` (cross inside).

**Doubt.** A sign you can place but are unsure of: the code with `?` appended (`q?`), and the runner-up in
the note (`or rho`). A sign you cannot place at all: `?`.

**New shapes.** A shape that is none of the 50: code `NEW1`, `NEW2`, ... in order of first appearance, with a
short description in the note on first use (e.g. `NEW1: circle with a dot, no box`). Never force a new shape
into an existing code; never invent a code for an allograph you are merely unsure about (use `?` instead).

## Output

One TSV, the same columns as the ff.28-29 passes, with header:

```
crop_file	line_no	token_no	token	note
```

- `crop_file` e.g. `f24r_L10_s1.jpg` (the gutter crops as `f24v_L03_s3.jpg`); `line_no` 1 or 2 within the
  band; `token_no` from 1 along that line within that crop file; `token` a code, `code?`, `?`, `NEWn`,
  or one bracketed PLAIN/BLANK/MARGIN token; `note` free text or empty.
- Every crop file must appear at least once, in the order listed above (f24r L01-L21 s1 then s2 per band,
  then f24v likewise, s3 after s2 for L01-L09).
- End the file with comment lines starting `#`: signs per crop file you are least sure of, and a list of the
  NEW codes with descriptions and where each first occurs.

Write your file (pass A: `passA_f24.tsv`; pass B: `passB_f24.tsv`) in `ciphers/dupuy452-carpi-1520/`. Do not
commit or push. Report in five lines: token count, cipher tokens per page, `?` count, NEW codes, anything
odd about the crops.
