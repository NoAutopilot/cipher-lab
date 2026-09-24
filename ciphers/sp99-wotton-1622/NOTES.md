open

# Letter in cipher from "159," Sir Henry Wotton's hand — TNA SP 99/24/251

QUEUE row: N59 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

The National Archives, Kew, **SP 99/24/251** (State Papers Foreign, Venice), folio 251, [?1622] (TNA Discovery,
fetched 24 Sept 2026, id C6915573; `digitised: false` confirmed by direct record fetch; `note` field: "? Wotton's
hand"). Scope content: "Letter in cipher from 159." Sir Henry Wotton was resident ambassador at Venice through
most of 1616-1624 (with breaks), so a Venice-series item catalogued to his hand in 1622 falls squarely in his
third embassy.

## Check-solved sweep (24 September 2026)

1. **Editions.** CSP Venetian calendars documents held *in the Archives of Venice* about English affairs (the
   Venetian ambassadors' own dispatches), not the English out-letters and intercepts held at TNA as SP 99 — so
   it is not the calendar for this collection, and was not pursued further as a source for this specific item
   (WebSearch confirmed CSP Venetian vol. 17, ed. Hinds 1911, covers April 1621-April 1623, but by scope, not
   shelfmark). The one edition that could calendar an SP 99 item directly, Logan Pearsall Smith's *Life and
   Letters of Sir Henry Wotton* (1907, 2 vols), was fetched in full text from archive.org
   (`in.ernet.dli.2015.184194`, vol. 2, covers the Venice years) and grepped: 7 hits for "cipher"/"cypher", none
   naming this item, "159," or SP 99/24; no hit for "159" as a correspondent name. Two footnotes on "Nys"
   confirm **Daniel Nys**, an art-purchasing agent employed by Wotton, Sir Dudley Carleton and Sir Isaac Wake at
   Venice (his major purchase, the Mantua/Gonzaga collection, came later, 1628) — a real Wotton-Venice
   correspondent, but not tied by the text to this cipher letter or to the number "159."
2. **Sibling search (TNA Discovery, same piece).** `tools/discovery_items.py "SP 99" "SP 99/24" decipher` and
   `... 159` return, besides the target, only **SP 99/24/159** itself: "Nys to [Carleton]," 1622 Oct. 25/Nov. 5,
   id C6915544 — a plain (non-cipher) item at folio 159 in the same piece. This does not confirm "159" in the
   cipher letter's description is a folio cross-reference rather than a numeric code-name for a person (both
   readings are possible from the catalogue text alone, and TNA's phrasing "from 159" reads more naturally as a
   correspondent identity than a folio pointer). No decipher, key, or duplicate record for SP 99/24/251 itself
   found in the piece under either search term. Numeric code-names for named persons are independently attested
   for a *different* Wotton (Edward Wotton, ambassador in Scotland, 1585, BL Add MS 32657 — solved by
   dbourdeau/cyphersolver, `wotton1585/`: 19 = Arran, 39 = Master of Gray, 10 = King James), which is suggestive
   of the convention but not evidence for this item or this "Wotton."
3. **Community lists.** WebSearch for "Wotton Venice 1622 correspondent 159 cipher code number intelligence"
   and a second pass on "St Quentin"-style phrasing returned only general Wotton biography (Wikipedia, LRB) and
   Venetian cryptology scholarship (Atlas Obscura, Iordanou 2018) with no mention of this item, "159," or SP
   99/24. Local grep of `sources/cryptiana/` for "wotton": no hits.
4. **DECODE.** No login attempted. `sources/decode/` greped for "159", "Wotton", "SP 99/24", "Venice 1622": the
   "159" hits are unrelated items (BRAH Signatura 9/25, BL Add MS 4136, BL Cotton MS Vespasian C IV, BnF
   Mélanges de Colbert 159) — none Venice, none Wotton.
5. **Solver repositories.** Fresh shallow clones (24 Sept 2026, shared across this pass's four targets).
   `dbourdeau/cyphersolver`: grep for "wotton|SP.?99.?24|159" across the tree surfaces only two *different*
   Wotton items, both read/partly read — Edward Wotton (Scotland) 1585 (`wotton1585/`, catalogue items 81-82,
   read) and Dr Nicholas Wotton 1554 (`harley1582r8499/`, catalogue 120, read in part) — neither is Sir Henry
   Wotton at Venice, and neither is SP 99. `aaymeloglu/unsolved-ciphers`: zero matches.
6. **General web search.** As (1) and (3). No result identifies "159" as a known intelligence code-name tied to
   Wotton's Venice network specifically, nor connects this shelfmark to any published edition or prior attempt.

**Host requests this pass:** discovery.nationalarchives.gov.uk 4 (search x2, record detail x1, >=3s apart,
shared budget with the other three targets this run), archive.org 2 (metadata + full-text fetch of Pearsall
Smith vol. 2), WebSearch 4, github.com 1 shallow clone each of both repos (grepped, shared across all four
targets), sources/decode/ and sources/cryptiana/ local greps (no network).

## Verdict

**Status: open.** No calendar reaches this collection (CSP Venetian calendars the wrong archive; Pearsall
Smith's edition of Wotton's own letters was searched in full and does not name this item or "159"). The
sibling search found a same-piece item at folio 159 ("Nys to [Carleton]") that may or may not explain the
catalogue's "from 159," but no decipher or key for folio 251 itself. No community list, DECODE record, or
solver-repository entry names this item; the two other "Wotton" targets in the solver repos are different
people (Edward Wotton 1585, Nicholas Wotton 1554), already read, and unrelated to this one.

**Copy status:** no online image located; `digitised: false` confirmed by direct record fetch (id C6915573).
**Copy-order.** See REQUEST.md.

**Recommended next steps (not run this pass):** (1) resolve whether "159" in the description is a correspondent
code-name or a folio cross-reference — read folio 159 itself ("Nys to [Carleton]") once ordered, alongside 251;
(2) if a numeric code-name, check whether Wotton's Venice network used a standing numbered-agent list
documented elsewhere in SP 99/24 or SP 99/25 (the following volume); (3) Daniel Nys is a real, identifiable
Wotton-Venice correspondent worth checking against Venice-period Wotton scholarship (Logan Pearsall Smith's
notes, or Gordon Kerr / other modern Wotton biographies) not reached under this run's hosts.
