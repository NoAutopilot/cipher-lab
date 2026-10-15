# PREREG BAL-302 (account 4, LANE DEFAULT-A4-1035-15), 15 Oct 2026 11:1x UTC by date -u -- pushed before any fetch or look

Prior work: `tools/prior_work.py baluze167-davaux-1637 --item-spec 'Baluze 169 c302 L01 65 stroke at max; Baluze 167 c276 R16 d une E shape;
c281 c284 c267 E rows' --step-type key --offline` exit 0, generic UNCHECKED rows only (no specific hold).

Requests: openapi.bnf.fr IIIF v3, ROOM take/release, one at a time >= 3.3 s, <= 4 in all: c302 (Baluze 169 btv1b9001488b) one `full/1000,` locator
+ one `pct:` region at `max`; c276 (Baluze 167 btv1b9001489r) one `full/1000,` locator + one `pct:` region at `max` (pct regions avoid an info.json
request). Scratchpad only, never git; sha1 and URL logged.

## Part A: c302 L01 "17' 65" under "diray" (glossed_pairs_169c.tsv c302a pos 2, now 65?)
1. Mark rule unchanged from PREREG-BAL-13X rule 7: plain = no stroke in cipher ink above or touching the top of the 5 at native scale; acute = a
   separate rising stroke in cipher ink (numeral ink tone, not the grey gloss) above the 6 or 5. A stroke running continuously out of the gloss
   letter y's descender (gloss ink, joined to the y) is gloss, not a mark. Unassignable stays 65?.
2. Recorded in f22mk/strokes_13x.tsv (row updated, evidence column). If plain: added as a row to f22mk/glossed_pairs_169c.tsv (65? row kept with a
   note) and `python3 f22mk/score_marks_169c.py` re-run unchanged; with < 3 glossed plain 65 the result is a count, M; f.22r L04 pos 0 stays M
   unless that scorer's own rule gives S.

## Part B: c276 R16 "[deffaut] d'une" pos 1 (s:E, unit '-')
3. Shape classes as defined by BAL-E293 (NOTES): epsilon E = two open curved bowls, no bar; Ebar = flat-topped capital E whose middle stroke runs
   through and projects left of the stem, small loop at the foot. Called by eye at max; unclear stays s:E.
4. Logged in c275g/glossed_pairs_g.tsv (label only: s:E -> s:Eeps-as-s:E or s:Ebar; unit stays '-', since "d'" leaves no letter for it either way).
   No grade or key change by itself; if Ebar, it is a third Ebar context (null-like) noted for the Ebar value question; no --try (Ebar has no
   ciphertext-file occurrence; any --try would be n 0/1 undecided by construction).

## Part C: c281/c284/c267 E rows for the Ebar form, from disk
5. Only images already on local disk may be used (no further requests in this job). If none of those canvases is on disk, logged "not on disk, not
   checked" with the regen URL, not a negative.
