# R4370 key (READ2-HEL2, account 2, 3 Oct 2026)

Source: DECODE R4370, BL Add MS 32276 f.46, 1751, no named holder. The images are not committed (not public domain); `../images/decode/manifest.json`
has the P2/P3 URLs and sha1s (P1 docket "1751" only, P4 blank). Printed codes 1-1000 in blocks of 100 (P2 1-500, P3 501-900 + 901-1000 strip).

- `PREREG.md`: the gate, statistics, attributions and pass threshold, pushed before any image was looked at.
- `key.tsv`: code, left, right, grade_left, grade_right, page. Two blind Sonnet passes per page on 36 `tools/iiif_lines.py` column crops;
  err_2reader 13.1% (letters only, 122/934 cells). The 46 disputed codes bearing on R1953 were settled from strip montages; the other 60
  disputed codes take pass A's cell (B's if A is empty) at grade M. '~' marks a crossed-out word. H 836 / M 81 cells.
- `build_keys.py [--check]`: key_L, key_R0, key_R100, key_LR100 (codes 1-800), key_full_LR100 (1-1000), key_decode.tsv.
- `test_key_*.txt`: `../sibling_michell/test_sibling.py --key key_<X>.tsv --out test_key_<X>.txt` (seed 1).
Result: no attribution reads R1953 (or any sibling letter) above its controls; see NOTES.md "READ2-HEL2" and HYPOTHESES.md.
