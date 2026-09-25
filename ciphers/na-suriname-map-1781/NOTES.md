open
NA 4.VEL's own finding-aid text read directly (the item page's embedded catalogue JSON -- `unittitle`,
`scopecontent`, `bioghist` -- for every item in the invnr range 2030A5-2090C, i.e. the whole Suriname
fortification-survey block of this toegang) plus the Atlas of Mutual Heritage pages for VEL2039 (page
2025), VEL2061 (page 2218) and the neighbouring VEL2044A/2044B/2045A (pages 2230/2231/2232), all read by
this worker 25 Sept 2026; those pages cite den Heijer, *Grote Atlas van de West-Indische Compagnie* II,
*de nieuwe WIC 1674-1791* (2012) as their source but this worker did not independently open that book.
No full decipherment of 2007A, 2039, 2046, 2061 or 2077 located anywhere (DECODE's cached dumps, both
solver repositories, and general web search, all below).

# NA 4.VEL Suriname fortification maps in cipher, 1781 (VX-N01)

QUEUE row: VX-N01 (`.claude/briefs/runs/2026-09-25-lane-vx-cs04.md`, LANE VX job 2 batch), itself sourced
from worker VX-SCNA's National Archief round-2 sweep (QUEUE.md, "Key beside the letter (LANE VX, 25 Sept
2026)" section, added 25 Sept 2026 ~07:45).

## What was asked

Fetch NA 4.VEL invnr 2039 ("Plan van het fortress Nieuw Amsterdam", "gedeeltelijk in cijferschrift", no
twin found by VX-SCNA) at full size; say how much of it is cipher and whether the alphabet looks like
2007A's; inventory 4.VEL (and the Suriname map collections the NA catalogue links) for other maps "in
cijferschrift"; check-solved via the map literature (Koeman / Leupe catalogue, NA's own description, web,
Atlas of Mutual Heritage) and whether the 2007A/B pairing has been written up. Not asked: decode, build a
key, or classify novelty (rule 10 -- that is the verifier's job).

## Established (H: catalogue text and images read directly by this worker)

**The 2007A/2007B pair** (already on file from round 2): 2007A is a manuscript map of the Suriname river
mouth and Fort Zeelandia/Paramaribo with every label enciphered; 2007B is catalogued "Blad 2, kopie,
cijferschrift vertaald, 1781" and is the identical map redrawn with every label in plain Dutch. New this
pass: **2007A itself also carries a full plain-Dutch interlinear gloss, written above (not below) the
ciphered line, for every text block checked** -- the title ("Generaal Plan van deffensie" over "Gзhaoxg
scph 5al Vзa7hysd", etc., `images/2007a_titletext.jpg`), a river-feature caption ("Mangroe en parumabos"
over "ijAlgok 3l sAosAxd#by.", `images/2007a_nota.jpg`), and a legend note ("Palissade en Krijgs Landen"
over "sosha qxgmbawd sldosromoja gplvrki.", `images/2007a_aanmerkinge.jpg`). This is a *third*, independent
route to 2007A's key beyond the 2007B twin: the plaintext is written directly on the ciphertext sheet. (A
call for whoever transcribes it: the gloss's ink/hand looks like a later, lighter, more casual annotation
than the fair-copy cipher text -- possibly a 20th-century archivist's working crib built by comparing 2007A
against 2007B -- but that is a transcription-worker's call, not this check-solved pass's, and it does not
change the finding: the plaintext is present in both places.)

**NA 4.VEL invnr 2039** ("Plan van het fortress Nieuw Amsterdam", 1781, 11267x8656 px, full size fetched:
`https://service.archief.nl/api/file/v1/default/09bc6088-27a9-4581-87c8-fc80d867441c`). NA's own
scopecontent: "Met profil / Gedeeltelijk in cijferschrift." Eye-check (native-resolution crops,
`images/2039_cartouche.jpg`, `2039_bastion_zoom.jpg`, `2039_remarque.jpg`) shows this understates how much
of the sheet is ciphered: the title cartouche ("Spexrt зAh sfзr F, ..."), the full a-r "Verklaringe der
Letteren" legend list, the descriptive clause after every "Bastion <province>" and "Redan/Schans <name>"
label (the province/bastion names themselves stay in plain Dutch; the artillery/measurement description
after each does not), and the entire "Remarque" paragraph (heading itself ciphered as "Ozijдcx37") are all
in cipher -- a large majority of the sheet's *running text*, though the map's own place-name labels stay
plain. No interlinear gloss and no adjoining key found anywhere on this sheet (checked the cartouche, the
bastion-list block and the remarque block at native resolution). The cipher hand/alphabet (elongated
ascenders, a recurring "λ", a numeral-like "5" used as a letter, doubled "##" marks, tilde diacritics)
looks like the same system as 2007A's on visual inspection -- not a formal glyph-by-glyph comparison, an
eye-check only.

**Sibling inventory of the same fortification-survey block (4.VEL invnr 2030A5-2090C, 95 items, the full
Suriname-forts run: Nieuw Amsterdam, Purmerent, Leiden, Zeelandia, Sommelsdyk, Oranje, Motkreek, Marowyne),
read via each item's own embedded scopecontent, not a further site-wide term search** (round 2 had already
closed `cijferschrift` and ten other spelling variants NA-wide -- see QUEUE.md 6549-6627 -- so a repeat of
that search would be duplicate work; this pass instead read the raw catalogue field for every item in the
one block where the known cipher maps sit). Two more items flagged, **neither found by round 2's term
search because NA's own catalogue spells the word "cyferschrift" here, not "cijferschrift"**:

- **4.VEL invnr 2046**, "Plan en defensie van de redout Purmerent." Scopecontent: "In cyferschrift. Met
  profil." Digitised, 11529x4584 px, full size:
  `https://service.archief.nl/api/file/v1/default/c8795078-bff2-49b5-bc16-23144f1be88e`. Eye-check
  (`images/2046_cartouche.jpg`): title cartouche fully ciphered ("Qext зh w7ivalyfo6lApr, ..."), same hand
  as 2039/2007A. No interlinear gloss found.
- **4.VEL invnr 2061**, "Plan en defentiestaat van de Redout Leyden." Scopecontent: **"In cyferschrift, met
  verklaring."** Digitised, 11355x4505 px, full size:
  `https://service.archief.nl/api/file/v1/default/14bbe911-339b-4ef5-8135-b4ec0cedc3ce`. Eye-check
  (`images/2061_title_gloss.jpg`, `2061_title_topleft.jpg`) confirms the "met verklaring" (with
  explanation): **a plain-Dutch interlinear gloss is written above the cipher for the title and the
  battery-list header** -- "Plan en Defensie Staat" over "Scah зt v7ivalymd ...", "van de Redout Leyde[n]"
  over "5Al v7 oow##k5r g3...", "De Batterijen zijn gedeponeerd" over "v3 dAr:Aroctal ψth g3vfq##h7aow:" --
  the same gloss-over-cipher pattern as 2007A, not checked past the header block (the No.1-6 battery list
  and the a-g legend below it were not individually checked for further gloss coverage; a follow-on worker
  should check the rest of the sheet before assuming the whole text is glossed).

Also checked and **eye-confirmed NOT ciphered** (ruling out three more titles that a search-engine summary
of the Atlas of Mutual Heritage site had suggested belonged to "a series in cipher, see VEL2007A and
2076-2078" -- that summary is wrong for two of the three and only half-right for the third; do not repeat
it without checking the image, per rule 2):
- **4.VEL invnr 2076** ("Platte grond van de Buytenwerken om het fortress Zeelandia..."): entirely plain
  Dutch, legend A-S all readable Latin script. `images/2076_overview.jpg`.
- **4.VEL invnr 2078** ("Plan van de teegenswoordigen staat der fortress Zeelandia..."): entirely plain
  Dutch, signed "Wellant" (i.e. Wollant). `images/2078_overview.jpg`.
- **4.VEL invnr 2077** ("Plan van de fortress Zelandia."): **mixed, like 2039/2046/2061** -- the title
  cartouche and the "Explicatie der Signatuuren" legend entries (a, b, c...) are ciphered, but the "Nota"
  and "Remarque" paragraph headings and body prose, and the building/place labels, are plain Dutch.
  NA's own scopecontent for this item says only "Bevat ook: Project ter verbetering..." -- **no cipher
  mention at all** in NA's catalogue text, the same silent-catalogue gap as 2046/2061's "cyferschrift"
  spelling, but worse (no keyword at all to find it by). `images/2077_overview.jpg`. This means a fourth,
  larger route was missed by every term-based search so far: some ciphered items in this block carry no
  cipher-related word anywhere in NA's metadata, and can only be found by eye-checking the image (as this
  pass did for a set of 95 candidates it could narrow down by co-location; a scan of 4.VEL's other ~9000
  items this way is out of this job's scope).

## Check-solved (web / print / community / DECODE / both solver repos)

- **Atlas of Mutual Heritage** (atlasofmutualheritage.nl), a specialist Dutch/Surinamese cartography-
  history project the job brief named: confirms this whole group is *known to be enciphered* but explicitly
  **not deciphered**. Page 2025 ("Map of fort Nieuw Amsterdam", Number field VEL2039): "c. Verklaringen:
  [linksboven] een legenda bij de letters a t/m u met beschrijvingen, in geheimschrift, niet
  getranscribeerd" and "[linksonder] een in geheimschrift gestelde notitie, niet getranscribeerd" -- i.e.
  the legend a-u and the lower-left note are both explicitly flagged as cipher and explicitly not
  transcribed. Page 2218 ("Plan and profile of the redoubt Leiden", Number field VEL2061): "The legend in
  cipher on Wollant's map is as follows: (...)" and "an encrypted key to the numbers 1 to 6 and the letters
  a to g, not transcribed." Both pages name the mapmaker as **Johann Friedrich Ferdinand Wollant**, ordered
  by Governor **Texier** after the outbreak of war with Great Britain became known in Suriname in 1781, as
  part of a general colony defence plan -- this dates and contextualises the whole 2007A/2039/2046/2061/2077
  cluster as one commission. Both pages cite the same single source, **den Heijer, H., *Grote Atlas van de
  West-Indische Compagnie*, II, *de nieuwe WIC 1674-1791* (2012)** -- this worker read the Atlas of Mutual
  Heritage pages themselves, not den Heijer's book, so the sentence above is what Atlas of Mutual Heritage
  (which credits den Heijer for its research) says, not an independent read of den Heijer.
  Pages checked near 2046 (2228-2232, covering VEL2044A/2044B/2045A) mention no cipher for those
  neighbouring items and do not cover 2046 itself -- 2046 was not located in Atlas of Mutual Heritage's own
  page index in this pass (a gap, not a negative: it may simply not have its own page there).
- **Koeman's *Atlantes Neerlandici*** (the standard reference for historical Dutch cartography that the job
  brief named): **not opened this pass** -- not found freely reachable from the cloud in the time budgeted;
  flagged rather than skipped silently, per the intake gate.
- **Web search** (general, 25 Sept 2026): no hit for any decipherment, transcription or discussion of this
  cipher beyond the Atlas of Mutual Heritage pages above; Wikipedia/Wikidata/mapcarta/Greater Caribbean
  Mapping pages on Fort Nieuw-Amsterdam and Fort Sommelsdijk describe the forts' history with no mention of
  a cipher.
- **DECODE (de-crypt.org)**: the repo's cached crawl (`sources/decode/records-decrypted-2026-09-24.tsv`,
  `records-non-decrypted-2026-09-24.tsv`, 24 Sept 2026) grepped for "suriname" -- one hit, NA 1.05.03
  (Sociëteit van Suriname) invnr 219 f.315r, 1689, a **different toegang, different date, different cipher**
  from this group; no match for Leupe, 4.VEL, Nieuw Amsterdam, Purmerent or Redout Leyden. Not re-crawled
  live (the cached dump is one day old and NA-wide; re-crawling for one target would be duplicate work).
- **Both solver repositories**, shallow-cloned and grepped 25 Sept 2026: `dbourdeau/cyphersolver` -- one
  incidental hit ("Collectie Suriname" inside `affry1757/bussemaker.txt`, an unrelated target's source
  citation, not this cipher). `aaymeloglu/unsolved-ciphers` -- one incidental hit in its DECODE-catalogue
  mirror, the same NA 1.05.03/1689 record already ruled out above. Neither repository has a target for any
  of 2007A, 2039, 2046, 2061 or 2077.

## Hosts and requests (this target)

`www.nationaalarchief.nl`: 6 (item pages for 2039, 2007A, 2046, 2061, 2076, 2077, 2078 -- 7 actually, plus
one failed plain-search-URL guess that 404'd, plus one browser-tool attempt at a guessed search URL that
also 404'd; all >=1.5s apart, descriptive User-Agent). `service.archief.nl`: 27 (7 x info.json + 18 image
crops/overviews, all >=1.5s apart, all HTTP 200, none hit a 429/403/challenge). Both well inside this
worker's combined 60-request budget for the pair of targets (the other target, na-raad-azie-1800, used
Huygens/archive.org instead, not this pair of hosts). WebSearch: 6 queries. WebFetch: 5 (Atlas of Mutual
Heritage pages). No DECODE live fetch, no credentials.

## Closing line (job brief format)

**Key beside the letter:** yes, for two of the five cipher sheets in this cluster --
(1) 2007A/Blad 1 has *three* independent routes to its key: the full plain-Dutch twin sheet 2007B ("Blad 2,
kopie, cijferschrift vertaald"), an interlinear plain-Dutch gloss written directly on 2007A itself, and (by
extension) 2061's own interlinear gloss pattern confirms this workshop consistently left cribs; (2) 2061
carries its own interlinear plain-Dutch gloss over its title and battery-list header (extent over the rest
of the sheet not yet checked). 2039, 2046 and 2077 have **no** key or gloss found on the sheet or elsewhere
in this pass -- they fail this lane's own gate (recovery via a beside-it key) and are cryptanalysis-lane
candidates instead, unless a key turns up elsewhere (e.g. in Wollant's own papers, not searched this pass).

**Undeciphered copy-free material it could read:** all five sheets are undeciphered (no transcription or
decipherment published anywhere found) and all are copy-free (digitised, no login):
- 4.VEL invnr 2039, full size `https://service.archief.nl/api/file/v1/default/09bc6088-27a9-4581-87c8-fc80d867441c`
- 4.VEL invnr 2046, full size `https://service.archief.nl/api/file/v1/default/c8795078-bff2-49b5-bc16-23144f1be88e`
- 4.VEL invnr 2061, full size `https://service.archief.nl/api/file/v1/default/14bbe911-339b-4ef5-8135-b4ec0cedc3ce`
- 4.VEL invnr 2077, full size `https://service.archief.nl/api/file/v1/default/cd3a65eb-7a10-497f-9c1e-373699a0e02d`
- 4.VEL invnr 2007A, full size `https://service.archief.nl/api/file/v1/default/daf5a571-6419-4086-9ae3-711a588a7efc`
  (Blad 1) with its own gloss and its twin 2007B `https://service.archief.nl/api/file/v1/default/222db0d8-5e8a-4023-9417-cfa290e8646f`

## Suggested next step (not this job's scope)

2007A (twin + on-sheet gloss) and 2061 (on-sheet gloss) are the two strongest recovery-lane candidates in
this cluster and belong on the board ahead of 2039/2046/2077. A transcription pass on 2061 should first
check whether the gloss continues past the header block this pass looked at.
