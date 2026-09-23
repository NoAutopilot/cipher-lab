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
| 7 | 23 Sept | cipher-lab | Once DECODE login works: open D1 letter and sibling records, transcribe (two Sonnet passes), apply the sibling's decipherment as key, read, then verifier | account with DECODE credentials | `.claude/briefs/archive-lookup.md`, `.claude/briefs/transcription.md`, `.claude/briefs/solver.md`, then verifier | revised 23 Sept 23:30: owner reports DECODE fixed. Once the single login test passes (ASKS row 1): record 8725 for the 1646 folio first, then a full catalogue pull (RecordsList, paged, 1.5 s apart, one session) to sources/decode/ so the neighbour tool runs on the whole catalogue rather than the public scrape; then D8 (RAH 9/29) if Bourdeau has not reached it |
| 8 | 23 Sept | cipher-lab | Re-score every QUEUE row and the D and G sections with the revised reader profile (all readable languages); no fetching, cached data only | any | `.claude/briefs/scout.md` | claimed, noautopilotytbiz, 23 Sept 2026 19:40 UTC |
| 9 | 23 Sept | cipher-lab | Scout on catalogues NOT on DECODE: TNA Discovery ('cipher', 'cypher', 'in cipher' in item descriptions, SP and PRO 30 series), NRS catalogue, BL Explore/Archives and Manuscripts, Gallica full-text ('en chiffre', 'chiffré' in inventories), county record offices; exclude anything with a DECODE record or a solver-repo hit; score for the unique-solves metric | any account with archive network access | `.claude/briefs/scout.md` | done, b5d1b76: 493 survivors, 19 scored (QUEUE.md N1-N19) |
| 10 | 23 Sept | cipher-lab | Check-solved on N1 (BL Mss Eur D623 Mornington cipher and key), N2 (TNA SP 35/36 1722 intercepts with keys), N3 (BL Add MS 4956 Courten diary with Madden's key): editions first (Wellesley Despatches 1836-37; SP 35 decrypts and the Deciphering Branch; Courten in print), then the six sources | any | `.claude/briefs/check-solved.md` | done, 0790a35: N2 found-solved, N1 partial, N3 open |
| 11 | 23 Sept | cipher-lab | Check-solved on N4-N19 in batches of four, cheapest first; any that pass go to REQUEST.md with an imaging quote request | any | `.claude/briefs/check-solved.md` | N4-N7 done, 10b97de (N4, N5 found-solved; N6 open campaign; N7 partial); N8-N11 done, 48422b8 (N8 open; N9-N11 dropped); N12-N15 done, 5164145 (N12 found-solved; N13-N15 open at stage 2); N16-N19 open |
| 12 | 23 Sept | cipher-lab | Draft REQUEST.md for SP 90/2 (1704), SP 87/13 (1743), SP 87/23 (1747) TNA copy orders from their NOTES.md; check Basil Williams, Carteret and Newcastle, and Dobrée's Chesterfield vol. 2 via an IA loan if IA_USER/IA_PASS work in that session | any | `.claude/briefs/archive-lookup.md` | open |
| 13 | 23 Sept | cipher-lab | Score the remaining 474 non-DECODE survivors (sources/solver-diffs/2026-09-23-non-decode-hits.tsv) with item details pulled for every TNA hit; add N20-N40 to QUEUE.md | any | `.claude/briefs/scout.md` | open |
| 14 | 23 Sept | cipher-lab | Scout of digitised-manuscript catalogues not swept by the solver projects (BnF Archives et manuscrits with Gallica images, Folger, Beinecke, LOC, Wellcome, Bodleian, CUDL, Leiden, KB): cipher items whose images are free online, excluded by volume against both solver repos | any | `.claude/briefs/scout.md` | claimed, noautopilotytbiz, 23 Sept 2026 19:40 UTC |
| 15 | 23 Sept | cipher-lab | Sforza-Maino 1446: sign-exact re-transcription of ff.68 and 70 from the Gallica image if digitised, then rerun run_target.sh against the existing controls | any | `.claude/briefs/transcription.md`, then the solver's run_target.sh | claimed, noautopilotytbiz, 23 Sept 2026 19:40 UTC |
| 16 | 23 Sept | cipher-lab | Bowes 1583: find CSP Scotland vi pp. 370-371 in running text (any free scan) to settle N0 vs N1; append to AUDIT.md | any | verifier follow-up | claimed, noautopilotytbiz, 23 Sept 2026 19:40 UTC |
