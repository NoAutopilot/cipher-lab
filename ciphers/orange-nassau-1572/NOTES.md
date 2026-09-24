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

## Nepveu tot Ameyde 1842, read in full (24 September 2026)

Located and read via Delpher (delpher.nl, tijdschriften collection); curl alone
returns an empty JS shell, so fetched with `tools/browser_fetch.js` (route: Delpher
search page render -> "49 tijdschriften gevonden" for `"Nepveu tot Ameyde"` ->
first hit is the right issue). Full citation confirmed: L. J. Nepveu tot Ameyde,
[untitled letter to the editor], *Algemeene Konst- en Letterbode, voor het jaar
1842*, no. 2 (14 Jan. 1842), A. Loosjes Pz., Haarlem, pp. 18-22, signed "Utrecht,
... Dec. 1841." Delpher item identifier `MMKB13:002671002:mpeg21`, page identifiers
`:00001`-`:00006` for printed pp. 17-22. Images (screenshots of the rendered page
scan, not a re-transcription) and OCR text saved to
`sources/nepveu-1842/` with `manifest.json` (URLs, identifiers, what each page
contains). Requests: delpher.nl ~13 (browser_fetch.js, >=1.5s apart, all 200; no
challenge encountered, route 1 -- JSON/plain URL -- did not work for this site's
client-rendered search/view pages, so route 2 -- real browser -- was used
throughout; no other host queried this pass).

**What the article actually contains, pp.18-22 (grade H throughout, read directly
from the 1842 print via the page images):**

- **p.18**: Nepveu's covering letter to the editor. States he found the key to
  cipher passages in Groen van Prinsterer's *Archives*, I Ser., 3e t., **both**
  no. CCCLXXXV (our target, pp.501-510) **and no. CCCLXXXVII** (pp.511-513 or
  thereabouts -- a different letter in the same volume, "du même au même, datée du
  Camp de Geel", 24 Sept./7bre 1572, i.e. Orange to Jean de Nassau again, three
  days after our letter -- **not currently a target in this repo**; flagging as a
  possible companion item, not pursued further this pass per brief).
- **p.19**: the key table in full (`key_nepveu.tsv`): a-z mapped to multiples of 3
  from 3 to 72 (i/j merged at 27, u/v merged at 60); "de overige cijfers zijn
  zoogenaamde non-valeurs, ter nedergesteld, om den oningewijden lezer het spoor
  bijster te maken" -- every other number is a null, inserted to throw off an
  uninitiated reader. Then the deciphered text of **CCCLXXXV** begins ("Vous etes
  fans doubte asfez adverty du ... meurtre" (de la St. Barthélemy) ...").
  Footnotes 1-3.
- **p.20**: CCCLXXXV continues to its end, **including the postscript** ("Quant a
  Diets von Sch(p)onenberg ..."), on which Nepveu himself notes: "(Omtrent dit P.
  S. schijnt eenige rectificatie of aanvulling van den tekst vereischt te
  worden.)" -- "Regarding this P.S. some rectification or completion of the text
  seems to be required" -- **this is almost certainly what the Huygens database's
  "(onv.)"/incomplete marker refers to**: Nepveu read the whole letter (the
  narrative body plus every cipher-bearing passage Groen printed, matching the
  page range 501-510/pp.502-503, 506-507, 509 noted above -- pencil marginal page
  numbers "p.503", "504/5", "505", "506/7" visible in the scan margin next to the
  corresponding paragraphs, apparently added by a later reader/cataloguer, not
  part of the 1842 print, tracking his readings against Groen's pages) but flags
  the postscript specifically as unresolved. Footnotes 4-7. **CCCLXXXVII** then
  begins ("du même au même, datée du Camp de Geel"), footnotes 8-12.
- **p.21**: CCCLXXXVII concludes ("Escrit en mon camp à Geel ce 24 de 7bre
  1572"), footnote 13. Immediately after, an **unrelated** section begins ("Ik
  wenschte bij deze gelegenheid uwe lezers mede nog opmerkzaam te maken op eene
  uitgaaf van Archieven ...") introducing an extract from Bertrand de Salignac de
  la Mothe Fénelon's published diplomatic correspondence (Paris, 1840) -- this is
  **not a decipherment**, it is already-plain French text Nepveu is sharing as a
  supplementary curiosity; it is not part of the Orange-Nassau cipher at all.
- **p.22**: the Fénelon extract concludes; article signed "Utrecht, L. J. Nepveu
  tot Ameyde. Dec. 1841." A new, unrelated article (an obituary of J. F. Hoefman)
  begins on the same page.

**Method** (as stated and as evidenced by the 13 footnoted corrections,
`nepveu_corrections.tsv`): simple monoalphabetic number substitution (multiples
of 3 for letters, everything else a null), applied by Nepveu against the cipher
numerals **as Groen printed them in 1836**. Where a printed numeral is not a
multiple of 3 (hence cannot be a letter under his own key) or otherwise yields
nonsense, he proposes in a footnote what the numeral should be, always adjusting
to a nearby number that (a) is a multiple of 3 and (b) makes the surrounding word
legible -- e.g. footnote 9 corrects a printed "14.6.12.6.9" (reads as nonsense
"b.d.b.c") to "14.12.60.9", which decodes (14 as a null) to "duc", matching "le
maine du duc d'Albe" in the immediately surrounding plain text; footnote 12
similarly resolves to "les miens". This reads as Nepveu treating the printed
numerals as probably containing 1836 typesetting/transcription errors rather than
cipher he could not break -- i.e. his stated key applies successfully to nearly
every cipher group in both letters once such corrections are made, and the cipher
mixed single enciphered letters into otherwise-plaintext words rather than
enciphering whole sentences.

**What is established vs inferred:** H (read directly from the 1842 print) --
the key table, the reconstructed French text of both letters, and the 13
footnoted corrections, all as printed by Nepveu. **I** (inferred by this worker,
not printed by Nepveu) -- the reading of footnotes 9 and 12 against
`key_nepveu.tsv` to show they decode to "duc" and "les miens" respectively, and
the identification of the postscript remark as the likely source of the "(onv.)"
tag; these are arithmetic checks of Nepveu's own published key against his own
published footnotes, not new cryptanalysis of the ciphertext, and are not a
claimed reading of our own under rule 4. No novelty class is claimed or implied
by any of this; rule 10 wording ("new", "first", "unpublished") is not used
anywhere in this section, consistent with the "found-solved" verdict already on
record above.

**Not established this pass:** whether Nepveu's key, applied group-by-group to
`ciphertext.txt`, reproduces the same French text and where it might diverge --
that comparison was not attempted (out of this brief's scope: "do not decode
anything yourself"). Whether letter CCCLXXXVII belongs in this repo as a
sibling target. Whether the marginal pencil page numbers in the scan were added
by Huygens ING staff or an earlier reader (not established, not material to the
reading itself).

## Next

1. ~~Locate and read Nepveu tot Ameyde 1842~~ -- done, this pass; see section
   above, `sources/nepveu-1842/`, `key_nepveu.tsv`, `nepveu_corrections.tsv`.
2. ~~Apply `key_nepveu.tsv` to `ciphertext.txt` mechanically~~ -- done, 24
   September 2026; see "Mechanical decode" section below.
3. ~~Consider whether Groen ... CCCLXXXVII ... should be scouted as a companion
   target~~ -- extracted as `ciphertext_2.txt`, 24 September 2026; see below.
   Groen's 1836 print itself already gives this letter's plaintext in clear
   French (a second, separate copy survived), immediately followed by a second,
   enciphered printing of the same letter offered as a cryptanalytic aid for
   letter 385 -- established from the primary source, see `ciphertext_2.txt`'s
   header. Not pursued as a folder of its own this pass (out of this job's
   brief); flagging again for a future worker.
4. If a key does survive, check whether the same cipher was reused in the Sept 1572
   "merchant's letters" pseudonym correspondence between Willem and Lodewijk van
   Nassau referenced by the Huygens ING project description (sibling-key lead named
   in the brief) -- would extend a recovered key across other Nassau-family items in
   the same tome. (Nepveu's key, now in hand, makes this directly testable.)
5. Correct QUEUE.md's P1 row from "check-solved: six-source sweep" to "found-solved,
   see ciphers/orange-nassau-1572/NOTES.md" (done, this sweep).
6. Whether an earlier Nederlandse-historische-bronnen volume covers 1572-1578
   Willem-Jan correspondence (distinct from Kluiver's 1578-1584 edition) was not
   resolved -- worth one more targeted search before treating source family (3) in
   the brief (Japikse/other editions) as exhausted.
7. Per the mechanical decode below, the residue left unread by `decode.py` looks
   resolvable by a page-image check (letter 385) or by aligning against Groen's
   own printed plaintext of letter 387 (letter 387) -- neither attempted here,
   both flagged as cheap next steps, not a cryptanalytic campaign.

## Mechanical decode (24 September 2026)

`decode.py` (this folder) applies `key_nepveu.tsv` to `ciphertext.txt` and, since
`ciphertext_2.txt` now exists (see below), to it as well, regenerating `reading.txt`
and `reading_2.txt`. `--check` recomputes both from the committed inputs and exits
non-zero if either committed reading file is stale (CLAUDE.md rule 7); both are
current as committed.

**What the script does, precisely** (see its own docstring for the full spec): it
tokenises each ciphertext file into numeral-group runs (chains of 2+ short,
period-terminated tokens -- the transcription's own convention for separating
groups), excludes Groen's own editorial footnotes (citation apparatus in French/
Latin/Dutch, not cipher) from group-scanning by line range, and classifies each
group token:
- **H** -- the token, after only the OCR-digit-misread substitution
  `ciphertext.txt`'s own header sanctions (lowercase l/i to "1", "o" to "0"),
  parses to a clean integer that `key_nepveu.tsv` resolves to a letter or, per
  Nepveu's own stated rule, a null ("de overige cijfers zijn non-valeurs").
- **M** -- uncertain: the token parses to a clean integer only after also
  stripping one stray non-digit typographic character (bracket, caret, asterisk)
  that is *not* part of the sanctioned substitution. Flagged, not decoded --
  `reading.txt` shows `[M:<token>]`, no letter is asserted.
- **U** -- unread: does not parse under either rule.
- **margin** -- a small, separately-counted class: tokens that are marginal
  "1572. Septembre" running-header text bled into the OCR by the lost
  two-column layout (recognisable by a literal caret or a fragment of
  "1572"/"1567"/"septembre"), not cipher at all; excluded from the H/M/U counts
  entirely.

It does **not** apply `nepveu_corrections.tsv`'s 7 footnoted numeral corrections
for letter 385 to `ciphertext.txt`: each correction cites the printed 1836
numeral as Nepveu read it from the original, and an exact-string search for
every "as printed" value in `ciphertext.txt` (a different, independent OCR
pass -- Google/Internet Archive, not Nepveu's own reading of the print) found no
match; the two OCR passes misread the same digits differently, and resolving the
mismatch would need the page image, which is solver work outside this job's
mechanical-key-application brief. This is a stated limitation of `decode.py`,
not a claim the corrections don't apply somewhere in the text.

**Counts** (per this job's grading scale -- H/C/M/U, not the general CLAUDE.md
rule-4 scale; see decode.py's docstring for why C is 0 here):

| Letter | groups scanned | margin excl. | H | M | U | C |
|---|---|---|---|---|---|---|
| CCCLXXXV (`ciphertext.txt`, our main target) | 917 (88 runs) | 4 | 867 | 6 | 40 | 0 |
| CCCLXXXVII (`ciphertext_2.txt`, companion) | 347 (49 runs) | 1 | 288 | 1 | 57 | 0 |

C = 0 for both: this pass mechanically applies the key table only; it does not
attempt the token-by-token alignment against Nepveu's own printed French
reconstruction (`sources/nepveu-1842/ocr_p19.txt`-`ocr_p21.txt`) that would let a
specific group be graded C ("confirmed by known plaintext") rather than H. A
spot check of one run (djvu-derived `ciphertext.txt` lines 126-128, the "Or(i)
[cipher]. cela nous ait esté" passage) shows the mechanically-decoded letters
reading, with gaps at the unread tokens, as a plausible fragment of Nepveu's
own printed "quel coup de masfue" -- consistent with, but not a rigorous
per-token confirmation of, the key's correctness; a full alignment pass was not
attempted (would itself be a substantial solver task, out of this brief).

**Unread (U) groups, main target (`ciphertext.txt`), 40 occurrences, 24 distinct
spellings:** `a5`(4) `e`(4) `s`(4) `4a`(3) `m`(3) `d`(2) `is`(2) `la`(2) `2S`(1)
`4ft`(1) `5a`(1) `5t`(1) `Si`(1) `_`(1) `a`(1) `aô`(1) `f`(1) `g`(1) `iS`(1)
`j6`(1) `n`(1) `p`(1) `v`(1) `y3`(1). Full list with line-adjacent context is
regenerable any time from `reading.txt`'s own header (`decode.py`'s output).

**Unread (U) groups, companion (`ciphertext_2.txt`), 57 occurrences, 39 distinct
spellings:** `la`(4) `4a`(3) `Si`(3) `aS`(3) `e`(3) `iS`(3) `5)`(2) `S9`(2)
`ao`(2) `p`(2), plus 29 more at 1 occurrence each (`%S 3a 3g 4> 4» 5& 9.4 >4 B
Co Gçi Sa U V a? bi fti ifl ij jB ji lâ lï s s5 sa t « »5 î6`). Full list in
`reading_2.txt`'s header.

**Assessment: is the unread residue enough to be a cryptanalytic target?** No.
Both counts are small relative to the whole (40/913 = 4.4% of graded groups for
the main letter, 57/346 = 16.5% for the companion, whose page range is visibly
more OCR-degraded -- compare the raw excerpts in `ciphertext_2.txt`), and the
unread tokens are scattered singly through otherwise-cleanly-decoding runs
rather than forming an unbroken block: the spot check above found a legible
French phrase fragment straddling three unread tokens in one run. This reads as
an artefact of this specific secondary OCR transcription (Google/Internet
Archive), not evidence of any cipher complexity beyond Nepveu's published key,
and not a cryptanalytic failure -- so CLAUDE.md rule 3's matched-control
requirement does not apply here (that rule is for a solver's claimed inability
to break a cipher; this is a mechanical transcription-fidelity gap in an
already-published key's application, not a claimed negative result). What
would close it, cheaply, without a cryptanalytic campaign: (a) for the main
letter, checking the ~24 distinct unread spots against the page image
(`images/manifest.json` already holds pp.501/503/506; pp.505/507/509 are not
yet fetched); (b) for the companion letter, aligning its unread groups against
Groen's own already-printed clear-French duplicate of the same letter (see
`ciphertext_2.txt`'s header) -- a crib-alignment exercise, not cryptanalysis,
and the cheaper of the two since no further image fetch is needed. Neither is
attempted here, per this job's brief ("do not attempt to solve the residue").

**Requests this pass:** archive.org 2 (one `curl -o /dev/null` reachability
check, one single fetch of `archivesoucorre04housgoog_djvu.txt`, cached to the
worker's scratch directory only -- not committed to the repo, since the extract
needed is now committed as `ciphertext_2.txt` and the manifest above records
where to re-fetch it). No other host queried this pass.
