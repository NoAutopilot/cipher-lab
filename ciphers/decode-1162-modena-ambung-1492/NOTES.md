# decode-1162-modena-ambung-1492

Status: partial
(VERIFY-MOD1162, 3 Oct 2026: AUDIT.md -- plaintext of the cipher runs N0, period gloss on the leaf and DECODE doc 3593; the 1168-key finding re-derives and its control holds.)
(MOD1162, 3 Oct 2026: decode-1168's key read on this letter's cipher groups, gate PASS against a band-shuffled key; the letter's own period gloss gives the plaintext of most groups. See "## MOD1162" below.)
Berzeviczy 1914, *Aragóniai Beatrix magyar királyné életére vonatkozó okiratok* (IA `aragoniaibeatrix00berz`), read by this worker (GF4-BATCH19, 3 Oct 2026) by full-text search of the whole IA OCR and by reading the 1492 table of contents (nos. CLI-CLXXXIII, pp. XXX-XXXI) and nos. CLIV-CLV (pp. 214-219): no Costabili letter of 27 Feb 1492 is printed, letter absent.

## What this is

DECODE R1162: envoy report, State Archives of Modena, Amb. Ung. b.2/20 no.6, Ferrara, 1492, Italian (Partially
decrypted, 2 images, one attached document tagged `[transc]`, "SAMo_Amb_Ung_b_2_20_6"). QUEUE.md row DC4, and
the named anchor for a further cluster of nine related Modena/Milano envoy-report records (DC10-DC19), none of
which are in this brief. Checked as part of LANE N check-solved batch DC1
(`.claude/briefs/runs/2026-09-24-lane-n-csDC1.md`).

## Check-solved sweep, 24 September 2026

1. **Aymeloglu.** `unsolved-ciphers/catalogue/decode-ranked.md` row: "| 5 | [1162](.../RecordsView/1162) | 1492
   | State Archives of Modena, Amb. Ung. b. 2/20, 6, Envoy reports, Ferrara | Eleonora d'Aragona | Italian | 2 |
   transcription attached; inline cleartext |" — the sender/recipient field reads "Eleonora d'Aragona" (Duchess
   of Ferrara), sharper than QUEUE.md's generic "Ferrara/Milan correspondence". This id is absent from that
   file's "Already carrying a deciphered text in DECODE" list (checked directly), so per this scrape the
   attached document is a transcription only, not a full decipherment.
2. **Web.** WebSearch `Beltrame Costabili ambasciatore Ungheria Ferrara 1491 1492 lettere cifra` surfaced a
   named, unread lead consistent with the brief's "Este ambassador editions" instruction: a Pázmány Péter
   Catholic University (PPKE) thesis, Dóra Labancz, "Lettere su e dall'Ungheria: 1491" (`btk.ppke.hu`), and a
   related published article on Taddeo Lardi's letters from Hungary 1487-1499 (`ojs.ppke.hu`, Verbum). Both
   concern exactly this Este-to-Hungary envoy correspondence — Beltrame Costabili was Ferrara's envoy to the
   Hungarian court under Duchess Eleonora d'Aragona in this period — but neither document was opened this pass
   to check whether it prints or discusses this specific cipher item. Flagged as the edition to check next,
   not confirmed absent.
3. **Tomokiyo.** No hit in `sources/cryptiana/` for "Amb. Ung.", "Costabili", "Eleonora d'Aragona" with
   1491/1492, or this shelfmark.
4. **Bourdeau.** dbourdeau/cyphersolver's `CATALOGUE.md`/`TARGETS.md`: no entry for DECODE id 1162 or this
   shelfmark.
5. **DECODE.** A prior LANE N pass this session read R1162's RecordsView page directly (QUEUE.md DC4 row): the
   attached `[transc]` document was noted but not opened, per that worker's brief scope.
6. **Community lists.** None found this pass.

## Verdict

**Open**, not blocked: the PPKE thesis/article found above is a real, unread lead for the named edition family,
and should be opened before this target is promoted or transcribed — until then this is a search result ("no
prior decipherment located by this method, on this date"), not a completed print check.

Requests this pass: WebSearch 1, github.com 0 (reused shared clones). No fresh DECODE login. No promotion, no
decoding; the attached `[transc]` document was not opened (out of scope for this brief).

## LANE N audit, 24 September 2026

**DocumentsList check** (`DocumentsList?showmaster=records&fk_id=1162`): confirms exactly one attached
document, ID 3593, title `SAMo_Amb_Ung_b_2_20_6`, category **Transcription**, uploaded 2 Jan 2021 (uploader
id 32), marked Public. No key or decipherment document. RecordsView: `Available Documents: Transcription`,
`Inline Cleartext: Yes`, `Inline Plaintext: No` — the "Partially decrypted" status tracks the attached
transcription (the ciphertext has been read off the page), not a broken cipher. Verdict unchanged: **open**,
cryptanalysis, transcription step already done by the attached document (still not opened here, out of this
brief's scope — a next worker should read `DOC_R1162_D3593_3593.txt` via a fresh DECODE login before any
fresh transcription pass).

**Edition gap, PPKE lead (job 3).** Both named PPKE sources were fetched and read in full this session:
- Dóra Labancz, *Lettere su e dall'Ungheria: 1491* (thesis, Università Cattolica del Sacro Cuore / PPKE,
  2012; `btk.ppke.hu/storage/tinymce/uploads/old/uploads/articles/1636637/file/Dora_Labancz_tesi_finale_per
  Pázmány.pdf`, 148 pp., fetched and converted with `pdftotext -layout`). Zero occurrences of "Costabili"
  anywhere in the text. Its letter corpus is the Archivio di Stato di Milano, fondo Sforzesco (e.g. "Archivio
  di Stato di Milano, fondo Sforzesco, cartella 645", 17 June 1491, Bologna) — Milanese/Sforza diplomatic
  correspondence about the Hungary-Sforza marriage negotiations, not Ferrara/Este correspondence. It does
  discuss cipher use among Sforza envoys generally ("spesso cifrate", citing Cerioni, *La diplomazia
  sforzesca*, for a "sistema di cifratura per sostituzione monoalfabetica, con lettere nulle ed omofoni") and
  transcribes at least one ciphered Sforzesco letter (cartella 645, "copia contemporanea di una lettera in
  cifra"), but none of this is Costabili's Ferrara-Modena material. **Not a match for R1162.**
- Verbum 2022/2, "Le prime lettere di Taddeo Lardi dall'Ungheria (1487–1499)" (`ojs.ppke.hu/index.php/verbum/
  article/download/188/172`, HTML full text fetched). Discusses Beltrame Costabili only in passing, as
  governatore of Ippolito d'Este's household in Buda/Esztergom (the article is about Lardi's own career as
  treasurer/majordomo under him). Zero occurrences of "cifra"/"cifrat-" anywhere in the article; no mention of
  a specific Feb/Mar 1492 letter or the Amb. Ung. b.2/20 shelfmark. **Not a match for R1162.**

Both PPKE leads are genuine editions of Este-Hungary-adjacent correspondence from the same years but neither
covers this specific cipher letter or Costabili's own outgoing correspondence to Eleonora d'Aragona. This is a
negative result for the log, not a block: no calendar/edition covering Costabili's own letters to the duchess
was located this pass. Status word unchanged (open).

Requests this pass: WebSearch 2, curl direct-fetch 2 (ojs.ppke.hu HTML, btk.ppke.hu PDF, one each, no repeat
retries), de-crypt.org (shared single login, see decode-2678's NOTES for the full per-host count).

## DECODE fetch, 24 Sept 2026

For LANE R2 (ROOM 08:50 flag). First login (`tools/decode_browser_login.js`), `--fetch-page RecordsView/1162`
plus auto-discovery of its `/decrypt-custom/filesrv` links, `--delay 1600`, `--max-files 10`: fetched 2 images
into `images/` (`TH_IMG_R1162_I5837_P1.png`, `TH_IMG_R1162_I5838_P2.png`, ~100 KB each) and confirmed
`DocumentsList?showmaster=records&fk_id=1162` still shows only the one attached document (id 3593, title
`SAMo_Amb_Ung_b_2_20_6`, category Transcription, uploaded 2 Jan 2021, Public) — but the record's 8 image
links (from decode-4450's fetch, processed first in the same run) plus this record's 2 images filled
`--max-files 10` before the doc link, found later in the RecordsView/1162 HTML than its images, could be
queued.

Second, minimal login targeting only the known missing URL (`--fetch
https://de-crypt.org/decrypt-custom/filesrv/?file=DOC_R1162_D3593_3593.txt`, no new page discovery, 1 file):
**the document could not be retrieved.** The server returns HTTP 200 with `Content-Type: image/png` and
`Content-Disposition: inline; filename="forbidden.png"` -- a fixed 986x568 PNG placeholder (sha1
`035489a0605851154ab88372216354b63596ca22`), byte-identical whether requested inside the logged-in browser
context (`ctx.request.get`, cookies attached) or with a bare, unauthenticated curl. This is not a login or
session bug on this pass: the same URL returns the identical placeholder either way, so the account (or the
document/category) is simply not permitted to fetch this attachment through `filesrv`, regardless of login.
**Corroborating evidence this is a standing site behaviour, not new**: `ciphers/intercepted-royalist-1646/
decode/DOC_8725_2024-Oct-12-01-36-20_15694.txt`, committed by an earlier worker as if it were record 8725's
real attached document text, is byte-identical to this same `forbidden.png` placeholder (same sha1) --
that file is mislabeled and contains no real content. Flagged in ROOM.md; not fixed here (out of this
brief's scope, names only 4450/1162).

No transcription document is on disk for this target; `images/manifest.json` records the attempt and the
placeholder's sha1 so a future pass does not repeat the same fetch believing it might succeed differently.
Two logins used this pass (brief asked for one; the first's auto-discovery order used up `--max-files`
before reaching the doc link -- see manifest for detail); no further DECODE login should be needed to
re-attempt this specific document, since the forbidden-placeholder result appears independent of login.
Folder now 220 KB, well under the 30 MB cap.

## D1: transcription, 24 September 2026

**Blocked on image resolution, no blind passes run.** Both files fetched via `filesrv` are named `TH_IMG_*`
("thumbnail image") and are in fact thumbnails: 200x300px for the full page (confirmed with `file`). Tried
6x and 10x Lanczos upscales of several regions (whole-line crops and single-word crops) in the scratchpad;
individual letterforms remain an unresolvable blur of ink specks at every zoom tested -- there is not enough
source information to recover, not just a display-scale problem. This is the same finding an earlier worker
logged for `ciphers/intercepted-royalist-1646/` on an identically-named/sized DECODE thumbnail ("too small to
transcribe" at 200x268/200x267), so it looks like a standing limitation of what `RecordsView`'s auto-discovered
`filesrv` links serve for this record, not a one-off.

Per CLAUDE.md rule 2 (image over transcription) and rule 7 (a reading must be reproducible from the image), a
blind line/token pass against an image this small would not be a real transcription -- it would be invented
detail dressed as a reading. No `ciphertext.tsv` was written; wrote `inventory.tsv` instead, at page level only
(recto/verso, rough line count, layout, seal/docket features), each row marked "class undetermined" for
cipher-vs-clear because that distinction needs legible letterforms this image does not provide.

**What is established:** 2 pages, recto (~15-16 lines, torn top-left corner) and verso (~6-8 lines of the main
hand, a small ruled address/docket panel, a probable wax-seal remnant, otherwise blank) -- consistent with a
single folded letter. Symbol inventory, token counts, and any cipher-vs-clear classification are not possible
from what's on disk.

**Follow-up (one-line suggestion, not run here):** a networked worker should check whether DECODE's own page
viewer (not just the `filesrv` links `decode_browser_login.js` auto-discovers) offers a larger image for
record 1162 -- e.g. a lightbox/zoom control on `RecordsView/1162` -- before writing this off; if the platform
genuinely serves nothing larger than 200px for this record, the attached transcription document (id 3593,
still unreachable, see above) is the only route left for this target's ciphertext.

Grades: none (no tokens read). Requests this pass: 0 (no network, per brief). Cost: transcription-pass work
only, well under the $6 cap shared with decode-4450 (see that folder's NOTES.md for the combined total).

## DECODE image-check follow-up answered, 24 September 2026

The "one-line suggestion" above (check DECODE's own viewer for anything larger than the 200px thumbnail)
was tried: no larger image exists. Full method and evidence in `sources/decode/NOTES.md` ("No larger image
than the 200px thumbnail for 1162 (and 4450)"). Summary: RecordsView's on-page zoom modal reuses the same
`TH_IMG_*` thumbnail URLs (CSS-stretched, not a real zoom); the guessed non-`TH_`-prefixed filenames the
modal's own `alt` text names (`IMG_R1162_I5837_P1.png`, `IMG_R1162_I5838_P2.png`) return the same
`forbidden.png` placeholder already seen for the blocked transcription document; the "Image Manager"
(`ImagesList?showmaster=records&fk_id=1162`) link redirect-loops when opened directly and was not reachable
this pass. Status unchanged: **open**, still blocked on image resolution for a blind transcription pass; the
attached transcription document (id 3593) remains the only route to this record's text, and it is also
blocked (same placeholder, see `sources/decode/NOTES.md`).

## LIKELY-4 (2 Oct 2026, account-4)

Brief `.claude/briefs/runs/2026-10-02-account4-likely-phase2.md`, row 4 of
`ciphers/_triage/likely-solves-2026-10-02.tsv`. Named first cheap test: apply the decode-1168 key to this
record's public DECODE transcription against 20 shuffled-key controls, login-free, at most 10 de-crypt.org
requests, no login. Clock read 03:34-03:4x UTC.

**Intake gate.** `python3 tools/intake_gate_check.py decode-1162-modena-ambung-1492` -> exit 0, output
"blocked (line 116) -- already terminal, nothing to gate". The tool took the word "Blocked" from the D1
transcription section's bold heading (line 116), not from the status line (line 3, `open`); exit 0 either way,
so nothing to do before the test, but a later pass should know the gate's parse of this file is of the
section heading, not the status word.

**The test did not run: both of its inputs are missing, so it is a non-test, not a negative (rule 3).**

1. *No key.* The triage row's head start (a) reads "sibling decode-1168-modena-costabili-1492 is partial with a
   key for the same Modena chancery". The sibling folder holds one file, NOTES.md; its `partial` is DECODE's own
   "Partially decrypted" status word, copied on 24 Sept 2026 without anyone confirming what it refers to (that
   NOTES.md says so in its own verdict). No key for 1168 exists on disk, in `keys/`, or anywhere else in the
   repository (grep for the record id and "Costabili" across keys/, ciphers/, QUEUE.md). So there is no key to
   apply and no key to shuffle. The 20-control calibration is therefore also unrun: a control cannot run
   before the instrument exists.
2. *No ciphertext.* The attached transcription document (id 3593, `DOC_R1162_D3593_3593.txt`) is still the
   site's `forbidden.png` placeholder when fetched login-free, re-checked today (request 3 below): HTTP 200,
   `Content-Type: image/png`, `Content-Disposition: inline; filename="forbidden.png"`, 17947 bytes, sha1
   `035489a0605851154ab88372216354b63596ca22`, byte-identical to the 24 Sept result. The only images on disk
   are the two 200x300 thumbnails (D1 section above), unreadable. No `ciphertext.txt`, no `inventory` of signs.

Login-free requests this pass (de-crypt.org, descriptive User-Agent, 1.6 s apart, 03:36-03:37 UTC):

| # | URL | result |
|---|---|---|
| 1 | `RecordsView/1162` | HTTP 200, 104 KB HTML, served without login (metadata block readable, see below) |
| 2 | `DocumentsList?showmaster=records&fk_id=1162` | HTTP 302 -> `/decrypt-web/login` (needs login) |
| 3 | `filesrv/?file=DOC_R1162_D3593_3593.txt` | HTTP 200 but the `forbidden.png` placeholder, sha1 `035489a0...` |

Vision calls: 0. No other host. No login attempted (brief).

**What the login-free record page adds (new to this folder).** RecordsView/1162's metadata block, read without
login: Author *Beltrame Costabili*, Receiver Eleonora d'Aragona, origin *Esztergom*, Hungary, start date
*27 February 1492* (Start Year 1492, Month 2, Day 27), 2 pages, symbol set graphic signs, "Cipher Type (notes):
Homophonic or simple substitution", Cleartext Italian, Plaintext "Italian?", Inline Cleartext Yes, Inline
Plaintext No, "Private Ciphertext: True", Available Documents: Transcription. Earlier passes had this record as
"envoy report, Ferrara" with the sender unread; it is the same envoy, place and month as decode-1168
(Costabili, Esztergom, 20 March 1492, b.2/21 no.8), three weeks earlier (b.2/20 no.6). The triage row's named
risk ("1168 and 1162 are different envoys' keys") is answered: same author, same posting, same month. A key
recovered from either letter is the first thing to try on the other.

**The premise of the brief's own stop condition is stale.** The brief says "the full-size images are
account-blocked". ASKS.md row 42 was answered on 28 Sept 2026: the DECRYPT PI extended this account's access,
and DECODE-OPEN (sources/decode/NOTES.md "Full-size images: access after the PI's extension (28 Sept 2026)")
fetched full-size images for 18 formerly blocked records through one `tools/decode_browser_login.js` login;
its listener run also fetched "5 documents". Whether 1162's transcription document and its two full-size
images (`IMG_R1162_I5837_P1.png`, `IMG_R1162_I5838_P2.png`, the names in the zoom modal's alt text) now come
through for a logged-in session has not been tested since the extension; every "blocked" line in this
folder and in sources/decode/NOTES.md about 1162 predates it (24 Sept). This worker's brief forbade a login,
so it is untested here, not failed.

**Status word stays `open`** (rule 5): the blocker is not outside the session; a known, untried, cheap
instrument exists. A `blocked` status would be wrong while that instrument is untried, and a LOCAL-QUEUE row
for the owner's desk would be premature for the same reason (and the key livecheck rule: DECODE_USER/
DECODE_PASS are present and the login works, so no access row may be filed on them).

**Next step (one logged-in fetch, Sonnet, about USD 1-2 priced from DECODE-OPEN's 7.56 for 73 requests):**

```
NODE_PATH=$(npm root -g) node tools/decode_browser_login.js 1162 ciphers/decode-1162-modena-ambung-1492/decode \
  --fetch 'https://de-crypt.org/decrypt-custom/filesrv/?file=DOC_R1162_D3593_3593.txt' \
  --guess-fullsize --max-files 3 --delay 1700
```

Check each file with `file` and the saved `Content-Disposition` before trusting it (a PNG signature or
`filename="forbidden.png"` means the fetch failed, sources/decode/NOTES.md 24 Sept). Images stay in the
scratchpad or under the 30 MB folder cap and are not published (the PI's reminder, DECODE-OPEN). If the
document comes through: it is the record's own transcription of a 2-page mixed cipher/clear letter
(Inline Cleartext Yes), so the first paid step is the known-answer step on its clear passages, then the same
logged-in fetch for 1168's record (its "Partially decrypted" document, if one is attached, is the only
candidate key source for this pair) before any shuffled-key run. If the document is still the placeholder
for a logged-in session after 28 Sept, the next step is the row below, and only then does this folder read
`blocked`.

**LOCAL-QUEUE.tsv row, drafted, to be appended only if the logged-in fetch above returns the placeholder
(tab-separated; id to be assigned by whoever appends it):**

```
L<n>	decode	ciphers/decode-1162-modena-ambung-1492	LIKELY-4 (2 Oct 2026). DECODE record 1162 (https://de-crypt.org/decrypt-web/RecordsView/1162, Costabili to Eleonora d'Aragona, Esztergom 27 Feb 1492, ASMo Amb. Ung. b.2/20 no.6) has one attached document, id 3593 'SAMo_Amb_Ung_b_2_20_6', category Transcription, marked Public, plus two page images. From the cloud, logged in or not, https://de-crypt.org/decrypt-custom/filesrv/?file=DOC_R1162_D3593_3593.txt returns the site's forbidden.png placeholder (sha1 035489a0605851154ab88372216354b63596ca22; last checked <date of the logged-in retry>). In a desk browser logged in to de-crypt.org: open the record, click the Transcription document under 'Available Documents', save it as ciphers/decode-1162-modena-ambung-1492/decode/DOC_R1162_D3593_3593.txt (check it is text, not a PNG), and from the image viewer save the two full-size page images (zoom modal, filenames IMG_R1162_I5837_P1.png and IMG_R1162_I5838_P2.png) into the same folder's images/ with a manifest.json line each (url, bytes, sha1, date). Quote the document's first line in the result cell. If the site shows the same placeholder in the browser, say so and quote the message.	queued	
```

Follow-up (one line, not run here): correct the triage row's head_start cell for row 4 -- 1168 holds no key --
so the parent does not re-rank it on that premise; and the 1162/1168 pair is a two-letter sign pool of one
envoy, one posting, one month, which is the shape the selection rule prefers once either text is on disk.

## Edition citation (GF4-BATCH19, 3 Oct 2026)

Standard edition for Este dispatches from Hungary about Beatrice d'Aragona: Albert Berzeviczy (with T. Gerevich and E.
Jakubovich), *Aragóniai Beatrix magyar királyné életére vonatkozó okiratok* (Budapest 1914; Vestigia's own bibliography
for this busta cites it), IA `aragoniaibeatrix00berz`, `_djvu.txt` fetched once (1.34 MB) and grepped. The 1492 table of
contents (pp. XXX-XXXI) runs CLI 20 Jan, CLII 23 Feb (Vimercati, Venice), CLIII 17 Mar, CLIV 19 Mar (Costabili),
CLV 20/22 Mar (Costabili), ... CLXII 3 May (Costabili): **nothing dated 27 Feb 1492 and no other Costabili letter of
Feb 1492.** Grep of the whole OCR for "Strigonii" + "Februarii"/"febr" and for "Costabili": no 27 Feb letter. The
other standard series (Nagy-Nyáry, *Magyar diplomacziai emlékek Mátyás király korából*, 4 vols) stops at 1490, out
of range. Letter absent from the edition; a search result, not a novelty verdict (rule 10).

## Web and blog check (GF4-BATCH19, 3 Oct 2026)

Web searches (4): (1) `Beltrame Costabili Eleonora d'Aragona 1492 Esztergom cifra lettera` -- PPKE Lardi article
(already read 24 Sept), Szakács, *Câteva aspecte ... Beltrame Costabili* (Studium 13, studium.ugal.ro PDF, fetched,
grepped: no "cifr"/"zifra", no Feb 1492 letter), Vestigia, Treccani; nothing about this letter. (2) `"Amb. Ung."
Modena Costabili cipher 1492 DECODE` -- nothing relevant (Bourdeau's site index only). (3) `Costabili Esztergom 1492
ciphered letter Este Hungary decipherment solves Claude` (also the model-solve query) -- Láng, *Real Life Cryptology*
(2018), Szakács on academia.edu; no reading of this letter, no model-solve announcement. (4) `Costabili "27 febbraio
1492" OR "XXVII Februarii 1492" Strigonio Eleonora` -- nothing.
Blogs, site search by name, 3 Oct 2026: **Cipherbrain** (scienceblogs.de/klausis-krypto-kolumne `?s=Costabili`):
no results. **Cryptiana blog** (cryptiana.blogspot.com `search?q=Costabili`): "No posts matching the query"; on-disk
`sources/cryptiana/` (Tomokiyo's pages): no "Costabili", no R1162. **Cipher Mysteries** (`?s=Costabili`): "Nothing
Found". No hit, so no comment thread to read.
Other projects' new publications: **Cabinet Noir** (github.com/el-descifrador/cabinet-noir, shallow clone HEAD
47b6db9, 3 Oct 2026): 24 project folders, none Este/Modena/Costabili/1492 (grep hits were only digit strings).
**Apeiron** (apeiron.re front page, 1 request): no publication list served; its only known publication is Koehler
(STATUS.md check-in 38). Solver repos: Aymeloglu (HEAD d2800bb) lists R1162 in `decode-ranked.md` only, no attempt;
Bourdeau (HEAD a439937) `research/oldest/CANDIDATES.md` B2 lists "Beltrame Costabili, Esztergom 1491-93
(R1162-R1168, R1095-R1097)" with "Valentini and Costabili not checked".
No decipherment or plaintext of this item located by these queries on 3 Oct 2026.

## Premise check (GF4-BATCH19, 3 Oct 2026)

(a) Folder's own mentions: DECODE says "Partially decrypted" with one attached Transcription document (id 3593),
still the forbidden placeholder (LIKELY-4); "Inline Cleartext Yes" means clear passages on the leaf. Not a
decipherment in hand -- **not found**, but the document is still the first thing to read once fetchable.
(b) Other solvers' working files: Bourdeau B2 found that in the same Modena series (Sadoleto, Buda 1483, R1107-R1118)
"every letter has a contemporary decipherment (filed copies or clear slips pasted on the leaf)" -- the shape to
expect here; Costabili explicitly unchecked. **Not found** for 1162.
(c) Neighbouring leaves: Vestigia (vestigia.hu, the ELTE/OTKA 81430 database of this series; 7 record pages, 6
thumbnails, 2 searches) numbers busta 2 "Beltrame Costabili (1492)" nos. 1-3 = 16 Jan, nos. 4-5 = 7 Mar, no. 6 = 19 Mar
(simple copy, 2 pp., DF 295973-a, = Berzeviczy CLIV) with no. 7 its original, no. 8 = 20-23 Mar ("olasz, titkosírás",
3 pp., DF 295974), with **Vestigia 4068, a contemporary 3-page clear copy** (DF 295974-4) and printed in full as
Berzeviczy CLV pp. 216-219, headed "Titkos írásjegyekkel írva" (written in cipher). No. 8 is decode-1168's letter
(Costabili, 20 Mar 1492, b.2/21 no.8): **its plaintext is printed and a period clear copy exists** -- flagged in
ROOM.md for decode-1168, not worked here. For 1162 itself: Vestigia's no. 6 is the 19 Mar letter, not 27 Feb, and a
pixel correlation of Vestigia 3014's four 200x300 thumbnails against DECODE R1162's two (no vision call) gives
0.60-0.69 against 0.51-0.66 for no. 8's thumbnails as controls -- not the same pages. Vestigia search for
"1492-02-27": 0 results. So DECODE's "b.2/20, 6" does not map onto Vestigia's numbering, and R1162's leaf was not
located on Vestigia this pass. **Not found**, but the 1168 result makes it likely that a clear copy of 1162 sits in
the same busta: the 1168 clear copy plus Berzeviczy CLV is now a period plain-cipher pair for **the same envoy's
key three weeks later** -- the key-source step for this letter (rule 4 grade C via `tools/interlinear_align.py`).
(d) Recipient-side edition: Berzeviczy 1914 (Eleonora's incoming dispatches) -- read above, letter absent.
**Not found.**

Next step (not run): rebuild Costabili's key from Vestigia 3016 (cipher original, 3 pp.) against Vestigia 4068 /
Berzeviczy CLV (clear), then the DECODE logged-in fetch for 1162 (LIKELY-4's command) and apply; ~$4.

Gate re-run (GF4-BATCH19, 3 Oct 2026): `decode-1162-modena-ambung-1492: open (line 3) -- edition/page or full-text-search citation found within 6 lines`, exit 0 (was exit 1).

## MOD1162: decode-1168's key applied to R1162 (account-2 worker, LANE-A2PUSH3, 3 Oct 2026, 14:20-14:3x UTC)

Brief: `.claude/briefs/runs/2026-10-03-acct2-mod1162.md`. Intake gate, 14:20 UTC:
```
$ python3 tools/intake_gate_check.py decode-1162-modena-ambung-1492
decode-1162-modena-ambung-1492: open (line 3) -- edition/page or full-text-search citation found within 6 lines
EXIT 0
```

**Fetch (the LIKELY-4 step, now run).** One DECODE browser login, 14:21 UTC: `NODE_PATH=$(npm root -g) node
tools/decode_browser_login.js 1162 <scratch> --fetch-page ImagesList,DocumentsList --fetch
'https://de-crypt.org/decrypt-custom/filesrv/?file=DOC_R1162_D3593_3593.txt' --guess-fullsize --max-files 6 --delay 1800`.
After the 28 Sept access extension everything came through, nothing was the forbidden.png placeholder: both full-size
images (2592x3888 PNG, sha1s in `images/manifest.json`, committed as 1400-px JPEGs `images/s_IMG_R1162_*.jpg`) and
**document 3593**, DECODE's own transcription (transcriber "RP", 11 Nov 2020, 98 min, manual), committed unmodified as
`decode/DOC_R1162_D3593_3593.txt`. So the 24 Sept "blocked on image resolution" and "document unreachable" findings
above are superseded. Requests: de-crypt.org 1 login, 3 pages, 6 files, 1.8 s apart.

**What the leaf is.** It is a letter in clear Italian with short runs of cipher signs, and a **period interlinear gloss
over most runs** ("la Regina", "sua M.ta", "pocha estima", "famiglia d arciuescouo", "in pre...", "ne comp...",
"il gouerno del arciuescouato d Strigonio"); DECODE's document tags these glosses as PLAINTEXT. Verso (image 2) is clear
text, signature and address only ("Steig. 27 fibr 1491 ... Bel. Cost..."; "Helyonore de Aragonia Duchesse Ferrarie").
The date is written **1491** on the letter and on the archive's target strip ("1491 év 02 hó 27 nap"); DECODE's record says
1492. Recorded, not settled here: if the year starts 25 March (Ferrara), 27 Feb 1491 is 27 Feb 1492 in modern reckoning,
three weeks before decode-1168's 20 Mar 1492.

**Pre-registration** `PREREG-MOD1162.md`, commit 53c61136, pushed before any decode or score. Statistic G = pooled
LCS(decoded, gloss) / keyed signs over the letter groups; control = 1168's key with values shuffled within its grade
bands (C among C, M among M), 1000 seeded draws; gate G > control p99 and G >= 0.50. The second named control (1168's key
on a different-envoy Modena cipher) was not run: there is none on disk (only 1162 and 1168 here).

**Transcription** (TRANSCRIPTION.md; crops before any vision call):
`python3 tools/iiif_lines.py --image IMG_R1162_I5837_P1.png --out <scratch>/crops --region 370,650,1963,2250 --centres
128,509,594,691,1049,1146,1554,2013,2110 --prefix p1 --lines-per-crop 1 --top-margin 75 --bottom-margin 35 --debug`,
which gave 9 line crops (1963x~360, each with the gloss above it). Two blind Sonnet passes (A in order, B in reverse), each one call
over the 9 crops, labels from 1168's sign list and no values shown: A has 13 runs and 82 signs, B 15 runs and 84 signs.
**err_2reader 0.146** (12 sign edits / 82, crop-pooled; part of it is naming, since A wrote "2"/"3" where B wrote "z"); err_true not
measurable (no benchmark item). The reconciliation was done by this worker from 2 crop views (L01, L08) plus agreement. Its choices:
drop the three "~" that both passes flagged as possible dashes (DECODE's transcription has no sign there); "2" -> z (B; "2"
is not in the label set); keep A's "a g" at the head of L01 (the gloss "il" sits over it); include "y a" in L08_3 (the
gloss "ne" sits over it). **This reconciler had seen the key and DECODE's transcription**, so the result is also given on
each raw pass below. `ciphertext.tsv` has 77 signs in 15 runs: 7 letter groups of 62 signs, and 8 dotted or short code
groups. Of the 77 signs, 25 carry conf '?' where the passes split. `gloss.tsv` gives pass A's gloss reading verbatim, as
pre-registered. Signs read: 166 over the two passes, for 3 subagent and worker units. Cost per 100 signs is the
orchestrator's figure to read.

**Result (rule 3, both numbers side by side; `score_g.py`, `--check` exits 0, `score_g.json`):**

| ciphertext | G target | control mean | control p99 | control max (1000) | gate |
|---|---|---|---|---|---|
| reconciled | **0.729** | 0.419 | 0.525 | 0.559 | PASS |
| raw pass A (scratch re-run) | 0.705 | -- | 0.508 | 0.541 | PASS |
| raw pass B (scratch re-run) | 0.645 | -- | 0.484 | 0.516 | PASS |

No control draw reached the target in any of the three (empirical p < 0.001). Coverage 95% of letter signs are in the key.
That figure is descriptive: a value shuffle cannot change coverage. Per group, decoded vs gloss: "ilpolernt" / il gouerno;
"poea" + "lstima" / pocha estima (TT=s, z=t, a=i, 8=m, +=a match); "loserlirino" / [lo] Seruipiana; "inpreeipttio" / in
pre...; "aamili" / famiglia; "nieomperino" / ne comp[e]rino. The misses fall on signs 1168 already grades M or where
the label set collides (g read as l, v and e; c read as p and g; q read as e and c), the same look-alike collisions that A2-COS2 named on f.12r.

**Judge** (rule 7, pasted; spec `specs/decode-1162-modena-ambung-1492.json`, it16dip, the nearest era/register corpus on
disk, on the 59 decoded letters of the letter groups):
```
FAIL language: score=-1.34, null_p99=-1.504, real_p05=-0.989, real_median=-0.808, mode=both, N=59
FAIL - decode-1162-modena-ambung-1492 (a PASS is a gate for a verifier, not a reading; rule 10)
```
Shuffled-key decodes through the same model have a median of -1.838 and a p95 of -1.512 (500 draws). The leaf's own period
gloss scores **-1.134**, also below real_p05. So by rule 3's gloss paragraph this judge cannot decide at this length and
register: it is not a negative. The gate is G, as pre-registered.
(VERIFY-MOD1162 correction, 3 Oct 2026: the gloss's -1.134 sits nearer real_p05 (-0.989) than the shuffled null (p99
-1.504), so unlike ZX-DEC349 the judge does separate genuine prose from noise somewhat at this N; the decode's -1.34 is
better read as the cost of its 27 known M-graded sign misreads than as "judge cannot decide". It stays not a negative on
the key question, which the judge does not test; G is the gate. See AUDIT.md.)

**Reading** (`decode.json`, `python3 tools/decode_key.py ciphers/decode-1162-modena-ambung-1492 --check`: "reading up to
date"): tokens 77: **H 0, C 32, S 10, M 27, I 5, U 3**. Grades, per the pre-registration through `votes.tsv`: C is a 1168
C-sign whose value agrees with this leaf's gloss, or a code group read from the gloss directly above it. S is a key-transferred
sign that was not contradicted. M is a sign that disagrees with the gloss or was read uncertainly. I is a code group valued by
repeat of a glossed code (`exceptions.tsv`). The plaintext of the cipher runs comes from the period gloss (C), not from
cryptanalysis. What this step adds is a control-backed check that **Costabili used the same sign key on 27 Feb as on
20 Mar**, plus the nomenclator codes it shows: `.t.` = la Regina, `.s.` = sua M.ta (3x), `T o 3/z o` = d[el]
arcivescovo (2x).

Key source: `period` (decode-1168's key, rebuilt from that leaf's period gloss) and this leaf's own period gloss. Not
classified for novelty (rule 10). VERIFIER WANTED flagged in ROOM.md.

## Remaining gaps (MOD1162, 3 Oct 2026)
Read so far: 77 of 77 cipher signs on p.1 assigned a value (C 32, S 10, M 27, I 5, U 3); verso has no cipher (DECODE doc 3593 and image 2)
- sign-label collisions (g, c, q, z; 25 conf-'?' signs) - blocker: not-attempted; err_2reader 0.146 and the M-graded misses above; next: one reconciliation unit by eye over crops L01/L05/L06/L08 against 1168's crops, or the owner's sign sorter for the joint 1162+1168 inventory, then re-run score_g.py and decode_key.py, ~$1.5
- the clear text of the letter (about 35 lines, DECODE doc 3593 is a rough transcription with many '?') - blocker: not-attempted; not needed for the cipher test, needed for a full edition of the letter; next: one transcription pass of the clear lines from the 9 crops plus re-cut full-line crops, ~$3
- code groups `T o` (L01) and `.e.` (L06, pass B only) - blocker: open-codes; one occurrence each, the L01 gloss not separable from the letter group's, the L06 sign unglossed and read by one pass

## Escalation (MOD1162, 3 Oct 2026)
- [x] siblings: decode-1168 key applied, gate PASS (G 0.729 vs control p99 0.525), MOD1162 3 Oct 2026
- [x] clear-pages: verso and the clear lines read by DECODE doc 3593 (rough), fetched MOD1162 3 Oct 2026
- [x] known-keys: decode-1168 key.tsv (period gloss key) is the known key, applied here
- [x] print: Berzeviczy 1914 checked, letter absent (GF4-BATCH19 3 Oct 2026)
- [ ] key-rebuild: joint 1162+1168 alignment with tools/interlinear_align.py (1162's own 7 glossed groups as extra pairs, --prior 1168 key) to settle the collided labels; planned
- [x] image-check: full-size DECODE images on hand, MOD1162 3 Oct 2026
- [n/a] retry: nothing failed that a retry would change
Verdict: keep going: 3 internal gaps; cheapest next: reconcile the collided labels by eye over crops L01/L05/L06/L08 and re-run score_g.py, ~$1.5
