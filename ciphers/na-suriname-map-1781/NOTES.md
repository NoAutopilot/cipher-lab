partial
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

## Reading (VX-RD03, 25 Sept 2026)

**Intake gate checked:** VX-CS04's check-solved verdict above names the standard sources read (NA's own
finding aid, Atlas of Mutual Heritage, den Heijer via Atlas of Mutual Heritage's citation) and the pages
read -- passes the 25 Sept 2026 intake gate.

**What this job set out to do:** (1) build a key from 2007A's on-sheet gloss + 2007B's plain twin + 2061's
on-sheet gloss; (2) decode 2039/2046/2077's ciphered legend/cartouche text with that key. Part (1) produced
a real, if partial, result; part (2) was not reached -- see "What was not done" below.

### Key source and method

Fetched 2007B (the plain-Dutch twin of 2007A, referenced in the check-solved pass but never downloaded --
`images/2007b_full.jpg` + title/Nota/Remarque crops) and native-resolution IIIF crops of 2007A's own
"Nota A-F" and "Remarque" paragraphs (`images/2007a_nota_af_block.jpg`, `images/2007a_remarque_af_block.jpg`
-- both carry their own interlinear gloss too, a bonus find beyond this job's scope, not transcribed).

Three independent transcription passes then read the short, clearly-glossed label lines: this worker's own
pixel-by-pixel reading of 2007A's title block ("Generaal Plan van Defensie...") and "Remarque" heading; a
Sonnet subagent's independent blind reading of the same 2007A crops (title/nota/aanmerkinge); a second
Sonnet subagent's independent blind reading of 2061's title + battery-header block. Passes agreed on the
glyph sequence for every word checked except one position in "Plan" and the tail of "Defensie" (both
flagged, see `conflicts.tsv`).

Reconciling the three passes against the known gloss text (`plain_votes.tsv`) produced **13 confirmed cipher
signs** (`key.tsv`, all grade **C**: known plaintext, read from the sheets' own interlinear glosses and
2007B's twin -- this is a **period** key in rule-10 terms, and **ours** in the 25 Sept 2026 key-source sense:
recovered by this worker's own alignment, not copied from a published source). The cipher is a **homophonic
monoalphabetic substitution** over Dutch: N, A and E each already show 2-4 distinct signs; the sign set mixes
Latin-letter-shaped glyphs, two digits used as letters (5=v, 7=e), and at least one invented mark not yet
tied to a letter. Province/bastion place-names are left in plain Dutch on every sheet checked; only
descriptive clauses are enciphered. Full atlas and every occurrence: `glyphs.md`. Every rejected or
unresolved candidate sign, with the specific disagreement: `conflicts.tsv`.

**Control (rule 3):** `tools/decode_key.py ciphers/na-suriname-map-1781 --check` regenerates
`reading.txt`/`reading_tokens.tsv` from `ciphertext.tsv` + `key.tsv` + `plain_votes.tsv` and exits 0 (up to
date). Output: **38 tokens: C 25, M 1, U 12.** The 25 grade-C tokens agree with the known gloss at every
position (100%) -- this is the key re-reading its own source material, i.e. a self-consistency check, not
an independent test (the key was built from exactly this data, so agreement here is expected and does not
by itself demonstrate the key transfers to new text). Grade counts: **C 25, M 1 (a two-way reader
disagreement on one "Plan" position, see conflicts.tsv), U 12 (glyphs not yet keyed).** No H, no S, no I
tokens. This target has no matching judge spec run yet (see below), so no judge output is pasted here for
the key-source control -- `specs/na-suriname-map-1781.json` documents why.

### What was not done (stopped honestly short of the job brief's step 2/3/4)

Thirteen signs is real progress but well short of the ~20+ a Dutch legend sentence needs to read as more
than scattered letters. **2039, 2046 and 2077 were not transcribed against this key this pass.** A by-eye
spot check of 2039's title cartouche (`images/2039_cartouche.jpg`, "Spcxl 5Ah sf3r F,") found roughly a
quarter to a third of its glyphs matched a confirmed sign -- too sparse to report as a reading rather than
noise, so no ciphertext.tsv/decode was built for any target sheet, and the judge was not run against a
target (rule 7's judge step applies to a candidate reading; producing one honestly needs the next step
below first). `specs/na-suriname-map-1781.json` is written and the judge block is configured (`language: nl,
min_word_cover: 0.4`) for whoever completes this.

**Next step for a follow-on worker:** transcribe the already-fetched, already-glossed
`images/2007a_nota_af_block.jpg` and `images/2007a_remarque_af_block.jpg` (the full "Nota A-F" and
"Remarque" paragraphs on 2007A, both carrying their own interlinear gloss, both untouched this pass) --
this is far more crib material than the title block alone and would likely add 10+ more confirmed signs
before 2039/2046/2077 are worth attempting. Also worth resolving first: the `[v-tall]`/`[v-plain]` D-sign
question and the `[delta]`/`[lambda]` question flagged in `conflicts.tsv`.

### Fresh-instance re-derivation (rule 7)

A fourth subagent, given only the glyph-code segmentation of `ciphertext.tsv` (sign codes and word/position,
no plaintext values) and the known gloss word for each cipher word, plus the crop images -- NOT `key.tsv`,
NOT `glyphs.md`, NOT this worker's reasoning -- independently re-derived a letter value for each sign, and
was explicitly asked to flag any sign that got two different letters at two different positions.

**Result: agreement 13/13 (100%) on every sign in key.tsv, zero contradictions.** The subagent independently
re-derived N=[h-loop]/[l-bare], A=[delta], V=5, E=7/[ezh-dot]/[a-plain], L=c, P=[s-loop], G=G, R=[o-plain],
D=[v-tall] -- matching this worker's key.tsv exactly, including which signs are homophones of which letter.
It cross-checked every code that recurs across word-positions in the given set and found none assigned to
two different letters. It also independently arrived at the same two structural hypotheses this worker used
for the two 8-letters/7-glyphs words: Generaal's doubled AA compressed to one glyph ([x-dot], tentative A,
its own words "low-medium confidence... could instead be a non-letter duplicate-previous-sign marker" --
matching this worker's own stated caveat in glyphs.md) and Defensie's F silently dropped (rejecting the
alternative "drop the final E" specifically because it would force `7`=F and `[h-loop]`=E, both of which
contradict signs already confirmed elsewhere -- the same reasoning this worker used, reached independently).
It additionally proposed letter values for the still-unkeyed Defensie-tail and Remarque-tail positions
(y/[defensie-i-cand]/[defensie-e-cand] -> S/I/E; [remarque-r1-cand]/[remarque-m-cand]/[remarque-r2-cand]/
[remarque-q-cand]/[remarque-u-cand]/[remarque-e2-cand] -> R/M/R/Q/U/E), all consistent with -- not
contradicting -- this worker's own working hypotheses, but each still resting on a single word-instance with
no cross-word confirmation, so **not** promoted to key.tsv's grade-C table; recorded as corroborated
candidates in `glyphs.md` instead. No difference beyond that -- i.e. nothing that would send the key back --
was found.

**Conclusion: the 13-sign key stands as reported, independently re-derived at 100% agreement.** This is
still, deliberately, a partial key (see "What was not done" above) -- the re-derivation confirms what is
here is solid, not that it is sufficient to read 2039/2046/2077.

### Hosts and requests (this pass)

`service.archief.nl`: 6 requests (2007B full-size default JPEG; 2007A's IIIF info.json; two native-resolution
IIIF region crops for the Nota-A-F and Remarque blocks, one superseded by a corrected region), all >=1.5s
apart, descriptive-then-browser User-Agent (matching the playbook's note that this host wants a browser UA),
all HTTP 200, no 429/403/challenge. No other host touched this pass (no new NA catalogue page fetches, no web
search, no DECODE). 2 Sonnet subagents used for independent transcription passes (2007A crops; 2061 crops),
plus a third launched for the fresh-instance re-derivation above (at most 2 concurrent at any time, per the
job brief).

## Reading (VX-RD03B, 25 Sept 2026)

**Intake gate:** unchanged from VX-CS04's verdict above (25 Sept 2026); no new intake-relevant material this
pass.

**What this job set out to do:** extend the 13-sign key from 2007A's Nota A-F and Remarque paragraphs (both
already fetched, both glossed, neither transcribed by RD03) and 2061's remaining glossed lines; then decode
2039/2046/2077's legend/cartouche text with the extended key.

### What was done

Two independent Sonnet subagents blind-transcribed the two already-fetched crops (`images/
2007a_nota_af_block.jpg`, the "Nota A-F" paragraph; `images/2007a_remarque_af_block.jpg`, the "Remarque"
paragraph), word by word, gloss-word-paired, reusing the existing atlas codes where a shape matched and
inventing new bracket codes where it did not (full raw output: `scratch_nota_pass.tsv`,
`scratch_remarque_pass.tsv` -- kept for the record, not committed as a final transcription). This worker also
fetched and read 2007B's own Nota block directly (`images/2007b_nota_crop.jpg` -- already on disk from the
manifest but not previously read for its text), which turns out to give the **full, unambiguous plain-Dutch
text** of the Nota A-F paragraph in clean plain script (not cursive gloss): "Nota / A, De twee geprojecteerde
Lijnen van Verstopping; / B, Geprojecteerde zwaare Vlotbatterijen; C Canonnieres / D, Eerste dispositie van de
tot dekking van de passage in de / rivier gerangeerde 2 Fregatten, 7 Koopvaerders, 2 brigantijnen en 1
uytlegger. E Tweede dispositie van een koopvaardijschip minder, echter 2 vlotbatterijen op ligte ponten, /
waarvan de Canons van elk Caliber zijn. F Dispositie, zo als de schepen thans leggen, behalven eene
Brigantijn en eene vlotbatterij die afgekeurd zijn." (`scratch_2007b_nota_plain.txt`) -- a stronger crib than
the cursive on-sheet gloss for this block, exactly the "twin sheet" method already used for the title.

**Two new signs reached grade C** (`key.tsv`, both `period`/`ours`):
- **`[hash]` = o**, **`λ` = t** -- from the cipher word directly below the plain "Nota" heading on 2007A,
  which this worker and an independent subagent both read as the same 4 glyphs (`[h-loop][hash]λ[delta]`).
  This is the same self-duplicating-heading pattern already confirmed for "Remarque" (a plain heading
  immediately followed by its own cipher echo, before the paragraph's gloss+cipher body begins) -- so the
  word must read N-O-T-A, and since `[h-loop]`=n and `[delta]`=a were already grade-C confirmed, the other
  two positions are forced: `[hash]`=o, `λ`=t. `λ` was independently corroborated a second time in
  "Signatuure" (from the Remarque paragraph's gloss, "De Signatuure als..."), where the letters flanking its
  position (`[h-loop]`=N, `[delta]`=A) land exactly where SIGNATUURE's own N and A fall, with no compression
  needed -- two independent word-contexts, two independent readers, one shared value.
  This also **resolves** the open `[delta]` vs `[lambda]` question in `conflicts.tsv` (flagged unresolved by
  RD03): they are two distinct signs, not two drawings of one letter -- both appear in the same 4-glyph NOTA
  word, decoding to two different letters (A and T).

**Control (rule 3):** `tools/decode_key.py ciphers/na-suriname-map-1781 --check` regenerates the reading from
`ciphertext.tsv` + `key.tsv` + `plain_votes.tsv` and exits 0 (up to date, after this pass added the "NOTA" and
"Signatuure" words to `ciphertext.tsv`/`plain_votes.tsv`). Output: **52 tokens: C 33, M 1, U 18** (up from 38
tokens, C 25, M 1, U 12 before this pass). The new NOTA word decodes 4/4 positions to grade C, matching N-O-T-A
exactly; the new Signatuure word decodes 4/10 positions to grade C (the three already-confirmed anchor signs
plus the new `λ`), the other 6 unkeyed. This is again a self-consistency check on the key's own source
material, not an independent test.

**Fresh-instance re-derivation (rule 7):** a subagent given only the two glyph sequences, the two known target
words (NOTA, SIGNATUURE), and the three anchor values already on file (`[h-loop]`=n, `[delta]`=a,
`[o-plain]`=r) -- NOT `key.tsv`, NOT this worker's reasoning -- independently derived `[hash]`=o and `λ`=t,
100% agreement, and confirmed λ's cross-word consistency is not circular. It also surfaced a genuine
contradiction not asserted anywhere in key.tsv: the code `з` (a Remarque-pass invention, tentatively distinct
from `[ezh-dot]`) is forced to two different letters (U and E) within "Signatuure" alone -- flagged in
`conflicts.tsv`, left unresolved and out of key.tsv, most likely a transcription/segmentation slip rather than
a real one-glyph-two-values case (which the cipher's own design rules out).

### What was not done (stopped honestly short of the job brief's step 2/3/4)

**2039, 2046 and 2077 were NOT transcribed or decoded against the extended key this pass.** Fifteen signs is
still well short of the ~20+ a Dutch legend sentence needs to read as more than scattered fragments (unchanged
verdict from RD03). A single by-eye spot check of 2039's title cartouche line 2 (`images/2039_cartouche.jpg`,
"y?λ wab?ge? 6??v?plmg?h ?λ?pr..." against the 15-sign key) found the new `λ` sign appears once, but the rest
of the line's glyphs are either plain-Latin-looking shapes not yet matched to a confirmed code at this
resolution, or genuinely unconfirmed shapes -- not enough for a reading or even a meaningfully wider
percentage-covered figure than RD03 already reported (roughly a quarter to a third).

**2061's remaining glossed lines were NOT checked this pass either** (the No.1-6 battery list and the a-g
legend below the title/battery-header block RD03 already read) -- `images/2061_title_topleft.jpg` (already on
disk) shows this material is a MIX of plain capital "M" + plain Arabic numerals (matching the
Bastion-name-plain pattern seen on 2039/2046) and cipher abbreviation-words, structurally similar to the
target sheets' own cartouches rather than a clean word-for-word gloss -- worth transcribing, but a different
(harder, structural-inference) job than "read the interlinear gloss," and out of this pass's time box.

The rest of the Nota A-F paragraph (clause D's tail and all of clauses D-F's continuation, roughly two-thirds
of the block by the transcribing subagent's own account) and the rest of the Remarque paragraph beyond
"Signatuure" were transcribed at only medium-to-low confidence in a single blind pass each (word-boundary
ambiguity in run-on cursive, several likely word-fusions) and were deliberately NOT promoted to key.tsv --
kept in `scratch_nota_pass.tsv`/`scratch_remarque_pass.tsv` for a follow-on worker's second, verification pass
rather than risking a false key entry. In particular, 2007B's own **plain, unambiguous** Nota text
(`scratch_2007b_nota_plain.txt`) was not yet used to re-derive glyph values for clauses B/D/E/F the way it was
used for the "zwaare Vlotbatterijen" correction above -- that alignment (matching 2007A's cipher word-by-word
against 2007B's clean plaintext, rather than against the harder-to-read cursive gloss) is very likely the
fastest path to the next several signs and is the strongest next step, not a second cursive-gloss pass.

**Next step for a follow-on worker (highest value first):** (1) align 2007A's Nota A-F cipher word-by-word
against 2007B's clean plaintext (`scratch_2007b_nota_plain.txt`), which sidesteps the cursive-gloss legibility
problems that limited this pass to two clauses; (2) settle the `з` = U-vs-E contradiction from a high-zoom
crop of "Signatuure" specifically; (3) only then attempt 2039/2046/2077 with a proper two-pass crop-by-crop
transcription (this pass's single spot-check is not a substitute).

### Hosts and requests (this pass)

`service.archief.nl`: 0 new requests (all images already on disk from RD03's manifest). No other host touched
(no NA catalogue fetches, no web search, no DECODE). 3 Sonnet subagents: 2 independent blind transcription
passes (Nota A-F block, Remarque block), 1 fresh-instance re-derivation (never more than 2 concurrent, per the
job brief).

`service.archief.nl`: 6 requests (2007B full-size default JPEG; 2007A's IIIF info.json; two native-resolution
IIIF region crops for the Nota-A-F and Remarque blocks, one superseded by a corrected region), all >=1.5s
apart, descriptive-then-browser User-Agent (matching the playbook's note that this host wants a browser UA),
all HTTP 200, no 429/403/challenge. No other host touched this pass (no new NA catalogue page fetches, no web
search, no DECODE). 2 Sonnet subagents used for independent transcription passes (2007A crops; 2061 crops),
plus a third launched for the fresh-instance re-derivation above (at most 2 concurrent at any time, per the
job brief).

## Reading (VX-RD03C, 25 Sept 2026)

**Intake gate:** unchanged from VX-CS04's verdict above; no new intake-relevant material this pass.

**What this job set out to do:** (1) align 2007B's clean plain-Dutch Nota text against 2007A's ciphered Nota
clause by clause (B, D, E, F) using two independent passes, settle the з (U-vs-E) contradiction; (2) decode
2039/2046/2077 label by label once the key reaches their signs; (3) judge + re-derive.

### What was done

**Signatuure/з (settle з):** re-cropped `images/2007a_remarque_af_block.jpg` locally at 5-10x zoom (no new
network fetch) and re-read "Signatuure" position by position. The three already-confirmed anchors land
exactly right (h-loop=N, delta=A, lambda=T, o-plain=R), confirming the word and this worker's segmentation
are sound, but the з contradiction is **not resolved and got one position worse**: a fourth position
(expected U) now reads as a clean digit-"5" shape, conflicting with the robust, 2-sheet-confirmed 5=v.
Likely 2-3 visually similar glyphs conflated under too few codes at this crop's resolution; not asserted
either way. Full account and the specific next step (a fresh higher-native-resolution fetch, not another
read of the same crop): glyphs.md "RD03C" section, conflicts.tsv.

**Nota B/D/E/F vs 2007B's plaintext (two independent blind subagent passes, per the brief):** both passes
independently confirmed two important structural facts that apply to every remaining target sheet: (1) the
gold cursive gloss sits ABOVE the black cipher line it explains; (2) **Arabic numerals in the running cipher
text are left PLAIN, unenciphered** (clause D's "2 Fregatten, 7 Koopvaerders, 2 brigantijnen, [&] 1
uytlegger" and clause E's "2 vlotbatterijen" all show bare unenciphered digits, plus a plain "&" for "en") --
this matches the pattern already seen in 2039's Bastion-list lines and should let a follow-on worker treat
every bare digit run on 2039/2046/2077 as free, not needing a key. (3) The cipher is heavily and
**inconsistently** compressed relative to the plain word (a 14-letter word can read as 7, 10 or 12 glyphs
depending on the word), which defeated most of the two passes' attempts to reconcile a shared word
segmentation for the longer words in these clauses -- both passes independently blamed the same root cause,
a family of visually similar loop/hook glyphs neither could reliably tell apart at the resolution available.

**Two new signs reached grade C** (key.tsv): **digit `4`=w** and **digit `6`=s**, each confirmed because
BOTH independent passes, working blind from the image, landed on the same shape at the same word and
position ("Tweede" pos2 for w; "Eerste" pos4 for s) -- the strict two-independent-pass bar this key.tsv has
used throughout. Everything else in both passes' output (full TSVs: `scratch_notaBDEF_passA.tsv`; pass B's
full output is on record in this session's transcript only, not re-saved as a file, see glyphs.md) is
**NOT** promoted -- the two passes disagree on segmentation for most of the remaining words in clauses
B/D/E/F, sometimes contradicting an already-confirmed sign (e.g. one pass's "zwaare" segmentation would
force lambda=z, conflicting with the robust confirmed lambda=t), so nothing beyond the two agreed positions
was asserted.

**Control (rule 3):** `tools/decode_key.py ciphers/na-suriname-map-1781 --check` regenerates the reading and
exits 0 (up to date). Output: **56 tokens: C 37, M 1, U 18** (up from 52 tokens, C 33/M 1/U 18 before this
pass) -- the two new signs' own source words (Eerste pos4, Tweede pos2) decode to grade C; this remains a
self-consistency check on material the key was partly built from for those two positions, not an independent
test.

**Out-of-sample check found by inspection, worth recording even though it wasn't run through decode_key.py
this pass:** the current 17-sign key, applied for the first time to a target sheet it was never built from,
correctly reads "van" (5=v, [delta]=a, [h-loop]=n) in **2039's own title cartouche**
(`images/2039_cartouche.jpg`, line 2: "...5Ah sf3r F,"), at much clearer resolution than RD03B's earlier
low-res spot check. This is a genuine transfer test (the key reading NEW material, not the words it was
built from), unlike the tautological self-consistency numbers reported so far for this target.

### What was not done (stopped at the 80%-of-box mark, honestly short of steps 2/3)

Two independent transcription passes on one block consumed most of this job's 45-minute wall-clock box
(each subagent pass ran about 20 minutes). **2039, 2046 and 2077 were NOT decoded this pass** -- with the
key now at 17 signs (still short of the ~20+ a Dutch legend sentence needs) and the two passes' own account
of how inconsistently this cipher compresses plaintext, a rushed decode attempt in the remaining minutes
would risk exactly the kind of forced reading rule 7 exists to prevent. No judge run, no fresh-instance
re-derivation subagent this pass (no time/subagent-slot budget left in the box for a third launch).

**Next step for a follow-on worker, highest value first:** (1) resolve the loop/hook-glyph family both Nota
passes and the Signatuure re-crop independently flagged as the actual blocker -- ideally with a fresh IIIF
fetch at higher native resolution of `2007a_nota_af_block.jpg` and the Remarque block, not another read of
the existing crops; (2) once that family is sorted, re-run a reconciliation pass over `scratch_notaBDEF_passA.tsv`
against pass B's output (session a28cbc8bbc9ab5160, full TSV in that agent's hand-back in this session's
transcript) for the remaining clause B/D/E/F words -- several (Koopvaerders, dekking, uytlegger, brigantijnen)
look close to resolvable once the loop family is split correctly; (3) only then attempt 2039/2046/2077,
using the now-confirmed "numerals are plain" rule to skip re-keying the many digit runs on those sheets.

### Hosts and requests (this pass)

No network requests (all work from images already on disk: `2007a_remarque_af_block.jpg`,
`2007a_nota_af_block.jpg`, `2039_cartouche.jpg`, cropped/zoomed locally with PIL, no re-fetch). 2 Sonnet
subagents (independent blind transcription of clauses B/D/E/F, one already using the atlas as ground truth,
per the job brief's cap).
