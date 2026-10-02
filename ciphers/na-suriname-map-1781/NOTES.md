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

## Reading (VX-RD03D, 25 Sept 2026) -- final worker on this target, LANE VX

**Intake gate:** unchanged from VX-CS04's verdict above; no new intake-relevant material this pass.

**What this job set out to do:** (1) resolve the loop/hook-glyph family + the з contradiction via native-res
crops; (2) count, per target sheet (2039, 2046, 2077), which signs it uses and how many are keyed now;
(3) decode each target as far as the key allows, label by label; (4) judge + fresh-instance re-derivation.

### Step 1: the loop/hook-glyph family was a transcription-precision problem, not a structural one

The IIIF native-res crops already on disk (`2007a_nota_af_block.jpg`, `2007a_remarque_af_block.jpg`) turn
out to already be native pixel density (info.json's own `sizes`/`maxWidth` confirm 8998px is the sheet's true
native width, and the region requests already returned 1:1 pixels for their crop area) -- there is no
"higher native resolution" left to fetch; RD03C's suggestion to re-fetch was based on an unverified
assumption. What DID work: a careful local re-read at 5x zoom of clause B's "zwaare" (`images/strips/
clauseB_full.jpg`, JPEG since GAPS7 2 Oct 2026, PNG original at commit fc921145, already on disk). Pass A's transcription had read this word's first glyph as `λ`, which
-- forced against Z-W-A-A-R-E -- produced the "λ=Z" contradiction RD03C flagged as the real blocker. Re-read
at higher local zoom, that glyph is clearly a distinct trident/fork shape (`ψ`), not λ. **The contradiction
resolves as a pass-A mis-segmentation, not a real one-glyph-two-values case** -- consistent with every other
apparent key.tsv conflict so far. With `ψ` correctly separated out, "zwaare" reads as 6 glyphs for 6 letters
with zero compression, and THREE already-confirmed signs (`4`=w, `[delta]`=a, `7`=e) land exactly on their
expected position, unforced -- a genuine transfer confirmation within the same source sheet. Two new signs
surface at single-instance confidence (`ψ`->Z candidate, a dot-checkmark shape->2nd A candidate,
`[o-tail]`->R candidate) but are NOT promoted to key.tsv, per this file's own >=2-independent-read bar (see
glyphs.md "RD03D" section, conflicts.tsv). The з/Signatuure U-vs-E-vs-5 conflict (RD03C) was re-examined
(`images/2007a_remarque_af_block.jpg`, the "De Signatuure als..." line) but **not resolved** this pass --
this worker's own read of that specific word did not clearly reproduce the position-4/5/6/9 alignment
RD03B/RD03C report, and forcing a resolution from one more uncorroborated read would repeat the mistake
already flagged in this file; left open for a successor with a dedicated two-pass reconciliation of that one
word.

### Step 2: sign coverage on 2039, 2046, 2077

Two Sonnet subagents independently transcribed cipher glyphs on the three target sheets against the current
17-sign key.tsv (mechanical matching only, not asked to interpret meaning), plus this worker's own direct
read of 2077's cartouche and legend block (native-res local crops of `images/2077_full.jpg`, fetched this
pass -- default_full_url, capped 5000x2385 vs the sheet's true 10711x5110, 1 request to service.archief.nl).

- **2077** (this worker + 1 subagent, cross-checked): cartouche + 2 legend entries ("a", "q"), 27 glyphs
  sampled -- **9/27 (33%) high-confidence MATCHED**, 4/27 (15%) tentative-only matches not counted in the
  headline figure, 14/27 (52%) genuinely UNMATCHED. The cartouche's first word decodes cleanly and
  unforced to **PLAN** ([s-loop] c [delta] [h-loop] = P-L-A-N), independently confirmed by this worker's own
  direct read and the subagent's cross-check against the reference crops -- the strongest, most reliable
  single result of this pass. No other run of 4+ consecutive matched glyphs was found in the two legend
  entries sampled (only ~2 of ~18 entries checked; most of the sheet's legend text is untranscribed).
- **2039 + 2046** (1 subagent, single uncorroborated pass, M-grade not confirmed): **72 glyphs on 2039
  (46 matched, 64%)**, **56 glyphs on 2046 (36 matched, 64%)** across the full 3-line title on each sheet.
  This subagent did NOT find the exact 4-glyph "PLAN" run on either sheet: on 2039 it read the cartouche's
  second word as `[s-loop][delta][h-loop]` = P-A-N (missing the L in between, a near-miss) rather than the
  "van" (`5`[delta][h-loop] = V-A-N) that RD03C's NOTES.md entry above reported finding at the same
  position. **This is an unresolved disagreement about a single glyph's identity (digit `5`=v vs `[s-loop]`=p
  at that specific position), not a new finding either way** -- this worker ran out of time-box to settle it
  with a third independent read before the 80%-of-box mark and is flagging it rather than picking a side.
  No 4+-glyph run on 2039 or 2046 decoded to a clear, plausible Dutch word (2039's best candidate, "ENSPE",
  is flagged by the subagent itself as unlikely to be meaningful; 2046's best run was only 3 glyphs, "DER").
  These figures are a single pass and should be treated as directional (coverage is clearly non-trivial and
  in the same range on both sheets) rather than a precise, confirmed percentage.

**No formal ciphertext.tsv/decode was built for 2039, 2046 or 2077 this pass.** Building one honestly needs a
transcription both this file's own standard (>=2 independent reads agreeing) and rule 7 would accept as a
candidate reading; what exists after this pass is single-pass coverage counts (2039/2046) and one
double-checked 4-glyph word (2077's "Plan") -- real progress, but not a base to decode a full legend/cartouche
from without risking exactly the forced-reading problem rule 7 exists to prevent. No judge was run (nothing
meeting the bar of a candidate reading exists to judge), and no fresh-instance re-derivation subagent was
launched this pass (no new key.tsv entries were promoted, so there is nothing rule 7 requires re-deriving).

### State at close (final worker, LANE VX)

**Status: partial.** What is established (grade C, ~C37/M1/U18 self-consistency on the key's own 56-token
source material, `tools/decode_key.py --check` exits 0): a 17-sign homophonic-substitution key for this
1781 Wollant fortification-cipher family, built entirely from 2007A/2061's own on-sheet interlinear glosses
and 2007B's plain twin -- period, ours, in the 25 Sept 2026 key-source sense. The key transfers out of sample:
it reads "van" (2039, RD03C) and "Plan" (2039 near-miss / 2077 confirmed, this pass) correctly on sheets it
was never built from. What is NOT established: a reading of any target sheet (2039, 2046, 2077) -- coverage
sits at roughly a third to two-thirds of running-text glyphs depending on sheet and method, well short of the
~20+ signs (currently 17, several still single-homophone) a Dutch legend needs to read as continuous prose
rather than isolated confirmed words. Grade counts across all material on file: **C 56, M 1, U 18** (key-source
label lines only); zero target-sheet tokens graded at all (none transcribed to the reliability bar this file
requires).

**Single best next step for a future lane** [run 2 Oct 2026, GAPS-na-suriname-map-1781: settled as "van", see "## GAPS-na-suriname-map-1781 (2 Oct 2026, account-4)" below]**:** settle the "van" vs "PAN" disagreement on 2039's cartouche line 2
with one more independent, high-zoom read of that specific 3-glyph position (this is a fast, cheap, high-value
check -- it either confirms digit `5`=v transfers out of sample too, strengthening the key, or reveals a second
homophone/mis-reading that would need fixing before any target decode is attempted); then use 2077's
already-open, already-partly-read legend block (`images/2077_full.jpg`, `images/2077_legend_5000.jpg`, both on
disk) as the next transcription target over 2039/2046, since it mixes plain Dutch entries with ciphered ones on
the same list -- a crib structure similar to 2007A/2061's gloss pattern, and likely the fastest path past the
current ~17-sign ceiling. A full two-pass transcription of 2007A's remaining Nota/Remarque clauses (still only
partly read, per RD03B/RD03C) is the other standing option and would add more signs before any target sheet is
attempted, per every prior worker's own recommendation in this file.

### Hosts and requests (this pass)

`service.archief.nl`: 1 request (2077's default_full_url, capped 5000x2385; >=1.5s spacing n/a, single
request). No other host touched. 2 Sonnet subagents (mechanical sign-coverage counting on 2039+2046, and on
2077; read-only, no file edits by either subagent). This worker's own direct reads used only images already
on disk plus the one 2077 fetch above, all local PIL crops/zooms, no further network calls.

## GAPS-na-suriname-map-1781 (2 Oct 2026, account-4)

Brief: `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the Verdict step of the section below, run verbatim:
one blind high-zoom read of the 3-glyph van-vs-PAN position on 2039's cartouche line 2 (`images/2039_cartouche.jpg`).

**Where the position is.** On the crop `images/2039_cartouche.jpg` (1750x1185 px, native-resolution), the large
title line reading "Spext 5Ah sf3r F," (the line RD03C and RD03D both call line 2; a shorter band sits above it)
has its ink in rows y 150-215. A column ink profile over those rows gives the word runs x 667-800 (word 1),
x 831-910 (word 2, the disputed 3-glyph word), x 929-1006 (word 3), x 1027-1068 (word 4). The crop sent to the
blind reader is the box (822,135)-(920,222), enlarged 4x with PIL (Lanczos) to 392x348; a native-size copy is kept
as `images/2039_cartouche_word2_native.jpg` (3 KB). No network request was made (0 requests, every host).

**Two independent reads, recorded in this order.**
1. This worker's own read, at 3x on the line crop (600,70)-(1100,235), written down before the blind call ran:
   glyph 1 is a numeral-5 shape (flat top bar, short vertical, bowl at the bottom), unlike the looped long-s that
   opens word 3 ("sf3r") on the same line; glyph 2 a Delta; glyph 3 the h-loop. Read: `5` `[delta]` `[h-loop]`.
2. One blind Sonnet subagent call, given only the 4x word crop and the question (the two options for glyph 1:
   numeral-5 shape vs looped long-s/p shape; no key, no notes, no context): "Glyph 1: a short flat-ish top stroke
   at upper left, a short descending stroke, then a thick curving bowl ... It is not a tall looped long-s or p,
   since it has no tall ascender or descender loop" -- option A (numeral 5) at 75%; glyph 2 "Greek capital Delta,
   or Latin A without a crossbar" at 70%; glyph 3 "Latin lowercase h" at 85%; "Overall the word reads visually
   like '5Δh'".

**Result.** Both reads give `5` `[delta]` `[h-loop]`, which the 17-sign key.tsv reads as v-a-n: "van". RD03D's
`[s-loop][delta][h-loop]` = "PAN" at this position was a single uncorroborated subagent pass and is now outvoted
3 reads to 1 (RD03C's by-eye read, this worker, the blind reader); the three reads that agree were made at 3-4x
on the native crop, RD03D's at the resolution of a whole-cartouche pass. Grade of the word: S (cryptanalytic
transfer of a C-grade key to a sheet it was not built from, with no plaintext on this sheet to check against;
3 tokens, 3 S, 0 M). The control for this step is the design of the read itself: the blind reader had the two
options and nothing else, and a shape that could have been read as the long-s/p option was in fact read as the
numeral at 75%; this is a transcription check, not a solver family, so rule 3's matched synthetic control does
not apply. What it changes: the key's digit `5`=v is now seen out of sample on a target sheet (previously only
in 2007A's and 2061's glossed "van"), and there is no second homophone or mis-reading to fix at this position
before a 2039 decode is attempted. What it does not change: no reading of 2039 exists yet (no ciphertext.tsv,
no two-pass transcription), the status stays `partial`, and `tools/decode_key.py ciphers/na-suriname-map-1781
--check` still exits 0 on the unchanged key-source reading (56 tokens: C 37, M 1, U 18). Vision calls: 1
subagent call; this worker's own looks: 2 (the line crop at 3x, the third-title-line crop at 3x that located the
line; the orientation look did not carry a read).

Not found: no prior reading of this word or of 2039's cartouche anywhere in this folder's search log or in the
web and blog check at the end of this file (a search result, rule 10, not a novelty verdict).

## GAPS2-na-suriname-map-1781 (2 Oct 2026, account-4)

Brief: `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the Verdict step as rewritten at 02:02 UTC, run verbatim:
"search the 4.VEL 2030A5-2090C block (95 catalogue records, VX-CS04 read them for cipher only) for a plain Nieuw Amsterdam
plan to use as 2039's legend crib, ~$2". Clock read at start 03:34 UTC; intake gate `tools/intake_gate_check.py` exit 0
(edition/page citation found within 6 lines). No reading was made or changed; `tools/decode_key.py ciphers/na-suriname-map-1781
--check` exit code is pasted at the end of this section.

**Route (metadata first, 8 requests in all).** Instead of 95 item pages, one download of the whole 4.VEL finding aid as EAD
2002 XML (`https://www.nationaalarchief.nl/onderzoeken/archief/4.VEL/download/xml`, HTTP 200, 6,798,490 bytes, 3,969
components) parsed offline with `xml.etree`. The 2030-2090 block is 100 components (95 items plus 5 range headers), every
one with a `dao` METS link, written unmodified to `vel_2030-2090_catalogue.tsv` (invnr, title, date, scopecontent,
physdesc, materialspec, bioghist, altformavail, parent, METS URL). The EAD confirms the catalogue wording VX-CS04 read on
the item pages (2039 "Met profil Gedeeltelijk in cijferschrift"; 2046 "In cyferschrift. Met profil."; 2061 "In cyferschrift,
met verklaring."; 2077 "In cyferschrift en gedeeltelijke verklaring." -- the last is a cipher mention VX-CS04's item-page
read did not report, so the "no cipher word at all" sentence for 2077 in the Established section holds for the item page's
scopecontent as read then, not for the EAD). It also adds a column nobody had used: `altformavail` says which sheets are
facsimiled in den Heijer, *Grote Atlas van de WIC* II (2039 at p. 342, 2040 p. 342, 2032 p. 337, 2034 p. 338, 2035 and 2037
p. 339, 2033 p. 340, 2042 p. 354, 2048 p. 357, 2053 p. 358).

**Nieuw Amsterdam plans in the block** (title search on the TSV, 9 rows): 2031, 2032 (Desmarestz), 2033 (kopie), 2034/2034A
(1737), 2035 (1741), 2036 (regenbak), 2037 (Chambrier, 1744, French), 2038 (Hurter, 1778), 2039 (cipher, 1781), 2040
(Wollant, 1784), 2053/2053A (the redoubt opposite, Bernhardy, 1755). Two were fetched as one 2800-px IIIF overview each
(METS record, info.json, then `full/2800,/0/default.jpg`; service.archief.nl 6 requests, 1.6 s apart) because they bracket
2039 in date and the step needs a legend, not a title:

| invnr | native px | what the sheet carries (own look at 2800 px, plain Dutch read, no cipher) | crib value for 2039 |
|---|---|---|---|
| 2038 | 10833x11292 | Title "Plan van 't Fortresse Nieuw-Amsterdam"; capital legend A-K (A Bastion Holland, B Bastion Gelderland, C Bastion Overijssel, D Bastion Utrecht, E Bastion Groningen, F Oude Sluijs, G Project tot een nieuwe Sluijs, H Natuurlijke Creeq, K a projected work "om het Water in te laaten"); a lowercase building list of about 30 entries; "No. I tot No. VIII Batterijen"; signed "Fortresse Nieuw Amsterdam den 31 July 1778, J.C. Hurter" | **the crib.** Same fort, three years earlier, same physical size and the same scale as 2039 (both 0.44 x 0.425 El, 100 Rijnlandse roeden = 370 strepen, EAD physdesc/materialspec), with a lowercase lettered list of the kind 2039 enciphers as its a-u "Verklaringe der Letteren"; 2039's own plain bastion labels (Holland, Gelderland, Overijssel, Groningen; RD03C) match 2038's A-E |
| 2040 | 8066x6210 | "Pl. L. D."; title "PLAN Van de geprojecteerde Veraanderingen op de Fortr. N. Amsterdam, volgens Generael Defensie Plan L. A. aldaer te doen"; battery labels "6 Can. a 24 lb Calib", "4 Mortieren a 8 d. St." and the like; a Nota that the Redout Leijden profiles apply here too; signed Wollant | secondary: no lettered legend, but its artillery clauses are the vocabulary 2039 enciphers after each Bastion label (RD03C: "the artillery/measurement description after each does not" stay plain). Its title ties 2039's survey to 2007A/B ("Generael Defensie Plan L. A.") |

Not fetched (title or date makes them weaker cribs, and the 15-request ceiling): 2031-2037 (1737-1744, earlier works and a
French plan) and 2053/2053A (a different work). Their METS links are in the TSV.

**Result in numbers.** 95 items searched by title and scopecontent; 9 Nieuw Amsterdam rows; 2 fetched; 1 plain lettered
legend found (2038, about 9 capital + about 30 lowercase entries, not yet transcribed), 1 secondary artillery-label sheet
(2040). Grades: none -- this step transcribed no cipher token and changed no reading (the legend text quoted above is a plain
read of a plain sheet at 2800 px, to be transcribed properly from a native crop before use as a crib). Control: not
applicable -- a catalogue listing and an eye-check, not a solver family or a gate (rule 3). Vision calls: 0 subagent calls;
own looks 2 (the two overviews). Requests: www.nationaalarchief.nl 2 (item page 2039, EAD download); service.archief.nl 6
(2 METS, 2 info.json, 2 images); 8 in all, every one HTTP 200, 1.6 s apart, no challenge page.

Not found: no plain twin of 2039 catalogued as such (no "cijferschrift vertaald" row in the block the way 2007B is for
2007A); 2038 is a predecessor by another hand, so its legend letters need not map one-to-one onto 2039's a-u. Rule 10:
a search result, not a novelty verdict.

Housekeeping: `images/` is 37 MB tracked, 28 MB of it `images/strips/` from an earlier worker, already over the 30-MB line
before this step added 1.1 MB; a shrink in the AX2-SHRINK shape (manifest with cited_by, regen script, uncited strips
deleted) is a one-line suggestion for the lane, not this step's job.

`tools/decode_key.py ciphers/na-suriname-map-1781 --check` (2 Oct 2026, after this step): `ciphertext.tsv: tokens 56: C 37, M 1, U 18 / reading up to date`, exit 0.

## GAPS3-na-suriname-map-1781 (2 Oct 2026, account-4)

Brief: `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the two Verdict steps as rewritten at 03:42 UTC, run in order as
one job. Clock read at start 05:17 UTC; `tools/intake_gate_check.py na-suriname-map-1781` exit 0 before the step. No cipher
token was transcribed and no reading was made or changed (2039 was not decoded, per the brief); `tools/decode_key.py
ciphers/na-suriname-map-1781 --check` output is pasted at the end of this section.

**Step 1 -- plain Purmerent legend for 2046 (eye-check 2045A and 2042).** METS record then one 2800-px IIIF overview each
(service.archief.nl, 4 requests, 1.6 s apart, all HTTP 200), two own looks. Both sheets carry a plain Dutch lettered legend:

| invnr | native px | what the sheet carries (own look at 2800 px, plain Dutch, no cipher) | crib value for 2046 |
|---|---|---|---|
| 2042 | 2800x2231 at this size (Calvi, undated; EAD "Met aanwijzingen", facsimile den Heijer II p. 354) | title "Redoute PURMERENT", "RIVIER SURINAME opwarts"; lower-right framed box with a lowercase a-l legend: aa.a Battery van 9 Stukke 12 lb, bbb Battery van 9 Stukke, cc twee batteryen yder van een stuk 4 a 6 lb, d.d Plaats voor de Afdakken der battery gereedschap, e Officiers Huis, f Keuke en Magas. voor de [officers], g Quartier voor 75 Mann, h Keuke en Water magas. voor het quartier, i Wagt & Proviant magasyn, k Provost, l Buite wagt; scale "Voete Rhynlands"; signed Andr. Lud. Calvi | **the building crib**: a lowercase lettered building list of the kind 2046's enciphered legend is expected to be (2039's a-u is the same shape for Nieuw Amsterdam) |
| 2045A | 2800x2099 at this size (A. Dircks, drawn by cadet J.G. Dircks, undated; EAD "Met aanwijzingen") | header "Revier Suriname aen de Zuyd Sy seer moterig en ondiep, circa 6 kettings van de Redout aff"; capital A-H legend across the foot: A Redout Purmerent soo als deselve teegenswoordig sig in staad bevind, B Bastions welke veel te klyn syn om eenig Geschut daer in te konnen plaetsen, C Gragt om deselve welke onnoodig is en diend gevuld te worden, D Bedeckte Weg en Glassie welke tot een Capitaele Wall diend gemaekt te woorden, EF Profiel door de Linie EF, G Wagt Huys, H Sluys; "De gestippelde Linien wysen aen de Verbeetering"; scale "Maad Stok van 10 Roeden" | secondary: works vocabulary (bastion, gragt, bedekte weg, glacis, wagthuis, sluis) rather than buildings |

Verdict of step 1: plain Purmerent legends found on both inventory numbers checked, 2042 (lowercase a-l buildings) and 2045A
(capital A-H works). Neither is transcribed to the two-pass bar in this job (the brief's step 1 was an eye-check); the texts
above are a single plain read of a plain sheet at 2800 px, grade none, to be transcribed from native crops before use as a
crib. Which better serves 2046 depends on what 2046's legend enciphers, which is unknown until its a-? list is transcribed;
2042's building list is the closer shape. Catalogue dates: the EAD dates neither sheet; Calvi and Dircks precede Wollant's
1781 survey (2046, 2047 are the 1781 sheets), as Hurter's 1778 sheet precedes 2039.

**Step 2 -- 2038's plain legend block transcribed into `crib_2038_legend.tsv`.** The block was located on the 2800-px overview
by an ink-density map, not by eye (to stay inside the brief's five vision calls): a framed box lower right. One native IIIF
region fetch, 8400,7540,2360,3380 (x,y,w,h in 10833x11292 native px), saved as `images/2038_legend_native.jpg`
(service.archief.nl, 1 request, HTTP 200). `tools/iiif_lines.py --image images/2038_legend_native.jpg --region 60,40,1950,3240
--distance 40 --prominence 20 --lines-per-crop 5 --debug --out images/crops_2038 --prefix leg2038` (the region excludes the frame
lines, which had dominated the default profile: 12 "lines" at pitch 29 on the first run) found 53 line centres at pitch 52 px and
wrote 11 band crops of about five lines each, 1950 px wide, under `images/crops_2038/` with their own manifest.json. The debug
overlay was checked by its numbers (every centre gap under 1.6 pitch except the two tall header lines and one 91-px gap at
2582-2673), not by eye, for the same vision-cap reason; the reconciliation look found every crop cut in whitespace, with one
line (F) split across the 02/03 band edge and the signature split across 09/10 -- both recoverable, both passes read them.

Two blind Sonnet subagent passes (one crop set each, one Read per crop, no access to NOTES.md or each other; `passes/
crib_2038_passA.tsv`, `passes/crib_2038_passB.tsv`), then this worker's one reconciliation look at crops 02-09 as a single set
(the disputed rows), settling each disagreement from the ink and recording the alternatives in the TSV's `note` column.

Result in numbers: `crib_2038_legend.tsv` has 41 rows: 40 text rows (2 title lines, 35 legend entries -- capitals A, B, C, D,
E, F, G, I, K with no H and no J on the sheet; lowercase a-z without j, 25; the indented "van No: I: tot No: VIII: Batterijen"
line -- and 3 signature lines "Fortresse Nieuw Amsterdam / den 31. Julij 1778 / J. C. Hurter") plus one row for an ornate glyph
left of the a/ line that both passes read as a capital L and that may be a bracket (no text, not counted). Confidence (the
brief's H/M, plain-text reads): H 24, M 16 of 40. Pass agreement: 28 of 40 lines identical after label/punctuation
normalisation (0.700); 152 of 169 words (0.899). Words still open after reconciliation (M, alternatives in the note column):
C Overijzel/Overijsel; F Sluijs/Seluys (line cut at a band edge); K "af te neemen" (both passes) against this worker's "in te
neemen"; a "Inspectie Sluijs" (A, own look) against "Huijs" (B); i Spuyten; k Klyne Smeederij; n Timmerloos; p Casserne;
t "daar 't tans ?loot" (the last word sits under a tall flourish; A read "tuin sloot"); u "waar 't Sloe geplaast sal worden";
y Timmer=Loos (A "Erve"). Grades under rule 4: not applicable to the crib itself (plain text read from a plain sheet, no
key); it carries no cipher token and changes no reading.

Control: not applicable -- a transcription of a plain sheet and an eye-check, not a solver family or a gate (rule 3); the
two-pass agreement figures above are the reliability measure, and a row's M stays M until 2039's own enciphered entry is
aligned against it. Rule 10: 2038's legend is a crib on disk, a search result; it is not a reading of 2039.

Vision calls: 2 own looks (step 1) + 2 blind subagent passes + 1 reconciliation set = 5, the brief's cap. Requests:
service.archief.nl 5 (2 METS, 2 overviews, 1 native region), www.nationaalarchief.nl 0; all HTTP 200, 1.6 s apart, no challenge
page. Box 05:17-05:3x UTC of 55 minutes. Housekeeping: `images/` is now 41 MB tracked (37 before this step, 28 MB of it the
earlier `images/strips/`; this step added 2042 and 2045A overviews, the native legend region and 1.5 MB of crops) -- still the
AX2-SHRINK-shape job GAPS2 suggested for the lane, not this step's. `images/manifest.json` carries the three new items.

`tools/decode_key.py ciphers/na-suriname-map-1781 --check` (2 Oct 2026, 05:30 UTC, after this step): `ciphertext.tsv: tokens 56: C 37, M 1, U 18 / reading up to date`, exit 0.

`python3 tools/gaps_check.py na-suriname-map-1781` (2 Oct 2026, 05:3x UTC, after the section below was rewritten): `OK keep-going na-suriname-map-1781: keep going: 5 internal gap(s), 5 step(s) untried` / `gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped`, exit 0.

## GAPS4-na-suriname-map-1781 (2 Oct 2026, account-4)

Brief: `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the Verdict's cheapest step as rewritten by GAPS3 at 05:30 UTC,
and only that step: transcribe 4.VEL 2042's plain a-l legend into `crib_2042_legend.tsv` as a crib for 2046. Clock read at start
06:06 UTC; `tools/intake_gate_check.py na-suriname-map-1781` exit 0 before the step. No cipher token was transcribed and no
reading was made or changed (2046 and 2039 were not decoded, per the brief); `tools/decode_key.py --check` output is pasted below.

**Locating the box without a vision call.** On `images/2042_overview.jpg` (2800x2231, on disk since GAPS3) a frame-line and
ink-density profile of the lower right (long dark runs: top rule at overview y 1764, bottom at 2114-2115, uprights at x 2021 and
2528; eight text rows at pitch about 40 px between them) placed the framed legend box at overview x 2015-2535, y 1764-2116.
`info.json` gave the native size 6498x5177 (scale 2.32), so one native IIIF region 4590,4010,1390,990 (x,y,w,h, with margin)
was fetched once and saved as `images/2042_legend_native.jpg` (service.archief.nl, 2 requests in all, both HTTP 200, 1.6 s
apart). Inside that file the frame sits at y 79-105 / 876-898 and x 96-104 / 1273-1284 (row and column ink sums), so
`tools/iiif_lines.py --image images/2042_legend_native.jpg --region 110,110,1155,760 --prominence 20 --distance 40
--lines-per-crop 20 --top-margin 60 --debug --out images/crops_2042 --prefix leg2042` excludes the frame; it found 11 line
centres at pitch 87 (eight strong text rows at 78/168/252/336/420/508/594/696 plus weaker ascender rows between, by the
profile) and, since the interior is only 1155 px wide, wrote one whole-box crop `images/crops_2042/leg2042_L01.jpg` (1155x717)
rather than bands whose edges would fall on the weak rows (a two-line cut at the 8-line pitch would have landed on them). The
debug overlay was checked by its numbers, not by eye, to stay inside the vision cap.

**Two blind passes and one reconciliation.** Two blind Sonnet subagent passes (one crop, one Read each, no access to NOTES.md,
the 2038 crib or each other; `passes/crib_2042_passA.tsv`, `passes/crib_2042_passB.tsv`), then this worker's one reconciliation
look at a single montage (the native legend file with 2x zooms of the two spots the passes flagged: the end of line a and the
right end of line d, which both passes thought might be cut).

Result in numbers: `crib_2042_legend.tsv` has 13 rows = 11 lettered entries (a, b, c, d, e, f, g, h, i, k, l -- lowercase, no
j, the labels doubled or tripled for the batteries: a.a.a., b.b.b., c.c., d.d.) plus 2 continuation rows (h "Water magas: voor
het quartier.", i "ant magasyn."); entries e/f, g/h and i/k/l share physical lines, so the box's eight text rows carry eleven
entries; there is no title line inside the box. Confidence (the brief's H/M, plain-text reads): H 10, M 3 of 13. Pass agreement:
12 of 13 rows identical after label/punctuation normalisation (0.923); 51 of 52 words (0.981). The one disagreement, a's
"tb.derv." (A) against "tb.ders." (B), is settled from the 2x zoom as "℔ders." (the pound ligature plus "ders", 12-ponders) and
kept M; d's last word is complete on the sheet ("gereedschap." with its stop against the frame, not cut), Affdakken/Afdakken stays
open (M); k reads "Provost." on the own look and on GAPS3's 2800-px eye-check against both passes' "Provoost." (M). Both passes
rendered the ditto sign as "do"; the sheet has d° (b, f). Grades under rule 4: not applicable to the crib itself (plain text read
from a plain sheet, no key); it carries no cipher token and changes no reading.

Against GAPS3's eye-check of the same box (a single 2800-px read, grade none): every entry's substance is confirmed; the
two-pass text corrects "9 Stukke 12 lb" to "9. Stukke 12. ℔ders.", adds the "4. à 6. ℔." gun weights on c, "batterij gereedschap"
on d, "75. Mann" on g, and the h/i continuations.

Control: not applicable -- a transcription of a plain sheet, not a solver family or a gate (rule 3); the two-pass agreement
figures above are the reliability measure, and a row's M stays M until 2046's own enciphered entry is aligned against it.
Rule 10: 2042's legend is a crib on disk, a search result; it is not a reading of 2046, whose legend may encipher a different
list (2042 is Calvi's undated plan, 2046 Wollant's 1781 one; the building set may have changed).

Vision calls: 2 blind subagent passes + 1 own reconciliation montage = 3, the brief's cap. Requests: service.archief.nl 2
(info.json, native region), www.nationaalarchief.nl 0; both HTTP 200, no challenge page. Box 06:06-06:2x UTC of 45 minutes.
Housekeeping: this step added 0.4 MB to `images/` (the native region 142 KB, one crop and its debug overlay 240 KB); the folder
stays at 41 MB tracked against the 30 MB line, 28 MB of it the earlier `images/strips/` -- the AX2-SHRINK-shape job GAPS2
suggested for the lane is now also listed in the gaps section below. `images/manifest.json` carries the native region under
4.VEL 2042; `images/crops_2042/manifest.json` the crop.

`tools/decode_key.py ciphers/na-suriname-map-1781 --check` (2 Oct 2026, 06:14 UTC, after this step): `ciphertext.tsv: tokens 56: C 37, M 1, U 18 / reading up to date`, exit 0.

`python3 tools/gaps_check.py na-suriname-map-1781` (2 Oct 2026, 06:1x UTC, after the gaps section below was updated): `OK keep-going na-suriname-map-1781: keep going: 6 internal gap(s), 5 step(s) untried / gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped`, exit 0.

## GAPS5-na-suriname-map-1781 (2 Oct 2026, account-4)

Brief: `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the Premise check first (section at the end of this file,
verdict CLEAR TO TEST, `tools/intake_gate_check.py` exit 0 at 13:40 UTC), then the Verdict's cheapest step and only that
step: 2039's a-u "Verklaringe der Letteren" legend block -- crops, two blind passes and one reconciliation, ciphertext rows,
alignment against `crib_2038_legend.tsv`, decode with `tools/decode_key.py`. Clock read at start 13:26 UTC.

**Locating the block without a vision call.** `images/2039_cartouche.jpg` is not a native-resolution crop as its manifest
line said: template-matched on `images/2039_overview.jpg` (FFT normalised cross-correlation at 18 candidate scales) it
fits at ncc 0.86 only at half native resolution, covering native 564,564,3490,2362 (the bastion zoom, by the same test,
is native: ncc 0.93). Its row profile shows the title line and about 13 legend lines at pitch 45 crop px (90 native)
and ink to its bottom edge, and the overview's profile in the same columns shows the pitch continuing to overview y
about 925 (native about 3700). One native IIIF region 780,980,2100,2800 was fetched once (`images/2039_legend_native.jpg`,
633 KB, HTTP 200) and cut with `tools/iiif_lines.py --image ... --prominence 25 --distance 55 --lines-per-crop 2
--max-width 1200 --overlap 200 --debug` into 15 two-line bands x 2 segments = 30 crops (30 line centres at pitch 100;
crops 1.6 MB, left uncommitted and regenerable by the command in `images/manifest.json`, since the folder is over its
30 MB line). The region turned out too narrow on the right: every band's _s2 is cut at native x 2880 and the readers
report the line ends missing, so entries d, h and p and the ends of c, g, o and r are outside what was read.

**Two blind passes and one reconciliation.** Two blind Sonnet subagent passes (`passes/leg2039_passA.tsv`,
`passes/leg2039_passB.tsv`; brief `passes/leg2039_pass_brief.md`: shape codes only, no letter values, no access to
NOTES.md, the key or each other; one Read per crop), then this worker's one reconciliation look at a 7-crop montage of
bands L04-L07. Both passes found the same structure: the line under the title (L01), the lettered legend a, b, c, e, f,
g, i, k, l, m, n, o, q, r (labels plain, each followed by a cipher clause; the clauses are short, 7-40 signs), one
long entry labelled s further down, and below the legend a plain-labelled fortification list (Bastion Holland,
Gelderland, Overijssel, Groningen, Utrecht; Texiersburg, Cranie, Nassauw, Brunswyk, Weilburg; Redan Amsterdam, Redan
Alkmar; Schans aan ...) with plain gun counts and a cipher clause after each -- the same shape as the bastion block
RD03C saw. Own look: the recurring initial glyph of a, b, m, n is a looped thorn/p shape (coded `[thorn]`; A had
called it a curl, B an h with tail), the "3"-shaped sign is a plain 3 without the ezh dot and is kept distinct from
`[ezh-dot]`, the start of band L05 line 2 ("kq ra darλrotrh") is entry o's text continued, so B's doubtful "p" label is
not one, and no d, h or p label is inside the region.

Result in numbers: `ciphertext_2039_legend.tsv` has 374 sign rows in 16 lines (head + 15 entries: a 13, b 26, c 40,
e 36, f 30, g 8, i 13, k 12, l 7, m 13, n 8, o 13, q 25, r 24, s 73 -- c and s carry pass-B spill-over from their
neighbours at M; g is pass B only, pass A's g text sat inside its f row and was not split). Pass agreement after code
normalisation, by sequence alignment: 277 of 370 aligned positions (0.749); per entry head 28/29, a 10/13, b 15/26,
c 20/40, e 31/36, f 18/30, i 12/13, k 10/12, l 6/7, m 12/13, n 5/8, o 10/13, q 19/25, r 22/24, s 59/73. Conf H
(both passes, same sign) 277, M 97 (the other pass's sign in the note column). The bastion/redan lines (L07-L15) were
read by both passes but are not in the file: not this step's block.

Decode (rule 4, rule 7): decode.json job 2 applies key.tsv plus `key_2039_aliases.tsv` (two code spellings of signs
already in the key, `[lambda]`=t and bare `o`=`[o-plain]`=r, grade M) with every key row in `m_sources`, so a keyed
token on this sheet is M (the key is transferred from 2007A/2061, not read from plaintext here) and an unkeyed one U:
`tools/decode_key.py ciphers/na-suriname-map-1781` -> `ciphertext_2039_legend.tsv: tokens 374: M 121, U 253`;
`--check` exit 0 (13:44 UTC). Grades: H 0, C 0, S 0, M 121, I 0, U 253. 253 of 374 signs (68%) are outside the 17-sign
key: the legend hand uses many Latin-letter-shaped signs (k, l, r, g, p, h, d, w, f, m, b, q, x, t, 8, 9, 0) the key
has no row for.

**Alignment against crib_2038_legend.tsv, rule 3** (`align_2039_legend.py`, 20 shuffled-crib controls: letters shuffled
within each crib entry, lengths and stock kept -- a control that varies on the statistic's own axis):
- same-label (2039 entry x against 2038 entry x, best offset, fraction of keyed positions matching): real 0.269 vs
  controls mean 0.283, sd 0.021, p95 0.311; z -0.68; 15 of 20 controls at or above the real score -- **no signal**.
- free (best over all 25 crib entries and offsets): real 0.594 vs controls mean 0.550, sd 0.028, p95 0.598, max 0.629;
  z +1.58; 2 of 20 controls at or above the real score -- **not above the control's p95; a non-pass**.
So no 2039 legend token gets an S grade from the crib and no vote file was written. Read with the entry lengths (2039's
b 26, i 13, l 7 against 2038's b 17, i 18, l 24), 2039's 1781 legend is not 2038's 1778 list entry for entry; the
2038 crib stays useful only as a vocabulary (Magatijn, Sluijs, Smeederij, Casserne, Neegers, Timmerloos ...) for a
word-level search once more signs are keyed, not as a label-aligned crib. Not a design negative: 68% of the signs are
unkeyed, so the statistic rests on 121 M-graded positions of 374.

One hypothesis, logged, not a reading: the four-sign unit `5 [hash] [pi] o` recurs in entries b, e and q (both passes,
three occurrences); under the key it is v-o-?-r, which fits Dutch "voor" if `[pi]` is a second o -- untested, no
control, M at best; for HYPOTHESES.md when the Remarque or cartouche is read.

Vision calls: 2 blind subagent passes + 1 own reconciliation montage = 3, the brief's cap. Requests: service.archief.nl 1
(the native region), www.googleapis.com 3, archive.org 1, be-api.us.archive.org 1 (the Premise check); all HTTP 200,
1.6 s apart, no challenge page. Box 13:26-13:5x UTC of 55 minutes. Housekeeping: this step adds 0.63 MB committed to
`images/` (42 MB tracked; the AX2-SHRINK-shape job in the gaps list stands); the 30 crops and the debug overlay are
regenerable and not committed.

Suggested follow-ups (one line each, not run): (1) fetch the right-hand strip native 2800,980,1300,2800 once and run the
same two passes on it for entries d, h, p and the cut line ends, ~$4; (2) port `align_2039_legend.py` into
`tools/interlinear_align.py` as a `--glyph-tokens` scoring mode (Usage 8) before a third target writes its own.

`python3 tools/gaps_check.py na-suriname-map-1781` (2 Oct 2026, 13:5x UTC, after the gaps section below was updated): `OK keep-going na-suriname-map-1781: keep going: 6 internal gap(s), 5 step(s) untried / gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped`, exit 0.

## GAPS6-na-suriname-map-1781 (2 Oct 2026, account-4)

Brief: `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; `tools/intake_gate_check.py na-suriname-map-1781` exit 0 at
14:19 UTC (Premise check from GAPS5 in place); the Verdict's cheapest step and only that step: the right-hand strip of
2039's "Verklaringe der Letteren" legend block, for entries d, h, p and the cut line ends. Clock read at start 14:19 UTC.

**Fetch and crops.** One native IIIF region 2800,980,1300,2800 (`images/2039_legend_right_native.jpg`, 1300x2800, 395 KB,
HTTP 200, 1 request to service.archief.nl; 80 px overlap with GAPS5's region, which ends at native x 2880). The strip's
own ink profile finds 27 peaks at pitch 97, most of them the map drawing in its lower two thirds, so the 15 band crops
were cut with `--centres` set to the 30 line centres `tools/iiif_lines.py` found on GAPS5's region (command in
`images/manifest.json`): band Lnn of the strip is band Lnn of the left crops. Crops 1.1 MB, regenerable, not committed.

**Two blind passes and one reconciliation.** Two blind Sonnet subagent passes (`passes/leg2039R_passA.tsv`, 17 rows;
`passes/leg2039R_passB.tsv`, 18 rows; brief `passes/leg2039R_pass_brief.md`: shape codes only, no letter values, no
access to NOTES.md, the key, the left passes or each other; one Read per crop). Both find the same structure: text in
L01 (one line, the end of the title line, ending with a comma at strip x~470), L03 (a two-glyph tail "n ," of the line
between title and legend, not in the file), L04 (two lines: the end of c, then the plain label d. and its clause; the end
of g, then the plain label h. and its clause) and L05 (two lines: the plain label o. at strip x~35 with its clause, the
plain label p. at x~390 with its clause; the end of r); L06-L15 carry no text (map drawing). Every text line ends in
blank paper before the strip's right edge (x 1045-1090 for the d, h, p lines), so nothing of the legend lies further
right. Pass agreement by sequence alignment after code normalisation ([a-plain]=a, [pi-like]=[pi], V=[v-tall],
punctuation dropped): 97 of 119 aligned positions (0.815); per line L01 9/12, L04 line 1 31/36, L04 line 2 28/35,
L05 line 1 23/28, L05 line 2 6/8. This worker's one reconciliation look at a montage of bands L01, L04 and L05 settled
the disagreements (own look named in the note column of every M row): the title line's hooked 4 ([4-bowl], A [q-tail]);
d's "g a d" before the hash (A "a a", B "a o d") and its l (A [lambda-tilde]); h's x (B a dot), b (B 6) and final 6 (A
none); g's x (B a dot); o's 3 (B s); p's opening three-bar box ([hand-box], the sign that opens entry f; both passes
three hashes) and its 7 (A r); r's g (A q) with no k before the 6 (A's k). The one structural correction: o's clause is
complete on its own line ("g r 7 o m [lambda] 3 [psi]" then a comma, then the p. label), so the 13 signs GAPS5 filed as
entry o (the start of the next line, "k q y a d [delta] r [lambda] 7 o t r h") are p's continuation -- the reading both
left passes gave (A: "belongs to entry p"; B labelled the line p) -- and are now p pos 19-31, grades unchanged, each row
noting the move. Recurring unit: "x y d [delta] g [lambda] 6" in both d and h (under the key "? s ? a ? t s").

**Result in numbers.** 108 signs added (H 90, M 18): head +9, c +8, d 25, g +9, h 24, o 8, p 19 (+13 moved), r +6.
`ciphertext_2039_legend.tsv` now 482 signs in 19 lines (head 38, a 13, b 28, c 48, d 25, e 36, f 30, g 17, h 24, i 13,
k 12, l 7, m 13, n 8, o 8, p 32, q 25, r 30, s 75), conf H 367, M 115. New codes: [4-bowl], [dash] (a long dash on the
line in d, kept as a mark like "="). Decode (rule 4, rule 7): `tools/decode_key.py ciphers/na-suriname-map-1781` ->
`ciphertext_2039_legend.tsv: tokens 482: M 167, U 315`; `--check` exit 0 (14:27 UTC). Grades H 0, C 0, S 0, M 167, I 0,
U 315 (65% of the signs outside the 17-sign key, 68% before).

**Alignment against both cribs, rule 3** (`align_2039_legend.py`, now with `--crib`, `--verbose`, `--shuffle-target`;
same statistic as GAPS5; shuffled-crib control = letters shuffled within each crib entry; shuffled-target control =
the decoded letters of each 2039 entry shuffled among that entry's positions; 20 seeds as in GAPS5, then 200):
- `crib_2038_legend.tsv` (1778 Nieuw Amsterdam, 25 lowercase entries): same-label real 0.279 vs shuffled-crib mean 0.285
  sd 0.018 p95 0.315 (z -0.29, 12/20 at or above; 200 seeds: mean 0.282, p95 0.315, 109/200), vs shuffled-target 200
  seeds mean 0.274 p95 0.314 (72/200) -- **no signal**. Free real 0.549 vs shuffled-crib mean 0.497 sd 0.027 p95 0.539
  max 0.570 (z +1.96, 1/20 at or above; 200 seeds: mean 0.491 sd 0.024 p95 0.527 max 0.570, z +2.45, 3/200), vs
  shuffled-target 200 seeds mean 0.483 sd 0.023 p95 0.520 max 0.540 (z +2.90, 0/200) -- **above both controls' p95**.
- `crib_2042_legend.tsv` (Purmerent, 11 entries a-l): same-label real 0.272 vs shuffled-crib mean 0.296 p95 0.331
  (z -1.11, 17/20; 200 seeds 171/200), vs shuffled-target 172/200 -- **no signal**. Free real 0.471 vs shuffled-crib mean
  0.447 p95 0.490 (z +1.02, 2/20; 200 seeds: mean 0.449 p95 0.490 max 0.526, z +0.87, 35/200), vs shuffled-target
  200 seeds mean 0.427 p95 0.471 (z +1.72, 9/200) -- **not above the shuffled-crib p95; a non-pass**.
What the 2038 free pass is and is not. `--verbose` lists each entry's best crib match: the free maximum is carried by
the entries with two to four keyed positions (k 2/2 on "s..r" inside huijsenderbanditenneegers, l 2/2, n 3/3, a 3/4,
g 3/4, i 3/4), each matching somewhere in a 15-44-letter crib string at some offset; the long entries score 0.21-0.31
(c 0.231, e 0.231, s 0.211, r 0.273, b 0.308), and no entry's best alignment reads two words at its keyed positions.
Same-label is null on both cribs and both axes. So **no entry aligns and no sign gets an S grade** (rule 4: S needs two
words); 2039's 1781 list is still not 2038's 1778 list entry for entry, nor 2042's. What the free statistic does reward
is the ORDER of the transferred key's letters (e, s, r, t, n, a, o, d, v, p, l, w, g) inside the 2039 entries against
real Dutch legend text -- it survives shuffling the crib's letters (3/200) and shuffling the target's keyed letters
(0/200) only for the 2038 crib, whose vocabulary is the same fort's. Logged as a hypothesis, not a reading: the 17-sign
key transfers to 2039 (its letters fall in Dutch-like order there). The test that would settle it is gap 1's key
extension (more keyed positions per entry), not another crib.

Not run: no judge (no reading; tools/judge_plaintext.py has no 1781 Dutch corpus, gap "retry"). Vision calls: 2 blind
subagent passes + 1 own montage = 3, the brief's cap. Requests: service.archief.nl 1 (HTTP 200); no other host. Box
14:19-14:3x UTC of 50 minutes. Housekeeping: +0.39 MB committed to `images/` (42 MB tracked; the shrink job in the gaps
list stands). `tools/file_shrink_guard.py` was given the text files only (it crashes with UnicodeDecodeError on a .jpg
path, flagged by GAPS5).

Suggested follow-ups (one line each, not run): (1) port `align_2039_legend.py` (free/same-label statistic, both shuffle
controls, `--verbose`) into `tools/interlinear_align.py` as a glyph-token scoring mode (Usage 8) before a third target
writes its own; (2) a word-level search of the 2038 vocabulary against the 2039 entries once gap 1 raises the keyed
fraction above half.

## GAPS7-na-suriname-map-1781 (2 Oct 2026, account-4)

The Verdict's cheapest step: the images/ shrink in the AX2-SHRINK shape (CLAUDE.md Access playbook; precedent
lodewijk-van-nassau-1573-74, 26 Sept 2026). No vision call, no transcription, no key or reading change
(`tools/decode_key.py ciphers/na-suriname-map-1781 --check`: "reading up to date", exit 0, after the shrink).

| | before | after |
|---|---|---|
| `du -sh images/` | 42M | 15M |
| files under images/ (tracked) | 116 | 53 |

- `images_manifest_full.tsv` (folder root): one row per file images/ has carried (116 + the new JPEG), with bytes, sha1,
  kind (regen-iiif 10, regen-default 2, regen-pil 3, regen-lines 14, kept-no-recipe 20, strip-kept 1, strip-deleted 63)
  and `cited_by` (every text file in the repository that names the basename, found by `git grep -F`).
- `regen_images.sh` (folder root): re-derives every file whose recipe a worker recorded -- the IIIF regions and 2800-px
  overviews of 2038/2039/2040/2042/2045A/2007A from service.archief.nl (bases read from images/manifest.json), the
  5000-px default images of 2007B and 2077, the three local PIL derivations (2007b_overview, 2077_legend_5000,
  2039_cartouche_word2_native), and the crops_2038/ and crops_2042/ line sets through tools/iiif_lines.py.
- Byte-identical regen test before any deletion (2 requests to service.archief.nl, 1.5 s apart, both HTTP 200):

  | file | committed sha1 | regenerated sha1 |
  |---|---|---|
  | 2042_legend_native.jpg | 8b462eb2a66c9cc9b13e47bf209716c632414045 | 8b462eb2a66c9cc9b13e47bf209716c632414045 |
  | 2038_overview.jpg | 322cf7d5a0ee5fd25e52f226188a6702a4713348 | 322cf7d5a0ee5fd25e52f226188a6702a4713348 |

- Deleted: the 63 uncited `images/strips/*.png` (30.1 MB), local 2x-upscaled crops of the 2007A legend blocks whose
  boxes were never recorded, so no recipe can re-cut them; each is restorable from git with
  `git show fc921145:ciphers/na-suriname-map-1781/images/strips/<name>.png` (the commit that added them).
- Converted: the one cited strip, `images/strips/clauseB_full.png` (cited by NOTES.md's RD03D "zwaare" re-read and
  glyphs.md), to `clauseB_full.jpg` (JPEG q92, the same 3000x270); both citations now name the JPEG and the PNG commit.
- Kept as they were: every other cited file, including the 20 VX-CS04/RD03 crops and overviews of 25 Sept 2026 whose
  recipes were not recorded (already JPEG; 1 to 1.3 MB each at most), so every file a NOTES line cites still opens.
- images/manifest.json carries a `shrink_2026_10_02` note pointing at both new files.

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
Read so far: unmeasured on the target sheets. No 2039, 2046 or 2077 tokens have been transcribed to this folder's two-pass bar, so there is no target ciphertext.tsv and no reading (RD03D "State at close"). The key-source control (self-consistency only) is 37 of 56 tokens at grade C (66.1%), with M 1 and U 18 (reading.txt header; tools/decode_key.py --check exits 0, rerun on a scratch copy 1 Oct 2026). RD03D's "C 56, M 1, U 18" is a slip for the 56-token total. The key has 17 grade-C signs (key.tsv), period and ours.
- 2007A key-source remainder: Nota clauses B/D/E/F (about two-thirds of the block), the Remarque paragraph after "Signatuure", and the other enciphered map labels on 2007A whose plain twins are on 2007B - blocker: not-attempted; the plain text is in hand (scratch_2007b_nota_plain.txt; images/2007b_remarques_crop.jpg is on disk but not transcribed). Only pass A of Nota B/D/E/F survives as a file (scratch_notaBDEF_passA.tsv); pass B exists only in the RD03C transcript. Each attempt so far gained signs (13, then 15, then 17), so rule 3's third-attempt clause does not apply. The з/Signatuure conflict belongs here too: single-reader zoom re-reads of that one word on crops already at native resolution failed twice (RD03C, RD03D), so settle з from its other occurrences in the aligned Remarque, not from a third read of the same word; next: transcribe 2007B's plain Remarque, run a fresh blind pass B over the Nota B/D/E/F crops, add a glyph-token option to tools/interlinear_align.py (it is numeral-only today; Usage 8, no private copy), and align against 2007B's plain text seeded with the 17 signs, ~$9
- 2077 (fortress Zelandia): the 3-line title cartouche after "PLAN"; the right-hand "Explicatie der Signatuuren" list (about 25 entries a-z, plain and cipher mixed); the second cipher "Explicatie" list and profile lines inside the left inset panel; the enciphered words inside the plain top-left Nota; the cipher river and land labels - blocker: not-attempted; RD03D sampled only the cartouche and 2 legend entries (9/27 high-confidence). The classifier undercounted this sheet: images/2077_overview.jpg shows two cipher legends, not one list of about 18. An untried crib is on disk: 4.VEL 2078 (images/2078_overview.jpg) is Wollant's plain plan of the same fort with a plain lettered Nota legend (a. oude Inspectie, b. Artillerie Caserne en Monteerings Kamer, l. Corps de Garde, u. Beetehuys, w. Woning van den Opsigter der Directie Slaaven, ...), and those building names recur among 2077's own plain entries (Menagerie, Ambagts Slaaven van de Monteerings-Kamer, Beetehuijs, Opziger). 2076 (plain outworks plan, legend A-S) is a second candidate crib; next: cut native IIIF crops of both 2077 legends and the cartouche with tools/iiif_lines.py (the image on disk is capped at 5000 px against a native 10711), plus a crop of 2078's Nota; run 2 blind passes + 1 reconciliation per 2077 block; align each cipher entry against its building name from 2078/2076 and 2077's own plain entries, ~$10
- 4.VEL 2061 (Redout Leyden): the No.1-6 battery list and the a-g legend below the glossed title and battery-header block - blocker: not-attempted; the gloss was checked on the header only (VX-CS04, RD03B). RD03B saw plain "M" and numerals mixed with cipher abbreviation-words (images/2061_title_topleft.jpg) and left them unread. The text after Atlas of Mutual Heritage page 2218's "The legend in cipher on Wollant's map is as follows: (...)" is elided in this file and was never captured; next: re-read AMH page 2218 in full and capture any plain legend text, then cut native line crops of the battery list and a-g legend with tools/iiif_lines.py and check how far the gloss covers them, ~$4
- 4.VEL 2039 (fortress Nieuw Amsterdam): the 3-line title cartouche (the van-vs-PAN position on line 2 is settled: "van", 2 Oct 2026, GAPS-na-suriname-map-1781, two independent high-zoom reads agree with RD03C against RD03D's single pass, see the section above), the a-u "Verklaringe der Letteren" legend, the clause after each Bastion/Redan label, and the lower-left Remarque - blocker: not-attempted; there is one uncorroborated pass on the title (46/72 glyphs matched, RD03D) and no ciphertext.tsv. The sheet is copy-free at 11267x8656, and Arabic numerals are plain (RD03C). Plain-counterpart search of the 4.VEL 2030A5-2090C block done 2 Oct 2026 (GAPS2-na-suriname-map-1781, see the section above and `vel_2030-2090_catalogue.tsv`): 4.VEL 2038, "Plan van 't fortresse Nieuw Amsterdam" (J.C. Hurter, 31 July 1778, "Zeer uitvoerig"), is plain Dutch throughout with a capital A-K legend (the five bastions by province, sluices, creek) plus a lowercase a-z building list and batteries I-VIII, at 2039's exact size and scale (0.44 x 0.425 El; 100 Rijnlandse roeden = 370 strepen) -- `images/2038_overview.jpg`; 4.VEL 2040 (Wollant, 1784) is plain but carries only artillery labels ("6 Can. a 24 lb Calib", "4 Mortieren ...") and a Nota -- `images/2040_overview.jpg`. 2038's legend block is transcribed (2 Oct 2026, GAPS3-na-suriname-map-1781, see the section above): `crib_2038_legend.tsv`, 35 legend entries (capitals A-G, I, K; lowercase a-z without j; the No. I-VIII battery line) plus title and signature lines, 40 text rows, H 24 / M 16, from two blind passes (28/40 lines identical, 152/169 words) and one reconciliation on the native crops `images/crops_2038/`; 2040's artillery labels are not transcribed (secondary); the a-u legend block was transcribed 2 Oct 2026 (GAPS5-na-suriname-map-1781, see the section above): one native IIIF region (`images/2039_legend_native.jpg`), 30 iiif_lines crops, two blind passes (277/370 positions, 0.749) and one reconciliation, `ciphertext_2039_legend.tsv` 374 signs in 15 entries (a, b, c, e, f, g, i, k, l, m, n, o, q, r, s; d, h, p and four line ends lie past the region's right edge), decode `M 121, U 253` (--check exit 0), alignment against crib_2038_legend.tsv a control-backed non-pass (same-label z -0.68, free z +1.58, 2/20 controls at or above) -- 2039's 1781 list is not 2038's 1778 list entry for entry, and 68% of the legend's signs are outside the 17-sign key; the right-hand strip was fetched and read 2 Oct 2026 (GAPS6-na-suriname-map-1781, see the section above): d, h, o, p complete and the ends of head, c, g, r, 108 signs added (H 90, M 18), the file now 482 signs in 19 lines, pass agreement 97/119 (0.815), decode M 167 U 315 (--check exit 0); alignment re-run against crib_2038 AND crib_2042 with shuffled-crib and shuffled-target controls: same-label null on both (12/20, 17/20), free above both controls only for 2038 (3/200, 0/200) and carried by two-to-four-position entries, no entry reads two words, no S grade -- the whole a-u legend block is now transcribed to the two-pass bar and nothing of it lies further right; next: the cartouche and the lower-left Remarque the same way (native crops, 2 blind passes + 1 reconciliation, append to ciphertext_2039_legend.tsv), ~$5; the key itself grows only from gap 1 (2007A Nota/Remarque against 2007B, ~$9), which is the step that unlocks every 2039 reading
- 4.VEL 2046 (redoubt Purmerent): the title cartouche and the enciphered legend and profile text - blocker: not-attempted; there is one uncorroborated title pass (36/56 glyphs matched; best run only "DER", RD03D). No gloss or twin is on file. The block's catalogue (`vel_2030-2090_catalogue.tsv`, 2 Oct 2026) lists nine Purmerent plans beside it -- 2041A/B, 2042 (Calvi, "Met aanwijzingen"), 2043 (profile), 2044A/B and 2045A/B ("Met aanwijzingen"), 2047 (1781 Schetsplan), 2048 (Wollant, nummer C) -- all digitised; 2042 and 2045A eye-checked 2 Oct 2026 (GAPS3-na-suriname-map-1781, one 2800-px IIIF overview each, `images/2042_overview.jpg`, `images/2045A_overview.jpg`): both carry a plain Dutch lettered legend -- 2042 (Calvi, undated) a lowercase a-l building list in a framed box (batteries a-c with gun counts, d Plaats voor de Afdakken, e Officiers Huis, f Keuke en Magas., g Quartier voor 75 Mann, h Keuke en Water magas., i Wagt & Proviant magasyn, k Provost, l Buite wagt), the shape 2046's legend most likely enciphers; 2045A (Dircks, undated) a capital A-H works list (Redout, Bastions, Gragt, Bedeckte Weg en Glassie, Profiel EF, Wagt Huys, Sluys) -- 2042's a-l legend is transcribed (2 Oct 2026, GAPS4-na-suriname-map-1781, see the section above): `crib_2042_legend.tsv`, 11 entries a-l without j in 13 rows (2 continuations), H 10 / M 3, from two blind passes (12/13 rows identical, 51/52 words) and one reconciliation on the native crop `images/crops_2042/leg2042_L01.jpg` (open: a's ℔ders, d's Affdakken/Afdakken, k's Provost/Provoost); 2045A's A-H works list is not transcribed (secondary); next: after the key is extended on 2039, the same protocol as 2039 on 2046 (iiif_lines crops of its legend and cartouche, 2 blind passes + 1 reconciliation, ciphertext.tsv rows, align the enciphered entries against crib_2042_legend.tsv and decode with decode_key.py), ~$9

Closed 2 Oct 2026 (GAPS7-na-suriname-map-1781, account-4): the housekeeping item (images/ 42 MB tracked against the 30 MB line, 28 MB of it images/strips/) -- images/ is now 15 MB; images_manifest_full.tsv (sha1, recipe kind, cited_by) and regen_images.sh (IIIF byte-identical on a 2-file sample) are in the folder; see the GAPS7 section above.

## Escalation (1 Oct 2026)
- [x] siblings: VX-CS04 read the catalogue scopecontent of all 95 items in 4.VEL 2030A5-2090C and eye-checked the images. It found 2046 and 2061 (catalogued "cyferschrift") and 2077 (no cipher word in the catalogue) and ruled out 2076 and 2078 as plain. DECODE's cached dumps hold only NA 1.05.03 inv 219 (1689, a different cipher), and neither solver repo has this target. Not opened: the invnrs next to 2007A/B outside that block, and the other ~9000 4.VEL items. 2077 shows that a cipher sheet with no cipher word in its catalogue record can be found only by eye.
- [ ] clear-pages: 2007B (the plain twin) and the on-sheet glosses of 2007A and 2061 were used for all 17 signs, and 2007B's Nota was transcribed (scratch_2007b_nota_plain.txt). Not yet used: 2007B's Remarque; 2061's text below the header; 2078's plain Nota legend for the same fort, by the same maker and survey, as a building-name crib for 2077's cipher legends (2076's A-S legend is a second candidate); and a search of the 95-item block for plain counterparts of 2039, 2046 and 2061 (2 Oct 2026, GAPS2: the block's catalogue is now on disk as `vel_2030-2090_catalogue.tsv`; 2038 is 2039's plain counterpart, eye-confirmed and, 2 Oct 2026 GAPS3, transcribed to `crib_2038_legend.tsv`; the Purmerent candidates 2042 and 2045A are eye-checked, both plain lettered legends, and 2042's a-l list is transcribed to `crib_2042_legend.tsv` (2 Oct 2026, GAPS4), 2045A's A-H works list is not; the Leyden candidates are not yet eye-checked). Planned as gaps 1-5.
- [ ] known-keys: KEY-DESIGN.tsv row 127 is this target's own 17-sign key only. KEY-OFFICES.tsv has no Suriname, WIC or Wollant row, and no design_prior.py run is recorded in this folder. Wollant's papers and Governor Texier's 1781 correspondence (Sociëteit van Suriname, NA 1.05.03) have not been searched for a key sheet. Planned: an NA catalogue search of 1.05.03 for 1781 "cijfer"/"sleutel" items, a design_prior.py run, and a KEY-OFFICES grep for WIC/Suriname 1770-1790, ~$4.
- [x] print: VX-CS04 read Atlas of Mutual Heritage pages 2025 (VEL2039) and 2218 (VEL2061) on 25 Sept 2026: the legends are enciphered and "niet getranscribeerd". It also ran 6 web searches and checked the cached DECODE dumps and both solver repos; none has a decipherment. Not opened: den Heijer's Grote Atlas van de WIC II (2012), which AMH cites as its source, and Koeman's Atlantes Neerlandici. AMH page 2218's legend sentence is elided in this file (gap 4 captures it).
- [ ] key-rebuild: the key has been extended only by hand-aligning known plaintext (13, then 15, then 17 signs; RD03, RD03B, RD03C). Each pass gained signs, so this is not retired under rule 3. No DP/EM alignment, annealing or LM-context instrument has been tried. Planned: tools/interlinear_align.py with a glyph-token option, aligning 2007A's Nota and Remarque against 2007B, seeded with the 17 signs (gap 1), and then the 2077 legend against 2078's names (gap 2).
- [ ] image-check: done in part. RD03D re-read "zwaare" at 5x and found the λ/ψ clash was a mis-segmentation. The з/Signatuure single-word re-read has failed twice (RD03C, RD03D) on crops already at native resolution, so it is not to be repeated with the same instrument; it moves into gap 1's alignment. The van-vs-PAN check on 2039 cartouche line 2 was run 2 Oct 2026 (GAPS-na-suriname-map-1781): one blind 4x read plus this worker's own 3x read both give `5[delta][h-loop]` = "van", settling it against RD03D's single "PAN" pass. Still never run: a native-crop image check of 2061's battery list and a-g legend (gap 3). Planned: with gap 3, ~$4.
- [ ] retry: there is no target-sheet ciphertext to rerun yet. The key-source decode is current (56 tokens: C 37, M 1, U 18). Before any target reading can be judged, a Dutch judge corpus from the right era is needed: tools/judge_plaintext.py has no "nl" corpus wired (its comment about nl_repo says so); nl20 is 1880-1920 novels and nl_dev is the Statenvertaling, and neither is matched to 1781 engineering prose. Planned: build an nl18 corpus (~$3, the V6-PTCORP precedent), then rerun every target group with the extended key and regrade.
Verdict: keep going: 5 internal gaps (all reading; the housekeeping shrink closed 2 Oct 2026, GAPS7); cheapest next: gap 3's 4.VEL 2061 (AMH page 2218 re-read in full, then native iiif_lines crops of the battery list and a-g legend checked against the gloss), ~$4; then gap 1's key extension (2007A Nota B/D/E/F and Remarque against 2007B with a glyph-token option in tools/interlinear_align.py, the step every 2039 reading waits on and the test of the GAPS6 hypothesis that the 17-sign key transfers to 2039), ~$9

## Web and blog check (GAPS-na-suriname-map-1781, 2 Oct 2026)

Run first because `tools/intake_gate_check.py na-suriname-map-1781` exited 1 only for the missing CHECK-SOLVED-WEB step
(28 Sept 2026 rule). Web search tool (US index), one query at a time; the three blogs by name; every plausible hit opened
and its comment thread read. Hosts: web search 11 queries; scienceblogs.de 1 page; atlasofmutualheritage.nl 1 page;
dbnl.org 1 page. `sources/cryptiana/` on-disk snapshot grepped for suriname / wollant / 4.VEL / zeelandia: 0 hits, 0 requests.

Plain web searches (a):
1. `Wollant 1781 Suriname kaart cijferschrift Nieuw Amsterdam` -- Delpher "Suriname in kaart gebracht", Rijksmuseum and NYPL
   Suriname maps, Wikipedia Fort Nieuw-Amsterdam, NA 4.CAF finding aid, DBNL Wekker (OSO 7, 1988) "Suriname in
   kaartencollecties". None names Wollant's cipher sheets. The Wekker article was opened: no mention of Wollant, 1781
   fortification plans, cijferschrift or the 4.VEL numbers.
2. `"4.VEL" 2039 OR 2046 OR 2061 OR 2007A cijferschrift Suriname Nationaal Archief` -- only general Nationaal Archief
   (Suriname and NL) pages; no hit about these items.
3. `"Generaal Plan van Defensie" Suriname 1781 cipher OR cijferschrift OR cypher` (the folder's most distinctive clear
   phrase, 2007B's title) -- 20th-century Surinamese military history, NA finding aids 1.01.01.01 / 2.13.63 / 2.10.18; no
   hit about this sheet.
4. `Suriname fortification maps 1781 cipher legend Wollant deciphered OR decipherment OR ontcijferd` (the folder's own
   descriptive title) -- Atlas of Mutual Heritage page 2123 "Plan of Fort Zeelandia" (opened: "Most or in some cases even
   all of the annotation on these plans is in cipher"; the legend is "partly encrypted, not transcribed", twice; no
   plaintext of any legend entry; source cited den Heijer 2012), AMH page 10141 "Map of the second Cordon of Defence"
   (a different, plain item), and the 1689 Suriname ciphertext paper (dspace.ut.ee / ResearchGate, "Send someone to
   finish Fredenburgh's works") -- that is NA 1.05.03 inv 219, 1689, the different item already logged above; not these
   sheets.
Blog searches (b), each run twice (once with a site: prefix, which the tool applied as a literal term, then with a
domain filter):
5. Cipherbrain (scienceblogs.de/klausis-krypto-kolumne), `Suriname Karte Chiffre 1781 Wollant Zeelandia Festung` -- no
   post about this item; the one post surfaced, "Fünf kryptologische Cold Cases" (3 Apr 2021), was opened with its
   comment thread: cigarette-case, Fair Game, Guy de Contet pigpen, Callimahos steganogram, Furlong postcard; no mention
   of Suriname, Wollant, Zeelandia, Nieuw Amsterdam, Paramaribo or a map legend cipher.
6. Cryptiana (cryptiana.blogspot.com, cryptiana.web.fc2.com), `Suriname map cipher Dutch 1781 Wollant Nieuw Amsterdam
   fortification` -- no results on either domain; the on-disk snapshot grep above is also empty.
7. Cipher Mysteries (ciphermysteries.com), `Suriname Dutch map cipher 1781 Wollant fortification legend` -- La Buse,
   d'Agapeyeff, Bellaso, Tamarin Bay and Voynich posts only; none about a Dutch map of 1781, so no thread opened.
Model-solve announcements (c): `Suriname 1781 map cipher "solves" OR "solved" Claude OR GPT OR ChatGPT cijferschrift
   kaart` -- Kryptos K4, Cyphral Distich and generic AI-cipher pages; nothing about this item.

Result: no decipherment or plaintext of this item located by these queries on 2 Oct 2026 (a search result, rule 10,
never a novelty verdict). Status word unchanged (`partial`).

## Premise check (GAPS5-na-suriname-map-1781, 2 Oct 2026)

Run first, 13:2x-13:4x UTC 2 Oct 2026, because `tools/intake_gate_check.py na-suriname-map-1781` exited 1 only for the
missing Premise check section (the 12:47 UTC rule). Stance: try to prove 4.VEL 2039's legend is already read. Each of
(a)-(d) as `.claude/briefs/check-solved.md` defines them; "opened" means the file or page was read in this session or
is on disk from a named earlier session.

(a) **The folder's own mentions of a decipherment, gloss, clear copy or translation -- not found for 2039.** Every such
mention in NOTES.md was listed by grep (vertaal / gloss / ontcijfer / sleutel / deciph / transcri / facsimil) and traced:
2007B "cijferschrift vertaald" is 2007A's plain twin (on disk, `images/2007b_*.jpg`, used for the key; it is not a twin
of 2039); 2007A's and 2061's interlinear glosses are on those two sheets (on disk, key source); Atlas of Mutual
Heritage page 2025 (VEL2039), read 25 Sept 2026 by VX-CS04, says the a-u legend and the lower-left note are "in
geheimschrift, niet getranscribeerd"; VX-CS04's native-resolution eye-check of 2039's cartouche, bastion list and
Remarque found no gloss and no key on the sheet. The one mention not opened is den Heijer, *Grote Atlas van de
West-Indische Compagnie* II (2012) p. 342, which facsimiles 2039 (finding aid, `vel_2030-2090_catalogue.tsv` row
2039): Google Books API (1 query, `"Grote Atlas van de West-Indische Compagnie" Wollant`) 0 volumes; Internet Archive
advancedsearch (1 query) 1 unrelated item (an Aruba plan) -- **unreachable from the cloud**; the only evidence about
its text is indirect (AMH credits den Heijer as its source and itself says not transcribed). This job's own native
legend region (`images/2039_legend_native.jpg`, fetched below) was located by ink profile, not looked at, before the
blind passes; the reconciliation look below is the first eye on it.
(b) **Other solvers' working files -- not found.** On-disk snapshots grepped for suriname / wollant / 4.VEL / zeelandia
/ nieuw amsterdam / purmerent / paramaribo: `sources/cyphersolver/2026-10-01` and `2026-10-02` (Bourdeau's current
tree: CLAUDE.md, mercy1648, matignon1586, catokwacopa only), `sources/bourdeau/`, `sources/solver-diffs/` including
`2026-10-02-aymeloglu.tsv` (his TARGETS rows: no Suriname or VEL item), `sources/decode/records-decrypted-2026-09-24.tsv`
(the only Suriname record is DECODE 7841, NA 1.05.03 inv 219, 1689 -- a different cipher, already logged above). No
apply-key script, rendering or output by another solver exists for this item; no borrowed key has been run on it (the
17-sign key.tsv is this repository's own, built from 2007A/2061).
(c) **Physical neighbours -- no clear copy or decipherment beside it.** 4.VEL is a map series, so the neighbours are the
adjoining inventory numbers, all in `vel_2030-2090_catalogue.tsv` (the EAD read offline, GAPS2): 2036 (regenbak,
1743), 2037 (Chambrier, 1744, French), 2038 (Hurter, 31 July 1778, plain Dutch throughout -- the crib already on
disk, `crib_2038_legend.tsv`), 2040 (Wollant, 1784, plain artillery labels and a Nota, `images/2040_overview.jpg`),
2041A/B (Purmerent). 2039's own METS record carries one file (catalogue column `files` = 1): there is no "Blad 2"
translation sheet of the 2007A/2007B kind. Grep of the whole 95-item block for vertaal / sleutel: 0 rows; "met
verklaring" appears only on 2061 (its own gloss, already used), 2067A-B (Tourton 1710, plain French) and 2077
("gedeeltelijke verklaring"). The 2007B pattern ("kopie, cijferschrift vertaald") occurs once in the series as far as
the on-disk catalogue goes (2007A/B sit outside this block; the rest of 4.VEL's ~9000 items were not read).
(d) **Recipient-side editions -- not found.** The sheets went to the directors of the Sociëteit van Suriname in
Amsterdam (NA 1.05.03). Google Books API, `country=US`, 2 further queries this session: `"Verklaringe der Letteren"
"Nieuw Amsterdam"` (345 volumes, none about these sheets in the top 5: 1887 De Librye, 1861 book lists, 1895
Wetenschap letteren en kunst, 1730 theology) and `Wollant 1781 Suriname cijferschrift "Nieuw Amsterdam" plan` (2
volumes, both Leupe's 1867 *Inventaris der verzameling kaarten berustende in het Rijks-Archief*, whose row reads
"... 1781 ... Met profil. Gedeeltelijk in cijferschrift" -- the catalogue entry, no text). Internet Archive full-text
(be-api, 1 query, Wollant AND "Nieuw Amsterdam" AND cijferschrift/geheimschrift): 0 hits. Earlier passes already
covered AMH (25 Sept), 6 + 11 web searches and the three blogs (above); no Dutch documentary edition (RGP, Sociëteit
van Suriname papers) printing Wollant's legend text was located by any of them.

Verdict: CLEAR TO TEST -- no decipherment, gloss, clear copy or print of 2039's legend found by (a)-(d); den Heijer
2012 p. 342 is the one named source not opened (unreachable from the cloud; a desk/LOCAL-QUEUE read of that page is
the cheap way to close it, not this job's). Status word unchanged (`partial`); rule 10 wording: a search result.
Requests this check: www.googleapis.com 3, archive.org 1, be-api.us.archive.org 1, all HTTP 200, 1.6 s apart.
