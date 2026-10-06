# rah-juan-manuel-1521 -- hypothesis rows (append-only; CONTROL and TARGET side by side, CLAUDE.md rule 3)

Earlier tests are in NOTES.md (test1, test42, test147, test147b, decode9501); this file starts with R14-RJMTQ.

| date | job | hypothesis | statistic | target | control (mean / p95 / max) | gate | verdict |
|---|---|---|---|---|---|---|---|
| 6 Oct 2026 | R14-RJMTQ | T has one value (free), held-out pool f.199+f.40+f.147b | top chunk share | e 4/42 = 0.095 (top on 1 page) | 0.106 / 0.143 / 0.214 | witness/PREREG_tq.md | FAIL |
| 6 Oct 2026 | R14-RJMTQ | T = s (Tomokiyo) | share chunk = s | 1/42 = 0.024 | 0.067 / 0.119 / 0.190 | same | FAIL |
| 6 Oct 2026 | R14-RJMTQ | T = d (alphabet.tsv, M) | share chunk = d | 1/42 = 0.024 | 0.010 / 0.048 / 0.071 | same | FAIL |
| 6 Oct 2026 | R14-RJMTQ | Q has one value (free), all 4 pages | top chunk share | y 4/13 = 0.308 (top on 1 page, f.40) | 0.142 / 0.231 / 0.385 | same | FAIL (pages rule) |
| 6 Oct 2026 | R14-RJMTQ | Q = y (K's value) | share chunk = y | 4/13 = 0.308 (1 page) | 0.053 / 0.154 / 0.308 | same | FAIL (pages rule) |
