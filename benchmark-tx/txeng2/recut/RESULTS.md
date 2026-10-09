# TXE2-RECUT results: fr.3623 f.23r masked re-cut from the Gallica native region (9 Oct 2026, 18:39-18:4x UTC by date -u)

LANE TX-ENGINEER-2 incarnation 2, round 5, PREREG `benchmark-tx/PREREG-txeng2-5.md` section R3 (binding). Item
bir1591-f23r-gloss. **Outcome: STOPPED after the crop step, as R3 and the brief require. Gloss letters are still
visible on the masked crops after the one tighter-mask try, so no blind reads ran, no passA_masked/passB_masked/passZ_masked
exists, and nothing was compared.**

truth-unknown (Amendment 3): no err_true claimed, no pool entry.

## Source (disk only, 0 network requests)
The native region is `ciphers/fr3621-dinteville-1592/f3623/src_ark_12148_btv1b525245007_f55_560_1780_2950_1560.jpg`
(2950 x 1560, Gallica ark:/12148/btv1b525245007 f.55, region 560,1780,2950,1560, fetched 3 Oct 2026). The brief places it in
`benchmark-tx/txeng2/bir1591-f23r-gloss/`; it is in the Dinteville folder's f3623/, where TXP-B23's RESULTS names it. Gallica
was not contacted.

Line centres (region y, at the left end of each line; the lines rise about 0.05 px per px to the right, roughly 140 px over
the leaf): the 8 cipher rows and the 8 gloss rows, each given as its own line so every band edge falls between a gloss row
and a cipher row (TXP-B23's 17-centre method). The cipher rows are bands 2, 4, ..., 16.

## Cut 1: the folder's earlier parameters (`--band-extent 0.05`, `--follow-slope 150 --slope-local`)
```
python3 tools/iiif_lines.py --image ciphers/fr3621-dinteville-1592/f3623/src_ark_12148_btv1b525245007_f55_560_1780_2950_1560.jpg --out benchmark-tx/txeng2/recut/crops --prefix f23r --max-width 1600 --overlap 250 --band-extent 0.05 --mask-neighbours --mask-keep 0.5 --follow-slope 150 --slope-local --overlap-note --debug --centres 190,320,400,480,570,640,710,800,865,925,1010,1080,1170,1235,1330,1395 --only-lines 2,4,6,8,10,12,14,16
```
(The output was then moved to `try1_bandextent/`; its manifest's crop names are unchanged.)
Overlay verdict: **gloss visible in full.** In every crop the whole gloss row above the line and the whole gloss row below
it are legible. Example: L02_s1 shows "dopo ... ispacisio ... fato" above the signs and "lei di monsiur sillerve qu" below.
Cause: `--band-extent` moves each band edge out to the row-profile minimum between two centres. On this sloping leaf the
unsheared profile has its minimum out near the neighbouring gloss rows, so the bands grew to 95-146 px around 80-130 px
centre spacings (L02 band rows 218-364 around centre 320, with gloss rows at 190 and 400; manifest `band_extent`). With
gloss ink inside the band, `--mask-keep 0.5` keeps it.

## Cut 2: the one tighter-mask try (midpoint bands: `--band-extent` dropped, everything else the same)
```
python3 tools/iiif_lines.py --image ciphers/fr3621-dinteville-1592/f3623/src_ark_12148_btv1b525245007_f55_560_1780_2950_1560.jpg --out <scratch>/t2 --prefix f23r --max-width 1600 --overlap 250 --mask-neighbours --mask-keep 0.5 --follow-slope 150 --slope-local --overlap-note --debug --centres 190,320,400,480,570,640,710,800,865,925,1010,1080,1170,1235,1330,1395 --only-lines 2,4,6,8,10,12,14,16
```
(Copied to `try2_midpoint/`: 16 crops, the debug overlay, manifest.json and crops_note.md.) Bands are 70-104 px; the mask
removed 51-252 components per crop and kept 50-207. Most gloss is gone. I looked at all 16 crops myself. **Gloss letters
remain**, boxed in `try2_gloss_marked.jpg` (blue = letter, orange = stroke fragment) and listed in `gloss_marks.tsv`:
- letters: L04 "q" (in the s1/s2 overlap, so in both segments); L06 "a" (in both segments) and "fr" (s2); L10_s2 "i"
  with its dot, and "up";
- fragments: L10_s1 a mark above a sign; L12_s2 and L16_s1 "g" tails; gloss ascender stems ("l", "ll", "d") under
  L02, L04 and L08 (10 boxes);
- L14_s2 and L16_s2 hold no cipher, only the plain subscription and signature. A read would drop them; they are not gloss.

**Why a further tighter mask cannot clear this.** `--mask-neighbours` whitens only ink components with less than
`--mask-keep` of their pixels inside the band. A gloss letter that survives is therefore joined to in-band ink or half
inside the band. A connectivity check on the try-2 crops (ink < 150, 8-connected) bears this out. The "up" on L10_s2 is one
component of 1984 px spanning rows 0-94, down into the cipher row's core. The "q" on L04_s2 is one component of 3348 px
spanning rows 0-110. Both are ink-joined to the cipher signs beneath them. Raising `--mask-keep` (TXP-B23 tried 0.6 and 0.75
on the DECODE copy) deletes those signs along with the gloss, as TXP-B23 found. The native resolution does not separate
gloss strokes from cipher strokes where the decipherer's pen touched the signs.

Verdict (overlay checked, both cuts): **gloss remains -> STOP after the crop step, no reads** (R3: "If the masked crops still
show gloss letters on the overlay the job stops after the crop step and says so").

## What was not done (by the brief)
- No blind reader pass ran. passA_masked.tsv, passB_masked.tsv and passZ_masked.tsv were not written, and reconcile_passes.py
  was not run.
- Not computed: err_2reader (masked vs gloss-visible), per-position agreement with passA/passB/passZ_pipeline, the
  confusion table, and the align-conflict share.
- The gloss-visible pass files (`benchmark-tx/outputs/bir1591-f23r-gloss/pass*.tsv`) were not opened.
- bir1591-f23r-gloss.truth.tsv and its jackknife variant were not opened. tx_bench did not run, and no err_true was written.

## Suggestions for the lane (one line each, not done, Usage 7)
- A masked read of this leaf needs a different instrument than component masking. Options: an inpainting or a stroke-level
  (not component-level) gloss removal, checked on the overlay; or a reader brief that names the remaining marks by
  position (gloss_marks.tsv) as not-cipher, which declares partial gloss visibility instead of removing it.
- Do not reuse `--band-extent` on this leaf, or any leaf with interlinear rows this tight: the profile-minimum edge move
  grows the band into the gloss row.

## Calls, tokens, files
- Subagent calls: 0 (no reads). Units spent: the crop step only (2 cuts + the overlay and crop checks).
- Requests per host: 0 (Gallica 0; no network).
- Files committed (sha256 below): try1_bandextent/ (16 crops + debug + manifest + note), try2_midpoint/ (same), gloss_marks.tsv,
  try2_gloss_marked.jpg, this file. None is a before-compare file, because nothing was compared.
- Cost: the orchestrator get_session reading.

Openings of eval truth: 0

## sha256
All committed files are listed with their sha256 in `SHA256SUMS` (this folder), written before the commit.
