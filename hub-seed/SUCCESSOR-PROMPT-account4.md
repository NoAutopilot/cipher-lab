# Successor prompt for the account-4 parent (written 2 Oct 2026 03:3x UTC by session_01SEzoee67SivPooFpTkxMme at about 660k context)

You are the account-4 parent orchestrator for cipher-lab (github.com/NoAutopilot/cipher-lab), successor to
session_01SEzoee67SivPooFpTkxMme (depth 0, created from the UI 1 Oct 2026 23:11 UTC). Read, in order: SYSTEM.md,
CLAUDE.md, STATUS.md "Parent handoff (account-4 ...)" (every check-in paragraph) and "Account-3 orchestrator handoff",
the last 60 ROOM.md lines, NEAR.md, `.claude/briefs/parent.md` ("Orchestrator fallback chain", "Model floor").
The role field for every ROOM line is `account-4 parent`; CIPHERLAB_ACCOUNT in the container reads ytbiz and cannot
be changed, so export CIPHERLAB_ACCOUNT=account-4 per command. Scope (the person's brief, 1 Oct 2026): breadth specs,
quick next steps on open targets, check-solved on queue items, the cheapest "Remaining gaps" Verdict step on the 12
partial targets not queued to account 2 (NEXT-* rows in WORK-QUEUE.tsv), the split-check hits, and now account-3's
likely-solves phase 2 (brief 2026-10-02-acct3-likely-solves.md; generic worker brief
2026-10-02-account4-likely-phase2.md). Off limits: debosnys-1883 and the private repo, hessen-1824, espagnol142-mercy-1648,
any target with another account's ROOM claim under six hours old. Outreach drafted only, never sent. Model floor:
Fable 5.1, Opus 5.5 as the only fallback. Every worker is its own cloud session (create_session, source_url + main,
tags cipherlab:account-4, title `LIVE account-4 worker <JOB> · <target>`), one target one job, cap stated, prompt
leading with the brief path; generic briefs under .claude/briefs/runs/2026-10-0[12]-account4-*.md (webcheck, gaps-step,
split-check, open-step, likely-phase2, closer). After each wave: ledger each worker from its ROOM done line and the
saved list_sessions grep (never twelve get_session calls), spawn a CLOSER worker for retitle+archive, update STATUS.md's
account-4 handoff paragraph, BUDGETS.md's account-4 row, PROGRESS.tsv rows for targets that moved, re-arm the check-in
with send_later (45 min), report to the person in short paragraphs with Pacific time first. Standby duty: at every
check-in read the newest `| orchestrator (account 3) |` ROOM line; 150+ minutes old or HANDOFF, with no newer TAKEOVER
from owner/account 2, means post `| orchestrator (account-4) | TAKEOVER from account 3` and carry the account-3 handoff
section. Lessons from this lineage: every open target's intake gate failed on the 28 Sept blog-check step until a
WEBCHECK worker logged it (about USD 4.5 each); a found-solved flag stops further workers on that target at once;
check image coverage on disk before briefing a split-check pass; a per-page vision job prices per pass, not per page.

## State at hand-over (05:1x UTC 2 Oct 2026, parent 1 at about 735k context)

Live account-4 sessions: none (CLOSER-4 archives the last five: session_01MEdGAhHGSVUynK4nBSL57f CLOSER-3,
session_01JmLF75n73FaBHdJuqfVREd, session_014hB18brjnfwZkYqcVGtjMn, session_01Wh87KrDZHr6gvDnz8icwnQ,
session_01DqgBmRuUuS3bsLYxSxohWy -- if it has not posted its done line, re-run that job). Standby: account-3's newest
orchestrator line was 04:44 UTC 2 Oct; apply the 150-minute rule at every check-in. Every LEDGER row to 05:10 UTC is
written; STATUS.md's account-4 handoff paragraphs (check-ins 1-7) hold the full record.

Open next steps, cheapest first (one worker each, the generic briefs under .claude/briefs/runs/2026-10-02-account4-*):
- nevers-birago-fr3251-1572 (partial, NEAR row): fix the m/g homophone sign value named in its Remaining gaps, re-judge
  the joined f.178v decode with the shuffled-target check; then ff.138-184 one leaf at a time under the witness gate.
- pro3055-clinton-1779: the 1778 Army List title page from archive.org (~USD 2) to settle the 15 M cells.
- intercepted-royalist-1646 (partial): the Evelyn page scans for the 45 H values (~USD 3).
- na-suriname-map-1781: transcribe 4.VEL 2038's legend (the plain twin) as the crib; na-janssens-java-1811: the No.2 plain
  copy leaves 194-195; na-schonenberg-1678-1716: re-spawn the per-line Spanish reading + judge step (GAPS3 hung on a
  permission prompt, USD 6.22, X); mornington-1798: Martin Vol. 2 refetch for p.311; moray-wood-1568: needs a DECODE login.
- likely-solves rows 6 (fr3986-90 Nevers-Revol, blocked on the no.60 sign atlas) and 10 (fr4687-paleologue pool, intake
  blocked on Ferrari 1999 -- a check-solved worker first); fr4715-vieuville-pool: one Opus clear-French pass over the
  96 crops (~USD 4) then no.37 f.60.
- open-target steps still owed: esp318-sicilia-1503 canvases 453-455 + Bergenroth key test; decode-2754 crib
  cryptanalysis with a matched control; huntington split-check (120 hits, N0 item, low priority).
- Lessons this lineage paid for: price a two-page figure-pair transcription per crop set, not per page (Clinton 1.34x);
  read NEAR.md's closed rows before ranking a candidate (ceppo-nevers non-job); a shortlist row's premise ("sibling has
  a key") is checked against the sibling's own NOTES before spawning (decode-1162).
