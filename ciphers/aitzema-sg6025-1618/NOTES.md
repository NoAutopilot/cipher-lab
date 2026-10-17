open
Resolutien der Staten-Generaal Nieuwe Reeks Deel 3 (1617-1618, GS152) pp.188, 289, 307, 351 (res. 1178/1178a, 1789, 1923, 2305/2305a) read in full by this worker via resources.huygens.knaw.nl/retroboeken/statengeneraal (`searchText` accessor pages.json lookup, pages fetched directly, no keyword search needed since the pages were already named in the harvest).

QUEUE row: SCOUT-KEYS K2 (QUEUE.md "## Key-beside-cipher candidates (17 Oct 2026)"; harvest/SCOUT-KEYS-2026-10-17.tsv).

## Target

Foppe van Aitzema, Dutch resident/agent for the States General at the Hanse towns (Lübeck, Hamburg), 1617-1625.
Nationaal Archief 1.01.02 (Staten-Generaal) inv. nr. 6025, "Liassen Agent Aitzema", 1617-1625, 589 scans,
digitised (`isDownloadable: true`, confirmed via the item page's own `drupal-settings-json`; title field reads
"Ingekomen brieven en stukken van Foppe van Aitzema, resident van de Staten-Generaal bij de Hanzesteden,
1671-1637" [sic, a typo for 1617-1637 in the NA's own metadata] -- "Beschrijving"/"Snippet" fields on the item
page are both empty, so the catalogue record itself carries no cipher flag; the cipher evidence is entirely in
the printed Resolutien, not the finding aid).

## Resolutions read (this worker, 17 Oct 2026)

- **Res. 1178/1178a (p.188, [no day given on this page extract; the surrounding entries 1176-1190 are dated
  mid-July 1617]):** "De instructief geloofsbrieven, pasbrief en akte van traktement voor Foppius Aissema tot
  Alsem worden vastgesteld. De griffier zal de door Aissema gemaakte code opbergen (1147, 1189)." Footnote
  1178a: "A.R.A., S.G. 6025 (minuut en kopie; de minuut met verbeteringen van de hand van Oldenbarnevelt) en
  12.453 no. 50." This footnote cites the archival source of the *resolution text itself* (draft and copy),
  not necessarily the code's storage location -- it is ambiguous whether "opbergen" (file away) sent the code
  into inv. 6025 alongside this resolution's own minuut/kopie, or elsewhere. Res. 1189 (same page): "Foppius
  van Aissema tot Alsem legt de eed af als agent bij de Hanzesteden" -- confirms Aitzema took his oath as agent
  shortly after, consistent with mid-July 1617.
- **Res. 1789 (p.289, 5 Dec 1617):** "De ontcijferde brief van Aitzema wordt gelezen (1780, 1791)." No footnote
  on this page pins a specific archival pointer for this letter (no "1789a" found in the apparatus read).
  Res. 1791 (6 Dec): "Eveneens het antwoord op de brief van Aitzema (1789)" -- the States General's reply was
  being drafted.
- **Res. 1923 (p.307, dated by position between res. 1921-1924, early Jan 1618 -- the entries bracketing it
  cite 23 and 30 Dec 1617, so 1923 itself falls in the first days of January 1618):** "De volgende brieven
  worden gelezen: a. De ontcijferde brief van Aitzema, twee dagen eerder ontvangen; b. van Brederode, dd. 23
  dec. 1617a; c. van Bilderbeke, dd. 30 dec. 1617." Footnote "1923a" on this page points to "A.R.A., S.G. 6018
  (orig.)" -- but that footnote attaches to item (b), Brederode's letter (inv. 6018 is Brederode's own lias,
  not Aitzema's), not to Aitzema's deciphered letter in item (a). No separate footnote for (a) is printed here.
- **Res. 2305/2305a (p.351, dated by position in the Feb 1618 run):** "De de vorige dag ontvangen en
  ontcijferde brief van Aitzema wordt gelezen. De Staten zullen hem de volgende dag bespreken." Footnote
  "2305a": "A.R.A., S.G. 6025 (orig. dd. Lübeck 17 febr.; de koning van Denemarken is van plan het bisdom...)"
  [footnote continues past the matched quote in the brief]. This is the one explicit pointer in the four cited
  entries: the *original ciphertext letter itself*, dated Lübeck 17 Feb 1618, is footnoted directly to inv.
  6025 -- the same lias this target's ciphertext lives in.

## Which letters are the known-plaintext pairs

Only **res. 2305 / the 17 Feb 1618 Lübeck letter** has an explicit archival footnote tying a specific original
ciphertext ("orig.") in inv. 6025 to a resolution that states it was received and deciphered the day before.
That is the one confirmed known-plaintext pair this job can name: the cipher original survives (in the lias)
and its 1618 plaintext content (the Danish bishopric business) is summarized in the same resolution. Res. 1789
(5 Dec 1617) and res. 1923 (~early Jan 1618, "received two days earlier" so written ~ late Dec 1617/early Jan
1618) are also described as "de ontcijferde brief van Aitzema" -- deciphered -- but neither has a footnote in
this edition pointing to a specific archival item number for the underlying original; if their originals are
also loose in inv. 6025 (plausible, since it is the lias for all of Aitzema's incoming correspondence in this
date range) that is inferred, not printed. Locating those two specific originals among the lias's 589 scans
would be a leaf hunt, out of this job's scope (brief: "no leaf hunt... this job locates nothing, it only
establishes status and the premise").

The undeciphered target population is: whatever other cipher letters from Aitzema sit in inv. 6025, 1617-1625,
with no resolution naming them as "ontcijferd" -- count unknown without reading the lias itself (the harvest's
own framing, SCOUT-KEYS K2).

## Premise check (CHECK-AITZEMA, 17 Oct 2026)

- **(a) Folder's own prior mentions:** none -- this folder was created by this job; no prior NOTES.md/REQUEST.md/spec existed.
- **(b) Other solvers' working files:** grepped two shallow clones (depth 1) for "aitzema"/"aissema" (case-insensitive,
  word match, not just the "6025" substring, which hits unrelated numeric data/IDs in both repositories --
  confirmed by inspection, e.g. aymeloglu's `catalogue/decode-catalog.csv` row "6025" is an unrelated Florence
  1541-1546 Italian-plaintext DECODE record, not Aitzema). **Zero matches for the name** in
  github.com/dbourdeau/cyphersolver or github.com/aaymeloglu/unsolved-ciphers. Not found.
- **(c) Physical neighbours:** not checked -- out of scope per this job's "no leaf hunt, no images" instruction;
  would require opening inv. 6025's own scans.
- **(d) Recipient-side editions:** not applicable in the usual sense -- the "recipient" here is the States
  General itself, and its own register (the Resolutien SG, read above) *is* the recipient-side record; there
  is no separate foreign recipient archive to check for this correspondence direction.
- **Is the 1617 code (res. 1178's "code... opbergen") extant?** The brief named NA inv. 12578.1 as a candidate.
  Checked the NA item page for 1.01.02 inv. 12578.1 directly: it exists, but its title is "Sleutel geheimschrift
  'Rangh van de grootte tot Constantinopelen voornaempste gouvernementen, principaelste steden, ministers van de
  Christelijke en Mahometaense potentaten...'" -- an Ottoman/Constantinople-ranking cipher key, 0 scans (not
  digitised), unrelated to the Hanse-towns agent. **This rules out 12578.1 as Aitzema's code**; it is almost
  certainly a Haga/Constantinople-correspondence key instead (consistent with CHECK-HAGA's and HEID-1621E's
  notes on inv. 6894/12578.1 elsewhere in ROOM.md). Where Aitzema's own 1617 code actually sits (within inv.
  6025 itself, under a different inventory number, or lost) is not established by this job -- footnote 1178a's
  "12.453 no. 50" is the resolution's own source citation, not confirmed as the code's location, and chasing it
  further (a different NA item page, or the inventory's own index) would start to be a leaf/key hunt beyond this
  job's cap and host list.

## Web and blog check (CHECK-AITZEMA, 17 Oct 2026)

Four plain web searches: (1) "Foppe van Aitzema cipher letters Hanzesteden agent decipher" -- no hit on ciphers,
only biography (Wikipedia, Deutsche Biographie, dbnl); (2) "\"Aitzema\" cijfer gecijferde brief 1617 1618
Staten-Generaal 6025" -- no hit naming the item or a cipher; (3) "Foppe van Aitzema agent Lübeck 1618 decoded
cipher Nationaal Archief 1.01.02 6025" -- no hit (one irrelevant result, a 1646 Portuguese-spy ciphertext
paper); (4) "\"Aissema tot Alsem\" code cipher key griffier 1617" -- no hit naming this document or key (general
background on 17th-c. Dutch/Habsburg ciphers only). Blog site searches: `site:scienceblogs.de
klausis-krypto-kolumne Aitzema` -- blog-listing pages only, no post names Aitzema; `site:cryptiana.blogspot.com
Aitzema` -- no hit (off-topic results only, search engine may not index this blog for this term); `site:
ciphermysteries.com Aitzema` -- no hit. No comment thread opened since no plausible hit surfaced on any of the
three blogs.

## DECODE / solver-repository cache check (CHECK-AITZEMA, 17 Oct 2026)

- **DECODE listing cache** (`sources/decode/`, and aymeloglu's own `catalogue/decode-catalog.csv` mirror of the
  DECODE catalogue): grepped for "aitzema"/"aissema", case-insensitive -- zero hits in either. DECODE's
  RecordsList is public without login (per `tools/decode_list.py`'s docstring); no live re-crawl was run this
  job (would be a fresh host hit beyond the cached grep, not needed since the cache already covers the DECODE
  catalogue and returned nothing).
- **Bourdeau** (`github.com/dbourdeau/cyphersolver`, shallow clone): zero hits for the name (see Premise check
  (b) above).
- **Aymeloglu** (`github.com/aaymeloglu/unsolved-ciphers`, shallow clone): zero hits for the name (see Premise
  check (b) above).
- **Cryptiana** (`sources/cryptiana/`, local snapshot): grepped for "aitzema"/"aissema" -- zero hits.

## Verdict

**open**, confirmed unsolved as far as this check-solved pass can tell: six sources read (web x4, three blogs,
Resolutien SG NR3 read directly at all four cited pages, DECODE cache, Bourdeau, Aymeloglu, Cryptiana), none
found a decipherment, key, or prior-solve claim for any *undeciphered* Aitzema letter in inv. 6025. The premise
check found no reason to treat this as already done or as a duplicate-effort risk, and corrected one piece of
the harvest's framing: NA inv. 12578.1 is not Aitzema's code (it is an Ottoman/Constantinople key, 0 scans),
so the 1617 code's own location is still unknown, not merely unconfirmed.

One confirmed known-plaintext pair exists in the resolutions (res. 2305, the 17 Feb 1618 Lübeck original in
inv. 6025, deciphered per the same resolution); two more deciphered letters are named (res. 1789, 5 Dec 1617;
res. 1923, received ~early Jan 1618) without a footnoted archival pointer to their originals. The undeciphered
population (other Aitzema cipher letters in the 589-scan lias with no resolution naming them "ontcijferd") has
an unknown count.

This target is `open`, not `blocked` or `partial`: nothing here waits on a person, an image, a key or an
edition outside this session's reach, so no "## While waiting"/"## Remaining gaps"/"## Escalation" section
applies (CLAUDE.md rule 5's "Finish or name the blocker" amendment, and `tools/gaps_check.py`'s own docstring,
are for a `partial` target's parked gaps, not an `open` one with a named unblocked next step).

Next test, unblocked: a stride contact sheet of inv. 6025 (589 scans) sampled across the 1617-1618 run for
cipher-block presence (cipher yes/no per sampled scan, the same method CHECK-HAGA/HAGA-LEAF used on inv.
6896), ~USD 2; or, cheaper first, one more NA item-page check for a plausibly-numbered "Sleutels geheimschrift"
or "Chiffres" sub-series near inv. 6025/12578 to re-attempt locating the 1617 code before any scan sampling,
~USD 0.5 (one item-page fetch).

## AITZEMA-SHEET (17 Oct 2026)

Stride contact sheet of all 589 scans, following CHECK-AITZEMA's named next step. The item page's own
`drupal-settings-json` (`viewer.response.scans[]`) gives `order`, `uuid`, `default.url` (native JPEG),
`thumbnail.url` (`service.archief.nl/api/file/v1/thumb/{uuid}`) and `iiif.url` directly per scan -- the
thumbnail route is a single field read, no derivation or extra request needed (answers the brief's "say
which"). isDownloadable: true confirmed again; 589 scans confirmed again.

**Sample:** stride 10, orders 1, 11, 21, ..., 581 -- 59 of 589 scans (~10%). 1 item-page fetch to
www.nationaalarchief.nl + 59 thumbnail fetches to service.archief.nl, >=1.6s apart, 60 requests total
(at the 60-request cap). Thumbnails are small (168-256 px on the long side) -- `images/manifest.json` and
`scans.tsv` record uuid, thumbnail_url and default_url (native-res) per sampled order for any later full-res
re-read. 8 contact sheets (`images/sheet_1.jpg`-`sheet_8.jpg`, 7-8 thumbnails each, order labelled) built with
PIL and read; `scans.tsv` has order/uuid/cipher/decipherment/note per scan.

**Result: 0 of 59 sampled scans show a clear cipher block (numeral or symbol groups) at this stride and this
resolution.** 2 scans (orders 131, 221) are marked `unsure`: 131's left page is heavily stained/darkened
(damage or bleed-through, not legible either way at thumbnail resolution); 221 has curved ink/pencil bracket
marks along the right-page margin that are not legible as cipher or as anything else at this resolution. The
other 57 are ordinary Dutch cursive letters (2pp each), several folded outer-cover/docket sheets with red wax
seals (orders 1, 531) or sideways-written address dockets (order 391), two pages under an NA-applied gray
privacy/redaction patch (orders 401, 461, consistent with the same device seen on order 1's seal block), and a
handful of faint/mostly-blank pages (orders 121, 211, 251, 321, 351 partial, 571). No interlinear or marginal
decipherment was seen on any sampled scan. The 17 Feb 1618 Lubeck letter (res. 2305's known-plaintext pair)
was not identified in this sample -- no scan carries a legible date at thumbnail resolution, and none shows a
cipher block to match it against; its specific order within the 589 scans is still unknown.

**Caveat on the negative:** this is a stride-10 sample at thumbnail resolution, not a full pass or a control-backed
negative (rule 3 does not apply here -- there is no matched-control gate for "is a cipher block visible in a
thumbnail", this is a presence/absence sweep, same genre as CHECK-HAGA/HAGA-LEAF). Two limits bound how much
weight the 0/59 carries: (a) stride 10 across an 8-year, 589-scan lias (1617-1625) could plausibly miss a
small number of cipher-bearing leaves if they cluster narrowly (e.g. only the 1617-1618 window, or only a few
loose originals within it) -- CHECK-AITZEMA's own resolution-register finding is that only 1-3 of the lias's
letters are named as deciphered across the whole 1617-1618 run, so cipher-bearing leaves could easily be a
small single-digit fraction of 589 and fall entirely between stride-10 sample points; (b) thumbnails are
168-256 px on the long side -- a numeral/symbol cipher block could in principle be mistaken for dense cursive
at this size, though the two genuinely ambiguous scans (131, 221) suggest the failure mode in practice is
"illegible", not "looks like plain text when it's cipher": every other sampled scan has text dense enough to
read as ordinary joined cursive strokes, visually distinct from the blockier, more separated character shapes
a numeral or symbol cipher produces even at low resolution (compare CHECK-HAGA/HAGA-LEAF's native-resolution
reads on inv. 6896, which did find and rule out several cipher-looking blocks this low-res method could not
have resolved).

**Next step, named:** a full pass at stride 1 on the cipher-bearing runs is not yet applicable since no
cipher-bearing run was found at this stride; instead, either (a) a second stride-10 contact sheet at offset 6
(orders 6, 16, ..., 586) to double the effective coverage to ~20% before concluding presence is unlikely at
this lias, ~USD 2 (same 60-request budget, one item-page re-fetch optional since the scan list is already on
disk); or (b) native-resolution reads (not thumbnails) of the handful of folded-cover/docket scans (orders 1,
381, 391, 531) and the two unsure scans (131, 221), which are the only candidates in this sample worth a
closer look, ~USD 1 (6 native fetches); or (c) if a specific order for the 17 Feb 1618 Lubeck letter can be
found (a finding-aid index, or a date-anchored docket read like HAGA-LEAF's calendar method), read that scan
directly rather than continuing a blind stride sample. (b) is cheapest and lowest-risk to run before (a).

Hosts: www.nationaalarchief.nl (1 request), service.archief.nl (59 requests), >=1.6s apart, 60 total. Vision:
8 contact-sheet reads. No transcription, no decode.
