# PREREG-MANT518 (R10-MANT518, 6 Oct 2026, written 10:42 UTC by date -u, LANE LANE-RUN10-account-4, account 4), before any pass was read or any statistic computed

Leaf unit "0518": SHStA Dresden 10026 Loc. 694/08, URL file 0518 (film label 0519, sha256 61261688...c002c71a9a178, www.archiv.sachsen.de,
1 request, HTTP 200). Two written pages: left (f.416 per N9-MANT2, paras 3-4, ~30 lines, the lower half dense with code groups and glosses),
right (top ~6 lines, codes in two lines). Earlier work on this leaf: N9-MANT2 eye-read 71 groups at M (no file kept; "le Pr. de Dessau" over
391.103..); R7-MANTSCR / R10-MANTSCR screen (U codes 402 404 398 391 400). The worker has seen only a 0.25x overview before this file was written.

Material: crops by
  tools/iiif_lines.py --image 0518.jpg --out crops --region <page text box, native px, pasted in the addendum> --prefix L|R --distance 40 --lines-per-crop 3 --debug
(or, if the line finder misses lines or cuts through glosses, PIL full-width overlapping strips of the same boxes, declared in the addendum).
Crops kept in scratch, not committed (folder over 30 MB); command, boxes and the frame URL in images/loc694-08-09/frames.tsv regenerate them.
Two blind Sonnet passes (A strips in order, B reversed), one call per pass, strip paths only, no candidate values or key; reconciled by the
worker against the strips and zooms (one unit). If A vs B split on more than 10% of code tokens, stop after reconciliation.

Per-leaf gate: identical to PREREG-MANT521 / PREREG-MANT526 (GAPS195 shape): pairs = one per glossed run (one per glossed line of code
when a run spans lines and is glossed line by line), tools/interlinear_align.py align --floor 0 --max-chunk 14 --seg-bonus 1.0
--len-prior 0.5, MANT5 normalisation (+ gloss_norm_0518.tsv only for abbreviations this leaf itself writes out in full over the same code,
declared in an addendum before scoring), S / S_multi / S_single, 200 draws gloss permutation across glossed runs, seed 518; PASS iff
N_rec >= 3 and S_real > p95 strictly. The control permutes gloss strings across runs, so it can change which chunk each recurring code
receives (the statistic). Licensing per PREREG-MANT27 (single-code glosses only; never overwrite a Krauske row; conflicts to HYPOTHESES.md,
not resolved by majority); per-unit merge rule: a code attested only on leaves that tie or miss their own control stays M. Codes that pass
enter key.tsv at M only (brief R10-MANT518).

Addendum to PREREG-MANTP (pooled gate), registered here before scoring: leaf 0518 (pairs from f0518/pairs.tsv, grades from
f0518/reconciled.tsv) is appended to pooled_gate.py's LEAVES after 0521 (option --add0518, implies --add0521), not prior-cleared;
statistic, MANT5 normalisation, control (1000 draws, seed 7101), gate, per-leaf rule (seed 7101 + leaf), licensing rules unchanged.
Run twice and both reported: as registered (MANT5, suffix _0518) and with rule SP (r10mantscr/PREREG-R10-MANTSCR.md; --sp, suffix
_0518sp), the licensing run. Compared beside R10-MANT521's 10-leaf result (SP: 0.833 vs p95 0.083).

Known-answer (reported first, not a gate): every single-code gloss on this leaf whose code has a C value in key.tsv is scored
agree / compatible / disagree.

## Addendum (6 Oct 2026, 10:50 UTC by date -u), after reconciliation, before any alignment or score
Crops (pasted): `tools/iiif_lines.py --image 0518.jpg --out crops --region 870,1100,1260,1650 --prefix L --distance 40 --lines-per-crop 3 --debug`
found 21 of ~30 left-page lines in 7 bands; as on 0521/0526 the bands cut through glosses, so PIL overlapping full-width strips were used:
left (870,1100+220k,2130,min(+300,2760)) k=0..7 (S01-S08), right (2130,1100+220k,3350,+300) k=0..1 (S09-S10). Passes got strip paths only
(A in order, B reversed). Reconciled: 12 runs, 210 code tokens; A vs B 200/210 (0.952), under the 10% stop line. Worker zooms 2x on 11 areas.
Disclosure: the worker looked up key.tsv values for the reconciled runs (to prepare the known-answer report) BEFORE zooming run 10's
gloss; that zoom reading ('Manteuffel le charg...') is therefore not independent and is not used: run 10's gloss is the passes' reading.
Every other gloss reading was settled from passes and zooms taken before the lookup.
Pairing: one pair per glossed run (10 runs; the multi-line runs here are glossed in fragments over parts of lines, not word for word per
line, so the run, not the line, is the unit). Codes written above codes ('402' over 110, '259' between lines of run 1) are not paired.
Runs 11-12 unglossed. Normalisation: MANT5 only, no gloss_norm_0518.tsv. No single-code glossed run on this leaf, so the pooled
single-code gate cannot change by construction; it is run as registered anyway and reported.
