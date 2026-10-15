You are transcribing single tokens in a 16th-century Spanish numeral cipher written by a clerk. Do not decipher.
For each item listed in BATCHFILE (one per line, tab-separated), open its image with the Read tool. Each image shows a native-resolution WINDOW of about seven tokens cut from one line of cipher (faint
strokes of neighbouring lines may show at the edges; use only the line centred in the image). Each item gives the transcribed tokens just BEFORE and just AFTER the TARGET token (they may contain errors; use them only to find the place). The window was cut around an ESTIMATED position, so the target is usually near the middle but not always; find it by its neighbours.

Notation: a number as written (21, 236); right after it a vowel sign: + (small cross), . (dot), ρ (looped e/p-like tail), σ (small hook like a
6 that is not clearly a digit), ⊣ (u-like hook); then marks ABOVE the number: @n = ^ circumflex/hat, @s = straight horizontal bar, @l = short
slanted acute stroke, @m = wavy tilde ~, @r = small r- or v-shaped hooked mark, @2 = two dots; _ = underline; {abc} = a word in letters.
Examples: 17.@n, 24ρ, 6σ, 15+@s, 231, {y}.

Task per item: write exactly what the TARGET token is, in this notation (number, vowel sign, and any mark above it). Look closely at
the digits, the sign right after them and the space above them. If you genuinely cannot tell, write `unclear`. Be strict and literal.

Write a TSV to OUTFILE: header line `id\tread\tnote`, then one row per item in order (note: a few words). Reply only "done N items".
