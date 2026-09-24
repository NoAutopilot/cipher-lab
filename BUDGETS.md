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
| the owner | Max | seven-day | see session | allowed_warning | orchestrator 2,042 since 17 Sept; workers about 330 | 21 Sept 2026 |
| noautopilotytbiz (same person, second account) | Max | five-hour | rolling | allowed | 235.5 for the session 23 Sept 15:12-23:16 UTC (orchestrator plus about 35 workers; the long conversation was the largest single cost); five-hour window allowed at close, no overage | 23 Sept 2026 23:16 UTC |
| noautopilotytbiz, orchestrator wake 2 (session_01SepNMpYrr6L2EwqL43aTnm) | Max | five-hour | rolling | allowed | 50.75 for the orchestrator session 23 Sept 23:16 to 24 Sept 01:47 UTC (closed below its $60 cap), plus about 120 across its 20 workers (LEDGER rows of 24 Sept); cap $60 for the session itself | 24 Sept 2026 01:20 UTC |
| | | | | | | |
| | | | | | | |

**Confirmed by the owner, 24 Sept 2026:** the project runs on a Claude Max subscription only, no API key, so no
session is billed. Every session record checked that day shows a five-hour window with overage off. The dollar
caps in briefs are pacing for the shared window, not a budget; if any session ever shows `isUsingOverage: true`,
stop and tell the owner.

**Scaling rule, 24 Sept 2026:** with about fifty sessions on one five-hour window, every orchestrator checks `rate_limit_info.status` on itself before each dispatch: `allowed_warning` means no new workers anywhere; `rejected` means every lane interrupts its workers and writes the reset time here and in ROOM.md. The window resets on the rolling schedule get_session reports; work already pushed is safe.

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

**Scaling rule, 24 Sept 2026 05:12 UTC, corrected 06:34 UTC after the 05:30-06:10 window exhaustion (owner: "2x
our efforts overall keeping our rate limit approach in mind").** Live lanes (T, G, V, N, R, W; S and T close
when their scope is exhausted rather than fill to ceiling — see below), each capped at $120 and **10** live
workers (cut from 16 after the doubling burned the shared window in 18 minutes: 05:12 authorised, 05:30
`allowed_warning`, 05:50 `rejected`, 06:10 reset, next reset 11:10 UTC). The parent adds a lane on an unowned
host family whenever every lane is at capacity and its own rate-limit status is still `allowed`.
- **The window is one account-wide pool, not per lane.** A ceiling raise applies to every live lane at once, so
  raise in increments (e.g. +3 per lane), not straight to target, and let a few minutes pass between increments
  while every lane's status stays `allowed`, so a burst shows up as an early warning instead of an immediate wall.
- **`allowed_warning` posted by any lane in ROOM.md stops spawning in every lane immediately** — do not wait to
  see it on your own `get_session` call, since by the time you do, the shared pool may already be past it. The
  lane that saw it also logs the reset time here and in ROOM.md.
- **`rejected`:** every lane interrupts its workers, notes the reset time here, and re-arms for it.
- **A lane whose scope is exhausted closes and says so, rather than filling to the ceiling** (LANE T, 24 Sept:
  "lane scope exhausted, so not filling to the new 16-worker ceiling"). A raised ceiling is a maximum, not a
  quota to hit.
Gallica stays at two fetchers regardless.

**LANE N, 24 Sept 2026 05:31 UTC:** five-hour window at `allowed_warning` (seen on three LANE N workers and on LANE N itself; resets 06:10 UTC). LANE N stopped spawning at 15 live (the last three spawned 05:30, before the reading). No worker interrupted (status is not `rejected`). LANE N own usage $6.69.

**Rate-limit event, 24 Sept 2026.** The 2x load (seven lanes, 16 workers each) reached `allowed_warning` at 05:30 UTC and
`rejected` at about 05:50; the window reset at 06:10. Three lane orchestrators (G, N, R) ended their
turns on the rejection and were woken by the parent at 06:36. The corrected pacing rule above (10 live workers per lane,
Sonnet for anything another agent checks, a warning anywhere stops spawning account-wide) dates from this same 06:34 UTC
correction. The parent re-arms its check-in for the reset time when the status is `rejected`.

**LANE N2, 24 Sept 2026 13:51 UTC:** rate_limit_info on LANE N2 (session_01DfQyAaXAgcoFZMAbBTGj4f) reads **allowed_warning on the seven_day window** (rateLimitType seven_day, resets 2026-09-26 13:00 UTC per resetsAt 1790427600), overage off. The five-hour window was not the one reporting. LANE N2 stopped spawning at 13:50 with two live Sonnet workers (csDA2, csBV, both small); no worker interrupted (not rejected). Own usage $55.8 at 13:50.
**LANE R3, 24 Sept 2026 13:50 UTC:** get_session on the LANE R3 orchestrator (session_01GPDjihFcZasP5KTSYRS5uN) reads
`rate_limit_info.status: allowed_warning`, `rateLimitType: seven_day`, resets Sat 26 Sept 2026 13:00 UTC (the five-hour window
read `allowed` at 13:23). LANE R3 stopped spawning and closed on handoff; posted in ROOM for every lane. Lane usage: orchestrator
about $14, four workers $41.15.

**Parent, 24 Sept 2026 14:20 UTC:** the seven-day window reads `allowed_warning` on the parent and on every lane (resets Sat
26 Sept 2026 13:00 UTC). Decision: every lane closed on its handoff (G3 14:01, V3 13:27, R3 13:52, N2 14:16), no lane or
worker is started until the window resets or the owner says otherwise; the hourly check-in keeps running and does owner
asks, ledger, board and second-opinion routing only. Parent usage $978.8 since 23 Sept 15:12; lanes and workers today about
$1,000 more. The five-hour window is not the binding limit any longer; the seven-day one is.

**Owner decision, 24 Sept 2026 14:45 UTC:** told of the seven-day `allowed_warning` and that `rejected` would stop every session
including their own until Sat 26 Sept 13:00 UTC, the owner chose to keep going ("momentum"). The parent started two lanes
(R4 recovery, cap $50, 5 workers; N3 copy-free nominations, cap $35, 4 Sonnet workers) instead of the earlier four-lane load.
Rule for this period: `allowed_warning` no longer stops spawning inside those caps; `rejected` on any session stops every lane
at once (interrupt workers, handoff, stop). The parent checks every 30 minutes.

**Owner, 24 Sept 2026 16:53 UTC:** "not concerned about the limits; whatever is pending will be parked till Saturday." Caps raised:
LANE N3 to $60 and 6 Sonnet workers (six new copy-free scout families), LANE R4 to $80 and 8 workers (the four new Gallica
letters, Salviati code-and-mark model, 1519 key). The stop rule is unchanged: `rejected` on any session halts every lane and
the parent re-arms at the reset.

**JSTOR, 24 Sept 2026 17:05 UTC:** the owner bought JPASS monthly (about $20 a month, cancel any time) on the account Chrome is
logged into on their machine: unlimited online reading, 10 PDF downloads a month. Reads are no longer rationed; the runner
still reads in the online viewer only and never downloads. Review at the end of October whether the runner used it enough to
keep; the cloud still cannot reach JSTOR at all.

**Owner, 24 Sept 2026 18:48 UTC (to parent 7b): "we want to keep chasing momentum."** Seven-day window still `allowed_warning` (resets Sat 26 Sept 13:00 UTC). Restarted LANE R5 (Opus, cap $60, 6 workers) and LANE N4 (Opus, cap $40, 4 Sonnet workers) plus one Sonnet board worker ($6). Same stop rule: `rejected` on any session halts every lane and the parent re-arms at the reset. Parent 7b own usage at 18:52: about $4.
