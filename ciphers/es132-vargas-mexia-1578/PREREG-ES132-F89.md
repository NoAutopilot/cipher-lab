# PREREG ES132-F89 -- es132-vargas-mexia-1578: two-crop look at the 40 unsettled f.89 duplicate candidates (account 4 worker for LANE DEFAULT-A4-0235-15, 15 Oct 2026, written 02:56 UTC by `date -u`, before any look call is made or any score computed)

Brief: `.claude/briefs/runs/2026-10-15-acct4-default-0235-jobs.md` "### ES132-F89" (continues ES132-40, NOTES.md, which stopped for want of a
native duplicate image). Inputs: the 40 rows of `dup_settled.tsv` whose decision starts `keep:` (30 `keep:R3a-not-isolated`, 10
`keep:R1-not-agreed`; f.89r 15, f.89v 15, f.90r 9, f.91r 1), `dup_align.tsv`, `ciphertext_f89r/f89v/f90r/f91r.tsv` and
`ciphertext_f93r ... f95r.tsv` as committed at origin/main 15 Oct 2026 02:5x.

## Images (not committed)
f.89 side: the committed native regions re-cut with the ES132-40 commands (`tools/iiif_lines.py --image images/src_..._f86/f87/f88_... --follow-slope
300 --slope-margin 40 --debug`). Duplicate side: the five A3V3-ES9396 regions of canvases 90-92 fetched once from openapi.bnf.fr (IIIF v3, `--iiif-host
openapi`, same regions and cut parameters as `regen_images.sh fetch f93r..f95r`), into the session scratchpad. For each item the two half-line crops
of a line are joined side by side, the f.89 line on top (panel A), the duplicate line below (panel B), labelled, one composite per item.

## Decoys (planted, >= 20% of items)
12 decoys from `dup_align.tsv`: pairs on f.89r/f.89v/f.90r/f.91r whose f.89 token and duplicate token are both unflagged (firm on both sides) and
whose class is `differ-base` (4), `differ-vowel` (4), `differ-mark` (4), drawn with `random.Random(1589)` after excluding any pair within 2 tokens of
a candidate on the same f.89 line. For a decoy the proposal P is the duplicate's token, which the firm f.89 reading says is wrong for f.89.
52 items (40 candidates + 12 decoys = 23% decoys), shuffled with `random.Random(15)` into 3 batches (18/17/17).

## The look (per item, blind to item kind)
One Sonnet vision subagent per batch sees, per item: the composite, the position of the token in each panel (1-based index in the line, cipher
tokens only) with the transcribed neighbours (two before, two after) on each side, the notation of the f.89 pass prompt (run2/pass_prompt_f89r.md,
marks by shape name), and one proposal P. It writes first what it sees at the A position (free transcription), then a verdict on whether
panel A's token is P: `yes`, `no` or `unclear`. The current f.89 reading of the token is NOT shown (for decoys it would reveal the answer; for
candidates it would anchor). The item's kind is never shown.

## Gate (computed once, from the three batch files, before anything is applied)
Decoys rejected (verdict `no` or `unclear`) >= 80%, i.e. >= 10 of 12. If the gate fails the look licenses nothing: no candidate is applied, the
result is logged as a non-test of this instrument at this N, and the 40 rows stay as they are.

## Application (only if the gate passes)
A candidate with verdict `yes` is applied: the f.89 token becomes P, unflagged (for the 6 `confirm` rows P equals the f.89 token and only the '?' is
removed). `no` and `unclear` leave the row unchanged ('?' kept). Applied tokens are graded M (rule 4; the f.89 pages carry no H/C/S). Applied through a
`settle_look.py` beside `settle_dup.py` (same position-checked edit of the ciphertext files, the old token kept in its own output TSV, `--check`
exit 1 if stale), then `test2.py` regenerates the f.89 readings and every folder `--check` is run.

## Reported beside the gate
Decoy rejection k/12; candidate verdict counts (yes/no/unclear) by action class (propose-base, propose-vowel, propose-mark, confirm); the reconcile
step: this worker reads every `yes` against the composite before applying and lists any it disagrees with (it does not overturn a verdict;
disagreements are logged and the item is held back, never added).
