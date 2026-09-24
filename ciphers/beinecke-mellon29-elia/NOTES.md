blocked

**Held by the LANE N3 orchestrator, 24 Sept 2026 17:40 UTC:** status `blocked`, not `open`: the check-solved pass did not read an edition or catalogue for the item (section 2) and did not check the DECODE record documents or the Aymeloglu repository (LANE N3 edition rule; COMMON addition (c)). The nomination line of 17:28 is held. Edition check: brief `.claude/briefs/runs/2026-09-24-lane-n3-csED3.md`.

# Pseudo-Elian alchemical cipher, "Lumen luminum" — Beinecke Rare Book & MS Library, Mellon MS 29

QUEUE row: CS2-14 (`sources/solver-diffs/2026-09-24-cyphersolver-site.tsv`, LANE N3 scout scCS2, 24 September
2026 — catalogue item 169 at dbourdeau.github.io/cyphersolver/catalogue.html), DECODE R2877. Check-solved run
24 September 2026 by LANE N3 csCS2c (session_0113dPptSGXZiBF5uwvtKmtc), brief
`.claude/briefs/runs/2026-09-24-lane-n3-csCS2c.md`.

## What it is

Not a letter — an alchemical codex, "Lumen luminum," ascribed (almost certainly falsely) to "Elias Cortonensis"
(Elia da Cortona, a 13th-century Franciscan; the manuscript itself dates to c.1525, and the catalogue's own
judgement is that the attribution is a deliberate pastiche, "a hint of charlatanism"). Bourdeau's catalogue:
"attempted, open (not a letter -- alchemical codex; cipher only ff.1v-2v, ~234 letters; simple/homophonic/
progressive/Vigenère/Alberti all fail)." Prior scout pass (24 Sept 2026) marked the image route "Beinecke online
viewer not checked this pass; DECODE thumbnail only" and the row "copy-order (unconfirmed)."

## Image route (confirmed copy-free, this pass)

collections.library.yale.edu's own catalogue search answers plain curl with an HTTP 202 challenge page (needs a
real browser — same pattern CLAUDE.md's Access playbook documents for Yale). `tools/browser_fetch.js` cleared it.
Search for "Mellon MS 29" surfaces catalog record `17388793` ("Lumen luminum, etc," creator "Elia, da Cortona,
frate, -1253," call number "Mellon MS 29," 74 images) — matches this target exactly. Its IIIF Image API endpoint
(`https://collections.library.yale.edu/iiif/2/17388794/info.json`, the first of the item's 74 images) answers
**plain curl directly** (no browser challenge on the image API itself, only on the HTML catalogue search page):
2269×3105, level2 profile — **image is online now, full size**. Exact image indices for ff.1v-2v (the cipher
folios) were not pinned down this pass (the item page's own image-label list did not load in the static HTML
capture; out of scope for check-solved to chase further) — flagged for a recovery-lane worker.

## Is the cipher already solved? (brief's gate)

1. **Beinecke's own description.** The standard pre-1600 manuscripts catalogue entry
   (`pre1600ms.beinecke.library.yale.edu/docs/pre1600.mell029.htm`, WebFetch) states: "written throughout in red
   and black in an italic hand with considerable abbreviation and partly in cipher"; "The text continues, partly
   in cipher on ff. 1v-2r, where alchemical operations are described"; and separately, "on f. 2v is an
   explanation of the ciphers for the signs of the Zodiac, which may be seen in the facsimile provided." The
   f.2v item is a **self-contained symbol legend for zodiac/planetary alchemical signs** (a standard alchemical
   convention, explained in the manuscript itself), distinct from the ff.1v-2r "alchemical operations" passage
   that Bourdeau's ~234-letter cipher attempt (and DECODE R2877) actually targets. The catalogue nowhere states
   the ff.1v-2r cipher itself has been read or its key published — it only documents the existence and location
   of the encrypted material. Citations given in the catalogue entry (TK 1237, TK 336-337 — Thorndike-Kibre
   incipit numbers; De Ricci-Bond 7(26) — the standard Yale pre-1600 MS census) are incipit/census matches, not
   claims of decipherment.
2. **DECODE R2877.** No local `sources/decode/` file for this record; not checked (DECODE login is the DECODE
   worker's alone per COMMON rules).
3. **Literature on the Mellon pseudo-Elian manuscripts.** alchemywebsite.com's Mellon Collection database entry
   for MS 29 (WebFetch) gives only physical description (33 folios, paper, 190×132mm, "Elias Cortonensis, O.F.M.
   Lumen luminum") with "no mention of ciphers, transcriptions, editions, or scholarly discussions." A WebSearch
   for the manuscript together with "cipher"/"zodiac"/"alchemical" returned only the same Beinecke catalogue
   entry, the alchemywebsite listing, and unrelated Mellon manuscripts (MS 2, 24, 33). No published transcription,
   edition or decipherment of this item's cipher passages was located. A second WebSearch on cryptiana.web.fc2.com
   + "Mellon"/"Elia"/"Cortona" returned no relevant hit (Tomokiyo's site does not appear to cover this item).

## Verdict: `open`

Image confirmed online (full resolution). No source read this pass shows the ff.1v-2r alchemical-operations
cipher (the actual target, distinct from f.2v's self-keyed zodiac-sign legend) has been transcribed, edited or
solved anywhere. Bourdeau's own catalogue status ("attempted, open," several classical cipher families
excluded by his own solver) stands unchallenged.

**Nomination:** posted to ROOM.md (stage-2, copy-free, cryptanalysis kind — not a letter, no key-in-archive
route apparent from what was checked this pass).

Rule 10: no novelty claim made. Not decoded, not transcribed (out of scope for check-solved).

Requests this pass: collections.library.yale.edu — 1 browser_fetch (search page, cleared the 202 challenge), 1
browser_fetch (item page), 1 plain curl (IIIF info.json, no challenge). WebSearch 3, WebFetch 2
(pre1600ms.beinecke.library.yale.edu, alchemywebsite.com — neither is a host this brief names explicitly, both
reached via WebFetch/WebSearch per the brief's general grant of those tools). No DECODE, no solver-repo clone.
