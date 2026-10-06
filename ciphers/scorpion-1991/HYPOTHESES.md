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

## PREREG R11-SCORPCYC (6 Oct 2026, 13:4x UTC, committed before any scored run)

Family: `cycling_homophonic` (new module tools/families/cycling_homophonic.py, this job): Pelling 2020's design hypothesis
for the Scorpion, each plain letter's homophones used in one fixed cyclic order (the i-th occurrence of a letter with m
homophones writes homophone (offset + i) mod m). Control design: a plaintext window held out of the solver's corpus, K
homophones allotted by corpus letter frequency (as homophonic_anneal.make_control), each letter's homophones then used in
cyclic order from a random offset. Solver: an n-gram anneal over the sign -> letter key whose objective adds
-lam x (cycle violations): for each letter, its sign sequence in text order must repeat with period m = its number of
distinct signs; every position where it does not counts one violation (a true key has none). Same spec judge corpora
(pg1661_holmes + pg2701_mobydick), seeds 1-3, restarts 8, gate 0.6 (control mean recovery).
Runs: (1) primary S1: N=70, K=53, lam default (2.0), on `scripts/s1_ours_oneline.txt`; (2) S5 shape placeholder N=180,
K=155 (`scripts/s5_shape_N180_K155.txt`, A2P4-SCORP3) control-only; (3) sensitivity N=180, K=145 control-only;
(4) sensitivity S1 N=70 K=53 with `--param lam=50` (cycle as a near-hard constraint), control-only unless it alone meets
the gate. Target S1 is run (ours and Bourdeau's transcription) only if the N=70 control mean >= 0.6, then judged by the spec's
judge block (en corpus of unknown reliability, EN-FOLDS: a PASS = "worth a verifier", never a reading). S5 is never run (no
settled transcription). A control below gate = "untestable by this family at this N, K" (rule 3), not a negative.
Can the control vary on the statistic? Yes: recovery is per-position letter agreement on a fresh enciphered window per
seed; the cycle term changes the solver's search, not the scoring. The module's offline test must show the cycle term
reading an easy cycling control (N=400) at least as well as lam=0, so a low N=70 figure is the N, not a broken solver.

**Amendment to PREREG R11-SCORPCYC (6 Oct 2026, 13:4x UTC, before any scored run; only the module's offline test had run).**
The violation count is changed from the period-m check to a gap check: between two consecutive occurrences of one sign
in a letter's sign sequence no other sign may appear twice (in a strict cycle every other sign appears exactly once);
each extra appearance is one violation. Reason: on the easy offline control (N=400, K=40, seed 1, 4 restarts) the
period-m term stalled the anneal (recovery 0.030 at lam=2 vs 0.953 at lam=0) because one wrong sign shifts m and rescores
the whole letter; the gap check reads 0.995 at lam=2 (0 violations) vs 0.953 at lam=0. Runs, N, K, seeds, restarts,
corpora, lam values and the 0.6 gate are unchanged.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 3 Oct 2026 17:40 | homophonic | N=70 K=53 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt profile=target | 1-3 | 0.038 (0.000-0.071) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | A2P4-SCORP S1 ours |
| 3 Oct 2026 17:40 | homophonic | N=70 K=53 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1-3 | 0.133 (0.086-0.171) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | A2P4-SCORP S1 ours, sensitivity (not preregistered): default profile |
| 3 Oct 2026 18:15 | homophonic | N=180 K=155 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt profile=target | 1-3 | 0.037 (0.011-0.067) | not run (control-only) | - | no | A2P4-SCORP3 S5 shape placeholder, primary |
| 3 Oct 2026 18:16 | homophonic | N=180 K=145 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt profile=target | 1-3 | 0.131 (0.061-0.228) | not run (control-only) | - | no | sens_K145_profile |
| 3 Oct 2026 18:16 | homophonic | N=180 K=155 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1-3 | 0.081 (0.050-0.100) | not run (control-only) | - | no | sens_K155_default_profile |
| 6 Oct 2026 13:46 | cycling_homophonic | N=70 K=53 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1-3 | 0.067 (0.057-0.071) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | R11-SCORPCYC S1 ours, primary |
| 6 Oct 2026 13:47 | cycling_homophonic | N=180 K=155 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1-3 | 0.078 (0.044-0.111) | not run (control-only) | - | no | R11-SCORPCYC S5 shape placeholder N180 K155, primary |
| 6 Oct 2026 13:47 | cycling_homophonic | N=180 K=145 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1-3 | 0.059 (0.050-0.072) | not run (control-only) | - | no | R11-SCORPCYC sens K145 |
| 6 Oct 2026 13:47 | cycling_homophonic | N=70 K=53 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt lam=50 | 1-3 | 0.114 (0.086-0.157) | not run (control-only) | - | no | R11-SCORPCYC S1 sens lam=50 (control-only) |
| 6 Oct 2026 17:50 | shape-source (Zodiac Z408/Z340 alphabet), blind second coder | 53 S1 types / 70 positions; distinct non-letter codes; control Unicode Geometric U+25A0..U+25E5 (no coder) | - | control 8 distinct codes | Zodiac 11 (cross-coder: B's S1 vs A's Zodiac); diff 3 | kappa A-vs-B S1 0.549 exact, 0.756 family | no (prereg diff >= 5) | R13-SCORP2C, PREREG-R13-SCORP2C.md; same-coder diff 7 (A and B alike) |
