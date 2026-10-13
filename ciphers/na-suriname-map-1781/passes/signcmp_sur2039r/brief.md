# Blind sign-comparison call (SUR-2039R). You see handwritten signs only; you are told nothing about what they mean.

Working directory: /home/user/cipher-lab/ciphers/na-suriname-map-1781
References: passes/signcmp_sur2039r/blind_refs.jpg -- 54 reference sign tiles labelled R1-R54, cut from one period sheet.
Query lines: images/crops_2039_remN/remN_<Lnn>_s1.jpg, _s2.jpg, _s3.jpg (left, middle, right parts of one line; neighbouring
parts overlap, so do not count an overlapping sign twice). L01 is a short heading in larger letters (it may sit in s1 only);
L02-L06 are a paragraph in a small hand; L06 is a short last line. Neighbouring lines may intrude at the top or bottom of a crop:
use only the line centred in it. Thin ruled lines may cross the crops: ignore them. Read only the files named here (do NOT open
remN_lines_debug.jpg or any other file in the repository).

For each line in passes/signcmp_sur2039r/query_sequences.txt, the line's signs are listed left to right as transcriber codes
(shape nicknames), with some positions replaced by a query number #k and plain-script numbers shown as <plain:...>.
Find each #k by counting along the line from its neighbours, look at that one sign (including any accent, dot, hook or flourish
on it), and choose which reference tile R1-R54 it is the same sign as (same shape, allowing for hand variation and size). Then
give your second choice. If none fits, say NONE (NONE is a valid answer; do not force a match).

Return TSV only, one row per query, header: query  line  best  best_conf  second  second_conf  located  note
- best_conf/second_conf 0-1; located = sure / approx (you are not sure you found the right sign); note: a few words on the
  shape seen.
All 30 queries (#1-#30). Judge every query on its own: look at that sign in the image each time, do not copy an earlier row's
answer or confidence because two signs seem to be the same kind, and say in the note what you actually saw on that instance.
Write the TSV to passes/signcmp_sur2039r/result.tsv and reply with the row count only.
