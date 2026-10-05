blocked

Read by this worker 3 Oct 2026: Martin, Catalogue des manuscrits de la Bibliothèque de l'Arsenal vol.6 (1892; IA cataloguedesman06bibl, OCR) entry for Ms-6334 items 8-29, and Chéruel, Lettres du cardinal Mazarin vols 3 and 9 (IA lettresducardina03maza, ...09maza, OCR) searched by Longueville, d'Alemont, Noyers, Livourne and the cipher letters' dates: no decipherment, key or plaintext of any Ms-6334 cipher letter found; blocked because the leaves are not online (finding aid https://archivesetmanuscrits.bnf.fr/ark:/12148/cc86298x, 200 on 3 Oct 2026, offers only Cote=Ms-6334 original reservation, no DAO/Gallica link).

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

## Web and blog check (CS-A2-L, 3 Oct 2026)

Queries (WebSearch, standard): (1) `Longueville "lettre chiffrée" 7 janvier 1650 Arsenal Ms-6334 déchiffrement`; (2) `"Arsenal" "6334" Longueville chiffre cipher letter 1659 d'Alemont`; (3) `duc de Longueville Noyers 22 août 1642 lettre chiffrée Livourne 26 septembre cipher decipherment`; (4) `Longueville Fronde cipher Cryptiana OR Cipherbrain OR "Cipher Mysteries" Arsenal Longueville chiffre`; (5) site-limited ciphermysteries.com `Longueville cipher letter Arsenal`.
Blog site searches: Cipherbrain (scienceblogs.de/klausis-krypto-kolumne/?s=Longueville and `Arsenal 6334`): "keine Beiträge" for both. Cryptiana blog (cryptiana.blogspot.com/search?q=Longueville and `Arsenal 6334`): "No posts matching" for both. Cipher Mysteries: its own ?s= search answered HTTP 406 to curl (not retried), so only the site-limited web search above was possible: no Longueville hit.
Hits opened: Biermann's Cipherbrain post (Louvois/Lauzun 1690, BnF fr.6204): no Longueville/Arsenal/Fronde mention, no comments. Lasry, "Armand de Bourbon's Poly-Homophonic Cipher - 1649" (HistoCrypt 2023): Conti to La Tremoille-Noirmoutier, 26-27 March 1649, no shelfmark on the abstract page, no Arsenal/Longueville mention. CCFr record Troyes Ms 2236 "Copies de lettres de et à Mme la duchesse de Longueville, 1650-1669": no cipher mention.
Other checks: Google Books (country=US, key): `"d'Alemont" Longueville duchesse 1659` -> 3 items, all Arsenal catalogues (1885, 1892 x2), no snippet text; `"Ms 6334" Arsenal Longueville` -> 1 item, unrelated 1982 Boüard volume. IA full text (be-api): `"duc de Longueville" "Arsenal" "6334"` 10 hits, all the Martin catalogue / unrelated inventories; `"M. d'Alemont" Longueville chiffre` 1 hit (Martin catalogue vol.6). Solver repositories, fresh shallow clones (grep only): dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers searched for longueville, alemont and `Ms-6334`/arsenal near 6334: every Longueville hit is the 1590s Nevers circle (nevers.htm, notice_4715, pieces_3977), not this volume; Bourdeau's repository has no Ms-6334 target (our own sources/solver-diffs 2026-10-02 and 10-03 rows say the same). DECODE (login-free tools/decode_list.py, 1,186 rows non-decrypted + partially-decrypted ciphers, 25 requests): no row naming Arsenal, Longueville or 6334; no Fronde-era Arsenal row. Cached catalogue row 6334 is a Florence 1592 record (unrelated).
Requests: de-crypt.org 25; archive.org 11 (be-api 12 fts calls incl. per-volume, 5 djvu downloads, 3 advancedsearch); archivesetmanuscrits.bnf.fr 1; scienceblogs.de 2; ciphermysteries.com 2 (406); cryptiana.blogspot.com 2; github.com 2 clones; googleapis 2; WebSearch 5; WebFetch 3.

## Premise check (CS-A2-L, 3 Oct 2026)

(a) Folder's own mentions: **found, corrected.** The 24 Sept note's "cipher refreshed in February 1650" and "Aug 1642 de Noyers cipher letter" came from a search summary. Re-read against the finding aid and Martin's catalogue (items 9, 10, 19, 23, 29): the 22 Aug 1642 de Noyers letter (fol.17) is catalogued "autographe", not as cipher, and **no February 1650 refresh/key item appears in either catalogue**; the Feb 1650 claim is unconfirmed and should not be cited as a key inside the volume. The four cipher entries are fol.18 (7 Jan 1650), fol.30 (two unsigned letters to "M. d'Alemont, prez de S. A. la duchesse de Longueville", one undated, one 30 Aug 1659), fol.38 (3 Nov 1659, unsigned, to the duc de Longueville), fol.51 (Livourne, 26 September, no year): five cipher letters on four leaves. Neither catalogue mentions a decipherment, interlinear or clear copy.
(b) Other solvers' working files: **not found.** No Ms-6334 file in either repository (see above). Related, not this item: Lasry's Conti 1649 poly-homophonic cipher (Fronde, same family circle, key family unknown to be shared) is a candidate cipher-design prior only.
(c) Physical neighbours / facing pages: **unreachable.** No images online (finding aid has no DAO; original-reservation only), so no leaf, facing page or pasted slip could be viewed. Fol.17-20 and fol.29-40 neighbours are plain royal and secretarial letters per Martin.
(d) Recipient/sender-side editions: **not found in what was readable.** Chéruel's Mazarin vols 3 (1648-50) and 9 (1658-61) full text: no letter dated 7 Jan 1650, 30 Aug or 3 Nov 1659 addressed to or about these cipher items found; vol.9 prints Mazarin letters to Longueville (27 Jan 1659; 25 Sept 1659 index entry) in clear, none flagged as deciphered from a Longueville cipher. OCR date matching is noisy; a "no match" here is a search result. Leads not opened: Troyes Médiathèque Ms 2236 (copies of letters of/to the duchess 1650-1669), may hold plain texts for the 1659 letters (CCFr ark:/16871/004D02B13030); Chéruel vols 4-7 not grepped by date; the senders of the unsigned letters are unknown.

## Verdict (CS-A2-L, 3 Oct 2026)

Not found solved or deciphered in any source above (found where: none; not found in: the sources listed, searched 3 Oct 2026). Status stays `blocked`: the only unread piece is the images, which need a reading-room visit (REQUEST.md); not a novelty statement. While waiting: open Troyes Ms 2236 via CCFr/Calames for plain copies of the 1659 letters (no one else's reply needed), and grep Chéruel vols 4-7 by date.


## fr17 re-judge (FR17-RJ2, 3 Oct 2026)

No reading on disk -- no ciphertext or reading: status blocked (REQUEST.md). No judge run (fr16 or fr17), no shuffled-decode control, no per-fold rate at a reading's N; the fr17 per-fold rates at N=138/300 are in tools/data/fr17/README.md.

## Next step (NO-CRACKS, 5 Oct 2026)

next: open Troyes Ms 2236 via CCFr/Calames for plain copies of the 1659 letters (depends on nobody), ~$1; the images themselves stay with the BnF Arsenal quote batch (ASKS 38, REQUEST.md). Who acts: agent. Source: this file's "Verdict (CS-A2-L, 3 Oct 2026)" While-waiting sentence; written by NO-CRACKS (account 3) because tools/next_steps.py found no next-step line in this file.
