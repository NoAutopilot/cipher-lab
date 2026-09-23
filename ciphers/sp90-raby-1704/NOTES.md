open

# Raby to Hedges, Reichart to Berlepsch — TNA SP 90/2/335, 337, 348, 409, 409v (1704)

QUEUE row: N13 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

TNA, State Papers Foreign, Prussia and German States, **SP 90/2**, The National Archives, Kew. Catalogue
text quoted verbatim from the Discovery API's item-details endpoint
(`discovery.nationalarchives.gov.uk/API/records/v1/details/{id}`, fetched 24 September 2026), which carries
a `note` field not shown in the search-result `description` used by the original scout pull:

> **SP 90/2/335** (1704 Apr. 29, id C6554808): *scopeContent* "Folio 335: Raby to [Hedges]. Receipt of
> cipher. No news from Prague. Stepney's qualifications for acting in the Bavarian affair. From [Berlin]."
> *note*: "**Partly in cipher.**"
> **SP 90/2/337** (1704 May 6, id C6554809): *scopeContent* "...Court news. No news of Bavarian
> negotiations. Use of ciphers. Swedish Envoy still not received officially..." *note*: "**Partly in
> cipher.**"
> **SP 90/2/348** (1704 May 13, id C6554812): *scopeContent* "Military news. Frederick I is negotiating
> advantageous treaties with Bayreuth and [Brandenburg] Ansbach..." *note*: "**Partly in cipher.**"
> **SP 90/2/409** (1704 June 2, id C6554831): Reichart to [Berlepsch]. *note*: "**Enclosed in SP 90/2 Folio
> 401. French. Copy. Partly in cipher.**"
> **SP 90/2/409v** (1704 June 3, id C6554832): [Reichart] to [Berlepsch]. *note*: "**Enclosed in SP 90/2
> Folio 401. French. Copy. Partly in cipher.**"

**Correction to the QUEUE N13 row and the scout's own description.** The scopeContent summaries for 348,
409 and 409v (used by the earlier scout pull and quoted in QUEUE.md) do not themselves mention cipher at
all — only 335 ("Receipt of cipher") and 337 ("Use of ciphers") do. All five were nonetheless correctly
flagged as cipher items: the item-details `note` field, fetched this sweep, confirms "Partly in cipher" for
all five, including 348, 409 and 409v whose search-result description text gives no hint of it. This is the
reverse of the SP 78 and SP 84 date/miscataloguing errors found earlier this session — here the original
scout call was right, but for reasons not visible in the summary description it used.

## Check-solved sweep (24 September 2026)

1. **TNA Discovery, full-piece sweep for a sibling decipherment.** `tools/discovery_items.py` against
   series "SP 90" piece "SP 90/2" with terms cipher/decipher/undeciphered/duplicate (4 requests) returned
   27 items in the piece; **none** carry "decipher"/"undeciphered"/"key to" in their scopeContent (checked
   by grep). A separate phrase search for "decipher" restricted to record series "SP 90" (1 request, 16
   hits across the whole class) returns items only from **SP 90/5 (1709, 1711) and SP 90/6 (1713-14)** —
   Raby's and his successor Breton's later years — none from SP 90/2 (1703-04). One of those later hits,
   SP 90/5/572 (1711), is explicitly annotated "[decipher interlineated]", showing the cataloguer does add
   that phrase when a contemporary decipherment exists on the document; its absence for the five target
   items and for all 27 other SP 90/2 items checked is real, not a gap in the search. A phrase search for
   "cipher key" restricted to SP 90 (1 request) returned zero hits — no companion decoding-book record
   visible on Discovery for this class (the QUEUE N13 "Next" suggestion to check for one). Item-level
   `digitised` field confirmed **false** for all five target items (from the same detail fetches above).
2. **Print.** The standard printed source for Raby's Berlin correspondence is James J. Cartwright (ed.),
   *The Wentworth Papers, 1705-1739* (1883) — but its own title and the memoir's chronology (confirmed by
   grepping the archive.org djvu text, `wentworthpapers100strauoft`, 2 requests: advancedsearch-equivalent
   direct fetch + grep) cover **1705 onward**; the only 1704 material in the book is a handful of memoir
   asides (dated "1704. June 7", "1704. Nov. 18", "1704. Nov. 29" — none in April-June, none matching these
   five items) in the editor's introduction, not transcribed despatches. No hit for "Berlepsch" or
   "Reichart" anywhere in the volume. The five target letters (Apr-June 1704) fall a year before the
   printed collection's own coverage starts and are not in it. No other printed edition of Raby's 1704
   Berlin despatches or of the Reichart-Berlepsch Bavarian-negotiation channel was found by web search.
3. **Community lists.** `sources/cryptiana/` grepped for "SP 90"/"SP90": no hit anywhere in the cached
   snapshot. WebSearch for "Cryptiana Raby Berlepsch Reichart Bavaria 1704 cipher SP 90": no dedicated post
   or forum thread found.
4. **DECODE.** `ay/catalogue/decode-catalog.csv` grepped for "SP 90"/"SP90"/"Raby"/"Berlepsch"/"Reichart":
   no record.
5. **Bourdeau.** `cs-recheck/CATALOGUE.md` and `SOLVED_CATALOGUE.md` grepped for the same terms: no hit
   (a broad recursive grep of the whole clone matched only coincidental binary/filename substrings, e.g.
   "sp90" inside unrelated PNG filenames — not a real reference).
6. **Aymeloglu.** `ay/CATALOGUE.md` grepped for the same terms: no hit.

Requests: discovery.nationalarchives.gov.uk 11 (4 term-searches on the piece, 5 item-details fetches, 1
class-level "decipher" phrase search, 1 class-level "cipher key" phrase search), archive.org 1 (djvu text
fetch, Wentworth Papers vol. I). WebSearch: 2 queries.

## Edition risk

**Open.** Raby's Berlin correspondence has a standard printed edition (Wentworth Papers, 1883), but by
its own stated date range and confirmed by full-text grep it does not cover April-June 1704 — the printed
collection starts the year after these five items. No other edition was located.

## Verdict

**Open, stage 2 verified unsolved (conditional: full text of Cartwright's introduction beyond the grepped
1704 asides, and the 1877-1883 HMC reports/Calendar of Treasury Papers not checked; German-language
literature on the Reichart-Berlepsch Bavarian mediation channel not searched).** Five items, all confirmed
"Partly in cipher" by the catalogue's own note field, none digitised, no sibling decipherment anywhere in
piece SP 90/2 or the wider SP 90 class outside 1709-14, no companion cipher-key record on Discovery, not in
the standard printed edition (out of its date range), no match on DECODE, Bourdeau's or Aymeloglu's working
lists, or Tomokiyo's cached pages. Not "new"; not "unpublished" — a search result, not a discovery (rule
10).

## Next

TNA page-copy order for all five (SP 90/2/335, 337, 348, 409, 409v; the last two are a single enclosure,
so effectively four separable copy requests) — none digitised, no cheaper print-check route left unexplored
given the date mismatch with Wentworth Papers. Worth a companion check of SP 90/2/343 (Berlepsch to
Frederick I, reporting the same Reichart conference — not itself flagged cipher, but the plaintext report
of the same channel that /409 and /409v encode) as context once copies are in hand. Not batched into
REQUEST.md this session (brief scope: record findings and stage only; batching several targets' requests
into one REQUEST.md is an access-worker task).
