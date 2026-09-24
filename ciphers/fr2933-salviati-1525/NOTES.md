open

# Cardinal Giovanni Salviati cipher letter, 16 Oct 1525 -- BnF Français 2933, no. 11

QUEUE row: M35 (`sources/solver-diffs/2026-09-24-lane-g3-gallica6.tsv`, "Sixth pass (LANE G3), 24 September 2026").

## Source

BnF, Département des Manuscrits, **Français 2933** ("Anc. 8469", "Recueil de lettres et de pièces
originales, et de copies de pièces indiquées comme telles dans le dépouillement qui suit"), item 11:
"Lettre en chiffres, et en italien, de « JOHANNES, cardinalis de Salviatis,... Die XVI octobris 1525 »."
Finding aid: `archivesetmanuscrits.bnf.fr/ark:/12148/cc493855/cd0e354` (fetched via browser, 24 Sept 2026).
Cardinal Giovanni Salviati (Medici-circle cardinal, papal nuncio to Spain 1525-1530, active negotiating
the release of the captured François Ier after Pavia) is a plausible author for a 16 Oct 1525 Italian
cipher letter to a French correspondent.

The finding aid's full item list (Fol.1-84+) was read: item 10 (Fol. ~49-54, "Rapport d'un envoyé de la
cour de France, concernant les intrigues de Charles-Quint") precedes it, item 12 (Fol. 58, another
unrelated "rapport") follows it -- **no adjoining "Deschiffrement" item is catalogued next to item 11**
(unlike item 17, Fol. 70, "Deschiffrement d'un rapport concernant messire PHILIBERT," which is a
different, unrelated item several folios later). Per rule about checking for an interlinear/facing gloss:
none is stated in the catalogue text for this item.

## Check-solved sweep (24 September 2026)

1. **Web search.** `"Français 2933" Salviati chiffre 1525`, `cardinal Salviati lettre chiffrée 1525
   déchiffrement`: no source ties BnF fr.2933 no.11 to a known decipherment. Search summaries surfaced only
   the unrelated 1525/26 "Planisphère de Salviati" (a world map, Biblioteca Laurenziana Med. Palat. 249,
   Florence -- different Salviati item entirely) and general Giovanni Salviati biography (legate to
   Madrid 1525, negotiating Charles V's Italian coronation and the treaty later formalised as the League
   of Cognac 1526). One search summary noted (from the Strozziane inventory, Archivio di Stato di Firenze)
   that "ciphers used by Cardinal Salviati were recorded, including a cipher with Jacopo Salviati (the
   cardinal's father)... kept on large open folios" -- background on Salviati-family cipher use in general,
   not a match to this specific BnF letter; not followed further (out of scope, no shelfmark or date tying
   it to fr.2933).
2. **Print / calendars.** Desjardins, *Négociations diplomatiques de la France avec la Toscane* (Canestrini's
   documents, 1859-1886) is the calendar most likely to print Florentine/Medici-circle correspondence of this
   period; web search located volume identifiers (Gallica `bpt6k292781` for tome 1) but returned no content
   match for "Salviati" + "1525" + "chiffre" together -- **a real gap, not searched by full text this pass**
   (out of the $8 cap for both targets; flagged for a follow-up). Mignet's *Rivalité de François Ier et de
   Charles-Quint* (checked for M36 below) does not cover Italian/papal correspondence of 1525 and was not
   re-run for this target.
3. Duplicate of item 2 (Desjardins/Canestrini is this period's Franco-Tuscan document series; no separate
   calendar identified).
4. **Cryptiana / Cipherbrain.** Grepped all 104 cached pages in `sources/cryptiana/web/` for "salviati",
   "2933", "cardinalis", "voiage.*allemagne" (case-insensitive): no hit anywhere. `francis.htm` ("earliest
   use of cipher in France", covering BnF Clair.325/328/329-331/333, fr.2984/3019/3045/3053/3081/20506,
   NAF 4206 in detail, and mentioning Hieronimo Ranzo f.73/f.136 and the "vasto1527" Del Vasto letters the
   brief flagged to watch for) never names Salviati or fr.2933. `venetian.htm`, `vatican.htm`, `schiner.htm`,
   `spanish.htm`, `spanish2.htm` (the other pages most likely to cover an Italian/papal cipher of this date)
   were grepped for "salviati" directly: no hit. No Cipherbrain (cipherbrain.org / cryptiana.blogspot.com)
   page found by web search either.
5. **DECODE.** `unsolved-ciphers/catalogue/decode-catalog.csv` (fresh shallow clone) grepped for "2933" and
   "salviati": the numeric "2933" is an unrelated DECODE record id (a 1829-1830 British Library item, Add MS
   32277); the only Salviati record is **DECODE R12**, Vatican Secret Archive i.1025 Segr. Stato Francia 7,
   "Nuncio Salviati, archbishop of Nazareth. France," dated **1574** -- a different Salviati (a later
   nuncio), a different archive (Vatican, not BnF), a different date, already marked "Partially decrypted"
   in the catalog and separately noted solved in `cyphersolver/CATALOGUE.md` ("read at the time, 21 Sept
   2026... Lasry's F6 key is on the record"). Not the same item; no DECODE record under the fr.2933 shelfmark.
6. **Solver repositories.** Fresh shallow clones of `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers`
   grepped for "salviati", "2933", "cardinalis" (case-insensitive, all matching files inspected): every
   "2933"/"salviati" hit is a coincidental filename, JSON id, or numeral (e.g. `jantini1517/vestigia/v1848.json`,
   `rome1536/*` file line counts, `sunyatsen/*.csv` codepoints) -- no shelfmark or content match to BnF
   fr.2933 no.11 in either repository.

Requests: WebSearch 5 queries. github.com 2 shallow clones (shared with M36 below). No credentials, no logins.

## Digitisation and ciphertext check (24 Sept 2026)

**Digitised: yes.** ark `btv1b90600674` (found in `sources/solver-diffs/2026-09-23-digitised-excluded.tsv`
row 83, a prior Gallica-SRU sweep of this same Français 2754-3068 run, tagged "Français 2933" against the
same catalogue title). `tools/gallica_folio.py btv1b90600674 --folio 54` was attempted to pin the canvas by
manifest label but the IIIF manifest endpoint reset twice (`[Errno 104] Connection reset by peer`); per the
LANE G3 common brief's Gallica note, stopped after one retry and fell back to the direct image endpoint.

**Ciphertext: yes, confirmed by direct inspection.** The direct-image endpoint
`/iiif/ark:/12148/btv1b90600674/f55/full/400,/0/default.jpg` (canvas 55) shows dense rows of numeral and
symbol groups in an Italian-hand nomenclator style -- unambiguous ciphertext, not a decipherment or plain
letter (saved: `images/canvas55_f54_confirm.jpg`). The preceding canvas (f54, `images/` not kept, item 10's
own leaf) shows continuous plain cursive French prose ending near the bottom of its right-hand page, where
a few numerals appear at the very foot -- consistent with item 11's cipher beginning at the end of that
same gathering, at the catalogued Fol. 54. Canvas = folio 54 label not independently confirmed (manifest
unreachable); **canvas ~55 is a content-matched pin (dense cipher text, immediately after item 10's plain
prose), not a label-confirmed one.**

Requests this section: gallica.bnf.fr 2 successful image fetches (f54, f55) + 2 failed manifest.json
attempts (1 try + 1 retry, both reset), all ≥2s apart, UA `cipher-lab research script (contact via
repository)`. No 403/429/challenge seen, only transient connection resets.

## Verdict

**Open**, 24 Sept 2026. Six sources checked (web, print/calendars, cryptiana/cipherbrain, DECODE, Bourdeau,
Aymeloglu): no found-solved claim, no key, no decipherment located under this shelfmark or this letter's
date/sender in any of them. Not scored closed-negative (no cryptanalytic attempt was made this pass -- this
is a location/prior-print check only, rule 3's matched-control requirement does not apply). Confirmed
digitised (ark `btv1b90600674`) and confirmed to carry genuine ciphertext at canvas ~55 (content-matched, not
manifest-pinned). The Desjardins/Canestrini Toscane calendar (item 2 above) is the one real gap: not full-text
searched this pass for "Salviati" + this date, out of the shared $8 cap for both M35 and M36.

Stage-2 eligible on this verdict (`open`, six sources checked, per check-solved.md).
