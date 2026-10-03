# PREREG -- GAPS98-sufi-fiddle (account-4), 3 Oct 2026, committed and pushed before the vision call

Step (GAPS94 Verdict): one blind Opus vision reading pass on the 7 Figure 1 line crops (words from the hand, not signs),
compared with `../reader/reader_out.json` and `../malay-arabic/spans.tsv` by the GAPS94 S1/S2 statistics.

1. Crops: Bulliet Mizan 2021 Figure 1 refetched once (mizanproject.org, sha1 2825b4427f25eb45e22659d085d44fc4b4cdc0ac, the
   GAPS87 file), cut with the GAPS87 command, scratch only, never committed (no licence stated):
   `python3 tools/iiif_lines.py --image <scratch>/fig1.jpg --out <scratch>/crops --prefix fig1 --region 0,0,2490,1301 --max-width 2490 --centres 148,289,445,613,820,1000,1195 --debug`
   The 7 boxes equal `../fig1-tx/crops_manifest.json`'s (checked by script before this file was written).
2. Reader: ONE Opus 5.5 subagent call, given only the 7 crop paths and `prompt_vision.txt` (no transcription signs, no
   word-list hits, no spans.tsv, no prior readings, no mention of Muhammad or of GAPS94's items; only the per-line group
   counts of ciphertext_fig1.txt so positions can be located, and the same language candidate list as GAPS94). Output:
   `vision_out.json`, saved verbatim.
3. Comparison: `compare_vision.py` (written and committed with this file, before the call):
   - items outside the line's group range are dropped and counted (not re-mapped by x position; x is for audit only);
   - S1/S2 against spans.tsv: `../reader/compare.py` run unchanged on the valid items (GAPS94's statistics);
   - S3 against GAPS94's text-only reader: share >= 1 group on the same line with a text-reader item, vs uniform
     placement of the same width; exact Poisson-binomial one-sided p, all items and H/M items;
   - S4: among S3-overlapping pairs, equal Arabic consonant skeleton (ar_skel), against the chance rate r = share of all
     (vision, text) item pairs with equal skeleton; expected = r x overlapping pairs; descriptive.
   - No gate. Both comparisons are consistency checks between readers of ONE hand copy; S3/S4 agreement means two Opus
     readers converge, not that the reading is right (same model family; the text reader saw this transcription, the
     vision reader sees the copy).
4. Grading (rule 4): no H, no C, no S. A vision item at confidence H/M is graded M; at L it is graded I. A word that BOTH
   readers give at the same span with the same skeleton stays M (at most M, per the brief), flagged "two readers".
5. Box: one vision call (~USD 3). If the reader returns nothing locatable, S1-S4 are reported with N = 0, not as a negative.
