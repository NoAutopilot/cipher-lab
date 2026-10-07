# LANE LANE-NZ-0914 jobs (account 4) -- 7 Oct 2026 09:5x UTC, lane orchestrator session_01AXbLoAzfBuAUxdjhfX6mTL

Lane brief: .claude/briefs/runs/2026-10-07-acct3-lanes-0914.md (default-lane.md over folders n-z, freshness check per row; cap 40, box
09:40-15:40 UTC 7 Oct). Freshness sweep (09:4x UTC, script greps of NOTES.md dated sections, ROOM.md since 6 Oct 18:00, briefs of the last
24 h): of 6 runnable n-z rows and ~35 blocked-row `parallel` actions, nearly all were already run on 6 Oct (RUN7-RUN15 lanes). Fresh steps:
wvo-hessen-1564 (verifier on realign/, WVO-REALIGN 7 Oct 01:47), na-suriname-map-1781 (0746 [ij]/s image check, 4.VEL s-codes vs
[sh-lig]), sachsstaatsarchiv-manteuffel-1712 (stale Verdict range; 0581-0592 off-stride screen). Stale rows corrected by the orchestrator:
scorpion-1991, siena-concistoro-2308, na-oldenbarnevelt-2442-1605. VERIFY-BACKLOG n-z: nla-heinrich audit2 not needed (N0; gate 2 applies
above N1 only, RUN12 6 Oct). Off limits: Birago, Armstrong, Debosnys; rah-juan-manuel (FRESH-0914 item 1). five_hour `allowed` at 09:5x.
Every worker: Opus 5.5, one job, then stop. Each job first checks that its named step is still undone; if so, correct the NOTES.md
next-step line, stop and report rather than inventing work.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-NZ-0914".
  If --start fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections), HYPOTHESES.md and AUDIT.md section list first.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge, one retry after a pause at most). Report request counts per host.
- Rule 3: any gate is pre-registered (a PREREG file committed and pushed before the scored run), with a matched control that can vary on
  the statistic tested; report both numbers. Rule 4 grades with counts. Rule 7: `tools/decode_key.py <folder> --check` (or the folder's
  own decode script --check) exit 0 before push if the reading or key changed. A reading change after AUDIT.md: say so in NOTES.md and
  flag in ROOM for a verifier.
- Rebase before writing shared files (status.json, PROGRESS.tsv, ROOM.md, HYPOTHESES.md, NOTES.md of a folder another job also touches);
  keep both facts on conflict. Run `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with
  `python3 tools/room.py --push <paths>`.
- Partial targets: update "## Remaining gaps" / "## Escalation" (Verdict line) and pass `python3 tools/gaps_check.py <target>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the
  owner; never print credentials (test presence with `test -n`). Never call AskUserQuestion. Report what was found and where it was not
  found; do not classify novelty (verifier jobs excepted, where the brief says).
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half
  done writes what was done and what remains into the folder's files. An Opus session floor is about 1.5; caps below assume it.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR` or the --ark/--canvas form); give
  subagents only crop paths, one page/leaf per call (or the stated crop batch), never a full-page image. Price: ~1.5 per Sonnet
  subagent pass, reconciliation = 1 unit. Thumbnail/contact-sheet triage by the worker's own eye at low resolution is allowed.
- Sorters: any sorter meant for the owner must PASS `python3 tools/sorter_preflight.py` and have 5+ random tiles opened against the line
  image; it is handed to the account-3 orchestrator (ROOM flag line) to publish. Never publish an artifact or edit ASKS.md yourself.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE LANE-NZ-0914",
  then a five-line final report.


## Wave 1 (spawned 09:5x UTC 7 Oct). Intake gate output (09:4x UTC) pasted per job.

### NZ-WVOV -- wvo-hessen-1564: verifier on WVO-REALIGN's realign/ + eye check of k28 (Opus; cap 3.5, box 60 min)
Intake: `wvo-hessen-1564: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
VERIFIER hat: you are not the solver (WVO-REALIGN, session_01GNSyk1ssQtFSZgtKSmkvpP) and do not protect its conclusions. Read NOTES.md
"## f.23 gloss re-aligned on the owner's settled signs (WVO-REALIGN ...)" and its Remaining gaps / Escalation. (1) Re-run the realign/
scripts from the committed inputs and confirm byte-identical outputs and the control numbers (AGREE 159/257; permutation p95 9;
derangement p95 5); confirm by git order that PREREG-WVO-REALIGN predates the scored run. (2) k28: it moved b -> e at C on this pass after an
earlier change; cut native crops of every k28 occurrence on f.23 (crop step mandatory and pasted) and read them by your own eye against the
glosses above: is C upheld, or should k28 be M (rule 4: two conflicting assignments are a data conflict, not a vote)? (3) If box remains,
the C03/C07 gloss letters eye check named in the Verdict (~1.2). Correct any over-claim in NOTES.md/key files; if a key value changes run
decode_key --check and flag the reading change in ROOM for AUDIT.md propagation (do not write a novelty class unless AUDIT.md already has
one for this item and the change must be carried into it). Update Verdict; gaps_check passes.

### NZ-SURIJ -- na-suriname-map-1781: [ij] on inv. 373 0746 and 4.VEL [s-loop]/[s-hook] vs [sh-lig] image comparison (Opus; cap 4, box 60 min)
Intake: `na-suriname-map-1781: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
Verdict cheapest-next (R15-SURV2, 6 Oct): "0746 `i j`/`s` check for [ij] (~1.5), and an image comparison of the 4.VEL [s-loop]/[s-hook]
codes with [sh-lig] before any alias". Read R15-SURALIAS, R15-SUR758 and R15-SURV2 first and copy their method. Step 1: per-token image check
of the 0746 reader `i j` and `s` tokens (service.archief.nl region fetch, one at a time; crop step mandatory), PREREG pushed before scoring,
the same control as R15-SUR758; does [ij] reach n >= 5 past its control? Step 2: crops of the 4.VEL map/legend [s-loop] and [s-hook]
tokens beside the 0730/0758 [sh-lig] crops; blind same/different look (your eye or one Sonnet call, crops only, with a known same-pair
and a known different-pair as in-call controls). Enter a value only if its gate passes; a map-reading change runs the decode script --check
and is flagged in ROOM for AUDIT.md propagation. Update Verdict; gaps_check passes.

### NZ-MANT -- sachsstaatsarchiv-manteuffel-1712: correct the stale "off-stride 0510-0580" Verdict and screen 694/08 0581-0592 (Opus; cap 2.5, box 45 min)
Intake: `sachsstaatsarchiv-manteuffel-1712: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
The Verdict's "cheapest next: off-stride 694/08 0510-0580 glossed frames for f.410's U codes" looks stale: n9mant/inventory_0504_0578.tsv
covers every frame 0504-0578, R7-MANTSCR eye-screened all 17 glossed frames for f.410's U codes, and 0518/0521/0526/0529/0530 have since been
transcribed. Check that against the folder (which glossed frames with U-code hits are still untranscribed?). Then screen the 694/08 frames
0581-0592 not yet seen (R13-MANTSCR named them; images/loc694-08-09/frames.tsv; archiv.sachsen.de one fetch at a time >= 1.5 s), by your own
eye at reduced size, with frame 0511 as an in-sheet positive control; record class / glossed / code range per frame. No transcription, no
key change. Rewrite the Verdict's cheapest-next to the true next step (with cost), or "parked" per rule 5 if every route left is
outside-blocked or only the low-yield 0001-0501 off-stride-10 screen remains (then name it with its cost as a [ ] step). gaps_check passes.
