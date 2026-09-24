open

# Willem van Oranje to Günther van Schwarzburg, cipher letter, 2 May 1561

QUEUE row: WV3 (`QUEUE.md`, "Willem van Oranje correspondence: unsolved cipher letters (LANE N harvest of 24
September 2026)"). Brief `.claude/briefs/runs/2026-09-24-lane-n-csWV.md`.

## Source

WVO briefnr **8246** (https://resources.huygens.knaw.nl/wvo/app/brief?nr=8246), date editorially assigned to
2 May 1561 from Japikse's edition (the letter itself carries no date), from Willem van Oranje to Günther XLI van
Schwarzburg-Arnstadt (1529-1583), his brother-in-law (Günther married Willem's sister Catharina van Nassau,
engaged from c.1558) and close friend -- the correspondence is described in scholarship as unusually personal
(WebSearch, ResearchGate summary of "Correspondentie totaal. Patronen en trends in de briefwisseling van Willem
van Oranje"). Content per WVO: report on progress of the marriage plan between King Frederik II of Denmark and
Renata van Lotharingen. Free PDF, no login:
`resources.huygens.knaw.nl/media/wvo/images/08000-08999/08246.pdf`.

WVO's Opmerkingen field, read directly this pass: "Grotendeels in cijfer. Zonder jaartal, wat is ontleend aan
Japikse, Correspondentie Willem den Eerste." (Mostly in cipher. Without a year, which is derived from Japikse,
Correspondentie Willem den Eerste.) No oplossing/opgelost/ontcijferd word. Bron: Japikse, N., ed.
*Correspondentie van Willem den Eerste, prins van Oranje*, Eerste deel (1551-1561) ('s-Gravenhage 1934).

**Japikse's edition, actually read this pass** (via `tools/browser_fetch.js` driving the Huygens retroboeken
viewer -- a legacy dojo-based page-image app with no plain image URL, worked around with its own `Zoek`
full-text-search endpoint, `search_in_text/index_html?search_term:ustring:utf-8=Schwarzburg`, paginated with
`batch_start:int=N`, to locate the letter's exact page in the edition's own "Chronologische lijst" index rather
than guessing): the index (viewer page image, printed p.385) gives **"1561 Mei 2 Aan Günther, graaf van
Schwarzburg . . . 343"** -- letter no. **316**, printed pp.343-344 (`images/japikse_p343.png`,
`images/japikse_p344.png`). Footnote 1 on p.343 cites the source: "S.A. Sondershausen. -- Uit Brussel. --
Zonder jaartal, dat echter niet dubieus is." (Staatsarchiv Sondershausen -- from Brussels -- undated, but the
date is not in doubt) -- **the same shelfmark as our manuscript image's own archive stamp** ("Staatsarchiv
Rudolstadt, Kanzlei Sondershausen 693 o.s."), confirming this is the same letter, not a different one on the
same date.

**Critical finding: Japikse's printed text is the letter's clear opening only, and it stops before any cipher.**
The printed German text (`Wolgeborner freundtlicher lieber Schwager und Bruder, Ich hab Pauln von Sahra kurtz
nach einander zwei schreiben...`) matches **verbatim** the clear opening paragraph visible on
`images/08246_p1.png`, confirming both are the same document. Japikse's print continues in clear German for
about a page and a quarter and ends cleanly at "...unserr freundtlicher lieber frau mutter und brudern und
schwestern viel gutter nacht und alles guts zu wünschen ----" (a normal letter close), after which Japikse's
own italicized editorial narrative moves on to a **different** letter (28 August). None of the letter's three
footnotes mentions a cipher, a lacuna, or an omission. But the manuscript image (`08246_p1.png`) shows this
same clear opening occupying only the top third to half of page 1 of a 3-page PDF, with the remainder of page 1
already in cipher (the "ps f 33 m..." nomenclator block) -- and WVO's own Opmerkingen calls the letter
"**grotendeels**" (mostly) in cipher, which the clear portion alone does not account for. **Japikse's 1934
edition therefore prints only the clear preamble and silently stops before the ciphered bulk of the letter**,
the same "prints the envelope, omits the cipher" pattern already documented for the Groen van Prinsterer volumes
covering WV1/WV2/WV4 in this batch. This is now a directly confirmed reading of the named edition, not an
inference from curatorial silence (rule 10 / M9 lesson satisfied for this target).

**Confirmed by eye this pass** (`images/08246_p1.png`): the manuscript (archive stamp reads "Staatsarchiv
Rudolstadt, Kanzlei Sondershausen 693 o.s. (na f. 26)") opens in clear German prose ("Mein freundtlich dienst
mit vermuege alles lieb vnd guten [...] Hochgeborner freundtlicher lieber Schwager vnd Bruder...") and then
switches into a cipher of German-nomenclator type distinct from the French numeral ciphers seen elsewhere in
this correspondence: doubled and tripled letters (aa, cc, dd, hs, xr, aaa) mixed with two-digit numbers (e.g.
"ps f 33 m [overline-o] xr [overline-x] [theta] f 00 aa r 34 88 x p 22 77 34 60..."), running for most of a
full page. Genuine cipher confirmed present.

**Solved sibling in the same circle.** WVO briefnr **5109** (https://resources.huygens.knaw.nl/wvo/app/brief?nr=5109),
also Willem to Günther van Schwarzburg, from Brussel, undated in the record but placed "24 Mar 1561" by the
QUEUE.md harvest row -- fetched and read directly this pass. Opmerkingen: "**Gedeeltelijk in cijferschrift, de
editie met oplossing.** De minuut is op 22 maart gedateerd en wijkt af van het eigenhandige origineel." (Partly
in cipher, **the edition carries the solution**. The draft is dated 22 March and differs from the autograph
original.) Content: news that Filips van Hessen still refuses his planned marriage but August van Saksen holds
to his promise, and that Willem will send Lodewijk van Nassau to August van Saksen to negotiate further. Bron:
same Japikse edition, page 261. This is a direct, explicit contrast within the same correspondence pair: the
Japikse edition prints a solution for 5109 (per WVO's own remarks) but 8246's remarks carry no such note --
the same "solved for some letters, silent for others in the same run" pattern already documented for the Groen
van Prinsterer editions covering WV1/WV2/WV4.

## Check-solved sweep, 24 September 2026

Run directly by this worker (Sonnet, no Workflow tool, no subagents), shared clones/searches with WV1/WV2/WV4
(see those NOTES.md files for the same solver-repo and DECODE sweep, not repeated verbatim here).

1. **Edition named in WVO's own record -- read directly this pass (see Source above).** Japikse's 1934 edition,
   letter no. 316, pp.343-344: confirmed to print only the clear opening of this exact letter (same shelfmark,
   verbatim-matching text) and to stop before the ciphered majority of it, with no footnote acknowledging a
   cipher passage at all. This resolves the M9-lesson requirement (quote verbatim what a named source says
   about this letter) for the target itself. The solved sibling 5109's citation (Japikse p.261, "de editie met
   oplossing") was not independently re-read this pass -- WVO's own remarks are trusted for that letter, since
   it is being used only as a possible key-recovery sibling, not as the basis for this target's own verdict.
2. **Community lists.** `sources/cryptiana/web/dutch.htm`: no mention of Günther van Schwarzburg or Willem's
   1561 correspondence specifically (the page does discuss Marnix as decipherer from 1576 onward, a later and
   unrelated period). WebSearch (`Günther von Schwarzburg Willem van Oranje 1561 chiffre Japikse Correspondentie`)
   found only general biographical material on the Günther-Catharina engagement and confirmed the Japikse
   edition's existence and 1934 publication, nothing specific to this letter's cipher status.
3. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` grepped for schwarzburg/nassau/oranje/
   willem: zero hits.
4. **Solver repositories.** Shared clone/grep (see WV1 NOTES.md item 5): zero hits for schwarzburg or this
   correspondence in either repository.
5. **General web search.** As item 2.

## Verdict

**Status: open, directly confirmed.** The named edition (Japikse 1934, letter 316, pp.343-344) was located and
read in full this pass: it prints only the letter's clear opening (already unremarkable, matching what the
manuscript itself shows in clear) and stops before the ciphered majority of the letter, with no footnote
acknowledging a cipher or an omission. WVO's own curatorial silence (no solution word, in direct contrast to
the same-pair sibling 5109 which the same database marks as solved) is corroborating evidence, and no community
list, DECODE record or solver repository names a decipherment of the ciphered portion. This is a page-checked
verdict, not an inference from silence alone.

**Copy status: copy-free.** Free PDF confirmed reachable and viewed by eye. No REQUEST.md needed.

**Kind: recovery** (5109, same correspondence pair, "de editie met oplossing" -- an alignment target once
Japikse p.261's solution is transcribed, per LESSONS.md §2, not cryptanalysis from scratch; the two systems'
similarity is not yet confirmed since 8246 was only viewed, not compared token-by-token to 5109).

**Next step (not this brief's scope):** get Japikse p.261 (5109's solution) and p.374 (8246 itself) read --
either via a working route into the retroboeken viewer or by locating the Japikse volume itself on Internet
Archive/HathiTrust/a library scan -- before any solving or promotion.

## C1: capture and inventory (LANE R2, 24 September 2026)

Per `.claude/briefs/runs/2026-09-24-lane-r2-capture-huygens.md`. Fetched 8246 in full (3 pages, was only p1
before), 5109 in full (9 pages), and Japikse edition pages 229-234 via the retroboeken viewer. `images/manifest.json`
updated, `images/inventory.tsv` written per page. Capture and inventory only -- no decoding, no alignment, no
novelty classification.

**Major finding: 5109's cipher is a single page, and its own WVO PDF already contains the printed plaintext.**
Fetching 5109 (the "de editie met oplossing" sibling) in full shows its cipher is confined to **page 6 only**
(pages 1-5 and the letter's close are all clear German prose). Reading it against the printed edition (fetched
independently this pass via the Huygens retroboeken viewer, see route note below, before noticing it was already
sitting in 5109's own PDF) shows:

- **Page 6's ciphertext** ("d tf hs tr 87 86 88 ii...") uses the same repertoire as target 8246's cipher: doubled
  letters, 2-3 digit numbers, occasional symbols.
- **5109 pages 7-9 are a scan of Japikse pp.231-233**, i.e. the printed edition's plaintext is bundled directly
  into the manuscript's own WVO PDF, immediately after the cipher page -- the same "printed edition scanned into
  the manuscript file" pattern independently found this pass in `ciphers/jan-van-nassau-1572-75/` (see that
  folder's NOTES.md 'C1' section) for letters 5218 and 5222.
- **Japikse p.232 carries an explicit editorial footnote** immediately before the relevant passage (printed there
  in spaced-out type, the edition's convention for a passage restored from a source other than the plain
  manuscript text): *"Het nu volgende ontbreekt in de minuut en is dus door den Prins zelf in cijferschrift
  ingelascht"* -- "the following is missing from the draft/minute and was thus inserted in cipher by the Prince
  himself." The spaced-out plaintext runs from "Der v(on) Egmont hat mich gefragt, ob Euer Liebe von
  S(ondershausen) eher nach Lothringen ziehen verden..." through to "...das nichtz gegenwider den König
  gehandelt werde." on p.233, then reverts to normal type and closes the letter in the clear.
- This is therefore a **complete, ready-made alignment pair**: `images/05109_p6.jpg` (ciphertext) against
  `images/05109_p8.jpg`+`05109_p9.jpg` / `japikse_p232.jpg`+`japikse_p233.jpg` (its own printed plaintext,
  editorially confirmed as the cipher's content) -- unblocked for a future alignment worker. This pass did not
  attempt the alignment or build a key (out of brief scope).
- Confirmed the letter's identity by content, independent of WVO's own citation: WVO's Bron field for 5109 gives
  "Japikse p.261" (an index or different-edition page number not matched by this pass), but the printed heading
  actually reads **"236. Aan Günther, graaf van Schwarzburg. 24 Maart 1561"** at printed page 230, and footnote 4
  there reads *"S.A. Sondershausen; de minuut (K.H.A. 2123) is 22 en 23 Maart gedateerd. -- Uit Brussel"* --
  matching WVO's own Opmerkingen for 5109 ("de minuut is op 22 maart gedateerd") word for word. The "p.261"
  citation is unresolved (possibly a different Japikse volume/printing, or a typo for "231"); not chased further
  this pass.

**Retroboeken viewer route (for the record, since a working route was previously unknown -- see route note in
`images/manifest.json`):** the WVO record HTML for a solved sibling links straight to the viewer with an internal
page index (`#page=261...`), not the printed page number. The viewer itself is a Dojo single-page app with no
static image URL in its HTML, but its `book_data.js` names a `pages.json` endpoint; fetching
`<base_url>/pages.json?source=1` returns a JSON array of `{page_index, source, number, image_url, html_url}` per
page, and `image_url` is a plain, unauthenticated `.jpg`. This is a faster, cheaper route than the previous
worker's `browser_fetch.js` + full-text-search approach for any future Japikse page fetch, and should generalise
to any other Huygens retroboeken-hosted edition (same `book_scripts.js`/`pages.json` pattern expected).

**Design comparison for the alignment step (not attempted here):** 8246's cipher (pp.1-3, dense throughout) and
5109's single cipher page use the same character repertoire (doubled letters aa/cc/dd/hs/xr, 2-3 digit numbers,
occasional overline diacritics), consistent with the same nomenclator system two months apart in the same
correspondence -- exactly the "kind: recovery" classification already in this file's Verdict section, now with a
concrete plaintext-ciphertext pair on disk to build the key from.

Host: resources.huygens.knaw.nl, ~17 requests this pass (2 PDF fetches + ~1 WVO record HTML + ~1 book_data.js +
1 pages.json + ~6 Japikse page images + retries, all >=1.5s apart, descriptive UA), shared budget with the other
two C1 targets.
