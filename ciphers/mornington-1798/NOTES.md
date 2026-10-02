partial

Martin 1836 Vol. 1 (IA india.history.resource.35304), Owen's 1877 *Selection* (117686) and the 1914 *Wellesley Papers* I-II (87788, 87766) read by this worker on 2 Oct 2026 as full OCR text (`print/grep_editions.py`) for D623/4, /5 and /24: Vol. 1 No. XXII p. 80 prints a Mornington-to-Dundas letter of 6 July 1798 on the Mauritius proclamation (D623/5's date and subject); no 3 July 1798 or 7 June 1799 Mornington-to-Dundas item in any of the four; Ingram 1970 (be-api fts) prints the 6 July 1798 and 7 June 1799 letters. Martin Vol. 2 (35315) refetched and read 2 Oct 2026 05:2x UTC (`print/grep_vol2.py`): the 7 June 1799 Mornington-to-Dundas letter on the Mysore settlement (D623/24's date, recipient and subject) is printed there as No. XV pp. 35-43; p. 311 is the 9 Jul 1800 Rainier letter, not a 21 Jun 1800 one, and D623/35 has no printed witness; a 13 Jul 1800 Wellesley-to-Dundas letter (no D623 item) at pp. 361-366.

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

**Correction (GAPS-mornington-1798, 2 Oct 2026):** the sentence above over-stated the search for D623/4, /5 and /24 (they were never phrase- or date-searched in any edition before 2 Oct 2026, see "Remaining gaps"), and the 2 Oct pass found D623/5's date and subject printed in Martin Vol. 1 No. XXII and in Ingram 1970 (private no. 6), and D623/24's date printed in Ingram 1970 (private no. 15 [recte 16]). Stage 2 now stands for D623/4, /22, /27, /28, /30, /35, /36 only; /5 and /24 are print-attested on date and subject pending a content check (see the GAPS section below).

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

**LOCAL-QUEUE row L31 (ia-reader, queued 2 Oct 2026 05:3x UTC):** a person borrows Ingram 1970 (`twoviewsofbritis0000melv`,
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

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
Read so far: unmeasured. No ciphertext, despatch image or key image is on disk (folder holds only NOTES.md and REQUEST.md), so no token count exists. By item: 12 cipher-bearing items (D623/4, /5, /10, /11, /22, /23, /24, /27, /28, /30, /35, /36; copies /29, /37; key /41). Of these, 1 has known plaintext in print (D623/23, Martin 1836 Vol. 1, "Print check" 23 Sept 2026), 1 is cataloguer-noted "decoded" (/10) and 1 is "partly decoded" (/11), with neither decipherment seen by us. Re-checked 2 Oct 2026 00:53 UTC by one searcharchives.bl.uk JSON request (42 records): the items whose catalogue text mentions cipher are exactly this list, so no in-fonds cipher item is missing.
- D623/41 (key, both copies) + D623/4 (3 Jul 1798, test despatch) - blocker: waiting-on ASKS row 12 (BL Digitisation Services reply, order submitted 23 Sept 2026); no reply is logged in ROOM.md or outreach/ as of 2 Oct 2026, and there is no online image (BL IIIF dead since 2023, CLAUDE.md hosts table)
- D623/5, /22, /24, /27, /28 (+/29), /30, /35, /36 (+/37) - blocker: waiting-on ASKS row 12 (BL reply; REQUEST.md "If the test batch images well" gates the follow-on order on the key reading D623/4); not ordered, and imaging is the only route to the ciphertext. Also: D623/10 asks Dundas for "a less cumbersome cipher", so /41 may cover only the 1798 despatches, and the follow-on order should include the /10-/11 controls (next gap)
- Clear-page and crib set: D623/23 (printed in clear, Martin Vol. 1), /10 ("decoded"), /11 ("partly decoded"), plus clear neighbours on the same subjects: D623/2 and /3 (20 Jun 1798, the Mauritius proclamation and the mobilisation orders, same subject as cipher /4-5), D623/25 (26-27 Oct 1799, settlement of Mysore) and /26 (memorandum on settlement), same subject as /24's "memorandum in cipher detailing the proposed settlement" - blocker: not-attempted; REQUEST.md lines 16-19 say "do not order" /23 and list /10-/11 as optional only. The printed /23 text is now saved (`print/D623-23_martin1836_v1_p587.txt`, GAPS 2 Oct 2026) and the 6 Jul 1798 letter that is D623/5's date and subject with it (`print/D623-5_candidate_martin1836_v1_p80.txt`), and since GAPS2 (2 Oct 05:3x) the 7 Jun 1799 letter that is D623/24's date and subject (`print/D623-24_candidate_martin1836_v2_p35.txt`, Martin Vol. 2 No. XV, whose OCR is `print/35315_djvu.txt` with the Partition Treaty papers of June 1799); Martin Vol. 1's OCR is kept in `print/35304_djvu.txt`, where the Malartic proclamation sits at normalised offsets 8948 (French) and 9831 (English), the 20 Jun 1798 Harris letter at 171565, so the crib extraction needs no refetch. The clear neighbours and the printed Malartic proclamation (Jan 1798) and Partition Treaty of Mysore (22 Jun 1799), the likely cribs for /4-5 and /24, were never identified; next: from `print/35304_djvu.txt` (on disk) extract the Malartic proclamation, the 20 Jun 1798 Harris letter (/2-/3's subject) and the Mysore partition papers as crib files, and draft an amendment to REQUEST.md/ASKS 12 adding /23, /10, /11 to the follow-on order (payment stays with the owner), ~$3
- Counterpart copies outside D623 (Wellesley's own retained letter-books and Dundas correspondence in the BL Wellesley Papers Add MS series; IOR Home Misc/Board of Control secret correspondence; Melville papers at Clements, Duke, NRS GD51, NLS) - blocker: not-attempted; outside the D623 fonds no sibling series was ever searched (grep 2 Oct 2026: no hit outside this folder; LEDGER rows 81, 82, 654 are print checks only). A clear retained copy or a recipient's decipherment would give plaintext without imaging; next: one Sonnet worker on searcharchives.bl.uk JSON (Wellesley Papers Add MS, IOR/H, Board of Control) for the nine despatch dates and cipher/decipher 1798-1800, plus the Clements Melville Papers finding aid, logging NRS (egress-blocked) and NLS (Cloudflare) as unreachable, ~$4
- Print residual for D623/4, /5 (3 and 6 Jul 1798) and /24 (7 Jun 1799), and Ingram 1970 by date - blocker: waiting-on LOCAL-QUEUE row L31 (ia-reader; was not-attempted until 2 Oct 2026). RESULT 2 Oct 2026 (GAPS section above): the three-edition grep and the 7-date Ingram pass are done -- D623/5's date and subject printed in Martin Vol. 1 No. XXII and Ingram private no. 6; D623/24's date printed in Ingram private no. 15 [recte 16] (body unread, no page from be-api); D623/4, /22, /28, /30 absent from Ingram by date with a working control; D623/35's date only in an Ingram footnote citing Add MS 13751 f.77 and Martin Vol. 2 p. 311. What remains internal is the content check: whether Ingram's 7 Jun 1799 letter carries the Mysore memorandum, and whether Martin Vol. 2 p. 311 prints the 21 Jun 1800 letter (D623/35); the 23 Sept pass searched Vol. 2 by date only and kept no text; RESULT 2 Oct 2026 05:3x UTC (GAPS2 section above): Vol. 2 refetched and read -- p. 311 is the 9 Jul 1800 Rainier letter (the Ingram footnote cites it, not a 21 Jun 1800 letter); 21 Jun 1800 0 hits in both forms, so D623/35 has no printed witness; the 7 Jun 1799 Mornington-to-Dundas letter on the Mysore settlement IS printed at Vol. 2 No. XV pp. 35-43 (saved, D623/24's date, recipient and subject); a 13 Jul 1800 Wellesley-to-Dundas letter at pp. 361-366 (saved; no D623 item, the cipher despatch of that date is outside D623). What remains is the Ingram body read (no. 6, no. 15/16, the footnote page), which no script can do - blocker: waiting-on LOCAL-QUEUE row L31 (ia-reader, the owner's desk runner, queued 2 Oct 2026)

## Escalation (1 Oct 2026)
- [ ] siblings: Done: the whole D623 fonds read at item level (23 Sept 2026; re-read 2 Oct 2026, 42 records). Only /10 and /11 carry decode notes; /2, /3, /25 and /26 are clear neighbours on the same subjects as cipher /4-5 and /24. DECODE has no D623 record. Never searched: counterpart copies outside D623 (Wellesley Papers Add MS, IOR Home Misc/Board of Control, Melville papers). Planned: the searcharchives.bl.uk JSON and Clements finding-aid pass, ~$4
- [ ] clear-pages: Known-plaintext items found by catalogue and print but not extracted or ordered: D623/23 printed in clear, /10 decoded and /11 partly decoded per the cataloguer. Crib candidates: clear /2-/3 (Mauritius proclamation) for /4-5, and /25-/26 (Mysore settlement) for /24. Done 2 Oct 2026: /23's printed text and the 6 Jul 1798 letter saved in print/ from Martin Vol. 1, and (GAPS2, 05:3x) the 7 Jun 1799 letter for /24 from Martin Vol. 2; both OCR volumes kept on disk. Planned: extract the Malartic proclamation, the 20 Jun 1798 letter and the Mysore partition papers from print/35304_djvu.txt as crib files and draft the REQUEST.md/ASKS 12 amendment, ~$2
- [x] known-keys: Key D623/41 ("Two copies of key to Lord Mornington's cipher", record 040-002273097) is located in the same fonds and is in the ASKS 12 order. KEY-OFFICES.tsv and KEY-DESIGN.tsv have 0 rows for Mornington, Wellesley, Dundas, India or Bengal (grepped 2 Oct 2026). Cryptiana snapshot: only web/maitland.htm, which is Arthur Wellesley's Peninsular practice, a different key. Bourdeau and Aymeloglu catalogues: no hit. design_prior.py cannot run without ciphertext
- [ ] print: Done: Martin Vols 1-5, the 1877 Selection and the 1914 Wellesley Papers for /22 and the 1800 items (23 Sept 2026); Ingram 1970 via be-api fts with a Dundas control (25 Sept 2026); Martin Vol. 1, Owen 1877 and the 1914 volumes for /4, /5, /24 and Ingram for all 7 remaining dates with a date-form control (2 Oct 2026, GAPS section). Result: /23 printed (found-solved); /5's date and subject printed in Martin Vol. 1 No. XXII and Ingram no. 6; /24's date printed in Ingram no. 15/16; no hit for /4, /22, /27, /28, /30, /36; /35 only via an Ingram footnote to Martin Vol. 2 p. 311. Done 2 Oct 2026 05:3x (GAPS2): Martin Vol. 2 refetched and read -- p. 311 is the 9 Jul 1800 Rainier letter, not /35; 21 Jun 1800 0 hits both forms; 7 Jun 1799 Mornington-to-Dundas printed at Vol. 2 No. XV pp. 35-43 (/24's date and subject, saved); 13 Jul 1800 Wellesley-to-Dundas at pp. 361-366 (no D623 item). Not done: the Ingram body read, queued as LOCAL-QUEUE L31 (ia-reader) -- nothing internal remains on this step, it waits on L31
- [n/a] key-rebuild: nothing reads yet to extend from; no ciphertext or key image is on disk until the ASKS 12 photographs arrive
- [n/a] image-check: no image of any D623 item is on disk (BL IIIF dead since 2023), so there are no doubtful tokens to re-read
- [n/a] retry: no reading and no extended key exist yet, so there are no unread groups to rerun or regrade
Verdict: keep going: 2 internal gaps; cheapest next: from the OCR on disk (`print/35304_djvu.txt`, `print/35315_djvu.txt`, no refetch) extract the Malartic proclamation, the 20 Jun 1798 Harris letter and the June 1799 Mysore partition papers as crib files beside the three saved letters (/23, /5, /24), and draft the REQUEST.md/ASKS 12 amendment adding /23, /10, /11 to the follow-on order (payment stays with the owner), ~$3; the print residual waits on LOCAL-QUEUE L31 (updated 2 Oct 2026 05:3x UTC, GAPS2)

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
