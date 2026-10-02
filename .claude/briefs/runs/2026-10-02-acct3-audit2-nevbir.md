# AUDIT2-NEVBIR (account-3 orchestrator, 2 Oct 2026): second adversarial audit, nos.71, 86, 90

VERIFIER (rule 10, Outreach gate 2). Target ciphers/nevers-birago-fr3251-1572. Model Opus 5.5. Cap $6, box 60 min.
Claim under audit: the first-audit N3 sections in AUDIT.md for no.71 (f.139v, VERIFY-NEVBIR-139V), no.86 (27 Aug
1572, VERIFY-NEVBIR-86) and no.90 (f.184r, VERIFY-NEVBIR-184; plus NEVBIR-185's f.184v/f.185r portion, not yet
audited). You are a different session from every solver and first verifier; do not protect their conclusions.
Try to find each letter's plaintext or decipherment in print.

1. Mémoires de Nevers (Paris 1665, 2 vols): VERIFY-NEVBIR-86 searched vol. 1 on Gallica (ContentSearch) and could
   not locate vol. 2. Locate vol. 2 (Gallica SRU, archive.org advancedsearch, Google Books API with country=US and
   GOOGLE_BOOKS_KEY, HathiTrust bibliographic API) and search inside it for Birago 1572 letters, by date
   (27 Mar, 27 June, 29 July, 27 Aug, 2 Oct 1572), "Birague"/"Birago"/"Saluces" and 2-3 distinctive phrases from
   each reading. Log hosts and counts.
2. Run tools/print_check.py on the folder (phrases.txt from all three readings; add them if absent).
3. Append JSTOR-QUEUE.tsv rows per letter, both families: (i) Birago/Birague + Nevers + 1572 ANDed with a cipher
   keyword; (ii) a distinctive phrase quoted exactly from the reading, NO cipher keyword.
4. Open indexes (OpenAlex, Semantic Scholar, Persée, HAL, CrossRef): Birago/Birague, Nevers, Saluzzo 1572,
   Tomokiyo's Nevers papers; Italian scholarship on Lodovico Birago (Piedmont/Saluzzo 1570s).
5. Per letter in AUDIT.md: a "Second audit (AUDIT2-NEVBIR)" section: families searched/unreachable, class
   (N3/N4/lower), key source (published; T42 fit ours), safe sentence. N4 only if the principal editions
   (incl. Mémoires vol. 2) are covered. Update PROGRESS.tsv audit-2 column (x for each letter cleared) and the
   SECOND-OPINIONS-QUEUE rows if a class changes. file_shrink_guard before push.
Do not decode, do not touch other targets, do not print or commit credentials. Done line "for the account-3 orchestrator".
