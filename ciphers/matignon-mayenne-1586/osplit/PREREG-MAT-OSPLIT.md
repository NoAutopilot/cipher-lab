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

## Addendum 1 (12:5x UTC 15 Oct 2026 by `date -u`, before the sort and before any score)
MAT-KA's `signs` reader concatenates block E from two drafts (`ciphertext_draft_f91.tsv` E1-E4, the MAT-F91 first pass, 112 tokens, and
`_f91e.tsv` E1-E5, the MAT-F91E redo, 153 tokens) against one E gloss. The registered tests above use MAT-KA's reader unchanged (gating).
A secondary run, reported but NOT gating, repeats tests 1-2 with block E taken from `_f91e.tsv` only. `sort_tokens.tsv` therefore keys
tokens by draft file as well as line and position (o tokens: 78 = 6 from the f91 E draft + 72 others). Sort jobs: job1 = blocks A, D, F
(40 tokens), job2 = blocks B, C, E (38 tokens). Each sorter sees each line image with the line's reader LABEL sequence (no values) in
which every o to sort is replaced by its opaque id, so it can find the sign; this is labels-only, no values, no gloss.

## Addendum 2 -- MAT-O3X re-sort (13:2x UTC 15 Oct 2026 by `date -u`, before the re-sort and before any score)
Job MAT-O3X (LANE DEFAULT-A4-1236-15): second attempt at this split. **Gate, statistic, control, per-shape rule and grade rule above are
unchanged; `osplit/mat_osplit.py` is re-run unchanged** on a new answer file. Only the sort input changes:
- **Crops:** `osplit/o3x_crops.py` cuts one per-token window per token of `sort_tokens.tsv` (all 78): the line strip (s1/s2 joined at
  their manifest offsets), sign columns from the column ink profile (read-free), the token's column estimated proportionally from its
  draft position, window = estimate +- 4 columns, upscaled 3x, no marker. Images in scratch only.
- **Join fix:** the 6 tokens of the MAT-F91 first-pass E draft (o0xx with draft `f91`, lines E1-E3) now get strips from
  `regen_f91.sh`'s own `f92r_ciE_L0n` crops (the line images MAT-OSPLIT's join never wrote). Those E crops are offset left (MAT-F91), so
  some may miss the token; such a token is X.
- **Locating the token:** each crop comes with the reader LABEL sequence of draft positions p-4..p+4 with the target as `[id]` (labels
  only, no values, no gloss), as MAT-OSPLIT gave the full line label sequence.
- **Exemplars:** shape B = three windows of the committed f.78v chart line 2 (`images/f78v_79r/ref/`, positions 15, 20, 29, the o's
  MAT-BOX eyed as B), with their label context. Shape A: no exemplar image (the committed f.110 line crops are 53 px high, and the
  f.110 1:18 position was not re-located within cap); A is described in MAT-BOX's words only ("a small plain closed round o"). This is a
  deviation from the registered "two exemplar crops per shape", declared now, before the sort.
- **Sorters:** two Sonnet calls (job1 = draft f91 blocks A, D + f91c F; job2 = f91 B, E + f91c C + f91e E; <= 40 crops each), answer
  A / B / X per id with a confidence (high/low). Output `osplit/sort_answers_o3x.tsv` (verbatim); `mat_osplit.py` reads it via the
  `--answers` option added for this job (default unchanged: `sort_answers.tsv`). Low-confidence A/B answers count as given (as MAT-OSPLIT's did).
- **Rule 3:** if the split FAILs again, it is logged untested-by-this-instrument (machine blind sort) and the o split goes to the owner's
  sign sorter; no third machine attempt.

## Addendum 3 -- MAT-R2 second blind reader (13:4x UTC 15 Oct 2026 by `date -u`, before the call and before any score)
Job MAT-R2 (LANE DEFAULT-A4-1236-15). **Gate, statistic, control, per-shape rule and grade rule unchanged; `osplit/mat_osplit.py` re-run
unchanged** with `--answers sort_answers_r2.tsv` (result `mat_osplit_result_r2.tsv`).
- **Crops:** the same 78 windows, regenerated in this container by `o3x_crops.py` from `regen_f91.sh` / `regen_f91c.sh` / `regen_f91e.sh`
  (c98 sha1 94d007c8, as MAT-O3X); images in scratch only. Same label context file (p-4..p+4, labels only).
- **Reader:** ONE Sonnet call, all 78 crops (the brief's one call; this exceeds addendum 2's <= 40 per call, declared now). Given only the
  crop paths with opaque ids, the label context, MAT-BOX's words for both shapes, and as shape-B exemplar the f.78v chart line 2 halves
  (2x, committed `images/f78v_79r/ref/`) with the positions of its three o's. No values, no gloss, no block/position, no first-reader
  labels. Answer A / B / X per id with high/low confidence; an id left unanswered is X. Output `osplit/sort_answers_r2.tsv` verbatim.
- **Agreement (reported, not a gate):** with `sort_answers_o3x.tsv` (MAT-O3X; o001 = X): raw agreement and Cohen's kappa over all 78 on
  A/B/X, and raw agreement + kappa on the tokens both readers called A or B. Descriptive reading fixed now: kappa(A/B, both-called) >= 0.6
  = the two readers see the same split; 0.2-0.6 = partly reader-dependent; < 0.2 = the O3X split is reader-dependent and the next step is
  the owner's sign sorter, not a further machine reader.
- **Consensus (reported, not a gate):** tokens where both readers give the same A or B, run through `mat_osplit.py` as a third answer file
  `sort_answers_r2cons.tsv` (disagreements and any X -> X), same gate, reported.
- No key/label/reading edit; HYPOTHESES.md row + NOTES.md section only. The 13-leaf relabel is not started.
