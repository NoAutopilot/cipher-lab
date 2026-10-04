# Pre-registration: gloss-masked, cipher-only read of f.84r as a known-answer control (RUN1-HAR, 4 Oct 2026)

Committed before either blind pass was run. Question (A2-HAR7 caveat): did the two A2-HAR7 passes, which read the
cipher with the gloss in view, project gloss letters into sign names? If so, `key_f84_f90.tsv` (0.819 consistency,
19/20 concordance with Bourdeau) is inflated.

Material. `images/f84r_masked/` -- 15 cipher lines x 2 segments, cut by `tools/iiif_lines.py --follow-slope 400
--slope-local` from a page canvas rebuilt from the committed native f.84r crops (no DECODE fetch), every row outside
[line peak - 78, line peak + 36] painted white by `gloss/mask_f84r.py`; L10_s2 (no cipher, gloss only) blanked
entirely. Checked by eye at half size: no readable gloss word in any crop.

Readers. Two blind Sonnet passes (`gloss/PASS_PROMPT_masked.md`), same sign code as A2-HAR7, gloss never shown,
no repository file named but the crops. Replies written unchanged to `gloss/passA_masked.tsv`, `gloss/passB_masked.tsv`.

Reconciliation (mechanical, for the gate). My own eye is contaminated (I have read gloss_pairs.tsv), so the gated
reconciliation is A2-HAR7's rule with no arbitration: per band, align the two token strings (difflib on tokens);
agreed tokens kept, the l/p naming split goes to p (as A2-HAR7), every other split or gap becomes `?`. Word
dividers " / " kept where both passes have them at the aligned position. Output `gloss/gloss_pairs_masked.tsv`
(same columns as gloss_pairs.tsv; gloss column copied from gloss_pairs.tsv, f84r rows only).

Statistics (gloss/run_align.py unchanged except a --pairs/--suffix option; same aligner, same controls, 20 seeds):
- S_m = key consistency of the masked pairs; C_m = concordance with Bourdeau's signs.tsv values (n>=3 signs).
- Baseline on the same 15 f84r rows from the gloss-in-view pairs (gloss_pairs.tsv restricted to f84r), S_v, C_v,
  computed by the same command, so the comparison is f84r-to-f84r.
- Nulls on the masked pairs: pair-shuffled (derangement) and letter-shuffled, 20 seeds each.
- err_2reader (masked) = token disagreements / aligned tokens between passA_masked and passB_masked, reported beside
  A2-HAR7's gloss-in-view 117/814 (0.144).

Gate.
- G1 (the control can read at all): S_m > max of both null families. Fail -> "non-test: masked read too noisy", no
  inference about projection either way.
- G2 (no material projection): G1 passes AND S_m >= S_v - 0.10 AND C_m >= C_v - 0.15. Pass -> the gloss-in-view key
  is not materially inflated by projection at this N. G1 pass, G2 fail -> projection (or masking cost) of that size is
  shown; key_f84_f90.tsv values supported only by the gloss-in-view read drop to grade M.
- Also reported, not gated: per-sign value table from the masked read beside key_f84_f90.tsv; whether 8 = d survives.
