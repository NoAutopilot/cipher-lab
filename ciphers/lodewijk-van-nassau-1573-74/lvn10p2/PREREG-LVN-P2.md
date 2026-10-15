# LVN-P2 pre-registration, unit 2: WVO 4610 p2 (addendum to lvn10p1/PREREG-LVN-3R.md; 15 Oct 2026, 03:2x UTC by date -u; pushed before any read is opened)

Job: LVN-P2 (LANE DEFAULT-A4-0235-15, account 4). Same protocol, same control, same gate, same settle rule as
lvn10p1/PREREG-LVN-3R.md (unit 1, 4610 p1, control 9/10 PASS), run on 4610 p2 only. 4611 and 4610 p3 are not touched.

Material: WVO 04610.pdf re-fetched once 15 Oct 2026 03:2x UTC (resources.huygens.knaw.nl, HTTP 200, 3,689,372 bytes), p2 rendered
`pdftoppm -png -r 300 -f 2 -l 2` (2481x3508, sha1 c997f0cb8a35e20d01e4c6b2a4c9363fd9e2b86f). Line boxes = the committed 150-dpi
boxes for 04610_p2_Lnn.jpg in images/manifest.json x2. Per-token crops by lvn10p2/crops.py (lvn10p1/crops.py with the page's own
per-line y offsets, if any are needed, recorded in the script). Centres in lvn10p2/tok.tsv are placed by eye on ruled strips and
checked on contact sheets of the tight crops until every crop sits on its token, before the read is opened. Crops stay in scratch.

Same forced change as unit 1: A150/B150 = the two 150-dpi passes as reconciled in settle_log_4610.tsv (columns A, B; '-' = that pass
had a segmentation gap there).

Rows: lvn10p2/key.tsv, built deterministically by lvn10p2/build_key.py (seed 20261015): 44 targets = every M numeral row of
ciphertext_4610.tsv on p2 (no slash groups on p2); 10 controls = H numeral rows on the same lines, each with one look-alike by a
seeded one-digit swap (0>6 1>7 2>3 3>8 4>9 5>3 6>8 7>1 8>6 9>4). 18 of the 44 targets are segmentation-gap rows with one value only.

Reader: one blind Sonnet subagent call per half of the rows (27 + 27, the unit-1 single call split in two because 54 rows x two
crops is twice unit 1's size; each call carries 5 controls), shown only the tight and context crop per row and the unlabelled
shuffled candidate list; may answer a value not listed, or '?'. Never shown the key, the role, the sign, or which pass gave which value.

Control gate: >= 8/10 controls read exactly as the H value (pooled over the two calls). Below gate: nothing changes (non-test).

Settle rule (gate passed only), per target, unchanged from unit 1:
- settle when the read equals A150 or B150 exactly (no '?'); the sign becomes that value; confidence H when it is a key_full.tsv code,
  else M kept with the new sign (read-confirmed-not-key-code). A read matching neither stays M, logged.
- a gap row (one pass '-') therefore settles only when the read equals the other pass's value exactly (unit 1's p1_L04/1 rule).
Apply: lvn10/apply.py gains lvn10p2/settle.tsv after lvn10p1/settle.tsv (settled/confirmed rows only); reading_4610 regenerated;
decode_key.py --check; recount C/H/M/U before and after.

## Placement note (before the read is opened)
Centres placed in four rounds of ruled strips and tight/context contact sheets; all 42 placed crops on their token before the read.
12 of the 44 targets are NOT placed and NOT read (they stay M, logged as segmentation findings, not reading questions):
- p2_L02/1 (192, B-only): the image has six tokens (102, 32, 62, 112, 102, 81) where the transcription has four (192 112 182 81);
  positions 2-4 are right-anchored on 112, 102, 81; position 1 has no unambiguous ink.
- p2_L25/6, p2_L25/7 (65, 105, B-only) and p2_L26/1-3 (85, 148, 120, B-only): pass B appears to have read the one ink run
  "55, 145, 120" (physical line at y ~2400, after 82, 2, 5, 83, 119) twice, once into each line; ownership is a segmentation question.
- p2_L26/20-25 (70 10 25 77 85 24, A-only): the same six values are p2_L27/1-6 (H); A appears to have carried the start of the next
  physical line into L26; a duplicate, not a reading question.
So the read is 32 targets + 10 controls = 42 rows (control gate unchanged: >= 8/10).
