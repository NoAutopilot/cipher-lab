# PREREG-MANT85 (R13-MANT85, 6 Oct 2026, written 18:08 UTC by date -u, LANE LANE-RUN13-account-4, account 4), before any pass was read or any statistic computed

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

## Addendum (6 Oct 2026, 18:12 UTC by date -u), after reconciliation, before any alignment or score
Time in the heading corrected 18:12 -> 18:08 (the commit time of a40fb3c98; the typed time was wrong).
Crops (pasted): `tools/iiif_lines.py --image 0085.jpg --out crops --region 900,1340,1240,560 --prefix L --lines-per-crop 3 --debug` found
10 lines in 4 bands (pitch 49), but the debug overlay showed band cuts through the interlinear glosses, so the same box was cut by PIL into
4 overlapping full-width strips, native boxes (900,1340+120k,2140,+200) k=0..3 (S01-S04, 1240x200 px); passes got strip paths only (A in
order, B reversed). Worker zooms (2x, 8 tiles of the box) for reconciliation, scratch only.
Reconciled: 12 runs, 89 code tokens (reconciled.tsv). A vs B code splits 4/89 (0.955 agree: 66/6?5, 2/21, 63/66, 501/50.1), under the 10%
stop line. Most runs are letter range (<=120); the nomenclator-range values 483 (run 4), 501 and 349 (run 10) carry NO gloss over them.
Pairing (scored): one pair per glossed run, 11 pairs (pairs.tsv); run 10 continues run 9 across the line break with no gloss of its own,
while run 9's gloss ("... que perdu a ce changement") runs past the codes of its own line, so runs 9+10 form one pair. Declared secondary
(reported, not the gate): pairs_line.tsv, the strict one-pair-per-line form with run 10 left out. Run 5's gloss "geh de urck l m h m"
is paired with run 5 (its placement, M). Normalisation: MANT5 only, no gloss_norm_0085.tsv (the leaf writes no abbreviation out in full
over the same code). Seed 85, 200 draws, as registered.
