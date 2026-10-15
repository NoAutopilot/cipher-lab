# PREREG-VIV67C (15 Oct 2026, 02:3x UTC by date -u; VIV-67C worker, session_01NYDLhChR2KM7dLMazhLN3t, run on account 2 for LANE VIV-KEYSTONE, account 4)

Brief: .claude/briefs/runs/2026-10-15-acct4-for-acct2-jobs.md "JOB VIV-67C" (= VIV-67B's method on f.202r, the remainder of ink 67, against the
continuation of ink 68). Written and pushed BEFORE any blind pass, decode or alignment. Looked at so far: the 600 px overviews of c207 and c212, the
two native regions at 1/6 scale, the iiif_lines debug overlay of f.202r and one crop (to check the cut), and the f.207r strip overview (to check the
cuts fall between lines). Nothing here edits key.tsv, reading_piece63.tsv, status.json or any committed reading.

**Leaves (by eye, offset canvas = folio + 5):** c207 right = f.202r, 32 cipher lines (iiif_lines found 32 bands, overlay checked), marginal notes in
the left margin (outside the cut region, not read). c212 right = f.207r, 19 lines of clerk French opening "que l'on estoit bien ayse de la bonne
affection ... a Don Jehan d'Austria"; **its last line ends "... bien jeune qu-", so ink 68 continues onto f.207v** (VIV-67B's "where ink 68 ends" was
not checked by eye). f.207v is outside this brief's target and is not fetched here.

**Decipherment re-use (disk first).** f.206v already has two blind passes on disk (tx/dec_f206v_passA.txt, passB.txt, VIV-67B) and is inside
tx/dec67b_norm.txt; it is not re-read. Only f.207r gets two new blind passes (A top-down, B bottom-up order of strips). Reader calls: 4 Sonnet
(f.202r A/B, f.207r A/B), under the brief's price of 6.

**Target string.** T67b = dec67[-401:] + dec67b (2,317 letters, VIV-67B's target untrimmed). f.201v's alignment window was [0, 1780] = aligned span
+-200 (tx/vivk67b_result.json), so f.201v ends at T67b[1580]. T = T67b[1580:] (737 letters, the f.206v tail f.201v did not reach) followed by the
letters of tx/dec67c_norm.txt (f.207r, merged by tx/viv67_merge_dec.py f207r --out dec67c_norm.txt). Trim rule PREREG-VIV70B's: the first
int(n x 1403/1270) + 200 letters of T, n = collapsed codes of the f.202r stream; if that exceeds len(T), T is used whole (expected here: 32 lines
~1,650 codes need ~2,000 letters, T is ~1,600, so the cipher's last ~15-20% should run past f.207r into f.207v and stay unaligned; the gate's window is
the aligned span +-200, so this does not inflate the share).

**Reconcile.** tx/viv67_prep.py f202r; tools/reconcile_passes.py tx/f202r_passA_c.tsv tx/f202r_passB_c.tsv --out-dir tx/rec_f202r; tx/reconcile_vivk.py
f202r (six label rules unchanged) -> tx/f202r_rec.tsv. err_2reader reported beside, not gating.

**Gate (code unchanged: build_vivonne_f211r.control(); new driver benchmark-tx/build_vivonne_f202r.py imports it).** f.202r stream (c2.raw_tokens of
tx/f202r_rec.tsv, [PLAIN]/[...] dropped, o o collapsed) decoded with the published key (key_tomokiyo.tsv), aligned by confirm2's align() to the trimmed
T; window = aligned span +-200; match share for the real key and 200 value-shuffled keys (random.Random(20261014)). **PASS iff the real key ranks 1 of
201 AND real > shuffled p95 (sorted[189]).** Run ONCE (a crash before any score is computed may be fixed and run once more, reported). key.tsv full
set (50 draws) reported beside, not gating. A/B word agreement on f.207r reported beside.

**If PASS:** benchmark-tx/vivonne1573-f202r-dev.truth.tsv (split=dev) by build_vivonne_f201v.truth()'s recipe (line ids f202r_, clerk-split mask
from the two blind passes of each decipherment page: T67b's mask from build_vivonne_f201v.target() sliced [1580:], f.207r's from its own passes),
control numbers and "PREREG-VIV67C" in the header, a BENCHMARK-TX.tsv row; tools/tx_bench.py on passA, passB (independent) and committed (circular),
as measured and flagged-excluded. Label table: tx/viv67_labels.py --f202r -> tx/viv67c_labels*.tsv, counts only, no key edit.
**If FAIL:** stop; report the numbers; no truth file, no label table. No re-run under another start offset, target or trim.
Stop rule: a unit (a pass, the gate) that would cross 80% of cap 10 (8.0) or box (02:11-04:10, 80% = 03:47) is not started; cost is not visible to this
session, so the unit estimate (Opus floor 2.5 + 1.4 per Sonnet call) decides.
