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

## Decoding conventions (stated 4 Oct 2026 by LANE-READ2 after the READ2-HELRD rule-7 re-derivation)

READ2-HELRD re-derived R1953 from the spec and key alone: 845/846 tokens agreed. The one difference (token 355, code 1023) and two
trial-matched choices come from conventions that were only in `build_keys.py`'s docstring. They are:
1. A cell whose text starts with `~` is crossed out on the sheet and is NOT used (code 1023's left cell `~satisfa` -> U).
2. A right-hand entry belongs to code+100 (the LR100 attribution chosen by the control-backed test, grade S); where a left cell and a
   right entry land on the same code, the right entry is used.
3. A trailing `?` on a ciphertext token (e.g. `990?`) is read as usual but graded M; an inner `?` (a doubtful digit, e.g. `128?3`) is unkeyed (U).
With these three rules a spec-plus-key reader reproduces the committed reading 846/846 (READ2-HELRD's own statement). The reading
itself is unchanged; `tools/decode_key.py ciphers/hellen-frederick-1752/key_r4369 --check` still passes.
