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

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 4 Oct 2026 06:18 | homophonic | N=232 K=77 restarts=8 corpus=bc.wbp.lodz.pl.Pamietniki_do_panowania_Augusta_II_91967.txt.gz+bc.radom.pl.11-359.txt.gz+bc.wbp.lodz.pl.Listy_Jana_III_Krola_Polskiego_a_96549.txt.gz+ojczystespomink01johngoog.txt.gz+pamitnikiksakit01kitogoog.txt.gz | 1-3 | 0.076 (0.009-0.159) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | A3V3-SANGP N=232 K=77 pl18 |
