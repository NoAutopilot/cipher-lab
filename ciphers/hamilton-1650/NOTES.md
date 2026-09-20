# Charles II to the Duke of Hamilton, August-September 1650

- **Status:** Open. Offline-only. The key is located in the archive and catalogued as open; nothing more can be
  done from published sources. This is the first target of the archive-request lane (see `REQUEST.md`).
- **Plaintext language:** English.
- **Source of ciphertext:** two printed witnesses, collated in `ciphertext.txt`. Gardiner (Camden Society 1880)
  printed the figures from the manuscripts and left them undeciphered; the 1766 *Account of the Preservation of
  King Charles II* printed them earlier. Where the two disagree (five places) both readings are kept and the
  microfilm of the originals will settle them.
- **Prior work:** Tomokiyo, charlesii.htm section 2, lists it and identifies 132 as Dunfermline. Bourdeau
  (cyphersolver/hamilton, 14-15 Sept 2026) collated the witnesses, established that the Camden volume cannot yield
  the key (Gardiner says the letters came "without any key being appended"), found the key's shelfmark in the NRS
  catalogue, and parked the item as offline-only. Aymeloglu's shortlist notes a second possible key location, John
  Wallis's papers at the Bodleian, which hold royalist letters he deciphered in 1650.
- **What is in the cipher:** 102 groups, 67 distinct, range 3-384. A small nomenclator. Groups under about 90 are
  probably letters and nulls, 100 and above words and names. 3 and 10 sit at the ends of runs three times each,
  so probably nulls or a terminal letter. Bare code words in clear: 163, 122, 223 (persons: agents or bearers),
  132 (the dateline). Repeated pairs across letters: 237 70, 192 ... 308 100, 308 290, 58 135 256 58 256.
- **Why it cannot be broken from the text:** 102 groups with almost no redundancy is far below what any solver
  reads. Bourdeau's judgement, and the matched-control discipline in LESSONS.md, both say stop here.
- **Historical frame, for checking the reading when the key comes:** Hamilton was confined to the Isle of Arran
  from the King's landing in June 1650 until January 1651. On 6 August the Kirk had just removed Charles from the
  army at Leith and was pressing the Dunfermline Declaration, signed 16 August; the "two things" are probably the
  declaration and the army. 31 August is three days before Dunbar. 27 September, "I have at last resolved that
  ... by the ...", is the decision that became the Start, Charles's flight from Perth to the Highland royalists on
  4 October; "preparing yourself ... to get you" is about getting Hamilton off Arran.
- **When the copies arrive:**
  1. Transcribe each of the five key sheets in GD406/1/2197 as `key-<item>.tsv` (number, value). Do not merge
     them; the 1650 key may be one sheet, or none of them.
  2. `python3 apply_key.py key-<item>.tsv` renders all four letters. A key that gives English in the runs and
     sensible names for 163, 122, 223 is the one. Grade every group H (read from the key sheet) and mark any
     group absent from the sheet M.
  3. If no sheet fits, order the microfilm frames of Red Book ii nos. 156-159 to check the printed figures,
     and try the Bodleian Wallis route.
  4. Send the result to Tomokiyo and to Bourdeau, who will record it.

## Check-solved sweep, 20 Sept 2026

Six independent searchers checked whether this target is still unsolved, per convention 1. All six report the
same conclusion: no solution, key, or plaintext for GD406/1/2197 has surfaced anywhere they could reach, and the
existing NOTES.md claim (Bourdeau, cyphersolver/hamilton, 14-15 Sept 2026: key exists at NRS GD406/1/2197, not
recoverable online) is independently corroborated, not contradicted.

1. **Web search (WebSearch/WebFetch only, no archive access attempted).** Checked general search engines,
   dbourdeau/cyphersolver (site and raw NOTES.md), and aaymeloglu/unsolved-ciphers front page for any mention of
   a solved Hamilton/Charles II 1650 cipher. Found: dbourdeau/cyphersolver's own hamilton/NOTES.md, quoted
   verbatim, confirms the "OFFLINE-ONLY (2026-09-15)" status and the GD406/1/2197 key location. No third-party
   solution claim anywhere. **Not checked** (no reachable URL found by search, not a negative result): Tomokiyo's
   charlesii.htm page content directly, de-crypt.org's internal search, full text of the 1766 Account and Camden
   1880 on IA/HathiTrust/Google Books, and aaymeloglu's repo beyond its front page.

2. **Internet Archive full text + HathiTrust catalogue.** Fetched and grepped the full text of Gardiner's
   *Hamilton Papers* (Camden Society n.s. 27, 1880, archive.org/details/hamiltonpapersbe00hamirich), the 1766
   *Account of the Preservation of King Charles II* (archive.org/details/bim_eighteenth-century_an-account-of-the-
   preser_charles-ii-king-of-eng_1766), Burnet's *Memoirs of the Dukes of Hamilton* (1852 reprint,
   archive.org/details/memoirsoflivesac00burn), and HMC 11th Report Appendix VI, *Manuscripts of the Duke of
   Hamilton* (1887, archive.org/details/manuscriptsofduk00greauoft). All four cipher letters (6, 14, 31 Aug and
   27 Sept 1650) are printed in both the 1766 Account and Gardiner 1880 as undeciphered numeral groups matching
   `ciphertext.txt`; Gardiner's own preface says letters reached him "without any key being appended." The HMC
   1887 calendar independently (i.e. not from Gardiner) describes items 395-396 as "partly in cipher, not
   deciphered" and "chiefly in cipher." Burnet narrates Hamilton's Arran confinement but does not quote or
   decipher the letters. **Blocked:** catalog.hathitrust.org returned HTTP 403 to curl; the same 1766 edition
   was obtained from the Internet Archive instead, so the check was completed via a different route, not left
   undone.

3. **Community-list sweep** (Cryptiana local snapshot + live search, Cipherbrain, Cipher Mysteries,
   MysteryTwister, r/codes). Cryptiana's charlesii.htm (S. Tomokiyo) prints the same undeciphered 1766-Account
   excerpts, not a solution. Cryptiana's unsolved.htm explicitly lists the item as unsolved and names the same
   Wallis/Bodleian lead already in this file's Prior Work line. No hit on Cipherbrain, Cipher Mysteries,
   MysteryTwister, or r/codes naming this item at all. **Not checked, listed as unchecked, not negative:** any
   comment posted only inside JS-rendered threads on ciphermysteries.com (HTTP 406 to curl) or reddit.com/r/codes
   (HTTP 403 to curl); these domains were covered only via WebSearch `site:` queries, not a browser fetch.

4. **DECODE database (de-crypt.org).** Browser-driven searches of the DECODE Records list for "Hamilton",
   "GD406", "Duke of Hamilton", "Charles II", and "1650" returned no record for this item. The few genuine
   Hamilton hits are unrelated people/centuries (BL Add MS 32256, BL Add MS 72438, BL Add MS 33591 f.165 — the
   last already marked "Decrypted" but concerning Thomas Randolph/1559, not this letter). The "Charles II" and
   "1650" searches surfaced only French BnF material and Restoration-era Kew State Papers box 6 keys (1660-1685),
   none from NRS. No DECODE record id for hamilton-1650 exists anywhere in this repo's CATALOG.md/LANDSCAPE.md
   (unlike some other targets, which do cite DECODE ids). **Partial:** only the first of six result pages for
   the "1650" query (20 of 103 rows) was read; the brief did not call for an exhaustive scan of every "1650"
   record, so the remaining 83 rows are unchecked, not negative.

5. **github.com/dbourdeau/cyphersolver (shallow clone).** Confirms, by reading the repository's own working
   files directly rather than a summary, everything the existing Prior Work line attributes to Bourdeau:
   TARGETS.md row 3 and hamilton/NOTES.md both state the key exists at NRS GD406/1/2197 ("Keys for ciphers used
   in the correspondence of the Duke of Hamilton," c.1645, 5 items, open access, found 2026-09-14), that Gardiner
   1880 "evidently never saw 2197," and the status block "OFFLINE-ONLY (2026-09-15) ... Nothing further can be
   done online; parked." hamilton/collate.py reproduces the 102-group/67-distinct collation with no key or
   decipherment attempted. No entry for this item exists in SOLVED_CATALOGUE.md, CATALOGUE.md, SOLVED_RANKING.md,
   catalogue.json, or docs/search.json — consistent with it being carried as unsolved/offline, not written up as
   solved.

6. **github.com/aaymeloglu/unsolved-ciphers (shallow clone) and github.com/robertpitt (web UI repo-name
   filter).** No `hamilton-1650`-named folder exists in aaymeloglu/unsolved-ciphers (11 target folders, none for
   this item). SHORTLIST.md lists the item twice, both as open: once under "Tier 2: real, open, more friction"
   naming the same Wallis/Bodleian lead, and again in a 2026-09-13 status-check row noting "No solve claims
   found." robertpitt's GitHub account (107 repos) has no repository name matching "hamilton" or "1650"; a
   name search for "charles" returns only the unrelated `charles-i-boswell-cipher` (Charles I, not Charles II;
   Boswell, not Hamilton; 1643, not 1650). **Not checked, listed as unchecked, not negative:** full-text search
   of all 107 of robertpitt's repos (GitHub search/API endpoints were blocked in the sandbox; only repo
   name/description matching via the web UI was available), and the full internal contents of
   aaymeloglu/unsolved-ciphers beyond README/TARGETS/CATALOGUE/SHORTLIST.

**People and dates for prior work found by this sweep, all already on record:** S. Tomokiyo (Cryptiana,
charlesii.htm and unsolved.htm, undated snapshot) transcribed the printed cipher and flagged the Wallis/Bodleian
lead; Bourdeau (cyphersolver/hamilton, 14-15 Sept 2026) collated the two printed witnesses, ruled out Camden 1880
as a key source, located GD406/1/2197 in the NRS catalogue, and parked the item offline-only on 15 Sept 2026;
Aymeloglu's shortlist (status-check dated 2026-09-13) independently lists the same item open with the same
Wallis lead and no solve claim; HMC's 1887 cataloguer independently confirmed the letters were printed
undeciphered.

**Verdict:** No solution, key, or plaintext for this cipher was found by any of the six searchers; the prior
"open, offline-only, key at NRS GD406/1/2197" status is independently confirmed, not contradicted, so the
target's status is unchanged: **offline-only**.
