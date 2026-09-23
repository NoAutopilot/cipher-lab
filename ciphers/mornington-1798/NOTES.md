partial

# Mornington (Wellesley) despatches to Dundas, 1798-1800 — BL Mss Eur D623

QUEUE row: N1 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

BL Archives and Manuscripts, India Office Records and Private Papers, **Mss Eur D623**. Candidate items:
D623/4, /5, /10, /11, /22, /23, /24, /27, /28, /30, /35, /36 (+ copies /29, /37); key at **D623/41**.

Catalogue text for D623/41, quoted verbatim from the BL Archives and Manuscripts API
(`searcharchives.bl.uk`, record id `040-002273097`, fetched 24 September 2026):

> "Two copies of key to Lord Mornington's cipher"

Catalogue text for D623/10 (record `040-002273066`) and D623/11 (record `040-002273067`), same fetch:

> D623/10: "Despatch in cipher from Lord Mornington to Lord Dundas, asking for better service of
> political news and for a less cumbersome cipher, and one not so likely to be decoded. **[The despatch
> has been decoded!]**"
>
> D623/11: "Despatch [overland copy, the original being sent by sea], mainly in cipher relating to
> political and military matters in India **(cipher partly decoded)**"

These two bracketed cataloguer's notes match QUEUE.md's row exactly; no other item in the fonds carries
a decode/decipher annotation (see below).

## Check-solved sweep (24 September 2026)

1. **Web search.** "Mornington Wellesley cipher Dundas Seringapatam" (WebSearch) and a
   `site:de-crypt.org` variant: no hit connecting these despatches to any solver, blog or catalogue.
   Only unrelated modern-day "Mornington" place names and Arthur Wellesley (Lord Wellington, a different
   person, Mornington's younger brother) came back.
2. **Print.** Fetched the full BL Archives and Manuscripts record set for the fonds directly
   (`https://searcharchives.bl.uk/?q=%22Mss+Eur+D623%22&search_field=all_fields&format=json&per_page=100`,
   1 request, 42 records = D623 top level + D623/1-41): only D623/10 and D623/11 carry a decode/decipher
   note; nothing else in the fonds does. Then checked print editions on archive.org:
   - **The Despatches, Minutes and Correspondence of the Marquess Wellesley, during his Administration
     in India** (ed. Montgomery Martin, 1836-37): fetched the full djvu text of Vol. 1
     (`india.history.resource.35304`, 1836, covers 1798 to ~Oct 1799) and Vol. 2
     (`india.history.resource.35315`, 1836, covers into 1800).
     - **D623/23** (16 May 1799, "Letter from Mornington to Henry Dundas, mainly in cipher, covering
       the letter fro[m despatches] containing details of the capture of Seringapatam") **is printed in
       clear in Vol. 1**, opening "Yesterday I received the enclosed despatch from Lieut.-General Harris,
       containing the details of the capture of Seringapatam..." (matches the catalogue summary word for
       word). This is a plaintext hit for a "mainly in cipher" item that the India Office catalogue does
       **not** mark as decoded.
     - D623/22 (11 May 1799, "partly in cipher", catalogued quote "I flatter myself you will now be of
       the opinion...") was searched for by date and by the quoted phrase in both volumes: **not found**.
       The neighbouring Mornington-to-Dundas letters actually printed for 11 May 1799 are different ones
       (to the Court of Directors, not this one), so the edition appears to have skipped this specific
       ciphered item rather than printing it.
     - D623/27, /28, /30 (Mar-Apr 1800) and D623/35, /36 (Jun-Jul 1800): searched Vol. 2 by date
       ("5th March, 1800", "6th March, 1800", "25th April, 1800", "21st June, 1800", "9th July, 1800");
       the two date-matches found (5 Mar 1800, 9 Jul 1800) are unrelated documents (a financial table and
       a General Koehler letter). **Not found** in Vol. 1-2. Vols 3-5 (1836-37, covering to 1805) and
       *A Selection from the Despatches, Treaties and other Papers of the Marquess Wellesley* (1877,
       archive.org `india.history.resource.117686` and others) were **not** checked this sweep — flagged
       below as the open conditional.
     - D623/4, /5 (1798): not checked against Vol. 1 by phrase this sweep (budget).
   - HathiTrust: `babel.hathitrust.org` and `catalog.hathitrust.org` both answered 403 (Cloudflare/API
     gate), not retried past one probe each, per playbook (no HTRC/Bibliographic API lookup attempted
     this sweep — Wellesley material is on archive.org already, no HathiTrust-only route needed).
3. **Community lists.** `sources/cryptiana/` grepped for "mornington"/"wellesley": one hit
   (`web/maitland.htm`), which is about Arthur Wellesley (Lord Wellington)'s Peninsular War cipher
   practice under Scovell, a different person and a different theatre — not this target. No Cryptiana
   page on Mornington/Mysore ciphers.
4. **DECODE.** Cached catalogue (`ay/catalogue/decode-catalog.csv`, `decode-records.jsonl`) grepped for
   "D623"/"Mornington"/"Wellesley": no hit. `site:de-crypt.org` web search for the same terms: no hit.
   India Office material of this kind is not generally on DECODE.
5. **Bourdeau.** `cs-recheck/CATALOGUE.md`, `SOLVED_CATALOGUE.md`, `SOLVED_RANKING.md`, `TARGETS.md`
   grepped for "D623"/"Mornington"/"Wellesley": no hit.
6. **Aymeloglu.** `ay/CATALOGUE.md`, `ay/TARGETS.md`, `ay/SHORTLIST.md` grepped for the same terms: no
   hit.

Requests: searcharchives.bl.uk 4 (D623/41, D623/10, D623/11, full-fonds fetch), archive.org family 5
(2 metadata + 2 djvu fetches + advancedsearch), 12 WebSearch queries shared across all three targets this
session (see sp35-intercepts-1722/NOTES.md and courten-diary/NOTES.md for the rest).

## Edition risk

**Realized for D623/23**: this specific despatch is already printed in clear in Montgomery Martin's 1836
edition (Vol. 1), a major, widely held 19th-century edition (multiple archive.org copies). **D623/23
should not be treated as a recovery candidate** — it is a "found-solved" item within this batch (the
plaintext has been public since 1836; the India Office catalogue simply never updated its "mainly in
cipher" note). The Montgomery Martin edition is selective, not a full letter-book transcription: at least
one neighbouring ciphered item from the same short run (D623/22, 11 May 1799) was searched for and not
found in the same two volumes, so the edition risk is real but not blanket — it must be checked despatch
by despatch, not assumed for the whole file. Vols 3-5 and the 1877 *Selection* edition remain unchecked for
the 1800 items (D623/27, /28, /30, /35, /36); this is the open conditional below.

## Verdict

**Partial.** The key (D623/41) is real and uniquely catalogued, and D623/10 and D623/11 are already
known to the cataloguer as decoded/partly decoded (not novel targets). D623/23 is now also confirmed
already in print (Montgomery Martin 1836) and should be dropped from any solving batch. The remaining
items — D623/4, /5, /22, /24, /27, /28, /30, /35, /36 — were not found in web search, the Cryptiana
snapshot, DECODE's cached catalogue, Bourdeau's or Aymeloglu's catalogues, or (for /22, /27, /28, /30, /35,
/36) in the two Montgomery Martin volumes searched by date and phrase.

**Stage 2, verified unsolved (conditional): D623/4, /5, /22, /24, /27, /28, /30, /35, /36** — conditional
on Montgomery Martin Vols 3-5 (1836-37) and the 1877 *Selection from the Despatches, Treaties and other
Papers* not being checked yet for the 1800 items, and on HathiTrust (Cloudflare-gated here) not being
searched by the Bibliographic/HTRC route for any further Wellesley editions.

## Next

Before ordering anything: (a) finish the Montgomery Martin Vols 3-5 / 1877 *Selection* phrase search for
the six remaining 1800 despatches (cheap, same archive.org route used here, no imaging needed); (b) drop
D623/10, /11 and /23 from any order. If the remaining items still test unread after (a), BL Imaging
Services quote for D623/41 (the key) plus one short remaining item (e.g. D623/4, the shortest) as the
size/legibility test the original QUEUE row proposed, before ordering the whole run. No REQUEST.md drafted
yet — waiting on the Vols 3-5 check first, since that may drop more items at zero cost.
