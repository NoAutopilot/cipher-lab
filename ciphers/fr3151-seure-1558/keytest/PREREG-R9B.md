# PREREG-R9B: Bourdeau's La Guiche 1551 key vs the reconciled f81R reads (R9-SEURE2, 6 Oct 2026, written 06:5x UTC by date -u, before any score)

Key: `guiche_key.tsv` (Bourdeau's recovered key, credit D. Bourdeau, cyphersolver `targets/guiche1551/`, CC BY 4.0), own text
`guiche_ct.txt` (his transcription, copied unmodified with credit header; struck lines L0-L1 included, the one ':' sign dropped).
Design note before scoring: La Guiche is a 22-sign simple substitution with no numerals; Seure's reconciled f81R read has 93 labels
and numeral word codes (12 in R1). The La Guiche key cannot be Seure's key as a whole; the test asks only whether shared shapes carry
La Guiche's values.

## Fixed label map (Seure reader-A label -> La Guiche code), from label names/shape descriptions and one look at Gallica
## btv1b90601662 f65 and images/kp/f81R_L03_s1.jpg; not tuned after scoring.
| Seure | LG code | value |
|---|---|---|
| # | # | i |
| #/ | X (double-barred #) | g |
| 3 | 3 | e |
| 4 | 4 | o |
| oo (lying figure-eight) | 8 (infinity) | p |
| + | + | b |
| t, t/ | t (barred cross) | r |
| ff, ff/ | F | q |
| f, f/ | f | d |
| p | p | c |
| W | W (III) | l |
| P | P (phi) | y |
| A, A/ | A (circled) | v |
| e/ | e (theta) | u |
| d | d | n |
| g | g | f |
| r | r (hook) | a |
Every other label is a gap.

## Statistic (coverage-free; R9-SEURE's lesson)
U = mean log10 P(letter) over every mapped sign of the read, P from `tools/data/fr16` letter unigrams (a-z, j->i, v->u, w->u,
add-0.5). Null: shuffled key = permute the value column across the 17 mapped LG codes (same positions, same coverage), 1000 draws.
U depends on which value sits at which sign, so the null CAN differ from the target (rule 3 orthogonality).

## Power control, run first
La Guiche's own text (all L rows of `guiche_ct.txt`, ':' dropped, about 430 signs), true key restricted to the same 17 codes (others
gaps), injected sign error 0 / 0.095 / 0.242 (a token replaced by a random other LG code), 3 seeds each, each vs its own 1000-draw
shuffled-key null. Power condition: U > own null p95 in >= 2/3 seeds at 0.095 AND at 0.242. If it fails: NON-TEST, the target is not
scored, stop. Caveat registered: this control is design-matched to La Guiche (simple substitution), not to Seure (homophonic +
codes); it measures the statistic's power for this key, not Seure's design.

## Target gate
R1 and R2 (`kp/f81R_recon_R1.tsv`, `_R2.tsv`): pass if U > own shuffled-key p95. Both fail: a negative for the La Guiche key under this
one map only. A pass licenses only "worth a blind second shape map and a trigram look", no reading, no grades.
