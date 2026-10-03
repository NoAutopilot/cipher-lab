# zeschau-seebach-1841 hypotheses (rule 3: control number beside every target number)

| date | id | hypothesis | target | control | verdict |
|---|---|---|---|---|---|
| 3 Oct 2026 | GAPS185 T1 | R5006 uses R5005's two-digit syllabary (pair-profile cosine to R5005) | 0.886 (345 pairs, phase 1) | shuffled-digit R5006, 2,000 draws: mean 0.760, p95 0.805; power: 200/200 R5005 692-digit windows p<0.01 | PASS, p 0.0005 (PREREG-GAPS185.md) |
| 3 Oct 2026 | GAPS185 T2 | Bourdeau's 7 gloss values (grade I) over-represented in R5006 | pin coverage 0.099 | same draws: mean 0.080, p95 0.104 | not significant, p 0.106 |
| 3 Oct 2026 | GAPS202 a | seeded syllabary annealer (summed 4-gram, fr19/de19, 7 Bourdeau pins) reads pooled R5005+R5006+R5007 (2,666 tokens, K 98) | not run | matched synthetic syllabary, same N/K/pins, 1 pct error: token acc 0.070/0.027/0.000, mean 0.032 (true key -3762.7 < annealer -3459.0) | CONTROL BELOW GATE (0.60), non-test (PREREG-GAPS202.md) |
| 3 Oct 2026 | GAPS202 b | same, length-neutral objective (Addendum A) | not run | token acc 0.000 x3, mean 0.000 (true key -2347.1 < annealer about -1972) | CONTROL BELOW GATE; untested-by-this-tool at this N |
