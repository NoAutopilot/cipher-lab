found-solved
Printed with its cipher passage deciphered: "The Herbert MSS. at Powis Castle", *Collections Historical & Archaeological relating to Montgomeryshire* vol. 20 (Powys-land Club, 1886, extra volume), Part I Miscellaneous, nos. XLIII-XLIV, pp. 73-76 -- read in full by this worker from the archive.org djvu text (`collectionshist04unkngoog`), found by Google Books full-text search for "Horesse" (volume sdg4AQAAMAAJ, snippet "1717, December 4 Letter (partly in cipher) from \"Mrs Horesse\"").

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

## While waiting (27 Sept 2026, WAIT-PASS-B)

Waits on: page copies of PRO 30/53/11/42 and /43 (REQUEST.md, since the 24 Sept 2026 check-solved sweep).

- M: read the note field of every item in PRO 30/53/11 individually by record id -- description-text search misses cipher marks -- tools/discovery_items.py.
- S: confirm W. J. Smith's 1963 Herbert Correspondence table of contents actually stops before 1717; that is currently only inferred from the edition's title, not checked directly.
- S: search 'Horesse' as a possible garbled name/code-name variant against the Herbert-family genealogy material already surfaced this pass.

## Check-solved re-run (GF4-BATCH13, account-4, 3 Oct 2026)

Gate fix: the 24 Sept verdict named no edition read. Re-run per `.claude/briefs/check-solved.md`.

1. **Edition (found).** Google Books API (`q="Horesse"`, key + `country=US`) returned *The Montgomeryshire Collections* 1886
   (sdg4AQAAMAAJ, N5ExAQAAIAAJ, 050MAAAAIAAJ), snippet: "1717, December 4 Letter (partly in cipher) from \"Mrs Horesse\"" with the
   numeral groups "16:27:11 -- 18 : 11 : 27 : 21" beside it. The archive.org copy `collectionshist04unkngoog` (vol. 20, 1886,
   "Being an extra volume, 'The Herbert MSS.' at Powis Castle, etc., presented by the President, the Earl of Powis") was read in
   full text by this worker (djvu, grepped for Horesse/Horbu/partly in cipher/the numeral groups, then the pages read). It prints:
   - **No. XLIII** (table of contents "1717, December 4. Letter (partly in cipher) from ---- to 'Mrs. Horesse'"), pp. 73-75: the
     whole letter (dated "Decemb. 4th 1717", opening "I wrote to you last week upon my coming here...") with every cipher group
     printed in place (e.g. "4 -- 18 : 23 : 7 : 15 : 11 : 5 : 21"), then a running decipherment of the cipher passages: "a subject
     subj a princes is to be got, then is one sent to see two who are named and I doe not yet believe that y'e p's of is
     impracticable who I confess I wish rather than any of y'e other two upon account of the good character she has besides a
     fine person it will take two months att least before there can be any certainty as to any of y'm, but as things goe you may
     be sure to hear from me ... friends subjects a prencess"; then "[On a detached paper.]" (p. 75) a short number-to-letter /
     name table (OCR rough: "23:19:7:15:27:16 ... 54 D 15 A 98 ... 78 e"), and the address "To Mrs. Horesse". The cipher is a
     numeral letter cipher (4 = a, 18 = s, 23 = u, 7 = b, 15 = j, 11 = e, 5 = c, 21 = t gives "subject" from the printed groups,
     a check by eye of the printed gloss, not a reading of ours).
   - **No. XLIV**, pp. 75-76: "1717, December 4. Letter from ---- to ----", "Decemb: 4th 1717. Madam, ..." (no signature, no
     address) -- the same hand per TNA's /43 description; in clear except name-code numerals (37, 24, "15 : 98 w't 78", 97, 16,
     43, 39, 31, 17), some of which the detached paper of no. XLIII glosses (15 = A, 98, 78); the rest are printed as numerals
     with no gloss.
   Match to the TNA items: same date, same recipient, "partly in cipher" (/42 note) and "letter in the same hand" (/43
   description) follow the 1886 calendar's own wording; PRO 30/53 is the Herbert/Powis Castle collection the 1886 volume prints.
   Context (inference, grade I, not checked further): written from the Stuart court at Urbino (Dec 1717; the letter calls it
   "out of the world ... an uglier & duller place"), on the search for a princess for James III -- the courtier's identity and
   the code names are left for any later reader.
   HMC *Calendar of the Stuart Papers* vol. 5 (archive.org `calendarofstuart05grea`, covers 1 Sept 1717 - 28 Feb 1718) grepped
   whole-volume for Horesse/Horess/"Mrs. Hor"/Powis and the 4 Dec 1717 entries (pp. 252-254) read: no copy of either letter, no
   "Horesse" in the index (Herbert entries: Lady Mary, Thomas 8th Earl of Pembroke only). Vol. 6 (`calendarofstuart06grea`)
   grepped: no Horesse.
2. **Web.** WebSearch `"Mrs Horesse" 1717`; `"PRO 30/53/11" Herbert cipher 1717`; `Herbert Powis Jacobite letter December 1717
   "partly in cipher" Horesse`; `"Horesse" Herbert papers National Archives letter` -- no hit on this item (genealogy, Hoover
   papers, an unrelated PRO 30/53/5 catalogue page). No model-solve announcement.
3. **Community lists, DECODE, Bourdeau, Aymeloglu.** As 24 Sept (no hit); not re-cloned this pass.

**Verdict: found-solved, F1** -- the plaintext and the cipher groups of /42 have been in print since 1886 (Montgomeryshire
Collections vol. 20 pp. 73-75), and /43 likewise (pp. 75-76, its name-code numerals only partly glossed); TNA's catalogue
entries for PRO 30/53/11/42-43 do not cite the print, and our queue (N57) and the 24 Sept sweep did not know of it. What it
leaves to hand on: the print citation for TNA's catalogue and for the list keeper; optionally a key table for the numeral
cipher from the printed groups and gloss, and the unglossed name codes of /43 (37, 24, 97, 16, 43, 39, 31, 17), which are a
small residual, not a reason to hold the folder open. REQUEST.md's copy order is moot for reading the text (the print has it);
an image would only serve a check of the 1886 transcription. No cryptanalysis, no transcription done here.

Requests: archive.org 9 (advancedsearch 4, djvu downloads 9 incl. one HTTP 500 on `collectionshist02unkngoog`, 1.6 s apart);
googleapis.com 7 (1.6 s apart); WebSearch 4 + 3 blog-site searches (shared table below).

## Web and blog check (GF4-BATCH13, account-4, 3 Oct 2026)

- Plain web: `"Mrs Horesse" 1717` (no hit); `"PRO 30/53/11" Herbert cipher 1717` (one TNA catalogue page, PRO 30/53/5/108, 1623,
  unrelated); `Herbert Powis Jacobite letter December 1717 "partly in cipher" Horesse` (Wikipedia Powis/Jacobite pages, no item);
  `"Horesse" Herbert papers National Archives letter` (Hoover papers, unrelated).
- Cipherbrain (site:scienceblogs.de, `Horesse 1717 Herbert cipher`): ten unrelated posts (Henry II device, Catinat, Yardley),
  none names Horesse or the Herbert papers; no comment thread to read.
- Cryptiana (site:cryptiana.blogspot.com / cryptiana.web.fc2.com, `Horesse Herbert 1717 cipher`): no results.
- Cipher Mysteries (site:ciphermysteries.com, same query): La Buse, Beale, Voynich posts only; no hit on this item.
- Result: no blog post or comment thread reads or mentions the item. The print hit came from Google Books, logged above.

## Premise check (GF4-BATCH13, account-4, 3 Oct 2026)

- (a) Folder's own files: NOTES.md and REQUEST.md mention no decipherment or clear copy -- not found (none was on file).
- (b) Other solvers' working files: no folder for this item in Bourdeau's or Aymeloglu's repositories (24 Sept grep) -- not found.
- (c) Physical neighbours: no image of the leaves is online (`digitised: false`); the printed neighbour is the find -- no. XLIII
  carries its own "[On a detached paper.]" table (p. 75), the laid-in slip this check asks about. Found (in print).
- (d) Recipient's side: the Powis/Herbert recipients' own printed papers are exactly the 1886 Montgomeryshire Collections
  volume -- found. The Stuart court side (HMC Stuart Papers v-vi) -- not found.
