# PREREG-MANT463 (R7-MANT463, 6 Oct 2026, written 01:40 UTC by date -u, LANE LANE-RUN7-account-2, account 2), before any pass was read or any statistic computed

Leaf unit "0574": SHStA Dresden 10026 Loc. 694/08 ff.463-463v, one letter "Berlin ce 15 Xbre 1712". URL file 0574 (film label 0575,
sha256 5df616fb...8f26): right page carries "463" and the date at its head, left page blank/clear (f.462v). URL file 0575 (film label
0576, sha256 b405a80f...cd37): left page = f.463v (code groups in its upper third, glossed), right page "464" in clear (not read).
Folio labels confirmed by this worker from the frames (4x-reduced views, scratch). Nothing on this letter was transcribed before
(N9-MANT2 inventory rows only).

Material: crops by tools/iiif_lines.py --image 0574.jpg --region 2110,990,1260,1660 --prefix R and --image 0575.jpg --region
860,1240,1250,730 --prefix V, both --distance 40 --lines-per-crop 3 --debug (13 bands; kept in scratch, not committed: the folder is
already over 30 MB; the command and sha256 regenerate them). Two blind Sonnet passes (A in order, B reversed), one page per call,
crop paths only; reconciled by the worker against the crops (one unit).

Per-leaf gate: identical to PREREG-MANT27 (pairs = one per glossed run, tools/interlinear_align.py align --floor 0 --max-chunk 14
--seg-bonus 1.0 --len-prior 0.5, MANT5 normalisation, S / S_multi / S_single, 200 draws gloss permutation across glossed runs,
seed 463; PASS iff N_rec >= 3 and S_real > p95 strictly). Licensing per PREREG-MANT27 (single-code glosses only; never overwrite a
Krauske row; conflicts to HYPOTHESES.md).

Addendum to PREREG-MANTP (pooled gate), registered here before scoring: leaf 0574 (pairs from f463_0574/pairs.tsv, grades from
f463_0574/reconciled.tsv) is appended to pooled_gate.py's LEAVES; it is not prior-cleared; statistic, normalisation, control (1000
draws, seed 7101), gate, per-leaf rule (seed 7101 + 574) and licensing rules unchanged. The pooled result with 0574 added is reported
beside the R7-MANTP result without it.

Known-answer (not a gate, but reported first): every single-code gloss on this leaf whose code has a Krauske C value in key.tsv is
scored agree / compatible / disagree (names: same person or office; "S.M." compatible with a sovereign code).
If the two passes split on more than 10% of code tokens, stop after reconciliation (brief).
