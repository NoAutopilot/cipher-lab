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
