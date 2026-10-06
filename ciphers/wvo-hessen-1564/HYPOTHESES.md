# HYPOTHESES -- wvo-hessen-1564

| date | hypothesis | instrument | control | target | verdict | by |
|---|---|---|---|---|---|---|
| 6 Oct 2026 | f.23 (WVO 1109, 1564) gloss key shares sign->letter values with the 1069 key (Hesse to Orange, 1563) | blind text-only shape concordance (Sonnet, letter-stripped descriptions) + same-letter count, `wvo-hessen-1564/r9wvox/score.py` | letter labels permuted within each key, 10000 draws: mean 0.90, p95 3, max 7 | 8 of 18 scored pairs same letter (p < 0.0001) | PASS (prereg PREREG-R9-WVOX.md) | R9-WVOX |
| 6 Oct 2026 | f.23 gloss key shares sign->letter values with the 174 key leaf alphabet (1567) | same | same: mean 0.33, p95 1, max 4 | 0 of 7 scored pairs same letter (p = 1.0) | FAIL | R9-WVOX |
| 6 Oct 2026 | 1069 key shares values with the 174 key leaf alphabet (reported, same gate) | same | same: mean 0.54, p95 2, max 5 | 4 of 17 same letter (a=X, b=triangle, c=barred h, z=small circle; p = 0.0015) | PASS (partial overlap: 13 of 17 matched shapes differ) | R9-WVOX |
| 6 Oct 2026 | f.23 German rows are a letter-over-sign decipherment of the cipher rows (re-run on a careful two-pass gloss) | `tools/interlinear_align.py align --shuffle 1000 --seed 1564`, PREREG-R9-WVOALIGN parameters, gloss `r10tx/gloss_r10.tsv` | row-derangement shuffle: piles mean 1.39, p95 3, max 5; pass A mean 2.43, p95 5; pass B mean 1.35, p95 3 | piles 17 (R9 sketch 10), pass A 15 (7), pass B 13 (11); p = 0.001 each | PASS (prereg PREREG-R10-WVOTX.md) | R10-WVOTX |
