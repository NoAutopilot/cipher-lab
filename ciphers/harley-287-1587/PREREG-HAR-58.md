# PREREG-HAR-58 (15 Oct 2026, 17:5x UTC by date -u), pushed before any image fetch, read or score

Job: `.claude/briefs/runs/2026-10-15-acct4-default-1735-jobs.md` "HAR-58". Continues HAR-41R (PREREG-HAR-41R.md, NOTES.md "## HAR-41R").
Unit: BL Harley MS 287 f.41r (DECODE R8480 P1, sha1 0f4896606b21...), the cipher block's lines 5-8 (R5-R8) and the second margin
note beside them ("He is in jelosye y^t your ho. ..." by eye at reduced size in HAR-41R). Key under test, unchanged: Bourdeau's
needham1587 three-grid pigpen (github.com/dbourdeau/cyphersolver targets/needham1587, commit 0445769; MIT code / CC BY 4.0 text):
J U L / C O F / N 7 D = a-i; dot below k-s; dot inside t u w x y z (no j; u = v).

Image: one DECODE browser login, `--fetch` of the two absolute filesrv URLs only (IMG_R8480_I39160_P1.jpg; IMG_R8479_I39159_P4.jpg
for the reader control), `--delay 1600 --max-files 2`: login + record page + 2 files, <= 8 requests. sha1 of P1 must equal HAR-41R's
0f4896606b21 or the job stops before any read. Scratchpad only.

Crops: the same rotation as tx/f41r_runs.tsv (native region from x=2650,y=6200, width 4030, rotate -2.25 deg PIL bicubic fill 230),
the region extended downward so lines 5-8 fit; R5-R8 cut tight to the box-sign row, interlinear gloss and margin out of view, halves
split at an ink gap with no overlap; boxes appended to tx/f41r_runs.tsv. The crop command is pasted in NOTES before the first reader
call. Never a full-page image to a reader. Second margin note cut separately (same tool as HAR-41R's margin).

Readers (all blind, Opus): one subagent call per run R5..R8, given only that run's crop(s), the nine shapes by Bourdeau's stroke
descriptions exactly as HAR-41R gave them, the three mark states, '|' at word gaps, '?' for unsure. Never told the key, any plaintext,
the margin, the gloss, HAR-41R's reads or Bourdeau's strings. Reader control (as HAR-41R): call 1 (R5) also gets the f.39v line G
words 1, 5, 8 crop (R8479 P4 boxes as in tx/f41r_runs.tsv), labelled in random order, not told it is a check. Gate >= 17/19 signs
equal in shape and mark to tx/f39v_lineG_har39v.tsv (the same 19-sign item and gate as HAR-41R). Control FAIL -> target score
reported, labelled a non-test of the key. Margin: one Opus call reads the second margin note from its crops only.

Normalisation, statistics, null and gate: identical to PREREG-HAR-41R.md (S1 semi-global, S2 exact-word share of decoded words >=3
letters, 1000 value-shuffled keys random.Random(41), p95 and fraction >= real), computed on R5-R8 against the second margin note,
with `gloss/har41r_score.py --block 2` (inputs tx/f41r_reads_b2.tsv, tx/f41r_ctrl_b2.tsv, tx/f41r_margin_b2.tsv; output
gloss/har58_score.tsv; `--check`). Gate fixed now:
- A: S1 > p95 AND S1 >= 0.60 AND S2 > p95, control PASS -> aligned signs matching the margin are C, the rest M.
- B: S1 > p95 and S2 > p95 but S1 < 0.60 -> key holds, grades stay M.
- C: S1 <= p95 or S2 <= p95 -> non-test or key does not hold here; control and '?' share decide which.
- A second margin read under 40 letters makes the test a non-test. If lines 5-8 do not sit beside the second note (as R4 sat under
  the interlinear gloss), the S1 free-end alignment covers the extent; any interlinear gloss is read only if seen and reported
  post hoc, never as the gate.
Units: 4 run calls + 1 margin + (control rides in call 1) + reconcile at ~1.3 each + floor 3 ~ 10.8 against cap 10; stop before a unit
that would cross USD 8 or 80 min. No key.tsv edit; a sign that conflicts with the margin is logged as a candidate, not a key change.

## Amendment 1 (15 Oct 2026, 18:0x UTC by date -u), after cropping, before any reader call or score

Found on cropping (worker's own look at a reduced overview for layout only; no sign read): the cipher lines after HAR-41R's R4 are
R5 "no lesse [cipher] other." under the interlinear gloss "sowght unto by the"; R6 "... and to [cipher] in that poin(t)" under
"Satisfye him"; R7 "... [cipher] with owt any other respect" under "to write this much"; R8 "in the world: [cipher] that [cipher]";
R9 "[cipher] This onelie to let y..". The second margin note ("He is in jelosye ...", 3 lines + an interlinear word) sits at native
y ~7800-8260, beside R8-R9, not R5-R7 -- the same shape as HAR-41R's R4. So, with the unit count unchanged (6 calls):
- Runs read: R5, R6, R7, R8 (2 parts), R9 (2 parts) -- one Opus call per run, control in call 1 (R5). R9 is one line past the brief's
  "lines 5-8"; it is read because the note sits beside it.
- Gate statistic (S1, S2, null, outcome A/B/C exactly as above) on D = R8 + R9 against the second margin note. The note crop is one
  1390x560 deskewed crop (region 1330,7760,1390,560, rotate -0.90 deg, the angle tools/iiif_lines.py --deskew-region fitted), under
  2500 px, the note only.
- The same margin call also reads the three interlinear glosses from their own crops (G5, G6, G7; cut above the cipher rows, cipher
  out of view). R5, R6, R7 are each scored post hoc against their gloss with the same S1 and null -- reported, not the gate.
- Boxes (rotated frame of native region 2650,6200,4400,2000, rotate -2.25 deg PIL bicubic fill 230, crops enlarged 1.15x): R5
  440-1580 x 805-912; R6 2370-3420 x 1040-1130; R7 1240-2520 x 1362-1460; R8 745-1990 / 2250-4060 x 1535-1640; R9 0-1600 / 1600-2560 x
  1705-1815; G5 380-1580 x 712-812; G6 2370-3420 x 965-1040; G7 1240-2520 x 1270-1362. (A taller/wider region than HAR-41R's shifts the
  rotation centre by a few px; boxes are stated in this frame.)
