# PREREG-W11008KP (written 8 Oct 2026 ~22:30 UTC by `date -u`, before any decode-vs-Groen diff)

Worker W11008-KP, LANE FAMILY-A2c (account 2). Question: do the Certain letters use the printed 1572 Orange-Nassau
table (`../orange-nassau-1572/key_nepveu.tsv`, letters = multiples of 3, other numbers null), the table that reads
WVO 11008's runs?

Material: WVO 5194 (KHA A 3, 895/I, 24 June 1572, image = WVO PDF 05194.pdf, 3 pages) against Groen III pp.448-449
(CCCLXIX), retroboeken OCR html of those two pages. Scope (cap 3.5): a sample of numeral runs from page 1, chosen by
position (the first cipher lines after "Mon frere Lambert Ceste servira pour vous advertir que"), not by content.
Unit = one run, i.e. a numeral stretch bounded by clear words that also appear in Groen, so the Groen span is fixed
by the two clear anchors, not by the decode.

Statistic per run: number of matching letters in an optimal global alignment (LCS) between the run decoded with
key_nepveu.tsv (nulls dropped, codes outside the key dropped) and Groen's span between the same anchors (letters only,
lower case, j->i, v->u, accents stripped). Null: the same decode under 1000 seeded keys that permute the 23 letter
values among the 23 letter codes (nulls fixed) -- a permutation changes which letters come out, so it can change the
LCS (the control can differ from the target on this statistic). Gate per run: PASS if real LCS > shuffle p95.
Overall PASS: every sampled run passes. MISS: name the runs that fail. Secondary (descriptive only, not gating):
fraction of decoded letters equal to Groen's letter at aligned position.

A MISS does not say the letter is undeciphered: Groen prints the plaintext, so the material is a known-plaintext pair
for whatever table 5194 does use (grade C for values aligned from print), not a cryptanalytic result.
