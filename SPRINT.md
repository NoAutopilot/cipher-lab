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
| armstrong-madison-1808 (trigger trig_019s5begSuU244cmPNboSyUN, :25) | campaign | the letter from the S. Tomokiyo thread; the owner's Codex session's attempts fold in as prior steps | 40 | hourly (minute 25 / 35 / 45), the account's default model; first firing after the seed lands |
| espagnol142-mercy-1648 (trigger trig_018cY9wT442xNo5jLnXCqWqA, :35) | campaign | furthest along: key evidence, register-matched judge corpus, DECODE ruled out, archive copy on order (a branch, not the state) | 40 | hourly (minute 25 / 35 / 45), the account's default model; first firing after the seed lands |
| fr4715-f61-mayenne-1592 (trigger trig_01BEknRRZSr3dimfZsmjA2Xb, :45) | campaign | Mayenne key on disk (25 rows), Tomokiyo's five read spans as the known answer, calibration in progress | 40 | hourly (minute 25 / 35 / 45), the account's default model; first firing after the seed lands |
| spinelli-beinecke-c1515 (or the best fr.4715 pool row) | campaign, pending gate | Domnina 2015 key, one phrase read by Tomokiyo; joins when INTAKE-SPINELLI's gate passes, else the pool row | 40 | created at the check-in after the gate |

**Runner sessions carry no connector tools** (the trigger stores none): a runner works with git, the repository's tools and its own subagents only; anything needing GitHub, Gmail or session tools is the orchestrator's.

## Scoreboard (the orchestrator updates at each check-in)

| UTC | Campaign | Steps run | Spent | Hypotheses open / done / dropped | Verified readings |
|---|---|---|---|---|---|
