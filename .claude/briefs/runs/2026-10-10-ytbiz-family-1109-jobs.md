# LANE FAMILY jobs (account 2, incarnation DEFAULT-account-2-20261010-1109, "FAMILY-A2q") -- 10 Oct 2026 11:3x UTC, lane orchestrator session_01RLS2137Qu85hEjRnbTRzh6

Lane brief: .claude/briefs/lane-family.md (+ lane-common-blast.md). Cap 60, box 11:10-21:10 UTC 10 Oct (80% 19:10). Started from STATUS.md
"LANE FAMILY handoff (incarnation DEFAULT-account-2-20261010-0909)" next list (items 1-3 wait on a person or a LOCAL-QUEUE row; item 4 carried
rows re-read: Manteuffel 199/321 low yield, the rest gated) and a fresh `next_steps.py --hot-only` read at 11:2x UTC, plus
research/POOLS-FAMILY-2026-10-10.tsv (rows 1-5 done since; row 9 open). Every candidate was re-read in its dated NOTES sections; stale
`parallel` cells (harley ff.70-72 HAR-GLOSS done, rah-juan-manuel CSP map done twice, fr16144 Boucher done, fr16106 Mousset done,
clairambault296 residue done, august 153 key done, bne R1172 re-test done, wallis Thurloe 2-5 done, hessen Brandt done) skipped.
Gate 0a: SESSION-SWEEP-account-2 stale-claimed since 5 Oct (prior incarnations proceeded; so do we). Exclusions: eckert-* and Huntington
ledgers (LANE LEDGER-13/14, account 1, live), Gallica fetches, Armstrong/Debosnys/Birago, any folder with a ROOM claim < 6 h and no done.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with these
substitutions: address every ROOM line "for LANE FAMILY-A2q (account 2)"; the "Hosts this wave" bullet there is replaced by the one below.
Halfway line: one ROOM line at half the box or half the cap, whichever first (skip if done before). Account 2 is at seven_day
`allowed_warning`: continue (blast rules) and say so in the done line.
Hosts this wave: archive.org ("IA": THUR-B146 only, >= 1.5 s, <= 60 requests); de-crypt.org ("DECODE": COS-1167 only, ONE browser login,
`tools/decode_browser_login.js`); service.archief.nl / www.nationaalarchief.nl ("NA": SUR-MRICH only, <= 30 requests, only if the lines it
needs are not already on disk). MANT-Y49 is disk only (no sachsen request).

## Wave 1 (11:3x UTC 10 Oct)

### THUR-B146 (Sonnet, cap 2.5, box 75 min, IA <= 60 requests): thurloe-printed, Birch 1742 vols 1, 4, 6 cipher-passage sweep
The folder's "## Siblings (8 Oct 2026)" third bullet and POOLS row 9: only vols 2, 3, 5, 7 were swept for the 23 extracted items. Check 1
first (grep ROOM.md and the folder for collectionofstat01/04/06 or a vols 1/4/6 sweep after 8 Oct; if found, one ROOM line and stop).
Find the IA identifiers for Birch vols 1, 4 and 6 (advancedsearch, the same series as collectionofstat02thur..07thur), fetch each `_djvu.txt`
once to scratch (manifest of identifier, size, sha1 in the folder), and run `tools/ia_numeral_runs.py` (or its documented option for a local
text) to list runs of cipher numerals; calibrate first on vol 3 against the folder's own P-item pages (a positive control: the known P items in
vol 3 must be found; report recall). For each hit in vols 1/4/6 give: volume, page (from the djvu page markers), sender/recipient/date from the
heading, run length, whether Birch prints a decipherment beside it (then N0 by construction -- a key-source pair, not a reading), and which
existing folder key (key_*.tsv, KH2-F list) shares the correspondent. No decoding, no transcription, no vision call. Output
`ciphers/thurloe-printed/b146/hits.tsv` + NOTES "## THUR-B146", Remaining gaps / Escalation / Verdict, gaps_check.py. A run with no printed
decipherment and a key in hand: one ROOM flag line for the lane. Report what was found and where it was not found; do not classify novelty.

### MANT-Y49 (Opus, cap 3.5, box 75 min, disk only): sachsstaatsarchiv-manteuffel-1712, pre-registered census of the y-shaped 4|9 glyph
The folder Verdict's named step (MANT-FIX, 9 Oct 2026): "the y-glyph 4|9 question stays open for a pre-registered census, ~$2", and the per-hand
question MANT-EYE63 left (694/09 0063 slot01/03/04: 7/24/34 vs 9/29/39). Read ONLY: NOTES MANT-FIX, MANT-EYE63 (grep "MANT-EYE"),
V-MANTC, MANT-CUC3 sections, key.tsv, and the committed strips/crops they cite. PREREG-MANTY49.md pushed in its own commit BEFORE any read:
the census set (every committed native strip slot whose digit is a 4 or a 9 in the transcription, by hand/file -- list them from the TSVs by
script first, no image read), the known-answer subset (slots where the gloss or the key fixes the digit, e.g. a glossed code whose 4- and
9-reading give different letters and only one fits the gloss), the blind reading protocol (two Sonnet passes on digit crops with no key, gloss
or transcription shown, one crop sheet per call), the statistic (blind agreement with the known answer on the known subset, against a
shuffled-label control that CAN differ), the gate, and what changes on PASS (only the unknown-subset digits the gate licenses, as M; per-hand
split reported). Crop step pasted. No sachsen request: if a needed crop is not committed, list it as owed. NOTES "## MANT-Y49", Remaining
gaps / Escalation / Verdict, gaps_check.py, decode --check after any edit. Report what was found and where it was not found; do not classify
novelty. Units: 2 blind passes + 1 reconciliation at ~0.6, plus session floor.

### COS-1167 (Opus, cap 3, box 75 min, DECODE one login): costabili-modena-1491, R1167 P2 L1-21 / P3 completeness against its clear copy
The folder Verdict's cheapest next ("R1167 P2 L1-21/P3 completeness vs copy (~$1)"). Read ONLY NOTES D4-COST, D4-COST2, D4-COST3 sections
(grep "D4-COST"), the COS-M per-page table, "## Remaining gaps" and "## Escalation". Check 1 first. ONE DECODE login
(`NODE_PATH=$(npm root -g) node tools/decode_browser_login.js 1167 <scratch> --guess-fullsize --max-files 8`), pages to scratch only, sha1s
against the folder's manifest; never commit the saved HTML; scrub the account name. The question is completeness, not a token alignment: does
the cipher letter on P2 (lines 1-21) and P3 carry the same text as the clear copy P5-P6, span by span, or does one side drop or add a clause?
Use the clear words that sit in clear on the cipher pages and the copy's paragraph structure as anchors (as D4-COST did for P1); measure per
span cipher-group count vs copy word count against the P1 ratio already aligned (D4-COST), and flag spans whose ratio falls outside the P1
range. No new key value, no grade change; any TT/Z/q observation is descriptive only (that route is retired, D4-COST3). Commit only a small
span table (`align/cos1167_spans.tsv`) and, if a later eye check needs it, JPEG crops under 1 MB total. NOTES "## COS-1167", Remaining gaps /
Escalation / Verdict, gaps_check.py. Known-text item: report the time spent. Report what was found and where it was not found; do not classify
novelty.

### SUR-MRICH (Opus, cap 4.5, box 90 min, disk first, NA <= 30): na-suriname-map-1781, m-rich glossed lines as held-out units for the m|n split
The folder Verdict's cheapest next (SUR-0745R, 9 Oct 2026): "m-rich glossed lines (count gloss m per page first) or the key-blind statistic at
88 lines, ~$2-3". Read ONLY NOTES SUR-SPLITPC, SUR-POOLPC, SUR-PARTIAL, SUR-KB, SUR-0745R, SUR-372 sections and the scripts/PREREGs they name.
Step 1 (script, no vision): count gloss m per page/line on every glossed page already transcribed or imaged on disk (inv. 372 0183-0195,
inv. 373 0692-0693, 0743-0745, 0701/0703, others the sections list), from the committed gloss TSVs where they exist; list the m-richest lines
not yet in the 88-line pool. Step 2: only if those lines would lift pooled gloss m enough to give the pre-registered SPLIT test power >= 0.8 at
f 0.50 (compute this first from SUR-0745R's power method and write it in PREREG-SURMRICH.md, pushed in its own commit BEFORE any read), blind
two-pass transcribe those lines (crop step pasted, one page-half per call; fetch from NA only lines not on disk, take/release lines) and run
the existing SPLIT test unchanged on the enlarged pool. If no set of lines on disk or in the 30-request budget reaches that power, stop after
step 1 and write the number of m-glossed lines still needed (that is the result). NOTES "## SUR-MRICH", Remaining gaps / Escalation / Verdict,
gaps_check.py. Report what was found and where it was not found; do not classify novelty. Units: 2 passes x 2 halves + 1 reconciliation at
~0.6, plus session floor.

## Wave 1 results (costs by get_session)

Intake gate (11:3x UTC, pasted before spawning): thurloe-printed, sachsstaatsarchiv-manteuffel-1712, costabili-modena-1491,
na-suriname-map-1781 each "partial -- edition/page or full-text-search citation found within 6 lines", exit 0. ROOM: no live claim on
any of the four (last: costabili FAM-COSCREM done 09:2x, Suriname SUR-DENSE done 00:12, Manteuffel MANT-66 done 00:3x).
- THUR-B146 2.13 / 2.5 (Sonnet): Birch vols 1/4/6, 108 numeral groups (b146/hits.tsv); vol 3 control 10/10, 15/18 known windows overall;
  OCR read of 11: 4 printed gloss (key-source pairs), 3 inline no-gloss (Dutch ambassadors 1652-53, family on file), 4 symbol noise; no keyed
  correspondent run without gloss; `ia_numeral_runs.py --inline-run` added with offline test. archive.org 6.
- MANT-Y49 5.63 / 3.5 (Opus, 1.61x over): PREREG b11237295; 77 gloss-fixed slots, 2 blind passes, gate PASS (BA 0.883/0.862 vs p99 0.59) but
  the 8 gloss-wants-9 transcribed-4 slots read 4 in both passes -> y-glyph untested-by-this-tool (2nd blind-read attempt); 0063 A1 tok2 7->9 M.
- COS-1167 2.95 / 3 (Opus): R1167 P2 L1-20/P3 cut into 10 cipher spans with group counts (align/cos1167_spans.tsv); copy P5/P6 not fetched
  (--max-files spent on thumbnails + P1-P4); completeness not established.
- SUR-MRICH 3.64 / 4.5 (Opus): no m-rich glossed page on disk; PREREG 58e514904; power at f 0.50 +23 lines 0.467/0.333, +117 0.633/0.500,
  +234 0.900/0.850 -> gate FAIL, no transcription; ~120-235 more glossed lines (~$40-60, a campaign) needed.
Wave 1 total 14.35; orchestrator 3.28 at 12:15.

## Wave 2 (12:2x UTC 10 Oct)
Hosts this wave: de-crypt.org ("DECODE": COS-1167B only, ONE browser login); archive.org ("IA": THUR-V6 only, <= 30 requests).

### COS-1167B (Opus, cap 2.5, box 60 min, DECODE one login): costabili-modena-1491, finish COS-1167 -- copy P5/P6 against the 10 spans
Read ONLY NOTES "## COS-1167" and align/cos1167_spans.tsv, align/cos1167_ref.py. ONE DECODE login fetching ONLY R1167's P5 and P6 full-size
pages (COS-1167's own lesson: thumbnails count against --max-files under --guess-fullsize; name the pages explicitly with the tool's page
option, check `node tools/decode_browser_login.js --help` first); scratch only, sha1s into the manifest, never commit the saved HTML, scrub the
account name. Transcribe only the copy words needed to bound each of the 10 spans (one Sonnet pass on line crops + your own check; this is
text known from the copy, no key work), compute copy_words and the groups/word ratio per span against the reference range COS-1167 already
set (0.615-1.053), and flag spans outside it. No key or grade change. NOTES "## COS-1167B", Remaining gaps / Escalation / Verdict,
gaps_check.py. Report what was found and where it was not found; do not classify novelty.

### THUR-V6 (Sonnet, cap 2, box 60 min, IA <= 30): thurloe-printed, image check of the 8 Birch vol 6 hits THUR-B146 could not read in OCR
The folder Verdict's cheapest next (THUR-B146: "IA availability check and crops of the 8 vol 6 hits, ~$1.5"). Read ONLY NOTES "## THUR-B146"
and b146/hits.tsv. For the bim_ vol 6 item: availability check (no login), then for each of the 8 hits (ll.25671, 74562, 75081, 77385,
40469, 44535, 65889, 89881, plus Jephson 65973, 76999 if the budget allows) fetch the one page image once (IIIF or the item's page-image
route), crop the numeral block with `tools/iiif_lines.py --image` (paste the command), and answer per hit only: is it cipher numerals, is a
printed decipherment/interlinear gloss beside it, sender/recipient/date from the heading. One page per Sonnet call. No decoding, no
transcription of the numerals. A cipher block with no printed decipherment under a correspondent of a folder key: one ROOM flag line for the
lane. Commit crops under 3 MB with a manifest. NOTES "## THUR-V6", Remaining gaps / Escalation / Verdict, gaps_check.py. Report what was
found and where it was not found; do not classify novelty.
