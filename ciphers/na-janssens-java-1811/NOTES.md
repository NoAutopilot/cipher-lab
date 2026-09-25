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
tokens 163: H 0, C 46, S 0, M 19, I 0, U 98
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

Required by `.claude/briefs/runs/2026-09-25-lane-vx-rd02.md` before this can move past a working draft: a
second subagent, given only `ciphertext.tsv`, the four key-source images and no other file, built its own
key from scratch and decoded leaf 188 independently. Result pending at the time this section was written --
see the addendum below (or a follow-up NOTES.md edit) for the agreement figures; if agreement is below the
threshold the brief implies, this section's grades stand only provisionally.

### Not found / next steps (one-line suggestions, out of this job's scope)

- No "Numero Un" decipherment located in leaves 180-210; a full page-through of the bundle's other ~185
  leaves (only 23% thumbnail-sampled by CS05) could locate one and lift coverage well above 40%.
- Leaf 192 (continuation of the No.2 gloss) was read by eye for structural confirmation only (the
  cer-/ti.fi.é. word-split check) but not two-pass transcribed into `key.tsv` -- doing so would likely add a
  handful more codes to the key, since it continues the same dispatch's vocabulary as leaf 191.
- The 13 M-graded/homophonic codes in `conflicts.tsv` (especially 689, 190, 1195) are worth a closer look at
  the original leaves if a future pass needs higher-confidence decoding of a token keyed to one of them.
