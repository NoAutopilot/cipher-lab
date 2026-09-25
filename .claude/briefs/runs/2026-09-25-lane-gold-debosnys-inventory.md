JOB GOLD-4C: Debosnys sign inventory, split by eye, and a tool fix. Fable (claude-fable-5-1). Stop and push at $10 or 60 minutes, whichever first. Lane: LANE GOLD orchestrator session_01DKDynpdEwZK5EokxtjCM3P. Written 25 Sept 2026 18:02 UTC.

Read first: `.claude/briefs/runs/2026-09-24-lane-r4-common.md`, `.claude/briefs/runs/2026-09-25-lanes-7b-COMMON.md` (binding), `ciphers/debosnys-1883/NOTES.md` (the GOLD-4A section in full), `glyphs/merge.tsv`, `tools/glyph_atlas.py --help`. Claim in ROOM. GOLD-4B (Sonnet) works on clear_poems/sektu/form-test files at the same time; do not edit those.
Intake gate (live, 18:02 UTC): debosnys-1883: open (line 1) -- edition/page or full-text-search citation found within 6 lines  (exit 0)

Why: GOLD-4A merged 90 k-means clusters into 68 ids but left 39 heterogeneous "junk-drawer" clusters (MISC-*) and the SUN cluster mixed; a blind second pass on cryptogram 4 agreed with the machine pass on only 22.4 percent of signs. No cryptanalysis is worth running until the sign inventory is right.
Do:
1. Split every MISC-* cluster and the SUN cluster by eye from the crops (glyphs/crops, contact sheets) into real sign shapes, extending merge.tsv to a per-box assignment where a cluster is mixed (`glyphs/box_labels.tsv`: box id -> sign id, confidence). Name signs by shape; keep pictograms as signs. Aim: every box has a sign id with confidence, and every sign id has 3+ exemplars on a new reference sheet `glyphs/inventory.png` (or says why it has fewer).
2. Add `--exclude-page` (or equivalent) to `tools/glyph_atlas.py classify` so kNN never votes with the target page's own unlabelled boxes (GOLD-4A's standalone workaround), with a line in its --help and a case in its offline test in tools/tests/.
3. Settle the c4 rows of `disagreements.tsv` on the image with the new inventory; report how many disagreements were inventory confusion (two ids for one shape, or one id for two shapes) versus segmentation versus reading error.
4. Rebuild pass A for all four cryptograms from box_labels.tsv; recompute N, K, IC per cryptogram with scripts/compute_ic.py's controls, and write `ciphertext_draft.tsv` (not ciphertext.txt: a second blind pass on the new inventory is the next Sonnet job and decides that). Write a "GOLD-4C, inventory" section in NOTES.md.
Do not decode, do not anneal. You may read images (this is inventory design, not a transcription pass). Push per step.
Done line: K after split, share of boxes at H/M/L, disagreement classes on c4, N/K/IC per cryptogram vs controls, no cost figure. Rule 10 wording.
