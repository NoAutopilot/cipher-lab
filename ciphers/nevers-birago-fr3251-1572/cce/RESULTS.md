# BIR-CCE results (4 Oct 2026, account 3): cross-cipher contamination test, 1572 off-sheet signs vs the Ceppo-Nevers key

**Caveat: same-day use of both keys by one clerk is NOT established here, unlike Mary Stuart's packets** (Lasry, Biermann
and Tomokiyo 2023, App. B, credited for the method; keys reconstructed by S. Tomokiyo).

Verdict: **no unit passes.** Every primary (H/M) unit FAILs its own shuffled-cell null p99. The known-answer control on no.87
is **not above its null p95** (7/10 vs p95 7), so this negative ran without a working positive control and is weak (rule 3).
Nothing changes in key.tsv, exceptions or any reading. Disk only, 0 network requests, 1 Sonnet vision call.

Files: `glyph_map.tsv` (value-blind read, pushed c97016e4 before any value), `PREREG.md` (f05da60e, before scoring),
`score_cce.py` (regenerates `results.tsv` and `known_no87.tsv`; seed 1, 1000 draws), montages and `make_montage.py`.

## Known answer, no.87 (positive control)
| sign | Ceppo cell (grade) | Ceppo value | clerk sheet | match |
|---|---|---|---|---|
| X_8 (1 occ) | C48 (H) | et | m | no |
| X_EQ (2 occ) | C09 (H) | d | f, n | no |
| X_CE (7 tiles) | C41 (M) | s | s (7/7) | yes |
Real 7/10; shuffled null mean 1.94, p95 7, max 8. Per sign it is 1 of 3, and the one match is X_CE, which carries all 7
occurrences. Under the shuffled map X_CE draws an s-valued cell 7 times in 24 (the reader mapped many query shapes to s
cells), so the agreement is within chance at p95 (5 of all 54 Ceppo cells are s). Read on its own, "the curled Ce sign looks
like a Ceppo s homophone and the clerk reads it s" is one observation, M at most. It is not a test result.

## Target units (nos.71/86/90 pools + no.73 f.144r; gain in per-letter mean log10 4-gram, it16dip)
| unit | occ | Ceppo cell (grade) | value | gain vs unread | null p99 | verdict |
|---|---|---|---|---|---|---|
| X_8 | 7 | C48 (H) | et | -0.0013 | -0.0005 | FAIL |
| X_T3 | 7 | C35 (H) | r | -0.0043 | -0.0023 | FAIL |
| X_EQ | 11 | C09 (H) | d | -0.0017 | -0.0002 | FAIL |
| X_AE | 16 | C46 (M) | u | -0.0153 | 0.0090 | FAIL |
| X_MA | 5 | C10 (M) | e | -0.0036 | -0.0012 | FAIL |
| X_CC | 7 | C03 (M) | a | -0.0038 | 0.0033 | FAIL |
| X_PCT | 3 | C25 (M) | n | -0.0064 | -0.0000 | FAIL |
| f144r L04.2_03 (T95 label) | 1 | C08 (M) | d | -0.0030 | -0.0004 | FAIL |
| f144r L04.1_10 (X_NEW) | 1 | C40 (M) | s | 0.0004 | 0.0012 | FAIL |
| f144r L03_03 (X_NEW) | 1 | C39 (M) | s | 0.0006 | 0.0006 | FAIL (ties p99) |
| T95 (pile -> C39) | 11 | C39 (M) | s | -0.0162 | -0.0070 | FAIL; vs current value: 0.0000 (current fitted value is already s, so no conflict to test here) |
Secondary (L, not gated): X_SQ, X_TRI, X_BB, X_A and three f.144r tiles all below their p99. Null spread is non-zero for every
unit (0.0008-0.0302), so the null could differ from the target (rule 3 check). Full table: `results.tsv`.

## Limits
- One vision read, Tomokiyo's modern redrawing on one side and 16th-century tiles on the other; 18 of 42 queries matched no cell.
- Pool classes were matched from text descriptions (readers' class definitions), not tiles: weaker than a tile match.
- No.85 has no committed reading tokens and no.77 has no mapped sign, so neither entered the statistic.
- The gain statistic is small at these occurrence counts (1-16), and the positive control did not clear p95, so a real CCE sign
  with few occurrences could be missed. Untested-by-this-tool at this N, not refuted.
