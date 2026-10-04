# PREREG-MANT4 (RUN5-MANT4, 4 Oct 2026, written 12:5x UTC by the clock, account 1), before any pass or statistic on the 0500/0502 glosses

Leaves: SHStA Dresden 10026 Loc. 694/08, film frames 0500 and 0502 (sha256 prefixes f23775930c241a0e, 8b32e44d8fe573e3, RUN4-MANT3).
Material: crops from `tools/iiif_lines.py --image` (one crop per code line, gloss margin above), two blind Sonnet passes (one call per
frame per pass, crop paths only, A in order, B reversed), reconciled by the worker against the crops. Unit: a "glossed run" = a maximal
run of code groups with a period interlinear gloss above it.

Re-commits PREREG-MANT0501 (RUN3-MANT, 1a7370f5) unchanged, applied to each frame as its own leaf (0500 alone, 0502 alone):
- pairs = one per glossed run; `tools/interlinear_align.py align --floor 0 --max-chunk 14 --seg-bonus 1.0 --len-prior 0.5`, no --prior.
- S = among codes with >= 2 glossed positions on this leaf, share whose aligned chunks are identical at every occurrence;
  S_multi = same restricted to codes occurring inside multi-code runs (AX-NAMES per-class lesson).
- Control: gloss strings permuted across glossed runs (pairing shuffle), re-aligned with identical options, 200 draws, seed 500
  (frame 0500) / 502 (frame 0502).
- Gate: merge into key.tsv only if N_recurring >= 3 AND S_real > p95(S_shuffle) strictly. Tie, miss or N_recurring < 3 = leaf HELD:
  values to f0500_0502/leaf_values_<frame>.tsv at grade M, nothing into key.tsv (rule 3 Szembek paragraph).
- Grades if the gate passes: code under a single-code gloss -> C; code inside a multi-code run whose chunk agrees at >= 2 occurrences
  -> C; any other multi-code chunk -> M. As at GAPS195/RUN3-MANT, if S_multi ties or misses its own p95, only single-code glosses are
  licensed. A gloss contradicting an existing key.tsv value is not overwritten: logged in HYPOTHESES.md (rule 4).
- Per-class breakdown reported (single-code vs multi-code glosses); single-code glosses vs key.tsv/Krauske (agree/disagree/new).
- Reported, NOT a gate: the same statistic on 0500+0502 pooled, and cross-leaf agreement of single-code glosses with 0501/0528.
Small-N risk stated in advance: frame 0500 carries about 4 glossed runs (RUN4-MANT3 R1-R4); if it has < 3 codes recurring under glosses
it is HELD by the N floor regardless of agreement. A single-code gloss seen once on a HELD leaf stays M.
