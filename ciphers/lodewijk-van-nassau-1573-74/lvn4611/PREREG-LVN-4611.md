# LVN-4611 pre-registration: WVO 4611 p1 and p3 (addendum to lvn10p1/PREREG-LVN-3R.md and lvn10p2/PREREG-LVN-P2.md; 15 Oct 2026, 04:5x UTC by date -u; pushed before any read is opened)

Job: LVN-4611 (LANE DEFAULT-A4-0437-15, account 4). Same protocol, same control, same gate, same settle rule as lvn10p1/PREREG-LVN-3R.md
(4610 p1, control 9/10 PASS) and lvn10p2/PREREG-LVN-P2.md (4610 p2, control 8/10 PASS), run on WVO 4611. 4610 and 4611 p2 not touched.

Units (rule 3 per-unit merge): **unit p1** (72 targets) and **unit p3** (16 targets), each with its own 10 controls and its own gate.
A unit's settles are applied only when that unit's own control passes. p1 first; p3 only if p1 finishes under 60% of cap and box.
4611 p2 (252 M numeral rows) is out of scope for this job (next step).

Material: WVO 04611.pdf fetched once 15 Oct 2026 04:4x UTC (resources.huygens.knaw.nl, HTTP 200, 3,758,971 bytes), rendered
`pdftoppm -png -r 300` (p1 2481x3508 sha1 64b18534d196..., p3 sha1 add43302eb94...). Line boxes = the committed 150-dpi boxes for
04611_pN_Lnn.jpg in images/manifest.json x2. Per-token crops by lvn4611/crops.py (lvn10p2/crops.py with the letter and page as
arguments). Centres in lvn4611/tok_<page>.tsv placed by eye on ruled strips and checked on contact sheets until every crop sits on its
token, before the read is opened. Crops stay in scratch, never in git.

A150/B150 = the two 150-dpi passes as reconciled in settle_log_4611.tsv (A, B; '-' = gap). Forced change: 4611 rows marked
`agree-flagged` (both passes agreed, so absent from settle_log) take A150 = B150 = sign (as unit 1's p1_L06/9 and p1_L03/19).

Rows: lvn4611/key_p1.tsv and key_p3.tsv, built deterministically by lvn4611/build_key.py (seed 20261015) from
lvn4611/ciphertext_4611_pre.tsv (= ciphertext_4611.tsv before this job): targets = every M numeral row of the page; 10 controls = H
numeral rows on the same lines, each with one look-alike by the seeded one-digit swap of unit 1.

Reader: blind Sonnet subagent calls, about 20-26 rows each (p1: four calls; p3: one call), each shown only the tight and context crop
per row and the unlabelled shuffled candidate list; may answer a value not listed, or '?'. Never shown the key, the role, the sign, or
which pass gave which value. Controls are spread across the calls.

Control gate per unit: >= 8/10 controls read exactly as the H value (pooled over that unit's calls). Below gate: nothing changes for
that unit (non-test).

Settle rule (gate passed only), per target, unchanged: settle when the read equals A150 or B150 exactly (no '?'); the sign becomes that
value; H when it is a key_full.tsv code, else M kept with the new sign. A read matching neither stays M, logged. A gap row settles only
when the read equals the other pass's value exactly. Rows that cannot be placed on a single token (segmentation questions) are not read
and stay M, listed in a placement note pushed before the read.
Apply: settle.py (4611 lineage) gains a last stage applying lvn4611/settle.tsv (settled/confirmed rows only) after its own settles;
reading_4611 regenerated; decode_key.py --check; C/H/M/U recounted before and after.

Prior work: `tools/prior_work.py lodewijk-van-nassau-1573-74 --item-spec 'wvo=4611;folio=p1' --step-type transcribe --offline` exit 4
at 04:4x UTC, before any priced read: owed rows are three own-work LEADs (the named next step, the audited reading, this job's claim)
and the plaintext-level holds AUDIT.md section 1 covers (Groen t. IV, Tomokiyo, solver caches); none bears on a transcription re-read.

Also in this job, (a): eye check of 4610 p2_L28/11 (LVN-P2's control miss, H 81 read 61), one Opus look beside the H exemplars
p2_L02/4 (81) and p2_L11/8 (61); reported, key and ciphertext not edited.

## Placement note, unit p1 (before the read is opened)
Centres: `lvn4611/blobs.py <p1 png> images/manifest.json lvn4611/key_p1.tsv 04611 <out>` numbers the ink runs on each target line
(column profile, merge gap 9 px); `lvn4611/blobmap_p1.txt` names the run (or runs, or the left/right end of a run) per row, chosen by
counting tokens on numbered strips; `lvn4611/mk_tok.py <out>_seg.json lvn4611/blobmap_p1.txt` gives the centres; four rows then
moved by hand (p1_L11/14 -35, p1_L24/11 -10, p1_L01/17 +8; p1_L02/6 and p1_L28/5 re-mapped one run) -> `lvn4611/tok_p1.tsv`.
Two contact-sheet rounds; all 78 tight crops sit on their token before the read.
4 of the 72 targets are NOT placed and NOT read (stay M, segmentation findings, not reading questions):
- p1_L05/1 (7, A-only): no numeral precedes "111" on the physical line; only a faint dot at the margin.
- p1_L29/16-18 (11 51 21, B-only, after the B-only clear words voyant que at /14-15): the image of L29 ends "... 129. 74, 10, 39, 75,
  100, 85, 60, 150, 61, 40." with no clear words; "Voyans que 11, 51, 21" is on the physical line L30 (p1_L30/8-12, A). Pass B carried
  L30's words and three numerals into L29; a duplicate, not a reading question. L29/19-28 (A = this line's ink) and L30/10-22 (A-only,
  B gap) are placed and read.
So unit p1 reads 68 targets + 10 controls = 78 rows, in four blind Sonnet calls (20/20/19/19 rows; controls 3/3/2/2).

## Placement note, unit p3 (LVN-PIN, 15 Oct 2026 05:2x UTC by date -u; pushed before the read is opened)
Job LVN-PIN (LANE DEFAULT-A4-0437-15, account 4) runs unit p3 under this PREREG unchanged (rows lvn4611/key_p3.tsv, gate >= 8/10, same
settle rule, one blind Sonnet call). 300-dpi render of WVO 04611.pdf p3 sha1 add43302eb94... (same as above; PDF fetched once 05:1x UTC).
**Line-box correction (placement only).** On p3 the committed 150-dpi boxes run one line above the transcription's numbering: box
04611_p3_L01 holds the page's first written line, "diy 78, 81, 28, 200, 9, 1?6, 120, 82, 29, 138. 127. 12, 81, 21, 77, 84, 111, 64, 124."
(read by eye at 300 dpi, not graded), which is in no 4611 transcription (ciphertext_4611_pre.tsv p3 starts "quil pourrons 75 6 5 ...",
the ink of box p3_L02; p2 ends "Je croy que vous trouvez"). Transcription line p3_Lk = box p3_L(k+1), checked line by line on ruled
300-dpi strips for L01-L09. `lvn4611/shift_boxes.py` writes the shifted box map (scratch) used by blobs.py and crops.py for this unit.
Centres: `lvn4611/blobmap_p3.txt` -> `mk_tok.py` -> two rows moved by hand (p3_L04/7 to x 1295 hw 45, the "15" after "particulierement"
rather than the following 25; p3_L04/14 to x 1920 hw 55) -> `lvn4611/tok_p3.tsv`; one contact-sheet round plus one check of the two
moved crops; every tight crop sits on its token.
Not placed (stays M, not read): **P323 p3_L08/8 (60)**: the image has one token "voz/boz" between "a" (p3_L08/7) and "bonnes" (/10),
where the transcription has two rows (/8 60 and /9 =bon); a segmentation question, not a reading one.
So unit p3 reads 15 targets + 10 controls = 25 rows in one blind Sonnet call.
The missing first line is a transcription gap (about 19 cipher numerals), logged in NOTES.md; not added to any ciphertext by this job.

## Addendum LVN-L1: p3 line boxes re-anchored, and the missing p3 first line (15 Oct 2026, 05:4x UTC by date -u; pushed before any read)
Job LVN-L1 (LANE DEFAULT-A4-0437-15, account 4). Render: WVO 04611.pdf fetched once 05:3x UTC (resources.huygens.knaw.nl, HTTP 200,
3,758,971 bytes), p3 at 300 dpi, sha1 add43302eb94... (same as LVN-4611 / LVN-PIN).

**(a) Line boxes.** `lvn4611/boxes_p3.py` re-anchors the p3 boxes on line centres from `tools/iiif_lines.py --image` (command in its
docstring) and writes `lvn4611/boxes_p3.tsv` in transcription numbering: new row **p3_L00** = physical line 1, p3_L01..L09 = physical
lines 2..10, p3_L10..L15 keep their committed boxes (shift_boxes.py had moved L10-L12 too; no read row sits there). `--recheck
lvn4611/tok_p3.tsv`: all 25 LVN-PIN rows sit on the same physical line (bands move 0-4 px; p3_L09/2 band trimmed from an over-tall box),
**0 moved**, so no LVN-PIN row is re-graded; the 25 crops were re-cut under the new boxes and eyed on one contact sheet, each on its token.

**(b) The missing first line, unit p3L00.** Tokens: `lvn4611/blobmap_p3L00.txt` -> `mk_tok.py` -> `lvn4611/tok_p3L00.tsv`: position 1 is the
clear word (entered `=diy` M by eye, not read), positions 2-20 are the 19 numerals (targets T01-T19 = positions 2-20). Crops by crops.py
under the boxes_p3.py JSON, scratch only; contact sheet eyed before the reads.
Rows: the 19 targets + the 10 unit-p3 controls of key_p3.tsv (P302 P303 P306 P307 P309 P312 P318 P321 P322 P325, H values there), 29 rows
per call, written to `lvn4611/key_p3L00.tsv` before the reads.
Readers: **2 blind Sonnet calls** (A, B), each reads all 29 rows independently, shuffled with its own seed (A 20261015, B 20261016), crops
renamed by row id, tight + context crop per row. **Free read** (no candidate list: the new line has no prior pass); may answer '?'. Never
shown the key, the role, any value or the by-eye line in NOTES.md.
Gate, per call: >= 8/10 controls read exactly as H. Both calls must pass for any target to be graded H; one or both FAIL = non-test, the
line is still entered (the brief asks for it) with every numeral M from the reconcile below, and logged as a non-test.
Settle (both gates passed): A == B, no '?': the sign is that value, **H** when it is a key_full.tsv code, else M. A != B, or a '?':
**1 reconcile** (the worker, one Opus look at the tight + context crops of those rows only, having seen the by-eye line in NOTES.md --
declared here): chooses A, B, or another value, graded **M** (never H). Script `lvn4611/settle_p3L00.py` writes
`lvn4611/insert_p3L00.tsv` (line, position, sign, confidence, alt, why); `../settle.py` inserts those rows ahead of the first p3_L01 row of
ciphertext_4611.tsv, existing rows not renumbered. Then decode_key.py --check, settle.py --check, lvn4611/settle.py --check; C/H/M
recounted before and after. 4610 p2_L28/11 not touched.

## Addendum LVN-4611P2: 4611 p2 per page-half (15 Oct 2026, 07:2x UTC by date -u; pushed before any read is opened)
Job LVN-4611P2 (LANE DEFAULT-A4-0645-15, account 4). Same protocol, control, gate and settle rule as the p1/p3 units above, on WVO 4611 p2,
in two units (rule 3 per-unit merge): **unit p2a** = the M numeral rows of transcription lines p2_L01-p2_L18 (92 targets), **unit p2b** =
p2_L19-p2_L33 (161 targets). Each unit has its own 10 controls and its own gate; a unit's settles are applied only if its own control passes.
p2a first; p2b only if p2a is finished before 08:25 UTC and the job's own estimate of spend (about 1.0 start-up + 0.6 per Sonnet call + my
placement rounds at about 1.0 each) is at or under 4.5, so p2b (about 4 to 5) cannot cross 80% of the USD 9 cap or the 100-minute box.

Material: WVO 04611.pdf fetched once 07:2x UTC (resources.huygens.knaw.nl, HTTP 200, 3,758,971 bytes, take/release in ROOM.md), p2 rendered
`pdftoppm -png -r 300 -f 2 -l 2` (2481x3508, sha1 36399838ce5c...). **Line crops (change from p1/p3, placement only):** the committed 150-dpi
boxes are straight, but the p2 text slopes (fit 0.03-0.057 per px from the 13th physical line down, a drift of 70-125 px over the 2200 px
text width against an 84 px pitch), so a straight box crosses two physical lines on the right half; this is why the transcription lines
p2_L13-L33 mix the head of one physical line with the tail of its neighbour. The crops for this job are therefore the 35 deskewed physical
lines K01-K35 cut by `tools/iiif_lines.py --image <p2 png> --region 250,140,2200,3000 --prefix p2 --deskew --centres $(cat
lvn4611/p2_centres.txt)` (the centres are the tool's own 33 peaks plus two lines it merged, at 1012 and 2181, region y). Ink runs are numbered
by `lvn4611/p2_blobs.py`; `lvn4611/blobmap_p2.txt` names each target and control row's physical line and run (chosen by counting tokens on
the numbered strips and matching the transcription's own neighbours); `lvn4611/p2_crops.py` cuts the tight crop (the run, 3x) and the
context crop (run +/- 130 px, 2x, blue wedge) from the deskewed line crop. Crops stay in scratch, never in git.

Rows: `lvn4611/build_key_p2.py` (seed 20261015) from `lvn4611/ciphertext_4611_pre_p2.tsv` (= ciphertext_4611.tsv p2 before this job; it
differs from ciphertext_4611_pre.tsv only at p2_L15/20, 82, now M after LVN-PIN's corpus regeneration, so it is a target here): targets =
every M numeral row of the unit's lines; A150/B150 from settle_log_4611.tsv ('agree-flagged' rows take A150 = B150 = sign); 10 controls =
H numeral rows on the unit's lines, `random.Random(20261015).sample`, one look-alike by the seeded one-digit swap; rows shuffled.
Readers: blind Sonnet subagent calls of about 25 rows (p2a: 4 calls; p2b: 6 or 7 calls), each shown only the tight and context crop per row
(renamed by row id) and the unlabelled shuffled candidate list; may answer a value not listed, or '?'. Never shown the key, the role, the
sign, or which pass gave which value. Controls spread over the calls.
Gate per unit: >= 8/10 controls read exactly as the H value (pooled). Below gate: nothing changes for that unit (non-test).
Settle rule unchanged (read equals A150 or B150 exactly, no '?'; H when a key_full.tsv code, else M with the new sign; a read matching
neither stays M). Rows that cannot be placed on a single token (a transcription token with no ink token, two transcription tokens on one
ink token, a pass duplicate across two lines) are not read, stay M, and are listed in a placement note pushed before the read.
Apply: `lvn4611/settle.py` and `../settle.py` gain units p2a, p2b (settled/confirmed rows only, same last stage as p1/p3); reading_4611
regenerated; decode_key.py --check; C/H/M/U recounted before and after. No by-eye re-transcription of the mixed lines enters any file in this
job (a finding for a later job, logged in NOTES.md).
Prior work: `tools/prior_work.py lodewijk-van-nassau-1573-74 --item-spec 'wvo=4611;folio=p2' --step-type transcribe --offline` exit 4 at
07:23 UTC, before any priced read: owed rows are four own-work LEADs (the named next step, the audited reading, LVN-EYE's and this job's
claims), the Groen t. IV edition LEAD and two generic UNCHECKED solver/Tomokiyo rows, which AUDIT.md section 1 covers at plaintext level;
none bears on a transcription re-read.

## Placement note, unit p2a (LVN-4611P2, 15 Oct 2026 07:3x UTC by date -u; pushed before the read is opened)
`lvn4611/blobmap_p2a.txt` (line, position, physical line K, ink runs) -> `lvn4611/p2_crops.py` (tight crop = the runs extended to 6 px short
of the neighbouring runs, at most 45 px, because a thin '1' often falls under the run filter). Three contact-sheet rounds; after two re-maps
(p2_L15/6 -> K15 runs 13+14, p2_L15/7 -> run 15, p2_L13/13 -> runs 16+17) every one of the 90 tight crops sits on its token.
Transcription line -> physical line: p2_L01-L12 = K01-K12 token for token. p2_L13-L18 each join the head of one physical line to the tail of
the line above or below (the straight 150-dpi boxes cross lines on the sloped right half): L13 = K13 head (/1-13) + K14 head (/14-18);
L14 = K14 (/3-19) + K15's first words; L15 = K16 head (/1-5) + K15 tail (/6-7, /12-20); L16 = K17 head (/1-7) + K16 tail (/9-16);
L17 = K18 head (/1-6) + K16 /8 + K17 tail (/11-18); L18 = K19 head + K18 tail.
**12 of the 92 targets are NOT placed and NOT read (stay M):**
- p2_L14/1-2 (9, 42, A only): a second copy of K14's first two numerals "19, 40", which p2_L13/17-18 already carry in order after
  "Il y auroit"; a pass duplicate across two lines.
- p2_L15/8-11 (114 18 39 85, A only): a second copy of K14 "114, 18, 39, 85" (p2_L14/4-7) between K15's "26, 82" and "115"; duplicate.
- p2_L17/9-10 (14 64, B only): a second copy of K16 "14, 64" (p2_L16/9-10); duplicate.
- p2_L17/7 (65, B only): B's run here is K16's tail, so the row could be K16 "61" or K18 "65"; two candidate tokens, not placed.
- p2_L13/19 (73, A; B 125): no ink token 73 between K14 "40" and "82"; K13's tail "77, 37" is the nearest look-alike, on another line.
- p2_L15/17 (74, B only): no 74 on K15 between "4" and "35"; K16 has "4, 74" (unread by any row here); not placed.
- p2_L16/8 (71, A only): between K17 "26" and K16 "14" no single token; not placed.
Ink with no transcription row (finding, logged in NOTES.md, nothing inserted): K13 tail "77, 37, 5, 85, 312."; K15 head "71, 9, 39, 25, 105,
24, 124. 147." and K15 "38" (after "26, 82"); K16 "4, 74, 150, 90, 81, 21, 61." after "advis" (in no transcription line); K17 "30, 84" before
"104"; K17 "Et s un" words sit at p2_L17/19-21. Physical lines on p2: 35 (K01-K35); the transcription has 33.
So unit p2a reads 80 targets + 10 controls = 90 rows in four blind Sonnet calls (23/23/22/22 rows; controls 3/3/2/2).
