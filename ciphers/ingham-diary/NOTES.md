found-solved

# Benjamin Ingham's Oxford Methodist diary "in Cipher", 1734 — Manchester University, Methodist Archives and Research Centre

QUEUE row: N12 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE"; the
same item also appears in the companion `-excluded.tsv` at scout stage, marked "not-record-level" — a
bare NRA index entry with no shelfmark — but was nonetheless scored into the main candidates sheet).

## Source

TNA Discovery, record **N13677160** (an aggregated National Register of Archives entry, `source: "NRA"`,
`catalogueLevel: 0`, no TNA reference of its own — only `otherReferences: [{"value": "25824"}]`, an NRA
report number). Full record fetched via the item-details endpoint
(`discovery.nationalarchives.gov.uk/API/records/v1/details/N13677160`, 24 September 2026):

> **coveringDates**: "1734" (coveringFromDate/coveringToDate both 1734).
> **scopeContent.description**: "**diary in Cipher**."
> **heldBy**: "Manchester University: Methodist Archives and Research Centre."
> **note**, **title**, **citableReference**: all null — this is the entirety of the catalogue text.

A Discovery search for "Ingham diary" (broadened beyond the piece filter, 1 request) returns exactly this
one record for Benjamin Ingham (1712-1772) at Manchester Methodist Archives — no sibling Ingham diary
entry for any other year is catalogued there on Discovery/NRA.

## Check-solved sweep (24 September 2026)

1. **The decisive check: is this the diary Heitzenrater already deciphered?** Richard P. Heitzenrater,
   *Diary of an Oxford Methodist: Benjamin Ingham, 1733-1734* (Duke University Press, 1985), is freely
   readable on archive.org (`diaryofoxfordmet01ingh`, not access-restricted; fetched the full djvu text, 2
   requests). Heitzenrater's own preface (pp. ix-x) describes finding the manuscript "in the solitude of
   the Methodist Archives strongroom in London on the last day of July 1969" — "a little notebook... the
   diary of Benjamin Ingham, friend of the Wesleys and fellow Oxford Methodist" containing "a key to much
   of the Wesleyan system of abbreviations and symbols" and "symbols, and a complex cipher... woven together
   to allow secrecy." The book's citation apparatus (p. 434) gives the manuscript's present location as
   "Methodist Archives, The John Rylands University Library of Manchester" — the Methodist Archives moved
   from London to the John Rylands Library, University of Manchester, in 1977 (confirmed by WebSearch of
   the Rylands' own collections page), matching the Discovery record's holder, "Manchester University:
   Methodist Archives and Research Centre", exactly. Heitzenrater's edition covers "1733-1734" and is the
   diary of the Oxford Methodist period; the Discovery record's covering date, "1734" (a single year, not a
   date range), sits inside that same span. No other Ingham diary of any date is catalogued at this holder
   on Discovery, and Ingham kept the Wesleyan-style "exacter diary" format specifically during his Oxford
   Methodist years (1733-34) per Heitzenrater's introduction — the years after, once Ingham had become an
   independent evangelist, are not described in the book as being in this shorthand/cipher format. Taken
   together (matching holder, matching date span, matching description "a complex cipher", no sibling
   record), this is almost certainly the same physical notebook, and it has been fully transliterated and
   published, with extensive annotation, since 1985 — forty-one years before this sweep.
2. **What system it actually is.** Heitzenrater's introduction and notes throughout identify the diary's
   shorthand as **James Weston's shorthand system** (a period stenography, the same system John Wesley
   later adopted and adapted into his own diary code), combined with numerical/symbolic abbreviations for
   activities and a small nomenclature of names — a personal secrecy/speed system of the Pepys-Byrom-Wesley
   type named in this project's own QUEUE row as the likely explanation, not a diplomatic or espionage
   cipher. This matches the QUEUE N12 row's own caution: "personal shorthand/cipher diaries of this type
   (cf. Pepys, Byrom) are often a known period shorthand rather than a true cipher."
3. **Print.** Heitzenrater 1985 (above) is the edition; his 1972 Duke PhD dissertation preceded it as the
   original decipherment. No further print check needed once the manuscript identity is established.
4. **Community lists.** `sources/cryptiana/` grepped for "ingham": no genuine hit (grep matches are all
   "Walsingham" substrings). Consistent with this being outside Cryptiana's diplomatic/state-cipher scope.
5. **DECODE.** `ay/catalogue/decode-catalog.csv` grepped for "ingham": no genuine hit (same
   "Walsingham"/"Nottingham" substring noise, no record for Benjamin Ingham).
6. **Bourdeau.** `cs-recheck/CATALOGUE.md` and `SOLVED_CATALOGUE.md` grepped for "ingham": no genuine hit
   (same substring noise).
7. **Aymeloglu.** `ay/CATALOGUE.md` grepped for "ingham": no hit.

Requests: discovery.nationalarchives.gov.uk 3 (1 item-details fetch, 1 parent-record fetch that returned
HTTP 204/no content for the NRA fonds level and was not pursued further, 1 broadened "Ingham diary" search
retried once after an initial empty/202 response). archive.org 2 (metadata + djvu text fetch for
`diaryofoxfordmet01ingh`). WebSearch: 2 queries.

## Edition risk

**Realized.** The Wesleyan-shorthand/cipher system in Ingham's diary was broken by Heitzenrater in the
process of reading John Wesley's diaries (research published from 1972 on) and the Ingham diary itself was
published in full transliteration in 1985. No cryptanalytic value remains in the item as catalogued.

## Verdict

**Found-solved — not a recovery or cryptanalysis target.** Not "new"; not "unpublished" (rule 10): the
diary's shorthand/cipher system has been in print since 1985 (Heitzenrater), and the underlying research
that broke it dates to 1969-72. This is also, more fundamentally, not the kind of item this project's
"unique solve" metric is built around (README "What counts as a result") — a personal period shorthand
system, not a correspondence cipher with a key that opens unread diplomatic or private text.

## Next

Drop N12 from the board. No access route needed. If anyone wants to fully confirm the manuscript identity
beyond the strong circumstantial match above (same holder, same date span, "complex cipher" wording), the
cheapest check would be a direct email/catalogue-search of the Rylands' online finding aid for the exact
shelfmark of MAM Ingham's diary and a page-count/format comparison with Heitzenrater's physical description
("a little notebook... small leatherbound volume") — not pursued here since the check-solved brief does not
extend to manuscript identification beyond what is needed for a stage-2 verdict, and the verdict here is
found-solved, not open.
