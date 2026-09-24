blocked

# Three "Lettre chiffrée" items, 1650-1659 -- Bibliothèque de l'Arsenal, Ms-6334

QUEUE row: M24 (sources/solver-diffs/2026-09-24-lane-g2-gallica4.tsv, "Fourth pass, 24 September 2026").

## Source

Bibliothèque de l'Arsenal, **Ms-6334** (191quinquiès. H.F, "Archives des ducs de Longueville, et autres
papiers"), archivesetmanuscrits ark `cc86298x`. QUEUE catalogue note: three separately catalogued "Lettre
chiffrée" items in one Longueville-family recueil -- 7 Jan 1650; 3 Nov 1659, to the duc de Longueville;
undated, Livourne -- no key or decipherment named for any of the three. Fronde/post-Fronde era (Henri II
d'Orléans, duc de Longueville, or his son Charles Paris, depending on exact date).

## Check-solved sweep (24 September 2026)

1. **Web search.** `"Arsenal" "6334" Longueville lettre chiffrée déchiffrement 1650` surfaced catalogue detail
   beyond the QUEUE row's three items: **an encrypted letter from M. de Noyers to the Duke of Longueville
   dated 22 August 1642** (a fourth cipher item in the same volume, not in QUEUE's list) and **"a cipher...
   refreshed in February 1650"** -- i.e. a contemporary key change recorded in the same volume, close in date
   to the 7 Jan 1650 item. Neither detail confirmed at the item-page level this pass (search-summary only);
   both are strong leads for whoever transcribes the volume. No solver/blog claim.
2. **Printed correspondence.** Fronde-era Longueville/Mazarin printed correspondence (e.g. Chéruel's edition of
   Mazarin's letters, or a Longueville-family memoir edition) not searched this pass -- flagged gap.
3. **Calendars/state-paper series.** Not reached.
4. **Cryptiana / Cipherbrain.** No hit for this item. `sources/cryptiana/web/nevers.htm` names a "duchesse DE
   LONGUEVILLE" (Catherine de Gonzague et de Clèves, letter no.34, f.57, to her father the duc de Nevers) --
   confirmed as a **different, unrelated** Longueville: a different generation (1580s vs 1650s), a different
   archive (fr.3995 vs Arsenal 6334), a different circle (League-era Nevers correspondence vs Fronde-era
   Longueville family papers), and that letter is plain, not ciphered. Flagging this explicitly, same
   convention as the Clairambault1225 two-Pagets note, so a future search does not conflate the two. No other
   cryptiana page or Cipherbrain hit.
5. **DECODE.** Cached catalogue (`unsolved-ciphers/catalogue/decode-catalog.csv`, fresh clone) grepped for
   "6334" and "Longueville": no hit.
6. **Solver repositories.** Fresh shallow clones of `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers`
   grepped for "6334" and "Longueville": no genuine hit (the only "6334" matches are unrelated numeric
   coincidences -- `caprile1519/f21_o4.txt` line data, `sunyatsen` CSV codepoints, `unsolved-ciphers/catalogue/
   decode-catalog.csv` row 6334 = an unrelated Florence/1592 DECODE key record -- all checked and ruled out).

Requests: WebSearch 1 query. github.com 2 shallow clones (shared across this worker's six rows). No
gallica.bnf.fr or archivesetmanuscrits.bnf.fr fetches (per brief).

## Verdict

**Open**, and (unlike this worker's other five rows) a genuine cryptanalysis target: no contemporary
decipherment is named for any of the three letters QUEUE lists. Flag before any solving attempt: check the
volume's own reported Feb 1650 cipher "refresh"/key first (a key inside the same physical recueil, close in
date to the 7 Jan 1650 letter, would make this a recovery rather than a cryptanalysis target), and add the
previously-untracked 22 Aug 1642 de Noyers-to-Longueville item as a fourth candidate in the same volume.

`python3 tools/room.py ... "nomination: ciphers/arsenal6334-longueville-1650-59 | copy-free | cryptanalysis |
volume also holds a Feb 1650 cipher refresh/key and an untracked Aug 1642 Noyers-to-Longueville cipher letter
-- check the volume's own key before fresh cryptanalysis"`

## Digitisation check (24 Sept 2026, LANE G2 worker O)

**Digitised: no** (finding aid without DAO; SRU `gallica all "Arsenal Ms-6334"` 607 records, none a
`dc:source` match; 24 Sept 2026). Fetched the archivesetmanuscrits finding aid
(`https://archivesetmanuscrits.bnf.fr/ark:/12148/cc86298x`) in full: `avecDaoGal` is defined in the
stylesheet but applied to no element on this record, and the page carries no `gallica.bnf.fr` href. The SRU
query needed two tunnel-reset retries before a clean response (`ws_closed_mid_exchange`, consistent with the
lane's earlier note that Gallica services endpoints were resetting today); the third attempt returned HTTP 200
and confirmed 0 of 607 hits name Ms-6334. Reservation link is `Cote=Ms-6334&typecote=orig` only, no microfilm
substitute offered. Wrote `REQUEST.md`. Status set to blocked.

Requests this section: archivesetmanuscrits.bnf.fr 1, gallica.bnf.fr 3 (1 SRU success + 2 tunnel resets, one
retry each per the good-citizen rule).
