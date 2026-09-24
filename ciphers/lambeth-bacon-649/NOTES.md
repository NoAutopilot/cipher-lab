# Letters in cypher to Anthony Bacon — Lambeth Palace Library MS 649, ff. 490-495

Status: open

## Description

Lambeth Palace Library, MS 649, ff. 490-495 (part of the Bacon Manuscript, MSS 647-662, "Bacon, Anthony
(1558-1601)", extent 16 volumes, 1579-1598). Catalogue title (verbatim, CalmView record
`MSS-647-662/649/490-5`, confirmed 24 Sept 2026): "Letters in cypher to BACON (Anthony), Secretary to the Earl
of Essex." Plural "letters", 6 folios, no date field in the catalogue record. Person index entry: "Bacon;
Anthony (1558-1601); diplomat and spy" (GB/109/14512). Copies: microfilm Lambeth Palace Library MS Film 793.
Anthony Bacon ran Essex's continental intelligence network from 1593; the fonds is "most numerous from 1591."

## Check-solved sweep, 24 September 2026

**Editions first.**
- *Calendar/Index*: the fonds's own FindingAids field cites E.G.W. Bill, *Index to the papers of Anthony Bacon
  (1558-1601) in Lambeth Palace Library (MSS. 647-662)* (1974) — a finding-aid index, not a transcription or
  edition; not consulted (on open shelves at LPL only, not online).
- *Birch, Memoirs of the Reign of Queen Elizabeth* (1754): the fonds's PublnNote states verbatim "The papers of
  Anthony Bacon were extensively used by Birch in 'Memoirs of the reign of Queen Elizabeth', 1754." Ran the
  Internet Archive be-api full-text search for "cypher" (period spelling; "cipher" returned 0 hits in both
  volumes) against `b30531469_0001` and `b30531469_0002`: one hit per volume. Vol. 1, p.508, discusses several
  cipher letters in the same passage — "to procure the secretary's cypher", a correspondent told "to receive
  from him a new cypher, having burnt his other", and "a letter... September, 1592... written most part in
  cypher" from a correspondent at St Sebastian "wrote to Mr. Bacon in cypher." Vol. 2, p.562, likewise discusses
  several cipher letters in one passage (Marengo, Dr [unnamed], "a letter from mr. Foulis, containing in cypher
  the advertisements"). Neither passage cites a shelfmark or folio number, so neither can be matched to ff.
  490-495 specifically; the September 1592 St Sebastian letter is a plausible date-window overlap (MS 649 has no
  date field, but the fonds is "most numerous from 1591") but this is not established, only noted as a lead.
  Quoting Birch's own words above per rule 1/10 practice; no sentence in Birch identifies *this* item by folio,
  so this verdict is not blocked from "open" by it.
- Adam Matthew Digital's *Early Modern England* database lists "Papers of Anthony Bacon MS 649 Volume 3 [2]",
  dated 1593 (public metadata only, subscription content not accessed) — gives a rough sense that MS 649's
  internal volumes run through the early-mid 1590s, but does not confirm which volume/folios cover ff.490-495.

**Related scholarship found, not opened.** The fonds's PublnNote also cites W. Tosh, "Testimonies of Affection
and Dispatches of Intelligence: The Letters of Anthony Bacon" (PhD thesis, Queen Mary, University of London,
2014), which "include[s] substantial quotations from the Bacon letters" — a modern scholarly work specifically
on this correspondence, not checked for a match on ff.490-495 this pass (flagged for a future worker/verifier;
QMUL's repository, QMRO, likely holds it open access).

**Community lists.** Cryptiana's local snapshot has no mention of Anthony Bacon, the Bacon papers, or Lambeth
MS 647-662 (checked `grep -rliE "anthony bacon|lambeth.*bacon|bacon.*essex"`); two unrelated "Lambeth" hits in
`thurloe.htm`/`louisxiv.htm` are a different Lambeth fonds (MS 929-942, 1702 French military codes) and are
false positives on the word "Lambeth" alone. Live web search
(`Lambeth Palace Library MS 649 "letters in cypher" Anthony Bacon Essex deciphered`) returned only the
library's own catalogue pages, an Open Library/WorldCat listing of Bill's 1974 Index, CELM's Lambeth repository
page, and the Adam Matthew listing above — nothing describing this item as read or attempted.

**DECODE.** Login broken (ASKS.md row 1), not attempted. No "Bacon" row in the cached DECODE catalogue
(`unsolved-ciphers/catalogue/decode-catalog.csv`).

**Bourdeau (dbourdeau/cyphersolver).** Shallow clone. `grep -rliE "anthony bacon|lambeth.*bacon|bacon.*essex"`
— zero hits anywhere in the repository.

**Aymeloglu (aaymeloglu/unsolved-ciphers).** Shallow clone. Same grep — zero hits.

## Verdict

**open.** No solution, key, plaintext or documented attempt on MS 649 ff.490-495 was found in any of the six
sources. Birch 1754 (queried by full-text search, not read cover to cover) discusses cipher correspondence to
Bacon in the same general period but cites no shelfmark matching this item; report what was found (general
cipher-letter mentions, no specific match) and where it was not found (no repo, no DECODE row, no community-list
mention). Tosh's 2014 thesis is a named, unchecked lead for the next worker. No novelty classification made
here.

**Copy status.** Needs a copy order or on-site visit — no free digitised image located (Lambeth's own "Image
database", images.lambethpalacelibrary.org.uk/luna, returned no Bacon-papers hits for a "MS 649" query this
pass; Adam Matthew Digital access is subscription-only). See REQUEST.md.

## Access notes

Lambeth CalmView: confirmed the documented `Overview.aspx?src=CalmView.Catalog&r=((((text)='TERM')))` route
works for an exact-phrase search (a plain name query like "Anthony Bacon" over-matches at 648 rows via implicit
OR-of-words; an exact phrase like "Letters in cypher to Bacon" narrows to the single record). Requests below.

## Searched, 24 September 2026 (for CLAUDE.md rule 1)

Cipher's shelfmark/description in a search engine; sender's/subject's printed edition (Birch 1754, by full-text
search); the holding archive's own catalogue (CalmView, item and fonds level); community lists (Cryptiana local
+ live search); DECODE (cache only, login broken); both solver repositories (shallow clone, grep).
