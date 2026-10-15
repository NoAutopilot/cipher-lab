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

## Addendum LVN-P2RETX: re-transcription of the mixed 4611 p2 lines (15 Oct 2026, 08:0x UTC by date -u; pushed before any read)
Job LVN-P2RETX (LANE DEFAULT-A4-0645-15, account 4). A transcription repair, as LVN-L1 did for p3_L00: **no grade changes and no per-token
settle** (the p2b settle under the LVN-4611P2 addendum is untouched and not run here). Render: WVO 04611.pdf fetched once 07:5x UTC
(resources.huygens.knaw.nl, HTTP 200, 3,758,971 bytes), p2 at 300 dpi, sha1 36399838ce5c... (same render as LVN-4611P2).
Lines: the 35 deskewed physical lines from `tools/iiif_lines.py --image <p2 png> --region 250,140,2200,3000 --prefix p2 --deskew --centres
$(cat lvn4611/p2_centres.txt)` (the LVN-4611P2 command). **Targets: K13-K35** (23 lines; transcription p2_L13-p2_L33). Each line is cut into
two halves at the inter-token gap nearest the middle (`lvn4611/retx_p2.py crops`), images in scratch only, renamed by an opaque id.
**Controls: K04 and K12** (`random.Random(20261015).sample(range(1,13),2)`; transcription p2_L04 / p2_L12 = K04 / K12 token for token per
the p2a placement note; H numerals 20 and 19).
Readers: **2 blind Sonnet passes (A, B) x 2 batches** = 4 calls. Batch 1 = K13-K24 + control K04; batch 2 = K25-K35 + control K12. Each call
gets only the half-line images of its batch, in an order shuffled with its own seed (A1 20261015, B1 20261016, A2 20261017, B2 20261018), and
is asked for a **free read** of every token (numerals, and clear words as written, '?' for an unreadable digit). Never shown the transcription,
the key, any value, which image is a control, or NOTES.md.
Gate, per call: the control line's read aligned (difflib on the numeral sequence) to the transcription's numerals; >= 80% of that line's H
numerals read exactly (16/20 for K04, 16/19 for K12). A call below gate is a non-test: its reads are not used.
Reconcile: per target line, align A and B (both passing); where A = B the token stands; where A != B or '?', **1 reconcile** (the worker,
one Opus look at the half-line image; the worker has seen the 150-dpi transcription and the by-eye runs in NOTES.md -- declared here). If
one call of a batch fails, the passing call's read stands and every token of the batch is marked single-pass; if both fail, the batch is a
non-test and nothing is inserted for it.
Outputs: (1) `lvn4611/retx_p2_lines.tsv` the reconciled physical-line token sequence K13-K35 (K, pos, token, A, B, how). (2)
`lvn4611/retx_p2_map.tsv`: every existing row of p2_L13-p2_L33 mapped to (K, pos) by alignment, status `match` (same value), `differs`
(placed, other value), `duplicate` (a second copy of a token another row already maps to), `no-ink` (no token). Existing rows are not
edited, deleted or regraded. (3) `lvn4611/insert_p2retx.tsv`: every reconciled numeral or word token of K13-K35 that no existing row maps to
(an ink run in no row) becomes a new row, **grade M** (A = B or not; the agreement is recorded in alt/why for a later settle), line id
`p2_R<K>` + a letter per run, inserted by `../settle.py` immediately after the existing row mapped to the preceding ink token (by file
order). Then decode_key.py --check, settle.py --check, lvn4611/settle.py --check; C/H/M/U recounted before and after.
Prior work: `tools/prior_work.py ... --item-spec 'wvo=4611;folio=p2' --step-type transcribe --offline` run before the first read (result in
NOTES.md). Stop rule: batch 2 is not started if its two calls would take the job past 80% of the USD 6.5 cap or 90-minute box (my estimate:
start-up 1.0 + crops 0.5 + 0.7 per call + reconcile/map 1.0).

## Addendum LVN-P2B: p2b settle on the map, then the p2_L13-L33 ordering repair (15 Oct 2026, 08:4x UTC by date -u; pushed before any output is computed)
Job LVN-P2B (LANE DEFAULT-A4-0645-15, account 4). Disk only, no image read, no subagent: both steps are deterministic rewrites from the files
LVN-P2RETX committed (`retx_p2_lines.tsv`, `retx_p2_map.tsv`, `insert_p2retx.tsv`) and the frozen p2b key (`key_p2b.tsv`, built by
LVN-4611P2 before any read). The 11 H rows the reconciled ink contradicts (LVN-P2RETX list) are **not** ruled here: no H row changes value or
grade in either step (they go to a separate verifier). Prior work: `tools/prior_work.py ... --item-spec 'wvo=4611;folio=p2' --step-type
transcribe --offline` exit 4 at 08:41 UTC (own-work LEADs, Groen t. IV LEAD, two generic UNCHECKED; none bears on a transcription repair).

**Step 1, p2b settle on the map (unit `p2bm`; the per-token read unit `p2b` stays unrun).** "Read" for a target = the ink token its row maps to
in retx_p2_map.tsv. Targets = the 161 `target` rows of key_p2b.tsv. A target is **eligible** when all hold: (i) map status `match`; (ii) the
ink token's how in retx_p2_lines.tsv is `A=B` (the two blind passes agree, no reconcile); (iii) **anchored**: the row at position +1 or -1
of the same transcription line maps to the same K at kpos +1 or -1 respectively (an isolated single-value match does not count; this guards
against the map's own value-matching placing a row on its value by construction); (iv) the ink equals A150 or B150 exactly. An eligible
target settles under the unchanged settle rule: H when the value is a key_full.tsv code (action settled/confirmed), else M kept
(read-confirmed-not-key-code). Every other target stays M with its reason.
Controls (same 10 as LVN-4611P2's p2b gate, the key_p2b.tsv `control` rows, all H): (a) **positive**: a control passes when it is eligible
by (i)-(iii) and the ink equals its H sign; gate >= 8/10. (b) **power (wrong value)**: for each control separately, its sign in
ciphertext_4611_pre_retx.tsv is replaced by its seeded look-alike (the other candidate in key_p2b.tsv's candidates column), the map is
rebuilt with `retx_p2.build`, and the control must come out not eligible with its look-alike value; gate >= 9/10 rejected. Both gates must
pass, else unit p2bm is a non-test and nothing changes. Apply: `lvn4611/settle.py` writes settle_p2bm.tsv; `../settle.py` applies it as the
last per-token unit (settled/confirmed rows only).

**Step 2, ordering repair of p2_L13-L33 (after step 1, as the last 4611 stage of ../settle.py).** The rows of transcription lines
p2_L13-p2_L33 and the LVN-P2RETX inserts p2_R* are re-sequenced into the physical lines K13-K35: (1) every row the map places (match or
differs) and every insert (its K/n in why) takes key (K, kpos); (2) a row the map does not place (no-ink, or `duplicate` by the near-value
rule only) stays attached after the nearest preceding row of its own transcription line in file order (before the following one if it heads
its line), so it keeps its neighbours; (3) a **block duplicate** (a row in a block of >= 2 equal tokens lying wholly on ink another row
already carries -- retx_p2.build's own `dup` set) is retired: moved out of ciphertext_4611.tsv into `lvn4611/retired_p2.tsv` with its full
row, unless it is graded H or C, in which case it is kept (attached as in (2)) and listed. Rows are rewritten with line = `p2_K<KK>` and
position = 1..n in K order; sign, confidence and alt unchanged; why gains "LVN-P2B order: was <line>/<position>". p2_L01-L12 and p1/p3 rows
untouched. Then decode_key.py --check for all decode*.json, settle.py --check, lvn4611/settle.py --check, retx_p2.py check; C/H/M/I/U
recounted before and after. No value is changed by step 2; its only effects are order, line ids, and the retired duplicates.
Stop rule: none priced beyond the worker's own time (estimate ~3 of the USD 5.5 cap); if either step's checks fail and cannot be fixed by
the 80% line (09:30 UTC), revert that step and log it.
