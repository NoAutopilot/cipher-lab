# PREREG BAL-65L (account 4, LANE DEFAULT-A4-1236-15), 15 Oct 2026 13:1x UTC by date -u -- pushed before any fetch or look

Prior work: `tools/prior_work.py baluze167-davaux-1637 --item-spec 'Baluze 169 c179 c180 c183 c184 c187 below line 9 glossed plain 65; Baluze
168/170 same-hand glossed plain 65' --step-type key --offline` exit 4: the one LEAD is this job's own ROOM claim (1-own, 0.0 h); generic
UNCHECKED rows only otherwise.

Requests: openapi.bnf.fr IIIF v3, ROOM take/release, one at a time >= 3.3 s, <= 12 in all, scratchpad only, sha1 + URL logged in
images/manifest.json `bal_65l_fetches`. Part 1: Baluze 169 btv1b9001488b f179, f180, f183, f184, f187 `full/2400,` (5). Part 2 only if Part 1
adds no glossed plain 65 and >= 40% of cap is left: same-hand glossed letters in Baluze 168 (btv1b9001503k) / 170 (btv1b90015040), canvases
chosen from survey.tsv before fetching, one `full/2400,` per canvas, <= 7. Stop before a unit that would cross 80% of cap (USD 3.5) or box (14:12 UTC).

Reader: my eye at 2400 px with 2-3x zooms of each 65 under a gloss, not blind (I know key.tsv). Part 1 covers c179, c180, c183, c184 whole and
c187 below line 9 (lines 1-9 of c187 were read by BAL-169).
1. Key-identity gate: c179-187 belong to the letter BAL-169 already read against key.tsv (glossed_pairs_169.tsv); no new gate. A Part 2 letter
   not yet gated: place >= 8 marked numerals (or all placeable) under its gloss; pass if >= 75% give the key.tsv form; else its pairs are excluded.
2. Mark rule (PREREG-BAL-302 unchanged): plain = no stroke in cipher ink above or touching the top of the 5; acute = separate rising stroke in cipher
   ink above the 6 or 5; a stroke continuous with a gloss letter is gloss; unassignable = 65?.
3. Every settled 65 under a gloss goes to f22mk/glossed_pairs_169c.tsv (65' or 65; 65? kept, not scored). If any plain 65 is added,
   `python3 f22mk/score_marks_169c.py` is re-run unchanged. Call rule unchanged: S if >= 3 glossed plain 65 give ra and that is >= 3/4 of them, AND
   real beats all 200 within-run shuffles; else M (under 3: a count, M). Only an S goes to `tools/decode_key.py ... --try` at every occurrence with
   its own power control before any key/exception entry; f.22r L04 pos 0 stays M otherwise. key.tsv, reading files and grades change only through an S.
