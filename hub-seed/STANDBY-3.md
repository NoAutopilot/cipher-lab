# Standby orchestrator on account 3

Set up 28 Sept 2026, 20:3x UTC, by the orchestrator on the owner account (session_01FXDfYR3CvGk7tcid1Aav1n), after the owner asked for one, so progress does not stop if the owner account runs out of usage. The owner account shows a seven-day usage warning (resets about 05:00 UTC 3 Oct); on 28 Sept a model limit stopped every owner-account runner from 06:45 to 14:15 UTC.

There is ONE orchestrator at a time (parent.md "Single orchestrator"). The standby does nothing to the tracks while the owner-account orchestrator is alive.

## Heartbeat

The owner-account orchestrator posts a ROOM line as `| orchestrator (owner account) |` at every check-in (hourly at about :10) and mirrors its current check-in prompt to `hub-seed/CHECKIN-PROMPT.md` whenever it changes that prompt. The mirror is the state: tracks, runners, counts, open items.

## Standby check (hourly, at :40)

`cd <cipher-lab> && git pull -q --rebase origin main; grep -E "\| orchestrator \(owner account\)|\| orchestrator \(account 3\)" ROOM.md | tail -3`

- **Stay in standby** (no ROOM line, no other action; reply "standby ok") when the last owner-account orchestrator line is under 150 minutes old AND there is no newer `HANDOFF to account 3` line.
- **Take over** when the last owner-account orchestrator line is 150 minutes old or older, OR a line `| orchestrator (owner account) | HANDOFF to account 3` is the newest orchestrator line (the owner-account orchestrator posts it when its own rate limit reads rejected, or the owner asks).

## Takeover

1. Post `| orchestrator (account 3) | TAKEOVER: last owner-account line <time>, reason <stale / handoff>`.
2. Read `hub-seed/CHECKIN-PROMPT.md`, SPRINT.md "Re-plan", NEAR.md, the last STATUS.md orchestrator note, and ROOM since the last owner-account line.
3. Owner-account runners and workers are presumed stopped (the same usage ran out). You cannot see or change owner-account sessions or triggers; never try. For each live track in the mirror, check ROOM: a track whose owner-account runner posted in the last 90 minutes is still alive, leave it; otherwise start an account-3 runner for it (Fable if its rate limit reads allowed, else Opus 5.5, never below; source_url https://github.com/NoAutopilot/cipher-lab; prompt modelled on the track's CAMPAIGN.md and the mirror; its own bound hourly trigger). Runner rows marked running by owner-account session ids are void (the runner prompts already say so).
4. Arm your own hourly check-in trigger and run the mirror's check-in yourself, with these changes: every "owner account" role becomes "account 3"; the owner-account trigger ids are not yours; post ROOM lines as `| orchestrator (account 3) |`; the Gmail steps apply only if this account has the Gmail connector for the project mailbox, otherwise list "mailbox not visible from account 3" under NEEDS YOU.
5. Keep the mirror current: write `hub-seed/CHECKIN-PROMPT.md` whenever your state changes.
6. The owner talks to you in this session while you hold the role. Same reply format (TLDR, progress bars, RUNNING / STALLED / NEEDS YOU), same rules (CLAUDE.md, parent.md; rule 9: never name the owner; rule 10 wording; never send email; never print credentials; never force-push main).

## Handback

When a new `| orchestrator (owner account) |` line appears after your TAKEOVER line (the owner account is back):
- The owner-account orchestrator reads your ROOM lines and the mirror, then posts `| orchestrator (owner account) | HANDBACK accepted: runners <kept on account 3 / to retire>`.
- On that line, you retire what it names (delete their triggers, retitle ARCHIVED, archive), disable your own check-in trigger, post `| orchestrator (account 3) | back to standby`, and return to the hourly standby check.
- Until a HANDBACK accepted line appears, keep running; if both post check-ins for two hours without a handback line, the owner-account orchestrator holds the role and you stand down.

## Model rule (owner, 28 Sept 2026 20:3x UTC)

The orchestrator runs on Fable; if Fable usage is out, Opus 5.5; never anything below Opus 5.5 (no Sonnet, no Haiku), for the orchestrator or for any runner or worker it starts. If neither Fable nor Opus 5.5 is available on any account, all work pauses until a usage reset: post `| orchestrator (account 3) | paused: no Fable or Opus 5.5 usage, resumes at <reset>` once and do nothing else. A paused state is acceptable; a downgraded model is not.

## Limits

- No new tracks on takeover; the mirror's tracks only. Harvest rows tagged `third` in WORK-QUEUE.tsv continue as before through the dispatcher.
- Account 3's own usage: if its rate limit reads rejected, post `| orchestrator (account 3) | out of usage` and stop; nothing else can continue until one account resets.
