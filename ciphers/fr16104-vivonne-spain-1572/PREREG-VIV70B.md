# PREREG-VIV70B (14 Oct 2026, 02:1x UTC by date -u; VIV-70B worker, account 2, for LANE VIV-KEYSTONE, account 4)

Brief: .claude/briefs/runs/2026-10-13-acct4-keystone-viv-jobs.md "Account-2 row VIV-70B" (= NOTES "VIV-70"'s own "Next"). Disk only, no
network, no vision call. Written and pushed BEFORE the re-run below. Nothing here edits key.tsv, reading_piece63.tsv, status.json or any
committed reading. PREREG-VIV70.md's registered verdict (FAIL, rank 2 of 201) stands for the untrimmed run; this is a separate run under a
trim rule, registered here.

**Disclosure (rule 3, honest order of events).** VIV-70 already ran the same trim rule post hoc (tx/viv70_diag_trim.py ->
tx/vivk70_diag_trim.json: 0.769 vs p95 0.522, rank 1 of 201) after its registered gate failed, and named it as the next registered run. The
rule below was fixed by the brief from ink 67 alone, not tuned on f.211r: no constant in it comes from the f.211r alignment. But the outcome
on this pair is therefore not blind; this run registers the rule and re-computes it once, and the result is reported with that caveat. The
rule's independent test is its next use on a pair it has not seen (f.211v ff., or another sibling).

**Trim rule (derived from ink 67 only).** ratio = dec67 aligned letters / f.201r codes, read from tx/vivk67_result.json control_published:
aligned letters = (window[1] - 200) - (window[0] + 200) = (1901 - 200) - (98 + 200) = 1,403; codes = n_signs = 1,270. Target for a cipher
stream of n codes that opens its decipherment = the first int(n x 1403 / 1270) + 200 letters of the decipherment letter string (for f.211r,
n = 519 collapsed codes of tx/f211r_rec.tsv, the stream PREREG-VIV70 built -> 773 letters of tx/dec70_norm.txt). The +200 is confirm2's
window margin. The rule assumes the cipher page starts the decipherment (true here by eye: f.211r's cipher opens "Quant a l'apparence de leurs
affaires", dec70's first words; NOTES "VIV-70").

**Gate (unchanged from PREREG-VIV70 except the target string).** benchmark-tx/build_vivonne_f211r.py's control(), code unchanged, called
with the trimmed letter string: published key (key_tomokiyo.tsv), confirm2's align() (band_dp band 400, match 2, mismatch -1, gaps 1,
free_start), window = aligned span +-200 clipped to the trimmed string, match share for the real key and for 200 value-shuffled keys
(random.Random(20261014)). PASS iff the real key ranks 1 of 201 AND real > shuffled p95 (sorted[189]). Run ONCE: `python3
benchmark-tx/build_vivonne_f211r.py --trim-ink67` (writes tx/vivk70b_result.json; tx/vivk70_result.json untouched). key.tsv full set (50
draws) reported beside, not gating.

**If PASS:** (a) build and register benchmark-tx/vivonne1573-f211r-dev.truth.tsv (split=dev) with build_vivonne_f201r.py's recipe (the
truth() of build_vivonne_f211r.py, code unchanged, on the same trimmed string; clerk-split mask = the full-string mask truncated to it),
control numbers and "VIV-70B trim rule, PREREG-VIV70B.md" in the header, a BENCHMARK-TX.tsv row; tools/tx_bench.py on passA, passB
(independent) and committed (circular, as confirm2's committed figure), as measured and flagged-excluded. (b) tx/viv70_labels.py (VIV-70's
script, viv67_labels.py's method) run on the same trimmed alignment -> tx/viv70_labels.tsv + tx/viv70_labels_summary.tsv, counts only, no
key edit.
**If FAIL:** stop; report the numbers; no truth file, no label table.
Stop rule: cap 3 / box 60 min (02:14-03:14 UTC 14 Oct); no step started that would cross 80% of either (03:02 UTC).
