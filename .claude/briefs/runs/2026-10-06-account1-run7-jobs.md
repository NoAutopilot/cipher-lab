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
