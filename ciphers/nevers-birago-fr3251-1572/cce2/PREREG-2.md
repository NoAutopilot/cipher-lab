# BIR-CCE2 pre-registration (4 Oct 2026, account 3, Fable worker; written after cce2/glyph_map.tsv and before any value file is opened)

Second attempt at BIR-CCE (cce/PREREG.md, cce/RESULTS.md) with a changed instrument: the glyph reader is the Fable worker
itself, one sign class per look, native tiles from several letters beside every reference cell, reference labels shuffled
(K01-K54 Ceppo cells, N01-N20 1572 column strips) so that neither the table layout nor run 1's C-ids can leak a value.
A third attempt with the same design (shape map -> n-gram gain vs shuffled-cell null) is not licensed by rule 3.
**Caveat, in every output: same-day use of both keys by one clerk is NOT established here, unlike Mary Stuart's packets.**

Honesty note. Before cutting, this worker read run 1's RESULTS.md and ceppo_cells.tsv, so it knows run 1's cell ids and
values (e.g. X_CE -> C41 = s, X_8 -> C48 = et) but not which shuffled K-label those cells now carry; it has not looked at
montage_ceppo.png, nevers_add1.png with headers, NeversBirago.png with headers, either key.tsv's value rows, or the two
perm files. The 1572 letter-grid strips (ref_1572.png) carry no printed text. "none" was allowed freely: 24 of 34 1572
classes map to no cell.

## Units (fixed now)
Primary (H or M in glyph_map.tsv), scored on the committed tokens of nos.71/86/90 (pools) and no.73 (f.144r), never no.87:
- X_8 -> K21 (H), X_EQ -> K44 (H), X_T3 -> K09 (H); X_BB -> K06 (M), X_MA -> K42 (M); the pool class carries every
  committed occurrence of the class (as run 1);
- T95 pile -> K40 (M): every T95 in the pools and f.144r, compared with BOTH unread and its current fitted value;
- tile f144r_L03_03 (X_NEW-d) -> K40 (M), one occurrence.
Secondary (L, reported, never gated): X_A -> K50, X_CC -> K30, X_NEW-o -> K13 (f168, no committed tokens -> no occurrence),
X_OJ -> K35, X_PCT -> K45. X_CE -> K07 (L) is known-answer only (off no.87 it is not separated from T50 in the tokens).
A K-label that resolves to a `null` cell drops the sign; `et` substitutes "et".

## Statistic, null, gate (unchanged from run 1, cce/PREREG.md)
gain = per-letter mean log10 4-gram (it16dip, judge_plaintext) over words of >= 4 letters between unread gaps, pooled over
the 71/86/90 pools and f.144r, with the Ceppo value substituted minus with the sign unread (T95 also minus current value).
Null = 1000 draws, the multiset of all mapped cells (H, M, L) shuffled among the units (rule 3: the null's spread per unit is
reported; a zero spread voids that unit). Gate: PASS = gain > 0 and gain > the unit's own null p99. A PASS is graded M at
most, enters neither key.tsv nor exceptions, and gets a ROOM line for a later verifier.

## Known answer first (no.87), the gate for reading the target at all
Occurrences on no.87 of mapped classes with a determinate clerk-sheet value: X_8 R03.4 (m), X_EQ L14.17 (f), L17.29 (n), plus
the 7 X_CE tiles (sheet s) = 10 occurrences, 3 signs (the same set as run 1; X_MA, X_BB, X_T3 do not occur on no.87).
Two counts, both against 1000 shuffled-cell draws (each sign redrawn from the multiset of mapped cells):
(a) occurrences with Ceppo value == sheet value (run 1's count; p95 gate); (b) SIGNS with Ceppo value == sheet value, out of
3 (p95 gate) -- (b) is added because (a) is dominated by X_CE's 7 tiles (rule 3, unbalanced-class paragraph).
Decision rule (brief item 3): if the real count is not above its null p95 on BOTH (a) and (b), the control has no power at
this N; the target rows are still computed and tabled but the verdict is "untested-by-this-tool", not a negative.

## Step 2: Ceppo-side off-key signs vs the 1572 letter grid (the other direction)
Mapped: X_THETA2 -> N10 row1 (M, primary), X_POUND -> N14 row2 (L), X_NEW (the Z-form, f21v L09.27 only) -> N01 row2 (L).
The N-label is resolved to a 1572 cell through ref_1572_perm.tsv and the table header, then to a letter through
keys/key_nevers_birago_1572.tsv. Statistic: the same 4-gram gain on the committed Ceppo readings (f.21v, f.35, f.87 tokens,
it16dip) with the 1572 value at the sign's occurrences vs unread (X_THETA2 also vs its current witness value r); null = 1000
draws of a random 1572 letter cell per mapped sign; gate as above. Known answer: none exists on this side (no Ceppo off-key
sign has a period gloss); reported as weaker. If the N-label resolves to a blank or word-code strip, the unit is "no cell".
