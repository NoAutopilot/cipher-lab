# della-torre-olanda-1690

Status: open

## What this is

Cipher-book ("CIFRARIO al Conte e Presidente Della Torre") filed in the same mazzo as the decade of
correspondence (1690-1700) of Savoy envoy extraordinary Conte e Presidente Della Torre at the Hague, negotiating
Dutch subsidies for the League of Augsburg war against France. Archivio di Stato di Torino, "Lettere Ministri —
Carteggio diplomatico" (Inv. 151/B), Lettere Ministri Olanda, mazzo 2. Box also holds letters to/from Lord
Nottingham, Milord Monquille, Cav. Giuseppe Terne (London), Conte Caraffa, Prelà Doria and the Marchese di Prié
(Vienna). QUEUE.md row IR1 (section "Italian regional state archives, Mantua Modena Turin Genoa Naples", LANE N
scout IT3 of 24 Sept 2026); source PDF `LETTERE MINISTRI_Vol.II.pdf`, ASTo.

No image or transcription has been seen by anyone in this project; the box-level finding aid gives no item-level
content note beyond the cipher-book's title, so it is not established from the finding aid alone that any letter
in the mazzo is itself ciphertext rather than clear correspondence about the cipher's issue — only that the box
holds both a keybook and the envoy's own decade of letters (CLAUDE.md "Confirm the key and the letters are in the
same unit and that the letters are ciphered" — partially met: same unit confirmed, letters-are-ciphered not yet
confirmed without opening the box). `ciphertext.txt` is not created (rule 2: no invented transcription).

## Check-solved sweep, 24 September 2026

1. **Web.** WebSearch `"Della Torre" ambasciatore Aia Olanda cifra 1690 1700 Savoia` and `Della Torre inviato
   Savoia Olanda "Lettere Ministri" cifrario Torino archivio` and `"Della Torre" negoziato Aia 1690 sussidi guerra
   Lega Augusta Savoia carteggio pubblicato`. Hits: the ASTo inventory PDF itself, Wikipedia pages for unrelated
   Della Torre namesakes (Filippo, Oberto, Giovanni Maria, Leonardo — all different people/centuries), and general
   background on the War of the League of Augsburg and Vittorio Amedeo II. No hit names this envoy's cipher, this
   mazzo, or a printed decipherment. Not found.
2. **Print.** No printed Savoy diplomatic edition or "Biblioteca di storia italiana" volume for the Della Torre
   Hague mission located by WebSearch this pass (queried against opac.sbn.it and generally); Vittorio Amedeo II's
   published *Lettere e relazioni diplomatiche* series was not checked volume-by-volume (out of scope for one
   worker's budget) — recorded as not located, not as a confirmed absence at N3/N4 level. This is a check-solved
   pass, not a verifier's edition sweep.
3. **Lists.** `sources/cryptiana/` grepped locally for `della torre|dellatorre`: no hits.
4. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` (1187 rows) grepped for `della torre|olanda|
   torino`: no matching envoy/shelfmark. Live de-crypt.org not queried (this lane's rule: only the DECODE worker
   logs in).
5. **Bourdeau.** Fresh shallow clone `github.com/dbourdeau/cyphersolver`. `grep -ril "Della Torre"` across the
   whole tree: 3 hits, none this item — `buda1489/vestigia/search_rows.json` (unrelated search-index noise),
   `vatican5/lit/elio.txt` line 405 ("Dandino, Della Torre et Trivultio (1546-...)", a different, earlier Della
   Torre, papal nuncio context), `pallotto1629/ed/pallotto_bd2_1629.txt` (unrelated edition text). Not found.
6. **Aymeloglu.** Same clone/grep pass against `github.com/aaymeloglu/unsolved-ciphers`: 0 hits for "Della Torre".
   Not found.

## Verdict

**Open.** No source located a solution, key, plaintext or documented attempt for this item. Not yet confirmed
whether the mazzo's letters are themselves ciphered (finding-aid text alone does not say), and no printed Savoy
diplomatic edition has been checked page-by-page — both gate items for promotion past stage 2, left for the next
worker (access/print-check pass) rather than closed here.

Copy-order: no digitised image of ASTo Lettere Ministri Olanda mazzo 2 found this pass (the PDF is an inventory,
not a viewer). REQUEST.md below.

Requests this pass: WebSearch 3 (shared with general Turin/Della Torre queries), opac.sbn.it via WebSearch
`allowed_domains` 1, github.com 2 shallow clones (shared across all six IR targets, grepped, kept for reuse),
archiviodistatotorino.beniculturali.it 0 direct fetches this pass (inventory PDF already fetched and quoted by
the 24 Sept scout; not re-fetched). No SIAS, no Google Books, no DECODE login, no promotion, no decoding.
