# HYPOTHESES -- willem-van-hessen-1567

| date | hypothesis | instrument | control | target | verdict | by |
|---|---|---|---|---|---|---|
| 6 Oct 2026 | f.23 (WVO 1109, 1564) gloss key shares sign->letter values with the 1069 key (Hesse to Orange, 1563) | blind text-only shape concordance (Sonnet, letter-stripped descriptions) + same-letter count, `wvo-hessen-1564/r9wvox/score.py` | letter labels permuted within each key, 10000 draws: mean 0.90, p95 3, max 7 | 8 of 18 scored pairs same letter (p < 0.0001) | PASS (prereg PREREG-R9-WVOX.md) | R9-WVOX |
| 6 Oct 2026 | f.23 gloss key shares sign->letter values with the 174 key leaf alphabet (1567) | same | same: mean 0.33, p95 1, max 4 | 0 of 7 scored pairs same letter (p = 1.0) | FAIL | R9-WVOX |
| 6 Oct 2026 | 1069 key shares values with the 174 key leaf alphabet (reported, same gate) | same | same: mean 0.54, p95 2, max 5 | 4 of 17 same letter (a=X, b=triangle, c=barred h, z=small circle; p = 0.0015) | PASS (partial overlap: 13 of 17 matched shapes differ) | R9-WVOX |
| 9 Oct 2026 | key_1068 (WVO 1068 period gloss) shares sign->letter values with key_1069 | blind Sonnet shape concordance + w1068/concord_1068.py | letters permuted within each key, 10000 draws: mean 0.73, p95 2, max 6 | 10 of 17 scored pairs same letter (p < 0.0001) | PASS (shared core; 7 of 17 matched shapes differ, four on 1069 o/NULL shapes, one of them -- seven -- glossed o in both) | WVO-1068-KEY |
| 9 Oct 2026 | key_1068 shares sign->letter values with the f.23 (WVO 1109) gloss key | same | same: mean 1.13, p95 3, max 7 | 13 of 20 same letter (p < 0.0001) | PASS (7 of 20 differ) | WVO-1068-KEY |
