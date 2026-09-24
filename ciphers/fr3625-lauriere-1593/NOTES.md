blocked

**Edition check (LANE N3 csED2, 24 Sept 2026 16:17 UTC):** hold not lifted -- the named edition (Gomberville's
*Mémoires du duc de Nevers*, 1665) could not be reached via this pass's granted hosts (archive.org, Gallica SRU).
Two substitute sources read in full, both negative for "Laurière" -- see section 2 below. Brief
`.claude/briefs/runs/2026-09-24-lane-n3-csED2.md`.

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
