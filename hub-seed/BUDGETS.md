# Budgets

Rate limits are per account and are visible only from inside that account. So each person's orchestrator
writes its own row here on every check-in, and the team picture appears in git. Nobody can see anyone else's
limits any other way.

Fill in from your own session: `get_session` reports `rate_limit_info` (window type, reset time, status:
allowed / allowed_warning / rejected, and whether overage is on) and `usage.cost_usd` for the session.
"Spend" below is the API-equivalent value of the tokens consumed, which is how a session record reports
it. On a subscription **none of it is billed**. Treat it purely as a measure of how fast something eats
the rate-limit window, which is the thing that actually stops work.

| Person | Plan | Window | Resets | Status | Spend this window | Updated |
|---|---|---|---|---|---|---|
| Ryan (owner) | Max | seven-day | see session | allowed_warning | orchestrator 2,042 since 17 Sept; workers about 330 | 21 Sept 2026 |
| noautopilotytbiz (same person, second account) | Max | five-hour | rolling | allowed | 218 for the session 23 Sept 15:12-22:24 UTC (orchestrator plus about 35 workers; the long conversation was the largest single cost) | 23 Sept 2026 22:24 UTC |
| | | | | | | |
| | | | | | | |

## What to do when you see a warning

- **allowed_warning**: finish the worker you are running, do not start another large one, and say so in
  `ROOM.md` so somebody with headroom picks up the next job.
- **rejected**: your window is spent. Note the reset time here and in `ROOM.md`. Work that was mid-flight is
  not lost, because workers push to the repository, not to a session.
- **Long orchestrator sessions are the expensive thing.** One session that runs for days re-reads its whole
  history on every turn. On 17 to 21 September that cost 2,042 against 330 for every worker combined. Start
  a fresh orchestrator every few days and let the old one go; the handoff note at the top of `STATUS.md` is
  what makes that free.

## Model tiering, which is the other half of cost control

Sonnet for searches, sweeps, harvesting and transcription passes. The strongest model only for reconciling
passes against an image, verifier verdicts and orchestration. `CLAUDE.md`'s Usage section is binding.
