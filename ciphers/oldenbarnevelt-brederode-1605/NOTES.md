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

- De Leeuw et al. 2024 "Keys with nomenclatures" (Cryptologia 48(2)) not yet read -- queue for
  OpenAlex/Semantic Scholar abstract check or JSTOR-QUEUE.tsv.
- Den Tex's *Oldenbarnevelt* biography (dbnl.org, full text online) not yet read -- host TLS-failed twice
  this pass; retry from a fresh session/container.
- "A.R.A., Holland 2613" (and "2589") not traced to a current Nationaal Archief toegang/invnr.
- No transcription-for-decoding pass has been done; the ~121-token count above is a by-eye description, not
  a token-by-token key-recovery transcription.

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
