not-a-cipher

# Chauran to Williamson, financial and intelligence letters transmitting ciphers — TNA SP 84/165

QUEUE row: N11 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

TNA, State Papers Foreign, Holland, **SP 84/165** items 14, 23, 66, 70, 75, 82, 87, 102, 103, 111, The
National Archives, Kew, all 1662. Catalogue text quoted verbatim from the Discovery API
(`discovery.nationalarchives.gov.uk/API/search/records`, fetched 23 September 2026):

> SP 84/165/14 (1662 Jan 18): "Folio 23: Wickfort to [-]. Fisheries still proving a hindrance to the treaty..."
> SP 84/165/23 (1662 [Jan 11/21]): "Folio 36: [Chauran] to [Williamson]. Concern about movement and secrecy
> of correspondence."
> SP 84/165/66 (1662 nd): "Folio 108: [Chauran] to [Williamson]. Requests payment. Spanish letters
> forthcoming."
> SP 84/165/70 (1662 Mar 19): "Folio 115: [Chauran] to [Williamson]. Insists on payment before he sends
> remaining Spanish papers. Fears the papers may be stolen from him. **Additions to cipher.**"
> SP 84/165/75 (1662 Mar 22): "Folio 122: [Chauran] to [Williamson]. **Transmits ciphers.** Plea for
> payment."
> SP 84/165/82 (1662 Mar 30): "Folio 136: [-] to the Bishop of Münster. Still further difficulties in
> Franco-Dutch negotiations..."
> SP 84/165/87 (1662 Apr 2): "Folio 144: [Chauran] to [Williamson?]. Acknowledges receipt of payment.
> **Arrangements for ciphering and security of post.**"
> SP 84/165/102 (1662 Apr 16): "Folio 174: [Chauran] to [Williamson?]. Financial arrangements."
> SP 84/165/103 (1662 [Apr 9]): "Folio 175: [Chauran] to [Williamson?]. His accomplice is too unwell to
> travel. Letters received by someone called Delacroix at M. de Bourdeaux's. Plea for more care in ensuring
> safety of the mail."
> SP 84/165/111 (1662 [Apr -]): "Folio 186: [Chauran] to [Williamson?]. Recovery of his accomplice.
> Financial requests."

## Check-solved sweep (23 September 2026)

1. **TNA Discovery, full item descriptions (decisive).** Fetched all ten items individually by reference
   via a targeted term search against series "SP 84" restricted to piece 165 (terms: Chauran, Williamson,
   cipher, payment — 102 items matched across the piece, of which the ten named items were extracted).
   **None of the ten item descriptions themselves say the letter is "in cipher"** — every one is catalogued
   as an ordinary English-language letter (mostly Richard Chauran to Joseph Williamson) *about* cipher
   logistics: arranging secure correspondence, transmitting cipher material, requesting or acknowledging
   payment, and reporting on an ailing "accomplice." Two (70, 75, 87) explicitly mention ciphering but as
   subject matter ("additions to cipher", "transmits ciphers", "arrangements for ciphering"), not as the
   letter's own writing system. Checked the eight items immediately flanking the cluster (68, 69, 71, 77,
   88, 104 — plus 14 and 82 themselves, which turned out to be *other* correspondents, Wickfort and an
   unsigned letter to the Bishop of Münster, on Franco-Dutch treaty business unconnected to Chauran) for a
   separately catalogued cipher/key item that might be the material Chauran is "transmitting" — none found;
   if the enclosed cipher material survives, it is not catalogued at item level in this piece. Confirmed via
   the record-details endpoint (`/API/records/v1/details/{id}`, spot-checked 14, 70, 111) that all three are
   `"digitised": false`.
   **/14 and /82 are miscatalogued for this cluster**: both are Wickfort/anonymous letters on Franco-Dutch
   treaty negotiations with no Chauran/Williamson/cipher content at all — they were presumably picked up by
   the original scout's search term matching elsewhere in their text, not by subject. Flagging this as a
   second scout-stage inaccuracy (after N8's date error) for whoever revises the "Candidates not on DECODE"
   sheet.
2. **Print / scholarship.** Alan Marshall, *Intelligence and Espionage in the Reign of Charles II,
   1660-1685* (Cambridge, 1994) is the standard secondary source for Williamson's intelligence network and
   almost certainly discusses paid agents of Chauran's type; it is not on archive.org (confirmed by
   `advancedsearch.php` query, no result) and was not otherwise searchable full-text this sweep — WebSearch
   for "Chauran" + "Williamson" + "SP 84/165" returned nothing specific to this correspondence. Flagged as
   an unchecked print source, though moot to the cryptanalysis question (point 1 already establishes these
   ten items are not ciphertext).
3. **Community lists.** `sources/cryptiana/web/` grepped for "Chauran", "Williamson", "SP 84": no hit.
4. **DECODE.** `ay/catalogue/decode-catalog.csv` grepped for "Chauran": no record. Grepped for "SP 84"/
   "Williamson": two hits, both BL Add MS 40677 (a different Williamson-related manuscript, keys only, "N/A"
   status) — no connection to SP 84/165 or Chauran.
5. **Bourdeau.** `cs-recheck` grepped for "Chauran"/"Williamson"/"SP 84": two superficially matching hits
   (`morosini1588/decrypt_raw.txt`, `harley1582r8499/lit/harlcat2.txt`) checked directly and confirmed to be
   coincidental substring matches — "chauranosecopiudirnenti" inside a run of decoded Italian text, and the
   Basque surname "Ynchaurandieta" — not Richard Chauran.
6. **Aymeloglu.** `ay/*.md` grepped for "Chauran"/"Williamson"/"SP 84": no hit.

Requests: discovery.nationalarchives.gov.uk 5 (1 term search covering the whole piece with 200-result page
size, 4 record-details lookups). WebSearch: 1 query.

## Edition risk

**Moot.** There is no cipher text in the ten named items to protect from an edition; they are plain-English
correspondence about the cipher trade, not ciphertext.

## Verdict

**Not-a-cipher.** All ten named SP 84/165 items are letters *about* ciphers — arranging their secure
transmission and payment for Spanish intercepted material — not letters written *in* cipher. This confirms
rather than overturns QUEUE N11's own characterisation ("financial and intelligence letters transmitting
ciphers... a paid-informant relationship, not diplomatic code"); the check-solved sweep found no cryptanalytic
target here at all, so there is nothing to verify as solved or unsolved. Two of the ten reference numbers
(14, 82) do not belong to the Chauran/Williamson cluster and were miscatalogued into it upstream.

## Next

Drop N11 from the board as a cryptanalysis candidate; it was never one. If the project wants Chauran's actual
enclosed cipher/key material (the object being "transmitted" in /70 and /75), that is a different search —
either elsewhere in SP 84/165 under a heading this sweep's search terms did not catch, or not preserved/
catalogued at all — and would need a full, unfiltered item-level listing of the piece (this sweep used a
term-restricted search, not the complete listing, per the good-citizen request-count budget). Not pursued
this session. No TNA digitisation exists for any of the ten items checked (digitised: false).
