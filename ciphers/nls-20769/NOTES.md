# Unidentified 18th-century cipher/symbol manuscript (National Library of Scotland, MS 20769)

- **Status:** closed-negative (not a cipher; NLS reply of 24 Sept 2026, below). **Extent confirmed:** the catalogue record (read 20 Sept 2026, see dated section below;
  a verbatim first-hand read, via an Internet Archive Wayback Machine capture of the live page dated 19 May
  2024, since manuscripts.nls.uk itself still refuses this environment's headless browser — see below) gives
  **Extent: 57 Leaves ; Oblong quarto and octavo**, confirming the proposer's figure. The record's own title
  is "Unidentified text, apparently 18th century, written in cipher." and its genre/form heading is "Ciphers.
  Codes.", which is stronger evidence for a genuine cipher than the earlier search-snippet read gave, but a
  cataloguer's genre tag is not proof against the private/occult-notation reading — see "Is it actually a
  cipher?" below, which still stands. Language of Materials is catalogued as "Undetermined".
- **Plaintext language:** unknown. Best guess English or Scots, weak: the manuscript is in a Scottish national
  collection and loosely encloses a copy of Sir Thomas Urquhart's *Pantochronachanon* (a work by a 17th-century
  Scottish laird, written in English, published London 1652) made by Robert Mylne. The pencilled name
  "Baptiste Romin or Romain" on ff.27-28 is ambiguous (French, or a garbled English/Scots rendering) and may
  just be an owner's or scribe's name, not evidence of the cipher's language. No cataloguer statement about the
  manuscript's own language was found.

## What the catalogue says (NLS Archives and Manuscripts Catalogue, checked 20 Sept 2026, via search snippets)

Source: manuscripts.nls.uk, record for shelfmark "MS.20769" / "MS 20769". manuscripts.nls.uk returned **HTTP
403 to curl with a browser user-agent** and a certificate error to the headless-Chromium tool
(`tools/browser_fetch.js`) on two independent attempts (once by a research subagent, once directly by the
orchestrating session) — not an org egress-policy block (checked `/__agentproxy/status`: no relay failures,
non-selective proxy), just the site itself refusing this environment. The description below is pieced together
from five independently-phrased web searches that returned identical cached text, which is strong evidence it
is the genuine record and not a generated summary, but it is still second-hand.

Quoted description (as returned by search snippets): "The cipher alphabet included Roman and Greek letters,
astrological symbols, and other apparently invented symbols. The text appears to be divided into sections by
horizontal lines... The name Baptiste Romin or Romain is added in pencil on folios 27 and 28 (inverted)...
Loosely enclosed is a fragment of a copy by Robert Mylne of Sir Thomas Urquhart's 'Pantochronachanon' (London,
1652), containing numbers 98-113 of the 'genealogy' of the Urquharts... a bifolium paginated 33-36."

Date given: "1652 and the 18th century" — most likely meaning the enclosed Urquhart fragment references the
1652 London edition, and the cipher manuscript itself is dated by the cataloguer to the 18th century; not
fully disambiguated from snippets alone.

Extent: **not independently confirmed**. The only folio numbers surfacing in snippets are 27 and 28 and a
bifolium paginated 33-36 — consistent with a manuscript of some dozens of leaves, but this does not establish
"57 leaves." That figure is the proposer's and needs checking against the live record.

Reproduction (NLS "Copying services guide", nls.uk/tools-for-research/copying-services/, prices effective
6 May 2025): A4 scan £1.80 inc. VAT (£1.50 ex VAT), A3 scan £3.60 inc. VAT, A2 £11.40 inc. VAT; A3 photocopy
£0.40/page. Minimum charges apply; prices exclude any re-use/publication permission fee. Orders via
auth.nls.uk/copy-enquiry-form/ or manuscripts@nls.uk; quote returned within 10 working days.

Digitisation: no evidence MS 20769 is on NLS's "Early manuscripts" digital gallery (digital.nls.uk/early-manuscripts/)
or has a IIIF manifest. Working assumption: not online.

## Catalogue record, read 20 Sept 2026

The section above ("via search snippets") is now superseded by a first-hand read of the actual catalogue HTML.
manuscripts.nls.uk is Cloudflare-protected (a JS "Performing security verification" challenge page, confirmed
by screenshot) and did not clear for `tools/browser_fetch.js` even after the container's NSS-store fix for
`ERR_CERT_AUTHORITY_INVALID` landed this session (see the Access playbook note below) — three attempts, up to
an 8s extra wait, all returned the Cloudflare interstitial, not the record. The record was instead read via the
Internet Archive Wayback Machine's capture of the live page, timestamp `20240519232501` (its own citation box
reads "Accessed May 20, 2024"), fetched through `tools/browser_fetch.js` against `web.archive.org` (not
Cloudflare-protected) at
`https://web.archive.org/web/20240519232501if_/https://manuscripts.nls.uk/repositories/2/resources/18888`.
The record's live URL — found via a second Wayback capture (`20240914073015`) of the "Ciphers. Codes." subject
browse page, `https://manuscripts.nls.uk/subjects/324`, which lists MS.20769 among its resources — is
`https://manuscripts.nls.uk/repositories/2/resources/18888` (the ArchivesSpace resource id, 18888, is distinct
from the shelfmark number 20769). This is a first-hand read of the cached catalogue markup, not a live fetch;
the shelfmark is stable and the record is unlikely to have changed since May 2024, but this is a snapshot, not
confirmation that the live page reads identically today.

Full "Scope and Contents", "Dates", and descriptive fields, quoted verbatim from the archived page:

> **Unidentified text, apparently 18th century, written in cipher.**
> File. Identifier: MS.20769.
>
> **Scope and Contents**
> The cipher alphabet included Roman and Greek letters, astrological symbols, and other apparently invented
> symbols. The text appears to be divided into sections by horizontal lines. The name Baptiste Romin or Romain
> is added in pencil on folios 27 and 28 (inverted).
> Loosely enclosed is a fragment of a copy by Robert Mylne of Sir Thomas Urquhart's 'Παντοχεονοχανον' (London,
> 1652). This bifolium, paginated 33-36, contains numbers 98-113 of the 'genealogy' of the Urquharts.
>
> **Dates**
> Creation: 1652, 18th century.
>
> **Conditions Governing Access**
> Normal access conditions apply.
>
> **Conditions Governing Use**
> Normal reproduction conditions apply, subject to any copyright restrictions.
>
> **Extent**
> 57 Leaves ; Oblong quarto and octavo.
>
> **Language of Materials**
> Undetermined
>
> **Arrangement**
> 27 + blank + 28 (inverted) + ii folios.
>
> **Immediate Source of Acquisition**
> Deposited, 1949, by the Society of Antiquaries of Scotland.
>
> **Genre / Form**
> Ciphers. Codes.
>
> Repository: National Library of Scotland Archives and Manuscripts Division.

Notes on the above, not repaired in the quote:
- The Greek title is transcribed by the cataloguer as "Παντοχεονοχανον"; Urquhart's actual title is usually
  rendered "Pantochronochanon" in Latin script — this looks like an OCR/typo artefact in the NLS record itself
  (Ε/Ρ, Ο/Ρ confusions are exactly what happens when Greek is mis-set from a manuscript), not something
  introduced by this project. Quoted as the record gives it.
- "Arrangement: 27 + blank + 28 (inverted) + ii folios" sums to 27+1+28+2 = 58 folios, one more than "Extent:
  57 Leaves" — an apparent internal inconsistency in the record (folios vs. leaves are not always counted the
  same way, or "ii folios" may be unfoliated endleaves counted outside the 57). Not resolved here; flagged for
  whoever eventually orders reproduction, so the frame count expected from a scan order is not a surprise.
- Provenance is now established: deposited 1949 by the Society of Antiquaries of Scotland — a first fact
  toward a provenance chain that was previously completely unknown.
- The record type badge reads "File" (an ArchivesSpace `resource`-level record, i.e., an archival file/item,
  not a larger collection or a sub-item `archival_object`) — this is a self-contained single item, not one part
  of a larger described series.

This does not settle "Is it actually a cipher?" below — the cataloguer's title and genre tag both say cipher,
which is stronger than the search-snippet read, but "Ciphers. Codes." is NLS's standard genre/form heading and
a cataloguer's classification of a mixed Roman/Greek/astrological/invented symbol set as a "cipher" is exactly
the same judgement call this project would need to independently verify from a page image before committing to
a substitution-style attack.

## Is it actually a cipher?

The cataloguer's own word is "cipher alphabet," not shorthand — but a mixed Roman/Greek/astrological/invented
symbol set with no numerals mentioned is also the classic profile of an occult or alchemical notebook, where
sigla (the standard alchemical planet/metal glyphs) mark subject matter rather than substitute letter-for-letter.
The "divided into sections by horizontal lines" detail and the loosely-enclosed Urquhart genealogy fragment
suggest a miscellany/commonplace-book context rather than a diplomatic or military cipher letter. `LESSONS.md`
notes that no verified break in this project's whole corpus was a large nomenclator read from ciphertext alone;
a large, heterogeneous symbol set spread over many leaves (if the leaf count holds) is a bad sign for
tractability even if it does turn out to be cryptographic. This cannot be resolved without a page image.

## Search before solving (CLAUDE.md rule 1), 20 Sept 2026

1. **Search engine.** "NLS MS 20769 cipher", "20769 National Library of Scotland manuscript", "National
   Library of Scotland cipher manuscript symbols", "18th century cipher notebook Roman Greek astrological
   symbols manuscript unsolved": only the NLS catalogue snippet itself (repeated); no third-party discussion,
   blog post, forum thread or solve claim anywhere.
2. **Prior mentions.** The proposer noted Cipherbrain has covered encrypted notebooks before. Klaus Schmeh's
   "List of Encrypted Books" / "111 encrypted books" pages were searched but not read line-by-line (Cipherbrain
   itself announced discontinuation around 24 Nov 2022 and has been unreliable since); no snippet named NLS or
   MS 20769. Cipher Mysteries (ciphermysteries.com) searched directly: no connection found.
3. **Community lists.** Grepped `sources/cryptiana/web/unsolved.htm` for "20769" and "National Library of
   Scotland": zero hits.
4. **DECODE.** "site:de-crypt.org 20769" and "site:de-crypt.org National Library of Scotland" returned no
   results via general web search; de-crypt.org's own internal search/browse was **not queried directly** —
   flag for a follow-up worker, since a generic site: search is a weak negative here.
5. **Solver repositories.** Grepped `/tmp/cyphersolver` and `/tmp/unsolved-ciphers` (shallow clones, 20 Sept
   2026) for "20769" (zero true hits) and "NLS"/"National Library of Scotland" (only false-positive substring
   matches inside unrelated filenames/text, e.g. "...nls..." inside soglia1848, kauderbach1754, etc.). No
   genuine reference to this manuscript in either repository.

**What could not be checked**: the live catalogue page itself (blocked from this environment — see above), the
full Cipherbrain Encrypted Book List line-by-line, de-crypt.org's own catalogue search, and any reading-room-only
digitisation not surfaced by public search. Confidence that the record is real: high (identical detailed
snippets across independent phrasings). Confidence that it is unaddressed anywhere in the sources rule 1 names:
moderate — the record itself, the leaf count and the cipher-vs-notation question all need a first-hand read
before this is worth a reproduction order.

## Ideas

The catalogue record is now read first-hand (see dated section above): shelfmark MS.20769, extent 57 leaves
confirmed, provenance (Society of Antiquaries of Scotland, 1949) established, and the cataloguer's own title
and genre tag call it a cipher. What is still missing before ordering scans: a page image (the record gives no
IIIF/digitisation link, and none was found earlier in this file), and ideally a direct answer from NLS
reprographics on whether their own cataloguer would still call this a cipher versus a private notation/shorthand
if pressed, since a genre tag alone does not settle "Is it actually a cipher?" above. With leaf count and
"cipher" status now both catalogue-confirmed, this is the largest genuinely open target in the project's queue
and worth the roughly £100-200+ (unconfirmed, 57 leaves at NLS's per-scan rates quoted above) full-manuscript
scan order — but that order should wait for the person's go-ahead, since no reproduction has been ordered here.

## Check-solved sweep, 20 Sept 2026

Six independent check-solved sweeps run 20 Sept 2026, blind to one another, covering every family named in
CLAUDE.md rule 1 plus the extra families this target's brief called out (Cipherbrain's book lists read
line-by-line, Cipher Mysteries, DECODE's own search form, the printed Proceedings of the Society of Antiquaries
of Scotland, and Romin/Romain genealogy). This supersedes and corroborates the scout pass logged above ("Search
before solving," 20 Sept 2026), which had only run a generic search-engine pass and a `site:de-crypt.org` query.

**1. Search engine and direct site checks (searcher 1).** Repeated phrasings of "MS 20769", "MS.20769",
"Baptiste Romin"/"Romain" cipher manuscript, and "National Library of Scotland cipher manuscript solved
deciphered" return only the NLS catalogue's own text, echoed verbatim across engines, with no third-party
discussion or solve claim — closed-negative. Also surfaced and ruled out as unrelated: Sir Thomas Urquhart's
own printed "Cyphral Distich" (a different NLS holding, shelfmark H.32.a.39, a 1653 printed book, not a
manuscript), reported solved by Claude Fable 5.1 per Vals AI and BoingBoing coverage dated 14 Sept 2026 — a
different item with no connection to MS.20769, Romin/Romain, or Robert Mylne, noted here only to flag it as
checked and dismissed.

**2. Print check (searcher 2).** Internet Archive's full-text API (`advancedsearch.php`, not just the search
UI) returns zero hits for `"Baptiste Romin"` and `"MS 20769"` across all indexed OCR text, and the two hits for
`"Baptiste Romain"` (a Vimeo choral transcript and a Haitian Creole linguistics document) are unrelated —
closed-negative. No sender/correspondence edition exists to search: the item is a catalogue-described cipher
notebook, not a letter, and has no named correspondent (only the pencilled "Baptiste Romin or Romain" and the
Urquhart-fragment copyist Robert Mylne, neither a sender in the CLAUDE.md rule-1 sense). Google Books
(`googleapis.com/books/v1/volumes`, with `GOOGLE_BOOKS_KEY` appended as CLAUDE.md's Access playbook specifies)
returned HTTP 403 "Cannot determine user location for geographically restricted operation" on every query —
blocked, not a negative. HathiTrust full-text search (`babel.hathitrust.org/cgi/ls`) returned HTTP 403 to curl;
the browser-tool workaround in CLAUDE.md's Access playbook was not tried in this bounded pass — blocked, not a
negative.

**3. Community lists (searcher 3).** Cipherbrain's "List of Encrypted Books" and "111 encrypted books" pages
(scienceblogs.de/klausis-krypto-kolumne, Klaus Schmeh) were fetched and read for every listed entry, not just
top-level snippets: no entry names Scotland, NLS, Edinburgh, Baptiste, Romin/Romain, or MS.20769, and no
entry's symbol-set (Roman + Greek + astrological + invented) matches — closed-negative, confirmed independently
by searcher 1's identical read of the same two pages. Cipherbrain's own site search for "Scotland" turns up only
unrelated posts (Charles I letters, encrypted gravestones, an IRA postcard, a BBC-covered student cryptogram).
Cipher Mysteries (ciphermysteries.com, Nick Pelling) site-searched for "National Library of Scotland" and
"Scotland": the only hit is an unrelated 14 Sept 2018 article on Netta Fornario's 1929 papers — closed-negative,
confirmed independently by searcher 1. The local Cryptiana snapshot (`sources/cryptiana/`, downloaded 19 Sept
2026 per its README, Yoshimasa Tomokiyo's site) has zero occurrences of "20769" and every "Scotland"/"Romin"/
"Romain" hit is an unrelated proper name or place (Moray-Wood Cipher, the Charles IX-du Croc letter,
"abbé de Saint-Romain," "le roy des romains") — closed-negative. MysteryTwister C3's live challenge list
redirected (mysterytwisterc3.org → mysterytwister.org) and was checked only via web search, not a direct page
read after the redirect — unchecked, not a negative. r/codes returned HTTP 403 to direct curl and was checked
only through web search's indexing of Reddit, not a direct subreddit crawl — unchecked, not a negative.

**4. DECODE (de-crypt.org) (searcher 4, reconciling searchers 1 and 2).** Searchers 1 and 2 found the
record-browsing app's REST API returns HTTP 401 unauthenticated and read this as a login wall; searcher 4 went
further and used the site's own public web search form directly (`POST .../RecordsSearch` with the page's own
CSRF token, as an anonymous session, `userlevelid=-2`), first confirming the mechanism works with sanity queries
that return real non-zero hits (e.g. holder "Vatican," country "United Kingdom"), then running it against the
shelfmark, holder, sender/receiver/author/owner name fields, and a geographic sweep (region "Scotland," city
"Edinburgh," free-text "Scotland"): every direct shelfmark/name query returned 0 records, and every one of the
23 geographic hits was fetched and individually checked (British Library or Kew holdings, Elizabethan-era
diplomatic correspondence) — none is NLS, none matches MS.20769, Baptiste Romin/Romain, Urquhart, or Mylne.
This is a real, exercised negative on DECODE's public catalogue, not merely an unreached login wall — it
supersedes searcher 1's "blocked" characterization of the search itself, though searcher 1's finding that the
REST API and any login-gated content return 401 unauthenticated still stands. Per the orchestrator's explicit
instruction, login with `DECODE_USER`/`DECODE_PASS` was **not attempted by any of the six searchers** (flagged
as currently rejected server-side, with a lockout risk on retry) — DECODE's authenticated content, if any exists
beyond the public catalogue, remains unchecked, not a negative.

**5. github.com/dbourdeau/cyphersolver (searcher 5).** Fresh shallow clone, HEAD `bea09bee`, 19 Sept 2026.
Whole-repo greps for "20769", "National Library of Scotland," "Romin"/"Romain"/"Baptiste," and "Urquhart"/
"Pantochron" all checked by hand for false positives (the few "20769" substring hits are inside unrelated
record numbers and floating-point values). Zero genuine hits — closed-negative. The repository does have a
target folder named `urquhart/`, read in full (`NOTES.md`): this is Sir Thomas Urquhart's own two printed
numeric cryptograms (the "Cyphral Octastich," read by Daniel Bourdeau as a book cipher on Urquhart's 1652 *The
Jewel*, and the "Cyphral Distich," which does not reproduce) on the last leaf of his own printed books — a
different item from MS.20769 (printed cryptogram vs. manuscript symbol alphabet), related only by the shared
surname; no mention anywhere of MS.20769, NLS, Romin/Romain, or Mylne. Noted to avoid future confusion, since
searcher 1 independently flagged the same printed-Urquhart item as a near-miss under a different name (the
"Cyphral Distich," reported solved by Claude Fable 5.1, 14 Sept 2026 coverage).

**6. github.com/aaymeloglu/unsolved-ciphers and github.com/robertpitt/\* (searcher 6).** Shallow clone, HEAD
`837075e0`, 19 Sept 2026: zero hits for "20769," "National Library of Scotland," "Romin," or "Romain" anywhere
in the repo, confirmed by both content grep and filename search — closed-negative. The repo's only
Scotland-adjacent content is unrelated 16th-century Anglo-Scottish diplomatic ciphers from de-crypt.org's own
harvested catalogue (British Library shelfmarks) and its own `moray-1568` target, and its only Urquhart content
is the printed 1653 *Logopandecteision*/1834 Maitland Club reprint (the same printed-cryptogram item as in
searcher 5's finding, at a different NLS shelfmark, H.32.a.39) — not MS.20769. Robert Pitt's 40 public
repositories (not one of the two solver repositories CLAUDE.md names, checked as extra coverage via the GitHub
search API) include three cipher-history projects (Forster 1644, Charles I-Boswell 1643, Le Tellier 1657), none
matching this target; code search for "20769," "National Library of Scotland," and "Urquhart" scoped to his
account returned zero genuine hits — closed-negative.

**Proceedings of the Society of Antiquaries of Scotland (1949-50, vol. 84), the print source most likely to
carry a note of the 1949 deposit.** Both searcher 1 and searcher 2 tried this independently and both were
blocked: the Archaeology Data Service's PSAS volume/query and contents tools
(`archaeologydataservice.ac.uk/archives/view/psas/query.cfm` and `.../contents.cfm?vol=84`) returned HTTP 403 to
both curl and WebFetch with a browser user-agent, the same block pattern already logged for manuscripts.nls.uk
in this file; no full-text copy of vol. 84 was found on Internet Archive by title or by guessed collection id.
**Unchecked, not a negative** — whether the Proceedings note the 1949 deposit, by shelfmark or by the Society of
Antiquaries as depositor, remains unknown.

**Romin/Romain genealogy and local history.** Searchers 1 and 2 both searched "Romin"/"Romain" together with
Scotland, genealogy, and cipher/coded-manuscript terms: no genealogical or local-history source connects either
spelling to a coded manuscript; hits are limited to the NLS catalogue text itself and unrelated persons (a
17th-century French engineer named Le Romain) — closed-negative, though this is a web-search-only check, not a
search of a dedicated Scottish genealogy database.

**Verdict:** No third-party discussion, prior decipherment attempt, solve claim, or DECODE catalogue record for
NLS MS.20769 was found by any of the six sweeps, across every source family CLAUDE.md rule 1 and this target's
brief name except the printed 1949-50 PSAS Proceedings and DECODE's authenticated content, which remain
unchecked (not negative) — the target stays **open**, and the scout's original "no relevant hit" finding is
confirmed and substantially strengthened.

## NLS reply, 24 Sept 2026 (closes the target)

The National Library of Scotland's Access Team answered the enquiry of 23 Sept 2026 (outreach/nls-20769-enquiry.md) on
24 Sept 2026: MS.20769 is not a cipher. A researcher recently examined it and identified the text as Mi'kmaw
hieroglyphs. Revised catalogue description, as sent by NLS: "A prayer book written in Mi'kmaw hieroglyphs, used by the
Mi'kmaq, an indigenous people of Nova Scotia. The text appears to be divided into sections by horizontal lines. The name
Baptiste Romain is added in pencil on folios 27 and 28 (inverted). Romain served the missionary Pierre Maillard. Loosely
enclosed is a fragment of a copy by Robert Mylne of Sir Thomas Urquhart's Pantochronochanon (London, 1652). This
bifolium, paginated 33-36, contains numbers 98-113 of the 'genealogy' of the Urquharts." Creation: 1652, 18th century;
57 leaves, oblong quarto and octavo; 27 + blank + 28 (inverted) + ii folios; deposited 1949 by the Society of
Antiquaries of Scotland. Copies could be ordered through the copy enquiry form (minimum charge eight scans) or taken
by phone in the reading room, but none is needed.

Outcome: closed-negative. The old "Unidentified text, apparently 18th century, written in cipher" description that
put the item on Cryptiana's list and in our queue is superseded by the library's own re-identification. Maillard's
Mi'kmaw hieroglyphic prayer books are a known genre (the script is a writing system, not a cipher); nothing here is
ours to read. Credit for the identification belongs to the researcher NLS names and to the library. No copy order,
no further work. Lesson for check-solved: a catalogue "in cipher" on an undigitised item is a cataloguer's guess
until someone has seen the leaf; an enquiry to the holding library costs one email and settled this in a day.
