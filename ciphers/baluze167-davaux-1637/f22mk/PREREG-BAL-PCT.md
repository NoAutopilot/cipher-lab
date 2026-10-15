# PREREG BAL-PCT (account 4, LANE DEFAULT-A4-1035-15), 15 Oct 2026 11:3x UTC by date -u -- pushed before any fetch or look

Prior work: `tools/prior_work.py baluze167-davaux-1637 --item-spec 'Baluze 169 c302 L01 65 stroke at max pct:37,40,10,5; Baluze 167 c276 R16
d une E at max pct:53,78.5,8,5' --step-type key --offline` exit 0 (generic rows only, as BAL-302).

Requests: openapi.bnf.fr IIIF, ROOM take/release, one at a time >= 3.3 s, 2 in all, no locator: Baluze 169 btv1b9001488b f302
`pct:37,40,10,5/max`; Baluze 167 btv1b9001489r f276 `pct:53,78.5,8,5/max` (both boxes measured by BAL-302 by ink profile on the 1000 px
locators). Scratchpad only, never git; sha1 and URL logged. If a region misses its target, that is logged as a miss; no third request.

Rules are those of PREREG-BAL-302 unchanged:
- Part A (c302 L01 "17' 65" under "diray"): plain = no stroke in cipher ink above or touching the top of the 5; acute = a separate rising stroke in
  cipher ink above the 6 or 5; a stroke running continuously out of the gloss y's descender (gloss ink, joined to the y) is gloss, not a mark;
  unassignable stays 65?. Recorded in f22mk/strokes_13x.tsv. If plain: row added to f22mk/glossed_pairs_169c.tsv and
  `f22mk/score_marks_169c.py` re-run unchanged; under 3 glossed plain 65 it is a count, M; f.22r L04 pos 0 regrades only if that scorer's rule
  (or decode_key --try / the corrections path) gives S.
- Part B (c276 R16 "[deffaut] d'une" pos 1): epsilon E = two open curved bowls, no bar; Ebar = flat-topped capital E whose middle stroke runs
  through and projects left of the stem, small foot loop. Called by eye at max; unclear stays s:E. Label only in c275g/glossed_pairs_g.tsv; unit
  stays '-'; no --try (n 0/1 undecided by construction).
