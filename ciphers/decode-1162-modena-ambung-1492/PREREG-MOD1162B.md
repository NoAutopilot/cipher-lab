# PREREG-MOD1162B (account-2 worker, LANE-A2PUSH3), committed 3 Oct 2026 before any label change or re-score

Brief: `.claude/briefs/runs/2026-10-03-acct2-mod1162b.md`. Starting point: commit state after MOD1162 (G 0.729, control p99
0.525, seeds 0..999; tokens C 32, S 10, M 27, I 5, U 3).

## Rule for settling a collided label (g/c/q/z, and every conf '?' sign in ciphertext.tsv)
A sign's label is changed, or its '?' cleared, only when BOTH hold:
1. **Shape:** on a line crop cut by `tools/iiif_lines.py --image` from `images/s_IMG_R1162_I5837_P1.jpg`, the sign matches
   the shape of that label as attested in decode-1168's own crops (`../decode-1168-modena-costabili-1492/images/c*.jpg`),
   and does not equally match the competing label's tile.
2. **Agreement:** the label is one the earlier readings already gave it -- a raw pass (A or B, as recorded in MOD1162's
   NOTES: "2"=z naming, the g/l/v/e, c/p/g, q/e/c splits) or the MOD1162 reconciliation (the current `ciphertext.tsv`).
   No label that no reader proposed is introduced.
If shape is ambiguous between two tiles, the '?' stays and the token stays M. The raw passes' per-sign files are not on
disk (MOD1162 scratch), so condition 2 is checked against what NOTES.md records of them; where that is silent, only
clearing a '?' on the current label is allowed, not a change of label.

**Bias disclosed:** this worker has seen 1168's key and this leaf's gloss. A label chosen by eye can drift toward the
reading the key and gloss predict, which the band-shuffle control cannot see (it shuffles values, not transcription).
Therefore:

## What moves M -> S / C
- A token whose label is **unchanged** and whose '?' is cleared by the rule above gets the MOD1162 grade rules
  (score_g.py `votes`): 1168-C sign agreeing with the gloss at the LCS position -> C; key-transferred, not contradicted -> S.
- A token whose label is **changed** by this pass goes at most to **S**, never C, whatever the gloss says.
- A token still '?' after this pass stays M. No grade moves on the gloss alone.

## Control and gate
score_g.py's band-shuffled control is re-run at **fresh seeds 1000..1999 (1000 draws)** on the settled ciphertext, plus the
original seeds 0..999 for comparison; gate unchanged (G > control p99 AND G >= 0.50). Because of the bias above, the settled
G is **descriptive**: the gate of record stays the raw-pass figures already on file (pass B, the lower, 0.645 vs p99
0.484), and the settled G is reported beside them, not instead of them. If the settled G fell below its own control p99
that would be logged as a FAIL and the change reverted to MOD1162's labels.

## Optional joint alignment
`tools/interlinear_align.py` jointly over 1162's 7 glossed groups + 1168's pairs, --prior 1168 key, only after its
shuffled-gloss control has run and read; skipped if cap/box do not allow (stated in NOTES).

## Judge
`tools/judge_plaintext.py` (it16dip) on the settled decode, beside the leaf's own period gloss score (rule 3 gloss paragraph)
and shuffled-key decodes. Descriptive.
