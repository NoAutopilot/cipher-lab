partial

# BL Harley MS 287 cipher letters 1587-88: Cobham to Walsingham (4), Needham, unsigned (7) — DECODE R8477-R8496

- Source: QUEUE.md rank 13 (score 33), scored 20 September 2026; catalogued from the DECODE record range
  (de-crypt.org/decrypt-web/RecordsView/8477 through 8496) via Bourdeau's `cyphersolver` catalogue harvest.

## Check-solved sweep (23 September 2026)

1. **Web search.** "Harley MS 287 Cobham Walsingham cipher 1587 1588 solved decrypted" — no page reports this
   volume decrypted; results are about the unrelated Babington Plot and Mary Stuart ciphers. found=false from
   open web search.

2. **Print.** The 20 September 2026 search-print pass already recorded in QUEUE.md checked CSP Foreign Elizabeth
   vol. 21 pt 4 (Jan-June 1588, british-history.ac.uk) in detail: the index and text around pp.442-460 give only
   English abstracts and a postscript note ("Sent the cipher by Spritwold"), never a reproduced or "deciphered"
   cipher passage, and "Needham" indexes to a single unrelated entry. Vol. 22 (July-Dec 1588) is on HathiTrust
   (htid `msu.31293027027295`, full view) but Cloudflare-blocks curl and the browser tool; the HTRC Extracted
   Features API located a candidate page (scan 62, adjacent to a Cobham mention, with both "cipher" and
   "decipher" tokens) but it remains unread. Not re-run this sweep; status unchanged: NOT FOUND in print,
   vol. 22 inconclusive. Google Books: not available in this account's environment (no key set here).

3. **Community lists.** `sources/cryptiana/web/elizabeth.htm` (grepped locally, never edited) documents Lord
   Cobham's separate 1588 ciphers with Burghley and Walsingham in general terms (Burghley providing a cipher in
   April 1588, Cobham sending one to Walsingham in June 1588) but does not mention Harley MS 287 or these DECODE
   records specifically, and prints no decipherment. Cipherbrain/scienceblogs.de site search for this item
   returned no matching post (see full log method in ciphers/charles-rupert-1645/NOTES.md item 3); full-page
   fetches of scienceblogs.de are blocked by this environment's egress policy, so only WebSearch snippets could
   be checked. found=false in Cryptiana; unread/unreachable on Cipherbrain.

4. **DECODE.** `curl -A "Mozilla/5.0" https://de-crypt.org/decrypt-web/RecordsView/R8477` — connection refused
   at the egress proxy (`CONNECT tunnel failed, response 403`, HTTP code 000; `connect_rejected — organization
   policy`). de-crypt.org is unreachable at all from this account's environment; no login attempted
   (DECODE_USER/DECODE_PASS unset here). Source: **unreachable**.

5. **Bourdeau (`github.com/dbourdeau/cyphersolver`, shallow clone 23 Sept 2026, MIT code / CC BY 4.0 text).**
   **found=true, substantial.** Bourdeau's project has already worked most of this DECODE range, in three
   folders, all dated 21-22 September 2026 (i.e. after our own 20 September 2026 search-print pass):
   - `needham1587/` (DECODE R8479, Francis Needham to Walsingham, 28 July 1587, ff.39-40): **read**,
     `fraction_read: 0.978` (182/186 unglossed signs; grades H:44, M:1), one word on one line unresolved. Cipher
     identified as a three-grid pigpen keyed to Thomas Wilkes (per CSP Foreign vol. 21 pt 3's editorial note on
     BL Add MS 5935, not itself online). CATALOGUE.md does not list a public write-up URL for this one.
   - `harley287/` (catalogue item 132: R8477 f.11 + R8482-R8487, Lord Cobham at Ostend to Walsingham, 20 and 22
     March 1587/8): **read in part**. Every cipher run of ff.70r-72v is read in sense (crib-based: "commaunded
     to attend", "that bearer hath", "under colour thereof" etc. fixed most letter values, confirmed
     independently by the `cobham1588` session against contemporary glosses on f.89/R8493); open items are code
     number 42, code sign ".7.", one Jesuit's surname, one verb, and scattered words, with the share of tokens
     read explicitly **not measured** (the 22 Sept 2026 entry in that folder's own profile.json downgrades it
     from "read" to "read in part" precisely because no token-level fraction was ever computed — note that the
     top-level `CATALOGUE.md` line still says "read" for this item, unreconciled with the folder's own later
     correction; we report the folder's own current, more conservative status). R8477 (f.11) is confirmed a
     different letter and code (about eight groups), not read, too short for a key. Write-up:
     https://dbourdeau.github.io/cyphersolver/harley287.html.
   - `cobham1588/` (catalogue item 131: R8490, R8492, R8495, R8496, Cobham to Walsingham, 5 May - 9 June 1588):
     **read in part**, `fraction_read: 0.35` (estimated, "about a third of the cipher words," not token-counted
     against a full sign transcription). Key partly rebuilt from the glossed sibling letters in the same volume;
     several signs remain unglossed or polyphonic (K, upsilon, rho, W; wedge s/t/a, gamma r/y). Write-up:
     https://dbourdeau.github.io/cyphersolver/cobham1588.html.
   DECODE key record R8497 (f.187, Bodley's cipher, December 1590) was checked by Bourdeau's project and
   confirmed a different, unrelated system, consistent with our own 20 September 2026 note. No print source was
   found by that project either (same CSP Foreign vol. 21 pt 4 negative result independently reached).

6. **Aymeloglu (`github.com/aaymeloglu/unsolved-ciphers`, shallow clone 23 Sept 2026; no licence, cite only, no
   code copied).** No target folder and no catalogue-file mention for Harley MS 287 or any R848x/R849x record
   (`grep -rli` across the repository returned zero matches). found=false (not attempted in this repository).

## Verdict

**Partial**, not open. This is not a single undisturbed target: Bourdeau's project has already produced real,
publicly committed partial-to-near-complete readings covering most of the named DECODE range (needham1587 ~98%
read; harley287/R8477+R8482-R8487 read in sense throughout with named gaps; cobham1588/R8490+R8492+R8495+R8496
about a third read), all dated 21-22 September 2026, citing Lasry-style key-recovery from contemporary glosses
rather than a printed source (none was found by their project or by this sweep). No fully "found-solved" claim
applies because none of the three sub-items is complete and cobham1588 in particular is far from it. This
project should not restart this item as an unattempted cryptanalysis target; any further work here is a
finishing/verification job on Bourdeau's existing partial key and transcriptions (MIT code, CC BY 4.0 text —
cite, do not silently duplicate). No Stage 2 line applies (verdict is not "open"). QUEUE.md row 13 has been
annotated with this finding rather than moved to Dropped, since the item is not fully solved.
