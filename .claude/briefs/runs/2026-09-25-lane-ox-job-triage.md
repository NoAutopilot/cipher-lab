OX-TRIAGE (Sonnet, cap $5, no subagents, NO fetching of any host). Parent: LANE OX orchestrator, session_01BE3g8tWbS4T24KXMpShHt4. Read .claude/briefs/runs/2026-09-25-lane-ox-COMMON.md first; it applies in full.

Job: triage twelve open targets from what is already on disk, and write ONE file: .claude/briefs/runs/2026-09-25-lane-ox-triage.md (the output; this brief is ...-ox-job-triage.md). Touch nothing else except ROOM.md (claim and done lines).

Targets (folders under ciphers/): hellen-frederick-1752, breda-statengeneraal-1624-25, clairambault1225-paget-1714, vaudemont-willemiii-1699, willem-van-hessen-1567, vanbeuningen-dewitt-1657, borssele-heinsius-1714, heinsius-dopff-1702, heinsius-hermitage-1704, heinsius-vanhaersolte-1703, rumpf-vandebie-heinsius-1716-19, la-garde-1577.

Read only: each folder's files (NOTES.md, ciphertext, manifests; do not open images unless one look settles whether a leaf carries an interlinear decipherment), the QUEUE.md rows for these targets (grep by folder name and by sender), and the repo's key lists (grep -ril "key\|sleutel\|chiffre" over ciphers/*/key.tsv, ciphers/*/NOTES.md, CATALOG.md, LANDSCAPE.md, sources/wvo/ for the same correspondents and offices). Scripts read, models judge: grep first.

Per target, one block:
- what is on disk: images (count, where), transcription (yes/no, how many tokens), ciphertext length and symbol set if known, language.
- route, one of: recovery (a decipherment on the leaf or in the same inventory number, a decrypted sibling in the same correspondence, a published key, or known plaintext such as the plain copy in vanbeuningen-dewitt-1657 -- name which and where it is); cryptanalysis (no key: name the matched control that rule 3 needs -- design, N, K, language -- and the route the solver repositories have not tried); blocked (the edition or print for that date not yet read, or images not on disk -- name what is missing).
- expected value by CLAUDE.md pipeline item 3: P(first cheap test moves it) x value / cost, with one line of reasoning each; a score 0-10.
- the named first step (one worker job, with its cap guess in dollars and whether it needs transcription first).
Heinsius circle first: for borssele-heinsius-1714, heinsius-dopff-1702, heinsius-hermitage-1704, heinsius-vanhaersolte-1703, rumpf-vandebie-heinsius-1716-19, establish whether any key of that office (Heinsius's secretariat, NA 3.01.19, or the correspondents' keys) is published, decrypted or on disk in the same fonds, so that one key could serve several; say which letters share a system if the notes show it. Likewise for the two Willem van Oranje letters (willem-van-hessen-1567, la-garde-1577): check sources/wvo/ and any WVO key already used in this repo.

End the file with a ranked table (rank, target, route, EV score, first step, cap) and a TOP THREE line. Rule 10 wording; mark every inference as inferred. If a target turns out solved or claimed elsewhere on disk, say so with the file and line.

Finish per COMMON: commit the one file by path, push with tools/room.py --push, ROOM done line naming the top three, one-paragraph reply.
