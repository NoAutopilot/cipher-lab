# call D (Opus subagent, 27 Sept 2026 ~16:09-16:12 UTC, MONT-DOTS2): the eight half-sheets images/f81rdots_L{03,08,13,15}{a,b}.jpg
# only; 124,828 subagent tokens, 9 tool uses, 177 s. Raw TSV as returned is call_D.tsv (the reader said its stray spaces
# are slips; the scorer ignores them). Scores: fix_call_D.txt (margin 8, decides), fix_call_D_m0.txt, precision_D.txt.
# Prompt, verbatim (committed this time, unlike calls A and C; wording follows call C's recorded instruction set plus
# the stacked-segment layout, adapted to two sheets per line):
#   You are transcribing four lines of a 1589 French cipher letter (numeric cipher, handwritten digits). Read ONLY these
#   eight image files with the Read tool, nothing else, and write no files: [the eight paths]
#   Layout: each line of the letter is cut into 12 consecutive horizontal segments, stacked vertically in reading order
#   and labelled in red ("L03 segment 1 of 12" ...). Sheet "a" holds segments 1-6, sheet "b" segments 7-12, so read L03a
#   then L03b as one line. Consecutive segments overlap by a few characters: do not read the overlap twice. The line to
#   read is the central row of each strip; ignore the partial rows above and below (neighbouring lines). The last
#   segment may be past the end of the line.
#   Instructions for each line:
#   - Read the digits left to right as ONE continuous digit string, with no grouping and no spaces.
#   - If a digit carries a dot or a stroke above it, put a single apostrophe ' immediately before that digit.
#   - If you cannot decide a digit, write ? in its place. Never guess.
#   - Pay particular attention to the small dots above digits; they matter.
#   Return exactly a TSV with a header and one row per line: line / digits_with_marks / confidence
#   After the TSV, add a short "Warnings" list: glyph shapes you were unsure of, marks you could not classify, any place
#   a segment lost the line, and at what scale you believe you saw the images (e.g. native or downscaled).
# The line "Pay particular attention to the small dots" is an addition to call C's recorded instruction set; call C's
# own prompt text was never committed, so no byte comparison is possible (disclosed in NOTES.md).
# Reader's warnings, in substance:
# - the most frequent '?' is ONE recurring glyph: a small open loop with a long tail rising to the right, almost always
#   before 3, 4 or 5, dozens of times in all four lines; "clearly a distinct cipher sign, possibly an 8 or a variant 0";
#   left as '?' every time. (Call C read this shape as 8, with its own warning that it might be 0 joined to 5.)
# - L03: a small closed loop with a crossed ascender (segs 4, 9/10) written '?; an inverted triangle in segs 7/8.
# - small raised u-like glyphs at L03 seg 5, 7, 10/11 and L08 seg 9 (with an underline below "4?2").
# - length uncertain at L03 seg 5-6 (one sign or two).
# - marks possibly belonging to a neighbouring glyph: L08 seg 9/10 tick; L13 seg 2/3 hook on a 3; L15 seg 6/7 colon-like
#   sign written '?; L15 seg 10/11 dot between 4 and 2 assigned to the 4; L15 end "'94" may be a correction.
# - ignored: dots below the line; a mid-height dot inside the 6 of several 65 pairs in L08; L13's trailing colon marks.
# - glyph forms: 5 a tall long-s; 6 b-like; 1 an undotted i (a dotted one written '1); 0 a small o; 9 sometimes q-like.
# - no segment lost the line; segment 12 blank/past the end on all four.
# - scale: sheets shown at about 1350 px wide, "probably downscaled, not native"; small dots "visible but only just
#   resolvable".
