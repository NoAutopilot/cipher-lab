# HATHI-UNLOCKS (account 3 worker) -- 4 Oct 2026 20:0x UTC (account-3 orchestrator)
Owner's ask (4 Oct): "Any others I can unlock like this?" -- i.e. full-view HathiTrust volumes (Cloudflare-blocked from the cloud, open
in the owner's browser) that print a cipher passage WITH its plaintext or key, like AOSB I:4 pp.341-342 (riksarkivet-r4282-1628).
Find the next ones; the owner reads them at his desk tomorrow.
1. Candidate volumes, by script: (a) every printed edition named in ciphers/*/NOTES.md, AUDIT.md, sources.tsv for open/partial targets
   (sender/recipient correspondences, state-paper calendars, Recueils, AOSB other volumes: ser. I and II via series OCLC 4445306);
   (b) resolve each to HathiTrust htids via the bibliographic API (full Chrome UA; Open Library -> OCLC where needed); keep full-view only.
2. For each full-view htid run tools/htrc_numeral_pages.py (EF API, no Cloudflare) to flag numeral-dense printed-cipher pages; also use
   EF per-page tokens to flag pages carrying "chiffre/chiffer/cifra/ziffer/cypher/déchiffr/klaven/Schlüssel" near numeral clusters.
   Respect >=1.5 s between EF calls, <=300 calls total.
3. Rank by value: a flagged page in an edition of a target's OWN correspondence/key family first (could give period key or known
   plaintext), then same office/decade. Drop false positives you can rule out from EF tokens (tables, indexes, accounts).
4. Write outreach/hathi-desk-reads-2026-10-04.md: one row per volume (target, why, htid, full babel URL
   https://babel.hathitrust.org/cgi/pt?id=<htid>&seq=<n> for each flagged scan seq, what to screenshot: page + footnotes zoomed,
   search-inside words to try). Top 5 at the top. No novelty claims. Commit; ROOM done line with the top 5 (target, htid, seq).
Model Opus 5.5. Cap USD 5, box 50 min. ROOM claim/done via tools/room.py. Report counts and the top 5 in a short paragraph and stop.
