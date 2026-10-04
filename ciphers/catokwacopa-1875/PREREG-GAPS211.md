# PREREG-GAPS211 (STALE4 for account 4, account 1 worker; 4 Oct 2026, written 02:08 UTC (clock read) before any statistic below was computed)

Job: GAPS211, account 4's claim of 3 Oct 2026 19:18 UTC (no done line, nothing pushed; taken over under STALE4,
.claude/briefs/runs/2026-10-04-acct3-stale4.md job 6). Step named in pollaky-1865-1875 and catokwacopa-1875 NOTES.md
Verdicts: re-run T' (gaps205_content.py) with its controls at the published 3-12-letter omission budget, so that
GAPS205's "not detected" (p 0.254, power 0.95/1.00 at 0-3 omissions) either brackets the design or is logged untestable.

Statistic: **unchanged from GAPS205 Addendum A.** T' = sum over the 24 letter lines of pairs.tsv of
(M[i][i] - E[len a_i][len b_i]); M = best order-preserving merge under the same English letter-bigram model
(tools/data/en Huck Finn + Gatsby, add-0.5); E = the same Expect table (40 independent corpus subsample pairs, seed
2050). Code: gaps205_content.model / merge / Expect / ptest imported unmodified. Target: same 20,000 re-pairings,
seed 205 (so the target p must reproduce 0.253987 exactly; if it does not, stop and report).

Control family (the only change): pairs.synth's line generator with the omission count o drawn uniformly from
3..12 per line (instead of 0..3); everything else as pairs.synth (same 24 total line lengths, same corpus, same coin
and half dealers). Arms as GAPS205: P-coin, P-half (true pairs; power = share of texts with p < 0.001) and U-half
(halves from two independent synthetic texts; FPR = share with p < 0.05); 20 texts per arm, 2,000 permutations each,
seeds 211000 + 1000*arm + c. The control can differ from the target on T' by construction (content and omission
change the merge score; the target is fixed).

Secondary, descriptive only (no gate attached): the same three arms at fixed omission bands o in 3..5, 6..8, 9..12,
10 texts per arm each, to show where power falls if it falls.

Gate (decided now, same thresholds as GAPS205):
  - Valid test only if max(P-coin, P-half) power >= 0.5 and U-half FPR <= 0.15 at the 3-12 primary arms.
  - Valid and target p >= 0.05: **not detected at the design's omission budget** (control-backed for T' only;
    no bearing on any reading).
  - Valid and target p < 0.001: supported. Otherwise inconclusive.
  - Not valid: T' is **untestable at the 3-12 omission budget at N = 24 lines** (rule 3: GAPS205's 0-3 negative then
    does not bracket the design and is not a design negative). No further variant of T' under this job.
No reading is attempted; nothing is graded (rule 4 n/a). Reproduce: `python3 gaps211_content.py --check`.
