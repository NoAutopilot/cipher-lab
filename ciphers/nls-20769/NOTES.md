# Unidentified 18th-century cipher/symbol manuscript (National Library of Scotland, MS 20769)

- **Status:** open. **Extent confirmed:** the catalogue record (read 20 Sept 2026, see dated section below;
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
