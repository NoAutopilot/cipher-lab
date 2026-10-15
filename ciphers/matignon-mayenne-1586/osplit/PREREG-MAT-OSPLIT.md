# PREREG MAT-OSPLIT (15 Oct 2026, account-4 worker, LANE DEFAULT-A4-1236-15)

Written 12:5x UTC 15 Oct 2026 by `date -u`, before any crop is sorted and before any score. Prior work:
`tools/prior_work.py matignon-mayenne-1586 --item-spec 'shelfmark=BnF fr.15572;folio=91-92,110;sender=Mayenne' --step-type key --offline`
exit 0, plaintext KNOWN (Tomokiyo l.640 = the period margin decipherment of f.91-92, the known answer here).

## Question
MAT-BOX (eye, 5 gloss witnesses on block E) suggested the reader label `o` (key o = i, H) merges two shapes: **A** a small plain closed
round, **B** an a-like round with a right stem or tail; A read i, B read a. Does a blind shape sort of every `o` token on f.91 A-F, scored
by MAT-KA's block-held-out gloss instrument, (1) separate the gloss letters better than a random split of the same tokens, and (2) give
each shape a held-out value?

## Sort (blind, before any score)
Tokens: every position whose reconciled sign is `o` at confidence H in `f91/ciphertext_draft_f91.tsv` (A, B, D), `_f91c.tsv` (C, F),
`_f91e.tsv` (E) -- the same token set MAT-KA's `signs` reads; plus f.110 `o` tokens as far as the box allows (record only, no gloss there).
One per-token crop per token (a small window around the token, cut from the regenerated line crops; images in the scratchpad only), named
by an opaque id. One Sonnet subagent call per <= 40 crops, given only: the crop paths, two exemplar crops per shape taken from
**outside f.91** (shape B: the f.78v chart's `o`, chart line 2 pos 15/20/29; shape A: f.110 1:18 per MAT-BOX), and the instruction to
answer A, B, or X (not an o / cannot tell). No sign values, no gloss, no block or position. A token whose crop is wrong (cut misses
the sign) is X. X tokens stay as label `o` and are dropped from the split statistics (reported). The worker does not re-label any token.

## Instrument (MAT-KA's, unchanged, `f91/mat_ka.py` functions imported)
Per-block masked alignment with `o` ALSO masked (`align(masked_h='o')`: removed from the prior, every o token a unique singleton), so an
o token's chunk comes only from the H codes around it. Positions with an empty chunk are excluded.

## Tests and gates
1. **Split test (the relabel test).** Statistic S = pooled LOBO hits of shape A (fit from A's other blocks) + LOBO hits of shape B (fit
   from B's other blocks), over n_A + n_B scored positions. Control: 1000 random relabelings of the same scored o positions into A/B
   keeping each block's A and B counts (seeds 1-1000); p95 = 950th sorted value. The control varies exactly the axis tested (which o
   goes to which group), so it can differ from the target (rule 3 non-test clause checked). Also reported: the unsplit o LOBO accuracy.
   **Split PASS iff S > control p95.**
2. **Per shape (only reported as a value if the split PASSes).** For shape A and B separately, MAT-KA's verdict rule: LOBO accuracy vs
   its 200-draw label-shuffle null (p95), all-block majority letter, and a power code subsampled to the shape's scored n (20 seeds,
   PASS if >= 11/20 beat their p95 and >= 11/20 fit the key value). Power code rule (fixed now): the H single-letter key code (other
   than o) with the same value as the candidate (A: i, B: a) with the most scored positions in the masked alignment if it has >= n;
   else the H code with the smallest scored count >= n (frequency-matched), as MAT-KA did for D2. Verdict per shape: power FAIL ->
   too-short; power PASS, acc > p95, majority = candidate -> candidate S at that value; majority differs -> candidate S at that letter,
   flagged; acc <= p95 -> fails held-out.
3. Grade: **M unless the split PASSes and the shape's own verdict is candidate S.** No key.tsv edit in this job (the brief: grade M unless the
   registered test passes; a passing shape is recorded as an S candidate in HYPOTHESES.md with its numbers; the key/label edit across the
   13 leaves needs Bourdeau's transcription re-labelled, which this job does not do).

## Outputs
`osplit/sort_tokens.tsv` (id -> block, line, pos; written before the sort), `osplit/sort_answers.tsv` (subagent output, verbatim),
`osplit/mat_osplit.py` (`--check`), `osplit/mat_osplit_result.tsv`, NOTES.md "MAT-OSPLIT", HYPOTHESES.md row, Verdict update, gaps_check.

## Addendum 1 (13:0x UTC 15 Oct 2026 by `date -u`, before the sort and before any score)
MAT-KA's `signs` reader concatenates block E from two drafts (`ciphertext_draft_f91.tsv` E1-E4, the MAT-F91 first pass, 112 tokens, and
`_f91e.tsv` E1-E5, the MAT-F91E redo, 153 tokens) against one E gloss. The registered tests above use MAT-KA's reader unchanged (gating).
A secondary run, reported but NOT gating, repeats tests 1-2 with block E taken from `_f91e.tsv` only. `sort_tokens.tsv` therefore keys
tokens by draft file as well as line and position (o tokens: 78 = 6 from the f91 E draft + 72 others). Sort jobs: job1 = blocks A, D, F
(40 tokens), job2 = blocks B, C, E (38 tokens). Each sorter sees each line image with the line's reader LABEL sequence (no values) in
which every o to sort is replaced by its opaque id, so it can find the sign; this is labels-only, no values, no gloss.
