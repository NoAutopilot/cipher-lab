# Blind same-hand letterform sorting call (GAPS45). You see handwritten signs only; you are told nothing about what they mean.

Query lines: images/crops_2077_leg/leg77_<Lnn>_s1.jpg (left part of the line) and leg77_<Lnn>_s2.jpg (right part), for
Lnn in: L05 L07 L08 L09 L10 L11 L12 L13 L14 L15 L17 L18 L19 . The two parts overlap by about 250 px (s2 begins about 1050
px into s1's width). Read only those 26 image files and passes/signcmp_gaps45/query_sequences.txt. Do not open any other
file in the repository.

For each line in query_sequences.txt the signs are listed left to right as transcriber codes (shape nicknames), with some
positions replaced by a query number #k. Plain-script words are shown as <plain:...>, and some of them have one letter
replaced by #k. The 32 queries #1-#32 are all small letterforms of the same hand; some may be the same letterform, some
different. Your task is to sort them by shape.

1. Find each #k by counting along the line from its neighbours (inside a plain word, by its letter position), and look
   closely at that one sign.
2. Describe it: body = one-hump / two-hump / three-hump / u-shape / y-shape / other; descender = none / straight / loop /
   curl; mark above = dots / loop / none / unclear.
3. Look across all 32 and decide how many distinct letterforms there are. Name them F1, F2, ... and say in one line each
   what defines them. Assign every #k to one form, with your confidence 0-1 that it belongs to that form and not another,
   and say whether you are sure you found the right sign (located = sure / approx).
Do not force a split that is not there, and do not force signs together that differ.

Return: first the form definitions (lines starting "FORM F1: ..."), then TSV, header:
query	line	body	descender	mark_above	form	form_conf	located	note
one row per query, all 32.
