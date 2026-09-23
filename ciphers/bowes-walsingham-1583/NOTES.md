open

# Robert Bowes to Walsingham, 7 April and 31 July 1583, and short Caligula B VIII ciphertexts 1580-83 — BL Cotton Caligula C VII, B VIII

- Source: QUEUE.md rank 17 (score 32), scored 20 September 2026; catalogued from Tomokiyo's Cryptiana
  `elizabeth.htm` page and Bourdeau's `TARGETS.md`.

## Check-solved sweep (23 September 2026)

1. **Web search.** "Robert Bowes Walsingham 1583 cipher Caligula Cotton solved decrypted" — results are general
   biographical and manuscript-catalogue pages (BL Archives Catalogue entries for other Caligula volumes,
   Wikipedia on Robert Bowes, a Cryptologia abstract on deciphering Mary Stuart's letters 1578-84) and confirm
   the manuscripts and their catalogue descriptions but report no decipherment of the 7 April or 31 July 1583
   letters, or of the Caligula B VIII fragments. found=false.

2. **Print.** The 20 September 2026 search-print pass recorded in QUEUE.md already established: CSP Scotland
   vol. 6 (Boyd 1910, covering 1581-83) is not on Internet Archive under its own title (`advancedsearch.php`
   found only vols 1, 2, 4, 8, 9, 13); british-history.ac.uk serves this volume's pages as paywalled "premium
   content" (confirmed for pp.356-434 and pp.521-570) and its site search returned HTTP 403; HathiTrust's
   Bibliographic API confirms a public-domain full-view copy exists (htid `nnc2.ark:/13960/t1gh9nc18`) but
   babel.hathitrust.org is Cloudflare-blocked to curl and to the browser tool. Not re-run this sweep (same
   blockers apply; HathiTrust access remains the identified next step, not completed this sweep). Google Books:
   not available in this account's environment (no key set here). Status: **unreachable, not settled** — same
   as 20 September 2026.

3. **Community lists.** `sources/cryptiana/web/elizabeth.htm` (grepped locally, never edited) is explicit and
   directly on point: "(f.196) Robert Bowes to (?)Walsingham, Edinburgh, 7 April 1583. A few words in cipher,
   **not deciphered**." and "(f.299) Robert Bowes to (?)Walsingham, Edinburgh, St Johnstons, 31 July 1583. A few
   words in cipher, **not deciphered**," with Tomokiyo's own transcription linked (`CottonMSBowes.txt`) and the
   note "If one can read the cleartext around the ciphertext, solution may not be difficult" — i.e. Tomokiyo
   flags it as an open, tractable target, not a solved one. The same page documents the sibling key lead already
   in QUEUE.md: Caligula B VIII f.290-293 ("Bowes's report of his conferences... to supplant Lenox," catalogued
   84) has an interlinear decipherment and a reconstructed key image (`elizabeth_bowes.png`); f.251-252 and
   f.306 are further short, undeciphered Bowes-related fragments in the same volume, also not solved. Cipherbrain
   /scienceblogs.de: no matching post found via WebSearch snippets; full-page fetch blocked by this
   environment's egress policy (see ciphers/charles-rupert-1645/NOTES.md item 3). found=false, confirmed
   explicitly "not deciphered" by the primary community source (Cryptiana); unreachable on Cipherbrain directly.

4. **DECODE.** No DECODE record IDs are attached to this QUEUE row (unlike ranks 11 and 13); the item is
   catalogued from Tomokiyo's own transcription rather than a DECODE upload. Not checked.

5. **Bourdeau (`github.com/dbourdeau/cyphersolver`, shallow clone 23 Sept 2026, MIT code / CC BY 4.0 text).**
   No target folder for this item (`grep -rli "bowes\|caligula"` across the repository returns only unrelated
   incidental mentions — e.g. "napoleon/unsolved.txt", the Randolph 1570 and Norfolk 1570 folders' source
   citations, Hamilton 1569 — none of which is a Bowes 1583 attempt). `TARGETS.md` lists it (per QUEUE.md's own
   rationale, "ranked it low", "101 groups of name") but with no working folder. found=false (not attempted).

6. **Aymeloglu (`github.com/aaymeloglu/unsolved-ciphers`, shallow clone 23 Sept 2026; no licence, cite only, no
   code copied).** No target folder and no catalogue-file mention (`grep -rli "bowes\|caligula"` returns zero
   matches anywhere in the repository). found=false (not attempted).

## Verdict

**Open.** Every source checked either found nothing (web search, Bourdeau, Aymeloglu, DECODE n/a) or explicitly
confirms the two named letters are "not deciphered" (Tomokiyo's Cryptiana page, the primary community source for
this exact item). The one print route that could settle it — CSP Scotland vol. 6 (Boyd 1910) via HathiTrust
`nnc2.ark:/13960/t1gh9nc18` — remains blocked by Cloudflare to every fetch route tried in prior sweeps and was
not re-attempted this sweep (no new access route available in this account's environment). The Caligula B VIII
f.290-293 interlinear decipherment (Tomokiyo, `elizabeth_bowes.png`) stands as the identified sibling-key lead
and is unchanged by this sweep.

Stage 2, verified unsolved.

## Search-print and image check (23 September 2026)

Network was opened for this account's environment at 23:00 UTC today (per ROOM.md 23:05 note); this pass used
route 1 of the access playbook (`curl -A "Mozilla/5.0"`) against archive.org and the BL's catalogue/IIIF hosts.
Per the owner's standing rate-limit rule: requests were single, sequential, at least 1.5s apart, never
parallel against the same host, and stopped (not retried in a loop) on the two 403s hit. Counts this session:
archive.org 8 requests (2 advancedsearch, 1 metadata, 5 download/djvu-text, all HTTP 200 after following one
redirect); searcharchives.bl.uk 4 requests (2 search pages, 2 catalogue records, all 200); bl.digirati.io 2
requests (one IIIF manifest per shelfmark, both 403); babel.hathitrust.org 1 request (403, not retried,
per the rule); cryptiana.web.fc2.com 2 requests (Tomokiyo's own linked transcription + key image, both 200).

### 1. Search-print

**CSP Scotland vol. 6 (Boyd 1910, 1581-83) is still not on archive.org.** Two targeted `advancedsearch.php`
queries (`title:(calendar state papers scotland)`; `creator:(Boyd) AND title:(calendar) AND mediatype:texts`)
return only `calendarstatepa00boydgoog` (vol. IV, 1905) and `calendarstatepa01boydgoog` (confirmed by its full
djvu text as vol. V, 1574-1581, Boyd 1907) — no identifier for vol. 6. Unchanged from the 20 September 2026
finding (also blocked on BHO and HathiTrust; babel.hathitrust.org repeated its Cloudflare 403 this pass too,
one attempt only, not retried).

**Found instead: *The Correspondence of Robert Bowes* (Surtees Society vol. 14, ed. Stevenson, 1842)**, on
archive.org as `correspondenceof00bowerich` (full djvu text fetched, 1.8 MB). Tomokiyo's own page already notes
this volume "does not include" the f.196/f.299 cipher letters (sources/cryptiana/web/elizabeth.htm line 428),
and this pass confirms why: it prints Bowes's own **Letter-Book copies**, a separate register kept alongside
the originals that Walsingham filed (now Cotton MS Caligula), not the originals themselves. A whole-volume
keyword sweep found "cipher" x2, "cypher" x12; none is flagged "deciphered", and no key or plaintext substitution
for a cipher passage is printed anywhere in the volume. Full detail (entry numbers, page citations, flagged
sentences) is in `print-check.tsv`. Three entries are directly relevant:

- **CLXXXVII, "To Sir Francis Walsingham, vijth April, 1583"** (Letter-Book p.172, printed pp.404-406): the
  same sender, recipient, place (Edinburgh) and date as the BL catalogue's f.196 entry (below). Contains
  unresolved **numeric name-codes** left as bare arabic numerals by Stevenson — 870, 91, 149, 19, 29, 85, 54,
  32 — e.g. "the doings and progress of Sir Henry Cobham with 870 and Smallet" and "he cannot abandon 149, 19,
  29, and 85." Not a decipherment (no name is ever substituted for a number); Tomokiyo's page independently
  flags these same codes as an "unidentified" lead separate from the Cotton MS symbol-cipher.
- **CCXXXIX, "To Sir Francis Walsingham, ultimo Julii, 1583"** (p.253, printed pp.525-529): the public/official
  companion letter of 31 July 1583; no cipher content.
- **CCXL, "The Private Letter of the same date"** (p.257, printed pp.529-534): numeric codes 223, 189, 32,
  0100, 54 — e.g. "upon suit made to 189 for the relief of Drumquhassell, 189 said that he must be examined
  what had passed betwixt 32 and him for the delivery of 0100 to 32." Tomokiyo's page separately notes "223" on
  Surtees p.530 as an unidentified code.

**Verdict on print: not found-solved, not an edition of the target letters.** The Letter-Book entries are a
related but textually distinct source (Bowes's own register, not the delivered/filed original), printed in a
public-domain 1842 edition, containing their own un-glossed numeric name-codes rather than the drawn cipher
symbols Tomokiyo transcribed from the Cotton MS. Whether entry CLXXXVII is word-for-word the same letter as
Cotton C VII f.196 (both dated 7 April 1583, same correspondents) is not established this pass — worth a
side-by-side check by whoever next has the manuscript images or Boyd's own calendar text.

### 2. Images (BL IIIF, route 1)

Fetched the British Library's own Archives and Manuscripts Catalogue records (`searcharchives.bl.uk`) for both
shelfmarks — not previously checked by this target's NOTES. Both **confirm and extend Tomokiyo's citations
verbatim**:

- **Cotton MS Caligula C VII** (`searcharchives.bl.uk/catalog/040-001102384`, covers 1582-1584, Languages
  includes "Cipher"): "**ff. 196r-197v**: Letter of Robert Bowes to (?) Sir Francis Walsingham, Edinburgh, 7
  Apr 1583. Original. Partly in cipher." and "**ff. 299r-v, 303r**: Letter of Robert Bowes to (?) Sir Francis
  Walsingham, Edinburgh, St Johnstons, 31 Jul 1583. Original. No address; Bowes addresses recipient as Your
  Honour. Some use of cipher." Two *other* Bowes-to-Walsingham items dated the same 31 July 1583 in the same
  volume (f.297r-v, a 17th-century copy; f.300r-302r, an original) are catalogued with no cipher note, so
  f.299/303 is specifically the cipher-bearing item among three same-day letters.
- **Cotton MS Caligula B VIII** (`searcharchives.bl.uk/catalog/040-001102375`): confirms Tomokiyo's three
  sibling fragments — **f.251r-252v** ("Copy of a letter from [Bowes?] to [Cecil?], reporting the state of
  affairs in Scotland [1583?]"), **f.290v-292v** ("Bowes's report of his conferences and negociations to
  supplant Lennox, partly in cypher [1580?]" — the interlinear/reconstructed-key lead, `elizabeth_bowes.png`),
  and **f.306r** ("A note, with some cipher, on Scottish affairs," undated).

**Neither volume is digitised.** Both catalogue pages give a Digitised Content link marked "(digital images
currently unavailable)"; the corresponding IIIF manifest at `bl.digirati.io` returns HTTP 403 (an S3
`AccessDenied` body, not a Cloudflare challenge page) for both arks. This is a different, harder failure mode
than the Cloudflare-gated hosts logged elsewhere in CLAUDE.md: the BL itself states the images do not exist
online yet, not merely that they are hard to reach. No image was captured; `images/manifest.json` records
what was tried. Not retried per the rate-limit rule (one manifest fetch per shelfmark, then stop on 403).

Also fetched (and added to `sources/cryptiana/web/`, since they are resources Tomokiyo's already-snapshotted
`elizabeth.htm` links to and were not yet mirrored): his own ciphertext transcription `CottonMSBowes.txt`
("the lines below are separate ciphertext fragments (not a contiguous ciphertext)", 11 short lines of 2-digit
symbol codes covering f.196 and f.299 combined) and `elizabeth_bowes.png` (his reconstructed key for the
f.290-293 fragment).

### Verdict

**Still open; status line unchanged.** No decipherment, key or plaintext for any of the five fragments (f.196,
f.299, f.251-252, f.290-293, f.306) is in print anywhere checked this pass. Per rule 10: reporting only what
was found and where it was not found, not novelty. Next steps, in order: (a) the manuscript images do not
exist yet at the BL, so transcription must wait on a physical/reading-room route (access playbook route 4,
not attempted this pass — no per-item price is quoted on the catalogue page to put in a REQUEST.md yet;
worth an email enquiry via route 4 if this target is prioritised further); (b) if CSP Scotland vol. 6 (Boyd's
own calendar text, which would settle whether f.196/f.299 print as deciphered or as symbols) becomes reachable
via HathiTrust or another route, re-run the search-print pass against it specifically; (c) cryptanalysis of
Tomokiyo's own 11-fragment symbol transcription (`sources/cryptiana/web/CottonMSBowes.txt`) remains the only
route that does not depend on new images, per his own note that the cipher "seems to be a simple one" and that
reading the surrounding cleartext (which does exist, via the BL catalogue folio numbers above, on a future
image-capture pass) "may be" enough to solve it.
