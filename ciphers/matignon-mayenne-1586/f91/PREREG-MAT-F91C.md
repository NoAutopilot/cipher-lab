# PREREG-MAT-F91C (addendum to PREREG-MAT-F91 and -F91B; 15 Oct 2026, 07:0x UTC by date -u; account-2 worker MAT-F91C, LANE DEFAULT-A2-0509-15)

Written and pushed before any transcription pass, gloss read, alignment or score of this job.
Brief: `.claude/briefs/runs/2026-10-15-ytbiz-default-0509-jobs.md` job MAT-F91C (blocks C and F of f.91v/92r, crops first).

## Step 1 gate (done before this file, no vision call): crops
`f91/regen_f91c.sh` (canvas c98 at max, sha1 dfec5334..., identical to MAT-F91B's): `tools/iiif_lines.py --deskew-region` (fitted
-1.35 deg for C, -1.55 deg for F) `--band-extent --mask-neighbours --max-width 1600 --overlap 80`. Overlays and every crop checked by eye:
each crop holds one line (C: 13 lines; F: 14 lines, of which F10, F11 are clear French only). Per-line band and crop heights in
`f91/crops_manifest_f91c.tsv` (band 102-160 px, crop 141-238 px; MAT-F91B's strips were a fixed 150 px window on unrotated lines).

## Material
- Lines passed: C1-C12 and F1-F9, F12, F13, F14 (24 lines). C13 (bottom of the region, mostly clear "Oultre que ... de Haultfort") is left
  out to keep each call at <= 12 images; recorded as a gap. Each line image = its s1 segment above its s2 segment (thin grey rule; 100 px
  native overlap, about one sign), the layout of MAT-F91B's reference chart; segments are not re-stitched side by side.
- Two blind Sonnet passes (A, B), 2 calls each (12 line images per call), reader brief `f91/PASS_BRIEF_F91C.md` = `PASS_BRIEF_F91B.md` with
  one added sentence on the segment overlap; the f.78v reference chart as before. Readers never see key.tsv, the gloss or any decoded value.
- `tools/reconcile_passes.py` A B; disagreements are not settled by eye (cost) and enter the alignment as unknowns (`?`), as MAT-F91 did.
- Gloss: one Opus read of the margin line crops (glC 20 lines, glF 18 lines from the same regen, `--region 900,1040,860,1580` and
  `4460,2640,840,1560`), then one Sonnet check pass on the same crops if the cap allows (else the read stays unchecked and is said so).

## Quality gate before any alignment (new, fixed now)
Pooled pass A/B agreement (reconcile_passes.py) >= 0.65. Below it: no alignment, no R, logged as a transcription-quality non-test
(MAT-F91B's 45.1% shape). MAT-F91's 80.5% on A/B/D is the reference.

## Alignment, statistic, control, gate
Unchanged from PREREG-MAT-F91 / -F91B: `f91/align_f91.py` with the block list C, F (and a separate ciphertext/gloss input file for this job),
`--prior key.tsv` H single-letter values, R on H single-letter codes, 200 within-block gloss-word shuffles (seeds 1-200).
Gate: real R > max of the 200 draws AND R >= 0.60, on C+F pooled; per block reported. Confirm/conflict rules as PREREG-MAT-F91; conflicts with
>= 2 occurrences go to HYPOTHESES.md with witnesses (block, line), never summed with MAT-F91's counts into a majority override.
Candidates for unkeyed labels reported M, untested. No --try (its power control failed in MAT-F91B). No key.tsv, reading or grade edit.

## Stop rules
Cap 5, box 75 min from 06:58 UTC (end 08:13); no unit started past 80% of either (4.0 / 07:58 UTC). Pricing: Sonnet vision call ~0.6, Opus
look ~1.0. openapi.bnf.fr <= 6 (1 used).
