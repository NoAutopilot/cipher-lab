# PREREG R9-NOX: exact-LCS variant of test0 (written 6 Oct 2026 06:11 UTC by date -u, before any LCS score was computed)

Worker R9-NOX (LANE LANE-RUN9-account-1). Why: R7A-NOX262 found test0's difflib ratio swings 0.23 on pass B for a two-letter gloss
change (L13 quil -> quon); its exact LCS ratio 2*LCS/(|dec|+|gloss|) stayed 0.5575. This re-scores the same inputs with that statistic.

Statistic: R_lcs = 2*LCS(dec, gloss) / (len(dec) + len(gloss)), exact longest common subsequence on test0's normalised letters
(same norm(), same decode(), same '#' handling). Added to scripts/test0.py as `--stat lcs`; the default (`--stat difflib`) is unchanged so
every committed results_*.json still passes `--check`.

Nulls: unchanged from test0 -- 200 key shuffles and 200 gloss-word-order shuffles, Random(16142), same draw order; scored with R_lcs.

Inputs (unchanged): gloss.tsv as at commit 24a793937; witness/c262_passA.tsv, c262_passB.tsv, c262rc_passC.tsv, c262rc_passD.tsv,
c262rc_recon.tsv; --hash e and --hash o. Outputs witness/results_lcs_<pass>_<e|o>.json.

Gate (same rule as witness/gate_recut.txt, statistic swapped): PASS if the gate pass (c262rc_passD) beats the MAX of BOTH nulls at BOTH
'#' resolutions; else "non-test at this transcription error". Passes A, B, C and reconciled are reported, not gated (pass B was FT-D's gate
pass; reported beside D with its own both-nulls-max result, as before).

Stability check (secondary, pre-registered): rebuild the pre-R7A gloss (L09 'treuve' -> 'trouve', L13 'quon' -> 'quil') in scratch and
score every pass x hash under both statistics. STABLE if every |R_lcs(new) - R_lcs(old)| <= 0.02; the difflib swings are reported beside.

What a result licenses: a PASS under R_lcs says the gate verdict does not depend on difflib's greedy anchoring; a FAIL where difflib
passed says the earlier PASS rested on the greedy statistic and test0's known-answer gate is reported as not met under the exact
statistic. Neither changes depth/N-class (verifier's job). No other input or threshold is changed after scores are seen.
