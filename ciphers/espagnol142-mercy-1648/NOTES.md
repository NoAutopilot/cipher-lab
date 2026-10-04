partial
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

## Premise check (MERCY-C15, 2 Oct 2026)

Short re-confirmation before the code-15 blind read (clock 2 Oct 2026 13:2x UTC, rule 6). The target already carries a
reading and two verifier audits (AUDIT.md: N4, key `ours`, safe sentence revised after the 1 Oct Bourdeau fold-in); this
section only records (a)-(d) against what is on disk.
- (a) folder's own mentions of a decipherment, gloss or clear copy: **not found** -- NOTES.md's sibling and print sections
  name no deciphered or clear copy of f.22; the only clear texts are the sibling instructions ff.20r and 21r (other
  errands, other dates), read and used as parallels.
- (b) other solvers' working files: **found, not a prior decipherment** -- Bourdeau's 1 Oct 2026 page
  (`sources/cyphersolver/2026-10-01/mercy1648/`) is built on our issue 16 and our key; its own "Prior work checked"
  records no prior decipherment; it leaves code 15 open ("probably n"). Aymeloglu's repository: no row for this item
  (earlier passes).
- (c) physical neighbours: **not found** -- ff.20r, 21r (clear, other instructions) and f.22r's clear overview; no
  decipherment bound beside f.22 (`siblings_1648_hunt.md`, MERCY-SIB 2 Oct 2026; M3/H38 image probes of Espagnol 144).
- (d) recipient side: **not found / unreachable** -- the Brussels SEE registers (AGR inv. 238-260, 576, 578) have no
  digital object (`siblings_1648_hunt.md` section 1); Lonchay-Cuvelier IV no. 183 is a précis of Leopold's covering
  dispatch, not the instruction (AUDIT.md N4.2 row 4); APW II B ends 19 May 1648.
Result: no find; the item stays a cryptanalytic reading, key `ours`, N4. Gate pasted: `espagnol142-mercy-1648: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.

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

## Y5: letter located (25 Sept 2026, LANE R6)

**Pinned: folio 22 recto = canvas 58, folio 22 verso = canvas 59 (ark `btv1b10035717h`).** This matches the
archivesetmanuscrits finding aid's own "F. 22-22 v°" for item 11 exactly, and is content-confirmed, not just
offset-derived: canvas 58 carries the ink page number "22" (top right) with a marginal "1648" annotation, and
canvas 59 closes "...os encargo. **Barneton a seis Junio de 1648**" -- place name + day ("seis" = six) + month
+ year all matching the finding aid's own title "Autre instruction chiffrée pour l'abbé de Mercy. **Barneton,
6 juin 1648**" word for word. Canvas 60 (folio 23) is blank, confirming the item ends at f.22v as the finding
aid says.

**How it was pinned (worker T's per-item-reset hypothesis does not hold here -- this run is a single
continuous foliation).** The ink page numbers found across canvases 30-45 (worker T's "8" at canvas 30 was the
*start* of a long, continuous run, not an isolated item-local page) are exactly linear: "12" at canvas 38,
"13" at canvas 40, "14" at canvas 42, "15" at canvas 44 -- i.e. canvas = 2 x folio + 14 (residual 0 at every
point checked, including the two content-confirmed anchors 58=22r and 60=23r/blank). `tools/gallica_folio.py
btv1b10035717h --anchor 58=22r --anchor 60=23r --folio 22` records this fit (a=2.000, b=14.00, residuals
+0.0/+0.0). The canvases 30-38 range (worker T's 1641 unciphered instruction to the same "abbé de Mercy",
still discussing his Holland/Imperial mission at canvas 35) and canvas 38-42 (a Spanish-language instruction
"al Sr Abbad de Mercij" for a Holland voyage, dated Bruxelles 1 Feb 1645, ink page "12") are earlier items in
the same continuously-numbered run, not the target; canvas 44-57 is a further item on Condé/Mazarin/Longueville
politics (ink pages 15+) that also precedes the target in the same numbering.

**Cipher extent and system.** Two leaves only (f.22r-22v, canvases 58-59), each a full page of cipher, ~20
lines per leaf. This is a mixed code+plaintext design, not a full monoalphabetic cipher of the whole letter:
short plaintext Spanish connective/framing phrases (the opening salutation, "asi... me digais lo que en esta
sazon saveis entendido", "porque qualquiera ora de tardanla...", "Con fundamento lo que nos podemos prometer
y Caso de no estar en estado...", "Caso que le paresca que esta materia no convenga Corra por su mano...",
"En todo os encargo la brevedad...") alternate with long runs of bare 2-digit numeric code groups (occasional
larger values up to 186; a handful of numbers carry a trailing "." or "-" mark, e.g. "34.28.10", "18.6",
consistent with a nomenclator/mark-notation system rather than plain digit-for-letter substitution). No
interlinear or marginal decipherment, gloss, or period key is present on either leaf -- ciphertext only, as
transcribed by no one yet.

**Plaintext naming sender and recipient.** The letter opens addressing the recipient directly: "**Baron de
Mercy** mi Sumiller de Cortina, deveis tener resolucion de la negociacion que hicisteis..." -- i.e. addressed
to "Baron de Mercy, my Sumiller de Corte" (a Spanish royal-household post, roughly gentleman/officer of the
bedchamber), not "abbé" as the French catalogue title and the 1641 item (canvas 30) call him -- flag for
whoever transcribes next: same person, a title variant between a French cataloguer's gloss and this letter's
own Spanish address, or a distinct "Baron de Mercy"/"abbé de Mercy" pair sharing a surname; not resolved this
pass. No sender name or signature appears on either leaf: the letter is unsigned, closing only with the
place/date "Barneton a seis Junio de 1648", consistent with an unsigned Spanish royal-secretariat instruction
(the addressee's own household rank, "Sumiller de Corte", points to a Spanish-crown correspondent, matching
the volume's "Espagnol" shelfmark).

Files: `images/f22r_canvas58.jpg`, `images/f22v_canvas59.jpg` (native resolution, ~2.7 MB total, well under
the 30 MB budget), `images/manifest.json` (canvas, label, size, URL, byte count, sha1 for both).

Requests this section: gallica.bnf.fr -- 41 low-res (`/full/600,/0/`) probe fetches, canvases 30-70, one at a
time, >=2 s apart, UA `cipher-lab research script (contact via repository)`, no 403/429/challenge; plus 2
native-resolution fetches (canvases 58-59) at >=2 s apart. 43 total, within the brief's <=45 cap. No
subagents, no other hosts.

Not done this pass (out of brief's scope): transcription of the ciphertext, key search, decode. Next step for
whoever takes this target: transcribe f.22r-22v as ciphertext.txt (2 blind passes per the project's usual
rule), and separately, since the "Baron"/"abbé" title mismatch is unresolved, a quick check of canvases
46-57 (the intervening Condé/Mazarin item) for any signature or heading that might explain it before assuming
it is the same agent.

## Y6: transcription and key trial (25 Sept 2026, LANE R6)

**Status unchanged: open.** This pass transcribes the ciphertext (f.22r-22v) and searches for a published key of
the same office; no key found, so no decode was attempted (per this worker's brief, cryptanalysis is out of scope).

### Transcription

Two blind passes from the images already on disk (`images/f22r_canvas58.jpg`, `images/f22v_canvas59.jpg`):
line crops cut with `tools/iiif_lines.py --image ... --lines-per-crop 5` (18 crops, `images/f22r_L*.jpg`,
`images/f22v_L*.jpg`, both leaves' full width split into left/right halves at native resolution). Pass A: this
worker, reading the crops directly. Pass B: one blind Sonnet subagent, given only the crop images (not this
worker's transcription), writing independently to `passB.tsv`.

`tools/reconcile_passes.py passA.tsv passB.tsv --crops images --keep-plain`: **95.3% agreement (662/695
signs), well above the 80% gate** (98.9% on the numeric/mark stream alone, 521 code+mark tokens). 33
disagreement columns, mostly period-spelling variants the two passes read differently (deseo/desseo,
saver/saber, tardança/tardanla, u/v equivalence) -- not settled further, both are legitimate readings of this
hand's orthography. Two real corrections came out of reconciliation and a re-check against the full-page
images (not just the line crops, which had cut a few lines short at their right-hand crop boundary): four
manuscript lines (v05-v08) had 5-7 trailing code tokens missing from pass A's initial reading, recovered by
comparing against `images/f22v_canvas59.jpg` directly; two spots pass A read as a bare digit 7 (r07, r09) are
in fact a distinct symbol pass B independently and correctly flagged as non-digit, transcribed here as
`[MARK:box]`. Settled from the image, not left as a majority vote.

Six columns still disagree after settling and are left at confidence M with the alternate noted in
`ciphertext.tsv`: `r04` pos17 (17 vs pass B's 47), `r20` pos6-7 (two single digits 2,3 vs pass B's joined
23), `v01` pos6 (a non-standard symbol, exact shape unclear -- "1½"-like vs pass B's "[MARK:loop]", needs an
eye-check against the image at higher zoom than this pass used), `v04` pos19 (a digit at the exact crop
boundary pass B's crop cut off), and `r03` pos1 (both passes agree the character is "24"; disagreement is
only bookkeeping -- pass A classed it as a plain section-numeral pass B classed as a code, see below).

**Files:** `passA.tsv`, `passB.tsv` (both long format: line, pos, token, conf, note), `disagreements.tsv`,
`agreement.tsv`, `ciphertext_draft.tsv` (reconciler output), `ciphertext.tsv` (= `ciphertext_draft.tsv`, the
committed reading). 18 new line-crop images in `images/` (`images/manifest.json` updated), well under the
30 MB budget (images/ now ~7 MB total).

### The ciphertext: structure

Two leaves, 40 manuscript lines (24 recto, 16 verso), 174 plain-Spanish-word tokens and 521 code/mark tokens.
**Only 38 distinct code/mark values are used across those 521 tokens** (36 numeric values, range 2-72, plus
two non-numeric marks `[MARK:box]` and `[MARK:frac]`), with the five commonest values (18, 32, 5, 10, 6)
covering nearly 40% of all code tokens. That is a small alphabet for 521 tokens -- consistent with a
**homophonic or plain substitution over individual letters** (roughly matching the size of the Spanish
alphabet plus a few homophones and nulls), not a nomenclator with hundreds of word/syllable codes the way
e.g. Bourdeau's Carpio-1677 or Balbases-1677 Brussels keys are built (both go well past 100 distinct code
values into the hundreds; see below). This is an observation for whoever attempts cryptanalysis next, not a
decode -- flagged, not solved, per this brief's scope.

The plain-Spanish runs open the letter's own address ("Baron de Mercy mi Sumiller de Cortina deseo tener
Resolucion de la negociacion que fuisteis..."), a mid-letter connective ("...porque qualquiera hora de
tardanza en la coyuntura presente es de summo perjuicio procuraveis sacar Respuesta Cathegorica en la
materia"; "Con fundamento lo que nos podemos prometer y Caso de no estar en estado y que es necesario esperar
algun tiempo para poder dezir determinadamente el que tiene esta negociacion y lo que se puede confiar della";
"Caso que le paresca que esta materia no convenga, Corra por su mano le preguntareis a que persona se podria
encargar para que se pudiese caminar en ello sin perder tiempo. ... En todo os encargo la brevedad porque
qualquiera dilacion que aya es summamente dañosa y de nuestro zelo fio atendera ello con el Cuydado que
conviene"), and the closing dateline ("...os encargo. Barneton, a seis Junio de 1648"), matching the finding
aid's own "Barneton, 6 juin 1648" word for word (confirms worker Y5's folio pin again, independently, from
the full transcription this time rather than just the closing line). "24 -" after "operaciones que se deven
saver:" (r03) reads as a plain section/item numeral in the same hand as the surrounding plain text, not a
cipher code -- flagged in `ciphertext.tsv` as `[PLAIN:24]` rather than a numeric sign, though pass B's blind
reading (which does not distinguish plain numerals from code numerals by convention) counted it as a code;
recorded as a bookkeeping disagreement above, not a reading dispute.

### Key trial (lead class 4: a published key of the same office)

Searched, within this brief's host limit (github.com, one shallow clone only -- no DECODE, no web search):

1. **Cryptiana's Spanish-cipher pages** (`sources/cryptiana/web/spanish*.htm`, all seven: spanish, spanish2,
   spanish2A, spanish2B, spanish2C, spanish3, spanish3C, spanish3D). All cover Ferdinand/Isabella through
   Philip II (1470s-1580s); none reaches the 1640s. No candidate.
2. **`dbourdeau/cyphersolver`** (fresh shallow clone, 25 Sept 2026). No folder or catalogue entry for
   "Castel-Rodrigo", "Peñaranda"/"Penaranda", or "Bracamonte". Folders in the 1640-1650 window
   (`baner1640/`, `conti1649/`, `goring1645/`, `hm1645/`, `rupert1645/`) are all non-Spanish (Swedish,
   Italian, English/Royalist, Prince Rupert). `esp318/` is Ferdinand/Isabella-era (1497-1504), wrong century.
   **Best lead found, not testable within this brief's hosts:** `balbases1677/NOTES.md` and
   `docs/balbases1677.html` record that Bourdeau checked "eight Brussels keys in the series ... DECODE
   R958-R965 ('chiffres 1647-98')" against the Balbases-Fuenmayor 1677-78 correspondence (same
   Secrétairerie d'État et de Guerre, Archives générales du Royaume, Brussels -- the same government office
   as this target, a generation later) and found none of the eight fit *that* correspondence. The series
   itself runs from **1647**, one year before this target's 6 June 1648 letter, and is the single closest
   date/office match found anywhere in this search -- but Bourdeau's repo only references these DECODE
   records (`de-crypt.org/decrypt-web/RecordsView/958` through `.../965`), it does not embed their key data,
   so this worker could not fetch or apply them: this job brief restricts hosts to github.com only, and
   DECODE is out of scope this pass. **Recommended next step for a worker with DECODE access:** fetch
   R958-R965 (Brussels "chiffres 1647-98") and test the earliest of the eight against this target -- it was
   checked against a *different* correspondence (Balbases-Fuenmayor, 1677-78, a different sender/recipient
   pair) and failing there does not rule it out for a Guise-household-to-Baron-de-Mercy letter of June 1648.
   As a secondary, weaker check: `balbases1677/key.json` (that repo's own rebuilt key, not from the "chiffres
   1647-98" series) was inspected directly -- it is a 180-entry syllabic nomenclator, numeric range 1-700,
   architecturally a poor match for this target's 38-value near-alphabet-sized code set, and 29 years off
   this target's date, so not applied. `carpio1677/`'s key (also Brussels-adjacent, described in its NOTES.md
   prose but with no machine-readable key file in the repo) is a similar large syllabic nomenclator (numbers
   9-60 plus a struck-through second table), same mismatch, same date gap; not applied.
3. No Aymeloglu clone made (this brief names only Bourdeau's index for this lead, and restricts this pass to
   one shallow clone).

**Result: no candidate key found that this worker could both identify and apply.** Per this brief, this is
reported as the negative result for the lead-class-4 search, not a decode attempt; no matched-control test
was run because no key was ever applied to the ciphertext (rule 3's control requirement applies to a
solver's *attempt*, and none was made here beyond identifying candidates). The transcription itself
(`ciphertext.tsv`) is now on file for whoever runs cryptanalysis or fetches the Brussels 1647-98 series next.

Requests this section: github.com 1 shallow clone (`dbourdeau/cyphersolver`, ~12,000 files, single fetch).
No other hosts. 1 Sonnet subagent (pass B transcription, within the brief's cap of one).

## Y8: spec and first test (25 Sept 2026, LANE R6)

**Status unchanged: open.** Per `.claude/briefs/runs/2026-09-25-lane-r6-y8-mercy-spec.md` (breadth lane,
CLAUDE.md 3a): built a Spanish period corpus, wrote `specs/espagnol142-mercy-1648.json`, and ran the spec's
first cheap test (homophonic anneal with a matched control). Full numbers are in the spec's
`cheap_test_done`; this section explains them and flags what needs attention.

### es17 corpus

`tools/data/es17/` (new): two Internet Archive `_djvu.txt` texts, early-17th-c. Spanish prose -- Cervantes'
*Don Quijote* (1876 reprint, clean OCR) and Quevedo's *Vida del Buscón* (1911 reprint, clean OCR; a genuine
1626-edition scan of the same text was tried first and rejected -- its long-s type OCRs as "f" throughout,
"feñor" for "señor", which would bias letter frequencies). 1,924,629 letters after `fold()`, well over the
brief's 200k floor. See `tools/data/es17/README.md` and `MANIFEST.tsv`. Wired into
`tools/judge_plaintext.py`'s `LANG_CORPORA["es"]` (there was no prior `es` default to preserve, unlike
`de`/`fr`, so this needed no per-spec workaround); `python3 tools/judge_plaintext.py --selftest` still
passes. `tools/data/README.md`'s table updated.

### Cheap test 1: homophonic anneal, matched control first

Extracted the 521 code/mark tokens from `ciphertext.tsv` (dropping the 174 `[PLAIN:...]` tokens) to
`cipher_codes.tsv` (marks as separate symbols, N=521, K=38) and `cipher_codes_nomarks.tsv` (marks dropped,
N=518, K=36). Ran `tools/homophonic_anneal.py` (default order=3, 8 restarts x 40,000 iters) against both,
with the es17 corpus, several seeds each; ran the tool's own matched `--control` (same N, K, homophonic
design, Spanish, same solver) **first**, 5 seeds at K=38 and 3 at K=36, per CLAUDE.md rule 3.

**Control (what a real Spanish text of this exact shape scores):** K=38/N=521 scores across 5 seeds:
-1321.7, -1356.6, -1326.0, -1337.4, -1339.1 (best -1321.7; letter-recovery share 35.5-81.4%, itself uneven,
consistent with this design being hard for the annealer even on real Spanish -- the Salviati/code+mark
lesson in CLAUDE.md rule 3 again: a homophonic/code design at this N does not read reliably blind).
K=36/N=518 (marks dropped) across 3 seeds: -1352.5, -1335.5, -1352.2 (best -1335.5).

**Target:** K=38/N=521 across seeds 1,2,3,4,5,7: best score -1154.3 to -1154.6 at seeds 2, 3, 5, and 7 (seed
7 run at 16 restarts, 9 of them land in that same narrow band); seed 1 stuck at -1353.2, seed 4 at -1178.5.
K=36/N=518 (marks dropped) across seeds 1,2,3: -1154.5, -1154.5, -1156.0 -- same optimum, same
reproducibility, regardless of whether the 3 mark tokens are kept or dropped.

**The gap:** the target's best score beats every one of the 8 control runs tried, by 167 points
(K=38: -1154.3 vs control best -1321.7) to 181 points (K=36: -1154.5 vs control best -1335.5) -- far outside
the control's own inter-seed spread (about 35 points at K=38, 17 points at K=36). This is reproduced by
`cheap_test_1/rerun.sh` (checked: re-running gives -1154.6/-1154.3/-1154.6 for three target seeds and the
same five control numbers, byte-for-byte).

**Judge verdict** (`tools/judge_plaintext.py` against an ad hoc `{"judge": {"language": "es", "letters_min":
200, "control_samples": 200}}` spec, `--file` the K=38 seed-3 decode): length OK; language **FAIL** --
score=-1.048, null_p99=-1.88 (clears -- this is clearly not random text), real_p05=-0.897, real_median=-0.812
(fails -- not yet as clean as real prose). So: neither a clean PASS nor a routine, uninformative negative.

**What this means, and what it does not mean.** The score gap is large and reproducible across independent
random seeds and both design variants (marks in/out), which is strong evidence this 521-code sequence is
*more decryptable toward Spanish* than a real Spanish text of the same shape typically is under this
solver -- consistent with a genuine (if only partially recovered) homophonic substitution, not noise. It is
**not** a reading: 17 of the 24 available letters are used across the 38 codes (f, g, h, k, w, x, z never
appear), so several low-frequency codes are almost certainly wrong under a pure trigram objective with no
crib; the plain-Spanish context already transcribed around the code runs (the address, the connective
sentences, the closing dateline) was **not** used as a crib here (that is the spec's test 2, a campaign-scale
step, not this breadth test). For the record, not as a claim: the decode contains legible-looking fragments
-- `electordebrandenburi` ("elector de Brandenburg", missing the final g since no code maps to g in this
key -- and the Elector of Brandenburg is a real figure in exactly this period's diplomacy), `cartasdecreencio`
("cartas de creencia", credential letters -- a real diplomatic term), `millombres`/`inoanteria` ("mil
hombres"/"infantería", military terms) -- flagged for a follow-up worker to check against the image and the
crib, not confirmed, and no rule-10 wording applies to any of it.

**Caveat on the control's rigor.** The brief asked for a control using "the target's own code frequency
profile" (i.e. replicating the exact 38 occurrence counts, 57/42/41/.../1, not just corpus letter
frequency). `tools/homophonic_anneal.py --control` allots homophone group *sizes* to letters by corpus
letter frequency, which is a matched-N/K/design/language control per CLAUDE.md rule 3's letter, but not
that stricter ask. A custom script attempting the exact multiset (`/tmp/exact_freq_control.py`, not
committed -- scratch only) had a bug (it zipped the 38 target counts against only the ~24 available
letters, producing K=307-320 instead of 38) and was abandoned mid-pass rather than spend further budget
debugging it under this test's cap. Given the size of the gap (167-181 points vs a control spread of
17-35), it is very likely a stricter control would still leave a large gap, but this was not run --
**flagged as the next worker's first move**, not claimed.

**Recommendation:** this spec's first test *moved it* (CLAUDE.md 3a) -- the gap is far larger than the
control's own noise and reproduces across seeds and design choices. Recommend promoting
espagnol142-mercy-1648 to a campaign: (1) the exact-frequency-profile control above; (2) hand/crib
refinement using the already-transcribed plain-Spanish context as anchors, and eye-checking the 1-3-
occurrence codes against the image; (3) fetching DECODE's Brussels "chiffres 1647-98" (R958-R965, Y6's lead)
in parallel. Status stays **open** -- no established reading, no key, nothing graded under rule 4 yet.

**Files:** `tools/data/es17/` (new, 2 files + README + MANIFEST), `tools/judge_plaintext.py` (LANG_CORPORA
edit), `tools/data/README.md` (table row), `specs/espagnol142-mercy-1648.json` (new),
`ciphers/espagnol142-mercy-1648/cipher_codes.tsv`, `cipher_codes_nomarks.tsv`,
`candidate_reading_seed3_marks.txt`, `candidate_reading_nomarks_seed1.txt`, `cheap_test_1/` (raw JSON
outputs for every seed reported above, plus `rerun.sh`, which reproduces the key numbers exactly).

**Requests:** archive.org 2 (djvu.txt downloads for es17) + 4 metadata/search calls (advancedsearch.php x2,
metadata.php x2), all >=1.5s apart, descriptive UA. No other hosts. No subagents.

## M2: graded reading (25 Sept 2026, LANE R6)

**Status unchanged: open** (judge FAIL; see the calibration note). Brief: `.claude/briefs/runs/2026-09-25-lane-r6-m2-mercy-read.md`.
Disk only, no hosts, no subagents. Start 17:45 UTC.

**Result in one line.** 521 code tokens graded **S 494, M 27, H 0, C 0** (a cryptanalytic result, rule 4). About
three fifths of the code stream now reads as connected Spanish in the letter's own frame; the rest (r16-r17,
v04-v08) does not, and the judge FAILs.

**Reading (cipher runs upper case in `reading.txt`, clear words as written):**
`[24] ALANDOSE ESTAS ARMAS EN CAMPAGNA y asi Holgare me digais lo que en esta razon saueis entendido. DE LA DUQUESA DE
CHEUREUSE Y DEL _ y porque qualquiera ora de tardanca ... en la materia. Y QUE EL _ UENGA CON UOS PARA QUE NOS
INFUME DE OULAY SEPAMOS Con fundamento lo que nos podemos prometer ... confiar della. PASAREIS A CLEUES A UEROS CON EL
ELECTOR DE BRANDENBURG Y CON COPURA D LONBURG SZRFSUCMAREY MAYOR PARA DIENSE Y EMBIAN CARTAS DE CREENCIA QUE UAN CON ESTA Y
LES PROPONDREIS DES I SE PERMITIRA SE LEUANTEN EN AQUEL PAIS TRES MIL HOMBRES DE INFANTERIA EN DOS O TRE SEGIMIENTI Y CON
QUE CONDICIONES Y ALEAMARE MAYOR SI QUERRA ENCARGAE DELLA Y QUE CORRA POR SU NOLADIRENTNONYSIIUNA SERA MAS CONUENIENT ARO
TRATAN TA GENTE DE QUE A A LEUANTADA TG DOLA Y EN SU LUGAR LEUAAR OTRA y Caso que le paresca ... sin perder tiempo. Y SE
CONSUIESE EL FRUTO DE TENER TA GENTE En todo os encargo la brevedad ... Barneton a seis Junio de 1648`
(`_` = [MARK:box], a word code left unread; twice where a name or title fits: "y del _", "que el _ venga con vos".)

**How it was read (files).** Y8's best key (`cheap_test_1/target_marks_seed3.json`) applied to the code runs with
their clear neighbours (`m2/view.py --runs`); ten corrections, each logged in `corrections.tsv` with the
occurrences that justify it and those that do not (rule: two independent readable occurrences, never one). Five
code->letter changes by reading (34 o->a, 20 o->f, 22 i->g, 24 l->h, 26 e->i), one after the anneal re-run (33 a->e),
two against the anneal (13 s->y on seven occurrences incl. "ma-y-or" checked on the image; 25 i->u on two, graded M),
frac->c (one occurrence, M). Then `tools/homophonic_anneal.py --fix` with the 29 confirmed codes held (3 seeds, all
-1199.1; `m2/cipher_codes_eyefix.tsv`) to settle the rest: 15 n, 48 d, 52 y, 65 s, 72 z, kept at grade M.
`key.tsv` (38 rows, grade and the words behind each), `exceptions.tsv` (5 rows), `decode.json`;
`python3 tools/decode_key.py ciphers/espagnol142-mercy-1648 --check` exits 0; `reading.txt`, `reading_tokens.tsv`.

**Transcription slips found (flag for a re-pass, not repaired in ciphertext.tsv).** Five glyphs both blind passes
read as 19 are 14 on the image (an open 4, the same shape as the 4 of the adjacent 24/34; a 9 in this hand has a
round bowl): r06:14, r14:7, r16:3, r16:6, r17:5. They give "de la duquesa de CHEUREUSE", "pasareis a CLEUES a veros
con el elector de Brandenburg", "y CON CO...". Recorded in `exceptions.tsv` at grade M, not silently repaired
(rule 2). All other 19s on r04, r07, r09, r10, r15, r19, r20 were checked and are 19. Also: the tail of v07 on the
image reads "... 7 17 16 10 3 17 22" where ciphertext.tsv has "... 7 17 16 10 7 22" (one code more, "3 17" for
"7"); not applied, needs the re-pass. Dots after some codes ("34.28.10", "16.", "8.", "19.") are on the image and
not in the transcription; they do not fall on word boundaries in the reading and were not used.

**Judge (rule 7, pasted).**
```
$ python3 tools/judge_plaintext.py specs/espagnol142-mercy-1648.json --file ciphers/espagnol142-mercy-1648/reading.txt
ok   length: got=1341, min=200, max=1000000000
FAIL language: score=-1.034, null_p99=-1.924, real_p05=-0.875, real_median=-0.814, mode=both, N=1341
FAIL - espagnol142-mercy-1648 (a PASS is a gate for a verifier, not a reading; rule 10)
$ python3 tools/judge_plaintext.py specs/espagnol142-mercy-1648.json --file ciphers/espagnol142-mercy-1648/m2/reading_codes_only.txt
ok   length: got=519, min=200, max=1000000000
FAIL language: score=-1.057, null_p99=-1.862, real_p05=-0.879, real_median=-0.811, mode=both, N=519
FAIL - espagnol142-mercy-1648
$ python3 tools/judge_plaintext.py specs/espagnol142-mercy-1648.json --file ciphers/espagnol142-mercy-1648/m2/clear_words_only.txt
ok   length: got=782
FAIL language: score=-0.892, null_p99=-1.899, real_p05=-0.888, real_median=-0.822, mode=both, N=782
FAIL - espagnol142-mercy-1648
```
The first is the brief's command (it scores the 174 clear words and the line labels together with the decode). The
second is the 519-letter decode alone: -1.057, against Y8's blind -1.048 -- the corrections do **not** move the
judge. The third is the calibration check: **the letter's own clear words, real 1648 secretarial Spanish transcribed
at 95% agreement, also FAIL the es17 judge** (-0.892 vs real_p05 -0.888). es17 is Cervantes and Quevedo; this
letter is chancery prose with German and French names (Brandenburg, Cleues, Cheureuse, Lonburg). So a FAIL here is
weakly informative (CLAUDE.md rule 3, era/register lesson of V6-PTCORP); a PASS would have needed a register-matched
corpus, which this pass did not build (suggestion below). The decode still sits 0.17 below the clear words, which
is real: roughly two fifths of the stream does not read.

**Crib-loop gain gate (rule 3), both numbers.** Same procedure on Y8's matched control seed 1 (K=38, N=521,
homophonic, Quijote text; blind -1321.7, 269/521 letters, judge -1.222): the words a reader sees in its blind
decode (tambien, caballo, sera, altos, buen, estan, que, de, la ...) fix 31 of 38 signs, of which only 15 are in
fact right; no code change could be justified by two readable occurrences; the re-anneal with those fixed returns
the identical optimum on 3 seeds. **Control gain: 0.0 anneal points, 0 letters, judge -1.222 -> -1.222. Target:
anneal -1154.3 -> -1199.1 (the trigram objective dislikes the corrections: gn, f, names), judge -1.048 -> -1.057,
readable clauses from about one (Y8's fragments) to about a dozen.** On the numeric gate the target's gain does
not exceed the control's; what changed is legibility, which neither number measures. Reported as such, not as a
pass. `m2/control_procedure.txt` has the run.

**Historical sense (context only, nothing searched, nothing claimed).** June 1648, Spanish Netherlands: the
Spanish-Dutch peace of Münster was ratified in May 1648 and the war with France went on. The Duchess of Chevreuse
was in exile in the Spanish Netherlands 1645-49; Cleves was the Elector of Brandenburg's residence on the Spanish
Netherlands' border; recruiting three thousand German foot in two or three regiments for Spain's service, with
credential letters and a demand for haste, fits that summer. "Mi Sumiller de Cortina" is a Spanish royal-chapel post,
so the unsigned sender is a prince with a household (the governor-general Archduke Leopold Wilhelm is the obvious
candidate; the catalogue's Guise link is the 1641 item, and Guise was a prisoner in Spain from April 1648) -- an
inference, not read from the leaf. "Lonburg" (r16) and "Barneton" are not resolved.

**What did not read, for the next worker (one line each).** (1) r16-r17 after Brandenburg: "Y CON CO[25]RA D LONBURG
S[72]RFS[25]CMARE[52] MAYOR PARA [48]IENSE" -- rare codes 72, 52, 48 sit here; likely word codes or nulls. (2) v04
"NOLADIRENTNONYSIIUNA" (two 15s, M-confidence row v04:19). (3) v07-v08 "A A LEUANTADA TG DOLA Y" (image has an extra
code, above). (4) 25: u reads twice, a reads once. Suggestions: a transcription re-pass of r16-r17, v04, v07 with the
14/19 and 3/7 shapes in mind; a register-matched es corpus (chancery letters, 1620-1660) before re-judging; the DECODE
Brussels chiffres 1647-98 lead (Y6) stays the recovery route -- a key sheet would settle 48/52/65/72 and the box mark.

**Search log.** Nothing searched for the letter in print (the verifier's job). Report what was found: a reading at
grade S/M from cryptanalysis with a control; where it was not found: no key source, no plaintext source consulted.
Requests: none. Subagents: none. Cost: read by the orchestrator.

## MR: fresh re-derivation (25 Sept 2026, LANE R6)

Rule-7 re-derivation, fresh instance: read only specs/espagnol142-mercy-1648.json, ciphertext.tsv, key.tsv,
exceptions.tsv and decode.json (not reading.txt, NOTES.md's M2 section, m2/ or corrections.tsv) before running
anything.

Ran `tools/decode_key.py ciphers/espagnol142-mercy-1648` via a copy of decode.json pointed at
`rederive/reading_fresh.txt` / `rederive/reading_tokens_fresh.tsv` (same ciphertext/key/exceptions/header/style
fields, only the output paths changed, so as not to overwrite the committed reading while regenerating it).
Token grade counts from the fresh run: **S 494, M 27** (H 0, C 0, I 0, U 0) of 521 -- identical to the committed
reading's M2 counts (S 494, M 27).

`diff reading.txt rederive/reading_fresh.txt` and `diff reading_tokens.tsv rederive/reading_tokens_fresh.tsv`:
**both exit 0, byte-identical.** Differing tokens against the committed reading: **0** (vs the M-graded count of
27 in the brief -- i.e. the fresh derivation reproduces every one of the 27 M-graded tokens exactly as committed,
0 tokens differ).

`tools/decode_key.py ciphers/espagnol142-mercy-1648 --check`: `reading up to date`, **exit 0**.

Conclusion: the committed reading.txt is a faithful, reproducible regeneration of ciphertext.tsv + key.tsv +
exceptions.tsv under decode.json as committed. Not classifying novelty (rule 10); not evaluating the judge result
or the register question (M2/MJ's job). Files: `rederive/reading_fresh.txt`, `rederive/reading_tokens_fresh.tsv`.
Hosts: none. Subagents: none.

## MJ: register-matched judge corpus (25 Sept 2026, LANE R6)

Brief: `.claude/briefs/runs/2026-09-25-lane-r6-mj-mr-mercy-judge.md`. Archive.org only, disk otherwise. Start
18:18 UTC per `date -u`.

Built `tools/data/es17c/` -- three Internet Archive volumes of *Memorial histórico español* ("Cartas de algunos
PP. de la Compañía de Jesús sobre los sucesos de la Monarquía entre los años de 1634 y 1648", tomos V-VII,
1643-1647), a Spanish court-newsletter register close in date, subject matter (war, diplomacy, troop levies,
credential letters, an elector) and genre (letters, not fiction) to this target's own 6 June 1648 letter --
unlike es17 (Cervantes/Quevedo novels). 2,099,273 folded letters, well over the ~200k floor. Full build
rationale, cleaning, MANIFEST.tsv and hold-out log: `tools/data/es17c/README.md`.

**Hold-out check (per the brief).** Grepped all three raw volumes for "Mercy", "Mercij", "Barneton", "Sumiller"
and "Brandenburg" near 1648 before cleaning. No hit is this letter, its reply, or plausibly connected to it:
every "Mercy" hit is Franz von Mercy, the Imperial general killed at Nördlingen in 1645 (not the target's
addressee, the Baron de Mercy, Sumiller de Cortina); zero "Barneton" hits in any volume; "Sumiller" hits are
generic office references to other named people (one explicitly dated to before 1641, the Infante-Cardenal's
household); "Brandenburg"/"Chevreuse" hits sit nowhere near each other or near the target's other distinctive
phrases, and the only "Chevreuse" hits are in tomo XIX's own cumulative name index citing other volumes. **Not
flagged in ROOM.md -- nothing found that needed flagging.**

**Wired into `tools/judge_plaintext.py`** as a new key `LANG_CORPORA["es17c"]`, `"es"` (es17) unchanged as the
default. `python3 tools/judge_plaintext.py --selftest` passes after the edit.

**Held-out real-prose false-negative rate** (`tools/data/es17c/holdout_check.py`, leave-one-file-out, N=519
matching the target's own code-only reading length, 200 samples per held-out file):
```
held_out=memorialhistri17realuoft.txt.gz N=519 samples=200 real_p05=-0.847 false_negatives=79/200 (39.5%)
held_out=memorialhistri18realuoft.txt.gz N=519 samples=200 real_p05=-0.866 false_negatives=42/200 (21.0%)
held_out=memorialhistri19realuoft.txt.gz N=519 samples=200 real_p05=-0.892 false_negatives=20/200 (10.0%)
TOTAL false-negative rate: 141/600 (23.5%)
```
Notably higher than pt18's 4.0% (V6-PTCORP) -- these three tomes are less internally uniform than pt18's four
periodical volumes (tomo XVII's false-negative rate is ~4x tomo XIX's), so a FAIL against es17c carries more
noise than a FAIL against pt18 did for Linhares. Reported as found, not smoothed over.

**Judge output, clear words alone and the reading, against es17c** (spec variant `{"judge": {"language":
"es17c", "letters_min": 200, "control_samples": 200}}`, run against the same files M2 already judged against
es17):
```
$ python3 tools/judge_plaintext.py <es17c spec variant> --file ciphers/espagnol142-mercy-1648/m2/clear_words_only.txt
ok   length: got=782, min=200, max=1000000000
FAIL language: score=-0.891, null_p99=-1.944, real_p05=-0.867, real_median=-0.787, mode=both, N=782
FAIL - espagnol142-mercy-1648-es17c-variant (a PASS is a gate for a verifier, not a reading; rule 10)
$ python3 tools/judge_plaintext.py <es17c spec variant> --file ciphers/espagnol142-mercy-1648/m2/reading_codes_only.txt
ok   length: got=519, min=200, max=1000000000
FAIL language: score=-1.052, null_p99=-1.928, real_p05=-0.874, real_median=-0.786, mode=both, N=519
FAIL - espagnol142-mercy-1648-es17c-variant (a PASS is a gate for a verifier, not a reading; rule 10)
$ python3 tools/judge_plaintext.py <es17c spec variant> --file ciphers/espagnol142-mercy-1648/reading.txt
ok   length: got=1341, min=200, max=1000000000
FAIL language: score=-1.04, null_p99=-1.998, real_p05=-0.87, real_median=-0.794, mode=both, N=1341
FAIL - espagnol142-mercy-1648-es17c-variant (a PASS is a gate for a verifier, not a reading; rule 10)
```

**Register-matching did not flip the FAIL to a PASS.** The clear words score -0.891 against es17c's real_p05
of -0.867 (0.024 gap) versus -0.892 against es17's -0.888 (0.004 gap) -- essentially the same borderline FAIL
either way, if anything slightly wider on es17c. **M2's register-mismatch hypothesis is not confirmed by this
corpus**: swapping Cervantes/Quevedo for contemporary Jesuit newsletters about the same decade's wars and
diplomacy did not rescue the calibration the way pt18 rescued Linhares. Combined with the 23.5% held-out
false-negative rate above, two explanations are left open, neither tested here: (a) N=519-782 may simply be
short enough that this add-k 4-gram judge's real_p05 threshold is noisy regardless of corpus; (b) the letter's
own terse secretarial idiom (heavy abbreviation, place/person names) may genuinely score lower than continuous
narrative prose on any corpus tried so far, independent of era or register. Status unchanged: **open**.

Not classifying novelty (that is the verifier's job, rule 10). Requests: archive.org 3 advancedsearch.php, 3
metadata.php, 3 djvu.txt downloads (>=1.6s apart, descriptive UA). No subagents.

## M3: sibling sweep (25 Sept 2026, LANE R6)

**Status unchanged: open.** Brief: `.claude/briefs/runs/2026-09-25-lane-r6-m3-mercy-siblings.md` (NEAR.md's
"pools first" next step for this target). Start 18:53 UTC per `date -u`. Result: **no sibling found; pooled N
stays 521 (unchanged).**

### Finding aid sweep

`archivesetmanuscrits.bnf.fr/ark:/12148/cc347546` (Espagnol 142-144 finding aid), fetched whole (1 request,
needed 2 retries after `Recv failure: Connection reset by peer` -- the same tunnel-reset flakiness this host
showed on 24 Sept, resolved on the third attempt, no 403/429/challenge). Read with `tools/html2text.py`, then
grepped the full text for `chiffr|cifr`, `Mercy|Merzy|Merçi|Mercij`, `Castel-Rodrigo`, `Peñaranda|Penaranda`,
`Bruxelles|Brusselas`, `secretairerie|secrétairerie`, and the 1640-1650 year range.

**Only one item in the entire 605-canvas, three-tome finding aid is marked "chiffrée": item 11 (F.22-22v),
the target itself.** No hit anywhere for Castel-Rodrigo or Peñaranda/Penaranda (repeats the 24 Sept
check-solved sweep's null result, now against the full item-level catalogue text, not just a name search).

A tight cluster of items in Espagnol 144 (TOME III, this target's own ark `btv1b10035717h`), F.4-21v, items
4, 6, 7, 8, 9-10, are all instructions to or about the abbé/Baron de Mercy from the same Guise/Brussels-secretariat
channel, 1639-1648 -- by title alone the strongest sibling candidates, and the brief's own "addressed to or from
Mercy" criterion names exactly this cluster. Two of the six (items 7 and 9-10) are explicitly "En espagnol"
language; the rest are French. None is marked "chiffrée" -- each is catalogued only as "Copie".

No other item in Espagnol 142 (TOME I) or 143 (TOME II) matches "ciphered, in Spanish, or addressed to/from
Mercy, Castel-Rodrigo, Peñaranda or the Brussels secretariat 1640-1650" closely enough to probe within this
brief's budget: TOME II's own Gallica catalogue description (`dc.source all "Espagnol 143"` SRU query, 1
request) is entirely Charles V/Philip II 16th-century instructions, confirming the full-text grep above rather
than adding a new lead; TOME I's few 1640s Spanish items (Olivares' 1643 disgrace, the Nov 1641 Pays-Bas
governors' patents, the 1646 Aragon cortes papers) are Spanish-crown domestic administration, not addressed to
Mercy or the Brussels secretariat and not digitised (per the 24 Sept digitisation check), so out of reach and
out of scope this pass -- flagged, not probed.

### Image probe (Espagnol 144, ark `btv1b10035717h`)

Canvas = 2 x folio + 14 (Y5's fit, confirmed again below). Probed every canvas of the five candidate items at
`/full/600,/0/`, one at a time, >=2 s apart (two `Recv failure`/`CONNECT tunnel failed` resets, each resolved
on a single retry after a pause, same flakiness as the finding-aid fetch):

- Item 4 (F.4-6v, canvas 22-26): **all 5 canvases probed** (22, 23, 24, 25, 26) -- full plain French secretarial
  hand throughout, ink page numbers "4"-"6" visible, marginal "1639" date on canvas 22. Zero digit code groups.
- Item 6 (F.8-11v, canvas 30-36): canvas 30 already read in full by worker T (24 Sept, unciphered); canvas 34
  (ink page "10") reprobed here -- plain French, zero code groups.
- Item 7 (F.12, canvas 38): probed directly (ink page "12", marginal "1645") -- full page of plain Spanish
  prose ("Instrucçion de lo que el Sr Abbad de Mercij ha de executar..."), zero code groups.
- Item 8 (F.14-19, canvas 42-52): canvas 46 (ink page "16") probed -- plain French, zero code groups.
- Item 9-10 (F.20-21v, canvas 54-57): canvas 55 is a largely blank verso showing recto bleed-through only;
  canvas 56 (ink page "21") is item 9's Spanish opening ("Instruccion de lo que vos el Abbad de Mercij mi
  Sumiller de Cortina...savreis a Kempen para aconcertar con la Duquesa de Cheurosia y el Conde de Sant Ibal"
  -- the same addressee title, "Sumiller de Cortina", and the same two named negotiating partners, Chevreuse
  and Saint-Ibal, as the target's own reading); canvas 57 closes item 10 with a dateline, "Bruselas a 13 de
  Abril de 1648". Both fully plain Spanish prose, zero code groups.

**No leaf in this cluster carries any 2-3 digit code group.** Every item catalogued only as "Copie" (4, 6, 7,
8, 9-10) is, on the actual image, a plain-text copy -- consistent with the finding aid's own "chiffrée" tag
being accurate and exhaustive for this volume: the compiler transcribed the Mercy correspondence to clear
copies for the recueil except this one item, where the cipher original (or a copy of it) was bound in instead.
This is a direct image read, not an inference from the catalogue (rule 2): 11 canvases fetched and read.

### Result

**Pooled N: 0 siblings found, stays at 521 (the target's own count), unchanged.** No code/key coverage
percentage or random-draw control was run: rule 3's control requirement applies to an attempted decode, and no
candidate ciphertext existed anywhere in this sweep to apply `key.tsv` to (the same reporting convention Y6
used for its own no-candidate-key result). `siblings.tsv` records the six items checked (5 candidates + the
target itself) with folio, canvas range, title, date, language and the ciphered/no-code-groups finding, per
item. Images: `images/siblings/` (11 canvases at `/full/600,/0/`, ~1.2 MB, `manifest.json` with sha1;
`images/` total now 8.1 MB, well under the 30 MB budget).

**What this means for NEAR.md.** The "pools first" next step named for this target is now answered negatively
within Espagnol 142-144: there is no second ciphered leaf under this 38-value code in the same recueil to pool
with the 521-token target, at least not among the items the finding aid, read in full, points to as plausible
candidates. The target's own reading stays a single-letter, N=521 cryptanalytic result (M2), not helped or
hurt by this pass. Two follow-ups this pass did not attempt (out of the brief's scope): (1) a wider,
budget-heavier canvas-by-canvas sweep of the entire 605-canvas ark rather than just the name-matched cluster,
in case an unrelated ciphered item sits elsewhere in the volume; (2) TOME I's undigitised 1640s Spanish items
(Olivares, Aragon cortes), which would need a copy order or a different digitisation route before they could
be checked at all.

Requests this section: archivesetmanuscrits.bnf.fr 1 (2 retries after connection resets). gallica.bnf.fr 13
IIIF image fetches (11 successful, 2 retried after resets) + 1 SRU query = 14. No other hosts. No subagents.

## V6-MERCY verifier note (25 Sept 2026, LANE V6)

Novelty class **N3**, key **ours**, evidence moderate (cryptanalytic, S/M only; judge cannot decide; crib-gain gate
not met numerically). See AUDIT.md for the class, the safe sentence and the search log; describe this item outside
the repo only in AUDIT.md's safe sentence. Two wording corrections for readers of this file: (1) the item is
Espagnol **144** f.22, not 142 (the folder name is historical); (2) the spec's "likely Peñaranda/Castel-Rodrigo
office per the finding aid" is not what the finding aid says -- its sibling items 9-10 are "remises par
Léopold-Guillaume", and Lonchay 1896 p.445 makes Mercy Archduke Leopold Wilhelm's chaplain, so the sender is best
inferred as Leopold Wilhelm's secretariat (inference: the leaf is unsigned). The five 19->14 exceptions that produce
"Cheureuse"/"Cleues" were made by the reader; a blind eye-check is owed before they go to S (AUDIT.md section 3).
Status word unchanged: open.

## MREV: blind split applied (25 Sept 2026, LANE R7)

R7-MEYE's independent blind re-transcription (`meye/`) agreed with the reader's `exceptions.tsv` 19->14 correction
at r06:14 and r17:5, but read `19` (not the exception's `14`) at r14:7, r16:3 and r16:6 -- 3 of 3 blind passes now
say `19` at those three positions, against only the non-blind M2 re-read saying `14`. Per the brief, the reading now
follows the blind majority: `exceptions.tsv` keeps only r06:14 and r17:5 (both graded M, reason updated to note the
blind agreement), and the other three revert to the key's plain `19`->`e`.

**(1) Word changes, 19-vs-14 split (`exceptions.tsv` 5 -> 2 rows):**

| line | pos | code before | code after | word before | word after |
|---|---|---|---|---|---|
| r14 | 7 | 14 (exception) | 19 (key) | CLEUES | ELEUES |
| r16 | 3 | 14 (exception) | 19 (key) | CON | EON |
| r16 | 6 | 14 (exception) | 19 (key) | CO | EO |

r06:14 (CHEUREUSE) and r17:5 unchanged, kept at `14` with the exception now citing "blind re-read R7-MEYE agrees".
`python3 tools/decode_key.py ciphers/espagnol142-mercy-1648` regenerated cleanly; `--check` exits 0.

**(2) v07 pos15-16 token-count mismatch, settled two tokens.** Zoomed to 4x on `images/f22v_canvas59.jpg`
(canvas x~2650-3300, y~1390-1630, the segment after the settled "...10" at v07 pos14): the image shows a closed-loop
digit ("3") and a separate two-stroke digit ("1" then "7") as two distinct, clearly space-separated glyphs, not one
"7" -- confirms R7-MEYE's blind read (`meye/compare.tsv` COUNT MISMATCH row) over the settled single-token `7`.
Both original blind passes (`passA.tsv`, `passB.tsv`) had already flagged this exact spot `m`/"ambiguous mark or
digit... read as 7 per convention", i.e. neither pass was confident in the single-token reading either. Recorded in
`corrections.tsv` step 11 (never silently edited `ciphertext.tsv`): `ciphertext.tsv` v07 pos15 changed from one `H`
token (`7`) to two `M` tokens (`3`, `17`), and the old pos16 (`22`) renumbered to pos17. Word change:

| line | pos | before | after |
|---|---|---|---|
| v07 | 15-17 (was 15-16) | TG | PAG |

Regenerated; `--check` exits 0.

**(3) Judge (rule 7, pasted), after both changes:**

```
$ python3 tools/judge_plaintext.py specs/espagnol142-mercy-1648.json --file ciphers/espagnol142-mercy-1648/reading.txt
ok   length: got=1342, min=200, max=1000000000
FAIL language: score=-1.031, null_p99=-1.911, real_p05=-0.873, real_median=-0.811, mode=both, N=1342
FAIL - espagnol142-mercy-1648 (a PASS is a gate for a verifier, not a reading; rule 10)
```

Essentially unchanged from the pre-MREV FAIL (-1.034 at N=1341, this file's own earlier "Judge" section above):
four letter changes and one added token do not move a 1342-letter score. Not re-run against the crib-loop control
(out of this job's scope) or a register-matched corpus (still not built for this letter, per the earlier section).

**New grade counts (rule 4).** Before this job (LANE R6 M2, committed): tokens 521, H 0 C 0 S 494 M 27 I 0 U 0.
After both changes: **tokens 522, H 0 C 0 S 496 M 26 I 0 U 0** (net: 3 exceptions removed drop 3 M -> S at their
positions; the v07 split adds 1 token and turns 1 S into 2 M). `reading.txt`, `reading_tokens.tsv` regenerated;
`tools/decode_key.py ciphers/espagnol142-mercy-1648 --check` exits 0.

Grade: cryptanalytic (S/M per rule 4, no H or C). Not classifying novelty (rule 10) -- AUDIT.md is LANE V6's file
and was not touched here. Search log: nothing searched this pass (disk-only edit of an existing transcription
against images already on disk); no hosts, no subagents.

## IA-BORROW: correspondancede0006jose p.647, 25 Sept 2026

parent worker IA-BORROW (Sonnet, session_01DzmCQYEVbNRHz3etXbHcrV), per ASKS row 59. Attempted to borrow
`correspondancede0006jose` (Cuvelier-Lefèvre, *Correspondance de la Cour d'Espagne VI*, 1937) and read p.647
(the index entry for Mercy) to confirm or correct the Fable verifier's existing be-api snippet.

**Result: borrow succeeds, page cannot be read by script.** `browse_book` returns `{"success": true}` (this
also surfaced and fixed a live bug in `tools/ia_borrow.py`: it previously never checked the JSON `success`
field, only the HTTP status). But `<id>_page_numbers.json`, which would map the printed page number 647 to a
BookReaderJSIA leaf index, answers HTTP 403 even with the loan active and a valid `loan-<id>` token -- there is
no script route to that mapping. A leaf fetched anyway (leaf 300 of 944, chosen arbitrarily to test the image
endpoint, not because it is near p.647) came back with an `X-Obfuscate` header and no JPEG magic bytes: the
image is obfuscated for the archive.org web reader, confirming the 23-24 Sept 2026 finding (CLAUDE.md, ASKS
row 18) holds for this item specifically, not only in general. Loan returned immediately after each test
(two short loans held this session, both < 2 minutes, both returned).

**No new page-647 text beyond what ASKS row 59 already has** (the be-api full-text snippet: "... chiffre a cet
effet. Il en est de même de l'abbé de Mercy qui a été envoyé par Léopold-Guillaume pour traiter ..."). Did not
attempt a fresh be-api query for pp.15/20 in this pass (out of the borrow test's scope once the page-image
route was confirmed closed; a plain be-api search for "Mercy" against this identifier would find any further
snippets without borrowing).

**Still: the owner is the only route to page 647's actual text** (ASKS row 59 unchanged, status still `open` --
this pass could not move it). Job stopped after this item per its brief: item 2 in the same job
(`sim_cryptologia_1981-04_5_2`) hard-failed the borrow step itself (HTTP 400, print-disabled tier, not this
target's problem) -- see CLAUDE.md's Internet Archive paragraph, dated 25 Sept 2026, for the full finding.
Items 3-5 of that job (hamilton-1650, dorabella-1897, koehler-1944/Farago) were not attempted.

## Local runner L20 (26 Sept 2026)

LOCAL-QUEUE.tsv row L20 (ASKS row 59, NEAR.md row step (3)) asked the owner's desk runner to borrow
`archive.org/details/correspondancede0006jose` for one hour and read p.647 and its index entries: does the
volume quote, summarise or merely list the 6 June 1648 instruction to the abbé de Mercy?

**Answer: negative -- p.647 does not quote, summarise or discuss the target instruction at all.** The runner's
full transcript (PR 24, closed without merge; saved as `local-runner/L20-2026-09-26.md`):

Printed p.647 (reader position 662/943) is entry 1499, dated Munster, 11 June 1648, Peñaranda to Philip IV --
a different letter, five days after the target's 6 June 1648 date, and not by or to Mercy. Its French
editorial summary reports Brun's correspondence with Schwartzemberg and possession of a cipher, then makes the
same connection for Mercy: "[Mercy] a été envoyé par Léopold-Guillaume pour traiter avec la duchesse de
Chevreuse" -- a note about Mercy's own mission (negotiating with the duchesse de Chevreuse on the Archduke's
behalf), not a quotation, summary or listing of the 6 June instruction. Its own source citation is Documentos
Ineditos vol. 84, p.258, not this volume.

The index (printed p.901) lists "MERCY (L'abbé de), 647, 15, 20" -- but 15 and 20 there are marginal line
references *within* p.647's own entry, not separate pages; the runner checked printed pp.15 and 20 directly
regardless and found they concern 1599, unrelated. So the index's only real hit for Mercy is the same p.647
entry above, which is not the target instruction.

This settles the question ASKS row 59 raised as cleanly as a negative can: the one edition our search
identified as citing "Mercy, 647" prints no trace of the 6 June 1648 Barneton instruction at that page, its
index has no other page for Mercy, and the passage that does mention him is about an unrelated later letter.
It does not move the V6-MERCY2 N3 classification (this is a "not printed here" result, not a fresh search of
new sources), and it does not supply a period-key or sender crib. Outreach gate 2 for this target (a second
adversarial audit plus JSTOR rows) still needs the JSTOR-QUEUE rows 80-83 answer before any outward note.

Gate: `tools/lq_answer_check.py ciphers/espagnol142-mercy-1648/local-runner/L20-2026-09-26.md --row L20` exits
0 (kind `ia-reader` -- a content read of a page already in hand, no catalogue-ladder rungs required; see
`tools/lq_answer_check.py`'s kind-awareness fix, 26 Sept 2026, UPDATES.md).

## MERCY-KEY (27 Sept 2026)

Parent worker MERCY-KEY (Sonnet, session_014APEYAjz8BFqwZkXdEM1ho), for parent 7n
(`.claude/briefs/runs/2026-09-27-parent-ytbiz-mercy-key.md`). Acquisition lookup only: no decoding, no
key.tsv change, no novelty wording. `date -u` 18:45 UTC. Intake gate re-run:
`espagnol142-mercy-1648: partial (line 1) -- edition/page or full-text-search citation found within 6
lines` (pass). `tools/key_livecheck.py`: 9 present, 6 working (unchanged from parent's last probe).

### U1: DECODE records 958-965 (Brussels SEE "chiffres 1647-98", inv.nr. 2), login-free RecordsView fetch

Fetched `RecordsView/<id>` for all 8 ids with plain curl (descriptive User-Agent, no cookies, no login --
per CLAUDE.md's DECODE table and `sources/decode/NOTES.md`'s confirmed login-free RecordsView route), HTTP
200 on every one, saved under `sources/decode/mercy-key-2026-09-27/record_<id>.html`.

| id | Name | Receiver | Dates | Cipher Type | Symbol Sets | Nomenclature size | Code length | Pages |
|---|---|---|---|---|---|---|---|---|
| 958 | ...key1 | "Dug. de Nienburg" | 1647-1698 (no narrower date given) | Homophonic substitution, Nomenclatures | Alphabet, Numerical | 21-50 | Fixed | 1 |
| 959 | ...key2 | "Conde de Cantecroy" | 1647-1698 | Nomenclatures | Numerical | >100 | Variable | 2 |
| 960 | ...key3 | (none) | 1647-1698 | Simple substitution, Nomenclatures | Alphabet, Graphic signs, Numerical | >100 | Variable | 1 |
| 961 | ...key4 | (none) | 1647-1698 | Nomenclatures | Numerical | >100 | Variable | 1 |
| 962 | ...key5 | (none) | 1647-1698 | Homophonic substitution | Numerical | >100 | Variable | 1 |
| 963 | ...key6 | (none) | 1647-1698 | Nomenclatures | Numerical | >100 | Fixed | 2 |
| 964 | ...key7 | (none) | 1647-1698 | Nomenclatures | Numerical | >100 | Variable | 2 |
| 965 | ...key8 | (none) | 1647-1698 | Homophonic substitution, Nomenclatures | Alphabet, Graphic signs, Numerical | >100 | Variable | 6 |

All eight are the same accession, DECODE record type **Key** (not a ciphertext letter), Holder "Algemeen
Rijksarchief, Secretairerie d'Etat et de Guerre, inv.nr. 2" (964: inv.nr. 2559), Cleartext/Plaintext language
Spanish for all eight. No record carries a date narrower than the whole series range (1 Jan 1647 - 31 Dec
1698); none names 1648, June, Barneton, Mercy or the Archduke/Cardenal-Infante's secretariat as sender or
receiver. Record 958's own "Additional Information" field: "A homophonic substitution cip[h]er with
homophones only for the vowels and a small nomenclature, 50 codegroups in sum total. Two-digit numbers are
reserved for the cipher, capital letters for the nomenclat[u]re." -- i.e. 958's cipher portion is exclusively
two-digit numbers with capital-letter codes reserved for a separate ~20-item name nomenclature, structurally
unlike our target's key.tsv (38 values total, no capital-letter/alphabet symbol class, no separate nomenclature
class -- personal/place names in the R6/R7 reading are spelled out letter-by-letter, not coded). The other
seven records all carry nomenclature size ">100", more than double our target's total code count, and six of
the eight are majority or wholly "Nomenclatures" in cipher type rather than a plain letter substitution.

### U2: thumbnail eye-check against our 38-symbol inventory

Fetched each record's one listed thumbnail (`/decrypt-custom/filesrv/?file=TH_IMG_R<id>_I<n>_P1.png`, the
`<img src>` embedded in the RecordsView page, login-free, confirmed distinct real images per record --
HTTP 200, 200x284px (965: 200x285px) each, saved as `sources/decode/mercy-key-2026-09-27/thumb_<id>.png`.

Two vision calls used (per the brief's cap), on the two records closest to our target by the U1 table: **958**
(nomenclature size 21-50, the only one near our K=38) and **965** (6 pages, the largest sheet in the series,
also Alphabet+Numerical+Graphic-signs like 958). Both are **unreadable at thumbnail size** for a symbol-shape
comparison: 958 shows only that the page holds two blocks of writing/a small table at the top and a line of
cursive prose below; 965 shows a dense multi-column table (consistent with its ">100"-entry nomenclature) but
every cell is illegible texture at 200x284px -- no individual digit, letter or graphic-sign shape can be made
out in either. DECODE serves no larger image to this account (`sources/decode/NOTES.md`, confirmed
account-wide, not per-record); per the brief, this counts as "unreadable at thumbnail size", not a negative
finding on its own, but it also could not supply a positive symbol match for outcome (a) even if the U1
design fields were closer than they are. The other six thumbnails were fetched (for the record) but not
opened with a vision call, since U1 already places them further from our design (nomenclature size >100,
mostly pure "Nomenclatures") than 958/965.

**Outcome: (b).** None of the 8 records fits by design: our target is a fixed-length, all-numeric, 38-value
simple/homophonic substitution with no separate nomenclature class, and every one of the 958-965 series is
either a mixed alphabet+numeric+capital-letter system with a distinct ~20-entry nomenclature (958) or a
>100-entry nomenclature-dominated key (959-965) at more than double our target's code count. This is a design
mismatch established from the records' own catalogued fields (U1), independent of the thumbnail step; the
thumbnails (U2) additionally could not be read at their served resolution, so no symbol-shape confirmation
either way was possible for any record. A logged negative for this key family at this resolution: the 1647-98
Brussels SEE series does not supply a period key for espagnol142-mercy-1648's cipher as catalogued, and DECODE
serves nothing larger to this account to re-check. No login was attempted (per the brief and CLAUDE.md).

### U3: Gayangos, *Catalogue of the Manuscripts in the Spanish Language in the British Museum* (Internet
Archive, public domain, 4 vols)

Located all four volumes on IA (vol. 2's djvu text is under a different identifier than the other three's
numbering suggests): vol.1 `manuscriptsinspa01brit`, vol.2 `catalogueofmanu02brit`, vol.3
`manuscriptsinspa03brit`, vol.4 `manuscriptsinspa04brit`. Downloaded each `_djvu.txt` (2.7MB/2.5MB/2.5MB/1.0MB)
and grepped locally (script, not a model read) for "Mercy", "Barneton" and "Warneton", case-insensitive.

"Barneton"/"Warneton": **0 hits in all four volumes.**

"Mercy": several hits, all either the common noun ("mercy", "Order of Mercy" religious order) or already-known
unrelated Mercy references, except one:

- **Vol. 1, item 146 (British Museum Add. MS 14,000, f.554; the same manuscript catalogued in items 121-151,
  ff.5-557, xvii cent. tracts on Franco-Spanish-Imperial affairs):** *"Memoria de los puntos de que el abbad
  de Mercy ha de dar quenta á Su A. E. y á los ministros de Su Magestad en virtud de las cartas de creencia
  que ti[e]ne para S. Al., y Don Miguel de Salamanca[,] de los duques de Guisa [Lorena] y de Bullón [Latour
  d'Auvergne]"* -- undated in its own entry, but bracketed by items dated 14-25 Feb 1641 (nos. 140, 145) and
  before item 147/148/149/150 (Sedan treaty articles, 10 March 1641): this item is from the **1641** Sarmiento
  de Acuña / Cardinal-Infante Fernando negotiations with the exiled Ducs de Guise and Bouillon at Sedan, not
  the 1648 Leopold Wilhelm / Cleves-Brandenburg mission our target concerns -- a different abbé de Mercy
  mission, seven years earlier, already the same conclusion AUDIT.md section 4 drew from Google Books snippets
  of this same volume ("Gayangos lists a different BM instruction to 'el abbad de Mercy'... no hit on this
  instruction"). No "en cifra"/"cifrado"/"descifrado" language appears in or near item 146's own entry (the
  nearest cipher-related item in the same manuscript, no. 137, is a separate 1642 Felipe IV-to-Sarmiento
  deciphered letter, f.536, unrelated to Mercy). Excerpt (surrounding items, full grep counts per volume) in
  `sources/decode/mercy-key-2026-09-27/gayangos_excerpt.txt`; full volumes not committed (Usage item 5,
  "digests not repositories" -- re-fetchable at `archive.org/download/<id>/<id>_djvu.txt` for
  manuscriptsinspa01brit, catalogueofmanu02brit, manuscriptsinspa03brit, manuscriptsinspa04brit).

No hit anywhere in the four volumes ties a ciphered instruction to *our* Mercy (1648, Leopold Wilhelm's
secretariat, Cleves/Brandenburg) or to Barneton. This closes out AUDIT.md section 6's Gayangos lead as
checked and negative for a sibling under the same 38-value code; the 1641 item 146 is a different mission by
the same named figure, itself uncoded as catalogued.

### Requests this pass

de-crypt.org: 16 (8 RecordsView + 8 thumbnails), all >=1.8s apart, one at a time, well under the 25-request
cap. No login. archive.org/be-api.us.archive.org: 19 (2 advancedsearch, 5 metadata, 4 djvu.txt downloads, 4
be-api fts sanity checks read but not relied on -- CLAUDE.md's be-api `page_num` caveat, so the djvu.txt grep
was used as the citable result, not the fts snippets, plus 4 more requests locating/confirming volume
identifiers), all >=1.6s apart, one at a time.

Status unchanged: `partial`. AUDIT.md not touched (the parent hands this to the verifier lane per the brief).
NEAR.md not edited: the brief updates its next-step cell only for outcome (a); this is (b)/(c), so the row's
existing "DECODE R958-R965... waits on the DECODE role upgrade (ASKS 1)" line is now stale (no role upgrade
was needed -- all 8 were read login-free) and is left for the parent to correct, reported in the ROOM done
line.

## MERCY-JUDGE2: widened judge corpus, validation only (27 Sept 2026)

parent worker MERCY-JUDGE2 (Sonnet). Brief: `.claude/briefs/runs/2026-09-27-parent-ytbiz-mercy-judge2.md`
(parent 7n, "Effort allocation" validation item, after the owner asked what can move this target while the
Brussels SEE t.LXIV f.16 copy is awaited). Internet Archive only, disk otherwise. Start 18:45 UTC per `date -u`.
No decoding, no key or reading change -- `reading.txt`, `key.tsv`, `ciphertext.tsv` and AUDIT.md untouched.

**U1: found all four other Cartas tomes and built `tools/data/es17c7/`.** es17c already held tomos V-VII
(MHE XVII-XIX, 1643-1647); the other four (Cartas I-IV = MHE tomos XIII-XVI, 1634 - early 1643) are on Internet
Archive in the same `realuoft` (University of Toronto) scan series, confirmed by each volume's own printed
front matter ("CARTAS DE ALGUNOS PP. DE LA COMPAÑÍA DE JESÚS ... TOMO [I-IV]" with its own stated date range)
before fetching in full. Hold-out grep (Mercy/Mercij, Barneton, Sumiller, Brandenburg) on all four: zero
Mercy/Mercij/Barneton hits, one generic "sumiller de Corps" (a different court office, different person) -- the
same non-hit shape es17c's own three tomes already showed, expected since these four tomes (1634-1643) predate
the target's 1648 letter and even Leopold Wilhelm's 1647 arrival as governor-general. Cleaned the same way as
es17c (front matter cut before each volume's own `CARTAS` heading; no back-matter index in any of the four,
unlike tomo XIX). `tools/data/es17c7/` now holds all seven tomes, 4,923,218 folded letters (es17c's three files
copied in byte-identical, confirmed by matching sha1). Wired into `tools/judge_plaintext.py` as a new
`LANG_CORPORA["es17c7"]` key (es17c and es (default) both unchanged). `--selftest` passes. Full build log,
MANIFEST.tsv and hold-out detail: `tools/data/es17c7/README.md`.

**U2: leave-one-file-out false-negative rate, es17c (3 folds) vs es17c7 (7 folds), both run this pass.**
```
es17c:
held_out=memorialhistri17realuoft.txt.gz N=519 samples=200 real_p05=-0.847 false_negatives=79/200 (39.5%)
held_out=memorialhistri18realuoft.txt.gz N=519 samples=200 real_p05=-0.866 false_negatives=42/200 (21.0%)
held_out=memorialhistri19realuoft.txt.gz N=519 samples=200 real_p05=-0.892 false_negatives=20/200 (10.0%)
TOTAL false-negative rate: 141/600 (23.5%)

es17c7:
held_out=memorialhistri13realuoft.txt.gz N=519 samples=200 real_p05=-0.878 false_negatives=21/200 (10.5%)
held_out=memorialhistri14realuoft.txt.gz N=519 samples=200 real_p05=-0.866 false_negatives=21/200 (10.5%)
held_out=memorialhistri15realuoft.txt.gz N=519 samples=200 real_p05=-0.882 false_negatives=15/200 (7.5%)
held_out=memorialhistri16realuoft.txt.gz N=519 samples=200 real_p05=-0.902 false_negatives=4/200 (2.0%)
held_out=memorialhistri17realuoft.txt.gz N=519 samples=200 real_p05=-0.867 false_negatives=46/200 (23.0%)
held_out=memorialhistri18realuoft.txt.gz N=519 samples=200 real_p05=-0.869 false_negatives=29/200 (14.5%)
held_out=memorialhistri19realuoft.txt.gz N=519 samples=200 real_p05=-0.872 false_negatives=20/200 (10.0%)
TOTAL false-negative rate: 156/1400 (11.1%)
per-fold spread: 2.0-23.0% (11.5x)
```
Blended rate roughly halved (23.5% -> 11.1%), but per-fold spread widened relative to itself (3.95x on es17c's
three folds vs 11.5x on es17c7's seven): tomo XVI's fold reads very clean (2.0%) but tomo XVII's, now trained on
six other tomes instead of two, is still the single worst fold (23.0%, though better than its 39.5% inside
es17c). A wide per-fold spread means the blended number is not trustworthy on its own, whichever direction it
moved (CLAUDE.md rule 3, es17c/MJ and es17c/EN-FOLDS paragraphs).

**Pre-registered gate (per the brief, set before U3 ran):** the judge is a gate only if es17c7's blended
false-negative rate is under 10% with a per-fold spread under 2x, AND the clear words PASS; otherwise the
verdict is "judge cannot decide" whatever the reading scores. **Neither corpus-quality leg is met** (11.1% is
over the 10% line; 11.5x is far over the 2x line) -- outcome (c), verdict stands "judge cannot decide"
regardless of what U3 finds. U3 was still run and is reported below, per the brief ("the conditions do not
hold -- 'judge cannot decide' stands, with the numbers").

**U3: reading, clear words and 20 shuffled nulls, through es17c7** (spec variant
`{"judge": {"language": "es17c7", "letters_min": 200, "control_samples": 200}}`, not committed as a separate
`specs/` file, matching es17c's own convention):
```
$ python3 tools/judge_plaintext.py <es17c7 spec variant> --file ciphers/espagnol142-mercy-1648/reading.txt
ok   length: got=1342, min=200, max=1000000000
FAIL language: score=-1.027, null_p99=-1.961, real_p05=-0.858, real_median=-0.789, mode=both, N=1342
FAIL - espagnol142-mercy-1648-es17c7-variant (a PASS is a gate for a verifier, not a reading; rule 10)

$ python3 tools/judge_plaintext.py <es17c7 spec variant> --file ciphers/espagnol142-mercy-1648/m2/clear_words_only.txt
ok   length: got=782, min=200, max=1000000000
FAIL language: score=-0.889, null_p99=-1.937, real_p05=-0.87, real_median=-0.795, mode=both, N=782
FAIL - espagnol142-mercy-1648-es17c7-variant (a PASS is a gate for a verifier, not a reading; rule 10)
```
The clear words FAIL by a similarly thin margin as under both es17 (-0.892 vs -0.888, 0.004 gap) and es17c
(-0.891 vs -0.867, 0.024 gap): here -0.889 vs -0.870, a 0.019 gap. Widening the corpus did not flip this FAIL
to a PASS either, so gate leg 2 (clear words PASS) also fails.

**20 shuffled nulls** (the reading's own N=1342 folded letters, comment header lines stripped the same way the
CLI strips them, shuffled with 20 different seeds -- order destroyed, letter multiset unchanged -- scored
through the same es17c7 model):
```
null seed=1  N=1342 score=-2.082 null_p99=-1.961 real_p05=-0.858 FAIL
null seed=2  N=1342 score=-2.047 null_p99=-1.961 real_p05=-0.858 FAIL
null seed=3  N=1342 score=-2.011 null_p99=-1.961 real_p05=-0.858 FAIL
null seed=4  N=1342 score=-2.056 null_p99=-1.961 real_p05=-0.858 FAIL
null seed=5  N=1342 score=-2.030 null_p99=-1.961 real_p05=-0.858 FAIL
null seed=6  N=1342 score=-2.103 null_p99=-1.961 real_p05=-0.858 FAIL
null seed=7  N=1342 score=-2.045 null_p99=-1.961 real_p05=-0.858 FAIL
null seed=8  N=1342 score=-2.038 null_p99=-1.961 real_p05=-0.858 FAIL
null seed=9  N=1342 score=-2.026 null_p99=-1.961 real_p05=-0.858 FAIL
null seed=10 N=1342 score=-2.007 null_p99=-1.961 real_p05=-0.858 FAIL
null seed=11 N=1342 score=-2.037 null_p99=-1.961 real_p05=-0.858 FAIL
null seed=12 N=1342 score=-1.996 null_p99=-1.961 real_p05=-0.858 FAIL
null seed=13 N=1342 score=-2.032 null_p99=-1.961 real_p05=-0.858 FAIL
null seed=14 N=1342 score=-2.035 null_p99=-1.961 real_p05=-0.858 FAIL
null seed=15 N=1342 score=-2.049 null_p99=-1.961 real_p05=-0.858 FAIL
null seed=16 N=1342 score=-2.037 null_p99=-1.961 real_p05=-0.858 FAIL
null seed=17 N=1342 score=-2.078 null_p99=-1.961 real_p05=-0.858 FAIL
null seed=18 N=1342 score=-2.034 null_p99=-1.961 real_p05=-0.858 FAIL
null seed=19 N=1342 score=-2.066 null_p99=-1.961 real_p05=-0.858 FAIL
null seed=20 N=1342 score=-2.096 null_p99=-1.961 real_p05=-0.858 FAIL
```
0/20 PASS; scores range -2.103 to -1.996, all below `null_p99` -1.961. The judge does separate the reading's
own letter order from a scramble of the same letters at this N (a necessary condition for it to be informative
at all), but that is not sufficient given the corpus-quality gate above -- the verdict stays "judge cannot
decide", not a PASS or a real negative.

**Outcome (c):** the pre-registered conditions do not hold (blended rate 11.1% >= 10%; per-fold spread 11.5x
>= 2x; clear words still FAIL). "Judge cannot decide" stands for this target at N~519-1342, with the numbers
above superseding es17c's own less-reliable three-fold figure as the current best estimate of this judge
family's own reliability at this era/register. Neither a PASS nor a FAIL against es17c or es17c7 should be read
as informative for this target until a homogeneity split (by correspondent or date range within a tomo, not
just tomo count) is tried -- named as the next cheap step in `tools/data/es17c7/README.md`, not attempted here
(out of this validation-only job's scope). Status word unchanged: **partial** (NEAR.md, no change to the
reading, no change to AUDIT.md's N3/ours classification). The corpus (`tools/data/es17c7/`) stays on disk for
the next era/register-matched target's own judge check.

Search log: no new external search beyond the U1 hold-out grep above (this job's own AUDIT.md is untouched;
novelty classification is the verifier's job, not run here). Requests: archive.org 4 `advancedsearch.php`/
`metadata` lookups, 4 `_djvu.txt` downloads, all >=1.6s apart, descriptive UA (8 of the brief's 30-request
allowance). No subagents. No credentials.

## While waiting (27 Sept 2026, WAIT-PASS-A)

Waits on the AGR quote for SEE t. LXIV f.16 (ASKS row 60), drafted 26 Sept 2026, gate 7 then the owner sends,
since 25-26 Sept 2026.

- Run the homogeneity split (correspondent/date range within a tomo) `es17c7/README.md` names as the next cheap step, before trusting a further judge FAIL/PASS. M.
- Flag for the parent: NEAR.md's own next-step line ("DECODE R958-R965... waits on the DECODE role upgrade, ASKS 1") is stale -- all 8 were read login-free this pass with no role upgrade needed, per this NOTES.md's own MERCY-DECODE section. S (a correction, not a reading change).
- Re-run the M2 crib-loop gain-gate test (rule 3) through es17c7 instead of the original es17, now that es17c7 is the better-calibrated corpus, to see whether the numeric gain-gate result changes. M.

## Campaign step H1 (2026-09-27 22:12-22:2x UTC, campaign runner account 2, session_01V7xEY9JxjCxiXnQLtjFnfL)

**Status unchanged: partial.** CAMPAIGN.md H1: the exact-frequency-profile control Y8 flagged on 25 Sept 2026 and
never ran (its scratch attempt produced K=307-320 instead of 38). Question: does the target's anneal score
(-1154.3, es17 model, K=38, N=521, `cheap_test_1/rerun.sh`) still beat a real Spanish text enciphered with the
target's *own* 38-code occurrence multiset (57/42/41/39/38/27/.../2/1/1/1/1/1), or was the 167-181-point gap over
Y8's frequency-allotted control carried by the skewed profile alone? Pre-registered pass (CAMPAIGN.md): target
beats the stricter control by more than 2x the control's own inter-seed spread.

**Tool.** `tools/homophonic_anneal.py --control PLAIN.txt --profile CIPHER.tsv` (new option, this step; offline test
`tools/tests/test_homophonic_anneal_profile.py`): reads the profile cipher's sign counts, searches PLAIN.txt (seeded
random window starts) for an N-letter window whose letter counts partition exactly by those counts (backtracking,
largest counts first), assigns each count to its letter as one sign, enciphers each occurrence by a homophone drawn
in proportion to remaining quota, so every sign ends at exactly its profile count (asserted; `sign_counts ==
profile_counts` in every JSON below). Same solver settings as Y8 throughout: order 3, 8 restarts x 40,000 iters,
`--skip NONE`. Profile taken from `cipher_codes.tsv` as annealed in Y8 (N=521, K=38) -- note that file is one token
behind `ciphertext.tsv` (522 code tokens after MREV's v07 split); like-for-like with -1154.3 needs the 521 version,
and regenerating it is H3's business.

**Results (best score of 8 restarts per run; share = letters of the control plaintext recovered blind).**

| model | run | seeds | best scores | mean | share |
|---|---|---|---|---|---|
| es17 (Y8's) | target (on file, Y8) | 2,3,5 | -1154.3 | -1154.3 | -- |
| es17 | Y8 freq-allotted control (on file) | 1-5 | -1321.7..-1356.6 | -1336.2 | 36-81% |
| es17 | R7-MSHUF full shuffle (on file) | 1-5 | -1474.3..-1505.6 | -1488.5 | -- |
| es17 | **exact-profile control, Don Quijote window (in-sample)** | 1-5 | -1063.8, -1071.3, -1099.5, -1109.7, -1078.0 | **-1084.4** | 93-99% |
| es17 | **exact-profile control, Cartas t.13 window (out-of-sample)** | 1-5 | -1159.6, -1088.2, -1106.3, -1227.8, -1119.8 | **-1140.4** | 91-98% |
| es17 | exact-profile control, Cartas window, 5% signs corrupted | 1-3 | -1279.5, -1157.2, -1173.7 | -1203.5 | 77-93% |
| es17 | exact-profile control, DQ window, 5% signs corrupted | 1-3 | -1146.7, -1200.4, -1291.6 | -1212.9 | 30-92% |
| es17 | exact-profile control, Cartas window, 10% corrupted | 1-3 | -1330.9, -1282.5, -1245.1 | -1286.2 | 50-81% |
| es17 | exact-profile control, DQ window, 10% corrupted | 1-3 | -1235.4, -1200.3, -1298.0 | -1244.6 | 63-88% |
| es17c7 (MERCY-JUDGE2's) | target | 2,3,5 | -1138.5 x3 (same optimum every seed) | -1138.5 | -- |
| es17c7 | exact-profile control, DQ window (out-of-sample) | 1-5 | -1139.2, -1094.6, -1168.0, -1137.0, -1221.4 | -1152.0 | 82-98% |
| es17c7 | exact-profile control, Cartas t.13 window (in-sample) | 1-3 | -1300.7 (anneal stuck, 25%), -1064.8, -1095.1 | -1153.5 | 25-98% |

Files: `cheap_test_1/exactprof_k38_seed{1..5}.json`, `exactprof_k38_oos_cartas13_seed{1..5}.json`,
`target_marks_es17c7_seed{2,3,5}.json`, `exactprof_k38_es17c7_oos_dq_seed{1..5}.json`,
`exactprof_k38_es17c7_ins_cartas13_seed{1..3}.json`, `noisy/exactprof_{cartas13,dq}_n{0.05,0.10}_seed{1..3}.{tsv,json}`
(the noisy TSVs carry a `.plain` sidecar with the window's true text); `cheap_test_1/exactprof_noisy.py` builds the
corrupted controls (a corrupted position takes a sign drawn from the profile's own distribution); commands appended
to `cheap_test_1/rerun.sh`. Corpora decompressed to scratch, never committed.

**Verdict on H1's gate: not met.** The target does not beat the exact-profile control at all: under es17 it sits
14 points *below* the out-of-sample control mean (-1154.3 vs -1140.4) and inside that band (-1227.8..-1088.2), 70
points below the in-sample mean; under es17c7 it sits 13 points *above* the out-of-sample mean (-1138.5 vs -1152.0),
again inside the band. Y8's 167-181-point gap over the frequency-allotted control was carried by the profile: a
real Spanish text enciphered with this skewed multiset (frequent letters nearly monoalphabetic) anneals 200-250
points better than one with homophones allotted by frequency, and reads 91-99% blind. Y8's sentence "more
decryptable toward Spanish than a real Spanish text of the same shape typically is" is therefore withdrawn -- the
correct comparison shape is this one, and on it the target is indistinguishable from a real text. R7-MSHUF's
finding stands unchanged (shuffled target -1488 is far below every control here: the target's order carries real
structure).

**What the error bracket adds (rule 3, the SALV-DIAG paragraph).** The target's transcription carries a measured
4.7% two-pass disagreement (Y6) and 5% blind-recheck disagreement (R7-MEYE). Clean exact-profile controls
out-of-sample average -1140 and read 91-98%; at 5% corrupted signs they average -1204..-1213 and read 77-93%
(one stuck run at 30%); at 10% they average -1245..-1286 and read 50-88%. The target's -1154.3, reproduced at the
same optimum by most seeds, lies between the clean band and the 5% band, nearer the clean one. So, *if* the design
is a flat homophonic substitution as assumed, the anneal behaves as it does on a real Spanish text with about 0-5%
misread signs -- consistent with the transcription's own measured error and with a decode that is mostly right but
not judge-clean (the controls at this score read 85-98% of letters; a decode at that level of a text full of proper
names would FAIL the judge the way `reading.txt` does). This is a calibration statement about the solver, not a
grade for any token of `reading.txt` (grades unchanged: S 496, M 26, H 0, C 0 of 522).

**Solver reliability note.** Even on clean in-sample text, one seed in 13 sticks in a bad optimum (es17c7 Cartas
seed 1: -1300.7, 25% read, with the other restarts no better); 8 restarts are not always enough at N=521, K=38.
A control mean quoted from 3 seeds can hide this; the tables above give every seed.

**Consequences for the ranking.** The two highest-leverage steps are now the transcription re-checks (H2's targeted
rare-code/stretch re-crop, H6's blind second pass on r16-r17 and v04): the bracket says every percent of misread
sign costs about 12-15 anneal points and 2-3% of letters, and the unread stretches are where the reading fails.
New H9: run the target with `--noise 0.05` (the error-tolerant solve, which names the positions it corrects) and
hand H2 that list of positions to eye-check first. H3 (re-run with the 29 held codes on the 522-token file) also
regenerates `cipher_codes.tsv` from the current `ciphertext.tsv`. H4/H5 move down: the judge corpus is not what
limits this target now, and the word-code question is subsumed by H2's eye-check of the same five codes.

Requests: none (disk only, no hosts). Subagents: none. Cost: est 3 USD (session cost not readable from inside
the runner; the orchestrator's `get_session` figure is the one of record).

## Campaign step H2 (2026-09-27 23:12-23:3x UTC, campaign runner account 2, session_01V7xEY9JxjCxiXnQLtjFnfL)

**Status unchanged: partial.** CAMPAIGN.md H2: targeted 4x re-crop and blind re-check of the rare codes (48, 52, 65,
72), the two marks, the v04 unread stretch and r16-r17, against `images/f22r_canvas58.jpg` / `f22v_canvas59.jpg`.
Question: are any of these mistranscribed in-range digits, two tokens read as one, or genuine non-letter units?

**Method.** Twelve crops cut at native resolution from the canvases and upscaled 3-4x (`h2crops/crop_*.jpg`, boxes in
`h2crops/crop_boxes.tsv`; the ciphertext's r-numbering is one behind the manifest's physical band number, r_n =
band n+1, which cost one wrong-line round before it was noticed). Three reads per crop: the runner's own (not
blind: key.tsv and reading.txt already read) and two independent Sonnet vision passes that saw only the crops and
`meye/ref_4_9.png` (`h2crops/blind_A.tsv`, `blind_B.tsv`, prompts identical except crop order). Reconciliation per
position in `h2crops/reconcile.tsv`. A fourth image, `h2crops/sheet_4_vs_9.jpg`, puts every isolated 4 and 9 of
the leaf (r06 code 9, r09 4, r09 14, r20 29, v01 14, r24 14 29) beside the two disputed 48s at 3x for the 4/9 call.
Two subagent calls, no hosts.

**Results (3 reads per position; full table in reconcile.tsv).**

| position | ciphertext.tsv | verdict | reads |
|---|---|---|---|
| r16:21 | 72 | 72, one two-digit group | 3/3 H |
| r17:10 | 52 | 52, one group | 3/3 H |
| r17:20 | 48 | 48, one group; first digit is the looped-open 4 | 3/3 (A, B alt 9/98) |
| r20:15 | 48 | 48, one group | 2/3 (B reads 98) + sheet |
| r24:4 | 65 | 65 as one group, segmentation M | 2/3 (A reads 6 5, crease between) |
| r17:21 | 31 | 31 | 2/3 (A reads 37) |
| r07:5, r09:6 | [MARK:box] | a boxed numeral 101, same glyph twice | 3/3 |
| v01:6 | [MARK:frac] | a corrected two-digit group, 14 or 19 with a digit written over | 3/3 "corrected" |
| v01:1 | 14 | 14 followed by a dot (also 8. at r06:2) | 3/3 |
| v04:9 | 15 | 15 | 3/3 H |
| v04:16 | 21 | 21 followed by a colon-like mark | 2/2 |
| v04:19 | 15 (M, gap) | unreadable: canvas 59 ends at the gutter, only the 1 and an entry stroke survive | 3/3 |

**The 4/9 call.** B read r20:15 as 98 (H) and gave 98 as the alternate at r17:20; A gave 9 as the alternate at
both. `sheet_4_vs_9.jpg` settles it by the leaf's own hand: every 9 inside 19 and 29 is a closed loop with a
curved tail sweeping left; the first digit of both 48s is an open loop with a straight descending tail; and that
looped-open form is exactly the glyph at r06:3 that both transcription passes read as code 9 -- the one position
where key.tsv itself flags 9 as "homophone of 4 or a slip", because the plaintext there ("du-q-uesa") needs q = 4.
So the hand has two 4 forms (angular open 4, and looped 4 with a straight tail), and the 48s are 48. [Corrected in steps H10+H11 below, 28 Sept 2026: two blind reads call the r06:3 glyph a 9; this inference was not blind and is withdrawn; the 48s stand on their own three reads at M with 98 as the alternate.] The same
sheet says r06:3 is probably 4, not 9 (H11 below: a blind re-read of that one glyph would drop code 9 from the key
and K from 38 to 37; not changed here, one runner's eye is not two passes).

**What the marks are.** The [MARK:box] at r07:5 and r09:6 is not a decoration: all three reads see a numeral 101
inside a hand-drawn open-topped rectangle, identical at both places, in the two spots where the reading already
wants a name ("Cheureuse y del [101]", "que el [101] uenga con uos"). A boxed three-digit number above the letter
range is the shape of a nomenclature entry, and 48, 52, 65, 72 -- all above the 2-34 letter range, all written as
plain two-digit groups -- fit the same class (five of 522 tokens). The design is therefore better described as a
flat substitution 2-34 plus a small numeric nomenclature, which is what MERCY-KEY (27 Sept) used as the criterion
for ruling out DECODE 958 ("mixes alphabet + numeric + nomenclature"); that ruling-out is weakened, not reversed --
958's nomenclature is at about 50 codegroups, this one shows five -- and the DECODE comparison should be re-read
with that in mind before any further key search (noted for the orchestrator; no re-fetch done here). H5 (the
word-code family) gains weight from this. The [MARK:frac] at v01:6 is a corrected 14/19 (key.tsv's c = 14 from
"condiciones" is consistent with 14). The dots after 14 (v01:1) and 8 (r06:2) and the colon after 21 (v04:16)
are marks ciphertext.tsv does not carry; unknown function (punctuation, ink, or a marker); logged, not interpreted.

**No reading change and no grade change** (S 496, M 26, H 0, C 0 of 522). `ciphertext.tsv` is not edited by this
step: the one candidate segmentation change (r24:4 as "6 5", A's read, which under key.tsv would give s r at the
start of "tre[s r]egimient..") and the one candidate value change (r06:3 as 4) each need the two-pass rule, filed
as H10 and H11. v04:19 needs a different image (H12, ASKS row 81: add f.22v's gutter edge to the BnF batch).

Requests: none (disk only). Subagents: 2 Sonnet vision calls (12 crops each) of the 4 allowed. Cost: est 3 USD.

## Campaign step H9 (2026-09-28 00:12-00:2x UTC, campaign runner account 2, session_01V7xEY9JxjCxiXnQLtjFnfL)

**Status unchanged: partial.** CAMPAIGN.md H9: the error-tolerant solve (`tools/homophonic_anneal.py --noise 0.05`,
anneal_noisy, which names the positions it treats as misread) on the target, 3 seeds each under the es17 and es17c7
models, with a matched control run first (rule 3): the same solve on the three 5%-corrupted exact-profile Cartas
controls from step H1 (`cheap_test_1/noisy/exactprof_cartas13_n0.05_seed{1,2,3}.tsv`), whose truly corrupted
positions are known (`noisy_solve/control_truth_seed*.json`, 22-24 letter-changing corruptions each). Files:
`cheap_test_1/noisy_solve/` (9 JSON outputs, truth files, `analyse.py` which prints every number below). Settings
as always: order 3, 8 restarts x 40,000 iters, `--skip NONE`. No hosts, no subagents.

**Control (can the solver find corrupted positions at N=521, K=38?)** Named 7-9 positions per run against 22-24
real ones: precision 0.44 / 0.11 / 0.57, recall 0.17 / 0.05 / 0.17 (seeds 1-3), and the letter it put at a
correctly named position was right in 2 / 0 / 3 cases. Its corrected decode read 92.9% / 34.4% / 81.0% -- no better
than the plain solver on the same corrupted inputs (H1: -1279.5 / -1157.2 / -1173.7 plain vs -1230.9 / -1361.5 /
-1165.3 noisy; seed 2 stuck). **Verdict: at this N and noise level the instrument does not locate misread
positions** (recall under one in five; one run in three sticks). Any position list from it on the target is
weakly evidenced by construction, and this is logged as "untestable by this tool at this N", not as a negative
on the target (CLAUDE.md rule 3, the "same instrument, second attempt" paragraph: the next attempt at locating
misreads needs a different instrument -- the eye, H10/H11 -- not a tuned noise level).

**Target.** Scores: es17 -1156.3 / -1155.5 / -1303.9 (plain solver on file: -1154.3 -- the free positions buy
nothing); es17c7 -1137.7 / -1133.3 / -1133.5 (plain -1138.5: about 5 points for 3-5 free positions). The solver
used only 3-7 of the 40 free positions it was allowed, on every seed -- consistent with a transcription that is
mostly clean under this design, the same reading H1's error bracket gave. 21 distinct positions were named across
the six runs; only two by three or more runs: r18:5 (code 26, reading i, S; solver wants d on 3 of 4) and r16:9
(code 25, reading u, M -- the M-graded code whose r16 occurrence "copura" does not read; solver wants a/o). All 19
others were named once or twice, and 20 of the 21 are S-graded. Given the control's precision, at most one or two
of the 21 are expected to be real misreads; r18:5 and r16:9 are handed to the H10/H11 eye-check job as two extra
crops (cheap, same subagent call), nothing more. No reading change, no grade change.

## Campaign steps H10 + H11 (2026-09-28 00:16-00:3x UTC, campaign runner account 2, session_01V7xEY9JxjCxiXnQLtjFnfL)

**Status unchanged: partial.** One job for two transcription questions left open by H2, plus the two positions H9
nominated. Two fresh blind Sonnet reads (C, D; crops only, plus an unlabeled strip of the leaf's own 4s and 9s,
`h2crops/h10h11_ref_strip.jpg`), the runner's own eye, and one objective measure. Files: `h2crops/h10h11_*.jpg`,
boxes in `h2crops/crop_boxes.tsv`, reads and verdicts in `h2crops/h10h11_reads.tsv`. Two subagent calls, no hosts.

**H10, r24:4 -- 65 or "6 5".** One group. Blind C and D both call 65 (M each); H2's B called 65 (H); only H2's A
called "6 5". Objective: blank-column runs across the 4x crop are 36-95 px inside two-digit groups, 179-263 px
between groups, and 13 px between the 6 and the 5. The faint vertical line between them continues through the
row above at the same x (`h10h11_crop_A_tall.jpg`, C and D both): a paper fold, not a space. `ciphertext.tsv`
unchanged; code 65 stays (value M in key.tsv); token count stays 522. C's report is internally inconsistent (its
body says 65, its summary line says "6 5"); logged, and the body's reasoning with gap sizes is what counts.

**H11, r06:3 -- code 9 or a looped 4.** 9 stands. Both blind reads call it 9 (C: H, closed loop with a curved tail
and no open angle; D: M, closed small loop, near-straight drop with a leftward flick); Y6's two transcription
passes also read 9; only the runner's own non-blind eye (H2, `sheet_4_vs_9.jpg`) read it as a looped 4. **Correction
to step H2:** the sentence there that "the looped-open form is exactly the glyph at r06:3 ... so the hand has two 4
forms, and the 48s are 48" was an unblinded inference and is withdrawn; the two 48s stand on their own three reads
(H2: A 48 M, B 48 with 98 as alternate at r17:20 and 98 at r20:15, runner 48) at grade M, with 98 as the recorded
alternate at both places. Code 9 keeps its single occurrence and its M grade ("homophone of 4 or a slip" -- now
"homophone of 4", since the glyph is a 9); K stays 38.

**H9's two nominations (r16:9 code 25, r18:5 code 26):** both correctly transcribed, 25 and 26 one group each, H on
both blind reads. Neither is a transcription error; whatever is wrong at r16:9 is the code's value (25, M), not the
digits. This closes H9's list: 0 of 2 nominations were misreads, consistent with the control's verdict there.

**New mark:** both blind reads see a dot after the 5 at r16:10 ("5."), in addition to the dots after 8 (r06:2) and
14 (v01:1) and the colon after 21 (v04:16) found in H2. Under the current reading none of the four sits at a word
end (du.quesa, c.ondiciones, opur.adlon...), so they are not obvious word separators; an inventory of every dot and
colon on both pages, with the reading letter before and after each, is a cheap step (H13).

No reading change, no grade change (S 496, M 26, H 0, C 0 of 522). ciphertext.tsv, key.tsv untouched.

## Campaign step H3 (2026-09-28 00:22-00:3x UTC, campaign runner account 2, session_01V7xEY9JxjCxiXnQLtjFnfL)

**Status unchanged: partial.** CAMPAIGN.md H3: the anneal-with-held-codes consistency check (M2's -1199.1) re-run on
the current token stream. `cipher_codes_522.tsv` (new): ciphertext.tsv minus the [PLAIN] tokens with the current
`exceptions.tsv` (r06:14, r17:5 -> 14) applied, N=522, K=38 -- the file the campaign's anneals should use from now on;
`cipher_codes.tsv` (521, Y8's) stays for reproducing Y8/H1/H9. Held: the 29 S-graded key.tsv codes (`--fix`, list
in `cheap_test_1/h3/analyse.py`'s output). Control: the same 29 codes held at a permutation of their own letters (at
most 2 in place), 3 seeds. Settings as always (order 3, 8 x 40,000, `--skip NONE`). Files: `cheap_test_1/h3/`. No hosts,
no subagents. `tools/decode_key.py --check` still exits 0 (the committed reading re-derives; it comes from key.tsv,
not from any anneal).

| run | scores (seeds 1-3) | free-code values |
|---|---|---|
| held-29, 522 tokens, es17 | -1205.2 x3 (every restart identical) | 9=q 15=s 25=a 48=t 52=s 65=s 72=z box=o frac=i |
| held-29, 522 tokens, es17c7 | -1161.4 x3 | 9=q 15=n 25=i 48=d 52=l 65=s 72=u box=a frac=c |
| held-29, M2's 521-token eyefix file, es17 (reproduction) | -1206.3 | 9=q 15=s 25=u 48=d 52=s 65=s 72=z box=a frac=i |
| **control: permuted-held-29, 522, es17** | **-2172.8, -2319.1, -2154.5** | (arbitrary) |
| free anneal, 522, es17 (Y8: -1154.3 on 521) | -1344.8 (stuck), -1160.0, -1160.0 | 9=q 15=n 25=u 48=d 52=y 65=d 72=t box=a frac=c |
| key.tsv M values | -- | 9=q 15=n 25=u 48=d 52=y 65=s 72=z box=_ frac=c |

**Findings.** (1) M2's figure does not reproduce exactly: the committed `m2/cipher_codes_eyefix.tsv` with the 29
codes held gives -1206.3, not -1199.1 (7 points), and on the 522 stream -1205.2; M2's file or settings must have
differed from what is committed (the eyefix file carried 5 exceptions then, MREV reverted 3 -- the file on disk may
be the post-MREV one) -- logged as a rule-7 note, no effect on the reading, which decode_key.py regenerates from
key.tsv. (2) The held key is far from arbitrary: permuting the 29 held letters costs 950-1,110 points against the
model, on every seed, with every restart converging -- a control that can differ and does. (3) Holding key.tsv's 29
S values costs about 45 points against the free optimum (-1205.2 vs -1160.0), the same shape M2's crib-loop gate
recorded (-1154.3 -> -1199.1): the hand corrections read words the trigram objective does not prefer. (4) The
M-graded values are corpus-dependent: between es17 and es17c7 only 9=q and 65=s agree; 15, 25, 48, 52, 72 and both
marks take different letters under each corpus, and 48=d, frac=c agree with key.tsv only under es17c7. Under the
nomenclature reading of H2 (48, 52, 65, 72, boxed 101 as word codes) their letter values are not meaningful anyway;
key.tsv's M grades for them are right and should not be promoted by any further anneal. (5) The free anneal of
the 522 stream (-1160.0, two of three seeds) lands on key.tsv's M values for 9, 15, 25, 48, 52 and both marks.

**Not reading-ready:** the shuffled-key (permuted) control passes by a wide margin, but the judge gate (MJ,
MERCY-JUDGE2: "judge cannot decide") is unchanged and no reading changed, so no reading-ready line is posted.
Grades unchanged (S 496, M 26, H 0, C 0 of 522).

## Campaign step H13 (2026-09-28 00:25-00:4x UTC, campaign runner account 2, session_01V7xEY9JxjCxiXnQLtjFnfL)

**Status unchanged: partial.** Inventory of the dots and colons attached to numeral groups (H2 found four; are they
separators?). Method and files in `h13marks/README.md`; the marks in `h13marks/marks.tsv`, the sheets in
`h13marks/verified_marks_{1,2}.jpg`. Runner's own eye over 50 detector candidates, no subagent, no hosts.

**Inventory: 16 marks after cipher groups** (a floor; the detector missed one the blind reads had found): dots after
r04:1 (34), r04:2 (28), r04:12 (34), r04:14 (34), r05:1 (3), r06:6 (8), r06:12 (16), r10:18 (6), r11:4 (2), r11:5 (6),
r14:3 (19), r16:10 (5), v01:1 (14), v05:9 (14), r23:8 (10), and the colon after v04:16 (21). Four of the sixteen sit on
r04, the first cipher line. Plus three full stops in the clear text immediately before a cipher run (r08, r13, v11).

**Test (rule 3): are they word separators?** Under the current reading 1 of 16 falls at a word end (r11:5, the s of
"sepamos" before the clear "Con"). Control: the same 16 marks placed at random cipher positions of the same lines,
10,000 draws: mean 1.22 word-end hits, 95th percentile 3, P(>= 1) = 0.75. [Corrected in step H14, 28 Sept 2026: these boundaries were run ends, not word ends; with M2's segmentation 2 of 16 at word ends vs random mean 3.09, P(>= 2) = 0.86 -- same conclusion.] **The marks are not word separators under
this reading, and not distinguishable from chance placement.** By the code they follow: 34 three times (all r04), 14
twice, 6 twice, the rest once -- no code-specific pattern either. What they are stays open (pen rests, or a
segmentation different from ours); they change no token.

**Side observation, no grade change:** all three clear-text full stops are followed by cipher 13, which key.tsv reads
y ("y ..." opening the sentence, 13 = y is the M2 correction from Y8's s), the commonest sentence opener in a letter
of this register -- an independent consistency point for 13 = y, logged for the verifier, not a new grade.

## Campaign step H5 (2026-09-28 00:28-00:3x UTC, campaign runner account 2, session_01V7xEY9JxjCxiXnQLtjFnfL)

**Status unchanged: partial.** `tools/family_run.py --family wordcode` (the letter-or-word nomenclator family built for
Salviati) with the six nomenclature-range types (48, 52, 65, 72, [MARK:box], [MARK:frac]; 8 of 522 tokens) as the
code-capable types (given a `^c` mark suffix so `codes=marked` selects exactly them), the cipher as its five real
runs merged across line ends (`families/h5/runs.txt`: 28, 27, 48, 386, 33 tokens -- the line-by-line runs the tool
would otherwise use break words at every line end), and the clear words on each side of every run as context
(`families/h5/context.tsv`). Control first (3 seeds), target once, es17 corpus, 4 restarts, err 0.047 (the
transcription's own two-pass disagreement). Row in `HYPOTHESES.md`; decode in `families/wordcode-1-*.txt`. No hosts,
no subagents. 82 s.

**Control: blended 0.852 (0.808-0.904), gate 0.6 met -- but per class:** letters 0.86 / 0.82 / 0.92; codes 0.000 (n=11),
0.000 (n=7), 0.607 (n=28); hapax codes 0.000 on every seed, repeated codes 0.68 on the one seed that had 25 of them.
The target's code-capable tokens are 8, five of the six types occurring once or twice. **So the family has no power on
exactly the class the hypothesis asks about (CLAUDE.md rule 3, the unbalanced-class paragraph): the gate passed on
the letters alone.** This is a control-backed non-test for the word-code question at this N and this code count,
not a negative.

**Target (for the record only):** best score -1231.2 (restarts -1231.2, -1356.7, -1365.3, -1433.5), judge FAIL
(-1.091 vs real_p05 -0.894), two code tokens decoded, both to "de"; the letter decode is well below the plain
homophonic anneal's (-1154.3 / -1160.0), i.e. the extra word-code freedom buys nothing and the family's own
letter solver is weaker than homophonic_anneal on this stream. Whether 48, 52, 65, 72 and the boxed 101 are word
codes stays open on the design evidence of H2 (their range and the box) alone; the instrument that could settle it
is a period key or a sibling letter reusing the same codes (H7, H8), not a further anneal. No reading change, no
grade change.

## Campaign step H4 (2026-09-28 00:36-00:4x UTC, campaign runner account 2, session_01V7xEY9JxjCxiXnQLtjFnfL)

**Status unchanged: partial.** The within-tome homogeneity split `tools/data/es17c7/README.md` named as the next
step: `tools/data/es17c7/holdout_split_check.py` (new) cuts each of the seven Cartas tomes into C contiguous
chunks (chronological newsletters, so a chunk is a date range), builds the judge model from everything except the
held-out chunk (the same tome's other chunks stay in), and scores 200 held-out windows of N=519 against that
model's own real_p05, exactly as `holdout_check.py` does by whole tome. Full output in
`tools/data/es17c7/holdout_split_2026-09-28.log`. No hosts, no subagents.

| split | folds | blended false-negative rate | per-fold spread | folds over 10% |
|---|---|---|---|---|
| by tome (MERCY-JUDGE2, on file) | 7 | 11.1% | 2.0-23.0% (11.5x) | 4/7 |
| 2 chunks per tome | 14 | 10.5% | 3.5-19.0% (5.4x) | 6/14 |
| 4 chunks per tome | 28 | 11.1% | 1.0-34.0% (34x) | 11/28 |

**Pre-registered gate (blended under 10%, spread under 2x) not met on either split**, and the picture is now
clear: the variance is inside tomes, not between them. Tomo XVII's four chunks read 34.0 / 17.0 / 23.5 / 14.5%,
tomo XIX's 1.0 / 8.5 / 5.5 / 30.0%, tomo XVIII's 14.5 / 17.5 / 3.5 / 7.0% -- a corpus whose held-out real prose
fails its own judge at up to a third in some stretches and one in a hundred in others (OCR quality, inserted
documents, verse and Latin, none of it separable by date). The judge stays "cannot decide" for this target at
N 519-1342, and this closes the corpus-tuning line: es17 -> es17c -> es17c7 -> a within-tome split is the same
instrument tuned four times without the numbers moving together toward the gate (CLAUDE.md rule 3, the
"second attempt at an unchanged approach" paragraph). Logged "untestable by this judge at this N"; the next
attempt at "is the reading Spanish" needs a different instrument (H14 below), not a fifth corpus. No reading
change, no grade change.

## Campaign step H14 (2026-09-28 00:40-00:5x UTC, campaign runner account 2, session_01V7xEY9JxjCxiXnQLtjFnfL)

**Status unchanged: partial.** A second instrument for "does the reading behave like Spanish", independent of the
n-gram judge that H4 closed: lexicon coverage, the share of the reading's cipher words found in the Cartas
vocabulary (`tools/data/es17c7`, 17,400 word types with 3 or more occurrences in 1.16M tokens). Script
`cheap_test_1/h14/lexcov.py` (controls) plus the re-run in this section's log for the reading; the segmented reading
used is M2's own word segmentation from its NOTES paragraph with MREV's four word changes applied
(`cheap_test_1/h14/reading_segmented_m2.txt`; `reading.txt` itself writes each cipher run unsegmented, which is why
the first pass of this step, and step H13's word-end test, had to be redone -- see the H13 correction below). No hosts,
no subagents.

| text | words | in vocabulary | letter-weighted | words of 4+ letters in vocabulary |
|---|---|---|---|---|
| **the reading (M2 segmentation, 121 words, 520 letters)** | 121 | **81.0%** | 63.8% | **51.7%** (56 words) |
| 20 shuffles of the same letters at the same word lengths | 121 | 34.3% (31.4-37.2) | -- | 0.8% (max 1.8) |
| the letter's own clear words (m2/clear_words_only.txt) | 171 | 87.7% | 79.4% | -- |
| H1 exact-profile controls, Cartas windows, clean (91-98% letters) | 113-135 | 79.7-90.3% | 63.7-84.8% | -- |
| H1 exact-profile controls, Don Quijote windows, clean (93-99%) | 121-136 | 75.8-93.4% | 59.3-88.5% | -- |
| the controls' true plaintexts | 121-124 | 94.2-94.4% | 90.4-90.6% | -- |
| corrupted controls, 5% signs (30-93% letters) | 113-136 | 54.5-81.6% | 32.2-68.3% | -- |
| corrupted controls, 10% signs (50-88% letters) | 113-136 | 49.2-77.2% | 25.7-62.4% | -- |

**Verdict: the pre-registered pass is met** -- the reading sits inside the clean-control band (81.0% vs 79.7-93.4%,
at its low edge) and above every shuffle by 44 points, and on the discriminating measure (words of four or more
letters) the separation is 51.7% against a shuffle maximum of 1.8%. Letter-weighted it sits with the 5%-corrupted
controls (63.8% vs 60-68%), the same place H1's error bracket put the anneal score: a decode that is mostly right
and carries a few wrong codes. The 23 words not in the vocabulary are the proper names and the unread stretch
(brandenburg, eleues, oulay, lonburg, szrfsucmarey, noladirentnonysiiuna, ...) plus verb forms the newsletters do
not use (pasareis, propondreis, permitira, embian). **This supports the reading as a cryptanalytic result; it is
not a judge PASS and does not change any grade** (rule 10 wording; the verifier lane already holds this reading at
N3 after two audits, and nothing here changes a token). Read together, H1 (score inside the real-text band), H3
(permuted-key control 950-1,110 points worse) and H14 (lexicon coverage inside the real-text band, far above
shuffle) are three controls of different kinds that the reading passes; the n-gram judge is the one instrument
that cannot decide, and H4 showed why.

**Correction to step H13 (word-end test).** H13's `word_ends()` took its word boundaries from `reading.txt`, which
writes each cipher run as one unsegmented upper-case string, so it counted run ends, not word ends (11 "word ends"
in 194 tokens). Redone with M2's segmentation: 2 of the 16 marks fall at word ends (r14:3 after "ARE" of
"pasareis a"? -- the end of "PASAREIS"; r16:10 the end of "EOPURA"), random placement over the same lines gives a
mean of 3.09, 95th percentile 6, P(>= 2) = 0.86. The conclusion stands (the marks are not word separators under
this reading); the numbers in the H13 section and CAMPAIGN.md's H13 row are superseded by these.

## Campaign step H15 (2026-09-28 00:43-00:5x UTC, campaign runner account 2, session_01V7xEY9JxjCxiXnQLtjFnfL)

**Status unchanged: partial.** Completeness check of the transcription by ink count (`h15count/README.md`,
`counts.tsv`): numeral groups per full-cipher line from connected components, merged at 20 / 30 / 40 px, against
`ciphertext.tsv`'s token count per line. Runner's own eye on the lines that stayed off; no subagent, no hosts.

**Result.** Of 24 full-cipher lines, 13 match the token count exactly at one of the three thresholds, 8 are off by
one at best, 3 are off by two or three at every threshold (r06 19 vs 22, r20 19 vs 21, r23 18 vs 20). All three
were counted by eye on native-resolution crops: r06 22 groups, r20 21 (already counted in H2), r23 20 -- each
exactly the transcription's count; the detector's deficit is touching digits written as one blob (r23 begins
"18 6" written as "186"; r06 has "17 16" and "6 34" nearly joined). **No missing or extra token found on any
full-cipher line at this instrument's resolution**; the eight off-by-one lines were not each re-read (five of
them -- r14, r16, r17, v04, v07 -- already carry R7-MEYE's blind count, which agreed with the transcription, and
r16/r17/v04 three further reads from H2/H10/H11). The mixed lines (r05, r07, r08, r11, r13, v09, v11, v13; 39
cipher tokens between them) are outside this check.

**Side finding for H13's inventory:** r06 carries two more dots the detector had merged into digits -- "18." at
r06:16 and "8." at r06:17 (the r06 dot H13 could not place) -- so the mark inventory's floor is 18, not 16; the
H13 conclusion (not word separators: 2 of 16, random mean 3.09) is unaffected in kind, and both new dots sit
inside "Cheureuse" (e u r e u s e), not at a word end. No token changed, no grade changed.

## Campaign step H16 (2026-09-28 00:46-01:0x UTC, campaign runner account 2, session_01V7xEY9JxjCxiXnQLtjFnfL)

**Status unchanged: partial.** DECODE catalogue search for a Spanish key of 1640-1660 with the design H2 found. Two
parts. No login, no credentials read; 60 requests to de-crypt.org (RecordsList only, 1.6 s apart, descriptive UA),
no thumbnails fetched; no subagents.

**(a) Record 958 re-read against H2 (saved page, no network).** 958's own description: "a homophonic substitution
cipher with homophones only for the vowels and a small nomenclature, 50 codegroups in sum total. Two-digit numbers
are reserved for the cipher, capital letters for the nomenclature." Our `key.tsv`, tabulated by letter, is exactly
the first half of that: **three homophones for each of a, e, i, o, u (15 codes) and one code for each consonant
(15 codes), all two-digit numbers 2-34**, plus the small nomenclature H2 identified (48, 52, 65, 72, the boxed
101 -- numerals, not capital letters; the second "codes" key.tsv lists for q, s, y, c, n, d are these rare codes
and the marks). MERCY-KEY (27 Sept) ruled 958 out for having a nomenclature at all; that reason is withdrawn (this
cipher has one), but the symbol-set difference stands: 958's name class is capital letters, ours is boxed and
high numerals, so 958 is a **design sibling of the same office's key family, not this letter's key**. The Brussels
SEE "chiffres 1647-98" register (inv.nr. 2, DECODE 958-965, images account-gated, ASKS row 1) is therefore the
one document whose reading could settle the key: if any of its eight keys has vowel-only homophones in 2-34 with a
numeric name class, it is a candidate; the thumbnails were unreadable at served size (MERCY-KEY U2). Filed as
H17 (`needs: doc`, ASKS row 82: add inv.nr. 2 to the AGR reproduction request that S3 already carries for
t. LXIV f.16).

**(b) Listing crawl (`tools/decode_list.py --record-type key`, all four statuses).** Keys sit under status N/A:
6,351 records, of which 2,850 (pages 1-58 of 128) were fetched before the 60-request cap; plus 19 Decrypted and 4
Non-decrypted key records (complete). `sources/decode/keys-all-2026-09-28.tsv` (2,873 rows, a snapshot). In the
fetched 45%: 39 Spanish-language keys; 7 with a date range touching 1640-1660, all Archivio di Stato di Firenze
"SIIVol6" keys dated 1501-1700 (a volume-level range, not a date), none from Brussels or Madrid in that slice;
2 Spanish keys undated. **A partial search result (45% of the key listing), not a negative** (rule 10 wording:
"not found in the fetched slice, searched by status/language/date on 28 Sept 2026"); pages 59-128 remain (H18).
No reading change, no grade change.

## Campaign step H19 (2026-09-28 00:51-00:5x UTC, campaign runner account 2, session_01V7xEY9JxjCxiXnQLtjFnfL)

**Status unchanged: partial.** Bookkeeping the close-out requires (CLAUDE.md Usage 8a): `KEY-OFFICES.tsv` gains this
key's row (office: Spanish Netherlands government, the governor-general's secretariat, inferred; correspondents;
1648; the design as H2/H16 describe it; BnF Espagnol 144 f.22r-22v; key `ours`, N3), `tools/key_design.py` rebuilt
`KEY-DESIGN.tsv` (the mercy row now carries the office instead of "(folder)"; `--check` exits 0), and
`tools/design_prior.py --no-write` on `cipher_codes_522.tsv` reads: multi-sign d=0.14 (envelope 0.56) plausible,
fine ranking homophonic 0.22 < nomenclator 0.25 < syllabary 0.34 < alphabet substitution 0.40; nearest key is this
target's own (d=0.01), next Thurloe's Johnson nomenclator (synthetic, d=0.16). The prior agrees with the design on
file. Disk only. No reading change, no grade change.

## Campaign step H20 (2026-09-28 00:52-00:5x UTC, campaign runner account 2, session_01V7xEY9JxjCxiXnQLtjFnfL)

**Status unchanged: partial.** The seven Archivio di Stato di Firenze "SIIVol6" Spanish-language keys H16's listing
slice returned for 1640-1660 (DECODE 7259, 7308, 7358, 7362, 7368, 7390, 7391): their RecordsView pages fetched
login-free (7 requests, 1.6 s apart; saved in `sources/decode/h20-2026-09-28/`, parsed in `summary.tsv`). Every one
declares graphic signs and/or alphabet letters among its symbol sets (7259: graphic signs + numerical; the rest
alphabet with or without graphic signs), and five of seven are simple rather than homophonic substitution; none is
the all-numeric, two-digit, vowel-homophone design of `key.tsv` (H16 a). No thumbnail was needed. A stated-design
negative on seven records, not a key comparison. No reading change, no grade change.

## Campaign step H18 (2026-09-28 01:39-01:5x UTC, campaign runner account 2, session_01V7xEY9JxjCxiXnQLtjFnfL)

**Status unchanged: partial.** The DECODE key listing finished: `tools/decode_list.py --start-page` (new option, offline
test passes) resumed the status-N/A crawl from page 59; 71 requests, 1.6 s apart, no login. Merged snapshot
`sources/decode/keys-all-2026-09-28-merged.tsv`: 6,324 of the 6,374 key records DECODE lists (99%). **62 Spanish-
language keys; 21 with a date range touching 1640-1660:** the eight Brussels SEE "chiffres 1647-98" keys (958-965,
MERCY-KEY and H16), three Brussels SEA inv.nr. 1 keys (941, 944, 946; series dated 1553-1729), Vienna HHStA
Staatskanzlei 1485 (1600-1799), two TNA SP 106 Charles II keys (1660-1685, out of scope), and the seven Florentine
SIIVol6 keys (H20); plus two undated Barcelona keys (10182, 10183). The six not yet examined were read on their
login-free RecordsView pages (`sources/decode/h18-2026-09-28/`, `summary.tsv`): 941 and 946 are homophonic
substitution with nomenclatures over alphabet + graphic signs + numerals, 944 a numeric word nomenclator, 1485 a
simple substitution with alphabet symbols, the Barcelona pair "unknown" over mixed symbol sets. **None states the
all-numeric two-digit homophonic alphabet of `key.tsv`; the only records whose stated design contains it are
958-965** (H16). What remains open is inside the images: 941 and 946 carry a numerical set among others, and
958-965's own numeric alphabets have never been read at full size (account-gated, ASKS row 1). A search result
over 99% of the listing, searched by language and date on 28 Sept 2026 -- not a novelty or key verdict (rule 10).
No reading change, no grade change. DECODE requests this session: 67 + 77 = 144, all 1.6 s apart.

## Campaign step H21 (2026-09-28 02:40-02:5x UTC, campaign runner account 2, session_01V7xEY9JxjCxiXnQLtjFnfL)

**Status unchanged: partial.** Design-matched control for H1: real Cartas windows (N=521, out of the es17 model's
sample) enciphered the way `key.tsv` is built -- three homophones per vowel (occurrences drawn uniformly), one code
per consonant, eight rare extra codes used once or twice (K 39-40) -- annealed with Y8's settings
(`cheap_test_1/h21/vowel_control.py`, TSVs with `.plain` sidecars, JSON outputs). A stricter version that also
imposed the target's exact 38-count profile under the vowel/consonant assignment found **no window in 20,000
tries**: the profile is not realisable on real text with that assignment, because the target's five largest counts
(57, 42, 41, 39, 38 = codes 18, 32, 5, 10, 6) are one vowel homophone and consonants -- the scribe used the vowel
homophones very unevenly (e: 57 / 27 / 11; a: 39 / 17 / 9), not one in three. Disk only, no subagents.

| model | design-matched control, 5 / 3 seeds | letters read | target |
|---|---|---|---|
| es17 | -1121.2, -1135.7, -1292.5 (stuck, 47%), -1087.9, -1118.5; mean -1151.1 | 94-98% | -1154.3 |
| es17c7 | -1100.7, -1090.0, -1177.1; mean -1122.6 | 98% | -1138.5 |

**Verdict: the same as H1 with the design matched rather than the profile** -- the target sits inside the band of
real Spanish under its own design, at the lower part, exactly where a mostly-right decode with a few misread or
nomenclature tokens would sit. Nothing here moves any grade; it closes the control question H1 opened. With H1,
H3, H14 and H21 the reading has four controls of different kinds behind it and one instrument (the n-gram
judge) that cannot decide at this length. The uneven homophone use is a scribal-habit observation worth carrying to
KEY-DESIGN's notes and to any comparison with the Brussels SEE register when it arrives (ASKS 82).

## Campaign step H22 (2026-09-28 03:39-03:5x UTC, campaign runner account 2, session_01V7xEY9JxjCxiXnQLtjFnfL)

**Status unchanged: partial.** The 39 cipher tokens on the eight mixed lines (r05, r07, r08, r11, r13, v09, v11,
v13) that H15's ink count could not cover: one blind Sonnet read from native half-line crops (no transcription,
no key), reconciled in `h22mixed/blind_read.tsv`. **39 of 39 agree with `ciphertext.tsv`.** Two instructive
non-disagreements: the reader twice appended a "9" after a cipher run (r05, v09) -- it is the clear word "y" that
opens the next clause, whose cursive shape is a 9 with a tail -- and took r11's final 6 for a capital "G." (the
hand's 6 is G-shaped; the dots after 2 and 6 there are H13's marks). The boxed 101 at r07:5 read as "boxed 9 (alt
8)" at native resolution against 101 on three 4x reads in H2 -- resolution, not a new reading. With H15 this
completes the per-token count check of the whole transcription: no missing or extra token found anywhere at the
instruments' resolution. One subagent call; no hosts. No reading or grade change.

## Campaign step H23 (2026-09-28 03:5x UTC): not run

Served-size thumbnails of DECODE 941 and 946: MERCY-KEY U2 (27 Sept) already established that DECODE's thumbnails
are 200 x 284 px and that "no individual digit, letter or graphic-sign shape can be made out" at that size for the
same series; a look at two more would return "unreadable at served size" by construction (CLAUDE.md rule 3, a
control that cannot fail differently). Dropped without spending requests; the full-size images stay behind ASKS
row 1 / 82 (H17).

## Campaign step H24 (2026-09-28 03:45-03:5x UTC, campaign runner account 2, session_01V7xEY9JxjCxiXnQLtjFnfL)

**Status unchanged: partial.** Could a clear "y" have been swallowed into the cipher stream as a 9 (or the reverse)?
Every cipher token at a run boundary (adjacent to a clear word) with sign 9, 19 or 29 was listed from
`ciphertext.tsv`: exactly one, v13:7 (19, the last letter of "gente" before the clear "En todo"), which H22's blind
reader had just read as "7 19" at H confidence with "En todo" following as words. The three clear "y" tokens that
directly follow a cipher run (after r05:5, r07:5, v09:6) are already in the plain stream. **Nothing to move**; the
y/9 confusion is a blind-reader effect at run edges, not a transcription fault. No reading or grade change.

## Campaign step H25 (2026-09-28 03:46-03:5x UTC, campaign runner account 2, session_01V7xEY9JxjCxiXnQLtjFnfL)

**Status unchanged: partial.** Does the scribe's choice among a vowel's homophones follow the neighbouring letter?
From `reading_tokens.tsv` (the S-graded vowel codes: a 10/17/34, e 18/19/33, i 21/26/31, o 2/23/29, u 8/27), a
G-statistic of homophone choice against the preceding and the following letter, pooled over the five vowels, against
1,000 shuffles of the homophone labels within each vowel (letters and positions kept) --
`cheap_test_1/h25/homophone_choice.log`. Preceding letter: G 145.8 vs shuffle mean 128.9, 95th percentile 147.7,
P = 0.072; following letter: G 117.6 vs 123.5, P = 0.70. **No rule detectable at this N**: the choice is a habit
with strong preferences (a: 39/18/9, e: 57/25/3, o: 20/8/5, u: 24/4) rather than a positional convention -- the
uneven use H21 noted, without a context rule behind it. A negative with a control that can differ. Disk only.

## Campaign step H26 (2026-09-28 03:47-03:5x UTC, campaign runner account 2, session_01V7xEY9JxjCxiXnQLtjFnfL)

**Status unchanged: partial.** M2's crib-loop gain gate re-run under es17c7 (the "While waiting" item). Control: the
three H21 design-matched Cartas controls, blind es17c7 decode, every in-vocabulary stretch of 4+ letters in the decode
held fixed (72-79 words, 35-38 of 39 signs, 32-33 of them right), re-annealed (`cheap_test_1/h26/`, `gain.log`).
Control gain: **+0.0, +0.0, +0.0** anneal points, letters 98.5 / 97.7 / 98.1% before and after. Target under es17c7:
free -1138.5 (H1) to held-29 -1161.4 (H3), gain -22.9 (under es17, M2: -44.8). **A non-test under both corpora, and
now visibly so:** the control reads 98% blind, so holding words it already has can gain nothing -- the control has
no headroom (CLAUDE.md rule 3, the "control already near ceiling" paragraph), which M2's own control (a 51.6% blind
read that also gained 0.0) had hidden. The target's negative "gain" is the cost of holding hand-read words the
trigram objective does not prefer, smaller under the register-matched corpus. The gate needs a control that can
gain (H27). No reading or grade change. Disk only.

## Campaign step H27 (2026-09-28 04:39-04:5x UTC, campaign runner account 2, session_01V7xEY9JxjCxiXnQLtjFnfL)

**Status unchanged: partial.** The crib-loop gain gate with controls that have headroom: the three H21 design-matched
Cartas controls corrupted at 5% and 10% of signs (`cheap_test_1/h27/`), blind es17c7 anneal (5%: 92-94% letters
right; 10%: 30-80%), every in-vocabulary stretch of the blind decode held (31-36 of 39 signs), re-anneal. Gain:
**+0.0 on all six** (one +1.0), letters unchanged in every case (`gain.log`), as on the three clean controls (H26)
and on M2's own control. **The numeric gate is a non-test by construction, not by ceiling:** holding words that
the annealer itself produced fixes the annealer at its own optimum, so it can never gain; only corrections made
against the anneal (M2's hand corrections, 13=y, 25=u, 33=e, ...) can move it, and those cost anneal points by
definition (-44.8 under es17, -22.9 under es17c7). M2's "control gains 0.0, target gains negative" therefore
compared a circular zero with the price of reading, and licenses nothing either way. The instrument for hand
corrections is letter accuracy on a control with known truth read by a reader, not an anneal score; the gate line
is retired here. No reading or grade change. Disk only.

## Campaign step H28 (2026-09-28 04:41 UTC, campaign runner account 2, session_01V7xEY9JxjCxiXnQLtjFnfL)

**Status unchanged: partial.** The 18 marks (H13's 16 plus H15's two on r06) against the codes they follow, versus
1,000 draws of 18 marks at code-frequency weights (`h13marks/marks_vs_code_frequency.log`). Overall no code is
dotted more than chance predicts (largest count for one code: observed 3, random mean 3.21, P = 0.81). One code is
notable on its own: **34 (= a) carries a dot on 3 of its 9 occurrences** (expected 0.31, P = 0.003 uncorrected, about
0.04 after correcting for the 13 codes tested), and all three are on r04, the first cipher line (positions 1, 12,
14: the a of "alandose", "estas", "armas"), so a first-line habit cannot be separated from a code-specific one on
this leaf. Codes 14 (2 of 14, P 0.09) and 8 (2 of 24, P 0.18) do not reach it. Logged for the comparison with the
Brussels register (a dotted homophone would be a key feature); no token or grade changed.

## Campaign step H29 (2026-09-28 05:39 UTC, campaign runner account 2, session_01V7xEY9JxjCxiXnQLtjFnfL)

**Status unchanged: partial.** Candidates for the boxed 101 name code, two occurrences: r07 "de la duquesa de
Cheureuse y del [101]" and r09 "que el [101] uenga con uos". From what is on file only (AUDIT.md: Lonchay 1896
p.445, which places Mercy's 1648 talks with the duchesse de Chevreuse and Saint-Ibal at Kerpen and Spa; the
Cuvelier-Lefèvre VI no. 1499 calendar of the parallel dispatch; the letter's own clear text). Constraints: the first
context wants a masculine person or title after "del" paired with Chevreuse; the second a person who could travel
with Mercy. Persons named in the sources around the mission: the Elector of Brandenburg (spelled out in cipher, so
not a code), Leopold Wilhelm (the inferred sender, cannot "come with you"), the duchesse de Chevreuse (feminine,
spelled out), **Saint-Ibal** (Chevreuse's agent, in the same talks per Lonchay -- fits both contexts), the **duke of
Lorraine** (a title after "del", could join Mercy -- fits both), Piccolomini (fits the second only). **Two names fit
both contexts, so by this row's own rule no candidate is graded**; the boxed 101 stays `_` (M). If the Brussels
register (H17, ASKS 82) lists a boxed 101, it decides. No hosts; no token or grade changed.

## Campaign step H30 (2026-09-28 14:20-14:28 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** The reader-on-control instrument H27 asked for. Four blind Sonnet readers, one packet
each (`cheap_test_1/h30/packet_{A,B,C,D}.txt`, built by `h30/build.py`): the es17c7 blind decode, a key table and the
glyph of every letter, glyphs relabelled `g10..` so no reader could tell target from control; asked for key changes
(a glyph re-lettered everywhere) with confidence and evidence words, no single-position rewrites. A, D = 5%-corrupted
design-matched controls (H27 seeds 1, 3), B = 10% seed 2 (the control with the most headroom, 12 wrong glyphs --
the same count as M2's corrections on the target), C = the target (`target_marks_es17c7_seed2.json`, no clear context,
as the controls have none). Scorer `h30/score.py`, output `h30/score.log`; truth for a control glyph is its majority
plaintext letter, and "ceiling" is the best any key reaches (corrupted signs are unrecoverable).

| packet | blind letters | reader changes | right | wrong glyphs fixed | letters after | ceiling |
|---|---|---|---|---|---|---|
| A (5%, s1) | 92.1% | 2 (high) | 2 | 2 of 9 | 93.5% | 95.4% |
| B (10%, s2) | 80.4% | 1 (high) | 1 | 1 of 12 | 81.8% | 90.6% |
| D (5%, s3) | 92.1% | 0 | 0 | 0 of 8 | 92.1% | 95.2% |
| C target | 87.7% agree with key.tsv | 1 (medium): code 24 l->h ("mil hombres de infanteria") | agrees with key.tsv | 1 of M2's 12 | -- | -- |

**Reading.** The instrument is **high-precision, low-recall**: 3 of 3 control proposals right (precision 1.00 on
N=3 -- small), 3 of 29 wrong glyphs found (10%), gains of 0 to +1.4 letter points against 1-10 points of headroom.
On the target the one proposal agrees with M2's key (24 = h). So (a) a reader proposal, where one is made, is
trustworthy at this N on the controls, and the target's one agrees with M2 -- a small positive for M2's method;
(b) a reader's *silence* is not evidence against a key value: at 10% recall, M2's other 11 corrections (13=y,
15=n, 20=f, 21=i, 22=g, 25=u, 26=i, 33=e, 34=a, 65=s, 72=z) are neither confirmed nor refuted by this single
blind pass. The gate this row set for hand corrections is therefore met on precision only; it cannot license M2's
full correction set. The instrument that can is a verify mode (H33): hand the reader candidate changes, true and
decoy mixed, on controls first, and measure accept/reject discrimination before putting M2's 11 through it.
Cost: four Sonnet calls, text only (no vision). No token, grade or class change.

## Campaign step H33 (2026-09-28 14:29-14:37 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Calibration gate not met; the target call was not run** (CLAUDE.md rule 3, calibration
before target). Verify mode for hand corrections: each H30 control packet plus a list of candidate key changes, half
true (the control's own wrong glyphs to their majority plaintext letter) and half decoys (a glyph whose blind letter
is right, moved to the alternative letter that costs least under the es17c7 trigram score, matched to the true set's
occurrence counts), shuffled, glyphs relabelled (`cheap_test_1/h33/build.py`, `answers.json`, `packet_{A,B,D}.txt`;
the target packet `packet_C.txt`, M2's 12 corrections plus 12 decoys, is built but unread). One blind Sonnet reader
per control; scorer `h33/score.py`, output `h33/score.log`.

| control | true accepted | decoys rejected | glyphs with >= 2 occurrences: true / decoys rejected |
|---|---|---|---|
| A (5%, s1) | 6/9 | 9/9 | 4/4 / 7/7 |
| B (10%, s2) | 2/12 | 12/12 | 0/8 / 10/10 |
| D (5%, s3) | 1/8 | 8/8 | 1/4 / 6/6 |
| pooled | **9/29 = 0.31** | **29/29 = 1.00** | 5/16 / 23/23 |

Gate (true-accept >= 0.8 and decoy-reject >= 0.8): **not met** on true-accept. The reader is a strongly conservative
verifier: it never accepted a decoy, but it rejected most true corrections, including B's two largest (s1 o->a, 17
occurrences; s20 a->o, 12 -- a swapped vowel pair, each change alone breaks words the other still spells wrong) and
B's s10 i->g, which the H30 reader on the same packet had itself proposed. A's 4/4 on its multi-occurrence glyphs
against B's 0/8 shows the per-packet variance is large at this N. With H30 the picture is consistent: **a reader's
accept is informative (0 false accepts in 29 decoys plus H30's 3/3), a reader's reject or silence is not**; nothing
in this family can license or refute M2's other 11 corrections one by one. Reading the target through a verifier
this calibration fails would only produce accepts that H30 already showed (24=h) and rejects that mean nothing.
Limits: decoys were the model's least-cost alternatives, yet mostly implausible letters (q->f, b->a), so decoy-reject
1.00 overstates how the reader would treat a plausible wrong change; B's per-row verdicts are reconstructed from its
summary (it named its two accepts). Cost: three Sonnet text calls, no vision. No token, grade or class change.

## Campaign step H31 (2026-09-28 14:38-14:38 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** Does the unread stretch read better as letters around word codes? The
nomenclature-range tokens (72 at r16:21, 52 at r17:10, 48 at r17:20; 48 at r20:15; 65 at r24:4) removed from their
stretch, the remaining key.tsv letters scored with the es17c7 trigram (per-trigram mean, so removal length does not
bias), against 1,000 draws removing the same number of random non-nomenclature positions
(`cheap_test_1/h31/nomen_remove.py`, `result.log`).

| stretch | n | gain per trigram, nomenclature removed | random removal median / p95 | P(null >= obs) |
|---|---|---|---|---|
| r16+r17 (72, 52, 48) | 42 | -0.107 | -0.116 / +0.116 | 0.476 |
| r20 (48) | 21 | -0.077 | -0.052 / +0.181 | 0.503 |
| r24 (65) | 20 | -0.361 | -0.126 / +0.217 | 0.888 |

**Negative, with low power.** Removing the nomenclature tokens gains nothing beyond a random removal on any stretch,
so there is no local sign that these positions are word codes rather than letters; at r24 removal costs more than
89% of random removals (65 = s gives "tres [r]egimient..."), and at r20 48 = d gives "propondreis de si", both
letter-shaped, but neither passes a significance line the other way either. Power is limited: at n = 20-42 the null
spread is +-0.12 to 0.22 per trigram, so only a large word-code effect could have shown. The stretch's letters
without the three tokens ("gyeoneopuradlonburgsrfsucmaremayorparai") read no better than with them. The word-code
question for 48/52/65/72 stays with the Brussels register (H17). No token, grade or class change; disk only.

## Campaign step H32 (2026-09-28 14:39 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** The campaign's measured key features and scribal habits are now one checklist for the
Brussels register comparison (H17, ASKS 82): `REGISTER-CHECKLIST.md` (vowel homophones with counts, the M codes and
the boxed 101 to decide, the uneven homophone use of H21/H25, the dots and colon of H13/H15/H28, the full stops before
13). KEY-OFFICES.tsv's row for this key names the checklist in its notes_source, and its stale "N3 after two audits"
now reads N4 (AUDIT.md "N4 decision (28 Sept 2026, MERCY-N4)"); `tools/key_design.py --check`: KEY-DESIGN.tsv is
current. No token, grade or class change.

## Campaign step H34 (2026-09-28 14:44-14:47 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** Iterated blind reader: each H30 control's decode with the H30 reader's changes applied
(`cheap_test_1/h34/build.py`, `round1_keys.json`, same relabelling and format) read by a fresh blind Sonnet reader
(round 2); scorer `h34/score.py`, output `h34/score.log`.

| control | round-2 changes (right) | wrong glyphs fixed: blind -> round 1 -> round 2 | letters |
|---|---|---|---|
| A (5%) | 1 (1): s38 c->n, "cuadros y pinturas" | 2 -> 3 of 9 | 92.1 -> 93.5 -> 93.7% |
| B (10%) | 0 | 1 -> 1 of 12 | 80.4 -> 81.8 -> 81.8% |
| D (5%) | 0 | 0 -> 0 of 8 | 92.1% throughout |

Cumulative over two rounds: **4 of 4 proposals right, 4 of 29 wrong glyphs found (14%)**, no glyph broken. The loop
converges at once -- two of three readers propose nothing in round 2 -- so iteration does not raise recall materially
(10% -> 14%) and the target round was not run (the row's condition). With H30 and H33 the reader family is closed for
this question: blind readers are precise and conservative, and M2's remaining 11 hand corrections cannot be licensed or
refuted by any reader configuration tried (propose, verify with decoys, iterate). Script instruments that score each
correction against known truth on the same controls are the next line (H35-H37). No token, grade or class change.

## Campaign step H35 (2026-09-28 14:51-14:49 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Gate not met; the target's corrections were not scored.** Per-correction script
verifier on H33's candidate sets (29 true corrections, 29 least-cost decoys, three controls with known truth): each
change applied alone to the blind key, the decode scored by (a) wseg, a Viterbi word segmentation under an es17c7
word-unigram model (words with 2+ corpus occurrences; unknown chunk -12 - 3 x length), and (b) lex4, letters in
in-vocabulary words of 4+ letters in that segmentation (H14's measure without given word boundaries). Pre-registered
rule: accept iff delta > 0; gate 0.8 / 0.8 on either measure (`cheap_test_1/h35/verify.py`, `deltas.tsv`,
`result.log`; no hosts, no subagents, 4 s of CPU).

| measure | true accepted | decoys rejected | glyphs with >= 2 occurrences: true / decoys rejected |
|---|---|---|---|
| wseg | 17/29 = 0.59 | 27/29 = 0.93 | 11/16 = 0.69 / 22/23 = 0.96 |
| lex4 | 15/29 = 0.52 | 21/29 = 0.72 | 8/16 / 17/23 |

wseg is the best discriminator this campaign has measured for single corrections (readers: 0.31 / 1.00 in H33), but
it misses the gate on true-accept, including at n >= 2 where 10 of M2's 12 target corrections sit; its misses are the
rare letters (h, z) and corrections whose occurrences fall in corrupted stretches. The subgroup figure is reported, not
used: the gate was pooled and pre-registered, and moving it now would be threshold-shopping. No token, grade or class
change. The whole-set version (H36) asks a question this per-change rule cannot: whether M2's set moves the text as far
toward Spanish as a true key moves a control.

## Campaign step H36 (2026-09-28 14:53-14:52 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** The whole correction set at once under H35's word-segmentation measure (wseg, log-
likelihood per letter; `cheap_test_1/h36/wholeset.py` -> `result.log`), plus a selection control the row did not
name but the first numbers required (`h36/greedy.py` -> `greedy.log`, 2 min CPU): M2's corrections were chosen by a
reader to make words, so the fair null is a word-seeking search, not decoys.

| packet | blind | + true set (control truth / target key.tsv) | + decoy set | shuffled keys | greedy 12 wseg moves: gain, right |
|---|---|---|---|---|---|
| A (5%) | -2.157 | -1.977 (+0.180) | -2.511 (-0.354) | -3.55..-3.43 | +0.186, 3 of 7 right |
| B (10%) | -2.562 | -2.420 (+0.142) | -2.934 (-0.372) | -3.58..-3.50 | +0.209, 5 of 12 right |
| D (5%) | -2.301 | -2.246 (+0.055) | -2.507 (-0.206) | -3.54..-3.48 | +0.072, 4 of 6 right |
| **C target** | -2.387 | **-2.197 (+0.190)** | -2.664 (-0.276) | -3.58..-3.47 | +0.235, 5 of 9 agree with key.tsv |

**Reading.** First pass: M2's set gains +0.190, at the top of the controls' true-set gains (+0.055 to +0.180), and every
decoy set and shuffled key loses -- which looked like support. **The selection control voids it as a test:** on every
control a greedy word-seeking search reaches a gain at or above the true key's with only 12 of 25 moves right (48%),
so a word-model gain of this size is reachable by selection alone, half of it wrong. On the target the same relation
holds (greedy +0.235 above key.tsv's +0.190), exactly as on the controls: consistent with M2's set being truth-like,
but not able to tell it from a word-seeking set. Side result, independent of M2: the target's greedy search picks 5 of
M2's corrections unprompted (22=g, 34=a, 20=f, 21=i, 15=n) and 4 others (24=n, 65=r, 25=t, 48=t) -- at the controls'
48% move precision this agreement is suggestive only. Non-test by selection, not a negative; no token, grade or class
change. With H30-H35 this closes the line "license M2's hand corrections without a period key": every instrument tried
(blind reader, reader-verifier with decoys, iterated reader, per-correction script verifier, whole-set gain against a
selection null) either misses its control gate or cannot separate truth from word-seeking selection. The Brussels
register (H17, ASKS 82; checklist in REGISTER-CHECKLIST.md) is the instrument that decides them.

## Campaign step H37 (2026-09-28 15:00-14:54 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Gate not met; the target was not scored.** Design conformance as a per-correction
arbiter: violations V = sum over letters of |codes - expected| (3 per vowel, 1 per consonant, H16 / DECODE 958's stated
style), counted on glyphs with 2+ occurrences; accept a change iff it lowers V (`cheap_test_1/h37/design.py`,
`result.log`). On H33's control candidates (2+ occurrences): **true accepted 7/16 = 0.44, decoys rejected 22/23 =
0.96.** It cannot see a swap inside one vowel's homophones or between two vowels (B's s1 o->a and s20 a->o each raise V
by 2 on their own), which is where most true corrections of this design sit. Blind-key violations: A 3, B 5, D 6. No
token, grade or class change.

Note for H40: H35's wseg and this measure fail on largely different true corrections (wseg misses h/z letters, design
misses vowel swaps), so an OR of the two might pass where each alone does not -- but that rule is chosen after
seeing these data and may be tested only on fresh controls.

## Campaign step H38 (2026-09-28 15:04-14:58 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** Pools first, beyond Espagnol 142-144: eight Gallica SRU queries (Galarreta / Galaretta;
Léopold-Guillaume or Leopoldo Guillermo with chiffr/cifra; Mercy + chiffr on manuscripts; dc.source "Espagnol" with
chiffr + 1648 or cifra/cifrada; Peñaranda + chiffr) and one record read (`h38/sru.py`, `sru_hits.tsv`,
`fr3854.xml`; gallica.bnf.fr 9 requests, 2 s apart, browser UA, no errors).

- **Galarreta**: the only manuscript hit is Espagnol 144 itself (the target's own recueil, already swept, siblings.tsv).
- **Léopold + chiffre**: BnF Français 3854 (ark btv1b52520094g), Fronde papers of 1649 -- the prince de Conti's
  instructions and letters to and from Leopold Wilhelm, with Conti's mémoires "avec chiffre" (items 41-42) and "avec
  chiffre et déchiffrement" (item 43), and Leopold Wilhelm's replies in Spanish (items 12, 13, 18, in clear per the
  record). The ciphers are Conti's (Paris, the Frondeurs' side), not the Brussels secretariat's, so not a pool for
  this key; the shelfmark is already in the repository's 23 Sept digitised sweep
  (`sources/solver-diffs/2026-09-23-digitised-excluded.tsv`, "noise-on-inspection", "bourdeau-named:fr.3xxx"). A lead for the
  orchestrator, not for this folder: item 43 carries its own decipherment.
- **Mercy + chiffre, Espagnol + cifra, Peñaranda + chiffre**: no manuscript of 1647-1649 from this office (the hits
  are medieval manuscripts and sale catalogues matched in their full text).
- The BnF finding aid (archivesetmanuscrits) was not queried again: the 24 Sept cipher sweeps of it (LEDGER, LANE G2 F,
  G2 X, G3 B; 894 arks) hold no Léopold/Galarreta/Mercy item, and its pagination is unreliable from here (host table).
- Also on file, not a pool: QUEUE row DA5 (Leopold Wilhelm's command letters to Hatzfeldt, partly ciphered, German,
  Neuenstein) -- the imperial chancery, a different office and language.

**Negative for a pool on Gallica/BnF.** The pool for this key is the Brussels archive itself (AGR SEE, H7/H17, ASKS 82).
No token, grade or class change.

## Campaign step H40 (2026-09-28 15:09-15:01 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Gate not met; the target was not scored.** The rule fixed in CAMPAIGN.md before any new
data -- accept a correction iff H35's word-segmentation delta > 0 OR H37's design violations fall -- tested on three
fresh design-matched controls (h21/vowel_control.py on Cartas tomo 15 windows, seeds 11-13, 5% of signs corrupted as
exactprof_noisy.py does; blind es17c7 anneal, order 3, 8 restarts x 40,000 iters, blind letters 93.5 / 70.1 / 90.6%)
with their own true and least-cost-decoy candidates (h33's recipe): `cheap_test_1/h40/make.py`, `score.py`,
`result.log`, `verdicts.tsv`, `anneal_seed*.log`. **Glyphs with 2+ occurrences: true accepted 13/21 = 0.62, decoys
rejected 17/23 = 0.74.** Both sides miss 0.8; on held-out controls the OR rule is weaker than either measure looked on
the data that suggested it (the H33 sets), which is what a post-hoc rule usually does.

This is the second script-verifier attempt (H35, then H37, then this combination) and every number stayed below the
gate: per CLAUDE.md rule 3 ("a second attempt ... that changes only the one knob"), single-correction licensing of M2's
hand corrections is **untestable by script verifiers at this N**, not refuted. The instrument that decides them is a
period key (H17, ASKS 82; REGISTER-CHECKLIST.md). No token, grade or class change.

## Campaign step H39 (2026-09-28 15:02 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** H36's greedy search proposed four values differing from key.tsv (24=n, 65=r, 25=t,
48=t); REGISTER-CHECKLIST.md now lists each with every occurrence in context under both values, so the Brussels
register comparison checks both sides. By the text alone 24 = h stands ("de Cheureuse", "tres mil hombres"; the H30
blind reader also chose h), and the greedy n is a search artefact -- one of the 13 wrong moves in 25 its controls
showed. 65, 25 and 48 stay open both ways (still M). Disk only; no token, grade or class change.

## Campaign step H41 (2026-09-28 15:24-15:06 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. A crib candidate, not a reading.** The unread stretch after "el Elector de Brandenburg"
(r16-r17) carries the letters "... d l o n b u r g s [72] r f s [25] c m a r e [52] m a y o r ...". Hypothesis (formed by
eye from the context "pasareis a Cleues a ueros con el Elector de Brandenburg y con ..."): **BURGS[72]RF = Burgsdorf**,
with the nomenclature code 72 standing for a syllable (do) -- Konrad von Burgsdorff, the Elector's Oberkämmerer in the
1640s. Because the name was chosen after seeing the text, it is tested against every name a reader in that context
could have chosen instead:

- **Name list, built before scoring** (`h41/names.py` -> `h41/namelist.tsv`): 402 names -- every surname or place after
  von / v. / Graf / Freiherr / Herr / Oberst / Kanzler or with a possessive 's, 6-12 letters, seen twice or more, in
  *Urkunden und Actenstücke zur Geschichte des Kurfürsten Friedrich Wilhelm von Brandenburg* Bd. 4 (1867) and Bd. 5
  (1869), Internet Archive `urkundenundacten04berluoft`, `urkundenundacten05berluoft` (_djvu.txt; archive.org 3
  requests). Burgsdorf is 5th by frequency (95); the list keeps OCR variants (hurgsdorf, bnrgsdorf) and places.
- **Fit** (`h41/fit.py`, `h41/result.log`): each name aligned whole to the token stream, S-graded tokens +1 equal / -1
  unequal, M-graded and nomenclature tokens (48/52/65/72, 9, 15, 25) as wildcards for one or two letters, best start.

| window | Burgsdorf fit | rank | next real name | P (list fits >= Burgsdorf) |
|---|---|---|---|---|
| r15-r18, as pre-registered | 7 at r16:16 | 2 | brandenburg 11 at r15:11 (the already-read word) | 0.005 |
| r16:2-r18 (after the read "Brandenburg") | **7 at r16:16** | **1** (unique) | oranien / garantie / brandenburg 4 | **0.002** |

The pre-registered window ranked Burgsdorf second only behind the word the reading already holds at r15 ("Brandenburg"
itself); on the unread part it is the list's unique best fit, three points clear of any other name (its two OCR
variants aside), 7 of 9 letters matching at S-graded tokens with no mismatch. **By the row's rule it is a crib
candidate**, with the window caveat stated. What it implies, untested here: 72 is a syllable code (do), which fits H2's
nomenclature class; the next row (H42) tests the independent half of the same hypothesis ("su camarero mayor" after
the name). No key.tsv, token, grade or class change; nothing here is a reading.

## Campaign step H42 (2026-09-28 15:28-15:08 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Borderline; not a reading.** The independent half of H41's hypothesis: after the
Burgsdorf candidate, r17 reads "s [25] c m a r e [52] m a y o r" -- "su camarero mayor" (Oberkämmerer) if 25 = u,
one a is unwritten and 52 is a syllable (ro). Title list built before scoring (`h42/titles.py` -> `titlelist.tsv`): every
word X in "X mayor" in the es17c7 Cartas corpus, 4-12 letters, 3+ occurrences (37 titles; camarero itself is not among
them at that threshold -- camarera is -- so camarero was added as the tested item). Each phrase "su X mayor" aligned to
r17-r18 with H41's scorer (S tokens +1/-1, M and nomenclature tokens one-or-two-letter wildcards, no deletions for any
candidate); `h42/result.log`.

**camarero: fit 9 at r17:3, rank 1, tied with camarera** (the same title, differing only in the letter that falls on
the 52 wildcard); next correo 7 (correo mayor, also a real office), then guarda / alferez 5. P (list phrases fitting at
least as well) = 2/38 = **0.053 -- the pre-registered P < 0.05 is not met by the strict count**; with camarera merged as
a gendered variant of the same title (as H41 kept OCR variants apart but they are one name) it is 1/37 = 0.027. The list
is small, so P cannot resolve finer than about 0.03. Read with H41: the name that best fits the stretch is the Elector's
chief chamberlain, and the title that best fits the next words is chief chamberlain -- two fits that agree, one clearing
its gate and one on the line. Both assume nomenclature codes stand for syllables (72 = do, 52 = ro), which no period key
has confirmed. **Crib candidates for the orchestrator and the Brussels register comparison, not a reading**; no key.tsv,
token, grade or class change. REGISTER-CHECKLIST.md gains the two syllable values to check.

## Campaign step H43 (2026-09-28 15:31-15:10 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Context corroboration for the H41-H42 crib candidates; not a reading, no print of this
letter.** Full text of *Urkunden und Actenstücke ... Friedrich Wilhelm* Bd. 4 and 5 (the H41 downloads, grepped on
disk) and IA be-api full-text search of Cuvelier-Lefèvre VI (`correspondancede0006jose`; positive control "Brandebourg"
and "Clèves" both hit; `h43/fts_cuvelier6_*.json`; be-api 4 requests):

- **Title and place match the crib.** Urkunden Bd. 4 prints an "Instruction für den **Oberkammerherrn Conrad von
  Burgsdorf** zur Verhandlung mit dem Pfalzgrafen, Dat. **Cleve** 9. Febr. 1647" and a "Kurfürstliche Attestation für
  Burgsdorf dat. Cleve 10. Sept. 1647 -- Der Oberkammerherr etc. Conrad von Burgsdorf"; Bd. 5 calls him "den
  einflussreichen Oberkammerherrn Konrad v. Burgsdorf". Oberkammerherr is literally camarero mayor, and in 1647 he was at
  Cleves, the town the letter sends Mercy to ("pasareis a Cleues a ueros con el Elector de Brandenburg").
- **Spanish contact in the same business:** Bd. 4 records the Spanish governor of Guelders (Baron de Ribeaucourt,
  Roermond, 13 Feb 1647) sending a letter that the Elector forwarded to Burgsdorf at Düsseldorf, and Burgsdorf reporting
  "die spanische Mahnung zum Frieden an den Pfalzgrafen" (18 Feb 1647); and a 1647-48 section "Burgsdorfs an Kursachsen
  und Braunschweig". Spanish Netherlands officials dealt with him directly the year before.
- **Not found:** no 1648 passage naming Mercy, a Spanish envoy's approach to Burgsdorf, or a levy of 3,000 infantry in
  Bd. 4-5 (grep of Burgsdorf within three lines of spani-/Leopold/Erzherzog/Brüssel/Mercy/Niederland: five hits, all
  1647 or general); Cuvelier-Lefèvre VI has no Burgsdorf at all (0 hits, both spellings).

Corroboration of plausibility only: the man the name crib picks was the Elector's chief chamberlain, at Cleves, dealing
with Spanish officials, in the months before the letter. The crib stays a candidate until the Brussels register gives 72
and 52 (REGISTER-CHECKLIST.md). No key.tsv, token, grade or class change.

## Campaign step H17: the Brussels register itself (DECODE-OPEN, 28 Sept 2026)

DECODE's PI extended the project account's image rights on 28 Sept 2026; DECODE-OPEN (parent worker, session_015RJ8kumxcx2XKtHHU1zzsU)
fetched all 17 full-size images and the 5 attached transcriptions of DECODE 958-965 (AGR Brussels, Secretairerie
d'Etat et de Guerre inv.nr. 2, "chiffres 1647-98") at 14:54-14:57 UTC and read every letter table against key.tsv.
Details, per-cell grades and the blind second pass: `period_keys/README.md`, `period_keys/decode_{958,960,965}.tsv`,
`period_keys/comparison.tsv` (regenerated by `period_keys/compare_decode.py --check`).

Result: **no candidate period key.** Best agreement 7 of 28 shared codes (R965 p7, the run o-u = 2-8); R958, the
H16 design sibling, agrees on 1 of 24 (a = 10). No table has key.tsv's three-homophones-per-vowel, even-consonant
layout, and none gives a value for the M codes (9, 15, 25, 48, 52, 65, 72) or the boxed 101. The register shows
that o-u = 2-8 is a habit of this office (R965 p6 and p7). That is a design point, not a key. key.tsv stays `ours`
(cryptanalytic); the register closes as a period-key source for this letter. Images are not in the repository;
the holding archive's permission may be needed before any is published.

## Web and blog check (CHECK-SOLVED-WEB, 28 Sept 2026)

Parent worker CHECK-SOLVED-WEB, 28 Sept 2026 15:23-15:27 UTC (clock-read; the Spinelli lesson: a Cipherbrain comment thread held a
reading our print tools could not see). **Verdict: no prior reading, decipherment or transcription of this instruction
found on the open web or in the three blogs.**

| # | Query / page | Hits |
|---|---|---|
| 1 | `"abbé de Mercy" 1648 instruction chiffrée` | Geneanet, Maison de Mercy (fr.wikipedia), Mercy-Argenteau archive inventory (agatha.arch.be, 18th c.), BnF Ms-6829 record; nothing on this letter. |
| 2 | `"Espagnol 142" BnF chiffre OR cifra Mercy` | BnF archivesetmanuscrits record Espagnol 142-144 (ark cc347546, already on file); nothing else. |
| 3 | `"Baron de Mercy mi Sumiller de Cortina"` (the letter's opening clear text) | 0 exact hits; only dictionary pages for *sumiller de cortina*. |
| 4 | `"Autre instruction chiffrée pour l'abbé de Mercy"` (catalogue title) | only our own PR #16 (SO-MERCY-F22). |
| 5 | `Mercy 1648 Felipe IV Münster cifra instrucción Cipherbrain OR cryptiana OR ciphermysteries` | generic cipher pages; the Wikipedia "Mercy (cipher)" article is a 2000 block cipher, unrelated. |
| 6 | `site:cryptiana.blogspot.com Mercy 1648` | no post on this item. |
| 7 | `site:scienceblogs.de klausis-krypto-kolumne spanische Verschlüsselung 1648` (Cipherbrain) | 2015 "ungelöste Verschlüsselung aus dem Jahr 1645", 2016 Rabenhaupt (Thirty Years' War), 2018 Ferdinand II -- all different items. |
| 8 | `site:ciphermysteries.com Mercy 1648 Spanish instruction cipher` | nothing on this item. |
| 9 | `"Mercy" "1648" Spanish cipher instruction BnF Espagnol decipherment` | Bourdeau index + two forks (WebFetch of arya1515 fork: no Mercy / Espagnol 142 entry); unrelated Cryptologia/academia papers. |

No flag raised. Not a novelty statement (rule 10); AUDIT.md untouched.
## Campaign step H44 (2026-09-28 15:38-15:40 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Control failed on the name; the target reader was not run.** Blind replication of the
H41-H42 crib, control first (`h44/build.py`, `packet_control.txt`, `packet_target.txt`, `reply_control.txt`). Control: a
Cartas sentence with a known person and title ("y al conde de Baynete, su caballerizo mayor"), encoded as the target
stretch is shown (letters run together, 4 of 35 as "?", 2 wrong letters), with its clear context. The blind Sonnet
reader returned **"y al conde de Basto es su caballerizo mayor" -- office right, name wrong**: it read the damaged
"baysete" as a better-known title ("Basto") and explained the mismatching letters away as damage. By the row's rule the
control must recover its known name before the target counts, so the target packet was not read.

What this shows about the instrument: a reader recovers a common office from damaged letters but fills a proper name
from world knowledge where the letters are few and uncertain. A target reader naming Burgsdorf would therefore not
have been independent evidence either -- Burgsdorff is the best-known courtier of that Elector. The letter-fit test
against a list built before scoring (H41) is the right instrument for the name, and it stands as it was. One text
call. No token, grade or class change.

## Campaign step H45 (2026-09-28 15:45-15:56 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** If the nomenclature codes stand for syllables (H41-H42's reading of 72 and 52), which one-
or two-letter value reads best for 48 and 65? Every value of 1-2 letters (506) substituted at all of a code's
occurrences in the key.tsv decode, scored by H35's word segmentation (es17c7 word unigram); control: 200 draws of the
same number of random S-graded positions searched the same way (`h45/syll.py`, `h45/result.log`, 16 min CPU).
Pre-registered: a candidate must improve every occurrence and beat the control's 95th percentile.

| code | occurrences | key.tsv | best value | gain | per occurrence | control median / p95 | candidate |
|---|---|---|---|---|---|---|---|
| 48 | r17:20, r20:15 | d | "qu" | +4.42 | +4.97, -0.55 | -1.47 / +6.54 | no |
| 65 | r24:4 | s | **"sr"** | **+15.16** | +15.16 | 0.00 / +7.08 | **yes** |

65 = "sr" gives "tres regimient-" at r24 ("en dos o tres regimientos"); key.tsv's s leaves "tres egimient-". The test
cannot separate two readings of that gain: 65 as a two-letter unit (s + r, across a word boundary -- unusual for a
syllable code) or 65 = s with the scribe leaving out the r. Either way the word is "regimientos" and the passage reads
"en dos o tres regimientos". 48 has no value that helps both occurrences; it stays d (M). No key.tsv, token, grade or
class change: 65 stays M, with "sr" logged as the candidate value in REGISTER-CHECKLIST.md.

Note from DECODE-OPEN's H17 (merged this hour): the Brussels register 958-965, read at full size, holds no candidate
period key for this letter and no values for the M codes or the boxed 101, so the register checklist's syllable
questions (72, 52, 65, 48) have no period source on file; they stay cryptanalytic.

## Campaign step H46 (2026-09-28 16:07-15:57 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Negative.** The other unread stretch, v04 after "y que corra por su": its letters with M
and nomenclature tokens as "?" read "noladire?tnonysiiu?a". List built before scoring: every word after "por su" in the
es17c7 Cartas corpus, 4-12 letters, 3+ occurrences (30 words, `h46/wordlist.tsv`); each aligned to v04:1 with H41's
scorer (`h46/crib.py`, `h46/result.log`). Best: **"poca", fit 0** (two letters agree, two disagree), then vida / casa /
alma -2. The pre-registered rule (unique best, P < 0.05) is met only formally (P 1/30 = 0.033): a fit of 0 means nothing
aligns, so this is logged as no candidate, and the rule's gap is noted -- a list test also needs a minimum fit (for
example most letters of the word agreeing), which H41's Burgsdorf (7 of 9 letters, no mismatch) met and this does not.
v04 may not begin a word, or "por su" may not be the phrase boundary; the stretch stays unread. No token, grade or
class change.

## Campaign step H47 (2026-09-28 15:59-15:59 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Negative.** A given name before the Burgsdorf candidate? The tokens ending at r16:15 read
"...y e o n e o p ? r a d l o n". List built before scoring (`h47/given.py` -> `h47/namelist.tsv`): 217 words standing
before "von <Name>" in Urkunden Bd. 4-5 (mostly given names -- Iohann, Conrad, Friedrich, Moritz, Wilhelm -- with some
nouns), each fitted as "X" and "X de" ending at r16:15, H41's scorer. Best: **"anton", 3 letters agree and 2 disagree
(fit +1)**; then garnison 0, the rest below. The pre-registered rule (unique best, P < 0.05, >= 60% of letters
agreeing, at most one mismatch) is **not met**. Conrad fits badly in every form (conrad / conrad de / conrado: 0 letters
agreeing; conrado de: 3 agree, 4 disagree). So the words before the name are not his given name in any form the list
holds; the stretch before "burgs" stays unread, and the H41 name candidate neither gains nor loses. `h47/result.log`.
No token, grade or class change.

## Campaign step H48 (2026-09-28 16:00 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** The list-crib instrument of H41/H42/H46/H47 is now a shared tool,
`tools/crib_list_fit.py` (a keyed code stream, a window, a word list built before scoring; S tokens +1/-1, other
grades 1-2-letter wildcards; the list as the null; anchors start/end/free; forms such as '{w}de' or 'su{w}mayor'), with
the minimum-fit rule H46 showed was missing (candidate only as unique best, P < 0.05, >= 60% of letters agreeing, at
most one mismatch). Offline test `tools/tests/test_crib_list_fit.py`: catches H41 (burgsdorf unique best, 7 agree / 0
disagree at r16:16, candidate) and refuses H46 (poca unique best at P < 0.05 but 2 agree / 2 disagree). Re-run on H41's
402-name list it reproduces H41 exactly (burgsdorf 7, P 0.002, candidate True). SYSTEM.md names it (system_map_check
ok); h41/fit.py and h46/crib.py carry a pointer to it. Under the new rule H42's "su camarero mayor" would also need
checking against its minimum fit (it agrees on its S letters; its borderline was P, not fit). No token change.

## Campaign step H49 (2026-09-28 16:01 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. No candidate by the rule (tie).** The word after "para" at r17:20, window "?iense i embian
cartas de cr..." (48 as wildcard): list built before scoring = every word after "para" in the es17c7 corpus, 4-12
letters, 3+ occurrences (299 words, `h49/wordlist.tsv`); `tools/crib_list_fit.py --anchor start --start r17:20`
(`h49/result.log`). Best: **"bien" and "quien" tied, 3 letters agreeing and 0 disagreeing** (P 0.007); next defensa /
hacerse / poderse at 3/2. Not unique, so not a candidate. Observation only, for the record: with 48 = "qu" the passage
reads "... mayor, para quien se embian cartas de creencia que uan con esta" (to whom letters of credence are sent,
which go with this), which is also the value H45 found best for 48 at this occurrence (+4.97) -- but H45 found the same
value slightly worse at 48's other occurrence (r20:15, -0.55), so 48 stays d (M) and "qu" stays an observation. No
token, grade or class change.

## Campaign step H50 (2026-09-28 16:07 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Negative.** 48 as a three-letter unit: H45's search (`h50/syll3.py`, derived from
`h45/syll.py`) over the 300 most frequent letter trigrams of es17c7 (`h50/values.tsv`, written before scoring; "que"
is first), substituted at both occurrences (r17:20, r20:15), word-segmentation gain against key.tsv's d, with the same
200-draw random-S-token control. **Best value "aqu": gain -1.64** (per occurrence +1.33, -2.97); control median -7.95,
p95 +2.11. No three-letter value, "que" included, reads better than d at both places; with H45 (best two-letter "qu",
+4.42 but -0.55 at r20) that closes the value search for 48 by this instrument: 48 stays d (M). H49's "para quien se"
remains an observation at one occurrence only. `h50/result.log`. No token, grade or class change.

## Campaign step H51 (2026-09-28 16:08 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Context corroboration only.** The remaining *Urkunden und Actenstücke* volumes, Bd. 1
(1864), 2 (1865), 3 (1866) and 6 (1872) (IA `urkundenundacten0{1,2,3,6}berluoft` _djvu.txt; archive.org 4 requests),
grepped for Burgsdorf within three lines of spani-/Leopold/Erzherzog/Brüssel/Mercy/Werbung/Infanterie/1648
(`h43/h51_hits.txt`; Burgsdorf occurs 57 / 20 / 1 / 18 times). Eight hits; the relevant ones:

- **Bd. 2 (French side), Cleve, January-February 1648:** Wicquefort to Lionne, "Dat. Cleve 14. Jan. 1648 -- Burgsdorf
  und ein anderer Vertreter der 'guten Partei' an diesem Hofe zu Gratificationen vorgeschlagen"; Schwerin to Wicquefort,
  Cleve 20 Feb 1648, calling him "M. le grand-chambellan" (the French for Oberkammerherr, i.e. camarero mayor), and the
  editors' note that the Elector's Oberkammerherr Conrad von Burgsdorf was then working on a "third" armed party in the
  Empire with the Brunswick courts and Saxony.
- **Bd. 1:** a copy sent to Conrad v. Burgsdorf "nach Cleve" (Königsberg, 7 Oct 1648): he was at Cleves in 1648.
- No passage names Mercy, a Spanish envoy, or a Spanish request for troops through Burgsdorf; Bd. 3 has nothing; Bd. 6
  only a 1651 mission.

So in the months around 6 June 1648 the Elector's court sat at Cleves, Burgsdorf was its chief chamberlain and the
man foreign courts approached (the French proposing to pay him), which is what the H41-H42 crib has the Brussels court
telling Mercy to do. Corroboration of plausibility, not of the reading; absence of a Spanish passage refutes nothing.
No token, grade or class change.

## Campaign step H52 (2026-09-28 16:09 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** For the orchestrator's decision whether to send the r16-r17 crib to a separate verifier
session: `candidates/candidates.tsv` lists each candidate value with its step, test and result (72 = do, H41 met; 52 =
ro, H42 not met strictly; 65 = sr, H45 met but indistinguishable from an omitted r; 48 = qu at r17:20 only, not met,
observation), and `candidates/make_candidates.py [--check]` writes `candidates/reading_candidates.txt`: every cipher
line under key.tsv (K) and, where a candidate applies, the same line with it in braces (C):
r16 "GYEONEOPURADLONBURGS{do}", r17 "RFSUCMARE{ro}MAYORPARA{qu}I", r24 "TRE{sr}EGIMIENTIYCONQUE". --check passes.
reading.txt, key.tsv and every grade are unchanged; the file's header says these are candidates, not a reading.

## Campaign step H53 (2026-09-28 16:11 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** Robustness of H41 to its wildcard set: the same 402-name list and window (r16:2-r18:21)
through `tools/crib_list_fit.py` with fewer wildcards (`h53/result.log`):

| wildcards | Burgsdorf | next real name | P | candidate |
|---|---|---|---|---|
| (0) every non-S token (H41 as run) | 7 agree / 0 disagree, unique best | brandenburg / garantie 4 | 0.002 | yes |
| (a) only nomenclature 48/52/65/72 (9, 15, 25 at key.tsv letters) | 7 / 0, unique best | garantie / oranien 4 | 0.002 | yes |
| (b) only 72 | 7 / 0, unique best | altenburg / brandenburg 3 | 0.002 | yes |
| (c) none (72 = z) | not in the top 5 | altenburg 3 (6/3), 7-way tie | 0.017 | no |

The crib does not lean on the uncertain letter codes (9, 15, 25) at all: it stands on **one assumption, that the
nomenclature code 72 is a two-letter unit** (do); with 72 as the single letter z nothing on the list fits the stretch.
That is the one question a period key of this office, or another letter using 72, would settle. No token, grade or
class change.

## Campaign step H54 (2026-09-28 16:12 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Negative.** The words between "el Elector de Brandenburg" and the Burgsdorf candidate,
r16:2-15 "y e o n e o p ? r a d l o n": list built before scoring = every 2-5-word sequence in es17c7 beginning "y con",
8-16 letters, 3+ occurrences (79, `h54/phrases.tsv`), fitted with `tools/crib_list_fit.py --anchor end --end r16:15`
(`h54/result.log`). Best "y con esta ocasion", 7 agree / 6 disagree (fit +1); everything else below 0. No phrase meets
the rule. The span may hold a title or particle the newsletters do not use ("y con el Oberkammerherr" has no Spanish
form in the corpus), or carry misread tokens; it stays unread and the H41 name candidate is unaffected. No token,
grade or class change.

## Campaign step H55 (2026-09-28 16:13 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Negative.** v04 anchored at its end (the clear "sera mas conuenient" follows): list =
every word before "sera" in es17c7, 4-12 letters, 3+ occurrences (17, `h55/wordlist.tsv`), `tools/crib_list_fit.py
--anchor end` at v04:19 (the gutter token, 15, M, wild) and at v04:18 (`h55/result.log`). Best "cual" fit 0 (1/1) at
v04:19, "bien" -2 at v04:18; no word meets the rule. With H46 (start-anchored) both ends of v04 are tested by list and
neither fits; the stretch stays unread. No token, grade or class change.

## Campaign step H56 (2026-09-28 16:14 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** Is H53's one assumption (72 is a multi-letter unit) this office's habit? Answered from
DECODE-OPEN's transcriptions already on disk (`period_keys/README.md`, section "The M codes and the H41/H42 syllable
reading"; no new fetch): in the Brussels register's own keys, codes just above the letter alphabet are syllables where
they occur -- R960 48 = no, 65 = ba; R962 (Latin) 52 = re, 65 = s, 72 = san, 101 = vu; R963 101 = ay; R959's two-letter
word codes (au, de, du ...) run 12-89 and R961's syllabary starts at 35. So a syllable at 72 in a key of this office
is the office's practice, not an exception; **the assumption the Burgsdorf crib rests on is consistent with the
register's design, but no table gives 72 = do or 52 = ro** (these are other keys). No token, grade or class change.

## Campaign step H57 (2026-09-28 16:15 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Usage attested both ways -- a caution for H42.** Google Books API (key present, country=US;
7 queries, 1.6 s apart; `h57/gbooks.tsv`):

- **"camarero mayor del Elector" for an elector's courtier is period usage**: *Mercurio histórico y político* (1739),
  "el Conde de Preysing, Camarero Mayor del Elector" (Bavaria); *El gran diccionario histórico* (1753), "camarero mayor
  del elector de Baviera". So a Spanish writer could call an electoral Oberkammerherr "su camarero mayor".
- **But "camarero mayor" is also the Spanish title of the Elector of Brandenburg himself**, as Arch-Chamberlain of the
  Empire (Erzkämmerer): *Crónica del emperador Carlos V* ("el Marqués de Brandemburgo, su Camarero mayor"), *Estado
  político de la Europa* (1740), *El gran diccionario histórico* (1753, "Brandeburgo, Camarero Mayor"). Near "el Elector
  de Brandenburg" the phrase could therefore name the Elector's own imperial office rather than a courtier.
- Spanish print knows the man as "Conrado de Burgsdorf" only in modern works (1919, 2006); no 17th-century Spanish hit
  for Burgsdorf; "Burgsdorf" with "camarero mayor" 0.

Effect on the crib: the name fit (H41, H53) does not depend on the title; the title fit (H42, borderline) now has a
second reading that does not need Burgsdorf at all ("... [Burgsdorf], su camarero mayor" vs a phrase about the Elector
as camarero mayor del Imperio). H42 stays borderline, and the pair of fits is weaker evidence of one person than H42's
note put it. No token, grade or class change.

## Campaign step H58 (2026-09-28 16:18 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Negative.** The Brussels side in calendar form, for 1648 entries on Brandenburg / Cleves /
a levy / Mercy that might name the persons Mercy was to see. (1) Cuvelier-Lefèvre VI, IA be-api full-text search
(`correspondancede0006jose`; 8 queries, `h58/fts_*.json`): Brandebourg, Clèves, levée, "trois mille", Neubourg hit
only early-century entries (Archduke Albert, the Jülich-Cleves question); Mercy hits only the known p.647 (no. 1499) and
index lines; Burgsdorf 0. The API returns at most five snippets per query, so this is a sample, not a full read. (2)
Lonchay 1896, *La rivalité de la France et de l'Espagne aux Pays-Bas*, full _djvu.txt (IA
`la-rivalite-de-la-france-et-d-espagne-aux-pays-bas-1635-1700`, grep; `h58/lonchay_hits.txt`): one Brandenburg passage
near 1647-49 dates (the 1658 imperial election), nothing on Mercy's Cleves mission beyond p.445 (already in
siblings_brussels.md). archive.org 3 requests, be-api 8. No token, grade or class change.

## Campaign step H59 (2026-09-28 16:32 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Non-test by construction, not a negative.** A list-free check of the crib: H45's value
search (506 one- and two-letter values, word-segmentation gain, 200 random-S-token draws) run for 72 and 52
(`h59/syll_72_52.py`, `h59/result.log`).

| code | best value (gain) | crib value: rank of 506, gain | control p95 | candidate |
|---|---|---|---|---|
| 72 (r16:21) | "e" (+3.07) | **do: 134th, -3.00** | +7.08 | no |
| 52 (r17:10) | "s" (+2.43) | **ro: 390th, -5.69** | +7.01 | no |

Neither crib value is favoured, but neither could have been by this instrument, and the control could not show it
(CLAUDE.md rule 3, "a control that cannot vary on the same axis"): the word model is es17c7's Spanish vocabulary, in
which "burgsdorf" occurs 0 times, so "burgs-do-rf" makes no known word and earns nothing; and "camarero" (17
occurrences) cannot be formed at 52 by any value, because the stretch reads "s u c m a r e [52]" -- the a after c is
missing, which a value at 52 cannot supply. A list-free value search can only confirm a value that completes a word
the corpus knows with no other letter missing. The crib's evidence stays H41/H53 (name fit, list null) with H43/H51/H56
as context. No token, grade or class change.

## Campaign step H60 (2026-09-28 16:33 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** The crib's own tokens (r16:14-21, r17:1-12) in every pass on disk: pass A and pass B
(Y6) agree on every token (A grades 72 and 52 m, B h); `disagreements.tsv` has no r16/r17 row; MEYE's blind pass
(`meye/blind_pass.tsv`) reads the same codes, with 72 at r16:21 graded M: **"written as one run-together stroke pair
with no visible gap; could be a single two-digit code 72 or two adjacent single tokens 7, 2"**; H2's three reads
(`h2crops/reconcile.tsv`) settle 72 as one group, 3 of 3 ("7 has the hand's leading top bar; gap 7-2 matches
intra-group gaps"); 52 is one group 3 of 3. So the transcription of the crib's letters is solid, and the one
alternative any pass raised is at 72 itself: **if r16:21 were the two tokens 7 (t) and 2 (o), both S-graded letters,
the stretch would read BURGS-T-O-RF, "Burgstorf", with no syllable assumption at all.** H2's gap measurement favours one
group; the question is filed as H62 (score the split reading with the same list and rule). No token, grade or class
change.

## Campaign step H62 (2026-09-28 16:34 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. The name fit no longer needs the syllable assumption, if r16:21 is two signs.** MEYE's
alternative (H60): r16:21 read as the two tokens 7 (t, S) and 2 (o, S) instead of the one code 72. A copy of the stream
with that split (`h62/cipher_codes_split72.tsv`; cipher_codes.tsv untouched) through `tools/crib_list_fit.py` on H41's
402-name list, window r16:2-r18:21 (`h62/result.log`):

| wildcards | Burgsdorf | P | candidate |
|---|---|---|---|
| default (M-graded tokens wild) | unique best, 8 of 9 letters agree, 1 disagrees (t for d) | 0.002 | yes |
| only 48/52/65 wild (9, 15, 25 at key.tsv letters) | same, 8 / 1 | 0.002 | yes |
| **none at all** (every token at its key.tsv letter) | **same, 8 / 1** -- next altenburg / brandenburg 3 | **0.002** | **yes** |

Read with 7 2, the stretch gives **B-U-R-G-S-T-O-R-F** letter for letter from codes graded S (12 b, 8 u, 5 r, 22 g,
6 s, 7 t, 2 o, 5 r, 20 f), and **"Burgstorf" is a period spelling of the name**: Urkunden Bd. 1 prints "Burgstorf" 7
times and "Burgstorff" 15 times beside 57 "Burgsdorf" (grep of the H51 download). The one disagreement with the list's
"burgsdorf" is exactly that spelling difference. Against it: H2's three reads call 72 one group ("gap 7-2 matches
intra-group gaps"), the code 72 occurs only here, and a separate 7 followed by a separate 2 occurs nowhere else in the
letter (0 pairs). So the crib now rests on a single transcription question -- one sign or two at r16:21 -- which an
objective gap measurement on the image can settle (H63). No token, grade or class change; cipher_codes.tsv unchanged.

## Campaign step H63 (2026-09-28 16:36 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. One sign: 72.** Objective gap measurement on line r16 of the native image
(`images/f22r_canvas58.jpg`, band y 3019-3244, H15's settings: threshold < 100, components of area >= 40 px and height
>= 12 px; `h63/gaps.py`, `h63/gaps.log`). The line's 34 ink spans map onto its 21 tokens from the end (72 = spans 32-33,
6 = 31, 22 = 29-30, 5 = 28, ...). Gaps split cleanly at about 25 px: **inside a group 5-14 px** (n = 14, the 13 px gap itself included), **between groups
33-74 px** (n = 19). **The 7-2 gap at r16:21 is 13 px**, inside the intra-group range and 20 px below the smallest
between-group gap on the line. So r16:21 is one code, 72, as H2's three reads had it; MEYE's "7, 2" alternative and
H62's letter-for-letter "BURGSTORF" are disfavoured by the leaf's own spacing. The Burgsdorf crib therefore rests again
on H53's one assumption, that the nomenclature code 72 stands for two letters (do) -- consistent with the office's
habit (H56) but unattested for this key. H62's result stands as recorded (the fit if the split were real), with this
measurement against the split. No token, grade or class change.

## Campaign step H61 (2026-09-28 16:37 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** H41 against larger lists built the same way (`h41/names.py`) from the Urkunden volumes
H41 did not use -- Bd. 1, 2, 3, 6 alone (599 names, `h61/names_bd1236.tsv`) and all six volumes (883,
`h61/names_bd1to6.tsv`) -- through `tools/crib_list_fit.py` on r16:2-r18:21, with only 72 wild (every other token at its
key.tsv letter) and with the default wildcards (`h61/result.log`). In all four runs **every fit of 5 or more is a
spelling of the one name** -- burgsdorfs 8/0 (the genitive, its s landing on the s of "su"), burgsdorf 7/0,
burgstorff 7/1, buigsdorf / bnrgsdorf / hurgsdorf (OCR variants) 6/1 -- and the best other name is "brandenburg" at 3-4,
the word already read at r16:9. P (list fits >= best) 0.002 (599) and 0.001 (883). The name fit is stable to the list:
a list three times larger from independent volumes turns up no rival. It still rests on 72 standing for two letters
(H53, H63). No token, grade or class change.

## Campaign step H64 (2026-09-28 16:38 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** The crib record is consolidated for the orchestrator: `candidates/candidates.tsv` (72's
row now carries H53, H61, H62/H63; 52's carries H57) and REGISTER-CHECKLIST.md ("Update, 28 Sept 2026 evening").
`candidates/make_candidates.py --check` passes (the reading_candidates.txt lines are unchanged: the candidate values did
not change, only their evidence). In one sentence: the unread r16-r17 stretch fits the name Burgsdorf (the Elector's
Oberkammerherr, at Cleves in 1647-48) better than any of 883 period names if, and only if, the nomenclature code 72 stands
for the two letters "do" -- the office's habit, unattested for this key. Disk only; no token, grade or class change.

## Campaign step H65 (2026-09-28 16:39 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Negative, with a precedent.** Meinardus, *Protokolle und Relationen des Brandenburgischen
Geheimen Rates* (1889-1907), six IA copies (`bub_gb_EeYXAAAAYAAJ` = Bd. 3, `protokolleundre01meingoog`,
`protokolleundre03meingoog`, `bub_gb_x-4XAAAAYAAJ`, `bub_gb_zuQXAAAAYAAJ`, `protokolleundre02meingoog`), _djvu.txt grepped on
disk (archive.org 7 requests). "Mercy" occurs once in all six (a "Kapitän Mercy" in a muster list, Bd. 3); no Spanish
envoy, Abt or Erzherzog passage is dated 1648 or tied to Mercy. The one Leopold Wilhelm mission found is Bd. 3 no. 501:
**"Sendung des Freiherrn von Ribaucourt seitens des Erzherzogs Leopold Wilhelm an den Kurfürsten. Cleve. [15 August]
1647"**, about restoring Count Schwarzenberg -- not Mercy's business, but a precedent a year earlier for the archduke
sending an envoy to the Elector at Cleves (Ribaucourt, governor of Spanish Guelders, is the same man who wrote to
Burgsdorf in Feb 1647, H43). Corroboration of the channel only. No token, grade or class change.

## Campaign step H66 (2026-09-28 16:41 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Negative / partly unreachable.** *Theatrum Europaeum* vol. 6 (1647-1651) is not on Internet
Archive under that title: the only IA copy found (`bub_gb_5L1OAAAAcAAJ`, 1662) is vol. 1 (1617-1629; no 1647-1651 dates
in its text), so vol. 6 is **unreached**, not searched. Google Books API (key, country=US; 4 queries, `h66/gbooks.tsv`):
"Theatrum Europaeum" Mercy Cleve 1648, "Abt von Mercy" Cleve, "Abbé de Mercy" Clèves Brandebourg 1648, and a German
phrasing -- 0 volumes each. No contemporary print of Mercy's Cleves mission found by these routes. archive.org 2
requests, googleapis 4. No token, grade or class change.

## Campaign step H67 (2026-09-28 16:42 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Negative: no alternates to try.** v03-v05 in every pass on disk: pass A and pass B agree
on all 18 readable tokens of v04 (A grades 15 at v04:9, 7 at v04:10, 21 at v04:16 and 15 at v04:19 m); disagreements.tsv
has only v04:19 (B has no token there); MEYE marks v04:16 "21" followed by a colon-like mark (punctuation, as H13
inventoried) and v04:19 "1?" unreadable at the gutter; H2's three reads agree: 15 one group at v04:9, 21 + colon at
v04:16, v04:19 cut by the photograph's edge (partial, 15/16/19). So the unread v04 stretch is not a transcription
tangle: every token but the gutter one is read the same by every pass, and the gutter token was already a wildcard in
H46 and H55. No list crib gets a new substitution to test; the stretch waits for a period key or the gutter capture
(H12, ASKS 81). No token, grade or class change.

## Campaign step H68 (2026-09-28 16:44 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Negative.** BSB/MDZ (www.digitale-sammlungen.de): the search page is rendered client-side
(plain curl returns the shell only), so `tools/browser_fetch.js` was used, one request at a time, 3-4 s apart (6
requests; saved pages in `h68/`). MDZ's search covers metadata and full texts of the Theatrum Europaeum continuations
(e.g. bsb10807452, vol. 14). Exact-phrase queries: **"Abt von Mercy" 0 matches, "Abbt von Mercy" 0**. Unquoted queries
(Mercy Cleve Churfürst 1648; Mercy Burgsdorff) are OR-matched across the library (406,192 and 103,584 hits, topped by an
English novel), so they are noise, not a test. Vol. 6 itself (1647-1651) was not opened page by page. No
contemporary German print of the abbé's 1648 mission found by this route. No token, grade or class change.

## Campaign step H69 (2026-09-28 16:45 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Unreached at issue level.** Gallica SRU (6 requests, 2 s apart, `h69/sru.tsv`): "abbé de
Mercy", Mercy + Clèves, Mercy + Brandebourg, each with dc.date 1648, match the *Gazette* (Paris, 1631-1761,
ark:/12148/cb32780022t) only **as a whole collection** -- the date filter does not narrow a periodical record, so these
hits say only that the words occur somewhere in 130 years of the Gazette -- plus 1648 books unrelated to the mission
(Dupleix, *Le Tacite françois*). The 1648 issues are not separate SRU records; reaching them needs the collection's date
listing (`https://gallica.bnf.fr/ark:/12148/cb32780022t/date1648`) and a ContentSearch per issue (about 100 requests),
more than this row's cap and the host's per-session rule allow. Left as the route for a later worker: list the 1648
issues once, then `services/ContentSearch?ark=<issue>&query=Mercy` for the June-August issues only (about 15 requests).
No token, grade or class change.

## Campaign step H70 (2026-09-28 16:47 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Negative.** The *Gazette* (Renaudot) for 1648 is one annual volume on Gallica
(`ark:/12148/bpt6k6391523f`, the collection's only 1648 date, 16480101). Gallica ContentSearch inside it (5 requests
including the date listing, 2 s apart; `h69/cs_*.xml`): "Mercy" / "Merci" 6 hits, all the word *merci* ("à la merci
des Confédérez", "se rendre à la merci du Parlement"), never the abbé; "Brandebourg" 14 hits, all the peace treaty,
Pomerania, the Elector's levy in Prussia (PAG_572) and the Polish succession -- none on a Spanish envoy at Cleves. The
Paris Gazette did not report Mercy's mission. No token, grade or class change.

## Campaign step H71 (2026-09-28 16:49 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. The Burgsdorf fit does not occur by chance in this letter's read text; the tool's rule
needed a floor, now added.** False-positive control for H41's method (`h71/fp.py`, `h71/windows.tsv`,
`h71/result.log`): every 62-token window (the unread stretch's length), step 8, over the letter's cipher stream,
excluding the unread stretch, v04, and the cipher spellings of Brandenburg, Cleues and Cheureuse -- 24 read, name-free
windows -- scored against the 883-name list (Urkunden Bd. 1-6) with the same wildcard rule.

- **No window reaches Burgsdorf's fit**: the best fit in any read window is **4** (24 of 24 at most 4), against **7 with
  no mismatch** for Burgsdorf on r16:16 (8 for the genitive burgsdorfs). Read Spanish text of this letter does not throw
  up a name-fit anywhere near the one on the unread stretch.
- **But the tool's candidate rule (H48) passed short names at fit 4** in 10 of the 24 windows -- two distinct spots,
  "xanten" (5 agree / 1 disagree) around r19-r21 and "tarent" in v05-v06 -- because uniqueness, P and "60% of letters,
  at most one mismatch" are all easy for a six-letter name. Fixed in `tools/crib_list_fit.py`: `--min-score` (default
  6) requires an absolute fit above what the target's read text produces; `tools/tests/test_crib_list_fit.py` gains the
  H71 must-not case (xanten at r19:6 refused, and passing without the floor); SYSTEM.md's entry updated. Re-run with the
  floor: 0 of 24 read windows pass, and H41's Burgsdorf (7) still passes. H46, H47, H49, H54, H55 were all negatives
  under the old rule, so the floor changes none of them.

No token, grade or class change.

## Campaign step H72 (2026-09-28 16:50 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** Synthetic-name null for H41, finer than the list's 1/883 (`h72/synth.py`,
`h72/result.log`): a character trigram model trained on the 883 Urkunden names sampled 10,000 name-shaped strings of
6-12 letters (seed 72, list names excluded), each fitted to r16:2-r18:21 with `tools/crib_list_fit.py`'s default
wildcards. **0 of 10,000 reach Burgsdorf's fit (7 agree, 0 disagree): P < 0.0001 (95% upper bound about 0.0003).** Three
reach 6, and they are the model rebuilding the Burgsdorf pattern itself from its training names ("burgsdorfdrg",
"urgsburf", "lenburgse"). With H71 (read text of the letter never above 4), H61 (no rival among 883 real names) and
H53/H63 (the fit needs only 72 to stand for two letters, and 72 is one sign), the name fit is as strong as a
cryptanalytic crib gets here without a key; it is still a candidate, not a reading, because the one assumption is
unattested for this key. No token, grade or class change.

## Campaign step H73 (2026-09-28 16:53 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** Adversarial review of the Burgsdorf crib: one blind Sonnet reader given only
`h73/packet.md` (the 29 NOTES sections H41-H72 that bear on the crib, plus candidates/candidates.tsv) and asked to argue
against it. Its eleven objections, ranked by it, with the runner's answer to each:

1. **"Fatal": H59 ranks "do" 134th of 506 for 72, so the campaign's own instrument contradicts the crib.** Not so: H59
   is logged as a non-test by construction -- the Spanish word model contains no "burgsdorf", so no value at 72 could
   earn a gain by completing it. H59 neither supports nor contradicts; the reviewer's point that nothing independent
   *confirms* 72 = do stands, and is the crib's stated limit.
2. **"Fatal": the null list is not independent -- it comes from the Brandenburg court's own chronicle, where Burgsdorf is
   frequent.** A fair point about the list as null: a court-specific list is the right *competitor* set (anyone Mercy
   could be told to see) but not a neutral null. H71 (read text of the letter never fits any of these names above 4) and
   H72 (synthetic names) partly answer it; H74 is added to answer it directly with a Brandenburg-independent onomasticon.
3. **H42 misses its bar (P 0.053) and passes only after a post-hoc merge.** Agreed; H42 has been logged "not met strictly,
   borderline" throughout and is not counted as support.
4. **"camarero mayor" may be the Elector's own imperial title (H57).** Agreed; recorded in H57 and candidates.tsv.
5. **The tool's rule was revised twice against this target's data.** True; both revisions tightened the rule (H48 minimum
   fit, H71 --min-score), neither changed Burgsdorf's numbers (7 agree / 0 disagree, P from the list and from H72), and
   both are recorded with the cases that forced them. Researcher degrees of freedom remain in the choice of window and
   list, which the controls below were built to bound.
6. **No source names Mercy, a Spanish approach to Burgsdorf, or the levy.** Agreed: all corroboration is plausibility
   (H43, H51, H65); the event itself is unconfirmed.
7. **H44 shows famous-name bias; the hypothesis was formed by eye.** Agreed that it was formed by eye (stated in H41);
   the list fit is mechanical, and H71/H72 test what a mechanical fit throws up by chance.
8. **The 13 px gap is at the top of the intra-group range.** It is the largest intra-group gap but 20 px short of the
   smallest between-group gap (33); the separation is clean, the call not borderline, though a better image would help.
9. **H72's generator is trained on the same corpus.** True; H72 shows the fit beats names shaped like that court's names,
   no more.
10. **65 = sr is not evidence for syllable codes.** Agreed; it was never used as such (H45 states the omitted-r reading).
11. **48 = qu sat in the candidates table though not met.** Fixed: candidates.tsv now marks 48 "not applied", and
    reading_candidates.txt (regenerated, --check passes) no longer applies it at r17:20.

Reviewer's overall verdict: "a carefully controlled and reasonably strong statistical candidate ... but it cannot bear
the weight of an identification ... treat it as a flagged hypothesis for a separate verifier and the period-key search,
not as a reading, and not as reportable outside the repo." The runner agrees with that verdict. No token, grade or class
change.

## Campaign step H74 (2026-09-28 16:54 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** H73's objection 2 answered with a Brandenburg-independent null: every capitalised word of
6-12 letters, 3+ occurrences, in the es17c7 Cartas newsletters (1634-48, the whole Spanish monarchy's people and places)
and in Lonchay 1896 -- 2,702 words (`h74/onomasticon.tsv`; Burgsdorf is absent; Luneburg, Luxemburg, Brandemburg, Burgos
present) -- fitted to r16:2-r18:21 with `tools/crib_list_fit.py` (default floor; `h74/result.log`). Best: **"cartas" 6/0
at r18:12 -- the real, already-read word of "y embian cartas de creencia"**, which the window includes (the tool finding a
word that is there); then amiens / cuaresma 5, adrien / tamayo 4 on the unread part; luneburg and burgos 3. **No word of
the independent onomasticon reaches Burgsdorf's 7 with no mismatch on the unread stretch.** With H71 (read text never above
4), H72 (0 of 10,000 synthetic names) and H61 (no rival among 883 court names), the name fit is not an artefact of the
list it was scored against. It remains conditional on 72 = two letters (H53, H63). No token, grade or class change.

## Campaign step H75 (2026-09-28 16:56 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** Rule 7 for the crib: `candidates/crib_evidence.py [--check] [--skip-image]` regenerates
every number the Burgsdorf crib candidate stands on from committed files into `candidates/crib_evidence.tsv` (20 s; needs
Pillow for the H63 gap): H41 7 (7/0) at r16:16, P 0.002; H53 the same with only nomenclature or only 72 wild, 1 (5/4) with
none; H61 P 0.002 / 0.001 on 599 / 883 names; H62 split 8/1; H63 gap 13 px; H71 read windows at most 4; H72 0 of 10,000;
H74 best independent name on the unread tokens 5 (cuaresma). `--check` passes. This is what a separate verifier session
would run first; the crib stays a candidate. Disk only.

## Campaign step H76 (2026-09-28 16:57 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Negative.** v04:1-19 with a free anchor, `tools/crib_list_fit.py` default floor
(`h76/result.log`): words after "por su" (H46, 30) best "mano"/"turno" 1; words before "sera" (H55, 17) best "dicen" 2;
the H74 onomasticon (2,702) best "relation" 4 (5 agree / 1 disagree at v04:7) -- the level read text reaches by chance
(H71). No candidate; v04 stays unread. No token, grade or class change.

## Campaign step H77 (2026-09-28 16:58 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Negative.** Of H14's out-of-vocabulary words, the ones not already worked (lonburg /
szrfsucmarey = H41-H74, noladirent... = H46/H55/H76, eleues = Cleues, read) leave "oulay" at r10 ("... nos infume de
oulay sepamos"). r10:1-19 ("enosinf?medeoulayse") with a free anchor against the H74 onomasticon (best "infante" /
"remedio" 3) and the 883 Urkunden names (best "frieden" 2): nothing near the floor (`h77/result.log`). No other proper
name surfaces by this method. No token, grade or class change.

## Campaign step H80 (2026-09-28 16:58 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Negative.** Gallica's IIIF info.json for canvas 59 (ark btv1b10035717h/f59; 1 request)
gives 3546 x 5245 px, exactly the size of the committed `images/f22v_canvas59.jpg`: the file on disk is already the
native image, so no larger Gallica image of f.22v's right edge exists to recover the gutter token v04:19. The token
needs a new capture of the leaf (H12, ASKS 81). No token, grade or class change.

## Bourdeau corrections folded in (1 Oct 2026)

**Status unchanged: partial** (a status change is the orchestrator's). Source: D. Bourdeau's reply of 1 Oct 2026 on
dbourdeau/cyphersolver issue 16 (quoted by the owner) and his files, snapshotted unmodified at
`sources/cyphersolver/2026-10-01/mercy1648/` (`ct_f22.tsv`, `edits.tsv`, `key.tsv`, `NOTES.md`, `lost_edge.tsv`,
`open_stretches.tsv`; MIT / CC BY 4.0). His page is built on our issue 16 (transcription, key, reading), so it is a
check and correction of our work, not a prior decipherment. Every correction was checked here on the native Gallica
images already on disk (`images/f22r_canvas58.jpg`, `images/f22v_canvas59.jpg`, 3454 x 5261 / 3546 x 5245), with
earlier crops in `h2crops/` and new local crops in `bcheck/` (cut with PIL from the disk images; no Gallica request for
the leaf itself). A token-stream diff of his `ct_f22.tsv` against our `ciphertext.tsv` shows no other difference: the
eight places below, the three 19/14 positions MREV had reverted, our five-plus-one existing 14 readings, and notation
(`BOX` = `[MARK:box]`, `14` = `[MARK:frac]`).

### Per token

| where (old pos) | ours before | Bourdeau 1 Oct | what the image shows (1 Oct 2026, this session) | verdict | word before -> after |
|---|---|---|---|---|---|
| r24:4 | 65 (key M, s) | 6 5 = s r | a visible gap with a paper crease between the 6 and the 5 (`h2crops/h10h11_crop_A.jpg`; H10's blind A already read "6 5") | agree, split | TRESEGIMIENTI -> TRES REGIMIENTOS |
| r17:10 | 52 (key M, y) | 5 2 = r o | written as one tight group, spacing like the within-group gap of 18 and 30 beside it (`h2crops/crop_r17_p9-11.jpg`): the image is neutral on segmentation | agree on the range argument (no code above 34) and sense | CMAREYMAYOR -> CMAREROMAYOR |
| r17:20 | 48 (key M, d) | 4 8 = q u | one tight group, the open-topped 4 (`h2crops/crop_r17_p19-21.jpg`); the same hand writes "que" as "4. 8." apart at r24:18-19 (`bcheck/r24_right.jpg`) | agree, range + sense | PARADIEN -> PARA QUIEN |
| r20:15 | 48 (key M, d) | 4 8 = q u | as r17:20 (`h2crops/crop_r20_p14-16.jpg`), the closed-bowl 19 next to it for contrast | agree, range + sense | DESISE -> QUE SI SE |
| r16:21 | 72 (key M, z) | 7 2 = t o | one tight group (`h2crops/crop_r16_p19-21.jpg`), neutral | agree, range + sense | BURGSZRF -> BURGSTORF |
| r18:5 | 26 (S, i) | 2 6 = o s | one tight group (`h2crops/h10h11_crop_D.jpg`); 26 is also a valid code (i), so this split rests on sense alone | agree, sense | SEIEMBIAN -> SE OS EMBIAN |
| r24:13 | 26 (S, i) | 2 6 = o s | one tight group (`bcheck/r24_p13-14_z4.jpg`), as r18:5 | agree, sense | REGIMIENTIY -> REGIMIENTOS Y |
| v01:15 | 19 (S, e) | 14 = c | the open-topped 4 with a crossbar, not the round closed bowl this hand gives 9 (`bcheck/v01_p14-16_z4.jpg`) | agree | YALEAMARE -> Y AL CAMARE[ro] |
| r14:7, r16:3, r16:6 | 19 (S, e) since MREV | 14 = c ("your five exceptions check out") | the same open 4 with crossbar; r15 has a "19 14" pair side by side that shows the two forms (`bcheck/r14_p6-7_z3.jpg`, `bcheck/r15_p3-5_z3.jpg`, `bcheck/r16_p3-6_z3.jpg`) | agree; restores M2's reading against the three blind passes MREV followed | ELEUES -> CLEUES; Y EON EO -> Y CON CO |
| r10:8 | 25 (key M, u) | 2 5 = o r, by sense, M | a normal tight 25 (`bcheck/r10_p7-9_z4.jpg`); neutral | accepted at M, credited | INFUME -> INFORME |
| r10:13-14 | 2 8 (S, o u) | one 28 = l, by sense, M | the 2 and the 8 stand apart at an ordinary between-token gap (`bcheck/r10_p12-15_z3.jpg`): the image is against the merge | accepted at M as a sense repair, kept as two tokens in `ciphertext.tsv` (the second carries no letter) | DEOULAY -> DELLA Y |

Disagreements with Bourdeau: none on value. One difference of emphasis: the image does not itself show a gap inside
52, 48, 72 or 26 (only inside 65), so those six splits rest on the key's range (no code above 34; H2's 3/3 "one group"
was a read of spacing, not of the key) and on the words, and are graded M here; Bourdeau also marks them M in his
`ct_f22.tsv`.

### How applied

- `ciphertext.tsv`: the seven splits (65, 52, 48 x2, 72, 26 x2) as two tokens each, confidence M, `alt` holding the
  group as transcribed, `why` naming the crop; positions renumbered on r16, r17, r18, r20, r24. 522 -> 529 tokens.
- `exceptions.tsv` (2 -> 9 rows): 19 -> c at r14:7, r16:3, r16:6, v01:15 (M); Bourdeau's two r10 re-cuts (r10:8 = "or",
  r10:13 = "l", r10:14 = no letter), M, credited.
- `key.tsv`: rows 48, 52, 65, 72 removed (no occurrences left); notes on 14, 19, 25, 26 updated. No value changed.
- `corrections.tsv` steps 12-16; `cipher_codes_529.tsv` (new: the code stream, 529 rows, 34 distinct signs, with the six
  19 -> 14 glyphs applied; `cipher_codes_522.tsv` stays for reproducing H3 onward).
- `decode.json` header line names the fold-in. `python3 tools/decode_key.py ciphers/espagnol142-mercy-1648` then
  `--check`: "ciphertext.tsv: tokens 529: M 41, S 488" / "reading up to date" (exit 0).

**Grades (rule 4): 529 tokens: H 0, C 0, S 488, M 41, I 0, U 0** (was 522: S 496, M 26). No H or C: a cryptanalytic
result. Open, as Bourdeau also finds: v04:9-13 and 17-19 ("no la dire?t non", "si i un[?]", code 15 twice, the second cut
by the gutter) do not read as Spanish; the letters lost at the trimmed right edge of f.22v (`lost_edge.tsv`:
camare[ro], encarga[r s]e, su [ma]no, pag[an]dola, leua[nt]ar, cons[ig]uiese, tener [tan]ta gente) are restorations by
sense, not tokens, and are not counted as read.

Reading, cipher runs as now regenerated (r14-r24): "pasareis a CLEUES a ueros con el elector de Brandenburg y con
COPURAD LON BURGSTORF su CMARERO mayor para quien se os embian cartas de creencia que uan con esta y les propondreis
que si se permitira se leuanten en aquel pais tres mil hombres de infanteria en dos o tres regimientos y con que
condiciones y al camare[ro] mayor si querra encargar[se] della ..."; r09-r10: "que el [box] uenga con uos para que nos
informe della y sepamos".

### Judge (rule 7, pasted)

```
$ python3 tools/judge_plaintext.py specs/espagnol142-mercy-1648.json --file ciphers/espagnol142-mercy-1648/reading.txt
ok   length: got=1349, min=200, max=1000000000
FAIL language: score=-1.018, null_p99=-1.923, real_p05=-0.875, real_median=-0.813, mode=both, N=1349
FAIL - espagnol142-mercy-1648 (a PASS is a gate for a verifier, not a reading; rule 10)
```

Up from -1.031 (522 tokens, MREV) and still a FAIL against real_p05 -0.875, far above the null (p99 -1.923). The spec
judges against the default `es` corpus, not an era/register-matched one (rule 3, es17c paragraph: a FAIL here is of
unknown reliability); reported as a FAIL.

### Names (identifications, not readings)

- **The box sign = the comte de Saint-Ibal** (Chevreuse's associate in the 1647-48 talks). Credited to D.
  Bourdeau (1 Oct 2026). Evidence: the clear sibling instruction of 13 Apr 1648, f.21r (Gallica canvas 56), which this
  session read on a 1800 px image (1 Gallica request): "Despues de oydo a la Duquessa con Santibal, Dessearia si fuesse
  possible que este viniese con Vos incognito (si pareciere), para que me hiciese relacion de las noticias ..." and
  further down "en procurar que Santibal venga aqui"; the cipher of 6 June has "de la duquesa de Cheureuse y del [box]"
  (r06-r07) and "que el [box] uenga con uos para que nos informe della" (r09-r10), the same request in the same words
  (now that r10 reads "informe"). Bourdeau also cites f.20r (8 Feb 1648) "el Conde de S. Ibal"; not re-read here. Our
  own H29 (28 Sept 2026) had Saint-Ibal and the duke of Lorraine as the two names fitting both contexts and graded
  neither; the f.21r parallel is what separates them. **Grade I** (an identification from a sibling leaf's clear
  text, not plaintext of this letter and not a key value); `key.tsv` keeps the box as `_` (M), so the reading does not
  render the name.
- **"COPURAD LON BURGSTORF su CMARERO mayor" = Konrad von Burgsdorff, the Elector's Oberkammerherr (camarero mayor).**
  Credited to D. Bourdeau (1 Oct 2026) for the reading through the splits 72 = t o and 52 = r o and for "copurad" =
  Conrad. Our own campaign had the name and the title as crib candidates (H41, H42, H43, 28 Sept 2026: Burgsdorf the
  unique best fit of 402 names, camarero the best title, Urkunden Bd. 4 "Oberkammerherrn Conrad von Burgsdorf", at
  Cleve in 1647), but assumed 72 and 52 were syllable codes (do, ro); the splits make every letter a key letter.
  "burgstorf" is exact (t for d); "copurad" is two letters off "conrad" and "lon" one off "von"; "cmarero" drops an a.
  **Grade I** for the identification; the letters themselves keep their token grades (S, with the split tokens M).

### Lesson

Five of the eight corrections (four distinct codes: 48 twice, 52, 65, 72) were tokens above 34 in a key whose values run
2-34 (count corrected 2 Oct 2026, reply drafter): a range check on the token stream against the key's own range
(now `tools/decode_key.py --split-check`) would have flagged 48, 52, 65 and 72 as two digits written together on the day the key
settled (M2, 25 Sept 2026), instead of carrying them for six days as "M codes" (H36 searched letter values for 48 and 65; H41-H42
assumed syllable values for 72 and 52). H2's three-way eye-check settled each as "one group" from spacing alone,
which the image cannot decide for this hand. Suggestion (one line, not done here): a `--range-check` option in
`tools/decode_key.py`, or a check in `tools/design_prior.py`, that lists every token outside the key's own numeric
range before a key is called settled.

Requests this session: gallica.bnf.fr 1 (f.21r canvas 56 at 1800 px, for the Saint-Ibal parallel); no other host.

## Code 15 (v04), 2 Oct 2026

**Status unchanged: partial.** Synthesis of three analyses run on 1-2 Oct 2026 after the Bourdeau fold-in (image,
key structure, crib), by the orchestrator's synthesis worker. Briefed as "1 Oct 2026"; the clock read 2 Oct 2026
01:07 UTC (rule 6). Their scratch output is in `code15/image/`, `code15/key/` and `code15/crib/`. No token, value,
grade or class changed: `ciphertext.tsv`, `key.tsv` and `reading.txt` are as the fold-in left them (15 = n, M).
Bourdeau's own position (`sources/cyphersolver/2026-10-01/mercy1648/key.tsv`, `open_stretches.tsv`) is 15 = no
value, with "probably n" ("una sera") at v04:19 and "direction" reachable only if v04:9 is a 14 and v04:11 is a 31.
He does not accept that reading because it moves two glyphs.

### What the three agree on

- **Two occurrences, both in v04.** v04:9 (`...corra por su [ma]no la dire[15]t non y si iu[15]`) and v04:19, the
  half-cut glyph at the gutter. Nothing else in 529 tokens carries 15 (image angle: none on f.22r or the lower lines
  of f.22v).
- **v04:9 is a real 15, one group.** H2's three reads already had this (3/3, step H2). The image angle's eye pass
  agrees: an S-form 5, a 13 px gap inside the group against 34-69 px between tokens, and this hand's 4 is crossed.
  So Bourdeau's 15 -> 14 alternative is held unlikely on four reads. All of them were made knowing what was being
  tested.
- **v04:11 looks like 31 (i), not 32 (n).** Both the image and the crib angle say so (no head loop or flat foot,
  the tall l-shaped 1 of the 31s at v04:6 and :17). This session looked at `code15/image/v04_p6-11_x2.jpg` and
  `v04_p11-15_x2.jpg` and saw the same. That makes three looks, all **primed** by Bourdeau's "direction" idea and
  none blind. Pass A, pass B, H2 and Bourdeau all read 32. The call stays a proposal and `ciphertext.tsv` keeps 32
  until two blind reads are run on an unlabelled sheet (rule: two passes).
- **The key is laid out as a table, and x and z have no code.** The even values 10-32 are a-n in order, 2-8 are o-u,
  the odd values 17-25 are a e i o u and 27-33 are u o i e (28 of 28 codes fit). 1, 11 and 35 never occur. The
  key and crib angles both read 11 x, 13 y, 15 z from this. One more point from the record (this session, from
  `period_keys/decode_965.tsv`): the same office's register table R965 p7 has o-u = 2-8 and then x y z = 9 10 11.
  So in this office, x, y and z sit together right after the o-u run. That supports "z near y", not the exact slot:
  our 9 is q (H11, a blind read).
- **Under z the "extra i" disappears.** "y si iuz[g]a sera mas conueniente" uses every token at v04:14-19 (31 = i/j).
  It needs one token (22, g) lost in the gutter, which ASKS 81 would show.
- **Nothing decides it.** Neither the key nor the crib angle's letter model can separate the leading letters at
  either place, as their own known-answer controls show (rule 3):
  - key angle: the true letter is ranked first 59.8% of the time, z first only 33%, and the gaps are under 1 point;
  - crib angle: 65% first overall, 95% first when the margin is at least 1.0, and the margin at v04:9 is 0.03.
  No value reaches S.

### Where they disagree, and why the grade stays M

- **Which sibilant.** The key and crib angles say z. The image angle says "ç / z / c, one sibilant code". c already
  has 14 and no consonant but q has a second code, so c is the weakest member of that set. Every Brussels office
  table on disk carries a z and none a ç (`period_keys/decode_958.tsv`, `_960`, `_965`), so if the code is a
  sibilant, it is the table's z, used for the ç sound too.
- **No single value gives standard spelling at both places.**
  - c reads v04:9 cleanly ("la direction", with 31), but v04:19 gives "iuc[g]a", which is not a word.
  - z reads v04:19 as "iuz[g]a" (juzga), but v04:9 gives "direztion". The key and crib angles both looked for a
    z (or ç) + t spelling and found none. The image angle's "Latinate -ct-, period-normal" applies to "direction"
    with c, not to z.
  - n (our committed value, from the Y8 anneal) gives no word at either place. It is also corpus-dependent: the
    held-29 anneal gave 15 = s on es17 and n on es17c7 (campaign step H3).
- **The statistics lean away from z, weakly.**
  - The key angle's order-5 model ranks z 13th of 23 after the edge fill, with n and c 2nd and 3rd. A true z ranks
    13th or lower in 10% of control trials, so this is mild evidence, and only on standard spelling.
  - The crib angle's window judge (es17c7, 77 letters) FAILs the z variant (-0.976) and PASSes c (-0.919).
  - The same window judge also PASSes Bourdeau's word-model variant (-0.883), which needs 15 = c in one place and n
    in the other. A judge that passes an internally inconsistent reading at this window cannot gate the choice,
    and its top six letters fall within 0.035 of each other. Both the PASSes and the FAILs here are noise, not
    evidence. The full-text judge cannot move on two letters out of 1349 (every variant -1.017 to -1.025, FAIL).
- **z rests on two things only:** the table layout and one word at the weaker of the two occurrences.
- **"z is missing" is weak.** The key angle expects about 1.9 z in 525 letters; a Poisson count of 0 at that mean
  happens about 15% of the time.
- **The 1e-26 figure measures the wrong thing.** The crib angle's "28 of 28, about 1 in 1e26 by chance" was
  computed for a scheme read off the recovered key. It shows the table is ordered, which nobody disputes. It does
  not measure how likely the extrapolated slot 15 = z is.

### Weakest needed links for 15 = z (each would have to hold)

1. **v04:19 is a 15.** Only the 1 and the left 12 px of the second digit survive. H2 read it 3/3 as unreadable; the
   image angle reads 13, 15, 17 or 19, and it chose 15 partly *on sense*. Picking the glyph by the word the value
   is meant to produce is circular: this occurrence cannot support the value on its own.
2. **One lost gutter token is 22 (g).** Unseen, so this is a restoration (I), not a reading.
3. **v04:11 = 31.** Primed, not blind (above). This one is needed only for v04:9; even with it, z gives a spelling
   for which no example was found.
4. **A clerk wrote z for the c of "direction".** Unattested.

### Grades (rule 4)

- **15 = z: M.** The best supported value, but no reading. It is a proposal that fits the table and one restored
  word. 15 = c and 15 = n are also M and weaker. 15 as a misread 14 is disfavoured on four reads.
- **v04:9 and v04:19 stay M**, whatever value is chosen.
- **"juzga" at v04:17-19 + gutter:** at best M for the letters read and I for the restored g. It is conditional on
  link 1, which does not rest on the value it supports.
- **No change to the counts:** 529 tokens: H 0, C 0, S 488, M 41, I 0, U 0.

### Proposals for the orchestrator (not applied here)

- (a) **Run two blind Sonnet reads** of v04:11 (31 or 32) and v04:9 on an unlabelled crop sheet with this hand's 2s,
  4s, 5s and 31/32s. Neither reader should be shown "direction" or Bourdeau's page.
- (b) **Only after (a), if both read 31:** change `ciphertext.tsv` v04:11 to 31 (M) and `key.tsv` 15 n -> z (M,
  note "table layout; juzga at v04:19; direztion unattested"). Then regenerate with `tools/decode_key.py --check`.
  - The value change alone (n -> z) is defensible now, since n has no word and no stable anneal support. But it
    changes the reading, so it goes through rule 7 and the orchestrator.
- (c) **Widen ASKS 81's expected value.** A gutter capture of f.22v would also check every letter in Bourdeau's
  `lost_edge.tsv`: about 18 restored letters on v01-v12 and the unrecovered v05/v06 junction. The row's "one
  token" understates it.
- (d) **Rule-10 check before anything goes out.** Any outward sentence about 15 says "proposed at grade M" and names
  the circular link 1. It must not say "15 = z" bare.

### Blind read of v04:6-19 (MERCY-C15, 2 Oct 2026, 13:1x UTC)

Proposal (a) above, run. Brief `.claude/briefs/runs/2026-10-02-acct3-mercy-c15.md`. Files in `code15/blind/`.
- **Sheet.** v04 positions 6-19 (14 crops) plus six control tokens elsewhere on f.22v (v05:9 = 14, v05:14 = 32,
  v05:15 = 31, v05:17 = 32, v03:7 = 13, v03:8 = 4). Line band from `tools/iiif_lines.py --image
  images/f22v_canvas59.jpg --region 0,500,3546,900`; tokens cut by column ink gaps (19 groups on v04, matching
  ciphertext.tsv), padded 22 px, x3, shuffled (seed 20261002), letter labels only. No positions, no candidate values,
  no word or "direction" shown (`cut_sheet.py`, `sheet_unlabelled.png`, key in `sheet_key.json`).
- **Reads.** Two Sonnet subagents, digits only, from the crops. The first pass B came back with its labels scrambled
  (it gave "15, cut by the binding" to the "21:" crop), so its rows were discarded unused as a protocol failure, not a
  read. A fresh pass B then read one file per call and wrote each row before opening the next file. Results are in
  `reads.tsv`.
- **Result: both blind reads agree with `ciphertext.tsv` at every v04 position 6-19 (14/14).**
  - **v04:11 = 32 on both reads**, each at medium confidence with 31 as the alternative.
  - v04:9 = 15 on both (high; medium with 13 as the alternative).
  - v04:19 = 15 on both, low (cut by the gutter; alternatives 13/14/17, or 15 with the second digit 5/6/9/3).
- **Controls.** 5 of 6 read correctly by both passes: all three 31/32 controls, 13 and 4. v05:9 (14) split: 19 on
  pass A, 14 on pass B. So both readers separate this hand's 31 from 32 on the controls, and this hand's 4 can pass
  for a 9.
- **Reconciliation** (this worker, against the crops; `recon_J_vs_31_32_controls.png` puts v04:11 beside the three
  31 and three 32 controls):
  - The second digit of v04:11 has a curved head and a short foot turning right.
  - That sits between the hand's 31 (a tall "l" with a small foot hook) and its 32 (a round head and a long flat
    base). It is nearer the 32s in having a rightward base, nearer the 31s in length.
  - Not decidable from the image beyond the two reads.
- **Applied.** Nothing. Brief rule: change only if both blind reads agree *against* the current value. They agree
  with it. `ciphertext.tsv`, `key.tsv`, `reading.txt` and AUDIT.md are untouched; there is no `corrections.tsv` row.
- **What this does to the proposals.**
  - The three primed looks that read v04:11 as 31 are **not confirmed blind**. Proposal (b)'s conditional ("if both
    read 31") does not fire, so "direction" (v04:9-11 with 31) stays without support from the image.
  - v04:9 as a real 15 now has two blind reads besides the four primed ones, so the 15 -> 14 alternative is weaker
    still.
  - The value of 15 is unchanged: n (M) committed, z the best proposal (M). It now rests on the table layout and
    "iuz[g]a" at v04:19 only. v04:19 is still a low-confidence glyph (link 1 above).
- **Grades.** No change: 529 tokens, H 0, C 0, S 488, M 41, I 0.

## Code 15 applied (4 Oct 2026, A3V2-MERCY15)

Worker A3V2-MERCY15 (account 3, for LANE-A3V2, brief `.claude/briefs/runs/2026-10-04-acct3-a3v2-wave1.md`), 04:56-05:0x
UTC (`date -u`). The lane's decision on proposal (b)'s value change alone (verdict line of 2 Oct 2026): **`key.tsv` 15 n
-> z at grade M, both occurrences**, on the evidence already on file and nothing new -- the table layout (even 10-32 a-n,
2-8 o-u, so 11 x 13 y 15 z; R965 p7 of the same office puts x y z right after o-u) and "iuz[g]a" at v04:17-19 with one
gutter token restored. v04:11 stays 32 on the two blind reads (MERCY-C15), so no "direction"/"direztion" is formed and
none is claimed: v04:9-13 reads "...no la direzt non..." and is still no word. c (M) stays weaker ("iuc[g]a").

- **Applied.** `key.tsv` row 15 (value, grade M unchanged, source and note rewritten); `python3 tools/decode_key.py
  ciphers/espagnol142-mercy-1648` then `--check` -> "reading up to date", exit 0.
- **Diff old vs new reading (rule 7):** exactly the two code-15 tokens changed, v04:9 n -> z (M) and v04:19 n -> z (M);
  `reading.txt` line v04 `NOLADIRENTNONYSIIUN` -> `NOLADIREZTNONYSIIUZ`; every other token identical. Counts unchanged:
  529 code tokens, H 0, C 0, S 488, M 41, I 0, U 0 (15 was already M).
- **Judge (rule 7, pasted):**

```
$ python3 tools/judge_plaintext.py specs/espagnol142-mercy-1648.json --file ciphers/espagnol142-mercy-1648/reading.txt
ok   length: got=1349, min=200, max=1000000000
FAIL language: score=-1.025, null_p99=-1.923, real_p05=-0.875, real_median=-0.813, mode=both, N=1349
FAIL - espagnol142-mercy-1648 (a PASS is a gate for a verifier, not a reading; rule 10)
```

  -1.025 against -1.018 under 15 = n: inside the -1.017..-1.025 band the 2 Oct synthesis already measured for every
  code-15 variant ("the full-text judge cannot move on two letters out of 1349"); still a FAIL against the default `es`
  corpus (rule 3, es17c paragraph: of unknown reliability), reported as a FAIL. No evidence for or against z.
- **Grades.** 15 = z: M (a proposal that fits the table and one restored word; not a reading). v04:9 and v04:19 M.
  "juzga" at v04:17-19 + gutter: M for the letters read, I for the restored g, conditional on v04:19 being a 15 (two
  blind reads, low confidence). Rule 10 (proposal (d)): any outward sentence says "15 proposed as z at grade M", never
  "15 = z" bare.
- **Propagated (rule 10):** AUDIT.md "Reading revised: code 15 n -> z at M (4 Oct 2026)" (safe sentence re-read: no
  word of it changes, counts unchanged); `second-opinions/PROMPT-chatgpt.md` correction block (it quotes the reading;
  the `SECOND-OPINIONS-QUEUE.tsv` row SO-MERCY-F22 is `checked` and quotes no reading, left as is).
- **Owed, not done here (brief did not name it):** `rederive/reading_fresh.txt` (the rule-7 fresh re-derivation) predates
  this change and now differs at the two M tokens; a fresh re-derivation from spec + key would show the same two-token
  diff, within the M-graded count (41), so it does not send the reading back, but the file is stale until re-run.

## Remaining gaps (finish-or-blocker pass, 2 Oct 2026, refreshed 4 Oct 2026)
Read so far: 521 of 529 code tokens (98.5%) read as Spanish words, 8 open in v04 (positions 9-13, 17-19); v04:6-19 glyphs confirmed by two blind reads, 2 Oct 2026; NOTES.md "Bourdeau corrections folded in (1 Oct 2026)", `reading_tokens.tsv` (H 0, C 0, S 488, M 41; the two box signs are counted as read but render as `_`); briefed as 1 Oct, clock 2 Oct 2026 (rule 6)
- code 15's value (both occurrences) - blocker: open-codes; two tokens. Now z at grade M in `key.tsv` (applied 4 Oct 2026, A3V2-MERCY15, on the table layout and "iuz[g]a" at v04:19; n and c weaker, both M). Neither key-angle nor crib-angle letter model separates the candidates within its own control (`code15/key/key15_out.txt`, `code15/crib/control_ranks.tsv`), the full-text judge cannot move on two letters (-1.025 vs -1.018), and the Brussels register holds no matching key (H17). v04:11 read 32 and v04:9 read 15 on two blind reads (MERCY-C15, `code15/blind/reads.tsv`), so "direction" has no image support and v04:9-13 is no word under any value. Lifted above M only by new material: a sibling letter in this key with 15 in a readable word (siblings sweep negative, `siblings_1648_hunt.md`; the AGR SEE 15 April 1648 instruction waits on ASKS row 60 / SEND-QUEUE S3), or the gutter capture of f.22v (ASKS row 81) showing the token after v04:19 is 22 (g), which would make "juzga" a read word and take v04:19's value to S
- v04:19 (half-cut 15) and the token(s) lost after it in the gutter, expected 22 (g) - blocker: waiting-on ASKS row 81 (gutter capture of f.22v, riding on the BnF batch of ASKS row 78, quotes awaited); H80: the disk image is already Gallica's native size
- letters lost in the gutter of f.22v, v01-v12 (Bourdeau `lost_edge.tsv`: about 18 restored by sense, not counted as read; the v05/v06 "conuenient[e ...]ar otra" and v06/v07 "gente de [?] que" junctions are unrecovered) - blocker: waiting-on ASKS row 81 (the same capture; its stated value of "one token" understates this)
- the box name sign, r07 and r09 (2 tokens) - blocker: no-key-material; identified as Saint-Ibal at grade I from the clear f.21r sibling (fold-in "Names"), but no table gives a value for the boxed sign (H17: no boxed 101 in DECODE 958-965), so `key.tsv` keeps `_`

## Escalation (2 Oct 2026, refreshed 4 Oct 2026)
- [x] siblings: Gallica/BnF pool sweep negative (M3, H38, `siblings.tsv`); clear sibling instruction f.21r (13 Apr 1648) read and used for the Saint-Ibal parallel (fold-in 1 Oct 2026), f.20r (8 Feb 1648) cited by Bourdeau, not re-read here; the 15 April 1648 instruction in Brussels (AGR SEE t. LXIV f.16) is waiting on ASKS row 60 / SEND-QUEUE S3; MERCY-SIB (2 Oct 2026, `siblings_1648_hunt.md`): no other cipher piece of the 1648 mission found with an image online -- AGR SEE (AGATHA T 100 EAD, 2,896 items, none with a digital object; Lonchay's t. LXIV lies in inv. 238-260, part not resolvable; Mercy/Galarreta 1648 correspondence inv. 576/578), Urkunden und Actenstuecke (earlier passes), Europeana, cached PARES sweep (no AGS Estado Flandes 1648 rows); GStA PK and Archivportal-D unreachable from the cloud
- [x] clear-pages: the f.21r clear text is the parallel for "que el [box] uenga con uos para que nos informe"; f.22r's clear overview read for spelling (ç in "negociaçion", "Operaçiones"; image angle 1-2 Oct 2026); no clear minute or draft of the 6 June 1648 instruction found (Lonchay-Cuvelier-Lefèvre IV no. 183 is a calendar only, per Bourdeau's snapshot)
- [x] known-keys: DECODE 958-965 (AGR SEE inv.nr. 2, "chiffres 1647-98") read in full size, best agreement 7/28, no period key for this letter (H17, 28 Sept 2026); design sibling R958 (H16); R965 p7 places x y z right after o-u = 2-8, a design point for 15 = z, not a key
- [x] print: Le Clerc 1725 III-IV, Acta Pacis Westphalicae II B (ends 19 May 1648), Lonchay 1896 p. 445 n. 2, Lonchay-Cuvelier-Lefèvre IV no. 183 (calendar); none prints f.22 (NOTES.md opening sections; Bourdeau snapshot NOTES.md "Print")
- [x] key-rebuild: Y8 anneal, M2, held-29 anneals (H3), crib steps H41-H77, Bourdeau's digit-pair splits (fold-in 1 Oct); code 15 swept with two letter models, each with a known-answer control, plus a window judge (1-2 Oct 2026): no value licensed above M, best z
- [x] image-check: out-of-range and doubtful tokens re-read on the native images (fold-in 1 Oct 2026, `bcheck/`); v04:6-19 read blind twice on an unlabelled shuffled sheet with six controls (MERCY-C15, 2 Oct 2026, `code15/blind/`): 14/14 agree with ciphertext.tsv, v04:11 = 32
- [x] retry: reading regenerated after the fold-in (`tools/decode_key.py --check`: "reading up to date", 529 tokens); v04 re-decoded under 15 = n, c, z and with v04:11 = 31 (`code15/crib/judge_variants.tsv`); after the blind reads (MERCY-C15) the value change alone applied 4 Oct 2026 (15 n -> z at M, A3V2-MERCY15; `--check` exit 0, two tokens changed, judge -1.025 FAIL as before), v04:11 left at 32
Verdict: keep going: 1 internal gaps; cheapest next: re-run the rule-7 fresh re-derivation (`rederive/`) against the 4 Oct 2026 key so the committed file matches, ~$1; code 15 itself is open-codes at M, lifted only by ASKS row 81 (gutter) or a sibling with 15 in a readable word
