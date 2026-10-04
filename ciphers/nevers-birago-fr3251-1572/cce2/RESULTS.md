# BIR-CCE2 results (4 Oct 2026, account 3, Fable worker): second cross-cipher contamination test, 1572 off-sheet signs vs the Ceppo-Nevers key, Fable value-blind glyph map

**Caveat: same-day use of both keys by one clerk is NOT established here, unlike Mary Stuart's packets** (Lasry, Biermann
and Tomokiyo 2023, App. B, credited for the method; both keys reconstructed by S. Tomokiyo).

Verdict: **untested-by-this-tool, not a negative** (pre-registered decision rule, `PREREG-2.md`; brief item 3). The no.87
known-answer control is **0/10 occurrences and 0/3 signs** against shuffled-cell nulls with p95 7 and 1: the control does not
beat its own null, so the target rows below are tabled but not read as a negative. Every primary unit FAILs its null p99
anyway (as in run 1). Nothing changes in key.tsv, exceptions or any reading. Disk only, 0 network requests, 0 subagents;
the 37 glyph views were read by this Fable worker itself, one sign class per look.

Files: `glyph_map.tsv` (value-blind read, pushed 4412af11 with `PREREG-2.md` before any value file was opened), `cut_tiles.py`
(regenerates `ref_ceppo.png`, `ref_1572.png`, the two perm files, `query_tiles.tsv` and `views/<class>.png`, 8 MB, not
committed), `score_cce2.py` (regenerates `results.tsv`, `known_no87.tsv`, `step2.tsv`; seed 1, 1000 draws).

## What changed against run 1, and what did not
- Instrument: Fable read every class itself from native tiles (2-5 per class, from different letters where they exist)
  beside all 54 Ceppo cells carrying shuffled labels; run 1 was one Sonnet call on a montage with run-1 cell ids in table
  order and text descriptions for the pool classes. 24 of 34 1572 classes now map to **no cell** (run 1: 18 of 42 queries).
- Agreement with run 1 on the cells that survived both reads: X_8 -> et (H both), X_EQ -> d (H both), X_T3 -> r (H both),
  X_MA -> e (M both), T95 -> the s-cell C39 (M both, now reached under shuffled labels), f144r_L03_03 -> C39 (M both),
  X_A -> n, X_NEW-o -> g (L both). Different: X_BB -> a null cell (run 1 c), X_CC -> r (run 1 a), X_PCT -> t (run 1 n),
  **X_CE -> the i-cell C17 (run 1: the s-cell C41)**, X_AE -> none (run 1 u), X_SQ/X_TRI -> none (run 1 L cells).
- The mapping is therefore stable on the three H units and on T95, and run 1's one known-answer "match" (X_CE -> an s
  cell) does not survive a reader that looks at the omega's lead stroke: the Ceppo cell with the c-lead (K17, z-row5) has a
  y descender the ink lacks, and the omega cell without a descender (K07, i-row1) has its flourish on the other side.

## Known answer, no.87 (the gate)
| sign | tiles | Ceppo cell (grade) | Ceppo value | clerk sheet | match |
|---|---|---|---|---|---|
| X_8 (1 occ, R03.4) | K21 = C48 (H) | et | m | no |
| X_EQ (2 occ, L14.17, L17.29) | K44 = C09 (H) | d | f, n | no |
| X_CE (7 tiles, f178v) | K07 = C17 (L) | i | s (7/7) | no |
(a) occurrences 0/10, null mean 1.25, p95 7, max 8; (b) signs 0/3, null mean 0.24, p95 1, max 2. Not above p95 on either
count: by the pre-registered rule the control has no power at this N and the target is untested-by-this-tool.
Read the other way, this is also the one letter where the clerk's own values are known, and none of the three glossed
off-sheet signs carries its clerk value in the Ceppo cell it resembles (X_8 is m to the clerk, et in Ceppo; X_EQ is f/n,
d in Ceppo). That is an observation against contamination on no.87 specifically, graded M (one reader, three signs, no
independent positive control), not a control-backed negative under rule 3.

## Target units (nos.71/86/90 pools + no.73 f.144r; gain in per-letter mean log10 4-gram, it16dip; tabled, not read as a negative)
| unit | occ | Ceppo cell (grade) | value | gain vs unread | null p99 | row |
|---|---|---|---|---|---|---|
| X_8 | 7 | C48 (H) | et | -0.0012 | 0.0007 | FAIL |
| X_EQ | 11 | C09 (H) | d | -0.0016 | -0.0002 | FAIL |
| X_T3 | 7 | C35 (H) | r | -0.0042 | -0.0023 | FAIL |
| X_MA | 5 | C10 (M) | e | -0.0035 | -0.0011 | FAIL |
| X_BB | 4 | C51 (M) | null (sign dropped) | 0.0005 | 0.0005 | FAIL (ties p99) |
| T95 (pile) | 11 | C39 (M) | s | -0.0204 | -0.0087 | FAIL; vs current value 0.0000 (current fitted value is already s) |
| f144r L03_03 (X_NEW-d) | 1 | C39 (M) | s | 0.0006 | 0.0006 | FAIL (ties p99) |
Secondary (L, not gated): X_A -> n, X_CC -> r, X_OJ -> h, X_PCT -> t, all below their p99. X_NEW-o -> g has no committed
token (f.168 only). Null spread is non-zero for every unit (0.0022-0.0173), so the null could differ from the target
(rule 3 check). Full table: `results.tsv`.

## Step 2: Ceppo-side off-key signs read against the 1572 letter grid (the other direction; `step2.tsv`)
The 1570-71 letters (fr.3251 f.21v, f.35, f.87) carry three off-key classes: X_THETA2 (double-barred oval, value r from the
fr.3252 f.36 witness), X_POUND (lb/pound sign, l at grade I) and X_NEW. The fr.3252 f.47r run was not tiled (its readings
are not committed tokens). Mapped value-blind against the 1572 letter-grid strips: X_THETA2 -> the barred-o cell = **a**
row1 (M), X_POUND -> **t** row2 (L), the Z-form X_NEW (f21v L09.27) -> **r** row2 (L); no known answer exists on this side.
| unit | occ | 1572 value | gain vs unread | gain vs current | null p99 | row |
|---|---|---|---|---|---|---|
| X_THETA2 (M) | 15 | a | -0.0171 | -0.0334 (current r) | 0.0163 | FAIL |
| X_POUND (L) | 10 | t | 0.0113 | (unkeyed in the reading) | 0.0188 | secondary: below |
| X_NEW Z-form (L) | 1 | r | 0.0009 | | 0.0019 | secondary: below |
The one primary unit loses against both unread and its witness value r: the 1572 key's a-cell does not read where the
double-barred oval stands. Without a positive control this is a weak negative on that one sign, not a design exclusion.

## Limits
- Tiles were cut by a column-ink-profile blob fit to the passage's sign count; 14 of 115 tiles were one position off or
  prose mis-cuts (named per class in `glyph_map.tsv`) and were ignored, never mapped from the wrong blob.
- The no.87 gate has three signs; it cannot distinguish "no contamination on no.87" from "the shape map is wrong" --
  which is exactly why the pre-registered rule reports untested rather than negative.
- Rule 3's third-attempt clause: this was the second attempt with a changed instrument (the reader); a third shape-map ->
  n-gram-gain run is not licensed. What would be a different instrument: a no.87-independent known answer (a Ceppo-key
  letter and a 1572-key letter by the same clerk on one day, which the folder does not have), or more committed tokens
  for the signs with 1-4 occurrences.
