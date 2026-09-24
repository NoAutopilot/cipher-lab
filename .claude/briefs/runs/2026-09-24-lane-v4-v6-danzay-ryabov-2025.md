# LANE V4 verifier V6: Ryabov 2025 on Danzay's diplomatic cipher versus our f.35-36 reading (Opus, cap $10)

Common rules: `.claude/briefs/runs/2026-09-24-lane-v4-common.md`. Target: ciphers/fr20140-danzay-1557 (Danzay to the Cardinal
of Lorraine, Copenhagen, 27 Jan 1557, BnF fr.20140 f.35r-36r), class N4 in AUDIT.md ("N4 decision (Cryptiana closed)"), read
with Tomokiyo's 2026 key reconstruction. The OpenAlex API (with the owner's key, 24 Sept 2026 17:50 UTC) returned:
Sergey M. Ryabov, "Secrets of the Foreign Policy of the Last Valois in Northern Europe: The Diplomatic Cipher of Charles de
Danzay", Quaestio Rossica 13/4 (2025) pp.1487-1508, doi 10.15826/qr.2025.4.1034, open access (the issue's contents PDF is at
elar.urfu.ru/handle/10995/147661; the article PDF is on the same repository or the journal site qr.urfu.ru). V3b read
Ryabov's dissertation today (0 hits for fr.20140); this article is later and specific to the cipher.

1. Fetch the article once (journal site, then elar.urfu.ru; one host at a time; save to your scratch dir, not the repo).
   Read it in full (it is Russian with an English abstract; read the Russian). Extract: which Danzay letters it treats
   (shelfmarks, dates), whether it prints a key or table, whether it prints or paraphrases any decipherment, whether it
   cites fr.20140 f.35-36 or the 27 Jan 1557 letter, whether it cites Tomokiyo, and its own sources.
2. Compare with our reading (reading files and key.tsv in the folder): same key? same letter? overlapping plaintext?
3. Classify f.35-36 again on the evidence: N0 if it deciphers this letter; N1 if it prints the plaintext; N2/N3/N4 as rule
   10 defines; write the evidence, safe and unsafe sentences, and a "Ryabov 2025" section in AUDIT.md; correct the results
   row in status.json only if the class changes; add the citation to NOTES.md sources. Also note whether the article's key
   agrees with Tomokiyo's (a credit question for the outreach note, not a class question).
4. Whatever the class, set outreach/tomokiyo-gramont-danzay.md's status line to record the outcome (still `drafted` until
   the three JSTOR READ rows are answered) and, if Danzay is reclassed, rewrite its Danzay paragraph in rule 10 wording or
   drop it. Update CONTRIBUTIONS.md row for the draft. Mark ASKS.md row 44's open-index queries as done from the cloud with
   the OpenAlex key (six queries; one relevant hit, this article).
5. ROOM done line `for LANE V4: Danzay f.35-36 vs Ryabov 2025 -- <class>, <one clause>`; one-paragraph report.
Do not decode. Never write the owner's name. Never print the OpenAlex key (it is OPENALEX_KEY in the environment; pass it
as the api_key query parameter only).
