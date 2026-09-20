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
2026-09-20 14:28 | Print Check: Hamilton/Cobham | note: GOOGLE_BOOKS_KEY works but API needs &country=US or it 403s 'Cannot determine user location'
2026-09-20 14:36 | DECODE login: access playbook | touching CLAUDE.md to record the login flow
2026-09-20 14:38 | Print Check: Hamilton/Cobham | touching QUEUE.md and QUEUE-scores.json (Cobham rank 13 row)
2026-09-20 14:40 | Orchestrator | note: IA_USER/IA_PASS and JSTOR_USER/JSTOR_PASS set; lending-only IA books can be borrowed one at a time for a page check; JSTOR for verifier scholarship checks
2026-09-20 14:42 | DECODE login | flag: login flow confirmed working (plain CSRF form POST, no client-side password encryption; tools/decode_fetch.sh) but DECODE_USER/DECODE_PASS in this environment are rejected server-side ("Incorrect user name or password"), confirmed by screenshot and by a second independent curl replication. Not an unset-var case. Blocks record 8725 (intercepted-royalist-1646) and R413 (boswell-1628, QUEUE rank 5) same as before; the three top-ten items the 06:12 note expected DECODE to unblock are still blocked. Needs the person to supply working credentials; do not keep retrying the same pair (lockout risk).
2026-09-20 14:43 | DECODE login | done: CLAUDE.md access playbook updated, tools/decode_fetch.sh added, intercepted-royalist-1646/NOTES.md + REQUEST.md updated; boswell-1628 not created (nothing fetched); pushing now
2026-09-20 14:40 | Print Check: Hamilton/Cobham | done: Hamilton 1677/1852/HMC threads closed (all not found); Cobham vol.22 found on HathiTrust but Cloudflare-blocked, HTRC EF API located a candidate cipher page (scan 62) unread; pushed
2026-09-20 15:05 | IA Login worker | flag: IA_USER/IA_PASS login does NOT work — IA_USER is not an email address and archive.org (xauthn API and the current /login page) requires one; account_not_found on the API, login page has only an "Email address" field. No borrow was possible this session; details in CLAUDE.md Access playbook and tools/ia_borrow.py.
2026-09-20 15:05 | IA Login worker | touching QUEUE.md, QUEUE-scores.json (rank-6 Cornwallis row only)
2026-09-20 15:22 | IA Login worker | done: pushed. Login blocked (see flag above); Hamilton/eckert page checks done via be-api search-inside only (no page numbers recoverable that way); Cornwallis/Saberton re-confirmed NOT FOUND on IA by a second search method.
2026-09-20 | check-solved: stair-townshend-1710, monck-1660, nls-20769 | note: running full six-source check-solved.js sweeps (owner opted into Workflow tool) on the three board items that reached the board without a full blind sweep; touching each target's NOTES.md in turn. Per the 14:42 DECODE flag above, DECODE_USER/DECODE_PASS are currently rejected server-side, so briefs telling searchers to log in directly will fall back to a blocked/unreachable report, not a false negative.
