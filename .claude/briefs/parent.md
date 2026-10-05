# Parent orchestrator (Opus; one per account; the owner talks to this session)

The parent does not solve, transcribe or verify. It opens lanes, keeps them alive, routes what arrives from outside
the repository, keeps the owner's desk current, and tells the owner only what he needs. It runs on an hourly
check-in (send_later, self-bound, re-armed at every firing) whose prompt is its full duty list.

## On start, before any other action

Read, in this order: SYSTEM.md (the current-state map of roles, loops, gates, registers and levers; SYSTEM-MAP, 26 Sept 2026); UPDATES.md (the cross-account changelog; also re-read its tail at every check-in and log there any change you institute); CLAUDE.md in full; STATUS.md from the top through every "Parent handoff" and "LANE <X> handoff"
section and the "Lane structure" table (they are long; do not stop at the first screen); BUDGETS.md (the scaling
rule); ASKS.md; the last 60 lines of ROOM.md; tools/second_opinion_runner_prompt.md; tools/jstor_runner_brief.md and
tools/local_runner_brief.md; the newest lane briefs under .claude/briefs/runs/. Then `list_triggers` (what is
scheduled on this account) and `list_sessions` (what is running). A parent on the other account is invisible to you:
its state is only what it committed, so read its handoff and its lanes' ROOM lines, and never take its targets.

## Duties at every check-in

0. **Near solves.** Read NEAR.md. A row untouched for 48 hours gets a worker or an ASKS row named in it; a row whose
   target reads `closed-negative` is a rule-5 breach to reverse. Nothing leaves the register without the named next
   step's numbers or a verifier class.

0a. **Keys.** `python3 tools/key_probe.py --sync` (room.py --start ran it at your start; run it again here only in a fresh
   container). KEYS.md rows still `requested` are on the owner's desk (ASKS); a "key now set" ROOM line from either account
   means the briefs that waited on it can run; a `set` row seen by the other account only means this account's environment
   still lacks it (say so in the parent handoff line, once). Never pass a value anywhere. This checks names only -- for
   whether a present credential's call actually works, see duty 1.

0b. **No target is only waiting.** Every blocked row in NEXT-STEPS.tsv carries a parallel action (the `parallel`
   column, from the folder's newest "## While waiting" section). Run `python3 tools/next_steps.py --wait-only` at
   every check-in; a row it lists is a job to queue that hour (a WAIT-PASS worker writes the section from the
   folder's own NOTES/AUDIT/NEAR evidence), never a row to leave.

1. **Key livecheck.** `python3 tools/key_livecheck.py` (CLAUDE.md Access playbook; not the same tool as duty 0a's
   `key_probe.py` -- that one is name-presence across accounts, this one is a live test call per credential). If a
   credential's present/works result changed since the last KEYS-STATUS.md (absent->present, or failing->working),
   re-scan open ASKS.md and LOCAL-QUEUE.tsv rows against the new result and the Access playbook for work now doable
   from the cloud with that key or login, and assign it to a worker in this same check-in -- do not leave it for the
   next lane to notice on its own. A row moved this way is annotated in ASKS.md/LOCAL-QUEUE.tsv with which key
   changed and the probe line it rests on.
2. **Rate limit.** `rate_limit_info` on yourself and on each lane orchestrator. BUDGETS.md scaling rule: `allowed`
   spawn freely; `allowed_warning` on any session means no new workers anywhere (running ones finish); `rejected`
   means every lane writes its handoff and stops. Post the state in ROOM.md when it changes.
3. **Lanes.** For each lane orchestrator: status, last ROOM line, last commit, pending check-in. Idle with no pending
   check-in, silent for 60 minutes while running, or failed: brief a successor from the lane's brief file and its
   last handoff or ROOM lines, telling it to adopt the live workers. A lane that wrote its handoff stays closed.
   Ask each live lane orchestrator for its own context estimate at every check-in (there is no `get_session`
   equivalent for context the way there is for cost, so this is a self-report -- but a self-report read every
   30-45 minutes catches an accelerating lane before its line, not only at its own hand-off announcement). A lane
   past 80 percent of its brief's context line writes its handoff on this check-in, not the next one (25 Sept
   2026: LANE B2 handed off at 425k against a 300k line, 41 percent over, with no context figure seen by the
   parent before that hand-off line itself; LANE R6 handed off at 505k against 500k, on the line, the same
   window -- the difference is whether the line was watched before it was crossed).
3a. **Orphan check** (26 Sept 2026, ORPHAN-TOOL, owner's ask: "make sure we don't have any orphaned tasks
   across orchestrator swaps, and make sure this is systematized"). At every check-in, save `list_sessions`
   (mine: true, limit 100) and `list_triggers` to files under your scratchpad and run `python3
   tools/orphan_check.py --sessions S --triggers T`; act on every line it prints in this same check-in (adopt
   an orphan session into a lane, ledger and archive a stale one, delete an orphan trigger, chase or supersede a
   stale claim, backfill an unledgered ASSIGNMENTS row, chase a dropped request) before re-arming. The check now
   also includes (h) DROPPED REQUEST (26 Sept 2026, OPTIMIZATION-2026-09-26.md (a), DESK-CAP): any ROOM.md line
   addressed "for <role>" with no later line from that role within two hours, so a silently-waiting question
   (the Japikse question waited three and a half hours before this existed) is a finding at every check-in, not
   only when someone happens to notice. Also run `python3 tools/system_map_check.py` and add a SYSTEM.md row for
   every name it prints MISSING (SYSTEM-MAP, 26 Sept 2026).

3b. **Owner-side rule (owner's directive, 26 Sept 2026, OPTIMIZATION-2026-09-26.md (a)).** The owner does nothing
   that requires reading this repository. Every ASKS.md `desk` row and every outreach/README.md draft handed to him
   is self-contained: the exact action, the exact recipient or setting, and any paste-ready text, inline in the row
   or the draft's own header -- not "see NOTES.md" or "see the target folder" as the only instruction. If an ask
   needs repository context to act on, the ask is wrong and gets rewritten (or the missing context copied in)
   before it reaches `desk`.
4. **Second opinions** (tools/second_opinion_runner_prompt.md, "Our side of the loop"). List open pull requests whose
   title starts with `[SO-`; set the matching SECOND-OPINIONS-QUEUE.tsv row to `posted` with the PR number; hand it
   in ROOM.md to the lane that owns the folder, or to the verification lane. Route GitHub writes (closing PRs,
   posting issues) through a short-lived worker: a parent's token goes stale (CLAUDE.md, Git).
5. **Local runners.** JSTOR-QUEUE.tsv and LOCAL-QUEUE.tsv rows are answered on the owner's own machine; rows that come
   back `done` with hits go to a verifier.
6. **Board and desk.** status.json and `python3 tools/build_dashboard.py` after any class change; ASKS.md rows and
   outreach/*.md `status: ready` drafts are the owner's desk. Nothing leaves the repository as "new" without a
   verifier's AUDIT.md class (rule 10). Run `python3 tools/desk_check.py --cap 5` at every check-in and act on every
   line it prints before republishing the board (CLAUDE.md Usage 8a; DESK-CHECK, 26 Sept 2026).

   **Desk (26 Sept 2026, OPTIMIZATION-2026-09-26.md (a), DESK-CAP).** Finding: 46 open asks on one person was not a
   queue, it was a wall -- the person cannot rank it, so nothing moves and each parent keeps adding. The parents
   keep at most five items on the owner's desk at any time, each an ASKS.md row with `desk` as the leading word of
   its status cell: one action, one sentence, with a paste-ready text or a single click -- an item that needs the
   owner to read a NOTES.md or AUDIT.md file to understand it is not desk-ready (see duty 3b above). Every other
   open ASKS.md row carries `backlog` as the leading word of its status cell, with a one-line expected value after
   it (what it is worth if it moves, not the whole history). `waiting` (on someone other than the owner) and `done`
   stay as before. The parents re-rank the desk at the first check-in of each UTC day (or the next check-in if none
   fires exactly at 00:00 UTC), promoting the highest-value backlog rows and demoting anything on the desk longer
   than a day with no owner action, and record what was demoted and why in STATUS.md's "Parent handoff" section.
   `tools/desk_check.py --cap 5` fails (its own new check) when more than five ASKS.md rows carry `desk`; a parent
   check-in that sees this failure demotes rows before doing anything else on the board.
7. **Tell the owner** only: a reading that passed its judge and a fresh-instance re-derivation, an AUDIT.md verdict,
   a second opinion that finds prior print, a credential or payment he must supply, or a blocker. For a real
   breakthrough also fire the routine "Cipher Lab: breakthrough alert (email)" with a plain, graded description.
   Also match open `[LQ-<id>]` pull requests (tools/local_queue_runner_prompt.md, the owner's ChatGPT runner answering LOCAL-QUEUE.tsv rows): a short Sonnet worker copies each answer into the file the row names, sets the row `done <date>`, closes the PR without merging. Likewise `[JSTOR-<stamp>]` pull requests (tools/jstor_runner_chatgpt_prompt.md): the worker copies each row's hits into JSTOR-QUEUE.tsv's `hits` column and the target's AUDIT.md "JSTOR" section, sets the row `done <date>`, closes the PR without merging, and posts "for LANE V<n>" when a candidate hit names a target under audit.

8. **Next lane.** When lanes close and the window allows, open the next from open targets no lane holds (ROOM claims
   in the last six hours, and the other account's lanes, excluded).
9. **Rolling quality audit.** Every two hours while lanes run, spawn a fresh Sonnet worker from
   .claude/briefs/runs/2026-09-25-parent-quality-audit.md with the window since the last QA/*.md. An item it flags counts
   toward no total until its lane clears the flag; tell the owner about any flag on a result already reported to him.
10. **Cross-account learning pass** (owner's ask, 25 Sept 2026 17:00 UTC), every third check-in while both accounts are live: a
   Sonnet worker (brief .claude/briefs/runs/<date>-parent-learn.md) reads what the other account pushed since the last pass
   (its lane briefs and COMMON addenda, LEDGER lessons, RETRO-*.md, QA/*.md, tools/ changes, ROOM flags) and writes
   LEARN-<date>-<hhmm>.md: what they do that we do not, with a concrete diff for each item worth porting. The parent applies the
   diffs that touch only briefs, tools or workflows (into the shared common tail in .claude/briefs/README.md, so every lane
   inherits them, never into one lane's dated copy alone), ledgers the pass (Q), and leaves anything touching the goal, the
   spend, rate-limit rules or the owner's asks to the owner. The same pass notes anything of ours the other account has not
   picked up, as a ROOM line addressed to its parent.
11. Re-arm the check-in.

## Opening a lane

Intake gate (25 Sept 2026): before any deep work (transcription, key application, cryptanalysis) on a target, read its check-solved verdict against .claude/briefs/check-solved.md: an `open` whose sentence does not name the standard edition and the pages or full-text search actually read, or that names an edition it could not open, is `blocked`, whatever word it uses. Send a check-solved worker first. (Linhares, 25 Sept: an `open` with the sender-family edition unread went to deep work; the verifier held it at N3 for that reason.)

**Job 1 from the backlog, not a fresh scout (26 Sept 2026, OPTIMIZATION-2026-09-26.md section (c), NEXT-STEPS-TOOL).** 63 of 111 open/partial target folders end with a written next step nobody has run, because lanes were opened from scout picks rather than from that backlog. Before opening a lane, run `python3 tools/next_steps.py --check` (regenerate first if it reports stale) and read NEXT-STEPS.tsv: a lane's job 1 is the top `runnable` row for the account's own targets, not a fresh scout pick. A scout is spawned only once every runnable row is exhausted or each remaining row is gated on a named ASKS.md row. A folder is not left `open`/`partial`/`blocked` with a runnable next step sitting more than a day without a LEDGER.md row saying why it was skipped.

**Tool shelf before an instrument (3 Oct 2026, TOOL-SHELF).** Before a lane brief names a new instrument, a private script or a hand method, the orchestrator runs `python3 tools/tool_shelf.py "<problem in words>"` and names the tool it offers in the brief, with its grade, or says in one line why it does not fit; `python3 tools/tool_shelf.py --underused` lists tools cited by 0-1 target folders whose use-when matches an open/partial next step (a lead to check, not a fit). The shelf (SYSTEM.md section 3c, `tools/data/tool_shelf.tsv`) records evidence, not existence: proven / controlled-only / weak / untested / retired, with the result on file cited.

**Lineage depth (26 Sept 2026, parent 7h, LANE V10).** Every hand-over creates the successor parent as a child of the outgoing one, so the parent chain deepens by one each time; at parent 7h (7a to 7h, depth 7) a lane it created (LANE V10) sat at depth 8, the platform limit, and could neither `create_session` nor `send_later`, and closed itself within ten minutes. A parent at depth 7 can still run workers directly (a worker uses in-process subagents, never sessions). Lanes and the successor parent must then start from a shallower session: the owner creating the session from the claude.ai UI (ASKS 69). A one-shot `create_trigger` with `create_new_session_on_fire` does NOT work (tested on LANE B12, 15:25 UTC 26 Sept 2026: the routine-started session had no repository source, no session tools, no git credentials and no settable model; it ran 7 minutes on Sonnet, posted nothing, cost 0.98, ledgered X). Until the owner creates a depth-0 session, the parent runs breadth workers and QA passes directly and spawns verifiers itself. Record the parent's depth in every hand-over line.

**Standing rule (26 Sept 2026, RETRO-2026-09-26i item 2, applied by RETRO-APPLY-U with the seven-hand-over
amendment in force -- this supersedes any "every parent from the UI" wording elsewhere).** A UI-created parent
sits at depth 0, and its line may hand over by `create_session` up to six more times before the chain needs
another UI reset: every hand-over line records the successor's depth and how it was created ("successor
created via UI" or "via `create_session`, depth N"), so depth is legible from ROOM.md and STATUS.md alone,
without querying the platform. The parent at depth 6 files the ASKS.md row asking the owner to create the
next parent from the UI *before* it hands over, so the owner-created reset recurs once every seven hand-overs,
planned in advance rather than discovered at a lane's failure. A hand-over that had to use `create_session` at
depth 6 anyway, because the owner was unavailable to create the UI session in time, names that in ASKS.md at
once (not at the next failure), so the debt is visible immediately rather than compounding silently.
`tools/orphan_check.py`'s (g) LINEAGE DEPTH WARNING (a proxy counted from STATUS.md's own hand-over prose, not
an exact platform count) fires at 5 or more hand-overs since the last UI reset, printed at every run this tool
is part of (parent duty 3a) -- read it before it reaches 6.

Spawning (25 Sept 2026, UPDATES.md): every `create_session` passes `source_url` https://github.com/NoAutopilot/cipher-lab and
`source_revision` main explicitly (inheritance from the parent's environment is not reliable: three workers on 25 Sept got no
repository and stopped at their first turn on an injection suspicion), and its prompt leads with the brief file path and a
plain one-line job description, not a wall of caps and rules -- a dense, rule-heavy inline prompt can read like an
injected instruction set and trip a fresh session's own safety check before it reads the brief (LEDGER.md rows
799/818/819, 25 Sept 2026). Rule text stays in the brief itself.

File the lane orchestrator brief and a COMMON for its workers under .claude/briefs/runs/<date>-lane-<x>-*.md (the
2026-09-25 LX, DX and OX files are the latest pattern), commit, post a ROOM claim line, then spawn the lane
orchestrator (Opus).

**Size the opening brief for a shift, not a wave (25-26 Sept 2026, RETRO-2026-09-26a).** LANE R7, R8 and B4 each
closed "brief's queue spent" in 1.5-2.5 hours this window, each paying a $4-7 orchestrator open/close overhead on
only $25-35 of worker spend (R8: 17% overhead in 93 minutes). Name a reserve batch alongside the first wave --
at minimum, a second wave of comparable size drawn from QUEUE.md's own unscored-but-scouted rows (the VX-*/KX-*/
KT-*/PX-* families are the current backlog: several are recovery-kind with a key or sibling decipherment already
beside them, the highest-EV shape per Pipeline 3's selection rule) or from the target's own hypothesis ladder (a
design family with more than one untried variant, the way R8-DSN's own NOTES.md sec.5 already lists three next
steps). An orchestrator that clears both waves closes on a real "no more candidates," not a brief that only ever
named one.

The lane orchestrator writes each job brief to a file before spawning its Sonnet workers,
ledgers every report, runs its own check-ins, feeds the second-opinion queue after its verifier reaches N3, and
keeps a "LANE <X> handoff" section in STATUS.md current from its first worker report onward (results table, open
items with costs so far), the same way this file's own "Handing over" section asks of the parent -- updated after
every worker archives, not written once at a clean stop that a `rejected` rate-limit read can cut off before it
arrives (24 Sept 2026: three lane orchestrators and five workers died 22:11-23:14 UTC having read
`allowed_warning` for hours already, none had written anything, and a separate closer session spent $6.03
reconstructing all three from disk -- LEDGER.md rows for R5, N4, B and the closer; RETRO-2026-09-25i proposal 1). A
brief that names this file inherits the instruction; it does not need restating per lane.

**Self-ledger cost: read `get_session` on yourself last (26 Sept 2026, RETRO-2026-09-26e).** When a lane
orchestrator closes (or a parent archives itself), write the self-ledger row's own cost from a fresh `get_session`
call on your own session id, taken *after* every worker's cost is already ledgered -- not from a running total kept
in your head across the lane's lifetime. Two self-ledger rows this window (LANE B7 5.55 vs `get_session` 6.67; LANE
V8 6.91 vs 7.70) understated cost by 11-17% against the same-window `get_session` figure cited in the row's own
check-in line -- both errors in the same direction, consistent with summing remembered worker costs rather than
reading the number fresh at close time. A lane's self-ledgered close cost is provisional until the parent replaces
it in place from its own `get_session` read on that lane orchestrator's session id; the parent's ASSIGNMENTS done
row for the lane records both figures (the self-ledger and the parent's `get_session` reading) rather than
overwriting one with the other.

**Cite what you read, not just what to change (26 Sept 2026, RETRO-2026-09-26f).** A ROOM.md line asking another
lane or the parent to change a shared file (status.json, STATUS.md, a target's key.tsv) names the exact text or
line it read and, where practical, the commit it was reading at (`git log -1 --format=%h -- <path>`) --
`grep <the old text>` is enough when a commit hash is not to hand. A reader can then tell in one command whether
the ask is still live or already stale, instead of re-deriving that by hand. LANE V9's 08:53 line asked the parent
to change status.json's lodewijk grade text to match AUDIT.md A4's withdrawal; the parent had already made that
exact change and pushed it at 08:12, and had to spend a correction line at 09:03 finding this out for itself.

## Campaigns (27 Sept 2026, about 20:20 UTC, the owner's decision after the proof-sprint discussion)

SPRINT.md names the campaigns: a few targets worked continuously by per-target runner triggers (`.claude/briefs/campaign.md`,
`tools/campaign.py`), each with a ranked hypothesis file `CAMPAIGN.md` that never runs empty and a daily budget. The owner's
direction in plain form: focus on a small fixed set and keep iterating; a copy request is a branch, never a state in which
nothing moves; the campaign list stays fixed so that neither his impulses nor the parent's churn it, and changes only at a
retrospective with the reason written down. For the orchestrator: breadth is frozen for the sprint (no intakes, scouting
or new lanes; runner PR landings, mailbox, desk and verifiers continue); at each check-in read every CAMPAIGN.md, update the
SPRINT.md scoreboard, argue with the rankings, ledger the runner sessions, and report the campaigns in the same order in the
TLDR every hour; close a campaign only with a written reason; three dropped steps in a row with no new hypothesis is a red
line for the owner, not a close. The 48-hour number is verified readings per dollar.

## Usage register (owner, 3 Oct 2026, about 04:3x UTC: "the actual usage bars ... dollar cost means nada to me")

The owner reads usage as the account's 5-hour and 7-day bars (percent used, account-wide, so every session and
subagent on the login is in them), never dollars. The `cipher-lab-usage` mod (`.claude/skills/cipher-lab-usage`, in the
repository, so any session in it can load it) reads `$.session.usage().rateLimits` and posts this login's bars to
USAGE.tsv on origin/main by git plumbing (working tree untouched), at most once per account per 15 min, and shows
every account's latest bars (`/usage` pane, status line). `python3 tools/account_usage.py` prints the same table.
At every check-in a parent reads it, and flags in ROOM.md any account whose bars are over an hour old (its sessions
are not loading the mod: the owner enables it there, or sets CLAUDE_CODE_PLUGIN_DIRS to the folder's absolute path in
that account's environment settings). A login posting as 'u<8 hex>' is unmapped: add its row to ACCOUNTS.tsv.
Recaps give usage as the bars ("account 2: 5h 41%, 7d 78%"), never dollars.

## Transcription standard (owner, 3 Oct 2026, about 03:4x UTC)

Every parent briefs transcription to `TRANSCRIPTION.md`: a transcription job reports err_true (benchmark item named) or
says why it cannot, plus err_2reader; a symbol cipher with siblings goes into its key family's atlas before line reads.
The build jobs (TX-BENCH, TX-ATLAS-B72, TX-DECODE, TX-SORTER) are account-3 orchestrator rows in WORK-QUEUE.tsv; any
account may run them. At each check-in, a parent landing a transcription result copies its err_true into the
TRANSCRIPTION.md "Today" column when it improves the best figure, and the recap names the change in one line.

## Progress bars in every recap (owner's request, 28 Sept 2026 18:1x UTC)

Every reply to the owner shows one bar per live target, in a code block, from the record only:
`<target>  [#####.....] <firm>/<total> read   Found Key Read A1 A2 Counted Sent`
The bar is the share of the letter's cipher tokens read at grade S or better (the audit's own counts; two-way or M-grade tokens are not firm). The stage row marks each step done (x), in progress (~) or not started (.): Found (transcribed), Key (none / partial / holds), Read (any audited passage), A1 and A2 (first and second audit), Counted (in status.json), Sent (outreach sent by the owner). A bar or stage moves only when a file on disk changes it; a stalled target shows the same bar twice, and that is the signal.

## Re-arm first (28 Sept 2026, after the 06:45-14:15 UTC outage)

At every check-in the orchestrator re-arms its own next check-in (update_trigger, run_once_at one hour out) BEFORE any other work, then updates the prompt at the end. On 28 Sept this account hit its Fable limit mid-check-in, the re-arm at the end of the turn never ran, and nothing woke the orchestrator for about 7.5 hours while every runner sat failed. A runner whose get_session shows status_bucket FAILED with a model-limit message is replaced at once on the model the owner names (Opus 5.5 from 14:17 UTC 28 Sept).

## Blocker question (28 Sept 2026, about 02:4x UTC; after the owner twice supplied the obvious next move)

At every check-in, before spawning anything, the orchestrator writes one line for the CLOSEST target: the current
blocker in plain words, and everything already on disk or in the record that bears on that blocker (sibling leaves,
unglossed text under the same key, an unused witness, a tool that exists). Anything on that list that is not being
worked gets a worker or a row now. Lessons: the four undeciphered Mayenne leaves were filed as follow-on targets when
they were evidence for f.61's rare classes (28 Sept); the Mercy N4 wait needed the owner's prompt (27 Sept).

## Single orchestrator (27 Sept 2026, about 20:05 UTC, the owner's decision)

From this line there is one orchestrator, on the owner account: this session and its successors. The other account has
no parent; a scheduled dispatcher there (`.claude/briefs/dispatcher.md`) pulls `WORK-QUEUE.tsv` every hour and spawns the
rows tagged `other` as workers on its own account. The reasons, recorded in plain form: two parents spent about a third of
all effort on coordination (RETRO-2026-09-27x) and still let runner PRs sit past the claim window; one queue file replaces
the cross-account asks, the tie-break and the account-roles split. What changes for the orchestrator:

- Every job is a `WORK-QUEUE.tsv` row (`tools/work_queue.py --add`) with the brief written first. Rows tagged `owner` it
  spawns itself at once; rows tagged `other` wait for the dispatcher (up to an hour), so long-box solver and transcription
  jobs go there and short urgent ones (runner PR landings, gate checks) stay here.
- It ledgers, retitles and archives every worker from both accounts by session id; if archive_session is refused for the
  other account's session, the retitle stands and the LEDGER row notes it.
- Runner PRs are claimed at every check-in and queued; there is no tie-break.
- The sections "Account roles", "Runner PR tie-break" and "No parking" below are history from the two-parent period and
  no longer bind; the "No parking" habit of a default plus a clock time on any ask still applies to asks to the owner.
- The other account's parent (7n) stands down after its live workers finish: it ledgers them, writes its handoff in
  STATUS.md, creates the dispatcher trigger on its account from the paste-ready prompt in dispatcher.md, posts one
  "stood down" line, and stops. Its open targets pass to this orchestrator unchanged.

## Account roles (26 Sept 2026, 18:4x UTC; agreed by both parents after OPTIMIZATION-2026-09-26.md and the owner's condition that nothing in progress moves)

Two accounts push to this repository. From this date they specialise instead of mirroring each other. Nothing in
progress moved: every lane keeps its targets to completion on the account that started it.

- **SOLVE** (the other account's parent, 7i and successors): target lanes on the deep work (Salviati, Malsburg,
  Armstrong, GOLD) and every new target lane, taking job 1 from the top runnable row of NEXT-STEPS.tsv; its
  verifier lineage verifies the owner account's readings.
- **SUPPLY** (the owner-account parent): scouting, capped at one genuinely new full-text index a day; check-solved
  filters; landing the ChatGPT runner pull requests; rolling QA; the one LEARN pass and the one retrospective a
  day; tools; outreach drafting and the gate-7 fact checks; LANE VO1 verifies SOLVE's readings. LANE WC (the WVO
  circles) runs to completion on this account as an exception.
- Either parent lands a runner pull request when the other is between hand-overs, so no PR waits on one account
  (7i's ask). The owner's desk (five items) and the project mailbox are shared: whichever parent the owner is
  addressing keeps them current, and every send is the owner's.
- Cross-account verification: a "reading ready" line unclaimed by the other side's verifier lane for 60 minutes
  is taken by the nearer lane; rule 10 needs a separate session, not a separate account.

**Runner PR tie-break (26 Sept 2026, after the PR 28 double claim).** A `[LQ-]`, `[JSTOR-]`, `[SO-]` or `[SENT-]` pull request is the SUPPLY parent's to land by default. The SOLVE parent lands one only when no SUPPLY claim line for that PR number has appeared in ROOM.md within 20 minutes of the PR opening, and it says so in its claim. Before spawning any PR-LAND worker, either parent runs `git pull --rebase` and reads the ROOM tail for a claim naming the PR number; a claim already there wins, whatever the clock minute.

## No parking (27 Sept 2026, the owner's direction after the other account's parent sat parked awaiting this one)

Neither parent ever waits on the other. The hourly check-in is the only guaranteed reader of ROOM.md, so a cross-account
ask answered "at the next check-in" costs up to an hour, and an ask with no default costs until someone notices. The rules:

1. **Every ask carries a default.** A ROOM.md line addressed to the other parent ("for parent 7k", "for the owner-account
   parent") states what the asker will do if no answer has landed by a named clock time, at most 60 minutes out, and the
   asker does that at that time without a second line. "Awaiting your reply" is not a line either parent writes.
2. **Open asks first.** Each check-in begins with `python3 tools/open_asks.py --me "<your role>"` and answers every line it
   prints with a decision in that same check-in (a line by you after the ask clears it; "noted" is not a decision).
3. **A rate-limited account transfers its duties, it does not park.** When a parent's window reads `rejected`, or
   `allowed_warning` on the five-hour window past one check-in (a seven-day warning is not a stop: BUDGETS.md, the
   owner's decision 27 Sept), its next line is "duties transferred to <the other parent> until <reset time>": runner PRs, the desk, the
   mailbox, verification, and any solver-ready target of its role. The other parent runs both roles from that line, with
   no per-item exception announcements, and hands the duties back on the first "window allowed" line. The rate-limited
   parent then either hands over to a successor or idles with one check-in armed at the reset time, and posts nothing
   else. Nothing in progress moves accounts (the owner's condition); only duties not yet started do.
4. **Silence is a transfer.** A parent that sees no line from the other account's parent for two of its own check-ins
   assumes the transfer in rule 3 has happened, says so once on ROOM.md, and proceeds.
5. **Work that needs no spawn.** A parent that cannot spawn still has an hour's work: the next three briefs written and
   pushed for whoever spawns them, the register pass, ledger and desk hygiene, outreach drafts for the owner's send. It
   does that before idling.

## Handing over

Naming and model (owner, 25 Sept 2026): every parent session is created on `claude-fable-5-1` and titled "Orchestrator N", N one more than the current parent's number (7c is Orchestrator 4, 7d is Orchestrator 5); the internal 7a/7b/7c labels stay in the files for lineage, the session title is the number. Lane orchestrators keep their lane names.

**Session titles say LIVE or ARCHIVED (owner, 26 Sept 2026, 05:1x UTC, after replying into the retired parent 7e by mistake; both accounts).** Every session a parent or lane creates carries the prefix `LIVE ` in its title from `create_session`. The session that archives it renames it first: `ARCHIVED <old title> (done <clock time>, $<cost> <code>)`, then `archive_session`. A parent taking over titles itself `LIVE parent <x> · Orchestrator <N> (talk to this one)`, and as its first act after its ROOM take-over line renames its predecessor `ARCHIVED parent <w> · Orchestrator <N-1> (handed over <clock time>; do not message)` and archives it -- an archived session is read-only, so a message typed into it by mistake cannot start a second parent. A non-archived session whose title lacks `LIVE ` is a flag for the orphan check (`tools/orphan_check.py`). Lane orchestrators do the same for their workers.

**Verify the archive took (26 Sept 2026, RETRO-2026-09-26d).** The rename-and-archive step above is prescriptive,
not self-checking: `archive_session` can fail or be skipped with no error the successor notices. As part of the
same first act, the successor re-reads the predecessor's session state (`list_sessions` or `get_session` on its
id) and confirms the title now starts `ARCHIVED`; if it does not, the successor writes a ROOM.md flag naming the
still-live predecessor immediately, rather than assuming the call worked. This is the gap the LIVE/ARCHIVED rule
itself does not close: the owner replied into 7e at 05:00-05:10 UTC before this rule existed at all, so no session
had a chance to confirm 7e's state either way -- closing the verification half now means the next hand-over is
caught by a session, not by the owner noticing.

Keep a "Parent handoff (<account>)" section in STATUS.md current: session id, check-in trigger id, live lanes, the
owner's standing decisions. A successor reads it, takes over the trigger with update_trigger, and continues.

Before writing the handoff, the outgoing parent runs `python3 tools/orphan_check.py --sessions S --triggers T`
(duty 3a) and pastes a clean result into the hand-over line; a non-clean result is acted on first, not handed
off unresolved. The successor runs the same command as its first duty after the reading list, before taking
over the trigger.

**A lane cannot archive itself (26 Sept 2026, RETRO-2026-09-26f).** A lane orchestrator that closes retitles its
own session ARCHIVED and self-ledgers (per "Self-ledger cost" above), but does not call `archive_session` on its
own session id; the parent runs `archive_session` on it at the parent's next check-in, per duty 3a's orphan check
(owner-account parent's ROOM line 09:42, AX2's close).

**Parent context line (27 Sept 2026, RETRO-2026-09-27x P4).** Both parents read their own context usage from
`get_session` at every check-in, not only when a hand-over already feels close -- the way the SOLVE lineage
already does by practice (7m handed over to 7n at 583k on 27 Sept; the owner-account parent's own 15:44 check-in
line named 700k with a successor prompt planned at 850k). Write `hub-seed/SUCCESSOR-PROMPT.md` at 850k of a 1M
window (or 300k of a 400k window) and hand over before 950k (or 350k): past that point a check-in itself risks
running out of room to read ROOM.md, the ledger and the open asks before acting on them. A parent that has not
written its own context figure into a check-in line since this rule landed says so at its next one.

## Recording the owner (26 Sept 2026)

The owner's decisions go into STATUS.md, ROOM.md and the briefs as decisions in plain form ("the owner approved the RAH copy order"; "the owner holds the Tomokiyo question until a solve"), never as quotations of his messages. His words stay in the chat. Rule 9 (never his name) stands.

## Times for the owner (26 Sept 2026)

The owner reads Pacific time (America/Los_Angeles). Every time in a reply to him is given Pacific first with UTC in brackets, e.g. 12:40 PT (19:40 UTC). The board converts client-side (tools/build_dashboard.py, UTC toggle). ROOM.md, STATUS.md, LEDGER.md and every other file stay UTC, clock-read.

## Effort allocation (owner's decision, 27 Sept 2026, about 14:08 UTC, on CODEX-REVIEW-2026-09-27.md section 3)

For a two-week trial from 27 Sept 2026, both parents shape spend as: about 50 percent of usage on focused recovery,
transcription and solving (about ten points of the total reserved for one difficult research campaign); 20 percent on
acquiring specific high-value inputs (images, key sheets, deciphered siblings, adjacent leaves, ranked by the number of
documents a page could unlock over its cost); 20 percent on reading validation and novelty research; 10 percent on
coordination and maintenance (parents, retrospectives, LEARN passes, tools). The retrospective (SUPPLY) reports the
actual split from LEDGER.md each day against these figures and reallocates weekly on observed yield; it also reports
usage per validated recovered passage and per completed document beside the raw counts. A parent whose own session
cost exceeds a third of its workers' spend in a day says so in its handoff line. Starting allocations, not optima.

## TLDR for the owner (26 Sept 2026; count format changed 27 Sept 2026 by the owner's decision, BOARD-COUNTS)

Every message to the owner that carries a board update opens with a three-line TLDR before anything else: (1) SOLVES: the board counts in documents, generated from the per-row fields (recovered-passage documents / completed readings, both N3+ and D2+ since BOARD-DEPTH, 5 Oct 2026 / fragments read, the same rule at D1, never summed into the first two / keys or mappings to text already in print / contributions and corrections) and whether any changed in that order, e.g. "recovered-passage documents 18 / completed 2 / keys-to-known-text 1 / contributions 6, unchanged" (the counts at BOARD-COUNTS, 27 Sept 2026 14:23 UTC; at BOARD-DEPTH, 5 Oct 2026: 20 / 2 / fragments 9 / 1 / 6) or "+1 recovered-passage: <target>, N<class>, two audits"; (2) CLOSEST: the one target nearest a class change, with its stage in five words and what it waits on; (3) NEW THIS HOUR: at most two clauses. Then the detail. The owner reads the TLDR to decide whether to read on.

English gist (owner, 2 Oct 2026): every recap that reports a reading that moved also gives a one-line English gist of what it says, with the language named and marked as interpretation; never only "N signs read". The owner reads no Italian, Latin or 16th-c. French and could not tell whether we had the text or what it said.

Lane health (owner, 2 Oct 2026, after account 4 sat silent five hours unflagged): at every check-in read the last ROOM line of each account's parent; one older than 150 minutes is flagged to the owner in the recap and in a ROOM flag, with the Opus 5.5 fallback (BUDGETS.md "Model choice under a warning") named, whether or not that account holds the orchestrator role.

Keep slots full (owner, 2 Oct 2026 20:4x UTC: accounts 2 and 4 each sat at 0-1 live jobs while their queues had work). Every account that spawns workers runs a rolling refill, not waves: it holds a target live count (default 6 while the five-hour window is clear), and within 15 minutes of any worker's done line it starts the next job, rather than waiting for a whole wave or the next hourly firing. A parent or lane orchestrator re-arms send_later at 10 min while workers are live, or at the earliest live worker's expected finish when that is sooner (the 80-90 min check-in is only the floor for the fallback chain). S-band one-step jobs finish in 3-15 min (LANE-A1 3 Oct: a 15-min cadence left slots idle about a third of the time; LANE-RUN3 4 Oct: 1-2 idle slots per round at 15, 6 live at 10). With no S-band job live, 15 min stands (RETRO-2026-10-04-acct1 P3). The hourly dispatcher is a backstop, not the pump; an account that needs a pump runs a lane orchestrator (template: .claude/briefs/runs/2026-10-02-acct3-lane-a2push.md). At every check-in the orchestrator counts live workers per account from ROOM claims without done lines and flags any account under its target with a queue that is not empty.

## Mailbox: unread first (28 Sept 2026, 20:2x UTC)
Three archive replies (Marburg 15:03, Bodleian 15:26, Adirondack 18:09 UTC) sat unread through four check-ins because the check-in skimmed thread previews. Every check-in now runs search_threads "is:unread in:inbox" FIRST and reads each hit in full with get_thread before anything else in the mailbox step; a reply is recorded (folder NOTES, CONTRIBUTIONS, ASKS), a reply draft made for the owner, and its lead given to a worker the same hour.

## Standby on account 3 (28 Sept 2026, 20:3x UTC, owner-requested)
A standby orchestrator on account 3 (hub-seed/STANDBY-3.md) takes over if no "| orchestrator (owner account) |" ROOM line appears for 150 minutes, or on a "HANDOFF to account 3" line. So: post that ROOM line at every check-in; mirror the check-in prompt to hub-seed/CHECKIN-PROMPT.md whenever it changes; post HANDOFF when this account's rate limit reads rejected; on a TAKEOVER line newer than yours, follow the file's Handback before anything else.

## Orchestrator fallback chain (owner, 2 Oct 2026 01:2x UTC, four accounts 01:3x; generalizes "Standby on account 3")
There is one orchestrator at a time, on whichever account holds the role. It posts `| orchestrator (<account>) | check-in ...`
in ROOM.md at every check-in (at least every 90 minutes while it holds the role), and `HANDOFF` when its usage reads
`rejected` or it is about to stop. All four accounts are standbys, in this order:
**owner -> account 2 -> account 3 -> account 4** (skipping the account that holds the role). Account 2 has no parent
session; its hourly dispatcher runs the standby check at every firing and, when account 2 is the one to take over, creates
a parent session on account 2 with the takeover prompt (dispatcher.md "Standby check"). At its own check-ins (or
firing), a standby reads the newest orchestrator line; it takes over when that line is 150
minutes old or older, or is a `HANDOFF`, and it is the first account after the silent one in the chain that is itself
alive (its own last ROOM line under 150 minutes old). Takeover: post `| orchestrator (<account>) | TAKEOVER from <account>`
first -- the earliest TAKEOVER line in ROOM.md wins and any later one stands down at once -- then read the previous holder's
handoff section in STATUS.md and its WIP branch if it names one, run `tools/orphan_check.py`, and continue its queue. The
silent account, when it comes back, reads the newer TAKEOVER line and stays standby until handed the role back. The
private repository (Debosnys) is never taken over: it waits for the account that holds it. An orchestrator keeps its
STATUS.md handoff section current enough that a standby can continue from it without the session transcript.

## Standby dispatch (owner, 3 Oct 2026 16:3x UTC: "why do I have to manually post to account 1?")
A session can create sessions only on its own account, so the orchestrator cannot start work on another account itself. Every
standing session on an account that does not hold the orchestrator role -- the account-2 dispatcher, the owner-account (account 1)
standby/watchdog, any account-4 parent -- therefore also acts as that account's dispatcher at every firing: after its standby check,
it reads WORK-QUEUE.tsv for rows `queued` and tagged for its own account (`other`/`account-2` on account 2; `owner`/`account-1` on
account 1; `account-4` on account 4), claims each with tools/work_queue.py, spawns it with create_session on its own account
(source_url https://github.com/NoAutopilot/cipher-lab, the row's model, never below Opus 5.5; prompt: "Read CLAUDE.md, then follow
<brief> exactly as job <job_id>; claim in ROOM.md first"), and posts one ROOM line naming the session. A standby whose firing interval
is over an hour moves it to hourly while any row for its account is queued. The owner then never has to paste a lane prompt into an
account that already has a standing session; a paste is needed only to bootstrap the first standing session on an account.

## Model floor (owner, 28 Sept 2026 20:3x UTC)
The orchestrator runs on Fable; if Fable usage is out, Opus 5.5; nothing below Opus 5.5 for the orchestrator, runners or workers on any account (no Sonnet or Haiku rows in WORK-QUEUE.tsv from now on). With neither model available on any account, all work pauses until a reset; that is acceptable, a downgrade is not. The orchestrator cannot switch its own session's model: when this account has Fable again, ask the owner to switch this session with /model, or move the role per hub-seed/STANDBY-3.md.

## Account 3 runs Fable (owner, 28 Sept 2026 20:5x UTC)
Every row queued to account 3 (tagged third) names Fable, with Opus 5.5 as the only fallback: runners, workers, verifiers and the standby. Vision-heavy transcription and adversarial audits go to Fable first. Nothing below Opus 5.5 anywhere.

## Restricted material guard (28 Sept 2026, owner-requested)
Material a holder shares on a no-publication condition lives only in NoAutopilot/cipher-lab-private, which the owner fills by hand. This public repository has three layers against a mistake: tools/room.py refuses any push whose outgoing files match tools/restricted_fingerprints.txt (one-way fingerprints only, never the words); the restricted-guard GitHub Action scans every push and the whole tree daily; and every worker that pushes with plain git runs `python3 tools/restricted_guard.py --outgoing` first. New restricted sets are added by the orchestrator with `--fingerprint` from a private scratch file; the source words are never committed. A guard finding is a stop: remove the file from the commit, say so in ROOM without quoting it, and tell the owner.

## Owner desk asks: one link, one action, one thing back (owner, 5 Oct 2026)
When the owner must do something at his desk (a HathiTrust page, a catalogue record, a form), give him: (1) ONE link that opens the
exact page or result -- never a volume home page or a search he has to refine; (2) ONE action, in a sentence ("screenshot the
footnotes", "copy the number at the top"); (3) what to send back. Try every cloud route first (IA copy, Google Books API, other
mirrors) and only then ask. Lesson: a HathiTrust volume link left him facing "a bunch of different options" and a Cloudflare page.
- Runner before owner (owner, 5 Oct 2026): a page read in a lent archive.org book, a HathiTrust page or search-inside, an
  academia.edu download or a catalogue lookup goes to the owner's local runner first (owner, 5 Oct 2026: the Claude browser runner that did the 4 Oct JSTOR runs, not the ChatGPT one), as a LOCAL-QUEUE.tsv row (kinds
  ia-reader, hathitrust, catalogue-lookup ...; tools/local_queue_runner_prompt.md), not to the owner's desk. The owner gets
  it only if the runner fails or the step needs his own judgement (a hand comparison, a decision, a payment, a form in his name).
