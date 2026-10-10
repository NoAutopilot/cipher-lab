open
Bescheiden betreffende het beleid van Johan van Oldenbarnevelt, deel II (ed. A.J. Veenendaal, RGP Grote
Serie GS 108), no. 92, pp.110-111, read by this worker at resources.huygens.knaw.nl/retroboeken/oldenbarnevelt
(digital edition, source=2, page_index=124-125); the edition's own full-text search across all three
volumes (deel 1-3, GS80/GS108/GS121) was run for `cijferschrift`, `sleutel`, `gecijferd` and `cijfer` and
every hit read on the actual page (not the snippet), 25 Sept 2026.

## Status

`open`. Handed to LANE TX by LANE VX (ROOM.md 07:53, 25 Sept 2026), who found it via the editor's own preface
while doing check-solved + key search on a different Oldenbarnevelt letter (na-oldenbarnevelt-2442-1605).

## What is established (H-grade: read directly from the source)

- **Item**: no. 92 in Veenendaal's edition, *Bescheiden betreffende het beleid van Johan van Oldenbarnevelt*,
  deel II (1602-1613), GS 108. Printed pp.110-111. Editorial heading (in square brackets, i.e. supplied by
  the editor, not read from a signature): "[P. VAN BREDERODE AAN OLDENBARNEVELT], 21 februari 1605." The
  letter itself ends "UE. onderdanigen ende getrouwen dienaer" with no name -- the attribution to P. van
  Brederode is the editor's inference, not an explicit signature.
- **Place/date**: "Uyt Heydelberg, desen 21en february 1605" -- written from Heidelberg (seat of the
  Elector Palatine), 21 Feb 1605.
- **Archival citation**: "A.R.A., Holland 2613, e. Duplicata." (Algemeen Rijksarchief, series "Holland",
  invnr 2613, item e; marked as a duplicate copy -- the toegang/inventaris number at the modern Nationaal
  Archief has not been resolved this pass, see Open below).
  For comparison: the immediately preceding letter (no. 91) cites "A.R.A., Holland 2589, b 4. Ondert.
  oorspr." (an original, signed).
- **Editor's own statement** (voorwerk p.XIII, images/voorwerk_XIII.jpg): "Cijferschrift kwam in dit deel
  maar in een stuk voor, nr. 92; ik zou het hebben opgelost, als ik gekund had. Maar de sleutel erop heb ik
  niet kunnen vinden, en de brief bood te weinig vergelijkingsmateriaal om daaruit de oplossing te halen."
  ("Cipher writing occurred in this volume in only one piece, no. 92; I would have solved it if I could
  have. But I could not find the key to it, and the letter offered too little comparison material from
  which to derive the solution.") This is a distinct sentence on the same page from the one an earlier
  harvest (sources/huygens/NOTES.md, "False positive from an ambiguous Dutch word") flagged as a false
  positive -- that flag concerns an *earlier* sentence on p.XIII ("Uren heb ik soms besteed aan de
  ontcijfering van een enkel woord", about palaeography, i.e. reading old handwriting), not this one. Both
  readings were checked against the fetched page text this pass; they do not contradict each other, and
  this sentence is unambiguously about a real, unsolved cipher.
- **Design**: a nomenclator/code embedded inline in otherwise plain Dutch prose -- numeral groups (mostly
  2-3 digits, one Roman numeral "XLII") stand for names, entities or amounts scattered through ordinary
  running text, not a solid block of ciphertext. Confirmed by eye against both page images
  (images/p110.jpg, images/p111.jpg) -- OCR and image agree exactly, including every numeral.
- **Extent** (counted by hand from the verified page text, excluding the literal sums "30.000" and "12 off
  13.000" which are money amounts written in the clear, not codes, and excluding footnote-reference
  superscripts): approximately 121 Arabic-numeral code tokens across the two pages (32 on p.110, 89 on
  p.111), plus one Roman-numeral token (XLII) immediately preceding a run of Arabic codes. Roughly 100
  distinct values, range 30-741 (a handful, e.g. 611, 617, 628, recur up to 5 times each, consistent with
  a small number of frequently-named parties). This is an approximate count for description, not a claimed
  reading; no judge run applies since nothing is being decoded here.
- **Language of the clear parts**: Dutch (with the recurring honorific "U E." = Uwe Edele/Excellentie).
  The letter this one answers/continues from and the one after it (no. 93, Louise Juliana to Oldenbarnevelt)
  are in French; no. 92 itself is entirely Dutch prose with the embedded numeral codes.

## Key route (S/negative)

Searched the same edition's own full-text search (all three volumes) for `cijferschrift` (6 hits),
`sleutel` (14 hits), `gecijferd` (0 hits) and `cijfer` (20 hits); every hit opened on the actual printed
page, not the snippet. Findings:
- Deel 1 (GS80, 1570-1601) has its own, separate cipher material -- several letters involving Calvart,
  Aerssen and others, with a key described repeatedly ("Zie den sleutel in Leg. 611 IV", pp.263-271,
  397-398, 555) and one item (p.378/397, this edition's no. 221) where "de sleutel is [in] hetzelfde
  dossier aanwezig" (the key survives in the same dossier) -- already flagged and excluded as an F-type
  item by the 24 Sept 2026 harvest (sources/huygens/cipher-letters-2026-09-24.tsv row for
  "Legatie-Archief 611, IV"). None of this concerns Brederode.
- Deel 3 (GS121, 1614-1620) front matter (pp.IX-X, XIII) describes a different, separately reconstructed
  partial key ("3x = La Noue, 7 = Brunswijk...") for yet another correspondence in that volume, and several
  more individually-solved cipher passages (pp.137, 151, 181, 182, 191-199) each with its own note. None
  mention Brederode, and none of the numeral ranges quoted in the search snippets overlap the 30-741 range
  used in no. 92 in a way that suggests a shared key (not exhaustively cross-checked digit-by-digit; a
  worker who transcribes for decoding should still verify this rather than take the non-overlap on faith).
  Deel 2's own preface (p.XIII) is explicit that no. 92 is the volume's *only* ciphered item, and separately
  (p.XIII, a different sentence again, "Van geen van beide heb ik de sleutel aangetroffen") the editor did
  not find the key to two other items either -- those two are in Deel 3, not Deel 2, and not Brederode's.
- **No other P. van Brederode cipher letter found** in this edition, in WVO (Willem van Oranje database;
  queried `opmerkingen=Brederode`, 12 hits, all dated 1552-1576, entirely within Willem I's lifetime and
  irrelevant to this 1602-1613 correspondent), in the two solver repositories (dbourdeau/cyphersolver and
  aaymeloglu/unsolved-ciphers, shallow-cloned and grepped for `brederode`/`oldenbarnevelt` -- the only hits
  are incidental: a word-frequency corpus entry, and an unrelated 1646 royalist key naming "the Brederodes"
  as subjects, not as correspondents), on Cipherbrain (Klaus Schmeh's blog and "Top 50 unsolved encrypted
  messages" list -- no match by web search), or on Cryptiana (Tomokiyo's site -- no match by web search).
  **Zero cipher/plaintext pairs exist for this correspondent as far as this search reached**; this is a
  solitary occurrence, matching the editor's own "too little comparison material" diagnosis.
- Karl de Leeuw's 1993 Cryptologia article with H. van der Meer ("A Homophonic Substitution in the Archives
  of the Last Great Pensionary of Holland") is about a different pensionary (Laurens Pieter van de Spiegel,
  1787), not Oldenbarnevelt -- not relevant. De Leeuw is a co-author on a much larger 2024 Cryptologia survey
  ("Keys with nomenclatures in the early modern Europe", Megyesi, Tudor, Láng, Lehofer, Kopal, de Leeuw,
  Waldispühl, Cryptologia 48(2):97-139), covering 1,600+ historical cipher keys from ten countries -- this
  could conceivably include a Dutch nomenclator matching this letter's numeral range, but the article is
  behind a Taylor & Francis paywall and was not read this pass (not queued to JSTOR-QUEUE.tsv or checked via
  OpenAlex/Semantic Scholar this pass -- a genuine open lead, not a search result yet).
- Jan den Tex's biography *Oldenbarnevelt* (which would be the natural secondary source for the 1605
  Palatinate mission and might discuss this letter or a related key) is hosted in full text at
  dbnl.org/tekst/tex_003joha01_01/ but the host failed TLS (`SSL_ERROR_SYSCALL`) on both the first attempt
  and the one permitted retry; not read this pass, logged per the good-citizen rule rather than retried
  further.
- The archival citation "A.R.A., Holland 2613, e. Duplicata." was not traced to a modern Nationaal Archief
  toegang/invnr this pass (out of this job's scope; a lead for whoever does archival access work on this
  target -- a "Duplicata" note raises the same possibility flagged elsewhere in this repository for other
  targets, that the original or a decoded duplicate sits elsewhere in the same series).

**Conclusion**: no key, sibling decipherment, or published solution located by any of the six CLAUDE.md
rule-1 sources (search engine, sender's printed correspondence [this edition itself, since Brederode has no
separate published Lettres], calendars/state-paper series [not applicable, Dutch domestic], list-post
comment threads [Cipherbrain, Cryptiana], DECODE [web-search restricted to de-crypt.org, no hit], the two
solver repositories) plus the edition's own full-text search of all three volumes and a WVO query. This is a
genuine open item: a single ~120-token nomenclator/code letter with no sibling and no key found anywhere
searched. Per LESSONS.md section 3 ("large nomenclator, one letter"), a single short letter using roughly
100 distinct code values is a poor ciphertext-only cryptanalysis target without a key or a sibling in the
same key -- exactly the editor's own diagnosis in 1934(ish; Veenendaal's edition date not checked this
pass).

## Access

Digital edition text and page images: no login, no blocks, resources.huygens.knaw.nl. Images fetched to
`images/` (p108-p112, plus the voorwerk_XIII preface page); folder well under the 30 MB cap.

## Open (for whoever continues)

- De Leeuw et al. 2022 "Keys with nomenclatures" (Cryptologia 48(2), 2024) now read in full by the local
  runner (LOCAL-QUEUE row L12, see "Local runner L12 recheck" below): no qualifying individual Dutch key
  1600-1610 found in the paper itself; this closes the paper as a lead but does not rule out an individual
  record in DECODE.
- Den Tex's *Oldenbarnevelt* biography (dbnl.org, full text online) not yet read -- host TLS-failed twice
  this pass; retry from a fresh session/container.
- "A.R.A., Holland 2613" (and "2589") does NOT match toegang 3.01.04.01's (Staten van Holland) own numbering
  by direct EAD lookup (YX-OBR, 25 Sept 2026, below) -- likely a pre-reorganisation "dubbelen Holland" series
  number not yet traced to its current home; NA's own catalogue search (client-rendered, needs a real browser)
  not yet tried for this.
- NL-HaNA 1.01.02 inv. 6016's whole "1605-1606" year-folder (image order 260-349) has now been read leaf by
  leaf (YX-OBR, 25 Sept 2026, below) with no cipher, key or interlinear decipherment found -- this specific
  lead is closed. The bundle's other year-folders (1602-1603 at order 1, 1607-1608 starting order 350, and
  onward to 1613) have not been walked.
- No transcription-for-decoding pass has been done; the ~121-token count above is a by-eye description, not
  a token-by-token key-recovery transcription.

## Key hunt (TX-KEYS, 25 Sept 2026, 08:57-09:15 UTC)

Job: find a key sheet or deciphered sibling of Pieter Cornelisz. van Brederode's cipher, 1600-1610, per
`.claude/briefs/runs/2026-09-25-lane-tx-keys.md`. **No key sheet or deciphered sibling found this pass**; one
substantial unexplored lead identified (NA 1.01.02 inv. 6016) and one access gap (de Leeuw et al. 2022, transient
connection failure, not a paywall).

### 1. NA 3.01.14 (Oldenbarnevelt archief), full EAD XML

Downloaded the whole finding aid as XML (`nationaalarchief.nl/onderzoeken/archief/3.01.14/download/xml`, 4.97 MB,
4448 items) and grepped locally for `sleutel` (3), `cijfer` (2), `chiffre` (0), `Brederode` (30). All read in
context:
- `sleutel`/`cijfer` hits are unrelated: a 1586 "verdeelsleutel" (division formula for money, not a cipher key);
  a key sheet for the **Buzanval** cipher (Oldenbarnevelt's correspondence with Choart de Buzanval, French
  ambassador -- invnr 2028, "Stuk houdende de sleutel voor de decodering van de code die Johan van Oldenbarnevelt
  gebruikte in zijn correspondentie met Paul Choart, heer Van Buzanval"); a cipher/decode note on a different
  bundle (1598-1602/1605-1609 correspondence with France, invnr not captured, "Bij de missive van 1598 augustus
  10 bevindt zich een sleutel"). None involve Brederode.
- Of the 30 Brederode hits, two are digitised items in this same archive by our exact correspondent, but **not
  cipher**: invnr **2477** (bundle "Missiven van Johan van Oldenbarnevelt" 1609) contains an item-level entry
  "Missive van Johan van Oldenbarnevelt aan Pieter Corneliszn. van Brederode... van 2 november 1609... concept",
  printed RGP 108 pp.378-379; invnr **1699** is "Missive van Pieter Corneliszn. van Brederode, diplomatiek agent
  in Duitsland, aan Johan van Oldenbarnevelt van 18 juni 1612", printed RGP 108 pp.517-521, digitised (dao METS
  link present). Both are in RGP 108, the **same printed volume** as our target letter -- but the editor's own
  preface (already quoted above) states no. 92 is the *only* ciphered item in the whole volume, so neither of
  these two letters is itself in cipher; they are plain correspondence between the same two people, useful only
  as biographical context, not as a key/sibling route.
- No other Brederode item in this archive is flagged as ciphered or carries a "sleutel" annotation.

### 2. NA 1.01.02 (Staten-Generaal), full EAD XML -- the one substantial lead

Downloaded the whole finding aid (22.7 MB, 28,573 items). `sleutel` (3, none relevant: a physical door-key
dispute 1585, a "Sleutel geheimschrift" for **Ottoman/Constantinople** governments and ministers, invnr 12578.1,
unrelated correspondent/period), `cijferschrift` (5, all dated 1629-1674, outside 1600-1610), `chiffre` (0).

**"Liassen Agent Brederode"** (invnr range 6016-6024, series description "Ingekomen brieven en stukken van
Pieter van Brederode, Agent van de Staten-Generaal in Duitsland en Zwitsersland, 1602-1637") is a dedicated,
year-bundled series of this exact correspondent's papers held at the States-General archive, not the
Oldenbarnevelt archive. Invnr **6016** covers **1602-1613** and is digitised, public domain (METS
`https://service.archief.nl/gaf/api/mets/v1/4153f78f-3369-4801-93bc-c3eb9b39012c`, 624 page images). Fetched 6
sample images (order 1, 100, 180, 260, 261, 262; method and URLs in `images/manifest.json`'s
`na_101_02_6016_note`) to characterise it:
- Order 1: folder-cover leaf handwritten "1602 en 1603" -- confirms the bundle is loose, year-divided, **not
  letter-indexed**.
- Order 260: folder-cover leaf handwritten **"1605-1606"** -- the exact year-folder for our target.
- Order 261 (the very next leaf): Brederode reporting his journey "nae Heydelbergh" and dealings with "Marquis
  Joachim Ernest van Brandenburg" -- on-topic for the same mission as our target letter (written from
  Heidelberg, 21 Feb 1605), though not visibly in cipher on this one leaf.
- Order 100/180 land in a different bound sub-document (a negotiation register/journal with its own archival
  page numbers, an index-tab margin visible at order 100) bound into the same digitised file -- the 624 pages
  are not one uniform letter-bundle.
- **No numeral cipher seen on any of the 6 sampled leaves.** This is far too small a sample to call a negative:
  the 1605-1606 folder's extent (order 261 to the next divider) was not located, and no page-by-page read was
  done (out of this job's scope/budget -- no subagents, $5 stall cap).
- A separate item, not checked for digitisation this pass: "Stukken betreffende de zending... van doctor Pieter
  Brederode naar de Zwitserse kantons, 1605. Met retroacta, 1587-1604" (a 1605 Swiss mission dossier, distinct
  from the German/Heidelberg mission our target concerns).

**This is the strongest open lead from this pass.** A future capture worker should read NL-HaNA 1.01.02 inv.
6016 image order ~261 through the next year-divider leaf, watching for (a) any duplicate/copy of the 21 Feb 1605
letter itself, (b) any nearby passage in the same numeral-code system with an interlinear gloss or an attached
key note (the archive is known to sometimes catalogue cipher items "met het cijfer", i.e. with the key attached
-- see the statengeneraal search below).

### 3. NA 3.20.07 (Van Brederode family archive) -- checked in full, negative

Found via web search (not previously in this repo): toegang 3.20.07, "Inventaris van het archief van de familie
Van Brederode", (1248)-1697, only 112 items -- small enough to fetch and grep whole. Zero `sleutel`/`cijfer`/
`chiffre` hits. One `Oldenbarnevelt` hit: invnr 28, letters of 20 Jan and 9 March 1616 to **Walraven IV** van
Brederode (a different branch/generation than our Pieter Corneliszn.), irrelevant to this target. Per the search
snippet, part of the wider Brederode family archive is held at the Fürstliches Haus- und Landesarchiv Detmold
(Germany) -- out of scope for the Nationaal Archief, not checked this pass.

### 4. Huygens retroboeken/statengeneraal (Resolutiën der Staten-Generaal 1576-1630), Deel 13 OR (1604-1606, GS 101)

Confirmed the accessor mechanics for this book (`searchText`, `search_term:ustring:utf-8=<term>&source_id=13OR`,
per the method `sources/huygens/NOTES.md` round 2 documented for the sibling books) and ran three searches
against the volume covering our exact date range:
- `Brederode`: 39 hits. The most relevant, p.101 (`page_index=113`, full OCR page read, not just the snippet):
  "Oldenbarnevelt deelde 21 Februari een brief van Brederode mede van ongeveer dezelfde inhoud; er werd nog
  uitgesteld er een besluit over te nemen" -- the States-General's own resolution records that Oldenbarnevelt
  personally communicated a letter from Brederode to the assembly on **21 February 1605**, on a matter the
  surrounding text says could not be put "in brieven of geschriften" (in letters or writings) -- i.e. sensitive
  enough to need oral/secure handling, consistent with (though not proof of) the letter's partial cipher. No
  archival citation is given for this specific incoming letter (Oldenbarnevelt reported it in person, so the
  resolution's own footnotes cite only the *replies*, e.g. footnote "10) De brief aan Brederode: R.A., S.G. 5888
  (minuut)" on p.96, and "Beide brieven: R.A., S.G. 5968" for the 1-2 March replies). This is strong
  corroboration that our target letter (or one essentially like it, same date) reached The Hague and was acted
  on, but it is not a key or a decipherment.
- `sleutel`: 1 hit, p.630, a literal door/lock key ("de sleutel van de plaats waar de..."), irrelevant.
- `cijfer`: 1 hit, p.649, "R.A., S.G. 7106 (orig., met het cijfer); beide gedrukt" -- about a **different**
  correspondent ("De Castries"), but establishes that this same archive's resolution editors do sometimes note
  when an item is filed "met het cijfer" (with its cipher key attached); no such note anywhere near the
  Brederode hits in this volume.

### 5. De Leeuw et al., "Keys with nomenclatures in the early modern Europe" -- access gap, not a paywall

Identified via OpenAlex (keyed): Megyesi, Tudor, Láng, Lehofer, Kopal, de Leeuw, Waldispühl, *Cryptologia*,
published **2022** (not 2024 as my job brief said -- DOI `10.1080/01611194.2022.2113185`), and it **is** open
access (OpenAlex `is_oa: true`, hybrid), with two repository mirrors: `uu.diva-portal.org` and `edit.elte.hu`.
Abstract read via OpenAlex's inverted index: a general survey of 1,600+ historical cipher keys from 10
countries, no country or correspondent named in the abstract. Full text **not read this pass**: the DiVA mirror
reset the connection twice (`curl: (35) Recv failure`, one retry per the good-citizen rule), the ELTE mirror
404'd on both URL forms OpenAlex gave, and the DOI resolver itself is Cloudflare-challenged from this
environment. This is a transient/environment access problem, not a subscription block -- worth a plain retry
from a fresh session or a LOCAL-QUEUE.tsv row for a home-IP fetch of
`https://uu.diva-portal.org/smash/get/diva2:1718372/FULLTEXT01`, not a JSTOR row (the paper is not on JSTOR).

### 6. Den Tex, *Johan van Oldenbarnevelt* (dbnl.org) -- retried once, now reachable, read in full, negative

The host TLS-failed twice in an earlier pass; per the job brief, retried once more this pass and it worked
(`dbnl.org/tekst/tex_003joha01_01/`, 200). This is the Jan den Tex **and Ali Ton** one-volume abridged edition
(not the original 5-volume unabridged biography), downloadable whole as
`tex_003joha01_01/tex_003joha01_01.pdf` (307 pages, fetched once, 1.5s+ between the two dbnl.org requests).
Extracted full text (`pdftotext`, installed this pass) and grepped: `Brederode` (6 hits, all "Pieter Corneliszn.
Brederode", confirms he is Oldenbarnevelt's calvinist agent in Germany and discusses the April 1605 Brandenburg/
Palatinate subsidy negotiations that our target letter's mission concerns) but **zero** hits for `sleutel`,
`cijferschrift` or `chiffre` anywhere in the volume. Genuine negative for this specific (abridged) edition; the
original unabridged Den Tex biography is a different, longer text not confirmed reachable the same way.

### Hosts/requests this section

`nationaalarchief.nl`: ~8 (3.01.14 page + XML, 1.01.02 page + XML, 3.20.07 page + XML, site search page).
`service.archief.nl`: ~8 (1 METS fetch, 6 image fetches, all >=1.5s apart). `resources.huygens.knaw.nl`: ~10
(retroboeken index, statengeneraal TOC x2, 3 searches, pages.json, 1 real page). `api.openalex.org`: 1 (keyed).
`uu.diva-portal.org`: 2 (both failed, connection reset, one retry per good-citizen rule, not retried further).
`edit.elte.hu`: 2 (both 404). `doi.org`: 1 (403, Cloudflare). `dbnl.org`: 2 (index page, PDF; both 200 this
pass). No logins, no credentials used.

## Search log (rule 1, dated 25 Sept 2026)

1. Web search (multiple queries: "Brederode Oldenbarnevelt cijfer 1605 sleutel ontcijferd"; "'van Brederode'
   Oldenbarnevelt cipher 1605 Heidelberg decoded"; "Bescheiden betreffende het beleid van Van Oldenbarnevelt
   deel 2 no. 92 Brederode cipher solved"; "cipherbrain.de OR 'Klaus Schmeh' Oldenbarnevelt cipher
   Netherlands 1605") -- no hit describing this letter or a solution; hits are all incidental (Wikipedia
   pages on the Brederode/Oldenbarnevelt families, archive finding aids).
2. Sender's printed correspondence: none separate from this edition exists for P. van Brederode as far as
   this search reached; the edition itself is the printed source.
3. Calendars/state-paper series: not applicable (Dutch domestic archive, not an English/foreign calendar).
4. List-post comment threads: Cryptiana (web search, no match) and Cipherbrain (web search including the
   "Top 50 unsolved encrypted messages" list, no match).
5. DECODE (de-crypt.org): `site:de-crypt.org Brederode OR Oldenbarnevelt` web search, no relevant hit (only
   the terms-of-use page).
6. Solver repositories: `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers` shallow-cloned and grepped
   case-insensitively for `brederode` and `oldenbarnevelt` -- 4 incidental matches (word-frequency corpora,
   an unrelated 1646 royalist key), none about this item.

## Requests

`resources.huygens.knaw.nl`: ~20 (landing page, book_data.js, toc form, full letter-list accessor for deel 2,
4 search-term queries across all 3 volumes, 6 page-html fetches, 6 page-image fetches, 1 search-form fetch),
all >=2s apart, descriptive User-Agent. `resources.huygens.knaw.nl/wvo`: 1. `github.com`: 2 shallow clones
(reused for grep, not committed). `dbnl.org`: 2 (both failed, TLS `SSL_ERROR_SYSCALL`, one retry per the
good-citizen rule, not retried further). No logins, no blocks other than dbnl.org.

## YX-OBR (25 Sept 2026)

Job: `.claude/briefs/runs/2026-09-25-lane-yx-obr.md`, two copy-free routes on the two open leads TX-KEYS left
(archival-citation trace; NA 1.01.02 inv. 6016 leaf walk). **Both routes are negative: no key, no clear copy,
no cipher passage found.** Per the brief, since neither route yielded a key or a clear copy, no transcription
or decode was attempted this pass.

### Route A: tracing "A.R.A., Holland 2613, e. Duplicata" / "Holland 2589, b 4" to a modern toegang

The brief's own hypothesis was NA toegang 3.01.04.01 (Staten van Holland en West-Friesland, 1572-1795).
Confirmed the toegang's title matches via its landing page. Fetched the whole EAD XML (2.97 MB,
`nationaalarchief.nl/onderzoeken/archief/3.01.04.01/download/xml`) and grepped for exact `<unitid>` values
`2613`/`2589` (allowing an optional trailing letter, e.g. `2613e`): **zero matches**. The only raw-string hits
for "2613"/"2589" anywhere in the 2.97 MB file are accidental substrings inside unrelated `hdl.handle.net`
UUIDs, not archival numbers -- confirmed by inspecting each hit's context.

The toegang's own processing notes ("Gebruikte nummering") state the pre-1880 numbering was largely retained,
and it carries a concordance appendix ("Concordantie van de oude nummering naar de nummering in deze
omgeknipte en bijgewerkte inventaris") whose abbreviation legend defines `D.H.` = "dubbelen Holland" (Holland
duplicates) -- a striking match to the RGP citation's "Holland 2613 ... Duplicata" wording. But the
concordance table itself (1,170 rows, parsed in full) contains **no `D.H.`-prefixed row at all**: the
abbreviation is defined in the shared legend but never used in this toegang's actual old-to-new mapping,
meaning the "dubbelen Holland" series is not held (or not separately concorded) under 3.01.04.01.

Cross-checked NA 1.01.02 (Staten-Generaal, the toegang TX-KEYS already explored for other reasons) as a
sanity check on the "old number = modern unitid" assumption: this toegang's own EAD *does* contain unitid
`2613` and `2589` verbatim -- but both are 12-volume bound registers dated **1754-1756** respectively
(confirmed by reading each `<unitdate>` in context), over a century after our 1605 letter. Coincidental
modern renumbering, not a match.

**Conclusion (negative, route A, S-grade search result):** the archival citation "Holland 2613"/"Holland
2589" in Veenendaal's edition does not resolve to either of the two most plausible modern toegangen
(3.01.04.01 Staten van Holland, 1.01.02 Staten-Generaal) by direct number lookup in their EAD finding aids.
It most likely refers to a pre-reorganisation numbering scheme (an old "dubbelen Holland"/Loketkas series)
renumbered or merged into a toegang not identified this pass. NA's own catalogue search
(`nationaalarchief.nl/onderzoeken?q=...`) is client-side rendered (Angular/React shell, no server-rendered
results reachable by curl, confirmed by fetching the search page and finding no results markup, only the
query string echoed back in a JS blob) -- a real-browser search for "dubbelen Holland" was not tried this
pass (out of route A's stated method, which was "confirm from the finding aid... not by assumption", already
done). A single web-search attempt via `google.com/search` returned an unparseable bot-challenge page (heavily
obfuscated JS, no plain results) and was not retried, per the good-citizen rule and because Google search is
not a documented route in CLAUDE.md's Access playbook.

### Route B: walking NA 1.01.02 inv. 6016 from image order 261

Built the full image-order -> file-UUID map from the bundle's METS XML (`service.archief.nl/gaf/api/mets/v1/
4153f78f-3369-4801-93bc-c3eb9b39012c`, 624 entries, saved to scratch as `order_map.json`; the IIIF image base
path is constant for the whole object, `41/53/f7/8f/33/69/48/01/93/bc/c3/eb/9b/39/01/2c/<uuid>.jp2`, so any
page can be fetched directly at `.../full/<width>,/0/default.jpg` without re-parsing the METS per leaf).

Read every one of the 91 leaves from image order 260 (the "1605-1606" folder-cover leaf TX-KEYS already
found) through order 350 -- which turned out to BE the next year-divider leaf, handwritten "1607 - 1608",
immediately after a blank verso at order 349. **The whole "1605-1606" folder has now been read leaf by leaf;
full per-leaf log in `obr_6016_leaflog.tsv` beside this file (order, date read if legible, cipher/key/
interlinear yes-no, one-line note).**

**No numeral-code cipher, no key/nomenclator table, and no interlinear decipherment found on any of the 91
leaves.** Every leaf is plain running prose -- Dutch, French, German or Latin -- covering diplomatic
correspondence, financial/exchange-rate accounts, legal memoranda and political lists (an addressee list of
princes and free cities for circular letters sent via Brederode, dated end of Jan 1605; a two-column list of
Imperial/Protestant territories and cities, dated Oct 1604; a Latin legal-argument outline). Several leaves
carry explicit multi-digit numbers, but always in an unambiguous plain context -- money sums in guilders/
florins/thalers, distances in miles, exchange rates, dates written in contracted form (e.g. "616" for 1616)
-- never a standalone code group substituting for a name or word the way no. 92's ~121 tokens do. Two leaves
that looked cipher-like at a glance on closer inspection were not: order 291 (mirror-image ink bleed-through
from the facing leaf, itself a plain French financial ledger) and order 321 (a two-column place-name list
with no numerals at all, examined at 2400px to rule out).

The folder contains **several other letters signed by Pieter van Brederode himself**, none in cipher: 24 Oct
1604; 16 Mar 1605 from Heidelberg (order 274 -- a different Heidelberg letter than our 21 Feb 1605 target);
10 May 1605; ~12 Apr 1605 from Frankfurt (order 289); ~26 Jul 1605 from Frankfurt (order 286); 7 Jul 1605
from Schaffhausen; Sept 1605 from Frankfurt; 20 Nov and 29 Nov 1605 from Hanau; 23 Jul 1606. A letter from
Elector Palatine Frederick IV himself also appears (order 338, dated ~21 April 1605). None of this
correspondence is enciphered -- consistent with Veenendaal's own statement (already on file) that no. 92 is
the volume's only ciphered item, now extended to: this entire adjoining year-folder of the agent's own
incoming-papers series carries no cipher either. No duplicate or copy of the specific 21 Feb 1605 letter was
spotted (order 261's on-topic Heidelberg/Brandenburg leaf, already flagged by TX-KEYS, remains the closest
thing to it and is not itself the letter).

**This closes the route B lead as stated in the brief.** A successor could walk the bundle's other
year-folders (order 1-259 for 1602-1604, order 350-624 for 1607-1613) if a duplicate is still wanted, but
that is a new, unbudgeted search, not a continuation of this job.

### Method (subagent use)

Fetched the coarse skeleton (every ~20th leaf, then gap-filled at 5-10 leaf granularity, then leaf-by-leaf
around the transition) personally; one Sonnet subagent (per the brief's "a subagent may look at batches of
images" allowance, 1 of the 2 permitted) filled the remaining 62 unchecked orders in the same range with the
same fetch method and log schema, so the combined `obr_6016_leaflog.tsv` covers all 91 leaves with no gaps
(verified programmatically). The subagent worked from the scratchpad only, touched no repository file, and
reported back inline; its findings are merged into the log and narrative above, not taken on faith --
cross-checked its yes/no cipher flags against its own per-leaf notes, all consistent with "no".

### Hosts/requests this section

`service.archief.nl`: ~106 (1 METS fetch, ~41 image fetches by this worker directly including 2 higher-res
re-fetches for closer inspection, ~64 image fetches by the one subagent including 2 higher-res re-fetches),
all >=1.5-1.8s apart, well under the brief's 150 cap, descriptive User-Agent. `www.nationaalarchief.nl`: 5
(toegang 3.01.04.01 landing page, its EAD XML, toegang 1.01.02 landing page, its EAD XML, one client-rendered
search page that returned no usable results), well under the brief's 30 cap. `google.com`: 1 (bot-challenge
page, not retried, not a documented route). No logins, no credentials, no blocks/429s encountered.

## Local runner L12 recheck (26 Sept 2026)

LOCAL-QUEUE.tsv row L12 (item 5 above's access gap), answered by the owner's desk runner, PR 27
(LOCAL-RUNNER-RECHECK-2026-09-26.md, landed by PR-LAND-7): the exact Uppsala DiVA mirror PDF
(`uu.diva-portal.org/smash/get/diva2:1718372/FULLTEXT01`) downloaded cleanly from a non-cloud IP, HTTP 200,
application/pdf, 7,750,993 bytes, 44 pages (Megyesi, Tudor, Láng, Lehofer, Kopal, de Leeuw, Waldispühl,
"Keys with nomenclatures in the early modern Europe", Cryptologia 48(2), 2024, DOI
10.1080/01611194.2022.2113185; article pp.97-139, PDF pagination differs -- citations below use the PDF's
own printed page numbers). PDF SHA-256 `5773415c2feacb746fafd524d904adcbe378f753ddc863712f3d177da803e27c`.

All 44 pages text-extracted; case-insensitive search for `Dutch`, `Oldenbarnevelt`, `Brederode`,
`States-General`, `States General`, `1600`, `1605`, `1610`, plus stems `Oldenbarnevel\w*`, `Brederod\w*`,
`Staten`, `Holland` and the 1600-1610 date range: **no hits anywhere in the paper**. "Netherlands" occurs
only in sample/archive descriptions, an affiliation and references. Three passages checked by eye against
the extracted text: article p.8/PDF p.9 (Sec.4, "Sample of keys": 1,610 keys registered in DECODE by 14 June
2021, images/metadata in DECODE, not itemised in the paper); article p.33/PDF p.34 (Sec.8.3, "Regional
tendencies": the Netherlands is one of the groups excluded from that regional analysis for having "less than
10 keys each" -- a statement about that analysis, not a total-sample count); article pp.40-41/PDF pp.41-42
(Appendix, "List of Archives": the Dutch institutions listed are Koninklijk Huisarchief, Museum voor
Communicatie and Nationaal Archief, The Hague -- institutions, not individual shelfmarks/correspondents/
dates).

**Bounded S-grade negative: no individually identified Dutch/Netherlands/Oldenbarnevelt/Brederode/
States-General key dated 1600-1610 is named in this paper's text, tables or appendix.** This closes the
paper itself as a lead (item 5 above, "access gap" resolved). It does not rule out an individual record
surviving only in DECODE's own database (the paper cites DECODE as the primary source, not itself), which
this recheck did not exhaustively search -- a DECODE search by date range/country remains open, per DECODE's
listing-only access (CLAUDE.md Access playbook).

LOCAL-QUEUE.tsv row L12: `done 26 Sept 2026`. Status stays `open`: no key or sibling found for this letter
by any route tried to date.

## Web and blog check (WEBCHECK-oldenbarnevelt-brederode-1605, 1 Oct 2026)

The open-web and blog comment-thread step required by `.claude/briefs/check-solved.md` (CHECK-SOLVED-WEB, 28 Sept
2026), run 1 Oct 2026 23:35-23:50 UTC by WEBCHECK-oldenbarnevelt-brederode-1605 (account-4, brief
`.claude/briefs/runs/2026-10-01-account4-webcheck.md`). Every query and every hit opened is listed; "no hit" means the
query returned nothing about this letter, a search result, never a novelty verdict (CLAUDE.md rule 10).

**Result: no decipherment or plaintext of this item located by these queries on 1 Oct 2026.** Status word stays `open`.

### (a) Plain web searches (search engine, 10 queries)

| # | Query | Result for THIS letter |
|---|---|---|
| 1 | `Brederode Oldenbarnevelt 1605 Heidelberg cijferschrift cipher letter` (sender + recipient + date) | no hit: Wikipedia pages on Reinoud van Brederode (a different Brederode, Oldenbarnevelt's son-in-law), NA toegangen 3.01.14 and 3.20.41, zandvoortvroeger.nl "Verzoekschrift aan de Heer van Brederode. Anno 1605" (a Zandvoort petition, unrelated) |
| 2 | `"Holland 2613" OR "Bescheiden betreffende het beleid van Johan van Oldenbarnevelt" cijferschrift sleutel no. 92 1605` (shelfmark + edition title + cijferschrift) | no hit: Huygens edition landing pages, den Tex on DBNL (already read in full, section 6 above), NA 3.01.14 -- nothing names no. 92 or a key |
| 3 | `"Uyt Heydelberg, desen 21en february 1605" OR "van den 671 van den 611 ende 612"` (distinctive clear-text phrase + first code run, both quoted) | no hit for either phrase; results are Wikipedia 1605/Heidelberg pages and US route numbers |
| 4 | `"Brederode aan Oldenbarnevelt" 21 februari 1605 cipher nomenclator unsolved` (folder's descriptive title) | no hit: generic unsolved-cipher lists, Bourdeau's cyphersolver index (opened, below), Wikipedia Brederode genealogy; nothing on this letter |
| 5 | `Veenendaal "Oldenbarnevelt" Brederode 1605 cijferschrift "sleutel" ontcijferd OR opgelost OR gedecodeerd` (Dutch, editor's name, "solved" vocabulary) | no hit: NA inventories, genealogy pages, Gemeentearchief Veenendaal (the town, not the editor) |
| 6 | `cryptiana Tomokiyo Oldenbarnevelt OR Brederode Dutch cipher Staten-Generaal 1605 nomenclator` | no hit for this letter: Cipherbrain nomenclator overview post (opened, below), Bourdeau issues #11 and #13 (other targets), de Leeuw et al. 2024 (read in full by L12 above, negative) |
| 7 | `Oldenbarnevelt Brederode cipher 1605 solves Claude OR GPT OR ChatGPT decipherment` (model-solve announcements, check-solved.md) | no hit for this letter: the only "solves" hits are Schneier on Security (Sept 2026) and vals.ai on Claude Fable 5.1 reading Urquhart's "Cyphral Distich" (c.1653, Scottish, a different item); Schneier thread opened, below |
| 8 | site search `scienceblogs.de` (Cipherbrain): `Oldenbarnevelt OR Brederode cipher 1605` | no hit for this letter; the engine returned Cipherbrain's general 16th-17th-century posts (Ferdinand III letters, Biermann/Louvois 1690, Thirty Years' War 1644, Spinelli 2017) -- the plausible ones opened, below |
| 9 | site search `cryptiana.blogspot.com` + `cryptiana.web.fc2.com`: `Oldenbarnevelt OR Brederode cipher Dutch 1605` | no links returned at all |
| 10 | site search `ciphermysteries.com`: `Oldenbarnevelt OR Brederode cipher Dutch 1605` | no hit for this letter; the engine returned van Heeck, Voynich, La Buse, Bellaso pages, none Dutch 1605 |

### (b) The three blogs' own search engines (each blog's native search, both names)

| Blog | URL | Result |
|---|---|---|
| Cipherbrain | `scienceblogs.de/klausis-krypto-kolumne/?s=Oldenbarnevelt` | "Wir konnten leider keine Beiträge finden" -- 0 posts |
| Cipherbrain | `scienceblogs.de/klausis-krypto-kolumne/?s=Brederode` | 0 posts |
| Cipher Mysteries | `ciphermysteries.com/?s=Oldenbarnevelt` | "Nothing Found" -- 0 posts |
| Cipher Mysteries | `ciphermysteries.com/?s=Brederode` | 0 posts |
| Cryptiana blog | `cryptiana.blogspot.com/search?q=Oldenbarnevelt` | "No posts matching the query" -- 0 posts |
| Cryptiana blog | `cryptiana.blogspot.com/search?q=Brederode` | 0 posts |
| Tomokiyo's cryptiana.web.fc2.com pages | on-disk snapshot `sources/cryptiana/` grepped case-insensitively for `oldenbarnevelt` and `brederode` (0 requests) | 0 files match |

### (c) Hits opened and comment threads read

| URL | What it is | What it says about THIS letter |
|---|---|---|
| scienceblogs.de/klausis-krypto-kolumne/norbert-biermann-solves-encrypted-letters-from-the-17th-century/ | Louvois to Lauzun, May-June 1690, nomenclator, solved by Biermann | nothing; no comments rendered |
| scienceblogs.de/.../2018/10/15/unsolved-cryptograms-from-the-thirty-years-war-1/ | Vienna Hofarchiv letters 1644 (Pentz, Christian IV, Tattenbach), 21 comments, Thomas Ernst solves II-V | nothing on Oldenbarnevelt, Brederode, Heidelberg 1605 or the States General |
| scienceblogs.de/.../2016/08/13/nomenclator-encryptions-centuries-old-but-still-hard-to-solve/ | nomenclator overview (Perwich, Manchester, Catinat, a 19th-c. Van Gelder Dutch nomenclator), 4 comments | nothing on this letter; the only Dutch item is early 19th century |
| scienceblogs.de/.../2017/03/24/who-can-solve-this-encrypted-text-from-the-16th-century/ | the Spinelli (Beinecke) letter whose thread produced the N0 that created this rule, 17 comments | nothing on this letter |
| schneier.com/blog/archives/2026/09/claude-fable-solves-a-historical-cipher.html | Claude Fable 5.1 reading Urquhart's Cyphral Distich (c.1652-56), 13 comments on Glasgow/NLS copies | nothing on Oldenbarnevelt, Brederode, 1605 or Veenendaal |
| dbourdeau.github.io/cyphersolver/index.html | Bourdeau's working-notes index (Latest, By outcome, Solved 1429-1644, Read 1691, Recent findings Sept 2026) | no line names Oldenbarnevelt, Brederode, Heidelberg 1605 or Veenendaal (the repository itself was grepped 25 Sept 2026, Key route section above) |

Not opened: Wikipedia genealogy pages, NA inventories (3.01.14 and 1.01.02 already read as full EAD XML in the Key hunt
section above), zandvoortvroeger.nl (a 1605 petition to the lord of Brederode at Zandvoort, a different Brederode and a
different document class), vals.ai (duplicate of the Schneier item).

### Requests per host

Search engine: 10 queries. `scienceblogs.de`: 6 page fetches. `ciphermysteries.com`: 2. `cryptiana.blogspot.com`: 2.
`schneier.com`: 1. `dbourdeau.github.io`: 1. `cryptiana.web.fc2.com`: 0 (snapshot grepped). One request at a time, no
403/429/challenge page met, no login.

### Intake gate re-run

```
$ python3 tools/intake_gate_check.py oldenbarnevelt-brederode-1605
oldenbarnevelt-brederode-1605: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit=0
```

## OLD-DKEY (2 Oct 2026, account-4)

Brief `.claude/briefs/runs/2026-10-01-account4-old-dkey.md`, answering the open point left by the L12 recheck above
("does not rule out an individual record in DECODE"). Searched DECODE's full key-record listing (record type Key,
every status) for a key dated 1595-1615 with a Dutch origin or holder. Source: the on-disk listing snapshot
`sources/decode/keys-all-2026-09-28-merged.tsv` (28 Sept 2026, 6,324 rows, H18 of espagnol142-mercy-1648) plus the
one page that snapshot lacked, N/A page 58, fetched this session into `sources/decode/keys-na-p58-2026-10-02.tsv`
(50 rows, all Florence ASF, none Dutch or in window) -- together all 6,374 key records DECODE lists on 2 Oct 2026
(N/A 6,351 + Decrypted 19 + Non-decrypted 4; the N/A total today equals the 28 Sept total, so nothing was added in
between). Login-free listing only (`tools/decode_list.py`), no login attempted, 5 requests to
`de-crypt.org/decrypt-web/RecordsList` at 1.6 s (one dry run that fetched nothing because `--max-pages` counts from
page 1, one run aborted by a `--raw-dir` path bug on the status name `n/a`, one clean run). Output
`decode_keys_1600s.tsv` (26 rows, classes in its header line).

**Candidates dated 1595-1615 with a Dutch holder or Dutch language: 0.** DECODE holds 69 key records from The Hague
(Nationaal Archief 1.10.29 Familie Fagel inv. 5345 x 61 dated 1680-1758 plus 11 undated, NA 1.01.02 Staten-Generaal
inv. 6894 x 1, NA legatie Rusland x 2, Koninklijk Huisarchief x 4, Museum voor Communicatie x 1) and 11 Dutch-language
keys, and not one is dated inside 1595-1615. The free-text holder search (Brederode, Oldenbarnevelt, Staten, Holland,
Prague, Kaiser, Emperor, Nassau, Orange, States) hits only record 2118 and the Vienna "Kaiser Franz" Handarchiv keys
of 1765-1792. What the TSV lists instead:

- **2118, the only States-General key** (`dutch-near-window`): NA 1.01.02 Staten-Generaal inv. 6894, listing date
  "1620 -", Dutch, 2 pages, status N/A. Fifteen years after the letter and in the wrong archive series (inv. 6894 is
  not the 1.01.02 6016 "Duitsland" bundle walked by YX-OBR), but it is the one DECODE key of the States General's own
  chancery from the first quarter of the century, and a two-digit/three-digit numeral nomenclator of the 1620s could
  descend from the one in use in 1605 (range 30-741 here). Its images are account-gated at full size (ASKS row 1).
- **2842-2852, 11 undated Fagel keys** (`dutch-undated`): the same inv. 5345 run whose dated siblings are 1680-1758;
  almost certainly the griffier Fagel's own 17th-18th-century keys, not candidates, listed only because the listing
  gives them no date.
- **938-953, 14 Brussels ARA Secretairerie d'Etat Allemande inv. nr. 1 keys** (`brussels-series-spans-window`): a
  Habsburg-Netherlands series whose stated range 1553-1729 spans the window; German/Spanish/Latin, the enemy
  chancery's keys (H18 of espagnol142-mercy-1648 already read 941, 944, 946 on their RecordsView pages: Spanish
  homophonic designs). Not a key Brederode would have used; listed so the next worker does not re-screen them.

Not listed (not Dutch, out of this brief's scope, counted for the record): in-window keys from the sender's own
German milieu exist in bulk -- Munich BayHStA 102, Marburg HStAM (Hessen-Kassel) 20 -- and Vienna HHStA 263,
Florence 811, Stockholm 75, Kew 26, Madrid 20, Paris 19. A Palatine or Hessian key would be a correspondent-side
key, not the States' key the editor could not find; nobody has screened those 122 records for a numeral
nomenclator in the 30-741 range.

Status stays `open`. **Rule 10 wording:** a search result over 100% of DECODE's key listing by date, holder, language
and holder text on 2 Oct 2026; not a key verdict and not evidence that no such key exists outside DECODE (the NA
1.01.02 and 3.01.14 EAD hunts in "Key hunt" above are the other half of route A).

**Named next step (one LOCAL-QUEUE.tsv row, drafted here, not filed):**

```
L<next>	browser-check	ciphers/oldenbarnevelt-brederode-1605	OLD-DKEY (2 Oct 2026): DECODE record 2118 (https://de-crypt.org/decrypt-web/RecordsView/2118, Nationaal Archief 1.01.02 Staten-Generaal inv. 6894, key, "1620 -", Dutch, 2 pages) is the only States-General key DECODE lists before 1650; its full-size images are account-blocked for the cloud (ASKS row 1). In the owner's logged-in DECODE browser open the record and its 2 images and paste into ciphers/oldenbarnevelt-brederode-1605/decode_2118/ : (1) the record's own description fields (date, description, "key design", inventory text) as plain text; (2) the two images at full size as 2118_p1.jpg, 2118_p2.jpg; (3) one line saying whether the key maps words/names to Arabic numerals in roughly 30-741 (the letter's range, NOTES.md "What is established") or to something else. No decoding, no other records.	queued	
```

## Premise check (GF4-BATCH4, 3 Oct 2026)

**Verdict: nothing found that reads, glosses or clear-copies this letter; the item stays `open`.** Adversarial pass (try to prove it is already done), run 3 Oct 2026 by a GF4-BATCH4 subagent. No test, decode or reading was run. "Not found" is a search result, not a novelty verdict (rule 10).

- **(a) Folder mentions: found only non-decipherments.** Opened: NOTES.md in full; `ciphertext.txt` and `images/p111.jpg` at full size (the printed page: footnote 1 only identifies "Schouwenberch" as "Mogelijk graaf Joost van Schauenburg", Ten Raa/De Bas; footnote 2 is about Louise Juliana; no gloss, no interlinear, no clear copy; citation "A.R.A., Holland 2613, e. Duplicata." = an archive copy marker, not a decipherment); `obr_6016_leaflog.tsv` (94 leaf rows, column cipher_numerals = `no` on every row, key_table and interlinear likewise `no`); `decode_keys_1600s.tsv` and `local-runner/L12-2026-09-25.md` (L12 is an access-failure record, superseded by the 26 Sept full-paper read). The editor's "ontcijfering" (p.XIII) is the palaeography sentence; his cipher sentence says the key was not found (voorwerk_XIII.jpg, already on file).
- **(b) Other solvers' working files: not found.** Shallow clones 3 Oct 2026: dbourdeau/cyphersolver @ 2341682, aaymeloglu/unsolved-ciphers @ d2800bb; `grep -rIil` for oldenbarnevelt, brederode, veenendaal, `3\.01\.14`, "inv.* 6016", heydelberg: only `d/targets/{cobham1588,perwich,matignon1586}` word-frequency corpora and `a/royalist-1646/{key129.txt,README.md}` (the 1646 royalist key naming "the Brederodes"). Opened none as a key for this text: wrong country, date and numeral scheme; the royalist key has not been run on this letter by anyone (no output in the repo). Clones deleted.
- **(c) Neighbours: not found.** Huygens edition pages (html_url pattern, 2.2 s apart) read in full: pp.112-114 (no. 93 Louise Juliana 22 Feb/4 Mar 1605, French, plain; nos. 94-101, Plessen/Rheydt letters of March-April 1605 on the Palatine-Brandenburg treaty, plain French, footnotes cite the treaty, no restatement of no. 92's coded names); pp.108-109 (no. 91, plain). Other Brederode letters of 1604-1605 in this edition (search `Brederode`, Deel 2: 70 hits; nos. 78, 81 and p.89/p.98 letters, A.R.A. St. Gen. 5888) are plain: no 3-digit code runs on pp.87, 89, 91, 98. Interior-phrase searches across all three volumes: `Schouwenberch` 1 hit (p.111 itself), `puyck` 2 hits (p.111, and an unrelated Deel 3 p.401), `ontcijfer` 0. `ciphers/na-oldenbarnevelt-2442-1605/NOTES.md` read only: it mentions no. 92 only as an unrelated "side finding" (lines 104-115, 138); no shared key, no reading. Archive neighbours: the 91-leaf inv. 6016 "1605-1606" folder was already walked leaf by leaf (YX-OBR; `obr_6016_leaflog.tsv`), no cipher, key or clear copy; the leaves outside that folder (orders 1-259, 350-624) remain unwalked.
- **(d) Recipient/States side: not found.** Huygens retroboeken/statengeneraal (Resolutiën, Deel 13 OR 1604-1606): `Schauenburg` (6 hits, pp.106, 113, 129, 639: German count's levy/justice matters, not Brederode's letter), `Schouwenberch` (2 hits, Deel 1 1576-77, wrong era), `puyck` (2 hits, Deel 7 index), `Brederode 1605 Heidelberg` 0 hits. The earlier TX-KEYS finding (Resolutiën p.101: Oldenbarnevelt communicated a Brederode letter on 21 Feb 1605) is the only States-side trace and contains no clear text of the letter. Foreign calendars: not applicable (Dutch domestic). Not reachable/not tried: Ritter, *Briefe und Acten* I (Rheydt report, p.466) and the Detmold Brederode family archive.

**Result: not found-solved -- stays open.**

Requests this section: resources.huygens.knaw.nl 15 (9 page fetches, 6 searches, all >= 2.2 s, descriptive UA, no 403/429); github.com 2 shallow clones. No logins.

Next cheap test: file the drafted OLD-DKEY LOCAL-QUEUE row (above): the owner's DECODE browser copy of record 2118 (NA 1.01.02 inv. 6894, States-General key, "1620 -") and one line saying whether it maps names to Arabic numerals in the 30-741 range.

## While waiting (RUN4-WAITBF, 4 Oct 2026)

- [done 6 Oct 2026, R8-OBRED2: 122 records screened, none shown to fit, 89 numeral-tagged left unread at full size; see the section at the end] Action that depended on nobody (6 Oct 2026, R8-OBRED): screen the in-window Palatine/Hessian DECODE keys (Munich BayHStA 102, Marburg HStAM 20) from their public RecordsView pages for a numeral nomenclator reaching the 700s; ~2-3 (estimate).
- [done 6 Oct 2026, R8-OBRED: record 2118 is a 1620 Levant key for Cornelis Haga, codes 1-116, does not fit; see the section below] Action that depended on nobody: open DECODE record 2118 (NA 1.01.02 inv. 6894, States-General key, "1620 -") ourselves -- RecordsView pages are public (N6-HEL81, 4 Oct 2026) and a full-size image has been served after one browser login (A2-HDK, 2 Oct 2026) -- and say whether it maps names to Arabic numerals in the 30-741 range; image to scratch, never committed; ~$1 (estimate). This replaces waiting on the drafted OLD-DKEY LOCAL-QUEUE row unless the image is refused.

## DECODE record 2118 opened (R8-OBRED, 6 Oct 2026, 03:37-03:39 UTC)

Brief `.claude/briefs/runs/2026-10-06-account2-run8-jobs.md`, job R8-OBRED (the "While waiting" action above). One browser
login (`tools/decode_browser_login.js 2118 <scratch> --guess-fullsize --max-files 8 --delay 1700`): logged in, RecordsView/2118
saved, both full-size images served (IMG_R2118_I15025_P1.png and IMG_R2118_I15026_P2.png, 5472x3648 RGB, about 15.9 MB each,
real photographs, not the forbidden.png placeholder). Images kept in the session scratchpad only, never committed (re-fetch:
same command; images are "Authentication required" on DECODE). Requests: de-crypt.org 1 login + 1 record page + 4 files,
1.7 s apart, no 403/429.

**Record fields (H, read from RecordsView/2118):** name `NA_1.01.02._SG_inr.6894_Cornelis_Haga__key_1620`; Nationaal Archief
1.01.02 (Staten-Generaal) inv. 6894; author/sender "Registry of the States General"; **receiver Cornelis Haga (1578-1653), Dutch
ambassador in Constantinople**; dates "1620 -"; type Key; cipher type "Simple substitution, Nomenclatures"; symbol sets
"Graphic signs, Numerical"; 2 pages; cleartext Dutch.

**What the key maps (read by eye from the images, rotated 90 degrees; grade H for the rows quoted, from the key sheet itself):**
- A letter alphabet a-z -> single graphic signs / letter-forms (two strips, a-l on the second image, m/n-z on the first) --
  not numerals.
- A nomenclator of names -> Arabic numerals **1 to 116** (the second image carries 1-~45, its right column cut off at the
  photograph's edge; the first image carries 46-116, ending at 116 "de golff"). Headings: "Int hoff vanden Turcxschen
  Keyser" (1 the present Sultan Osman, 2 Sultan Mustafa his uncle, 3 the vizier, 4 the capitan pasha, 7 the Mufti ...),
  bashas and beys (13-23), "Eenige voorneme steden in Turkie" (24 Mecca?, 25 Cairo, 26 Alexandria, 27 Jerusalem,
  28 Babylonia, 29 Aleppo, **30 Constantinopolis**, 31 Adrianopolis, 32 Buda, 33 Canisa), Mohammedan kings and their
  ambassadors (34-36 ...), Christian princes in friendship with the Turk and their ambassadors (46-64: 49 the King of France,
  51 the King of Great Britain, 55 the Republic of Venice, ~58 the States General's own ambassador), tributary princes
  (60 Ragusa, 62 the Prince of Transylvania), Turkish ships and galleys (76-82), the Christian enemies of the Turkish lands
  (83 France?, 84 Great Britain, 85 Venice, 86 the United Netherlands, 87-92 Spain, Naples, Sicily, the Pope, Malta, Tuscany),
  Turkish islands and harbours (93-102: Cyprus, Rhodes, Scio, Smyrna, Negroponte, Modon, Coron, Navarino, Argiers, Tunis),
  Christian ones (103-116: Candia, Zante, Corfu, Sardinia, Corsica, Messina, Napoli, Livorno, Genua, Marsilia, Ragusa,
  Spalato, Venetia, de golff). Examples above are read from the downsized images; spellings and a few numbers marked "?"
  are M, not checked at full resolution.

**Does it fit this letter's numerals (30-741)?** No, on two independent counts, so no fit test was pre-registered or run:
(1) range -- the key's codes stop at 116, while of the 123 two- and three-digit numbers in the printed p.110-111 text (a rough
count, unfiltered for dates and footnote numbers) about 107 lie above 116, including every high group the editor could not
read (241, 289, 337, 409, 433, 578, 611, 612, 636, 671, 741); (2) content -- the vocabulary is the Ottoman court and the
Levant for Haga's Constantinople embassy (opened 1612), and code 30 is Constantinople, whereas no. 92 is a Heidelberg/Palatine
letter of 1605 about levies and the Palatine-Brandenburg negotiation. The key's letter alphabet is signs, not numerals, so it
cannot explain the letter's numerals as a spelled cipher either. Rule 10 wording: a key read and compared, not a verdict on
the letter.

Effect: route "DECODE 2118" is closed for this target (the drafted OLD-DKEY LOCAL-QUEUE row above is now unnecessary and must
not be filed). DECODE then lists no States-General key from 1595-1615 at all (OLD-DKEY), so the remaining key routes are the
correspondent side (the 122 unscreened Munich BayHStA / Marburg HStAM in-window DECODE keys, OLD-DKEY's "Not listed" paragraph)
and the NA 1.01.02 / 3.01.14 archive hunts of "Key hunt". Status stays `open`.

Next cheap step (named, not run): screen the in-window Palatine/Hessian DECODE key records (Munich BayHStA 102, Marburg HStAM 20)
from their login-free RecordsView pages for a numeral nomenclator reaching the 700s, then open the best one or two images under
one login; ~2-3 (estimate).

## Palatine/Hessian DECODE keys screened (R8-OBRED2, 6 Oct 2026, 04:04-04:24 UTC)

Brief `.claude/briefs/runs/2026-10-06-account2-run8-jobs.md`, job R8-OBRED2 (the "While waiting" action). Table:
`decode_keys_palatine_hessian.tsv` (122 rows, column `fit`). Candidates from the on-disk listing snapshot
(`sources/decode/keys-all-2026-09-28-merged.tsv`), date range touching 1595-1615: **Munich BayHStA 102** -- all one bundle,
Kurbayern Aeusseres Archiv 4591 (records 9277-9423), every one carrying the bundle's blanket date "1475 - 1625", not an
item date; **Marburg HStAM 20** -- Bestand 4 d Nr. 1219 (records 4578-4593, "1600 -") and Nr. 1234 (4687-4691, "1600 - 1699").
(The snapshot spells Muenchen in double-encoded UTF-8; a filter on the city name alone misses all 102 rows -- match on
"Bavaria"/`BayHStA` instead.)

Method: every record's public RecordsView page (login-free) for cipher type, symbol sets, pages and the author field; the
public 200 px thumbnails of the 90 records tagged both Nomenclatures and Numerical (272 thumbnails, viewed as contact
sheets); one browser login for one record's full-size images (4690, the Marburg bundle with visibly numeral name columns).
Images in the session scratchpad only, never committed.

Results:
- **20 records: no numerals** in DECODE's own symbol-set metadata (M: catalogue tagging, not read) -> cannot carry this
  letter's numeral groups.
- **4690 (HStAM 4 d Nr. 1234_03), read at full size (H for the rows quoted):** the right design family -- a homophonic numeral
  letter alphabet (20 a, 21 f, 22 b ... 157) plus a numeral nomenclator in the 300s (300 Kayser, 301 Chur Sachsen,
  302 Churbrandenburg, 303 Churcoelln, 304 Bischof zu Muenster, 305 Bischof zu Paderborn, 306 Koenig in Schweden, 307 Koenig
  in Dennemarck, 308 Herzog Georg Wilhelm zu Braunschweig; then French words 328 Capitaine, 329 Armee, 330 Alliance ...
  339 Conjunction) -- but **out of window**: Georg Wilhelm of Brunswick-Lueneburg was born 1624, and the French military
  vocabulary fits the later 17th century, so not a 1605 key. No fit test.
- **89 numeral-tagged records: fit unknown.** At 200 px the code columns cannot be read. What the thumbnails do show: the
  Munich bundle is overwhelmingly graphic-sign alphabets and name lists keyed to signs, with Italian cover titles ("Con
  Franza", "Con Loreno", "Col Card. de Medici", "Del Ungero", "Con M. Pandolpho da la Staffa", "Duca di Terranova",
  "Vergerio", "Aurelio Augurelio") -- 16th-century Bavarian-Italian correspondence, a weak prior for a 1605 Dutch-language
  Palatine letter. A right-hand code column that may be numerals is present but unresolved in 9280, 9282, 9305, 9306, 9308
  (Munich, German name lists) and 4587, 4691 (Marburg).
- **No record shown to fit.** Rule 10: a screening of DECODE catalogue metadata and thumbnails on 6 Oct 2026, not a key
  verdict and not evidence that no fitting key exists.

Requests: de-crypt.org 122 RecordsView pages + 273 thumbnails (login-free, 1.6 s apart, descriptive UA) + 1 browser login
session (record page + 4 files, 1.7 s apart); no 403/429/challenge.

Status stays `open`.

Next cheap step (named, not run): one browser login, full-size images of the Marburg HStAM 4 d Nr. 1219 numeral-tagged
records (4578, 4579, 4581-4584, 4586, 4587, 4589-4593; about 20 images; Hessen-Kassel under Landgrave Moritz, 1592-1627, is
the in-window Hessian chancery) plus Munich 9280/9282/9305/9306/9308, reading only the code column's range and the item
date; ~3 (estimate). Pre-register a fit test only for a key whose names reach the 700s and whose date touches 1605.


## Marburg 4 d 1219 and five Munich keys read at full size (R9-OBRED3, 6 Oct 2026, 05:18-05:30 UTC)

Brief `.claude/briefs/runs/2026-10-06-account2-run9-jobs.md`, job R9-OBRED3 (R8-OBRED2's named next step). One browser login
(`tools/decode_browser_login.js 4578 <scratch> --fetch-page <17 RecordsView URLs> --guess-fullsize --max-files 140 --delay 1700`):
logged in; all 64 full-size images of the 18 records served (none the forbidden.png placeholder). Images and the logged-in pages
stay in the session scratchpad only, never committed (they carry the account name; re-fetch: same command). Each record read by eye
from a per-record contact sheet of its full-size pages. Results, one row each in `decode_keys_palatine_hessian.tsv` (`fit` column):

- **Marburg HStAM 4 d Nr. 1219 (13 records, 4578-4593): every code value stops at or below 100** (`no-range`). The bundle is
  Hessen-Kassel chancery keys of Landgrave Moritz's time: homophonic numeral alphabets (10-99, 1-96, 10-78, 10-82, 19-99, 11-99)
  with names keyed to graphic signs or letter pairs. The closest in content is **4586** (French, c.1609-14 by its names: 16 les
  Estats du Paisbas, 26 le Prince Maurice, 28 Christian d'Anhalt, 30 le pal. Wolffg. Wilhelm, 33-38 the Electors including
  Palatin, 46 l'Empereur; H for the rows quoted) -- the Palatine/Union network of this letter, but its alphabet is 10-78 and its
  name list 10-46, so it cannot carry 241, 289, 337, 611, 617, 628 or 741. **4589** ("Clavis cum Illustrissimo Principe nostro":
  letters 1-70, names 71-100, 82 Kon. Mattias, 95 Landgraf Moritz) and **4587** (homophonic 10-99, names as signs, Principes
  Uniti, P. Moritz, Conte Jean) are in or near the window and also too small. 4593 is 1620s (Mansfeld, Tilly, Bethlen Gabor).
- **Munich BayHStA KAA 4591 9280, 9282, 9305, 9306, 9308: out of window and wrong symbol set** (`no-date`). Four are copies of one
  German key (Alba, Prinz von Oranien, Prinz von Conde, Admiral, Hugenotten, Pfalzgraf Casimir: c.1568-80) using capitals, Roman
  numerals and signs, with Arabic numerals only for seven cities (No. 1-7) and a few words (und 10, der 2, die 6); 9282 is a
  Cologne-War-era list (Erzherzog Mathias, Herzog Ernst, the Cologne postulation; 1580s) on the same pattern. DECODE's "Numerical"
  tag on these rests on those small numbers.

**Fit:** no record has numeral codes reaching the 700s, or even past 100, so no fit test was pre-registered or run (the brief's
condition was not met). Rule 10: a reading of 18 DECODE key sheets on 6 Oct 2026, not a verdict on the letter and not evidence that
no fitting key exists. A design observation for whoever continues (M, inferred): the in-window Palatine/Hessian chancery keys seen so
far (4586, 4587, 4589, 4581) are all small two-digit systems; a 30-741 code range points to a larger nomenclator than this
chancery's, e.g. a Dutch-side (Oldenbarnevelt/States) key, which is where "Key hunt" already looks.

Requests: de-crypt.org 1 browser login + 18 RecordsView pages + 128 files (64 thumbnails, 64 full-size), 1.7 s apart; no
403/429/challenge.

Still unread at full size in the screened table: 74 Munich KAA 4591 records and Marburg 4687 and 4691 (Nr. 1234, `unknown-thumb`; 4690 of the same bundle was already read as post-1624); the Munich
bundle's thumbnails show the same sign-based 16th-century family as the five read here, so they rank low. Status stays `open`.

Next cheap step (named, not run): the NA 1.01.02 / 3.01.14 archive hunt for a States-side key of 1600-1610 ("Key hunt" above), not
more Munich KAA 4591 sheets.

## NA States-side key hunt, wider terms (R9-NAKEY, 6 Oct 2026, 05:58-06:03 UTC, account 2)

The step named above ("NA 1.01.02 / 3.01.14 archive hunt"), re-run on freshly downloaded full EAD XML of both finding aids
(`www.nationaalarchief.nl/onderzoeken/archief/<toegang>/download/xml`, 3.01.14 4.97 MB, 1.01.02 22.7 MB) with a wider term set
than TX-KEYS (25 Sept: sleutel, cijfer, chiffre, cijferschrift): `cijfer|cyfer|ciffer|cyffer|chiffre|chiffer|zijffer|sleutel|
geheimschrift|gecijferd|ontcijfer|dechiffr|code`, matched per `<c>` element's own text, not its children.

**The letter's own manuscript is in NA 3.01.14 and is digitised (H, read from the catalogue and the first scan).**
- **NA 3.01.14 inv. 1490** (handle `http://hdl.handle.net/10648/7d46913b-93cd-43ac-9f7d-b60fe6e2dee0`): "Missive van Johan
  Wilhelm, hertog van Gulik, Kleef en Berg en Duitsland, aan Johan van Oldenbarnevelt van 21 februari 1605, betreffende de
  diplomatieke en militaire omstandigheden in de Palts, 1605; afschrift (begin 17e eeuw). Met een bijlage, 1605; afschrift.
  2 stukken. 1. Gedeeltelijk in geheimschrift. 2. RGP 108: p. 110-111." Item page `drupal-settings-json`: `"availability":
  "DIGITALIZED"`, 7 scans (METS `https://service.archief.nl/gaf/api/mets/v1/a39ba4d8-4706-43fc-8e9b-3b56d1fe5f57`).
- First scan fetched (`images/na_301_14_1490_p0001.jpg`, 2510x3740) and looked at once, downscaled, by this worker (no
  transcription): headed "Duplicata" top left, a later pencil note "(Brederode aan Oldenb.?)" at the top, Dutch text with
  numeral groups inline -- e.g. "vanden 671 vanden 611 ende 612", "578 337 241 97 409 420 108 289", "741", "146 110 252 433",
  "636", "241 200 50 160 440 210 300 217", "671 ... 613". These are the codes of the printed no. 92 (241, 289, 337, 611, 741
  among those the key screens above tested against). So the manuscript the edition cites as "A.R.A., Holland 2613, e.
  Duplicata" is this item, and route A of YX-OBR (tracing Holland 2613 to a modern toegang) is answered: 3.01.14 inv. 1490.
- Why TX-KEYS missed it: the catalogue says "geheimschrift", not "cijfer"/"sleutel"; and the NA cataloguer gives the sender as
  Johann Wilhelm of Jülich-Cleves-Berg, where the editor (in square brackets) and the pencil note give P. van Brederode. The
  attribution conflict is recorded, not settled (M either way).
- Consequence for this folder (rule 2): `ciphertext.txt` comes from the printed edition only; a page image of the cipher itself
  now exists. The printed numerals have not been checked against the 7 scans.

**States-side keys in or near the window (catalogue, H; key design read from one scan, H for what is visible):**
- **NA 3.01.14 inv. 2028** (`http://hdl.handle.net/10648/86f02055-7104-4de5-90ff-25c725a8c62d`): "Stuk houdende de sleutel voor
  de decodering van de code die Johan van Oldenbarnevelt gebruikte in zijn correspondentie met Paul Choart, heer Van Buzanval,
  ambassadeur van Frankrijk in de Republiek, [eind 16e eeuw]; afschrift." Digitised, 3 scans (METS
  `https://service.archief.nl/gaf/api/mets/v1/676010c8-0563-4b90-ba2a-801de20fea7b`). First scan fetched
  (`images/na_301_14_2028_p0001.jpg`): a **syllabary**, columns "Sillabes" (ba be bi bo bu by, ca ... ry, sa) and "Supplet
  Letters" (a-z), each syllable or letter mapped to one to three **numbers from about 1 to 99**, some with a bar or cross mark
  over the digit, a few to letters or short words; a worked example on the right ("Exempel ... Wy hebben het gerucht laten
  luyden") enciphered syllable by syllable. Old number "2625 l" in pencil at the foot (the same old Holland numbering as
  "Holland 2613 e"). **No three-digit numbers on this scan**, so as seen it is not a numeral nomenclator reaching 241-741; scans
  2-3 (possibly a names list) were not fetched, per the brief. Fit test: not run (brief).
- **NA 3.01.14 inv. 2016-2025**: François van Aerssen to Oldenbarnevelt, 1598-1602 and 1605-1609, originals, "Gedeeltelijk in
  cijfercode. Gedeeltelijk gedecodeerd. Bij de missive van 1598 augustus 10 bevindt zich een sleutel." Inv. 2016 (1598) is
  digitised (METS `https://service.archief.nl/gaf/api/mets/v1/70426ba3-d59c-474d-bd4b-f9906cbe37de`, 81 scans); the key's
  scan was not located or fetched (it is inside the pack, not the first scan). Partly decoded originals of the same chancery
  1605-1609 = a deciphered-sibling source for Oldenbarnevelt's own cipher practice in the window.
- **NA 3.01.14 inv. 1769**: Oldenbarnevelt to Otto Hendrik van Bylandt, 14 Oct 1595, minute, "In het Frans, gedeeltelijk in
  geheimschrift", RGP 80 pp.318-319, digitised (dao present; flag not fetched). Outgoing States-side cipher, 10 years early.
- Other 3.01.14 hits (inv. 937 verdeelsleutel 1586; 2442 Spanish 1605, its own target folder; 2980 a 1594 "codebrief"; 3429
  1590 Egmond annexes) are not this correspondence.
- **NA 1.01.02**: 78 hits, none dated 1595-1615 except the already-logged Ottoman key (12578.1, 1618-22); the rest are
  1629-1691 ("gedeeltelijk in cijfer" letters from Copenhagen, Stockholm, London, Madrid; "Cijfers, 1652"). No States-General
  key of 1600-1610 under these terms.

Next steps (named, not run): (1) read the 7 scans of 3.01.14 inv. 1490 and check `ciphertext.txt` against them -- an image
check, one subagent pass per scan on line crops (`tools/iiif_lines.py --image`), ~1.5 per scan, ~12 with reconciliation;
(2) fetch scans 2-3 of inv. 2028 to see whether the Buzanval key has a three-digit names list (2 requests; no fit test before
a PREREG); (3) locate the 10 Aug 1598 key inside inv. 2016 (81 scans, thumbnails first). Status stays `open`.

Requests: `www.nationaalarchief.nl` 3 (two EAD XML, item page 1490); `service.archief.nl` 5 (METS 1490, 2016, 2028; two
first-scan images); all >= 2 s apart, descriptive User-Agent, no 403/429/challenge. (Plus 2 for the Rumpf re-probe, logged
in that folder.) No subagents.

## Image check of ciphertext.txt against NA 3.01.14 inv. 1490 (R9-OBRED4, 6 Oct 2026, 06:25-06:32 UTC, account 2)

All 7 scans of inv. 1490 fetched once (`images/na_301_14_1490_p0001..7.jpg`, METS a39ba4d8-...). The letter is scans 1 (one page) and
2 (one opening, two pages); scan 3 is the endorsement (dated 1605, read on the thumbnail only), scans 4-6 are the annex (money accounts,
no numeral code groups seen), scan 7 an endorsement. Line crops: `tools/iiif_lines.py --image ... --out ... --debug` (commands in
`imagecheck_1490/README.txt`; debug overlays checked, 29 + 29 + 26 bands, every text line in one band), 84 crops in
`images/crops_1490/`. One blind Sonnet pass per page on line crops only (3 calls), then a script diff against the print
(`imagecheck_1490/printed_numerals.py`), then each disagreement settled by this worker on the line crop or a zoom of the scan.

- **121 printed code groups (355 digits), all 121 located on the manuscript, in the same order; the edition omits no line or
  paragraph** (the closing "Men heeft alhier advijs dat 588 aen 628 ..." paragraph is in both).
- Blind pass agreed with the print on 107/121 groups (88.4%); 12 of the 14 disagreements were settled for the print on the image,
  8 of them the hand's s-shaped 8 (read by the pass as 5, 0 or a letter: 628 x3, 80, 108, 218, 438, 387).
- **One group differs: printed "170" reads "179" on the manuscript** (scan 2 left, line 21, "... 49 314 30 467 387 179 sullen oock
  XII off XIII M. doen"), H on the image: round head with a descender like the line's other 9s; a fold crosses the tail.
- One group not confirmable: "704" (scan 2 left, line 24, end of line) is under an ink blot, M; print kept.
- Editorial, not cipher: the manuscript has "XXX M." and "XII off XIII M." where the print has "30.000" and "12 off 13.000".
- Per-sign: 355 digits, 1 differing (0.3%), 1 not legible (0.3%). Recorded in `imagecheck_1490/corrections.tsv`; `ciphertext.txt` is
  left as printed (never silently repaired).
- Which tests on disk would change: none materially. The key screens (decode_keys_1600s.tsv, decode_keys_palatine_hessian.tsv,
  OLD-DKEY, R8-OBRED2, R9-OBRED3) tested numeral range (max 741), office and design, not single values; 179 sits inside the
  same range. No reading, key.tsv or spec exists for this folder, so nothing needs re-running. Rule 2 is now met for the cipher
  groups: a future test can cite the manuscript, with the one correction applied.
- Attribution: the right-hand page ends with a monogram above "onderdanigen ende getrouwen dienaer"; not read here (the
  Brederode vs Johann Wilhelm attribution conflict stays M).

**Step 0, inv. 2028 (Buzanval key), scans 2-3 fetched (`images/na_301_14_2028_p0002/3.jpg`).** Scan 2 is the decipher table
("Patroon om eenich brief ... te dechiffreren"): numbers 10-99 plain, 10-99 with a bar ("Cyfers met schrapkens boven"), and with
a cross ("Cyfers met cruyskens boven"), each to a syllable or letter; "Latynsche grote letters" and "Gemeyne letters" to
syllables; a short "Sillabes" column; "Characters" (+ mi, ++ so). **No three-digit numbers and no names list.** Scan 3 is the
cover ("Cyfre met den heer van Buzanval"). As seen it cannot carry this letter's groups (97-741, mostly 100-741, no bars or crosses
recorded in the print or seen on the manuscript). No fit test (brief).

Next steps (named, not run): (1) locate the 10 Aug 1598 key inside NA 3.01.14 inv. 2016 (81 scans, thumbnails first); (2) the
Brederode-side correspondence in NA 1.01.02 inv. 6016 from image order 261 on (named by TX-KEYS) for a sibling cipher letter with
a gloss. Requests: `service.archief.nl` 10 (2 METS, 8 images), >= 2 s apart, descriptive UA, no 403/429/challenge. Subagents: 3
Sonnet blind passes (one per page).

## Verifier on the inv. 1490 corrections (R10-OBREDV, 6 Oct 2026, account 2)

AUDIT.md "Verifier: R9-OBRED4 corrections": 170 -> 179 upheld (bowl and right stroke match the scan's 9, not its 0; the crease is
only a thin line above the bowl), 704 upheld as undecidable (blot; print kept, M). ciphertext.txt unchanged; no test on disk changes.

## The 10 Aug 1598 "sleutel" in NA 3.01.14 inv. 2016 located (R10-OBRED98, 6 Oct 2026, 07:22-07:28 UTC, account 2)

Step (1) of the R9-OBRED4 next steps. METS fetched once (81 scans; full list with IIIF info URLs in `na_301_14_2016_scans.tsv`).
Contact sheets of every third scan (1, 4, ..., 79) at 400 px by this worker's own eye, then candidates at 1400 px. Dates on the
thumbnails run in order: scan 4 "May 1598", scan 7 "7-6-1598", scans 34/37 Sept 1598, scans 67-79 Oct 1598.

**Where the key is (H, read on the image):** scans 30-32. Scan 30 (`images/na_301_14_2016_p0030.jpg`) is Van Aerssen to
Oldenbarnevelt, pencil-dated "10-8-1598", p.1 in French, in clear ("Le brief du 29e de Juillet me fut delivree le 4e d'Aoust ...").
Scans 31 and 32 are the same inner opening photographed twice, with a loose slip laid first over the right page, then over the
left. The slip (`images/na_301_14_2016_p0031_slip.jpg`) is headed "bij no 6" and pencil-dated "10-8-1598": this is the catalogue's
"sleutel". It is a **worked decipherment, not a key table**: each cipher group copied with its plaintext syllable written over it
(e.g. "de fonz" over "2d 3S 12 21", "aessert" over "37 . S 3S 20 iS"), and marginal letters a-d each given as a whole French phrase
("c trouue quatre vingtz mil escus en papier sur lres [one word not read] corroborees par celles de Mr d'Incarville ...", "d de se roidir a
ne rien innouer de la premiere posture").

**Design (H for what is visible, no transcription made):**
- Two layers. (a) A **phrase code**: single letters a-x (and a few signs) each standing for a phrase or a name ("Mr de Villeroy",
  "Calais", "Le Roy", "Mr le Mareschal de Bouillon", "Mr de Buzanval", "Mr d'Incarville", "Le Cardinal d'Austriche"); the key
  changes per letter, with a gloss sheet per letter ("bij no 2" scan 7, 7-6-1598; "No 4" scan 16; "bij no 6" the slip).
  (b) A **syllabary**: mostly one- and two-digit numbers (about 2-97 seen) with over-bars, dots and superscript strokes, plus a few
  letter-like signs, each to a French syllable or letter; isolated three-digit groups (109, 526) occur but are rare.
- Language French. The letters' own pages carry interlinear decipherments above the cipher (scan 31 left, scan 32 right: "de Mr de
  Villeroy", "pour la Royne d'Angleterre", "rendition des gages", "Le Roy", "Breda" ...).

**Fit to this folder's ciphertext: not a plausible design match, so no fit test was run (no PREREG).** No. 92 is Dutch, 121 unmarked
groups of mostly three digits (97-741, 100-741 for all but a handful), with no bars, dots or letter signs on the print or on the
manuscript (R9-OBRED4). A two-layer French syllabary of marked one- and two-digit numbers cannot produce that stream. Recorded as a
design exclusion of this key for no. 92 (H on the design, not a statistical negative).

**Siblings with a period decipherment (the higher-value find, for a different correspondence):** inv. 2016 itself carries several
partly deciphered originals of 1598 -- scans 31/32 (10 Aug), and numeral passages visible on the thumbnails of scans 43 (Sept 1598)
and 64 -- plus per-letter gloss sheets (scans 7, 16, 31 slip). With inv. 2017-2025 (1599-1609, "Gedeeltelijk gedecodeerd") this is a
period-decipherment pool for Van Aerssen's own syllabary, which by its marked one- and two-digit numbers resembles the Buzanval
syllabary of inv. 2028 (numbers 10-99 plain, barred, crossed; R9-OBRED4 step 0). That resemblance is an observation (M), not tested.
None of it bears on no. 92's three-digit Dutch code.

Next steps (named, not run): (1) NA 1.01.02 inv. 6016 from image order 261 on, for a Brederode-side sibling cipher letter with a
gloss (unchanged from R9-OBRED4). (2) Out of this folder's scope, a possible target of its own: Van Aerssen 1598-1609 (NA 3.01.14 inv.
2016-2025) as a period-glossed syllabary pool; a scout or check-solved worker decides whether it belongs on the queue. Status stays
`open`.

Requests: `service.archief.nl` 34 (1 METS, 27 thumbnails at 400 px, 5 scans at 1400 px, 1 region crop), >= 1.9 s apart, descriptive
User-Agent, no 403/429/challenge. No subagents.

## OBRED-6016 (10 Oct 2026, 02:46-02:5x UTC by date -u, account 2, Sonnet)

Brief: contact-sheet screen of NA 1.01.02 inv. 6016 "from image order 261" for a Brederode-side cipher letter with a period gloss. Orders 260-350
were already read leaf by leaf by YX-OBR (25 Sept 2026, `obr_6016_leaflog.tsv`, 91 leaves, no numeral cipher, key or gloss), so this pass starts at
351 (the "1607 - 1608" divider) and runs to the end of the object, 624.

- Prior-work step: `prior_work.py` run (step lookup, exit 4: one LEAD, my own live claim, plus UNCHECKED rows for a unit with no folio), all five rows
  recorded CLEAR in `prior-work.tsv`; checks 1-4 by hand are the folder's own Premise check lines (a)-(c) above (3 Oct 2026): own files, solver repos
  and Tomokiyo, edition and neighbours; no unit-keyed prior work on inv. 6016 351-624 on file.
- Route: METS `service.archief.nl/gaf/api/mets/v1/4153f78f-...` (1 request, 624 scans, order -> IIIF base), then IIIF `/full/400,/0/default.jpg` for every
  third scan 351, 354, ..., 624 (92 scans, 2.0 s apart) and `/full/1200,/0/default.jpg` for four. Descriptive User-Agent, all HTTP 200, no 403/429/challenge.
  Requests: service.archief.nl 97 (1 METS, 92 at 400 px, 4 at 1200 px); cap was 120.
- Method: ten contact sheets, each seeded with the same two controls from disk (no request): CTRL-CIPHER = NA 3.01.14 inv. 2016 scan 31
  (`na_301_14_2016_p0031.jpg`, the interlinear decipherment opening with numeral groups) and CTRL-PLAIN = inv. 6016 order 261. One reader (this worker's own
  eye, no subagent). Control calls: on all ten sheets the cipher control read as figure-groups and the plain control as running prose (10/10 seen both), so no
  sheet is a non-test by the brief's rule. Calls per scan are in `images/6016_screen.tsv` (92 rows, every one "no cipher").
- Result: **no numeral-code page, key table or interlinear decipherment seen on any of the 92 scans.** Four scans were re-looked at 1200 px because a sheet
  showed something unusual: 417 (dense Dutch columns, p.355; plain prose), 492 (a slip-like block on the left leaf is the upside-down address of a German
  letter dated 31 Jan 1610 from Christian of Anhalt; plain), 507 (a note slip on a German letter of 5 Jan 1611; plain), 597 (a Dutch letter, marginal date
  "11 Juli 161[3]", with a stray "1, 91" annotation; plain, no code groups). Glossed: no for all four. Year dividers seen at 357 (1607), 375 (1608), 408
  (1609), 498 (1611). 417 and 492 are committed as `images/na_101_02_6016_p0417_1200.jpg` and `..._p0492_1200.jpg`.
- Where it was not found, and the limits: every third scan only, so 182 of the 274 scans in 351-624 were not looked at (a cipher letter or key slip on one
  leaf only could sit in them); contact sheets at 400 px show a numeral run of the control's density, a short code passage inside prose may not stand out; the
  positive control is a French letter of 1598 with dense figure-groups, not a Dutch three-digit run like no. 92; orders 1-259 (1602-1604) were not in the
  brief and are unlooked beyond the six sample leaves of TX-KEYS. Not a negative for the series; a negative for the sampled leaves at this resolution only.

## OBRED-0259 (10 Oct 2026, 05:43-06:0x UTC by date -u, account 2, Sonnet)

Brief: the same contact-sheet screen as OBRED-6016, for NA 1.01.02 inv. 6016 image orders 1-259 (1602-1604), stride 3 (scans 1, 4, ..., 259 = 87 scans).

- Prior-work step: `prior_work.py` (step lookup, exit 4: one LEAD = my own live claim, four UNCHECKED rows: no unit-keyed prior work); all five recorded CLEAR in
  `prior-work.tsv`. Checks 1-4 by hand are the folder's Premise check (a)-(c) (3 Oct 2026); nothing on file keyed to inv. 6016 orders 1-259 beyond the six sample leaves
  of TX-KEYS (orders 1, 100, 180, 260-262). Check 5 (after a decode): not applicable, nothing decoded.
- Route: METS (1 request) then IIIF `/full/400,/0/default.jpg` for 87 scans, 2.1 s apart, descriptive User-Agent, and `/full/1200,/0/default.jpg` for six. Requests to
  service.archief.nl: 94 (1 METS, 87, 6), all HTTP 200, no 403/429/challenge (cap 95).
- Method: nine contact sheets (ten scans each, seven on the last), every sheet seeded with the same two disk controls placed by a seeded shuffle (CTRL-CIPHER = inv. 2016
  scan 31, CTRL-PLAIN = inv. 6016 order 261). One reader, this worker's own eye, no subagent. Control calls: on all nine sheets the cipher control read as
  figure-groups and the plain control as running prose (9/9 both), so no sheet is a non-test by the brief's rule. Calls per scan: `images/6016_screen_0001_0259.tsv` (87 rows).
- **Found: scan 187 (inv. 6016 image order 187; leaf folio-numbered "143" by the archive's pencil mark) carries a Dutch letter dated "... 17 october 1604" ending
  "... onderdanigen ende getrouwen dienaer" with a signature beginning "P. Br..." (not read further), and directly under the signature a block of five lines of numeral
  groups, mostly three-digit (about 85 groups by a rough count, values seen from 36 to 758 including 577, 457, 289, 217, 623, 553), with a short clear-text insertion in
  the third-to-fourth line that I read as "oock bestaen dat dits" (reading M, not checked at native size).** Seen at 1200 px
  (`images/na_101_02_6016_p0187_1200.jpg`) and a 3x local zoom of the block (`images/na_101_02_6016_p0187_numerals_zoom.jpg`, no request). The sign-off wording is the same
  formula that the folder records for no. 92 ("UE. onderdanigen ende getrouwen dienaer", above). Not transcribed, not decoded, not graded: a by-eye finding on one leaf,
  grade M. Whether this leaf is the same sender and what its cipher block belongs to is not established here.
- Five further 1200 px looks, all plain (Glossed: no): 208 (reversed show-through of a letter dated 1604 and a note block; no numerals), 232 (Latin text with marginal
  notes), 256 (two loose Dutch letters dated 4 Sept? and 21 Aug 1604, deleted words only), 205 (German letter of the Elector's court, an inventory slip), 85 (Dutch
  letter of 1603, note slip). Committed beside the 187 pair.
- Year dividers seen: 1 (1602-1603), 127 (1604); the "1605" divider is the control at 261.
- Where it was not found, and the limits: every third scan only, so 173 of the 259 scans in 1-259 were not looked at (the two scans between each sampled one, including
  186 and 188, which may continue the 187 letter); 400 px sheets show a numeral run of the control's density and a short code passage inside prose may not stand out;
  the positive control is a French letter of 1598, not a Dutch three-digit run; the cipher block on 187 was found only because it is large and sits on a leaf sampled by
  the stride. Not a negative for the series elsewhere; a negative for the other 86 sampled leaves at this resolution only.

## OBRED-187 (10 Oct 2026, 06:12-06:2x UTC by date -u, account 2, Opus worker, Sonnet subagents)

Brief: the scan-187 postscript (NA 1.01.02 inv. 6016 image order 187, archive leaf 143r) -- prior work, native fetch of 186-188, the clear letter,
a blind transcription of the numeral block, and a pre-registered overlap test against no. 92's printed values. No decode, no key.

- Prior work: `prior_work.py ... --item-spec 'shelfmark=NA 1.01.02 inv. 6016;folio=scan 187;date=1604-10-17;...' --step-type transcribe --fetch`
  exit 4 (2 LEAD = OBRED-0259's claim and my own; LOOK 2-leaf; UNCHECKED 3-tomokiyo, 3-solver; UNCHECKED-NET 3-solver aaymeloglu, 4-editions);
  five recorded CLEAR in `prior-work.tsv` after the checks below; the two -NET rows stay unchecked by the tool (edition check by hand below).
  - Check 1 (own work): folder NOTES/AUDIT/decode-key TSVs and sources/decode grepped for "1604" and Brederode: only OBRED-0259's find; no transcription on file.
  - Check 2 (leaf and neighbours): scans 186-188 at native size (5000 px). 186 right = leaf 142r, the letter's opening; 187 left = 142v, 187 right = 143r
    (letter end, signature, numeral block); 188 left = 143v, the address leaf, with only mirror show-through of the numerals; 188 right = 144r, a French
    news enclosure ("Quant a l'estat des affaires de dela ..." on Denmark, Sweden, Duke Charles, Livonia, Brandenburg) under the same docket. No
    interlinear or marginal decipherment, no clear copy, no "ontcijferd" note on any of the six pages. The code does not continue on 186 or 188.
  - Check 4 (edition): Huygens retroboeken/oldenbarnevelt full-text search, all three volumes: "17 october 1604" 2 hits (Deel 1 p.719 errata; Deel 2 p.106,
    nos. 88-89 of Aug/Sept 1604 -- the OCR matched the words separately), "Brederode" 181 hits (first 20 read; Deel 1 only), "Stettin" 2 hits (Deel 3 only,
    1614-20). Deel 2 pp.106-107 read in full: the edition runs no. 89 (J. van der Veken, 28 Sept 1604) -> no. 90 (P. Merula, 27 Nov 1604), so **the
    17 Oct 1604 letter is not printed in Veenendaal II** (chronological order; positive control: no. 92's own letter is found on p.110 by the same route,
    25 Sept 2026). The edition prints Oldenbarnevelt's papers; this letter is addressed to the griffier (below), which fits its absence. Its postscript is
    therefore neither printed, marked nor deciphered there. Not searched: the Resolutiën der Staten-Generaal XIII for Oct-Nov 1604 (a griffier letter
    would be read in the States General), the Den Tex biography, Brandenburg-side editions.
  - Requests: resources.huygens.knaw.nl 6 (3 searches, pages.json, 2 page texts); service.archief.nl 4 (METS + 3 native scans). All HTTP 200.
- The clear letter (by eye at native size, grade M throughout): opening (142r) "Edele Erntfesten Hoochgeleerde wyse ende seer voorsinnige heere, Uijt mijne
  voorgaende schrijven aen mijn heere van Oldenbarnevelt sullen mijn E.M. heeren sonder twijfel ... verstaen hebben ... van mijne negotiatie bijden
  Churf. van Brandenburg ende om wat oorsaeck mij dese mijne reyse op Stettin noodich gevonden heeft ..."; end (143r) "... uijt Stetijn desen 17 october
  1604. U E. onderdanighe ende getrouwen dienaer P. Brederode"; docket at the head of each leaf "de Stettin le 17 octob. 1604"; address (143v, upside
  down) "Den Edele Erntfesten hoochgeleerde wyse ende seer voorsinnighe heere [Doctor? Aerssens], Griffier van mijn heeren Staten Generael der vereenichde
  Nederlanden, mijne gunstighe heere, in den [Hage]". So: P. Brederode to the griffier of the States General (the name read is M), from Stettin, on his
  negotiation with the Elector of Brandenburg (Berlin) and his journey to Stettin, with talk of a particular alliance (Brandenburg, England, Denmark,
  "the whole Empire") on 142v. Images: `images/na_101_02_6016_p0187_native.jpg` (5000x3933), `..._p0186_opening.jpg`, `..._p0187_dateline.jpg`,
  `..._p0188_address_rot180.jpg`.
- Transcription: `tools/iiif_lines.py --image images/na_101_02_6016_p0187_native.jpg --out images/p187_lines --region 2930,2450,1840,450 --prefix p187
  --centres 142,205,263,324,378 --deskew 300 --band-extent 0.35 --debug` -> 5 line crops (auto-detection found 4 slanted bands; centres given by eye
  from the debug overlay; a --mask-neighbours cut lost the raised digits and was discarded). Two blind Sonnet passes on the crops only (not told no. 92
  or any value): **59 numeral groups, the two passes agree on 59/59**; reconciliation on the crops by me: `ciphertext_187.tsv`, 49 H-read, 10 M
  (low-confidence shapes: 265, 48, 444, 440, 751, 461, 553, 335, 105, 450; "444 440" run together with a heavy 4 at the join, possibly overwritten),
  plus two clear insertions kept as text: L3 end "[Ick hebbe]" (faded) and L4 start "[oock verstaen dat dits]" (M). 48 313 sit under an overline.
  OBRED-0259's "about 85 groups" was a rough count; the block is 59.
- Overlap test: `obred187/PREREG-OBRED187.md` pushed in its own commit 774b4ccb1 before scoring; `python3 obred187/overlap.py` (`--check` OK) ->
  `obred187/overlap.json`. V187 57 distinct of 59 tokens; V92 99 distinct of 121 tokens (ciphertext.txt); **S = 26 shared values** (40 80 97 105 108 110
  119 137 139 144 217 289 330 337 409 420 433 440 457 461 481 492 529 577 611 623). C1 uniform on 1..751: mean 7.42, p99 13, p = 0.0001; C2 band-matched
  to 187's hundreds histogram: mean 8.72, p99 15, p = 0.0001; negatives subsampled to 59 tokens: N1 Lodewijk 7206 (1574) mean 5.19, p95 8; N2 Jan van
  Nassau 5551 (32 tokens, resampled) mean 5.07, p95 6. H-read only: 24 of 49. **The overlap clears its pre-registered control** (p < 0.01 under both
  models and above both negatives): consistent with no. 92 (Heidelberg, Feb 1605) and the Stettin postscript (Oct 1604) using one code list, grade M,
  not a reading. Caveat: N2 is short (32 numerals); the negatives also have smaller ranges (max 348, 146), so they bound chance only loosely -- C1/C2 carry
  the gate. `tools/key_design.py` has no fit: it needs a code->letter key table and none exists; not run.
- Where it was not found: no decipherment of either text on the leaves 142-144, in Veenendaal II, or in the folder's DECODE notes; the 173 unlooked
  scans of orders 1-259 other than 186/188 were not looked at.

## Remaining gaps (OBRED-187, 10 Oct 2026)
Read so far: unmeasured; nothing decoded -- no. 92 (121 groups) and the scan-187 postscript (59 groups, transcribed this pass) are both unread; they share 26 values, above chance (OBRED-187)
- no. 92 and the 187 postscript, pooled (180 tokens, about 130 distinct values) - blocker: not-attempted; the shared-list evidence is new this pass and the brief stops before an attack; next: lane decides a design_prior / pooled-attack step on the two texts with a matched control at N=180, ~$3
- the 173 unlooked scans of NA 1.01.02 inv. 6016 orders 1-259 - blocker: not-attempted; stride-3 screen only; next: 400 px sheets at stride 1 around 187 (orders 181-193 first: further Brederode letters of 1604 in the same hand and code), ~$1.5
- the 182 unlooked scans of NA 1.01.02 inv. 6016 orders 351-624 - blocker: not-attempted; stride-3 sampling found no cipher; next: two more sessions of 400 px sheets, ~$1.5 each
- States-side trace of the 17 Oct 1604 letter (Resolutiën der Staten-Generaal XIII, Oct-Nov 1604; the griffier's papers) - blocker: not-attempted; outside this brief's named sources; next: Huygens retroboeken/statengeneraal search "Brederode" + "Stettin" in Deel 13, ~$0.5

## Escalation (OBRED-187, 10 Oct 2026)
- [ ] siblings: scan 187 is a second code text sharing 26 values with no. 92 (OBRED-187); further 1604 Brederode letters may sit in the unlooked scans of orders 1-259; next: stride-1 sheets of 181-193, then the rest
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187: Stettin, 17 Oct 1604, to the griffier of the States General, on the Brandenburg negotiation); it carries no gloss of the code
- [x] known-keys: the 10 Aug 1598 Van Aerssen slip excluded for no. 92 by design (R10-OBRED98); Buzanval syllabary inv. 2028 excluded (R9-OBRED4); DECODE 1600s and Palatine/Hessian keys screened (OLD-DKEY, R8-OBRED2, R9-OBRED3); the 187 values fall in the same 1-751 range as no. 92 and add no key
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187, nos. 89 -> 90)
- [ ] key-rebuild: the pooled two-text attack is now the named step (overlap gate cleared, OBRED-187); next: design_prior.py and a pooled family run with a matched control at N=180, ~$3
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv is two blind passes agreeing 59/59 on native crops (OBRED-187)
- [ ] retry: the Den Tex biography (dbnl.org) retry named in "Open" above has not been run (TLS-failed twice, 25 Sept 2026); next: one retry from a fresh container, ~$0.3
Verdict: keep going: 4 internal gaps; cheapest next: the pooled no. 92 + 187 attack (design_prior first), ~$3
