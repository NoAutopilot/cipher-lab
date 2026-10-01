# fr1810: Napoleonic-era official and military French (1800-1811) for the judge's language check

Built 1 Oct 2026 (account-4 worker BER-FRCORP, `.claude/briefs/runs/2026-10-01-account4-ber-frcorp.md`) because
`ciphers/berthier-napoleon-1812` (Berthier to Napoleon, 22 Dec 1812) had no French corpus on disk matching both its
era and its register: `tools/data/fr18` is 1680-1790 diplomatic/official prose (a 22-132-year mismatch, flagged in
the spec's own judge note), `fr19` is 1830-1888 novels (fiction register, not wired), `fr16` is 16th-century letters
(CLAUDE.md rule 3, the pt17 -> pt18 and fr16 -> fr18 lessons). BER-HOMO (27 Sept 2026) named building this corpus as
the folder's next step. Built the way `tools/data/pt18` was: Internet Archive `_djvu.txt` OCR, front and back matter
trimmed with every cut recorded in MANIFEST.tsv, letters counted after `judge_plaintext.fold()`.

Six volumes across three works, all letters, orders and dispatches of the imperial chancery and a marshal's staff,
no narrative, no fiction, no verse:

- **Correspondance de Napoléon Ier, publiée par ordre de l'empereur Napoléon III** (Paris 1858-70), tomes XI
  (1805-06), XVI (1807-08) and XX (1809-10) -- University of Toronto scans `correspondancede11napouoft`,
  `correspondancede16napouoft`, `correspondancede20napouoft`. Napoleon's own dictated letters and orders, most of
  them routed through Berthier as major général.
- **Correspondance du maréchal Davout, prince d'Eckmühl: ses commandements, son ministère, 1801-1815**, ed. Charles
  de Mazade (Paris 1885), tome II (July 1807 - May 1809) and tome III cut before 1812 (May 1809 - Nov 1811) -- Google
  Books scans `correspondanced01davogoog`, `correspondanced00davogoog`. A marshal's dispatches to the major général
  (Berthier) and to the Emperor: the target letter's own office and direction, seen from the other side.
- **Lettres inédites de Napoléon Ier (an VIII-1815)**, ed. Léon Lecestre, tome I (an VIII-1809), 2nd ed. (Paris
  1897) -- `lettresindites01napo`. The letters left out of the 1858-70 edition, same register, a different editor.

See MANIFEST.tsv for per-file identifier, title, date, URL, byte and letter counts, fetch date, the exact cut lines and
why each volume was chosen. Fetched once, one request at a time, >=1.5 s apart: 18 archive.org requests this pass
(12 `advancedsearch.php` candidate searches -- 6 of them wasted on a field-encoding bug and repeated -- and 6
`_djvu.txt` downloads; no other host touched).

**Trimming.** Google's boilerplate (English and French copies) and each editor's modern front matter were cut: the
1865 "Rapport à l'Empereur" in tome XVI, Mazade's 1885 introductions in both Davout tomes, Lecestre's 1897 preface.
The volumes' own back-matter indexes ("Table des pièces", "Table analytique", "Table des matières") were cut.
Mazade's two chapter introductions that sit *between* letter sections inside the text (chapter VI "Campagne de 1809"
in tome II, chapter VII "L'armée d'Allemagne ... 1810-1811" in tome III, plus its duplicate scan) were stripped as
modern editorial narrative, the risk fr18's README flagged for the Recueil des instructions; the editors' short source
footnotes ("(1) A. du Casse, Supplément ..."), running headers and scattered scanner stamps were left in place as
low-volume noise, as pt18 and fr18 did. Raw OCR is kept raw (tome XX's headings read "PRIXCE", "GEXERAL" for PRINCE,
GÉNÉRAL -- a heading-typeface n/x confusion; its body text is clean, see the coverage check below).

**Excluded, deliberately.** Correspondance de Napoléon tomes XXIII-XXIV (Napoleon's own 1812 letters, including the
30 Dec 1812 reply to Berthier that NOTES.md discusses), Davout's 1812-13 letters (the Russian campaign, the target's
own weeks), Chuquet's *1812: la guerre de Russie* (the target folder's own candidate-plaintext pool), the Bulletins de
la Grande Armée 1812 (the only IA copies are German-catalogued BSB items of the 1812 campaign itself) and anything
else from Dec 1812 -- a judge corpus that contains the target's own month and correspondents is circular the way
pt17/pt18's warnings describe. Never add Berthier's own Dec 1812 letters, Chuquet 1912 or tome XXIV to this folder.

**Size.** 1017150 + 888742 + 988967 + 854733 + 473643 + 597410 = **4,820,645 letters after fold()**, 4.8x the
1,000,000-letter floor the brief set, over twice fr18's 2.36M. No single file is more than 21.1 pct of the total
(tome XI); the smallest is 9.8 pct (Davout tome III, cut before 1812).

**OCR-quality check** (leave-one-out cross-corpus word coverage, as pt18 and fr18 did): for each file,
`NgramModel.cover()`'s word list built from the other five files only, scored on the first 400,000 folded letters of
the held-out file: tome XI 0.960, tome XVI 0.962, tome XX 0.923, Davout II 0.952, Davout III 0.953, Lecestre I 0.958
-- the same band fr18 reported (0.88-0.97) for a clean period corpus.

## Held-out calibration at N=325: fr1810 beside fr18 (1 Oct 2026, rule 3's fold-count paragraph)

`holdout_check.py` (this folder; the es17c7 method, parametrised by corpus): leave-one-file-out, 200 windows of
N=325 letters per held-out file -- N=325 is the target's own group count (specs/berthier-napoleon-1812.json), the
short end of its plaintext length band -- scored against the five-file model's own `real_p05`. The identical check
was run on `fr18` (six files) at the same N. Full output in `holdout_2026-10-01.log`.

| corpus | fold (held-out file) | real_p05 | false negatives |
|---|---|---|---|
| fr1810 | correspondancede11napouoft (Napoléon XI) | -0.896 | 8/200 (4.0%) |
| fr1810 | correspondancede16napouoft (Napoléon XVI) | -0.887 | 4/200 (2.0%) |
| fr1810 | correspondancede20napouoft (Napoléon XX) | -0.833 | 118/200 (59.0%) |
| fr1810 | correspondanced01davogoog (Davout II) | -0.849 | 46/200 (23.0%) |
| fr1810 | correspondanced00davogoog (Davout III, to Nov 1811) | -0.854 | 31/200 (15.5%) |
| fr1810 | lettresindites01napo (Lecestre I) | -0.849 | 27/200 (13.5%) |
| **fr1810** | **blended** | | **234/1200 (19.5%)**, per-fold spread 2.0-59.0% (29.5x) |
| fr18 | memoiresdemonsie01torc (Torcy I) | -0.983 | 0/200 (0.0%) |
| fr18 | memoiresdemonsie02torc (Torcy II) | -1.026 | 6/200 (3.0%) |
| fr18 | mmoiresduducde01invill (Villars I) | -1.025 | 6/200 (3.0%) |
| fr18 | mmoiresduducde02vill (Villars II) | -1.017 | 1/200 (0.5%) |
| fr18 | mmoiresetlettre01margoog (Maintenon) | -1.001 | 40/200 (20.0%) |
| fr18 | lagazettedefran01unkngoog (Gazette 1786) | -0.887 | 191/200 (95.5%) |
| **fr18** | **blended** | | **244/1200 (20.3%)**, per-fold spread 0.0-95.5% |

Reading. The two blended rates are the same within noise (19.5 vs 20.3 pct at N=325); what differs is the shape.
fr18 at this N is five near-zero folds plus one fold (the Gazette, its only newspaper) that fails 95.5 pct of the
time -- fr18's own README reported 18-19 pct blended at N=200/500 without this per-fold breakdown, and the breakdown
shows that figure is almost entirely one outlier file. fr1810 has no fold above 59 pct but four folds between 13.5
and 23 pct and one (tome XX) at 59 pct; its worst fold is the volume with the lowest word coverage (0.923) and the
loosest threshold (real_p05 -0.833, the five other files making a tighter model than tome XX fits), the same
"one volume's own register or scan is the outlier" shape as es17c7's tomo XVII and EN-FOLDS' Moby-Dick. By CLAUDE.md
rule 3's es17c/EN-FOLDS paragraphs, **a FAIL/PASS against fr1810 at N about 325 is of unknown reliability on the
blended number alone, exactly as one against fr18 is**; fr1810 is the era- and register-matched corpus the target
needed, it is not a more reliable gate than fr18 at this N. A spec that uses it should state the per-fold spread
beside any verdict, and a FAIL close to the gate is "judge cannot decide", not a negative. The named next cheap step
for the corpus itself (not for the target) is a homogeneity split -- by addressee or by year inside tome XX -- to
find what makes that fold the outlier, es17c7's own unrun next step; the pre-strip run of the same check (before
Mazade's chapter introductions were removed) read 17.7 pct blended, 2.0-60.0 pct per fold, so the strip moved
nothing material and the outlier is not editorial prose.

A note on the real_p05 thresholds: fr1810's run between -0.833 and -0.896, fr18's between -0.887 and -1.026 -- the
1800-1811 chancery register scores itself about 0.1 nat/letter higher under its own model than fr18's 1680-1790
memoir register does under its own, so a candidate reading's absolute score is not comparable across the two corpora;
only the PASS/FAIL against each corpus's own thresholds is.

## Wired into `tools/judge_plaintext.py`

Added as its own key `LANG_CORPORA["fr1810"]` (the same pattern as `pt18`, `fr18`, `es17c7`); `"fr"` still points
to fr16, and `specs/berthier-napoleon-1812.json`'s judge block still says `fr18` so every recorded result there and
in HYPOTHESES.md stays reproducible -- a `judge_note` in the spec names this corpus as available, and a future run
opts in with `"judge": {"language": "fr1810", ...}`. Offline test: `tools/tests/test_judge_plaintext_lang_fr1810.py`
(a Davout letter of 23-24 Jan 1812 from the part of tome III cut from this corpus, genuinely unseen: passes; shuffled
and random-letter controls fail).
