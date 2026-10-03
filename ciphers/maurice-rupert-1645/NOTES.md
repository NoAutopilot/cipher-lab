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
