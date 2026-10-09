# TXE2-OVERLAP -- overlap-zone audit of the baselines' deletions and insertions (PREREG-txeng2-7 O1)

9 Oct 2026, 19:58-20:1x UTC by `date -u`. Worker TXE2-OVERLAP (account 4, Opus) for LANE TX-ENGINEER-2 incarnation 2; TX-RED F23,
PREREG-txeng2-0 Amendment 5 "Overlap sentence". Read-free: no reader, no subagent, no host, no instrument; no sign value
was shown by the tool. Cost: the orchestrator's get_session reading.

Openings of eval truth: 4 (positions only) -- eval_heldout, f178r, birago1572-f152r, spinelli-c1519-confirm. Their per-indel
positions were opened in the session and are **not** committed (`--no-positions`: counts only in their JSONs). Two
deviations inside those openings, disclosed: (1) one whole-item `tx_bench.py --item birago1572-no87` summary line each for
labels/passA/passB (aggregate counts only, used to reconcile the three units' indel totals: A 9 deleted + 1 inserted = 10,
B 8 + 6 = 14); (2) one `tx_bench.py --item spinelli-c1519-confirm` run printed its "top confusions" line once, unmapped
(8 truth-value <- read pairs), before the collapse map was applied -- seen in this session only, not used, not committed.
Eval looks: 0 (no instrument scored).

## Method

`tools/overlap_audit.py` (added this job; `--help`; offline test `tools/tests/test_overlap_audit.py`, 3 tests ok; SYSTEM.md and
tool_shelf rows; `tools/system_map_check.py`: ok, 200 of 200). Per line: (a) overlap of each neighbouring segment pair from
the crop manifest boxes (native px), (b) the same measured by pixel-matching s2's left strip inside s1 (NCC, coarse 4x then
full-res refine, small vertical search for sheared bands), (c) every deletion and insertion of each pass from tx_bench.py's
own `align()` (so the counts are exactly tx_bench's), placed at the line's ink-mass quantile of its truth position
(primary model) or evenly over the 0.5-99.5% ink extent (`--model uniform`, sensitivity), and classed inside a zone / at
the seam (within one sign pitch of a zone edge, or of a cut when segments do not overlap) / outside. "chance" is the share
of all truth positions on the item's lines that fall inside or at the seam -- what a uniformly placed indel would score.
The position model is stated, approximate (signs are not evenly inked); it was changed from uniform to ink-mass after the
initial run showed short lines (dint f128_L02: 8 signs, f152r_L01: 7) spread across the whole crop -- after all items'
initial-run results were seen, so both are reported and the verdict below says where they differ.
Regenerate: `sh benchmark-tx/txeng2/overlap/run_overlap.sh` and `MODEL=uniform sh ...`, then `summarise.py [_uniform]`
(f87's gitignored `lines2x/` crops beforehand: `cd ciphers/ceppo-nevers-fr3251-1570s/harvest && python3 cut_folio_lines.py`,
which reproduced "f87 15 18", the set passes A/B read).

Passes per the brief: no.87 units L (labels.tsv, the committed sequence), A, B; dint pass A, B and the X21 Sonnet pipeline;
f152r passZ_pipeline; Spinelli passZ_pipeline with `--label-map benchmark-tx/txeng/confirm/collapse_map.tsv` (the scoring
convention; 2 deleted + 3 inserted, as the brief says); f87 passC (0 indels), with passes A and B as supplementary rows.

## Per-item table

Overlap in native px; all crops on disk are 1:1 with their manifest boxes (crop width = box width) except f87 `lines2x` (2x).
Pixel match agreed with the boxes on 88 of 88 overlapping pairs at NCC >= 0.95 (exact to 1 px); on f87's 13 no-overlap cuts
no pair reached 0.95 (0.37-0.89), as expected for abutting crops.

| item (split) | brief | stated overlap | measured per line (boxes = pixel) | passes: indels in / seam / out (ink model) | pooled in+seam (ink; uniform) | chance | verdict |
|---|---|---|---|---|---|---|---|
| no.87 dev_tune (dev) | harvest/blind_pass_brief_1572.md | "about 100 px at the 2x scale (50 px native)", crops "upscaled 2x" | f178v_L01-L12: 425, 425 every line (24/24 pairs) | L 0; A 2: 0/0/2; B 4: 1/0/3 | 1 of 6 (0.17; 0.17) | 0.38 | below half: sentence corrected for future briefs only |
| no.87 eval_heldout (eval) | same | same | f178v_L13-L23: 425, 425; f179r_L01-03: 375, 375 (28/28) | L 0; A 0; B 1: 0/1/0 | 1 of 1 (1.0; 1.0) | 0.37 | **overlap-sentence-suspect** (N=1) |
| no.87 f178r (eval) | same | same | f178r_L01-03: 350, 350 (6/6) | L 0; A 8: 1/1/6; B 9: 1/1/7 | 4 of 17 (0.24; 0.35) | 0.33 | below half: corrected for future briefs only |
| dint-f128-print (dev) | f128/pass_instructions.md | "about 150 px" | f128_L02-L05: 1100 every line (4/4) | A 9: 4/0/5; B 5: 1/0/4; X21 Sonnet pipeline 7: 2/0/5 | 7 of 21 (0.33; 0.38) | 0.37 | below half: corrected for future briefs only (pass A alone 4 of 9; 5 of 9 uniform) |
| birago1572-f152r (eval) | txeng2/f152r/blind_pass_brief_f152r.md | 612 native px (manifest `--overlap-note`, not typed) | f152r_L01-L04: 612, 613, 613, 612 (16/16) | Z 1: 0/0/1 | 0 of 1 (0.0; 1.0) | 0.52 | below half under the primary model; **model-dependent** (N=1 flips to seam under uniform); the stated sentence already equals the measurement |
| spinelli-c1519-confirm (confirm) | txeng/confirm/reader_task.txt | "~200 px" | p1c_L01-08: 200; p2c_L01-02: 145 (10/10) | Z 5: 1/1/3 | 2 of 5 (0.40; 0.40) | 0.12 | below half: corrected for future briefs only (p2c is 145, not ~200) |
| ceppo-f87-S (dev) | ceppo harvest/blind_pass_brief.md | "do NOT overlap" | f87_L01-L05: 0 (gap cuts; 13 cuts, no NCC >= 0.95) | C 0; suppl. A 3: 0/0/3; B 10: 0/1/9 | 0 of 0 (passC); suppl. A+B 1 of 13 (5 of 13 uniform) | 0.12 | no indels in the declared pass: rule not applicable; sentence correct |

Uniform-model detail (sensitivity, `summary_uniform.txt`): dev_tune B 0/1/3; f178r A 3/0/5, B 3/0/6; dint A 5/0/4, B 1/0/4,
X21 2/1/4; f152r Z 0/1/0; Spinelli 1/1/3; f87 suppl. A 0/3/0, B 0/2/8. Same verdict on 6 of 7 items; f152r differs (N=1).

## Reading under the declared rule

- One item crosses: **no.87 eval_heldout** (1 of 1 indel at a seam, on both models). It rests on one insertion in pass B
  against a chance share of 0.37-0.45, so the mark is the rule's, not evidence of a mechanism; per the PREREG its re-read
  under the manifest `--overlap-note` is declared a baseline change (never a gain) in the next Amendment. Marked in
  `benchmark-tx/txeng/units/README.md`.
- Below half on both models: dev_tune, f178r, dint-f128-print, Spinelli; f87 has no declared-pass indels. Across the
  three no.87 units and dint the pooled in-or-seam share (13 of 45, ink model) sits at or under chance (0.33-0.38): the
  wrong typed sentence did not concentrate the baselines' indels in the overlaps. What the readers flagged (X21 dev 6,
  X21b dev 3) was a misstatement, not -- on this audit -- the source of most indels.
- f152r: verdict model-dependent with one indel, and its brief already carried the measured sentence, so no correction
  applies; noted, not marked.
- Side finding: `blind_pass_brief_1572.md` says the crops are "upscaled 2x", but the f178r/f178v/f179r crops on disk are at
  native scale (1250 px = box width); the overlap is 425/375/350 px in the image the reader sees, not 100.

## Corrected overlap sentences (for future briefs; the `iiif_lines.py --overlap-note` form, sign width = pitch from ink extent / truth signs)

- f178v: segments of a line overlap by 425 native px (the images you read are at native resolution, so 425 px in each image), about 5 signs (median sign width 83 px, sign pitch); a sign at the right edge of s1 and the left edge of s2 is ONE sign: the last 425 px of s1 and the leftmost 425 px of s2 show the same ink, read it once.
- f179r: segments of a line overlap by 375 native px (the images you read are at native resolution, so 375 px in each image), about 4 signs (median sign width 94 px, sign pitch); a sign at the right edge of s1 and the left edge of s2 is ONE sign: the last 375 px of s1 and the leftmost 375 px of s2 show the same ink, read it once.
- f178r: segments of a line overlap by 350 native px (the images you read are at native resolution, so 350 px in each image), about 5 signs (median sign width 74 px, sign pitch); a sign at the right edge of s1 and the left edge of s2 is ONE sign: the last 350 px of s1 and the leftmost 350 px of s2 show the same ink, read it once.
- f128 (dint): segments of a line overlap by 1100 native px (the images you read are at native resolution, so 1100 px in each image), about 20 signs (median sign width 56 px, sign pitch); a sign at the right edge of s1 and the left edge of s2 is ONE sign: the last 1100 px of s1 and the leftmost 1100 px of s2 show the same ink, read it once.
- f152r: segments of a line overlap by 612 native px (the images you read are at native resolution, so 612 px in each image), about 5 signs (median sign width 116 px, sign pitch); a sign at the right edge of s1 and the left edge of s2 is ONE sign: the last 612 px of s1 and the leftmost 612 px of s2 show the same ink, read it once. (Its brief's own note says "about 14 signs" from the 45 px ink-run width; the pitch counts gaps too.)
- Spinelli p1c: segments of a line overlap by 200 native px (the images you read are at native resolution, so 200 px in each image), about 2 signs (median sign width 105 px, sign pitch); a sign at the right edge of s1 and the left edge of s2 is ONE sign: the last 200 px of s1 and the leftmost 200 px of s2 show the same ink, read it once.
- Spinelli p2c: segments of a line overlap by 145 native px (the images you read are at native resolution, so 145 px in each image), about 1 sign (median sign width 108 px, sign pitch); a sign at the right edge of s1 and the left edge of s2 is ONE sign: the last 145 px of s1 and the leftmost 145 px of s2 show the same ink, read it once.
- f87: segments of a line do not overlap (cut at the column-ink minimum; 0 native px from the boxes, no pixel match at NCC >= 0.95); continue the sign count across them and check the sign at each cut once.

## Proposed BENCHMARK-TX.tsv note column (the lane edits BENCHMARK-TX; nothing edited here)

| item | proposed note |
|---|---|
| birago1572-no87 | overlap: crops overlap 425 (f178v) / 375 (f179r) / 350 (f178r) native px at 1x; passes A/B read under "100 px at 2x"; eval_heldout baseline overlap-sentence-suspect (1/1 indel at a seam, N=1), dev_tune and f178r below half (TXE2-OVERLAP, 9 Oct 2026) |
| dint-f128-print | overlap: 1100 native px, passes A/B read under "about 150 px"; 7 of 21 indels in or at the seam (chance 0.37), below half: sentence corrected for future briefs only (TXE2-OVERLAP) |
| birago1572-f152r | overlap: 612 native px, brief carried the manifest sentence; 1 indel, verdict model-dependent, not marked (TXE2-OVERLAP) |
| spinelli-c1519-confirm | overlap: 200 (p1c) / 145 (p2c) native px vs "~200" stated; 2 of 5 indels in or at the seam, below half (TXE2-OVERLAP) |
| ceppo-f87-S | overlap: none (gap cuts, as the brief states); passC 0 indels (TXE2-OVERLAP) |

## Files and hashes

Commit b22ee0a6a (rebased from local 7d64322a4; tool, test, SYSTEM.md, tool_shelf row, units/README mark, per-item JSON/TXT, run_overlap.sh,
summarise.py): `benchmark-tx/txeng2/overlap/SHA256SUMS` (34 files) sha256
19629234a6698ffa059c1c8bc6382d6e5d759e6eece957e49ba2a0d4b68c47cc; tools/overlap_audit.py sha256 7bbf2ea8595564ad...,
tools/tests/test_overlap_audit.py 99c62197b8bdb441..., summary.txt a536fba7413e8c09..., summary_uniform.txt
a951f30d42a8767f... (full values in SHA256SUMS). This RESULTS.md: commit 019541aa6 and the citation fix after it; its sha256 in the done line.
