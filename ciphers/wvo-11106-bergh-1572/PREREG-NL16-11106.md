# PREREG NL16-11106 (LANE FAMILY, account 2), written 8 Oct 2026 before any NL16-11106 family score was computed

Target: tx/ciphertext_oneline.txt (N 820, K 41, FAM-11106T), the same cipher, K and N as FAM-11106L's fr16/de1600/la17 rows.
Spec copy specs/wvo-11106-bergh-1572-nl16.json (judge language nl16; tools/data/nl16, built by this job).
Family `homophonic`, `--tokens space --param profile=target --param noise=0.10 --measured-error 0.10 --gate 0.6`, restarts 8,
`--seeds 6`, `--decode-tag nl16`. Control first; the target runs only if the control mean >= 0.6 (the tool enforces this).
Attempt count: homophonic Dutch K41 is attempt 1.

Known before scoring (tools/data/nl16 holdout_check.py, logs in tools/data/nl16/): leave-one-file-out false-negative rate against
the in-model real_p05 is 81.5% at N=820 (folds 95.0, 94.0, 43.5, 98.0, 77.0) and 62.3% at N=200. The judge's real_p05 gate
therefore rejects most genuine unseen 1569-1589 Dutch at this length: a target FAIL against real_p05 alone is NOT a negative.

Placement rule (fixed now): under the full nl16 model, score 200 windows of N=820 drawn from DBNL cice001offi01 (Coornhert's
Officia Ciceronis, 1561, out of corpus) -> its 5th percentile `offi_p05` (script tools/data/nl16/offi_calibration.py, run after
this file is pushed). Then:
- control mean < 0.6 -> non-test (no target).
- control at gate, target judge PASS, or target judge score >= offi_p05 -> a candidate; then one `--shuffle-target 1` run at the
  same settings; a shuffled decode that also reaches offi_p05 voids it. A surviving candidate goes to the lane for a verifier.
- control at gate, target score < offi_p05 AND target best anneal score worse than every passing control seed's anneal score ->
  control-backed negative for homophonic Dutch K41 (conditional on the provisional transcription).
- otherwise -> "judge cannot decide" (logged, not a negative).
