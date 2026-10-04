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

## R4369 Hellen key (READ2-HEL, account 2, 3 Oct 2026) -- reads R1953 above every control

Hypothesis: DECODE R4369 (BL Add MS 32276 f.44, "Hellen avec le Roy de Prusse", 1751, English Deciphering Branch) is the key of
R1953. Key: `key_r4369/key.tsv` (2 blind passes + reconciliation, err_2reader 4.8%, codes 801-1796); keys per attribution of the
sheet's right-hand entries from `key_r4369/build_keys.py`. Script: `sibling_michell/test_sibling.py --key K --out F` (outputs
`key_r4369/test_key_*.txt`). Statistics: uni = mean fr18 word log-prob of covered tokens (order-blind); bi = mean fr18 junction-pair
PMI over adjacent covered tokens (order-sensitive). Controls x200: value-shuffled key (uni, bi); token-order shuffle (bi only -- uni
cannot move under it); positive control power from fr18 prose encoded with the same key at the target's covered/pair count.

| key on R1953 | covered | uni real | uni shuffle mean / p95 | uni p | pairs | bi real | bi val-shuffle mean | bi val p | bi order-shuffle mean / p95 | bi order p | power uni / bi |
|---|---|---|---|---|---|---|---|---|---|---|---|
| L (left entries) | 359 | -8.985 | -9.750 / -9.229 | 0.005 | 148 | -0.756 | -0.880 | 0.025 | -0.858 / -0.758 | 0.040 | 1.00 / 1.00 |
| R0 (right entry = own row) | 195 | -8.891 | -8.604 / -8.046 | 0.805 | 44 | -0.896 | -0.875 | 0.545 | -0.846 / -0.656 | 0.645 | 1.00 / 1.00 |
| R100 (right entry = row +100) | 315 | -6.930 | -8.578 / -8.185 | 0.000 | 125 | -0.455 | -0.865 | 0.000 | -0.656 / -0.541 | 0.010 | 1.00 / 1.00 |
| L where R100 absent | 155 | -7.193 | -9.667 / -8.958 | 0.000 | 26 | -0.212 | -0.867 | 0.000 | -0.762 / -0.544 | 0.000 | 1.00 / 1.00 |
| L where R100 present | 204 | -10.346 | -9.949 / -9.418 | 0.855 | 48 | -0.836 | -0.889 | 0.285 | -0.899 / -0.755 | 0.220 | 1.00 / 1.00 |
| LR100 (seed 1) | 470 | -7.017 | -9.157 / -8.755 | 0.000 | 266 | -0.361 | -0.877 | 0.000 | -0.694 / -0.609 | 0.000 | 1.00 / 1.00 |
| LR100 (seed 2) | 470 | -7.017 | -9.181 / -8.809 | 0.000 | 266 | -0.361 | -0.871 | 0.000 | -0.688 / -0.596 | 0.000 | 1.00 / 1.00 |

Secondary rows (other seven letters, same script, files above): no letter beats its controls under L, R0, R100 or LR100 (uni p
0.155-0.98, coverage 7-34%; lowest bigram p R1046 order 0.025 on 34 tokens with uni p 0.94, not surviving correction) -- R4369 is not their key. Result: **LR100 reads R1953 above every control**; R100 attribution chosen by the test,
so those values are grade S. Decode H 152 / S 304 / M 16 / U 374 (codes 1-800 absent from the sheet); judge FAIL -0.976 vs real_p05
-0.954 (null_p99 -1.741), with a calibration on true decodes at this coverage failing 2/8 at -0.972/-0.980 -- judge cannot decide.

## R4370 as codes 1-800 of the Hellen key (READ2-HEL2, account 2, 3 Oct 2026) -- fails at power 1.00, pre-registered k=4

Pre-registration: key_r4370/PREREG.md (f275f41d, before any look). Pass = uni value-shuffle p and bi order-shuffle p both <= 0.0125, power >= 0.8.
Keys restricted to codes 1-800 (R1953: 349 numeric tokens there). Script: sibling_michell/test_sibling.py --key, seed 1, 200 shuffles each.

| R4370 key on R1953 | covered | uni real | uni shuffle mean / p95 | uni p | pairs | bi real | bi val-shuffle mean | bi val p | bi order-shuffle mean / p95 | bi order p | power uni / bi |
|---|---|---|---|---|---|---|---|---|---|---|---|
| L | 191 | -9.283 | -9.383 / -8.758 | 0.370 | 48 | -1.047 | -0.809 | 0.985 | -0.837 / -0.648 | 0.985 | 1.00 / 1.00 |
| R0 | 158 | -10.106 | -10.225 / -9.566 | 0.350 | 28 | -0.817 | -0.811 | 0.510 | -0.797 / -0.615 | 0.535 | 1.00 / 1.00 |
| R100 | 145 | -10.719 | -10.143 / -9.552 | 0.935 | 29 | -0.830 | -0.822 | 0.550 | -0.831 / -0.628 | 0.505 | 1.00 / 1.00 |
| LR100 | 243 | -10.036 | -9.664 / -9.221 | 0.875 | 79 | -0.908 | -0.813 | 0.840 | -0.888 / -0.769 | 0.595 | 1.00 / 1.00 |
| full 1-1000 (rival, outside k) | 341 | -10.259 | -9.849 / -9.518 | 0.950 | 146 | -0.905 | -0.807 | 0.915 | -0.867 / -0.780 | 0.825 | 1.00 / 1.00 |

Secondary rows: no other letter clears 0.0125 on both statistics under any R4370 key. Result: **fail** on every attribution (target vs
control above); R4370's 801-1000 shares 70 codes with R4369, 0 with the same meaning (rival series). R4369's row above stands.


## NEAR3-HEL4 (4 Oct 2026): R4372 (f.48) as codes 1-800 on R1953
Pre-registration: key_r4372/PREREG.md (453a570a, before the images were fetched). Pass = uni value-shuffle p and bi order-shuffle p both <= 0.0125, power >= 0.8.
Keys restricted to codes 1-800. Script: sibling_michell/test_sibling.py --key, seed 1, 200 shuffles each.

| R4372 key on R1953 | covered | uni real | uni shuffle mean / p95 | uni p | pairs | bi real | bi val-shuffle mean | bi val p | bi order-shuffle mean / p95 | bi order p | power uni / bi | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L | 147 | -10.164 | -10.038 / -9.331 | 0.625 | 19 | -0.444 | -0.787 | 0.050 | -0.698 / -0.443 | 0.055 | 1.00 / 1.00 | fail |
| R0 | 63 | -10.512 | -10.263 / -9.444 | 0.670 | 4 | -0.602 | -0.857 | 0.300 | -0.800 / -0.301 | 0.278 | 1.00 / 0.97 | fail |
| R100 | 69 | -9.825 | -10.323 / -9.590 | 0.165 | 5 | -0.963 | -0.829 | 0.820 | -0.948 / -0.332 | 0.410 | 1.00 / 0.98 | fail |
| LR100 | 191 | -10.035 | -10.137 / -9.628 | 0.375 | 42 | -0.525 | -0.796 | 0.025 | -0.784 / -0.626 | 0.010 | 1.00 / 1.00 | fail (bi passes, uni does not) |
| LR100 seed 2 | 191 | -10.035 | -10.196 / -9.677 | 0.295 | 42 | -0.525 | -0.794 | 0.010 | -0.786 / -0.626 | 0.000 | 1.00 / 1.00 | fail |
| full 1-1000 (rival, outside k) | 195 | -10.041 | -10.234 / -9.682 | 0.290 | 45 | -0.570 | -0.795 | 0.050 | -0.810 / -0.680 | 0.000 | 1.00 / 1.00 | fail |

Combined (PREREG item 6, reported not gated -- R4369's half passes alone, so this control cannot fail differently):
comb_L uni -7.767 vs -9.439, comb_R0 -7.430 vs -9.376, comb_R100 -7.376 vs -9.370, comb_LR100 -7.889 vs -9.516 (all p 0.000, bi order p 0.000);
R4369 LR100 alone -7.017. Adding any R4372 half lowers the uni real by 0.36-0.87: the 1-800 half reads worse than the 801+ half.
Secondary rows (not gated): R1049 (1756) LR100 uni p 0.010 with bi order p 0.310, full uni p 0.005 / bi 0.205 -- one statistic only, 35 secondary tests; nothing else under 0.0125.
Result: **fail** on every attribution. Unlike R4370 (bi order p 0.595), R4372 LR100's bigram statistic sits at or under the gate on both seeds.

## N4-HEL6 (4 Oct 2026, account 2, for LANE-NEAR4): diagnosis of R4372 LR100's bigram-only signal (PREREG key_r4372/PREREG_diag.md, f5dd973f)
Script key_r4372/diag.py (seeds 1, 2; `--check`), output diag_output.txt / diag_output_seed2.txt; not pre-registered follow-up diag_oov.py.

| test | target | control | p | power | verdict |
|---|---|---|---|---|---|
| Part A: pairs carrying bi excess (42 pairs) | k* = 1: dropping "mon peuple" (414-422, pmi 3.24) raises bi order p 0.005 -> 0.030 | order shuffle mean -0.797 | -- | -- | artefact rule (k*<=3, one tag m1-m4 on all) did not fire: the pair carries no tag |
| Part B: junctions with R4369 H/S neighbours (93 codes, 139 tokens, J=186) seed 1 | S_B -0.794 | (i) R4372 permuted mean -0.814 / p99 -0.658; (ii) R4370 size-matched mean -0.794 / p99 -0.636 | 0.310 / 0.460 | 1.00 (R4369 held-out, J=186) | **FAIL** |
| Part B seed 2 | -0.794 | (i) -0.817 / -0.679; (ii) -0.787 / -0.611 | 0.310 / 0.555 | 1.00 | **FAIL** |
| not pre-registered: OOV pairs set to the floor | -1.012 | order shuffle -1.101 | 0.115 (seed 2 0.105) | -- | signal gone; with "mon peuple" also dropped p 0.505 |

Result: control-backed negative for R4372 as codes 1-800 on the context test; the bigram signal is one high-PMI pair plus the share of
pairs whose left word is outside fr18 (pmi() returns 0 there, above the -1.204 floor): 40.5% in the real order vs 25.2% under shuffle.
