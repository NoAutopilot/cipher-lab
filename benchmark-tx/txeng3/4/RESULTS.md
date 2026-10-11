# TXE3-4 CALIB: does two-reader disagreement predict true transcription error? (11 Oct 2026)

Worker TXE3-4 (account 3, Fable, session_01U7rBmn7MS5LJn9JMzfoFgP) for the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M).
PREREG benchmark-tx/PREREG-txeng3-4.md (pushed 05:53 UTC before any score). Run 05:5x-06:0x UTC 11 Oct 2026 by `date -u`.
Committed outputs and committed truth only: 0 model passes, 0 subagent calls, 0 network requests. No confirm item scored
(spinelli, vivonne f.103r confirm2/-w untouched); no oracle page opened; no truth file edited. Script
`benchmark-tx/txeng3/4/calib.py` (imports tools/tx_bench.py and tools/reconcile_passes.py); tables `calib_pairs.tsv` (22 pass
pairs), `calib_leaves.tsv` (13 primary leaves, one pair each), `calib_lines.tsv` (per-line sums behind the bootstrap),
`calib_fit.json`, console `calib_run.txt`. Seed 20261011, 1,000 resamples/permutations.

## Verdict: NULL. The gate is not met; no estimator goes into tx_bench.

err_2reader does not predict err_true across the 13 benchmark leaves. Spearman rho 0.11 (shuffled-label control: permutation
p 0.39, control q95 0.48); the leave-one-leaf-out ratio predictor (MAE 0.090) is WORSE than the constant mean (0.087); the
per-leaf ratio err_true/err_2reader runs 0.14 to 5.39 (q10-q90 0.23-2.57, a factor of 11 against the registered factor of 3).
The eval leaves fall "inside" the dev-fitted band (4/4) only because that band is 0.14x-5.4x, which is no prediction.
The data are not too few to say this: they are enough to show that the quantity agreement cannot see -- the agreed-wrong
rate -- varies from 0 to 16% of signs between hands, and that is what breaks the mapping (section 4).

## 1. Per leaf (primary pair; err_true = tools/tx_bench.py default scorer, 0.75-indel alignment, as measured | flagged excluded)

err_2reader = 1 - agreeing columns / alignment columns, Needleman-Wunsch (`reconcile_passes.py nw`), over the item's lines
(every sign on them, as an unread letter would give it); err_2reader(scored) = share of scored truth positions where the two
passes' aligned signs differ. Single = mean of pass A and pass B. Wilson 95% in calib_pairs.tsv.

| leaf | split | readers | scored | err_2reader | err_2reader (scored) | pass A | pass B | single meas / flag | recon meas / flag | ratio single | ratio recon | hidden share single / recon |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| no87 | eval | Sonnet | 803 | 0.088 | 0.072 | 0.066 | 0.097 | 0.082 / 0.069 | 0.051 / 0.038 | 0.927 | 0.58 | 0.516 / 0.634 |
| f152r | eval | Opus | 73 | 0.062 | 0.041 | 0.082 | 0.069 | 0.075 / 0.043 | 0.069 / 0.029 | 1.205 | 1.096 | 0.667 / 0.75 |
| bir1591 | eval | Opus | 203 | 0.194 | 0.074 | 0.084 | 0.103 | 0.094 / 0.019 | 0.079 / 0.000 | 0.483 | 0.406 | 0.474 / 0.562 |
| gunther | eval | Opus | 317 | 0.027 | 0.025 | 0.051 | 0.054 | 0.052 / 0.020 | 0.047 / 0.016 | 1.951 | 1.772 | 0.645 / 0.667 |
| f36v | dev | Sonnet | 16 | 0.316 | 0.375 | 0.312 | 0.375 | 0.344 / 0.344 | 0.438 / 0.438 | 1.089 | 1.385 | 0.182 / 0.143 |
| f21v | dev | Sonnet | 189 | 0.150 | 0.116 | 0.048 | 0.053 | 0.050 / 0.050 | -- / -- | 0.336 | -- | 0.105 / -- |
| f87 | dev | Sonnet | 139 | 0.281 | 0.086 | 0.043 | 0.130 | 0.086 / 0.086 | -- / -- | 0.307 | -- | 0.0 / -- |
| dint128 | dev | Sonnet | 85 | 0.136 | 0.141 | 0.353 | 0.306 | 0.329 / 0.329 | 0.377 / 0.377 | 2.42 | 2.766 | 0.545 / 0.5 |
| dint98v | dev | Opus | 53 | 0.165 | 0.019 | 0.057 | 0.019 | 0.038 / 0.038 | 0.000 / 0.000 | 0.228 | 0.0 | 0.0 / -- |
| dint113 | dev | Opus | 81 | 0.129 | 0.037 | 0.012 | 0.025 | 0.018 / 0.000 | 0.000 / 0.000 | 0.143 | 0.0 | 0.0 / -- |
| dint89 | dev | Opus | 240 | 0.109 | 0.075 | 0.079 | 0.121 | 0.100 / 0.098 | 0.042 / 0.015 | 0.916 | 0.382 | 0.457 / 0.8 |
| luzerne | dev | Sonnet | 64 | 0.017 | 0.000 | 0.094 | 0.094 | 0.094 / 0.000 | 0.094 / 0.000 | 5.391 | 5.388 | 1.0 / 1.0 |
| viv102r | dev | Sonnet | 1234 | 0.081 | 0.065 | 0.194 | 0.225 | 0.209 / 0.021 | -- / -- | 2.569 | -- | 0.779 / -- |

Reproduction check: pass A/B figures match the ones on file (no.87 0.066/0.097, bir1591 0.084/0.103, dint-f89 0.079/0.121,
dint-f128 0.353/0.306, luzerne 0.094/0.094, Vivonne f.102r on the dev truth 0.330/0.353); f152r pass B reads 0.069 (5/73) here
against 0.082 (6/73) in txeng2/f152r/RESULTS.md; `tools/tx_bench.py` gives 0.069 with both the default and the `--legacy`
scorer against the current truth file, so the one-sign difference lies in the truth file's later revision (it now carries one TXV-152
`corrected` row and the flag column, written after that RESULTS; passZ moves 0.082 -> 0.069 the same way), not in this script.
"hidden share" = of a pass's errors at scored positions, the share where the OTHER pass reads the same (wrong) sign or also
misses it: the error no agreement check can see. f21v/f87: truth = S tokens of the committed decode, which IS these two
passes' reconciliation, so an agreed-wrong sign is excluded from the truth by construction (hidden 0.0-0.1 there is an
artefact, not a property of the hand). dint-f98v/f113/f89 and bir1591: truth aligned to passZ (from these passes), scored only
where the alignment agrees -- the same bias, weaker; their key_print / jackknife truth variants read 0.15-0.53 for the same
passes (section 6). Flagged-excluded figures drop sharply on viv102r (0.209 -> 0.021), luzerne (0.094 -> 0.000), bir1591
(0.094 -> 0.019): the verifier flags sit where the readers agree against the truth, so "flagged excluded" removes much of
the agreed-wrong error along with the doubtful truth. Never quoted alone.

## 2. Secondary pairs (same leaves; the cluster bootstrap over leaves covers them)

| leaf | pair | readers | lines | err_2reader | single meas | recon meas | ratio single | hidden share single | agreed-wrong rate | visible errors per disagreement |
|---|---|---|---|---|---|---|---|---|---|---|
| no87 | X21opus | Opus | 12 | 0.034 | 0.045 | 0.055 | 1.329 | 0.733 | 0.032 | 0.4 |
| f36v | X21bsonnet | Sonnet | 1 | 0.238 | 0.312 | 0.375 | 1.312 | 0.8 | 0.250 | 0.5 |
| f36v | X21bopus | Opus | 1 | 0.095 | 0.156 | 0.188 | 1.641 | 0.8 | 0.125 | 0.5 |
| f87 | X21opus | Opus | 5 | 0.195 | 0.147 | 0.187 | 0.756 | 0.595 | 0.079 | 0.469 |
| dint128 | X21opus | Opus | 4 | 0.145 | 0.377 | 0.447 | 2.595 | 0.706 | 0.212 | 0.75 |
| dint128 | X21bopus | Opus | 4 | 0.095 | 0.294 | 0.329 | 3.089 | 0.683 | 0.165 | 0.812 |
| viv102r | sv | Opus | 36 | 0.102 | 0.241 | 0.246 | 2.358 | 0.802 | 0.179 | 0.757 |
| viv102r | tl | Opus | 36 | 0.094 | 0.269 | 0.272 | 2.851 | 0.829 | 0.195 | 0.739 |
| viv102r | dv1 | Opus | 36 | 0.139 | 0.273 | 0.276 | 1.965 | 0.708 | 0.174 | 0.702 |

All 22 pairs: Spearman rho 0.27, leaf-cluster bootstrap 95% -0.16 to 0.60 (covers 0).
By reader model (ratio single, all pairs): Sonnet n=8 median 1.20 (0.31-5.39); Opus n=14 median 1.48 (0.14-3.09).
By hand (ratio single, all pairs): Birago 1572 clerk n=3 0.93-1.33; Dinteville 1591 n=1 0.48-0.48; Oranje secretary 1561 n=1 1.95-1.95; Ceppo-Nevers n=6 0.31-1.64; Dinteville office n=6 0.14-3.09; La Luzerne digits 1781 n=1 5.39-5.39; Vivonne clerk 1573 n=4 1.97-2.85.
Within one hand the ratio is stable-ish (Vivonne 4 pairs 1.97-2.85, dint-f128 3 pairs 2.42-3.09, Birago 1572 clerk 0.93-1.33);
between hands it is not. A per-hand calibration would need a known-answer leaf of that hand -- which is err_true itself.

## 3. Fits, bootstraps, control (primary leaves, N=13; recon N=10)

| endpoint | k = median ratio (line-boot 95% / leaf-boot 95%) | LS k | OLS | per-leaf ratio min-max (q10-q90) | Spearman (line-boot 95%) | perm p (control q95) | LOO MAE ratio / OLS / const | perm p (LOO) | predictive 95% ratio (new leaf) |
|---|---|---|---|---|---|---|---|---|---|
| single (as measured) | 0.927 (0.71-1.09 / 0.34-1.95) | 0.766 | y = 0.061 + 0.446 x | 0.14-5.39 (0.23-2.57) | 0.110 (-0.07-0.42) | 0.389 (0.48) | 0.0900 / 0.0924 / 0.0866 | 0.321 | 0.14-5.39 |
| recon (as measured) | 0.838 (0.48-1.06 / 0.38-2.08) | 0.984 | y = -0.009 + 1.037 x | 0.00-5.39 (0.00-2.77) | 0.164 (-0.05-0.42) | 0.336 (0.53) | 0.1279 / 0.1324 / 0.1278 | 0.761 | 0.00-5.39 |
| single (flagged excluded, beside) | 0.336 (0.27-0.58 / 0.23-0.78) | 0.652 | y = -0.008 + 0.692 x | 0.00-2.42 (0.00-1.09) | 0.468 (0.18-0.63) | 0.040 (0.43) | 0.0746 / 0.0829 / 0.0857 | 0.255 | 0.00-2.42 |

Control: the shuffled-label permutation (x values re-paired with other leaves' y) can and does vary on both statistics
(rho spread about 0 +- 0.48 at q95; LOO MAE spread), so it is a real control, not an identical-by-construction one. The observed
rho (0.11) sits inside the permuted distribution; the observed LOO MAE is beaten by 32% of permutations.
Tune on dev, report on eval: dev-only (9 leaves) median ratio 0.916, dev ratios 1.09, 0.34, 0.31, 2.42, 0.23, 0.14, 0.92, 5.39, 2.57; dev LOO MAE ratio
0.1320 vs const 0.1148 (ratio worse). Eval leaves against the dev-only predictive band (= x times the dev ratio
distribution, 2.5-97.5%): no87 x 0.088 true 0.082 pred 0.081 band 0.013-0.474 IN; f152r x 0.062 true 0.075 pred 0.057 band 0.009-0.337 IN; bir1591 x 0.194 true 0.094 pred 0.178 band 0.028-1.045 IN; gunther x 0.027 true 0.052 pred 0.024 band 0.004-0.144 IN.
4/4 inside a band that spans a factor of 38 is not a pass of anything; gate 3 is formally met and means nothing here.
Sensitivity without the two S-token leaves (f21v, f87, whose truth is these passes' own reconciliation): N=11, median ratio
1.089, Spearman 0.22, LOO MAE ratio 0.0813 vs const 0.0982 -- a small LOO gain, rho still at chance.
Flagged-excluded (beside, not the registered endpoint): rho 0.47, permutation p 0.040 -- one marginal p on 13 leaves after
removing the truth-doubtful positions, with a ratio spread 0.00-2.42 (q10 0.00: four leaves read 0 errors), so even if real it
licenses only "err_true is somewhere between 0 and 2.4 times err_2reader". Not a pass of gate 4, not adopted.

Gate (PREREG): g1 permutation p < 0.05: False (p 0.389); g2 LOO ratio beats const: False (0.0900 vs 0.0866);
g3 eval inside: 4/4; g4 q90/q10 spread factor 11.3 (gate 3). **holds = False.** No --estimate-from-2reader option is added.

## 4. Why it fails: the error agreement cannot see

Position-level identity per leaf: single-pass position error = agreed-wrong rate + (visible errors per disagreement) x err_2reader(scored).

| leaf | agreed-wrong rate (both read the same wrong sign or both miss it) | visible errors per disagreement | single position error | err_2reader (scored) |
|---|---|---|---|---|
| no87 | 0.040 | 0.517 | 0.077 | 0.072 |
| f152r | 0.041 | 0.5 | 0.062 | 0.041 |
| bir1591 | 0.044 | 0.667 | 0.094 | 0.074 |
| gunther | 0.032 | 0.688 | 0.049 | 0.025 |
| f36v | 0.062 | 0.75 | 0.344 | 0.375 |
| f21v | 0.005 | 0.386 | 0.050 | 0.116 |
| f87 | 0.000 | 0.5 | 0.043 | 0.086 |
| dint128 | 0.141 | 0.833 | 0.259 | 0.141 |
| dint98v | 0.000 | 0.5 | 0.009 | 0.019 |
| dint113 | 0.000 | 0.5 | 0.018 | 0.037 |
| dint89 | 0.033 | 0.528 | 0.073 | 0.075 |
| luzerne | 0.094 | -- (0 disagreements) | 0.094 | 0.000 |
| viv102r | 0.163 | 0.713 | 0.209 | 0.065 |

The visible term is well behaved: 0.5-0.8 errors per disagreement on every leaf (at a split at least one reader is wrong; both
are wrong at 0-67% of splits). So err_2reader(scored) x 0.5 is a LOWER bound on single-pass error that holds on every leaf.
The agreed-wrong rate is not: 0.000 (dint-f98v, dint-f113, f87 -- partly by truth construction) to 0.141 (dint-f128) and 0.163
(Vivonne f.102r, where 78% of a pass's errors are shared with the other pass, and the S2 pipeline on the frozen sibling
f.103r read 0.148/0.154 per pass with disagreement 208/1918 = 0.108, from file, not rescored: the same shape). Luzerne's digits:
the two readers agree on 100% of columns and both are wrong on 9.4% of scored signs (every error shared). Two further gaps
between an unread letter's figure and a benchmark figure: err_2reader over whole lines and err_2reader over scored positions
differ by a leaf-specific factor of 0.11 (dint-f98v) to 1.2 (f36v), because readers split most where the truth is also unsure
(unaligned, uncertain, off-key positions are excluded from the score); and the truth definition itself moves err_true by 2-10x
on the same passes (section 6). An unread letter has neither a truth nor its mask.

## 5. Table for the named unread letters (what err_2reader implies, and does not)

Point = x times the median ratio 0.927 (single) / 0.838 (recon); range = x times the per-leaf ratio min-max (0.14-5.39 single,
0.00-5.39 recon; the predictive 95% band from the leaf bootstrap is the same interval). Lower bound = 0.5 x err_2reader, the
only figure that held on every leaf -- and only for disagreement measured on the positions a truth would score.

| letter | err_2reader on file (source) | single pass: point | single pass: range | reconciled: point | reconciled: range | lower bound (0.5 x) |
|---|---|---|---|---|---|---|
| Florence c.127 (florence-dieci-responsive) | 0.17 (TRANSCRIPTION.md Why) | 0.158 | 0.024-0.916 | 0.143 | 0.000-0.916 | 0.085 |
| Florence c.70 L07-L10 gaps117 pair | 0.345 (ciphers/florence-dieci-responsive/NOTES.md:424) | 0.320 | 0.049-1.860 | 0.289 | 0.000-1.860 | 0.172 |
| Birago 1571 f.36/f.47 (fr.3252) | 0.33 (TRANSCRIPTION.md Why; birago-fr3252 NOTES.md:598 (0.34 raw)) | 0.306 | 0.047-1.779 | 0.277 | 0.000-1.779 | 0.165 |
| Birago 1571 f.47r L01-04 merged | 0.44 (ciphers/birago-fr3252-1571-72/NOTES.md:148) | 0.408 | 0.063-2.372 | 0.369 | 0.000-2.372 | 0.220 |
| Birago 1572 f.117r (fr.3252, re-pair) | 0.134 (ciphers/birago-fr3252-1571-72/NOTES.md:1951 (earlier pair 0.25)) | 0.124 | 0.019-0.722 | 0.112 | 0.000-0.722 | 0.067 |
| Debosnys 1883 | 0.28 (TRANSCRIPTION.md Why) | 0.260 | 0.040-1.509 | 0.235 | 0.000-1.509 | 0.140 |
| Birago 1572 f.144r no.73 | 0.24 (ciphers/nevers-birago-fr3251-1572/NOTES.md:1342) | 0.223 | 0.034-1.294 | 0.201 | 0.000-1.294 | 0.120 |
| Birago 1572 f.168 no.85 | 0.13 (ciphers/nevers-birago-fr3251-1572/NOTES.md:1342) | 0.121 | 0.019-0.701 | 0.109 | 0.000-0.701 | 0.065 |
| Birago 1572 f.185r / f.185v | 0.13 (ciphers/nevers-birago-fr3251-1572/NOTES.md:1775 (0.12 / 0.29, pooled 0.13)) | 0.121 | 0.019-0.701 | 0.109 | 0.000-0.701 | 0.065 |

These are NOT calibrated estimates (the gate failed); they are what the numbers would say if one ignored the failure. The one
usable line is the lower bound: Birago 1571 f.36/f.47 at 0.33 cannot have a single pass better than about 0.17; Debosnys at
0.28 not better than 0.14; Florence c.127 at 0.17 not better than about 0.085 -- none near 0.05.
err_2reader a letter would need to imply err_true <= 0.05: at the median ratio 0.054 (single) / 0.060 (recon); at the worst
observed ratio (5.39, Luzerne) 0.0093; and by the agreed-wrong mechanism NO value of err_2reader implies it -- Luzerne's readers
agreed on 98.3% of columns and were both wrong on 9.4%. Only a known answer of the same hand (a glossed sibling leaf, a clerk
sheet, a print) puts a ceiling on err_true; a disagreement figure puts a floor.

## 6. Truth-mask sensitivity (same primary passes, another truth file; never extra points)

| leaf | truth variant | scored | err_2reader | single meas | recon meas |
|---|---|---|---|---|---|
| bir1591 | bir1591-f23r-gloss-jk | 191 | 0.194 | 0.246 | 0.241 |
| dint98v | dint-f98v-gloss-kp | 66 | 0.165 | 0.530 | 0.515 |
| dint98v | dint-f98v-gloss-kp2 | 76 | 0.165 | 0.336 | 0.303 |
| dint113 | dint-f113-gloss-kp | 71 | 0.129 | 0.465 | 0.465 |
| dint113 | dint-f113-gloss-kp2 | 75 | 0.129 | 0.187 | 0.187 |
| dint89 | dint-f89-gloss-kp | 223 | 0.109 | 0.433 | 0.390 |
| dint89 | dint-f89-gloss-kp2 | 249 | 0.109 | 0.147 | 0.124 |
| viv102r | vivonne1573-f102r-dev | 1008 | 0.081 | 0.342 | -- |

Under the key_print truths the Dinteville gloss leaves read 0.15-0.53 instead of 0.02-0.10 for the SAME passes; bir1591's
jackknife 0.25 vs 0.09; Vivonne dev 0.34 vs dev2 0.21. The truth definition moves err_true by more than err_2reader does.

## 7. For the owner, in three sentences

Two readers agreeing does not tell you how right they are: across our 13 known-answer leaves the true error ran from one
seventh of the disagreement rate to five times it, and a shuffled pairing predicts as well as the real one. What the
disagreement rate does give is a floor -- a letter whose readers split on a third of the signs has at least about one sixth of
its signs wrong per pass, so Birago 1571, Debosnys and Florence are all far above the 5% target whatever the reconciliation
looks like. A ceiling needs a known answer in the same hand (a glossed sibling, a clerk sheet, a print), and that, not more
reader passes, is what moves an unread letter from "unknown error" to "measured error".

## 8. Next step and cost

Not a further fit: with 13 leaves and an agreed-wrong rate that is a property of the hand, more leaves of the same hands will
not tighten it. The step that would help an unread letter is a per-hand known answer: for Birago 1571 (fr.3252) the f.36v
gloss beyond line 1 (F36-GLOSS bands, named in TRANSCRIPTION.md "Next items") -- about USD 3-4 for two blind passes plus the
gloss alignment, giving that hand its own err_true and agreed-wrong rate; for Debosnys and Florence no period witness is
known, so their figure stays a floor. Retired for this question: fitting err_true from err_2reader (logged
untestable-at-this-N-and-spread, not refuted; rule 3's third-attempt clause applies to any re-brief on the same data).
Open suggestion (not done, Usage 7): tx_bench could print the 0.5 x err_2reader floor beside any err_2reader a job reports,
as a one-line reminder that it is a floor; that is a reporting convenience, not the estimator this brief asked for.
