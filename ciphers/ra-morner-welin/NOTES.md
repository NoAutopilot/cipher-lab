# ra-morner-welin

Status: open
No standard edition exists for anonymous, unsigned letters; Google Books API full-text search by this worker (GF-A2B-2, 3 Oct 2026) for Welin/Östergren/Mörner/Esplunda + chiffer: 0 hits naming a cipher; one hit is the printed Esplunda inventory (Riksarkivet Meddelande, Google Books Kok4AAAAIAAJ), snippet "( Welin - Östergren ) 154 Brev i folioformat" (see Premise check).

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

## Web and blog check (GF-A2B-2, 3 Oct 2026)

Plain web searches (WebSearch, standard):
1. `Mörner Welin Östergren brev i chiffer` (sender + recipient as catalogued; no date exists): Scandia article
   (postal espionage), Stockholm University news on historical cryptology, the Heusner 1637 paper, a Jan Östergren
   book record -- none about this bundle.
2. `"SE/RA/720290" Esplunda Mörner chiffer` (shelfmark + cipher): a Riksarkivet arkis2dok PDF (Herrborum), Codex
   Esplunda, Mörner biographies -- no hit on the item.
3. `Adolf Göran Mörner Esplunda arkiv inkommande brev chiffer Welin` (folder title; no clear-text phrase exists):
   Birger Mörner, Runeberg, museum objects (one a music-score cipher, unrelated) -- no hit.
4. `Swedish enciphered letters Mörner Riksarkivet cipher unsigned Welin Östergren`: Uppsala S:t Barthélemy
   collection volumes (Mörner-family letters, 1815), the UiO/ScienceNorway piece on AI-decoded letters, Heusner --
   none names Welin/Östergren or Esplunda.
5. Google Books API, 4 queries (status line): only the printed Esplunda inventory and a Norwegian order register.

Blog site searches:
- Cipherbrain + Cryptiana + Cipher Mysteries (combined domain filter, "Mörner Welin Östergren Esplunda chiffer"):
  only unrelated scienceblogs.de pages (a Nils-Axel Mörner climate post, Notizblock murderer) -- nothing on this item.
- Cipherbrain alone: "Schwedische Literatur-Wissenschaftlerin sucht Unterstützung beim Knacken einer Verschlüsselung"
  (2015-04-03), opened with its comment thread: Clas Livijn's almanacs of 1800 and 1803 (Stockholm University),
  read in the comments by "Kent"; no mention of Mörner, Welin, Östergren or Esplunda. Unrelated.
- Cryptiana: no page returned on these terms (the combined search; the local snapshot grep of 24 Sept also empty).

No plausible hit for this item. Requests: WebSearch 5 + 1 shared, Google Books API 4, scienceblogs.de 1.

## Premise check (GF-A2B-2, 3 Oct 2026)

- (a) Folder's own mentions: no decipherment, gloss, key or clear copy is mentioned in NOTES.md or REQUEST.md; no
  spec. One premise is in doubt: the printed Esplunda inventory's snippet lists neighbouring volumes as
  "D:o (Mörner, Carl Gabriel) 1794-1820", "1821-28" and then "( Welin - Östergren ) 154 Brev i folioformat", the
  form of an alphabetical range of correspondents. "Welin - Östergren" is therefore probably the surname range W-Ö of
  the private-person letters in volume 153, not a sender "Welin" writing to a recipient "Östergren" as this folder's
  description reads it (inferred from one snippet; the inventory page itself not read). Not a decipherment; noted
  for whoever orders the copy.
- (b) Other solvers' working files: fresh shallow clones 3 Oct 2026 (Bourdeau e8b4287, Aymeloglu d2800bb),
  `grep -rliwE "m[öo]rner|welin|[öo]stergren|esplunda"`: zero files in either. Not found.
- (c) Physical neighbours: not digitised (Sök-API `onlyDigitisedMaterials: false`, 24 Sept 2026). Unreachable.
- (d) Recipient side: the recipient is Count Adolf Göran Mörner (1773-1838) or his wife; no printed edition of their
  incoming letters was found (web searches 3-4, Google Books). Not found.

## While waiting

Waiting on a copy order (REQUEST.md). The one action that depends on nobody: read the printed Esplunda inventory
(Google Books Kok4AAAAIAAJ, Riksarkivet Meddelande) around volume 153 through further Books API snippet queries, to
settle whether "Welin - Östergren" is a surname range and whether any other volume notes cipher letters or a key.

## Next step (NO-CRACKS, 5 Oct 2026)

next: read the printed Esplunda inventory (Google Books Kok4AAAAIAAJ) around volume 153 through Books API snippet queries, to settle whether "Welin - Ostergren" is a surname range and whether any other volume notes cipher letters or a key, ~$0.5; the copy order stays in REQUEST.md. Who acts: agent. Source: this file's "## While waiting"; written by NO-CRACKS (account 3) because tools/next_steps.py found no next-step line in this file.
