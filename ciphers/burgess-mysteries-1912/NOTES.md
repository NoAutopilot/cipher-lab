open

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
