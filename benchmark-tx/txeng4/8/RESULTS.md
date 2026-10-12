# TXE4-8 BOX-ANCHOR results: numbered machine boxes on the Saint-Gouard line images, one answer per box (account 3, Fable 5.1 worker, session_014V4uay7sV21NShHzNwq1sU; 12 Oct 2026 01:18-01:5x UTC by date -u)

Pre-registration: benchmark-tx/PREREG-txeng4-8.md (committed 4391e7f29 before any read; addendum with the can-vary count, the cvd
verdict and the pass order in 27f17577c, also before any read). Brief: `.claude/briefs/runs/2026-10-11-acct3-txe4-8.md`.
**Verdict: gate NOT MET -- a negative, not a null.** Giving the Sonnet reader the machine's numbered pen boxes and asking one
answer per box made the read WORSE than a free line read on both masks, and the random-geometry overlay at the same count read
exactly like the pen overlay: the per-box output format, not the box placement, carries the change, and the change is a loss.
Dev result (vivonne1573-f102r-dev2); no eval or confirm item opened; no truth file edited; no owner evidence used.

## Item and split
- vivonne1573-f102r-dev2 (dev; Saint-Gouard clerk 1573; truth the clerk's period decipherment under the published Tomokiyo key).
  The 13 TXE3-6 TEST lines (f102r_L02, L04, L08, L10, L16, L18, L20, L24, L28, L30, L32, L34, L36): 662 truth positions, 417
  scored, 216 scored after the flagged-excluded mask (201 clerk-split / align-conflict flags). Crops as committed (1600 x 102 px).
- Boxes: `benchmark-tx/txeng3/6/seg/pen/boxes.tsv` test-line rows (569 pen-unit boxes for 662 truth positions), copied to
  boxes_O.tsv. R set boxes_R.tsv: `tools/iiif_lines.py --box-overlay boxes_O.tsv --random-geometry 20261013` (same count per
  line, boundaries uniform random inside the line's ink extent, pen band as height).
- **Can-vary count (before any read): 423 / 569 = 0.743 of R boxes have IoU < 0.5 with every pen box of their line** -- R
  differs from O in geometry at an equal count (VERIFY-6's count confound closed).
- Overlay palette through `tools/cvd_check.py --marks '#0072B2,#B35900,#000000' --bg '#ffffff' --tints '#F0E442' --text
  '#000000' --tint-text '#F0E442:#000000'`: normal worst pair dE2000 39.2 (+19.2), protan 38.1, deutan 38.3, tritan 41.5; **PASS**.

## Arms and calls (all Sonnet claude-sonnet-5, fresh context per call; sheet_tomokiyo_v1.png and the SHEET-VIV task text)
- N free line read (SHEET-VIV `reader_task.txt` as is), 2 passes. O pen-box overlay, one row per numbered box, 2 passes. R
  random-geometry overlay at the pen count, same task text and format as O, 1 pass. Task texts: tasks/*.txt.
- Registered order R1, O1, N1, N2, O2 (`random.Random(20261013)`). The registered fallback applied at the first call: the
  one-call R1 reader answered boxes on L02-L10 only and filled L16-L36 with "-" unread (its own report; kept as
  reads/R1_call1_incomplete.tsv, sha256 in SHA256SUMS.prescore, never scored), so EVERY pass of every arm ran as two calls of
  7 and 6 lines (a = L02-L20, b = L24-L36), 10 calls in all, merged by merge_halves.py. The O2a reader truncated L08 at box 18
  of 38 (20 boxes unanswered); O2 is scored AS DELIVERED (R3, scored once), which counts against O; O1 is complete and loses
  to both N passes on its own, so the verdict does not rest on O2.
- Every read committed with its sha256 before scoring (SHA256SUMS.prescore, commits 89b408996, 3576f454e, 6e49542df, 9d59f712f,
  ea3b2f6c6); scorer score.py (box rows -> positions, then `tools/tx_bench.py --bench benchmark-tx/txeng3/6/bench_test.tsv
  --exclude-flagged --strict --coverage-diagnostic --ci`), run once per read; raw output in scores/*.txt, JSON in scores/*.json.

## Numbers (unit-cost edits = tx_bench ser_errors = S+D+I; err_true with Wilson 95%; wilson.tsv)

| pass | as measured (417): edits (S / D / I) | err_true, Wilson 95% | strict | flagged excluded (216): edits (S / D / I) | err_true, Wilson 95% | strict |
|---|---|---|---|---|---|---|
| N1 | **111** (98 / 7 / 6) | 0.266 (111/417) 0.226-0.311 | 0.130 | **21** (13 / 2 / 6) | 0.097 (21/216) 0.064-0.144 | 0.097 |
| N2 | **116** (98 / 15 / 3) | 0.278 (116/417) 0.237-0.323 | 0.127 | **22** (14 / 5 / 3) | 0.102 (22/216) 0.068-0.149 | 0.102 |
| O1 | **129** (94 / 24 / 11) | 0.314 (131/417) 0.271-0.360 | 0.185 | **37** (13 / 13 / 11) | 0.181 (39/216) 0.135-0.237 | 0.181 |
| O2 | **127** (90 / 31 / 6) | 0.307 (128/417) 0.265-0.353 | 0.194 | **33** (11 / 16 / 6) | 0.157 (34/216) 0.115-0.212 | 0.157 |
| R1 | **127** (97 / 14 / 16) | 0.309 (129/417) 0.267-0.355 | 0.187 | **37** (16 / 5 / 16) | 0.181 (39/216) 0.135-0.237 | 0.181 |

Arm means, as measured / flagged excluded: **N 113.5 / 21.5; O 128.0 / 35.0; R 127 / 37.** Within-arm spread: N 5, O 2.
Per-box answers: O1 37 of 569 boxes "-", 78 boxes with several tokens; O2 51 "-" (20 of them L08's unanswered tail); R1 208 "-",
150 multi-token boxes (the random boxes straddle signs, as they should).
Reader agreement (beside, no model call): O1 vs O2 by box (`reconcile_passes.py --by-box`, first use) 456 of 569 boxes agree
(80.1%), 113 disagree; N1 vs N2 by nw 590 of 651 columns (90.6%), 61 disagree (rec/).
Cross-session check (TXE4-1 arm D, the same configuration as N, committed fb60112cb before this file; quoted, never pooled):
D1 112 (94 / 9 / 9) as measured, 22 flagged excluded; D2 127 (94 / 14 / 19), 35. N here: 111 / 116 and 21 / 22.

## Gate (PREREG, the brief's words), applied
"The overlay is adopted for joining hands if all of these hold:"
- "mean(N) >= 1.15 x mean(O) as measured": 113.5 >= 147.2? **NO** (N is lower than O; O is 1.13x N).
- "mean(N) > mean(O) flagged-excluded": 21.5 > 35.0? **NO**.
- "the gap > the maximum within-arm spread": gap N-O = -14.5; spread max(5, 2) = 5: **NO** (the gap is negative; its size,
  14.5, does exceed the spread, so the LOSS is larger than either arm's pass-to-pass noise).
- "O's substitutions <= N's substitutions": 94, 90 <= 98, 98: yes (the only condition met: substitutions did not rise).
- "mean(R) >= mean(O) + O's pass spread": 127 >= 130? **NO** (R equals O within the spread).
**Gate NOT MET.** Reading, per the PREREG: the overlay is not adopted; "R matches O: the output format, not the boxes, carries
the gain" -- here the format carries a loss. Beside (not gated): O's insertions+deletions 35 / 37 against N's 13 / 18 -- the
per-box format did NOT lower indels as the brief expected "by construction": insertions did not fall (O 11, 6 against N 6, 3)
and deletions ROSE (O 24, 31 against N 7, 15) because a box answered "-" or under-filled deletes every sign the segmenter's box swallowed
(pen boxes join 662 truth positions into 569 units). The loss is on both masks and larger than the within-arm spread, but the
Wilson intervals of err_true overlap (N 0.226-0.323 vs O 0.265-0.360 as measured); at two passes per arm this is a reproducible
direction, not a tight estimate.

## What was not run, and why
- SECONDARY (reconcile -> tx_adjudicate packets, N packets through `tools/box_token_align.py` under R4a): NOT RUN. The PREREG
  allows it only if the five passes finish under 80% of the time box AND of the running estimate; time was fine (27 of 120
  min) but the running estimate (the Fable floor USD 9-10 for a vision-step shape plus five passes at 0.45-0.6 each, 11
  reader calls in all, plus the tools unit) sits at or past the USD 12 line, and the primary gate had already failed in the
  direction the secondary would have built on. No box-to-token join was made anywhere in this job, so no join check was
  needed (R4a); no width-DP file was read. The `--by-box` reconcile of O1/O2 above is disk-only and is reported beside.
- Not re-run: the O2a reader's truncated L08. A re-run would be a post-hoc choice in the treatment's favour.

## Limits
- Dev only; one hand; two passes per arm and one R pass; a single reader model. The flagged-excluded mask keeps 216 of 417.
- The N task text and the O/R task text differ in more than the overlay: O/R also changes the output unit (box) and forbids
  rows outside boxes, so N-vs-O measures the whole "anchored answering" protocol, as the brief designed; R isolates geometry
  from format within that protocol.
- The readers' own reports say they graded every row M (no H), and the R readers said they "padded with '-' where signs did
  not map onto boxes", which is the expected behaviour of a random box set; the O1 reader left alts empty.
- Access log (access_log.tsv, access_log_summary.txt): 11 reader agents, 2 calls outside the allow-list, both a helper write
  script the reader placed at /tmp/gen.py or /tmp/w.py (its own scratch write, no read of any other file); 0 reads outside the
  readers' own directories. Token usage per agent in usage.txt (input_all 0.44-1.01 M per call, lower-bound outputs).
- Hosts: 0 network requests (disk and model calls only).

## What it means for the owner (three plain sentences)
Telling the reader exactly where each sign is, with the machine's own boxes drawn and numbered, did not cut errors on the
Saint-Gouard hand: both box-anchored passes read worse than both free passes (128 edits against 113 on the 417 scored
positions, 35 against 21 on the clean subset), mostly because a box that swallows two signs or holds none makes the reader drop
signs it would otherwise have read. The machine's boxes were no better than boxes placed at random (127 edits either way), so
on this hand the box set is not yet good enough to anchor a reader without you. Do not wire the overlay into the joining-hand
pipeline; the next step is not more box drawing but better boxes, and the only box set that could still change this answer is
yours (the L74 re-cuts, geometry only), tested in this same design.

## Next step (named, not run)
The brief's "if it passes" wiring (overlay as the default join; feeding tx_adjudicate, the sorter and the pair classifiers)
is NOT taken. If the question is kept open, run the same three arms with the OWNER's verified boxes (ORACLE-LOCATION-1 arm B's
12 train lines, LANE TX-ENGINEER-2, account 4) as a fourth set O* beside O and R, two passes, about USD 2 of reader calls on
this tooling (the overlay option and the by-box reconcile exist now); if O* beats N where O did not, the loss is the machine's
boxes, not the format; if O* loses too, the per-box format itself is retired for this hand and the segmenter question is moot.

## Files
PREREG-txeng4-8.md (with addendum); boxes_O.tsv, boxes_R.tsv; overlays/O/, overlays/R/ (26 pages each, overlay_manifest.tsv);
tasks/*.txt (10 call texts, scratch paths replaced); build_tasks.py, merge_halves.py, score.py, wilson.py (wilson.tsv),
access_log.py (access_log.tsv, access_log_summary.txt), usage.py (usage.txt); reads/*.tsv (+ *.pos.tsv for O and R),
SHA256SUMS.prescore; scores/*.txt, *.json; rec/O_bybox/, rec/N_nw/. Tools: tools/iiif_lines.py --box-overlay /
--random-geometry / --overlay-lines (tools/tests/test_box_overlay.py), tools/reconcile_passes.py --by-box
(tools/tests/test_reconcile_by_box.py); both tools' existing tests still pass. Cost: from the parent's get_session.
