# LANE-NEAR3 wave 1 (4 Oct 2026, written by LANE-NEAR3, account 2 / ytbiz, session_01Au8dSL1TXFoCk5P5opEMVv)

Lane brief: `.claude/briefs/runs/2026-10-04-acct3-lane-near3-run1.md`. Both targets are NEAR.md rows from LANE-READ2 (STATUS.md
"LANE READ2 handoff"). Intake gate, pasted by the lane at 01:1x UTC 4 Oct:
`hellen-frederick-1752: partial (line 1) -- edition/page or full-text-search citation found within 6 lines` exit 0;
`clair1161-avis-flandre-1688: partial (line 1) -- edition/page or full-text-search citation found within 6 lines` exit 0.

## Common to every job below
- Read `.claude/briefs/README.md` "Common tail" and follow it; last 20 lines of UPDATES.md; last 30 of ROOM.md.
- Start: `python3 tools/room.py --start` (if it cannot push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`);
  `date -u`; claim with `python3 tools/room.py "<JOB> (account 2 worker, for LANE-NEAR3)" 'claim: <target> <job>; box ends <HH:MM> UTC'`.
- Stop and push at the cap or the box, whichever first; before starting a unit that would cross 80% of either, stop. Never write a dollar
  figure for yourself: "cost: see the lane ledger". Never call AskUserQuestion. Never print or commit credentials or the DECODE account name.
- Rule 10 wording only (never new/first/unpublished/solved/cracked); "report what was found and where it was not found; do not classify novelty".
- **clair1161 jobs run in parallel (up to five at once): never edit its NOTES.md, NEAR.md row, key.tsv, ciphertext.tsv or reading.**
  Write your section to `ciphers/clair1161-avis-flandre-1688/reports/<JOB>.md` instead (the lane folds them into NOTES.md, refreshes
  gaps and NEAR.md); where a section below says "NOTES.md: section ...", read that as this file. Skip gaps_check for clair1161 jobs.
- hellen (NEAR3-HEL3): if the target stays `partial`, refresh "## Remaining gaps" / "## Escalation" at the end of NOTES.md and paste `python3 tools/gaps_check.py <target>`'s OK line.
- If your result bears on the target's NEAR.md row, update its Evidence and Last-touched cells in the same push.
- End: commit by explicit path, `python3 tools/file_shrink_guard.py <paths>`, `python3 tools/room.py --push <paths>`, confirm on origin/main,
  one done line for LANE-NEAR3 (account 2) with the numbers (target and control side by side), requests per host, subagent calls used.

## NEAR3-HEL3 -- hellen-frederick-1752: find a sheet carrying codes 1-800 of the Hellen key (Opus; cap USD 8; box 60 min)
Why: R4369 (BL Add MS 32276 f.44, "Hellen avec le Roy de Prusse", 1751) keys codes 801-1796 and reads R1953 above every control
(NOTES.md "READ2-HEL"); 374 of 846 R1953 tokens sit in codes 1-800 and are unread. R4370 (f.46) was tested as the first half and fails
(READ2-HEL2). IMG-DECODE1 looked at R4369, R4370, R4373, R4377, R4378, R4379 only.
Read: NOTES.md sections "IMG-DECODE1", "READ2-HEL", "READ2-HEL2", "Remaining gaps (READ2-HEL2)"; `images/decode/manifest.json`.
1. Login-free first: `python3 tools/decode_list.py --help`, then list every DECODE record whose shelfmark is BL Add MS 32276 (or whose
   sender/receiver names Hellen/Ellen) with its folio, date, type and sender. Write `key_search/add32276_records.tsv`.
2. One browser login (`NODE_PATH=$(npm root -g) node tools/decode_browser_login.js <id> <scratchpad dir> --guess-fullsize ...`, read its
   --help; one login for the whole job, 1.7 s between requests). Fetch RecordsView + page images for R4376 (f.56, 1754) and every Add MS
   32276 record before f.44 not yet looked at, plus R4371, R4372, R4375 if they exist. Images stay in your scratchpad (not public domain;
   never committed); sha1, size and URL go into `images/decode/manifest.json`.
3. Look at each sheet once (contact sheet; one vision call per few sheets, at most 6 vision calls): is it a code table with meanings, a
   tally sheet, blank? Header naming Hellen/Ellen/La Haye? Which code range? Table like IMG-DECODE1's.
4. If a sheet carries meanings for codes in 1-800 attributable to the Hellen line (header, or same hand/layout as R4369's), stop there and
   write the transcription brief's facts into NOTES.md (record, pages, code range, image URLs, native size) -- the transcription and the
   LR100 re-run are a separate job. If none does, say so, record what each sheet is, and name the next place to look (other BL volumes
   of the Deciphering Branch, e.g. the Add MS 32xxx series DECODE lists, or the 1740s Hellen records), with the request count.
NOTES.md: section "NEAR3-HEL3 (4 Oct 2026)". No transcription, no test, no grades in this job.

## NEAR3-C1RD -- clair1161-avis-flandre-1688: rule-7 fresh re-derivation (Sonnet; cap USD 3; box 30 min; disk only)
Why: CLAUDE.md rule 7; the reading changed in READ2-C1161B (key.tsv = gloss-repaired anneal key; C 97 S 675 M 152 U 15).
Read ONLY: this section, CLAUDE.md rules 4 and 7, `specs/clair1161-avis-flandre-1688.json`, the folder's `ciphertext.tsv`, `key.tsv`,
`decode.json` if present, and `python3 tools/decode_key.py --help`. Do NOT open NOTES.md, HYPOTHESES.md, `reading*` or `glossctl/` until
step 2 is written down.
1. Write `rederive/rederive_c1rd.py`: map each ciphertext token through key.tsv by the rules stated in the spec/key/decode.json alone;
   write `rederive/rederive_c1rd.txt` (one line per token, `?` for unkeyed).
2. `python3 tools/decode_key.py ciphers/clair1161-avis-flandre-1688 --check`; paste output.
3. Only now open `reading_tokens.tsv` and diff token by token: agreements, differences, each difference with its committed grade.
   Verdict PASS if every difference is on an M-graded token (or none), else SEND BACK with the list and the convention that caused it.
NOTES.md: append "## NEAR3-C1RD rule-7 re-derivation (4 Oct 2026)". Do not edit key.tsv or the reading.

## NEAR3-C1LOOSE -- clair1161: pre-registered looser gloss-seeded repair (Opus; cap USD 6; box 60 min; disk only)
Why: the strict all-agree rule fixed only 6 signs (READ2-C1161B step 2; c185R judge -1.128 real-gloss vs -1.177..-1.243 shuffled-gloss,
3 shuffles). Read NOTES.md "READ2-C1161B", `tx/PREREG_glossctl.md`, `glossctl/repair.py`. Tool shelf: `python3 tools/tool_shelf.py
"gloss-seeded key repair with a shuffled-gloss control"` -- name what it offers or why it does not fit.
1. Write `tx/PREREG_loose.md` and push it BEFORE any run: rule = a sign is fixed (grade C) to its majority aligned gloss letter when it has
   >= 3 aligned occurrences and the majority letter holds >= 60% of them (state exactly); same alignment, same re-anneal recipe
   (homophonic_anneal seed 1, restarts 32, fr16 order 3, 924-sign stream). Control: the identical procedure with the gloss letters
   shuffled within the gloss, **10 shuffles** (seeds 1-10). Pre-registered outcome: PASS when the real-gloss repair's c185R judge score
   (the leaf the gloss does not touch) beats the best of the 10 shuffled-gloss repairs AND beats the strict-rule repair (-1.128). Also
   report block-vs-gloss match, but it is not the gate (it is fit to the gloss by construction).
2. Run serially (one anneal at a time). Rows in `glossctl/loose.tsv`; keys `glossctl/loose_real_key.tsv`, `glossctl/loose_shufN_key.tsv`.
3. Do NOT replace `key.tsv` or the reading in this job, whatever the outcome; the pooled re-anneal job (later) decides. Write which signs
   moved and from what.
NOTES.md: section "NEAR3-C1LOOSE (4 Oct 2026)" with the table, target vs best control side by side, PASS/FAIL against the pre-registration.

## NEAR3-C1SPLIT -- clair1161: q/ls and the two S shapes, split test (Opus; cap USD 5; box 50 min; disk only, may look at crops)
Why: the passes split q/ls and two S shapes and they were merged by eye only (READ2-C1161 "Remaining gaps"). Read NOTES.md "READ2-C1161"
and "READ2-C1161B", `tx/labels_v2.md`, `tx/c185R_rec.tsv`, `tx/c186R_blk_rec.tsv`, `tx/c185R_passA.tsv`/`passB.tsv` (where the passes split).
1. Build the split streams in `split/` (never edit ciphertext.tsv): for each pair, a variant where the two shapes are separate symbols, using
   whichever pass (or crop look, at most 2 vision calls on the relevant crops) separates them. Write how each occurrence was assigned.
2. Write `split/PREREG_split.md` and push it BEFORE any run. Statistic: block-vs-gloss match of the c186R block (as in `glossctl/glossctl.py`)
   and c185R judge score, after the same anneal recipe as READ2-C1161B (seed 1, restarts 32, fr16 order 3). Control that can differ: a
   PLACEBO split -- split a sign of similar frequency at random into two symbols (5 placebo signs/seeds) -- because adding a symbol alone can
   raise fit. PASS for a split when its gloss match AND c185R judge beat the merged baseline AND the placebo p80 (state exactly).
3. Run serially; rows in `split/results.tsv`. Do not edit `ciphertext.tsv` or `key.tsv`; recommend merged or split per pair for the pooled job.
NOTES.md: section "NEAR3-C1SPLIT (4 Oct 2026)", numbers side by side.

## NEAR3-C1TX-<LEAF> -- clair1161: transcribe one more cipher leaf (Opus with Sonnet subagents; cap USD 7; box 60 min)
Leaves (one job each): **c186L** = IIIF f187 left, native region 100,50,3400,2000; **c187L** = f188 left, 100,1200,3250,4450;
**c187R** = f188 right, 3950,50,3150,4650; **c188L** = f189 left, 100,50,3150,4600 (NOTES.md "IMG-GALLICA1"; ark btv1b90010063).
Why: pooling the four untranscribed leaves of the same "Avis" (~100 lines) with c185R+c186R (924 signs) for a re-anneal.
Read NOTES.md "IMG-GALLICA1", "READ2-C1161"; TRANSCRIPTION.md in full; `tx/labels_v2.md` (the label set every pass uses);
`python3 tools/tool_shelf.py "transcribe a 16th-century French pen-sign symbol cipher from line crops"`.
Units (Usage 6, priced per subagent call): crop + 2 blind Sonnet passes + 1 reconciliation (yours) = 3 units.
1. Crop command, pasted BEFORE any subagent call: `python3 tools/iiif_lines.py --ark btv1b90010063 --canvas <f> --region <x,y,w,h> --out
   ciphers/clair1161-avis-flandre-1688/images --prefix <LEAF> --bottom-margin 75 --debug` (check the overlay by eye; re-cut if bands span
   two lines). Gallica: one request at a time, >= 2 s apart.
2. **Folder size: the folder is ~20 MB of a 30 MB limit and four leaves are being added in parallel.** Do NOT commit the `src_*` native
   region file (delete it from the folder after cropping; its URL stays in images/manifest.json); commit only your crops and the debug
   overlay, and if they exceed ~2 MB re-encode them (JPEG q75, same dimensions). `du -sh` the folder in your done line.
3. Two blind passes (Sonnet subagents; each sees only crop paths + `tx/labels_v2.md`; one call per pass for the leaf); then
   `python3 tools/reconcile_passes.py`; you settle disagreements from the crops (that is the reconciliation unit). New shapes not in
   labels_v2: give a provisional label `NEW1..`, list them with a crop reference, never force them into an existing label.
4. Write `tx/<LEAF>_passA.tsv`, `_passB.tsv`, `_rec.tsv` (same columns as `tx/c185R_rec.tsv`), err_2reader for the leaf. Do NOT edit
   `ciphertext.tsv`, `key.tsv` or `tx/stream_all.txt` (four jobs run in parallel; the pooled job merges). If err_2reader > 0.10 run
   `tools/lookalike_pass.py` once and write the residual as a sorter focus list, never a third full pass.
5. Decode your leaf under the current key.tsv for information only (`tx/<LEAF>_decode_info.txt`), ungraded, not a reading.
NOTES.md: section "NEAR3-C1TX-<LEAF> (4 Oct 2026)": route, requests per host, subagent calls, lines, signs, err_2reader, new shapes.
