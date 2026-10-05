partial

Martin 1836 Vol. 1 (IA india.history.resource.35304), Owen's 1877 *Selection* (117686) and the 1914 *Wellesley Papers* I-II (87788, 87766) read by this worker on 2 Oct 2026 as full OCR text (`print/grep_editions.py`) for D623/4, /5 and /24: Vol. 1 No. XXII p. 80 prints a Mornington-to-Dundas letter of 6 July 1798 on the Mauritius proclamation (D623/5's date and subject); no 3 July 1798 or 7 June 1799 Mornington-to-Dundas item in any of the four; Ingram 1970 (be-api fts) prints the 6 July 1798 and 7 June 1799 letters. Martin Vol. 2 (35315) refetched and read 2 Oct 2026 05:2x UTC (`print/grep_vol2.py`): the 7 June 1799 Mornington-to-Dundas letter on the Mysore settlement (D623/24's date, recipient and subject) is printed there as No. XV pp. 35-43; p. 311 is the 9 Jul 1800 Rainier letter, not a 21 Jun 1800 one, and D623/35 has no printed witness; a 13 Jul 1800 Wellesley-to-Dundas letter (no D623 item) at pp. 361-366. GAPS4 (2 Oct 2026 13:27-14:0x UTC, premise check and counterpart search): D623/27's letter (5 Mar 1800, the treaty of Hyderabad) is printed as Martin Vol. 2 No. LXIX pp. 225-252 and D623/36's letter to Admiral Rainier (9 Jul 1800) as No. LXXXIV p. 311, both found only when the second date form was run (saved in print/, grade C, not readings); the counterpart series are BL Add MS 13456-13459 and 37274-37276 (physical only, no decipher note); BL Mss Eur F228/65 holds a Wellesley cipher despatch of 8 Jul 1798 with its period decypher, printed in clear as Vol. 1 No. XXV; the Melville side (Clements, NRS, NLS) is Cloudflare-blocked from the cloud (LOCAL-QUEUE L34).

Ingram, *Two Views of British India: the private correspondence of Mr. Dundas and Lord Wellesley, 1798-1801*
(Bath, 1970; IA `twoviewsofbritis0000melv`) searched by this worker via `be-api.us.archive.org/fts/v1/search`
with control "Dundas" (hit, five real body-text snippets returned, e.g. "Wellesley also wrote to Dundas
fourteen secret and confidential letters"): no hit for the D623/4-5, /22, /24, /28-29 catalogue phrases, no
hit for either 5 or 9 July/March 1800 date forms, "Admiral Rainier" (D623/36) recurs only generically (same
false-positive pattern as the earlier Montgomery Martin check), and "cipher" itself returns zero hits
anywhere in the book.

## Check-solved (LANE CX, 25 Sept 2026)

This pass closes the one named risk left open by the 23 September 2026 sweep below (the "Edition risk not
yet closed" section): whether Ingram 1970 prints any of the still-open D623 despatches. The full six-source
sweep (web, print, community lists, DECODE, Bourdeau, Aymeloglu) was already run and logged in the 23
September 2026 sections below by an earlier worker; this session did not re-run those five, only the Ingram
addition, per this session's job brief.

1. **Route-finding.** `archive.org/advancedsearch.php?q=title:(Two Views of British India)` (1 request) found
   identifier `twoviewsofbritis0000melv`; `archive.org/metadata/twoviewsofbritis0000melv` (1 request) shows
   `access-restricted-item: true`, collections `internetarchivebooks`/`inlibrary`/`printdisabled` — a
   lending-only, print-disabled-tier item (Access playbook: cannot be borrowed by this account). Per CLAUDE.md
   item 3, full-text search still works on lending-only items via `be-api.us.archive.org/fts/v1/search`.
2. **Controlled full-text search (be-api, no login).** Control query `q=Dundas` returned a real hit with body
   text (not just metadata), confirming the route works and the OCR text is genuinely searchable, not just a
   catalogue stub. Target queries: `"proclamation issued at Mauritius"` (D623/4-5, 0 hits), `"I flatter myself
   you will now be of the opinion"` (D623/22, 0 hits), `"re-distributing"` (D623/24, 0 hits), `"government
   records" Seringapatam` (D623/28-29, 0 hits), `"Admiral Rainier"` (D623/36, 1 hit but the name recurs five
   times in unrelated naval-command sentences — the same generic-name false positive already documented for
   "treaty of Hyderabad" in the Montgomery Martin check, not the despatch itself, whose own scope text is only
   "Extract from a letter to Admiral R, mainly in cipher" with no distinctive content to search on), `"5th of
   March, 1800"` and `"9th of July, 1800"` (0 hits each), and `cipher` alone (0 hits anywhere in the book — the
   editor never discusses ciphered despatches). 10 be-api requests, >=1.6s apart.
3. **Item-level scope text refetched** (`searcharchives.bl.uk`, 8 requests this pass: D623/4, /5, /24, /27,
   /28, /30, /35, /36) to get exact catalogue wording for the search terms above; D623/30 and /35 both read
   only "Extract from a letter, mainly in cipher" — no distinctive content in the catalogue record at all, so
   no phrase search is possible for those two from the catalogue alone (unchanged blocker, not new).

Intake verdict: open.

# Mornington (Wellesley) despatches to Dundas, 1798-1800 — BL Mss Eur D623

QUEUE row: N1 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

BL Archives and Manuscripts, India Office Records and Private Papers, **Mss Eur D623**. Candidate items:
D623/4, /5, /10, /11, /22, /23, /24, /27, /28, /30, /35, /36 (+ copies /29, /37); key at **D623/41**.

Catalogue text for D623/41, quoted verbatim from the BL Archives and Manuscripts API
(`searcharchives.bl.uk`, record id `040-002273097`, fetched 23 September 2026):

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

## Check-solved sweep (23 September 2026)

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
     (`india.history.resource.35315`, 1836, covers into 1800). [Corrected 2 Oct 2026, GAPS2: Vol. 2 begins in May 1799 (No. XV is 7 Jun 1799), so the 1799 dates needed grepping in it too.]
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

## Print check, part 2 (23 September 2026)

Finished the conditional left open above: Montgomery Martin Vols 3-5 (1836-37), the 1877 *Selection*
(Owen), and (per the brief) the *Wellesley Papers* (1914, ed. Martin/Pearce family correspondence — 2
vols) — all six sources now checked for D623/22 and the six 1800 despatches (D623/27, /28+copy /29, /30,
/35, /36+copy /37).

**archive.org identifiers used** (advancedsearch by title, 1 query each for the Martin set and the 1914
set; `_djvu.txt` fetched once per volume to
`/tmp/.../scratchpad/mornington/<identifier>.txt`, not committed):
- Vol. 3 (1836): `india.history.resource.111968`
- Vol. 4 (1837): `india.history.resource.111967`
- Vol. 5 (1837): `india.history.resource.35037`
- 1877 *Selection from the Despatches, Treaties and other Papers of the Marquess Wellesley* (Owen):
  `india.history.resource.117686`
- *The Wellesley Papers* (1914), Vol. I: `india.history.resource.87788`; Vol. II:
  `india.history.resource.87766`

**Method.** `grep_martin.py` (scratchpad) normalises OCR whitespace and hyphenated line-breaks, then
searches each volume for (a) the catalogue's distinctive phrase per despatch, from the fonds's full-text
`scope_and_content` fetched fresh for each item this pass (`searcharchives.bl.uk`, one query per item:
D623/4, /5, /22, /24, /27, /28, /29, /30, /35, /36, /37, /41), and (b) every plausible spelling of the
despatch date ("5th March, 1800" / "5th of March 1800" / etc., case-insensitive, comma optional).

**Result: no genuine hit for any of the seven items in any of the six volumes.** Two phrase matches
surfaced and were checked in full context, both false positives:
- "found in the palace at Seringapatam" (1877 *Selection*, near "Fort William, March 9th, 1800") is from
  a *different*, broader Mornington-to-Dundas letter of **9 March 1800** (Mahratta empire, Zemaun Shah,
  the Poonah subsidiary force, Scindia) that mentions the Seringapatam papers in passing — not D623/28's
  narrow Edmonstone despatch (6 Mar 1800) on Tippoo's captured government records specifically. Confirms
  the general topic reached print nearby in date but not this cipher item.
- "treaty of Hyderabad" (D623/27 search term) and "Admiral R[ainier]" (D623/36 search term) each recur
  many times across all volumes in unrelated sentences — generic phrases, not despatch-specific.
- Date-only matches ("26th of March, 1800" swallowing a loose "6th... March, 1800" regex; the 5 Mar 1800
  stock-price table already flagged in the first pass) are the same false positives as before, re-confirmed.

No letter with a dateline of 11 May 1799, 5, 6, 25 March/April 1800, 21 June 1800 or 9 July 1800
matching any of these seven despatches appears as its own printed item in Vols 3-5, the 1877 *Selection*,
or the 1914 *Wellesley Papers* (both volumes, which are mostly personal/political correspondence, not
despatch texts, and cover this period only thinly).

**D623/41 (the key) catalogue text, re-checked** (`searcharchives.bl.uk`, record `040-002273097` for the
duplicate lookup this pass): "Two copies of key to Lord Mornington's cipher" — no decode/decipher note,
same as the first pass.

Requests this pass: `searcharchives.bl.uk` 12 (one per item, D623/4,5,22,24,27,28,29,30,35,36,37,41),
`archive.org` 15 (3 advancedsearch + 6 metadata + 6 `_djvu.txt` downloads).

## Verdict (updated 23 September 2026)

**Partial**, unchanged in kind but the conditional is now cleared for this batch of six editions.
D623/23 stays found-solved (Montgomery Martin Vol. 1, first pass); D623/10 and /11 stay already
known-decoded to the cataloguer. **D623/4, /5, /22, /24, /27, /28 (+copy /29), /30, /35, /36 (+copy
/37) are now stage 2, verified unsolved**, not found in web search, the Cryptiana snapshot, DECODE's
cached catalogue, Bourdeau's or Aymeloglu's catalogues (first pass), or in six print editions spanning
Vols 1-5 of Montgomery Martin (1836-37), the 1877 *Selection* (Owen), and the 1914 *Wellesley Papers*
(both passes) — a search result, not a claim that no other edition exists (rule 10; e.g. HathiTrust
remains Cloudflare-gated here and was not searched by the Bibliographic/HTRC route for further Wellesley
material).

**Correction (GAPS-mornington-1798, 2 Oct 2026):** the sentence above over-stated the search for D623/4, /5 and /24 (they were never phrase- or date-searched in any edition before 2 Oct 2026, see "Remaining gaps"), and the 2 Oct pass found D623/5's date and subject printed in Martin Vol. 1 No. XXII and in Ingram 1970 (private no. 6), and D623/24's date printed in Ingram 1970 (private no. 15 [recte 16]). Stage 2 now stands for D623/4, /22, /27, /28, /30, /35, /36 only; /5 and /24 are print-attested on date and subject pending a content check (see the GAPS section below). **Correction 2 (GAPS4, 2 Oct 2026):** /27 and /36 are print-attested too (Martin Vol. 2 No. LXIX pp. 225-252 and No. LXXXIV p. 311, found when the second date form was first run on 2 Oct 2026); stage 2 stands for D623/4, /22, /28, /30, /35 only.

## Next

REQUEST.md drafted this pass (BL Imaging Services quote): D623/41 (the key, both copies) plus the
shortest unprinted despatch, D623/4 (3 Jul 1798), as the size/legibility test the original QUEUE row
proposed, before committing to the full nine-item run. No email sent, no price guessed.

## Edition risk not yet closed (23 September 2026, orchestrator)

Edward Ingram, ed., *Two Views of British India: The Private Correspondence of Mr Dundas and Lord Wellesley, 1798-1801* (Bath, 1970) prints the private Dundas-Wellesley letters of exactly these years and is not on the Internet Archive. Despatches to Dundas "mostly in cipher" are likely to be that private correspondence. Before any imaging payment, check Ingram 1970 by date for D623/4, /5, /22, /24, /27, /28, /30, /35, /36: an IA loan if held, HathiTrust search-only, or a library copy. Until then the best case for this target is unknown, not N3.

**(corrected LANE CX 25 Sept 2026): Ingram 1970 *is* on the Internet Archive** (`twoviewsofbritis0000melv`,
a lending-only/print-disabled item, not full-view or borrowable, but full-text searchable without login via
`be-api.us.archive.org/fts/v1/search` — see the "Check-solved (LANE CX, 25 Sept 2026)" section above). Checked
with a control and found no hit for any of the still-open despatches; this conditional is now cleared, no IA
loan or library copy needed for the Ingram question specifically.

## GAPS-mornington-1798 (2 Oct 2026, account-4)
Verdict step of the 1 Oct 2026 finish-or-blocker pass, run 2 Oct 2026 01:57-02:1x UTC: grep Martin Vol. 1, the 1877
*Selection* and the 1914 *Wellesley Papers* for D623/4, /5 and /24; be-api fts on Ingram 1970 for the 7 unsearched
despatch dates; save D623/23's printed text. Hosts: archive.org family only (30 requests: archive.org 13 = 4 wrong-name
404/500 + 4 metadata + 4 `_djvu.txt` + 1 permitted retry of 117686 after two HTTP 500s; be-api 17). Vision calls 0.
Everything fetched is in `print/` with `print/manifest.tsv` (5.1 MB, four OCR texts kept so the next pass refetches
nothing); `print/grep_editions.py` regenerates every match below; `print/ingram_fts_results.tsv` holds every be-api query
and snippet.

**Editions (local grep, date in every spelling + catalogue phrases), per item:**

| item | Martin Vol. 1 (1836) | Owen 1877 | Wellesley Papers I/II (1914) |
|---|---|---|---|
| D623/4, 3 Jul 1798 | 0 date hits; no Mornington-to-Dundas letter of that date | 0 | 0 / 0 |
| D623/5, 6 Jul 1798 | **No. XXII, p. 80 ff.: "The Earl of Mornington to the Right Hon. Henry Dundas ... Fort William, July 6, 1798. With my Letter, No. 5, dispatched overland, I transmitted to you a copy of the Proclamation issued by the Governor of the Isle of France"** (the other four 6 July hits are Harris, Webbe, Malcolm and an index row) | only Webbe's 6 Jul 1798 memorandum | 0 / 0 |
| D623/24, 7 Jun 1799 | 0 date hits; "re-distributing" 0; "memorandum ... settlement" 0 | 0 | 0 / 0 |
| D623/23, 16 May 1799 | No. CCIII, p. 587, re-located and saved: `print/D623-23_martin1836_v1_p587.txt` | 0 | 0 / 0 |

The 1914 volumes carry no 1798-99 despatch text at all (0 hits for every date, phrase and for "cipher"). "cipher/cypher"
in Martin Vol. 1 (4) and Owen (10) is always the Company's cypher No. 11, Harris's "having no cypher", Tippoo's
Carnatic cypher, or Dundas's 30 Dec 1800 reply to an "overland despatch in cypher, dated 13th July last" (D623 has no 13
July 1800 item; a lead for the counterpart-copies gap, not this one).

**Ingram 1970 (be-api fts, control first):** control "16 June 1798" (Dundas to Mornington, printed) = 1 hit, header form
"Hon. Henry Dundas to the Earl of Mornington 16 June 1798, Wimbledon Private: no. 2"; the "June 16, 1798" form = 0, so
Ingram's headers use day-month-year and the ordinal form is the second spelling tested. Target dates, two forms each:
3 Jul 1798 0/0; **6 Jul 1798 1/0 -- "Earl of Mornington to the Rt Hon. Henry Dundas 6 July 1798, Fort William Private:
no. 6"**; 11 May 1799 0/0; **7 Jun 1799 1/1 -- "Earl of Mornington to the Rt Hon. Henry Dundas 7 June 1799, Fort St
George Private: no. 15 [recte 16]" and, in a later letter, "points stated in my dispatch overland of the 7th June 1799
[no. 15]"**; 6 Mar 1800 0/0; 25 Apr 1800 0/0; 21 Jun 1800 1/0 -- an editorial footnote only: "1 On 21 June 1800. 2 Add.
MSS. 13751, f. 77. Wellesley, ii, 311" (a 21 June 1800 letter held at BL Add MS 13751 f.77 and printed in Martin Vol. 2
p. 311: D623/35's date, a counterpart-copy lead). Subject check "Malartic": 1 hit, index "Malartic, Anne, Cte de, 46 fn.,
52, 63, 64, 100, 124" with the sentence "it appears probable that Monsieur Malartic took that step with the combined
objects of exposing" -- the same letter as Martin's No. XXII ("whatever construction may be put upon the policy of M.
Malartic in this extraordinary measure", Vol. 1 offset 211547), so Ingram's private no. 6 and Martin's No. XXII are one
text, printed twice (1836, 1970).

**What this establishes (rule 10 wording).** (1) A clear Mornington-to-Dundas letter dated 6 July 1798 on the Mauritius
proclamation, the catalogue date and subject of D623/5 ("duplicate of /4 ... re the Mauritius proclamation"), is printed in
Martin 1836 Vol. 1 No. XXII and in Ingram 1970 as private no. 6; it opens by saying letter No. 5 "dispatched overland"
carried the proclamation, which fits D623/4 (3 Jul 1798, "original letter appended to a despatch in cipher"). Whether the
cipher despatch's plaintext is this letter or a separate enclosure cannot be settled from print; the printed text is
grade C for the clear letter and the natural crib for the /4-5 cipher, saved as `print/D623-5_candidate_martin1836_v1_p80.txt`
(31 KB). (2) A Mornington-to-Dundas letter of 7 June 1799, Fort St George, private no. 15 [recte 16], the date of D623/24
("memorandum in cipher detailing the proposed settlement"), is printed in Ingram 1970; be-api gives no page and no body
text, and Martin/Owen/1914 do not print it, so whether Ingram prints the memorandum itself or only the covering letter is
unread. (3) D623/4, /22, /28, /30 have no date hit in Ingram in either form, with a working control; D623/35's date appears
only in a footnote pointing to Add MS 13751 f.77 and Martin Vol. 2 p. 311. (4) D623/23's printed text is on disk.
Not found is a search result, not a novelty verdict; nothing here is "new" or "first".

Gate outputs after this pass: `tools/intake_gate_check.py mornington-1798` -> "partial (line 1) -- edition/page or full-text-search citation found within 6 lines", exit 0 (was 1 before the web/blog section below); `tools/gaps_check.py mornington-1798` -> "OK keep-going mornington-1798: keep going: 3 internal gap(s), 3 step(s) untried", exit 0.

**Effect on the order (ASKS row 12 / REQUEST.md):** D623/5 joins D623/23 as print-attested on date and subject and should
not be paid for as a fresh recovery candidate before the key test; D623/24 the same pending a read of Ingram's letter
no. 15/16. Neither file was changed beyond a dated correction note in REQUEST.md; the ASKS row is the parent's.

## GAPS2-mornington-1798 (2 Oct 2026, account-4)
Verdict step of the "## Remaining gaps" section as rewritten 2 Oct 2026 02:1x UTC, run 2 Oct 2026 05:18-05:3x UTC: refetch
Martin Vol. 2 (`india.history.resource.35315`) once, read p. 311 for the 21 Jun 1800 letter Ingram's footnote seemed to
place there (D623/35), grep Vol. 2 for 7 Jun 1799 (D623/24) and 13 Jul 1800, and queue a LOCAL-QUEUE row for the Ingram
body read. Hosts: archive.org 1 request (the `_djvu.txt`, HTTP 200, 1.95 MB, saved once as `print/35315_djvu.txt` with a
manifest row); no other host. Vision calls 0. `print/grep_vol2.py` regenerates every match below from disk (no network)
and runs the same dates against the 1914 Wellesley Papers II OCR already on disk, in case "Wellesley, ii, 311" meant that
edition: 0/0/0 hits there, and its p. 311 is 1835 material.

**p. 311.** Running heads "310 THE MARQUESS WELLESLEY, July" / "1800. VICE ADMIRAL RAINIER. 311" / "312 THE GOVERNOR-GENERAL
IN COUNCIL": p. 311 carries the close of No. LXXXIII, General Koehler to Wellesley, Jaffa, 9 July 1800, and No. LXXXIV, the
Marquess Wellesley to Vice-Admiral Rainier, Fort William, 9 July 1800 (discontinuing the Batavia expedition; the squadron to
stay in Indian seas against a French move on Egypt by the Red Sea). No 21 June 1800 letter and no letter to Dundas is on
p. 311. The be-api snippet (`print/ingram_fts_results.tsv`) is two separate page-foot footnotes, "1 On 21 June 1800." and
"2 Add. MSS. 13751, f. 77. Wellesley, ii, 311", under body text ending "...of the Company's European infantry ought":
footnote 1 dates something in Ingram's sentence, footnote 2 cites the Rainier letter's manuscript and its print. The 2 Oct
02:1x pass read the two as one footnote placing a 21 June 1800 letter at p. 311; corrected here. D623/35's date has no
printed witness located.

**Date grep, Vol. 2, both forms ("21st June, 1800" and "June 21st, 1800" etc., `date_rx`):** 21 Jun 1800: 0 (the 23 Sept
one-form negative now holds for both forms). 7 Jun 1799: 2 -- No. XIV, Harris to Mornington, Camp, 7 June 1799 (the
Seringapatam ordnance and prize), and **No. XV, pp. 35-43, "The Earl of Mornington to the Right Hon. Henry Dundas. My dear
Sir, Fort St. George, 7th June, 1799. Nothing can be more favourable than the state of affairs in Mysore ... the
information which I have collected has enabled me to determine the basis and outline of the new settlement of the
extensive empire"** -- an 18.7 KB letter arguing the partition (why not equal shares with the Nizam, why not a third to the
Mahrattas, why the old Rajah's heir and not a son of Tippoo, the subsidiary force, Goa, the artillery): the date, sender,
recipient and subject of D623/24 ("memorandum in cipher detailing the proposed settlement", 7 Jun 1799). Within the letter
"memorandum", "re-distributing" and "cipher" occur 0 times, "partition" 1, "Treaty" 3 (grep). Saved as
`print/D623-24_candidate_martin1836_v2_p35.txt`. 13 Jul 1800: 7 -- **No. LXXXVIII, pp. 361-366, "The Marquess Wellesley to
the Right Hon. Henry Dundas, July 13th, 1800"**, on the reduced state of HM regiments and the European force India needs
(index row "Wellesley, Marquess to Rt. Hon. Henry Dundas, 13 July, 361"), plus two later self-citations ("In my letter of
the 13th of July, 1800") and four appendix list entries (writers' appointments); saved as
`print/martin1836_v2_p361_wellesley-dundas_13jul1800.txt`. "cipher/cypher" in Vol. 2 (19 hits): all Omdut ul Omra and
Tippoo's Carnatic cypher or the Grand Signor's cypher, nothing on the Dundas correspondence.

**Why the 2 Oct 02:1x pass missed /24.** Martin's Vol. 2 begins in May 1799 (TOC: Henry Wellesley 25 May 1799 p. 15; No.
XV is 7 Jun 1799), not in 1800 as the 23 Sept note ("Vol. 2 covers into 1800") implied; that pass grepped Vol. 1 alone for
the 1798-99 dates and the 23 Sept pass grepped Vol. 2 for the 1800 dates alone, so 7 Jun 1799 had never been run against
Vol. 2. A volume boundary is not a year boundary: every date goes against every volume on disk.

**What this establishes (rule 10 wording).** (1) A clear Mornington-to-Dundas letter of 7 June 1799 on the settlement of
Mysore, D623/24's date, sender, recipient and subject, is printed in Martin 1836 Vol. 2 No. XV pp. 35-43 (read on 2 Oct
2026) and, by date and header, in Ingram 1970 as private no. 15 [recte 16] (be-api, 2 Oct 02:0x UTC). Whether D623/24's
cipher memorandum is this letter's text or a separate enclosure cannot be settled from print: text known for the clear
letter, grade C, the natural crib for /24 -- not a reading of /24. (2) D623/35 (21 Jun 1800): not printed in Martin Vol.
2 in either date form, and the Ingram footnote cites p. 311 for the 9 Jul 1800 Rainier letter; no printed witness located
(a search result). (3) A Wellesley-to-Dundas letter of 13 July 1800 is printed at Vol. 2 pp. 361-366; D623 has no 13 July
1800 item, and Dundas's 30 Dec 1800 reply (Owen 1877, GAPS 2 Oct 02:1x) answers an "overland despatch in cypher, dated
13th July last", so a cipher despatch of that date exists outside D623 (a lead for the counterpart-copies gap). Nothing
here is new, first or unpublished.

**LOCAL-QUEUE row L32 (ia-reader, queued 2 Oct 2026 05:3x UTC):** a person borrows Ingram 1970 (`twoviewsofbritis0000melv`,
print-disabled tier; `tools/ia_borrow.py` cannot read its pages, Access playbook item 3) and reads private no. 6 (6 Jul
1798) and no. 15 [recte 16] (7 Jun 1799) against the two Martin extracts on disk, plus the page carrying the "21 June 1800"
and "Add. MSS. 13751, f. 77" footnotes, answering the questions the row lists (page numbers, whether the 7 Jun 1799 letter
carries a memorandum or enclosure on the settlement, any editorial note that either letter went in cipher, what footnote 1
dates).

**Effect on the order (ASKS row 12 / REQUEST.md):** D623/24 joins /5 and /23 as print-attested on date, recipient and
subject and is not a fresh recovery candidate before the key test; a dated note added to REQUEST.md. The ASKS row is the
parent's.

Gate outputs after this pass: see the done line and the "## Remaining gaps" Verdict below (intake gate exit 0 before the
step; gaps_check output pasted in the ROOM.md done line).

## GAPS3-mornington-1798 (2 Oct 2026, account-4)
Run 06:06-06:1x UTC 2 Oct 2026 (clock read) on the "## Remaining gaps" Verdict step as rewritten by GAPS2 at 05:3x: crib
extraction from the two Martin OCR volumes already on disk, and the REQUEST.md/ASKS 12 amendment draft. Disk only: 0 requests
to any host, 0 vision calls, no refetch; `print/extract_cribs.py` cuts each file by raw OCR line range and `--check` exits 0
on the committed files. Intake gate exit 0 before the step (partial, citation within 6 lines).
| crib file (print/) | printed source | pages | OCR lines | crib for | content lines |
|---|---|---|---|---|---|
| `crib_malartic-proclamation-30jan1798_martin1836_v1_pviii-x.txt` | Martin 1836 Vol. 1, Introduction | viii-x | 35304 raw 314-575 | D623/4, /5 | 190 (French and English columns de-interleaved per page) |
| `crib_mornington-harris-20jun1798_martin1836_v1_p64.txt` | Martin 1836 Vol. 1, No. XVII | 64-65 | 35304 raw 4612-4664 | D623/4, /5 (D623/2-3's date and subject) | 47 |
| `crib_mysore-partition-treaty-22jun1799_martin1836_v2_p25.txt` | Martin 1836 Vol. 2, No. XIII (letter) + footnote | 25-34 (footnote 26-33) | 35315 raw 2075-2584 | D623/24 | 404 (letter body, then the treaty footnote) |
Grade: C for every token of all three (printed clear text, rule 4); H 0, S 0, M 0, I 0 -- these are crib candidates, no D623
cipher text is on disk to read against them, so nothing is claimed as read. Findings from the extraction itself: (1) the
proclamation is dated Port North-West 30 Jan 1798 (10 Pluviose an VI), printed in both languages, so the English translation
is the crib text for a despatch written in English; (2) the 20 Jun 1798 Harris letter (No. XVII) is the mobilisation order
whose clear copies are D623/2-3; (3) the "June 1799 Mysore partition papers" of the Verdict line are printed as the footnote
to Mornington's 5 Jun 1799 letter to Kirkpatrick (No. XIII), which itself describes the proposed form of the settlement two
days before D623/24's date -- the letter body is therefore the closer crib for a 7 Jun "memorandum detailing the proposed
settlement", and the treaty (as executed 22 Jun, ratified 26 Jun and 13 Jul) supplies the shares, place names and sums. The
OCR interleaves two text streams on these pages (two columns; body and footnote), so the script writes each stream separately
with page marks; the OCR is otherwise uncorrected ("Jess" for "less", "Matartic" for "Malartic").
Amendment draft: REQUEST.md ("Amendment draft, 2 Oct 2026 06:1x UTC") and ASKS.md row 12 (appended, existing wording kept)
now carry the proposal to add D623/23, /10 and /11 to the follow-on order as controls; the order and payment stay with the
owner, nothing sent, no personal or payment detail written (rule 9). Rule 10: nothing here is a reading or a novelty claim.
Suggested follow-up, not run (Usage 7): the counterpart-copy search outside D623 (the Remaining gaps' remaining internal
step, ~$4).

## Premise check (GAPS4-mornington-1798, 2 Oct 2026)
Run 13:27-13:5x UTC 2 Oct 2026 per `.claude/briefs/check-solved.md` "Premise check" (a)-(d), before the counterpart-copy step
(GAPS4 section below; the two overlap, every host is logged once there). The intake gate exited 1 at 13:27 UTC for the missing
section only ("passes the citation and web/blog checks but has no '## Premise check' section").
(a) **Decipherments and keys the folder mentions, opened where anything can be opened.** D623/10 "[The despatch has been
decoded!]", D623/11 "(cipher partly decoded)" and D623/41 "Two copies of key": item records re-read (searcharchives.bl.uk,
D623/10 = 040-002273066, `restrictions_on_access` says request the physical item, no digitised copy; BL IIIF dead since 2023)
-- the period decode and the key are **unreachable** online, not opened. D623/23's printed text: opened (on disk since 2 Oct
02:1x). Ingram 1970's footnote "Add. MSS. 13751, f. 77. Wellesley, ii, 311" (`print/ingram_fts_results.tsv`) opened against
the Vol. 2 OCR on disk: No. LXXXIV, the Marquess Wellesley to Vice-Admiral Rainier, Fort William, 9 July 1800 -- **found**:
D623/36 is "Extract from a letter to Admiral R, mainly in cipher", 9 Jul 1800 (copy /37), so the letter the extract was taken
from is printed in clear (saved `print/D623-36_candidate_martin1836_v2_p311.txt`, grade C, `extract_cribs.py --check` exit 0)
and its manuscript is Add MS 13751 f. 77 (BL, "Copies of letters from Lord Wellesley to Vice Admi. Peter Rainier, 13 Dec.
1798-17 Feb. 1805"). The 23 Sept pass matched "9th July, 1800" on the Koehler letter of the same date and never ran "July
9th" (the OCR reads "1808" for 1800 on this letter, so a date grep alone would still miss it; the running head "1800. VICE
ADMIRAL RAINIER. 311" is the witness). A both-forms date grep of Vol. 2 for the dates never run in both forms (11 and 16 May
1799, 5 and 6 Mar, 25 Apr, 9 Jul 1800; `date_rx` of `print/grep_vol2.py`, 2 Oct 13:3x UTC) then **found** No. LXIX, "The
Earl of Mornington to the Right Honourable Henry Dundas. My dear Sir, Fort William, March 5th, 1800. Although most of the
points touched in your several despatches have already been anticipated ... approbation of the treaty of Hyderabad", pp.
225-252 (OCR lines 12485-13703): D623/27's date, sender, recipient and subject ("Letter and memorandum, partly in cipher,
concerning the treaty of Hyderabad and policies for the preservation and consolidation of the British power in India");
saved `print/D623-27_candidate_martin1836_v2_p225.txt` (1,168 lines, grade C). The 23 Sept pass ran "5th March, 1800" only
and matched the stock-price table on the same date. 11 May 1799 (/22), 6 Mar 1800 (/28), 25 Apr 1800 (/30): 0 hits in both
forms; 16 May 1799: only the editor's footnote pointing to Vol. 1 p. 587 (/23). Whether the cipher passages of /27 and the
cipher extract of /36 are in these printed texts or in separate enclosures cannot be settled from print: text known for the
clear letters, not readings of /27 or /36.
(b) **Other solvers' working files.** `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers` cloned fresh (depth 1,
2 Oct 2026 13:3x UTC, scratchpad) and grepped for mornington, "Mss Eur D623", "D623/", wellesley, dundas: Bourdeau --
only `targets/r1892` (General Dundas, a 1790s French-Dutch target) and literary source texts; Aymeloglu -- only a Sherlock
Holmes test fixture ("the Dundas separation case") and `uv.lock`. No working file, rendering, key or apply-key output for
this item: **not found**. DECODE: no D623 record (23 Sept 2026, cached catalogue; unchanged).
(c) **Physical neighbours.** Within D623: /2-/3 (20 Jun 1798, clear) beside /4-/5; /25-/26 (Oct 1799, clear) beside /24;
/29 and /37 are copies of /28 and /36 -- catalogued, not openable (no image). Outside D623, the sibling series located this
pass (numbers in the GAPS4 section): Add MS 13456-13457 "Letters from Lord Wellesley to the Right Hon. Henry Dundas,
1798-1801" (catalogued also as "India: Letters from the Governor General to the Board of Control: 1798-1805"), with the
enclosures (13458) and Dundas's letters to Wellesley 13 Jun 1798-18 Mar 1799 (13459); Add MS 37274-37275 (Wellesley Papers
I-II, 7 Mar 1797-10 Jun 1805), whose record reads "original 'private' and 'secret and confidential' dispatches and letters of
Dundas (some few being in cypher), with many lengthy enclosures", with Malartic's proclamation at 37274 f. 42; Add MS 37276,
Mornington's letter-book of copies to Dundas, Clive, Clarke and Harris, 29 Jul 1798-19 May 1799, ff. 88 (covers /22's and
/23's dates, not /4-5 or /24); Add MS 13751 (copies to Rainier; f. 77 = /36's letter); Mss Eur D587 (one letter to Dundas,
12 Aug 1798, no D623 date). No record among these carries a decipher or decode word for a Wellesley despatch; all are
physical-only: **found as series, not opened**. And **found**: Mss Eur F228/65 (Kirkpatrick Collection; Lt-Col James
Achilles Kirkpatrick, Resident at Hyderabad, unbound correspondence F228/65-75; record 040-002288638): "Copy of despatch
(with decypher) dated 8 Jul 1798 from Wellesley on policy towards Tipu Sultan following the Proclamation issued by the French
Governor of Mauritius during the residence of Tipu's ambassadors in the Island, with related papers" -- a cipher despatch of
the same office and week as D623/4 (3 Jul) and /5 (6 Jul 1798), on the same subject, with its period decypher beside it; its
clear text is printed as Martin Vol. 1 No. XXV ("The Earl of Mornington to J. A. Kirkpatrick, Esq. Acting Resident at
Hyderabad. (Secret.) Fort William, 8th July 1798. I transmit to you an authentic copy of a Proclamation ...", pp. 100-,
both date forms, saved `print/crib_mornington-kirkpatrick-8jul1798_martin1836_v1_p100.txt`, grade C). Whether the
Governor-General used the same cipher with the Resident at Hyderabad as with Dundas is unknown (D623/10 asks Dundas for "a
less cumbersome cipher", so the Dundas cipher may be Dundas's own); if it is the same, F228/65 is a cipher + decypher +
print triple for the D623/41 key before any D623 item is read. Not a reading of any D623 item.
(d) **Recipient side.** Ingram 1970 (be-api fts, 4 queries): the letters it prints are cited to "Add. MSS. 13457, f. 66" and
"Add. MSS. 37274, ff. 122, 293", so Ingram's clear private letters are the Wellesley Papers at BL; "D. 623" 0 hits (he does not
cite this fonds). IOR/H "Wellesley Papers" Nos 1-23 (IOR/H/457-479): Clive's and Duncan's letters to Wellesley 1798-1805,
not the Dundas side. IOR/L/PS/9 (Board of Control, secret letters): 0 hits for Wellesley 1798; IOR/L/PS/9/76/49 is a Harford
Jones to Dundas letter of 17 Dec 1798 "in cypher" with "a decoded copy ... catalogued as IOR/L/PS/9/76/51" (a different
sender; the recipient office did keep cipher and decode together). Melville papers: Clements Library finding aids
(findingaids.lib.umich.edu, clements.umich.edu, quod.lib.umich.edu) each answer HTTP 403 with Cloudflare's "Just a moment"
challenge to curl (one request each); the headless browser could not start (Chromium does not hold the container's proxy
CA; the apt-get fix was not run); web.archive.org's CDX index reset the connection on the first try and the one permitted
retry -- **unreachable** from the cloud. The printed Guide to the manuscript collections in the William L. Clements Library
(1953; IA `guidetomanuscrip00will`, 2 be-api fts queries) indexes "Melville, Henry Dundas, 1st viscount, 1742-1811: 62, 97,
174, 251, 268, 288" and "Wellesley, Richard Colley, 2nd earl of Mornington" in several collections: those pages are the
desk read queued as LOCAL-QUEUE L34. NRS (catalogue.nrscotland.gov.uk) and NLS (manuscripts.nls.uk): HTTP 403 Cloudflare
challenge, one request each, no retry -- **unreachable** (NRS is a Cloudflare challenge here, not the egress block the gap
text expected).
**Verdict of the premise check:** no prior decipherment or plaintext of any D623 cipher item located; two more items are
print-attested on date, sender/recipient and subject (D623/27, Martin Vol. 2 No. LXIX; D623/36, Vol. 2 No. LXXXIV), joining
/5, /23 and /24, so stage 2 (verified unsolved, no printed witness on date) now stands for D623/4, /22, /28, /30, /35 only;
a sibling cipher + decypher pair (F228/65) and the counterpart series (Add MS 13456-13459, 37274-37276, 13751) are located
and are calibration material once imaged. Clear to test when an image exists. Status `partial`, unchanged (a status change is
the parent's). Nothing here is new, first or unpublished (rule 10).

## GAPS4-mornington-1798 (2 Oct 2026, account-4)
Verdict step of the "## Remaining gaps" section as rewritten by GAPS3 (06:1x UTC): the counterpart-copy search outside D623,
run 13:27-14:0x UTC 2 Oct 2026 as one pass with the premise check above (clock read). Vision calls 0. Hosts and request
counts: searcharchives.bl.uk 56 (45 all_fields JSON searches + 11 item records, >= 2.2 s apart; every query, its total and
its hits in `counterparts/bl_search_2026-10-02.tsv`); archive.org family 9 (be-api fts 6: Ingram 4, Clements guide 2;
advancedsearch 1; web.archive.org CDX 2, both connection reset); Clements family 3 (findingaids.lib.umich.edu,
clements.umich.edu, quod.lib.umich.edu, one each, all Cloudflare 403; one headless-browser attempt that never left the
container); catalogue.nrscotland.gov.uk 1 (403 Cloudflare); manuscripts.nls.uk 1 (403 Cloudflare); github.com 2 clones.
**Hits, by series (catalogue reference; cipher, decipher or clear copy per the record):**
| reference | record | what it is | cipher / decipher / clear |
|---|---|---|---|
| Add MS 13456-13457 (Vols I-II) | 036-002035775 | Letters from Lord Wellesley to the Rt Hon. Henry Dundas, 1798-1801 ("India: Letters from the Governor General to the Board of Control: 1798-1805") | no cipher word; the counterpart file of the D623 despatches to Dundas, presumed clear copies or received originals; physical only |
| Add MS 13458 | 040-002035778 | Enclosures in those letters | no cipher word |
| Add MS 13459 | 040-002035779 | Letters from Dundas to Wellesley, 13 Jun 1798-18 Mar 1799 | no cipher word |
| Add MS 37274-37275 (Wellesley Papers I-II) | 037-002053573 | Official correspondence of Mornington with Dundas, 7 Mar 1797-10 Jun 1805: original "private" and "secret and confidential" dispatches and letters of Dundas, "some few being in cypher", many enclosures; 37274 f. 42 Malartic's proclamation (Fr., copy) | **cipher** (Dundas's letters, a few); the D623/41 key's other direction, and any decipher beside them is a known-plaintext pair |
| Add MS 37276 (Wellesley Papers III) | 040-002053576 | Mornington's letter-book, copies to Dundas, Clive, Clarke, Harris, 29 Jul 1798-19 May 1799, ff. 88 | clear copies; covers /22 (11 May) and /23 (16 May 1799) by date, not /4-5 or /24 |
| Add MS 13751 | (q10) | Copies of letters from Wellesley to Vice-Admiral Rainier, 13 Dec 1798-17 Feb 1805; f. 77 = 9 Jul 1800 letter (Ingram's footnote) | clear copy of /36's letter; printed Martin Vol. 2 No. LXXXIV p. 311 |
| Mss Eur F228/65 | 040-002288638 | Kirkpatrick Collection: copy of despatch (with decypher) dated 8 Jul 1798 from Wellesley on the Mauritius proclamation, with related papers | **cipher + period decypher**; printed clear Martin Vol. 1 No. XXV p. 100 ff. (saved) |
| Mss Eur D587 | 032-002272768 | One letter, Wellesley to Dundas, 12 Aug 1798 (state of the Government, Council, army) | clear; no D623 date |
| IOR/L/PS/9/76/49, /51 | 041-003710957 | Harford Jones (Baghdad) to Dundas, 17 Dec 1798, in cypher; decoded copy at /51 | different sender; shows the Board's secret-letter series keeps cipher and decode together |
| IOR/H/457-479 | (q41) | "Wellesley Papers" Nos 1-23: Clive's and Duncan's letters to Wellesley 1798-1805 | not the Dundas side; no cipher word |
| Add MS 38237 (Liverpool Papers XLVIII) | 040-002057461 | "Cyphers: Various British and foreign diplomatists: 1800-1804" | cipher material, no Wellesley/Dundas link in the record; noted only |
"No hit" rows (rule 10, a search result): "Wellesley decipher" 0; "Wellesley decypher" 2 (F228/65 and an unrelated Liverpool
volume); "Mornington decoded" 1 (D623/10 itself); the nine despatch dates as "Wellesley <d Mon yyyy>" 0-14 hits each, none a
Wellesley-Dundas item outside D623; "decypher 1799"/"decypher 1800" 2 each, both unrelated (Hamilton at Naples, Auckland);
"Home Miscellaneous cipher 1798" 0; "Bengal secret letters cypher 1798" 0; "IOR/L/PS/9 Wellesley 1798" 0.
**What this establishes (rule 10 wording).** (1) Two further D623 cipher items have their letter printed in clear on date,
sender/recipient and subject: D623/27 (Martin Vol. 2 No. LXIX pp. 225-252, Mornington to Dundas 5 Mar 1800, treaty of
Hyderabad) and D623/36 (No. LXXXIV p. 311, Wellesley to Rainier 9 Jul 1800; manuscript Add MS 13751 f. 77); both saved,
grade C, regenerated by `print/extract_cribs.py` (`--check` exit 0, 6 files); the cipher memorandum of /27 and the cipher
extract of /36 may be these texts or separate enclosures -- unread. Both were missed on 23 Sept 2026 because only one date
form was run and a same-date neighbour (the stock table, the Koehler letter) absorbed the match: every date goes against
every volume in both forms (`date_rx`), and a hit on one document of a date does not close that date. (2) The counterpart
copies of the Dundas despatches exist as a series at BL (Add MS 13456-13457, 37274-37275), with Dundas's own cipher letters
among them; none is online, so they join the ASKS row 12 order as an amendment (REQUEST.md), not an internal step. (3) A
cipher + decypher + print triple of the same office and week as D623/4-5 exists (F228/65 + Vol. 1 No. XXV) -- a known-answer
control for the key if the Resident's cipher is the Dundas cipher, unknown until imaged. (4) The Melville side (Clements,
NRS, NLS) is unreachable from the cloud and is queued for the owner's desk (LOCAL-QUEUE L34). Nothing here is a reading;
nothing is new, first or unpublished.
Gate outputs after this pass: pasted in the ROOM.md done line (intake gate before and after the premise section; gaps_check).

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
Read so far: unmeasured. No ciphertext, despatch image or key image is on disk (folder holds only NOTES.md and REQUEST.md), so no token count exists. By item: 12 cipher-bearing items (D623/4, /5, /10, /11, /22, /23, /24, /27, /28, /30, /35, /36; copies /29, /37; key /41). Of these, 1 has known plaintext in print (D623/23, Martin 1836 Vol. 1, "Print check" 23 Sept 2026), 1 is cataloguer-noted "decoded" (/10) and 1 is "partly decoded" (/11), with neither decipherment seen by us. Re-checked 2 Oct 2026 00:53 UTC by one searcharchives.bl.uk JSON request (42 records): the items whose catalogue text mentions cipher are exactly this list, so no in-fonds cipher item is missing.
- D623/41 (key, both copies) + D623/4 (3 Jul 1798, test despatch) - blocker: waiting-on ASKS row 12 (BL Digitisation Services reply, order submitted 23 Sept 2026); no reply is logged in ROOM.md or outreach/ as of 2 Oct 2026, and there is no online image (BL IIIF dead since 2023, CLAUDE.md hosts table)
- D623/5, /22, /24, /27, /28 (+/29), /30, /35, /36 (+/37) - blocker: waiting-on ASKS row 12 (BL reply; REQUEST.md "If the test batch images well" gates the follow-on order on the key reading D623/4); not ordered, and imaging is the only route to the ciphertext. Also: D623/10 asks Dundas for "a less cumbersome cipher", so /41 may cover only the 1798 despatches, and the follow-on order should include the /10-/11 controls (next gap)
- Clear-page and crib set: D623/23 (printed in clear, Martin Vol. 1), /10 ("decoded"), /11 ("partly decoded"), plus clear neighbours on the same subjects: D623/2 and /3 (20 Jun 1798, the Mauritius proclamation and the mobilisation orders, same subject as cipher /4-5), D623/25 (26-27 Oct 1799, settlement of Mysore) and /26 (memorandum on settlement), same subject as /24's "memorandum in cipher detailing the proposed settlement" - blocker: waiting-on ASKS row 12 (the BL order, the owner's; was not-attempted until 2 Oct 2026); REQUEST.md lines 16-19 said "do not order" /23 and listed /10-/11 as optional only, amended 2 Oct 2026 (GAPS3) to propose them as controls. The printed /23 text is now saved (`print/D623-23_martin1836_v1_p587.txt`, GAPS 2 Oct 2026) and the 6 Jul 1798 letter that is D623/5's date and subject with it (`print/D623-5_candidate_martin1836_v1_p80.txt`), and since GAPS2 (2 Oct 05:3x) the 7 Jun 1799 letter that is D623/24's date and subject (`print/D623-24_candidate_martin1836_v2_p35.txt`, Martin Vol. 2 No. XV, whose OCR is `print/35315_djvu.txt` with the Partition Treaty papers of June 1799); Martin Vol. 1's OCR is kept in `print/35304_djvu.txt`, where the Malartic proclamation sits at normalised offsets 8948 (French) and 9831 (English), the 20 Jun 1798 Harris letter at 171565, so the crib extraction needs no refetch. The clear neighbours and the printed Malartic proclamation (Jan 1798) and Partition Treaty of Mysore (22 Jun 1799), the likely cribs for /4-5 and /24, were never identified until GAPS3. RESULT 2 Oct 2026 06:1x UTC (GAPS3 section above): three grade-C crib files cut from the OCR on disk by `print/extract_cribs.py` -- the Malartic proclamation (Vol. 1 pp. viii-x, French and English), Mornington to Harris 20 Jun 1798 (Vol. 1 No. XVII pp. 64-65) and Mornington to Kirkpatrick 5 Jun 1799 with the Partition Treaty, Schedules A-D and Separate Articles (Vol. 2 No. XIII pp. 25-34); the REQUEST.md amendment draft and the ASKS row 12 appendix propose /23, /10, /11 as controls in the follow-on order. Nothing internal remains on this gap: the cribs can only be applied once an image of /4, /5 or /24 exists (ASKS row 12)
- Counterpart copies outside D623 (Wellesley's own retained letter-books and Dundas correspondence in the BL Wellesley Papers Add MS series; IOR Home Misc/Board of Control secret correspondence; Melville papers at Clements, Duke, NRS GD51, NLS) - blocker: waiting-on ASKS row 12 and waiting-on LOCAL-QUEUE row L34 (was not-attempted until 2 Oct 2026 13:5x UTC, GAPS4); outside the D623 fonds no sibling series had been searched (grep 2 Oct 2026: no hit outside this folder; LEDGER rows 81, 82, 654 are print checks only). A clear retained copy or a recipient's decipherment would give plaintext without imaging; next: one Sonnet worker on searcharchives.bl.uk JSON (Wellesley Papers Add MS, IOR/H, Board of Control) for the nine despatch dates and cipher/decipher 1798-1800, plus the Clements Melville Papers finding aid, logging NRS (egress-blocked) and NLS (Cloudflare) as unreachable, ~$4. RESULT 2 Oct 2026 13:5x UTC (GAPS4 section above): run -- the counterpart series are located at BL (Add MS 13456-13459 Wellesley-Dundas letters and enclosures 1798-1801; Add MS 37274-37275 with Dundas's own letters "some few being in cypher"; Add MS 37276 letter-book 29 Jul 1798-19 May 1799; Add MS 13751 f. 77 = /36's letter), none online and none with a decipher note for a Wellesley despatch; Mss Eur F228/65 is a Wellesley cipher despatch of 8 Jul 1798 with its decypher (printed clear, Vol. 1 No. XXV, saved); IOR/H and IOR/L/PS/9 hold no Wellesley-Dundas cipher item; Clements, NRS and NLS are Cloudflare-blocked from the cloud. Blocker now: waiting-on ASKS row 12 (the BL order; REQUEST.md amendment of 2 Oct 13:5x proposes F228/65, the cypher letters of Add MS 37274-37275 and the Add MS 13456-13457 counterparts of /4, /22, /28, /30, /35 as further items) and waiting-on LOCAL-QUEUE row L34 (the Melville-side finding aids and the 1953 Clements guide pages, from the owner's desk)
- Print residual for D623/4, /5 (3 and 6 Jul 1798) and /24 (7 Jun 1799), and Ingram 1970 by date - blocker: waiting-on LOCAL-QUEUE row L32 (ia-reader; was not-attempted until 2 Oct 2026). RESULT 2 Oct 2026 (GAPS section above): the three-edition grep and the 7-date Ingram pass are done -- D623/5's date and subject printed in Martin Vol. 1 No. XXII and Ingram private no. 6; D623/24's date printed in Ingram private no. 15 [recte 16] (body unread, no page from be-api); D623/4, /22, /28, /30 absent from Ingram by date with a working control; D623/35's date only in an Ingram footnote citing Add MS 13751 f.77 and Martin Vol. 2 p. 311. What remains internal is the content check: whether Ingram's 7 Jun 1799 letter carries the Mysore memorandum, and whether Martin Vol. 2 p. 311 prints the 21 Jun 1800 letter (D623/35); the 23 Sept pass searched Vol. 2 by date only and kept no text; RESULT 2 Oct 2026 05:3x UTC (GAPS2 section above): Vol. 2 refetched and read -- p. 311 is the 9 Jul 1800 Rainier letter (the Ingram footnote cites it, not a 21 Jun 1800 letter); 21 Jun 1800 0 hits in both forms, so D623/35 has no printed witness; the 7 Jun 1799 Mornington-to-Dundas letter on the Mysore settlement IS printed at Vol. 2 No. XV pp. 35-43 (saved, D623/24's date, recipient and subject); a 13 Jul 1800 Wellesley-to-Dundas letter at pp. 361-366 (saved; no D623 item, the cipher despatch of that date is outside D623). What remains is the Ingram body read (no. 6, no. 15/16, the footnote page), which no script can do - blocker: waiting-on LOCAL-QUEUE row L32 (ia-reader, the owner's desk runner, queued 2 Oct 2026). RESULT 2 Oct 2026 13:3x UTC (GAPS4, premise check (a)): the both-forms date grep of Vol. 2 for the dates never run in both forms found D623/27's letter (No. LXIX pp. 225-252, 5 Mar 1800 to Dundas) and D623/36's (No. LXXXIV p. 311, 9 Jul 1800 to Rainier), both saved; /22, /28, /30 0 hits in both forms. Still waiting-on L32 for the Ingram body

## Escalation (1 Oct 2026)
- [x] siblings: Done: the whole D623 fonds read at item level (23 Sept 2026; re-read 2 Oct 2026, 42 records). Only /10 and /11 carry decode notes; /2, /3, /25 and /26 are clear neighbours on the same subjects as cipher /4-5 and /24. DECODE has no D623 record. Never searched: counterpart copies outside D623 (Wellesley Papers Add MS, IOR Home Misc/Board of Control, Melville papers). Planned: the searcharchives.bl.uk JSON and Clements finding-aid pass, ~$4. Done 2 Oct 2026 13:5x (GAPS4): 45 searcharchives.bl.uk queries + 11 item records (counterparts/bl_search_2026-10-02.tsv) located Add MS 13456-13459, 37274-37276, 13751 and Mss Eur F228/65 (cipher with decypher, 8 Jul 1798); Clements, NRS, NLS Cloudflare-blocked, queued as LOCAL-QUEUE L34. Nothing internal remains: every series is physical-only (ASKS 12)
- [x] clear-pages: Known-plaintext items found by catalogue and print but not extracted or ordered: D623/23 printed in clear, /10 decoded and /11 partly decoded per the cataloguer. Crib candidates: clear /2-/3 (Mauritius proclamation) for /4-5, and /25-/26 (Mysore settlement) for /24. Done 2 Oct 2026: /23's printed text and the 6 Jul 1798 letter saved in print/ from Martin Vol. 1, and (GAPS2, 05:3x) the 7 Jun 1799 letter for /24 from Martin Vol. 2; both OCR volumes kept on disk. Done 2 Oct 2026 06:1x (GAPS3): the Malartic proclamation, the 20 Jun 1798 Harris letter and the 5 Jun 1799 Kirkpatrick letter with the Partition Treaty papers cut as grade-C crib files (print/crib_*.txt, print/extract_cribs.py --check exits 0); REQUEST.md/ASKS 12 amendment drafted for the owner (/23, /10, /11 as controls). Nothing internal remains; applying the cribs waits on the images (ASKS 12)
- [x] known-keys: Key D623/41 ("Two copies of key to Lord Mornington's cipher", record 040-002273097) is located in the same fonds and is in the ASKS 12 order. KEY-OFFICES.tsv and KEY-DESIGN.tsv have 0 rows for Mornington, Wellesley, Dundas, India or Bengal (grepped 2 Oct 2026). Cryptiana snapshot: only web/maitland.htm, which is Arthur Wellesley's Peninsular practice, a different key. Bourdeau and Aymeloglu catalogues: no hit. design_prior.py cannot run without ciphertext
- [x] print: Done: Martin Vols 1-5, the 1877 Selection and the 1914 Wellesley Papers for /22 and the 1800 items (23 Sept 2026); Ingram 1970 via be-api fts with a Dundas control (25 Sept 2026); Martin Vol. 1, Owen 1877 and the 1914 volumes for /4, /5, /24 and Ingram for all 7 remaining dates with a date-form control (2 Oct 2026, GAPS section). Result: /23 printed (found-solved); /5's date and subject printed in Martin Vol. 1 No. XXII and Ingram no. 6; /24's date printed in Ingram no. 15/16; no hit for /4, /22, /27, /28, /30, /36; /35 only via an Ingram footnote to Martin Vol. 2 p. 311. Done 2 Oct 2026 05:3x (GAPS2): Martin Vol. 2 refetched and read -- p. 311 is the 9 Jul 1800 Rainier letter, not /35; 21 Jun 1800 0 hits both forms; 7 Jun 1799 Mornington-to-Dundas printed at Vol. 2 No. XV pp. 35-43 (/24's date and subject, saved); 13 Jul 1800 Wellesley-to-Dundas at pp. 361-366 (no D623 item). Not done: the Ingram body read, queued as LOCAL-QUEUE L32 (ia-reader) -- nothing internal remains on this step, it waits on L32. Done 2 Oct 2026 13:3x (GAPS4): every remaining date in both forms against Vol. 2 -- /27 (No. LXIX) and /36 (No. LXXXIV) found printed and saved; /22, /28, /30 0 hits; the 8 Jul 1798 Kirkpatrick despatch (F228/65's clear text) saved from Vol. 1 No. XXV
- [n/a] key-rebuild: nothing reads yet to extend from; no ciphertext or key image is on disk until the ASKS 12 photographs arrive
- [n/a] image-check: no image of any D623 item is on disk (BL IIIF dead since 2023), so there are no doubtful tokens to re-read
- [n/a] retry: no reading and no extended key exist yet, so there are no unread groups to rerun or regrade
Verdict: parked: every gap has an outside blocker -- the key and every cipher image wait on ASKS row 12 (the BL order; REQUEST.md amendment of 2 Oct 2026 13:5x proposes Mss Eur F228/65, the cypher letters in Add MS 37274-37275 and the Add MS 13456-13457 counterparts of /4, /22, /28, /30, /35 as further items), the Ingram body read on LOCAL-QUEUE L32, the Melville-side finding aids on LOCAL-QUEUE L34; no untried step within the session -- the counterpart search, the crib set and both-forms print grep are done (updated 2 Oct 2026 13:5x UTC, GAPS4)

## Web and blog check (GAPS-mornington-1798, 2 Oct 2026)
Run 2 Oct 2026 01:58-02:05 UTC per `.claude/briefs/check-solved.md` "Required step: Open web and blog comment threads"
(the intake gate exited 1 on this target only for the missing section).
(a) Plain web searches (10 queries): "Lord Mornington Henry Dundas 1798 despatch cipher decoded"; `"Mss Eur D623" cipher`;
`"Lord Mornington's cipher"` (the D623/41 catalogue phrase, in quotes); "Mornington Wellesley despatches to Dundas
1798-1800 cipher India Office key" (the folder title); `Wellesley Dundas 1799 "in cipher" Seringapatam despatch
deciphered India Office Mss Eur`; "Mornington Wellesley Dundas cipher solved Claude GPT" (model-solve announcements);
plus the engine's own three refinements under the first query. Hits: Wikipedia and ship/peerage pages, the Ingram 1970
bookseller listings (AbeBooks, Biblio, Semantic Scholar record), the Cambridge Library Collection reprint of Martin's
Despatches, and lifeofwellington.co.uk chapter 5 ("Mornington and the Indian Scene") -- opened, no mention of cipher,
cypher, code or ciphered despatches anywhere on the page or in its comments. No hit names D623, the key, or any
decipherment of these despatches.
(b) Blog site searches: Cipherbrain -- engine `site:scienceblogs.de klausis-krypto-kolumne Mornington Wellesley Dundas`
(one Wellesley hit: "Die Raetsel-Grabsteine von Monmoth und Wellesley", 21 Dec 2014, a gravestone in Wellesley, Ontario;
opened, post and its 5 comments mention no Mornington, Dundas, India or despatch) and the blog's own search
`?s=Mornington` (0 posts); Cryptiana -- `sources/cryptiana/` grepped on disk for mornington/D623/wellesley (only
web/maitland.htm, Arthur Wellesley's Peninsular practice, already logged 23 Sept; the one "d623" string is a file hash in
the manifest), engine `site:cryptiana.blogspot.com Mornington Wellesley Dundas cipher` (0 blog hits), and the blog's own
search `search?q=Mornington` and `search?q=Wellesley` (0 posts each); Cipher Mysteries -- engine
`site:ciphermysteries.com Mornington Wellesley Dundas` (0 hits) and the site's own search `?s=Mornington` and
`?s=Wellesley+Dundas` (0 posts each).
(c) Every plausible hit opened and its comment thread read: 2 pages (the Cipherbrain gravestone post, lifeofwellington
chapter 5). 0 comments about this item.
Result: no decipherment or plaintext of any D623 cipher item located by these queries on 2 Oct 2026 (a search result,
not a novelty verdict, rule 10). Status word unchanged. Requests: scienceblogs.de 2, ciphermysteries.com 2,
cryptiana.blogspot.com 2, lifeofwellington.co.uk 1, web-search engine 10.

## While waiting (RUN4-WAITBF, 4 Oct 2026)

Nothing depends on anyone: the key and every cipher image wait on ASKS row 12 (the BL order, REQUEST.md amendment of 2 Oct 2026), the Ingram body read on LOCAL-QUEUE L32 and the Melville-side finding aids on LOCAL-QUEUE L34; the counterpart search, the crib set and the both-forms print grep are done (GAPS4).
- 5 Oct 2026 (PR-LAND-67): LOCAL-QUEUE L32 and L34 answers landed, local-runner/L32-2026-10-05.md and L34-2026-10-05.md -- L32: Ingram 1970 prints private no. 6 (pp.51-63) and no. 15 [16] (pp.156-163) in full (Martin abridged), the 7 Jun 1799 memorandum not printed, the p.279 footnotes belong to Wellesley to Dundas 13 Jul 1800 (no. 29 secret), no cipher note seen; L34: NRS GD51/3/101 "Extract from a coded letter. [Enclosure in letter, 13 July, 1800, from Lord Wellesley]" (21 Jun 1800, open, on site), Clements Melville papers no item list and 0 cipher hits, NLS Cloudflare-blocked.
