# PREREG-VIV70C (15 Oct 2026, 02:1x UTC by date -u; VIV-70C2 worker, session_01PQQeT5nvVaht6zBgPNhQBa, account 2, for LANE VIV-KEYSTONE, account 4)

Brief: .claude/briefs/runs/2026-10-15-acct4-for-acct2-jobs.md "JOB VIV-70C" (re-queued as VIV-70C2, ROOM.md 01:50 UTC 15 Oct) = NOTES
"VIV-70B"'s "Next" line. Written and pushed BEFORE any native fetch, any blind pass, any decode and any alignment; only four 600 px overviews
(c216, c217, c221, c222) have been looked at. Nothing here edits key.tsv, reading_piece63.tsv, status.json or any committed reading.

**Which blind use this is (correcting the brief's wording).** The brief calls this the trim rule's first blind use. PREREG-VIV67B already
applied the same rule blind to ink 67's second leaf (f.201v; PASS 0.714 vs p95 0.498). This run is the rule's first blind use on a pair
that did not supply its constant: the ratio 1403/1270 comes from ink 67 / ink 68 only, and ink 70's f.211r run (VIV-70B) was not blind.

**Leaves (by eye on the 600 px overviews, openapi.bnf.fr).** c216 left = f.210v (blank but a docket), c216 right = f.211r (VIV-70). So the
offset canvas = folio + 5 holds for rectos and a verso sits on the left of the next canvas: **c217 left = f.211v**, a full page of cipher,
about 30 lines, a short heading line above; c217 right = f.212r, about 26 cipher lines. Decipherment (ink 71): c220 right / c221 left =
ff.215r-215v (on disk, tx/dec70_norm.txt); c221 right = f.216r, c222 left = f.216v, c222 right = f.217r (clerk French, not read).

**Scope decision (made here, before any pass).** Cipher page = **f.211v only**; target = the part of dec70 that f.211r did not reach.
Reason: f.211r's alignment ended at dec70 letter 533 (tx/vivk70b_result.json window [0, 733], unclipped end 733 - 200), so 2,614 - 533 =
2,081 letters of ff.215r-215v are unused; by ink 67's ratio f.211v's ~30 lines (~1,600 codes at f.211r's ~52 per line) need ~1,770 letters,
i.e. nearly all of them, so f.212r's text lies on f.216r-216v. A second unit (f.212r passes A/B + f.216r and f.216v passes A/B + one
reconciliation) is 6 Sonnet calls + 1 unit: with U1 at Opus floor 2.5 + 2 calls x 1.4 + 1 reconciliation x 1.4 = 6.7, U2 adds 9.8 -> 16.5,
over 80% of the cap (9.6) by the README estimate; even U2 cut to f.212r + f.216r only (4 calls + 1) is 13.7. **U2 is not started**; it is the
one-line next step. No network request for f.212r or ff.216r-217r beyond the overviews already taken.

**Units, in order.** U1 one native fetch (c217 left region; 1 request, take/release lines in ROOM.md) and crops (tools/iiif_lines.py
--debug overlay checked by eye, crops <= 1600 px wide, pasted in NOTES before the first reader call); two blind Sonnet passes, A (top-down)
and B (bottom-up), tx/SIGNS.md, one page per call, crop paths only, text returned in the reply and written by me to tx/f211v_passA.tsv /
tx/f211v_passB.tsv; `tx/viv67_prep.py f211v`; `tools/reconcile_passes.py tx/f211v_passA_c.tsv tx/f211v_passB_c.tsv --out-dir tx/rec_f211v`;
`tx/reconcile_vivk.py f211v` (six label rules unchanged) -> tx/f211v_rec.tsv. Then the gate, once.

**Target string.** T = letters[533:] of tx/dec70_norm.txt's letter string (sa.letters), 2,081 letters (the part f.211r did not reach). Trim
rule exactly PREREG-VIV70B's: the first int(n x 1403 / 1270) + 200 letters of T, n = collapsed codes of the f.211v stream (c2.raw_tokens of
tx/f211v_rec.tsv, [PLAIN]/[...] dropped, o o collapsed). If that length is >= len(T), T is used whole and the trim rule is reported as
**not exercised** (its own verdict below is then "not tested", never a pass).

**Gate (alignment; code unchanged).** New driver benchmark-tx/build_vivonne_f211v.py (build_vivonne_f201v.py with the 70C names) calls
build_vivonne_f211r.control() unchanged: published key (key_tomokiyo.tsv), confirm2's align() (band_dp band 400, match 2, mismatch -1, gaps
1, free_start), window = aligned span +-200 clipped to the trimmed T, match share for the real key and 200 value-shuffled keys
(random.Random(20261014)). **PASS iff the real key ranks 1 of 201 AND real > shuffled p95 (sorted[189]).** Run ONCE (`--control-only`,
writes tx/vivk70c_result.json). key.tsv full set (50 draws) reported beside, not gating. Reported beside, not gating: err_2reader.

**Trim rule's own verdict (a separate result, registered here).** The rule predicts f.211v's span in T as int(n x 1403/1270) letters. In the
same single run, the f.211v stream is also aligned by c2.align() (same key, same parameters) to the whole untrimmed T (report only, no null),
and the aligned span is measured as last aligned letter index - first aligned letter index + 1. **Trim rule PASS iff the alignment gate
passes AND |span - predicted| / predicted <= 0.15**; FAIL otherwise; "not tested" in the case above. Disclosure: the tolerance was chosen
knowing the two earlier spans against the same prediction (f.211r: 533 vs 573, -7%; f.201v: about 1,580 vs 1,777, -11%); it is not tuned
on f.211v, which nobody has read.

**If the alignment gate PASSES:** (a) benchmark-tx/vivonne1573-f211v-dev.truth.tsv (split=dev) by the truth() recipe of build_vivonne_f201v.py
(forcing set = published-and-C rows of key.tsv; excluded unaligned / off-key / key-M / letter-off-key / align-uncertain; flags align-conflict,
clerk-split with dec70's clerk mask from build_vivonne_f211r.clerk_mask sliced [533:]), control numbers and "PREREG-VIV70C" in the header, a
BENCHMARK-TX.tsv row; tools/tx_bench.py on passA, passB (independent) and committed (circular), as measured and flagged-excluded. (b) the
label table (tx/viv70_labels.py's method, a --f211v option) -> tx/viv70c_labels.tsv + _summary.tsv, counts only, no key edit.
**If FAIL:** stop; report the numbers; no truth file, no benchmark row, raw label counts only. No re-run under another target, offset or trim.
Stop rule: cap 12 / box 02:13-04:43 UTC 15 Oct (80% = 9.6 / 04:13); cost is not visible to this session, so the unit estimate decides; no unit
started that would cross either.
