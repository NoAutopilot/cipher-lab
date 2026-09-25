LANE DX job 1, PROBE (Sonnet, cap $1.50, no subagents). Parent: LANE DX orchestrator session_01LgrmyB7HMcMaeLTRNbEqb4. Filed 25 Sept 2026.
You are NOT the DECODE worker: never log in anywhere, never call any site. Read .claude/briefs/runs/2026-09-25-lane-dx-COMMON.md first (the credentials rule especially).

Job: report, for this account's fresh container, whether each credential variable is set or MISSING, and nothing else about any value:
DECODE_USER, DECODE_PASS, IA_USER, IA_PASS, JSTOR_USER, JSTOR_PASS, GOOGLE_BOOKS_KEY, OPENALEX_KEY, OPENALEX_API_KEY, S2_KEY, NARA_API_KEY.
Method: one loop of `if test -n "${!v}"; then echo "$v set"; else echo "$v MISSING"; fi` (bash indirect expansion prints only the name). For DECODE_USER only, add whether it contains an `@`: `case "$DECODE_USER" in *@*) echo "DECODE_USER has @";; *) echo "DECODE_USER no @";; esac`. No lengths, no character classes, no substrings, no env/printenv/set/export -p, no set -x.
Output: one ROOM line via `python3 tools/room.py --push ROOM.md` flow, e.g. `python3 tools/room.py "LANE DX probe (Sonnet, <session id>)" "done: probe -- DECODE_USER set (no @), DECODE_PASS set, ..."`, pushed. Touch only ROOM.md. Final reply: one paragraph with the same list, files touched (ROOM.md), request count per host (github only), cost. Then stop.
