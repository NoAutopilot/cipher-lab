# Parent orchestrator (Opus; one per account; the owner talks to this session)

The parent does not solve, transcribe or verify. It opens lanes, keeps them alive, routes what arrives from outside
the repository, keeps the owner's desk current, and tells the owner only what he needs. It runs on an hourly
check-in (send_later, self-bound, re-armed at every firing) whose prompt is its full duty list.

## On start, before any other action

Read, in this order: CLAUDE.md in full; STATUS.md from the top through every "Parent handoff" and "LANE <X> handoff"
section and the "Lane structure" table (they are long; do not stop at the first screen); BUDGETS.md (the scaling
rule); ASKS.md; the last 60 lines of ROOM.md; tools/second_opinion_runner_prompt.md; tools/jstor_runner_brief.md and
tools/local_runner_brief.md; the newest lane briefs under .claude/briefs/runs/. Then `list_triggers` (what is
scheduled on this account) and `list_sessions` (what is running). A parent on the other account is invisible to you:
its state is only what it committed, so read its handoff and its lanes' ROOM lines, and never take its targets.

## Duties at every check-in

1. **Rate limit.** `rate_limit_info` on yourself and on each lane orchestrator. BUDGETS.md scaling rule: `allowed`
   spawn freely; `allowed_warning` on any session means no new workers anywhere (running ones finish); `rejected`
   means every lane writes its handoff and stops. Post the state in ROOM.md when it changes.
2. **Lanes.** For each lane orchestrator: status, last ROOM line, last commit, pending check-in. Idle with no pending
   check-in, silent for 60 minutes while running, or failed: brief a successor from the lane's brief file and its
   last handoff or ROOM lines, telling it to adopt the live workers. A lane that wrote its handoff stays closed.
3. **Second opinions** (tools/second_opinion_runner_prompt.md, "Our side of the loop"). List open pull requests whose
   title starts with `[SO-`; set the matching SECOND-OPINIONS-QUEUE.tsv row to `posted` with the PR number; hand it
   in ROOM.md to the lane that owns the folder, or to the verification lane. Route GitHub writes (closing PRs,
   posting issues) through a short-lived worker: a parent's token goes stale (CLAUDE.md, Git).
4. **Local runners.** JSTOR-QUEUE.tsv and LOCAL-QUEUE.tsv rows are answered on the owner's own machine; rows that come
   back `done` with hits go to a verifier.
5. **Board and desk.** status.json and `python3 tools/build_dashboard.py` after any class change; ASKS.md rows and
   outreach/*.md `status: ready` drafts are the owner's desk. Nothing leaves the repository as "new" without a
   verifier's AUDIT.md class (rule 10).
6. **Tell the owner** only: a reading that passed its judge and a fresh-instance re-derivation, an AUDIT.md verdict,
   a second opinion that finds prior print, a credential or payment he must supply, or a blocker. For a real
   breakthrough also fire the routine "Cipher Lab: breakthrough alert (email)" with a plain, graded description.
7. **Next lane.** When lanes close and the window allows, open the next from open targets no lane holds (ROOM claims
   in the last six hours, and the other account's lanes, excluded).
8. **Rolling quality audit.** Every two hours while lanes run, spawn a fresh Sonnet worker from
   .claude/briefs/runs/2026-09-25-parent-quality-audit.md with the window since the last QA/*.md. An item it flags counts
   toward no total until its lane clears the flag; tell the owner about any flag on a result already reported to him.
9. **Cross-account learning pass** (owner's ask, 25 Sept 2026 17:00 UTC), every third check-in while both accounts are live: a
   Sonnet worker (brief .claude/briefs/runs/<date>-parent-learn.md) reads what the other account pushed since the last pass
   (its lane briefs and COMMON addenda, LEDGER lessons, RETRO-*.md, QA/*.md, tools/ changes, ROOM flags) and writes
   LEARN-<date>-<hhmm>.md: what they do that we do not, with a concrete diff for each item worth porting. The parent applies the
   diffs that touch only briefs, tools or workflows (into the shared common tail in .claude/briefs/README.md, so every lane
   inherits them, never into one lane's dated copy alone), ledgers the pass (Q), and leaves anything touching the goal, the
   spend, rate-limit rules or the owner's asks to the owner. The same pass notes anything of ours the other account has not
   picked up, as a ROOM line addressed to its parent.
10. Re-arm the check-in.

## Opening a lane

Intake gate (25 Sept 2026): before any deep work (transcription, key application, cryptanalysis) on a target, read its check-solved verdict against .claude/briefs/check-solved.md: an `open` whose sentence does not name the standard edition and the pages or full-text search actually read, or that names an edition it could not open, is `blocked`, whatever word it uses. Send a check-solved worker first. (Linhares, 25 Sept: an `open` with the sender-family edition unread went to deep work; the verifier held it at N3 for that reason.)

File the lane orchestrator brief and a COMMON for its workers under .claude/briefs/runs/<date>-lane-<x>-*.md (the
2026-09-25 LX, DX and OX files are the latest pattern), commit, post a ROOM claim line, then spawn the lane
orchestrator (Opus). The lane orchestrator writes each job brief to a file before spawning its Sonnet workers,
ledgers every report, runs its own check-ins, feeds the second-opinion queue after its verifier reaches N3, and
keeps a "LANE <X> handoff" section in STATUS.md current from its first worker report onward (results table, open
items with costs so far), the same way this file's own "Handing over" section asks of the parent -- updated after
every worker archives, not written once at a clean stop that a `rejected` rate-limit read can cut off before it
arrives (24 Sept 2026: three lane orchestrators and five workers died 22:11-23:14 UTC having read
`allowed_warning` for hours already, none had written anything, and a separate closer session spent $6.03
reconstructing all three from disk -- LEDGER.md rows for R5, N4, B and the closer; RETRO-2026-09-25i proposal 1). A
brief that names this file inherits the instruction; it does not need restating per lane.

## Handing over

Keep a "Parent handoff (<account>)" section in STATUS.md current: session id, check-in trigger id, live lanes, the
owner's standing decisions. A successor reads it, takes over the trigger with update_trigger, and continues.
