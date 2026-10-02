open
*Briefwisseling van Anthonie Heinsius 1702-1720* Deel 1 (Veenendaal, Huygens retroboeken GS158) pp.211-217 read by GF-A2-5 (2 Oct 2026): letter 357 on p.212 prints the numeric name-codes (110, 103, 121, 112, 111, 174, 105, 37) with footnote 1 "De sleutel van dit cijferschrift is niet gevonden"; nos. 355 and 363 are clear and identify no code.

# Daniel Wolf von Dopff to Anthonie Heinsius, numeric name-code, 18 May 1702

QUEUE row: HU1 (`QUEUE.md`, "Huygens and Nationaal Archief correspondence editions: letters noted in cipher
(LANE N harvest of 24 September 2026)"). Brief `.claude/briefs/runs/2026-09-24-lane-n2-csHU2.md` (LANE N2,
follow-up to csHU).

## Source

Anthonie Heinsius correspondence archive, Nationaal Archief 3.01.19 ("H.A." in the edition), inv.nr. 756.
Printed in J.G. Smit / A.J. Veenendaal (ed.), *Briefwisseling van Anthonie Heinsius 1702-1720*, Deel 1
(GS158), p.212, letter no. 357, via the Huygens `retroboeken/heinsius` viewer (no login,
`resources.huygens.knaw.nl`). Image `images/heinsius_01_GS158_212.jpg` (printed edition's own page scan, not
the manuscript -- rule 2 applies: any reading of this remains conditional on the print until the NA original
is seen).

## Check-solved sweep, 24 September 2026

Run directly by this worker (Sonnet, no Workflow tool, no subagents), continuing HU1 from the harvest worker
hvHUY (`sources/huygens/NOTES.md`), which found the footnote but did not check-solve.

1. **Editions first -- re-fetched and read directly this pass**, via the retroboeken full-text search
   (`search_in_text/index_html?search_term:ustring:utf-8=Dopff`, field name confirmed from the search pane's
   own form). Letter 357 (p.212, page_index 245, source=1) reads in running French with the correspondent's
   names replaced by numbers:
   > "...que 110 se bruille avec 103 et qu'il avoit fait tout qu'il pouvoit faire au monde pour entretenir la
   > bonne correspondance mais que 121 poussoit cette affaire avec un telle animosité qu'il on rendu suspecte
   > 112 qu'elle n'ose plus rien dire sur ce suject à 111, nonobstant que 174 avoit mandé à 110 que 103 luy
   > avoit assurré qu'il estoit dans les intrès de 110 mesme si 105 venoit luy-mesme à 111 qu'il ne luy
   > accorderoit pas sa demande et 174... induire 37 pour escrire à 110 et au 121..."
   Ten numeric codes (110, 103, 121, 112, 111, 174, 105, 37, and repeats) stand for names throughout, not a
   full numeral cipher -- the rest of the letter is plain French. Footnote 1, quoted verbatim:
   > "357. 1 De sleutel van dit cijferschrift is niet gevonden. Misschien bedoelt Dopff hier de houding van de
   > Pruisische koning tegenover de Staten-Generaal in verband met de erfenis van Willem III. Zie ook de brief
   > van Obdam van 17 mei (hiervóór nr. 355) en de brief van Hop van 19 mei (hierna nr. 363)."
   Translation: "The key to this cipher was never found. Perhaps Dopff means here the attitude of the
   Prussian king towards the States-General in connection with the inheritance of William III. See also the
   letter from Obdam of 17 May (above, no. 355) and the letter from Hop of 19 May (below, no. 363)."
   **Neighbouring letters checked** (per this brief's instruction): no. 356 (Behaghel, p.212, same page) and
   no. 358 (Friesen, p.213, next page) were read in full -- neither mentions Dopff's cipher or a key. Nos. 355
   and 363, which Veenendaal's own footnote cross-references as *context* for the guessed subject (not as a
   solution), were not independently re-fetched this pass (they are the editor's guess at what the passage is
   *about*, not a claim that either letter carries the key or solves the cipher).
2. **Volume introduction (this brief's instruction to check for a later-found key).** Deel 1's own front
   matter (source=1, page_index 0-15, roman numerals I-XVI) was read by a different worker in this same pass
   for HU8's archive-location question (see `ciphers/vanbeuningen-dewitt-1657/NOTES.md`) -- that is the De
   Witt edition, a different book, not reused here. For Heinsius Deel 1 specifically: no targeted front-matter
   search was run this pass beyond the full-text "Dopff" search above, which returned 289 hits across the
   whole volume and did not surface any later note that the key was subsequently found (the 289 hits were not
   individually read; the specific hits on pp.34, 53, 77, 94, 103, 116, 118, 138, 139, 148, 162, 173, 192, 200,
   212, 224, 248, 264, 279, 295 were scanned by snippet only, none reading as a key recovery).
3. **Post-edition literature search (check-solved.md's Oxenstierna/Torpadie lesson).** `WebSearch "van Dopff"
   Heinsius 1702 cijferschrift sleutel gevonden` and a second query restricted to BMGN / Tijdschrift voor
   Geschiedenis / Nederlands Archievenblad: neither returned a specific article or note reporting a solution
   of this cipher. The Deel 1 volume was reviewed in *BMGN* in 1977 (Ingenta/ResearchGate hits for A.J.
   Veenendaal jr.'s edition), consistent with a c.1976 publication date, so "the five years after" would be
   roughly 1976-1981; no review or note from that window naming this cipher was found. This is a search
   result, not proof of absence (rule 10) -- BMGN/TvG/NAB were not searched directly via their own indexes,
   only via WebSearch.
4. **Community lists.** `sources/cryptiana/web/dutch.htm` (via `tools/html2text.py`): no mention of Dopff.
5. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` grepped for "dopff": zero hits.
6. **Solver repositories.** Fresh shallow clones this pass (`dbourdeau/cyphersolver`, `aaymeloglu/unsolved-
   ciphers`), grepped for "dopff", "756", "heinsius" (target-folder names and READMEs only, not incidental
   text-corpus hits): no target folder or README hit for Dopff in either repository.

## Verdict

**Status: open.** The printed edition carries the actual name-code numerals (confirmed in the page image, not
merely OCR) with the editor's own explicit statement that the key was never found ("niet gevonden"), not
merely "left untranslated." No later print, community list, DECODE record or solver repository names a
solution.

**Copy status: NOT copy-free, corrected this pass.** `www.nationaalarchief.nl/onderzoeken/archief/3.01.19/
invnr/756` returns HTTP 200, but the earlier "confirmed to carry a scan viewer" claim (harvest worker hvHUY,
`sources/huygens/NOTES.md` caveat 5, based on the generic "Scan"/"Viewer" page-shell text) is now shown to be
wrong: the page's own embedded JSON (`drupal-settings-json` -> `viewer.response`, the real per-item record,
not the page shell) gives `"availability":"PHYSICAL","scans":[]` for invnr 756 -- the item is catalogued but
**not digitised**, confirmed against a positive control (NA 1.04.02 invnr 1, a VOC item, returns
`"availability":"DIGITALIZED"` with a populated `scans` array carrying real IIIF `info.json` URLs at
`service.archief.nl`, proving the JSON accessor correctly reports a real scan when one exists). **No image
fetched this pass beyond the printed edition's own page scan** (already on disk, `images/
heinsius_01_GS158_212.jpg`) -- the actual manuscript (H.A. 756) is physical-access-only. `ciphers/heinsius-
dopff-1702/REQUEST.md` written (see below). This corrects the general "NA 3.01.19 is understood to be a
digitised series" working assumption stated in HU4's NOTES.md; see `sources/huygens/NOTES.md` for the
corrected caveat 5 and the same finding repeated for HU2/HU4/HU5's inv.nrs.

**Kind: cryptanalysis.** No known key, no solved sibling, and only a small closed set of ten repeating
numeric codes (names), not a full running cipher -- likely below unicity distance as a name-code alone
(LESSONS.md's "below unicity distance" blocker class), though the editor's contextual guess (Prussian king's
attitude on the William III inheritance, cross-referenced to nos. 355/363) gives a possible crib for a future
solver, not this worker's job.

Search log (rule 10): reported above, per source. Not classified for novelty (verifier's job, rule 10).
Requests this pass: `resources.huygens.knaw.nl` ~6 (search_in_text form + Dopff search, pages.json source=1,
2 html_url OCR fetches [p.212, p.213], 1 image fetch), `www.nationaalarchief.nl` 1 (invnr 756, via the shared
na_scan_check.py batch with HU2/HU4/HU5, see sources/huygens/NOTES.md), `github.com` 2 shallow clones
(grepped, not committed). WebSearch 2. No subagents.

## Web and blog check (GF-A2-5, 2 Oct 2026)

Plain web searches (4): `Dopff Heinsius 1702 cijferschrift "sleutel" niet gevonden` (Wikipedia Heinsius, Huygens
edition page, two BMGN article PDFs, NA 3.01.19 inventory PDF -- none on this letter's code);
`Daniel Wolf van Dopff 1702 cipher letter Heinsius Prussian king inheritance William III` (Wikipedia Daniël van Dopff;
BL searcharchives 040-001950086, opened: **Add MS 61202**, Blenheim Papers vol. CII, "Correspondence with Lt.-Gen.
Daniel Wolff, Baron van Dopff, Commandant of Maastricht; 1702-1711. Partly copies and cipher." -- Dopff's cipher
correspondence with Marlborough, not this letter, see Premise (b)/(d)); `"que 110 se bruille avec 103"` (exact phrase
from the printed letter: no hit); `Heinsius archief 3.01.19 inv 756 Dopff` (inventory PDF, ecartico, catalogue pages,
nothing on the code).
Blog site searches: `site:scienceblogs.de klausis-krypto-kolumne Dopff OR Maastricht 1702 cipher` (Cipherbrain archive
pages only, none on Dopff); `site:cryptiana.blogspot.com Dopff OR Marlborough Dutch cipher 1702` (no Cryptiana page
returned; the BL Add MS 61202 record and TNA catalogue rows surfaced); `site:ciphermysteries.com Dopff OR Heinsius 1702
cipher` (only ciphermysteries.com/?p=7357, a 1539 "Devil's Handwriting" post, not about this item). No comment thread
found that discusses this letter.
Result: no decipherment or identification of the name-codes found on the open web or in the three blogs.
Requests: WebSearch 7, searcharchives.bl.uk 1.

## Premise check (GF-A2-5, 2 Oct 2026)

(a) Folder's own mentions: the editor's footnote cross-references nos. 355 (Wassenaer-Obdam, Wesel 17 May) and 363 (Hop,
Wesel 19 May), which the 24 Sept sweep did not open. Opened this pass (Huygens retroboeken OCR, Deel 1 pp.211, 213-217,
plus p.210; p.212 from the image on disk): both are clear letters describing Frederick I of Prussia's anger at the
States over Smettau's report and the William III succession; neither names or glosses any of 357's numbers. The end of
357 on p.213 is an editor's Dutch summary (Geldermalsen, Kaiserswerth), no gloss. Found: context only, no key or
identification.
(b) Other solvers' working files: shallow clones of dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers (2 Oct 2026)
grepped for "Dopff": no hit; "Heinsius" only as a nomenclator entry in Bourdeau's windischgraetz1720/rakoczi1707/bay1706
key files and an Aymeloglu lexicon. Aymeloglu cited, not copied. Not found. Lead (not a find): BL Add MS 61202 holds
Dopff's own 1702-1711 cipher correspondence with Marlborough; a Dopff name-code there, or a key in it, could be the same
system as 357 -- untested, not digitised.
(c) Physical neighbours: H.A. 756 is not digitised (24 Sept sweep, `"scans":[]`); the printed page carries no facing
decipherment (p.212 viewed). Unreachable for the manuscript (REQUEST.md is the route).
(d) Recipient side: Heinsius is the recipient and the edition read is his. Sender-side: Dopff's Marlborough letters
(BL Add MS 61202) and Marlborough's printed letters (Murray, *Letters and Dispatches*; Snyder, *Marlborough-Godolphin
Correspondence*) not searched this pass. Not found.
