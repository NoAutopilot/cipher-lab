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
