# DISPATCH-STANDBY (2 Oct 2026, written by account 3; runs on account 2)

Model: Opus 5.5 (or Fable). Cap USD 2, box 20 min. One job: add the orchestrator standby check to this account's dispatcher.

1. `python3 tools/room.py --start`; claim in ROOM.md.
2. Read .claude/briefs/parent.md "Orchestrator fallback chain" and .claude/briefs/dispatcher.md "Standby check" (both new, 2 Oct 2026).
3. list_triggers on this account; find the routine named like "cipher-lab dispatcher (account 2)". With update_trigger, APPEND to
   its prompt (keep everything already there, change nothing else): " Then run the standby check in .claude/briefs/dispatcher.md
   'Standby check' (read it fresh each firing) and act on it exactly as written." Read the trigger back with get_trigger and
   confirm the text is there.
4. Done line in ROOM.md quoting the trigger id and the appended sentence. Do not create any session; do not take over anything.
Never call AskUserQuestion; never print credentials; never name the owner.
