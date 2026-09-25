# KEYS.md: the credential register (names only, never values)

One row per environment variable a session may read. Agents **request** a key with `tools/key_request.py NAME --purpose
"..." --tool tools/x.py` (it appends the row here, an ASKS.md row for the owner's desk and a ROOM.md flag); the owner
**adds** it in the environment settings of both accounts (cloud environment menu, Edit, API credentials or environment
variables; a session started before the change never sees it); the next fresh session on each account **announces**
it: `tools/room.py --start` runs `tools/key_probe.py --sync`, which flips the row to `set`, records which account saw
it and when, and appends a ROOM.md line "key NAME now set on <account>" -- so both parents learn of it at their next
check-in without the owner writing anything. Accounts label themselves with `CIPHERLAB_ACCOUNT` (`ytbiz` for the
noautopilotytbiz account, `owner` for the other; `unlabelled` until set, ASKS row 63). A `set` row whose `seen`
column names one account only is a key the other account still lacks. No worker uses a key whose purpose reads
"undocumented". Status words: `requested`, `set`, `declined`. Instituted by parent 7d, 25 Sept 2026 (UPDATES.md).

| name | purpose | read by | requested (by, date, ASKS) | status | seen (account@UTC) |
|---|---|---|---|---|---|
| DECODE_USER | DECODE (de-crypt.org) login, plain user name | tools/decode_browser_login.js | owner, 20 Sept 2026 | set | ytbiz@2026-09-25T22:44 |
| DECODE_PASS | DECODE password | tools/decode_browser_login.js | owner, 20 Sept 2026 | set | ytbiz@2026-09-25T22:44 |
| IA_USER | Internet Archive account (email) for lending | tools/ia_borrow.py | owner, 20 Sept 2026 | set | ytbiz@2026-09-25T22:44 |
| IA_PASS | Internet Archive password | tools/ia_borrow.py | owner, 20 Sept 2026 | set | ytbiz@2026-09-25T22:44 |
| GOOGLE_BOOKS_KEY | Google Books API key (`&key=`, with `&country=US`) | tools/print_check.py | owner, 20 Sept 2026 | set | ytbiz@2026-09-25T22:44 |
| JSTOR_USER | JSTOR (JPASS), owner's machine only | tools/jstor_runner_brief.md | owner, 20 Sept 2026 | set | ytbiz@2026-09-25T22:44 |
| JSTOR_PASS | JSTOR password, owner's machine only | tools/jstor_runner_brief.md | owner, 20 Sept 2026 | set | ytbiz@2026-09-25T22:44 |
| OPENALEX_KEY | OpenAlex API key (Bearer header) | tools/print_check.py | owner, 24 Sept 2026 | set | ytbiz@2026-09-25T22:44 |
| S2_KEY | Semantic Scholar API key (x-api-key header) | tools/print_check.py | owner, 24 Sept 2026 | set | ytbiz@2026-09-25T22:44 |
| REDDIT_CLIENT_ID | Reddit API app id (client_credentials grant) | .claude/briefs/runs/2026-09-24-reddit-fetch-*.md | owner, 24 Sept 2026 | set | ytbiz@2026-09-25T22:44 |
| REDDIT_CLIENT_SECRET | Reddit API app secret | .claude/briefs/runs/2026-09-24-reddit-fetch-*.md | owner, 24 Sept 2026 | set | ytbiz@2026-09-25T22:44 |
| EUROPEANA_API_KEY | Europeana Search API (`wskey=`) | scouts (QUEUE.md) | ASKS 47, 25 Sept 2026 | set | ytbiz@2026-09-25T22:44 |
| DPLA_API_KEY | Digital Public Library of America (`api_key=`) | scouts | ASKS 47, 25 Sept 2026 | set | ytbiz@2026-09-25T22:44 |
| AWS_ACCESS_KEY_ID | undocumented (document before use): ASKS 62 asks which service and job | none yet | found by probe, 25 Sept 2026 | set | ytbiz@2026-09-25T22:44 |
| AWS_SECRET_ACCESS_KEY | undocumented (document before use): ASKS 62 | none yet | found by probe, 25 Sept 2026 | set | ytbiz@2026-09-25T22:44 |
| CLOUDSDK_AUTH_ACCESS_TOKEN | undocumented (document before use): Google Cloud SDK access token, ASKS 62 | none yet | found by probe, 25 Sept 2026 | set | ytbiz@2026-09-25T22:44 |
| DDB_API_KEY | Deutsche Digitale Bibliothek API | scouts | CLAUDE.md optional keys, 25 Sept 2026 | requested | |
| APE_API_KEY | Archives Portal Europe API | scouts | CLAUDE.md optional keys, 25 Sept 2026 | requested | |
| CORE_API_KEY | CORE open-access full text (Bearer) | verifiers | CLAUDE.md optional keys, 25 Sept 2026 | requested | |
| NARA_API_KEY | NARA catalog API (x-api-key; by email per NARA's README) | scouts (koehler-1944 RG 65 file) | QUEUE.md free-key gap, 24 Sept 2026 | requested | |
| CIPHERLAB_ACCOUNT | account label for this register (`ytbiz` or `owner`), not a secret | tools/key_probe.py | parent 7d, 25 Sept 2026, ASKS 63 | requested | |
