blocked

Check-solved (this worker, NX2-GATE, 26 Sept 2026): CSP Spain vol.3 part 1 (Gayangos, 1525-26) and part 2
(1527-29) opened at British History Online (index pp.1101-1102 "Soria, Lope de", pp.1095-1096 "Sanchez,
Alonso") -- both correspondents are extensively calendared there across 1525-1529, but this worker did not
locate calendar entries matching the five exact dates below or read whether any entry states a contemporary
decipherment, so the edition is confirmed reachable but not yet checked page-by-page for these items; treated
as `blocked` per the intake gate rather than `open`, pending that page-by-page read.

# Lope de Soria (Genoa/Mirandola) and Alonso Sánchez (Venice) to Charles V, 1524-1528 — RAH Colección Salazar y
Castro (Madrid)

Five archive-catalogued letters, from the RAH's own printed 49-volume *Índice de la Colección Salazar y
Castro* (Real Academia de la Historia, 1949-1979), found by SCOUT-OWN-4 (26 Sept 2026,
`SCOUT-OWN-4-2026-09-26.md`, its "S1" candidate) via a full-text OCR copy of the whole Índice on Internet
Archive (`salazary-castro-22-nov-2016`), never before on file in this repository. Each is marked by the
RAH's own cataloguers "en cifra, sin descifrar" (in cipher, not deciphered):

| # | Correspondent | Date | Place | Shelfmark | Inv. no. |
|---|---|---|---|---|---|
| 1 | Lope de Soria → Charles V | 21 Sept 1525 | Genoa | A-35, ff.310-312 (+ 1 duplicate) | 5180 |
| 2 | Lope de Soria → Charles V | 16 Jun 1526 | Genoa | A-37, ff.428-429 | 5540 |
| 3 | Lope de Soria → Charles V | 14 Apr 1528 | Mirandola | A-42, ff.243-244 | 6417 |
| 4 | Alonso Sánchez → Charles V | 17 Dec 1524 | Venice | A-33, ff.72-74 | 4670 |
| 5 | Alonso Sánchez → Charles V | 17 Jun 1528 | Venice | A-42, f.443 | 6502 |

Plus a sixth, adjacent item in the same legajo: A-42 ff.441-442, "Texto descifrado de los párrafos en cifra de
los tres documentos anteriores" — a period/19th-c. decipherment of three of the above (S2 in SCOUT-OWN-4).

Correspondents' ciphers are independently published on two tracks: Kolosova's dissertation (Ko.6 Lope de
Soria, Ko.9 Alonso Sánchez) and Tomokiyo's own reconstruction, with a full substitution-alphabet-plus-
nomenclature table for Alonso Sánchez's **1522** cipher already on file (`sources/cryptiana/web/
AlonsoSanchez.htm`). **Caveat carried over from SCOUT-OWN-4, confirmed and sharpened this session**:
Tomokiyo's own comments page (`sources/cryptiana/web/spanish2C.htm`) states Lope de Soria used **two**
different ciphers with the Emperor across his career (Ko.6, "the main cipher of the two", and a second,
Ko.16, not otherwise described there) — so even once a page image is obtained, "the on-file key still
applies" is not guaranteed for the 1525-1528 items without checking which of the two matches. Alonso
Sánchez's key (Ko.9) is dated to 1522-1523 correspondence; items 4 and 5 above are 1524 and 1528, 2-6 years
later.

## Check-solved (rule 1), this session, 26 Sept 2026

**(e) Solver repositories — checked first, per this job's brief, since it settles whether this is someone
else's lane.** Fresh shallow clones: `dbourdeau/cyphersolver` (HEAD `fc0c9e865d0fae67ca92d19750d2b09ab11972e0`,
2026-09-25) and `aaymeloglu/unsolved-ciphers` (HEAD `2495c45e8b94ffbc4f09a085224aa5ebce5cdf9f`, 2026-09-23),
grepped for `soria`, `sanchez`/`sánchez`, `A-33`/`A-35`/`A-37`/`A-42`, `9/33`/`9/35`/`9/37`/`9/42`,
`mirandola`, then deleted. **Bourdeau has four active folders on exactly these two correspondents**:
`soria1523/` (RAH 9/28), `soria1527/` (RAH **9/17**, Mirandola, 13 Dec **1527** — a different shelfmark and a
different year from our item 3, but the same place and the same key family, `keyB` — see below), `sanchez1522/`
(RAH 9/23-9/26), `sanchez1523/` (RAH 9/28). **None of his four folders touches Signatura 9/33, 9/35, 9/37 or
9/42** — the highest Soria/Sánchez shelfmark he has opened is 9/30 (`R9844`, cited inside `soria1523/` as the
source of key B). This resolves the lane-orchestrator's specific worry (ROOM.md 14:47, "Bourdeau runs a live
RAH Salazar campaign, sessa1524, 9/28-9/34"): `sessa1524/` is the Duke of Sessa/Luis Fernández correspondence
(a different sender), and even taking its stated reach at face value (into 9/33-9/34 per rah9-34-fernandez-1525's
NOTES.md), it is Sessa's hand, not Soria's or Sánchez's, and 9/33 there is Fernández's own item, not
necessarily Soria's or Sánchez's. **No overlap found; not his lane, not found-solved.** aaymeloglu's repository
has no folder or catalogue row for either correspondent beyond its cached DECODE snapshot (same rows checked
in (d) below).

Also worth noting for whoever picks this up: Bourdeau's own `soria1527/` NOTES.md (RAH 9/17, Mirandola, 13 Dec
1527) is the court's own bound decipherment ("Claro" A/B/C on f.34r) checked against key B — this is the
*same place* (Mirandola) as our item 3 (14 Apr 1528, four months later) and uses the same key family. If a
page image of item 3 is ever obtained, Bourdeau's key B (`soria1523/keyB.md`, `keyB_r9844.txt`) is the first
key to try, not a fresh Kolosova/Tomokiyo lookup.

**(d) DECODE.** On-disk snapshot (`sources/decode/records-non-decrypted-2026-09-24.tsv`,
`records-decrypted-2026-09-24.tsv`, `-diff.tsv`) greped for every `Signatura 9/NN` value present: the highest
RAH Salazar signaturas catalogued at all are **9/34** (8 rows, Non-decrypted, matching ROOM.md's 14:47 note
that SCOUT-OWN-4's "stops at 9/28-9/31" claim is wrong at least once) and **9/39** (3 rows, all already
**Decrypted**, dated 1526, a different item from ours). **No row for 9/33, 9/35, 9/37 or 9/42 in either
file.** This snapshot is dated 24 Sept 2026 (2 days old); it was not re-crawled live this session
(`tools/decode_list.py` would need on the order of tens of pages/minutes for a full non-decrypted-cipher
re-harvest, out of this job's box — flagged as a next step, not run). So: DECODE's coverage claim is
corrected (it does reach 9/34 and touches 9/39, not just 9/28-9/31), but still shows nothing for our five
items' signaturas as of the 24 Sept snapshot.

**(c) Tomokiyo.** `sources/cryptiana/web/spanish2C.htm` (already on file) read directly for the Ko.6/Ko.9
sections (quoted above) — confirms both correspondents' 1522-1523-era ciphers are reconstructed and gives the
two-cipher caveat for Soria. Its sibling `sources/cryptiana/web/AlonsoSanchez.htm` (already summarized in
SCOUT-OWN-4). Kolosova's own dissertation: the full 854pp doctoral text is not open (RODERIC serves only the
2016 Master's/TFM predecessor, 148pp, confirmed dead-end for a different target by job bLOP3 in
`ciphers/lope-hurtado-1522/NOTES.md` — not re-fetched here, same conclusion applies). **New this session**: a
WebSearch for "Lope de Soria" cifra turned up Eduardo Ibarra y Rodríguez y G. Arsenio de Izaga, *Catálogo de
los documentos del archivo de Lope de Soria, embajador del emperador Carlos V* (Boletín de la Real Academia de
la Historia, tomo 98, 1931) — **Soria's own printed archive catalogue**, with a search snippet stating some
Soria-Charles V correspondence carries "partes cifradas" (encrypted passages) with interlinear translations.
This is a strong, unopened lead: if this 1931 catalogue prints an interlinear decipherment for any of items
1-3 above, that item could be `found-solved`/period-keyed outright. **Not opened this session** — the only
online copy found (cervantesvirtual.com) is Cloudflare-blocked from the cloud (CLAUDE.md host table); the
UAM repository copy (`repositorio.uam.es/bitstream/handle/10486/1251/17136_D7.pdf`, a related article "Un
embajador de Carlos V en Italia: don Lope de Soria (1528-1532)") downloaded fine (2.6 MB) but this container
has no working PDF-text tool (`pdftotext`/`pdfinfo` not installed; `pypdf`/`PyPDF2`/`fitz` not importable,
and a `pip install pypdf` attempt crashed on a broken `cryptography`/`cffi` binding — not fixed, out of this
job's scope) and WebFetch's own summarizer could not read the scanned/image-heavy PDF. **Named next step**:
a worker with a working PDF-text tool (or `poppler-utils` installed) reads this UAM PDF and, if reachable, the
1931 BRAH catalogue itself (HathiTrust/archive.org, not yet searched for "Boletín de la Real Academia de la
Historia" tomo 98) for our five items by date/folio.

**(b) CSP Spain, printed calendar.** Confirmed via British History Online (not archive.org djvu.txt, faster
this session) that both correspondents are heavily calendared in vol.3 part 1 (1525-26) and part 2 (1527-29,
Gayangos): Index entries at vol3/no2 pp.1101-1102 (Soria) and pp.1095-1096 (Sánchez) list dozens of page
references for "Letters to emperor from Genoa (1525-1529)" and "Extensive letters to emperor (1525-1528)"
respectively. **This worker did not match these page references to the five exact dates** (17 Dec 1524, 21
Sept 1525, 16 Jun 1526, 14 Apr 1528, 17 Jun 1528) — BHO's per-fortnight page URLs for the missing ranges
(e.g. "September 1525, 11-20"/"21-30"; "April 1528, 11-20") did not resolve by guessed URL and BHO's own
search endpoint 403'd once, not retried (good-citizen rule). **This is the specific gap that keeps this
target `blocked` rather than `open`** per the intake gate's own wording ("names an edition it could not
[fully] read"): the edition is open and reachable, but the page-by-page match was not completed. Next step:
fetch the CSP Spain vol.3 no.1/no.2 month-pages by date directly (URLs are sequential ~10-day chunks; a
script that walks the sequence, rather than guessing, would find the right page in under 10 fetches per
date) and read whether each entry says "Autograph in cipher... Contemporary deciphering" (the same phrase
that flagged Lope Hurtado's no. 497 and R9644 as already-keyed, per `ciphers/lope-hurtado-1522/NOTES.md`).

**(a) Web search.** Two queries (see below): confirmed both correspondents' extensive published record and
surfaced the 1931 Soria-archive catalogue lead above; no source found stating any of these five items
specifically has been read or deciphered by anyone.

## RAH image route — negative, reproducible (this session)

**No page image obtained. The RAH's own online digital library (`bibliotecadigital.rah.es`) does not appear
to catalogue any of these five items at all** — this is a different, more decisive blocker than the
Anubis bot-challenge documented elsewhere in this repo for this host (`registro.do`/`catalogo_imagenes/
grupo.do` 307s): every search this session returned a normal HTTP 200 result page (not a challenge), and the
POST-to-`resultados_busqueda.do` route worked exactly as QUEUE.md's precedent describes, confirmed against a
known-good control:

- `busq_general=cifra` returns exactly the same 4 hits (1 Morillo item + 3 cartographic false positives)
  QUEUE.md and `ciphers/rah-morillo-1817/NOTES.md` already recorded — **the search engine works correctly**.
- `busq_general=cifrada` / `cifrado` / `descifrar` (the exact terms that surfaced the Morillo and Xiquena
  items in the 24-26 Sept sweeps) return, respectively: 3 hits (all Morillo/Xiquena, already known), 3 hits
  (same), 0 hits. **Nothing from the 1520s Salazar y Castro correspondence anywhere in this catalogue.**
- `busq_general="Lope de Soria"` (exact phrase, tried at both `/i18n/consulta/` and `/es/consulta/` paths) —
  **0 hits** ("No hay ningún registro que cumpla las condiciones de búsqueda").
- `busq_general="Alonso Sanchez"` — not separately retried after the phrase-search pattern above was
  established (see request count; folded into the "Soria" bare-word test below instead to conserve budget).
- `busq_general=Soria` (bare word) returns 20+ hits, all unrelated (Agreda, province of Soria genealogies) —
  the ambassador's name never appears as a title match.
- `busq_general="Salazar y Castro Carlos V"`, `"Colección Salazar y Castro A-33"`, `"Salazar y Castro
  correspondencia Carlos V"`, `A-33`, `Mirandola Soria` — either 0 hits or a broad, alphabetically-sorted
  listing of unrelated genealogical-treatise titles (the Colección's own compiled family trees, of which
  Luis de Salazar y Castro himself is often the *author*) with no title or visible field matching our
  correspondents, dates or shelfmarks.
- `busq_general="Salazar 9/33"` — one connection reset (`curl: Recv failure`), not retried (good-citizen
  one-retry rule; the very next query, on the same host 3s later, succeeded normally, so this reads as a
  transient network blip, not a block).
- OAI-PMH `ListSets` confirms the Access playbook's existing finding: only the generic `driver` set exists,
  no way to filter a harvest to this collection or these dates.

**Conclusion:** these five items are most likely catalogued *only* in the RAH's printed 49-volume Índice
(the physical finding aid SCOUT-OWN-4 found on Internet Archive) and have not yet been individually
digitized into the searchable online portal — unlike the Morillo papers, which clearly were digitized in
bulk with per-letter records. A page image is not obtainable from this host by any search term tried this
session. See `REQUEST.md`.

## Request counts (this session)

`bibliotecadigital.rah.es`: 15 POST search requests (1 phrase at `/i18n/`, 14 at `/es/`), all ≥3s apart
(one 3s gap hit a transient connection reset, not retried), well under the 40-request cap this job's brief
set; 1 OAI-PMH `ListSets` GET. No `imagen_id.do`/`browser_fetch.js` calls made (no record id was ever found
to fetch an image for). `github.com`: 2 shallow clones (`dbourdeau/cyphersolver`, `aaymeloglu/unsolved-
ciphers`), grepped and left on disk in the session scratchpad, not committed. `britishhistory.ac.uk`: 1
WebFetch (Index: S) + 2 failed WebFetch attempts on guessed month-page URLs (404s, not retried) + 1 403 on
the site's own search endpoint (not retried). `repositorio.uam.es`: 1 WebFetch (downloaded the PDF; not
readable this session, see above). WebSearch: 5 queries. No DECODE login, no image opened, no transcription,
no novelty wording (rule 10).

## Intake gate

```
$ python3 tools/intake_gate_check.py rah-salazar-soria-sanchez-1524-28
rah-salazar-soria-sanchez-1524-28: blocked (line 1) -- already terminal, nothing to gate
exit=0
```

## Check-solved page-by-page (NX2-GATE2, 26 Sept 2026) — three of five items already in print

**Method.** Fetched CSP Spain vol.III part 1 (`calendarofletter0003pasc`, Gayangos, 1873, archive.org
`_djvu.txt`) and part 2 (`calendarorleters0003vari`, Gayangos, 1877, archive.org `_djvu.txt`) once each;
CSP Spain vol.II (Bergenroth, 1866, covers to 1525) via archive.org `bub_gb_ZoY9AAAAcAAJ_djvu.txt` (poor
Google-Books OCR, cross-checked against British History Online's clean per-month HTML pages, which give
the same negative). Grepped by script for each correspondent and each of the five exact dates, then read
every matching entry by hand. `poppler-utils` (`pdftotext`) was installed this session (`apt-get install -y
-q poppler-utils`), fixing the "no working PDF-text tool" blocker NX2-GATE hit.

**Item 1 — Lope de Soria → Charles V, 21 Sept 1525, Genoa (A-35 ff.310-312, inv.5180): plaintext already
in print.** CSP Spain vol.III pt.1, No. 212 (pp.341-343, "LOPE DE SORIA, Imperial Ambassador in Genoa, to
the EMPEROR"). The full letter is given in English translation, with the cipher passages explicitly
marked inline — `(Cipher :) Has been informed that in the last conference held [at Milan]...` /
`(Common writing :) It would be highly advantageous...` — alternating for the whole entry. Ends: "Indorsed:
'To the King. 1525. From Genoa, Lope de Soria, 21 Sept.' Spanish. Original partly in cipher. Contemporary
deciphering. pp. 44." The shelfmark and date match item 1 exactly; the "Contemporary deciphering" note
means Gayangos worked from a period decipherment. **Item 1's plaintext (in English translation, drawn from
a period decipherment) is already published — no cryptanalytic campaign is possible or needed on it.**

**Item 2 — Lope de Soria → Charles V, 16 Jun 1526, Genoa (A-37 ff.428-429, inv.5540): not found in CSP;
remains genuinely open.** CSP Spain vol.III pt.1's calendar runs 13 June (No. 459, Alonso Sanchez to the
Emperor, deciphered) -> 13 June (No. 460, Sanchez to Soria, a note that "There is no longer occasion to use
our mutual cipher") -> 15 June (No. 461, Sanga to the Bishop of Porto, no cipher) -> 16 June (No. 462,
**Prothonotary Caracciolo**, not Soria — this is QUEUE.md's S3, already resolved as interlinear-deciphered
in the Índice itself) -> 17 June (No. 463, Jean Jonglet). **No Lope de Soria entry appears on or near 16
June 1526 in this volume.** This is consistent with the RAH's own "sin descifrar" cataloguing: unlike
items 1/3/5 below, Gayangos did not calendar this letter at all, which fits the pattern Tomokiyo records
(`AlonsoSanchez.htm` line 16: "more undeciphered letters in cipher are in BRAH... corresponding to
'M.Re.Ac.d.His.Salazar' in CSP" — i.e. the RAH-only, CSP-absent letters are the ones nobody has deciphered).
**Item 2 stays genuinely unresolved; a page image is still the only route.**

**Item 3 — Lope de Soria → Charles V, 14 Apr 1528, Mirandola (A-42 ff.243-244, inv.6417): plaintext already
in print.** CSP Spain vol.III pt.2, No. 399 (pp.653-654, "LOPE DE SORIA to the EMPEROR"), header "M. Re. Ac.
d. Hist. Salazar, A. 42" (shelfmark matches exactly). Multiple `(Cipher :)` sections in English translation,
including one with the original Spanish quoted verbatim in a footnote: *"Que el Papa ha concedido la
dispensacion para que el Rey de Inglaterra dexe su muger, y se case con la otra que quiere"* (news of Henry
VIII's divorce, reported in cipher from Mirandola). Dateline: "—La Mirandola, 14th April 1528" (place and
date match item 3 exactly; this is the same letter cited in passing, without addressing cipher status, by
Pizarro Llorente's UAM article, see below). Ends: "Spanish. Original partly in cipher. Contemporary
deciphering on separate sheet. pp. 7." **Item 3's plaintext is already published** on the same basis as
item 1 (a surviving period/contemporary decipherment).

**Item 4 — Alonso Sánchez → Charles V, 17 Dec 1524, Venice (A-33 ff.72-74, inv.4670): not found in CSP;
remains genuinely open.** CSP Spain vol.II (Bergenroth) covers this date; British History Online's clean
December 1524 page (`british-history.ac.uk/cal-state-papers/spain/vol2/pp683-687`) lists exactly six
entries for the whole month — Nos. 700 (1 Dec, Soria), 701 (7 Dec, Soria), 702 (12 Dec, treaty text), 703
(19 Dec, Emperor to Sessa/Gattinara), 704 (21 Dec), 705 (22 Dec) — jumping from 12 to 19 December with
**no entry on the 17th and no Alonso Sánchez entry anywhere in the month**. Cross-checked against the
archive.org OCR of the same volume (`bub_gb_ZoY9AAAAcAAJ`, a Google Books scan with heavy OCR corruption,
e.g. "1622" for "1522" — unreliable for exact-date greps on its own, but consistent: no Sánchez/December-1524
match found there either). **Item 4 stays genuinely unresolved; a page image is still the only route.**

**Item 5 — Alonso Sánchez → the High Chancellor (Gattinara), 17 Jun 1528, Venice (A-42, f.443, inv.6502):
plaintext already in print, but via Gayangos's own reading, not a period key.** CSP Spain vol.III pt.2,
No. 462 (p.714, "The SAME [i.e. Alonso Sanchez] to the HIGH CHANCELLOR"), addressed "Al Illmo. Señor el
Señor Gran Canceller, mi señor" — correspondent and addressee (Gattinara, not the Emperor — matching item
5's Índice note exactly, distinct from the immediately preceding No. 461 letter of the same date to the
Emperor, a *sixth*, different Sánchez item at A-42 f.429, not in our five). Gives a full, specific
`(Cipher :)` translation (named individuals, a bill-of-exchange transaction, travel plans) — but ends:
"Spanish. Holograph entirely in cipher. **No deciphering appended.** pp. 14." This is the opposite of items
1/3's "Contemporary deciphering" note: no period key survives attached to this letter, yet Gayangos still
prints its content in English, which can only mean **Gayangos solved this cipher himself** (a 19th-century
cryptanalytic reading, not a period decipherment) — a materially different kind of "already in print" than
items 1 and 3, worth flagging precisely for whoever grades this (CLAUDE.md's `ours`/`period`/`published`
key-source distinction, rule 10 addendum). **Item 5's plaintext is already published, by Gayangos's own
19th-century cryptanalysis.**

**Net effect on this target.** Three of the five original "held" items (1, 3, 5) already have their cipher
passages' content published in English translation in CSP Spain — no image, no key application, and no
cryptanalytic campaign is needed or possible for them; this repository's role for those three, if any,
would be transcribing/back-translating Gayangos's English into a plaintext record, not solving anything.
Only items 2 and 4 remain genuinely open cryptanalytic/recovery targets, and both still require a page
image (the RAH access route, see REQUEST.md) since neither is calendared in CSP at all — consistent with,
not contradicted by, the RAH's own "sin descifrar" marking for all five in the printed Índice (which
describes the *manuscript's own state*, not whether a later scholar separately deciphered and published a
translation elsewhere).

## The two Soria print sources (this session)

**UAM PDF (Pizarro Llorente, "Un embajador de Carlos V en Italia: don Lope de Soria (1528-1532)",
`repositorio.uam.es/bitstream/handle/10486/1251/17136_D7.pdf`), now read.** `poppler-utils` installed
(`apt-get install -y -q poppler-utils`); `pdftotext -layout` on the 37-page PDF (fetched via `curl -L`,
the plain URL 301-redirects) gave clean, if OCR-typo-riddled, running text. Grepped the whole 130 KB text
for `cifr`/`descifr`/`A-33`/`A-35`/`A-37`/`A-42`/`Mirandola`: **zero hits for `cifr` or `descifr`
anywhere in this article** — it is a straightforward diplomatic-history narrative, not a cipher-focused
source, and never discusses the correspondence's cipher/decipherment status at all. It cites **A-42, ff.
243-244 exactly once** (footnote, discussing item 3's own content — Soria writing from Mirandola about a
secret plan to travel to Milan) — the historian evidently read and paraphrased this letter's content
(consistent with item 3 having been solved and its content available, per the CSP finding above; the UAM
article does not itself reproduce a decipherment or address cipher status). No other RAH shelfmark from
our five items is cited anywhere in this article. **This source adds nothing beyond confirming item 3's
readability; it is not a cipher catalogue and does not print a decipherment.**

**The 1931 BRAH catalogue (Ibarra y Rodríguez & Izaga, "Catálogo de los documentos del archivo de Lope de
Soria, embajador del emperador Carlos V") — located precisely, confirmed unreadable from the cloud.**
Located via Dialnet (`dialnet.unirioja.es/servlet/articulo?codigo=9991374`): published in *Boletín de la
Real Academia de la Historia*, tomo 98, cuaderno 1 (1931), pp.363-416 — Dialnet is bibliographic metadata
only, "texto no disponible" (no PDF). Confirmed via HathiTrust's bibliographic API
(`catalog.hathitrust.org/api/volumes/brief/htid/osu.32435013919725.json`) that Ohio State University holds
a scan, record 102910157, but `rightsCode: "ic"` (in-copyright) with `usRightsString: "Limited
(search-only)"` — full text/page images are not reachable from the cloud (matches CLAUDE.md's HathiTrust
host-table row exactly); the HTRC Extracted Features API returned 404 for this volume (not in that corpus
either, presumably because it is not public-domain). Google Books API confirms the same record
(`F9FtpxiufdgC`, 60pp, 1931, `viewability: NO_PAGES`). archive.org's own Boletín collection tops out at
tomo 81 (never reaches 98). RAH's own digital catalogue (`bibliotecadigital.rah.es`, 2 new POST searches
this session, both broad/tokenized, no relevant hit — search engine tokenizes loosely and returned an
unrelated "Astronomie" result for a multi-word query, confirming this host simply does not hold the 1931
Boletín digitized) does not have it either. **This specific catalogue — the strongest remaining unopened
lead for items 2 and 4 — is confirmed located exactly (BRAH tomo 98, pp.363-416, 1931) but is genuinely
unreadable from the cloud by any route tried; it needs a HathiTrust-affiliated reader (LOCAL-QUEUE.tsv,
per CLAUDE.md's HathiTrust full-text/page-images host-table row) or a physical/JSTOR-style access route.**
One transient network failure (`Recv failure: connection reset`, Wayback CDX for the CORE.ac.uk PDF below)
not retried per the good-citizen one-retry rule.

## Kolosova and Tomokiyo sources, more precisely (this session)

`sources/cryptiana/web/spanish2C.htm`, Ko.6 and Ko.16 sections read directly: **Kolosova gives no specific
letter dates/shelfmarks for Ko.6** (Lope de Soria's main Charles-V cipher) beyond thesis page numbers
(substitution alphabet p.284, nomenclature p.307). For **Ko.16** (Soria's second, simpler cipher),
Tomokiyo's own note reads: "Lope de Soria usually used a full cipher (Ko.6), but used this simple cipher in
one letter (**I regret I could not find which one**)" — confirming NOTES.md's existing caveat cannot be
resolved from any on-file source: which of the two ciphers a given unseen Soria letter (items 1, 2, 3) uses
is undeterminable without an image, even for item 1 whose *content* is now known via CSP (Gayangos's
calendar entries do not identify which Spanish cipher key was used, only that one was).

`sources/cryptiana/web/AlonsoSanchez.htm` (Ko.9): confirms **all** of Tomokiyo's own DECODE-derived
specimen letters (R9509-R9614) are dated **1522**, none matching items 4 (1524) or 5 (1528) — the 2-6 year
gap flagged in this file's opening section stands unresolved. Tomokiyo's own summary line states plainly:
"Alonso Sanchez's letters to the Emperor and Chancellor... are calendared in [CSP Spain] vol.2 (1866)...
of which **most are labelled 'Autograph in cipher. Contemporary deciphering'**. However, **more
undeciphered letters in cipher are in BRAH**... (corresponding to 'M.Re.Ac.d.His.Salazar' in CSP)" — this
is exactly the pattern this session's CSP read confirms first-hand: the CSP-absent, RAH-only letters (items
2 and 4) are the ones nobody has deciphered; the CSP-present ones (items 1, 3, 5) already are.

Kolosova's dissertation itself: RODERIC's 2016 Master's/TFM predecessor (148pp) remains the only version
previously found open, per `ciphers/lope-hurtado-1522/NOTES.md` (bLOP3), not re-fetched. **New this
session**: a CORE API search (`api.core.ac.uk/v3/search/works/`, keyed) surfaced a direct `downloadUrl` for
what CORE indexes as the actual 2017 dissertation ("El lenguaje secreto de la diplomacia de Carlos V
(1521-1527)", 854pp) at `core.ac.uk/download/159375827.pdf` — but fetching it returns HTTP 404
`BlobNotFound` from CORE's own file server (`fileserver-az.core.ac.uk`) after the redirect: CORE's own
indexed copy is gone/stale. An OpenAlex search for the same title returned only Kolosova's *other*,
unrelated open-access articles (Mary Tudor/Granvelle ciphers), not this dissertation. A Google Books API
search found only `NO_PAGES`/`PARTIAL` snippets of the same work and its 2024 published successor. **Not
resolved this session** — named as a next step (retry the CORE record for a mirror, or a Google Scholar
check) but not pursued further given the box.

## A-42 ff.441-442 (S2 crib, inv.6501) re-examined — decodes Sánchez letters, not item 3 or (certainly) item 5

`sources/salazar-castro-index/cipher_mentions.tsv` row 1917 (inv.6501, A-42 f.441-442, dated 1528.06.17,
Venecia — the Índice's own dating of the *decipherment entry itself*, not necessarily of the letters it
decodes) gives the full index wording, truncated at: "Texto descifrado de los párrafos en cifra de los
tres documentos anteriores: **Cartas de Alonso** [Sánchez, continuation cut off by the TSV's own truncation
— not re-fetched this session, 30 MB source, out of this box]." **This decipherment sheet covers three
letters of Alonso Sánchez specifically** (plural "Cartas de Alonso" — Sánchez's cognomen is the obvious
completion given his name recurs throughout this run of A-42 folios), **not** item 3 (a Soria letter, whose
own CSP entry cites an entirely separate "Contemporary deciphering on separate sheet" not this one) and
likely **not** item 5 either, despite the two being catalogue-adjacent (inv.6501/6502): item 5's own CSP
entry explicitly says "No deciphering appended," which is hard to square with a period decipherment sheet
sitting in the very next two folios of the same legajo — unless that decipherment sheet was compiled
*after* Gayangos catalogued item 5, or covers three *other* Sánchez letters from nearby folios in A-42
(plausibly among rows 8/9/11/12/13/15/17 in QUEUE.md's list, six more undeciphered Sánchez items in this
same A-37/A-41/A-42 run) rather than item 5 itself. **Not resolved this session** — the exact three letters
this sheet covers needs either the full Índice OCR re-read around inv. 6498-6501 (not done here, budget) or
the RAH's own image of ff.441-442 (requested below regardless, since it is cheap — two folios, same legajo
as items already being requested).

## Verdict for the orchestrator

**Still `blocked`, not `open` or `closed-negative`** — no page images obtained for any of the five folios
this session either, and two of the five items (2 and 4) remain genuinely unresolved with no route to a
reading short of a physical/RAH-image or HathiTrust-affiliated read of the 1931 BRAH catalogue. **But three
of the five items (1, 3, 5) are no longer cryptanalytic targets at all: their plaintext (in English
translation) is already published in CSP Spain** (Gayangos, vol.III parts 1 and 2, 1873/1877) — items 1
and 3 via a surviving period/contemporary decipherment, item 5 via what appears to be Gayangos's own
19th-century solving of a cipher with no period key attached. This is a search result about print, not a
decipherment performed here, and not this worker's novelty classification to make (rule 10) — a verifier
should confirm these three CSP entries against the exact RAH shelfmarks (folio-level matches are inferred
from date+place+correspondent+addressee, not from an RAH image) before any outward claim. **Not Bourdeau's
or Aymeloglu's lane** (unchanged from NX2-GATE). **REQUEST.md** below narrows to a much smaller ask: a
period decipherment/crib check plus images for items 2 and 4 only, and the 1931 BRAH catalogue read
(now precisely located) as the cheapest remaining route to settle those same two items without any archive
visit.

## Request counts (this session, NX2-GATE2)

`archive.org`: 4 fetches (CSP Spain vol.III pt.1 djvu.txt 3.1 MB, pt.2 djvu.txt 3.5 MB, vol.II djvu.txt
3.4 MB, one `advancedsearch.php` metadata query), each preceded by a request to the item's own metadata
endpoint (1 more) — 6 total, >=1.5s apart. `repositorio.uam.es`: 1 fetch (2.6 MB PDF, redirected). Google
Books API (`googleapis.com/books/v1`, keyed + `country=US`): 2 queries. `catalog.hathitrust.org`: 2 (bib
API brief lookup, one by OCLC that returned an unrelated record, one by htid that resolved correctly).
`data.htrc.illinois.edu`: 1 (404, not in that corpus). `dialnet.unirioja.es`: 3 fetches (journal listing,
tomo-98 issue page, article page), >=1.5s apart. `bibliotecadigital.rah.es`: 2 POST searches, >=3s apart.
`api.openalex.org`: 1 (keyed). `api.core.ac.uk`: 2 (keyed; one search, one that returned no results for an
exact-phrase query). `core.ac.uk`/`fileserver-az.core.ac.uk`: 1 (404 after redirect, not retried).
`web.archive.org`: 2 attempts (CDX lookup), both a transient connection reset, not retried (good-citizen
one-retry rule already exhausted by the two attempts landing as one logical try). `british-history.ac.uk`:
2 WebFetch calls (vol2 landing page for the December 1524 URL, then the December 1524 page itself).
WebSearch: 2 queries. No DECODE login, no image opened, no transcription, no novelty wording (rule 10).
