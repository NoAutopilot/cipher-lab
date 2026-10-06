# PREREG-MANT529 (R7-MANT529, 6 Oct 2026, written 02:17 UTC by date -u, LANE LANE-RUN7-account-2, account 2), before any pass was read or any statistic computed

Leaf unit "0529": SHStA Dresden 10026 Loc. 694/08 ff.424v-425, URL file 0529 (film label 0530, sha256 eaec9f4d...2e181,
www.archiv.sachsen.de, 1 request, HTTP 200). No folio number is legible on either page at native (the right page's top-right "225."
is a code group, glossed area "renoncer a ses vastes conquestes"); the labels ff.424v (left) / 425 (right) are inferred from the
sequence (D2B-MANT27: URL file 0528's right page carries "424"), as R7-MANTSCR read them. Both pages are written in one hand,
glossed interlinearly; nothing on this leaf was transcribed before (R7-MANTSCR eye screen only, grade M).

Material: crops by
  tools/iiif_lines.py --image 0529.jpg --region 870,1150,1270,1690 --prefix L --distance 40 --lines-per-crop 3 --debug
  tools/iiif_lines.py --image 0529.jpg --region 2110,1110,1270,1720 --prefix R --distance 40 --lines-per-crop 3 --debug
(18 bands); the tool's edge bands cut the first/last written lines, so four bands were re-cut by PIL at full width with these native
boxes: L_L01 (870,1150,2140,1394), L_L09 (870,2601,2140,2800), L_L10 (870,2745,2140,2850), R_L01 (2110,1130,3380,1367),
R_L08 (2110,2655,3380,2850). Crops kept in scratch, not committed (folder already over 30 MB); the commands, boxes and the frame URL in
images/loc694-08-09/frames.tsv regenerate them. Two blind Sonnet passes (A in order, B reversed), one page per call, crop paths only;
reconciled by the worker against the crops (one unit).

Per-leaf gate: identical to PREREG-MANT27 / PREREG-MANT463 (pairs = one per glossed run, tools/interlinear_align.py align --floor 0
--max-chunk 14 --seg-bonus 1.0 --len-prior 0.5, MANT5 normalisation (+ a gloss_norm_0529.tsv only for abbreviations this leaf itself
writes out in full over the same code, declared in an addendum before scoring), S / S_multi / S_single, 200 draws gloss permutation
across glossed runs, seed 529; PASS iff N_rec >= 3 and S_real > p95 strictly). Licensing per PREREG-MANT27 (single-code glosses only;
never overwrite a Krauske row; conflicts to HYPOTHESES.md); per-unit merge rule: a code attested only on leaves that tie or miss their own
control stays M.

Addendum to PREREG-MANTP (pooled gate), registered here before scoring: leaf 0529 (pairs from f424v_0529/pairs.tsv, grades from
f424v_0529/reconciled.tsv) is appended to pooled_gate.py's LEAVES after 0574 (option --add0529, implies --add0574); it is not
prior-cleared; statistic, MANT5 normalisation, control (1000 draws, seed 7101), gate, per-leaf rule (seed 7101 + 529) and licensing
rules unchanged. Reported beside R7-MANTP (4 leaves) and R7-MANT463 (5 leaves). The specific question: do 898 (l'Empire, 0527) and 939
(le Mecklenbourg, 0527) gain a second single-code attestation that agrees?

Known-answer (reported first, not a gate): every single-code gloss on this leaf whose code has a Krauske C value in key.tsv is scored
agree / compatible / disagree. If the two passes split on more than 10% of code tokens, stop after reconciliation (brief).

## Addendum (6 Oct 2026, 02:20 UTC by date -u), after reconciliation, before any alignment or score
Reconciled: 31 runs, 147 code tokens, 29 glossed, 9 of them single-code (reconciled.tsv, pairs.tsv). Pass agreement by token alignment
A vs B: f.424v 93/99 (0.939), f.425 45/48 (0.938), under the 10% stop line; each pass vs the reconciled text 0.86 (f.424v), 0.915/0.894
(f.425). The hand writes 4 like y (as on 0574): 32y, 53y, 18y, 8y, 6y, 51y, 65y, 46y settled as 324, 534, 184, 84, 64, 514, 654, 464.
No abbreviation is written out in full over the same code on this leaf, so no gloss_norm_0529.tsv: MANT5 normalisation only, both gates.
Dropped from pairs: run 11 (no gloss), run 29 (gloss illegible), the struck group after run 7, and the unplaced "225." (f.425 top right).
