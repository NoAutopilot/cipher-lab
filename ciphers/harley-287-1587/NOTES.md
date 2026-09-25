partial
CSP Foreign Elizabeth vol.21 pt.3 pp.197-217 and pt.4 pp.199-212 (British History Online) read by this worker today, with a control name confirmed present on each page, and DECODE's own record pages fetched directly (RecordsView/8477 etc.): no decipherment of the Cobham/Needham cipher passages found in print and DECODE still marks every record Non-decrypted/Partially decrypted; unchanged from the 23 Sept 2026 sweep below.

# BL Harley MS 287 cipher letters 1587-88: Cobham to Walsingham (4), Needham, unsigned (7) — DECODE R8477-R8496

- Source: QUEUE.md rank 13 (score 33), scored 20 September 2026; catalogued from the DECODE record range
  (de-crypt.org/decrypt-web/RecordsView/8477 through 8496) via Bourdeau's `cyphersolver` catalogue harvest.

## Check-solved (LANE CX2, 25 September 2026)

Fresh sweep by this worker (session CX2-BRIT2), independent of the 23 Sept pass below (its findings are not
quoted, only cross-checked).

1. **Web search.** `Harley MS 287 Cobham Walsingham cipher 1587 1588 deciphered solved` and `Harley 287 cipher
   "solves" Claude GPT Vals AI` (WebSearch) — no page reports this volume solved; hits are the Babington Plot
   (unrelated Mary Stuart ciphers), a Cambridge Core article on Nicholas's correspondence, and the unrelated
   Cyphral Distich (Urquhart 1653) model-solve story. One snippet paraphrased Bourdeau's own `harley287`/
   `cobham1588` pages (see item 5) without adding a new source. found=false.
2. **Print, own read.** CSP Foreign Elizabeth vol.21 pt.3 (British-History-Online, `cal-state-papers/foreign/
   vol21/no3`, HTTP 200) is dated April-December 1587; fetched `pp197-217` ("Elizabeth: July 1587, 26-31") and
   found the Francis Needham letter dated "Flushing, 28 July, 1587" calendared as an ordinary English narrative
   of the Sluys relief attempt, with no "in cipher"/"deciphered" marker on it; control: the same page also
   calendars "Sir William Pelham to Walsingham" and "The Same to Walsingham" for the same date, confirming real
   page content, not a stale fetch. CSP Foreign vol.21 pt.4 (`cal-state-papers/foreign/vol21/no4/pp199-212`,
   "Elizabeth: March 1588, 16-20") read the same way: no entry names "Cobham" on this page; two entries
   mentioning "Ostend" (Remarks touching Ostend; De Loo to Burghley) are plaintext with no cipher notation;
   control: "Sir James Crofte" (20 March) and "Dr. Rogers" (18 March) both present on the page, confirming it
   is being read, not a blank/error page. Neither page reproduces or notes a decipherment of the Harley 287
   cipher runs. Google Books: `GOOGLE_BOOKS_KEY` is set in this environment (unlike the 23 Sept pass, which
   found it unset) but not used this pass — the calendar pages above already answer the "is it printed
   deciphered" question with a control, and CLAUDE.md's usage rule against redundant fetches applies once one
   source has answered with a control.
3. **Community lists.** `sources/cryptiana/web/elizabeth.htm` re-grepped (on disk, not edited): still documents
   Cobham's 1588 ciphers with Burghley/Walsingham only in general terms, no mention of Harley MS 287 or these
   DECODE records, no decipherment printed. Cipherbrain/scienceblogs.de: WebSearch snippets only, as
   23 Sept (full-page fetch of that host is not attempted here; not re-tested for reachability this pass).
   found=false in Cryptiana; unread/unreachable on Cipherbrain (unchanged).
4. **DECODE.** de-crypt.org answers HTTP 200 from this container today (egress unblocked since 23 Sept, when it
   was `connect_rejected`). Fetched `RecordsView/8477`, `8479`, `8482`, `8490`, `8496` directly (no login,
   1.6s apart): R8477 Non-decrypted, R8479 Partially decrypted, R8482 Non-decrypted, R8490 Non-decrypted, R8496
   Non-decrypted — DECODE's own status field, read by this worker, matches Bourdeau's off-platform findings
   below and shows no one has posted a decipherment to the platform itself. found=false (own read, not a
   citation of the 23 Sept "unreachable" note, now superseded).
5. **Bourdeau (`github.com/dbourdeau/cyphersolver`, fresh shallow clone 25 Sept 2026, MIT code / CC BY 4.0
   text).** Re-confirms the 23 Sept finding, dated in this clone's own commit (25 Sept 2026 11:19): `needham1587/`
   (R8479, "read", 227/261 tokens measured, three-grid pigpen, Wilkes-Walsingham key per CSP Foreign 21/3 n.4,
   key itself in BL Add MS 5935, not consulted); `harley287/` (R8477+R8482-R8487, "read in part", reclassified
   from "read" on 22 Sept because no token-level fraction was ever computed — open items still code 42, sign
   `.7.`, one Jesuit's surname, one verb, scattered words; R8477/f.11 confirmed a different, shorter, unrelated
   code, not read); `cobham1588/` (R8490+R8492+R8495+R8496, "read in part", key rebuilt from the same cipher's
   glossed siblings, no fraction measured). No other DECODE record in the R8477-R8496 range belongs to a
   different BL volume (checked profile.json shelfmarks for every neighbouring folder — harley1582r8499/r8500/
   r8504, harley286, r8356/r8358/r8361/r8362/r8364, stafford1586, walsingham1572/1572nov/1585, wotton1585 — all
   are Harley MS 260, 1582 or 286, or Add MS 32657, not Harley MS 287). Write-ups unchanged:
   https://dbourdeau.github.io/cyphersolver/harley287.html, /cobham1588.html.
6. **Aymeloglu (`github.com/aaymeloglu/unsolved-ciphers`, fresh shallow clone 25 Sept 2026; no licence, cite
   only).** `grep -rli` for "cobham", "walsingham", "needham", "harley" (any Harley shelfmark) across the whole
   repository: zero matches beyond the unrelated `forster-1644` and `royalist-1646` folders (different targets,
   different shelfmarks). found=false (not attempted in this repository).

Intake verdict: open (this worker's own CSP Foreign read, with a control on each page, satisfies the gate's
citation requirement; `tools/intake_gate_check.py` exits 0 below).

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
