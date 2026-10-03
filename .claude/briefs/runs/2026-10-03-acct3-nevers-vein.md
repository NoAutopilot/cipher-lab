# NEVERS-VEIN (account-3 orchestrator, 3 Oct 2026): scout the Nevers collection for letters whose key is already known

Scout only (Pipeline 1). Model Opus 5.5 (Sonnet allowed for page-through subagents). Cap $5, box 60 min.
The Birago vein worked because Tomokiyo published the keys (sources/cryptiana/web/nevers.htm, local mirror) and the
letters sat unread in the same BnF volumes. That page catalogues ~70 Nevers-collection keys (fr.3995 nos.1-70+) and,
under many of them, letters that use them -- several marked "undeciphered", "partially undeciphered" or "can be read
with this" (e.g. no.36: Henry IV to Nevers 1591, no.78 partially undeciphered; no.40 decodes Sillery to Nevers 25 July
1593, fr.3984 f.198; no.7's second fr.3976 letter "remains undeciphered but can be read with this"; no.13/no.23 Italian
letters in fr.4702 whose numbers "do not match").
1. Parse nevers.htm (script, not a model read): every (key no., letter shelfmark/folio, date, sender, recipient,
   Tomokiyo's status words) row.
2. Drop rows already in a ciphers/ folder (grep shelfmark+folio) or marked deciphered with a decipherment beside it.
3. For the rest: Gallica availability (SRU/IIIF canvas for the folio), est. cipher length from one low-res view,
   whether a clerk decipherment is visible on the leaf or facing page (premise (c) at low res; say "unchecked" if not).
4. Score by expected value (Pipeline 3: P(key opens it) x value / cost; pools first -- same key, many letters) and write
   QUEUE.md section "Nevers vein (3 Oct 2026)" + NEVERS-VEIN.tsv. Top 5 get a one-line first-test brief suggestion each.
No solving, no transcription, no class. Requests per host in the done line. Done line "for the account-3 orchestrator".
