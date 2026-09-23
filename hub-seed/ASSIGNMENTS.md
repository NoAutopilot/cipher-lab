# Assignments

The work queue between accounts. Nothing here dispatches: no account can start a session in another
account. An orchestrator **writes** a row, and the orchestrator on the named account **pulls** it on its
next scheduled wake. Latency is one poll interval, and a row sits until someone wakes.

Status: `open` (nobody has it), `claimed` (with who and when), `done` (with the commit), `dropped` (with
a reason). Do not delete rows; a queue's history is how the retrospective learns what routing works.

| # | Raised | Project | Job | For | Brief | Status |
|---|---|---|---|---|---|---|
| 1 | 21 Sept | cipher-lab | Native-resolution re-transcription of Randolph f.277r-v, 20-30 crops under 2500px, then frequency analysis | any | `.claude/briefs/transcription.md` plus the "What a next solver needs" section of that target's NOTES.md | dropped, 3d69025: target found-solved (f.278 is the contemporary decipherment), crops kept |
| 2 | 21 Sept | cipher-lab | Print check: CSP Foreign vol. 22 for Cobham 1588, and CSP Domestic 1644-45 for Charles I to Rupert | any account whose environment has `GOOGLE_BOOKS_KEY` (not ytbiz as of 23 Sept, ASKS row 10) | `.claude/briefs/print-check.md` | open |
| 3 | 21 Sept | cipher-lab | Check-solved sweep on the next five unswept queue items (taken as ranks 11, 13, 15, 17, 18: the first five below the top ten with no target folder and no prior sweep) | any | `.claude/briefs/check-solved.md` | done, eca0be9 (23 Sept 2026) |
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
| 5 | 23 Sept | cipher-lab | Sforza reply to Zorzo del Maino, 4 May 1446, and Amidani to Sforza, f.70 (BnF italien 1583, DECODE R7898-R7899; QUEUE G7): check-solved sweep, then a solver session annealing both as one shared key with a matched synthetic control | any | `.claude/briefs/check-solved.md`, then `.claude/briefs/solver.md` | done, 88d5f3e (open at stage 2) and 69cac80 (closed-negative conditional on the transcription, matched control 99%+) |
| 6 | 23 Sept | cipher-lab | Check-solved on the Pallotto cluster (QUEUE D1, BAV Barb.lat 6956, DECODE R233/R239/R241/R242/R253 vs R221): Nuntiaturberichte and other editions first | any | `.claude/briefs/check-solved.md` | done, 0cb5f5b: found-solved (key 2018, edition 1895) |
| 7 | 23 Sept | cipher-lab | Once DECODE login works: open D1 letter and sibling records, transcribe (two Sonnet passes), apply the sibling's decipherment as key, read, then verifier | account with DECODE credentials | `.claude/briefs/archive-lookup.md`, `.claude/briefs/transcription.md`, `.claude/briefs/solver.md`, then verifier | dropped 23 Sept 22:30: D1 found-solved; D2-D7 are in Bourdeau's volumes; only D8 (RAH 9/29) survives and is his by adjacency |
| 8 | 23 Sept | cipher-lab | Re-score every QUEUE row and the D and G sections with the revised reader profile (all readable languages); no fetching, cached data only | any | `.claude/briefs/scout.md` | open |
| 9 | 23 Sept | cipher-lab | Scout on catalogues NOT on DECODE: TNA Discovery ('cipher', 'cypher', 'in cipher' in item descriptions, SP and PRO 30 series), NRS catalogue, BL Explore/Archives and Manuscripts, Gallica full-text ('en chiffre', 'chiffré' in inventories), county record offices; exclude anything with a DECODE record or a solver-repo hit; score for the unique-solves metric | any account with archive network access (not ytbiz until ASKS row 11) | `.claude/briefs/scout.md` | open |
