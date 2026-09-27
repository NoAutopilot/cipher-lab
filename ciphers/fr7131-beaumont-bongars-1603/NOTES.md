# BnF fr.7131, f.256 -- Christophe de Harlay, comte de Beaumont, to Jacques Bongars, 8 February 1603

found-solved

Tomokiyo, `bongars.htm` (`sources/cryptiana/web/bongars.htm`, local mirror), read in full by this worker: the
no.16/no.24 cipher entries and the "Unsolved Ciphertext" -> "BnF fr.7131, f.256" item.

## Summary (read this first)

CS-BONGARS7131 (parent worker, 27 Sept 2026). Queued by `SCOUT-OWN-7` (QUEUE.md "SCOUT-OWN-7 key-adjacent
candidates" row 4, 27 Sept 2026) from `KEY-ADJACENT.tsv` row 18, on the strength of Tomokiyo's `bongars.htm`.

**The brief's own citation, and both `KEY-ADJACENT.tsv` row 18 and `QUEUE.md` row 4, name the wrong cipher.**
They say f.256 "can be deciphered with Bongars' cipher no.3." Reading `bongars.htm` directly (verbatim, below)
shows the cipher is **no.16** (f.243, BnF fr.7131), not no.3 (f.275, BnF fr.7129). No.3 is a different cipher
used for a different letter two entries above f.256 on the same page -- BnF fr.7129, f.268, 2 November 1604,
signed Villeroy -- which is this repository's own existing target `ciphers/fr7129-villeroy-bongars-1604/`
(status `blocked`). The scout's row concatenated the `no.24 (f.256)` heading's own sentence ("A letter mostly in
cipher (no.16), undeciphered. See below.") with the *next* item's key-attribution sentence, the same
paste-across-headings error CS-CLAIR331 found in `francis.htm` row 3 the same morning (`ciphers/
clair331-rangone-montmorency-1530/NOTES.md`, "Correction to KEY-ADJACENT.tsv / QUEUE.md"). `ciphers/
fr7129-villeroy-bongars-1604/NOTES.md` itself repeats the same wrong "no.3" in one sentence contrasting the two
letters -- corrected in the same push as this folder (see "Corrections made" below).

**More importantly: Tomokiyo already prints a fragment of the plaintext.** Under the page's own "Unsolved
Ciphertext" section, the fr.7131 f.256 item reads (quoted verbatim, `bongars.htm` line ~213-216):

> BnF fr.7131, f.256
> Dated 8 February 1603 and signed Beaumont. Addressed to Bongars in Frankfurt. Can be (for the most part)
> deciphered with Bongars' cipher no.16. (From the few interlined letters, someone must have been aware that the
> symbol for "r" is unique to this cipher.)
> [image: BnFfr7131f256.jpg, the ciphertext leaf]
> One portion of the plaintext turned out to be a Latin phrase "Sabini sumniant quad volunt" (The Sabines dream
> what they will.).

This is a printed plaintext fragment from a named source (Tomokiyo), matching this repo's own `SCOUT-OWN-7`
selection-guidance wording for check-solved item (a): "A printed plaintext makes it `found-solved`." `QUEUE.md`'s
own KT-01 row (the fr7129 target, written 24 Sept 2026, before this folder existed) already flagged this in
passing -- "contrast BnF fr.7131 f.256 two entries below it, where Tomokiyo already quotes a deciphered fragment
-- excluded here for that reason" -- but nothing had acted on it until now.

Found-solved grade (README F0/F1/F2): **F0**. Tomokiyo's own page is the specialist source for the Bongars
fr.7125-7132 cipher group (the source this repo's own `bongars.htm` mirror and every related target, including
fr7129-villeroy-bongars-1604, already cites as the identification of record); it already links f.256 to a partial
decipherment under its own key attribution (no.16) and quotes a resulting plaintext fragment. No contribution
to make here -- Tomokiyo did not overlook this letter, and this repo does not repeat the reading.

**Caveat, stated as Tomokiyo states it, not stronger:** "can be (for the most part) deciphered" and "one portion
of the plaintext" is a partial claim, not a full transcription; no.16's key is described in prose only ("Cipher
alphabet with symbols and Arabic figures. Names and words. Nulls. A symbol to double the preceding letter and a
symbol to cancel the preceding character") -- unlike no.17/no.15/no.13, `bongars.htm` prints no key-table image
for no.16 itself. This does not change the found-solved verdict (rule 10's F-grades key on the plaintext being in
print, not on a full key being published), but it does mean this repo could still make an F1-style contribution
(a complete, machine-readable key and full reading) if the parent decides it is worth pricing -- see "Key on
disk" below for what that would cost.

## Identification

- Image: Gallica ark `btv1b10509420g`, confirmed by `tools/gallica_folio.py btv1b10509420g --folio 256`
  (27 Sept 2026): folio 256 resolves cleanly to canvas f523 (256r, 3603x5970) and f524 (256v, 3524x6036), both
  labelled `256r`/`256v` in the manifest (no offset ambiguity at this folio -- the tool's own offset-change
  warnings are for other folio ranges in this same volume). Manifest title: "BnF. Département des Manuscrits.
  Français 7131" (`sources/gallica-manifests/btv1b10509420g.json`), confirming this is BnF fr.7131.
  - `https://gallica.bnf.fr/iiif/ark:/12148/btv1b10509420g/f523/full/full/0/native.jpg` (256r)
  - `https://gallica.bnf.fr/iiif/ark:/12148/btv1b10509420g/f524/full/full/0/native.jpg` (256v)
- Sender: Christophe de Harlay, comte de Beaumont (1570-1615), French ambassador to England 1602-1605 (confirmed
  by web search, English Wikipedia "Christophe de Harlay, Count of Beaumont"; his official dispatches to the king
  and to Villeroy during his London embassy are BnF fr.3513, a *different* volume from this one -- this letter,
  to Bongars in Frankfurt rather than to the king or Villeroy, is not part of that series).
- Recipient: Jacques Bongars, in Frankfurt (per `bongars.htm`'s own line, "Addressed to Bongars in Frankfurt").
- Cipher: Bongars' cipher no.16 (BnF fr.7131 f.243), described but not imaged on `bongars.htm`: "Cipher alphabet
  with symbols and Arabic figures. Names and words. Nulls. A symbol to double the preceding letter and a symbol
  to cancel the preceding character."

## Key on disk (item b, per brief)

This repo already holds `ciphers/fr7129-villeroy-bongars-1604/` (status `blocked`), with three key files:
`keys/key_f270.tsv` (cipher no.1, f.270-271, BnF fr.7129), `keys/key_f274.tsv` + `key_f274_names.tsv` (cipher
no.2, f.274), and `keys/key_f275.tsv` / `_v2` / `_v3` (cipher no.3, f.275, built from a period interlinear
decipherment of sibling folios). **None of these is cipher no.16 or an earlier/later state of it** -- no.16 is a
different cipher, at a different folio (f.243), in the *other* volume of the pair (fr.7131, not fr.7129). There
is no key on disk anywhere in this repo for cipher no.16. Recovering one would need either (1) a fresh
transcription of the f.243 alphabet table itself (BnF fr.7131, same volume as the ciphertext, so no extra
digitisation cost) or (2) reconstruction from the ciphertext against Tomokiyo's one confirmed plaintext fragment
as a crib, the same shape as the reconstructed-cipher approach `bongars.htm` itself uses for other ciphers in
this group ("Below is my reconstruction of this cipher made before I found the original cipher"). Pricing either
is a decision for the parent; this worker did not attempt it (out of brief).

## Corrections made this push

1. `KEY-ADJACENT.tsv` row 18 (bongars.htm / fr.7131 f.256): "Bongars' cipher no.3" -> "Bongars' cipher no.16" in
   both the `sentence` and `key_location` columns; `key_printed` corrected from "yes" to "no (described in prose
   only; no key-table image for no.16 on `bongars.htm`, unlike no.17/no.15/no.13)"; the `in_repo` cell's
   found-solved note is resolved by this folder (was "unchecked").
2. `QUEUE.md` row 4 (SCOUT-OWN-7 top-5 table): key-status cell struck through with the same convention CS-CLAIR331
   used for row 3 ("~~key printed (Bongars' cipher no.3)~~ -- wrong, see `ciphers/fr7131-beaumont-bongars-1603/
   NOTES.md`"); status cell set to `check-solved found-solved`.
3. `ciphers/fr7129-villeroy-bongars-1604/NOTES.md`'s "Tomokiyo (`bongars.htm`...), quoted verbatim" section: the
   sentence "Contrast the next item down, fr.7131 f.256 ... which Tomokiyo tags 'can be (for the most part)
   deciphered' with cipher no.3" corrected to "cipher no.16" (the substance of that paragraph -- that f.268
   itself carries no partial-reading language, unlike f.256 -- is unaffected and left as written).

## Sources checked (date, method) -- CLAUDE.md rule 1 order

1. **Search engine (web), 27 Sept 2026**, `WebSearch`, five queries: `"fr. 7131" Bongars Beaumont "1603" cipher
   OR chiffre f.256`; `Sabini somniant quae volunt Bongars Beaumont`; `cipherbrain Bongars fr.7131 OR "fr. 7131"
   Beaumont`; `Christophe de Harlay Beaumont Bongars cipher letter Frankfurt 1603`. No hit for this specific
   letter, its plaintext, or a decipherment anywhere but Tomokiyo's own page and this repository. Confirmed
   Beaumont's identity and that his own official-dispatch volume (fr.3513) is a different collection from this
   letter's (fr.7131, Bongars' own papers).
2. **Sender's/recipient's printed correspondence, 27 Sept 2026.** Beaumont's own dispatch series (fr.3513, to the
   king/Villeroy) does not cover Bongars correspondence, per its own Gallica title, so not the right edition for
   an incoming letter to Bongars; not opened (out of scope for this letter). Bongars' own printed *Lettres*
   (Leiden 1647 Latin `Epistolae`; Paris 1668/1681 French translation, *Lettres de Monsieur de Bongars ... vers
   les electeurs, princes, & Etats protestants d'Allemagne*) collect Bongars' own *outgoing* letters, not
   incoming ones from Beaumont -- web search found no Internet Archive or HathiTrust copy in the time available;
   given the direction-of-correspondence mismatch (this edition would not carry a letter written *to* Bongars),
   not pursued further this pass.
3. **Calendars/documentary editions, 27 Sept 2026.**
   - Anquez, *Henri IV et l'Allemagne d'après les mémoires et la correspondance de Jacques Bongars* (1887,
     Gallica `bpt6k213732d`), full-text searched via Gallica ContentSearch (`services/ContentSearch?ark=ark:/
     12148/bpt6k213732d&query=...`), read by this worker directly: "7131" (40 hits, none at f.256 or naming an 8
     February 1603 Beaumont letter), "Beaumont" (6 hits, all "le roi à Beaumont" -- Henri IV's outgoing letters
     to Beaumont in London, a different correspondence direction and none dated 8 Feb 1603), "février 1603" (74
     hits, none matching this letter). Letter absent from Anquez's narrative under all three query families.
   - Berger de Xivrey, *Recueil des lettres missives de Henri IV* (HathiTrust catalog record 000410962, t.6
     covers 1603-1606) -- `tools/print_check.py`'s HTRC Extracted Features co-occurrence check ran against all 9
     resolved volume ids across four libraries (hvd/mdp/nyp/uva/iau digitisations); no page in any volume carries
     all four content words of either spelling of the Latin phrase. A coarse negative (co-occurrence, not a page
     read), logged as such, not as a page-by-page read of t.6.
4. **Comment threads of list posts (Cryptiana blog, Cipherbrain), 27 Sept 2026.** Web search for "cipherbrain"
   plus this letter's identifiers returned nothing relevant (see query 3 above). No Cryptiana blog post found
   naming this letter.
5. **DECODE (de-crypt.org), 27 Sept 2026.** Grepped the existing login-free crawls (`sources/decode/
   records-decrypted-2026-09-24.tsv`, 1361 rows; `records-non-decrypted-2026-09-24.tsv` +
   `-diff.tsv`, 1187 rows each) for "7131", "Bongars", "Beaumont": no hits in any file. Not re-crawled live (the
   24 Sept crawl is a full sweep of both statuses for record_type=Cipher and is not stale for a shelfmark/name
   check).
6. **Solver repositories, 27 Sept 2026.** Shallow-cloned both fresh (`git clone --depth 1`) into scratch, per the
   CS-CLAIR331 lesson (dbourdeau has been working straight down Tomokiyo's key-adjacent items this month).
   - `dbourdeau/cyphersolver` (commit at clone time not recorded; fetched 27 Sept 2026): `grep -rliw Bongars`
     across the tree hits only tangential files (a Gallica-sweep search-index JSON, an unrelated `henryiv.txt`
     harvest, `targets/breves1603/` -- a different letter, Bréves 1603 -- and `docs/hesse1603.html` -- Hesse
     1603, also different). No target folder under `targets/` for fr.7131, f.256, Beaumont, or Bongars-to-Bongars
     correspondence generally.
   - `aaymeloglu/unsolved-ciphers` (fetched 27 Sept 2026): `grep -rliw Bongars` hits only `TARGETS.md`, row 11
     ("Cocquet -> Mangot, Rome (Clairambault 369 f.317), Nov 1616 ... no period key from Bongars volumes
     fr.7129/7131 fits") -- a *different* target (Clair.369) that tried Bongars-family keys against it and found
     none fit; not this letter. No dedicated target for fr.7131 f.256 anywhere in this repository either.
   - Neither repository's own planning text (README/profile notes, per the 26 Sept "stated next step" rule)
     names this letter as a next step.
7. **print_check.py, 27 Sept 2026** (`ciphers/fr7131-beaumont-bongars-1603/print-check.tsv`,
   `print-check-hosts.tsv`): phrases = Tomokiyo's own printed fragment in both spellings given on the page
   ("Sabini quod volunt somniant", the correct classical proverb word order, confirmed by web search as the
   standard form; and "Sabini sumniant quad volunt", the exact string as printed on `bongars.htm`, possibly an
   OCR/typo of the same proverb). `ia-global` (be-api full-text search) returns "168 item(s)" for the
   normal-word-order spelling, but is not an exact-phrase match (CLAUDE.md's own documented caveat: be-api's
   result fields are not reliable phrase locators) -- the top hits (an Italian dialect etymology dictionary, an
   18th-c. English theological pamphlet, a 1951 psychiatry journal, Burton's *Anatomy of Melancholy*, a 1943
   Italian touring guide) are all clearly unrelated to Bongars/Beaumont/Henri IV, consistent with fuzzy
   word-level matching rather than a genuine phrase hit; treated as no genuine hit. Google Books, OpenAlex and
   CrossRef likewise return only bibliographically-unrelated results under both spellings (raw hit counts in the
   tens of thousands for the keyword rows are relevance-ranked noise, not phrase matches) -- no title or DOI in
   any result plausibly discusses this letter. Semantic Scholar hit its keyless 429 mid-run (one query blocked);
   not retried (good-citizen one-retry rule). Net: no printed source found anywhere except Tomokiyo's own page
   for the specific plaintext fragment he quotes, which is expected for an F0 found-solved reading (the fragment
   is Tomokiyo's own translation/transcription, not itself independently republished).

## intake_gate_check.py

```
$ python3 tools/intake_gate_check.py fr7131-beaumont-bongars-1603
fr7131-beaumont-bongars-1603: found-solved (line 3) -- edition/page or full-text-search citation found within 6 lines
```
