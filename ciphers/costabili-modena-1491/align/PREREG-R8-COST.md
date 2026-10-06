# PREREG R8-COST, 6 Oct 2026 (written and pushed before any P4 crop is cut or read)

Target: R1166 P4 (b.2/20 no.16, 21 Jun 1491), image scratch-only, sha1 7d53e868ad1cd5a2cd98a2147877c08d4fd1163b = images_manifest.tsv
(re-fetched 6 Oct 2026 04:07 UTC, one DECODE browser login, one file).
Instrument: the N8-COS group-crop instrument, unchanged except the label list now carries `W` (align/labels.tsv, N9-COS2). The worker
cuts boxes from the page geometry around the cipher spans of P4 (a box holds one to three cipher groups and any interlinear writing
directly above them, nothing of the line below), commits them as `align/r8cost_boxes.tsv` with the crop command before the first reader
call, and passes the readers no value, gloss text or key. Readers: two blind Sonnet calls, pass A (crops in page order) and pass B
(reverse order), labels.tsv shapes and the RUN3-COSK2 dash convention (dash dropped except dash+z = `Z` and dash+open loop = `W`).
Per crop: gloss (small writing above, if any) and signs (groups separated by spaces).
Measured:
 (1) err_2reader = sign-level disagreement between A and B on groups both read with equal length (difflib-aligned otherwise).
 (2) C coverage = share of P4 cipher sign tokens that (a) A and B read identically at the aligned position and (b) carry a C value in
     align/key_n9cos2.tsv (+ a, T d, a i, b o, c p, d r, g l, o e, y n, z o, W t). Denominator: all aligned sign positions of both passes
     (a disagreement or an indel counts as not covered).
Decode gate (from PREREG-N8-COS, unchanged): P4 is decoded as a running reading only if C coverage >= 0.80. Below 0.80 the reading is not
written; the coverage, err_2reader and the per-sign shortfall are logged and P4 stays "transcribed, not decoded".
Held-out check (reported, licenses nothing): where a P4 group carries interlinear gloss, its decode under the C key is compared to the gloss
letter by letter; the key is not changed from it.
Grading of any decoded token: C where the sign is C in key_n9cos2.tsv and both passes agree; M otherwise. No key value changes in this job.
Reconciliation by this worker (glosses in view) is reported and licenses M at most.
