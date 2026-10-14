# PREREG-VIV70 (14 Oct 2026, 01:2x UTC by date -u; VIV-70 worker, account 2, for LANE VIV-KEYSTONE, account 4)

Brief: .claude/briefs/runs/2026-10-13-acct4-keystone-viv-jobs.md "VIV-70" (= the VIV-67 job with the ink 70/71 substitutions). Written and
pushed BEFORE any image fetch beyond the 600 px overviews, any blind pass, any decode of f.211r and any alignment. Nothing here edits key.tsv,
reading_piece63.tsv, status.json or any committed reading. Method and code exactly PREREG-VIV67.md's; only the names change.

**Pair.** BnF fr.16105 f.211r (btv1b9009663p canvas 216, right page expected; old ink 70, Saint-Gouard to Charles IX, docket 4/5 Nov 1573),
confirmed by eye on a 600 px overview before any native fetch. If the cipher does not start on f.211r (a plain head longer than a page), the
first page that is mostly cipher is taken instead and the decipherment pages that match its opening (brief). Known text: its clerk
decipherment, ink 71 "dechiffre de la precedente", f.215r (c220 right) and f.215v (c221 left), each read in two blind Sonnet passes
(tx/DEC_READ.md prompt), merged by tx/merge_dec.py's rules (tx/viv67_merge_dec.py generalised with an --out name) into tx/dec70_norm.txt.
tx/dec_norm.txt (ink 41) and tx/dec67_norm.txt (ink 68) are NOT touched.

**Cipher transcription.** Two blind Sonnet passes on the f.211r line crops (tx/SIGNS.md conventions, one page per call, line crops under
2500 px cut by tools/iiif_lines.py and pasted before the first call), the VIV-67 [PLAIN:...] tokenisation fix, tools/reconcile_passes.py,
then tx/reconcile_vivk.py's six label rules (unchanged) -> tx/f211r_rec.tsv. err_2reader = disagreements / aligned positions as
reconcile_passes reports it.

**Gate (the pair stands only if both hold).** benchmark-tx/build_vivonne_f211r.py = build_vivonne_f201r.py with the names substituted, code
otherwise unchanged: f.211r stream (raw tokens of tx/f211r_rec.tsv, [PLAIN]/[...] dropped, o o collapsed by confirm2's collapse()) decoded
with the published key (key_tomokiyo.tsv), aligned to the whole dec70 letter string by confirm2's align() (tools/stream_align band_dp, band
400, match 2, mismatch -1, gaps 1, free_start); window = aligned span +-200; match share re-aligned in the window for the real key and for
200 value-shuffled keys (random.Random(20261014)). PASS iff the real key ranks 1 of 201 AND real share > shuffled p95 (sorted[189]).
No anchor scan, no parameter choice after seeing a score. Reported beside, not gating: key.tsv's full value set (50 draws), which now carries
VIV-KEY's e -> m row (whatever its state at run time is recorded).

**If PASS:** (a) unkeyed/M-label table tx/viv70_labels.tsv + tx/viv70_labels_summary.tsv (tx/viv67_labels.py's code, names substituted):
every token outside key_tomokiyo.tsv or M-graded in key.tsv with the aligned clerk letter and the local DP confidence -- counts only, no key
edit; (b) truth item benchmark-tx/vivonne1573-f211r-dev.truth.tsv (split=dev) by the same recipe, registered in BENCHMARK-TX.tsv with the
control numbers in the header; err of passA/passB/committed reported by tools/tx_bench.py (as measured / flagged-excluded), the committed
figure stated as circular.
**If FAIL:** stop after the control; report the numbers; no truth file, no label table beyond raw counts.
Stop rule: cap 12 / box 150 min (01:13-03:43 UTC); no unit started that would cross 80% of either (03:13 UTC).
