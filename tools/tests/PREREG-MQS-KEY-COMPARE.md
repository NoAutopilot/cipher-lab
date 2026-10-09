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

## Result (appended after scoring, 9 Oct 2026 08:42 UTC by date -u; `python3 tools/key_design.py --compare-control`, exit 1)

- K (Nevers-Birago 1572 printed table vs the clerk sheet): S 0.750 (V 0.667, L 0.880, D 0.705).
- R null: 20 pairs from a pool of 27 Nevers-office keys; max 0.917, mean 0.435; K rank 2 of 21 -> **FAIL** (not void:
  the max is below the 0.95 ceiling line).
- P null (vocabulary-permuted, 200 draws from 665 pool words): mean 0.529, p95 0.528 -> PASS.
- Identity S(A, A) = 1.000.
- The one R pair above K is fr3416 key_no25 x fr3993 key_no70 (S 0.917: V 1.000, L 0.974, D 0.777). Tomokiyo
  (nevers.htm, no.70, quoted in ciphers/fr3993-gonzague-nevers-1595/NOTES.md) describes no.70 as "a superset of no.25",
  so the random draw happened to contain a second, period-documented sibling pair. Read after scoring, this does not
  change the gate: the registered rule (K above all 20) is missed, and the option ships `weak`. Note also that its
  V = 1.000 rests on one word-like value in each key; a small-vocabulary shrinkage is a suggestion for a later brief,
  not a re-tune here. Post hoc and not gated: K ranks above the other 19 pairs.

Outcome: `weak` on tools/data/tool_shelf.tsv with both numbers; not re-briefed; nothing run on a target from it.
