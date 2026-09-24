# decode-1162-modena-ambung-1492

Status: open

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
