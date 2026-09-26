open

**Hold lifted, LANE N4 scGOM2, 24 Sept 2026:** the genuine seconde partie is Google Books `H2eV4wAmIr0C` (title
page confirmed, distinct from the two Gallica arks which are both Première partie); full-text searched for
"Lauriere"/"Delauriere" and the theatre's place names -- letter absent; see the dated section below.

# Laurière to Nevers, Châlons, 9 July 1593 — BnF fr. 3625 no. 55 (f. 66r)

QUEUE row: CS2-06 (`sources/solver-diffs/2026-09-24-cyphersolver-site.tsv`, LANE N3 scout scCS2, 24 September
2026 — catalogue item 30 at dbourdeau.github.io/cyphersolver/catalogue.html). Check-solved run 24 September 2026
by LANE N3 csCS2b (session_01711qcbvcwvGDsSAtVXwfJB), brief `.claude/briefs/runs/2026-09-24-lane-n3-csCS2b.md`.

## What it is

A letter signed "Laurière" to the duc de Nevers (as governor of Champagne), dated Châlons, 9 July 1593, in clear
French with eight inline cipher runs (86 groups, a mixed syllabic-and-figure nomenclator). D. Bourdeau's own
working folder (`champagne1590/` in his repository, session of 21 September 2026) reads 19 of the 86 groups
(grade C) by applying a 12-entry code table rebuilt from the interlinear-glossed runs of Laurière's sibling
letter of 13 July 1593 (no. 10, f. 10r, same volume): "come", "du ... que", "... que le Roy soit encores",
"... la volonté du pape", "... aussitost", "... que". 67 groups remain unread; the code is syllabic with
unmarked group boundaries, so the twelve anchored values do not extend further without a better alignment of
no. 10's seven glossed runs.

## Six-source search log (24 September 2026)

1. **Tomokiyo (sources/cryptiana/ on disk, `nevers.htm`).** No sentence naming fr. 3625 or Laurière anywhere in
   the local snapshot (grep across `sources/cryptiana/web/*.htm` for "3625", "Lauri" — the only "3625" hit is an
   unrelated Queen's University PDF URL, and the only "Lauri" hits are Napoleon's General Lauriston, a different
   person). Tomokiyo's Nevers-cipher-key catalogue (nos. 1–70 of fr. 3995, per `champagne1590/NOTES.md`) does not
   list fr. 3623 or fr. 3625 at all, so his key list gives no key candidate for this letter either.
2. **Standard printed edition.** Not read this pass. Bourdeau's own search checked only "the Mémoires de Nevers
   index in Tomokiyo's article" (a secondary listing, not the Gomberville 1665 edition itself) and found no
   entry; he did not run a full-text search of Gomberville's *Mémoires du duc de Nevers* (1665, 2 vols; part 1 on
   Gallica `bpt6k6435941k`/`bpt6k8717151d` per his own citation elsewhere) against this letter's clear phrases,
   the way he did for CS2-26 (below). Per this lane's brief (R8 lesson, LANE N3 addition of 24 Sept 2026), an
   edition not actually read for the date does not support "open." **archive.org** (which would let a printed
   edition or the Nevers/Champagne calendars be read and phrase-searched) is held by csED this pass and was not
   available to this worker; WebSearch/WebFetch located the manuscript's BnF catalogue record
   (`archivesetmanuscrits.bnf.fr/ark:/12148/cc500759`, confirming item 55 = f. 66, Laurière, Châlons, 9 July 1593)
   but no printed edition text.
3. **DECODE (sources/decode/) + both solver-repo clones.** No DECODE record found for fr. 3625 no. 55 in the
   local snapshot (grep for "3625" in `sources/decode/records-*-2026-09-24*.tsv`: no hit — the item may not be
   catalogued in DECODE at all). dbourdeau/cyphersolver (shallow clone, 24 Sept 2026): `champagne1590/NOTES.md`
   and `CATALOGUE.md`/`TARGETS.md`/`README.md` give the fullest account (above); verdict there is "open" (read
   only in fragments), citing his own escalation checklist (siblings, clear-pages, known-keys, print, retry all
   done; key-rebuild not done — "a solver that fits group boundaries to the seven glosses ... was named and not
   built"). aaymeloglu/unsolved-ciphers: no hit for fr.3625 in a fresh shallow clone (`grep -ri 3625`, no match).
4. **Web search** ("Laurière" Nevers Châlons 1593 chiffre BnF fr.3625): only the BnF catalogue record surfaces;
   no solution, key or edition text.
5. **Ciphertext confirmed present on the Gallica leaf.** IIIF fetch, gallica.bnf.fr, 24 Sept 2026, 1 request:
   `https://gallica.bnf.fr/iiif/ark:/12148/btv1b52511322v/f143/full/500,/0/native.jpg` (canvas 143 = f.66r).
   Image shows a full page of clear French prose signed "Laurière" with several groups of 2–3-digit cipher
   figures inline (e.g. "347 184 71 285 91... 59 74 23 89 44..."), matching Bourdeau's description and count.
   Leaf: https://gallica.bnf.fr/ark:/12148/btv1b52511322v/f143.item

## Verdict

**Blocked, not open.** No source of the six claims a decipherment of BnF fr. 3625 no. 55, and Bourdeau's own
attempt (deepest single source) leaves 67 of 86 groups unread. But the standard printed edition for the date
(Gomberville's *Mémoires du duc de Nevers*, 1665) was not located or read for this specific letter this pass —
only a secondary index was checked — and archive.org, which could confirm or search it, is not available to
this worker this pass (csED holds the slot). Per the lane rule, that is `blocked`, not `open`: no nomination
line posted. Unblocks when: archive.org access is available to search Gomberville's edition (both tomes) and
any Champagne/Ligue-period calendar for "Laurière" and the letter's read fragments ("volonté du pape",
"encores"), or a worker with a Google Books grant runs the same check (out of this lane's host list).

Credit: D. Bourdeau, cyphersolver, https://dbourdeau.github.io/cyphersolver/ (catalogue item 30; `champagne1590/`
working folder, key table `key_lauriere.txt`), CC BY 4.0 — prior attempt, read in fragments only (not a
solution). S. Tomokiyo, "Undeciphered Historical Ciphers" and Nevers cipher-key catalogue (cryptiana.web.fc2.com).

Not decoded, not transcribed here (out of scope for check-solved). Rule 10: no novelty claim made; this is a
search result, not a verifier's classification.

## Edition check, LANE N3 csED2, 24 September 2026 (IA + Gallica SRU slots)

**Gomberville, *Mémoires du duc de Nevers* (Paris, 1665, 2 vols; the edition this row's own brief names) --
still not reached.** Located on Gallica as `bpt6k6435941k` (Premiere partie) and `bpt6k8717151d` (seconde partie)
via Gallica SRU (`dc.title all "memoires duc nevers"`, 24 Sept 2026), matching the two arks Bourdeau's own working
folder cites. Not on archive.org: `advancedsearch.php?q=creator:Gomberville` (17 hits, none this title) and
`q=title:(nevers) AND date:[1600 TO 1700]` (12 hits, none this title) both checked, 24 Sept 2026. WebSearch finds
only Google Books scans of it (`id=ztkvMWA_yO0C`, `id=H2eV4wAmIr0C`) -- checked both against archive.org's
`bub_gb_<id>` mirror convention (the pattern that worked for Ribier in the Seure edition check): both
`archive.org/metadata/bub_gb_ztkvMWA_yO0C` and `.../bub_gb_H2eV4wAmIr0C` return empty (`{}`), i.e. not mirrored
on IA. Google Books itself is out of this brief's route. Gallica SRU indexes catalogue metadata, not full OCR
text at passage level (a test query "Lauriere Chalons Nevers 1593" surfaced the manuscript's own Gallica image
and BnF catalogue record, not either Gomberville tome -- so SRU cannot confirm presence or absence inside the
volume); IIIF/`.texteBrut` access to actually read the tomes is outside this brief's grant (SRU only). **The
primary named edition remains unread; this alone keeps the row `blocked` per the lane rule.**

**Substitute sources, both read in full, both negative for "Laurière":**
- Berger de Xivrey (ed.), *Recueil des lettres missives de Henri IV*, tome 3, 1589-1593 (archive.org
  `recueil-des-lettres-missives-de-...-henri-iv-tome-3-1589-1593`, djvu text). This is Henri IV's own outgoing
  letters, not third-party correspondence to Nevers, so it was never likely to carry this letter -- read anyway
  since it is the edition this row's brief names for Dinteville/Champagne. `grep -i "Lauri"`: **0 hits.** (It does
  carry several of Henri IV's own letters "A Mons. de Dinteville", relevant to the sibling row CS2-16, not this one.)
- *Les luttes religieuses en Champagne au XVIe siècle: la Ligue* (E. Pérot, 1911, archive.org `lesluttesreligie00pr`,
  djvu text), the Champagne-Ligue regional history named in this row's brief. `grep -i "Lauri"`: **0 hits.**

Neither substitute names Laurière or prints anything from this letter. This does not lift the block (the primary
edition is still unread), but it removes two of the alternate routes the brief named without needing to promote
the row.

Credit: unchanged from the check-solved pass (D. Bourdeau, cyphersolver, `champagne1590/`; S. Tomokiyo). Rule 10:
no novelty claim made.

## Edition check, LANE N3 csGOM, 24 September 2026 (Gallica ContentSearch + IIIF)

Brief `.claude/briefs/runs/2026-09-24-lane-n3-csGOM.md`. Gomberville's *Mémoires du duc de Nevers* (1665) both
arks read directly this pass -- the block does not lift, but the reason is now structural rather than "not
reached."

**Both known Gallica arks are the same volume, "Premiere partie," not a first and second tome.** Gallica SRU
`dc.title all "memoires duc nevers"` (24 Sept 2026, 6 results total for all of Gallica; 2 are this title) confirms
`bpt6k6435941k` (BnF shelfmark FOL-LA23-13 **(1)**, 1028 canvases) is the dc:title-labelled "Partie 1"; `bpt6k8717151d`
(shelfmark FOL-LA23-13 **(A,1)**, 1024 canvases) is a *second physical exemplar of the same Partie 1*, not
"seconde partie" as this row's own citation of Bourdeau's working-folder ark pair implied. Confirmed two ways:
(1) IIIF manifest page-label sequences for both arks run continuously 1-937 with no restart (`bpt6k6435941k`
resets to "1" once, at canvas 82, immediately after the front matter/privilège -- the main text itself never
resets; `bpt6k8717151d` has the same max label, page 937, no reset at all); (2) canvas f82 of `bpt6k6435941k`,
read as an image, is the privilège du roy page itself, dated "dernier iour de Septembre 1665," ending "RECVEIL"
-- the collection of documents that follows is this single physical part.

**Gallica's own OCR search (`services/ContentSearch`) shows this digitized volume's content stops before 1591,
i.e. before either target year.** Query-by-year counts against `bpt6k6435941k`: 1588 -> 17 hits, 1589 -> 2,
1590 -> 2, **1591 -> 0, 1592 -> 0, 1593 -> 0**. "Lauriere"/"Dinteville" -> 0 in both arks (already checked by
csED2; re-confirmed here for `bpt6k8717151d` too, 1 retry after a mid-request connection reset, good-citizen
rule). Laurière's letter (9 July 1593) falls three years past where this digitized part's OCR-findable content
ends.

**No third ark for a genuine "seconde partie" was located on Gallica this pass.** The SRU title search above is
exhaustive for Gallica's own `dc.title` index and returns only these two exemplars of Partie 1; `dc.creator all
"Gomberville"` returns 0 (the record's creator field is "Nevers, Louis de Gonzague... Auteur du texte," not the
editor); the record's linked catalogue ark (`cb31011834g`) 404s as a Gallica document. WebSearch (not fetched,
per this brief's host grant) surfaces Hachette BnF/POD reprint listings (lessaisons.fr, actualitte.com,
decitre.fr) explicitly titled "...Partie 2," confirming a seconde partie was printed and BnF-scanned somewhere,
plus a second Google Books id (`H2eV4wAmIr0C`, distinct from `ztkvMWA_yO0C` already checked and found absent
from archive.org's `bub_gb_` mirror by csED2) that is a plausible candidate for it -- Google Books is this
lane's excluded host (LANE V's), so not opened; flagged for whoever next holds that grant.

**Flag for fr3993-villeroy-1595 (CS2-26, open, nominated, not this row's target):** that row's NOTES.md and
QUEUE.md both state Bourdeau "searched Gomberville... t. 2... via Gallica's own full-text search" with a "no
hit" result treated as the strongest edition check of its batch. Bourdeau's own `nevers1595/NOTES.md` (checked
this pass, github.com, 1 shallow clone, grep only) makes the same claim ("Memoires de Nevers (1665) t. 2, Gallica
full text: ... not found") but cites no ark. Given this pass's finding that no second-tome ark is findable on
Gallica by title, and that both findable arks are copies of the same "Premiere partie" (page-numbering and OCR
year-range both stop before 1591, matching this row's own problem), that "t. 2" search most likely ran against
one of the same two Premiere-partie arks under a mistaken belief it was the second tome -- which would make its
"no hit" true but uninformative about the real seconde partie. Not this row's target to fix; posted to ROOM.md.

**Verdict unchanged: `blocked`.** The volume containing July 1592/1593 (Gomberville's seconde partie) is not
digitized under a separate Gallica ark findable by SRU title search this pass; the two arks that are on Gallica
are structurally confirmed (page numbers, OCR year range, and one page image) to be two copies of a different
part that does not reach these dates. No nomination line posted. Unblocks when: the seconde partie is found on
archive.org, HathiTrust or Google Books (out of this lane's host grant) and searched or read for "Laurière" /
9 July 1593 / "Châlons," or a BnF-catalogue-level check (catalogue.bnf.fr, data.bnf.fr) locates its own Gallica
ark if one exists under a shelfmark this pass's SRU queries did not surface.

Requests this section: gallica.bnf.fr ~14 (ContentSearch x9, SRU x4, IIIF image x2, 1 connection-reset retry),
WebSearch 3, github.com 1 shallow clone (grep only, dbourdeau/cyphersolver). Credit unchanged. Rule 10: no
novelty claim made; this is a search result.

## Edition check, LANE N4 scGOM2, 24 September 2026 (Google Books, genuine seconde partie found)

Brief `.claude/briefs/runs/2026-09-24-lane-n4-scGOM2.md`. Same Gomberville pass as the sibling row CS2-26
(`ciphers/fr3993-villeroy-1595/NOTES.md`, same date, full method there) and CS2-16 (`ciphers/fr3621-dinteville-1592/NOTES.md`);
summarized for this letter here.

**Google Books `H2eV4wAmIr0C` confirmed as the genuine seconde partie** (title page read via
`jscmd=SearchWithinVolume`: PP5 "SECONDE PARTIE", PP6 "TABLE GENERALE DES MATIERES CONTENVES DANS CETTE SECONDE
PARTIE"), distinct from `ztkvMWA_yO0C` (Première partie, the same part as both Gallica arks csGOM already ruled
out). Both `FULL_PUBLIC_DOMAIN`, `ALL_PAGES`.

**Full-text search for this letter's correspondent and place names:**
- "Lauriere": 0 hits. "Delauriere" (nobiliary-particle spelling variant): 0 hits.
- "Chaalons" (period spelling): 10 hits, pp. 237-390 — a dense, genuinely on-topic cluster of Henri IV's and
  Nevers's own 1592-93 correspondence about the Champagne theatre (e.g. p. 306 "Chaalons le 15. de Iuillet 1592.
  Signé HENRY", p. 361 "ne pouuant d'icy aller droit à Langres... pour essayer de conserver cette ville"), i.e.
  the right place and years are printed in this volume, in detail — but none of the ten hits names Laurière.

**Verdict: `open -- Gomberville 1665 seconde partie (Google Books H2eV4wAmIr0C), full-text searched (Lauriere,
Delauriere, Chaalons), letter absent.`** This is a stronger result than csED2's substitute-source check (which
read Xivrey and Pérot, both negative, but never reached Gomberville itself) and than the original csCS2b/csGOM
holds (which had only the wrong tome available): the correct tome is now searched directly, in a section of the
book that is demonstrably about the same place and years, and still gives no hit. Hold lifted; re-nominated (see
ROOM.md and QUEUE.md CS2-06).

Credit: unchanged (D. Bourdeau, cyphersolver; S. Tomokiyo). Rule 10: no novelty claim made; this is a search
result, not a verifier's classification.

Requests this section: 0 additional www.googleapis.com/books.google.com requests beyond the CS2-26 section (same
volume, metadata already fetched there); books.google.com search terms for this row counted in the CS2-26
section's total (~15). No gallica.bnf.fr, HathiTrust, BSB, ONB or archive.org used.

## NX-LAU, 26 September 2026 (LANE NX worker, interlinear alignment attempt on no.10 + key-application control)

Brief `.claude/briefs/runs/2026-09-26-lane-nx-lau.md`. Intake gate already exit 0 (LANE NX orchestrator, 08:45 UTC,
per ROOM.md). This session re-fetched images, re-ran the seven-run interlinear alignment as its own control-gated
cheap test (rule 3), and reports a negative on that test with both numbers.

### 0. Intake extras

- Shallow-cloned `github.com/dbourdeau/cyphersolver` at commit `fc0c9e865d0fae67ca92d19750d2b09ab11972e0` (26 Sept
  2026). `champagne1590/` still reads exactly **19 of 86 groups** of no. 55 (`key_lauriere.txt`, 12 table entries;
  `ct_3625_10_glossed.txt`, `ct_3625_55.txt` match the content already described in this file's own "What it is"
  section above, word for word) — not more than the 19 on file, so no STOP-and-flag needed.
- Shallow-cloned `github.com/aaymeloglu/unsolved-ciphers` at `2495c45e8b94ffbc4f09a085224aa5ebce5cdf9f`. `grep -ril
  "3625\|Lauri"` hit six files, all confirmed false positives on inspection: `forster-1644/lex_old.txt` ("lauriers"/
  "laurier" as ordinary French words, unrelated to Laurière), `catalogue/pares-ranked.md` (PARES description
  numbers `3625361`/`3625389`/`3583625`, unrelated Simancas items about Juan Andrea Doria and Pedro de Mendoza),
  `catalogue/decode-catalog.csv` (DECODE record id 3625 = BL Add MS 32297 f.135, Gazola/Parma/Vienna 1720-21, an
  unrelated item). No genuine hit for this target in either repository.
- Credit: D. Bourdeau, cyphersolver (`champagne1590/`, MIT code / CC BY 4.0 text) for the first attempt (19/86) and
  the 12-entry code table; S. Tomokiyo as already credited above. Copied nothing from Aymeloglu's repo (no licence).

### 1. Images

`python3 tools/gallica_folio.py btv1b52511322v --folio 10` → folio 10: canvas f31 label '10r' 3915x5732 (matches
Bourdeau's own canvas 31). Canvas 143 = f.66r (no.55) already established (check-solved pass, 24 Sept).
`python3 tools/iiif_lines.py --ark btv1b52511322v --canvas 31 --out ciphers/fr3625-lauriere-1593/images --prefix
f10r --debug` → 59 detected lines, 118 crops. `python3 tools/iiif_lines.py --ark btv1b52511322v --canvas 143 --out
ciphers/fr3625-lauriere-1593/images --prefix f66r --debug` → 23 detected lines, 46 crops. Both debug overlays
checked (`f10r_lines_debug.jpg`, `f66r_lines_debug.jpg`) before any pass: line detection is clean on both pages;
f.66r's body text (Monseigneur salutation through "Comendemens come celuy qui...") runs bands 2-18, then a large
blank gap to the closing/signature (bands 19-23, no cipher there). f.10r's seven glossed runs (R1-R7, per Bourdeau's
key_lauriere.txt) fall within bands 2-28 (the rest of the letter, unglossed, was out of scope for this job's
alignment step). Transcription subagents were given only these crop paths (54 for f10r bands 2-28, 34 for f66r
bands 2-18), never a full leaf, per CLAUDE.md Usage 6.

Gallica requests this session: 2 IIIF region fetches (one per canvas, cached to disk after); 1 connection-reset
(`gallica.bnf.fr`, canvas 31 first attempt), one retry after a pause per the good-citizen rule, succeeded.

### 2. Transcription (rule 2, image over transcription)

Two blind Sonnet subagent passes were run on f.10r's 54 crops (bands 2-28) and, separately, on f.66r's 34 crops
(bands 2-18), at most 2 concurrent. Both f.10r passes struggled with the fast secretary cursive outside the cipher
groups themselves (both flagged most connecting prose as low-confidence, and neither confidently isolated a genuine
second/thinner interlinear hand as a "gloss" distinct from the main hand — one pass called one spot on L14 a
possible gloss, unconfirmed; the other found none). The cipher digit-groups and their attached marks were read with
higher confidence by both passes.

Given that, the reconciliation for f.10r's seven runs was done directly from the source crops (not just the two
blind passes), per this brief's "reconcile disagreements from the crops yourself": custom taller crops were cut
locally from the cached full-page image (`src_ark_..._f31_full.jpg`, no extra network fetch) covering each run's
gloss-and-cipher pair at higher context than the tool's tight ink-profile bands allow. This resolved the structural
question the two blind passes could not: **the "interlinear decipherment" on this leaf is not tiny superscript
text — for most runs it is a full clear paraphrase line, in a hand close in size to the main text, inserted as its
own manuscript line immediately above (or in one case squeezed onto a thinner line above) the cipher figures it
glosses.** Direct-image spot checks against Bourdeau's `key_lauriere.txt`/`ct_3625_10_glossed.txt` R1, R3, R4 and
part of R5 confirm his transcription closely (gloss wording and cipher-group digits match at every spot checked,
with only the usual minor digit-reading variants expected in this hand — e.g. this session read "20 197 Δ12y 28‡ 99
15q+ 78 ✗ 375 141 288" for R1 where Bourdeau has "10 197 Δ124 28# 99 159+ 25 ✗ 335 141 288"). Given this
independent confirmation (both blind Sonnet passes plus this session's own direct-image reading agree with
Bourdeau's structure and gloss wording at every spot checked, even where individual digits are read differently),
Bourdeau's seven-run table is used as the reconciled transcription for the alignment step below, credited as
above and reported here as a third witness per this brief, not substituted for our own two-pass-plus-reconciliation
process, which is what actually established that the gloss-line reading is correct.

f.66r (no.55): two further blind Sonnet passes were run on its 34 crops (bands 2-18), independently of the no.10
work above. Both agree closely with Bourdeau's own `ct_3625_55.txt` on the cipher-heavy lines (e.g. both blind
passes and Bourdeau all read line 1 as "347 184P[?]n 285 92[27]# 59[⊥/✗] w32[q] 25 2[4]8 25 26 14‡ 17 59[q]P 49⊥ⱨ
334 107 16", digit-for-digit agreement on all but a handful of positions); confidence was markedly lower on the
connecting plain French, and one pass flagged its own possible mis-split of two crops (L06/L12, L07/L13 read as
near-duplicate content) as an artefact to check rather than a real feature of the page -- a direct check against
this session's own earlier full-page debug read (`f66r_lines_debug.jpg`) confirms the page has each of these
passages only once, so that pass's duplication is a crop-ordering slip on its part, not a second copy of the text.
Neither pass, nor this session's own direct look at the page, found a genuine interlinear gloss on f.66r itself
(only the single word "come" written over the leaf's own first group, already on file, and "n" over one "304",
also already on file) -- consistent with Bourdeau's account (no.55 carries its own two glosses only; the seven-run
gloss table comes from the sibling no.10).

Bourdeau's three files (`ct_3625_55.txt`, `ct_3625_10_glossed.txt`, `key_lauriere.txt`) are copied into
`bourdeau_ref/` with attribution headers (his own commit `fc0c9e865d0fae67ca92d19750d2b09ab11972e0`, cloned above),
per this brief's step 0 ("copy his transcription files only with attribution in the header") -- this session's
alignment inputs (`align/runs.tsv`) are drawn from these files, cross-checked against this session's own two blind
passes plus direct-image spot checks as described above, not copied uncritically.


### 3. Alignment (grade C, no cryptanalysis) — `tools/interlinear_align.py`

**Floor chosen: 0 (every cipher group treated as a word/particle-level code, none as a below-floor single letter),
and why.** This nomenclator's groups are not the 1-3 digit Thurloe-style numerals the tool's `--floor` option was
built around: most carry an attached letter or sign (`54y+`, `56nΔ`, `184y`, `22n27`), and a few are pure signs with
no digits at all (`XX`, `✗`). `classify_token()`'s digit-proportion heuristic (`digitish()`) would otherwise split
these across its `num`/`doubtful`/`clear` branches inconsistently — a pure-sign group like `XX` has zero digits and
falls to `'clear'` (treated as if it were already plain text), and a mixed group like `54y+` falls to `'doubtful'`
(the OCR-repair path, meant for print-scan digit confusions, not manuscript marks) — both of which stop the value
from accumulating cross-run agreement counts at all. Every one of Bourdeau's twelve anchored values is a whole word
or short particle (`que`, `le Roy`, `volonté`, `du`, `pape`, `soit`, `Catholique`, `aussitost`, `Sa Majesté`,
`auroit`, plus the very frequent short particles `le/la/que` and `a/de`) — none is a single letter — so the
word-level (at-or-above-floor) branch is the right model regardless of the digit-classification problem above.
Fix: each of the 87 distinct raw group strings across the seven runs (numeral or sign, whichever) was mapped to a
unique synthetic 3-digit surrogate number (`align/TOKEN_MAP.tsv`, same raw string -> same surrogate everywhere, so
repeated codes still accumulate agreement), and `--floor 0` was used so every surrogate (all >=100) and every
genuine short numeral is "at or above floor" and gets the DP's full 0-14-letter freedom. This is a documented
preprocessing step (`align/build_pairs.py`, committed, reproducible: `python3 align/build_pairs.py align/runs.tsv align/PAIRS.tsv align/TOKEN_MAP.tsv`), not a change to `tools/interlinear_align.py` itself.

`python3 tools/interlinear_align.py align align/PAIRS.tsv align/ALIGN.tsv align/key_align.tsv --floor 0`:
`tokens 109; values 74; {'single': 25, 'single-segment': 45, 'conflict': 14, 'agrees': 8, 'null-or-unaligned': 17}`.
Only three values reach `agrees` (>=2 occurrences, top meaning agreeing every time): `346`->volonté (2/2),
`59`->du (2/2), `XX`->pape (2/2) — exactly Bourdeau's three most solid C-grade entries, recovered here completely
independently (blind DP over the seven (gloss, cipher) pairs, no prior). The DP did **not** independently confirm
`✗`=que (3 occurrences, predicted "le"/"luy"/"ne", no agreement) or `335`=le Roy (only 1 occurrence in this
7-run set, can't be cross-checked) — those remain Bourdeau's reading only within this session's own alignment.

**Second run, seeded with `--prior` from Bourdeau's 12-value table (as this brief also asked, "report both"):**
`align/PRIOR.tsv` maps each of the 8 single-token anchored values (✗, 335, 346, 59, XX, 141, 288, 184y) to its
established meaning as a surrogate-code prior. `load_prior()` only seeds codes with `int(code) < floor`; at
`--floor 0` nothing is below floor, so the seeded run is a no-op by construction — confirmed by diffing
`align/key_align.tsv` against `align/key_align_prior.tsv` (byte-identical). This is an expected consequence of the
floor choice above (justified by the actual word-level structure of the code), not a tool bug; reported here rather
than silently skipped, per rule 7.

**Control (a), known-answer leave-one-run-out**, gate written before running it: mean per-token exact-chunk
accuracy >= 0.60 on values attested at least twice in the other six runs, using Bourdeau's twelve established
values as ground truth (folded/lowercased; the two frequent-particle entries 25 and 26 count a prediction correct
if it matches any of their listed alternatives, le/la/que and a/de respectively, since those are M-graded and
genuinely ambiguous in Bourdeau's own table, not one fixed answer).

| held out | qualifying tokens | correct | accuracy |
|---|---|---|---|
| R1 | 2 | 0 | 0.000 |
| R2 | 3 | 2 | 0.667 |
| R3 | 1 | 0 | 0.000 |
| R4 | 1 | 0 | 0.000 |
| R5 | 3 | 0 | 0.000 |
| R6 | 4 | 1 | 0.250 |
| R7 | 1 | 0 | 0.000 |
| **total** | **15** | **3** | **mean 0.200** |

15 total qualifying tokens (>=5, so this is a real test, not a non-test per this brief's own caveat).
**Gate not met: 0.200 < 0.60.**

**Control (b), shuffled pairing**: the seven gloss texts permuted across the seven cipher lines (derangements only,
no gloss kept with its true cipher line), same leave-one-out procedure, 10 permutations (seed 20260926):
per-permutation mean accuracy 0.000, 0.176, 0.200, 0.000, 0.000, 0.000, 0.118, 0.176, 0.000, 0.176 — **shuffle mean
0.085 over the 10 permutations (range 0.000-0.200)**. The true pairing's 0.200 sits inside the shuffle range, not
"well below" the shuffle floor as this brief's gate (b) asked to see for a real signal — one shuffled permutation
(mismatched gloss-cipher pairing) scored exactly as high as the true pairing. **The true pairing is not
distinguishable from the shuffled-pairing null at this N.**

**Verdict: CONTROL BELOW GATE.** Per this brief's step 4 ("Apply: only if (a) meets its gate"), no key.tsv/decode.json
change is made for no.55 and no `specs/fr3625-lauriere-1593.json` is written this session — there is no new reading
to apply or judge. Bourdeau's 19/86 (grade C, from his own by-hand alignment of the same seven runs) stands
unchanged as the reading on file. Both this session's DP alignment and Bourdeau's own by-hand alignment used the
same seven (gloss, cipher) pairs; the difference is method (automated DP vs. by-eye), and the DP's own
leave-one-out accuracy on those same pairs does not clear a level that would license extending the code table
further than Bourdeau's twelve entries.

Files: `align/runs.tsv` (the seven gloss/cipher pairs), `align/build_pairs.py` (raw-token -> surrogate mapping),
`align/PAIRS.tsv`, `align/TOKEN_MAP.tsv`, `align/ALIGN.tsv`, `align/key_align.tsv`, `align/PRIOR.tsv`,
`align/ALIGN_prior.tsv`, `align/key_align_prior.tsv`, `align/control_lau.py` (the leave-one-out and
shuffled-pairing controls, re-run with `python3 align/control_lau.py`).

### 4. Apply — skipped (gate not met)

Per this brief, step 4 (write key.tsv/decode.json for no.55, specs/fr3625-lauriere-1593.json, judge run) is
conditional on control (a) above meeting its gate. It did not (0.200 < 0.60), so step 4 was not performed this
session. No key.tsv, decode.json, ciphertext.txt or specs/fr3625-lauriere-1593.json was written; no
`tools/judge_plaintext.py` run to paste. Bourdeau's 19/86 (grade C) stands unchanged as the reading on file.

### 5. Next step

The seven-run known-answer leave-one-out control does not clear its own gate (0.200 vs 0.60) and is not separated
from its shuffled-pairing null (0.085 mean, up to 0.200) — this specific cheap test (automated DP alignment of the
seven glossed runs alone, no other information) does not move the target past Bourdeau's 19/86. The next cheap step
per Bourdeau's own escalation checklist and this session's finding is unchanged from before this session: **another
glossed Laurière letter** (more (gloss, cipher) pairs would raise both the training data and the number of
qualifying held-out tokens above today's N=15) or a structural constraint on group boundaries (the syllable/word
lengths are currently free 0-14 letters; a lexicon-constrained beam search over the code's likely entries, the way
Forster 1644's solve used a lexicon rather than free n-gram hill-climbing, per LESSONS.md section 2, is untried).
Status unchanged: `open` (the target's own status line; not touched by this job beyond this dated section).

## NX-LAU2, 26 September 2026 (LANE NX worker, desk search for more glossed Lauriere/Nevers material)

Brief `.claude/briefs/runs/2026-09-26-lane-nx-lau2.md`. Desk search and image look only, per this brief -- no
transcription, no alignment, no cryptanalysis. NX-LAU's own next step (26 Sept, above) named "another glossed
Laurière letter" as the cheapest untried move; this session searched for one and, more usefully, found a
candidate period *key* (rule 3's own framing: "a period KEY in that list would beat any number of glosses").

### Candidates found

| shelfmark | item/folio | ark / canvas | date | cipher? | glossed? | rough count | notes |
|---|---|---|---|---|---|---|---|
| Français 3625 no.10 (known) | f.10r, item 10 | btv1b52511322v, canvas 31 | 13 Jul 1593 | yes | yes | 7 runs (R1-R7) | already on file, NX-LAU's own control target |
| Français 3625 no.55 (target) | f.66r, item 55 | btv1b52511322v, canvas 143 | 9 Jul 1593 | yes | no (2 words only) | n/a | the target letter itself |
| **Français 3632 no.8 (new)** | f.15, item 8 | **not digitized** -- no Gallica ark found (Gallica SRU checked, no hit; finding-aid page carries no `pictoGallica` badge / no `btv1b*` link) | undated in the finding aid (volume spans roughly 1590 to after 1593, per neighbouring items 6 and 46) | yes ("avec chiffre et déchiffrement" per the finding aid's own wording) | **yes, per the finding-aid text** (same "avec chiffre et déchiffrement" construction BnF uses for no.10, which is known-glossed) -- not visually confirmed, no image available | unknown, not viewed | new Laurière-to-Nevers letter, not in either solver repo, not in DECODE's local snapshot (`grep 3632` on `sources/decode/*.tsv`, no hit); a copy-order or archive-visit target (REQUEST.md/ASKS.md), not copy-free |
| **BnF fr.3995 no.57 (Tomokiyo catalogue, new)** | fol.102 | `btv1b525085665` (fr.3995's own Gallica ark, per `nevers.htm`'s intro); no.57's own canvas within that book not resolved this pass | Feb 1593 (endorsement date; the cipher was reused through Aug 1593 per Tomokiyo) | n/a -- this is a **key table**, not a letter | n/a | n/a | **viewed in full**, `sources/cryptiana/web/nevers_no57.png` (fetched this pass, 930 KB, a "mosaicized from three images" composite already on Tomokiyo's own page) -- see below |
| BnF fr.3985 fol.58 (the letter no.57's own key was used on) | fol.58 | `btv1b90606498` (confirmed via IIIF manifest metadata: Shelfmark "Français 3985"), 485 canvases, **no folio labels at all** (same shape as fr.16092 in the CLAUDE.md host table -- needs eye-checked `--anchor` pairs before a specific canvas can be fetched) | 12 Aug 1593 | yes | no (this is the key's *application*, not a second glossed source) | n/a | not viewed this pass (canvas unresolved, kept within the 10-image budget); next worker's first step if pursuing this key |

### The no.57 finding, in more detail

Tomokiyo's `nevers.htm` catalogues BnF fr.3995 no.57 (fol.102, Feb 1593) as: "Substitution by symbols.
Homophones. Figures 1-72 represent two-letter syllables and 73-98 represent double letters. 99-353 represent
words, while 1-69 with an overbar represent provinces and towns. Special symbols represent names." He names its
correspondent as **"Mons. de Laveriere" [Honoré Mauroy La Verrière]** (his own bracketed identification, not an
OCR artefact -- the endorsement itself reads "Mons. de Laveriere" on fol.102v, place "Chartres"), and cites its use
"in a letter from Laveriere to the Duke of Nevers, Poissy, 12 August 1593 (BnF fr.3985 fol.58)."

**This is not confirmed to be the same person as our target's "Laurière."** The names are visually close
("Laveriere" / "Laurière") but Tomokiyo's own gloss treats them as a specific, named individual (La Verrière,
not La Rivière or Laurière), and BnF's finding-aid search (below) returns "Laurière" and "Laveriere"/"La
Verrière" as distinct name-authority entries. Flagging the resemblance, not asserting identity.

What is worth testing, without doing the test here (out of this brief's scope): the *range structure* Tomokiyo
describes for no.57 (short function-word codes at or below 72, full-word codes in 99-353) is compatible on its
face with every one of Bourdeau's twelve already-published (grade C) meanings for fr.3625's own code --
`59`=du, `25`=le/la/que, `26`=a/de (all <=72, the syllable/short-word band) and `335`=le Roy, `346`=volonté,
`141`=soit, `288`=Catholique, `334`, `107` (all in 99-353, the word band) -- with no value from either list
falling outside where the other would predict it. This is a desk-level compatibility check (comparing two
already-published range descriptions), not a new decode of anything, and it is exactly the kind of match rule 3
says to control before trusting: whether fr.3625's cipher *is* fr.3995 no.57, a closely related system reused
across correspondents to Nevers in 1593 (several of Tomokiyo's other entries document exactly that pattern, e.g.
no.36 "Chiffre pour Monsieur de Nevers avec le Roy" used by several senders), or an unrelated coincidence of a
common design convention needs a real test (apply no.57's actual table, read off the same entries Bourdeau's 12
anchors give, and gate against a shuffled/relabelled control per rule 3) before it is reported as anything more
than "worth testing."

Bourdeau's own `champagne1590/NOTES.md` (checked again this pass at the same commit `fc0c9e865d0fae67ca92d19750d2b09ab11972e0`
as NX-LAU used) states he reviewed Tomokiyo's nevers.htm catalogue and tested **no.46** against a different,
unrelated fr.3623 cipher ("does not fit") -- he does not record testing no.57 against anything, and specifically
against fr.3625: no.57 is an untested candidate, not a ruled-out one.

### BnF search method (step 1)

`archivesetmanuscrits.bnf.fr`'s own free-text name search (`POST resultatRechercheSimple.html`,
`TEXTE_LIBRE_INPUT=Lauriere`, per the route QUEUE.md's M22 pass already documented) searches the whole BnF
manuscripts catalogue, not one shelfmark range, so it supersedes this brief's narrower ask (walk fr.3620-3650,
fr.3980-4020, fr.4700s by hand): 33 raw hits, of which exactly three are the 1592-94 Nevers-correspondence sense
of the name (fr.3625 no.10, fr.3625 no.55, and the new fr.3632 no.8 above); the rest are unrelated people sharing
the surname across other centuries (Philippe de Pompadour marquis de Laurière, François Laurière, Dorré de
Laurière's legal treatise, a 1972 reader-letter correspondent, a Louis Bertrand correspondence item). Gallica SRU
(`dc.title`/general queries for "Français 3632", "Français 3985") was used only to check digitization status of
the two new leads, not as a name search (SRU indexes catalogue-title-level metadata, not item-level finding-aid
text, confirmed again this pass -- consistent with NX-LAU's own 24 Sept finding for fr.3625's Gomberville check).

### Step 2 (Bourdeau) and step 3 (Tomokiyo key list)

Both folded into the sections above: Bourdeau's `champagne1590/` names no other Lauriere letter and tested only
no.46 from Tomokiyo's key list; Tomokiyo's own list gives no.57 as a real, previously-unconsidered-for-this-target
candidate key. `gallica_sweep/bnf_candidates.txt` (Bourdeau's own broader keyword sweep across the Colbert/Dupuy/
Ségur/Navarre/Villeroy/Bellièvre/Nevers volumes, checked this pass) has exactly one "Lauri" hit, the same fr.3625
no.55 already on file -- no coverage of fr.3980-4020 or fr.4700s specifically (it is a keyword sweep of SRU hits,
not an exhaustive per-shelfmark walk), consistent with the BnF name-search above being the more complete route.

### Next step

Two independent leads, in order of promise: (1) **test BnF fr.3995 no.57's published table against fr.3625's
known codes** (a real decode-and-gate exercise, rule 3 control included, not a glossed-letter alignment problem
at all -- if it fits, this replaces the whole "find more glosses" approach). This needs no new image: no.57's
table is already on disk (`sources/cryptiana/web/nevers_no57.png`) and fr.3625's ciphertext is already on disk
(`bourdeau_ref/ct_3625_55.txt`, `align/runs.tsv`). (2) If (1) fails, **fr.3632 no.8** is a second glossed Laurière
letter to fold into NX-LAU's leave-one-out alignment (would raise N from today's 15 qualifying tokens), but it is
not digitized -- write a REQUEST.md/ASKS.md row for a BnF copy order or reading-room visit before it can be used.
Status unchanged: `open`.

## NX-LAU3, 26 September 2026 (LANE NX worker, key57 known-answer gate against fr.3625's 12 anchors)

Brief `.claude/briefs/runs/2026-09-26-lane-nx-lau3.md`. Intake gate already exit 0 (08:45 UTC, per ROOM.md). This
session tests NX-LAU2's candidate period key (BnF fr.3995 no.57, fol.102-103) against fr.3625's own established
code meanings, per rule 3's known-answer gate, and reports a **negative on the transfer test with both numbers**.
No.55 is not decoded further and no novelty claim is made (rule 10).

### 0. Correction to NX-LAU2's folio pointer

**Fol.102 is not the key table.** Placed with `python3 tools/gallica_folio.py btv1b525085665 --folio 102`:
canvas f196 = 102r, f197 = 102v. Eye-check against both canvases (fetched at 800px for a first look, then full
native res) shows fol.102r carries only an endorsement date ("fevrier 1593") and fol.102v only the address/docket
("A Mons... de la Verriere / chiffre des affaires de..."), both otherwise blank -- this is the *outside* of the
folded key sheet (the address written on the back, as letters of the period were folded and addressed on the
verso), not the table itself. The actual key table -- the same one mosaicked into
`sources/cryptiana/web/nevers_no57.png` -- is the *unfolded interior* of that same physical sheet, digitized by
Gallica as an oversized fold-out across four canvases that all carry the manifest's own duplicate label "103r"
(the offset table's own "DUPLICATE label '103r' on f198 and f199" / "on f198 and f200" already flagged this,
per CLAUDE.md's `tools/gallica_folio.py` precedent for fr.16092-style eccentric foliation): **f198, f199, f200 =
recto "103" in three overlapping horizontal strips (syllables/double-letters/word-bank columns, left to right);
f201 = a further sheet, also labelled "103", carrying the special-symbol table for names and titles (Le pape,
Le Roy, the dukes and cardinals -- "special symbols represent names" per Tomokiyo); f202 = blank/bleed-through,
not part of no.57's own key at all (a different, later document bound nearby, dated 1592, "Suisse").** This is a
deviation from the brief's "the key leaf (fol.102, perhaps fol.102v too)" instruction, made necessary by what the
images actually show; the brief's assumption (inherited from NX-LAU2's fol.102 citation, itself following
Tomokiyo's own "fol.102" shorthand for the whole sheet) undercounted the leaf by one full folio. Recorded here so
a successor does not re-fetch fol.102 expecting a table.

Gallica requests this session: 2 IIIF region fetches at 800px (f196, f197, 1 connection reset + 1 retry, good-
citizen rule), 5 more at 800px (f198-f202, 1 reset + 1 retry), 4 at 2000px native (f199, f200, f198, f201, 1 reset
+ 1 retry) -- 11 total, all 1.5s+ apart, all eventually HTTP 200.

### 1. Images and crops

Given the leaf is an oversized 4-canvas fold-out (not a leaf of ordinary running prose), `tools/iiif_lines.py`'s
row-ink-profile line detector is built for lines of text, not a multi-column numbered table, and running it
unmodified across four ~2000x3000px canvases risked exactly the unit-mispricing this repo's Usage section 6
warns against (a call sized to outlive its box). Given the box (120 min) and the call budget (~12 calls at ~USD
1.5), this session instead cut the crops needed for the 12 anchors directly with PIL from the cached 2000px-wide
canvas images (no extra network calls), reconciled per-cell against the systematic row/column structure visible
in the full-canvas images, and gave a blind subagent the same crop paths for a second read -- the same
"reconcile from crops yourself, subagents get crop paths only" method NX-LAU used on f.10r when the tool's line
detector did not fit the material. Crops: `crop_syllables_zoom.jpg`, `crop_syllables_zoom2.jpg`,
`crop_101_103.jpg`, `crop_141_zoom2.jpg`, `crop_288_wide3.jpg`, `crop_184_zoom4.jpg`, `crop_335_346_v2.jpg`,
`crop_346_v2.jpg`, `crop_doubles.jpg`, `crop_199_232_{top,bot}.jpg`, plus the full canvases `f198_hi.jpg`,
`f199_hi.jpg`, `f200_hi.jpg`, `f201_hi.jpg` for the special-symbol table and as context for the tighter crops.

### 2. Transcription (`key57/key57.tsv`)

**Pass A** (this session, direct read from the crops above, cross-checked against the systematic 14-consonant x
5-vowel structure of the syllable table, which is internally self-consistent and lets a misread cell be caught
immediately). **Pass B**: one blind Sonnet subagent, given only the same crop paths and a list of code numbers to
read (never told pass A's answers), asked to report the word next to each number with no interpretation. ~104
numeral-table entries transcribed (syllables 1-72 partial, double letters partial, word bank 99-353 sampled
across ~190 codes including all 12 anchor codes) -- not the full ~353+72+26-entry table (out of scope once the
gate result was clear; every anchor code itself is covered). `key57.tsv`: code, meaning, class, crop, per-cell
pass agreement.

**Agreement on every anchor-bearing cell**: passes A and B agree exactly on 25=que, 26=re, 54=ro, 56=to, 99-104
(a/aux/au/au/aussy(auffz)/art), 141=catholique, 183-184=estre/est, 335=soit, 346=volonté ou vouloir. Two cells
disagree in wording but agree on the verdict that matters (neither reads the fr.3625 target word): 288 (pass A
"Noua", pass B "Nous" -- neither is "Catholique"); 337 and 347 (spelling variants, not anchor codes). XX = "le
pape ou sa saincteté" confirmed by both the initial full-canvas read and the blind pass, on `f201_hi.jpg`'s own
name/title symbol list. The blind pass also independently confirms **the "✗" (que) symbol used in fr.3625 and in
Bourdeau's own key_lauriere.txt has no counterpart anywhere in no.57's special-symbol table** -- that table pairs
symbols only with proper names and titles (popes, kings, dukes, cardinals), never with a common word, and a full
page read (both columns) found no plain-X-for-"que" entry.

### 3. Known-answer gate (rule 3), written before comparing

**Anchors** (12, per key_lauriere.txt's Table, `bourdeau_ref/key_lauriere.txt`): ✗=que (C), 335=le Roy (C),
141=soit (M), 288=Catholique (M), 346=volonté (C), 59=du (C), 25=le/la/que (M), 26=a/de (M), "103 56nΔ"=aussitost
(M), "101 54y+"=Sa Majesté (M), 184y=auroit (M) -- 12 entries total (5 grade C, 7 grade M), matching NX-LAU's own
count and use of this same table as ground truth. Normalisation: lower-cased, accents stripped, "x ou y" cells
split into alternatives, a match counted if key57's meaning equals fr.3625's word or one of its listed
alternatives (rule 3, PX-BRODEC normalisation lesson). Compound two-code anchors (Sa Majesté, aussitost) require
both component codes to match their component word for that anchor to count (a conservative rule; loosening it
to "either code matches" would not change today's result -- neither component matches for either compound).

**Statistic: number of anchors whose key57 meaning matches fr.3625's established meaning.**

| anchor | fr.3625 meaning (grade) | key57 meaning | match? |
|---|---|---|---|
| XX | pape (C) | "le pape ou sa saincteté" | **MATCH** |
| 59 | du (C) | "Du" (syllable) | **MATCH** |
| 346 | volonté (C) | "volonté ou vouloir" | **MATCH** |
| 25 | le/la/que (M) | "Que" (syllable) | **MATCH** |
| 335 | le Roy (C) | "soit" | mismatch |
| 141 | soit (M) | "catholique" | mismatch |
| 288 | Catholique (M) | "Noua"/"Nous" (passes disagree, neither is Catholique) | mismatch |
| 26 | a/de (M) | "Re" (syllable) | mismatch |
| 184y | auroit (M) | "Est" | mismatch |
| 101+54y+ | Sa Majesté (M) | "Au" + "Ro" | mismatch |
| 103+56nΔ | aussitost (M) | "Aussy" + "To" | mismatch |
| ✗ | que (C) | not present in key57 (no plain-X "que" symbol anywhere on the sheet) | mismatch |

**Real statistic: 4 of 12.**

**Control**: 1000 shuffles of key57's own transcribed meanings over its own codes (`key57/control_key57.py`,
`python3 control_key57.py` reproduces it, seed 20260926) -- the 104-entry numeral pool shuffled for the 10
numeral-table anchors, a separate Bernoulli(1/73) draw per shuffle for the XX anchor (73 = the counted number of
distinct title-to-symbol rows on `f201_hi.jpg`'s own two columns, the population XX would have to beat by chance),
the que-mark anchor fixed at 0 (it cannot match under any permutation, since no cell for it exists in either
table). **Shuffle mean 0.072, p99 1, max 2** (out of 1000 shuffles).

**Gate: target at or above 6 of the anchors AND above the shuffle max.** 4 is above the shuffle max (2) --
the match is not pure noise -- but 4 < 6. **GATE NOT MET.**

Per class: syllable band (25, 26, 54, 56, 59) 2/5 match; word band (101, 103, 141, 184, 288, 335, 346) 1/7 match;
special-symbol band (XX, ✗) 1/2 match. The word band is the discriminating one (rule 3, AX-NAMES) and it is the
weakest: 1/7, on the two most solidly attested C-grade word-band anchors (335=le Roy, 346=volonté) split one
match and one clean mismatch.

### 4. Apply -- skipped (gate not met)

Per this brief's step 5: key57 is not this letter's key. No key.tsv/decode.json/ciphertext for no.55, no
`specs/fr3625-lauriere-1593.json`, no judge run -- there is no reading to apply or score. Bourdeau's 19/86 (grade
C) stands unchanged as the reading on file. Status unchanged: `open`.

### 5. Reading the result

This is a real, above-chance partial overlap (4 beats a shuffle max of 2), not zero -- most plausibly because
this cipher office's key sheets for different Nevers correspondents in 1593 shared the same syllable-table
*template* (the same 14-consonant x 5-vowel numbering convention, which is why 25=que and 59=du land in the same
place in both fr.3625's and no.57's systems) while assigning the *word bank* independently per correspondent
(which is why le Roy/soit/Catholique/aussitost/Sa Majesté/auroit/a-de all disagree). That is a plausible and
interesting structural observation about the office's key-issuing practice, worth naming for a successor, but it
is not evidence that no.57 is fr.3625's own key, and the brief's gate (>=6 of 12, word-band anchors doing the real
discriminating) correctly says so. Not a NEAR.md candidate (rule 5): this is a negative on the key-identity
question with a passed, informative control, not a solver beating a control on an actual decode.

### Next step

fr.3625 no.55 remains unread beyond Bourdeau's 19/86. NX-LAU's own next step stands: fr.3632 no.8 (a second
glossed Laurière letter, not digitized, needs a REQUEST.md/copy-order row) would raise the leave-one-out alignment
N past today's 15 qualifying tokens; a lexicon-constrained beam search over the code's likely word-bank entries
(per Forster 1644's precedent, LESSONS.md section 2) is untried. Testing further Tomokiyo-catalogued Nevers keys
against fr.3625 (no.57 was the only untested one on Bourdeau's own list; his own next candidate would need a fresh
desk search of `nevers.htm` for still-untested entries) is a third option, cheap since the syllable-table
convention this session found shared across at least two correspondents suggests more of these keys share it,
even where the word bank differs. Status unchanged: `open`.

Credit: S. Tomokiyo, "Catalogue of Ciphers (Mainly Related to Duke of Nevers) in BnF fr.3995"
(cryptiana.web.fc2.com/code/nevers.htm) for the no.57 catalogue entry and the correspondent identification; D.
Bourdeau, cyphersolver (`champagne1590/key_lauriere.txt`), CC BY 4.0, for the 12-entry anchor table this session
tested against. Rule 10: no novelty claim made; this is a controlled negative on a key-identity test, not a
reading of no.55.

Files: `ciphers/fr3625-lauriere-1593/key57/{f198_hi.jpg,f199_hi.jpg,f200_hi.jpg,f201_hi.jpg,f10*_eyecheck.jpg,
f19*_eyecheck.jpg,f20*_eyecheck.jpg,crop_*.jpg,key57.tsv,control_key57.py}`. No `specs/fr3625-lauriere-1593.json`
written (gate not met, no reading to spec). Stopping per brief -- the orchestrator sends a fresh re-derivation.

Requests this session: cryptiana.web.fc2.com 2 (1 reachability check, 1 image fetch, both HTTP 200, 1.5s+ apart);
archivesetmanuscrits.bnf.fr 6 (1 reachability re-check of the fr.3625 record, HTTP 200; 2 failed attempts at the
bare site root, `ws_closed_mid_exchange` tunnel resets per `/__agentproxy/status`, one retry per the good-citizen
rule, not pursued further since the deep-link routes worked fine; 1 search POST, HTTP 200; 2 attempts at the
fr.3632 record, 1 tunnel reset + 1 retry succeeded, HTTP 200); gallica.bnf.fr 4 (3 SRU queries, 1 IIIF manifest
fetch, all HTTP 200, 1.5s+ apart); github.com 1 shallow clone (`dbourdeau/cyphersolver`, grep only, deleted after
use). No aymeloglu/unsolved-ciphers clone this pass (NX-LAU already re-checked it this session's window and
found nothing for this target; re-cloning it again added nothing new to search for a name query that repo's own
earlier grep already covered).

Credit: S. Tomokiyo, "Catalogue of Ciphers (Mainly Related to Duke of Nevers) in BnF fr.3995" (cryptiana.web.fc2.com/code/nevers.htm)
for the no.57 catalogue entry and key-table image; D. Bourdeau, cyphersolver (`champagne1590/`), for the prior
key-list review this session cross-checked. Rule 10: no novelty claim made; this is a search result, listing
candidates for a future worker, not a reading.

## NX-LAU4, 26 September 2026 (LANE NX worker, sibling key-sheet search across fr.3995's other 1592-1594 keys)

Brief `.claude/briefs/runs/2026-09-26-lane-nx-lau4.md`. NX-LAU3's own next step: since fr.3995 no.57 (Feb 1593,
La Verriere) beats its shuffle floor on the 12 gloss anchors (4/12, shuffle max 2) but misses the 6/12 gate, and
the mismatches look like a *renumbered word bank of the same office* (key57 has 335=soit/141=catholique where
fr.3625 has 141=soit/288=Catholique), this session tests whether any OTHER 1592-1594 key in Tomokiyo's fr.3995
catalogue is fr.3625's true sibling key. Intake gate already exit 0 (per LANE NX orchestrator, 08:45 UTC, per
ROOM.md). Result: **negative on all four sheets tested, and the "shared syllable template" hypothesis itself
does not survive a wider look at the catalogue** -- see "Reading the result" below.

### 1. Candidate list (`keysib/candidates.tsv`)

`sources/cryptiana/web/nevers.htm` (Tomokiyo's catalogue of fr.3995 nos.1-70) was read in full (`/tmp/nevers.txt`,
a plain-text extraction, `grep -n "^### no\."` for the index, then every entry dated 1592-1594 read individually).
**No entry other than no.57 gives the specific "figures 1-72 represent two-letter syllables... 99-353 represent
words" range breakdown** -- a `grep -i "syllable\|1-72\|73-98\|99-35"` across the whole catalogue file confirms
no.57's own line (697) is the only hit with that structure. Candidates were therefore ranked by a looser design
family (a French-language, homophone-plus-nomenclator numeral cipher, not Italian/Spanish, not an intercepted
third-party letter) and by closeness to Champagne/Chalons and to July 1593, per the brief's step 1: no.58
(fol.104, Jul 1593, same month as the target letter), no.60 (fol.108, Aug 1593, given to the Duke of Nevers
himself, used in many fr.3985 letters -- the same volume as no.57's own application letter), no.45 (fol.84, Aug
1592, Provins -- a historic Champagne fair town), no.61 (fol.112, Oct 1593, Andre Hurault de Maisse to the Duke
of Nevers), no.66 (fol.122, Mar 1594, conceptually closest to no.57's tiered structure per its own catalogue
text: "symbols for double letters, nulls, and monosyllables... names by special symbols"). Excluded outright:
no.46 (Bourdeau already tested, "does not fit," per this job's own brief); no.57 (NX-LAU3, already tested);
Italian/Spanish-language entries (47,52,53,54,56,59,62,63,64,67); intercepted third-party-letter ciphers
(48,50,51, issued between enemies of the Nevers office, not by it); no.70 (dated 1595, outside the window).

### 2. Locating each table on the Gallica manifest (`btv1b525085665`, fr.3995)

Per NX-LAU3's own finding for no.57 (docket folio N recto = the address/outside of a folded sheet; the table
itself is the *interior*, usually the very next canvas), `tools/gallica_folio.py` located each docket folio, then
the manifest (`sources/gallica-manifests/btv1b525085665.json`, cached after the first `gallica_folio.py` call --
folios 85, 84, 112, 113, 122, 123 all read from that cache, 0 further manifest fetches) was read directly for the
canvas immediately after, which turned out to carry a combined label confirming the fold-out interior in every
case tested: f203 "104v-105r" (no.58), f166 "84v-85r" (no.45), f235 "122v-123r" (no.66). No.61 (fol.112) does
**not** follow this pattern -- f215/f216/f217 are three separate canvases ("112r"/"112v"/"113r"), no combined
fold-out label -- its table turned out to be the ordinary recto f217 ("113r"), a single normal-sized page, not an
oversized sheet like the other three.

### 3. What each table actually is (eye-check first, per rule 2 -- image over transcription)

Each candidate's own table image was read directly (this session) and cross-checked by one blind Sonnet subagent
given only the crop paths (never told this session's own readings), per the brief's "two readers" instruction.
Crops: `keysib/imgs/{f203_syllables,f203_wordbank,f166_q4,f217_1400,f235_1400}.jpg` (full-canvas eye-check images
for f209/f216/f166/f203 at 1200-2400px were fetched, read, and then deleted after their content was established,
to keep the target folder under the 30 MB line -- CLAUDE.md Access playbook).

**No.58 (fol.104, f203, "104v-105r"):** a genuine numeral table -- a syllable grid across columns A-Z (two rows of
numbers per column, values running only **0-46**, confirmed by both readers) and a separate word list running
**99 down to 45/49** ("Pape"=99, both readers agree; "Marquis du Pont"=49 this session's own read, or "Comte de
grand pre"=45 by the row just below it -- either way the list bottoms out in the mid-to-high 40s). This key's
entire number space (0-99) is smaller than fr.3625's own code range (which needs at least 346). **Eight of the
twelve anchors (101, 103, 141, 184, 288, 335, 346, and the que-symbol) fall outside this key's number space by
construction** -- there is no cell for them to compare against, at any value. Of the remaining four (25, 26, 54,
56, 59, all inside the 0-46/49-99 space), the word-bank half (49-99) is exclusively noble titles/names (Pape, Roy,
Duc de Savoye, ...), never a common function word like "du" -- so even 59 cannot be "du" by class, whatever its
exact cell reads. **Maximum achievable score under this design is well below the 6/12 gate; no shuffle control
was run, since a control cannot discriminate when 8 of 12 comparisons have no cell to compare (the AX-5799/bCAS
non-test shape, CLAUDE.md rule 3) -- the disqualification is the range mismatch itself, reported here as the
concrete evidence rather than forced into a shuffle-gate frame that would test nothing.**

**No.66 (fol.122, f235, "122v-123r"):** a small (~24-entry) table where **every name is coded by a single SYMBOL
or mark, not a number** -- "le Pape --", "le Roy --", "sa Mte --" are each followed by a distinct glyph (a cross-
like mark, a circle-like mark, a T-shaped mark), confirmed independently by the second reader ("None of the three
is a plain multi-digit number -- each is a single symbol or character"). There is no word-bank tier here at all
for common words (que/du/soit/volonte/aussitost/auroit) -- the design (per Tomokiyo's own catalogue text,
confirmed by this eye-check) is symbols-for-names plus a separate letter-homophone alphabet and Doubles/Nulles
lists, structurally incompatible with fr.3625's numeral word-bank. Excluded on design-class grounds, no gate run
for the same reason as no.58 (nothing to compare numerically).

**No.61 (fol.112, f217, "113r," the "Tour de Chiffre"):** a 1-99 numbered table, but **the great majority of
codes 12-29 are single-letter homophones** (12=f, 13=s, 16=B [confirmed by both readers, though this session
initially misread this cell as "s" before the second reader's independent count of letters caught it], 17=x,
20=t, ...), used to spell arbitrary words letter-by-letter, interleaved with a much smaller set of proper-name
codes (1=Empereur, 2=Roy d'Espagne, 4=Pape, 16=Roy [name], ...). **There is no single-code tier for whole common
words at all** -- "que", "du", "soit", "volonte", "aussitost" and "auroit" would each have to be spelled out
letter by letter in this design, not looked up as one code the way fr.3625 does. Excluded on design-class
grounds, same reasoning as no.58/no.66.

**No.45 (fol.84, f166, "84v-85r"):** the richest table of the four -- three tiers (a numeral "Villes" list up to
~199; a "Noms particuliers" tier using mixed letter+roman-numeral-like codes, e.g. "Roy d'Espagne" read as
something like "I", "Duc de Lorraine" as "fn," not plain integers; and a "Mot comuns" [sic] tier of ordinary
function words, numbered **alphabetically within each letter block** rather than as scattered independent codes).
This last tier is the one structurally closest to fr.3625's own "que/du/soit" single-code words, so it is the one
concrete anchor this session could actually compare: **"Que" in the Q column reads a number in the low-30s to
low-70s range (this session read ~31; the second, independent reader read ~71, genuinely unable to resolve the
tens digit at this resolution -- but both readings disagree with fr.3625's own 25 (or the que-symbol) regardless
of which is correct).** 0 of 1 concrete anchor checked matched; the per-letter-alphabetized construction (Q-words
numbered together in the 30s-40s, S-words in the 30s-60s, T-words in the 60s-70s, V-words in the high 70s-80s,
per both readers' partial counts) is also a different construction from fr.3625's/no.57's scattered single-purpose
codes, independent of the "que" mismatch.

### 4. Reading the result

**None of the four tested sheets is fr.3625's sibling key, and none shares no.57's own specific design either.**
This is a stronger, more informative negative than a per-sheet shuffle-gate table would have been: the four
sheets actually surveyed cover three genuinely different code families within the same volume and the same
1592-1594 window (a small 2-digit name-only table [no.58]; a symbol-for-names table with no word tier [no.66]; a
homophone-letter table with no word tier [no.61]; a rich multi-tier alphabetized dictionary [no.45]) -- **the
office did not use one shared template across its 1593 Nevers correspondents.** NX-LAU3's "renumbered word bank
of the same office" hypothesis (motivated by no.57's own partial, above-chance overlap with fr.3625) is not
corroborated by this wider search: no other sampled key even shares no.57's *shape* (syllable-grid-plus-word-bank
running into the 300s), let alone its specific numbering. The most that can be said is that no.57 itself remains
the single best partial match on file (NX-LAU3's 4/12 against a shuffle max of 2); this session did not find a
better one, and the pattern it was sent to test for ("shared syllables, renumbered words," holding across
sheets) **does not hold** across the four sheets actually read.

### 5. Apply -- not run (no candidate reached the point of a decode)

Per this brief's step 3/4: no sheet passed a 6/12 gate (none of the four reached a state where that gate was even
computable in the normal sense -- see per-sheet notes above), so no key.tsv/decode.json/ciphertext/spec was
written for no.55, and no.55 is not decoded further. Bourdeau's 19/86 (grade C) stands unchanged as the reading
on file. Status unchanged: `open`.

### Next step

The office-template hypothesis from NX-LAU3 is now the weaker of the two remaining leads, not the stronger one --
this session's four-sheet sample argues against a repository-wide shared design, though it cannot rule out that
no.57 specifically (the one sheet with an above-chance partial overlap) is still worth a closer, non-anchor-only
read (e.g. checking whether *more* of fr.3625's 19 already-read tokens beyond the 12 table anchors land on
plausible no.57 cells). Untested from `candidates.tsv`: no.60 (fol.108, eye-checked only via f209 at the earlier
scoping stage -- visually the same symbol-based family as no.66, not worth a fifth full test) and no.65 (fol.120,
Mar 1594, Grenoble -- Tomokiyo's "two figures per entry" wording implies the same 2-digit cap problem as no.58,
and it is geographically and temporally the furthest of the untested candidates). The two options named by
NX-LAU2/NX-LAU3 remain open: fr.3632 no.8 (a second glossed Laurière letter, not digitized, needs a REQUEST.md/
copy-order row) and a lexicon-constrained beam search over fr.3625's own code (Forster 1644 precedent, LESSONS.md
section 2). Status unchanged: `open`.

Credit: S. Tomokiyo, "Catalogue of Ciphers (Mainly Related to Duke of Nevers) in BnF fr.3995"
(cryptiana.web.fc2.com/code/nevers.htm) for the catalogue entries and key-table images; D. Bourdeau, cyphersolver,
for the prior key-list review and the 12-entry anchor table this session compared each candidate against. Rule
10: no novelty claim made; this is a controlled negative on a key-identity search across four candidates, not a
reading of no.55.

Files: `ciphers/fr3625-lauriere-1593/keysib/{candidates.tsv,imgs/f203_syllables.jpg,imgs/f203_wordbank.jpg,
imgs/f166_q4.jpg,imgs/f217_1400.jpg,imgs/f235_1400.jpg}`. No `specs/fr3625-lauriere-1593.json` written (no
candidate reached a scoreable state). Stopping per brief.

Requests this session: gallica.bnf.fr ~11 (1 manifest fetch via `tools/gallica_folio.py`'s first call on this ark
+ 1 redundant direct manifest fetch of the same file for python parsing, both HTTP 200; folio lookups for 85, 84,
112, 113, 122, 123 all served from the resulting cache, 0 further manifest requests; 9 IIIF image region fetches
at 1200-2400px across f203, f209, f166, f216, f235, f217, all HTTP 200, no 429/403, no retries needed, spaced
1.5s+ apart). 1 Sonnet subagent (the second-reader cross-check on five crops, one call). cost: see the lane
ledger.
