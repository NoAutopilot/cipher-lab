# PREREG-MAT-F91E (addendum to PREREG-MAT-F91, -F91B, -F91C; 15 Oct 2026, 08:3x UTC by date -u; account-2 worker MAT-F91E, LANE DEFAULT-A2-0810-15)

Written and pushed before any transcription pass, gloss read, alignment or score of this job.
Brief: `.claude/briefs/runs/2026-10-15-ytbiz-default-0810-jobs.md` job MAT-F91E (f.92r block E, MAT-F91C's method).

## Step 1 gate (done before this file, no vision call): crops
`f91/regen_f91e.sh` (canvas c98 at max, 1 openapi.bnf.fr request, sha1 dfec5334..., identical to MAT-F91B/C's): `tools/iiif_lines.py
--deskew-region` (fitted -1.80 deg) `--band-extent --mask-neighbours --max-width 1600 --overlap 80` on cipher region 5230,1200,2900,680
(MAT-F91B's E estimate 5255,1240,2850,600, padded). 7 bands: L01 = clear "...reigment se feroit pareillement ...", L02-L06 = the five
cipher lines E1-E5 (E1 opens with clear "bas meilleur", E5 ends in clear "J'ay veu, Sire, ..."), L07 = clear. Overlay and every crop
checked by eye: one line each. Gloss region 4470,1290,780,620, same flags: 8 bands = the 8 margin lines by eye.
One layout change from MAT-F91C, fixed now: the two segments overlap by 300 native px (about 4 signs); s2 is trimmed by 200 px at its left
so the overlap is 100 px (about one sign), which is what the unchanged reader brief says. Done in `regen_f91e.sh`.

## Material
- Lines passed: E1-E5 (5 line images, s1 above s2, grey rule), one call per pass. Two blind Sonnet passes (A, B), reader brief
  `f91/PASS_BRIEF_F91E.md` = `PASS_BRIEF_F91C.md` verbatim (same f.78v reference chart). Readers never see key.tsv, the gloss or any value.
- `tools/reconcile_passes.py --keep-dots` A B; disagreements are not settled by eye and enter the alignment as unknowns (`?`).
- Gloss: one Opus read of the 8 margin line crops, `f91/gloss_f91e.tsv` (uncertain words left out of the normalised column), not
  Sonnet-checked unless the cap allows.

## Quality gate before any alignment (unchanged)
Pass A/B agreement (reconcile_passes.py) >= 0.65 on E. Below it: no alignment, no R, logged as a transcription-quality non-test.

## Alignment, statistic, control, gate (unchanged)
`f91/align_f91e.py` = `align_f91c.py` with block list E and file names only; `--prior key.tsv` H single-letter values; R on H single-letter
codes; 200 within-block gloss-word shuffles (seeds 1-200). Gate: real R > max of the 200 draws AND R >= 0.60, on E.
Small-N note fixed now: E is one block of ~110 signs, so n (aligned H-letter tokens) may be ~50-70; the gate is applied as written, and an
E+C+F pooled R (same script, blocks C, E, F, same seeds) is reported as a secondary number only, not a gate.
Confirm/conflict rules as PREREG-MAT-F91; conflicts with >= 2 occurrences go to HYPOTHESES.md with witnesses (block, line), never summed
with earlier counts into a majority override. Unkeyed-label candidates reported M, untested. No --try, no key.tsv, reading or grade edit.

## Stop rules
Cap 4, box 75 min from 08:23 UTC (end 09:38); no unit started past 80% of either (3.2 / 09:23 UTC). Pricing: Sonnet vision ~0.6, Opus look
~1.0. openapi.bnf.fr <= 4 (1 used).
