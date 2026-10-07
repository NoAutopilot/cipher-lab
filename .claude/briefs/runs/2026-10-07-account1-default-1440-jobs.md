# LANE DEFAULT-account-1-20261007-1440 jobs (account 1) -- 7 Oct 2026 14:4x UTC, lane orchestrator session_01FEtepdKvZ6iYUGCHy52qyE

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 14:40-00:40 UTC. Gate 0a: SESSION-SWEEP-account-1 row still `claimed` since
5 Oct 22:40 but its TSV is on disk; proceeding (as RUN8-12 and DEFAULT-account-1-20261007-0042 did), 0 exclusions from it.
Backlog a: VERIFY-BACKLOG regenerated 14:43 UTC: Birago off limits; eckert-1864 rows held by the live account-4 lane; nla-heinrich is N0
(Outreach gate 2 applies above N1 only); the rest are `counted` rows with priority none (count already decided). No verifier job taken.
Backlog b: `tools/next_steps.py --hot-only` (exit 0) runnable rows, filtered against ROOM claims < 6 h, 7 Oct briefs of live lanes and
folders already worked today. Excluded: Birago, Armstrong, Debosnys; eckert-1862/1864, fr7129, hessen-daenemark, costabili, fr15564
(account-4 DEFAULT-1335 live); lodewijk, fr16045, nevers-birago-fr3251, pro3055, manteuffel, wvo-hessen, decode-1411, fr3416, ceppo.
Every worker: one job, then stop. First check the named step is still undone (a later ROOM done line or NOTES section may have run it);
if it was, write one ROOM line saying so and stop.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim line
  with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE DEFAULT-account-1-20261007-1440". If --start
  fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections), HYPOTHESES.md and AUDIT.md section list first.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge, one retry after a pause at most). Report request counts per host. Prefer files already on disk.
- Rule 3 (matched control first; a control that cannot differ from the target on the statistic is a non-test), rule 4 grading, rule 7
  (`--check` scripts). Pre-register any new gate in a PREREG-<JOB>.md pushed before the score is computed. A reading change after AUDIT.md:
  say so in NOTES.md and flag in ROOM for a verifier.
- Rebase before writing shared files (status.json, PROGRESS.tsv, ROOM.md, HYPOTHESES.md, NEXT-STEPS.tsv); keep both facts on conflict.
  Commit only your own paths. Run `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with
  `python3 tools/room.py --push <paths>`.
- Partial targets: update "## Remaining gaps" / "## Escalation" (Verdict line) and pass `python3 tools/gaps_check.py <target>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the owner; never
  print credentials (test presence with `test -n`). Never call AskUserQuestion. Solver jobs: report what was found and where it was not
  found; do not classify novelty.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half done
  writes what was done and what remains into the folder's files. An Opus session floor is about 1.5; caps below assume it.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR ...` or the `--ark/--canvas` form, or the
  folder's existing crops); read line or strip crops, never a full page image; one page (or half page) per subagent call. Price ~1.5 per
  vision call, reconciliation one more unit.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE
  DEFAULT-account-1-20261007-1440", then a five-line final report.

## Wave 1 (spawned 14:47 UTC 7 Oct)
Intake gate 14:4x UTC (tools/intake_gate_check.py, each exit 0):
`fr16142-noailles-constantinople-1571: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`;
`colbert26-lathuillerie-1644: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`;
`fr16104-vivonne-spain-1572: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`;
`antt-linhares-chave: blocked (line 3) -- already terminal, nothing to gate`;
`fr2980-gramont: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`.

### DA1-NOX -- fr16142-noailles-constantinople-1571 c262 gloss + c510 look-alikes (solver, Opus; cap 5, box 70 min)
Verdict line (NOTES.md l.1667): "two blind word-level passes on c262 gloss L01-L13, ~$1.5; for c510 the next step is
tools/lookalike_pass.py on the named split glyphs, then the pre-registered score of witness/c510_recon.tsv, ~$2". Units: 2 blind gloss
passes (one subagent call each, on the existing native L01-L13 crops) + 1 reconciliation, then lookalike_pass.py on the named c510 split
glyphs (read its --help; its 2-of-3 residual is agreement, not accuracy) and the score of witness/c510_recon.tsv exactly as its existing
PREREG says (find it; if none exists, write one before scoring). Update NOTES.md, HYPOTHESES.md, gaps sections.

### DA1-COL -- colbert26-lathuillerie-1644 word-level gloss/code pairing (solver, Opus; cap 7, box 90 min)
Verdict line (NOTES.md l.1825): word-level pairing of gloss words to code groups on the native crops of c50, c3940, c47 to get one-code
spans for the open f.23 codes (the span-level positional test D22-COL26P gave 0 PASS of 26). Do that first unit only (c50/c3940/c47); the
canvas 20-21 pairing for 42, 11, 6 is the second unit, start it only if the first finished under 50% of cap and box. Use the folder's own
crops; register the pairing gate and a shuffle control that can differ on the pairing statistic before scoring; codes reaching C go to
the key only with that control passed (rule 3, the Szembek per-unit lesson).

### DA1-VIV -- fr16104-vivonne-spain-1572 ink 54 audit (verifier, Opus; cap 6, box 75 min)
Gap (NOTES.md l.1794): "ink 54 audit (depth re-check) - blocker: not-attempted; b2 + wrong-key PASS on the re-decode (PREREG-N7VIV54L);
next: verifier session". You are separate from every solver of ink 54 (N5-VIV54, N7-VIV54L). Re-derive the ink 54 reading with the
folder's decode script and `--check` (rule 7), check a sample of its tokens on the crops, recount H/C/S/M/I, then run
`tools/depth_check.py` per rule 4a and write "## AUDIT (ink 54 depth re-check, DA1-VIV)" in AUDIT.md: depth D0-D4 with the check used,
the D2+ content sentence if earned, any over-claim corrected. Do not re-run novelty searches beyond confirming the existing class still
stands; do not decode other inks. Update status.json depth fields for ink 54's row (rebase first) and the gap line.

### DA1-LIN -- antt-linhares-chave front-trim/join re-score by pt18 letter n-gram (solver, Opus; cap 3, box 50 min)
Verdict (NOTES.md l.978): "the front-trim and join enumeration re-scored by a pt18 letter n-gram (the word-unigram run, D22-LINTRIM 6 Oct
2026, passed its control and changed nothing), ~$2". Reuse D22-LINTRIM's enumeration and control; swap only the scorer to a pt18 letter
n-gram (tools/data pt18 corpus); pre-register the decision rule. Do not touch the two column counts (retired on this scan).

### DA1-GRA -- fr2980-gramont barred-z relabel (solver, Opus; cap 2, box 40 min)
Verdict tail (NOTES.md l.1494): "relabel the fr.3040 barred z (reader label zb) as its own code in n8gra2/n8gra3 and close the z/zb half
of the HYPOTHESES.md z A-vs-R entry, ~$0.5" (R12D-GRAZB2 found f.30 zb and fr.3040 barred z are different classes). Do the relabel,
re-run the affected scripts with --check, confirm key.tsv unchanged or say exactly what changed, close the HYPOTHESES.md entry half.

## Wave 1b (spawned 14:48 UTC 7 Oct)
Intake gate 14:48 UTC: `bowes-walsingham-1583: partial (line 1) -- edition/page or full-text-search citation found within 6 lines` exit 0.

### DA1-BOW -- bowes-walsingham-1583 known-keys rung: Walsingham-Wotton 1585 (solver, Opus; cap 3, box 50 min)
NOTES.md l.623 (the folder's "depends on nobody" action) and Escalation "[ ] known-keys" (l.587): try Tomokiyo's Walsingham-Wotton 1585
reconstruction (the elizabeth.htm images; use sources/cryptiana snapshots on disk first, fetch from Cryptiana only what is missing,
Wayback CDX if 404) against this letter's code layer (85, 0100 and the M codes), plus one TNA Discovery API search for the Wotton key /
Bowes cipher. A code reading from that key is H only if the key is a period key for this channel; a different-correspondent key is a
hypothesis to test with a control (wrong-key or shuffled-code null that can differ on the fit statistic), not a grade. Tick or retire the
known-keys rung with the result; credit Tomokiyo.

## Wave 2 (spawned 15:08 UTC 7 Oct)
Wave 1 all done by 15:02 (get_session: NOX 7.19, COL 5.78, VIV 3.14, LIN 1.71, GRA 1.91, BOW 1.08 = 20.81). Intake gate re-run 15:07:
colbert26 and bowes as in wave 1/1b (partial, citation found, exit 0).

### DA1-COL2 -- colbert26-lathuillerie-1644 second blind word-pairing pass + re-score (solver, Opus; cap 5, box 70 min)
Verdict (NOTES.md l.1881): "a second blind word-pairing pass on c50, c3940, c47 to measure the pairing's reader agreement and re-score
siblings/word_da1.py, ~$4.5". You are not DA1-COL's session and must not read DA1-COL's pairing files before your pass is written
(read only the crops, the gloss transcription and the code-group transcription). Units: 3 canvases x 1 blind pass each + 1 comparison.
Report per-canvas agreement with DA1-COL's pairing; re-score word_da1.py on your pass (unchanged statistic, control, gate). If any of the
six codes DA1-COL merged at C (16 se, 20 i, 46 ce, 67 leur, 81 me, 96 que) fails on your pass, say so and lower it to M in key_f23 with a
NOTES line; do not raise anything beyond what both passes support. Held-out units c54-56/c62-63 are a later job, not yours.

### DA1-BOWW -- bowes-walsingham-1583 Wayback CDX for CottonMSBowes.png (solver, Opus; cap 2.5, box 40 min)
NOTES.md l.624: one Wayback CDX lookup for Tomokiyo's glyph sheet CottonMSBowes.png (2 Oct attempt was a connection reset, not a 404).
CDX API then the `if_` capture (CLAUDE.md access playbook item 2); one retry after a pause at most. If found: save under
sources/cryptiana/ (unmodified snapshot, credit Tomokiyo), compare its sign alphabet with this letter's signs 02-28 and the f.290-293 key
as the known-keys rung describes, with a control that can differ (shuffled sign assignment), and tick or retire the rung. If not
captured: log the CDX result (URL, date, rows) in NOTES.md and mark the action done.
