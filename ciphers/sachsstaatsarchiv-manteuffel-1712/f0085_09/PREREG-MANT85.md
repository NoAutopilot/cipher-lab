# PREREG-MANT85 (R13-MANT85, 6 Oct 2026, written 18:12 UTC by date -u, LANE LANE-RUN13-account-4, account 4), before any pass was read or any statistic computed

Leaf unit "0085_09": SHStA Dresden 10026 Loc. 694/09, URL file 0085 (film label 0086; sha256 d99e49ad...c499dae7c; www.archiv.sachsen.de,
1 request, HTTP 200). Two written pages; the left page (end of a letter, signed) carries a block of dotted code runs with interlinear
glosses (R13-MANTSCR screen: ~8 runs, "Grumbkow" over 7.60, values to 483/501, M). Nothing on this leaf was transcribed before.
The worker has seen only a 0.25x overview before this file was written.

Material: crops by tools/iiif_lines.py --image 0085.jpg --out crops --region <left-page code block, native px, pasted in the addendum>
--prefix L --lines-per-crop 3 --debug, or, if band cuts fall through glosses, PIL full-width overlapping strips of the same box (declared
in the addendum). Crops in scratch, not committed (folder over 30 MB); the command, box and the frame URL in images/loc694-08-09/frames.tsv
regenerate them. Two blind Sonnet passes (A strips in order, B reversed), one call per pass, crop paths only, no candidate values or key;
reconciled by the worker against the strips and zooms (one unit). If A vs B split on more than 10% of code tokens, stop after reconciliation.

Per-leaf gate: identical to PREREG-MANT521 / PREREG-MANT526 (the GAPS195 shape): one pair per glossed line of code,
tools/interlinear_align.py align --floor 0 --max-chunk 14 --seg-bonus 1.0 --len-prior 0.5, MANT5 normalisation (+ gloss_norm_0085.tsv only
for abbreviations this leaf itself writes out in full over the same code, declared in an addendum before scoring), S / S_multi / S_single,
200 draws gloss permutation across glossed runs, seed 85; PASS iff N_rec >= 3 and S_real > p95 strictly; anything else HELD (tie or miss)
or FAIL. The control permutes gloss strings across runs, so it can change which chunk each recurring code receives (the statistic).
A light leaf: an N-floor HELD is the likely outcome and is reported as such.

Merge rule (brief R13-MANT85; CLAUDE.md rule 3 per-unit gate): only if this leaf's own gate PASSes may codes enter key.tsv, single-code
glosses only, graded M (C only where the leaf itself glosses a single code unambiguously AND the leaf passed), never overwriting a Krauske
row; conflicts with Krauske logged in HYPOTHESES.md with witnesses, never resolved by majority (rule 4). HELD/FAIL: nothing merges.
Known-answer (reported first, not a gate): every single-code gloss on this leaf whose code has a C value in key.tsv is scored
agree / compatible / disagree. The pooled gate (pooled_gate.py) is not run in this job (not in the brief).
