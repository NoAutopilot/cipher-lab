open
Galende Díaz 1993-94 (Cuadernos de Estudios Medievales y CC.TT.HH. XVIII-XIX, 1993-94, pp.159-178) read in full
by this worker, 25 Sept 2026 (OCR text and the original PDF, both already on disk in dbourdeau/cyphersolver's
`esp318/lit/galende1994.{txt,pdf}`, cross-checked against Dialnet record 255134 for the same article/journal/page
range) -- footnote 5 names only BNE mss. 20211/56 (Dueñas, 12 Nov 1470) and mss. 20211/73 (Zaragoza, 3 Nov 1474)
at this shelfmark, neither of which is item /123 or /126; Tomokiyo 2018 (academia.edu/37751652) opened by this
worker via a real headless browser, past the previous session's WebFetch/curl 403 -- its public abstract, "key
takeaways" and references sections read directly, the 6-page body still gated behind an academia.edu account/
download (not attempted; no credential for that site in the playbook).

# Ferdinand (the future Ferdinand II of Aragon) to his father John II of Aragon, BNE MSS/20211, 1478 — QUEUE.md row D5

DECODE ids (row D5): R1172 / R1180.

## Verdict: open, strong sibling-crib lead, unclaimed by either solver repository; neither located edition read this
## far deciphers item 123 or 126

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
again this pass, still blocked — see Search log §4); the Non-decrypted/Decrypted split itself, which is the
load-bearing fact for scoring this recovery, is confirmed independently from our own DECODE mirror as shown
above, not from his file.

If Aymeloglu's reading of the catalogue notes is right, this is the strongest possible recovery shape (LESSONS.md
§"Look for the sibling"): not one adjacent Decrypted neighbour but **ten** contemporary interlinear decipherments
of the same correspondent's hand across the same nine-year span, of which R1180 (26 days after the target) is
one. Neither solver repository has a folder for it: Bourdeau's clone has no Ferdinand-1478/BNE-20211 entry
(his `ferdinand-1634`/`ferdinand-1635-1640` folders are a different, 17th-century Ferdinand; his `esp318/`
folder, on BnF Espagnol 318, covers a distinct, later cipher run of the same office, 1497-1504, see §"Print
check" below); Aymeloglu's own `bne-ranked.md` lists it as scored material, not yet opened as a target folder.

## Print check (25 Sept 2026, this worker) — the two named editions, read directly

**Galende Díaz 1993-94**, read in full (all 439 OCR'd lines of the article body, footnotes and appendix
description; the article itself does not print a full transcription of any cipher key relevant to 1478). Its
footnote 5, the passage cited by both Tomokiyo's paper and `sources/cryptiana/web/eleanor1476.htm` as covering
early Ferdinand-John II ciphers, reads in the original (digibug pagination, page 159-160):

> "...en la Biblioteca Nacional se conservan dos cartas de Fernando el Católico a Juan II de Aragón; una fechada
> en Dueñas el 12 de noviembre de 1470, en la que le comenta temas tales como el restablecimiento del propio
> Juan II después de una enfermedad, su obediencia al arzobispo de Toledo Alonso Carrillo o la remisión de una
> misiva del doctor Mastre Lorenzo Badoz (mss. 20211/56), y otra, entre los mismos corresponsales, sobre el
> casamiento de su hermana Juana, fechada en Zaragoza el 3 de noviembre de 1474 (mss. 20211/73)."

That is the entire MSS/20211 content of the footnote: items **/56** and **/73** only. Item /123 (Córdoba, 4 Nov
1478, R1172) and item /126 (Trujillo, 4 Dec 1478, R1180) are **not named anywhere in the article** — checked by
grep of the full OCR text for "1478", "Córdoba", "Trujillo", "20211" and "John II"/"Juan II" (all hits shown
above or in the BRAH list below). The footnote's BRAH list separately names a 3 December 1478 letter from Nápoles
by the Master of Montesa, Luis Despuig, to the Catholic Monarchs (BRAH 9/7 fol. 236) — a different sender,
recipient and archive from R1180, coincidentally the same year; not to be confused with it. (Flag for whoever
finalises Aymeloglu's "thirteen letters" count: Galende names /73, dated 1474, as a second early Ferdinand-John
II item at this shelfmark, which does not appear in the /56, /98, /123 trio quoted from his `CATALOGUE.md` above
— either /73 is one of the ten already-deciphered letters, or the two catalogue digests disagree; not resolved
this pass.) The article's appendix describes the later **"Cifra general de los Reyes Católicos"** (BRAH 9/15,
c. 1500) in detail — the key Bourdeau's own `esp318/` folder uses for a different, 1500-dated letter — but
Galende does not tie that or any other printed key to a letter of 1478.

**Tomokiyo 2018**, opened directly (not just cited) via `tools/browser_fetch.js` this pass, which got past the
403 that stopped WebFetch and curl on this same URL in the previous session. Academia.edu serves the abstract,
"key takeaways" and references sections to an anonymous visitor but gates the 6-page PDF body behind a free
account signup ("Download Free PDF" → `/trial/pdf_pack/37751652`); that step was not taken (no academia.edu
credential in the playbook, and creating an account is outside this worker's brief). What is readable:

> "The present article describes several ciphers Ferdinand used before his accession in his letters to his
> father, King John II of Aragon in the 1470s." ... "Four distinct ciphers have been reconstructed from
> Ferdinand's letters to King John II of Aragon." ... "Cipher (1470) and Cipher (1476-1479) are significant for
> their representation of syllables." ... "despite perceptions of primitive ciphers, some employed extensive
> systems with over 500 entries, indicating significant cryptographic development by the late 1470s."

The paper's own references section states (this is Tomokiyo's own addendum, added after first posting the
article): "A few days after uploading this article, I found Spanish ciphers of the 1470s and earlier have been
described in footnotes 2 and 5 in Galende Diaz (1993-1994)... Specifically, of Ferdinand's letters treated
herein, those of 12 November 1470 and 3 November 1473 are mentioned" — i.e. Tomokiyo's own cross-check of
Galende Díaz against his four reconstructed ciphers turned up only the 1470 letter (matches /56 above; "3
November 1473" appears to be Tomokiyo's own slight misdate of Galende's "3 de noviembre de 1474" = /73). Neither
Tomokiyo nor Galende, on this account, connects Galende's article to Ferdinand's 4 Nov or 4 Dec 1478 letters.

**What is not settled**: whether Tomokiyo's fourth reconstructed cipher, "Cipher (1476-1479)" — a syllable
cipher with "over 500 entries", the right date window for both R1172 (4 Nov 1478) and R1180 (4 Dec 1478) — was
built from item /123, from item /126, from other letters in the run, or from some other source entirely (e.g.
Bergenroth's 19th-century transcriptions, which the paper's reference list also cites via Calendar of State
Papers, Spain vol.1). If it was built from R1172 or R1180 specifically, this target is already keyed and this
worker's own "open, unclaimed" framing above would need correcting. The paper's visible preview does not name a
shelfmark or a specific letter date for "Cipher (1476-1479)", so this cannot be settled without the full text.

## BNE catalogue / digitisation check (attempted again, still inconclusive)

`bdh.bne.es` (Biblioteca Digital Hispánica) 403s outright — confirmed both by a plain curl test this pass and by
a cached Cloudflare-challenge page already sitting in Bourdeau's own `esp318/lit/bne_q.html` for the identical
query ("MSS/20211"), so this is a standing site-wide block, not a one-off. `catalogo.bne.es`'s discovery search
(a JS-rendered Ex Libris Primo/Alma front end) returns HTTP 200 but the page never finishes loading its AJAX
results within the browser tool's default wait (screenshot shows only a loading spinner after render) — same
failure mode as the previous session's plain WebFetch attempt, now confirmed with a real browser too. Digitisation
status for MSS/20211 items 123 and 126 remains unknown; not investigated further this pass (BNE catalogue access
is a bigger sub-problem than this job's budget covers — would need a longer `--selector`/wait-for-network-idle
pass or a different entry point, e.g. a direct record permalink if one can be found via web search).

## Search log (25 Sept 2026, this pass)

1. Dialnet (`dialnet.unirioja.es`): found Galende Díaz's article record (codigo=255134) by title search,
   confirming journal, volume (Nº 18-19, 1993-94) and pages (159-178); its own "Texto completo" link redirects
   to the same digibug.ugr.es URL, which 504'd again (3rd/4th attempt across two sessions) — stopped hitting that
   host, per the good-citizen rule's one-retry limit; used Bourdeau's already-fetched copy instead (rule 8: credit
   Bourdeau's `esp318/` folder for the OCR and the original PDF, MIT code / CC BY 4.0 text).
2. Semantic Scholar (`api.semanticscholar.org`, keyed): found the same Galende Díaz record (paperId
   a6f7237aaf38c7dcc84e830a0b76d6addba991c5) confirming author, year, no open-access PDF (points at the same
   digibug URL). OpenAlex (keyed) found no record for it at all (search and title-filter both zero hits) — the
   journal is evidently not indexed there.
3. `cryptiana.web.fc2.com`: fetched `crypto.htm` (the site's own index) and `spanish.htm` — confirmed no local
   htm mirror exists for the 1470-1479 paper (matches `sources/cryptiana/PAPERS.tsv`'s existing note) and no
   other cryptiana page mentions MSS/20211, item /123 or /126.
4. `academia.edu`: fetched the Tomokiyo 2018 paper's page directly with `tools/browser_fetch.js` (past the
   403 that blocked WebFetch/curl previously) — content quoted above. A second academia.edu URL (a related 2024
   paper, "Deciphering Historical Syllabic Ciphers", surfaced by WebSearch as a possible fuller treatment) hit a
   Cloudflare "Just a moment..." interstitial on the second request to that host this session — stopped there
   per the one-request-at-a-time/one-retry rule, not pursued further.
5. `catalogo.bne.es` (browser) and `bdh.bne.es` (curl): see "BNE catalogue" section above.
6. Re-cloned `dbourdeau/cyphersolver` (shallow) specifically to grep for "20.211" (period-separated) and
   date/correspondent patterns the previous pass's plain "20211" grep might have missed — this surfaced the
   `esp318/` folder (a different target, BnF Espagnol 318) which happens to hold both editions' texts already
   fetched, cited under "Print check" above; still no dedicated Bourdeau folder for this BNE MSS/20211 target
   itself.
7. Community/repository re-checks from the previous pass (Bourdeau/Aymeloglu grep, WebSearch for the paper
   title, no Cryptiana blog or Cipherbrain thread specific to MSS/20211) stand; not repeated.

## Recovery route (do not decode; for a solver session)

1. The DECODE login worker fetches **R1180** (item /126, Trujillo, 4 Dec 1478 — Decrypted, the crib) and
   **R1172** itself (item /123, the target, Non-decrypted) into this folder's `decode/`. If Aymeloglu's
   "ten already deciphered" count for this run is right, the other Decrypted siblings across 1470-1479 are worth
   the same fetch for a larger key (their DECODE ids not looked up this pass).
2. Before spending solver time: get the full text of Tomokiyo 2018 (an academia.edu account/download, a library
   ILL, or asking Tomokiyo directly — he is an active, responsive researcher per his cryptiana blog) and check
   whether his "Cipher (1476-1479)" is keyed from item /123 or /126 by name. This is the single cheapest test
   that could close this target as found-solved instead of recovery — see "What is not settled" above.
3. Independently opening BNE's own catalogue (Cloudflare/Primo-blocked from this environment so far, both curl
   and browser) or its digitised-image viewer, if MSS/20211 is digitised, would settle both the "cifra
   interlineal" wording on item /123 and whether item /123 and /126's page images are already public — a
   longer, dedicated browser-automation pass than this job's budget covers.

## What a recovery worker would need (previous pass, superseded in part by "Recovery route" above)

Images: not fetched (no DECODE login; playbook forbids it for this role; BNE's own digitisation status for
MSS/20211 not settled this pass either, see above).

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

## Hosts this pass

dialnet.unirioja.es (curl) 3; api.semanticscholar.org (keyed) 2; api.openalex.org (keyed) 2; cryptiana.web.fc2.com
(curl) 2; digibug.ugr.es (curl) 2, both 504, stopped; academia.edu (browser_fetch.js) 2, one succeeded past the
prior 403, one hit a Cloudflare challenge, stopped; catalogo.bne.es (browser_fetch.js) 1, inconclusive
(JS-rendered); bdh.bne.es (curl) 1, 403; googleapis.com/books (keyed) 1; archive.org (curl, advancedsearch + be-api
full-text search) 2; github.com 1 fresh shallow clone of dbourdeau/cyphersolver (grep only, superseding the
previous pass's clone).

Hosts, previous pass (25 Sept 2026, kept for the record): WebSearch 3, academia.edu (WebFetch) 1 (403),
web.archive.org (WebFetch 1 + curl 1, both failed/blocked), digibug.ugr.es (WebFetch 1 + curl 1, both 504),
catalogo.bne.es (WebFetch 2, empty render), github.com 2 shallow clones (shared with D2/D3/D8, grep only, not
counted twice).
