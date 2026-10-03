# hellen-frederick-1752 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

## Michell sibling key (FT4, account-4, 3 Oct 2026) -- not the same code

Hypothesis: Hellen used the Prussian chancery code Michell (London) used in 1751-52, read by the Dutch (DECODE R1050/R1051,
"Decrypted"). Key: `sibling_michell/key_sibling.tsv`, 268 codes from the period interlinear glosses (grade S). Statistic: mean
fr18 word-unigram log-prob of the decoded covered tokens (depends on values, so a value-shuffle can differ from the real key;
coverage is identical by construction and is not the statistic). Control: 200 value-shuffled keys. Positive control: key from
R1050 only on R1051's own codes; power = share of 200 subsamples, at each target's covered count, reaching p<=0.05.

| item | tokens | covered | real | shuffle mean / p95 | p | power at this N |
|---|---|---|---|---|---|---|
| R1051 positive control | 122 | 68 | -5.735 | -9.236 / -8.218 | 0.000 | -- |
| R1953 (4 Jan 1752) | 836 | 98 | -9.641 | -9.367 / -8.500 | 0.695 | 1.00 (capped at 68) |
| R1049 (7 Sept 1756) | 506 | 42 | -9.260 | -9.295 / -8.053 | 0.480 | 1.00 |
| R1045 | 367 | 35 | -8.205 | -9.352 / -8.133 | 0.060 | 1.00 |
| R1046 | 209 | 18 | -8.903 | -9.288 / -7.827 | 0.330 | 0.99 |
| R1047 | 193 | 24 | -9.254 | -9.316 / -8.028 | 0.455 | 1.00 |
| R1048 | 188 | 13 | -8.839 | -9.301 / -7.496 | 0.355 | 0.99 |
| R1060 | 134 | 11 | -8.481 | -9.361 / -7.657 | 0.245 | 0.99 |
| R1061 | 151 | 18 | -8.064 | -9.327 / -8.065 | 0.050 | 1.00 |

Result: no Hellen letter beats its shuffled control (lowest p 0.050 and 0.060 across 8 tests, none survives a multiple-test
correction), while the same statistic at the same covered counts separates the held-out Michell letter at power 0.99-1.00.
Range check (run first; ranges overlap, so the test ran): Michell's glossed codes run 2-~3600 with 37.3% of tokens above 1732
(que 2999, l' 2692); R1953's codes stop at about 1650 (1 of 836 tokens above 1732, a run-together group). The 1752 Hellen code is
a smaller code than Michell's, consistent with the negative. Also: Michell marks half-codes (40½ la, 10½ le, 120½ dans); no
Hellen transcription carries the mark. **Michell 1751-52 code is not Hellen's code** for any of the eight letters (control-backed,
conditional on DECODE's transcriptions of both). Retired as an instrument for this target: the Michell sibling key.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 2 Oct 2026 00:16 | homophonic | N=1234 K=634 restarts=8 corpus=lagazettedefran01unkngoog.txt.gz+memoiresdemonsie01torc.txt.gz+memoiresdemonsie02torc.txt.gz+mmoiresduducde01invill.txt.gz+mmoiresduducde02vill.txt.gz+mmoiresetlettre01margoog.txt.gz profile=target | 1-3 | 0.100 (0.090-0.113) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | HEL-T2 2 Oct 2026 (account-4): spec test 2, pooled 1763 cluster, matched control before target |
| 2 Oct 2026 00:23 | nomenclator | N=1234 K=634 restarts=3 corpus=lagazettedefran01unkngoog.txt.gz+memoiresdemonsie01torc.txt.gz+memoiresdemonsie02torc.txt.gz+mmoiresduducde01invill.txt.gz+mmoiresduducde02vill.txt.gz+mmoiresetlettre01margoog.txt.gz sweeps=30,phase1=20 | 1 | 0.092 (0.092-0.092) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | HEL-T2 2 Oct 2026 (account-4): spec test 2 next instrument after homophonic non-test, ARM-C1 settings, seed 1 timing run |
| 2 Oct 2026 00:30 | nomenclator | N=1234 K=634 restarts=3 corpus=lagazettedefran01unkngoog.txt.gz+memoiresdemonsie01torc.txt.gz+memoiresdemonsie02torc.txt.gz+mmoiresduducde01invill.txt.gz+mmoiresduducde02vill.txt.gz+mmoiresetlettre01margoog.txt.gz sweeps=30,phase1=20 | 2 | 0.109 (0.109-0.109) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | HEL-T2 2 Oct 2026 (account-4): spec test 2 next instrument after homophonic non-test, ARM-C1 settings, seed 2 |
