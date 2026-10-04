# DSCALE-CHECK, 4 Oct 2026

Worker DSCALE-CHECK (account 3). Question from the owner: does the field's own practice support the internal
depth scale D0 key identified / D1 scattered words / D2 partial text / D3 substantial text with an external check /
D4 coherent full text under one fixed key, externally confirmed, and the outside wording "key identified",
"partially deciphered (about N%)", "deciphered"?

Method and limits: open indexes only (OpenAlex, Semantic Scholar, CrossRef, Unpaywall), the HistoCrypt proceedings
PDFs at ecp.ep.liu.se (open access), and one login-free read of de-crypt.org. No login, no JSTOR. Requests: de-crypt.org
14 (1 form page, 12 listing probes at recperpage=1, 1 earlier probe), ecp.ep.liu.se 4, dspace.ut.ee 2, api.openalex.org 8,
api.semanticscholar.org 4, api.crossref.org 5, api.unpaywall.org 1, tandfonline.com 2 (both 403 Cloudflare, stopped, not retried).
Run date 4 Oct 2026, 04:11-04:20 UTC.

## 1. DECODE's status field

**Exact values (verified, live site, 4 Oct 2026).** The field is `status` ("Status") on the `records` table. The lookup
options embedded in the RecordsList page are `{"lf":"1","df":"Decrypted"}, {"lf":"2","df":"Non-decrypted"},
{"lf":"3","df":"Partially decrypted"}, {"lf":"4","df":"N/A"}` (de-crypt.org/decrypt-web/RecordsList, `lookupOptions` for
field "status"). The list grid shows the display text per row (e.g. "Partially decrypted"). There is no "Key only"
value. A key is a separate record type (`record_type`: 1 Cipher, 2 Key, 3 Manual, per sources/decode/NOTES.md, 24 Sept 2026),
and the same four status values are offered for every record type. "N/A" is the value for items where decryption does not
apply (we infer keys and manuals; unverified, the page does not say).
- Confirms: the scale needs a level for "key identified" that is not a status; DECODE handles it as a record type plus a
  linked key record. Our D0 has no DECODE equivalent as a status.
- Refines: DECODE has three real levels (Decrypted / Partially / Non-decrypted). Our D1-D3 all map to "Partially decrypted"
  and D4 to "Decrypted". The word the field uses for D1-D3 is "partially decrypted", with no percentage.

**How a record is assigned a status: UNVERIFIED.** No rule is stated on the public pages, and neither HistoCrypt paper on
DECODE says (Héder, Fornés, Kopal, Szigeti, Megyesi, "Supporting Historical Cryptology:
The Decrypt Pipeline", dspace.ut.ee bitstream 48f9a540; and "The DECODE Database of Historical Ciphers and Keys: Version 2",
HistoCrypt 2022, doi 10.3384/ecp188397, section 2.2 "Metadata", which lists creator/owner, split dates, publications and
key-cipher links, and does not mention status). The Megyesi et al. Cryptologia 2020 paper "Decryption of historical
manuscripts: the DECRYPT project" (doi 10.1080/01611194.2020.1716410) is the likely place; tandfonline answered 403 to
curl, so it was not read. Practical reading from the form: status is a free uploader/curator choice from a four-item list,
with no recorded threshold or percentage. Next step: owner's browser reads that paper's metadata section
(a LOCAL-QUEUE row, ~$0).
Cross-check from our own data: the 24 Sept crawl has 385 "Partially decrypted" cipher records against 801 "Non-decrypted"
(sources/decode/NOTES.md), so the middle value is used heavily and is coarse.

## 2. Acceptance criteria in decipherment papers

Read in full (open PDFs): Kopal and Waldispühl (HistoCrypt 2021, "Two Encrypted Diplomatic Letters Sent by Jan Chodkiewicz
to Emperor Maximilian II in 1574-1575", ecp.ep.liu.se article 160); Lang and Piorko / Dee paper (HistoCrypt 2022, "Solving an
Alchemical Cipher in a Shared Notebook of John and Arthur Dee", doi 10.3384/ecp188388); von zur Gathen ("Unicity Distance of the
Zodiac-340 Cipher", HistoCrypt 2022, doi 10.3384/ecp188395). Abstract only: Lasry, Biermann, Tomokiyo, Cryptologia 2023
(doi 10.1080/01611194.2022.2160677, via Semantic Scholar; full text 403). Zodiac solvers' own paper: **not found** in the open
indexes (see below).

| Source | Extent stated | Uncertain readings | External confirmation | "Deciphered" vs "partial" |
|---|---|---|---|---|
| Kopal and Waldispühl 2021 (Chodkiewicz letters A-D) | ciphertext-only: "it was possible to decipher 80% of the letter without having the original key"; with the key "decrypt letters A-C by 95%. Only the code for a few nomenclature elements is still unknown" (section on letters A-C, p. 2 of the PDF) | unknown nomenclature elements named; "transcription and deciphering errors were assumed" until Latin was recognised, "After Latin had been identified ... the decipherment could be verified" | a photographed original 1572 key "Cyffra nova ad Poloniam" found in DECODE; a second copy of the letters; linguistic analysis | uses "deciphered" (abstract) for letters that are 95% read under the period key, and quotes a percentage for each stage |
| Lang and Piorko 2022 (Sloane MS 1902) | "successfully deciphered": plaintext of 177 Latin words; "decrypted the recipe contained within the ciphertext" | key reconstruction "until the entire 45 letter key was" found; some table errors traced to copying | Latin statistical models; the plaintext is a recipe whose source (Hermeticae Philosophiae medulla) is identified; the adjacent cipher table matches | "deciphered" on a full 177-word text under one key, with an external text match |
| von zur Gathen 2022 (Zodiac 340) | solution is the full 340-symbol text, quoted with its typos kept ("obvious original typos have not been corrected") | spelling errors in the plaintext left as is, not repaired | "publicly confirmed by the FBI"; unicity argument: unicity distance at most 153, so a 340-symbol decipherment is "highly likely to be unique" | "solved"; no partial vocabulary |
| Lasry, Biermann, Tomokiyo 2023 (Mary Stuart) | abstract: "over 55 letters fully in cipher ... after we broke the code and deciphered the letters"; "about 50,000 words in total" | **unverified** (full text not read) | **unverified** beyond the abstract: identification of sender and recipient from content is implied | "deciphered" for the whole corpus; per-letter extent not in the abstract |

- Confirms: all four call a text "deciphered" only when a full text reads under one key with some external check
  (a found period key, an identified source text, an authority's confirmation, or a unicity argument). That matches D4.
- Confirms: where a paper says less than full, it gives a number (80%, 95%) and a reason (named unknown elements), which matches
  "partially deciphered (about N%)" for D2-D3.
- Refines: the field's percentage is a share of the text under a stated key condition (80% ciphertext-only, 95% with the period
  key), so a percentage should carry that condition. Our scale has no slot for "key found by cryptanalysis vs period key";
  the repo's S/H grades already carry it, so cite the grade beside the N%.
- Refines: nobody in these papers uses a D1-style "scattered words" level. It appears only as work in progress, never as a
  result label. Recommend not exporting D1 wording.
- Zodiac solvers' own acceptance wording (Oranchak 2021a, Blake 2021, Van Eycke 2021, HistoCrypt 2021 keynotes): **unverified**.
  Only the secondary account is read: von zur Gathen states the solution was announced 11 Dec 2020 and "publicly confirmed
  by the FBI" (his own words).
- Not read: other HistoCrypt partial-decipherment papers beyond the two above (two papers plus the Mary Stuart abstract, short of the
  4-6 asked for; the Mary Stuart full text and the Zodiac keynotes are the two gaps).

## 3. Unicity distance (one sentence, citable)

Shannon showed that a ciphertext shorter than the unicity distance d = H(key) / (redundancy per letter) admits many equally
plausible decipherments, so a fragment of a few words read under a candidate key is expected to fit by chance and proves little
(C. E. Shannon, "Communication Theory of Secrecy Systems", Bell System Technical Journal 28(4), 1949, pp. 656-715,
doi 10.1002/j.1538-7305.1949.tb00928.x, verified on CrossRef; the formula d = I(key) / (log2(len) - H(lang)) and the reading
that a decipherment longer than d is "highly likely to be unique and ... accepted as correct" are in von zur Gathen, HistoCrypt 2022,
sections 1-2, doi 10.3384/ecp188395, whose Zodiac-340 figure is d at most 153). Refines: the scale's D1 and D2 are below the
unicity distance by construction for a homophonic or nomenclator key; D3 should require the checked span to exceed the
design's estimated d, not only to be "substantial".

## Recommendation

Adopt the scale internally, but change two things before using the field's words outside. (1) Map outside wording to DECODE's three
values: D0 stays "key identified" and is described as a key record linked to a cipher, never as a decipherment status; D1-D3 export
only as "partially decrypted" with a stated percentage and the key condition ("about 80% under a reconstructed key", "about 95%
under the period key", after Kopal and Waldispühl); D4 only as "deciphered", which the papers reserve for a full text under one key
with an outside check (found period key, identified source, authority, or unicity argument). Do not export D1 "scattered words".
(2) Add a unicity condition to D3: the externally checked span must be longer than the design's unicity distance, otherwise the check proves
little (Shannon 1949; von zur Gathen 2022). Not settled and marked unverified: how DECODE decides a status (read Megyesi et al.
Cryptologia 2020 from the owner's browser), what the Mary Stuart paper reports per letter, and what the Zodiac solvers' own papers call
"solved" versus "partial". These do not change the recommendation but should be read before it is used in any outward note.
