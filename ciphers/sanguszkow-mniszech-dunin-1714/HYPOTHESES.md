# sanguszkow-mniszech-dunin-1714 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

## H1: R7524 is in Bourdeau's Potocka key (A3V3-SANGP, 4 Oct 2026) -- control-backed negative

`potocka/potocka_trial.py` (rule 7: `--check` reproduces `potocka/trial_results.json`). Key: D. Bourdeau,
cyphersolver `targets/potocka1714/key-potocka.json` (46 entries, CC BY 4.0, used as data). Coverage 132/232 tokens,
32/77 signs. Statistic: mean log10 4-gram probability of the decode over covered runs (pl18 minus the held-out
Otwinowski file). The key-right control enciphers held-out Otwinowski text with the same key at the target's own
covered positions (same N, mask and run structure; 69 signs mean, the uncovered-sign labels cannot move the statistic);
the key-wrong control can fail, and does, so the test is not a coverage-only non-test (rule 3).

| seed | TARGET | CONTROL A key right mean (p05) | CONTROL B key wrong mean (p95) | shuffled-target null mean (p95) |
|---|---|---|---|---|
| 1 | -2.257 (13 four-grams) | -0.898 (-1.232) | -2.157 (-1.730) | -2.163 (-1.784) |
| 2 | -2.257 | -0.908 (-1.182) | -2.154 (-1.632) | -2.196 (-1.882) |
| 3 | -2.257 | -0.916 (-1.292) | -2.120 (-1.631) | -2.211 (-1.868) |

Control A beats control B's p95 in 200/200 windows; the target sits below the shuffled null's mean. Verdict: the
Potocka key does not read R7524 (agrees with Bourdeau's "separate numerical system"). Caveat: only 13 four-grams fall
inside covered runs at N=232, so the per-window statistic is noisy, but control A's minimum over 600 windows (-1.87)
is still above the target.

## H2: homophonic, unknown key (A3V3-SANGP, 4 Oct 2026) -- non-test at this N

`tools/family_run.py --family homophonic` at N=232, K=77, pl18: CONTROL BELOW GATE (row below). Bourdeau's own
control read 21.1%; ours 7.6% mean. Neither is a negative on the target.

## H3: homophonic, crib-drag on the exact repeats (RUN3-SANG, 4 Oct 2026) -- non-test at this N (CONTROL BELOW GATE)

Pre-registered in `crib/PREREG.md` (commit 358bfabf, before any run). Instrument: `tools/family_run.py --family homophonic
--param profile=target --param crib=drag` (option added to `tools/families/homophonic.py`, test
`tools/tests/test_homophonic_cribdrag.py`). R6 = 22.118.82.36.31.81 (x3), R2 = 15.20 (x8); the top 200 pl18 6-grams pinned
on R6, best 5 crossed with the top 40 bigrams on R2, best pair pinned for the full anneal. The control carries the same
crib kind and count (one 6-sign repeat x3 and one 2-sign repeat x8 planted with identical signs). Rule-3 orthogonality:
recovery is against the known plaintext and a wrong pin drags it to the blind band, so the control can fail -- and did.

| seed | planted 6-gram / bigram | drag chose | crib right (6, 2) | recovery (all) | recovery (unpinned) |
|---|---|---|---|---|---|
| 1 | obadwa / ie | alenie / po | no, no | 0.039 | 0.056 |
| 2 | warsza / ie | ieisze / ie | no, yes | 0.388 | 0.250 |
| 3 | orlows / ie | oktore / ie | no, yes | 0.345 | 0.205 |
| mean | | | 0/3, 2/3 | **0.257 < gate 0.6** | |

Target not run. Two control-only diagnostics, not gates: (i) `crib_oracle=1`, planted 6-gram and bigram added to the
candidate lists: mean 0.250, the planted 6-gram ranked in stage 1's top 5 in 0/3 seeds -- the scoring at N=232 cannot
pick the true 6-gram even when it is offered, so the candidate list is not the limit; (ii) `crib/oracle_ceiling.py`, the
true crib pinned outright on three windows of the same design (windows differ from the battery's: corpus file order): recovery
0.845 / 0.478 / 0.694, mean 0.672 -- a correct crib of this size would carry a control past the gate. Reading: the
instrument that is missing is a way to *choose* the crib, not the annealer; crib-drag by n-gram score is untested-by-this-
tool at N=232 (not refuted). Control K under profile=target is 62-63 (the target's 77; the profile allotment leaves some
small buckets undrawn, also without crib=drag), which makes the control easier, not harder.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 4 Oct 2026 06:18 | homophonic | N=232 K=77 restarts=8 corpus=bc.wbp.lodz.pl.Pamietniki_do_panowania_Augusta_II_91967.txt.gz+bc.radom.pl.11-359.txt.gz+bc.wbp.lodz.pl.Listy_Jana_III_Krola_Polskiego_a_96549.txt.gz+ojczystespomink01johngoog.txt.gz+pamitnikiksakit01kitogoog.txt.gz | 1-3 | 0.076 (0.009-0.159) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | A3V3-SANGP N=232 K=77 pl18 |
| 4 Oct 2026 09:11 | homophonic | N=232 K=77 restarts=8 corpus=bc.wbp.lodz.pl.Pamietniki_do_panowania_Augusta_II_91967.txt.gz+bc.radom.pl.11-359.txt.gz+bc.wbp.lodz.pl.Listy_Jana_III_Krola_Polskiego_a_96549.txt.gz+ojczystespomink01johngoog.txt.gz+pamitnikiksakit01kitogoog.txt.gz profile=target,crib=drag | 1-3 | 0.257 (0.039-0.388) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | RUN3-SANG crib-drag PREREG 358bfabf |
| 4 Oct 2026 09:13 | homophonic | N=232 K=77 restarts=8 corpus=bc.wbp.lodz.pl.Pamietniki_do_panowania_Augusta_II_91967.txt.gz+bc.radom.pl.11-359.txt.gz+bc.wbp.lodz.pl.Listy_Jana_III_Krola_Polskiego_a_96549.txt.gz+ojczystespomink01johngoog.txt.gz+pamitnikiksakit01kitogoog.txt.gz profile=target,crib=drag,crib_oracle=1 | 1-3 | 0.250 (0.017-0.388) | not run (control-only) | - | no | RUN3-SANG diagnostic: planted crib in candidate list (control-only, not a gate) |
| 5 Oct 2026 05:24 | crossmatch (foreign key) | key_crossmatch stat, 200 draws/null, prereg research/PREREG-N9-XM.md | 1-200 | (a) villeroy f200 shuffled-key p99 3.001 / in-class 3.640; (b) hellen R4370 2.690 / 3.766 | (a) 4.120; (b) 3.629 | n/a (no judge; eye: no word stretch) | (a) yes, but order-shuffle z4g 43% >= real; (b) no | N9-XM: (a) frequency coincidence, (b) does not survive |
