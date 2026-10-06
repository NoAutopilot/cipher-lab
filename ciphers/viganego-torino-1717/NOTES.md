# viganego-torino-1717

Status: blocked

No printed edition of Viganego's 1717 Turin dispatches could be opened or identified by this worker, and the ASGe inventory PDF (31_Trattati_202008.pdf) did not open from this container (connection reset twice, 2 Oct 2026), so no edition or page was read. The 24 Sept 2026 sweep below stands as a negative search result only.

## What this is

Cipher and code-names issued to Genoese envoy abate Gio. Battista Viganego at Turin ("Cifrario e nomi dati a
Gio. Batta Viganego, inviato a Torino, per servirsene nella corrispondenza da inviare a Genova", 7 Apr 1717),
Archivio di Stato di Genova, Archivio segreto, Materie politiche (Trattati e negoziazioni, Inv. 31), item 249.
Items 246 (7 Apr 1717) and 254 (14 Apr 1717) in the same series, same weeks — "Notizie trasmesse da Torino
dall'abate Gio. Battista Viganego" — are plausible sibling ciphertext from the very correspondent the key was
issued to, in the same box. QUEUE.md row IR2 (LANE N scout IT3 of 24 Sept 2026); source PDF
`31_Trattati_202008.pdf`, ASGe.

Same-unit is confirmed (key and the two dispatch items are three consecutive/near items in the same inventory
volume). Whether items 246/254 are themselves ciphertext, versus a cover note about ciphered correspondence, is
not established from the finding-aid entries alone — the titles describe the dispatches' subject ("Notizie
trasmesse da Torino"), not their script. `ciphertext.txt` is not created.

## Check-solved sweep, 24 September 2026

1. **Web.** WebSearch `Viganego abate inviato Torino Genova 1717 cifra dispacci`. Hits: an unrelated Società
   Ligure di Storia Patria PDF ("Genova e Torino. Quattro secoli di incontri e scontri", no Viganego mention
   found), a Wikipedia Salvatore Viganò (different person, different era), a Chiesa di S. Siro in Viganego
   (place name, not this envoy). No hit names this envoy, mission or cipher. Not found.
2. **Print.** No printed edition of Genoese Archivio segreto diplomatic correspondence for this 1717 Turin
   mission located this pass (Atti della Società Ligure di Storia Patria checked by WebSearch for adjacent
   Genoa-Turin diplomatic material generally, no specific hit for Viganego). Not confirmed absent at
   verifier level, only not located by this worker.
3. **Lists.** `sources/cryptiana/` grepped locally for `viganego`: no hits.
4. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` grepped for `viganego|genova|torino`: no
   matching envoy/shelfmark (the "Torino"/"Genova" hits it does have, if any, were checked and are unrelated
   place-name substrings, not this item). Live de-crypt.org not queried.
5. **Bourdeau.** Fresh shallow clone `github.com/dbourdeau/cyphersolver`, `grep -ril "Viganego"`: 0 hits.
6. **Aymeloglu.** Same clone/grep pass against `github.com/aaymeloglu/unsolved-ciphers`: 0 hits.

## Verdict

**Open.** No source located a solution, key, plaintext or documented attempt for this item. The sibling-ciphertext
claim (items 246/254 being ciphered dispatches from Viganego, on the same key as item 249) is the finding aid's
juxtaposition, not a confirmed reading of either item's script — the next worker needs the images or a copy order
to confirm before this can move past stage 2 as a recovery target.

Copy-order: no digitised image of ASGe Materie politiche (Inv. 31) items 246/249/254 found this pass. REQUEST.md
below.

Requests this pass: WebSearch 1, github.com 0 (reused the shared clone from della-torre-olanda-1690, same
session). No SIAS, no Google Books, no DECODE login, no promotion, no decoding.

## Web and blog check (CS-A2-B, 2 Oct 2026)

WebSearch (standard) on the envoy/secretary, place, year and "cifra/cifrario" in Italian (see below per target); results were the holding archives' own inventory PDFs, unrelated namesakes and general background, none naming a decipherment. Cryptiana blog, Cipherbrain and Cipher Mysteries: the Waldegrave-run site searches the same day (same three hosts) cover only that name; for this target the three blogs were searched through WebSearch and `sources/cryptiana/` only, no post found, comment threads not separately opened. DECODE: login-free `tools/decode_list.py --status non-decrypted` crawl of 2 Oct 2026 (801 rows): 0 rows matching viganego|genova|torino for this item (the 54 "Hague/Aia" matches in the crawl are Dutch royal-archive items of 1789-1804, not this mazzo). Solver repos, shallow clones grepped 2 Oct 2026: dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers: no hit for this item (only namesake or place-name noise). Unreachable this pass: archiviodistatogenova.cultura.gov.it and archiviodistatotorino.beniculturali.it (curl, connection reset, one retry), so the holding finding aid was not re-opened.

## Premise check (CS-A2-B, 2 Oct 2026)

(a) Folder's own NOTES.md/REQUEST.md: no decipherment, gloss, clear copy or attachment mentioned. Not found. (b) Solver working files: no file for this item in either repository. Not found. (c) Physical neighbours / facing page: no image exists or was reachable (copy-order). Unreachable. (d) Recipient-side editions: not located by this worker's searches. Not found (not an edition read).

Hosts this pass: de-crypt.org 17 (no login, shared run), github.com 2 clones (shared), archiviodistatogenova/torino 2 attempts each failed, WebSearch 1 for this target.

## Re-check (CS-BATCH5, 3 Oct 2026)

WebSearch (standard) `Viganego abate inviato Genova Torino 1717 cifrario Archivio segreto Materie politiche`: hits were the ASGe inventory PDFs (31_Trattati_202008.pdf, 34_ArchivioSegreto202003.pdf, listed only, not opened: ASGe host reset twice on 2 Oct and not retried here), memoriedigitaliliguri.it (an extract PDF, not opened) and unrelated cipher papers; none names Viganego, the mission or a cipher. No printed edition of these dispatches was located or opened by this worker, so the status stays `blocked`. Premise check (a)-(d) as of CS-A2-B (2 Oct 2026) still stands; nothing new in (a)-(c); (d) recipient-side (Savoy/Turin) edition: not located.

## Retry and extract read (A2P4-VIG, 3 Oct 2026, 17:37-17:50 UTC)

Hosts: archiviodistatogenova.cultura.gov.it 1 request (the single retry of 31_Trattati_202008.pdf: HTTP 200, 826,146 bytes, opened and read with pdftotext, 647,549 characters; the 2 Oct connection resets did not recur); memoriedigitaliliguri.it 6 requests (the six PDFs the 3 Oct search returned, one fetch each, 2 s apart, pdftotext); WebSearch 1. No vision calls, no login, no email.

- **ASGe inventory n. 31 (Piscioneri regesti, Archivio segreto, Materie politiche bb. 2748-2757), read:** item 249 "Cifrario e nomi dati a Gio. Batta Viganego, inviato a Torino, per servirsene nella corrispondenza da inviare a Genova", Apr 1717 (day blank); 246 "Notizie trasmesse da Torino dall'abate Gio. Battista Viganego", 7 Apr 1717; 254 "Notizie da Torino trasmesse dal Viganego", 14 Apr 1717. The regesti name no script, no cipher on 246/254 and no folio count, and the busta number for these items did not print in the text. More Viganego items in the same series (not in the brief, listed only): 242 (22 Mar 1717, from Cherasco, "Giovanni Viganego", corte di Torino), 273 (21 Apr, troop movements), 307 (26 May), 312 (9 Jun), 320 (16 Jul, "Rapporto di quanto ha potuto fare e sapere Gio. Battista Viganego durante la permanenza in Torino"). Whether any is ciphered is not stated. Other cipher items in the inventory (229, 237, 294, 299) are different persons and years.
- **memoriedigitaliliguri.it, 6 PDFs, grepped viganego|cifr|1717:** the first (Giornale Ligustico, "A. N.") mentions a Viganego writing in 1756, a different man and year. The other five (Atti SLSP n.s. vol. I; an introduction; Quaderni SLSP 2, "Genova e Torino", whose one "decifrati" is a figure of speech; Giornale storico e letterario della Liguria; Radiose giornate genovesi 1746) have no Viganego, no cipher of 1717 and no reference to this mission. None of the six names the 1717 envoy, key or a printed edition of these dispatches. Not found in these six (search result, not a novelty verdict).
- **Effect:** the "ASGe PDF did not open" blocker is lifted; the gap that remains is the images or a copy of 246/249/254, which no source here provides. Status stays `blocked` (no image or print of the items exists to read), reason now only needs-physical-access / copy order.

## Next step (costed)

Send the existing REQUEST.md (ASGe items 246, 249, 254; the regesti above confirm the item numbers and titles) to ASGe; ~USD 0 agent cost, owner-side email, then ~USD 3 for a first transcription batch if the images come. The cheaper PDF retry is spent. Verdict: parked (blocked on the copy order, ASGe reply).

## While waiting

- Ask ASGe (in the same message) whether Viganego's later reports (items 242, 273, 307, 312, 320) are in clear or in the 249 cipher; depends on nobody to draft, needs the reply to act.
- The memoriedigitaliliguri.it extract read is done (above, nothing found).

## Next step (R13-STALE, 6 Oct 2026)

Next step: send REQUEST.md to ASGe (items 246, 249, 254, with the question on 242/273/307/312/320 from "While waiting") -- an owner-side email,
needs the owner; no outreach draft or ASKS row for it was found on 6 Oct 2026, so the lane orchestrator drafts one in outreach/ and files the
row. Agent cost ~USD 0 until the images come, then ~USD 3 for a first transcription batch. The online steps (inventory PDF, memoriedigitaliliguri
extracts) are done (A2P4-VIG, 3 Oct). Status stays `blocked`. Housekeeping line, R13-STALE (account 4): no work run.
