# PREREG BAL-65G (account 4, LANE DEFAULT-A4-1236-15), 15 Oct 2026 12:5x UTC by date -u -- pushed before any fetch or look

Prior work: `tools/prior_work.py baluze167-davaux-1637 --item-spec 'Baluze 169 c297 c232 c344 glossed plain 65; Baluze 167 c281 c284 c267 E rows
Ebar form' --step-type key --offline` exit 4: the one LEAD is this job's own ROOM claim (1-own, 0.0 h); generic UNCHECKED rows only otherwise.

Requests: openapi.bnf.fr IIIF v3, ROOM take/release, one at a time >= 3.3 s, <= 8 in all, scratchpad only, sha1 + URL logged in
images/manifest.json `bal_65g_fetches`. Order: Part A 169 btv1b9001488b f297, f232, f344 `full/2400,`; Part B 167 btv1b9001489r f281, f284, f267
`full/2400,`. Up to 2 further `pct:.../max` regions only for a candidate that 2400 px cannot settle. Stop before a unit that would cross 80% of cap
(USD 3) or box (13:45 UTC).

Part A (plain 65, hypothesis = ra as 65', PREREG-BAL-169C step 3). Reader: my eye at 2400 px with 3x zooms, not blind (I know key.tsv).
1. Key-identity gate: c297 and c344 belong to letters that already passed (f.144 12/12, f.169 10/10; f22mk/gate_b169c.tsv). c232 (La Barde f.112)
   has no gate yet: if a 65 under a gloss is found there, place >= 8 marked numerals on c231-232 (or all placeable); pass if >= 75% give key.tsv.
2. Mark rule (PREREG-BAL-302 unchanged): plain = no stroke in cipher ink above or touching the top of the 5; acute = separate rising stroke in cipher
   ink above the 6 or 5; a stroke continuous with a gloss letter is gloss; unassignable = 65?.
3. Every settled 65 under a gloss goes to f22mk/glossed_pairs_169c.tsv (65' or 65; 65? kept, not scored). If any plain 65 is added,
   `python3 f22mk/score_marks_169c.py` is re-run unchanged. Call rule unchanged: S if >= 3 glossed plain 65 give ra and that is >= 3/4 of them, AND
   real beats all 200 within-run shuffles; else M (under 3: a count, M). Only an S goes to `tools/decode_key.py ... --try` at every occurrence with its
   own power control before any key/exception entry; f.22r L04 pos 0 stays M otherwise.
Part B (s:E rows c281 R23 "contenter", c284 unglossed, c267 R18/R19/R20/R22). Forms as BAL-E293: epsilon E = two open curved bowls, no bar; Ebar =
flat-topped capital E whose middle stroke runs through and projects left of the stem, small foot loop; neither = "capital, not epsilon" (BAL-PCT
c276 class). Called by eye at 2x/3x beside each other. A relabel goes into c275g/glossed_pairs_g.tsv (sign column) / hits_c275g.tsv note only; if
any glossed row changes label, `python3 c275g/count_shuffle_g.py` is re-run unchanged and its output compared. No --try (Ebar has no occurrence in
any ciphertext file; n 0, undecided by construction). key.tsv, reading files and grades change only through an S above.
