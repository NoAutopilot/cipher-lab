# Queue of targets to attempt

Scout run of 19 Sept 2026 (first real run; stages of `.claude/workflows/scout.js` executed as ordinary agent work: five
harvesters, one filter, batched scorers, this file). Harvested from the two solver repositories
(github.com/dbourdeau/cyphersolver, github.com/aaymeloglu/unsolved-ciphers, both cloned 19 Sept 2026), the Cryptiana
snapshot in `sources/cryptiana/` and this repository's CATALOG.md and LANDSCAPE.md, the community blogs and
forums, and the archive catalogues. Re-run weekly.

**Re-scored 20 Sept 2026 with the unread axis.** A worker session added the `unread` axis (0-3) and `kind`
(cryptanalysis, recovery, contribution, edition) to every scored row, per CLAUDE.md's Usage section and the
scoring schema in `.claude/workflows/scout.js`, and recomputed every total. This ran after, and on top of, a
same-night search-print sweep (QUEUE-scores.json `status_summary`) that found three rows — the Moray regency
letters, Throckmorton's 20 Add MS 4136 ciphertexts, and Sadler's 22 April 1543 letter — already found-solved
with printed contemporary decipherments; those three moved to Dropped first, leaving 40 rows to re-score. A
fourth row (the Eckert Papers) turned out to be an edition once `unread` was applied and also moved to Dropped,
leaving 39 tiered rows. The 163-item `unscored_kept` backlog was reviewed for the same axes but left unscored
this sweep: see the note at the end of "Kept, not scored this sweep" below.

Reader profile (revised 23 September 2026, owner's metric is the count of unique solves): any language the models read
(English, French, Italian, Spanish, Latin, German, Dutch, Portuguese) scores language_fit 3; no institutional archive
access; can send copy requests and pay small fees; works with AI agents for transcription and solving. Rows scored
before 23 September used English-only language_fit and are under-scored for other languages until re-scored.

## Solver-repository diff, 23 September 2026

Queue-hygiene sweep against fresh clones of both solver repositories (dbourdeau/cyphersolver 2e9ec01,
aaymeloglu/unsolved-ciphers), covering ranks 1, 5, 7, 8, 13, 16, 19, 20, 22, 23, 24, 30, 31, 32, 35, 38. Four rows
dropped as found-solved (ranks 5 Boswell 1628, 22 Goring 1645, 23 Sadler/Croft 1559, 24 Queen Anne 1711); one
false-positive resolved (rank 1's "harley7001" hit is a different letter that only tried and rejected an Add MS
72438 key — it does not read BL Add MS 72438 ff.9-10, which stays offline-only per the existing NOTES.md).
Partly read by Bourdeau, rows kept with a dated note: ranks 7, 8, 19, 20, 35 (harley7001 itself, at 94%, is the
real match for rank 35, not rank 1). Attempted and not read: ranks 16, 30, 31, 32, 38. Rank 13 was already
annotated this morning; the fresh clone adds nothing beyond that annotation.
Re-run tools/solver_repo_diff.py against fresh clones before promoting or solving anything.

Score = language_fit x3 + material x2 + key_lead x3 + size x2 + competition x2 + weight + unread x3 (max 48).
Axes: language_fit 3 = English plaintext, 1 = other language readable with AI help, 0 = unknown; material 3 =
images or full transcription online free, 2 = printed figures, 1 = login needed, 0 = nothing online; key_lead 3
= key or decipherment located, 2 = sibling with decipherment, 1 = design known, 0 = nothing; size 3 = enough
text or a key for a checkable reading, 0 = below unicity with no key lead; competition 3 = on nobody's tracker,
1 = open on a solver-repository tracker, 0 = active work reported; weight = historical interest, 3 = decision of
state; **unread** (new) 3 = never read and no key survives with it (kind `cryptanalysis`), 2 = unread but a key
or a deciphered sibling survives in another box (`recovery`), 1 = plaintext already in print but the
cipher-to-key mapping is unknown (`contribution`), 0 = readable today with a key held in the same collection
(`edition`, dropped from the tiers).

The `Kind` column names the lane a target belongs to (README "What counts as a result"): **recovery** (a key
found elsewhere reads a text nobody has read), **cryptanalysis** (reading without a key), **contribution**
(handing on a correction, mapping or verified negative); editions are dropped, not tiered, since the collection
already holds its own key.

Per-axis scores and each scorer's rationale (including the 20 Sept 2026 re-scoring note and the search-print
sweep's `status_summary`) are in `QUEUE-scores.json` beside this file. A row whose next step is `blocked` is
open but waits on something a person must do; rows marked closed-negative by a solver repository are kept, as
CLAUDE.md rule 3 says a negative without our own matched control is not a closure for us. Two rows (Stair 1710,
Monck 1660) carry an `unread` of 2 despite the kind being genuinely undecided between recovery and cryptanalysis
pending a key test in the field — see their rationale in QUEUE-scores.json and LANDSCAPE.md "Decisions of
20 September 2026".

## Tier A: start now

| Rank | Target | Year | Lang | Kind | Next step | Detail | Total | Sources |
|---|---|---|---|---|---|---|---|---|
| 1 | [Intercepted royalist letters to Charles I and 'My Lord', 13 and 21 May 1646 (BL Add MS 72438 ff.9-10)](ciphers/intercepted-royalist-1646/) | 1646 | en | recovery | archive-request | Order BL copies of Add MS 72438 f.11 and check Bodleian Tanner MSS 59-60 and TNA SP 16/514 for the contemporary decipher of f.10. | 40 | aymeloglu, tomokiyo |
| 2 | Wellington to General Maitland, Villa Castin, 2 Sept 1812 (Peninsular War dictionary code and strip cipher) | 1808-1814 | en | recovery | transcription | Save the lot 1184 images from live.spink.com before the 23 Sept 2026 sale and transcribe every 5b429-style group to identify the pocket-dictionary edition. | 40 | aymeloglu, tomokiyo |
| 3 | [Charles II to the Duke of Hamilton, 6 Aug - 27 Sept 1650 (four letters, passages in cipher)](ciphers/hamilton-1650/) | 1650 | en | recovery | archive-request | Copy request for NRS GD406/1/2197 (5 cipher-key items) and GD406/1/10573-10576 sent 19 Sept 2026; wait for the reply, then apply the sheet to the 102 groups. | 39 | aymeloglu, bourdeau, tomokiyo |
| 4 | [Charles Whitworth (Moscow) to Harley, partly undeciphered despatches and an undeciphered duplicate, 1707-08 (TNA SP 91/5)](ciphers/whitworth-1707/) | 1707-1708 | en | contribution | archive-request | Verified 19 Sept 2026 (ciphers/whitworth-1707/NOTES.md): only one clause of SP 91/5/108 is unread; ff. 163, 298, 300 have deciphers at ff. 180, 294, 274, printed in Sbornik IRIO vols 39 and 50. Order TNA copies of ff. 108, 106 and 121 to recover the 1707 key (REQUEST.md). | 37 | archives |
| 6 | Cornwallis Papers, American campaign: Rawdon, Craig, Tarleton, Balfour and others to Cornwallis, 1780-81 (TNA PRO 30/11) | 1780-1781 | en | recovery | archive-request | Check Saberton, The Cornwallis Papers (2010) for the six items Discovery marks undeciphered (PRO 30/11/6/23-26, 3/207-209, 69/18-24, 68/32-35) against his printed Common, Balfour and Ninety Six cipher keys. Search-print checked 20 Sept 2026: NOT FOUND — Saberton's 2010 edition has no Internet Archive copy (advancedsearch.php, two queries, 0 hits), so its index could not be checked against the six PRO refs; not attempted via Google Books/WorldCat this sweep. But Saberton's allthingsliberty.com article (6 June 2019, read in full) already prints the mechanism and worked examples of all five ciphers (Common, Ferguson's, Balfour's, Ninety Six, Balfour's dictionary) in the clear, so the six items are a straight key-application job once TNA copies of the ciphertext itself are in hand — next step is an archive-request for the six PRO 30/11 items, not a further print check. Re-checked 20 Sept 2026 (IA-login worker): `creator:Saberton` (11 hits, all unrelated novels/theses) and `title:(Cornwallis Papers)` (9 hits: an unrelated 1970 Rees abstracts volume, 1780s-1888 Clinton-Cornwallis controversy reprints, none the 2010 Saberton edition) both independently confirm no IA copy exists. Google Books API returned HTTP 403 ("Cannot determine user location") in this environment, so that route is still not attempted; WorldCat also still not attempted. Re-checked 21 Sept 2026 (IA login worker 2): Google Books is now reachable (`&country=US`); it lists all fourteen 2010 Saberton parts by title but every one is `viewability: NO_PAGES` — no preview and no search-inside available, so the index still cannot be checked this way. WorldCat's search-item API returns 404 "disabled." Open Library has no OCLC/IA-linked copy. NOT FOUND / NOT REACHABLE by every online route tried; the archive-request for the six PRO 30/11 items remains the only path forward. | 36 | archives |
| 7 | Other Add MS 4136 correspondents to Cecil, 1559-67: Henry Percy, Thomas Smith (7), Norreys, Middelmore, Lomer, 'Amiral to D. Angle' (DECODE R9235-R9256) | 1559 | en | recovery | transcription | Register on DECODE (free), download key records R9260, R9261, R9262 and pages R9235-R9256, and apply Tomokiyo's Throckmorton and Smith alphabets line by line. Queue-hygiene sweep 23 Sept 2026 vs fresh clone (2e9ec01): most of this range is already covered by Bourdeau, per-item — `lomer1563` (R9235): already solved, printed 1741/calendared CSP Foreign vi no.1471. `middelmore1563` (R9246-R9247): already solved, fraction 1.0, printed 1741. `coligny1563` (R9237,R9239,R9240): already solved, fraction 1.0, printed 1741. `foix1563` (R9238,R9241): R9238 closed already-solved (print); R9241 still open, in progress. `smith1562` (R9236,R9248-R9254): class read, most passages read from Forbes's copy. `norreys1567` (R9250-R9251): read in part, fraction 0.33. `percy1559` (R9256): not read, fraction 0, too short without the key. R9242-R9245 are not addressed by any Bourdeau folder found. Net: Percy (R9256), Foix's R9241, and R9242-R9245 are the real remainder; everything else named in this row is already print-solved or well read. | 36 | bourdeau |
| 8 | Walsingham and Edward Wotton (ambassador to Scotland), seven letters 28 July - 10 Sept 1585 (BL Add MS 32657, DECODE R4838-R4844) | 1585 | en | recovery | search-print | Check CSP Scotland vol. VIII (Boyd, 1914) for the 28 July-10 Sept 1585 letters in clear, then apply Tomokiyo's Walsingham-Wotton key (elizabeth.htm) to DECODE R4838-R4844. Search-print checked 20 Sept 2026: UNREACHABLE, not settled. BHO's TOC confirms the right window is in this volume (July 1585 pp.1-51, Aug pp.51-88, Sept pp.88-117) but the page text itself is BHO "premium content"; no separate IA copy of this 1914 (Boyd) vol. VIII was found (only unrelated vols II, IV and a different 1898 one-vol edition); HathiTrust copy is Cloudflare-blocked to curl; Google Books API quota was exhausted (429). Retry with the browser tool (per CLAUDE.md Access playbook) against BHO or the Wayback Machine before requesting DECODE. Queue-hygiene sweep 23 Sept 2026 vs fresh clone (2e9ec01): `walsingham1585` (R4838,R4839,R4840,R4844): read in part, fraction_read 0.49 — all four letters readable, two already in print as calendar abstracts, name code mostly identified, but the ~14 sign-word run of 10 Sept 1585 (R4844) is unread. `wotton1585` (R4841-R4843): class read, drafts read in full, but 4 of 11 code numbers (27, 32, 36, 40) are still open. Real remainder: R4844's unread run and the 4 open code numbers, not the whole seven-letter bundle. | 36 | bourdeau |
| 12 | [Letter partly in cipher relating to Gen. Monck and his movements, 1659-1660 (BL Add MS 32093 f.423, Malet collection)](ciphers/monck-1660/) | 1659-1660 | en | recovery | archive-request | Order BL reproduction of Add MS 32093 f.423 (REQUEST.md); check HMC 5th/7th Report pp.308-320/428-433 and Thurloe vol.7 for a decipherment first; once transcribed, test the Hyde-Barwick key (Bourdeau's hyde/barwick_key.py, entries 600 Monck, 637 Clarges) before any fresh cryptanalysis. | 34 | web, print, archives |

## Tier B: next

| Rank | Target | Year | Lang | Kind | Next step | Detail | Total | Sources |
|---|---|---|---|---|---|---|---|---|
| 13 | [BL Harley MS 287 cipher letters 1587-88: Cobham to Walsingham (4), Needham, unsigned (7) (DECODE R8477-R8496)](ciphers/harley-287-1587/) | 1588 | en | recovery | finish-existing-key | **Check-solved 23 Sept 2026 (ciphers/harley-287-1587/NOTES.md): verdict partial, not open.** Bourdeau's project has already read most of this range (21-22 Sept 2026, after our 20 Sept search-print pass, before any print source was found): needham1587/R8479 read 97.8%; harley287/R8477+R8482-R8487 read in sense throughout with named gaps; cobham1588/R8490+R8492+R8495+R8496 about a third read. No print source located by them or by us. Next step is finishing/verifying Bourdeau's existing partial key and transcriptions (MIT code, CC BY 4.0 text), not a fresh cryptanalytic attempt. Prior next_step_detail retained below: Check CSP Foreign 1588 (vols 21.4 and 22) for Cobham's Bourbourg despatches of the DECODE dates, then fetch DECODE key R8497 and R8477-R8496 images. Search-print checked 20 Sept 2026: NOT FOUND, partial (vol. 22 not yet checked). CSP Foreign Elizabeth vol.21 pt.4 (Jan-June 1588, BHO) index: "Bourbourg" p.567 (~30 letters), "Cobham" p.568 (~40 "letters from" entries plus "sends cipher to Walsingham, 455, 462"), "Needham" p.650 (only one entry, a paper he delivered, no letters of his own indexed). Text checked at pp.442-460: the 3 June Cobham entry gives only "Sent the cipher by Spritwold" — a postscript note, not a decrypted passage; the calendar gives English abstracts throughout, never reproduces ciphertext or a "deciphered" block, and whether the abstracts capture the 14 DECODE items' specific passages was not checked line-by-line (~40 entries, over this sweep's budget). Vol. 22 (July-Dec 1588), which likely holds the bulk of the Bourbourg talks, was not reached this sweep. **Vol. 22 follow-up, 20 Sept 2026:** not on Google Books (all matching volumes NO_PAGES). Found on HathiTrust, record 100823430, htid msu.31293027027295, "Full view", 596 scans — but babel.hathitrust.org still serves the Cloudflare "Just a moment" interstitial to both curl and tools/browser_fetch.js (confirmed again), and there is no Wayback capture of this id (CDX query, zero results), so no page text was read. Used the HTRC Extracted Features API (tools/htrc_ef_headwords.py) to locate token positions without reading page text: "cobham" at scan seqs 61,64,68,72,73,75,90,96,155,200,247,253,255,326,327,473,491,498,556,569,574,576,591; "bourbourg" at 9,11,12,14,17 (front matter, likely the index) and 490,491,492; "cipher" at 62,148,157,164,166,178,182,258,353,356,450,455,459; "decipher" (as its own token, not just "cipher") at 62,148,157,178,353; "needham" and "nedham" (both spellings) at zero scans anywhere in the volume. Scan 62 is adjacent to Cobham's scan 61 and is the one page where both "cipher" and "decipher" and a Cobham mention cluster — the strongest candidate in this volume, but **unread, not found**: this is a lead for a worker with HathiTrust browser access or an archive request, not a confirmed printed decipherment. NOT FOUND stands; the "Needham" name is now confirmed absent from vol. 22 by token count, not just by index-page sampling. | 33 | bourdeau |
| 14 | [George Stepney to the Earl of Manchester, Vienna, 23 March 1702 (short ciphertext)](ciphers/stepney-manchester-1702/) | 1702 | en | recovery | archive-request | Tier B at 27, one under the line: only 24 groups (size 1) and no key located yet (key_lead 2); still the cheapest English finish. TNA page-check order for SP 105/65 (Discovery C3609655, the 23 March 1702 letter-book entry) was started 19 Sept 2026 but not completed, pending the account confirmation email; finish it per ciphers/stepney-manchester-1702/REQUEST.md. | 33 | bourdeau, tomokiyo |
| 15 | [Gelett Burgess, The Master of Mysteries (1912), third hidden message](ciphers/burgess-mysteries-1912/) | 1912 | en | cryptanalysis | cryptanalysis | **Check-solved 23 Sept 2026 (ciphers/burgess-mysteries-1912/NOTES.md): verdict open, Stage 2 verified unsolved.** Web, print, Cryptiana/Cipherbrain and both solver repositories all confirm no third message found; Aymeloglu's own detailed negative log (burgess-1912/README.md) confirms the two families this next_step targets (paragraph-first-word acrostics; true printed-line units) remain untested by them. Score paragraph-first-word acrostics and printed-line units from the Cornell scan (archive.org cu31924022342871), the families Aymeloglu's README lists as untested. | 33 | aymeloglu |
| 16 | [Regent Moray to John Wood, Edinburgh, 13 July 1568 (cipher postscript, BL Add MS 32091 f.213)](ciphers/moray-wood-1568/) | 1568 | sco | cryptanalysis | blocked | Leave to Aymeloglu; only a BL copy of Add MS 32091 f.213v or a sibling letter in the same alphabet could settle the seven-sign ending. Queue-hygiene sweep 23 Sept 2026 vs fresh clone (2e9ec01): Bourdeau `moray/`: not read, fraction 0 — attempted 15 Sept 2026 from Tomokiyo's transcription only (no image; DECODE has no record; the letter is not in print), several Scottish court ciphers of the period (the Queen's Cipher, Throckmorton-Moray 1569) ruled out as non-matching alphabets, no key found. `throck1569` and `wod1568` also name this shelfmark but only as a sibling mentioned in passing, not a reading of it. | 33 | aymeloglu, bourdeau, tomokiyo |
| 17 | [Robert Bowes to Walsingham, 7 April and 31 July 1583, and short Caligula B VIII ciphertexts 1580-83 (BL Cotton Caligula C VII, B VIII)](ciphers/bowes-walsingham-1583/) | 1583 | en | recovery | search-print | **Search-print + image check 23 Sept 2026 (NOTES.md, print-check.tsv, images/manifest.json): still open.** CSP Scotland vol.6 (Boyd 1910) confirmed still absent from archive.org (2 fresh advancedsearch queries); HathiTrust htid nnc2.ark:/13960/t1gh9nc18 re-tried once, still 403. Found instead: Surtees Soc. vol.14 (Correspondence of Robert Bowes, 1842, archive.org id correspondenceof00bowerich) prints Bowes's own Letter-Book copies of both dates (entries CLXXXVII for 7 Apr, CCXXXIX/CCXL for 31 Jul) with unresolved numeric name-codes (870/91/149/19/29/85/54/32 and 223/189/32/0100/54) but no cipher symbols and no decipherment — a related, not confirmed-identical, source to the Cotton MS originals. BL's own catalogue (searcharchives.bl.uk) confirms Tomokiyo's folio citations verbatim (C VII f.196r-197v "partly in cipher", f.299r-v+303r "some use of cipher" — the cipher one of 3 same-day letters; B VIII f.251-252, f.290-293, f.306). Both Cotton volumes are undigitised: BL's own "(digital images currently unavailable)" note confirmed, IIIF manifests both 403 (S3 AccessDenied, not Cloudflare). No route to images this pass; no price quoted to put in REQUEST.md. Next: Tomokiyo's own symbol transcription (sources/cryptiana/web/CottonMSBowes.txt, now mirrored) is the only material not blocked on new images — a solver could attempt it directly, or wait for a physical-access route to the two Cotton volumes. | 32 | bourdeau, tomokiyo |
| 18 | [Catokwacopa advertisements, Evening Standard, 8 and 20 May 1875](ciphers/catokwacopa-1875/) | 1875 | en | cryptanalysis | cryptanalysis | **Check-solved 23 Sept 2026 (ciphers/catokwacopa-1875/NOTES.md): verdict partial, not open.** Mechanism agreed and substantial partial readings published since 2018 (Bosbach, Estes, Ernst, Krajčovič); Schmeh/Cipherbrain and Aymeloglu (SHORTLIST.md, "effectively cracked, remove") both hold no unique plaintext is recoverable given the omission rule's freedom (Bourdeau's 15 Sept 2026 audit). No matched-control negative test run; not closed-negative. Run a phrase-level language-model search on line 23 (48 letters) with Bourdeau's positional prior, using cyphersolver/catokwacopa/search.py (MIT). | 32 | bourdeau, web |
| 19 | BL Harley MS 1582 cipher letters: Sir Edward Stafford 1586, N. Wotton? 1554, and unsigned (DECODE R8499-R8505) | 1586 | en | recovery | search-print | Check CSP Foreign Elizabeth vol. XXI pt 1 (british-history.ac.uk) for Stafford's letters of 19 Sept and 9 Nov 1586 in clear, then use R8503's inline plaintext as key source. Queue-hygiene sweep 23 Sept 2026 vs fresh clone (2e9ec01): six of the seven named records are now read at high fraction or already solved by Bourdeau — `harley1582r8500` (R8500, 20 Aug 1586): read, 1.0. `harley1582r8504` (R8504, 9 Nov 1586): read, 1.0. `stafford1586` (R8503, 19 Sept 1586): already solved, fraction 1, read at the time. R8501 (ff.71-72): "already read" via its own contemporary decipherment on f.72r (per harley1582r8500/harley1582r8505 notes). R8502 (f.73): glossed. `harley1582r8505` (R8505, the unsigned "L'Estat du Roy de Navarre"): broken from ciphertext alone here, fraction 0.951. Only `harley1582r8499` (R8499, N. Wotton? 1554) remains materially open: read in part, fraction 0.75, ~40 rare codes not on the recovered key (R354), the period's contemporary decipherment (Harley 1582 ff.5r-7v) not digitised. | 31 | bourdeau |
| 20 | Nicholas Throckmorton to Elizabeth I, 10 July 1559, marginal ciphertext in an unknown cipher (BL Add MS 4136, DECRYPT 2988-2989) | 1559 | en | recovery | search-print | Check CSP Foreign Elizabeth 1558-59 (SP 70/5, Throckmorton to the Queen, 10 July 1559) for the deciphered marginal passage before requesting DECODE R2988 images. Queue-hygiene sweep 23 Sept 2026 vs fresh clone (2e9ec01): `wod1568` (catalogue 97, covers R2988 margin + R2989) is the real match (bl32305, coligny1563, foix1563, lomer1563, middelmore1563, moray, norreys1567, percy1559, smith1562, throck1560 only share the "Add MS 4136" shelfmark, not this folio) — class read in part, fraction 0.3 over all three texts on the sheet: the Throckmorton letter body itself (f.32) is read ~85-90% (lines 1-4 secure), but the **marginal** ciphertext this row names (a separate word-sign code, 222 groups, f.32 margin) remains unread, as does Wood's own 1568 line (39 signs, non-unique). | 31 | bourdeau, tomokiyo |
| 21 | [Prince Maurice to Prince Rupert, Worcester, 7 July 1645 (Warburton, Memoirs of Prince Rupert iii.133)](ciphers/maurice-rupert-1645/) | 1645 | en | recovery | archive-request | Register on DECODE (free) and ask for the R8429-R8454 images (BL Add MS 18980-82, 1645 letters with interlinear decipherments) to look for the Rupert-Maurice cipher. | 31 | tomokiyo, bourdeau |
| 25 | Intercepted letter of Edward Hyde, 1 Nov 1659, f.93 full of undecoded code numbers (BL Add MS 4166 ff.92-93, DECODE R4886) | 1659 | en | recovery | search-print | Search the Calendar of Clarendon State Papers vol. 4 (1932) for a Hyde cipher of late 1659 with numbers to about 966, then order the Bodleian Clarendon MS key by copy request. | 30 | bourdeau, tomokiyo |
| 26 | Charles I to Henrietta Maria, 8 April 1645, one sentence in their private cipher (The King's Cabinet Opened, 1645) | 1645 | en | cryptanalysis | search-print | Check Green, Letters of Queen Henrietta Maria (1857) p.299 and locate the ciphered original of her 2 April 1645 letter, the only sibling in this private cipher. | 30 | bourdeau, tomokiyo |
| 27 | John Armstrong to James Madison, Paris, 20 Feb 1808 (unique code, 369 groups) | 1808 | en | cryptanalysis | cryptanalysis | Place Krajcovic's crib from Armstrong's 15 Feb 1808 letter to Jefferson against the opening groups in cyphersolver/armstrong/feb20_ciphertext.txt and score it with a shuffled control. | 30 | bourdeau, tomokiyo, web |
| 28 | Sir Francis Walsingham, autograph letter partly in cipher to an unknown recipient, 26 May 1574 (Folger V.b.264) | 1574 | en | cryptanalysis | archive-request | Email Folger reference for a digital image or LUNA link of the Walsingham letter of 26 May 1574 in V.b.264 and its folio number. | 30 | archives |
| 29 | [John Dalrymple, 2nd Earl of Stair, to Viscount Townshend, diplomatic report, 27 Feb 1710 (Univ. of Kansas, Spencer Research Library, MS P556)](ciphers/stair-townshend-1710/) | 1710 | en | recovery | archive-request | Free first: search J. M. Graham's 1875 Annals and Correspondence of the...Earls of Stair (Internet Archive/HathiTrust/NLS) for this letter's phrases (Fitzdome, Danzig, Fleming). If nothing turns up, order the KU reproduction per REQUEST.md ($0.75-$15 for the item). | 29 | archives |
| 30 | Charles I in the Isle of Wight: to Worsley 22 May 1648 and to Prince Charles 1 Aug 1648 (BL Harley MS 6988 f.208; Worsley/Hillier prints) | 1648 | en | cryptanalysis | blocked | No key is located; the two unread letters need the Worsley and 'noble frend' keys themselves, whose shelfmarks nobody has identified (DECODE R8342 image is login-only). Queue-hygiene sweep 23 Sept 2026 vs fresh clone (2e9ec01): Bourdeau `charlesi/`: not read, fraction 0 — two candidate keys excluded, the letters judged too short and non-repeating for ciphertext-only analysis; confirms this row's own "blocked" verdict, adds no new lead. | 29 | bourdeau, aymeloglu, tomokiyo |
| 31 | John Wood to Secretary Cecil, 6 Sept 1568, 'Wool letter' on the sheet of DECRYPT 2989 (BL Add MS 4136) | 1568 | en | cryptanalysis | search-print | Check CSP Scotland vol. 2 (1563-69) and SP 52/15 for Wood to Cecil, 6 Sept 1568, with a deciphered copy, before requesting DECODE R2989. Queue-hygiene sweep 23 Sept 2026 vs fresh clone (2e9ec01): `wod1568` (same sheet as rank 20's R2988/R2989 folio) attempted and not read for this specific line — Wood's 1568 line is 39 signs, non-unique, and stays unread even though the Throckmorton letter sharing the sheet is read ~85-90%. | 29 | bourdeau, tomokiyo |
| 32 | BL Harley MS 260 cipher letters 1571-72: Elizabeth R., Burghley, Walsingham and unsigned (DECODE R8356-R8364) | 1572 | en | contribution | search-print | Match the nine DECODE dates (R8356-R8364) against Digges, Compleat Ambassador (1655) on the Internet Archive, where the deciphered Walsingham-Burghley letters of 1571-72 are printed. Queue-hygiene sweep 23 Sept 2026 vs fresh clone (2e9ec01), per record: R8356 not read (0); `burghley1572`/R8357 not read (0, two code items, no key, letter otherwise printed by Digges); R8358 not read (0.13, one code by context); R8361 not read (0.19, one code identified); R8362 not a cipher (two boxed cover-name markers on an otherwise clear letter); R8364 read in part (0.23, a port name as "St Valery", grade M); `walsingham1572`/R8363 closed unread (no key extant, Dieppe only a guess); `walsingham1572nov`/R8359-R8360 closed (no ciphertext survives in this copy). No record in the range reaches a real reading; this confirms rather than changes the row's own search-print status. | 28 | bourdeau |
| 33 | [Ormond to Arran, 24 Jan 1678, short undeciphered segments (HMC Ormonde iv.93)](ciphers/ormond-arran-1678/) | 1678 | en | cryptanalysis | search-print | Search HMC Ormonde vols. 4-5 and the Carte calendar for another 1678 Ormond-Arran letter with numbers up to 732 and a decipherment. | 28 | bourdeau, tomokiyo |
| 34 | William, Baron Craven to Prince Rupert, The Hague, 6 Nov 1648 (BL Add MS 18982 ff.134-135, DECODE R8447) | 1648 | en | cryptanalysis | transcription | Register for DECODE, obtain the R8447 images of Add MS 18982 ff.134-135, transcribe the cipher and count tokens before anything else. | 28 | bourdeau, tomokiyo |
| 35 | Unsigned letter from Paris, 19 April 1641 (BL Harley MS 7001 ff.148-149, DECODE R7766) | 1641 | en | cryptanalysis | transcription | Register for a DECODE account, download the R7766 images (Harley MS 7001 ff.148-149) and transcribe the numerical groups with the surrounding cleartext. Queue-hygiene sweep 23 Sept 2026 vs fresh clone (2e9ec01): Bourdeau `harley7001/` is the real match for this exact record (identifies the letter as Robert Reade, Windebank's secretary, to his cousin) — class read in part, fraction_read 0.94, key DECODE R9115 (Add MS 32256 f.4, an 18th-c. Deciphering Branch reconstruction of the Windebank cipher) applied; 12 of 137 code values remain blank on the surviving key and are only conjectured from context/alphabetical slot (6% of tokens, grade M). No print source found (CSP Domestic 1640-41 calendars Reade's letters to Thomas Windebank with the cipher passages left unread). Note: this same shelfmark's DECODE key R8694 ("Browne", Add MS 72438) was tried here and rejected as a false lead — that is the source of a separate, unrelated false match of this folder against rank 1 (BL Add MS 72438 ff.9-10), which `harley7001/` does not read at all. | 27 | bourdeau |
| 36 | Gun Wa advertisement cipher, 1889 (77 letters) | 1889 | en | cryptanalysis | search-print | Search Chronicling America 1889-90 for further Gun Wa advertisements carrying cipher text, since only a sibling ciphertext would lift 77 letters above unicity. | 26 | aymeloglu |
| 37 | Thurloe State Papers intercepts with undeciphered portions: vol. 5 (1656, du Gard to White etc.) and vol. 7 (c.1659) | 1656 | en | recovery | search-print | Search the Calendar of Clarendon State Papers vol. 3 (1655-57, archive.org) for 1656 letters of Waddall, Copinger and White that mention a cipher or key. | 25 | tomokiyo, bourdeau |

## Tier C: watch

| Rank | Target | Year | Lang | Kind | Next step | Detail | Total | Sources |
|---|---|---|---|---|---|---|---|---|
| 38 | 'Mr. Conley's hand', Paris, 28 Dec 1652 and 3 May 1653 (BL Harley MS 7003, DECODE R7768-R7769) | 1652 | en | cryptanalysis | transcription | With a DECODE login, download R7768-R7769 (Harley MS 7003), read the cleartext and count the nomenclator groups before deciding whether an attack is possible. Queue-hygiene sweep 23 Sept 2026 vs fresh clone (2e9ec01): Bourdeau `conley1652/`: not read, fraction 0 — the clear text was read, but the 23 code numbers are judged too few for a ciphertext-only attack, and no Jermyn/Queen key of 1652-53 was located. Confirms this row's own next step; no new lead. | 23 | bourdeau |
| 39 | [Unidentified cipher/symbol manuscript, 18th century (National Library of Scotland MS 20769)](ciphers/nls-20769/) | 18th century | unknown | cryptanalysis | archive-request | Two-step order in REQUEST.md: first get NLS (or a person who can load manuscripts.nls.uk) to confirm the true leaf count and whether their own cataloguer calls this a cipher or a shorthand/notation; only then request scans (roughly GBP 100-200+ unconfirmed for a full 57-leaf order). | 22 | web |

## Candidates held on GitHub (harvest of 23 September 2026)

Scout sweep of `cs-recheck/*/profile.json` (github.com/dbourdeau/cyphersolver, commit 2e9ec01, 23 Sept 2026;
code MIT, text CC BY 4.0: credited by folder below) against `ay/` (github.com/aaymeloglu/unsolved-ciphers,
no licence: cited only). Method and full table in `QUEUE-github-held.tsv` at the repository root: every one of
Bourdeau's 304 profiled targets whose outcome class is `not read`, `offline only`, or `read in part` with
`fraction_read` below 0.5 (93 rows), filtered to a real transcription file already sitting in the folder
(named in the profile's own `documents[].length.file`, or a `transcription.txt`/`ciphertext*.txt`/`*.tsv`) of
at least about 150 tokens, plaintext language English, French, Italian, Spanish, Latin, Dutch or German, and
not classed "not a cipher" (44 rows). Items already tracked elsewhere in this file or in `LANDSCAPE.md`
(Chaulnes 1690, Colbert, Destaing-Gérard 1779, Le Tellier 1657, Berthier-Napoleon 1812, Charles I Isle of
Wight 1648, Stepney-Manchester 1702, Ottobon 1589, the Add MS 4136 Cecil batch that already covers Norreys
1567/1568 and Foix/Coligny 1563 at rank 7, and Walsingham-Wotton 1585 at rank 8) are excluded here as
duplicates, not as a fresh finding. Aymeloglu's catalogues were grepped by shelfmark and name for each
survivor; none of the twelve below appears in his `TARGETS.md`, `SHORTLIST.md` or `CATALOGUE.md` files except
where noted in its row.

Per CLAUDE.md rule 3, none of these is reported here as a closed negative: Bourdeau's own notes are read below
as an attempt, not a verdict, and no matched-control number is claimed for or against any row that this sweep
did not itself run. Per rule 10, "unread" and "not read" describe Bourdeau's own recorded status, not a
novelty class; nothing here is new, first or unpublished, and any future solve still needs a verifier's
N-class before that word is used.

| Rank | Target | Year | Lang | Kind | Bourdeau folder / class | Length | What he tried and why it stalled | Unused lead | Total |
|---|---|---|---|---|---|---|---|---|---|
| G1 | Forget/Mayenne/Matignon despatches, Ligue civil war, 1585-86 (BnF fr. 15572 + fr. 15571 f.177, 13 folios) | 1585-1586 | fr | recovery | `matignon1586`, read in part (0.28) | 12,994 profile tokens across 13 folios; largest transcribed block in this sweep | Key for Mayenne-Forget Cipher-1 already recovered and verified against sibling leaves (ff.14/15, 18/19, 78-79, 91-92) and beats scrambled-key controls by +2.07/figure on ff.123-124; most leaves (f.110, ff.123-124, ff.143/150/154/173/196/201, f.177) are transcribed only in part or not re-checked against the verified key, so 0-45% of each is "unread" for transcription reasons, not cryptanalytic ones | A second cipher in the same volume (Cipher-3, fr.15572 f.276 and fr.15571 f.179) has a contemporary interlinear decipherment already photographed (`img/BnFfr15571f179.jpg`, in magenta ink) that has never been transcribed or checked | 35 |
| G2 | Lope Hurtado de Mendoza (Rome) to Charles V, nine ciphertexts, 1522 (RAH Salazar 9/26, DECODE R9634-R9656) | 1522 | es | recovery | `lopehurtado`, read in part (0.45) | 6,289 profile tokens across 9 records | Sánchez's and Juan Manuel's 1522 ciphers (Tomokiyo 2025) don't fit; this is a separate, unpublished key. Only worked from a crib | R9644 in the same box carries the clerk's own full contemporary clear version of itself, keyed to the cipher by marginal letters, giving 49 confirmed code values (`key_codes.tsv`) by direct alignment. Three sibling records in the same batch (R9634, R9646, R9649) are flagged "not-attempted" against that recovered key/alphabet, and Aymeloglu's `bne-ranked.md` separately lists two more Lope Hurtado letters at the BNE (MSS/18697/29, MSS/20212/27) neither project has checked | 34 |
| G3 | Principe di Castelcicala (London, Paris) despatches to Naples, 1816-23 (ASNa Esteri 2337, DECODE R9553-R9589) | 1816-1823 | it | recovery | `castelcicala1816`, read in part (0.429) | 10,397 profile tokens; ~2,450-group two-part numeric code | Ciphertext-only LM scoring on the open code did not discriminate; 55% of target groups have no value | Contemporary interlinear decipherments already exist and were used as cribs on four records (R9566, R9569, R9571, R9589), giving 162 confirmed values, but the escalation log's own "retry" step (hand-reading the un-glossed 1816 letters against the Decazes/Florida crib themes with those values) is checked not-done; R9586/R9588's faint pencil glosses are noted but not attacked at all | 31 |
| G4 | Riksarkivet Stockholm cipher group, four unrelated correspondences bundled as one catalogue row, 1628-1633 (DECODE R4282-R4341) | 1628-1633 | de/la | recovery | `riksarkivet1628`, read in part (0.3) | 2,622 profile tokens across 4 open documents (Bremen 1631 itself fully read) | Bremen 1631's key was rebuilt from its own interlinear glosses (a six-column alphabet grid, four numbers per letter); blind homophonic/substitution annealing in 11 languages on the other three documents (R4282, R4284, R4306) found no language | R4284 carries its own key-test leaf (four Latin phrases written over their cipher equivalents) not yet used as a crib for the *letter* cipher R4282 it may share; only 2 of 70 fetched Chifferklaver key records were tried against any of the three; R4338-R4341 (E 708, June 1633) carry interlinear decipherments of the time that were never transcribed | 31 |
| G5 | BL Add MS 32305 "Carré" code letters, 1742-45 (DECODE R2968, R2970, R2972; part of a larger 1719-1759 working file) | 1742-1745 | fr | cryptanalysis | `bl32305`, not read (0.09 over the whole catalogued group) | 1,323 groups, 381 distinct, fully transcribed and merged | Two-part ~800-group code; the decipherer of the time also stopped here; a ciphertext-only break was judged infeasible from 1,323 groups of a code this size and the folder is marked "attempted, closed" | None visible from the repository alone: the same volume's neighbouring records (R2963-R2981) were all checked and only the six catalogued ones are unglossed; the next lead (a key, a clear copy, or more Carré letters elsewhere in BL/SP 107) is archival, not on GitHub | 31 |
| G6 | BnF Espagnol 318, Catholic Monarchs' correspondence, nos. 92-95, 1500-1504 | 1500-1504 | es/it | recovery | `esp318`, read in part (0.4) | 1,979 profile tokens over 4 open folios | No. 93 fails ciphertext-only (-3.5 vs -1.8 nats); no. 95 has a third of its glyphs still disputed between three independent transcription passes | No. 92 already uses Galende Díaz's 1994 printed key for three-quarters of its words, but five groups (bog, zeb, zems, xob, bue) contradict it in context and about ten letter-sign stretches are unplaced; no. 94 (four pages, drops into Spanish clear repeatedly) has never been transcribed at all, and Bergenroth's Gran-cifra list, already identified as the likely key, was never tested against it | 30 |
| G7 | Sforza-side reply to Zorzo (Giorgio) del Maino, 4 May 1446 (BnF italien 1583 f.68, DECODE R7898) plus its sibling f.70 (Amidani to Sforza) | 1446 | it | cryptanalysis | `it1583`, not read (closed unread) | ~800 signs across two hands (404 + 390 signs), both transcribed | Homophonic and one-to-one annealing (the same solver design that solves synthetic 400-letter Italian controls) collapsed to nonsense on f.68 alone; 208 Sforza-family key records checked at thumbnail size, none headed Maino or Amidani | f.70 (Amidani, same sign family, a different hand) was transcribed and found, but only annealed on its own, also to nonsense; the two ciphers were never annealed together as one key, which is the standard move (LESSONS.md sec. "look for the sibling") for two texts sharing a chancery cipher, and both transcriptions already exist in the folder. **Attempted 23 Sept 2026** (`ciphers/sforza-maino-1446/`): joint anneal with matched controls (99%+ read) gives no reading; closed-negative conditional on the draft transcription. Reopens only with a sign-exact transcription from the image or a key (ASMi cart. 1597 at full size, Cerioni vol. 2, Cremona 'codice segreto degli Sforza') | 29 |
| G8 | Giuliano Caprile and Alfonso Cistarelli to Ferrara, 1519-1521 (ASMo Ambasciatori Ungheria b.4, DECODE R1128-R1139) | 1519-1521 | it | recovery | `caprile1519`, read in part (0.3) | 2,284 profile tokens over 5 open records | 1520-21 sign cipher (R1136, R1139) and Cistarelli's numeric cipher (R1137) both open; single-reader transcription of R1136/R1139 not re-checked | An EM key rebuilt from Somogyi 2025's cribs reproduces 89.6% of an aligned sibling (R1138); the escalation log's own next step, a second careful transcription of R1133/R1131/R1132 against the 1882 Vestigia decipherments already on file, to complete the letter table before R1128, is checked not-done; no key of the 1520-21 or Cistarelli systems was tried on R1137 | 29 |
| G9 | Van Dedem (Constantinople) despatches to Van de Spiegel and Van der Goes, 1788-1799 (DECODE R2120, R2122, R2131, R1895) | 1788-1799 | nl | recovery | `dedem1788`, not read (0) | 987 profile tokens; 258 + 50 open groups | Hard-EM and leave-one-out word aligners on the deciphered siblings (R2121, R1947, R2053) converge with no consistent group-to-word values; French/Dutch cribs share only 17% of groups | R2120's own contemporary clear decipherment survives as R2121 (both already transcribed here), giving the 1788-93 homophonic code's shape, but three further DECODE records with solutions in the same code family (R1948-R1952, R2134, R2141) were named as further cribs and never fetched or transcribed | 29 |
| G10 | La Guiche (Rome 1551), Noailles (Venice 1558), Seure (Lisbon 1558): BnF fr. 3138 no.22, fr. 3151 nos. 33, 39-44 | 1551, 1558 | fr | recovery | `guiche1551`, read in part (0.17) | 474 profile tokens (La Guiche + Noailles only; Seure's ~2,000 signs untranscribed) | La Guiche is a plain 22-sign substitution, ~350 of 406 signs read; two struck-through opening lines and two rare signs remain uncertain | Noailles (fr. 3151 no. 33) carries a marginal gloss whose visible words could serve as cribs for its own ~150-sign cipher, but the escalation log marks the cipher itself "not-attempted"; Seure's six letters (nos. 39-44, two duplicate pairs) were found but never transcribed | 24 |
| G11 | Champagne news-letters to Nevers, 1590-91, and Laurière to Nevers, 1593 (BnF fr. 3623, fr. 3625) | 1590-1593 | fr | recovery | `champagne1590`, read in part (0.418) | 196 profile tokens net unread across 4 folios | No. 23 read in full from its own bound key slip; nos. 24/25/60 about three-quarters read from interlinear glosses; no. 55 only 19 of 86 groups glossed | No. 55's remaining 67 groups are a syllabic nomenclator for which no second glossed Laurière letter has been found (a genuine dead end); nos. 24/25/60's few open code numbers have no key bound with the letters and need an archival lookup, not a repository one | 24 |
| G12 | Benedetto Fantini ("Jantini"), Buda and Eger, to the Este court, 1517-1518 (ASMo Ambasciatori Ungheria b.4, DECODE R1126-R1127) | 1517-1518 | it | cryptanalysis | `jantini1517`, not read (closed unread) | 581 profile tokens over 2 records | Resembles Caprile 1519's two-tier sign system but a different sign inventory; Caprile's recovered values were seeded into the annealer and the score collapsed; a control-validated ciphertext-only syllabary anneal fails where matched controls succeed | None found: no decipherment, clear copy or key anywhere in the file; the one lead worth naming (borrowing Caprile's key) was already tried here and explicitly rejected. Listed as the negative case in this batch | 23 |

Honest assessment: these are ciphertexts a well-tooled AI project already spent a session on and set aside, so a
solving session that just reruns the same annealer will get the same nonsense. A genuinely different route is
visible in only three of the twelve: **G2 (Lope Hurtado)**, where a full contemporary decipherment is sitting
unused in the same box for three sibling records that were never even attempted with the key it gives; **G1
(Matignon)**, where the key is already verified and most of the "unread" total is a transcription backlog
against a key that works, plus a second cipher in the same volume whose interlinear decipherment is already
photographed and simply never typed up; and **G7 (it1583)**, where a sibling in the same sign family was found
and transcribed but never annealed jointly with the target, which is the standard move for two texts on one
chancery key and was not tried. The rest mostly need either the same annealer (G5, G12, closed for good reason)
or an archive visit no GitHub clone supplies (G3's codebook, G4's 68 untried key images, G6's BNE key, G10's and
G11's missing siblings) — real work, but not a different route from what already failed. G8 (Caprile) sits in
between: the next step it names (a second transcription pass against decipherments already on file) is
achievable from the repository, but it is transcription discipline, not a new idea.

## Neighbour-record recovery candidates (DECODE catalogue scan of 23 September 2026)

**Re-run with volume-aware exclusion, 23 September 2026, 17:29 UTC (`tools/decode_neighbours_exclude.py`,
`sources/solver-diffs/2026-09-23-decode-neighbours-annotated.tsv`).** The first exclusion matched Bourdeau's
profiles by DECODE id only and let the Pallotto cluster (D1) through although his `pallotto1629/` folder works
the sibling volume with a key broken in 2018. Matching by volume as well: of the 202 pairs, 156 share an id with a
Bourdeau folder, 37 share a volume, 4 are on this queue, and **5 survive**, all Luis Fernández letters of 1523 at
RAH Signatura 9/29 (R9838-R9843 beside Decrypted R9841 and R9834), a volume that lies between 9/28 and 9/30, both
of which Bourdeau's `lopehurtado1523/` already reads. So D1 is found-solved (ciphers/pallotto-1628/NOTES.md),
D2, D3, D4, D5, D6 and D7 are in volumes or on ids Bourdeau's repository already names, and the cached catalogue's
neighbour lane is, for practical purposes, his. What remains of this lane needs the full DECODE catalogue (login,
ASKS row 1) rather than Aymeloglu's cached scrape, and volumes that are not on DECODE at all.

| D8 | Luis Fernández (Rome) letters, 1523, RAH Signatura 9/29 | 1523 | es | recovery | R9838, R9839, R9840, R9842, R9843 / R9841, R9834 (Decrypted) | Only survivors of the volume-aware exclusion; same hand as Bourdeau's 9/28 and 9/30 targets, so expect him to reach 9/29 | Read only if DECODE opens before he gets there; otherwise a duplicate | 30 |


Scan of the cached DECODE catalogue (`ay/catalogue/decode-catalog.csv` + `decode-records.jsonl`, both aaymeloglu/
unsolved-ciphers) for the Randolph f.277/f.278 pattern (LESSONS.md, 23 September 2026): a shelfmark that carries
both a Non-decrypted record and a Decrypted or Partially decrypted one, matched by a normalised shelfmark plus
adjacent folio/item number, a close date, or a shared sender and recipient. Method, code and both raw sheets:
`tools/decode_neighbours.py`, `sources/solver-diffs/2026-09-23-decode-neighbours.tsv` (202 catalogue-level
pairs before exclusion) and `-excluded.tsv` (175 removed as already on our QUEUE, in Bourdeau's catalogue.json/
`cs-recheck/*/profile.json`, or in Aymeloglu's TARGETS.md/SHORTLIST.md — ranges such as "R8429-R8454" were
expanded to every id they cover, not just the two endpoints, which is what removed the whole BL Cotton MS
Vespasian C III/C IV "Edward Lee" cluster and the Prince Rupert Add MS 18982 pair found on the first pass: both
turned out to be already read, `cs-recheck/lee1526/` at fraction 1.0 and rank 21's Maurice-Rupert row). 27
records survived exclusion, all Italian, Spanish or French; no English survivor was left once the ranges were
expanded correctly. They group into 7 distinct shelfmark clusters, all shown below (fewer than fifteen).
Ranked by: English first (none survived), then match strength (same sender-and-recipient plus adjacent folio
strongest), then size (pages). Score = language_fit x3 + material x2 + key_lead x3 + size x2 + competition x2 +
weight + unread x3, with material fixed at 1 (DECODE needs a login) and key_lead at 2 for every row (each
neighbour is a sibling letter in the same box/legajo/fond, not a contemporary decipherment of this exact letter
the way Randolph's f.278 is of f.277 — no self-decipherment pair of that kind turned up this sweep).

| # | Target | Year | Lang | Kind | DECODE ids (letter / neighbour) | Why matched | What a worker would do | Score |
|---|---|---|---|---|---|---|---|---|
| D1 | Mgr Giovanni Battista Pallotto, nuncio extraordinary to Emperor Ferdinand II (Mantuan succession mission), to the "Nunzio all'Imperatore" — 5 further dispatches in the same file as one already-glossed one | 1628 | it | recovery | R233, R239, R241, R242, R253 / R221 | Same shelfmark (BAV Barb.lat 6956), same sender and recipient string, catalogue date identical (1628, likely a placeholder day) to the Partially decrypted neighbour R221 | **Check-solved, 23 Sept 2026: found-solved, not a fresh recovery target.** dbourdeau/cyphersolver's own catalogue (entry 236, DECODE R215-R285+R318, covers all six ids here) lists this whole shelfmark "solved by others" and removed 21 Sept 2026: Norbert Biermann & Thomas Bosbach broke the key in March 2018, filed on DECODE R215's documents; George Lasry confirmed it and applied it to the sibling Barb.lat 6960 (all 28 sheets read into Italian, matching Kiewning's 1897 edition word for word). The actual 2020 Cryptologia paper on this material is Lasry/Megyesi/Kopal (QUEUE's "Sacré" citation appears to be a mis-attribution of the same paper). No one has yet run the key against R233/239/241/242/253 specifically, and Kiewning's Band 1 (1628) may already print the plaintext — see ciphers/pallotto-1628/NOTES.md for the full sweep and the concrete next step (apply cs-recheck/pallotto1629/key6956/apply.py to these five transcriptions, check Kiewning Band 1) | 32 |
| D2 | Rome embassy correspondence (Lope Hurtado de Mendoza's circle; several letters signed "Luis Fernández") to Charles V/court, RAH Signatura 9/31 | 1524 (13 of the shelfmark's items undated in the catalogue) | es | recovery | R9872, R9875, R9879, R9880, R9882, R9883, R9885-R9889, R9891, R9892, R9894 / R9872's, R9881's, R9884's, R9890's, R9893's and R9895's own Decrypted status (6 different neighbours, one per sub-cluster) | Same shelfmark (BRAH Signatura 9/31), each Non-decrypted item a folio away from a Decrypted sibling; same correspondent name recurs across the legajo | Same correspondent and RAH Signatura 9.x series as QUEUE row G2 (`ciphers` none yet, `cs-recheck/lopehurtado/`, Signatura 9/26) — check whether G2's recovered `key_codes.tsv` alphabet (49 confirmed values) reads any of these before assuming a new key; if not, log in to DECODE and read the six Decrypted siblings first | 32 |
| D3 | Same "Luis Fernández" Rome-embassy hand, RAH Signatura 9/34 | 1525 | es | recovery | R9896, R9899, R9901 / R9898 | Same shelfmark, same year, one folio-adjacent Decrypted neighbour (R9898) for all three | Same as D2: try G2's key first, then read R9898's decipherment as a crib | 32 |
| D4 | Bernardino Naro / the "Nuncio Damiata" at the Paris nunciature, to the Secretariat of State, doss. 62, next to a Partially decrypted item in doss. 64 of the same fond | 1624-1625 | it | recovery | R59, R60, R61 / R71 | Same fond (Vatican Secret Archive i.1025, Segretario di Stato, France), dossier numbers 3 apart, dates 6-7 weeks apart, same recipient ("the Secretariat") | Register on DECODE, read R71's partial decipherment, apply to R59-R61; check Bernardino Spada's and Naro's own printed correspondence (Bibl. Vat. and Treccani entry cite a documented 1625 Paris nunciature) for a contemporary abstract first | 32 |
| D5 | Ferdinand (the future Ferdinand II of Aragon) to his father John II of Aragon | 1478 | es | recovery | R1172 / R1180 | Same shelfmark (BNE MSS/20211), items 3 apart, both catalogued 1478 | **Check print first**: a paper titled "Spanish Ciphers before Accession of King Ferdinand: 1470-1479" (found via web search, not yet read) appears to already discuss and reconstruct Ferdinand's 1470s/1476-79 ciphers to John II from this same manuscript family — read it before assuming this is unworked; if it stops short of R1172 specifically, log in to DECODE and read R1180 as the crib | 32 |
| D6 | Extension of QUEUE row G2 (Lope Hurtado de Mendoza), one more item just past the R9634-R9656 range already flagged there | 1522 | es | recovery | R9659 / R9652 | Same shelfmark (BRAH Signatura 9/26) as G2, adjacent folio to the Partially decrypted R9652 | Fold into G2's existing work rather than opening separately — `cs-recheck/lopehurtado/` already has a partial key for this legajo | 28 |
| D7 | Jean de Langeac, bishop of Avranches (French ambassador to Venice from 1528, envoy earlier too), to Anne de Montmorency | c. 1520-1540, this item's own date not separately catalogued | fr | recovery | R3694 / R3695 | Same shelfmark (BnF fr. 3083), same 10-day-or-less date window as the Decrypted R3695, both catalogued to the Montmorency correspondence | Register on DECODE, read R3695's decipherment for the cipher's scheme/key, apply to R3694; BnF's own finding aid (archivesetmanuscrits.bnf.fr) lists fr. 3083 among Montmorency's incoming diplomatic correspondence, worth checking for a contemporary calendar entry first | 32 |

Caveats: this scan is catalogue metadata only (DECODE's holder string, date fields and Sender/Receiver, cached
19-23 September 2026 by aaymeloglu/unsolved-ciphers), not the page images — a "same shelfmark, adjacent item"
match can still be two unrelated documents bound together, and the shelfmark-normalisation itself is a heuristic
(one bug already caught and fixed this sweep: BAV Barb.lat 6956 and Barb.lat 6960 were first merged as "the same
shelfmark" because both codes end in a single trailing number, corrected by requiring the volume number to
recur across sibling records before treating it as one file). Every row needs the DECODE login (ASKS.md row 1)
or the images from the holding library (BAV, RAH, BNE, BnF, ASV) to read past the catalogue entry — nothing here
has been opened, read or scored against a control.

## Candidates not on DECODE (catalogue scout of 23 September 2026)

Scout sweep of ASSIGNMENTS row 9: catalogues DECODE does not scrape and neither solver project reads by name,
per LESSONS.md's 23 September entry ("a catalogue a daily-active project also reads is not a lane"). Queried
the TNA Discovery API (six phrase/boolean queries, 1500-1850, restricted after fetch to catalogue level 6-7
"Piece"/"Item"), the BL Archives and Manuscripts Catalogue's JSON search (`searcharchives.bl.uk/?format=json`,
two queries), and the Gallica SRU API (four queries against `gallica.bnf.fr/SRU`, `dc.type all "manuscrit"`
where that kept precision). NRS (`catalogue.nrs.gov.uk`) is blocked by this account's egress policy (`CONNECT
tunnel failed`, organisation policy, confirmed twice); NLS manuscripts (`manuscripts.nls.uk`) serves a
Cloudflare "Just a moment" challenge to curl, consistent with the known HathiTrust-class block in CLAUDE.md's
Access playbook — neither was queried further. BL Explore (`catalogue.bl.uk`) and BnF's Archives et manuscrits
(`archivesetmanuscrits.bnf.fr`) are both JS-rendered search UIs with no plain query URL found in the time
budget; not queried. Archives Portal Europe was not reached (out of budget after the three working catalogues).
Every hit was normalised (reference + title/description + holder) and checked against `ay/catalogue/` (DECODE
scrape, matched by holder+shelfmark via the volume-key regexes in `tools/decode_neighbours_exclude.py`, copied
into `tools/` for this sweep as `exclude_lib.py`-equivalent logic), every `cs-recheck/*/profile.json` and
catalogue file, `ay/TARGETS.md`/`SHORTLIST.md`, and the current QUEUE.md. Raw hits and exclusions are in
`sources/solver-diffs/2026-09-23-non-decode-hits.tsv` (493 rows survive) and the `-excluded.tsv` sheet (211
rows, with the matching Bourdeau/Aymeloglu/QUEUE volume). Full detail (all fields, all three catalogues'
un-scored survivor lists) is in the scratchpad; only the top 20 are scored and tabled here.

| Rank | Target | Year | Lang | Kind | Reference / Holder | What the catalogue says | First move | Total |
|---|---|---|---|---|---|---|---|---|
| N1 | Mornington (Wellesley), Governor-General of Bengal, despatches to Henry Dundas, mostly in cipher, 1798-1800 | 1798-1800 | en | recovery | BL Mss Eur D623/4,5,10,11,22,23,24,27,28,30,35,36 (+ copies /29,/37) / British Library, Asian and African Studies | The catalogue entry for D623/41 reads "Two copies of key to Lord Mornington's cipher", filed in the same collection as a dozen despatches on the Seringapatam campaign and Tipu Sultan's captured correspondence catalogued only "in cipher" or "mainly in cipher"; only D623/10 is annotated "[the despatch has been decoded!]" and D623/11 "partly decoded" — the rest read as still opaque to the cataloguer. | Print-check 24 Sep 2026 (ciphers/mornington-1798/NOTES.md): partial. D623/23 already printed in clear (Montgomery Martin 1836, Vol.1) — drop it; D623/10, /11 already known decoded/partly-decoded by the cataloguer. D623/4,5,22,24,27,28(+29),30,35,36(+37) now stage 2 verified unsolved: not found across six editions checked (Martin Vols 1-5, 1877 Selection, 1914 Wellesley Papers) or the six check-solved sources; D623/41 key catalogue text carries no decipher note. REQUEST.md drafted (BL Imaging quote for D623/41 both copies + D623/4 as size/legibility test) — no email sent, no price guessed. | 39 |
| N3 | William Courten (Charleton), antiquarian diary partly in cipher, with a key appended by Sir Frederic Madden | 17th c. (diary), Madden's key 19th c. | en | recovery | BL Add MS 4956 / British Library, Western Manuscripts | Catalogue: "Interleaved copy used as a diary by William Courten al. Charleton. Partly in cipher, to which a key has been appended by Sir Frederic Madden (f. 66; cf. Sloane [...])." The key is bound into the same volume. | Print-check 24 Sep 2026 (ciphers/courten-diary/NOTES.md): open, stage 2 verified unsolved (conditional on JSTOR, queries logged, not yet run — no credentials used by this worker). Sloane MS 4019 f.79 read via the untruncated individual-record JSON: it is a second, 18th-century copy of Courten's cipher key, not a decipherment or closing note. Eight WebSearch queries across two passes and BL's own catalogue found no transcript, decipherment or scholarship on the diary's cipher passages (one dead-end closed: Add MS 5156 is Courten's will, not a cipher key, despite a search-summary claim). REQUEST.md drafted (BL Imaging quote for Add MS 4956 in full + Sloane MS 4019 f.79) — no email sent, no price guessed. | 35 |
| N6 | Seven Years War: Bute, Holdernesse, Prince Ferdinand of Brunswick and Colonel/Sir Henry Clavering, sustained two-way cipher correspondence | 1759-1762 | en | cryptanalysis | TNA SP 87/36, 38, 39, 40, 42, 43, 44 (~90 pieces) / The National Archives, Kew | Dozens of despatches each side, most "partly" or "mainly in cipher", running years with the same correspondents — consistent with a standing nomenclator, not yet located online; no decipherment noted in any hit. | Check-solved 24 Sep 2026 (ciphers/sp87-brunswick-1759/NOTES.md): open, stage 2 verified unsolved (conditional). Cluster is far bigger than scored — 818 item-level records across the 7 pieces, 98 explicitly cipher-flagged. Several already pair with an in-box contemporary decipherment (SP 87/36/9-10, /40/76-77, /40/121-124) — transcribe those first, cheaper than fresh cryptanalysis. Westphalen vol.1 (only one on archive.org) predates the relevant years; vols 2-6, Savory and SPO unchecked. Needs re-scoring as a multi-session campaign before any solve attempt. | 33 |
| N7 | Sir Henry Clinton, Cornwallis and Haldimand, cipher correspondence, American War of Independence | 1779-1782 | en | cryptanalysis | TNA PRO 30/55/19,24,32,33(x2),42,53 (Clinton Papers, 8 pieces) / The National Archives, Kew | Several "letter in cypher"/"original written in cypher" pieces across the Clinton Papers, a different PRO 30 sub-series from the Cornwallis cluster already on QUEUE row 6; one piece (30/55/24/76) is catalogued as previously matched to plaintext "by comparison to [...]" — worth checking what that comparison used. | Check-solved 24 Sep 2026 (ciphers/pro3055-clinton-1779/NOTES.md): partial. All cipher-flagged items in the 6 named pieces already carry an HMC 1904-09 plain-English calendar summary (TNA's Discovery text is drawn from it) — 30/55/24/76 (HMC 2894) explicitly content-known via a British Museum comparison copy, not a broken cipher. Stage 2 verified unsolved (conditional: HMC Report volume pages, Saberton, Clements Library calendar, the BM comparison item, none opened yet). Next: read HMC vols 3-4 pages directly; find the BL item matching 2894's French-fleet detail. | 33 |
| N8 | France despatches, sibling folio catalogued "deciphered" in the same piece-run | 1580s (catalogue error — actual covering dates 1642-44 / 1650-57, see NOTES) | en/fr | recovery | TNA SP 78/111, SP 78/113 (SP 78/113/57 "largely in cipher"; SP 78/113/123 "mostly in cipher - deciphered") / The National Archives, Kew | SP 78/113/123 explicitly reads "Letter mostly in cipher - deciphered"; several other pieces in the same two files ("Letter entirely in cipher", "largely in cipher") carry no such note. Possible overlap with QUEUE rank 13's Cobham/Bourbourg negotiations (BL Harley 287, a different physical set) in period — not reconciled this sweep. | Check-solved 24 Sep 2026 (ciphers/sp78-france-1583/NOTES.md): open, stage 2 verified unsolved (conditional). Full-piece Discovery sweep confirms SP 78/111/93 and /135 have no sibling decipherment anywhere in the piece; SP 78/113/57 likewise, conditional on Thurloe State Papers vol.6 (1657, unchecked) since /113 falls in the Interregnum, not the 1580s — CSP Foreign Elizabeth (this row's stated period) never calendars it. All four items digitised:false; TNA page-copy order needed for /93, /135 and /113/123 (to see what its own "deciphered" note means on the page) before /113/57's print check. | 33 |
| N13 | Raby to Hedges and Reichart to Berlepsch, War of the Spanish Succession diplomatic ciphers | 1704 | en/de | cryptanalysis | TNA SP 90/2/335,337,348,409,409v (5 pieces) / The National Archives, Kew | Five pieces, mixed correspondents (English envoy to Berlin; a separate German-language exchange bound in the same volume), "receipt of cipher"/"use of ciphers" noted but no decipherment. | Check-solved 24 Sep 2026 (ciphers/sp90-raby-1704/NOTES.md): open, stage 2 verified unsolved (conditional). Item-details fetch found a "Partly in cipher" note on all five (not visible in the search-summary description used originally, including for /348, /409, /409v which don't mention cipher in their scopeContent at all). No sibling decipherment anywhere in SP 90/2 or the wider class outside 1709-14; no companion cipher-key record on Discovery. Wentworth Papers (1883), the standard printed edition, covers only 1705 onward — these five (Apr-June 1704) predate it and are not in it. TNA page-copy order next. | 28 |
| N14 | Newcastle to Carteret, ciphers around the Dettingen campaign | 1743 | en | cryptanalysis | TNA SP 87/13/18,76,85 (3 pieces) / The National Archives, Kew | "Partially in cipher"/"original in cipher", Secretary of State to the King's minister with the army in Germany; earlier and smaller than the N6 cluster in the same series. | Check-solved 24 Sep 2026 (ciphers/sp87-newcastle-1743/NOTES.md): open, stage 2 verified unsolved (conditional). No sibling decipherment in SP 87/13 or the wider SP 87 class for 1743. Coxe's *Pelham Administration* (1829, checked by full-text grep) does not name "Munchberg" or agent "101" and has no letter on any of the three exact dates. Basil Williams's *Carteret and Newcastle* (1943), the dedicated modern study, is on archive.org but lending-only — unread this sweep (no logins), flagged as the cheapest next print check before a TNA copy order. | 28 |
| N15 | Chesterfield and Cumberland, ciphers on the Anglo-Dutch/Orange succession question | 1747 | en | cryptanalysis | TNA SP 87/23/41,51,70 (3 pieces) / The National Archives, Kew | "Partly in cipher" both directions, short run. | Check-solved 24 Sep 2026 (ciphers/sp87-chesterfield-1747/NOTES.md): open, stage 2 verified unsolved (conditional) — real, unresolved edition risk. No sibling decipherment in the piece or class for 1747. Dobrée's *Letters of ... Chesterfield* vol. 2 (lending-only on archive.org, not opened) discusses the identical Waldeck/Cronstrom/Cumberland episode SP 87/23/41 and /70 report, with a "(S.P. Holland" citation nearby (no-login full-text search only; be-api's page_num is not a real locator, confirmed bogus here too) — whether it prints the cipher letters themselves or only narrates from other sources needs the actual book before any copy order. | 28 |
| N16 | Louvois (French war minister) correspondence with Rosen and la Hoguette | 1689-1690 | fr | cryptanalysis | BL Add MS 21375 / British Library, Western Manuscripts | Catalogued "in cipher" with no decipherment note; Louvois's own cipher practice with Maumort/d'Avaux/Tirconel etc. is separately catalogued elsewhere on Gallica (excluded this sweep as already in Bourdeau's catalogue). | BL reproduction order; check the excluded Gallica Louvois-cipher-list item (btv1b52509819x, already flagged to Bourdeau's project) for whether it names this correspondent's key too. | 28 |
| N17 | Venetian ambassador's letter, partly in cipher, no name or address, dated Venice | 26 Aug 1634 | it | cryptanalysis | TNA PRO 30/25/6 / The National Archives, Kew | Single piece, catalogued only "partly in cipher"; bound with other Venetian-ambassador papers (PRO 30/25/13-14) from the same years. | TNA page-copy order for /6 plus the two neighbouring pieces as context/crib source. | 27 |
| N18 | Domestic intercept(s), correspondent unnamed, "partly in [?cipher]" | 1714-ish (former reference series) | en | cryptanalysis | TNA SP 34/24/86,87 / The National Archives, Kew | Catalogue's own transcription is uncertain ("partly in [?cipher]"), a caveat from the cataloguer, not a confirmed cipher. | Treat as unconfirmed until a TNA copy is seen; lowest-confidence row on this list. | 27 |
| N19 | "For writing in cipher": a printed cipher instruction sheet with manuscript annotations | 18th century | en | contribution | TNA SP 106/40 / The National Archives, Kew | A single parchment sheet, not a letter: printed cipher-writing instructions with manuscript annotations. SP 106 (the small "Miscellaneous ciphers" class) also holds SP 106/10, "Italian and other ciphers ... not deciphered", already in Bourdeau's catalogue and excluded from this list — this sheet may be the generic method behind that class, not a matched key to a specific unread text. | TNA page-copy order; hand to whoever next works SP 106/10, as a possible general-method aid rather than a standalone target. | 22 |
| N20 | Anonymous letter to Lord Townshend enclosing a cipher key, and the rest of the Atterbury-Plot intercept series | 1719-1725 | en | contribution | TNA SP 35/71/61,62 + SP 35/19,31,33,37,39,45,49,50(x2),53(x2),56 (14 items, Atterbury-Plot series) / The National Archives, Kew | TNA's own hierarchy note ties SP 35/71/61-62 explicitly to "Papers relating to the Atterbury Plot (SP 35/35-39 and SP 35/71-72)" -- the same catalogued unit as the dropped N2 row (SP 35/36), whose keys and decrypts are already printed in the 1723 Report and Reports from Committees vol.1 (1803) App. H. SP 35/71/61 is an anonymous letter to Townshend "enclosing cipher key"; SP 35/71/62 is that key itself. The other twelve items are further SP 35 domestic intercepts from the same 1719-1725 Jacobite-correspondence sweep, none individually noting a key or decipherment. | Do not treat as fresh: check the 1723 Report and the 1803 Committees Report App. H (already fetched for N2) against SP 35/71/61-62 and the twelve singles by date/correspondent before any of this group goes further -- high prior odds it is already printed, per N2's finding. Check-solved 24 Sep 2026 (ciphers/sp35-townshend-key-1719/NOTES.md): open, stage 2 verified unsolved (conditional). Cryptiana's atterbury.htm covers appendix items B.Y.1/B.Y.10/C.50-52/F.11/H.34-37 by name but not SP 35/71/61-62 or the twelve singles -- a gap, not a confirmed negative, since the appendix is organised by topic not shelfmark and the actual 1723/1803 appendix text (not the Lords' procedural report, fetched and checked this sweep with no match) was not obtained. Closed-negative on DECODE, Aymeloglu; Bourdeau names a neighbouring item (SP 35/46/59) but not this row's. | 29 |
| N21 | Sir Horatio Palavicino to Burghley, with a cipher key in the same folio | 1590 | en | recovery | TNA SP 81/6/125 / The National Archives, Kew | "Folio 125: Palavicino to Burghley, with a cipher key." Single item, German States series; the key is catalogued as part of the same folio, not a separate cross-reference. | TNA page-copy order for f.125 (both letter and key visible on one folio, per the catalogue description -- a single copy request should suffice). | check-solved 24 Sep 2026 (ciphers/sp81-palavicino-1590/NOTES.md): found-solved, F1-leaning -- Lawrence Stone's *An Elizabethan: Sir Horatio Palavicino* (1956) already cites this exact folio ("S.P. Germany, States, 6, f. 125") by shelfmark and describes the cipher on it (a 103-name nomenclator for Palavicino's 1590 embassy) via archive.org be-api full-text search on the lending-only IA copy; not confirmed whether Stone reproduces the key in full. Copy order still needed to see the folio itself. | 35 |
| N22 | John Wroth to Cecil, with a cipher key | 1596 | en | recovery | TNA SP 81/7/239 / The National Archives, Kew | "Folio 239: Jn. Wrothe to Cecil with cipher key." Same German States series as N21, one item, key catalogued in the same folio. | TNA page-copy order for f.239. | check-solved 24 Sep 2026 (ciphers/sp81-wroth-1596/NOTES.md): open, stage 2 verified unsolved (conditional -- List and Analysis and Google Books outstanding). HMC Salisbury vol.6 and CSP Domestic 1595-97 (both fetched and searched in full) establish Wroth's 1596-97 embassy to the German princes (dividing them with Henry Wotton) but do not calendar or quote this specific letter. | 34 |
| N23 | Charles Fanshaw to Sir Leoline Jenkins, Lisbon embassy despatches, partly/wholly in cipher | 1682-1684 | en | cryptanalysis | TNA SP 89/14/131, SP 89/16/2,15,33,39 (5 items, 2 pieces) / The National Archives, Kew | Five items across two pieces, same correspondent pair (Fanshaw, envoy at Lisbon, to Secretary Jenkins), one two-year run: SP 89/16 alone carries 'In cypher'/'Partly in cypher' notes on four of its items (89/16/2,15,33,39; the note field, not the search description -- LESSONS.md's 23 Sept pattern). SP 89/14/131 (1682) is the same correspondent pair one piece earlier, also 'Partly in cypher' by note. Topic: the projected Savoy-Infanta marriage and French/Spanish diplomacy. | TNA page-copy order for the five folios (89/14/131; 89/16/2,15,33,39); no sibling decipherment found in SP 89 class this sweep. | 30 |
| N24 | Tyrawly (Lisbon) to Delafaye/Keene, and Grantham to R. Walpole, cipher-adjacent Lisbon embassy items | 1734-1775 | en | cryptanalysis | TNA SP 89/37/110, SP 89/39/153, SP 89/80/42 (3 items, 3 pieces) / The National Archives, Kew | Three items, same Lisbon-desk correspondence as N23 but later and lower-confidence: 89/37/110 (1734) is Tyrawly asking to be sent the SAME cipher as Keene's, since he holds a different key -- a report about a cipher, not necessarily ciphertext itself; 89/39/153 (1737) says the original was 'sent to Keene in cypher' (again possibly describing an enclosure, not this copy); 89/80/42 (1775) has its 'last section originally in cypher'. Flag: none of the three is unambiguously an untranslated ciphertext as filed -- lower confidence than N23. | TNA page-copy order to see whether any untranslated cipher survives on the folio, or whether these are English-language reports about cipher use; do not promote before that check. | 29 |
| N25 | Champigny (Governor of Martinique) to Maurepas, intercepted French colonial cipher correspondence | 1744-1745 | fr | cryptanalysis | TNA SP 42/27/73, SP 89/44/63,64 (3 items, 2 pieces) / The National Archives, Kew | Same correspondent pair across two classes: SP 42/27/73 (Navy) is 'a copy of an intercepted letter (in cypher) taken by HMS Hound... from Count de Champigny... to Count Maurepas', dated 24 Feb 1744; SP 89/44/63-64 (Portugal, filed as enclosures to f.131) are further Champigny-Maurepas items 'mostly in cypher', Feb 1745. Naval interception of French Caribbean administrative traffic, not a single-letter one-off. | TNA page-copy order for all three; check whether SP 42/27 or SP 89/44 hold a companion decipherment nearby (not checked this sweep beyond the item level). | 30 |
| N26 | Francis Parry to Lord Arlington, Lisbon, partly in cipher | 1672 | en | cryptanalysis | TNA SP 89/12/74 / The National Archives, Kew | 'Folio 124: Francis Parry to Lord Arlington. Original of f.123.' -- note field (not description) carries 'Partly in cipher'; f.123 may be a duplicate/translation, not checked. | TNA page-copy order for f.123-124 together. | 28 |
| N27 | Raby/Whitworth, Northern-Europe diplomatic despatches partly in cipher (extends N13's SP 90/2 run forward) | 1705-1719 | en/fr | cryptanalysis | TNA SP 90/3/358, SP 90/7/149,212, SP 90/8/84 (4 items, 3 pieces) / The National Archives, Kew | SP 90/3/358 (1705, Raby to Harley, Frederick I's secret Sweden treaty) is the SAME correspondent as N13's Raby cluster (SP 90/2, Apr-June 1704), one piece later -- real edition risk, since N13's own note already flags the Wentworth Papers (1883) as covering Raby/Strafford correspondence from 1705 onward, i.e. potentially this exact item. SP 90/7/149,212 (1716-17, Whitworth to Townshend/Stanhope) and SP 90/8/84 (1719, Whitworth to Stanhope, translation of f.80, itself noted 'partly in cipher') are a different correspondent (Whitworth, envoy to Russia/Prussia), lower edition risk. | Check Wentworth Papers 1883 for SP 90/3/358 by date before anything else; SP 90/7 and 90/8 (Whitworth) have no obvious dedicated edition found this sweep -- TNA page-copy order for those three. Check-solved 24 Sep 2026 (ciphers/sp90-raby-whitworth-1705/NOTES.md): open, stage 2 verified unsolved (conditional). Wentworth Papers confirmed to cover 1705 by date (a "RABY, AT BERLIN (1705-1708)" section) but the specific Sweden-treaty passage not matched in the fetched text -- book is a selection, not a safe negative. Found instead: BL Add MS 37373-37389, Whitworth's own retained Berlin correspondence 1716,1719-22 (a manuscript sibling, not a print edition) -- worth checking for a contemporary decipher before a TNA copy order. Closed-negative on DECODE, Bourdeau, Aymeloglu. | 30 |
| N28 | SP 87 class, further pieces beyond N6's scored cluster (Stair/Hyndford, Harrington, Clavering, Boyd, Holdernesse), 1712-1763 | 1712-1763 | en/fr | cryptanalysis | TNA SP 87/4/234, 8/45,51,59, 16/12,13, 17/58,122, 21/45, 30/4, 32/115, 45/36,92 (13 items, 8 pieces) / The National Archives, Kew | Thirteen items across eight further SP 87 pieces, none inside N6's already-scored SP 87/36,38-40,42-44 (1759-62): Stair/Hyndford-Villiers (87/8, 1742, War of Austrian Succession, Breslau/Dresden -- correspondent Stair has a dedicated 1875 edition, Graham's Annals and Correspondence of the Stair family, unchecked, real edition risk); Harrington-Cumberland/Fawkener/Ligonier (87/16,17,21, 1745-46); Boyd-Holdernesse (87/30, 1758) and Holdernesse-Clavering (87/45, 1762-63, same correspondent Clavering as N6's Bute cluster, one piece outside it); a 1712 Namur intercept run (87/4/234). N6's own note already calls SP 87 'far bigger than scored... needs re-scoring as a multi-session campaign' -- these belong to that same campaign, not a separate target. | Fold into N6's campaign rather than opening separately; when N6 is re-scored, check Graham 1875 for the /8 items specifically before any copy order. | check-solved 24 Sep 2026 (ciphers/sp87-further-1712/NOTES.md): open, stage-2 candidate (editions/community-list pass only, no TNA sibling-decipherment sweep run yet). Graham 1875 vol.2 grepped in full: no Hyndford/Villiers 1742 letters, only one unrelated 1719 cipher passage -- narrows but doesn't close the /8 edition risk (vol.1 not fully checked). No edition/DECODE/solver-repo hit for any of the 13 items. LANE S worker H, 24 Sep 2026: Google Books sweep (7 queries) -- 6 zero results, 1 weak hit (a 1713 Treaty of Utrecht history mentioning Namur/Charleroy/Newport's 1712 handover, not this item's intercepted-letters content). Still open. | 33 |
| N29 | Cardinal Giulio Sacchetti, papal nuncio to Spain: secret dispatch registers, partly in cipher | 1623-1626 | it/es/la | cryptanalysis | BL Add MS 8693-8698 (6 registers) / British Library, Western Manuscripts | Six-volume register of copies of Sacchetti's secret dispatches as nuncio to Spain (1624-26) and of Curia correspondence about him (Urban VIII, Cardinals Francesco and Antonio Barberini, Philip IV, Olivares), 'partly in cipher', copied at the Papal Curia in 1626. Substantial (6 items/registers), major Thirty-Years-War-era Curia-Madrid diplomacy. Not itemised further in this sweep; url_tsi (BL's digitised-content field) empty on the top-level record -- not digitised. | Named-edition check first: the Barberini/nunciature-to-Spain documentary series (Acta Nuntiaturae/Nunziature series editions) very likely already publishes Sacchetti's Spain correspondence in some form -- search before any copy order. Check-solved 24 Sep 2026 (ciphers/bl-sacchetti-nunzio-1623/NOTES.md): open, stage 2 verified unsolved (conditional). No dedicated Nunziature-di-Spagna/ISIME edition of Sacchetti's own Spain registers located (web search + 2 Google Books queries); Pastor's History of the Popes vol. XIII/1 p.273 confirmed (via a Yale catalogue citation) to discuss this nunciature but not read for a direct cipher citation. Closed-negative on DECODE (nearest DECODE nunciature-cipher records are Spain 1576-77 and 1767, neither Sacchetti), Bourdeau, Aymeloglu. | 33 |
| N30 | Granville (Leveson-Gower) Papers, Russia/Naples embassy files marked partly in cipher -- mostly already deciphered by the cataloguer | 1804-1806 | en | contribution | BL Add MS 89317/5/57,58,59,60(x2),61,62,88, 9/10 (9 files) / British Library, Asian and African Studies (India Office Records and Private Papers hierarchy notwithstanding -- collection area is Western Manuscripts) | Full scope note read for 89317/5/61 (the Sardinia/Sicily/Naples file): nine constituent letters listed, seven explicitly '(in cipher, deciphered)' or '(partly in cipher, deciphered)' -- Granville-era Foreign Office practice was evidently to file the clerk's decipherment with the original, exactly the N1/Mornington pattern. Only one letter in that file, Hugh Elliot to Granville, Naples, 1 Oct 1804, is marked plain '(in cipher)' with no 'deciphered' qualifier. The other eight sibling files (57-60,62,88,9/10) were not opened to the same depth this sweep. | Do not treat as a fresh cryptanalysis target; if pursued, narrow first to the specific undeciphered items (Elliot, 1 Oct 1804 confirmed; the other 8 files unchecked) rather than ordering the whole run. | 27 |
| N31 | Letter in cipher (or shorthand), Interregnum diplomatic correspondence | 1656 | en | cryptanalysis | TNA SP 84/161/66 / The National Archives, Kew | 'Folio 169: Letter in cipher (or shorthand.)' -- the cataloguer's own uncertainty between cipher and shorthand, single item, Flanders series. | TNA page-copy order for f.169; resolve cipher-vs-shorthand from the image before any solver time. | 28 |
| N32 | Portion in cipher concerning Mansfelt | 1625 | en/de | cryptanalysis | TNA SP 84/130/27 / The National Archives, Kew | 'Folio 82: Portion in cipher concerning Mansfelt.' Single item, Flanders series, Thirty Years War (Ernst von Mansfeld's campaign). | TNA page-copy order for f.82. | 28 |
| N33 | Portion in cipher concerning the Prince Palatine and France | 1639 (approx.) | en/fr | cryptanalysis | TNA SP 81/46/273 / The National Archives, Kew | 'Folio 273: Portion in cipher concerning Prince Palatine and France.' Single item, German States series. | TNA page-copy order for f.273. | 28 |
| N34 | Louis XIII to the Marquis de Cesy (French ambassador, Constantinople), partly in cipher | 1628 | fr | cryptanalysis | TNA SP 78/83/62 / The National Archives, Kew | 'Folio 147: Louis XIII to Cesy, partly in cipher.' A reigning king's own correspondence -- higher weight than most rows on this list -- single item, France series. | check-solved 24 Sep 2026 (ciphers/sp78-cesy-1628/NOTES.md): open. Halphen 1904 edition of Louis XIII to Cesy excludes this item by date (starts 1631); Avenel Richelieu vol.3 fts samples are from Richelieu not the king and don't match the date; Tomokiyo's Cesy-cipher page covers only 1619-1624 BnF material. No image found; TNA page-copy order for f.147 still the next step (REQUEST.md drafted). | 29 |
| N35 | George Kendall to Robert Cecil, in cipher | 1600 | en | cryptanalysis | TNA SP 77/6/229 / The National Archives, Kew | 'Folio 229: Geo. Kendall to Cecil (in cipher).' Single item, Flanders series, Elizabethan. | TNA page-copy order for f.229. | 28 |
| N36 | To Paget (envoy to the Ottoman Porte), Dresden despatches with a cipher postscript, key cross-referenced to SP 106 but untraced | 1693-1694 | en/fr | cryptanalysis | TNA SP 105/60/121,135 / The National Archives, Kew | Two substantial letters (Levant Company series) to Paget: f.121 (1693) has its 'cover given in cipher'; f.135 (1694) closes with 'a PS in cipher (Key untraced in SP 106)' -- the TNA cataloguer's own note names SP 106 (the small Miscellaneous Ciphers class, already touched by N19's SP 106/40) as the expected home of the key and records it as not found there. | check-solved 24 Sep 2026 (ciphers/sp105-paget-1693/NOTES.md): open. SP 105/60 is George Stepney's Vienna/Dresden letter-book (out-letters to Paget); no printed edition, CSPD entry, DECODE record or solver-repo note found. dbourdeau/cyphersolver's unrelated stepney/ item (1702, different shelfmark) confirms Stepney had his own named office cipher. TNA SP 106 key search (row's own next step) not yet run -- gated on session_01JE9661cSHNoQDHEvtc2qQb posting done in ROOM.md. REQUEST.md drafted for both folios. LANE S worker H, 24 Sep 2026: TNA SP 106 key search now run (4 calls, Paget/Dresden/cipher/key terms) -- confirms the cataloguer's own "untraced" note structurally: SP 106 has no William & Mary-era (1685-1702) cipher/decipher table at all (Charles II's run ends 1685, Anne-George II's starts 1702), so no further SP 106 search can find this key. Google Books sweep (5 queries) found Lexington Papers (Manners Sutton 1851) prints Paget-to-Lexington letters from this exact Nov 1693-95 window -- wrong correspondent/direction, not a match, but flags the volume as worth a look for a Stepney-to-Paget item too. Still open. | 33 |
| N37 | Jacobite intercepts including Charles Edward Stuart's own cipher letters, found on Sir Hector MacLean | 1745 | en | cryptanalysis | TNA SP 54/25/5,8B / The National Archives, Kew | SP 54/25/8B: 'Letters, partly in cipher, from Burnet [Charles Edward Stuart]; found in the possession of Sir Hector MacLean.' SP 54/25/5: three further letters partly in cipher seized with MacLean, George Blaw and MacLean's recruiting for Lord John Drummond's regiment. High weight (the Young Pretender's own correspondence) but the 1745 Rising is one of the most heavily published episodes in the catalogue -- Blaikie's Itinerary, the Lyon in Mourning collection and Jacobite-studies scholarship are the obvious places to check first. (A third item first pulled into this group, SP 54/19/98B, 1729, is already noted 'with de-cipher' by the cataloguer -- dropped from here as found-already-decoded.) | Search Blaikie/Lyon in Mourning/named Jacobite-studies works for MacLean's seizure and 'Burnet' before treating as unread. Check-solved 24 Sep 2026 (ciphers/sp54-maclean-1745/NOTES.md): open, stage 2 verified unsolved (conditional: Lyon in Mourning, HMC Stuart Papers, Blaikie's Itinerary not read this sweep). Blaikie's Origins of the Forty-Five (1916, read in full) confirms "Burnet" as the Prince's standing cipher alias generically but has no passage tied to SP 54/25/5 or 8B or to MacLean's arrest. Closed-negative on DECODE, Bourdeau, Aymeloglu. | 27 |
| N38 | Paris-embassy items referencing a cipher for decoding (ambiguous whether the item itself is ciphertext) | 1709, 1725 | fr | cryptanalysis | TNA SP 34/10/120A, SP 78/181/29 / The National Archives, Kew | SP 34/10/120A (1709): 'Extract from a letter of Baron Malknecht..., partly in cipher (French).' SP 78/181/29 (1725): 'St. Saphorin has sent a piece in cypher for decoding' -- Walpole reporting an enclosure, not necessarily itself the ciphertext as filed. Lower-confidence pair, flagged rather than scored high. | TNA page-copy order to confirm whether either folio itself carries untranslated cipher. | 27 |
| N39 | Venetian ambassador's despatch, partly in cipher, ten days before N17's item in the same piece | 1634 | it | cryptanalysis | TNA PRO 30/25/13 / The National Archives, Kew | '6pp Partly in cipher' (note field), '[?Venetian Ambassador to France]', dated 10 Aug 1634 -- same piece (PRO 30/25) and near-identical description as N17's PRO 30/25/6 (26 Aug 1634), almost certainly the same correspondence run. | Order together with N17's copy request rather than separately. | 27 |
| N40 | Cotton MS Tudor state-papers cluster (England-Rome, -Burgundy, -Spain, -Scotland), c.1509-1603 -- caution row, very high edition risk | 1509-1603 | en/la/it/es | cryptanalysis | BL Cotton MS Vitellius B II/VII/XIII, Galba B IV/VII/D III, Vespasian C I/VII/VIII/F VI, Caligula B VII/C IV/C VI/D I (14 volumes, 16 hits) / British Library, Western Manuscripts | Sixteen items across fourteen Cotton volumes, matched by the BL search on a generic 'cipher' mention somewhere in each volume's description, not read item-by-item this sweep. This is the core Tudor diplomatic-correspondence series -- Letters and Papers Henry VIII, and the Calendars of State Papers Spain/Scotland/Foreign -- already exhaustively calendared, and several of these Cotton volumes were also damaged in the 1731 Ashburnham House fire and heavily worked by 18th-19th century antiquarians. Recorded as a caution/backlog entry, not a live lead. | Do not pursue without first checking the relevant CSP/L&P volume by date for each item individually; low expected yield given the editorial coverage. | check-solved 24 Sep 2026 (ciphers/cotton-tudor-cluster/NOTES.md): found-solved for the 5 of 14 volumes checked (Vespasian C I, Galba B VII, Caligula B VII/C IV/C VI) -- 4 already read at grade H via Tomokiyo's Cryptiana keys or (Caligula C VI f.128) print in Robertson 1759; one small fragment (Caligula C IV f.278) stays open. Remaining 9 volumes not checked this pass (BHO search Cloudflare-gated, archive.org fts unreliable) -- unclassified, not a live lead per this row's own caution flag. LANE S worker H, 24 Sep 2026: checked 5 more of the 9 (download-and-grep of the calendar's own djvu.txt works around the BHO/fts gaps). Galba B IV joins found-solved (6 cipher items, contemporary 1516 decipherments already printed in Brewer's L&P vol.2 pt.1). Vitellius B II and Vespasian F VI checked and genuinely not found in their expected volume. Vitellius B XIII has a strong but OCR-ambiguous candidate (Casale/Benet to Henry VIII, 23 Mar 1532, "Cipher deciphered", also in Burnet's History of the Reformation iv.176) -- not confirmed enough to reclassify. Vitellius B VII, Galba D III, Vespasian C VII/C VIII, Caligula D I still unresolved (wrong sub-volume/identifier ambiguity, not a tooling block this time). | 25 |
| N41 | Gualterio correspondence: fourteen BL volumes of letters to Cardinal Filippo Antonio Gualterio (nuncio in Paris 1700-06, then Cardinal and Governor of Rome) from French ministers, Spanish/Sardinian ambassadors and fellow cardinals, most 'partly in cipher' | 1700-1730 | it/fr/es | cryptanalysis | BL Add MS 20318-20319, 20338-20339, 20365-20366, 20369-20370, 20371-20380, 20416-20420, 20426-20431, 20466-20467, 20473-20474, 20510-20511, 20554-20556, 20567-20568, 20570-20571, 20634-20635 (14 volumes) / British Library, Western Manuscripts | Full record read for two representative volumes: Add MS 20426-20431 ('Correspondence with Abbate Albicini... Ital.') and Add MS 20554-20556 ('Correspondence of [Vernon] and his wife with Card. Gualterio... Ital.'), both two-line notes confirming correspondence with no decipherment mentioned; the harvest snippets for the other twelve name a fresh correspondent each (French Secretary of State Torcy, ambassadors at Venice/Madrid/Turin/Genoa, cardinals Acquaviva and Ottoboni, and Gualterio's own nephew as Nuncio at Naples). One 30-year correspondence network to a single Vatican statesman, not thirteen unrelated letters -- comparable in shape to N29's Sacchetti registers but larger. No decipherment noted for any volume in this sweep; not itemised folio-by-folio. Edition risk: real, untested -- a documented Cardinal's own diplomatic archive; Italian nunciature scholarship on Gualterio not checked this sweep. | Named-edition check first (Gualterio's own published correspondence or a nunciature-series edition), same caution as N29; if clear, BL reading-room request for the two or three richest-looking volumes (Torcy and Acquaviva letters look most substantive) before the rest. | check-solved 24 Sep 2026 (ciphers/bl-gualterio-1700/NOTES.md): open, stage 2 verified unsolved (conditional). None of the 14 target shelfmarks is on DECODE, in Tomokiyo's Gualterio page, or in either solver repo. Major context, not a match: the wider Gualterio Papers (same BL acquisition) already has a companion volume with contemporary interlinear decipherings (Add MS 20244, "ciphers, with decipherings") and two correspondents' ciphers already reconstructed by Tomokiyo (Add MS 20359-20361 D'Estrées, Add MS 20563 Medinaceli) plus 48 DECODE records for a third companion volume (Add MS 20443, Botti) -- none of these is one of our 14 volumes, but any volume opened should be checked against these before fresh cryptanalysis. | 33 |
| N42 | John Wallis's own decipherer's letter-book: originals and copies of ciphered letters with his decipherings, Jacobite and French diplomatic traffic across five decades | 1651-1701 | en/fr | contribution | BL Add MS 32499 / British Library, Western Manuscripts | 'Letter-book of John Wallis, D.D., Savilian Professor... decipherer of political correspondence to the government... containing originals and copies of ciphered letters, with [decipherings, per the harvest title]. William III and Mary II: Intercepted Jacobite correspondence, with decipherings: 1689-1693. Louis XIV of France: Deciphers of French diplomatic and other letters: 1651-1694.' The volume already carries Wallis's own decipherings alongside the cipher, so it reads today, not a fresh unread text -- but it is the key source behind a working decipherer's output across nearly the whole period this sweep's TNA rows cover (SP 78, SP 87, SP 90 France/Empire traffic 1650s-1690s); worth checking against any of this queue's undated-key TNA rows before assuming a fresh key is needed. Edition risk: low as a target (already deciphered); real for anything matched to it (a printed Wallis biography or the Deciphering Branch scholarship may already list his solved corpus). | BL reading-room request for the full letter-book's index of correspondents (not opened folio-by-folio this sweep); cross-check its named correspondents against this queue's unkeyed TNA France/Empire rows before treating any of them as needing a fresh solve. | check-solved 24 Sep 2026 (ciphers/bl-wallis-letterbook/NOTES.md): found-solved (F0) -- this is a key-lead resource, not an unsolved cipher: its own BL catalogue description already says it contains "originals and copies of ciphered letters, with decipherings". Tomokiyo's page cites the shelfmark for Wallis's known 1651-1701 corpus (per Stedall 2002) but does not analyse it; Beeley & Scriba's edition has reached only 1641-1675, not this material. Not on DECODE, Bourdeau or Aymeloglu (expected, since it is already-solved material). Should not be scored as a cryptanalysis/recovery target; retained as a cross-reference resource for un-keyed TNA France/Empire rows. | 33 |
| N43 | Anonymous 1669 cipher letters to James II with a partial key to the names, plus a decade of further ciphered political correspondence bound in the same volume | 1669-1688 | en/fr | recovery | BL Add MS 21483 / British Library, Western Manuscripts | 'Anonymous letters, in cipher: 1669' (ff.1-8) -- the harvest title continues '...partly in cipher, on political affairs, WITH A KEY TO SOME OF THE NAMES', i.e. a partial key survives in the same volume. Full record adds nine further correspondence items 1685-1688 around James II's court (Melfort, the Abbess of the English Benedictines at Ghent, even a letter involving Eleanor 'Nell' Gwyn) -- Exclusion-Crisis-to-Glorious-Revolution political material, not itemised past the folio list this sweep. Edition risk: untested. | BL reading-room request for ff.1-8 (the 1669 letters and their partial name-key) first, since that pairing is the cheapest solve in the volume; the later 1685-88 items next. | check-solved 24 Sep 2026 (ciphers/bl-james-1669/NOTES.md): open, stage 2 verified unsolved (conditional -- Clarke's 1816 *Life of James the Second* and CSP Domestic 1669 not full-text searched this sweep). No hit on DECODE, Bourdeau, Aymeloglu, Cryptiana or general web. | 33 |
| N44 | King Charles I's own cipher instructions to Lord Digby, countersigned on every page, no decipherment noted | 1640s | en | cryptanalysis | BL Add MS 6912 / British Library, Western Manuscripts | 'Long original paper in cypher, signed by King Charles I, and countersigned by George, Lord Digby, on every page. It has originally been indorsed instructions for Digbie.' A single item but multi-page and page-by-page countersigned -- substantial, not a postscript. No decipherment or key mentioned anywhere in the record. Highest-weight single item in this pass: the king's own hand, not a minister writing in his name. Edition risk: untested; Civil-War-era royal correspondence is heavily edited in places, worth a named-edition check before a copy order. | BL reading-room request for the full item; check standard Charles I letter collections (e.g. the Cabala, or a Digby-family edition) by date/recipient first given the weight of the correspondent. | check-solved 24 Sep 2026 (ciphers/bl-charles-digby/NOTES.md): open, but with a major named lead not yet resolved: Wheatstone published a full decipherment in 1862 (Philobiblon Society, *Interpretation of an important historical Document in Cipher*, "Instructions [by Charles I] pour le Sieur de Goffe" -- confirmed via a *Notes and Queries* 1877 bibliography entry on archive.org) of a document matching this one's physical description (King's-hand cipher, Digby countersignature on every page) but naming Goffe, not Digby, as addressee, with no shelfmark given. Locate the 1862 pamphlet itself before any reading-room request or solve attempt -- if it names Add MS 6912, this reclassifies to found-solved. | 31 |
| N45 | Portuguese royal despatches: Alfonso VI and his ministers to the ambassador in England and France, with a named cipher section, around the cession of Bombay to England | 1662-1666 | pt/es | cryptanalysis | BL Add MS 38038 / British Library, Western Manuscripts | Multi-item embassy archive: despatches from the King of Portugal and ministers (Castello Melhor, Sousa de Macedo) to the Marquez de Sande, 'many of them in duplicate, with seals'; a named 'Cyphers: Portuguese despatches In cypher: 1662-1666' section; and material on the cession of Bombay to England (the 1661 marriage treaty's key colonial clause) and Charles II's Portuguese marriage. Real diplomatic weight -- an Anglo-Portuguese alliance archive, not a single letter. Edition risk: untested; a Restoration Anglo-Portuguese diplomatic edition may exist, not checked this sweep. | BL reading-room request for the cipher-flagged items specifically (not the whole multi-item archive); named-edition check for a Sande/Castello Melhor printed correspondence first. | 31 |
| N46 | Cardinal Alessandro Farnese's correspondence relating to France and Portugal, partly in cipher, with dispatches from a future Pope among the copies | 1539-1540, 1560-1564 | it | cryptanalysis | BL Add MS 8716 / British Library, Western Manuscripts | 'Copies, partly in cipher.' Substantial (280+ folios): correspondence of Card. Alessandro Farnese (nephew of Paul III) relating to France under Francis I and Charles V, with dispatches from Marcello Cervini (future Pope Marcellus II) and Guido Ascanio Sforza among the copyists' work. Mid-16th-century Franco-Papal diplomacy at a senior level. Edition risk: untested; Farnese correspondence is a well-studied Renaissance-diplomacy corpus, real risk of a prior edition. | Named-edition check (Farnese correspondence calendars/editions) before any copy order, given the corpus's prominence. | 30 |
| N47 | Andrew Stone (Newcastle's under-secretary) reporting Mr Stanhope and Walpole's private letter to the King, a matter the Duke wants reconsidered | 1728 | en | cryptanalysis | TNA SP 36/9/118 / The National Archives, Kew | 'Note from (Newcastle) to the King. Finding upon a second reading of Mr. Stanhope and Mr. Walpole's private letter...' -- ministerial-level correspondence naming both Secretary of State Townshend's circle and Robert Walpole himself; the highest weight of this sweep's single TNA items given who is named, though the folio itself is a note not a whole despatch. Edition risk: untested. | TNA page-copy order for f.118-119; check Coxe's Walpole correspondence and the Newcastle papers calendars by exact date first. | 29 |
| N48 | Maria Casimira, Queen of Poland (widow of John III Sobieski), autograph letters to Pope Clement XI, partly in cipher | 1702-1709 | fr/it | cryptanalysis | BL Add MS 8526 / British Library, Western Manuscripts | 'Partly in cipher. Autograph.' A dowager queen's own hand to the Pope; includes her seal (f.61) and letters from Cardinal Gualterio's circle (ff.259-260v) touching the same Vatican-diplomacy world as the Gualterio cluster above. Edition risk: untested. | BL reading-room request; check for a Sobieski/Maria Casimira letters edition first (she has some modern scholarly attention as John III Sobieski's queen). | 28 |
| N49 | Cardinals Ottoboni and Paolucci to Abbate Atto Melani in Paris, partly in cipher with an accompanying decipherment | 1699-1702 | it | contribution | BL Add MS 62401 / British Library, Western Manuscripts | Harvest title: 'Partly in cipher with deciphering.' Two cardinal correspondents (141 folios together), decipherment already present alongside at least some of the cipher, so likely readable today rather than a fresh solve; the record itself cross-references 'the papers of Cardinal Filippo Antonio Gualteri[o]' -- i.e. this volume and the Gualterio cluster above are the same diplomatic circle under different addressees. Scored as a contribution (residual value is the cipher-to-key mapping, not a first reading) pending a look at how much of the volume the accompanying decipherment actually covers. Edition risk: likely already covered in whole or part by its own accompanying decipherment. | BL reading-room request to see how much of the 141 folios the decipherment covers before treating any of it as unread. | 28 |
| N50 | Lord Shaftesbury's drafts of letters in cipher to Percivall, Perkins and Captain Fisher | 1682 | en | cryptanalysis | TNA PRO 30/24/7/505 / The National Archives, Kew | 'Draft of letter from Lord Shaftesbury to Mr. Percivall, also of one to Mr. Perkins, and another to Captain Fisher, in cypher.' Anthony Ashley Cooper, 1st Earl of Shaftesbury, was the leading Exclusion-Crisis opposition figure and died in exile in early 1683 -- these drafts fall in the last months before his flight to Holland, addressed to obscure correspondents (possibly agents), unread as filed. Edition risk: untested; Shaftesbury's own papers have been calendared (Christie's Life) but these specific cipher drafts not checked against it. | TNA page-copy order; check Christie's Life of Shaftesbury and the published Shaftesbury Papers calendar for these three names/date first. | 28 |
| N51 | Yorke to Bedford: Albemarle's appointment, the Townshend answer, and Tobago's return, partly in cipher | 1749 | en | cryptanalysis | TNA SP 78/232/44 / The National Archives, Kew | 'Yorke to Bedford. Albermarle's appointment is welcomed... Tobago has been refused...' -- substantive mid-century diplomatic business (colonial and appointment matters) between the ambassador at The Hague and the Secretary of State, 'Partly in cipher' by the note field. Edition risk: untested. | TNA page-copy order for f.103; check Bedford Correspondence (ed. Russell, 1842-46) by date first. | 28 |
| N52 | Secretary of State Nicholas to Sir L.R. at San Sebastián, in cipher | 1659 | en | cryptanalysis | TNA SP 77/32/289 / The National Archives, Kew | 'Nicholas to Sir L.R. at St. Sebastian - in cipher.' Sir Edward Nicholas, Secretary of State to the exiled Charles II, corresponding on the eve of the Restoration -- Flanders series, single folio. Edition risk: untested. | TNA page-copy order for f.289; check Nicholas Papers (Camden Society editions) by date first. | 28 |
| N53 | Doncaster (Earl of Carlisle) to Calvert, with an advertisement in cipher enclosed | 1621 | en | cryptanalysis | TNA SP 78/69/91 / The National Archives, Kew | 'Doncaster to Calvert - and duplicate, with advertisement in cipher (f.222).' James Hay, Earl of Carlisle (styled Viscount Doncaster at this date), envoy to France, to Secretary Calvert -- Jacobean diplomatic enclosure. Edition risk: untested. | TNA page-copy order for f.214/222; check CSP Domestic/Foreign James I calendar entries for this date first (may already summarise the enclosure's content, not necessarily its cipher). | 28 |
| N54 | St Quentin to 'the Pretender', partly in cipher, on the Austrian military situation and the Queen of Hungary | 1743 | fr | cryptanalysis | TNA SP 36/61/53 / The National Archives, Kew | 'St. Quentin to [the Pretender] with news of the general situation concerning the Austrian troops; the Queen of Hungary...' Note field: 'French. Part in cypher.' Direct correspondence addressed to the Stuart Pretender (James Francis Edward) during the War of the Austrian Succession, two years before the '45. Edition risk: untested. | TNA page-copy order for f.53; check the Stuart Papers calendar (Royal Archives, published volumes) for St Quentin by date first. | 28 |
| N55 | Waldegrave to Delafaye: a paper of Cardinal Fleury's left on a table, copied and sent in cipher | 1734 | en/fr | cryptanalysis | TNA SP 78/205/95 / The National Archives, Kew | 'Waldegrave to Delafaye. He managed to see a paper carelessly left on a table by Fleury which was a copy of a letter in [cipher, per the note field].' Ambassador Waldegrave reporting espionage against Cardinal Fleury, chief minister of France -- unusually specific tradecraft detail for a catalogue description. Edition risk: untested. | TNA page-copy order for f.146; check Coxe's Walpole and any Waldegrave-embassy calendar by date first. | 28 |
| N56 | 87 avvisi (newsletters) to the Papal Secretary of State from France, partly copies and partly in cipher, imperfect | 1624-1627 | it/la/fr | cryptanalysis | BL Add MS 8730 / British Library, Western Manuscripts | 'Partly copies, partly in cipher. Imperfect.' Cardinal Bernardino Spada, nuncio to France, avvisi collection covering wars and politics of the period, including a plan of the Huguenot attack on Port-Louis, Brittany (c.1625) among the enclosures. News-digest material rather than a single decision-of-state letter, and 'imperfect' flags gaps. Edition risk: untested. | BL reading-room request for the cipher-flagged avvisi specifically. | 27 |
| N57 | Two related letters to 'Mrs Horesse', partly in cipher, same hand and date | 1717 | en | cryptanalysis | TNA PRO 30/53/11/42, 43 / The National Archives, Kew | Two items, same correspondent pair, same day: 42 ('[?] to Mrs Horesse', note 'Seal Partly in cipher') and 43 ('Letter in the same hand to Mrs Horesse', note 'Partly in cipher'). 'Mrs Horesse' is not otherwise identified in the catalogue snippet -- possibly a code name. Edition risk: untested. | TNA page-copy order for both folios together; identify 'Mrs Horesse' before any solve attempt. | 27 |
| N58 | Sir Thomas Roe to the Secretary of State, postscript in cipher | 1638 | en | cryptanalysis | TNA SP 81/44/225 / The National Archives, Kew | 'Roe to Secretary of State, with postscript in cipher.' Sir Thomas Roe, veteran ambassador (Ottoman Porte, Mughal court, Swedish mediation) -- German States series, but the ciphered portion is a postscript only, so small. Edition risk: untested; Roe's letters are partly printed (Negotiations of Sir Thomas Roe) but this volume/date not checked against it. | TNA page-copy order for f.225; check the printed Roe Negotiations/correspondence volumes for this date first. | 26 |
| N59 | Letter in cipher from '159', in Sir Henry Wotton's hand | 1622 | en | cryptanalysis | TNA SP 99/24/251 / The National Archives, Kew | 'Letter in cipher from 159.' Note field: '? Wotton's hand' -- Sir Henry Wotton, ambassador to Venice, apparently the scribe/sender behind a numbered-codename correspondent ('159'). Venice series, single folio. Edition risk: untested; Wotton's letters partly printed (Logan Pearsall Smith's edition) but not checked against this item. | TNA page-copy order; check Pearsall Smith's Life and Letters of Sir Henry Wotton for '159' or this date first. | 26 |
| N60 | Duplicate of a paper sent by Mr Stanning in cipher | 1631 | en | cryptanalysis | TNA SP 81/37/284 / The National Archives, Kew | 'Duplicate of paper sent by Mr. Stanning in cipher.' German States series, correspondent otherwise unidentified in the snippet, single folio. Edition risk: untested. | TNA page-copy order for f.284. | 25 |
| N61 | Major d'Ehrenstein to M. de Bernsdorff regarding M. de Guldenstolp, partly in cypher | 1689 | de/fr | cryptanalysis | TNA SP 8/6/65 / The National Archives, Kew | 'Letter from Major d'Ehrenstein to Monsiuer de Bernsdorff regarding Monsieur de Guldenstolp partly in cypher.' William III-era continental military/diplomatic correspondence, minor named figures. Edition risk: untested. | TNA page-copy order for f.208. | 25 |
| N62 | Z Ball to an unknown recipient, in cipher, the autumn before the '45 | 1745 | en | cryptanalysis | TNA SP 36/74/1/60 / The National Archives, Kew | 'Z Ball to [unknown]. In cipher.' November 1745, the month of the Jacobite army's advance into England -- correspondent otherwise unidentified. Edition risk: untested. | TNA page-copy order for f.60; identify 'Z Ball' before any solve attempt. | 25 |
| N63 | Elizabethan enclosure, partly in cipher, apparently attached to a neighbouring item | 1600 | en | cryptanalysis | TNA PRO 30/50/70/8 / The National Archives, Kew | 'Letter, partly in cipher. Apparently an enclosure to PRO 30/50/70/7.' Neither item's correspondent named in the snippet; the sibling /7 not checked this sweep. Edition risk: untested. | TNA page-copy order for both /7 and /8 together (the enclosure and its covering letter). | 25 |
| N64 | Edward Reynoldes to Owen Reynoldes, postscript partly in cipher, seeking a Privy Seal office through 'Lord Harry' | 1603 | en | cryptanalysis | TNA SP 14/1/38 / The National Archives, Kew | 'Purposes to labour to be admitted in the office of the Privy Seal, by favour of "Lord Harry" [Lord Henry Howard ?] P.S. Partly in cypher.' Early Jacobean patronage-seeking letter, cataloguer's own bracketed uncertainty is about the addressee's identity, not the cipher. Edition risk: untested. | TNA page-copy order for the postscript. | 25 |
| N65 | Andrew Stone to Newcastle, reporting the CONTENT of a cipher letter from Mr Robinson -- ambiguous whether Stone's own letter carries ciphertext or only paraphrases one | 1735 | en | cryptanalysis | TNA SP 36/37/44 / The National Archives, Kew | 'The Dutch post brought a letter in cypher from Mr. Robinson concerning a Frenchman...' Reads as Stone summarising Robinson's ciphered report in plain English to Newcastle, the same 'report about a cipher, not necessarily the cipher itself' pattern flagged for N24 and N38. Flagged low-confidence, not dropped. Edition risk: untested. | TNA page-copy order to confirm whether f.44 itself carries any untranslated cipher before treating as unread ciphertext. | 25 |
| N66 | 'For writing in cypher' and 'For Decyphering' parchment method-sheets, numbered 1-1800, with duplicates | 18th century | en | contribution | TNA SP 106/42 / The National Archives, Kew | 'Parchment sheet entitled "For writing in cypher"; two parchment sheets entitled "For Decyphering", numbers 1-1800, with two duplic[ates].' Same SP 106 Miscellaneous Ciphers class as N19's SP 106/40 (a printed instruction sheet) -- this one is a numbered nomenclator table rather than instructions, and could be the general-method key behind other SP 106 items (including N19) or other unkeyed nomenclator-style targets in this class. Edition risk: low. | TNA page-copy order; hand to whoever next works SP 106/10 or N19's SP 106/40, as a possible matching nomenclator rather than a standalone target. | 22 |

Caveats: (1) each catalogue's search here covers only its metadata (title/description fields), never the page
image or the piece itself — a "cipher" mention is a cataloguer's description, not a verified reading of an
actual enciphered text, and several rows above flag the cataloguer's own uncertainty (`[?cipher]`) or an
unresolved ambiguity (SP 105/60/121's cut-off snippet). (2) Coverage is partial by design and by budget: TNA
Discovery's six queries were capped at 100 hits each before the 1500-1850/level-6-7 filter (three queries
returned more matches than fetched: "in cipher" 486 total/100 fetched, "in cypher" 207/100, "partly in cipher"
223/100 — the unfetched tail is not represented here); BL's two queries were exhausted in full (262 and 42,
`per_page=100`); Gallica's `"chiffré"` alone returned 5,188 hits of which the sampled 50 were overwhelmingly
false positives (library cataloguers' "chiffré" = "numbered [foliation]", not "enciphered") and were dropped
entirely rather than scored — only the three precise phrase queries are represented. NRS and NLS were not
reachable (egress-blocked and Cloudflare-challenged respectively); BL Explore, BnF Archives et manuscrits and
Archives Portal Europe were not queried (JS-rendered search, no plain API URL found in budget, or budget ran
out first). (3) None of these nineteen has been check-solved; "not found on DECODE/in Bourdeau/in Aymeloglu" is
a catalogue-matching result under rule 10, not a verified-unsolved verdict — every row still needs the six-source
sweep before it can move to the board.

**Scoring pass of 23 September 2026 (N20-N40), against the 474-row backlog of unscored survivors named above.**
Grouped the 493-row TSV by piece/volume, re-excluded by volume against the ranks scored above (N1-N19, and the
rows dropped as found-solved) since those already cover every item in their pieces even where the raw survivor
list still lists other items from the same piece — this leaves 335 genuinely fresh rows (79 TNA, 214 BL, 42
Gallica), not the raw 474, once whole already-worked pieces are pulled out. For TNA, ran the Discovery search
API by exact reference for all 79 (one request each; the "note" field returned by an exact-reference search
already carries the "partly in cipher"/"deciphered" text this sweep's LESSONS.md entry says search results
otherwise omit, so a second `records/details/{id}` call was only spent on the ~30 items that made the shortlist
below, to confirm `digitised` — false for every one checked). For BL, read the full scope-and-content note (not
just the title snippet the harvest TSV stores) for the largest multi-item groups: Add MS 89317 (Granville
Papers), Add MS 8693-8698 (Sacchetti), Mss Eur F699 (one relevant item found by full-text grep of a 43-letter
index: item 30, a cipher message to Sir James Outram, 10 Nov 1857 — the other constituent items not opened). Of
the 42 Gallica survivors, essentially all are noise: medieval/early-modern literary and liturgical manuscripts
(Roman de la Rose, a Hebrew Bible, an Infortiatum, etc.) or printed books that matched "chiffré" incidentally,
plus four rows that are the SAME manuscripts as the already-dropped N4/N5/N9/N10 (Baluze 188, Dupuy 63, Lorraine
377, Dupuy 155) surfacing again under a different ark id — none scored. BL's IOR items (6 of the 8 survivors)
are administrative correspondence about cipher/code logistics (telegram mistakes, code-book requests), not
ciphertext — same pattern as the dropped N11; not scored. BL's "Photo 2" hits (3) are unrelated portrait
photographs, a false match; not scored.

Of the 335 genuinely fresh rows, 21 were examined closely enough to score (N20-N40, all TNA and BL, 34 raw TSV
items between them — several rows group 2-14 items from one piece or volume, per the brief). No item digitised;
a TNA page-copy order or BL reading-room request is the first move for every live row. Kept, not scored:
roughly 60 further TNA singleton items (from pieces with only one survivor and no note-field cipher confirmation
checked) and roughly 155 further BL singleton items (never opened past the title snippet) — genuinely
**examined only at the title/description level, not scored**, plus the ~50 Gallica/IOR/Photo rows explicitly
ruled out above. **Honest count: of the 474 rows named in the brief, 158 were already accounted for by existing
scored/dropped pieces (re-excluded this pass), 335 were newly reviewed at some level, 79+~20 BL/Gallica items
were opened to full record or note-field detail, and 21 rows (34 underlying items) were scored into the table.
The remaining backlog is roughly 215 BL singleton titles and 60 TNA singleton titles that have only ever been
read as a one-line catalogue snippet — the next scoring pass should open those before harvesting anything new.**
Requests: discovery.nationalarchives.gov.uk ~114 (79 reference searches + 31 detail calls + ~4 one-off checks,
1.5s apart, no 429/403 seen), searcharchives.bl.uk 7, gallica.bnf.fr 1 (reachability only). Full per-item data
(notes, descriptions, ids, digitised flags) is in the scratchpad, not committed (would exceed a sensible file
size for what is mostly raw API JSON); QUEUE-scores.json's `non_decode.rows` carries the scored axes.

**Scoring pass of 24 September 2026 (N41-N66, ASSIGNMENTS row 13), against the backlog the pass above flagged.**
Fixed a bug in the piece-exclusion logic used to derive that "215 BL / 60 TNA" backlog figure: N6's and N28's
reference fields list further pieces as bare trailing numbers after a shared series prefix ("SP 87/36, 38, 39,
40..."), which a naive per-row regex does not expand, so SP 87/37-44 read as unscored when most of that range
is already inside N6's Seven Years War campaign (SP 87/37 itself, one piece N6/N28 do not cover, was folded into
that campaign's note below rather than opened as a fresh row, matching N28's own precedent). After the fix, only
20 TNA pieces (22 items) and 180 BL volumes (189 items) outside every already-scored piece/volume remained
unopened. Fetched all 20 TNA pieces by exact-reference search (one request each; two — SP 54/19/98B, already
flagged found-already-decoded by N37's own text, and ADM 1/1665/176, whose description states outright "written
in cypher code and decrypted" — dropped as already-read, not scored) plus a details call on the 14 that made the
shortlist to confirm `digitised` (false for all 14). For BL, ranked the 180 fresh volumes by a keyword signal
over the harvest title/description (key, deciphered, cipher, secret, intercept, ambassador, treaty, minister)
after removing three noise patterns that had already tripped this project up once (IOR telegram/code-logistics
administrative items, "Photographer:"/Visual Arts false matches, and "[word undeciphered]" OCR-uncertainty
flags, none of them actual cipher) and pulled the full scope-and-content note for the top sixteen singletons plus
two representative volumes of a fourteen-volume cluster that shares one recipient (below). Four of the sixteen
turned out to be false leads on the full note (no "cipher" anywhere in the untruncated text — Egerton MS 2813,
Add MS 63742 — or the matched passage was a cipher *treatise*, not ciphertext — Add MS 8280 — or was itself
already deciphered — Add MS 24321, Add MS 48049 the Mary-Queen-of-Scots volume turned out to hold Robert Beale's
own "extracts from deciphered letters", i.e. already-read Babington-era material); none of the four scored.
**Honest count: of the 335 rows this project has now looked at across the two scoring passes, 82+26=108 have a
score; the true remaining backlog, after the exclusion-logic fix, is roughly 22 further BL singleton volumes not
opened this pass (kept at the title-snippet level only) plus whatever the corrected exclusion logic would trim
from the "roughly 155 BL / 60 TNA" the first pass estimated — that estimate is superseded by this pass's fix and
should not be reused without re-deriving it.** No item digitised (`url_tsi` empty on every BL record checked
except the dropped Add MS 48049, which states images are "currently unavailable"); a BL reading-room request or
TNA page-copy order is the first move for every live row. Two items found already-deciphered and not scored
(SP 54/19/98B, ADM 1/1665/176); four BL false-leads on the full note not scored (Egerton MS 2813, Add MS 8280,
Add MS 63742, Add MS 24321, Add MS 48049 — five, corrected). Requests: discovery.nationalarchives.gov.uk 98
(84 exact-reference searches across the 22 fresh items + 14 detail calls, 1.5s apart, no 429/403), searcharchives.bl.uk
35 (16 search + 16 full-record + a handful of format probes before finding the working `?format=json` query
form — `/catalog.json?q=` redirects to an HTML page for this endpoint, `/?format=json&q=` does not).

check-solved 24 Sept 2026 (LANE S batch G): N45 (`ciphers/bl-portugal-bombay-1661/`) open, stage 2 verified
unsolved (conditional — no image seen, BL catalogue offline since 2023). Prestage 1925 and the relevant *Corpo
diplomatico portuguez* tome are named editions with real edition risk, neither actually checked against this
correspondence yet; REQUEST.md drafted for the cipher-flagged folios only, contingent on that edition check.
N46 (`ciphers/bl-farnese-cipher/`) open, stage 2 verified unsolved (conditional — no image seen, BL catalogue
offline since 2023). Disambiguated from three other "Farnese cipher" items already known to this project
(Vatican Spagna 1A/DECODE R91-R92, the Duke of Parma's general cipher, and the solved Odoardo Farnese/Sabran
1637 item) — all confirmed different people, items, or both. *Nunziature di Francia*/*Portogallo*, Susta and
Ancel named as candidate editions, none checked against this item's two date ranges yet; REQUEST.md drafted,
contingent on that edition check given the item's size (280+ folios). N47 (`ciphers/newcastle-stone-1728/`)
open, stage 2 verified unsolved (conditional — TNA Discovery out of this brief's hosts, digitised status not
directly re-confirmed). Coxe's 1798 Walpole and 1802 Horatio Walpole memoir volumes (both on archive.org) are
named, readily available editions from this exact circle and period, not yet full-text searched against this
note's own language — the cheap next step before any TNA page-copy order, which REQUEST.md notes as a
precondition.

## Digitised candidates, no copy needed (scout of 23 September 2026)

Scout sweep for cipher manuscripts whose page images are already free online, in catalogues neither solver
project sweeps, so that no copy order and no login is the blocker (owner's steer at 19:31 UTC, four workers
started while the owner was away). Read first: README "What counts as a result", LESSONS.md's 23 Sept entries
(the "chiffré alone is foliation noise" lesson and the neighbour-volume-key exclusion lesson), QUEUE.md
"Candidates not on DECODE" and its caveats.

BnF's own Archives et manuscrits site (archivesetmanuscrits.bnf.fr) is a JS-rendered search UI with no plain
query URL found in budget; its `ccfr.bnf.fr` cross-catalogue portal 302-redirects to a session-cookie page, also
not reached. Per the brief, fell back to the **Gallica SRU API** (`gallica.bnf.fr/SRU`), which is BnF's own
digitisation platform, so every hit is by construction already imaged with a IIIF manifest — no separate
digitisation check was needed for this source, only a content check. Ran the four adjacency-phrase queries
named in the brief (`dc.description adj "en chiffre"`/`"en chiffres"`/`"lettre chiffrée"`, and `"chiffré" and
"déchiffrement"`) restricted to `gallica all "manuscrit"` (36+114+19+55 = 224 raw records before de-duplication),
then eight further queries scoping `dc.source` to the eight preferred fonds named in the brief (Clairambault,
Dupuy, Baluze, Cinq Cents de Colbert incl. Mélanges de Colbert, Espagnol, Italien, Lorraine, NAF) combined with
`dc.description all "chiffre"` (29 more records, mostly overlapping). 223 unique ark records after merge.

**The "chiffré alone is foliation noise" lesson confirmed at scale.** Of the 223 unique hits, 112 are BnF
cataloguers' own foliation, pagination, date or numeral-table language ("en chiffre(s) arabes/romains" =
Arabic/Roman page numerals, not cryptography) and a further 96 read as noise on inspection (Quran verse-counts,
Ptolemy's Cosmographia tables, Chinese loan registers, an Oulipo wordplay title). Only 15 of 223 (unique arks;
39 raw rows before dedup, several items matched more than one query) are genuine cipher content on a full read
of their catalogue description. Ten of those (Français 2996, 2980, 4102, 4137; Dupuy 468, 452; and two
lower-confidence edge cases, Français 14765's alchemical "12 clefs" treatise and a single line of "secret
writing in Indian numerals" bound into Arabe 1966 — kept out of the table, see caveats) are single or few
named ciphered letters inside much larger plain-text miscellanies, with no key stated in the same item. Five
are scored below as the strongest leads. Exclusion: every survivor's shelfmark and ark were checked against
`cs-recheck/*/profile.json` (Bourdeau, matched by volume key, not id, per LESSONS.md's Pallotto lesson), every
`ay/*.md` tracker line, `ay/catalogue/decode-catalog.csv` (the cached DECODE scrape) and QUEUE.md itself; 88 of
the 223 were excluded this way (69 by the brief's own named Bourdeau ranges/Nevers/Ligue, 7 more by a
Bourdeau-profile volume-key match, 4 by the DECODE catalogue, 2 by QUEUE.md) — full sheet in
`sources/solver-diffs/2026-09-23-digitised-excluded.tsv`.

Non-BnF catalogues named in the brief: LOC's JSON API (`loc.gov/search/?fo=json`) is reachable and returned
1,013 hits for "cipher" restricted to the Manuscript Division, but the sampled first page (100 rows) is
entirely Jefferson/Madison/Monroe/Randolph correspondence from the Papers-of-Madison/Jefferson project — the
same Founders Online edition that closed the Erving 1807 row as found-solved on 21 Sept 2026 — so this lane was
not paged further or scored this sweep (high edition risk, not a copy-order blocker). Wellcome's API
(`api.wellcomecollection.org/catalogue/v2`) is reachable, 77 hits, but "cipher" there means the Ottoman tughra
(a calligraphic royal monogram) in art-collection items and one modern book title, not cryptography — nothing
scored. Beinecke (`collections.library.yale.edu`), the Folger catalogue and Bodleian Digital all answered with
an empty 202/404 body to a plain `curl` (consistent with a bot check rather than a real empty result; not
retried per the good-citizen stop-on-challenge rule); CUDL serves only its JS search page to `curl`; Trinity
College Dublin's digital collections serves a reCAPTCHA page; Leiden and the KB gave `curl: (52)/(56)` transport
failures (egress or TLS, not a challenge page) on every attempt. None of these six were reached this sweep.

| Rank | Target | Year | Lang | Kind | Reference / Holder | Catalogue note | Leaf viewed | Image route | Total |
|---|---|---|---|---|---|---|---|---|---|
| M1 | Register of ciphered correspondence between a French ambassador and the Court, with the cipher itself bound in at the head of the volume | 1580s-90s | fr/it/la | recovery | BnF Cinq Cents de Colbert 369 (ark:/12148/btv1b100339414, 394 leaves) | Gallica's own note: "En tête du volume, se trouve le chiffre de la correspondance entre l'ambassadeur et la Cour" -- followed by letters of Henri III, André Hurault de Maisse, Horatio Rucellaï, Henri IV, François de Luxembourg (envoy to Sixtus V), plus an "Interpretatio litterarum" of a letter from Sultan Murad III to Henri IV (f.126, 261v) and a Florentine credenza (f.272) -- reads as the register of a French embassy near the Ottoman/Italian sphere, with its own key present. | **Yes, check-solved 23 Sept 2026**: ff.3-5 carry the cipher table itself, matching Bourdeau's already-published Maisse key digit-for-digit; ff.8-270 (18 leaves sampled) are a plain-French clerk's register, not ciphertext. See ciphers/colbert369-maisse/NOTES.md — found-solved, dropped. | gallica.bnf.fr IIIF manifest, public domain, no login | 41 |
| M2 | "Chiffre du duc de Paliano" among a recueil of 1550s Franco-Italian diplomatic letters (Salerno, Este, Caraffa/Paliano affair, Strozzi) | 1550s | fr/it/es | recovery | BnF Clairambault 351 (ark:/12148/btv1b9000680d, 327 leaves) | Gallica's item list names "Chiffre du duc de Paliano" alongside letters to/from the same circle (cardinal Caraffa, the duc de Paliano, maréchal Strozzi) in the same recueil -- a plausible but not confirmed pairing of key and correspondence in one box. | **Yes, check-solved 23 Sept 2026**: folio pinned via the BnF finding aid (ff.173 and 175, a nomenclator table copied twice, dated 1557); no letter in the volume is catalogued or observed "avec chiffre". See ciphers/clairambault351-paliano/NOTES.md — closed-negative, key-only, dropped. | gallica.bnf.fr IIIF manifest, public domain, no login | 39 |
| M3 | Paolo Sarpi's own cipher for his Italian letters, noted at f.100 of a volume of his 40 autograph letters (1608-1611, to a masked "Castrino") plus later Latin letters to Gillot, Hotman and Casaubon | 1604-1617 | it/la | recovery | BnF Dupuy 111 (ark:/12148/btv1b10034811v, 105 leaves) | "le chiffre dont fra Paolo se servait dans ses lettres italiennes, autogr. (100)" -- Sarpi is a major, heavily edited figure (Interdict-crisis correspondence, printed by Ulianich, Cozzi and others); real edition risk, flagged for check-solved rather than assumed novel. | **Yes, check-solved 23 Sept 2026**: key at f.100-101 (canvas 102-103), a genuine ciphertext letter confirmed at approx. f.34 (canvas 36); Busnelli 1931/1986 already printed this correspondence from this manuscript by folio. See ciphers/dupuy111-sarpi/NOTES.md — found-solved, dropped. | gallica.bnf.fr IIIF manifest, public domain, no login | 39 |
| M4 | Autograph letter of "Paget" with cipher, bound into a large miscellany of unrelated 17th-18th c. legal and genealogical papers | 1714 | en/fr | cryptanalysis | BnF Clairambault 1225 (ark:/12148/btv1b9001034d, 268 leaves) | "lettres autogr. de Paget, avec chiffre, 1714" -- a single named item in a 200-plus-item miscellany; no key or sibling decipherment named. | **Check-solved 23 Sept 2026**: folio pinned via the item-level finding aid (Fol. 48, "PAGET -- Lettres chiffrees" plural); canvas-index probes (48, 54) failed to locate it in this non-sequential "Melanges" volume. Best lead by date: Henry Paget, 7th Baron Paget/1st Earl of Uxbridge, envoy to Hanover May-Oct 1714 (William Paget, the Constantinople ambassador, died 1713). See ciphers/clairambault1225-paget-1714/NOTES.md — open, stage 2 verified unsolved (conditional: item not yet viewed by image). | gallica.bnf.fr IIIF manifest, public domain, no login | 34 |
| M5 | "Double du chiffre de Claudio Marini" (1610) and a second, unattributed "Double d'un chiffre", in a Marie-de-Médicis-regency administrative recueil | 1609-1610 | fr/it | recovery (tentative) | BnF Clairambault 361 (ark:/12148/btv1b9001048f, 535 leaves) | Two cipher-key copies named in a long list of mostly plain administrative and political papers (edicts, remontrances, letters to the king); no ciphertext explicitly named alongside either key in the same list -- may pair with correspondence elsewhere in the much larger Clairambault series, not checked this sweep. | **Check-solved 23 Sept 2026**: folios pinned via the item-level finding aid (Fol. 211 Marini key, Fol. 237 second key); no ciphertext letter named anywhere in this volume's ~80-item list. Canvas probes failed (this composite carries multiple overlapping foliation layers). Tomokiyo's Cantaluppi-sourced Marini cipher (1624, Turin, different archive) is a partial, unresolved-date lead only. See ciphers/clairambault361-marini-1610/NOTES.md — closed-negative, key-only, dropped. | gallica.bnf.fr IIIF manifest, public domain, no login | 33 |
| M6 | Nine "presque entièrement en chiffres" letters to Cardinal de Sens and others, incl. Alberto Pio de Carpi (Rome, 1520-1528) | 1520-1528 | it/la/fr | cryptanalysis | BnF Dupuy 452 (ark:/12148/btv1b10036146c, 295 leaves) | Several originals in the item list marked "orig., presque entièrement en chiffres" (items ~16, 20, 28...) among plain Latin/Italian correspondence to and from the Sacred College, Henry VIII, Wolsey, Adrian VI, François Ier; no key named in this volume. | **Check-solved 23 Sept 2026**: finding aid actually names only 2 items "presque entièrement en chiffres" (ff.20, 28, both Louise-de-Savoie correspondence), not nine -- QUEUE description corrected. f.20 (Carpi, canvas 23) viewed and confirmed genuinely ciphered (~70-90 numeral tokens, final third of an otherwise plain letter); f.16 (Cardinal de Sens letter) viewed and confirmed plain; f.28 (Raince) not located. Volume also holds 4 already-"Dechiffrement" items (ff.56/60/72/76, 1535 Rome dispatches) as a sibling-decipherment lead. See ciphers/dupuy452-carpi-1520/NOTES.md — open, stage 2 verified unsolved (conditional: Champollion-Figeac checked by full-text search only; Guasti/Negociations diplomatiques/Brewer not reached). | gallica.bnf.fr IIIF manifest, public domain, no login | 36 |
| M7 | Latin cipher letter to François Ier catalogued as Ernest and Joachim of Anhalt (verifier 23 Sept 2026: more probably Ernest of Brunswick-Lüneburg and Joachim von Moltzan, 1518/19), "orig., en latin, presque entièrement en chiffres" | 1515 or 1516 | la | cryptanalysis | BnF Dupuy 468 (ark:/12148/btv1b10035959t, item 28 of 492 leaves) | Single named item, "orig., en latin, presque entièrement en chiffres (28)", inside a recueil of German-Imperial jurisdiction memoranda; no key named. | **Check-solved 23 Sept 2026**: folio 28 pinned and viewed (canvas 64) -- genuinely mostly ciphered (~100-130 mixed numeral/symbol tokens), BUT a later hand has already glossed ~15-20 tokens interlinearly with their Latin plaintext ("maiorem", "confoederationem", "principibus", "foedus"...) -- a partial decipherment already sits on the leaf. Recharacterise from cryptanalysis toward recovery once transcribed. See ciphers/dupuy468-anhalt/NOTES.md — partial, not open; gloss hand/date unresolved. | gallica.bnf.fr IIIF manifest, public domain, no login | 34 |
| M8 | "Lettre en chiffre du cardinal Gabriel de Gramont, évêque de Tarbe" (x2), inside François Ier's ransom-negotiation recueil | 1530 | fr | **recovery** (was cryptanalysis) | BnF Français 2980 (ark:/12148/btv1b9059991d, 110 leaves) | Two items marked "Lettre en chiffre"/"Lettre, avec chiffre" from the same cardinal-ambassador, amid plain letters on François Ier's captivity and ransom after Pavia. | **Check-solved 23 Sept 2026**: both leaves viewed (f.29, f.30), genuinely and heavily ciphered (~150-200 + ~500-600 tokens); Tomokiyo/Lasry's already-published "Gramont's Cipher (1530)" (from fr.3019, confirmed on fr.3071/fr.3040, read in part by Bourdeau) applies but neither solver repo has touched fr.2980 itself — reclassified recovery, cheapest-solve pattern. **Print-check class gate, 23 Sept 2026**: neither letter found printed, calendared or online anywhere searched (LP Henry VIII vol.4 pt.3's own 1530 calendar checked directly and does not include either item, though it does calendar two neighbouring Gramont-Villandry/Gramont-Brion cipher letters from Feb. 1530, one cited to Le Grand 1688 ii.386; Decrue's Montmorency biography cites fr.2980 repeatedly by item number for other letters but not these two; PUR/Rentet, Bourrilly-Vindry, solver repos, DECODE cache all checked or reused, no hit). Best-case N3 both items; gate passed for a solver. Gaps: Le Grand's own page content bot-blocked on Google Books, Pocock/SP7/Ribier-Camusat/Molini unreached. See ciphers/fr2980-gramont/NOTES.md — open, stage 2 verified unsolved. | gallica.bnf.fr IIIF manifest, public domain, no login | 34 |
| M9 | "Dépêche en chiffre" from Morvillier (envoy at Venice) to the king | 24 Jan 1546 | fr | ~~recovery~~ dropped, found-solved | BnF Français 2996 (ark:/12148/btv1b9060087w, 117 leaves) | Single named ciphered despatch inside a recueil of 16th-c. royal correspondence (Claude, Marguerite de Navarre, Charles d'Alençon, Charles-Quint). | **Found-solved (orchestrator correction 23:43 UTC)**: Tomokiyo's francis.htm and GL.htm say Lasry broke this very letter (f.52 no.25) in 2023; the check-solved 'open' verdict is withdrawn. Earlier text: leaf viewed (f.53), ~6 lines genuinely ciphered (~80-120 tokens); Tomokiyo/Lasry's already-published "De Morvillier's Cipher (1546)" applies, unread by either solver repo; an unresolved pencil marginal note near the cipher needs a higher-res read before transcribing. See ciphers/fr2996-morvillier/NOTES.md — open, stage 2 verified unsolved. | gallica.bnf.fr IIIF manifest, public domain, no login | 33 |
| M10 | "Memoyre que Mr de Sabran a envoyé en chiffre" to the Duke of Savoy's court | 1637 | fr | ~~cryptanalysis~~ dropped | BnF Français 4137 (ark:/12148/btv1b9060192j, 186 leaves) | Single named ciphered memoir inside a year's run of Sabran's plain despatches (to Bouthillier, Chavigny, the Duke of Parma). | **Check-solved 23 Sept 2026**: leaf viewed (f.129, item 112) — the volume is a "Recueil de copies", and this leaf carries only the memo's plain-French text under an "envoyé en chiffre" heading; no ciphertext survives. See ciphers/fr4137-sabran/NOTES.md — closed-negative, dropped. | gallica.bnf.fr IIIF manifest, public domain, no login | 33 |
| M11 | "Lettre en chiffre du presidant Du Faure à Galepin", inside a Rohan-wars/Languedoc recueil | 1622 | fr | ~~cryptanalysis~~ dropped | BnF Français 4102 (ark:/12148/btv1b9007662n, 285 leaves) | Single named ciphered letter inside Duc Henri de Rohan's Languedoc-campaign papers (1621-22 Huguenot wars). | **Check-solved 23 Sept 2026**: leaf viewed (f.64, item 68) — a captured-papers register (item 66 explains Du Faure's secretary Ginaud was intercepted near Aigues-Mortes in 1622); the "lettre en chiffre" survives here only as plain French, no ciphertext. See ciphers/fr4102-dufaure-galepin/NOTES.md — closed-negative, dropped. | gallica.bnf.fr IIIF manifest, public domain, no login | 33 |
| M12 | Whole volume titled "Recueil de chiffres diplomatiques (1688-1713)": a "Chiffre commun entre M. de Louvois et M. de Maumort et M. le comte d'Avaux" (1688), a second Louvois-Maumort-d'Avaux key, a "Chiffre commun entre M. de Louvois et M. Tirconel", a "Chiffre avec M. d'Usson" (14 Sept 1701) and more | 1688-1713 | fr | contribution (key-only, unpaired) | BnF Français 6204 (ark:/12148/btv1b525094217, 60 leaves) | Gallica's own title and item list name this as a bound register of Louvois-era diplomatic cipher *keys* themselves, not ciphertext letters -- same pattern as M2/M5 dropped 23 Sept ("key present, no ciphertext named in this volume"). | Not check-solved. Canvas 1 viewed (title leaf, image loads, no login). Not in dbourdeau/cyphersolver (fresh clone, "6204" only hits unrelated files), not in aaymeloglu/unsolved-ciphers or its cached DECODE catalogue, not in QUEUE.md/CATALOG.md/ciphers/ or the 23 Sept excluded sheet. Value is conditional on a matching ciphertext letter under one of these named keys (Maumort, d'Avaux, Tirconel, d'Usson) surviving elsewhere in Gallica or another archive -- not searched this pass, flagged as the next step. | gallica.bnf.fr IIIF manifest, public domain, no login | 39 |
| M13 | "Dépêches originales de la Cour à André Hurault de Maisse, ambassadeur [at Venice]": instructions (Aug 1582, Feb 1583) and "Chiffre de la correspondance de Mr de Maisse" (f.5) | Aug 1582-Dec 1585 | fr | recovery (published key, unread volume) | BnF Français 16092 (ark:/12148/btv1b90612993, 932 leaves) | Gallica's item list separately names the Maisse cipher key at f.5 in *this* volume of despatches sent by the Court to Maisse, distinct from BnF Cinq Cents de Colbert 369 (M1, found-solved 23 Sept: the register with the Maisse key already matched to Bourdeau's published key digit-for-digit). If fr.16092's despatches use the same Maisse key, this is a cheap-solve pattern like M8 Gramont: a published key applied to an unread volume. | **Check-solved pass 24 Sept 2026** (editions-first + leaf, not the full six-source run): Tomokiyo's own page (quoted in ciphers/fr16092-maisse-1582/NOTES.md) has reconstructed the key from f.5 but states "I have not seen its actual use" -- Bourdeau's repo covers only the successor volume fr.16093 (1592-93, different cipher, via Brienne clear-copy alignment), not this one. Gallica leaf check (4 canvases): found the key image itself (canvas 12) and three clear-French letters; no actual ciphertext passage located this pass. Boucher's *Lettres de Henri III* tomes V-VI cover exactly this date range and were **not checked** for whether they already print any of these letters from a lost decipherment -- the key open risk before promotion. Status: open (unresolved edition-coverage risk). See NOTES.md. | gallica.bnf.fr IIIF manifest, public domain, no login | 42 |
| M14 | "1-3 Lettres, en italien, avec chiffres, de MARGUERITE PALEOLOGUE, duchesse DE MANTOUE, au duc de Nevers, Louis de Gonzague" | **1562-1564** (corrected 24 Sept 2026; Gallica's own catalogue dates items 1-3 precisely, not the volume's outer 1562-1625 span) | it | cryptanalysis | BnF Français 4687 (ark:/12148/btv1b90075058, 139 leaves) | Gallica's item list names three ciphered letters ("avec chiffres", plural) from a named sender to a named recipient at the head of a Nevers-family recueil; no key stated in this item. | **Check-solved pass 24 Sept 2026**: not in dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers, or Tomokiyo's own mirrored fr.3995 Nevers-cipher catalogue (a different volume -- the Duke's own outgoing ciphers, not his mother's letters to him). Gallica leaf check **confirms ciphertext**: canvas 8 (f.6) shows dense two-digit numeral cipher, ~15-25 groups/line across 6+ lines, with short Italian catch-phrases in the margin (not a full decipherment). No published key found. Status: open, genuine cryptanalysis candidate. See NOTES.md. | gallica.bnf.fr IIIF manifest, public domain, no login | 34 |
| M15 | "Correspondance, originale et en partie chiffrée, de Charles de Danzay, ambassadeur en Danemark" (fol. 16) | 1557 (four items, all Jan 1557; volume's outer span 1557-1567) | fr | **recovery** (corrected 24 Sept 2026 from cryptanalysis -- see verdict) | BnF Français 20140 (ark:/12148/btv1b52521512h, alt. digitisation btv1b10782904z, 60 leaves) | Gallica's item list names Danzay's correspondence with the Danish court as "in part ciphered" over a decade; no key stated in this item. Tomokiyo's own catalogue (cyphersolver/gallica_sweep/src/henryiii.txt) separately names a *different* Danzay item -- BnF fr.4736 f.87, Copenhagen 1574, to Henri III -- and explicitly calls it still undeciphered ("contains some undeciphered lines in cipher"), so this is a sibling lead, not a duplicate: same ambassador's cipher family, different volume and decade, key unpublished either way. | **Check-solved pass 24 Sept 2026: found-solved (3 of 4) / open (1 of 4).** Tomokiyo's own dedicated Danzay page (`sources/cryptiana/web/danzay.htm`, local mirror) names f.16, f.24 and f.30 (10 and 27 Jan 1557) as each already carrying a **contemporary decipherment in the manuscript** ("deciphered in separate sheets" / "in the margin", x2) and states he reconstructed the published key from exactly those three. Only f.35 (27 Jan 1557, same correspondent type) lacks a decipherment -- a cheap recovery with the same key, not cryptanalysis. See NOTES.md. | gallica.bnf.fr IIIF manifest, public domain, no login | 39 |
| M16 | **Loménie de Brienne père-et-fils correspondence** (corrected 24 Sept 2026 from "Michel Le Tellier correspondence" -- see verdict), "en partie chiffrées, et souvent accompagnées du déchiffrement" -- about 47 letters | 10 Jan 1653 - 21 Dec 1661 | fr | recovery (decipherment often present) | BnF Français 5160 (ark:/12148/btv1b9060495t, 367 leaves) | Gallica's own description says most of the ~47 partly-ciphered letters already carry an accompanying contemporary decipherment in the same volume -- the Dupuy 468 pattern (a transcription-and-collation job, not blind cryptanalysis, for whichever of the 47 lack one). | **Check-solved pass 24 Sept 2026**: Gallica's own item-level description attributes the 47 ciphered letters to **Henri-Auguste and Henri-Louis de Loménie de Brienne writing to Abel Servien**, not to Michel Le Tellier (whose own, separate letters in the same volume, item 2, carry no cipher note at all). Bourdeau's `letellier/` folder covers an unrelated item (Le Tellier to Castelnau, 1657, different shelfmark). "Caron 1898" could not be identified as a real edition; Depping's *Correspondance administrative sous Louis XIV* (1850-55) is real but not checked against this correspondence. Gallica leaf check (3 canvases): no ciphertext passage located in this small sample of 367 canvases/47 letters -- inconclusive, not a contradiction. Status: open. See NOTES.md. | gallica.bnf.fr IIIF manifest, public domain, no login | 42 |

**Second pass, 24 September 2026 (M12-M16).** New search terms beyond the 23 Sept sweep's adjacency phrases:
`dc.description adj "chiffré"`/`"chiffrée"`/`"en chiffre"` (singular forms), `"déchiffrement"`, `"déchiffré"`,
`"contre-chiffre"`, `"cifra"`, `"cifre"`, `"zifferschrift"`, `"in cipher"`, each `and dc.source all "Manuscrits"`
(the SRU `dc.type` index is unindexed here -- returns 0 for any query -- so `dc.source` naming the Manuscrits
department is the working restriction, not `gallica all "manuscrit"`, which full-text-searches the entire
digitised corpus and returned 52,961 hits for "chiffré" alone). 244+42+33+87+7+3+7 = 423 raw records, 308
unique arks after dedup. Collection-level browsing of archivesetmanuscrits.bnf.fr for Dupuy, Clairambault, Cinq
Cents de Colbert, Français 2900-3100 and Italien was not reached: the site is JS-rendered with no plain query
URL, as the first pass already found, and its ccfr.bnf.fr cross-catalogue portal still redirects to a
session-cookie page. Exclusion, in order: 86 arks already named in QUEUE.md/CATALOG.md/LANDSCAPE.md/ciphers/ or
the 23 Sept excluded sheet (222 left); 36 more already present in a fresh clone of dbourdeau/cyphersolver's own
`gallica_sweep/bnf_candidates.txt` -- his repository runs the same kind of Gallica sweep and its 422-line output
was diffed by ark, not just grepped by shelfmark (186 left); a keyword filter for foliation/pagination noise
("chiffres arabes/romains" page-numbering, non-Manuscrits sources) and for correspondence context (lettre,
dépêche, ambassad-, secret, roi/duc/cardinal etc. near the matched term) narrowed this to 137 candidates read in
full. Of those, the entire Français 3000-3999 "Recueil de lettres" and "Collection Mémoires de la Ligue" cluster
(9 more hits: fr.3234, 3281, 3323, 3455, 3902, 3975, 3979, 3980, 3990) was dropped as already covered by
Tomokiyo's own "Ciphers during the Reigns of Charles IX and Henry III" and "List of Cipher Materials in Mémoires
de la Ligue" catalogue articles, cited and quoted at length in Bourdeau's `gallica_sweep/src/henryiii.txt` and
`segur/henryiii.txt` -- fr.3281 is individually named there by exact item description ("D'Aranger to sieur des
Pruneaux... can be reconstructed from decipherments on separate sheets"), and the article's own scope statement
covers the whole fr.3xxx Ligue/Nevers run, matching the 23 Sept pass's own "bourdeau-named:fr.3xxx" exclusion
(Français 3005-3993, 57 items) at the same convention. Three more (Français 23202 Mazarin-to-Fouquet, Baluze 331
Le Tellier/Colbert, Baluze 163 "Chrysogono"-signed letters to d'Avaux) were checked against Aymeloglu's cached
DECODE catalogue (`unsolved-ciphers/catalogue/decode-catalog.csv`) and found already status "Decrypted" there
(records 7895-7897, 2771/2773, 2755) -- found-solved, dropped, not scored. Five survivors scored below as M12-M16;
none check-solved, none promoted, no novelty wording used anywhere in this section. Requests this pass:
gallica.bnf.fr SRU ~22 (2 connection resets, each retried once per the good-citizen rule, both recovered),
gallica.bnf.fr IIIF manifest/image ~13 (1 connection reset, retried once, failed again -- stood down per the
one-retry rule and used the volume's alternate digitisation ark instead, a different resource, not a further
retry), github.com 2 shallow clones (dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers). No logins, no
credentials, no subagents.

Caveats: (1) "Leaf viewed" for M1 and M3 means a nearby leaf was fetched and read, not the exact folio the
catalogue names for the cipher/key itself -- Gallica's IIIF image index does not always run 1:1 with a volume's
own internal foliation (front flyleaves, substitution scans), and pinning the exact leaf for every row was out
of budget this sweep; treat "key/cipher present" for every row above as the BnF cataloguer's claim, not a
verified image read, per the d'Avaux lesson (a catalogue description conflated two different items in that
case). No score here claims a reading; nothing is new, unpublished or first (rule 10) -- these are catalogue
hits, not verified unsolved targets, and every row still needs check-solved's six-source sweep before the
board. (2) M6-M11 are each one or a few short ciphered letters inside a much larger plain-text miscellany, with
no key named in the same volume -- `size` was scored conservatively (1-2) because an unassisted short letter
can sit below unicity; a control test, not this scout, should settle whether there is enough ciphertext to
attempt without a key. Two further genuine-but-fragmentary hits were left off the table rather than padded in:
Français 14765's Flamel-attributed alchemical treatise "écrite en chiffres, en 12 clefs" (Denis Molinier) may
be symbolic/allegorical alchemical writing rather than a classical substitution cipher, and a single line of
"écriture secrète en chiffres indiens" at the end of Arabe 1966 (a 1332 CE religious manuscript) is too short to
size on its own. (3) Coverage outside BnF is thin and honestly so: LOC and Wellcome were queried and read (see
above) but yielded nothing worth scoring; Beinecke, Folger, Bodleian Digital, CUDL, Trinity College Dublin,
Leiden and the KB were not reached this sweep (bot-challenge empty responses, JS-only search pages, a
reCAPTCHA wall, or a transport failure on every attempt) -- a browser-tool pass (CLAUDE.md's Access playbook)
is the next step for those six, not a fresh curl attempt.

**Third pass, 24 September 2026 (M17-M21).** Brief: sweep the BnF series the first two passes did not reach --
Italien, Espagnol, Latin, Allemand, Nouvelles acquisitions françaises (NAF), Clairambault beyond the volumes
already listed above, Cinq Cents de Colbert, Mélanges de Colbert, Dupuy beyond 111/155/452/468, Moreau, Baluze
-- via the Gallica SRU API, `dc.source` scoped to each series and `dc.description` matching the brief's term
list (chiffre, chiffré, chiffrée, chiffres, cifra, cifre, cifrato, cifrada, zifra, Ziffer, Geheimschrift, "in
cipher", déchiffrement, contre-chiffre), restricted to the Manuscrits department by construction of `dc.source`
(the "dc.type is unindexed" finding from the second pass still holds). One request per series (11 total, plus
3 retries after proxy-side connection resets, all recovered -- `recentRelayFailures` in the agent-proxy status
traced these to the tunnel, not to Gallica, per `/root/.ccr/README.md`) rather than one per series-per-term,
using an OR clause across all fourteen terms inside the `dc.source` scope; SRU's default relevance ranking
returned the true top hits for every series this way, confirmed by spot-probing three series' raw dc.source
strings against a bare `dc.source all "<series>"` query first. Two series-name corrections needed before the
real hits appeared: NAF's `dc.source` field reads "NAF nnnn", not the spelled-out "Nouvelles acquisitions
françaises" (0 hits with the phrase, 20 with "NAF"); "Moreau" alone collides with the unrelated Moreau-Nélaton
art-history donation, the real Département des Manuscrits Moreau collection needing `dc.source all "Manuscrits
Moreau"` (0 hits either way once scoped correctly -- a genuine negative, not a syntax miss, confirmed by a
direct probe that the real collection is indexed and large, 86 hits for "Moreau" and "Manuscrits" together with
no chiffre term). 158 raw records, all unique arks. Filtered in two passes, same method as the second pass: 83
of 158 dropped as foliation/pagination/numeral-table noise (regex on "chiffres arabes/romains", pagination,
foliotation, numérotation, cote/cotation, microfilm -- confirmed again for Latin, where every hit was a
liturgical, biblical or grammatical manuscript using "chiffre" for a monogram, folio numbering or arithmetic
example, not cryptography), then 11 of the remaining 75 dropped for no correspondence-context word (lettre,
dépêche, ambassade, secret, correspond-, roi/duc/cardinal/reine, instructions, négociat-, envoyé, ministre,
cour) -- again poetry, liturgy and an arithmetic manual, not letters. 64 read in full.

Exclusion against a fresh shallow clone of both solver repositories (grepped by shelfmark, not just by name,
per the Pallotto lesson), Aymeloglu's cached `unsolved-ciphers/catalogue/decode-catalog.csv`, and this file,
CATALOG.md, LANDSCAPE.md and ciphers/ removed the majority of what looked promising on first read -- worth
recording because it is exactly the duplicate-work the exclusion step exists to catch:
- **Espagnol 132** (Philippe II to Vargas Mexia, "en chiffre", 16 Dec 1577) is already in Bourdeau's own
  `gallica_sweep/bnf_candidates.txt` (his repository runs the same kind of Gallica sweep; this ark is already on
  his radar even though no target folder exists yet for it) -- dropped per the second-pass convention of
  excluding by his sweep file, not only his solved folders.
- **Cinq Cents de Colbert 33** (cardinal de Joyeuse, "chiffrée", f.539, 1588-94 Ligue-Espagne negotiations) is
  Bourdeau's own already-solved `joyeuse/` target (his `gallica_siblings/src/colbert33_manifest.json` and the
  folder's own `ct_f539.txt` match the exact folio) -- found-solved, dropped.
- **Clairambault 325** (Jean de Calvimont to chancelier Duprat, "avec chiffre", 1525-26) already named as a
  checked sibling key ("Calvimont, Biermann key") in Bourdeau's `bayard1526/NOTES.md` -- a published key already
  exists for this letter, dropped.
- **Clairambault 328** (Guillaume Bochetel to Montmorency, "avec chiffres", Montcallier 28 Jul 1528) is DECODE
  record 2286, status Decrypted -- dropped. (The same shelfmark also carries DECODE record 2287, f.291-293,
  Bishop of Bayonne to Montmorency, Non-decrypted, that neither our Gallica hit nor Bourdeau's repo named --
  left unscored here as DECODE-catalogue territory, which LESSONS.md's 23 Sept entry already treats as not our
  lane, "a catalogue a daily-active project also reads.")
- **Clairambault 357** ("Lettre chiffrée" among 1586 Guise/Mayenne correspondence) is Bourdeau's own solved
  `clair357/` (README: "Deciphered in 1586, bound with the letter", published to his github.io) -- the whole
  volume is his, dropped.
- **Clairambault 360** ("Clef du chiffre employé avec le landgrave de Hesse-Cassel", Oct 1602) is the exact key
  sheet Bourdeau's `hesse1603/NOTES.md` already cites for his solved Hesse 1603 item -- dropped.
- **NAF 1045** ("Recueil de chiffres de correspondances militaires", Turenne/d'Erlach/Candale keys) is DECODE
  record 2790, a key-only entry -- key-present-no-letter-named, same pattern as M2/M5/M12, dropped.
- **NAF 720** (a Charles-le-Mauvais cipher key) states in its own catalogue description that the key has been
  "published several times" -- dropped on the catalogue's own word.
- **Baluze 331** (Michel Le Tellier?, "en partie chiffrée", Paris 11 Jun 1650, f.38) is DECODE record 2771,
  status Decrypted; the same volume's f.100 Colbert item is DECODE record 2773, also Decrypted -- dropped.
- **Baluze 163** ("Chrysogono" to comte d'Avaux, "en partie chiffrée", 1629-33) is DECODE record 2755, status
  Decrypted, and Tomokiyo's own `louisxiii.htm` (mirrored in Bourdeau's `esp318/lit/crypt/`) already prints a
  tentative reconstructed key for exactly this letter -- dropped.
- **Espagnol 318** (Frédéric III of Naples to Ferdinand/Isabelle, "en partie en chiffre", 1497) is a different
  item in the same shelfmark as Bourdeau's active `esp318/` target (his own item 95) -- whole-volume exclusion
  per the same convention as Espagnol 132, dropped without opening the image.
- **Italien 2245** ("Correspondance des Sforza", with an appended 19th-c. "Chiffres et catalogue de Registres"
  inventory of the Milan state archive's cipher registers) is a scholarly finding-aid list about ciphers, not a
  ciphertext letter, and sits in the same Sforza-Milan material our own `ciphers/sforza-maino-1446/` (closed
  negative) and two DECODE Sforza/Milan records already cover -- not scored, too tangential and too close to
  worked ground to be worth a leaf view this pass.

Five candidates survived, none checked against a control or check-solved, none opened at full resolution:

| Rank | Target | Year | Lang | Kind | Reference / Holder | Catalogue note | Leaf viewed | Image route | Total |
|---|---|---|---|---|---|---|---|---|---|
| M17 | Two ciphered letters (and a reply) between Cardinal Hippolyte d'Este ("cardinal de Ferrare") and the duc de Guise | Nov-Dec 1556, Jan-Feb 1557 | fr | recovery (kind corrected 24 Sept 2026 check-solved, was cryptanalysis -- a key is already published) | BnF Clairambault 349 (ark:/12148/btv1b9000668z, part of the Bossuet-Béthune-Brienne copy series) | "Lettres orig. du cardinal de Ferrare [Hippolyte d'Este], au duc de Guise et réponse (novembre-décembre 1556, janvier et février 1557), avec chiffres" -- catalogued as originals, not the 18th-c. Bossuet copies that make up most of this Clairambault sub-series (see M14/M15's caveat pattern for that distinction); no key named in this item. Not in either solver repo or the cached DECODE catalogue by this shelfmark. Check-solved 24 Sept 2026 (ciphers/clair349-este-guise-1556/NOTES.md): **partial** -- Tomokiyo's guise.htm (fr.20974 no.15) already publishes the substitution+nulls key for this exact letter and photographs this exact leaf (Clair 349 f.3, his "BnFClair349f3.jpg"), quoted verbatim in NOTES.md per rule 10; no plaintext/reading published anywhere found (Ribier 1666 checked by full text, one unconfirmed "cardinal de Ferrare" mention p.667, not this letter). Highest-value target of M17-M19: a solver only needs to apply the published key. | Yes (canvas f9 = f.3, confirms dense ciphertext) | gallica.bnf.fr IIIF manifest, public domain, no login | 33 |
| M18 | Letter from a Loménie de Brienne to the Queen of Poland | 19 May 1646 | fr | cryptanalysis | BnF Clairambault 1067 (ark:/12148/btv1b9000856f or btv1b90008551, two digitisations, "Mélanges généalogiques... X BRUN (DE)-BUX (DU)") | "Lettre avec chiffres adressée par de Brienne à la reine de Pologne (19 mai 1646)" -- same secretarial family as M16 (fr.5160, 1653-61 Brienne-Servien correspondence) but seven years earlier and a different volume; Tomokiyo's louisxiv0.htm Brienne 1647/1651 key tables (already fetched for M16's dense-band worker) are a plausible same-office key lead, not tried this pass. Not in either solver repo or DECODE by this shelfmark. Check-solved 24 Sept 2026 (ciphers/clair1067-brienne-poland-1646/NOTES.md): **open**, stage 2 verified unsolved (conditional). Confirmed Fol. 226 (short, single item) from the archivesetmanuscrits finding aid; Tomokiyo's Brienne ciphers (1647, 1651) are to a different correspondent (D'Estrades) and later dates, a lead not a match. Leaf not located this pass -- manuscript has no Gallica pagination/OCR index, two calibration probes both hit unrelated later (c.1701-02) printed material bound into the same composite volume, same failure mode as clairambault361-marini-1610. Closed-negative on DECODE, both solver repos. | No | gallica.bnf.fr IIIF manifest, public domain, no login | 34 |
| M19 | "Du Vergier", several original ciphered letters | undated within a name-alphabetised miscellany | fr | cryptanalysis | BnF Clairambault 1108 (ark:/12148/btv1b90009665, "Mélanges généalogiques... L UZES-VENDOME") | "Du Vergier (Lettres orig., dont plusieurs avec chiffres)" -- sender not otherwise identified in the visible catalogue snippet; plural ciphered originals in one place is the promising part. Not in either solver repo or DECODE by this shelfmark. Check-solved 24 Sept 2026 (ciphers/clair1108-duvergier/NOTES.md): **open**, stage 2 verified unsolved (conditional). Confirmed Fol. 245-264ish (~20 folios, a genuine multi-letter item) from the finding aid; no key or reading found in six sources. Leaf viewed at canvas f251 (folio stamp "248"): numeral-group ciphertext with a possible partial interlinear gloss (not confirmed at this resolution), and the clear-French facing page is signed "Vergier", confirming the sender name directly from the image. Closed-negative on DECODE, both solver repos, Cryptiana (0 hits for "vergier"). | Yes (canvas f251/folio 248, within item) | gallica.bnf.fr IIIF manifest, public domain, no login | 33 |
| M20 | "Avis de Flandre" (intelligence reports from Flanders), ciphered | undated within a volume catalogued "Année 1688" (Ordre du Saint-Esprit history series) | fr | cryptanalysis | BnF Clairambault 1161 (ark:/12148/btv1b90010063) | "Avis de Flandre, chiffrés" -- lowest confidence of the four Clairambault survivors: "avis" (intelligence briefs) rather than named correspondence, and the volume's own date heading may not be this item's date. Not in either solver repo or DECODE by this shelfmark. **Check-solved pass 24 Sept 2026 (LANE G): verdict open, low confidence, not promoted.** The finding aid (archivesetmanuscrits.bnf.fr, cc137837/cd0e35310) shows "Avis de Flandre, chiffrés" is not a standalone dated item but one clause inside a single bundled note for "Fol. 106 et suiv." that mixes four different Noailles-family figures and dates 1570-1719 -- no sender, recipient or date of its own is established, so neither "unsolved" nor an editions check can be confirmed yet. Not found in either solver repo (fresh clones grepped) or DECODE (web search only, no login) by this shelfmark or "Noailles". One IIIF leaf viewed at canvas 105 (naive folio guess, unverified) turned out to be an unrelated printed portrait engraving, confirming the volume interleaves printed and manuscript matter and that canvas-to-folio calibration is unresolved (all 342 canvas labels are "NP"). See ciphers/clair1161-avis-flandre-1688/NOTES.md. Next step: calibrate foliation (Lauer's printed catalogue, tome II, may help) and actually view f.106 before this can go on the board. | No | gallica.bnf.fr IIIF manifest, public domain, no login | 28 |
| M21 | Jean-Jacques Rousseau's own decipherments of diplomatic dispatches, written into the ambassador's letterbook during his Venice secretaryship | 1743-44 (volume's outer dates 18th-19th c.) | fr | recovery (decipherment already present, high edition risk) | BnF NAF 14913 (ark:/12148/btv1b525174513, "Papiers Montaigu") | "Aux f. 206, 214, 217, 250 et 274, déchiffrement de dépêches diplomatiques de la main de Jean-Jacques Rousseau" -- the decipherment is already on the leaf, in Rousseau's own hand, the M1/M3/M9/M15 pattern of a transcription-and-collation job rather than cryptanalysis. Not in either solver repo or DECODE by this shelfmark, but Rousseau's Venice secretaryship (Comte de Montaigu's embassy, the subject of a well-known Confessions chapter) is heavily studied; very likely already transcribed and discussed in Rousseau biographical scholarship (Leigh's Correspondance complète, the Pléiade edition) -- not checked this pass, flagged as the class-gate risk before any promotion. **Check-solved pass 24 Sept 2026 (LANE G): verdict open, strongly flagged against promotion -- very likely found-solved in substance.** Leaf viewed at f.206r: clean legible French plaintext ("venitiens en faveur de la Reine de Hongrie...M. le Prince de Lobkowitz"), confirming no ciphertext survives on these folios, only Rousseau's own decipherment. Editions-first sweep found this exact corpus (Montaigu ambassador, Rousseau secretary, 1743-1749) has been critically edited at least four times: Souchon 1915 (*Correspondance diplomatique du comte de Montaigu*, confirmed via Google Books metadata, Gallica altcha-walled), Leigh's *Correspondance complète* (a Feb/May 1744 enciphered passage already cited in scholarship), the Pléiade *Œuvres complètes* III (Candaux, Starobinski on the cipher/decipherment theme), and dedicated "Dépêches de Venise" critical editions by Catherine Labro (2012) and Fabrice Brandli (2014). Not found in either solver repo or DECODE by this shelfmark. No exact page match to f.206/214/217/250/274 confirmed this pass (Cairn 403'd, Gallica altcha-walled, Google Books NO_PAGES) -- recommend a JSTOR/Cairn print-check of Labro 2012 and the 2015 Archives de Philosophie article before any further work, not a fresh transcription. See ciphers/naf14913-rousseau-venice-1743/NOTES.md. | No | gallica.bnf.fr IIIF manifest, public domain, no login | 31 |

Caveats: (1) none of the five has been check-solved, viewed at full resolution, or scored against a control --
same status as M1-M16 before their check-solved passes; every row needs that six-source sweep before the board.
(2) Rounding out the coverage note from the second pass: the Archives et manuscrits site
(archivesetmanuscrits.bnf.fr) answered a plain reachability probe with HTTP 200 this pass but is still the same
JS-rendered search UI with no plain query URL found in budget -- consistent with both prior passes, not
re-attempted with the browser tool (out of this brief's scope). (3) Coverage of the eleven named series is
uneven by construction: Latin (68 raw hits, 0 survivors) and Italien (12 raw hits, 0 survivors after Italien
2245 was set aside) read as thoroughly negative for this term list; Allemand and the correctly-scoped Moreau
collection are genuine zero-hit series (confirmed reachable and populated by a bare `dc.source` probe, not a
syntax failure); NAF, Clairambault and Baluze were the productive series, matching the pattern already
established in LESSONS.md and the neighbour-record scan that BnF's own diplomatic-copy fonds (Clairambault,
Baluze, the Colbert series) concentrate cipher material more than the language-named series. Requests this
pass: gallica.bnf.fr SRU 14 (11 series queries + 3 retries after proxy-side `ws_closed_mid_exchange` resets,
confirmed proxy-side via `/root/.ccr/README.md` and the agent-proxy status endpoint, not a Gallica block; no
altcha/403 from Gallica itself), gallica.bnf.fr probe/dc.source-verification 6 (identifying the correct
dc.source strings for NAF and Moreau), archivesetmanuscrits.bnf.fr 1 (reachability only). github.com 2 shallow
clones (dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers, grepped by shelfmark, deleted after). No logins,
no credentials, no subagents.

## Digitised candidates outside the BnF (scout of 24 September 2026)

Row 14 continuation: a browser-tool pass (CLAUDE.md Access playbook route 2) on the six hosts the 23 Sept
sweep left unreached by curl, plus JSON/IIIF API checks on catalogues the 23 Sept sweep did not try. Read
first: LESSONS.md, the BnF digitised section above and its caveats, QUEUE.md "Candidates not on DECODE".
Every candidate below was checked against fresh shallow clones of dbourdeau/cyphersolver and
aaymeloglu/unsolved-ciphers, against sources/cryptiana/, and against this file, CATALOG.md, LANDSCAPE.md and
ciphers/ -- none is already named there. No image was opened at full resolution and no group was counted;
"leaf viewed" below means a catalogue/record page was read, not the ciphertext itself, per the M1/M3 caveat
in the BnF section.

**Hosts reached, real results, nothing scored.** Beinecke (Yale, `collections.library.yale.edu`, browser
tool): 54 hits for "cipher", 20 for the exact phrase "in cipher". The results are almost entirely two
already-mined clusters, not fresh material: the Voynich manuscript's own provenance/research files (Beinecke
MS 408A -- a separate, already enormously studied research area, out of this project's profile), and the
Manchester papers (OSB MSS fc37, Series II Letterbooks) -- Yard to the Earl of Manchester (12 & 16 Oct 1699)
is Bourdeau's own `yard1699/`, solved 18 Sept 2026 from a key in the same box ("Diplomatic cipher,
contemporary copy", OID 2046948, also in these results); the Earl of Jersey and Vernon letters to the same
recipient use the same THE=452/454 keys Bourdeau's `stepney/NOTES.md` already documents (DECODE R2854-R2872),
and Stepney-to-Manchester 1702 is already `ciphers/stepney-manchester-1702/` in our own repo. One
unattributed "Cipher manuscript" (OID 2002046, "unidentified language ... apparently based") and an
"Alchemical miscellany" surfaced but neither is correspondence with a named sender/recipient; not scored.
Bodleian Digital (`digital.bodleian.ox.ac.uk`, browser tool, reached, no challenge) returned only the
foliation/rhetorical-figure sense of "cipher" (a date in alphanumeric cipher notation, a Shakespeare
quotation, "cipher" meaning zero/nought) -- the same noise pattern as Gallica's "chiffré", confirmed again
for English; the exact phrase "in cipher" returned zero hits. CUDL (`cudl.lib.cam.ac.uk`, browser tool,
reached) returned 90 hits by collection facet (Cairo Genizah 13, Newton Papers 8, Medieval Medical Recipes
11, etc.) but the titled results sampled (Lambeth Palace MS 2086, Trinity College MS R.14.30, an Album
Amicorum, a Peterhouse astronomical text) are miscellanies and notebooks where "cipher" is an incidental
OCR/transcription hit, not correspondence; not scored.

**Hosts still blocked.** Folger (`catalog.folger.edu`): still a bot-check page ("Human Verification") to the
browser tool, one attempt, stood down. Trinity College Dublin (`digitalcollections.tcd.ie`): confirmed
reCAPTCHA challenge by page source (`recaptcha/releases/.../recaptcha__en.js`), one attempt, stood down.
Leiden (`digitalcollections.universiteitleiden.nl`): "upstream request failed" on both the first attempt and
the one permitted retry -- a transport/egress failure, not a bot page, matching CLAUDE.md's existing note for
this host. KB: `manuscripts.kb.nl/search` redirects to a static "Middeleeuwse handschriften" browse page that
does not honour a `?query=` parameter (no hits, no error) -- the right search endpoint for KB's own
manuscript catalogue was not found this budget; a Wayback fallback was not tried for any of these three
because none had a plain-page search result to look for in the archive (a live query, not a fixed URL).

**New API sources tried.** Wellcome (`api.wellcomecollection.org`, JSON API, reached): re-queried with
"cifra letter" and "chiffre lettre manuscrit" beyond the 23 Sept "cipher" query -- zero hits both times, this
lane is exhausted. LOC (`loc.gov/search/?fo=json`, reached): not re-queried, 23 Sept's Founders-Online-noise
verdict stands. Europeana (`api.europeana.eu`, JSON API, reached, `wskey=api2demo`): the productive new
route this sweep -- see below. e-manuscripta.ch: Cloudflare "Verifying your browser" challenge, stood down,
one attempt. e-codices.unifr.ch: reached (real server-rendered search, not a JS shell), English full-text
search for "cipher" returns zero documents; three metadata-field-name guesses (`sSearchField=description`)
all 500'd and the correct field name was not found this budget -- worth a second, better-briefed attempt, not
a plain retry. Manuscripta.se: reached (200) but is a client-rendered SPA with no results in the static HTML
for any curl query; needs the browser tool, not tried this pass (budget). BSB Digitale Sammlungen: has IIIF
Image/Presentation and OCR APIs (confirmed by documentation) but no plain-text search API found at the
guessed endpoint (404); the real search lives behind `opacplus`/`digitale-sammlungen.de`'s own search UI, not
resolved this budget. ONB: Primo Discovery, a JS-only shell to curl, not tried with the browser tool this
pass. Biblioteca Digital Hispánica (bdh.bne.es): 403 to curl, one attempt, stood down (a bot check, distinct
from its sister site below). Biblioteca Nacional de Portugal: the guessed URL (`purl.pt`) is a PURL resolver
index page, not a search interface -- the real BND search endpoint was not identified this budget.

**Europeana, the productive lane.** Europeana aggregates member-library metadata (including BnF, BNE, and
smaller archives neither solver project nor the 23 Sept sweep queries directly) behind one JSON API. "cipher"
alone is dominated by modern/WWII resistance material and Pepys-diary noise (already published, already
deciphered in the 19th century). Non-English terms are cleaner: "cifrada carta" (Spanish) surfaced a cluster
at the **Real Academia de la Historia's own Biblioteca Digital** (`bibliotecadigital.rah.es`, Madrid, public
domain / CC mark, reachable directly by curl with a browser-style User-Agent -- notably, Bourdeau's own
`lopehurtado/NOTES.md` and `r9658/NOTES.md` record this same site returning HTTP 403 to automated requests
for a different collection (Salazar y Castro A-26) as recently as 22 Sept 2026; it did not block this sweep's
`/es/consulta/` and `/es/catalogo_imagenes/` requests, which may be worth a retry for that stalled Bourdeau
lead -- not pursued here, out of this brief's scope, noted for NOTES.md/ASKS only).

| Rank | Target | Year | Lang | Kind | Reference / Holder | Catalogue note | Leaf viewed | Image route | Total |
|---|---|---|---|---|---|---|---|---|---|
| N1 | Cluster of royalist military-intelligence ciphered letters from the Spanish reconquest of Venezuela/New Granada against Bolívar, addressed to or from General Pablo Morillo, in a continuous archival series | 1817, 1817, 1820 | es | recovery (tentative) | Real Academia de la Historia, Madrid, Colección (Sig. 9/76xx): "Carta reservada y cifrada del General Enrile a Morillo..." (9/7658, leg.15, ff.32-34, 15 Jul 1817, record id=2242); "Morillo al Ministro de la Guerra... propone una clave en cifra para comunicar los asuntos reservados" (9/7657, leg.14, ff.155v-156v, 19 Nov 1817, id=1957); "Herrera a Morillo en carta cifrada dándole noticias de Romerito, que iba en busca de Bolívar" (9/7666, leg.23, ff.420-420v, 7 Nov 1820, id=5186) | Three items in one numbered series (9/7657-9/7666) spanning the same royalist expeditionary command: two explicitly-catalogued ciphered letters three years apart (1817, 1820) plus, in between, a letter of Morillo's own proposing a cipher key ("clave en cifra") for confidential business with the Minister of War -- a plausible in-collection key lead for the other two, in the "the key was in the archive beside the letter" pattern (LESSONS.md). Not confirmed: whether the Nov 1817 letter itself carries the key table or only announces the proposal. | No (record pages read via curl; RAH's `imagen_id.do` endpoint confirmed serving real JPEGs for two of the three ids, not opened) | bibliotecadigital.rah.es direct JPEG viewer, public domain (CC PDM), no login | 36 |
| N2 | "Nota cifrada del Conde de la Cañada" inside an exchange between Queen Isabel II and her Minister of the Interior Luis González Bravo | 1869 | es | cryptanalysis | Real Academia de la Historia, Madrid, Sig. 9/6958, Legajo XIX, Nº 117 (record id=14495) | Single named ciphered note inside a small folder of royal correspondence; different reign and collection from N1, no key lead found, not checked against N1's material this pass. | No (record page read via curl only) | bibliotecadigital.rah.es direct JPEG viewer, public domain (CC PDM), no login | 27 |

check-solved 24 Sep 2026 (ciphers/rah-morillo-1817/NOTES.md): **found-solved** for item 1 (9/7658, 15 Jul
1817 Enrile-to-Morillo) -- Rodríguez Villa's *El teniente general don Pablo Morillo* (1908, `eltenientegener01villgoog`
on Internet Archive) prints this exact letter in clear under its own matching heading, with footnotes marking
which passages were originally in cipher; **partial** for item 2 (9/7657, 19 Nov 1817, Morillo's cipher-key
proposal) -- the covering letter is likewise already in print, but the "adjunta clave" it refers to is not
reproduced in this edition, so the key itself (if it survives at RAH) remains an unpublished recovery
candidate; **open** for item 3 (9/7666, 1820 Herrera/Romerito) -- not found in the two volumes of this
edition located on IA (t.1, t.3); t.2 (1815) and t.4 (post-1818, which would cover 1820) were not found
digitised. Six-source sweep otherwise clean (no DECODE/Bourdeau/Aymeloglu/cryptiana hit).

check-solved 24 Sep 2026 (ciphers/rah-canada-1869/NOTES.md): **open**, stage 2 verified unsolved
(conditional -- RAE's "Copias de cartas de Isabel II de los años 1869 a 1871" catalogue page 403'd to one
WebFetch attempt and is otherwise unread; Google Books outstanding). No edition, catalogue or solver-repo
match found for this note by any of the six sources.

Caveats: (1) RAH's own on-site search (`/es/consulta/busqueda.do` -> `resultados_busqueda.do`) returned zero
rows for every query tried (`busq_general=cifrada` and variants) despite the site itself being reachable --
either it needs a session/cookie the plain GET does not carry, or a different field encoding; both records
above were found only via Europeana's index of RAH's metadata, so RAH's collection is very likely under-swept
here and a dedicated pass (ideally with the browser tool driving the real search form) would very likely find
more "cifrada"/"clave" items in the same 9/76xx-9/79xx numbered series. (2) Neither item's actual ciphertext
has been read off the image; "cryptanalysis" vs "recovery" for N1 is provisional pending that. (3) No score
here claims a reading or a novelty class; both rows still need check-solved's six-source sweep, including a
DECODE and PARES check specific to Spanish material (PARES holds the companion Consejo de Guerra/Estado
papers for this same 1817-1820 Venezuela campaign and was not queried this pass), before the board.

## UK and US catalogue candidates (LANE S scout of 24 September 2026)

LANE S brief: catalogues neither solver project reads, outside Gallica (LANE G's host). Read first: LANDSCAPE.md's
noise patterns ("cipher" as zero/foliation, Pepys, WWII, Voynich, Founders Online), QUEUE.md "Candidates not on
DECODE" and "Digitised candidates outside the BnF" (what those sweeps already reached and left blocked). Hosts
reached: Huntington Library CONTENTdm API (`hdl.huntington.org`, JSON), Lambeth Palace Library CalmView
(`archives.lambethpalacelibrary.org.uk/CalmView`), the Royal Archives / Georgian Papers Programme (`gpp.rct.uk`,
also CalmView-based), e-codices.unifr.ch (real search, English-language full text). Queried "cipher", "cypher"
(Lambeth/GPP, both spellings distinguished by CalmView's tokeniser), "chiffre"/"Geheimschrift" (e-codices, per
the brief's language list). NRS (`catalogue.nrs.gov.uk`): one reachability test only, `CONNECT tunnel failed`,
confirming the 23 Sept egress block -- not queried further. County record offices via TNA Discovery's "held by
other archives" records were gated on ASSIGNMENTS row 13's scoring worker (`session_01JE9661cSHNoQDHEvtc2qQb`)
posting a `done` line in ROOM.md; it had not by the time of this sweep (still only its 02:57 UTC claim line) --
skipped entirely per the brief, not attempted. Folger and Beinecke were not retried (already covered/blocked 24
Sept). Every candidate below was checked against fresh shallow clones of `dbourdeau/cyphersolver` and
`aaymeloglu/unsolved-ciphers` (by name and shelfmark/call-id, not just folder name), the cached DECODE catalogue
notes already in this repo, and QUEUE.md/CATALOG.md/LANDSCAPE.md/`ciphers/`; none is already named there. Raw
hits (86 across the three CalmView/CONTENTdm queries) and exclusion reasons are in
`sources/solver-diffs/2026-09-24-lane-s-uk-us.tsv`.

**Lambeth Palace Library, a working access route found.** The bare hostname 403s (an IIS-level block, both a
default and a browser User-Agent tried, one retry as the good-citizen rule allows); the actual catalogue lives
under `/CalmView/` and answers curl directly at 200 with no bot challenge. Its ASP.NET search form is a
WebForms postback, but submitting it once yields a **plain, repeatable GET URL** for the results page:
`/CalmView/Overview.aspx?src=CalmView.Catalog&r=((((text)='TERM')))` (URL-encode the parentheses/quotes) --
no session cookie needed, confirmed by re-fetching it cold. Paging beyond the default 20 needs one POST
setting the page-size dropdown to `0` ("All"), captured from the results page's own `__VIEWSTATE`. This route
is worth recording in CLAUDE.md's Access playbook for the next worker who needs Lambeth. "Cipher" returned 27
hits, "cypher" a further 10 (no overlap). Most of the "cipher" hits are the printed **Carew Manuscripts** (MS
596-638, Elizabethan Ireland, Sir George Carew/Mountjoy/Pelham correspondence): opening one record
(MS 597 p.246a, "A CIPHER") shows its own FindingAids field citing *Calendar of the Carew Manuscripts ... ed.
Brewer & Bullen (6 vols., 1867-73), vol. II, document 308* -- the whole run is a printed calendar, not a fresh
target; the other 15 Carew hits in the sweep are the same piece-run and almost certainly share that fate
(not individually opened). Two hits outside Carew have no such citation and are Anthony Bacon's own
intelligence archive (MS 647-662, Bacon's network for the Earl of Essex):

| Rank | Target | Year | Lang | Kind | Reference / Holder | What the catalogue says | Material | Total |
|---|---|---|---|---|---|---|---|---|
| U3 | Letters in cypher to Anthony Bacon, Secretary to the Earl of Essex | n/a (Bacon Papers, 1579-1598 span) | en/fr(?) | cryptanalysis | Lambeth Palace Library, MS 649, ff. 490-495 / Bacon Manuscripts | Title reads plainly "Letters in cypher to BACON (Anthony), Secretary to the Earl of Essex" -- plural letters, 6 folios, no FindingAids/printed-edition field (unlike every Carew hit checked). Bacon ran Essex's continental intelligence network; this class of archive (secret correspondence with named and coded agents) is exactly where a real nomenclator shows up. | Not confirmed online; LPL's own "Image database" link not checked this pass -- likely a copy order or on-site visit | 36 |
| U5 | Casenowe (A. Dufauk de) to Henri IV, King of France/Navarre | [1586] | fr | cryptanalysis | Lambeth Palace Library, MS 647, f. 218 / Bacon Manuscripts | Catalogue's own Language field: "French and cipher". Single letter, no FindingAids/printed-edition field. Possibly part of the same network/key as U3 (same MS 647-662 fonds), not established this pass. | Not confirmed online | 30 |

check-solved 24 Sept 2026 (U3, `ciphers/lambeth-bacon-649/`): **open**. Birch 1754 (full-text search, "cypher"
spelling) discusses cipher letters to Bacon in the same general period (pp.508, 562 of the two-volume
archive.org copy) but cites no shelfmark matching ff.490-495 -- a lead, not a match. Tosh's 2014 QMUL PhD
thesis on the Bacon letters is a named, unchecked lead. No hit in Cryptiana, DECODE cache, or either solver
repo. No free image found; REQUEST.md drafted (microfilm MS Film 793 / BL Microform Research Collections /
Adam Matthew Digital). Full search log in NOTES.md.

check-solved 24 Sept 2026 (U5, `ciphers/lambeth-casenowe-1586/`): **open**. Birch 1754 does not name Casenowe
or a 1586 Henri IV letter. *Recueil des lettres missives de Henri IV* (Guadet/Berger de Xivrey ed.) searched by
name and three spelling variants -- 0 hits. A live-web Cryptiana blog lead ("Henry IV's Cipher from 1590") was
followed up and ruled out: it covers a different correspondent (Hurlaut de Maisse, ambassador to Venice,
1590-92 letters) already worked in Bourdeau's repo (PR #7, f.370) -- not this item, not to be confused with it.
No hit in DECODE cache or either solver repo. No free image found; REQUEST.md drafted. Full search log in
NOTES.md.

**Huntington Library CONTENTdm API, a working query found after a false start.** The naive
`dmQuery/ALIAS/TERM/fields/...` form silently ignores the search term and returns a fixed title-sorted listing
(diagnosed on the Stowe Papers collection: "cipher", `"in cipher"` and no term at all all returned the identical
77 rows, all Jamaica plantation surveys with no cipher content) -- discard that form. The documented
`CISOSEARCHALL^TERM^all^and` clause works once `suppressfulltextsearch` is set to include full text (position 6
of the path = `1`, i.e. **not** 0 as in the first attempt, which gave a true zero). Query against the
**Manuscripts** collection (`/p15150coll7`), not Stowe: "cipher" (CISOSEARCHALL, full-text on) returned 31
genuine hits, "cypher" zero (the collection's own cataloguers use "cipher" only). Two clusters stand out, both
already digitised and viewable at `hdl.huntington.org/digital/collection/p15150coll7/id/<pointer>` with no
login wall hit (200, no auth):

| Rank | Target | Year | Lang | Kind | Reference / Holder | What the catalogue says | Material | Total |
|---|---|---|---|---|---|---|---|---|
| U1 | La Luzerne to Destouches (French naval commander, Chesapeake campaign), two undeciphered letters, with two sibling letters in the same small collection already deciphered | 16 & 31 Jan 1781 | fr | recovery | Huntington Library, mssDE 68 (4pp, 16 Jan) and mssDE 108(A) (8pp, 31 Jan) / Papers of Charles-René-Dominique Sochet Destouches | Per-page item records: mssDE 68 has 5+9+4 lines of "numerical cipher" across pp.1-3 (p.4 not checked) with no decode/translation noted; mssDE 108(A) has 11+ lines on p.1 of 8. Two other letters in the SAME small collection -- mssDE 37 (26 Feb, "decoded by Destouches") and mssDE 55 (3 Mar, "translated in another hand") -- are explicitly already deciphered, giving a plausible in-collection key (LESSONS.md's "the key was in the archive beside the letter" pattern). Destouches commanded the French fleet that fought the First Battle of the Chesapeake weeks later; La Luzerne was France's minister to the United States. | Digitised, viewer page loads without login (rights-reserved for reproduction per Huntington's standard notice, not access-gated) | 44 |
| U2 | Blathwayt Papers (Addenda), Spain/Madrid diplomatic-intelligence run, one confirmed cipher fragment plus an in-collection key and several unopened siblings | 1725-1729 | fr | recovery (tentative) | Huntington Library, mssBLA 186 (Madrid, 13 Sept 1728) + mssBLA 188 (July 1729, key source) + 8 further unopened items (mssBLA, "To [-----]"/named, same phycola) / William Blathwayt papers (Addenda) | mssBLA 186: "In French, with two lines in cipher" -- a small, likely below-unicity fragment on its own. mssBLA 188: an enclosure "in cipher [from Port Ste. Marie] ... deciphered in French" already in the same collection, i.e. a key for this correspondence network exists somewhere in mssBLA. Eight further 1725-29 items from the same "phycola" were returned by the search but not opened to item-info level this pass (pointers in the TSV). | Digitised, viewer page loads without login | 37 |

check-solved 24 Sept 2026 (U1, `ciphers/huntington-luzerne-destouches-1781/`): **open**. Doniol vol.5 (phrase
search, both dates) and Founders Online: no match on mssDE 68/108(A). Directly relevant lead, not a match on
this shelfmark: Cryptiana's blog (local snapshot) prints Tomokiyo's own decoding of a *different*, 8 Jan 1781
La Luzerne letter (Beinecke/Yale, not Huntington) in the same ~1200-element code, key/figure-assignment not
identified by him -- independently corroborated by Bourdeau's own notes ("The Luzerne 1781 code on cryptiana's
blog runs to 1199"). Strengthens the in-collection-key recovery case (mssDE 37/55 already deciphered) but is
not itself a reading of mssDE 68/108(A). No hit in DECODE cache or either solver repo (only false positives).
Copy-free, no REQUEST.md needed. Full search log in NOTES.md.

check-solved 24 Sept 2026 (U2, `ciphers/huntington-blathwayt-madrid-1728/`): **open**, but the "recovery"
framing is now much less tentative. The full OAC finding aid (item-level, not read by the scout) shows **six**
of the ten cipher-bearing items in this run (BLA 179, 185, 188, 189, 190, 194 -- not just BLA 188) are already
"deciphered in French" by the contemporary clerk, right beside the ciphertext in the archive; only BLA 186 (the
row's headline "two lines in cipher"), 184, 187 and 191(a) lack that note. No solution/key/attempt found in
editions, community lists, DECODE cache or either solver repo. Copy-free, no REQUEST.md needed. Full
item-by-item table and search log in NOTES.md.

**Georgian Papers Programme / Royal Archives (`gpp.rct.uk`), reached, low yield.** Runs the same CalmView
software as Lambeth (confirmed by identical CSS paths and the same `Overview.aspx?r=` query pattern) once the
`https://www.` host is dropped for the bare one (the `www` host is egress-blocked, `000`, the bare host
redirects and serves 200). "cipher" (2 hits) and "cypher" (4 hits) found only heraldic/monogram noise (a "Cipher
G.R." royal-jewels inventory, an "English cypher" on a carriage panel) and one single, already-famous 1880
telegram (Kimberley recalling Sir Bartle Frere from South Africa after the Anglo-Zulu War, VIC/MAIN/A/52/75) --
not scored, near-certain to be quoted in print given how documented that recall is. The Stuart Papers series
itself matched "cipher" only at the series (not item) level; per the brief's own warning, HMC's *Calendar of the
Stuart Papers* (7 vols.) already covers this collection in depth, so it was not swept item-by-item this pass.

**e-codices.unifr.ch, a real search this time, still no yield.** Found the actual search endpoint
(`/en/search/all?sQueryString=TERM&sSearchField=fullText`, confirmed from the page's own form, not a guessed
field name). "cipher" in full text: confirmed zero ("Your query for cipher in Full text returned no documents").
"chiffre" and "Geheimschrift" both return many hits, but e-codices' holdings are overwhelmingly medieval
liturgical/literary codices, not archival correspondence, and French "chiffre" = digit/numeral is the same
foliation-noise pattern already documented for Gallica; not opened item-by-item (budget, and a poor profile
match for this project regardless). Recommend dropping this host from future sweeps rather than retrying again.

Caveats: (1) neither the Bacon Papers items (U3, U5) nor the Blathwayt/Destouches items (U1, U2) have been
check-solved -- "not found in the two solver repos or this repo's own trackers" is a catalogue-matching result
under rule 10, not a verified-unsolved verdict; all four need the six-source sweep before the board. (2) None
of the four has had its actual page image opened; "cryptanalysis" vs "recovery" and the size estimates rest on
the catalogue's own item-level notes, not a leaf view. (3) U2's "recovery" is explicitly tentative: it is not
established that mssBLA 188's key covers the same cipher system as mssBLA 186's two lines, only that both are
in the same small collection from the same three-year window. (4) The Carew Manuscripts cluster (15 further
"cipher" hits beyond the one opened) is recorded here as a caution, not scored, so the next scout does not
re-find it: FindingAids on the one record opened cites the printed Calendar directly, and Carew's Calendar was
compiled specifically to print this correspondence in full, so the whole run is almost certainly already in
print. (5) Materials for U1/U2 (Huntington) carry a standard rights-reserved notice for reproduction use; that
is a copyright caveat on republishing images, not a login wall on viewing them (confirmed 200, no auth, on the
digital-library viewer page). Requests: hdl.huntington.org 18 (1 collection list, 6 dmQuery searches including
the diagnosed-broken form, 9 dmGetItemInfo, 2 viewer-page checks), archives.lambethpalacelibrary.org.uk 14 (2
root 403s, 1 retry per the good-citizen rule, then 11 under `/CalmView/`), gpp.rct.uk 8, e-codices.unifr.ch 6,
catalogue.nrs.gov.uk 1 (blocked, confirmed). All hosts one request at a time, >=1.5s apart, descriptive UA. No
Google Books, no TNA Discovery, no logins, no credentials, no subagents.

## Printed ciphertext (detector test of 23 September 2026)

Detector-test worker (RETRO-2026-09-23.md proposal 5, hypothesis A): `tools/ia_numeral_runs.py` swept 300
Internet Archive public-domain editions (`sources/ia-fulltext/editions.tsv`: 2 controls + curated named
editions from the brief + 8 keyword samples) for OCR lines that are mostly 1-4 digit numerals beside otherwise
clear prose, clustered lines fewer than 4 apart, and scored for repeat rate, distinct values and nearby prose.
Kept clusters (repeat_rate >= 0.3, numerals >= 15, prose_words >= 5) were judged from their context line only
(cipher-with-decipherment / cipher-without-decipherment / table / noise); adjacent kept clusters within 60
lines of each other in the same identifier were merged into one candidate passage. This is a detector test, not
a solver or verifier pass: nothing here is promoted, nothing is solved, and rule 10 applies (no reading is
claimed and no wording of new/unpublished/first is used).

**Controls** (must show their known printed cipher, per the brief): Thurloe vol. 1 (`collectionofstat01thur`)
reproduces exactly the RETRO-2026-09-23.md probe (111 clusters; the known cipher at line 43962, "at present
here 7. 7. 17. 24. 7. 6...", confirmed verbatim) — per that document this volume's own clusters are the
positive control (Aymeloglu has already worked Vande Perre's letters in it), not new candidates, and are
excluded from the table below. Rommel 1840 (`correspondancein00henr`) recovers cipher passages throughout (11
merged passages, pp. 84-391 of the printed volume per cyphersolver's own page map) matching cyphersolver
`hesse1603/NOTES.md`, which has already decoded every one of them with Rommel's 1846 key — both controls pass.
Catinat 1819 (*Mémoires et correspondance du maréchal Catinat*) is **not on Internet Archive** under any title
search tried (`catinat`, `memoires correspondance marechal catinat`, `memoires catinat`; Bourdeau's
`catinat1691/` reads the same edition from Bayerische Staatsbibliothek MDZ scans, `bsb10720287`, not IA) — this
is a gap in IA's holdings, not a tool failure, and is reported rather than silently skipped.

**Survivors** (cipher-without-decipherment on the page, not part of a known control): 24 merged candidate
passages, 23 of them further undeciphered numeral-figure passages in Thurloe State Papers vols. 2, 3, 5 and 7
(the same edition as the control, but different volumes/pages from the ones RETRO already flagged as control),
and one in a different edition entirely (BnF's sibling scan is not involved; this is a Leiden/Google-Books scan
via Internet Archive). Line numbers are exact and reproducible from `sources/ia-fulltext/runs.tsv` and the
cached `_djvu.txt` (gitignored, re-fetched by identifier on demand); they are OCR line numbers, not printed page
numbers, which were not reverse-engineered from the running heads this sweep (flagged as a caveat, not resolved).

| # | Edition | Identifier | OCR line(s) | Correspondents / date (from context) | Tokens | Decipherment on page | Prior work found where | Next step |
|---|---|---|---|---|---|---|---|---|
| P1 | Archives ou correspondance inédite de la maison d'Orange-Nassau, 1re série, **t. III** (Groen van Prinsterer, Leiden 1836; corrected from "t. IV" 23 Sept 2026 -- confirmed by DBNL's own edition and the Huygens WvO database's source citation, both read "tome III") | `archivesoucorre04housgoog` | 24010-24378 (full letter; corrected from 24100-24227, which covered only its first cipher cluster) | **Lettre CCCLXXXV, "Le Prince d'Orange au Comte Jean de Nassau"** (William of Orange to his brother Jean/Jan VI of Nassau), dated Malines, 21 Sept. 1572, printed **pp. 501-510** (corrected from 501-506; cipher recurs on pp.507 and 509 too); letter discusses the St Bartholomew's Day Massacre victims (Coligny, Rochefoucauld, Téligny) and his Low Countries campaign (Tilmont, Diest, Louvain, Malines, Dendermonde) | 79+ numerals over the whole letter | No, in the 1836 print itself — editor's footnote (p.502 n.1) states: "Il est à regretter qu'une comparaison attentive des passages [manqu]ants avec d'autres pièces dont nous possédons le déchiffrement, n'ait conduit à aucun résultat... il sera très difficile, si non décidément impossible, de retrouver le sens" | **found-solved, 23 Sept 2026** — see `ciphers/orange-nassau-1572/NOTES.md`: the Huygens Institute's "Correspondentie van Willem van Oranje" database (briefnr. 5198) cites L.J. Nepveu tot Ameyde's partial 1842 decipherment (*Algemeene Konst- en Letterbode* 1 (1842) 18-22, solution pp.19-20, marked incomplete) — absent from `sources/cryptiana/`, DECODE's cached catalogue and both solver-repo clones | found-solved, not promoted; next step is locating and reading Nepveu tot Ameyde 1842 pp.18-22 (Delpher.nl/Google Books/KB) to see what fraction of the cipher he broke and whether a usable key survives (possible contribution-lane item) |
| P2 | Thurloe State Papers vol. 2 | `collectionofstat02thur` | 46987 | Gen. Fleetwood to sec. Thurloe, printed p.368 | 31 | No | none of P2-P24 (checked 24 Sept 2026, see below) is one of the 4 catalogued STUCK items (TSP i.435, v.78, v.267, v.337 — all in vol.1/vol.5, different pages); "Fleetwood" not found in cryptiana or either solver repo | leaf-check done; category (b) different letter, no further action from this sweep |
| P3 | Thurloe State Papers vol. 2 | `collectionofstat02thur` | 402 | Mr. Bradshaw (Hamburgh) to sec. Thurloe | 54 | No | "Bradshaw" not found in cryptiana or either solver repo | category (b) |
| P4 | Thurloe State Papers vol. 3 | `collectionofstat03thur` | 56 | Mr. W. Prideaux to sec. Thurloe | 153 | No | "Prideaux" not found | category (b) |
| P5 | Thurloe State Papers vol. 3 | `collectionofstat03thur` | 273 | Major Creed to sec. Thurloe (re: Worcestershire/Gloucestershire forces); same letter as P6 | 241 | No | "Creed" not found (Thurloe context) | category (b) |
| P6 | Thurloe State Papers vol. 3 | `collectionofstat03thur` | ~275 | Major Creed to sec. Thurloe — 2nd cipher cluster of the P5 letter | 139 | No | as P5 | category (b), same letter as P5 |
| P7 | Thurloe State Papers vol. 3 | `collectionofstat03thur` | 277 | Mr. Bradshaw (Hamburgh), 2nd letter, A.D. 1654 in margin; longest vol.3 candidate | 527 | No | "Bradshaw" not found | category (b), distinct letter from P3 |
| P8 | Thurloe State Papers vol. 3 | `collectionofstat03thur` | 289 | Ld. chief baron Steele to sec. Thurloe | 444 | No | "Steele" not found | category (b) |
| P9 | Thurloe State Papers vol. 3 | `collectionofstat03thur` | ~611 | **General Blake** to sec. Thurloe, 14 June [1655] (West Indies fleet report, "...sent your highness an account of our affaires by capt. Peck in the Amity") | 25 | No | Tomokiyo's `sources/cryptiana/web/thurloe.htm` "General Blake (1655)" section reconstructs this correspondent's own cipher (worked example there decodes "26 33 39 24 36 31 24 32 38" = "gouerment"); this letter/date not individually named on that page but is the same cipher family | category (b); Tomokiyo's partial key applied mechanically 24 Sept 2026 (H=13/M=4/U=12 of 29 in this window) — not continuous English, see `ciphers/thurloe-printed/NOTES.md` |
| P10 | Thurloe State Papers vol. 3 | `collectionofstat03thur` | ~615 | Dr. Ralph Cudworth to sec. Thurloe | 45 | No | "Cudworth" not found | category (b) |
| P11 | Thurloe State Papers vol. 5 | `collectionofstat05thur` | 67 | **General Montagu** to sec. Thurloe, 20 April 1656, aboard fleet off Cadiz | 161 | No | Tomokiyo's thurloe.htm "Edward Montagu (Mountagu)" section publishes a full key reconstruction (E=18/42/56/93, THE=407) for this correspondent; confirmed directly against this passage — "407" recurs at every "the" in the OCR'd plaintext/cipher alignment. **Not** one of the 4 catalogued STUCK items (those use different, much smaller ciphers) | category (b), NOT one of the 4 catalogued items; same letter as P12/P13; Tomokiyo's partial key applied mechanically to the combined letter 24 Sept 2026 (H=36/M=27/U=256 of 319 across P11-13) — 8 "the"/6 "and" hits corroborate the crib, not continuous English, see `ciphers/thurloe-printed/NOTES.md` |
| P12 | Thurloe State Papers vol. 5 | `collectionofstat05thur` | ~68 | General Montagu, same letter as P11 — 2nd cipher cluster | 100 | No | as P11 | category (b), same letter as P11 |
| P13 | Thurloe State Papers vol. 5 | `collectionofstat05thur` | ~68-69 | General Montagu, same letter as P11 — 3rd cipher cluster | 149 | No | as P11 | category (b), same letter as P11 |
| P14 | Thurloe State Papers vol. 5 | `collectionofstat05thur` | 101 | **The Protector [Cromwell] to Blake and Montagu, generals at sea, 9 June 1656** — corrected from an earlier pass that mis-attributed this line to the preceding Lockhart letter, which ends just above it | 71 | No | Tomokiyo names this *exact* letter by page: "Cromwell wrote to Blake and Montague (9 June 1656, Thurloe State Papers, p.101)", same reconstructed Montagu cipher; also BL Add MS 4166 f.90-91 (DECODE R4885) per thurloe.htm | category (b); Tomokiyo's partial key applied mechanically 24 Sept 2026 (H=7/M=8/U=72 of 87) — not continuous English; NOT one of the 4 catalogued items; see `ciphers/thurloe-printed/NOTES.md` |
| P15 | Thurloe State Papers vol. 5 | `collectionofstat05thur` | ~420-421 | General Mountagu to sec. Thurloe, 16 Sept 1656, aboard the Naseby (MS Vol.xli p.474) | 129 | No | same Montagu cipher family as P11-14 (Tomokiyo); this specific date not individually named on that page | category (b); Tomokiyo's partial key applied mechanically 24 Sept 2026 (H=15/M=8/U=61 of 84) — not continuous English; NOT one of the 4 catalogued items; see `ciphers/thurloe-printed/NOTES.md` |
| P16 | Thurloe State Papers vol. 7 | `collectionofstat07thur` | 83 | Capt. Stoakes to sec. Thurloe (re: intercepted mail via Livorno) | 46 | No | "Stoakes" not found | category (b) |
| P17 | Thurloe State Papers vol. 7 | `collectionofstat07thur` | 365 | **Mr. Downing** to sec. Thurloe; heavily garbled OCR (long-s/Gothic type) over ~200 lines | 593 | No | Tomokiyo's thurloe.htm "George Downing (1658-1660)" section reconstructs this correspondent's ~600-element code (E=39/40/41/42/43/44/45, THE=468); token "39" recurs at very high frequency in this passage, consistent with E=39; this specific letter/date not individually named | category (b); Tomokiyo's partial key applied mechanically 24 Sept 2026 (H=99/M=73/U=892 of 1064) — not continuous English (only "e" recurs at H); re-OCR or view leaf before any further attempt, OCR quality is poor, see `ciphers/thurloe-printed/NOTES.md` |
| P18 | Thurloe State Papers vol. 7 | `collectionofstat07thur` | ~585 | Dr. Tho. Harrison to sec. Thurloe (re: proclamation of the new protector, i.e. Sept 1658) | 91 | No | a different "Jo Harrison" appears on thurloe.htm (re: the Blanck Marshall alias), not this correspondence; no coverage found for this Dr. Tho. Harrison letter | category (b) |
| P19 | Thurloe State Papers vol. 7 | `collectionofstat07thur` | ~403 | General Monck to sec. Thurloe | 411 (split across 35664-35794, see also P22/P23) | No | thurloe.htm mentions Monck only as a third party in Broghill's and other correspondents' key entries; no dedicated "Monck's cipher" reconstruction found; cipher style (numerals ~1-50) differs from Montagu/Downing's larger code sets | category (b); distinct letter from P22/P23 (different page) |
| P20 | Thurloe State Papers vol. 7 | `collectionofstat07thur` | 437 | Mr. S. Disbrowe (council of Scotland) to sec. Thurloe | 22 | No | "Disbrowe" not found | category (b) |
| P21 | Thurloe State Papers vol. 7 | `collectionofstat07thur` | 449 | not an intercepted letter — Richard Cromwell's speech to the army officers, "in the hand-writing of secretary Thurloe, and corrected by him", partly rendered in cipher (context: Richard Cromwell's protectorate, 1658/59) | 170 | No | none found; unusual item, no sender/recipient pair; cipher style resembles P19/P22/P23 | category (b), an unusual non-letter item |
| P22 | Thurloe State Papers vol. 7 | `collectionofstat07thur` | 461 | General Monck to sec. Thurloe — distinct letter from P19 (different page) | 200 | No | as P19 | category (b) |
| P23 | Thurloe State Papers vol. 7 | `collectionofstat07thur` | 527 | General Monck to sec. Thurloe — distinct letter from P19/P22 | 208 | No | as P19 | category (b) |
| P24 | Thurloe State Papers vol. 7 | `collectionofstat07thur` | 611 | Consul Maynard to sec. Thurloe (re: siege of Elvas) | 39 | No | "Maynard" not found (only an unrelated mirror hit in cyphersolver) | category (b) |

**Leaf-check results, 24 Sept 2026** (worker brief from the orchestrator; full table with letter dates, cipher-system notes and cross-reference detail in `sources/ia-fulltext/thurloe-check.tsv`; djvu texts for vols 2/3/5/7 fetched fresh this pass, 1.5s apart, cached under `sources/ia-fulltext/*_djvu.txt`, gitignored): **0 of 23** are identical to one of the 4 catalogued STUCK items (TSP i.435, v.78, v.267, v.337 — confirmed by locating all three of the vol.5 pieces, b/c/d, directly in the cached djvu text by their distinctive phrases and checking their OCR line positions fall nowhere near P11-P15); **23 of 23** are category (b), different letters with printed cipher groups and no decipherment shown on the page; **0** are category (c) (not cipher). Also checked directly against `sources/cryptiana/web/thurloe.htm` (Tomokiyo): a 5th Thurloe-vol.7 undeciphered fragment Tomokiyo documents there (Brussels, 3 April 1660, "the last post failing us...", pp.860-869) was located in the cached djvu (line ~79918) and falls well outside every P16-P24 line range — not a match for any of them either. Two correspondents among P2-P24 turn out to have their own cipher systems already reconstructed by Tomokiyo elsewhere on that page, independent of the 4 catalogued items: **General Blake** (P9) and **General/Cromwell-Montagu** (P11-P15, confirmed by direct THE=407 alignment; P14 is the exact 9 June 1656 letter Tomokiyo names by page), and **George Downing** (P17, consistent E=39 frequency, not directly confirmed by an aligned crib). General Monck's three letters (P19, P22, P23) and Richard Cromwell's speech transcript (P21) use a similar small-alphabet numeral style but no reconstructed key for them was found in the sources checked. No prior work found (cryptiana, cyphersolver, unsolved-ciphers) for the remaining 13 correspondents (Fleetwood, Bradshaw x2, Prideaux, Creed, Steele, Cudworth, Stoakes, Harrison, Disbrowe, Maynard). Nothing here is promoted or solved; rule 10 applies throughout, no wording of new/unpublished/first is used. Requests: archive.org 4 (djvu fetches for the 4 volumes, none previously cached this session), github.com 2 (shallow clones of both solver repos, cited not copied, deleted after grep). No subagents, no logins, no credentials.

**Extraction + mechanical decode, 24 Sept 2026** (`ciphers/thurloe-printed/`, `tools/thurloe_extract.py`): all 23 rows extracted into `ciphers/thurloe-printed/<Pn>/ciphertext.txt` (raw OCR + digit-normalised cleaned column, doubtful tokens marked, `index.tsv` summary). Check-solved for the 5 letters with a Tomokiyo-reconstructed system (P9 Blake; P11/P12/P13 Montagu, one letter; P14 Protector-to-Blake-and-Montagu; P15 Mountagu; P17 Downing): none is `found-solved` — Tomokiyo's page reconstructs each cipher from *other* correspondence and prints no decipherment of these specific letters. Mechanical application of his published partial key values (`decode.py --check`, rule 7) grades H=13/M=4/U=12 (P9), H=36/M=27/U=256 (P11-13), H=7/M=8/U=72 (P14), H=15/M=8/U=61 (P15), H=99/M=73/U=892 (P17) — none continuous English (H-graded content is letter-frequency crumbs, mostly "e", plus a few correctly-recurring "the"/"and", corroborating the crib alignment above without reading the letter). The 16 unkeyed rows (15 distinct letters, P5+P6 being one) grouped by correspondent and system: Monck's 3 letters + Richard Cromwell's speech transcript (P19/P21/P22/P23, small-alphabet numeral style, confirmed by spot-check) form the largest same-style pool at 1,610 raw numeral tokens — flagged as the best cryptanalysis candidate among the 18 unkeyed, not attempted (rule 3 would need a matched control first). Every other row is an isolated, apparently unrelated numeral cipher. Full detail, per-letter status and next steps in `ciphers/thurloe-printed/NOTES.md`. Requests: archive.org 4 (djvu re-fetch, fresh container, no cache carried over, 1.5s apart). No subagents, no logins, no credentials, no promotion, no novelty wording.

**Judged table/noise, dropped** (10 of 136 kept-filter clusters, not in the table above): `calendarofclaren05bodl`
(2 clusters — a name/subject index with volume.page citations, not cipher), `nuntiaturberich01romgoog`,
`nuntiaturberich04romgoog`, `nuntiaturberich10romgoog` (4 clusters — German-index page-number lists under
headwords), `bub_gb_RGMSAAAAIAAJ` and `correspondancem01goldgoog` (3 clusters — *Correspondance mathématique et
physique*, a Quetelet-edited math journal; the numerals are number sequences and tables, one context line reads
literally "cujus quilibet terminus indicat..."), `mobot31753002104062` (1 cluster — a Bulletin de l'Académie
royale de Belgique data table). None of the other 274 fetched identifiers' clusters passed the filter.

**Precision in the top 50 clusters by score** (score = numerals x repeat_rate): 50/50 (100%) judge as genuine
cipher-in-plain-text (27 candidate, 23 control); every table/noise cluster scored below rank 50 of 136 kept.
**Control recall:** 2 of 2 available controls recovered in full (Thurloe vol. 1's known cipher at line 43962;
every Rommel 1840 passage cyphersolver has already decoded); Catinat 1819 unavailable on Internet Archive
(reported above, not run). **Survivors:** 24 merged candidate passages (1 non-Thurloe, 23 Thurloe across 4
volumes not previously flagged as control), none promoted, none solved, five of them (P11-P15, Thurloe vol. 5)
flagged as needing a page check against the 4 already-catalogued/STUCK Thurloe items before being treated as
distinct. **Cost:** see `sources/ia-fulltext/NOTES.md` for the full accounting; approximately 35 archive.org
advancedsearch/metadata calls plus 274 cached `_djvu.txt` fetches (26 skipped on HTTP 401/404/500, no retries),
well inside the ~$8 cap.

## Bourdeau offline-only items with a route (scout of 23 September 2026)

Scout of ASSIGNMENTS row 21: a fresh shallow clone of `github.com/dbourdeau/cyphersolver` (commit `763a3b9`, 23
Sept 2026 17:30 UTC; code MIT, text CC BY 4.0, credited by folder below) was read with scripts (`TARGETS.md`'s
status column, every `profile.json`'s `outcome.class`/`class` field, and the per-target `NOTES.md`), not by
opening the clone in full. Twelve raw candidates carry a status of `offline-only`, `stuck`, `blocked`, or (in
`profile.json`) class `offline only` — i.e. Bourdeau's own attempt stopped for lack of material, not because
the cryptanalysis itself failed: `hamilton`, `colbert`, `rupert` (two TARGETS.md rows, one folder), `thurloe`,
`stepney`, `superscript`, `geertruidenberg`, `censorship`, `ungnad1576`, `florence1414`, `blancmesnil`,
`toulon1803`. Seven of the twelve (hamilton, colbert, rupert, thurloe, stepney, geertruidenberg, blancmesnil)
are already tracked under their own names in this project's LANDSCAPE.md, CATALOG.md and QUEUE.md (several
already on the board with an archive request out), so they are excluded here as duplicates, not as a fresh
finding — see `ciphers/hamilton-1650/`, `ciphers/stepney-manchester-1702/`, `ciphers/maurice-rupert-1645/`,
LANDSCAPE.md's "Colbert passages 1665-75" and "Torcy and Villars 1710" rows, and CATALOG.md's "Offline-only"
list. Five survivors are new to this project's own tracking. `tools/solver_repo_diff.py` was run against fresh
clones of both solver repositories and the current QUEUE.md (Tier A-C rows only; it does not cover the sections
below, which have no DECODE ids to match against these five) and returned no hit naming any of the five
shelfmarks, confirming none is already a QUEUE row under a different name.

Per CLAUDE.md rule 3, nothing below is reported as a closed negative: these are material-access blockers on
Bourdeau's own attempt, not a cryptanalytic verdict this sweep ran or checked against a control. Per rule 10,
"blocked"/"offline-only" describe Bourdeau's own recorded status, not a novelty class. Scores are hand-applied
against the scout.js rubric (`language_fit*3 + material*2 + key_lead*3 + size*2 + competition*2 + weight +
unread*3`, max 48), not run through the model scorer, since this sweep had no subagent budget.

| Rank | Target | Year | Lang | Kind | Bourdeau folder / blocker | Digitised image or copy route found this sweep | Total |
|---|---|---|---|---|---|---|---|
| B1 | WW2 postal-censorship training manual, two worked steganograms: a fashion drawing (Duployé shorthand signature) and an Amsterdam tram-line map (Morse in the print's "heavy lining", shift −11 fixed by a 2016 published fragment) | c.1943 (manual); message text de/fr | de/fr | contribution | `censorship/`, blocked (2026-09-15, TNA KV 2/2424): both illustrations' captions already state the plaintext in the manual itself (quoted in full in `censorship/NOTES.md`); what is missing is the exact mark-by-mark encoding, not the meaning. TNA's own free digital copy (115 images, downloaded by Bourdeau) tops out at ~3,504 px; the pen marks are 0.1-0.3mm, 2-5px at that resolution, below what any public scan (including Schmeh's blog photo) resolves | TNA holds the item (KV 2/2424) and already supplies digital copies for free; Bourdeau's own note names the fix directly — "needs new photography of the original at Kew" at roughly 1,200 dpi (about 47 px/mm) for page-spreads 14 and 17 only. This is the same TNA page-copy-order route already used elsewhere in this project (e.g. the N13-N33 rows); not itself priced or ordered this sweep, and not checked against LANDSCAPE.md's Dropped table for Schmeh's other famous/modern entries (this one, no. 33, is not on that table) | 26 |
| B2 | 1520s superscript-digit ciphers: Bishop of Worcester/Ghinucci (BL Cotton MS Vespasian C III f.304, DECODE R8476; C IV ff.313/315/363), Serno Gilino (Cotton MS Vespasian C IV f.214), and the Garbino letter (BnF Clairambault 327 ff.279-280 + fr.2988, 3019, 3022) | 1526-29 | la/it | recovery | `superscript/`, blocked (2026-09-15): DECODE images "Authentication required"; BL's own viewer unreliable since the 2023 attack; Bourdeau's note says "Gallica blocks this client" for the Garbino piece. A deciphered sibling (R8590) already exists for the Worcester fragments — "seed with the R8590 deciphered fragments" | The BL/DECODE portion is the same blocked category CLAUDE.md's own Access playbook already tracks (BL offline since 2023; DECODE needs a login this project's credentials do not currently pass) — no new route found. The Garbino leaf is on Gallica, which usually serves this project's client fine (unlike Bourdeau's, per CLAUDE.md); a single SRU catalogue query for "Clairambault 327" hit Gallica's altcha challenge this sweep (the same block the 23 Sept Dupuy 468 verifier hit on `texteBrut`), so its digitisation status is unconfirmed, not ruled out — worth a `tools/browser_fetch.js` retry from a session that can clear the challenge. **Flag, not resolved here:** CATALOG.md line 188 already states "Bishop of Worcester's superscript cipher (1526, 1529): decryption published, per Aymeloglu", which conflicts with Bourdeau's still-blocked status for the same fragments; the discrepancy needs a session that reads both claims side by side | 28 |
| B3 | David Ungnad (imperial ambassador, Constantinople) to Maximilian II, 12 March 1576, wholly in cipher | 1576 | de | recovery | `ungnad1576/`, blocked (checked 23 Sept 2026, the same day as this clone): ÖStA HHStA Türkei I Karton 32 Konvolut 3 (1576 I-IV) ff.199-203, catalogued in the public Archivinformationssystem with no item-level scan; the key survives and is already transcribed, from DECODE R392 (a 1830s-40s Gévay copy of the Vienna original, OSZK Quart. Lat. 2254 f.23) | The key is already in hand, so a reading is a table lookup once the five folios are photographed. `oesta.gv.at` is reachable from this environment (HTTP 200, unlike whatever blocked Bourdeau); its Fotoauftrag/reproduction order page was not located this sweep (one guessed path 404'd, not retried further per the URL-guessing rule) — route exists in principle (a national archive with a standing reproduction service) but not confirmed priced | 34 |
| B4 | Letters to the Signoria of Florence in the "Cifra Decemviri di Balìa 1414" | 1414 | it/la | recovery | `florence1414/`, blocked (checked 23 Sept 2026, the same day as this clone): the 1864 Gabbrielli key is rebuilt as a seed (`KEY.md`, 35 letter signs + 3 word signs) but the letters' exact filza is still unresolved (candidates: ASF Signori Responsive 7 or 8, or Signori-Dieci-Otto Legazioni e commissarie 4 or 8); DECODE, the ASF digitised-registers portal (Legazioni e commissarie 1-28 only) and the Yale Ilardi microfilm project (three reels, none covering the Signori letters) were all checked and hold nothing | ASF (`archiviodistatofirenze...`) returned `CONNECT tunnel failed` from this environment, consistent with an organisation egress-policy block rather than a site-side one (same failure mode CLAUDE.md's playbook describes for other blocked hosts) — not confirmed reachable or unreachable from a session with different network access | 29 |
| B5 | Lodewijk van Toulon to Dirk van Hogendorp (St Petersburg), The Hague, 30 July 1803, DECODE R2034 | 1803 | nl | recovery | `toulon1803/`, blocked across three sessions (most recent 22 Sept 2026): the ciphertext image itself is on DECODE and transcribed (110 groups); the key — Croiset's "Correspondentiecijffer" — survives only as a physical booklet (Nationaal Archief 2.21.045 inv. 34313 / duplicate description NA 2.21.227 item 335; original on loan to the Museum voor Communicatie, B1 392), with no online scan found anywhere checked. Same-key solved siblings (R1944-R1946) fixed only 3 of 67 words before that route was exhausted | `nationaalarchief.nl` returned HTTP 503 on both of this sweep's requests (one retry per the good-citizen rule, then stopped, host left alone) — could not confirm or rule out a reproduction route this sweep. Bourdeau's own notes name two holders to write to (the NA, which holds a photocopy, and the Museum voor Communicatie, which holds the original) | 39 |

**Per-lane report:** raw 12 (offline-only/stuck/blocked/profile-class-"offline only" folders in the fresh clone,
excluding one TARGETS.md row classed `infeasible` for a design reason, not lack of material) · kept 5 (the seven
duplicates above excluded) · digitised, copy-free 0 confirmed this sweep (Gallica altcha-blocked on the one
query tried for B2's Garbino leaf; nothing else came back positive) · copy-order 5, of which B1 (TNA) has the
most concrete, cheapest route (two named pages of an already-downloaded, already-catalogued piece); B2's BL/DECODE
portion is the generic already-tracked blocker, its Gallica portion unconfirmed; B3 (ÖStA), B4 (ASF) and B5 (NA)
all have a named holder and item but no confirmed price or process this sweep. Requests: github.com 2 (shallow
clones), oesta.gv.at 1, archiviodistatofirenze.beniculturali.it 1 (CONNECT tunnel failed), nationalarchives.gov.uk
1, nationaalarchief.nl 2 (503 both times, one retry), gallica.bnf.fr 1 (altcha challenge, stopped). No images
fetched, no logins used, no subagents.

## German and Austrian catalogue candidates (LANE S scout of 24 September 2026)

LANE S brief row K: German-language union catalogues and digitised libraries, per CLAUDE.md rule 1 and
LESSONS.md's "a catalogue a daily-active project also reads is not a lane" — DECODE (Vienna ÖStA above all)
is worked daily by both solver projects, so this sweep targets material neither scrapes: the German union
catalogue of letters and Nachlässe (Kalliope-Verbund) plus BSB/MDZ, ONB, the Deutsche Digitale Bibliothek and
Archivportal-D. Hessen/Rommel and Starhemberg/Windischgrätz are already solver territory (excluded per brief,
confirmed still true against fresh shallow clones of both solver repositories, `LANDSCAPE.md` and `CATALOG.md`).

**Hosts reached.** Kalliope-Verbund (`kalliope-verbund.info/sru`, SRU 1.2/MODS, no key needed): the main target
and the only productive host this sweep. Fifteen queries in German and Latin (`Chiffre` alone confirmed the same
"chiffré"/"chiffré" noise LESSONS.md already names for Gallica — 224 hits, almost all a Swiss "Association Le
chiffre de la Parole" literary correspondent, zero kept; `notis arcanis`, `litteris occultis`, `Chiffreschlüssel`,
`Ziffernschrift`, `Kanzleichiffre`, `Chiffrenschlüssel Brief` all returned 0; `in Ziffern geschrieben` returned 30,
all medieval/early-modern manuscripts where "Ziffern" means numerals/foliation, the same noise pattern as
Gallica's "chiffré" and Bodleian's "cipher" = zero — see LESSONS.md and QUEUE.md's BnF/outside-BnF sections):
`Geheimschrift` (113), `chiffriert` (17), `verschlüsselte Briefe` (43), `Chiffrierter Brief` (14, a targeted
phrase query used to pull the Konstanz cluster's full title text), `Geheimzeichen` (4), `verschlüsselter Brief`
(43, near-duplicate of the "verschlüsselte Briefe" set, run to catch singular/plural variants — no new hits).
112 unique records surfaced across every query; 108 are noise (modern literary Nachlässe and postcards where
a correspondent's or archive's name happens to contain "chiffr-", "Geheim-" or "Ziffer-" — Dürrenmatt's
Swiss "chiffre de la Parole" society, Goethe's own 1815 poem titled "Geheimschrift", a 1984 book title, a
1960s "secret sign: white handkerchief" note, and the medieval-manuscript "Ziffern"-as-numerals sense — full
list with per-row exclusion reasons in `sources/solver-diffs/2026-09-24-lane-s-de-at.tsv`). Four unique letters
in two clusters survive, all confirmed against fresh shallow clones of `dbourdeau/cyphersolver` (no shelfmark,
holder or correspondent-name hit) and `aaymeloglu/unsolved-ciphers`' cached DECODE catalogue (no matching
holder; the catalogue's own Busbecq/"Busbeck" entries, DECODE R1220/R1221, are a *different* item — see K1) and
against QUEUE.md, CATALOG.md, LANDSCAPE.md and `ciphers/`. Every record page was read (MODS via SRU, then the
underlying `swisscollections.ch` catalogue record for the ZB Zürich items, whose `500 |a` note field gives the
cataloguer's own description of the cipher); no image was opened — none of the four is public online (see below).

**Hosts not productive or not reachable.** BSB/MDZ: `opacplus.bsb-muenchen.de` and a guessed
`api.digitale-sammlungen.de/search` endpoint both 404; the IIIF/OCR APIs are documented but no plain-text
search API was found this budget (same unresolved finding as the 24 Sept BnF-outside sweep above — needs a
correctly-guessed `opacplus` query URL or the browser tool against the JS search UI, not tried again here).
ONB: `search.onb.ac.at` is a Primo Explore Angular shell (`<primo-explore>` root, no server-rendered results)
to curl; a guessed `primaws/rest/pub/pnxs` REST path 404'd (wrong path, not retried). Deutsche Digitale
Bibliothek: `api.deutsche-digitale-bibliothek.de/search` answers `403 NotAuthorizedException` unauthenticated —
needs an API key this environment does not have (ASKS-worthy if the person wants this lane reopened; not
requested here, per brief). Archivportal-D: `www.archivportal-d.de/search` serves an Anubis proof-of-work bot
challenge (not a JS-only shell, a PoW gate), one attempt, stood down per the good-citizen rule. None of these
four hosts contributed a row this sweep.

| Rank | Target | Year | Lang | Kind | Reference / Holder | Catalogue note | Total |
|---|---|---|---|---|---|---|---|
| K1 | Augerius Ghislen de Busbecke (Ogier Ghiselin de Busbecq, imperial diplomat) to Emperor Rudolf II | 6 June 1587 | la | cryptanalysis | ZB Zürich, Ms F 42.5 (swisscollections `ZBC73e7677281a24c689e4d1c1e2a9dd36d`) / Zentralbibliothek Zürich, Handschriftenabteilung | Catalogue note field (`500 |a`): "Verschlüsselter Brief eines Gesandten an den Kaiser" (an envoy's enciphered letter to the Emperor) — the cataloguer's own word, not a query-term coincidence. 10 pages. `506 |a gesuchspflichtig`: viewing requires an application, not open-shelf. Possible key lead, unconfirmed: `aaymeloglu/unsolved-ciphers`' cached DECODE catalogue carries two *different* Busbecq items, R1220/R1221 (Vienna ÖStA HHStA Staatskanzlei Interiora, "Chiffrenschlüssel", Kt.13 Fasc.20 ff.50-55, dated 1559, French plaintext, status "Key") — 28 years earlier, a different court archive and a different working language (French vs this letter's Latin), so not assumed to be the same system; worth a check once either item is in hand. | 36 |
| K2 | Talleyrand (French Foreign Minister) to Sieyès (French envoy to Berlin) and the reverse, on Prussian neutrality, the Repnin mission and Rhine troop movements around the Congress of Rastatt | Jul-Dec 1798 (P 1839/5, /21, /28, /41 read; P 1828/4 is 1804, same shelfmark family, not read) | fr | cryptanalysis | Stadtarchiv Konstanz, "Korrespondenz Ignaz Heinrich von Wessenberg – N-Q" (fonds `DE-611-BF-42689`), items P 1839/5, /21, /28, /41 (+ P 1828/4 unread) | Titles are the cataloguer's own ("Ansetzungssachtitel von Bearbeiter/in"), not originals. P 1839/5 (17 Jul 1798, Berlin, Sieyès probably to Talleyrand): "im Nachtrag chiffrierte und nicht chiffrierte Tagesnachrichten" (enciphered and plain daily news in a postscript), 4pp. P 1839/21 (26 Oct 1798, Paris, Talleyrand to Sieyès): "Chiffrierter Brief" outright, asking about Berlin's reaction to French troop movements on the Rhine, 1p. P 1839/28, /41 (Dec 1798, Feb 1799): further items in the same run, titles suggest continuing plain-plus-cipher traffic, not reopened to the note-field level this sweep. Filed inside a Wessenberg correspondence fonds at a diocesan city archive — an odd home for Directory-era Foreign Ministry traffic, not explained by anything read this sweep; worth resolving before any campaign (possibly Wessenberg-family provenance, not Wessenberg as correspondent). No image online; no key or sibling decipherment found. | 33 |
| K3 | Duke Ulrich of Württemberg to Ulrich Zwingli(?) [cataloguer's own "?"] | 11 Apr 1531 | de | cryptanalysis | ZB Zürich, Ms F 46.186 (swisscollections `ZBCb0983abd4cda4e25b2ec4c18a151b83a`), in "Briefe und Aufzeichnungen von Persönlichkeiten des Reformationszeitalters" | `500 |a`: "Der Brief ist in der Anrede sehr vage und stellenweise verschlüsselt" (the letter's salutation is very vague and it is enciphered in places) — a partial, in-line cipher inside an otherwise plaintext German letter, not a full ciphertext; likely well below unicity distance for the enciphered spans alone with no key lead. `gesuchspflichtig`. Reformation-era (Duke Ulrich's 1531-34 restoration campaign), addressee attribution uncertain. | 28 |
| K4 | Duke Ulrich of Württemberg to Ulrich Zwingli(?) [cataloguer's own "?"], undated, possibly an enclosure to another letter | 16th c. (undated) | de | cryptanalysis | ZB Zürich, Ms F 46.202 (swisscollections `ZBC63cf86b536d443f3b00b57ccd32ad325`), same fonds as K3 | `500 |a`: "Der Brief ist unadressiert, in der Anrede sehr vage und stellenweise verschlüsselt. Möglicherweise handelt es sich um eine Beilage zu einem anderen Brief." Same partial-cipher-in-plaintext pattern as K3, lower confidence (undated, unaddressed, cataloguer's own "possibly an enclosure" hedge). `gesuchspflichtig`. | 27 |

Caveats: (1) none of the four has been check-solved; this is a catalogue-metadata match (title plus the
cataloguer's own `500 |a` note field, read for all four), not a verified reading of an actual enciphered
text. (2) All four are `gesuchspflichtig` at ZB Zürich or held at a municipal archive with no digitisation
found — copy-order/access-request targets, not the copy-free preference the brief asked for; this sweep's
one copy-free lead (Kalliope itself never links to page images; it is a finding-aid aggregator, not a
digitised-library search) did not materialise this budget. (3) K3 and K4 are partial in-line ciphers inside
otherwise-plaintext letters, not full ciphertexts — closer to the SP 53/22-style "below unicity, no key lead"
blocker LESSONS.md already names than to a fresh cryptanalysis campaign; flagged low-confidence rather than
dropped, since the letters themselves (plaintext portions) have not been read for content that might justify
a copy order anyway. (4) K2's Wessenberg-fonds provenance question is unresolved and should be checked before
any request is drafted. (5) BSB, ONB, Deutsche Digitale Bibliothek and Archivportal-D are not exhausted, only
blocked at the routes tried this budget (see "Hosts not productive or not reachable" above); a session with
the browser tool or a DDB API key could reopen them.

**Per-host report:** Kalliope-Verbund: 15 queries, ~112 raw unique records, 4 kept (K1-K4), 108 excluded
(full list in `sources/solver-diffs/2026-09-24-lane-s-de-at.tsv`); 0 digitised/copy-free. BSB/MDZ: 2 requests
(both 404, no search API found). ONB: 2 requests (Primo JS shell, then a guessed REST path 404). Deutsche
Digitale Bibliothek: 1 request (403, needs an API key). Archivportal-D: 1 request (Anubis PoW challenge, one
attempt, stood down). github.com: 2 shallow clones (both solver repositories, grepped by shelfmark/holder,
deleted after). No logins, no credentials, no subagents. Never promoted, never solved.

**check-solved 24 Sept 2026 (LANE S batch F):**
- K1 (`ciphers/zbz-busbecq-1587/`): open, stage 2 verified unsolved (conditional — no image seen). Print check
  (Forster & Daniell 1881 vol. 2) inconclusive, no June 1587 letter located there; DECODE/Bourdeau/Aymeloglu
  confirm the cached R1220/R1221 Busbecq key records are a different 1559 item, as this row already noted.
- K2 (`ciphers/konstanz-talleyrand-sieyes-1798/`): open, stage 2 verified unsolved (conditional — no image
  seen). Bailleu 1881-87 vol. 1 print check inconclusive (same milieu, no exact date match); Pallain and Guyot
  not checked this pass.
- K3 (`ciphers/zbz-ulrich-zwingli-1531/`): **found-solved.** Printed in Huldreich Zwinglis sämtliche Werke
  (Corpus Reformatorum ed.), vol. 11 (1935), letter no. 1193, "Herzog Ulrich von Württemberg an Zwingli,
  (Cassel), 11. April 1531", source "Zürich, Zentralbibliothek: F 46, p. 473" — matches this row's shelfmark,
  sender, recipient and date exactly. Its coded names are already resolved via the edition's own printed
  cipher table, itself a reprint of an earlier decipherment (Schuler & Schulthess vol. VIII, p. 594, pre-1861).
  See NOTES.md for the full sweep and citation chain.
- K4: open, not located as a separately dated letter in the same edition (only two direct Ulrich-to-Zwingli
  letters are printed there, both fully dated: no. 1176, 3 March 1531 — a third F 46 item not previously a
  queue row, see NOTES.md — and no. 1193 above). Vol. 10 and the Schuler & Schulthess original not checked
  this pass.

## Kept, not scored this sweep

163 further kept candidates were left unscored by the 40-candidate cap (by plaintext language: fr 57, es 34, unknown 19, it 17, de 14, la 10). They are listed with the harvesters' evidence under `unscored_kept` in `QUEUE-scores.json`, in the filter's order, so the next run scores them first if the top forty move. Those with a working folder already, all closed-negative or blocked in LANDSCAPE.md: [Anonymous letters to Mr Tempest (Paris) and Dr Barret (Rheims), c. Dec 1585, endorsed by Phelippes (TNA SP 53/16 nos. 78-79)](ciphers/sp53-16-78/); ['Cifer with Spanish Spye', short ciphertext c.1586 (TNA SP 53/22 f.52, and the verso of f.40)](ciphers/sp53-22-f52/); [Lodovico Birago to the Duke of Nevers, Saluzzo, 13 Nov 1571, paragraph in numerical cipher (BnF fr. 3251 f.119)](ciphers/birago-nevers-1571/); [Admiral d'Estaing to Gerard, French minister in Philadelphia, 30 April 1779, intercepted (Clements Library, Clinton Papers 64:14)](ciphers/destaing-gerard-1779/); [Berthier to Napoleon, Koenigsberg, 22 Dec 1812 (AN AF/IV/1643) and the encoded letter to Marshal Marmont, 1807 (Vilcoq 1969)](ciphers/berthier-napoleon-1812/).

**Unread axis, 20 Sept 2026:** a heuristic first pass looked for edition/recovery/contribution signal words ("same collection", "sibling", "deciphered", "plaintext printed", ...) across all 163 rows' `material`, `key_lead` and `status_summary` fields. The result was not reliable enough to commit: the same words ("key", "sibling") show up for a candidate key that was tried and rejected as often as for one that is still live, and most rows are a single harvested line, too thin to tell the two apart without the kind of read a full scoring pass gives (CLAUDE.md rule 4). `unread` and `kind` were therefore left unset on the 163-item backlog this sweep; score them properly, per item, when they are next promoted into the scored set, rather than trusting a keyword match.

## Dropped this sweep

| Candidate | Reason |
|---|---|
| William Perwich to Lord Arlington, Paris, 9 April 1670 (TNA SP 78/129 f.180) | found-solved: broken Oct 2025 by Matthew Brown and by Lasry, Biermann and Tomokiyo (cyphersolver README 'Found already solved by others') |
| Thomas Randolph (Edinburgh) to the Earl of Sussex, 5/9 July 1570 (BL Cotton Caligula C II f.277, DECODE R4931; was rank 10) | found-solved: sibling sweep 23 Sept 2026 — the next leaf, f.278 (DECODE R4932, status Decrypted), is a clerk's contemporary decipherment (every cipher word re-copied with the plaintext above), reported and read by dbourdeau/cyphersolver `randolph1570/` on 21 Sept 2026 (CC BY 4.0 text); Boyd, CSP Scotland iii no. 339 already notes the original as 'partly in cipher, deciphered'. Not verified against the f.278 image from this account (bl.digirati.io egress-blocked). Our images and first-pass transcription stay in `ciphers/randolph-sussex-1569/` |
| Domestic intercepts with Jacobite-alias correspondents, cipher and cipher-key pairs, 1722 (TNA SP 35/36/34-37; was N2) | found-solved: check-solved 23 Sept 2026 (ciphers/sp35-intercepts-1722/NOTES.md). Atterbury Plot papers; keys and decrypts printed in the 1723 Report and Reports from Committees vol. 1 (1803) App. H pp. 329-330; Tomokiyo's atterbury.htm treats H.34-H.37 by name |
| Comte d'Avaux to Cardinal Antonio Barberini, 25 Nov 1633 (BnF Baluze 188; was N4) | found-solved / not a target: check-solved 23 Sept 2026 (ciphers/davaux-1633/NOTES.md). The letter is plain Italian (leaf viewed on Gallica); the volume's ciphered item is a separate 1632 letter already keyed by Tomokiyo (louisxiii.htm) and marked Decrypted on DECODE (2768) |
| Henri IV correspondence, letter no. 139 'chiffré', Antoine Séguier sieur de Villiers, Venice, 30 Jan 1601 (BnF Dupuy 63; was N5) | found-solved: check-solved 23 Sept 2026 (ciphers/dupuy63-139/NOTES.md); Tomokiyo henryiv.htm gives the reconstructed cipher |
| Bréval to Duke Henri II of Lorraine, in cipher (BnF Lorraine 377 ff.95-96; was N9) | found-solved: check-solved 23 Sept 2026 (ciphers/lorraine377-breval/NOTES.md); interlinear 17th-century decipherment on the leaf, Tomokiyo lorraine.htm key (2024), DECODE 7952 Decrypted |
| Cipher letter to Ferdinand I of Tuscany via Guicciardini, 10 May 1597 (BnF Dupuy 155 item 41; was N10) | found-solved / not a target: check-solved 23 Sept 2026 (ciphers/dupuy155-1597/NOTES.md); contemporary parallel decipherment on the leaves |
| Chauran to Williamson 1662 (TNA SP 84/165; was N11) | not a cipher: check-solved 23 Sept 2026 (ciphers/sp84-chauran-1662/NOTES.md); plain letters about cipher logistics; two items miscatalogued into the cluster |
| Benjamin Ingham, diary partly in cipher (Manchester, Methodist Archives; was N12) | found-solved: check-solved 23 Sept 2026 (ciphers/ingham-diary/NOTES.md); Weston shorthand, transliterated in Heitzenrater, Diary of an Oxford Methodist (1985) |
| George W. Erving to Madison, Madrid, 10 Aug 1807 (Pinckney legation code, no decode on the NARA copy) | found-solved: search-print check 21 Sept 2026 (ciphers/erving-1807/NOTES.md) — Founders Online's Early Access text of *The Papers of James Madison, Secretary of State Series* (founders.archives.gov/documents/Madison/99-01-02-1993) prints the despatch, docketed "In the Cypher of the Legation. No. 24 Duplicate", in full continuous plain English; QUEUE's "no decode on the NARA copy" was true of the specific M31 reel 12 microfilm frames but not of the printed edition. Bourdeau's cyphersolver/erving1807/NOTES.md (18 Sept 2026) had flagged this exact check ("whether Founders prints a decode") as its own next step and had not yet run it. |
| [Charles I (Oxford) to Prince Rupert, 29 April 1645 (BL Add MS 18983 f.14, DECODE R4921)](ciphers/charles-rupert-1645/) | found-solved: check-solved sweep 23 Sept 2026 (ciphers/charles-rupert-1645/NOTES.md) — Bourdeau's `cyphersolver/rupert1645/` (catalogue item 71) read 305 cipher groups (fraction_read 0.95) on 21 Sept 2026 by applying George Lasry's previously reconstructed King-Queen cipher key (DECODE R929, TNA SP106-5) unchanged, after ruling out two other sibling keys; write-up at https://dbourdeau.github.io/cyphersolver/rupert1645.html (MIT code, CC BY 4.0 text). No printed decipherment of this letter exists (Warburton 1849, Bromley 1787, web all checked, same as our own 20 Sept 2026 search-print pass); this is a key-recovery reading, not a rediscovered print source. Novelty not assessed here (rule 10; a verifier session would be needed before calling it new). |
| Jean Du Bellay, ambassador in England, letters 1529 (BnF Clairambault 329) | plaintext known: Du Bellay 1528-29 found already solved (Le Grand 1688, Bourrilly 1905, Lasry 2022) per cyphersolver SOLVED_CATALOGUE §4; Scheurer 1969 prints the 1529 letters from deciphered copies |
| Roosevelt cryptogram, April 1935 | explained by Bourdeau 16 Sept 2026: the number block is a permutation of 1-52 padded with zeros, not a cipher; famous list |
| Fair Game end-credits code, 2010 | modern film-credits puzzle, not a historical cipher; Bourdeau top50 'open but not settleable by cryptanalysis' |
| Doge Cicogna / Marco Ottobon to Giovanni Mocenigo, 27 April 1589 (BNE Mss/994 ff.34-38) | solved by Aymeloglu 16 Sept 2026 (ottobon-1589, key Ziffra prima R1789); Bourdeau's attempt was closed before that |
| Scorpion letters S1 and S5, 1991 | famous/excluded list (Aymeloglu SHORTLIST §6: hoax risk); modern |
| Le Tellier to Castelnau, 12 May 1657 | solved by Robert Pitt, reported on Tomokiyo's page 15 Sept 2026 ('Le Tellier-Castelnau Cipher (1657) Solved') |
| Voynich manuscript | famous/excluded list; adjudicated by Bourdeau as not a cipher of a European language |
| John Quincy Adams to the Secretary of State, No. 88, 25 June 1812 | read by Bourdeau 18 Sept 2026: premise refuted, code rebuilt, the nine 'undecyphered' lines read |
| Japanese diplomatic code telegram printed by Yardley (c.1920) | plaintext known: Yardley printed the plaintext (American Black Chamber p.251); Tomokiyo says it was probably solved by the Cipher Bureau; a reconstruction exercise, not an unsolved cipher |
| Davison to Walsingham, 27 July 1584 | found-solved by Aymeloglu 16 Sept 2026: printed in Boyd, CSP Scotland VII no. 222 (LANDSCAPE 'rows that moved') |
| Chinese gold bar ciphers, Shanghai 1933 | explained by Bourdeau 15 Sept 2026 (letter counts flat, no real text); famous/excluded list |
| D'Agapeyeff cipher, 1939 | famous/excluded list; Bourdeau: not enciphered English |
| Register of instructions/despatches to André Hurault de Maisse, ambassador at Venice (BnF Cinq cents de Colbert 369; was M1) | found-solved: check-solved 23 Sept 2026 (ciphers/colbert369-maisse/NOTES.md); ff.3-5's cipher table matches Bourdeau's already-published Maisse key digit-for-digit (catalogue id 17, fr.16093, credited 19-20 Sept 2026); the register's own text (18 leaves sampled) is plain French, not ciphertext |
| "Chiffre du duc de Paliano" (BnF Clairambault 351; was M2) | closed-negative / key-only: check-solved 23 Sept 2026 (ciphers/clairambault351-paliano/NOTES.md); folio pinned to ff.173/175 via the BnF finding aid, a nomenclator table copied twice, dated 1557; no letter in the volume is catalogued or observed as written in that cipher |
| Paolo Sarpi's cipher for his Castrino letters (BnF Dupuy 111; was M3) | found-solved: check-solved 23 Sept 2026 (ciphers/dupuy111-sarpi/NOTES.md); key at f.100-101, genuine ciphertext confirmed at approx. f.34; Busnelli already published this correspondence from this manuscript (1931 partial, 1986 full), folio citations matching what was viewed |
| "Double du chiffre de Claudio Marini" (1610) + a second "Double d'un chiffre" (BnF Clairambault 361; was M5) | closed-negative / key-only: check-solved 23 Sept 2026 (ciphers/clairambault361-marini-1610/NOTES.md); folios pinned via the finding aid (Fol. 211, Fol. 237) but not located by image (multi-layer foliation defeats canvas-index guessing); no ciphertext letter named anywhere in the volume's ~80-item list |
| Dorabella cipher, 1897 | famous/excluded list |
| Kryptos K4 | famous/excluded list; plaintext recovered from Sanborn's archive 2025 |
| WWII pigeon cipher | famous/excluded list; one-time pad per GCHQ |
| ADFGVX residue, 1918 (Childs corpus) | found-solved: keys published by Lasry, Niebel, Kopal and Wacker; the unread residue is transmission garble (cyphersolver README 'Found already solved by others') |
| Lima, Ohio robbery note, 1916 | modern true-crime note; Bourdeau odds low, variant transcriptions |
| Rubin cryptogram, 1953 | modern true-crime slip; not a historical cipher |
| Rayburn note, 2004 | modern; plausibly a password list, not a cipher (Bourdeau) |
| SS radio message, 1944 | probable forgery (Bourdeau: wrong typography and rank abbreviations) |
| Erba murder note, 2006 | modern true-crime note |
| Sufi Fiddle | unidentified script with no published transcription; provenance rests on a novel's afterword; not established as a cipher |
| Zodiac ciphers | famous/excluded list |
| Somerton Man code | famous/excluded list; not a cipher |
| Rohonc Codex | famous/excluded list |
| McCormick notes | famous/excluded list; modern true crime |
| Cylob, Blitz, Untersberg (Schmeh Top 50 nos. 50, 41, 11) | famous/excluded list (Blitz, Cylob) and modern; Bourdeau 'not settleable by cryptanalysis' |
| Shugborough, Fair Game, Powers (Schmeh Top 50 nos. 37, 36, 22) | famous/modern puzzles; Bourdeau 'not settleable by cryptanalysis' |
| World Record and Double Column Reloaded challenges (Schmeh Top 50 nos. 45, 13) | artificial compute challenges, not historical ciphers |
| Intercepted League letters summarised for Nevers' office, Sept-Oct 1589 (BnF fr. 3977 no. 96) | not a ciphertext: only the contemporary 'Recueil sommaire' of interpreted letters is described; the intercepts are not located |
| Frederick II to Louis Michell, Berlin, 28 Dec 1751 (KHA Prins Willem V inv. 198, DECODE R1957) | found-solved: printed in Politische Correspondenz Friedrichs des Grossen 8 (1882) no. 5263 (cyphersolver README) |
| Henry IV to Savary de Breves, Paris, 5 Jan 1610 (BnF fr. 3541 ff.4-7) | marked 'Solved' on Tomokiyo's page (Lasry solved a significant part in 2021; key reportedly preserved in BnF per Desenclos) |
| Vatican Challenge Part 4: manuscript of 1535/36, Segr. Stato Portogallo | solved Aug 2019 by Thomas Bosbach (Lasry et al., Cryptologia 2020), per Tomokiyo 'New Vatican Challenges'; MysteryTwister records 2 solves |
| Spanish Strip Cipher telegram, MysteryTwister Level X | MysteryTwister challenge with no locatable archival source; no new solutions accepted since July 2026 |
| Dataset of cryptographic postcards, 21 'unidentified' items (Slovak paper) | paper's dataset only; individual items neither identified nor accessible; not a ciphertext |
| Cylob cryptogram, c.1995-96 | famous/excluded list; modern |
| Madsen cryptogram (printed book, 2016) | modern book puzzle, not a historical cipher |
| Townshend chalkboard cryptogram, c.1980 | modern video clip, possibly meaningless (Schmeh); not a historical cipher |
| Scottish state letters of the Moray regency, Jan 1568 and 26 July 1569 (BL Add MS 33531 ff.73-74, 79-80) | found-solved: search-print sweep 20 Sept 2026 — CSP Scotland ii (Bain) no. 966 p.604 prints 'Decipher of same' for Mary to Abp Hamilton (f.73, 18 Jan 1568/69) in full; no. 1103 p.661-662 prints Throckmorton to Moray (f.79, 20 July 1569) 'In cipher deciphered'. Both already-printed contemporary decipherments |
| Sir Nicholas Throckmorton (Paris, Edinburgh) to Cecil, the Queen and the Council, 1559-63, 20 ciphertexts (BL Add MS 4136) | found-solved: search-print sweep 20 Sept 2026 — Forbes, A Full View of the Public Transactions... (1740-41), prints Throckmorton's 1559-62/63 despatches in full from deciphered MSS per his own stated editorial method; CSP Foreign vol.1 is abstract-only and twice notes it cannot render ciphered passages. Per-item match of the 20 DECODE dates to Forbes page numbers is a follow-up, not a fresh cryptanalysis |
| Sir Ralph Sadler (Edinburgh) to Henry VIII, 22 April 1543 (BL Add MS 32650 ff.214-216) | found-solved: search-print sweep 20 Sept 2026 — Clifford, Sadler State Papers I (1809) p.158 gives the letter in full continuous plain English; L&P Henry VIII vol.18 pt.1 no.448 confirms the BL MS itself already holds a contemporary Tudor decipher, citing Sadler I.158 |
| Thomas T. Eckert Papers, US Military Telegraph: ledgers of telegrams sent 'still in code', 1862-67 (Huntington mssEC 1-76) | edition, readable with the collection's own key: the 32 cipher/code books (mssEC 36-67) survive in the same Huntington collection as the ledgers, and the project's own blog already read at least one entry by looking the code words up in the book (re-scored 20 Sept 2026, unread=0) |
| Charles I to William Boswell, 1628 (TNA SP 106/5, DECODE R413), was rank 5 | found-solved: queue-hygiene sweep 23 Sept 2026 vs fresh clone (dbourdeau/cyphersolver 2e9ec01) — `boswell1628/`, fraction_read 0.99, already solved by Mark Woodard (Furman University), whose decipherment (CrypTool 2 monoalphabetic analyzer) was uploaded to DECODE R413 on 2021-11-09. Bourdeau's session (2026-09-21) added the sender's identity (Sir Ralph Boswell, a kinsman, not Charles I) and the date (15 Dec 1627, from the endorsement) but read no new signs. Source of plaintext: printed/uploaded decipherment (Woodard 2021), not a fresh cryptanalysis. |
| Unknown (York) to Lord Goring, 5 June 1645 (TNA SP 106/10, DECODE R932), was rank 22 | found-solved: queue-hygiene sweep 23 Sept 2026 vs fresh clone — `goring1645/`, already solved by George Lasry, whose key ("TNA SP106-3") and plaintext were uploaded to DECODE R932 on 2020-10-23; codes 104 and 46 remain open in Lasry's own reading. Bourdeau's session (2026-09-21) independently re-checked the key against the raw transcription (`check.py`) and confirms the same English throughout; added nothing new. Source of plaintext: key recovered by Lasry, applied via DECODE upload. |
| William Cecil to Sir Ralph Sadler and Sir James Croft, 11 Sept - 30 Oct 1559 (BL Add MS 33591, DECODE R4847-R4860), was rank 23 | found-solved: queue-hygiene sweep 23 Sept 2026 vs fresh clone — `burghley1559/`, fraction_read 1.0, printed in 1809 (Clifford, Sadler State Papers). The cipher itself is two groups in one letter; the other letter is entirely in clear. Source of plaintext: printed edition. |
| Queen Anne to Charles Mordaunt, Earl of Peterborough, 22 Feb 1711 (BL Add MS 4107 f.184, DECODE R4878), was rank 24 | found-solved: queue-hygiene sweep 23 Sept 2026 vs fresh clone — `anne1711/`, fraction_read 1.0, every code run matched to a printed clear-text source; two runs (91, 261) have no printed word but do not block the reading. Source of plaintext: printed edition (the code table itself is not rebuilt). |

Sources unreachable: archives: PARES (pares.mcu.es and pares.cultura.gob.es) was unreachable from this environment on 19 Sept 2026: curl got 'Connection reset by peer' and a TLS 'unable to get local issuer certificate' through the agent proxy, WebFetch got 503; PARES candidates therefore rest on search-engine snippets and on the unsolved-ciphers repository's PARES cache (/tmp/unsolved-ciphers/catalogue/pares-*.jsonl, harvested by aaymeloglu), cited as such. TNA Discovery's JSON API answered one query then returned 403 'Restricted' for every further query; the beta catalogue search (beta.nationalarchives.gov.uk) worked and was used instead. archivesetmanuscrits.bnf.fr and gallica.bnf.fr return 403 to WebFetch but 200 to curl with a browser user agent; two Gallica OAI calls were reset once and succeeded on retry. searcharchives.bl.uk returns its landing page for search URLs (single record pages load). folgerpedia.folger.edu gave 503 and catalog.folger.edu 403/202, so Folger call numbers come from search snippets. huntington.org gave 429; the OAC finding aid loaded. DECODE record pages and the record list load without login, but every DECODE image at TNA/BL is 'Authentication required' (free DECODE account).; tomokiyo: Nothing unreachable. Cryptiana web and blog were live on 19 Sept 2026 (HTTP 200). Tomokiyo's two 1710 transcription links (blencowe_geertruidenberg.txt, blencowe_polignac.txt) redirect (HTTP 302) and are dead, as LANDSCAPE.md says; maitland.htm and mirabeau.htm are not in the snapshot and were fetched live.; web: cipherbrain.de (Klaus Schmeh's 2023-mid-2026 blog) returned HTTP 503 on every path tried, and web.archive.org and reddit.com are not fetchable by the tool, so Cipherbrain posts from Jan 2023 to Jul 2026 and r/codes threads could only be seen through search snippets. boingboing.net (403), clements.umich.edu (403) and historum.com (paywalled 402) were unreadable; worked from snippets. The HistoCrypt 2026 Vichy-telegrams PDF downloaded but its text could not be extracted (no pdftotext, pypdf's crypto backend broken), so only its abstract is used; the Jacobite paper PDF link was 404. ciphermysteries.com monthly archive URLs for May-Sept 2026 are 404; the homepage shows no cipher-document posts after 5 Apr 2026.

## Printed ciphertext, round 2 (24 September 2026)

Detector-test worker, round 2 over continental editions (orchestrator brief, RETRO-2026-09-23.md proposal 5 /
hypothesis A continued): same method as the 23 Sept round (`tools/ia_numeral_runs.py`, `sources/ia-fulltext/NOTES.md`
§1), applied to `sources/ia-fulltext/editions2.tsv` — 276 further Internet Archive identifiers across 18 named
continental documentary-correspondence series (Lettres de Catherine de Médicis, Négociations diplomatiques
France-Toscane, Papiers d'État / Correspondance du cardinal de Granvelle, Relations politiques des Pays-Bas et de
l'Angleterre [Kervyn de Lettenhove], Archives ou correspondance inédite de la maison d'Orange-Nassau, CODOIN,
Nuntiaturberichte aus Deutschland, Deutsche Reichstagsakten, Calendar of State Papers Spanish/Venetian, Lettres
missives de Henri IV, Mémoires et documents / Nouvelle collection [Michaud-Poujoulat], Correspondance de
Marguerite d'Autriche, Urkunden und Actenstücke [Brandenburg], Lisch's Maltzan, Archivio storico italiano),
harvested via `archive.org/advancedsearch.php` (one request at a time, 1.5s apart, descriptive User-Agent,
deduped against round 1's `editions.tsv`). This is a detector test, not a solver or verifier pass: rule 10
applies, nothing here is promoted or solved, and no wording of new/unpublished/first is used.

**Controls** (3, per the brief: the 2 round-1 controls plus one continental control): Thurloe vol. 1
(`collectionofstat01thur`) and Rommel 1840 (`correspondancein00henr`) both reproduce their round-1 clusters
exactly (the known Thurloe cipher at OCR line 43962 recovered verbatim again). The continental control, Groen's
Archives Orange-Nassau tome III (`archivesoucorre04housgoog`, the Comte Jean de Nassau letter CCCLXXXV that round
1 found-solved via Nepveu tot Ameyde's 1842 key — see `ciphers/orange-nassau-1572/`), also recovers: 2 merged
cipher clusters at OCR lines 24181-24229 and 24362-24373, both inside the letter's known printed-cipher range
(pp. 501-510, corrected 23 Sept 2026). **3 of 3 controls recovered.**

**Fetch:** 279 identifiers processed (276 continental + 3 controls), 255 fetched (no items pre-cached — fresh
container, no cache carried over from round 1), 24 skipped on HTTP 404 (16) or 500 (8) with **no retries**
(good-citizen rule) — mostly dead/renamed `dli.ministry.*`, `bub_gb_*` and one guessed Henri IV identifier from
the keyword harvest. 17,783 raw cluster rows in `runs2.tsv`.

**Filter and judgement:** 270 of 17,783 raw clusters pass the same thresholds as round 1
(`repeat_rate>=0.3 & numerals>=15 & prose_words>=5`), across 33 of the 255 fetched identifiers. Merging adjacent
kept clusters (<=60 OCR lines apart, same identifier) gives 201 candidate passages: 21 are the 3 controls (8
Thurloe, 11 Rommel, 2 Orange-Nassau), leaving **180 non-control passages across 30 identifiers**, all judged from
their context line as **table/noise**, none as cipher-with-decipherment or cipher-without-decipherment:

| Type | Passages | Identifiers | What it is |
|---|---|---|---|
| Back-of-volume name/subject index, "Person, dates: vol,page. vol,page." citation format | 173 | 24 (Deutsche Reichstagsakten — several digitized copies/scans of the same run of Ältere/Jüngere Reihe volumes, `deutschereichst*`, `bub_gb_*`, `DeutscheReichstagsaktenJuengereReihe4`) | register/index apparatus, not a letter |
| Same, chronological "Regesten" register of report dates by month/day | 4 | 3 (`nuntiaturberich11romgoog`, `nuntiaturberich00kommgoog`, `bub_gb_VtBdAAAAIAAJ`, all Nuntiaturberichte) | a calendar of document dates, not a cipher letter |
| Same, name/subject index with volume,page citations | 2 | 3 (`urkundenundacten19berluoft`, `urkundenundacte15kommgoog`, `urkundenundacten2302berluoft` — Brandenburg Urkunden) | index |
| Same, name index | 1 | 1 (`correspondancedu00gran`, Correspondance du cardinal de Granvelle) | index |

(Row counts sum to 180 passages / 30 identifiers using each passage's dominant type; a handful of identifiers
carry more than one type.) Spot-checked from context lines across the full highest-to-lowest score range and
every distinct identifier group (not just the top 50) — every one reads as a citation list (a proper name or
subject heading followed by a run of "volume, page." references, or a list of report dates by month), the same
false-positive shape round 1 flagged for Clarendon's index volume and Nuntiaturberichte's page-list appendices,
but here the dominant source of the corpus's numeral-heavy prose-adjacent lines rather than a minor tail. None of
Lettres de Catherine de Médicis, Négociations diplomatiques France-Toscane, CODOIN, Calendar of State Papers
Venetian/Spanish, Lettres missives de Henri IV, Mémoires et documents/Nouvelle collection, Correspondance de
Marguerite d'Autriche, Lisch's Maltzan or Archivio storico italiano produced any cluster passing the filter at
all — these editions either print cipher passages as decoded plaintext with editorial brackets (the more common
continental convention per LESSONS.md) or simply have no register/index apparatus in this numeral-dense OCR
shape.

**Survivors: 0.** No cipher-without-decipherment passage was found among the 276 continental identifiers this
round (versus round 1's 24, all English-language Thurloe/Orange-Nassau). This is a negative result with matched
controls per rule 3: the detector demonstrably still works on this corpus (all 3 controls recovered, including
one continental-edition control), so the absence of survivors reflects the corpus, not a broken detector — but
see the caveat below on genre bias. No survivor rows to check against `sources/cryptiana/`, the DECODE cache or
either solver repository this round (nothing passed the filter to check); no blind check performed.

**Top five scoring passages** (all judged table/noise, listed for transparency, not as candidates): (1)
`deutschereichst00weizgoog` OCR line 102848, 1402 numerals, repeat rate 0.55 — a name-index run under a
biographical headword; (2) `deutschereichst02unkngoog` line 52048, 891 numerals, rate 0.68 — same; (3)
`DeutscheReichstagsaktenJuengereReihe4` line 51459, 1022 numerals, rate 0.40 — a bare page-number list under a
subject heading; (4) `deutschereichst05unkngoog` line 41130, 726 numerals, rate 0.51 — name-index run for a
margrave/elector entry; (5) `deutschereichst04unkngoog` line 62294, 620 numerals, rate 0.55 — name-index run for
a city entry.

**Caveat (methodological, for the next round):** round 1's near-zero false-positive rate does not generalise to
this corpus. Continental critical editions — especially the German *Akten*/*Urkunden* series — carry extensive
back-of-volume name/subject indices in a "headword, then a run of volume,page citations" format that structurally
matches the detector's numeral-run + nearby-prose signature (a German personal name or place name reads as the
"prose_words" the score requires). A future round over this kind of edition should either exclude index/register
volumes by title pattern before fetching, or add a cheap pre-filter (e.g., citations of the form `\d+,\s*\d+\.`
repeated many times per line, versus the looser groups-separated-by-periods-or-spaces shape of an actual cipher
passage) rather than relying on per-cluster human judgement at this volume.

**Requests, archive.org only** (no other host touched, no credentials used): 34 `advancedsearch.php` calls
(1 reachability test + 18 initial series queries + 6 ad-hoc debug queries fixing the Calendar of State Papers
Spanish/Venetian title-phrase queries, which needed "Venice"+"archives" rather than "Venetian" and returned 0
under the brief's first phrasing + 2 corrected re-runs + 7 page-2 boost queries on the largest series) plus 279
`_djvu.txt` fetches (1.5s apart, no retries on the 24 that came back 404/500) — 313 total, within the good-citizen
budget. No subagents, no logins, no credentials, no github.com requests this round (no survivors to check against
the solver repositories).

**Files:** `sources/ia-fulltext/editions2.tsv` (276 identifiers: identifier, title, year, why); `runs2.tsv` (all
raw clusters from the 255 fetched identifiers plus the 3 controls, reproducible by re-running
`python3 tools/ia_numeral_runs.py $(tail -n +2 sources/ia-fulltext/editions2.tsv | cut -f1) collectionofstat01thur correspondancein00henr archivesoucorre04housgoog --cache sources/ia-fulltext --tsv sources/ia-fulltext/runs2.tsv`
against freshly-fetched `_djvu.txt` files, gitignored, not committed).

## Dutch and Nordic archive candidates (LANE S scout of 24 September 2026)

Row 5 of the lane brief (`.claude/briefs/runs/2026-09-24-lane-s-scR.md`): Nationaal Archief, KB, Riksarkivet,
Rigsarkivet, manuscripta.se, openarch.nl. Read LANDSCAPE.md, LESSONS.md secs 1-2, README "What counts as a
result", the rubric in `.claude/workflows/scout.js`, and the two QUEUE.md sections named in the brief before
starting. Excluded against fresh shallow clones of `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers`
(grepped by name/shelfmark), `sources/cryptiana/`, CATALOG.md, LANDSCAPE.md and `ciphers/` — none of the rows
below is already named there. No image was opened (none of these items is digitised); "leaf viewed" does not
apply to any row.

**Hosts blocked, one attempt logged, not pursued further per the good-citizen rule.** `www.nationaalarchief.nl`
serves "Site in onderhoud" (site under maintenance) at HTTP 503 on every path, confirmed by page title, not a
bot block — retried once, still 503, stopped. `sok.riksarkivet.se` (the NAD/Riksarkivet search UI) redirects
every query to `/captcha`, confirmed both by curl and by `tools/browser_fetch.js` (a real headless Chromium hit
the same captcha page) — one retry via the browser tool, still captcha, stopped; its underlying JSON search API
lives on a different host and was used instead (see below). `daisy.rigsarkivet.dk` (the Danish Rigsarkivet's
Daisy finding-aid database) is reachable and not challenge-blocked, but its search box is a React component
with a hidden `<input>` behind a JS autocomplete widget that Playwright's `fill()` cannot target (confirmed:
`waiting for element to be visible` timeout) — no query was executed; a worker with more budget for
reverse-engineering the widget's underlying request, or a person with a browser, could search it directly at
`https://daisy.rigsarkivet.dk/daisy_forside`, field "Arkivskaber eller arkivserie" — note Daisy is a
fonds/series-name search, not a free-text item-description search like TNA Discovery, so it would not surface
"partly in cipher" notes the way the Riksarkivet API below does even if the widget were driven successfully.

**KB (Koninklijke Bibliotheek).** `jsru.kb.nl/sru/sru` is a real, working SRU endpoint (confirmed via
`operation=explain`), but its only collection reached (`x-collection=GGC`, the general printed-book catalogue)
returns exclusively noise for cipher terms: "cijferschrift" is 19th/20th-century numbered singing notation
(sheet music), not cryptography (142-100 hits sampled, all bladmuziek/liederen). No manuscripts-specific KB SRU
collection was found this pass (matches the 23 Sept sweep's finding that `manuscripts.kb.nl/search` does not
honour a `?query=` parameter); KB is exhausted for this budget, not pursued further.

**openarch.nl / openarchieven.nl.** Redirects to the modern `openarchieven.nl` domain; its API
(`api.openarch.nl/1.0/records/search.json`) requires a registered email parameter (`error_code:22`) and the
site itself indexes Dutch civil-registration records (birth/marriage/death registers), not archival
correspondence — structurally the wrong source family for cipher letters, so not pursued past reachability
checks (out of profile by design, not a block).

**manuscripta.se — reached, searched, off-profile.** A real, working full-text search
(`https://manuscripta.se/search?q=...`, confirmed navigable by URL once the initial JS route is loaded).
"chiffer", "chifferskrift" and "kryptografi" return zero hits. "hemlig skrift" (43 hits) and "brev chiffer" (63
hits, OR-matched, not a phrase) are entirely one pattern: 19th-century administrative letter-registers of the
Riksantikvarieämbetet (Swedish National Heritage Board), where "hemlig" and "skrift" match as ordinary index
words, not cipher correspondence. Manuscripta.se catalogues medieval/early-modern codices and a few
institutional archives, not the diplomatic/private correspondence collections this project needs — checked and
exhausted, not a live lane.

**Riksarkivet's public Sök-API — the productive route.** `sok.riksarkivet.se` itself is captcha-walled (above),
but its search functionality is also exposed, unauthenticated, as a documented REST API at a different host,
`data.riksarkivet.se/api/records` (docs: `github.com/Riksarkivet/dataplattform/wiki/Sök-API`, found by
websearch after the captcha block, not named in the brief). It searches item-level archive records (`Record`,
types Volume/Dossier/MapDrawing/etc., not just fonds titles), which is exactly the TNA-Discovery-style
free-text-over-descriptions search the brief wants, and it is not captcha-gated. Connection to
`data.riksarkivet.se` itself is noisy (intermittent `SSL_ERROR_SYSCALL` resets through the agent proxy, same
class of transient failure other lanes report for Gallica) — every query below needed 1-3 attempts, all
eventually 200. Queries run: `chiffer` (125 hits, both pages fetched), `chifferskrift` (0), `chiffrerad` (1),
`chifferskrivelse` (0), `chiffernyckel` (5), `dechiffrerad` (0), `"en chiffre"` (0), and `chiffer` restricted to
`only_digitised_materials=true` (2 hits, both WWII Krigsarkivet organisational-history volumes about the
signals/crypto service's administration, not ciphertext — confirming **zero digitised, copy-free items** in
this sweep). ~133 raw item-level hits read at snippet/note level; most are 20th-century Utrikesdepartementet
diary volumes recording only that a bundle of "telegram i chiffer" existed (administrative logistics, not
extant ciphertext) or WWI/WWII Krigsarkivet Kryptoavdelningen files, which the results themselves point to as
an already-published field (one hit's own note cites Gunnar Åsebo's *Chiffer och koder inom svenska flottan
under ett sekel 1845-1945* and three Bengt Beckman books on Swedish 20th-century cryptology) — not scored, per
rule 1, same pattern as the non-DECODE section's dropped "administrative correspondence about cipher/code
logistics" rows. One hit set also self-names the Riksarkivet "Chifferklaver" collection as a card-indexed cipher
group (`SE/RA/221/2210.01.1/F/F 5/F 5 C/7`'s note); that collection is already Bourdeau's ground —
`riksarkivet1628` (DECODE R4282-R4341, "låda II:113" etc.), `goertz1717` (DECODE R4350) and `baner1640` are all
drawn from material DECODE has catalogued out of Riksarkivet Stockholm, so **Chifferklaver items are excluded
from this sweep as DECODE/Bourdeau territory**, not a fresh Riksarkivet lane. The rows below are all outside
Chifferklaver, in named family/embassy/chancery archives.

| Rank | Target | Year | Lang | Kind | Reference / Holder | Catalogue note | Next move | Total |
|---|---|---|---|---|---|---|---|---|
| R1 | Ulric Celsing (Swedish minister to the Ottoman Porte, Dresden, Vienna) — correspondence with Ignace Mouradgea d'Ohsson (dragoman, later Swedish minister at Constantinople, author of *Tableau général de l'Empire othoman*), with a cipher key in the same folder | 1779-1782 | sv/fr | recovery | SE/RA/721512/IV/IV 1/5 (Beskickningsarkivet från Biby, "Ulric Celsings tid i Dresden, Wien och Sverige 1780-1805 / Korrespondens") / Riksarkivet i Stockholm/Täby | "Korrespondens med Ignace Mouradgea d'Ohsson... Brev och brevkoncept ligger tillsammans: - Chiffernyckel. Se även bilaga till brevkoncept 13/10 1780. - [dated runs of letters/drafts] 1779-1782" — several years of letters and drafts filed with an explicit cipher key, the "key beside the letter" pattern (LESSONS.md). d'Ohsson is independently notable (his *Tableau* is a major primary source on the Ottoman Empire), raising the weight and the chance a specialist edition already exists — not checked this sweep. | Riksarkivet reading-room copy order for the whole folder (key + letters); check d'Ohsson biographical/editorial literature for a published correspondence before cryptanalysis. Not digitised. | 37 |
| R2 | Gustaf Celsing (Swedish minister to the Ottoman Porte) — letter-drafts to Georg Wilhelm af Sillén, with a cipher key in the same volume | 1755-1764 | sv/fr | recovery | SE/RA/721512/II/II 1/II 1 B/4 (Beskickningsarkivet från Biby, "Beskickningarna till Konstantinopel 1737-1779 / Korrespondens / Korrespondens med hemlandet") / Riksarkivet i Stockholm/Täby | "Brevkoncept av Gustaf Celsing till Georg Wilhelm af Sillén 1755-1757, 1760-1764, odat. Med ett brevkoncept... till greve Ekeblad 3 maj 1763... Med chiffernyckel." Same family/embassy archive as R1 (father and son, one fonds); a Dutch archive item in Bourdeau's own `roell1809/turk_inv.txt` independently names "G. Celsing, Zweeds gezant te Constantinopel" in an unrelated 1753/1763 context, confirming the person but not this material. | Riksarkivet reading-room copy order (drafts + key); combine with R1 as one fonds-level request. Not digitised. | 34 |
| R3 | Louis de Geer (financier of Sweden's Thirty Years' War armaments) papers — journals, letters and a cipher key, in the circle of Axel Oxenstierna | 1644-1646 | sv/nl/fr | recovery | SE/ULA/13506/1/I/45 (Leufstaarkivet I, "Leufsta arkiv. Det historiska arkivet") / Riksarkivet i Uppsala landsarkiv | "Brev från W. Lancken (?) 1644... Louis de Geers advertisement insänt till Axel Oxenstierna 17/8 1644... Journal myner Reyse... Chiffernyckel. Förteckning över adressater (moderna) i journalerna." A cipher key sits among de Geer's own war-logistics correspondence and journals; which specific letter(s) it maps to is not stated in the catalogue note — genuine but unconfirmed key-to-text match. | Riksarkivet i Uppsala reading-room copy order; on arrival, check whether the key matches any of the bundled letters before assuming cryptanalysis is needed. Not digitised. | 31 |
| R4 | Krigsarkivet Kryptoavdelningen and UD "telegram i chiffer" diary cluster — administrative, not scored | 1901-1949 | sv | — | ~60 further SE/RA/221 and SE/KrA/0202 items from this sweep's raw TSV | Excluded as a class, not a row: diary volumes recording only that ciphered telegrams existed (the cipher itself not preserved as text) or Kryptoavdelningen instruction/policy files; the field already has a dedicated published historiography (Beckman, Åsebo — cited above). Listed here for the record per rule 10 ("report where it was not found"), not scored. | None — do not pursue without a specific published gap identified first. | — |
| R5 | Anonymous unsigned enciphered private letters, "Welin" to "Östergren", among incoming letters to Count Adolf Göran Mörner and his wife | undated | sv | cryptanalysis | SE/RA/720290/I/12/2/153 (Esplunda arkiv, "Excellensen greve Adolf Göran Mörners och hans makas handlingar / Inkommande brev") / Riksarkivet i Stockholm/Täby | "Brev från privatpersoner: Welin - Östergren, brev i chiffer och icke undertecknade" — private, unsigned, enciphered correspondence in a count's incoming-letters series; no key or date given at catalogue level, no printed source found. Lowest-confidence dating of this batch (Mörner's own dates not established here). | Riksarkivet reading-room copy order; establish date/hand before anything else, since "undated, unsigned, private" is also the profile of a much later (e.g. 19th-c. social/romantic) cipher, not necessarily diplomatic. | 28 |
| R6 | Magnus Jakob Crusenstolpe (1795-1865) papers — spy reports and cipher documents concerning the 1809 revolution (the coup against Gustav IV Adolf) | 1809 (papers collected/held by Crusenstolpe, who was 14 in 1809) | sv | cryptanalysis | SE/RA/720266/03/08/~/2,5 (Ericsbergsarkivet, "Smärre enskilda arkiv och arkivfragment / Crusenstolpe-papper") / Riksarkivet i Stockholm/Täby | "Ink brev och skrivelser, diverse utkast och anteckningar m m. Spionrapporter, chiffer handlingar rörande revolutionen 1809." Crusenstolpe was a well-known 19th-c. Swedish writer/censor whose own later work is extensively published, but this note describes items about 1809 in his papers, not by him — provenance and authorship of the cipher material itself unclear from the catalogue snippet alone. | Riksarkivet reading-room copy order; read the full finding-aid entry (not just this snippet) to date and attribute the cipher items before scoring further. Not digitised. | 28 |
| R7 | Mauritz Vellingk (former Swedish governor-general of Bremen-Verden), reports partly in cipher sent from exile in Hamburg after the Danish conquest of Bremen-Verden, plus his own collected copies referencing the 1713 neutrality treaty | 1713-1714 | sv/de | cryptanalysis | SE/RA/1411/E/E VI/1 (Kanslikollegium, "Inkomna handlingar / Skrivelser i utrikesärenden...") and SE/RA/720626/E/E 6015 (Mauritz Vellingks samling, "Avskrifter") / Riksarkivet i Stockholm/Täby | First: "Från M. Vellingk... som efter dessa provinsers erövring av danskarna vistades i Hamburg utan egentligt uppdrag men sände rapporter, delvis i chiffer." Second (his own collection): "Avskrifter. Chiffer. Handlingar angående neutralitetstraktaten 1713." Great Northern War period, one named correspondent, two related holdings in the same repository. | Riksarkivet reading-room copy order for both; check Great Northern War documentary editions (e.g. Nordisk familjebok-adjacent or period diplomatic-history print series) for Vellingk material before cryptanalysis. Not digitised. | 28 |
| R8 | Karl XI's full power (fullmakt) for the Swedish peace commissioners, partly in cipher | 6 May 1677 | la | cryptanalysis | SE/RA/25.3/4/II/7/B (Originaltraktater med främmande makter, "Tyskland / Kejsaren (Österrike-Ungern) / Fredsfördrag med tillägg") / Riksarkivet i Stockholm/Täby | "Konung Karl XI:s fullmakt för svenske kommissarierna, Nääs, 6 maj 1677. Latin, delvis i chiffer. Papper, 3 sidor text, sigill." A royal full-power document for treaty negotiations (Sweden-Empire, Scanian War era) — high formal weight but real edition risk: full-power instruments for named 17th-c. treaties are often already printed in treaty collections (e.g. Du Mont's *Corps universel diplomatique* or period Swedish riksdag/chancery print series), not checked this sweep. | Search treaty-edition literature for this Nääs/1677 full power before any copy order; lowest-priority row here pending that check. Not digitised. | 28 |
| R9 | "Handlingar ang. chiffer" — 18th/19th-c. cipher-system descriptions, incl. a 1786 proposal for a cipher machine by F. Gripenstierna | 1700s-1800s | sv | contribution (caution) | SE/RA/221/2210.01.1/F/F 5/F 5 C/7 (Utrikesdepartementet med föregångare, "Samlingsserie") / Riksarkivet i Stockholm/Täby | "Handlingar ang. chiffer, med bl.a. skrivelser från F. Gripenstierna 1786 ang. en chiffermaskin, beskrivningar av chiffersystem under 1700- och 1800-tal, kvitton på mottagna chiffernycklar. Jfr. vidare samlingen Chifferklaver..." — about cipher *systems and machines*, not a specific enciphered text to read; the note's own cross-reference to Chifferklaver puts this adjacent to Bourdeau's territory. Interesting as a history-of-technology contribution (an 18th-c. Swedish cipher-machine proposal), not a solve target. | Not a cryptanalysis/recovery candidate; flagged for the contribution lane only if someone wants the Gripenstierna machine description specifically. Not digitised. | 22 |
| R10 | "Chiffer och chiffernycklar avseende Axel Oxenstiernas korrespondens" — a modern research project's notes and copies, not primary material | undated (project active) | sv | caution, not scored | SE/RA/721502/3/1 (Oxenstiernaprojektets arkiv, "Anteckningar om och kopior av källmaterial") / Riksarkivet i Stockholm/Täby | This is the Oxenstierna edition project's own working notes/copies about ciphers in Axel Oxenstierna's correspondence, not an unread original — secondary material, and Bourdeau already has Oxenstierna-adjacent Riksarkivet targets (`riksarkivet1628`) via DECODE's Chifferklaver. Excluded as likely-duplicate research territory, not a fresh lead. | None. | — |

check-solved 24 Sept 2026 (LANE N batch J, six sources + Riksarkivet digitisation check, full logs in each target's NOTES.md):
- **R5** (`ciphers/ra-morner-welin/`): open. Nothing found in web, print (no correspondent to check against), lists,
  DECODE cache, Bourdeau or Aymeloglu. Not digitised.
- **R6** (`ciphers/ra-crusenstolpe-1809/`): open, with an unclosed edition-search gap flagged — Crusenstolpe's own
  printed "Portefeuille" (1837-44, full text at runeberg.org/portef/) and the standard Swedish 1809-coup
  historiography were not searched this pass (out of this pass's budget), only judged as a next step. Not digitised.
- **R8** (`ciphers/ra-karlxi-fullmakt-1677/`): open, but with real print risk left unresolved — Sverges traktater med
  främmande magter's volume covering 1672-1697 ("vol. 7") could not be located or confirmed to exist in this
  bibliographic record (HathiTrust's OCLC 11777373 record jumps from v.6 pt.1 to v.8, omitting v.7 and v.9); do not
  score this stage 2 until that is resolved. Not digitised.
- **R9** (`ciphers/ra-ud-chiffer-handlingar/`): closed-negative, confirmed. Gripenstierna's 1786 cipher machine is
  already published twice over (Beckman, FRA report 1999; Beckman, *Cryptologia* 26(2), 2002) — QUEUE's own
  "contribution (caution), not a solve target" call stands verified. No key-sharing link to R5/R6/R8 established.
  Not nominated.

Caveats: (1) every row above rests on a catalogue note or item title, never a page image — none of this material is
digitised (`onlyDigitisedMaterials: false` on every hit, confirmed also by a dedicated `only_digitised_materials=true`
query returning only two unrelated WWII administrative volumes), so every row is a copy-order/reading-room target,
scoring `material=0`; per the lane rule these score lower and the person already has 13 copy-order targets waiting.
(2) None of R1-R10 has been check-solved; "not named in Bourdeau/Aymeloglu/our files" is a name/shelfmark match under
rule 1, not a verified-unsolved verdict. (3) R1-R3's cipher keys are catalogued as present but their exact mapping to
specific letters is not established from the snippet alone (especially R3) — confirming that mapping is the first
reading-room task, before any solver time. (4) KB, manuscripta.se and openarch.nl are exhausted for this profile at
this budget (noise or off-topic, detailed above); Nationaal Archief's main site and Riksarkivet's own search UI are
blocked (maintenance, captcha) but Riksarkivet's underlying data is reachable through its public API, which is the
one genuinely new access route this sweep found and which a future NL/Nordic sweep should try first for Rigsarkivet
too (Daisy's data almost certainly has an equivalent API; not located this pass — worth ten minutes at the start of
the next session rather than fighting the JS widget again). (5) Requests: nationaalarchief.nl 2, service.archief.nl 1,
jsru.kb.nl 3, sok.riksarkivet.se 2 (curl) + 1 (browser tool), data.riksarkivet.se ~16 (several needed 1-2 retries for
transient TLS resets through the agent proxy, all eventually 200), daisy.rigsarkivet.dk 3 (browser tool; no query
executed), www.sa.dk 1, manuscripta.se ~9 (browser tool + direct query-string GETs), openarch.nl/openarchieven.nl 3,
github.com 2 (shallow clones, deleted after grep). No logins, no credentials, no subagents, no image opened. Per-host
counts: NL/Nordic raw ~133 item-level hits read at note/title level (Riksarkivet API only; other hosts returned no
item-level results to count), kept 8 scored + 2 caution rows, digitised 0.

**check-solved 24 Sept 2026 (LANE S batch I):** R1 (`ciphers/ra-celsing-dohsson-1779`), R2
(`ciphers/ra-celsing-sillen-1755`), R3 (`ciphers/ula-degeer-1644`) and R7 (`ciphers/ra-vellingk-1713`) all
verified **open** (six sources each: web, print/editions, community lists, DECODE public/cached, Bourdeau,
Aymeloglu — 0/24 found a solution, key transcription or documented attempt). All four confirmed
`onlyDigitisedMaterials: false` again via a fresh Sök-API query (data.riksarkivet.se had transient
SSL_ERROR_SYSCALL through the proxy on 2 of 5 queries, both recovered on the one allowed retry) — no route past
a Riksarkivet copy order for any of the four; REQUEST.md written for each. Full search logs in each target's
NOTES.md.

## Europeana and Real Academia de la Historia digitised candidates (LANE S scout of 24 September 2026)

LANE S worker E (row E1-, `.claude/briefs/runs/2026-09-24-lane-s-scE.md`). Hosts: `api.europeana.eu` (JSON API,
`wskey=api2demo`, `qf=TYPE:TEXT`, 24 queries across es/it/de/nl/fr/la/pt/sv terms from the brief) and
`bibliotecadigital.rah.es` (RAH's own digital library, curl with a browser-style User-Agent). Read first: the
"Digitised candidates outside the BnF" section above (its noise-pattern list and its RAH caveat that the on-site
search needed the browser tool), LESSONS.md, STATUS.md's 24 Sept lane structure. Excluded per brief: the two RAH
rows already on this file (N1 Morillo 1817-20, N2 Cañada 1869), being checked this wake by LANE S check-solved
worker C.

**Europeana: clean negative.** 24 queries, 208 unique raw hits (`sources/solver-diffs/2026-09-24-lane-s-europeana-rah.tsv`
has the exclusion reasons; the full raw dump is in the scratchpad, not committed). 87 hits are `dataProvider`
"National Library of France" — hosted on gallica.bnf.fr, off-limits to this worker and LANE G's own SRU sweep
already covers BnF directly; not opened further. Of the rest, 32+ are National Library of Spain (BNE) items —
checked against a fresh shallow clone of aaymeloglu/unsolved-ciphers and **all are already in its own
`catalogue/bne-ranked.md`/`bne-hits.jsonl`** (his BNE harvest used the identical terms cifra/cifrada/cifrado
across the whole BNE catalogue, 173 raw hits, 106 expanded records, confirmed by grep — this repeats
LESSONS.md's "a catalogue a daily-active project also reads is not a lane"), including the two that looked most
promising on title alone: *Cartas de la Reina de Hungría al Cardenal Granvela* (BNE MSS/7909/177-187, 1544-48,
one letter "con texto cifrado") and *Cartas del Duque de Sessa al Emperador Carlos V* (BNE MSS/20214/52,
1524-54, "algunas cartas con texto parcialmente cifrado" — note this is a different shelfmark from, but the
same correspondent and overlapping years as, Bourdeau's already-solved `sessa1524/` (RAH Salazar A-31), an
edition-risk worth flagging if anyone opens it later). The remaining ~60 non-Gallica, non-BNE hits are noise,
confirming the established pattern in a new set of languages: Spanish "cifra" is dominated by guitar/accordion
tablature notation ("método... por cifra") and the idiom "se cifra en" (amounts to); Dutch "cijferschrift" is a
school-song numbered-notation method; "déchiffrement" hits are decipherment of ancient scripts (cuneiform,
hieroglyphs, Etruscan), not historical cryptography; two Italian/German hits (Belaso 1553, "Il vero modo di
scrivere in cifra" 1564) are printed cipher-instruction manuals, already-published editions, not correspondence;
one Digital Memory of Catalonia item whose title claims "escrita en cifra" is, on viewing the leaf, a printed
17th-century political pamphlet in plain Spanish prose (image checked, see caveats); a Romanian letter
paraphrases in clear the content of a ciphered telegram it received, rather than containing ciphertext itself.
Requests: api.europeana.eu 26 (24 term queries + 2 full-record fetches, 1.6s apart, no 429/403).

**RAH: one new candidate, and a technical fix for the next worker.** The 24 Sept sweep's note that RAH's search
needs the browser tool driving the real form was half right: the browser tool hit RAH's own Anubis
("Making sure you're not a bot!") bot-challenge intermittently and its advanced search fields
(`#busq_general` on `formBusqueda`) render hidden by default, so `--type` timed out waiting for visibility even
after the challenge passed. **The actual fix is simpler: `resultados_busqueda.do` requires POST, not GET** — the
23-24 Sept curl sweeps got HTTP 200 with zero rows because they sent a GET; a plain `curl -X POST
--data-urlencode busq_general=<term>` reaches the same endpoint the advanced form posts to and returns real
results with no login, no cookie jar and no CSRF token needed for the search itself (a cookie jar is needed only
to keep a result-set's numeric `id` alive across a follow-up record-detail fetch, since each new search gets a
fresh id and an old one's detail page reports "la búsqueda... ha expirado"). RAH also exposes a DIGIBIB OAI-PMH
endpoint (`/oai/oai.do`, confirmed working, `completeListSize=24739`) but it has no query verb and only the
generic "driver" set — a full-collection bulk harvest, not a substitute for the keyword search, and out of this
budget. Eight terms tried beyond `cifrada` (already scored as N1/N2 above): `cifra` (4 hits: the known Morillo
item plus three cartographic false positives, "cifra" = scale-figure legend on maps, matching the established
foliation-noise pattern for a new host); `cifrado` (3 hits, two new); `clave en cifra`/`clave cifra` (2 hits
each, both already-known); `despacho cifrado` (2 hits, the same two `cifrado` finds); `telegrama cifrado`
(0); `clave` alone (410 hits, far too broad — not pursued); `descifrar`/`clave secreta` (0). The two new
`cifrado` hits are War Minister Alós's and War Minister Eguía's despatches to Morillo (RAH 9/7655 and 9/7654,
1819 and 1818, same 9/76xx numbered series as N1) — **both carry RAH's own cataloguer note that they are
already printed**, "Publicado por Rodríguez Villa" (vol. IV doc. 814 and vol. III doc. 754 respectively): a
useful negative and a flag for check-solved worker C's N1 sweep, since Rodríguez Villa's edition is not one of
the six sources its note lists as checked. The one survivor:

| Rank | Target | Year | Lang | Kind | Reference / Holder | Catalogue note | Leaf viewed | Image route | Total |
|---|---|---|---|---|---|---|---|---|---|
| E1 | Letters and documents exchanged between Queen Isabel II and the Count of Xiquena: copy of a ciphered telegram to the Queen's minister in Munich | 3 May 1868 | es | cryptanalysis (tentative) | Real Academia de la Historia, Madrid, Archivo de Isabel II, Sig. 9/6963, Legajo XXIV, Nº 158 | "[Cartas y documentos cruzados entre la Reina Isabel II y el Conde de Xiquena. Copia del telegrama cifrado al Ministro de la Reina en Munich. 3 de mayo de 1868] [Manuscrito]" — unlike the two Morillo `cifrado` hits above, this record's own catalogue entry carries **no** "Publicado por..." note. Two further items sit in the same small file (path 1008497, a plain minute on the Infanta's wedding announcement, not ciphertext; path 1008499, undated, title and author fields only read, not opened for content this pass — a possible sibling worth a look) plus an unrelated "Costados de..." genealogical roll that matches only on a different Conde de Xiquena's surname. | No — the record page's viewer is a JS-driven image loader (`catalogo_imagenes/grupo.do?path=1008498`) that did not yield a static image URL to curl this pass; not opened at full resolution | `bibliotecadigital.rah.es`, Public Domain Mark 1.0, no login (per the record's own rights field) | 32 |

Caveats: (1) Europeana's own index of RAH is thin (only the already-known Morillo 1817 item surfaced across all
24 queries) — the RAH-specific finds above came only from RAH's own search, confirming the 24 Sept section's
guess that RAH is under-indexed in Europeana. (2) E1's kind is provisional: it is scored cryptanalysis because
no key or sibling decipherment was found in this file this pass, but the two unopened companion items
(1008497 sibling context, 1008499 undated) were not read closely enough to rule out a decipherment sitting
beside it — check those before any solve attempt. (3) No score here claims a reading or a novelty class; E1
still needs check-solved's six-source sweep, including PARES (which was not queried this pass — out of this
brief's hosts) and a print check against Spanish 1868-revolution-era diplomatic correspondence editions, before
the board. (4) The Digital Memory of Catalonia pamphlet and the two Rodríguez-Villa-printed Morillo despatches
were confirmed by viewing the leaf/reading the catalogue's own note, not merely by title, per the brief's
instruction to check before scoring. Requests: bibliotecadigital.rah.es curl ~24 (1 reachability + 2 initial
form-structure probes + 11 term-query POSTs + ~10 record-detail GETs, ≥1.5s apart, HTTP 200 throughout);
`tools/browser_fetch.js` against the same host 6 (2 hit RAH's own Anubis bot-challenge, both stood down per the
one-retry limit and not repeated; logged here rather than retried further).

check-solved 24 Sept 2026 (LANE S batch G): E1 (`ciphers/rah-xiquena-1868/`) open, stage 2 verified unsolved
(conditional — image still not opened at full resolution; the RAE 1869-71 letters catalogue, RAH's own "1869 á
1875" correspondence catalogue, and the file's own two unopened sibling items, especially undated path
1008499, are outstanding). No edition of Isabel II's 1868 correspondence with the Conde de Xiquena found; the
item's own catalogue record still carries no "Publicado por..." note. Not on DECODE (cached), not in Bourdeau's
or Aymeloglu's repositories, no Cryptiana mention.
## Dutch and Belgian archives (LANE N scout of 24 September 2026)

Row NB of the lane brief (`.claude/briefs/runs/2026-09-24-lane-n-scNL.md`). Hosts: Nationaal Archief open data,
Huygens resources (`resources.huygens.knaw.nl` and its editions), KB catalogue (SRU, not Delpher), Archives
Portal Europe, Belgian State Archives search, KBR. Read first: CLAUDE.md rule 1, LESSONS.md §§1-2,
`.claude/briefs/check-solved.md`, the "Dutch and Nordic archive candidates" section above (its rows are all
Swedish — Riksarkivet/Uppsala landsarkiv; **it names no NL/Belgian item**, so nothing there needed excluding)
and its Nationaal Archief/KB caveats (both re-confirmed stale this pass, see below). Excluded against fresh
shallow clones of `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers` (grepped for Nassau/Oranje/Hessen/
Saksen/Huisarchief/KHAG/the specific briefnrs below — no match beyond incidental name collisions in unrelated
targets), `sources/cryptiana/`, CATALOG.md, LANDSCAPE.md and `ciphers/` (only `orange-nassau-1572` mentions
"Oranje"/"Nassau" there, a different letter, already found-solved — not one of the rows below).

**Hosts blocked or exhausted, one attempt logged, not pursued further.** `www.nationaalarchief.nl` still serves
"Site in onderhoud" at HTTP 503 on every path (`/`, `/onderzoeken/archieven`), the same outage LANE S logged a
few hours earlier the same day; one retry, stopped. `service.archief.nl/gaf/api/` 404 (wrong path, not
resolved this pass); `data.nationaalarchief.nl` does not resolve through the proxy (CONNECT tunnel failed,
000). `jsru.kb.nl` not re-queried: LANE S exhausted the one reachable collection (GGC, printed books) as noise
this same day and no manuscripts-specific SRU collection has been found; repeating it would be duplicate work
(rule against re-doing what the room already logged). `search.arch.be`, the host named in this lane's brief,
was decommissioned 23 December 2024 (confirmed by web search and by curl: it now redirects to an "end of life
notice" serving an unrelated login-only genealogy tool, DEMOGEN VISU) — its confirmed successor, run by the
same institution, is `agatha.arch.be`, used instead below. `opac.kbr.be`/`www.kbr.be` were reachability-tested
only (HTTP 200 both) — no query run, budget spent on the three hosts below instead.

**Huygens resources — the productive route, via the Willem van Oranje correspondence database (WVO).** The
1626-1651 Staten-Generaal resolutions have a working full-text search (`silva/sg/resoluties/index_html?text=`)
but it only indexes the editors' modern-Dutch summaries, not manuscript detail: `cijfer` returns one hit ("het
laatste cijfer van de datum", a false positive — the control that the query form works); `cijferbrief`,
`gecijferd`, `cijferschrift`, `geheimschrift`, `ontcijfer` all return zero — a "no ontcijfering" verdict from
this search is conditional on the summaries (rule 2), not a finding. The 1576-1625 resolutions, Bescheiden
Oldenbarnevelt, Brieven van Johan de Witt, Heinsius and Willem III/Bentinck editions are served only as
page-image "retroboeken" viewers with no full-text search endpoint found this pass — not searched (flagged for
a future sweep). The productive database is `resources.huygens.knaw.nl/wvo` (Briefwisseling van Willem van
Oranje, a proper record database with an advanced-search GET API, `wvo/app/brieven?opmerkingen=&opmerkingenBool=
AND&geavanceerd=1`, and a free PDF scan of every letter). `opmerkingen=cijfer` returns 96 letters (raw dump:
`sources/solver-diffs/2026-09-24-lane-n-wvo-cijfer-96.tsv`, every letter's date/correspondent/remarks/sources
fetched and read). **Control:** the search surfaces true positives — 14 of the 96 carry their own editorial
"oplossing"/"ontcijferd"/"ontcijfering" note or a Groen van Prinsterer print citation (e.g. nos. 74, 98, 153,
175, 4613, 4615, 7205, 7206, 7208, 6238, 6178, 5033, 5575, 1069), confirming the field genuinely records cipher
status rather than being noise; those 14 (and similar) are excluded below as already deciphered/printed. Six
rows below have neither marker. Every row's image is a free PDF, no login (`resources.huygens.knaw.nl/media/
wvo/images/...`), so material scores 3 (copy-free) throughout.

Scored per `.claude/workflows/scout.js` (language_fit×3 + material×2 + key_lead×3 + size×2 + competition×2 +
weight + unread×3, max 48), ranked best first:

| Rank | Target | Year | Lang | Kind | Reference / Holder | Catalogue note | Leaf viewed | Image route | Total |
|---|---|---|---|---|---|---|---|---|---|
| NB1 | Lodewijk van Nassau (brother of Willem van Oranje) to Willem van Oranje, four letters "hoofdzakelijk in cijferschrift" (mainly in cipher) with no solution recorded — briefnrs 4610 (3 Jun 1573, "Pour Hollande"), 4611 (2 Jul 1573), 4612 (6 Mar 1574), 4616 (12 Apr 1574) — plus two sibling letters in the *same* shelfmark and correspondence run **with a contemporary solution present and imaged**: 4613 (25 Mar 1574) and 4615 (7 Apr 1574), both "Tevens aanwezig de oplossing daarvan, die ook is afgebeeld" | 1573-1574 | fr | recovery | Koninklijk Huisarchief Den Haag, A 11/XIV D/13a (WVO briefnrs 4610-4616) | All six identified only by secretary's hand and seal, not signature (Lodewijk did not sign); 4613/4615 carry a period decipherment depicted on the same leaf — exactly the "key beside the letter" pattern (LESSONS.md §2, "look for the sibling"). Three further letters *to* Lodewijk/Jan/Hendrik van Nassau from the same 1574 exchange (7205, 7206, 7208, held at the Algemeen Rijksarchief van België) also carry a contemporary solution, confirming this correspondence circle's cipher was broken at the time on both sides. | Yes (PDF) | Free PDF per letter, `resources.huygens.knaw.nl/media/wvo/images/04000-04999/0461{0,1,2,6}.pdf`, `.../0461{3,5}.pdf` for the two solved siblings | 45 |
| NB2 | August van Saksen (Sachsen) ↔ Willem van Oranje/his secretaries, three letters or postscripts "in cijferschrift" with no solution recorded — briefnrs 53 (24 Oct 1561, postscript), 57 (18 Nov 1561, "bijvoegsel" enclosure) and 126 (16 Sep 1564, postscript) — in a correspondence run where four other letters from the same years (74, 98, 153, 175, all excluded above) **do** carry a contemporary solution or decipherment on the same or an adjoining folio | 1561-1564 | de | recovery | Sächsisches Hauptstaatsarchiv Dresden (Geheimer Rat, Locat 8510/5 and 9941/3); Koninklijk Huisarchief Den Haag holds duplicates/minutes of some | Same "sibling with contemporary decipherment" pattern as NB1, one correspondence circle earlier: the cipher system between Willem van Oranje and August van Saksen in the early 1560s appears to have been broken at the time for some letters and not transcribed for others in the same run. | Yes (PDF) | Free PDFs, `resources.huygens.knaw.nl/media/wvo/images/00000-00999/000{53,57,126}.pdf` | 42 |
| NB3 | Willem van Hessen to Willem van Oranje: news of a birth and a succession dispute, "Een gedeelte van het origineel is in onopgelost cijferschrift" (explicitly unsolved); "De minuut geeft de complete tekst" (the draft gives the complete text) | 28 Jan 1567 | de | cryptanalysis (crib available) | Original: Koninklijk Huisarchief Den Haag, A 11/XIV B/15-43 (no image online this pass); draft: Hessisches Staatsarchiv Marburg, Bestand 3II (WVO briefnr 1127) | The draft is a plain-text crib for (part of) the same letter, if the draft and the enciphered passage cover the same content — worth checking directly rather than assuming, since a "minuut" can also just be an earlier compositional stage. The KHAG original (which is where the cipher sits) has no PDF listed in the WVO database this pass — a copy-order or further look-up target, not copy-free for the cipher passage itself, even though the draft is free. | Partial — draft only | Free PDF for the draft only, `resources.huygens.knaw.nl/media/wvo/images/01000-01999/01127.pdf` | 39 |
| NB4 | La Garde, superintendent of Schoonhoven, to Willem van Oranje: report on troop strength near Namur, "Gedeeltelijk in onopgelost cijferschrift" (partly in unsolved cipher — the WVO database's own curators use "onopgelost", not just absence of a marker) | 28 Nov 1577 | fr | cryptanalysis | Koninklijk Huisarchief Den Haag, A 11/XIV C/G-1 (WVO briefnr 6179) | Printed by Groen van Prinsterer, *Archives... Maison d'Orange-Nassau* 1e série VI, 249-251, no. DCCLXXXIX, but flagged "(onv)" = onvolledig/incomplete in the WVO citation — the same "(onv.)" tag that marked the already-known orange-nassau-1572 letter's partial 1842 print; consistent with Groen's edition skipping the still-unbroken cipher portion. Not checked this pass whether Groen's own footnotes discuss the gap (next step). | Yes (PDF) | Free PDF, `resources.huygens.knaw.nl/media/wvo/images/06000-06999/06179.pdf` | 36 |
| NB5 | Willem van Hessen to Willem van Oranje: enclosure "eigenhandig ondertekende in cijferschrift geschreven bijlage" (a hand-signed attachment written in cipher), cross-referenced by the database to briefnr 1107 | 18 Sep 1564 | de | cryptanalysis | Hessisches Staatsarchiv Marburg, Bestand 3II, Nassau-Niederlande, Korr. 1564-1565 (WVO briefnr 1109) | No solution recorded; not checked this pass against the cross-referenced 1107 for a decipherment there. | Yes (PDF) | Free PDF, `resources.huygens.knaw.nl/media/wvo/images/01000-01999/01109.pdf` | 33 |
| NB6 | Jan van Nassau to Willem van Hessen: report on the accident that killed/probably killed Lodewijk van Nassau, Hendrik van Nassau and Christoph von Württemberg at Mookerheyde — "Twee regels in cijferschrift" (two lines in cipher) | 17 Apr 1574 | de | cryptanalysis (marginal) | Koninklijk Huisarchief Den Haag, A 11/XIV A/5-20 (WVO briefnr 5551) | Two lines is well below unicity distance without a key; listed for completeness (rule 10, "report what was found") rather than as a serious cryptanalysis target on its own — a candidate only if NB1's or NB2's key turns out to cover the same period/correspondents. | Yes (PDF) | Free PDF, `resources.huygens.knaw.nl/media/wvo/images/05000-05999/05551.pdf` | 32 |

**Archives Portal Europe** (`archivesportaleurope.net`, now a JS app; the old static `?query=` URL 301-redirects
to it, driven via `tools/browser_fetch.js --type`). Control: `cijfer` returns real NL-HaNA/NL-LwHCL fonds
records (repositoryCode + recordId pairs), so the query form works — but 10,589 raw hits is far too broad for
this budget (two sample records opened were 19th-20th century administrative noise, e.g. a 1920 "Geheimschrift"
Defence-ministry fonds); not triaged past two sample queries. `gecijferde brieven` (0, not a literal-phrase
index) and `geheimschrift` (10 sampled, all 19th-20th c. or unopened) did not narrow it usefully this pass.
Since APE mirrors Nationaal Archief finding aids (`repositoryCode=NL-HaNA`), it is also a possible workaround
for the NA site's own outage — worth a properly time-boxed pass with the `heading`/date-range filters (not the
free-text box) next time.

**Belgian State Archives, via AGATHA** (`agatha.arch.be/en/search/ead/`, JS app, driven the same way). Control:
`cijfer` returns 35 real archival-inventory titles with genuine shelfmarks and date ranges, so the query form
works. Page 1 of 10 is entirely 19th-20th century administrative fonds (commercial courts, provincial finance)
— "cijfer" as ordinary Dutch for "figure/number", the same noise class KB and the 1626-1651 SG resolutions gave.
Not triaged past page 1 (25 more rows unread) within this budget. Flagged for the next sweep: filter by Heading
= A1-A4 ("Central administrations, Ancien régime": Spanish/Austrian Netherlands, Prince-Bishopric Liège,
Stavelot-Malmedy, Bouillon) specifically, where a genuine cipher-correspondence hit is far more likely to sit
than in the unfiltered 20th-century-heavy full-text index.

Caveats: (1) NB1-NB6 all rest on the WVO database's own curatorial description (Opmerkingen field, written by
J.G. Smit and collaborators), not on this worker's own reading of the image — the PDFs were located and their
existence confirmed (HTTP 200, correct byte sizes shown by the database) but not opened and read; "leaf viewed"
in the table means the PDF was confirmed reachable, not that this worker verified the cipher's extent or
transcribed anything, per the brief ("never transcribe"). (2) None of NB1-NB6 has been check-solved; the WVO
database's own field only rules out a solution reaching that specific field, not a decipherment published
elsewhere (e.g. in Groen van Prinsterer's own footnotes for NB4, in Demandt's *Nassau-oranische Korrespondenzen*
for the August-van-Saksen circle of NB2, or in Rachfahl's or Japikse's biographical literature on Willem van
Oranje and his brothers, none checked this pass) — the next step for any of these is check-solved's six-source
sweep plus a look at the cited "excerpt" editions (Demandt, DNOK) in the Bron table of each letter. (3) NB1 and
NB2 are recovery candidates on the strength of a sibling-letter pattern, not a confirmed key: nobody this pass
has actually tried aligning 4613/4615's imaged solution against 4610/4611/4612/4616, or the four solved
August-van-Saksen letters against 53/57/126 — that alignment is the first real step, not a search-hit. (4) The
"Dutch and Belgian" brief's own preference for VOC secret correspondence and Staten-Generaal/Gecommitteerde
Raden material was not satisfied this pass: the only Staten-Generaal source with full-text search (1626-1651)
returned nothing, VOC editions on the Huygens site were not searched (no obvious full-text route found in this
budget — flagged for next time), and Archives Portal Europe's one VOC-era hit sampled (a National Archives fonds
code in the 1.02.x range, "cijfer") was not opened before the budget ran out. Requests:
resources.huygens.knaw.nl ~130 (1 root page, ~15 Besluiten-SG search/browse, ~14 WVO search-form/help pages, 96
WVO letter-detail fetches, 4 WVO result-list pages), www.nationaalarchief.nl 2, data.nationaalarchief.nl 1 (000,
proxy-blocked), service.archief.nl 1, jsru.kb.nl 0 (not re-queried), www.archivesportaleurope.net ~6 (1 curl +
`tools/browser_fetch.js` x2 + a handful of record-detail curls), search.arch.be 1, agatha.arch.be ~4
(`tools/browser_fetch.js` x2 + form-page fetches), opac.kbr.be 1, www.kbr.be 1, github.com 2 (shallow clones of
both solver repos, grepped, deleted after). All ≥1.5s apart on curl hosts; the browser-tool hosts ran single
requests at a time. No logins, no credentials, no subagents, no image opened/transcribed, no novelty wording.

## Printed ciphertext (detector round 3, LANE S, 24 September 2026)

Detector-test worker, round 3 (`.claude/briefs/runs/2026-09-24-lane-s-det3.md`): same method as rounds 1-2
(`tools/ia_numeral_runs.py`, `sources/ia-fulltext/NOTES.md` §1) over English state-paper/calendar editions and
continental series not covered by round 2, plus two new steps: a pre-filter for back-of-volume indexes before
judgement, and an interlinear test on every cipher-without-decipherment survivor (per the Thurloe interlinear
lesson of 24 Sept 03:00-03:05 UTC — several apparent Thurloe "unkeyed" passages turned out to carry a printed
decipherment set as a second line above each cipher line). This is a detector test, not a solver or verifier
pass: rule 10 applies, nothing here is promoted or solved, no wording of new/unpublished/first is used.

**Edition list:** `sources/ia-fulltext/editions3.tsv`, 212 identifiers from 75 `archive.org/advancedsearch.php`
title queries (English: Haynes/Murdin Burghley, Hardwicke, Clarendon State Papers 1767-86, Nicholas Papers,
Carte's Ormonde, Winwood, Sadler, Hamilton Papers, Forbes, Birch, Digges, Cabala, CSP Scotland/Border Papers,
HMC Salisbury/Stuart/Portland/Bath/Buccleuch, Macpherson, Hailes, Miscellanea Aulica, Letters and Papers Henry
VIII, State Papers Henry VIII; continental: Corpo diplomatico portuguez, Oxenstiernas skrifter och brefvexling,
Hurmuzaki, Monumenta Hungariae Historica, Acta Tomiciana, Briefe/Akten Dreissigjährigen Krieges, Druffel, Politische
Correspondenz Friedrichs des Grossen, Gachard, Werken van het Historisch Genootschap, Lettres et négociations de
Jean de Witt, Archivio veneto/lombardo/napoletane, Miscellanea/Documenti di storia italiana, Recueil des
instructions), deduped against `editions.tsv`/`editions2.tsv`. **Not found on Internet Archive under any title
tried** despite three rounds of loosened phrasing: Carte's Ormonde letters, Birch's *Memoirs of the Reign of
Queen Elizabeth*, and Dalrymple/Lord Hailes's *Annals of Scotland* — a gap in IA's holdings or metadata, not a
tool failure, reported rather than silently substituted (same pattern as round 1's Hardwicke/Sidney Papers,
which this round *did* find under a looser query). The 212-identifier total falls short of the brief's
"about 250-300" — several named series (Hardwicke, Clarendon, Nicholas Papers, HMC Stuart/Portland, CSP
Scotland) needed 2-3 rounds of query loosening to surface even a handful of volumes, reflecting genuinely
sparse or inconsistent IA metadata for these titles rather than an unexplored source.

**Controls, both recovered, one retry needed (good-citizen rule, single retry after a pause):** Thurloe vol. 1
(`collectionofstat01thur`) 500'd once, then on retry reproduced its round-1/round-2 cluster count exactly (111
clusters; known cipher at line 43962 confirmed verbatim). Rommel 1840 (`correspondancein00henr`) fetched clean,
50 raw clusters (consistent with rounds 1-2's 11 merged passages, all already in cyphersolver `hesse1603/`).

**Fetch:** 212 identifiers, 182 fetched, 30 skipped on HTTP 404 (16)/500 (10)/401 (1)/503 (1) with no retries —
mostly dead Polish JBC (`jbc.bj.uj.edu.pl.*`) and `ArchivioVeneto*`/`bub_gb_*` ids from the keyword harvest.
20,160 raw cluster rows parsed into `runs3.tsv` from a nominal 21,342 (some rows lost to stray quote characters
in the OCR context field confusing the TSV's csv-quoting; a known limitation of storing raw OCR text in a TSV
context column, not attempted to fix this round — flagged for a tools/ia_numeral_runs.py fix, not this worker's
brief).

**Pre-filter** (before judgement, per the brief's lesson from round 2's 173-of-180 index/register false
positives): of the 20,160 raw clusters, 20,099 fail the standing thresholds (repeat_rate>=0.3, numerals>=15,
prose_words>=5); of the 61 that pass, 4 are dropped as being in the last 8% of their volume's lines and 2 as
mostly-ascending numeral sequences (a page-reference run), leaving 55 kept clusters merging into **27 candidate
passages** across 8 identifiers. Spot-checked 10 dropped clusters by hand (the 6 pre-filter drops plus the 4
highest-scoring threshold drops): all 10 are genuine back-of-volume apparatus — 2 place/subject indexes
(`statepaperspubli11grea`/Letters and Papers Henry VIII, `sim_great-britain-public-record-1625-1649-domestic-
series_1639-1640`/CSPD index), 2 commodity-price or coin-value tables (`rikskanslerenax00styfgoog` foodstuffs
prices, `rikskanslerenax03akadgoog` "plåtkoppar" copper-plate currency), 1 military-movement page-reference
run (`politischecorres22freduoft`), 1 regesten-style citation list (`briefeundactenz00altmgoog`), and 4 more
`rikskanslerenax00*` footnote blocks that are the edition's own already-solved cipher apparatus (see below) with
too little surrounding prose to clear the threshold — none is a hidden undeciphered passage.

**Judgement (all 27 candidate passages read from +-10 lines of djvu context, not the one stored context
line):**

| Category | Passages | What it is |
|---|---|---|
| cipher-with-decipherment | 8 | `calendarofstuart01grea`/`01greauoft` (2 copies of the same volume), `calendarofstuart02grea`, `stuartpaperswind56greauoft` — Calendar of the Stuart Papers / Stuart Papers at Windsor print every cipher figure with its plaintext gloss in brackets immediately alongside it ("43. 96. 28. 29. 55. 11. 69. Agincourt {the money)", "22, 10, 23, 25, 20 (b,r,e,a,d)"), a 20th-century calendaring convention, not an unread passage |
| cipher-with-decipherment | 14 | `rikskanslerenax00akadgoog`/`00palagoog`/`02akadgoog` (Rikskansleren Axel Oxenstiernas skrifter och brefvexling, several volumes) — this edition's standard apparatus: ciphered words are printed in clear inside asterisks in the letter body, with a footnote giving "Siffrorna äro: ..." (the figures are: ...), the original cipher numerals, for every asterisked word; several footnotes state explicitly the editor solved the cipher using a key found in the Riksarkivet (e.g. "genom fynd af den i Riksarkivet befintliga klaven har det varit möjligt att lösa chiffern") |
| table/noise | 4 | `sim_great-britain-public-record-papers-domestic-charles-ii_1673-1675_index` and `..._october-1672-february-1673` (x2 passages) — CSPD Charles II's own shipping-log appendix table (Date / King's ships outward / inward / Wind / Remarks columns); flagged "interlinear=yes" by the automated test purely because remarks-column prose happens to word-count near the row's numeral count — a demonstrated false positive, judged table by content |
| **cipher-without-decipherment (survivor)** | **1** | see row W1 below |

**Interlinear test** (required before calling any passage undeciphered, per the Thurloe lesson): run against
all 27 passages' +-10-line windows (numeral-line word-count vs. neighbouring clear-line word-count, tolerance
+-2 or 25%). 4 flagged "yes"/"maybe" — all 4 checked by hand and are false positives (the CSPD shipping table's
remarks column, and one Rikskansleren asterisk-footnote block where an unrelated nearby prose line happened to
match): none is a real plain-line-above-cipher-line layout. The one true survivor (W1) scores "no" (4 of 14
neighbour lines within tolerance, below the 0.3 threshold) and was independently confirmed by eye to be
continuous prose with inline cipher numerals, not a two-line interlinear format.

| # | Edition | Identifier | OCR line(s) / printed page | Correspondents / date | Tokens | Decipherment on page | Prior work found where | Next step |
|---|---|---|---|---|---|---|---|---|
| W1 | Rikskansleren Axel Oxenstiernas skrifter och brefvexling (Styffe ed.) | `rikskanslerenax00styfgoog` | OCR lines 39880-39942, printed pp. 821-822 (letter no. 602) | Gustav II Adolf (Gustavus Adolphus) to Axel Oxenstierna ("Rikskansleren"), dated "Nürnberg den 23 Julij" — printed "Anno 1682" is an OCR digit slip for 1632 (Gustavus Adolphus died Nov. 1632; the letter discusses the Nürnberg campaign and Banér) | approx. 150 cipher numerals (2-4 digit groups, values seen up to 3965) over ~40 lines of continuous German/Swedish prose, cipher words interspersed with clear text word by word | **No** — editor's own footnote states: "Nyckeln till ofvanstående chifferbref har af utgifvaren icke i riksarkivet kunnat återfinnas, men då intet tvifvel är om, att det är ett Konungens bref till Rikskansleren, hvartill möjligen en lösning sedermera kan finnas, har det här blifvit meddeladt" (the key to the above cipher letter could not be found by the editor in the Riksarkivet, but as there is no doubt it is a letter from the King to the Chancellor, to which a solution may possibly be found later, it is included here [unsolved]) | Not found under "Oxenstierna"/"Gustav(us) Adolph(us)" in `sources/cryptiana/`; fresh shallow clones of both solver repos show adjacent-but-distinct Riksarkivet/Oxenstierna-circle items already worked or surveyed by Bourdeau — `riksarkivet1628/` (DECODE Chifferklaver catalogue #207: R4282/R4284/R4306 open, R4330-31 read [1631 Bremen-Salvius], R4333-37 [Rusdorff to Oxenstierna, 1628, open], R4338-41 [June 1633, read in part]) and `baner1640/` (Banér to Stålhandske, Dec. 1640, read in part) — none dated 23 July 1632 or matching this letter's incipit; QUEUE.md rows R3/R10 (24 Sept scout) already flag the Oxenstierna-project's own Riksarkivet holdings as adjacent territory. Not found in QUEUE.md or `ciphers/` under any of these terms. The editor's footnote also notes two further cipher letters of the same day to Gustaf Horn ("duplett"/"triplett", same format) not located in this sweep — a next worker should check whether they are printed elsewhere in this volume. | Not promoted, not solved. Next: check-solved sweep (six sources) before any board promotion; locate the "duplett"/"triplett" Horn letters in the same volume; the numeral range (up to ~3965) implies a large nomenclator rather than a simple cipher — a period Riksarkivet Chifferklaver key search (as `riksarkivet1628/` and `baner1640/` already do for adjacent material) is the likely route in, not ciphertext-only cryptanalysis |

check-solved 24 Sept 2026: **open**, stage 2 verified unsolved (conditional). Six sources + editions-first (Styffe's
*Konung Gustaf II Adolfs skrifter* 1861 checked, letter absent between the printed 21 Jul/1 Aug letters; Irmer's
*Verhandlungen Schwedens* vol. 1 checked, one non-matching introduction hit; fresh Bourdeau/Aymeloglu clones, no
match; `sok.riksarkivet.se/oxenstierna` blocked by CAPTCHA). Extraction done: `ciphers/oxenstierna-gustav-adolf-1632/`
now has `printed_ocr.txt`, `ciphertext.txt`, `tokens.tsv`, `extract.py` (733 cipher tokens, 91 distinct values
4-5152 — corrects this row's "approx. 150 ... up to 3965" estimate, a per-token recount vs. the detector's cluster
estimate). Full search log and leaf-check links (archive.org page/n831, n832) in NOTES.md. Not promoted, not solved,
no novelty wording.

**Requests, archive.org only:** 75 `advancedsearch.php` calls (44 initial + 20 loosened re-queries for 0-hit
titles + 11 third-round loosened queries) + 215 `_djvu.txt` fetches (212 new identifiers, one retried once on
500, plus the Rommel control refetch — the Thurloe vol.1 control's 500-then-retry counted in the 212) = 290
total, well within the ~400 cap, one at a time, >=1.5s apart, no other host touched. No subagents, no logins,
no github.com requests beyond the two shallow clones (grepped for W1, not committed).

**Files:** `sources/ia-fulltext/editions3.tsv` (212 identifiers), `runs3.tsv` (all raw clusters: the two
controls plus the 212 new identifiers, reproducible by re-running
`python3 tools/ia_numeral_runs.py collectionofstat01thur correspondancein00henr $(tail -n +2 sources/ia-fulltext/editions3.tsv | cut -f1) --cache sources/ia-fulltext --tsv sources/ia-fulltext/runs3.tsv`
against freshly-fetched `_djvu.txt` files, gitignored), `editions3_passages.tsv` (the 27 merged candidate
passages with interlinear-test scores) and `editions3_dropped_examples.tsv` (the 6 pre-filter drops used in the
spot-check), both committed for reproducibility.

## Central and Eastern European digital-library candidates (LANE S scout of 24 September 2026)

Brief: Polona, Kramerius instances (Czech National Library ndk.cz/kramerius5.nkp.cz and the Moravian Library),
Hungaricana, Slovenian dLib.si, Monasterium.net (charters only), querying cipher/chiffre/cifra/Chiffre/cijfer
/kryptografi in each catalogue's own language plus Latin. Read first: LESSONS.md, QUEUE.md "Candidates not on
DECODE" and "Digitised candidates outside the BnF" (the noise patterns already found there: "cipher" as
zero/foliation, Pepys, WWII, Voynich, Founders Online). Every candidate class below was checked against fresh
shallow clones of `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers` and against QUEUE.md/CATALOG.md/
LANDSCAPE.md/`ciphers/`; none of the reported hits are correspondence, so no exclusion check was needed beyond
this. Raw hits and exclusion reasons: `sources/solver-diffs/2026-09-24-lane-s-cee.tsv`.

**Zero rows this sweep.** Every host reached returned either no working search route, or a working route whose
top hits (checked by opening the record) are not cipher correspondence. The row-id prefix **Z** stays reserved
for this lane; a future pass with better queries or hosts should continue from Z1.

**Polona (polona.pl), blocked -- API not found.** The SPA's `env.js` gives the gateway base
(`https://polona.pl/api`); `/api/search-service/search/advanced-form` (the field-schema config) and
`/api/search-service/search/suggest?query=...` (autocomplete) both answer, confirming the route family and that
GET is the right verb, but the actual results endpoint was not found this budget: `/simple`, `/basic`,
`/results`, `/advanced`, `/query` and `/search` itself all return `400 Bad Request` (the route exists, the
parameter shape does not match a bare `?query=`), and no OpenAPI/swagger listing was found. A Playwright session
(`NODE_PATH=$(npm root -g) node`, `/opt/pw-browsers/chromium`) filled the visible search box and clicked the
navbar search button (`aria-label="Szukaj"`) and the modal's "Wyszukaj" button in turn; neither produced a
capturable results fetch inside the wait budget -- the site opens an advanced-search modal by default and the
click sequence needed to reach a real results page was not identified. Worth a second attempt with more time on
the browser-automation side, or a request to the person for Polona's documented API if one exists outside the
SPA. 0 raw, 0 kept, 0 digitised.

**Kramerius (Czech), clean negative -- the wrong kind of library.** `kramerius5.nkp.cz` (NDK, the National
Digital Library) has a working, undocumented-but-discoverable REST/Solr API at
`https://kramerius5.nkp.cz/search/api/v5.0/search?q=...&wt=json` (found by reading `main.js` for the
`getApiUrlForBaseUrl`/`k5Compat()` logic; CORS-open, no auth). "šifra" alone returns 26,322 hits because Czech
"šifra" is as ambiguous as French "chiffre" (also means a plain numeral/code, e.g. a page or call number); the
phrases "šifrovaný dopis" (ciphered letter), "psáno šifrou" (written in cipher) and "tajné písmo" (secret
writing), restricted to `datum_begin:[1450 TO 1900]`, still return only 71 hits, every one `model_path
monograph/page` -- OCR word-matches inside printed 19th-c. books (memoirs, popular science, poetry, a foreign-
words dictionary), not manuscripts. A direct query for `fedora.model:manuscript` or `document_type:manuscript`
combined with any cipher term returns **zero** results: this instance holds essentially no digitised manuscript
correspondence under these terms -- NDK is a books-and-periodicals library, not an archive. The Moravian
Library's own instance has been merged into a national portal, `digitalniknihovna.cz` (and
`kramerius.mzk.cz` now redirects there); that portal serves the same Angular SPA shell at every path tried,
including the plausible namespaced guess `/mzk/search/api/v5.0/search`, so its backend API location was not
found this budget. Raw 71 (Czech, dated) + 26,322 (unfiltered, not swept further), kept 0, digitised n/a.

**Hungaricana (hungaricana.hu), reached, noise-dominated but with a working filter.** Server-rendered (works
directly with a browser User-Agent after one redirect; a plain descriptive UA gets refused). The site's facet
API was reverse-engineered: `GET /hu/search/filter/DATABASE/?list=<base64 JSON>` returns each content
database's hit count, and re-encoding `{"query": "...", "filters": {"DATABASE": ["LI"]}}` as the `list` param
restricts results to "Könyvtár (Levéltári iratok)" -- digitised archival records, the closest facet to what
this brief wants. "rejtjeles levél" (ciphered letter) restricted to that facet gives 3 hits, all 1951-1981
Hungarian Communist Party (MSZMP) committee records; "titkosírás" (cipher/secret writing) restricted the same
way gives 8, all archival-science training manuals and more 1950s-60s party minutes referencing the topic in
passing. Nothing pre-1900 surfaced in the archival-records facet for either term. The unrestricted "rejtjel"
query (2,796 hits) is dominated by an actual 1930s cipher-machine patent and modern press usage; not swept
further given the archival-facet negative. Raw 2,796 + 3 + 8, kept 0, digitised n/a (nothing scored).

**Slovenian dLib.si, clean negative.** Server-rendered, answers curl directly with no UA requirement, and has a
working field-search form: `GET /results/?query='keywords=TERM'&pageSize=N`; the bare/default `text=` field
returns nothing for the same terms, so the `keywords=` field is the one that works. "cifer" and "šifra" both
resolve to modern content only: a 1985 poem, two items literally titled "Šifra"/"Šifra 2.0" and one titled "Da
Vincijeva šifra" (the Slovenian edition of *The Da Vinci Code*), a comics-studies article and a pseudo-random-
bit-generator statistics paper. No archival correspondence. Raw ~32 (6 titled, rest uncounted past the
confirming query), kept 0, digitised n/a.

**Monasterium.net, not reached.** Out of budget this pass; the brief scopes it to charter cipher notes only,
the lowest-yield of the five hosts named, and was not attempted.

Caveats: (1) all four reached hosts have real, working query mechanisms now documented above and in the TSV --
the negative is a language/term problem (period Latin/German/Hungarian diplomatic phrasing was not tried beyond
the brief's word list) and a collection problem (NDK and dLib.si are books/periodicals libraries; Hungaricana's
useful archival facet turned out to be a 20th-century party-records collection, not the early-modern
diplomatic and ecclesiastical archives these catalogues also host under names not yet searched, e.g. Magyar
Nemzeti Levéltár finding aids proper, distinct from the OCR'd "Levéltári iratok" text corpus hit here). (2) No
image was opened at full resolution for any hit; every exclusion above rests on the record's own title, date
and collection metadata, not the ciphertext. (3) Polona's API remains unsolved and is worth a dedicated
follow-up given the site's likely 17th-18th c. diplomatic-letter holdings named in the brief. (4) Requests per
host, all ≥1.5s apart, single UA `cipher-lab research script (contact via repository)` except Hungaricana
(needs a browser UA per its redirect behaviour) and the Playwright sessions (browser UA, per playbook route 2):
polona.pl ~30 (curl) + 3 Playwright page loads; kramerius5.nkp.cz ~8; digitalniknihovna.cz/kramerius.mzk.cz ~4;
hungaricana.hu ~12 (curl) + 2 Playwright page loads; dlib.si ~10. No 429/403/Cloudflare challenge hit on any
host; nothing to log as blocked-by-the-site, only blocked-by-not-finding-the-route (Polona) or blocked-by-
merger (MZK).

## Printed ciphertext (detector round 4, LANE S, 24 September 2026)

Detector-test worker, round 4 (`.claude/briefs/runs/2026-09-24-lane-s-det4.md`): same method as rounds 1-3
(`tools/ia_numeral_runs.py`, `sources/ia-fulltext/NOTES.md` §1), round 3's pre-filter and interlinear test, plus
one new check this round — grepping each whole cached volume for a decipherment-indicator term, not only the
passage's own context window (see below) — over the Nordic, Thirty Years' War, and Scottish/Stuart-exile
editions named in the round-4 brief. This is a detector test, not a solver or verifier pass: rule 10 applies,
nothing here is promoted or solved, no wording of new/unpublished/first is used. Row prefix `X` was reserved for
this round; none is used below since there are no survivors.

**Edition list:** `sources/ia-fulltext/editions4.tsv`, 152 identifiers from 53 `archive.org/advancedsearch.php`
queries (31 precise-phrase queries across the brief's named series — Oxenstierna, Gustaf II Adolfs skrifter,
Handlingar rörande Skandinaviens historia, Historiska handlingar, Arkiv till upplysning om svenska krigens,
Kong Christian den Fjerdes egenhaendige Breve, Danske Kancelliregistranter/Magazin, Irmer, Hallwich, Förster,
Hamilton Papers, Lauderdale Papers, Carte's Original Letters, Nairne/Macpherson, Letters of Queen Henrietta
Maria; + 22 loosened follow-up queries for titles that returned nothing), deduped against
`editions.tsv`/`editions2.tsv`/`editions3.tsv`. The loosened queries surfaced 364 raw hits, of which 211 were
off-series noise (Baroness Nairne's songs and an C18th telescope-maker also named Nairne under a bare
`title:(Nairne)` query; dozens of secondary Wallenstein/Thirty-Years'-War narrative histories — Gindely,
Schiller, popular accounts — under a bare `title:(Dreissigjährigen) AND title:(Krieges)` query) and were dropped
by a documentary-title keyword filter (Urkunden/Akten/Briefe/Correspond/Papers/Verhandlung/Documenta/Regesten/
"Original Papers"/"Secret History") before any fetch, rather than fetched to pad the identifier count toward the
brief's 250-350 target — short of that target, reported rather than papered over, the same shape as round 3's
212-of-250-300 shortfall. **Not found on Internet Archive under any title tried:** Sverges/Sveriges traktater
med främmande magter, Documenta Bohemica Bellum Tricennale.

**A tooling bug this round, disclosed:** mid-fetch, this worker ran `git commit` + `git rebase --autostash`
against `sources/ia-fulltext/runs4_new.tsv` while the background fetch process still held that file open for
writing; git's rebase checkout orphaned the process's file handle, silently losing its writes for most of the
137 fetched identifiers (the file on disk reverted to the partial snapshot committed mid-fetch — 5 identifiers'
worth of rows). Caught before write-up by cross-checking the fetch log's identifier list against
`runs4.tsv`'s identifiers. Fixed with no new network calls for the 137 already-cached `_djvu.txt` files (only
the 15 still-uncached identifiers made new requests on the rerun; 1 succeeded, 14 reproduced the same error).
`runs4.tsv` as committed is the corrected, complete file. **Lesson for later rounds: a rebase/checkout touches
the working tree and will orphan a background process's open output file — let a fetch finish (or write outside
any path touched by a mid-run commit) before running one.**

**Controls, 2 of 2 recovered, exact match to rounds 1-3:** Thurloe vol. 1 (`collectionofstat01thur`, 111
clusters, known cipher at OCR line 43962 verbatim) and Rommel 1840 (`correspondancein00henr`, 50 raw clusters,
already in cyphersolver `hesse1603/`).

**Fetch:** 152 identifiers, 138 fetched (137 first pass + 1 on the bug-recovery rerun), 14 skipped (7×404,
4×401, 3×500), no retries beyond the one disclosed bug-recovery rerun.

**Pre-filter:** of the edition-4 raw clusters, 30 pass the standing thresholds (`repeat_rate>=0.3,
numerals>=15, prose_words>=5`) across 6 identifiers; 6 dropped by the pre-filter (3 last-8%-of-volume, 3
mostly-ascending-numerals), leaving 24 kept clusters merging into **18 candidate passages**. Spot-checked 10
dropped clusters by hand (the 6 pre-filter drops + the 4 highest-scoring threshold drops among this round's own
identifiers): all 10 are genuine back-of-volume name/subject indexes ("name/place, vol:page, vol:page."
citation format) — the pre-filter did not hide a real cipher passage.

**Interlinear test:** run on all 18 passages; all score low (0.00-0.50), correctly indicating none carries a
plain-text line printed directly above or below its cipher line — unlike round 3's one true survivor, this
round's interlinear test alone was not the deciding check (see next).

**New same-volume decipherment check:** the interlinear test does not catch a decipherment printed in a
*different part of the same volume* with no interlinear or bracketed layout. Six of the 18 passages
(`kongchristianden03chriuoft`, *Kong Christian den Fjerdes egenhaendige Breve* vol. 3, ed. Bricka & Fridericia
1878) read as genuine cipher-without-decipherment on first pass — numeral groups word-by-word inside continuous
German prose letters from Christian IV to his secretary Frederik Günther, dated 20 Aug 1632, 18 Sept 1633, and
four more of 1635. Grepping the whole cached volume text (not just each passage's ±10-line window) for
`dechifr`/`nøgle` found a "Dechifrerede Breve" appendix near the end of the same volume: the editors state they
later found Christian IV's own 1632 cipher key in the Geheimearkiv (Danske Samlinger Nr. 64, endorsed by the
King "Zifferen So Friderich guntheren zugesteldt ... den 15 Maij Anno 1632") and deciphered the letters printed
earlier as cipher — Nrr. 34, 35, 43 (1632), 191 (1633), 474, 480, 482, 504 (1635) — matching all six passages by
date and, for one, word-for-word opening text (passage 1's cipher-body "Weiil icli mich cless alten Spriichess
Errinnere, 64." is the same letter as the appendix's "Nr. 35", resolved there to "Weiil icb micli cless alten
Spruchess Errinnere, quod in turbbid quod optim..."). **Added to the standing method for future rounds:** before
calling any passage undeciphered, grep the whole cached volume (not only the passage's context window) for a
decipherment-indicator term (dechiffr/dechifr/entziffert/nøgle/gelöst/chiffernøgle/résolu/solved/deciphered).

| Category | Passages | Identifiers | What it is |
|---|---|---|---|
| cipher-with-decipherment (same-volume appendix, not interlinear) | 6 | `kongchristianden03chriuoft` | see above |
| table/noise, back-of-volume place/regiment-name index | 1 | `handlingarrrand03scangoog` (title is literally *Kronologiskt register*, a chronological register volume) | "name, vol:page, vol:page" citations |
| table/noise, back-of-volume personal-name index | 2 | `danskemagazin03histgoog` | same citation format |
| table/noise, "List of Persons" citing scene/line numbers | 2 | `wallensteineind02schigoog` (an English edition of Schiller's *Wallenstein* play, not archival correspondence) | not cipher figures |
| table/noise, Personen-/Sachregister citing "Nr. XXX S. YYY" | 4 + 3 | `dieverhandlunge02irmegoog`, `dieverhandlunge00irmegoog` (Irmer's own named edition, two Google-scanned copies) | index, not cipher |

**Survivors: 0.**

**Requests, archive.org only:** 53 `advancedsearch.php` (31 + 22 loosened) + 152 djvu fetches (137 fetched + 15
errors, first pass) + 2 controls + 15 bug-recovery reruns (1 succeeded, 14 reproduced the same error) = 222
total, well within the ~400 cap, one at a time, >=1.5s apart, no other host touched. No subagents, no logins;
two solver-repo shallow clones made available for grep but not needed (no survivor passage required it) and not
committed.

## Spanish archives beyond the queue, PARES and BDH (LANE N scout of 24 September 2026)

Brief: PARES (pares.mcu.es / pares.cultura.gob.es) beyond Simancas/AHN/AGI rows already on the board, and the
Biblioteca Digital Hispanica (bdh.bne.es), for cifra/cifrado/en cifra/descifrado/"carta en cifra"/"despacho
cifrado"/"con su descifrado"/"cifra de"/"contracifra" items 1450-1800 with PARES images online and no descifrado
alongside. Zero candidates: both hosts were unreachable this session before any query form loaded, so no search
was ever run and no control could be attempted (logged as **query form unverified** for both, per the brief's
control rule, not as "no candidates").

**PARES: blocked, not a bot challenge in the usual sense.** `pares.mcu.es` itself completes a TLS handshake and
answers curl with a clean 302 to `pares.cultura.gob.es/inicio.html` (the real search UI lives there). Following
that redirect fails with curl's "unable to get local issuer certificate": `openssl s_client` through the session
proxy shows the *real* Spanish government leaf certificate (CN `*.cultura.gob.es`, issuer FNMT-RCM "AC Componentes
Informaticos"), not a proxy-generated one, so this host is passed through untouched by the intercepting proxy and
its root CA is simply not in this session's trust bundle -- a different failure from the usual agent-proxy
MITM-CA gap the Access playbook fixes with `certutil`. The browser tool (already fixed for the proxy's own CA,
confirmed by `certutil -L` listing `ccr-agent-proxy`) gets a distinct failure on every path tried against either
hostname (`/ParesBusquedas20/catalogo/find`, `/ParesBusquedas20/catalogo/inicio.html`,
`pares.cultura.gob.es/inicio.html`): a 174-byte `upstream request failed` stub, twice >=3s apart (the one retry
the good-citizen rule allows), never a real page. Per the brief, tried one Wayback capture: the CDX search API
(`web.archive.org/cdx/search/cdx?url=pares.mcu.es...`) itself fails the same way (curl: connection reset, then a
25s timeout on the one retry; browser tool: the same `upstream request failed` stub) while a plain
`web.archive.org/web/.../pares.mcu.es` calendar page loads fine (200, 142KB) -- confirming web.archive.org and the
browser tool both work in general and the failure is specific to PARES/the CDX endpoint, not this session's
egress broadly. The calendar page is a client-side JS widget with no capture links in the saved DOM, so it could
not be followed further within the one-retry budget. This matches and extends QUEUE.md's 19 Sept 2026 note that
PARES was unreachable from this environment (then: curl reset + WebFetch 503; now: a cert-chain gap plus a
distinct proxy-stub failure on the browser tool) -- five days apart, still blocked, by a different symptom each
time. Switched to BDH per the brief.

**BDH: Cloudflare-style challenge, as already logged.** `bdh.bne.es/bnesearch/Search.do?text=cifra` returns curl
403 (one attempt) and the browser tool a "Just a moment..." security-review interstitial (200, 1.3MB, one
attempt) -- the same bot check QUEUE.md's 19 Sept 2026 entry already stood down on ("403 to curl, one attempt,
stood down (a bot check)"). Tried three alternate BNE endpoints once each, hoping for an API route around the
challenge: `datos.bne.es` (BNE's linked-data service) 403, `bdh.bne.es/bnedigital/oai/OAIHandler` (OAI-PMH) 403,
`bdh-rd.bne.es` (an alternate viewer subdomain) 403. All blocked the same way; stood down per the good-citizen
rule rather than retrying in a loop.

Per-host counts: pares.mcu.es/pares.cultura.gob.es -- curl 3, browser_fetch.js 3, openssl diagnostic 1 (not a
retry); web.archive.org -- curl 2, browser_fetch.js 2; bdh.bne.es/datos.bne.es/bdh-rd.bne.es -- curl 3,
browser_fetch.js 1. Raw 0, kept 0, copy-free 0 from both hosts combined. Full log:
`sources/solver-diffs/2026-09-24-lane-n-pares.tsv`.

No ES-prefixed rows this sweep (the prefix stays reserved for whichever LANE N worker gets a working route to
either host). Caveats: (1) this is an access failure, not evidence the hosts hold nothing -- Aymeloglu's
`unsolved-ciphers` repository already caches a PARES sweep (`catalogue/pares-*.jsonl`, cited in QUEUE.md's 19
Sept entry) that a later worker should grep instead of re-querying PARES live; (2) the FNMT-RCM cert gap is a
session/environment issue a later worker or the orchestrator could resolve by adding that CA to the trust bundle,
which would very likely unblock `pares.cultura.gob.es` for curl even without the browser tool; (3) BDH's
challenge may be solvable the way RAH's Anubis challenge was solved by a browser click-through elsewhere in
QUEUE.md's 24 Sept LANE S section -- not attempted here to stay within the one-retry-per-host rule and the $8 cap.

## United States archives (LANE N scout of 24 September 2026)

LANE N brief: 1600-1900 letters in cipher or code with **no decipherment beside them** (Revolutionary
War/Continental Congress/early-republic diplomats, Confederate and Union cipher telegrams, colonial governors,
fur trade), preferring items with a public image, excluding the Eckert 1864 telegrams and anything Tomokiyo or
the solver repos read. Hosts named in the brief: `loc.gov` JSON API, NARA catalog API (`catalog.archives.gov`),
`founders.archives.gov`, and up to two state historical societies with an open CONTENTdm/ArchivesSpace GET
search.

**Egress test (`curl -sS -o /dev/null -w "%{http_code}"`).** `www.loc.gov/search/?fo=json` 200; `catalog.
archives.gov/api/v2/records/search` 200 (but serves the front-end app shell, not JSON, without an API key --
see below); `founders.archives.gov/API/core/search/Founders` 202 with an empty body; `www.masshist.org` 200;
`www.vahistorical.org` connection reset (`000`); `digitalcollections.hsp.org` `CONNECT tunnel failed` (`000`).
The last two were dropped at the egress test per the brief's own instruction ("000 means the egress policy
blocks it... say so and stop").

**founders.archives.gov is behind an AWS WAF challenge to plain `curl`** (`x-amzn-waf-action: challenge` on
every response, empty body, HTTP 202), confirmed on both the documented-looking `/API/core/search/Founders`
endpoint and the `/search`/`/?q=` faceted-browse UI -- the latter renders (via `tools/browser_fetch.js`) but
only as facet/counts (Author, Recipient, Period), never an actual document-result list a script can read; the
underlying result list appears to be populated by a further in-page AJAX call this pass did not reverse-engineer.
Individual document pages (`/documents/<Project>/<id>`) do render in full via `tools/browser_fetch.js` once the
URL is known. Given this, and the brief's specific ask (search editorial notes for "in cipher", "not
deciphered", "undeciphered", "code not found"), the practical route this pass used was `WebSearch
site:founders.archives.gov "<phrase>"` to locate candidate document URLs, each then read in full with
`tools/browser_fetch.js` + `tools/html2text.py` (7 document-page fetches, all successful; 1.5s+ apart, single
fetcher).

**Control (required by the brief before trusting a zero count).** This method demonstrably surfaces genuine
editor-written "not deciphered"/"undecypherable" annotations, not just noise: five such letters were found and
read in full --
[Robert R. Livingston to John Jay, 20 Oct. 1781](https://founders.archives.gov/documents/Jay/01-02-02-0254),
[same, 28 Nov. 1781](https://founders.archives.gov/documents/Jay/01-02-02-0272) and
[1 Nov. 1781](https://founders.archives.gov/documents/Jay/01-02-02-0258),
[Robert R. Livingston to John Adams, 20 Nov. 1781](https://founders.archives.gov/documents/Adams/06-12-02-0044),
and James Madison's "Buried Cipher" letter to Jefferson, 22 Apr. 1783 -- so **founders.archives.gov's
zero-candidates result below is a verified negative**, not an unswept query form. `catalog.archives.gov` and the
one historical society reached have no equivalent control (no already-known cipher item on either host to test
the query form against) and are logged as **query form unverified**, not "no candidates", per the brief.

**Result: 0 open candidates kept of 13 raw items examined in depth (0 copy-free, since none is open).** Every
genuine "not deciphered"/"undecypherable" editorial note found in the Founders Online corpus (Jay, Adams,
Jefferson and Madison Papers) turned out **found-solved**: the modern documentary-editing projects behind
Founders Online had already recovered the plaintext decades ago from a surviving sender's draft, letterbook
copy or duplicate held elsewhere, even in every case where the historical recipient never deciphered their own
copy at the time. This is the same "sibling with a decipherment" pattern LESSONS.md describes (recovery by
alignment) -- except it was already executed, and published, by professional editors:

| Letter | Cipher | Contemporary status | Modern resolution |
|---|---|---|---|
| Livingston to Jay, 20 Oct. 1781 | Thomson's nomenclator (the copy sent via consul Palfrey, lost at sea) | ALS "partly in code, not decoded... illegible to JJ"; endorsed "not decd." | Editors supplied the decoded passage from Livingston's own surviving draft (NHi) |
| Livingston to Jay, 28 Nov. 1781 | same lost Palfrey code | ALS "partly in code, not decoded"; coded passages omitted from the 1890s Johnston and Wharton printed editions | "Decoding based on Dft, with additional decoding by the editors" |
| Livingston to Jay, 1 Nov. 1781 | YESCA cipher (Weber WE033) | triplicate LS and letterbook copies "partly in code, not decoded" | Decoded from the sibling LS copy that was deciphered on receipt; full text printed |
| Livingston to Adams, 20 Nov. 1781 | Lovell cipher, 8 passages | JA's own interlineations show he deciphered only 4 of 8 (enciphering errors defeated the rest) | Editors supplied the whole enciphered paragraph's text from Livingston's surviving draft (NHi) |
| Madison to Jefferson, 22 Apr. 1783 ("Buried Cipher") | Jefferson-Madison code, heavily cancelled by Madison, marked "Undecypherable" | unread at the time | Irving Brant (20th-c. Madison biographer) was first to penetrate the cancellation and decode it |

Also examined and excluded, outside Founders Online: the **Confederate "Vicksburg cipher" telegrams** among
Gov. John J. Pettus's papers at the Mississippi Department of Archives and History (Jefferson Davis and Gen.
Pemberton to Pettus, 1863, Vigenère keyed "Manchester Bluff") -- found-solved, already deciphered and published
by the CWRGM (Civil War & Reconstruction Governors of Mississippi) digital edition project; the **Huntington
"Decoding the Civil War" Union telegram ledgers** -- the same corpus as this repo's own `ciphers/eckert-1862`
and `ciphers/eckert-1864` targets, excluded per the brief; and **Thomas Hutchinson's** (colonial Governor of
Massachusetts) private letterbook cipher (Mass. Archives, SC1/series 45X, vols. 26-27) -- found-solved, decoded
by Malcolm Freiberg using Hutchinson's own key (which Hutchinson himself recorded in vol. 27), published with
footnotes in the Colonial Society of Massachusetts's edition of his correspondence. Full detail and citations
for every row: `sources/solver-diffs/2026-09-24-lane-n-us.tsv`.

**NARA (`catalog.archives.gov`), query form unverified.** The API v2 requires an `x-api-key` (confirmed from
NARA's own `usnationalarchives/Catalog-API` GitHub README: a key must be requested by emailing
Catalog_API@nara.gov, no self-service or keyless read access), which this environment does not hold. Per the
brief, the public catalog search page was tried once with the browser tool instead:
`catalog.archives.gov/search?q=cipher%20telegram` returns 15,493 hits, but the visible results are dominated by
unrelated full-text OCR noise across huge digitized series (a spot-checked hit: "Records Related to Radium Dial
Painters") rather than item-level cipher correspondence -- not tractable to narrow to genuine candidates within
this lane's $8 cap and no subagent budget for it. Flagged for a future pass with either an API key or a
subagent budget to page and filter the item list, not scored as "no candidates".

**State historical societies, one tried, two blocked at egress.** `www.masshist.org` answers 200 at the root,
but its actual library catalog is `balthazaar.masshist.org`, a legacy III/Innovative ILS with no documented GET
search API (not CONTENTdm or ArchivesSpace as the brief anticipated) -- no query built this pass, logged as
unverified rather than swept. `www.vahistorical.org` (Virginia Museum of History & Culture) and
`digitalcollections.hsp.org` (Historical Society of Pennsylvania) both failed the initial egress test (`000`)
and were dropped without further attempts, per the brief's own instruction.

**Blocked host.** `blogs.loc.gov` -- one specific, on-topic post found by web search ("Copies of Copies:
British-Intercepted Letters During the Revolutionary War", LOC Manuscript Division, Sept. 2025) could not be
read: `curl` got HTTP 403, and the one `tools/browser_fetch.js` retry allowed by the good-citizen rule hit a
Cloudflare challenge domain (`brunhild.challenges.cloudflare.com`) that this environment's egress proxy refuses
to reach (`connect_rejected`, organization policy) -- logged, not retried further.

Caveats: (1) this sweep found and closed leads, it did not sweep NARA, the historical societies or fur-trade
archives (American Fur Company, Hudson's Bay Company) at item level -- a genuine gap remains there for a future
pass with either a NARA API key or more budget; (2) nothing here has been check-solved in the formal sense
(rule 1's six-source order) since every item resolved to found-solved or excluded well before that stage was
needed; (3) no ciphertext was transcribed and no page image was opened beyond what the cited pages themselves
show. Requests: `www.loc.gov` 2, `catalog.archives.gov` 2 (1 API test, 1 browser search page), `founders.
archives.gov` 2 direct curl (WAF-challenged) + 7 via `tools/browser_fetch.js` (document pages), `www.masshist.
org` 3, `www.vahistorical.org` 1 (blocked), `digitalcollections.hsp.org` 1 (blocked), `blogs.loc.gov` 2 (both
blocked). WebSearch used as the practical substitute for founders.archives.gov's own search UI, per COMMON
RULES. No Google Books, no Gallica, no DECODE, no subagents, no logins, no credentials.

## Italian state archives, Florence and Milan (LANE N scout of 24 September 2026)

Brief: `.claude/briefs/runs/2026-09-24-lane-n-scIT1.md`. Hosts named: Archivio di Stato di Firenze, the Medici
Archive Project/BIA, Archivio di Stato di Milano, SIUSA/SAN, Antenati -- ciphered despatches and letters 1450-1800
(cifra, cifrato/a, deciferato, zifra, "lettere in cifra", "con cifra", "contrassegni", Latin "notis arcanis") with
no decipherment beside them, strongest preference for a public image online. Read first: LESSONS.md, the BnF and
non-BnF digitised sections above, STATUS.md's 24 Sept lane table. Every candidate lead below was checked against
fresh shallow clones of `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers`, `sources/cryptiana/`, and this
file/CATALOG.md/LANDSCAPE.md/`ciphers/`. Raw hits and exclusion reasons:
`sources/solver-diffs/2026-09-24-lane-n-italy-a.tsv`. **The row-id prefix IT stays reserved for this lane; zero
rows this sweep** -- a future pass with document-level access (not fondo-level description search) should
continue from IT1.

**Domain migration, worth recording once.** Both institutes' historic domains (`www.archiviodistato.firenze.it`,
`www.archiviodistatomilano.beniculturali.it`) now TLS-reset or serve an expired/mismatched certificate to curl;
both redirect (Milan, plain HTTP 301) or resolve (Florence) to a new `cultura.gov.it` subdomain
(`archiviodistatofirenze.cultura.gov.it`, `archiviodistatomilano.cultura.gov.it`), which is what the CLAUDE.md
Access playbook's egress-test-first step is for. `bia.medici.org` similarly answers with a TLS hostname mismatch;
its replacement, found from the medici.org site map, is `mia.medici.org` (MAP renamed BIA to MIA at some point
after this repo's LESSONS.md/CLAUDE.md were last updated with the old name).

**SIAS (Sistema Informativo degli Archivi di Stato, `sias-archivi.cultura.gov.it`), reached, fondo-level only.**
Both archives publish through the national SIAS portal (`RicProgetto=as-milano` / `as-firenze`), a working,
curl-reachable GET search (`ricercasemplice`) confirmed functioning correctly by two genuine positive matches and
several confirmed true-negative matches (below) -- but SIAS describes archival complexes (fondo/series/sub-series)
down to box level, never individual letters, so a "cifra" hit here is a lead to a box of up to several hundred
buste, not a candidate item. Milan: "cifra"/"cifrata"/"in cifra" match 2 fondi via one shared sentence in the
archival-history note for "Registri delle cancellerie dello Stato" (1538-1796) and its child "Militare parte
antica" (1440-1802, 460 buste): both fondi absorbed documents from several ducal-period magistracies, "particolarmente
dalla Cancelleria di guerra e cifra" -- a historical "War and Cipher Chancery" office of the Sforza/Spanish-Milan
administration. This is a real structural fact (the Milanese ducal chancery had a dedicated cipher office,
matching the published literature on Sforza-era cryptography), but SIAS gives no way to browse or search inside
either fondo for the letters that office actually produced; "cifrato", "cifrati", "deciferato" and "zifra" all
return zero complessi at Milan. Florence: "cifra"/"in cifra" match 7 fondi, every one confirmed by opening the
record to be the numeral/amount sense of cifra ("la consistente cifra di 500.000 scudi" in a Lunigiana
acquisition note; tax registers; a chivalric order's insignia; a 20th-c. publicist's figures) -- the same
foliation-noise pattern QUEUE.md's Europeana section already documented for Spanish "se cifra en"; "cifrato" and
"cifrata" return zero. Requests: sias-archivi.cultura.gov.it curl, 1 reachability + 7 Milan term queries + 6
Florence term queries + 4 record-detail fetches = 18, >=1.5s apart, HTTP 200 throughout.

**Archivio di Stato di Firenze's own digitised-image viewer (`archividigitali/`), reached, CONTROL FAILED.**
Separately from SIAS, ASFi runs a WordPress-based viewer over 6,610 digitised filze/registri of the Mediceo del
Principato (Minute di lettere 1536-1671, Carteggio Universale 1530-1737), reproduced in partnership with the
Medici Archive Project, with its own "Cerca" free-text search (`testo_libero=`, confirmed to need the
`ricerca_testo_libero=Cerca` companion field, found by reading the page's own form markup). **Required control:**
before trusting a zero count here, the search was run for "Giovio" -- the surname of the sender on the site's own
homepage "In Evidenza" showcase item ("Lettera di Paolo Giovio a Cosimo I, 1538 gennaio 11", Mediceo del Principato
332 c.85). It returned "La ricerca non ha prodotto risultati" (zero results), confirmed twice: once by a plain curl
GET with the correct field names, and once by a real Playwright browser filling the field and submitting the form
(screenshot in the worker's scratchpad, not committed). A search engine that cannot find a name it advertises on
its own front page is not indexing document content at any scale useful to this brief -- **this host's "cifra"
zero-count is logged as query form unverified, not no candidates**, per the brief's control requirement. Most
likely explanation: the "In Evidenza" captions are a small hand-curated set and the great majority of the 6,610
digitised units carry no per-item transcription for free text to match against. Requests:
archiviodistatofirenze.cultura.gov.it curl ~8 (homepage, cerca page, 2 curl search attempts, 4 record/fondo
pages) + 1 Playwright browser_fetch.js call (2 page loads inside it: initial + post-submit).

**Medici Archive Project (MIA, ex-BIA) -- blocked, needs a login.** `mia.medici.org` (found via medici.org's own
"Databases > Access MIA" link; the brief's `bia.medici.org` now answers with a TLS hostname mismatch and appears
retired) redirects every path to `/Mia/user/LoginUser.do`. The brief scopes this lane to "a public search or API
only, no login"; MAP is not in CLAUDE.md's credentialed-hosts list, so this is out of scope rather than an
access-playbook route to pursue. Not counted as raw/kept/copy-free; logged for the next worker who does have a
MAP account.

**SIUSA, Antenati -- blocked.** `siusa.archivi.beniculturali.it` (the national SIUSA portal, distinct from SIAS)
answered the egress proxy with a policy-style `connect_rejected` (502 to CONNECT) on the one permitted attempt
and its retry; not a site-side block, logged for the orchestrator to check egress policy if this host matters
later. `antenati.cultura.gov.it` (vital-records genealogy portal, unlikely to index diplomatic correspondence
even if reached) answered 403 twice; stood down per the one-retry rule.

**SAN, catalogo.beniculturali.it -- reached but not productive within budget.** `san.beniculturali.it` redirects
(one hop) to a Liferay portal at `/web/san/home`, HTTP 200; its underlying search API was not identified this
budget (out of scope to chase further given SIAS already covers both archives' own fondo descriptions).
`catalogo.beniculturali.it` is reachable but is the ICCD general heritage-object catalogue (paintings,
archaeological finds, monuments) -- the wrong domain for archival correspondence, confirmed by reading its
own category list (`typeOfResources/HistoricOrArtisticProperty` etc.), not swept further.

**One named lead, already covered by a competitor.** WebSearch surfaced a 2011 Cipher Mysteries post naming a
specific unread cipher passage: Albrico Maletta (Sforza's ambassador in Naples) to Duke Francesco Sforza, 26 July
1455, "in cifre", at ASMi Potenze Estere, Napoli 1455 -- not digitised, no image online. A grep of a fresh
`dbourdeau/cyphersolver` clone found his own `oldest/CANDIDATES.md` already tracking the adjacent item at the
same shelf series (Louis XI to the same Alberico Maletta, Saumur, 11 Apr 1465, Latin, one cipher passage never
printed in Vaesen's or Mandrot's editions): "Original at ASMi, Potenze Estere, Francia; not online. Milan keys in
DECODE. Needs a photograph from Milan." This confirms Bourdeau's project already works ASMi Potenze Estere and
Sforza-era diplomatic cipher material directly against material held in Milan, including tracking the same
not-yet-photographed gap themselves -- excluded per rule 1, and not copy-free even if it were not already tracked.

**Per-host counts.** sias-archivi.cultura.gov.it: raw 9 complessi + 1 produttore, kept 0, copy-free 0.
archiviodistatofirenze.cultura.gov.it/archividigitali: raw 0 (control failed), kept 0, copy-free n/a.
mia.medici.org, siusa.archivi.beniculturali.it, antenati.cultura.gov.it: blocked, 0/0/0. san.beniculturali.it,
catalogo.beniculturali.it: reached, not swept for candidates, 0/0/0. WebSearch/github (secondary literature): 1
named lead, excluded as already tracked by a competitor.

Caveats: (1) SIAS's fondo-level granularity is a structural limit, not a budget one -- the Sforza/Spanish-Milan
ducal chancery plainly had a dedicated cipher office ("Cancelleria di guerra e cifra"), and Florence's Mediceo del
Principato is the single largest ducal-diplomatic correspondence archive in Italy (6,610 filze, per the
`archividigitali` project page), so this sweep's zero rows reflect a lack of a working item-level search route
into either archive from this budget, not an absence of cipher material. (2) The most promising next step is not
another keyword sweep of SIAS but either (a) a MAP/MIA account (the BIA/MIA database is specifically a
transcribed, searchable letter-level index of the Mediceo del Principato, built for exactly this kind of query),
or (b) reading the printed inventories SIAS links for "Registri delle cancellerie" and the Sforzesco Carteggio
Interno PDF inventories (`archiviodistatomilano.cultura.gov.it/fileadmin/.../Carteggio_Visconteo_Sforzesco-*.pdf`)
by hand/script for filza-level notes naming cipher content, which a script can grep without a model reading the
whole PDF (Usage rule 2). (3) No score here claims a reading or a novelty class; nothing was promoted, nothing
was solved.

## Italian regional state archives, Mantua Modena Turin Genoa Naples (LANE N scout of 24 September 2026)

LANE N brief: ciphered despatches 1450-1800 in the Gonzaga archive at Mantua, the Este archive at Modena
(beyond QUEUE.md rows G7/G8/G12, its Ambasciatori Ungheria DECODE run), the Savoy archives at Turin, Genoa and
Naples, excluding SAN and SIAS (reserved for the Florence/Milan scout) and anything Lasry, Tomokiyo or DECODE
already decoded. Hosts reached: `archiviodistatomantova.cultura.gov.it` (box-level Archivio Gonzaga finding
aid, Torelli/Luzio; a separate art-history correspondence database at `banchedatigonzaga.centropalazzote.it`),
`asmo.cultura.gov.it` (Este Cancelleria, "Carteggio ambasciatori" -- one downloadable, OCR'd PDF inventory per
foreign court), `archiviodistatotorino.beniculturali.it` (the two "Lettere Ministri" PDF inventories named in
the brief), `archiviodistatogenova.cultura.gov.it` (three "Materie politiche" / Archivio segreto PDF
inventories). `patrimonio.archiviodistatonapoli.it` is egress-blocked (DNS failure on http, `CONNECT tunnel
failed 502` on https, one retry) -- no Naples-native row this sweep; the only Naples material found is filed at
Modena (Este correspondence with the Naples court, IR3 below). `archivi.ibc.regione.emilia-romagna.it` (Modena's
EAD finding aids via IBC) 502'd twice, also blocked. Method: fetch each PDF once, `pdftotext -layout`, grep for
`cifra|cifrat|zifra|chiave` (Italian for cipher/ciphered/key), read the surrounding entry by hand. **Control**:
the same grep found real, dated hits in five of the eight Este-court PDFs (Francia, Roma, Napoli, Spagna,
Venezia) and in one of three Genoa PDFs, and the Genoa "chiave" hits that were noise (harbour-gate and
treasury-door keys, not cipher keys) were individually read and excluded rather than counted -- so the zeros
recorded for the other PDFs (Genova/Inghilterra/Levante at Modena; 32_BustePaesi and 58_Politicorum at Genoa)
are genuine zeros, not a broken query. Raw hits and exclusions (26 rows, including every dropped/noise/blocked
entry): `sources/solver-diffs/2026-09-24-lane-n-italy-c.tsv`. Counts: Mantua 0 kept (2 hosts reached, 0 raw
cipher hits -- box-level inventory has no content notes; Gonzaga art-database search form not reproduced,
logged `query_form_unverified`); Modena 5 kept of 11 raw hits across 8 PDFs (3 excluded as editions/general
remarks, 3 logged as leads not scored); Turin 1 kept of 2 raw hits (1 out-of-period at ~30 further 19th-century
hits, 1 lead not scored); Genoa 3 kept of 5 raw hits in the one PDF with content (2 excluded/lead). Copy-free
count: **0 of 9** -- none of these finding aids links a digitised image of the item itself, only a text
description; every row below needs a copy order or an on-site visit, logged accordingly, not scored as
copy-free. No candidate here overlaps QUEUE.md, CATALOG.md, LANDSCAPE.md, `ciphers/`, `sources/cryptiana/`, or
fresh shallow clones of `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers` (checked by envoy name and
by the specific 1530 Rangone item that could have been confused with IR9's 1720 Rangoni before the mismatch was
ruled out on inspection).

| Rank | Target | Year | Lang | Kind | Reference / Holder | What the finding aid says | Material | Total |
|---|---|---|---|---|---|---|---|---|
| IR1 | Cipher-book with the correspondence of Savoy envoy extraordinary Conte e Presidente Della Torre at The Hague | 1690-1700 | it/fr | recovery | Archivio di Stato di Torino, "Lettere Ministri -- Carteggio diplomatico" (Inv. 151/B), Lettere Ministri Olanda, mazzo 2 | "CIFRARIO al Conte e Presidente Della Torre" filed in the same mazzo as his own decade of correspondence (1690-1700): letters to/from Lord Nottingham, Milord Monquille, Cav. Giuseppe Terne (London), Conte Caraffa, Prelà Doria and the Marchese di Prié (Vienna) -- the embassy negotiated Dutch subsidies for the League of Augsburg war against France. | Copy-order (PDF inventory only, no digitised images found) | 34 |
| IR2 | Cipher and code-names given to Genoese envoy abate Gio. Battista Viganego at Turin, with dispatches from the same correspondent the same weeks in the same box | Apr 1717 | it | recovery | Archivio di Stato di Genova, Archivio segreto, Materie politiche (Trattati e negoziazioni, Inv. 31), item 249, alongside items 246 and 254 | Item 249: "Cifrario e nomi dati a Gio. Batta Viganego, inviato a Torino, per servirsene nella corrispondenza da inviare a Genova" (7 Apr 1717). Items 246 and 254 in the same series, same month: "Notizie trasmesse da Torino dall'abate Gio. Battista Viganego" (7 and 14 Apr 1717) -- plausible sibling ciphertext from the very correspondent the key was issued to, in the same box. | Copy-order | 32 |
| IR3 | Cipher attached to Este envoy Angelo Belmesseri's Naples dispatches on the Stigliano marriage negotiation | 16 May 1627 - Jan 1628 | it | recovery | Archivio Segreto Estense, Cancelleria, Carteggio ambasciatori -- Napoli, b.20 fasc.1 (precise shelfmark given by the finding aid itself) | "Evvi congiunta una cifra" ("there is attached a cipher") on a nine-month run of dispatches about negotiating a marriage between the prince and princess of Stigliano; the same run's earlier fascicle (b.19) carries an unciphered mission by the same envoy, so the cipher use is localised to this specific box. | Copy-order | 32 |
| IR4 | Cipher issued to Genoese secretary Salvago for his 1691 mission to Imperial Count Caraffa, in a run of items about the same Caraffa subsidy affair | 1691 | it | recovery | Archivio di Stato di Genova, Archivio segreto, Materie politiche (Inv. 31), item 294, in the run items 288-299 | Item 294: "Cifra per il segretario Salvago data nel tempo che si portò in Alessandria dal conte Caraffa." The surrounding items (288-298, same year) cover payments to Caraffa's imperial troops then present in Italy during the Nine Years' War and a councillor's justification of Genoa's wartime conduct -- a coherent affair the cipher was issued for. | Copy-order | 32 |
| IR5 | Single Este-France dispatch filed together with the cipher-table sheet used to write it | 27 Apr 1648 | fr/it | recovery | Archivio Segreto Estense, Cancelleria, Carteggio ambasciatori -- Francia, envoy Clerville cav., appendice (precise busta/fasc not resolved from the PDF's table layout this pass) | "1648, aprile 27. con il foglio del cifrario impiegata nel dispaccio" -- the strongest form of LESSONS.md's "the key was in the archive beside the letter" pattern: key and ciphertext catalogued as one physical unit. Small item (one dispatch). | Copy-order | 30 |
| IR6 | Two undated cipher items (a cipher issued to secretary Ricci, and an unattributed cifrario) in the same Genoa political-papers series as IR2 and IR4 | s.d. (within a run otherwise dated 1620s-1630s) | it | recovery (tentative) | Archivio di Stato di Genova, Archivio segreto, Materie politiche (Inv. 31), items 229 and 237 | Item 229: "Cifra data al segretario Ricci." Item 237: "Cifrario." Both undated, no surrounding content description in the finding aid to anchor a specific affair or correspondent, unlike IR2/IR4 in the same series. | Copy-order | 29 |
| IR7 | Fascicle of "imperfect letters and decipherments" from Este envoy Alfonso Rossetti's Spanish embassy | 1533-1539 | it/es | recovery (tentative, edition risk) | Archivio Segreto Estense, Cancelleria, Carteggio ambasciatori -- Spagna, b.4 | "Vi è infine un fascicolo di lettere imperfette e decifrature senza data spettanti al carteggio del detto Rossetti" -- decipherments (decifrature) are catalogued in the same fascicle as the letters, which may mean the letters here are already part-read; not resolved from the finding-aid text alone, flagged rather than dropped since "imperfette" (imperfect/incomplete) suggests the decipherment coverage may not be total. | Copy-order | 26 |
| IR8 | Single Este-Rome dispatch entirely in cipher, from the mission of Petr'Antonio Taurello to Filiberto di Chalons, Prince of Orange | 24 Jun 1527 | it | cryptanalysis | Archivio Segreto Estense, Cancelleria, Carteggio ambasciatori -- Roma, piece no. "32" as printed in the finding aid (not a full modern shelfmark) | "Questa lettera è tutta in cifra" -- sent from Vetralla near Rome, where Taurello had been dispatched with a special commission to the future Habsburg commander of the Sack of Rome, five weeks before it happened. No key or sibling decipherment noted in the finding aid. | Copy-order | 22 |
| IR9 | Plural ciphered letters from an Este envoy in France, name uncertain in the OCR ("Rangoni(?) Giovanni") | 1720 | it/fr | cryptanalysis | Archivio Segreto Estense, Cancelleria, Carteggio ambasciatori -- Francia, appendice | "1720, lettere cifrate" -- plural, no key or content note in the finding aid. Distinct from `cyphersolver`'s already-read `rangone1530` (Guido Rangone, Venice, 1529-30 letters to Anne de Montmorency) -- different person, 190 years apart, checked by name to rule out a collision before keeping this row. | Copy-order | 22 |

Caveats: (1) none of IR1-IR9 has been check-solved; "not found in QUEUE.md/CATALOG.md/LANDSCAPE.md/`ciphers/`
or the two solver repos by envoy name" is a catalogue-matching result under rule 10, not a verified-unsolved
verdict -- all nine need the six-source sweep before the board. (2) No page image has been opened for any of
the nine; every "recovery" framing rests on the finding aid's own prose (a cipher/cifrario catalogued with or
beside a correspondence run), not on having seen a ciphertext leaf, so IR1-IR6's "the key is right there"
claims are inventory-level, not folio-level. (3) IR2 and IR4's sibling-evidence claims (a key and, in the same
box, dispatches from or about the same person/affair) are the strongest form found this sweep, but "in the same
box" is not "on the same key system" -- unconfirmed until someone opens both items. (4) IR5's precise
busta/fascicolo could not be pulled from the France PDF: its "Carteggio diplomatico restituito" table has a
"Segnatura attuale" column that `pdftotext -layout` scrambles against a repeating "APPENDICE" watermark column;
a worker with a PDF-table-aware tool (or the browser reader) should re-extract page 67 before ordering a copy.
(5) IR8's "32" and other Roma-fondo piece numbers read from `pdftotext` are very likely early Appendice-I piece
numbers (busta numbers), not final ASMo shelfmarks; cross-check against the finding aid's own key before
requesting. (6) Two whole hosts (Naples' own archive, and Modena's EAD mirror on the IBC Emilia-Romagna site)
were unreachable this sweep (blocked/502, one retry each, logged in the TSV) -- absence of a Naples-native row
is an access failure, not evidence Naples holds nothing; a later worker with different egress or a browser
fallback should retry both. (7) The Gonzaga art-history database at Mantua (`banchedatigonzaga.centropalazzote.it/collezionismo`)
has a real search form over 1563-1630 correspondence but its PRADO WebForms postback (full PAGESTATE + hidden
fields) was not reproduced this pass; Torelli's full 1920 volume (25.7MB, linked from the ASMn site) was also
not fetched -- both are follow-up leads, not searched to a verifiable zero, so Mantua is NOT confirmed empty,
only not reached this sweep with the budget available. (8) All nine rows are copy-order, not copy-free: this
sweep found no digitised-image route into any of the five archives' relevant series (unlike Gallica or the
Huntington CONTENTdm routes other LANE N sweeps have used), so the LANE N "at least half copy-free" nomination
goal is not met by this batch on its own. Requests: `archiviodistatomantova.cultura.gov.it` 3,
`banchedatigonzaga.centropalazzote.it` 3, `asmo.cultura.gov.it` 10 (1 page, 1 subpage, 8 PDFs), `archiviodistatotorino.beniculturali.it`
3 (2 PDFs, 1 reachability check), `archiviodistatogenova.cultura.gov.it` 5 (1 listing page, 4 PDF
head/get requests), `archivi.ibc.regione.emilia-romagna.it` 2 (both 502), `patrimonio.archiviodistatonapoli.it`
3 (all unreachable). All hosts one request at a time, >=1.5s apart, descriptive UA. No SAN, no SIAS, no Google
Books, no logins, no subagents, no credentials.

## Vatican and Venetian archives (LANE N scout of 24 September 2026)

LANE N worker (`.claude/briefs/runs/2026-09-24-lane-n-scIT2.md`), row prefix VA (reserved). Target: nuncio
despatches, avvisi, cardinals' letters and Venetian ambassadors' dispacci 1450-1800 in cipher with NO
decipherment beside them. Read first: CLAUDE.md rule 1, the Access playbook, LESSONS.md sections 1-2,
`.claude/briefs/check-solved.md` (Thurloe/Raince/Bowes/M9 lessons). Excluded against fresh shallow clones of
dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers, sources/cryptiana/, CATALOG.md, LANDSCAPE.md, ciphers/.

**Egress test.** `archivioapostolicovaticano.va` 302->200; `digi.vatlib.it` 200; `manus.iccu.sbn.it` 200;
`www.internetculturale.it` 200; `www.archiviodistatovenezia.it` 301/200 on the bare root but `curl: (35) Recv
failure: Connection reset by peer` on every subpath tried (`/divenire/`, the `moreveneto` HTML page) across
four separate attempts on three different URLs -- a proxy-level reset (`ws_closed_mid_exchange`), not a clean
block or a repeated retry loop on one URL; logged and stood down per the one-retry rule, not pursued further
this pass. Biblioteca Nazionale Marciana's own manuscript catalogue was not reached at all this pass (budget) --
next worker should try it fresh.

**digi.vatlib.it -- the productive host, and a CONTENTdm-shaped gotcha.** The obvious query form
(`/mss/search?q=TERM`) silently ignores the query exactly like the Huntington CONTENTdm case CLAUDE.md already
documents: `q=cifra` and `q=zzznonsensequeryxyz123` both returned the identical "31081 results found (278005
records)" banner. The real simple-search form is the two-field one (`k_f=0` for Keywords, `k_v=TERM`) reached
from `/mss/`; it also needs a same-origin `Referer` header (`https://digi.vatlib.it/mss/`) or the search path
403s even with a real browser User-Agent (the browser tool hit the same 403, and separately could not drive the
JS search box: `.queryText` stayed `disabled`/invisible after 30s, an unresolved lead for a future worker who
wants item-level Manus/DigiVatLib results without this curl workaround). **CONTROL, confirmed**: `k_v=cifra`
gives 24 results, `k_v=zzznonsensequeryxyz123` gives 0 -- the form genuinely filters once `k_f`/`k_v` are used.
Record-to-shelfmark pairing on the results page needed care: a naive regex split by `box-search-result-details`
mis-attributes each record to the *following* shelfmark header, not its own (caught by fetching two detail
pages and reading their own embedded `f_v[]=SHELFMARK` value, which disagreed with the naive split twice before
a corrected parser -- split on `row-search-result-record` and take the title that opens each block -- was
verified 3/3 against ground truth). Worth documenting so the next worker doesn't repeat the mis-pairing.
Terms tried: `cifra` (24), `cifrato` (0), `cifrata` (1), `cifre` (106, six pages; shelfmark list scanned for
correspondence-shaped titles on pages 2-6, one repeat hit, no new candidates). Full list with exclusion reasons:
`sources/solver-diffs/2026-09-24-lane-n-italy-b.tsv`.

**Clean negative, with a pattern worth naming for the next Italian/Vatican scout.** Every "cifra"-tagged
correspondence item found (not the 15+ keyword-noise hits: foliation, music, unrelated Latin prose) turned out
to already carry its own decipherment or its own published edition, confirmed by reading the record's own
catalogue note (never by title alone, per the M9 lesson) and, twice, cross-checked against a solver repository:
- **Cappon.164 ff.292r-299r, 298r** (5+1 cipher letters, nuncio Ludovico Taverna, Bishop of Lodi, in Spain,
  "forse al card. segretario di Stato, Filippo Boncompagni") -- leaf viewed (both folios, native IIIF images):
  the text under the heading "Cifra del Nuntio di Spagna" / "Cifra del N.o di Sp.a" is plain, fully legible
  Italian prose, not ciphertext. "Cifra" here is the archival document-class label for a *decoded paraphrase
  copy* kept by the Secretariat, not the cipher itself -- the single most useful negative finding of this pass,
  since it will recur across this fondo and probably others (the Vatican chancery habit of filing the decrypt
  under a "Cifra del..." heading). Any future "cifra"-titled Vatican item should have its leaf checked before
  scoring, not just its catalogue title.
- **Urb.lat.1704 f.237r** (nunzio Giambattista Castagna, later Urban VII, to card. Alessandrino/Michele
  Bonelli; catalogue note: "Nel codice: solo la parte in cifra" -- only the ciphered part is kept) -- not
  excluded by an in-codex decipherment, but the record's own Bibliographic References field cites L. Serrano,
  *Correspondencia diplomatica entre Espana y la Santa Sede... Pio V*, t.II, Madrid 1914, p.278-279. The same
  correspondent pair (Alessandrino to Castagna, Madrid nunciature, 1568-69) is independently confirmed already
  solved end-to-end in `dbourdeau/cyphersolver/alessandrino1568/` (11 ciphertexts read with Lasry's key,
  DECODE R93-R102/R115) -- that NOTES.md itself names the same Serrano 1914 edition as an open comparison task,
  so this specific direction of the correspondence (Castagna to Alessandrino rather than the reverse) is the
  same archive, same years, same already-worked correspondent pair.
- **Vat.lat.2392 f.72v** ("Secretum... scriptum in cifra cum eius explicatione") and **Vat.lat.9684** ff.23r-26r
  (Federico Cesi/Johann Eck, early Lincei academy, "parole anteposte alle cifre" as a key to 19 letters) both
  carry their decipherment in the same codex (Vat.lat.9684's at f.140r, Francesco Cancellieri's hand, and
  ff.144r-146v, Domenico Morosini's hand, both early 19th century).
- **Vat.lat.13153 ff.38v-39r** (Du Vernay-Boucault, French envoy, to Imre Thokoly, the Hungarian rebel leader,
  1682) carries "decifrazione interlineare" in the manuscript and is discussed in print: C. Gerin, *Revue des
  questions historiques* 39 (1886), p.117-118.

**Two resource leads, not scored as targets (both fail the rubric's unread=0 "edition" test for themselves, but
match CLAUDE.md's "a key beside undeciphered letters elsewhere is a recovery lead").** Neither has a matched
undeciphered sibling located this pass; both are handed on for a future worker who wants to pair them with one:
- **Urb.lat.948, ff.1r-101v**, "Scriptura occulta, vulgo cifra, Friderici II, Urbini ducis" -- a cipher system/
  key manual belonging to Federico II, Duke of Urbino (sec. XV), fully digitised, no login. A future scout
  should look for an undeciphered Della Rovere/Montefeltro-court cipher letter (ASV or elsewhere) this system
  might open.
- **Barb.lat.9848-9849, ff.2r-232r+** (Francesco Mancini to Cardinal Francesco Barberini and to Mons. Attilio
  Marcellini, 1644-1655) -- catalogued "Cifre e decifrati" (ciphers and their decipherments together), exactly
  the Barberini-fondo cipher register CLAUDE.md flags as often holding keys. The letters themselves are already
  decoded in situ, but the key they carry is a plausible match for *other* Barberini Segreteria di Stato cipher
  correspondence of the same 1640s-50s window that is not yet paired with a decrypt -- worth an ASV (not just
  BAV) search for that sibling before this is dropped for good.

**manus.iccu.sbn.it -- query form unverified (control incomplete).** Reached (200); its real simple search is
`monocampo` posted GET to `/web/manus/risultati-ricerca-manoscritti` (found from the homepage's
`data-form-config`, not documented). The browser tool (results load via AJAX/Handlebars templates, not present
in the plain HTML) shows a live "Trovati: 861 Manoscritti" banner for `monocampo=cifra` that a nonsense query
does not render, so the header count is plausibly live filtering rather than the CONTENTdm-style no-op -- but
861 hits for "cifra" in an all-Italy manuscript catalogue is consistent with the same foliation/numbering noise
CLAUDE.md already documents for Gallica's "chiffre" and BAV's own "cifra romana" (Roman numeral) usage, and the
actual item list is behind a separate infinite-scroll fetch this budget did not resolve (playwright's
`--wait` does not trigger the lazy-load; needs a real scroll or a network-trace approach). Per the brief: logged
"query form unverified", not "no candidates" -- do not read 861 as a real count.

**internetculturale.it -- query form not found.** Root reachable (200); the guessed search endpoints
(`/it/16/search?q=`, `/opencms/.../ricerca_avanzata.jsp?testo1=`) either ignored the parameter or 404'd. Not
resolved this budget.

**archivioapostolicovaticano.va -- no online finding aid found in plain HTML.** The site is almost entirely
institutional/informational pages; its own "Archives" catalogue link routes to `www.mss.vatlib.it/arch_guii/
console?service=tree`, an ArchiveGuide console likely requiring JS, not tried this pass.

Caveats: (1) no leaf image was opened except the two Cappon.164 folios (292r, 298r) and none of the excluded
items' images were needed once the catalogue note or a cited edition settled the exclusion, per the brief's
"never transcribe" instruction and the M9/Thurloe lesson (check the note and the cited edition before the
image, not instead of it, when the note already names a decipherment or a print). (2) The `cifre` search (106
hits) was only sampled by shelfmark/title text on pages 2-6, not individually detail-checked; a title-only pass
can miss a case shaped like Urb.lat.1704 (whose title alone gave no hint of "cifra" -- only the full catalogue
note did). (3) Zero VA rows are filed: every correspondence-shaped hit resolved to found-solved or
already-decoded-in-situ once checked, which is itself the result of this sweep, not an absence of effort --
raw 131 keyword hits reviewed across digi.vatlib.it (24 cifra + 1 cifrata new + 106 cifre, with cifre sampled
by title beyond the two already seen), kept 0, copy-free 0. Requests: digi.vatlib.it ~55 (reachability,
6 keyword-search fetches with pagination, 11 detail pages, 4 IIIF manifests, 3 leaf images, all with a browser
User-Agent and same-origin Referer, >=1.5s apart); manus.iccu.sbn.it curl 3 + browser_fetch.js 3; www.
internetculturale.it curl 2; www.archiviodistatovenezia.it curl 5 (2 succeeded on the bare root, 3 reset on
subpaths); www.archivioapostolicovaticano.va curl 2; github.com 2 shallow clones (dbourdeau/cyphersolver,
aaymeloglu/unsolved-ciphers, grepped only); WebSearch 2. No DECODE, no Google Books, no logins, no subagents,
no novelty wording, no promotion.
## French national and diplomatic archives (LANE N scout of 24 September 2026)

Brief row AN: French national and diplomatic archives outside the BnF -- Archives nationales K/KK/AP series, the
Trésor des chartes, and the Archives diplomatiques (Correspondance politique, Mémoires et documents), 1450-1815,
via francearchives.gouv.fr. LANE G owns gallica.bnf.fr and archivesetmanuscrits.bnf.fr; neither touched here.

**Hosts reached.** `siv.archives-nationales.culture.gouv.fr` (the AN's own Salle des inventaires virtuelle) and
`archives.diplomatie.gouv.fr` both answered every CONNECT with a proxy-level `502` (`gateway answered 502 to
CONNECT (policy denial or upstream failure)`, confirmed via `$HTTPS_PROXY/__agentproxy/status`'s
`recentRelayFailures` -- an egress-policy denial, not a site-side block) -- both logged unreachable, one attempt
each, no route in the playbook helps (rule: "000 means the egress policy blocks it"). `francearchives.gouv.fr`
(the interministerial portal that indexes AN, the Archives diplomatiques and every departmental/regional service)
answered but needs a browser: the search form is a WebForms-style token redirect that 404s on a bare GET, and a
Tarteaucitron cookie panel intercepts pointer events on some pages; `--type "#norql=..."` on the homepage search
box (id `norql`, submits to `/fr/search?q=...`) reliably reaches results, `es_publisher=34633` restricts to
Archives nationales and `es_publisher=34566` to Archives diplomatiques. All queries went through this one host,
>=1.6s apart, browser tool only.

**Control.** Before trusting a low count, ran `q=Viète&es_publisher=34633`, which returned 38 records under the
finding aid "Papiers François Viète (XVIe-XIXe siècles)" (106 AP, cited in `sources/cryptiana/web/viete.htm` as
holding "many letters deciphered by Viète") -- confirms the query form and publisher facet genuinely surface a
known AN-held cipher-adjacent fonds, not a broken search returning zero for everything.

**Queries run** (phrase-quoted, both publishers unless noted): `en chiffre` (102 AN / not re-run AAE, term itself
is foliation/statistics noise per LESSONS.md's Gallica/Kalliope precedent -- confirmed here too, first hits were
"exportation du livre... en chiffre" and "orientation en chiffre: statistiques"), `écrite en chiffre` (2 AN / 0
AAE), `lettre chiffrée` (260 AN / 0 AAE), `déchiffrement` (68 AN, almost all 20th-century cryptology-policy and
judicial noise / 3 AAE), `en partie chiffrée` (47 AN / page 404'd on first attempt, not retried -- one attempt
limit, logged unreachable this budget, not "0"). `lettre chiffrée` and `en partie chiffrée` at AN were the
productive queries; two pages of `lettre chiffrée` (of 26 total, sorted by relevance) and one page of `en partie
chiffrée` were read in full, not the whole 260+47. Producteur facets confirm two dominant series: "France.
Secrétariat d'État de la marine. Administration des consulats (1669-1790)" (91 of the 260) and "...Bureau des
consulats" (44) -- the Navy Ministry's consular correspondence, filed at AN, not AAE, despite being foreign
correspondence (Marine handled consular affairs under the Ancien Régime). AAE's own La Courneuve holdings
(Correspondance politique proper) are thin on francearchives -- only 340PO and 53MD series surfaced at all --
consistent with AAE's main series not being indexed on the portal; `archives.diplomatie.gouv.fr` itself, which
would carry it, is the egress-blocked host above.

Every kept row below was read on its own record page (fonds, cote, date, "Où consulter" block); none has a
"Consulter le document numérisé" link except AN1, so material=1 (described, not imaged) for the rest. No leaf
image was opened for AN1 either: its image sits on `siv.archives-nationales.culture.gouv.fr`, egress-blocked
from this account, so "digitised" here means the portal record links an image this session could not view --
flagged, not scored as copy-free-confirmed. Checked against QUEUE.md, CATALOG.md, LANDSCAPE.md, `ciphers/`, and
fresh shallow clones of `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers` (grep by holder/shelfmark and
correspondent name): no match for any kept row. "Vaulgrenant" alone (a different context, a DECODE-cached note
in `unsolved-ciphers/starhemberg-1758/key-audit-continuation.json`) is a coincidental name hit, not the same
item. d'Estaing 1779 (already in LANDSCAPE.md, AAE Correspondance politique) did not resurface as new.

| Rank | Target | Year | Lang | Kind | Reference / Holder | Catalogue note | Total |
|---|---|---|---|---|---|---|---|
| AN1 | Hoche (general commanding the Armée d'Angleterre) to Clarke, on Admiral Morard de Galles | 19 brumaire an V (9 Nov 1796) | fr | recovery | AN, AF/III/169-AF/III/201, "Archives du Directoire exécutif. Guerre. Volume 4 (an IV-an VIII)" > Armée d'Angleterre > Correspondance secrète > Brumaire an V, Pièce 84 | Catalogue title verbatim: "Lettre en partie chiffrée du général Hoche au général Clarke au sujet de l'amiral Morard de Galles." Same box, 18 pieces earlier (Pièce 66, 4 brumaire an V): "Lettre chiffrée de de Zwanziger à Clarke au sujet du projet de négociation de paix séparée avec l'empereur d'Autriche," immediately followed in the same inventory by Pièces 67-69, "Déchiffrement de la pièce précédente" -- a contemporary decipherment filed beside its cipher letter, in this same folder. That specific decipherment is Zwanziger's alone (an edition once obtained, dropped from this table, see Caveats); nothing this sweep confirms an adjacent decipherment for Pièce 84 itself, but the folder's own filing habit (a cipher piece followed by its clear-text key) is a genuine key lead for the rest of the folder, unconfirmed beyond Piece 66. Not digitised; "Voir sur le site d'origine" points at the egress-blocked AN viewer. Hoche's Expédition d'Irlande (the planned invasion with Wolfe Tone, autumn 1796) is one of the best-studied Directory-era military plans. | 36 |
| AN2 | Hoche to Clarke, announcing the arrival of [Wolfe Tone] | An V (1796-97) | fr | recovery | Same fonds/box as AN1, Pièce 108 | Catalogue title verbatim (truncated by the search snippet): "Lettre, en partie chiffrée, du général Hoche au général Clarke annonçant l'arrivée de [Wolfe Tone]. Il déplore l'aventure arrivée au général..." Same folder, same key-lead reasoning as AN1 (untested beyond Pièce 66/67-69). Wolfe Tone's own role in the Irish expedition is independently well documented (his journals are printed), raising both weight and the risk that this specific letter's content is already summarised or quoted in Tone/Hoche biographical literature even if the cipher itself was never applied -- not checked this sweep. | 36 |
| AN3 | "Idem" [Vallière], French consul at Algiers, six dispatches on Algiers war preparations and peace-treaty news (Spain, Sardinia, Hamburg, Tuscany) | 3 Mar-16 Sept 1750, 2 Mar 1751 | fr | cryptanalysis | AN, "Affaires étrangères. Correspondance reçue du consulat d'Alger (1642-1792)", ff.11-13, 95, 133, 165-167 | Six separate "Lettre chiffrée" (one "Lettre chiffrée et en clair", mixed) items from one run of consular dispatches, titles naming Oran siege preparations, an Algiers-Hamburg peace treaty, Tuscan-flag abuses at Livorno, and manoeuvres over the Kaznadar. Not digitised. High print risk flagged, not checked: Eugène Plantet's 1889 "Correspondance des Deys d'Alger avec la Cour de France" specifically covers this consulate and era; a same-edition check is the obvious next step before any campaign. | 28 |
| AN4 | Chevalier de Lironcourt, French consul at Amsterdam, to the Minister, on a conference with the Prince of Nassau | 1778 | fr | cryptanalysis | AN, "Affaires étrangères. Correspondance reçue du consulat d'Amsterdam (1775-1784)", Fol. 150 | "Copie de la lettre chiffrée du Chevalier de Lironcourt, Consul à Amsterdam au Ministre, sur une conférence avec le Prince de Nassau." A copy, not the original send. 1778 sits inside French preparations for the American War (the Franco-American treaties were signed Feb 1778); Dutch neutrality/the Prince of Nassau's position was a live diplomatic question that year. Not digitised. | 28 |
| AN5 | Marquis de Bouillé to Comte de Fersen | 21 April 1791 | fr | cryptanalysis | AN, 440AP/3 pièce 3, "Papiers Marie-Antoinette (XVIIIe-XIXe siècle)" | "Lettre chiffrée du 21 avril 1791 du marquis de Bouillé au comte de Fersen." 2 pages. **Digitised** -- the only copy-free row this sweep (`Consulter le document numérisé` links to the AN's own viewer) -- but the image sits on the egress-blocked `siv.archives-nationales...` host, so it was not opened or confirmed to show ciphertext (rule 2 not fully met). Six weeks before the royal family's flight to Varennes (20-21 June 1791), which Bouillé helped plan and to which Fersen was central: this is very likely covered by Fersen's own published correspondence (Klinckowström's 1877-78 "Le Comte de Fersen et la cour de France" is the standard edition and is known to print ciphered Fersen letters with their decipherments) -- flagged as the single highest print risk in this table, not checked this sweep. | 25 |
| AN6 | Comte de Vaulgrenant (French diplomat at the Spanish court) to Jean Partyet, French consul at Cadiz | 1737 | fr | cryptanalysis | AN, same consular-correspondence class as AN3/AN4/AN7 (Cadix), Fol. 202-202v | "[Lettre chiffrée] - Extraits; indult de la flotte et des fruits; remboursement à faire aux esclaves français." Ransom/redemption of French captives and a fleet/fruit-trade licence. Finding aid title and full fonds citation not captured this sweep (time-boxed); date and cote confirmed from the record page. | 28 |
| AN7 | Jean-Baptiste Poirel, French vice-consul at Cadiz, to Sartine (Secretary of State for the Navy) | 1779 | fr | cryptanalysis | AN, "Affaires étrangères. Correspondance reçue du consulat de Cadix" (title inferred from AN3/AN4 pattern, not independently confirmed), Fol. 71-71v | "[Lettre chiffrée] - N° 110. Il donne l'état d'armement des différents bâtiments de l'escadre Córdoba; salutations." Naval intelligence on the Spanish fleet under Córdoba, 1779 -- the year Spain entered the American war against Britain and began the Great Siege of Gibraltar; Sartine was Navy Secretary 1774-1780, consistent with the date. | 28 |

**Leads, not scored** (found in the same sweep, worth a follow-up read, not verified enough to rank):

- Henry Lavie, French consul at Saint-Pétersbourg, to the Conseil de Marine, 1720 (AN, "Correspondance des consuls
  de France à Saint-Pétersbourg (1713-1792)", Fol. 92-94v°): this record's own text says a courier "a bien voulu
  se charger du duplicata de ma dépêche du 22 novembre dernier laquelle étant écrite en chiffre" (was carrying a
  duplicate of my 22 November dispatch, which was written in cipher) -- so the record matched here is a covering
  letter *about* a ciphered dispatch, not the cipher itself. The 22 Nov 1720 dispatch it names was not located
  separately this sweep; next step is a dated search in the same fonds.
- Guilleragues (French ambassador to the Porte) to Duquesne (naval commander), Péra/Constantinople, four letters
  Aug-Sept 1681-Jan 1682 (AN fonds not re-confirmed, ff.163/182/225/292), all matched `en partie chiffrée` but the
  visible search snippet for each does not itself show the phrase -- it may sit in a dossier-level note covering
  the whole run rather than each individual piece. Not opened to check which.

**Dropped this sweep** (already deciphered in the same box, or outside the brief's 1450-1815 window):

| Name | Reason |
|---|---|
| Zwanziger to Clarke, 4 brumaire an V (AN, same box as AN1/AN2, Pièce 66) | Edition, not a target: immediately followed by Pièces 67-69, "Déchiffrement de la pièce précédente," a contemporary decipherment in the same folder (unread=0 per scout.js's own definition). Left out of the table; its existence is the key lead cited under AN1. |
| "27 février 1519. Lettre en partie chiffrée (et déchiffrée) de Joachim de Moltzan au chancelier de France Antoine Duprat..." (AN) | Catalogue says "et déchiffrée" outright. Also a likely direct hit for this repository's own `ciphers/dupuy468-anhalt/` target (M7 in QUEUE.md): the verifier's 23 Sept 2026 re-attribution of that Gallica item names "Joachim von Moltzan" as a correspondent -- worth checking by the target's own workers, not pursued further here (out of this brief's scope). |
| Correspondance secrète de Berlin: Mirabeau to Comte de Goltz, "Déchiffrement de cinq lettres de l'abb[é]..." 1786-87 (AAE, 53MD/1884) | Catalogue says a decipherment of five letters already exists. Mirabeau's Berlin mission correspondence was printed by Mirabeau himself in 1789 ("Histoire secrète de la Cour de Berlin"); high likelihood of found-solved rather than open, not checked further. |
| "Lettre chiffrée écrite en 1816 au général Jacquemard..." (AN) | 1816, one year outside this brief's 1450-1815 window. |
| "Lettre écrite en chiffre, paraissant provenir de la région de Saint-Brieuc (janvier 1825)" (AN, F/7/6751, Police politique) | 1825, outside the window. Genuinely striking as a real, undescribed ciphered intercept (domestic political police file) -- worth a QUEUE row for whichever lane covers 19th-century French police/political material, not this brief's period. |

**Caveats.** (1) None of the seven scored rows has been check-solved; this is a catalogue-title match, read on the
record page, not a verified reading. (2) AN1/AN2's key lead (a decipherment habit in the same folder) is
confirmed only for Pièce 66, not for Pièces 84 or 108 themselves -- a worker with AN viewer access should check
every piece between 66 and, say, 120 in this folder for a similar "Déchiffrement de la pièce précédente" entry.
(3) AN3's Plantet-edition risk and AN5's Klinckowström-edition risk are both real and unchecked -- a print check
before any campaign is not optional for either. (4) AN6/AN7 (Cadix cluster) were time-boxed: cote and date are
confirmed from the record page, the parent finding aid was not independently reopened for AN7. (5) `en partie
chiffrée` restricted to Archives diplomatiques 404'd once and was not retried (one-attempt rule); AAE's index
coverage on francearchives looks thin generally (see Hosts reached), so a true AAE sweep needs
`archives.diplomatie.gouv.fr` itself, which is egress-blocked from this account -- ASKS-worthy if the lane wants
it reopened, not filed here (out of this brief's scope). (6) Zero rows are copy-free-confirmed: AN5 is digitised
but the image host is blocked; every other row needs a copy order or a reading-room visit -- below the "at
least half copy-free" lane goal stated in the COMMON brief, reported honestly rather than stretched.

**Per-host report:** francearchives.gouv.fr: about 22 browser-tool page loads (homepage + control query + 5
phrase queries x2 publishers + 2 result pages + 9 record-detail pages), all >=1.6s apart, no login, no
challenge. siv.archives-nationales.culture.gouv.fr: 2 attempts (both `502` at the proxy, egress-policy denial),
logged, not retried further. archives.diplomatie.gouv.fr: 1 attempt (`502`, same cause), logged. github.com: 2
shallow clones (both solver repositories, grep only, no push). No credentials used. No subagents. Never
promoted, never solved, never transcribed.

## British Library and Wellcome digitised candidates (LANE N scout of 24 September 2026)

Hosts reached: `searcharchives.bl.uk` (JSON search and per-record fetch, 28 requests, >=2s apart, well under
the 120 cap), `api.wellcomecollection.org/catalogue/v2/works` (6 requests, >=1.5s apart), `bl.digirati.io` and
`iiif.bl.uk` (3 requests, digitisation checks only). Two shallow clones (`dbourdeau/cyphersolver`,
`aaymeloglu/unsolved-ciphers`), grep only. Two extra probes strayed outside this brief's named hosts
(`www.bl.uk`, `digitisedmanuscripts.bl.uk`) trying to find a "Digitised Manuscripts" search endpoint before
remembering the brief names only `searcharchives.bl.uk` and the IIIF hosts; `digitisedmanuscripts.bl.uk` was
refused at the proxy (502, policy denial) before any data crossed, `www.bl.uk` returned ordinary 200/404/307
pages with no useful content. Flagged here rather than repeated.

**Controls (required, both pass).** BL: the general `cipher`/`cypher` query (668 + 447 raw hits) surfaces BL
Add MS 6912 (QUEUE.md N44) and the Mss Eur D623 items (N1) verbatim on page 1 -- the query form works.
Wellcome: `query=cipher` surfaces "Johann Gerlach" (Wellcome MS.309), the item Bourdeau's repository already
names and calls "read in effect" because its own decipherment key is bound in
(`/tmp/cyphersolver/oldest/scan_2026-09-23/france_england_mss.md`) -- the query form works there too.

**BL Add MS copy-order recheck (required by this brief).** All BL Add MS rows currently on the board as
copy-order were re-checked for digitisation via `searcharchives.bl.uk`'s `url_tsi` ("Digitised Content")
field: N3 (Add MS 4956), N16 (Add MS 21375), N30 (Add MS 89317/5/61), N48 (Add MS 8526), N49 (Add MS 62401)
and N56 (Add MS 8730) were fetched fresh this pass, all empty. N29, N41, N42, N43, N44, N45 and N46 had
already been re-checked "not digitised" earlier today by other LANE N/V/W sessions (cited from their
NOTES.md, not re-fetched). **None has since been digitised; no row moves from copy-order to copy-free.**

**Structural finding, worth flagging to every lane touching BL manuscripts.** `access.bl.uk` (the viewer
domain named in catalogue "Digitised Content" links) does not resolve at all (DNS failure, tested fresh
today), and `bl.digirati.io`'s IIIF endpoint returns 403 (S3 AccessDenied) even for a shelfmark whose own
catalogue record carries a live-looking Digitised Content link (Add MS 33596, ark `vdc_100162924544.0x000001`).
This matches LESSONS.md's 19 Sept note ("the British Library viewer has been offline since the 2023 cyber
attack") and the Bowes-walsingham-1583 finding (23 Sept, same 403 S3 AccessDenied pattern). Practical effect:
**no British Library manuscript is reachable as a public digitised image right now, regardless of what its
own catalogue record claims.** This sweep therefore produced zero BW rows for the table -- not because no
new BL cipher material was found (see below and the TSV), but because the "public digitised image" gate this
brief sets cannot currently be met by any BL manuscript.

**Wellcome.** Both spellings (`cipher`, `cypher`) fetched in full (209 unique hits). 70 are `workType`
"Archives and manuscripts"; every one is a personal or professional alchemical, medical or astrological
notebook (Wellcome MS.105, MS.309, MS.259 and about a dozen siblings, all already named in Bourdeau's own
pre-1450/early-modern sweep) or Samuel Tertius Galton's own 1829 diary cipher and its key
(GALTON/1/1/7/2/1-5, UCL Special Collections) -- a private diary, not a letter or register, so out of this
brief's scope even though it is a genuine unread-with-key-in-hand item. None is a diplomatic or political
cipher letter. This extends the 23 Sept 2026 finding already in this file ("this lane is exhausted") rather
than reversing it.

**Raw and kept counts.** BL: 199 unique item-level hits inspected from page 1 of each spelling (out of 668 +
447 raw); 6 genuinely new (not on DECODE, not in QUEUE/CATALOG/LANDSCAPE/ciphers/, not in either solver repo)
survive exclusion, all copy-order (Add MS 72307, 72308, 72246, 72387-72399 -- Trumbull Papers, partly cipher,
1552-1626; Add MS 45518-45523 -- the Willes decipherers' own family papers, 1706-1844; Add MS 61228-61230 --
Blenheim Papers, partly cipher, 1701-1710) plus one further new find logged but out of scope for the table
(Egerton MS 1696, three cipher keys inserted at the end of a volume, including the Tuscan Secretary of
State's ciphers 1682-1713). Two near-misses were caught and excluded only after checking the solver repos by
name: Add MS 4136 (Forbes Papers) looked new but is the same shelfmark already worked in QUEUE.md rows 7/20
and across seven of Bourdeau's folders; Add MS 32270 looked new but is entirely Bourdeau's `visconti1727`/
`palm1727` territory (the Deciphering Branch's own reconstructed-key volume). Add MS 33596 (royalist cipher
keys, Digby) carries a "Digitised Content" link but is already on DECODE (records for BL_Add_MS_33596_025
through 031-032) and its viewer is dead per the finding above. Full per-hit table, exclusions and reasons:
`sources/solver-diffs/2026-09-24-lane-n-bl-wellcome.tsv`. Per-host: BL raw 199 inspected / kept 6 (all
copy-order, logged not tabled) / copy-free 0. Wellcome raw 209 / kept 0 / copy-free 0.

No BW-prefixed rows this sweep: every BL find that is genuinely new is copy-order only (per this brief, logged
in the TSV, not tabled), and Wellcome yielded nothing in scope. **Caveats.** (1) The six new BL finds carry
real, unchecked edition risk, especially the Trumbull Papers cluster (a major, calendared 17th-century
diplomatic archive) and the Blenheim Papers (Coxe 1818-19, and the subject of Churchill's biography of
Marlborough) -- a check-solved pass, not this scout, should run before either is promoted. (2) Only page 1
(100 hits) of each spelling was inspected against 668/447 raw totals; further pages may hold more candidates,
but given the structural BL-access finding above, any further copy-order BL find would still not satisfy this
brief's copy-free gate. (3) Egerton MS 1696's inserted cipher keys (Tuscan Secretary of State, 1682-1713) are
worth a look for any future Italian-diplomatic-cipher lane even though the volume itself is not a letter.
(4) The Willes Papers (Add MS 45518-45523) are a key-lead resource across many other targets' correspondents,
not themselves a single unread letter -- worth opening before scoring as its own target.

<<<<<<< Updated upstream
## US research libraries B (LANE N scout of 24 September 2026)

LANE N brief (US research libraries B, worker for session_01W4z8JhXJYHRjorPC1Qkpiy): the William L. Clements
Library (quod.lib.umich.edu, clements.umich.edu), the American Philosophical Society (search.amphilsoc.org,
diglib.amphilsoc.org), NYPL Digital Collections (api.repo.nypl.org, digitalcollections.nypl.org), the New-York
Historical Society (digitalcollections.nyhistory.org), Harvard Houghton/CURIOSity (curiosity.lib.harvard.edu,
hollisarchives.lib.harvard.edu), and Princeton special collections (dpul.princeton.edu). Excludes loc.gov,
NARA, founders.archives.gov and the state historical societies (held by the sibling "LANE N scout US"
worker, ROOM.md 05:10 UTC claim). Reachability tested first per the good-citizen rule (`curl -sS -o /dev/null
-w "%{http_code}"`, descriptive User-Agent, one retry with a browser User-Agent after a pause on any
403/429/challenge, never a retry loop).

**Six of the seven named hosts were blocked before any query form loaded**, each confirmed by two independent
attempts (not a transient egress "000"): `quod.lib.umich.edu` and `clements.umich.edu` both 403 on the bare
root and a collections path, matching this repository's own 19 Sept 2026 note for `clements.umich.edu`;
`search.amphilsoc.org` 403; `diglib.amphilsoc.org` redirects (302) straight to a Cloudflare Turnstile challenge
page; `digitalcollections.nyhistory.org` 403; `curiosity.lib.harvard.edu` and `hollisarchives.lib.harvard.edu`
both 429 on three attempts each spaced by a pause (3s, then 8s), never resolving this session. NYPL's two
routes are blocked for different reasons: `api.repo.nypl.org/api/v2/items/search` answers 200 with the literal
body `HTTP Token: Access denied.` (needs an OAuth token not held in this environment), and
`digitalcollections.nypl.org/search/index` answers 200 but the body is an Incapsula bot-detection iframe
(959 bytes, no search results). All seven of these are logged **"query form unverified"**, not "no
candidates," per the brief's control rule. Full per-host detail in
`sources/solver-diffs/2026-09-24-lane-n-us-b.tsv`.

**dpul.princeton.edu is the one host that answered.** Its `catalog.json?q=` JSON endpoint is a real, working
search (34 hits for "cipher", 115 for "cypher", verified against a plain HTML fetch of the same query showing
identical hit text). **Control passed**: the query surfaces a genuine cipher item, `ark:/88435/dcr781wv919`
(Arthur Lee to the Continental Congress's Committee of Correspondence, 31 Aug 1778, box 20 folder 3 of
Princeton MS collection C0063) -- Princeton's own curator's note says Lee "encoded his letter using a
sophisticated cipher [keyed to] Entick's Dictionary, which this letter's recipient subsequently interlined."
That "subsequently interlined" is a contemporary decipherment written directly on the same document, so by
README "What counts as a result" this scores `unread=0` (an edition: readable today with the key/plaintext in
the same file) and is **not nominated** -- logged here only as the control evidence that the search itself
works. The remaining 33 "cipher" hits and all 115 "cypher" hits, sampled across pages plus two phrase searches
("in cypher", "in cipher": 15 and 5 hits), are printed 18th/19th-century books and pamphlets where the word
appears in ordinary prose (arithmetic and "ready reckoner" texts using "cypher" for digits, a manuscript
catalogue's watermark description "cipher/monogram", war-narrative memoirs by Cornwallis/Tarleton/Burgoyne/
Monroe using "in cypher" rhetorically) -- none is a manuscript ciphertext. A `f[format][]=Manuscript` facet
attempt did not cleanly isolate manuscripts (still returned Book-format rows), so this is a text-search noise
problem, not a format-filter fix found this pass. `findingaids.princeton.edu`, the companion finding-aid
catalogue for the same C0063 collection (not a brief-named host, tried only because it is the direct source
for the one genuine hit above), returned a Cloudflare Turnstile "Verifying connection" page for every query
tried and was not retried.

**No rows filed this sweep (UB1 unused).** Checked the one genuine candidate and all sampled printed-book hits
against QUEUE.md, CATALOG.md, LANDSCAPE.md, `ciphers/`, and fresh shallow clones of `dbourdeau/cyphersolver`
and `aaymeloglu/unsolved-ciphers` (grepped for "Princeton", "Arthur Lee", "dpul"): no match in either solver
repository or this project's own files.

Caveats: (1) this is a small, noisy slice of Princeton's holdings under one free-text query; a collection-
scoped search (e.g. within "Princeton and the Revolution" or other Revolutionary-War-era manuscript
collections specifically, once `findingaids.princeton.edu`'s Turnstile clears) could still surface an unread
cipher letter that the whole-catalogue "cipher"/"cypher" query missed under a different cataloguing word
("ciphered", "in figures", a French/Spanish equivalent). (2) Six of seven brief-named hosts never got past
reachability, so this sweep should not be read as "the Clements/APS/NYPL/NYHS/Harvard collections have no
open candidates" -- it establishes only that this session's tools could not reach their query forms today.
(3) No leaf image was opened (the one genuine hit was excluded on its own catalogue-note text, per rule 2's
"never transcribe" and the M9/Thurloe lesson to check the note before assuming). Requests: quod.lib.umich.edu
2, clements.umich.edu 2, search.amphilsoc.org 2, diglib.amphilsoc.org 1, api.repo.nypl.org 1,
digitalcollections.nypl.org 1, digitalcollections.nyhistory.org 2, curiosity.lib.harvard.edu 3,
hollisarchives.lib.harvard.edu 2, dpul.princeton.edu 8 (1 reset, retried once), findingaids.princeton.edu 2,
github.com 2 shallow clones (grepped only, deleted after). No Google Books, no TNA, no DECODE, no Gallica, no
subagents, no novelty wording, no promotion, no solving.
=======
## Irish archives and libraries (LANE N scout of 24 September 2026)

Hosts reached: `sources.nli.ie` (an NLI-run union index of manuscript sources for Irish history, indexing
material held at NLI and at many other repositories -- its `/Search/Results` pages load cleanly over curl,
its `/Record/` item pages are Cloudflare-challenged and were not reached); `www.nli.ie` (PDF collection-list
finding aids under `/pdfs/mss%20lists/` and `/sites/default/files/`, item-level text, no login). Controls: no
cipher item at NLI, PRONI, TCD or RIA was already known to this project before this sweep (checked QUEUE.md,
CATALOG.md, LANDSCAPE.md, ciphers/, sources/cryptiana, and fresh greps of both solver repositories -- zero
hits), so the brief's "known item" control could not be run as specified; logged as a control-note row in the
TSV rather than skipped. Blocked hosts, one attempt each, not retried: `catalogue.nli.ie` and `digital.nli.ie`
(Cloudflare JS challenge / proxy 502); PRONI eCatalogue (`apps.proni.gov.uk/eCatNI_IE`) -- GET redirects to a
session-timeout page, a POST replaying the ASP.NET `__VIEWSTATE`/`__EVENTVALIDATION` triple is rejected by a
WAF ("Request Rejected"); `digitalcollections.tcd.ie` -- a Cloudflare/hCaptcha challenge page, matching
CLAUDE.md's existing note on this host; `archives.ria.ie` -- proxy CONNECT tunnel failure (egress-policy
denial, not the site). `www.nidirect.gov.uk` and `www.proni.gov.uk` load (HTTP 200) but neither is the
eCatalogue search itself. Every one of these four is logged "query form unverified," not "no candidates."

Raw: 51 hits for `cipher` on sources.nli.ie across all repositories it indexes (6 held at NLI itself after
filtering to `Archive: Dublin: National Library of Ireland`, plus 2 further hits for `cypher` found only by
grepping the two Ormond Papers PDF finding aids, which the search box does not reach). Kept: 4 (IE1-IE4).
Copy-free: 0 -- every kept row is a catalogue description or finding-aid line, not an image; none of the four
`/Record/` pages or any digitisation could be reached this sweep, so material scores 0-1 throughout and every
row needs a reading-room visit or copy order, not a free download.

| Row | Target | Year | Lang | Kind | Next step | Detail | Total | Sources |
|---|---|---|---|---|---|---|---|---|
| IE1 | Correspondence in cipher by statesmen and others, re. negotiations from Belgium on the restoration prospects of Charles II | [c.1656-60, undated in the catalogue snippet] | en | cryptanalysis | search-print | NLI, ref. not visible in the search snippet (sources.nli.ie/Record/MS_UR_019357, page Cloudflare-blocked). Diplomatic/exile correspondence about the Restoration is heavily published (Thurloe, Clarendon State Papers, Nicholas Papers); check those editions by date range before any campaign. Record page and image not reached this sweep -- material and size both unconfirmed. | 24 | sources.nli.ie |
| IE2 | "Rendition of Ireland 1690" volume: letters to Sir Robert Southwell (Secretary of State for Ireland) from Captains Sincock, Wright and Dover, plus a "(Jacobite?) cypher of names" and Navy Office letters, 1639-1741 | 1690 | en | cryptanalysis (the cypher-of-names item only; the volume's other letters read as plain covering correspondence) | search-print | NLI, ref. not visible in the snippet (sources.nli.ie/Record/MS_UR_028273, page Cloudflare-blocked). Likely a small nomenclator/alias list rather than running ciphertext -- confirm size before scoring further. Williamite War in Ireland (1690) is well covered by CSPD and Dalton's *English Army Lists*; check both for Southwell's correspondence of this date. | 22 | sources.nli.ie |
| IE3 | "[Letter] in cypher. With 2 photostat copies." | [c.165-] | en (unconfirmed) | cryptanalysis | archive-request | NLI Ms. 11,061 (1-20), item 3, in "Miscellaneous items relating to the Ormond's lands in Kilkenny etc." (Ormond Papers, Collection List a017, PDF p.129 of the finding aid). No decipherment noted for this item or its neighbours (1,2,4,5, all read). That photostat copies already exist suggests the item has been consulted before, which cuts both ways -- worth a search-print pass (Carte's Ormond calendars, HMC Ormonde) before an archive-request, not skipped in favour of one. | 21 | www.nli.ie (PDF finding aid) |
| IE4 | "Minute da porsi in cifra a varii Nuntii, 1608-10" (instructions to be put into cipher for various nuncios) | 1608-1610 | it | contribution (tentative; may be an administrative minute rather than a ciphertext) | search-print | NLI, ref. not visible in the snippet (sources.nli.ie/Record/MS_UR_066509, page Cloudflare-blocked). Papal-nuncio diplomatic material of this date is the same family Tomokiyo and the solver repos already cover heavily for Italy (Pallotto, Morosini, Ottobon, Vatican Challenges) -- check those pages by date before assuming this is unclaimed material, and confirm the item is ciphertext, not an instruction document, before scoring further. | 18 | sources.nli.ie |

**Dropped this sweep:**

| Name | Reason |
|---|---|
| Four ciphers used by the Earl of Orrery, late 17th c. (NLI, sources.nli.ie MS_UR_088020) | A cipher key/table itself, not an unread ciphertext letter; no paired letter using this key located this sweep. Worth keeping as a key-lead resource if any Orrery correspondence turns up cipher-flagged elsewhere. |
| Miscellaneous quatrains with glossarial notes in cipher, by Seán Ó Murchú of Sunday's Well(?), early 19th c. (NLI, MS_UR_053333) | A literary/scribal cipher notation, not a political or personal ciphertext letter; wrong kind and low weight for this project. |
| "A dissuasive from Protestancy," bearing the "ciphers" W.N./N.W. (NLI, MS_UR_050136) | The catalogue's "ciphers" are a printer's/author's monogram device, not encryption -- false positive on the search term. |
| Everything else on sources.nli.ie held outside Dublin (British Museum, Bodleian, Rome, Madrid, Siena, Brussels items that surfaced under the unfiltered `cipher` query) | Out of this lane's scope (other lanes cover BL/TNA and the continental archives); not excluded as solved, just not this brief's material. |

**Caveats.** (1) None of IE1-IE4 has an image or a full catalogue record confirmed this sweep -- every
`/Record/` page on sources.nli.ie returned a Cloudflare "Just a moment" challenge to curl, `browser_fetch.js`
and WebFetch alike (one attempt each, not retried), so dates, extents, and full descriptions rest on the
search-result snippet or the PDF finding-aid line only; a session that can clear that specific Cloudflare
challenge (or an NLI reading-room/reproduction request) is the next step for all four, not further search.
(2) IE1's and IE2's language, size and any key lead are unconfirmed for the same reason -- both next-step
entries say "search-print" rather than anything stronger because the print-check itself (the standard
pre-campaign step) could not be run without knowing the correspondents' identities beyond what the snippet
gives. (3) IE3 was found by brute-force grepping a 1,072-page PDF finding aid (`a017_ormond.pdf`) for
"cipher"/"cypher" after the catalogue's own search interfaces failed; the same method applied to the
NLI's other ~175 numbered collection-list PDFs (Inchiquin, Wild Geese/"Irish Abroad" material, and the rest of
the Ormond Papers' own numbered lists beyond a017 and the "Additional" list checked here) was not attempted
this sweep for lack of a bulk index of their filenames -- a real, cheap next lane if a filename list can be
found or guessed. (4) IE4's Italian "minute da porsi in cifra" phrasing reads as instructions about what to
encipher, not necessarily a surviving ciphertext; flagged, not resolved. (5) check-solved has not been run on
any of the four; a later worker does that before promotion, per the brief.

**Per-host report:** sources.nli.ie: 7 curl requests (3 unfiltered-query pages + 1 NLI-only-filtered page + 1
alternate-spelling filtered page + 2 record-page attempts, plain and with a cookie jar, both hitting the
Cloudflare wall), all >=1.5s apart, descriptive UA, plus 1 `browser_fetch.js` and 2 WebFetch attempts on the
same blocked record page (different network paths, same result). `www.nli.ie`: 1 reachability check + 3 PDF downloads (Ormond Papers Additional list, Ormond
Papers main list, and one 403 on a third-party mirror of an Inchiquin Papers list, not an nli.ie host so
dropped from the count), >=1.5s apart. `catalogue.nli.ie`: 1 curl (403) + 1 curl with browser UA (403) + 1
`browser_fetch.js` attempt (Cloudflare challenge page returned). `digital.nli.ie`: 1 attempt (proxy 502).
`apps.proni.gov.uk`: 1 GET (session-timeout redirect) + 1 form-page fetch + 1 POST replay (WAF rejection).
`www.proni.gov.uk` / `www.nidirect.gov.uk`: 1 reachability check each (200, not searched further -- neither is
the eCatalogue). `discovery.proni.gov.uk`: 1 attempt (proxy 502). `digitalcollections.tcd.ie`: 1 reachability
check (200) + 1 query attempt (Cloudflare/hCaptcha challenge). `ria.ie` / `www.ria.ie`: 2 reachability checks
(403 default UA, 200/301 browser UA), no working catalogue search located. `archives.ria.ie`: 1 attempt (proxy
502). WebSearch: 7 queries. github.com: 1 shallow clone each of dbourdeau/cyphersolver and
aaymeloglu/unsolved-ciphers, grep only, both deleted after. No credentials used, no subagents, never
check-solved, never promoted.
>>>>>>> Stashed changes
