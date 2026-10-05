# PREREG-MANT27 (D2B-MANT27, 5 Oct 2026, written 23:36 UTC by date -u, account 2), before any pass was read or any statistic computed

Leaf: SHStA Dresden 10026 Loc. 694/08 ff.422v-423, URL file 0527 (film label 0528; sha256 bfd3ce7d...87d5). Folio confirmed by
this worker from the frame: right page carries "423" at its head; file 0528 (label 0529) shows "424" with "877 Bartholdi" at its
head = GAPS195's leaf, i.e. GAPS195 read ff.423v-424 (N9-MANT2's flag confirmed). Nothing on this leaf was transcribed before.

Material: crops by tools/iiif_lines.py --image 0527.jpg --region 860,1080,1260,1660 --prefix L and --region 2110,1040,1250,1680
--prefix R, --distance 40 --lines-per-crop 3 (f422v_0527/crops/). Two blind Sonnet passes per page (A in order, B in reverse
order), crop paths only; reconciled by the worker against the crops (one reconciliation unit). A "glossed run" = a maximal run of
code groups with a period interlinear gloss above some part of it.

Pairs, aligner, statistic, control: identical to PREREG-GAPS195 + addendum and PREREG-MANT5 (the folder's current standard):
one pair per glossed run (plain = gloss as reconciled; where pieces sit over parts of a run, the pieces joined in order),
tools/interlinear_align.py align --floor 0 --max-chunk 14 --seg-bonus 1.0 --len-prior 0.5, no --prior; gloss normalisation by
f0500_0502/gloss_norm.tsv (r, pr, pol); any further abbreviation found in this leaf's reconciled glosses is added to a local
gloss_norm_0527.tsv only from the gloss strings themselves and before the first score (logged here as an addendum).
S = share of codes with >= 2 glossed positions whose aligned chunks are identical at every occurrence; S_multi = same over codes
occurring inside multi-code runs; also reported (per-class, AX-NAMES lesson): S_single = same over codes with >= 2 occurrences as
single-code glossed runs. Control: gloss strings permuted across the glossed runs, re-aligned identically, 200 draws, seed 527.
Gate: N_rec >= 3 AND S_real > p95(S_shuffle) strictly -> PASS; tie or miss -> leaf HELD, values to leaf_values_0527.tsv at M,
nothing into key.tsv.
Licensed on PASS (GAPS195 shape): only single-code glosses (code under its own gloss) -> C if the gloss read is C, M if the gloss
read is M; multi-code chunks stay M in leaf_values_0527.tsv, not key.tsv. A gloss contradicting an existing key.tsv value is not
overwritten: logged in HYPOTHESES.md as a data conflict with both witnesses (rule 4). Single-code glosses vs existing key.tsv
values reported (agree/disagree) as a known-answer side check, not a gate.
