# Printed-ciphertext detector test, 23 September 2026

**Status: open** (a detector test, not a target folder — nothing here is promoted or solved; rule 10 applies
throughout, no reading is claimed and no wording of "new"/"unpublished"/"first" is used).

Worker brief: `.claude/briefs/detector-test.md` (Sonnet, cap ~$8), from RETRO-2026-09-23.md proposal 5 /
hypothesis A. Read first: CLAUDE.md rules 1, 3, 6, 8, 10 and the Access playbook's good-citizen rule;
LESSONS.md §1 (printed ciphertext plus an unapplied key is the largest single solve route in Sept 2026);
RETRO-2026-09-23.md §4A (the Thurloe vol. 1 probe: 111 clusters, controls named).

## 1. Method

`tools/ia_numeral_runs.py` downloads an Internet Archive item's `_djvu.txt` full text once (cached under this
directory, gitignored — `sources/ia-fulltext/*_djvu.txt`), marks OCR lines with >=6 tokens of which >=70% are
1-4 digit numerals, groups marked lines fewer than 4 lines apart into a cluster, and scores each cluster:
numeral count, distinct values, repeat rate (a cipher repeats values; a page index or table mostly does not),
and prose words of 4+ letters within 3 lines either side. One TSV row per raw cluster.

For this sweep, kept clusters use the brief's thresholds: `repeat_rate >= 0.3`, `numerals >= 15`,
`prose_words >= 5`. Kept clusters were judged from their context line only into four categories
(cipher-with-decipherment, cipher-without-decipherment, table, noise — index/accounts/dates/page-lists), and
adjacent kept clusters within 60 OCR lines of each other in the same identifier were merged into one candidate
passage (raw clustering fragments a single long, OCR-garbled cipher letter into many short clusters; merging
avoids reporting the same letter as a dozen separate "survivors"). For each surviving cipher-without-decipherment
passage, `sources/cryptiana/` and fresh shallow clones of `github.com/dbourdeau/cyphersolver` and
`github.com/aaymeloglu/unsolved-ciphers` (cloned into this session's scratchpad, not committed) were grepped for
the edition and the letter's date/correspondents where the context line gave them.

## 2. The edition list (`editions.tsv`, 300 identifiers)

- 2 controls: Thurloe vol. 1 (`collectionofstat01thur`) and Rommel 1840 (`correspondancein00henr`).
- 62 curated named editions from the brief: Thurloe State Papers vols 1-7 (7 ids), Clarendon State Papers
  Calendar (6 ids), Cabala (5 ids), Winwood Memorials/Sawyer 1725 (3 ids), Lettres missives de Henri IV,
  Berger de Xivrey ed. 1843 (5 ids), Négociations diplomatiques series — 8 distinct works sharing this generic
  title (Jeannin, France-Autriche, succession d'Espagne, Buzanval, Levant), Ribier (1 id), Papiers d'État /
  Correspondance du cardinal de Granvelle (5 ids), Nuntiaturberichte aus Deutschland (15 ids across the Erste
  and Zweite Abteilungen plus two named Bände), Marlborough despatches (6 ids).
- 236 further identifiers from 8 keyword-title archive.org advancedsearch queries (`state papers`,
  `négociations`, `lettres`, `dépêches`, `despatches`, `correspondance`, `carteggio`, `Briefe`; date range
  1550-1850, mediatype texts, sorted by downloads, capped at 27-30 per query to land near the brief's "roughly
  300" target after the curated list).

One `archive.org/advancedsearch.php` call per named title/series and per keyword query — 34 calls total (listed
in the worker's scratchpad, not committed) — plus one `archive.org/metadata` call each for two identifiers
needing confirmation (Rommel's exact id; Orange-Nassau's volume). No identifier was searched twice.

**Not found on Internet Archive under any title tried:** Hardwicke's *Miscellaneous State Papers*, the
*Sidney Papers* (Collins ed.), and *Mémoires et correspondance du maréchal Catinat* (1819) — the last is a
named control; Bourdeau's `catinat1691/` reads the same 1819 edition from Bayerische Staatsbibliothek MDZ scans
(`bsb10720287`), not from IA. This is a gap in what IA holds, not a tool failure, and is reported rather than
silently substituted or skipped.

## 3. Fetch results

300 identifiers processed: 274 fetched (2 already cached from the control run) or skipped, 26 skipped on
HTTP 401/403/404/500 with **no retries** (good-citizen rule) — `collectionofstat06thur` (500), `Portia` (404),
all 5 of the `lettersdispatche000Nmarl` Marlborough-despatches ids (401 — a lending-restricted item), 15 further
404s (dead/renamed ids from the keyword sweep, mostly `bub_gb_`/`in.ernet.dli`/library-specific ids that the
advancedsearch index carries but whose full-text endpoint is gone or was never generated), and 4 further 500s.
7,984 raw cluster rows in `runs.tsv` across all 274 fetched items.

## 4. Filter and judgement

136 of 7,984 raw clusters pass `repeat_rate>=0.3 & numerals>=15 & prose_words>=5`, across only 14 of the 274
fetched identifiers (every other identifier's OCR produced zero qualifying clusters). Merging adjacent kept
clusters (<=60 OCR lines apart, same identifier) gives **54 candidate passages**:

| Category | Passages | Identifiers |
|---|---|---|
| Control (cipher-without-decipherment, already read) | 18 | Thurloe vol. 1 (7 passages, the RETRO-2026-09-23.md probe's own control — Aymeloglu has already worked Vande Perre's letters in this volume) + Rommel 1840 (11 passages, all already decoded in cyphersolver `hesse1603/`) |
| Survivor: cipher-without-decipherment, candidate | 24 | Thurloe vols 2 (2), 3 (7), 5 (5), 7 (9); Archives ou correspondance inédite de la maison d'Orange-Nassau vol. IV (1) |
| Table / noise, dropped | 12 (10 merged passages) | Calendar of the Clarendon State Papers vol. V (a name/subject index), Nuntiaturberichte (3 ids — German index page-lists), *Correspondance mathématique et physique* (a math journal — 2 ids), a Bulletin de l'Académie royale de Belgique (a data table) |

See QUEUE.md's new section "Printed ciphertext (detector test of 23 September 2026)" for the 24-row survivor
table with per-passage OCR line numbers, token counts, and what the cryptiana/solver-repo grep found (mostly:
Thurloe's cipher passages are already cryptiana's catalogued unsolved item #9 and cyphersolver's `thurloe/`
folder, 4 pieces marked STUCK; the Orange-Nassau letter — Lettre CCCLXXXV, William of Orange to Comte Jean de
Nassau, Sept. 1572, discussing the St Bartholomew's Day Massacre — was not found under any of the searched
terms in `sources/cryptiana/` or the two solver-repo clones, and its own 1836 editor states in a footnote that a
comparison against known-key material failed to yield a decipherment).

**Caveat carried into the QUEUE row for Thurloe vol. 5 (P11-P15):** cyphersolver's `thurloe/NOTES.md` places 3
of its 4 already-catalogued, STUCK Thurloe cipher pieces in volume 5 (TSP v.78, v.267, v.337). This sweep's
OCR-line locations were not converted to print page numbers (the volume's running-head page markers are not
reliably OCR'd at the positions checked), so overlap between P11-P15 and the 3 known pieces is **not ruled
out** — a next worker should view the leaf or British History Online page before treating any of P11-P15 as
distinct from the catalogued items.

## 5. Metrics (report block)

- **Control recall:** 2 of 2 available controls recovered in full. Thurloe vol. 1's known cipher (line 43962,
  "at present here 7. 7. 17. 24. 7. 6...") reproduced verbatim, and the volume's 111-cluster count matches
  RETRO-2026-09-23.md §4A exactly. Rommel 1840's cipher passages recover across the volume (11 merged
  passages spanning printed pp. 84-391 by cyphersolver's own page map), and every one is already decoded in
  `cyphersolver/hesse1603/`. Catinat 1819 (the third named control) is not on Internet Archive and was not run
  — reported, not silently skipped.
- **Precision in the top 50 clusters by score** (score = numerals × repeat_rate): 50/50 (100%) are genuine
  cipher-in-plain-text by page content (27 survivor-candidate, 23 control); zero table/noise clusters rank in
  the top 50 of 136 — the false positives are all lower-scoring (max score among table/noise: 61, vs. a top-50
  cutoff score of 23.8).
- **Survivors:** 24 merged candidate passages (1 non-Thurloe: Orange-Nassau vol. IV letter 385; 23 Thurloe
  across vols 2/3/5/7), none promoted, none solved. 5 of the 24 (Thurloe vol. 5) are flagged as needing a
  page-level check against already-catalogued material before being treated as distinct from it.
- **Requests, archive.org only** (no other host touched, no credentials used): 34 `advancedsearch.php` calls +
  2 `metadata` calls (36 total), plus 274 `_djvu.txt` fetches (1.5 s apart, descriptive User-Agent, no retries
  on the 26 that came back 401/404/500).
- **Cost:** within the ~$8 cap (the two Bash calls that ran the fetch loop to completion, plus this analysis
  pass, dominate; no subagents were used).

## 6. Files

- `editions.tsv` — the 300-identifier list (identifier, title, year, why included). Committed.
- `runs.tsv` — every raw cluster from all 274 fetched identifiers (identifier, line, n_lines, numerals,
  distinct, repeat_rate, prose_words, context). Committed; reproducible by re-running
  `python3 tools/ia_numeral_runs.py $(tail -n +2 editions.tsv | cut -f1) --cache sources/ia-fulltext --tsv runs.tsv`
  against the same 274 cached `_djvu.txt` files (not committed — re-fetches on a clean checkout, 1.5 s/item).
- `*_djvu.txt` — the cached full text of each fetched identifier. Gitignored (`sources/ia-fulltext/*_djvu.txt`
  in `.gitignore`); re-fetch on demand rather than committing ~250 MB of OCR text.

## 7. Next step (not this worker's brief)

check-solved on the 24 survivor rows in QUEUE.md (six-source sweep per CLAUDE.md rule 1), starting with the
Orange-Nassau letter (the strongest single lead: a distinct edition, a named sender/recipient/date, and the
1836 editor's own statement that a decipherment attempt failed) and, for the Thurloe vol. 5 rows, a page check
against the 3 already-catalogued items before anything else. Never solve from this worker's output directly —
stage 2 (Verified unsolved) has not been set for any of these 24.

## 8. Round 2, continental editions (24 September 2026)

Second detector-test worker, same method (§1), over 276 further Internet Archive identifiers across 18 named
continental documentary-correspondence series (Lettres de Catherine de Médicis, Négociations diplomatiques
France-Toscane, Granvelle's Papiers d'État and Correspondance, Kervyn de Lettenhove's Relations politiques,
Archives Orange-Nassau, CODOIN, Nuntiaturberichte, Deutsche Reichstagsakten, Calendar of State Papers
Spanish/Venetian, Lettres missives de Henri IV, Michaud-Poujoulat, Correspondance de Marguerite d'Autriche,
Brandenburg Urkunden, Lisch's Maltzan, Archivio storico italiano) — `sources/ia-fulltext/editions2.tsv`, harvested
from `archive.org/advancedsearch.php`, deduped against round 1's `editions.tsv`. Full write-up, tables and the
methodological caveat are in QUEUE.md's "Printed ciphertext, round 2 (24 September 2026)" section; summary here:

- **Controls:** 3 of 3 recovered (Thurloe vol. 1 and Rommel 1840 exactly as round 1; a third, continental
  control — Groen's Archives Orange-Nassau tome III, the same Orange-Nassau letter round 1 found-solved —
  recovers its known cipher clusters at OCR lines 24181-24229 and 24362-24373, inside the letter's printed range).
- **Survivors: 0** cipher-without-decipherment passages among the 276 continental identifiers (255 fetched, 24
  skipped on 404/500, no retries). 270 of 17,783 raw clusters passed the same filter as round 1, merging into 180
  non-control candidate passages across 30 identifiers — every one judged table/noise from its context line: a
  back-of-volume name/subject index or chronological register (dominated by Deutsche Reichstagsakten, 24
  identifier-copies, 173 passages), not a letter.
- **Methodological finding for later rounds:** round 1's near-zero false-positive rate on English/Latin editions
  does not carry over to German *Akten*/*Urkunden* series, whose back-matter indices ("Person, dates: vol,page.
  vol,page.") structurally match the detector's numeral-run-plus-nearby-prose signature. A future sweep of this
  kind of edition should pre-filter index/register volumes by title, or tighten the cluster shape test, rather
  than rely on per-cluster judgement at this volume (270 kept clusters this round vs. 136 in round 1's 274
  identifiers).
- **Requests:** archive.org only, 313 total (34 advancedsearch + 279 djvu fetches), no other host, no
  subagents, no logins.

`runs2.tsv` committed (raw clusters, reproducible per the command in QUEUE.md); `_djvu.txt` caches gitignored as
in round 1.
