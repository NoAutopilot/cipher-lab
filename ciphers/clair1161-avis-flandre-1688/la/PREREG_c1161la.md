# PREREG D2-C1161LA (account-1 worker for LANE-D2PUSH), written 5 Oct 2026 18:5x UTC by date -u, before any re-read or score

Brief: .claude/briefs/runs/2026-10-05-acct1-d2-c1161la.md. Target: key-constrained look-alike pass on th/z/S/4.

## Packet (built, no model call yet)
- Alignment: la/build_align.py -- C = ciphertext.tsv (merged), A/B = tx/<leaf>_passA/B.tsv aligned per line by edit
  distance (lookalike_pass._align); reader synonyms ss/NEW:5hook -> s, NEW:v-bar -> vdash, epsilon -> e. 3434 signs:
  agree 2971, split 299, split_gap 81, A=B!=C 83. Confusion: la/confusion.tsv (299 swaps, top tz/z 36, iib/iii 17).
- Tiles: la/make_tiles.py -- every split/split_gap position with th, z, S or 4 on any side (merged, A or B): **109 tiles**
  (merged z 45, s 17, th 11, S 6, dia 4, 4 only 2, others 24). The agreed th/z/S/4 tokens (most of the 896) are NOT in
  the packet: a 2-of-3 rule cannot move a position both readers agree on (LESSONS.md "Look-alike pass": that is where
  half of true errors sit, so this pass is agreement-raising, not accuracy-raising).
- Instrument: `tools/lookalike_pass.py windows` (packet-format tiles, label hidden, candidates alphabetical, shape
  descriptions la/desc.tsv from tx/labels_v2.md), --per 10 --scale 1, from the existing native line crops (images/,
  cut by the iiif_lines.py commands recorded in NOTES.md, e.g. `python3 tools/iiif_lines.py --ark btv1b90010063 --canvas
  187 --region 3800,1300,3400,4650 --out ...`; c186R block lines from the c186Rblk crops) via la/crops/manifest.json.
  11 montage JPEGs la/win/c1161la_win_01..11.jpg, never a full page.
  Command: `python3 tools/lookalike_pass.py windows --tiles la/c1161la_tiles.tsv --passc la/passC.tsv --manifest
  la/crops/manifest.json --crop-pattern '{line}_s*' --out la --run c1161la_win --per 10 --scale 1 --desc la/desc.tsv`

## Pricing (Usage 6, per pass)
- Re-read: 3 Sonnet subagent calls (montages 01-04, 05-08, 09-11; about 40 tiles each), est. USD 0.6 per call = 1.8.
  One value-blind reader (the brief's "one re-read"; Sonnet for the tile read, allowed if priced). No reconciliation
  model call: reconcile is the script. Total cap 6, stop before starting a call that would cross 80% (4.8).

## Fold-in (fixed, the tool's rule)
`lookalike_pass.py reconcile --tiles la/c1161la_win_tiles.tsv --passc la/passC.tsv --reread la/reread.tsv --out la/passD.tsv
--alt la/passD_alt.tsv --focus la/focus.tsv`: a firm (H/M) re-read matching A or B settles 2-of-3; else UNSETTLED, passC kept.
The residual is agreement, never reader error.

## Test (fixed before any score; la/la_test.py)
Relabel set R = positions where passD != passC. Under the UNCHANGED key.tsv:
- G = glossctl stat (c186R block decode vs its period gloss); J = fr16 NgramModel.score on the letters-only decode;
  L = longest C/S run (token grade = key grade, lowered to M when conf != H), reported, not gated.
- Control: 50 seeds, the same multiset of (from -> to) relabels at random positions carrying the same `from` label
  (excluding R). Rule-3 check: the control moves different positions, so dG and dJ can differ from the target's; dG is
  non-discriminating if R has no c186R tile (both 0) -- then G cannot pass and the set is NOT applied.
- Gate: R applied to ciphertext.tsv only if real dG > null p95 AND real dJ > null p95 (strict). One test, no re-tuning.
- If R is empty: no test; logged.
- If applied: decode_key --check, grades, depth_check, longest C/S stretch quoted; no depth/novelty change by this worker.
