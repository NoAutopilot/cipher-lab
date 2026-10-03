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
vol. 1 (rather than a name-string grep alone) to rule out an OCR-garbled entry; [Done, GAPS111, 3 Oct 2026: the entry is found at p. 387 and the OCR-fuzzy sweep adds nothing; see the GAPS111 section below.] (2) identify the specific
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
