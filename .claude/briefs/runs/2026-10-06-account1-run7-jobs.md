# LANE LANE-RUN7-account-1 jobs (account 1) -- 6 Oct 2026 01:5x UTC, lane orchestrator session_017EaoA9jsirqf8k8M7LCMwt

Lane brief: .claude/briefs/default-lane.md (cap 60, box 01:40-11:40 UTC 6 Oct). WORK-QUEUE row LANE-RUN7-account-1: next tier --
tools/next_steps.py runnable rows with cost_band M, ranked by PROGRESS.tsv closeness to a counted result, then depth pushes toward D2;
folders a-l only (account 2 takes m-z). VERIFY-BACKLOG.tsv has nothing actionable in a-l (Birago off limits; fr16142 depth already set
N0 D0 by D2-NOXA2). Off limits: Birago (incl. ceppo-nevers, nevers-birago), Armstrong, Debosnys, and the account-4 LANE-PRIV1 targets
(bne20211-ferdinand, destaing-gerard, bowes-walsingham, hamilton-1650). Every worker: Opus 5.5, one job, then stop. Each solver job
first checks that its named step is still undone (NEXT-STEPS.tsv lags the folders): if a dated NOTES.md section already ran it, take the
folder's own Verdict "cheapest next" instead if it fits this job's cap and box and is not a campaign; otherwise stop and report.
Caps below are sized per CLAUDE.md Usage 6: (subagent passes + 1 reconciliation) x ~1.5 per pass, plus ~1.5 Opus session floor.
Intake gate (tools/intake_gate_check.py, 6 Oct 01:5x UTC): fr16104-vivonne-spain-1572, baluze103-letellier-marca-1644,
hellen-frederick-1752, eckert-1864, colbert26-lathuillerie-1644, fr16142-noailles-constantinople-1571 all exit 0 ("edition/page or
full-text-search citation found within 6 lines").

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-RUN7-account-1".
  If --start fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections) and AUDIT.md section list before acting.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge). Report request counts per host.
- Rebase before writing shared files (status.json, PROGRESS.tsv, VERIFY-BACKLOG.tsv, SECOND-OPINIONS-QUEUE.tsv, JSTOR-QUEUE.tsv,
  ROOM.md); keep both facts on conflict. Run `python3 tools/file_shrink_guard.py <every file you touched>` before the final push;
  push with `python3 tools/room.py --push <paths>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the
  owner; never print credentials (test presence with `test -n`). Never call AskUserQuestion.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half
  done writes what was done and what remains into the folder's files.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE
  LANE-RUN7-account-1", then a five-line final report.

## Solver jobs (solver template .claude/briefs/solver.md; report what was found and where it was not found; do not classify novelty;
## rule 4 grades; rule 7 --check before push; pre-register any gate (PREREG file pushed before the answer is opened); a partial
## target keeps Remaining gaps / Escalation and passes `python3 tools/gaps_check.py <target>`; crops via tools/iiif_lines.py pasted
## before the first subagent call, never a full-page image to a subagent)

### R7A-VIV53 -- fr16104-vivonne-spain-1572, ink 53 gap tiles toward a D2 stretch (cap 3.5, box 60 min; ~1 Sonnet window pass + re-decode)
Context: AUDIT 2 (VER1-VIV, 5 Oct) held ink 53 at N3 D1: no repair-free stretch reaches the ~42-letter authentication distance (longest 20).
Job: the Remaining-gaps line "ink 53 residual label questions": extend tx/viv53L_windows.py to the 270 one-reader gap tiles (and, if the
cap allows, the 82 UNSETTLED split tiles) in tx/lookalike53L/*/focus.tsv, re-read them blind (one Sonnet call per batch of windows, never
a full page), apply only what the pre-registered 2-of-3 rule settles, re-decode with key.tsv (decode_key.py --check), and report the
longest repair-free stretch before/after and b2 + wrong-key gates as in PREREG-N7VIV53L. Do not change key.tsv. If a stretch now
exceeds ~42 letters, say so with the span and leave the depth call to a verifier (write the suggestion in NOTES.md; no depth edit).

### R7A-BAL103 -- baluze103-letellier-marca-1644, f.50r-v transcription + Tomokiyo 1644 table (cap 8, box 100 min; 2 pages x 2 blind passes + 2 reconciliations + key-table transcription ~ 7 passes)
Check-solved OPEN (D2-BAL103, 5 Oct). Leaf: Gallica btv1b9001389d (tools/gallica_folio.py for the canvas). Key: Tomokiyo, cryptiana
louisxiv0.htm (also DECODE R2742 doc 3821; credit Tomokiyo, key `published`); put it on disk as key.tsv with its source line. Calibrate
the table first on a few lines of one sibling with a period decipherment (f.171/f.189/f.200/f.230, DECODE R2743-R2746 or Gallica) if the
cap allows; otherwise say the calibration was not run. Then crops (tools/iiif_lines.py), two blind passes per page, reconcile
(tools/reconcile_passes.py), decode via decode.json + tools/decode_key.py --check, grade per token. Judge: tools/judge_plaintext.py with
an era-matched French corpus (fr17 if present; say which). One Gallica request at a time, >= 2 s apart; stop on 429.

### R7A-HEL53 -- hellen-frederick-1752, R1953 image check for codes 1-800 (cap 6, box 75 min)
Remaining gaps: "codes 1-800 of the Hellen key (374 R1953 tokens) ... next: image check of R1953 against DECODE's transcription where
decoded spans break (rule 2), ~$6". One DECODE browser login only (tools/decode_browser_login.js, try --guess-fullsize for the full image,
A2-HDK precedent); if the full image is refused, stop and log it. Crops of the lines where decoded spans break; one blind Sonnet read per
crop batch; tabulate DECODE transcription vs image per token (ciphertext.txt is never silently repaired: write a corrections TSV and a
re-decode, H/S/M/U before and after). Do not touch status.json depth fields (it is counted; a verifier re-checks depth later).

### R7A-ECK64 -- eckert-1864, Jan-Feb 1864 entries in the old vocabulary (cap 4, box 60 min)
Verdict: "Jan-Feb 1864 entries in the old vocabulary (read mssEC 67 or the No. 12 template, decode a sample), ~$3". Read the folder's
D2-ECK64S section (Spit/men data conflict, rule 4) first and keep it logged as a conflict. Images per the folder's own route (Huntington
CONTENTdm; documented CISOSEARCHALL form). Decode a sample, grade per token, rule 7 --check, phrase-check against OR where the folder's
scripts already do so.

### R7A-COL26 -- colbert26-lathuillerie-1644, anchor_split with canvases 54-56 as cleared units (cap 3, box 50 min)
Verdict: "re-run siblings/anchor_split.py with canvas 54, 55, 56 added as cleared units (pre-registered as a new script copy, statistic,
control B and gate unchanged), ~$0.3 ... then canvas 62-63 (La Haye, Jan-Feb 1648) numerals + gloss". Do the re-run (PREREG pushed first),
then canvas 62-63 only if cap and box allow (crops + 2 passes for the numerals; gloss read). Key changes only as the gate licenses.

### R7A-NOX262 -- fr16142-noailles-constantinople-1571, c262 gloss L09-L13 native cut and read (cap 2.5, box 40 min)
Verdict: "c262 gloss L09-L13 native cut and read, ~$0.5" (L13 "quon" vs gloss.tsv "quil"). Same tools/iiif_lines.py command as DEF1-NOXG
(--centres extended), one read, re-run the scripts listed in that section (RUN6-NOXREAD statistic and its controls), report old/new R vs
p99/max. Then, if within cap: "text-check the date-only Dupuy matches, ~$1". AUDIT.md is not edited by this job; if a number in AUDIT.md
or status.json depth_check moves, write a "Revision after AUDIT" note in NOTES.md and flag it in ROOM for a verifier (rule 10 propagation).

## Wave 2 (6 Oct 2026 02:1x UTC). Wave-1 lesson: three of six ran 1.2-1.8x cap; an Opus session costs ~1.5 before any work, and a
## "window pass" is many subagent calls, not one -- count calls, and stop before a call that would cross 80% of the cap.

### R7B-BAL103R -- baluze103-letellier-marca-1644, reconcile the 157 disagreement columns + re-decode (cap 5, box 60 min)
Verdict after R7A-BAL103: "reconcile the 157 disagreement columns from the crops and re-decode, ~$3". Settle each from the crops (batched,
<= 4 Sonnet calls, crops only; or your own reading of the crops as one priced unit), write the settled ciphertext (never silently repair:
keep the pass files and a settlement TSV), re-decode with key.tsv (decode_key.py --check), H/M/U before and after, re-run the fr17 judge
with its null. Then, only if >= 40% of cap remains: calibrate the table on a few lines of one sibling with a period decipherment
(f.171/f.189/f.200/f.230). Key changes only as a known-answer test on the sibling licenses (pre-registered).

### R7B-ECK64B -- eckert-1864, the rest of the Jan-Feb 1864 old-vocabulary entries (cap 5, box 70 min)
Verdict after R7A-ECK64: "pages 1-20 of mssEC 19, with key-no9.md extended from mssEC 67 pp.[11]-[15], [18], ~$4". Extend key-no9.md from
those mssEC 67 pages (H, period), decode as many entries as the cap allows in page order, decode_no9.py --check, OR comparison where the
folder already does it; log any rank/word conflict under rule 4 (Spit/men and Village conflicts stay logged). Huntington CONTENTdm per
CLAUDE.md (CISOSEARCHALL form), >= 1.5 s apart.

### R7B-ECK62 -- eckert-1862, carry 9991.571 book 1r, then the wrong-telegram test (cap 3.5, box 50 min)
Verdict: "carry 9991.571 book 1r into assign_free/readings_free, ~$0.5; then the wrong-telegram test on the 18 neither-book entries,
~$1.5". Pre-register the wrong-telegram test (statistic, control, gate) and push before running it.

### R7B-HUNT -- huntington-blathwayt-madrid-1728, descending-glyph census (cap 3.5, box 50 min)
Verdict: "descending-glyph census on BLA188 p4-p6 / BLA194 p1, ~$2". Read the A4-RFHUN section (23:4x 5 Oct) first. Crops via
tools/iiif_lines.py or the folder's own crop route; one subagent call per page at most.

### R7B-NOXV -- fr16142-noailles-constantinople-1571, verifier propagation of the R7A-NOX262 revision (cap 2.5, box 40 min)
You are a verifier, not the solver (never R7A-NOX262's session). R7A-NOX262 corrected gloss.tsv L09/L13 and re-ran RUN6-NOXREAD: R 0.3506
unchanged, but the nulls quoted in status.json depth_check moved (b p99 0.2496->0.2525; d p99/max 0.2581/0.2749 -> 0.2546/0.2721) and a
test0 difflib swing was found (NOTES.md "R7A-NOX262" and its "Revision after AUDIT" note). Check those numbers from the committed outputs
(re-run the scripts if cheap), then propagate per rule 10: a dated "## Revision after AUDIT (R7B-NOXV, 6 Oct 2026)" note in AUDIT.md (never
rewrite earlier audits), the status.json c262 row's depth_check string, and any SECOND-OPINIONS-QUEUE.tsv row for this target. N-class
and depth should not change (N0, D0); say so or say why not. `python3 tools/depth_check.py` after; paste its line for the row.

## Wave 3 (6 Oct 2026 02:2x UTC; last wave, lane ~46.5 of 60 after wave 2)

### R7C-BAL103K -- baluze103-letellier-marca-1644, the pre-registered sibling calibration of Tomokiyo's 1644 table (cap 4, box 50 min)
R7B-BAL103R pre-registered the calibration as the next step (read its NOTES.md section and PREREG). Run it as registered: a few lines of
one sibling with a period decipherment (f.171/f.189/f.200/f.230; DECODE R2743-R2746 or Gallica), crops + one blind pass (+ the
reconciliation only if cap allows), decode with key.tsv, agreement with the period decipherment vs the registered control. Key changes
only if the registered gate licenses them; then re-decode f.50 (--check) and re-run the fr17 judge. If the gate fails, log it and stop.

### R7C-ECK62C -- eckert-1862, conflict-pair table test (cap 3, box 45 min)
Verdict after R7B-ECK62: "conflict-pair table test ~$1.5". Pre-register (statistic, control, gate), push, then run; outputs and NOTES.md.
