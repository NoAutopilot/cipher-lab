# PREREG-D1A-SUR -- pooled [ij] class test, inv. 373 scans 0746 + 0758 (control off ceiling by n, gate unchanged)

Written 8 Oct 2026 05:51 UTC (date -u read 05:50), pushed alone before pool_run.py exists or any pooled number is computed.
LANE DEFAULT-account-1-20261008-0540, job D1A-SUR (account 1). Second [ij] attempt (NZ-SURIJ was the first gated one; R15-SUR758
a non-test at n 4). Rule 3 third-attempt clause: change n, not the gate or the instrument.

## Units (fixed, no new image labels)
The image-dotted ij forms already labelled by eye on the two inv. 373 scans that are held OUT of T (T = 0693+0702+0730 sign tables):
- 0746: the 6 `IJ` units of ../inv373_0746_tok_nz/labels.tsv (NZ-SURIJ, 7 Oct 2026).
- 0758: the 4 `ONE` units of ../inv373_0758_tok_r15/labels.tsv (R15-SUR758, 6 Oct 2026).
Pooled n = 10. 0693/0702/0730 are not searched for further dotted forms: they build T, so a class test on them is not held out, and
re-cutting their crops would be a new vision unit this brief does not need for n >= 10.

## Known before this test (not blind)
The per-scan target counts are already on file: 0746 6/6 on m|n, 0758 4/4 on m|n. What is NOT yet known is the pooled C1 null at n 10.
This test therefore asks one question only: is 10/10 outside a deranged-gloss null at n 10 (it could not be at n 6 or n 4, where the
null p99 was 1.000). The descriptive plain-y figure (0746: 45/47 m|n) already says the dotted form and the undotted y-form share a value
class; a PASS licenses "the dotted ij form is a member of the [y-fam] m|n class", not a separate value and not a key-file row.

## Instrument (unchanged)
Both scans scored exactly as their own retok_run.py did (R15-SURALIAS alias_run.py driver -> R14-SURDP dp_align.py, T as above +
[sh-lig]={h}); C1 = 1,000 deranged-gloss draws per scan with that scan's own seed (746, 758). Pooled C1 draw i = (agree_0746,i +
agree_0758,i) / (n_al_0746,i + n_al_0758,i), the two scans' draws being independent. Pooled real share = (6+4 agreeing)/(n_al 0746 +
n_al 0758) as re-computed by the script.

## Control-first step (stop rule)
pool_run.py prints the pooled C1 class-share distribution (mean, p95, p99, max) BEFORE the pooled real share. If pooled C1 p99 >= 1.000
(still at ceiling at n 10), stop: "untestable at this n" logged, the real share is not used, rule 3 third-attempt clause logged
(untested-by-this-tool at n 10). The control CAN differ from the target: deranging the gloss moves which letters face the tagged positions.

## Gate (same as NZ-SURIJ, applied to the pooled class)
PASS iff pooled n_al >= 10 and pooled share >= 0.60 and pooled share > pooled C1 p99, AND each scan's own scan-level check still holds
(A after >= A before - 0.010 and SAME SYSTEM (DP)). n_al < 10 pooled: non-test. Otherwise FAIL.
Per-unit caveat (CLAUDE.md rule 3, per-unit merge paragraph): neither scan cleared its own control alone (both non-discriminating at
ceiling, not failed); a pooled PASS is logged as a pooled-class result, graded S only inside inv. 373 passes, never merged into key.tsv,
key_period_*.tsv or conflicts.tsv by this job (verifier decides; ROOM flag).

## Unit 2 (only if unit 1 finishes under 50% of cap and box)
The [d-loop][s-loop] one-tile step-2 look, with a same-hand known-same control (two whole 0758 SH crops); counts only if known-same is
SAME and known-different is DIFFERENT. Descriptive; no alias or key entry.
