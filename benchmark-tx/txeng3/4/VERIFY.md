# VERIFY TXE3-4 CALIB (11 Oct 2026, about 15:00 UTC by date -u)

Verifier for the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M). This session did not run the experiment. It worked
only from committed files, in a sparse worktree of origin/main at 702468311: 0 model passes, 0 image reads, no network
beyond git. No confirm item and no oracle page was opened. The experiment's own files are unchanged.
Under audit: PREREG `benchmark-tx/PREREG-txeng3-4.md` (d6641d4e9, 05:53:38 UTC), RESULTS and outputs in
`benchmark-tx/txeng3/4/` (67cadbd1f, 06:04:51 UTC), the LEDGER row (USD 10.40, Fable 5.1) and ROOM lines 14628 and 14648.

## Verdicts on the three sentences told to the owner

| # | Claim | Verdict | Corrected sentence |
|---|---|---|---|
| 1 | Across 13 known-answer letters there was no usable link between two-reader disagreement and true error. | **overstated** | On the registered test, two-reader disagreement did not give a usable error estimate across 13 known-answer leaves in 7 hands (Spearman 0.11, shuffle p 0.39; a constant guess predicted as well), so no estimator was adopted. That is weaker than "no link". The test had about even odds of detecting a moderate link. The registered secondary measure, disagreement on scored positions, does track error (Spearman 0.52, p 0.04). The six leaves whose answer key was built from these same passes all read low. On the other seven, the link is strong (post hoc: rho 0.71, error 0.9-5.4x the disagreement). |
| 2 | Disagreement gives only a floor, so Birago 1571, Debosnys and Florence are all well above 5%. | **overstated** | For a *single blind pass*, the splits on file suggest a rough floor of about half the disagreement rate: about 17% for Birago 1571, 14% for Debosnys and 8-9% for Florence c.127. That floor was not pre-registered. Measured over whole lines, as these letters' figures are, it held on 8 of the 13 test leaves. It says nothing about a reconciled or sorter-checked transcription. The 0.28 Debosnys figure dates from before its alphabet was settled. |
| 3 | Only a known answer in the same hand can measure their error. | **overstated** | Disagreement alone cannot put a ceiling on their error. This experiment did not test what can. A known answer in the same hand (a glossed sibling, a clerk sheet, a print) is the obvious candidate, but whether one transfers to another leaf of that hand was not measured here (TXE3-3 and TXE3-7 bear on it). |

## 1. Re-derivation (committed script, committed truth, committed outputs)

`python3 benchmark-tx/txeng3/4/calib.py --out <scratch>` (Python 3.11.15, 7 s) rewrote all five outputs.
calib_pairs.tsv, calib_leaves.tsv and calib_lines.tsv are **byte-identical**. calib_fit.json and calib_run.txt differ only
in the last float digit (largest absolute difference 2.2e-16, summation order). Each pass was also scored separately with
`tools/tx_bench.py --bench BENCHMARK-TX.tsv --item <item> --exclude-flagged <pass>.tsv`. All 35 primary-pass figures
(A, B and the reconciliation on 13 leaves) match calib_pairs.tsv as measured: for example no87 0.066 (53/803), 0.097
(78/803), 0.051 (41/803); viv102r 0.194 (239/1234), 0.225 (277/1234); f152r B 0.069 (5/73), matching RESULTS' own note.

| figure | reported | re-derived |
|---|---|---|
| Spearman single, 13 leaves | 0.110 | 0.110 (Pearson 0.375, not reported in RESULTS) |
| shuffle-control p (rho), control q95 | 0.389, 0.48 | 0.389, 0.478 (same seed); 0.372 on an independent 10,000-shuffle run |
| LOO MAE ratio / OLS / constant | 0.0900 / 0.0924 / 0.0866 | same |
| per-leaf ratio min-max, q10-q90, spread factor | 0.14-5.39, 0.23-2.57, 11.3 | same |
| recon: Spearman, p | 0.164, 0.336 | same |
| flagged-excluded single: Spearman, p | 0.468, 0.040 | same |
| all 22 pairs: Spearman, leaf-bootstrap 95% | 0.27, -0.16 to 0.60 | same |
| dev-only -> eval | 4/4 inside a band 0.14x-5.39x | same |
| gate: g1 / g2 / g3 / g4 | False / False / 4 of 4 / 11.3 -> holds False | same |
| "0.5 x err_2reader(scored) is a lower bound ... that holds on every leaf" | every leaf | **12 of 13**: fails on f21v (9.5 single-pass errors vs 22/2 = 11). f87, dint98v and dint113 sit exactly at the bound |
| "visible term ... 0.5-0.8 errors per disagreement on every leaf" | 0.5-0.8 | **0.386 on f21v**; secondary pairs no87 X21opus 0.40, f87 X21opus 0.469 |
| floor applied to unread letters: 0.5 x whole-line err_2reader (sec. 5, owner sentence 2) | "the only figure that held on every leaf" | **8 of 13 primary leaves** (17 of 22 pairs). Fails on bir1591 (0.094 < 0.097), f21v (0.050 < 0.075), f87 (0.086 < 0.141), dint98v (0.038 < 0.083), dint113 (0.018 < 0.065) |
| registered secondary x = err_2reader on scored positions vs single err_true | per-leaf column only, no association reported | Spearman 0.522, Pearson 0.762, shuffle p 0.038 (10,000) |

Post hoc and NOT registered, given only to test claim 1. RESULTS section 1 names six leaves whose truth is built from these
same passes: f21v and f87 (S-tokens of these passes' own decode), and dint98v, dint113, dint89 and bir1591 (truth aligned to
passZ from these passes). The two groups separate completely on the ratio:

| group | n | ratio err_true/err_2reader (single) | Spearman | shuffle p (exact) | LOO ratio vs const | q90/q10 |
|---|---|---|---|---|---|---|
| truth built from these passes (f21v, f87, dint98v, dint113, dint89, bir1591) | 6 | 0.14, 0.23, 0.31, 0.34, 0.48, 0.92 | 0.03 | -- | -- | 3.4 |
| the other seven (no87, f152r, gunther, f36v, dint128, luzerne, viv102r) | 7 | 0.93, 1.09, 1.20, 1.95, 2.42, 2.57, 5.39 | 0.71 | 0.044 | 0.112 vs 0.125 | 2.4 |

The seven-leaf result is a subset chosen after seeing the data, from 7 leaves. It is a lead, not a pass. It does show that
the registered null mixes two truth regimes, and that most of the "factor 11" spread lies between those regimes, not
between hands.

Power of gate 1 at n = 13 (simulated, 4,000 draws, against the control's own q95 of 0.478): P(pass) is 0.25 at a true
correlation of 0.3, 0.52 at 0.5 and 0.84 at 0.7.

## 2. Pre-registration order and deviations

- The PREREG was committed at 05:53:38 UTC, 11 min before the results at 06:04:51; the ROOM claim was 05:53. calib.py first
  appears in the results commit, so git cannot prove that no score was run before 05:53, but the order is consistent.
  This is a re-analysis of figures already on disk: the PREREG itself cites per-pass err_true "0.01-0.45 on file". So the
  registration fixes the analysis (leaf set, pairs, endpoint, gate), not blindness to the y values. That is acceptable for
  this design.
- Undeclared deviation (minor): the PREREG says "the form used for the unread-letter table is chosen on DEV leaves only by
  leave-one-leaf-out MAE". On dev, OLS (0.1290) beats the ratio form (0.1320), and both lose to the constant (0.1148). RESULTS
  used the ratio form for the dev->eval prediction and the point column without saying so. It does not change the verdict,
  since gates 1 and 2 fail anyway.
- Selective reporting (minor): the registered secondary x (err_2reader on scored positions) is tabulated per leaf, but its
  association (p 0.038) is not reported. The flagged-excluded "beside" p of 0.040 is reported.
- Post hoc material presented as a finding: the section-4 decomposition, the "floor" and the "lower bound" column in
  section 5 are not in the PREREG. They are not labelled exploratory and have no control. Owner sentence 2 rests on them.

## 3. Gate as registered

Gate: "holds" only if ALL of (1) shuffle p < 0.05 for Spearman (single, 13 leaves); (2) LOO MAE of the ratio predictor <
constant-mean LOO MAE; (3) at least 3 of 4 eval leaves inside the dev-only leaf-bootstrap 95% band. (4) The q90/q10 spread
factor at most 3 governs only the tool output. If any of 1-3 fails: "a null, logged in RESULTS.md ('err_2reader does not
license an err_true estimate at this N / these hands'), no tool option."

On the numbers: g1 False (0.389), g2 False (0.0900 vs 0.0866), g3 4 of 4 (meaningless: the band spans a factor of 38, as
RESULTS says). The registered verdict, **NULL (no estimator)**, follows correctly, and no tool option was added. The
registered wording is "does not license an err_true estimate at this N / these hands". "No usable link" drops the
qualifier.

## 4. Control

The shuffled-label permutation re-pairs x with other leaves' y. Both statistics it is used for (Spearman, LOO MAE) depend on
that pairing, so it can vary (rule 3), and it did: the q95 is 0.48 and 32% of shuffles beat the observed LOO MAE. It is a
real control. It cannot see the truth-regime confound in section 1: within each regime, the shuffle and the observed
pairing share the same mix.

## 5. Split

Dev 9 leaves and eval 4 leaves, as registered. The primary endpoint uses all 13, as registered. No parameter was tuned on
eval. The dev-only prediction is reported on eval. No eval look was used for tuning.

## 6. Rule issues

- Flagged-excluded figures: never quoted alone in RESULTS or in the owner sentences (both masks given). Several flagged
  masks are small (dint113: 26 of 81 positions left; viv102r: 679 of 1234).
- Cost USD 10.40, under the 15 cap. Done at 06:05 UTC, inside the 07:47 box.
- No novelty wording. No shared tool changed. No truth file edited.
- Rule 3 third-attempt clause misapplied: RESULTS logs "fitting err_true from err_2reader" as retired, with "rule 3's
  third-attempt clause applies to any re-brief on the same data". The clause needs a second or third attempt at an
  unchanged approach. This is the first. Given the regime split above, a fit restricted to independent-truth leaves (or
  new ones) is a different design, not a re-tune.
- Unread-letter inputs taken unchecked: 0.33, 0.28 and 0.17 come from TRANSCRIPTION.md "Why" (3 Oct 2026), with no check
  of their convention or currency. CLAUDE.md Usage 6 records Debosnys' 28% as disagreement from before the owner settled the
  alphabet. Under an unsettled label inventory, a split can be naming, not reading error (cf. dint-f128 raw 0.353 vs
  label-mapped 0.247, TRANSCRIPTION.md row 1). So the floor need not transfer.
- "13 known-answer letters": these are 13 leaves in 7 hands. Two (f21v, f87) have a truth that BENCHMARK-TX.tsv itself
  marks "not independent of the committed transcription".
- The floor is single-pass only. RESULTS section 7's "whatever the reconciliation looks like" is unsupported: the
  reconciled ratio runs down to 0.00 (section 5's own recon range), and a third look can resolve visible splits.

## 7. Safe sentence for the owner

Disagreement between two readers did not give a usable error estimate on the registered test (13 leaves, 7 hands), so none
was adopted. But that is not proof of no link: on the 7 leaves whose answer key is independent of the passes, the link was
strong (post hoc). For a single blind pass, Birago 1571, Debosnys and Florence c.127 are probably above 5% (a rough floor
of half the split, which held on 8 of 13 test leaves). Nothing here bounds a reconciled or sorter-checked transcription,
and whether a same-hand known answer transfers was not tested.

## Second check (11 Oct 2026, written about 16:4x UTC by the account-3 parent from the second verifier's report; workflow wf_35ed2244-0e6)

A second, independent agent ruled on each objection and non-holds verdict above, re-running the commands itself. Where it disagrees with this file, this section governs.

### Rulings on the first verifier's objections

- **agree**: 1. RESULTS sec. 4: '0.5 x err_2reader(scored) is a lower bound that holds on every leaf' is false; f21v has 9.5 single-pass errors vs 11 (half of 22 disagreements).
  - Evidence: I re-ran calib.py into scratch. calib_pairs/leaves/lines.tsv are byte-identical and calib_fit.json is within 2.2e-16. From calib_pairs.tsv, f21v has wrongA 9, wrongB 10 and 0.1164 x 189 = 22 scored disagreements, so 9.5 < 11. f87, dint98v and dint113 sit exactly at the bound. I also found the cause: the benchmark truth is value-level homophone sets (186 of 189 scored f21v positions are multi-valued). When two readers pick different homophones, neither is wrong, so 'at a split at least one reader is wrong' is not true under the project's own scorer.
- **agree**: 2. RESULTS sec. 4: 'visible term 0.5-0.8 errors per disagreement on every leaf' is false (f21v 0.386; no87 X21opus 0.40; f87 X21opus 0.469).
  - Evidence: The visible_per_disagree column in calib_pairs.tsv reads f21v 0.386, no87 X21opus 0.4 and f87 X21opus 0.469. RESULTS contradicts its own tables here: its section-4 table prints 0.386 and its section-2 table prints 0.4 and 0.469.
- **agree**: 3. Sec. 5 / owner sentence 2: on whole-line err_2reader the floor holds on only 8/13 primary leaves (fails bir1591, f21v, f87, dint98v, dint113).
  - Evidence: Re-derived the same: bir1591 0.0936<0.0969, f21v 0.0503<0.0749, f87 0.0863<0.1406, dint98v 0.0377<0.0827, dint113 0.0185<0.0645. That is 8/13 primary leaves and 17/22 pairs. The verifier left out a caveat that cuts the other way. All five misses are among the six leaves that RESULTS sec. 1 says have truth built from these same passes. On the other seven leaves the floor held 7/7. The alternate truth variants (kp, kp2, jk) give 0.19-0.53 single error on dint98v, dint113 and bir1591, which clears the floor there too. So 8/13 is the correct figure, but the misses look like truth construction rather than random. The floor is still post hoc and has no control.
- **agree**: 4. Sec. 7 'whatever the reconciliation looks like' is unsupported; the floor bounds a single pass only.
  - Evidence: The reconciled ratio runs down to 0.00 (dint98v and dint113 recon 0.000). Against 0.5 x whole-line err_2reader, the reconciliation clears the floor on only 6 of 10 leaves (fails bir1591 0.079<0.097, dint98v 0<0.083, dint113 0<0.065, dint89 0.042<0.055). A third look can resolve visible splits. Only the agreed-wrong term bounds a reconciliation.
- **partly**: 5. The registered secondary x (err_2reader on scored positions) has its association left out: Spearman 0.522, Pearson 0.762, shuffle p 0.038.
  - Evidence: The figures reproduce: rho 0.522, Pearson 0.762, p 0.036 on my own 10,000 shuffles. The PREREG registers this x as a secondary statistic but registers no association test for it; the Endpoint names only err_2reader. RESULTS did report the equally unregistered flagged-excluded p 0.040, so leaving this one out is mildly selective. The verifier is wrong to read it as evidence of a usable link, for three reasons. (a) It needs the truth's scored mask, which an unread letter does not have. (b) It is partly arithmetic: every scored split between non-homophones adds at least half an error to y. (c) It rests on f36v, which has 16 signs; without f36v, rho is 0.39 and p 0.11.
- **partly**: 6. Truth-regime confound: the 6 leaves with pass-derived truth all have ratio <=0.92 and the other 7 all have >=0.93 (post hoc rho 0.714, exact p 0.044); the factor-11 spread is mostly between regimes.
  - Evidence: The numbers reproduce: exact p 0.044 over 5,040 permutations, six-leaf rho 0.03, seven-leaf LOO ratio 0.112 vs constant 0.125. RESULTS should have analysed this, so it is a fair lead against the null. Four things weaken it. (a) The gap between the groups is 0.916 vs 0.927. (b) The split exists only on the as-measured mask. Under flagged-excluded the groups overlap (seven 0.00-2.42, six 0.00-0.90). The seven's two highest as-measured ratios sit almost entirely on build-flagged, truth-doubtful positions: luzerne goes from 6+6 errors to 0, viv102r pass A from 239 to 2. (c) 'Answer key independent of the passes' does not hold for all seven. BENCHMARK-TX.tsv says no87's clerk sheet was aligned on passC, these passes' own reconciliation ('home advantage on segmentation'). PREREG-dint128 says dint128 is scored only where a reconciled read agrees with the print ('a lower bound'). (d) Even on the seven, the ratio runs 0.93-5.39, so the spread is still too wide for an estimate. New finding: calib scores dint128 raw, but its own PREREG names the label-mapped figure as err_true (pass A 0.247, pass B 0.188). That gives ratio 1.60, not 2.42. Rho stays 0.11 and the gates do not change (LOO ratio 0.081 vs constant 0.072).
- **agree**: 7. Undeclared deviation: dev LOO picks OLS (0.1290) over ratio (0.1320), yet the ratio form was used for dev->eval and the point column.
  - Evidence: calib_fit.json dev_fit.loo gives ratio 0.13197, OLS 0.12899 and constant 0.11483. The PREREG says the form is chosen 'by leave-one-leaf-out MAE' on dev, so OLS should have been used, and RESULTS reports only ratio vs constant. A second minor deviation: the dev band is 'x times the dev ratio distribution', not the registered leaf-bootstrap band. Neither changes the NULL, and the section-5 table is labelled 'NOT calibrated'.
- **agree**: 8. RESULTS sec. 8 misapplies rule 3's third-attempt clause ('retired') to a first attempt.
  - Evidence: No earlier err_2reader-to-err_true calibration is on file. A grep of benchmark-tx PREREGs and RESULTS finds only PREREG-txeng3-4. PREREG-agreeaudit (4 Oct) audits agreed signs on no.87 with a different instrument. The clause covers a second or third attempt at an unchanged approach. Calling the approach 'retired' after one attempt goes beyond it. The correct log is 'NULL at this N / these hands', with a re-design (independent-truth leaves, label-normalised truth) left open.
- **agree**: 9. Unread-letter inputs 0.33/0.28/0.17 were used without checking convention or date; Debosnys' 28% predates the settled alphabet.
  - Evidence: TRANSCRIPTION.md 'Why' (3 Oct 2026) gives the three figures with no method. CLAUDE.md Usage 6 says 'Debosnys ran about 28% reader disagreement through many machine passes before this', meaning before the owner's sign-sorter settlement of 2 Oct. Two things can inflate a split without any reading error: naming differences (dint-f128 raw 0.353 vs label-mapped 0.247 is the same mechanism, measured on err_true) and homophone choice (see objection 1). The floor therefore need not transfer to these letters.
- **agree**: 10. Gate-1 power at n=13 is ~0.25/0.52/0.84 at true correlation 0.3/0.5/0.7, so the null is weak evidence against a moderate link.
  - Evidence: My own simulation (4,000 bivariate-normal draws per level, Spearman > 0.478; the null q95 recomputes to 0.478) gives 0.24 / 0.50 / 0.83. One caveat: power bears on 'no link', not on 'no usable link'. The ratio spread (q10-q90 factor 11.3 against a registered 3) is measured directly and does not depend on power.
- **agree**: 11. calib.py has no --check (stale) mode; outputs reproduce, so rule 7 is effectively met.
  - Evidence: argparse has only --out, --boot and --seed. My re-run gave byte-identical TSVs and JSON within 2.2e-16. Rule 7 is written for decipherment readings; this is a measurement. Minor.
- **partly**: Claim 1 verdict 'overstated' and its corrected sentence (adds 'scored-position disagreement does track error (p 0.04)' and 'on the 7 independent-truth leaves the link was strong').
  - Evidence: I agree the verdict is overstated: 'letters' should be 'leaves' (13 leaves, 7 hands), and 'no usable link' drops the registered qualifier 'at this N / these hands'. The verifier's corrected sentence overreaches in the other direction. Scored-position disagreement cannot be computed for an unread letter, is partly arithmetic, and depends on f36v (objection 5). The seven leaves are not all independent of the passes, and their high ratios sit on flagged truth (objection 6). 'Strong' is not supported for a post hoc subset of n=7 whose ratios still span 0.93-5.4.
- **agree**: Claim 2 verdict 'overstated'.
  - Evidence: The floor is post hoc and covers a single pass only, not a reconciliation. 'Well above' does not fit Florence c.127 at 0.085. The Debosnys input predates the settled alphabet. The verifier's corrected sentence should add that all five whole-line misses are on pass-derived-truth leaves (the floor held 7/7 on the other seven), so the floor is better supported than '8 of 13' suggests on its own.
- **agree**: Claim 3 verdict 'overstated'.
  - Evidence: Transfer of a same-hand known answer was never tested. The 'stable within hand' figures are repeat pairs on one leaf (Vivonne: 4 pairs all on f102r; dint128: 3 pairs all on f128). Across leaves of one hand the ratio spans Dinteville office 0.14-3.09 and Ceppo-Nevers 0.31-1.64 (by_hand in calib_fit.json). Inside each hand the spread follows how each leaf's truth was built: print or gloss vs aligned to passZ or S-tokens. 'Only' also rules out routes this experiment never tried.

### Final verdict on each claim told to the owner (11 Oct ~07:05 UTC)

- **overstated**: Across 13 known-answer letters there was no usable link between two-reader disagreement and true error.
  - Evidence: The registered NULL reproduces exactly (re-run byte-identical): Spearman 0.110, shuffle p 0.389 (0.356 on my own 10,000 shuffles), LOO ratio 0.0900 vs constant 0.0866, per-leaf ratio 0.14-5.39 (q10-q90 factor 11.3 against a registered 3). The gate fails on g1 and g2, and no tool option was added. Two problems with the wording: these are 13 leaves in 7 hands, not 13 letters, and the registered wording is 'does not license an err_true estimate at this N / these hands'. Gate-1 power at a moderate correlation is about 0.5. The post hoc six/seven truth split (rho 0.71 on 7, exact p 0.044) is a lead, not a link. On the seven the ratio still spans 0.93-5.39, two of those leaves carry their errors on flagged truth, and the separation vanishes under the flagged mask. Scored-position disagreement (p 0.036) cannot be computed for an unread letter.
  - Corrected: On the registered test (13 known-answer leaves, 7 hands), two-reader disagreement did not give a usable estimate of true error. True error ran from 0.14 to 5.4 times the disagreement, and a shuffled pairing predicted as well, so no estimator was adopted. This is a null at this sample size, not proof that no link exists.
- **overstated**: Disagreement gives only a floor, so Birago 1571, Debosnys and Florence are all well above 5%.
  - Evidence: The floor (0.5 x err_2reader) is not in the PREREG and has no control. RESULTS says it held 'on every leaf'. On scored positions it fails on f21v (9.5 vs 11, because homophone-set truth means a split is not always an error). Over whole lines, the measure applied to the unread letters, it held on 8/13 primary leaves. All five misses are leaves whose truth was built from the same passes; it held 7/7 on the rest. It bounds a single blind pass only: the reconciliation clears it on 6/10 and reaches 0.000. Florence c.127's implied floor is 0.085, which is not 'well above' 5%. The 0.33/0.28/0.17 inputs come from TRANSCRIPTION.md with no method stated, and Debosnys' 0.28 predates the settled alphabet (CLAUDE.md Usage 6).
  - Corrected: An unregistered rule of thumb from this data: a single blind pass is wrong on at least about half the signs the two readers split on. It held on 8 of 13 leaves, and all five misses were on leaves whose answer key came from those same passes. By that rule a single pass on Birago 1571 would be about 16% or worse and on Florence c.127 about 8% or worse. It says nothing about a reconciled or sorter-checked transcription, and the Debosnys 28% split predates the settled alphabet.
- **overstated**: Only a known answer in the same hand can measure their error.
  - Evidence: Transfer of a same-hand known answer to another leaf was not tested. The within-hand stability RESULTS cites comes from repeat pairs on one leaf. Across leaves of one hand the ratio spans 0.14-3.09 (Dinteville office) and 0.31-1.64 (Ceppo-Nevers), following how each leaf's truth was built. 'Only' rules out routes never tried here.
  - Corrected: Disagreement alone cannot put a ceiling on these letters' error. A known answer in the same hand (a glossed sibling, a clerk sheet, a print) is the obvious candidate, but this experiment did not test whether one transfers to another leaf.

### Sentence the parent may give the owner

On the registered test (13 known-answer leaves, 7 hands), disagreement between two readers did not give a usable estimate of true error: true error ran from 0.14 to 5.4 times the split and a shuffled pairing predicted as well, so no estimator was adopted (a null at this size, not proof of no link). A rough, unregistered rule of thumb (a single blind pass is wrong on at least half the signs the readers split on, which held on 8 of 13 leaves) puts a single pass on Birago 1571 at about 16% or worse, but it bounds nothing reconciled or sorter-checked, the Debosnys 28% predates the settled alphabet, and whether a same-hand known answer transfers was not tested.
