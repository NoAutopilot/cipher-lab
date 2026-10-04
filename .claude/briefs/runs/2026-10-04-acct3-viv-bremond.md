# VIV-BREMOND (account 3 worker) -- 4 Oct 2026 18:4x UTC (account-3 orchestrator)
Target: ciphers/fr16104-vivonne-spain-1572 (readings of Saint-Gouard's letters, rule-10 N4 step pending). Lead (ROOM 18:18): Ribera 2007
note 18 cites "de Madrid, le 5 septembre 1572; BNF Fr. 16104; cité par G. de ..." -- likely Guillaume de Bremond d'Ars, Jean de Vivonne,
sa vie et ses ambassades (Paris, 1884). Job: a print check, not a decode, and not a novelty verdict.
1. Find the 1884 book (Internet Archive advancedsearch / Gallica SRU / HathiTrust bibliographic API). Full-text search it (IA djvu or
   be-api fts; Gallica texteBrut only if reachable) for the 5 and 7 Sept 1572 letters and 10 Oct 1573: every page citing or quoting a
   Saint-Gouard letter of those dates, quoted exactly with page, and whether the quoted words are the CIPHER passages our readings cover
   (compare against the folder's piece*_decode.txt and phrases_*.txt by script, not by eye).
2. Run tools/print_check.py on the folder if the book's text is on disk (sources.tsv entry). Record in NOTES.md (section "VIV-BREMOND")
   and update the verifier-facing Remaining gaps line; do not edit AUDIT.md classes (a verifier does that).
Good-citizen rule, <=40 requests per host. Model Opus 5.5. Cap USD 2.5, box 30 min. ROOM claim/done via tools/room.py.
Report what was found and where it was not found; do not classify novelty.
