# NO-CRACKS (account 3 worker) -- 5 Oct 2026. Opus 5.5. Cap $8, box 90 min. Owner: "for all of these, what's blocking them / next
step, and if it requires a human, add to my kanban ... nothing slipping through the cracks. Systematize."
Build tools/no_cracks.py (+ offline test tools/tests/test_no_cracks.py, --help, docstring stating what it catches and one case it must
NOT block, CLAUDE.md Usage 8a):
1. Inputs: PROGRESS.tsv (folder column), NEXT-STEPS.tsv (regenerate first with tools/next_steps.py), ASKS.md open rows,
   LOCAL-QUEUE.tsv rows bounced/blocked by the runner, SEND-QUEUE.tsv, and a board export JSON (path arg; the parent exports the desk
   board's "cards" collection to a file -- card fields: id, lane, title, detail, link, asks[], folders[]).
2. For EVERY PROGRESS row and every open/partial/blocked NEXT-STEPS folder: emit one row {folder, name, next_step, blocker, who:
   agent|owner|outside, board_card_id or MISSING}. who=owner when the next step needs a person: a payment/order, an email/form send, a
   judgement (sorter, eye check, decision), a desk read the runner could not do (Cloudflare/sign-in), a credential. who=outside when
   it waits on an archive/person reply (no card needed, but the waiting card must exist if we asked). who=agent otherwise.
   A row with no next step at all is flagged NO-NEXT.
3. Output NO-CRACKS.tsv (repo root) and --cards-json FILE: proposed new board cards for who=owner rows with no card (title <= 60
   chars, one link, one action, one thing back per .claude/briefs/parent.md "Owner desk asks"; group rows sharing one action, e.g. all
   HathiTrust desk reads in one card). Exit 1 when any MISSING or NO-NEXT remains (--report-only to always exit 0).
4. Wire it in: one line in .claude/briefs/parent.md check-in duties and in hub-seed/CHECKIN-PROMPT.md ("run tools/no_cracks.py; add the
   proposed cards; every NO-NEXT row gets a next step written in its NOTES"), SYSTEM.md entry.
5. Run it once now (export the board with the ArtifactData tool: url https://claude.ai/artifact/GNMEYAR5C1ZeBHvJ9bXYxm, collection
   cards), write NO-CRACKS outputs, and for NO-NEXT rows write the next step into the folder's NOTES (from its own gaps/handoffs, or
   "next: <step>, ~$X"). Do NOT write board cards yourself: put the proposed cards in research/no-cracks-cards-2026-10-05.json; the
   parent reviews and writes them. Commit by path, push, ROOM done line, 5-line report (counts: rows, owner, outside, agent, MISSING, NO-NEXT).
