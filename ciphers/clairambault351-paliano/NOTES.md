closed-negative

# "Chiffre du duc de Paliano" — BnF Clairambault 351

QUEUE row: M2 (sources/solver-diffs/2026-09-23-digitised-hits.tsv, "Digitised candidates, no copy needed").

## Source

BnF, Departement des Manuscrits, **Clairambault 351**, Gallica `ark:/12148/btv1b9000680d` (327 leaves),
part of a Franco-Italian diplomatic recueil "Documents originaux et copies... concernant les regnes de
Francois Ier a Henri III" (Gallica IIIF manifest title). BnF Archives et manuscrits notice
`http://archivesetmanuscrits.bnf.fr/ark:/12148/cc13826w/cd0e9660` (a combined finding-aid page spanning
Clairambault 348-351), fetched 23 September 2026, gives the volume's item-by-folio list. The relevant
entry, quoted verbatim, under the heading "Clairambault 351 • XLI Regne de Henri II. — 1557, aout-1558,
avril. — Correspondance des Guise; lettres orig. signees":

> Fol. 173 et 175 • Chiffre du duc de Paliano.

with surrounding entries "Fol. 161 • Projet d'alliance entre le pape et la France" and "Fol. 196-197 •
Lettre de Charles-Quint et de sa mere Jeanne la Folle, a l'eveque de La Plata...". Elsewhere in the same
volume's list: "Fol. 22 • Le cardinal Caraffa, le duc de Paliano, et le marechal Pietro Strozzi" and
"Fol. 68, 102 • [Marcantonio], duc de Paliano" (his own letters, no cipher noted against them).

## Check-solved sweep (23 September 2026)

1. **Web search.** WebSearch `"Clairambault 351" Paliano chiffre cardinal Caraffa` — no dedicated blog,
   blog comment or DECODE/Cipherbrain post naming this shelfmark; general BnF/Biblissima catalogue pages
   and Wikipedia biography pages for Giovanni Carafa, Duke of Paliano only.
2. **Print / scholarship.** Ribier's *Lettres et memoires d'estat* (1666) and the Caraffa-war literature
   were not searched page-by-page this sweep, since the item itself resolves to a key, not a ciphertext
   (see "What the leaves show" below) — moot for the same reason as the d'Avaux case in
   `ciphers/davaux-1633/NOTES.md`.
3. **Community lists.** `sources/cryptiana/` grepped for "paliano": no hit. "caraffa": one hit,
   `sources/cryptiana/web/habsburg.htm`, discussing an unrelated Habsburg-era cipher ("Castaldo and
   Caraffa" nomenclator tables, 16th-c. Imperial ciphers) with no connection to this volume or the
   Guise-Caraffa correspondence. "clairambault": two hits (`GL.htm`, `louisxiv.htm`), both unrelated
   later-period Clairambault volumes (Louis XIV era), not 351.
4. **DECODE.** Cached catalogue grepped for "paliano"/"clairambault 351": no hit.
5. **Bourdeau.** `cs-recheck/CATALOGUE.md`, `SOLVED_CATALOGUE.md`, `TARGETS.md` grepped for the same:
   no hit.
6. **Aymeloglu.** `ay/CATALOGUE.md`, `TARGETS.md`, `SHORTLIST.md` grepped for the same: no hit.

Requests: gallica.bnf.fr 4 (1 manifest, 3 IIIF image fetches), archivesetmanuscrits.bnf.fr 1 (HTTP 200,
plain curl, 804 KB combined finding-aid page for Clairambault 348-351). WebSearch 1 query (shared across
M1-M3 batch).

## What the leaves show

Located the item precisely from the finding-aid's folio citation ("Fol. 173 et 175") rather than guessing:
canvas index 178 on the IIIF manifest carries the folio mark "173" in its top-right corner and shows a
**full-page Italian cipher key** — an alphabet substitution table, a "Doppie Lettere" (doubled-letter)
section, a "Nulle per usar al Cifrare" (nulls) section, and an "Accompiate" nomenclator of place-code
numbers (Firenze, Venetia, Roma, "Il Duca di M[ilano]", etc.), dated internally "fatto li 13 di luglio
1557". Canvas 180 (folio "175") carries a near-identical second copy of the same table, with a wax-seal
outline and the words "duca di Paliano" visible on the facing leaf — the item is the key copied twice, not
a letter. The facing/neighbouring correspondence leaves sampled (canvas 175 = folio ~170, a plain Italian
letter; the several named "duc de Paliano" letters at ff.22, 68, 102, 309 in the finding aid's own list are
each described as "Lettre orig." with no "avec chiffre"/"chiffree" qualifier, unlike other entries in the
same finding-aid page that are explicitly marked "avec chiffre" or "avec chiffres" when they are, e.g.
"Lettre orig. de Jean de Calvimont... avec chiffre" and "Lettre d'Hippolyte d'Este... avec chiffres" in the
neighbouring Clairambault 325/349 sections) show no ciphertext. No letter in this volume is catalogued as
being written in cipher; the "Chiffre du duc de Paliano" entry is the key alone, matching the brief's
expected key-only pattern (compare "Double du chiffre de Claudio Marini", Clairambault 361, QUEUE M5).

## Edition risk

Low/moot: since the item is a key with no attached ciphertext in this volume, there is no decipherment to
check against a printed edition. Ribier and the Caraffa-affair literature were not searched for this
reason.

## Verdict

**Key-only / not a cryptanalysis or recovery target.** "Chiffre du duc de Paliano" (Clairambault 351,
ff.173 and 175) is a nomenclator key, copied twice, with no letter in the same volume marked or observed as
written in that cipher. Per the brief: this is contribution material (a key, offered for the record) if
anyone ever finds a matching ciphertext elsewhere in the wider Clairambault series or another Guise/Caraffa
collection — it is not itself a reading, and nothing here is claimed as new or unpublished (rule 10).

## Next

Drop M2 from the board as scored (recovery); it is not a recovery target because no ciphertext pairs with
this key in the volume. If anyone wants to chase the narrower question — whether any Guise-Caraffa letter
elsewhere in Clairambault 325-461 (the wider "documents pour Bossuet's Dauphin studies" run this volume
belongs to) was ever sent in this specific 1557 key — that is a fresh scout task across the whole
Clairambault sub-series, not a next step on this one volume.
