# DESK-CARDS (account 3 worker) -- 4 Oct 2026 02:0x UTC (account-3 orchestrator)

The owner's desk is now a kanban (https://claude.ai/artifact/GNMEYAR5C1ZeBHvJ9bXYxm, 20 cards seeded: the BnF/Desenclos emails,
10 sorters, quotes, send queue, Francis Bacon Society, JSTOR/local run, TNA Wroth, "other copy orders", duplicates). The owner says
he likely still owes work requested by the other accounts (1, 2, 4 and the earlier owner/ytbiz parents). Build the full list.
Model Opus 5.5, cap USD 6, box 45 min. Claim in ROOM first; no outward action of any kind.

1. Sources: every ASKS.md row not closed (done/answered/closed/resolved/withdrawn/superseded/sent); outreach/*.md drafts whose
   status is ready/drafted/checked and not sent (python3 tools/desk_check.py helps); SEND-QUEUE.tsv rows not sent; LOCAL-QUEUE.tsv
   and JSTOR-QUEUE.tsv rows not answered (count only -- one card per queue); outreach/QUOTES.md; sorter artifacts named in ASKS/ROOM.
   For each, check it is still live: the target's NOTES.md/status may show it was answered, superseded or no longer needed
   (e.g. a target since closed, found-solved, or its question answered by a later lane) -- list those separately as "can close".
2. Merge duplicates and group trivia: all pure paid copy orders to one archive = one card; one card per distinct decision; the 20
   cards already on the board are excluded (ids: confirm-bnf bnf-reply desenclos s-birago s-jm s-arm s-din s-rev s-sav s-deb s-flo
   s-sic s-mlh quotes sendq fbs local tna copies dups) -- if a row belongs inside one of them, say which.
3. Rank by impact: what it unblocks (a NEAR row or counted reading > a partial target with a named next step > backlog), times
   probability, over the owner's minutes or money. Mark each: tag sort|email|send|order|runner|decide, mins, and the ASKS row(s).
4. Write outreach/desk-cards-2026-10-04.json: a list of {id, title (<=60 chars, plain words), detail (<=300 chars: what to do and
   why, in plain words, no jargon, no personal data, no addresses of private individuals), link (the draft/sorter/ASKS URL on
   github.com/noautopilot/cipher-lab/blob/main/... or artifact URL), linkLabel, mins, tag, rank, asks: [row numbers]} in rank order,
   plus outreach/desk-cards-close.tsv (ASKS row, why it can close, evidence file). Do not edit ASKS.md statuses yourself.
5. Commit by explicit path, push, done line with counts (cards, can-close), five-line report, stop.
