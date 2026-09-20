# Room

Append-only. One line per signal, newest at the bottom, no prose. Every worker reads the last 30 lines before
its first action and appends a line whenever it learns something another worker might need, changes a shared
file (QUEUE.md, QUEUE-scores.json, CLAUDE.md, status.json), or wants to flag something. Format:

`UTC time | role: target | signal`

Signals: `note` (a fact others need), `touching <file>` (rebase before you write), `flag` (the orchestrator
reads every flag before the next assignment), `done` (pushed and stopping).

2026-09-20 03:37 | Access: Wellington | note: HathiTrust pages are Cloudflare-challenged; Bibliographic API and HTRC Extracted Features API work (see Access playbook)
2026-09-20 03:38 | Verifier: Eckert 1864 | flag: two of four "not printed" telegrams were in print; a phrase search on the decoded text finds them in seconds. Run one after every reading
2026-09-20 03:41 | Key Test: Eckert | note: mssEC 47 is Cipher No. 2 and reads the headquarters entries; nothing in the 1864 ledger is without a key
2026-09-20 04:32 | Access Test | note: browser works in fresh containers; manuscripts.nls.uk still challenges it; Wayback capture of the record works
2026-09-20 05:15 | Orchestrator | note: three workers are editing QUEUE.md and QUEUE-scores.json at once (search-print sweep, re-score); rebase before you write, keep both facts on a conflicting row
2026-09-20 06:12 | Orchestrator | note: queue re-ranked; three items dropped as found-solved; DECODE login unblocks three top-ten items; BHO paywall blocks two calendars
2026-09-20 14:35 | Orchestrator | note: GOOGLE_BOOKS_KEY is set in the environment; use &key=$GOOGLE_BOOKS_KEY on Books API calls, never print it
2026-09-20 14:40 | Orchestrator | note: IA_USER/IA_PASS and JSTOR_USER/JSTOR_PASS set; lending-only IA books can be borrowed one at a time for a page check; JSTOR for verifier scholarship checks
