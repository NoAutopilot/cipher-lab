# Team ledger

One row per worker session, written by the orchestrator when the worker is archived. Columns: date, role
(brief template), model, cost in dollars of usage (session metadata), outcome, and the lesson if any. The
weekly retrospective (`.claude/briefs/retrospective.md`) reads this table, LESSONS.md and the git log and
proposes changes to the briefs, CLAUDE.md and the workflows.

Outcome codes: **D** delivered on brief and stopped; **D-** delivered but needed a poke to push, or ran past
the brief; **F** failed (usage limit, init error, blocked); **X** over-claimed and was corrected; **N** clean
negative (a search that found nothing, done right).

| Date | Role | Model | Cost | Outcome | Lesson |
|---|---|---|---|---|---|
| 19 Sept | Archive Lookup: Stepney (first try) | Fable | 9 | F | Blocked by the old network policy; not the worker's fault |
| 19 Sept | Archive Lookup: Stepney | Fable | 12 | D | |
| 19 Sept | Scout: queue builder | Fable | 57 | D- | Read both solver repos in full; began attempting ciphers beyond its brief; interrupted. Led to Usage rules 3 and 7 |
| 19 Sept | Image Capture + Transcription: Wellington | Fable | 30 | D | |
| 19 Sept | Archive Lookup: Whitworth | Fable | 20 | D- | Went idle with work uncommitted; needed a poke. Led to "push, report, stop" |
| 19 Sept | Archive Lookup + Transcription: Eckert 1862 | Fable | 35 | D | |
| 19 Sept | Research: Wellington dictionary edition | Fable | 40 | N | 57 editions, clean negative with a full log |
| 19-20 Sept | Transcription + Reading: Eckert 1864 | Fable | 189 | X | Twenty readings at grade H were sound; "four not printed" was an over-claim; then it started its own audit and a sister-copy sweep beyond the brief. Led to rule 10, Usage rule 7 |
| 20 Sept | Verifier: prior-art audit, Eckert 1864 | Fable | 28 | D | Model for every verifier brief |
| 20 Sept | Access: HathiTrust via browser (Wellington) | Fable | 11 | N | Browser blocked by the proxy CA; found the two APIs instead and documented them |
| 20 Sept | Key Test: Eckert Cipher No. 2 | Fable | 26 | D | Outcome A; settled the last Eckert question |
| 20 Sept | Check Solved: five board targets (workflow) | Sonnet | 18 | D | First Sonnet job; five verdicts, one status change |
| 20 Sept | Scout: verify and file four proposed targets | Sonnet | 6 | D | |
| 20 Sept | Print Check: Stair in Graham 1875 | Sonnet | 2 | N | |
| 20 Sept | Access Test: setup-script fix (first) | Sonnet | 0 | F | Setup script failed at container start (apt-get without update). Led to the guarded script |
| 20 Sept | Access Test: setup-script fix (second) + NLS record | Sonnet | 1 | D | Browser works; NLS Cloudflare-challenged; Wayback fallback |
