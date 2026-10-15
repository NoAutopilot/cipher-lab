# LVN-3R pre-registration, unit 1: WVO 4610 p1 (15 Oct 2026, 02:5x UTC by date -u; written and pushed before the blind read is opened)

Job: LVN-3R (LANE DEFAULT-A4-0235-15, account 4). NOTES.md Remaining gaps item 3 / Escalation: the LVN16-3R per-token zoomed read
(lvn16/PREREG-LVN16-3R.md), run unchanged on 4610 p1, then p2, then 4611; stop after any unit whose control fails. 4610 p3 is not
touched (per-token crops [retired] there).

Material: WVO 04610.pdf fetched once 15 Oct 2026 (resources.huygens.knaw.nl, HTTP 200), p1 rendered at 300 dpi with pymupdf
(`page.get_pixmap(dpi=300)`, 2481x3508, sha1 d13c2517bde5...). Line boxes = the committed 150-dpi boxes in images/manifest.json x2.
Per-token crops by `lvn10p1/crops.py PAGE images/manifest.json lvn10p1/tok.tsv OUT` (tight crop 3x, context crop 2x with a blue
wedge; same shape as lvn16/crops3r.py). Centres in lvn10p1/tok.tsv placed by eye on ruled strips and checked on contact sheets of
the tight crops until every crop sat on its token (three rounds; all 24 on-token before this file). Crops stay in scratch, not git.

The one change forced by the material: LVN16-3R's settle rule compares the read to A3/B3, R12-LVN16's two 300-dpi blind passes.
4610 p1 has no 300-dpi passes; the equivalents on file are the two 150-dpi passes as reconciled in settle_log_4610.tsv (columns
A, B; for the two `agree-flagged` rows, A = B = the current sign). Written into lvn10p1/key.tsv as A150/B150.

Rows (lvn10p1/key.tsv, shuffled, seed 20261015): 14 targets = every M numeral row of 4610 p1 (there are no slash groups on p1);
10 controls = H numeral rows on the same lines (random.Random(20261015).sample), each with one look-alike fixed in key.tsv by a
one-digit swap (map 0>6 1>7 2>3 3>8 4>9 5>3 6>8 7>1 8>6 9>4, position seeded).

Reader: one blind Sonnet subagent call, all 24 rows, shown only the tight and context crop per row and an unlabelled shuffled
candidate list; may answer a value not listed, or '?'. Never shown the key, the role, the sign, or which pass gave which value.

Control gate: >= 8/10 controls read exactly as the H value. Below gate: nothing changes (non-test), logged only, and the job stops
(no unit 2).

Settle rule (gate passed only), per target:
- settle when the read equals A150 or B150 exactly (no '?'); the sign becomes that value; confidence H when it is a key_full code,
  else M kept with the new sign. A read matching neither stays M, logged.
- `agree-flagged` rows (A150 = B150 = sign; p1_L03/19 81, p1_L06/9 6): H only if the read equals the sign exactly.
- p1_L04/1 (A150 '-', B150 145, a segmentation gap): H only if the read is 145 exactly.
Recount: reading_4610_full_tokens.tsv C/H/M/U before and after; NOTES.md "Read so far" line recomputed; decode_key.py --check.
