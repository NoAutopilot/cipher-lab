open

# Two letters to "Mrs Horesse" — TNA PRO 30/53/11/42, 43

QUEUE row: N57 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

The National Archives, Kew, **PRO 30/53/11**, items **/42** and **/43**, both 1717 Dec 4 (TNA Discovery,
fetched 24 Sept 2026 via `tools/discovery_items.py "PRO 30/53" "PRO 30/53/11" cipher Horesse`, ids
C6745878/C6745879):
- **/42**, id C6745878: description "[?] to Mrs Horesse." Note field (fetched separately by record id):
  **"Seal Partly in cipher"** — i.e. the cipher marking is on the seal note, not the description; correspondent
  unidentified even by the cataloguer (`[?]`).
- **/43**, id C6745879: description "Letter in the same hand to Mrs Horesse." (Note field not re-fetched by
  id this pass — QUEUE row already states "Partly in cipher.")

Both undigitised (`digitised: false`, confirmed for /42 by full record fetch).

**Piece and series identification (24 Sept 2026, not in the original QUEUE row).** PRO 30/53/11 is catalogued
as "MISCELLANEOUS HERBERT PAPERS, 1586-1735" (parent id C11999), itself part of **PRO 30/53, "Edward Herbert,
1st Baron Herbert of Cherbury: Collection of Herbert Papers"** (parent id C659), covering the 14th century to
1772. The series' own administrative history describes it as centred on Sir Edward Herbert (later 1st Baron
Herbert of Cherbury), ambassador to France 1619-21 and 1622-24 — but Herbert died in 1648, seventy years
before this item's 1717 date, and the series scope note itself describes PRO 30/53/11 as a later
"miscellaneous" bundle reaching to 1735. This item therefore belongs to a **later generation of the Herbert
family** (Cherbury, Powis or another branch), not to the 1st Baron's own embassy correspondence, and the
correspondent "[?] to Mrs Horesse" was not identified with any Herbert family member this pass — "Horesse" is
not a name recognised from general knowledge of the family and was not resolved to a known Herbert
correspondent, alias, or estate connection.

## Check-solved sweep (24 September 2026)

1. **Editions.** The standard printed edition of the earlier (1st Baron's) Herbert of Cherbury
   correspondence is W. J. Smith (ed.), *Herbert Correspondence: the sixteenth and seventeenth century
   letters of the Herberts of Chirbury, Powis Castle and Dolguog* (Cardiff, 1963) — per its own title this
   covers the 16th-17th centuries only, i.e. up to c.1700, and would not be expected to reach a December
   1717 item; not confirmed against a table of contents this pass (not found on Internet Archive/Google
   Books-free by search — no hit under this run's hosts, which exclude Google Books), a caveat not a
   clearance. No calendar of PRO 30/53 itself, and no Historical Manuscripts Commission report specifically
   on the later (post-1700) Herbert papers, was located by web search
   (`"Herbert papers" Historical Manuscripts Commission Powis OR Cherbury 1717 correspondence calendar`) —
   results point only to the National Library of Wales' *separate* Powis Castle Herbert archive (a different
   physical collection from TNA's PRO 30/53) and general Herbert-of-Cherbury library/manuscript pages, none
   naming a 1717 item or "Mrs Horesse."
2. **Sibling search (TNA Discovery, same piece).** `tools/discovery_items.py "PRO 30/53" "PRO 30/53/11"
   cypher decipher key` (searched for "cypher"/"decipher"/"key" as catalogue-description terms) returned no
   rows at all — the cipher marking on /42 and /43 lives only in the **note** field ("Seal Partly in cipher"
   / "Partly in cipher"), which the standard description-field search does not reach; a second query using
   "cipher" plus "Horesse" as terms found only the two target items themselves, no companion key or
   decipherment elsewhere in the piece under those terms. This piece's records may have other ciphered items
   whose note fields likewise don't surface via a description-text search — not exhaustively checked
   (the tool searches descriptions, not note fields, for the term match itself; only /42's note field was
   read directly, by record id).
3. **Community lists.** Web search (`"Mrs Horesse" 1717 letter cipher`) returned no relevant hits at all
   (results were about Lady Mary Wortley Montagu's 1717-18 Turkish Embassy letters and unrelated ciphers —
   Bacon, Copiale, Mary Queen of Scots, Arnold). No Cryptiana or Cipherbrain post names "Horesse," PRO 30/53,
   or the Herbert papers' later cipher items. Local grep of `sources/cryptiana/` for "horesse"/"herbert"/
   "PRO 30/53": no hits.
4. **DECODE.** No login attempted. `sources/decode/` greped for "Horesse"/"Herbert"/"PRO 30/53": no hits.
5. **Solver repositories.** Both freshly shallow-cloned (24 Sept 2026, shared across this run's four
   targets). `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers`: grep for "horesse|PRO 30/53" across
   both trees returns zero matches in either repository.
6. **General web search.** A broad archive.org full-text search on the bare string "Horesse" (no login,
   `be-api.us.archive.org/fts/v1/search?q=Horesse`) returned 250+ documents across many languages — far too
   generic to be useful without a stronger anchor (almost certainly OCR noise on "horses"/similar strings in
   most hits) and not narrowed further this pass; not a targeted result, listed here only as a request-count
   note, not treated as a search of this correspondent.

**Host requests this pass:** discovery.nationalarchives.gov.uk 5 (item search + two record-detail-by-id
fetches for hierarchy, >=3s apart, shared across all four targets this run), archive.org be-api fts 1
(broad, low-value "Horesse" query), WebSearch 2, github.com 1 shallow clone each of both repos (grepped,
shared across all four targets), sources/decode/ and sources/cryptiana/ local greps (no network).

## Verdict

**Status: open.** No edition or calendar reaching this later (post-1700) stratum of the Herbert papers was
located; the one standard Herbert-correspondence edition found (W. J. Smith 1963) is scoped to the 16th-17th
centuries by its own title and would not be expected to cover a 1717 item, not directly confirmed by table of
contents this pass — a caveat, not a clearance, and the weakest link in this sweep given rule 11's edition-
first requirement. No sibling key or decipherment found in the piece under a description-text search (the
piece's cipher notes live in a field this search does not reach uniformly). No community list, DECODE record,
or solver-repository entry names "Mrs Horesse," PRO 30/53/11, or these two items. The correspondent(s) —
sender "[?]" and recipient "Mrs Horesse" — remain unidentified; resolving either name (a Herbert-family
genealogy, or "Horesse" as a possible code name or garbled surname) would be the single most useful next step
before any solve attempt, since a 93-year gap in the standard edition and two unidentified names leave this
target's edition risk genuinely untested rather than cleared.

**Copy status:** no online image located (confirmed `digitised: false` for /42); **copy-order**, both items
together (same hand, same date). See REQUEST.md.
