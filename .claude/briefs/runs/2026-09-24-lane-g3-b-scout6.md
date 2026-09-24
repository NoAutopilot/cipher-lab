# LANE G3 worker B: Gallica scout round 6, archivesetmanuscrits pages past 1 with a real browser (Sonnet, cap $5, archivesetmanuscrits fetcher)

Read .claude/briefs/scout.md, QUEUE.md 'Fifth pass' section and sources/solver-diffs/2026-09-24-lane-g2-gallica5.tsv (round 5: nine century
buckets, page 1 only, 25 kept, all duplicates; pagination past page 1 answers ERREUR RESULTATS for curl on both search endpoints).
Job: with `NODE_PATH=$(npm root -g) node tools/browser_fetch.js` (see its --help; one browser, one page at a time, >= 3 s apart), page through
archivesetmanuscrits.bnf.fr results for the capped terms 'chiffre', 'en chiffre', 'avec chiffres', 'en chiffres', 'déchiffrement', in the
century buckets round 5 used (control: clair1067 must appear). Pages 2 onward only; stop a term when a page adds no unseen ark, and stop the host
on any challenge page after one retry. At most 150 requests on the host.
Filter with round 5's noise rule and drop: anything already in QUEUE.md/CATALOG.md/ciphers/, fr.3xxx wholesale exclusion, 'déchiffrement'-only
items with no ciphertext named, register copies, Arsenal items not digitised. For each survivor record: shelfmark, folio, date, sender,
recipient, language, catalogue wording, Gallica ark if digitised (one SRU or item-page lookup), and whether ciphertext is on the leaf.
Write survivors as new M rows in QUEUE.md 'Sixth pass (LANE G3, 24 Sept 2026)' and QUEUE-scores.json (rebase first), full table in
sources/solver-diffs/2026-09-24-lane-g3-gallica6.tsv. Do not check-solved, do not promote, do not capture. Zero survivors is a valid result:
say so with counts per term and page.
