You are checking single tokens in a 16th-century Spanish numeral cipher (two copies of the same letter, written by a clerk). Do not decipher.
For each item listed in BATCHFILE (one per line, tab-separated), open its image with the Read tool. The image has PANEL A (top: one line of
copy 1) and PANEL B (below: the corresponding line of copy 2). Faint strokes of neighbouring lines may show at the panel edges; use only the
line centred in each panel. Each item names a token position in A and in B (1-based count of numeral groups/tokens along the line, left to right,
counting the words in letters such as y or xum as tokens; any ordinary handwriting at the start of a line is not counted), with the
neighbouring tokens as transcribed earlier (they may contain errors; use them to find the place), and a PROPOSAL P.

Notation: a number as written (21, 236); right after it a vowel sign: + (small cross), . (dot), ρ (looped e/p-like tail), σ (small hook like a
6 that is not clearly a digit), ⊣ (u-like hook); then marks ABOVE the number: @n = ^ circumflex/hat, @s = straight horizontal bar, @l = short
slanted acute stroke, @m = wavy tilde ~, @r = small r- or v-shaped hooked mark, @2 = two dots; _ = underline; {abc} = a word in letters.

Task per item: (1) look at panel A at the named position and write what you see there in this notation (your own reading); (2) decide whether
panel A's token there IS exactly the proposal P (number, vowel sign AND mark all the same). Copy 2 (panel B) may legitimately differ from copy 1:
the clerk sometimes enciphered differently, so judge panel A on its own ink; B only helps you find the place. Verdict: yes (A clearly shows P),
no (A clearly shows something else), unclear (cannot tell). Zoom mentally; be strict.

Write a TSV to OUTFILE: header line `id\tA_seen\tverdict\tnote`, then one row per item in order (note: a few words). Reply only "done N items".
