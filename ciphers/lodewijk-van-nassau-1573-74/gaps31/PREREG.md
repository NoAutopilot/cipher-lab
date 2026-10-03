# GAPS31 pre-registration (3 Oct 2026, written and pushed before any scoring run; clock read 06:1x UTC)

Step (Verdict line, GAPS28): align the band tokens of the Groen-printed 5810 (142 x5, 140 x3, 149 x4, 139 x2, 147 x2,
125 x1) and 5811 (139 x2, 140 x2, 150 x2) to print, to decide 139/140/142 (and 149, 150) NULL vs letter from the print side.

Instrument: `tools/interlinear_align.py align --floor 121 --clear-consumes --prior key_full.tsv` (the AX-COMP recipe)
on pairs cut by `axcomp/build_pairs.py` (unchanged, clear-word anchors >= 9 letters) with Groen IV CDLXVIII (5810) and
CDLXXXIII (5811) as the plain text (same spans as `axnames/align_names.py`). Driver `gaps31/run.py`. Codes 1-120 are
seeded from key_full; codes >= 121 are never seeded, so every band meaning comes from print alone (grade C at most).
This is a different aligner (hard-EM, consistency across occurrences, whole-letter pairs) from AX-NAMES' anchored DP,
which counted only clusters with >= 3 exact letters each side; it is NOT an independent witness of the same print,
only a second reading of it. Its observations are counted on their own, never pooled with names.tsv.

Controls (both can come out differently from the target on the statistic, empty vs non-empty chunk per occurrence):
- NULL class: the 16 C-graded null codes 121-144 in key_full, scored from the target run (they are unseeded there).
  Per code: called NULL if > 50% of its occurrences take an empty chunk. Per-occurrence empty rate p_null reported.
- letter class: a separate run (`run.py hide`) renames the 13 rarest C single-letter codes with >= 2 occurrences in
  5810+5811 (96 57 86 66 15 65 116 25 75 80 111 94 115; n = 2-12, matched to the band's n = 1-5) to unseeded codes
  760-772. Per code: called letter if > 50% of occurrences take a non-empty chunk. Per-occurrence false-empty rate
  q reported; value accuracy (top chunk == key_full letter) reported, not gated.

Gate (all three, else nothing is applied and the band is logged untested-by-this-tool at this N):
- G1: >= 0.80 of the 16 null codes called NULL.
- G2: >= 0.80 of the 13 hidden letter codes called letter.
- G3: q <= 0.316, so that 4 unanimous empty observations of a letter code have probability q^4 <= 0.01.

Licence (only if G1-G3 pass): a band code becomes NULL at grade C (class b, unchanged) iff its observations in this
target run, 5810 + 5811 together, are >= 4 empty and 0 non-empty, AND none of its occurrences contradicts names.tsv's
observation at the same occurrence (rule 4: a conflict is logged, never settled by majority). A band code with any
non-empty observation is recorded, not applied. If a code is lifted: key_full row added with source "GAPS31 print
alignment", readings regenerated, decode --check exit 0.
No parameter of the tool, the cutter or this rule is changed after the first scoring run.
