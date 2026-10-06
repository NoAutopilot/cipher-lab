# PREREG-MANT521 (R10-MANT521, 6 Oct 2026, written 10:20 UTC by date -u, LANE LANE-RUN10-account-4, account 4), before any pass was read or any statistic computed

Leaf unit "0521": SHStA Dresden 10026 Loc. 694/08, URL file 0521 (film label 0522, sha256 5b42d15f...bead46bea1b80abf6c1ab0,
www.archiv.sachsen.de, 1 request, HTTP 200). One written page (left: the end of a letter, ~14 lines, signed), right page blank.
Nothing on this leaf was transcribed before (R7-MANTSCR eye screen only; R10-MANTSCR rank 1: one glossed 3-line run with 714 553 555 549).
The worker has seen a 0.25x overview and one 1:1 view of the top six lines (to place the crop box) before this file was written.

Material: crops by
  tools/iiif_lines.py --image 0521.jpg --out crops --region <left-page text block, native px, pasted in the addendum> --prefix L --distance 40 --lines-per-crop 3 --debug
(or, if the line finder misses lines, PIL full-width overlapping strips of the same box, declared in the addendum). Crops kept in scratch,
not committed (folder over 30 MB); the command, box and the frame URL in images/loc694-08-09/frames.tsv regenerate them. Two blind Sonnet
passes (A crops in order, B crops reversed), one call per pass (one page), crop paths only, no candidate values or key; reconciled by the
worker against the crops and zooms (one unit). If A vs B split on more than 10% of code tokens, stop after reconciliation.

Per-leaf gate: identical to PREREG-MANT526 (the GAPS195 shape): pairs = one per glossed run, tools/interlinear_align.py align --floor 0
--max-chunk 14 --seg-bonus 1.0 --len-prior 0.5, MANT5 normalisation (+ a gloss_norm_0521.tsv only for abbreviations this leaf itself writes
out in full over the same code, declared in an addendum before scoring), S / S_multi / S_single, 200 draws gloss permutation across glossed
runs, seed 521; PASS iff N_rec >= 3 and S_real > p95 strictly. The control permutes gloss strings across runs, so it can change which chunk
each recurring code receives (the statistic). A light leaf (few glossed runs): an N-floor HELD is the likely outcome and is reported as
such, not as a miss.
Licensing per PREREG-MANT27 (single-code glosses only; never overwrite a Krauske row; conflicts to HYPOTHESES.md, not resolved by majority);
per-unit merge rule: a code attested only on leaves that tie or miss their own control stays M. Codes that pass enter key.tsv at M only
(brief R10-MANT521).

Addendum to PREREG-MANTP (pooled gate), registered here before scoring: leaf 0521 (pairs from f0521/pairs.tsv, grades from
f0521/reconciled.tsv) is appended to pooled_gate.py's LEAVES after 0526 (option --add0521, implies --add0526), not prior-cleared;
statistic, MANT5 normalisation, control (1000 draws, seed 7101), gate, per-leaf rule (seed 7101 + leaf), licensing rules unchanged.
Run twice and both reported: as registered (MANT5, suffix _0521) and with R10-MANTSCR's rule SP as registered in
r10mantscr/PREREG-R10-MANTSCR.md (--sp, suffix _0521sp), which is the licensing run (R10-MANTSCR's adopted normalisation, per the brief).
Compared beside R10-MANTSCR's 9-leaf result (SP: 0.833 vs p95 0.083).

Known-answer (reported first, not a gate): every single-code gloss on this leaf whose code has a C value in key.tsv is scored
agree / compatible / disagree.
