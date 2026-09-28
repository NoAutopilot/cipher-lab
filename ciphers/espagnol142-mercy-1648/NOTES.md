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
