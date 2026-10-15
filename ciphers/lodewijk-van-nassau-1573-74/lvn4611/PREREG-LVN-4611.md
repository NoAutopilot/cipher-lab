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
