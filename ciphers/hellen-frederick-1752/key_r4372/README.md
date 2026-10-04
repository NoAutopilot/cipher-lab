# R4372 candidate first half (NEAR3-HEL4, account 2, 4 Oct 2026)

Source: DECODE R4372, BL Add MS 32276 f.48 (undated, no named holder), same printed form and layout as R4369 (`../key_r4369`).
The images are not committed (not public domain); `../images/decode/manifest.json` has their URLs and sha1s (both matched on refetch).

- `PREREG.md`: pushed (453a570a) before the images were fetched.
- `key.tsv`: code, left, right, grade_left, grade_right, page. P2 = codes 1-500, P3 = 501-1000 (601-700 and 901-1000 empty;
  801-900 carries 868 left and two right entries). 400 rows, 477 cells, grade H 445 / M 32 (H = read from a period key sheet, both
  blind passes agree or settled from the crop; M = settled by taking one pass's reading, or a doubtful row for a right entry).
- `build_keys.py [--check]`: `key_L/R0/R100/LR100.tsv` (restricted to 1-800), `key_full_LR100.tsv` (rival, 1-1000), `key_comb_<X>.tsv`
  (X + `../key_r4369/key_LR100.tsv` 801+; PREREG item 6, reported not gated), `key_decode.tsv`.
- `test_key_*.txt`: `../sibling_michell/test_sibling.py --key key_r4372/key_<X>.tsv --out key_r4372/test_key_<X>.txt` (seed 1).

Transcription conventions (stated here, READ2-HELRD lesson):
1. `~word` = struck through on the sheet, NOT used (`build_keys.py` drops it). A cell like `~avoit ~auroit avoit` keeps only `avoit`.
2. A right entry is recorded on the printed row on whose line its trailing dash sits; between two rows, the upper row (grade M if the
   readers split on the row). Which code it belongs to is the attribution under test (R0, R100), as for R4369.
3. A trailing `?` in a cell = doubtful letter(s), kept, graded M; a cell that is only `?`/`~?` is empty.
4. `zero` is written on the sheet (a null); kept as the meaning `zero`, as in `../key_r4370` (24 codes).
5. Dropped as not part of the table: 803 "49" (modern pencil folio number), 899 "2 on?" and a speck at 940 (no legible entry).
Where the left cell holds two words with a separator (`com/m`, `personne/senateur` with the first struck), the struck word is `~`-prefixed.
