# R4376 (BL Add MS 32276 f.56, docket 1754) P3, tested on R1049 (N6-HEL76, account 2, 4 Oct 2026)

Source: DECODE R4376 (https://de-crypt.org/decrypt-web/RecordsView/4376). P1 = docket "1754"; P2 = blank ruled form; P3 = filled French
table, codes 1-500 in five blocks of 100, plus a strip of right entries LEFT of block 1-100 and a cut 501-600 column at the right page
edge. No holder named. The image is not committed (not public domain); `../images/decode/manifest.json` has its URL and sha1
(84ef4ad7..., matched on refetch).

- `PREREG.md`: pushed (a6f0668b) before the image was fetched.
- `key.tsv`: code, left, right, grade_left, grade_right, page. 480 rows, 609 cells, grade H 507 / M 102 (H = read from a period key
  sheet, both blind passes agree or settled from the image; M = doubtful, cut by the page edge, or one pass's reading taken unsettled).
- `build_keys.py [--check]`: `key_L/R0/R100/LR100.tsv` (gated, "zero" nulls dropped, PREREG item 3), `key_<X>_z.tsv` (nulls kept,
  reported), `key_decode.tsv`.
- `test_key_*.txt`: `../sibling_michell/test_sibling.py --key key_r4376/key_<X>.tsv --out key_r4376/test_key_<X>.txt --seed 1 --oov-floor`.

Transcription conventions (as `../key_r4372/README.md`, plus 6-7):
1. `~word` = struck through, NOT used. 2. A right entry is recorded on the printed row on whose line its trailing dash sits; between two
rows, the upper row (M if the readers split on the row). 3. A trailing `?` = doubtful letter(s), kept, graded M. 4. `zero` = a null, kept
as written. 5. `/` joins two readings the hand wrote on one cell. 6. The strip LEFT of block 1-100 holds right entries whose dash points at
a code c in 1-100: stored as a right entry on row c-100 (codes -99..0, page `P3-strip`), so R100 attributes it to c. 7. 501-600: left
entries cut by the page edge, stored with `…` (dropped in build) and graded M.
