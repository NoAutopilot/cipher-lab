COMMON (every LANE G3 worker, 24 Sept 2026). Parent: LANE G3 orchestrator session_01WVnAc4cU7RQjEoBfbkuGrG (successor to LANE G2).
- Read CLAUDE.md in full, then this brief, then the target's NOTES.md sections named in your brief; the last 30 lines of ROOM.md.
- First action: `python3 tools/room.py --start`, then a claim line with `python3 tools/room.py "<role> (<model>, cap $N, for LANE G3)" "claim: <target> -- files: ..."`.
  Last action: a `done:` line with the commit hash and a two-line result. Push with `python3 tools/room.py --push <paths>`; stage by explicit path.
- Run every long job in the FOREGROUND (never background a solver or a fetch loop). Commit and push after each step, so a rate-limit stop loses nothing.
- Stop at your cap (the session metadata's cost figure). At the cap, push what you have, write a 'progress' paragraph in NOTES.md, post done.
- Rule 4 grades per token, rule 7 a script that regenerates any reading (tools/decode_key.py with decode.json, `--check` exit 0), rule 3 matched
  controls for any negative. Rule 10: no "new", "first", "unpublished", "previously unread"; say "read at grade X" and "not found in <source>,
  searched <date>". Absolute dates; read `date -u` before writing any time.
- Gallica on 24 Sept: the IIIF manifest and services endpoints reset often; the direct image endpoint
  (/iiif/ark:/12148/<ark>/f<N>/full/<size>/0/default.jpg) works. After one retry per URL, stop that endpoint and report. .texteBrut is altcha-walled: never.
- Good-citizen rule: one request at a time per host, >= 1.5 s apart, UA `cipher-lab research script (contact via repository)` unless the
  playbook says a site needs a browser UA, stop a host on 429/403/challenge and log it. Report requests per host in your done line.
- Keep committed images under 30 MB per folder; above that, keep a manifest and put working copies in your scratchpad.
- End: a short report paragraph in the target's NOTES.md (what was found, where it was not found); do not classify novelty. Stop; no follow-ups.
