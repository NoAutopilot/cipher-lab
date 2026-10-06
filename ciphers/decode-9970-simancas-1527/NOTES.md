# decode-9970-simancas-1527

Status: open
CSP Spanish III pt 2 (Gayangos 1877, IA calendarorleters0003vari), be-api full-text search for "Andrea del Burgo", "Burgo", "26th October 1527" and "1563" run by this worker (GF-A2B-1, 3 Oct 2026): del Burgo's Ferrara letters of 4, 18 and 24 Oct 1527 are calendared (some "(Cipher:)" extracts), no entry dated 26 Oct 1527 and no leg. 1563 citation surfaced; the DECODE images themselves are not this letter (Premise check (b)).

## What this is

DECODE R9970: Simancas, Archivo General de Simancas, sec. Estado, leg. 1563, fol. 572, 1527, Spanish
(Non-decrypted, 4 images, no attached document found on the record page). QUEUE.md row DC5. Sender/recipient
per aaymeloglu's scrape: Andrea del Burgo (Ferrara) to Chancellor [Mercurino] Gattinara, dated 26 October 1527.
Checked as part of LANE N check-solved batch DC1 (`.claude/briefs/runs/2026-09-24-lane-n-csDC1.md`).

## Check-solved sweep, 24 September 2026

1. **Bourdeau.** dbourdeau/cyphersolver's `CATALOGUE.md` entry 2.5 is this exact item: "AGS, sec. Estado, leg.
   1563, fol. 572 (DECODE R9970) ... DECODE R9970: Non-decrypted, 4 pp., unknown; alphabet, graphic signs,
   numerical; images login. Not viewed here. DECODE note: Letter dated October 26, 1527, from Andrea del Burgo
   to Chancellor Gattinara from Ferrara." Catalogued but explicitly "not viewed", confirming it has not been
   solved or attempted there.
2. **Editions.** CSP Spanish (Bergenroth/Gayangos), the brief's named edition for Simancas Estado 1509-1527:
   found `calendarorleters0003vari` (Gayangos, 1877, internetarchivebooks) on archive.org. An archive.org
   be-api full-text search for `"Andrea del Burgo" "Gattinara"` returns this volume as a hit, with highlighted
   snippets about "Giovan Bartholomeo da Gattinara" (Mercurino's nephew) — the query is a document-level AND,
   not a phrase match, so this does not show both names co-occurring on the same page, only that the volume
   discusses Gattinara's circle at length. Per the Access playbook's 23-24 Sept 2026 finding, be-api's
   `page_num` field is not a real page locator (it equals the item's total page count), so this hit cannot be
   cited to a page; the volume was not opened and read page by page this pass.
3. **Aymeloglu.** id 9970 is present in `decode-catalog.csv`/`decode-records.jsonl` as a routine catalogue
   entry; absent from `decode-ranked.md`'s printed rows and from `exclude.txt`.
4. **Tomokiyo.** No hit in `sources/cryptiana/` for "Andrea del Burgo", "leg. 1563", or "fol. 572".
5. **Web.** WebSearch `"Andrea del Burgo" Gattinara 1527 cifra Simancas carta` returned only general
   biographical pages (Gattinara's Wikipedia entry, del Burgo as Maximilian's ambassador alongside Gattinara in
   1509) — no specific mention of this 1527 cipher letter or a decipherment.
6. **Community lists.** None found this pass.

## Verdict

**Open.** CSP Spanish (Gayangos, vol. 3, 1877) is the named edition for this period and discusses Gattinara's
circle, but was not opened to a specific page this pass — the archive.org full-text search cannot cite a page
number for this item, per the Access playbook. A worker with more budget should read the relevant supplement
volume covering late 1527 directly (or the volume's own index for "Burgo") rather than rely on full-text
search alone before this is called blocked. Not found by any of the six sources checked.

Requests this pass: WebSearch 1, archive.org 2 (advancedsearch 1 + be-api fts 1, >=3s apart), github.com 0. No
DECODE login. No promotion, no decoding.

## LANE N audit, 24 September 2026

**DocumentsList check** (`DocumentsList?showmaster=records&fk_id=9970`): **"No records found"** — no
attached document. RecordsView: `Available Documents:` (empty), `Inline Cleartext: Yes`, `Inline Plaintext:
No`. No change to the verdict: still **open**, cryptanalysis. Status word unchanged.

**Edition gap (job 3): CSP Spanish vol. 3.** Identified the correct HathiTrust volume for the letter's date
(26 Oct 1527, per Bourdeau's `CATALOGUE.md` entry 2.5): *Calendar of letters, despatches, and state papers ...
preserved in the archives at Simancas, Vienna, Brussels, and elsewhere*, v.3 pt.2, 1527-1529 (Gayangos, 1877),
HathiTrust id `msu.31293027025760`, 1214 pages (bibliographic search only, catalog.hathitrust.org not queried
directly — found via WebSearch). Ran `tools/htrc_ef_headwords.py msu.31293027025760 --words
burgo,gattinara,ferrara,cipher` (HTRC Extracted Features API, no HathiTrust page view, no login) to place the
correspondence without reading the Cloudflare-gated site. Del Burgo (69 pages), Gattinara (81 pages) and
Ferrara (191 pages) all recur throughout the volume, as expected for its two chief correspondents-adjacent
figures over two years — not by itself a page citation. Narrowed by requiring all three tokens within one page
of each other: **seq 508, 643, 851, 980, 1065, 1105, 1129** (scan sequence numbers, front matter included, so
not printed page numbers). Of these, **seq 508 and seq 980** also fall within one page of a "cipher" token hit,
the two strongest candidates for the entry itself or an adjoining editorial note. **Not read**: HathiTrust's
page images are Cloudflare-gated and out of this brief's host list (data.htrc.illinois.edu and
catalog.hathitrust.org's bibliographic API only); nobody has yet opened seq 508 or seq 980 to confirm this is
the 26 Oct 1527 del Burgo-to-Gattinara letter or check for an "in cipher"/deciphered editorial note. This
narrows "read a 1214-page volume" to "read two candidate pages" for whichever worker has HathiTrust access
next (or the person, via `REQUEST.md` if a login proves necessary) — genuine progress, not a block, and not a
confirmed page citation. Status word unchanged (open); no REQUEST.md written (nothing here needs the person's
direct action yet, only HathiTrust page access which the tool list may open to a future worker).

Requests this pass (job 3 only): WebSearch 2 (PPKE, HathiTrust catalog record), data.htrc.illinois.edu 2
(metadata + pages, one volume, cached to disk), curl direct 0.

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/burgo1527/NOTES.md ; targets/burgo1527/reading_evidence.md
- Their extent, in their words: explained, not a cipher: R9970 images are a clear Spanish minute, two drafts of Charles V to Prince Philip about a Fugger exchange, 1543-1554; the Burgo->Gattinara letter of 26 Oct 1527 is not on these scans; catalogue 198 removed, DECODE correction queued
- Their date: 28 Sept 2026
- Note: NOT in our NOTES.md (grep burgo1527, "not a cipher": 0). Earlier (22-23 Sept) they had "attempt closed, target unread"
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## Web and blog check (GF-A2B-1, 3 Oct 2026)

Plain web searches (WebSearch, 3 Oct 2026):
1. `"Andrea del Burgo" Gattinara 26 octubre 1527 Ferrara carta cifrada` (sender + recipient + date) -- Este-court
   cipher pages (Bologna FICLIT exhibit, "La parola incognita"), Estudios Románicos articles on imperial ciphers
   (Rome 1543 and others), a Milan SSMD article. None names this letter.
2. `Simancas Estado legajo 1563 folio 572 cifra` (shelfmark + cipher) -- Simancas generalities, british-history.ac.uk
   CSP Simancas (Elizabethan volumes), UCM article on the archive's founding. No hit.
3. `"Andrea del Burgo" cipher letter 1527 deciphered Gattinara` -- british-history.ac.uk CSP Spain III nodes (Dec 1527),
   HistoCrypt article 389, Venice cryptography press pieces. No decipherment of a 26 Oct letter.
4. `DECODE R9970 Simancas 1527 Galende cifras Andrea del Burgo Gattinara Fugger "al príncipe"` (descriptive title, with
   Bourdeau's reading of the images) -- BL Add MS Simancas-transcript records (searcharchives.bl.uk 040-002019988/9: del
   Burgo letters 1525-29, one of 3 Nov 1527), CSP Spain "November 1527, 1-20" (prod.british-history.ac.uk node 74585:
   HTTP 401 to WebFetch, not read), Estudios Románicos "Nápoles 1547" and "Ciphers of Joanna of Austria". No page on R9970.
Blog site searches:
5. Cipherbrain (`site:scienceblogs.de klausis-krypto-kolumne Simancas 1527 Gattinara`): no scienceblogs.de page returned.
6. Cryptiana (`site:cryptiana.blogspot.com Simancas Charles V cipher 1527`): no cryptiana.blogspot.com page; results were
   the Estudios Románicos series, the Granada cipher museum page on Philip II's Cifra General, and an Oviedo thesis record
   "Construcción, uso y descifrado de los lenguajes secretos en el siglo XVI" (Charles V's ciphers 1521-27; not opened).
7. Cipher Mysteries (`site:ciphermysteries.com Simancas cipher Charles V Gattinara`): no ciphermysteries.com page; LORIA's
   "Charles V's encrypted letter" (1547 letter, a different item) and the same academic set.
No decipherment or plaintext of the 26 Oct 1527 letter found in any post or comment thread. Requests: WebSearch 7,
prod.british-history.ac.uk 1 (401, not retried), archive.org 1 (advancedsearch) + be-api.us.archive.org 6.

## Premise check (GF-A2B-1, 3 Oct 2026)

(a) Folder's own mentions -- found: the "Solver-repo check (bourdeau, 2 Oct 2026)" section above already records
Bourdeau's verdict that R9970's images are not a cipher; DocumentsList "No records found".
(b) Other solvers' working files -- **found, decisive for the images**: dbourdeau/cyphersolver (shallow clone, HEAD
e8b4287, 2 Oct 2026) `targets/burgo1527/NOTES.md` and `reading_evidence.md` (28 Sept 2026): the four DECODE R9970
images are two revised drafts of a clear Spanish minute headed "al principe" -- Charles V to Prince Philip about an
exchange (*cambio*) of 110,770 ducats ("CX U DCC LXX") with "Antonio Fucar" (Anton Fugger), datable 1543-1554 since
Philip was born in May 1527; "No cipher anywhere on the four surfaces"; the Roman-numeral sum and the U thousands
sign explain DECODE's "graphic signs, numerical" tags. The del Burgo-Gattinara letter of 26 Oct 1527 (DECODE's
description, after Galende 1994 p. 163) is not on these scans and was not located by him (PARES leg. 1563 not
itemised). Bourdeau's catalogue entry 198 is removed and a DECODE correction queued. Read here, not copied (MIT/CC BY
4.0, credited). aaymeloglu/unsolved-ciphers (HEAD d2800bb, 27 Sept): R9970 only in the catalogue harvest (cited, not
copied).
(c) Physical neighbours -- not viewed: the R9970 images were not fetched this pass (no DECODE login); Bourdeau's
reading of all four surfaces stands unchecked by this repo. Leg. 1563's neighbouring folios are not itemised online.
(d) Recipient-side editions -- partly: CSP Spanish III pt 2 (the calendar of Simancas Estado for 1527) calendars del
Burgo's Ferrara letters of 4, 18 and 24 Oct 1527 with "(Cipher:)" passages (status-line citation), none dated
26 Oct; the BL's Simancas transcripts (Add MS records 040-002019988/9) list del Burgo letters 1525-29. Gattinara's
own papers (Bornate's edition of his autobiography/documents) not searched.
Consequence (for the orchestrator, not changed here): the item as imaged in DECODE carries no cipher on Bourdeau's
reading; the 1527 letter it is meant to represent is unlocated. ROOM flag sent to the account-3 orchestrator.

## While waiting

Next action that depends on nobody: one DECODE browser login to fetch R9970's four images and confirm or refute
Bourdeau's "al principe / Antonio Fucar" reading by eye (a one-page check, no cryptanalysis); if confirmed, the
target is a catalogue correction and the 26 Oct 1527 letter is a separate search (Galende 1994 p. 163's source).

## CS-BATCH4 pass (3 Oct 2026)

No new source opened (no DECODE login, no images, per brief). Re-read the folder against the intake gate (python3 tools/intake_gate_check.py decode-9970-simancas-1527: "open (line 3) -- edition/page or full-text-search citation found within 6 lines", exit 0). Standing reading of the Premise check stays: Bourdeau (28 Sept 2026) reads the four R9970 images as a clear Spanish minute, not the del Burgo letter; this repo has not viewed them. Status stays `open`; next step is the one-login image check in "While waiting" (~USD 1), after which the folder is a catalogue correction rather than a cipher target if Bourdeau's reading holds.

## Image check (IMG-DECODE1, account 2 worker for LANE-IMAGES, 3 Oct 2026)

Route that worked: one headless-browser login, `tools/decode_browser_login.js 9970 <scratch> --guess-fullsize --fetch-page
https://de-crypt.org/decrypt-web/ImagesList?showmaster=records&fk_id=9970` (shared with two other targets through `--listen`).
RecordsView/9970: name AGS_EST_LEG_1563; AGS Estado leg. 1563 fol. 572; date 1527; author Andrea del Burgo; receiver Chancellor
Gattinara; Ferrara; Type Cipher, Non-decrypted, Cipher Type Unknown, symbol sets Graphic signs/Alphabet/Numerical; 4 pages,
0 documents. **All four full-size images are served** (1951-1992 x 2803-2812 px, real JPEGs, none is forbidden.png); sha1s and
URLs in `images/manifest.json`. Not committed: the record says "The image is not in the public domain. Publishing it is only
possible with the permission of the Library."

Image-type check (one vision call on a contact sheet of all four pages, about 740 px wide each; no transcription, nothing graded):
- Every written surface is Spanish cursive in clear, with deletions and interlinear revisions. **No cipher sign seen on any page.**
- The archive's own frame captions give the order: DECODE P2 = AGS image _0001 (stamped "E. 1563 - 572"), P3 = _0002, P1 = _0003,
  P4 = _0004.
- P2 and P3 each have the marginal heading "al principe" (as Bourdeau reads it) and each open "demas de los cambios ..."; so
  these are two drafts of the same minute, consistent with Bourdeau's "two revised drafts".
- P2's fifth line has a Roman-numeral sum with the U thousands sign ("c x U dcc lxx" at this size), consistent with his 110,770 ducats.
- P1 has a short continuation (ten lines). P4 is almost blank, with only a trace of a short endorsement.
- "Antonio Fucar" could not be made out at contact-sheet resolution. It is neither confirmed nor refuted here.
Result: the four DECODE images of R9970 are a clear Spanish minute headed "al principe", not a cipher letter, as Bourdeau
(cyphersolver, targets/burgo1527, 28 Sept 2026) reported. The 26 Oct 1527 del Burgo-to-Gattinara letter is not on these scans.
Where it is remains unlocated (Galende 1994 p. 163's source).

Requests: de-crypt.org 12 for this target (login flow 2, RecordsView 1, ImagesList 1, 4 thumbnails, 4 full-size), 1.5-1.7 s
apart, no challenge. Shared job total: about 39 de-crypt.org requests. Vision calls: 1 for this target (3 in the job).

## While waiting (updated 3 Oct 2026, IMG-DECODE1)

[done 3 Oct 2026, IMG-DECODE1] The image blocker is cleared: R9970's four images were fetched and checked by eye, and they carry
no cipher (section above). [done 6 Oct 2026, D22-FTS: Galende 1994 p.163 gives only the same AGS leg. 1563 fol. 572 citation, see the D22-FTS section] Next action that depends on nobody: report the catalogue mismatch to the orchestrator. The target as
imaged is a catalogue correction, and the 1527 letter is a separate search. Two things remain: a search for the letter's own
location (Galende 1994 p. 163, Simancas Estado leg. 1563 neighbouring folios via PARES when reachable), and a read of
"Antonio Fucar" at full size if a later worker needs the date.

## While waiting (RUN4-WAITBF, 4 Oct 2026)

- Action that depends on nobody: locate the 1527 letter itself -- read Galende 1994 p.163 (on disk in a dbourdeau/cyphersolver clone, esp318/lit/galende1994.txt) for its Simancas Estado leg. 1563 citation, then grep Aymeloglu's cached PARES sweep (catalogue/pares-*.jsonl; PARES itself is dead from the cloud) for the neighbouring folios; ~$1 (estimate). The image blocker is already cleared (IMG-DECODE1).

## D22-FTS (6 Oct 2026)

Item 5 of D22-FTS (Sonnet worker, 6 Oct 2026). Shallow clone of dbourdeau/cyphersolver (MIT / CC BY 4.0; credited) in the scratchpad (1 request, github.com); the file is `targets/esp318/lit/galende1994.txt` (the brief's `esp318/lit/` path sits under `targets/`); only that file was read (latin-1 text, page marker 163 at line 254).
Galende Díaz, J. Carlos (1994), documentation list, entry: "Carta del 26 de octubre de 1527 de Andrea del Burgo al canciller Gattinara desde Ferrara (A. G. S., sec. Estado, leg. 1563, fol. 572)." It stands in a dated list of letters from AGS Estado and B.R.A.H. holdings, among entries for Lope de Soria and Gattinara; the page's footnote 6 says a study of "esta documentación y sus claves" is published in *Hispania* LII/181, pp. 493-520 (it names BRAH sign. 9/1951-9/1954 there). So Galende p.163 supplies the Simancas citation DECODE R9970 already carries (leg. 1563, fol. 572, 26 Oct 1527, del Burgo to Gattinara, Ferrara) and no more: it does not say the letter is ciphered and does not print its text. Neighbouring-folio check not done (PARES dead from the cloud; Aymeloglu's catalogue/pares-*.jsonl not grepped this pass). Lead: *Hispania* LII (181), pp. 493-520, for the keys of that correspondence.
Result: the letter's location is the same shelfmark as the DECODE record; no neighbouring folios identified. Not a novelty verdict. Requests: github.com 1.
