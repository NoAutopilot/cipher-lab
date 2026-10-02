# LIKELY-<n>: likely-solves phase 2 -- one candidate, intake gate, then exactly its first cheap test with its control

Written 2 Oct 2026 03:3x UTC (clock read) by the account-4 parent (session_01SEzoee67SivPooFpTkxMme), from account-3's
brief `.claude/briefs/runs/2026-10-02-acct3-likely-solves.md` (owner's ask, 2 Oct: likely solves in the vein of what we
have solved -- a key we hold, a sibling with a period decipherment, a printed clear text, or a sign pool). The session's
prompt names the row of `ciphers/_triage/likely-solves-2026-10-02.tsv` (read its `first_cheap_test`, `head_start` and
`why` cells first), the cap, hosts and vision-call count. Role field: `LIKELY-<n>-<slug> (account-4)`. Model: Fable 5.1
(Opus 5.5 if Fable fails). Box: 60 minutes. Stop before any unit that would cross 80 pct of cap or box.

Before `create_session`, the parent runs `python3 tools/premise_check.py <slug> --row-text "<head_start cell>"` (add
`--new` for a `new` row, `--needs-images --leaf <f.N>` when the first test reads an image) and pastes its output in the
prompt; a nonzero exit means no session (the row goes back to SHORTLIST with the failure named). SHORTLIST itself runs
it on every row it ranks (RETRO-2026-10-02-account4 proposal 5, applied 2 Oct 2026: LIKELY-2, -4, -7 and SPLIT-matignon
spent USD 19.77 on rows whose `head_start` named material not on disk).

1. `python3 tools/room.py --start`; last 30 ROOM.md lines; stop with `blocked` if another account claims the target in
   the last six hours; claim line naming the row.
2. Intake gate. If the folder exists: `python3 tools/intake_gate_check.py <slug>`; exit 1 only for the missing web/blog
   check -> do that step first (check-solved.md "Required step", section headed `## Web and blog check (LIKELY-<n>, 2 Oct
   2026)`), re-run and paste; exit 1 for any other reason (an edition unread, no verdict) -> stop with a `blocked` line
   naming what a check-solved worker must read; a hit carrying a decipherment -> `found-solved`, stop. If the row is
   `new` (no folder): create `ciphers/<slug>/NOTES.md` with the status word `open` on line 1 only after a minimal
   check-solved of your own (the editions the row names, both solver repositories grepped from fresh shallow clones,
   the web/blog step), written in the gate's format with line 2 naming what you read; nonzero exit -> `blocked`, stop.
3. The first cheap test, exactly as the row's `first_cheap_test` cell names it, with its matched control FIRST
   (rule 3): a key application runs against 20 shuffled-key controls (or `--shuffle-target`), a family through
   `tools/family_run.py`; the known-answer step first when any part of the text is already read (README common tail,
   "Known answer first"). Images: fetch once with a manifest line, `tools/iiif_lines.py` crops before any subagent
   call, two blind passes + reconciliation at most, vision calls as the prompt names. Grade every token (rule 4).
4. Record: the two numbers side by side in HYPOTHESES.md (one row) and a dated NOTES.md section
   "## LIKELY-<n> (2 Oct 2026, account-4)"; a spec under specs/<slug>.json with a `cheap_test_done` entry if the
   target has none (Pipeline 3a); `tools/judge_plaintext.py` output pasted for any candidate reading; the
   finish-or-blocker sections (rule 5) if the status becomes `partial`; `python3 tools/gaps_check.py <slug>` then.
   A reading that clears the judge AND the shuffled-target check gets a "reading ready" ROOM line for a separate
   verifier; never "new", "first", "unpublished"; never a status change beyond open/partial/blocked/found-solved.
5. Commit by explicit path, rebase, `python3 tools/restricted_guard.py --outgoing`, push to main; done line with both
   numbers, the gate's exit code, vision calls and request counts per host. Stop; no second test.

The common tail of `.claude/briefs/README.md` applies in full.
