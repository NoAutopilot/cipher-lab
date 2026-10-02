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
