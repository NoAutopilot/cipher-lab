# ILL-SWEEP (account 3 worker) -- 4 Oct 2026 19:xx UTC (account-3 orchestrator)
The owner now has a working public-library card (Washington County, Oregon; WCCLS interlibrary loan, no fee) and wants ONE batch of
interlibrary-loan requests rather than one at a time. Build that batch. Disk + light catalogue lookups only; no ordering, no emails.
1. Harvest candidates by script, not by reading folders whole: grep every ciphers/*/NOTES.md, AUDIT.md, REQUEST.md, ASKS.md (open rows),
   LOCAL-QUEUE.tsv (queued rows of kind edition-read / ia-reader / catalogue-lookup) and JSTOR-QUEUE.tsv for printed works that were
   "not opened", "no online copy", "snippet only", "NO_PAGES", "print-disabled", "lending-only", "not digitised" (book or article; not
   manuscripts -- those are archive copy orders, out of scope). Seed items known: Serrao 1969 (Arquivos do Centro Cultural Portugues 1,
   pp.455-458, OCLC 490240802; fr3151-seure-1558); Ribera 2007 Diplomatie et espionnage (note 139 + notes citing fr.16104;
   fr16104-vivonne-spain-1572); Falgairolle 1896 Le Chevalier de Seure; Flament 1996 (likely unlendable thesis -- say so); Daussy 2001
   (ASKS 26); Farnsworth 2010 The Adirondack Enigma (ASKS 98).
2. Keep only items where a specific page range or chapter would settle a named open question (a verifier's N4 step, a premise check, a
   key/decipher lookup). For each: full citation, OCLC number (WorldCat/Open Library API lookup, <=1 req per 1.5 s), exact pages or
   "chapter N" (ILL article/chapter scans are usually limited to ~1 chapter or 10% of a book), the question it answers, the target folder,
   and priority (A = could change a status or N-class; B = useful context; C = nice to have). Drop anything readable online already
   (check archive.org/HathiTrust bibliographic API/Google Books API with country=US).
3. Write outreach/ill-sweep-2026-10-04.md: a short intro, then a table sorted A->C, then per item a paste-ready request block (citation,
   OCLC, pages, "PDF scan please, private research"). No personal data, no card numbers. Commit + push; ROOM done line with counts by
   priority.
Model Opus 5.5. Cap USD 4, box 40 min. ROOM claim/done via tools/room.py. Report counts and the A-list in a short paragraph and stop.
