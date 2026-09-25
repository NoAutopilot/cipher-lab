open
Jean Le Clerc, *Négociations secrètes touchant la paix de Munster et d'Osnabrug* (1725, tomes III-IV,
archive.org negociationssecr03lecl/04lecl, both read in full via djvu text and grepped by this worker; the
job brief's own named edition family for this target), control "Servien" 175 hits in tome IV confirming
readable OCR for exactly this 1648 period; zero hits for "Mercy" or "Barneton" in either tome. Acta Pacis
Westphalicae itself, the job brief's other named source, is structurally incapable of covering this item: its
own "Über die Acta Pacis Westphalicae" page states the French correspondence (Serie II B) is "zur Zeit erst
bis zum 19. Mai 1648" published (currently only as far as 19 May 1648), and the target letter is dated 6 June
1648 -- three weeks past the edition's own current end date (see follow-up section below).

### Standard-edition follow-up (LANE CX, 25 Sept 2026)

Job brief's other named source, **Acta Pacis Westphalicae, Serie II Abteilung B**, for 1648 (job brief: "vol.
7 or 8, whichever covers June 1648"). Reached via the browser tool at `apw.digitale-sammlungen.de` (curl hits
the site's Anubis bot-challenge; same fetch method used for clair571-estrades-1645 in this same batch, see
that NOTES.md for the tool syntax).

1. **No volume 7 or 8 exists, digitised or (currently) published.** The site's own volume list under "Serie
   II: Korrespondenzen -> Abteilung B: Die französischen Korrespondenzen" runs only **APW II B 1 through
   APW II B 6** (`/search/start.html?tree=002:002` -- checked directly, 8 sub-nodes total: B1, B2, B3.1, B3.2,
   B4, B5.1, B5.2, B6). A search restricted to APW II B 6 (facet `titleAPW_str=APW+II+B+6`) confirms its own
   documents are dated **1647** (e.g. doc. 21, "[Brienne] an Longueville und d'Avaux, Amiens 1647 Juli 6"; doc.
   157, "Servien an Brienne, [Münster] 1647 September 17") -- i.e. B6 = 1647, not 1648, and there is no B7/B8
   at all on this site.
2. **The project's own static page confirms this is not a digitisation gap but a publication gap.**
   `apw.digitale-sammlungen.de/apw/static.html` ("Über die Acta Pacis Westphalicae") states in its own words:
   *"die französische Korrespondenz liegt zur Zeit erst bis zum 19. Mai 1648 vor"* -- "the French correspondence
   [edition] currently extends only to 19 May 1648." The target instruction is dated **6 June 1648**, i.e.
   roughly three weeks **after** the point the published critical edition of the French correspondence
   currently reaches. APW II B for June 1648 does not yet exist to be opened, in any format, from any host.
3. This is a clean structural negative, not an access block: no route (curl, browser, login, a different
   mirror) would find this item in APW, because the edition itself has not been written that far yet. It also
   means Le Clerc's *Négociations secrètes* (already read, this NOTES.md's opening lines) and APW are the two
   editions the job brief named for this target, and both are now closed out -- Le Clerc by direct negative
   read, APW by this structural gap.

Requests this section: apw.digitale-sammlungen.de -- reused this batch's browser-tool session pattern; 2 fresh
fetches (the Serie II B volume-list page, the "Über die Acta Pacis Westphalicae" static page) plus 1 facet
search (APW II B 6 for "Brienne", to confirm B6's own date range), all via headless Chromium, >=1.6s apart, no
login. No new WebSearch or github.com requests (this target's check-solved sources were otherwise unchanged
from the 25 Sept pass above).

`python3 tools/intake_gate_check.py ciphers/espagnol142-mercy-1648` output: see done line.

**Verdict: unchanged, stays open (conditional).** Both editions the job brief named are now directly read or
structurally ruled out; the addressee's surname and the target's own folio (within ark `btv1b10035717h`,
canvas range ~30-70) remain unpinned, per the 24 Sept folio-pin attempt above -- still the fastest next step,
not a fresh edition search.

## Check-solved (LANE CX, 2026-09-25)

Six-source sweep run fresh this pass (LANE CX worker CX-CLAIR), on top of -- not only quoting -- the 24 Sept
2026 pass kept below (which already identified "l'abbé de Mercy" as a real envoy the Duc de Guise sent to the
Holy Roman Emperor from at least 1641, via a 1641 instruction on the same ark, resolving the earlier
identification gap, but left the addressee's surname and the target item's own folio unpinned).

1. **Web search.** `abbé de Mercy Duc de Guise 1648 Naples Empereur instruction diplomate` -- the Duc de
   Guise's own major 1647-48 project was the Neapolitan expedition (claiming the throne of Naples during
   Masaniello's revolt), which needed Imperial and Spanish diplomatic cover; no source found names a specific
   "abbé de Mercy" as his agent to the Emperor by full name/biography, but the chronology (envoy active
   1641-1648, instructions from the Guise household, Imperial destination) is internally consistent and not
   contradicted by anything found. No hit on the target item itself.
2. **Standard printed edition, opened and read.** The job brief's named edition, Le Clerc's *Négociations
   secrètes touchant la paix de Munster et d'Osnabrug* (already fetched for clair571-estrades-1645, tomes III
   and IV cover 1647-1648) -- re-used and grepped for this target: control "Servien" 175 hits in tome IV
   confirms the OCR reads well for exactly the 1648 period; "Mercy" 0 hits and "Barneton" 0 hits in both
   tomes III and IV. This is a real negative (the Munster/Osnabrück French-Swedish-Imperial negotiation
   record, read directly, does not print this Guise-to-Emperor channel), consistent with "l'abbé de Mercy"
   being a Guise-household channel to the Emperor running alongside, not through, the official Munster
   plenipotentiaries (d'Avaux/Servien). Acta Pacis Westphalicae itself (apw.digitale-sammlungen.de) named in
   the job brief for this row too, not opened this pass (budget; flagged for a future worker, since APW II B
   catalogues the same year's French correspondence in more granular detail than Le Clerc's printed digest).
3. **Community lists.** Cryptiana local snapshot re-grepped for "Mercy", "Espagnol 142/143/144", "Barneton":
   no hit (repeats 24 Sept finding). No Cipherbrain hit by web search.
4. **DECODE.** `unsolved-ciphers/catalogue/decode-catalog.csv` (fresh clone, 25 Sept 2026) grepped for
   "mercy", "espagnol 14", "barneton": zero hits for all three (repeats and extends the 24 Sept null result,
   now also covering the corrected shelfmark Espagnol 144/TOME III the 24 Sept digitisation-check pass
   pinned).
5. **Bourdeau** (fresh shallow clone, 25 Sept 2026). Grepped for "Mercy", "Espagnol 142/143/144", "Barneton":
   same as 24 Sept -- every "Mercy" hit checked is the common French word "merci" (clemency) inside unrelated
   transcriptions, no shelfmark hit, no "Barneton" hit anywhere.
6. **Aymeloglu** (fresh shallow clone, 25 Sept 2026). Grepped for "Mercy", "Espagnol 142/143/144", "Barneton":
   no hit.

Requests this section: archive.org 1 new (`_djvu.txt` fetch for negociationssecr04lecl; tome III reused from
target 1's fetch). WebSearch 1. github.com 0 new (clones reused from target 1).

## Verdict (confirmed, LANE CX 2026-09-25)

Stays **open, stage 2 verified unsolved (conditional)**, gate now closed with a real edition read and
control. The Le Clerc Munster/Osnabrück edition -- the job brief's own named source -- is now directly read
with no hit, which is informative (this channel runs outside the official Munster correspondence it prints)
rather than merely absent-because-unchecked. Still conditional: APW itself and any Guise-family or Naples-
expedition-specific edition remain unopened, and the target item's own folio (within the ark's canvases
30-70 range, per the 24 Sept pin attempt) is still not located.

---

# "Autre instruction chiffrée pour l'abbé de Mercy" -- BnF Espagnol 142-144

QUEUE row: M34 (`sources/solver-diffs/2026-09-24-lane-g2-gallica4.tsv`, LANE G2 worker F's archivesetmanuscrits
item-level sweep).

## Source

BnF, Espagnol 142-144 (Supplément français 1257A-C), `ark:/12148/cc347546`. Single named ciphered instruction,
"Autre instruction chiffrée pour l'abbé de Mercy", dated **6 June 1648**, inside a multi-tome Spanish-affairs
volume; no key stated. Not fetched at gallica.bnf.fr or archivesetmanuscrits.bnf.fr this pass per the brief;
catalogue text only, no image viewed.

## Check-solved sweep (24 September 2026)

1. **Search engine.** `"abbé de Mercy" 1648 instruction chiffrée Espagnol BnF` and `"abbé de Mercy" 1648
   diplomate Espagne Catalogne instruction` -- **the addressee is not securely identified**. No 1640s French
   abbé named Mercy surfaced in a diplomatic role; the only "de Mercy" figures found are chronologically wrong
   (Florimond Claude de Mercy-Argenteau, 1727-1794; Claude Florimond de Mercy, 1666-1734, a soldier not an
   abbé; a 19th-c. bishop of Luçon). Given the volume is Spanish-affairs and the date falls in the Catalan
   Revolt / Franco-Spanish War period, a search for French agents to Catalonia in 1648 (Magí Sivillà i
   Magoles, an abbot acting for the Generalitat; Abel Servien; Philippe de La Mothe-Houdancourt) found no match
   either. This is a genuine identification gap, not a checked-and-clear negative -- the addressee's identity
   needs the image or the volume's own finding aid, not a general web search.
2. **Printed correspondence / calendars.** Not run: no correspondent securely identified to search by name.
   The instruction itself, addressed by the French crown to its own agent, would most plausibly appear (if
   printed) in a Recueil des instructions données aux ambassadeurs volume for Spain -- not checked this pass.
3. **Cryptiana.** Local snapshot grepped for "Mercy", "Espagnol 142": no hit.
4. **Cipherbrain.** No dedicated query run; the addressee's uncertain identity makes a targeted Cipherbrain
   search unproductive without first resolving who "l'abbé de Mercy" is.
5. **DECODE.** Aymeloglu's cached `catalogue/decode-catalog.csv` (10,107 rows) grepped for "mercy",
   "espagnol 142", "espagnol 143", "espagnol 144": zero hits for any. This repo's own local harvest also has
   no matching row.
6. **Solver repositories.** Fresh shallow clones of both repos grepped for "Mercy" and "Espagnol 142"/
   "cc347546" exactly. "Mercy" returns many hits in both repos (e.g. `herbault1626/`, `bethune/`, `sega1593/`,
   `windischgraetz1720/`, `matignon1586/`) but every one checked by context is either the common French word
   "merci"/"mercy" (clemency) inside unrelated letter transcriptions, or an unrelated named person (none an
   "abbé de Mercy" or this shelfmark). No hit for the shelfmark or ark in either repo.

## Verdict

**Open, stage 2 verified unsolved (conditional).** Not found in a search engine, Cryptiana, DECODE's cached
catalogue, or either solver repository, searched by shelfmark, ark and the addressee's name on 24 Sept 2026.
Conditional, and lower-confidence than most of this pass's rows: the addressee "abbé de Mercy" could not be
identified as a historical figure this pass (name variant, mistranscription, or an obscure agent are all
possible), which blocks the correspondent-specific legs of the sweep (printed correspondence, calendars). The
image or the volume's own finding-aid context (title, adjacent items) is needed before this row can be swept
further.

Requests: WebSearch 2 queries. github.com 0 new (reused clones). No gallica.bnf.fr, no
archivesetmanuscrits.bnf.fr fetch. No subagents.

## Digitisation check (24 Sept 2026, LANE G2 worker O)

**Digitised: yes, ark `btv1b10035717h`, canvas not yet pinned (no folio labels on the manifest) -- but flag:
the item is in Espagnol 144 (TOME III), not Espagnol 142.** (`gallica all "Espagnol 144"` needed two
tunnel-reset retries, `ws_closed_mid_exchange`, before a clean response -- the same lane-wide flakiness noted
for M24; a third attempt returned HTTP 200 but 97210 records, all irrelevant.) The archivesetmanuscrits finding aid
(`https://archivesetmanuscrits.bnf.fr/ark:/12148/cc347546`) lists three sub-units, "Espagnol 142 (cote) • TOME
I," "Espagnol 143 (cote) • TOME II," "Espagnol 144 (cote) • TOME III"; `avecDaoGal` ("Consultable sur gallica")
is applied to 143 and 144 but **not** to 142. The finding aid's item list places "Autre instruction chiffrée
pour l'abbé de Mercy. Barneton, 6 juin 1648" at **F. 22-22 v° (item 11)**, whose foliation restarts at F.1
after the TOME III/"Espagnol 144" heading (checked by document-position order: the item's HTML anchor
`d0e2774` falls after the Espagnol 144 heading's `d0e2602`, itself after 143's `d0e597` and 142's `d0e82`) --
so the item is in the digitised TOME III, not the undigitised TOME I this target's folder name names. Ark
found via Gallica SRU field query `dc.source all "Espagnol 144"` (needed after `gallica all "Espagnol 144"`
returned 97210 hits, "144" being too common a substring for the non-field-scoped operator); the single
`dc.source`-scoped hit's `dc:relation` cites `archivesetmanuscrits.bnf.fr/ark:/12148/cc347546/cd0e2602` --
the exact Espagnol 144 component id. `tools/gallica_folio.py btv1b10035717h --folio 22` found 605 canvases,
0 with any folio label -- cannot pin the canvas without an eye-checked `--anchor` pair, out of this brief's
scope. Flag for whoever captures this: retitle/relocate this folder to reflect Espagnol 144, or at minimum
correct the shelfmark in any future capture/read files, before crops are cut. Status stays open (not blocked).

Requests this section: gallica.bnf.fr 3 (1 `gallica all` SRU query, 1 `dc.source all` SRU query, 1
`gallica_folio.py` manifest fetch).

## Folio 22 pin attempt, addressee identified (24 Sept 2026, LANE G2 worker T)

**"L'abbé de Mercy" is a real historical figure, resolving the check-solved sweep's identification gap.**
Canvas 30 of this ark (`btv1b10035717h`, 605 canvases, no manifest folio labels) carries, in its own ink page
number top right, "**8**", and is headed:

> "Instruction pour l'abbé de Mercy et ordre de ce qu'il aura affaire alant trouver sa Ma.té Imperiale de la
> part du Duc de Guise" -- dated **1641**.

This is a *different*, earlier, unciphered instruction to the same "abbé de Mercy" -- an envoy the **Duc de
Guise** sent to treat with the Holy Roman Emperor, active from at least 1641 (this item) through 1648 (our
target, whose own title "**Autre** instruction chiffrée pour l'abbé de Mercy" -- "**another/further**
instruction" -- now reads as one of a run of instructions to this same agent, not an isolated item). This
identifies the addressee role (envoy/agent, not a beneficed cleric of note) but not yet his surname or a
biographical entry; a further search for "abbé de Mercy" tied to the Duc de Guise (rather than alone, as
tried in the check-solved sweep) is the next step for the addressee's identity.

**Folio 22 (item 11) itself: still not pinned.** The page numbers found on-leaf (canvas 20 "~4", canvas 30 "8")
do **not** track the finding aid's own foliation in any simple linear way against canvas count (10 canvases
advance the on-leaf number by only ~4), which most likely means these ink numbers are each **item's own
original pagination** (carried over from the source document when bound into this recueil), not a continuous
archival foliation for the whole volume -- the same trap worker P already flagged for clairambault296. The
finding aid's "F.22" is probably a separate, volume-wide (often pencil) foliation not visible in these ink
page-corner numbers at this resolution. Given the abbé de Mercy items cluster together (canvas 30 = one such
item), item 11 (the 1648 one, presumably later in the binding order than the 1641 one since items in this run
look chronological) is likely within a canvas span of roughly 30-60, but this is not narrowed further this
pass -- out of budget.

**Content note (not yet the target item):** canvas 25, a few canvases before the 1641 Mercy item, is a
different, undated French instruction/dispatch discussing the "Duc de Richelieu" and a naval action
("quoi combattu 20 contre 120"), also in clear, no cipher -- unrelated to Mercy by name but confirms the
neighbourhood of canvases 20-30 holds a run of 1640s French diplomatic instructions in clear French, the same
genre as our target.

**Not pinned; status stays `open`.** A worker with budget for ~15-20 more canvas probes in the 30-70 range,
watching for the on-leaf date "1648" or the words "abbé de Mercy"/"Barneton" (the place the finding aid names
for the 6 June 1648 item), should be able to narrow it from here.

Requests this section: gallica.bnf.fr 8 (canvases 1, 20, 25, 30 at 200px -- canvas 1 retried once = 5
requests; canvases 20, 25, 30 re-fetched at ~1100px = 3 requests), >=1.5s apart, UA `cipher-lab research
script (contact via repository)`. No 403/429/challenge; one transient `Connection reset by peer` on the first
attempt at canvas 1, resolved on retry.
