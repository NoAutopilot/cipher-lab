blocked

# D'Allion - Lanmary correspondence, "en grande partie chiffrée" -- Bibliothèque de l'Arsenal Ms-4764 and Ms-11639

QUEUE row: M25 (`sources/solver-diffs/2026-09-24-lane-g2-gallica4.tsv`, LANE G2 worker F's archivesetmanuscrits
item-level sweep).

## Source

Two Arsenal witnesses of the same diplomatic circle (D'Allion, French chargé d'affaires/minister in Russia and
Sweden -- Lanmary, ambassador in Sweden), 1744-1746:

- **Ms-4764** (635 H.F, "Recueil concernant les relations de la France avec la Suède"), `ark:/12148/cc85044f`.
  Names one specific dated item: "Dépêche chiffrée, signée Lanmary, adressée à d'Alion, Stockholm 9/20 août
  1745".
- **Ms-11409-12471 "Archives de la Bastille"** (Ms-11639, "Papiers divers"), `ark:/12148/cc12947k`. Describes
  the whole 1744-46 run as "en grande partie chiffrée" between the two men, alongside plain letters of
  credence and treaty copies.

Per the brief, gallica.bnf.fr and archivesetmanuscrits.bnf.fr were not fetched this pass; catalogue text is
the QUEUE row's own harvest text, no image viewed, no item page opened.

## Check-solved sweep (24 September 2026)

1. **Search engine.** `D'Allion Lanmary Suède 1744 1745 1746 correspondance chiffrée` and `Lanmary ambassadeur
   Suède correspondance imprimée archive.org OR gallica` -- both surfaced only the BnF Archives et manuscrits
   notices themselves (`cc12947k`) plus unrelated hits (Wikipedia's "List of ambassadors of France to Sweden",
   "1745 in Sweden", "1744 in France", a Voltaire bibliography, an unrelated Graffigny correspondence volume).
   No cipher blog, forum, or scholarly discussion of this correspondence found.
2. **Printed correspondence / calendars.** No dedicated printed edition of Lanmary's or d'Allion's
   correspondence located this pass (a full check of France-Sweden diplomatic-history calendars, e.g. a
   Recueil des instructions volume for Sweden, was not run -- budget-limited, flagged as the next step for
   whoever returns to this row).
3. **Cryptiana.** Local snapshot grepped for "Arsenal", "d'Allion", "dallion", "Lanmary": no hit beyond the
   unrelated generic "Arsenal" library mentions already noted for M22.
4. **Cipherbrain.** No dedicated query run for this row specifically (the M22 query's date range 1708/1713/1745
   covers this correspondence's years and returned no hit for any Arsenal item).
5. **DECODE.** Aymeloglu's cached `catalogue/decode-catalog.csv` (10,107 rows) grepped for "arsenal",
   "allion", "lanmary": zero hits for any. This repo's own local harvest
   (`sources/decode/records-non-decrypted-2026-09-24.tsv`) also has no matching row.
6. **Solver repositories.** Fresh shallow clones of both repos grepped for the shelfmarks ("Ms-4764",
   "Arsenal 4764", "Ms-11639", "Arsenal 11639") and both arks (`cc85044f`, `cc12947k`) exactly: zero matches in
   either repo. (The bare numbers "4764"/"11639" coincidentally appear in dozens of unrelated files in both
   repos -- e.g. `zeschau1841/ct_R5005.txt`, `bethune/em_model.json` -- none of them this item.)

## Verdict

**Open, stage 2 verified unsolved (conditional).** Not found in a search engine, Cryptiana, DECODE's cached
catalogue, or either solver repository, searched by shelfmark and ark on 24 Sept 2026. Conditional because:
(a) the France-Sweden diplomatic calendar/edition series (a Recueil des instructions volume, if one exists for
this window) was not checked this pass; (b) the QUEUE row's own open caveat stands unresolved -- Ms-4764 and
the Ms-11639 Bastille volume may describe the same underlying correspondence read from two different registers
(sender's letter-book vs. recipient's file) rather than two independent witnesses, not settled by this sweep.

Requests: WebSearch 2 queries. github.com 0 new (reused the M22 clones). No gallica.bnf.fr, no
archivesetmanuscrits.bnf.fr fetch. No subagents.

## Digitisation check (24 Sept 2026, LANE G2 worker O)

**Digitised: no**, both witnesses.

- **Ms-4764** (`ark:/12148/cc85044f`): finding aid's `avecDaoGal` marker applied to no element, no
  `gallica.bnf.fr` href on the page. SRU `gallica all "Arsenal Ms-4764"` (0 of 1179 hits' `dc:source` name
  Ms-4764) confirms it. Reservation link `Cote=Ms-4764&typecote=orig` only, no microfilm substitute.
- **Ms-11639** (`ark:/12148/cc12947k` -- this ark resolves to the whole "C. Dossiers des prisonniers, Ms-11409
  à 12471" finding aid, not a page scoped to Ms-11639 alone; Ms-11639 "Papiers divers" is one sub-item in it,
  containing our target's "correspondance...entre d'Allion et Lanmary" alongside an unrelated "Papiers
  particuliers du comte de Sade"). No `avecDaoGal` use and no `gallica.bnf.fr` href anywhere on the whole
  297 KB page (i.e. across the entire Ms-11409-12471 run, not just this sub-item). SRU `gallica all "Arsenal
  Ms-11639"` (0 of 293 hits' `dc:source` name Ms-11639) confirms it. No reservation section was present on
  this page at all (the ark serves a series-level description, not an individually reservable item page) --
  a future worker would need the item-level page (unresolved this pass) or a direct enquiry to establish the
  original's own reservation cote.

Wrote `REQUEST.md`. Status set to blocked.

Requests this section: archivesetmanuscrits.bnf.fr 2 (cc85044f, cc12947k), gallica.bnf.fr 2 SRU queries (both
200 first try).

## While waiting (27 Sept 2026, WAIT-PASS-A)

Waits on a BnF Arsenal reading-room visit or reproduction enquiry for Ms-4764 and Ms-11639 (REQUEST.md,
"waiting on you"), since 24 Sept 2026.

- Full-text search a Recueil des instructions volume for Sweden 1744-46 on archive.org/Google Books -- the printed-edition leg the check-solved sweep flagged as unrun. S, tools/print_check.py.
- Re-read Ms-11639's finding-aid text to settle whether it and Ms-4764 describe the same correspondence from two registers (the open caveat in NOTES's own verdict) -- a closer catalogue read, no image needed. S.
- Run OpenAlex/Semantic Scholar (keys already set) for "d'Allion"/"Lanmary" Sweden 1744-46 diplomatic scholarship, not yet tried beyond plain web search. S, tools/print_check.py.

## Edition search: Recueil des instructions, Sweden/Russia legs (D2-ARSDAL, 6 Oct 2026, 00:00-00:08 UTC by date -u)

Search results only (rule 10); no novelty class. Hosts: archive.org advancedsearch/metadata/download 14 requests, Google Books API
(`country=US`, key) 9 requests, be-api fts 1; no blocks.

- **IA, Recueil des instructions (Commission des archives diplomatiques, 1884-90).** The Sweden volume (t. II, Geffroy, 1885) was not found by
  title/creator queries on IA (0 hits). `_djvu.txt` of `recueildesinstr02diplgoog`, `recueildesinstr00diplgoog`, `recueildesinstr02frangoog` and
  `recueildesinstr03diplgoog` (volumes labelled 7, 14, 3/30, 3; none of them Sweden) grepped for Lanmary/Allion/Dallion: 0 real hits (OCR noise only).
- **IA, `sc_0000914511_00000001011417` (Recueil t. VIII, Russie 1, to 1748, 1890), full text read by grep:** the printed series carries
  *Instruction* to d'Usson Dallion (Versailles, 21 June 1742) and *Instructions à M. d'Alion, 1744* (Châlons-sur-Marne, 1 Aug 1744; "deuxième mission
  1744-1747", Russia), with the editor's notes naming Lanmary as French ambassador at Stockholm, and a passage on the tables de chiffre sent to the
  minister ("articles de ses lettres qu'il pourroit être dangereux de confier en clair"). Edition p. 467-468 range; also notes on La Chétardie's cipher
  being read by the Russians. So the Russian leg of the same circle is in print as *instructions*; no printed text of a Lanmary-d'Alion cipher
  dispatch (incl. Stockholm 9/20 Aug 1745) found in it.
- **Google Books API:** Sweden volume exists in full view (ids `BuoJAAAAIAAJ`, `hGWs91_CP1AC`, `rWTEx4RWum4C`, `kWJGVsgSpgIC`, `qgbSAAAAMAAJ`, `TxQjZ8_2ow0C`
  is a 1888 volume with a Lanmary/Alion footnote). The API only returns a snippet per query and cannot search inside one volume;
  books.google.com page/text view is blocked from the cloud (host table). Therefore the Sweden volume's text was NOT read for Alion/chiffre/1745:
  untested, not a negative.
- Other print leads from snippets (not opened): Zevort, *Le marquis d'Argenson et le Ministère des affaires étrangères* (1880; `XisxAQAAIAAJ`, d'Alion,
  Lanmary); Karge, *Die russisch-österreichische Allianz von 1746* (1887; `hLSB-hSQwqEC`, "Alion, Lanmary" Woronzow-Archiv);
  Mézin, *Correspondance des consuls de France à Saint-Pétersbourg 1713-1792* (2009; `emtFAQAAIAAJ`, NO_PAGES): a calendar entry "Lanmary dès le départ
  de d'Alion ... Lettre chiffrée" (Jan 1748, F° 356), i.e. a modern calendar that summarises ciphered Lanmary/Alion letters. Not read beyond the snippet.
- Not found: any hit naming Ms-4764/Ms-11639 or the 9/20 Aug 1745 dépêche chiffrée in the series text read.

Next (S, ~USD 1): read Recueil t. II Suède intro/notes on a loan-free full view (Google Books ids above via a person, or IA if a copy is uploaded) for
Alion; locate Mézin 2009 entries 1744-47 for the Arsenal shelfmarks (LOCAL-QUEUE row if only a person can open it).
