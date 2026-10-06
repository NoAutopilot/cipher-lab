# PREREG-MANT530 (R8-MANT530, 6 Oct 2026, written 04:40 UTC by date -u, LANE LANE-RUN8-account-4, account 4), before any pass was read or any statistic computed

Leaf unit "0530": SHStA Dresden 10026 Loc. 694/08 ff.425v-426, URL file 0530 (film label 0531, sha256 9cb00628...f2c0bc1,
www.archiv.sachsen.de, 1 request, HTTP 200). Folio check: the right page carries "426" top right under "ce 24 nov. 1712." (read at native,
crop 3100,1000,3400,1120); the left page is f.425v by sequence (URL file 0529 = ff.424v-425, R7-MANT529). The left page continues 0529's
letter (paragraphs 8-9); the right page is the "P.S." dated 24 Nov 1712. Nothing on this leaf was transcribed before (R7-MANTSCR eye screen
only, grade M).

Material: crops by
  tools/iiif_lines.py --image 0530.jpg --region 880,1030,1250,1680 --prefix L --distance 40 --lines-per-crop 3 --debug   (9 bands)
  tools/iiif_lines.py --image 0530.jpg --region 2130,1010,1250,1660 --prefix R --distance 40 --lines-per-crop 3 --debug  (8 bands)
L_L01 re-cut by PIL at native box 880,995,2130,1215 (the tool's band clipped the top gloss line). Crops kept in scratch, not committed
(folder over 30 MB); the commands, box and the frame URL in images/loc694-08-09/frames.tsv regenerate them. Two blind Sonnet passes per
page (A crops in order, B crops in reversed order), one page per call, crop paths only, no candidate values or key; reconciled by the
worker against the crops and zooms (one unit).

Per-leaf gate: identical to PREREG-MANT529 / PREREG-MANT27 (pairs = one per glossed run, tools/interlinear_align.py align --floor 0
--max-chunk 14 --seg-bonus 1.0 --len-prior 0.5, MANT5 normalisation (+ a gloss_norm_0530.tsv only for abbreviations this leaf itself
writes out in full over the same code, declared in an addendum before scoring), S / S_multi / S_single, 200 draws gloss permutation across
glossed runs, seed 530; PASS iff N_rec >= 3 and S_real > p95 strictly). Expected from the eye screen: a light leaf (about 10 glossed runs),
so an N-floor HELD is the likely per-leaf outcome and is reported as such, not as a miss. Licensing per PREREG-MANT27 (single-code glosses
only; never overwrite a Krauske row; conflicts to HYPOTHESES.md); per-unit merge rule: a code attested only on leaves that tie or miss
their own control stays M.

Addendum to PREREG-MANTP (pooled gate), registered here before scoring: leaf 0530 (pairs from f425v_0530/pairs.tsv, grades from
f425v_0530/reconciled.tsv) is appended to pooled_gate.py's LEAVES after 0529 (option --add0530, implies --add0529), outputs with suffix
_0530; it is not prior-cleared; statistic, MANT5 normalisation, control (1000 draws, seed 7101), gate, per-leaf rule (seed 7101 + 530),
licensing rules unchanged; the pooled input carries R8-MANT's 0527 run-7 correction (848), as r8mant/*_r8 did. Reported beside R8-MANT's
6-leaf result (0.750 vs p95 0.167). The specific question: does 864, 783, 867, 939, 357 or 107 gain a further single-code attestation
that agrees, and does any code that so far sits only on uncleared leaves (898, 867, 783) recur here?

Known-answer (reported first, not a gate): every single-code gloss on this leaf whose code has a C value in key.tsv is scored
agree / compatible / disagree. If the two passes split on more than 10% of code tokens, stop after reconciliation (brief).

## Addendum (6 Oct 2026, 04:56 UTC by date -u), after reconciliation, before any alignment or score
Reconciled: 12 runs, 44 code tokens (f.425v 10 runs / 32 tokens, f.426 2 runs / 12 tokens), 11 glossed, 4 of them single-code (107, 864 x2,
357) (reconciled.tsv, pairs.tsv). Pass agreement A vs B by token alignment: f.425v 30/32 (0.938; yy vs 44, 71 vs 74), f.426 11/11 (A adds a
doubtful single "4"), under the 10% stop line; each pass vs the reconciled text f.425v 26/32 and 28/32, f.426 11/11. Worker zooms settled
the hand's open y-form as 4 (as on 0529): 5y2 542, 10y 104, 28y 284, 7y 74 (both passes 592, 109, 289, 77). Passes ran "754. 864" as one
run; the gloss's own full stop ("exclus le Roy. Le Roy de Prusse") and the clause split it (runs 7, 8). Run 5's gloss: passes "le Roy de
Suede" (uncertain), worker zoom "le Roy de Prusse" -> M; run 9 "Ilgen" read by the worker only -> M. No abbreviation written out in full
over the same code on this leaf, so no gloss_norm_0530.tsv: MANT5 normalisation only. Dropped from pairs: run 12 (unglossed single "4").
Expected: S_single over 864 (2 occurrences, both "le Roy de Prusse") and the per-leaf gate at the N floor (N_rec likely < 3) -> HELD (N floor).
