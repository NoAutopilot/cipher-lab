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
| armstrong-madison-1808 (account 2 self-trigger retired; the campaign continues on the owner-account standing runner session_01R2T5qwd7NBMWGnjRtj8ieX, bound continuous trigger at :25; the earlier owner-account runner session_01H27tXgYoK6tVYXUGAN1h5T finished its H7 step and retired first) | campaign | the letter from the S. Tomokiyo thread; the owner's Codex session's attempts fold in as prior steps | 40 | hourly (minute 25 / 35 / 45), the account's default model; first firing after the seed lands | 00:12 UTC 28 Sept: account 2's runner (session_013E5jUS9GV1AsxLeUcwgbf6) stopped at 620k context after 11 steps; replaced by the owner-account standing runner above (RUNNER-CONT-2 narrowed to the mercy runner per the parent's 00:12 ROOM line). 00:2x UTC: RUNNER-CONT-2 deleted the account-2 self-trigger (trig_01S4q7kbGj2GW5TEHmhF5hx1) and its own stray continuous replacement created before that line was read (trig_01HNdGGeKAhWyDLwpoFH2k9J, fired once at 00:20 into the still-live account-2 session, harmless per that session's own 00:15 ROOM note); no account-2 armstrong trigger remains. |
| espagnol142-mercy-1648 (account 2: runner session_01V7xEY9JxjCxiXnQLtjFnfL, trigger trig_015UXr57KfocoBF6Ut28egBu continuous, :30; the owner-account runner retired unused 22:28) | campaign | furthest along: key evidence, register-matched judge corpus, DECODE ruled out, archive copy on order (a branch, not the state) | 40 | hourly (minute 25 / 35 / 45), the account's default model; first firing after the seed lands |
| fr4715-f61-mayenne-1592 (trigger trig_01BzG21fsHEquT4zqXjgQnGk (bound, continuous, to session_01UgTmQhR7wFtVFrTVdtsq9i), :45) | campaign | Mayenne key on disk (25 rows), Tomokiyo's five read spans as the known answer, calibration in progress | 40 | hourly (minute 25 / 35 / 45), the account's default model; first firing after the seed lands |
| spinelli-beinecke-c1515 (trigger trig_017Ew7azS1JppLzRUvVxrSGG (bound, continuous, to session_016fvFiTTAhQng2VqbiBDmRE), :55) | campaign | Domnina 2015 key (Tomokiyo's own table on disk, 45 rows), one phrase read by Tomokiyo; gate passed 20:09, seeded 20:46 | 40 | hourly at :55 |

**Cadence:** a runner never waits: it runs steps back to back until its daily budget is spent or its list is empty (continuous mode, campaign.md); the hourly cron only restarts a runner that stopped. Hand-firing a bound trigger does not deliver (found 22:3x UTC) and is not used.

**Runner sessions (fixed 21:4x UTC):** a trigger that spawns a fresh session gets no repository checkout and cannot clone the private repository, so the first four firings (20:35 to 21:35) did nothing at about 0.80 USD each. The runners are now four standing sessions created with the repository (session_01H27tXgYoK6tVYXUGAN1h5T armstrong, session_01TrimUWpSxSyUXp7w7FEMfR mercy, session_01UgTmQhR7wFtVFrTVdtsq9i f61, session_016fvFiTTAhQng2VqbiBDmRE spinelli) and the hourly triggers fire into them; a runner past 700k context says so in its done line and the orchestrator replaces it. Runners carry no connector tools: git, the repository's tools and their own subagents only.

## Lean in (28 Sept 2026, about 00:15 UTC, owner's direction)

The owner runs the work on a Max account, not on API keys, so the dollar cost of a step is not a constraint; the
constraint is what the accounts can run at once. Where a campaign shows momentum the orchestrator leans in and decides
what that means. Applied at once: daily_budget_usd raised to 240 for fr4715-f61-mayenne-1592 and to 120 for the other
three (nobody idles on budget; the ledger still records real get_session cost, verified readings per dollar stays the
number shown at the end); a parallel branch on f.61, PARENT WORKER F61-FAMILY (Fable, cap 40), gathers the whole cipher
family Tomokiyo lists (fr.3982, fr.3983, fr.3984, eleven leaves, three with period decipherments) and rebuilds the period
key from them while the campaign runner keeps working its rows; the Armstrong runner moved to this account
(session_01R2T5qwd7NBMWGnjRtj8ieX, :25) when account 2's hit 620k context.

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
| 27 Sept 22:30 | armstrong-madison-1808 | 1 done (H1: the Codex key-image claim never reached GitHub; PR 50 located the Livingston 1803 key frames), H7 running (fetch and hash those frames) | 1 | 12 / 1 / 0 | 0 |
| 27 Sept 22:30 | espagnol142-mercy-1648 | 1 done (H1: the anneal's target sits inside an exact-frequency-profile control band, so the earlier gap was the profile, not decryptability; tools/homophonic_anneal.py --profile added) | 3 | 9 / 1 / 0 | 0 |
| 27 Sept 22:30 | fr4715-f61-mayenne-1592 | 1 done (H1: class map 24/55 vs shuffled max 19/55, unstable between folds), H11 null-aware refit fired 22:27 | 1 | 11 / 1 / 0 | 0 |
| 27 Sept 22:30 | spinelli-beinecke-c1515 | 1 done (H1: the two remaining canvases fetched; cipher is about 9 lines on p.1 plus two lines on p.2, about 55 signs; address leaf clean), next step fired 22:27 | 0.5 | 10 / 1 / 0 | 0 |
| 27 Sept 22:45 | armstrong-madison-1808 | 2 done (H1 Codex claim void; H7 Livingston 1803 key frames fetched, hash-verified, not the target key by value range, control-backed); next H12 reel-9 table screen (account 2 runner, hourly :10) | 2.5 | 13 / 2 / 0 | 0 |
| 27 Sept 22:45 | espagnol142-mercy-1648 | 1 done (H1 exact-profile control: no decryptability beyond the profile); next on account 2's :10 firing | 3 | 9 / 1 / 0 | 0 |
| 27 Sept 22:45 | fr4715-f61-mayenne-1592 | 1 done; continuous runner restarts 22:45 with H11 null-aware refit | 1 | 11 / 1 / 0 | 0 |
| 27 Sept 22:45 | spinelli-beinecke-c1515 | 1 done; continuous runner restarts 22:55 (locate the known phrase) | 0.5 | 10 / 1 / 0 | 0 |
| 27 Sept 23:45 | armstrong-madison-1808 | 4 done, chaining on account 2 (H12 reel-9 table is a one-part sequential key 1-1700, not the target key; H2 glyph-20-null model FAIL control-backed; H3 two-strokes-per-sign design FAIL control-backed); H4 NARA IIIF route in flight | 7.5 (est) | 15 / 4 / 0 | 0 |
| 27 Sept 23:45 | espagnol142-mercy-1648 | 2 done (H2 4x re-crop: rare codes 72, 52, 48, 48 confirmed by three reads per position); runner stops between firings until RUNNER-CONT-2 re-binds it (00:08 dispatcher) | 6 (est) | 12 / 2 / 0 | 0 |
| 27 Sept 23:45 | fr4715-f61-mayenne-1592 | 11 done, 2 dropped, continuous; fragment L10 reading-ready 23:26 (8 letters, S/M, two blind passes 13/13, controls) -> VERIFY-F61-FRAG-1 audit 1; H3 found Tomokiyo's 85-letter read of the sibling fr.3983 f.108 (transfer test next, H19 fetch in flight) | 33.75 (get_session) | 19 / 11 / 2 | 0 |
| 27 Sept 23:45 | spinelli-beinecke-c1515 | 5 done, continuous (H2 crib not located, 3/22, control 22/22; H11 glyph atlas 39 codes; H10 p.[2] reconciled 52 signs, 64 percent agreement; H14 atlas v2 per line); H3 p.[1] blind passes in flight | 29.28 (get_session) | 14 / 5 / 0 | 0 |
