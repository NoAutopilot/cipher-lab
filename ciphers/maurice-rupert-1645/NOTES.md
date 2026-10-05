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

**3 Oct 2026 (GAPS52):** still open, parked again. DECODE 9119 (Add MS 32256 ff.8-9) and 9117 (f.6) were fetched at full size. Both are printed number forms filled in by a later hand (9119 is dated 1820, built from the Charles I-Nicholas letters of 1644-45), not period key sheets. Both FAIL the judge. For 9119, coverage is 35/93, at the banded-control median, and the language test has 0/50 power at that coverage, so it is a non-test, not a negative. 9117 is at chance. 0 tokens read. gaps_check: parked.

**3 Oct 2026 (GAPS51):** still open, no longer parked. The key registers hold no English 1640s key. Key no. 129 on disk is a non-test (5/93 tokens). The DECODE listing gives an untried, reachable key: 9119, BL Add MS 32256 ff.8-9, Charles I/Nicholas to Rupert, 1644, whose design fits. Next: one login to fetch and test it.

**3 Oct 2026 (GAPS47):** still open, parked. BL Add MS 30305 has no Maurice letter and no 7 July 1645 item, but its f.86 "Keys to cyphers" (Charles I; Nicholas 1646-58) are undigitised; added to REQUEST.md. The Bodleian MSS Firth c. 6-8 record (Warburton's transcripts) is Anubis-blocked from the cloud: LOCAL-QUEUE L43. gaps_check: parked.

**3 Oct 2026 (FT4f):** still open. The BL item lists of Add MS 18980-82, the current DECODE listing and all three Warburton volumes hold no key and no decipherment of this letter; the 7 July leaf is still not itemised. Next: Add MS 30305 and Bodleian Firth C6-C8 records (see the FT4f section).

**3 Oct 2026 (FT4e):** still open. The Osborne key family is now read in full from the DECODE images (8443 P1 has no
cipher; 8443 P2, P4 and 8444 P2 read) and still does not read this letter: 19/93 tokens keyed, 4-gram rank 148/201 vs
shuffled keys, judge FAIL. The remaining unread piece is blocked from outside the session (BL Add MS 18980-82 images,
ASKS row 56). See "## Remaining gaps" at the end of this file.

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

## Osborne lines completed: 8443 P1/P2 and 8444 P2 (FT4e-maurice-rupert-1645, account-4, 3 Oct 2026)

Run 3 Oct 2026, 04:44-05:0x UTC (`date -u`). FT4d named this step. **Result: the extra pages add 40 genuine pairs and 7
codes, but the extended key still does not read the target. Both numbers are below FT4d's own controls.**

- **Fetch.** One DECODE browser login (`tools/decode_browser_login.js 8443 ... --fetch` with the three full-size
  file URLs). Full-size images were served, and the sha1s match `osborne/fullsize_sha1.txt` (P1 2cc22f58, P2 72d6ce17,
  8444 P2 51af71f5). Not committed (13 MB each). Locator: one contact sheet of the three committed 200 px thumbnails.
- **Crops** (pasted commands):
  `python3 tools/iiif_lines.py --image IMG_R8444_I38995_P2.jpg --region 3100,1300,3896,3900 --out c8444p2 --prefix r8444p2 --debug`
  (14 lines) and `python3 tools/iiif_lines.py --image IMG_R8443_I38994_P2.jpg --region 1300,900,3900,1900 --out
  c8443p2 --prefix r8443p2 --debug` (7 lines). Each page's line crops were joined into one sheet and read in one vision
  call. 8443 P1 got a contrast-equalised view of the text block (the third call). It is a letter wholly in clear ("May it
  please your Highnesse / I had not kept Mr Craven thus long here ..."), with **no cipher numerals**, so it gives 0 pairs.
- **Pairs.** 8444 P2: four cipher stretches with period interlinear glosses. They read "will be [283] reproued / for not
  reading it in the house", "to be disputed [284] into better conditions" (`osborne/pairs_8444p2.tsv`, 27 pairs).
  8443 P2: "are many [of both houses] inclined [to your Highnesse]" (`osborne/pairs_8443p2.tsv`, 13 pairs). The eye
  alignment was checked with `tools/interlinear_align.py align` (`osborne/align_pairs_new.tsv` -> `align_new.tsv`,
  `--floor 75 --prior` P4 key `--word-prior`). It agrees token for token. A flat-start run without the prior misplaces
  "be" and the nulls 283/284, so the prior is what makes this alignment work. New codes: 29 m, 37 b, 69 e (twice; the 8444 gloss
  looks like "a" by eye, while 8443 P2 glosses it e and the sense wants "better"), 79 are, 109 for, 133 into, 156 not.
  The new glosses also settle two P4 conflicts the other way: 10 = y, 40 = c.
- **Per-page gate before merging** (rule 3 per unit; `osborne/osborne_test2.py`). Each page's glosses must agree with
  the P4 key on shared codes more often than the same page's glosses shuffled among its own occurrences (1000 shuffles):

  | page | agree with P4 key | shuffle mean | p95 | verdict |
  |---|---|---|---|---|
  | 8443 P2 | 0.900 (10 shared occ of 13) | 0.132 | 0.300 | clears, rank 1/1001 |
  | 8444 P2 | 1.000 (22 shared occ of 27) | 0.106 | 0.227 | clears, rank 1/1001 |

  Within-page repeat consistency: 8444 P2 1.000 vs shuffle p95 0.600 (10 repeated occurrences); 8443 P2 1.000 vs p95
  0.500 (only 2 repeated occurrences, rank 35, weak by itself). Both pages are merged: 68 codes, 181 occurrences
  (`osborne/osborne_key2.tsv`).
- **Target test, same statistics as FT4d** (`osborne/osborne_test2.tsv`; en16_repo 4-gram, judge block of
  `judge_key118.json`, 200 shuffled-value keys, seed 1):

  | stat | FT4d (P4 key, 60 codes) | FT4e (extended, 68 codes) | FT4e shuffled mean | FT4e p95 | FT4e rank |
  |---|---|---|---|---|---|
  | tokens keyed | 17/93 (13/63 codes) | 19/93 (15/63 codes) | - | - | - |
  | 4-gram/letter | -2.012 (rank 175/201) | -1.844 | -1.733 | -1.469 | 148/201 |
  | word cover | 0.606 (rank 87/201) | 0.541 | 0.615 | 0.789 | 150/201 |
  | judge | FAIL -2.012 (real_p05 -0.638, N=33) | FAIL -1.844 (real_p05 -0.617, null_p99 -1.621, N=37) | | | |

  Only 2 more target tokens are keyed (156 "not", which the target uses once, and one more letter). The target's
  frequent codes (148, 212, 229, 293, 323, 351, 355) and its whole 290-398 band are still outside every Osborne pair.
  All Osborne cipher lines on the six DECODE images are now read. The table as written in these letters does not use
  codes above 291 (283-291 are nulls), so no further Osborne material on these records can reach the target's band.
- **Rule 3 third-attempt clause.** This was a second attempt with the same instrument and more key material, and every
  number stayed below its control. So the Osborne key family is logged **untested-by-this-instrument** (sibling-key
  transfer at 20% coverage), not refuted. The pairs are genuine, but the table, as far as it survives here, does not
  overlap the target's code band. Only a different instrument or new material reopens it: Osborne's full key sheet,
  or the 7 July leaf itself.
- **Grades:** none claimed for the target (rule 4). The sibling values are S at best. Rule 7: `python3
  osborne/osborne_test2.py --check` exits 0 ("osborne2 outputs up to date"). `osborne_test.py --check` and
  `tools/decode_key.py . --check` still pass.

Requests: de-crypt.org 6 (login page, login post, RecordsView/8443, thumbnail, 3 full-size), one login, 1.5 s apart. Vision
calls: 3 on crops/page views (8444 P2 sheet, 8443 P2 sheet, 8443 P1 view), plus 1 locator on the three 200 px
thumbnails. Rule 10: nothing here says new or unread.

## BL Add MS 18980-82 route (FT4f-maurice-rupert-1645, account-4, 3 Oct 2026)

Run 3 Oct 2026, 05:20-05:30 UTC (`date -u`). FT4e named this route. **Result: no key and no decipherment of this letter
was found in any of the three sources. The 7 July 1645 leaf is still not itemised in the BL catalogue. Status stays
`open`. Nothing was tested, because no candidate key turned up.**

1. **BL catalogue records** (`searcharchives.bl.uk/catalog/<id>?format=json`, HTTP 200 each, read in full from the
   Scope & Content item lists). Every volume reads "Digitised Content: ... *(digital images currently unavailable)*".
   All three are ark-linked viewer records whose images are offline. Physical access needs a letter of introduction
   (18980, 18981) or is "restricted" (18982).
   - **Add MS 18980** (`040-002095606`, 1642-1643, 148 item paragraphs). There are 10 Nicholas-to-Rupert letters
     "partly in cipher, deciphered" (ff.33, 38, 40, 42, 46, 50, 138, 146, 148, 150; Apr and Nov 1643). The volume holds
     no Maurice-to-Rupert letter. Maurice appears only in the Barnstaple articles (ff.110-111, 27 Aug 1643) and in the
     doctors' letter on his illness (ff.125-126). It ends in 1643, so it cannot hold the target.
   - **Add MS 18981** (`040-002095607`, 1643-1644, 238 paragraphs). There are 14 partly ciphered items: Digby, Elliott,
     Richmond, Jermyn, Ashburnham, Nicholas and Gage, Apr-Nov 1644, most deciphered. Two are undeciphered (Nicholas
     22 Oct 1644 ff.301-302; Digby 27 Oct 1644 ff.312-313). One more is "almost wholly in cipher to Prince Rupert, n.d."
     (f.172). The volume holds no Maurice-to-Rupert cipher letter. Maurice appears only as the addressee of Grenville,
     23 Dec 1644 (ff.340-341). It ends in 1644.
   - **Add MS 18982** (`040-002095608`, 1645-1658, 147 paragraphs). The only Maurice-to-Rupert item is ff.27-28,
     Worcester, 29 Jan 1645 (no cipher noted). The June-August 1645 run is ff.64-65 (Nicholas, 10 and 23 Jun,
     deciphered), ff.66-67 (Goring to Legge, 30 Jun), ff.68-69 (Nicholas, 11 Jul, copy undeciphered and original
     deciphered: the Cryptiana Nicholas-Rupert key, already excluded), ff.70-73 (12 and 22 Jul), ff.74-78 (28 Jul) and
     ff.79-80 (Richmond, 3 Aug, "some use of cipher": the THE=g4 key, Cryptiana). **There is no 7 July 1645 entry,
     confirming the LANE CX2 finding.** Cipher items later in the volume (ff.93-96 Osborne, read FT4c-FT4e; 1648-49
     items) are all later than the target.
   - **New lead, not pursued (outside this brief).** The record's own "Related Material" field names **Oxford,
     Bodleian Library, MSS Firth C6-C8: "transcripts of letters to Prince Rupert, including both material here and
     other letters"**. The 18980 scope note also says that "a number of Civil War letters to Rupert" sit in **Add MS
     30305**, which also came through Bentley. Either could hold the 7 July letter that the 18982 list lacks: Warburton
     printed it from Bentley's Rupert papers, and his own vol. i calendar lists it (item 3 below).
2. **DECODE, login-free listing** (`tools/decode_list.py`, page 1 of each status, 7 requests). Live totals on 3 Oct
   2026: Cipher, Decrypted 1360, Non-decrypted 801, Partially decrypted 385. Key: 6374 in all. These equal the on-disk
   harvests exactly (`records-*-2026-09-24.tsv`: 1360 + 1186; `keys-all-2026-09-28-merged.tsv` +
   `keys-na-p58-2026-10-02.tsv`: 6374 ids), and no page-1 id is missing from them. So the harvests are current.
   In them: **0 records of any type for Add MS 18980 or 18981**, though the BL lists about 24 partly ciphered letters
   there. Add MS 18982 has 28 Cipher records (ff.44-195) and **0 Key records**; LANE CX2 read every 18982 record and
   none is by Maurice or from Worcester. Add MS 72438 has 71 Key records (8627 index and no. 118 tested, FT4/FT4b).
   "Rupert" and "Maurice" match no key row. **No DECODE key for Maurice or Rupert, 1644-46, beyond what was already
   tested.**
3. **Warburton, *Memoirs of Prince Rupert and the Cavaliers* (1849), IA full text, all three volumes**
   (`memoirsofprincer01warbuoft` and `02warbuoft`; vol. iii `memoirsprinceru01warbgoog`, because `03warbuoft`'s
   djvu.txt answered HTTP 500; vol. iii cross-checked in `02warbgoog` and `07warbgoog`). Each volume was grepped for
   cipher, cypher, decipher, key and Maurice, and every hit was read in context.
   - The letter (iii.133) is printed with its clear text and the 93 groups, with no reading. Three independent OCR
     copies agree with `ciphertext.txt` group for group, OCR noise aside.
   - Warburton's vol. i "Index and Abstract" (calendar) has, under 1645: "MAURICE, Prince, Worcester, to Prince
     Rupert, July 7 -- has appointed four regiments, and Maxwell's troop of horse to attend Prince Rupert at Bristol;
     would have come himself, but this place threatened by the Scots." Every fact in this abstract comes from the clear
     part of the letter. It glosses nothing in the cipher, so **it gives no crib**. It does confirm that the original
     was among the Rupert papers Warburton used.
   - The other cipher passages in the three volumes involve Nicholas, Digby, Richmond, Jermyn, Ashburnham, Charles I
     (who sends Rupert "a cypher of my own making", Boconnoc 30 Aug 1644, iii.23) and the Prince of Wales, printed
     "[In cipher]" or as raw numbers. **No Maurice-Rupert key and no decipherment of this letter is printed anywhere in
     the three volumes.**
- **Grades:** none (rule 4). No reading was attempted. No known-key test was planned, because no candidate key was
  found. Rule 10: this is a search result, never a novelty verdict.

Requests: searcharchives.bl.uk 5 (3 records, 2 searches), de-crypt.org 10 (3 ignored-psearch grid pages, 7
decode_list page-1 fetches; no login), archive.org 7 (1 advancedsearch, 6 djvu.txt, one of which was HTTP 500), all
>=2 s apart. Vision calls: 0.

## GAPS47-maurice-rupert-1645 (3 Oct 2026, account-4)

Run 3 Oct 2026, 07:13-07:20 UTC (`date -u`). This worker was spawned on the stale NEXT-STEPS.tsv row ("read the unread
Osborne cipher lines 8443 P1/P2, 8444 P2"), but FT4e had already done that step (commit af264881, section above). So it
ran the current Verdict step instead: the two secondary-witness catalogues that FT4f named. **Result: no 7 July 1645
Maurice item, no decipherment and no Maurice-Rupert key found in either catalogue as far as the cloud reaches.
Add MS 30305 does list two sets of "keys to cyphers" (f.86), and those are not reachable. Nothing was tested.**

1. **BL Add MS 30305** (`searcharchives.bl.uk/catalog/040-002021962?format=json`, HTTP 200, the Scope & Content item list
   read in full). Vol. I of Add MS 30305-30306, the Fairfax of Denton correspondence, ff.221. It holds Rupert letters
   1644-1649: Digby to Rupert ff.63, 80 (1644, 1645); Nicholas to Rupert f.79 (1645); Richmond to Rupert f.80 (n.d.,
   "Partly cipher"); Jermyn to Rupert f.88 (1644); Long to Rupert f.146 (1649); and **f.86, "Charles I of England: Keys
   to cyphers" and "Sir Edward Nicholas ...: Keys to cyphers used by him: 1646-1658"**. **There is no Maurice letter in
   the volume, and no 7 July 1645 item.** The record carries no "Digitised Content" line (the 18980-82 records do), so
   f.86 has no online image. The keys are undated for Charles I and dated 1646-58 for Nicholas. Nicholas's 1645 key is
   already excluded (the Cryptiana Nicholas-Rupert key, FT4f item 1). Whether a Charles I key on f.86 reaches the
   letter's code range (up to about 398) is unknown without the leaf. On-disk DECODE harvest (`sources/decode/*.tsv`)
   grepped for "30305": 0 records.
2. **Bodleian MSS Firth c. 6-8.** What these are, from Google Books snippets (keyed API with `country=US`, 1 call):
   "Prince Rupert papers, 3 vols. (MSS. Firth c. 6-8)" (Bodleian Curators' Annual Report 1902 and 1921), "The
   transcripts of Rupert's correspondence made for Warburton" (*Journal of Sir Samuel Luke*, 1950), "Many printed in
   Warburton's Memoirs of Prince Rupert" (*Student's Guide to the Manuscripts Relating to English History in the
   Seventeenth Century in the Bodleian*, 1922). They are therefore most likely the very copy Warburton printed the 7 July
   cipher from. A transcript could carry the transcriber's decipherment, but nothing found says it does. The holding
   record could not be read: archives.bodleian.ox.ac.uk answered one curl and one headless-browser fetch with the Anubis
   page "Making sure you're not a bot!" (the documented 26 Sept 2026 block), and was not retried. EMLO Solr: 0 docs for
   "Firth" AND "Rupert" and 0 for Rupert AND Maurice AND 1645 (EMLO does not catalogue these volumes). **Filed as
   LOCAL-QUEUE.tsv row L43** for the owner's desk runner: the record, its availability flag, and the 7 July 1645 folio.
- **Grades:** none (rule 4). No reading was attempted. Rule 10: search results only, never a novelty verdict.

Requests: searcharchives.bl.uk 4 (2 search attempts redirected or answered HTML, 1 search JSON, 1 record);
archives.bodleian.ox.ac.uk 2 (1 curl, 1 browser, both Anubis); emlo.bodleian.ox.ac.uk 3; archive.org 1 advancedsearch
(noise); www.googleapis.com 1. All at least 2 s apart. Vision calls: 0. de-crypt.org: 0, no login, because the step
needed none.

## GAPS51-maurice-rupert-1645 (3 Oct 2026, account-4)

Run 3 Oct 2026, 07:31-07:36 UTC (commit c7380f4f). That commit cut this section short and deleted the "## Remaining
gaps", "## Escalation" and "## While waiting" sections below it. GAPS52 restored them from 57895624 and rewrote them
below. GAPS51's findings, from its ROOM.md done line:
- KEY-OFFICES.tsv and KEY-DESIGN.tsv hold no English key of the 1640s.
- The on-disk Digby key no. 129 covers 5 of 93 tokens, a non-test.
- Tomokiyo's after-Naseby letter table covers 14 isolated letters, also a non-test.
- The DECODE listing, read with no login, has 9119 = BL Add MS 32256 ff.8-9, "Charles I/Nicholas to Pr. Rupert", 1644.
  Tomokiyo (Cryptiana) identifies it as the ministers' cipher, with words at 84-521. It also has 9117, Add MS 32256
  f.6, a King-Queen-family key form.
- Vision calls: 1. Requests: de-crypt.org 10, cryptiana fc2 1.

## GAPS52-maurice-rupert-1645 (3 Oct 2026, account-4)

Run 3 Oct 2026, 07:48-08:0x UTC (`date -u`). The step was to fetch DECODE 9119 and 9117 and test them on the letter.
Credit: Tomokiyo (Cryptiana) identified 9119 as the Charles I/Nicholas-to-Rupert cipher (rule 8).
**Result: neither form reads the letter. Both FAIL the judge.**
- 9119 does no better than chance on coverage once the form's own layout is controlled for.
- The power control shows that the 4-gram test cannot detect a true key at 35/93 coverage. The 9119 language miss is
  therefore a **non-test, not a negative** (rule 3).
- Grades: 0 H, 0 C, 0 S. No token is read.

**What the two records are.**
- One browser login, `tools/decode_browser_login.js 9119 ... --fetch-page RecordsView/9117 --guess-fullsize`.
- The full-size images were served (6 pages, about 5000x7000 px; none was the forbidden.png placeholder). They are
  not committed. Re-fetch them the same way: IMG_R9119_I42603_P1-P4, IMG_R9117_I42597_P1-P2.
- **Neither is a period key sheet.** Both are a printed numbered form (1-600, six columns of 100) filled in by a
  later hand.
- 9119 (Add MS 32256 ff.8-9; P2 is the filled form, P3 its continuation with notes, P1 and P4 blank or endorsement).
  - Header: "Corresp. between K. Charles I, Pr. Rupert, Sir Edw. Nicholas, Sir Edw. Hyde & Sir R. Browne during the
    Civil War ... Key made to the cypher ... 1820 ... F.W.S.", "The K. and Sir Edw. Nicholas. 1644", and a margin
    note "From Evelyn's Memoirs edited by ...".
  - Below the table are worked decipherments of King-to-Nicholas letters of Oct 1645. Examples: "Bridgnorth 9th
    Aug. 1645 ... Digby hates 358.39.31.19.35.53"; "P.113 ... 16th Oct. 1645"; and "2.50.151.57.60 = r + forward s
    +". The page numbers cited (P.102, 111, 113) are presumably those of the Evelyn Memoirs edition.
  - So 9119 is a 19th-century reconstruction built from the Nicholas cipher letters it worked through. It fills only
    the codes those letters used: 147 non-blank rows in 1-400 (71 letter or null rows in 1-100, 76 word rows).
- 9117 (Add MS 32256 f.6): "King Charles I to Lord Culp[epe]r 1645, Duplicate". It is the same form: letters and
  nulls in 1-78, scattered words in 157 and 301-600.

**Transcription.**
- Crops come from the shared tool, one crop per printed 20-row block. Auto line-finding misread the hand-filled form,
  so the centres were set by eye. Commands, as run:
  - `python3 tools/iiif_lines.py --image <IMG_R9119_I42603_P2.jpg> --out ciphers/maurice-rupert-1645/key9119/crops
    --region {1460,2200,2930,3660},960,790,5000 --prefix p2c{1..4} --centres 516,1464,2412,3360,4380`
  - Notes: `--region 1300,5780,3585,1220 --prefix p2notes --centres 300,900`.
  - 9117: `--image <IMG_R9117_I42597_P1.jpg> --out .../key9117/crops --region 820,270,800,4660 --prefix p1c1
    --centres 531,1435,2339,3243,4147` and `--region 2820,330,720,4600 --prefix p1c4 --centres
    471,1375,2279,3183,4087`.
- 9119 had two blind Opus passes on the crops: pass A (148 rows, plus the notes) and pass B (153 rows, read in reverse
  column order). Raw agreement was 136 of 153 rows. The worker settled the other 17, giving each reason in the note
  column of `keys/key9119.tsv`:
  - 28 = h: the ascender is visible on the crop.
  - 151 = forward, from the reconstructor's own worked note.
  - 398 is a dash only, so it was left blank.
- 9117 rows 1-80 had one blind Opus pass (C). The worker read rows 301-400 from the p1c4 debug overlay (single
  reader). Rows 401-600 were not transcribed, because the letter's codes stop at 398.
- Files: `keys/key9119.tsv`, `keys/key9117.tsv`, the raw passes `keys/passA.tsv`, `keys/passB.tsv` and
  `keys/passC_9117.tsv`, and `keys/key9119_notes_passA.txt`.

**Test** (`keys/key_test.py KEY`; `--check` exits 0 for both).
- Statistics: coverage, and the en16_repo 4-gram score and word cover of the rendered text (as key118_test.py does).
- All-slot control: 1000 keys with the value column permuted over all 600 code slots, blanks included, so coverage
  can move too (rule 3).
- Banded control: 1000 keys permuted within each block of 100. The form fills letters in 1-100 by design, so the
  all-slot shuffle would credit any key of this layout for the target's low codes.
- Power control: 50 synthetic en16 letters enciphered with the key itself, cut to 93 tokens, with key rows blanked
  until coverage matches the target's. Each is ranked against 200 banded shuffles of its own key.

| key | coverage /93 | all-slot mean / p95 / rank | banded mean / p95 / rank | 4-gram (banded p95, rank /1001) | power | judge |
|---|---|---|---|---|---|---|
| 9119 | 35 | 22.8 / 33 / 28 | 35.8 / 45 / 509 | -1.521 (-1.439, 159) | 0/50 | FAIL -1.521 vs real_p05 -0.579, N=94 |
| 9117 | 23 | 12.7 / 21 / 18 | 21.1 / 27 / 261 | -1.894 (-1.404, 813) | 1/50 | FAIL -1.894 vs real_p05 -0.611, N=25 |

- The 9119 render (cipher tokens only, clear words dropped): "g from d g c h y Banbury g from found h no i b leave no d
  from of leave forward l from k no e his next from d forward no me part".
  - Code 26 reads as a bare "g" four times. The letter codes read as consonant strings, not words.
  - "Banbury" (329) is the only proper name.
- What the numbers say:
  - The coverage excess over the all-slot control is the form's layout, not a fit. Under the banded control the
    target sits at the median (rank 509).
  - The power control shows that 4-gram scoring cannot separate a true key from a banded shuffle at 35 covered tokens
    (0/50). The language FAIL therefore cannot exclude 9119 as this letter's key family: rule 3 non-test, untested by
    this instrument.
  - For 9117, the King-Culpeper key, the fit is at chance on every statistic. Its language test also has no power at
    23 tokens (1/50).
- **Grades (rule 4):** none. 35 tokens (9119) and 23 tokens (9117) take a value from the form, but neither key is shown
  to be this letter's. They are a key test, not a reading.
- Rule 10: search results only.

Requests:
- de-crypt.org: 1 login plus 13 fetches (2 record pages, 6 thumbnails, 6 full-size images), 1.8 s apart. The saved
  pages stay in the scratchpad and are not committed; the account name was not written anywhere.
- No other host.
- Vision calls: 3 (passes A, B, C), plus the worker's own two crop checks for reconciliation.

## Remaining gaps (FT4f, 3 Oct 2026; GAPS47, GAPS52 3 Oct 2026)
Read so far: 0 of 93 tokens at any grade. Keys tested, all with judge FAIL: no. 118 (rank 80/201); Osborne P4 (rank 175/201); Osborne extended (rank 148/201); DECODE 9119 reconstruction (banded 4-gram rank 159/1001, coverage at the banded median, power 0/50 so a non-test); DECODE 9117 (chance on every statistic). See NOTES FT4b, FT4d, FT4e and GAPS52.
- The letter's own key, or a decipherment of the 7 July 1645 leaf, in Rupert's papers BL Add MS 18980-82 (the leaf is not itemised in the catalogue) - blocker: needs-physical-access; BL images have been offline since the 2023 cyberattack, and the copy order is ASKS row 56 / REQUEST.md. Every key reachable online was tested: Digby cabinet no. 118, the DECODE 8627 index, Osborne 8443/8444 in full, Cryptiana Nicholas-Rupert, Bourdeau's King-Queen SP106-5, and DECODE 9119/9117 (GAPS52).
- Secondary witnesses for the 7 July leaf (GAPS47, 3 Oct 2026): BL Add MS 30305 is read from its catalogue record. It has no Maurice letter and no 7 July 1645 item. Bodleian MSS Firth c. 6-8, the transcripts of Rupert's letters made for Warburton - blocker: waiting-on LOCAL-QUEUE row L43; their holding record is Anubis-blocked from the cloud, so the owner's desk runner reads the Firth c. 6-8 record, its availability flag and the 7 July 1645 folio
- The "Keys to cyphers" at BL Add MS 30305 f.86 (Charles I, undated; Nicholas 1646-58), which could hold a key covering this letter's codes - blocker: needs-physical-access; the record has no Digitised Content line, and BL images are offline since 2023. Added to REQUEST.md beside the ASKS row 56 BL copy order
- The 9119 key family (Charles I/Nicholas ministers' cipher) at this letter's coverage (GAPS52, 3 Oct 2026). The 1820 reconstruction fills only the codes its source letters used. At 35/93 tokens the 4-gram test has 0/50 power, so the family is untested by this instrument, not refuted. A fuller key of the same family would reopen it - blocker: needs-physical-access; the candidates are the Add MS 30305 f.86 keys (gap above) and the 7 July leaf itself, under ASKS row 56
- Statistical key rebuild from the 93 tokens alone - blocker: too-short; 93 tokens with 63 distinct codes in a letters-plus-words nomenclator. The rule 3 controls on file show code+mark designs read only at pooled lengths (22-67% blind at N=720), so no solver can be expected to read this at N=93.

## Escalation (FT4f, 3 Oct 2026; GAPS47, GAPS52 3 Oct 2026)
- [x] siblings: BL item lists of Add MS 18980-82 (FT4f) and Add MS 30305 (GAPS47) read: no Maurice-Rupert cipher sibling, and DECODE has no 18980/18981 records and no 18982 keys; Digby-cabinet key index DECODE 8627 and key no. 118 (FT4/FT4b, excluded, control-backed); Add MS 18982 ff.95-96 is a different letter, Osborne 10 Nov (FT4c); Osborne 8443/8444 are read in full, see known-keys
- [x] clear-pages: the Osborne clear text (8443 P1, P2; 8444 P2) was read by FT4e and gives no crib for this letter; the letter's own clear tail ("Garrison ... Accordingly") is in ciphertext.txt
- [retired] known-keys: the Osborne-Rupert sibling key was transferred by 4-gram vs shuffled-key control plus the judge, twice: FT4d rank 175/201, then FT4e with 40 more pairs rank 148/201, judge FAIL both times, coverage 17-19/93. Rule 3's third-attempt clause applies: untested-by-this-instrument, not refuted. It reopens only on new material, such as Osborne's own key sheet or a key reaching codes 290-398. Key no. 118, the Cryptiana Nicholas-Rupert key and King-Queen SP106-5 are excluded. DECODE 9119 and 9117 (GAPS52): both judge FAIL. 9119 is non-test on language (power 0/50 at 35 tokens) with coverage at the banded median; 9117 is at chance with no power (1/50 at 23 tokens)
- [x] print: Warburton, Memoirs vol. iii pp.131-137, read at the page: the cipher is printed without a decipherment. FT4f grepped all three volumes and the vol. i calendar for this letter: no key, and no gloss beyond the clear text. CSP Domestic 1644-5 was full-text searched (LANE CX2)
- [n/a] key-rebuild: 93 tokens is too short for a letters-plus-words nomenclator (gap above)
- [x] image-check: Warburton's printed cipher matches ciphertext.txt group for group (LANE CX2). The manuscript leaf is not reachable (gap above)
- [x] retry: the Osborne step was retried with the full remaining material (FT4e). The rule 7 checks pass: osborne_test.py, osborne_test2.py, decode_key.py --check, keys/key_test.py key9119|key9117 --check
Verdict: parked: every gap has an outside blocker

## While waiting

- The one action that depends on nobody is to find where the 9119 reconstructor's source letters are printed. The form
  cites "Evelyn's Memoirs", pages 102-113, with King-to-Nicholas letters of Oct 1645. Locate that edition on Internet
  Archive and grep it, with no login, for cipher numbers printed beside decipherments. Each printed pair would add a
  code-value row of the same ministers' family to key9119.tsv. Re-run keys/key_test.py only if coverage rises well
  above 35/93, because the power control needs more covered tokens. Depends on nobody; about $2. (GAPS52, 3 Oct 2026)
- 5 Oct 2026 (PR-LAND-67): LOCAL-QUEUE L43 answer landed, local-runner/L43-2026-10-05.md -- MS. Firth c. 6-8 (1849 Rupert transcripts; c. 6 and c. 7 "NOT AVAILABLE ONLINE") carry no per-volume dates or item list; the 7 Jul 1645 letter not located in the catalogue; originals mostly BL Add. MSS. 18980-2.
