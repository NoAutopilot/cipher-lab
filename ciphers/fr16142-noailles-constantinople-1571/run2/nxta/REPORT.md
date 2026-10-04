# RUN2-NXTA -- two blind passes of c510 (training leaf), 4 Oct 2026, 02:46-03:0x UTC (account 1 worker, for LANE-RUN2)

Brief: `.claude/briefs/runs/2026-10-04-acct1-run2-wave1.md`, RUN2-NXTA. No decode, no alignment, no key application (the wave-2
pre-registration stays blind). Intake gate (02:46 UTC): `fr16142-noailles-constantinople-1571: partial (line 1) -- edition/page or
full-text-search citation found within 6 lines`, exit 0.

## What was done
- **Leaf c510 done in full: 37 cipher lines (L00 = the cipher tail of manuscript line 4, after the clear "...la reception dicelle que";
  L01-L36 = the 36 full cipher lines down to the foot of the page).** c511 not started (see "Why c511 was not started").
- Native canvas 510 fetched once (4986x7169, 1 Gallica request). Crops (`regen.sh` re-cuts them; strips are kept out of the repo):
  ```
  python3 tools/iiif_lines.py --image c510_full.jpg --region 1100,1040,3650,4680 --centres 82,213,...,4582 (36, from the row ink
    profile of the block's left 500 px) --follow-slope 300 --slope-margin 15 --max-width 1900 --overlap 100 --prefix c510 --out crops510 --debug
  region 3650x4680, 36 lines, 36 bands x 2 segments; slopes -0.018..+0.008 (drift -65..+29 px over the block, pitch 128)
  wrote 72 crops
  ```
  Overlay checked by eye: one text row per band. Deviation from the brief's command: `--max-width 1800` cut this 3650 px block into 3
  segments overlapping by ~875 px (double-count risk), so `--max-width 1900` (2 segments, 150 px overlap) was used; a red split line is
  drawn in the middle of each overlap (`mark_overlap.py`) and readers counted a sign on the side of the line its centre falls.
  L00 was cut by hand (`crop((3420,905,4720,1090))`): the region started below it.
- Passes: 6 Sonnet subagent calls (A and B, three line groups each: L00-L12, L13-L24, L25-L36, ~375 signs per call), each given only the
  crop paths, Tomokiyo's table image (cryptiana CharlesIX_Acqs2.png, scratchpad, not committed) and the NX-RECUT label convention
  (`prompt_template.md`). Groups were ~12 lines rather than "at most 10" so each call held the brief's ~400 signs (3 calls per pass).
  A 1130 signs, B 1123.

## Numbers
| measure | value |
|---|---|
| err_2reader, raw (`?{desc}` = unnamed) | 484 / 1157 aligned columns = **41.8%** |
| err_2reader after the label convention (`descmap.tsv`: 20 free descriptions mapped to table labels from the table zoom, before reconciling) | 452 / 1156 = **39.1%** (272 label-vs-label splits, 180 gap or unnamed-vs-label) |
| reconciled.tsv | 1156 signs: H 538 (both readers, same label, both confident), M 618 (166 agreed low-confidence, 158 by family rule, 180 one reader only, 114 split taken from A) |
| audit: this worker's own read of 2 lines NOT used to set the rules (L06, L30; 61 signs) vs reconciled | 39/66 = **err 0.409**; H-graded signs 21/28 right (**0.25 wrong**), M 18/38 |
| same audit vs raw pass A / pass B | 0.476 / 0.444 |
| err_true | **not measurable**: no BENCHMARK-TX item of this hand; the audit "truth" is one more reader (this worker), not a benchmark |

## What the splits are
The disagreement is naming, not cutting (as on c262, NX-RECUT): whole glyph families are named inconsistently, and in some both readers
agree on the wrong label, so even H is unsafe (`focus.tsv`):
- hash family (57 split columns): the tall H with two crossbars (table o row 2) is called r1 by both readers, and the triple-stroke ### (table r row 1) is called o1/e2.
- Y family (28): the plain Y (s1) is called W:les or s2.
- box-on-bar nomenclator signs (36): W:par / W:qui / W:que / W:le named inconsistently; c510 has both 'Fu' (F with a cup) and a box hung under a bar.
- n1/u1 (29), e3/r2/m1 (26), p1/i2 (12; both shapes occur), g1/N1 for a '+ with a tick' sign (12), e1/d1 (9).
Family rules applied in `family_rules.tsv` were ruled from L01, L02, L12, L20 against the table zoom; they fix some pairs but cannot fix
an agreed wrong label (the reconciler only sees splits).

## Look-alike pass / sorter
err_2reader > 10%, and no RUN2-NXATL atlas sheet existed at 02:5x UTC, so `tools/lookalike_pass.py` was not run; `focus.tsv` lists the
sign families that split for the sign sorter (with example positions). Not a sorter sheet: no exemplar images were cut here.

## Why c511 was not started
Pacing allowed it, but the instrument does not: the audit puts the reconciled c510 text at ~40% sign error with 25% of H-graded signs
wrong, the same table-image Sonnet pass rule 3's third-attempt clause already retired for the c262 gate (NX-RECUT). A second leaf read the
same way adds ~1,200 more signs at the same error, not information; the next instrument is the atlas (RUN2-NXATL) and settled sorter
labels, then re-label these passes (or re-read c510-c511) against them. c511: 0 lines done.

## For wave 2 (RUN2-NXALN)
Use `reconciled.tsv` only with its grades and this report's audit figure; an alignment gate run on it should expect ~40% sign noise and
treat the hash and Y families as merged classes unless the atlas separates them. The atlas cluster ids (NXATL) need no reader to name a
sign and are likely the better instrument for the same alignment.

## Files
passA_raw.tsv / passB_raw.tsv (as written by the readers), passA.tsv / passB.tsv (long format after `descmap.tsv`), agreement.tsv,
disagreements.tsv, reconciled.tsv (leaf, line, pos, label, grade, A, B, how), focus.tsv, audit_read.tsv + audit_cmp.py, family_rules.tsv,
reconcile_rules.py, to_long_map.py, rebuild.sh (`sh .../rebuild.sh --check` from the repo root: exit 0 = committed files match a rebuild),
regen.sh + mark_overlap.py (crops), crops_manifest.json, prompt_template.md.

Requests: gallica.bnf.fr 1 (native c510); cryptiana.web.fc2.com 2 (henryiii.htm, CharlesIX_Acqs2.png). Subagent calls: 6 Sonnet + this
worker's reconciliation and 2-line audit (1 unit).
