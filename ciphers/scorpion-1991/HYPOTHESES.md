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
