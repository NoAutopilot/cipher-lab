# PREREG FAM-11106L (LANE FAMILY, account 2), written 8 Oct 2026 before any FAM-11106L score was computed

Target: tx/ciphertext_oneline.txt (N 820, K 41, FAM-11106T). Family: `homophonic` (tools/family_run.py), `--param profile=target
--param noise=0.10 --measured-error 0.10` throughout (noise = err_2reader 0.10, the rule-3 bracket), restarts 8, gate 0.6 on control mean.

Runs, in this order (each control first; target only if that control's mean >= 0.6; the tool enforces this):
1. fr16 (spec as is, corpus lettresdecatheri01, same as FAM-11106T), `--seeds 6`. Purpose: the control's mean and spread at 6 seeds.
   Attempt count for "homophonic French K41": this is attempt 2 (FAM-11106T was 1). Only the seed count changes.
2. German, corpus **de1600** (Bezold, Briefe Johann Casimir 1575-86 + Briefe und Acten 1599-1611; real period letters), not de16:
   de16 is an 8.5 KB model-composed text, not a historical source (tools/data/de16/README.md), so a control or judge built on it would
   not be a period-German test. Spec copy specs/wvo-11106-bergh-1572-de1600.json (judge language de1600). `--seeds 3`. Attempt 1.
3. Latin, corpus **la17** (1590-1649 scholar-diplomat letters; era gap 20-75 years, no 16th-c. Latin on file; stated, not fixed).
   Spec copy specs/wvo-11106-bergh-1572-la17.json (judge language la17). `--seeds 3`. Attempt 1.
4. Dutch: **skipped**. nl18 / nl20 are era-mismatched (18th c. / 1880-1940), nl_dev is a modern Bible, nl_repo is targets' own readings.
5. Merged inventory (stated before scoring): merge only the three pairs both passes split on in both directions with >= 7 splits in
   tx/focus.tsv -- dd->d (17), yx->y (10), S->s (7). K 41 -> 38. File tx/ciphertext_oneline_merged.txt (tx/merge_inventory.py).
   Run under fr16 with `--seeds 3`, and under the language whose control has the best mean among 2-3 if any passes its gate.

Pass rule (per run): a target judge PASS with its control at gate = a candidate, followed by a `--shuffle-target 1` floor run of the same
settings; a judge PASS on the shuffled decode voids it. A target FAIL with control at gate = control-backed negative for that
language/inventory. Control below gate = non-test (no target scored).
Firmness rule for run 1: if the 6-seed control mean is < 0.6, FAM-11106T's French negative is downgraded to a non-test; if >= 0.6 but
fewer than 4 of 6 seeds reach 0.6, the negative is reported "weak (bimodal control)".
