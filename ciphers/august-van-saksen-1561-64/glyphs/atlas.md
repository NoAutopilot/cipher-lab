# Glyph atlas -- ciphers/august-van-saksen-1561-64

Built 24 September 2026 (LANE R worker R14, `.claude/briefs/runs/2026-09-24-lane-r-nb2-atlas.md`), by eye from
the page images already on disk (`images/`, rendered at 100dpi by worker R9 -- see NOTES.md "Image capture,
24 September 2026"), from **74 p3-p4, 98 p2 and 126 p4 together**, per the brief. No pixel-crop segmentation
pipeline (no PIL/cv2/ImageMagick in this container; `pip install` is out of scope for a $7 cap): unlike
`ciphers/dupuy452-carpi-1520/glyphs/`, this atlas gives a shape description and example locations per code
instead of a cropped PNG per sign. Follows `.claude/briefs/transcription.md` "Symbol alphabets" in spirit (one
shared code book before any pass, so two blind passes can be reconciled row by row) but not in mechanism.

**Design of this cipher differs from a pure invented-sign alphabet** (contrast dupuy452): all three source
pages mix plain Arabic digits 0-9, plain Latin letters used as cipher signs in their ordinary printed shape
(X, V, Z, T, S, R, N, K, M, H, Q, W -- these are read as themselves, no atlas code needed, since two blind
readers cannot disagree on what a printed "X" looks like the way they can on an invented glyph), and a smaller
set of genuinely invented or Greek-derived symbols and diacritics, which is what this atlas codes.

**Confidence:** low-to-medium on rare/ambiguous shapes at this resolution (R9's note already flags 100dpi as
lower than the 150dpi used for NB1/NB4; a re-fetch at higher resolution is recommended before any solver pass,
not done here -- brief did not name re-fetching and this worker has no network host in scope). Each pass must
flag any glyph it cannot confidently match to a code below as `NEWn` with a one-line description rather than
force-fitting it, per the pass instructions in NOTES.md.

## Symbol codes (non-alphanumeric / invented signs only)

| code | shape | closest Unicode | seen in (briefnr/page) | notes |
|---|---|---|---|---|
| G1 | capital, apex-only triangle, open base (like a peaked tent with no floor) | Λ (GREEK CAPITAL LAMDA) | 53p1, 57p3, 74p3, 74p4, 126p4 | most frequent symbol across every page seen; sometimes drawn taller/narrower |
| G2 | closed triangle (apex + base stroke) | Δ (GREEK CAPITAL DELTA) | 53p1, 57p3 | not confidently seen in 74/98/126 this pass -- may be repertoire-specific to 53/57, flag for the passes to confirm |
| G3 | cursive squiggle, a looping stroke like a reversed "3" or a tailed "v"/"w", drawn in one continuous motion | ϖ (GREEK PI SYMBOL) used as a working label only, not a claim of Greek pi | 53p1 (prior worker's read), 57p3, 74p3, 74p4, 126p4 | the single most distinctive recurring invented sign; R9's inventory called this "ϖ-like"/"ѵ-like" independently for 53/126 |
| G4 | three (occasionally two) short vertical strokes under one horizontal top bar | π (GREEK SMALL LETTER PI, capital-height) | 53p1, 57p3, 74p3 | not confidently seen in 98p2/126p4 this pass |
| G5 | small cross/plus mark, either full-size as its own sign or reduced as a superscript diacritic sitting above a digit or letter | † / ⁺ | 98p2 (several superscript instances above digits, e.g. mid-line 3 and 5), 126p4 (superscript instances, e.g. line 2 and line 6) | **diacritic vs. independent sign is unresolved** -- record both readings when in doubt: the base sign, then a separate `G5` token if it looks free-standing, or `G5d` appended as a diacritic flag if it sits directly above another sign (cf. LESSONS.md's Birago 1571 lesson: superscript crosses over digits were a real diacritic class there) |
| G6 | backward "C" / open hook opening left | ε (GREEK SMALL LETTER EPSILON) used as working label | 74p3, 98p2 | |
| G7 | small checkmark / narrow "v" with a short tail, lowercase-height | λ (GREEK SMALL LETTER LAMDA) used as working label | 74p3 | rare this pass, one clear instance |
| G8 | small circle, sometimes with a short horizontal bar through it | θ (GREEK SMALL LETTER THETA) used as working label | 126p4 | |
| G9 | letter-like shape with a small hook or cedilla below (an "e" or "c" with a tail) | ę / ç -style tail | 126p4 | low confidence, one instance |
| G10 | horizontal overline sitting above a digit or short digit group | combining overline | 98p2 (over one "M"-like sign) | cf. briefnr 153 in this same correspondence circle, whose whole cipher is overlined numerals (see NOTES.md/inventory.tsv) -- overlining may be a house convention across this circle's ciphers, not unique to one letter |
| G11 | backward "C"/hook, larger and squarer than G6, resembling an open bracket | ⊃ | 98p2 | distinguish from G6 by size/squareness; low confidence, may be the same sign as G6 seen twice |
| G12 | vertical stroke with a small flag/hook at the top, digamma-like | Ϝ | 98p2 | one instance, low confidence |
| G13 | small star/asterisk flourish, several short strokes crossing at a point | ✳ | 53p1 | one clear instance mid-block |
| G14 | a blotted or struck-through rounded sign at the head of a cipher block, resembling a ligature (an "O"/"Q" shape crossed by a bar) | Œ-like ligature, working label only | 57p3 (head of the first of the two cipher blocks on this page) | very low confidence -- may be an ink blot / pen flourish rather than a cipher sign; flag for eye-check on the image, not the atlas |

## Repertoire comparison: does 53/57 match 74/98/126?

**Partial overlap, not identical.** 53 (p1 postscript) and 57 (p3 block) share G1 (Λ), G3 (the cursive
squiggle) and G4 (π) with the 74/126 block ciphers, and both also show G2 (Δ) and, in 53 only, G13 (the star
flourish) that were **not** confidently seen in 74/98/126 this pass. 74 and 126 share G1 and G3 heavily but
not G2 or G13. 98 stands apart: numerals dominate and its distinctive marks are the diacritic/hook family
(G5, G10, G11, G12), not G2/G4/G7/G8/G9. This confirms R9's image-capture note (NOTES.md, "Six distinct cipher
designs observed") rather than overturning it: 53/57 look closer to 74/126's symbol-plus-digit design than to
98's numeral-dominant design or 153's pure-numeral design, but the codebooks are not shown identical by this
pass -- G2 and G13 in 53/57 with no confirmed counterpart in 74/98/126 is exactly the kind of thing the two
blind passes below should either confirm (found in 74/98/126 too, atlas was incomplete) or corroborate
(genuinely absent, the repertoires only partially overlap). Do not assume 53/57 share one key with 74/98/126
without this being settled by the passes and, eventually, by a solver.

## Method note for the two passes

Read each cipher-block line left to right. For every mark:
- A recognisable printed Latin letter (X V Z T S R N K M H Q W ...) or Arabic digit (0-9): record it literally.
- A mark matching one of G1-G14 above: record the code.
- A diacritic (dot, cross, overline) sitting on top of another sign: record the base sign, then append `d`
  to the diacritic's code on its own token immediately after (e.g. base `3` then `G5d`), do not merge them
  into one string.
- Anything not covered above: record `NEW1`, `NEW2`, ... (numbered per your own pass, not shared with the
  other pass) and add one line per NEW code at the end of your TSV as a `#` comment describing its shape and
  exact location (briefnr/page/line/idx), so the reconciler can look at the image.
- Word/group breaks (visible gaps in the manuscript line): start a new `idx` but do not insert a separate
  "space" sign; the reconciler compares position-by-position within each `line` key, and gaps are handled by
  the alignment, not by an explicit token.
