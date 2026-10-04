# BIR-CCE pre-registration (4 Oct 2026, written after cce/glyph_map.tsv was pushed in c97016e4 and before any Ceppo value was joined to it)

Hypothesis (Lasry, Biermann and Tomokiyo 2023, App. B, "cross-cipher contamination"): some off-sheet or conflicting signs in
the 1572 letters are the clerk using a sign of the earlier Ceppo-Nevers key. **Caveat, in every output: same-day use of both
keys by one clerk is NOT established here, unlike Mary Stuart's packets.**

Honesty note: the glyph reader (one Sonnet call) saw no value and no plaintext. The worker who cut the montage had seen
Tomokiyo's key image with its headers while cutting the cells, and the C-id -> column map (`ceppo_cells.tsv`) went up in the
same commit as the read. The read itself is the reader's alone (`glyph_read.tsv`), and nothing in it was edited.

## Units (fixed now)
Primary units are the mappings graded H or M by the reader:
- pool shape classes (nos.71/86/90, `harvest/offsheet/pool_*.tsv`): X_8->C48 (H), X_T3->C35 (H), X_EQ->C09 (H),
  X_AE->C46, X_MA->C10, X_CC->C03, X_PCT->C25 (M);
- no.73 tiles (f.144r, `harvest/ciphertext_f144r.tsv`; sorter order = ciphertext order): f144r_L04.2_03 (T95)->C08,
  f144r_L04.1_10 (X_NEW)->C40, f144r_L03_03 (X_NEW)->C39 (all M);
- conflict sign T95, pile mapping by tile majority -> C39 (M), over every T95 in the pools and in f.144r except the one tile
  above mapped separately; it is compared with BOTH unread and its current 1572 value.
L mappings are scored and reported as secondary, never gated. X_CE->C41 (M) is known-answer only: off no.87 it is not
separated from T50 in the committed tokens.
No.77 (f.152r) has no mapped sign (6 X_NEW, unsubtyped, not tiled); no.85 (f.168) has no committed reading tokens. No.87 is
the known-answer item and never enters the target statistic.

## Statistic
For a unit: substitute the Ceppo cell's value (letter; `et` -> "et"; a `null` cell -> dropped) at its occurrences;
gain = per-letter mean log10 4-gram score (`judge_plaintext` corpus it16dip, the spec judge, scoring as
`harvest/offsheet/fit_offsheet.py`: words of >= 4 letters between unread gaps, pooled over the 71/86/90 pools and f.144r)
with the value minus with the sign unread. For T95, also minus with its current fitted-map value.

## Null (rule 3 check)
1000 draws: the multiset of all mapped cells (H, M and L) is shuffled among the units, so each unit receives the value of
a random other mapped cell; the same gain is computed. The value assigned changes the decoded letters, so the 4-gram gain
can and does change between draws: the null is not identical to the target by construction (checked by reporting the
null's spread per unit; a zero spread voids that unit).

## Gate
A unit PASSes if gain > 0 and gain > its own null p99. A PASS is graded M at most, enters neither key.tsv nor exceptions,
and gets a ROOM line for a later verifier.

## Known answer first (no.87)
Occurrences on no.87 of mapped classes with a determinate clerk-sheet value (`harvest/offsheet/known_no87.tsv`), plus the
7 X_CE tiles (sheet s, NOTES.md NO87 section): count how many have Ceppo value == sheet value; compare with the same count
under the 1000 shuffled maps. Reported as the positive control: if the real count is not above the null p95, the target
test is reported as running without a working positive control (weaker), not stopped (the brief's wording).
