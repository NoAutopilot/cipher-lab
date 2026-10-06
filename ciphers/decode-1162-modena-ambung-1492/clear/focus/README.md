# Clear-text focus sheet, decode-1162 (D1-DEC1162F, 6 Oct 2026)

`focus-sheet.html` (1.45 MB, self-contained, no runtime capability) shows the 22 rows of `../doubts_R10B.tsv` marked `stays`
(20), `read-doubtful` (1, 1.14 'grignol?') and `RAISED` (1, the month on p.2 l.6): per card the word crop (enlarged 2x,
autocontrast), its line with the word boxed in red, the text now, both blind readings, the crop note and the transcribed line.
The reader types a reading and a confidence per card; "Make the answer list" gives a TSV (`id reading confidence`) to paste back.
Answers are kept in the viewer's browser only (localStorage), so the TSV is the hand-back.

- `boxes.tsv`: id -> crop, row, word x-range in the native line-crop pixels of `../../images/clear/`, placed by eye on ruler
  views; row a = top 62% of the crop, b = bottom 62%, c = bottom half (address crop).
- `build_focus.py`: rebuilds `tiles/` and the page from the two TSVs; `check_contact.png`: 5 random tiles (seed 1162: F16 F02
  F01 F10 F03) boxed on their full line crops, each box on its word. All 22 word tiles were also viewed; F11, F13, F14 and F22
  were re-placed once after that view.

Not published. To publish: Artifact publish of `focus-sheet.html` (no capabilities needed). After the read: apply the answers
to `../clear_text.tsv` and `../doubts_R10B.tsv` (verdict `settled-person`), no cipher change.
