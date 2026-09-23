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

## Next

Small, single-volume item (66 folios total, key included in the same volume) — the cheapest access route
of the three N-targets this sweep covered. BL Imaging Services quote for Add MS 4956 in full (diary leaves
+ f. 66 key) is the natural next step; a REQUEST.md can be drafted for this once someone reads Sloane MS
4019 f. 79 first (a single-folio check, likely far cheaper than a full Add MS 4956 reproduction, and might
close the question on its own). Also worth a JSTOR search on "Courten" + "diary"/"cipher" before ordering,
per rule 10's demand for a documentary-edition and scholarship check beyond WebSearch.
