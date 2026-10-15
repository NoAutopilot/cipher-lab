# PREREG BAL-65D (account 1, LANE DEFAULT-A1-1426-15), 15 Oct 2026 15:2x UTC by date -u -- pushed before any fetch or look

Brief: `.claude/briefs/runs/2026-10-15-acct1-default-1426-jobs.md` "BAL-65D": BAL-65C's Verdict, two more Baluze 168 Chavigny canvases for a
glossed plain 65. Exactly BAL-65C's method (PREREG-BAL-65C.md steps 1-3, unchanged) on 168 c438 and c440 only (the f.212 letter whose c439
passed BAL-65L's gate 17/17), with one addition BAL-65C's own caveat named: a plain-65 row goes into the pair file as its full glossed run.

Requests: openapi.bnf.fr IIIF v3, ROOM take/release, one at a time >= 3.3 s, <= 4 in all, scratchpad only, sha1 + URL logged in
images/manifest.json `bal_65d_fetches`. Baluze 168 btv1b9001503k f438, f440 `full/2400,` (2; the other two spare for one failed fetch or one
`max` region re-fetch of a 65 unassignable at 2400 px). Stop before a unit that would cross 80% of cap (USD 2.0) or box (16:08 UTC).

Reader: my eye at 2400 px with 2-3x zooms of each 65 under a gloss, not blind (I know key.tsv).
1. Key-identity gate per canvas: place >= 8 marked numerals (or all placeable) under its gloss; pass if >= 75% give the key.tsv form; else that
   canvas's pairs are excluded.
2. Mark rule (PREREG-BAL-302 unchanged): plain = no stroke in cipher ink above or touching the top of the 5; acute = separate rising stroke in
   cipher ink above the 6 or 5; a stroke continuous with a gloss letter is gloss; unassignable = 65?.
3. Every settled 65 under a gloss goes to f22mk/glossed_pairs_169c.tsv (65' or 65; 65? kept as a comment, not scored); a plain 65 goes in as its
   full run (every token of the run I can place under the gloss, unit per token, '-' where not placeable) so the within-run shuffle can vary.
   If any plain 65 is added, `python3 f22mk/score_marks_169c.py` is re-run unchanged. Call rule unchanged: S if >= 3 glossed plain 65 give ra and
   that is >= 3/4 of them, AND real beats all 200 within-run shuffles; else M. Only an S goes to `tools/decode_key.py ... --try` at every
   occurrence with its own power control before any key/exception entry; f.22r L04 pos 0 stays M otherwise. key.tsv, reading files and grades
   change only through an S.
