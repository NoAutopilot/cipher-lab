# fr3151-seure-1558 hypotheses (rule 3: control number beside target number)

| date | job | family / instrument | control (design, N, err) | control result | target | target result | verdict |
|---|---|---|---|---|---|---|---|
| 5 Oct 2026 | D2-SEURE | nom_test, null cost -3.0 (kp/result_run6b.json) | nomenclator, 0% nulls, P 407 letters, err 0.095 / 0.242 | 2/3 / 2/3 | f81R R1, R2 | S* 0.230, 0.231 vs shuffled p95 0.246, 0.248: FAIL | negative conditional on no nulls, these reads, this H-span |
| 5 Oct 2026 | D2-SEURE | nom_test, null cost -3.0 | nomenclator, 10% nulls, err 0 / 0.095 / 0.242 | 0/3-1/3 at every level | -- | -- | null-bearing design untested |
| 6 Oct 2026 | R8-SEURE | nom_test, null cost -1.0 (kp/PREREG-R8.md, kp/result_r8.json) | nomenclator, 10% nulls, err 0 / 0.095 / 0.242 | 0/3 / 1/3 / 0/3 (S 0.23-0.27 vs null p95 0.25-0.28) | f81R R1, R2 | not run: CONTROL BELOW GATE (exit 3) | null-bearing design untested-by-this-tool (retired, rule 3 third-attempt) |
| 6 Oct 2026 | R8-SEURE | nom_test, null cost -1.0 | nomenclator, 0% nulls, err 0 / 0.095 / 0.242 | 3/3 / 3/3 / 1/3 (S 0.99 / 0.89-0.92 / 0.26-0.78) | -- | -- | lowering the null cost costs power on the no-null design at 0.242 (2/3 at -3.0) |
