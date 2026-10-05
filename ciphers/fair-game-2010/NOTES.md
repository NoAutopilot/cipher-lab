# fair-game-2010

open
Minimal check-solved, 25 Sept 2026 (LANE B3 worker bFAI), before any transcription/solve (intake step, `.claude/briefs/breadth.md`): Cipherbrain post 36 (Schmeh, 13 Apr 2017, scienceblogs.de/klausis-krypto-kolumne, already on disk as `sources/schmeh/posts/36-fair-game.txt`/`.html`, fetched by bSPEC2 this same window) and its comment thread read in full: no solution posted by any commenter. Schmeh's own text: "not much can be found about the Fair Game code online... nothing seems to have been published about this mystery." One commenter ("Martin Halpin", the only comment ever posted under that name, 2014-15 window) proposed reading the letter immediately after each marked letter instead of the marked letter itself -- Schmeh states this is untested by him. A second commenter, James Mulliss (9 Feb 2023, comment #5/#6), transcribed the actual credit words containing each of the ~64 marked positions (word with the marked letter capitalised), which is real primary-source context text, not just the AboveTopSecret marked-letter sequence -- this is the "original unmarked credits text" the spec's test 1 says is needed, already on disk, no new fetch required for it. Both solver repositories grepped via shallow clone (github.com/dbourdeau/cyphersolver, github.com/aaymeloglu/unsolved-ciphers; cloned to /tmp, grepped, deleted, not committed): cyphersolver's `TARGETS.md`/`top50/NOTES.md` list Fair Game among items "open but not settleable by cryptanalysis", grouped with Shugborough/Powers as "Ten letters; a disputed transcription of film credits" (that repo counts 71 letters, not 68 -- a source discrepancy, not reconciled this pass); aaymeloglu/unsolved-ciphers `SHORTLIST.md` describes the SAME Halpin-type hypothesis independently ("A 2014 anonymous commenter claimed the yellow letters mark the letters that follow them") and recommends "Enumerate marker schemes (next letter, previous letter, first letter of next name, offsets) and check for an English sentence" -- confirming this specific test has not been run and reported anywhere found. It also flags two later Schmeh posts with "complete screenshots" (2017-06-22) and a "2019 revisit" -- not fetched this pass, out of scope (imdb.com is the only extra host this brief allows). OpenAlex (`api.openalex.org/works?search=`, key header) for "Fair Game film cipher yellow letters credits": 125 hits, none relevant (film-studies/Indigenous-history/comics papers, no cryptography match). Semantic Scholar (`api.semanticscholar.org/graph/v1/paper/search`, key header) for "Fair Game film cipher yellow letters end credits": 0 hits.

Status: open, unsolved by any source checked. Proceeding to cheap test 1 (Halpin "next letter" hypothesis, using the James Mulliss comment-thread transcription already on disk) per brief `.claude/briefs/runs/2026-09-25-lane-b3-fair-game-2010.md`.

Intake gate check (`python3 tools/intake_gate_check.py fair-game-2010`):
```
fair-game-2010: open (line 3) -- edition/page or full-text-search citation found within 6 lines
exit=0
```
Proceeding.

## Cheap test 1: Martin Halpin "next letter" hypothesis (25 Sept 2026, LANE B3 worker bFAI)

Data: James Mulliss's real credit-context transcription (comment #5/#6, already on disk, see intake
paragraph above) gives the actual word each of ~65 recoverable marked letters sits in -- the "original
unmarked credits text" cheap_tests_in_order[0] called for; no IMDb fetch was needed once this was found in
the post already on disk (the spec's proposed IMDb route was written before this comment was located).
Multiset check: the 65 letters recoverable this way match the ciphertext's 67 known letters exactly except
one missing S and one missing T -- strong corroboration this is the real marking (not fabricated), but the
transcription is incomplete by 2/67 and the commenter's list order is an UNVERIFIED proxy for the true
credit-roll order (a caveat on the negative below).

Procedure: for each marked occurrence, in list order, take the letter immediately following the mark
inside its word (a documented proxy -- next listed word's first letter -- for the handful of marks that
are a word's last letter). Script: `specs/cheap-tests/fair-game-2010/run_test1.py` +
`credits_words.py`; output `specs/cheap-tests/fair-game-2010/test1_output.json`.

**Target**: next-letter sequence (65 letters: `tatdmotaeaepmlefciceaselrtirinseoranaeouiugleaobadoauearussvwberr`)
judged with `tools/judge_plaintext.py specs/fair-game-2010.json`: language score -2.202 (random-null p99
-1.77, real-English p05 -0.944), word cover 0.462 (min 0.6) -- **FAIL**.

**Control (a), planted-name sanity check**: same extraction procedure, same word pool, marks placed to
spell a known 13-letter name (ROBERTJOHNSON, unrelated to the film's plot) -- recovered exactly in 3/3
trials. Confirms the procedure and script work correctly and can recover a real signal when one exists.

**Control (b), random-marking false-positive rate**: 3 trials of random marks in the same word pool at the
same N=65: judge FAIL on 3/3 (scores -2.134 to -2.261, word cover 0.246-0.523). The real target's score
(-2.202, cover 0.462) sits **inside** this random-noise band, not below or above it.

**Verdict**: control-backed negative for this specific reconstruction of the Halpin hypothesis -- the real
target's next-letter sequence is indistinguishable from random-marking noise of the same design, while the
sanity control confirms the test has power to detect a real signal. Caveated per the missing-2-letters and
unverified-order limitation above: this negative applies to this particular reconstruction of the mapping,
not to every possible true ordering of the same underlying words. Does not close the target on its own
(only test 1 of 3 run this pass, per brief; do not run test 2).

Status stays `open` (a single cheap test's control-backed negative is not `closed-negative` per rule 5 --
the full ladder for this target is only one test long so far). No NEAR.md candidate: this is a clean
negative with its own control landing in the expected band, not a control-below-gate gap.

Requests this pass: github.com 2 shallow clones (dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers;
grepped, deleted, not committed), api.openalex.org 1, api.semanticscholar.org 1. No imdb.com or
web.archive.org requests needed (real data already on disk covered the test). No subagents.

## Web and blog check (GF4-BATCH21 (account-4), 3 Oct 2026)

Plain web searches (WebSearch, 3 Oct 2026): (1) `"Fair Game" 2010 film end credits yellow letters code` -- Cipherbrain posts (2017-04-13 post 36, 2017-06-22 screenshots, 2019-09-22 revisit, the "Fair Game Code" page), IMDb crazy credits, Wikipedia, AboveTopSecret thread833418, an oddheader fandom list; all describe it as unsolved; (2) the two ciphertext lines in quotes (`"CESOAPCHFHTEOPISFMNADAMECAOREDATN" OR "RAYUURNQWKNUFRCOJRWRMDGSEHUWTOAKRA"`) -- no relevant hit (unrelated Wikipedia/CJK/datasheet pages); (3) `"Fair Game code" solved OR solution` -- only Codeforces problem 864A pages, nothing on this item; (4) `"Fair Game" credits cipher solved Claude OR GPT OR "ChatGPT"` -- model-solve announcements for the Urquhart Cyphral Distich (Schneier, dev.to, itdoeswhatnow, explainx), nothing on Fair Game; (5) `"Fair Game" Plame movie credits highlighted letters hidden message reddit` -- IMDb trivia ("coded message ... not yet decoded"), a Tumblr post of 17 Oct 2012 (justanothercinemaniac.tumblr.com/post/33813314733, opened: "Apparently there is a coded message in the end credits of the film that IMDb has yet to decode", no reply with a solution), film review pages. The item has no separate shelfmark; query 1 is the descriptive title.

Blog site searches, in order:
- Cipherbrain (`scienceblogs.de/klausis-krypto-kolumne/?s=Fair+Game`): 8 posts; every one opened and its comment thread read live on 3 Oct 2026:
  - 2014-10-12 "Der versteckte Code im Abspann des Films 'Fair Game'" (10 comments, 12 Oct 2014-24 Jul 2015): Martin Halpin's "following letter" comment (13 Oct 2014); **Sansibar, 22 Jul 2015, a partial anagram, not a decipherment**: "Aus einzelnen Buchstaben läst sich ein sinnvoller Satz zusammensetzen: YOU WISH TO KNOW HOW TO CRACK SECRETS ? und vielleicht: RUN APACHE MADAME AND FRAME", with the leftover letters listed as "Restbuchstaben ohne Lösung"; nobody accepts it; Braunschweiger (24 Jul 2015): the redacted "Hammad" role is not in the screenplay.
  - 2015-07-22 "Noch immer ungelöst ..." (no comments): "Leider gibt es bisher keine heiße Spur zur Lösung des Kryptogramms."
  - 2015-07-22 "Fair Game Code" page (credits transcription, "under construction"): 1 comment (Braunschweiger, 24 Jul 2015, upper/lower case may matter); no solution.
  - 2017-04-13 post 36 (live thread re-checked against the on-disk 25 Sept copy): still 6 comments, latest James Mulliss 9 Feb 2023; **no comment added since 25 Sept 2026**; no solution.
  - 2017-06-22 "The Fair Game code: Here are the complete screenshots" (Rossignol's screenshots; 15 comments, 24 Jun 2017-3 Nov 2020): next-letter sequences by Rich SantaColoma (only scattered words), Racingdevil48 (19 Apr 2019, "TAT?DAMOTAEAYEPMLEFCICEASEARTIRINSEORANAEOUIUGLEAOSADOAUEAYRUSSVWBERR", no meaning found), Cyarutchiii (29 Feb 2020, a refined string); speculation by BREAKER (El Chapo / Sean Penn) and Michael Victor (rearranged fragments); no plaintext.
  - 2019-09-22 "Revisited: The Fair Game Code" (10 comments, 22 Sep 2019-22 Mar 2021): Schmeh lists transcription uncertainties and alternative adjacent-letter sequences; **CrazyT, 10 Jan 2020, a tentative partial reading, withdrawn by its own author**: "...YOU NAME THE DEVANIC KILLER TO VIPMANNAGER AND WIN AN INSTANT SOUND...", revised 12 Jan 2020 to fragments "TH|ED|ICK|ER|SON|SVIDEOSOURCE" and "M|I|LLER" with "I'm still clueless about the rest"; no reply from Schmeh; nobody accepts it.
  - 2021-05-11 "A Crypto Classic: The Fair Game Cryptogram" (no comments): "The meaning of these letters is unknown to this day".
  - 2021-05-11 "Ein Krypto-Klassiker: Das Fair-Game-Kryptogramm" (7 comments, 12-14 May 2021): dexter and Dg point out that the clear line "Democracy only works if you do your part" appears in the credits (4th-from-last screenshot); no solution.
- klausschmeh.net (`?s=Fair+Game`): two pages, both opened: "The Fair Game Code" gallery (Rossignol's high-res screenshots and his transcript; "so far no one has succeeded in deciphering it") and portfolio/the-fair-game-code (dated 24 May 2026: "Nevertheless, the solution is still unknown"); no comments on either. The "Solved cryptogram" category: 4 posts (Koehler, Copenhagen, WWII Enigma, ADFGVX); nothing on Fair Game.
- Cryptiana: on-disk `sources/cryptiana/` grepped for `fair.?game`: no hit (zero requests); live blog `cryptiana.blogspot.com/search?q="Fair Game"`: "No posts matching the query".
- Cipher Mysteries (`?s="Fair Game"`): only idiomatic "fair game" hits (Wikipedia, Tamam Shud, Voynich posts), nothing on the film; `?s=Plame credits`: "Nothing Found".
Unreachable: IMDb crazy credits (`imdb.com/title/tt0977855/crazycredits/`) HTTP 403; AboveTopSecret thread833418 HTTP 522; neither retried.

New-publication check: apeiron.re front page (an ASCII logo and "Pushing the limits of adversarial engineering", no listing of items; nothing on Fair Game); Cabinet Noir (github.com/el-descifrador/cabinet-noir, sibling's shallow clone at /tmp/claude-0/cabinet-noir, HEAD 47b6db9, 2 Oct 2026, 26 target folders of 1568-1824 nomenclators) grepped for `fair.?game|plame`: no hit.

Result: no decipherment or plaintext of this item located by these queries on 3 Oct 2026 (a search result, not a novelty verdict, rule 10). Two partial comment-thread readings exist (Sansibar 2015 anagram, CrazyT 2020 tentative and withdrawn); neither is complete or accepted. Any later reading must be compared against both, and against the next-letter strings above, before novelty is classed. Status word unchanged.
Requests: WebSearch 5; scienceblogs.de 11 (WebFetch); klausschmeh.net 4; cryptiana.blogspot.com 1; ciphermysteries.com 2; apeiron.re 1; imdb.com 1 (403); abovetopsecret.com 1 (522); tumblr.com 1; github.com 0 (sibling's clone). One request at a time per host.

## Premise check (GF4-BATCH21 (account-4), 3 Oct 2026)

(a) Folder's own mentions: **not found** -- NOTES.md and specs/fair-game-2010.json mention no decipherment or clear copy, only the Halpin hint and the Mulliss credit-word list (used in test 1). Comment threads hold two partial readings (above), neither a decipherment. One premise flag: the spec's ciphertext is AboveTopSecret's sequence. Schmeh's 2019 revisit lists transcription uncertainties, and Rossignol's complete transcript and high-res screenshots (klausschmeh.net gallery) now exist, so the spec's text may not match the best transcription (rule 2). This was not checked this pass; no images were viewed.
(b) Other solvers' working files: **not found** -- the Aymeloglu snapshot rows (`sources/solver-diffs/2026-10-03-aymeloglu.tsv`, re-checked 3 Oct 2026) list it as "listed as a candidate; no attempt"; the on-disk cyphersolver snapshots (`sources/cyphersolver/2026-10-0{1,2,3}`) have no `fair.?game` hit; Cabinet Noir has no hit. No rendering of the sequence under any key in any of them.
(c) Neighbours: **found, not a decipherment** -- the credits carry a clear line, "Democracy only works if you do your part" (Cipherbrain comments, 12-14 May 2021). This is a possible crib or closing message, not a reading of the marked letters. The commenter-derived next-letter strings (Racingdevil48 2019, Cyarutchiii 2020) are alternative ciphertexts, not plaintexts. IMDb crazy credits/trivia were unreachable (403). Valerie Plame's memoir *Fair Game* (2007), the film's source, was not searched; no source links the marking to it.
(d) Recipient's side: **not applicable / not found** -- there is no addressee. The production side (Schmeh's guess that the producers planted the Halpin hint) has published nothing that was found. Schmeh's own 24 May 2026 page still says "the solution is still unknown".
Verdict: the premise holds -- no decipherment or plaintext of the marked letters was found in the folder, in the solver files, on neighbouring material or from the production side. The item stays `open`. Before any test 2, reconcile the spec's ciphertext with Rossignol's transcript.

Gate after this pass (3 Oct 2026, GF4-BATCH21):
```
fair-game-2010: open (line 3) -- edition/page or full-text-search citation found within 6 lines
exit 0
```

## Ciphertext reconciliation against Rossignol's screenshots (GF4-BATCH22 (account-4), 3 Oct 2026)

Answers GF4-BATCH21's premise flag (rule 2, image over transcription). Sources: (i) the spec's ciphertext, AboveTopSecret's sequence via Cipherbrain post 36; (ii) Schmeh's page `klausschmeh.net/portfolio/the-fair-game-code/` (dated 24 May 2026), which prints `ces?oapchfhteopisfmnadamecaoredatn` / `rayuurnqwknufrcojrwrmdgeushwtokara`; Rossignol's "transcript" is the set of 25 screenshots, not a typed text; (iii) the screenshots themselves, `klausschmeh.net/wp-content/uploads/2026/06/BFG03.png`-`BFG25.png` (BFG04 as `BFG04-1.png`), with BFG01-02 from `scienceblogs.de/klausis-krypto-kolumne/files/2017/06/`. All 25 were fetched 3 Oct 2026, 1230x1080 px. They are kept in the session scratchpad only, not committed.

Method: a script found the marked letters by colour. Marked letters are amber, about (160-200, 120-160, 40-60) RGB, while the normal credit text is near-white. Blobs repeated where consecutive frames overlap were dropped (same x within 3 px, the bottom of frame k and the top of frame k+1; 9 dropped). The two adjacent marked letters "CO" of FRANCO were one blob. Each blob's row was cut into one contact sheet that was read once by eye. The uncertain glyphs (rows 4, 48, 56, 57, 59, 65 of the sheet) were then checked as text renderings of the blob masks, not by more image reads. The result is `reconcile_2026-10-03.tsv`: one row per position with the spec letter, Schmeh's 2026 letter, the image letter, the frame, y, x, the credit word and agreement.

Result: the image gives 67 visible marked letters plus the one hidden under the white bar (BFG03, line 1 position 4, still `?`). **62 of 68 positions agree in all three. The image letters agree with the spec at every position (67/67 visible).** The six differences are all line 2 positions 24-27 and 31-32. They are order, not letters: spec `SEHU ... OAKR`, Schmeh 2026 `EUSH ... OKAR`. Both strings have the same letters. In frames BFG22-BFG24 the end credits switch to a two-column music-cue block (x of the marks: 890 right, 236 left, 918 right, 465; then 363 left, 979 right, 298 left, 969 right). Read top to bottom in scroll order, as the screen shows them, the block gives the spec's `S E H U ... O A K R`. Read column by column it gives Schmeh's `E U S H ... O K A R`. The image cannot say which order the maker meant. Both orders are logged in the TSV, and test 2 (substitution anneal) should run both: a monoalphabetic score ignores order only for unigram statistics, not for the n-gram judge. Two marked letters in this block are lower case in the credit (Courte**s**y, M**u**sic), and so is the next mark, the w of ABCNe**w**sVideoSource. The case may matter (Braunschweiger, 24 Jul 2015, Cipherbrain).

Spec: **not changed.** The reconciled scroll-order text equals the spec's ciphertext. The column-order variant is recorded here and in the TSV, not in the spec (the brief allows a spec edit only if the reconciled text differs).

Possible crib, not tested (brief): the credits carry a clear line, "Democracy only works if you do your part" (fourth-from-last screenshot; Cipherbrain comments of 12-14 May 2021), and one marked letter is the G of "TAKEPART.COM/FAIR GAME" (BFG22, y 255), the film's TakePart campaign. "do your part" / "takepart" may relate to the hidden message's theme or be its plaintext's closing. Noted only.

Requests: klausschmeh.net 3 pages + 23 images; scienceblogs.de 2 images; at least 3.2 s apart, one at a time. No 403/429. Vision: one contact-sheet read.

## Cheap test 2: simple substitution on both credit-block orders (3 Oct 2026, GAPS71-fair-game-2010, account-4)

Both orders from `reconcile_2026-10-03.tsv` (GF4-BATCH22): scroll order (spec/ATS, line 2 `...GSEHUWTOAKRA`) and
column-wise (Schmeh 2026, `...GEUSHWTOKARA`), 67 known letters each (position 1:4 dropped), N=67, K=21, same multiset,
in `test2/order_scroll.txt` and `test2/order_column.txt`. Tool: `tools/family_run.py specs/fair-game-2010.json
--family masc --cipher <order> --seeds 5`, en corpus, rows in `HYPOTHESES.md`.

| order | control mean (8 / 32 restarts) | gate 0.6 | target judge (run at gate 0.5) | shuffle floor (seeds 7-10) |
|---|---|---|---|---|
| scroll (spec) | 0.537 / 0.591 (0.179-0.791) | below | FAIL -0.985 (real_p05 -0.92, null_p99 -1.837) | -1.11 to -1.38 |
| column-wise | 0.537 / 0.591 (same control) | below | FAIL -1.290 | -1.14 to -1.27 |

The control is below its gate at both restart counts and not at ceiling, so neither FAIL is a negative: a non-test at
N=67 with this instrument (rule 3). The scroll order's judge score is above all 8 shuffled decodes but below real_p05,
and its decode is not English (`dnotsudeleantupolarstsandstentsaresitter...`); the anneal score does not separate
target from shuffle (-150.9/-151.6 vs -151.6 to -153.7). The en judge has unknown reliability (EN-FOLDS). Test 3 (per
line, N=34) would be a weaker non-test with the same anneal. Not run: the crib GF4-BATCH22 noted (per brief). Next
step needs a different instrument, not more restarts: a crib/word-constrained solve, or the marker-scheme sweep
aaymeloglu's SHORTLIST proposes.

## Next step (NO-CRACKS, 5 Oct 2026)

next: a crib/word-constrained solve or aaymeloglu's SHORTLIST marker-scheme sweep (a different instrument, not more anneal restarts; rule 3's third-attempt clause), with a matched control at N=67, ~$3. Who acts: agent. Source: this file's last paragraph ("Next step needs a different instrument"); written by NO-CRACKS (account 3) because tools/next_steps.py found no next-step line in this file.
