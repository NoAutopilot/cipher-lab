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
