# PREREG BAL-65C (account 1, LANE DEFAULT-A1-1426-15), 15 Oct 2026 14:4x UTC by date -u -- pushed before any fetch or look

Brief: `.claude/briefs/runs/2026-10-15-acct1-default-1426-jobs.md` "BAL-65C": BAL-65L's Verdict, more Baluze 168 Chavigny canvases for a glossed
plain 65. Exactly BAL-65L's method (PREREG-BAL-65L.md steps 1-3, unchanged), on two canvases only.

Requests: openapi.bnf.fr IIIF v3, ROOM take/release, one at a time >= 3.3 s, <= 4 in all, scratchpad only, sha1 + URL logged in
images/manifest.json `bal_65c_fetches`. Baluze 168 btv1b9001503k f346, f348 `full/2400,` (2; the other two are spare for one failed fetch or one
region re-fetch of a 65 unassignable at 2400 px). Stop before a unit that would cross 80% of cap (USD 2.0) or box (15:29 UTC).

Reader: my eye at 2400 px with 2-3x zooms of each 65 under a gloss, not blind (I know key.tsv).
1. Key-identity gate: c346 and c348 belong to the f.166 letter whose c347 passed BAL-65L's gate (8/8); re-checked per canvas: place >= 8 marked
   numerals (or all placeable) under its gloss; pass if >= 75% give the key.tsv form; else that canvas's pairs are excluded.
2. Mark rule (PREREG-BAL-302 unchanged): plain = no stroke in cipher ink above or touching the top of the 5; acute = separate rising stroke in cipher
   ink above the 6 or 5; a stroke continuous with a gloss letter is gloss; unassignable = 65?.
3. Every settled 65 under a gloss goes to f22mk/glossed_pairs_169c.tsv (65' or 65; 65? kept, not scored). If any plain 65 is added,
   `python3 f22mk/score_marks_169c.py` is re-run unchanged. Call rule unchanged: S if >= 3 glossed plain 65 give ra and that is >= 3/4 of them, AND
   real beats all 200 within-run shuffles; else M (under 3: a count, M). Only an S goes to `tools/decode_key.py ... --try` at every occurrence with
   its own power control before any key/exception entry; f.22r L04 pos 0 stays M otherwise. key.tsv, reading files and grades change only through an S.
