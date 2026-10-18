# Research director, wave 16 (18 Oct 2026, 08:1x UTC by date -u): key application, Cossit/Summer cypher from Entick 1781

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, `tools/experiment_log.py --check`). The job ends its NOTES section with the six research-director questions in one
line each. Report what was found and where it was not found; no novelty class (rule 10). Credit Entick (the book), and say the
identification of the book and the reading are ours (key: ours, codebook identified).

## JOB SHERWOOD-READ (account 4; Opus 5.5; cap USD 9; box 75 minutes; hosts: archive.org (11280377bsb only: djvu.xml, page_numbers.json, page images through the IIIF/BookReader image URLs, at most 60 requests, 1.5 s apart); Price: vision calls: 12 x USD 0.5 + 1 reconciliation = 6.5)

SHERWOOD-BOOK (ciphers/sherwood-cossit-1781/NOTES.md "## Code-book identification") identified the code book as John Entick, *The New
Spelling Dictionary* (1781), archive.org 11280377bsb: 12 anchors at mean page error 0.58 vs a shuffled control at 104.2, and the book's
last page, 472, equals the cipher's top first figure. Open question: what W counts (W runs 1-38; page 364 OCRs to about 59 lines in two
columns). The cipher is ciphertext.tsv (214 P-W groups, BL Add MS 21838 pp.345-347). Sherwood's own paraphrase of the four messages is in
NOTES.md (p.84-85).
Scripts read, models judge (Usage 2): the OCR (djvu.xml, with word coordinates) gives each page's entries and columns; vision calls only
settle the convention and the cases the OCR cannot.
1. Convention, as a gate: fetch the page images for the convention anchors -- 138 (February, the one C-grade anchor, W 28), 364 (the 32,
   them 1), 246 (of 35), 240 (new 12), 409 (was 6), 331 (sleigh 36), 371 (towards 21) -- and work out the rule (W per column, per page,
   main headwords only, counted from the top or from the first headword, etc.). Use crops of the column, not full pages
   (`tools/iiif_lines.py --image FILE --region ... --out DIR`, paste the command). State the rule and how many of the 8 anchors it
   satisfies. Gate: if no single rule fits February and at least 5 of the other 7, stop, log the candidates and their counts, and do not
   decode (rule 3, a non-fitting convention is not a reading).
2. If the gate passes: write ciphers/sherwood-cossit-1781/decode_entick.py, which builds a page->entry list from the djvu.xml (cached
   under the folder's own book/ subdirectory, under 30 MB, or re-downloaded on demand), applies the rule to every group in
   ciphertext.tsv, writes reading.tsv (group, page, W, entry, grade) and reading.txt, and has `--check` (rule 7). Grades: H where the entry
   is read from the book (OCR confirmed, or the image where the OCR was unclear); M where the OCR entry is uncertain and was not
   image-checked; the period gloss "February" stays C. Spend the remaining vision calls on the OCR-uncertain entries, most-used first.
3. Matched control (rule 3): the same script with W offset by +1 and by -1, and with P shuffled across the groups (20 seeds), reporting the
   share of the decoded stream that forms grammatical English word sequences (use `tools/judge_plaintext.py` with the en18 corpus on the
   reading and the controls, and paste the output, rule 7). Then compare the reading with Sherwood's paraphrase message by message:
   agree / differ / Sherwood unread.
4. NOTES.md "## Reading from Entick 1781 (SHERWOOD-READ, 18 Oct 2026)": the convention and its anchor count, the reading per message
   with grade counts (H/C/S/M/I), the judge output for the reading and controls, the comparison with the sketch, and what is still unread.
   Do not call the reading new or first (rule 10).
Report: convention and gate result, grade counts, judge vs controls, the sketch comparison in one line, five lines.
