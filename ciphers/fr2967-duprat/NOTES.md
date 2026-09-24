open

# Chancelier Duprat decipherments to François Ier -- BnF Français 2967

QUEUE row: M30 (sources/solver-diffs/2026-09-24-lane-g2-gallica4.tsv, "Fourth pass, 24 September 2026").

## Source

BnF, Département des Manuscrits, **Français 2967** ("Recueil de lettres et de pièces originales"),
archivesetmanuscrits ark `cc494214`. QUEUE catalogue note: at least four/five items catalogued "Autre
Dechiffrement de despesche envoyée au roy François premier par le chancelier DUPRAT" plus a fifth "Dechiffrement
de lettre envoyée par le chancelier DUPRAT au roy." Undated in the queue row; Antoine Duprat was chancellor of
France 1515-1535. Below the Français 3005-3993 exclusion line, so not covered by the second pass's fr.3xxx drop.

## Check-solved sweep (24 September 2026)

1. **Web search.** `"chancelier Duprat" déchiffrement dépêche François premier "2967"` surfaced the manuscript's
   IIIF/Biblissima record and, per the search summary, additional catalogue detail not in the QUEUE row: "one
   dispatch is from A. Duprat, Jehan de Selve, and Robert Gedoyn to King François I, dated in Calais on
   September 8th" -- naming two co-correspondents (Jehan de Selve, Robert Gedoyn) and a place (Calais) the
   QUEUE row did not carry. No solver or blog claim surfaced.
2. **Printed correspondence / calendars.** *Collection des ordonnances des rois de France: Catalogue des actes
   de François Ier* (Académie des sciences morales et politiques, 1887-1908, 8-9 vols) is exactly this period's
   royal-acts calendar and is on Internet Archive (`collectiondesor05acad` and siblings). A targeted full-text
   query (`be-api.us.archive.org/fts`, `q=Duprat chiffre`) against vol.5 (`collectiondesor05acad`) returned one
   page (p.836) but the "chiffre" hit there is the ordinary sense ("fixe le chiffre des troupes qu'il mettra à
   sa disposition," a troop count in an unrelated 1546 act), not a cipher reference, and the page's separate
   "Duprat" hit is likewise unrelated (a different 1546 benefice appointment) -- a genuine negative for this
   one query on this one volume, **not** an exhaustive sweep: only 1 of the catalogue's 8-9 volumes was queried,
   and only one query string was tried. Flagged as a real gap for a follow-up worker, not scored as a clean
   source-family negative.
3. Duplicate of item 2 (the Catalogue des Actes de François Ier is the calendar/state-paper-series source for
   this period; no separate series identified).
4. **Cryptiana / Cipherbrain.** `sources/cryptiana/web/francis.htm` ("earliest use of cipher in France")
   covers BnF Clair.325 (1526), fr.2984 (1526), Clair.328 (1528), Clair.329/330/331/333 (1529-30), fr.3019,
   fr.3045, fr.3053, fr.3081, fr.20506, NAF 4206 in detail. Antoine Duprat appears once, as the **recipient**
   of an unrelated 1526 Jean de Calvimont cipher postscript (Clair.325 f.67, solved by Norbert Biermann in
   2021) -- a different item, different volume, and the opposite role (recipient, not the decipherer/author).
   Français 2967 and a Duprat-authored decipherment cluster are not mentioned anywhere on the page. No
   Cipherbrain page found for this item.
5. **DECODE.** Cached catalogue (`unsolved-ciphers/catalogue/decode-catalog.csv`, fresh clone) grepped for
   "2967" and "Duprat": no hit.
6. **Solver repositories.** Fresh shallow clones of `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers`
   grepped for "2967" and "Duprat": no genuine hit (the only "2967" matches are unrelated line-number/CSV-id
   coincidences, already checked and ruled out: `sunyatsen/*.csv` Chinese-character codepoints,
   `bne-ranked.md` an unrelated Spanish catalogue row).

Requests: WebSearch 1 query. archive.org 2 (advancedsearch title queries) + 1 be-api fts query. github.com 2
shallow clones (shared across this worker's six rows). No credentials, no logins.

## Verdict

**Open.** Per QUEUE's own framing this is the M1/M15/M21 "cheap-transcription" pattern -- the items are
already-existing period decipherments, so the live question is whether that plaintext has already been printed
somewhere, not whether it can be cryptanalysed. That question is genuinely unresolved: the one calendar series
most likely to cite it (Catalogue des actes de François Ier) was checked with a single query against a single
volume out of 8-9, a real gap not a negative. Not scored found-solved or closed-negative on this evidence.

`python3 tools/room.py ... "nomination: ciphers/fr2967-duprat | copy-free | recovery | Duprat/Selve/Gedoyn
Calais embassy decipherments; Catalogue des actes de François Ier (8-9 vols, IA) not fully swept, only 1
query/1 vol tried"`
