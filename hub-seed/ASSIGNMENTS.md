# Assignments

The work queue between accounts. Nothing here dispatches: no account can start a session in another
account. An orchestrator **writes** a row, and the orchestrator on the named account **pulls** it on its
next scheduled wake. Latency is one poll interval, and a row sits until someone wakes.

Status: `open` (nobody has it), `claimed` (with who and when), `done` (with the commit), `dropped` (with
a reason). Do not delete rows; a queue's history is how the retrospective learns what routing works.

| # | Raised | Project | Job | For | Brief | Status |
|---|---|---|---|---|---|---|
| 1 | 21 Sept | cipher-lab | Native-resolution re-transcription of Randolph f.277r-v, 20-30 crops under 2500px, then frequency analysis | any | `.claude/briefs/transcription.md` plus the "What a next solver needs" section of that target's NOTES.md | open |
| 2 | 21 Sept | cipher-lab | Print check: CSP Foreign vol. 22 for Cobham 1588, and CSP Domestic 1644-45 for Charles I to Rupert | any | `.claude/briefs/print-check.md` | open |
| 3 | 21 Sept | cipher-lab | Check-solved sweep on the next five unswept queue items | any | `.claude/briefs/check-solved.md` | open |
| 4 | 21 Sept | cipher-lab | Once the DECODE login works: read record 8725, then pull R413 (Boswell) and R4930 (Randolph key) | any | `.claude/briefs/archive-lookup.md` | blocked on ASKS row 1 (retested 21 Sept with rotated creds, still rejected) |

## Writing a row

Say what the job is in one line, name the brief that governs it, and set **For** to a specific account only
when it must be that one, for example because only that account holds a credential. Otherwise leave it
`any`, because a row that anyone can take is a row that gets taken.

## Taking a row

Check your own limits first, in `BUDGETS.md`. If your window is near its end, do not claim; write your row
in the budgets file instead so someone with headroom sees it. Otherwise set the status to `claimed` with
your account name and the time, push immediately so nobody duplicates you, then do the work in the project
repository as normal. Set it to `done` with the commit hash when the work is pushed.
