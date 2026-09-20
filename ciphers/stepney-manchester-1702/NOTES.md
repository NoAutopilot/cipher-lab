# George Stepney to the Earl of Manchester (Vienna, 23 March 1702)

- **Source:** Manchester Papers. Short ciphertext in a letter from George Stepney, English envoy at Vienna.
- **Status:** Offline-only (confirmed by check-solved sweep, 20 Sept 2026; see below).
- **Transcription:** `ciphertext.txt`. Two short code runs embedded in cleartext, numbers up to 847.
- **Known key nearby:** Other undeciphered letters in the Manchester Papers can be read with a key preserved with them in which THE = 454. Test whether that key fits this letter; Cryptiana implies it does not, but confirm.
- **Ideas:** Too short for cryptanalysis on its own. The route is archival: the same cipher was probably used in other Stepney letters of 1702, some of which will have contemporary decipherments.
- **Solver status (19 Sept 2026):** Offline-only per Bourdeau (cyphersolver/stepney), 15 Sept 2026: manuscript located and transcribed at Yale (OSB MSS fc37 box 8 folder 40, 24 groups); the THE=454 key rejected; the real key is in TNA SP 105/106 or BL Add MSS 7058-78.
- **Archive route (English, no key needed):** Stepney's own letter-books at TNA, SP 105 (Archives of British
  Legations), normally hold copies of his out-letters in clear. A copy of the entry for 23 March 1702 would give
  the plaintext directly. **Piece identified on Discovery, 19 Sept 2026: SP 105/65**, "Letter book(s) of George
  Stepney, envoy extraordinary to the Holy Roman emperor", 1702 Jan-1702 Aug, record C3609655,
  https://discovery.nationalarchives.gov.uk/details/r/C3609655. Not digitised, no item-level catalogue (only
  SP 105/60, 1693-94, is itemised), so the folio must be found by the copying team from date and addressee.
  Neighbours: SP 105/62-64 (Mar-Dec 1701), SP 105/66 (Sept-Dec 1702); SP 105/61 (1701-1705) is a memoranda book
  on Sweden and Poland. Request drafted in `REQUEST.md`. Second route: the Stepney Papers, BL Add MSS
  7058-7078, which reportedly include his cipher keys, once the British Library is producing copies again.
  Third: TNA SP 106, the office's cipher templates. Fourth: SP 80/18, Stepney's despatches as received, 1702
  Jan-June (C5909986); Manchester was Secretary of State from January 1702 (inferred relevance only).
  Bourdeau's transcription of the 24 groups from the Yale images is in cyphersolver/stepney/ciphertext.txt, with
  one correction to Tomokiyo (413, not 412).
- **Correction to Bourdeau's pointer (checked on Discovery, 19 Sept 2026):** "SP 105/106" is the letter book of
  Sir Dudley Carleton, ambassador at Venice, 1612-1613 (C3609696), not a Stepney volume. The intended reference
  is presumably the cipher series SP 106; treat the key's location as SP 106 or BL Add MSS 7058-7078, unverified.

## Check-solved sweep, 20 Sept 2026

Six independent searches were run to confirm or contradict the 15 Sept 2026 Bourdeau finding
(cyphersolver/stepney: offline-only, manuscript transcribed, THE=454 key rejected). None found a plaintext,
a key, or a claimed solution for this item anywhere. Findings by source:

1. **General web search (WebSearch/WebFetch), checked 20 Sept 2026.** Searched Stepney/Manchester/cipher/1702
   combinations, both solver repositories, and the Yale catalogue and TNA Discovery pages named in this file.
   Fetched Bourdeau's `cyphersolver/stepney/NOTES.md` directly from GitHub raw: it states the manuscript is
   located and fully transcribed, the key is not THE=454, 24 groups of an unknown two-part nomenclator cannot
   be broken, and no image of a key for 1702 or a deciphered Stepney letter was found in Yale's digitised
   Manchester papers (which hold only THE=452 and THE=454, both 1699-1700). Bourdeau's project index
   (dbourdeau.github.io/cyphersolver) has no separate, more-recent entry for this target. Aymeloglu's
   `unsolved-ciphers` repository (profile, PRs, README) has no mention of Stepney or Manchester at all.
   No independent scholarship, blog or catalogue note anywhere claims a solution. **Unchecked:** the Yale
   catalogue page collections.library.yale.edu/catalog/2046948 returned blank content (likely JS-rendered).
   Verdict contribution: closed-negative (no solution found).

2. **Internet Archive / HathiTrust / printed-edition search for the letter itself, checked 20 Sept 2026.**
   Read full OCR text of *Calendar of State Papers Domestic, Anne, vol. 1* (ed. R. P. Mahaffy, HMSO, 1916,
   archive.org calendarofstatep01greauoft): Stepney is named on unrelated business, no entry for 23 March 1702
   to Manchester, and "cipher" does not occur in the volume. Read full OCR text of *Court and Society from
   Elizabeth to Anne, edited from the Papers at Kimbolton* by William Drogo Montagu, 7th Duke of Manchester
   (1864, archive.org courtandsociety00mancgoog) — the Manchester family's own edition of the same Manchester
   Papers this letter belongs to: it prints exactly one Stepney-to-Manchester letter, dated Bruxelles, 28 March
   1707, in clear, recommending a Mr Hicks; not this letter, no cipher passage. Read full OCR of William Coxe,
   *Memoirs of the Duke of Marlborough* (1847-48, archive.org bub_gb_Hen1pnVNqeMC): Stepney appears only in
   1704-05 business, nothing from March 1702 or to Manchester. The DNB (1898) entry for George Stepney lists
   printed sources for "some of his correspondence" (Hill's *Familiar Letters* 1767, Hardwicke's *Miscellaneous
   State Papers* 1778, Warner's *Epistolary Curiosities* 2nd ser. 1818, Coxe, and the *Gentleman's Magazine*)
   but none is identified as containing this letter, and only Coxe was checked directly. Yale's own catalogue
   description (known only via a search-engine snippet, since the live page would not render) confirms the item
   — "partly in cipher, dated March 23, 1702" — but is a manuscript record, not a printed plaintext edition, and
   claims no decipherment. **Unchecked (not searched negative):** British History Online's scanned CSPD pages
   (gated behind a "gold subscription"); HathiTrust's catalogue search (403 to curl; no matching Stepney volume
   surfaced by web search either, so treated as unchecked rather than confirmed absent); the Historical
   Manuscripts Commission's 8th Report, Appendix Part II (Manchester/Kimbolton manuscripts, 1881), the most
   likely printed calendar entry for this exact letter, which could not be located as digitised text in this
   session. Verdict contribution: closed-negative on the sources actually read; several likely sources remain
   unchecked.

3. **Community lists and comment threads, checked 20 Sept 2026.** Cryptiana's unsolved-ciphers page
   (sources/cryptiana/web/unsolved.htm, local snapshot) lists this exact item under "George Stepney to Earl of
   Manchester (1702)" as not deciphered, with no linked blog post (unlike most other entries on that page).
   Cipherbrain (scienceblogs.de/klausis-krypto-kolumne, Klaus Schmeh) has a separate, unrelated "Manchester
   Cryptogram" post (2 March 2014, 12 comments through 25 April 2017, by Schmeh with commenters cimddwc, rolak,
   Pnugi, Helmut, Peter Lichtenberger, Wikka, Thomas Ernst) about a different item: Fontainebleau, 20 Sept 1783,
   signed "Manchester", to Sir John Stepney — same two families a generation on, deemed likely hopeless by the
   commenters, no key or plaintext posted, and not this target. Cipherbrain's own site search for "Manchester
   1702" and "George Stepney" returned no matching posts; Cipher Mysteries' (Nick Pelling) search for "Stepney"
   returned no results; MysteryTwister C3's challenge listing has no occurrence of Stepney or Manchester.
   **Unchecked:** r/codes on Reddit (search page redirects to a login wall, JSON API returns 403, and the
   headless-browser fallback failed on an untrusted proxy CA that this session did not attempt to fix via a
   TLS-weakening action); MysteryTwister C3's own keyword-search endpoint (only the front listing page was
   read). Verdict contribution: closed-negative on what could be read; two forums unchecked.

4. **DECODE database (de-crypt.org), checked 20 Sept 2026, no DECODE_USER/DECODE_PASS set in this
   environment.** Public record ID 2864 matches the Yale item exactly: "Yale_Beinecke_OSB_fc37_box08_folder40",
   Osborn fc37 Box 08 Folder 40, dates 1702-1702, author "G. Stepney", city "Manchester?", content type
   "Cipher", symbol set "Numerical", 7 pages, **Status field verbatim "Non-decrypted"**, 8 manuscript-page
   images attached (photographs only, no key or decipherment document visible), record created 2022-01-05.
   No DECODE record exists for the TNA shelfmarks (SP 105/65, SP 80/18, C3609655) — DECODE only catalogues the
   Yale copy. A search on "Manchester" surfaces the wider Manchester Papers cipher series (other Beinecke OSB
   fc37 folders, 1697-1737, various authors) with no visible solved companion record for this item on the
   results page reached. **Unchecked:** record 2864's DocumentsList and AssociatedRecordsList sub-pages, which
   would show any attached key file or linked solved companion record, both require login this environment
   lacks. Verdict contribution: independently confirms "Non-decrypted" as of the DECODE record's own status
   field; closed-negative on what is publicly visible.

5. **dbourdeau/cyphersolver repository, shallow-cloned, HEAD commit cf73f46, checked 20 Sept 2026.** Direct
   file reads (not web fetch) confirm the same verdict as source 1: `stepney/NOTES.md` — "OFFLINE-ONLY
   (manuscript located and fully transcribed; the key is not the THE=454 Manchester cypher; 24 groups of an
   unknown two-part nomenclator cannot be broken; the key/plaintext should exist in TNA or BL material that is
   not online)"; `TARGETS.md` row 10 (dated within the row 15 Sept 2026, by Daniel Bourdeau) adds that Schmeh's
   Top 50 entry 34 (the 1783 Cipherbrain item, see source 3) is the same two families a generation on, and that
   the Clements Library told a reader in 2017 one letter is not enough for cryptanalysis, a corpus would be
   needed — the same conclusion reached independently for this target; `README.md`, `docs/index.html` (grey
   "offline" marker, not the green solved marker used for neighbouring solved targets like yard1699) and
   `docs/writeups.html` (no linked write-up page, unlike solved targets) all agree; `SOLVED_CATALOGUE.md`
   contains zero occurrences of "stepney". No key.json or plain.txt exists in the stepney/ folder. Verdict
   contribution: closed-negative, and directly corroborates the prior offline-only status this file already
   recorded from Bourdeau, 15 Sept 2026.

6. **aaymeloglu/unsolved-ciphers repository, shallow-cloned, and Robert Pitt's GitHub profile, checked
   20 Sept 2026.** No target folder, README/TARGETS/SHORTLIST/CATALOGUE entry, or write-up mentions Stepney or
   Manchester anywhere in the repository (full-repo grep, case-insensitive). The repo's own harvested mirror of
   the DECODE database carries the same record 2864 verbatim (`catalogue/decode-records.jsonl` line 634,
   `catalogue/decode-catalog.csv` line 7335) as a raw catalogue entry, not a solve attempt, and it does not
   appear in the repo's own ranked shortlist (`decode-ranked.md`) or `exclude.txt`. Robert Pitt's GitHub
   profile (30 repositories) has no repository or description referencing Stepney or Manchester; his
   historical-cipher repos are forster-cipher, le-tellier-1657 and charles-i-boswell-cipher, none matching.
   Verdict contribution: closed-negative.

**People and dates of record for prior work on this target:** manuscript located and transcribed, and the
THE=454 key tested and rejected, by Daniel Bourdeau (github.com/dbourdeau/cyphersolver), recorded
15 Sept 2026; catalogued (not solved) in the DECODE database (DECRYPT project) as record 2864, created
2022-01-05, status "Non-decrypted"; listed as undeciphered by Satoshi Tomokiyo on Cryptiana's unsolved-ciphers
page (undated on that entry, page current through 2025-09), with one correction to Tomokiyo's transcribed
ciphertext (413, not 412) made by Bourdeau. No solver, published edition, or archive has been found to claim a
key, plaintext or decipherment for this specific letter.

**Verdict: offline-only.** All six independent sweeps agree: the manuscript is located and transcribed, no
solution, key or plaintext has surfaced anywhere reachable, and the target remains blocked on archival material
(TNA SP 106 or BL Add MSS 7058-7078) not yet obtained. Nothing found here contradicts Bourdeau's 15 Sept 2026
assessment; several source families (British History Online's gated CSPD pages, HathiTrust's catalogue search,
the 1881 HMC Kimbolton report, DECODE's login-gated document pages, r/codes) remain unchecked rather than
searched negative and should not be read as clearing them.
