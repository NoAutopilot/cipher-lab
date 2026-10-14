# PREREG-VIV67 (14 Oct 2026, 00:1x UTC by date -u; VIV-67 worker for LANE VIV-KEYSTONE, account 4)

Brief: .claude/briefs/runs/2026-10-13-acct4-keystone-viv-jobs.md "VIV-67". Written and pushed BEFORE any blind pass, any decode of
f.201r and any alignment. Nothing here edits key.tsv, reading_piece63.tsv, status.json or any committed reading.

**Pair.** BnF fr.16105 f.201r (btv1b9009663p canvas 206, right page; old ink 67, Saint-Gouard to Charles IX, Madrid 20 Oct 1573;
confirmed by eye on a 600 px overview: "20 Octobre 1573 Madrid", "du s. de S.t Goard au Roy", "67 / 201"): four plain lines
("Sire, Encores quil ne se presente ...") then 24 cipher lines (crop bands L02-L25; L01 = the fourth plain line, whose end may
carry cipher). Known text: its clerk decipherment, ink 68 "dechiffre de la precedente", f.205r (c210 right) and f.205v (c211 left),
read in two blind Sonnet passes per page (tx/DEC_READ.md prompt), merged by tx/merge_dec.py's rules into tx/dec67_norm.txt (same
normalisation; tx/dec_norm.txt of ink 41 is NOT touched).

**Cipher transcription.** Two blind Sonnet passes on the f.201r line crops (tx/SIGNS.md conventions, one page per call), then
tools/reconcile_passes.py, then tx/reconcile_vivk.py's six label rules (unchanged) -> tx/f201r_rec.tsv. err_2reader = disagreements /
aligned positions as reconcile_passes reports it.

**Gate (the pair stands only if both hold).** Statistic = benchmark-tx/build_vivonne_confirm2.py's control, unchanged in code:
the f.201r stream (raw tokens of tx/f201r_rec.tsv, [PLAIN]/[...] dropped, o o collapsed, exactly its collapse()) decoded with the
published key (key_tomokiyo.tsv) and aligned to dec67 letters by its align() (stools/stream_align.band_dp, band 400, match 2,
mismatch -1, gaps 1, free_start, linear ref); window = aligned span +-200 letters; match share = aligned keyed signs whose value
equals the aligned letter / aligned keyed signs, re-aligned inside the window for the real key and for each of 200 value-shuffled
keys (random.Random(20261014)). PASS iff the real key ranks 1 of 201 AND real share > the shuffled p95 (sorted[189]).
No anchor scan, no parameter choice after seeing a score; the whole dec67 text (both pages) is the target string.
Reported beside, not gating: the same with key.tsv's full value set (C, M and V rows).

**If PASS:** (a) unkeyed-label table: every token of f201r_rec.tsv whose label is outside key_tomokiyo.tsv or M-graded in key.tsv
(c, o, e, 2, r, l, Z, t, S, y, b, A, V and any other), with the aligned clerk letter at each occurrence and the local DP confidence
(share of keyed neighbours within 8 positions decoding to their aligned letter) -- counts only, no key edit; (b) a truth item
benchmark-tx/vivonne1573-f201r-dev.truth.tsv (split=dev) built by build_vivonne_confirm2.py's recipe (forcing set, exclusions,
align-uncertain window 0.5, align-conflict and clerk-split flags set at build time), registered in BENCHMARK-TX.tsv with the
control numbers in the header; err of passA/passB/committed reported, the committed figure stated as circular.
**If FAIL:** stop after the control; report the numbers; no truth file, no label table beyond raw counts.
Stop rule: cap 12 / box 150 min; no unit started that would cross 80% of either.
