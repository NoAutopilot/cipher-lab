# HYPOTHESES fr15575-syllabic-1592-95

| date | job | hypothesis | instrument | control (both numbers) | target | verdict |
|---|---|---|---|---|---|---|
| 13 Oct 2026 | SYL54-TRY | no.54 legend caret ^ = s (f.228 `^` tokens, n 13) | decode_key.py --try, es1600, W 8, 100 nulls (PREREG-SYL54-TRY.md) | hidden 23/24/73 true values accepted 0/3 (gate 2/3: FAIL); wrong values not accepted 3/3 | accept, 65.1 bits over R (null p95 8.4 / -93.1) | non-test at this N (control failed, syllable class); lead, M |
| 13 Oct 2026 | SYL54-TRY | ^ = l | same | same | reject, -225.9 | non-test |
| 13 Oct 2026 | SYL54-TRY | n = en (dotted-n mark) | same | same | reject, -83.0 | non-test |
| 13 Oct 2026 | SYL54-TRY | n = l | same | same | reject, -133.7 | non-test |
| 13 Oct 2026 | SYL54-TRY | n = e (key header value) | same | same | reject, -50.1 | non-test |
| 13 Oct 2026 | SYL54-TRY | + = e | same | same | undecided, n 1 | untestable at n 1 |
| 13 Oct 2026 | SYL54-TRY | 16 marked nomenclator rows as code + modifier | - | - | n 0 in f.228 L01-L08 | untestable at this N |
| 13 Oct 2026 | SYL-1LC | no.54 legend caret ^ = s vs l; dotted n = en vs l (f.228 L01-L08, env E = syllabary + H header letters) | decode_key.py --try, es1600, W 8, 100 nulls (PREREG-SYL-1LC.md, syl1lc_try.sh) | single-letter control: masked `:`=r (n 13), `y`=r (n 6), `9`=y (n 4) true values accepted 0/3 (gate 2/3 with `:` required: FAIL; `:`=r +29.5 bits over NULL, above both p95s, rejected by the breakage rule, 5/13 occurrences lose >3 bits); wrong l/s/e not accepted 3/3 | not run (control below gate) | non-test at this N; targets not scored; second --try control class failed on this text (syllable 0/3 SYL54-TRY, single letter 0/3 here) |
