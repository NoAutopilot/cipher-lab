# Samples for the owner to look at. Nothing here is sent; any outward use passes outreach gate 7.

Rendered 9 Oct 2026 (MQS-SHEETS-R, account 4) by `tools/decipher_sheet.py` from each folder's own graded data; regenerate
all with `sh outreach/sheets/render_all.sh` (`--check` exits 1 for a stale sheet, rule 7). Layout after Lasry, Biermann and
Tomokiyo 2023, Figs 5-14 (pp.112-127); no figure reproduced. Glyph tiles are cut from the manuscript images already on disk,
never from anyone's drawn table. Open an .html in a browser; each is self-contained. K3 = the tile check pre-registered in
`tools/tests/PREREG-MQS-SHEETS.md` G4 (programmatic: non-empty crop and ink share in [0.02, 0.65] on every tile; eye: one grid
of at most 60 tiles beside the line label or the code's exemplar; a sheet with more than 10% unusable or misplaced in either
count is "not fit to show"). The commit is the one that adds this file; each sheet's footer carries its own render commit.

| file | target, unit | depth wording (rule 4a) | key source | K3 programmatic | K3 eye | status |
|---|---|---|---|---|---|---|
| gramont-key.html | BnF fr.2980, Gramont key | n/a (key sheet) | published (Tomokiyo, Lasry) | 0 tiles | n/a | codes only, no glyph tiles: the full-resolution f.29r region is not on disk (Gallica answers 403 to cloud sessions) and the committed 1400 px double-page image is too small to cut glyphs |
| gramont-f29r-reading.html | fr.2980 f.29r, Gramont to Villandry, 20 May 1530 | partially deciphered (about 94%) | published | 0 tiles | n/a | value row without tiles; H 532, S 1, M 30, U 5 |
| danzay-f35-key.html | BnF fr.20140, Danzay key | n/a | published (Tomokiyo's 2026 reconstruction) | 0 tiles | n/a | codes only: Danzay has no sign boxes or atlas, so no exemplar crops |
| danzay-f35-reading.html | fr.20140 f.35r-v, Danzay to the Cardinal of Lorraine, 27 Jan 1557 | partially deciphered (about 77%) (status.json counts f.35-36; the sheet shows f.35 only, 638 tokens: H 509, M 59, U 70) | published | 37 line crops: blank 0, ink out of range 0 | 37 of 37 line crops carry their own label (0 misplaced, 0 unusable); checked by the clear words in 33 lines, by order alone in V1, V19, V26, V28 | line-crop mode, "token row not aligned to the image"; f.36 (4 lines) not rendered: its line crops are not committed |
| eckert-e4-key.html | Huntington mssEC 19 p.49, E4, the code words it uses | n/a | period (Cipher No. 1, mssEC 41) | 0 tiles | n/a | 10 distinct code words, each with its mssEC 41 page and line |
| eckert-e4-reading.html | mssEC 19 p.49, E4, Fox to Butler, 21 Apr 1864 | deciphered (N4: no prior decipherment located; 11 code-word tokens, all H) | period | 8 line crops: blank 0, ink out of range 1 (L8, ink share 0.011 against the 0.02 floor: faint pencil) | 8 of 8 crops carry their own line (0 misplaced; L8 legible) | **not fit to show** by the pre-registered rule (1 of 8 = 12.5% over 10% on the programmatic count); the eye count is 0 of 8, so the failure is the ink floor on a faint pencil line, not a misplaced or unreadable crop. The floor was not adjusted afterwards; the owner decides whether to look at it. Not offered outward |

## Held (Birago 1572 family): rendered in the scratchpad only, never written here

Held: open owner sort in this key family (ASKS row 118 and the 2 Oct / 3 Oct Birago sorter rows); regenerate with the commands
below once those rows are done and no Birago family sorter is open. Counts only:
- **no.87 reading, f.178v (box mode)**: `python3 tools/decipher_sheet.py reading ciphers/nevers-birago-fr3251-1572 --job f178v --out <dir>/no87-f178v-reading.html --tile-report <dir>/f178v.tsv`. 659 tiles: blank 0, ink out of range 0, label/value disagreements 9 (the exceptions.tsv corrections; reported, not failures). Eye, 60 tiles sampled at seed 9 beside the key-sheet exemplar of the same code: about 11 of 60 (18%, my count, plus or minus 1) differ in shape from that exemplar (partial glyphs, neighbouring signs, or a label that disagrees with the picture), over the 10% line: **not fit to show**. This agrees in direction with A1's KM (held-out agreement 0.606 against a permuted-box p95 of 0.085): the box placement is far above chance and far from perfect.
- **no.87 reading, f.178r (line-crop mode)**: `... --job f178r --out <dir>/no87-f178r-reading.html`. 0 tiles: no line-image table exists for f.178r, so the sheet shows the value row with the "not aligned" notice and no crops. K3 not applicable.
- **Birago key sheet**: `... key ciphers/nevers-birago-fr3251-1572 --job f178v --variants 3 --out <dir>/birago-key.html --tile-report <dir>/birago-key.tsv`. 113 exemplar tiles: blank 0, ink out of range 0. The eye check above is its check (tiles against its exemplars).

## Notes for whoever uses these
- `tools/decipher_sheet.py` needs opencv-python-headless (and scikit-image, scikit-learn for box mode); none was installed in the cloud container, `pip install` fixed it.
- The Eckert sheets embed crops of Huntington page images under the Huntington's rights statement (`ciphers/eckert-1864/images/README.md`, "Rights"); the footer says so.
- Danzay's crops are cut at the boxes in `danzay-f35-lines.tsv` from the committed `f69_cipher.jpg` and `f70_cipher_top/bot.jpg`; Eckert's from `eckert-e4-lines.tsv` (bands read by eye from a preview). `eckert_e4_inputs.py` re-derives the token and key TSVs from `ciphers/eckert-1864` (decode.py's own grades).
