# LANE LANE-RUN9-account-2 jobs (account 2) -- 6 Oct 2026 05:1x UTC, lane orchestrator session_01A1YMVHYC29a1P95MRiYJHg

Lane brief: .claude/briefs/default-lane.md (cap 60, box 05:13-15:13 UTC 6 Oct). WORK-QUEUE row 246: RUN9, same tier as RUN8 --
tools/next_steps.py runnable rows (S, M) and `parallel` actions, first RUN8's own named next steps for this split (STATUS.md "LANE
LANE-RUN8-account-2 handoff", "Open for the next i-r lane"). Folders i-r (account 1 a-h, account 4 s-z). VERIFY-BACKLOG.tsv has no
i-r row needing a verifier (05:14 UTC). Off limits: Birago (incl. nevers-birago-fr3251-1572), Armstrong, Debosnys; riksarkivet-r4282-1628.
Every worker: Opus 5.5 (Sonnet for the check-solved job), one job, then stop. Each job first checks that its named step is still undone
(a dated NOTES.md section may already have run it); if so, stop and report rather than inventing work. Gate 0a: SESSION-SWEEP-account-2
row still `claimed`, but its TSV (2026-10-05) is on disk; RUN7/RUN8 proceeded past it the same way.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-RUN9-account-2".
  If --start fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections), HYPOTHESES.md and AUDIT.md section list first.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge, one retry after a pause at most). Report request counts per host.
- Rule 3: any gate is pre-registered (a PREREG file committed and pushed before the scored run), with a matched control that can vary on
  the statistic tested; report both numbers. Rule 4 grades with counts. Rule 7: `tools/decode_key.py <folder> --check` (or the folder's
  own decode script --check) exit 0 before push if the reading or key changed. A reading change after AUDIT.md: say so in NOTES.md and
  flag in ROOM for a verifier.
- Rebase before writing shared files (status.json, PROGRESS.tsv, ROOM.md, HYPOTHESES.md); keep both facts on conflict. Run
  `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with `python3 tools/room.py --push <paths>`.
- Partial targets: update "## Remaining gaps" / "## Escalation" (Verdict line) and pass `python3 tools/gaps_check.py <target>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the
  owner; never print credentials (test presence with `test -n`). Never call AskUserQuestion. Report what was found and where it was not
  found; do not classify novelty.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half
  done writes what was done and what remains into the folder's files. An Opus session floor is about 1.5; caps below assume it.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR` or the --ark/--canvas form); give
  subagents only crop paths, one page/leaf per call, never a full-page image. Price: ~1.5 per Sonnet subagent pass, reconciliation = 1 unit.
- Sorters (lane rule since RUN7): any sorter meant for the owner must PASS `python3 tools/sorter_preflight.py` and have 5+ random tiles
  opened against the line image before it is handed on; it is handed to the account-3 orchestrator (ROOM flag line) to publish. Never
  publish an artifact or edit ASKS.md yourself.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE LANE-RUN9-account-2",
  then a five-line final report.


## Wave 1 (spawned 05:2x UTC 6 Oct). Intake gate output (05:15 UTC) pasted per job.

### R9-NLACS -- nla-heinrich-braunschweig-1519, check-solved on the Grein key sheets (Sonnet, cap 3, box 45 min)
Intake gate: `nla-heinrich-braunschweig-1519: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
RUN8 named step (R8-NLA2, NOTES.md tail): NLA BU L 1 Nr. 548 and 562 each carry a 19th-c. archivist's key table and deciphered word list
(Dr. Grein, 1858/1860). Follow .claude/briefs/check-solved.md (six sources + Premise check) with this specific question: does the archival
decipherment, and any printing of it (Schaumburg / Braunschweig historical-society journals, Zeitschrift des Historischen Vereins fuer
Niedersachsen, Braunschweigisches Jahrbuch, Havemann, Merkel on Heinrich d. J., Grein's own publications), make this target `found-solved`
under rule 5, or does it stay `open` with a period key in hand (then the decode is a `period`-key check, grade H, not cryptanalysis)?
Do not decode. Write the verdict and the search log (sources, queries, hits, date) into NOTES.md; change the status line only if the
check-solved brief's own rules call it; flag in ROOM what the next job should be (e.g. the ~4.5 transcription + key-apply check already
costed in NOTES.md). No vision work.

### R9-RAYSORT -- rayburn-2004, owner sign sorter (cap 3.5, box 60 min; no vision subagent)
Intake gate: `rayburn-2004: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
RUN8 named step: the two blind passes reconciled at 47.1% agreement (pass2/), over the 10% line, so per TRANSCRIPTION.md and CLAUDE.md
Usage 6 the next step is the owner's sign sorter, not test 3 and not a third machine pass. Build a sorter with tools/sign_sorter.py (read
its --help, sorter README conventions from a recent folder, e.g. ciphers/matignon-mayenne-1586/sorter/) from the image and line crops on
disk, with the pass-split signs in focus.tsv. Then `python3 tools/sorter_preflight.py` must PASS (paste output) and you open 5+ random
tiles against the line image and list them. Only if both pass: one ROOM flag "rayburn sorter preflight PASS, ready for the account-3
orchestrator to publish (db capability), path ..."; update NOTES.md Remaining gaps (test 3 now waiting-on the sorter). Never publish or
edit ASKS.md. If preflight fails after one fix attempt, write why in sorter/README.md and stop.

### R9-RJMSORT -- rah-juan-manuel-1521, hand on the RUN1-SEG letter-alphabet sorter (cap 3, box 50 min; no vision subagent)
Intake gate: `rah-juan-manuel-1521: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
NOTES.md Remaining gaps: "Letter alphabet held out -- sorter/index.html built (RUN1-SEG: 1,781 tiles, 79 piles, 3 named), not yet published
or sorted -- account 3 publishes it". The Verdict's "label-anchored f.199 pass" is a machine pass on an unsettled inventory, which the
sorter rule hands to the owner first. Job: check whether the sorter was ever handed on (grep ROOM.md/ASKS.md for rah-juan-manuel sorter);
if not, rebuild it with sorter/build.sh against the current tools/sign_sorter.py template (the template changed 6 Oct, commit 09b452df4),
run `python3 tools/sorter_preflight.py` (must PASS, paste output), open 5+ random tiles against the line images and list them. Only if both
pass: one ROOM flag for the account-3 orchestrator to publish (db capability), path given; NOTES.md gap 1 becomes waiting-on that handoff;
pass tools/gaps_check.py. If it fails after one fix attempt, write why in sorter/README.md and stop.

### R9-ROUS4 -- naf14913-rousseau-venice-1743, re-registered count-vector gate with a same-class planted known-answer (cap 2.5, box 45 min)
Intake gate: `naf14913-rousseau-venice-1743: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
RUN8 named step (R8-ROUS3, NOTES.md ~l.1600-1620, PREREG 0ec1ce048): the gate's known-answer licence was 0/3 (de/et/se) so 605=republique
and 739 were NON-INFORMATIVE. Next ~1: a re-registered run whose known-answer controls are of the same class as the tested candidates
(long content words, comparable occurrence counts on the slip-backed pairs), so the licence can actually be met. Commit and push a PREREG
before the scored run; the control must be able to fail differently from the target (rule 3). Report both numbers. Do not change key 501
(a separate verifier job, R9-ROUSV, is reviewing it this wave); no key change unless the registered gate licenses it; then
decode --check.

### R9-ROUSV -- naf14913-rousseau-venice-1743, verifier on the 501 grade flag (cap 2, box 40 min)
Intake gate: as R9-ROUS4. You are a verifier, not the solver; do not protect the solver's conclusions. R8-ROUS3 logged (M, unregistered)
that code 501, graded C = "et" from the slips, has a count vector (1,1,0,2) matching "un", not "et" (0,1,0,2). Check every slip-backed
occurrence of 501 against the slip images/transcriptions on disk and the plain context: is C "et" supported at each occurrence, or is it
a data conflict (rule 4: two witnesses disagree -> record each, grade M where unsupported)? Correct key/grades only as rule 4 allows, then
decode --check; carry any change into AUDIT.md and any SECOND-OPINIONS-QUEUE.tsv row for this target (rule 10 propagation). Write a short
dated section in AUDIT.md or NOTES.md. Do not run new cryptanalysis.

### R9-OBRED3 -- oldenbarnevelt-brederode-1605, full-size read of the remaining in-window DECODE keys (cap 3.5, box 60 min)
Intake gate: `oldenbarnevelt-brederode-1605: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
RUN8 named step (R8-OBRED2, decode_keys_palatine_hessian.tsv, commit 256bcaf78): 89 numeral-tagged in-window keys unread at 200 px; next
"full-size Marburg 4 d 1219 + 5 Munich records ~3". One DECODE browser login for the session (tools/decode_browser_login.js, CLAUDE.md
DECODE row; --guess-fullsize per A2-HDK), fetch full size for those records, and for each record read whether the key is a numeral
nomenclator whose correspondents, date and code range could fit the Oldenbarnevelt-Brederode 1605 cipher (compare with the target's own
code range and the frequency facts in NOTES.md). Crop before any vision call (one record per call). Fit test only if a key is shown to
fit by those criteria, with a control. Scrub the account name from any saved page. Update the TSV and NOTES.md. Report requests per host.
