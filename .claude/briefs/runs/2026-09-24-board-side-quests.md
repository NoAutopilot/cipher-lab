BOARD WORKER: side quests tab (Sonnet, cap $6). Owner's ask, 24 Sept 2026 20:57 UTC: "make sure I have clear visibility on all the new stuff I added in." Tonight's owner-added items live in results rows, lane lines and ASSIGNMENTS; they need one place.

First: `date -u`; `python3 tools/room.py --start`; read tools/build_dashboard.py in full (four views: Readings, Your desk, The machine, Hall of fame; the Hall of fame view added at 18:55 is the pattern to copy), status.json keys, hub-seed/ASSIGNMENTS.md tail (from 18:40), LEDGER.md tail, and `python3 tools/room.py --digest "2026-09-24 18:40"`. ROOM claim "board side quests: files status.json (new key sidequests), tools/build_dashboard.py, tools/tests/test_build_dashboard_sidequests.py, docs/index.html".

Deliverables:
1. status.json: a new top-level list `sidequests`, one object per item: `title`, `asked` (absolute time, e.g. "24 Sept 2026 19:46 UTC"), `state` (one of: running, done, blocked, waiting on you, queued), `result` (one sentence, rule 10 wording, numbers where they exist), `next` (one sentence: what happens next and who does it), `link` (repo folder or file), `session` (id if live). Items, from the record (verify each against ASSIGNMENTS, LEDGER, ROOM; do not invent):
   - Hall of fame view (done 18:55; Cryptiana credit on the board)
   - Momentum restart: LANE R5 and LANE N4 (running; their live focus lines)
   - Image cipher-page detector (done, gate failed: recall 0.69, false positives 0.21)
   - Pooling letters by key (done, no ready corpus; RAH 9/23-25 lead)
   - Iberian archives scout (done: PARES down, Torre do Tombo two codex leads; scDIGI running)
   - Solver experiment, crib loop (done: +13.5 to +15 at N 244; +4.9 on code+mark at 720)
   - Salviati purchase f.55v-f.57v (owner 20:16; state per R5's latest ROOM line)
   - Nevers key no.60 application, six letters (running/blocked on the hand; calibration on fr.3983 f.169 next)
   - Grants: OpenAI Researcher Access (submitted by the owner 24 Sept); Anthropic AI for Science and External Researcher Access (waiting on you: NCIS membership first, then the forms; links in outreach/grants-applications.md)
   - Z13 ARTHUR LA stress test (done, mechanism negative with control; paste-ready paragraph in ciphers/zodiac-z13-stress/NOTES.md)
   - Reddit thread, runaway note 2021 (state from rfetch run 2's ROOM line: fetched, or blocked on the credential)
   - Reddit thread, 1600s book (queued behind the first fetch)
   - Urquhart host-text lesson ingest (state from the lessons worker's ROOM line)
   - Gold-target survey on Fable: Schmeh top 50 and Dunin lists, approach and spec per item, mechanical judge, process memo (running; session_013GkMQP9y84gHGG4pSSwaQj)
   - Retrospective f and retro-apply f (state from ROOM)
   - Successor prompt (done: hub-seed/SUCCESSOR-PROMPT.md)
2. tools/build_dashboard.py: a fifth view button "Side quests" in the same style, a count line at the top ("N items: a running, b done, c waiting on you"), then one card per item ordered: waiting on you first, then running, blocked, queued, done; each card shows state as a chip, asked time, result, next, link, and the session id in small text when live. "Waiting on you" items also appear on Your desk as a short list "Side quests waiting on you" (no duplication of the copy boxes). Nothing else on the board changes. Test in tools/tests/ that builds from a three-item fixture and asserts the view, count and ordering; existing tests still pass.
3. Rebuild `python3 tools/build_dashboard.py`; check docs/index.html renders the tab (browser_fetch.js --shot if it works, else read the HTML). Commit with `MSG="board: side quests view (owner-added items with state, result, next)" python3 tools/room.py --push status.json tools/build_dashboard.py tools/tests/<test> docs/index.html dashboard.html`.
Do not publish the artifact (the parent republishes). Do not edit results rows or lanes. ROOM done line with the item counts; final paragraph of five lines; stop.
