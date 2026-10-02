# Intercepted royalist letter (21 May 1646)

- **Source:** BL Add MS 72438, f.9r. DECODE record R8623. Tomokiyo believes it is undeciphered.
- **Status:** partial (2 Oct 2026, LIKELY-9: key no. 129 as reconstructed by Aymeloglu reads 190 of 735 tokens of f.10 above 20 shuffled keys, rank 1/21; was Open since 19 Sept 2026).
- **Transcription:** `ciphertext.txt` holds only the opening, as quoted on unsolved.htm. The full text must be transcribed from the DECODE image (R8623).
- **Related:** BL Add MS 72438 f.10 (DECODE R8624), an intercepted letter to Charles I of 13 May 1646, is also undeciphered and may share the cipher.
- **Ideas:** Mixed cleartext and one- to three-digit code groups. Highest seen so far 333. Cleartext anchors ("beholding to 309 for", "Messenger", "communicate") give word-class hints for the adjacent groups.
- **Solver status (19 Sept 2026):** Partial by Aymeloglu (unsolved-ciphers/royalist-1646), 16 Sept 2026. Note the folder covers two letters: f.10 (13 May, to Charles I) is Digby key no. 129 with about 45 values fixed; f.9 (21 May, the opening quoted here) uses a smaller key in which 226 = London. Needs the rest of key 129 or the contemporary decipher.

## Scout addition: f.104 and the volume's keys, 20 Sept 2026

A proposed fourth candidate (a separate letter, BL Add MS 72438 f.104, "almost wholly in undeciphered cipher")
was checked against this folder rather than filed as a new target, since it is the same volume. Findings, not
yet acted on:

- **The volume is Weckherlin's, not "Nicholas Papers":** BL catalogue title (searcharchives.bl.uk/catalog/040-001967027,
  checked 20 Sept 2026) is "Cipher-keys and intercepted royalist correspondence from the papers of Georg
  Rudolph Weckherlin, government official, 1625-1647." Digital images: "currently unavailable" (BL viewer
  offline since the 2023 cyber attack).
- **f.104 entry (verbatim, matching /tmp/cyphersolver/rupert/NOTES.md's own quote):** "f. 104r: Royalist
  intercepted letter almost wholly in undecoded cipher, n.d." No sender/date/recipient given in the catalogue,
  so no print-edition search was possible (nothing to search on). A second item, f.171r, is in the same
  state ("undecoded") per the same source but has no DECODE record in the harvested set below, so its coverage
  is unclear.
- **DECODE status conflict — do not treat f.104 as an open target without resolving this.** f.104 has its own
  DECODE record, **no. 8725** (https://de-crypt.org/decrypt-web/RecordsView/8725), confirmed by raw HTML:
  "Type: Cipher | Status: **Decrypted** | Cipher Type: Unknown | Symbol Sets: Numerical | Pages: 1 |
  Author/Sender/Receiver: blank | Access mode: Authentication required." This is the opposite of f.9 and f.10
  (DECODE records R8623/R8624), both explicitly "Non-decrypted" in the same harvested catalogue
  (`/tmp/unsolved-ciphers/catalogue/decode-catalog.csv`). Tomokiyo's unsolved.htm does not list f.104 at all
  (grepped `sources/cryptiana/web/unsolved.htm` for "72438" and "104": only f.9/R8623 and f.10/R8624 appear),
  which is consistent with DECODE marking it already solved rather than with Tomokiyo having simply missed a
  live target. Neither solver repository flags this DECODE status (Aymeloglu's `royalist-1646` folder never
  engaged with f.104 at all; Bourdeau's `rupert/NOTES.md` names the folio only from the archival "no
  contemporary decipherment survives" sense, not DECODE's project-status sense). **No DECODE credentials are
  available in this environment** (checked; `DECODE_USER`/`DECODE_PASS` unset), so record 8725's actual
  plaintext/decipherer could not be read. Resolve this — with a DECODE login — before requesting a physical
  copy of f.104 or including it in any campaign.
- **Keys in the volume**, extending the "49 captured Digby keys" figure already in `LANDSCAPE.md` (sourced from
  `/tmp/cyphersolver/TARGETS.md`): the index leaf f.25, "Cyphers taken in the Lord Digby's cabinet" (Sherburn,
  Oct 1645), numbers the captured keys roughly 80-139; surviving key pages run across ff.25/27-99 (not all 60
  numbered slots survive as separate leaves, which is where "49" comes from). Cross-checked independently in
  both the BL catalogue and Aymeloglu's own from-the-record research (`/tmp/unsolved-ciphers/royalist-1646/README.md`):
  f.27 = key no.84 (Bennet); f.52 = no.113 (Digby & Vavasour); f.70 = no.125 (Mr Browne, ~700-entry key);
  f.77 = no.129 (unnamed, "from the Queen's Court" — the key already in partial use on f.10 above); f.78 =
  no.130 (Col. Hurliston, syllabary); f.82 = no.132 (Sir Kenelm Digby). Beyond ff.25-99, the catalogue also
  lists cipher-key items at ff.100-101 (King & Queen), 102-103 (Digby/Walsingham), 105-106, 108-109
  (unidentified royalist keys — not yet matched to a name), then Weckherlin's own diplomatic cipher-books
  ff.110-170 (a different, unrelated haul: Latin cipher-book ff.124-141, Augier ff.151-158, Waller ff.162-163).
  f.104 itself is not catalogued as a key; it sits as the one non-key "intercepted letter" leaf between the
  f.102-103 and f.105-106 key items.
- Any of ff.100-101, 102-103, 105-106 or 108-109 ("unidentified royalist keys") could in principle be the rest
  of key no. 129 that f.10's reading still needs, or the key for f.9's smaller cipher — worth requesting
  alongside f.11 (already planned) once a DECODE login clarifies whether f.104 is actually open. See
  `REQUEST.md`.

## Check-solved sweep, 20 Sept 2026

Six independent searches run against the 16 Sept 2026 claim (Aymeloglu, unsolved-ciphers/royalist-1646:
f.10 = Digby key no. 129, ~45 values fixed; f.9 = a smaller, different key in which 226 = London; both
need the rest of key 129 or a contemporary decipher). None found a decipherment of f.9 or f.10 anywhere.
One found a genuine independent disagreement about the claim itself, detailed below.

**1. Web search + direct fetches (github.com/aaymeloglu, dbourdeau.github.io, de-crypt.org RecordsView).**
Re-confirmed Aymeloglu's own partial-decipherment claim verbatim on the live repo. Fetched Bourdeau's
*rendered docs page* (dbourdeau.github.io/cyphersolver/index.html) and found no mention of this target
there — see source 5 below, which cloned the underlying repo and found this was a false negative from
checking the rendered site rather than the source files. DECODE RecordsView pages for 8623 and 8624 both
read "Non-decrypted". Noted that nearly every WebSearch query returned an identically-worded synthesized
summary regardless of phrasing, i.e. all roads led back to the single Aymeloglu page, not independent
corroboration. Cipherbrain and the Cryptiana blog's own search boxes were not reachable via WebFetch/WebSearch
site-scoping in this pass — **unchecked**, not negative.

**2. Printed-edition search (CSPD Domestic Charles I, Rushworth, HMC/Downshire).** Downloaded and
full-text-searched the Internet Archive OCR of *Calendar of State Papers Domestic, Charles I* (ed. Hamilton,
1891, covering 1645-7; archive.org id `calendarofstatep0021will`). Result: **no 21 May 1646 entry exists in
the calendar at all**, the three 13 May 1646 entries in it are unrelated routine Derby House business, the
volume's own "Deciphered Letters" appendix (keys supplied by Col. J. S. Rothwell) stops at 11 Jan 1645/6 and
does not reach May 1646, and the only calendar entry touching this Weckherlin cipher haul at all is a 31 Jan
1645/6 finding-list summary (p.331) with no text of any individual letter. Rushworth vol. 6 (Mar-May 1646,
British History Online) has nothing matching either. No sender name is recorded for f.9/f.10 anywhere, so no
sender-specific "Letters"/"Correspondance" edition could be searched. British History Online's page-level text
for CSPD pp.430-439 (the free archive.org OCR of the same edition was used instead) is paywalled —
**unchecked** at that specific URL, though covered via the substitute text.

**3. Community list / comment-thread sweep (Cryptiana, Cipherbrain, Cipher Mysteries, MysteryTwister, r/codes).**
Cryptiana's `unsolved.htm` (local snapshot) lists both f.9/R8623 and f.10/R8624 verbatim as items S. Tomokiyo
"believe[s] ... not deciphered", with no solution and no comment thread (a static list page, not a blog post).
Tomokiyo's other Add MS 72438 pages (digby.htm, charlesi.htm, charlesii.htm, louisxiv0.htm) cover other folios
of the same volume in detail but never mention f.9, f.10, R8623, R8624 or key no. 129. Cipher Mysteries' own
site search for "Weckherlin" returned an explicit "Nothing Found." No Cipherbrain, MysteryTwister or r/codes
thread naming this target was found by web search. Cipherbrain.de itself (503 on WebFetch, TLS failure on
direct curl) and reddit.com/r/codes (WebFetch domain-refused, curl 403) could not be queried directly —
**unchecked** by their own search tools, though WebSearch site-scoping against both returned nothing.

**4. DECODE (de-crypt.org) direct.** Confirms record 8623 (f.9, 21 May 1646) and record 8624 (f.10, 13 May
1646) both "Non-decrypted", Cipher Type "Unknown", Access mode "Authentication required", Author/Sender/
Receiver all blank in DECODE's own fields (DECODE does not itself record "to Charles I" for f.10; that
description is from NOTES.md/Tomokiyo, not from DECODE). Sender-family site searches for "Weckherlin",
"Digby" and "Charles I" do not surface 8623/8624 (Digby surfaces other 72438 key folios instead), consistent
with those two records carrying no sender/receiver metadata in DECODE. The Documents/Images sub-pages for
both records, where an attached key or decipherment file would be listed, redirect to `/decrypt-web/login`;
`DECODE_USER`/`DECODE_PASS` are unset in this environment — **unchecked**, so an attached key or decipherment
file on DECODE itself can be neither confirmed nor ruled out.

**5. github.com/dbourdeau/cyphersolver (cloned, HEAD cf73f46).** This is the significant independent result.
Bourdeau's repository does carry this exact shelfmark, but files it under `rupert/` (item #6, alongside a
separate 1645 Maurice-to-Rupert letter), not under a `royalist-1646` folder, which is why source 1's fetch of
the rendered docs page missed it. Bourdeau's own status for BL Add MS 72438 ff.9-10 (DECODE R8623, R8624) is
**"offline-only"**, not "partial", and his notes give **no key attribution at all** — no Digby key no. 129, no
"226 = London" claim. Verbatim: "Full ciphertext is not available anywhere online: cryptiana prints only the
first two lines of f. 9 ... DECODE records are 'Private Ciphertext: True', authentication required; the BL
digitisation (vdc_100162920089) is offline (403) ... The same volume holds 49+ keys (ff. 25-99, 100-109,
151-170) that would very likely read f. 9/f. 10 by simple trial once images are accessible — this is a 'key in
the same box' situation like Hamilton, not a cryptanalysis problem." `TARGETS.md` and both rendered docs pages
(`writeups.html`, `index.html`) repeat the same "offline-only" / "waiting on an archive" framing, with no
mention of key no. 129. Neither `SOLVED_CATALOGUE.md` nor `SOLVED_RANKING.md` lists this item. Bourdeau's
working notes carry no date of their own beyond the clone's HEAD (19 Sept 2026); no other blocker.

**6. github.com/aaymeloglu/unsolved-ciphers (cloned) + github.com/robertpitt (via GitHub API).** Re-confirms,
from the repo's own files rather than a rendered page, Aymeloglu's 16 Sept 2026 claim in full: `README.md`,
`TARGETS.md` and `royalist-1646/README.md` all state f.10 = Digby captured-cabinet key no. 129 ("from the
Queen's Court", also used by the King June-August 1646), "about 45 values fixed from the surviving key page
and Evelyn's printed decipherments," full reading needing the rest of the key or the contemporary decipher;
f.9 "[n]ot attacked beyond noting that it uses a different, smaller key (max value 343) in which 226 reads
'London'." Flags one unresolved discrepancy worth carrying forward without resolving here: Aymeloglu's own
`f9_ct.txt` gives a max value of 343 for f.9, where this project's `ciphertext.txt` (only the Cryptiana-quoted
opening) shows a highest value of 333 — the two transcriptions were made independently and have not been
reconciled. A search of all 40 of github.com/robertpitt's repositories (API `search_repositories` +
`search_code`, both pages) found no repository or code referencing "72438", "weckherlin" or "royalist-1646";
that route is a clean negative, not unchecked.

**People and dates for prior work, consolidated:** S. Tomokiyo (Cryptiana `unsolved.htm`, undated static
page, first source establishing both folios as unsolved) — Aymeloglu (`unsolved-ciphers/royalist-1646`,
16 Sept 2026, key-129 partial attribution for f.10, "226 = London" note for f.9) — Bourdeau
(`cyphersolver/rupert/`, repo state 19 Sept 2026, independently reaches the same shelfmark but calls it
offline-only with no key identified) — no archive, editor, forum or database (DECODE, CSPD, Rushworth,
Cipher Mysteries, Cipherbrain, MysteryTwister, r/codes, robertpitt) has published or claims a decipherment of
either folio.

**Verdict:** Still open — no decipherment of BL Add MS 72438 f.9 (R8623) or f.10 (R8624) exists anywhere
that six independent searches could locate; Aymeloglu's 16 Sept 2026 partial key-129 attribution for f.10 is
neither corroborated by any source outside Aymeloglu's own repository nor contradicted by direct evidence,
but Bourdeau's independently-derived assessment of the identical shelfmark does not support it (offline-only,
no key identified) — treat the key-129 attribution as an unverified, single-source claim pending the rest of
the key or a contemporary decipher, not as confirmed independently.

## Print check, 20 Sept 2026

Free-source check for the contemporary decipher of f.10 (or f.9) that QUEUE.md flags as undone, following the
route suggested there: Bodleian Tanner MSS 59-60 and TNA SP 16/514.

1. **Bodleian Tanner MSS 59-60 / TNA SP 16/514, printed calendars.** No free online printed calendar of the
   Tanner MSS was located (the Bodleian's own Tanner catalogue is a manuscript finding-aid, not a printed
   edition); TNA Discovery API returned nothing under SP 16/514 (see item 6). No relevant match.
2. **Cary, *Memorials of the Great Civil War in England from 1646 to 1652* (1842),** both volumes, full text
   from Internet Archive (`memorialsofgreat01caryuoft`, `memorialsofgreat02caryuoft`; Cary's own preface says
   the work is drawn from the Tanner collection). Grepped for cipher/decipher terms near the two target dates:
   the only cipher item near them is Edward Hyde to Richard Arundel, Jersey, 15 May 1646, "written with General
   Digby's cipher" (vol.1 pp.45-49) — a different correspondent pair, different date, sent from Jersey rather
   than intercepted in England. No entry for 13 or 21 May 1646 of any kind in either volume. No relevant match.
3. **Journals of the House of Lords and Commons, May 1646.** Lords Journal vol.8 (13 and 21 May 1646, pp.314-
   315 and 321-324) and Commons Journal vol.4 (13 and 21 May 1646, pp.543-545 and p.552), fetched from British
   History Online and grepped for cipher/decipher/intercept/Digby/Weckherlin: zero matches on any of the four
   pages. No relevant match.
4. **Rushworth vol.6, second route.** Internet Archive's cross-corpus full-text search API (independent of the
   British History Online check already logged above) for "Digby's cipher" and "key no. 129": only hits were
   the same Cary/Hyde-Arundel letter (also digitised separately) and unrelated catalogue/bibliography entries
   for a distinct 1644 pamphlet titled "Lord Digby's cipher." No 13/21 May 1646 Rushworth match by this route
   either. No relevant match.
5. **Digby cabinet material / key no.129 in print.** Same full-text search, plus `"key no. 129" Digby` (zero
   hits): no printed edition or calendar names key no.129 anywhere outside the solver repositories already
   cited above. No relevant match.
6. **TNA Discovery API.** `/API/search/records` 500-errors on any query containing a literal "/" (a reproducible
   server-side bug, not an egress block); worked around with slash-free date-scoped queries ("intercepted
   letter", "cipher key", "Digby cabinet", "cipher 129", "Weckherlin", all dated 1646). All returned either zero
   results or results unrelated to SP 16/514 or Add MS 72438. The API's `sps.reference` parameter does not
   filter by document reference, so a direct SP 16/514 lookup by shelfmark could not be completed. No relevant
   match.

**Verdict:** Not found in the sources checked here — no decipherment, contemporary transcription, or reference
to key no.129 for f.9 or f.10 turned up in Cary's Memorials, the Lords/Commons Journals on the exact dates, a
second-route Rushworth full-text search, print references to Digby's captured cipher keys, or TNA Discovery's
catalogue descriptions. This does not change REQUEST.md.

## DECODE record 8725, read 20 Sept 2026

First use of the DECODE (de-crypt.org) login from this environment. The login flow itself now works and is
recorded in `CLAUDE.md`'s Access playbook item 3, with `tools/decode_fetch.sh` as the reusable helper — but
the `DECODE_USER`/`DECODE_PASS` credentials set in this environment were **rejected** by the server
("Incorrect user name or password", confirmed by screenshot after a real form submission with a fresh CSRF
token; not a client-side or scripting fault, since a plain curl replication of the exact browser request
failed identically). Record 8725 (f.104) could therefore **not be read** this session: its "Decrypted" status
basis — who deciphered it, when, whether a plaintext or key file is attached, contemporary vs. modern — is
still unknown. This is not "unset credentials" (rule out that case first: both variables are set, non-empty,
no stray whitespace) but a rejected login; do not retry it repeatedly against the live account, since the
site's own phrase table warns of an account lock after too many failed attempts. Getting a login that the
server accepts is now a task for the person (new/corrected credentials), not a technical blocker.

No images or files for 8725 were fetched (login never succeeded), so `/tmp/decode/8725` holds nothing beyond
`tools/decode_fetch.sh`'s own failure marker, and nothing from this session is committed under `images/`.

## DECODE record 8725 (24 Sept 2026)

Login now works (`CLAUDE.md` Access playbook item 3, "Resolved 24 Sept 2026, 04:40 UTC": the curl POST in
`tools/decode_fetch.sh` is never evaluated by the server; `tools/decode_browser_login.js`, a real headless-Chromium
submission, logs in first try). This session extended that tool with `--fetch`/`--fetch-page`/`--delay`/`--max-files`
options (downloads inside the same logged-in browser context, auto-following any `/decrypt-custom/filesrv/?file=`
link found on a fetched list page) and added `tools/tests/test_decode_browser_login_help.py` as an offline `--help`
smoke test, then ran it once (one login) for record 8725, plus one further login to search RecordsList for
sibling records in the same volume (see below). Files saved under `ciphers/intercepted-royalist-1646/decode/`:
`record_8725.html`, `DocumentsList.html` (both scrubbed of the account name), the two attached documents, and the
two page images; `siblings.tsv` from the RecordsList search. Requests to de-crypt.org: 3 logins (main fetch run,
one aborted ImagesList diagnostic, one RecordsList search run) + roughly 15 page/file GETs total, all ≥1.5s apart,
well under the few-hundred-per-session budget.

**Record 8725 = BL Add MS 72438 f.104, confirmed again:** RecordsView shows Status **Decrypted**, Cipher Type
Unknown, Symbol Sets Numerical, 1 page. `DocumentsList?showmaster=records&fk_id=8725` lists two attached documents:

| doc id | title | category | uploaded | uploader |
|---|---|---|---|---|
| 4349 | "Cipher between Charles I and Prince Rupert (1647)" | Key | 10/12/24 | account id 83 |
| 4350 | "Decipher of the beginning" | Deciphered text | 10/12/24 | account id 83 |

DECODE gives only a numeric uploader id (83) in the fields this account can see, not a name — consistent with the
project's own convention, nothing to redact. The titles themselves are new information: f.104 has no sender/date
in the BL catalogue description ("Royalist intercepted letter almost wholly in undecoded cipher, n.d.", logged in
the Scout addition above), but DECODE's own metadata for this record now names the correspondents and date as
**Charles I and Prince Rupert, 1647** and confirms a "Deciphered text" document exists for it.

**Content of both documents could not be read.** Fetching either attachment's file
(`DOC_8725_2024-Oct-12-01-33-12_24005.jpg` for the Key, `DOC_8725_2024-Oct-12-01-36-20_15694.txt` for the
Deciphered text) returns, for both, a byte-identical 17,947-byte PNG (not the named format — the filenames'
extensions do not describe the actual returned content) reading "Insufficient permissions to see the full image"
in plain black text on white. This is a server-generated placeholder, not the file — this account has RecordsView/
DocumentsList *metadata* access but not Documents *content* access. `ImagesList?showmaster=records&fk_id=8725`
("Manage Images" / "Image Manager" in the record page's own UI) is unreachable for the same evident reason: both a
full page navigation and a plain authenticated HTTP GET to that URL end in `ERR_TOO_MANY_REDIRECTS` /
"max redirect count exceeded" (tested once each, not retried further, consistent with the good-citizen single-retry
rule for anomalous host behaviour). What *is* reachable: the two page-image thumbnails already known from the
record page, `TH_IMG_R8725_I40320_P1.jpg` (200×268, a real manuscript recto in a secretary hand — legible as a
short block of running text, not obviously cipher symbols at this resolution, but too small to transcribe) and
`TH_IMG_R8725_I40320_P2.jpg` (200×267, blank/verso, folded). Both downloaded successfully and are committed.

**Is this a found-solved lead for our leaf?** Record 8725 *is* f.104 (established independently in the Scout
addition above), so the "Decipher of the beginning" document is attached to the very folio in question, not a
different one — DECODE's own project has therefore marked f.104 as already deciphered, at least in part. But this
session could not read that document's actual text (permission-blocked), so per the brief's instruction the first/
last ten words of its plaintext cannot be quoted, and it cannot be confirmed whether "the beginning" means a few
lines or a full transcription, nor whether it is a contemporary or modern decipherment. This is a **found-solved
lead, not a confirmed found-solved reading**: report to whoever picks this up next that DECODE record 8725
(f.104) carries a named, dated attachment titled "Decipher of the beginning" that this account cannot open: the
person (or a worker with different DECODE credentials/role) needs to open it directly, e.g. via
`https://de-crypt.org/decrypt-web/DocumentsList?showmaster=records&fk_id=8725` while logged in with a role that
has document-download permission, or by asking DECODE's maintainers for the file. Not classifying novelty here
(rule 10) — that is the verifier's job once the text is actually read, and this is not a reading yet, only a
provenance/status finding about f.104's record.

**This target's own scope (f.9/f.10) is unaffected and still open.** f.104 was never adopted as a target of this
folder, only flagged as a candidate pending this DECODE check (see the Scout addition above); the top-line
`Status: Open` refers to f.9/f.10 and is not changed by this f.104 finding. That check is now resolved: **do not
promote f.104 as a fresh cryptanalysis target** — DECODE already holds (even if this account cannot read) a
named decipherment for it, so any campaign on f.104 should start from requesting that document, not from
transcribing and attacking the cipher again.

**RecordsList search for "72438" (siblings, `decode/siblings.tsv`, all 5 pages / 81 records fetched).** Confirms,
independently of this folder's own file, that f.9 (record 8623) and f.10 (record 8624) are still the *only* two
"Cipher" records under Add MS 72438 marked **Non-decrypted** by DECODE; every other Cipher-type record in the
volume (f.1, f.3-4, f.5-6, f.7, f.12-13, f.14-15, f.104, f.107 — 8 records) is already Decrypted, and 71 further
records are Key-type (status N/A, not applicable to a cipher/decrypted distinction). f.107 (record 8728) is a
second already-Decrypted single-page Cipher record adjacent to f.104 worth noting for later but out of this
brief's scope (no document check run on it). This corroborates the folder's existing "Verdict: Still open" for
f.9/f.10 from an independent DECODE-side source (status field, not a text search), rather than changing it.

## DECODE fetch, 25 Sept 2026

LANE DX job 2 (the one DECODE login worker), one login, `tools/decode_browser_login.js`. Re-fetched record 8725
(f.104) in the same run as records 413, 4930, 1172 and 1180 (owed to sibling clusters; those four are filed under
their own targets' `decode/` folders, not here — see `ciphers/boswell-1628/NOTES.md`,
`ciphers/randolph-sussex-1569/NOTES.md`, `ciphers/bne20211-ferdinand-1478/NOTES.md`).

| file | bytes | sha1 | content |
|---|---|---|---|
| record_8725.html | 121578 | 84bb8d5f9fc2f28a8bff9010051cb6de85b8e816 | real (RecordsView metadata; unchanged from 24 Sept: Status Decrypted, Cipher Type Unknown, Symbol Sets Numerical, 1 page) |
| TH_IMG_R8725_I40320_P1.jpg | 14280 | 95245bec0fb2ece60a4f4e2fcb7abc4e9fb84aad | real thumbnail, unchanged |
| TH_IMG_R8725_I40320_P2.jpg | 8466 | 84b80b1617bd8e0268db8f2035a9b0d12ce2dbf7 | real thumbnail, unchanged |
| IMG_R8725_I40320_P1.jpg, IMG_R8725_I40320_P2.jpg | 17947 each | 035489a0605851154ab88372216354b63596ca22 | **placeholder** ("Insufficient permissions to see the full image"), same sha1 as 24 Sept and as the owner's own browser test |
| DOC_8725_2024-Oct-12-01-33-12_24005.jpg, DOC_8725_2024-Oct-12-01-36-20_15694.txt | 17947 each | 035489a0605851154ab88372216354b63596ca22 | **placeholder**, same as 24 Sept — the "Decipher of the beginning" document is still unreadable by this account |

No change from the 24 Sept 2026 finding: this account has RecordsView metadata access to record 8725 but not
Documents/full-image content access. `ASKS.md` row 1 updated with today's date. Requests to de-crypt.org this run:
2 (login) + 1 (primary RecordsView) + 4 (`--fetch-page` for 413/4930/1172/1180) + 32 (auto-discovered/guessed
filesrv links across all five records) = 39, all ≥1.5s apart, well under the session cap. One login only.

## LIKELY-9 (2 Oct 2026, account-4)

Worker LIKELY-9-intercepted-royalist-1646 (Fable 5.1), brief `.claude/briefs/runs/2026-10-02-account4-likely-phase2.md`, row 9 of `ciphers/_triage/likely-solves-2026-10-02.tsv`. Disk only after one shallow clone of github.com/aaymeloglu/unsolved-ciphers (commit d2800bb2, 27 Sept 2026) to the scratchpad, deleted after; 0 vision calls, 0 subagents, 0 requests to any other host. Files: `f10_ct.tsv`, `f9_ct.tsv` (his transcriptions quoted with attribution, converted to the `tools/decode_key.py` tsv layout), `key.tsv` (his key129.txt with a grade and source column, rule 4), `decode.json`, `reading_f10.txt`/`reading_f9.txt` + token files (regenerated by `python3 tools/decode_key.py ciphers/intercepted-royalist-1646`, `--check` passes), `likely9/run.py` (the control), `likely9/results*.json`, `likely9/text_*.txt` and `likely9/judge_*.txt` (judge inputs and outputs), `HYPOTHESES.md` (new), `specs/intercepted-royalist-1646.json` (new, Pipeline 3a, with `cheap_test_done`).

**Intake gate.** `python3 tools/intake_gate_check.py intercepted-royalist-1646` -> `intercepted-royalist-1646: offline-only (line 137) -- already terminal, nothing to gate`, exit 0. That is a mis-parse, flagged for the parent: line 137 is this file's quotation of Bourdeau's status for the same shelfmark (`cyphersolver/rupert/`, "offline-only"), not this folder's status, which line 4 gave as `Open` (now `partial`, below). The triage row's "status word reads offline-only" came from the same line. The six-source check-solved sweep of 20 Sept 2026 above carries its verdict and the editions read (CSPD 1645-7 full text, Rushworth vi, Cary, the Lords/Commons Journals); the 2 Oct web/blog step in `check-solved.md`'s format is not written here (this brief allowed no network beyond the one clone), so a check-solved worker owes that one step before any campaign.

**Known answer first (README common tail).** None on disk. The key's known-plaintext witness is Nicholas's interlinear decipherment of the King's letters of 24 June and 16 Aug 1646 in Evelyn, *Diary and Correspondence* (1857) iv 178-179 (archive.org `diarycorresponde41evel`, leaves 186-187 per Aymeloglu), which fixes 23 of the 45 H values; not fetched (no network in this brief). The only read text on f.10 is its 73 clear fragments; on f.9 its 16.

**Grades (rule 4), key.tsv (65 values).** H 45: 22 names from the surviving key page f.77 (`f77`), 23 words from Evelyn's printed period decipherment (`evelyn`). M 18: 13 letter homophones from Aymeloglu's "loose interlinear alignment" of Evelyn's spelled words (`evelyn-align`), 4 values whose source his README does not name (162 for, 197 had, 200 having, 356 Southampton), 351 "my?" marked doubtful by him. I 2: 430 your, 543 Majesty, fixed from f.10's own opening. Every grade is conditional on his transcription of f.77 and of Evelyn's page scans (rule 2: neither image is on disk here). 370 = "tion" (his commented guess from "d i r e c 370" twice) is not in the key.

**Grades per token.** f.10: 735 cipher tokens (20 of them a bare `?`, illegible or torn): H 69, C 0, S 0, M 109 (all M-graded key values; the 20 bare `?` and the tokens whose transcription carries a `?` are counted U, value unknown), I 12, U 545 not in the key; plus 73 clear fragments. 190 tokens carry a value. f.9: 151 cipher tokens: H 0, C 0, S 0, M 12 (all letter homophones), I 0, U 139; plus 16 clear fragments. No C: this is a key application on a third party's key, not a cryptanalytic result, and nothing here is "read" in the sense of rule 7 beyond what the key gives.

**The test (rule 3): key129 vs 20 value-shuffled copies of itself, `likely9/run.py`.** A shuffled key keeps the 65 codes, so coverage (190/735) cannot differ by construction (the bCAS lesson) and is not the statistic. Three statistics that depend on which value lands where, each on the maximal readable runs (clear + keyed tokens; an unkeyed token breaks a run) containing at least one keyed token: `lm`, mean log10 4-gram letter probability (`tools/judge_plaintext.py`'s NgramModel); `wbg`, mean log10 word-bigram probability over adjacent readable words with a keyed member (add-k, unigram backoff); `cover`, the judge's word cover. Two corpora: `en16_repo` (this repository's own readings of Thurloe's printed 1650s state letters, the nearest register on disk, no fold check at this N) and `LANG_CORPORA["en"]` (two 19th-c. novels, **of unknown reliability**, `tools/data/en/README.md`). 20 shuffles are the brief's gate; 200 and a stratified shuffle (letters among letter codes, words among word codes) are supplements in `results.json`.

| text, key | keyed / tokens | letters, runs, pairs | corpus | lm real vs shuffle mean / max (rank, z) | wbg real vs mean / max (rank) | cover real vs mean / max (rank) |
|---|---|---|---|---|---|---|
| f.10, key129 all 65 | 190 / 735 | 609, 139, 59 | en16_repo | -1.576 vs -1.846 / -1.704 (**1/21**, z 2.66; 1/201) | -3.868 vs -4.184 / -3.861 (2/21; 3/201) | 0.581 vs 0.462 / 0.575 (1/21; 2/201) |
| f.10, key129 all 65 | 190 / 735 | 609, 139, 59 | en | -0.837 vs -1.258 / -1.134 (**1/21**, z 5.19; 1/201) | -3.061 vs -4.095 / -3.669 (1/21; 1/201) | 0.793 vs 0.771 / 0.859 (8/21) |
| f.10, H rows only (45) | 69 / 735 | 295, 63, 21 | en16_repo | -1.534 vs -1.855 / -1.683 (**1/21**, z 3.07; 2/201) | -4.031 vs -4.515 / -4.189 (1/21; 2/201) | 0.725 vs 0.460 / 0.577 (1/21; 1/201) |
| f.10, H rows only (45) | 69 / 735 | 295, 63, 21 | en | -0.885 vs -1.307 / -1.102 (**1/21**, z 3.21; 1/201) | -3.127 vs -4.019 / -3.436 (1/21; 1/201) | 0.895 vs 0.755 / 0.862 (1/21; 3/201) |
| f.9, key129 all 65 | 12 / 151 | 44, 12, 3 | en16_repo | -1.705 vs -1.806 / -1.575 (6/21) | -5.100 vs -4.237 / -4.108 (21/21) | 0.636 vs 0.533 / 0.746 (3/21) |
| f.9, key129 all 65 | 12 / 151 | 44, 12, 3 | en | -0.865 vs -1.115 / -0.893 (1/21, z 1.5; 22/201) | -4.009 vs -3.759 / -3.668 (21/21) | 0.659 vs 0.771 / 0.911 (18/21) |

Stratified shuffle (harder control, 20 seeds): f.10 all-65 rank 1/21 on all three statistics under both corpora (en16_repo z 3.9 / 3.7 / 4.9). The control can fail differently from the target (shuffle sd 0.08-0.22 on each statistic), so this is a test, not a non-test.

**Reading of the numbers.** Key129 as reconstructed reads f.10 above its shuffled-key control on the letter 4-gram and the word bigram under both corpora, at rank 1 of 21 (1 of 201 on lm), and the margin survives removing the two values Aymeloglu fixed from f.10 itself and the 13 alignment-derived letters (H-only rows: rank 1/21 on all three statistics, both corpora). That corroborates his attribution of f.10 to key no. 129 with a control -- it does not read the letter: 545 of 735 tokens have no value, the key's 45 H values rest on a transcription of f.77 and of Evelyn's page that nobody here has seen, and the spelled-letter runs (his 218 letter tokens, 13 homophones fixed) are mostly suffixes and fragments ("596 d", "585 s", "d i r e c 370"). f.9 shows nothing under this key (12 letter homophones only, word bigram rank 21/21), consistent with his note that it is a different, smaller key (max 343, 226 = London by the f.4 key) -- not a negative on f.9's own key, which was not tested. The row's third clause (`print_check.py` on decoded phrases against the Clarendon calendar) was not run: network. The row's "715 tokens" counts f.10 without its 20 bare `?`; "156" on f.9 is his count, 151 is what the tsv parse yields (the `[comunicate]`-style clear fragments are not tokens).

**Judge** (`python3 tools/judge_plaintext.py specs/intercepted-royalist-1646.json --file ciphers/intercepted-royalist-1646/likely9/text_f10.txt`, the readable text with unkeyed tokens dropped, 970 letters; spec corpora = en16_repo):
```
FAIL language: score=-1.695, null_p99=-1.923, real_p05=-0.6, real_median=-0.223, mode=both, N=970
ok   words: cover=0.585, min=0.5, real_text_median_cover=0.871
FAIL - intercepted-royalist-1646 (a PASS is a gate for a verifier, not a reading; rule 10)
```
Shuffled-target decode (cipher tokens permuted among cipher positions, clear words in place, seed 1; `likely9/judge_f10_shuffled_target.txt`): `FAIL language: score=-1.718 ... ok words: cover=0.582`. Under the default `en` judge (unknown reliability): candidate `FAIL -1.052 vs real_p05 -0.861, words ok 0.859`; shuffled target `FAIL -1.141, words ok 0.853`. f.9: `FAIL -1.62` (en16_repo). The judge FAILs the candidate and its shuffled target alike, 0.02-0.09 apart against a gap of 1.1 to real_p05: at 190 of 735 tokens keyed the text fed to it is clear scaffold plus scattered words, and the judge neither PASSes (so it is not voided the ARM-C1 way) nor discriminates. Not a negative; the shuffled-key control above is the instrument for this test. Note for the parent: en16_repo's `real_median -0.223` is in-sample (a 240 KB corpus of our own readings), so its real_p05 is a strict bar; a fold check on it has not been run.

**Status: `partial`** (rule 5: a key beat its matched control by a reproducible margin; 69 H tokens + 12 I + 109 M values stand on f.10, image-unchecked). Not "reading ready": the judge did not clear. Never "new" or "first": every value here is Aymeloglu's (16-27 Sept 2026), credited by repository, commit and path. For the parent: a NEAR.md row (rule 5) with the rank-1/21 numbers and the next step below; `status.json` is the orchestrator's.

**Suggestions, one line each (Usage 7, not run):** (a) the known answer: fetch Evelyn iv 178-179 leaves 186-187 from archive.org once (2 requests), re-read the 23 Evelyn values and the 13 letters from the page, regrade; ~$3. (b) f.9's own key: Aymeloglu says 226 = London by "the key recovered from the deciphered f.4 intercept of 1645" -- DECODE's f.4 record is Decrypted (siblings.tsv, 24 Sept) and its key document is content-blocked for this account (ASKS row 1); the f.4 key, once readable, is f.9's first cheap test. (c) the 0-99 letter homophones: his anneal control read 0.07-0.12, so no further anneal at this length; the suffix runs after word codes ("596 d", "585 s", "430 depart") are the hand-crib route, ~$2 on Sonnet with the H words as anchors.

## Remaining gaps (LIKELY-9, 2 Oct 2026)
Read so far: 190 of 735 cipher tokens on f.10 carry a key value (H 69, I 12, M 109; reading_f10_tokens.tsv), rank 1 of 21 shuffled keys; 12 of 151 on f.9 (letters only, no signal); the clear fragments (73 + 16) are read as transcribed
- the 545 unkeyed tokens of f.10 (word codes 100-430 and names 431-580 beyond the 45 H rows; the unexplained 581-697) - blocker: no-key-material; only one page of key 129 survives (f.77, names 559-580; Aymeloglu checked every other DECODE record of the volume) and the candidate rest-of-key leaves ff.100-109 are in REQUEST.md item 2, BL viewer offline since 2023
- the 45 H values and 13 letter homophones, image-unchecked (rule 2) - blocker: not-attempted; Evelyn iv 178-179 page scans (archive.org diarycorresponde41evel leaves 186-187) were not fetched, no network in this brief; next: fetch once, re-read the 23 Evelyn values + 13 letters from the page, regrade key.tsv, ~$3
- the letter homophones 0-99 beyond the 13 fixed (218 letter tokens on f.10) - blocker: open-codes; Aymeloglu's anneal control read 0.07-0.12 at this shape (his README), so no annealer run; the suffix runs after word codes are the hand-crib route (suggestion c)
- f.9's own key (max 343, 226 = London per the f.4 key) - blocker: waiting-on ASKS row 1; DECODE document content access: the f.4 record's key document is content-blocked for this account (NOTES.md 24-25 Sept 2026)
- the contemporary decipher of f.10 (f.11; Tanner 59-60; SP 16/514) - blocker: needs-physical-access; REQUEST.md item 1 and the print check of 20 Sept 2026 above (not found in Cary, the Journals, Rushworth, TNA Discovery)
- f.10 and f.9 transcriptions, image-unchecked (20 bare ? on f.10) - blocker: waiting-on ASKS row 1; DECODE full-size images are account-wide blocked (24-25 Sept 2026) and BL vdc_100162920089 is offline

## Escalation (2 Oct 2026)
- [x] siblings: the volume's other Add MS 72438 cipher records are all Decrypted or Key-type on DECODE (siblings.tsv, 24 Sept); Aymeloglu tried every other key in the volume against f.10 (Browne 125, Bennet, Digby, Hurleston, Nicholas-circle, French: negative, his README); f.9 is the only sibling in its own key
- [x] clear-pages: the 73 clear fragments of f.10 and 16 of f.9 are in the tsv as [PLAIN:...] and anchor the keyed runs (the "your Majesty" fits)
- [x] known-keys: key129 applied, rank 1/21 shuffled keys on lm (1/201 at 200), H-only rows rank 1/21 on all three statistics
- [ ] print: print_check.py on 2-3 decoded phrases (Clarendon calendar, the row's third clause) needs network; planned with the Evelyn fetch, ~$1
- [n/a] key-rebuild: the key is a period key read from f.77 and Evelyn; the rebuild that matters is the rest of it, which does not survive (gap 1)
- [n/a] image-check: no image is on disk or reachable (DECODE content block, BL offline); the transcription is Aymeloglu's from the DECODE image
- [n/a] retry: no fetch, challenge or reset this session; disk only after the one clone
Verdict: keep going: 2 internal gaps; cheapest next: Evelyn iv 178-179 page scans as the known answer for the 45 H values and 13 letters, ~$3
