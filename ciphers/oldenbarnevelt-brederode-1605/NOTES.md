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

## OBRED-DP (10 Oct 2026, 06:50-06:59 UTC by date -u, account 2, Opus)

Brief: pooled structure of no. 92 + the scan-187 postscript, and a print check. No decode, no key; nothing below is a reading.

- **Print check, Resolutiën der Staten-Generaal XIII OR (1604-1606, GS 101)** (Huygens retroboeken/statengeneraal, `searchText`, `source_id=13OR`;
  10 requests to resources.huygens.knaw.nl, all 200, take/release in ROOM). Queries: `Brederode` 39 hits (positive control: it returns the
  known p.101 entry, Oldenbarnevelt communicating Brederode's letter of 21 Feb 1605, and p.104, Brederode's letter of 22 June 1604 from
  Frankfurt read 1 July -- the route works); `Stettin` 8 hits (p.114 Bogislaw of Pommern, p.640, the rest index pages -- no Brederode letter
  from Stettin); `ontcijferd` 0, `dechiffr` 0, `cyffer` 0, `cijffer` 0 (`cijfer` 1 and `sleutel` 1, both off-topic, were run on 25 Sept, see
  "Key route" section 4). Pages 104, 108, 111 (the Oct-Dec 1604 Brederode entries) read in full from the OCR page text: 14 Oct a Brandenburg
  letter of 15 June received, 29 Oct and 11-19 Nov the Margrave's visit and an instruction to write to Brederode, 23 Nov a procuration for
  Brederode; **no receipt of a 17 Oct 1604 Stettin letter is minuted on these pages, and no "met het cijfer", decipherment or key note sits
  near any Brederode entry of Oct 1604-Feb 1605.** Not found here: a period decipherment of either text. Not searched: the S.G. archive
  files the footnotes cite (R.A., S.G. 5888, 5968), which are archive items, not print.
- **design_prior.py** (`python3 tools/design_prior.py ciphers/oldenbarnevelt-brederode-1605/obred187/tokens_{pooled,92,187}.txt --no-write`;
  token files written from `overlap.py`'s extractors):
  - pooled, 180 tokens, 130 distinct: multi-sign d=0.73 (envelope 0.26, null_p05 0.27) -> not above null; letter-for-letter d=1.90 excluded;
    mixed d=2.28 excluded; code d=3.07 excluded; shuffled-input false-positive rate 0.065; fine (advisory) nomenclator 1.09, homophonic 1.14,
    syllabary 1.36; nearest key huntington-luzerne-destouches-1781 (syllabary) d=0.20.
  - no. 92 alone, 121/99: multi-sign d=0.32 (env 0.27, null_p05 0.11) -> not above null; letter-for-letter, code, mixed excluded; fp 0.085;
    fine: syllabary 0.32, nomenclator 0.93, homophonic 1.00.
  - 187 alone, 59/57: multi-sign d=0.79 not above null; code and mixed not above null; letter-for-letter excluded; fp 0.140; fine: syllabary 0.79.
  Reading: every run excludes one-sign-per-letter and code-number designs and leaves the multi-sign class (homophonic / nomenclator / syllabary,
  which the tool cannot separate) nearest; the pooled multi-sign distance sits outside its own printed envelope yet the tool prints "not above
  null" rather than "excluded" -- reported as printed, not investigated (a one-line question for the tool's owner).
- **Structure** (`obred187/structure.py`, `--check` OK, output `obred187/structure.json`; gates pre-registered in `obred187/PREREG-OBREDDP.md`,
  pushed in its own commit ae9dd4a8d before scoring):
  - Runs. no. 92 splits into 43 runs at the clear words: 34 single tokens and 9 runs of 4-15 (8, 4, 8, 12, 6, 13, 15, 11, 10); 187 is two runs
    (43 and 16) either side of the clear insertion "[Ick hebbe] ... [oock verstaen dat dits]".
  - **G2 (names stand alone): PASS.** All 33 no. 92 tokens >= 600 stand as single-token runs (H = 1.000) against a value permutation over the
    same run structure (mean 0.281, p99 0.424, p = 0.0001). The single tokens span 588-741 (34 tokens; 97% >= 600) and occupy name slots by
    grammar ("van den 671 van den 611 ende 612", "617 is op ghisterenavont alhier angelandt", "advijs dat 588 aen 628 geschreeven heeft").
    Grade M: a nomenclator name band about 588-751. In 187 three band values sit inside the long run (611, 623, 751-M) -- names inside a spelled sentence.
  - **G1 (shared order): FAIL.** One ordered pair is shared across the texts, 529 433 (no. 92 run "577 102 481 529 433 ..." and 187 L2
    "84 529 433 337"), against an order permutation of each text (mean 0.097, p99 1.0, p = 0.0923); no shared trigram. The control can differ
    (order-dependent statistic). "No shared order above chance at N=180", not a design exclusion. Descriptive: both texts' long runs open with
    577 (no. 92 "Van 577 102 481 ...", 187 L1 "577 457 289 ...").
  - Value range by run length: long runs (6+) 142 tokens, values 30-507 except 3 band values (hundreds 0:17, 100:36, 200:18, 300:25, 400:35,
    500:8, 600+:3); runs of 2-5 (one run, 4 tokens) 110-433. Pooled long-run tokens 146, 113 distinct: no value occurs more than 3 times
    (108, 433, 440, 40 three times each).
  - Crib slots in no. 92 (grade I, grammatical inference only; the word candidates are illustrations, not tested): "hij neffens [8] bevel heeft
    om met 741 daer van te handelen" ([8] = a person or office, co-subject); "datter oock noch [4] van de zijde van 611 ende 612 ... sal
    gefourneert werden" ([4] = what is furnished: a sum or troops); "dat hij XLII [12] belooft heeft ... ende hoewel die quota wel wat meer
    bedraecht" ([12] after a Roman numeral = a promised amount; XLII may itself be part of the sum); "636 ende [6] sullen oock 12 off 13.000
    doen" ([6] = a second contributing party beside the name code 636, spelled out, so not in the name band); "dat hij [11] uyt sijn voornempste
    [10] lichten mach" ([11] = what may be raised -- men or money; [10] = a plural noun after "sijn voornempste", e.g. towns, offices or
    subjects); "Van [13] ende [15] ende is vermeent ... sich tot sulx te begeven" (two spelled stretches, the first a source of news).
  - Ranked design hypotheses (each with its test and matched control):
    1. **Nomenclator: a name band (~588-751, single codes) + a lower table (~30-507) that spells words** -- supported by G2 and the
       grammar of the slots. Test that remains: none needed for the band; the lower table is the question below.
    2. Lower table = **letter-level homophonic** (~480 values over ~24 letters, ~20 homophones each; run length = letter count). Fits the
       near-absence of repeats (146 tokens, 113 distinct) and a 10-group run in a one-noun slot. Test: run-length vs word-length fit over the
       crib slots, and a value-band x letter-class test once a crib holds. Matched control: synthetic Dutch letter-homophonic, ~480 values,
       N=146 in runs of the same lengths, corpus era-matched (no 17c Dutch prose corpus checked this pass -- confirm tools/data first).
    3. Lower table = **syllabary** (letters + syllables, run length < letter count). design_prior's fine tier puts syllabary nearest for both
       texts (advisory, not calibrated). Test and control: as 2 with a syllable table; the 10-group run in a one-noun slot fits 2 better than 3.
    4. Lower table = **word code** (one group per word): unlikely -- an 8-group co-subject and a 10-group noun after "sijn voornempste" would
       be 8-10 words. Control: synthetic word-code text, same N and run lengths.
  - Unicity: at ~20 homophones per letter, 146 spelled tokens with 113 distinct values make any crib nearly unfalsifiable (a value seen once
    can take any letter); this is the editor's own "te weinig vergelijkingsmateriaal" in numbers. A crib attack at N=180 would test nothing
    until more text in the same table exists.
- Where it was not found: no decipherment, key or "met het cijfer" note in Resolutiën XIII OR around either letter (above); no shared
  ordered sequence beyond one pair between the two texts.
- Next attack step (not started): more ciphertext in the same table first -- OBRED-S1's stride-1 screen of inv. 6016 orders 1-259 (live,
  account 2) and the 351-624 screen; then, if a third text appears, a run-length/crib consistency test of hypothesis 2 against its matched
  synthetic control, about $3 (Opus, disk only). Without more material, the crib test is a non-test at this N.

## OBRED-S1 (10 Oct 2026, 06:50-07:1x UTC by date -u, account 2, Sonnet)

Brief: stride-1 contact-sheet screen of the scans of NA 1.01.02 inv. 6016 image orders 1-259 that OBRED-0259 did not look at (not in `images/6016_screen_0001_0259.tsv`, not 186-188).

- Prior-work step: `prior_work.py ... --step-type read --fetch` exit 4 (3 LEAD = live claims of OBRED-0259, OBRED-187 and this job, 1 LOOK, 2 UNCHECKED, 2 UNCHECKED-NET); the six non-net rows recorded CLEAR in `prior-work.tsv` (no unit-keyed prior work on orders 1-259 beyond OBRED-0259/187); the two -NET rows (aaymeloglu cache, edition) stay with the folder's Premise check and OBRED-187 check 4. Check 5 not applicable (nothing decoded).
- Scope count: 259 - 87 sampled by OBRED-0259 - 186 and 188 = **170** scans (the brief's 173 counted 186-188 and 3 more); every order 1-259 is now either sampled, sheeted here, or one of 186-188 (read at native size by OBRED-187): `images/6016_screen_s1.tsv` (170 rows).
- Route: METS (1 request), then IIIF `/full/400,/0/default.jpg` for each of the 170 scans (2.1 s apart, descriptive User-Agent) and `/full/1200,/0/default.jpg` for five. service.archief.nl requests: **176** (1 METS, 170, 5), cap 180, all HTTP 200, no 403/429/challenge. NA take/release lines in ROOM.md.
- Method: 17 contact sheets (ten scans each) from `images/6016_screen_s1_sheetkey.json`; every sheet carries three disk controls placed by a seeded shuffle, tile letters not scan numbers (the key was opened only after a sheet's calls were noted): CTRL-CIPHER = inv. 2016 scan 31, CTRL-PLAIN = inv. 6016 order 261, CTRL-PS = scan 187 itself reduced to 400 px wide (no request; the Dutch three-digit postscript shape). One reader, this worker's own eye, no subagent. **Control calls: 17 of 17 sheets read the cipher control as figure-groups, the plain control as running prose and CTRL-PS as the dense numeral block under a signature (51/51), so no sheet is a non-test or re-sheeted.** Per-sheet notes: `images/6016_screen_s1_sheetcalls.txt`.
- Result: **no numeral-code page, key table or interlinear decipherment seen on any of the 170 scans.** Five scans re-looked at 1200 px because a sheet showed a small block, a signed letter or marginal numerals; all plain, Glossed: no, committed as `images/na_101_02_6016_p00NN_1200.jpg`:
  - 17: a German memorial (1602 by the leaf's head, M) naming Petrus Brederode as the States' agent in Germany, with an upside-down address slip; plain.
  - 111: a Dutch letter from Hanau dated 22 September 1603 (M), signed P. Brederode, two folded leaves, no numerals, right leaf blank; a Brederode letter in the same series as the Stettin one, plain.
  - 224: German treaty articles numbered 11-27 (the marginal numerals are article numbers); plain.
  - 225: French "Articles du traicte" for the ambassador in France (England/Spain), two columns; plain.
  - 227: a Latin address to a prince-bishop (Heinrich Julius of Brunswick, M) and French text on the left leaf; plain.
  Not re-looked: scans 230 and 231 (dark marginal-note blocks beside Latin text, read as clear-word marginalia on the sheet view).
- Where it was not found, and the limits: no second numeral postscript in 1-259 beyond scan 187 at this resolution; 400 px sheets show a numeral run of the controls' density, and a block of a dozen groups or fewer inside prose could escape (the CTRL-PS block is about 59 groups); one reader; the cipher control is a French letter of 1598 and the postscript control is the target's own scan, so the postscript shape is covered but a table or key slip of another shape is covered only by the French control; orders 351-624 remain at stride 3 (OBRED-6016). Not a negative for the series elsewhere; a negative for these 170 scans at this resolution.

## OBRED-S2 (10 Oct 2026, 07:3x-07:5x UTC by date -u, account 2, Sonnet)

Brief: stride-1 contact-sheet screen of the scans of NA 1.01.02 inv. 6016 image orders 351-624 that OBRED-6016 did not look at (not in `images/6016_screen.tsv`), then a table of inv. 6017-6024 and the 1605 Swiss-mission dossier (no image fetches).

- Prior-work step: `prior_work.py ... --step-type read --fetch` exit 4 (4 LEAD = live claims of OBRED-0259, OBRED-187, OBRED-S1 and this job; 1 LOOK; 2 UNCHECKED; 2 UNCHECKED-NET); the seven non-net rows recorded CLEAR in `prior-work.tsv` (no unit-keyed prior work on 351-624 beyond OBRED-6016's stride-3 look); the two -NET rows stay with the Premise check. Check 5 not applicable (nothing decoded).
- Scope count: 274 scans in 351-624 - 92 sampled by OBRED-6016 = **182** scans (the brief's count), all sheeted: `images/6016_screen_s2.tsv` (182 rows).
- Route: METS (1 request), then IIIF `/full/400,/0/default.jpg` for each of the 182 scans (2.1 s apart, descriptive User-Agent, all HTTP 200) and `/full/1200,/0/default.jpg` for six. NA requests for the scan screen: **190** (1 METS, 1 stray HEAD on a file URL, 182 at 400 px, 6 at 1200 px), at the cap, no 403/429/challenge. NA take/release lines in ROOM.md.
- Method: 19 contact sheets (ten scans each, the 19th has two) from `images/6016_screen_s2_sheetkey.json`; every sheet carries three disk controls placed by a seeded shuffle, tile letters not scan numbers (the key was opened only after all 19 sheets' calls were written, `images/6016_screen_s2_sheetcalls.txt`): CTRL-CIPHER = inv. 2016 scan 31, CTRL-PLAIN = inv. 6016 order 261 (the 1605-1606 folder cover), CTRL-PS = scan 187 reduced to 400 px wide (no request; the Dutch three-digit postscript shape). One reader, this worker's own eye, no subagent. **Control calls: 19 of 19 sheets read the cipher control as figure-groups, the plain control as the folder cover and CTRL-PS as the dense numeral block under a signature (57/57), so no sheet is a non-test or re-sheeted.**
- Result: **no numeral-code page, key table or interlinear decipherment seen on any of the 182 scans.** Six scans re-looked at 1200 px because a sheet showed a marginal column, a short list, or a small pasted slip; all plain, Glossed: no, committed as `images/na_101_02_6016_p0NNN_1200.jpg`:
  - 391: a Dutch letter signed P. Brederode, "Vanden deses 5. Novemb[er]" (year not read here, M), plain prose, no numerals.
  - 494: a German letter to the States General dated 15 April 1610 (M) with an upside-down address slip; plain.
  - 505 and 506: the same German letter of Wolfgang Wilhelm of Pfalz-Neuburg and Ernst of Brandenburg dated 5 January 1611 (M), with two small pasted slips in a clear hand (one dated January 1611); plain, no numerals.
  - 550: a list of presents for the Sultan ("Verzeichnis ...", Constantinople 7 May 1612, M) beside a Latin address leaf; plain, the numerals are item counts.
  - 622: a Dutch slip dated 7 September 16[1x] (M) with "Brederode" in the margin, two struck lines; plain.
  Year dividers seen at scans 448 (1610), 514 (1612) and 539 (1613); printed (Fraktur) leaves on sheet 9.
- Where it was not found, and the limits: no numeral block, key or gloss in 351-624 at this resolution; with OBRED-S1 and OBRED-0259, every scan of inv. 6016 orders 1-259 and 351-624 has now been looked at once and orders 260-350 were read leaf by leaf by YX-OBR (25 Sept 2026), so no third numeral text of the no. 92 / scan-187 shape was seen anywhere in inv. 6016. 400 px sheets show a numeral run of the controls' density; a block of a dozen groups or fewer inside prose, or text in a printed or pasted slip too small at 400 px, could escape; one reader; the cipher control is a French letter and the postscript control is the target's own scan. Not a negative for the series elsewhere; a negative for these 182 scans at this resolution.
- Table `nl_brederode_lias.tsv` (NA requests 11: the 1.01.02 EAD xml once, item pages 6017 twice by a script slip, 6018-6024, 12569.38; all HTTP 200): inv. 6016-6024 ("Liassen Agent Brederode", 1602-1637) are all digitised, each with a METS id in the EAD (`dao`) and a `viewer.response` scan count from the item page's drupal-settings-json: 6016 624 (read earlier), 6017 (1614-1617) 585, 6018 (1618) 577, 6019 (1619) 649, 6020 (1620) 604, 6021 (1621-1622) 810, 6022 (1623-1626) 595, 6023 (1627-1631) 536, 6024 (1632-1637) 470, 4,826 scans in 6017-6024, all later than the 1605 letter and not looked at. The 1605 Swiss-mission dossier is invnr 12569.38 in the same EAD ("1 omslag", 1605 with retroacta 1587-1604): its item page answers 200 but the viewer carries 0 scans and the EAD record has no `dao`, so **not digitised** (catalogue and item page, 10 Oct 2026); physical access only.

## OBRED-S3 (10 Oct 2026, 08:11-08:3x UTC by date -u, account 2, Sonnet)

Brief: stride-3 contact-sheet screen of NA 1.01.02 inv. 6017 (1614-1617, 585 scans), scans 1, 4, ..., 583 (195 scans), same method and three controls as OBRED-S1/S2.

- Prior-work step: `prior_work.py ... --step-type read --fetch` exit 4 (5 LEAD = live claims of OBRED-0259, OBRED-187, OBRED-S1, OBRED-S2 and this job, all target-level and none covering inv. 6017; 1 LOOK; 2 UNCHECKED; 2 UNCHECKED-NET); the eight non-net rows recorded CLEAR in `prior-work.tsv`; the two -NET rows stay with the Premise check. Check 5 not applicable (nothing decoded).
- Route: METS `b060ccbc-...` from `nl_brederode_lias.tsv` (1 request, 585 scans), then IIIF `/full/400,/0/default.jpg` for 195 scans (2.1 s apart, descriptive User-Agent; scan 1 doubled as the URL test) and `/full/1200,/0/default.jpg` for five. service.archief.nl requests: **201** (1 METS, 195, 5), cap 205, all HTTP 200, no 403/429/challenge. NA take/release lines in ROOM.md.
- Method: 20 contact sheets (ten scans each, the 20th five) from `images/6017_screen_sheetkey.json`; each carries three disk controls placed by a seeded shuffle, tile letters not scan numbers (the key was opened only after all 20 sheets' calls were written, `images/6017_screen_sheetcalls.txt`): CTRL-CIPHER = inv. 2016 scan 31, CTRL-PLAIN = inv. 6016 order 261, CTRL-PS = scan 187 at 400 px (no request). One reader, this worker's own eye, no subagent. **Control calls: 20 of 20 sheets read the cipher control as figure-groups, the plain control as the folder cover and CTRL-PS as the dense numeral block under a signature (60/60; checked mechanically against the key), so no sheet is a non-test or re-sheeted.**
- Result: **no numeral-code page, key table or interlinear decipherment seen on any of the 195 scans (every third scan of 1-583); no numeral hit, so no value list and no transcription or overlap test is called for.** `images/6017_screen.tsv` (195 rows). Five scans re-looked at 1200 px (a sheet showed a numbered list, a slip, a short column of marks); all plain, Glossed: no, committed as `images/na_101_02_6017_p0NNN_1200.jpg`:
  - 571: Latin articles of a knightly order (rules numbered 1-6 and 1-4, ordinal words in the margin); the numerals are article numbers.
  - 574: a Dutch draft with struck lines and marginal notes, dated February 1617 (M).
  - 580: a leaf with show-through text, an address-like short list and a pasted slip; no numerals.
  - 478 and 472: the same Dutch letter from Heidelberg dated 15 September 1617 (M), signed Brederode, its short show-through list is verso text; plain.
  Year dividers seen at scans 1 (1614) and 82 (1615); scan 340 a blank cover. Latin pages on sheet 13.
- Where it was not found, and the limits: **every third scan only** -- 390 of the 585 scans of inv. 6017 were not looked at, and inv. 6018-6024 (4,241 scans) not at all; a numeral postscript of one leaf could fall in an unlooked scan (a one-leaf item is a third as likely to be sampled as a run of three). 400 px sheets show a numeral run of the controls' density; a block of a dozen groups or fewer inside prose could escape; one reader; the cipher control is a French letter of 1598 and the postscript control is the target's own scan. Not a negative for the series elsewhere; a negative for these 195 scans at this resolution.

## OBRED-SG (10 Oct 2026, 09:22-09:3x UTC by date -u, account 2, Sonnet)

Brief: Den Tex retry, then the States-side trace of the 17 Oct 1604 letter in NA 1.01.02. Nothing decoded; no gate computed.

- Prior-work step: `prior_work.py ... --step-type read --fetch` exit 4: 6 LEAD (target-level live claims of earlier A2o workers and this one, none naming S.G. 5888/5968 or inv. 11851), 1 LOOK, 2 UNCHECKED, 2 UNCHECKED-NET; none covers this item. Check 1 (own): Den Tex was already read once on 25 Sept 2026 (section 6 above) but the abridged Den Tex/Ton edition only and without `cijfer`, `Stettin` or page refs; the Escalation line "retry not run" was stale. Checks 2-4 not run beyond that (no decode; checks owed stay UNCHECKED). Check 5 not applicable.
- **Den Tex (dbnl.org, 2 requests incl. none failed; 1 PDF GET, HTTP 200, 307 pages, 3.5 MB):** per-page grep of `Brederode|cijfer|chiffre|Stettin|sleutel|geheimschrift`: PDF p.126 (Pieter Corneliszn. Brederode, contacts with Bongars), p.136, p.148 (Brederode as Oldenbarnevelt's agent), p.134 (Reinoud van Brederode, a different man), index p.294 (printed pp. 131, 141, 153); `cijfer` once, p.68, a troop quota ("ver beneden het cijfer ... Nonesuch"), unrelated; `Stettin`, `sleutel`, `chiffre`, `geheimschrift` 0. Not found: any cipher, key or 1604-1605 Stettin letter note. Limit: the abridged one-volume edition only, not the 5-volume original.
- **NA 1.01.02 EAD** (1 request, 22.7 MB, scratch only): the footnote number "R.A., S.G. 5888 / 5968" of the Resolutien does **not** equal the current inventory numbers (5888 = Liassen Engelandt 1621-1624; 5968 = 1749-1750), so those citations cannot be followed directly. Table `images/sg_inventory.tsv`. The series where an incoming German-sent letter of Oct 1604 would sit, **Liassen Hoogduytschlandt inv. 6034 (1604) and 6035 (1605)**, and Liassen Loopende 4909/4910, have **no dao in the EAD: not digitised** (catalogue, 10 Oct 2026; item pages not separately fetched); physical access only. Digitised and relevant by date: inv. 11851 (Brievenboeken, registers of incoming ordinaris letters, 1604, 733 scans, METS 69557eee-2aae-4284-98ff-db14579daf50) and 11852 (1605, 522 scans), plus the minuut-resolutie registers 30/31.
- **Inv. 11851 screen** (`images/sg_11851_screen.tsv`): the register copies letters in full, chronologically (scan 100 = p.96, 9 June 1604; 300 = p.295, June; 560 = Sept; 620 = about 23-26 Oct; 680 = Dec 1604). 45 scans (596-640) fetched at 700 px; two six-tile sheets viewed (608-613, 626-631, committed): domestic letters (Holland, Zeeland, Utrecht, dike matters, exhibitum 28 Oct and 2 Nov 1604), no Brederode or German entry, no numeral block other than money sums. **Not done:** the other 33 fetched scans were not viewed; this was a no-control look (no CTRL-CIPHER / CTRL-PS tiles on the sheets, unlike OBRED-S1..S3), so it is a layout and content probe, not a numeral screen with a control, and licenses no negative. 11852 not looked at. NA requests: 1 EAD + 2 METS + 9 probes + 45 = 57; no 403/429.
- Where it was not found: no Brederode or Stettin entry in the 12 views read; the Hoogduytschlandt liassen are the likely home and are not on line.


## Remaining gaps (OBRED-DP, 10 Oct 2026)
Read so far: unmeasured; nothing decoded -- no. 92 (121 groups) and the scan-187 postscript (59 groups, transcribed this pass) are both unread; they share 26 values, above chance (OBRED-187)
- no. 92 and the 187 postscript, pooled (180 tokens, 130 distinct values) - blocker: too-short; OBRED-DP: name band 588-751 stands alone (G2 PASS), the spelled lower table has 146 tokens over 113 distinct values and no shared order beyond one pair (G1 FAIL), so a crib test is unfalsifiable at this N; more text in the same table is the step (the 6016 screens below)
- the later liassen NA 1.01.02 inv. 6017-6024 (1614-1637, 4,826 scans, all digitised, METS ids in `nl_brederode_lias.tsv`) - blocker: not-attempted beyond a stride-3 look; all of inv. 6016 is looked at (OBRED-0259, OBRED-S1, OBRED-S2, YX-OBR: no third numeral block) and every third scan of 6017 (OBRED-S3, 195 scans, controls 60/60: no numeral block); next: the other 390 scans of 6017 at stride 1 (~390 requests, ~$3), only if a later cipher use by the agent in 1614-1617 is worth testing
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2: item page 0 scans, EAD no dao); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 letter (OBRED-SG, 10 Oct 2026) - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035 and Loopende 4909/4910 not digitised; footnote numbers 5888/5968 are old numbering); digitised remainder: brievenboek inv. 11851 scans 596-640 (13 of 45 viewed, domestic letters) and 11852 (1605, 522 scans) not viewed; next: view the other 32 fetched sheets-worth of 11851 and a Brederode-heading look at 11852 Jan-Jun 1605, ~$1.5, no control

## Escalation (OBRED-DP, 10 Oct 2026)
- [x] siblings: scan 187 is a second code text sharing 26 values with no. 92 (OBRED-187); the stride-1 screen of orders 1-259 (OBRED-S1, 170 scans, controls 51/51) found no third numeral block; orders 351-624 are now stride 1 too (OBRED-S2, 182 scans, controls 57/57: no numeral block); the whole of 6016 is looked at
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187: Stettin, 17 Oct 1604, to the griffier of the States General, on the Brandenburg negotiation); it carries no gloss of the code
- [x] known-keys: the 10 Aug 1598 Van Aerssen slip excluded for no. 92 by design (R10-OBRED98); Buzanval syllabary inv. 2028 excluded (R9-OBRED4); DECODE 1600s and Palatine/Hessian keys screened (OLD-DKEY, R8-OBRED2, R9-OBRED3); the 187 values fall in the same 1-751 range as no. 92 and add no key
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187, nos. 89 -> 90); Resolutiën S.G. XIII OR has no decipherment, key or "met het cijfer" note near the Oct 1604 or Feb 1605 Brederode entries (OBRED-DP)
- [ ] key-rebuild: design_prior and structure done (OBRED-DP: multi-sign class nearest, name band 588-751 PASS, shared order FAIL); a crib/run-length test of the letter-homophonic hypothesis waits on a third text, and none was found in inv. 6016 (OBRED-S2); next: a third text from the 6017 screen above or a States-side find, then the crib consistency test with a synthetic matched control, ~$3
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv is two blind passes agreeing 59/59 on native crops (OBRED-187)
- [x] retry: Den Tex (abridged Den Tex/Ton, dbnl.org) read twice now (25 Sept; OBRED-SG 10 Oct 2026, PDF pp. 68, 126, 134, 136, 148): no cipher, key or Stettin note; the 5-volume original not reached
Verdict: keep going: 1 internal gap; cheapest next: viewing the rest of the 11851 scans (OBRED-SG, ~$1.5) or the stride-1 fill of the other 390 scans of inv. 6017 (~$3); all of inv. 6016 is now looked at and found no third numeral block (OBRED-S1, OBRED-S2)

## OBRED-11851 (11 Oct 2026, 19:22-19:3x UTC by date -u, account 1, Opus; for LANE DEFAULT-A1-1840)

Brief: the rest of NA 1.01.02 inv. 11851 (brievenboek, incoming ordinaris letters, 1604) scans 596-640 that OBRED-SG did not view, as a
numeral screen with controls; then the stride-1 fill of inv. 6017 from where OBRED-S3 stopped, within the request cap. Nothing decoded;
no gate computed.

- Prior-work step: `prior_work.py oldenbarnevelt-brederode-1605 --item-spec 'NL-HaNA 1.01.02 inv. 11851 scans 596-640' --step-type read
  --fetch` exit 4: 1 LEAD (this job's own claim), 1 LOOK (target-level crop, not an 11851 leaf), 2 UNCHECKED (solver caches by unit,
  Tomokiyo), 2 UNCHECKED-NET (aaymeloglu cache, editions); the four non-net rows recorded CLEAR in `prior-work.tsv` (only earlier
  unit-keyed work on 11851 is OBRED-SG). Checks 2-4 by hand: not applicable beyond the folder's Premise check (a States-side register
  screen, no reading); check 5 not applicable (nothing decoded).
- Scope: OBRED-SG fetched 45 scans (596-640) and viewed 12 (608-613, 626-631; the brief's "13" counted one more), so **33** were
  unviewed: 596-607, 614-625, 632-640. All 33 looked at here.
- Route: METS `69557eee-2aae-4284-98ff-db14579daf50` (1 request, 733 scans), IIIF `/full/700,/0/default.jpg` per scan (2.1 s apart,
  descriptive User-Agent; `screen_tools/na_fetch.py`). Contact sheets: `screen_tools/contact_sheets.py`, six scans + the three disk
  controls of OBRED-S1..S3 per 3x3 sheet (CTRL-CIPHER = inv. 2016 scan 31, CTRL-PLAIN = inv. 6016 order 261, CTRL-PS = scan 187 at
  1200 px; no request), seeded shuffle (seed 11851), tile letters only; all calls written to
  `images/sg_11851_screen2_sheetcalls.txt` before the key (`images/sg_11851_screen2_sheetkey.json`) was opened. One reader, this
  worker's own eye, no subagent. Sheets themselves stay in scratch (folder at 27 of 30 MB); they regenerate from the two scripts and
  the key.
- **Controls: 18 of 18 placed correctly (6 sheets x 3), so no sheet is a non-test.**
- **Result, inv. 11851 scans 596-640: no numeral-code block, key table or interlinear decipherment on any of the 33 scans**
  (`images/sg_11851_screen2.tsv`, 33 rows). The pages (printed register pp. about 590-635) are clerk's fair copies of incoming letters of
  late October to early November 1604 (Missive headings in the left margin, exhibitum dates 23-28 Oct and Nov 1604): Holland, Zeeland,
  Utrecht, Stad en Lande, Commissaris and Raad van State letters, dike (Sonnewijk) matters. Numerals seen are money columns (scans
  597-603, 620s), morgen sums (633, and a "Bylage" area list), and counts of guns ("Stucken", 623); none is a code-group run. **No
  Brederode or German-sent entry seen in 596-640** at this resolution (a heading read at 700 px; a Brederode name inside a long entry
  could escape). With OBRED-SG's 12, all 45 scans of 596-640 are now looked at once.
- Lead, not a finding (M): the 17 Oct 1604 Stettin letter (OBRED-187) would be registered by its exhibitum date; a letter from Pomerania
  took two to four weeks, so its register copy, if the clerk entered it here at all, would fall in early-to-mid November 1604, i.e. after
  scan 640 (scan 680 = Dec 1604 per OBRED-SG), not in 596-640.
- **Inv. 6017 stride-1 fill:** METS `b060ccbc-a7f8-4174-a34f-c25e5ff9e526` (1 request), then 24 scans at 700 px: the scans between
  OBRED-S3's stride-3 samples from 2 to 36 (2, 3, 5, 6, ..., 35, 36). Same sheet method, seed 6017, calls before key
  (`images/6017_screen_s4_sheetcalls.txt`, key `images/6017_screen_s4_sheetkey.json`). **Controls 12 of 12.** **No numeral-code block on
  any of the 24** (`images/6017_screen_s4.tsv`): Dutch and German letters of 1614, several signed P. Brederode from Heidelberg (scans 21,
  24, 32, 36), address leaves with seals, blank openings (5, 29, 33). One region look: scan 14, a letter signed "Pieter van Brederode
  Doctor" dated 29 March (year not read, M) with a short postscript block beside the signature, fetched at 1400 px
  (`pct:0,50,75,30`, committed as `images/na_101_02_6017_p0014_ps_1400.jpg`): the postscript is clear Dutch ("Syne G. es ... op
  manendach naest komende ... Hanau"), not figures.
- Requests: `service.archief.nl` **60** (2 METS, 57 scans at 700 px, 1 region at 1400 px), all HTTP 200, no 403/429/challenge; cap 60.
  NA take/release lines in ROOM.md.
- Where it was not found, and the limits: no numeral block in 11851 596-640 or 6017 scans 2-36 (stride-1 part) at 700 px; a block of a
  dozen groups or fewer inside prose could escape; one reader; the controls are a French cipher letter and the target's own postscript,
  so a table of another shape is covered only by the French control. 11851 scans 641-733 and all of 11852 were not looked at; 6017 has
  366 scans still unlooked (390 minus these 24). Not a negative for the registers or the series elsewhere.

## Remaining gaps (OBRED-11851, 11 Oct 2026)
Read so far: unmeasured; nothing decoded -- no. 92 (121 groups) and the scan-187 postscript (59 groups) are both unread; they share 26 values, above chance (OBRED-187)
- no. 92 and the 187 postscript, pooled (180 tokens, 130 distinct values) - blocker: too-short; OBRED-DP: name band 588-751 stands alone (G2 PASS), shared order beyond one pair absent (G1 FAIL), so a crib test is unfalsifiable at this N; more text in the same table is the step
- the later liassen NA 1.01.02 inv. 6017-6024 (1614-1637, 4,826 scans, all digitised) - blocker: not-attempted beyond a stride-3 look of 6017 plus the stride-1 fill of scans 2-36 (OBRED-11851, controls 12/12, no numeral block); the agent's later letters are screened only in part; next: the other 366 unlooked scans of 6017 at stride 1 (~370 requests over several NA sessions, ~$3), only if a later cipher use by the agent in 1614-1617 is worth testing
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 letter - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder: brievenboek inv. 11851 scans 596-640 now all looked at (OBRED-SG 12, OBRED-11851 33 with controls 18/18: no numeral block, no Brederode entry); next: 11851 scans 641-700 (Nov-Dec 1604, where a 17 Oct Stettin letter would be registered by exhibitum date), ~60 requests, ~$3, then a Brederode-heading look at 11852 Jan-Jun 1605

## Escalation (OBRED-11851, 11 Oct 2026)
- [x] siblings: scan 187 is a second code text sharing 26 values with no. 92 (OBRED-187); all of inv. 6016 looked at (OBRED-0259, OBRED-S1, OBRED-S2, YX-OBR): no third numeral block; 6017 stride 3 (OBRED-S3) plus scans 2-36 at stride 1 (OBRED-11851): none
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187: Stettin, 17 Oct 1604, to the griffier of the States General); it carries no gloss of the code
- [x] known-keys: the 10 Aug 1598 Van Aerssen slip excluded for no. 92 by design (R10-OBRED98); Buzanval syllabary inv. 2028 excluded (R9-OBRED4); DECODE 1600s and Palatine/Hessian keys screened (OLD-DKEY, R8-OBRED2, R9-OBRED3)
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII has no decipherment or key note near the Brederode entries (OBRED-DP)
- [ ] key-rebuild: design_prior and structure done (OBRED-DP); a crib/run-length test waits on a third text in the same table, none found in 6016, 6017 (part) or 11851 596-640; next: a third text from 11851 641-700 or the 6017 fill, then the crib consistency test with a synthetic matched control, ~$3
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv two blind passes agreeing 59/59 (OBRED-187)
- [x] retry: Den Tex (abridged edition) read twice (25 Sept; OBRED-SG 10 Oct 2026): no cipher, key or Stettin note; brievenboek 11851 596-640 completed with controls (OBRED-11851)
Verdict: keep going: 1 internal gap; cheapest next: inv. 11851 scans 641-700 (Nov-Dec 1604, the exhibitum window of the 17 Oct 1604 Stettin letter), ~60 NA requests, ~$3, with the same three controls; then the 6017 stride-1 fill (366 scans left)

## OBRED-641 (11 Oct 2026, 19:52-20:0x UTC by date -u, account 1, Opus; for LANE DEFAULT-A1-1840)

Brief: NA 1.01.02 inv. 11851 (brievenboek 1604) scans 641-700, the Nov-Dec 1604 exhibitum window of the 17 Oct 1604 Stettin letter,
with the three controls of OBRED-S1..S3; then the inv. 6017 stride-1 fill from scan 37. Nothing decoded; no gate computed.

- Prior-work step: `prior_work.py oldenbarnevelt-brederode-1605 --item-spec 'NL-HaNA 1.01.02 inv. 11851 scans 641-700' --step-type read
  --fetch` exit 4: 1 LEAD (this job's own claim), 1 LOOK (target-level crop, not a register scan), 2 UNCHECKED (solver caches by unit,
  Tomokiyo), 2 UNCHECKED-NET (aaymeloglu cache, editions); the four non-net rows recorded CLEAR in `prior-work.tsv` (earlier unit-keyed
  work on 11851 is OBRED-SG and OBRED-11851, scans 596-640 only). Checks 2-4 not applicable beyond the folder's Premise check (a register
  screen, no reading); check 5 not applicable.
- Route: METS `69557eee-...` (1 request), IIIF `/full/700,/0/default.jpg` for scans 641-700 (60 requests, 2.1 s apart, descriptive
  User-Agent, `screen_tools/na_fetch.py`); 10 sheets by `screen_tools/contact_sheets.py`, seed 641, six scans + CTRL-CIPHER (inv. 2016
  scan 31), CTRL-PLAIN (inv. 6016 order 261), CTRL-PS (scan 187 at 1200 px) each, tile letters only; all calls written to
  `images/sg_11851_screen3_sheetcalls.txt` before the key (`images/sg_11851_screen3_sheetkey.json`) was opened. One reader, this
  worker's own eye, no subagent. Sheets in scratch (they regenerate from the two scripts and the key).
- **Controls: 30 of 30 placed correctly (10 sheets x 3), checked mechanically against the key; no sheet is a non-test.**
- **Result, inv. 11851 scans 641-700: no numeral-code block, key table or interlinear decipherment on any of the 60 scans**
  (`images/sg_11851_screen3.tsv`, 60 rows). Content (printed register pp. about 641-695): clerk's fair copies of incoming letters with
  exhibitum dates from about 15 November to late December 1604 (Gedeputeerden, Raad van State, Maurice of Nassau, Johan Sluys, the
  Oostindische Compagnie); goods lists with prices (scans in sheets 1-2, 6); munition lists ("Lyste van Ammunitien van Oorlogh", Sluys,
  Novem-Decem 1604) whose quantity columns are Roman-numeral counts against named stores -- the nearest look-alike to figure groups at
  sheet size, but item counts, not a code run (sheets 7-8); a Bergen op Zoom garrison/works pay account of 1596-1603 with guilder sums
  (sheets 9-10). **No Brederode, Stettin or German-sent entry seen in 641-700 at heading level** (margin headings read at 700 px; a name
  inside a long entry could escape).
- The OBRED-11851 lead (register copy, if any, in early-to-mid November 1604) is not borne out in 641-700 at this resolution: the 17 Oct
  1604 Stettin letter was not seen registered in 11851 596-700 (about 23 Oct to late Dec 1604). Where it was not found: these 105
  scans; the originals (Liassen Hoogduytschlandt inv. 6034) are not digitised.
- **Inv. 6017 stride-1 fill, scans 38-72** (the 24 not sampled by OBRED-S3's stride 3; 37 was already looked at): METS (1 request) + 24
  scans at 700 px; 4 sheets, seed 6017, same controls, calls before key (`images/6017_screen_s5_sheetcalls.txt`, key
  `images/6017_screen_s5_sheetkey.json`). **Controls 12 of 12.** **No numeral-code block on any of the 24** (`images/6017_screen_s5.tsv`):
  Dutch and German letters of May-September 1614, several signed P. Brederode, address slips, blank openings. No region look needed.
- Requests: `service.archief.nl` **86** (2 METS, 84 scans at 700 px), all HTTP 200, no 403/429/challenge -- over the brief's 70: the
  brief's 70 was read as the 11851 part (61) and the 6017 fill (25) was added without re-checking the total; noted here, not hidden.
  NA take/release lines in ROOM.md.
- Limits: 700 px sheets; a block of a dozen groups or fewer inside prose could escape; one reader; the controls are a French cipher
  letter and the target's own postscript. 11851 scans 701-733 and all of 11852 not looked at; 6017 has 342 scans unlooked (366 minus
  these 24; next start scan 73). Not a negative for the registers or the series elsewhere.

## Remaining gaps (OBRED-641, 11 Oct 2026)
Read so far: unmeasured; nothing decoded -- no. 92 (121 groups) and the scan-187 postscript (59 groups) are both unread; they share 26 values, above chance (OBRED-187)
- no. 92 and the 187 postscript, pooled (180 tokens, 130 distinct values) - blocker: too-short; OBRED-DP: name band 588-751 stands alone (G2 PASS), shared order beyond one pair absent (G1 FAIL), so a crib test is unfalsifiable at this N; more text in the same table is the step
- the later liassen NA 1.01.02 inv. 6017-6024 (1614-1637, 4,826 scans, all digitised) - blocker: not-attempted; only a stride-3 look of 6017 plus the stride-1 fill of scans 2-36 (OBRED-11851) and 38-72 (OBRED-641, controls 12/12, no numeral block); next: the other 342 unlooked scans of 6017 at stride 1 from scan 73 (~350 requests over several NA sessions, ~$3), only if a later cipher use by the agent in 1614-1617 is worth testing
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 letter - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder: brievenboek inv. 11851 scans 596-700 now all looked at with controls (OBRED-SG, OBRED-11851, OBRED-641 30/30: no numeral block, no Brederode or Stettin entry, exhibitum dates to late Dec 1604); next: 11851 scans 701-733 (end of 1604) and a Brederode-heading look at 11852 Jan-Mar 1605 (~90 requests, ~$3), a low-yield step since no register copy was seen in the window where one was expected

## Escalation (OBRED-641, 11 Oct 2026)
- [x] siblings: scan 187 is a second code text sharing 26 values with no. 92 (OBRED-187); all of inv. 6016 looked at (OBRED-0259, OBRED-S1, OBRED-S2, YX-OBR): no third numeral block; 6017 stride 3 (OBRED-S3) plus scans 2-36 and 38-72 at stride 1 (OBRED-11851, OBRED-641): none
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187: Stettin, 17 Oct 1604, to the griffier of the States General); it carries no gloss of the code
- [x] known-keys: the 10 Aug 1598 Van Aerssen slip excluded for no. 92 by design (R10-OBRED98); Buzanval syllabary inv. 2028 excluded (R9-OBRED4); DECODE 1600s and Palatine/Hessian keys screened (OLD-DKEY, R8-OBRED2, R9-OBRED3)
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII has no decipherment or key note near the Brederode entries (OBRED-DP)
- [ ] key-rebuild: design_prior and structure done (OBRED-DP); a crib/run-length test waits on a third text in the same table, none found in 6016, 6017 (part) or 11851 596-700; next: a third text from the 6017 fill or 11851 701-733 / 11852, then the crib consistency test with a synthetic matched control, ~$3
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv two blind passes agreeing 59/59 (OBRED-187)
- [x] retry: Den Tex (abridged edition) read twice (25 Sept; OBRED-SG 10 Oct 2026): no cipher, key or Stettin note; brievenboek 11851 596-700 completed with controls (OBRED-11851, OBRED-641)
Verdict: keep going: 1 internal gap; cheapest next: the 6017 stride-1 fill from scan 73 (342 scans left, ~$3 per ~60-90 scans with controls) or 11851 701-733 plus 11852 Jan-Mar 1605 (~90 requests, ~$3); the Nov-Dec 1604 exhibitum window of 11851 showed no register copy of the Stettin letter (OBRED-641)

## OBRED-11851B (13 Oct 2026, 21:49-22:0x UTC by date -u, account 4, Opus; for LANE DEFAULT-A4-2135)

Brief: the States-side trace step OBRED-641 named: NA 1.01.02 inv. 11851 (brievenboek 1604) scans 701-733 (end of 1604), and a
Brederode-heading look at inv. 11852 (1605) for January-March 1605. Route, sizes and controls are OBRED-641's. Nothing decoded; no gate
computed. (Called OBRED-11851B here so it is not confused with the 11 Oct OBRED-11851 section above.)

- Prior-work step: `prior_work.py oldenbarnevelt-brederode-1605 --item-spec 'NL-HaNA 1.01.02 inv. 11851 scans 701-733; inv. 11852
  Jan-Mar 1605' --step-type read --fetch` exit 4: 1 LEAD (this job's own claim), 1 LOOK (target-level crop, not a register scan), 2
  UNCHECKED (solver caches by unit, Tomokiyo), 2 UNCHECKED-NET (aaymeloglu cache, editions). The four non-net rows were recorded CLEAR in
  `prior-work.tsv` (the only earlier unit-keyed work on 11851 is OBRED-SG, OBRED-11851 and OBRED-641, scans 596-700; 11852 was never
  viewed). Checks 2-4 do not apply beyond the folder's Premise check, because this is a register screen and reads nothing. Check 5 does
  not apply.
- Route: 11851 by METS `69557eee-...` (1 request) and `screen_tools/na_fetch.py`, scans 701-733 at `/full/700,/0/default.jpg`. 11852
  had no METS id on record. One item-page request
  (`www.nationaalarchief.nl/onderzoeken/archief/1.01.02/invnr/11852`) gave the embedded scan list: 522 scans, each with its IIIF base.
  The bases used are in `screen_tools/na_11852_iiif_map.json`, and `screen_tools/na_fetch_map.py` fetches from that map. Requests were
  2.1 s apart, with a descriptive User-Agent.
- Locating Jan-Mar 1605 in 11852: five probe scans (1, 40, 80, 120, 160) were read by eye. Scan 1 is the cover. Scan 40 is printed p.35,
  with entries dated about 26 Feb 1605. Scan 80 is p.74, Nijmegen 3 March 1605. Scan 120 is p.114, late April 1605. Scan 160 is p.155,
  May 1605. **The register's run starts in late February, so January to mid-February 1605 sits in scans 2-39.** Within the request cap I
  took scans 50-104, the arrival window of the 21 Feb 1605 Heidelberg letter (no. 92). These run from about 24 Feb to about 6 April 1605
  by exhibitum. **Scans 2-49 (Jan to about 23 Feb 1605) were not screened.** Scan 40 was seen only as a probe tile, with no control.
- Contact sheets: `screen_tools/contact_sheets.py`, 3x3 sheets of six scans plus the three disk controls of OBRED-S1..S3 per sheet
  (CTRL-CIPHER = inv. 2016 scan 31, CTRL-PLAIN = inv. 6016 order 261, CTRL-PS = scan 187 at 1200 px). Seeds were 11852 (11851 sheets) and
  1605 (11852 sheets), with tile letters only. Every call was written to `images/sg_11851_screen4_sheetcalls.txt` and
  `images/sg_11852_screen1_sheetcalls.txt` before the keys (`images/*_sheetkey.json`) were opened. There was one reader, this worker's own
  eye, and no subagent. The sheets stay outside git. `screen_tools/regen_11851b.sh` re-derives the scans and sheets, and key1 was
  re-derived byte-identical from the same seed.
- **Controls: 18 of 18 (6 sheets of 11851) and 30 of 30 (10 sheets of 11852) were placed correctly, checked mechanically against the
  keys. No sheet is a non-test.**
- **Result, inv. 11851 scans 701-733** (`images/sg_11851_screen4.tsv`, 33 rows): **no numeral-code block, key table or interlinear
  decipherment.** Printed pp. about 696-723:
  - pp. 696-713 are fair copies of letters with exhibitum dates 22-30 Dec 1604, from the Gedeputeerden of Drenthe, the Staten van
    Zeelandt, the Commissarissen at Sluys, the Magistraet of Nijmegen and the Raad van State. Some of these letters are **dated October
    1604 but entered with exhibitum 30 Dec 1604** (pp. 712-713: "dat 23 Octob 1604 ... ex 30 decem"), so the clerk did enter some letters
    weeks after their date.
  - pp. 714-722 are a goods list of July-September 1604 (cloth packs, Amsterdam), with money columns.
  - p. 723 is a French entry.
  - The volume then ends in blank endleaves and the back cover.
  - **No Brederode, Stettin or German-sent heading was seen.** Headings were read at 700 px, so a name inside a long entry could escape.
- **Result, inv. 11852 scans 50-104** (`images/sg_11852_screen1.tsv`, 55 rows): **no numeral-code block, key table or interlinear
  decipherment.** Printed pp. about 45-98, exhibitum about 24 Feb to about 6 April 1605. The register mixes incoming missives (Raad van
  Brabant, Ridderschap of Nijmegen and of Zutphen, the Admiralty of Zeeland, Commissarissen Bomberg and Coren at Middelburg and
  Vlissingen, Willem Lodewijk of Nassau at Leeuwarden, Raad van State, the Magistraet of Emden) with States General acts and octrooien of
  26 Feb, 6 March and 25-31 March 1605. Figures seen are:
  - company and regiment lists with counts (pp. 45-46, 59, 66)
  - money accounts (pp. 60-65)
  - an ammunition list (p. 89)
  - tariff lists (pp. 93-95)

  None of these is a code-group run. Two French or foreign-sent entries were looked at closely at sheet size: p. 80, a letter about an
  Englishman Thomas Wright, apparently from Cleves, and p. 98, "Messeigneurs", 6 April 1605. **Neither carries a Brederode, Heidelberg or
  Stettin heading.** **No Brederode, Heidelberg or Palatine heading was seen in scans 50-104.** The page numbers in the TSV are read at
  700 px and some are approximate (marked "?").
- Where the Stettin and Heidelberg letters were not found: inv. 11851 scans 596-733 (all of late Oct to the end of the 1604 register)
  and inv. 11852 scans 50-104 (about 24 Feb to 6 April 1605), at heading level. A plausible reading, graded M and not established: the
  brievenboek registers ordinaris letters from the provinces, officers and colleges, while an agent's letters to Oldenbarnevelt or to the
  griffier went into the liassen (Hoogduytschlandt inv. 6034/6035, not digitised) and were not copied here. This explains the absence
  but is not tested.
- Requests: `service.archief.nl` / `www.nationaalarchief.nl` **94** (1 item page, 1 METS, 33 scans of 11851, 59 scans of 11852), all
  HTTP 200, no 403/429/challenge. The brief's cap was 95. NA take and release lines are in ROOM.md.
- Limits: 700 px sheets, one reader. A block of a dozen groups or fewer inside prose could escape. The controls are a French cipher letter
  and the target's own postscript. 11852 scans 2-49 and 105-522 were not screened.

## Remaining gaps (OBRED-11851B, 13 Oct 2026)
Read so far: unmeasured; nothing decoded -- no. 92 (121 groups) and the scan-187 postscript (59 groups) are both unread; they share 26 values, above chance (OBRED-187)
- no. 92 and the 187 postscript, pooled (180 tokens, 130 distinct values) - blocker: too-short; OBRED-DP: name band 588-751 stands alone (G2 PASS), shared order beyond one pair absent (G1 FAIL), so a crib test is unfalsifiable at this N; more text in the same table is the step
- the later liassen NA 1.01.02 inv. 6017-6024 (1614-1637, 4,826 scans, all digitised) - blocker: not-attempted; only a stride-3 look of 6017 plus the stride-1 fill of scans 2-36 (OBRED-11851) and 38-72 (OBRED-641, controls 12/12, no numeral block); next: the other 342 unlooked scans of 6017 at stride 1 from scan 73 (~350 requests over several NA sessions, ~$3), only if a later cipher use by the agent in 1614-1617 is worth testing
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 and 21 Feb 1605 letters - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder: brievenboek inv. 11851 scans 596-733 all looked at with controls (OBRED-SG, OBRED-11851, OBRED-641, OBRED-11851B 18/18) and inv. 11852 scans 50-104 (about 24 Feb - 6 Apr 1605, OBRED-11851B, controls 30/30): no numeral block, no Brederode, Stettin or Heidelberg heading; the register appears to copy ordinaris letters, not an agent's letters (M); next: 11852 scans 2-49 (Jan - about 23 Feb 1605; ~50 NA requests, ~$2.5), a low-yield step since neither letter's arrival window showed a register copy

## Escalation (OBRED-11851B, 13 Oct 2026)
- [x] siblings: scan 187 is a second code text sharing 26 values with no. 92 (OBRED-187); all of inv. 6016 looked at (OBRED-0259, OBRED-S1, OBRED-S2, YX-OBR): no third numeral block; 6017 stride 3 (OBRED-S3) plus scans 2-36 and 38-72 at stride 1 (OBRED-11851, OBRED-641): none
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187: Stettin, 17 Oct 1604, to the griffier of the States General); it carries no gloss of the code
- [x] known-keys: the 10 Aug 1598 Van Aerssen slip excluded for no. 92 by design (R10-OBRED98); Buzanval syllabary inv. 2028 excluded (R9-OBRED4); DECODE 1600s and Palatine/Hessian keys screened (OLD-DKEY, R8-OBRED2, R9-OBRED3)
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII has no decipherment or key note near the Brederode entries (OBRED-DP)
- [ ] key-rebuild: design_prior and structure done (OBRED-DP); a crib/run-length test waits on a third text in the same table, none found in 6016, 6017 (part), 11851 596-733 or 11852 50-104; next: a third text from the 6017 fill or 11852 scans 2-49, then the crib consistency test with a synthetic matched control, ~$3
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv two blind passes agreeing 59/59 (OBRED-187)
- [x] retry: Den Tex (abridged edition) read twice (25 Sept; OBRED-SG 10 Oct 2026): no cipher, key or Stettin note; brievenboek 11851 596-733 completed with controls (OBRED-11851, OBRED-641, OBRED-11851B) and 11852 50-104 screened (OBRED-11851B)
Verdict: keep going: 1 internal gap; cheapest next: the 6017 stride-1 fill from scan 73 (342 scans left, ~$3 per ~60-90 scans with controls); 11852 scans 2-49 (~$2.5) is lower yield, since the 1604 register to its end and the Feb-Apr 1605 arrival window of no. 92 showed no register copy of either letter (OBRED-11851B)

## OBRED-11852A (13 Oct 2026, 22:13-22:2x UTC by date -u, account 4, Opus; for LANE DEFAULT-A4-2135)

Brief: NA 1.01.02 inv. 11852 (brievenboek 1605) scans 2-49, the January to about 23 February 1605 part that OBRED-11851B left
unscreened, by OBRED-11851B's route, sizes, controls and contact-sheet method. Nothing decoded; no gate computed.

- Prior-work step: `prior_work.py oldenbarnevelt-brederode-1605 --item-spec 'NL-HaNA 1.01.02 inv. 11852 scans 2-49' --step-type read
  --fetch` exit 4: 1 LOOK (the target-level look.tsv crop of no. 92, not a register scan), 2 UNCHECKED (solver caches by unit,
  Tomokiyo), 2 UNCHECKED-NET (aaymeloglu cache, editions); the three non-net rows recorded CLEAR in `prior-work.tsv` (the only earlier
  unit-keyed work on 11852 is OBRED-11851B: probes 1, 40, 80, 120, 160 and scans 50-104). Checks 2-4 do not apply beyond the folder's
  Premise check (a register screen, no reading); check 5 does not apply.
- Route: one item-page request (`www.nationaalarchief.nl/onderzoeken/archief/1.01.02/invnr/11852`) re-read the embedded scan list
  (522 IIIF bases; the 59 already in `screen_tools/na_11852_iiif_map.json` matched at their orders, so the order is the same), and
  bases for 2-49 were added to the map; then `screen_tools/na_fetch_map.py` at `/full/700,/0/default.jpg`, 2.1 s apart, descriptive
  User-Agent. OBRED-11851B's scans were not on disk in this container, so scan 40 was fetched again (its sha1 equals OBRED-11851B's
  manifest entry). `screen_tools/regen_11852a.sh` re-derives scans and sheets; the sheet key re-derived byte-identical from seed 1602.
  Images stay outside git; sha1s in `images/manifest.json` (`obred_11851b.files`, tagged OBRED-11852A).
- Contact sheets: `screen_tools/contact_sheets.py`, 8 sheets of six scans plus the three disk controls (CTRL-CIPHER = inv. 2016 scan 31,
  CTRL-PLAIN = inv. 6016 order 261, CTRL-PS = scan 187 at 1200 px), seed 1602, tile letters only; every call written to
  `images/sg_11852_screen2_sheetcalls.txt` before the key (`images/sg_11852_screen2_sheetkey.json`) was opened. One reader, this
  worker's own eye, no subagent.
- **Controls: 24 of 24 placed correctly (8 sheets x 3), checked mechanically against the key; all 48 scan tiles called as scans. No
  sheet is a non-test.** A further check: the printed page numbers read blind on the tiles run p.1-44 in scan order (scan = page + 5
  from scan 8), which the key confirms.
- **Result, inv. 11852 scans 2-49** (rows appended to `images/sg_11852_screen1.tsv`, sheet column A1-A8): **no numeral-code block, key
  table or interlinear decipherment.** Scans 2-5 are the cover's inner leaves (blank openings, a title "Register ... Fol. 1-312");
  scan 6 opens the register, "Brieven ingekomen uit diversche plaetsen in den Jaere 1605", Raad van State, exhibitum about 6 January
  1605. Printed pp. 1-44 run from about 6 January to 24 February 1605 by exhibitum: Raad van State, Gedeputeerden and Stad Groningen
  en Ommelanden, Willem Lodewijk of Nassau at Leeuwarden, the Commissarissen Coren and Bomman (Sluys, Middelburg), the Graef van
  Oostfriesland, Maurice of Nassau, Dorth/Voogt/Hilman, States General acts of 3, 4 and 24 Feb 1605. Figures seen are money sums
  (pp. 6-8), a "Bylage" of ships and skippers of Nov-Dec 1604 with amount columns (pp. 15-20), a muster table by province (p. 22), a
  company list with pay amounts (p. 28) and garrison lists of captains' names (pp. 40-44, Bergen op Zoom "Besetting" 24 Feb 1605);
  none is a code-group run. French entries: p. 5 ("Les Estats Generaux des Provinces Unies", an outgoing text), p. 20 ("Monsieur",
  ex 24 Jan), p. 21 ("Messeigneurs", ex 25 Jan), p. 35 (a French entry whose Dutch margin heading names a sender not read at 700 px,
  M). **No Brederode, Heidelberg, Stettin or Palatine heading was seen** (headings read at 700 px; a name inside a long entry, or the
  unread p. 35 heading, could escape).
- Where the Stettin (17 Oct 1604) and Heidelberg (21 Feb 1605) letters were not found: inv. 11851 scans 596-733 and inv. 11852 scans
  2-104 (about 23 Oct 1604 to 6 April 1605), every scan looked at once with controls, at heading level. The M reading of OBRED-11851B
  (the brievenboek copies ordinaris letters from provinces, colleges and officers, not an agent's letters) fits this too and stays
  untested.
- Requests: `www.nationaalarchief.nl` 1 (item page) and `service.archief.nl` 48 (scans 2-49 at 700 px) = **49**, all HTTP 200, no
  403/429/challenge; brief cap 55. NA take and release lines in ROOM.md.
- Limits: 700 px sheets, one reader; a block of a dozen groups or fewer inside prose could escape; the p. 35 margin heading is unread
  (a 1400 px region look would settle it, 1 request); controls are a French cipher letter and the target's own postscript. 11852 scans
  105-522 (April 1605 onward) not screened: past both letters' arrival windows.

## Remaining gaps (OBRED-11852A, 13 Oct 2026)
Read so far: unmeasured; nothing decoded -- no. 92 (121 groups) and the scan-187 postscript (59 groups) are both unread; they share 26 values, above chance (OBRED-187)
- no. 92 and the 187 postscript, pooled (180 tokens, 130 distinct values) - blocker: too-short; OBRED-DP: name band 588-751 stands alone (G2 PASS), shared order beyond one pair absent (G1 FAIL), so a crib test is unfalsifiable at this N; more text in the same table is the step
- the later liassen NA 1.01.02 inv. 6017-6024 (1614-1637, 4,826 scans, all digitised) - blocker: not-attempted; only a stride-3 look of 6017 plus the stride-1 fill of scans 2-36 (OBRED-11851) and 38-72 (OBRED-641, controls 12/12, no numeral block); next: the other 342 unlooked scans of 6017 at stride 1 from scan 73 (~350 requests over several NA sessions, ~$3), only if a later cipher use by the agent in 1614-1617 is worth testing
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 and 21 Feb 1605 letters - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder done: brievenboek inv. 11851 scans 596-733 and inv. 11852 scans 2-104 (about 23 Oct 1604 - 6 Apr 1605) all looked at with controls (OBRED-SG, OBRED-11851, OBRED-641, OBRED-11851B 18/18 and 30/30, OBRED-11852A 24/24): no numeral block, no Brederode, Stettin or Heidelberg heading; the register appears to copy ordinaris letters, not an agent's letters (M)

## Escalation (OBRED-11852A, 13 Oct 2026)
- [x] siblings: scan 187 is a second code text sharing 26 values with no. 92 (OBRED-187); all of inv. 6016 looked at (OBRED-0259, OBRED-S1, OBRED-S2, YX-OBR): no third numeral block; 6017 stride 3 (OBRED-S3) plus scans 2-36 and 38-72 at stride 1 (OBRED-11851, OBRED-641): none
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187: Stettin, 17 Oct 1604, to the griffier of the States General); it carries no gloss of the code
- [x] known-keys: the 10 Aug 1598 Van Aerssen slip excluded for no. 92 by design (R10-OBRED98); Buzanval syllabary inv. 2028 excluded (R9-OBRED4); DECODE 1600s and Palatine/Hessian keys screened (OLD-DKEY, R8-OBRED2, R9-OBRED3)
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII has no decipherment or key note near the Brederode entries (OBRED-DP)
- [ ] key-rebuild: design_prior and structure done (OBRED-DP); a crib/run-length test waits on a third text in the same table, none found in 6016, 6017 (part), 11851 596-733 or 11852 2-104; next: a third text from the 6017 fill (from scan 73), then the crib consistency test with a synthetic matched control, ~$3
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv two blind passes agreeing 59/59 (OBRED-187)
- [x] retry: Den Tex (abridged edition) read twice (25 Sept; OBRED-SG 10 Oct 2026): no cipher, key or Stettin note; brievenboek 11851 596-733 and 11852 2-104 completed with controls (OBRED-11851, OBRED-641, OBRED-11851B, OBRED-11852A)
Verdict: keep going: 1 internal gap; cheapest next: the 6017 stride-1 fill from scan 73 (342 scans left, ~$3 per ~60-90 scans with controls); the digitised brievenboek remainder for both letters' arrival windows is now screened with no register copy (OBRED-11852A)

## OBRED-6017B (14 Oct 2026, 09:52-10:0x UTC by date -u, account 4, Opus; for LANE DEFAULT-A4-0935-14)

Brief: the inv. 6017 stride-1 fill from scan 73 named by OBRED-11852A's Verdict, by OBRED-11851's method (700 px scans, 3x3 contact
sheets of six scans plus the three disk controls, calls before key). Nothing decoded; no gate computed.

- Prior-work step: `prior_work.py oldenbarnevelt-brederode-1605 --item-spec 'NL-HaNA 1.01.02 inv. 6017 scans 74 onward (stride-1 fill)'
  --step-type read` exit 4: 1 LEAD (this job's own claim), 1 LOOK (the target-level look.tsv crop of no. 92, not a 6017 scan), 2
  UNCHECKED (solver caches by unit, Tomokiyo), 2 UNCHECKED-NET (aaymeloglu cache, editions); the three non-net rows recorded CLEAR in
  `prior-work.tsv` (earlier unit-keyed work on 6017 is OBRED-S3 stride 3, OBRED-11851 scans 2-36, OBRED-641 scans 38-72). Checks 2-4 do
  not apply beyond the folder's Premise check (a liassen screen, no reading); check 5 does not apply.
- Scope: scan 73 is one of OBRED-S3's stride-3 samples (1, 4, ..., 583), so the fill starts at 74. Taken here: **the 90 scans of
  74-207 not sampled by OBRED-S3** (74, 75, 77, 78, ..., 206, 207). With OBRED-S3's samples, every scan 1-207 of inv. 6017 has now been
  looked at once.
- Route: METS `b060ccbc-...` (1 request) and `screen_tools/na_fetch.py`, IIIF `/full/700,/0/default.jpg`, 2.1 s apart, descriptive
  User-Agent. 15 sheets by `screen_tools/contact_sheets.py`, seed 6074, controls CTRL-CIPHER = inv. 2016 scan 31, CTRL-PLAIN = inv. 6016
  order 261, CTRL-PS = scan 187 at 1200 px (no request), tile letters only. Every call was written to
  `images/6017_screen_s6_sheetcalls.txt` before the key (`images/6017_screen_s6_sheetkey.json`) was opened. One reader, this worker's own
  eye, no subagent. Images stay outside git; sha1s in `images/manifest.json` (`obred_6017b`); `screen_tools/regen_6017b.sh` re-derives
  scans and sheets, and the sheet key re-derived byte-identical from seed 6074.
- **Controls: 45 of 45 placed correctly (15 sheets x 3), checked mechanically against the key; all 90 scan tiles called as scans. No
  sheet is a non-test.**
- **Result, inv. 6017 scans 74-207 (stride-1 fill): no numeral-code block, key table or interlinear decipherment on any of the 90**
  (`images/6017_screen_s6.tsv`, 90 rows). Content: the 1615 run of the liasse (a blank divider at scan 81, OBRED-S3's year divider at 82)
  to the 1616 divider (scan 198) and the first 1616 letters. Dutch letters to the States General, many signed P. Brederode from Heidelberg
  (datelines read at sheet size: April, May, 24 July, 10 August, late 1615; some from Frankfurt, April 1615), address leaves with seals,
  French copies and extracts of 1615 ("Extraict d'une lettre ...", "Copie de la lettre ..."), Spanish royal letters ("Don Phelippe por la
  gracia de Dios ...", Madrid), German pieces ("Kurtzer Bericht ..."), blank openings. Figures seen: a list of regiments and companies with
  an amount column (scan in sheet 5, printed p. about 649), and on scan 80 a sideways money addition (94-11 1/2, 95-9 1/2 ... 100-0, ruled
  sum lines), checked by one region look at 1200 px; neither is a code-group run. **No Brederode letter in this run carries a numeral
  postscript or figure block.** Dates and folio numbers in the TSV are read at 700 px and are approximate (marked "?").
- Requests: `service.archief.nl` **92** (1 METS, 90 scans at 700 px, 1 scan at 1200 px), all HTTP 200, no 403/429/challenge; brief
  cap 100. NA take and release lines in ROOM.md.
- Limits: 700 px sheets, one reader; a block of a dozen groups or fewer inside prose could escape; the controls are a French cipher letter
  and the target's own postscript. Inv. 6017 has **252 scans unlooked** (342 minus these 90; next unlooked scan 209, since 208 is an
  OBRED-S3 sample). Not a negative for the series elsewhere.

## Remaining gaps (OBRED-6017B, 14 Oct 2026)
Read so far: unmeasured; nothing decoded -- no. 92 (121 groups) and the scan-187 postscript (59 groups) are both unread; they share 26 values, above chance (OBRED-187)
- no. 92 and the 187 postscript, pooled (180 tokens, 130 distinct values) - blocker: too-short; OBRED-DP: name band 588-751 stands alone (G2 PASS), shared order beyond one pair absent (G1 FAIL), so a crib test is unfalsifiable at this N; more text in the same table is the step
- the later liassen NA 1.01.02 inv. 6017-6024 (1614-1637, 4,826 scans, all digitised) - blocker: not-attempted; 6017 scans 1-207 all looked at (OBRED-S3 stride 3; stride-1 fill 2-36 OBRED-11851, 38-72 OBRED-641, 74-207 OBRED-6017B, controls 45/45, no numeral block); next: the other 252 unlooked scans of 6017 at stride 1 from scan 209 (~255 requests over about three NA sessions, ~$3 per 90 scans), only if a later cipher use by the agent in 1614-1617 is worth testing
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 and 21 Feb 1605 letters - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder done: brievenboek inv. 11851 scans 596-733 and inv. 11852 scans 2-104 (about 23 Oct 1604 - 6 Apr 1605) all looked at with controls (OBRED-SG, OBRED-11851, OBRED-641, OBRED-11851B 18/18 and 30/30, OBRED-11852A 24/24): no numeral block, no Brederode, Stettin or Heidelberg heading; the register appears to copy ordinaris letters, not an agent's letters (M)

## Escalation (OBRED-6017B, 14 Oct 2026)
- [x] siblings: scan 187 is a second code text sharing 26 values with no. 92 (OBRED-187); all of inv. 6016 looked at (OBRED-0259, OBRED-S1, OBRED-S2, YX-OBR): no third numeral block; 6017 stride 3 (OBRED-S3) plus scans 2-36, 38-72 and 74-207 at stride 1 (OBRED-11851, OBRED-641, OBRED-6017B): none
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187: Stettin, 17 Oct 1604, to the griffier of the States General); it carries no gloss of the code
- [x] known-keys: the 10 Aug 1598 Van Aerssen slip excluded for no. 92 by design (R10-OBRED98); Buzanval syllabary inv. 2028 excluded (R9-OBRED4); DECODE 1600s and Palatine/Hessian keys screened (OLD-DKEY, R8-OBRED2, R9-OBRED3)
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII has no decipherment or key note near the Brederode entries (OBRED-DP)
- [ ] key-rebuild: design_prior and structure done (OBRED-DP); a crib/run-length test waits on a third text in the same table, none found in 6016, 6017 scans 1-207, 11851 596-733 or 11852 2-104; next: a third text from the 6017 fill (from scan 209), then the crib consistency test with a synthetic matched control, ~$3
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv two blind passes agreeing 59/59 (OBRED-187)
- [x] retry: Den Tex (abridged edition) read twice (25 Sept; OBRED-SG 10 Oct 2026): no cipher, key or Stettin note; brievenboek 11851 596-733 and 11852 2-104 completed with controls (OBRED-11851, OBRED-641, OBRED-11851B, OBRED-11852A)
Verdict: keep going: 1 internal gap; cheapest next: the 6017 stride-1 fill from scan 209 (252 scans left, ~$3 per ~90 scans with controls); scans 1-207 (1614 to early 1616) carry no numeral block (OBRED-6017B)

## OBRED-6017C (14 Oct 2026, 10:13-10:3x UTC by date -u, account 4, Opus; for LANE DEFAULT-A4-0935-14)

Brief: the inv. 6017 fill from scan 209 named by OBRED-6017B's Verdict, by the same method (700 px scans, 3x3 contact sheets of six
scans plus the three disk controls, calls written before the key is opened). Nothing decoded; no gate computed.

- Prior-work step: `prior_work.py oldenbarnevelt-brederode-1605 --item-spec 'NL-HaNA 1.01.02 inv. 6017 scans 209 onward (stride-1 fill)'
  --step-type read` exit 4: 1 LEAD (this job's own claim), 1 LOOK (the target-level look.tsv crop of no. 92, not a 6017 scan), 2
  UNCHECKED, 2 UNCHECKED-NET; the three non-net rows recorded CLEAR in `prior-work.tsv`, as OBRED-6017B did.
- Scope: scans 208 and 352 are OBRED-S3 stride-3 samples, so the fill took **the 96 scans of 209-351 not sampled by OBRED-S3** (209, 210,
  212, 213, ..., 350, 351). With OBRED-S3's samples, every scan 1-351 of inv. 6017 (585 scans in the METS) has now been looked at once.
- Route: METS `b060ccbc-...` (1 request) and `screen_tools/na_fetch.py`, IIIF `/full/700,/0/default.jpg`, 2.1 s apart, descriptive
  User-Agent. 16 sheets by `screen_tools/contact_sheets.py`, seed 6209, the same controls as OBRED-6017B (CTRL-CIPHER = inv. 2016 scan 31,
  CTRL-PLAIN = inv. 6016 order 261, CTRL-PS = scan 187 at 1200 px; disk, no request), tile letters only. Every call was written to
  `images/6017_screen_s7_sheetcalls.txt` before the key (`images/6017_screen_s7_sheetkey.json`) was opened. One reader, this worker's own
  eye, no subagent. Images stay outside git (kept in the session scratchpad); sha1s in `images/manifest.json` (`obred_6017c`);
  `screen_tools/regen_6017c.sh` re-derives scans and sheets, and the sheet key re-derived byte-identical from seed 6209.
- **Controls: 48 of 48 placed correctly (16 sheets x 3), checked mechanically against the key; all 96 scan tiles called as scans. No
  sheet is a non-test.**
- **Result, inv. 6017 scans 209-351 (stride-1 fill): no numeral-code block, key table or interlinear decipherment on any of the 96**
  (`images/6017_screen_s7.tsv`, 96 rows). Content: the 1616 run of the liasse from March to about December 1616 / January 1617. Mostly Dutch
  letters to the States General signed P. Brederode from Heidelberg (datelines and dockets read at sheet size: March, April, May, June,
  July, August, September, October, November, December 1616), address leaves with seals, blank openings; around scans 311-326 a run of
  French, Latin and German copies (one headed "Decretum ... Maximiliano wegen der Succession in Hungern"); around 327-336 a "Bylage van
  Brederode 15/21 Dec 1616", a piece headed "Die Staten generael ...", and heavily corrected States-side drafts (minuten) headed
  "Brederode", one dated in The Hague. One tile (scan 332) carries a marginal flourish beside the heading, not figures. **No Brederode
  letter in this run carries a numeral postscript or figure block.** Dates in the TSV are read at 700 px and approximate (marked "?").
- Requests: `service.archief.nl` **97** (1 METS, 96 scans at 700 px), all HTTP 200, no 403/429/challenge; brief cap 100. NA take and
  release lines in ROOM.md. No 1200 px region look was needed.
- Limits: 700 px sheets, one reader; a block of a dozen groups or fewer inside prose could escape; the controls are a French cipher letter
  and the target's own postscript. Inv. 6017 has **156 scans unlooked** (353-584 not sampled by OBRED-S3; next unlooked scan 353). Not a
  negative for the series elsewhere.

## Remaining gaps (OBRED-6017C, 14 Oct 2026)
Read so far: unmeasured; nothing decoded -- no. 92 (121 groups) and the scan-187 postscript (59 groups) are both unread; they share 26 values, above chance (OBRED-187)
- no. 92 and the 187 postscript, pooled (180 tokens, 130 distinct values) - blocker: too-short; OBRED-DP: name band 588-751 stands alone (G2 PASS), shared order beyond one pair absent (G1 FAIL), so a crib test is unfalsifiable at this N; more text in the same table is the step
- the later liassen NA 1.01.02 inv. 6017-6024 (1614-1637, 4,826 scans, all digitised) - blocker: not-attempted; 6017 scans 1-351 all looked at (OBRED-S3 stride 3; stride-1 fill 2-36 OBRED-11851, 38-72 OBRED-641, 74-207 OBRED-6017B, 209-351 OBRED-6017C, controls 45/45 and 48/48, no numeral block); next: the other 156 unlooked scans of 6017 at stride 1 from scan 353 (~160 requests over two NA sessions, ~$3 per 90 scans), only if a later cipher use by the agent in 1614-1617 is worth testing
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 and 21 Feb 1605 letters - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder done: brievenboek inv. 11851 scans 596-733 and inv. 11852 scans 2-104 (about 23 Oct 1604 - 6 Apr 1605) all looked at with controls (OBRED-SG, OBRED-11851, OBRED-641, OBRED-11851B 18/18 and 30/30, OBRED-11852A 24/24): no numeral block, no Brederode, Stettin or Heidelberg heading; the register appears to copy ordinaris letters, not an agent's letters (M)

## Escalation (OBRED-6017C, 14 Oct 2026)
- [x] siblings: scan 187 is a second code text sharing 26 values with no. 92 (OBRED-187); all of inv. 6016 looked at (OBRED-0259, OBRED-S1, OBRED-S2, YX-OBR): no third numeral block; 6017 stride 3 (OBRED-S3) plus scans 2-36, 38-72, 74-207 and 209-351 at stride 1 (OBRED-11851, OBRED-641, OBRED-6017B, OBRED-6017C): none
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187: Stettin, 17 Oct 1604, to the griffier of the States General); it carries no gloss of the code
- [x] known-keys: the 10 Aug 1598 Van Aerssen slip excluded for no. 92 by design (R10-OBRED98); Buzanval syllabary inv. 2028 excluded (R9-OBRED4); DECODE 1600s and Palatine/Hessian keys screened (OLD-DKEY, R8-OBRED2, R9-OBRED3)
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII has no decipherment or key note near the Brederode entries (OBRED-DP)
- [ ] key-rebuild: design_prior and structure done (OBRED-DP); a crib/run-length test waits on a third text in the same table, none found in 6016, 6017 scans 1-351, 11851 596-733 or 11852 2-104; next: a third text from the 6017 fill (from scan 353), then the crib consistency test with a synthetic matched control, ~$3
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv two blind passes agreeing 59/59 (OBRED-187)
- [x] retry: Den Tex (abridged edition) read twice (25 Sept; OBRED-SG 10 Oct 2026): no cipher, key or Stettin note; brievenboek 11851 596-733 and 11852 2-104 completed with controls (OBRED-11851, OBRED-641, OBRED-11851B, OBRED-11852A)
Verdict: keep going: 1 internal gap; cheapest next: the 6017 stride-1 fill from scan 353 (156 scans left, ~$3 per ~90 scans with controls); scans 1-351 (1614 to about January 1617) carry no numeral block (OBRED-6017C)

## OBRED-6017D (14 Oct 2026, 10:41-10:5x UTC by date -u, account 4, Opus; for LANE DEFAULT-A4-0935-14)

Brief: the inv. 6017 fill from scan 352 to the end, by the method of OBRED-6017B/C (700 px scans, 3x3 contact sheets of six scans plus
the three disk controls, calls written before the key is opened). Nothing decoded; no gate computed.

- Prior-work step: `prior_work.py oldenbarnevelt-brederode-1605 --item-spec 'NL-HaNA 1.01.02 inv. 6017 scans 353 onward (stride-1 fill)'
  --step-type read` exit 4: 1 LEAD (this job's own claim), 1 LOOK (the target-level look.tsv crop of no. 92, not a 6017 scan), 2
  UNCHECKED, 2 UNCHECKED-NET; the three non-net rows recorded CLEAR in `prior-work.tsv`, as OBRED-6017B/C did.
- Scope: scan 352 is an OBRED-S3 stride-3 sample (= 1 mod 3), so the fill starts at 353. The NA request limit (100) allowed one METS call
  plus 96 scans: taken here are **the 96 scans of 353-495 not sampled by OBRED-S3** (353, 354, 356, 357, ..., 494, 495). With OBRED-S3's
  samples, every scan 1-495 of inv. 6017 (585 scans in the METS) has now been looked at once. The inventory is **not finished**: 60
  scans of 497-585 remain unlooked (496 is an S3 sample; next unlooked scan 497).
- Route: METS `b060ccbc-...` (1 request) and `screen_tools/na_fetch.py`, IIIF `/full/700,/0/default.jpg`, 2.1 s apart, descriptive
  User-Agent. 16 sheets by `screen_tools/contact_sheets.py`, seed 6353, the same controls as OBRED-6017B/C (CTRL-CIPHER = inv. 2016 scan
  31, CTRL-PLAIN = inv. 6016 order 261, CTRL-PS = scan 187 at 1200 px; disk, no request), tile letters only. Every call was written to
  `images/6017_screen_s8_sheetcalls.txt` before the key (`images/6017_screen_s8_sheetkey.json`) was opened. One reader, this worker's own
  eye, no subagent. Images stay outside git (session scratchpad); sha1s in `images/manifest.json` (`obred_6017d`);
  `screen_tools/regen_6017d.sh` re-derives scans and sheets, and the sheet key re-derived byte-identical from seed 6353 (checked from disk).
- **Controls: 48 of 48 placed correctly (16 sheets x 3), checked mechanically against the key; all 96 scan tiles called as scans. No
  sheet is a non-test.**
- **Result, inv. 6017 scans 353-495 (stride-1 fill): no numeral-code block, key table or interlinear decipherment on any of the 96**
  (`images/6017_screen_s8.tsv`, 96 rows). Content: the 1617 run of the liasse from about February to October 1617. Mostly Dutch letters to
  the States General signed P. Brederode, from Heidelberg (February to early September 1617, datelines and dockets read at sheet size)
  and from Frankfurt (late September / October 1617), address leaves with seals, blank openings. Also: a run of Latin prose (an address to
  the princes, around scans 360-375); French pieces from the Union meeting at Heilbronn ("Fait a Heilbron ... Avril 1617", one on the
  Elector Palatine and the Duke of Savoy); German pieces dated "Hailbron den 11. Aprilis 1617"; a list of the Union princes with names
  only; a Palatine chancery letter "Signatum ... Julij 1617"; a French letter "Monseigneur ..." of September 1617; an itemised Dutch
  account in numbered articles with sums at line ends and a "Memorie" in numbered articles (September 1617) -- figures in a list, not
  code groups. **No Brederode letter in this run carries a numeral postscript or figure block.** Dates in the TSV are read at 700 px and
  approximate (marked "?").
- Requests: `service.archief.nl` **97** (1 METS, 96 scans at 700 px), all HTTP 200, no 403/429/challenge; brief cap 100. NA take and
  release lines in ROOM.md. No 1200 px region look was needed.
- Limits: 700 px sheets, one reader; a block of a dozen groups or fewer inside prose could escape; the controls are a French cipher letter
  and the target's own postscript. Inv. 6017 has **60 scans unlooked** (497-585 not sampled by OBRED-S3; next unlooked scan 497). Not a
  negative for the series elsewhere.

## Remaining gaps (OBRED-6017D, 14 Oct 2026)
Read so far: unmeasured; nothing decoded -- no. 92 (121 groups) and the scan-187 postscript (59 groups) are both unread; they share 26 values, above chance (OBRED-187)
- no. 92 and the 187 postscript, pooled (180 tokens, 130 distinct values) - blocker: too-short; OBRED-DP: name band 588-751 stands alone (G2 PASS), shared order beyond one pair absent (G1 FAIL), so a crib test is unfalsifiable at this N; more text in the same table is the step
- the later liassen NA 1.01.02 inv. 6017-6024 (1614-1637, 4,826 scans, all digitised) - blocker: not-attempted; 6017 scans 1-495 all looked at (OBRED-S3 stride 3; stride-1 fill 2-36 OBRED-11851, 38-72 OBRED-641, 74-207 OBRED-6017B, 209-351 OBRED-6017C, 353-495 OBRED-6017D, controls 45/45, 48/48 and 48/48, no numeral block); next: the last 60 unlooked scans of 6017 at stride 1 from scan 497 (~61 requests, one NA session, ~$2), only if a later cipher use by the agent in 1614-1617 is worth testing
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 and 21 Feb 1605 letters - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder done: brievenboek inv. 11851 scans 596-733 and inv. 11852 scans 2-104 (about 23 Oct 1604 - 6 Apr 1605) all looked at with controls (OBRED-SG, OBRED-11851, OBRED-641, OBRED-11851B 18/18 and 30/30, OBRED-11852A 24/24): no numeral block, no Brederode, Stettin or Heidelberg heading; the register appears to copy ordinaris letters, not an agent's letters (M)

## Escalation (OBRED-6017D, 14 Oct 2026)
- [x] siblings: scan 187 is a second code text sharing 26 values with no. 92 (OBRED-187); all of inv. 6016 looked at (OBRED-0259, OBRED-S1, OBRED-S2, YX-OBR): no third numeral block; 6017 stride 3 (OBRED-S3) plus scans 2-36, 38-72, 74-207, 209-351 and 353-495 at stride 1 (OBRED-11851, OBRED-641, OBRED-6017B, OBRED-6017C, OBRED-6017D): none
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187: Stettin, 17 Oct 1604, to the griffier of the States General); it carries no gloss of the code
- [x] known-keys: the 10 Aug 1598 Van Aerssen slip excluded for no. 92 by design (R10-OBRED98); Buzanval syllabary inv. 2028 excluded (R9-OBRED4); DECODE 1600s and Palatine/Hessian keys screened (OLD-DKEY, R8-OBRED2, R9-OBRED3)
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII has no decipherment or key note near the Brederode entries (OBRED-DP)
- [ ] key-rebuild: design_prior and structure done (OBRED-DP); a crib/run-length test waits on a third text in the same table, none found in 6016, 6017 scans 1-495, 11851 596-733 or 11852 2-104; next: a third text from the last 6017 scans (497-585), then the crib consistency test with a synthetic matched control, ~$3
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv two blind passes agreeing 59/59 (OBRED-187)
- [x] retry: Den Tex (abridged edition) read twice (25 Sept; OBRED-SG 10 Oct 2026): no cipher, key or Stettin note; brievenboek 11851 596-733 and 11852 2-104 completed with controls (OBRED-11851, OBRED-641, OBRED-11851B, OBRED-11852A)
Verdict: keep going: 1 internal gap; cheapest next: the 6017 stride-1 fill from scan 497 to 585 (60 scans left, one NA session, ~$2); scans 1-495 (1614 to about October 1617) carry no numeral block (OBRED-6017D)

## OBRED-6017E (14 Oct 2026, 11:09-11:2x UTC by date -u, account 4, Opus; for LANE DEFAULT-A4-0935-14)

Brief: the inv. 6017 fill from scan 497 to the end named by OBRED-6017D's Verdict, by the method of OBRED-6017B/C/D (700 px scans, 3x3
contact sheets of six scans plus the three disk controls, calls written before the key is opened); finish the inventory and set the
siblings rung and Verdict. Nothing decoded; no gate computed.

- Prior-work step: `prior_work.py oldenbarnevelt-brederode-1605 --item-spec 'NL-HaNA 1.01.02 inv. 6017 scans 497 onward (stride-1 fill)'
  --step-type read` exit 4: 1 LEAD (this job's own claim), 1 LOOK (the target-level look.tsv crop of no. 92, not a 6017 scan), 2
  UNCHECKED, 2 UNCHECKED-NET; the three non-net rows recorded CLEAR in `prior-work.tsv` (adhoc-f03f31), as OBRED-6017B/C/D did.
- Scope: scan 496 is an OBRED-S3 stride-3 sample (= 1 mod 3), so the fill took **the 60 scans of 497-585 not sampled by OBRED-S3** (497,
  498, 500, 501, ..., 584, 585); the METS still lists 585 scans. With OBRED-S3's samples, **every scan 1-585 of inv. 6017 has now been
  looked at once: the inventory is finished.**
- Route: METS `b060ccbc-...` (1 request) and `screen_tools/na_fetch.py`, IIIF `/full/700,/0/default.jpg`, 2.1 s apart, descriptive
  User-Agent. 10 sheets by `screen_tools/contact_sheets.py`, seed 6497, the same controls as OBRED-6017B/C/D (CTRL-CIPHER = inv. 2016 scan
  31, CTRL-PLAIN = inv. 6016 order 261, CTRL-PS = scan 187 at 1200 px; disk, no request), tile letters only. Every call was written to
  `images/6017_screen_s9_sheetcalls.txt` before the key (`images/6017_screen_s9_sheetkey.json`) was opened. One reader, this worker's own
  eye, no subagent. Images stay outside git (session scratchpad); sha1s in `images/manifest.json` (`obred_6017e`);
  `screen_tools/regen_6017e.sh` re-derives scans and sheets and checks the sheet key.
- **Controls: 30 of 30 placed correctly (10 sheets x 3), checked mechanically against the key; all 60 scan tiles called as scans. No
  sheet is a non-test.**
- **Result, inv. 6017 scans 497-585 (stride-1 fill, end of the inventory): no numeral-code block, key table or interlinear decipherment on
  any of the 60** (`images/6017_screen_s9.tsv`, 60 rows). Content: the last run of the liasse, October to 30 December 1617. Mostly Dutch
  letters to the States General signed P. Brederode (several with paraph) from Heidelberg (datelines and dockets read at sheet size: 21,
  26, 31 Oct, 17 Nov, 22 and 30 Dec 1617), address leaves with red seals, blank openings. Also: Italian copies/avvisi (around scans 551-552,
  567, one naming the Spanish ambassador); French letters headed "Magnifiques Seigneurs ..." and "Les Seigneurs des ligues Grises ..."
  (Swiss and Grisons affairs, around 561-566); Latin pieces on the Grey Leagues with capital-letter headings and marginal item labels
  (569-572); a heavily corrected Dutch States-side draft (573) and a pasted-in minute slip (576). Scan 585 is a single address leaf with
  seal and a grey card, apparently the end of the volume. **No Brederode letter in this run carries a numeral postscript or figure block.**
  Dates in the TSV are read at 700 px and approximate (marked "?").
- Requests: `service.archief.nl` **61** (1 METS, 60 scans at 700 px), all HTTP 200, no 403/429/challenge; brief cap 80. NA take and
  release lines in ROOM.md. No 1200 px region look was needed.
- Limits: 700 px sheets, one reader per scan across all the 6017 jobs; a block of a dozen groups or fewer inside prose could escape; the
  controls are a French cipher letter and the target's own postscript. **Inv. 6017 (1614-1617) as a whole: every scan looked at once, no
  third text in the no. 92 / scan-187 table.** Not a negative for 6018-6024 or the series elsewhere.

## Remaining gaps (OBRED-6017E, 14 Oct 2026)
Read so far: unmeasured; nothing decoded -- no. 92 (121 groups) and the scan-187 postscript (59 groups) are both unread; they share 26 values, above chance (OBRED-187)
- no. 92 and the 187 postscript, pooled (180 tokens, 130 distinct values) - blocker: too-short; OBRED-DP: name band 588-751 stands alone (G2 PASS), shared order beyond one pair absent (G1 FAIL), so a crib test is unfalsifiable at this N; more text in the same table is the step
- the later liassen NA 1.01.02 inv. 6018-6024 (1618-1637, 4,241 scans, all digitised, METS ids in `nl_brederode_lias.tsv`) - blocker: not-attempted; inv. 6016 and 6017 (1602-1617) are now looked at in full (6017: OBRED-S3 stride 3; stride-1 fill OBRED-11851, OBRED-641, OBRED-6017B/C/D/E, controls 45/45, 48/48, 48/48, 30/30), no third numeral block; next: a stride-3 screen of inv. 6018 (1618, 577 scans, ~193 requests over two NA sessions, ~$5) by the same method, only if a later cipher use by the agent is worth testing -- four years of his letters (1614-1617) carry none
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 and 21 Feb 1605 letters - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder done: brievenboek inv. 11851 scans 596-733 and inv. 11852 scans 2-104 (about 23 Oct 1604 - 6 Apr 1605) all looked at with controls (OBRED-SG, OBRED-11851, OBRED-641, OBRED-11851B 18/18 and 30/30, OBRED-11852A 24/24): no numeral block, no Brederode, Stettin or Heidelberg heading; the register appears to copy ordinaris letters, not an agent's letters (M)

## Escalation (OBRED-6017E, 14 Oct 2026)
- [x] siblings: scan 187 is a second code text sharing 26 values with no. 92 (OBRED-187); all of inv. 6016 looked at (OBRED-0259, OBRED-S1, OBRED-S2, YX-OBR) and all of inv. 6017 looked at (OBRED-S3 stride 3 plus the stride-1 fill by OBRED-11851, OBRED-641, OBRED-6017B, OBRED-6017C, OBRED-6017D, OBRED-6017E): no third numeral block in 1602-1617; inv. 6018-6024 (1618-1637) not yet screened
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187: Stettin, 17 Oct 1604, to the griffier of the States General); it carries no gloss of the code
- [x] known-keys: the 10 Aug 1598 Van Aerssen slip excluded for no. 92 by design (R10-OBRED98); Buzanval syllabary inv. 2028 excluded (R9-OBRED4); DECODE 1600s and Palatine/Hessian keys screened (OLD-DKEY, R8-OBRED2, R9-OBRED3)
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII has no decipherment or key note near the Brederode entries (OBRED-DP)
- [ ] key-rebuild: design_prior and structure done (OBRED-DP); a crib/run-length test waits on a third text in the same table, none found in 6016, 6017 (complete), 11851 596-733 or 11852 2-104; next: a stride-3 screen of inv. 6018 (1618) for a third text, then the crib consistency test with a synthetic matched control, ~$5 for the screen
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv two blind passes agreeing 59/59 (OBRED-187)
- [x] retry: Den Tex (abridged edition) read twice (25 Sept; OBRED-SG 10 Oct 2026): no cipher, key or Stettin note; brievenboek 11851 596-733 and 11852 2-104 completed with controls (OBRED-11851, OBRED-641, OBRED-11851B, OBRED-11852A)
Verdict: keep going: 1 internal gap; cheapest next: a stride-3 screen of inv. 6018 (1618, 577 scans, ~$5 over two NA sessions); inv. 6016-6017 (1602-1617) are finished with no third numeral block, so the expected yield of the later liassen is low (OBRED-6017E)

## OBRED-6018 (14 Oct 2026, 22:22-22:4x UTC by date -u, account 2, Opus; for LANE DEFAULT-A2-2209-14)

Brief: stride-3 screen of NA 1.01.02 inv. 6018 (Liassen Agent Brederode, 1618, 577 scans) for a third numeral text in the no. 92 /
scan-187 table, by the method of OBRED-S3 / OBRED-6017E. Nothing decoded; no gate computed.

- Prior-work step: `prior_work.py oldenbarnevelt-brederode-1605 --item-spec 'NL-HaNA 1.01.02 inv. 6018 scans 1-577 (stride-3 screen)'
  --step-type read` exit 4: 1 LEAD (this job's own claim), 1 LOOK (the target-level look.tsv crop of no. 92, not a 6018 scan), 2
  UNCHECKED, 2 UNCHECKED-NET; the four non-net rows recorded CLEAR in `prior-work.tsv` (adhoc-d64c4d). Check 1: no earlier section ran
  any of inv. 6018 (grep `6018`: only the lias table and the gap lines). Check 5 not applicable.
- Scope: scans 1, 4, ..., 577 (= 1 mod 3), **193 of 577**.
- Route: METS `8ab6959a-...` from `nl_brederode_lias.tsv` (1 request, 577 scans, matches the item page count), `screen_tools/na_fetch.py`,
  IIIF `/full/700,/0/default.jpg`, 2.1 s apart, descriptive User-Agent; 3 scans at `/full/1200,/0/default.jpg`. 22 sheets by
  `screen_tools/contact_sheets.py` with its new `SHEET_SCANS=9` option (4x3 sheets, nine scans plus the three disk controls; the default
  3x3 mode is unchanged and still reproduces the 6017E key), seed 6018, tile letters only; controls as OBRED-6017B..E (CTRL-CIPHER = inv.
  2016 scan 31, CTRL-PLAIN = inv. 6016 order 261, CTRL-PS = scan 187 at 1200 px; disk, no request). Every call was written to
  `images/6018_screen_sheetcalls.txt` and pushed (0ab8a2cb9) before the key (`images/6018_screen_sheetkey.json`) was opened. One reader,
  this worker's own eye, no subagent. 700 px scans stay outside git; sha1s in `images/manifest.json` (`obred_6018`);
  `screen_tools/regen_6018.sh` re-derives scans and sheets and checks the key (rebuild from disk reproduced the key).
- **Controls: 66 of 66 placed correctly (22 sheets x 3), checked mechanically against the key. No sheet is a non-test.**
- **Result, inv. 6018 stride 3: no numeral-code block, key table or interlinear decipherment on any of the 193 scans**
  (`images/6018_screen.tsv`, 193 rows). Content: the 1618 run of the liasse, January to December, mostly Dutch letters to the States
  General signed P. Brederode (several with paraph; datelines read at sheet size from about March to December 1618, approximate),
  address leaves with red seals, openings, blank versos; also Latin pieces (numbered articles, a delegate list, a letter dated in roman
  numerals MDCXVIII), French, Italian and Spanish copies and avvisi, and 'Post data' paragraphs in prose. Three tiles called doubtful at
  sheet size were re-looked at 1200 px and are plain (committed as `images/na_101_02_6018_p0NNN_1200.jpg`):
  - 214: a pasted slip of faded prose on the left, a short Dutch note headed "Brederode" on the right; no numerals.
  - 379: a Latin letter (Bern legates, the Longueville matter, the Elector); the marks along the right edge are cut-off text of the
    leaves beneath.
  - 460: an inverted address on a blank verso, show-through on the left.
- Requests: `service.archief.nl` **197** (1 METS, 193 at 700 px, 3 at 1200 px), all HTTP 200, no 403/429/challenge; brief cap 220. NA
  take and release lines in ROOM.md.
- Where it was not found, and the limits: **every third scan only** -- 384 of the 577 scans of inv. 6018 were not looked at, and inv.
  6019-6024 (3,664 scans) not at all; a one-leaf numeral postscript is a third as likely to be sampled as a run of three. Tiles were
  about 525 px wide on a sheet read at about 1,568 px, close to OBRED-S3's 400 px; a block of a dozen groups or fewer inside prose
  could escape; one reader; the controls are a French cipher letter and the target's own postscript. A negative for these 193 scans at
  this resolution, not for inv. 6018 as a whole.

## Remaining gaps (OBRED-6018, 14 Oct 2026)
Read so far: unmeasured; nothing decoded -- no. 92 (121 groups) and the scan-187 postscript (59 groups) are both unread; they share 26 values, above chance (OBRED-187)
- no. 92 and the 187 postscript, pooled (180 tokens, 130 distinct values) - blocker: too-short; OBRED-DP: name band 588-751 stands alone (G2 PASS), shared order beyond one pair absent (G1 FAIL), so a crib test is unfalsifiable at this N; more text in the same table is the step
- the later liassen NA 1.01.02 inv. 6018-6024 (1618-1637, 4,241 scans, all digitised, METS ids in `nl_brederode_lias.tsv`) - blocker: not-attempted; inv. 6016 and 6017 (1602-1617) looked at in full, inv. 6018 at stride 3 (OBRED-6018: 193 scans, controls 66/66), no third numeral block in any; next: the 384 unsampled scans of inv. 6018 (two NA sessions at stride-1 fill, ~$6) or a stride-3 screen of inv. 6019 (1619, 649 scans, ~217 requests, ~$4), only if a later cipher use by the agent is worth testing -- five years of his letters (1614-1618) show none at the depth screened
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 and 21 Feb 1605 letters - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder done: brievenboek inv. 11851 scans 596-733 and inv. 11852 scans 2-104 (about 23 Oct 1604 - 6 Apr 1605) all looked at with controls (OBRED-SG, OBRED-11851, OBRED-641, OBRED-11851B 18/18 and 30/30, OBRED-11852A 24/24): no numeral block, no Brederode, Stettin or Heidelberg heading; the register appears to copy ordinaris letters, not an agent's letters (M)

## Escalation (OBRED-6018, 14 Oct 2026)
- [x] siblings: scan 187 is a second code text sharing 26 values with no. 92 (OBRED-187); all of inv. 6016 and 6017 looked at (OBRED-0259, OBRED-S1, OBRED-S2, YX-OBR; OBRED-S3 plus the stride-1 fill OBRED-11851, OBRED-641, OBRED-6017B/C/D/E) and inv. 6018 at stride 3 (OBRED-6018, controls 66/66): no third numeral block in 1602-1618 at the depth screened; inv. 6018 fill and 6019-6024 not yet screened
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187: Stettin, 17 Oct 1604, to the griffier of the States General); it carries no gloss of the code
- [x] known-keys: the 10 Aug 1598 Van Aerssen slip excluded for no. 92 by design (R10-OBRED98); Buzanval syllabary inv. 2028 excluded (R9-OBRED4); DECODE 1600s and Palatine/Hessian keys screened (OLD-DKEY, R8-OBRED2, R9-OBRED3)
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII has no decipherment or key note near the Brederode entries (OBRED-DP)
- [ ] key-rebuild: design_prior and structure done (OBRED-DP); a crib/run-length test waits on a third text in the same table, none found in 6016, 6017 (complete), 6018 (stride 3), 11851 596-733 or 11852 2-104; next: a stride-3 screen of inv. 6019 (1619) or the 6018 fill for a third text, then the crib consistency test with a synthetic matched control, ~$4-6 for the screen
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv two blind passes agreeing 59/59 (OBRED-187)
- [x] retry: Den Tex (abridged edition) read twice (25 Sept; OBRED-SG 10 Oct 2026): no cipher, key or Stettin note; brievenboek 11851 596-733 and 11852 2-104 completed with controls (OBRED-11851, OBRED-641, OBRED-11851B, OBRED-11852A)
Verdict: keep going: 1 internal gap; cheapest next: a stride-3 screen of inv. 6019 (1619, 649 scans, ~$4) or the stride-1 fill of inv. 6018 (384 scans, ~$6); 1602-1618 show no third numeral block at the depth screened, so the expected yield of the later liassen is low (OBRED-6018)

## OBRED-6019 (15 Oct 2026, 05:49-06:0x UTC by date -u, account 2, Opus; for LANE DEFAULT-A2-0509-15)

Brief: stride-3 screen of NA 1.01.02 inv. 6019 (Liassen Agent Brederode, 1619, 649 scans) for a third numeral text in the no. 92 /
scan-187 table, by the method of OBRED-6018. Nothing decoded; no gate computed.

- Prior-work step: `prior_work.py oldenbarnevelt-brederode-1605 --item-spec 'NL-HaNA 1.01.02 inv. 6019 scans 1-649 (stride-3 screen)'
  --step-type read` exit 4: 1 LEAD (this job's own claim), 1 LOOK (the target-level look.tsv crop of no. 92, not a 6019 scan), 2
  UNCHECKED, 2 UNCHECKED-NET; the four non-net rows recorded CLEAR in `prior-work.tsv` (adhoc-632749). Check 1: no earlier section ran
  any of inv. 6019 (grep `6019`: only the lias table and the gap lines). Check 5 not applicable.
- PREREG addendum `obred187/PREREG-OBRED6019.md` pushed (4c629aa57) before any fetch; it carries the stop rule.
- Scope: scans 1, 4, ..., 649 (= 1 mod 3), 217 fetched; **sheets 1-19 read = 171 scans (1-511)**. Sheets 20-25 (scans 514-649 at stride
  3, 46 scans) were built but **not read**: the PREREG stop rule (80% of the cap 5, priced from OBRED-6018's 4.43 for 22 sheets) allowed
  about 19-20 sheets, and the reader stopped after 19.
- Route: METS `1ebb4182-...` from `nl_brederode_lias.tsv` (1 request, 649 scans, matches the item page count), `screen_tools/na_fetch.py`,
  IIIF `/full/700,/0/default.jpg`, 2.1 s apart, descriptive User-Agent. 25 sheets by `screen_tools/contact_sheets.py` with SHEET_SCANS=9,
  seed 6019, controls as OBRED-6018 (CTRL-CIPHER = inv. 2016 scan 31, CTRL-PLAIN = inv. 6016 order 261, CTRL-PS = scan 187 at 1200 px;
  disk, no request). Every call was written to `images/6019_screen_sheetcalls.txt` and pushed (4e0add3de) before the key
  (`images/6019_screen_sheetkey.json`) was opened. One reader, this worker's own eye, no subagent. **No image committed**; sha1s of the
  217 scans in `images/manifest.json` (`obred_6019`); `screen_tools/regen_6019.sh` re-derives scans and sheets and checks the key (the key
  rebuilt from disk reproduced byte-identical).
- **Controls: 57 of 57 placed correctly (19 sheets x 3), checked mechanically against the key. No sheet is a non-test.**
- **Result, inv. 6019 scans 1-511 at stride 3: no numeral-code block, key table or interlinear decipherment on any of the 171 scans**
  (`images/6019_screen.tsv`, 171 rows). Content: the 1619 run of the liasse from January to about early October 1619 (datelines read at
  sheet size, approximate). Mostly Dutch letters to the States General signed P. Brederode (many with paraph), address leaves with red
  seals, letter openings, blank openings; also German pieces (one dated August 1619), French letters (one headed "Extraict ... 19
  avril"), Italian copies/avvisi, Latin prose, pieces headed "Exhib." and "Copie", and pieces in numbered articles (article numbers in
  the margin; one list of names in numbered articles) -- figures in a list, not code groups. One 'Post data' paragraph (sheet 1) is in
  prose. **No Brederode letter in this sample carries a numeral postscript or figure block.** No 1200 px re-look was needed.
- Requests: `service.archief.nl` **218** (1 METS, 217 at 700 px), all HTTP 200, no 403/429/challenge; brief cap 230. NA take and
  release lines in ROOM.md.
- Where it was not found, and the limits: **every third scan of 1-511 only**; 46 stride-3 scans of 514-649 fetched but not read, and the
  other two thirds of the inventory not looked at; a one-leaf numeral postscript is a third as likely to be sampled as a run of three.
  Tiles about 525 px wide on a sheet read at about 2,000 px; a block of a dozen groups or fewer inside prose could escape; one reader; the
  controls are a French cipher letter and the target's own postscript. A negative for these 171 scans at this resolution, not for inv.
  6019 as a whole.

## Remaining gaps (OBRED-6019, 15 Oct 2026)
Read so far: unmeasured; nothing decoded -- no. 92 (121 groups) and the scan-187 postscript (59 groups) are both unread; they share 26 values, above chance (OBRED-187)
- no. 92 and the 187 postscript, pooled (180 tokens, 130 distinct values) - blocker: too-short; OBRED-DP: name band 588-751 stands alone (G2 PASS), shared order beyond one pair absent (G1 FAIL), so a crib test is unfalsifiable at this N; more text in the same table is the step
- the later liassen NA 1.01.02 inv. 6018-6024 (1618-1637, all digitised, METS ids in `nl_brederode_lias.tsv`) - blocker: not-attempted; inv. 6016 and 6017 (1602-1617) looked at in full, inv. 6018 at stride 3 (OBRED-6018, controls 66/66), inv. 6019 scans 1-511 at stride 3 (OBRED-6019: 171 scans, controls 57/57), no third numeral block in any; next: the last 6 sheets of inv. 6019 (stride-3 scans 514-649, 46 scans; re-fetch by `screen_tools/regen_6019.sh` or read sheets 20-25, ~$1.5), then 6020-6024 only if a later cipher use by the agent is worth testing -- six years of his letters (1614-1619) show none at the depth screened
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 and 21 Feb 1605 letters - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder done: brievenboek inv. 11851 scans 596-733 and inv. 11852 scans 2-104 (about 23 Oct 1604 - 6 Apr 1605) all looked at with controls (OBRED-SG, OBRED-11851, OBRED-641, OBRED-11851B 18/18 and 30/30, OBRED-11852A 24/24): no numeral block, no Brederode, Stettin or Heidelberg heading; the register appears to copy ordinaris letters, not an agent's letters (M)

## Escalation (OBRED-6019, 15 Oct 2026)
- [x] siblings: scan 187 is a second code text sharing 26 values with no. 92 (OBRED-187); all of inv. 6016 and 6017 looked at (OBRED-0259, OBRED-S1, OBRED-S2, YX-OBR; OBRED-S3 plus the stride-1 fill OBRED-11851, OBRED-641, OBRED-6017B/C/D/E), inv. 6018 at stride 3 (OBRED-6018, controls 66/66) and inv. 6019 scans 1-511 at stride 3 (OBRED-6019, controls 57/57): no third numeral block in 1602-1619 at the depth screened; 6019 sheets 20-25, the 6018/6019 fills and 6020-6024 not yet screened
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187: Stettin, 17 Oct 1604, to the griffier of the States General); it carries no gloss of the code
- [x] known-keys: the 10 Aug 1598 Van Aerssen slip excluded for no. 92 by design (R10-OBRED98); Buzanval syllabary inv. 2028 excluded (R9-OBRED4); DECODE 1600s and Palatine/Hessian keys screened (OLD-DKEY, R8-OBRED2, R9-OBRED3)
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII has no decipherment or key note near the Brederode entries (OBRED-DP)
- [ ] key-rebuild: design_prior and structure done (OBRED-DP); a crib/run-length test waits on a third text in the same table, none found in 6016, 6017 (complete), 6018 (stride 3), 6019 scans 1-511 (stride 3), 11851 596-733 or 11852 2-104; next: 6019 sheets 20-25 (46 scans, ~$1.5), then the crib consistency test with a synthetic matched control only if a third text appears
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv two blind passes agreeing 59/59 (OBRED-187)
- [x] retry: Den Tex (abridged edition) read twice (25 Sept; OBRED-SG 10 Oct 2026): no cipher, key or Stettin note; brievenboek 11851 596-733 and 11852 2-104 completed with controls (OBRED-11851, OBRED-641, OBRED-11851B, OBRED-11852A)
Verdict: keep going: 1 internal gap; cheapest next: inv. 6019 stride-3 sheets 20-25 (scans 514-649, 46 scans, one NA session of 47 requests or regen, ~$1.5); 1602-1619 show no third numeral block at the depth screened, so the expected yield of the later liassen is low (OBRED-6019)

## OBRED-6019B (15 Oct 2026, 06:25-06:4x UTC by date -u, account 2, Opus; for LANE DEFAULT-A2-0509-15)

Brief: read the six OBRED-6019 sheets left unread (sheets 20-25 = inv. 6019 stride-3 scans 514-649, 46 scans), same PREREG and
controls. Nothing decoded; no gate computed.

- Prior-work step: `prior_work.py oldenbarnevelt-brederode-1605 --item-spec 'NL-HaNA 1.01.02 inv. 6019 scans 514-649 (stride-3, sheets
  20-25)' --step-type read` exit 4: 1 LOOK (the target-level look.tsv crop of no. 92, not a 6019 scan), 2 UNCHECKED, 2 UNCHECKED-NET,
  the same generic rows as OBRED-6018/6019 (rows written to `prior-work.tsv`/`look.tsv` by the tool). Check 1: OBRED-6019 is the only
  earlier section on inv. 6019 and did not read sheets 20-25.
- PREREG addendum `obred187/PREREG-OBRED6019B.md` pushed (6b4e41577) before any fetch.
- Rebuild: the 700 px scans were not committed, so `screen_tools/regen_6019b.sh` re-fetched the 46 scans (+ METS) and rebuilt all 25
  sheets with blank placeholders for scans 1-511, so the seed-6019 shuffle is unchanged; `cmp` of the rebuilt key against
  `images/6019_screen_sheetkey.json` passed without either being opened, and all 46 re-fetched scans are byte-identical to the sha1s
  OBRED-6019 recorded. Calls for sheets 20-25 appended to `images/6019_screen_sheetcalls.txt` and pushed (60a6bb678) before the key was
  opened. One reader, this worker's own eye.
- **Controls: 18 of 18 placed correctly (6 sheets x 3), checked mechanically against the key. No sheet is a non-test.** With OBRED-6019:
  inv. 6019 stride 3 complete, 217 scans, controls 75/75.
- **Result: one hit. Scan 556 (sheet 21 tile I, called doubtful at sheet size and re-looked at 1200 px, scratchpad only, sha1 in
  `images/manifest.json`)** is a Dutch letter (about October 1619 by its place in the liasse; dateline not on this opening) whose left page
  carries about six lines of **numeral groups inside the prose, with interlinear glosses above some groups and a marginal gloss** -- a
  numeral code of the same general kind as no. 92 / scan 187 (arabic groups separated by points, inside prose). Provisional single read at
  1200 px, every token grade M, not a transcription (two blind passes owed):
  `578 605 | 457 13 289 797 798 | 433 461 385 50 | 73 193 458 | 67? 390 415 202 109 | 593 594 | 430 100 169 110 241 337 120 | 380`
  (32 groups; `|` = prose between). Glosses seen, unread at this resolution and not used: a two-word name above 605, a marginal note
  beside 457-798 (begins "van ambassadeur van ..."), "Turck" in the margin, a name above 593, a word above 594, and single letters above
  430-337 (which would suggest letter-level values in that range). Whether this is the no. 92 / 187 table is **not tested**: no overlap
  count or gate was pre-registered for this job. The other 45 scans of sheets 20-25 show no numeral block (`images/6019_screen.tsv`):
  October-December 1619 letters signed P. Brederode, address leaves, openings, French/Latin prose, one 'Post data' in prose, one piece in
  numbered articles (margin numbers, not code groups).
- Requests: `service.archief.nl` **48** (1 METS + 46 at 700 px + 1 at 1200 px), all HTTP 200; PREREG cap 53. NA take/release in ROOM.md.
- Where it was not found, and the limits: every third scan only; the neighbours of 556 (555, 557: the rest of that letter, possibly more
  groups or a decipherment) and two thirds of inv. 6019 not looked at; inv. 6020-6024 not at all. One reader at sheet size.

## Remaining gaps (OBRED-6019B, 15 Oct 2026)
Read so far: unmeasured; nothing decoded -- no. 92 (121 groups) and the scan-187 postscript (59 groups) are both unread; they share 26 values, above chance (OBRED-187); inv. 6019 scan 556 carries a third numeral text (about 32 groups, interlinear glosses), single provisional read only (OBRED-6019B)
- no. 92 and the 187 postscript, pooled (180 tokens, 130 distinct values) - blocker: not-attempted; OBRED-DP found a crib test unfalsifiable at 180 tokens; inv. 6019 scan 556 may add a third text with glosses; next: two blind transcription passes of scan 556 and its neighbours 555/557 at native size (crop step mandatory) plus a read of the glosses, then a pre-registered overlap test of its values against no. 92/187 with a shuffled-value control, ~$4
- the later liassen NA 1.01.02 inv. 6020-6024 (1620-1637, all digitised, METS ids in `nl_brederode_lias.tsv`) - blocker: not-attempted; inv. 6016-6017 in full, 6018 and 6019 at stride 3 (controls 66/66, 75/75); one numeral block found (6019 scan 556, about Oct 1619); next: only after scan 556 is placed -- if it is the no. 92 table, a stride-3 screen of inv. 6020 (~$4) and the 6019 stride-1 fill around 556
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 and 21 Feb 1605 letters - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder done: brievenboek inv. 11851 scans 596-733 and inv. 11852 scans 2-104 (about 23 Oct 1604 - 6 Apr 1605) all looked at with controls (OBRED-SG, OBRED-11851, OBRED-641, OBRED-11851B 18/18 and 30/30, OBRED-11852A 24/24): no numeral block, no Brederode, Stettin or Heidelberg heading; the register appears to copy ordinaris letters, not an agent's letters (M)

## Escalation (OBRED-6019B, 15 Oct 2026)
- [x] siblings: scan 187 is a second code text sharing 26 values with no. 92 (OBRED-187); inv. 6016 and 6017 in full, 6018 and 6019 at stride 3 (OBRED-6018 66/66; OBRED-6019 + OBRED-6019B 75/75): one further numeral block, inv. 6019 scan 556 (about Oct 1619, interlinear glosses), not yet transcribed or placed
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187: Stettin, 17 Oct 1604, to the griffier of the States General); it carries no gloss of the code
- [x] known-keys: the 10 Aug 1598 Van Aerssen slip excluded for no. 92 by design (R10-OBRED98); Buzanval syllabary inv. 2028 excluded (R9-OBRED4); DECODE 1600s and Palatine/Hessian keys screened (OLD-DKEY, R8-OBRED2, R9-OBRED3)
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII has no decipherment or key note near the Brederode entries (OBRED-DP)
- [ ] key-rebuild: design_prior and structure done (OBRED-DP); a third text found (inv. 6019 scan 556, glossed); next: two blind passes of 556 (and 555/557) with the glosses read, then a pre-registered value-overlap test against no. 92/187 with a shuffled-value control, ~$4
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv two blind passes agreeing 59/59 (OBRED-187)
- [x] retry: Den Tex (abridged edition) read twice (25 Sept; OBRED-SG 10 Oct 2026): no cipher, key or Stettin note; brievenboek 11851 596-733 and 11852 2-104 completed with controls (OBRED-11851, OBRED-641, OBRED-11851B, OBRED-11852A)
Verdict: keep going: 2 internal gaps; inv. 6019 stride-3 screen closed (217 scans, controls 75/75) with one hit, scan 556 (about Oct 1619, ~32 numeral groups with interlinear glosses); cheapest next: two blind passes of scans 555-557 and a pre-registered overlap test against no. 92/187 (~$4)

## OBRED-556 (15 Oct 2026, 07:02-07:1x UTC by date -u, account 2, Opus; for LANE DEFAULT-A2-0509-15)

Brief: two blind passes of inv. 6019 scans 555-557 (the numeral block OBRED-6019B found on 556), the glosses read once (Opus) and checked
once (Sonnet), and a pre-registered value-overlap test against no. 92 / the scan-187 postscript with a shuffled-code control. No key edit.

- Prior-work step: `prior_work.py oldenbarnevelt-brederode-1605 --item-spec 'NL-HaNA 1.01.02 inv. 6019 scans 555-557 ...' --step-type read
  --fetch` exit 4: 1 LEAD (this job's own claim), 1 LOOK (the target-level no. 92 crop), 2 UNCHECKED, 2 UNCHECKED-NET; the four non-net
  rows recorded CLEAR in `prior-work.tsv` (adhoc-851b7d); `grep -ril brederode sources/` finds nothing on inv. 6019. Check 1: OBRED-6019B's
  single provisional read is the only earlier work on these scans.
- PREREG `obred187/PREREG-OBRED556.md` pushed in its own commit (76466e0cb) before any fetch or score.
- Requests: `service.archief.nl` 4 (METS + scans 555, 556, 557 at 5000 px), all HTTP 200; NA take/release in ROOM.md. No image committed:
  sha1s in `images/manifest.json` (`obred_556`); `screen_tools/regen_556.sh` re-derives scans, line crops and gloss crops.
- **What the scans are.** One letter: it runs from before 555 (555 left page begins mid-letter, "de Catholijcken ...") through 556 to 557,
  which ends "uyt Ogersheim desen 14 octob. 1619 / UE. onderdanighste ende getrouwe dienaer / P. van Brederode" (grade M, by eye). Two
  numeral blocks: 555 right page (12 lines carrying groups, about 55 groups) and 556 left page (6 lines, 26 groups). Scan 557 carries no
  groups. OBRED-6019B saw only the 556 block.
- **Transcription.** `tools/iiif_lines.py --image s0555_5000.jpg --region 2480,1180,2280,1560 --prefix s555 --debug` (15 bands) and
  `--image s0556_5000.jpg --region 440,660,2160,720 --prefix s556 --debug` (7 bands); overlays checked (one text line per band). Two blind
  Sonnet passes, each as two calls of 11 crops (not told any value or no. 92). `ciphertext_556.tsv`: **81 groups, 55 H-read (both passes agree,
  high), 26 M.** The band cut lost one line (555 "30 265 434 530 320", between L14 and L15 bands): it has one transcription only (from the two
  gloss-check calls on taller crops), graded M. Pass disagreements: 529 (passes 579, the reconciler and G1 529), 241/221/271 (555 L13, under an
  ink cross), 605/665 (555 L09).
- **Glosses.** Many groups carry a small interlinear letter above them, a few a name; three marginal notes summarise. Read once by this worker
  on taller crops that keep the gloss band (`g/t555_*`, `g/t556_*`), and checked by two blind Sonnet calls (G1, G2) on the same crops.
  **45 group glosses graded C (both reads agree on one letter or name over one group), 16 M.** The letter glosses spell Dutch words across
  runs (grade M as words, read by this worker from the C letters): 555 L05-L06 "te favoriseren" (457 125 | 145 36 490 337 409 220 433 132 413
  126 324), 555 L12 "met vrede" (290 178 459 490 415 130 100 129; margin "met vrede te"), 555 L14-L15 "neutra[e]l..." (323 133 483 460 411 30
  265 ...; margin, struck, "neutrael sijn"?), 556 L03-L04 "eene diversie" (73 193 458 97 390 415 202 108), 556 L05-L06 "geholpen" (430 100
  169 110 241 337 120 300). Name glosses: **605 "Fredrich Palsgrave" (556) and "Palsgrave" (555)**, **594 "Bohemen" on both pages**, 593
  "Co[ninck] van Pol[en]", 587 and 600 names not read at this size. Marginal notes: 556 "van ambassadeur van Hans George Marg." beside
  457 13 289 797 798, and "Turck"; 555 "Hertoch van B..." (unread), "met vrede te", a struck note. The glosses are a period decipherment
  on the leaf, not ours. In-text conflicts (rule 4, logged in `HYPOTHESES.md`): 415 r/s, 337 o/p, 100 d/e (one side M).
- **Overlap gate** (`python3 obred187/overlap556.py`, `--check` OK, `obred187/overlap556.json`): V556 69 distinct of 81 tokens; R = no. 92 |
  187 = 130 values; **S = 42 shared** (32 with no. 92, 23 with 187). C1 uniform mean 12.64, p99 20, p = 0.0001; C2 band-matched mean 15.37,
  p99 23, p = 0.0001; N1 Lodewijk 7206 mean 11.73, p95 16; N2 Jan van Nassau 5551 mean 8.31, p95 9. Power (187 subsampled to 81 tokens vs
  no. 92): 0.886. H-read only: 31 of 55 tokens' values shared. **The overlap clears its pre-registered control: consistent with one code list
  shared by no. 92 (1605), the 1604 postscript and this 1619 letter, grade M, not a reading.**
- Descriptive, not gated: 41 distinct values carry a C gloss here; they cover 21 of no. 92's 121 tokens and 16 of 187's 59. 605 occurs in
  no. 92 ("heeft bij 605 geobtineert", Heidelberg 1605) where the Palsgrave fits the sense (M). The names glossed here (593, 594, 600, 605) sit
  in or at the edge of OBRED-DP's name band 588-751 (587 just below it). No value was applied to no. 92 or 187 and nothing enters key.tsv: a
  glossed pair enters a key only through the folder's own path with a passing control (rule 3, per-unit merge), and the in-text conflicts
  come first.
- Where it was not found, and the limits: scans before 555 (the start of this letter, about 552-554) were not fetched, so more groups or
  glosses may precede; the inv. 6019 stride-1 fill around 556 and inv. 6020-6024 not looked at; the 555 L15 line has one transcription; the
  long glosses over 587, 600 and 732 and two margin notes are unread at this size.

## Remaining gaps (OBRED-556, 15 Oct 2026)
Read so far: unmeasured for no. 92 and 187 (nothing applied to them); inv. 6019 scans 555-556 carry 81 groups (55 H-read) with 45 C-graded period glosses; the overlap with no. 92/187 clears its control (S 42 vs C1 p99 20, C2 p99 23; OBRED-556)
- no. 92 and the 187 postscript, pooled (180 tokens) with the 1619 letter's glossed values - blocker: not-attempted; the glosses were read this pass and the --try step was outside this brief; next: resolve the gloss conflicts (415, 337, 100) on the image and build a per-unit glossed-pair table, then apply it to no. 92/187 by decode_key.py --try with a value-class control (the C glosses cover 21 of no. 92's 121 tokens), ~$3
- the start of the 1619 letter (inv. 6019 scans ~552-554) and the 555 L15 second pass - blocker: not-attempted; scans before 555 were outside this brief's 555-557; next: fetch 552-554 (3 NA requests), two blind passes of any further numeral lines plus a second pass of 555 L15, glosses read and checked, ~$3
- the later liassen NA 1.01.02 inv. 6020-6024 and the 6019 stride-1 fill - blocker: not-attempted; screening waited on placing scan 556, done this pass; next: a stride-3 screen of inv. 6020 (~$4), now worth running since the 1619 letter shows the agent still used the 1604-05 code list
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 and 21 Feb 1605 letters - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder done (OBRED-SG, OBRED-11851, OBRED-641, OBRED-11851B, OBRED-11852A): no numeral block, no Brederode, Stettin or Heidelberg heading (M)

## Escalation (OBRED-556, 15 Oct 2026)
- [x] siblings: scan 187 shares 26 values with no. 92 (OBRED-187); inv. 6019 scans 555-556 (Oggersheim, 14 Oct 1619) carry 81 groups sharing 42 values with no. 92/187, clearing the shuffled-code control (OBRED-556)
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187); the 1619 letter's prose and margin summaries read in part (OBRED-556)
- [x] known-keys: the 10 Aug 1598 Van Aerssen slip excluded for no. 92 by design (R10-OBRED98); Buzanval syllabary inv. 2028 excluded (R9-OBRED4); DECODE 1600s and Palatine/Hessian keys screened (OLD-DKEY, R8-OBRED2, R9-OBRED3)
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII has no decipherment or key note near the Brederode entries (OBRED-DP)
- [ ] key-rebuild: a period-glossed sibling in the same code list now exists (inv. 6019 scans 555-556, 45 C glosses); next: settle the three gloss conflicts on the image, then a per-unit glossed-pair table and decode_key.py --try on no. 92/187 with a value-class control, ~$3
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv 59/59 (OBRED-187); ciphertext_556.tsv two blind passes, 55 of 81 H-read (OBRED-556)
- [x] retry: Den Tex (abridged edition) read twice; brievenboek 11851 596-733 and 11852 2-104 completed with controls
Verdict: keep going: 3 internal gaps; the 1619 Oggersheim letter (inv. 6019 scans 555-556) shares the code list of no. 92 and 187 (overlap clears its control) and carries a period letter-gloss; cheapest next: settle the gloss conflicts and --try the glossed values on no. 92/187 with a control (~$3), and fetch scans 552-554 for the letter's start (~$3)

## OBRED-552 (15 Oct 2026, 08:28-08:3x UTC by date -u, account 2, Opus; for LANE DEFAULT-A2-0810-15)

Brief: NA 1.01.02 inv. 6019 scans 552-554 (expected start of the Oggersheim letter of 14 Oct 1619 whose numeral blocks are on 555-556) and a
second pass of 555 L15. No --try (OBRED-TRY's step), no key edit.

- Prior-work step: `prior_work.py oldenbarnevelt-brederode-1605 --item-spec 'NL-HaNA 1.01.02 inv. 6019 scans 552-554 + 555 L15 ...'
  --step-type read` exit 4: 2 LEAD (this job's and OBRED-TRY's claims; OBRED-TRY covers the 555/556 gloss conflicts, not 552-554), 1 LOOK
  (the target-level no. 92 crop), 2 UNCHECKED, 2 UNCHECKED-NET; the five non-net rows recorded CLEAR in `prior-work.tsv` (adhoc-7717d2).
  Check 1: OBRED-6019 saw 553 at stride 3 (sheet size, no numeral block); no earlier section read 552 or 554.
- PREREG addendum `obred187/PREREG-OBRED552.md` pushed in its own commit (6c26a46f7) before any fetch.
- Requests: `service.archief.nl` **5** (METS + scans 552, 553, 554, 555 at 5000 px), all HTTP 200; 555 is byte-identical to OBRED-556's sha1.
  No image committed: sha1s in `images/manifest.json` (`obred_552`); `screen_tools/regen_552.sh` re-derives the scans and the L15 crop.
- **What 552-554 are (by eye, grade M, this worker's read only).** None carries a numeral group, interlinear gloss or key table.
  - 552 left page: the **end of a different letter, Heidelberg 8 Oct 1619**, signed "UE Hooch: Mog. onderdanichste ende getrouwe dienaer /
    P van Brederode" with paraph, and a postscript (the Elector's sending to the three spiritual Electors; more by the bearer, "eene van Adel
    genaempt van Rousdorff"). Its last paragraph is about the cipher: "... alsoo men voortaen, apparentelycke, alle pacquetten sal betrachten
    op te vangen, hebbe ick noodich gevonden mijn voorgaende cyffer een weynich te reformeren, ende beter te doen verstaen, vermits ick hier
    voorn vernomen hebbe datter bij tselven wat difficulteyts was gevonden geworden, niet twyfelende (gelijck het seer licht es) off ten sal
    nu seer wel te verstaen sijn, hoe wel het anders sonder de selve instructie ende sleutel, niet en es te deuchyfferen; bidde UE Hooch:
    Mog. mij op desen een woort van advysse te laten weten, ten eynde ick weten mach off tselve cyffer in behouden handen sal gecommen sijn
    ..." (one reader, words read from the image at about 1,800 px, M). So by 8 Oct 1619 the agent had sent the States General a reformed
    cipher with an instruction and key ("instructie ende sleutel"), six days before the 14 Oct letter on 555-556.
  - 552 right page: the address leaf of the 8 Oct letter ("Den Hooch vermogende Heeren, Heeren Staten Generael der Vereenichde
    Nederlantsche Provintien ...", seal remnant, docket at the top edge unread).
  - 553: both pages blank (show-through of the address and of 554 only).
  - 554 left blank; 554 right: the **opening of the 14 Oct 1619 letter**, docket "d. 14 Oct. 1619 / R 28 Oct." (M), beginning "Hooch
    vermogende ... Heeren. / Uyt mijne laetste voorgaende vanden 8 deser, gelijck oock uyt het rapport des van Rusdorff ende van Adel ...",
    prose only to the foot of the page; it runs on to 555 left ("de Catholijcken ..."). So the 14 Oct letter is 554r-557, and its only numeral
    blocks are the two OBRED-556 transcribed; no groups precede them.
- **555 L15 second pass.** One whole-line crop (`tools/iiif_lines.py --image s0555_5000.jpg --region 3060,2540,880,160 --distance 200
  --prominence 10 --debug`, overlay checked: one band, all five groups), two blind Sonnet calls (not told any value). Both read
  `30 265 434 530 320`, agreeing with OBRED-556's single read on every group: 30, 265, 320 high in both -> **H-read**; 434 (alts 431/454) and
  530 (first digit under a blot; alts 630/330) low in both -> M. Neither new pass saw the interlinear letters (the crop's top edge clips
  them); the OBRED-556 gloss grades stand. `ciphertext_556.tsv` now 81 groups, **58 H-read, 23 M**.
- `obred187/overlap556.py` re-run (values unchanged, only grades): the gating numbers (S 42, C1, C2, N1, N2, power) are identical; the
  non-gating H-read sensitivity row moves from 31 of 55 to 34 of 58 tokens shared; `--check` OK.
- Where it was not found, and the limits: no numeral group on 552-554; the 8 Oct letter's own opening (scans before 552; OBRED-6019 saw 550 at
  sheet size as "letter opening, Oct 1619", no numeral block) and any enclosed "instructie ende sleutel" not looked at -- the key may have
  travelled as a separate enclosure and been filed elsewhere; 549, 551 not looked at in any pass. One reader for the prose.

## Remaining gaps (OBRED-552, 15 Oct 2026)
Read so far: unmeasured for no. 92 and 187 (nothing applied to them); inv. 6019 scans 555-556 carry 81 groups (58 H-read) with 45 C-graded period glosses; the overlap with no. 92/187 clears its control (S 42 vs C1 p99 20, C2 p99 23; OBRED-556); the 14 Oct 1619 letter is complete on 554-557 (OBRED-552)
- no. 92 and the 187 postscript, pooled (180 tokens) with the 1619 letter's glossed values - blocker: not-attempted; OBRED-TRY (LANE DEFAULT-A2-0810-15) holds the gloss-conflict and --try step; next: resolve the gloss conflicts (415, 337, 100) on the image and build a per-unit glossed-pair table, then apply it to no. 92/187 by decode_key.py --try with a value-class control, ~$3
- the reformed cipher's "instructie ende sleutel" sent with the Heidelberg letter of 8 Oct 1619 (inv. 6019, letter ending on scan 552) - blocker: not-attempted; next: read inv. 6019 scans 549-551 at 5000 px (the 8 Oct letter's opening and any enclosure; 3-4 NA requests, ~$1.5), then, if no key sheet is there, the stride-1 fill of 6019 around October 1619 for a separate key leaf
- the later liassen NA 1.01.02 inv. 6020-6024 and the 6019 stride-1 fill - blocker: not-attempted; outside the screens run so far; next: a stride-3 screen of inv. 6020 (~$4), worth running since the 1619 letter shows the agent still used the 1604-05 code list
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 and 21 Feb 1605 letters - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder done (OBRED-SG, OBRED-11851, OBRED-641, OBRED-11851B, OBRED-11852A): no numeral block, no Brederode, Stettin or Heidelberg heading (M)

## Escalation (OBRED-552, 15 Oct 2026)
- [x] siblings: scan 187 shares 26 values with no. 92 (OBRED-187); inv. 6019 scans 555-556 (Oggersheim, 14 Oct 1619) carry 81 groups sharing 42 values with no. 92/187, clearing the shuffled-code control (OBRED-556); the letter's start (554) carries no groups (OBRED-552)
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187); the 1619 letter's prose and margin summaries read in part (OBRED-556); 552-554 read by eye (OBRED-552)
- [ ] known-keys: the 10 Aug 1598 Van Aerssen slip, Buzanval inv. 2028, DECODE 1600s and Palatine/Hessian keys screened (R10-OBRED98, R9-OBRED4, OLD-DKEY, R8-OBRED2, R9-OBRED3); the 8 Oct 1619 letter names a reformed cipher sent with "instructie ende sleutel" (OBRED-552); next: inv. 6019 scans 549-551 for the enclosure, ~$1.5
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII has no decipherment or key note near the Brederode entries (OBRED-DP)
- [ ] key-rebuild: a period-glossed sibling in the same code list exists (inv. 6019 scans 555-556, 45 C glosses); next: OBRED-TRY's gloss conflicts and --try on no. 92/187 with a value-class control, ~$3
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv 59/59 (OBRED-187); ciphertext_556.tsv two blind passes, 58 of 81 H-read after the 555 L15 second pass (OBRED-556, OBRED-552)
- [x] retry: Den Tex (abridged edition) read twice; brievenboek 11851 596-733 and 11852 2-104 completed with controls
Verdict: keep going: 3 internal gaps; scans 552-554 hold no groups (552 = end of a Heidelberg 8 Oct 1619 letter saying the cipher was reformed and sent with an instruction and key; 554 = opening of the 14 Oct letter); cheapest next: inv. 6019 scans 549-551 for that enclosure (~$1.5), and OBRED-TRY's --try (~$3)

## OBRED-TRY (15 Oct 2026, 08:24-08:3x UTC by date -u, account 2, Opus; for LANE DEFAULT-A2-0810-15)

Brief: settle the gloss conflicts 415/337/100 on the image, build a per-unit glossed-pair table with its own shuffle gate, then apply it to
no. 92 / the scan-187 postscript by decode_key's --try with a value-class control. No key edit.

- Prior-work step: `prior_work.py ... --step-type decode` exit 4 (1 LEAD own claim, 1 LOOK, 2 UNCHECKED, 2 UNCHECKED-NET); the four
  non-net rows recorded CLEAR in `prior-work.tsv` (adhoc-e22962). Check 1: OBRED-556 is the only earlier work on these pairs; no --try ran.
- PREREG `obred187/PREREG-OBREDTRY.md` pushed in its own commit (b7011c090) before any fetch or score. It discloses that the worker saw a
  rising code/letter pattern in ciphertext_556.tsv before registering, so statistic B is post-hoc-selected and gated per leaf too.
- Requests: `service.archief.nl` 3 (METS + 555, 556 at 5000 px), all 200, sha1 identical to OBRED-556's; NA take/release in ROOM.md. No
  image committed. One blind Sonnet call on four gloss-line crops (scratchpad).
- **Step 1, conflicts: none settled.** Eye and blind read agree with OBRED-556 on 415 (r / s) and 337 (o / p, blind high on both); 100
  (d / e) is unsupported by the blind read on either side (blotted / "u or n"). All three stay logged in HYPOTHESES.md with witnesses
  (rule 4) and were tried as two separate hypotheses each, any outcome M.
- **Step 2, per-unit gate (`obred187/try/run_try.py`, `gate.json`): PASS.** 41 C single-letter pairs, 10,000 gloss permutations.
  A (repeat consistency): 3 repeated codes, 1 of 3 pairs agree (0.333) vs null mean 0.068, p95 0.333, p 0.19 -- not significant,
  at N 3 near non-discriminating. B (Spearman, code value vs gloss letter's alphabet index): pooled rho 0.959 (null p95 0.256, p < 1e-4),
  555 alone 0.930 (n 30, p95 0.309, p < 1e-4), 556 alone 0.989 (n 11, p95 0.524, p < 1e-4). The glossed letters rise with the code
  value: the 1619 table is, on this evidence, a homophonic list with letter codes in alphabetical bands (grade M as a design statement).
- **Step 3, --try (nl16, window 8, 100 nulls, tool defaults; leave-one-out on a scratch table `obred187/try/work/key_T.tsv`, 35 codes):
  0 accepts.** 25 glossed codes (22 C + 3 conflict) occur in no. 92/187: 20 of no. 92's 121 tokens, 16 of 187's 59.
  Target: true glosses 0 accept, 8 reject, 14 undecided (all n = 1); decoys 0 accept, 8 reject. **Power control on the 1619 text
  itself (codes with n >= 2 there): true glosses 0 of 7 accepted, 6 rejected** (decoys 0 of 7, 7 rejected). Power 0.0 < 0.70: under
  the PREREG every target verdict is a **non-test at this N**, not a negative for any gloss. Why (M): with 35 of ~130 values known, the
  ±8 window is mostly unknown codes filled with the model's likeliest letter, so the true letter does not beat the runner-up even
  where the gloss is read off the same leaf. Per code (glossed value, n92, n187, verdict): 30 a 1 0 und.; 36 a 0 1 und.; 108 e 2 1 rej.;
  120 e 0 1 und.; 126 e 0 1 und.; 132 e 0 1 und.; 169 h 1 0 und.; 193 i 0 1 und.; 217 i 1 1 rej.; 241 l 2 0 rej.; 265 l 0 1 und.;
  290 m 1 0 und.; 313 n 0 1 und.; 314 n 2 0 rej.; 320 n 0 1 und.; 409 r 1 1 rej.; 411 r 1 0 und.; 433 s 2 1 rej.; 457 t 1 1 rej.;
  460 t 1 0 und.; 468 t 1 0 und.; 529 y 1 1 rej.; 100 d|e 0 1 und.|und.; 337 o|p 1 1 und.|rej.; 415 r|s 1 0 und.|und.
  (`obred187/try/try_results.tsv`, `run_try.py --check` up to date.) Nothing applied to no. 92/187 as a reading; key.tsv not written.
- Where it was not found, and the limits: --try is the only instrument run; its power at this key density is nil on the glossed text
  itself, so it says nothing about no. 92/187. The band structure (statistic B) was not used for any value. 555 L15 (one pass) entered
  the table as transcribed. Scans 552-554 (OBRED-552's job) not used.

## Remaining gaps (OBRED-TRY, 15 Oct 2026)
Read so far: unmeasured for no. 92 and 187 (nothing applied to them); inv. 6019 scans 555-556 carry 81 groups (55 H-read) with 45 C-graded period glosses; overlap with no. 92/187 clears its control (OBRED-556); the 14 Oct 1619 letter is complete on 554-557, 58 of 81 groups H-read (OBRED-552); the glossed letters rise with the code value (rho 0.96, p < 1e-4, OBRED-TRY)
- no. 92 and the 187 postscript with the 1619 glossed values - blocker: not-attempted; decode_key --try had power 0/7 on the glossed letter itself (OBRED-TRY), so its verdicts are non-tests; next: a band-interval decode (each letter's code range from the 1619 glosses, alphabetical order) with a pre-registered held-out check -- predict one leaf's glossed letters from the other leaf's bands against a shuffled-band control -- then apply to no. 92/187 graded M, ~$3
- the reformed cipher's "instructie ende sleutel" sent with the Heidelberg letter of 8 Oct 1619 (inv. 6019, letter ending on scan 552; OBRED-552) - blocker: not-attempted; found by OBRED-552 this window, outside OBRED-TRY's brief; next: read inv. 6019 scans 549-551 at 5000 px (3-4 NA requests, ~$1.5), then, if no key sheet is there, the stride-1 fill of 6019 around October 1619
- the later liassen NA 1.01.02 inv. 6020-6024 and the 6019 stride-1 fill - blocker: not-attempted; outside this brief, the 1619 letter shows the agent still used the 1604-05 code list (OBRED-556); next: a stride-3 screen of inv. 6020 (~$4)
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 and 21 Feb 1605 letters - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder done (OBRED-SG, OBRED-11851, OBRED-641, OBRED-11851B, OBRED-11852A): no numeral block, no Brederode, Stettin or Heidelberg heading (M)

## Escalation (OBRED-TRY, 15 Oct 2026)
- [x] siblings: scan 187 shares 26 values with no. 92 (OBRED-187); inv. 6019 scans 555-556 (Oggersheim, 14 Oct 1619) share 42 values with no. 92/187, clearing the shuffled-code control (OBRED-556); the letter's start (554) carries no groups (OBRED-552)
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187); the 1619 letter's prose and margin summaries read in part (OBRED-556)
- [ ] known-keys: the 10 Aug 1598 Van Aerssen slip, Buzanval inv. 2028, DECODE 1600s and Palatine/Hessian keys screened (R10-OBRED98, R9-OBRED4, OLD-DKEY, R8-OBRED2, R9-OBRED3); the 8 Oct 1619 letter names a reformed cipher sent with "instructie ende sleutel" (OBRED-552); next: inv. 6019 scans 549-551 for the enclosure, ~$1.5
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII has no decipherment or key note near the Brederode entries (OBRED-DP)
- [ ] key-rebuild: the 1619 glossed pairs clear their own per-unit gate (OBRED-TRY, statistic B); decode_key --try ran with power 0/7 (non-test); next: band-interval decode with a held-out leaf check and shuffled-band control, then no. 92/187 graded M, ~$3
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv 59/59 (OBRED-187); ciphertext_556.tsv two blind passes, 58 of 81 H-read after the 555 L15 second pass (OBRED-556, OBRED-552); the three gloss conflicts re-seen at 5000 px, eye + blind, none settled (OBRED-TRY)
- [x] retry: Den Tex (abridged edition) read twice; brievenboek 11851 596-733 and 11852 2-104 completed with controls
Verdict: keep going: 3 internal gaps; the 1619 glossed pairs pass their per-unit gate (code value rises with gloss letter, rho 0.96) but decode_key --try has no power at this key density (0/7 on the glossed text itself), so nothing is applied to no. 92/187; cheapest next: inv. 6019 scans 549-551 for the 8 Oct 1619 key enclosure (~$1.5, OBRED-552), then a band-interval decode with a held-out leaf check (~$3)

## OBRED-549 (15 Oct 2026, 08:42-08:4x UTC by date -u, account 2, Opus; for LANE DEFAULT-A2-0810-15)

Brief: NL-HaNA 1.01.02 inv. 6019 scans 549-551 (walk back <= 4 more only if 549 is still inside the 8 Oct 1619 letter) for the "instructie
ende sleutel" the Heidelberg letter of 8 Oct 1619 says was sent with the reformed cipher (OBRED-552). Key leaf -> key_6019.tsv and a
known-answer test against ciphertext_556.tsv's 45 C glosses; no key leaf -> say what the scans are and stop.

- Prior-work step: `prior_work.py oldenbarnevelt-brederode-1605 --item-spec 'NL-HaNA 1.01.02 inv. 6019 scans 549-551 ...' --step-type read`
  exit 4: 1 LEAD (this job's own claim), 1 LOOK (the target-level no. 92 crop), 2 UNCHECKED, 2 UNCHECKED-NET; the four non-net rows recorded
  CLEAR in `prior-work.tsv` (adhoc-f826a0). Check 1: OBRED-6019 saw 550 at sheet size, stride 3 ("letter opening, Oct 1619", no numeral
  block); no earlier pass read 549 or 551.
- PREREG addendum `obred187/PREREG-OBRED549.md` pushed in its own commit (99e04076e) before any fetch.
- Requests: `service.archief.nl` **4** (METS + scans 549, 550, 551 at 5000 px), all HTTP 200, >= 3 s apart (`screen_tools/na_fetch.py`
  pause raised from 2.1 to 3.1 s for the shared-host rule); NA take/release in ROOM.md. No image committed: sha1s in `images/manifest.json`
  (`obred_549`); `screen_tools/regen_549.sh` re-derives the scans and the two eye crops. No subagent call (nothing to transcribe).
- **What 549-551 are (by eye, grade M, this worker's read only, quarter-size views plus two full-resolution crops).** None carries a numeral
  group, numeral table, alphabet, name list, interlinear gloss or anything laid out as a key or an instruction.
  - 549 left page: the **end of a French piece** in a cursive hand, one paragraph: "Ce partant puis que par les raisons susd. il a esté
    suffisamment deduict et representé, que le Roy Ferdinand n'a jamais esté esleu Roy de Boheme par voye ordinaire, et que luy mesme s'est
    privé et est descheu de la reception et du Couronnement ... comme le tout sera plus amplement deduict par un Manifeste qui sera donné au
    public." -- a justification of the Bohemian deposition of Ferdinand, not a letter of Brederode's and not a key. 549 right page: blank.
    So 549 is not inside the 8 Oct letter; per the brief, no walk-back was made.
  - 550 left page: blank (outer side of the sheet). 550 right page: the **opening of the 8 Oct 1619 letter**, docket in a later pencil-grey
    hand "d 8 Oct. 1619 / R 17 Oct." (M), flourished heading "Hoochvermogende Hoochghe[leerde?] ende ghe-/biedende Heeren", text "UE.
    Hoochvermogende hebben sonder eenigen twyfel uyt mijne laetste voorgaende ... verstaen ... die goede ende vaste resolutie die alhier bij
    sijne Curf. Hoocheyt ende aenwesende Fursten ... het Coninckrijck Bohemen ..." (M), prose to the foot of the page.
  - 551 both pages: the 8 Oct letter continued, prose only (551 left ends with "Furst Christiaen van Anhalt" leaving for the army after news
    from Prague of a mutiny in the Bohemian army for want of pay; 551 right on a general council of state and finance in Bohemia) (M).
  - So the 8 Oct letter is complete on 550r-552r (with its address on 552 right, OBRED-552): three scans, prose only, and the "instructie
    ende sleutel" is not filed with it in this run.
- Known-answer test: **not run** (no key leaf; PREREG step 3 conditional). Nothing scored; key_6019.tsv not created; key.tsv not touched.
- Where it was not found, and the limits: not on 549-552 (this pass and OBRED-552). Not looked at: the rest of inv. 6019 at stride 1 around
  October 1619 (scans before 549, and after 557), where a separately filed key leaf might sit; the States General's own receipt of the
  key (resolutions of 17-28 Oct 1619, when the 8 Oct letter was received); inv. 6020-6024. One reader for the prose; words quoted are M.

## Remaining gaps (OBRED-549, 15 Oct 2026)
Read so far: unmeasured for no. 92 and 187 (nothing applied to them); inv. 6019 scans 555-556 carry 81 groups (58 H-read) with 45 C-graded period glosses; overlap with no. 92/187 clears its control (OBRED-556); the 14 Oct 1619 letter is complete on 554-557 (OBRED-552) and the 8 Oct 1619 letter on 550-552, prose only (OBRED-549); the glossed letters rise with the code value (rho 0.96, p < 1e-4, OBRED-TRY)
- no. 92 and the 187 postscript with the 1619 glossed values - blocker: not-attempted; decode_key --try had power 0/7 on the glossed letter itself (OBRED-TRY), so its verdicts are non-tests; next: a band-interval decode (each letter's code range from the 1619 glosses, alphabetical order) with a pre-registered held-out check -- predict one leaf's glossed letters from the other leaf's bands against a shuffled-band control -- then apply to no. 92/187 graded M, ~$3
- the reformed cipher's "instructie ende sleutel" sent with the Heidelberg letter of 8 Oct 1619 - blocker: not-attempted; not filed with the letter on 549-552 (OBRED-549); next: the States General resolutions of 17-28 Oct 1619 (Resolutiën der Staten-Generaal, Huygens retroboeken, nieuwe reeks 1619) for a note on the key's receipt or where it was laid, then a stride-1 screen of inv. 6019 scans 520-548 and 558-600 at sheet size for a key leaf, ~$2
- the later liassen NA 1.01.02 inv. 6020-6024 and the 6019 stride-1 fill - blocker: not-attempted; outside this brief, the 1619 letter shows the agent still used the 1604-05 code list (OBRED-556); next: a stride-3 screen of inv. 6020 (~$4)
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 and 21 Feb 1605 letters - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder done (OBRED-SG, OBRED-11851, OBRED-641, OBRED-11851B, OBRED-11852A): no numeral block, no Brederode, Stettin or Heidelberg heading (M)

## Escalation (OBRED-549, 15 Oct 2026)
- [x] siblings: scan 187 shares 26 values with no. 92 (OBRED-187); inv. 6019 scans 555-556 (Oggersheim, 14 Oct 1619) share 42 values with no. 92/187, clearing the shuffled-code control (OBRED-556); the letter's start (554) carries no groups (OBRED-552)
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187); the 1619 letter's prose and margin summaries read in part (OBRED-556); 549-554 read by eye (OBRED-552, OBRED-549)
- [ ] known-keys: the 10 Aug 1598 Van Aerssen slip, Buzanval inv. 2028, DECODE 1600s and Palatine/Hessian keys screened (R10-OBRED98, R9-OBRED4, OLD-DKEY, R8-OBRED2, R9-OBRED3); the 8 Oct 1619 letter's "instructie ende sleutel" is not on 549-552 (OBRED-549); next: Resolutiën S.G. 17-28 Oct 1619 for the key's receipt, then a stride-1 screen of inv. 6019 520-548 / 558-600, ~$2
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII has no decipherment or key note near the Brederode entries (OBRED-DP)
- [ ] key-rebuild: the 1619 glossed pairs clear their own per-unit gate (OBRED-TRY, statistic B); decode_key --try ran with power 0/7 (non-test); next: band-interval decode with a held-out leaf check and shuffled-band control, then no. 92/187 graded M, ~$3
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv 59/59 (OBRED-187); ciphertext_556.tsv two blind passes, 58 of 81 H-read after the 555 L15 second pass (OBRED-556, OBRED-552); the three gloss conflicts re-seen at 5000 px, eye + blind, none settled (OBRED-TRY)
- [x] retry: Den Tex (abridged edition) read twice; brievenboek 11851 596-733 and 11852 2-104 completed with controls
Verdict: keep going: 3 internal gaps; inv. 6019 549-551 hold no key (549 = end of a French piece on Ferdinand's deposition in Bohemia; 550r-552 = the 8 Oct 1619 letter, prose only); cheapest next: the band-interval decode with a held-out leaf check (~$3), and the Resolutiën S.G. Oct 1619 plus a stride-1 screen of inv. 6019 for the separately filed key (~$2)

## OBRED-KEYHUNT (15 Oct 2026, 08:57-09:1x UTC by date -u, account 2, Opus; for LANE DEFAULT-A2-0810-15)

Brief: the reformed cipher's "instructie ende sleutel" named in the Heidelberg letter of 8 Oct 1619 (OBRED-552): Resolutiën der
Staten-Generaal 1619 first (receipt of the key, or where it was laid), then a stride-1 screen of inv. 6019 from 548 backward and 558 forward
at the smallest size that shows a numeral table. A screen, not a reading: no PREREG, nothing scored.

- Prior-work step: `prior_work.py ... --item-spec 'Resolutien S.G. nieuwe reeks 1619 Oct 17-28; NL-HaNA 1.01.02 inv. 6019 scans 520-548,
  558-600 key leaf screen' --step-type read` exit 4 (own claim LEAD, target-level LOOK, 2 UNCHECKED, 2 UNCHECKED-NET); the four non-net rows
  recorded CLEAR in `prior-work.tsv` (adhoc-ea1bef).
- **Resolutiën der Staten-Generaal, nieuwe reeks, Deel 4 (1619-1620, RGP GS 176)**, Huygens retroboeken/statengeneraal `source_id=4`
  (`page_view_navigation` confirms 4 = 1619-1620 NR). 18 requests to resources.huygens.knaw.nl, all 200, >= 3 s apart, take/release in ROOM.
  Searches in Deel 4: `Brederode` 131 hits (first 20 read as snippets: positive control, the route returns his 1619 letters in date order),
  `sleutel` 1 (p.667, a door key for Falckenburgh and Van Herdersum, off-topic), `cijffer` 0, `cijfer` 2, `ontcijferen` 3, `ontcijferd` 0,
  `chiffre` 0, `Rusdorff` 0 (the edition spells him Ransdorff/Ruestorff), `Oggersheim` 2. OCR pages read in full: pp.266, 272, 273, 275, 276,
  286, 584, 615. What they say (the printed regest's words; read from the OCR text, H for what the edition prints):
  - **p.266, 11 Oct 1619, res. 1779** (end): "Ontvangen een brief van Brederode, dd. Heidelberg 2 okt. [c: S.G. 6019 (orig.)]. Maurits
    presenteert nog een door hem van Brederode ontvangen memorie, die hij heeft laten ontcijferen. Hij verzoekt haar geheim te houden. Daar
    het cijfer ongeschikt bevonden wordt, wordt Z. Ex. verzocht een beter op te stellen." So the States General had Brederode's cipher read
    on Maurits's side (Maurits "had it deciphered"), judged the cipher unfit, and asked Maurits to draw up a better one -- three days after
    Brederode wrote on 8 Oct that he had reformed it himself. No archive reference is given for the memorie or its decipherment.
  - **p.272, 17 Oct 1619, res. 1832**: "Brederode bericht in zijn beide brieven dd. Heidelberg 8 okt. [a] het vertrek van de keurvorst ...
    naar de Overpalts"; note 1832a "In S.G. 6019 brieven van 5 en 8 okt. (orig.)". No word of a key, cipher or instruction received.
  - p.272-273, 18 Oct, res. 1835: Johan Joachim van Ransdorff (Rusdorff), the Elector's councillor and bearer named in the 8 Oct letter,
    has audience; nothing on a cipher.
  - **p.286, 28 Oct 1619, res. 1921b**: the 14 Oct letter received, "S.G. 6019 (orig. dd. Oggersheim 14 okt.)" -- the ciphered letter on
    scans 554-557 (OBRED-556); no decipherment or key note.
  - pp.584, 615 (Sept-Oct 1620): Maurits again has Palatine and Hessian letters deciphered for the States General ("Z. Ex. heeft alles
    laten ontcijferen"); context only -- the decipherment of incoming Palatine cipher sat with Maurits's household, not with the griffie.
- **inv. 6019 stride-1 screen** (NL-HaNA 1.01.02 inv. 6019, METS 1ebb4182-...): 25 requests to service.archief.nl (METS + 24 scans at 1000
  px), all 200, >= 3.1 s apart, take/release in ROOM; sha1s in `images/manifest.json` (`obred_keyhunt`), `screen_tools/regen_keyhunt.sh`
  re-derives them; no image committed. By eye at 1000 px (M), as contact sheets of six; **no numeral table, alphabet, nomenclator, numeral
  group or interlinear gloss on any of the 24 scans.**
  - 533: a copy of a Brederode letter ending "Heydelberg desen 5 october 1619", signed (no name visible on this copy).
  - 534 left: address leaf with seal; 534 right-535: the 5 Oct 1619 letter (docket at the top right unread), ending "Heydelberg desen 5
    october", signed "P van Brederode". So 533 and 534-535 are two copies of the 5 Oct letter that res. 1832 cites.
  - 536 left: an address leaf with seal; 536 right-549: a French tract, "Raisons et considerations pour lesquelles ... Ferdinand ...
    Boheme ..." with its own foliation (3-7 on 538-542), ending on 549 (OBRED-549's "French piece"): a printed-manifesto draft on the
    Bohemian deposition, filed with the 5 Oct letter (M).
  - 558 left: address leaf; 558 right-561: a letter (docket unread at this size); 562-563: the opening of a letter docketed "d. 22 Oct.
    1619 / R. 4 Nov." (M), dated "22 octob. 1619" on 562 left -- 563 is a re-scan of the same opening with a colour card; 564-565 continue a
    copy of the 558-560 text. So 558-565 are two copies of one later letter, prose only (M).
- Where it was not found, and the limits: no receipt of an "instructie ende sleutel" is minuted in the S.G. resolutions of 11-28 Oct 1619
  (searches above, eight pages read); no key leaf on inv. 6019 533-552 or 554-565 (this pass with OBRED-549, OBRED-552, OBRED-556). Not looked
  at: inv. 6019 at stride 1 before 533 (where the 2 Oct 1619 letter of res. 1779 should sit, perhaps with the memorie Maurits had deciphered)
  and after 565; Maurits's own papers (the decipherment and the "better" cipher of res. 1779 were his to make); the S.G. outgoing minutes
  (S.G. 6051 and the Brederode minuut files) for a key sent back to Heidelberg. One reader at 1000 px; dockets mostly unread at that size.

## Remaining gaps (OBRED-KEYHUNT, 15 Oct 2026)
Read so far: unmeasured for no. 92 and 187 (nothing applied to them); inv. 6019 scans 555-556 carry 81 groups (58 H-read) with 45 C-graded period glosses; overlap with no. 92/187 clears its control (OBRED-556); the 14 Oct 1619 letter is complete on 554-557 (OBRED-552) and the 8 Oct 1619 letter on 550-552, prose only (OBRED-549); the glossed letters rise with the code value (rho 0.96, p < 1e-4, OBRED-TRY); the S.G. resolution of 11 Oct 1619 records that Maurits had a Brederode memorie deciphered and was asked to draw up a better cipher (OBRED-KEYHUNT)
- no. 92 and the 187 postscript with the 1619 glossed values - blocker: not-attempted; decode_key --try had power 0/7 on the glossed letter itself (OBRED-TRY), so its verdicts are non-tests; next: a band-interval decode (each letter's code range from the 1619 glosses, alphabetical order) with a pre-registered held-out check -- predict one leaf's glossed letters from the other leaf's bands against a shuffled-band control -- then apply to no. 92/187 graded M, ~$3
- the 1619 key, the deciphered memorie and the "instructie ende sleutel" - blocker: not-attempted; not minuted in the S.G. resolutions of 11-28 Oct 1619 beyond res. 1779 (memorie deciphered by Maurits, cipher judged unfit, Maurits asked for a better one) and not on inv. 6019 533-565 (OBRED-KEYHUNT, OBRED-549, OBRED-552); next: inv. 6019 stride-1 from 532 backward to the 2 Oct 1619 letter (res. 1779c, S.G. 6019 orig.) for the memorie and any decipherment filed with it, ~15 NA requests at 1000 px, ~$1.5
- the later liassen NA 1.01.02 inv. 6020-6024 and the 6019 stride-1 fill after 565 - blocker: not-attempted; outside this brief, the 1619 letter shows the agent still used the 1604-05 code list (OBRED-556); next: a stride-3 screen of inv. 6020 (~$4)
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 and 21 Feb 1605 letters - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder done (OBRED-SG, OBRED-11851, OBRED-641, OBRED-11851B, OBRED-11852A): no numeral block, no Brederode, Stettin or Heidelberg heading (M)

## Escalation (OBRED-KEYHUNT, 15 Oct 2026)
- [x] siblings: scan 187 shares 26 values with no. 92 (OBRED-187); inv. 6019 scans 555-556 (Oggersheim, 14 Oct 1619) share 42 values with no. 92/187, clearing the shuffled-code control (OBRED-556); the letter's start (554) carries no groups (OBRED-552)
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187); the 1619 letter's prose and margin summaries read in part (OBRED-556); 533-554 and 558-565 seen by eye (OBRED-552, OBRED-549, OBRED-KEYHUNT)
- [ ] known-keys: the 10 Aug 1598 Van Aerssen slip, Buzanval inv. 2028, DECODE 1600s and Palatine/Hessian keys screened (R10-OBRED98, R9-OBRED4, OLD-DKEY, R8-OBRED2, R9-OBRED3); the 1619 "instructie ende sleutel" is not on inv. 6019 533-565 and its receipt is not minuted in the S.G. resolutions of 11-28 Oct 1619, which record a Brederode memorie deciphered by Maurits (res. 1779, 11 Oct) (OBRED-KEYHUNT); next: inv. 6019 stride-1 from 532 backward to the 2 Oct 1619 letter, ~$1.5
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII has no decipherment or key note near the Brederode entries (OBRED-DP); Resolutiën S.G. NR 4 (1619-1620) has res. 1779 and no key receipt (OBRED-KEYHUNT)
- [ ] key-rebuild: the 1619 glossed pairs clear their own per-unit gate (OBRED-TRY, statistic B); decode_key --try ran with power 0/7 (non-test); next: band-interval decode with a held-out leaf check and shuffled-band control, then no. 92/187 graded M, ~$3
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv 59/59 (OBRED-187); ciphertext_556.tsv two blind passes, 58 of 81 H-read after the 555 L15 second pass (OBRED-556, OBRED-552); the three gloss conflicts re-seen at 5000 px, eye + blind, none settled (OBRED-TRY)
- [x] retry: Den Tex (abridged edition) read twice; brievenboek 11851 596-733 and 11852 2-104 completed with controls
Verdict: keep going: 3 internal gaps; no key leaf on inv. 6019 533-565 and no key receipt in the S.G. resolutions of 11-28 Oct 1619, but res. 1779 (11 Oct) records a Brederode memorie deciphered by Maurits and a better cipher asked of him; cheapest next: inv. 6019 stride-1 from 532 back to the 2 Oct 1619 letter for that memorie (~$1.5), and the band-interval decode (~$3)

## OBRED-BAND (15 Oct 2026, 09:07-09:1x UTC by date -u, account 2, Opus; for LANE DEFAULT-A2-0810-15)

Brief: band-interval decode of no. 92 / the scan-187 postscript from the 1619 glossed pairs, with a held-out leaf check against a
shuffled-band control and a power check at the target's own counts; names left as codes; never key.tsv. Disk and CPU only, 0 requests.

- Prior-work step: `prior_work.py ... --step-type decode` exit 4 (own claim LEAD, LOOK, 2 UNCHECKED, 2 UNCHECKED-NET); the four non-net
  rows recorded CLEAR in `prior-work.tsv` (adhoc-34c751). No earlier band decode; OBRED-TRY ran --try only.
- PREREG `obred187/PREREG-OBREDBAND.md` pushed in its own commit (8e9bcd573) before any statistic. Pairs = OBRED-TRY's rule (C,
  single letter, i/j u/v/w folded): 555 has 30, 556 has 11. Script `obred187/band/band.py` (`--check` up to date), output `band_gate.json`.
- **Power (synthetic, assumed design):** alphabetical homophonic list on 1..587, band widths ~ nl16 letter frequency, train 30 / test 11,
  1,000-draw shuffled null, 200 simulations: power 1.00 (gate 0.70). At the application's own count (41 pooled pairs -> 180 tokens):
  one-letter intervals 41.9% of tokens, all correct, interval hit 1.00 -- an upper bound, since the synthetic list has no transcription
  or gloss error and perfectly clean bands.
- **Held-out check, primary (fit 555, score 556): PASS.** S 0.171 (hit 8/11 = 0.727, mean width 3.45, nearest-code exact 0.455) vs
  shuffled-band null mean 0.034, p95 0.104, max 0.416, p 0.0107 (10,000 draws, seed 1619). Reverse (fit 556, score 555; not gated):
  S 0.199 (hit 0.80, width 3.9) vs p95 0.141, p 0.0033. H-read groups only (not gated): S 0.191 (n 7) vs p95 0.117, p 0.0073.
  The three held-out misses are 415 (s, bands give r), 337 (p, bands give o) -- two of the logged rule-4 conflicts, which score as
  misses by construction -- and 458 (glossed v "n shape", between 457 t and 459 t on 555).
- **Application (as registered, grade M): `obred187/band/reading_92_187.tsv`.** 180 tokens: 37 name codes (588-751) left as codes;
  72 (40.0%) fall in a one-letter interval, 115 (63.9%) in an interval of width <= 2, the rest wider (codes above 530 get n..z because the
  M-group 530 carries an n gloss). Expected accuracy of the one-letter calls on the real data is below the synthetic 1.00: the real held-out
  hit rate is 0.73-0.80, and band edges (r/s, o/p, d/e) are where the 1619 glosses themselves conflict. Each token is an interval of
  letters, not a reading; no word or sense is claimed from the interval string, and nothing went into key.tsv.
- Where it was not found, and the limits: one statistic and one predictor (nearest-glossed-neighbour interval); band edges are the
  weak point; the 1619 list is assumed to be the 1604-05 list (OBRED-556's overlap gate); no language model or segmentation was applied
  to the intervals (that would be the next instrument, and it needs its own control).

## Remaining gaps (OBRED-BAND, 15 Oct 2026)
Read so far: no. 92 and the 187 postscript as band intervals only (M): 72 of 180 tokens (40.0%) one-letter, 115 (63.9%) width <= 2, 37 name codes (OBRED-BAND; held-out check fit 555 -> 556 S 0.171 vs shuffled-band p95 0.104, p 0.011, power 1.00); inv. 6019 scans 555-556 carry 81 groups (58 H-read) with 45 C-graded period glosses; the S.G. resolution of 11 Oct 1619 records that Maurits had a Brederode memorie deciphered (OBRED-KEYHUNT)
- no. 92 and the 187 postscript beyond letter intervals - blocker: not-attempted; band intervals pass a held-out check but give letters, not words; next: a constrained segmentation of the interval strings (each token's letter set, nl16 lexicon, tools/segmenter.py or decode_key --consistency --auto-segment) with a matched control on a synthetic band text at the same counts and a shuffled-interval null, PREREG first, graded M, ~$3
- the 1619 key, the deciphered memorie and the "instructie ende sleutel" - blocker: not-attempted; not minuted in the S.G. resolutions of 11-28 Oct 1619 beyond res. 1779 and not on inv. 6019 533-565 (OBRED-KEYHUNT, OBRED-549, OBRED-552); next: inv. 6019 stride-1 from 532 backward to the 2 Oct 1619 letter, ~15 NA requests at 1000 px, ~$1.5
- the later liassen NA 1.01.02 inv. 6020-6024 and the 6019 stride-1 fill after 565 - blocker: not-attempted; outside this brief; next: a stride-3 screen of inv. 6020 (~$4)
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 and 21 Feb 1605 letters - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder done (OBRED-SG, OBRED-11851, OBRED-641, OBRED-11851B, OBRED-11852A): no numeral block, no Brederode, Stettin or Heidelberg heading (M)

## Escalation (OBRED-BAND, 15 Oct 2026)
- [x] siblings: scan 187 shares 26 values with no. 92 (OBRED-187); inv. 6019 scans 555-556 (Oggersheim, 14 Oct 1619) share 42 values with no. 92/187, clearing the shuffled-code control (OBRED-556); the letter's start (554) carries no groups (OBRED-552)
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187); the 1619 letter's prose and margin summaries read in part (OBRED-556); 533-554 and 558-565 seen by eye (OBRED-552, OBRED-549, OBRED-KEYHUNT)
- [ ] known-keys: the 10 Aug 1598 Van Aerssen slip, Buzanval inv. 2028, DECODE 1600s and Palatine/Hessian keys screened (R10-OBRED98, R9-OBRED4, OLD-DKEY, R8-OBRED2, R9-OBRED3); the 1619 "instructie ende sleutel" is not on inv. 6019 533-565 and its receipt is not minuted in the S.G. resolutions of 11-28 Oct 1619 (OBRED-KEYHUNT); next: inv. 6019 stride-1 from 532 backward to the 2 Oct 1619 letter, ~$1.5
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII has no decipherment or key note near the Brederode entries (OBRED-DP); Resolutiën S.G. NR 4 (1619-1620) has res. 1779 and no key receipt (OBRED-KEYHUNT)
- [ ] key-rebuild: band-interval decode passes its held-out leaf check (S 0.171 vs p95 0.104, p 0.011, power 1.00) and gives no. 92/187 as letter intervals, 40.0% one-letter (OBRED-BAND); next: constrained segmentation of the interval strings with a synthetic-band control and shuffled-interval null, ~$3
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv 59/59 (OBRED-187); ciphertext_556.tsv two blind passes, 58 of 81 H-read after the 555 L15 second pass (OBRED-556, OBRED-552); the three gloss conflicts re-seen at 5000 px, eye + blind, none settled (OBRED-TRY)
- [x] retry: Den Tex (abridged edition) read twice; brievenboek 11851 596-733 and 11852 2-104 completed with controls
Verdict: keep going: 3 internal gaps; band intervals from the 1619 glosses pass a held-out leaf check (fit 555 -> 556 S 0.171 vs shuffled-band p95 0.104, p 0.011, power 1.00) and put 40.0% of no. 92/187's 180 tokens in a one-letter interval (M); cheapest next: inv. 6019 stride-1 from 532 back to the 2 Oct 1619 letter (~$1.5), then a constrained segmentation of the interval strings with its own control (~$3)

## OBRED-MEM (15 Oct 2026, 09:16-09:2x UTC by date -u, account 2, Opus; for LANE DEFAULT-A2-0810-15)

Brief: the Brederode memorie Maurits had deciphered (res. 1779, 11 Oct 1619): inv. 6019 at stride 1 from 532 backward to the 2 Oct 1619
letter, for the memorie and any decipherment filed with it. A screen, not a reading: no PREREG, nothing scored.

- Prior-work step: `prior_work.py ... --item-spec 'NL-HaNA 1.01.02 inv. 6019 scans 500-532 memorie deciphered by Maurits (res. 1779)
  screen' --step-type read` exit 4 (own claim LEAD, LOOK, 2 UNCHECKED, 2 UNCHECKED-NET); the four non-net rows recorded CLEAR in
  `prior-work.tsv` (adhoc-71518e).
- **inv. 6019 stride-1 screen** (NL-HaNA 1.01.02 inv. 6019, METS 1ebb4182-...): 20 requests to service.archief.nl (METS + 18 scans 532-515
  at 1000 px + 530 at 3000 px for the postscript), all 200, >= 3.1 s apart, take/release in ROOM; sha1s in `images/manifest.json`
  (`obred_mem`), `screen_tools/regen_mem.sh` re-derives them; no image committed. By eye (M), contact sheets of six: **no numeral table,
  alphabet, nomenclator, numeral group or interlinear gloss on any of the 18 scans.**
  - 532: left an address leaf with seal; right the opening of a letter docketed "d. 5 Oct 1619" (the 5 Oct letter continues on 533).
  - 531: blank opening (back of the 2 Oct letter's last leaf).
  - **528 right-530: the 2 Oct 1619 letter of res. 1779**: 528 left address leaf with seal, 528 right opening docketed "d. 2 Oct / r. 11 Oct
    1619" (received the day of res. 1779), 530 right ending "Uyt Heydelberg desen 2en octobre 1619", signed "P van Brederode"; a
    postscript in the left margin of 530 (read at 3000 px, M) says the Elector had asked whether he had orders to go to Bohemia and he had
    answered that he had none yet -- nothing on a memorie or a cipher. Prose only; no enclosure filed after it (531 blank, then 532).
  - 522 right-526: a letter docketed "d. 26 Sept / r. 7 Oct 1619" (522 left address leaf with seal), prose; 526 right ends dated and signed
    with a marginal postscript (unread at this size).
  - 521: the end of a letter "Francfort desen 23 Septembre 1619", signed P van Brederode; 520: a letter in a rough, different hand with an
    address leaf; 515-518: a Brederode letter ending on 518 "... 22 Septembre 1619", signed. All prose (M).
- Where it was not found, and the limits: not on inv. 6019 515-532 (this pass) nor 533-565 (OBRED-KEYHUNT, OBRED-549, OBRED-552). Res. 1779
  says Maurits presented a memorie "door hem van Brederode ontvangen" -- sent to Maurits, not to the States General -- so the S.G. letter
  liasse need not hold it. Not looked at: the 2 Oct letter's text for a mention of the memorie (read only at its opening, end and
  postscript); Maurits's own papers (Koninklijk Huisarchief); the S.G. secrete liassen for Oct 1619; inv. 6019 before 515. One reader at
  1000 px; dockets read only where enlarged. 5 of 25 requests unused.

## Remaining gaps (OBRED-MEM, 15 Oct 2026)
Read so far: no. 92 and the 187 postscript as band intervals only (M): 72 of 180 tokens (40.0%) one-letter, 115 (63.9%) width <= 2, 37 name codes (OBRED-BAND; held-out check fit 555 -> 556 S 0.171 vs shuffled-band p95 0.104, p 0.011, power 1.00); inv. 6019 scans 555-556 carry 81 groups (58 H-read) with 45 C-graded period glosses; the S.G. resolution of 11 Oct 1619 records that Maurits had a Brederode memorie deciphered (OBRED-KEYHUNT)
- no. 92 and the 187 postscript beyond letter intervals - blocker: not-attempted; band intervals pass a held-out check but give letters, not words; next: a constrained segmentation of the interval strings (each token's letter set, nl16 lexicon, tools/segmenter.py or decode_key --consistency --auto-segment) with a matched control on a synthetic band text at the same counts and a shuffled-interval null, PREREG first, graded M, ~$3
- the 1619 key, the deciphered memorie and the "instructie ende sleutel" - blocker: not-attempted; not minuted in the S.G. resolutions of 11-28 Oct 1619 beyond res. 1779 and not on inv. 6019 515-565 (OBRED-MEM, OBRED-KEYHUNT, OBRED-549, OBRED-552); the 2 Oct 1619 letter is on 528-530 (docket "d. 2 Oct / r. 11 Oct 1619") with no enclosure filed after it (531 blank, 532 opens the 5 Oct letter); res. 1779 says Maurits presented a memorie he had received from Brederode himself, so it was likely kept with Maurits's papers; next: read the 2 Oct letter 528-530 for any mention of the memorie (3 scans at 3000 px, disk-light, ~$1.5), then a catalogue check of Maurits's papers (Koninklijk Huisarchief) and the S.G. secrete liassen for Oct 1619, ~$1
- the later liassen NA 1.01.02 inv. 6020-6024 and the 6019 stride-1 fill after 565 - blocker: not-attempted; outside this brief; next: a stride-3 screen of inv. 6020 (~$4)
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 and 21 Feb 1605 letters - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder done (OBRED-SG, OBRED-11851, OBRED-641, OBRED-11851B, OBRED-11852A): no numeral block, no Brederode, Stettin or Heidelberg heading (M)

## Escalation (OBRED-MEM, 15 Oct 2026)
- [x] siblings: scan 187 shares 26 values with no. 92 (OBRED-187); inv. 6019 scans 555-556 (Oggersheim, 14 Oct 1619) share 42 values with no. 92/187, clearing the shuffled-code control (OBRED-556); the letter's start (554) carries no groups (OBRED-552)
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187); the 1619 letter's prose and margin summaries read in part (OBRED-556); 515-554 and 558-565 seen by eye (OBRED-MEM, OBRED-552, OBRED-549, OBRED-KEYHUNT)
- [ ] known-keys: the 10 Aug 1598 Van Aerssen slip, Buzanval inv. 2028, DECODE 1600s and Palatine/Hessian keys screened (R10-OBRED98, R9-OBRED4, OLD-DKEY, R8-OBRED2, R9-OBRED3); the 1619 "instructie ende sleutel" and the memorie Maurits had deciphered (res. 1779) are not on inv. 6019 515-565 and the key's receipt is not minuted in the S.G. resolutions of 11-28 Oct 1619 (OBRED-MEM, OBRED-KEYHUNT); next: read the 2 Oct 1619 letter (528-530) for the memorie, ~$1.5, then Maurits's papers (KHA) and the S.G. secrete liassen, ~$1
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII has no decipherment or key note near the Brederode entries (OBRED-DP); Resolutiën S.G. NR 4 (1619-1620) has res. 1779 and no key receipt (OBRED-KEYHUNT)
- [ ] key-rebuild: band-interval decode passes its held-out leaf check (S 0.171 vs p95 0.104, p 0.011, power 1.00) and gives no. 92/187 as letter intervals, 40.0% one-letter (OBRED-BAND); next: constrained segmentation of the interval strings with a synthetic-band control and shuffled-interval null, ~$3
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv 59/59 (OBRED-187); ciphertext_556.tsv two blind passes, 58 of 81 H-read after the 555 L15 second pass (OBRED-556, OBRED-552); the three gloss conflicts re-seen at 5000 px, eye + blind, none settled (OBRED-TRY)
- [x] retry: Den Tex (abridged edition) read twice; brievenboek 11851 596-733 and 11852 2-104 completed with controls
Verdict: keep going: 3 internal gaps; inv. 6019 515-532 hold no cipher memorie, decipherment or key (OBRED-MEM); the 2 Oct 1619 letter of res. 1779 is on 528-530, prose, with nothing filed after it; band intervals put 40.0% of no. 92/187's 180 tokens in a one-letter interval (M); cheapest next: read the 2 Oct letter for the memorie (~$1.5), and a constrained segmentation of the interval strings with its own control (~$3)

## OBRED-OCT2 (15 Oct 2026, 09:33-09:4x UTC by date -u, account 2, Opus; for LANE DEFAULT-A2-0810-15)

Brief: read the 2 Oct 1619 letter of res. 1779 (inv. 6019 scans 528-530) for any mention of a memorie, cipher or sleutel; then catalogue
lookups only (S.G. secrete series for 1619; Maurits's papers at the Koninklijk Huisarchief) for where a deciphered Brederode memorie would
be filed. A reading of one prose letter, no PREREG, nothing scored.

- Prior-work step: `prior_work.py ... --item-spec 'NL-HaNA 1.01.02 inv. 6019 scans 528-530 ...' --step-type read` exit 4 (own claim LEAD,
  LOOK, 2 UNCHECKED, 2 UNCHECKED-NET); the four non-net rows recorded CLEAR in `prior-work.tsv` (adhoc-834178).
- Requests: service.archief.nl 4 (METS + scans 528, 529, 530 at 3000 px), all 200, >= 3.1 s apart, take/release in ROOM; sha1s 9047ca14 /
  06d2c0d9 / 6a742012, `screen_tools/regen_oct2.sh` re-derives them; no image committed. Catalogue: nationaalarchief.nl 2 (1.01.02 EAD
  XML 22.7 MB, inv. 4562 item page), koninklijkeverzamelingen.nl 2 (A13 page; `A13.ead.pdf` guess 404), web search 2.
- **The letter, read by eye (M, one reader at 3000 px, page crops).** 528 right: "Nader mijne voorgaenden vanden 26en ende 28en des
  voorleden maents, waer van de copie hier bij gaen" -- copies of the 26 and 28 Sept letters went with it -- then his return from Frankfurt
  to Heidelberg, the Electoral court (the Dowager, Duke Ludwig, Duke Johann of Zweibrücken, the Margraves of Ansbach and Baden, the Duke of
  Württemberg), and his congratulation on the Bohemian election. 529 left-530 right: the news (Anhalt general of the Bohemian forces;
  Achatius von Dohna and the Anhalt hofmeister sent to Prague; Spinola, Vaudémont, Spanish and Italian troops via Savoy; Saxe-Weimar and
  Denmark's horse; Mühlhausen and Nuremberg; Buquoy, Bethlen Gabor, Leopold, Ferdinand at Munich; Doncaster's embassy; Oñate), ending
  "Uyt Heydelberg desen 2en octobre 1619", signed P van Brederode, with the marginal postscript OBRED-MEM read.
- **The cipher passage, 529 left lines 12-22 (M, read by eye; spelling as seen, doubtful letters not marked):** "Wat hier onder bij mij
  daer van vernomen es geworden, hebb' ick mettet cyffer van sijne Ex.tie aende selven geschreven; alsoo men mij hier voorts heeft
  geadvyseert, dat men sich met mijn cyfer (: twelcke in des Advocaets Barnevelt handen es geweest :) niet en konde behelpen; U Hoog Mog.
  onderdanichst versoeckende mij te willen doen berichten, off tselve noch voorhanden sij, ende bijde selve cyffers gebruijckt kan werden,
  ofte niet, om daer in te voorsien; gelijck het vannoden schijnt, alsoomen aenvanckt aen verscheyden oorden de pacquetten t'intercepteren."
  In plain words (M): what he had learned there he wrote **to Maurits in Maurits's own cipher**; he had been told that **his own cipher, "which
  had been in the Advocate Barnevelt's hands", could not be relied on**; he asks the States General whether that cipher is still at hand and
  whether the same ciphers can still be used, "since they are beginning to intercept the packets in various places". Nothing else on the
  three scans mentions a memorie, cipher or sleutel.
- What this settles about res. 1779 (inference, I): the "memorie" Maurits presented on 11 Oct is most likely the enclosure Brederode wrote
  to him in **Maurits's cipher** on or about 2 Oct, not a text in Brederode's own (no. 92) cipher; the S.G.'s finding that "het cijfer
  ongeschikt" is the answer to his question about **his own cipher, last held by Oldenbarnevelt** (arrested Aug 1618), and the "better" one
  Maurits was asked to draw up is the replacement, matching Brederode's 8 Oct reform. So the deciphered memorie, if kept, is a Maurits-cipher
  text and its key is Maurits's, not the no. 92 key; the **no. 92 key's last stated home is Oldenbarnevelt's papers**.
- Catalogue lookups (where it was not found):
  - NA 3.01.14 (Oldenbarnevelt) was already grepped wide (R9-NAKEY, 6 Oct: cijfer/cyffer/sleutel/geheimschrift/ontcijfer...): no Brederode
    key item; only Buzanval (inv. 2028) and Van Aerssen (2016) keys. Not re-fetched.
  - NA 1.01.02 EAD (fresh copy, grepped per `<c>`): the seized-papers / process series **inv. 9450-9460** ("Bijlagen dienende in de zaak
    tegen Johan van Oldenbarnevelt 1607-1618", 9459, 7 stukken; letters to Caron, Van Aerssen, Langerak, Ledenberg 9451-9454) -- titles
    name no Brederode and no cipher; **secrete resoluties inv. 4562** (Dec 1615 - Dec 1634, 290 scans, availability DIGITALIZED) holds the
    secret register for Oct 1619, not read; no 1619 item in the Secrete Kas Duitsland (12584.x items found are 1615 Hanze treaties and later);
    "Brederode" in the EAD hits only the 6016-6024 liassen and unrelated Brederodes. No item titled for a cipher of 1618-1620.
  - Koninklijk Huisarchief: Maurits's archive is **A13** (1567-1625 (1632), 2.5 m; koninklijkeverzamelingen.nl/archief/a/a13); its inventory
    loads by script only and no EAD PDF is served at the C01-style path (404); access is by research request to the KHA. Not searched inside.
- Limits: one reader; the passage read at 3000 px from page crops, all M; the S.G. secrete resoluties inv. 4562 and A13's inventory not read.

## Remaining gaps (OBRED-OCT2, 15 Oct 2026)
Read so far: no. 92 and the 187 postscript as band intervals only (M): 72 of 180 tokens (40.0%) one-letter, 115 (63.9%) width <= 2, 37 name codes (OBRED-BAND); inv. 6019 scans 555-556 carry 81 groups (58 H-read) with 45 C-graded period glosses; the 2 Oct 1619 letter says Brederode's own cipher had been in Oldenbarnevelt's hands and that he wrote his news to Maurits in Maurits's cipher (OBRED-OCT2, M)
- no. 92 and the 187 postscript beyond letter intervals - blocker: not-attempted; band intervals pass a held-out check but give letters, not words; next: a constrained segmentation of the interval strings (OBRED-SEG brief, wave 5) with its matched control and shuffled-interval null, PREREG first, graded M, ~$3
- the no. 92 key ("mijn cyfer ... in des Advocaets Barnevelt handen") - blocker: not-attempted; 3.01.14 grepped wide (R9-NAKEY) with no Brederode key; the 1.01.02 process series 9450-9460 titles name no cipher; next: a stride screen of NA 1.01.02 inv. 9459 (Bijlagen in de zaak tegen Oldenbarnevelt 1607-1618, 7 stukken) and the S.G. secrete resoluties inv. 4562 at Oct 1619 for the cipher's fate, ~$2
- the deciphered memorie of res. 1779 (a Maurits-cipher text, OBRED-OCT2 inference) - blocker: needs-physical-access; KHA A13 (Maurits) inventory not served to scripts and the archive is research-request only; owner-side step: a KHA research request, not queued
- the later liassen NA 1.01.02 inv. 6020-6024 and the 6019 stride-1 fill after 565 - blocker: not-attempted; outside this brief; next: a stride-3 screen of inv. 6020 (~$4)
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 and 21 Feb 1605 letters - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder done (OBRED-SG, OBRED-11851, OBRED-641, OBRED-11851B, OBRED-11852A): no numeral block, no Brederode, Stettin or Heidelberg heading (M)

## Escalation (OBRED-OCT2, 15 Oct 2026)
- [x] siblings: scan 187 shares 26 values with no. 92 (OBRED-187); inv. 6019 scans 555-556 (Oggersheim, 14 Oct 1619) share 42 values with no. 92/187, clearing the shuffled-code control (OBRED-556); the letter's start (554) carries no groups (OBRED-552)
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187); the 1619 letter's prose and margin summaries read in part (OBRED-556); 515-554 and 558-565 seen by eye (OBRED-MEM, OBRED-552, OBRED-549, OBRED-KEYHUNT); the 2 Oct 1619 letter 528-530 read in full (OBRED-OCT2)
- [ ] known-keys: the 10 Aug 1598 Van Aerssen slip, Buzanval inv. 2028, DECODE 1600s and Palatine/Hessian keys screened (R10-OBRED98, R9-OBRED4, OLD-DKEY, R8-OBRED2, R9-OBRED3); the 2 Oct 1619 letter puts Brederode's own cipher last in Oldenbarnevelt's hands (OBRED-OCT2); next: NA 1.01.02 inv. 9459 and secrete resoluties inv. 4562 (Oct 1619), ~$2
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII has no decipherment or key note near the Brederode entries (OBRED-DP); Resolutiën S.G. NR 4 (1619-1620) has res. 1779 and no key receipt (OBRED-KEYHUNT)
- [ ] key-rebuild: band-interval decode passes its held-out leaf check (S 0.171 vs p95 0.104, p 0.011, power 1.00) and gives no. 92/187 as letter intervals, 40.0% one-letter (OBRED-BAND); next: constrained segmentation of the interval strings with a synthetic-band control and shuffled-interval null, ~$3
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv 59/59 (OBRED-187); ciphertext_556.tsv two blind passes, 58 of 81 H-read after the 555 L15 second pass (OBRED-556, OBRED-552); the three gloss conflicts re-seen at 5000 px, eye + blind, none settled (OBRED-TRY)
- [x] retry: Den Tex (abridged edition) read twice; brievenboek 11851 596-733 and 11852 2-104 completed with controls
Verdict: keep going: 3 internal gaps; the 2 Oct 1619 letter (528-530) says Brederode wrote to Maurits in Maurits's cipher and that his own cipher had been in Oldenbarnevelt's hands (M), so the res. 1779 memorie is likely a Maurits-cipher text (KHA A13, research request) and the no. 92 key's last stated home is Oldenbarnevelt's papers; cheapest next: NA 1.01.02 inv. 9459 + secrete resoluties inv. 4562 at Oct 1619 (~$2), and the constrained segmentation (~$3)

## OBRED-SEG (15 Oct 2026, 09:33-09:5x UTC by date -u, account 2, Opus; for LANE DEFAULT-A2-0810-15)

Brief: constrained segmentation of OBRED-BAND's no. 92/187 letter intervals into Dutch words, against a shuffled-band null (>= 200) and a
synthetic Dutch control at no. 92's length that must segment above gate; grade M unless the control licenses S; never key.tsv. Disk only,
0 requests.

- Prior-work step: `prior_work.py ... --step-type decode` exit 4 (LEAD = OBRED-OCT2's target-level claim, a 1619 archive lookup; LOOK;
  2 UNCHECKED; 2 UNCHECKED-NET); the four non-net rows recorded CLEAR (adhoc-2f5f27). No earlier segmentation.
- PREREG `obred187/PREREG-OBREDSEG.md` pushed in its own commit (4f729ee4c) before any statistic; it discloses that this worker had
  guessed "gelt" for 146 110 252 433 by eye beforehand. Corpus: nl16 (1569-1589 prose) -- no nl17 exists; era-near (16-36 years before
  1605), register-mismatched (prose, not letters). Script `obred187/seg/seg.py` (`--check`), outputs `seg_gate.json`, `seg_92_187.tsv`.
- Decoder: DP per letter sub-run (13 sub-runs, 143 letter tokens; runs split at name codes 588-751), nl16 unigram cost, +1.0 per letter
  one alphabet step outside its interval, 4.0 per unknown letter. Statistic I = sum log2(23/width) over tokens inside recovered words
  (lexicon words >= 4 letters).
- **Synthetic control (registered gate at e = 0.25): PASS.** 20 sims, held-out nl16 file (coor001boev01), alphabetical list 1..587,
  41 pool pairs, the target's sub-run lengths: beats its own shuffled-band null 20/20, word precision 0.577 (n 487), recall 0.590,
  precision for >= 5 letters 0.610, interval hit 0.92. e = 0: 20/20, precision 0.530. **Not registered, added after the registered run
  to bracket the real held-out interval hit (0.73-0.80; rule 3 error-bracketing clause):** e = 0.5 (hit 0.81) 20/20, precision 0.539;
  e = 0.75 (hit 0.71) 18/20, precision 0.538. So about half the words such a search returns are right, at every error level tried.
- **Target: PASS both nulls.** I 320.2 vs shuffled-band p95 238.2 (mean 202.0) and order-shuffle p95 232.9 (mean 181.6), p 0.00 for
  both (200 draws each). 20 words of >= 4 letters cover 112 of 143 letter tokens. Grade M for every word: the S condition (control
  precision for >= 5-letter words >= 0.80) fails at 0.61.
- Words returned (M; spans per `seg_92_187.tsv`; control says about half are right): run 4 "lessen" (6 of 8), run 6 "gelt", run 10
  "licht" (5 of 8), run 16 "dvytsen", run 28 "emavs", run 36 "vyten" + "voeren", run 37 "regiment" + "volx", run 39 "drie" + "hondert",
  run 40 "ondersaten"; 187 postscript "middel", "vane", "allen", "sovde", "ende", "dochter", "vrome", "staet". Several fit the clear
  context: "noch [gelt] van de zijde van 611 ende 612 dese somer sal gefourneert werden"; "dat hij [drie hondert] uyt sijn voornempste
  [ondersaten] lichten mach"; run 10 "om die [licht...] te beginnen" (licht- + 3 unread tokens, possibly a levy word); these are
  leads at M, not a reading, and no sense of the letter is claimed.
- Where it was not found, and the limits: no word for runs 4 positions 1-2 (578, 337), run 10 positions 6-8 (210 300 217), run 36
  positions 1-2, and parts of the 187 postscript; "emavs", "dvytsen", "sovde" are likely wrong segmentations or wrong band edges.
  One lexicon (nl16, prose), unigram only, no bigram/context model; the 1619 list is still assumed to be the 1604-05 list.

## Remaining gaps (OBRED-SEG, 15 Oct 2026)
Read so far: no. 92 and the 187 postscript as band intervals (OBRED-BAND; 72 of 180 one-letter) and, by constrained segmentation, 20 nl16 words of >= 4 letters covering 112 of 143 letter tokens, all M (OBRED-SEG: target I 320 vs shuffled-band p95 238 and order p95 233; synthetic control beats its null 20/20 with word precision 0.58, 0.54 at the real error level); 37 name codes unread; inv. 6019 scans 555-556 carry 81 groups (58 H-read) with 45 C-graded period glosses
- no. 92 and the 187 postscript beyond M word leads - blocker: not-attempted; segmentation passes its control but precision is ~0.55, so no word reaches S; next: a context-scored pass (bigram/clear-context model from the letter's own clear prose plus nl16) on the 20 leads with --try per code, each accepted value re-tested at every occurrence (decode_key.py --try), PREREG with the same synthetic control, graded M, ~$3
- the 1619 key, the deciphered memorie and the "instructie ende sleutel" - blocker: not-attempted; not on inv. 6019 515-565 (OBRED-KEYHUNT, OBRED-549, OBRED-552, OBRED-MEM); next: the 2 Oct 1619 letter's home and the later liassen (OBRED-OCT2 in progress), ~$2.5
- the later liassen NA 1.01.02 inv. 6020-6024 and the 6019 stride-1 fill after 565 - blocker: not-attempted; outside this brief; next: a stride-3 screen of inv. 6020 (~$4)
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 and 21 Feb 1605 letters - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder done (OBRED-SG, OBRED-11851, OBRED-641, OBRED-11851B, OBRED-11852A): no numeral block, no Brederode, Stettin or Heidelberg heading (M)

## Escalation (OBRED-SEG, 15 Oct 2026)
- [x] siblings: scan 187 shares 26 values with no. 92 (OBRED-187); inv. 6019 scans 555-556 (Oggersheim, 14 Oct 1619) share 42 values with no. 92/187, clearing the shuffled-code control (OBRED-556); the letter's start (554) carries no groups (OBRED-552)
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187); the 1619 letter's prose and margin summaries read in part (OBRED-556); 515-554 and 558-565 seen by eye (OBRED-552, OBRED-549, OBRED-KEYHUNT, OBRED-MEM)
- [ ] known-keys: the 10 Aug 1598 Van Aerssen slip, Buzanval inv. 2028, DECODE 1600s and Palatine/Hessian keys screened (R10-OBRED98, R9-OBRED4, OLD-DKEY, R8-OBRED2, R9-OBRED3); the 1619 "instructie ende sleutel" is not on inv. 6019 515-565 (OBRED-KEYHUNT, OBRED-MEM); next: the 2 Oct 1619 letter's home (OBRED-OCT2), ~$2.5
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII and NR 4 carry no key or decipherment note (OBRED-DP, OBRED-KEYHUNT)
- [ ] key-rebuild: band intervals pass a held-out leaf check (OBRED-BAND) and segment into nl16 words above both nulls with a passing synthetic control, 20 words M (OBRED-SEG); next: a context-scored --try pass on the word leads with the same control, ~$3
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv 59/59 (OBRED-187); ciphertext_556.tsv two blind passes, 58 of 81 H-read after the 555 L15 second pass (OBRED-556, OBRED-552); the three gloss conflicts re-seen at 5000 px, eye + blind, none settled (OBRED-TRY)
- [x] retry: Den Tex (abridged edition) read twice; brievenboek 11851 596-733 and 11852 2-104 completed with controls
Verdict: keep going: 3 internal gaps; band intervals segment into 20 nl16 word leads above shuffled-band and order nulls (I 320 vs p95 238/233) with a synthetic control that passes (precision 0.58, 0.54 at the real error level), all M; cheapest next: a context-scored --try pass on the word leads with the same control (~$3)

## OBRED-NA (15 Oct 2026, 11:21-11:3x UTC by date -u, account 2, Opus; for LANE DEFAULT-A2-1109-15)

Brief: the no. 92 key's fate after OBRED-OCT2 put Brederode's own cipher last "in des Advocaets Barnevelt handen": a stride screen of NA
1.01.02 inv. 9459 (Bijlagen in de zaak tegen Oldenbarnevelt 1607-1618, 7 stukken) for a key leaf, cipher alphabet or Brederode letter, and
the S.G. secrete resoluties inv. 4562 at Oct 1619 for any entry naming Brederode, a memorie, cyfer or sleutel. A screen, nothing scored.

- Prior-work step: `prior_work.py ... --item-spec 'NL-HaNA 1.01.02 inv. 9459 ... + secrete resoluties inv. 4562 Oct 1619 ...' --step-type
  read` exit 4 (own claim LEAD, LOOK, 2 UNCHECKED, 2 UNCHECKED-NET); the four non-net rows recorded CLEAR in `prior-work.tsv` (adhoc-2cd3f8).
- Requests: 16, all 200, >= 3.2 s apart, NA take/release in ROOM: www.nationaalarchief.nl 2 (item pages for 9459 and 4562, scan list read
  from the page's `drupal-settings-json`), service.archief.nl 14 (IIIF). Every scan viewed, with sha1 and what is on it: `na_obredna_scans.tsv`;
  `screen_tools/regen_obredna.sh` re-derives them; no image committed. By eye, one reader (M).
- **inv. 9459** (17 scans, not 7 as the stuk count might suggest): odd scans 1-17 at 900 px, i.e. the opening of every one of the seven stukken
  (pencil numbers 1-7 on the backs). Cover "No. 1 h. Verschillende stukken"; stuk 1 a French letter "Monseigneur"; stukken 2-6 Dutch prose,
  three headed "Copie" / "Copie authentique", one a two-column set of articles; stuk 7 a blank folded sheet. **No numeral table, alphabet,
  nomenclator, numeral group or Brederode signature on the nine scans.** Not seen: the even scans 2-16 (continuation pages of the same
  stukken, 8 scans).
- **inv. 4562** (290 scans, Dec 1615 - Dec 1634; a thin register, about seven scans a year): located by bisection (50 = fol. 28v-29, 6 Dec
  1621 - 10 Jan 1622; 32 = fol. 10v-11, 30 Apr - 4 May 1619; 35 = fol. 13v-14, to 18 July and 29 Aug 1619). **Scan 36 (fol. 14v-15) runs on
  from the 29 Aug 1619 entry (Oostindische Compagnie; "Geschut uyt Engelant") straight to "Veneris den 7 Februarij 1620" (the Markgraf of
  Ansbach, troops raised in Germany)**: the secret register holds **no resolution at all between 29 Aug 1619 and 7 Feb 1620**, so nothing for
  Oct 1619, nothing on Brederode, a memorie, cyfer or sleutel. Folios 14 and 15 are consecutive, so no leaf is missing at the break (M, read
  from the date headings and foliation at 1000 px). Scan 37 (fol. 15v-16, 27 Mar - 21 May 1620): margins name England, a Keyserse legatie,
  Brunswick, Wulfsen Munter; nothing on Brederode or a cipher.
- What this settles (I): the key question of Oct 1619 (res. 1779 of 11 Oct, "het cijfer ongeschikt", Maurits to draw up a better one) was
  handled in the ordinary resolutions only (OBRED-KEYHUNT), not in the secret register. The no. 92 key is not filed among the seven
  9459 stukken at their openings, nor in 3.01.14 (R9-NAKEY). Where it was not found: 9459 odd scans; 4562 Aug 1619 - Feb 1620. Not looked at:
  9459 even scans 2-16; the other process series 9450-9458 and 9460 (titles name no cipher); KHA A13 (Maurits).

## Remaining gaps (OBRED-NA, 15 Oct 2026)
Read so far: no. 92 and the 187 postscript as band intervals (OBRED-BAND; 72 of 180 one-letter) and, by constrained segmentation, 20 nl16 words of >= 4 letters covering 112 of 143 letter tokens, all M (OBRED-SEG); 37 name codes unread; inv. 6019 scans 555-556 carry 81 groups (58 H-read) with 45 C-graded period glosses; the 2 Oct 1619 letter puts Brederode's own cipher last in Oldenbarnevelt's hands (OBRED-OCT2, M)
- no. 92 and the 187 postscript beyond M word leads - blocker: not-attempted; segmentation passes its control but precision is ~0.55, so no word reaches S; next: the context-scored --try pass on the 20 leads (OBRED-CTRY, this lane's wave 1), ~$3.5
- the no. 92 key ("mijn cyfer ... in des Advocaets Barnevelt handen") - blocker: not-attempted; not in 3.01.14 (R9-NAKEY), not at the opening of any of the seven stukken of 1.01.02 inv. 9459, and the S.G. secret register inv. 4562 has no entry between 29 Aug 1619 and 7 Feb 1620 (OBRED-NA); next: 9459 even scans 2-16 at 900 px (8 requests, ~$1), then the remaining process series 1.01.02 inv. 9450-9458/9460 by stride, ~$2
- the deciphered memorie of res. 1779 (a Maurits-cipher text, OBRED-OCT2 inference) - blocker: needs-physical-access; KHA A13 (Maurits) inventory not served to scripts and the archive is research-request only; owner-side step: a KHA research request, not queued
- the later liassen NA 1.01.02 inv. 6020-6024 and the 6019 stride-1 fill after 565 - blocker: not-attempted; outside this brief; next: a stride-3 screen of inv. 6020 (~$4)
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 and 21 Feb 1605 letters - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder done (OBRED-SG, OBRED-11851, OBRED-641, OBRED-11851B, OBRED-11852A): no numeral block, no Brederode, Stettin or Heidelberg heading (M)

## Escalation (OBRED-NA, 15 Oct 2026)
- [x] siblings: scan 187 shares 26 values with no. 92 (OBRED-187); inv. 6019 scans 555-556 (Oggersheim, 14 Oct 1619) share 42 values with no. 92/187, clearing the shuffled-code control (OBRED-556); the letter's start (554) carries no groups (OBRED-552)
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187); the 1619 letter's prose and margin summaries read in part (OBRED-556); 515-554 and 558-565 seen by eye (OBRED-MEM, OBRED-552, OBRED-549, OBRED-KEYHUNT); the 2 Oct 1619 letter 528-530 read in full (OBRED-OCT2)
- [ ] known-keys: the 10 Aug 1598 Van Aerssen slip, Buzanval inv. 2028, DECODE 1600s and Palatine/Hessian keys screened (R10-OBRED98, R9-OBRED4, OLD-DKEY, R8-OBRED2, R9-OBRED3); Brederode's own cipher last in Oldenbarnevelt's hands (OBRED-OCT2); not at the openings of 1.01.02 inv. 9459's seven stukken, and no secret resolution 29 Aug 1619 - 7 Feb 1620 (OBRED-NA); next: 9459 even scans 2-16, ~$1, then 9450-9458/9460 by stride, ~$2
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII and NR 4 carry no key or decipherment note (OBRED-DP, OBRED-KEYHUNT)
- [ ] key-rebuild: band intervals pass a held-out leaf check (OBRED-BAND) and segment into nl16 words above both nulls with a passing synthetic control, 20 words M (OBRED-SEG); next: the context-scored --try pass (OBRED-CTRY), ~$3.5
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv 59/59 (OBRED-187); ciphertext_556.tsv two blind passes, 58 of 81 H-read after the 555 L15 second pass (OBRED-556, OBRED-552); the three gloss conflicts re-seen at 5000 px, eye + blind, none settled (OBRED-TRY)
- [x] retry: Den Tex (abridged edition) read twice; brievenboek 11851 596-733 and 11852 2-104 completed with controls
Verdict: keep going: 3 internal gaps; the no. 92 key is not at the openings of the seven stukken of NA 1.01.02 inv. 9459 and the S.G. secret register inv. 4562 has no entry between 29 Aug 1619 and 7 Feb 1620 (OBRED-NA, M); cheapest next: 9459 even scans 2-16 (~$1), then the process series 9450-9458/9460 (~$2); the context-scored --try pass is running as OBRED-CTRY

## OBRED-CTRY (15 Oct 2026, 11:19-11:3x UTC by date -u, account 2, Opus; for LANE DEFAULT-A2-1109-15)

Brief: a context-scored --try pass on OBRED-SEG's 20 word leads: each lead's implied code->letter assignment tested at every other
occurrence of the same codes in no. 92/187, against a shuffled-band null and a synthetic-band control at the real error level that must
accept a known right word before any target lead counts. Disk and CPU only, 0 requests.

- Prior-work step: `prior_work.py ... --step-type decode` exit 4 (two own-lane claim LEADs -- OBRED-NA's covers the NA key search, not
  this test -- LOOK, 2 UNCHECKED, 2 UNCHECKED-NET); the five non-net rows recorded CLEAR in `prior-work.tsv` (adhoc-2a7d17). No earlier
  context or every-occurrence test (OBRED-TRY ran --try on glossed codes only; OBRED-SEG ran the segmentation).
- `decode_key.py --try` does not apply (no key.tsv / decode.json: letters are band intervals); the brief's fallback lattice scorer was used.
- PREREG `obred187/PREREG-OBREDCTRY.md` pushed in its own commit (0bbd2682b) before any statistic. Script `obred187/ctry/ctry.py`
  (`--check` up to date), outputs `ctry_gate.json`, `ctry_leads.tsv`. Scorer: char 4-gram (nl16 x5 + the letter's own 679 clear words),
  Viterbi over each sub-run with the clear words before/after as context; a lead holds if pinning its letters at every other occurrence
  costs <= 3 bits per pinned token. The script asserts the 20 leads are OBRED-SEG's own decode of the same intervals.
- **Synthetic control: BELOW GATE (registered: right-lead hold >= 0.60 and holding raises precision by >= 0.10, at both e).**
  e = 0.5 (interval hit 0.81): right leads hold 0.965 (n 202), wrong leads hold 0.782; precision 0.530 -> 0.582 among holders (+0.052).
  e = 0.75 (hit 0.73): right 0.961 (n 180), wrong 0.782; precision 0.455 -> 0.506 (+0.051). The test accepts a known right word but
  also accepts most wrong ones: the 3-bit tolerance plus single-letter pool intervals (a glossed code's pin equals its interval) let
  almost any in-interval assignment through. The per-lead random-assignment null says the same (random in-interval letters hold at
  1.000 for 11 of the 19 testable leads).
- **Target (read as a non-test at this N, per the PREREG):** 16 of 19 testable leads hold (h 0.842) vs shuffled-band null mean 0.579,
  p95 0.765, p 0.01 (100 draws) -- above the null, but the control shows holding barely separates right from wrong, so no lead gains
  from it. "staet" is untestable (no code recurs). All 20 stay M; nothing reaches S; nothing went into key.tsv (none exists).
- **Breaks (ungated observation, not a refutation):** "hondert" (code 200 read h; OBRED-BAND's interval for 200 is i, and the lead
  "licht" reads 200 = i -- a direct cross-lead conflict; d 11.3 bits in sub-run 3), "middel" (d 9.8 and 9.2 bits in sub-runs 1 and 6),
  "allen" (d 4.4 bits in sub-run 13). In the control a right lead breaks 4% of the time and a wrong one 22%, so a break is about
  5x likelier for a wrong lead; at precision ~0.5 that puts these three near 0.15 right, a lead's estimate, not a registered statistic.
  "drie [hondert]" fits the clear context ("dat hij ... uyt sijn voornempste [ondersaten] lichten mach") and may be "drie" + another
  numeral or a band-edge error at 200 (not tested here).
- Where it was not found, and the limits: one LM (char 4-gram, nl16 prose + 679 clear words), one tolerance (3 bits per pin), 13 short
  sub-runs; recurring codes inside the 92/187 letter runs are few, so most tests rest on one or two other occurrences.

## Remaining gaps (OBRED-CTRY, 15 Oct 2026)
Read so far: no. 92 and the 187 postscript as band intervals (OBRED-BAND; 72 of 180 one-letter) and, by constrained segmentation, 20 nl16 words of >= 4 letters covering 112 of 143 letter tokens, all M (OBRED-SEG); the every-occurrence context test holds 16 of 19 testable leads but its synthetic control is below gate (wrong leads hold 0.78 vs right 0.96), so it adds no grade (OBRED-CTRY); "hondert", "middel", "allen" break (ungated); 37 name codes unread; inv. 6019 scans 555-556 carry 81 groups (58 H-read) with 45 C-graded period glosses; the 2 Oct 1619 letter puts Brederode's own cipher last in Oldenbarnevelt's hands (OBRED-OCT2, M)
- no. 92 and the 187 postscript beyond M word leads - blocker: not-attempted; band intervals, segmentation and the every-occurrence context test are all done with controls and no lead reaches S (OBRED-BAND, OBRED-SEG, OBRED-CTRY: control below gate); next: a joint band-monotonicity check of all lead assignments together (an alphabetical homophonic list means code order implies letter order, so leads contradicting each other on codes outside the pool are caught) with the same synthetic control, PREREG first, ~$2
- the no. 92 key ("mijn cyfer ... in des Advocaets Barnevelt handen") - blocker: not-attempted; not in 3.01.14 (R9-NAKEY), not at the opening of any of the seven stukken of 1.01.02 inv. 9459, and the S.G. secret register inv. 4562 has no entry between 29 Aug 1619 and 7 Feb 1620 (OBRED-NA); next: 9459 even scans 2-16 at 900 px (8 requests, ~$1), then the remaining process series 1.01.02 inv. 9450-9458/9460 by stride, ~$2
- the deciphered memorie of res. 1779 (a Maurits-cipher text, OBRED-OCT2 inference) - blocker: needs-physical-access; KHA A13 (Maurits) inventory not served to scripts and the archive is research-request only; owner-side step: a KHA research request, not queued
- the later liassen NA 1.01.02 inv. 6020-6024 and the 6019 stride-1 fill after 565 - blocker: not-attempted; outside this brief; next: a stride-3 screen of inv. 6020 (~$4)
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 and 21 Feb 1605 letters - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder done (OBRED-SG, OBRED-11851, OBRED-641, OBRED-11851B, OBRED-11852A): no numeral block, no Brederode, Stettin or Heidelberg heading (M)

## Escalation (OBRED-CTRY, 15 Oct 2026)
- [x] siblings: scan 187 shares 26 values with no. 92 (OBRED-187); inv. 6019 scans 555-556 (Oggersheim, 14 Oct 1619) share 42 values with no. 92/187, clearing the shuffled-code control (OBRED-556); the letter's start (554) carries no groups (OBRED-552)
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187); the 1619 letter's prose and margin summaries read in part (OBRED-556); 515-554 and 558-565 seen by eye (OBRED-MEM, OBRED-552, OBRED-549, OBRED-KEYHUNT); the 2 Oct 1619 letter 528-530 read in full (OBRED-OCT2)
- [ ] known-keys: the 10 Aug 1598 Van Aerssen slip, Buzanval inv. 2028, DECODE 1600s and Palatine/Hessian keys screened (R10-OBRED98, R9-OBRED4, OLD-DKEY, R8-OBRED2, R9-OBRED3); Brederode's own cipher last in Oldenbarnevelt's hands (OBRED-OCT2); not at the openings of 1.01.02 inv. 9459's seven stukken, and no secret resolution 29 Aug 1619 - 7 Feb 1620 (OBRED-NA); next: 9459 even scans 2-16, ~$1, then 9450-9458/9460 by stride, ~$2
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII and NR 4 carry no key or decipherment note (OBRED-DP, OBRED-KEYHUNT)
- [ ] key-rebuild: band intervals pass a held-out leaf check (OBRED-BAND), segment into 20 nl16 word leads above both nulls (OBRED-SEG, M); the every-occurrence context test's control is below gate, a non-test (OBRED-CTRY: wrong leads hold 0.78, right 0.96, precision +0.05); next: a joint band-monotonicity check of all lead assignments with the same synthetic control, ~$2
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv 59/59 (OBRED-187); ciphertext_556.tsv two blind passes, 58 of 81 H-read after the 555 L15 second pass (OBRED-556, OBRED-552); the three gloss conflicts re-seen at 5000 px, eye + blind, none settled (OBRED-TRY)
- [x] retry: Den Tex (abridged edition) read twice; brievenboek 11851 596-733 and 11852 2-104 completed with controls
Verdict: keep going: 3 internal gaps; the every-occurrence context test holds 16 of 19 testable leads (h 0.84 vs shuffled-band p95 0.76, p 0.01) but its synthetic control is below gate (wrong leads hold 0.78, right 0.96), a non-test that leaves all 20 leads M, and "hondert" conflicts with "licht" on code 200 (OBRED-CTRY); the no. 92 key is not at the openings of NA 1.01.02 inv. 9459 nor in the secret register 29 Aug 1619 - 7 Feb 1620 (OBRED-NA, M); cheapest next: 9459 even scans 2-16 (~$1), then a joint band-monotonicity check of the leads (~$2)

## OBRED-MONO (15 Oct 2026, 11:42-11:4x UTC by date -u, account 2, Opus; for LANE DEFAULT-A2-1109-15)

Brief: OBRED-CTRY's next, a joint band-monotonicity check of all 20 OBRED-SEG lead assignments together (an alphabetical homophonic list
means code order implies letter order), PREREG first, a control that can fail differently from the target, and a synthetic known-answer
case at the real error level that must pass before any target number counts. Disk and CPU only, 0 requests.

- Prior-work step: `prior_work.py ... --step-type decode` exit 4 (two own-lane claim LEADs -- OBRED-NA2's covers the NA key search, not
  this test -- LOOK, 2 UNCHECKED, 2 UNCHECKED-NET); the five non-net rows recorded CLEAR in `prior-work.tsv` (adhoc-fc6e82). No earlier
  monotonicity test (OBRED-BAND fitted intervals, OBRED-SEG segmented, OBRED-CTRY tested every occurrence; none compared leads by code order).
- PREREG `obred187/PREREG-OBREDMONO.md` pushed in its own commit (9a6abd583) before any statistic. Script `obred187/mono/mono.py`
  (`--check` up to date), outputs `mono_gate.json`, `mono_leads.tsv`. Statistic D = discordant pairs among the 112 lead slots
  ((c1 < c2, l1 > l2) or one code with two letters). Null: letters permuted among the slots of each pool gap (1,000 draws), which keeps
  intervals, edge letters and each gap's letter multiset and changes only the in-gap order -- the axis D measures, so it can differ.
- **Synthetic control: BELOW GATE (registered: at both e, joint p <= 0.05 in >= 70% of sims, right-lead clean rate >= 0.60, precision of
  clean leads >= precision of testable + 0.10).** e = 0.5 (interval hit 0.82): joint test 0.925 of 40 sims, but right leads clean 0.118
  (wrong 0.066), precision 0.541 -> 0.678 among clean. e = 0.75 (hit 0.75): joint 0.900; right clean 0.059 (wrong 0.036), precision
  0.488 -> 0.609. The joint test has power at the real error level; the per-lead flag does not: with ~110 slots, almost every right lead
  shares a gap with some wrong lead or a gloss-error edge letter, so it is "contradicted" too.
- **Target (read as a non-test at this N, per the PREREG):** D 126 vs within-gap null mean 136.6, p05 128, min 119, p 0.036 (1,000 draws).
  All 20 leads are testable and all 20 contradicted. On its own the joint number is below the null's p05 -- the order of the leads'
  letters inside gaps agrees with code order a little more than chance -- but the registered gate binds the target to the whole control,
  so it is not counted; even taken as an observation it says some leads carry order information, not which.
- Observations (ungated): code 200 i ("licht") vs h ("hondert") again; code 409 s ("lessen") vs r ("dochter"); 433 t ("gelt", "vyten")
  vs s ("sovde"); 108 e ("lessen", "voeren") vs d ("middel"); 105 e ("vrome") vs d ("ondersaten"); 40 e ("allen") vs a ("ondersaten");
  314 m ("emavs") vs n ("ondersaten"). Leads with the most discordant pairs: "dvytsen" 25, "lessen" 24, "emavs" 24, "vrome" 22.
- All 20 leads stay M; nothing reaches S; nothing went into key.tsv (none exists).
- Where it was not found, and the limits: one statistic (pairwise discordance) and one null; the per-lead flag has no discriminating power
  at this lead count (control), so no lead is ranked by it. A per-lead contribution score (drop one lead, compare the fall in D with its
  within-gap null) is a different instrument and was not run (outside this brief).

## Remaining gaps (OBRED-MONO, 15 Oct 2026)
Read so far: no. 92 and the 187 postscript as band intervals (OBRED-BAND; 72 of 180 one-letter) and, by constrained segmentation, 20 nl16 words of >= 4 letters covering 112 of 143 letter tokens, all M (OBRED-SEG); the every-occurrence context test and the joint band-monotonicity check are both below their synthetic controls' gates, so neither adds a grade (OBRED-CTRY; OBRED-MONO: joint D 126 vs within-gap null p05 128, p 0.036, ungated, per-lead flag right-clean 0.06-0.12); code-200 and six more one-code-two-letter conflicts among the leads (OBRED-MONO, ungated); 37 name codes unread; inv. 6019 scans 555-556 carry 81 groups (58 H-read) with 45 C-graded period glosses; the 2 Oct 1619 letter puts Brederode's own cipher last in Oldenbarnevelt's hands (OBRED-OCT2, M)
- no. 92 and the 187 postscript beyond M word leads - blocker: not-attempted; band intervals, segmentation, the every-occurrence context test and the joint monotonicity check are done with controls and no lead reaches S (OBRED-BAND, OBRED-SEG, OBRED-CTRY, OBRED-MONO); next: a per-lead leave-one-out monotonicity contribution score (fall in D when a lead is dropped vs its within-gap null), whose synthetic control must separate right from wrong leads at e 0.5/0.75, PREREG first, ~$2
- the no. 92 key ("mijn cyfer ... in des Advocaets Barnevelt handen") - blocker: not-attempted; not in 3.01.14 (R9-NAKEY), not at the opening of any of the seven stukken of 1.01.02 inv. 9459, and the S.G. secret register inv. 4562 has no entry between 29 Aug 1619 and 7 Feb 1620 (OBRED-NA); next: 9459 even scans, then 9450-9458/9460 openings (OBRED-NA2 live at 11:41 UTC 15 Oct), ~$3
- the deciphered memorie of res. 1779 (a Maurits-cipher text, OBRED-OCT2 inference) - blocker: needs-physical-access; KHA A13 (Maurits) inventory not served to scripts and the archive is research-request only; owner-side step: a KHA research request, not queued
- the later liassen NA 1.01.02 inv. 6020-6024 and the 6019 stride-1 fill after 565 - blocker: not-attempted; outside this brief; next: a stride-3 screen of inv. 6020 (folded into OBRED-NA2, ~$4)
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 and 21 Feb 1605 letters - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder done (OBRED-SG, OBRED-11851, OBRED-641, OBRED-11851B, OBRED-11852A): no numeral block, no Brederode, Stettin or Heidelberg heading (M)

## Escalation (OBRED-MONO, 15 Oct 2026)
- [x] siblings: scan 187 shares 26 values with no. 92 (OBRED-187); inv. 6019 scans 555-556 (Oggersheim, 14 Oct 1619) share 42 values with no. 92/187, clearing the shuffled-code control (OBRED-556); the letter's start (554) carries no groups (OBRED-552)
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187); the 1619 letter's prose and margin summaries read in part (OBRED-556); 515-554 and 558-565 seen by eye (OBRED-MEM, OBRED-552, OBRED-549, OBRED-KEYHUNT); the 2 Oct 1619 letter 528-530 read in full (OBRED-OCT2)
- [ ] known-keys: the 10 Aug 1598 Van Aerssen slip, Buzanval inv. 2028, DECODE 1600s and Palatine/Hessian keys screened (R10-OBRED98, R9-OBRED4, OLD-DKEY, R8-OBRED2, R9-OBRED3); Brederode's own cipher last in Oldenbarnevelt's hands (OBRED-OCT2); not at the openings of 1.01.02 inv. 9459's seven stukken, and no secret resolution 29 Aug 1619 - 7 Feb 1620 (OBRED-NA); next: 9459 even scans and 9450-9458/9460 (OBRED-NA2, live), ~$3
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII and NR 4 carry no key or decipherment note (OBRED-DP, OBRED-KEYHUNT)
- [ ] key-rebuild: band intervals pass a held-out leaf check (OBRED-BAND), segment into 20 nl16 word leads above both nulls (OBRED-SEG, M); the every-occurrence context test (OBRED-CTRY) and the joint monotonicity check (OBRED-MONO: joint test has power, 0.90-0.93 of control sims, but the per-lead flag clears 0.06-0.12 of right leads) are both below their controls' gates; next: a per-lead leave-one-out monotonicity contribution score with its own synthetic control, ~$2
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv 59/59 (OBRED-187); ciphertext_556.tsv two blind passes, 58 of 81 H-read after the 555 L15 second pass (OBRED-556, OBRED-552); the three gloss conflicts re-seen at 5000 px, eye + blind, none settled (OBRED-TRY)
- [x] retry: Den Tex (abridged edition) read twice; brievenboek 11851 596-733 and 11852 2-104 completed with controls
Verdict: keep going: 3 internal gaps; the joint band-monotonicity check of the 20 leads reads D 126 vs within-gap null p05 128 (p 0.036) but its synthetic control is below gate (per-lead flag clears only 0.06-0.12 of right leads), a non-test that leaves all 20 leads M; seven one-code-two-letter conflicts among the leads, code 200 among them (OBRED-MONO, ungated); cheapest next: OBRED-NA2's NA screen (live), then a per-lead leave-one-out monotonicity score with its own control (~$2)

## OBRED-NA2 (15 Oct 2026, 11:41-11:5x UTC by date -u, account 2, Opus; for LANE DEFAULT-A2-1109-15)

Brief: OBRED-NA's next -- NA 1.01.02 inv. 9459 even scans, then the openings of the process series 9450-9458 and 9460, then (if >= 35% of
cap left) the inv. 6020 stride-3 screen; NA <= 40 requests. A screen for the no. 92 key, nothing scored, so no PREREG.

- Prior-work step: `prior_work.py ... --item-spec 'shelfmark=NL-HaNA 1.01.02 inv. 9459 even scans + inv. 9450-9458, 9460 openings + inv. 6020
  stride 3' --step-type read` exit 4 (LOOK, 2 UNCHECKED, 2 UNCHECKED-NET); the three non-net rows recorded CLEAR in `prior-work.tsv` (adhoc-597cdc).
- Requests: 38, all HTTP 200, >= 3.2 s apart, NA take/release in ROOM: www.nationaalarchief.nl 11 (item pages 9450-9460; unit titles and scan
  lists read from the page's `drupal-settings-json`), service.archief.nl 27 (IIIF at 900 px). Every scan with sha1 and content:
  `na_obredna_scans.tsv` (rows marked OBRED-NA2); `screen_tools/regen_obredna2.sh` re-derives them; no image committed. By eye, one reader (M).
- Unit titles (from the item pages): 9450 Intendit tegen Oldenbarnevelt (72 scans); 9451 letters of Oldenbarnevelt to Caron 1610-1619 (58);
  9452 to Van Aerssen 1606-1611 (11); 9453 to Langerak 1614-1619, with two memories and a letter of Maurits (46); 9454 to Ledenberg (4);
  9455 Willem Lodewijk to Oldenbarnevelt 1618 (7); 9456 rekesten of his wife and children (21); 9457 letters to wife and children, copies
  (7); 9458 memories in the case (8); 9459 bijlagen 1607-1618 (17); 9460 declaration on the burial (3).
- **inv. 9459 even scans 2-16**: French letters (one dated 1617, signed), Dutch copies of depositions and articles signed and dated 1618, an
  English letter naming Thomas Wood (1618), blank pages. With OBRED-NA's odd scans **all 17 scans of 9459 are now seen: no numeral table,
  alphabet, nomenclator, numeral group or Brederode signature.**
- **9450-9458, 9460** (19 scans: 9450 s1; 9451 s1, 15, 30, 45; 9452 s1, 6; 9453 s1, 12, 24, 36; 9454 s1; 9455 s1, 4; 9456 s1; 9457 s1;
  9458 s1, 5; 9460 s1): covers and wrappers, Dutch letter prose, legal memories in Dutch and Latin, the burial declaration. **One flag:
  9453 scan 24**, a letter to Langerak (margin date 15-1-1616 or 1617, M) whose prose carries small numerals as name codes (read at 900 px
  as 92, 47, 424, 47, 10, 49, 41, 3, 244, 32; M), with decodes in the margin in a second hand (Hert. van Bouillon, De Coninck van
  Engelant, Churfurst Paltz, Wesel / de Churfurst, M. d'Oldenbarnevelt, Troenes, De Coninck v. Spaegne). It is a names-only nomenclator of
  one- to three-digit numbers among clear words; the no. 92 code enciphers letters as well as names with three-digit groups (Palsgrave 605,
  Bohemen 594 in the 1619 glosses, OBRED-556), so it is not the no. 92 key. Not read further (outside this brief).
- **inv. 6020 stride 3: not run.** The 6019 stride-3 screen took 218 requests (regen_6019.sh); 2 were left under this job's 40.
- Where it was not found: all 17 scans of 9459; 19 of the 217 scans of 9450-9458/9460 (openings and a stride in 9451 and 9453). Not looked
  at: the other 198 scans of 9450-9458 (most in 9450, 9451, 9453); inv. 6020-6024; KHA A13 (Maurits).
- Suggestion (outside this target, one line, Usage 7): NA 1.01.02 inv. 9453 scan 24 carries an Oldenbarnevelt-Langerak name nomenclator
  with period margin decodes; a scout row could check it against a check-solved pass before any work.

## OBRED-9453 (15 Oct 2026): the inv. 9453 scan 24 names nomenclator against the no. 92/187 name codes (known-keys rung)
PREREG obred9453/PREREG-OBRED9453.md (d84524746), written before the native fetch. NA 3 requests (item page 9453, info.json 5360x4420,
full/max 5000x4123 sha1 b15d8cf11e52; scratch only, re-fetch via screen_tools/regen_obredna2.sh with full/max). One Opus read of two crops.
- Table (obred9453/table_9453_s24.tsv): 63 Ambassadeur van Venetien, 92 Hertoch van Bouillon (x3), 10 Mijne H. Staten General (x2), 99 Spinola,
  20 De Coninck van Engelant, 47 Churfurst Paltz (x2), 424 Wesel, 41 M. d'Oldenbarnevelt, 32 De Coninck van Spaegne (9 codes C by a period margin
  or interlinear decode on the same line); 49 Brand[enburg] and 241 (or 244) Treves M; "3 jaren" is a plain numeral. The 900 px read's "10"
  for the Engelant line is 20 at native size. Two-digit codes for persons and powers, three-digit for two places, among clear Dutch words.
- T1 form: exact value overlap with the 20 distinct no. 92/187 name codes (588-751) is k = 0; the ranges are disjoint (10-424 vs 588-751).
  The [1, 424] null cannot vary for this statistic (it never reaches 588: a non-test by construction, logged as such); the [1, 999] null
  gives mean k 0.21, p(k >= 0) = 1.0. T1 shows no match; it cannot by itself exclude a relation.
- T2 names: the only person in both lists is the Elector Palatine: 47 "Churfurst Paltz" here (C; Oldenbarnevelt to Langerak, Jan 1616)
  against 605 "Palsgrave" / "Fredrich Palsgrave" in the no. 92 family (C, OBRED-556; Brederode, Oggersheim, 14 Oct 1619) and 605 as an M
  context lead in no. 92 itself (Heidelberg 1605). Different code for the same person: a data conflict logged in HYPOTHESES.md, read as a
  different key, not settled. Bohemen (594), 600, 587 and 732 have no counterpart on this leaf.
- Ungated note (not in the PREREG): 241 and 10-99-sized values also occur among no. 92's letter groups (e.g. 241 in "578 337 241 97"); a
  names-only table and a letter-and-name table share number space by accident, so this is not a match.
- Result: no no. 92/187 name code matches the 9453 s24 nomenclator in form or context; every statement above is M or C as graded, none S.
  Where it was not looked for: the other 45 scans of inv. 9453 (only s1, 12, 24, 36 seen), so any second Langerak sheet or key is unseen.

## Remaining gaps (OBRED-NA2, OBRED-9453, 15 Oct 2026)
Read so far: no. 92 and the 187 postscript as band intervals (OBRED-BAND; 72 of 180 one-letter) and, by constrained segmentation, 20 nl16 words of >= 4 letters covering 112 of 143 letter tokens, all M (OBRED-SEG); the every-occurrence context test and the joint band-monotonicity check are both below their synthetic controls' gates, so neither adds a grade (OBRED-CTRY; OBRED-MONO: joint D 126 vs within-gap null p05 128, p 0.036, ungated, per-lead flag right-clean 0.06-0.12); code-200 and six more one-code-two-letter conflicts among the leads (OBRED-MONO, ungated); 37 name codes unread; inv. 6019 scans 555-556 carry 81 groups (58 H-read) with 45 C-graded period glosses; the 2 Oct 1619 letter puts Brederode's own cipher last in Oldenbarnevelt's hands (OBRED-OCT2, M)
- no. 92 and the 187 postscript beyond M word leads - blocker: not-attempted; band intervals, segmentation, the every-occurrence context test and the joint monotonicity check are done with controls and no lead reaches S (OBRED-BAND, OBRED-SEG, OBRED-CTRY, OBRED-MONO); next: a per-lead leave-one-out monotonicity contribution score (fall in D when a lead is dropped vs its within-gap null), whose synthetic control must separate right from wrong leads at e 0.5/0.75, PREREG first, ~$2
- the no. 92 key ("mijn cyfer ... in des Advocaets Barnevelt handen") - blocker: not-attempted; not in 3.01.14 (R9-NAKEY), not in the secret register 29 Aug 1619 - 7 Feb 1620 (OBRED-NA), not on any of the 17 scans of 1.01.02 inv. 9459, nor on the openings/stride scans of 9450-9458 and 9460 (19 of 234 scans; OBRED-NA2, M); the only numeral code seen in the process series is a small-number name nomenclator with margin decodes in an Oldenbarnevelt-Langerak letter (9453 scan 24), not the no. 92 design; next: the unseen scans of the three thick letter files 9450 (72 scans), 9451 (58), 9453 (46) at stride 3, about 55 NA requests, ~$2
- the deciphered memorie of res. 1779 (a Maurits-cipher text, OBRED-OCT2 inference) - blocker: needs-physical-access; KHA A13 (Maurits) inventory not served to scripts and the archive is research-request only; owner-side step: a KHA research request, not queued
- the later liassen NA 1.01.02 inv. 6020-6024 and the 6019 stride-1 fill after 565 - blocker: not-attempted; a stride-3 screen of a liasse costs about 220 NA requests (inv. 6019 took 218), which no 30-40-request job fits (OBRED-NA2 used its 38 on 9450-9460); next: a stride-3 screen of inv. 6020 as its own job with a request limit of about 230, ~$4
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 and 21 Feb 1605 letters - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder done (OBRED-SG, OBRED-11851, OBRED-641, OBRED-11851B, OBRED-11852A): no numeral block, no Brederode, Stettin or Heidelberg heading (M)

## Escalation (OBRED-NA2, OBRED-9453, 15 Oct 2026)
- [x] siblings: scan 187 shares 26 values with no. 92 (OBRED-187); inv. 6019 scans 555-556 (Oggersheim, 14 Oct 1619) share 42 values with no. 92/187, clearing the shuffled-code control (OBRED-556); the letter's start (554) carries no groups (OBRED-552)
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187); the 1619 letter's prose and margin summaries read in part (OBRED-556); 515-554 and 558-565 seen by eye (OBRED-MEM, OBRED-552, OBRED-549, OBRED-KEYHUNT); the 2 Oct 1619 letter 528-530 read in full (OBRED-OCT2)
- [ ] known-keys: the 10 Aug 1598 Van Aerssen slip, Buzanval inv. 2028, DECODE 1600s and Palatine/Hessian keys screened (R10-OBRED98, R9-OBRED4, OLD-DKEY, R8-OBRED2, R9-OBRED3); Brederode's own cipher last in Oldenbarnevelt's hands (OBRED-OCT2); not in the secret register 29 Aug 1619 - 7 Feb 1620 (OBRED-NA), not on any 9459 scan nor the 9450-9458/9460 openings (OBRED-NA2); the 9453 s24 Langerak names nomenclator (10-424, Paltz = 47) shares no value with the no. 92 name codes and conflicts on the Elector Palatine (605) (OBRED-9453); next: 9450/9451/9453 at stride 3, ~$2
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII and NR 4 carry no key or decipherment note (OBRED-DP, OBRED-KEYHUNT)
- [ ] key-rebuild: band intervals pass a held-out leaf check (OBRED-BAND), segment into 20 nl16 word leads above both nulls (OBRED-SEG, M); the every-occurrence context test (OBRED-CTRY) and the joint monotonicity check (OBRED-MONO: joint test has power, 0.90-0.93 of control sims, but the per-lead flag clears 0.06-0.12 of right leads) are both below their controls' gates; next: a per-lead leave-one-out monotonicity contribution score with its own synthetic control, ~$2
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv 59/59 (OBRED-187); ciphertext_556.tsv two blind passes, 58 of 81 H-read after the 555 L15 second pass (OBRED-556, OBRED-552); the three gloss conflicts re-seen at 5000 px, eye + blind, none settled (OBRED-TRY)
- [x] retry: Den Tex (abridged edition) read twice; brievenboek 11851 596-733 and 11852 2-104 completed with controls
Verdict: keep going: 3 internal gaps; the no. 92 key is not on any of the 17 scans of NA 1.01.02 inv. 9459 nor on 19 opening/stride scans of the process series 9450-9458 and 9460 (OBRED-NA2, M), whose one numeral code is an Oldenbarnevelt-Langerak name nomenclator of a different design (9453 scan 24); cheapest next: a per-lead leave-one-out monotonicity score with its own control (~$2), then 9450/9451/9453 at stride 3 (~$2); inv. 6020 stride 3 needs its own job (~220 requests, ~$4)

## OBRED-6020 (15 Oct 2026, 12:01-12:1x UTC by date -u, account 2, Opus; for LANE DEFAULT-A2-1109-15)

Brief (wave 3): stride-6 screen of NA 1.01.02 inv. 6020 (Liassen Agent Brederode, 1620, 604 scans) by the OBRED-6019/OBRED-NA method,
<= 120 NA requests, for a third numeral text in the no. 92 / scan-187 / 6019-556 table, a key leaf or a Brederode figure postscript.
Nothing decoded; no gate computed.

- Prior-work step: `prior_work.py ... --item-spec 'shelfmark=NL-HaNA 1.01.02 inv. 6020 scans 1-601 (stride-6 screen)' --step-type read`
  exit 4 (1 LEAD = this job's own claim, 1 LOOK, 2 UNCHECKED, 2 UNCHECKED-NET); the four non-net rows recorded CLEAR in `prior-work.tsv`
  (adhoc-3bc4f6). No earlier section ran any of inv. 6020 (grep: only the lias table and gap lines).
- PREREG addendum `obred187/PREREG-OBRED6020.md` pushed (8b9b6018c) before any fetch, with the stop rule.
- Route: METS `6b71330d-...` (from `nl_brederode_lias.tsv`; 604 scans, matches the item page count), `screen_tools/na_fetch.py`, IIIF
  `/full/700,/0/default.jpg`, >= 3.1 s apart, descriptive UA. **Requests: service.archief.nl 102 (1 METS + 101 scans), all HTTP 200**, no
  403/429/challenge; NA take/release lines in ROOM.md; no 1200 px re-look was needed. 12 sheets by `screen_tools/contact_sheets.py`,
  SHEET_SCANS=9, seed 6020, controls as OBRED-6019 (disk). Calls written to `images/6020_screen_sheetcalls.txt` and pushed (9e8660ecc)
  before `images/6020_screen_sheetkey.json` was opened; the key rebuilt from disk reproduces byte-identical. One reader, this worker's own
  eye, no subagent. No image committed; sha1s in `images/manifest.json` (`obred_6020`) and in `na_obredna_scans.tsv` (rows "OBRED-6020");
  `screen_tools/regen_6020.sh` re-derives scans and sheets.
- **Controls: 33 of 33 placed correctly (sheets 1-11 x 3), checked mechanically against the key. No sheet is a non-test.**
- **Result, inv. 6020 scans 1-589 at stride 6 (99 scans): no numeral-code block, key table, interlinear decipherment or figure
  postscript on any scan** (`images/6020_screen.tsv`, 99 rows). Content (by eye at sheet size, M): the 1620 run from about January to
  October 1620 by datelines read at sheet size -- Dutch letters to the States General signed P. Brederode (several with paraph), address
  leaves with red seals, letter openings, two 'Post data' paragraphs and one Post data page, all in prose; German, French, Italian and
  Latin copies and extracts; a printed German pamphlet laid in ('Copia ...', Johann Georg); two French lists (regiments/companies, places)
  with a quantity column -- figures in a list, not code groups; blank openings.
- Sheet 12 (scans 595 and 601) was built but **not read**: the PREREG stop rule placed the 80% cap line at about sheet 11.
- Where it was not found, and the limits: **every sixth scan of 1-589 only**; the other five sixths of inv. 6020 and scans 595/601 not
  looked at; a one-leaf postscript is a sixth as likely to be sampled as a run of six; tiles about 525 px wide on a sheet read at about
  2,000 px, so a block of a dozen groups or fewer inside prose could escape; one reader. A negative for these 99 scans at this
  resolution, not for inv. 6020 as a whole.

## OBRED-945X (15 Oct 2026, 12:28-12:4x UTC by date -u, account 2, Opus; for LANE DEFAULT-A2-1109-15)

Brief (wave 4): OBRED-NA2's next -- NA 1.01.02 inv. 9450, 9451 and 9453 at stride 3 beyond the scans already seen, same screen method,
one Opus read per flagged page, every scan logged. Nothing decoded; no gate computed.

- Prior-work step: `prior_work.py ... --item-spec 'shelfmark=NL-HaNA 1.01.02 inv. 9450, 9451, 9453 stride 3 (scans 4,7,...)' --step-type read`
  exit 4 (2 LEAD = this job's and OBRED-6021's claims, 1 LOOK, 2 UNCHECKED, 2 UNCHECKED-NET); the five non-net rows recorded CLEAR in
  `prior-work.tsv` (adhoc-8bb4ba).
- PREREG addendum `obred187/PREREG-OBRED945X.md` pushed (00bb760ec) before any fetch. Waited for OBRED-6021's NA release (12:38 UTC).
- Route: the three item pages on www.nationaalarchief.nl (scan lists from `drupal-settings-json`; 72, 58 and 46 scans, matching OBRED-NA2),
  then service.archief.nl IIIF `/full/700,/0/default.jpg`, >= 3.2 s apart, descriptive UA. **Requests: 60, all HTTP 200** (3 item pages +
  57 scans); NA take/release lines in ROOM.md; no 1200 px re-look was needed. Scans: 9450 4..70 (23), 9451 4..58 (19), 9453 4..46 (15),
  orders = 1 mod 3. 7 sheets by `screen_tools/contact_sheets.py`, SHEET_SCANS=9, seed 9450, the OBRED-6019/6020 disk controls. Calls
  written to `images/945x_screen_sheetcalls.txt` and pushed (74f4add2f) before `images/945x_screen_sheetkey.json` was opened. One reader,
  this worker's own eye, no subagent. No image committed; sha1s in `images/manifest.json` (`obred_945x`), `images/945x_screen.tsv` and
  `na_obredna_scans.tsv` (rows "OBRED-945X"); `screen_tools/regen_945x.sh` re-derives scans, sheets and the sheet key.
- **Controls: 21 of 21 placed correctly (7 sheets x 3), checked mechanically against the key. No sheet is a non-test.**
- **Result, 57 scans: no numeral-code block, key table, alphabet, interlinear decipherment or figure postscript on any scan; no hit tile,
  so no Opus page read was spent** (by eye at sheet size, M). Content: 9450 (Intendit) is a fair copy of numbered articles (about 12-225)
  in Dutch prose with margin notes, one article struck through; 9451 (to Caron) and 9453 (to Langerak) are address leaves with dockets
  dated 1612-1619 and red seals, numbered 'B n' on the 9453 backs, Dutch letters 'Myn Heer' in dense prose with signed closes and margin
  notes, a paragraphed memorandum, a two-column memorandum, a wrapper and one blank opening.
- Where it was not found, and the limits: one scan in three of 9450 4-70, 9451 4-58, 9453 4-46 (with OBRED-NA2's openings and stride,
  57 + 10 = 67 of 176 scans of the three files seen); tiles about 525 px wide on a sheet read at about 2,000 px, so a block of a dozen
  groups or fewer, and **small name-code numerals inside prose of the 9453 s24 kind, are below sheet resolution** (s24 itself was found at
  900 px); one reader. A negative for these 57 scans at this resolution, not for the three files as a whole.

## OBRED-6021 (15 Oct 2026, 12:25-12:5x UTC by date -u, account 2, Opus; for LANE DEFAULT-A2-1109-15)

Brief (wave 4): OBRED-6020's next -- a stride-6 screen of NA 1.01.02 inv. 6021 (Liassen Agent Brederode, 1621-1622, 810 scans) by the
OBRED-6020 method and sheet controls, <= 140 NA requests, for a third numeral text, a key leaf or a Brederode figure postscript.
Nothing decoded; no gate computed.

- Prior-work step: `prior_work.py ... --item-spec 'shelfmark=NL-HaNA 1.01.02 inv. 6021 scans 1-805 (stride-6 screen)' --step-type read`
  exit 4 (1 LEAD = this job's own claim, 1 LOOK, 2 UNCHECKED, 2 UNCHECKED-NET); the four non-net rows recorded CLEAR in `prior-work.tsv`
  (adhoc-86478c). No earlier section ran any of inv. 6021 (grep: only the lias table and gap lines).
- PREREG addendum `obred187/PREREG-OBRED6021.md` pushed (4dff21570) before any fetch, with the stop rule.
- Route: METS `c82b1eb5-...` (from `nl_brederode_lias.tsv`; 810 scans in the METS, matching the item page count), `screen_tools/na_fetch.py`,
  IIIF `/full/700,/0/default.jpg`, >= 3.1 s apart, descriptive UA. **Requests: service.archief.nl 137 (1 METS + 135 scans at 700 px +
  scan 379 at 1200 px), all HTTP 200**, no 403/429/challenge; NA take/release lines in ROOM.md, one at a time with OBRED-945X (the 1200 px
  re-look waited for its 12:44 release). 15 sheets by `screen_tools/contact_sheets.py`, SHEET_SCANS=9, seed 6021, the OBRED-6019/6020 disk
  controls. Calls written to `images/6021_screen_sheetcalls.txt` and pushed (1a6cb6621 sheets 1-9, f32c62b34 sheets 10-13) before
  `images/6021_screen_sheetkey.json` was opened; `screen_tools/regen_6021.sh` re-derives scans, sheets and the key (cmp check). One reader,
  this worker's own eye, no subagent. No image committed; sha1s in `images/manifest.json` (`obred_6021`) and `na_obredna_scans.tsv`
  (rows "OBRED-6021"); per-scan notes in `images/6021_screen.tsv` (117 rows read).
- **Controls: 39 of 39 placed correctly (sheets 1-13 x 3), checked mechanically against the key. No sheet is a non-test.**
- **Result, inv. 6021 scans 1-697 at stride 6 (117 scans): one numeral-code text, scan 379** (sheet 08 tile B; re-looked at 1200 px, M,
  nothing decoded): a Dutch letter whose left page carries about 12 lines of dotted numeral groups inside the prose, opening "Desen dach
  ... bekomme ick advijs" and running into plain words ("in date des 29 July ouden stijl dat", "te continueren", "op den uytganck van",
  "vande schriftelijcke resolutie in corten volgen sal"); the groups are mostly **two-digit consecutive pairs, each followed by a single
  letter** (read at 1200 px, M: 22.23 x, 76.77, 40.41 d, 13.14, 58.59, 49.50, 96.97, 67.68, 11.12, 16.17, 19.20, 29.30, 31.32, 52.53),
  a layout unlike no. 92 / scan 187 / 6019-556 (one- to three-digit groups up to about 741, no letters between) by eye; the right page
  closes "... Heydelberg den .. Augusti 1621" with the subscription "onderdanichste ende getrouwste dienaer" and **no name visible on this
  scan** (the sender is inferred from the liasse, Agent Brederode, not read; M). Every other scan (116): Dutch letters to the States
  General, several closes signed P. Brederode with paraph, address leaves with red seals dated 1621-1622, French, German, Italian and Latin
  copies and extracts, French articles with marginal letters, two name lists (signatures, no figures), blank openings.
- Sheets 14-15 (scans 703-805, 18 scans) were built but **not read**: the PREREG stop rule placed the 80% cap line at about sheet 13.
- Where it was not found, and the limits: **every sixth scan of 1-697 only**; the other five sixths of inv. 6021 and scans 703-805 not
  looked at; scans 378 and 380 (the letter's neighbours, for the sender's name and any further groups) not fetched; tiles about 525 px wide
  on a sheet read at about 2,000 px, so a block of a dozen groups or fewer inside prose could escape; one reader. A negative for the other
  116 scans at this resolution, not for inv. 6021 as a whole.

## Remaining gaps (OBRED-NA2, OBRED-9453, OBRED-6020, OBRED-945X, OBRED-6021, 15 Oct 2026)
Read so far: no. 92 and the 187 postscript as band intervals (OBRED-BAND; 72 of 180 one-letter) and, by constrained segmentation, 20 nl16 words of >= 4 letters covering 112 of 143 letter tokens, all M (OBRED-SEG); the every-occurrence context test and the joint band-monotonicity check are both below their synthetic controls' gates, so neither adds a grade (OBRED-CTRY; OBRED-MONO: joint D 126 vs within-gap null p05 128, p 0.036, ungated, per-lead flag right-clean 0.06-0.12); code-200 and six more one-code-two-letter conflicts among the leads (OBRED-MONO, ungated); 37 name codes unread; inv. 6019 scans 555-556 carry 81 groups (58 H-read) with 45 C-graded period glosses; the 2 Oct 1619 letter puts Brederode's own cipher last in Oldenbarnevelt's hands (OBRED-OCT2, M)
- no. 92 and the 187 postscript beyond M word leads - blocker: not-attempted; band intervals, segmentation, the every-occurrence context test and the joint monotonicity check are done with controls and no lead reaches S (OBRED-BAND, OBRED-SEG, OBRED-CTRY, OBRED-MONO); next: a per-lead leave-one-out monotonicity contribution score (fall in D when a lead is dropped vs its within-gap null), whose synthetic control must separate right from wrong leads at e 0.5/0.75, PREREG first, ~$2
- the no. 92 key ("mijn cyfer ... in des Advocaets Barnevelt handen") - blocker: not-attempted; not in 3.01.14 (R9-NAKEY), not in the secret register 29 Aug 1619 - 7 Feb 1620 (OBRED-NA), not on any of the 17 scans of 1.01.02 inv. 9459, nor on the openings/stride scans of 9450-9458 and 9460 (19 of 234 scans; OBRED-NA2, M), nor on 9450/9451/9453 at stride 3 (57 more scans, controls 21/21; OBRED-945X, M; 67 of the 176 scans of the three files now seen); the only numeral code seen in the process series is a small-number name nomenclator with margin decodes in an Oldenbarnevelt-Langerak letter (9453 scan 24), not the no. 92 design; next: the remaining two thirds of 9451 and 9453 (about 70 scans) read at 900 px one by one, not on sheets, since a name-code letter of the s24 kind is below sheet resolution, ~$3
- the deciphered memorie of res. 1779 (a Maurits-cipher text, OBRED-OCT2 inference) - blocker: needs-physical-access; KHA A13 (Maurits) inventory not served to scripts and the archive is research-request only; owner-side step: a KHA research request, not queued
- the numeral text on NA 1.01.02 inv. 6021 scan 379 (a Dutch letter, Heidelberg, Augusti 1621, about 12 lines of two-digit consecutive-pair groups each followed by a letter; OBRED-6021, M) - blocker: not-attempted; seen at 1200 px only, nothing transcribed or decoded, sender's name not on this scan; next: scans 378-380 at native size (3 NA requests), line crops, two blind passes + reconcile into a ciphertext_6021_379.tsv, then a design comparison with no. 92/187/556 (shared values, layout), PREREG first, ~$3
- the later liassen NA 1.01.02 inv. 6022-6024, the rest of inv. 6020 and 6021 and the 6019 stride-1 fill after 565 - blocker: not-attempted; inv. 6020 at stride 6, scans 1-589 (99 scans, controls 33/33), shows no numeral block (OBRED-6020, M); inv. 6021 at stride 6, scans 1-697 (117 scans, controls 39/39), shows one (scan 379 above) and nothing else (OBRED-6021, M); next: the two built but unread 6021 sheets 14-15 (scans 703-805, regen only, no new requests beyond 18 refetches), ~$0.5, then 6021 scans 361-397 at stride 1 around the hit, ~$1.5
- the 1605 Swiss-mission dossier NA 1.01.02 inv. 12569.38 - blocker: needs-physical-access; not digitised (OBRED-S2); owner-side step: a copy enquiry to the National Archives, not queued
- States-side trace of the 17 Oct 1604 and 21 Feb 1605 letters - blocker: needs-physical-access for the originals (Liassen Hoogduytschlandt inv. 6034/6035, Loopende 4909/4910 not digitised); digitised remainder done (OBRED-SG, OBRED-11851, OBRED-641, OBRED-11851B, OBRED-11852A): no numeral block, no Brederode, Stettin or Heidelberg heading (M)

## Escalation (OBRED-NA2, OBRED-9453, OBRED-6020, OBRED-945X, OBRED-6021, 15 Oct 2026)
- [ ] siblings: scan 187 shares 26 values with no. 92 (OBRED-187); inv. 6019 scans 555-556 (Oggersheim, 14 Oct 1619) share 42 values with no. 92/187, clearing the shuffled-code control (OBRED-556); the letter's start (554) carries no groups (OBRED-552); inv. 6020 at stride 6 (scans 1-589) shows no third numeral text (OBRED-6020, controls 33/33); inv. 6021 at stride 6 (scans 1-697) shows a third numeral text, scan 379 (Heidelberg, Aug 1621; OBRED-6021, controls 39/39, M), not yet transcribed; next: scans 378-380 at native size, two blind passes + reconcile, ~$3
- [x] clear-pages: the clear letter of 142r-143r read by eye (OBRED-187); the 1619 letter's prose and margin summaries read in part (OBRED-556); 515-554 and 558-565 seen by eye (OBRED-MEM, OBRED-552, OBRED-549, OBRED-KEYHUNT); the 2 Oct 1619 letter 528-530 read in full (OBRED-OCT2)
- [ ] known-keys: the 10 Aug 1598 Van Aerssen slip, Buzanval inv. 2028, DECODE 1600s and Palatine/Hessian keys screened (R10-OBRED98, R9-OBRED4, OLD-DKEY, R8-OBRED2, R9-OBRED3); Brederode's own cipher last in Oldenbarnevelt's hands (OBRED-OCT2); not in the secret register 29 Aug 1619 - 7 Feb 1620 (OBRED-NA), not on any 9459 scan nor the 9450-9458/9460 openings (OBRED-NA2), nor on 9450/9451/9453 at stride 3 (OBRED-945X, controls 21/21); the 9453 s24 Langerak names nomenclator (10-424, Paltz = 47) shares no value with the no. 92 name codes and conflicts on the Elector Palatine (605) (OBRED-9453); next: the rest of 9451/9453 at 900 px scan by scan, ~$3
- [x] print: no. 92 settled by "Search log", "Web and blog check", "Premise check"; the 17 Oct 1604 letter is not in Veenendaal II (OBRED-187); Resolutiën S.G. XIII and NR 4 carry no key or decipherment note (OBRED-DP, OBRED-KEYHUNT)
- [ ] key-rebuild: band intervals pass a held-out leaf check (OBRED-BAND), segment into 20 nl16 word leads above both nulls (OBRED-SEG, M); the every-occurrence context test (OBRED-CTRY) and the joint monotonicity check (OBRED-MONO: joint test has power, 0.90-0.93 of control sims, but the per-lead flag clears 0.06-0.12 of right leads) are both below their controls' gates; next: a per-lead leave-one-out monotonicity contribution score with its own synthetic control, ~$2
- [x] image-check: ciphertext.txt checked against NA inv. 1490 (R9-OBRED4, R10-OBREDV); ciphertext_187.tsv 59/59 (OBRED-187); ciphertext_556.tsv two blind passes, 58 of 81 H-read after the 555 L15 second pass (OBRED-556, OBRED-552); the three gloss conflicts re-seen at 5000 px, eye + blind, none settled (OBRED-TRY)
- [x] retry: Den Tex (abridged edition) read twice; brievenboek 11851 596-733 and 11852 2-104 completed with controls
Verdict: keep going: 4 internal gaps; inv. 6021 at stride 6 (117 scans, controls 39/39) shows one numeral-code text, scan 379, a Dutch letter dated Heidelberg Augusti 1621 with about 12 lines of pair-plus-letter groups (OBRED-6021, M, not transcribed); 9450/9451/9453 at stride 3 and inv. 6020 at stride 6 show none (OBRED-945X, OBRED-6020, M); cheapest next: scans 378-380 of inv. 6021 at native size with two blind passes + reconcile (~$3), then the per-lead leave-one-out monotonicity score (~$2) and the rest of 9451/9453 at 900 px (~$3)

## HEID-1621 (15 Oct 2026, 14:12-14:3x UTC by date -u, account ytbiz, Opus worker + 2 Sonnet readers; for LANE VIV-KEYSTONE, account 4)

Brief: `.claude/briefs/runs/2026-10-15-acct4-depth-steps.md`, JOB HEID-1621. The intake path for the numeral text OBRED-6021 found on
NL-HaNA 1.01.02 inv. 6021 scan 379. Not a solve attempt: no key, no reading, no family_run. Files in `heid1621/`. Kept here as a
subsection; the parent decides whether to split it into its own folder.

### Premise check (anonymous-pile path, CLAUDE.md pipeline step 2)
The sender is not read on scans 378-380 (below), so check-solved ran by holder, shelfmark, scan and glyph set; the edition step is
**deferred until a sender is named**.
- Holder notice: NA 1.01.02 inv. 6021 is the liasse of Agent Brederode, 1621-1622, 810 scans (`nl_brederode_lias.tsv`, METS
  c82b1eb5-...; read by OBRED-6021). Nothing in the notice as recorded there names a cipher or a decipherment for this letter; the
  item page itself was not re-fetched in this job (no budget for www.nationaalarchief.nl in the brief).
- Our own work: grep of the repository for inv. 6021 outside this folder: only ROOM.md, STATUS.md, LEDGER.md and the two briefs
  that queued OBRED-6021 and this job. No earlier transcription.
- DECODE: `sources/decode/` key and record listings (24-28 Sept 2026 caches) grepped for Brederode, Heidelberg/Heydelberg, 6021: no
  record of this item (DECODE record 6021 is an unrelated Florence key, ASFi SI vol. 3).
- Cryptiana: `sources/cryptiana/web` grepped for the same terms: no page about this item.
- Solver repositories: `sources/solver-diffs/2026-10-02/03-aymeloglu.tsv` and `sources/cyphersolver-site/catalogue-2026-10-09-diff.tsv`
  grepped: no row for this item (the one Brederode hit is this folder's own catalogue row). Cache-based, not a live fetch.
- `tools/prior_work.py ... --item-spec 'shelfmark=NL-HaNA 1.01.02 inv. 6021;folio=scan 379;date=1621-08-13;...' --step-type
  transcribe --offline`: exit 4 (1 LEAD = this job's own claim, 1 LOOK leaf, 2 UNCHECKED, 2 UNCHECKED-NET); the four non-net rows are
  recorded CLEAR in `prior-work.tsv` (adhoc-2a2c97). The two UNCHECKED-NET rows (live aymeloglu clone, editions) are not run here.
- The leaf and its neighbours: scans 378 and 380 at 1200 px and the 379 numeral block at native size carry no interlinear or marginal
  decode and no clear copy.
- **Verdict: `open` (anonymous-pile path, M).** No prior transcription or decipherment found in the sources above; edition step deferred
  until a sender is named.

### Material and sender (M)
Requests: **service.archief.nl 7** (METS, scans 378/379/380 at 1200 px, info.json of 379, two native regions of 379 at
730,1640,1960,1420 and 2930,1180,1850,950), all HTTP 200, >= 3.1 s apart, take/release lines in ROOM.md. Nothing committed; sha1s are in
`images/manifest.json` (`heid_6021`); `heid1621/regen_heid1621.sh` re-derives them.
- Scan 378: two pages of the same letter's body in clear Dutch (news of England, the Palatinate, Switzerland, the Valtellina), no groups.
- Scan 379: left page, the numeral block (15 lines); right page, the close: "Hier mede sal ick voor dit mael desen besluyten, den
  Almogende van harten biddende Uwe Hoochdem. in haere Christelijcke ende loffelijcke voornemen met gheluckelijcken uytcompste genadichlijck
  te willen [zegenen?, M]. Uyt Heydelberg desen 13 Augusti 1621", subscription "Uwer Hoochdem. onderdanichste ende getrouwsten dienaer".
  **No name after the subscription** (both readers and the eye agree).
- Scan 380: the address leaf, "Den Hoochmogenden Heeren Staten Generael der Vereenichde Nederlantsche Provincien, mijne hooch geeerde
  ende gebiedende Heeren ... [In den] Hage", with "Duplicaet vanden 13 Augusti 1621" in the same hand, a seal, and a receipt endorsement
  "L. 20 Aug. 1621". **This copy is the duplicate of a letter of 13 Aug 1621 to the States General.**
- Sender: not read on 378-380. The liasse (Agent Brederode) is the only pointer; not a reading. The start of the letter (scan 377 or
  earlier) was not fetched, and the hand was not compared with the signed P. Brederode closes elsewhere in inv. 6021.

### Transcription (M)
`tools/iiif_lines.py --image s379_block_native.jpg --out crops --prefix h379 --debug` -> 15 line crops, overlay checked, run before any
reader call; the close region likewise (9 crops; readers given 5). Two blind Sonnet readers (A plain left-to-right; B read each
line right-to-left before writing it out), text only, one reconciliation by this worker against the crops. `heid1621/ciphertext_6021_379.tsv`, every
token M. Reader agreement on numerals: 95 of 96 (the one split, L03 58 / 88, left unsettled). Letters: the readers agree with each other
everywhere; the eye differs on three tokens (L06 pos 1, L10 pos 12 read x where both readers read r, from the glyph shared with the x
after 22.23; L04/L12/L13 "1" read as an undotted letter i), each kept as an `alt`. Under the PREREG stop rule (more than a tenth
split) the transcription is settled enough to count.

Clear context inside the block (M): "Desen dus wijt geschreven hebbende, bekomme ick advijs [groups] in date des 29 July ouden stijl dat
[sign] van [sign] aldaer [groups] ... hebben [groups] ... [sign] volgende [groups] te continueren bij soo verre als oock [groups] hadde
devoir metten [groups] tot op den uytganck van [groups] te presteren te vroeden sijn, waer van de schriftelijcke resolutie in corten
volgen sal." Three non-numeral signs (a dotted bracket, a cross, an open box) stand in clear prose where a name would go.

### Structural test (PREREG-HEID1621.md, pushed 0b95fd8e5 before any count; `heid1621/structure_6021.py --check`)
| statistic | inv. 6021 s379 | C1 no. 92 (121 groups) | C2 order shuffle of s379 (10,000) |
|---|---|---|---|
| S1 pairs with second = first + 1 | 40 of 41 = 0.976 (0.951 if L03 reads 88) | -- | -- |
| S1 adjacent numeral tokens consecutive | 0.474 (96 tokens) | 0.042 (5 adjacent pairs: 611 612 twice, 616 617, 656 657, 703 704) | mean 0.020, p99 0.053 |
| S2 distinct pairs / value range | 21 distinct of 41, 12 repeat (22.23 x5, 76.77 x4); values 10-84 | 99 distinct of 121; 30-741 | -- |
| S3 trailing letter | 44 of 45 units carry one; 18 letter forms incl. B/S variants (x 7, c 5, d 5, f 4, p 4) | none (0 by construction, not a test) | -- |
| S4 units per numeral-only line vs Dutch | 6.5 units (L05, L08) vs 6.5 words and 14.3 syllables per clear line (6 clear lines, eye, M) -> **unit ~ word** | n/a (printed edition, no line widths) | -- |

- **PREREG decision: "pairs always (n, n+1)" is met** (0.976 >= 0.95 and C2 p99 0.053 < 0.5). The one exception, L11 "29 20 f", is read
  20 by both readers and the eye; whether it is a slip for 29 30 or 19 20 is not settled here.
- Units outside the pair shape: 38 stands alone three times (before 10.11 b, before 64.65 c, after 84), 84 once; 67.68 once without a
  letter (before 59.60 p). These four runs are the "longer units" in `structure_6021.json`.
- Descriptive, **not preregistered** (reported as a lead only): the trailing letter follows the pair. Every repeated pair keeps its
  letter except 31.32 (o, then g) and 76.77 (r?, box sign, c, c), and pairs that overlap by one number share it: 22.23 / 23.24 x,
  40.41 / 41.42 d, 58.59 / 59.60 p, 46.47 / 47.48 f, 19.20 / 20.21 m, 10.11 / 11.12 b. The letter seems to belong to a band of about
  three numbers, not to a single pair.

**Design-class lead (M):** a word-level code of about 45 units in which each unit is a consecutive number pair (the second number adds
no information beyond the first) plus a letter tag tied to a band of numbers, with a few standalone numbers (38, 84) and three
non-numeral signs in the clear text. This is a different design from no. 92/187/556 (one- to three-digit groups up to 741, consecutive
only 4% of the time, no letters). No class above M; nothing decoded.

### For the verifier
Nothing here is a reading. What a verifier would check: (1) the PREREG decision from `structure_6021.json` (`--check`); (2) the three
eye-over-reader letter calls (x for r twice, i for 1) and the unsettled L03 58/88 against the crops (regen script); (3) the sender
question: the letter is an unsigned duplicate (380 "Duplicaet vanden 13 Augusti 1621") in the Brederode liasse, so attribution needs the
start of the letter (scan 377 or earlier) and a hand comparison with Brederode's signed closes in the same inv., not the liasse alone;
(4) whether the band-shared letters (descriptive) hold up on a second letter in the same system. The PREREG statistics are counts on an
M transcription; the S4 word/syllable counts are this worker's own reading of six clear lines. Suggested next steps (not run, Usage 7):
scans 370-377 at 700 px to find the letter's opening and any name (about 8 NA requests, ~$1); then a stride-1 screen of inv. 6021 scans
361-397 and the unread sheets 14-15 for a second letter in the pair-plus-letter system (~$1.5); a hand comparison against P. Brederode's
signed closes in inv. 6021 (~$1).
