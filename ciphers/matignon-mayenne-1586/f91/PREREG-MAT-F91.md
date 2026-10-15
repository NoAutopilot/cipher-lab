# PREREG-MAT-F91 (15 Oct 2026, 05:5x UTC by date -u; account-2 worker MAT-F91, LANE DEFAULT-A2-0509-15)

Written and pushed before any transcription, alignment or score. Brief: `.claude/briefs/runs/2026-10-15-ytbiz-default-0509-jobs.md` job MAT-F91.
Scope: BnF fr.15572 f.91r-92r (btv1b9061879d canvases 97-98), blocks A, B, D, E of `f91/blocks.tsv` only (C and F a later job).

## Material
- Cipher lines: each line's s1/s2 crops (from `regen_f91.sh`) stacked into one image per line (local PIL, scratchpad only).
  Two blind Sonnet passes (A, B), <= 12 line images per call, label set and conventions of `align1f/PASS_BRIEF.md` with the
  f.78v reference chart (`align1f/reference_f78v_l1-5.tsv` + `images/f78v_79r/ref/`). Readers never see key.tsv, the gloss or
  any decoded value. `tools/reconcile_passes.py` A B -> agreed columns; disagreements settled by eye on the crop where
  possible (one reconciliation unit), otherwise kept as an unknown token `?` (excluded from every statistic below).
- Gloss lines: one Opus read of the margin crops (clear French, as written, abbreviations expanded only in a separate
  normalised column), one Sonnet check pass on the same crops; disagreements settled by eye; the gloss is grade C
  (a period decipherment).

## Alignment
`tools/interlinear_align.py align`, one pair per block (whole gloss of the block vs the whole cipher block),
`--code-prefix @` (letter-class signs take 0-1 letter), numerals >= 10 as word codes (`--word-code-prefix %`,
`--code-chunk 1`, `--max-chunk 12`), `--prior key.tsv` (single-letter values seeded, as the brief says), `--keep-fs`.
If the tool cannot take these together, the nearest working flag set is used and named in NOTES.md, unchanged between
the real run and the control.

## Statistics (fixed now)
Over H-graded key codes whose value is one letter (u=v, i=j folded):
- token confirm rate R = aligned occurrences whose chunk equals the key value / aligned non-empty occurrences
  of those codes (unknown `?` tokens excluded);
- code confirmed: >= 2 aligned non-empty occurrences and >= 60% equal to the key value;
- code conflict: >= 2 aligned non-empty occurrences, >= 60% on one letter that is not the key value (or any listed
  alternative). A conflict goes to HYPOTHESES.md with its witnesses (rule 4), never into key.tsv.
- M codes (alternatives `a|b`): reported separately as which alternative the gloss picks; U / '+' / absent labels:
  top chunk reported as a candidate, grade M, untested (a `--try` with control is a later step).

## Control (shuffled gloss)
200 draws: each block's gloss words randomly permuted within the block (seeds 1-200), same alignment flags, same R.
The control changes letter order, which R depends on, so it can fail differently from the target (rule 3, orthogonality
check). Gate: real R > max of the 200 draws AND real R >= 0.60. Gate fails -> the alignment is reported as a non-test
for the key at this transcription quality; nothing confirmed, no conflict logged as evidence.
Also reported, not gated: pass A/B agreement, and R on each block alone.

## Stop rules
Cap 6, box 90 min from 05:48 UTC; no unit started past 80% of either (4.8 / 07:00 UTC). No key.tsv or reading edit in this job.
