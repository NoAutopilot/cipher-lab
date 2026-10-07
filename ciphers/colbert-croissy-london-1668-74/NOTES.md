found-solved
Read by this worker on 7 Oct 2026: DECODE RecordsView/2702, /2711 and /2724 (live, no login, HTTP 200, status Decrypted) and the 24 Sept 2026 DECODE decrypted-records listing on disk; Mignet, Négociations relatives à la succession d'Espagne vols 3-4 (IA ngociationsrel03mignuoft, whole-volume grep for "Croissy", 10 hits, read at the text lines named below); Dalrymple, Memoirs vol 1-2 (IA memoirsofgreatbr01dalruoft, memoirsofgreatbr002dalr, grep "Croissy"/"Croissi": 0 hits).

# colbert-croissy-london-1668-74 -- Colbert de Croissy, London embassy, BnF Mélanges de Colbert 149-167, 176bis (NC-CROI, 7 Oct 2026, for LANE NEWT-C-account-4)

Scout row S4-02 (sources/newt-scout/2026-10-06/S4.tsv). Key on disk: ciphers/colbert155-beziers-1670/keys/key_colbert_croissy_1668.tsv.

## Verdict
`found-solved` for the pool as a whole, at the level of DECODE status: 25 of the 72 folios Tomokiyo names as using the Colbert-Croissy
(1668-1674, DE=68) cipher sit inside a DECODE record whose status is **Decrypted** (record owner and creator id 83, created 2021-04-23,
"Available Documents: Key", cipher type "Simple substitution, Nomenclatures", symbols for syllables). The key itself is published
(Tomokiyo, louisxiv0.htm, "Colbert-Croissy Cipher (1668-1674) (DE=68)"), so any further London letter is key application, not a
cryptanalytic target. DECODE's non-decrypted list (24 Sept 2026 file; S1's 6 Oct 2026 re-pull "identical") holds no London letter of
this embassy (its only Colbert rows are 11, 127, 168bis, 172, 500C33).
Who did not know (README F-class): this repo's own scout row S4-02 listed the pool as open; DECODE and Tomokiyo already carried it.

### DECODE status of each Colbert 149-167 record (sources/decode/records-decrypted-2026-09-24.tsv; ids = DECODE record id)
149 f.109 (2702, London, to J.-B. Colbert, 20 Oct 1668, live-read) ; 149 f.457-458 (2703) ; 155 f.132-133 (2704, Béziers, Madrid; already a found-solved folder) ;
158 f.359-362 (2708), f.388-392 (2709) ; 159 f.102-103 (2710), f.203-206 (2711, live-read), f.312-313 (2712) ; 160 p.23-28 (2713), p.57-60 (2714), p.188-195 (2715) ;
161 f.346 (2716), f.371-373 (2717), f.422-423 (2718) ; 162 f.43-45 (2719), f.105-107 (2720) ; 163 f.147-148 (2721), f.412-413 (2722), f.493-495 (2723) ;
164 f.105-106 (2724, live-read) ; 165 f.180-181 (2725), f.277-278 (2726) ; 165bis f.470-480 (2727), f.624-625 (2728), f.731-732 (2729) ;
166 f.23-26 (2730) ; 166bis f.380-381 (2731), f.403-404 (2732) ; 167 f.119-120 (2228) ; 176bis f.646-647 (2735), f.650-651 (2736), f.657-660 (2737), f.669-670 (2738).
Script check (inline, this session): of the 72 folio numbers in Tomokiyo's London list, 25 fall inside a Decrypted record's folio range.

### Residue (no DECODE record found): 47 folios
149: 113, 166, 250, 402, 456, 579 ; 159: 244, 282, 305, 320, 340 ; 160: p.396, 477, 509, 565, 728, 766, 727 ; 164: 303, 444, 447, 545, 627, 629, 667 ;
165bis: 500, 502, 546, 557, 592, 630, 651, 664, 683, 691, 715, 452, 563, 621, 667, 710 ; 166: 27, 30, 46, 128, 145, 335.
Not known whether each carries a contemporary decipherment on the leaf or is a copy/duplicate (Tomokiyo marks 149 f.113, 164 f.444, 166 f.27, 165bis f.710 as copies of letters to Lionne/Seignelay,
164 f.447 "duplicate of the previous?"). Several are duplicates of letters whose original is in a Decrypted record. Tomokiyo does not say these 47 are undeciphered; he lists them as letters "using" the cipher.

## Solver repositories (fresh shallow clones, 7 Oct 2026)
- dbourdeau/cyphersolver: targets/colbert/NOTES.md covers Colbert 127, 168bis, 172 only (Gravel, Charost); it states "None of the published Colbert-office keys of 1665-74 (Millet, d'Estrades, Croissy 1668-74, ...) uses plain three-digit groups above ~316" -- the Croissy 1668-74 key is named as a comparison, not applied to a London letter. Grep for "Colbert 149/158-167", "btv1b100350812", "Croissy" elsewhere: README row (Louis XIV -> Chaulnes 1690, "Croissy design"), sp53 (1584-89 Croissy-office keys, a different Croissy-family key), bethune/chaulnes/feuquieres notes (incidental). Stated next step for London letters: none found.
- aaymeloglu/unsolved-ciphers: catalogue/decode-records.jsonl and decode-catalog.csv are DECODE scrapes (37 rows matching "Colbert 1[456]x"); no reading or working file for any London letter. No licence; nothing copied.
- el-descifrador/cabinet-noir (one commit, last 2 Oct 2026): ~27 files name Croissy, all from Croissy-Mazarin 1660 (Baluze 178 f.73-74), Croissy-Rome 1661 (Baluze 178, 8 letters, readings with "lecture.md"), and beziers-1670 (Colbert 155 f.133r, "première lecture avec clé publiée", 91.7% group / 75.8% word, uses the DE=68 key). Quote (beziers-1670/README.md): "Les 7 dernières lignes (96 groupes) sont chiffrées, sans glose." **No London Croissy letter (149-167) is read in this repository.** It also holds baugy-1616/ (relevant to NC-BAUG, flagged in ROOM).

## Print
- Mignet, Négociations relatives à la succession d'Espagne vols 3-4 (IA ngociationsrel03mignuoft, 3.47 MB djvu): Croissy appears 10 times; only short quotations and footnote references to the dispatches (e.g. the passage beginning "M. Colbert de Croissy, ambassadeur de Louis XIV à Londres, écrivait à sa cour : « On aura beaucoup de peine à contenir les malintentionnés... »" and a footnote citing "Lettre de Louis XIV à M. Colbert de Croissy, du 10 février 1671 [Correspondance d'Angleterre, fol. LXXXVII]"). Not the dispatches in full; no cipher passages printed. Vol 1-2 (ngociationsrel01mignuoft): 1 hit.
- Dalrymple, Memoirs (vols 1-2): 0 Croissy hits. 
- Recueil des instructions données aux ambassadeurs, Angleterre (Jusserand, 1929): prints instructions to Croissy, not his dispatches (per Britannica 1911/encyclopedic summaries read in search results; the volume itself not opened this pass -- listed under "not reached").
- Google Books (country=US, key): q "Colbert de Croissy dépêche chiffre Londres 1672" -> 2 volumes, none a printed London dispatch edition; "Copie de la lettre de Monsr. le marquis Croissy, ambassadeur de France" (1715, NO_PAGES) and "Lettres et negociations de messieurs le Marechal d'Estrades, Colbert, ..." (1710, NO_PAGES; Nijmegen 1675-78) noted but not opened (not London 1668-74). Second query: 0 hits.
- BnF Fonds français 10664-5 hold copies of Croissy's London letters to Louis XIV and Lionne, Sept 1668-Oct 1669 (NLI catalogue record MS UR 021286 via search result): a second copy series in the same archive, not examined.

## Web and blog check (NC-CROI worker, 7 Oct 2026)
Queries: (1) "Colbert de Croissy London 1668 cipher dispatches deciphered ... Melanges de Colbert" -> Wikipedia, NLI MS UR 021286, Pepys Diary, 1911 EB; no decipherment. (2) "Croissy ambassadeur Londres 1668 1674 dépêches imprimées Mignet ..." -> same set; points to Mignet vol iv. and the Recueil des instructions. (3) '"Colbert 164" OR "Colbert 159" Croissy cipher decrypted DECODE Tomokiyo London 1672' -> TNA blog "secret diplomatic message deciphered after 350 years" (a different cipher: the 1670s Colbert/Charles II column cipher by Brown, Lasry, Biermann, Tomokiyo; not this key). (4) "Cipher Mysteries OR Cryptiana OR Cipherbrain Colbert-Croissy cipher 1668-1674 London" -> no hit. Site searches (allowed_domains ciphermysteries.com, cryptiana.blogspot.com, cryptiana.web.fc2.com, scienceblogs.de): hits were cryptiana.blogspot.com/2026 (index) and scienceblogs.de "Can you decipher this letter written by Louis XIV?" (31 Jan 2019); neither opened in full (not the London letters by title) -- comment threads NOT opened, so this part is thin. Model-solve family ("solves" + "Claude"/"GPT"): not run.
Tomokiyo, verbatim (louisxiv0.htm): "This cipher is used in many letters in Melanges de Colbert 149 ..., f.109, f.113 (copy of a letter to Lionne), f.166, f.250, ..." -- he does not call these letters undeciphered; the only one he calls undeciphered is the Béziers letter (Colbert 155), already found-solved on DECODE 2704.

## Premise check (NC-CROI worker, 7 Oct 2026)
(a) the folder's own mentions: S4-02 itself says "Check DECODE status of these Colbert records first (colbert155 was Decrypted) - a Decrypted record is a near miss for that letter" -- found: 25 of 72 folios Decrypted (above). colbert155-beziers-1670 NOTES found-solved on DECODE 2704.
(b) other solvers' working files: cabinet-noir has run the DE=68 key on one letter (Béziers); no London letter; cyphersolver and unsolved-ciphers none. Found only that the key has been run on a sibling letter at 75.8% word-level.
(c) physical neighbours: NOT DONE. Gallica manifest for Colbert 164 (btv1b100350812, 720 canvases) carries no folio labels (tools/gallica_folio.py: "0 with a folio label"), so locating f.303 etc. needs eye-checked anchors; no image was viewed.
(d) recipient's side: the addressees are Louis XIV, Lionne, J.-B. Colbert and Seignelay (French offices); the English side (Calendar of State Papers Domestic 1668-74, Arlington's papers) is not a recipient edition for these dispatches; not searched. Not found/unreachable.

## NC-CROI2 (7 Oct 2026)
Job: classify the 47 residue folios (a copy / b contemporary decipherment on the leaf / c cipher, no decipherment / d not cipher or mislocated). Method: Gallica IIIF low-res, one look each (~37 canvases viewed, 6 volumes, 5 of 6 volumes touched at 164/149/159/165bis; 160 NOT looked at; 166 sampled at c40, 48, 60, 70, 150, 165, 350, 360 -- all clear text, Calais/Brittany correspondents, ties to f.27/30/46/128/145/335 unconfirmed). No manifest carries folio labels (all 'NP'); folio numbers stamped top right were read by eye and are only partly legible at 600-700 px, so canvas-to-folio ties are +-2 canvases except where a number was read.
Result: **not a full classification.** 47 folios were not each located; the table lists what was seen. Verdict line 1 unchanged: `found-solved`.

| vol | canvas (folio tie) | what the leaf shows | class |
|---|---|---|---|
| 149 | c188 (~f.113, copy to Lionne?) | ~18 lines digit cipher, Colbert signature, interlinear gloss | (b) (copy, glossed) |
| 149 | c397 (29 Oct 1668, not a listed folio) | ~18 lines digits, interlinear gloss | (b), outside the 47 |
| 149 | c267 = f.166 (number read) | clear text on this side; cipher, if any, on the next side not viewed | unresolved |
| 149 | c640 = f.406, c644 = f.408 | clear (f.402 ~c636 not viewed) | unresolved |
| 149 | c189-193 (f.115-118, number read "116") | a letter dated Lisbon 20 Oct 1668 (not London): ~17 lines + ~6 lines letter-and-digit symbols, NO gloss on the leaf | (c)/(d): unglossed, ~370 groups, different hand/sender and a letter-form symbol set not checked against the DE=68 key; not one of the 47 (neighbour, f.115-118) |
| 159 | c325 (~f.320) | ~6 lines digits, interlinear gloss | (b) |
| 159 | c246, c284, c310, c345, c355 | clear on the sides viewed | unresolved (ids unconfirmed) |
| 164 | c315 (~f.303; c313 = f.301, c316 = f.304 read) | ~5 lines digits, interlinear gloss | (b) |
| 164 | c456 (~f.444, "Copie de la lettre ... Seignelay" 12 Juin 1673) | ~5 lines digits, interlinear gloss; text duplicates c459 | (a)+(b) |
| 164 | c459 (~f.447) | clear duplicate text of c456 | (a) |
| 164 | c560 (~f.545) | cipher lines mid-page, gloss not made out | unresolved |
| 164 | c642 (~f.627), c644 (~f.629, number read 629) | 2 blocks / ~4 lines digits, interlinear gloss | (b), (b) |
| 164 | c682 | clear (f.667 ~c683 not viewed) | unresolved |
| 165bis | c210 (~f.5xx-6xx, number illegible) | ~40 lines digits, interlinear gloss | (b) |
| 165bis | c70, c140, c280 (~f.541, ~f.6xx, ~f.683, "Nancy 20 7bre 1673") | clear on the sides viewed | unresolved |
Counts of the 47: located and seen cipher with gloss (b) about 6-7; copy (a) 1-2; (c) 0 among the 47; (d) 0; the rest (about 38) unlocated or seen only clear. Pattern, stated as observation not a result: in this pool the clerks' interlinear gloss is usual where the cipher is a few lines to a page; the one gloss-free cipher seen is the Lisbon letter at f.115-118, not a London dispatch and not on the list.
Estimate of residue (c) from the leaf look: 0 letters among the 47 seen; at most ~370 groups (Lisbon, outside the 47). Gate (>= 2 letters or >= 1,500 groups) NOT met on what was seen, but 38 folios were not seen, so this is "not shown", not "absent".
Decision: keep `found-solved`; spec NOT written (partial not triggered). Reason: every cipher passage seen in the pool carries its own period gloss or is a copy, and no unglossed London letter was located.
Caveats: (1) status stays tied to DECODE Decrypted for 25/72 folios, the rest rests on this sample only; (2) a fuller pass needs per-volume folio anchors (about 1 USD per volume) and a look at both sides of each target folio; 160 (7 folios) untouched and 166 (6) only sampled; (3) the Lisbon letter at 149 f.115-118 is worth a one-line check against DECODE/Tomokiyo before anyone calls the pool exhausted.
Requests: Gallica ~85 images (1.6 s apart, 2 connection resets, one retry each), no other host.

## While waiting
Nothing is waiting: verdict is found-solved. The one action that depends on nobody, if the pool is ever revisited: for each of the 47 residue folios, anchor the Colbert 149/159/160/164/165bis/166 canvases by eye (gallica_folio.py --anchor) and see whether a contemporary decipherment is written on the leaf or a Decrypted sibling holds the original (several are copies). ~$1 per volume, not requested.

## Intake gate
(pasted below)

```
colbert-croissy-london-1668-74: found-solved (line 1) -- edition/page or full-text-search citation found within 6 lines
exit 0
```
