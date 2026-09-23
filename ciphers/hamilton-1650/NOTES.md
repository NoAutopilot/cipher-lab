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

## Print check, 20 Sept 2026

Free-source check for a printed decipherment of any of the four target letters, or of any other letter using
the same Hamilton-family cipher of 1648-50, or of a printed key. Internet Archive full-text/search-inside;
Google Books and HathiTrust catalogue were blocked (Google Books API HTTP 429, quota exhausted; HathiTrust
Cloudflare 403 to curl, consistent with the existing block logged above) and are unchecked by this pass, not
negative.

1. **Burnet, *Memoires of the Lives and Actions of James and William Dukes of Hamilton*, 1677 original
   edition.** Not located on Internet Archive (only the 1852 Oxford reprint already checked, plus a duplicate
   BSB scan of the same 1852 reprint, and an unrelated 1673 title by the same author that is not full-text
   indexed). Google Books/HathiTrust, which might hold it, were blocked. **Unchecked**, not negative.
2. **HMC Supplementary Report on the manuscripts of the Duke of Hamilton (1932).** Located on Internet Archive
   (`supplementaryrep0000grea`); full text is access-restricted (controlled digital lending), searched via IA's
   full-text-search API snippets only. No hit for the four target letters' dates or phrases. Found instead: the
   report calendars two earlier letters "to the Earl of Lanark" (same man, before he became 2nd Duke of
   Hamilton in March 1649) dated [Feb 1648] and [March 1648], noting "passages in italics on pages 70-4 are in
   cipher in the original" and quoting "...to trouble your Lop being in your first cipher with me." This
   indicates pp.70-74 print a decipherment of cipher passages in two 1648 letters to the same recipient — not
   confirmed to be the same nomenclator as the four 1650 letters, and not read past the search snippets (the
   item could not be opened in full). A lead, not a match: worth a full read of pp.70-74 before any claim about
   this being the same cipher.
3. **Gardiner (ed.), *Letters and Papers illustrating the relations between Charles the Second and Scotland in
   1650* (Scottish History Society, 1894).** Four IA copies searched; no hit for the four target letters. One
   unrelated decipherment found in the volume: Ormond's cipher, printed "from the interlined decipher" after he
   lost his key at Rathmines — a different correspondent, different cipher. No relevant match for this target.
4. **The Nicholas Papers (Camden Society, all located volumes).** Confirms Hamilton/Lanark as the same
   recipient again; all "cipher" hits concern other royalist correspondents (O'Neill, Ross/Rowe, Nicholas's own
   cipher) with no reference to a Hamilton cipher letter or the four target dates. No relevant match.
5. **Carte's Ormonde collection** (*Life of James Duke of Ormonde*, 1735 and 1851 editions, and the printed
   *Letters*). General remarks on Ormonde's own cipher correspondence, and mention of a different "Mr. James
   Hamilton" (an Ormonde correspondent, not the 2nd Duke) writing "in the same cipher... deciphered" — not this
   cipher, not this Hamilton. No relevant match.
6. **Phrase sweep** (Hamilton + Arran + 1650 + cipher + deciphered) across the above items: no further hits.

**Verdict:** No decipherment or key for the four target letters (6/14/31 Aug, 27 Sept 1650) was found in the
sources checked here. Two open threads for a follow-up pass, not acted on in this check: the 1677 Burnet first
edition (blocked by Google Books quota and HathiTrust's Cloudflare block, not searched), and HMC Supplementary
Report (1932) pp.70-74, which appear to print a decipherment of cipher passages in two 1648 letters to the same
recipient under his earlier title — worth reading in full to see whether it is the same nomenclator. This does
not change REQUEST.md; the archive order for GD406/1/2197 remains the fastest route to the key.

### Follow-up, 20 Sept 2026: the two Google-Books-quota threads, closed

`GOOGLE_BOOKS_KEY` works from this container but the API returns HTTP 403 "Cannot determine user location" unless
`&country=US` is appended to every call; with that, the two threads left open above are now checked.

1. **Burnet 1677 first edition.** Not found on Google Books: `intitle:Hamilton intitle:Castleherald`,
   `q=Burnet Memoires Hamilton 1677`, and `q=Burnet Dukes Hamilton Castleherald` return only the 1852 reprint,
   unrelated 20th-century reprints (Legare Street Press, 2023), and unrelated Grammont/Hamilton titles. Open
   Library gives OCLC 1828960, 23620856, and 613966038 for 1677 editions; the HathiTrust Bibliographic API
   (`/api/volumes/brief/oclc/<n>.json`) returns `{"records":{},"items":[]}` for all three — no HathiTrust holding.
   **Not found**, checked by Google Books full-text search and HathiTrust bibliographic lookup by OCLC; no
   digitized copy of the 1677 first edition was located by either route.
2. **1852 Oxford reprint, second scan.** Google Books holds a full-view copy, volume id `Zh9cAAAAcAAJ`, a
   different scan from the Internet Archive copy already checked (`archive.org/details/memoirsoflivesac00burn`).
   Searched inside it (via `intitle:Hamilton intitle:Castleherald "<phrase>"`, which reliably restricts hits to
   this volume) for "Dunfermline Declaration", "get you off", "sixth of August", "September 1650" beyond the
   narrative sentence already known, and "preparing yourself": no hit for the cipher-specific phrases. "cipher"
   gets one hit, snippet "...cipher, but I am afraid I shall hardly read it, for there is so little distance
   betwixt the numbers, that it seems but one continued number from the beginning to the end of every line, so
   that I must desire you henceforward to 19-I. 43 41 42 43 25..." — this is **not the target letters**: full
   context from the Internet Archive text of the same reprint (`memoirsoflivesac00burn_djvu.txt`, matches at
   line 3485) identifies it as Charles I to James, 1st Marquis of Hamilton, dated 25 Sept 1631, complaining that
   a letter of 22 Aug 1631 "from Stetin" is hard to decipher because the numbers run together, printed with the
   King's reply text and the leftover fragment "19-I. 43 41 42 43 25" left as numerals; a different cipher, a
   different Hamilton, 19 years before the target. The two scans agree (same passage, same wording, in both);
   no OCR advantage from the Google Books copy was found or needed. Also confirms the Arran-confinement narrative
   sentence already on record (line 28755 of the IA text: Dunbar "third of September 1650"), still narration,
   not a letter quote. **Not found:** no decipherment of the four target letters in this scan either.
3. **HMC 11th Report Appendix VI (1887).** Google Books has a full-view copy, volume id `Y0TwqQPL4lsC` ("Eleventh
   Report | Appendix. The manuscripts of the Duke of Hamilton, K.T.. Part VI"). Searched inside (`q=Hamilton
   Eleventh Report Appendix "cipher"`): the only hit is the same wording already found via the Internet Archive
   copy in the check-solved sweep — "...cipher, not de-ciphered, thanking the Duke for his offer of service,
   but... report was prepared, as narrated on page 202 infra..." — same items 395-396, no new content, no
   decipherment. **Not found**, and this Google Books copy adds nothing beyond the IA copy already on record.

Both open threads are now closed as not found by these two additional routes (Google Books full-text search,
HathiTrust bibliographic API). The HMC Supplementary Report (1932) pp.70-74 thread from the previous pass is
untouched by this one. Status unchanged: **offline-only**; REQUEST.md for GD406/1/2197 remains the fastest
route to the key.

## Print check follow-up, 20 Sept 2026 (IA-login worker)

Attempted the follow-up flagged above: borrow `supplementaryrep0000grea` with the IA_USER/IA_PASS login and
read the index plus the 1650 section (the four Charles II letters) and pp.70-74 in full. **Blocked**: the
login itself failed — archive.org requires an email address and IA_USER as set is not one (see Access
playbook, CLAUDE.md, "Credentials from the environment" §3, dated today). No page image or OCR text of this
restricted item could be read this session; the item could not be opened beyond the search-inside snippets
already on record above.

Within that limit, ran further `be-api.us.archive.org/fts/v1/search` queries against the same item, targeted
at the four letter dates specifically, to sharpen the existing snippet-only check: `"1650, August"` (no hit),
`"1650, September"` (one hit, "Hamilton to the Committee of Estates. 1650, September 14. — He begs that his
banishment..." — a different letter, Hamilton to the Estates, not Charles II to Hamilton), `"August 6"` (no
hit), `"in cipher"` (one hit, the same pp.70-74/1648 passage already on record, no other occurrence in the
volume). No hit anywhere in the volume for a cipher or deciphered passage tied to any of 6 Aug, 14 Aug,
31 Aug or 27 Sept 1650. This is consistent with, not additional proof beyond, the existing verdict: still
**not found in the sources checked**, and the pp.70-74/1648 passage is still an unconfirmed lead (same
recipient, different date and, on this evidence, no textual link to the 1650 letters) that needs a full read,
not a search-inside snippet, to settle. Status unchanged: **offline-only**.

## Print check follow-up, 21 Sept 2026 (IA login worker 2)

Retested the IA login now that IA_USER is set to an email address (rotated ~21 Sept 2026, per ROOM.md/CLAUDE.md).
**Still blocked**: `POST https://archive.org/services/xauthn/?op=login` with the corrected email-format IA_USER
returns HTTP 401, `{"success": false, "values": {"reason": "account_not_found"}}` — the same error the prior
worker got with a non-email IA_USER, but now for a different reason (the value is syntactically a valid email;
archive.org simply has no account registered under it, or the account exists but is not password-login-enabled,
e.g. sign-in-with-Google only). One attempt only, per the no-repeat-retry rule (lockout risk); not retried
further this session. `tools/ia_borrow.py`'s login step and CLAUDE.md's Access playbook are updated with this
finding; the person needs to check which archive.org account IA_USER/IA_PASS are meant to reach (flagged in
ROOM.md and ASKS.md). `supplementaryrep0000grea` could not be borrowed or opened beyond search-inside snippets
this session either.

With login still unavailable, tried the two remaining free routes instead of a third login attempt:
1. **HathiTrust Bibliographic API by OCLC.** The IA item's own metadata gives `urn:oclc:record:1151348305`;
   `catalog.hathitrust.org/api/volumes/brief/oclc/1151348305.json` returns `{"records": {}, "items": []}` —
   no HathiTrust holding for this OCLC number at all, so the HathiTrust route (blocked for other reasons
   before) is now confirmed to have no copy to be blocked from.
2. **Google Books.** `intitle:"Supplementary Report" intitle:Hamilton Manuscripts` (with `&country=US`) finds
   nine catalog entries for this and related HMC Hamilton titles (1887 and 1932 reports, a 2009-2010 reprint of
   the related Supplementary Report vol. 2), but every one is `viewability: NO_PAGES` — no preview, no
   search-inside, nothing readable.

No new route located to read pp.70-74 (the 1648 cipher-passage lead) or the 1650 section itself. Status
unchanged: **offline-only**; the pp.70-74 lead is still open and unread. No key, deciphered passage, or
description of the family cipher for the four target 1650 letters was found in any source reachable this
session.

## Print check follow-up, 23 Sept 2026, 21:51 UTC (credential session, ytbiz account)

archive.org login now works (the person registered the account; `services/xauthn/?op=login` returned
`{"success": true}` this session). `tools/ia_borrow.py` was run against `supplementaryrep0000grea` (HMC
Supplementary Report, Hamilton, 1932) as the named page check for pp.70-74 and the 1650 section: the
one-hour SESSION_LOAN opened (`browse_book` success, `lendingInfo.userHasBrowsed` true, 300 leaves in the
BookReader manifest) and was returned at the end of each of four short sessions (`return_loan` true every
time; nothing is held). The page-image step was debugged and now reaches the image server (details in the
script's docstring), but this item is a controlled-digital-lending item (`shouldProtectImages` true) and the
server hands the leaf to the web reader in an obfuscated form, not as a JPEG. Decoding that outside
archive.org's reader would circumvent the lending protection, so it was not done and the script now stops
on such a payload. **Result: pp.70-74 and the 1650 entries were not read this session.** They can be read
by the person in the archive.org reader (borrow the item at archive.org/details/supplementaryrep0000grea,
one hour at a time) or, for presence/absence only, through the `be-api` search-inside snippets already on
record above. Status unchanged: **offline-only**. Requests this session: archive.org 4 logins and 4 loans
(all returned), about 25 requests in all; ia800406/ia600406.us.archive.org 8.
