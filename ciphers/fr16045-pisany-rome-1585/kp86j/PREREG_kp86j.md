# PREREG kp86j -- fr16045 f.275v block B lines 12-15 (L17-L20): third blind reader + eye-reconcile, then kp86i re-run unchanged (D2-PIS275, 5-6 Oct 2026)

Written and pushed before reader C is run. Third attempt on these four lines; this one changes the material (the transcription), not the
instrument or the span, as RUN6-PISFIN's own next step names.

1. Reader C (blind): 4 Sonnet subagent calls, one per line, prompt = `sh tx86h/make_prompt.sh C Lnn` verbatim (tx86f brief and sign sheet
   unchanged, crops images/f275vB2_L01..L04_s1/_s2, cut by RUN6-PIS's pasted iiif_lines.py command; no new crop). Reader C sees no earlier pass.
   Replies verbatim to tx86i/lines/C_Lnn.txt -> tx86i/local_passC.tsv. No re-ask.
2. err (fixed before any eye work): `python3 tools/reconcile_passes.py tx86h/local_ciphertext.tsv tx86i/local_passC.tsv --out-dir tx86i/cmp`;
   err_new = 1 - (C's agreement with the RUN6-PIS reconciled tokens over L17-L20). This is an independent reader against the prior
   reconciliation, the same shape as kp86h/kp86i's err (1 - two-reader agreement), not a 2-of-3 residual.
3. Eye-reconcile: only the positions listed in tx86i/cmp/disagreements.tsv are settled from the crops by the worker, choosing among the
   readings already present (R, A, B, C) or `?`; every other token stays as tx86h/local_ciphertext.tsv. -> tx86i/local_ciphertext.tsv,
   with a change log tx86i/reconcile_log.tsv (line, pos, old, new, why). Done without decoding and without the key or the copy open.
4. Test: kp86j/kp86j.py = kp86i/kp86i.py with tokens tx86i/local_ciphertext.tsv, extra tx86h/local_passA.tsv tx86h/local_passB.tsv
   tx86i/local_passC.tsv, outputs kp86j_*; COPY = kp86i/colbert_f275v.txt (unchanged); kp86d statistic, nulls, seeds, arms A/B, positive
   control and gate unchanged. `python3 kp86j/kp86j.py --local --err <err_new> --inms "<kp86h phrase>"` -> kp86j/kp86j_local_result.json,
   log kp86j/kp86j_local_run.log. One run, no parameter change after it. If err_new > 0.223, run at err_new anyway (harsher control).
5. Gate per arm (as kp86d-i): PASS if the reconciled target > p99 of both nulls AND that arm's control passes; control fails -> NON-TEST;
   target fails at err > 0.10 with control passing -> FAIL at that e. Arm A gates grades; arm B reported beside it only.
6. Grades: arm A PASS -> L17-L20 tokens regraded C where the decoded letter aligns identically to the copy, T31 tokens M, by
   kp86h/grades_f275v_h.py logic with the kp86i copy and the tx86i tokens on L17-L20 rows only (written as tx86i grades, L01-L16 stay kp86h's).
   FAIL/NON-TEST -> L17-L20 stay M; kp86h/grades_f275v.tsv stands. A FAIL here is the third attempt with the kp86d instrument on these lines:
   logged per rule 3's third-attempt clause as untestable by kp86d at this N (187 letters), not refuted.
