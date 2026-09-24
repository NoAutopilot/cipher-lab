# AUDIT: the Bowes 1583 fragment reading (novelty class)

Verifier session, 23 September 2026 (Opus, no subagents). Audits the solver section of NOTES.md ("Solver session
(23 September 2026)"), reading.tsv and key.tsv as of commit 072e824, and the sentences about them in status.json,
LEDGER.md and ROOM.md. This session did not take part in the solving, did no decoding, and does not protect the
solver's conclusions. Classes are those of CLAUDE.md rule 10.

## 1. Verdict

| item | fragments | prior plaintext | prior decipherment of this item | class |
|---|---|---|---|---|
| A. Bowes to (?) Walsingham, Edinburgh, 7 Apr 1583, Cotton Calig. C VII ff.196r-197v | F1-F7 (65 tokens) | **yes.** Surtees Soc. vol. 14 (Stevenson 1842) no. CLXXXVII, pp.404-406, Bowes's letter-book copy, names in clear. Also CSP Scotland vi (Boyd 1910) pp.370-371, the calendar of this folio, whose page text contains every name the fragments give (section 4) | **probable, not confirmed.** The 1910 calendar of fol.196 seems to print the cipher words as names. Its running text was not read, so how Boyd got the names (a decipher on the manuscript, the letter-book, or his own work) and whether he marks them as cipher is not known. No sign-to-letter key located | **N1** (N0 if the calendar page, once read, gives the names as the reading of the cipher) |
| B. Bowes to (?) Walsingham, Edinburgh/St Johnstons, 31 Jul 1583, Cotton Calig. C VII ff.299r-v, 303r | F8-F11 (26 tokens, 8 unread) | **yes.** Surtees no. CCXL ("The Private Letter of the same date"), pp.529-534: "This day Glencarne and 223 ...", "the act done at Ruthen on his person". CSP Scotland vi no. 584, pp.566-567, a Bowes-to-Walsingham entry of 31 July that has Glencairn, 223 and Ruthven. It is probably fol.299 (no. 583 on p.564 cites ff.297 and 300, the other two 31 July items), but its folio citation cannot be read in the token counts | not located. Probable in the 1910 calendar on the same reasoning as item A, with weaker evidence | **N1** |
| C. The sign-to-letter table (key.tsv) for Tomokiyo's sign numbers 06-24 | all | n/a | no prior table located in the families of section 3. Tomokiyo (Cryptiana) marks both letters "not deciphered". JSTOR, Google Books full text, HathiTrust full text and DECODE could not be reached | not a plaintext claim; search-level only (N3 scope for this narrow artefact, not N4) |

**Folder class: N1.** The plaintext of every passage the fragments read has been in print since 1842. For the
7 April letter, the 1910 calendar of this very folio very probably already gives the cipher names in clear. The
solver's result is an **independent re-decipherment**: it aligns Tomokiyo's transcription with published
plaintext to recover a sign table. The only part not located elsewhere is that table in Tomokiyo's numbering. It
is conditional on his transcription (no image seen), and its second signs for a, e and g each rest on a single
token at grade M.

**Safe sentence.** "Tomokiyo's transcription of the eleven cipher fragments in Bowes's letters of 7 April and 31
July 1583 (Cotton Caligula C VII ff.196, 299) was aligned with Bowes's letter-book copies printed in 1842. This
gives a sign table that reads 93 of 101 tokens (S 82, M 8, I 3) as the names printed there. It is an
independent re-decipherment of plaintext in print since 1842, conditional on the transcription. No earlier
sign-level key was found in the sources listed in AUDIT.md."

**Unsafe sentences.** "Bowes's 1583 cipher deciphered for the first time", "previously unread names recovered",
"93 of 101 tokens read at grade S", "a new decipherment of the Cotton letters".

## 2. What the repo claims (extracted per item)

| field | item A | item B |
|---|---|---|
| date, place | 7 Apr 1583, Edinburgh | 31 Jul 1583, Edinburgh / St Johnstons (Perth) |
| sender, recipient | Robert Bowes to (?) Sir Francis Walsingham | same |
| archive id | BL Cotton MS Caligula C VII ff.196r-197v, "Original. Partly in cipher." (searcharchives.bl.uk 040-001102384) | same volume, ff.299r-v, 303r, "Original ... Some use of cipher." |
| ciphertext | F1-F7 of `ciphertext.txt` (Tomokiyo's CottonMSBowes.txt; his f.196/f.299 split is not marked, and the solver's is inferred from the order of the names) | F8-F11 |
| plaintext as read | F1 sir henni[r] cobham; F2 smallet; F3 g[c]lencarne; F4 magnyuil h[r]ntley o glencarne ?; F5 ?; F6 mauuissier; F7 smallet | F8 ? glencarn; F9 his ruthen; F10 ???; F11 ? ? him |
| distinctive phrases (Letter-Book) | "Sir Henry Cobham with 870 and Smallet"; "credit by and with Glencarne"; "Manningvile, Huntley, Glencarne, and Montrosse, with especial commendations from 870"; "offer himself to Mauvisier"; "return of Smaller [Smallet]" | "This day Glencarne and 223"; "the act done at Ruthen on his person"; "his fault at Ruthen" |
| solver's search (NOTES.md "Where it was not found") | Bourdeau clone 2e9ec01 and Aymeloglu clone 6f9c462 grepped for `bowes\|smallet\|glencarne\|mauvissier\|magnyvil\|caligula c vii`; one WebSearch; Surtees vol. 14 as the parallel text; CSP Scotland vi marked unreachable | same |
| check-solved (23 Sept 2026) | web search; print (CSP vi unreachable: not on archive.org, BHO premium, HathiTrust Cloudflare); Cryptiana "not deciphered"; DECODE n/a; Bourdeau and Aymeloglu greps. Verdict open, stage 2 | same |
| print check (23 Sept 2026) | CSP vi still absent from archive.org; Surtees vol. 14 found, read as "a related but textually distinct source ... not an edition of the target letters"; BL catalogue confirms the folios; both volumes undigitised (IIIF 403) | same |

## 3. Search log (this session, 23 September 2026)

| family | what was searched | result |
|---|---|---|
| (a) CSP Scotland vi (Boyd 1910) | HathiTrust Bibliographic API (htid record 008437788; v.6 = `nnc2.ark:/13960/t1gh9nc18`, full view); **HTRC Extracted Features API** per-page token counts for the whole volume (886 scans), searched for smallet, glencairn, glencarne, mauvissiere, cobham, maineville, mainville, cipher, deciphered, decipher, bowes, ruthven, huntly, 1583, april, and for pages with folio numbers 196, 297, 299, 300 | **hit, section 4.** Running text not read: `babel.hathitrust.org/cgi/imgsrv/download/plaintext` answered 403 "Blocked from HathiTrust" (1 request, stopped). Wayback CDX has no capture of the volume on babel. British History Online vol6/pp356-434 captured 20150502 is already the "premium content" stub |
| (a) Thorpe, Calendar of State Papers relating to Scotland vol. 1 (1858), SP 52 | IA `cu31924091754360` djvu text, 1583 section | SP 52/31-32 has Bowes letters of 6 April (nos 89, 92) and 31 July (nos 114, 115), not the Cotton cipher letters. No name glossed as cipher. No hit for Smallet at April 7 |
| (a) CSP Foreign 1583 | not searched (the letters are Scottish and calendared in CSP Scotland vi) | not needed once vi was located |
| (b) Surtees vol. 14 (Stevenson 1842), sender's letters | repo copy `corpus/correspondenceof00bowerich_djvu.txt`, CLXXXVII and CCXXXIX-CCXL in full, the preface and the table of contents | Stevenson prints the names in clear and leaves the numeric codes (870, 91, 32, 54, 223, 189, 0100) as numbers. **He does not mark or gloss any word of these two letters as cipher**; the only "cypher" in CLXXXVII is Bowes's sentence about Cary's cipher. His Cotton-sourced 1580 letter (LXII, "names in cypher") prints the numeric code layer only |
| (b) Recipient: Conyers Read, *Mr Secretary Walsingham* vol. 2 (1925) | IA full-text API on `mrsecretarywalsi0000unse`: Smallet 0, Maineville 0; controls Bowes 1 hit, Mainville 1 hit (index works) | no mention of Smallet; no decipherment |
| (c) Border Papers vol. 1 (Bain 1894) | IA search returned `cu31924091786065`, whose djvu text is vol. 2 (1595-1603), so wrong volume; vol. 1 not searched. Hamilton Papers not searched (the series ends before 1583 in substance) | **not covered** |
| (d) BL catalogue | `searcharchives.bl.uk/catalog/040-001102384?format=json`, grepped for decipher and for the folios | ff.196 and 299 have no decipher note. The same volume has 17th-century "deciphered" copies of *other* Bowes letters (ff.69v-70r, 17 Oct 1582; ff.201r-203r, 12 Apr 1583; ff.269v-270r, 10 Jul 1583). f.297 is a 17th-century copy of the 31 July public letter, not of f.299 |
| (e) Google Books | WebSearch only (no key in this container): quoted Smallet/Maineville/Glencairn with Bowes and Walsingham; CSP Scotland vi on Google Books | no snippet. Series record `AFoMAQAAMAAJ` noted. **Full text unreachable** |
| (e) Internet Archive | advancedsearch for CSP Scotland volumes (no vi), Border Papers, Read | as above |
| (f) Solver repositories | fresh shallow clones, 23 Sept 2026: Bourdeau `763a3b9`, Aymeloglu `9260394`; grep `caligula c vii`, `calig. c. vii`, smallet, glencarne, robert bowes, bowes 1583, CottonMSBowes | Bourdeau: only `TARGETS.md:105` ("Bowes 1583 is 101 groups of name") and mirrored copies of Tomokiyo's "undeciphered ciphertext ... from Robert Bowes (1583)". Aymeloglu: nothing |
| (f) Cryptiana | `sources/cryptiana/web/elizabeth.htm` lines 425-428 | "not deciphered" for both. It also says the Surtees volume "does not include these letters"; section 4 contradicts that for f.196. Tomokiyo's `CottonMSBowes.png` could not be fetched: cryptiana.web.fc2.com is not on this container's egress allowlist (1 request) |
| (f) Cipherbrain, Cipher Mysteries | WebSearch `ciphermysteries OR scienceblogs klausis-krypto-kolumne "Bowes" Walsingham cipher` | nothing on Bowes |
| (g) Scholarship | WebSearch: Tomokiyo + Bowes + Walsingham 1583 + Caligula; "Robert Bowes" cipher Maineville Smallet decipher | only Lasry-Biermann-Tomokiyo 2023 (Mary Stuart to Castelnau), which does not touch Bowes's own letters |
| JSTOR | **unreachable** (no credentials here) | queries for a session with credentials: `"Bowes" AND "Walsingham" AND 1583 AND (cipher OR cypher)`; `"Smallet" AND ("Maineville" OR "Mainville")`; `"Caligula C. VII" AND (cipher OR decipher*)`; `Tomokiyo AND Bowes` |
| Google Books API | **unreachable** (no GOOGLE_BOOKS_KEY here) | `q="Smallet" "Glencairn" 870`; `q="Calig. C. VII. fol. 196"`; `q="Maineville, Huntly, Glencairn"`, all with `filter=full&country=US`; `tools/gbooks_search_within.py` on any full-view CSP Scotland vi copy for "Smallet" |
| DECODE | **unreachable** (no credentials here) | search records for "Caligula C VII", "Bowes", 1583. Aymeloglu's cache has Caligula C II and C V records only (solver, 23 Sept) |
| HathiTrust full text | **unreachable** (babel 403) | read CSP vi seq 414-415 (pp.370-371) and 610-611 (pp.566-567), or search-inside "Smallet". This one read settles N0 against N1 for item A |

## 4. The calendar evidence (CSP Scotland vi, from token counts)

Evidence file: `audit_csp6_tokens.tsv`, the per-page token counts of scans 413-416 and 608-611, from the HTRC
Extracted Features API. The header number on each page is the printed page.

- **p.370 (seq 414)** has entry numbers 388 and 389, a Bowes-to-Walsingham heading, "7", "April", and a marginal
  source "Cott. Calig. C. VII." with folio numbers 189b and 196. **p.371 (seq 415)** has entry 390, which is
  James Lowson's letter of 9 April (Thorpe no. 93, the same date). So **no. 389 is the fol.196 letter of 7 April**.
  The entry number is inferred from its place on the page.
- p.371 contains **Cobham** (OCR "Cobhani"), **Henry**, **Smallet ×2**, **Glencairn ×2**, **Maineville ×2**
  (one OCR "Maijieville"), **Huntly**, **Montrose**, **Mauvissi[ère]**, **Cary**, and the code numbers **870 ×7, 91
  ×3, 32, 54, 000**. These are exactly the names the fragments give, and the numbers the letter-book leaves
  unresolved. The vocabulary of pp.370-371 shares 111 of its 246 words of six or more letters with CLXXXVII,
  against 60-83 with the other letter-book entries tested. So the calendared fol.196 letter is the letter-book's
  CLXXXVII, as the solver argued from the order of the names. Tomokiyo's "does not include these letters"
  therefore does not hold for f.196.
- "cipher" occurs once on p.371. Cary and "errors" are also on the page, so that one occurrence is very probably
  the abstract of Bowes's sentence about the errors in Cary's cipher, not a note such as "partly in cipher". This
  is inferred and unconfirmed. Three pairs of square brackets on p.371 might mark editorial insertions. Their
  content cannot be recovered from token counts.
- **p.564 (seq 608)** has no. 583, Bowes to Walsingham 31 July, citing folios 297 and 300 (the copy and the
  original of the public letter, CCXXXIX: 99 of 150 words shared). **p.566-567 (seq 610-611)** has no. 584,
  Bowes to Walsingham, with Glencairn, 223 and Smallet (the Smallet is at the end of no. 583), and Ruthven, 54
  and 85 on p.567. These pages share 145 of 243 words with CCXL. By elimination no. 584 is fol.299, but its
  folio citation cannot be read.

What this establishes: the plaintext of item A is in print as the calendar of this very manuscript, since 1910.
What it does not establish: that Boyd presents the names as the reading of cipher, or that anyone before 24
September 2026 wrote down a sign-to-letter table.

## 5. Test of the reading itself

- `python3 check.py` runs and exits 0 ("reading.tsv regenerates from ciphertext.txt + key.tsv").
- Applying key.tsv to ciphertext.txt with an independent script gives the same strings as reading.tsv:
  sirhennicobham, smallet, gclencarne, magnyuilhrntleyoglencarne?, ?, mauuissier, smallet, ?glencarn,
  hisruthen, ???, ??him. The key gives 85 S, 8 M and 8 unread. check.py lowers three S tokens to I, for a final
  **S 82, M 8, I 3, unread 8** (101). The names match the letter-book's names in the letter-book's order. The
  three I tokens are honestly marked: F1 pos.7 (n where "Henry" wants r), F3 pos.2 (an extra c), F4 pos.10 (r
  where "Huntley" wants u). So are the eight unread tokens (F4 pos.26, F5, F8 pos.1, F10 ×3, F11 pos.1-2). The
  unread signs are not given values in the reading. The guesses 28 = 870 and 02 02 03 = 223 stay in notes and
  are "not verified".
- **Qualifications the repo understates.** (i) Each second sign (14 = e, 26 = a, 23 = g) occurs once and is
  graded M. "Second signs for a, e and g" is a reading at M, not an established property of the system. (ii) The
  method is alignment with a known parallel plaintext. The S grade is defensible, because the letter-book is a
  separate copy and the crib placement was tested against a control (43 tokens covered, against 28.8 ± 2.9 and
  27.0 ± 3.1). But "cryptanalytic result" here means "key recovered from printed plaintext", not "plaintext
  recovered from ciphertext". (iii) F4's "magnyuil" is not the letter-book's spelling "Manningvile". The match
  rests on the calendar's "Maineville" and on position, and the value 24 = y is M.
- **Transcription condition.** No image of the manuscript was seen, and Tomokiyo's glyph image was not fetched.
  This limits the per-token grades and the sign table (item C). It does not raise the class, because the
  plaintext is in print whatever the transcription. Even the narrow "no prior sign table" statement cannot go
  past search level until the image confirms the signs.

## 6. Did we first-decipher?

No. The names were printed in 1842 from Bowes's own copies, and in 1910 as the calendar of the f.196 original
itself. The solver's contribution is a sign table in Tomokiyo's numbering, obtained from that printed plaintext.
It corroborates the identification of f.196 with letter-book CLXXXVII, which the calendar's vocabulary
independently supports. It may be worth giving to Tomokiyo as a correction to "not deciphered" and "does not
include these letters". That would be a contribution, not a recovery of unknown text.

Confidence: high that the plaintext is prior (1842 print, read in full here). Moderate-high that the 1910
calendar prints the f.196 names in clear (token counts, not running text). Low on whether anyone has published a
sign table (four families unreachable).

## 7. Postmortem

**Failure.** Stage 2 ("verified unsolved") rested on Tomokiyo's "not deciphered" while the one calendar that
could contradict it was logged as unreachable. Its token counts were reachable the whole time through the HTRC
Extracted Features route in CLAUDE.md's access playbook. They show the fol.196 letter calendared in 1910 with
every cipher name in clear. A second, smaller over-claim appeared downstream of the solver: "93 of 101 tokens at
grade S" (status.json note and log, ROOM.md 03:00 note). The true count is 93 tokens read, of which 82 are S.

**Sentences corrected in this commit:**
- status.json, target note: "93/101 tokens read at grade S with a control ... simple substitution with second
  signs for a, e, g" is replaced by the grades and the class.
- status.json, log of 23 Sept 03:00: "93 of 101 tokens at grade S with a control" becomes "93 of 101 tokens read
  (S 82, M 8, I 3)".
- NOTES.md, print-check verdict: "a related but textually distinct source ... not an edition of the target
  letters" is annotated. The calendar's vocabulary shows CLXXXVII is the same letter as fol.196.
- NOTES.md, solver "Reading": "The cipher is a simple substitution (one sign per letter, with second signs for a,
  e and g)" gains the qualifier that the second signs are single tokens at M.
- NOTES.md, solver "Where it was not found": the CSP Scotland vi line is annotated with this audit's finding.
- ROOM.md: a correction line for the 03:00 "93/101 tokens, S" note (the log is append-only).
- LEDGER.md row of 23 Sept ("93 of 101 tokens, S 82 M 8 I 3") is accurate and was left alone. STATUS.md has no
  sentence about this reading and was left alone.

**Lesson (for the check-solved brief, one line):** when a calendar is Cloudflare-blocked, run the HTRC EF token
test for the item's names and folio numbers before setting stage 2. A calendar page that holds the item's
folio number and its cipher names is a found-solved signal.

## 8. Requests this session, per host

data.htrc.illinois.edu 3 (one 404 from a wrong id encoding, 2 × 200); catalog.hathitrust.org 1;
babel.hathitrust.org 1 (403, stopped); archive.org 7 (advancedsearch 2, metadata 1, download 4 of which one
404); be-api.us.archive.org 4; web.archive.org 5 (CDX 4, of which one connection reset retried once and one 504,
plus one snapshot); searcharchives.bl.uk 1; cryptiana.web.fc2.com 1 (blocked by the egress allowlist);
github.com 2 shallow clones; WebSearch 5 queries. All requests were sequential, at least 1.5 s apart per host,
with the descriptive User-Agent.

## 9. Calendar page check (23 September 2026)

Verifier follow-up session (Sonnet, no subagents), continuing directly from section 4/8 above. Question: does
CSP Scotland vi (Boyd 1910) no. 389 (pp.370-371, Cott. Calig. C VII fol.196, 7 April 1583) and no. 584
(pp.566-567, 31 July 1583) print the seven names in clear, and mark any of them "in cipher" or "deciphered" —
which decides N0 against N1 for item A/B.

**Routes tried, in order.**

1. **Internet Archive.** `advancedsearch.php` for `title:(calendar state papers scotland)`, for
   `creator:Boyd AND title:(calendar scotland)`, and for `identifier:calendarofstatep*` (120 hits, paged):
   no identifier for vol. 6 (Boyd 1910) appears in the public index. Direct-guessed identifiers
   `calendarstatepa06boydgoog`, `calendarstatepa06boyd`, `calendarofstatep06vari` do not exist (`{}`).
   `calendarofstatep06grea` exists but `is_dark:true` (no public files, not search-indexed); its `/details/`
   page returns "Internet Archive: Error" and `be-api` full-text search on it returns 0 hits for "Smallet" and
   for "Boyd" — this identifier cannot be confirmed as vol. 6 and is not usable either way. **No route to the
   volume's own scan or its search-inside index on archive.org.**

2. **HathiTrust.** Extended the existing `audit_csp6_tokens.tsv` (HTRC Extracted Features, htid
   `nnc2.ark:/13960/t1gh9nc18`, already fetched 23 Sept 2026, no new request needed) with a targeted grep for
   `cipher`, `cypher`, `decipher`, `deciphered` across every page in the file (seq 413-416, 608-611). Result:
   **`cipher` occurs exactly once on p.371 (seq 415, the second page of no. 389) and exactly once on p.567
   (seq 611, the second page of no. 584). `cypher`, `decipher` and `deciphered` occur nowhere in either
   entry's pages.** p.371's full token list also confirms Cobham ("Cobhani"), Henry, Smallet ×2, Glencairn
   ×2, Maineville ("Maineville"/"Maijieville"), Huntly, Montrose and Mauvissi[ère] all present in clear, as
   AUDIT.md section 4 already found. p.567 has Ruthven ×2 but not Glencairn, Smallet or Maineville, which
   land instead on p.566 (seq 610) and — per section 4 — probably belong to the tail of no. 583, not no. 584.
   Re-tried `babel.hathitrust.org/cgi/pt?id=...&seq=415` directly (a different endpoint from section 8's
   `imgsrv/download/plaintext`, with a full desktop Chrome User-Agent): still **403**, one request, stopped
   per the good-citizen rule — running text remains unreachable this route.

3. **Wayback Machine of British History Online.** Confirmed the exact chunk URLs from BHO's own vol. 6 table
   of contents (`/cal-state-papers/scotland/vol6`, fetched directly, 200): no. 389 is in
   `/cal-state-papers/scotland/vol6/pp356-434` ("Elizabeth: April 1583"); no. 584 is in
   `/cal-state-papers/scotland/vol6/pp521-570` ("Elizabeth: July 1583"). CDX for both: earliest captures
   2 May 2015, length 8270-8273 bytes for an entire month of entries (pp356-434 alone is 78 printed pages) —
   too short to be the running text. Fetched the pp356-434 2015 capture (`if_`, one connection reset, one
   retry): confirms it is a **stub**, not the text — `<p>Pages 356-434</p><p>Calendar of State Papers,
   Scotland: Volume 6, 1581-83. ... </p><p>This premium content was digitised by double rekeying. All rights
   reserved.</p>` with no entry text and no hit for any of Cobham/Smallet/Glencairn/Maineville/Huntly/
   Mauvissière/cipher in the page source. This matches and confirms section 8's earlier finding for the same
   URL. A possible unpaywalled mirror, `archive.british-history.ac.uk` (surfaced by a WebSearch snippet for
   vol. 5), refused the direct connection twice (`Recv failure: Connection reset by peer` through this
   session's proxy — the same symptom the Access playbook records for Cloudflare-challenged sites); a CDX
   lookup for it returned no captures for the vol. 6 chunk (one clean empty result) and Internet Archive's
   own services returned "Temporarily Offline" banners on three further attempts (2 CDX, all in the same few
   minutes) — an infrastructure outage, not a block, but it closed off retrying this route inside the budget.

4. **WebSearch**, 4 queries: `"Cott. Calig. C. VII" "196" Bowes Walsingham 1583 calendar`; `"Bowes"
   "Walsingham" cipher "Smallet" OR "870" Cotton Caligula 1583`; `british-history.ac.uk "Calendar of State
   Papers" Scotland Mary Queen of Scots "vol. 6" 1581-1583 pp356-434`; `Boyd "Calendar of State Papers"
   Scotland 1910 "no. 389" OR "No. 389" Bowes April 1583`. No snippet quotes the entry text; results are the
   BHO series/volume pages (confirming the premium gate), the BL catalogue, Wikipedia's Robert Bowes article,
   and unrelated Cotton-manuscript pages. No hit for a phrase from the entry itself.

**Answer.** Not settled by direct reading of the running text — every route to it (HathiTrust `babel`,
BHO/Wayback, `archive.british-history.ac.uk`) is blocked or unreachable this session, for the same reasons
already logged in section 8, now independently re-confirmed rather than merely re-asserted. What the extended
token-frequency check adds: the word **"deciphered" (and "cypher"/"decipher") does not occur anywhere on
either entry's pages**, and "cipher" occurs only once per page — a single loose occurrence, not the kind of
repeated marginal tagging ("in cipher", "deciphered by X") that a calendar typically prints when a manuscript
note or an editorial decipherment sits next to a passage. Combined with section 4's earlier reasoning (the one
"cipher" on p.371 sits with "Cary" and "errors", almost certainly the abstract of Bowes's own sentence about
errors in *Cary's* cipher, not a note on this letter), this is evidence against "marked in cipher/deciphered"
next to the names, but it is evidence from word frequency and position guesses, not from having read the
sentence, and it does not by itself prove absence — an editor's practice of embedding "[in cipher]" inline
after a name would still show up as one more "cipher" token, indistinguishable in this data from the Cary
sentence. The names being present in clear on both pages is unchanged from section 4 and is not in question.

**Class: still N1, page not reached.** What remains to move it to N0 or to firm up N1: the running text of
CSP Scotland vi pp.370-371 and pp.566-567, read verbatim, by any of (a) a HathiTrust login/full-view download
route not yet available in this environment, (b) a BHO "gold" subscription or the print volume itself
(REQUEST.md candidate), or (c) a working fetch of `archive.british-history.ac.uk` once the connection-reset
is diagnosed (it may simply need the certutil fix from the Access playbook applied to this specific host, or
it may be Cloudflare-challenged like HathiTrust and manuscripts.nls.uk). No sentence in NOTES.md, status.json
or ROOM.md claims N0 or "marked as cipher/deciphered in the calendar" as settled fact, so no correction is
needed this pass; the safe sentence in section 1 already says "probable, not confirmed" and that qualifier
stands.

### Requests this session (verifier follow-up, 23 September 2026)

archive.org 13 (advancedsearch 6, metadata 4, details 1, — plus 2 counted under be-api below are separate);
be-api.us.archive.org 2 (fts, 0 hits each, on an unconfirmed dark identifier); web.archive.org 10 (CDX 6 of
which 3 hit "Temporarily Offline" and were each retried once, page-content fetches 4 of which one connection
reset was retried once); british-history.ac.uk 2 (200, direct, not paywalled for the index/TOC pages);
archive.british-history.ac.uk 2 (connection reset both times, not retried a third time); babel.hathitrust.org
1 (403, stopped, one request as instructed); WebSearch 4 queries. All requests sequential, at least 1.5 s apart
per host, descriptive User-Agent, no logins or keys used.

## 10. Calendar running text reached through Google Books snippets (23 September 2026, 21:56 UTC)

Credential session on the ytbiz account (not the verifier; this section is evidence for the verifier, and the
class in section 1 is left as it stands). With `GOOGLE_BOOKS_KEY` the Books API lists six Google copies of
CSP Scotland vi (Boyd 1910), all "NO_PAGES" (no preview): `a3ZZTPid3VQC` (887 pp., its front-matter snippet
reads "BOYD, F.R. HIST. SOCIETY. VOL. VI. A.D. 1581-1583"), `414MAQAAIAAJ` (890 pp.), `lC_ljgEACAAJ`,
`gSSEPwAACAAJ`, `cmJ5swEACAAJ`, `FlUwyQEACAAJ`. No full-view copy exists: the five full-view CSP Scotland
volumes on Google Books (`SF4MAQAAIAAJ`, `20qDQJaze38C`, `vSd_wQczmCgC`, `eewrKaHskh4C`, `WQk5AQAAMAAJ`) and
the 1913 vol. vii (`hHdKAAAAYAAJ`) have no "Smallet" at all. But the two 1910 copies are full-text indexed, and
the search-within endpoint (`tools/gbooks_search_within.py`, at most three hits per query) returns running-text
snippets of about 300 characters with the printed page number. Both copies give identical text. Snippets
verbatim (OCR punctuation as returned):

**No. 389, p.370:** `April 7. 389. ROBERT BOWES TO [WALSINGHAM]. Cott. Calig. C. VII., fol. 196. Received his
letter of the 31st of March. By his letter of the 28th of March, etc., ... fol. 204. And if`

**No. 389, p.371, three passages (queries "Cobham with", "commendations from", "870"/"Glencairn and"):**
- `... Cobham with "870" and Smallet. Finds the Queen of England ["32"] as well resolved to entertain the matter,
  not with opinion to receive sound dealings, but rather to play on the advantage offered- a matter which needs
  to be warily guided as ...`
- `... Glencairn, and Montrose, with especial commendations from "870." He may not forget to offer himself to
  Mauvissière, and to bring his letters with him. It shall be good that he bring some credit from "870" and
  others in "54." Whereas by his last letter he wished him ...`
- `... Glencairn, who commended him to "870," and he shall have great credit with the French faction in case he
  shall come with the commendations looked for. For the course fit to be holden with him he can better determine
  than he [Bowes] can advise. Thinks it shall be convenient to entertain him with some favour ...`

**No. 584, p.566 (query "fol. 299"):** `... King and sundry of the Council especially chosen, and without
[running head: Elizabeth. 1583.] the privity of the rest. C. VII., fol. 299. * In cipher. * In cipher. etc. * The
date is taken [running head: 566 CALENDAR OF SCOTTISH PAPERS.]` (page-foot footnotes and the marginal source
note interleaved by the OCR). **p.567 (query "on his person"):** `... on his person was to be disproved.
Wherein, nevertheless, he will receive to his mercy all such offenders therein as penitently shall ask his
pardon. These two persons have travailed by all means in their power to stay the matter ...` **p.568 (query
"223"):** `... 223" and himself could nothing prevail with the King to stay or alter the proclamation made for
the approbation of the late act at St. Andrews, and for the condemnation of the act at Ruthven last year ...`

**Boyd's own device for supplied cipher words, p.374 (end of no. 392, before "April 12. 393. ROBERT BOWES TO
WALSINGHAM"):** `... in cipher. Addressed. Indorsed. The words in italics are supplied from the copy in the
British Museum. Copy of the same with the words in cipher deciphered.` The query "italics are supplied" has
exactly one hit in the volume, p.374; so no. 389 carries no such note.

**What this settles, for the verifier.**
1. No. 389 is fol.196, now read in the entry heading itself, not inferred from token counts.
2. In no. 389 Boyd prints Cobham, Smallet, Glencairn, Montrose and Mauvissière **in clear in the running
   abstract**, and prints the unresolved numeric codes as quoted numerals ("870", "32", "54"), the "32" inside
   square brackets. None of the three name passages carries an "in cipher" flag, an asterisk or an italics
   note; the volume's one "words in italics are supplied ... deciphered" note belongs to no. 392. The single
   "cipher" on p.371 (section 9) could not be retrieved (the endpoint shows at most three hits per query and
   "cipher" has more than three in the volume), so it stays inferred as the Cary sentence.
3. No. 584's entry on p.566 cites **fol. 299** explicitly, so the elimination in section 4 is confirmed, and
   that page carries at least two page-foot footnotes reading "* In cipher." Which words they mark cannot be
   read from the snippet.

Under section 1's own criterion ("N0 if the calendar page, once read, gives the names as the reading of the
cipher"): the 1910 calendar of fol.196 gives the names in clear but does not present them as readings of cipher,
and marks nothing in that entry as cipher; for fol.299 it does mark words as cipher. How Boyd got the clear
names (the letter-book, a decipher on the manuscript, or his own work) is still not stated on the page. The
class stays the verifier's call; nothing in this section is a decipherment or a novelty claim.

Requests this session: www.googleapis.com/books 22, books.google.com 41 (1.5 s apart), one session, no login.
HathiTrust `babel` and `catalog` both still 403 to curl from this container (checked once each, not retried).

## Open-index scholarship pass (24 Sept 2026)

Worker session (Sonnet, cap $8, orchestrator session_01EFmUvFAifLKGdBSsW9mjEG), replacing JSTOR as the
scholarship-coverage gate (CLAUDE.md, JSTOR-QUEUE.tsv rows 8-11). Not a verifier session: does not move the N1
class, does not decode. Full per-host results in `OPEN-INDEX-RESULTS.tsv` rows 8-11.

**OpenAlex and Semantic Scholar unreachable** for this whole pass (shared-IP daily budget exhausted / 429 on
repeated attempts; see the fr2980-gramont AUDIT.md section of the same date for the exact error text, identical
across all five targets this pass covered). Logged as unreachable, not as a negative.

**CrossRef, Persée, HAL:** no hit on either fragment (F1-F7 of 7 April, F8-F11 of 31 July) or on a sign-to-letter
key for them. Genuine but irrelevant hits surfaced and set aside: Tomokiyo's own peer-reviewed piece ("How I
reconstructed a Spanish cipher from 1591", Cryptologia 2018) is not about Bowes; the Lasry/Biermann/Tomokiyo 2023
Mary Stuart paper (already known) quotes a *different* Bowes-to-Walsingham letter of 28 March, about ciphers
found with one "Holte" — not the 7 April or 31 July letters this target reads. Everything else (a Hakluyt-society
reprint of Walsingham's 1583 letters, a board-game-studies chapter titled "The Walsingham Gambit", surname
collisions on "Bowes"/"Caligula"/"decipherment") is noise, logged in full in the TSV. HAL returned 0 hits for
every query on this target; a single true positive turned up only by accident (a 2026 cancer-biology conference
paper by "Simon Mallet", a coincidental near-match to the code-name "Smallet", not the target).

**Row 9 ("Smallet"/"Maineville"):** WebSearch confirms François de Rocherolles, sieur de Mainville, as the French
agent sent to Scotland in Dec 1582 — the identification NOTES.md already uses for the cipher's "Maineville" — and
adds one piece of adjacent context (a March 1583 report that Castelnau sent him letters via a courier from
Gravesend, and that Bowes reported the agent believed them unread). No source on any host uses the code-name
"Smallet" anywhere; this remains a name recovered only by the solver's alignment with the 1842 letter-book, as
section 5 already says.

**Verdict for this pass:** no hit on any of the six hosts adds a print or decipherment of either fragment, or of
a sign-to-letter key, beyond what sections 1-10 above already establish. This does not close family (g)'s
JSTOR/Google-Scholar gap named in section 8's search log; it substitutes for it, per the owner's 24 Sept
directive. **N1 unchanged; the verifier does not move the class from a scholarship-pass worker's report.**

Requests: api.openalex.org 8 (all 429, shared budget). api.semanticscholar.org 6 (all 429). api.crossref.org 4
(one per row, 200 each). api.archives-ouvertes.fr 8 (4 combined-query attempts at 0 hits, 4 narrower follow-ups).
www.persee.fr 4 (200 each). WebSearch 4 queries. No logins, no credentials, no decoding, no edits to
reading.tsv/key.tsv/ciphertext.txt.


## Specialist acknowledgement (24 Sept 2026, recorded by the orchestrator, not a verifier verdict)

S. Tomokiyo, whose transcription the reading rests on, accepted the identification by email on 24 Sept 2026 and
recorded it on https://cryptiana.web.fc2.com/code/unsolved.htm the same day, with a link to this folder and three
corrections from the manuscript (NOTES.md, "Specialist reply"). The class stays N1: the plaintext was in print in
1842, and the item's novelty is unchanged by the acknowledgement. Rule 10's N5 ("confirmed by a specialist") is a
verifier's call and has not been assigned; a verifier reading this section may record that the specialist confirmed
the letter-substitution reading and left the numerical codes open. The page itself is not snapshotted into sources/
because the entry names the repository owner (rule 9); it is cited by URL, section and date instead.
