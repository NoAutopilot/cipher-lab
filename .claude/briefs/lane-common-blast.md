# Standing family lanes under blast mode -- common rules (account-3 orchestrator, 8 Oct 2026)

Owner, 8 Oct 2026: "5 - 8 running on all accts, with refills". `tools/work_queue.py --blast` keeps one lane open per account and
refills it 15 min after it closes, with the same standing brief. So a lane is one incarnation of a standing lane, not a one-off:

- **Start.** Exactly as `.claude/briefs/default-lane.md` steps 0, 0a and 1 (fetch, `room.py --start`, `date -u`, claim the WORK-QUEUE
  row, exclusions), then read your lane's newest "LANE <name> handoff" in STATUS.md and continue its "next" list before anything new.
- **Operating rules.** As default-lane.md "Operating rules": lane orchestrator on your own account, workers via create_session on your
  own account, ~6 live (5-8 total sessions on the account with you), refill within 15 min via send_later, ledger every worker from
  get_session, Opus 5.5 for you, verifiers and cipher reasoning, Sonnet for mechanical reads and searches. Stop on five_hour or
  seven_day `rejected` (BUDGETS.md); on `allowed_warning` keep going (owner, 8 Oct: usage resets in a couple of days) but say so in
  each check-in line. Cap 60, box 600 per incarnation.
- **Prior work.** Every worker brief that transcribes, keys, decodes, aligns, crops, looks up or audits an item includes
  `.claude/briefs/prior-work-step.md` by reference and pastes its result before the first priced step. Briefs written from a
  register (NEXT-STEPS, SIBLINGS, LOOSE-ENDS, specs, a previous handoff) re-check every row with its check 1 first.
- **Intake gate.** `tools/intake_gate_check.py <target>` pasted before any deep-work brief; a nonzero exit means a check-solved
  worker first (`.claude/briefs/check-solved.md`, with its Premise check), not the deep work.
- **Hosts.** One worker at a time per external host across the whole lane (CLAUDE.md good-citizen rule); fetch once to disk with a
  manifest, read from disk after. Gallica answered 403 to every cloud session on 8 Oct: one probe per lane incarnation at most, no
  retries; BnF items only from images already on disk until a probe returns 200.
- **Results.** A reading that beats its matched control goes to a SEPARATE first-verifier session (CLAUDE.md verifier template,
  depth per `.claude/briefs/runs/2026-10-08-acct3-depth-bar.md`). At N3+ D2+ after a first audit, add one WORK-QUEUE row
  `AUD2-<lane>-<n>` for its second audit on **account-3** (the VERIFY lane) unless account 3 read or first-audited it, then on another
  account that did not; name it in ROOM for the account-3 orchestrator.
- **Rule 10 and rule 4a wording only.** Report what was found and where it was not found; never "new", "first", "solved".
- **Close.** `tools/ledger_check.py`, LEDGER rows, STATUS.md "LANE <name> handoff" with a numbered **next** list the next incarnation
  can start from (cost per item, what is blocked and on what), `work_queue.py --done`, one ROOM done line, push via room.py.
