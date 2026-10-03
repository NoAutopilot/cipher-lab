# Blind same-hand sign-sorting call (GAPS37). You see handwritten signs only; you are told nothing about what they mean.

Query lines: images/crops_2077_leg/leg77_<Lnn>_s1.jpg (left part of the line) and leg77_<Lnn>_s2.jpg (right part), for
Lnn in: L02 L03 L05 L06 L08 L09 L10 L11 L12 L14 L15 L16 L18 . The two parts overlap by about 250 px (s2 begins about 1050 px into s1's width).
Read only those 26 image files and passes/signcmp_gaps37/query_sequences.txt. Do not open any other file in the repository.

For each line in query_sequences.txt, the line's signs are listed left to right as transcriber codes (shape nicknames),
with some positions replaced by a query number #k, and plain-script words shown as <plain:...>. All 46 queries #1-#46 were
given ONE nickname by the transcriber, but they may in fact be one letterform or two or more letterforms of the same hand
that look alike (e.g. differing in how the descender ends, or whether the bowl is closed). Your task is to sort them.

1. Find each #k by counting along the line from its neighbours, and look closely at that one sign.
2. Describe it with two features: bowl = closed / open / unclear; descender = straight / curls-left-open / closed-loop /
   curls-right / none / unclear.
3. Look across all 46 and decide how many distinct letterforms there are (1, 2 or more). Name them F1, F2, ... and say in
   one line each what defines them. Then assign every #k to one form, with your confidence 0-1 that it belongs to that form
   and not to another, and say whether you are sure you found the right sign (located = sure / approx).
Do not force a split that is not there, and do not force everything into one form if you see two.

Return: first the form definitions (lines starting "FORM F1: ..."), then TSV, header:
query  line  bowl  descender  form  form_conf  located  note
one row per query, all 46.
