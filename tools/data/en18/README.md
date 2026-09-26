# en18: 1795-1815 American diplomatic/official English for the judge's language check

Built 26 Sept 2026 (LANE ARM worker ARM-EN18, `.claude/briefs/runs/2026-09-26-lane-arm-en18.md`) because
`LANG_CORPORA["en"]` (Sherlock Holmes 1892 + Moby-Dick 1851, plus three more Gutenberg novels tried in
`tools/data/en/`) is 19th-century British/American *fiction*, not 1800s American *official diplomatic
correspondence* -- an era-and-register mismatch for `ciphers/armstrong-madison-1808` (John Armstrong to
James Madison, Paris, 20 Feb 1808) the same shape as pt17-vs-Linhares (CLAUDE.md rule 3, V6-PTCORP lesson)
and es17-vs-espagnol142 (MJ lesson). `tools/data/en/README.md` already flagged this target's own judge
block with a `corpus_caveat` naming this as the fix.

## Sources

Internet Archive OCR full text (`_djvu.txt`) of six Google-Books/library scans of period American official
and private correspondence, 1794-1819, spanning Armstrong's own 1808 despatch year on both sides:

- **The Writings of James Monroe** (ed. S. M. Hamilton), **Vol. II, 1794-1796** and **Vol. V, 1807-1816**
  (`writingsjamesmo02unkngoog`, `writingsjamesmo11monrgoog`) -- Monroe's own official/private correspondence
  as US minister to France (1794-96, the same posting Armstrong later held) and as Secretary of State-elect
  covering exactly 1808.
- **The Writings of Albert Gallatin** (ed. Henry Adams), **Vol. I** (`writingsalbertg01gallgoog`) -- Gallatin's
  own official correspondence in the same Washington/Treasury/diplomatic circle as Armstrong and Madison
  (an 1816 Gallatin-to-Madison letter appears near the volume's end).
- **The Writings of James Madison** (ed. Gaillard Hunt), **Vol. VII, 1803-1807** and **Vol. VIII, 1808-1819**
  (`writingsofjamesm0007unse_s2a1`, `writingsofjamesm0008unse`) -- Madison's own official correspondence and
  papers, as the target letter's addressee, immediately before and during the target's own year.
- **The Writings of Thomas Jefferson** (ed. Paul Leicester Ford), **Vol. IX, 1807-1815**
  (`writingsofthomas09jeffiala`) -- Jefferson's own correspondence spanning the target letter's year (President
  through March 1809, then Monticello).

See `MANIFEST.tsv` for identifier, title, year range, URL, raw/cleaned byte counts, letter counts and why
each was chosen. American State Papers Foreign Relations vols 2/3 (also suggested in the job brief) were not
fetched this pass -- the six sources above already cleared the 1.5M-letter floor comfortably (4,806,387
letters after `fold()`) within this job's time box; a future worker can add ASP volumes the same way if more
diversity is wanted.

## Cleaning

Each raw `_djvu.txt` was cut and stripped (`clean_en18.py`, a scratch script, not committed -- see the shared
`tools/judge_plaintext.py`'s own `read_corpus()`/`fold()` for what a target/judge run actually uses):

1. **Header**: for scans carrying Google Books' standard English boilerplate ("This is a digital copy of a
   book...", "Usage guidelines", "About Google Book Search"), everything through the last
   `books.google.com` marker line was cut. Two of the six files (`writingsofjamesm0007unse_s2a1`,
   `writingsofjamesm0008unse`, both non-Google Internet Archive/library scans) and one (`writingsofthomas09jeffiala`,
   a Google scan whose title page starts the file directly, no boilerplate line matched) had no boilerplate to
   cut; their front matter is a few hundred bytes of garbled library-stamp OCR ("SAN FRANCISCO PUBLIC LIBRARY",
   "DOCUMENTS DEPARTMENT", call numbers) left in place, the same low-volume noise the pt18 corpus's README
   accepted rather than hand-editing out of a multi-hundred-thousand-letter file.
2. **Footer**: everything after the *last* `^END OF VOL(UME)?...` line was cut where a following-junk tail
   existed (library return-date stamps, blank-page OCR noise) -- 4 of 6 files. `writingsalbertg01gallgoog`'s
   own such line (OCR'd "END  OP  VOLUME  I." -- long-s-adjacent "OF"->"OP" misread) is the file's literal last
   line, so there was nothing after it to cut.
3. **Running heads and page numbers**: bare page-number lines (roman or arabic, <=6 chars) and any short line
   (<=90 chars) repeating 5+ times verbatim across a file -- the standard running-head pattern in these prints
   ("THE WRITINGS OF JAMES MONROE," at the top of every page, "1807] JAMES MADISON. 469" at the bottom) --
   were dropped by exact-string frequency, not by a hand list. Counts per file in `MANIFEST.tsv`'s
   `raw_bytes`/`cleaned_bytes` columns (the difference is mostly this pass, since header/footer cuts are small).
4. **Editorial footnotes**: not separately identified or stripped -- these prints interleave footnotes as
   normal-looking paragraphs mid-page (no consistent OCR marker to grep), so a handful remain inside the
   corpus text as ordinary prose, the same acknowledged gap the pt18/fr18 corpora left for the same reason.
5. **Long-s OCR** (the brief's specific ask): checked for the common tell-tale words ("moft", "fome", "fhall",
   "firft", "congrefs", etc. -- long s misread as f). **Zero hits across all six files** (see `MANIFEST.tsv`
   generation output, not committed) -- these OCR passes render the long s correctly as "s" throughout (the
   one exception found, "END OP VOLUME I." in the Gallatin volume, misreads "OF" as "OP", a different letter
   pair, not the classic long-s artifact) -- so **no long-s correction was needed or applied**.

Combined: 679061 + 542202 + 1161811 + 780926 + 647549 + 994838 = **4,806,387 letters after `fold()`**, well
over the 1.5M floor and over 4x the target's own `letters_min`/`letters_max` range needed for a single 369-code
decode. No single source is more than 24.2 pct of the total (Gallatin); the smallest is 11.3 pct (Monroe Vol. V).

## Fold check (`tools/data/en18/holdout_check.py`, CLAUDE.md rule 3 / EN-FOLDS amendment)

Leave-one-file-out, at **N=1000 and N=1500 letters** (a 369-code-group decode of this target is roughly that
length), not the 200/500 `tools/data/en/holdout_check.py` uses for its own shorter-ciphertext specs:

| N | held out | real_p05 | false negatives | null false positives |
|---|---|---|---|---|
| 1000 | writingsjamesmo02unkngoog (Monroe II) | -0.812 | 28/200 (14.0%) | 0/200 (0.0%) |
| 1000 | writingsjamesmo11monrgoog (Monroe V) | -0.825 | 7/200 (3.5%) | 0/200 (0.0%) |
| 1000 | writingsalbertg01gallgoog (Gallatin I) | -0.808 | 55/200 (27.5%) | 0/200 (0.0%) |
| 1000 | writingsofjamesm0007unse_s2a1 (Madison VII) | -0.830 | 13/200 (6.5%) | 0/200 (0.0%) |
| 1000 | writingsofjamesm0008unse (Madison VIII) | -0.827 | 7/200 (3.5%) | 0/200 (0.0%) |
| 1000 | writingsofthomas09jeffiala (Jefferson IX) | -0.813 | 61/200 (30.5%) | 0/200 (0.0%) |
| 1500 | writingsjamesmo02unkngoog (Monroe II) | -0.806 | 33/200 (16.5%) | 0/200 (0.0%) |
| 1500 | writingsjamesmo11monrgoog (Monroe V) | -0.810 | 11/200 (5.5%) | 0/200 (0.0%) |
| 1500 | writingsalbertg01gallgoog (Gallatin I) | -0.802 | 59/200 (29.5%) | 0/200 (0.0%) |
| 1500 | writingsofjamesm0007unse_s2a1 (Madison VII) | -0.812 | 10/200 (5.0%) | 0/200 (0.0%) |
| 1500 | writingsofjamesm0008unse (Madison VIII) | -0.816 | 8/200 (4.0%) | 0/200 (0.0%) |
| 1500 | writingsofthomas09jeffiala (Jefferson IX) | -0.823 | 60/200 (30.0%) | 0/200 (0.0%) |

**Blended: 171/1200 (14.2%) at N=1000, 181/1200 (15.1%) at N=1500. Null false-positive rate 0.0% at both N,
every fold. Per-fold false-negative spread: 0.270 at N=1000 (3.5% to 30.5%), 0.260 at N=1500 (4.0% to 30.0%).**

The same check against `LANG_CORPORA["en"]` (its own 5-file corpus, `tools/data/en/`) at the *same* N=1000/1500
(re-run this pass with `tools/data/en/holdout_check.py --n 1000 1500`, not previously computed at these N):

| N | corpus | blended false-negative rate | per-fold spread |
|---|---|---|---|
| 1000 | en18 | **171/1200 (14.2%)** | **0.270** |
| 1000 | en (Holmes/Moby-Dick/Huck Finn/Gatsby/Pride&Prejudice) | 586/1000 (58.6%) | 0.675 |
| 1500 | en18 | **181/1200 (15.1%)** | **0.260** |
| 1500 | en | 648/1000 (64.8%) | 0.710 |

**Register-matching the corpus to the target's own era and genre (era-diplomatic-official prose, not any
novel) cuts the blended false-negative rate by roughly 4x and the per-fold spread by roughly 2.5x at this
target's own decode length**, the same direction of effect pt18 (vs pt17) and, more cautiously, es17c (vs
es17) showed. **Both figures are still well above the amendment's 0.05 per-fold-spread gate** -- this is an
improvement, not a clean pass, and a FAIL/PASS against en18 is still calibrated with a known residual spread,
not a settled result. The driver: Gallatin Vol. I (27.5-29.5%) and Jefferson Vol. IX (30.0-30.5%) read as
outliers when held out against the other four (more Monroe/Madison-heavy) volumes -- Gallatin Vol. I's early
pages carry more domestic-political/Treasury prose than diplomatic despatch language, and several of Jefferson
Vol. IX's later letters are private retirement correspondence from Monticello (philosophy, agriculture,
friends), not official despatches -- while the two Monroe volumes and both Madison volumes, closer in genre to
Armstrong's own despatch, sit at 3.5-16.5%. This is the same shape as `tools/data/en/README.md`'s own finding
(one or two files reading as outliers against a more homogeneous remainder), not a new failure mode.

## specs/armstrong-madison-1808.json

Judge block updated: `language` -> `en18`, `letters_min`/`letters_max` widened to 600/3000 (the previous
200/500 range cannot fit a 369-code decode), and `corpora_note` records the blended rate and spread above
plus the honest caveat that the spread is still over the amendment's gate.

## Requests this job

archive.org: about 16 (2 advancedsearch.php calls not counted separately above the six `_djvu.txt` fetches
that succeeded, plus two `writingsjamesmo0{4,5}unkngoog` fetches that 503'd -- retried once after a pause per
the good-citizen rule, still 503, dropped rather than retried further; Monroe Vol. II and Vol. V were fetched
instead and cover the same span). All >=1.5s apart, one at a time, descriptive User-Agent. No other hosts.
