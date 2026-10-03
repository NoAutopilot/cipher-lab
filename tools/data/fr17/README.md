# fr17: French diplomatic, administrative and epistolary prose of about 1617-1644, in period spelling

Built 3 Oct 2026 (TOOL-FR17, account-4 worker for the account-4 parent), the While-waiting step GAPS46 named for
`ciphers/decode-2754-bnf-baluze156-1636` (ROOM.md 07:19 UTC 3 Oct 2026: its spec fell back to fr16, Catherine de
Medicis and Marguerite de Valois letters of c.1560-1615, "not era-matched for 1636"). Same pattern as
`tools/data/pt18` (V6-PTCORP) and `tools/data/sco16`: Internet Archive `_djvu.txt` OCR, one request per file, a
`build.py` that regenerates every committed file from the raw OCR, and a leave-one-file-out check.

Register in the judge: `LANG_CORPORA["fr17"]` in `tools/judge_plaintext.py`. "fr" stays the default; a spec opts in
with `"judge": {"language": "fr17", ...}`.

## Sources (all public domain, 1858-1890 printings of 17th-c. letters)

| file | work | letters dated | folded letters |
|---|---|---|---|
| `bub_gb_OIQItRIybmIC` | Richelieu, *Lettres, instructions diplomatiques et papiers d'Etat* (Avenel), tome III, 1858 | 1628-1630 | 650,123 |
| `bub_gb_wBJLsV8B_BgC` | same, tome VI, 1867 | 1638-1642 | 650,437 |
| `lettresdepeiresc01peiruoft` | *Lettres de Peiresc aux freres Dupuy* (Tamizey de Larroque), tome I | Dec 1617-Dec 1628 | 650,643 |
| `lettresdepeiresc02peiruoft` | same, tome II | Jan 1629-Dec 1633 | 650,641 |
| `lettresdejeancha01chap` | *Lettres de Jean Chapelain* (Tamizey de Larroque), tome I, 1880 | 1632-1640 | 650,095 |
| `lettresducardina01maza` | *Lettres du cardinal Mazarin pendant son ministere* (Cheruel), tome I, 1872 | Dec 1642-June 1644 | 650,464 |

Total **3,902,403 folded letters**, six files from four authors, none above 16.7 pct of the model. URLs, line counts
and why each was chosen are in `MANIFEST.tsv`. Fetched 3 Oct 2026, 7 archive.org requests for text (one Sourdis
volume fetched and dropped, see below) plus 7 advancedsearch calls (14 archive.org requests in all), >=1.5 s apart.

**Build** (`build.py --raw DIR`, reads `raw_<identifier>.txt`): rejoin hyphenated words; keep OCR lines of >= 4
words; group lines in chunks of 15 and keep a chunk only when its period-spelling markers (estoit, avoit, nostre,
mesme, estre, faict, sçavoir, -oit/-oient imperfects) are at least as many as its modern ones (etait, avait, notre,
meme, etre, -ait/-aient) and at least one -- this drops most of the editors' 19th-c. notes, introductions and indexes;
cap each file at 650,000 folded letters from its start. Residue: editor footnote lines and page headers that fall
inside a kept chunk ("DU CARDINAL DE RICHELIEU", bibliographic note fragments) remain, as in sco16 and fr1810.

**Left out on purpose.** The Sourdis *Correspondance* (1839) was fetched and dropped: its editor modernised the
spelling (1 period marker against 1,584 modern in the whole volume). Avenel tomes IV-V and Peiresc tome III (1630-37)
are left out so nothing dated 1633-1637 is in the model (davaux-1633, arsenal6314-hanau-1635 and baluze156-1636 are
targets of those years). Never add Baluze 155/156 Sabran-circle letters, Lasry's keys' plaintexts, or any edition that
prints a target's own letter.

## Held-out calibration (3 Oct 2026, CLAUDE.md rule 3 fold-count paragraph)

`holdout_check.py` (this folder; the fr1810/es17c7 method): leave-one-file-out, 200 windows per held-out file, a
window false-negatives when it scores at or below the in-model real_p05. N=138 is baluze156's own length (letter
cipher, 138 symbols). Logs: `holdout_*.log`.

| check | per fold (Avenel III, Avenel VI, Peiresc I, Peiresc II, Chapelain I, Mazarin I) | blended | spread |
|---|---|---|---|
| fr17 leave-one-out, N=138 | 6.5, 17.5, 17.5, 17.5, 8.0, 14.5 | **163/1200 (13.6%)** | 6.5-17.5% (2.7x) |
| fr17 leave-one-out, N=300 | 18.0, 25.0, 16.5, 25.0, 8.0, 12.0 | **209/1200 (17.4%)** | 8.0-25.0% (3.1x) |
| same fr17 windows scored by the fr16 model (all 3 fr16 files, its own real_p05 -1.007), N=138 | 3.0, 10.0, 9.5, 13.0, 4.0, 10.0 | **99/1200 (8.2%)** | 3.0-13.0% (4.3x) |
| fr18 leave-one-out, N=138 (comparison) | Torcy I 0.5, Torcy II 3.0, Villars I 6.5, Villars II 4.0, Maintenon 19.0, Gazette 87.0 | 240/1200 (20.0%) | 0.5-87.0% (174x) |

Discrimination, N=138, 100 windows per fold: the shuffled held-out windows pass the real_p05 threshold 0/600 times
under fr17 leave-one-out and 0/600 under fr16; median held-out margin over real_p05 is +0.125 (fr17) and +0.159 (fr16).

**Reading.** fr17 has the even fold shape rule 3 asks for (six folds, four sources, no outlier fold -- unlike fr18's
Gazette or es17c's 4x three-fold spread), so a FAIL/PASS against it is not of "unknown reliability" in the es17c sense.
But it is **not** the calibration rescue pt18 was for pt17: genuine 1617-1644 prose is false-negatived *more* often
under fr17 leave-one-out (13.6%) than under fr16 (8.2%) at N=138. The fr17 threshold is stricter (real_p05 about
-0.93 against fr16's -1.007) because its in-model windows are cleaner and more alike; fr16's noisier OCR sets a more
lenient bar, and both bars reject every shuffled window. (Leave-one-out also trains fr17 on five sixths of its text,
so the full six-file model is a little better than these folds show.) A second build tried 6-line chunks plus an
OCR-debris line filter (`build.py --chunk 6 --debris`): it shrank the corpus 29 pct and read 14.3% (7.5-23.0%) at
N=138 and 20.9% (6.5-37.0%) at N=300 -- no better, so the committed build is the first; per rule 3's third-attempt
clause, a further cleaning knob is not the next step.

**Use.** For a 1615-1665 French target, run the judge under both `fr17` and `fr` and report both. A PASS under one and
FAIL under the other at N about 140-300 is "judge cannot decide", not a negative. Expect about 14% (N=138) to 17%
(N=300) false negatives on real prose under fr17 alone.

## Targets that should be re-judged under fr17 (not re-scored in this job)

Specs whose judge is `fr` (fr16) and whose letter falls in 1615-1665: `specs/decode-2754-bnf-baluze156-1636.json`
(first; GAPS46's step), `specs/colbert26-lathuillerie-1644.json`, `specs/thurloe-barriere-1654.json`. Any candidate
reading in the 1620s-1650s French folders without a spec yet: davaux-1633, arsenal6314-hanau-1635,
arsenal6334-longueville-1650-59, baluze103-letellier-marca-1644, clair1067-brienne-poland-1646, clair571-estrades-1645,
clair577-brienne-estrades-1647, clair577-estrades-piombino-1647, clerville-francia-1648, fr5160-letellier-1653,
decode-9482-bnf-colbert11-mazarin-bordeaux-1654, baluze178-croissy-mazarin-1660, decode-2678-bnf-colbert127-gravel-1665.
Circularity check before re-judging colbert26-lathuillerie-1644 and baluze103-letellier-marca-1644: Mazarin tome I runs
to June 1644, so grep the target's reading against `lettresducardina01maza.txt.gz` first; if it is printed there, judge
with that file left out (`"corpora"` in the spec).

## Re-judge, rest of the list (FR17-RJ2, 3 Oct 2026)

None of the twelve remaining targets has a committed candidate reading, so no judge, shuffled-decode or per-fold run was made; nothing changed verdict. Already judged elsewhere: baluze156-1636 (REJUDGE-FR17), clair1067-brienne-poland-1646 and fr5160-letellier-1653 (SPEC-FR17), riksarkivet-r4282-1628 (GAPS65); colbert26-lathuillerie-1644 skipped (parked by the owner).

| target | N | fr16 | fr17 | shuffled fr17 | verdict change | note |
|---|---|---|---|---|---|---|
| thurloe-barriere-1654 | -- | not run | not run | not run | none (no reading on disk) | spec judge block now fr17 + language_also fr; coverage test only, no reading file |
| davaux-1633 | -- | not run | not run | not run | none (no reading on disk) | found-solved, no reading of ours |
| arsenal6314-hanau-1635 | -- | not run | not run | not run | none (no reading on disk) | blocked, no ciphertext |
| arsenal6334-longueville-1650-59 | -- | not run | not run | not run | none (no reading on disk) | blocked, no ciphertext |
| baluze103-letellier-marca-1644 | -- | not run | not run | not run | none (no reading on disk) | blocked; Mazarin I circularity check waits for a reading |
| clair571-estrades-1645 | -- | not run | not run | not run | none (no reading on disk) | open, not digitised |
| clair577-brienne-estrades-1647 | -- | not run | not run | not run | none (no reading on disk) | blocked |
| clair577-estrades-piombino-1647 | -- | not run | not run | not run | none (no reading on disk) | blocked |
| clerville-francia-1648 | -- | not run | not run | not run | none (no reading on disk) | blocked |
| decode-9482-bnf-colbert11-mazarin-bordeaux-1654 | -- | not run | not run | not run | none (no reading on disk) | found-solved, no reading of ours |
| baluze178-croissy-mazarin-1660 | -- | not run | not run | not run | none (no reading on disk) | found-solved, no reading of ours |
| decode-2678-bnf-colbert127-gravel-1665 | -- | not run | not run | not run | none (no reading on disk) | open, transcription only |

Test: `tools/tests/test_judge_plaintext_lang_fr17.py` (held-out 1640 Chapelain passage past the cap passes; shuffled
and random fail; corpus >= 5 files and >= 1M letters and does not contain the passage).
