# Novelty audit: ciphers/vanbeuningen-dewitt-1657

Verifier: OX-VBV (Sonnet), LANE OX, 25 September 2026. Separate session from the solvers (OX-VB transcription,
OX-VBS/OX-VBS2 key recovery); this session did not decode and does not protect their conclusions.

**Claims under audit** (as the repo states them, `NOTES.md` "Archive location pinned" and "Key recovery"
sections):
1. NA 3.01.17 inv.nr 1538 ff.210-211 (the cipher copy, "van een andere hand") is the same letter as the plain
   copy ff.208-209 and as *Brieven aan Johan de Witt* I, pp.405-406 (Fruin/Japikse 1919).
2. The cipher's system is clear Dutch function words + a 9-entry nomenclator + a homophonic letter alphabet,
   and `key.tsv` (53 code-values, 446/517 coded tokens grade C) recovers it.

## Verdict table

| item | N-class | prior plaintext | prior decipherment/key |
|---|---|---|---|
| 1. The letter's text (19/29 Sept 1657, Van Beuningen to De Witt) | **N1** | yes -- Fruin/Japikse 1919, from the plain copy | no (the cipher copy itself was never deciphered; see item 2) |
| 2. The key / decipherment of *this cipher copy* (ff.210-211) | **N3** | -- | no prior key or decipherment located after the search below; Postma 2006, the standard modern study of this exact correspondence, could not be read directly (see gaps) |

## 1. Extraction from the repo

- **Date/parties**: 19/29 September 1657 (Julian/Gregorian), Coenraad van Beuningen (Dutch envoy at Copenhagen)
  to Johan de Witt (Grand Pensionary of Holland).
- **Plaintext** (already in print, grade H, `plaintext_print.txt`): a report on Danish court affairs,
  Anglo-Danish diplomacy (the envoy "Rosewinge"/Corfitz Ulfeldt-adjacent court business, "geobtineert op sijn
  versoeck"), an English ambassador at Elsinore, Sweden/Denmark relations, and a request for orders.
- **Ciphertext**: `ciphertext.tsv`, 862 tokens (517 coded + 345 clear Dutch), transcribed from
  `images/cipher_crops/0210_right.jpg` and `0211_left.jpg` (NL-HaNA_3.01.17_1538_0210-0211).
- **Distinctive phrases/identifiers**: "Rosewinge", "Rijcxhoffmeester", "geobtineert op sijn versoeck",
  "onopgelost cijfer van een andere hand" (the editor's own footnote), "Vereenichde Nederlanden",
  "danckbaerheyt", NA 3.01.17 inv.nr 1538, the Fruin/Japikse *Brieven aan Johan de Witt* I p.405 citation.
- **What the solvers searched** (24-25 Sept 2026, `NOTES.md`): Cryptiana `dutch.htm`, DECODE's 24 Sept
  catalogue snapshot, fresh shallow clones of both solver repositories, WebSearch, the printed edition's own
  front matter and footnotes, EMLO, and a citing scriptie (vriendenvandewitt.nl) of Postma's book (grepped for
  "cijfer"/"geheimschrift": zero hits in 1122 lines). Academia.edu returned 403 for Postma's own book, not read.

## 2. Independent search (this session, 25 Sept 2026)

Families searched, logged as searched or unreachable, per the verifier template and the brief's item list:

**(a) Fruin/Japikse indexes and introductions.** Read directly (not re-derived from the harvest): the printed
edition's own footnote to this letter (p.405, note 1) states plainly "Dezelfde brief ook in onopgelost cijfer,
van een andere hand" -- the editor knew of the cipher copy and explicitly says it was *not* deciphered at time
of printing (1919). No index entry for "cijfer"/"sleutel" checked beyond this footnote and the front-matter
passage already quoted in `NOTES.md` (p.XVI, "de brieven aan De Witt alle eigenhandige originelen zijn").
Searched.

**(b) M. Postma, *Johan de Witt en Coenraad van Beuningen: correspondentie tijdens de Noordse oorlog
(1655-1660)*** (Utrecht doctoraalscriptie, 2006; OpenAlex W156503838, type "dissertation", author M. Postma).
Not read directly this pass either: Academia.edu still 403s (per `NOTES.md`); the OpenAlex-listed landing page
`dspace.library.uu.nl/handle/1874/8472` now 404s (stale handle, most likely migrated to
`studenttheses.uu.nl`); queried that repository's own DSpace 7 REST search API
(`studenttheses.uu.nl/server/api/discover/search/objects?query=...`) for "Postma Beuningen Witt" and for the
Dutch title directly -- no matching record found (3 unrelated De Witt-adjacent theses returned). Also queried
`dspace.library.uu.nl`'s own current REST API directly -- no match. **This is the standard modern study of
exactly this correspondence circle and remains genuinely unread; logged as a gap below, not scored as a
negative.** A related citing work (a vriendenvandewitt.nl scriptie that cites Postma ~20 times) was already
searched by the solver and contains zero mentions of "cijfer"/"geheimschrift" in its own text -- real evidence
that the *citing* paper does not discuss the cipher, not evidence about Postma's own book. Unreachable by two
routes across two sessions; queued as a JSTOR row this pass (see below) in case Postma's work or a review of it
is indexed there, though a scriptie itself is unlikely to be on JSTOR -- the row also covers the correspondence
generally.

**(c) NA 3.01.17's own inventory**, searched for a key ("sleutel", "cijfer", "cypher", "chiffre",
"geheimschrift", "onopgelost") anywhere across the whole archive's finding aid: fetched the full EAD XML
(`www.nationaalarchief.nl/onderzoeken/archief/3.01.17/download/xml`, 3.1 MB, one request) and grepped it --
**zero hits for any of those six terms anywhere in the entire De Witt archive's catalogue description**,
including its own entry for inv.nr 1538. The archive's own finding aid does not note a separate key item among
De Witt's papers. Searched, negative.

**(d) Karl de Leeuw on Dutch diplomatic ciphers, 17th century.** Located via OpenAlex (`OPENALEX_KEY` as
Bearer header): his PhD thesis *Cryptology and statecraft in the Dutch Republic* (2000, UvA) is green open
access (`pure.uva.nl/ws/files/3074957/12760_Thesis.pdf`, fetched, 21.4 MB, `pdftotext`'d, 12,813 lines read in
full by grep). This is the definitive scholarly source the brief named. Findings:
  - Grepped for "beuningen": two hits. One (p.20-21 of the thesis) discusses a **different, later** Van
    Beuningen cipher letter -- 1668, Van Beuningen as ambassador *in France* (by then), to Burgersdijk and Van
    der Togt, reported via the 18th-century historian Wagenaar, with 2-digit letter-codes not exceeding 97 and
    3-4 digit nomenclator codes not under 344. Not this letter (different year, different recipients, different
    posting, different code-value ranges from our key's 4-65/104-225). The other hit is the unrelated 1785
    Rechteren-tot-Borgbeuningen item already flagged as a surname false positive.
  - Grepped for "1657", "rosewinge", "copenhagen"/"coppenhagen"/"kopenhagen", "denemark": no hit connects to
    this letter, its envoy, or its cipher.
  - **Directly relevant context, not a match**: de Leeuw dates the *start* of systematic Dutch diplomatic
    codebook-keeping to two 1657/1658 measures -- 21 July 1657 (centralising despatch handling in one official)
    and 20 Sept/4 Oct 1658 (Pieter van Peenen appointed to make and guard codebooks) -- with the large,
    standardised 10,000+ item nomenclature dating from that reorganisation onward. Our letter (19/29 Sept 1657)
    predates Van Peenen's appointment by just over a year, consistent with its key being a small, ad hoc
    9-entry nomenclator rather than the later elaborate system -- useful corroborating context for the system
    identification, not a prior decipherment of this item. de Leeuw does not mention this letter, its cipher,
    or a key for it anywhere in the thesis. Searched, negative, one directly relevant contextual passage found
    and quoted above (not a prior print of this item).

**(e) Internet Archive / HathiTrust full text.** `be-api.us.archive.org` full-text search (works even for
lending-only items) on "Rijcxhoffmeester" (a distinctive compound in this letter): 2 hits, both in Laursen's
*Traités du Danemark et de la Norvège* (1907, French-language treaty-collection series, `traitsdudanemar02/
00denmgoog`). Downloaded and read the actual matching lines (`tools/print_check.py`'s cached djvu text): the
hits are "Corfits Ulefelt, Riicxraet, Riicxhoffmeester" -- Corfitz Ulfeldt, a specific, well-known Danish
nobleman, holding the generic court title "rijkshofmeester" in an entirely different (French-language, treaty,
not correspondence) document. A title-word coincidence, not this letter. All six phrases from `phrases.txt`
also run against IA-global, Google Books, OpenAlex, HathiTrust and CrossRef via `tools/print_check.py`
(`print-check.tsv`, `print-check-hosts.tsv`): every plaintext-phrase hit on Google Books traces only to the
Japikse 1919 edition itself (*Brieven aan Johan de Witt*, *Werken uitgegeven door het Historisch Genootschap*
1918/1919) -- no independent secondary print. No HathiTrust hit. Searched.

**(f) Solver repositories, DECODE, Cryptiana, Cipherbrain.** Fresh shallow clones of both
`dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers` this pass (25 Sept, one day after the solver's own
19 Sept-vintage check): grepped for "beuningen", "3.01.17", "nieuwpoort" -- only known false positives (the
1785 Rechteren-tot-Borgbeuningen item, the "Oostende en Nieuwpoort" city name in an unrelated Affry 1757 note,
a bare link to the 3.01.17 archive landing page in a different unsolved-ciphers target, vande-perre-1653).
No hit for this target in either repository. DECODE's local 24 Sept catalogue snapshot
(`sources/decode/records-non-decrypted-2026-09-24.tsv`, `records-decrypted-2026-09-24.tsv`) grepped again: no
genuine hit (the one "1538" match is an unrelated Vatican archive's date range, 1538-1612). Cryptiana
`dutch.htm` re-read: only the already-flagged "Beverning and Nieuport" (different ambassadors, unrelated
letter) false positive. No local Cipherbrain/schmeh snapshot mentions Beuningen. Searched.

**(g) JSTOR.** Appended one row to `JSTOR-QUEUE.tsv` for the owner's local runner: `"Van Beuningen" AND "De
Witt" AND (cijfer OR cipher OR sleutel) AND (Noordse OR Denemarken OR 1657)`. Queued, does not block this
class per the outreach rule.

**Scholarship, open indexes** (`OPENALEX_KEY` Bearer header, `S2_KEY` x-api-key header, `crossref` unkeyed):
`tools/print_check.py`'s openalex/crossref/s2 passes and manual OpenAlex/Semantic Scholar searches for
"Coenraad van Beuningen", "Karl de Leeuw Dutch diplomatic cipher", "Postma Johan de Witt Coenraad van
Beuningen", and direct phrase searches -- no work found that discusses this specific 1657 letter, its cipher
copy, or a key for it, beyond de Leeuw's thesis (searched directly, see (d)) and Postma's book (unreached, see
(b)). Semantic Scholar 429'd twice (rate limit despite the key, re-tried once each per the one-retry rule,
logged, not chased further).

## 3. Key soundness check (not re-solving)

`tools/decode_key.py ciphers/vanbeuningen-dewitt-1657 --check` exits 0 (`ciphertext.tsv: tokens 862: C 446, M
70, U 1, clear 345`; reading up to date).

Sampled the decode directly against the manuscript images (`images/cipher_crops/0210_right.jpg`,
`0211_left.jpg`), not just the printed alignment:
- L03-L05 (`40,50:59,50,51,21:22,12,23,51,32,61,10,57,51:bij49,51:23,25,40,51,25:`) reads cleanly against the
  image as "d[40] e[50] : h[59] e[50] e[51] r[21] : r[22] o[12] s[23] e[51] w[32] i[61] n[10] g[57] e[51] : bij
  d[49] e[51] : s[23] t[25] d[40] e[51] t[25] :" -- "de heer : Rosewinge : bij de : stdet :" (the code-40
  conflict's "Staet" mismatch visible in situ, exactly as `NOTES.md` describes it, not a transcription error).
- On leaf 0211 (later in the letter), the run "de 40,57,50,10,25:" against the image reads clearly as a
  5-code word directly after "dat" -- matching the plaintext's "omdat de agent van de Coningh van Denemarcken"
  and confirming this specific occurrence of code 40 votes 'a' (agent), consistent with `conflicts.tsv`'s
  own account of the 40=d|a split rather than a mis-transcription.
- The 9-entry nomenclator's codes (143, 144, 173, 213, 222 etc.) are visible in the image exactly where
  `NOTES.md`'s context table places them (e.g. "144:" preceding "Willemsmaker om" and followed by
  "40,50:27,21,20,10,25,24,46,59,41,17,27,39,10:" = "de vruntschap van dese Croon", matching the "Haer Hoog
  Mog. de vruntschap van dese Croon" alignment claimed).

No transcription or key error found in this sample; the two flagged conflicts (codes 11, 40) are visibly real
ambiguities in the cipher's own design at those positions, not transcription slips -- consistent with
`key.tsv` keeping them at grade M rather than forcing a value. This session did not attempt to resolve either
conflict (out of scope: "do not decode").

## 4. Postmortem

No over-claiming sentence found in `NOTES.md`, `reading.txt`, `key.tsv` or `decode.json`: the folder already
uses "partial", never claims the cipher copy or its plaintext is new, unpublished, unread or first-deciphered,
and explicitly states the plaintext is already in print. Nothing to correct.

**What would move item 2 from N3 to N4**: reading Postma 2006 directly (still unreached after two sessions'
attempts across two different routes), and an answer to the queued JSTOR row. Both are named gaps, not
silently skipped.

## Safe / unsafe sentences

- **Item 1 (the letter)**: Safe -- "The plaintext of this letter is already in print (Fruin/Japikse, *Brieven
  aan Johan de Witt* I, 1919, pp.405-406); the cipher copy (NA 3.01.17 inv.1538 ff.210-211) had not itself been
  deciphered by that edition, which calls it 'onopgelost cijfer'." Unsafe -- any wording implying the letter's
  content is new or unpublished; it is not.
- **Item 2 (the key/decipherment of this cipher copy)**: Safe -- "No prior key or decipherment of this specific
  cipher copy was found in the sources searched 24-25 Sept 2026 (this file); the standard modern study of this
  exact correspondence, M. Postma's 2006 dissertation, could not be read directly and remains a named gap."
  Unsafe -- "first decipherment", "previously unread", "newly recovered" or similar (rule 10; not reached
  without Postma read and the JSTOR row answered, i.e. not below N4).

## Search log summary (host/request counts, this session)

`www.nationaalarchief.nl` 1 (EAD XML download), `api.openalex.org` ~12 (works search + rate-limit-free
`tools/print_check.py` pass), `api.semanticscholar.org` ~10 (2 manual + `tools/print_check.py`'s pass, 2x
429'd, one retry each per the good-citizen rule), `api.crossref.org` ~6 (retried once after a 429),
`www.googleapis.com` (Google Books) ~9, `be-api.us.archive.org` ~8, `archive.org` 2 (djvu text downloads via
`tools/print_check.py`'s cache), `pure.uva.nl` 1 (de Leeuw thesis PDF, 21.4 MB), `dspace.library.uu.nl` 2,
`studenttheses.uu.nl` 2, `books.google.com` 1 (browser_fetch, not used further once search-within-volume
worked), `github.com` 2 (fresh shallow clones). No subagents used. All single-host, >=1.5s apart, no 429 except
the two noted (each retried once, not chased further).
