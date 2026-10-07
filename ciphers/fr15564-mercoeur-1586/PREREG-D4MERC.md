# PREREG-D4MERC (7 Oct 2026, committed before the sheet-matched cells file is scored)

Worker D4-MERC (account 4, LANE DEFAULT-account-4-20261007-1335). Target fr15564-mercoeur-1586, f.151.

1. Sheet: `make_glyph_sheet.py` -> `sheet/tile_{1..4}.jpg` (Lasry key image x2.2 above f.151 crop halves x0.9, about the
   same glyph height). One vision unit (this session's own read of the four tiles): each of the 48 settled labels of
   `ciphertext_draft.tsv` -> a key glyph (letter value(s)) or `none`, confidence H/M/L. Written to
   `lasry_cells_f151_sheet.tsv` (cells = letters only; nomenclator/'ff' groups and `none` excluded, as MERC151B).
2. Rerun, same flags as MERC151B: `tools/partial_key_test.py --cells lasry_cells_f151_sheet.tsv --draft ciphertext_draft.tsv
   --lang fr --keys 500 --within 10 --width 400 --min-run 4 --seed 342 --key-seed 3420`, then the same with `--shuffle-target 1`.
3. Gate unchanged: PASS only if real order gain > permuted-key p95 AND the shuffled-target run does not also pass. Fewer than
   2 runs of >= 4 keyed signs = non-test (too few runs). Overlap count = labels with a key counterpart (any confidence), out of 48.
4. A FAIL stays conditional on a 2-reader draft (err_2reader 28.8%) and on matching at the key image's 600-px resolution.
