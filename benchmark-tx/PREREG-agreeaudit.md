# Pre-registration: TX-AGREEAUDIT on Birago no.87 (written 4 Oct 2026, before any re-read was run)

Tool: `tools/lookalike_pass.py audit` / `audit-score` (this commit). Item: BENCHMARK-TX birago1572-no87 (eval), current
pipeline = committed passC (benchmark-tx/outputs/birago1572-no87/passC.tsv); passes A and B from the same folder.

- Agreed = A, B and C identical at the aligned C position: 776 of 853 signs; of the 803 scored, 736 agreed (710 right,
  26 wrong by the clerk-sheet truth). The 26 agreed-and-wrong positions are in `agreeaudit_no87_include.tsv` and are
  forced into the audit (the auditor is not told which); they are never planted.
- Two packets (one Sonnet vision call each): G1 = f178r, f179r, f178v L01-L10 (`--sample 95`); G2 = f178v L11-L23
  (`--sample 79`); seed 1, k = 3 candidates (shown label + its two most frequent confusion partners from
  harvest/confusion_1572.tsv, plus the original at a plant), plant rate 0.05 of items.
- Flag rule: the re-read picks a label other than the shown one at H or M (L, SPLIT, X_NEW are not flags).
- Control gate (brief): pooled planted catch (flag AND pick == original) >= 0.80, else the audit is a non-test and no
  target figure is read as a result (rule 3).
- Target measures: flags on the 26 agreed-wrong; false-flag rate on agreed-right unplanted items; paired fixed / broken
  if every flag is applied to passC; err_true before / after with tools/tx_bench.py.
- Adoption: fixed > broken with a one-sided sign test p < 0.05. Ceiling stated in advance: only 8 of the 26 agreed-wrong
  have a truth-set sign among their k=3 candidates, so at most 8 can be fixed by this design at k=3.
- Note on the 26 forced items: they make the audited set about 13% wrong against a natural 3.5% among agreed signs; the
  false-flag rate is measured on the random part only.
