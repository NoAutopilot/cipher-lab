# Proof sprint (27 Sept 2026, 20:2x UTC, the owner's decision): four campaigns, 48 hours, one number at the end

**The question:** can this pipeline turn a letter that has a key, an image and a known-answer sibling into a verified
reading (N3 or better after two audits)? Four campaigns run continuously until 29 Sept 2026, 21:00 UTC. The number
reported at the end is verified readings per dollar. That number, not the target count, is what the owner shows before
more accounts join.

**The rules (parent.md "Campaigns"):**
- The list below is fixed for the sprint. It changes only at a retrospective, with the reason written here. New ideas go
  into a campaign's hypothesis list, ranked against the rest, never onto this list.
- A campaign never ends on "couldn't". A runner that finds no runnable hypothesis writes three before it stops. A
  document or person the campaign waits on is one branch (`needs: doc ...` / `needs: person ...`), never the state.
- Breadth frozen for the sprint: no new intakes, no scouting, no new lanes, no tooling except what a campaign's step
  needs. Runner PR landings, the mailbox, the desk and the verifier lane continue.
- Each campaign has a daily budget; the runner stops for the day when it is spent, and the orchestrator can raise it
  at a check-in with the reason logged.
- The orchestrator's job at each check-in is to read the four CAMPAIGN.md files and argue with their rankings, not to
  spawn breadth. Only the orchestrator closes a campaign, by writing `closed:` with the reason.

| Target | Kind | Why it is in | Daily budget USD | Runner trigger |
|---|---|---|---|---|
| armstrong-madison-1808 (trigger trig_01D5cb4ja2EhZiYPmjGUoLDX (bound to session_01H27tXgYoK6tVYXUGAN1h5T), :25) | campaign | the letter from the S. Tomokiyo thread; the owner's Codex session's attempts fold in as prior steps | 40 | hourly (minute 25 / 35 / 45), the account's default model; first firing after the seed lands |
| espagnol142-mercy-1648 (trigger trig_01DioitDVNdFvdBeUpaNz1pd (bound to session_01TrimUWpSxSyUXp7w7FEMfR), :35) | campaign | furthest along: key evidence, register-matched judge corpus, DECODE ruled out, archive copy on order (a branch, not the state) | 40 | hourly (minute 25 / 35 / 45), the account's default model; first firing after the seed lands |
| fr4715-f61-mayenne-1592 (trigger trig_018p5Y75bmcRKCKQkyMpCqSm (bound to session_01UgTmQhR7wFtVFrTVdtsq9i), :45) | campaign | Mayenne key on disk (25 rows), Tomokiyo's five read spans as the known answer, calibration in progress | 40 | hourly (minute 25 / 35 / 45), the account's default model; first firing after the seed lands |
| spinelli-beinecke-c1515 (trigger trig_01JyLt8CeZV2pbpzNPUxBUYG (bound to session_016fvFiTTAhQng2VqbiBDmRE), :55) | campaign | Domnina 2015 key (Tomokiyo's own table on disk, 45 rows), one phrase read by Tomokiyo; gate passed 20:09, seeded 20:46 | 40 | hourly at :55 |

**Cadence:** a runner never waits for its scheduled minute; the orchestrator fires an idle runner by hand as soon as its last step is done, at every check-in and between them (the owner's direction, 21:58 UTC).

**Runner sessions (fixed 21:4x UTC):** a trigger that spawns a fresh session gets no repository checkout and cannot clone the private repository, so the first four firings (20:35 to 21:35) did nothing at about 0.80 USD each. The runners are now four standing sessions created with the repository (session_01H27tXgYoK6tVYXUGAN1h5T armstrong, session_01TrimUWpSxSyUXp7w7FEMfR mercy, session_01UgTmQhR7wFtVFrTVdtsq9i f61, session_016fvFiTTAhQng2VqbiBDmRE spinelli) and the hourly triggers fire into them; a runner past 700k context says so in its done line and the orchestrator replaces it. Runners carry no connector tools: git, the repository's tools and their own subagents only.

## Scoreboard (the orchestrator updates at each check-in)

| UTC | Campaign | Steps run | Spent | Hypotheses open / done / dropped | Verified readings |
|---|---|---|---|---|---|
| 27 Sept 20:45 | armstrong-madison-1808 | 0 (seed 20:34) | 0 | 10 / 0 / 0 | 0 |
| 27 Sept 20:45 | espagnol142-mercy-1648 | 0 (seed 20:31; runner fired 20:35 before the seed) | 0 | 8 / 0 / 0 | 0 |
| 27 Sept 20:45 | fr4715-f61-mayenne-1592 | 0 (seed 20:36; F61-CAL's calibration 8/55 recorded as the prior attempt) | 0 | 10 / 0 / 0 | 0 |
| 27 Sept 20:45 | spinelli-beinecke-c1515 | gate passed 20:09, seed queued | 0 | -- | 0 |
| 27 Sept 21:45 | armstrong-madison-1808 | 0 (runner fired 21:25, no ROOM line, no commit: the trigger's fresh session has no repository checkout) | 0 | 10 / 0 / 0 | 0 |
| 27 Sept 21:45 | espagnol142-mercy-1648 | 0 (runner fired 20:35 and 21:35, same) | 0 | 8 / 0 / 0 | 0 |
| 27 Sept 21:45 | fr4715-f61-mayenne-1592 | 0 (runner fired 20:46, same) | 0 | 10 / 0 / 0 | 0 |
| 27 Sept 21:45 | spinelli-beinecke-c1515 | 0 (seed 20:57, 9 hypotheses; runner fired 20:55 before the seed, same) | 0 | 9 / 0 / 0 | 0 |
