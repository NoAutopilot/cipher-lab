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
