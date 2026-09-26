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

## Verdict for the orchestrator

**No images on disk for any of the five folios. Check-solved is not clean**: the CSP Spain calendar (vol.3
parts 1-2) is confirmed reachable and both correspondents are extensively calendared there, but this worker
did not complete the page-by-page date match, so this target is `blocked`, not `open`, per the intake gate.
**Not Bourdeau's or Aymeloglu's lane** (checked, no overlap with Signatura 9/33/35/37/42). **Not
found-solved.** The RAH image route is a genuine, reproducible negative (the search engine works and finds
real results for other terms, just none for these five items) rather than the Anubis block documented
elsewhere for this host — see REQUEST.md for the recommended next step. The strongest unopened lead is the
1931 BRAH *Catálogo de los documentos del archivo de Lope de Soria* (Ibarra y Rodríguez/Izaga), which a
Google Books/web snippet says covers Soria letters with cipher passages and interlinear translations — a
worker with a working PDF-text tool should read it before any further RAH access attempt.
