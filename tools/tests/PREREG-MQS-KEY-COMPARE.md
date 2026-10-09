# PREREG-MQS-KEY-COMPARE (9 Oct 2026, LANE MQS next, account 4)

Written and pushed before any control is scored (CLAUDE.md rule 3). Tool: `tools/key_design.py --compare KEY_A KEY_B`
(new option beside `--matrix`, reusing the same key parser `load_table` and `signature`). Source of the idea: Lasry,
Biermann and Tomokiyo 2023 (Cryptologia 47:2) pp.128-130, nn.64-66 (Figs 15-16: sibling keys of one office compared by
shared design and nomenclature vocabulary); research/MARY-STUART-TALK-2026-10-09.tsv row M27.

## Statistic (namespace-free: two keys of one office rarely share sign labels)

Both keys are parsed by `load_table`; values are classified by `classify_value` (letter / short / word / name / null).
- **V (vocabulary)**: Jaccard of the two sets of word-like values (short + word + name, folded, '?' stripped).
  Two empty sets give V = 0 (no evidence), never 1.
- **L (letter profile)**: cosine of the two 26-dim vectors of codes-per-letter (homophone counts).
- **D (design)**: mean of five min/max ratios -- valued codes, distinct letters, homophones per letter (mean),
  word-like share of valued codes, null count + 1 -- and one indicator (both keys numeric, or both not).
- **S (composite)** = (V + L + D) / 3. Code-level agreement (same code, same value) is printed when the two keys share
  at least 5 code labels, but is NOT part of S (sign labels are transcriber-assigned; see below).

## Known answer

Pair K: `ciphers/nevers-birago-fr3251-1572/keys/key_nevers_birago_1572.tsv` (the printed Tomokiyo table, descriptive
glyph labels) vs `ciphers/nevers-birago-fr3251-1572/keys/key_1572_clerk.tsv` (the clerk's sheet on canvas 182, aligned
to the no.87 blind transcription, T-labels). Same office, same year, a sibling/variant key; no shared label namespace,
so only value-space features can see the relation. Intended use: two keys of one office and period, compared to say
"likely sibling" vs "same office only". Language French/Italian mix as in the Nevers papers.

Caveat stated in advance: the clerk key's values come from alignment to a transcription read with the printed key in
view of the same project; part of their agreement is therefore not independent. The gate tests whether the tool ranks a
known sibling pair, not whether the two keys are independently related.

## Nulls (both computed, both gated)

- **R (random same-office pairs)**: pool = KEY-DESIGN.tsv rows with usable=yes, duplicate_of empty, and 'nevers' in the
  office or correspondents column (case-insensitive). 20 pairs drawn with `random.Random(0)` from different folders
  (two files of one folder never form a pair). Gate R: S(K) > max S over the 20 pairs (rank 1 of 21).
  Why R can differ from K on S: every pair changes vocabulary, letter profile and design at once; nothing about S is
  fixed by construction.
- **P (vocabulary-permuted null)**: 200 draws. Key B's word-like values are replaced, one for one, by values drawn
  without replacement from the word-like vocabulary of the pool keys outside K's folder; letters, nulls and code count
  are kept, so L and D are unchanged by construction and only V moves. Gate P: S(K) > p95 of S under P.
  Why P can differ from K on S: V is the only component it changes, and V is a component of S; if K's rank rests on
  shared design alone (L, D), P matches K and the gate fails. (L and D cannot differ under P -- stated, not tested.)
- **Identity (must score high, not gated)**: a key against itself must give S = 1.000.
- **Must NOT read as sibling (offline test)**: two synthetic keys with disjoint vocabulary and different design must
  score below 0.5.

Ceiling check: if the R-null max is >= 0.95, the R gate is void (no headroom) and reported as a non-test.

## Outcome rule

Both gates met: shelf grade `controlled-only` for comparing two keys of one office (one known sibling pair; a single
pair cannot support `proven`). Any miss: the option ships `weak` with both numbers, is not re-briefed, and nothing is
run on a target from it. No key, status, reading or AUDIT.md changes in any case; the tool reads and prints only
scores (no sign values are printed by the control; the Birago 1572 family has an open blind sort, ASKS 118).
