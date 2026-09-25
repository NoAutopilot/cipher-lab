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
