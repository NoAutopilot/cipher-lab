# VERIFY-F61-V6 vision prompts -- WRITTEN BEFORE THE CALLS (29 Sept 2026, 04:24 UTC)

Three fresh Opus subagents (one per call), each seeing only the sheets named, no repository file, no letters, no runner reply.
Items and their key: `items_v6.tsv` (tiles_v6.py). Sheets in the verifier's scratchpad (regenerable by `tiles_v6.py tiles SCRATCH`
after cut_bands.py on canvases 327/328, `h193_attr.py tiles`, and the f.61 slope fits in the scratch file f61_slopes.txt).
Disclosure: the verifier looked at c1_01, c2_01 and f61_L05 for legibility before the calls (A011 is a nearly blank tile; two
f.176r tiles carry a thin red stroke at the top edge from the band crop, away from the marked sign).

Common text (calls 1-3): "You are a blind shape reader. Use no tool but your image reader (Read) on the images named; run no command,
write no file, read nothing else. No letters are involved. The question, for each marked sign: does that sign's vertical stem run down
below the writing line and end in a closed loop or bowl (like the bottom of a 'b')? Answer yes or no; if the marked sign cannot be told
(blank, cut off, marker not on a sign), answer n."
- Call 1: control_K.jpg (K01-K20, red triangle UNDER the sign) and c1_01..c1_05.jpg (A001-A100, blue triangle UNDER the sign).
- Call 2: control_K.jpg and c2_01..c2_06.jpg (B001-B114; a blue triangle either UNDER the strip pointing up, or ABOVE the strip pointing
  down at the upper row of writing -- any smaller writing lower in such a strip is not the sign).
- Call 3: control_K.jpg, c3_01.jpg (C001-C020), and six line sheets f61_L01, L03, L05, L07, L08, L11 (a cipher line cut into two parts,
  read part 1 then part 2, left to right; ordinary handwritten words are not signs): list every sign shaped like a figure 4 (a 4 with
  anything attached), in order, numbered 1, 2, 3..., and answer the same question for each.
Reply: a TSV block 'id<TAB>answer' (calls 1-2: K rows then target rows; call 3 adds rows 'L01:1', 'L01:2', ...).
GATE per call: K >= 17/20 in the runner's direction (CP yes, AN no) AND the verifier-framed anchors (set FA) >= 17/20; else that call's
targets are not scored.
