# LANE LANE-RUN11-account-4 jobs (account 4) -- 6 Oct 2026 13:4x UTC, lane orchestrator session_01XzCvfu53Hdqny4LQ8kgxgz

Lane brief: .claude/briefs/default-lane.md (cap 60, box 13:36-23:36 UTC 6 Oct). WORK-QUEUE row LANE-RUN11-account-4 (split s-z):
RUN10-account-4's "Open for the next s-z lane" 1-4 (STATUS.md) first, then tools/next_steps.py runnable rows and the `parallel` action of
blocked rows, cost band S and M, folders s-z only. VERIFY-BACKLOG.tsv (regenerated 13:38 UTC): no s-z row needing a verifier. Gate 0a: no
SESSION-SWEEP-account-4 row. Off limits: Birago, Armstrong, Debosnys; every target of the live DEFAULT-account-4-20261006-1235 lane
(in s-z: sp105-paget-1693, sp99-wotton-1622); anything in a private repository.
Every worker: one job, then stop. Each job first checks its named step is still undone (NEXT-STEPS.tsv lags the folders): if a dated NOTES.md
section already ran it, take the folder's own Verdict "cheapest next" instead if it fits this job's cap and box and is not a machine
transcription pass the TRANSCRIPTION.md / CLAUDE.md Usage 6 sorter rule hands to the owner; otherwise stop and report.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-RUN11-account-4".
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
  owner; never print credentials (test presence with `test -n`). Never call AskUserQuestion. Solver/lookup jobs: report what was found
  and where it was not found; do not classify novelty.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half
  done writes what was done and what remains into the folder's files. An Opus session floor is about 1.5; caps below assume it.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR` or the --ark/--canvas form); give
  subagents only crop paths, one page/leaf per call, never a full-page image. Price: ~1.5 per Sonnet subagent pass, reconciliation = 1 unit.
- Sorters: any sorter meant for the owner must PASS `python3 tools/sorter_preflight.py` and have 5+ random tiles opened against the line
  image before it is handed on; it is handed to the account-3 orchestrator (ROOM flag line) to publish. Never publish an artifact or edit
  ASKS.md yourself.
- No private-repository access in these sessions: if a step needs one, stop and say so in ROOM (the lane hands it to the standing session).
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE LANE-RUN11-account-4",
  then a five-line final report.


## Wave 1 (spawned 13:4x UTC 6 Oct). Intake gate output (13:40 UTC) pasted per job.

### R11-MANTPOOL2 -- sachsstaatsarchiv-manteuffel-1712, pooled multi-code aligner re-run with 0518/0521/0526 added (Opus; cap 2.5, box 50 min)
Intake gate: `sachsstaatsarchiv-manteuffel-1712: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
RUN10 "Open" item 1. R9-MANTPOOL's pooled multi-code-run aligner (pooled_mantp/, r9mant/) ran before R10-MANTSCR transcribed and gated
0526/0521/0518 (r10mantscr/). Re-run the same aligner, same PREREG gate shape (pre-register the new pooled frame set and the gate in a PREREG
file pushed before the scored run), with the three frames added; matched control = the same row/code shuffle as R9 (report S vs shuffle p95
and the known-answer check). Then R9-MANTPC's per-code shuffle test on any code whose verdict changes. Key changes only for codes that clear
the gate; grade per rule 4; decode --check exit 0. Reading changes after AUDIT.md -> NOTES.md note + ROOM flag for a verifier. Do not decide
the 0501 question (orchestrator decision; report what the pooled run says about 0501's codes). Units: disk-only, no vision.

### R11-ZESCORP -- zeschau-seebach-1841, era/register-matched 1840s diplomatic-French control corpus + fill-free pattern-rarity crib score (Opus; cap 5, box 90 min)
Intake gate: `zeschau-seebach-1841: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
RUN10 "Open" item 3 (see R10-ZESBASIN / R10-ZESCRIB in NOTES.md and HYPOTHESES.md). R10-ZESCRIB's control was a non-test because the control
text held no multi-unit crib. Step 1: build a small 1835-1850 diplomatic-French corpus (public-domain printed dispatches/notes on archive.org
or Gallica full text; fetch once, record sources in tools/data/ with a README, as V6-PTCORP did for pt18; the CLAUDE.md rule 3 era paragraph).
Step 2: a fill-free pattern-rarity crib score (score a crib placement by how rare its repeat pattern is under the target's design, no filler
search), with a control built from the new corpus enciphered under the target's design at the target's N, that DOES contain formula cribs.
Pre-register gate + control in a PREREG file pushed before any scored run. Run the target only if the control clears its gate; else log
CONTROL BELOW GATE in HYPOTHESES.md (non-test, not negative). Corpus build is a shared tool/data asset: add the corpus name where
tools/judge_plaintext.py / LANG_CORPORA documents corpora if it is general enough, with an offline test if you add code to tools/.

### R11-SIENAPOOL -- siena-concistoro-2308 no. 7, sign-set overlap pooling across fasc. 2 (Opus; cap 2, box 45 min)
Intake gate: `siena-concistoro-2308: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder's own "Next step (suggestion, not run)" (a), NOTES.md line ~867: disk-only check on the Bourdeau transcripts already on disk (cite;
MIT code / CC BY text) -- rank every other piece of fasc. 2 by sign-set overlap with no. 7 (Jaccard on sign inventory plus shared bigram
signs), with a shuffled-inventory null so the overlap ranking has a floor; for any piece above the null, list word-code candidates attested
there that also occur in no. 7 at low count. No new family run, no DECODE login (that is step (b), a later job). Report the ranked table and
whether any sibling clears the null; write "## R11-SIENAPOOL" in NOTES.md and update Remaining gaps / Escalation.

### R11-SCORPCYC -- scorpion-1991, cycling-homophonic family module + matched control (Opus; cap 4, box 75 min)
Intake gate: `scorpion-1991: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder's own named next (A2P4-SCORP3 Verdict): a cycling/sequential homophonic family (Pelling 2020 design: each plain letter's homophones
used in a fixed cyclic order) does not exist in tools/families/. Add it as a family module for tools/family_run.py (`--family
cycling_homophonic`), with `--help` text and an offline test in tools/tests/ (CLAUDE.md Usage 8; add it to SYSTEM.md in the same commit,
tools/system_map_check.py). Its solver may exploit the cycle constraint (e.g. homophone-cycle consistency as a hard constraint in the anneal).
Pre-register (HYPOTHESES.md row / PREREG file pushed first): control at N=70 K=53 (S1) and N=180 K=145-155 (S5 shape placeholder, as
A2P4-SCORP3), seeds 3, gate 0.6. Run the target S1 only if the N=70 control clears the gate; S5 has no settled transcription, never run it.
Report both numbers per run in HYPOTHESES.md. A control below gate = "untestable by this family at this N", not a negative.
