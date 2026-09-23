found-solved

# Orange-Nassau 1572

## Source

- G. Groen van Prinsterer (ed.), *Archives ou correspondance inédite de la maison
  d'Orange-Nassau*, 1re série, **tome III** (not tome IV -- see "Edition risk" below;
  Leiden, 1836), Lettre CCCLXXXV, pp. 501-510: William of Orange to Count Jean (Jan
  VI) of Nassau, dated Malines (Mechelen), 21 September 1572, with a postscript.
  Numeral cipher figures on pp. 502-503, 506-507 and 509. Editor's footnote (p.502
  n.1, printed at the foot of p.503): "Il est à regretter qu'une comparaison
  attentive des passages suivants avec d'autres pièces dont nous possédons le
  déchiffrement, n'ait conduit à aucun résultat. On s'est convaincu que les chiffres
  y étant infiniment plus nombreux que les lettres, il sera très difficile, si non
  décidément impossible, de retrouver le sens."
- Internet Archive identifier `archivesoucorre04housgoog` (Google-digitised scan);
  cached OCR at `sources/ia-fulltext/archivesoucorre04housgoog_djvu.txt`, lines
  24010-24378.
- Clean modern transcription: DBNL,
  https://www.dbnl.org/tekst/groe009arch03_01/groe009arch03_01_0159.php (confirms
  page 501, tome III, and the footnote text verbatim).
- Autograph original: Koninklijk Huisarchief Den Haag, A 3, 895/I, imaged in full
  (9 leaves) at https://resources.huygens.knaw.nl/media/wvo/images/05000-05999/05198.pdf
  via the Huygens Institute "Correspondentie van Willem van Oranje" database, record
  https://resources.huygens.knaw.nl/wvo/app/brief?nr=5198 (briefnr. 5198).
- `ciphertext.txt` (OCR, verbatim, page-marked, with the manuscript/DBNL cross-check
  noted); `images/manifest.json` (3 IA page images: pp.501/503/506; 2 KHA manuscript
  leaves: opening and a heavily-ciphered page).

## Check-solved sweep (23 September 2026)

Six sources, per CLAUDE.md rule 1. This target reached the queue via the printed-
ciphertext detector test of 23 Sept 2026 (`sources/ia-fulltext/NOTES.md`), which
flagged it as a candidate (cipher present, no decipherment visible on the page,
absent from `sources/cryptiana/` and both solver-repo clones by simple keyword
grep) but explicitly deferred a stage-2 verdict to a check-solved sweep. This is
that sweep.

1. **Web search engine.** `Groen van Prinsterer Archives correspondance
   Orange-Nassau "Comte Jean de Nassau" 1572 chiffre déchiffrement` and
   `Huygens ING "Correspondentie Willem van Oranje" 1572 Jan van Nassau cijfer
   Malines` (WebSearch tool). Surfaced DBNL's digitised edition of the *Archives*
   and the Huygens Institute's "Correspondentie van Willem van Oranje" database
   (successor project to the "Briefwisseling van Willem van Oranje" named in the
   brief) as the two live leads followed up below.

2. **Sender's/recipient's printed correspondence and calendars (editions first).**
   - DBNL (`dbnl.org`) hosts the full Groen van Prinsterer *Archives*, all series,
     as a clean re-transcription with page images. Located the exact page
     (`groe009arch03_01_0159.php`) and confirmed: **this letter is in tome III
     (1567-1572), not tome IV** -- see "Edition risk" below. DBNL's text of the
     footnote matches the 1836 print exactly; no later editorial correction or
     "solved since" annotation is attached to it on DBNL (DBNL republishes the 1836
     text as-is, it does not re-edit it).
   - Checked for a later Groen supplément (1847) or a 2nd edition of this volume
     specifically re-visiting the cipher: none found by search; the 1841 2nd
     edition Groen produced was of **tome I** only ("Deel I is met wijzigingen en
     aanvullingen herdrukt (Leiden 1841)", per the Huygens database's own citation
     of the edition), not tome III, so no 2nd-edition correction of this letter
     exists to check.
   - Searched for the 1984 scholarly edition *De correspondentie tussen Willem van
     Oranje en Jan van Nassau* (Nederlandse historische bronnen, deel 4): the only
     edition confirmed by this search is J.H. Kluiver's edition, reviewed in *Revue
     belge de philologie et d'histoire* 67 (1989), which covers **1578-1584** only
     (https://www.persee.fr/doc/rbph_0035-0818_1989_num_67_4_5735_t1_0860_0000_2) --
     six years after our letter, so it cannot bear on this item. Whether a separate,
     earlier-period Kluiver/Nederlandse-historische-bronnen volume exists covering
     1572-1578 was not established either way this sweep (not searched exhaustively;
     flagged as a loose end, not as a source that was checked and came back empty).

3. **Comment threads (Cryptiana blog, Cipherbrain) / Tomokiyo.**
   `sources/cryptiana/` grepped for "Nassau", "Orange", "Oranje", "Groen",
   "Prinsterer", "Malines": all hits are either the wrong period (Tomokiyo's
   `dutch.htm` covers 1780s-1802 Orange-Nassau ciphers -- William V/the Hereditary
   Prince era, over two centuries later) or unrelated uses of "Orange"/"Nassau" as
   place/family names in other articles (`habsburg.htm`'s 1519 Nassau-to-Margaret-
   of-Austria cipher is a different, earlier letter to a different correspondent).
   No hit for "Nepveu" anywhere in `sources/cryptiana/`. Tomokiyo's site does not
   cover this letter or this cipher.

4. **DECODE (de-crypt.org) cached catalogue** (`ay/catalogue/decode-*.jsonl|csv`,
   no login used, per this session's no-logins instruction). Searched "Nassau",
   "Oranje", "Orange", "1572", "Groen": the only 1572 hits are unrelated English
   items (BL Harley MS 260, Walsingham/Burghley correspondence) and unrelated
   Italian ciphers (ASFi); the only Orange-Nassau hits are 1795-1804 items (KHA
   Prins Willem V/Koning Willem I, the Napoleonic-era Hereditary Prince
   correspondence already being worked in `cs-recheck/fagel1804/`,
   `r1892/`, `r2232/`, `r2242/`). No DECODE record for this 1572 letter or its
   cipher.

5. **dbourdeau/cyphersolver.** Fresh grep of the scratchpad clone (`cs-recheck/`)
   for "Nassau", "Orange", "Groen", "Prinsterer", "Nepveu": all "Nassau" hits are
   either the 1795-1804 Orange-Nassau items already in the catalogue (`CATALOGUE.md`
   lines 136/153/256, `SOLVED_CATALOGUE.md` items 69/79/88) or incidental uses in
   unrelated targets (Rohan-Valtellina report, Napoleon-era French texts). No hit
   for this letter, this tome, or "Nepveu".

6. **aaymeloglu/unsolved-ciphers.** Fresh grep of the scratchpad clone (`ay/`) for
   the same terms: the only "Nassau" hits are the same 1795-1799 KHA
   Orange-Nassau items in `decode-records.jsonl`/`decode-catalog.csv` (mirrored
   from DECODE, not independent), plus one 1580s PARES catalogue snippet about
   William the Silent's health (unrelated to this letter or its cipher). No hit for
   "Nepveu" or this letter.

## The finding

The **Huygens Institute's "Correspondentie van Willem van Oranje" database**
(https://resources.huygens.knaw.nl/wvo, the modern successor project referenced by
its older name "Briefwisseling van Willem van Oranje" in the check-solved brief)
catalogues this exact letter as **briefnummer 5198** (searched by sender/recipient
"Jan van Nassau" + place "Mechelen (Malines)"; 3 results, of which 5198 matches the
date 21-9-1572 and the incipit "Les empeschements continuelz de ce mien present
voiage ensemble et la difficulté" verbatim). Its "Opmerkingen" (remarks) field
states, quoted in full:

> "Met een postscriptum. Ten dele in cijferschrift. De gedeeltelijke editie van
> Nepveu tot Ameyde, die ook is afgebeeld, biedt de oplossing daarvan."
>
> ["With a postscript. Partly in cipher-writing. The partial edition of Nepveu tot
> Ameyde ... offers its solution."]

and its source table cites, verbatim:

> Nepveu tot Ameyde, L.J., ['Cijferschrift in de Archives de la Maison
> d'Orange-Nassau'], *Algemeene Konst- en Letterbode* 1 (1842), 18-22.
> (page reference for this letter: "19-20 (onv.)" -- onvolledig, i.e. incomplete)

**L.J. Nepveu tot Ameyde published a partial decipherment of this cipher in 1842**,
six years after Groen's 1836 edition called it "décidément impossible" -- in a
Dutch general-interest periodical, *Algemeene Konst- en Letterbode*, vol. 1 (1842),
pp. 18-22, with the solution itself on pp. 19-20 and marked by the Huygens database
as incomplete/partial.

This 1842 publication is **not indexed anywhere this sweep could reach**: not in
`sources/cryptiana/`, not in a fresh clone of either solver repository, not in the
DECODE cached catalogue. It was found only because the Huygens Institute's
correspondence database -- a scholarly finding aid for the sender's and recipient's
correspondence, source family (2) in the brief -- catalogues it. This is exactly
the kind of source the six-source sweep exists to catch that a keyword grep of
"Groen"/"Prinsterer"/"Orange-Nassau" against the solver repos and cryptiana (as the
detector test did) would miss, because "Nepveu tot Ameyde" is not a name that
search would surface.

**Not done this sweep** (next steps, not a source checked and come back empty):
locating and reading the actual text of Nepveu tot Ameyde 1842 pp.18-22, to see how
much of the cipher he broke, what the recovered plaintext says, and whether a key
survives from his working. DBNL's digitised run of *Algemene konst- en letterbode*
(`dbnl.org/tekst/_alg004alge00_01/`) did not show an 1842 volume in its available-
years listing on this pass -- try Delpher.nl (the KB's Dutch newspapers/periodicals
portal), Google Books, or a direct KB catalogue request next.

## Edition risk

QUEUE.md's detector-test row (P1) abbreviated the volume as "1re série, t. IV" and
the printed range as "pp. 501-506". Both are corrected here:

- **Tome, not IV but III** (1567-1572, not 1572-1574). Confirmed two independent
  ways: (a) DBNL's own edition of tome III lists this exact letter, page and title
  (`groe009arch03_01_0159.php`); DBNL's tome IV table of contents starts at Lettre
  CCCLXXXIX (389), i.e. tome IV does not contain letter 385 at all. (b) The Huygens
  WvO database's own source citation reads "Archives d'Orange-Nassau III, 501-510
  nr. CCCLXXXV" verbatim.
- **Page range 501-510, not 501-506.** The letter's ciphertext does not stop at
  p.506: cipher-numeral runs recur on p.507 and again on p.509 (see `ciphertext.txt`,
  which now transcribes the full letter through its closing "Escrit à Malines, ce 21
  de septembre 1572" and signature block). The detector test's OCR-line range
  (24100-24227) captured only the first, longest cluster (pp.502-506); this sweep's
  extraction (OCR lines 24010-24378) covers the whole letter.

Neither correction changes the verdict; both matter for anyone using QUEUE.md's row
to relocate the item without re-deriving the tome and page range from scratch.

## Verdict

**found-solved** (partial). A prior decipherment of this cipher exists in print:
L.J. Nepveu tot Ameyde, *Algemeene Konst- en Letterbode* 1 (1842), pp. 18-22
(solution on pp. 19-20, incomplete), as catalogued by the Huygens Institute's
"Correspondentie van Willem van Oranje" database (briefnr. 5198). This target is
not promoted to the board as an open cryptanalysis/recovery candidate. Rule 10
applies: this note does not say "new", "unpublished" or "first" -- it says a prior
decipherment was found, where, and that it is incomplete by the cataloguing
database's own description; no verifier N-class is being claimed or needed here,
since this is a "found-solved" catalogue correction, not a claimed reading of our
own.

## Next

1. Locate and read Nepveu tot Ameyde 1842, pp. 18-22 (Delpher.nl / Google Books /
   KB catalogue), to record what fraction of the cipher he broke and whether a
   usable key survives -- this could still be a **contribution** lane item (handing
   a machine-readable key to DECODE/the solver repos) even though the letter itself
   is not a fresh solve.
2. If a key does survive, check whether the same cipher was reused in the Sept 1572
   "merchant's letters" pseudonym correspondence between Willem and Lodewijk van
   Nassau referenced by the Huygens ING project description (sibling-key lead named
   in the brief) -- would extend a recovered key across other Nassau-family items in
   the same tome.
3. Correct QUEUE.md's P1 row from "check-solved: six-source sweep" to "found-solved,
   see ciphers/orange-nassau-1572/NOTES.md" (done, this sweep).
4. Whether an earlier Nederlandse-historische-bronnen volume covers 1572-1578
   Willem-Jan correspondence (distinct from Kluiver's 1578-1584 edition) was not
   resolved -- worth one more targeted search before treating source family (3) in
   the brief (Japikse/other editions) as exhausted.
