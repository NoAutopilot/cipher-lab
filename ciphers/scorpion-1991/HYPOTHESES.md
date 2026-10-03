# scorpion-1991 -- hypothesis families

## PREREG A2P4-SCORP (3 Oct 2026, committed before any run)

Family: `homophonic` (tools/family_run.py, homophonic_anneal.py), cryptogram 1 (S1) only, one message of N=70, K=53
(grid rows joined; `scripts/s1_ours_oneline.txt` from ciphertext.txt). Control first at N=70, K=53, English, spec judge
corpora (pg1661_holmes + pg2701_mobydick), `--param profile=target` (the control's sign-count profile matches S1's own:
39 of 53 signs hapax), seeds 1-3, restarts 8. Gate: control mean recovery >= 0.6 (family_run default). If the control
misses the gate the target is not run and the result is logged "untestable by this family at N=70, K=53" (rule 3), not a
negative. If the control meets the gate, the target is run on both transcriptions (ours and Bourdeau's
`scripts/s1_bourdeau_oneline.txt`; they agree on 61/70 positions, bourdeau_diff.tsv) and judged by the spec's judge
block; the `en` judge corpus is of unknown reliability (EN-FOLDS), so a PASS would be "worth a verifier", never a reading.
Status stays `open` unless the judge PASSes with the control met.

## PREREG A2P4-SCORP3 (3 Oct 2026, committed before any run)

Question: is cryptogram 2 (S5) testable at all by the `homophonic` family once transcribed? Control only; **no target
run** (S5 has no settled transcription, TRANSCRIPTION.md). Same family, corpora (spec judge: pg1661_holmes +
pg2701_mobydick), seeds 1-3, restarts 8 and gate 0.6 as A2P4-SCORP. N and K come from a shape-only placeholder
(`scripts/s5_shape_placeholder.py`, not a transcription): N=180 and K=155 (the spec's values, Schmeh), flattest
sign-count profile (130 hapax + 25 doubletons), `--param profile=target` = the primary run.
Sensitivity runs (declared now, not primary): K=145 (Bourdeau's and Cipherbrain comment 6's count; 110 hapax + 35
doubletons) with profile=target; and K=155 with the default profile.
Decision rule: primary control mean >= 0.6 -> "testable at N=180": the S5 transcription step is worth costing, then a
target run under the A2P4-SCORP prereg's judge terms. Mean < 0.6 -> "untestable by this family at N=180, K=155" and,
with A2P4-SCORP's N=70 result, untestable by this family on both published cryptograms (rule 3: not a negative on the
target). If only the K=145 sensitivity run meets the gate, the result is "depends on K": a settled K is the next step
before any transcription spend.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 3 Oct 2026 17:40 | homophonic | N=70 K=53 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt profile=target | 1-3 | 0.038 (0.000-0.071) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | A2P4-SCORP S1 ours |
| 3 Oct 2026 17:40 | homophonic | N=70 K=53 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1-3 | 0.133 (0.086-0.171) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | A2P4-SCORP S1 ours, sensitivity (not preregistered): default profile |
