found-solved

# Paolo Sarpi's cipher for his Italian letters to "Castrino" — BnF Dupuy 111

QUEUE row: M3 (sources/solver-diffs/2026-09-23-digitised-hits.tsv, "Digitised candidates, no copy needed").

## Source

BnF, Departement des Manuscrits, **Dupuy 111**, Gallica `ark:/12148/btv1b10034811v` (105 leaves),
"Recueil de lettres italiennes et latines de fra Paolo SARPI, d'octobre 1608 a juillet 1617" (Gallica IIIF
manifest title, matching the WebSearch-confirmed BnF description). QUEUE M3's catalogue quote: "le chiffre
dont fra Paolo se servait dans ses lettres italiennes, autogr. (100)". Sarpi's Italian letters in the
volume are addressed to "Monsieur Castrino", a probable pseudonym for a French Huguenot correspondent;
later Latin letters in the same volume go to Gillot, Hotman and Casaubon.

## Check-solved sweep (23 September 2026)

1. **Web search.** WebSearch `"Dupuy 111" Sarpi "chiffre" Castrino cipher` and a follow-up query for
   Busnelli/Ulianich together turned up, decisively:
   - A dedicated scholarly digital edition, **correspondance-sarpi.univ-st-etienne.fr** ("Paolo Sarpi"
     project, Universite de Saint-Etienne), with individual pages per letter (e.g. `/lettre/1610-02-16a-
     castrino`, `/lettre/1609-04-28a-castrino`, `/lettre/1611-01-31a-castrino`...) and a "chiffrement"
     (cipher) field in its search facets, i.e. the project explicitly tracks which letters are enciphered.
     A search snippet for the 16 Feb 1610 letter to Castrino gives its source as **"BnF, Dupuy 111,
     f. 34r-v"**, "previously published by M. Busnelli in 1931 and 1986". Direct fetch of that page
     returned HTTP 503 ("service temporairement indisponible pour cause de maintenance", the university's
     own scheduled-maintenance page) both on first try and after a 1.5s-spaced retry — read from the
     WebSearch snippet only, not confirmed by a live page render this sweep.
   - Manlio Duilio Busnelli's edition, cited by title: *"Un carteggio inedito di Fra Paolo Sarpi con
     l'ugonotto Francesco Castrino (1608-1611)"* (1986), building on an earlier 1931 partial publication;
     51 letters to Castrino in Dupuy 111, compiled 1630 by the volume's original collector Pierre Dupuy.
   - A second, separate scholarly article specifically on this cipher: Marie Viallon, *"Paulo Sarpi, le
     chiffrement de la correspondance"* (HAL id hal-01524175, univ-lyon3.hal.science), discussing Sarpi's
     decision from 1607-1609 to encipher his correspondence with French Protestants after two attacks on
     his life, and citing Jacques Aleaume's cryptographic advice. The article's HAL PDF link returned a bot
     challenge page (Anubis-style proof-of-work gate) to a plain curl fetch; not pursued further (no
     browser route attempted, per budget). A secondary route via the Wayback Machine CDX API failed twice
     (`Recv failure: Connection reset by peer`, then "Internet Archive: Temporarily Offline" on retry,
     matching the IA outage other workers logged tonight) — one retry taken per the good-citizen rule, not
     pursued a third time.
   - Boris Ulianich is cited elsewhere as having used Busnelli's edition in his own scholarship on Sarpi's
     correspondence (WebSearch synthesis only, no primary citation opened this sweep).
2. **Print / scholarship — see above; realized.** Busnelli's 1931/1986 editions are printed decipherments
   of this exact correspondence, citing this exact manuscript by folio.
3. **Community lists.** `sources/cryptiana/` grepped for "sarpi"/"castrino"/"dupuy 111": no hit anywhere
   in the local mirror.
4. **DECODE.** Cached catalogue grepped for the same terms: no hit.
5. **Bourdeau.** `cs-recheck/CATALOGUE.md`, `SOLVED_CATALOGUE.md`, `TARGETS.md` grepped for the same:
   no hit.
6. **Aymeloglu.** `ay/CATALOGUE.md`, `TARGETS.md`, `SHORTLIST.md` grepped for the same: no hit.

Requests: gallica.bnf.fr 4 (3 new IIIF image fetches at reduced width, plus reuse of the scout's 3 cached
images f98/f99/f100), correspondance-sarpi.univ-st-etienne.fr 2 (1 redirect follow, 1 HTTP 503 on retry —
university maintenance window, not a block on this project's side), univ-lyon3.hal.science 1 (bot
challenge, not solved), web.archive.org (CDX) 2 (both failed, IA outage, 1 retry per good-citizen rule).
WebSearch 2 queries (shared across the M1-M3 batch, plus 1 more specific to this target).

## What the leaves show

The catalogue's folio "100" is the key, not a letter: canvas index 102 (image corner "100") carries only a
later French archival note, "Chiffre escrit de la main du Pere Paul par lequel il se servoit avec ses amys
auquel il a joint les lettres italiennes qu'on peut au reste de ce volume" ("cipher written in Father
Paul's own hand, which he used with his friends, to which he has joined the Italian letters found in the
rest of this volume"). The actual key table is on the following leaf, **canvas 103 = folio "101"**: a full
page of alphabetically-organised code-word/number pairs (city and office names — Bruxelles, Anversa,
Milano, Roma, Firenze — each given a number), with a "nulle a.e.i.o.u." null-letter line, matching the
WebSearch summary's description of a nomenclator drawing on Polybius-square-style nulls. **The letters
themselves ARE in cipher, confirmed by direct image inspection**: canvas 36 (approx. folio 34, matching
Busnelli's citation for the 16 Feb 1610 letter to Castrino) shows continuous Italian prose with two- and
three-digit numeral groups embedded inline in place of names and sensitive terms — a nomenclator-over-
cleartext system, consistent with the key at f.101 and with Viallon's description of Sarpi's post-1607
enciphering practice. This settles the brief's question directly: the letters are genuinely enciphered, not
merely accompanied by a surviving but unused key. (QUEUE M3's own caveat, "f98/f99...show plain Latin text
on Baronio's Annales", is confirmed and explained: those are two leaves earlier, part of the later Latin
correspondence to Gillot/Hotman/Casaubon, not the enciphered Castrino letters, which sit earlier in the
volume, around f.34 and presumably elsewhere through the Oct 1608-July 1617 run.)

## Edition risk

**Realized, specifically and by name.** Busnelli published this correspondence from this manuscript in
1931 (partial) and 1986 (full, as *Un carteggio inedito di Fra Paolo Sarpi con l'ugonotto Francesco
Castrino*), citing individual folios (e.g. f.34r-v for the 16 Feb 1610 letter observed above). A live,
actively-maintained university digital-edition project (correspondance-sarpi.univ-st-etienne.fr) currently
indexes the letters with a cipher-status field, strongly suggesting the modern scholarly community already
tracks which of these letters are enciphered and has (or is building) transcriptions/decipherments for
them, though the site's own pages could not be read live this sweep (maintenance window).

## Verdict

**Found-solved / not a valid cryptanalysis or recovery target.** The letters are genuinely in cipher
(confirmed by image, contrary to a plain-key-only reading), but the correspondence has already been
deciphered and published by Busnelli using this exact manuscript, with folio citations that match what was
viewed here. This is the high-edition-risk realization the QUEUE row explicitly flagged before scoring.
Nothing here is claimed as new, unpublished or unread (rule 10); a check-solved sweep is a search result,
not a novelty verdict, and no verifier session has been run on this target.

## Next

Drop M3 from the board; it is not a recovery or cryptanalysis target under README "What counts as a
result" once a printed decipherment of this exact manuscript's letters exists. If anyone wants a narrower
follow-up: (1) confirm live against correspondance-sarpi.univ-st-etienne.fr once its maintenance window
ends, to see whether every one of the 51 Castrino letters is marked deciphered or only some; (2) the
Viallon HAL article (hal-01524175) would need a real-browser fetch (per the Access playbook's bot-challenge
route) to read in full, if anyone wants the cipher's technical description rather than the WebSearch
summary used here.
