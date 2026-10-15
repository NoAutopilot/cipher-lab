# PREREG ES132-BLIND -- es132-vargas-mexia-1578: blind single-crop read of the 40 unsettled f.89 duplicate candidates (account 4 worker for LANE DEFAULT-A4-0235-15, 15 Oct 2026, written 03:3x UTC by `date -u`, before any read call is made or any score computed)

Brief: `.claude/briefs/runs/2026-10-15-acct4-default-0235-jobs.md` "### ES132-BLIND". Continues ES132-F89 (NOTES.md), whose two-crop look with a
proposal shown failed its decoy gate (8/12). Different instrument: no proposal, no second copy beside the crop. Inputs as committed at origin/main
15 Oct 2026 03:2x: the 40 `keep:` rows of `dup_settled.tsv`, the 25 `flag-removed` rows, `ciphertext_f89r/f89v/f90r/f91r.tsv`, `ciphertext_f93r..f95r.tsv`.

## Images (not committed)
Same crops as ES132-F89 (scratchpad only): f.89 side re-cut from the committed `src_*` regions (ES132-40 commands); duplicate side the five A3V3-ES9396
regions of canvases 90-92 from openapi.bnf.fr (<= 6 requests), same cut parameters. One image per read: ONE line only (its two half crops joined at the
manifest seam), labelled with a neutral read id; never a second panel.

## Reads
- Candidate reads: for each of the 40 candidates, read C-A (its f.89 line, its f.89 position) and read C-B (its duplicate line, its duplicate position).
  80 reads.
- Decoy reads: 12 already-settled tokens from the `flag-removed` rows of `dup_settled.tsv` (both copies read the same and the '?' was removed): 8 read on
  the f.89 side (truth = `f89_tok_new`), 4 on the duplicate side (truth = `dup_tok`), 12 distinct rows drawn with `random.Random(1578)`.
- 92 reads, shuffled (`random.Random(132)`) into 3 batches; the two reads of one candidate are forced into different batches.
- Per read the reader is shown: the line image, the 1-based token position, the transcribed neighbours (two before, two after, '?' stripped), and the
  notation of ES132-F89's prompt. It is NOT shown the token's current reading, any proposal, the other copy, or the read's kind. It writes one token in
  the notation, or `unclear`.
- One Sonnet vision subagent per batch (3 calls), plus this worker's reconcile (no overturning).

## Gate (computed once, before anything is applied)
Decoy accuracy: a decoy read is right when the reader's token equals the truth exactly (number, vowel sign and mark; `unclear` counts as wrong).
Gate: >= 10 of 12 right (>= 80%). If the gate fails, nothing is applied and the result is logged as a non-test of this instrument at this N.

## Settlement (only if the gate passes)
A candidate settles only where C-A and C-B are both non-`unclear` and equal exactly. The f.89 token then becomes that value, unflagged, grade M (rule 4;
the f.89 pages carry no H/C/S). Otherwise the row is unchanged ('?' kept). Applied through `dup_settled.tsv` (decision `blind-agreed`), the ciphertext
files edited position-checked, `test2.py` regenerating the f.89 readings, every folder `--check` and `tools/decode_key.py . --check` run.
Reconcile: this worker looks at every settling candidate's two crops before applying and lists any it disagrees with; such a row is held back, never added.

## Reported beside the gate
Decoy k/12 (f.89 side k/8, duplicate side k/4); candidates agreed / disagreed / unclear; for agreed rows how many equal the current f.89 token (flag removal
only) vs equal the duplicate token vs neither.
