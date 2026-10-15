You are transcribing single tokens in a 16th-century Spanish numeral cipher written by a clerk. Do not decipher.
For each item listed in BATCHFILE (one per line, tab-separated), open its image with the Read tool. Each image shows ONE line of cipher (faint
strokes of neighbouring lines may show at the edges; use only the line centred in the image). Each item names a token position (1-based count of
numeral groups/tokens along the line, left to right, counting words in letters such as y or xum as tokens; any ordinary handwriting at the start of a
line is not counted), with the neighbouring tokens as transcribed earlier (they may contain errors; use them only to find the place).

Notation: a number as written (21, 236); right after it a vowel sign: + (small cross), . (dot), ρ (looped e/p-like tail), σ (small hook like a
6 that is not clearly a digit), ⊣ (u-like hook); then marks ABOVE the number: @n = ^ circumflex/hat, @s = straight horizontal bar, @l = short
slanted acute stroke, @m = wavy tilde ~, @r = small r- or v-shaped hooked mark, @2 = two dots; _ = underline; {abc} = a word in letters.
Examples: 17.@n, 24ρ, 6σ, 15+@s, 231, {y}.

Task per item: write exactly what the token at the named position is, in this notation (number, vowel sign, and any mark above it). Look closely at
the digits, the sign right after them and the space above them. If you genuinely cannot tell, write `unclear`. Be strict and literal.

Write a TSV to OUTFILE: header line `id\tread\tnote`, then one row per item in order (note: a few words). Reply only "done N items".
