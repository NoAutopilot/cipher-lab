# bMAT1F blind transcription pass (one leaf, one pass)

You are transcribing a 1586 French cipher (BnF fr.15572, Mayenne to Henri III) from native-resolution line crops.
Signs are a nomenclator of letter-like figures, digits, and a few special marks. You must use the SAME label set
as the reference sheet below.

REFERENCE (label chart): `ciphers/matignon-mayenne-1586/align1f/reference_f78v_l1-5.tsv` gives lines 1-5 of the
same hand, sign by sign, with their crops `ciphers/matignon-mayenne-1586/images/f78v_79r/ref/f78v_ref_line{1..5}_s{1,2}.jpg`
(s1 = left segment, s2 = right segment; the two overlap by about 150 px, do not count the overlap twice).
Study it first: learn what each label looks like (e.g. `.v.` = v between two dots, `D2` = triangle, `BOX2` = small
square, `oo` = infinity-like loop, `Ze` = Z-like sign, `w-` = barred w, `4+` = crossed 4, `ff` = double-f form,
`T` vs `t`, `he`, `lam`, `U` = the x/cross-like sign;
digits as digits, multi-digit codes as one token e.g. `13`, `14`, `24`, `26`, `99`, `100`).
If a sign matches no label in the chart, write `?{short description}` (e.g. `?hooked-s`). Never guess from context:
you do not know the plaintext and must not try to read French.

TARGET: transcribe ONLY the line whose body sits in the vertical middle of each crop (neighbour lines are clipped
at top/bottom; ignore them). Ignore clear-text French words (e.g. margin words at the far left like "Mau", "gem" if
they are ordinary script, or the prose after the cipher). Crops for each line come as s1 (left) and s2 (right)
with ~150 px overlap: join them without duplicating the overlapping signs.

OUTPUT: write a TSV file (path given below) with header `line\ttokens\tuncertain` and one row per line:
line id, the space-separated tokens, and a comma-separated list of 1-based token positions you are unsure of.
Write the file after each line (append), so partial work survives. Reply with just the file path and line count.
