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

**Armstrong, 28 Sept 2026 about 00:40 UTC (owner's direction).** The owner's ChatGPT runner works armstrong-madison-1808
as a parallel sprint of its own and is not to be influenced: its checkpoint PRs are landed verbatim and closed with the
landed commit only, no ROOM line is addressed to it, nothing is written into second-opinions/ by us, and its files are
read as leads, never as verdicts. Our Armstrong work runs alongside on both accounts: the owner-account runner takes the
shorthand (H24), account 2 takes the correspondent pools (ARM-CORR: H25 Monroe Papers, H26 Pinkney and Erving) through
the queue; the owner's desk holds ASKS 80 (Brooklyn private Livingston letter, moved up) and 66 (editors, follow-up in a
week); ASKS 77 (Brant Box 37) is deprioritised because that key family is the printed-form type and the target is not.

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
| 28 Sept 00:45 | armstrong-madison-1808 | 13 done (account 2's runner finished H18 mark inventory and stopped at 620k context); owner-account runner on H24 (six shorthand systems, known-answer control first); H24-H27 added rank 1-4 (shorthand; Monroe, Pinkney, Erving pools; crib-loop power test); ARM-CORR queued to account 2 for H25-H26; ChatGPT parallel sprint walled off | 11 est + 8.56 (new runner) | 25 / 13 / 0 | 0 |
| 28 Sept 00:45 | espagnol142-mercy-1648 | 9 done 1 dropped, continuous since 00:30 on account 2 (H13 dots inventory; H5 wordcode non-test control-backed; H4 judge split no gain; H14 lexicon-coverage instrument in flight); no reading | 16 est (account 2 cost not visible) | 16 / 9 / 1 | 0 |
| 28 Sept 00:45 | fr4715-f61-mayenne-1592 | 14 done 2 dropped; fragment L10 audit 1 HELD (cells 5/8 S, letters M, judge control not reproduced); map transfers to fr.3983 f.108 (0.643 vs 0.38 permuted) and the joint fit passes both ways; F61-FAMILY branch gathering the 11-leaf family (f.274 passes running); runner restarts 00:45 | 40.79 real (7.04 today) | 24 / 14 / 2 | 0 |
| 28 Sept 00:45 | spinelli-beinecke-c1515 | 12 done, continuous (p.[1] reconciled 71 percent on atlas v3; HOOK family does not split; the other three 1519 Barcelona letters carry no cipher; Domnina PDF unreachable, IA offline); runner at 553k context, replacement due near 700k | 55.36 real (26.08 today) | 20 / 12 / 0 | 0 |
| 28 Sept 01:45 | armstrong-madison-1808 | 19 done; this hour: shorthand instrument fails its own known-answer control (non-test); Monroe pool all clear, an Erving-to-Monroe 1806 glossed code letter found and screened out; Adams lead is the Department's cipher; held marks re-read (inventory 9); ARM-CORR (account 2): Pinkney used WE028 with Madison Jan 1808 (known answer), Erving legation cipher a third table, no second letter in the target code, ASKS 83; first owner-account runner retired at 570k, second runner live (:25) on H27 | 67 real (both runners) | 29 / 19 / 0 | 0 |
| 28 Sept 01:45 | espagnol142-mercy-1648 | 14 done 1 dropped, continuous on account 2; DECODE 958 ruling-out withdrawn (key.tsv matches the Brussels 1647-98 key style), ASKS 82 for the eight-key register; H18 DECODE listing in flight | 24 est | 20 / 14 / 1 | 0 |
| 28 Sept 01:45 | fr4715-f61-mayenne-1592 | 21 done 2 dropped; F61-FAMILY: period key (37 pairs, f.274r) reads known spans 0.782 vs 0.382, coverage-limited; joint fit with bracket split 0.745 and held-out 0.873; runner's own f.108r gloss key FAIL (crop design, H34 refiles it); BnF finding aid dates the family leaves; six JSTOR rows; F61-FAMILY-2 on f.101r (46 rows x 5 segments, chunk passes running); runner at 627k, deferring subagent rows under the old warning reading (corrected 01:4x) | 68.52 real runner + 39.28 family + 29.76 family-2 so far | 34 / 21 / 2 | 0 |
| 28 Sept 01:45 | spinelli-beinecke-c1515 | 17 done 1 dropped; first runner stopped at 717k (homophonic solver a design-mismatched non-test; key table word-codes corrected; Domnina citation found, no open copy); second runner live (:55) on H22 | 71.19 real (first runner) | 24 / 17 / 1 | 0 |

Runner sessions at 01:45 UTC 28 Sept: armstrong session_01NuaRiPghx6VRXA6GuJE8ne (trig_01ADnvcNKc3ygErySr42Y8TP :25); mercy account 2 session_01V7xEY9JxjCxiXnQLtjFnfL (trig_015UXr57KfocoBF6Ut28egBu :30); f61 session_01UgTmQhR7wFtVFrTVdtsq9i (trig_01BzG21fsHEquT4zqXjgQnGk :45); spinelli session_01213SyYPVrRii7MWRZbyU3S (trig_017Guv5Q4sWeWdskDQbUvAv5 :55).
