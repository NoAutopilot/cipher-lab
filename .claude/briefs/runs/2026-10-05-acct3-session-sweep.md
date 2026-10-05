# SESSION-SWEEP (written by account 3, 5 Oct 2026; one row per account, run ON that account). Opus 5.5. Cap $6, box 60 min.

Owner, 5 Oct 2026: make sure every chat on every account pushed its work to GitHub. Each account sees only its own
sessions, so this job runs once per account.

0. `git fetch origin && git checkout -B main origin/main`; ROOM claim via tools/room.py ("SESSION-SWEEP (account N)").
1. list_sessions with mine: true; page through ALL sessions since 1 Oct 2026 (idle, completed, archived). Skip this
   session and live lane orchestrators that are still inside their box (they report on their own).
2. For each session: get_session + list_events (last events only; do not read whole transcripts) and decide one of:
   pushed (its claimed result has a matching commit on origin/main or a ROOM.md done line with a commit hash) /
   unpushed-live (container still holds work: commits not on origin/main or files written, not pushed) /
   transcript-only (result stated in its last messages, container gone, no matching commit) / nothing (no result).
3. unpushed-live: send_message the session: 'Push your unpushed work to main by explicit path (git fetch origin main;
   git pull --rebase origin main; git push origin HEAD:main), write your ROOM done line for the account-3 orchestrator,
   then stop.' Check back once after 15 min.
   transcript-only: copy the stated result (numbers, readings, findings, file contents it printed) into the target's
   NOTES.md under '## Recovered from session <id> (<date>)', marked "recovered from transcript, not re-verified", and
   push it yourself. Never recover credentials, personal data or images.
4. Write SESSION-SWEEP-<account>-2026-10-05.tsv at repo root (session_id, title, target, last_active, verdict, action,
   commit) and push. ROOM done line: totals per verdict, list of targets with recovered or newly pushed work, cost.
Rules: one message per session; do not restart work, do not start new work; never archive anything still holding
unpushed work.
