# ra-morner-welin

Status: open

## What this is

Anonymous, unsigned, enciphered private letters, "Welin" to "Östergren", among the incoming private letters of
Count Adolf Göran Mörner and his wife. Riksarkivet i Stockholm/Täby, Esplunda arkiv, "Excellensen greve Adolf
Göran Mörners och hans makas handlingar / Inkommande brev", reference code `SE/RA/720290/I/12/2/153`. Catalogue
note (verbatim, from the Riksarkivet Sök-API): "Brev från privatpersoner: Welin - Östergren, brev i chiffer och
icke undertecknade." No date is given at catalogue level. QUEUE.md row R5 (section "Dutch and Nordic archive
candidates", LANE S scout of 24 Sept 2026).

No transcription exists anywhere the searches below reached; `ciphertext.txt` is not created (CLAUDE.md rule 2:
never invent a transcription).

## Check-solved sweep, 24 September 2026

Six sources, run directly (not via the Workflow tool, per this lane's brief), blind to each other only in the
sense that each was a separate query pass; reconciled here by one worker.

1. **Web.** WebSearch `"Mörner Welin Östergren chiffer brev Riksarkivet Esplunda"`. Hits: Adolph G. Mörner's and
   Carl Mörner's Svenskt Biografiskt Lexikon entries (biography only, no mention of this correspondence), the
   Esplunda arkiv finding-aid page, and Wikipedia's Axel Otto Mörner page (a different Mörner). No hit names
   "Welin", "Östergren" or this specific bundle of letters. Not found.
2. **Print.** No sender or recipient identity is established for either "Welin" or "Östergren" — the catalogue
   note itself flags them as unsigned and anonymous, so there is no named correspondent whose printed
   Correspondance/Lettres could be checked, and no calendar series covers unpublished Swedish private-archive
   incoming letters of this kind. Nothing to check against; recorded as inapplicable rather than blocked.
3. **Lists.** `sources/cryptiana/` grepped locally for `mörner|morner|welin|östergren|ostergren`: no hits.
   Cryptiana, Cipherbrain and Cipher Mysteries's live sites were not fetched separately (out of profile for
   this obscure, uncatalogued Swedish item; the local snapshot is the productive check per LESSONS.md and
   returned nothing).
4. **DECODE.** `sources/decode/` grepped locally for the same terms: no hits. Live de-crypt.org not queried
   (this lane's DECODE slot was spent on R9's Gripenstierna check instead, and nothing in the catalogue note
   points to a specific shelfmark DECODE would index under, since it has no date or key mentioned). Recorded as
   checked-against-cache-only, not blocked.
5. **Bourdeau.** Shallow clone `github.com/dbourdeau/cyphersolver` (fresh, this session). `grep -n -i` for
   `mörner|morner|welin|östergren|ostergren` against `README.md`, `TARGETS.md`, `SOLVED_CATALOGUE.md`: no
   matches. A broader repo-wide grep turned up only unrelated false positives (data files where "morner" etc.
   are substrings of unrelated tokens, none naming this item). Not found.
6. **Aymeloglu.** Shallow clone `github.com/aaymeloglu/unsolved-ciphers` (fresh, this session). Same grep
   against `README.md`, `TARGETS.md`, `SHORTLIST.md`, `CATALOGUE.md`: no matches. Not found.

**Riksarkivet digitisation check** (this lane's own slot, `data.riksarkivet.se/api/records`, one request,
`text=Welin Östergren`): confirms the single matching record, `SE/RA/720290/I/12/2/153`, with
`"onlyDigitisedMaterials":false`. Not digitised; no image exists online for this item.

## Verdict

**Open.** No source located a solution, key, plaintext, transcription or documented attempt on this item. It is
also, by its own catalogue description, the weakest-attested row in this batch: no date, no identified sender or
recipient (both names may be surnames of minor or untraceable private individuals), and the catalogue's own
caution about a possibly later (e.g. 19th-c. social/romantic) cipher rather than a diplomatic one, per QUEUE.md's
own next-move note. Establishing a date and hand would need the physical item.

Copy-order (not digitised). REQUEST.md below drafts the Riksarkivet reading-room request.

Requests this pass: data.riksarkivet.se 1 (this item; shared count with the other three targets in this
worker's ROOM claim, batch total below), github.com 2 shallow clones (grepped, kept for the other three
targets in this batch), WebSearch 1, no Google Books, no TNA, no DECODE login.
