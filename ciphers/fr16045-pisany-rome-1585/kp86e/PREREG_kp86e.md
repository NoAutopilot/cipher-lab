# PREREG kp86e -- fr16045 f.275r (4 Nov 1586) per-line re-pass vs Colbert 16 pt II pp.121-123 (RUN5-PIS3, 4 Oct 2026)

Written and pushed before any blind pass of f.275r in this job and before any decode of the new files.

Why a second attempt: kp86d (RUN4-PIS2) was NON-TEST because its positive control failed at err_2reader 0.756; each reader
read all 30 crops in one call and B's line breaks drifted. The instrument changes (rule 3, third-attempt clause): ONE LINE PER
READER CALL, so a reader cannot drift across lines. Nothing else changes. If kp86e is again NON-TEST, the f.275r re-pass step
is logged [retired] for one-call readers and the next step names new material; there is no third tuning of the same knob.

Material.
- Same cipher, same clear copy, same keys as kp86d/PREREG_kp86d.md (c562 f.275r; kp86d/colbert_p121_123.txt; arm A key86.tsv
  as published, arm B key86 + RUN4-PIS1 remap T31->o, T45->u, T47->f, T57->n, reported beside A, never in place of it).
- Crops re-cut from the cached native region (0 Gallica requests), one line per band:
  `python3 tools/iiif_lines.py --image ciphers/fr16045-pisany-rome-1585/images/src_ark_12148_btv1b9060906j_f562_900_2600_2850_2520.jpg --out ciphers/fr16045-pisany-rome-1585/images --prefix f275rL --debug --max-width 1600 --overlap 100 --centres 114,274,441,616,762,934,1101,1277,1446,1607,1821,1978,2124,2263,2425 --follow-slope 400 --slope-local --slope-margin 20 --only-lines 2,3,4,5,6,7,9,10,11,12,13,14,15`
  then L01 and L08 fixed-y (their slope fits jumped to the neighbouring line on the first run; montage checked):
  `python3 tools/iiif_lines.py --image <same src> --out <same> --prefix f275rL --max-width 1600 --overlap 100 --centres <same 15> --only-lines 1,8`
  Montage of all 30 crops checked by eye: each crop's middle row is its own line. L01 s1 is clear handwriting only (not given
  to readers); L01 s2 ends in 2 cipher signs; L07 s2 is cipher "...a07." then clear "Mais croyant que Monsieur de"; L08 starts
  with clear "Luxembourg".

Transcription: two blind Sonnet readers (A, B), tx86e/PASS_BRIEF86e.md, one subagent call per line per reader (15 + 15
calls; L01 gets s2 only), each call given only that line's crops and tx86e/SIGNSHEET86.png (copied unchanged). Replies
collected verbatim into tx86e/lines/A_Lnn.txt, B_Lnn.txt and assembled to tx86e/passA.tsv, passB.tsv. A reply that is not a
label row (refusal, wrong line number) is re-asked once with the same prompt; the second reply stands.
Reconciliation: `python3 tools/reconcile_passes.py tx86e/passA.tsv tx86e/passB.tsv --out tx86e` then
`python3 kp86d/reconcile_d.py tx86e` (RUN3 shape rules, unchanged) -> tx86e/ciphertext_f275r.tsv. No sign-by-sign judgement.
err_2reader = 1 - agree share from reconcile_passes.py.

Test: `python3 kp86e/kp86e.py --err <measured err_2reader>` = kp86d/kp86d.py UNCHANGED (statistic tools/stream_align
nw_score via kp86/kp86.py; key-shuffle 1000 and order-shuffle 1000 nulls, p99; seeds as in kp86d; positive control: copy span
with the in-clear phrase removed, enciphered with the arm's key at the measured err, 5 seeds, 200/200 nulls, pass >= 4/5)
-> kp86e/kp86e_result.json.
Gate per arm (as kp86d): PASS if the reconciled target > p99 of both nulls AND that arm's control passes; control fails ->
NON-TEST; target fails at err > 0.10 with the control passing -> FAIL at that e (not a refutation of the table).
Blind A and B scored too (not gating).

Grades (rule 4): only if arm A is a licensed PASS, decoded letters aligned identically to the copy are C (known plaintext),
the rest M; T31 tokens are M wherever the letter they yield is not settled by the copy alignment (key86 T31 data conflict,
HYPOTHESES.md). If NON-TEST, every token stays M. `tools/decode_key.py ... --check` on the committed reading.
No parameter changes after the first run.
