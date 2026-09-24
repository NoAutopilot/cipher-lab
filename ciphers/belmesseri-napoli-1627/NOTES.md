# belmesseri-napoli-1627

Status: open

## What this is

Cipher attached to Este envoy Angelo Belmesseri's Naples dispatches on the Stigliano marriage negotiation, 16
May 1627 – Jan 1628. Archivio Segreto Estense, Cancelleria, Carteggio ambasciatori — Napoli, b.20 fasc.1
(shelfmark given directly by the finding aid). Finding-aid note (verbatim): "Evvi congiunta una cifra" ("there
is attached a cipher"), on a nine-month run of dispatches about negotiating a marriage between the prince and
princess of Stigliano. The same run's earlier fascicle, b.19, carries an unciphered mission by the same envoy,
so the finding aid itself localises the cipher use to b.20 fasc.1 specifically. QUEUE.md row IR3 (LANE N scout
IT3 of 24 Sept 2026); source PDF `ASE_Cancelleria_ambasciatori_napoli.pdf`, ASMo/Este archive.

Same-unit and ciphered-letters are both stated directly by the finding aid's own wording ("evvi congiunta" = a
cipher is attached to this fascicle), the strongest form of confirmation available from a text-only source —
still short of having seen the item itself. `ciphertext.txt` is not created.

## Check-solved sweep, 24 September 2026

1. **Web.** WebSearch `"Belmesseri" OR "Belmessieri" Napoli Stigliano matrimonio ambasciatore estense 1627`.
   Hits: Treccani entries for Marzio Mastrilli and unrelated figures, a 21st-century Parma family news item
   (different "Belmessieri"), Tommaso Stigliani (poet, different spelling/person), general Stigliano/Colonna
   pages. No hit names this envoy, negotiation or cipher. Not found.
2. **Print.** No printed Este diplomatic edition for the Naples 1627-28 Stigliano marriage negotiation located
   this pass (Venturi/Balan/Pastor appendices and the "Carteggio degli oratori" series not checked
   volume-by-volume — out of one worker's budget). Not confirmed absent at verifier level.
3. **Lists.** `sources/cryptiana/` grepped locally for `belmesseri|belmessieri|stigliano`: no hits.
4. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` grepped for `belmesseri|napoli|stigliano`:
   the file's "Modena" rows are all Ambasciatori Ungheria (Ferrara envoy reports, 1482-1504, boxes Amb. Ung.
   b.2/... and Carteggio Principi Esteri) — a different fondo and box entirely from Carteggio ambasciatori
   Napoli b.20; no row matches this envoy or shelfmark. Live de-crypt.org not queried.
5. **Bourdeau.** Fresh shallow clone `github.com/dbourdeau/cyphersolver`, `grep -ril "Belmesseri"`: 0 hits.
6. **Aymeloglu.** Same clone/grep pass against `github.com/aaymeloglu/unsolved-ciphers`: 0 hits.

## Verdict

**Open.** No source located a solution, key, plaintext or documented attempt for this item. "Evvi congiunta una
cifra" is ambiguous by itself between "a cipher key is attached" (the IR1/IR2/IR4/IR5 recovery pattern) and "a
ciphered letter is included" (cryptanalysis) — Italian archival usage of "cifra" covers both the table and the
enciphered text, and the finding aid does not disambiguate. Kept as recovery per the scout's row pending
inspection; a worker who opens the fascicle should confirm which reading is right before any solver attempt.

Copy-order: no digitised image of ASMo Carteggio ambasciatori Napoli b.20 fasc.1 found this pass. REQUEST.md
below.

Requests this pass: WebSearch 1, github.com 0 (reused shared clone). No SIAS, no Google Books, no DECODE login,
no promotion, no decoding.
