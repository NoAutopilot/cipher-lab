LANE R8 WORKER COMMON (parent: LANE R8 orchestrator, session_01RUhLrpkEtWxVLVVDoYdsvm). Written 25 Sept 2026 22:24 UTC.
Read, in order: CLAUDE.md; `.claude/briefs/runs/2026-09-24-lane-r4-common.md` (base rules); `.claude/briefs/runs/2026-09-25-lanes-7b-COMMON.md`
(25 Sept addendum, wins where they differ); `.claude/briefs/runs/2026-09-25-lane-r6-common.md` and `2026-09-25-lane-r7-common.md` (their overrides
still hold; where they name LANE R7, read LANE R8); this file; your job brief.
First command: `python3 tools/room.py --start`. ROOM lines through `tools/room.py` only (claim before work, done when stopping).
- Wall-clock box and $ cap in your brief: stop and push at whichever comes first; the box is also a minimum. Never read your own cost.
- No subagents unless your brief names them. Never call AskUserQuestion; if blocked, `flag:` ROOM line, push, stop.
- Hosts: only those your brief names. gallica.bnf.fr: one fetcher in this lane (R8-L3034), 1-2 s apart; the BnF finding aid
  (archivesetmanuscrits.bnf.fr) at >= 2 s, page 1 via plain POST as in ciphers/fr2933-salviati-1525/leafnotes/siblings.md "Method".
- Every cryptanalytic run through `tools/family_run.py`, control first (rule 3); both numbers side by side in HYPOTHESES.md.
- Rule 10 wording only. Report what was found and where it was not found; do not classify novelty.
- Done line: `done: for LANE R8: <target> <target number> vs <control number> ...`, requests per host, no cost figure. Times from `date -u`.
- Stage shared files by explicit path; `python3 tools/room.py --push <paths>` to commit and push.
