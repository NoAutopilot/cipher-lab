blocked
Corrected by the LANE DX orchestrator, 25 Sept 2026 01:35 UTC (check-solved.md: an edition this worker could not open makes the verdict `blocked`, not `open`): Tomokiyo 2018 and Galende Díaz 1993-94 both located, neither read. Next: a fresh worker reads them (cryptiana.web.fc2.com, other mirrors), and the DX login worker fetches R1172/R1180.
This worker's own DECODE catalogue mirror read directly (`sources/decode/records-decrypted-2026-09-24.tsv`, `sources/decode/records-non-decrypted-2026-09-24.tsv`); no print edition opened this pass -- Tomokiyo's 2018 paper (academia.edu) and Galende Díaz 1993-94 (digibug.ugr.es) were both located but blocked, see search log.

# Ferdinand (the future Ferdinand II of Aragon) to his father John II of Aragon, BNE MSS/20211, 1478 — QUEUE.md row D5

DECODE ids (row D5): R1172 / R1180.

## Verdict: open, strong sibling-crib lead, unclaimed by either solver repository

R1172 and R1180 mapped from this worker's own local DECODE mirror (`sources/decode/records-*.tsv`, not
Aymeloglu's catalogue):

- **R1172** = Madrid, National Library of Spain, MSS/20211/123, date range "1478 -", **Non-decrypted**,
  cleartext_lang Spanish, plaintext_lang blank.
- **R1180** = Madrid, National Library of Spain, MSS/20211/126, date range "1478 -", **Decrypted**,
  cleartext_lang Spanish, plaintext_lang Spanish.

BNE's own public catalogue (via Aymeloglu's `catalogue/bne-ranked.md`, a repository digest, cross-checked against
his `CATALOGUE.md`) identifies item /123 as "Carta del rey Fernando el Católico a su padre, el rey Juan II de
Aragón, Córdoba 4 noviembre 1478" and item /126 as "...Trujillo, 4 diciembre 1478" — 26 days apart, same
correspondent pair, matching DECODE's own Non-decrypted/Decrypted split exactly. His `CATALOGUE.md` (line 82)
states the wider context: **thirteen** Ferdinand-to-Juan-II letters at this shelfmark (1470-1479), of which
**ten already carry a contemporary "cifra interlineal"** (interlinear decipherment, bound on the manuscript
itself) and only **three are "parcialmente cifrada" and unread**: item /56 (Dueñas, 12 Nov 1470), item /98
(Bilbao, 5 Aug 1476), and **item /123 (Córdoba, 4 Nov 1478) — i.e. R1172, this cluster's own target**. This
worker did not independently open BNE's catalogue page to re-verify the "cifra interlineal" wording (attempted
below, blocked); the Non-decrypted/Decrypted split itself, which is the load-bearing fact for scoring this
recovery, is confirmed independently from our own DECODE mirror as shown above, not from his file.

If Aymeloglu's reading of the catalogue notes is right, this is the strongest possible recovery shape (LESSONS.md
§"Look for the sibling"): not one adjacent Decrypted neighbour but **ten** contemporary interlinear decipherments
of the same correspondent's hand across the same nine-year span, of which R1180 (26 days after the target) is
one. Neither solver repository has a folder for it: Bourdeau's clone has no Ferdinand-1478/BNE-20211 entry
(his `ferdinand-1634`/`ferdinand-1635-1640` folders are a different, 17th-century Ferdinand); Aymeloglu's own
`bne-ranked.md` lists it as scored material, not yet opened as a target folder.

## Search log (25 Sept 2026)

1. Bourdeau: fresh shallow clone, grepped "20211", "MSS/20211", "Ferdinand.*1478", "Juan II"/"John II" — no hit
   outside the unrelated 17th-century Ferdinand folders.
2. Aymeloglu: fresh shallow clone. `catalogue/bne-ranked.md` and `CATALOGUE.md` give the item-level breakdown
   quoted above; no target folder exists for it (top-level dirs checked: forster-1644, ferdinand-1634,
   starhemberg-1758, vande-perre-1653, ottobon-1589, ferdinand-1635-1640, moray-1568, royalist-1646,
   burgess-1912 — none match).
3. Print: QUEUE.md flagged "Spanish Ciphers before Accession of King Ferdinand: 1470-1479" (S. Tomokiyo, 2018,
   academia.edu/37751652) as worth reading first. Attempts this pass: WebFetch on the academia.edu URL -> HTTP
   403 (matches CLAUDE.md's known academia.edu-blocks-WebFetch note). Wayback Machine CDX lookup found an
   archived copy (`web.archive.org/web/20240710055134/...`), but both WebFetch and a direct curl fetch of it
   failed (WebFetch: "unable to fetch from web.archive.org"; curl: connection reset via the agent proxy) —
   matches the known session-level web.archive.org egress block logged elsewhere in LESSONS.md 24 Sept 2026.
   One retry each, per the good-citizen rule; stopped both hosts after that. `sources/cryptiana/PAPERS.tsv`
   already carries a row for this exact paper, noting no htm mirror exists on cryptiana.web.fc2.com, but flags a
   related article, `sources/cryptiana/web/eleanor1476.htm` (Tomokiyo, 2025, on a different BRAH cipher between
   Eleanor of Navarre and John II), which cites the 1470-1479 paper by name and also cites Galende Díaz
   (1993-1994), "La escritura cifrada durante el reinado de los Reyes Católicos y Carlos V"
   (digibug.ugr.es/bitstream/handle/10481/30410/...pdf) as an even earlier print source for the same subject.
   Fetched that PDF: WebFetch and a direct curl both returned HTTP 504 (server timeout); one retry, stopped.
   Neither paper's actual content on items /56, /98 or /123 specifically was read this pass — the "ten
   deciphered, three not" claim above rests on Aymeloglu's CATALOGUE.md, not on this worker independently
   reading either paper.
4. Attempted BNE's own public catalogue directly (catalogo.bne.es discovery pages for items /123 and /126, URLs
   from Aymeloglu's bne-ranked.md): both WebFetch calls returned an empty page (the discovery interface is a
   JS-rendered Ex Libris Primo/Alma front end; WebFetch's HTML-to-markdown conversion got nothing usable). Not
   retried with a browser tool this pass (cap).
5. Community: WebSearch for the paper's title and for "Ferdinand" + "John II" + "cipher" + "1478" turned up only
   the paper itself, Wikipedia biographical pages, and the Cryptiana 2018 forum-index page (not opened
   individually). No Cryptiana blog post or Cipherbrain thread specific to MSS/20211 found. `sources/decode/
   NOTES.md` carries no mention of R1172 or R1180.

## What a recovery worker would need

The DECODE login worker to fetch R1180's decipherment (item /126, Trujillo 4 Dec 1478) as the crib, plus R1172
itself (item /123, the target) and, if the ten-deciphered claim holds, the other eight Decrypted siblings for a
larger, more robust key (item /56 and /98's own DECODE ids were not looked up this pass — a next step, not done
here). Independently opening BNE's own catalogue page (a real browser, not WebFetch, given the JS front end) or
Tomokiyo's/Galende Díaz's papers by another route (Google Scholar cache, ResearchGate, a library copy) would
settle whether this is already written up, before any campaign spend.

Images: not fetched (no DECODE login; playbook forbids it for this role; BNE's own digitisation status for
MSS/20211 not checked this pass).

Hosts this pass: WebSearch 3, academia.edu (WebFetch) 1 (403), web.archive.org (WebFetch 1 + curl 1, both
failed/blocked), digibug.ugr.es (WebFetch 1 + curl 1, both 504), catalogo.bne.es (WebFetch 2, empty render),
github.com 2 shallow clones (shared with D2/D3/D8, grep only, not counted twice).

## DECODE fetch, 25 Sept 2026

LANE DX job 2 (the one DECODE login worker), one login shared with `ciphers/intercepted-royalist-1646` (record
8725), `ciphers/boswell-1628` (record 413) and `ciphers/randolph-sussex-1569` (record 4930) —
`tools/decode_browser_login.js`, `--fetch-page /decrypt-web/RecordsView/1172,/decrypt-web/RecordsView/1180`,
`--guess-fullsize`. Both records confirmed against this worker's own DECODE mirror figures above.

**RecordsView/1172 fields (real content):** ID 1172, Name `NLS_MSS_20211_123` (DECODE's own "NLS" prefix,
despite the City field reading "National Library of Spain, MSS/20211/123" — not National Library of Scotland;
report literally), Country Spain, City Madrid, Author Ferdinand V, Receiver King John II of Aragon, Type Cipher,
**Status: Non-decrypted**, Cipher Type Homophonic substitution, Symbol Sets Alphabet, Graphic signs, Pages 2,
Creation Date 2019-08-26, Cleartext Spanish, Plaintext blank, Created by `lehoanna`.

**RecordsView/1180 fields (real content):** ID 1180, Name `NLS_MSS_20211_126`, Country Spain, City Madrid /
"National Library of Spain, MSS/20211/126" / "Trujillo" (matches the "Trujillo, 4 diciembre 1478" catalogue
description above), Author Ferdinand V, Receiver King John II of Aragon, Type Cipher, **Status: Decrypted**,
Cipher Type Homophonic substitution, Symbol Sets Graphic signs, Numerical, Pages 2, Creation Date 2019-08-26,
Cleartext Spanish, **Plaintext Spanish** (DECODE's own field says a Spanish plaintext exists, but the attached
document itself is placeholder-blocked below), Created by `lehoanna`.

| file | bytes | sha1 | content |
|---|---|---|---|
| record_1172.html | 120883 | dd9e81f7e6d72848cab7021779d5084f9f3d6f9a | real (RecordsView metadata, scrubbed) |
| record_1180.html | 121502 | 7f17cfa55d17b4424a28349aa577eb4e1a040c1e | real (RecordsView metadata, scrubbed) |
| TH_IMG_R1172_I5878_P1.png | 118326 | cfcb3ae96be665e4c852828bf7dc58b1de0618b5 | real thumbnail |
| TH_IMG_R1172_I5879_P2.png | 80518 | c88b99561ac6fedf319bce58f5ce8145db313dbb | real thumbnail |
| TH_IMG_R1180_I5897_P1.png | 111985 | 4c22b4af522d8d9d73362a2f65d9e7bcb639de87 | real thumbnail |
| TH_IMG_R1180_I5898_P2.png | 45794 | cf7b359beed66d900fd77f2f825f99d6d93e19f9 | real thumbnail |
| TH_IMG_R1180_I5899_P3.png | 73377 | fcb5bb568289c7830fefb5ced88ef7b1e644a947 | real thumbnail |
| IMG_R1172_I5878_P1.png, IMG_R1172_I5879_P2.png, IMG_R1180_I5897_P1.png, IMG_R1180_I5898_P2.png, IMG_R1180_I5899_P3.png | 17947 each | 035489a0605851154ab88372216354b63596ca22 | **placeholder** ("Insufficient permissions to see the full image") for every full-size page of both records |

Same account-wide block already documented for record 8725 (`ciphers/intercepted-royalist-1646/NOTES.md`):
metadata is readable, full images and R1180's plaintext document are not. R1180's DECODE-recorded Spanish
plaintext therefore cannot yet be read or quoted from this account — the crib this target needs (LESSONS.md
"Look for the sibling") exists on DECODE but is not accessible without a role upgrade
(`outreach/decode-image-access.md`, sent 24 Sept 2026, reply pending) or the BNE catalogue image route (still
blocked per the search log above). Not classifying novelty (rule 10); not a solver step, out of this worker's
brief.
