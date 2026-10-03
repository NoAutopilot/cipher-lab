# R4369 Hellen key (READ2-HEL, account 2, 3 Oct 2026)

Source: DECODE R4369, BL Add MS 32276 f.44 (English Deciphering Branch), "Hellen avec le Roy de Prusse", 1751. The images are
not committed (not public domain); `../images/decode/manifest.json` has their URLs and sha1s. Codes 801-1796 only.

- `key.tsv`: code, left, right, grade_left, grade_right, page. Two blind Sonnet passes per page on 40 `tools/iiif_lines.py` column
  crops, then reconciliation. err_2reader 4.8% (44/908 cells). err_true is not measurable. '~' marks a crossed-out word.
- `build_keys.py [--check]`: derives `key_L`, `key_R0`, `key_R100`, `key_LR100`, `key_Lonly`, `conflicts_L_R100` and `key_decode.tsv`
  (the graded key for `tools/decode_key.py`; R100 values graded S).
- `test_key_*.txt`: output of `../sibling_michell/test_sibling.py --key key_<X>.tsv --out test_key_<X>.txt` (seed 1).
- `decode.json`, `R1953_pipe.txt` -> `reading_R1953.txt`, `reading_R1953_tokens.tsv` via
  `python3 tools/decode_key.py ciphers/hellen-frederick-1752/key_r4369 [--check]`.
- `judge_calib.py` -> `judge_calib_output.txt`: the judge run on true decodes at this key's coverage.
See NOTES.md "READ2-HEL" and HYPOTHESES.md.
