partial
Check-solved basis (head rewritten 5 Oct 2026 by FER1478-READ from sections already below, intake-gate fix only): Galende Díaz 1993-94 (Cuadernos de Estudios Medievales XVIII-XIX, pp.159-178) read in full 25 Sept 2026 -- names only items /56 and /73; Tomokiyo 2018 (academia.edu/37751652) read in full 5 Oct 2026 from the owner's download (section "Tomokiyo 2018 read" below) -- prints a reconstructed key (Fig. 4) built partly from item 123 but no decipherment or plaintext of item 123 or 126. Neither edition deciphers the letter; the earlier `blocked` (Tomokiyo body not yet opened) is lifted by that read.
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

1. **Done, partially blocked**: the DECODE login worker already fetched R1180 and R1172 into `decode/` (see
   "DECODE fetch" below) — metadata confirms the crib shape, but the actual page images and R1180's plaintext
   document are placeholder-blocked account-wide ("Insufficient permissions"), same block as record 8725. A
   role upgrade (`outreach/decode-image-access.md`, reply pending) or the BNE image route is needed before the
   crib can actually be read. If Aymeloglu's "ten already deciphered" count for this run is right, the other
   Decrypted siblings across 1470-1479 are worth the same fetch for a larger key (their DECODE ids not looked up
   this pass) once images are reachable.
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

## Desk runner, 27 Sept 2026

LOCAL-QUEUE row L22 (ASKS row 45): a run from ChatGPT's remote cloud browser (not the owner's own machine,
despite the row's prescribed runner label) reached academia.edu/37751652 (Tomokiyo, "Spanish Ciphers before
Accession of King Ferdinand: 1470-1479") and was held at the site's Cloudflare "Performing security
verification" challenge for the whole attempt -- an access failure, not a negative finding about the paper.
The "Cipher (1476-1479)" section and any item-123/item-126 source attribution remain unread; no login
interface was reached and no credential was used. Row set `done 2026-09-27` as an exhausted attempt, not a
found-solved or ruled-out verdict -- target status stays `blocked` (ASKS row 45 unresolved).


## Web and blog check (CS-A2-M, 3 Oct 2026)
Plain searches (WebSearch, 8 queries): (1) "Spanish Ciphers before Accession of King Ferdinand" 1470-1479 Tomokiyo -> only Ferdinand II 1502/1506 Gran Capitan coverage (scienceblogs.de 3 Feb 2018, Fox, Olive Press), nothing on 1478; (2) Fernando Juan II Cordoba 4 noviembre 1478 cifra MSS/20211/123 -> no hit on the item (UCM autograph-letter paper, unrelated); (3) Ferdinand 1478 John II cipher syllable Tomokiyo -> same 1502/1506 stories; (4) "20211" BN Trujillo 4 diciembre 1478 -> Galende Diaz 1993-94 footnote 5 (items /56, /73 only) and unrelated journals; (5) Tomokiyo 1470s letters on cryptiana domains -> Cryptiana 29 Nov 2018 post and Catherine of Aragon post, no item numbers; (6) Ferdinand John II 1478 BNE on scienceblogs.de/ciphermysteries.com -> Ferdinand II 1502/06 (Bergenroth 1862, CNI) and Ferdinand III (Ernst) only, Cipher Mysteries nothing. Blogs: Cipherbrain (scienceblogs.de) and Cipher Mysteries searched by site restriction, no post about MSS/20211; Cryptiana blog 2018 archive opened: the post of 29 Nov 2018 quotes the abstract only, "3 comments" present but their text did not come back from the fetch, so comment threads are unread. Quoted sentence about the target family (Cryptiana 2018): "Spanish ciphers before 1480 are found in archives" and "Two of them turned out to be rather complex" -- no shelfmark, no 1478 date. Model-solve search (name + "solves"/"Claude"): nothing found.
Other routes: Wayback CDX for academia.edu/37751652 -> 3 captures, landing page only; cryptiana.web.fc2.com guess URL 302; Google search page unusable; catalogo.bne.es Primo REST for the /123 record (docid alma991044178389708606) HTTP 400, availability flag not obtained.
DECODE (login-free listing mirrored in sources/decode/records-*.tsv): MSS/20211 siblings Decrypted: R1174 /56, 1177 /73, 1176 /98, 1175 /94, 1178 /105 (1477), 1184 /116, 1179 /115, 1171 /114 (1478), 1180 /126, 1181 /128 (1479), 1183 /64; Non-decrypted: R1172 /123 only seen -- target unchanged. Plaintext/images still account-blocked (ASKS 42).
Solver repositories, shallow clones 3 Oct 2026, grep only: dbourdeau/cyphersolver -- no hit for MSS/20211 or Ferdinand-to-John II (esp318 holds Galende's text, a different cipher run); aaymeloglu/unsolved-ciphers (cited, no code copied) -- only catalogue rows (decode-records.jsonl line 727 for /123, bne-ranked.md line 12), no target folder, no working files, no reading. Neither repo names this item as a next step.

## Premise check (CS-A2-M, 3 Oct 2026)
(a) Folder's own mentions: found -- DECODE R1180 Plaintext Spanish (document placeholder-blocked) and BNE "cifra interlineal" wording relayed through Aymeloglu's digest, not independently opened; both already in this file, nothing new openable. Tomokiyo's "Cipher (1476-1479)" is the unresolved candidate key for /123 and /126.
(b) Other solvers' working files: not found -- neither repo has outputs, apply-key scripts or renderings for MSS/20211.
(c) Physical neighbours (interlinear decipherment on the leaf, facing page, slip): unreachable -- no image of /123 or /126 openable (DECODE full-size blocked, bdh.bne.es 403, catalogo.bne.es JS/400).
(d) Recipient/sender-side editions: unreachable beyond the above -- Galende Diaz (read earlier by another worker) names /56 and /73 only; Spanish documentary editions of Ferdinand-John II correspondence not opened this pass (no full-text route found).
Verdict stays blocked; the unblocking step is unchanged (ASKS row 45, or a BNE record/image route). Requests this pass: WebSearch 8, WebFetch 3 (cryptiana.blogspot.com, google search), web.archive.org 2, cryptiana.web.fc2.com 1, catalogo.bne.es 1, github.com 2 clones.

## While waiting (RUN4-WAITBF, 4 Oct 2026)

- Action that depends on nobody: one DECODE browser login (tools/decode_browser_login.js with --guess-fullsize, the A2-HDK route that served R4692's full-size image on 2 Oct 2026) to re-test whether R1172 (/123) and the Decrypted sibling R1180 (/126) serve full-size images or plaintext documents; image to scratch, never committed; ~$1 (estimate). ASKS row 45 (Tomokiyo 2018 body) stays the outside blocker for the key.

## Tomokiyo 2018 read (5 Oct 2026 03:28 UTC, owner download, account-3 orchestrator)

The owner opened S. Tomokiyo, "Spanish Ciphers before Accession of King Ferdinand: 1470-1479" (academia.edu/37751652, 2018)
with a free account and downloaded it. The PDF and its key figure are kept in the private repository
(cipher-lab-private, bne20211-ferdinand-1478/lit/), not here: it is the author's work, not ours to redistribute.

- Section 2.4, "Ferdinand-John II of Aragon Cipher (1476-1479)", lists nine source letters, MSS/20211/94, 105, 109, 114
  ("mainly used in the reconstruction"), 115, 116, **123 (Cordoba, 4 Nov 1478)**, **126 (Trujillo, 4 Dec 1478)** and 128.
- Fig. 4 ("Cipher Used in Letters of Ferdinand the Catholic before Accession (1478)") is the reconstructed table:
  homophonic letter signs for a-y, numbered syllables (ba=3 ... zu=72, bracketed values inferred), and a short
  nomenclator (Rey, como, por, que, del, vuestra alteza; 82, de, do, du, fu, gi).
- The paper prints **no decipherment** of item 123 or item 126: no plaintext of either letter is quoted.

Consequence: not found-solved. Status moves from `blocked` to `open` (the block was this one read; the letter is not yet read), but the key question is answered:
a **published key** (Tomokiyo 2018, Fig. 4; key source `published`, credited) built partly from item 123 itself. What
the target now needs is the ciphertext: the BNE images of item 123 (bdh.bne.es/bnesearch/detalle/bdh0000186627,
403 from the cloud) or item 126 (bdh0000186569). Next: owner desk download of those images (one link each), then a
transcription + key application with tools/decode_key.py; ~$4.

## Item 126 images on hand (5 Oct 2026 03:4x UTC, account-3 orchestrator)

The owner downloaded BNE MSS/20211/126 (Trujillo, 4 Dec 1478) from bdh.bne.es; PDF and page images are in the private
repository (bne20211-ferdinand-1478/images-126/). First look: f.1r and the top of f.1v are almost entirely cipher (numerals
for syllables plus letter signs, Tomokiyo's "Cipher (1476-1479)"), and **every cipher line carries a faint interlinear
decipherment in a second hand**, letter by letter above the groups (matches DECODE R1180 "Decrypted"). The closing lines
are clear ("...De Trugillo a quatro de Dezienbre de lxxviij"), signed "Yo el Rey", countersigned "Ant. Ximenez(?) secretario".
That makes 126 a key source in its own right (grade C, period). Next, after FER1478-READ on item 123: a 126 job aligns
the interlinear decipherment to the cipher, builds the period key, merges with 123's key under rule 3's per-unit gate.

## Sign pool on hand: all 9 of Tomokiyo's source letters (5 Oct 2026 03:5x UTC, account-3 orchestrator)

The owner downloaded six more BNE MSS/20211 items from bdh.bne.es; all in the private repository
(bne20211-ferdinand-1478/images-<item>/): 94 (Madrigal 30 Apr 1476), 105 (Medina del Campo 6 Jul 1477), 114 (Madrid 9 Apr
1478, Tomokiyo's main source), 115 and 116 (Madrid 18 Apr 1478; folio numbers read from the leaf), 128 (Trujillo 22 Jan
1479). 109 (dated "Dic. 22" 1477 on the leaf) followed the same night, so all nine are on hand. Thumbnail look only, not a reading: each mixes clear text with a cipher block of
numerals + letter signs; 115 shows faint interlinear writing above its cipher lines like 126, and 128 has marginal notes
beside its cipher lines (decipherment or not: unchecked). Rule 3 / selection: this is a one-sender, one-key pool (letters to
John II, 1476-79) with a published key and at least two period decipherments (123 below the cipher, 126 interlinear).
Not yet checked-solved per item: before deep work on any item other than 123/126, check-solved per
.claude/briefs/check-solved.md and tools/intake_gate_check.py. Next: after FER1478-READ, one pool job: check-solved for
the six, then key from 123+126 (per-unit gates), apply to all eight; ~$15, needs the parent's go.

## Superseded head lines (kept for the record; replaced 5 Oct 2026 by the Tomokiyo read)

- (3 Oct 2026, CS-A2-M) Tomokiyo 2018 (academia.edu/37751652), the one edition that could key item /123 or /126, not then opened by CS-A2-M on 3 Oct 2026: academia.edu body still account/Cloudflare-gated, Wayback holds only the 18 KB landing page (CDX 10 Jul 2024), no Tomokiyo mirror; read instead his 29 Nov 2018 Cryptiana post (abstract only, 3 comments not retrievable) and eleanor1476.htm -- verdict then `blocked`.
- (25 Sept 2026, LANE DX) Corrected again by the LANE DX orchestrator, 25 Sept 2026 02:10 UTC: Galende Díaz read in full (below) and does not cover items /123 or /126, but Tomokiyo 2018's body was then not opened and its "Cipher (1476-1479)" (a syllable cipher of over 500 entries) covers the very window of R1172 (4 Nov 1478) and R1180 (4 Dec 1478); by check-solved.md an edition not opened kept the verdict blocked at that date. Unblock: ASKS row 45 (the owner reads the paper), or DECODE document access (ASKS row 42).
## FER1478-READ, 5 Oct 2026 (account-3 worker, brief .claude/briefs/runs/2026-10-05-acct3-fer1478-read.md)

Material: BNE MSS/20211/123 f.1r image p-000.jpg and Tomokiyo 2018 Fig. 4, both in the private repository
(cipher-lab-private, bne20211-ferdinand-1478/), never committed here. The image is 1114x1520 px, 120 ppi; the BNE PDF
beside it embeds the same 120 ppi JPEG (pdfimages -list), so no higher-resolution copy is on hand.

Intake: tools/intake_gate_check.py first failed (line 2-3 still said Tomokiyo was not opened); fixed by rewriting
only the head from the sections already below (old lines kept under "Superseded head lines"). Re-run:
`ciphers/bne20211-ferdinand-1478: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.

**Step 1, verdict: the lower cursive block is a period DECIPHERMENT of the cipher block, not a continuation.**
Layout of f.1r: clear opening ("Recebi la carta de v. alteza de xvij de setiembre ... sobre la reducion de charles
darteida ... de lo qual soy maravillado"), then 22 lines of cipher, which close with the clear address formula
"Exmo señor / La vida y Real estado de aquella por luengos tiempos ...". Below that, in a different, smaller cursive
hand, there are about 15 lines of clear Spanish. Evidence:
- Its first words, "porq sabe v. alteza lo q yo en ... en dias passados", are what the first cipher signs read
  under Fig. 4: after "soy maravillado" come double-crossed ff (p), e: (o), gt (r), then a group, then
  barred-b/q/long-s/crossed-t, i.e. s a b e. So the cipher reads "por[que] sabe".
- A recurring cipher group, crossed-f/b/q/gt/curly-d/t/barred-b, reads c h a r l e s sign for sign under Fig. 4.
  It occurs at least 4 times in the cipher block, and the cursive block names "el dicho charles" at least 5 times
  (D01/D02, D05, D06, D12, D13; both passes).
- The cursive block takes up the clear opening's subject: the "reducion" of Charles, the kingdom of Navarre, not
  receiving "ninguno de los agramonteses" (the Agramont faction). It has no salutation or address of its own and
  starts mid-sentence, which a continuation of the letter would not.
- The faint interlinear writing above cipher lines 1-2 is a third hand (not read; too faint at 120 ppi).

**Step 2, gate FAILED: the cipher block cannot be transcribed sign by sign from this image.** The crop step ran as
the brief required:
`python3 tools/iiif_lines.py --image p-000.jpg --out <scratch>/crops --region 150,355,860,745 --prefix cph --centres <22 eye-checked centres>`
-> `region 860x745, 22 lines, 22 bands x 1 segments ... wrote 22 crops` (auto-detection gave 20-21 lines on this
uneven block; the 22 centres came from the ink profile and were checked against the debug overlay; crops stay in
the session scratchpad). Pass A ran as 4 Sonnet calls over line groups 1-4, 5-8, 9-12 and 13-16 (2x upscale).
Every call reported the signs as unresolvable: "near-noise", "rough approximations from line shapes". L01 got 24
labels against about 50 visible signs. A 3x half-line upscale (my own check, L01a/b) is still blurred: the cipher
x-height is about 12-15 px at native size. TRANSCRIPTION.md's <=5% per-sign error target is out of reach at 120 ppi,
so per the brief I stopped before pass B on the cipher. The pass-A labels are discarded, not committed. Steps 4-5
(key.tsv, decode_key.py, reading.txt) were not run, and no reading is claimed.

**Step 3, partly done:** the period decipherment has two blind passes, `period_decipherment_passes.tsv`: pass A by
the worker (Opus), pass B by a Sonnet subagent (which said about half was legible and some words were filled from
context). They are not reconciled. They agree on these spans (substance, spelling aside): "porq sabe v. alteza lo q
yo en ... en dias passados ... el dicho / charles fazia de reduzir se"; "del dicho mes de setiembre"; "soy
maravillado de lo q por aquesta carta me [scrive]"; "q he fecho al dicho charles"; "y reposo al regno de navarra ...
por no venir en efecto la reducion del dicho charles"; "en dias passados ... al dicho q no recibiesse ninguno de los
agra[monteses]"; "de aql regno no solo no lo estorbaria mas [con] todas mis fuerças lo". Both passes are
low-confidence below line D08 (water stain on the right, faded ink).

Not graded per rule 4: there is no cipher-token reading. This report finds and gives the substance of the period
decipherment on the leaf only; no novelty is classified (rule 10). Fig. 4 (published) vs a period-derived key: not
compared (step 4 not reached).

## FER1478-READ2, 5 Oct 2026 (account-1 worker for account 3, brief .claude/briefs/runs/2026-10-05-acct3-fer1478-read2.md)

Stopped at step 1 (19:42-19:45 UTC by date -u), nothing read. The new screenshots (images-123-shots/set1-1..6.png) are only
in the private repository, and this session could not reach it: its GitHub access covered only the public repository; a
clone and an add_repo request for the private one were both refused by the session's permission policy. No crop, pass,
key or reading was made; the images were never on this container. Next: rerun the same brief from a session whose
GitHub scope already includes the private repository (or the owner allows it for this account's sessions), ~$10.

## FER1478-READ2 rerun, 5 Oct 2026 22:21-22:3x UTC (account-4 standing session, session_01PpZtGZsbseHrXViC8rzExA, private repo attached)

Brief .claude/briefs/runs/2026-10-05-acct3-fer1478-read2.md, restarted at step 1 with the private repository in scope.
Stopped at the step-2 gate; no key, no reading, 0 tokens graded.

**Step 1, crops.** Material: images-123-shots/set1-4.png (1564x736), set1-5.png (1481x802), set1-6.png (1552x675) in the
private repo; nothing copied here. The auto line detector misreads this sloping hand (6/15/5 lines found), so the centres
came from a narrow-strip ink profile, checked on the debug overlay:
`python3 tools/iiif_lines.py --image set1-5.png --out <scratch>/h5b --prefix s5b --region 180,0,1180,802 --centres 15,60,100,138,185,238,285,333,380,428,480,527,572,621,670,726,778 --follow-slope 300 --top-margin 14 --bottom-margin 14 --max-width 660 --overlap 90`
-> `wrote 34 crops` (17 lines x 2 half-line segments); likewise set1-4 (`--centres 515,557,598,640`, 8 crops) and set1-6
(`--region 230,0,1150,110 --centres 70`, 2 crops). Segments upscaled 2x (PIL Lanczos) in the scratchpad. **The cipher block
has 22 lines** (set1-4 C01-C04, set1-5 C05-C21, set1-6 C22, ending in the clear "Exmo señor"). A first cut with eye-placed
centres drifted up to a full line in the lower half of set1-5, and its passes for C11-C22 were discarded and re-run.
A first full-width crop run (no upscale) was also discarded: all 4 readers rated it near-illegible and read only about half
of each line.

**Step 2, cipher block: two blind Sonnet passes, gate FAILED (alphabet not settled).** File: `cipher_shape_passes.tsv`
(pass A, pass B, 22 lines; s1/s2 joined with the overlap removed). Labels are the Latin-letter shape of each glyph plus
colon/dot marks, since no settled sign inventory exists for this hand. Pass A 1,418 glyphs, pass B 1,323. Agreement
0.829 overall (letters only 0.866). By line it runs from 0.59-0.71 (C06-C08, where one reader dropped glyphs in dense
runs) to 0.93-0.96 (C13-C15, C18-C19). That is over TRANSCRIPTION.md's 10% disagreement line. Worse, the label set
does not resolve the cipher's sign set: "t" is 427 of 1,418 glyphs (30%) in pass A. In Tomokiyo's Fig. 4, the signs for e, g, h,
i and t are all t-based variants (a crossed t, tt, tb, t with a colon), which the readers cannot tell apart at this
size and label alike. Reconciliation was not run (it cannot repair an unresolved label set).

**Diagnostic only, not a test of the key (step 4 not reached properly).** A stream alignment
(`tools/stream_align.py` via its library calls; band 120, step 200, 3 iters) of pass A's glyph stream against the
earlier period-decipherment pass A (`period_decipherment_passes.tsv`, 940 letters, low confidence) scores 0.302
identical-pair accuracy against 0.292 mean (max 0.317) for 10 shuffled-text controls. It does not beat its control, as
expected from the 30% "t" class and an unreconciled clear text: a non-test, not a negative about the letter or the key.

**Step 3, period decipherment: 2 more blind passes, too weak to reconcile.** At this block's 29 px line pitch, the 44-88 px
crops held two lines each, and both readers reported uncertainty about which line was the target (rows D04-D09 of one
pass flagged unreliable). The passes stay in the scratchpad and are not committed. The block needs crops cut at its own
pitch (top/bottom margin <= 4 px, or --follow-slope) before another pass.

Cost: see the lane ledger (about 20 Sonnet calls: 4 discarded full-width, 10 cipher half-line, 6 decipherment).
Report: what was read and where it was not found. No reading claimed, no novelty classified (rule 10).

## LANE-PRIV1 FER-POOL step 1, item 126, 6 Oct 2026 01:3x-01:4x UTC (account-4 standing session, session_01PpZtGZsbseHrXViC8rzExA)

Material: BNE MSS/20211/126 (Trujillo, 4 Dec 1478) images-126/p-000.jpg (f.1r, 1123x1549) and p-001.jpg (f.1v spread,
2144x1526), both 120 ppi (pdfimages: the BNE PDF holds the same), private repository; nothing image-like committed here.
Cipher line centres from a dark-ink row profile: **f.1r 28 cipher lines, f.1v 12** (then the clear closing "qual Recebire
merçed ..."). Crops: `tools/iiif_lines.py --image p-000.jpg --region 130,180,950,1140 --centres <cipher centre - 5> --top-margin 8
--bottom-margin 8 --max-width 500 --overlap 50` (56 half-line crops) and p-001.jpg `--region 150,180,850,480` (24), each holding the
cipher line and the faint interlinear decipherment written above it; 3x upscale. Two blind Sonnet passes, 8 calls each:
`item126_passes.tsv` (G = interlinear as read, C = cipher tokens; V12 is the clear closing).

**Result 1 (control-backed): Tomokiyo 2018 Fig. 4's syllable numerals agree with this leaf's own period decipherment.**
Rule fixed before the first run (`item126_fig4_test.py`): share of numeral tokens whose Fig. 4 syllable occurs in the same
line's gloss letters (lines with >= 8 gloss letters read), against Fig. 4's syllables shuffled over its codes (2000 draws), gate
real > shuffled p99. Pass A: 0.370 (149/403) vs shuffled mean 0.100, p99 0.156, **PASS**. Pass B, read independently: 0.371
(116/313) vs 0.097, p99 0.160, **PASS**. The published key (`published`, credited to Tomokiyo) is supported for the
numeral layer by an independent period witness on a second letter of the pool (it was built mainly from item 114).
The test is lenient in the same way on both sides (a syllable anywhere in the line's gloss counts), so it measures
key-vs-gloss consistency, not per-token correctness; it does not test Tomokiyo's letter signs or his nomenclator.

**Result 2 (gate failed): the item 126 transcription is not settled, so no per-token reading or sibling decode.**
Pass A 1,303 tokens, pass B 1,376; agreement 0.626 on all tokens, 0.758 on numerals alone. That is far over the 10% line.
The letter-like signs show item 123's problem (shape labels lump the t-based signs), and the interlinear is mostly
unreadable to the readers at 120 ppi (pass A read about 400 gloss letters over 40 lines; most G rows are "?"), so it
cannot carry a full key alignment (`tools/interlinear_align.py` was not run: the gloss is too sparse to align). Count only, not
a reading: agreed numeral tokens with an unbracketed Fig. 4 value are 298 of about 1,420 tokens (21%); with Tomokiyo's
bracketed (inferred) values 59 more. Siblings (items 94-128) were not decoded: the same unsettled letter-sign alphabet applies
to them, and their images are the same 120 ppi.
Report: what was read and where not found; no novelty classified (rule 10). Cost: see the lane ledger (16 Sonnet calls).

## FER126-ALIGN, 6 Oct 2026 02:35-02:4x UTC (account-4 standing session, session_01PpZtGZsbseHrXViC8rzExA; brief .claude/briefs/runs/2026-10-06-acct3-fer126-align.md)

Material: the owner's colour screenshots of item 126 at about 250% (private repo images-126-shots/1-3.webp, 1714x935,
1684x893, 1708x712). Cipher line centres from a brown-ink row profile in three vertical strips: 10 + 11 + 8 lines, with the
stated one-line overlaps = **f.1r's 28 lines; the shots do not cover f.1v**. Crops: `tools/iiif_lines.py --image <shot> --centres
<cipher centre - 12> --top-margin 4 --bottom-margin 16 --max-width 900 --overlap 80` (56 line-pair crops, gloss above + cipher,
2x upscale; spot-checked 3), and for the gloss alone `--centres <cipher centre - 34> --max-width 2400` (full-width gloss-centred
strips, native). Passes kept in `item126_colour_passes.tsv` (text only).

**Gate failed at step 2: the interlinear gloss is still not legible enough to align.** Sonnet pass A on the line-pair crops read
103 gloss letters over R21-R28 and almost none elsewhere ("the grey lines are almost entirely illegible"). One Opus gloss-only
trial on gloss-centred strips (R01-R07) read about 30-35% of the letters with confidence, only short syllables (R01 "su ca r ta
do", R04 "pu e s con", R05 "men te con", R07 "pue s a lo"). Contrast stretching does not help: the webp screenshots carry little
detail in the grey ink (compression blocks dominate once the brown is removed). A per-line alignment
(`tools/interlinear_align.py`) needs a gloss read close to letter by letter, so steps 3-4 (key.tsv, decode_key.py, siblings) were
not run.
The cipher is no better on the colour crops: pass A vs pass B on R01-R10 agree 0.435 on all tokens and 0.698 on numerals,
against 0.626 / 0.758 at 120 ppi in LANE-PRIV1, because the readers marked more letter signs "?". The letter-sign alphabet
is the limit, not the image (ASKS 143, the sorter). Pass B was therefore stopped after R01-R10 (the rest was not worth its cost).
No tokens graded (H 0 / C 0 / S 0 / M 0); no PROGRESS.tsv row. Report: what was read and where not found; no novelty words.
Cost: see the lane ledger (8 Sonnet calls + 1 Opus call).

## FER126-ALIGN2, 6 Oct 2026 05:37-05:4x UTC (account-4 standing session, session_01PpZtGZsbseHrXViC8rzExA; brief .claude/briefs/runs/2026-10-06-acct3-fer126-align2.md)

New instrument (PREREG-ALIGN2.md, pushed c687ec9f before any reader call): candidate-constrained gloss verification with decoys.
Candidates (`align2_candidates.py`): per line, the numerals LANE-PRIV1's two blind passes agree on, decoded with Tomokiyo Fig. 4
(unbracketed values) -> 299 syllables over all 39 cipher lines (f.1r R01-R28, f.1v V01-V11; the owner's f.1v shots confirm 11
cipher lines + the clear closing). Decoys: another line's list (not adjacent, closest length), 295 syllables. Gloss-centred crops
from the colour shots (1-3.webp; f1v-3.webp for f.1v), `tools/iiif_lines.py --centres <cipher centre - 34 (f.1r) / - 30 (f.1v)>
--max-width 2400`, upscaled to <= 2400 px; 3 spot-checked (R05's gloss readable by eye: "a res su dique ... men te con").
78 items shuffled (seed 20261006), 8 packs, 4 Sonnet calls.

**Result: GATE FAIL, untested-by-this-tool.** Real yes 0/299 = 0.000, decoy yes 0/295 = 0.000, difference 0.000, real > decoy on
0/39 lines (gate: difference >= 0.30, decoy <= 0.15, 2/3 of lines). Every answer from all four readers was "?": "the grey ink was
too faint and small to read at the displayed resolution". This is not the agreeing-reader failure the decoy guards against (decoy
yes stayed 0); the Sonnet reader cannot see the grey ink at this resolution at all, so the instrument is untested on this material,
not a negative about Fig. 4 or the gloss. No tokens graded (H 0 / C 0 / S 0 / M 0); no PROGRESS.tsv row. Steps 3-4 not run.
Not tried within this job: the same items with an Opus reader (the Opus blind trial in FER126-ALIGN read about 30-35% of gloss
letters, so it may answer y/n where Sonnet abstains); it is a reader change after a failed gate, so it is named as the next step
with its own pre-registration rather than run here (8 Opus calls, about the whole cap of this job).
Report: what was read and where not found; no novelty words (rule 10). Cost: see the lane ledger (4 Sonnet calls).

## FER126-ALIGN3, 6 Oct 2026 07:37-07:44 UTC (account-4 standing session, session_01PpZtGZsbseHrXViC8rzExA; brief .claude/briefs/runs/2026-10-06-acct3-fer126-align3.md)

Third and last machine attempt at item 126's grey interlinear gloss (rule 3, third-attempt clause). PREREG-ALIGN3.md pushed (bde0446fa)
before any reader call: PREREG-ALIGN2's items, decoys, shuffle, packs, question, statistic and gate unchanged; instrument changed to an
Opus reader and native-resolution segments (each line cut by `tools/iiif_lines.py --image <shot> --centres ... --max-width 640 --overlap 80`
into three segments, upscaled 2.4x to about 1536 x 391 px, so the image reader no longer shrinks the line to about 80 px tall; commands in
the pre-registration; crops kept in the session scratchpad, never in this repository). 8 Opus calls, all 78 items answered
(`align3_answers.tsv`).

**Result: GATE FAIL.** Real yes 92/299 = 0.308, decoy yes 31/295 = 0.105, difference 0.203 (gate >= 0.30); real > decoy on 25/39 lines
(gate >= 26/39); decoy yes <= 0.15 passes. Answers: real 92 y / 52 n / 155 ?; decoy 31 y / 92 n / 172 ?. Unlike ALIGN2, the reader now
sees the grey ink (it answered y or n on about half of the syllables). Descriptive only, outside the pre-registered gate: on the
syllables it did answer, real lines read y 64% (92/144), decoys 25% (31/123); two-proportion z about 6.1 on the yes rates. This is a
signal that the gloss carries the Fig. 4 syllables, but it does not meet the gate fixed before the run, so no tokens are graded
(H 0 / C 0 / S 0 / M 0), no conflict rows, no PROGRESS.tsv row; steps 3-4 of the ALIGN2 brief were not run.
Logged: **untested-by-this-tool (machine gloss reading, 3 attempts)** -- FER126-ALIGN (blind reads), FER126-ALIGN2 (Sonnet, decoy-gated),
FER126-ALIGN3 (Opus, decoy-gated, native segments). The machine gloss-reading step is retired with that instrument named; no fourth
machine pass. Next: the owner reads the gloss in a sorter-style page (one gloss line crop at a time, type what the grey writing says),
then the typed gloss goes through interlinear_align.py against the Fig. 4 decode. Report: what was read and where not found; no novelty
words (rule 10). Cost: 8 Opus calls at about 120k tokens each.

## Remaining gaps (finish-or-blocker pass, 5 Oct 2026)
Read so far: 0% of cipher tokens graded H/C/S; the period decipherment is in two unreconciled passes (15 lines, about 50% agreed spans)
- cipher block sign transcription (22 lines, about 1,400 glyphs) - blocker: waiting-on ASKS row 143 (the owner's sign sorter); the screenshots are legible, but two blind passes split on 17% of glyphs and the shape labels lump the t-based signs (30% of glyphs); next: settle the alphabet in tools/sign_sorter.py on the set1-4/5/6 crops (focus: t/tt/tb/crossed-t, e/e:/c, d/d.), then 2 passes against the settled labels, ~$6
- period decipherment reconciliation (15 lines) - blocker: not-attempted; reconciled once by FAM-BNEDEC (10 Oct 2026, `period_decipherment_reconciled.tsv`, 12/15 lines doubt < 1/3, not blind) and one phrase found in print (Paz y Meliá 1914, below); next: read the 1914 print's page (IA elcronistaalonso0000unse, lending/print-disabled: a person's read, LOCAL-QUEUE or ASKS) and settle the doubt-marked words against it as grade C witness, ~$1
- key alignment against the period decipherment (step 4) and decode_key.py reading (step 5) - blocker: not-attempted; it needs the cipher transcription above; next: interlinear_align.py on cipher vs the reconciled decipherment, ~$3
- item 126 and siblings 94-128 per-token reading - blocker: waiting-on ASKS row 143 (the owner's sign sorter, now for items 123 and 126) and ASKS row 148 (a sharper image of 126's grey interlinear: the colour shots at 250% still give Opus about 30-35% of its letters, FER126-ALIGN); machine gloss reading [retired] after 3 attempts (FER126-ALIGN, -ALIGN2, -ALIGN3: Opus decoy-gated check FAILed its gate, diff 0.203 vs 0.30, 25/39 lines vs 26, though real y 0.308 vs decoy 0.105); next: the owner types the gloss line by line in a sorter-style page (ASKS 148), then interlinear_align.py against the Fig. 4 decode, ~$2; 126's numerals are supported by Fig. 4 (two passes PASS), but its passes agree 0.626 and the letter-sign alphabet is unsettled; the Fig. 4 table used by item126_fig4_test.py is not committed (author's work): re-create KEY.tsv (code, value, grade) by typing the 73 syllable cells from the private repo's lit/fig4-000.jpg (bracketed values grade M), ~15 min

## Escalation (5 Oct 2026)
- [x] siblings: item 126 transcribed in two passes with its interlinear (LANE-PRIV1, 6 Oct 2026): Fig. 4 numerals PASS against the period gloss (0.370/0.371 vs shuffled p99 0.156/0.160); its interlinear is too faint at 120 ppi for a full alignment, and the letter signs wait on the sorter (ASKS 143)
- [x] clear-pages: the clear opening and the period decipherment on f.1r located and used (step 1 verdict)
- [x] known-keys: Tomokiyo 2018 Fig. 4 (published) is in hand and was used to test the step-1 verdict
- [x] print: tools/print_check.py run on 4 phrases of the reconciled decipherment (FAM-BNEDEC, 10 Oct 2026): "reposo al regno de navarra" found in Paz y Meliá, El cronista Alonso de Palencia (1914; IA elcronistaalonso0000unse, gbooks 7q9CAAAAYAAJ); the page itself is not yet read
- [ ] key-rebuild: align the cipher with the period decipherment to rebuild the key and compare it with Fig. 4 value by value
- [x] image-check: the owner viewer screenshots (images-123-shots, about 2x the PDF) are legible line by line (FER1478-READ2 rerun, 5 Oct 2026); the block is now limited by the unsettled sign alphabet, not by the image
- [ ] retry: transcription passes against settled sorter labels (the shape-label retry ran on 5 Oct 2026 and split 17%)
Verdict: keep going: 2 internal gaps; cheapest next: read the Paz y Meliá 1914 page that carries "reposo al regno de navarra" (a person's read in the IA reader) and set the decipherment against it, ~$1; then a verifier on whether the letter's text is already in print; the cipher transcription waits on ASKS row 143 (sign sorter) (verdict updated 10 Oct 2026, FAM-BNEDEC)

## BNE-DECODE re-test of DECODE R1172 / R1180 (9 Oct 2026, 11:27 UTC by date -u; account 4, Sonnet)
One DECODE browser login (`decode_browser_login.js 1172 <scratch> --guess-fullsize --fetch-page RecordsView/1180 --max-files 14`), ~14 requests, 1.5 s apart. Images and saved pages stay in scratch, not committed; the account name is in no committed file.
Full-size images were served this time (HTTP 200, `image/png` by file(1)); the 24 Sept placeholder (17,947 B, sha1 035489a0...) did not come back for any of the 5 pages:
| file | bytes | pixels | sha1 (first 12) |
|---|---|---|---|
| IMG_R1172_I5878_P1.png | 2,309,727 | 1114x1520 | 11442cec6e3e |
| IMG_R1172_I5879_P2.png | 1,188,237 | 1117x1510 | bc8d2adf8600 |
| IMG_R1180_I5897_P1.png | 2,145,965 | 1123x1549 | 57e0a770a907 |
| IMG_R1180_I5898_P2.png | 2,127,163 | 2144x1526 | 02d49e2e5e23 |
| IMG_R1180_I5899_P3.png | 939,112 | 1120x1520 | 7a922427db3f |
Not found: any document link on either record page (no `filesrv` link except the 5 thumbnails); the record pages' "Plaintext" field reads only the language ("Spanish" on R1180, empty on R1172). The Documents list was not requested (one login only), so R1180's plaintext document is untested, not refuted. The `decode/IMG_*.png` files already committed in this folder are the old placeholders (17,947 B each); they were not replaced.
Next (one line): a later session with one login can fetch `DocumentsList` for R1180 and read the full-size pages above (they are about the size of the owner-viewer screenshots, so check against `images-123-shots` before any new transcription pass).

## BNE-1180 (J6): R1180 DocumentsList and full-size pages (9 Oct 2026, 13:53-14:0x UTC by date -u; account 4, Sonnet)
One DECODE browser login (`decode_browser_login.js 1180 <scratch> --guess-fullsize --fetch-page "/decrypt-web/DocumentsList?showmaster=records&fk_id=1180" --max-files 12`), 8 requests after login, 1.5 s apart. Pages and images stay in scratch, not committed; manifest in `r1180-manifest.tsv`.
- **DocumentsList for R1180: "No records found"** (page 200, 93,989 B). No plaintext document is attached to R1180; the record's "Plaintext: Spanish" is a language field only. The record header says "No. of Pages 2" while three images are held.
- Full-size images served again, same sizes and sha1 as the 11:27 fetch (P1 1123x1549, P2 2144x1526, P3 1120x1520).
- Content seen (P2, P3 only; P1 not viewed): P2 is a two-leaf spread, folio number 117, with a cipher block with grey interlinear gloss and the clear closing dated Trujillo, 4 Dec 1478; P3 is the address verso. Consistent with item /126.
- Comparison with `images-123-shots`: not made. Those screenshots are in the private repository, not in this container, and by the notes above they are crops of item /123 (R1172), not of R1180. The R1180 pages (about 1100-2100 px wide for a whole leaf or spread) are a different item at a different scale. Not found here: any R1180 plaintext document.
Next (one line): R1180's P2 is a legible full-size image of /126's cipher block and interlinear for the owner's sign sorter (ASKS 143/148) without further fetching; the key-rebuild step still needs a person-settled alphabet.

## BNE-DEC29 (FAM-BNEDEC, 10 Oct 2026 09:22-09:3x UTC by date -u; account 2, LANE FAMILY-A2p, Opus worker, brief .claude/briefs/runs/2026-10-10-ytbiz-family-0909-jobs.md)
Prior work: `tools/prior_work.py ... --step-type transcribe --fetch` exit 4 (LEAD own claim, LOOK leaf, UNCHECKED solver/tomokiyo); all four recorded in prior-work.tsv (CLEAR/CONTEXT). Check 1: no re-cut of the decipherment after 5 Oct in ROOM.md or this folder.
- **Image:** one DECODE browser login (`decode_browser_login.js 1172 <scratch> --guess-fullsize --max-files 6`), 4 files served; IMG_R1172_I5878_P1.png 2,309,727 B, 1114x1520, sha1 11442cec6e3e (= the 9 Oct table). It is f.1r of item 123; the 15-line decipherment block is its lower part. Committed only the block region, `images/r1172_p1_decipherment_block.jpg` (1014x392, region x100 y1120 of the page, manifest `images/manifest.json`); the full page and saved record page stay in scratch.
- **Pitch:** at this image's own scale the block's pitch is ~24 px (the "29 px" of the 5 Oct notes was measured on another scale). The block slopes up to the right by ~20 px across its width, so fixed-y half-line crops put the right half on the wrong line: the earlier two blind passes (4 Sonnet calls) ran on those crops and drifted line by line -- logged as a non-test, not used. Re-cut: `python3 tools/iiif_lines.py --image images/r1172_p1_decipherment_block.jpg --out images/dec_lines --prefix dec --centres 27,47,72,97,121,143,168,193,218,242,267,292,314,336,358 --max-width 560 --overlap 60 --follow-slope 120 --slope-margin 4 --debug` (slope fit ~ -0.02 px/px per band; debug overlay checked; 30 crops committed).
- **Blind passes on the corrected crops** (2 x 2 halves, Sonnet, crops only, 3x upscaled): readers' self-confidence 0.1-0.6 per line; both passes again mis-numbered lines (read s1 and s2 as separate lines), and pass B lines 9-15 came back truncated (3 rows). **Two-pass agreement before reconciliation:** half 1 (D01-D08) 48 exact word matches of 138 (A2) / 81 (B2) words; half 2 11 of 84 / 16; pooled 59 of 222 = 26.6% by the longer pass (Dice 0.37). For the record, the defective-crop passes gave 43.8% by `tools/reconcile_passes.py` (word tokens incl. "?"), not comparable.
- **Reconciliation** (worker, from the crops): `period_decipherment_reconciled.tsv` (line, text, agreement, doubt). 12 of 15 lines have doubt < 1/3 (D08 0.53, D09 0.36, D15 0.80). Caveat: not blind -- this worker had read `period_decipherment_passes.tsv` (5 Oct, pass A) before reconciling; words neither 10 Oct pass supports and the crop does not show clearly are marked "?". Nothing graded above M.
- **Print rung** (`tools/print_check.py` on 4 phrases, `phrases.txt`, `print-check.tsv`; requests be-api.us.archive.org 4+7, googleapis 4, openalex 5, semanticscholar 5, crossref 1, archive.org metadata 1): "reposo al regno de navarra" found as an exact phrase in Paz y Meliá, *El cronista Alonso de Palencia: su vida y sus obras* (1914), IA `elcronistaalonso0000unse` (collections internetarchivebooks, printdisabled) and Google Books 7q9CAAAAYAAJ. be-api snippet: "alteza mucho seruicio y benefficio, y reposo al regno de navarra, ca por no venir en effecto la reduccion" -- the same words as D05 end / D06 here, and it shows that D05's "mando? siempre" should probably read "mucho seruicio" (left as read; the print is not used to change the reconciliation). Not found in that item by be-api: "agramonteses en su favor", "charles de artieda", "secretario coloma", and the single words agramonteses, artieda, demostraciones (be-api returned 0 for every single-word query here, so these misses are not informative). The other three phrases: no IA/Google Books hit (the gbooks hits for "con todas mis fuerças lo procuraria" are unrelated genealogy volumes). The page number in the 1914 book is not known (be-api page_num is the item's image count).
- **What this means for the target:** the print rung moved: a 1914 book prints at least one passage of this letter's text (or of a text sharing it). Whether it prints the whole letter, from the decipherment or another copy, is unread; that is a verifier's question (rule 10), not settled here. No cipher transcription (waits on ASKS 143).
Report: what was found and where it was not found. No reading claimed, no novelty classified.

