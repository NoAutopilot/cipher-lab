# Reconciliation: p2 line 1, two blind passes (OX-WV69, 25 Sept 2026)

Brief item 1 asked for two blind subagent passes over p2-p4, reconciled, with a 60% agreement gate
(`.claude/briefs/transcription.md`). Scoped down to line 1 of p2 only (the line OX-WVH's `key_1069.tsv`
already partly read from a tight crop, `crop_grumbachs.png`), as a feasibility check before committing to
the full ~61 line-pairs across p2-p4.

Both passes read the same crop (`/tmp/wv69_render/p2_strip00.png`, not committed -- see regeneration note
in NOTES.md) blind, with no access to each other or to `key_1069.tsv`. Raw tables: `passA_p2line1.tsv`,
`passB_p2line1.tsv`.

## Result: below the 60% gate

The two passes do not even agree on how many cipher glyphs are on the line (pass A: ~22 before the torn
corner; pass B: 26). At the level the gate is meant to measure -- does pass A's glyph-shape-N give the same
plaintext letter as pass B's glyph-shape-N at the same position -- agreement is well under 60%: the two
passes name different shapes for the letters they do agree on (e.g. pass A's position 6 "twin-vertical-bars"
= "r/t" vs pass B's position 6 "double-loop-no-crossbar" = "t" -- different shape descriptions, claimed to
be at "the same" position, decoding to a compatible letter more by luck than by a shared glyph identification).

What DOES roughly agree, at the level of whole words rather than individual glyphs:
- Word 1 ends "...m i t" (both passes, independently, with medium-high confidence on m/i/t specifically) --
  consistent with `key_1069.tsv`'s existing H-grade anchor (capital-H-with-crossbar = t, "end of mit").
- Word 2 is "g _ _ _ a c h s"-shaped (both passes agree on g...achs, both are unsure of the 2-3 letters in
  between) -- consistent with the existing M-grade uncertainty already recorded in `key_1069.tsv` for
  those middle positions (u/m, n/b).
- Word 3 (NOT previously read) is "_ b e w e r _ u _ g"-shaped in both passes, plausibly "(o/s)bewerdung" --
  new information, but neither pass is confident enough in individual glyph shapes to add a clean new
  sign->letter row.

## Conclusion (transcription.md's own rule)

"If pass agreement is under 60%, stop and report the blocker; the next step is a glyph atlas, not a third
pass." That is the finding here, on the *easiest* line of the three pages (the one line already partly
anchored). Whole-line strip crops are not tight enough for this manuscript's small, crowded interlinear
hand -- the OX-WVH original 10-sign read only worked because it used a single tight multi-glyph crop
(`crop_grumbachs.png`) at higher effective zoom, not a full-row strip. Extending `key_1069.tsv` or reading
p2's other ~23 lines, or p3/p4, needs per-glyph (or short multi-glyph) crops cut at the actual ink, the way
`crop_grumbachs.png` was, before another transcription pass is worth running -- exactly the atlas step this
repo's shared tooling (`tools/iiif_lines.py`'s design, `.claude/briefs/transcription.md`'s "Symbol alphabets"
paragraph) already prescribes for invented-sign pages. That per-glyph cropping is the concrete next step,
and it is out of this session's remaining scope -- see NOTES.md's OX-WV69 section for the explicit handoff.

Four letter/shape pairs were flagged by both passes with at least medium confidence on one side and are
recorded as *unconfirmed candidates*, not added to `key_1069.tsv`, in `key_1069_candidates.tsv`: b, e, w
(word 3), r (word 3). Two of the four candidate shapes reported for these letters echo shapes already used
for *different* letters in the confirmed 10-sign key (a "double-hump-w" shape already = u at grade M; a
cross shape already = c at grade H), which is either a real homophone/confusable-hand problem or a
mis-identification by the passes -- either way, not safe to add without an image-level check.
