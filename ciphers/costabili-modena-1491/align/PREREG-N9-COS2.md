# PREREG N9-COS2, 5 Oct 2026 (addendum to PREREG-N8-COS.md; written and pushed before any image is fetched, any crop cut or any
# re-score computed)

Statistic, filter, control, gate and grading rule: **unchanged from PREREG-N8-COS.md** (`align/run_align.py`: pairs with sign/letter
ratio 0.8-1.25, `tools/interlinear_align.py align --code-prefix @ --keep-fs`, share of aligned tokens agreeing with the sign's majority
value; gloss-shuffle control, 20 seeds; gate per pass real >= shuffle p95 + 0.20 AND real >= 0.430; C only if both passes clear the gate
and both passes' alignment keys give the sign the same value with >= 2 agreeing occurrences each, in >= 2 distinct groups/pairs;
reconciliation licenses M at most). No knob change in either step.

## Step 1 -- re-score of the committed N8-COS passes with the third shape kept apart
Label: the dash + open-loop shape N9-COSV calls "Ω" gets its own label, written `W` (ASCII, so the aligner's @-prefix tokens stay plain),
added to `align/labels.tsv` (the folder's label list, decode-1168 labels + W).
Relabel rule, fixed now and applied mechanically to BOTH committed pass files (`n8cos_pass{A,B}_norm.tsv` -> `n9cos2_pass{A,B}_W.tsv`):
a token is W in both passes wherever pass A reads `z` and pass B reads `o` at the same position of the two sign strings aligned by
`difflib.SequenceMatcher` (equal-length rows: same index). This is N9-COSV's finding (every A-z/B-o split it eye-checked is this shape);
nothing else is relabelled (a W that both passes wrote as z, or both as o, stays as written -- stated as a known under-count).
Crop fix: p1_u03 and p1_u18 are re-cut with the left edge widened (box x0 - 60 px, page pixels); if this worker's eye check of the wider
crop shows the first sign is the looped-descender g (as N9-COSV saw on the full page), that first token is set to `g` in both passes;
otherwise left as written. Boxes written to `align/n9cos2_boxes_fix.tsv`.
Report: both passes' real / shuffle mean / p95 / gate, side by side with the N8-COS numbers (A 0.575 vs p95 0.244; B 0.459 vs p95 0.219),
and the per-sign C table under the rule above; W's value is reported but W can reach C only by the same rule.

## Step 2 -- R1163 and R1165 cipher slips against their clear slips
Material: R1163 P2 (pasted-in cipher slip, ~12 lines) against R1163 P1 (clear slip f.7 laid over it); R1165 P5 (postscript cipher slip,
~8 lines) against R1165 P4 (clear slip with the postscript's content). One DECODE browser login fetches all pages needed for both steps;
images in the scratchpad only, sha1 checked against `images_manifest.tsv`, never committed.
Crops: line bands by `tools/iiif_lines.py --image` (command pasted before the first reader call); within each cipher line, group crops
cut at column ink gaps; where the gap cutter cannot separate groups, the line crop is given and the reader marks group boundaries
(which form was used is reported per slip). Clear slips: line crops.
Readers: 2 blind Sonnet calls per slip (pass A top-down, pass B bottom-up), each returning (i) the cipher slip as tokens per line, cipher
signs by the labels of `align/labels.tsv`, any word written in clear kept as the word, and (ii) the clear slip's text line by line. No
value, key or gloss from this worker. + 1 reconciliation unit per slip by this worker (licenses M at most). Units: 6 (3 per slip).
Pairs: clear words standing in clear in both the cipher slip and the clear slip are anchors; the cipher signs between two consecutive
anchors and the clear-slip letters between the same two anchors form one pair (no forced split inside a span); then the N8-COS ratio filter
and statistic, per pass, per slip and pooled over both slips. Gate and C rule as above (pooled over the two slips per pass; a value at C
needs >= 2 agreeing occurrences in distinct pairs in each pass). If fewer than 4 pairs survive the filter in a pass, that pass is reported
as non-test (the shuffle control has no room to differ), not as a FAIL.
Output: new C values (if any) into `align/key_r1166p12_n8cos.tsv`'s successor `align/key_n9cos2.tsv` (same columns + source column), the
N8-COS file left as committed.
