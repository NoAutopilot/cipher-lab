# Research director, wave 15 (18 Oct 2026, 07:2x UTC by date -u): identify the Cossit/Summer code book

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, `tools/experiment_log.py --check`). The job ends its NOTES section with the six research-director questions in one
line each. Report what was found and where it was not found; no novelty class (rule 10).

## JOB SHERWOOD-BOOK (account 4; Sonnet 5; cap USD 4; box 50 minutes; hosts: archive.org (advancedsearch, metadata, _djvu.xml/_djvu.txt downloads, at most 40 requests, 1.5 s apart), books.googleapis.com (with &country=US and the key, at most 20); Price: vision calls: 0 x USD 0 = 0)

SHERWOOD-PAGES (ciphers/sherwood-cossit-1781/NOTES.md "## Pages and key-application test") found the Cossit/Summer cypher (BL Add MS 21838
pp.345-347, Feb 1783) is a P-W code ordered by spelling (P 4-472, W 1-38): Spearman rho 0.998 between first figure and alphabetical rank on
34 sketch-aligned words, against a permuted control of 0.003. That alignment is ours and an upper bound. Anchors, alignment grade M except
February (C, period gloss): Albany 10-34, alarmed 10-28, Colonel 65, council 81, destined 109, expect 131, from 131-22, February 138-28,
force 146, hearing 168, house 176, last 206, men 219, my 237, new 240, of 246-35, post 274, reduction 297, reported 301, said 312,
Saturday 315, sleigh 331-36, state 344, Strong 349, the 364-32, them 364-1, they 365-8, towards 371-21, Vermont 382, was 409-6,
Wednesday 411. Question: which printed book is it (page = P, word or entry on the page = W)?
Use scripts, not reading (Usage 2). `tools/ia_djvu_headwords.py` already locates headwords by scan and running head (built for the
Wellington dictionary code); extend it with an option rather than copying it (Usage 8).
1. Candidates: English dictionaries and spelling dictionaries in print before 1783 that a Loyalist officer could own, with archive.org
   scans: at least Bailey (Universal Etymological English Dictionary, several editions), Entick (New Spelling Dictionary, 1764 on), Dyche
   and Pardon, Johnson's abridged Dictionary (octavo), Fenning, Perry (Royal Standard), Sheridan (1780), Kenrick (1773), Dilworth, Buchanan.
   Different editions of one title paginate differently: score each scanned edition separately. Proper names (Albany, Vermont) may sit in
   an appendix or gazetteer: note where each title puts them.
2. Score: for each edition, the printed page holding each anchor word, then the mean absolute page error over the anchors, with the share
   within +-2 pages; for the best few, check whether W counts entries on the page (or per column) to the anchor. Matched control (rule 3):
   the same scoring with the anchors' page numbers shuffled among the anchors (100 shuffles), so a fit is not just a monotone page curve.
3. NOTES.md "## Code-book identification (SHERWOOD-BOOK, 18 Oct 2026)": a table of edition (IA id), page error, share within +-2, W fit,
   control. Name the book if one edition fits within +-2 pages on most anchors and beats its control; otherwise say what the curve implies
   (pages per letter) and the next candidate list. Do not decode the unaligned groups in this job: that is the next brief.
Report: best edition and its numbers vs control, or none, the next step, five lines.
