# f.128r sign-by-sign transcription (A2-DIN, 3 Oct 2026)

Leaf: BnF fr.3621 f.128r (no.114, Dinteville to Nevers, Langres 1 July 1592, "avec chiffre et dechiffrement"),
Gallica btv1b52524472n canvas f265, region 200,1800,3700,560 (crops in ../images/, made with tools/iiif_lines.py).

- pass_instructions.md: the brief both blind passes got (sign labels).
- passA.tsv, passB.tsv: two blind Sonnet passes on the 8 line-segment crops (raw, not edited).
- gloss_pairs.tsv: reconciliation (Opus, from 1.6x zoom sub-crops in ../images/zoom/): per cipher line, the gloss
  as written above it and the cipher signs in order. Committed before any alignment.
- align_f128.py: gloss_pairs.tsv -> pairs.tsv, align.tsv, key.tsv, control.tsv (tools/interlinear_align.py,
  --code-prefix mode); `--check` exits 1 if outputs are stale.

Extra sign labels beyond pass_instructions.md: D = triangle with flag (Δ), r = r-like sign with a curl (ꝶ),
al = alpha (α, distinct from plain a), zh = bare ʒ (distinct from 3 and from m = ɱ), h = h-like sign (ɧ),
B = barred B-like sign, n = n shape, div = ÷, plus = a + written in the cipher row.
