# salvago-caraffa-1691

Status: blocked

No printed Genoese edition for the 1691 Caraffa affair could be opened or identified by this worker, and the ASGe inventory PDF (31_Trattati_202008.pdf) did not open from this container (connection reset twice, 2 Oct 2026), so no edition or page was read. The 24 Sept 2026 sweep below stands as a negative search result only.

## What this is

Cipher issued to Genoese secretary Salvago for his 1691 mission to Imperial Count Caraffa ("Cifra per il
segretario Salvago data nel tempo che si portò in Alessandria dal conte Caraffa"), Archivio di Stato di Genova,
Archivio segreto, Materie politiche (Inv. 31), item 294, in the run items 288-299. Items 288-298 (same year)
cover payments to Caraffa's imperial troops then present in Italy during the Nine Years' War; item 299
paraphrases in some detail a cipher advising Italian princes to ally against Caraffa's demands (excluded from
this batch as a possible edition risk — the catalogue entry itself may already summarise its content). QUEUE.md
row IR4 (LANE N scout IT3 of 24 Sept 2026); source PDF `31_Trattati_202008.pdf`, ASGe.

Same-unit is confirmed; whether any surrounding item (288-298) is itself ciphertext in Salvago's key, versus
plain correspondence about the Caraffa affair, is not established from the finding aid alone. `ciphertext.txt`
is not created.

## Check-solved sweep, 24 September 2026

1. **Web.** WebSearch `"Salvago" segretario Genova Caraffa 1691 Alessandria sussidio truppe imperiali` and
   `"Atti della Società Ligure di Storia Patria" Caraffa sussidi 1691 Genova carteggio`. Hits: background on
   Antonio Carafa's 1691 command of imperial troops in Italy, his extortionate subsidy demands and April 1692
   recall to Vienna (confirms the archive item's historical context, from Wikipedia, not from any edition
   naming this cipher); unrelated Salvago-family genealogy and Almadén-mines articles; the Atti della Società
   Ligure digital library's general catalogue pages, no specific article surfaced for this item. No hit names
   this cipher, envoy or a decipherment. Not found.
2. **Print.** No printed Genoese diplomatic edition for the 1691 Caraffa affair located this pass (Atti della
   Società Ligure di Storia Patria not searched article-by-article — out of one worker's budget). Not confirmed
   absent at verifier level.
3. **Lists.** `sources/cryptiana/` grepped locally for `salvago`: no hits.
4. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` grepped for `salvago|caraffa|genova`: no
   matching envoy/shelfmark. Live de-crypt.org not queried.
5. **Bourdeau.** Fresh shallow clone `github.com/dbourdeau/cyphersolver`, `grep -ril "Salvago"`: 1 hit,
   `buda1489/vestigia/search_rows.json` line ~39347, "Gabriele Salvago, Gian Vincenzo Pinelli" — a different
   Salvago (a 16th-century correspondent of Pinelli, unrelated to this 1691 Genoese secretary) in an unrelated
   target folder (buda1489). Checked by name and date, ruled out as a collision. Not found.
6. **Aymeloglu.** Fresh shallow clone `github.com/aaymeloglu/unsolved-ciphers`, `grep -ril "Salvago"`: 0 hits.

## Verdict

**Open.** No source located a solution, key, plaintext or documented attempt for this item. Lower confidence than
IR1/IR2 in the same batch: the finding aid gives no explicit sibling-ciphertext item the way IR2's items
246/254 do (only a shared subject-matter run, items 288-298), so the "key opens a specific letter" claim is
weaker here and needs the images to confirm.

Copy-order: no digitised image of ASGe Materie politiche (Inv. 31) item 294 (or its neighbours) found this pass.
REQUEST.md below.

Requests this pass: WebSearch 2, github.com 0 (reused shared clones). No SIAS, no Google Books, no DECODE login,
no promotion, no decoding.

## Web and blog check (CS-A2-B, 2 Oct 2026)

WebSearch (standard) on the envoy/secretary, place, year and "cifra/cifrario" in Italian (see below per target); results were the holding archives' own inventory PDFs, unrelated namesakes and general background, none naming a decipherment. Cryptiana blog, Cipherbrain and Cipher Mysteries: the Waldegrave-run site searches the same day (same three hosts) cover only that name; for this target the three blogs were searched through WebSearch and `sources/cryptiana/` only, no post found, comment threads not separately opened. DECODE: login-free `tools/decode_list.py --status non-decrypted` crawl of 2 Oct 2026 (801 rows): 0 rows matching salvago|caraffa|carafa for this item (the 54 "Hague/Aia" matches in the crawl are Dutch royal-archive items of 1789-1804, not this mazzo). Solver repos, shallow clones grepped 2 Oct 2026: dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers: no hit for this item (only namesake or place-name noise). Unreachable this pass: archiviodistatogenova.cultura.gov.it and archiviodistatotorino.beniculturali.it (curl, connection reset, one retry), so the holding finding aid was not re-opened.

## Premise check (CS-A2-B, 2 Oct 2026)

(a) Folder's own NOTES.md/REQUEST.md: no decipherment, gloss, clear copy or attachment mentioned. Not found. (b) Solver working files: no file for this item in either repository. Not found. (c) Physical neighbours / facing page: no image exists or was reachable (copy-order). Unreachable. (d) Recipient-side editions: not located by this worker's searches. Not found (not an edition read).

Hosts this pass: de-crypt.org 17 (no login, shared run), github.com 2 clones (shared), archiviodistatogenova/torino 2 attempts each failed, WebSearch 1 for this target.

## CS-BATCH4 pass (3 Oct 2026, 15:3x-15:4x UTC)

- Holding finding aid opened this time: ASGe Archivio segreto, Materie politiche, inventory 31, at `archiviodistatogenova.cultura.gov.it/fileadmin/risorse/pdf/31_Trattati_202008.pdf` (the earlier root-path URL 404s; this one answers HTTP 200, 826 KB, one request). Read: items 292-300 (1691): 293 "Per il pagamento della missione in Alessandria del segretario Salvago" (28 Dec 1691); **294 "Cifra per il segretario Salvago data nel tempo che si portò in Alessandria dal conte Caraffa" (1691)**; 295 draft letter from the secretary to Durazzo, Imperiale and the governor of Savona; 296-298 Caraffa's subsistence demand and the Republic's justification; 299 "Cifra con cui il signor di Coysis consiglia i principi italiani ad allearsi contro le pretese esagerate del conte Caraffa". Also Archivio segreto b. 2756, "Vienna e Impero. Negoziazioni relative al Gen.le Caraffa" (1691), a separate busta of notes and reports. Both ciphers (294, 299) are listed as items, but the aid gives no content, no ciphertext marker and no availability flag. Grade I for any claim that a ciphered letter sits beside item 294.
- Edition: Carutti vol. 3 (IA `carutti-...-v-3`, whole-volume djvu grepped for "Salvago": 0 hits; Caraffa's 1691 campaign is narrated, nothing on a Genoese cipher). No printed Genoese edition of this affair identified. Not found.

Intake gate (python3 tools/intake_gate_check.py salvago-caraffa-1691): "blocked (line 3) -- already terminal, nothing to gate", exit 0.

Verdict: stays `blocked` (finding aid read, no edition or image exists to open). Next: ASGe copy enquiry of REQUEST.md for items 294 and 299 (owner-side), or a Società Ligure di Storia Patria article-level search (~USD 1.5).

## A2P4-SALV pass (3 Oct 2026, 18:14-18:32 UTC): Atti della Societa Ligure di Storia Patria, full-text

Route: Internet Archive advancedsearch listed 31 Atti volumes (UofT scans vols 3-48, Cavagna-era scans vols 1-25 and 71-72, 1885 vol., vol. 49 f.1-2, a Google scan; one non-Atti Castelnuovo book also queried); `be-api.us.archive.org/fts/v1/search`, quoted term + `identifier=`, one volume at a time, 1.6 s apart. Terms: "Coysis", "Caraffa", "Salvago". Requests: archive.org advancedsearch 1, be-api 96 (32 ids x 3 terms), memoriedigitaliliguri.it root 1 (200; its own search not used, Atti vols after about 49 are not in this IA set).
Positive control: "Salvago" reproduces in 19 of 32 volumes (the family is common in the Atti), so the search reads the OCR. This control shows the route works for the family name, not that a 1691 Caraffa passage would be found.
Result: "Coysis" 0 of 32. "Caraffa" hits in 5 volumes (13-24 combined, 10, 38, 8, 9 of the Cavagna/UofT scans), each a snippet on 16th-century Carafa (Tommaso, Alfonso, Paolo IV, Livia Doria-Caraffa, Ferrante) or an index entry; none concerns Antonio Carafa, the 1691 subsidy or a cipher. Only snippet hits were read (fts returns snippets, no page locators), so a Salvago snippet in a volume was not opened to rule out a 1691 mention. Not found in these volumes.
Not covered: Atti volumes absent from this IA set (later 20th-century volumes, in copyright), Giornale Ligustico, and any article that prints item 299's cipher under another spelling of the name (Coysis/Coisis/Coissy not tried). Grade I for any claim about what the Atti hold.
Status unchanged: `blocked`. Intake gate unchanged (terminal status, exit 0).

## While waiting

One action that depends on nobody: full-text search of Atti della Società Ligure di Storia Patria (memoriedigitaliliguri.it) for "Caraffa" 1691 and "Coysis", to see whether item 299's cipher was printed; ~USD 1.

Update 3 Oct 2026 (A2P4-SALV): the Atti search above was run (0 for Coysis, Carafa hits all 16th-century). Next: ASGe copy enquiry (REQUEST.md, owner-side), or retry with spelling variants Coisis/Coissy in the same 31 volumes plus Giornale Ligustico (~USD 0.5).

## R8-SPS2 (b) pass (6 Oct 2026, 04:30-04:36 UTC): spelling variants in the Atti set
Route as the A2P4-SALV pass: IA advancedsearch (31 Atti ids) then be-api fts, quoted term + identifier, 1.6 s apart. Terms "Coisis", "Coissy", "Coysis", control "Salvago". Requests: archive.org 1, be-api 124.
Result: Coisis 0 of 31 (1 request errored, not retried), Coissy 0 of 31, Coysis 0 of 31. Control "Salvago": 22 of 31 volumes, so the OCR is read. Not found in these volumes; snippets only, no page locators. Giornale Ligustico and memoriedigitaliliguri.it's own search not used. Grade I for any claim about the Atti. Status unchanged: `blocked`.
