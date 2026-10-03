# Blind sign-comparison call (GAPS29). You see handwritten signs only; you are told nothing about what they mean.

References: passes/signcmp_gaps29/blind_refs.jpg -- 26 reference sign tiles labelled R1-R26, cut from one period sheet.
Query lines: images/crops_2077_leg/leg77_<Lnn>_s1.jpg (left part of the line) and leg77_<Lnn>_s2.jpg (right part); the
two parts overlap by about 250 px (s2 begins about 1050 px into s1's width). Read only the files named here.

For each line in passes/signcmp_gaps29/query_sequences.txt, the line's signs are listed left to right as transcriber
codes (shape nicknames), with some positions replaced by a query number #k and plain-script words shown as
<plain:...>. Find each #k by counting along the line from its neighbours, look at that one sign, and choose which
reference tile R1-R26 it is the same sign as (same shape, allowing for hand variation and size). Then give your
second choice. If none fits, say NONE.

Return TSV only, one row per query, header: query  line  best  best_conf  second  second_conf  located  note
- best_conf/second_conf 0-1; located = sure / approx (you are not sure you found the right sign); note: a few words on
  the shape seen (e.g. "9 with closed loop", "g with open tail", "8 tilted", "ij with dots", "small c").
All 68 queries (#1-#68). Do not open any other file in the repository.
