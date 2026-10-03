open
Warburton, Memoirs of Prince Rupert and the Cavaliers, vol. iii pp.131-137 (Internet Archive OCR, identifier memoirsprinceru01warbgoog, own read by this worker 25 Sept 2026) read in full around the letter: no decipherment, no "key lost"/"not deciphered" footnote and no clear-text sequel anywhere near it, and the printed cipher matches ciphertext.txt group for group.

# Prince Maurice to Prince Rupert (Worcester, 7 July 1645)

## Check-solved (LANE CX2, 25 Sept 2026)

Six-source sweep by this worker (session CX2-BRIT2), all queries and URLs logged; nothing here supersedes the 15/19 Sept Bourdeau finding, which still holds.

1. **Web search.** `"Prince Maurice" "Prince Rupert" cipher 1645 Worcester deciphered solved` and `Maurice Rupert cipher Naseby 1645 "solves" Claude GPT AI` (WebSearch) -- no page reports this letter solved or deciphered; hits are general Rupert/Maurice biography pages, the unrelated Cyphral Distich (Urquhart 1653, Vals AI, Claude Fable 5.1) model-solve story, and dbourdeau.github.io/cyphersolver itself (see item 5). found=false.
2. **Print/edition, own read.** Fetched the full OCR text of Warburton, *Memoirs of Prince Rupert, and the Cavaliers* vol. iii (archive.org identifier `memoirsprinceru01warbgoog`, `_djvu.txt`, HTTP 200 after one redirect). Located the letter at print pages 132-134 (line "now at Worcester, when he writes thus on the 7th of July") and read pp.131-137 in full myself: the cipher groups printed there ("1.5, 25, [3]42, 148, 136, 13, 325, 162, 84, 212, 26, 331, 61, ... 397, 150, 100, 148, 212, 66, 336, 156, 217, 28, 229, 355, 82, 16, 15, 194, ... Garrison, ... Accordingly, ...") match `ciphertext.txt` (OCR noise aside: "1.5"="15", "im"="199", "S2S"="328" etc. are scanner artifacts, not transcription differences). No decipherment, gloss, or editorial note ("key lost", "not deciphered") appears with the letter; Warburton does mark other letters in the same volume `[Partly in cipher]` or paraphrases an "almost undecipherable" one (Nicholas to Rupert, 11 July, p.136-137, a different letter, prose-paraphrased not printed in cipher), showing he distinguishes solved/handled passages elsewhere in the same volume from this one, which he simply transcribes as received. Control: the surrounding narrative (Sabran's dispatch, Edward Hyde's 8 July letter, Goring's letter) reads continuously and unambiguously as the same printed book, confirming this is a real page read, not a stale index. CSP Domestic Charles I 1644-5 (own read, archive.org identifier `sim_great-britain-public-record-1625-1649-domestic-series_1644-1645`, `_djvu.txt`, HTTP 200; the British History Online edition of this same volume is paywalled -- "gold page scans" -- so BHO could not be read directly, but the Internet Archive OCR text of the identical printed Calendar could): searched for "Worcester", "Maurice", "cipher"/"cypher"/"deciphered" together; the volume's cipher/deciphered hits are all letters taken from Digby's coach at Sherburn in Oct 1645 (Henrietta Maria-Digby, Jermyn-Wotton correspondence, submitted to Parliament 3 Nov 1645) or other captured Royalist correspondence, none involving Maurice, Rupert or Worcester, and no entry for 7 July 1645 concerning this letter (it was never intercepted; it survives in Rupert's own papers, not a Parliamentary seizure). found=false, own read.
3. **Community lists.** `sources/cryptiana/web/charlesi.htm` (grepped locally, not edited): section "Nicholas-Rupert Cipher after Naseby (July 1645)" gives a different key (higher numbers 98-373 / 427-616, alphabetical word series) which does not fit our max-398 letter-and-word mix, confirming the existing NOTES line "which this does not appear to match"; no other Cryptiana page names this specific letter. found=false.
4. **DECODE (de-crypt.org).** Reachable from this container today (HTTP 200; unreachable 23 Sept). No DECODE record exists for the shelfmark itself, so searched by context: the on-disk harvest (`sources/decode/records-{decrypted,non-decrypted}-2026-09-24.tsv`, comprehensive by status) has records only from BL Add MS 18982 (28 items, ff.44-195, dated "1645 -" through "1649-1950"), none from Add MS 18980 or 18981. Fetched all 27 RecordsView pages for the 18982 items (1.6s apart) and read each one's Origin/Author/City fields: none has Author "Maurice" or City "Worcester" (candidates seen: George [Digby], Nicholas, Lr. Gerrard, L. Digby, P.R./Charles R. as author, cities Oxford/Hereford/London/Cardiff/Dover/Jersey/Bristoll). No DECODE record for this letter. found=false, own search (not a citation of a prior pass).
5. **Bourdeau (github.com/dbourdeau/cyphersolver, shallow clone 25 Sept 2026, MIT code / CC BY 4.0 text).** `rupert/` folder (own re-clone, commit dated 25 Sept 2026 11:19 in this session's clone) still profiles this exact letter (target id `maurice1645`, 93 groups/63 distinct, max 398) as **offline-only**, unchanged from the 15/19 Sept finding already in this file: known Rupert-family keys (Charles I-Rupert-Digby-Ormonde 1644-45; Nicholas-Rupert July 1645) do not fit; the key would sit in BL Add MS 18980-18982 or 72438, both offline since the 2023 BL cyber-attack. `TARGETS.md` row 5 confirms the same status as of this clone. Note: a *different*, unrelated letter in the same project, `rupert1645/` (Charles I to Rupert, 29 Apr 1645, DECODE R4921), was separately read by Bourdeau on 21 Sept 2026 using Lasry's King-Queen key SP106-5 -- do not confuse the two folders; that key was tried on our target by Bourdeau's own project and rejected (see `rupert/NOTES.md`, "known keys tested"). found=false (this letter), true (sibling letter, different key, not ours).
6. **Aymeloglu (github.com/aaymeloglu/unsolved-ciphers, shallow clone 25 Sept 2026; no licence, cite only).** `grep -rli` for "rupert", "maurice" and "worcester" across the whole repository returns no hits. found=false (not attempted in this repository).

**New this pass, not previously in this file:** the BL Archives and Manuscripts catalogue's item-level list for Add MS 18982 (`searcharchives.bl.uk/catalog/040-002095608`, read directly, HTTP 200) itemises Maurice-to-Rupert letters at ff.27-28 (29 Jan 1645) and other January-February 1645 correspondence, but has no item entry at all for a 7 July 1645 letter -- so it is either uncatalogued at item level within 18982, or Warburton drew on a volume/leaf the modern catalogue does not itemise; either way it is not addressable from the catalogue alone. The same volume's item list also records ff.95r-96v, "Letter of Henry Osborne to Prince Rupert, 10 Nov 1645 ... Partially ciphered (with deciphering)" -- a sibling item in the very same volume carrying a contemporary decipherment, not yet checked against our key (a lead for whoever next has BL image access, not pursued here: image capture is out of this brief's scope and BL digitised content for this volume is itself marked "currently unavailable"). Add MS 18980 (1642-43) and 18981 (1643-44) are confirmed by their own catalogue records to predate this letter, so are not candidates for it.

## Verdict

**Open.** Verified unsolved by this worker's own sweep (Warburton read at the page, CSP Domestic checked by full-text search with a real control, DECODE searched exhaustively for the relevant volume, fresh Bourdeau/Aymeloglu clones). Unchanged from the 15/19 Sept 2026 finding: offline-only, blocked on BL images for Add MS 18980-18982/72438 (catalogue confirms "digital images currently unavailable"). New leads for a future worker: the ff.95-96 (R.) decipherment in the same 18982 volume, and Add MS 18982's item list as a place to watch if BL restores images.

## Background

- **Source:** Eliot Warburton, Memoirs of Prince Rupert and the Cavaliers, vol. iii p.133 (Google Books id Iz8JAAAAIAAJ; archive.org `memoirsprinceru01warbgoog`). Encoded letter sent soon after the Battle of Naseby.
- **Transcription:** `ciphertext.txt`. Highest number 398. Two-digit figures never appear in succession.
- **Background page:** `sources/cryptiana/web/charlesi.htm` (Rupert's ciphers with Charles I and Nicholas, which this does not appear to match).
- **Ideas:** The pattern "two-digit figures never consecutive" suggests two-digit groups are letters and three-digit groups are words or syllables, with the letters used only to spell what the nomenclator lacks. Context: Naseby aftermath, garrisons, Worcester. Warburton printed only a portion of vol. iii's Rupert correspondence in cipher form; pp.131-137 (this letter's neighbourhood) hold no other ciphertext.
- **Solver status (19 Sept 2026, reconfirmed 25 Sept 2026):** Offline-only per Bourdeau (cyphersolver/rupert): known Rupert keys do not fit; the key would be in BL Add MS 18980-82 or 72438, digitised but offline since the 2023 attack.

## Web and blog check (WEBCHECK-maurice-rupert-1645, 1 Oct 2026)

Required step of `.claude/briefs/check-solved.md` ("Open web and blog comment threads", CHECK-SOLVED-WEB, 28 Sept 2026), run by this worker on 1 Oct 2026, 23:35-23:41 UTC. Every query and every opened hit is listed; a comment thread was read in full wherever a post was opened. **Result: no decipherment or plaintext of this item located by these queries on 1 Oct 2026** (a search result, never a novelty verdict, CLAUDE.md rule 10). Status word on line 1 unchanged (`open`).

**(a) Plain web searches (WebSearch, 9 queries).**

| # | Query | Result for THIS letter |
|---|---|---|
| 1 | `"Prince Maurice" "Prince Rupert" cipher letter Worcester "7 July 1645"` | No page about the cipher. Hits: Huntington lib-77109 (1646 declaration), BL Sloane MS 1519 catalogue record (opened, below), bcw-project Maurice biography, Christie's lot 5210955 (Rupert ALS 17 May 1645, different letter), Eva Scott *Rupert Prince Palatine* (Gutenberg 39426, opened, below), Wikipedia Siege of Worcester/Bristol. |
| 2 | `"Add MS 18982" cipher Rupert` | Only the BL catalogue facet page for Charles I "Digitised Content: Yes (unavailable)"; the rest are modern "cipher" noise (Windows cipher command, TLS suites). No decipherment. |
| 3 | `"By your cipher, you may observe"` (the letter's own clear-text lead-in, quoted) | Zero hits on this phrase; results are unrelated (Flynn's 1927 cipher column, Gallup's Bacon biliteral, Wikipedia cipher articles). |
| 4 | `"Prince Rupert's Cipher with His Brother Maurice" 1645` (Tomokiyo's own heading for the item) | Zero hits on the heading itself; hits are Rupert/Maurice biographies, DNB Rupert, Naseby, tandfonline "Wilmot's blots" (June 1644 captured letters, different year and letters). |
| 5 | `Maurice Rupert 1645 cipher Naseby Warburton solved deciphered key` | Naseby battle pages; dbourdeau.github.io/cyphersolver index (opened, below); Folgerpedia "Decoding the Renaissance" (a Digby-to-Rupert-or-Maurice 1645 cipher letter in the Folger exhibition, a different letter, not ours); nothing reporting this letter read. |
| 6 | `site:scienceblogs.de klausis-krypto-kolumne Rupert Maurice 1645` | One plausible hit: Cipherbrain, "Eine ungelöste Verschlüsselung aus dem Jahr 1645" (20 Mar 2015) -- opened and read with all 17 comments, below. |
| 7 | `site:cryptiana.blogspot.com Rupert Maurice cipher` | Blog index pages only; no post naming this letter. Site's own search run directly, below. |
| 8 | `site:ciphermysteries.com Prince Rupert Maurice cipher 1645` | No Cipher Mysteries post about Rupert or Maurice; hits are La Buse and Somerton Man posts plus Wikipedia. Site's own search run directly, below. |
| 9 | `"Prince Maurice" Rupert 1645 cipher "solves" Claude OR GPT OR AI` (model-solve announcements) | Only the Cyphral Distich (Urquhart 1653) Claude story (vals.ai, Schneier, 36kr, dev.to) and Bourdeau's index (Charles I to Rupert 29 Apr 1645 read with Lasry's key -- the *other* Rupert letter, not ours). No model-solve claim for this letter. |

**(b) The three blogs, searched by name.**

- **Cipherbrain** (scienceblogs.de/klausis-krypto-kolumne). Site search `?s=Rupert`: "Wir konnten leider keine Beiträge finden" (no posts). `?s=Naseby`: no posts. `?s=Maurice`: 8 posts, all other Maurices (La Buse 2015, Chinese gold bar 2017, Playfair 2020, 1854 musical cryptogram, Moustier 2022, 1983 puzzle, Highland Park 2022, Goldene Alice 2022) -- none about Rupert, none opened. The one 1645 post, **"Eine ungelöste Verschlüsselung aus dem Jahr 1645"** (Klaus Schmeh, 20 Mar 2015, https://scienceblogs.de/klausis-krypto-kolumne/2015/03/20/eine-ungeloeste-verschluesselung-aus-dem-jahr-1645/), opened and its 17 comments read in full: the post is the UK National Archives "Can you crack the code?" image, which is **Prince Maurice to Lord Digby, Worcester, 31 August 1645** -- a different letter from ours. Comment #6 (Kent Ramliden, 24 Mar 2015) gives a full solution of that Digby letter and its key skeleton (1-69 letters, 70-78 nulls, 79-220 words alphabetical: 79 and, 80 are, 81 at, ... 172 horse, 189 force); comments #4/#8-11/#16 (Hans Jahr) give his independent solution and find the official decipherment already printed in CSP Domestic 1645-47 preface pp.xvi-xvii (keys by Col. J. S. Rothwell, RA); #17 links Ramliden's PDF write-up (opened, 3,174 chars, "Rupert" 0 hits). The word "Rupert" does not occur anywhere in the post or its thread; the 7 July letter, Warburton, and Add MS 18982 are not mentioned. Hans Jahr's linked write-up, katkryptolog.blogspot.com/2015/03/solution-of-enciphered-letter-from-1645.html, also opened: Digby letter only, "Rupert"/"7 July"/"18982" 0 hits, no comments. Useful side fact for this folder, not a decipherment: Maurice's cipher with Digby in Aug 1645 is a 1-69/70-78/79-220 design with two-digit letters, which cannot be our max-398 letter-and-word mix where two-digit groups are never consecutive (consistent with Tomokiyo's and Bourdeau's conclusion that no known Rupert-family key fits).
- **Cryptiana blog** (cryptiana.blogspot.com) and Tomokiyo's pages (cryptiana.web.fc2.com). On-disk snapshot `sources/cryptiana/` grepped first (zero requests): "By your cipher" occurs only in `web/unsolved.htm` (the item's own listing, "appears to be unsolved"); "Maurice" in charlesi.htm/digby.htm (the Digby 31 Aug 1645 cipher), "18982" in nicholas.htm and unsolved.htm (the Craven 1648 letter R8447, a different item). Live `cryptiana.web.fc2.com/code/unsolved.htm` fetched 1 Oct 2026: the "Prince Rupert's Cipher with His Brother Maurice (1645)" entry is byte-identical to the 24 Sept 2026 snapshot, still "appears to be unsolved", no "Solved" marker (the neighbouring Maurice-Digby entry carries one). Blog search `search?q=Rupert` returns three posts, `search?q=Maurice` one; the two that touch 1645 opened and read with their comment areas: "Cipher Letters to Charles I of England (1645) in the Parliamentary Archives" (25 Sept 2023, https://cryptiana.blogspot.com/2023/09/cipher-letters-to-charles-i-of-england.html; Charles I-Rupert 29 Apr and 31 July 1645 letters, Add MS 18983 and 18982 f.79 "THE=g4" key; "No comments"; "7 July"/"Worcester" 0 hits) and "A Bundle of Ciphers of Lord Digby" (13 Oct 2024, https://cryptiana.blogspot.com/2024/10/a-bundle-of-ciphers-of-lord-digby.html; says of Add MS 18982 "Most of the undeciphered ciphertexts can be read by using already deciphered letters or with known keys. I added one from Add MS 18982 in 'Unsolved Historical Ciphers'" -- that one is the Craven 1648 letter, not ours; "No comments"; "Maurice" 0 hits). The third ("Two Diplomatic Ciphers of Marquis de Villars", Sept 2026) matched only on a PS about Digby to Rupert 12 July 1644, not opened. Nothing on either blog names the 7 July 1645 letter.
- **Cipher Mysteries** (ciphermysteries.com). Direct `?s=Rupert` with curl answered HTTP 406 (Mod_Security "Not Acceptable"), one request, not retried with curl; the same search through the WebFetch fetcher returned four posts (Nigel West/Arnold Deutsch 2014 x2, Voynich pub meet 2014, Heltoft Voynich 2013), every "Rupert" being Rupert Allason; `?s=Naseby`: "Nothing Found". No Cipher Mysteries post concerns this letter; none opened further.

**(c) Other hits opened.**

- **Eva Scott, *Rupert Prince Palatine* (1899), Gutenberg 39426** (opened, full text grepped): cites "Warburton. III. p. 133. Maurice to Rupert, July 7, 1645" as footnote 1 of the chapter-end assessment ("his advice to make peace was reasonable enough") -- a citation of Warburton's commentary beside the letter, with no transcript, paraphrase or decipherment of the ciphered passage; her other Maurice-to-Rupert citations are 29 Jan 1645 (Warb. III p.54).
- **dbourdeau.github.io/cyphersolver/index.html** (opened 1 Oct 2026): "Maurice" occurs only in the Henri IV-Maurice of Hesse-Kassel entry; the Rupert row is unchanged from the 25 Sept clone (offline-only, no reading).
- **BL Sloane MS 1519** (searcharchives.bl.uk/catalog/040-002113870, catalogue record from query 1, opened): a Fairfax collection with "28. Letter from -- to Prince Rupert, [in cypher] an intercepted letter, f.63" (undated, sender unnamed) and "40. Craufurd-Lindesay ... requesting to have the key of the cypher used in the addresses between the King and the Prince Rupert". Not our letter (ours survives in Rupert's own papers, not a Parliamentary seizure, and is dated), logged as a lead for a future BL worker, not pursued.

**Requests per host:** scienceblogs.de 5 (post, three site searches, one PDF); cryptiana.blogspot.com 4; cryptiana.web.fc2.com 1; gutenberg.org 1; dbourdeau.github.io 1; katkryptolog.blogspot.com 1; searcharchives.bl.uk 1; ciphermysteries.com 1 curl (406) + 2 via WebFetch; WebSearch 9 queries. All at >=1.5 s spacing, browser UA; no 403/429/challenge other than the single Cipher Mysteries 406 noted above.

**Gate re-run** (`python3 tools/intake_gate_check.py maurice-rupert-1645`, 1 Oct 2026):

```
maurice-rupert-1645: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit=0
```

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/rupert/NOTES.md (#5)
- Their extent, in their words: offline-only: 93 groups from Warburton, known Rupert keys do not fit; key would be in BL Add MS 18980-82/72438
- Their date: 15 Sept 2026
- Note: already cited in our NOTES.md
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## Premise check (GF4-BATCH1, account-4, 3 Oct 2026)

**Result: not found solved.** No decipherment or applied key for this letter was found under (a)-(d). Status stays `open`.
This is the adversarial pass of `.claude/briefs/check-solved.md` "Premise check", run 3 Oct 2026 00:00-00:06 UTC
(`date -u`). No test or reading was run. One finding changes the blocker: Add MS 72438 is reachable through DECODE
(see (b)).

**(a) Decipherments the folder mentions. Not found / unreachable.**
- Warburton iii.131-137 (the source print): no gloss or footnote (check-solved pass above, re-confirmed by the phrase
  hits below). Every one of the 12 IA digitisations of Warburton prints the groups without a reading.
- Add MS 18982 ff.95r-96v, Osborne to Rupert, 10 Nov 1645, "Partially ciphered (with deciphering)" (REQUEST.md):
  **unreachable**. It is a BL image, and there is no DECODE record for 18982 ff.95-96 in the on-disk harvest. Not opened.
  [Corrected 3 Oct 2026, FT4c: the harvest does list it -- DECODE 8444 = 18982 f.95 and 8443 = ff.93-94, both
  Decrypted. Both are Osborne to Rupert, 9-10 Nov 1645, so neither is this letter. See the FT4c section below.]

**(b) Other solvers' working files. Not found, but one finding moves the blocker.**
- **Bourdeau**: fresh shallow clone, HEAD 2341682 (2 Oct 2026 15:12 -0500). `targets/rupert/` (NOTES.md,
  maurice1645.py, profile.json, find_letter.py, get_warburton.py, thumbsize.py) read: a structure profile only
  (93 groups, 63 distinct, max 398). The keys were tried "ranges only" (Charles I-Rupert-Digby-Ormonde 1644-45;
  Nicholas-Rupert July 1645), with no rendering. `targets/rupert1645/` (Charles I to Rupert, 29 Apr 1645, Lasry's
  King-Queen key SP106-5) is a different letter. Its NOTES do not record that key being applied to Maurice's groups.
- **Aymeloglu**: fresh shallow clone, HEAD d2800bb (27 Sept 2026). `royalist-1646/README.md` covers BL Add MS 72438
  ff.9-10. It names no Maurice-Rupert key, and its key 129 (names 559-580, one of them "Prince Maurice") sits far
  above this letter's max of 398. **But** the README says its 72438 images "were obtained through the DECODE"
  login, and our own DECODE harvest (`sources/decode/keys-all-2026-09-28-merged.tsv`) lists about 70 Key records for
  72438, ids 8627-8745. Among them is **8627 = f.25-26, the contemporary index "Cyphers taken in the Lord Digby's
  cabinet" (keys 80-139)**. So the Verdict's "72438 offline since 2023" is out of date for the keys: they sit behind
  the DECODE login, and A2-HDK (2 Oct 2026) got a full-size image from a record this way. **Next step: read
  DECODE record 8627 (the f.25 index) for a key naming Maurice, Rupert or Worcester. After that, if one exists,
  that key page. One browser login, about $1-2.**

**(c) Physical neighbours. Unreachable.** The 7 July letter is not itemised in the Add MS 18982 contents list (check-solved
pass). Its leaf and the leaves on either side cannot be reached until BL images return. Warburton pp.131-137, the
printed neighbourhood, hold no other ciphertext.

**(d) Recipient's side and other prints. Not found.**
- Rupert, the recipient, is the source of Warburton's print (the Rupert papers, now BL Add MS 18980-82). No other
  edition of his received letters was found.
- Interior-phrase searches. IA full text: "By your cipher, you may observe" gave 12 hits, all Warburton digitisations
  (including `memoirsofprincer0000elio`, `in.ernet.dli.2015.190974`, `india.history.resource.70653`,
  `baclac_896580987_003`), plus two copies of Jane Lane, *Sir Devil-May-Care* (London: Muller, 1971;
  `sirdevilmaycare0000lane`). "342, 148, 136" gave the same books plus number-table noise. "you may observe, that 15"
  gave the same. Google Books (country=US, keyed): "By your cipher, you may observe" gave 3 hits, all Warburton 1849;
  the clear words plus names gave 1, Warburton.
- **Lane 1971 is a novel.** Its Maurice composes the letter "in laborious cipher: 'God damn those Scots! The rebels
  rail on us for calling in the Irish to assist us, but sure ...'" (be-api snippets). That is an invented plaintext,
  not a decipherment. Logged here so that no later search mistakes it for a reading of the groups.

Requests this pass: archive.org be-api 11 (>=2 s apart) + 1 metadata, googleapis.com 2 (keyed, country=US), github.com 0
(clones shared with this batch). No logins, no DECODE call.

## First cheap test: DECODE 8627, the Digby-cabinet key index (FT4-maurice-rupert-1645, account-4, 3 Oct 2026)

Run 3 Oct 2026, 00:11-00:16 UTC (`date -u`). The test named by GF4-BATCH1: does the contemporary index of keys taken in
Lord Digby's cabinet (BL Add MS 72438 ff.25-26, DECODE record 8627) list a Maurice-Rupert key?
**Result: no. No key was applied, so there are no target or control numbers.** Status stays `open`.

- **Route.** One DECODE browser login (`tools/decode_browser_login.js 8627 . --guess-fullsize`). The first attempt
  failed with `ERR_CERT_AUTHORITY_INVALID` before the login form loaded, so no login was spent on it. This container's
  NSS database did not hold the proxy CA, which goes against the 20 Sept note that the setup script adds it. After
  the playbook's `certutil` fix, the second run logged in and **served all three full-size images** (6188-6333 x
  9345-9460 px, 12.8-14.1 MB each, real JPEGs). So 72438 full-size images are reachable for this record too, as
  A2-HDK found for record 4692. Files are in `decode/`: 2000 px copies, thumbnails, the scrubbed RecordsView page and
  `manifest.json`. The full-size originals were deleted to keep the folder under the 30 MB limit; their sha1s are in
  `fullsize_sha1.txt` and the re-fetch URL is in the manifest.
- **What the index says** (f.25r, transcribed in `decode/index_f25r.tsv`, one vision read at 2000 px). The heading is
  "Cyphers taken in the Ld Digbys". Keys are numbered 80-90, then 100-139, about 52 entries. Correspondents include
  the Countess of Cork, Lady Goring, Culpeper, Antrim, Killigrew, Vavasour, Ogle, Inchiquin, Secretary Nicholas,
  "His Maties Cypher with the Queene" (123), Lord Goring, Kenelm Digby, Newport and "many sheets De Vics hand" (138).
  **No entry names Maurice or Worcester.** The only Rupert entry is **118, "Ormond & Pr: Rupert"**. f.25v carries
  only the endorsement "List of L. Digbys Cyphers &c". f.26r is blank apart from a DURAND watermark. The index is
  complete at 80-139.
- **Why this is a real negative for the index, and why it does not close the key.** These are keys captured from
  Digby's papers (Sherburn, Oct 1645). A key held only by Maurice and Rupert would sit in Rupert's or Maurice's own
  papers (Add MS 18980-82, the source Warburton printed from), not in Digby's cabinet. So the index's silence fits
  the premise and rules out only the 72438 keys listed here. Key 118 is the one Rupert key in the set. Bourdeau
  tested a "Charles I-Rupert-Digby-Ormonde 1644-45" key against this letter by ranges and rejected it; whether that
  key is the same table as index 118 has not been checked.
- **Next step** (keep going; not blocked): find which 72438 Key record holds index no. 118 (the Ormond-Rupert
  cipher) and check its number range against this letter (max 398; two-digit groups never consecutive). Only if
  the ranges fit, apply it with a shuffled-key control (rule 3). Estimate: one DECODE login, reading thumbnails of
  records 8628-8745 for a "118" heading, at most ~15 requests, about $2. After that comes the Add MS 18982 ff.95-96
  Osborne decipherment (REQUEST.md), which needs BL images, not DECODE.

Requests: de-crypt.org 8 (1 failed TLS navigation before login, then login + RecordsView + 6 filesrv, 1.6 s apart),
one login. Vision calls: 2 (f.25r; f.25v+f.26r together).

## Key no. 118 tested: Digby key "Ormond & Pr: Rupert", BL Add MS 72438 ff.59-60 (FT4b-maurice-rupert-1645, account-4, 3 Oct 2026)

Run 3 Oct 2026, 00:28-00:35 UTC (`date -u`). FT4 named this step. **Result: key 118 does not read this letter. It was
applied, with a shuffled-key control and the judge, and failed both.** Status stays `open`.

- **Record found.** Nothing on disk said which DECODE record holds index no. 118, so it was placed from folio anchors.
  The index numbers run in folio order (f.52 = 113, f.70 = 125, from `ciphers/intercepted-royalist-1646/NOTES.md`).
  Keys 114-124 then fall on the 11 Key records for ff.53-69, which puts no. 118 on ff.59-60, **DECODE 8655**.
  Tomokiyo confirms it (`sources/cryptiana/web/charlesi.htm`, "Cipher with Prince Rupert, Digby, and Ormonde
  (1644-1645)": "A copy is preserved in Add MS 72438, f.59-60"). The leaf itself confirms it too: f.59r is endorsed
  "Cypher for Ormond & Prince Rupert 118". No `decode_list.py` crawl was needed, because
  `sources/decode/keys-all-2026-09-28-merged.tsv` already lists every 72438 Key record.
- **Fetch.** One browser login: `tools/decode_browser_login.js 8655 --guess-fullsize`, with the NSS proxy-CA fix
  applied first because it was missing again in this container. All 4 full-size pages were served (13-16 MB each). The
  2000 px copies, thumbnails, scrubbed RecordsView and manifest are in `key118/`. The originals were deleted (sha1s in
  `key118/fullsize_sha1.txt`).
- **Range check: the ranges overlap and the design matches.** The key has letters 1-80 as homophones (a 14-17, b 21-23,
  c 11-13, d 5-7, e 1-4, ... z 51-52), nulls 81-90, and words 91-434 in alphabetical order, nearly all proper names
  (354 = Rupert Prince, as Tomokiyo has it). Common words are letter+digit codes (a1 and ... p6 wch). The target's
  values (6-398; letters at or below 80, nulls 82/84, words 100-398) all fall inside that range, so this is not a
  range mismatch. One caveat: the target has **no** letter+digit codes. The "two-digit groups never consecutive"
  remark is also not quite true of the transcription ("15 26", "6 15", "12 15").
- **Applied.** `key118.tsv` holds all letters and nulls plus the 42 word rows the target uses, from one reader pass over
  the rotated crops; every row is graded M. `ct118.tsv` holds the target. `decode.json` drives
  `tools/decode_key.py`, whose output is in `reading_key118.txt` (M 90, U 3). The decode begins "a m [342] Designe
  Clanrickard_Ea c Peace Edenburgh [null] Harbour m Queene q Question Give h Poland Row_Sr_Tho Dartmouth ...". It is
  isolated letters and a run of place and person names, with no function words. 3 of the 93 tokens (239, 252, 342)
  fall on code numbers that are **blank** on the key sheet.
- **Test vs control** (rule 3; `key118_test.py`, output in `key118_test.tsv`, `--check` passes). The test scores the
  cipher-only decode with the en16_repo 4-gram model, because no en17 corpus is wired and en16_repo holds 1650s
  printed Thurloe readings, the nearest era on disk. The control is 200 keys whose values are shuffled among the
  key's own rows, so it varies on the same axis as the statistic.

  | stat | key 118 | shuffled-key mean | shuffled p95 | rank of 201 |
  |---|---|---|---|---|
  | 4-gram/letter | -1.783 | -1.796 | -1.698 | 80 |
  | word cover | 0.319 | 0.313 | 0.372 | 88 |

  Judge (`judge_key118.json`, en16_repo): **FAIL**, score -1.783 vs real_p05 -0.568, null_p99 -1.831, N=504.
  The decode is indistinguishable from random keys and scores near shuffled letters.
- **Grades:** M 90, U 3; no H, no C. The key is not shown to be this letter's, which is what the test found.
- **Verdict on the step.** Key 118 (Charles I / Rupert / Digby / Ormonde, 1644-45) is excluded for this letter: the
  ranges overlap, but the key was applied with a control and failed. This agrees with Bourdeau's range-only rejection
  of the "Charles I-Rupert-Digby-Ormonde 1644-45" key, which is this same table. The letter's own key (Maurice and
  Rupert) would sit in Rupert's papers (BL Add MS 18980-82), not in Digby's cabinet.
- **Next key / next step** (keep going): the Add MS 18982 ff.95r-96v Osborne-to-Rupert decipherment (REQUEST.md). It
  needs BL images; check DECODE for an 18982 f.95 record first (none in the 24 Sept harvest), at about $1. There is
  one cheap internal check: `design_prior.py`/KEY-DESIGN.tsv for any other Rupert-circle key with letters at or below
  80, nulls in 81-90 and no letter+digit codes, about $0.5.

Requests: de-crypt.org 9 (login + RecordsView + 8 filesrv, 1.6 s apart), one login. Vision reads: 12 (4 page overviews,
1 mis-rotated crop, 1 rotated overview, 6 table crops; one reader pass by this worker, no subagents -- over the
brief's 3, because the table spans two rotated pages). Rule 10: nothing here says new or unread.

## design_prior and Add MS 18982 ff.95-96 (FT4c-maurice-rupert-1645, account-4, 3 Oct 2026)

Run 3 Oct 2026, 00:47-01:00 UTC (`date -u`). No cryptanalysis was done. Status stays `open`.

**design_prior** (`python3 tools/design_prior.py ciphers/maurice-rupert-1645/ciphertext.txt --no-write`):

```
ciphers/maurice-rupert-1645/ciphertext.txt: 99 tokens, 69 distinct, inventory digits
  relabel-invariant statistics: True; references at this N: 120
  multi-sign (homophonic/nomenclator/syllabary) d=0.10 envelope=0.31 null_p05=0.12 -> plausible
  mixed (partial table)  d=0.81 envelope=2.32 null_p05=0.52 -> not above null
  letter-for-letter      d=0.90 envelope=1.5 null_p05=0.66 -> not above null
  code                   d=1.59 envelope=1.1 null_p05=1.17 -> excluded
  shuffled-input false-positive rate: 0.135
  fine family ranking (advisory, not calibrated): homophonic=0.17; nomenclator=0.26; syllabary=0.64; mixed=0.81; alphabet substitution=0.90; code numbers=1.59
  nearest keys: vanbeuningen-dewitt-1657/key.tsv [nomenclator; d=0.05] || jan-van-nassau-1572-75/key_5549.tsv [homophonic; d=0.06] || lodewijk-van-nassau-1573-74/key_5801.tsv [homophonic; d=0.17]
```

What it says: the multi-sign class (a homophonic or nomenclator table) is plausible. A pure code is excluded. This fits
the letters-plus-words reading already in this file and the key 118 design. The nearest keys are Dutch and Nassau
tables, which have nothing to do with this letter. They match on statistics only. At N=99 the shuffled-input
false-positive rate is 13.5%, so this is a weak prior. It licenses no key.

**Add MS 18982 ff.95-96: what it is.**
- BL catalogue JSON (`searcharchives.bl.uk/catalog/040-002095608?format=json`, HTTP 200, read 3 Oct 2026):
  "ff. 95r-96v: Letter of Henry Osborne to Prince Rupert, 10 Nov 1645. Original: holograph. With address. Partially
  ciphered (with deciphering)." The leaves before it are "ff. 93r-94v: Letter of Henry Osborne to Prince Rupert,
  9 Nov 1645 ... Partially ciphered (with deciphering)". The same catalogue still has **no item for a 7 July 1645
  Maurice letter**. Its only Maurice-to-Rupert item is ff.27-28 (Worcester, 29 Jan 1645). Its July 1645 items are
  Nicholas (ff.68-69, 71), Goring, Watson, Digby and Glemham.
- DECODE: `sources/decode/records-decrypted-2026-09-24.tsv` has **8444** ("Add MS 18982 f 95", 1645, Decrypted,
  2 images) and **8443** ("f 93-94", Decrypted, 3 images). The premise-check line above wrongly said there was no such
  record. RecordsView/8444 was fetched without a login (HTTP 200) and gives: Receiver "Hen?Osborne", date 1645-11-10,
  access mode "Authentication required", "The image is not in the public domain."
- **Answer: no.** ff.95-96 is not a period decipherment of this letter. It is a different letter: Osborne, not
  Maurice, 10 Nov, not 7 July. The premise risk (N0) is cleared for this item. No image was fetched and no vision call
  was made, because the catalogue and DECODE metadata already settle the question.
- What it could still give: a deciphered Osborne-Rupert table from Nov 1645 (8443 and 8444 together, 5 images). It is
  a possible key, not this letter's key. Osborne is a different correspondent, so the prior that it fits is low.

**Next step** (keep going): one DECODE browser login fetches 8443 and 8444 (5 images, about 8 requests). Read off
the number range and design of the Osborne table (letters vs words, max code). Apply it with the shuffled-key control
(as `key118_test.py` did) only if it fits this letter's profile (letters at or below about 80, words up to 398, no
letter+digit codes). About $1.5-2. If it does not fit, the remaining unread piece is blocked from outside the session:
Rupert's own papers (Add MS 18980-82) on BL images, where the 7 July leaf is not itemised.

Requests: de-crypt.org 1 (RecordsView/8444, no login); searcharchives.bl.uk 1. Vision calls 0. Rule 10: nothing here
says new or unread.

## Osborne-Rupert siblings, DECODE 8443 and 8444 (FT4d-maurice-rupert-1645, account-4, 3 Oct 2026)

Run 3 Oct 2026, 01:06-01:15 UTC (`date -u`). FT4c named this step. **Result: the Osborne key does not read this letter.
Its pairs are genuine (they beat their own shuffle control), but they cover only 17 of the target's 93 tokens, and
those 17 score worse than shuffled keys.** Status stays `open`.

- **Fetch.** One DECODE browser login (`tools/decode_browser_login.js 8443 --guess-fullsize --fetch-page
  RecordsView/8444`), after the NSS proxy-CA fix (missing again in this container). All 6 full-size images were served
  (4 for 8443, 2 for 8444; 13-14 MB each). Neither record has a document or transcription attached ("Documents 0").
  The metadata reads 8443 Author "P. R. (Prince Rupert?)", Receiver "Osborne"; 8444 Receiver "Hen?Osborne". The DECODE
  author/receiver fields look reversed against the BL catalogue (Osborne to Rupert); the leaves end "Your Highness's
  most faithful ... servant, Hen. Osborne", place and date line not transcribed. Committed: thumbnails, two 2400 px crops of
  8443 P4 and `osborne/fullsize_sha1.txt`. The full-size originals and the two RecordsView pages were not committed (the
  pages carry the account name).
- **What they hold.** Letters in clear with numbered cipher passages, each with a **period interlinear decipherment**
  above the numbers. 8443 P4 (the second leaf's recto) carries most of it (about 20 cipher lines); 8443 P1 and 8444 P2
  carry a few more lines. Only 8443 P4 was read (vision cap 3: one overview, two crops). 8443 P1/P2 and 8444 P2 cipher
  lines are unread.
- **Pairs** (`osborne/pairs_8443p4.tsv`, 141 occurrences, one eye read). Design: letters 2-66 (homophones, e.g. e = 40?,
  45, 46, 52; s = 21, 22; o = 49, 50, 55, 66), nulls about 283-291, words about 75-226 in near-alphabetical order (all 75,
  be 80, but 81, best 84, done 95, expect 103, is 120, it 130, in 131, may 139, me 143, not 153, of 159, or 164,
  quarell 177, rather 181, that 193, this 194, they 201, unto 203, under 204), then King 226. Per-leaf control
  (rule 3; `osborne/osborne_test.py`): repeated codes agree with their modal gloss 0.958 of the time against a shuffle
  mean of 0.376 (p95 0.403, rank 1 of 1001). The pairs pass. The key is `osborne/osborne_key.tsv`: 60 codes, 5 with
  conflicting glosses (4 d/g, 10 y/t, 40 e/c, 107 part/from, 193 that/the), graded M; the rest S.
- **Range overlap with the target.** Partial. Both are letters-plus-words nomenclators with low two-digit letters. The
  target's words run to 398, and its most frequent codes (148, 212, 229, 293, 323, 351, 355) are not in the Osborne
  pairs; 293 would be a null in the Osborne table. Only 13 of the target's 63 distinct codes are keyed.
- **Target test vs control** (`osborne/osborne_test.tsv`; en16_repo 4-gram, the judge block of `judge_key118.json`;
  200 keys with values shuffled among the key's rows, seed 1):

  | stat | Osborne key | shuffled-key mean | p95 | rank of 201 |
  |---|---|---|---|---|
  | 4-gram/letter | -2.012 | -1.778 | -1.442 | 175 |
  | word cover | 0.606 | 0.583 | 0.788 | 87 |

  Judge: **FAIL**, -2.012 vs real_p05 -0.638, null_p99 -1.631, N=33. The decode (`osborne/osborne_reading.txt`) begins
  "[15] [26] [342] [148] [136] w [325] [162] best ...": isolated letters and stray words. N=33 is short, so this is a weak
  negative. But the decode is no better than random keys, and 80% of the target's tokens fall on codes the sibling
  table, as read, does not cover.
- **Grades:** none claimed for the target. The sibling values are S at best (rule 4), and none read the target.
- **Rule 7:** `python3 osborne/osborne_test.py --check` passes ("osborne outputs up to date"); `tools/decode_key.py
  . --check` on the key-118 reading still passes.
- **Next step** (keep going, about $1.5): read the unread Osborne cipher lines (8443 P1/P2, 8444 P2) from the full-size
  images (re-fetch, one login; sha1s in `osborne/fullsize_sha1.txt`). That adds pairs, mostly in the 100-226 word band.
  This is only worth doing if a fuller Osborne table might reach the target's 290-398 band. The 280s-290s are nulls
  here, so the prior is low. Otherwise the remaining unread piece is blocked from outside the session: Rupert's own
  papers (Add MS 18980-82) on BL images, where the 7 July leaf is not itemised.

Requests: de-crypt.org about 15 (login, RecordsView/8443, RecordsView/8444, 6 thumbnails, 6 full-size; 1.6 s apart), one
login. Vision calls: 3 (overview sheet, two 8443 P4 crops). Rule 10: nothing here says new or unread.
