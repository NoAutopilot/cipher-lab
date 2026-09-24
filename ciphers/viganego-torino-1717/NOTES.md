# viganego-torino-1717

Status: open

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
