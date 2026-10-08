# PREREG OLD-SIBS (8 Oct 2026, written and pushed before any blind pass was read)

Job: OLD-SIBS (account 4, brief .claude/briefs/runs/2026-10-08-acct3-old-sibs.md). Leaves 004 (folios 59v/60r), 005 and
007 (61v/62r); crops `images/crops_L457/` (L4a 15 + L4b 30 + L5a 4 + L5b 8 + L7a 3 + L7b 25 = 85 line crops; commands in
NOTES.md section 22). Blocks named by leaf: L4, L5, L7.

1. Two blind passes per leaf, Sonnet subagents, crops only (no key, no reading, no prior transcription, no full-page
   image). Pass A reads the crops in order, pass B in reverse order. Notation exactly as PREREG_OLD-PASS2 item 1 (letters
   as Latin cursive letters; digit-like signs as digits; the G-shaped ligature as `l7`; superscript small a as `^a`).
   Every word on the line is transcribed, plain or cipher. Output TSV: block, line (crop name), pos, token, conf.
2. Normalisation of both passes alike: `transcription/diff_pass2.py`'s `norm_tok` (PREREG_OLD-PASS2 item 2).
3. Figure: per-sign disagreement A vs B = sum of per-line Levenshtein of normalised line strings / sum of mean line
   lengths, per leaf and pooled. Agreement, not accuracy.
4. Rule: a leaf over 10.0% is recorded as split; no third pass. Reconciliation goes ahead either way (one unit per leaf,
   `tools/reconcile_passes.py` then eye on the crop; a sign the crop does not support -> token M; never chosen because it
   decodes better). A split leaf's reading is reported as a draft, graded no higher than M where the passes split.
5. Solve: (a) fixed B/C1 key (a=4 e=8 i=3 o=7 u=2; 5 final -> s, 6 -> b) applied to the reconciled cipher tokens; (b) the
   free solve `scripts/solve_digit_subst.py` on the same tokens with every clear letter fixed as a crib, plus a matched
   control at these leaves' own N and K with injected noise at the measured A/B disagreement. Both numbers side by side.
   Agreement of (a) and (b) on the digit->vowel map is the test; a different map is reported as a finding.
