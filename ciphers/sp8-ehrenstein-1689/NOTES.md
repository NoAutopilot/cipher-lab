open
CSP Domestic William and Mary vol. 1 (Feb 1689-Apr 1690; archive.org calendarofstatep01grea_2, djvu full text) grepped by this worker 2 Oct 2026: the item is calendared at p. 387 ("Major d'Ehrenstein to Mons. de Bernsdorff, touching Mons. de Guldenstolp. [S.P. Dom. King William's Chest 6,] No. 68"), a one-line description only, no text or decipherment printed.

# Major d'Ehrenstein to M. de Bernsdorff re M. de Guldenstolp, partly in cypher — TNA SP 8/6/65

QUEUE row: N61 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

The National Archives, Kew, **SP 8/6/65** (item 65, described in the record as folio 208), [1689] (TNA
Discovery, fetched 24 Sept 2026, id C18727349; `digitised: false` confirmed by direct record fetch; no separate
`note` field). Scope content: "Folio 208. Letter from Major d'Ehrenstein to Monsiuer de Bernsdorff regarding
Monsieur de Guldenstolp partly in cypher." SP 8 is **"King William's Chest"** — William III's own papers as
Prince of Orange and King, 1670-1698; TNA's own research guide states the series is "nearly all calendared" in
the printed CSP Domestic for Charles II, James II, and William and Mary. 1689 is the first year of William's
reign and the start of his continental resistance to Louis XIV (Nine Years' War), consistent with correspondence
about raising or coordinating German/Scandinavian military contacts. "Bernsdorff" and "Guldenstolp" plausibly
render Bernstorff (a prominent Hanoverian/Danish noble family) and Gyldenstolpe (a Swedish diplomatic family;
Nils Gyldenstolpe was Swedish envoy to the Hague through the 1680s-90s) — web-searched but not confirmed as the
specific individuals in this letter.

## Check-solved sweep (24 September 2026)

1. **Editions.** TNA's own guide (`nationalarchives.gov.uk`, State Papers Domestic 1660-1714 research guide,
   confirmed by WebSearch 24 Sept 2026) states SP 8 is nearly all calendared in *Calendar of State Papers
   Domestic, William and Mary*, ed. Hardy and Bateson, 11 vols (1895-1937). Vol. 1 (13 Feb 1689-Apr 1690, the
   window that contains this item) was fetched in full text from archive.org (`calendarofstatep02grea_1`) and
   [Correction, GF-A2-6, 2 Oct 2026: the identifier `calendarofstatep02grea_1` is vol. 2 (1 May 1690-Oct 1691, its own
   preface), not vol. 1; vol. 1 is `calendarofstatep01grea_2` and calendars this item at p. 387 -- see the Premise check
   below. The zero-hit sentence that follows is true of vol. 2 only.]
   grepped for "Ehrenstein," "Bernsdorff"/"Bernstorff," and "Guldenstolp"/"Gyldenstolpe": **zero hits** for all
   variants. TNA's phrasing is "nearly all," not "all," and period German/Scandinavian names are OCR-fragile, so
   this is a real check with a real caveat, not a full clearance — but it is the standard calendar for this
   series and comes back negative for every named party by direct full-text search.
2. **Sibling search (TNA Discovery, same piece).** `tools/discovery_items.py "SP 8" "SP 8/6" decipher` and
   `... Ehrenstein` return **only the target record itself** — no companion key, decipher, or duplicate found in
   SP 8/6 under those terms.
3. **Community lists.** WebSearch (`Bernstorff Gyldenstolpe Ehrenstein 1689 diplomatic correspondence Denmark
   Sweden William III`) returned only unrelated later Bernstorffs (18th-19th century diplomats) and a
   Gyldenstolpe-family biography (EMLO correspondence catalogue) with no tie to this letter or the year 1689.
   No Cryptiana or Cipherbrain hit; local grep of `sources/cryptiana/` for "ehrenstein"/"bernsdorff"/
   "bernstorff"/"guldenstolp": no hits.
4. **DECODE.** No login attempted. `sources/decode/` greped for "Ehrenstein"/"Bernsdorff"/"Bernstorff"/
   "Guldenstolp"/"SP 8/6": no hits.
5. **Solver repositories.** Both freshly shallow-cloned (24 Sept 2026, shared across this pass's four targets).
   `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers`: grep for "ehrenstein|bernsdorff|bernstorff|
   guldenstolp|SP.?8.?6" across both trees: zero matches.
6. **General web search.** As (1) and (3). No result ties a decipherment, key, or prior reading to SP 8/6/65
   specifically, nor definitively identifies "d'Ehrenstein," "de Bernsdorff," or "de Guldenstolp" as the exact
   individuals in this letter (only plausible family-name matches for the period and milieu).

**Host requests this pass:** discovery.nationalarchives.gov.uk 3 (search x2, record detail x1, >=3s apart,
shared budget with the other three targets this run), archive.org 2 (metadata + full-text fetch of CSP Domestic
William and Mary vol. 1), WebSearch 2, github.com 1 shallow clone each of both repos (grepped, shared across all
four targets), sources/decode/ and sources/cryptiana/ local greps (no network).

## Verdict

**Status: open.** The standard calendar for this series (CSP Domestic William and Mary vol. 1, which covers this
exact date window) was fetched in full text and searched for every named party in the catalogue description,
with no hit — a real check, though "nearly all calendared" (TNA's own wording) and OCR fragility on foreign
names keep this a caveat rather than a certainty. No sibling key or decipher found in the same TNA piece; no
community list, DECODE record, or solver-repository entry names this item or any of its three named
correspondents.

**Copy status:** no online image located; `digitised: false` confirmed by direct record fetch (id C18727349).
**Copy-order.** See REQUEST.md.

**Recommended next steps (not run this pass):** (1) a full page-by-page read of CSP Domestic William and Mary
vol. 1 (rather than a name-string grep alone) to rule out an OCR-garbled entry; [Done, GAPS111, 3 Oct 2026: the entry is found at p. 387 and the OCR-fuzzy sweep adds nothing; see the GAPS111 section below.] (2) [Done as probable identifications, GAPS114, 3 Oct 2026; see the GAPS114 section.] identify the specific
"d'Ehrenstein," "de Bernsdorff," and "de Guldenstolp" via Scandinavian/Hanoverian prosopography (SSNE database,
per LESSONS.md precedent) before any solve attempt, since a firm identification would open a proper printed-
correspondence search for any of the three; (3) check whether SP 8's neighbouring volumes/pieces (SP 8/1-5,
8/7+) hold a general cipher key for William III's continental correspondents — not searched this pass.

queued JSTOR rows, 26 Sept 2026, QUEUE-FILL.

## JSTOR runner, 26 Sept 2026

- `"Ehrenstein" AND "Bernsdorff" AND 1689 AND cypher`: no relevant hit (0 results, none about the letter).
- `"Guldenstolp" AND "Ehrenstein"`: no relevant hit (0 results, none about the letter).

## Web and blog check (GF-A2-6, 2 Oct 2026)

Plain web searches (WebSearch, 2 Oct 2026):
1. `Ehrenstein Bernstorff Gyldenstolpe 1689 letter cipher` -- Tartu/HistoCrypt papers (Fredenburgh Suriname ciphertext 1689; Heusner von Wandersleben 1637), SNL "Bernstorff", Archives cantonales vaudoises record for Andreas Gottlieb von Bernstorff (1649-1726), Britannica 1911 "Cryptography". None about this letter.
2. `"SP 8/6" cypher King William's Chest` -- TNA series record C13550 and SP 8/6 item records (C18727312, -316, -323, -363, -367, -389); the snippet mentioning "some lines of cypher ... Henning will be able to decipher these lines" is a different SP 8 item (calendared in CSP Dom W&M vol. 2, King William's Chest No. 23), not this one.
3. `"Major d'Ehrenstein"` (the catalogue's own wording in quotes) -- only Albert Ehrenstein (1886-1950, poet) and unrelated pages; no 1689 officer.
4. `"Ehrenstein" "Bernsdorff" "Guldenstolp"` -- unrelated Ehrenstein/Bernstorff genealogy and heraldry pages.

Blog site searches:
- Cipherbrain (scienceblogs.de), `Ehrenstein Bernstorff cypher 1689`: only unrelated posts (musical cryptogram 17th c., La Buse, Ferdinand III, Blitz ciphers); none mentions this letter.
- Cryptiana (cryptiana.blogspot.com, cryptiana.web.fc2.com), `Bernstorff Gyldenstolpe cipher 1689`: no results.
- Cipher Mysteries (ciphermysteries.com), `Ehrenstein Bernstorff cipher William III`: only Zodiac, Voynich, Blitz, Milanese letters posts.
No plausible hit for this item, so no comment thread bears on it.

Not found: no decipherment, plaintext or prior attempt for SP 8/6/65 on the open web or in the three blogs.

## Premise check (GF-A2-6, 2 Oct 2026)

(a) Decipherments the folder already mentions: none for this item. The 24 Sept sweep's edition check had searched the wrong volume (see the correction inside it): CSP Domestic William and Mary vol. 1 (`calendarofstatep01grea_2`, preface: 13 Feb 1689 to the close of April 1690) calendars the letter at p. 387 as "Major d'Ehrenstein to Mons. de Bernsdorff, touching Mons. de Guldenstolp. [Ibid., No. 68.]", in a run of King William's Chest 6 entries (No. 66 ends "[S.P. Dom. King William's Chest, 6, No. 66.]"). The calendar prints only that one line: no extract, no "in cypher" note and no decipherment. Index entries "D'Ehrenstein, Major, 387" and "De Guldenstolp, Mons., 387" only. The calendar's No. 68 differs from TNA's item number 65 (folio 208); the description is the same, so it is the same letter under a renumbering. Found: calendar entry (description only); not found: plaintext or decipherment.
(b) Other solvers' working files: fresh shallow clones (2 Oct 2026) grepped for `ehrenstein|bernsdorff|bernstorff|guldenstolp|gyldenstolp`: aaymeloglu/unsolved-ciphers none (cited, not copied); dbourdeau/cyphersolver only `targets/windischgraetz1720/` (key5017 nomenclator code 432 and key5018 code 53 = "Bernsdorff"), an Imperial key of 1720 naming the same family -- a different sender, office and date, not run on this letter and not evidence for its key. Not found for this item.
(c) Physical neighbours: no image online (`digitised: false`) -- leaves, facing page and slips unreachable. Calendar neighbours on p. 387 (King William's Chest 6, Nos. 66-74): an artillery report from Ireland, a description of the Emperor's generals, a Breda fortifications project, Waldeck to Heinsius (copy), a Galicia salt-farm memorandum, Castanaga's army, the Duke of Brunswick-Lüneburg to the King, winter-quarter proposals. None is a key, decipherment or clear copy of No. 68. Not found.
(d) Recipient side: Bernsdorff is most plausibly Andreas Gottlieb von Bernstorff (1649-1726), then minister at Celle (identification not confirmed). No printed edition of his 1689 correspondence was located in the web searches above; the Hanover archive (NLA Hannover) holds the Celle side and was not searched this pass. Separately, vol. 1 shows Dr John Wallis deciphering intercepted French letters for Nottingham in 1689 (pp. 363-364, De Bethune and De Gravel to de Croissy); Wallis's decipherment volumes were not searched for this letter. Not found in what was read; Celle-side and Wallis-side unsearched.

## GAPS111 (3 Oct 2026, account-4): CSP Dom. William and Mary full-text grep

Step run: "Recommended next steps" (1), by script, not by a model reading the volume (Usage 2). Full text fetched once
from Internet Archive: vol. 1 `calendarofstatep01grea_2_djvu.txt` (2.40 M chars; 13 Feb 1689 - Apr 1690) and, as a
check for any later mention, vol. 2 `calendarofstatep02grea_1_djvu.txt` (2.35 M chars). Script: `csp_grep.py` in this
folder (name regexes, an OCR-fuzzy token sweep at edit distance <= 2 with f/s, c/e, y/i folded, King William's Chest 6
references, cipher words within 400 characters of any name; exits 2 if the positive control is missed).

Positive control: the same regex method finds the p. 387 neighbour "The Prince of Waldeck to Pensionary Heinsius"
(No. 70 in the calendar run, 1 hit in vol. 1) and "Castanaga" (27 hits in vol. 1, 30 in vol. 2). Control passed.

| Search (vol. 1) | Hits | What they are |
|---|---|---|
| Ehrenstein regex | 2 | p. 387 entry "Major d'Ehrenstein to Mons. de Bernsdorff, touching Mons. de Guldenstolp. [Ibid., No. 68.]"; index "D'Ehrenstein, Major, 387" |
| Bernsdorff regex + fuzzy | 1 + 2 | the p. 387 entry; index "De Bernsdoff, Mons., 387" (OCR or print spelling); "Ebersdorff, letters dated at" (unrelated place) |
| Guldenstolp regex | 2 | p. 387 entry; index "De Guldenstolp, Mons., 387" |
| Ehrenstein / Guldenstolp fuzzy (beyond regex) | 0 | -- |
| King William's Chest 6 references | 66 | the run containing No. 68 |
| cipher/cypher/decipher within 400 chars of a name | 0 | -- |
| cipher words in the volume | 26 | editorial rules, Wallis decipherments of French and Polish letters (pp. 363-364 etc.), seals "with a cypher and coronet"; index "Cipher, letters, &c. in, 201, 205, 217, 227, 314, 363, 364, 374" -- p. 387 is not among them |

Vol. 2: 0 hits for all three names (regex and fuzzy), 0 King William's Chest 6 references; 21 cipher words, none
within 400 characters of a name.

Found: the calendar's one-line description of the letter (vol. 1 p. 387, King William's Chest 6 No. 68; TNA's item
65), already logged by GF-A2-6 on 2 Oct 2026 and confirmed here by script. Not found: any extract, "in cypher" note,
plaintext or decipherment of this letter in vol. 1 or vol. 2, nor any other mention of the three named parties in
either volume; the calendar's own cipher index does not list p. 387. The calendar's editorial rule (vol. 1 front
matter: "when a contemporary or authorised decipher exists it will be sufficient to treat the cipher as an ordinary
document") means a one-line entry neither confirms nor excludes a decipher among the original papers -- only the
leaf can settle that. Search result, not a novelty verdict (rule 10).

Requests: archive.org 3 (metadata x1, djvu.txt x2, >= 1.6 s apart). No vision, no subagents.

Next cheapest step: recommended step (2), identification of the three parties (SSNE / Bernstorff-Celle
prosopography), web-only, about USD 2; the letter itself stays copy-order (REQUEST.md, `digitised: false`).

## GAPS114 (3 Oct 2026, account-4): party identification, web-only

Step run: "Recommended next steps" (2), web and API only, no vision, no subagents. Identifications below are
probable, not confirmed; nothing here is a reading or a novelty verdict (rule 10).

| Party (TNA / CSP spelling) | Best candidate | Evidence | Confidence |
|---|---|---|---|
| Mons. de Guldenstolp | Nils Gyldenstolpe (1642-1709), Swedish envoy at The Hague 1679-1687; in 1689 lantmarskalk of the Riksdag and royal councillor (riksråd), count 1690 | sv/en Wikipedia, SBL art. 13339, NE (WebSearch 3 Oct 2026); the only Gyldenstolpe of diplomatic weight in 1689 | probable |
| Major d'Ehrenstein | an Ehrenstéen (Swedish noble family nr 33), Gyldenstolpe's brothers-in-law: Nils Gyldenstolpe married Margareta Ehrenstéen (b. 1659) at The Hague, 22 Oct 1676. Her brother **Lars Filip Ehrenstéen (1662-1700)**: "Kapten vid blå regementet i Lüneburg 1688 ... Major 1694 ... Major vid garnisonsregementet i Bremen 1697" (Adelsvapen-Wiki, Ehrenstéen nr 33, fetched 3 Oct 2026). Brother Edvard (1664-1711) was in the Swedish life guards (lieutenant 1688), and Carolus Ehrenstein (b. Thorn 1656, son of riksråd Edvard Ehrenstéen) travelled with Gyldenstolpe as his embassy secretary at The Hague (Thornische Chronica 1727, Google Books snippet). | possible-to-probable: Lars Filip fits the Lüneburg (Celle) service and the Gyldenstolpe link, but the genealogy gives him "kapten" in 1688 and "major" only from 1694, so either the TNA date "[1689]" is a cataloguer's bracket or the rank is a courtesy/foreign-service rank. Not confirmed. |
| Mons. de Bernsdorff | Andreas Gottlieb von Bernstorff (1649-1726), leading minister of Duke Georg Wilhelm of Brunswick-Lüneburg at Celle (Hanover prime minister from 1709) | ADB / de-Wikipedia / Deutsche Biographie (WebSearch 3 Oct 2026); the Celle "blue regiment" link above | probable |

Context consistent with a cipher letter between these parties in 1689 (not evidence for its content): Celle troops
served William III in 1688-89, and from September 1689 Georg Wilhelm of Celle occupied Lauenburg against Denmark,
a dispute in which Sweden's stance (Gyldenstolpe sat in the Council) mattered to Celle. The letter's presence in
King William's Chest suggests it was intercepted, forwarded to William, or handed over by Bernstorff -- not settled.

Where a sibling letter, key or decipherment would sit (named, not searched this pass):
1. **Bernstorff side:** Niedersächsisches Landesarchiv, Abt. Hannover -- Bernstorff's Nachlass (Wikidata Q442108
   records an NLA Nachlass) and the Celle ministry series (Celle Br. / Calenberg Br. foreign-affairs files for 1689,
   Lauenburg succession). Searchable in Arcinsys Niedersachsen (www.arcinsys.niedersachsen.de) for "Ehrenstein" /
   "Ehrensteen" / "Gyldenstolpe" 1689.
2. **Ehrenstéen / Gyldenstolpe side:** Riksarkivet Stockholm -- Gyldenstolpe family archive (EMLO catalogue
   "The Correspondence of the Gyldenstolpe family", emlo-portal.bodleian.ox.ac.uk, catalogue=gyldenstolpe-family)
   and the Ehrenstéen papers; NAD search for "Ehrenstéen" brev 1689. The EMLO Solr endpoint answers plain GET
   (CLAUDE.md host table) and is the cheapest next probe.
3. **William's side:** the rest of SP 8/6 (Discovery queried 3 Oct 2026 for Bernsdorff, Guldenstolp, Lunenburg,
   Zell: only SP 8/6/65 itself and an unrelated Schomberg letter, SP 8/6/40) -- no sibling in the piece under those
   terms.

Positive control for the Google Books route: the query `"Ehrenstein" "Bernsdorff"` returns the CSP Dom W&M vol. 1
p. 387 entry itself (18 hits, all editions of that calendar); `"Ehrenstein" Bernstorff Gyldenstolpe` returned 0, and
no printed source tying the three names to a 1689 letter, key or decipherment was found. Search result, not a
novelty verdict (rule 10).

Requests: WebSearch 6; adelsvapen.com 2 (one 404); www.googleapis.com/books 6; discovery.nationalarchives.gov.uk 4
(via tools/discovery_items.py, one per term). No vision, no subagents.

Next cheapest step: EMLO Solr query (gyldenstolpe-family catalogue, plain GET) for Ehrenstéen / Bernstorff letters
of 1688-1690, about USD 1; then Arcinsys Niedersachsen search for the Bernstorff/Celle side (browser tool, about
USD 2). The letter itself stays copy-order (REQUEST.md, `digitised: false`).

## GAPS119 (3 Oct 2026, account-4): EMLO Solr probe, Gyldenstolpe / Ehrensteen / Bernstorff 1688-90

Step run: GAPS114's named next step. The EMLO Solr endpoint (`emlo.bodleian.ox.ac.uk/solr/all/select`) was queried
by plain GET, about 1.6 s apart. No vision, no subagents, no reading. Nothing here is a reading or a novelty verdict
(rule 10).

Positive control: `foaf_name:Gyldenstolpe*` returned 13 person records, among them **Nils Gyldenstolpe, 1642-1709**
(200 works addressed to him). The free-text query `cipher OR cypher` returned 191 works across EMLO (for example
"Wallis cipher books"), so a zero below is a real zero for this index and not a broken query. Both controls passed.

| Query | Hits | What they are |
|---|---|---|
| Gyldenstolpe family catalogue (`cito_Catalog`), all works | 207 | letters to Nils from his brothers Daniel, Samuel, Carl, Gustaf and others, 1661-1680, plus 3 later ones (Samuel 4 Mar 1692; Carl 15 Jul and 18 Dec 1699) |
| same catalogue, works dated 1688-1690 | 0 | -- |
| same catalogue, cipher/cypher/chiffre/chiffer/ziffer/decipher* (free text) and cipher-like keywords | 0 / 0 | -- |
| persons named Ehrenst* | 4 | Margareta (Nils's wife), Edvard Philipsson, Carl (1656-1702), **Lars Philip Ehrensteen (1662-1700)**: EMLO describes him as "Courtier in the Court of Charles XI ... Major in the Swedish Military; Commandant of the Ottersberg Castle". He wrote no works and received none; he is mentioned in 3 works |
| works mentioning Lars Philip or Carl Ehrensteen | 6 | all are 1676-1679 family letters to Nils (Daniel, Carl). None is from 1687-91 |
| works 1687-1691 naming Ehrenstein/Ehrensteen/Guldenstolp*/Gyldenstolp* (free text) | 0 | -- |
| persons named Bernsdorf*/Bernstorf* | 2 | Andreas Gottlieb von Bernstorff, 1649-1726 (2 works addressed to him); Johann Hartvig Ernst (1712-1772) |
| works linked to A. G. von Bernstorff | 2 | E. S. Cyprian to Bernstorff, 11 Sep 1719 and 25 Feb 1722: drafts at Forschungsbibliothek Gotha, Chart. A 425 and Chart. A 301. Not 1689 and not the Celle ministry |
| Wallis cipher books catalogue, years present | 53 works, 1641-1658 only | no 1688-90 item, so no Wallis decipherment of this letter is catalogued in EMLO |

Repositories and shelfmarks, read from the manifestation records. The Gyldenstolpe family manuscripts are held at
**Uppsala universitetsbibliotek, Nordin collection** (sample: `Nordin 469:71`; the 1692/1699 letters are in `Nordin
469` and `Nordin 470`; 206 Nordin shelfmarks among Uppsala's 300 EMLO manifestations). They are not at Riksarkivet,
which GAPS114 had assumed. The printed copies are Sarasti-Wilenius 2015 (Latin letters of the Gyldenstolpe brothers,
1661-1680) and Ström 2017. The `bibo_Note` field is empty on every Uppsala manifestation (0 of 300 carry one). The
cipher, key and shelfmark information therefore comes from the work and manifestation fields above, not from a note.

Found: the EMLO Gyldenstolpe corpus is the brothers' letters to Nils, almost all from 1661-1680, held at Uppsala
(Nordin 469-470). It contains nothing from 1688-90, nothing from or to an Ehrensteen, and nothing that mentions a
cipher or key. EMLO's Lars Philip Ehrensteen record adds his Ottersberg (Bremen-Verden) command, which is consistent
with GAPS114's Lüneburg/Bremen service but does not settle the 1689 rank. EMLO has no Bernstorff material from 1689.
Not found in EMLO: any sibling letter, key or decipherment for SP 8/6/65. This is a search result, not a novelty
verdict (rule 10).

Where a sibling would sit, named from these results only (none of them searched this pass):
1. Uppsala UB, Nordin collection: the volumes next to Nordin 469-470, in case Nils Gyldenstolpe's incoming
   letters for 1688-90 continue beyond what EMLO catalogues. EMLO's own coverage stops at 1680, so the volume list
   in Uppsala's catalogue (Alvin / the UUB manuscript catalogue) is the place to check whether Nordin 469-470 run
   into 1689.
2. NLA Hannover (Celle Br. / Bernstorff Nachlass), unchanged from GAPS114. EMLO adds nothing for 1689 on the
   Bernstorff side; its only Bernstorff manifestations are at Gotha and date from 1719-22.

Requests: emlo.bodleian.ox.ac.uk 25 (Solr select, ~1.6 s apart). No vision, no subagents.

Next cheapest step: check Uppsala UB's manuscript catalogue (Alvin, plain search) for the contents and date range
of Nordin 469-470 and the neighbouring Nordin volumes holding Nils Gyldenstolpe's correspondence from 1688-90.
Web/API only, about USD 1. Then the Arcinsys Niedersachsen search for the Bernstorff/Celle side (browser tool,
about USD 2). The letter itself remains a copy order (REQUEST.md, `digitised: false`).

## GAPS123 (3 Oct 2026, account-4): Uppsala (Alvin / Nordin catalogue) and Arcinsys Niedersachsen

Step run: GAPS119's named next step (Alvin for Nordin 469-470 and 1688-90 Gyldenstolpe volumes), then the Arcinsys
search for the Bernstorff/Celle side. Plain curl GET on both hosts (no challenge), about 1.6 s apart. No vision, no
subagents, no reading. Nothing here is a reading or a novelty verdict (rule 10).

**Uppsala, Alvin (www.alvin-portal.org).** Positive control: `Gyldenstolpe` 223 hits, `Gyldenstolpe Nils` 76 hits.
- `Nordin 469` (alvin-record:380384) and `Nordin 470`: bare shelfmark records, "Format: Non digital", no contents
  note. `Nordin 464` (alvin-record:380409): "Brev till Nils Gyldenstolpe från enskilda, W-Ö", Non digital. So the
  Nordin 4xx run is Nils Gyldenstolpe's incoming letters filed alphabetically by sender, not by year.
- The volume-level contents are in the typed copy of the collection catalogue, "Katalog över nordinska samlingen :
  4. 442-724" (alvin-record:255191, "Format: Non digital + Digital", OCR text attachment ATTACHMENT-0398, 253 kB;
  the handwritten original is UUB arkiv M 19 a-g). Grepped for Ehrenst*/Gyldenstolp*/Bernst*/Celle/chiff*/1689:
  - **Bernstorff**: two items only, neither 1689. A letter "Bernstorff, Minister hos Hert. af Celle", dated Celle
    26 July 1696 with 2 enclosures, among letters to N. Gyldenstolpe from individuals; and Gyldenstolpe's own drafts
    to Bernstorff ("Premierminister hos Hert. af Braunschw.-Lüneburg-Celle"), The Hague 14/24 Mar and 7/17 Oct
    1682 (Nordin 467, "Gr. N. Guldenstolpes Bref till åtskillige. Concepter").
  - **Ehrensteen family** (catalogue section C, "Ehrenstenska familjebrefvexlingen", Nordin 473 and neighbours):
    letters of Lars Ph. Ehrensteen ("f. 1662 - Commend. i Ottersberg, +1700") to his mother only, Uppsala 15 Jan
    1678 and Forsby 17 May 1693 (with enclosure). No letter of his from 1688-90, none to or about Bernstorff.
    Margareta Gyldenstolpe (née Ehrensteen) to her husband: one letter of 1689 (Forsbygård, 28 July).
  - **1689 overall**: 13 occurrences of "1689" in the volume; none is Ehrensteen, Bernstorff or Celle.
  - **Cipher**: one key volume, **Nordin 724, "Chiffer-[nycklar?] för svenska diplomater och militärpersoner
    1640-166?"** (OCR damaged; Alvin record alvin-record:380743, "Format: Non digital"). Its date range stops in
    the 1660s, so it is not a 1689 key; noted as a Swedish key-family source only. Section 14 of the same
    catalogue lists "Bref och rapporter till N. Gyldenstolpe, dels utan namn dels med oläsliga [underskrifter]",
    21 pieces, undated in the catalogue: unsigned reports, the one place in the Nordin run where an unattributed
    1689 piece could sit unseen.
- Free-text `chiffer` in Alvin: 18 hits, none 1680-1700 except "Castel Rodrigo ... brev i chiffer", 1695? (Örebro,
  OUB/001/208), unrelated. `chiffer 1689`: 0.

**Arcinsys Niedersachsen (www.arcinsys.niedersachsen.de, einfachsuchen.action GET).** Positive control:
`Bernstorff` 1,215 hits; restricted to 1688-1690, 49.
- `Ehrenstein` 64 (none 17th-century Celle; seals and 19th-20th-century persons); `Ehrensteen OR Ehrensten` 6, of
  which **NLA ST, Rep. 5a, Nr. 734**, Gyllenstierna's correspondence including "Korrespondenz Ehrensteens mit
  Gyllenstierna vom 2. Dezember 1699 ..." (1699-1701; Lars Philip as Ottersberg commandant: a hand sample for him, not
  a sibling). `Gyldenstolpe OR Güldenstolpe OR ...` 7: **NLA HA, Celle Or. 8, Nr. 1304/1**, B. Oxenstierna,
  N. Bielke and N. Gyldenstolpe [to Celle], 1 July 1691, the nearest dated Celle-Gyldenstolpe item.
- Bernstorff 1688-90 (page 1, 20 of 49 rows): **NLA HA, Cal. Br. 24, Nr. 1627, "Vier Briefe Portlands an Bernstorff
  aus England", 1689** (William III's side of the same channel; old sign. Cal. Br. 24 England Nr. 49), and
  **NLA HA, Celle Br. 16, Nr. 401**, a Hamburg agent's report to Bernstorff on a rumoured France-Denmark alliance,
  1689. Neither title names Ehrenstein, Gyldenstolpe or a cipher.
- Cipher wording 1688-90 (`Chiffre OR Ziffer OR dechiffriert OR Chiffern`, 19 hits): **NLA WO, 2 Alt, Nr. 2837 and
  2838, "Chiffern zur Korrespondenz der Herzöge ... mit den Gesandten an den Höfen in Hannover, Celle, Paris,
  Petersburg, Berlin ...", Bd. 1 (1641) 1675 - end 17th c., Bd. 2 1675-1725.** These are Wolfenbüttel keys, not
  Celle's, but they name Celle as a correspondent court.
- `Schweden Bernstorff` 1688-90: 3, `Stockholm Gesandtschaft` 1688-90: 5 (Bremen-Verden Ritterschaft envoys, not
  Celle), `Lauenburg Schweden` 1689: 0.
- Availability flag, quoted from each detail page's "Repräsentationen": Original, Sicherungsfilm (and for the two HA
  files Micro-/Macrofiche); no Digitalisat on any of the four files above.

Found: no sibling letter, key or decipherment of SP 8/6/65 in the Uppsala Nordin catalogue or in Arcinsys under these
terms. Two leads, both of them undigitised: Cal. Br. 24 Nr. 1627 (Portland to Bernstorff, 1689) on the
recipient's side, and NLA WO 2 Alt 2837-2838 (Guelph cipher keys naming Celle, to 1699) as a possible key family. Both
are physical-access items. This is a search result, not a novelty verdict (rule 10).

Requests: www.alvin-portal.org 20 (incl. one OCR attachment); www.arcinsys.niedersachsen.de 23 (5 of them empty
detail fetches before the redirect was followed). No vision, no subagents.

Next step: the letter itself remains a copy order (REQUEST.md, TNA `digitised: false`); the cheapest remote step
left is a reproduction enquiry to NLA (Hannover for Cal. Br. 24 Nr. 1627, Wolfenbüttel for 2 Alt 2837, both on
Sicherungsfilm) for the person's desk, about USD 0 of model time plus the archive's fee.

## While waiting

- [done 6 Oct 2026 R8-SPS1, pages 2-3 read, no hit; Celle Br. 16 / Cal. Br. 24 tree lists not done] Action that depends on nobody: read the remaining 29 rows of the Arcinsys `Bernstorff` 1688-1690 list (page 2-3)
and the Celle Br. 16 / Cal. Br. 24 England series lists in the Arcinsys tree for any 1689 file naming Sweden,
Gyldenstolpe or Ehrenstein (web only, about USD 1).

## R8-SPS1 (b): Arcinsys `Bernstorff` 1688-1690, pages 2-3 (6 Oct 2026, 04:2x UTC)

Intake gate: `open (line 1)`. Same query as GAPS123 (rechercheBean.defaultfield=Bernstorff, von 1688, bis 1690): 49 hits, 3 result pages, all three read via `recherchePaging.action?pagingvalues=N` (sessioned, 2 s apart). Pages 2-3 carry no Ehrenstein, Gyldenstolpe/Güldenstolpe or Chiffre/cipher wording (regex over all three pages: 0 hits). Items seen: NLA HA Cal. Br. 1 Nr. 2341 (Harpstedt prisoner, 1689-1701); NLA ST Rep. 5a Nr. 128 (Reichskammergericht move, 1680-95, includes letters of Carl XI of Sweden, not Ehrenstein); NLA WO 2 Alt Nr. 18282 (intercessions to Hessen-Darmstadt); NLA ST Rep. 5a Nr. 2441 (Reduktion donierter Güter); NLA WO LB Nr. 2981 (Trauerschriften). Page 1 additionally lists Cal. Br. 24 Nr. 3005 (P. Siegel to Bernstorff from The Hague, 1689), Cal. Br. 24 Nr. 1597 (instruction for Schütz's mission to England, 1689), Cal. Br. 11 Nr. 1085 and Celle Or. 8 Nr. 1295/1 (5 Dec 1689 treaty extension, Heeckeren/Bernstorff): England-adjacent 1689 items, none naming Ehrenstein or a cipher. Found: no Ehrenstein or cipher item in the list. Not done: the Celle Br. 16 / Cal. Br. 24 England series tree lists (second half of the While-waiting line). A search result, not a novelty verdict. Host requests: www.arcinsys.niedersachsen.de 8.
