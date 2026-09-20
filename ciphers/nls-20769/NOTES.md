# Unidentified 18th-century cipher/symbol manuscript (National Library of Scotland, MS 20769)

- **Status:** open. **Caveat before any campaign:** the catalogue record could not be loaded directly from
  this environment (see below); its wording comes from repeated, identical search-engine snippets, not a
  first-hand read. The proposer's "57 leaves" figure is **unverified** — no snippet gave a leaf/folio total.
  Whether this is a true substitution cipher or a private/occult notation (shorthand, alchemical sigla used
  non-cryptographically) is also unresolved — see "Is it actually a cipher?" below. Both must be settled,
  ideally by the person reading the live catalogue page, before any reproduction is ordered.
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

Before ordering scans: get someone who can load manuscripts.nls.uk to read the live record (confirm shelfmark
form, true extent, full physical description, provenance) and, if possible, ask NLS reprographics directly
whether their own cataloguer would call this a cipher or a private notation/shorthand. If leaf count and
"cipher" status both hold, this would be the largest genuinely open target in the project's queue and worth the
roughly £100-200+ (unconfirmed) full-manuscript scan order; if it turns out to be shorthand or an occult
notebook, it is out of scope for a substitution-cipher attack.
