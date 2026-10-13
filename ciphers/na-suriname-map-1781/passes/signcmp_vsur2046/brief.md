# Blind sign-comparison call (V-SUR2046). You see handwritten signs only; you are told nothing about what they mean.

References: passes/signcmp_vsur2046/blind_refs.jpg -- 54 reference sign tiles labelled R1-R54, cut from one period sheet.
Query lines: images/crops_2046_leg/leg46_<Lnn>_s1.jpg (left part of the line) and leg46_<Lnn>_s2.jpg (right part); the two
parts overlap by about 150 px. Neighbouring lines may intrude at the top or bottom of a crop: use only the line centred in it.
Map drawing may show at the left edge: ignore it. Read only the files named here (do NOT open leg46_lines_debug.jpg).

For each line in passes/signcmp_vsur2046/query_sequences.txt, the line's signs are listed left to right as transcriber codes
(shape nicknames), with some positions replaced by a query number #k and plain-script words or numbers shown as <plain:...>.
Find each #k by counting along the line from its neighbours, look at that one sign (including any accent, dot or hook on it),
and choose which reference tile R1-R54 it is the same sign as (same shape, allowing for hand variation and size). Then give
your second choice. If none fits, say NONE (NONE is a valid answer; do not force a match).

Return TSV only, one row per query, header: query  line  best  best_conf  second  second_conf  located  note
- best_conf/second_conf 0-1; located = sure / approx (you are not sure you found the right sign); note: a few words on the
  shape seen (e.g. "triangle with stroke above", "d with hook", "loop crossed by diagonal").
All 36 queries (#1-#36). Do not open any other file in the repository.
Judge every query on its own: look at that sign in the image each time, do not copy an earlier row's answer or confidence because
two signs seem to be the same kind, and say in the note what you actually saw on that instance (marks, hooks, dots, accents).
