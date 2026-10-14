# PREREG-VIV67B (14 Oct 2026, 03:2x UTC by date -u; VIV-67B worker, session_01TpzB2U75qJhGLAj2Pg61Pw, for LANE VIV-KEYSTONE, account 4)

Brief: .claude/briefs/runs/2026-10-13-acct4-keystone-viv-jobs.md "Account-2 row VIV-67B" (= VIV-67's method on the rest of ink 67, under
PREREG-VIV70B's trim rule). Written and pushed BEFORE any native fetch, any blind pass, any decode and any alignment; only the three
600 px overviews (c207, c211, c212) have been looked at. Nothing here edits key.tsv, reading_piece63.tsv, status.json or any committed
reading.

**Leaves (by eye on the 600 px overviews, openapi.bnf.fr, offset canvas = folio + 5):** c207 left = f.201v, a full page of cipher (about 32
lines, no plain head); c207 right = f.202r, about 30 cipher lines with marginal notes; c211 right = f.206r and c212 left = f.206v, plain
clerk French continuing ink 68 (c212 right = f.207r, where ink 68 ends).

**Scope decision (made here, before any pass).** Cipher page = **f.201v only**. Reason, from ink 67's own ratio (1,403 aligned letters /
1,270 codes, tx/vivk67_result.json) and the overviews: f.201r gave 1,270 codes from 24 cipher lines (~53 per line), so f.201v's ~32 lines
are ~1,700 codes -> a trimmed target of ~2,070 letters, while the brief's whole target (the last 401 letters of dec67 + ff.206r-206v,
~900 letters a page) is ~2,200 letters. f.201v alone is expected to consume nearly all of it, so f.202r's text lies mostly on f.207r,
outside this brief's target; and 4 cipher + 4 decipherment calls plus two reconciliation units would cross 80% of the cap (Usage 6/7).
f.202r is not fetched or read in this job (one-line next step in NOTES.md).

**Units, in order, each started only if it does not cross 80% of cap 12 (9.6) or box (03:11-05:41 UTC, 80% = 05:11) by the README estimate
(Opus floor 2.5 + 1.4 per Sonnet call + 1.4 per reconciliation unit):** U1 native fetches (c207 left, c211 right, c212 left; 3 requests) and
crops (tools/iiif_lines.py, --debug overlay checked, crops <= 1600 px for the cipher; tx/viv67_strips.py strips for the clerk pages);
U2 f.201v blind passes A (top-down) and B (bottom-up), tx/SIGNS.md, one call each, the pass text returned in the reply and written by me;
U3 ff.206r and 206v blind passes A and B (tx/DEC_READ.md), one page per call; U4 reconciliation: tx/viv67_prep.py-style [PLAIN] fix,
tools/reconcile_passes.py, tx/reconcile_vivk.py's six label rules unchanged -> tx/f201v_rec.tsv; tx/viv67_merge_dec.py f206r f206v --out
dec67b_norm.txt; then the gate. If U3 would cross 80%, f.206v is dropped and the target is the tail + f.206r only (said in the result).

**Target string.** T = the last 401 letters of tx/dec67_norm.txt's letter string (sa.letters, i.e. letters[1701:2102], the part f.201r did not
reach) followed by the letters of tx/dec67b_norm.txt (ff.206r-206v merged). Trim rule exactly PREREG-VIV70B's: the first int(n x 1403 / 1270)
+ 200 letters of T, n = collapsed codes of the f.201v stream (if that exceeds len(T), T is used whole). The rule assumes the cipher page
opens the target: f.201v follows f.201r directly, and f.201r's alignment ended at dec67[1701] (tx/vivk67_result.json window end 1901 - 200).

**Gate (code unchanged from build_vivonne_f211r.py's control(); new driver benchmark-tx/build_vivonne_f201v.py imports it).** The f.201v
stream (c2.raw_tokens of tx/f201v_rec.tsv, [PLAIN]/[...] dropped, o o collapsed) decoded with the published key (key_tomokiyo.tsv), aligned
by confirm2's align() (band_dp band 400, match 2, mismatch -1, gaps 1, free_start) to the trimmed T; window = aligned span +-200; match share
for the real key and 200 value-shuffled keys (random.Random(20261014)). **PASS iff the real key ranks 1 of 201 AND real > shuffled p95
(sorted[189]).** Run ONCE. key.tsv full set (50 draws) reported beside, not gating. Reported beside, not gating: err_2reader (disagreement
columns / aligned columns, reconcile_passes), A/B word agreement per decipherment page.

**If PASS:** (a) benchmark-tx/vivonne1573-f201v-dev.truth.tsv (split=dev) by the same truth() recipe (forcing set = published-and-C rows of
key.tsv; excluded unaligned / off-key / key-M / letter-off-key / align-uncertain window 8, 0.5; flags align-conflict, clerk-split, the
clerk-split mask built from the two blind passes of each decipherment page, dec67's mask for the tail), control numbers and "PREREG-VIV67B"
in the header, a BENCHMARK-TX.tsv row; tools/tx_bench.py on passA, passB (independent) and committed (circular), as measured and
flagged-excluded. (b) tx/viv67b_labels.py (tx/viv67_labels.py's method) -> tx/viv67b_labels.tsv + _summary.tsv, counts only, no key edit.
**If FAIL:** stop; report the numbers; no truth file, no label table beyond raw counts. No re-run under another target or trim.
Stop rule: as above; cost is not visible to this session, so the unit estimate decides.
