# PREREG-MANT526 (R10-MANT526, 6 Oct 2026, written 09:44 UTC by date -u, LANE LANE-RUN10-account-4, account 4), before any pass was read or any statistic computed

Leaf unit "0526": SHStA Dresden 10026 Loc. 694/08 f.422 (URL file 0526, film label 0527, sha256 29882479...4c776c309c,
www.archiv.sachsen.de, 1 request, HTTP 200). One written page (right; "422" and "ce 24 nov. 1712" at its head on the overview), the left
page blank (a cover/verso). Recto of the 0527 leaf (ff.422v-423, D2B-MANT27): the same letter of 24 Nov 1712. Nothing on this leaf was
transcribed before (R7-MANTSCR eye screen only: codes 402 447 560 237 106 403 285 143 108 384 583 714 272 seen, ~15 runs, 898/939/867 not seen).

Material: crops by
  tools/iiif_lines.py --image 0526.jpg --region <right-page text block, native px, pasted in the addendum> --prefix R --distance 40 --lines-per-crop 3 --debug
Crops kept in scratch, not committed (folder over 30 MB); the command, box and the frame URL in images/loc694-08-09/frames.tsv
regenerate them. Two blind Sonnet passes (A crops in order, B crops reversed), one call per pass (one page), crop paths only, no candidate
values or key; reconciled by the worker against the crops and zooms (one unit). If A vs B split on more than 10% of code tokens, stop after
reconciliation.

Per-leaf gate: identical to PREREG-MANT530 / PREREG-MANT529 / PREREG-MANT27 (the GAPS195 shape run for 0528): pairs = one per glossed run,
tools/interlinear_align.py align --floor 0 --max-chunk 14 --seg-bonus 1.0 --len-prior 0.5, MANT5 normalisation (+ a gloss_norm_0526.tsv
only for abbreviations this leaf itself writes out in full over the same code, declared in an addendum before scoring), S / S_multi /
S_single, 200 draws gloss permutation across glossed runs, seed 526; PASS iff N_rec >= 3 and S_real > p95 strictly. The control permutes
gloss strings across runs, so it can change which chunk each recurring code receives (the statistic), not a non-test. A light leaf: an
N-floor HELD is the likely outcome and is reported as such, not as a miss.
Licensing per PREREG-MANT27 (single-code glosses only; never overwrite a Krauske row; conflicts to HYPOTHESES.md, not resolved by majority);
per-unit merge rule: a code attested only on leaves that tie or miss their own control stays M. Codes that pass enter key.tsv at M only
(brief R10-MANT526). The specific question: do 898 (l'Empire), 939 (le Mecklenbourg) or 867 (le Feldmarechal) occur here as single codes,
and do they agree?

Addendum to PREREG-MANTP (pooled gate), registered here before scoring: leaf 0526 (pairs from f422_0526/pairs.tsv, grades from
f422_0526/reconciled.tsv) is appended to pooled_gate.py's LEAVES after 0530 (option --add0526, implies --add0530), outputs with suffix
_0526; not prior-cleared; statistic, MANT5 normalisation, control (1000 draws, seed 7101), gate, per-leaf rule (seed 7101 + 526),
licensing rules unchanged. Reported beside R8-MANT530's 8-leaf result (0.750 vs p95 0.167).

Known-answer (reported first, not a gate): every single-code gloss on this leaf whose code has a C value in key.tsv is scored
agree / compatible / disagree.
