# Pre-registration: spec test 3, Scorpion S1 sign shapes vs Zodiac Z408/Z340 alphabets (A2P4-SCORP2, 3 Oct 2026)

Committed before any comparison is scored.

**Sets.**
- Target set: the 53 S1 sign types in `sign_table1.tsv` (LANE B2 bSCO transcription, 25 Sept 2026).
- Zodiac reference: the union of glyphs in Z408 (54 symbols) and Z340 (63 symbols), 70 glyph types, as typed in
  D. Oranchak's webtoy (zodiackillerciphers.com/webtoy, `zodiac.js` alphabet strings and char-to-glyph map, one
  image per glyph under `webtoy/alphabet2/`; fetched 3 Oct 2026). Typed transliteration + glyph images, credited.
- Control: Unicode Geometric Shapes U+25A0..U+25E5 (the first 70 code points of the block, equal size to the
  Zodiac union), coded from their Unicode character names (unicodedata, Unicode 15). Not Zodiac-derived, made of
  the same primitives (filled/half-filled circles, squares, triangles), so it CAN score higher or lower than Zodiac
  on the statistic.

**Feature code.** Each glyph gets one code:
- `L:<X>` upright Latin letter or digit X; `RL:<X>` mirrored letter; `ROT:<X>` rotated letter.
- `<base>/<fill>` for closed shapes: base in {circle, square, triangle, rect, dome, teardrop}; fill in {outline,
  solid, halfL, halfR, halfT, halfB, diag, dot, cross, hline, vline, wedge, notch, inner-triangle, inner-square}.
- `ST:<name>` open stroke glyphs: bracket, caret, slash, backslash, plus, dash, dbldash, dblbar, T, invT, gamma,
  pi, headphone, cupdot, venus, hook, gt, lt, perp, dot.
A Scorpion sign has a counterpart in a set iff some glyph in that set has the identical code (orientation of
bracket/caret/half-fill ignored only where the code itself does not name it). "Near" (same base, different
fill) is reported separately and not counted.

**Statistic.** Primary: count of S1 *non-letter* sign types (all codes except `L:`) with an identical-code
counterpart, Zodiac vs control. Letters are excluded from the primary because the control has no letters by
construction (a control that cannot differ on that axis tests nothing, rule 3). Secondary, descriptive only: S1
letter types matched in Zodiac (`L:`/`RL:`/`ROT:`), against a plain A-Z alphabet as its own baseline.

**Decision rule.** Support for "draws on published Zodiac material" = Zodiac primary count exceeds control primary
count by at least 5 sign types AND at least one S1 sign matches a Zodiac-specific glyph absent from the control
(e.g. a reversed/rotated letter or a Zodiac-only stroke). Otherwise: no support. Descriptive only, no reading;
codes are one coder's eye judgement (grade M), not a measured shape distance.
