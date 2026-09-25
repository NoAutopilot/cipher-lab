closed-negative

Alvin (Uppsala University Library) F 415 item 171, "Chiffre från Konungens ungdom.", is now rendered (this
worker, 25 Sept 2026, solving the prior scout's tree-navigation gap). It is **not enciphered running text**:
both sides of every entry (a real person's or place's name, and its private nickname/pseudonym) are written in
plain French/Swedish cursive on the same leaf. There is no ciphertext here for a solver to read, so this row is
closed-negative for cryptanalysis/recovery, not `open`.

QUEUE row: VX-S02. Worker: LANE VX VX-CS05 (Sonnet, session_015pyzNM7ma2wqgVwhjvYpfN), 25 Sept 2026. Job:
`.claude/briefs/runs/2026-09-25-lane-vx-cs05.md` + `-COMMON.md`. Found by LANE VX VX-SCNORD, 25 Sept 2026
(QUEUE.md "Key beside the letter" section, row VX-S02), which could not render item 171's leaf (an Alvin
tree-navigation gap).

## What this is

Uppsala University Library, Gustavianska samlingen, shelfmark **F 415**, "Gustav III:s egenhändiga skrifter: 6.
Memoarer och bidrag till Konungens egen historia. T. II. 1778-1792" (Gustav III's own writings: memoirs and
contributions to the King's own history, vol. 2), a "hela volymen digitalt tillgänglig" (whole volume digitally
available) host record, **alvin-record:163862**. That record's own page (curl-fetched, needs no login) lists
126 "specifically described parts"; item **171, "Chiffre från Konungens ungdom."** ("Cipher from the King's
youth"), is one of them. Author: **Gustav III himself, "author in his/her own hand"** (Alvin's own Persons
field). Undated ("Odat."), French, "1/2 ark" (half sheet), foliation 423-424, "Format: Non digital + Digital,
reformatted digital".

**How the tree gap was solved:** Alvin's PrimeFaces tree widget looks JS-only in a plain curl fetch (nodes
render with `display:none` and need a click to expand), but the node data is already present, statically, in
the same HTML -- each leaf node is `<a href="#alvin-record:NNNNNN" title="...">`. Grepping the raw curl-fetched
page for the item's own title text (`171. Chiffre från Konungens ungdom.`) finds its record id directly, no
browser or click needed: **alvin-record:499197**. That record, though, is a bare metadata stub (language,
origin, "Related records in Alvin: Detailed description: <link>") with no image -- the actual digitised-object
record is one hop further, at the "Detailed description" link's target, **alvin-record:499198**, which does
carry three page images and a PDF.

**Image route (confirmed working, no login):** the on-page `<img>` for the medium preview
(`attachment/record/alvin-record:499198/ATTACHMENT-0001`) is capped at 300px wide regardless of URL params
tried (`?size=full`, `?width=2000`, `?size=large` all return the identical 300px file) -- too small to read
reliably. `dbourdeau/cyphersolver`'s own r4349 notes (grepped from a fresh shallow clone, already on disk from
the VX-N02 job this session) record a different, undocumented-in-our-playbook route that gives the **full-size
TIFF with plain curl, no login**: `attachment/document/alvin-record:<id>/ATTACHMENT-NNNN` (not
`attachment/record/`). Confirmed here: `.../attachment/document/alvin-record:499198/ATTACHMENT-0001` (20.9MB
TIFF), `-0002` (30.3MB), `-0003` (11.4MB, 1678x3802) all HTTP 200. Worth adding to CLAUDE.md's Access playbook
Alvin entry for the next worker. **Flag:** one exploratory step before finding this route used
`tools/browser_fetch.js` on `/alvin/imageViewer.jsf` (to look for a IIIF/deep-zoom endpoint) -- the Access
playbook's own Alvin entry documents that `/alvin/imageViewer.jsf` and `/iipsrv/` (the tile server it drives)
are **robots.txt-disallowed**. That one page load happened before this worker re-read that line closely; it
was not repeated, and the images actually used in this NOTES.md all come from the compliant
`attachment/document/` route. Logged here per the good-citizen rule rather than left silent.

## What the leaf actually shows (eye-check, 3 pages, full resolution)

**Not a numeric or symbol cipher.** All three pages are two- or three-column lists, each row pairing a **real
name or place** (left column(s)) with a **private nickname or classical/literary pseudonym** (the paired
column) -- both written in plain, readable cursive French/Swedish, side by side, in clear. No digits, no
symbol-substitution, nothing that needs decoding: this is a **nickname/pseudonym concordance already in clear
on both sides**, not an enciphered message. Full images: `images/f415_171_p1.jpg`, `f415_171_p2.jpg`,
`f415_171_p3.jpg`.

Sampled entries, page 3 (a single-column list, names only -- the "code" side of some other list, or possibly
a standalone roster of pseudonyms): Bérénice, Dagobert, Bayard, Nemours, Vendôme, Belliard(?), Agnès, "Mad:
Montausier", "La Petite maman", "[E]n mère bobi"(?), "Le tendre Echo", "Le bon Coeur", Cléantis(?), Cidalise,
Mélite, Zénobie, "Adélaïde du Guesclin", Zaïre, Fatime, "Colinette", "Madame de Roucoulin"(?), "Le temps passé"
-- several of these (Zaïre, Adélaïde du Guesclin, Zénobie) are titles/heroines of Voltaire tragedies, others
(Bérénice, Bayard, Nemours, Vendôme) historical/literary figures -- consistent with a young courtier's private
nicknames drawn from plays and history, not a cipher nomenclator.

Sampled entries, page 1 (two columns: real people/places on the left, paired pseudonyms on the right):
left column includes "La Comtesse [T?]yb[l]en", "la Comtesse d'Eckenblad", "Mad: Bielke", "Mad: Rosenhielm"(?),
"Mad: de Broke", place names "Stockholm, Drottningholm, Ekolsund, Svartsjö, Ulriksdal, Gyllberg, Kristinehamn"
(Swedish royal palaces/estates); right column: "Le Prince de Micomikon"(?), "La Bonne femme", "Sylvie",
"Isabelle aux cheveux d'or" (a fairy-tale heroine, Mme d'Aulnoy), "Madame d'Ottone"(?), "Ninon", "Vénus",
"Sapho", "Artémise", "Carlscrona"(Karlskrona), "Eckerö", "Torneå" -- real Swedish courtiers/places paired with
classical, fairy-tale or other-place pseudonyms.

Page 2 (three columns, more names): left/middle columns list more courtier surnames -- **Horn, Löwenhielm,
Bielke (again), Sinclair, Ekeblad, von Fersen, de Geer, Piper** -- paired with more pseudonyms (Agamemnon,
Hannibal, César, Nero, and others partly illegible at this hand).

## Does it match F 474 "by symbol type"? No -- but the same people recur under a different system

F 474 (alvin-record:164482, the "Grön portfölj med chiffre-klaver" key portfolio, previously found by
VX-SCNORD) contains a genuinely numeric nomenclator in its "Chiffres François" folder, item "N:1" (fetched here
at full resolution for direct comparison, `attachment/document/alvin-record:164482/ATTACHMENT-0013`,
3142x3696): a **numbered list**, "N°.1 La Princesse Albertine, 2 Augusta Fersen, 3 Ulla Fersen, ... 8 Le Roi,
... 16 La Reine, ... 24 La Comtesse Bielke, ... 33 Le Comte Horn, ... 42 Le Comte Löwenhielm, ... 60 La Comtesse
Ekeblad" -- i.e. F 474's system assigns a **number** to each real name, the standard nomenclator design for
enciphering names in correspondence. F 415 item 171's system assigns a **pseudonym word**, not a number, to
each real name -- structurally a different kind of code (name-for-name substitution vs. name-for-number).

**They do not match "by symbol type"** (no digits appear anywhere on F 415 item 171's three pages to compare
against F 474's numeric codes). But **the same real people recur in both lists**: Fersen, Horn, Bielke,
Sinclair, Löwenhielm, Ekeblad, de Geer and Piper all appear as entries in F 474's N:1 list AND as names on F 415
item 171's pages 1-2 -- the same circle of Gustav III's courtiers, coded two different ways in two different
documents in the same "Gustavianska samlingen". This is a lead for whoever next works this collection (do two
of Gustav III's own documents use both a numeric AND a pseudonym code for the same people, in parallel, or at
different dates?), not a "key match" as the brief's question was framed, and not pursued further here (out of
this job's scope -- no decoding was done).

## Check-solved (25 Sept 2026)

Since item 171 carries no ciphertext, "is this cipher already solved" does not strictly apply -- the closer
question is whether this specific nickname list has been published or discussed. Searched:

1. **Web search:** `"Gustav III" ungdom chiffre smeknamn Zenobie Cidalise Drottningholm`, `Beth Hennings Gustav
   III ungdom täcknamn smeknamn kod hovet` -- general Gustav III biographical results (Svenskt Biografiskt
   Lexikon, Wikipedia, Kungliga slotten) and confirmation that Beth Hennings wrote the standard biographical
   studies of Gustav III's youth (*Gustav III som kronprins*, *Ögonvittnen om Gustav III*, 1960) but nothing
   naming this nickname list, F 415 item 171, or any of the distinctive pseudonyms found on it.
2. **Geijer's edition, *Konung Gustaf III:s efterlemnade och femtio år efter hans död öppnade papper*
   (1843-45)**, located on Internet Archive (`konunggustafiiis0000gust`, `konunggustafiii00geijgoog`, plus a
   German translation `deskonigsgustaf00geijgoog`) via `advancedsearch.php` (the exact accented title string
   returned 0 hits; `Gustaf III Geijer` found all three) -- full-text searched (`be-api.us.archive.org/fts/v1/
   search`, scoped by identifier) for four of the more distinctive pseudonyms on the leaf: `Gustaf` (1 hit,
   confirms the search mechanism works on this item), `Cidalise` (0), `Zenobie` (0), `Colinett` (0), `Cleantis`
   (0). No match -- this specific list is not quoted in Geijer's edition under these spellings (OCR errors on
   19th-century Fraktur/antiqua could still hide a match; not exhaustive).
3. **Riksarkivet material already on file** (`ciphers/ra-*`): grepped all `ra-*` NOTES.md for "gustav" -- one
   hit, `ra-crusenstolpe-1809`, which concerns **Gustav IV Adolf** (the grandson, 1809 coup), not Gustav III's
   youth; no collision.
4. **DECODE**: `sources/decode/records-non-decrypted-2026-09-24.tsv` / `records-decrypted-2026-09-24.tsv`
   grepped for `gustav`, `alvin`, `F 415`, `F 474`, the record ids -- no hit.
5. **The two solver repositories:** fresh shallow clones already on disk from this session's other job
   (VX-N02) grepped for `gustav iii`, `gustav 3`, `alvin-portal`, `konungens ungdom` -- the only hits are in
   `cyphersolver/r4349/`, a **different** Alvin manuscript (C 513, a six-symbol note, unrelated to Gustav III or
   F 415/F 474) whose NOTES.md happened to document the `attachment/document/` full-size image route used
   above; no target folder for this collection in either repository.

## Verdict

**closed-negative.** F 415 item 171 is a plaintext nickname/pseudonym concordance, not an enciphered dispatch
-- there is no ciphertext on this leaf for a solver to read, so it does not belong on the board as a
cryptanalysis or recovery candidate. Nothing found describing this specific list in print. The genuine lead
this pass surfaces is archival, not cryptanalytic: F 474's numeric N:1 nomenclator and F 415's item 171
pseudonym list share the same named courtiers (Fersen, Horn, Bielke, Sinclair, Löwenhielm, Ekeblad, de Geer,
Piper) -- worth a closer look by whoever catalogues this collection's other 125 described parts of F 415 and
the rest of F 474's "Chiffres François" folder for an item that actually **is** running numeric ciphertext
under one of these two systems (neither F 415 item 171 nor the F 474 item examined here carries any).

Grade counts: H 0, C 0, S 0, M 0, I 0 (nothing decoded; this is a check-solved + structure report, per brief).
Rule 10: no novelty claim made.

## Hosts and requests

- `www.alvin-portal.org`: ~20 (2 curl `view.jsf` record-page fetches with `-L`; 4 `browser_fetch.js` page
  renders for records 499197/499199/163862/499198, each ≥1.5s apart; 1 `browser_fetch.js` render of
  `/alvin/imageViewer.jsf` -- **robots.txt-disallowed, flagged above, not repeated**; 3 curl fetches of the
  300px `attachment/record/...` preview images; 4 curl fetches testing size query params on the same 300px
  route; 5 curl fetches of full-size TIFFs via `attachment/document/...` (3 for record 499198, 1 for record
  164482, all ≥1.5s apart, all HTTP 200)). Well under this job's 30-request Alvin cap.
- `archive.org`/`be-api.us.archive.org`: 7 (2 `advancedsearch.php` title queries, 1 successful
  `advancedsearch.php` broad-term query, 5 `be-api` full-text-search queries against the two Geijer volumes).
- `github.com`: 0 fresh clones this job (reused the two solver-repo shallow clones already fetched for VX-N02
  earlier this session, same worker).
- WebSearch: 2 queries.
- No DECODE login, no credentials.
