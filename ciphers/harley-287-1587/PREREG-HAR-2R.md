# PREREG-HAR-2R (15 Oct 2026, 18:1x UTC by date -u), pushed before any image fetch, read or score

Job: `.claude/briefs/runs/2026-10-15-acct4-default-1735-jobs.md` "HAR-2R". A second blind reader on BL Harley MS 287 f.41r (DECODE R8480 P1)
cipher runs R1-R9, the step HAR-41R and HAR-58 left undone. Key under test, unchanged: Bourdeau's needham1587 three-grid pigpen
(github.com/dbourdeau/cyphersolver targets/needham1587, commit 0445769; MIT code / CC BY 4.0 text): J U L / C O F / N 7 D = a-i; dot
below k-s; dot inside t u w x y z (no j; u = v).

Image: one DECODE browser login, `--fetch` of the two absolute filesrv URLs only (IMG_R8480_I39160_P1.jpg; IMG_R8479_I39159_P4.jpg for
the reader control), `--delay 1600 --max-files 2`: login + record page + 2 files, <= 6 requests. sha1 of P1 must start 0f4896606b21 (and
P4 7076557b0b0e) or the job stops before any read. Scratchpad only.

Crops: recut from tx/f41r_runs.tsv's boxes in their two stated frames (R1-R4: native region 2650,6200,4030,800; R5-R9: 2650,6200,4400,2000;
both rotated -2.25 deg PIL bicubic fill 230, enlarged 1.15x); the script and command are pasted in NOTES before the first reader call; one
crop per run part, never a full page. Control crop: R8479 P4 boxes (3030,3150,3570,3340), (4730,3110,5110,3300), (5700,3020,6290,3210).

Readers (all blind, Opus): one subagent call per run R1..R9 (9 calls), given only that run's crop(s), the nine shapes by Bourdeau's stroke
descriptions (J right+bottom; U left+bottom+right; L left+bottom; C top+left+bottom; O closed box; F top+left; N left+top+right; 7 top+right;
D top+right+bottom), the three mark states (none, '.' dot below, ':' dot inside), '|' at word gaps, '?' for unsure, {clear} for cursive,
{blot}. Never told the key, any plaintext, the margin, the glosses, Bourdeau's strings, or reader 1's (HAR-41R/HAR-58) strings or notes.
Reader control: call 1 (R1) also gets the f.39v line G words 1, 5, 8 crop, the two images labelled A/B in random order (random.Random(2)),
not told which is a check. Gate >= 17/19 signs equal in shape and mark to tx/f39v_lineG_har39v.tsv (same item and gate as HAR-41R/HAR-58).
Output: tx/f41r_reads_r2.tsv, tx/f41r_ctrl_r2.tsv.

Statistic in place of S2. HAR-58 found S2 (exact-word share of decoded words) cannot vary when the reader marks no gaps (rule 3 non-test).
S3, gap-free: of the clear partner's normalised words of >= 3 letters, the share found as a substring of the normalised gap-free decode
(PREREG-HAR-41R normalisation). Null: the same 1000 value-shuffled keys (random.Random(41)). On paper, before any read, on reader 1's reads
already on file (`python3 gloss/har41r_score.py --second --demo-s3`):

  unit  clear partner          S1 real / p95   S3 real / p95 (frac>=)
  U1    R1-R3 vs margin note 1  0.468 / 0.257   0.258 / 0.032 (0.000)
  U5    R5 vs gloss G5          0.500 / 0.286   0.000 / 0.000 (1.000)
  U6    R6 vs gloss G6          0.750 / 0.333   0.500 / 0.000 (0.001)
  U7    R7 vs gloss G7          0.857 / 0.286   0.667 / 0.000 (0.000)
  U89   R8+R9 vs margin note 2  0.656 / 0.266   0.364 / 0.000 (0.000)

So S3 and its value-shuffled null can and do differ (a shuffle changes the decoded letters, which is what S3 counts); U5 shows it can also
tie at 0 for a short gloss, which then fails the gate rather than passing it.

Units and gate (per unit, on reader 2's reads, `gloss/har41r_score.py --second`, output gloss/har2r_score.tsv, `--check`): U1, U5, U6, U7,
U89 as above. R4 has no blind-read clear partner (its gloss was seen by eye only), so R4 gets reader agreement only and stays M.
A unit PASSES iff reader 2's control PASSES, S1 > p95, S3 > p95 and S1 >= 0.60 (the 0.60 bar of PREREG-HAR-41R's outcome A).

Grade rule (M -> C). Reader 1's and reader 2's tokens are Levenshtein-aligned per run part (word gaps dropped). A pair is agreed iff both
tokens are equal in shape and mark and neither carries '?'. The unit's consensus decode (agreed letters; '?' elsewhere) is aligned
semi-globally to the unit's clear text (letters j->i, v->u, y->i, doubles kept). A sign is C iff its unit PASSES, the pair is agreed, its
letter equals its aligned clear letter, and at least one neighbour in the consensus string is also such a match. Everything else stays M.
Disagreements are written to tx/f41r_disagree_r1r2.tsv and not settled by a third machine pass. No key.tsv edit.

Units priced: 9 run calls + (control rides in call 1) + 1 reconcile (script, my own read of the disagreement list) ~ 11 x ~1.0 + floor 3
~ 14; stop before a unit that would cross USD 11 or 96 min of the 120-min box. de-crypt.org one login, <= 6 requests, 1.6 s apart.
