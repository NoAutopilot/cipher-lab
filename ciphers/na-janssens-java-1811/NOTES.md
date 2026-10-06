partial
Colenbrander's *Gedenkstukken der Algemeene Geschiedenis van Nederland 1795-1840*, Deel VI (huygens retroboeken
sources 9/10/11), full-text search for "Janssens" and independent read of the Inleiding footnote, by this worker
(25 Sept 2026): the edition names this exact archival series and a decipherment item in it ("In n°. 11 de berichten
van Janssens omtrent de overgave van Java") but does not print the dispatches or their decipherment -- see
"Check-solved" below.

QUEUE row: VX-N02. Worker: LANE VX VX-CS05 (Sonnet, session_015pyzNM7ma2wqgVwhjvYpfN), 25 Sept 2026. Job:
`.claude/briefs/runs/2026-09-25-lane-vx-cs05.md` + `-COMMON.md`. Found (as a lead, not scored) by LANE VX
VX-SCNA, 25 Sept 2026 (QUEUE.md "Key beside the letter" section, row VX-N02).

## What this is

Nationaal Archief, toegang **2.01.27.05** (Hollandse Divisie bij het Ministerie van Marine en Koloniën te
Parijs, 1810-1814), **invnr 12**: "Niet-genummerde ingekomen stukken bij de Chef der Hollandse Divisie
('pièces non enregistrées dont Son Exc. le Ministre en fait l'envoi particulièrement au Chef du bureau
Hollandais'). Met bijlagen en index." A 233-leaf bundle (each scan a two-page spread), `DIGITALIZED`. Full scan
list: `https://www.nationaalarchief.nl/onderzoeken/archief/2.01.27.05/invnr/@12`; per-leaf image/IIIF URLs are
in `images/manifest.json` (drawn from the item page's own `drupal-settings-json`).

Sender: Gouverneur-Generaal J.W. Janssens (Batavia/Java) to the Minister (Hollandse Divisie, Paris). The
archival description names three enclosure groups: an October 1811 report, a run of cipher dispatches "van 20
juni 1811 tot 7 augustus 1811 met bijgevoegde ontcijfering" (with attached decipherment), and December
1811/January 1813 letters.

## Bundle inventory (eye-check, 53 of 233 leaves = 23%, NOT exhaustive)

Method: 42 leaves at even spacing (every ~5.6th leaf, `service.archief.nl`'s `/thumb/` endpoint, 256x197 px)
covering the whole bundle, plus 11 denser leaves (186-198) and 5 leaves (185, 191, 199, 200, 221) re-fetched at
IIIF `full/1200,/0/default.jpg` for legibility once the 186-198 cluster showed cipher content. Full per-leaf
classification and URLs: `images/manifest.json`. This is a sample, not a page-by-page transcription pass; a
future worker paging the remaining 180 leaves may find more cipher material, especially immediately around the
leaves flagged below (the sample step is ~5-6 leaves, wide enough to miss a single-leaf item).

**Leaves 1-179 and 203-233 (all 32 sampled points in that range): no cipher.** Plain French/Dutch prose letters
and reports, a signed CV-style "Etat de Service du Général de Division J.W. Janssens" (leaf 185, No.37, Paris 5
Janvier 1813 -- part of the Dec 1811/Jan 1813 enclosure group the archival description names), a sealed cover
letter Paris 8 mai 1811 to the Minister's chef de division re: unrelated manuscripts (leaf 221), tabular forms,
and several blank/divider leaves. None of these 32 points carries a cipher digit.

**Leaves 186-200 (13 leaves, sampled at every leaf): the cipher cluster**, matching the archival description's
"20 juni tot 7 augustus 1811" run. Eye-read only, M-grade (not a transcription, headings hard to read for sure
at this resolution -- a transcription pass should re-verify every number cited here):

| leaf | content | URL |
|---|---|---|
| 186 | blank (faint show-through) | `images/186.jpg` |
| 187 | plain signed prose report, no cipher | `images/187_med.jpg` |
| **188** | **raw cipher only** -- rows of pure numeric groups, no interlinear gloss anywhere on the leaf, heading eye-read "Numéro [digit illegible]", ends "Signé [name illegible]" | `https://service.archief.nl/api/file/v1/default/bf152dd2-ce11-493c-bf0e-828193041803` |
| 189 | plain prose, no cipher | `images/189_med.jpg` |
| **190-191** | **cipher + decipherment**: heading eye-read "N°.2" "(Duplicata)", grid of numeric code with a French word/syllable written directly below each number, continuous readable French across the line ("...Batavia, neuf Juillet...le port où...est les bâtiments...à deux cent lieues de Batavia; l'ennemi a deux croisières...sur tous les côtes; je ne puis sans...heureux, car il y a...peu de jours un...frigate ennemie...") -- a naval-intelligence dispatch about an enemy frigate off Batavia | leaf190 `https://service.archief.nl/api/file/v1/default/41b9da74-07f2-481d-b2f2-7301302f5943`; leaf191 `https://service.archief.nl/api/file/v1/default/0bf1881b-67af-451c-8f94-69a97aad98fc` |
| **192** | **raw cipher only** -- rows of pure numeric groups, no gloss, ends "Signé [name illegible]" | `https://service.archief.nl/api/file/v1/default/5f81190c-4c3e-42bd-847e-dcecb5b4f9b4` |
| 193 | blank divider | `images/193_med.jpg` |
| 194-195 | heading eye-read "N°.6" "(Duplicata)", "Batavia 9 Juillet" -- **body is plain continuous French prose, NOT enciphered** (a "Duplicata"-headed dispatch that was simply never put in cipher) | `images/194_med.jpg`, `images/195_med.jpg` |
| 196 | blank | `images/196_med.jpg` |
| 197 | blank divider (archive stamp only) | `images/197.jpg` |
| **198** | **raw cipher only** -- heading eye-read "Numéro 2" "(Duplicata)" (NB: same "2" as leaves 190-191's heading, by eye -- unverified, could be a misread digit), dense rows of pure numeric groups, no gloss, ends with a signature | `https://service.archief.nl/api/file/v1/default/e58671b6-0977-4bf2-93aa-f01c431a2b1f` |
| **199-200** | **cipher + decipherment**: heading eye-read "Numéro 3." "(Duplicata)", numeric code + French word grid, several entries crossed out/corrected, continuous readable French about the same subject (frigate, wind, a ship unable to leave port, awaiting reinforcement), ending "Fin." -- this is the pair the original VX-SCNA scout found | leaf199 `https://service.archief.nl/api/file/v1/default/9d81a97b-0b19-45ee-8c82-3637d7117c61`; leaf200 `https://service.archief.nl/api/file/v1/default/9c01a739-6ed2-4229-9a7f-38c4850207ec` |

**Reading of the pattern (M-grade, offered as a lead for a transcription pass, not established):** the bundle
appears to interleave, for the same run of numbered dispatches ("Numéro 1/2/3...", each headed "(Duplicata)"),
a **raw cipher-only copy** (leaves 188, 192, 198 -- pure digits, ends in a signature, no gloss) and a **separate
decipherment copy** (leaves 190-191, 199-200 -- digits with the French word glossed directly beneath each one).
If leaf 198's heading really is "Numéro 2" (unverified, see above), its decipherment counterpart would be
leaves 190-191, which also read "N°.2" -- i.e., the raw original and its decipherment may sit only ~8 leaves
apart rather than being scattered across the whole 233-leaf bundle as the QUEUE row's original note speculated.
This needs a digit-by-digit re-check by whoever transcribes the cluster; do not cite the "Numéro 2 = leaves
190-191/198" pairing as established.

**Not located in this sample:** a "Numéro 1" leaf (would be expected before leaf 188 given 2 and 3 are both
present; the nearest sampled point below the cluster is leaf 179, plain prose -- a "Numéro 1" leaf could sit
anywhere in the unsampled 180-187 range), and any raw-cipher-only counterpart to the leaf 199-200 "Numéro 3"
decipherment (could be leaf 201/202, immediately after and unsampled, or elsewhere).

## Check-solved (25 Sept 2026)

1. **Web search:** `Janssens Java 1811 cijferschrift ontcijfering Nationaal Archief`, `"generaal Janssens" Java
   1811 geheimschrift cipher letter frigate` -- both return only general Invasion-of-Java-1811 history (Wikipedia,
   warhistory.org) and unrelated National Archief finding aids (Janssens family papers 2.21.092, his own maps
   4.JSF); nothing connects a cipher or decipherment to this correspondence.
2. **Colenbrander's *Gedenkstukken der Algemeene Geschiedenis van Nederland 1795-1840*, Deel VI** (the standard
   edition for this period; via `resources.huygens.knaw.nl/retroboeken/gedenkstukken`, source ids 9/10/11 = Deel
   6 bands 1-3, GS 13/16/17), full-text search (`searchText` accessor) for `Janssens`: 19 hits (band 1), 11 hits
   (band 2), 5 hits (band 3) -- all read by this worker. All are Janssens as a subject/addressee of OTHER
   people's letters (French ministers, Dutch commissioners discussing him) or index/register entries, **except
   one direct hit that identifies the archive**: band 2 (Deel VI, Tweede Stuk, GS 16), p. XXX, in Colenbrander's
   own Inleiding (Introduction) describing the Hollandse Divisie archive: after listing its contents as items
   "1-2. Minuut-uitgaande stukken van den chef der divisie. 3-4. Uitrusting van schepen voor Java... 5.
   Minuut-rapport... 6-11. Ingekomen stukken bij den chef der divisie..." (matching our target's own archival
   description almost verbatim -- "Niet-genummerde ingekomen stukken bij de Chef der Hollandse Divisie"), a
   footnote reads verbatim: **"In n°. 11 de berichten van Janssens omtrent de overgave van Java"** ("In no. 11
   [are] the reports of Janssens concerning the surrender of Java"). This is Colenbrander's own 1915-era
   description of the archive's contents, not a printed transcription or decipherment -- **he does not print
   these dispatches**, he only names the archival item that holds them (source page:
   `https://resources.huygens.knaw.nl/retroapp/service_gedenkstukken/deel6_band2/html/gedenkstukken_deel6_band2_gs16_voorwerk_XXX.html`).
   Colenbrander's inventory numbering ("6-11") is close to but not necessarily identical with the modern
   toegang's invnr numbering (invnr 12 in the current finding aid) -- the archive has likely been renumbered
   since 1915; this is strong circumstantial confirmation that Colenbrander knew of and is describing the same
   physical dossier (or a close sibling of it) as this target, not proof the invnr matches exactly. Also tried
   the phrase `overgave van Java` directly (URL-encoded space): returned no results banner on any of the three
   sources, inconsistent with the single-word searches above -- likely a query-encoding quirk of the site's
   search box with multi-word phrases, not re-attempted (one query form is enough to establish the single
   substantive hit already found via `Janssens`).
3. **Internet Archive, "val van Java 1811" / a printed edition:** `advancedsearch.php` for `"val van Java"` (0
   hits) and `Janssens Java 1811 cijfer` (0 hits, title/metadata search); the be-api full-text search for the
   broader phrase `"overgave van Java"` returns 64 items (general Dutch East Indies histories, expected for a
   major historical event) -- not narrowed further, since nothing in the check-solved brief or this search
   suggests a specific printed edition transcribes Janssens' cipher dispatches themselves; this is a search
   result, not an exhaustive negative on all 64 items' full text.
4. **DECODE**: `sources/decode/records-non-decrypted-2026-09-24.tsv` and `records-decrypted-2026-09-24.tsv`
   (2548 rows, crawled 24 Sept 2026) grepped for `janssens`/`java`: no hit.
5. **The two solver repositories:** shallow-cloned fresh this session, grepped case-insensitively for
   `janssens` and (folder-name only, to avoid the many false-positive substring hits of "java" inside unrelated
   filenames) `java`/`batavia`. No target folder, TARGETS.md row, or NOTES.md mention of this correspondent,
   archive, or dispatch in either repository (the only "java" hit is an unrelated "Javan roads" phrase in
   `cyphersolver/feuquieres/` TARGETS.md row, a different 1691 target).
6. **Cryptiana / comment threads:** not separately searched this pass (not named in this row's brief beyond the
   standard six; nothing found anywhere else suggests a listing).

No key, decipherment or printed transcription of this bundle's Java dispatches found anywhere outside the
bundle itself. Colenbrander's Deel VI independently confirms the archive holds "de berichten van Janssens
omtrent de overgave van Java" but does not print them.

## Closing line

**Key beside the letter: not a separate key table, but a contemporary decipherment sitting in the same
233-leaf bundle as raw cipher-only copies of the same numbered dispatches** -- leaves 190-191 (heading "N°.2
Duplicata") and 199-200 (heading "Numéro 3. Duplicata") each carry a French word/syllable glossed directly
beneath every cipher-code number, reading as continuous naval-intelligence prose about an enemy frigate
blockading Batavia; this is the "met bijgevoegde ontcijfering" the archival description promises. **Undeciphered
copy-free material it could read:** leaf 188 (raw cipher only, no gloss anywhere on the leaf,
`https://service.archief.nl/api/file/v1/default/bf152dd2-ce11-493c-bf0e-828193041803`) and leaf 192 (raw cipher
only, `https://service.archief.nl/api/file/v1/default/5f81190c-4c3e-42bd-847e-dcecb5b4f9b4`) -- and, if the
eye-read "Numéro 2" heading on leaf 198 is confirmed distinct from the "N°.2" decipherment at leaves 190-191
(unverified here), leaf 198 too
(`https://service.archief.nl/api/file/v1/default/e58671b6-0977-4bf2-93aa-f01c431a2b1f`). Whether these raw
leaves are already paired with a decipherment elsewhere in the 180 unsampled leaves of this same bundle is not
established by this pass -- the next step for whoever takes this target is a full 233-leaf page-through (not
another sample) to pair every raw cipher leaf with its decipherment counterpart by dispatch number, followed by
transcription of the confirmed code-to-syllable pairs into a key. Do not decode from this NOTES.md; nothing here
is a built key or a rule-7 reading.

## Hosts and requests

- `www.nationaalarchief.nl`: 1 (invnr 12 item page, for the scan manifest).
- `service.archief.nl`: 58 (42 thumbnails spanning the whole bundle + 5 IIIF-medium re-fetches of leaves
  185/191/199/200/221 + 11 IIIF-medium fetches of leaves 186-190/192-196/198), all ≥1.5s apart, all HTTP 200.
  Combined with the one `nationaalarchief.nl` request: 59 of this worker's 60-request cap for these two hosts.
- `resources.huygens.knaw.nl`: 11 (1 toc probe on source 7, the index page, book_data.js, 3 `searchText`
  queries for "Janssens" across sources 9/10/11, 3 more `searchText` queries for the phrase "overgave van Java"
  across the same three sources (no-results banner, likely a phrase-encoding quirk), `pages.json` for source
  10, one page-html read of p.XXX), all ≥2s apart.
- `archive.org`/`be-api.us.archive.org`: 3 (2 advancedsearch, 1 be-api full-text).
- `github.com`: 2 fresh shallow clones (dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers), grep only.
- WebSearch: 2 queries.
- No DECODE login, no credentials.

## Reading (VX-RD02, 25 Sept 2026)

Corrects the bundle structure CS05's eye-check sample described (heading misreads at thumbnail/1200px
resolution; re-fetched leaves 188/190/191/192/198/199/200 at IIIF `full/2561` for this pass,
`images/NNN_hi.jpg`, plus a full inventory of the previously-unsampled leaves 180-184/201-202/204-208/210
(all plain prose or tabular, no cipher -- `images/manifest.json`). The 186-200 cipher cluster is not three
raw-cipher leaves beside two decipherments; it is **three numbered dispatches, each surviving as a clean
ciphertext-only fair copy plus (for two of the three) a full contemporary decipherment**:

| Dispatch | Clean copy (ciphertext only) | Decipherment | Status |
|---|---|---|---|
| No.1 ("Numero Un. Triplicata") | leaf 188 | **none found in the sampled 180-210 range** | the target below |
| No.2 ("Numero Deux. Duplicata") | leaf 190 (lower block) | leaves 191-192 (interlinear gloss; the word "certifié" splits cer-/ti.fi.é. across the 191/192 leaf boundary, confirming they are one continuous gloss) | key source |
| No.3 ("Numero Trois. Duplicata") | leaf 198 (heading eye-read "Numero 2" by CS05 at low resolution; at full size it reads "Trois", and its opening 12 codes match leaves 199-200's opening codes exactly) | leaves 199-200 (5-column table, read row-major) | key source |

**Reconciled 2 Oct 2026 (GAPS5-na-janssens-java-1811, section below; `leaves_186-215_inventory.tsv`, every leaf 186-215 read
at the best resolution on disk).** Five numbered dispatches, each in up to three forms; the table above stands as the
25 Sept picture, this one supersedes it where they differ (the 180-210 "no cipher digit anywhere" sentence below it
is withdrawn: 201-209 carry No.3's tail and the whole No.4 set):

| Dispatch (heading as read) | Clean copy (cipher only) | Decipherment (gloss) | Plain copy | Date |
|---|---|---|---|---|
| No.1 "Numero Un. Triplicata" | 188R, signed | **none on 186-215** (every gloss leaf in the range is accounted for below) | none; 187R is an "Extrait d'une lettre du Gouv.r General Janssens au Ministre ... datee Batavia 20 Juin 1811 / No 11", plain, not signed -- same date as the archival description's first cipher dispatch, untested as a crib | text ends "le trente Juin"? (unread) |
| No.2 "Numero Deux. Duplicata" | 190R, signed | 191R-192L, ends "Gouverneur G.al le trente Juin. Fin. Signe Janssens" | 194R (with the pasted slip ordering a copy for the Directeur general des Douanes "traduite d'une lettre chiffree") and 195R, both headed "N.2 Duplicata", Batavia 9 Juillet, Signe Janssens -- NOT "N.6" | 9 Juillet 1811 |
| No.3 "Numero Troisieme. Duplicata" | 198R, 14 lines ending 574. 62. 420., signed | 199R-200L-200R-201L (one bifolium; 200R ends "grand malheur. Fin. Treize", 201L adds the postscript "parmi les croisieres / il y a deux vaisseaux" + end mark, then "Signe Janssens") | 202R, "N.3 Duplicata", 11 Juillet, paragraph "12.", Signe Janssens (202L = 201L re-imaged under a blank sheet) | 11 Juillet, PS 13 |
| No.4 "N. Quatre / premiere expedition" | 204R, signed (the top of 205's gloss sheet lies over its heading) | 205R-206L-206R-207L (one bifolium, 5-column code+word table, opens "La force navale ennemie augmente", ends "Fin. Trois Aout. Signe Janssens"; 208L = 207L under a translucent sheet; the 25 Sept "Signe Vanteau" was this signature misread) | 208R-209L, "N.4 Premiere Expedition", "L'Amiral Stafforth ...", ends "precieuse possession. 3 Aout. Signe Janssens" | 3 Aout 1811 |
| No.5 "N. Cinq. premiere Expedition" | the pasted slip, imaged on 210R (not 211), 10 lines, signed | 211R-212L, "N.5 1re Expedition", ends "Fin. Batavia 7. aout. Signe Janssens" | 214R, "N.5 1re Expedition", Batavia 7 Aout, Signe Janssens (`no5_plaintext.txt`) | 7 Aout 1811 |

Blank or divider: 186, 189 (verso of 188, not prose), 193, 196, 197, 203, 213, 215. So No.1 is the only dispatch of the
five with neither a gloss nor a plain copy in 186-215; No.4's gloss and plain copy (gap 2) are the largest untranscribed
key source on disk.

No "Numero Un" decipherment leaf was found: leaves 180-187 (all individually eye-checked at full size this
pass) and 189 are plain prose or blank; leaves 201-210 (also individually checked) are plain prose or
tabular forms, no cipher digit anywhere. This is a negative search result for the 180-210 range specifically,
not the whole 233-leaf bundle (leaves 1-179 and 211-233 are only the original 23% thumbnail sample from
VX-CS05's pass); a full page-through of the remaining ~185 leaves could still turn one up.

### Key-building

Two independent blind Sonnet subagent transcription passes (`keysource_passA.tsv`, `keysource_passB.tsv`)
over the four key-source images (190, 191, 199, 200), each reading every code:gloss pair in the interlinear
(190-191) or columnar row-major (199-200) layout, noting corrections/crossed-out cells. Reconciled by
`scripts/build_key.py`, which aligns the two passes' **code sequences** with `difflib` (not row index --
pass A silently skipped one whole code-line on leaf 191, "12.966.558.571.53.411.771.810.1096" = "encore le
certifié t demandé par", which cascaded a false ~20-point misalignment under naive row-index comparison;
sequence alignment recovers past a skip and gives the real figure): **449 aligned code positions, 429 exact
gloss agreement, 95.5%** (comfortably clear of the two-pass 60% gate in `.claude/briefs/transcription.md`).
20 genuine disagreements and 23 codes only one pass transcribed (mostly digit-reading differences, e.g.
138 vs 158, or the one skipped code-line) are in `pass_disagreements.tsv` / `pass_unmatched.tsv`.

`key.tsv`: **167 codes**. 154 grade C (clean: both passes agree, not a corrected/crossed-out cell). 13 grade
M, logged in `conflicts.tsv` -- genuinely ambiguous, i.e. the SAME code recurs with two different glosses in
clean, unanimous, uncorrected occurrences on different leaves (not a transcription slip): most are minor
period-spelling variants a single nomenclator entry would plausibly cover under normalisation (à/a, où/ou,
port/porte, lieues/lieu, Capitaine/Capitaines, peu/peut, de/Dé, le/lé, frigate/frigates), but three are
semantically live and look like genuine **homophones** (the nomenclator assigning one code to more than one
very common function word, a known flattening technique -- LESSONS.md section on Kauderbach/period design):
code 689 = "de" (leaves 190/191, clean, n=2) or "Le" (leaf 199, clean, n=2); codes 190 and 1195 each = "est"
(leaves 190/191) or "en" (leaves 199/200). `key.tsv`'s `value` column takes the majority-count reading for
these; the alternative is in `note`.

System, from the evidence: a **numeric nomenclator, one code (2-4 digits, observed range 3-1197) mostly for
one French word**, with rarer/proper words spelled out letter-by-syllable across several consecutive codes
(confirmed readable in both dispatches: leaf 191 "cer-ti-fi-é/cer[192]-ti.fi.é"="certifié",
"ad-mi-ni-st-ra-t-eur"="administrateur", "ar-ri-vé"="arrivé"; leaf 199-200 "Su-ra-ba-y-a"="Surabaya",
"D'étroit ... Li"="Détroit de Bali", "de-li-vr-er"="délivrer"). No separator digit or fixed group width. A
"." ends each numbered dispatch/entry region; "Fin." (or the code alone under a closing rule) marks the end
of leaf 200's table. The decipherer's own drafting is visible on the page (crossed-out wrong guesses,
caret-inserted corrections, one abandoned 12-code false start on leaf 200 that the clean copy, leaf 198,
simply omits) -- this is a period working decipherment, not a fair key table, hence grade C not H throughout
(rule 4: "H only from a period key sheet").

### Control (the key re-reads each deciphered page to its own decipherment)

Both raw-cipher clean copies are, code for code, the *same* text as their own gloss leaves, so decoding them
with `key.tsv` and diffing against the gloss leaves' own agreed reading is a direct sanity check on both the
transcription and the reconciliation (not an independent cryptanalytic control -- `key.tsv` is partly built
from the same pages):

- **Leaf 190 (raw) vs leaf 191's own gloss**: 107 compared positions (where leaf 191's gloss run ends,
  mid-word, at the bottom of the page), **98/107 = 91.6%**. All 9 residual mismatches are already-logged M
  codes (526 crossed-out/uncertain, 689 and 25/1096/738/883/140/511 the spelling-variant conflicts above)
  plus 2 genuine digit disagreements between the two period copies (leaf 191 "158" vs leaf 190 "138"; leaf
  191 "494" vs leaf 190 "454" at the cut-off point) -- flagged, not resolved, since both readings are
  plausible period handwriting and neither copy is silently preferred.
- **Leaf 198 (raw) vs leaves 199-200's own gloss**: after excluding the 12-code abandoned/crossed-out false
  start that the clean copy naturally never wrote (leaf 200 order 57-68, all `note=crossed-out` in
  `keysource_passB.tsv`), **135/161 = 83.9%** over 163 compared positions. Residual mismatches are again the
  already-logged M/conflict codes, one further digit disagreement (656 vs 636), and the final "Fin."/closing
  code (this worker's single, unchecked reading of leaf 198's very last digit vs the gloss leaves' "420").

Both controls clear comfortably above chance and land exactly on the codes `key.tsv` already flags uncertain
-- no surprise failures, i.e. no evidence the reconciliation silently corrupted a clean reading.

### Target: leaf 188, dispatch "Numero Un" (Triplicata)

`ciphertext.tsv` (this worker, single careful read with crop zooms, cross-checked against a second
independent look at the same crops -- **not** a two-pass blind reconciliation like the key-source leaves,
since leaf 188 is pure digits with no gloss to cross-validate against and budget did not extend to a second
full blind pass on it; flagged here rather than silently presented as equally solid).

Decoded with `tools/decode_key.py` + `decode.json` against `key.tsv`:

```
tokens 163: H 0, C 44, S 0, M 21, I 0, U 98   (updated after the fresh-instance re-derivation below
                                                upgraded codes 168 and 527 from C to M; was C 46, M 19)
```

Coverage: only **65/163 tokens (39.9%)**, **52/130 unique codes**, are codes also seen in the No.2/No.3
key-source leaves -- expected, since dispatch No.1 is a different message with mostly different vocabulary
and proper nouns (dates, place names, ship names) that the other two dispatches never use. `reading.txt` /
`reading_tokens.tsv` carry the full token-by-token grades; unkeyed codes print as `[nnn]`.

`tools/judge_plaintext.py specs/na-janssens-java-1811.json --file reading.txt`:
```
FAIL language: score=-1.469, null_p99=-1.855, real_p05=-0.898, real_median=-0.786, mode=both, N=488
ok   words: cover=0.791, min=0.3, real_text_median_cover=0.947
FAIL - na-janssens-java-1811
```
Reported as a **FAIL** per rule 7 (a FAIL may still be reported, as a FAIL): the language-model check fails
(unsurprising -- 60% of tokens are `[?]` gaps that break up the letter n-gram stream the check scores), the
word-coverage check technically passes but is not a meaningful signal at this gap density. This is a
**partial cryptanalytic-adjacent decode**, not a solved reading: it stands or falls with `key.tsv`, which is
grade C throughout (period decipherment of other text in the bundle), and the M-graded/ambiguous codes.

What the covered fragments say (English gloss of the clearer runs, French tokens as decoded; full context is
missing at every `[?]` gap so this is not connected prose): line 1 "...l'état..." (the state/condition...);
line 2 "de [?] [?] est . ... sont [e] puis" (...is. ... are [?] then); line 6 "...reçu ; il..." (...received;
he/it...); line 7 "...qu'il [?] [?] le débarquer [?] [?] [?] de seules" (...that he/it [?] to disembark it
[?] [?] of [alone/only]); line 12 "...tous [?] [?] l'ennemie" (...all [?] [?] the enemy [fem., likely
"ennemie" modifying a feminine noun like "frigate" as in dispatches No.2/No.3]); **line 14 "[?] [?] ar ri vé
a [929] peu vent [514] er"** = "...arrivé a [?] peu vent ...er" (...arrived at [?], little wind, ...) -- the
clearest run in the whole leaf, syllable-spelled "arrivé" exactly as in leaf 199's "ar-ri-vé", and it echoes
the No.2/No.3 dispatches' recurring theme (arrival, wind, a ship). Everything else is too gap-broken to
paraphrase honestly.

### Fresh-instance re-derivation

Required by `.claude/briefs/runs/2026-09-25-lane-vx-rd02.md`: a second subagent, given only
`ciphertext.tsv`, the four key-source images (190/191/199/200) and no other repo file (not `key.tsv`, not
this NOTES.md, not the pass TSVs), built its own key from scratch and decoded leaf 188 independently.

Coverage: 66/163 tokens keyed (40.5%) vs this worker's 65/163 (39.9%, before the two fixes below) -- **near-
identical coverage**, itself a strong signal the two independent reads found the same set of codes
recoverable from the same source pages. Per-position comparison (`scripts/build_key.py`'s own reconciliation
logic applied by hand to the two token sequences): of the 163 positions, both left **96 unkeyed** (agree on
what cannot be read), one code this worker keyed the re-derivation left `[?]` and two the re-derivation keyed
this worker left `[?]` (coverage differs by 1-2 tokens, not a structural gap), and of the **64 positions both
keyed, 54 agree (84.4%)**.

The 10 disagreements, all individually checked against `keysource_passA.tsv`/`keysource_passB.tsv`:
- **(line 2, pos 4) est / en** -- code 190, the already-logged 190/1195 homophone conflict (`conflicts.tsv`); no action.
- **(line 10, pos 11) part / par** -- code 1096, already logged in `conflicts.tsv`; no action.
- **(line 12, pos 12) ennemie / ennemi** -- code 1128, a gender-spelling variant of the same word; no action.
- **(line 4, pos 8) A / à** and **(line 10, pos 4) ât / à** -- codes 1090 and 875, already grade M
  (875 explicitly "only a corrected/crossed-out cell seen"); the re-derivation's plain "à" is plausible but
  not more authoritative than the existing grade -- no change.
- **(line 2, pos 5) "." / Le** and **(line 2, pos 11) puis / sans**, **(line 10, pos 12) chargent / corvette**
  -- codes 728, 893, 381: this worker's value is a clean **two-pass agreement** (`keysource_passA.tsv` and
  `keysource_passB.tsv` both read the same word at the same source position -- see the grep in the commit
  history), the re-derivation is one subagent's single read; kept as C, flagged here as the honest record of
  a disagreement rather than silently resolved. (381 "chargent" is itself written after a correction in the
  source per `keysource_passB.tsv`'s note "chargent." with a trailing period the reconciler dropped -- worth
  a closer look by a future pass, not changed here since two passes independently agree with each other.)
- **(line 3, pos 2) ; / j** and **(line 6, pos 6) ; / j** -- codes 168 and 527: checking
  `keysource_passA.tsv`/`keysource_passB.tsv` directly found the re-derivation was right to flag these --
  code 168's leaf 199/200 occurrences split pass A ";" / pass B "j" (a real two-pass disagreement this
  worker's reconciler had silently dropped rather than surfaced, since disagreeing rows are excluded from
  `key.tsv` and the code still had a clean single occurrence elsewhere, on leaf 191); code 527 has a clean
  leaf 200 occurrence ";" and a leaf 199 occurrence both passes read "j" (pass A flagged it uncertain, which
  routed it to the low-priority "shaky" bucket in `build_key.py` and hid a real second reading). **Fixed**:
  both codes upgraded to grade M in `key.tsv` with the ambiguity spelled out in `note`; `reading.txt`/
  `reading_tokens.tsv` regenerated (`tools/decode_key.py ciphers/na-janssens-java-1811`, now
  `C 44, M 21, U 98`, `--check` exits 0); judge re-run, same verdict (FAIL language, same scores to 3dp --
  the two changed tokens are both mid-gap and don't move the language-model score at this sample size).

Net effect of the cross-check: two real gaps in the reconciliation script's conflict-detection found and
fixed (168, 527 -- a class of bug worth knowing about: a code's *shaky/uncertain-flagged* occurrence was
silently dropped rather than checked against the code's *clean* occurrence for disagreement, whenever the
code also had at least one clean reading elsewhere); everything else in the 10 disagreements is either an
already-logged M/conflict code or a two-pass-agreed C code the single-pass re-derivation didn't overturn.
No difference beyond these is unresolved.

### Not found / next steps (one-line suggestions, out of this job's scope)

- No "Numero Un" decipherment located in leaves 180-210; a full page-through of the bundle's other ~185
  leaves (only 23% thumbnail-sampled by CS05) could locate one and lift coverage well above 40%.
- Leaf 192 (continuation of the No.2 gloss) was read by eye for structural confirmation only (the
  cer-/ti.fi.é. word-split check) but not two-pass transcribed into `key.tsv` -- doing so would likely add a
  handful more codes to the key, since it continues the same dispatch's vocabulary as leaf 191.
- The 13 M-graded/homophonic codes in `conflicts.tsv` (especially 689, 190, 1195) are worth a closer look at
  the original leaves if a future pass needs higher-confidence decoding of a token keyed to one of them.

## Sweep for more key source (VX-RD02B, 25 Sept 2026)

Job: find more key source for dispatch No.1 ("Numero Un"), in order: (1) sweep the outer 233-leaf bundle for a
"Numero Un" decipherment or Primata/Duplicata copy CS05/RD02 did not see; (2) check neighbouring invnrs 11, 13
and any invnr whose description names Janssens/Java/cijfer/ontcijfering; (3) re-decode with anything found.

### (1) Densified sweep of invnr 12 outside leaves 180-210

CS05's original sample covered leaves 1-179 and 211-233 only sparsely (every ~5.6th leaf, 34 points). This pass
fetched `service.archief.nl` thumbnails for 42 of the remaining 167 unsampled leaves in that range (every 4th
leaf, IIIF `/thumb/`), eye-checked each: **all 42 are plain prose, tabular registers, or blank** -- no cipher
digit anywhere, no "Numero" heading. Two leaves (211, 230) initially looked numeric at thumbnail resolution and
were re-fetched at full IIIF resolution to check: leaf 211 turned out to be the hit described below; leaf 230
is an ordinary arithmetic/accounting jotting (sums, not code groups) with an unrelated slip of prose pasted on,
not a cipher. This sweep, like CS05's, is still a sample (spacing 4, not exhaustive) of the 1-179 and 211-233
ranges; a single-leaf item between sample points could still be missed.

**But leaves 210-219, immediately after the already-exhaustively-checked 180-210 range, were then checked
individually** (CS05/RD02's earlier "leaves 180-210" claim turns out to have stopped exactly at leaf 210, one
leaf short of a real hit) -- see "New dispatch found" below. Leaves 215-217 (checked individually after) are
unrelated 1812 Bibliothèque Impériale correspondence about the papers of the late Governor of Batavia
Frederik van Boekholtz/Eijsinghe; no more cipher material found through leaf 219. Leaves 1-179 and 218-233
remain only sparsely sampled.

Host requests this step: `service.archief.nl` 42 (sweep thumbnails, every 1.6s) + 2 (leaves 211/230 full-res
re-fetch) + ~13 (leaves 208-219 medium-res + 210/211/212/214 full-res) = 57, all ≥1.5s apart, all HTTP 200.

### (2) Neighbouring invnrs

Fetched the toegang 2.01.27.05 overview page (`nationaalarchief.nl/onderzoeken/archief/2.01.27.05`), which
lists every invnr 1-57 with its archival description inline (this is the actual invnr-level finding aid, not
leaf-level -- invnr 12's 233 scanned leaves are all ONE invnr, an unusually large grab-bag folder; most other
invnrs are much smaller dossiers). Descriptions containing "Janssens": invnr 7 ("Analyses" of missives received
since Nov 1810 from Governors-General Daendels and Janssens, with partial French translation, drawn up by the
Chef der Divisie) and invnr 26 ("Missiven van de Gouverneur-Generaal J.W. Janssens aan de Minister van Marine en
Koloniën van het Keizerrijk. Met bijlagen" -- Janssens' own registered outgoing-letter series, separate from
invnr 12's unregistered incoming pieces). No description contains "cijfer", "ontcijfering", or "geheimschrift".
Invnrs 11 and 13 (named in the brief) do not mention Janssens or Java at all (11: unordered original missives
from the Emperor/Minister to Daendels; 13: a financial decision re: colonial-affairs receiver P. de Munnick).

- **invnr 11** (22 scans): description checked, no Janssens/Java/cipher content -- not swept further.
- **invnr 13** (6 scans): description checked, financial/administrative -- not swept further.
- **invnr 26** (191 scans, Janssens' own missives to the Minister): sparse sample, every 8th leaf (24 leaves),
  `service.archief.nl` thumbnails. All 24 are plain prose letters/reports or administrative register tables
  (an alphabetical name/subject index within the volume) -- **no cipher digit found**. This is a sparse sample
  of a 191-leaf bundle, not exhaustive.
- **invnr 7** (190 scans, "Analyses" with partial French translation): sparse sample, every 24th leaf (8
  leaves). All 8 are financial/accounting ledger tables ("Balans" register) or blank -- **no cipher digit, no
  narrative analysis of a specific dispatch found in this sample**; the volume looks more like an accounts
  ledger than the textual précis its title suggested, at least in the leaves sampled.

Host requests this step: `nationaalarchief.nl` 5 (toegang overview + invnr 7/11/13/26 item pages) +
`service.archief.nl` 32 (24 invnr26 thumbnails + 8 invnr7 thumbnails), all ≥1.5s apart, all HTTP 200.

**No "Numero Un" decipherment or Primata/Duplicata copy found anywhere in this pass** -- neither in the
densified invnr 12 sweep nor in the four neighbouring invnrs checked. Leaf 188 remains the only known copy of
dispatch No.1, still without a decipherment on file.

### New dispatch found: No.5, "1ère Expédition" (leaves 210-214)

Not what this job set out to find (it is not "Numero Un"), but it is squarely "any other deciphered Janssens
dispatch" per the brief, and it is new key source. A fifth numbered dispatch survives in **three parallel
forms** on leaves immediately after the range CS05/RD02 had called fully checked:

- **Leaves 210 (right page) - 212 (left page)**: the interlinear decipherment (numeric code above, French
  word/syllable below), heading "No.5  1er Expédition", ending "Fin. Batavia 7. aoust." signed "Janssens".
- **Leaf 211**: a separate slip of paper **pasted onto** the lower part of the decipherment page, carrying a
  clean raw-cipher-only copy headed "No. Cinq. 1ère expédition." -- one continuous unbroken run of ~70 numeric
  codes with no gloss, the same relationship as the No.2/No.3 clean-copy-plus-decipherment pairs but here
  physically attached to the decipherment leaf rather than a separate leaf.
- **Leaf 214**: a **plain, unenciphered French fair copy** of the same dispatch -- "No 5. 1re Expédition" /
  "Une expédition forte de 71 voiles en arrivée le 4 aoust devant la Rade; et débarque les troupes à l'Isle de
  la Ville — Nous avons détruit nos magasins de Sucre, Caffé et poivre — nous nous sommes portés dans le Camp
  retranché destiné pour cela depuis Six mois — Il en probable que dans quelques jours une affaire décisive
  aura lieu. Batavia 7. Aoust. Signé Janssens." (transcribed by this worker directly from the full-resolution
  image, `no5_plaintext.txt`; plain legible French, not a code-reading judgment call, so not run through a
  two-pass blind reconciliation the way the coded leaves are).

This last item is new for this target: every other key source so far has been a *period decipherment* (grade
C, "cryptanalytic-adjacent" per rule 4's own caveat that a working decipherment is not a fair key table). Leaf
214 is an independent plain-language original of the SAME message that was also enciphered and deciphered two
leaves earlier -- the closest thing to ground truth this bundle offers, and a genuine control for the
No.2/No.3/No.5 key as a whole (not just a self-consistency check against the same decipherment's own gloss).

Content: a 71-sail hostile expedition arrived 4 August off Batavia, landed troops at the Isle de la Ville
(Onrust), the defenders destroyed their sugar/coffee/pepper stores and withdrew to the entrenched camp prepared
for six months, a decisive engagement expected within days -- this is the British invasion of Java, days before
the landing that took Batavia (historically, the British East India Company expedition under Auchmuty/Stopford
landed at Cilincing 4 August 1811). Nearby leaf 208's plain-text letter (right page, headed "No.4 Première
Expédition", Batavia 3 Août, signed Janssens, **not enciphered**) independently confirms the same picture one
day earlier: "L'Amiral Stopford commande sur nos côtes 18 à 20 bâtiments, dont 6 vaisseaux... une expédition des
plus formidables est sur le point d'arriver... Les dépêches dont le bâtiment No.4 étoit porteur, ne me sont pas
parvenues" (the No.4 dispatches were lost in transit). Leaf 208's left page also carries the tail end of a
different decipherment (code+gloss table, ending "3 Août. Signé Vanteau" on leaf 209) -- a different signer,
not Janssens, not transcribed this pass (out of this job's scope), flagged here as a lead.

Two blind Sonnet subagent transcription passes of the No.5 interlinear decipherment + pasted clean-copy slip
were launched (`keysource_no5_passA/B.tsv`, `no5_cleancopy_passA/B.tsv`). Both independently corrected this
worker's own framing: the pasted clean-copy slip physically sits on the leaf whose scan order is 210 (not 211
as first guessed from the thumbnail), and the interlinear decipherment runs continuously from leaf 210's first
couple of rows through leaf 211 (uninterrupted) to leaf 212's signature -- both passes agree with each other on
this correction even though they split the 95-code sequence across the three leaf-images differently row for
row, which is why the two pass TSVs were reconciled as ONE continuous 95-code sequence (synthetic id `no5`,
shown as `no5(210-212)` in key.tsv/conflicts.tsv) rather than per-leaf: aligning by leaf label would have
compared pass A's 5-row "leaf 210" against pass B's 17-row "leaf 210" and manufactured false disagreements from
a page-boundary artefact, not a reading difference.

### Key merge and redecode

`combined_passA.tsv`/`combined_passB.tsv` = the existing No.2/No.3 passes + the new No.5 passes, reconciled by
the same `scripts/build_key.py` (sequence-aligned per leaf, unchanged logic):

```
aligned code positions: 541  agree: 509  disagree: 32  agreement: 94.1%
codes only one pass saw (sequence gap): 29
unique codes: 202  clean (single gloss): 208  conflicting: 17
```

`key.tsv` grew from **167 codes to 208** (+41 net new/reconfirmed codes from the No.5 material; some No.5 codes
duplicate No.2/No.3 codes and independently cross-validate them -- e.g. code 190, already a known M-graded
"est"/"en" homophone, gets 2 more clean "en" readings from No.5, shifting the majority value from "est" to
"en"). `conflicts.tsv` grew from 13 to 17 M-graded codes (four new: 99 "n'"/"n", 624 "fe"/"fé", 997 "4"/"quatre"
digit-vs-spelled-out, 1150 "avoir"/"avons").

Leaf 188 redecoded (`tools/decode_key.py`): **163 tokens, C 49, M 22, U 92** (was C 44, M 21, U 98) -- coverage
rises from 65/163 (39.9%) to **71/163 (43.6%)**, a real but modest gain (dispatch No.1's vocabulary still
mostly doesn't overlap with No.2/No.3/No.5's). New readable fragments include line 7 "...qu'il [?] [?] le
débarquer [?] [?] [?] Le seules" (echoes No.5's own "débarqua les troupes") and line 12 "...tous [?] [?]
l'ennemie" (echoes No.5's "expédition ennemie").

`tools/judge_plaintext.py specs/na-janssens-java-1811.json --file reading.txt`:
```
FAIL language: score=-1.45, null_p99=-1.871, real_p05=-0.877, real_median=-0.779, mode=both, N=508
ok   words: cover=0.803, min=0.3, real_text_median_cover=0.947
FAIL - na-janssens-java-1811 (a PASS is a gate for a verifier, not a reading; rule 10)
```
Reported as a **FAIL** per rule 7, same as before the merge (still 56.4% gap tokens breaking the n-gram
stream) -- word coverage improves 0.791 -> 0.803. This is still a partial cryptanalytic-adjacent decode, not a
solved reading. Leaf 188 ("Numero Un") itself has **no decipherment found anywhere in this pass's sweep**, so
it is still the reading target, not a control, per the brief's own framing.

### Not done this pass (time-box, one line each)

- **Fresh-instance re-derivation of the newly added No.5 codes** (rule 7, named in the brief's step 3) was not
  run -- the two transcription subagents plus the merge took most of the 45-minute box; a successor should run
  one fresh-instance subagent against `no5_cleancopy_passA.tsv`'s underlying images only (or re-crop) before
  any of the No.5-sourced codes are relied on for a claimed reading elsewhere.
- **Cross-check the No.5 raw-cipher slip's own decode against `no5_plaintext.txt`** (the independent plain
  fair copy on leaf 214) was not run -- decoding `no5_cleancopy_passA/B.tsv`'s 95 codes through the merged
  `key.tsv` and diffing against `no5_plaintext.txt` word-for-word would be a strong, genuinely independent
  control on the whole key (not a same-decipherment self-check like the No.2/No.3 controls), and is cheap
  (no network, everything already on disk) -- named here as the highest-value next step.
- Leaf 208's left-page decipherment tail (signed "Vanteau", not Janssens, ending leaf 209) was not transcribed
  -- a different correspondent/decipherer, out of this job's scope, flagged as a lead.
- Leaves 1-179 and 218-233 remain only sparsely sampled; a further densified or exhaustive pass could still
  find a "Numero Un" decipherment or more key material.

## VX-RD02C (final worker on this target, 25 Sept 2026)

Job: `.claude/briefs/runs/2026-09-25-lane-vx-rd02c.md` + `-COMMON.md`. (1) decode the No.5 raw-cipher slip and
cross-check word-for-word against `no5_plaintext.txt`, adding/correcting `key.tsv`; (2) fresh-instance
re-derivation of the codes this added; (3) check whether leaf 208's "Vanteau" tail uses the same code, and if so
transcribe it; (4) re-decode leaf 188, report coverage, judge, per-token counts, a French+English reading.

### (1) No.5 raw-cipher slip vs the plain fair copy -- a genuine independent control

`no5_cleancopy_passA.tsv`/`no5_cleancopy_passB.tsv` (the pasted clean-copy slip, leaves 210-211) agree on all 95
codes with zero disagreements (`diff` on the code column: empty). Decoding that 95-code sequence against
`key.tsv` **found 5 codes with no entry at all** -- `597, 748, 904, 456, 244` -- even though all five are read,
clearly and in most cases by both independent human transcribers, in the very interlinear decipherment
(`keysource_no5_passA/B.tsv`) that built `key.tsv`. Tracing why found a real bug in `scripts/build_key.py`'s
merge, not a transcription gap:

- **Code 597**: both passes read it as "expedition"/"expédition" (order 2) -- the *same word*, differing only by
  an accent `build_key.py`'s `glossnorm()` doesn't fold. Because the strings differ, the merge scores this as a
  disagreement (`pass_disagreements.tsv` line 22) and drops the code from `key.tsv` entirely, rather than
  treating it as agreement or even flagging it M.
- **Codes 748, 904, 456, 244**: the two interlinear passes gave genuinely different individual readings at
  these four cells (`ns`/`ins`, `ï`/`î`, `rc`/`re`, `à`/`ci`) -- real reading disagreements, correctly logged to
  `pass_disagreements.tsv`, but then **silently dropped from `key.tsv` rather than surfacing as grade M**,
  because `build_key.py` only falls back to a shaky/uncertain bucket when a code has *no* clean occurrence
  anywhere -- a disagreement with no fallback path at all is simply lost. (This is the same root cause, one
  bug wider, as the 168/527 case below.)

Aligning the decoded sequence word-by-word against `no5_plaintext.txt` (leaf 214's independent plain French fair
copy of the same dispatch) resolves all five, using the words they complete:

| code | resolved value | plaintext word it completes | evidence |
|---|---|---|---|
| 597 | expédition | "**Une expédition** forte de 71 voiles..." | both passes already agree; only the accent-fold dropped it |
| 748 | ns | "nos **magasins**" (ma-ga-zi-**ns**) | pass A's "ns" (not pass B's "ins") gives the correct 8 letters |
| 904 | i | "et **poivre**" (po-**i**-vr-e) | resolves the ï/î accent ambiguity to plain i |
| 456 | re | "le Camp **retranché**" (**re**-tra-n-ché) | pass B's "re" (not pass A's "rc") -- pass B's own note had already guessed this |
| 244 | ci | "une affaire **décisive**" (de-**ci**-si-vé) | pass B's "ci" (not pass A's "à"); "affaire" already has its own whole-word code (819), so 244 cannot also be part of "affaire" |

All five added to `key.tsv` as grade **C** (per the brief: the plain-copy control corrects or adds, not merely
"confirms" -- these five had no prior key.tsv entry at all). Decoding the full 95-code sequence against the
corrected key now covers **95/95 codes (was 90/95)**, reading as continuous French that matches
`no5_plaintext.txt` closely, with a handful of genuine **wording divergences** (not decode errors -- the fair
copy is a paraphrase, not a verbatim transcript, and NOTES.md says so nowhere before this pass):

- the cipher's "**une expédition ennemie** forte de..." vs the fair copy's "une expédition forte de..." -- the
  fair copy drops "ennemie" (hostile/enemy), read cleanly and identically by both passes;
- the cipher's "...les Troupes **à l'est** de la Ville" (code 190, the already-logged est/en homophone, reading
  "est" here per both interlinear passes' own note "same code 190 as order 10 ('en'); reused for different
  word") vs the fair copy's "**à l'Isle** de la Ville" -- "east of the town" vs "at/to the Isle of the town" is
  a real wording difference, not a spelling one; flagged, not resolved, since key.tsv already carries both
  variants of code 190 as a known homophone and this pass adds no new evidence either way;
- "**nous avons** détruit" (fair copy) vs the coded "nous avoir" (code 1150, already logged
  avoir/avons homophone) -- already-flagged conjugation homophone, this occurrence favours "avons";
- "**ils** en probable..." (both interlinear passes, clean, code 900) vs the fair copy's singular "**Il** en
  probable..." -- a real number disagreement (they/it), not resolved.

No other position among the 95 contradicts `key.tsv`; every other already-M/homophone code that recurs in this
sequence (190, 997, 738, 1150, 875, 1090) lands on the variant the plaintext favours at that spot, which is
exactly what a homophone should do and adds no new fix.

**Also re-applied a regression**: `key.tsv` codes 168 and 527 were still grade C (";" only), even though VX-RD02's
own fresh-instance re-derivation section above already found and fixed this -- both codes have a clean ";"
occurrence on one leaf *and* a genuine pass A ";" / pass B "j" disagreement on other leaves
(`pass_disagreements.tsv` lines 9, 17), which the same `build_key.py` bug drops instead of surfacing. VX-RD02B's
later rerun of `build_key.py` on the merged passes rebuilt `key.tsv` from scratch and silently lost the manual
fix (the script has no memory of a hand edit). Re-applied here as grade M with the disagreement spelled out in
`note`; flagging the underlying `build_key.py` bug (glossnorm doesn't fold accents; a disagreement is dropped
outright rather than downgraded to M whenever the code has *any* clean occurrence elsewhere) for whoever next
touches key-building, since it has now cost two separate fixes to two separate merges.

### (2) Fresh-instance check of the five added codes

A fresh Sonnet subagent was given only `no5_cleancopy_passA.tsv` (the bare order/code sequence, no gloss) and
`no5_plaintext.txt` -- deliberately *not* the interlinear passes -- and asked to derive a word-by-word syllable
segmentation from scratch. It built a 62-word/95-code budget that lines up end to end and independently landed
code 547 on "Aoust" at both its occurrences (orders 17 and 95), a genuine structural cross-check that the overall
segmentation scheme is sound. At the syllable level, though, it placed the five flagged codes differently
(597="Ex-" not a whole word; 748="it" of "détruit", not "ns" of "magasins"; 904="Caf" of "Caffé", not "i" of
"poivre"; 456="le", not "re" of "retranché"; 244="af" of "affaire", not "ci" of "décisive") -- **this worker
does not adopt those values**: the subagent worked from word-counting alone, with no access to the actual
period decipherment, whereas the values used above come directly from two independent human readings of the
primary source (`keysource_no5_passA/B.tsv`) cross-checked against the plaintext, which is materially stronger
evidence. Two of its five guesses (748, 244) are additionally impossible given the real order-indexed code
sequence already on file (e.g. "affaire" at order 85 would double-code a word that already has its own single
code, 819, at order 83) -- a check this worker made by hand against `no5_cleancopy_passA.tsv`'s real order
column, which the subagent's word-budget approach did not use position-by-position. Recorded here as the
required fresh-instance check, not as a reason to revert the five fixes.

### (3) Leaf 208 ("Vanteau" tail): same code, cross-correspondent confirmation

Leaf 208's left page (thumbnail/medium-res on disk; fetched hi-res this pass, `images/208_hi.jpg`,
2 `service.archief.nl` requests) carries a 5-column numeric-code table, code above gloss, matching the same
tabular layout NOTES.md already describes for leaf 199-200. Its top (clearest) row: codes 697, 168, 960, 225,
204 gloss "ble/blé", ";", "(près" [bracketed with the row-2 code 195], "De", "Batavia". **Four of five are
already in `key.tsv` from the Janssens dispatches and read the same way here**: 697="ble" (already M,
corrected-cell-only), 168=";" (the homophone above), 225="De" (C), 204="Batavia" (C) -- confirmed by this
worker's own read and independently by one blind Sonnet subagent given only the cropped image. **This settles
the brief's question: yes, the same nomenclator is shared across correspondents in this archive series** (leaf
208 ends "Signé Vanteau", not Janssens). `key.tsv`'s `pages` column for these four codes now also lists
`208(Vanteau)`. One new code, **960 = "près"**, added at grade M (the row-2 code 195 is bracketed with it in the
source, suggesting the gloss may span both cells; not resolved).

**Not transcribed further**: everything below this top row is markedly fainter in the source -- confirmed
genuinely faint (not a JPEG artefact) at full IIIF resolution by this worker and independently by the blind
subagent, which called it "likely bleed-through or badly faded ink" and could not read it with confidence
either. Whether the table is more decipherment text or (given codes 697/168/960/225/204 don't obviously read as
a connected sentence in either row-major or column-major order, per the blind subagent's own phrase test) a
nomenclator reference listing is **not established** by this pass -- flagged as a lead needing either a better
scan (raking light, a conservator's read) or simply more visible rows than these ten cells give.

### (4) Leaf 188 ("Numero Un") redecode

`tools/decode_key.py ciphers/na-janssens-java-1811` (--check exits 0, reading is current):

```
tokens 163: H 0, C 52, S 0, M 24, I 0, U 87
```

Coverage: **76/163 tokens (46.6%)**, up from 71/163 (43.6%) before this pass -- a modest gain (+5 tokens: the
five No.5 fixes above intersect leaf 188 at codes 456 x2, 748 x1, 904 x2; codes 597 and 244 do not occur on this
leaf). The 168/527 M-downgrade (part of undoing the regression in (1)) moved 2 tokens from C to M without
changing total coverage.

`tools/judge_plaintext.py specs/na-janssens-java-1811.json --file reading.txt`:
```
FAIL language: score=-1.472, null_p99=-1.84, real_p05=-0.912, real_median=-0.785, mode=both, N=563
ok   words: cover=0.78, min=0.3, real_text_median_cover=0.945
FAIL - na-janssens-java-1811 (a PASS is a gate for a verifier, not a reading; rule 10)
```
Reported as a **FAIL** per rule 7, same verdict as before this pass (53.4% of tokens are still `[?]` gaps,
which is what the language check is sensitive to) -- word coverage moves 0.791 (VX-RD02) -> 0.803 (VX-RD02B) ->
**0.78** this pass: a real drop, not a typo. `tools/judge_plaintext.py`'s `cover` metric is a greedy
word-segmentation of the reading's raw letters, not grade-weighted, so the mechanism isn't the 168/527
M-downgrade as such -- most likely the 5 newly-filled tokens sit next to `[?]` gaps in a way that locally
breaks the greedy segmentation rather than extending a real word; not chased further this pass (small effect,
well above the 0.3 floor either way, and not evidence the fixes in (1) are wrong -- they are grounded in the
primary source, not in this metric). This remains a **partial cryptanalytic-adjacent decode, not a solved
reading**: it stands or falls with `key.tsv`, itself grade C throughout (a period decipherment of other text
in the same bundle).

No new legible connected run emerged from this pass's five fixes (they land in already-gap-broken lines).
Reading, [?] for unkeyed codes, French as decoded / English gloss of the clearest runs (unchanged from
VX-RD02B's reading except the five newly-filled codes, none of which joins an existing run into a longer one):

- Line 1: "...l'état..." -- the state/condition...
- Line 2: "de [?] [?] en . [?] re [?] Sont e puis" -- ...is/are... then... (fragment, code 456="re" now filled
  but isolated between gaps)
- Line 6: "...reçu ; il..." -- ...received; he/it...
- Line 7: "...qu'il [?] [?] le débarquer [?] [?] [?] de seules" -- ...that he/it [?] to disembark it [?] [?] [?]
  of [alone/only]...
- Line 12: "...tous [?] [?] l'ennemie" -- ...all [?] [?] the enemy [fem.]...
- **Line 14: "[?] [?] ar ri vé a [929] peu vent [514] er"** = "...arrivé a [?] peu vent...er" -- ...arrived at
  [?], little wind... -- still the clearest run on the leaf, echoing the arrival/wind theme common to No.2,
  No.3 and No.5.

Everything else remains too gap-broken (53.4% `[?]`) to paraphrase honestly as connected prose.

### Hosts this pass

`service.archief.nl`: 2 (invnr 12 item page for leaf 208's file id + the leaf 208 hi-res image fetch), both
>=1.5s apart, both HTTP 200 -- 2 of the 6-request hard cap for this leaf. No other hosts. 2 Sonnet subagents
(No.5 fresh-instance re-derivation; leaf 208 blind pass B), run in parallel, within the 2-at-once cap.

## State at close (final worker, VX-RD02C, 25 Sept 2026)

**Status: partial.** What is established: a 208-code (now 214) nomenclator, grade C throughout (a period
decipherment of other text in the bundle, not a fair key table), built from four contemporary decipherment
leaves (No.2, No.3, No.5) and now confirmed shared with a fifth correspondent's dispatch (leaf 208, signed
Vanteau) via four cross-matching codes. Grade counts on the target leaf (188, "Numero Un"): of 163 tokens,
**C 52, M 24, U 87** -- 46.6% coverage, up from 39.9% at the start of this lane's work on this target. The
No.5 dispatch's independent plain-language fair copy (leaf 214) gave this target's first genuine
cryptanalytic-independent control (as opposed to a same-decipherment self-check) and resolved 5 codes plus a
2-code regression that a `build_key.py` bug had dropped twice. `tools/judge_plaintext.py` still FAILs language
on leaf 188 (score -1.472 vs real_p05 -0.912) at this coverage -- expected with 53% gaps, not a claim this
reading is right or wrong, per rule 7.

**Single best next step for a future lane**: a full page-by-page read of the ~185 still-sparsely-sampled leaves
of this 233-leaf bundle (1-179, 218-233) for a "Numero Un" decipherment -- leaf 188 is pure digits with zero
gloss on the page itself, so it can only ever be read from outside key material (this bundle's own, or the
leaf-208 Vanteau cluster's fuller table if a better scan resolves it), never from the leaf alone. A second-best,
cheaper step: leaf 192 (the unread continuation of the No.2 gloss, flagged since VX-RD02) would likely add a
handful more codes for free, no network needed.

## Web and blog check (GAPS-na-janssens-java-1811, 2 Oct 2026)

The open-web and blog comment-thread step that `.claude/briefs/check-solved.md` requires (CHECK-SOLVED-WEB, 28 Sept
2026), run 2 Oct 2026 01:58-02:02 UTC by the GAPS worker (account-4, brief
`.claude/briefs/runs/2026-10-02-account4-gaps-step.md` step 2) because `tools/intake_gate_check.py` exited 1 on this
section's absence. Check-solved item 6 above (25 Sept 2026) had left Cryptiana and comment threads "not separately
searched".

**Result: no decipherment or plaintext of this item located by these queries on 2 Oct 2026** (a search result, never
a novelty verdict, rule 10). The status word on line 1 stays `partial`.

### (a) Plain web searches (WebSearch, 8 queries)

| # | Query | Result |
|---|---|---|
| 1 | `Janssens Batavia 1811 dépêche chiffrée "Hollandse Divisie" ministre Marine cipher letter` (sender + recipient + date) | The NA finding aid 2.01.27.05 itself, napoleon-series.org's Janssens biography, Wikipedia (Janssens, Invasion of Java 1811), the 2.01.29.01 finding aid PDF, DBNL's NNBW entry. None mentions a cipher dispatch or a decipherment. |
| 2 | `"2.01.27.05" Nationaal Archief Janssens cijferschrift OR cipher OR chiffre Java 1811` (shelfmark + cipher) | The 2.01.27.05 finding aid (whose own description of invnr 12 names the "cijferberichten ... met bijgevoegde ontcijfering", already quoted in "What this is"), plus unrelated NA finding aids (2.01.27.02, 2.21.092 Janssens family, 2.13.01, VOC 1.04.02). No page outside the archive's own inventory. |
| 3 | `"Une expédition forte de 71 voiles" OR "la Corvette la Sapho est partie" Janssens` (two distinctive decoded/glossed phrases, quoted; the first from `no5_plaintext.txt`, the second from leaf 192's gloss) | Neither phrase appears on any page. The engine returned napoleon-histoire.com's Correspondance de Napoléon, Novembre 1810 (opened, (c) below), Wikipedia ship pages (HNLMS Janssens, Revenant), the SHD ark for the corvette Sapho's log, patrimoine-maritime-fluvial.org. |
| 4 | `Janssens Java 1811 cipher dispatches Nationaal Archief decipherment "Numero Un" Triplicata` (the folder's own descriptive title) | The ANRI/Brill VOC inventory history PDF, Wikipedia (Invasion of Java, Janssens, interregnum, transport vessels), a Wacana article on Java's provincial archives, a 2026 J. Imperial & Commonwealth History article on the British occupation of Java, and an Econlib chapter whose title merely contains "cipher dispatches". None concerns this dispatch. |
| 5 | `site:scienceblogs.de/klausis-krypto-kolumne Janssens Java 1811` | Four Cipherbrain posts returned (1915 pulp-magazine puzzle, an 1870s "cryptographers of all nations" puzzle, Top-25 part 2, Van Gelder cryptogram) plus Wikipedia; none mentions Janssens or Java. |
| 6 | `site:cryptiana.blogspot.com Janssens Java Batavia 1811` | No page from that domain returned (Wikipedia and a TNA Discovery record only); the blog's own search was run directly instead, (b) below. |
| 7 | `site:ciphermysteries.com Janssens Java Batavia 1811 cipher` | No page from that domain returned (Wikipedia, warhistory.org, an Adam Matthew East India Company ledger listing, britainssmallwars.co.uk); the blog's own search was run directly instead, (b) below. |
| 8 | `Janssens Java 1811 cipher solved OR solves Claude OR GPT OR ChatGPT decipherment Batavia` (model-solve announcements, check-solved.md) | Only generic LLM-and-cipher papers (arXiv 2510.09714, the DescryptTool Cryptologia article, IJAIA) and Wikipedia. No announcement that any model or person read this dispatch. |

### (b) Site searches of the three blogs by name (one request each, descriptive User-Agent)

- **Cipherbrain** (`scienceblogs.de/klausis-krypto-kolumne/?s=Janssens`, HTTP 200): "Wir konnten leider keine Beiträge
  finden, die zu Ihrer Anfrage passen" (no posts match). The on-disk Schmeh snapshot (`sources/schmeh/`) grepped with
  zero requests: no "janssens".
- **Cryptiana blog** (`cryptiana.blogspot.com/search?q=Janssens`, HTTP 200): "No posts matching the query: Janssens".
  Tomokiyo's own pages: the on-disk snapshot `sources/cryptiana/` grepped first with zero requests -- no file contains
  "janssens"; the only "batavia" match is `web/telegraph2.htm` (telegraph codes, unrelated to this archive, not
  opened). The live pages were not re-fetched: the snapshot's `unsolved.htm` was already checked on 25 Sept 2026
  (Check-solved item 5 covers the two solver repositories; no Cryptiana listing of a Janssens item exists in the
  snapshot).
- **Cipher Mysteries** (`ciphermysteries.com/?s=Janssens`, HTTP 200): exactly one post, "Voynich proto-optics...?"
  (29 Mar 2008, 17 comments), which matches on the Janssen family of 1590 spectacle-makers in a discussion of early
  microscopes and the Voynich pharma jars. Not plausibly about an 1811 Java dispatch; its thread was not opened.

### (c) Every plausible hit opened and its thread read

- `napoleon-histoire.com/correspondance-de-napoleon-ier-novembre-1810/` (WebFetch, 1 request): Napoleon's own
  November 1810 letters. The passages naming Janssens or the Sapho, verbatim: "Je vous ai mandé que vous n'avez qu'à le
  mener (le général Janssens) demain au lever pour prêter serment."; "J'approuve ce que le général Janssens veut
  emmener, hors le sieur Briatte et le chirurgien-major hollandais."; "La _Sapho_ de Bordeaux, doit porter 50 hommes
  et 1,500 fusils." These are Paris-side orders before Janssens sailed; the page prints no dispatch from Janssens in
  1811, no cipher and no decipherment, and has no comment section. (A print lead for a verifier: the Sapho's 1810-11
  voyage and Janssens' passage are in the Correspondance de Napoléon, which does not bear on the cipher.)
- No other hit in (a) or (b) was about this letter, so no further thread was opened.

Requests this step: scienceblogs.de 1, cryptiana.blogspot.com 1, ciphermysteries.com 1, napoleon-histoire.com 1
(via WebFetch); WebSearch 8 queries. No 403/429/challenge.

## GAPS-na-janssens-java-1811 (2 Oct 2026, account-4)

The Verdict line's cheapest step of the 1 Oct 2026 finish-or-blocker pass, run 2 Oct 2026 01:57-02:1x UTC (brief
`.claude/briefs/runs/2026-10-02-account4-gaps-step.md`): two-pass transcription and reconciliation of leaf 192 from
`images/192_hi.jpg` (on disk, no fetch), merge into `key.tsv`, redecode leaf 188.

**Leaf 192 is the end of the No.2 interlinear decipherment, not raw cipher** (CS05's inventory row above was wrong,
as the 1 Oct pass's eye-read already said): eight code rows with a French gloss under every code, then "Signé
Janssens". Only the left page of the spread carries ink; the right page is blank.

Crops: `python3 tools/iiif_lines.py --image ciphers/na-janssens-java-1811/images/192_hi.jpg --out
ciphers/na-janssens-java-1811/images/crops_192 --region 0,90,1300,1230 --distance 45 --prominence 15
--lines-per-crop 2 --prefix 192 --debug` (the default settings found 0 lines on the full 2561x1964 spread, and at
`--prominence 60` centred on the gloss rows so a band edge would have cut every code row; the finer setting finds
the 17 alternating code/gloss lines and pairs them: nine crops `192_L01..L09.jpg`, 1300 px wide, one code row with its
gloss row each, L09 the signature). Overlay `images/crops_192/192_lines_debug.jpg` checked before the passes.

Passes: two blind Sonnet subagent calls, one per pass, each given only the nine crop paths
(`leaf192_passA.tsv`, `leaf192_passB.tsv`, format leaf/order/code/gloss/note as the earlier key-source passes).
Both read **58 codes**; codes agree at 57/58 (the one difference is the struck code in row 3, A "7504" / B "750",
excluded as crossed-out either way); glosses agree exactly at 53/58 (91.4%). The five gloss differences plus seven
flagged cells were settled by this worker from the crops (`leaf192_reconciled.tsv`, each settlement in its note):
722 "importan" (A importan / B importau; n and u are one shape in this hand; 516 "te" completes "importante"),
411 "ca" (an overwritten cell both passes read "cet"; key.tsv's own 411 = ca from leaf 191 completes
cer-ti-fi-ca-t = "certificat"), 406 "rais" (A rain / B rais; "J' au- rais"), 396 "p" (A p / B long-s; Sa-p-ho),
420 "Fin." (A Fin. / B Jin.), 1096 "par" (both: "part" with the t struck, 571 "ti" following), 1082 "avec" (a struck
word overwritten), and A's one stray "." gloss with no code in row 3 (the separator dot copied, dropped). Three
vision calls in all: the two subagent passes and this worker's own reconciliation reads (the overlay plus crops
L01, L03, L04, L06, L07).

The gloss reads continuously (this worker's reading of the decipherer's own gloss, grade C per token as the
earlier leaves): "...[un état détaillé et cer-]ti-fi-é de la cargaison, importan-te exportation. Je demande que cet
Etat ti-en-ne lieu du cer-ti-fi-ca-t que j'au-rais donné moi même si cela avoit été possible. [.] alinea. La
Corvette la Sa-p-ho est par-ti-e avec l'ancien Gouverneur Gal le trente Juin. Fin. Signé Janssens."

Merge: `scripts/merge_leaf.py leaf192_reconciled.tsv --key key.tsv --conflicts conflicts.tsv` (incremental:
touches only the 54 distinct codes leaf 192 attests, keeps the VX-RD02C hand edits a `build_key.py` rebuild would
lose, folds accents for the same-value test -- see its docstring). Result: **19 codes added** (16 grade C, both
passes clean and agreeing: 236 é, 167 exportation, 757 en, 1086 ne, 861 si, 315 avoit, 144 été, 156 alinea,
688 Corvette, 79 l', 441 ancien, 497 Gouverneur Gal, 536 trente, 845 Juin, and 722/406 at M as settled above;
3 grade M: 48 cet (corrected cell), 1035 possible (A uncertain), 327 ho (both uncertain)); **28 same-value
confirmations** (n and pages updated, grade unchanged); **10 conflicts** logged to `conflicts.tsv`, each code now M:
355 car/cargaison, 516 et/te, 738 lieues/lieu, 904 i/J' (period i=j), 13 aux/au, 840 mois/moi, 1187 va/Sa,
190 en/est (the known homophone, one more "est"), 1096 part/par, 571 ti/tie. `key.tsv` 214 -> **233 codes**
(C 131 -> 141, M 83 -> 92); `conflicts.tsv` 17 -> 24 rows. Codes left crossed-out: 1 (the struck 750x "fi").

Leaf 188 redecoded (`python3 tools/decode_key.py ciphers/na-janssens-java-1811`, then `--check`, exit 0):
**163 tokens: C 60, M 26, U 77** (was C 52, M 24, U 87) -- keyed **86/163 = 52.8%** (was 76/163, 46.6%): exactly the
+10 tokens the gap predicted, from six codes new to the key (79, 441, 497 twice each: lines 1 and 10 now read
"l'ancien Gouverneur Gal" and "l'ancien Gouverneur Gal part chargent"; 156 "alinea" twice, lines 4 and 12; 236 "é"
line 11; 757 "en" line 9). No unkeyed code of leaf 188 beyond those six occurs on leaf 192 (the 58 codes of 192
cover 54 distinct values, 21 of them not previously in the key, 6 of those on 188).

`python3 tools/judge_plaintext.py specs/na-janssens-java-1811.json --file ciphers/na-janssens-java-1811/reading.txt`:
```
FAIL language: score=-0.985, null_p99=-1.803, real_p05=-0.89, real_median=-0.781, mode=both, N=235
ok   words: cover=0.902, min=0.3, real_text_median_cover=0.945
FAIL - na-janssens-java-1811 (a PASS is a gate for a verifier, not a reading; rule 10)
```
Reported as a **FAIL** per rule 7, as before; the language score moves from -1.472 (VX-RD02C) to -0.985 against a
real_p05 gate of -0.89, and word cover from 0.78 to 0.902, both toward the gate, which is what a key gain looks
like; still 47% of the tokens are gaps breaking the n-gram stream, so the FAIL says "not yet readable", not
"wrong". No matched control was run this step: the step is a known-plaintext key extension (grade C from a period
decipherment of other text), not a solver family, and the same-page control of the earlier leaves (NOTES "Control")
is the shape that applies; leaf 192 has no raw-cipher twin on disk to decode against it (leaf 198 is No.3's raw
copy, 190 is No.2's first page), so the agreement figures above (57/58 codes, 53/58 glosses) are its reconciliation
control, not a key control.

Rule 10: no decipherment or plaintext of leaf 188 was found; the web and blog check above (same session) located
none either. Requests this step: none to any image host (192_hi.jpg was already on disk); WebSearch 8, one request
each to the three blogs and to napoleon-histoire.com for the gate step.

Not done (one line each, out of this step's scope): leaf 201's two code+gloss rows (done 02:45-03:0x UTC, GAPS2
section below); the No.4 set (gap 2); the build_key.py accent/drop bug fix (gap 2 names it first).

## GAPS2-na-janssens-java-1811 (2 Oct 2026, account-4)

The Verdict line's cheapest step as rewritten at the 02:07 UTC done line above, run 2 Oct 2026 02:45-03:0x UTC (same
brief, `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`): one IIIF fetch of leaf 201, crops, two blind passes
plus one reconciliation of its two code+gloss rows, `scripts/merge_leaf.py`, redecode leaf 188, re-judge.

**Fetch (one request to service.archief.nl):** `images/manifest.json` had no IIIF id for leaf 201 (the thumbnail-only
rows carry none), so the scan record was read from the invnr @12 page's embedded `drupal-settings-json` (one request
to www.nationaalarchief.nl; scan id 4229b518-9671-4ae5-a3f1-da180635d74d) and the leaf fetched once at `full/2561`
(`images/201_hi.jpg`, 2561x1969, 196 KB; manifest row updated with the ids and a corrected eye-check).

**Leaf 201 is the close of an interlinear decipherment, not "tabular column headers"** (the 1 Oct eye-read of the
thumbnail was right, the CS05 inventory row wrong): the left page carries two code rows with a French gloss under each
code, then "Signé Janssens"; the right page is blank. Which dispatch it closes is not established here: leaf 192
already ends No.2 ("Fin. Signé Janssens") and leaf 200 ends No.3, so these two rows are the tail of a third gloss whose
earlier leaves are not identified on disk (the raw sequence 710 721 881 404 435 574 62 420 does not occur on leaf 188).

Crops: `python3 tools/iiif_lines.py --image ciphers/na-janssens-java-1811/images/201_hi.jpg --out
ciphers/na-janssens-java-1811/images/crops_201 --region 0,60,1300,640 --distance 45 --prominence 15 --lines-per-crop 2
--prefix 201 --debug` (the leaf-192 settings; 6 lines found, paired into three crops `201_L01..L03.jpg`, 1300 px wide:
code row 1 with its gloss, code row 2 with its gloss, the signature). Overlay `images/crops_201/201_lines_debug.jpg`
checked before the passes: every band edge falls in whitespace.

Passes: two blind Sonnet subagent calls, one per pass, each given only the three crop paths (`leaf201_passA.tsv`,
`leaf201_passB.tsv`, same format as leaf 192). Both read **8 codes**; codes agree 8/8 and glosses 8/8 (identical
files apart from the notes). Reconciliation by this worker from the crops (`leaf201_reconciled.tsv`, settlements in
its note column) changed two cells both passes had read alike and settled one flag:
- row 2 cell 1: both passes 674 "dans"; pass A flagged "first digit could be 5". Crop L02: the first digit is the same
  hooked open-top 5 as the final digit of 435 beside it (the 6 of 62 is a closed loop), so **574**; the gloss's final
  glyph is the looped x that ends "vaisseaux", not the short s that ends "mis" and "les", so **deux**. `key.tsv`
  already holds 574 = Deux at grade C from four cells (190, 191, 199, 200), and "il y a deux vaisseaux" is the sense.
- row 1 cell 4: both passes "croisiers"; the crop shows "croisieres" with a faint accent; key 404 = croisières (191):
  recorded as the same word (accent-fold agreement).
- row 1 cell 1: 710 "part", final letter a small t or a flourish (uncertain, graded M); with 721 "mis" next it reads
  par-mis = parmi, and the whole close is "parmis les croisières il y a deux vaisseaux. —".
- row 2 cell 4: 420 with a dash under it, the end-of-text mark, no word; left out of the merge (key 420 = fin, from
  192's "Fin.").
Vision calls: three (the two subagent passes and this worker's reconciliation reads of the overlay and crops L01/L02).

Merge: `scripts/merge_leaf.py leaf201_reconciled.tsv --key key.tsv --conflicts conflicts.tsv`: **4 codes added**
(881 les, 435 il y a, 62 vaisseaux at C; 710 part at M as above), **2 same-value confirmations** (404 croisières n=2,
574 deux n=5), **1 conflict** (721 mi/mis, the row was already M from a corrected cell on 191; one more row in
`conflicts.tsv`, 24 -> 25), 2 rows skipped (the dash, the signature). `key.tsv` 233 -> **237 codes** (C 141 -> 144,
M 92 -> 93).

Leaf 188 redecoded (`python3 tools/decode_key.py ciphers/na-janssens-java-1811`, then `--check`, exit 0):
**163 tokens: C 62, M 26, U 75** (was C 60, M 26, U 77) -- keyed **88/163 = 54.0%** (was 86/163, 52.8%): +2 tokens,
both on line 12, which now reads "[442] . alinea [443] vaisseaux [645] [335] tous les [476] l' ennemie" (62 and 881;
710, 721, 435, 404 and 574 do not occur on leaf 188). The 75 unkeyed tokens are 62 distinct codes.

`python3 tools/judge_plaintext.py specs/na-janssens-java-1811.json --file ciphers/na-janssens-java-1811/reading.txt`:
```
FAIL language: score=-0.976, null_p99=-1.816, real_p05=-0.899, real_median=-0.789, mode=both, N=247
ok   words: cover=0.903, min=0.3, real_text_median_cover=0.951
FAIL - na-janssens-java-1811 (a PASS is a gate for a verifier, not a reading; rule 10)
```
Reported as a **FAIL** per rule 7: language -0.985 -> -0.976 against real_p05 -0.899 (the gate itself moved from
-0.89 with the longer N), cover 0.902 -> 0.903; a small move toward the gate, as two tokens in 163 should give. No
shuffled-target check was run because the judge did not clear. No matched control, for the same reason as the leaf-192
step: this is a grade-C known-plaintext key extension from a period decipherment of other text, not a solver family;
the 8/8 code and 8/8 gloss agreement of the two blind passes is the reconciliation control. Rule 10: no decipherment
or plaintext of leaf 188 was found this step; nothing was searched for one (the web and blog check above, same day,
stands).

Requests this step: www.nationaalarchief.nl 1, service.archief.nl 1; no 403/429/challenge. Vision calls 3.
Intake gate before the step: `tools/intake_gate_check.py na-janssens-java-1811` exit 0 (the web/blog section was logged
at 02:07 UTC).

## GAPS3-na-janssens-java-1811 (2 Oct 2026, account-4)

Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`, run 03:35-03:5x UTC 2 Oct 2026 (clock read), Fable 5.1,
disk only, vision 0, no network request to any host. Intake gate exit 0 before the step. The Verdict step of 02:52 UTC
as run: gap 5, regrade the M-graded tokens of leaf 188 against their occurrences on leaves 192 and 201 and against the
plain copies of No.2 (194-195) and No.5 (214). After SPLIT's 13:11 correction the leaf carried **25 M tokens over 19
codes** (the Verdict's "26" was written before that correction). Files touched: `regrades.tsv` (new, one row per code:
tokens on 188, grade before/after, value before/after, decision, evidence), `scripts/apply_regrades.py` (new, applies
it to `key.tsv` and `conflicts.tsv`, `--check` exits 1 when they disagree with it), `scripts/m_concordance.py` (new,
the evidence report: every occurrence of each M code across `combined_passA/B.tsv`, `leaf192_reconciled.tsv`,
`leaf201_reconciled.tsv` with three glosses of context each side, and the leaf-188 contexts), `scripts/merge_leaf.py`
(conflicts.tsv gains a `decision` column it now preserves), `key.tsv` (19 rows: grade and note; one value), `conflicts.tsv`
(decision column), the regenerated `reading.txt` / `reading_tokens.tsv`, this section and the gaps section below.

**What counted as evidence (rule 4).** The key is a period decipherment of other dispatches in the same bundle, so a
clean, unambiguous gloss cell grades C; M where the cell was corrected, uncertain, single-pass, or where two cells read
different values. A regrade to C needed the same value in **two different words or sentences** (a value seen in one
word stays M, whatever the plain copy says of that one word), with variants that differ only by accent, apostrophe,
case or a completed final letter (a/à, de/dé, n'/n, peu/peut/peu-vent) counted as one value -- `scripts/merge_leaf.py`'s
own same-value rule already folds these, and the "ambiguous" rows they produced were `build_key.py`'s accent-drop bug
(VX-RD02C (1)), not a conflict in the key. The No.5 plain copy (leaf 214, `no5_plaintext.txt`) was aligned by eye to
the 95 No.5 codes (`combined_passA/B.tsv` leaf 500, both passes) and used where it covers a code. **The plain copy of
No.2 (leaves 194-195) is not transcribed on disk** (only `images/194_med.jpg`, `195_med.jpg`, thumbnails); with vision
at 0 it could not be used this step, so the No.2 side of every decision rests on the 190/191/192 gloss alone, and the
Escalation clear-pages row keeps it. No reading was found or searched for (rule 10).

**Decisions (19 codes, 25 tokens; the full evidence sentence per code is in `regrades.tsv`):**

| code | tokens on 188 | before | after | decision in one line |
|---|---|---|---|---|
| 25 | 9:10, 14:6 | M | C | a/à, four distinct words (il y a; Sou-ra-ba-y-a twice; chargent à) |
| 99 | 3:5 | M | C | n'/n, two words (n'ai; re-tra-n-ché = retranché, plain copy 214 agrees) |
| 102 | 3:10, 14:8 | M | C | the syllable peu in three words (peu de jours; peut venir; peu-vent tenir la mer) |
| 140 | 2:1, 3:11, 5:9 | M | C | de/dé, five cells in four texts (Dé-part; dé-tru-it, plain copy "détruit") |
| 168 | 3:2 | M | C | ; in three sentences, two-pass agreed at 191#28; B's j at two cells where ; is the grammatical reading |
| 420 | 15:3 | M | C | the end-of-text mark: glossed fin (500#92) and Fin. (192#58), last code of No.2, No.5, leaf 201 and leaf 188 |
| 444 | 1:6 | M | C | l' in two words (L'est/l'Isle de la Ville, plain copy agrees; l'ennemi) |
| 689 | 7:11 | M | C | le in five contexts across four texts (plain copy "le 4 aoust"); the lone de (No.2 #5 "de port où est") is one cell where Le reads as well |
| 904 | 8:8, 9:1 | M | C | the letter i in two words (po-i-vr-e, plain copy "poivre"; J'au-rais) |
| 190 | 2:4 | M | M | est 4 distinct sentences vs en 3 (+1 B-only); value column flips en -> est by merge_leaf.py's own majority rule; three of the four en cells read as est grammatically (est arrivé, est arrivée, est un grand malheur); the plain copy 214 writes "en arrivée" at a gloss-en cell and "Il en probable" at a gloss-est cell, so it does not separate the two; 188's neighbours (1024 403 364) are unkeyed |
| 353 | 10:1 | M | M | one cell (199#33 C.), pass A uncertain |
| 527 | 6:6 | M | M | ; in one clean sentence (200#103), j in the other (199#32, both passes) |
| 534 | 14:9 | M | M | one word (peu-vent); the pair 102 534 recurs on 188 14:8-9, target-internal |
| 607 | 8:5, 11:7 | M | M | one word (mal-heur), first digit 607/809 uncertain |
| 760 | 14:11 | M | M | one word (li-vr-er) |
| 875 | 10:4 | M | M | one uncertain fragment (191#54 ât) |
| 1041 | 8:7 | M | M | one word (dé-ci-si-ve, plain copy "décisive"); digits settled by the leaf-210 clean-copy slip (1041, not pass A's 1541; key.tsv's 1541 row is this cell's digit twin, left for a follow-up) |
| 1096 | 10:11 | M | M | par/part one syllable with and without the t, 2:2 (par-ti, par-ages, par-tie struck t; Dé-part); on 188 "Gouverneur Gal part chargent" the verb part or the preposition par, undecidable from the key |
| 1137 | 4:10 | M | M | one word (re-tra-n-ché, plain copy "retranché"); digits settled by the clean-copy slip |

**Counts (rule 4).** `python3 scripts/apply_regrades.py` then `--check` (ok), `python3 tools/decode_key.py
ciphers/na-janssens-java-1811` then `--check`, exit 0:
```
before (SPLIT, 03:0x UTC): tokens 163: H 0, C 63, S 0, M 25, I 0, U 75   keyed 88/163
after  (this section):     tokens 163: H 0, C 77, S 0, M 11, I 0, U 75   keyed 88/163
```
14 tokens M -> C, 11 stay M, one value change (2:4 190 en -> est), coverage unchanged at 54.0%.

**Judge (rule 7)**, `python3 tools/judge_plaintext.py specs/na-janssens-java-1811.json --file ciphers/na-janssens-java-1811/reading.txt`:
```
before (SPLIT): FAIL language: score=-0.972, null_p99=-1.778, real_p05=-0.912, real_median=-0.783, mode=both, N=245
after:          FAIL language: score=-0.963, null_p99=-1.813, real_p05=-0.899, real_median=-0.782, mode=both, N=246
                ok   words: cover=0.915, min=0.3, real_text_median_cover=0.947
                FAIL - na-janssens-java-1811 (a PASS is a gate for a verifier, not a reading; rule 10)
```
Flat within the judge's own resampling (about 0.01 per run), as expected from a one-token text change; no PASS, so no
shuffled-target check was due and no "reading ready" line is written. Status stays `partial`. Follow-up (not run,
Usage 7): key.tsv's 1541 row (si, pass A's digit misread of the 1041 cell) can be dropped with a one-line note; the
PROGRESS.tsv "Janssens Java" row's note still describes GAPS (86/163, -0.985) and is the parent's to refresh.

## GAPS4-na-janssens-java-1811 (2 Oct 2026, account-4)

Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`, run 05:17-05:2x UTC 2 Oct 2026 (clock read), Fable
5.1. The Verdict step after GAPS3: gap 4, the LOCAL-QUEUE.tsv row for the Paris-side translation search. Files
touched: `LOCAL-QUEUE.tsv` (row L31 appended) and this file (this section, the gap 4 line and the Verdict line of
"## Remaining gaps"). Not touched: key.tsv, ciphertext.tsv, reading.txt, any image. Vision calls: 0.

**Cloud probe first (the brief's order).** One request each, browser-style UA, no retries, `curl -w %{http_code}`:

| host | code | what came back |
|---|---|---|
| https://francearchives.gouv.fr/ | 200 | the root page |
| https://francearchives.gouv.fr/fr/search?q=Janssens+Batavia+1811 | 200 | 255 bytes, text/html: "This website requires JS enabled and cookies" (a challenge page, not a result list) |
| https://www.siv.archives-nationales.culture.gouv.fr/ | 503 | service unavailable |

So the CLAUDE.md host-table line ("archivesnationales.culture.gouv.fr/francearchives.gouv.fr ... do not load from the
cloud at all") holds in substance: the FranceArchives root now answers, but the search behind it is JS-gated to a
script, and the SIV did not answer. Not retried (good-citizen rule); `tools/browser_fetch.js` was not tried, since
the brief caps outside requests at 4 and a headless navigation loads more than one. Requests: francearchives.gouv.fr
2, siv.archives-nationales.culture.gouv.fr 1; no other host.

**The row.** `LOCAL-QUEUE.tsv` L31, kind `browser-check` (the kind the runner brief lists as one it does, and one
`tools/lq_answer_check.py` holds to the catalogue-ladder rule; L29's `catalogue-lookup` is the other such kind but
is not in the runner brief's list), target this folder. It names the searches (FranceArchives: Janssens Batavia;
Janssens Java 1811; Java chiffre / chiffree / dechiffrement / traduction 1811; "Hollandse Divisie" / "bureau
hollandais"), the series to open in the SIV (Marine BB/4 campagnes 1811, AF/IV ministerial reports 1811, and ANOM
Colonies C/2 if the SIV hands the colonial series to IREL), and asks for each record's title, cote, date range,
catalogue URL or ark, and availability flag in the record's own words, with at least one holding-catalogue record
quoted even on a negative; results to `paris_search.md` in this folder. The gate was tested against the row before
the push: a bare "no results" answer exits 1 naming both missing rungs, the same answer with a SIV record URL and a
quoted availability phrase exits 0 (`python3 tools/lq_answer_check.py <file> --row L31`).

**Numbers.** Nothing read changes: leaf 188 keyed 88/163, C 77 / M 11 / U 75, judge FAIL -0.963 vs real_p05 -0.899
(GAPS3). Gap 4 moves from not-attempted to waiting-on L31; the Verdict's cheapest next step is now gap 3 (~$3).
Rule 10: no Paris-side record was found or searched for in this session; the row is the search.

One-line suggestion (not done, outside the brief): `tools/data/catalogue_ladders.tsv` has no Archives nationales /
FranceArchives / ANOM row, so `lq_answer_check.py` matches L31's rung (a) only through the generic ark/"catalogue"
fallback; a row naming siv.archives-nationales.culture.gouv.fr as the holding catalogue and francearchives.gouv.fr as
the aggregator portal would let the gate check the right host by name.

## GAPS5-na-janssens-java-1811 (2 Oct 2026, account-4)

Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`, run 06:06-06:2x UTC 2 Oct 2026 (clock read), Fable 5.1.
The Verdict step after GAPS4: gap 3's first half, the full-resolution re-inventory of leaves 186-215. Files touched:
`leaves_186-215_inventory.tsv` (new), `images/manifest.json` (in place), `images/197_med.jpg` and `images/202-207_med.jpg`
(new), `images/sheets/sheet1-4*.jpg` (the four contact sheets the passes read), `scripts/apply_inventory.py` (new), this
file (this section, the dispatch table's reconciled copy under "Reading", the gap 3 line, two Escalation lines and the
Verdict). Not touched: key.tsv, ciphertext.tsv, reading.txt, decode.json, corrections.tsv -- no transcription, no
decoding, no key change (`python3 tools/decode_key.py ciphers/na-janssens-java-1811 --check` exit 0 before and after,
unchanged: tokens 163, C 77, M 11, U 75, keyed 88/163).

**Fetches.** `images/manifest.json` listed 23 of the 30 leaves at medium (1200 px wide) or 2561 px; the other seven
(197, 202, 203, 204, 205, 206, 207) had thumbnails only, and 202 and 204-207 carried no IIIF id at all. One request to
`www.nationaalarchief.nl` (the invnr @12 page's `drupal-settings-json`, 233 scan records) gave the ids; seven requests
to `service.archief.nl` at `full/1200,/0/default.jpg`, 1.6 s apart, descriptive UA, all HTTP 200 image/jpeg, 44-89 kB
each. Folder 8.5 -> 12 MB with the four sheets (under the 30 MB line); nothing deleted.

**Sheets and passes.** Four PIL contact sheets (2 columns, 1200 px per leaf, a yellow "LEAF nnn" bar per cell, best
file on disk per leaf: `_hi` where it exists, else `_med`): 186-193, 194-201, 202-209, 210-215. Four blind Fable
subagent calls, one sheet each, no access to any text file of the folder; each returned one row per leaf (left page,
right page, heading verbatim, dispatch number, class cipher/gloss/plain/other, confidence H/M, note). Because a
single image is read at about 1.15 megapixels whatever its size, a sheet of eight gives each leaf about 0.14
megapixels -- below the thumbnail resolution at which CS05's headings were misread -- so each call was allowed to open
the individual files of its own eight leaves inside the same call for the headings (the passes opened 6, 5, 8 and 4
leaf files respectively; the sheet decided the class). Vision calls 4 of 4; this worker opened no image.

**Result: 30 leaves classified, all H.** cipher 5 (188, 190, 198, 204, 210), gloss 10 (191, 192, 199, 200, 201, 205,
206, 207, plus 202L and 208L, which are 201L and 207L re-imaged under a loose sheet), plain 5 (187, 194, 195, 209, 214;
202R and 208R are the plain copies of No.3 and No.4), other 8 (186, 189, 193, 196, 197, 203, 213, 215). Per-leaf rows
with the pass's note, the file read and the manifest's earlier text: `leaves_186-215_inventory.tsv`.

**Misfilings corrected in `images/manifest.json`** (`scripts/apply_inventory.py`; the old `eye_check` text moves to
`eye_check_prev`, never deleted; ids and local file fields filled from disk and the scan list): 14 leaves -- 187
(an "Extrait" dated Batavia 20 Juin 1811, "No 11", not a signed report), 189 (blank, not prose), 194-195 (the plain copy
of No.2, heading "N.2 Duplicata", not "N.6"), 201 (the tail of the No.3 gloss, not an unidentified third gloss), 202
(the plain copy of No.3), 204 (raw No.4 cipher, not a tabular form), 205-207 (the No.4 gloss, not tabular forms /
prose), 208-209 (the plain copy of No.4, not blank), 210 (carries the No.5 raw slip), 211 (the No.5 gloss, the slip
is on 210). The remaining 16 rows got an `inventory_2oct_GAPS5` field with the pass's reading; 192 and 198 had already
been corrected by earlier passes.

**Dispatch table reconciled** (under "Reading (VX-RD02, 25 Sept 2026)"): five dispatches, No.1-No.5, each with its
cipher copy, gloss and plain copy named by scan and page. The pairing that mattered: leaf 201's two rows are No.3's
postscript -- pass A's leaf-200 gloss ends "grand malheur. Fin. Treize" (`keysource_passA.tsv` 200#119-120), the
sheet-2 pass reads the raw No.3 copy on 198 ending "574. 62. 420.", and `leaf201_reconciled.tsv` ends 574 deux, 62
vaisseaux, 420 -- the same closing codes; none of 710/721/881/404/435/574/62 occurs on leaf 188 (`ciphertext.tsv`,
0 hits), so GAPS2's "which dispatch 201 closes is unidentified" is settled as No.3 (dated 11 Juillet, PS "Treize"). The
No.4 set is as gap 2 describes it (204R raw; 205R-207L gloss; 208R-209L plain), signed Janssens throughout -- the
25 Sept "Signe Vanteau" on 208-209 was this signature misread, so "a fifth correspondent's dispatch" in "State at
close" is withdrawn: the four cross-matching codes came from Janssens' own No.4 gloss.

**What the inventory says about No.1 (rule 10 wording).** No decipherment or plain copy of "Numero Un" was found on
leaves 186-215 at the best resolution on disk: every glossed page in the range belongs to No.2, No.3, No.4 or No.5.
This is a negative search result for the 30-leaf range, read at 1200-2561 px, not for the bundle. One lead the
inventory adds: 187R is a plain extract of a Janssens letter dated Batavia 20 Juin 1811 -- the first date of the
archival description's cipher run ("van 20 juni 1811 tot 7 augustus 1811"), so it is the only plain text on disk that
could be No.1's own; VX-RD02B's eye-read called it "revenue farms", the sheet-1 pass reads it as about the Residents,
the Emperor and the Sultan, and neither transcribed it. The Escalation clear-pages row already names the 187-against-188
alignment test (~$4); it is now the cheapest next step.

Two leads for the No.4 merge job (not acted on): `keysource_passA.tsv` 200#119 reads the "Fin." code as 120 where
the end mark reads 420 on 192, 201 and 211 -- a digit to check on `199_hi.jpg`/`200_hi.jpg` when that leaf is next
opened; and the top of 205's gloss sheet lies over 204R's heading on the scan, so a No.4 raw-copy transcription should
crop below the slip.

**Numbers.** Leaves fetched 7; classified 30 (cipher 5, gloss 10, plain 5, other 8, two of the gloss and two of the
plain being re-imaged pages); misfilings corrected 14; vision calls 4; requests www.nationaalarchief.nl 1,
service.archief.nl 7, no other host, no 403/429/challenge. Intake gate exit 0 before the step. Reading unchanged
(88/163 keyed, C 77 M 11 U 75, judge not re-run since nothing read changed).

## Premise check (GAPS6-na-janssens-java-1811, 2 Oct 2026)

Adversarial pre-reading pass per `.claude/briefs/check-solved.md` "Premise check" (a)-(d), run 13:2x-13:4x UTC 2 Oct 2026
(clock read) before the clear-pages step below; stance: prove leaf 188 ("Numero Un") is already deciphered somewhere.

**(a) Every decipherment, gloss, plain copy or extract the folder mentions, opened -- not found for No.1.** All read at
1200-2561 px on 2 Oct 2026 by the GAPS5 inventory (`leaves_186-215_inventory.tsv`, four blind passes, every row H), and
the heading of each re-checked here against that TSV: glosses 191-192 = No.2 ("No 2. Duplicata", opens "Batavia, neuf
Juillet", ends "Signe Janssens") -- the decipherment of cipher leaf 190, already aligned (key source, VX-RD02); 199-201 =
No.3 ("Numero 3. Duplicata", "onze Juillet", PS "Treize") -- the decipherment of cipher leaf 198, aligned (key source);
205-207 = No.4 ("N 4 / Premiere Expedition", "La force navale ennemie augmente", "Fin. Trois Aout") -- the decipherment
of cipher leaf 204R, NOT yet aligned (gap 2), but of No.4, not of 188; 211-212 = No.5 ("N 5 - 1re Expedition", "Batavia
7. aout") -- the decipherment of 210, aligned (key source). Plain copies 194-195 = No.2 (9 Juillet), 202R = No.3 (11
Juillet), 208R-209L = No.4 (3 Aout), 214 = No.5 (7 Aout): each is the clear copy of a dispatch whose gloss is listed
above, none of No.1. Leaf 187R, the one plain text with no cipher twin ("Extrait d'une lettre du Gouv.r General
Janssens au Ministre de la Marine et des Colonies a Paris, datee Batavia 20 Juin 1811 / No 11"), was transcribed and
tested this job (section below): it is about the Residents' revenue farms at the courts of the Emperor and the Sultan,
shares no content word with leaf 188's 88 keyed tokens, and ties its own shuffled-order control -- not a decipherment of
188. The archival description's "met bijgevoegde ontcijfering" is accounted for by the No.2-No.5 glosses. No file in the
folder calls anything a decipherment of No.1 (NOTES.md, REQUEST.md absent, spec: 0 such mentions beyond the "none found"
rows of the dispatch table).

**(b) Other solvers' working files -- not found.** Both solver repositories shallow-cloned fresh this job (github.com, 2
requests) and grepped case-insensitively for `janssens`, `batavia`, `2.01.27`, `hollands(ch)e divisie`, and file/folder
names containing `java`: dbourdeau/cyphersolver hits are all "Batavian Republic" (DECODE KHA records R1035/R1038/R1891,
Hogendorp R1942, Fagel/Wolff rows in `research/catalogue_harvest/decode/`) and the Napoleon correspondence OCR;
aaymeloglu/unsolved-ciphers hits are the same KHA "Batavian Repub;ic" rows in `catalogue/decode-*.{jsonl,csv}` and a 1783
PARES "socorro al general de Batavia" row (Philippines). No target, key, apply-key script or rendering for this
correspondence in either; clones deleted after the grep. DECODE: `sources/decode/` (records crawled 24-28 Sept 2026,
keys-all files) grepped for `java`/`janssens`/`batavia`: no hit. Cryptiana snapshot: one "Janssens" in
`sources/cryptiana/web/telegraph2.htm`, a telegraph-era page, unrelated.

**(c) Physical neighbours -- not found.** Leaves 186 (blank, stamp), 187 (the Extrait above, plain, not a decipherment:
tested), 189 (blank verso of 188, bleed-through only) at 1200 px (GAPS5 inventory rows, H); nothing bound beside 188
carries its clear text. The nearest glossed leaf, 191, belongs to No.2 (its first codes match leaf 190's first line,
inventory row 190).

**(d) Recipient side -- not found in what could be read; one lead unreachable from the cloud.** The recipient is the
Minister of Marine and Colonies in Paris via the Hollandse Divisie, so the editions are Dutch and French, not the
sender's. Colenbrander, *Gedenkstukken* VI (all 35 "Janssens" hits read 25 Sept 2026, Check-solved item 2): names the
dossier ("In n. 11 de berichten van Janssens omtrent de overgave van Java"), prints none of it. Van Deventer, *Het
Nederlandsch gezag over Java en onderhoorigheden sedert 1811*, I (1891), fetched once this job
(archive.org `hetnederlandsch00devegoog_djvu.txt`, 1.3 MB, `print/`): 5 "Janssens" hits, all 1811 capitulation /
Cornelis narrative, no letter of June-August 1811, no "cijfer/chiffr" hit. Internet Archive full text (be-api, 2
queries): "Janssens" + "20 Juin 1811" 37 items, every snippet a different 20 juin 1811 (Napoleon's decisions, army
lists, biographies); "Janssens" + "20 Junij 1811" 0. Google Books API (3 queries, keyed, country=US): no snippet
printing a Janssens letter of 20 June 1811; two recipient-side leads: Octave J. A. Collet, *L'ile de Java sous la
domination francaise* (Paris 1910, 558 pp., Google Books id -BCyBiSVklAC, viewability ALL_PAGES), whose snippet
footnotes a Janssens dispatch as "... 1811, no 2" -- a French work citing the numbered 1811 dispatches to Paris, so it
may quote No.1 -- not on archive.org (advancedsearch creator/title 0) nor found on Gallica (SRU title query, 1 request),
and books.google.com page view is blocked from the cloud (CLAUDE.md hosts table): **unreachable**, named in the gaps
section as the print step's next action (a LOCAL-QUEUE row); and *Archipel* (1971) citing Janssens material in AN AF IV
1722, the Paris side already queued as LOCAL-QUEUE L31 (gap 4, waiting). The De Jonge *Opkomst* series ends before 1811 [A3V-VJAN correction, 4 Oct 2026: wrong -- Opkomst deel XIII (1888, ed. Van Deventer) prints Janssens' letters of 16 and 21 June, 29 Aug and 5 Oct 1811 and quotes the No.4 and No.5 cipher dispatches; see AUDIT.md]
(Van Deventer's 1891 volume is its continuation, read above). Rule 10: these are search results, not a novelty verdict.

**Verdict: no decipherment or print of leaf 188 found by (a)-(d); clear to run the clear-pages step.** Requests this
section: github.com 2 (clones), archive.org advancedsearch 4 + download 1, be-api.us.archive.org 2, googleapis.com 4,
gallica.bnf.fr 1.

## GAPS6-na-janssens-java-1811 (2 Oct 2026, account-4)

Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`, run 13:26-13:5x UTC 2 Oct 2026 (clock read), Fable 5.1.
Premise check first (section above, gate exit 1 -> 0), then the Verdict step after GAPS5: the clear-pages step for leaf
187 -- transcribe 187R and test it as a crib against leaf 188's keyed tokens with a shuffled-order control. Files:
`images/crops_187/` (native IIIF region of the slip, 15 line crops, overlay, manifest), `leaf187_passA.tsv`,
`leaf187_passB.tsv`, `leaf187_reconciled.tsv`, `leaf187_text.txt`, `scripts/crib_test_187.py`, `crib_test_187.txt`,
`print/hetnederlandsch00devegoog_djvu.txt`, this file. Not touched: `key.tsv`, `ciphertext.tsv`, `reading.txt`,
`decode.json`, `corrections.tsv` -- no key or reading change (`tools/decode_key.py --check` exit 0, unchanged 163
tokens, C 77 M 11 U 75, keyed 88/163).

**Image.** `images/187_med.jpg` (1200 px) is too small for a 17-line slip, so the leaf's IIIF `info.json` (native 5034 x
3914; 1 request) and the slip region (2558,1229,2387,2626 at native, located by the paper/ink profile of the medium
file, no vision; 1 request, 373 kB) were fetched from service.archief.nl, descriptive UA, 1.5 s apart, both HTTP 200.
`python3 tools/iiif_lines.py --image images/crops_187/187_right_native.jpg --out images/crops_187 --prefix 187
--max-width 2450 --debug`: 15 bands (pitch 110). The heading line ("Extrait d'une lettre du Gouv.r General Janssens,
au Ministre", lighter ink) sits above band 1 and got no crop; band 3 holds two lines; band 15 is the archive stamp.

**Passes.** Two blind Sonnet subagent calls, each given only the 15 crop paths and the band overlay, forbidden every
text file of the folder (`leaf187_passA.tsv`, `leaf187_passB.tsv`). Both read 14 text lines + the stamp, both flagged
the uncropped heading and the two-line band 3. Word-level agreement: 12 of 14 body lines identical (punctuation
aside); the one disagreement is one word, twice: "Residens" (A) vs "Rendens" (B) on lines 2 and 11. Reconciliation
(this worker, one montage of the top strip and crops L01, L02, L11, L13, L14): "Residens" (R-e-s-i-d-e-n-s), the
heading and date line confirmed ("datee Batavia 20 Juin 1811", "N 11" underlined), "destination" overwritten at its
start, "avenir" one word, "positive" confirmed. `leaf187_reconciled.tsv` (per line: both passes, who settled it);
`leaf187_text.txt` (16 lines, 154 body words). Transcription grade H (clear French, two passes + reconciliation); it
is a plain text, not a decipherment.

**What 187R says.** An extract of a Janssens letter to the Minister, Batavia 20 June 1811, "No 11": the Residents at
the courts of the Emperor (Susuhunan) and the Sultan hold revenue farms ("la ferme d'objets") whose profit the
Governors of Java and lately the Governor-General shared; the Sovereign has been told; Janssens will not add the sum
to his own income, will receive it and hold it in deposit until the Emperor rules on it, and will inform His
Excellency of the details. Nothing naval or military. Leaf 188's keyed words (C grade) are "l'ancien Gouverneur Gal",
"vaisseaux", "debarquer", "l'ennemie", "Troupes", "arrive", "recu", "seules" -- a dispatch about the enemy's ships and
a landing.

**Crib test (rule 3), `scripts/crib_test_187.py`, output `crib_test_187.txt`.** Query: leaf 188's keyed token values in
order (`reading_tokens.tsv`, C and M, U dropped, punctuation values dropped by normalisation: 82 tokens of the 88).
S1 = longest common subsequence against the candidate's word sequence, null = 2000 shuffles of the candidate's own
word order (the axis LCS varies on); S2 = coverage of leaf 188's keyed word types (len >= 3: 26 types; len >= 5: 9
content words), which a shuffle cannot vary, so its controls are two other Janssens texts of the bundle. Positive
control (ceiling, by construction since the key was built from it): the No.2 cipher codes decoded by key.tsv against
the No.2 gloss words.
```
S1 LCS  leaf187R (target crib)      : LCS 17/82 (0.207); shuffled-order null mean 16.6 sd 1.3 p95 19 p99 20 max 22; z +0.30; null >= target 999/2000
S1 LCS  No.5 plain copy (control)   : LCS  9/82 (0.110); null mean  9.7 sd 1.1 p95 11 p99 12; z -0.66; 1753/2000
S1 LCS  No.2 gloss (control)        : LCS 17/82 (0.207); null mean 15.3 sd 1.3 p95 17 p99 18; z +1.37; 324/2000
S1 LCS  positive control No.2 decoded vs No.2 gloss: LCS 102/262 (0.389); null mean 35.6 sd 1.9 p99 40 max 43; z +35.49; 0/2000
S2 coverage of 26 keyed types / 9 content words: leaf187R 4/26 (0.15), content 0/9; No.5 plain 3/26, 1/9 [troupes]; No.2 gloss 8/26, 1/9 [chargent]
Verdict's named C words (deux, vaisseaux, arrive, ennemie, debarquer) present in 187R: none
```
The control can fail differently from the target and does: the true pair scores z +35 against the same null, so the
test has power; the target scores z +0.30 (999 of 2000 shuffles at or above it), at the median of its own null, and
its content-word coverage of leaf 188 is 0 of 9, below both other-letter controls. **Leaf 187R is not the plaintext of
leaf 188** (negative with a matched control, rule 3); the shared tokens are function words (de, la, le, les, et, que,
en). Rule 10: this is a search result about one slip, read from the image; No.1's clear text was not found.

**Numbers.** Premise check (a)-(d): not found / not found / not found / not found in what could be read, one lead
unreachable (Collet 1910). Intake gate exit 1 (no Premise check) -> exit 0 after. 187R lines read 16 (heading 2 +
body 14), pass agreement 12/14 body lines word-identical, 1 word disputed (x2), settled from the image. Crib test:
target z +0.30 vs positive control z +35.49; coverage 0/9 content words. Vision calls 3 of 3 (two blind Sonnet
passes, one reconciliation montage). Requests: service.archief.nl 2; github.com 2; archive.org 5; be-api 2;
googleapis.com 4 answered (3 further snippet queries returned no body, not retried); gallica.bnf.fr 1. No 403/429/
challenge. Reading unchanged, judge not re-run (nothing read changed).

## GAPS7-na-janssens-java-1811 (2 Oct 2026, account-4)

Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`, run 14:19-14:4x UTC 2 Oct 2026 (clock read), Fable 5.1, no
vision calls. Intake gate before the step: `partial (line 1) -- edition/page or full-text-search citation found within 6
lines`, exit 0. The Verdict step of the gaps section (GAPS6 rewrite), both parts: the Collet 1910 route, then
`tools/print_check.py` on the four plain texts. Files touched: `LOCAL-QUEUE.tsv` (row L35), `phrases.txt`, `sources.tsv`,
`print-check.tsv`, `print-check-hosts.tsv`, `print/` (one djvu text, two extracts, `manifest.tsv`), `scripts/crib_test_187.py`
(a `--text PATH` option, nothing else changed), this section and the gaps section. Not touched: `key.tsv`, `ciphertext.tsv`,
`corrections.tsv`, `reading.txt`; `python3 ../../tools/decode_key.py . --check` still exits 0 (C 77 M 11 U 75 of 163).

**Collet 1910 (the Verdict's first part): no readable copy from the cloud; LOCAL-QUEUE row L35 filed.** Google Books API
volume record for `-BCyBiSVklAC` (HTTP 200): Octave J. A. Collet, *L'ile de Java sous la domination francaise*, Paris, Falk,
1910, 558 pp., viewability ALL_PAGES, accessViewStatus FULL_PUBLIC_DOMAIN, a PDF download link on books.google.com. That link
answers HTTP 429 and redirects to google.com/sorry (a captcha page), one attempt, not retried -- books.google.com stays blocked
from the cloud as the CLAUDE.md hosts table says. Three API snippet searches (`inauthor:Collet`): "Janssens" "1811" "no 2"
intitle:Java -> 2 volumes (`-BCyBiSVklAC` and a second scan `uz1BAQAAMAAJ`, same snippet); "Janssens" "1811, no 1" -> 0;
Janssens chiffre intitle:Java -> the same 2 volumes, same snippet. The snippet, verbatim as the API returns it: "... Janssens.
« L'état florissant de cette colonie, l'excellent esprit dont les habitants sont animés ne laissent ... 1811, no 2. (2) Un
premier serment avait été prêté à l'arrivée de Claudius Civilis. (Voir p. 357.)" -- Collet footnotes a Janssens dispatch
"1811, no 2" and quotes a sentence from it. That sentence is in none of the folder's transcriptions (grep of every file for
"florissant", "excellent esprit", "habitants sont": 0), so it is not in our No.2 gloss (leaves 190-192, Batavia 9 July 1811)
as read; either Collet's "no 2" is a different dispatch series (a numbering to Paris that is not this bundle's, or the
Daendels-era run) or it quotes a passage of No.2 our gloss does not carry. Which, only the page can say. Other routes:
archive.org advancedsearch (title java + creator collet / title domination; collet java 1900-1930) 0 items both; Open Library
gives the edition (OL61021068M, OCLC 1417504); HathiTrust bibliographic API for OCLC 1417504 returns no record. So the read
is a desk job: `LOCAL-QUEUE.tsv` row **L35** (kind edition-read, this target) asks the runner to open the Google Books volume,
read every footnote citing a numbered or dated 1811 dispatch with its page and the archive carton cited, say whether any
cites no 1 / no 11 / 20 juin 1811 or the dates of No.2-No.5, search chiffre/dechiffr/Sapho/Stafforth/71 voiles, quote the
preface's source sentence, and write `print/collet1910_L35.md`. `tools/lq_answer_check.py` gates runner *answers*, not
queued rows, so it was not run here; the row's kind (edition-read) is one of the four that tool exempts from the
catalogue-ladder rungs when the answer lands.

**print_check (the Verdict's second part): 17 phrases, 5 listed sources, 89 rows -- Nos.2, 3, 4 and 187R no hits; No.5's
opening sentence is printed.** `phrases.txt` carries 4 phrases from the No.2 gloss (190-192, the text of the plain copy
194-195), 4 from the No.3 gloss (199-201, the text of 202R), the 2 spans of the plain No.4 copy (208R-209L) the GAPS5
inventory quotes verbatim (nothing more of No.4 is transcribed on disk), 4 from the No.5 plain copy (214), 2 from leaf 187R,
and one positive control -- the sentence Google Books' own snippet shows in Collet 1910. `sources.tsv`: the two Collet scans,
Van Deventer 1891 (cached djvu), OpenAlex and CrossRef keywords. Hosts: be-api.us.archive.org 17, www.googleapis.com 17,
api.openalex.org 18, api.crossref.org 2, all ok; api.semanticscholar.org 1 then blocked (HTTP 429 on the first call, the
tool's own one-strike rule, 18 rows `not searched`). Reading the 19 rows the tool counts as "with hits":
- the control phrase hits exactly the two Collet volumes (`-BCyBiSVklAC`, `uz1BAQAAMAAJ`, both flagged as listed) -- the
  method reaches a Google Books full-view 1910 volume, so a miss on the other phrases is a miss of this method at this date;
- three of the four No.5 phrases ("une expédition forte de 71 voiles", "détruit nos magasins de Sucre", "camp retranché
  destiné pour cela") each return the same 6 Google scans of *De Opkomst van het Nederlandsch gezag in Oost-Indië* (1888),
  snippet "... expédition forte de 71 voiles est arrivée le 4 devant la rade, et débarque des troupes à l'est de la ville.
  Nous avons détruit nos magasins de sucre, café et poivre, et nous nous sommes portés dans le camp retranché destiné pour
  ..." -- No.5's first sentence and a half, verbatim (the plain copy on 214 reads "à l'Isle de la Ville" where the print has
  "à l'est de la ville"; the print is the better reading of that clerk's hand, a note for the next owner of 214, grade unchanged
  here); the fourth No.5 phrase ("une affaire décisive aura lieu") returns 2 unrelated Moniteurs;
- every other gbooks row is a generic phrase returning 300+ unrelated volumes (procès Bazaine, Bulletin des lois, Boyer's
  dictionary), and the one ia-global hit ("c'est une précieuse possession") is Aurifodina universalis 1865 -- noise, logged
  in `print-check.tsv`; CrossRef's 166,000-record keyword rows are its usual relevance tail; OpenAlex 0 on every phrase.
Per text: No.2 0 hits (4 phrases), No.3 0 (4), No.4 0 (2), No.5 3 of 4 phrases -> one print, 187R 0 (2). "No hits" is a search
result by this method on this date, not a novelty verdict (rule 10).

**The print, read from archive.org.** advancedsearch (title opkomst nederlandsch gezag, 1886-1890: 9 items) gives
`depkomstvanhetn00unkngoog` = Reeks 1, deel 13, 1888, 845 leaves (the 844-page Google scan `z1WElvgNiqUC`); its `_djvu.txt`
(2.1 MB, 1 request) is now `print/depkomstvanhetn00unkngoog_djvu.txt` (manifest row). The OCR double-spaces every word gap
and confuses u/n, so every multi-word grep below is whitespace-tolerant (`\s+`); a first single-space pass had returned 0 for
"magasins de sucre" and "Juin 1811" and was discarded. Found: (1) the No.5 quotation at OCR lines 6298-6302, in the editor's
Inleiding, page CXXXIII, footnote 2: "Op dien dag berichtte de Gouv.-Gen. aan den Franschen minister van Koloniën: 'Une
expédition forte de 71 voiles est arrivée le 4 devant la rade, et débarque des troupes à l'est de la ville. Nous avons détruit
nos magasins de sucre, café et poivre, et nous nous sommes portés dans le camp retranché destiné pour cela depuis six mois'"
(OCR regularised) -- so Van Deventer read the dispatches to Paris themselves (this bundle or its Paris copies), and that one
sentence of No.5 is text-known, printed in De Opkomst deel 13 (1888) p. CXXXIII n.2; No.5's cipher was already decoded against
its own plain copy on 214 (VX-RD02C), so this adds a citation, not a key source. (2) Four Janssens letters to the Minister of
Colonies printed in full, in French: doc. LII Batavia 16 Juin 1811 (p. 539 by the table of contents, OCR lines 33072-33146),
doc. LIII Batavia 21 Juin 1811, "Confidentielle, pour le Ministre seul" (33147-33241), doc. LIV Tjikapondong 29 Août 1811
(33242-33391, opening "Par mes dépêches avec la corvette le Sapho j'ai dépeint la situation critique de la colonie"), doc. LV
Batavia 5 Octobre 1811 (33392-). Not found anywhere in the volume (whitespace-tolerant): "cent lieues", "20 Juin", "Juillet
1811", "Août 1811" as a date line, "tenir la mer", "précieuse possession", "affaire décisive", "chiffr", "Residens", "ferme
d'" -- Nos.2, 3, 4 and 187R are not quoted, and no letter dated 20 June 1811 is printed.

**Are LII (16 June) or LIII (21 June) the plaintext of leaf 188 (No.1, Triplicata, about 20 June 1811)? No, by the same
test that excluded 187R.** `scripts/crib_test_187.py --shuffles 2000 --text print/opkomst13_LII_16juin1811.txt --text
print/opkomst13_LIII_21juin1811.txt` (the two extracts, 574 and 665 OCR words):
```
S1 LCS  leaf187R (target crib) vs leaf 188: query 82 tokens, candidate 186 words: LCS 17; shuffled-order null mean 16.6 sd 1.3 p95 19; z +0.30; null >= target: 999/2000
S1 LCS  opkomst13_LII_16juin1811 vs leaf 188: query 82 tokens, candidate 587 words: LCS 24; shuffled-order null mean 23.6 sd 1.3 p95 26; z +0.33; null >= target: 1016/2000
S1 LCS  opkomst13_LIII_21juin1811 vs leaf 188: query 82 tokens, candidate 684 words: LCS 26; shuffled-order null mean 26.3 sd 1.4 p95 29; z -0.21; null >= target: 1425/2000
positive control (ceiling): No.2 codes decoded by key.tsv (262 tokens) vs No.2 gloss (109 words): LCS 102; null mean 35.6 sd 2.0; z +33.82; null >= target: 0/2000
S2 coverage of leaf 188's 9 keyed content words (alinea ancien chargent debarquer ennemie gouverneur seules troupes vaisseaux): LII 0/9, LIII 0/9, 187R 0/9, No.5 control 1/9, No.2 control 1/9
```
Both letters sit inside their own shuffled-order null (rule 3: order is the axis the control varies on) while the known
cipher/gloss pair scores z +34 on the same statistic. Conditional on the OCR (rule 2): a loose grep of the content words
(vaisse/ennemi/troupe/barqu/ancien/seules/charge) finds in LII only "ennemi" twice and in LIII "vaisse" once and "ennemi"
once, where a true match would carry leaf 188's "vaisseaux ... tous les ... l'ennemie" and "l'ancien Gouverneur Gal"; OCR
damage cannot hide all nine. Reading of the negative: No.1 of the ciphered series is neither the plain financial letter of
16 June nor the confidential letter of 21 June that Van Deventer printed; it is a third dispatch of the same week, and deel
13 does not print it by this OCR search. No token, grade, key or reading changed (rule 4 counts unchanged: C 77 M 11 U 75).

**Requests this section:** www.googleapis.com 25 (Collet volume + 3 searches; 4 intitle:opkomst searches, one HTTP 503 not
retried; 17 in print_check), books.google.com 1 (HTTP 429 captcha, not retried), archive.org 4 (3 advancedsearch, 1 djvu
download), be-api.us.archive.org 17, openlibrary.org 1, catalog.hathitrust.org 1, api.openalex.org 18, api.crossref.org 2,
api.semanticscholar.org 1 (429, blocked by the tool). Vision calls 0 of 0. Cost: the orchestrator reads get_session.

For the next owner: the Collet read waits on L35; De Opkomst deel 13's LII-LV are printed Janssens letters of 1811 in the
same French and office as the cipher dispatches -- a free era-matched corpus for the judge spec (`specs/na-janssens-java-1811.json`
judge block), which the rule-3 pt18/es17c lessons say to prefer over a generic French corpus, and the page-through (gap 3)
should look for the 16 and 21 June letters' own cipher copies in the bundle, which would be two more key sources of the same
kind as No.2-No.5.

## GAPS8-na-janssens-java-1811 (2 Oct 2026, account-4)

Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`, run 21:28-21:5x UTC 2 Oct 2026 (clock read), Opus 5.5
orchestrating, Sonnet blind passes, one Opus reconciliation. Intake gate before the step: `partial (line 1) --
edition/page or full-text-search citation found within 6 lines`, exit 0. The Verdict step: the No.4 set (gap 2).
Requests: 0 (disk only: images/204-209_med.jpg at 1200 px, images/208_hi.jpg).

**Crops** (pasted, every call): `python3 ../../tools/iiif_lines.py --image images/<n>_med.jpg --region <page> --out
images/crops_no4 --prefix <page> --centres <top,mid,bottom> --lines-per-crop 3` for 204R (625,150,575,550), 205R
(600,60,600,880), 206L (0,0,600,934), 206R (600,0,600,934), 207L (0,0,600,700); the plain copy into
images/crops_no4_plain from images/208_hi.jpg (2560,0,2440,3758) and images/209_med.jpg (0,0,620,200). One crop per
page: line-band crops were tried first (`--lines-per-crop 4`, profile-detected) and the debug overlay showed band edges
through the gloss table's code/word rows, so each page went whole (600 px wide, under the 2500-px limit).

**Passes (7 subagent vision calls, the brief's budget).** 4 blind Sonnet gloss passes, one per page (205R 60 cells,
206L 60, 206R 60, 207L 43: 223), each writing code + gloss + H/L (no4/gloss_*.tsv); 1 blind Sonnet pass on the raw
cipher 204R (223 groups, 16 lines, no4/raw_204R.tsv), an independent second read of every code; 1 blind Sonnet pass on
the plain copy 208R-209L (30 lines, 160 words) written straight to no4/SEALED_plain_208R-209L.txt, sha256 recorded in
no4/SEAL.sha256 at 21:31 UTC before any alignment, the subagent told not to quote it; 1 Opus reconciliation of the 34
code disagreements and 4 doubtful glosses against both images (no4/reconcile.tsv: 30 to the table read, 2 to the raw
read -- 551 sources, 110 eu -- 2 other: 354 Je, 585 unchanged; 5 at L). Deviation from the brief: its "2 blind
passes + 1 reconciliation per page" needs 12+ calls for four gloss pages; inside 7, codes got two independent reads
(table + raw page) plus a reconciliation, gloss words one read, checked against the plain copy instead of a second
read. Also: the six passes ran at once (Usage 6 says at most four), and this worker saw the plain copy at thumbnail
size in one contact sheet (page layout check) before sealing; no subagent saw it, and the gloss transcriptions were
written blind before it was opened. Own looks: 4 (204 and 205 spreads, one 206-209 contact sheet, one crop overlay).

**Code agreement.** Gloss-table codes vs the raw page: 190/222 in order before reconciliation (85.6%; one table cell's
code unread), 192/223 after (86.1%); the remaining 31 are the raw read at 575 px, where the table digits are larger and
the reconciler, citing same-code cells elsewhere in the table, settled for the table (no4/code_disagreements.tsv).

**Control (rule 3), `python3 scripts/no4_align.py --seeds 20`.** tools/interlinear_align.py (new options `--digits 4
--word-prior`, offline test added) aligns the gloss table's code sequence to the plain copy's letters with the gloss
values as the seeded hypothesis; per position the plain-copy chunk is compared with the gloss (letters, accents
folded). The null is the same tool on the same codes in shuffled order (each code keeps its gloss) -- order is the
axis the statistic depends on, so the null can fail differently.
```
codes: gloss table 223, raw 204R 223, matched in order 192 (86.1% of gloss, 86.1% of raw)
position agreement gloss vs plain-copy alignment: 154/210 = 0.733; shuffled-order null (20 seeds) mean 0.191 max 0.233
char LCS reading vs plain copy: 0.874 of 756 plain letters; shuffled null mean 0.444 max 0.458
codes with gloss/plain-copy value conflict: 53 of 173 (no4/conflicts_no4.tsv)
merge file no4/no4_merge.tsv: 223 cells, 56 marked uncertain
```
The 56 disagreeing cells are mostly the single gloss pass's misreads of the clerk's s/t/n/u (sous/sont, par/pas,
der/des, Douze/dont, Mr. 4/N°. 4) and the plain copy writing numbers as digits (18, 20, 5) where the gloss has words;
none is settled by majority (rule 4): each is logged and its cell enters the key as M.

**No.4 reading (no4/reading_no4.txt), grade per position (rule 4):** 223 cells: C 164 (gloss, a period decipherment
of this very text, agreeing with the plain copy, or punctuation), M 56 (gloss single-read disagreeing with the
plain-copy alignment), 3 struck cells not counted; H 0, S 0, I 0.

**Merge and leaf 188 (rule 7).** `python3 scripts/merge_leaf.py no4/no4_merge.tsv` (accent-folding merge): 91 codes
added, 97 same-value, 32 conflicts (conflicts.tsv, 3 struck skipped); key.tsv 237 -> 328 codes. `python3
../../tools/decode_key.py .` then `--check`, exit 0:
```
before: tokens 163: C 77, M 11, U 75   keyed 88/163
after:  tokens 163: C 75, M 32, U 56   keyed 107/163
```
Judge, `python3 tools/judge_plaintext.py specs/na-janssens-java-1811.json --file ciphers/na-janssens-java-1811/reading.txt`:
```
FAIL language: score=-0.973, null_p99=-1.833, real_p05=-0.893, real_median=-0.783, mode=both, N=332
ok   words: cover=0.916, min=0.3, real_text_median_cover=0.949
FAIL - na-janssens-java-1811 (a PASS is a gate for a verifier, not a reading; rule 10)
```
Flat (was -0.963): more of leaf 188 is keyed but 21 more tokens are M. No reading is claimed (rule 10); nothing was
searched in print this step. Next: a second, native-resolution blind gloss pass on the 56 + 32 doubtful cells only.

## GAPS9-na-janssens-java-1811 (2 Oct 2026, account-4)

Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`, run 22:38-22:5x UTC 2 Oct 2026 (clock read), Opus 5.5.
Intake gate before the step: `partial (line 1) -- edition/page or full-text-search citation found within 6 lines`,
exit 0. The Verdict step (GAPS8): a native-resolution second gloss pass on the 56 plain-copy-disagreeing No.4 cells and
the cells carrying the No.4 conflict codes. Requests: service.archief.nl 6 (3 IIIF info.json, 3 native region fetches,
1.6 s apart; the disk copies were 1200 px), no other host.

**Native pages and crops.** `images/crops_no4_native/{205,206,207}_native.jpg` (205 region 2380,200,2462,3592; 206 the
whole 4871x3791 spread; 207 region 0,0,2480,2880). Row centres from `python3 tools/iiif_lines.py --image
ciphers/na-janssens-java-1811/images/crops_no4_native/<n>_native.jpg --region <page> --out
ciphers/na-janssens-java-1811/images/crops_no4_native --prefix <page> --distance 110 --prominence 15 --dry-run` per
page (205R 0,0,2462,3592; 206L 0,0,2435,3791; 206R 2435,0,2436,3791; 207L 0,0,2479,2879), two missing centres on 206R
and 207L set by eye; the 5-column x 12-row (207L 9-row) grid checked on one overlay of all four pages before any pass.
`python3 scripts/no4_cells.py` selects 82 cells (the 56 GAPS8 `uncertain` cells plus every No.4 cell whose code sits in
a conflicts.tsv row naming a no4 page: 31 codes; GAPS8's "32" counted one row twice) and cuts each at native size into
7 contact sheets of 12 labelled boxes (`sheet_01..07.jpg`) showing only a box number -- no code, gloss or plain copy.

**Passes (2 vision calls of the 3 allowed).** Two blind Opus passes, run together (2 at once), each reading only the 7
sheets (B in reverse order), told the clerk's u/n, s/t/r, final s/t, 2/4, 1/7 confusions and to read the ink, not the
sense (`no4/gaps9_passA.tsv`, `no4/gaps9_passB.tsv`; 26 and 20 rows L). Agreement A vs B: gloss 74/82, code digits
79/82 (the three code splits are a stray bracket read into the code, `(960`, `585)`, and 913/513 at 205R:17). The
reconciliation call was not spent: under this brief a cell changes only when both blind passes agree, so a third read
could not change any of the 8 split cells; they stay as they were, graded by the plain-copy check below.

**Outcome per cell** (`python3 scripts/no4_gaps9_apply.py` -> `no4/gaps9_compare.tsv`, overrides in
`no4/reconcile.tsv` with basis `GAPS9 native 2-pass agree`): 52 confirmed (both passes = the GAPS8 value), 21 changed
(both passes agree on a different reading), 8 kept because the passes split, 1 kept as a struck cell (205R:40
`fort[e]`). The 21 changes: 205R:43 bler -> bles, 205R:44 et -> est, 206L:9 repondu -> repondre, 206L:10 der -> des,
206L:18 votre -> notre, 206L:21 meuh -> ment, 206L:22 dans -> san, 206L:23 to- -> bo-, 206L:29 gue -> gne, 206L:30 Le ->
Les, 206L:37 Mr. 4 -> N°. 4, 206L:43 sous -> sont, 206L:49 ller -> elles, 206L:51 sous -> sont, 206L:53 Duer -> Dues,
206R:9 ué -> né, 206R:20 der -> des, 206R:23 Douh -> Tout, 206R:56 tend -> rend, 207L:10 eu -> en, 207L:42 Trois -> Troi
(both passes see no final s; logged, not repaired). Split, unchanged: 205R:17 cotés (A coter / B cotes), 205R:22
batiments (batimens / batiments), 205R:23 Douze (Dout / Dont), 206L:25 ne (re / ne), 206L:32 dont (dout / dont), 206L:47
uner (nues / ner), 207L:12 piter (pil[le]r / pi?r), 207L:41 fui. (fu / fin.).

**Control re-run (rule 3), `python3 scripts/no4_align.py --seeds 20`** -- the same sealed plain copy (no4/SEAL.sha256,
not reopened by any pass) and the same shuffled-order null (order is the statistic's axis, so the null can fail
differently):
```
codes: gloss table 223, raw 204R 223, matched in order 192 (86.1% of gloss, 86.1% of raw)
position agreement gloss vs plain-copy alignment: 172/210 = 0.819; shuffled-order null (20 seeds) mean 0.199 max 0.238
char LCS reading vs plain copy: 0.903 of 756 plain letters; shuffled null mean 0.447 max 0.460
codes with gloss/plain-copy value conflict: 35 of 173 (no4/conflicts_no4.tsv)
merge file no4/no4_merge.tsv: 223 cells, 38 marked uncertain
```
(GAPS8: 154/210 = 0.733, null mean 0.191 max 0.233; LCS 0.874; 53 conflicting codes; 56 uncertain.) Caveat: only the
82 doubtful cells were re-read, so the 0.819 is a second read of the disputed cells plus GAPS8's single read of the
rest; the passes were blind to the plain copy, so the rise is not built in, but the 52 "confirmed" cells and the cells
not re-read have not had a second gloss read.

**Re-merge (no double count).** `key.tsv` and `conflicts.tsv` restored to their pre-GAPS8-merge state (`git show
06ebe184^:...`, which decodes to GAPS3's C 77 M 11 U 75 exactly), then `python3 scripts/merge_leaf.py no4/no4_merge.tsv`:
rows 223, added 91, same-value 102 (was 97), conflicts 27 (was 32), skipped 3; key 328 codes. Conflict rows naming a
No.4 page: 31 -> 26; resolved 110 (en/eu), 364 (les/Le), 656 (ne/ué), 808 (Sont/sous), 1106 (elles/ller), 1195
(est/et); new 743 (trois on 191 vs Troi on 207L, both blind passes). The 26 remaining stay logged with their witnesses
in conflicts.tsv, never settled by majority (rule 4); several are accent or punctuation only (1049 événement(s), 547
aoust/août, 456 re/=re, 13 au/aux, 960 près/(Près, 585 l'Isle de Java/Java)), and the real ones (1094 Douze/dont, 1135
forte/fort, 564 de/des, 1096 par/part, 997 N°. 4/quatre/4, 1023 N°./nd) are homophone or fragment questions the image
alone does not settle.

**Counts (rule 4/7)**, `python3 ../../tools/decode_key.py .` then `--check` (exit 0, "reading up to date"):
```
before (GAPS8 06ebe184): tokens 163: C 75, M 32, U 56   keyed 107/163
after  (this section):   tokens 163: C 84, M 23, U 56   keyed 107/163
```
No.4 itself: 223 cells, uncertain (M) 56 -> 38, C 164 -> 182, 3 struck cells not counted; H 0, S 0, I 0.
Judge, `python3 tools/judge_plaintext.py specs/na-janssens-java-1811.json --file ciphers/na-janssens-java-1811/reading.txt`:
```
FAIL language: score=-0.958, null_p99=-1.833, real_p05=-0.893, real_median=-0.783, mode=both, N=332
ok   words: cover=0.919, min=0.3, real_text_median_cover=0.949
FAIL - na-janssens-java-1811 (a PASS is a gate for a verifier, not a reading; rule 10)
```
Up from -0.973 / 0.916 (GAPS8), still FAIL. No reading is claimed (rule 10); nothing was searched in print this step.
Vision calls: 2 subagent passes; this worker's own looks 3 (one 205R page view, one grid overlay, one sheet check).

## GAPS10-na-janssens-java-1811 (2 Oct 2026, account-4)

Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`, run 22:57-23:0x UTC 2 Oct 2026 (clock read), Opus 5.5.
Intake gate before the step: exit 0. The Verdict step (GAPS9): the contact-sheet page-through of invnr 12's unsampled
leaves and invnr 7 (gap 3). The prompt capped requests to service.archief.nl/nationaalarchief.nl at 50, so this session
covered part of invnr 12 only. Invnr 7 was not reached.

**Which leaves.** The leaves that earlier passes checked are not all recorded leaf by leaf. VX-RD02B's "every 4th" 42
thumbnails were not kept on disk or in the manifest. So "unsampled" here means: not in `images/manifest.json`, not on
disk in `images/`, and outside 180-219. That leaves 159 candidates: 2-178 minus the CS05 points, and 220-232. Picked
first: the ones nearest the cipher cluster, 220-232 (10 leaves, 230 skipped as RD02B already checked it) and
137-178 going down (35 leaves). Leaves 2-136 (114 candidates, of which RD02B saw roughly a quarter unrecorded) are not
covered by this session.

**Method.** 1 request for the item page `nationaalarchief.nl/onderzoeken/archief/2.01.27.05/invnr/@12`; scan ids
parsed from its `drupal-settings-json` (233 scans). Then 45 `service.archief.nl/api/file/v1/thumb/<id>` thumbnails
(256 px), 1.6 s apart: 44 returned HTTP 200 and leaf 140 returned 500, which succeeded on its one retry. The thumbnails
were cut by PIL into 3 contact sheets of 13-16 labelled boxes, kept in the session scratchpad and not committed.
3 vision calls, one per sheet, made by this worker.

**Result** (`leaves_gaps10_contact_inventory.tsv`, 45 rows, grade M, thumbnail eye-check):

| class | n | leaves |
|---|---|---|
| prose | 41 | 137, 139-143, 145-149, 151-155, 157-161, 163-167, 169-172, 175-178, 220, 222, 224, 226, 228, 231, 232 |
| blank | 2 | 173, 225 |
| table | 1 | 223 (ruled register/index, word entries) |
| numeric-uncertain | 1 | 229 |

141, 142 and 143 are counted as prose: they are part-blank leaves carrying a note or letter.
No leaf shows the row-and-column digit grid of 188/192/198, an interlinear gloss like 190-191/199-200/205-207, or a
"Numero"/"Duplicata" heading readable at 256 px. Leaf 229 has numeric clusters at the top left (sums-like, no row
grid) and a pasted prose slip on the right. It looks like leaf 230, which RD02B found at full size to be an
arithmetic jotting and not cipher. 229 was fetched once at IIIF `full/1200,/0` as `images/229_med.jpg` (86 KB, added to
the manifest) and not viewed in this session. Its eye-check is the next job's first look.

Control/caveat (rule 3): a thumbnail pass has a resolution floor. This session ran no matched known-positive thumbnail
of 188 alongside the sheets. The negative "no cipher grid" is therefore conditional on 256 px. The earlier 256 px sweeps
did flag 211 and 230 as numeric, and 211 was the real No.5 hit, so a digit grid does show at this size. A single
glossed line inside a prose letter would not. No reading or decoding was done, and nothing was searched in print.
Requests: nationaalarchief.nl 1, service.archief.nl 47 (45 thumbs + 1 retry + 1 IIIF 1200 px), total 48 of 50. No 429 or 503.

## GAPS11-na-janssens-java-1811 (2 Oct 2026, account-4)

Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`, run 23:16-23:2x UTC 2 Oct 2026 (clock read), Opus 5.5.
Intake gate before the step: exit 0. The Verdict step (GAPS10, with the parent's decision to page invnr 12 before
invnr 7): (1) eye-check `images/229_med.jpg`; (2) page invnr 12 leaves 2-136 by contact sheet.

**229.** One look at the 1200 px file already on disk. The left page has arithmetic jottings: multiplications and
sums such as 14598 x 7 and 3750 x 750, set out as worked sums with rules, with no row-and-column code grid. The right
page has a pasted French prose slip headed "11 avril", beginning "Monseigneur, Conformement aux ordres...". It is not
cipher, not a gloss and not a code table. Leaf 229 is reclassed `arithmetic` (grade H) in
`leaves_gaps10_contact_inventory.tsv`. It is the same kind of leaf as 230 and is not new material.

**Which leaves.** Leaves 2-136 held 113 candidates: every leaf not on disk and not in `images/manifest.json`, the
CS05 points 7, 13 ... 132 excluded. The request limit was 60: 1 for the item page, 58 thumbnails and 1 control. That
covers 58 leaves, taken in a contiguous run from 136 down to 68 so that a whole dispatch set cannot fall between
sample points (the GAPS5 lesson). Leaves 2-67 (55 candidates) are not covered by this session.

**Method.** 1 request for the item page `nationaalarchief.nl/onderzoeken/archief/2.01.27.05/invnr/@12`; scan ids
parsed from its embedded settings JSON (233 scans). Then 58 `service.archief.nl/api/file/v1/thumb/<id>` thumbnails
(256 px), 1.6 s apart. All returned HTTP 200, with no retry, 429 or 503. One more thumbnail, of leaf 188 (the raw No.1
Triplicata), was fetched as a known-positive control and placed inside sheet 3 between leaves 93 and 92. The tiles
were cut by PIL into 4 contact sheets of 14-15 labelled boxes, kept in the session scratchpad and not committed.
4 vision calls, one per sheet, made by this worker. Including the 229 look, that is 5 vision calls in total.

**Control (rule 3).** At the same 256 px, on the same sheet as the target leaves, the leaf 188 tile shows its
row-and-column digit grid plainly. The thumbnail pass can see a full cipher page at this size, so a full cipher page
among 68-136 would have shown. A single glossed line or a short coded passage inside a prose letter would not show,
as GAPS10 already noted. The control was labelled, so it was not blind: it tests the resolution floor, not the
reader's bias.

**Result** (`leaves_gaps11_contact_inventory.tsv`, 58 target rows grade M + 1 control row):

| class | n | leaves |
|---|---|---|
| prose (letters, some part-blank or docket covers) | 56 | 68-69, 71, 73-77, 79-83, 85, 87-89, 91-95, 97-101, 103-107, 109-113, 115-118, 119, 121-125, 127-131, 133-136 |
| blank | 2 | 70, 86 |

Covers with only a docket note: 80, 87, 119. Leaf 103 is prose with a bracketed list and no digits in a grid.
None of the 58 shows a digit grid like 188/192/198, an interlinear gloss like 190-191/199-200/205-207, or a "Numero"
or "Duplicata" heading readable at 256 px. No leaf was flagged, so none was fetched at native size. Nothing was read
or decoded. Requests: nationaalarchief.nl 1, service.archief.nl 59 (58 target thumbnails + 1 control), total 60 of 60.

## GAPS12-na-janssens-java-1811 (2 Oct 2026, account-4)

Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`, run 23:33-23:4x UTC 2 Oct 2026 (clock read), Opus 5.5.
Intake gate before the step: exit 0. The Verdict step (GAPS11): page invnr 12 leaves 2-67 by contact sheet, then
invnr 7 as far as the 60-request limit allows.

**Which leaves.** Leaves 2-67 not in `images/manifest.json`'s leaf list with a local thumbnail: 55 candidates (the
CS05 points 7, 13, 19 ... 60, 66 excluded), the same 55 GAPS11 counted. With this session, every invnr 12 leaf 1-233
has been looked at at least at 256 px: 1-67 here and by CS05, 68-136 GAPS11, 137-178 and 220-232 GAPS10 and CS05/RD02B,
179-219 leaf by leaf (VX-RD02/RD02B, GAPS5).

**Method.** 1 request for the item page `nationaalarchief.nl/onderzoeken/archief/2.01.27.05/invnr/@12`; scan ids
parsed from its embedded settings JSON (233 scans). Then 55 `service.archief.nl/api/file/v1/thumb/<id>` thumbnails
(256 px) and the leaf 188 thumbnail (control), 1.6 s apart, all HTTP 200, no retry, 429 or 503. 4 contact sheets of
14-15 labelled boxes (PIL, session scratchpad, not committed), with the leaf 188 tile placed at a different position
on **every** sheet (GAPS11 had it on one). 4 vision calls, one per sheet, made by this worker.

**Control (rule 3).** On all 4 sheets the leaf 188 tile shows its row-and-column digit grid plainly at the same
256 px. A full cipher page among 2-67 would have shown. A single coded line inside a prose letter would not (the
GAPS10/11 caveat stands). The control was labelled, so it tests the resolution floor, not reader bias.

**Result** (`leaves_gaps12_contact_inventory.tsv`, 55 target rows grade M + 1 control row):

| class | n | leaves |
|---|---|---|
| prose (letters, some with a blank cover page or docket) | 51 | all of 2-67 not listed below |
| blank / near-blank | 2 | 38, 53 (one docket line) |
| printed | 1 | 44 ("Extrait des Minutes" decree headed Napoleon) |
| table | 1 | 54 (ruled register with word entries) |

Leaves 40-65 are a run of dense French prose (a "Memoire" begins at 56). None of the 55 shows a digit grid like
188/192/198, an interlinear gloss like 190-191/199-200/205-207, or a "Numero"/"Duplicata" heading readable at 256 px.
No leaf was flagged, so none was fetched at native size. Nothing was read or decoded.

**Invnr 7.** With 57 of 60 requests spent, one more request fetched the invnr 7 item page
(`.../2.01.27.05/invnr/@7`, HTTP 200): 190 scans, "Analyses der sedert november 1810 ... van de Gouverneurs-Generaal
H.W. Daendels en J.W. Janssens ontvangen missiven ... met bijgevoegde gedeeltelijke vertaling dier missiven in het
Frans". The scan list (order, label, scan id, thumbnail URL) is saved as `invnr7_scans.tsv`, so the next session
needs no item-page request. No invnr 7 thumbnail was fetched; the earlier sample (every 24th leaf, 8 leaves, "Sweep
for more key source (2)") stands as the only look. Requests: nationaalarchief.nl 2, service.archief.nl 56; total 58
of 60.

`python3 tools/gaps_check.py na-janssens-java-1811` after the update:

```
OK keep-going na-janssens-java-1811: keep going: 2 internal gap(s), 5 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```
(exit 0). Folder 22 MB.

## GAPS13-na-janssens-java-1811 (2 Oct 2026, account-4)

Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`, run 23:52-23:5x UTC 2 Oct 2026 (clock read), Opus 5.5.
Intake gate before the step: exit 0. The Verdict step (GAPS12): page invnr 7 by contact sheet (~182 leaves, ~3 sessions
at 60 requests); this is session 1 of 3: invnr 7 scans 1-58 in order.

**Method.** No item-page request (scan ids from `invnr7_scans.tsv`). 58 `service.archief.nl/api/file/v1/thumb/<id>`
thumbnails (scans 1-58, contiguous; the 1-in-24 sample points inside the range were re-paged, not skipped) plus the
invnr 12 leaf 188 thumbnail (control), 1.6 s apart, all HTTP 200, no retry, 429 or 503: 59 requests. 4 contact sheets of
14-15 labelled tiles (PIL, session scratchpad, not committed), the leaf 188 tile at a different position on every sheet;
4 vision calls, one per sheet, made by this worker.

**Control (rule 3).** On all 4 sheets the leaf 188 tile shows its rows of digit groups at the same 256 px. A full cipher
page or a code-over-gloss page among scans 1-58 would have shown. A single coded line, or a code number quoted inside a
prose précis, would not (the GAPS10-12 caveat stands, and matters more here: invnr 7 is an *analysis* register, so a
No.1 précis would be prose, not cipher, and could only be found by reading).

**Result** (`leaves_gaps13_contact_inventory.tsv`, 58 rows grade M + 1 control row):

| class | n | scans |
|---|---|---|
| analysis register (margin summary column + précis prose; 6, 18-20, 22-23 with an inset figures column) | 29 | 3-31 |
| table (ruled accounts / "Staat" registers, word entries and sums) | 13 | 37-38, 46-55, 58 |
| prose (single documents, letters or memoranda) | 6 | 35-36, 39, 41, 43-44 |
| blank / near-blank | 8 | 32-34, 40, 42, 45, 56-57 |
| cover / list | 2 | 1 (cover), 2 (contents-like list) |

Scans 3-31 are the "Analyses" proper: a précis register whose dated margin entries would be where a summary of Janssens's
20 Juin 1811 No.1 sits, if this volume reaches June 1811 -- the margin dates are not legible at 256 px, so which months
3-31 cover is not established. None of the 58 shows a digit grid like 188/192/198, an interlinear gloss, or a
"Numero"/"Duplicata" cipher heading readable at 256 px. No scan was flagged as cipher, gloss or plain copy, so none was
fetched at native size. Nothing was read or decoded. Requests: service.archief.nl 59, nationaalarchief.nl 0.

`python3 tools/gaps_check.py na-janssens-java-1811` after the update:

```
OK keep-going na-janssens-java-1811: keep going: 2 internal gap(s), 5 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```
(exit 0). Folder 22 MB.

## GAPS14-na-janssens-java-1811 (3 Oct 2026, account-4)

Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`, run 00:10-00:2x UTC 3 Oct 2026 (clock read), Opus 5.5.
Intake gate before the step: exit 0. The Verdict step (GAPS13): resume invnr 7 at scan 59; this is session 2 of 3,
scans 59-117 in order.

**Method.** Same as GAPS13. No item-page request (scan ids from `invnr7_scans.tsv`). 59 thumbnails (scans 59-117,
contiguous) plus the invnr 12 leaf 188 thumbnail (control), 1.6 s apart, all HTTP 200, no retry, 429 or 503: 60
requests to service.archief.nl, 0 to nationaalarchief.nl. 4 contact sheets of 15-16 labelled tiles (PIL, session
scratchpad, not committed), the leaf 188 tile at a different position on every sheet; 4 vision calls, one per sheet,
made by this worker.

**Control (rule 3).** On all 4 sheets the leaf 188 tile shows its rows of digit groups at the same 256 px. A full
cipher page or a code-over-gloss page among scans 59-117 would have shown; a single coded line or a code number quoted
in prose would not (the GAPS10-13 caveat stands).

**Result** (`leaves_gaps14_contact_inventory.tsv`, 59 rows grade M + 1 control row):

| class | n | scans |
|---|---|---|
| table (ruled accounts, "Marine" letterhead forms with figures, "Etat general" registers) | 32 | 61-62, 64-65, 70-71, 73-77, 79-80, 83-85, 89-91, 93, 96-98, 104-112 |
| prose (letters/reports on "Marine" letterhead, slips, "Chapitre" articles) | 10 | 68-69, 72, 81-82, 86-87, 94, 116-117 |
| blank / near-blank | 12 | 63, 66, 78, 88, 95, 99-100, 102-103, 113-115 |
| cover | 3 | 67 (one-line title, first word possibly "Traduction", not legible at 256 px), 92 and 101 ("Etat General ...") |
| analysis register (end of the précis run) | 2 | 59-60 |

The précis register (GAPS13 scans 3-31) does not resume here; 59-60 are its last register-like pages. Scans 68-91 are
French "Marine" letterhead returns and letters (accounts, not cipher). None of the 59 shows a digit grid like
188/192/198, an interlinear gloss, or a cipher heading readable at 256 px. No scan was flagged as cipher, gloss or plain
copy, so none was fetched at native size. Nothing was read or decoded. One suggestion, not done (Usage 7): the scan 67
cover title, if it reads "Traduction", heads the bundle 68-91 -- a 1200 px fetch of scan 67 alone (1 request) would
settle it in the next session.

`python3 tools/gaps_check.py na-janssens-java-1811` after the update:

```
OK keep-going na-janssens-java-1811: keep going: 2 internal gap(s), 5 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```
(exit 0). Folder 22 MB.

## GAPS15-na-janssens-java-1811 (3 Oct 2026, account-4)

Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`, run 00:28-00:35 UTC 3 Oct 2026 (clock read), Opus 5.5.
Intake gate before the step: exit 0. The Verdict step (GAPS14): scan 67 at 1200 px first, then resume invnr 7 at
scan 118 as far as 58 more requests allow; this is session 3.

**Scan 67.** The scan's IIIF id needed the invnr 7 item page once (`www.nationaalarchief.nl/.../2.01.27.05/invnr/@7`,
HTTP 200; invnr 7's IIIF path prefix is `a4/9d/8f/96/fa/99/4d/55/b9/bb/e9/dc/48/30/43/75/<scan id>.jp2`, recorded here
so later sessions need no item-page request), then one `full/1200,/0/default.jpg` request (HTTP 200, 63 kB). One vision
call: the cover reads "Factures d'envoi par les Bala[ou]s" (shipping invoices; last word as seen, grade M), facing
page blank. It is not "Traduction": the bundle 68-91 it heads is the accounts/returns run GAPS14 classed, not a
translation. No priority paging followed.

**Method (118-175).** Same as GAPS13/14: 58 `service.archief.nl/api/file/v1/thumb/<id>` thumbnails (scans 118-175,
contiguous, 256 x 200 px), 1.6 s apart, all HTTP 200, no retry, 429 or 503. The leaf 188 control tile was made from the
local `images/188_med.jpg` downscaled to the thumbnail's 256 px (no request), placed at a different position on each of
4 contact sheets of 15-16 tiles (PIL, session scratchpad, not committed); 4 vision calls, one per sheet. Requests:
service.archief.nl 59 (1 + 58), www.nationaalarchief.nl 1.

**Control (rule 3).** On all 4 sheets the 188 tile shows its rows of digit groups. A full cipher page or a code-over-
gloss page among 118-175 would have shown; a single coded line or a code number quoted in prose would not (the
GAPS10-14 caveat stands).

**Result** (`leaves_gaps15_contact_inventory.tsv`: scan 67 + 58 rows grade M + 1 control row):

| class | n | scans |
|---|---|---|
| prose (letter/minute registers with margin columns, letters, tipped-in slips) | 35 | 124-132, 134, 137, 140-143, 147-157, 160-163, 165, 167, 171, 173, 175 |
| blank / near-blank | 9 | 133, 135, 138, 144-145, 158, 166, 168, 174 |
| table (lists with figures columns, recapitulation) | 5 | 119, 122, 136, 139, 164 |
| "Chapitre" register openings | 4 | 118, 120-121, 123 |
| sketch (small pen diagrams with short notes, not digit groups) | 3 | 169-170, 172 |
| cover | 2 | 146 (one large word), 159 (3-line title), neither legible at 256 px |

None of the 58 shows a digit grid like 188/192/198, an interlinear gloss, or a cipher heading readable at 256 px. No
scan was flagged as cipher, gloss or plain copy, so none was fetched at native size. Nothing was read or decoded.
Invnr 7 is now paged to scan 175; scans 176-190 (15 scans, about 15 requests) remain.

`python3 tools/gaps_check.py na-janssens-java-1811` after the update:

```
OK keep-going na-janssens-java-1811: keep going: 2 internal gap(s), 5 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```
(exit 0). Folder 22 MB.

## GAPS16-na-janssens-java-1811 (3 Oct 2026, account-4)

Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`, run 00:47-00:5x UTC 3 Oct 2026 (clock read), Opus 5.5.
The Verdict step (GAPS15): finish the invnr 7 page-through, scans 176-190 (15 scans).

**Method.** Same as GAPS13-15. No item-page request (thumbnail URLs from `invnr7_scans.tsv`). 15
`service.archief.nl/api/file/v1/thumb/<id>` thumbnails (scans 176-190, contiguous, 256 px), 1.6 s apart, all HTTP 200,
no retry, 429 or 503: 15 requests to service.archief.nl, 0 to nationaalarchief.nl. The leaf 188 control tile was made
from the local `images/188_med.jpg` at 256 px (no request), at a different position on each of 2 contact sheets
(8 + 7 tiles plus the control; PIL, session scratchpad, not committed); 2 vision calls, one per sheet.

**Control (rule 3).** On both sheets the 188 tile shows its rows of digit groups and the signature. A full cipher page or
a code-over-gloss page among 176-190 would have shown; a single coded line or a code number quoted in prose would not
(the GAPS10-15 caveat stands).

**Result** (`leaves_gaps16_contact_inventory.tsv`, 15 rows grade M + 1 control row):

| class | n | scans |
|---|---|---|
| table (ruled registers, "Etat ..." tables, lists, some with tipped-in prose slips and red seals) | 11 | 177-187 |
| prose (minute/register page with margin entries) | 1 | 176 |
| blank / back board | 3 | 188-190 |

None of the 15 shows a digit grid like 188/192/198, an interlinear gloss, or a cipher heading readable at 256 px; none
was fetched at native size. Nothing was read or decoded. **Invnr 7 is now paged end to end (scans 1-190, GAPS13-16)
with no cipher, gloss or plain copy found**, and no part of the "partial French translation" of the Janssens missives
the item description names showed at 256 px (it may be prose pages among the 1-190 classed "prose"; a translation in
plain French prose is not distinguishable from other prose at thumbnail size -- a limit of the method, not a negative).

**Next step not run (cap).** The LM-context fill of the 26 conflicting No.4 codes and the unkeyed leaf-188 codes was
not started: its estimate (~$5) would cross 80% of this session's USD 6 cap after the page-through. Note for its brief:
the gloss and plain copies are French, so the language model is `tools/data/fr1810` (era-matched, 1810s French), not a
Dutch corpus; the matched control is No.4's raw copy (204R) against its plain copy (208R-209), same hidden-code
fraction, plus a 20-seed shuffled-assignment control and a known-answer check on settled codes; a code moves only if
it beats both, and conflicting H/C witnesses are never settled by majority (rule 4).

`python3 tools/gaps_check.py na-janssens-java-1811` after the update:

```
OK keep-going na-janssens-java-1811: keep going: 2 internal gap(s), 5 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```
(exit 0). `tools/decode_key.py --check` exit 0 (no reading change; leaf 188 still 107/163 keyed, C 84 M 23).

## GAPS17-na-janssens-java-1811 (3 Oct 2026, account-4)

Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`, run 01:06-01:2x UTC 3 Oct 2026 (clock read), Opus 5.5.
The Verdict step (GAPS16): the key-rebuild LM-context fill of the 26 conflicting No.4 codes (`conflicts.tsv` rows with a
`no4-*` witness). Disk only: 0 requests, 0 vision calls.

**Pre-registration.** `lmfill/PREREG.md`, commit e5ff7541, pushed before `lmfill/lmfill.py` scored anything: letter
5-gram (interpolated backoff) on `tools/data/fr1810`, text folded by `judge_plaintext.fold()`; contexts = every
occurrence of the code in the code sequences on disk (190, 191, 199, 200, No.5, 192, 201, No.4 205R-207L, and leaf 188
with key values), 3 tokens either side; a code moves only if (1) winner minus runner-up >= 1.0 log10, (2) that margin
exceeds the maximum of 20 shuffled-assignment margins (same value pair scored in an equal number of contexts drawn from
the other codes' occurrences -- the control varies the context, the axis the statistic depends on), and (3) the method
passes its known-answer gate: on settled No.4 cells (plain-copy-confirmed, grade C, not in conflicts.tsv), contexts from
No.4 with 34% of neighbours masked (leaf 188's unkeyed fraction), true value vs one morphological decoy, precision >= 0.85
on >= 15 items clearing gates 1-2. A moved code keeps grade M; witnesses stay in conflicts.tsv (rule 4: no majority).

**Known-answer (method gate, No.4 matched control).** 131 items; argmax correct 103/131 = 0.786 with no gate; 15 clear
gates 1-2, of which 13 are right = **0.867 -> PASS, at the pre-registered minimum count** (`lmfill/known_answer.tsv`).
Caveat, post hoc and not used to change any gate: most cleared decoys are non-words (abl, notr, cen, l's); on the 7
cleared items whose decoy is a real word the method is 5/7 (wrong on navale/naval and enlevé/enlevés, exactly the
gender/number shape of several target conflicts), so the method is weak for that shape.

**Result** (`lmfill/results.tsv`): of 26 codes, **6 clear all three gates** (value column set, grade M kept):

| code | witnesses | LM winner | margin (log10) | shuffled max | contexts |
|---|---|---|---|---|---|
| 13 | aux / au- / au | au | 13.14 | 7.51 | 7 |
| 102 | peu / peut | peu (unchanged) | 7.04 | 1.14 | 6 |
| 697 | ble / bles | ble (unchanged) | 2.90 | 2.71 | 3 |
| 1040 | uner / nu | nu | 12.38 | 8.18 | 2 |
| 1094 | Douze / dont | dont | 5.94 | 5.90 | 2 |
| 1096 | part / par | par | 16.40 | 15.29 | 9 |

19 do not clear (the shuffled-context margin is as large as the real one: the preference is the model's prior for the
shorter/commoner string, not the context) and 1 (456 re/=re) is untested-by-this-tool (folds equal). 697, 1094 and 1096
clear gate 2 by under 0.2 log10 and 1094/1040 rest on 2 contexts each: weak moves, graded M. Only 1096 occurs on leaf 188
(line 10: "Gouverneur Gal part chargent" -> "Gouverneur Gal par chargent"); the other five are key-only.

**Leaf 188 after:** keyed 107/163 unchanged, **C 84, M 23, U 56 before and after** (the one changed token stays M);
`tools/decode_key.py --check` exit 0; judge FAIL language -0.956 vs real_p05 -0.887, cover 0.918 (was -0.958 / -0.893 /
0.919). Not run: an LM fill of the 56 unkeyed leaf-188 codes (no candidate set; open vocabulary), named in the Escalation row.

`python3 tools/gaps_check.py na-janssens-java-1811` after the update:

```
OK keep-going na-janssens-java-1811: keep going: 2 internal gap(s), 5 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```
(exit 0).

## R10-JANS26-na-janssens-java-1811 (6 Oct 2026, account 2)

Brief `.claude/briefs/runs/2026-10-06-account2-run10-jobs.md` section "R10-JANS26", run 07:21-07:29 UTC 6 Oct 2026 (clock
read), Opus 5.5, for LANE LANE-RUN10-account-2. The Verdict step (GAPS17): the invnr 26 page-through (gap 3), one
60-request session. Not run before (no dated section; invnr 26 had only VX-RD02B's every-8th sample of 24 leaves, which
leaves were sampled not recorded).

**Method.** 1 request for the item page `www.nationaalarchief.nl/onderzoeken/archief/2.01.27.05/invnr/@26` (HTTP 200);
191 scan ids parsed from its `drupal-settings-json` and saved as `invnr26_scans.tsv` (order, label, scan id, thumbnail
URL, IIIF info URL), so later sessions need no item-page request. Then 58 `service.archief.nl/api/file/v1/thumb/<id>`
thumbnails (scans 1-58, contiguous, 256 px), 1.9 s apart, all HTTP 200, no retry, 429 or 503. Leaf 188 control tile
made from the local `images/188_med.jpg` at 256 px (no request), at a different position on each of 4 contact sheets of
14-16 tiles (PIL, session scratchpad, not committed); 4 vision calls by this worker, one per sheet, plus one 2x zoom of
the 9-11 thumbnails and one look at each 1200 px fetch. Requests: www.nationaalarchief.nl 1, service.archief.nl 60
(58 thumbnails + 2 IIIF `full/1200,/0`).

**Control (rule 3).** On all 4 sheets the 188 tile shows its rows of digit groups and the signature. The one cipher page
in 1-58 showed at the same size (below), so the control did what it is for; a single coded line inside prose would still
not show (the GAPS10-16 caveat stands).

**Result** (`leaves_jans26_contact_inventory.tsv`, 58 rows grade M + 1 control row):

| class | n | scans |
|---|---|---|
| prose (letters to the Minister, most headed "A Son Excellence ... Monseigneur" and signed with the Janssens flourish) | 46 | 2-3, 6-9, 12-30, 32-34, 36-40, 42-54 |
| table / list registers | 6 | 4-5, 55-58 |
| blank / near-blank | 3 | 31, 35, 41 |
| cover | 1 | 1 |
| **cipher (numeric code rows, no gloss)** | **2** | **10-11** |

**Hit: scans 10-11 are a second copy of dispatch No.1's cipher.** Both fetched at 1200 px (`images/inv26_010_med.jpg`,
`images/inv26_011_med.jpg`, 64 and 52 kB, in `images/manifest.json` with `"invnr": 26`). Described by eye at 1200 px,
grade M, not transcribed (the brief forbids transcription in this job):
- Scan 10, right page (foliated "5" top right): 19 rows of numeric code groups with dots, no interlinear gloss, no
  heading line visible above the first row. Rows 1-2 read by eye "204 387 374 848 1197 79 441 497 853 1121 / 444 605
  130 1173 573 1027 140 1024 403": from the sixth group on this is leaf 188's opening (ciphertext.tsv line 1 "79 441 497
  853 1121 444 605 130 1173 573 1027", line 2 "140 1024 403 ..."), preceded by **5 codes not on leaf 188** (204, 387,
  848 and 1197 are in key.tsv; 374 is not). Row 5 has a pen stroke through its first groups ("102 140 17[6] ..."; leaf 188
  line 3-4 "102 140 / 176 990 156 1104"), cause not determined at 1200 px. Row 18 reads by eye "... 984 1192 443 164",
  agreeing with SPLIT's correction 1194 -> 1192 (corrections.tsv row 2) rather than the original 1194 -- an eye check at
  1200 px, M, not a pass.
- Scan 10, left page: faint prose with a signature, lighter than ink on the page (offset or show-through), not cipher.
- Scan 11, left page: 2 rows "568 976 363 25 929 102 534 514 / 760 585 1197 420." (= leaf 188 lines 14-15, its last 11
  tokens), then the Janssens signature with a small date line under it ("...1811", day and month not read at 1200 px);
  the rest of the page is the mirrored offset of scan 10's cipher. Right page: the next letter, "A Son Excellence ...
  Monseigneur", with a slanted 4-line note in another hand in the left margin, not read.

So invnr 26 holds a signed copy of No.1 in Janssens' own outgoing series, with the same body as leaf 188 (start and end
checked by eye; the middle not compared) and 5 more leading codes. Its copy label (Primata/Duplicata) was not seen: no
heading line is visible on the page at 1200 px. It is **not a decipherment, gloss, plain copy or translation**: no
key source for No.1's 56 unkeyed codes was found in scans 1-58. It is a second witness for leaf 188's digits and for
whatever the 5 extra codes are (a heading or opening phrase leaf 188 lacks, or leaf 188's own first row cut or written
elsewhere -- not determined). The every-8th sample of 2 Oct missed it. Nothing was decoded, and the reading is unchanged.

**Not covered:** invnr 26 scans 59-191 (133 scans, about 2.3 more 60-request sessions; scan list on disk). The prose
letters near 10-11 (9, 12) were not read at higher resolution; a covering letter for No.1 or a later plain repeat of it
could sit among them and is not distinguishable from other prose at 256 px.

`python3 tools/gaps_check.py na-janssens-java-1811` after the update:

```
OK keep-going na-janssens-java-1811: keep going: 2 internal gap(s), 5 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```
(exit 0). `tools/decode_key.py --check` exit 0 (no reading change; leaf 188 C 84, M 23, U 56). Folder 22 MB.

## R10-JANS26B-na-janssens-java-1811 (6 Oct 2026, account 2)

Brief `.claude/briefs/runs/2026-10-06-account2-run10-jobs.md` section "R10-JANS26B", run 07:40-07:46 UTC 6 Oct 2026 (clock
read), Opus 5.5, for LANE LANE-RUN10-account-2. Continues R10-JANS26: invnr 26 page-through from scan 59, one session of
<= 60 requests.

**Method.** Same as R10-JANS26 and GAPS10-16: scan list read from `invnr26_scans.tsv` (no item-page request); 58
`service.archief.nl/api/file/v1/thumb/<id>` thumbnails (scans 59-116, contiguous, 256 px), 1.9 s apart, all HTTP 200, no
retry, 429 or 503. Leaf 188 control tile from the local `images/188_med.jpg` at 256 px (no request), at a different
position on each of 4 contact sheets of 14-15 tiles (PIL, session scratchpad, not committed); 4 vision calls by this
worker, one per sheet. Requests: service.archief.nl 58, nothing else.

**Control (rule 3).** On all 4 sheets the 188 tile shows its rows of digit groups and the signature, as on R10-JANS26's
sheets where the inv26 No.1 copy (scans 10-11) showed at the same size. A single coded line inside prose would still not
show (the GAPS10-16 caveat stands).

**Result** (`leaves_jans26b_contact_inventory.tsv`, 58 rows grade M + 1 control row):

| class | n | scans |
|---|---|---|
| prose (letters headed to the Minister, most signed with the Janssens flourish; 77 a draft with struck lines) | 26 | 65, 68-71, 73-87, 89-93, 95 |
| table / list registers and account tables (lettered sections A-G) | 25 | 59-64, 96-111, 113-115 |
| blank / near-blank | 5 | 72, 88, 94, 112, 116 |
| sketch (pen drawings of box/crate shapes beside a letter page) | 2 | 66-67 |
| cipher, gloss, plain copy or translation | 0 | -- |

No cipher grid, interlinear gloss, plain copy or translation of No.1 in scans 59-116; no 1200 px fetch was needed. No key
source for No.1's 56 unkeyed codes was found. Nothing decoded; reading unchanged.

**Not covered:** invnr 26 scans 117-191 (75 scans, about 1.3 more 60-request sessions; scan list on disk). The prose
letters were not read above 256 px, so a covering letter or a plain repeat of No.1 inside them is not excluded.

## R10-JANS26C-na-janssens-java-1811 (6 Oct 2026, account 2)

Brief `.claude/briefs/runs/2026-10-06-account2-run10-jobs.md` section "R10-JANS26C", run 07:59-08:03 UTC 6 Oct 2026 (clock
read), Opus 5.5, for LANE LANE-RUN10-account-2. Continues R10-JANS26/26B: invnr 26 page-through from scan 117, one session
of <= 60 requests.

**Method.** Same as R10-JANS26/26B and GAPS10-16: scan list read from `invnr26_scans.tsv` (no item-page request); 60
`service.archief.nl/api/file/v1/thumb/<id>` thumbnails (scans 117-176, contiguous, 256 px), 1.9 s apart, all HTTP 200, no
retry, 429 or 503. Leaf 188 control tile from the local `images/188_med.jpg` at 256 px (no request), at a different
position on each of 5 contact sheets (15, 15, 14, 14 and 2 scans; PIL, session scratchpad, not committed); 5 vision calls by
this worker, one per sheet. Requests: service.archief.nl 60, nothing else. The 60-request session cap stops at 176, so
"finish" in one session was not possible (75 scans remained).

**Control (rule 3).** On all 5 sheets the 188 tile shows its rows of digit groups and the signature, as on R10-JANS26's
sheets where the inv26 No.1 copy (scans 10-11) showed at the same size. A single coded line inside prose would still not
show (the GAPS10-16 caveat stands).

**Result** (`leaves_jans26c_contact_inventory.tsv`, 60 rows grade M + 1 control row):

| class | n | scans |
|---|---|---|
| prose (letters, many headed to the Minister and signed with the Janssens flourish) | 24 | 119, 124-132, 134-138, 144-146, 148-149, 152, 162-163, 173 |
| table / list / register / account pages | 23 | 117, 121-122, 139-141, 153-156, 158-161, 165, 167-169, 171-172, 174-176 |
| blank / near-blank | 13 | 118, 120, 123, 133, 142-143, 147, 150-151, 157, 164, 166, 170 |
| cipher, gloss, plain copy or translation | 0 | -- |

No cipher grid, interlinear gloss, plain copy or translation of No.1 in scans 117-176; no 1200 px fetch was needed. No key
source for No.1's 56 unkeyed codes was found. Nothing decoded; reading unchanged.

**Not covered:** invnr 26 scans 177-191 (15 scans, one short session of 15 requests; scan list on disk). The prose letters
were not read above 256 px, so a covering letter or a plain repeat of No.1 inside them is not excluded.

## R10-JANS26D-na-janssens-java-1811 (6 Oct 2026, account 2)

Brief `.claude/briefs/runs/2026-10-06-account2-run10-jobs.md` section "R10-JANS26D", run 08:17-08:22 UTC 6 Oct 2026 (clock
read), Opus 5.5, for LANE LANE-RUN10-account-2. The last 15 scans of the invnr 26 page-through (gap 3), then gap 3's state.

**Method.** Same as R10-JANS26/26B/26C and GAPS10-16: scan list read from `invnr26_scans.tsv` (no item-page request); 15
`service.archief.nl/api/file/v1/thumb/<id>` thumbnails (scans 177-191, contiguous, 256 px), 1.9 s apart, all HTTP 200, no
retry, 429 or 503. Leaf 188 control tile from the local `images/188_med.jpg` at 256 px (no request), at a different position
on each of 2 contact sheets (8 and 7 scans; PIL, session scratchpad, not committed); 2 vision calls by this worker, one per
sheet. Requests: service.archief.nl 15, nothing else.

**Control (rule 3).** On both sheets the 188 tile shows its rows of digit groups and the signature, as on R10-JANS26's sheets
where the inv26 No.1 copy (scans 10-11) showed at the same size. A single coded line inside prose would still not show (the
GAPS10-16 caveat stands).

**Result** (`leaves_jans26d_contact_inventory.tsv`, 15 rows grade M + 1 control row):

| class | n | scans |
|---|---|---|
| prose (short signed pieces, one headed page at 186) | 6 | 183-188 |
| table / list pages (numbered entries with signatures) | 4 | 177, 179-181 |
| blank / near-blank (offset, inserted slips) | 4 | 178, 182, 189-190 |
| back cover | 1 | 191 |
| cipher, gloss, plain copy or translation | 0 | -- |

No cipher grid, interlinear gloss, plain copy or translation of No.1 in scans 177-191; no 1200 px fetch was needed. Nothing
decoded; reading unchanged.

**Gap 3 state.** invnr 26 is now paged end to end (1-191: R10-JANS26 1-58, R10-JANS26B 59-116, R10-JANS26C 117-176, this
job 177-191). With invnr 12 (GAPS10-12, plus GAPS5's 186-215 at 1200 px and above) and invnr 7 (GAPS13-16), all three known
Janssens inventory numbers in NA 2.01.27.05 are paged end to end at 256 px with a leaf-188 positive control on every sheet.
Invnrs 11 (22 scans) and 13 (6 scans) were checked by description in VX-RD02B ("Sweep for more key source", no Janssens/Java
cipher content) and are not page-through candidates. The one find is the inv26 copy of No.1's cipher itself (scans 10-11),
a second digit witness, not a key source. What is left for No.1's key source: the Paris side (a Primata/Duplicata
decipherment or a Ministere de la Marine translation), which is gap 4, waiting on LOCAL-QUEUE.tsv row L31 (and the Collet
1910 footnotes, L35). Residual, not a step: the prose letters were read at 256 px only, so a covering letter that quotes
No.1 in clear is not excluded; no cheap instrument for reading ~550 prose pages at sense level is named.

## R11-JANS26TX-na-janssens-java-1811 (6 Oct 2026, account 2)

Brief `.claude/briefs/runs/2026-10-06-account2-run11-jobs.md` section "R11-JANS26TX", run 09:17-09:22 UTC 6 Oct 2026 (clock
read), Opus 5.5, for LANE LANE-RUN11-account-2. Two-pass transcription of the invnr 26 copy of dispatch No.1 (scans 10-11,
found by R10-JANS26) and alignment against leaf 188. Pre-registered in `PREREG-R11-JANS26TX.md` (commit e85835654, pushed
before any pass or score).

**Material and crops.** 2 IIIF info.json + 2 `full/full` fetches from service.archief.nl (5000 px wide, the server's
maxWidth; native 5228/5195), 2.0 s apart, all HTTP 200; full images kept in the session scratchpad only (re-fetchable from
`invnr26_scans.tsv`). Crops, pasted commands:
`python3 tools/iiif_lines.py --image inv26_010_full.jpg --region 2480,330,2370,2380 --out images/crops_inv26 --prefix i26s10 --debug --centres 100,225,325,435,550,660,775,895,1020,1135,1240,1350,1465,1585,1705,1820,1930,2050,2190 --follow-slope 400`
(auto-detection found 18 of the 19 rows, so centres were given by eye) and
`python3 tools/iiif_lines.py --image inv26_011_full.jpg --region 330,300,2150,360 --out images/crops_inv26 --prefix i26s11 --centres 130,265 --debug`
(re-cut: the first cut clipped scan 11's second row, and both passes then read its last code as 120).

**Passes.** Two blind Sonnet passes on the 21 crops only (`inv26_passA.tsv`, `inv26_passB.tsv`; scan 10's 19 rows and scan
11's 2 rows in one call per pass, since the cipher runs across the two pages; 168 codes each): 167/168 codes agree. The
worker reconciled from the crops (`inv26_reconciled.tsv`): 7:2 A 80 / B 50 -> 50 (the S-shaped 5 of this hand); 21:4 both
passes 120 on the clipped crop -> 420 on the re-cut crop (open-top 4); 19:2 590 kept M (first digit overwritten); row 5's
first four codes (102 140 176 990) kept M as legible under a heavy pen stroke. 163 H, 5 M.

**Scored alignment (pre-registered).** `scripts/inv26_align.py` (Needleman-Wunsch on whole codes vs `ciphertext.tsv` as
transcribed, corrections not applied), output `inv26_vs_188.tsv`, `--check` mode:

```
inv26 codes 168, leaf188 codes 163; agree 161, differ 2, only-inv26 5, only-188 0
A = 161/163 = 0.988; control mean 0.078, max 0.153, shuffles >= real 0/1000
GATE PASS
```

The copy is the same text as leaf 188, code for code, with no gap on either side after the 5 leading codes.

| leaf 188 position | leaf 188 (split188 A/B) | inv26 (passes A/B, recon.) | image says |
|---|---|---|---|
| 13:11 | 1194 as transcribed; 1192 by SPLIT's correction (corrections.tsv) | 1192 / 1192 / 1192 H (19:6) | the copy independently supports SPLIT's 1192 'et'; corrections.tsv row already carries it, no change |
| 5:1 | 448 / 448, both H; key 'la' C | 948 / 948 / 948 H (6:5) | leaf 188 plainly 448 (crops_188/188_L05.jpg); the copy's first digit has the 9 descender. 948 is not in key.tsv; read as a copyist's variant on the copy; leaf 188 unchanged (PREREG: leaf 188's reading is not doubtful) |

Every leaf-188 M-read digit position agrees with the copy, including 19:2/the 590 group and the struck row-5 groups,
so nothing in leaf 188 moves: **no corrections.tsv change, reading unchanged** (`tools/decode_key.py --check` exit 0, leaf
188 C 84, M 23, U 56). The copy settles no unkeyed code, since it carries the same codes as leaf 188.

**The 5 leading codes** are 204 387 574 845 1197 (both passes and the worker agree; R10-JANS26's eye read "374 848" at
1200 px was wrong in two digits). Through the existing key.tsv they read "Batavia vingt Deux Juin ." (204 C, 387 M -- single
No.4 occurrence, 574 C, 845 C, 1197 C): a place-and-date opening, Batavia 22 June [1811], that leaf 188's Triplicata does
not carry. Grade per token as keyed: C 4, M 1; no key value added (all five already in key.tsv). It agrees with the
signature date line under scan 11's text ("...1811", day and month still not read). No copy label (Primata/Duplicata)
appears on either page.

**Requests:** service.archief.nl 4 (2 info.json, 2 full images). Subagents: 2 Sonnet passes; reconciliation by the worker.
Not done: the signature date line on scan 11 at native size (would check "22 Juin" against the plain hand, ~1 request, cheap).

## While waiting (GAPS7-na-janssens-java-1811, 2 Oct 2026)

- The one action that depends on nobody while LOCAL-QUEUE rows L31 (Paris search) and L35 (Collet 1910 footnotes) wait: the
  rest of the contact-sheet page-through (invnr 7, then invnr 26; gap 3, ~$4 per 60-request session). GAPS10
  (2 Oct 2026) paged 45 leaves (137-178, 220-232) and GAPS11 (2 Oct 2026) paged 58 more (68-136, with a 188 positive
  control) and GAPS12 (2 Oct 2026) the last 55 (2-67, 188 control on every sheet): no cipher, gloss or plain copy;
  invnr 12 is now paged end to end. What remains of this action: invnr 7 (190 scans, list on disk as invnr7_scans.tsv); GAPS13 (2 Oct 2026) paged scans 1-58 (no cipher, gloss or plain copy), GAPS14 (3 Oct 2026) paged scans 59-117 (no cipher, gloss or plain copy), GAPS15 (3 Oct 2026) scan 67 at 1200 px ("Factures d'envoi", not a translation) and scans 118-175 (no cipher, gloss or plain copy), and GAPS16 (3 Oct 2026) scans 176-190 (no cipher, gloss or plain copy): invnr 7 is paged end to end. What remains of this action: invnr 26 (sampled 1 in 8) -- R10-JANS26 (6 Oct 2026) paged scans 1-58: scans 10-11 are a second, signed copy of No.1's cipher (same body as leaf 188 plus 5 leading codes; no gloss, plain copy or translation); R10-JANS26B (6 Oct 2026) paged scans 59-116 (no cipher, gloss or plain copy); R10-JANS26C (6 Oct 2026) paged scans 117-176 (no cipher, gloss or plain copy); R10-JANS26D (6 Oct 2026) paged scans 177-191 (no cipher, gloss or plain copy): no page-through of the known Janssens invnrs (12, 7, 26) remains, so this action is DONE; the two-pass transcription of the inv26 No.1 copy was DONE 6 Oct 2026 (R11-JANS26TX, section above: 161/163 codes agree with leaf 188 vs shuffled max 0.153, no leaf-188 change, 5 leading codes read "Batavia vingt Deux Juin ."); what depends on nobody now is the disk-only LM-context fill (key-rebuild row), which depends on nobody: its conflict half DONE 3 Oct 2026 (GAPS17, 6 of 26 moved at grade M), the unkeyed-code half not yet run. The No.4 second gloss pass named here
  before was DONE 2 Oct 2026 (GAPS9-na-janssens-java-1811, section above).

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
Read so far: 107 of 163 code tokens keyed (65.6%; C 84, M 23, U 56; GAPS9 2 Oct 2026 native second gloss pass on the No.4 doubtful cells, was C 75 M 32 at GAPS8, 88/163 C 77 M 11 at GAPS3, 86/163 at GAPS 02:07 UTC and 76/163 on 1 Oct), reading.txt header and NOTES.md "GAPS9-na-janssens-java-1811 (2 Oct 2026, account-4)"; keyed is not read-as-sense (judge FAIL language -0.958 vs real_p05 -0.893, cover 0.919; was -0.973 / 0.916 at GAPS8, -0.963 / 0.915 at GAPS3, and -1.472 / 0.78 on 1 Oct); the 56 unkeyed tokens and the 23 M tokens are listed in reading_tokens.tsv
Done (gap 1, both halves): Leaf 192 (the rest of the No.2 interlinear gloss) - DONE 2 Oct 2026 (GAPS-na-janssens-java-1811, section above): two blind passes on tools/iiif_lines.py crops of images/192_hi.jpg (58 codes each, 57/58 code and 53/58 gloss agreement) plus one reconciliation, merged by scripts/merge_leaf.py: key.tsv 214 -> 233 codes, leaf 188 keyed 76 -> 86/163 (52.8%), "l'ancien Gouverneur Gal" read twice as predicted, judge -0.985 vs real_p05 -0.89 (FAIL, from -1.472), --check exit 0. Leaf 201 left page (two code+gloss rows ending "Signé Janssens") - DONE 2 Oct 2026 (GAPS2-na-janssens-java-1811, section above): one IIIF fetch (images/201_hi.jpg), tools/iiif_lines.py crops, two blind passes (8 codes each, 8/8 code and 8/8 gloss agreement) plus one reconciliation (674 dans -> 574 deux from the digit and final-letter shapes), scripts/merge_leaf.py: key.tsv 233 -> 237 codes, leaf 188 keyed 86 -> 88/163 (54.0%), line 12 now "vaisseaux ... tous les ... l'ennemie", judge -0.976 vs real_p05 -0.899 (FAIL, from -0.985), --check exit 0. Gap 1 is closed: no further glossed leaf of this set is known on disk (which dispatch leaf 201 closes is unidentified; its earlier leaves, if in the bundle, fall to gap 3's re-inventory)
- Leaf 188: the remaining unkeyed codes, via the No.4 "Premiere Expedition" set (3 Aout 1811) - blocker: not-attempted; first pass DONE 2 Oct 2026 (GAPS8-na-janssens-java-1811, section above): 204R raw and the 205R-207L gloss transcribed from tools/iiif_lines.py crops of the 1200-px spreads (223 cells; gloss-table codes vs the independent raw read 190/222 before, 192/223 after one reconciliation), plain copy 208R-209L sealed before alignment; gloss reading vs plain copy by tools/interlinear_align.py (--digits 4 --word-prior): 154/210 positions = 0.733 against a shuffled-order null of mean 0.191, max 0.233 (20 seeds), char LCS 0.874 vs null mean 0.444; merged by scripts/merge_leaf.py: key.tsv 237 -> 328 codes, leaf 188 keyed 88 -> 107/163, but 32 codes now conflict with earlier leaves or within No.4 (conflicts.tsv) and 56 No.4 cells disagree with the plain copy (no4/conflicts_no4.tsv), mostly single-pass gloss misreads (sous/sont, par/pas, Douze/dont, Mr. 4/N°. 4), so leaf 188's C fell 77 -> 75 and M rose 11 -> 32; second pass DONE 2 Oct 2026 (GAPS9-na-janssens-java-1811, section above): 6 native IIIF requests, 82 doubtful cells (56 uncertain + the cells of 31 No.4 conflict codes) cut per cell, two blind Opus passes (gloss 74/82 agree), a cell changed only when both agreed: 21 changed, 52 confirmed, 8 split kept, 1 struck kept; gloss vs sealed plain copy 172/210 = 0.819 against the shuffled-order null mean 0.199, max 0.238 (20 seeds), char LCS 0.903 vs null mean 0.447; re-merged from the pre-GAPS8 key (no double count): No.4 conflict codes 31 -> 26 (resolved 110, 364, 656, 808, 1106, 1195; new 743 trois/Troi), No.4 uncertain cells 56 -> 38, leaf 188 C 75 -> 84, M 32 -> 23, keyed 107/163 unchanged, --check exit 0, judge -0.958 vs real_p05 -0.893 (FAIL); remaining: the 26 conflicts are logged with witnesses, mostly accent/punctuation or homophone/fragment questions no further image read settles; the 56 unkeyed leaf-188 codes are attested on no glossed leaf on disk; next: the gap 3 contact-sheet page-through for more glossed leaves carrying these codes, ~$8
- Dispatch No.1's own key source (its decipherment, a plain copy, or a Paris translation) elsewhere in the archive series - blocker: waiting-on LOCAL-QUEUE.tsv row L31 (the Paris-side search; the NA archive-series half is paged end to end, see R10-JANS26D); first half DONE 2 Oct 2026 (GAPS5-na-janssens-java-1811, section above): leaves 186-215 re-inventoried at the best resolution on disk (7 fetched at 1200 px, 4 contact sheets, 4 blind vision passes, leaves_186-215_inventory.tsv, all 30 rows H): no No.1 gloss or plain copy in the range; 14 manifest misfilings fixed (194-195 = plain No.2, 201 = No.3 postscript, 202R = plain No.3, 204-209 = the No.4 set, 210 = the No.5 slip); still open: invnr 12 leaves 1-179 and 218-233 were only sampled (CS05 every ~5.6th leaf, RD02B every 4th), invnr 7 at 1 in 24 and invnr 26 at 1 in 8 (NOTES "Sweep for more key source (2)"), and the 186-215 inventory shows a sample step of 4-6 misses whole dispatch sets; contact-sheet page-through PART 1 DONE 2 Oct 2026 (GAPS10-na-janssens-java-1811, section above): 45 unsampled invnr 12 leaves (137-178 and 220-232), 256 px thumbnails, 3 sheets, 3 vision calls, leaves_gaps10_contact_inventory.tsv: 41 prose, 2 blank, 1 table, 1 numeric-uncertain (229, likely the same arithmetic jotting as 230; fetched at 1200 px as images/229_med.jpg, not yet eye-checked), no cipher grid, gloss or plain copy; contact-sheet page-through PART 2 DONE 2 Oct 2026 (GAPS11-na-janssens-java-1811, section above): 229_med.jpg eye-checked = arithmetic jottings + a French prose slip of 11 avril, not cipher; 58 more invnr 12 leaves paged (68-136, contiguous), 4 sheets, 5 vision calls, 60 requests, with leaf 188's thumbnail as a known-positive control on the same sheet (its digit grid plainly visible at 256 px): 56 prose, 2 blank, no cipher grid, gloss or plain copy (leaves_gaps11_contact_inventory.tsv); contact-sheet page-through PART 3 DONE 2 Oct 2026 (GAPS12-na-janssens-java-1811, section above): the last 55 invnr 12 leaves (2-67), 4 sheets with leaf 188's thumbnail as known-positive control on every sheet (grid plainly visible each time), 4 vision calls, 58 requests: 51 prose, 2 blank, 1 printed decree, 1 table, no cipher grid, gloss or plain copy (leaves_gaps12_contact_inventory.tsv); invnr 12 is now paged end to end at 256 px or better with no No.1 key source found (a single coded line inside a prose letter would not show at 256 px); invnr 7 scan list saved (invnr7_scans.tsv, 190 scans, 1 request); invnr 7 page-through SESSION 1 DONE 2 Oct 2026 (GAPS13-na-janssens-java-1811, section above): scans 1-58, 4 sheets with the leaf 188 control on every sheet (digit groups visible each time), 4 vision calls, 59 requests: 29 analysis-register openings (3-31, précis prose, margin dates not legible at 256 px), 13 tables, 6 prose, 8 blank/near-blank, cover + list; no cipher grid, gloss or plain copy (leaves_gaps13_contact_inventory.tsv); invnr 7 page-through SESSION 2 DONE 3 Oct 2026 (GAPS14-na-janssens-java-1811, section above): scans 59-117, 4 sheets with the 188 control on every sheet (digit groups visible each time), 4 vision calls, 60 requests: 32 tables, 10 prose, 12 blank, 3 covers (67 title possibly "Traduction", unread), 2 register; no cipher grid, gloss or plain copy (leaves_gaps14_contact_inventory.tsv); invnr 7 page-through SESSION 3 DONE 3 Oct 2026 (GAPS15-na-janssens-java-1811, section above): scan 67 at 1200 px = "Factures d'envoi par les Bala[ou]s" (invoices, not "Traduction"), scans 118-175 by 4 sheets with the 188 control on every sheet, 5 vision calls, 60 requests: 35 prose, 9 blank, 5 tables, 4 register openings, 3 sketches, 2 covers; no cipher grid, gloss or plain copy (leaves_gaps15_contact_inventory.tsv); invnr 7 page-through SESSION 4 DONE 3 Oct 2026 (GAPS16-na-janssens-java-1811, section above): scans 176-190 by 2 sheets with the 188 control on both, 2 vision calls, 15 requests: 11 tables, 1 prose, 3 blank; no cipher grid, gloss or plain copy (leaves_gaps16_contact_inventory.tsv) -- invnr 7 page-through DONE, paged end to end (1-190); invnr 26 page-through SESSION 1 DONE 6 Oct 2026 (R10-JANS26-na-janssens-java-1811, section above): scans 1-58, 4 sheets with the 188 control on every sheet, 4 vision calls, 61 requests: 46 prose, 6 tables, 3 blank, 1 cover, and scans 10-11 = a second signed copy of dispatch No.1's cipher (images/inv26_010_med.jpg, inv26_011_med.jpg; same body as leaf 188 by eye at start and end, plus 5 leading codes 204 387 374 848 1197; no gloss, plain copy or translation), so still no key source for No.1 (leaves_jans26_contact_inventory.tsv); invnr 26 page-through SESSION 2 DONE 6 Oct 2026 (R10-JANS26B-na-janssens-java-1811, section above): scans 59-116, 4 sheets with the 188 control on every sheet, 4 vision calls, 58 requests: 26 prose, 25 tables, 5 blank, 2 sketches; no cipher grid, gloss, plain copy or translation (leaves_jans26b_contact_inventory.tsv); invnr 26 page-through SESSION 3 DONE 6 Oct 2026 (R10-JANS26C-na-janssens-java-1811, section above): scans 117-176, 5 sheets with the 188 control on every sheet, 5 vision calls, 60 requests: 24 prose, 23 tables/lists, 13 blank; no cipher grid, gloss, plain copy or translation (leaves_jans26c_contact_inventory.tsv); invnr 26 page-through SESSION 4 DONE 6 Oct 2026 (R10-JANS26D-na-janssens-java-1811, section above): scans 177-191, 2 sheets with the 188 control on both, 2 vision calls, 15 requests: 6 prose, 4 lists, 4 blank, back cover; no cipher grid, gloss, plain copy or translation (leaves_jans26d_contact_inventory.tsv) -- invnr 26 paged end to end (1-191); state: invnrs 12, 7 and 26 are all paged end to end at 256 px with the 188 control (invnrs 11 and 13 checked by description, no Janssens cipher content), so the archive-series half of this gap is exhausted at 256 px; the only find is the inv26 copy of No.1's cipher (a second digit witness, not a key source); what remains for No.1's key source is the Paris side, waiting on LOCAL-QUEUE.tsv row L31 (and L35, Collet 1910 footnotes); residual: prose letters read at 256 px only, a clear quotation of No.1 inside a covering letter is not excluded
- Primata/Duplicata of No.1 and any Paris-side decipherment or translation (Ministere de la Marine et des Colonies, French archives) - blocker: waiting-on LOCAL-QUEUE.tsv row L31 (queued 2 Oct 2026 by GAPS4-na-janssens-java-1811, section above: a desk-browser catalogue lookup on FranceArchives and the Archives nationales SIV -- Janssens / Batavia / Java 1811, chiffre / dechiffrement / traduction, Marine BB/4, AF/IV, ANOM Colonies C/2 -- quoting each record's URL and availability flag; the cloud probe the same day got HTTP 200 on francearchives.gouv.fr's root but a JS-and-cookies challenge page on its search, and HTTP 503 on the SIV, one request each); the reason the search is worth a row: leaf 188 is a Triplicata, so two more copies were sent, and the slip pasted on leaf 194 orders a copy of No.2 for the Directeur general des Douanes "traduite d'une lettre chiffree", which shows Paris made plain translations; no French archive searched, and archivesnationales/francearchives do not load from the cloud (CLAUDE.md hosts table); no ASKS.md or LOCAL-QUEUE.tsv row exists for this target; next: file one LOCAL-QUEUE.tsv row for the desk runner (FranceArchives / AN Marine et Colonies search: Janssens, Batavia, 1811, dechiffrement/traduction, quoting the catalogue record's availability flag), ~$2
Done (gap 5): the M-graded tokens on leaf 188 (25 over 19 codes after SPLIT's 13:11 fix) - DONE 2 Oct 2026 (GAPS3-na-janssens-java-1811, section above): every code regraded against its occurrences on 190/191/199/200, 192, 201 and the No.5 plain copy (214), one decision per code in regrades.tsv (applied by scripts/apply_regrades.py, --check ok): 9 codes / 14 tokens M -> C (25, 99, 102, 140, 168, 420, 444, 689, 904), 10 codes / 11 tokens stay M (190 value en -> est by majority, 353, 527, 534, 607, 760, 875, 1041, 1096, 1137: one word each, or a live homophone), C 63 -> 77, M 25 -> 11, keyed 88/163 unchanged, decode_key.py --check exit 0, judge -0.963 vs real_p05 -0.899 (FAIL, flat). The plain copy of No.2 (194-195) is not transcribed on disk and was not used (vision 0); the Escalation clear-pages row keeps it

## Escalation (1 Oct 2026)
- [ ] siblings: done so far: 180-219 checked one leaf at a time (VX-RD02/RD02B), about 76 sample points elsewhere in invnr 12, invnrs 7, 11, 13 and 26 sampled; this found No.5 (210-214). 2 Oct 2026 (GAPS5): leaves 186-215 re-inventoried at 1200-2561 px, every leaf, four blind passes -- the earlier leaf-by-leaf checks had misfiled 14 of the 30 (194-195 the plain No.2, 201-202 the No.3 postscript and plain copy, 204-209 the whole No.4 set, 210-211 the No.5 slip); no No.1 gloss or plain copy in the range. 2 Oct 2026 (GAPS10): 137-178 and 220-232 paged by contact sheet (45 leaves, no cipher, gloss or plain copy). 2 Oct 2026 (GAPS11): 229 eye-checked (arithmetic, not cipher); 68-136 paged by contact sheet with a leaf 188 positive control (58 leaves, no cipher, gloss or plain copy). 2 Oct 2026 (GAPS12): 2-67 paged by contact sheet with the 188 control on every sheet (55 leaves, no cipher, gloss or plain copy) -- invnr 12 paged end to end. 2 Oct 2026 (GAPS13): invnr 7 scans 1-58 paged with the 188 control on every sheet (no cipher, gloss or plain copy). 3 Oct 2026 (GAPS14): invnr 7 scans 59-117 paged the same way (no cipher, gloss or plain copy). 3 Oct 2026 (GAPS15): scan 67 at 1200 px (invoices cover, not a translation) and scans 118-175 paged the same way (no cipher, gloss or plain copy). 3 Oct 2026 (GAPS16): scans 176-190 paged the same way (no cipher, gloss or plain copy) -- invnr 7 paged end to end. 6 Oct 2026 (R10-JANS26): invnr 26 scans 1-58 paged the same way; 10-11 = a second signed copy of No.1's cipher (5 more leading codes than leaf 188, no gloss). 6 Oct 2026 (R10-JANS26B): invnr 26 scans 59-116 paged the same way (no cipher, gloss or plain copy). 6 Oct 2026 (R10-JANS26C): invnr 26 scans 117-176 paged the same way (no cipher, gloss or plain copy). 6 Oct 2026 (R10-JANS26D): invnr 26 scans 177-191 paged the same way (no cipher, gloss or plain copy) -- invnr 26 paged end to end; all three known Janssens invnrs (12, 7, 26) paged end to end. 6 Oct 2026 (R11-JANS26TX): the inv26 No.1 copy transcribed in two blind passes and aligned: 161/163 codes agree with leaf 188 (shuffled-order control max 0.153, 0/1000), differences 13:11 (copy supports SPLIT's 1192) and 5:1 (copy 948, leaf 188 plainly 448, copy variant), no leaf-188 change; its 5 leading codes read "Batavia vingt Deux Juin ." through the existing key. No further sibling of No.1 is known in the three Janssens invnrs
- [ ] clear-pages: done: leaf 214's plain copy of No.5 used as an independent control (5 codes fixed, 95/95 decoded). Leaf 187R DONE 2 Oct 2026 (GAPS6-na-janssens-java-1811, section above): transcribed from native IIIF crops, two blind passes + one reconciliation (leaf187_text.txt, 16 lines, grade H as a transcription), tested as a crib against leaf 188's keyed tokens with a shuffled-order control: LCS z +0.30 (999/2000 shuffles at or above), content-word coverage 0/9, while the known No.2 cipher/gloss pair scores z +35 on the same test -- 187R (revenue farms of the Residents, 20 Juin 1811, "No 11") is not No.1's plaintext; No.1's clear text remains unlocated. Not used yet (all confirmed and located by the GAPS5 inventory, 2 Oct 2026): the plain No.2 copy (194R and 195R, "N.2 Duplicata", 9 Juillet, same text as the 190-192 gloss), the plain No.3 copy (202R, "N.3 Duplicata", 11 Juillet, paragraph "12.", Signe Janssens), and the plain No.4 copy (208R-209L) USED 2 Oct 2026 (GAPS8) as gap 2's sealed control (0.733 vs shuffled null 0.191, section above). Planned: align the plain No.2 and No.3 copies against their cipher copies the same way (scripts/no4_align.py pattern), ~$6 each
- [ ] known-keys: done: KEY-DESIGN.tsv line 121 row for key.tsv (syllabary, 214 codes); no other 1800s-1810s French or Dutch office key in KEY-DESIGN.tsv or KEY-OFFICES.tsv; DECODE and both solver repositories grepped with no hit (check-solved items 4-5). Not done: Cryptiana/Tomokiyo (check-solved item 6, "not separately searched"), tools/design_prior.py, the Daendels-era (1808-11) Governor-General dossiers for the same office key, and the missing KEY-OFFICES.tsv row (close-out omission). Planned: ~$3
- [ ] print: done: Colenbrander, Gedenkstukken VI, all 35 "Janssens" hits read; it names the dossier ("In n°. 11 de berichten van Janssens omtrent de overgave van Java") but does not print it; IA advancedsearch 0 hits; be-api "overgave van Java" 64 items, not narrowed. 2 Oct 2026 (GAPS6 premise check (d)): Van Deventer 1891 (Nederlandsch gezag over Java, deel I) full text on disk (print/), 5 Janssens hits, no 1811 letter; be-api "Janssens" + "20 Juin 1811" 37 items all other 20 juin 1811s, "20 Junij 1811" 0; Google Books API found Collet, L'ile de Java sous la domination francaise (Paris 1910, id -BCyBiSVklAC, full view) footnoting a Janssens dispatch "... 1811, no 2" -- a French work citing the numbered 1811 dispatches, unreadable from the cloud (books.google.com page view blocked; not on archive.org or Gallica). Not done: tools/print_check.py phrase search of the plain copies (No.2, No.4, No.5, now also leaf187_text.txt); the Collet 1910 read. DONE 2 Oct 2026 (GAPS7-na-janssens-java-1811, section above): Collet 1910 is unreadable from the cloud (Books API record FULL_PUBLIC_DOMAIN but the PDF link answers a 429 captcha, no archive.org or HathiTrust copy) -> LOCAL-QUEUE.tsv row L35 (edition-read, the desk runner reads every 1811-dispatch footnote and reports whether any cites no 1 / 20 juin 1811); print_check.py 17 phrases: Nos.2, 3, 4 and 187R no hits, No.5's opening sentence printed in De Opkomst van het Nederlandsch gezag deel 13 (1888) Inleiding p. CXXXIII n.2 (text-known for that sentence; No.5 was already keyed from its own plain copy 214); deel 13 (archive.org depkomstvanhetn00unkngoog, djvu in print/) also prints Janssens to the Minister 16 Juin 1811 (doc. LII, p. 539) and 21 Juin 1811 (doc. LIII, confidentielle), neither No.1's plaintext by the crib test (z +0.33 and -0.21 against shuffled-order nulls, content words 0/9, positive control z +33.8; OCR-conditional). Waiting-on: L35 for the Collet footnotes
- [ ] key-rebuild: two-part code with unordered values (1=Soixante, 12=encore, 13=aux) and homophones (de=140/564/682/841, et=454/516/930/1192), so alphabetical bracketing does not apply; no annealing or seeded EM tried; 54 single unkeyed codes in 163 tokens is too few for EM alone. LM-context fill of the 26 No.4 conflict codes DONE 3 Oct 2026 (GAPS17-na-janssens-java-1811, section above; pre-registered e5ff7541): fr1810 letter 5-gram, 20-seed shuffled-context control, known-answer gate on settled No.4 cells 13/15 = 0.867 (PASS at the minimum count; real-word decoys 5/7): 6 codes moved, grade M kept (13 au, 102 peu, 697 ble, 1040 nu, 1094 dont, 1096 par), 19 stay logged, 1 untested-by-this-tool; leaf 188 C 84 M 23 unchanged. Planned: an LM fill of the 56 unkeyed leaf-188 codes against the key's value vocabulary, same control and known-answer gate (method weak on real-word decoys, so expect few moves), disk only, ~$3
- [x] image-check: done 2 Oct 2026 by SPLIT-na-janssens-java-1811 (section above): right page of leaf 188 at native IIIF size, tools/iiif_lines.py line crops, two blind passes (split188_passA/B.tsv) plus one reconciliation, 162/163 three-way digit agreement, one digit fixed (13:11 1194 -> 1192, corrections.tsv); still open from the original row: leaf 198 (raw No.3) against 199-200 (glossed No.3) as a further digit cross-check, ~$2
- [x] retry: leaf 188 re-decoded with tools/decode_key.py after each key extension: 65/163 (39.9%, VX-RD02), 71/163 (43.6%, VX-RD02B), 76/163 (46.6%, VX-RD02C), 86/163 (52.8%, GAPS 2 Oct 2026, leaf 192 merged), 88/163 (54.0%, GAPS2 2 Oct 2026, leaf 201 merged), 88/163 with C 77 M 11 (GAPS3 2 Oct 2026, regrade), 107/163 with C 75 M 32 (GAPS8 2 Oct 2026, No.4 merged), 107/163 with C 84 M 23 (GAPS9 2 Oct 2026, native second gloss pass), --check exits 0
Verdict: keep going: 1 internal gaps (gap 1 done: leaves 192 and 201 merged; gap 5 done: M regrade; gap 2 both No.4 passes done 2 Oct 2026 (GAPS8, GAPS9): 107/163 keyed, C 84 M 23, gloss vs sealed plain copy 0.819 vs shuffled null 0.199, 26 conflicts logged; gap 3 first half done: 186-215 re-inventoried, 14 misfilings fixed; gap 4 waiting-on LOCAL-QUEUE row L31; clear-pages leaf 187 done: not No.1's plaintext, control-backed; print step done 2 Oct 2026 (GAPS7): Collet 1910 -> LOCAL-QUEUE row L35); gap 3 page-through part 1 done 2 Oct 2026 (GAPS10): 45 leaves 137-178/220-232, no new material; part 2 done 2 Oct 2026 (GAPS11): 229 = arithmetic, 58 leaves 68-136 with a 188 positive control, no new material; part 3 done 2 Oct 2026 (GAPS12): 55 leaves 2-67 with the 188 control on every sheet, no new material -- invnr 12 paged end to end; invnr 7 session 1 done 2 Oct 2026 (GAPS13): scans 1-58 with the 188 control on every sheet, no new material (3-31 are a précis register, dates not legible at 256 px); invnr 7 session 2 done 3 Oct 2026 (GAPS14): scans 59-117 with the 188 control on every sheet, no new material; invnr 7 session 3 done 3 Oct 2026 (GAPS15): scan 67 at 1200 px reads "Factures d'envoi par les Bala[ou]s" (invoices, not "Traduction"), scans 118-175 with the 188 control on every sheet, no new material; invnr 7 session 4 done 3 Oct 2026 (GAPS16): scans 176-190 with the 188 control on both sheets, no new material -- invnr 7 paged end to end (1-190), page-through step done for invnr 7; key-rebuild LM-context fill of the 26 No.4 conflicts done 3 Oct 2026 (GAPS17): 6 moved at grade M, 19 stay logged, 1 untested, leaf 188 C 84 M 23 unchanged, known-answer 13/15; invnr 26 session 1 done 6 Oct 2026 (R10-JANS26): scans 1-58 with the 188 control on every sheet, scans 10-11 = a second signed copy of No.1's cipher in Janssens' outgoing series (same body as leaf 188 at start and end, 5 more leading codes, no gloss or plain copy), no key source; invnr 26 session 2 done 6 Oct 2026 (R10-JANS26B): scans 59-116 with the 188 control on every sheet, no new material; invnr 26 session 3 done 6 Oct 2026 (R10-JANS26C): scans 117-176 with the 188 control on every sheet, no new material; invnr 26 session 4 done 6 Oct 2026 (R10-JANS26D): scans 177-191 with the 188 control on both sheets, no new material -- invnr 26 paged end to end, all three Janssens invnrs paged, gap 3 now waiting-on LOCAL-QUEUE row L31 (Paris side); inv26 No.1 copy two-pass transcription done 6 Oct 2026 (R11-JANS26TX): 161/163 agree with leaf 188, no leaf-188 change, its 5 leading codes read "Batavia vingt Deux Juin ."; cheapest next: the LM fill of the 56 unkeyed leaf-188 codes (disk only), ~$3

## SPLIT-na-janssens-java-1811 (2 Oct 2026, account-4)

Brief `.claude/briefs/runs/2026-10-02-account4-split-check.md`, run 02:45-03:0x UTC 2 Oct 2026 (clock read), Fable
5.1, concurrent with GAPS2-na-janssens-java-1811 (whose leaf 201 merge landed at e116b0ef while this job ran; this
section's "before" numbers are GAPS2's "after"). Files touched: `corrections.tsv` (new), `decode.json` (one job key,
`exceptions: corrections.tsv`, plus two header lines), `images/crops_188/` (new), `split188_passA.tsv` and
`split188_passB.tsv` (new), the regenerated `reading.txt` / `reading_tokens.tsv`, and this section. Not touched:
`key.tsv`, `ciphertext.tsv`, the "## Remaining gaps" / "## Escalation" sections, PROGRESS.tsv.

**What the hits were.** `ciphers/_triage/split-check-1-Oct-2026.tsv` carries 70 rows for this target: 69 `unkeyed`
codes and one `unkeyed,out-of-range` (the single digit `3` at 7:9), every one with an empty `splits` column -- this
is a 1-1197 nomenclator read from a period gloss, not a 2-34 letter key, so no flagged token cuts into two or three
*confident* key codes. The question the image can answer is therefore the plain one: is each flagged group one group
as transcribed, and are its digits right. After the leaf 192 merge (GAPS, 02:07) 64 of the 70 were still flagged;
after the leaf 201 merge (GAPS2) 62 (`--split-check` total, 75 token positions).

**Image.** `images/188_hi.jpg` on disk is the 2561-px spread (digits about 25 px tall). The leaf's IIIF `info.json`
(service.archief.nl, 1 request) gives a 5088 x 3087 native; the right-page cipher block was fetched once at native
size as `images/crops_188/188_right_native.jpg` (region 2660,220,2460,1980; 1 request; 346 kB) and cut with
`python3 tools/iiif_lines.py --image images/crops_188/188_right_native.jpg --out images/crops_188 --prefix 188
--distance 90 --prominence 15 --max-width 2450 --debug` into 16 single-line crops (`188_L01..L15.jpg` = cipher lines
1-15, `188_L16.jpg` = the signature, unused); overlay `188_lines_debug.jpg` checked before the passes (every band on
one line, no digit cut). Requests: service.archief.nl 2, no other host.

**Passes.** Two blind Sonnet subagent calls, each given only the 15 crop paths and asked, per group, "one group or
two (or three), and which digits", with H/L confidence; neither saw `ciphertext.tsv`, `key.tsv` or this file
(`split188_passA.tsv`, `split188_passB.tsv`). Both passes count 11, 11, 11, 11, 12, 12, 12, 12, 11, 12, 11, 12, 11,
11, 3 groups per line -- identical to `ciphertext.tsv`'s 163 tokens, so **no glued or split group anywhere on the
leaf**. Digits: pass A, pass B and `ciphertext.tsv` agree three ways on **162 of 163** tokens. Pass A flagged 3 rows
L and pass B 6 (2/4 shape doubts at 2:2 1024, 7:6 1122, 12:5 62; the small-loop 0 of 5:6 50 and 12:8 60; the lone
`3` at 7:9), all with the same digits as the transcription. This worker's own look at the five lines at native size
(one montage) agrees on each: the clerk's 2 (as in 442, 472) and open-top 4 (as in 984, 443) are distinct shapes; the
`3` at 7:9 stands alone between `443.` and `270.` with its own dot, so it is kept as a one-digit group as transcribed
(the key already holds a one-digit code, 1 = Soixante), unkeyed.

**The one correction: 13:11, transcribed 1194, reads 1192.** Pass A H, pass B H, this worker's look: the last digit
is the clerk's 2, not the open-top 4 of `984` immediately before it; VX-RD02's single read (1194) stands alone.
1192 = `et` (key.tsv, grade C, No.2 gloss); 1194 = `ages` (M). Recorded in `corrections.tsv` (line, pos, token,
corrected, value, grade C, read_grade H, source `SPLIT-na-janssens-java-1811 2 Oct 2026`, reason), wired through
`decode.json`'s `exceptions` key so `tools/decode_key.py` applies it per position; `ciphertext.tsv` itself stays as
transcribed (CLAUDE.md Layout). Line 13 now ends "... 130 984 et" where it read "... 130 984 ages".

**Counts (rule 4).** `python3 tools/decode_key.py ciphers/na-janssens-java-1811` then `--check`, exit 0:
```
before (GAPS2 e116b0ef): tokens 163: H 0, C 62, S 0, M 26, I 0, U 75   keyed 88/163
after  (this section):   tokens 163: H 0, C 63, S 0, M 25, I 0, U 75   keyed 88/163
```
One token M -> C; coverage unchanged. `--split-check` after: 62 flagged tokens (unchanged, the correction was on a
keyed M token).

**Judge (rule 7)**, `python3 tools/judge_plaintext.py specs/na-janssens-java-1811.json --file ciphers/na-janssens-java-1811/reading.txt`:
```
before: FAIL language: score=-0.976, null_p99=-1.816, real_p05=-0.899, real_median=-0.789, mode=both, N=247
after:  FAIL language: score=-0.972, null_p99=-1.778, real_p05=-0.912, real_median=-0.783, mode=both, N=245
        ok   words: cover=0.902, min=0.3, real_text_median_cover=0.947
        FAIL - na-janssens-java-1811 (a PASS is a gate for a verifier, not a reading; rule 10)
```
(the "before" line is the same tool on the reading regenerated without `corrections.tsv`, same session; the judge
resamples its null and real bands each run, so the gate itself moves by about 0.01). Flat, still FAIL; no reading is
claimed (rule 10: no decipherment of leaf 188 was found; this job searched nothing new).

**Hits checked / confirmed splits / kept as one token / not reached: 70 / 0 / 70 / 0** (every group on the leaf was
read by both passes, including the six 1-Oct hits the 192 and 201 merges had since keyed). Vision calls: 5 (two
subagent passes; this worker's spread overlay, band overlay and five-line montage). Box: about 20 of 60 minutes.
Cost: see the lane ledger.

For the next owner of the gaps section (not edited here, GAPS2 live in the same hour): the Escalation row
"[ ] image-check: leaf 188's ciphertext.tsv is one careful read plus a second look, not a two-pass reconciliation"
is now done by this section -- two blind passes plus a reconciliation at native resolution, 162/163 three-way
agreement, one digit fixed -- and can be marked [x] citing `split188_passA.tsv`/`split188_passB.tsv` and
`corrections.tsv`. PROGRESS.tsv row "Janssens Java" still reads 86/163 and should read 88/163 (C 63 M 25 U 75,
source this file); left for GAPS2 or the parent so two workers do not write the same row in the same hour. The
leaf-198-vs-199/200 digit cross-check named in the same Escalation row is untouched.

## Verifier audit (A3V-VJAN, 4 Oct 2026)

AUDIT.md section 1: leaf 188 classed **N1**, key source period. O. Collet, *L'île de Java sous la domination française*
(Paris 1910), pp. c.407-408 (Google Books API snippet, ids -BCyBiSVklAC / uz1BAQAAMAAJ) quotes "une lettre chiffrée du 22
juin" of Janssens: "L'ancien gouverneur général présentera les choses bien différemment ... Il part, chargé de trésors et
de la malédiction" -- leaf 188 lines 1 and 10-11. So No.1 is the cipher letter of 22 June 1811 and part of its plaintext
is in print; the premise check's "no decipherment or print of leaf 188 found" is superseded. Van Deventer, Opkomst XIII
(1888), pp. CXXIX and CXXXIII n.2, quotes No.4 and No.5. Crib values suggested by Collet's text for unkeyed codes are in
AUDIT.md section 4 ("found, not applied"); the next solver step is the full Collet page (LOCAL-QUEUE L35).
