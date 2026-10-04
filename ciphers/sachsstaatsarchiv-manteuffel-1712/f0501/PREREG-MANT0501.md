# PREREG-MANT0501 (4 Oct 2026, written 09:26 UTC by the clock, RUN3-MANT, account 1), before any pass or statistic

Leaf: SHStA Dresden 10026 Loc. 694/08, film frame 0501 (sha256 prefix b27f0809877381af, as GAPS207). Material: crops from
`tools/iiif_lines.py --image` (one crop per code line, gloss margin above), two blind Sonnet passes, reconciled by the worker
against the crops. Unit: a "glossed run" = a maximal run of code groups with a period interlinear gloss above it.

Identical to PREREG-GAPS195 (f423_0528/PREREG-GAPS195.md incl. its addendum), applied to this leaf alone:
- pairs = one per glossed run; `tools/interlinear_align.py align --floor 0 --max-chunk 14 --seg-bonus 1.0 --len-prior 0.5`, no --prior.
- S = among codes with >= 2 glossed positions on this leaf, share whose aligned chunks are identical at every occurrence;
  S_multi = same restricted to codes occurring inside multi-code runs (AX-NAMES per-class lesson).
- Control: gloss strings permuted across glossed runs (pairing shuffle; this varies the code/gloss pairing S measures, so S
  can differ under it), re-aligned with identical options, 200 draws, seed 501.
- Gate: merge into key.tsv only if N_recurring >= 3 AND S_real > p95(S_shuffle) strictly. Tie, miss or N_recurring < 3 =
  leaf HELD: values to f0501/leaf_values.tsv at grade M, nothing into key.tsv (rule 3 Szembek paragraph).
- Grades if the gate passes: code under a single-code gloss -> C; code inside a multi-code run whose chunk agrees at >= 2
  occurrences -> C; any other multi-code chunk -> M. A gloss contradicting an existing key.tsv value is not overwritten:
  logged in HYPOTHESES.md as a data conflict with both witnesses (rule 4).
- Per-class breakdown reported (single-code vs multi-code glosses). Also reported, not a gate: single-code glosses vs
  key.tsv / Krauske (agree / disagree / new).
Expected small-N risk, stated in advance: if this leaf has < 3 codes recurring under glosses, the gate cannot pass by
construction of its N floor and the leaf is HELD regardless of agreement.
