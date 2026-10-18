# Research director, wave 20 (18 Oct 2026, 12:1x UTC by date -u): sibling cypher letters of Cossit and Sumner

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, `tools/experiment_log.py --check`). The job ends its NOTES section with the six research-director questions in one
line each. Report what was found and where it was not found; no novelty class (rule 10).

## JOB SHERWOOD-SIB (account 4; Opus 5.5; cap USD 7; box 60 minutes; hosts: archive.org (Brymner 1888 djvu text; Fryer 1981 be-api search), heritage.canadiana.ca and image-uab.canadiana.ca (only frames named in step 2, at most 30 requests, 1.5 s apart); Price: vision calls: 6 x USD 0.5 + 1 reconciliation = 3.5)

ciphers/sherwood-cossit-1781 is `partial`: the Cossit/Sumner cypher of February 1783 (BL Add MS 21838 pp.345-347) reads from Entick's *New
Spelling Dictionary* (1781) by page and printed column line (decode_entick.py; AUDIT.md N3, D2). Its "## Siblings" section names the
next step: the same correspondents' other cypher letters in the same code.
1. List by script, not by reading pages: grep Brymner 1888's calendar text (archive.org `reportoncanadian1888publuoft`, already used) for
   every B.175-B.178 entry naming Cossit/Cossitt, Sumner/Summer, "cypher"/"cipher", or "Claremont", winter 1782-83 and 1783-84; and Fryer
   1981 (be-api full-text, `buckskinpimperne0000frye`) for her source notes on them (she cites B.175 pp.185-186, 30 Dec 1782). Write
   siblings/candidates.tsv (volume, page, date, Brymner's words, cypher flag).
2. Map each candidate page to its reel frame the way SHERWOOD-PAGES did (heritage.canadiana.ca series oocihm.lac_mikan_105513; H-1736
   holds Add MS 21835-21838; B.175 = Add MS 21835). Fetch only the cypher-flagged pages and any Sherwood sketch or decipherment beside
   them. Line crops with `tools/iiif_lines.py --image FILE --out DIR` (paste the commands); never a full frame to a vision call.
3. For each cypher page: transcribe the P-W pairs (two blind passes if more than 30 pairs; tools/reconcile_passes.py), add them to a
   siblings ciphertext file with the same conventions as ciphertext.tsv, and decode them with decode_entick.py (add an option to take
   another ciphertext file; keep `--check` working for both). Grade per token as the parent reading does; run the same W+-1 and P-shuffle
   controls on the siblings.
4. Then use what the siblings add: does any sibling repeat a group from No.2/No.3 where its own context fixes the column? List the M
   rows of reading.tsv that a sibling settles (both contexts quoted); do not change reading.tsv in this job, write the proposals to
   siblings/m_row_proposals.tsv for the next verifier. Note any second encoder one-line slip (the "Beyond" 33-35 question).
5. NOTES.md "## Sibling letters (SHERWOOD-SIB, 18 Oct 2026)".
Report: candidates found, cypher pages fetched, pairs decoded with grades and control numbers, M rows a sibling settles, five lines.
