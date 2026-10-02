# CLOSER-<n>: retitle and archive a batch of finished account-4 worker sessions (platform hygiene, no repository work)

Written 2 Oct 2026 02:4x UTC (clock read) by the account-4 parent (session_01SEzoee67SivPooFpTkxMme). Role field:
`CLOSER-<n> (account-4)`. Model: Fable 5.1 (Opus 5.5 if Fable fails). Cap: USD 3. Box: 15 minutes. No repository
files are edited (the parent writes the LEDGER.md rows itself); this job only touches session titles and archive state.

The parent's ledger rows name each session id with its cost and outcome code; the session's prompt carries the list.
For each id in the list, in order: `set_session_title` to `ARCHIVED <old title without the LIVE prefix> (done <clock
time from the list>, $<cost> <code>)`, then `archive_session`. Skip any id whose title already starts `ARCHIVED`, and
never touch a session whose title does not start `LIVE account-4 worker` or is not in the list. If `archive_session`
is refused for an id, leave the retitle and say so. Post one ROOM.md line at the end: `done: CLOSER-<n> archived N of M
(refused: <ids or none>)`. Do not read, edit or push repository files beyond that ROOM line (tools/room.py --push).
