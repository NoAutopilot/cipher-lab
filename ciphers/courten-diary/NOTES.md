open

# William Courten (Charleton) diary, partly in cipher, key by Sir Frederic Madden — BL Add MS 4956

QUEUE row: N3 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

BL Archives and Manuscripts, Western Manuscripts, **Add MS 4956**. Catalogue text, quoted verbatim from
the BL Archives and Manuscripts API (`searcharchives.bl.uk`, record id `032-002110476`, fetched 24
September 2026):

> Title: "APOLLO ANGLICANUS: an almanack published by Richard Saunder; 1698"
>
> Scope & Content: "Printed. Interleaved copy used as a diary by William Courten al. Charleton. Partly in
> cipher, to which a key has been appended by Sir Frederic Madden (f. 66; cf. Sloane MS. 4019, f. 79).
> Paper; ff. i + 66. Duodecimo. A.D. 1698. The names occur of Mrs. Langly (f. i), and Ann, Jane, and
> William Ke..." [truncated by the API at ~250 characters; the diary is a single small item, 1 item / ff.
> i + 66, so the key (f. 66) is the last leaf of the same 66-folio volume, not a separately catalogued
> piece as in the Mornington case].

This matches QUEUE.md's row exactly, including the "cf. Sloane MS. 4019, f. 79" cross-reference. Fetched
that record too (same API, 1 request): Sloane MS 4019 is "Fragments of miscellaneous catalogues... Sir
Hans Sloane, Baronet: Collection of his loose papers and letters", a large composite volume; its own
catalogue description does not say what is specifically at f. 79, so this cross-reference could not be
resolved further this sweep without ordering that folio too.

## Check-solved sweep (24 September 2026)

1. **Web search.** Four WebSearch queries this sweep: "William Courten Charleton diary cipher Madden Add
   MS 4956"; "William Courten diary in cipher Sloane manuscripts scholarship"; "Courten cipher key numbers
   Sloane specimens naturalist labels deciphered"; "Courten diary 1698 almanack transcript published
   Frederic Madden British Library". No hit on a published transcript or decipherment of the Add MS 4956
   diary text itself. A different, related fact turned up: William Courten used a **separate, short
   numeric cipher on tiny paper labels attached to specimens** in the Sloane Herbarium (Natural History
   Museum), recording provenance/donor information, and a modern researcher ("Scott", per the Sloane Lab /
   herbarium scholarship search snippet) has already decoded many of those specimen-label codes. This is
   a different corpus (herbarium labels, not the Add MS 4956 diary) and does not by itself resolve whether
   the diary's own cipher passages have been read, but it establishes that Courten's ciphering habits are
   already a studied subject among Sloane-collection scholars, which is a reason for caution before
   assuming the diary cipher is untouched.
2. **Print.** No archive.org or HathiTrust edition of the diary text was found or searched by phrase
   this sweep (the diary is unpublished as far as located; no known print edition title to search for).
   The Cambridge University repository item "William Courten's lists of 'Things Bought' from the late
   seventeenth century" (a different Courten manuscript, his purchase lists, with an online transcribed
   appendix) was found but its PDF could not be fetched cleanly this sweep (redirect/landing-page only,
   126 bytes returned) — not re-tried, low priority since it is a different document from Add MS 4956.
3. **Community lists.** `sources/cryptiana/` grepped for "courten"/"charleton"/"madden": hits in
   `spanish2C.htm`, `henryvii.htm`, `spanish2.htm` — all unrelated (other pages that happen to contain
   "Madden" or similar substrings in other contexts). No Cryptiana page on Courten. Cipherbrain: fetched
   `scienceblogs.de/klausis-krypto-kolumne/seven-encrypted-diaries/` (a post literally titled "Seven
   encrypted diaries", 1 request) and grepped for "courten"/"charleton"/"madden"/"4956": no hit in the raw
   HTML fetched — caveat: this is a heavy, consent-wall-laden WordPress/scienceblogs.de page and the
   article body may not be fully present in a plain curl fetch, so this is a weaker negative than the
   others in this sweep. Also checked two 2008 Cipher Mysteries (Nick Pelling) posts that WebSearch
   surfaced under similar keywords, "British Library cipher manuscript" and its update: no mention of
   Courten/Charleton/Add MS 4956 either (those posts are about a different BL cipher manuscript).
4. **DECODE.** Cached catalogue grepped for "Courten"/"Charleton"/"4956"/"Add MS 4956": the only "4956"
   hit is DECODE record for a Sibiu, Romania item (an unrelated coincidental record number, not a
   shelfmark match), and the only "Courten" substring hit is "Courtenay" (a French place name in an
   unrelated Colbert-era cipher, BnF fr. 6889) — both false positives, confirmed by reading the matched
   rows. `site:de-crypt.org Courten` web search: no hit. Not on DECODE.
5. **Bourdeau.** `cs-recheck/CATALOGUE.md`, `SOLVED_CATALOGUE.md`, `SOLVED_RANKING.md`, `TARGETS.md`
   grepped for "Courten"/"Charleton"/"Add MS 4956": no hit.
6. **Aymeloglu.** `ay/CATALOGUE.md`, `ay/TARGETS.md`, `ay/SHORTLIST.md` grepped for the same: no hit.

Requests: searcharchives.bl.uk 2 (Add MS 4956, Sloane MS 4019), scienceblogs.de 1, ciphermysteries.com 2,
archive.org 1 (Cambridge-repository PDF fetch attempt, failed). 12 WebSearch queries shared across all
three targets this session (see mornington-1798/NOTES.md and sp35-intercepts-1722/NOTES.md).

## Edition risk

**Not realized, but not closed.** No print edition or transcript of the Add MS 4956 diary text was found.
The adjacent fact that Courten's *herbarium-label* cipher is already partly decoded by a named modern
scholar is a caution, not a hit: it is a different, much shorter numeric code on specimen labels, not the
diary's own cipher passages, and nothing found this sweep connects that specimen-label work to Madden's
appended key at f. 66 of this volume. The unresolved "cf. Sloane MS. 4019, f. 79" cross-reference is the
main loose thread: if that folio turns out to be a related key or a note about the diary's cipher having
already been read (Madden was Keeper of Manuscripts and routinely left such notes), the picture would
change; it was not ordered or read this sweep.

## Verdict

**Open.** No decipherment, transcript, key discussion, or catalogue mention of this specific manuscript
was found in web search, print, the Cryptiana snapshot or the two cipher blogs checked, DECODE's cached
catalogue, or the Bourdeau/Aymeloglu catalogues. Not found in <source> per rule 10; this is a search
result, not a claim of discovery.

**Stage 2, verified unsolved (conditional: <what was unreachable>).** Conditional on: (a) Sloane MS 4019,
f. 79 not being read (the cross-reference the BL catalogue itself makes, which could contain Madden's own
notes on the cipher or a related key); (b) the Cipherbrain "Seven encrypted diaries" post not being fully
rendered by a plain curl fetch (JS/consent-wall page, real article text may sit behind it); (c) no search
run yet against JSTOR/dissertation literature on Courten specifically (this sweep used only WebSearch,
which is not equivalent to a JSTOR full-text search — no JSTOR credentials were used this sweep, out of
scope for check-solved per the brief).

## Print check, part 2 (24 September 2026)

**Sloane MS 4019, f.79 — resolved.** The BL Archives and Manuscripts record for Sloane MS 4019 truncates
its `scope_and_content` field to ~250-300 characters in the search-results JSON, but the *individual*
catalogue record (`searcharchives.bl.uk/catalog/040-002116413.json`, 1 request) carries the field
untruncated (7033 characters), as an itemised folio list. The f.79 entry reads, verbatim:

> "f. 79 William Courten, alias Charleton; of the Middle Temple: **Key to his cipher**: 18th cent."

This is **a second, separate copy of the key**, catalogued as 18th-century (i.e. contemporary with
Courten's own lifetime, or shortly after — not a 19th-century Madden addition like the f.66 key bound
into Add MS 4956 itself). It is not annotated as a decipherment, a transcript, or a note that the cipher
has already been read; it is a key only, the same status as the two D623/41 copies in the Mornington
target. This resolves the cross-reference the BL catalogue itself makes (Add MS 4956's note "cf. Sloane
MS. 4019, f. 79") without changing the open verdict, and adds a second key source worth imaging alongside
the diary.

**Scholarship search, four further WebSearch queries this pass** (in addition to the four run at
check-solved): `William Courten "Sloane MS 4019" cipher key Middle Temple`; `Sloane Lab project William
Courten diary cipher Add MS 4956`; `"William Courten" "Add MS 4956" OR "Additional MS 4956" diary`;
`Frederic Madden Courten cipher key almanack 1698 British Library blog`. No hit on a published transcript,
decipherment, or discussion of the Add MS 4956 diary's cipher passages, from the Sloane Lab
(sloanelab.org), the British Museum's Sloane Lab project page, Reconstructing Sloane, the Digital Ark
(Courten's own project page at USask), or the British Library blog. One dead-end checked and closed: a
search summary asserted a "Key to Charleton's cipher" in **Add MS 5156**; checked directly against BL's
own catalogue (`searcharchives.bl.uk`, 1 query) — Add MS 5156 is in fact Courten's **will** (attested
office copy, dated 10 March 1701, with three codicils), not a cipher key. This looks like a
search-summary misattribution, not a real lead, and is recorded here so nobody re-chases it.

**JSTOR queries for the next session with credentials** (not run — JSTOR_USER/JSTOR_PASS are set in this
environment but out of scope for a print-check worker per the brief; log the article and date in
ciphers/courten-diary/AUDIT.md when run):
- `"William Courten"` AND `diary` AND `cipher`
- `Courten` AND `Sloane` AND `cipher` AND `Charleton`
- `"William Charleton"` Middle Temple naturalist collection 17th century
- `Frederic Madden` AND `manuscript` AND `key` AND `cipher` AND `cataloguing` (in case Madden's own working
  papers or a 19th-century Museum report describe why he added the f.66 key, which could itself say
  whether he — or anyone since — read the diary)

Requests this pass: `searcharchives.bl.uk` 4 (Sloane MS 4019 search-results, Sloane MS 4019 individual
record, "Key to Charleton's cipher" phrase search, Add MS 5156 search); 4 WebSearch queries.

## Verdict (updated 24 September 2026)

**Open, unchanged.** Still no decipherment, transcript, key discussion beyond the catalogue's own key
notices, or scholarly treatment of this specific manuscript's cipher passages found in web search (eight
queries total across both passes), print (none checked — no known edition title to search against), the
Cryptiana snapshot, DECODE's cached catalogue, or the Bourdeau/Aymeloglu catalogues. The Sloane MS 4019
f.79 cross-reference is now resolved: it is a second key, not a decipherment or a closing note. Not found
in \<source\> per rule 10; this is a search result, not a claim of discovery. JSTOR remains unchecked
(queries logged above for the next session with credentials) — the stage 2 conditional narrows to that one
open item plus HathiTrust/Google Books full-text (not attempted this pass; no known print edition title to
search for, so a phrase search rather than a title lookup would be needed there, out of scope for this
worker's cap).

## Next

REQUEST.md drafted this pass: BL Imaging Services quote for Add MS 4956 in full (66 ff., diary + f.66
key) plus Sloane MS 4019 f.79 (the second key). No email sent, no price guessed. A JSTOR pass on the four
queries above, run by a session with credentials, should happen before the order is placed, per rule 10's
scholarship-coverage requirement — it is cheap and could change the picture at zero further imaging cost.
