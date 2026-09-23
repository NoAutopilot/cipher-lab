closed-negative

Closed-negative for the families in "Families run" below only (solver session, 23 September 2026), each with its
matched control; the families under "What a next solver needs" are untested, so the target as a whole stays
unsolved. Conditional on OCR text (two independent IA scans reconciled), not on page images (rule 2).

# Gelett Burgess, *The Master of Mysteries* (1912) — third hidden message

- Source: QUEUE.md rank 15 (score 33), scored 20 September 2026; catalogued from Aymeloglu's `burgess-1912/`
  target folder and README.

## Check-solved sweep (23 September 2026)

1. **Web search.** "Gelett Burgess Master of Mysteries third hidden message solved 2026" — results confirm the
   two known messages (first-letter-of-first-word acrostic: THE AUTHOR IS GELETT BURGESS; last-letter-of-
   last-word acrostic: FALSE TO LIFE AND FALSE TO ART) but no source reports a third message found; the top
   result is Aymeloglu's own `unsolved-ciphers` GitHub repository, whose description states only "Forster 1644
   letter deciphered Sept 2026" (a different target), not this one. found=false.

2. **Print.** The book is free on Internet Archive (Cornell scan `cu31924022342871`) and Wikisource
   ("Index:The Master of Mysteries (1912).djvu"); no separately published solution to a third message was
   located via web search of Google Books-adjacent sources, Gutenberg, or the LOC Crime Classics 2023 reprint
   (Aymeloglu's own README already logs this last item as an explicitly unchecked gap: "Klinger's 2023 LOC Crime
   Classics edition notes (no preview online; not on IA)"). Google Books API itself: not available in this
   account's environment (no key set here). found=false / one named source still unread.

3. **Community lists.** Aymeloglu's own status-check log (`burgess-1912/README.md`, "Status check for a
   published third-message solve (none found)") already covered: Schmeh's 2021 post and its comments
   (klausschmeh.net), Cipher Mysteries, the Codebreaking Guide unsolved list, Ramble House's own pages, the
   Black Chamber blog (Dec 2021), and general search engines (Brave/Bing/Marginalia/HN Algolia/GitHub) — all
   negative. This sweep's own web search for "Gelett Burgess Master of Mysteries third hidden message solved
   2026" independently reached the same negative result. Cipherbrain/scienceblogs.de: no post on this title
   found via WebSearch snippets; full-page fetch of scienceblogs.de is blocked by this environment's egress
   policy (see ciphers/charles-rupert-1645/NOTES.md item 3 for the exact error), so a direct site search could
   not be run. found=false across every community list checked; one source (scienceblogs.de direct search)
   unreachable.

4. **DECODE.** Not applicable — this is a 1912 printed book with no DECODE record; DECODE covers manuscript
   cipher archives, not printed literary puzzles. Not checked.

5. **Bourdeau (`github.com/dbourdeau/cyphersolver`, shallow clone 23 Sept 2026, MIT code / CC BY 4.0 text).**
   No target folder for this item (`grep -rli "burgess\|master of mysteries"` across the repository returned no
   matches under a target folder). found=false (not attempted by this project).

6. **Aymeloglu (`github.com/aaymeloglu/unsolved-ciphers`, shallow clone 23 Sept 2026; no licence, cite only, no
   code copied).** **found=true, documented attempt, no solve.** `burgess-1912/README.md` (dated 13 September
   2026, "first crack") is an active, detailed negative log, not a solve: it lists every family tested against a
   quadgram-model scorer (`cipherkit.CharLM`) built from the book itself — per-story first/last letter or word at
   fixed offsets, sentence/paragraph/page-level units, diagonal acrostics, contents-page numbers used as indices,
   every-nth-word/letter scans of the whole book, book-wide first/last letters of pages/paragraphs/sentences/
   italics, OCR line-initial/final letters over 15.5k lines, plate captions, and the Introduction's own
   paragraph structure — all negative (the two known messages still rank #1 and #2 under the same scorer, which
   is the control that makes the negatives meaningful). An "Untested ideas" section remains open: Baconian
   biliteral/Donnelly-style word counts, in-story cipher rules reused on the frame narrative, **word-level
   acrostics** (first words of paragraphs forming a sentence — explicitly not yet scored, only letter-level
   units have been), and reading true **printed-page line** units rather than noisy OCR line breaks. `TARGETS.md`
   and `SHORTLIST.md` both list it as Tier 1 #1, i.e. still the project's own top active pick as of the clone
   date. SHORTLIST.md's exclusion table does not list it as solved or dropped.

## Verdict

**Open.** No source checked — web, print, Cryptiana/Cipherbrain, DECODE (n/a), Bourdeau, or Aymeloglu's own
detailed negative log — reports a third message found. This is active, ongoing work by another project
(Aymeloglu), whose own README lists the exact untested families (paragraph-first-word acrostics; true
printed-line units) that QUEUE.md's next_step for this item already targets, so the next step is unchanged and
not yet duplicated by anyone. Per rule 3, none of Aymeloglu's negatives constitute a closed result on their own
without a matched control, and this sweep does not attempt one — it only establishes that the target is still
unsolved.

Stage 2, verified unsolved.


## Solver session, 23 September 2026

### Method

Scripts read, the model judged the hits. `units.py` builds the book from the OCR word coordinates of two
scans; `families.py` extracts every unit sequence, scores it with `tools/english_score.py`, compares it with
shuffles of the same units and with planted messages, and writes `control.tsv`, `runs.tsv` (1,004 rows) and
`top_windows.tsv` (the 15 best word windows of every word family, and the best letter window of every letter
family). The windows were then read by eye. `python3 families.py --check` regenerates all three tables and exits
1 if any committed table is stale (it regenerates them exactly as of this commit; about 2 minutes).

Scorer (`tools/english_score.py`, own code): letters by an interpolated 4-gram model; words by "lift", i.e.
log P(w2 | w1) under a bigram model minus log of w2's frequency in the sequence itself, so common opening words
("oh", "yes", "he") earn nothing for following one another. Both models are built from Doyle's *Adventures of
Sherlock Holmes* and Melville's *Moby Dick* (Gutenberg #1661, #2701, in `tools/data/`), not from this book. So
planted sentences taken from the book are held out. Also recorded: word-cover, the longest stretch of letters
that splits wholly into dictionary words.

### Text sources (`text/manifest.json`)

- **UC**: `masterofmysterie00burgrich` (University of California copy, 1912, 500 ppi). This is the base text.
  Its OCR dropped some lines (for example the last line of "The Assassins' Club", "assassin.").
- **CU**: `cu31924022342871` (Cornell copy, 1912, 300 ppi). This is the second pass. In this scan printed pages
  355-358 are colour-bar noise and page 411 could not be matched.
- **Reconciled text (R)**: each UC page was aligned line by line with its CU page (478 pages). On 435 of 14,902
  aligned lines the two passes differ in their letters; 89 of those lines take CU's reading because it has more
  known words, and 18 lines that only CU has were put back in. After the running heads, folios, plates and
  "THE END" are removed, the text has 480 printed pages, 3 introduction pages, 15,105 printed lines, about 3,500
  paragraphs (found from indentation, or from the line before being short) and about 10,200 sentences.
- **Drop capitals**: 12 stories open with a two-line drop capital that neither OCR pass reads. The first word
  was restored from the letters that survive and from sense (`units.DROPCAP`, grade I): UNDERNEATH, OH, I,
  SURELY, GASPING, EVERY, LATE, BE, UNLESS, GRACIOUS, EXCUSE, SHE. Page images were not fetched to confirm them.
- **Wikisource**: the API answered HTTP 429 twice, so the session stopped using it, and no Wikisource text is
  in this folder. `fetch_wikisource.py` is a polite batched fetcher for a later session.
- **Requests**: archive.org 13, en.wikisource.org 3, gutenberg.org 3 (one search, two texts). The details are
  in the manifest.

### Control (rule 3; `control.tsv`)

| control | result |
|---|---|
| Family A, the two known messages among all 560 distinct 24-letter strings (unit word/sentence/paragraph/line/page x position 1-8 from either end x letter 1-2 from either end x forward/reversed) | FALSETOLIFEANDFALSETOART rank 1 (quad -1.065, shuffle z 3.16, word-cover 24); THEAUTHORISGELETTBURGESS rank 2 (quad -1.305, z 3.09, cover 11); best other string AKEYOMEADTOGTYONDPRESOLD at -1.461 (z 2.89, cover 7). **Margins 0.395 and 0.156 in quad** |
| Same family from each single OCR pass | UC 1 letter wrong in 48 (ALD for AND), CU 1 wrong (LRF for LIF); the drop capitals restored as above |
| D: 24-letter book sentences planted in book-wide printed-line initials (15,026 letters) | 40/40 recovered as the best window. Mean planted quad -0.884; the natural best window is -1.468 |
| D, E, F: 10 plants in every letter family, in its own sequence | recovered as the best window in 8-10 of 10 in every family (mean 9.7) |
| B: a 24-word book sentence treated as a story-level word sequence | z >= 3 in 38/40 (median z 4.94) |
| C: 6-, 8- and 12-word book sentences planted in first or last words of paragraphs, sentences and lines | best window in 7-33 of 40, depending on the family and width; among the top 15 windows (which were read by eye) in 12-36 of 40 |
| C, per family (10 plants each, `runs.tsv` note column) | best window 0-10/10 (mean 5.3); top 15 4-10/10 (mean 7.4) |
| F: every-nth-letter plants in the Introduction | ranked first among 2,293 (n, offset) choices in 10/10 |

The word-level controls are the weak point. Openings of paragraphs and lines are drawn from a small vocabulary
of interjections and pronouns, and those form English-looking bigrams by chance. A short word-level message (6-8
words) in first words of lines or sentences can therefore be missed about half the time, even in the top-15 read.

### Families run (`runs.tsv`)

| family | what | rows | best result | reads as English? |
|---|---|---|---|---|
| A story-level letters | letter 1-2 from either end of the k-th (1-8) word, sentence, paragraph, printed line or page from either end of each of the 24 stories; forward and reversed | 560 distinct | the two known messages at 1 and 2; next -1.461 | only the two known messages |
| B story-level words | k-th word (1-12) from either end of each story; first/last word of the k-th (1-5) sentence, paragraph, line, page; forward and reversed | 208 | max z 3.28 ("Ring didn't Fools acteristics that It Calendon ...") | no |
| C book-wide words | first and last word of every sentence, paragraph, printed line and page, forward and reversed, best windows of 6, 8 and 12 words by lift | 48 | max z 4.36 ("it all exclaimed here then you up i already him him that", paragraph last words reversed); the 240 top 8-word windows (15 x 16 sequences) read by eye, and the best 6- and 12-word window of each sequence | no |
| D book-wide letters | letters 1-3 from either end of every sentence, paragraph, printed line and page, forward and reversed, best 24-letter window + word-cover | 48 | best window -1.149 ("AFTOESDENDREGUELESAMSTAN"), max z 1.93; longest cover 22 (short-word chains) | no |
| D per-page printed lines | letters 1-3 from either end of the lines of each page, page by page | 6 | best page -1.282 (p. 326, "ERSAULSEESETTEDIDIOENTIR"), z 3.45 against 472 pages | no |
| E titles/contents | letter 1-5 from either end of each title; first/last letter of title word k; all title-word initials and finals; contents page numbers and story lengths mod 26 | 52 | best -1.314 ("EETENRYENTENGES", from title-word finals) | no |
| F introduction | letters 1-3 from either end of every word, sentence, paragraph and line; first/last words of sentences, paragraphs and lines; every n-th letter (n 2-60) and every n-th word initial (n 2-30) at all offsets | 77 | letters -1.106 (window), words 2.103 ("yes of the second"), every-nth max z 3.30 among 2,293 choices ("...GIWASSTOLD...") | no |
| G plate captions | first/last letters and first words of the 19 UC plate captions | 5 | max z 0.87 | no |

These overlap Aymeloglu's letter-level negatives (13 Sept 2026) but are not the same text or scorer: here the
text is printed lines from word coordinates and his was OCR line breaks. Two families he listed as untested
are covered: word-level acrostics (B, C, F) and true printed-line units (D, B, C).

### Result

No candidate. Nothing beat the control margin and also read as English:
- In the letter families, some best windows score above the weaker known message (-1.305). These are all
  letter-2 and letter-3 streams, which are rich in E, T and H by construction, and none of them segments into
  English.
- In the word families, no window read is a phrase a reader can follow.

### Grading (rule 4)

No reading is claimed: 0 tokens graded (H 0, C 0, S 0, M 0, I 0). The control uses the two known messages,
which were found by others (known before 2021, Ramble House; see Aymeloglu's README). Twelve of their 48
letters come from drop capitals restored at grade I, and the other 36 are read by both OCR passes, or by one
pass where the other is wrong at one letter each.

### Where it was not found

- No candidate phrase came up, so none was phrase-searched.
- Web search on 23 Sept 2026 for "Master of Mysteries" Burgess "third cipher" OR "third message": the results
  were Schmeh's post (scienceblogs.de), Ramble House, Wikisource, the Black Chamber blog (6 Dec 2021) and the LOC
  Crime Classics 2023 post. None reports a third message read.
- Aymeloglu's log (github.com/aaymeloglu/unsolved-ciphers, `burgess-1912/README.md`, 13 Sept 2026; cited, no code
  copied) is negative for the letter-level families listed in the check-solved section above.

### What a next solver needs

- **Page images**, to confirm the 12 drop capitals, read the four plates, and look at the typography.
- **Untested families:**
  - Baconian biliteral in two founts or italics; this needs the images.
  - Donnelly-style word counts keyed to page/column/line.
  - The Lorsson Elopement's Bible chapter:verse rule applied to the frame, or to the contents numbers.
  - Dalrymple phonetic French.
  - Word-level acrostics weighted by a stronger language model than a bigram. The C control shows a 6-8-word
    message can be missed about half the time.
  - The last word of one unit read with the first word of the next.
  - Klinger's 2023 LOC edition notes (unread).
- **Wikisource page text**, as a third transcription (the API returned 429 on this day).
