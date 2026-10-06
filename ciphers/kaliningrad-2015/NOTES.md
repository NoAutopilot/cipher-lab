open
Check-solved intake sweep (LANE B2 bINT, 25 Sept 2026): sources/schmeh/posts/19-kaliningrad.{html,txt} (Cipherbrain post 19, 17 Oct 2017, 58 comments) read in full -- two unconfirmed self-reported "solved" claims found (Thomas Ernst, Oct/Nov 2017; "Frank", 19 Feb 2021), neither ever published a plaintext or method, and they contradict each other on content; dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers shallow-cloned, grepped for kaliningrad/baltiysk, deleted -- cyphersolver carries a dedicated `kaliningrad/` target folder recording its own attempt: transcription abandoned as too error-prone, no cryptanalysis attempted, outcome "not solved"; one OpenAlex and one Semantic Scholar query for "Kaliningrad Baltiysk bottle cipher cryptogram" returned no relevant results. See "Check-solved sweep, 25 Sept 2026" section below for the full log.

# kaliningrad-2015

status: open

## What this is

Two sheets of paper (a torn front sheet with 20 lines, and a separate second sheet with 6 lines,
not its reverse) found rolled in a bottle during excavation work on Lenin Street, Baltiysk
(formerly Pillau), Kaliningrad Oblast, in 2015. First reported in a Russian local-news article
(strana39.ru, 2016) and covered by Klaus Schmeh as no. 19 on his Top 50 unsolved list
(scienceblogs.de/klausis-krypto-kolumne, 17 Oct 2017; comment thread has 58 comments, no solve).
Source page saved at `sources/schmeh/posts/19-kaliningrad.{html,txt}`.

## Search before solving (rule 1)

Not run fresh this session (out of scope for a breadth cheap-test-1 worker; the spec itself
(`specs/kaliningrad-2015.json`, written 24 Sept 2026) already records: "open per Schmeh 2017;
nothing later found 24 Sept 2026"). The saved Schmeh post's 58-comment thread was read in full
this session and contains no claimed solution, only structural speculation (Thomas Ernst's
autokey/Cardano guess, comment #36) and an image-forensics offer from a Moscow specialist
(Alex Ulyanenkov, comment #37) that trails off without a transcription or reading. Not
independently re-checked against DECODE, the solver repositories, or the archive catalogues this
session; a future worker running check-solved should do that before any campaign (CLAUDE.md
pipeline step 2).

## cheap_tests_in_order[1] -- transcription + images (this session, 25 Sept 2026)

**Images.** Fetched both cryptogram photos named in the post directly from scienceblogs.de
(`ciphers/kaliningrad-2015/images/`, manifest.json with sha1). A third image in the post
(`Kalinigrad-Frequencies.png`) is a reader's own frequency-count graphic, not a third page of the
cryptogram, and was not fetched.

**Transcription.** The brief pointed at "the Russian thread" (simple_life.dirty.ru, linked from
the post, line 171 of the saved text) for the full transcription, but the saved Schmeh post
itself already carries a complete, line-numbered transcript: Thomas Ernst, comment #32
(22 Oct 2017, `#comment-924706`), who transcribed both sheets letter-by-letter from the images
after an earlier attempt (comment #31) was silently dropped by the site's comment filter. This
transcript is the one used here (`ciphertext.txt`), credited in its header; the Russian thread
was not separately fetched (it is a discussion of the same cryptogram by different commenters,
not a second source image, and fetching it was not needed once Ernst's transcript was found
on the page already on disk).

Ernst's own transcription convention (his note, comment #31): he replaced a Cyrillic
hard-sign-like glyph -- described in the thread as looking like a "2" turned upside down -- with
the Latin letter "x" throughout. That is a labelling choice, not a claim about the plaintext
language; `ciphertext.txt`'s header records it so a later worker does not read "x" as literally
attested in the manuscript.

**Row-level agreement check (this worker's own pass against the images).** Read both fetched
images directly and compared word-for-word against Ernst's transcript, line by line. All 26
lines (20 in section I, 6 in section II) match in word count, word shape and letter sequence at
the resolution the photos allow; the only systematic difference found is exactly the "x" for the
hard-sign-like glyph noted above (e.g. image line I/1 reads as `elhxikiracel` at a glance where
the transcript has `elhxikixacel` -- same glyph, different label). No line was found where a
word is missing, added, or reordered relative to Ernst's transcript. This is a spot-check at
normal photo resolution, not a second blind pass with a reconciler (out of scope for cheap test
1; a real second pass would need higher-resolution crops of individual lines, which test 1's
budget did not cover).

**Counts.** `scripts/ic_analysis.py` tokenises `ciphertext.txt` into signs (apostrophe- and
diaeresis-modified letters counted as one sign each, per the alphabet Thomas describes in the
post) and reports:

```
N=978 K=36 IC=0.0657
```

N=978 signs is close to the sum of Ernst's own seven running character-counts per repeated
section (194+194+187+199+166+5 = 945; the difference is tokenisation choices around the four
dotted groups like `x.s.f.d.` and the two section headers, which this script splits into
individual signs). K=36 is one below reader Thomas's count of 37 in the post (comment #4); the
difference is plausibly the "f2" mark on the first "f" of line I/13, which Ernst flags (comment
#32) as possibly a doubled apostrophe rather than a distinct sign, and which this script folded
into a single sign rather than inventing a 37th class. IC=0.0657 differs from Thomas's own
reported ~0.054 (comment #5); this is very likely a sign-boundary artefact (whether an
apostrophe merges into the preceding letter as one sign, as done here, or is scored as a
separate symbol) rather than a disagreement about the underlying text -- flagged, not resolved,
since resolving it is test 2's job (an annealer needs one fixed convention, and cheap test 1 is
not that).

**Matched-N controls.** `scripts/matched_controls.py`, 20 windows of N=978 letters each, seed 42:

```
target:                    N=978  K=36  IC=0.0657
ru (transliterated, 30774): IC mean=0.0563  range=(0.0543-0.0605)   [Gutenberg 30774, "Московия в представлении иностранцев XVI-XVII в.", one fetch]
de (composed_enhg.txt):     IC mean=0.0724  range=(0.0676-0.0765)   [tools/data/de16, existing corpus, only 6855 letters so the 20 windows overlap heavily -- not fully independent]
```

Polish was not fetched (the spec allows "one Gutenberg fetch at most"; that one fetch was spent
on Russian, the language the spec and Thomas both flag as the most likely candidate on IC
grounds, and a first Gutenberg attempt at a Russian text, id 19681 "Детство", turned out to be
an audiobook readme with no prose body and was discarded before the working fetch of id 30774).

The target's IC (0.0657) sits above the Russian control's range and inside/near the German
control's range, at K=36 (vs the corpora's natural alphabet sizes, ~32-33 for transliterated
Russian, ~30 for German). Not informative on its own for language choice -- a K=36 alphabet
that splits many letters into hard/soft or plain/modified pairs would, if the plaintext really
is a simple substitution or a straightforward transliteration, be expected to show a *lower* IC
than a natural-alphabet control of the same language, not a higher one; the target does neither
relative to Russian (higher, not lower) nor sits cleanly inside German's range either. This is
a test-1 observation for test 2 to use, not a verdict; no candidate plaintext, no annealing, no
periodic-IC (cheap test 3) was attempted this session per the brief ("run cheap_tests_in_order[0]
... nothing else").

## Files

- `ciphertext.txt` -- as transcribed (Ernst's comment #32), with the source and the "x for
  hard-sign glyph" convention documented in the header. Never silently repaired (rule 2).
- `images/cryptogram1.png`, `images/cryptogram2.png`, `images/manifest.json`.
- `scripts/ic_analysis.py`, `scripts/matched_controls.py`, `scripts/ru_gutenberg_30774.txt`
  (the fetched Russian corpus, kept so a later worker does not re-fetch it).

## Grades (rule 4)

No reading claimed this session -- transcription and counts only. Not applicable.

## Rule 10

No novelty claim made. This is open per Schmeh 2017 and this session's read of the comment
thread found no solution posted there.

## Check-solved sweep, 25 Sept 2026 (LANE B2 bINT, intake gap after QA/2026-09-25-1740.md failure 3)

Ran the minimal check-solved sweep this brief names (not a full six-source rule-1 sweep) to close the gap
flagged in QA: this target had a cheap test (transcription/images) run with no check-solved verdict on file.

1. **Cipherbrain post 19 and its comment thread** — `sources/schmeh/posts/19-kaliningrad.{html,txt}`, already
   on disk, not re-fetched. Read in full (58 comments). Two unconfirmed self-reported solve claims, from two
   different commenters, that contradict each other and neither of which was ever substantiated with a
   published plaintext:
   - **Thomas Ernst** (Latrobe), 31 Oct 2017 (#50/#51): "I have the cipher text. I have the plaintext... as of
     this Halloween, October 31, 2017, consider the contents of the cipher solved." Follow-up comments (7 Nov
     2017, #52) describe the plaintext as "political in nature" but say working out the *cipher mechanism*
     (a cross-language polyalphabetic scheme) is still in progress. Three later commenters (Harald, Alex
     Ulyanenkov, Hans) ask him to post the plaintext; he never does on this thread.
   - **"Frank"**, 19 Feb 2021 (#58, the thread's last comment): "I got the plaintext. It is from a chapter of
     the first Orthodox bible translation which was edited by the Metropolitan of Moscow Filaret and released
     in 1876. I hope to be able to publish the encryption method... here soon." No follow-up comment exists on
     this thread after this one.
   Neither claim is corroborated by the other (Ernst: a "political" text via a cross-language polyalphabetic
   cipher; Frank: a chapter of the 1876 Russian Synodal Bible), no plaintext was ever posted publicly by
   either, and the blog itself later stopped taking comments — this is two unresolved leads, not a solve.
2. **Solver repositories** — `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers` shallow-cloned to
   `/tmp`, grepped case-insensitively for `kaliningrad`, `baltiysk`, `kalinigrad`, deleted immediately after.
   cyphersolver carries a dedicated `kaliningrad/` target (`NOTES.md`, `profile.json`) recording its own
   attempt: transcription from the two published photographs was tried and abandoned as too error-prone
   ("faint cursive, bleed-through... cursive n/u/v/w barely separable"), so no cryptanalysis was run;
   `profile.json`'s `outcome` is `"method": "not solved"`, `"class": "not read"`, and it explicitly notes the
   Frank/2021 Synodal-Bible claim as "never published" the method. cyphersolver's `top50/NOTES.md`/`TARGETS.md`
   both list item 19 as still "high" priority/open, citing the same outstanding, unpublished crib claim.
   aaymeloglu's repo had no hits for this item under any of the three search terms.
3. **OpenAlex** (`api.openalex.org/works`, `Authorization: Bearer $OPENALEX_KEY` header) — query
   `"Kaliningrad Baltiysk bottle cipher cryptogram"`: 0 results.
4. **Semantic Scholar** (`api.semanticscholar.org/graph/v1/paper/search`, `x-api-key: $S2_KEY` header) — same
   query: first attempt 429 despite the key; one retry after a ~3s pause (good-citizen single-retry rule)
   returned `{"total": 0}`.

**Verdict: open.** No published plaintext or decipherment found in any of the four sources; two informal,
mutually contradictory claims of a private solution (Ernst 2017, Frank 2021) were never substantiated, and a
prior independent solver attempt (cyphersolver, 15 Sept 2026) reached the same "not solved" conclusion working
from the same two source photographs. Per rule 10 this is a search result, not a novelty classification — a
future worker running a full check-solved or campaign on this target should try to reach "Frank" or search for
a match against the 1876 Filaret Synodal Bible directly, since that lead is specific and testable even though
unconfirmed.

### Requests (this section)

- `scienceblogs.de`/`ciphermysteries.com`: 0 (this target's brief does not name either for fresh fetching; the
  Cipherbrain post was already on disk).
- `api.openalex.org`: 1.
- `api.semanticscholar.org`: 2 (first attempt 429'd despite the key; one retry after a ~3s pause succeeded
  with 0 results).
- GitHub: 2 shallow clones (`dbourdeau/cyphersolver`, `aaymeloglu/unsolved-ciphers`), deleted after grep.

### Intake gate output, 25 Sept 2026 18:19 UTC

```
kaliningrad-2015: open (line 1) -- edition/page or full-text-search citation found within 6 lines
```
Exit code: 0.

## GOLD-KAL1, crib test and German homophonic, 25 Sept 2026

LANE GOLD2's reserve breadth test (cheap_tests_in_order[2], the spec's own "2-crib"/"2-homophonic-de" entries).
Two families, both control-first (CLAUDE.md rule 3). Fetched `tools/data/ru19` (Russian Synodal Bible, 78
books, one HTTP request to api.getbible.net) as a vocabulary and chapter index for a pure-Python word-pattern
crib solver (`ciphers/kaliningrad-2015/scripts/pattern_crib.py`) testing "Frank"'s Feb 2021 claim (Cipherbrain
comment #58) that the plaintext is a chapter of the 1876 Synodal Bible. Control gate (>=0.9 letters recovered
on a real chapter window, 3 seeds, both tokenisation conventions, with and without the chapter held out of the
vocabulary): MET, means 0.997-0.999. Target: only 22-23 of 187 crib-matchable words matched a Bible vocabulary
form under either convention (11.8-12.3 pct) -- well within the shuffle-null's own range (6.4-9.6 pct), no
flag on the primary word-match criterion. A secondary criterion (one chapter covering over half the decoded
words) is literally met in both conventions (John 6 at 63.6 pct, Ezekiel 39 at 82.6 pct) but the same shuffle
null clears that bar in 5 of 6 seeds too, so it is flagged to ROOM per the brief's mechanical rule and NOT
read as evidence for Frank's claim -- full tables and the corpus-scale reason the held-out control barely
differs from the full-vocabulary one are in HYPOTHESES.md. Ernst's 2017 "political... cross-language
polyalphabetic" claim (comment #50-52) names no text or method and remains untestable as stated.

German light homophonic substitution (`tools/family_run.py --family homophonic --param profile=target`, K=36,
judge repointed to `tools/data/de20`, 1880-1940 German, since the default `de` corpus is Early New High German
and wrong for a Soviet-era target): control 0.982 mean recovery (3 seeds, gate 0.9 MET), target judge **FAIL**
(-1.605 vs real_p05 -0.817). Control-backed negative for this family at this K and register.

Status stays `open` (rule 10: nothing here is a reading -- no H/C/S/M/I tokens claimed). Not closed-negative:
only two of the languages in `language_candidates` (ru via the crib test, de via homophonic) have been tested
with a control, and Polish, Lithuanian and a Russian simple substitution remain untried (no Cyrillic-alphabet
mode in `homophonic_anneal.py`, out of this job's scope). See HYPOTHESES.md for full numbers and commands.

## GOLD-KAL2, Russian transliteration schemes, 26 Sept 2026

Reserve cycle-5 job (brief `.claude/briefs/runs/2026-09-26-lane-gold-c5-kaliningrad-russian.md`), disk/CPU
only, no subagents. Settled the 13-apostrophe tokenisation discrepancy between LANE B2's NOTES.md counts and
the committed `ciphertext_signs.tsv`: `ic_analysis.tokenize_signs` silently drops an apostrophe it cannot
attach to an immediately preceding consonant within the same token (a genuine leading/orphaned apostrophe,
including one starting a dot-separated part of a dotted group) -- regenerating the TSV with `make_signs_tsv.py`
reproduces the committed file byte for byte, so no repair was needed; a true back-to-back pair like `n'n'` is
two ordinary compound signs, not a dropped double apostrophe. Built `ciphertext_signs_B.tsv` (convention B,
N=1066 K=28) and a periodic-IC control (flat, best period 17 margin 0.0008, no flag). Built
`tools/translit_ru.py` (four Russian-to-Latin schemes, offline test, corpus committed to
`tools/data/ru19_lat/`) and ran `tools/family_run.py --family homophonic --param profile=target` control
first on all four: S3'-partial and S1 (convention B, K=28) both cleared their control gate (mean 0.999 and
0.997) and both came back **control-backed negatives** on the target (judge FAIL, -1.706 and -1.729 against
real_p05 around -0.89); S1-stripped (convention A, K=36) and S3-full (convention B, K=28) did NOT clear their
own control gate (mean 0.733 and 0.677 -- an anneal-side difficulty at these K/profile combinations, one
control seed collapsing to 0.206 recovery), so those two remain untested rather than excluded, gate not
lowered per the brief. No judge PASS; no reading described. Full tables, commands and the exact tokenisation
rule are in HYPOTHESES.md's "GOLD-KAL2, Russian transliteration schemes" section. Status stays `open`.

## GOLD-KAL3, Polish and Lithuanian, 26 Sept 2026

Reserve cycle-5 job (brief `.claude/briefs/runs/2026-09-26-lane-gold-c5-kaliningrad-polish.md`), ran after
GOLD-KAL2 finished, no live overlap, disk/CPU + two hosts (gutenberg.org/gutendex.com for Polish, api.getbible.net
for Lithuanian), no subagents. Built `tools/data/pl19` (Polish prose, Project Gutenberg, 4 texts, 840,725
folded letters -- Gutendex's Polish-fiction catalogue is thin, none of the brief's named example authors
turned up, and the 4-text cap left the corpus short of the brief's 1.5M-letter aim, reported as found, not
padded) and `tools/data/lt` (Lithuanian Bible, getbible.net, 66 books, 2,599,750 folded letters, Bible
register not prose). Fixed a real `fold()` bug found while building pl19: ł is its own Unicode code point,
not a base letter plus a combining mark, so `homophonic_anneal.fold()`'s NFKD-strip-combining step does not
touch it and the final `[^a-z]` filter drops it outright (2.87% of raw letters); the corpus files have ł/Ł
replaced with l/L before gzip so `fold()` keeps every letter (residual difference 0.0037%, under the brief's
0.1% bar). Lithuanian needed no such fix (its marked letters all decompose under NFKD, 0.0000% difference).
Three `family_run.py --family homophonic --param profile=target` units, gate 0.9, control before target, never
lowered: convention A pl19 (K=36) and convention A lt (K=36) both **CONTROL BELOW GATE** (mean 0.655 -- one
seed collapsed to 0.003, reported per-seed not averaged away -- and mean 0.633 respectively), target not run
either time, untested not excluded; convention B pl19 (K=28) cleared its control gate (mean 0.996) and came
back a **control-backed negative** on the target (judge FAIL, score -1.971 against real_p05 -0.913, null_p99
-2.109). One tool wrinkle: `judge.corpora` set to a bare directory path raised `IsADirectoryError` in
`judge_plaintext.py`'s `read_corpus` (it wants explicit file paths, unlike `family_run.py --corpus`'s own
directory scan); fixed in the spec and the convention-B unit re-run cleanly for a correct row. No judge PASS;
no reading described. Full tables, IC numbers and commands are in HYPOTHESES.md's "GOLD-KAL3, Polish and
Lithuanian" section. Status stays `open`.

## GOLD-KAL4, restarts and sweep, 26 Sept 2026

Reserve cycle-6 job (brief `.claude/briefs/runs/2026-09-26-lane-gold-c6-kaliningrad-restarts-and-sweep.md`).
No subagents, disk and CPU only, no hosts touched. Part (a) re-ran GOLD-KAL2/KAL3's four CONTROL BELOW GATE
pairings at restarts 20 (up from 8), seeds 5 (then 6 where the brief's single-collapsed-seed pattern applied),
to tell a restarts problem from a real limit: three of the four now clear gate and come back **control-backed
negatives** (2-ru-s1s-A convention A K=36, judge FAIL -1.652; 2-ru-s3-B convention B K=28, judge FAIL -1.934;
2-pl-A convention A K=36, judge FAIL -1.827) -- more restarts alone fixed the anneal's convergence in each
case, the target did not become more readable. The fourth, 2-lt-A (convention A K=36, Lithuanian Bible), moved
from mean 0.633 to 0.827 but still did not clear gate (two seeds under 0.9, not the single-collapsed-seed
pattern, so no 6th-seed re-run per the brief), and is recorded as a residual anneal limit at this N/K with this
corpus, untested not excluded. Part (b) swept the convention-B (K=28) Latin alphabet across seven more
languages at restarts 8/seeds 3 (nl, da, en, fr, it, es, pt): six cleared their control gate and came back
control-backed negatives (nl, da, fr, es, it clean; en's judge corpus itself carries a documented 0.44-0.64
per-fold false-negative spread, so its FAIL is directionally consistent but of unknown reliability, per
CLAUDE.md's EN-FOLDS lesson); pt did not clear gate (mean 0.555, two seeds collapsed), CONTROL BELOW GATE,
untested not excluded. No judge PASS this job; no reading described. Full tables, per-seed numbers and the
per-unit sentences (restarts problem / real limit / control-backed negative) are in HYPOTHESES.md's
"GOLD-KAL4, restarts and sweep" section; both numbers for every unit are also in specs/kaliningrad-2015.json's
`cheap_test_done`. `judge.corpora` restored to `tools/data/de20` (the GOLD-KAL1 state) as this job's last spec
edit. Status stays `open`.

**Next steps.** Every convention-B Latin-alphabet language tried so far (German not tried at B; Russian S1/S3'
already negative; nl/da/en/fr/it/es/pl/ru-s3 all now control-backed negatives) leaves Portuguese (2-pt-B,
CONTROL BELOW GATE at restarts 8) as the one convention-B pairing still open in this sweep -- a restarts-20
rerun of that single unit, matching this job's own part (a) method, is the cheapest next step and was not
attempted here (out of this job's ordered task list). Convention A's Lithuanian pairing (2-lt-A) is the one
part-(a) unit that restarts 20 did not resolve; a seeds-6-8 battery at the same restarts, or a fixed/annealed
restart schedule, is the natural next test before concluding anything about Lithuanian at K=36. Convention B
Lithuanian (2-lt-B) was never run at all, per the brief. Beyond the homophonic family, the lane's own
cycle-4/5/6 record has now spent light-homophonic substitution across German, Russian (all four transliteration
schemes), Polish and seven further Latin-alphabet languages at both conventions with only two untested residual
gaps (pt-B, lt-A/lt-B) -- the next dollars on this target are better spent on a different family (periodic key,
running key, or the wide-alphabet/Cyrillic-native anneal named as out-of-scope in GOLD-KAL2) than on further
homophonic reruns, unless a worker wants to close the two remaining gaps first for completeness.

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/kaliningrad/ ; README.md ; TARGETS.md #19
- Their extent, in their words: attempted 15 Sept, blocked on transcription from two photographs
- Their date: 15 Sept 2026
- Note: already cited in our NOTES.md
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## Web and blog check (GF-A2-4, 2 Oct 2026)

Queries (WebSearch, 2 Oct 2026 22:3x UTC), each with what came back:
1. find-place + date (no sender/recipient known): `Kaliningrad bottle message cipher Baltiysk 2015 solved` -- Cipherbrain
   post 19 (17 Oct 2017), **a second, earlier Cipherbrain post, "Kaliningrad's second mystery: who can break this
   encrypted bottle post" (12 Sept 2016)**, and the Alster bottle-post series (other items). No solve announced.
2. Russian-language find report: `Балтийск бутылка шифр записка улица Ленина 2015 расшифровка` -- only unrelated Baltic
   message-in-a-bottle news (1913, 1987, Alaska 1969); nothing on this find.
3. distinctive phrase / the 2021 crib claim: `Kaliningrad cryptogram Filaret Synodal Bible plaintext encryption method
   bottle` -- Wikipedia "Russian Synodal Bible", the two Cipherbrain posts; no publication of "Frank"'s claimed method or
   plaintext found.
4. folder title: `"Kaliningrad" cryptogram Top 50 unsolved Schmeh bottle post Pillau decrypted` -- the two Cipherbrain
   posts plus "Unsolved: an encrypted bottle post found by a blog reader" (16 Oct 2016, another item) and Alster posts.
5. Cipherbrain: `site:scienceblogs.de klausis-krypto-kolumne Kaliningrad` -- the same two posts only.
6. Cipher Mysteries: `site:ciphermysteries.com Kaliningrad bottle` -- no ciphermysteries.com result (scienceblogs only).
7. Cryptiana blog: `site:cryptiana.blogspot.com Kaliningrad OR Baltiysk OR Pillau` -- no cryptiana.blogspot.com result.
Opened (curl, 1 request, HTTP 200; saved `sources/schmeh/posts/19-kaliningrad-2016.{html,txt}`): the 12 Sept 2016 post and its **14-comment thread, read in full**. Comments:
Facebook relays (Romo: "looked like French, then Russian"; Ulyanenkov: "Look like English. Vowel+1, consonant-1"),
Brantner (French-Flemish impression), Thomas #4-#7, #10, #14 (37 symbols with the apostrophe/umlaut variants; IC about
0.054 with variants, 0.08 on base letters; e n r i s order suggests a transposition of German), Leonid #8 (the Russian
forum also raised German anagrams), Piper #9/#11 (bottle never in the sea; apostrophes as repeat marks?), Merzmensch #13
(a "kosmopol method" PDF of a partial attempt, merzmensch.files.wordpress.com, no reading). **No plaintext or decipherment
in the thread.** Comment #6 links a Russian forum discussion (simple_life.dirty.ru/...-784251/) "without a solution but
with a transcription and a frequency count": fetch failed (proxy CONNECT 502), Wayback CDX for it and for the strana39.ru
source article both reset by the proxy (1 attempt each); strana39.ru article itself now answers 404 -- unreachable, not
read. The 2017 post-19 thread (58 comments) was read in full by LANE B2 bINT (25 Sept, above): two unsubstantiated
"solved" claims (Ernst 2017, "Frank" 2021), no plaintext posted. Nothing new found.

## Premise check (GF-A2-4, 2 Oct 2026)

(a) Decipherments the folder already mentions: the two claimed private solutions in the 2017 thread (Ernst: "political"
text; Frank: a chapter of the 1876 Filaret Synodal Bible) -- opened by bINT (thread on disk, `sources/schmeh/posts/
19-kaliningrad.txt`); neither posted a plaintext, key or method, and web query 3 above finds no later publication. No
gloss, clear copy or key exists for this item. Not found (two unverified claims, not a reading).
(b) Other solvers' working files: shallow clones of dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers (2 Oct 2026).
cyphersolver `targets/kaliningrad/` (README line 311: "Blocker is transcription from two photographs, not cryptanalysis";
top50/NOTES.md #19 "high") -- attempted 15 Sept 2026, not read, already cited in this file (Solver-repo check, 2 Oct).
Aymeloglu: only an unrelated DECODE postcard (R3282, Königsberg 1911) in catalogue/decode-catalog.csv. Merzmensch's
2016 PDF (comment #13) is a partial substitution attempt, no reading claimed. The Russian forum thread (comment #6) is
unreachable from here. Not found.
(c) Physical neighbours: the bottle's other contents (the 2016 thread: shells, sand, a wooden tag and string, per
Piper #9) carry no visible writing in the published photographs; the two sheets are both imaged (`images/cryptogram1.png`,
`cryptogram2.png`, the 2016 post's own "front side"/"rear side" -- note the 2016 post calls them front and rear of one
sheet, this file calls them two sheets; not settled here). No other sheet or clear copy is reported. Not found.
(d) Recipient's side: none identified (unaddressed note); the only primary report, strana39.ru (July 2015), now 404s
and was not reachable through Wayback this pass. Unreachable.
Result: nothing found that reads the cryptogram.

## A2-KAL, convention-B Portuguese and Lithuanian at restarts 20, 3 Oct 2026

Brief `.claude/briefs/runs/2026-10-03-acct2-a2-kal.md` (LANE-A2PUSH, account 2). Intake gate before deep work:
`python3 tools/intake_gate_check.py kaliningrad-2015` -> `kaliningrad-2015: open (line 1) -- edition/page or
full-text-search citation found within 6 lines`, exit 0.

Ran the step GOLD-KAL4's "Next steps" named: the two convention-B (K=28) homophonic units still open, by GOLD-KAL4
part (a)'s method (`tools/family_run.py --family homophonic --param profile=target`, restarts 20, seeds 5, a 6th seed
only for the four-0.9+/one-under-0.5 pattern, gate 0.9 never lowered, control before target). Disk and CPU only.
- **2-pt-B (pt18):** control 0.998/0.977/0.998/0.990/0.981, mean 0.989 (met; it was 0.555 at restarts 8). Target
  judge **FAIL** (score -1.316, real_p05 -1.078, null_p99 -1.613). A restarts problem, now resolved: a
  control-backed negative for Portuguese at convention B. No reading.
- **2-lt-B (lt, Bible register):** control 0.991/0.991/0.416/0.997/0.984, mean 0.876; 6th seed 1.000, mean 0.896.
  **CONTROL BELOW GATE**, target not run, untested not excluded. Not pursued further: a 7th seed would be a third
  turn of the same knob (rule 3's third-attempt clause).
Tables, per-seed numbers and commands: HYPOTHESES.md "A2-KAL" section; both numbers per unit also in
specs/kaliningrad-2015.json `cheap_test_done`. The target has no "Remaining gaps"/"Escalation" sections (status
`open`, not `partial`; `tools/gaps_check.py` reports SKIP), so none were edited. Status stays `open`; rule 10:
nothing here is a reading.

**Next steps.** The homophonic family is now spent at convention B across every Latin-alphabet language tried
(nl/da/en/fr/it/es/pt/pl/ru-s3: control-backed negatives; German was run at convention A only, GOLD-KAL1); the only homophonic residuals are
Lithuanian at both conventions (2-lt-A 0.827, 2-lt-B 0.896, both anneal-control limits on the Bible corpus, not
target results), which further reruns of the same anneal should not chase. The periodic-IC test was flat (best
period 17, margin 0.0008), so a periodic polyalphabetic family is a poor bet. The cheapest genuinely different
instrument is the transposition hypothesis the 2016 thread raised (Thomas: IC about 0.08 on base letters, order
e n r i s): test whether the convention-B letters read as plain German letters in another order -- unigram fit of
the target's own letter counts against tools/data/de20, with a matched control of transposed de20 text at N=1066
and a shuffled-alphabet null (the control can fail differently: a substitution of German changes the unigram fit,
a transposition does not); ~$2, one worker, no hosts.

## A2-KAL2, transposition-of-German unigram test, 3 Oct 2026

Brief `.claude/briefs/runs/2026-10-03-acct2-a2-kal2.md` (LANE-A2PUSH, account 2). Intake gate before deep work:
`python3 tools/intake_gate_check.py kaliningrad-2015` -> `kaliningrad-2015: open (line 1) -- edition/page or
full-text-search citation found within 6 lines`, exit 0.

Ran the step A2-KAL named above: `scripts/transposition_unigram.py` (disk and CPU only, no hosts). The convention-B
letters (N 977 folded, K 21) against tools/data/de20 unigrams, L1, with a matched control of transposed de20 windows at
N 977 (T) and a substituted-de20 null (S) on the same windows; the statistic separates T from S (gate T p99 < S p01 met
on both seeds), so the control could have failed differently from the target (rule 3).
- **As transcribed:** target L1 0.374 vs T p99 0.195/0.192 (seeds 42/7; T max 0.225 over 1,300 windows). Outside.
- **One free glyph label** (Ernst's "x" is a stand-in for an unidentified glyph; every text given the same one-relabel
  freedom): target 0.238 (x -> r) vs T p99 0.182/0.181, T max 0.211. Outside.
- Apostrophes: 88 in-word vs 0.58 expected for de20 at N 977 (cycle-4 exclusion, unchanged).
**Control-backed negative for transposition of German (de20 register)**, conditional on Ernst's transcript (rule 2).
Tables and per-letter gaps: HYPOTHESES.md "A2-KAL2"; both numbers also in specs/kaliningrad-2015.json `cheap_test_done`.
Status stays `open`; no "Remaining gaps"/"Escalation" sections exist for an `open` target (`tools/gaps_check.py`:
SKIP), so none were edited. Rule 10: nothing here is a reading.

**Next steps.** Cheapest still-untried unit on record: German homophonic at convention B (K 28), the one Latin language
the convention-B sweep skipped (German was run at convention A only, GOLD-KAL1): `tools/family_run.py --family
homophonic --param profile=target --corpus tools/data/de20`, restarts 20, seeds 5, gate 0.9, control first; ~$1, one
worker, no hosts. After that, the remaining structural lead is cycle 4's rank 6 (Russian with each softened consonant its
own plaintext letter, K 36-37, which needs an alphabet parameter in `homophonic_anneal.py` and the judge's fold; ~$12 tool
job + 2 units).

## A2-KAL3, German homophonic at convention B, 3 Oct 2026

Brief `.claude/briefs/runs/2026-10-03-acct2-a2-kal3.md` (LANE-A2PUSH, account 2). Intake gate before deep work:
`python3 tools/intake_gate_check.py kaliningrad-2015` -> `kaliningrad-2015: open (line 1) -- edition/page or
full-text-search citation found within 6 lines`, exit 0.

Ran the step A2-KAL2 named: `tools/family_run.py --family homophonic --param profile=target --corpus tools/data/de20`,
convention B (ciphertext_signs_B.tsv, N 1066, K 28), restarts 20, seeds 5, gate 0.9, control before target. Disk and CPU only.
- **2-de-B (de20):** control 0.998/0.997/0.995/0.998/0.999, mean 0.997 (met). Target judge **FAIL** (score -1.572,
  real_p05 -0.807, null_p99 -2.075; position 0.40 between null and real, in the band of the sweep's other negatives).
  **Control-backed negative** for light homophonic German at convention B; with GOLD-KAL1 (convention A, FAIL -1.605)
  German homophonic is now negative at both conventions. Conditional on Ernst's transcript (rule 2). No reading.
Table and command: HYPOTHESES.md "A2-KAL3"; both numbers also in specs/kaliningrad-2015.json `cheap_test_done`.
Status stays `open` (no "Remaining gaps"/"Escalation" sections for an `open` target; `tools/gaps_check.py`: SKIP).
Rule 10: nothing here is a reading.

**Next steps.** The convention-B homophonic sweep is now complete for every Latin-alphabet language on disk
(de/nl/da/en/fr/it/es/pt/pl/ru-s3 control-backed negatives; lt below its own control gate at both conventions, an anneal
limit on the Bible corpus, not chased further). The next untried instrument on record is cycle 4's rank 6: Russian with
each softened consonant its own plaintext letter (K 36-37), which first needs an alphabet parameter in
`tools/homophonic_anneal.py` and the judge's fold (a tool job with an offline test, ~$12) and then two family_run units
(~$1 each); one worker, no hosts.

## A2P4-KAL4, Russian with each softened consonant its own letter, 3 Oct 2026

Brief `.claude/briefs/runs/2026-10-03-acct2-a2p4-kal4.md` (LANE-A2PUSH4, account 2). Intake gate before deep work:
`python3 tools/intake_gate_check.py kaliningrad-2015` -> `kaliningrad-2015: open (line 1) -- edition/page or
full-text-search citation found within 6 lines`, exit 0.

Tool step (commit fbda87f4): a plaintext alphabet option -- `tools/homophonic_anneal.py --alphabet NAME|CHARS`,
`--param alphabet=` in `tools/families/homophonic.py` (passed through `tools/family_run.py`), a judge-block `"alphabet"`
in `tools/judge_plaintext.py`, and `tools/translit_ru.py --soft-letters`, which built `tools/data/ru19_soft` (S3'/S3
Latin with every q merged into the letter before it as one upper-case letter: 35 and 37 letters; rule in its README).
Offline test `tools/tests/test_homophonic_alphabet.py`: default-alphabet outputs byte-identical to the pre-option code
(fixture from commit 85a7db4e), a synthetic K-36 cipher over the 35-letter alphabet read back at 0.978, judge PASS on a
real window and FAIL on it shuffled. Existing homophonic, translit, judge and family_run tests still pass.

Then three pre-registered units (HYPOTHESES.md "A2P4-KAL4", pre-registration commit adb71590 before any run), homophonic
profile=target, restarts 20, seeds 5, gate 0.9, control before target. Disk and CPU only, no hosts:
- **5-ru-soft-s3p-A** (convention A, K 36, 35 letters): control mean 0.723, **CONTROL BELOW GATE**, untested.
- **5-ru-soft-s3p-B** (convention B, K 28, the brief's literal unit; design-mismatched, since at B the apostrophe is its
  own sign): control mean 0.842, **CONTROL BELOW GATE**, untested (a 6th seed cannot reach 0.9).
- **5-ru-soft-s3-A** (convention A, K 36, 37 letters): control mean 0.995; target judge **FAIL** (-1.992, real_p05
  -0.859, null_p99 -2.242; position 0.18). **Control-backed negative**, conditional on Ernst's transcript and on an
  uncalibrated judge corpus.
Both numbers per unit also in specs/kaliningrad-2015.json `cheap_test_done`. Status stays `open` (no judge PASS); no
"Remaining gaps"/"Escalation" sections for an `open` target. Rule 10: nothing here is a reading.

**Next steps.** Cycle-4 rank 6 is now half spent: the S3 softness rule is a control-backed negative; the S3' rule (the one
whose K matches the target's 36 best) is untested because the anneal's own control does not converge at 35 letters with
3 pct soft letters (0.723) -- the same kind of control limit restarts alone fixed for 2-ru-s1s-A (GOLD-KAL4). A third
turn of restarts is not the next step (rule 3's third-attempt clause; this is the second family at this design). The
genuinely different instrument would be an anneal move set that proposes soft/hard pairs together (swap n<->N as one
move) or a two-stage solve (base 22 letters first, then the softness split), built with its own offline test, ~$6; or
a measured judge calibration for ru19_soft (leave-one-book-out FN rate) before trusting any further Russian FAIL, ~$2.
Verdict: keep going (no outside blocker), but the homophonic family on this target is near exhausted.


## A2P4-KAL5, ru19_soft judge calibration, 3 Oct 2026

Brief `.claude/briefs/runs/2026-10-03-acct2-a2p4-kal5.md` (LANE-A2PUSH4, account 2). Script only, no anneal, no hosts.
Tool shelf named `judge_plaintext.py`; the 16 per-corpus `tools/data/*/holdout_check.py` copies had no alphabet option,
so a shared `--holdout FILES --N --alphabet` option was added to `tools/judge_plaintext.py` (offline test
`tools/tests/test_judge_holdout.py`). Pre-registration in HYPOTHESES.md (commit f613b8ef) before any score.

ru19_soft is one file per scheme, so folds are 8 book groups of the Synodal Bible rebuilt with the same command: 8 folds,
one independent source. Leave-one-group-out false-negative rate on the in-model real_p05 gate: **s3_soft N 978 38.4%
(folds 14.5-49.5%, 3.4x); s3_soft N 1066 45.9% (26.5-56.0%, 2.1x); s3p_soft N 1066 40.1% (25.0-48.5%, 1.9x).** Per-fold
table and held-out p05/p01/min in HYPOTHESES.md "A2P4-KAL5 result" and tools/data/ru19_soft/README.md.

**Correction to A2P4-KAL4 (above).** By rule 3 (one source, wide spread) the ru19_soft real_p05 gate is of unknown
reliability at this N, so the 5-ru-soft-s3-A FAIL is re-labelled **"judge cannot decide" on the real_p05 gate**, not a
control-backed negative. Beside it, unchanged: the target scored -1.992, below every one of 1,600 held-out real Russian
windows at N 978 (minimum -1.201, p01 -1.054) and 0.25 above the shuffled null's p99 (-2.242). On the held-out
distribution as gate the s3-soft decode still fails by a wide margin; the relabel concerns the gate's calibration, not
the size of the miss.

**Next steps.** Score Russian candidates against the held-out distribution (p01 about -1.05 at N about 1000) as well as
real_p05; the ru19_lat corpora behind GOLD-KAL2/GOLD-KAL4's Russian FAILs are uncalibrated the same way (same `--holdout`
run, ~$1). The S3' unit stays untested (control 0.723); the different instrument named by A2P4-KAL4 (paired soft/hard
move set or two-stage solve, ~$6) is unchanged. Verdict: keep going (no outside blocker).

## RUN4-KAL, ru19_lat judge calibration, 4 Oct 2026

Brief `.claude/briefs/runs/2026-10-04-acct1-run4-wave2.md` "RUN4-KAL" (LANE-RUN4, account 1). Script only, no anneal, no
hosts; A2P4-KAL5's `--holdout` method on the four ru19_lat schemes, pre-registration commit f766765b before any score.
Leave-one-book-group-out FN on the in-model real_p05 gate: **s3p N 1066 22.0% (folds 8.0-35.5%); s1 N 1066 22.5%
(7.0-39.0%); s1s N 978 17.4% (8.0-32.5%); s3 N 1066 17.0% (9.0-31.5%)**, one source. Tables in HYPOTHESES.md "RUN4-KAL
result" and tools/data/ru19_lat/README.md.

**Correction to GOLD-KAL2/GOLD-KAL4.** The four Russian FAILs (S3' -1.706, S1 -1.729, 2-ru-s1s-A -1.652, 2-ru-s3-B
-1.934) are relabelled **"judge cannot decide" on the real_p05 gate** (unknown reliability, rule 3). On the held-out
distribution as gate all four stay **FAIL**: each lies 0.40-0.84 below the lowest of 1,600 held-out real windows
(minimum -1.095 to -1.284) and only 0.19-0.43 above the shuffled null's p99. No logged Russian FAIL is "judge cannot
decide" on the held-out gate; the miss is real in size, only the gate's label changed. Status stays `open`; nothing
here is a reading.

**Next steps.** Unchanged from A2P4-KAL5: the S3' soft unit (control 0.723) needs a different instrument (paired
soft/hard move set or two-stage solve, ~$6); further Russian FAILs are reported against the held-out distribution.

## R9-KAL6, paired soft/hard move and two-stage solve for the S3' unit, 6 Oct 2026

Brief `.claude/briefs/runs/2026-10-06-account2-run9-jobs.md` "R9-KAL6" (LANE-RUN9, account 2). The step A2P4-KAL4 named
("paired soft/hard move set or two-stage solve, ~$6") was still undone. Disk and CPU only, no hosts.

Tool step: `--param soft=pair|two-stage` on the shared homophonic family (`tools/families/homophonic.py`,
`homophonic_anneal.soft_pairs`, `anneal(pairs=, pair_prob=)`), offline test `tools/tests/test_homophonic_soft.py`;
the default path is byte-identical to HEAD's. Pre-registration in HYPOTHESES.md (commit 55a90309) before any scored run.
Then, convention A, N 978, K 36, ru-s3p-soft (35 letters), profile=target, restarts 20, seeds 5, gate 0.9, control first:
- **soft=pair**: control 0.899 (four seeds 0.989-0.994, one 0.526), CONTROL BELOW GATE by 0.001, untested.
- **soft=two-stage**: control 0.990 (0.985-0.993), up from A2P4-KAL4's 0.723 with the plain anneal. Target judge
  FAIL -1.733 (real_p05 -0.864, null_p99 -2.137); held-out at N 978 (measured this job, `tools/data/ru19_soft/
  holdout_s3p_N978.log`): p01 -1.026, min -1.156, blended FN 29.4 pct (folds 9.0-41.0). Shuffled target (same pipeline)
  -1.765.
Reading (pre-registered): real_p05 gate "judge cannot decide"; held-out gate FAIL; but the shuffled target scores within
0.1 of the target, so the target's number licenses nothing either way -- the decode does not separate from its own
shuffle. Not a control-backed negative, no reading. Status stays `open`. Rule 10: nothing here is a reading.

**Next steps.** The S3' design is now testable (two-stage control 0.990), and the judge cannot tell this target's decode
from its shuffle at N 978 on ru19_soft. A different instrument, not a further tuning of this one, would be the next test:
a judge statistic that the shuffle control can separate (for example the decode's word-segmentation rate against a
Russian lexicon, with the shuffled target as its control), ~$2. Verdict: keep going (no outside blocker); the
homophonic family on this target is otherwise spent.

## R10-KAL7, lexicon word-segmentation gate for the S3' two-stage decode, 6 Oct 2026

Brief `.claude/briefs/runs/2026-10-06-account2-run10-jobs.md` "R10-KAL7" (LANE-RUN10, account 2), the instrument R9-KAL6
named. Disk and CPU only, no hosts. Pre-registration in HYPOTHESES.md "R10-KAL7" (commit 32b67fba) before any scored run.
Driver `scripts/lexseg.py`: R9-KAL6's two-stage homophonic unit (ru-s3p-soft, convention A, N 978, K 36, restarts 20)
retrained on the S3'-soft Synodal Bible without the New Testament; lexicon = NT word types (length >= 4, count >= 2,
7,586 types, `tools/data/ru19_soft/lexseg/`), held out from every corpus the decoder used; statistic = share of decode
letters covered by non-overlapping lexicon words (DP).
- Null: 50 shuffles of the target through the same pipeline, coverage 0.020-0.087, p95 **0.0736**.
- Positive control first: 5 synthetic windows at the target's N, K and sign-count profile read 0.160-0.729 (mean 0.469),
  all above the gate and above their own shuffle null (p95 0.0654): **control PASS**, and the shuffle control is shown to
  differ from a true decode on this statistic (rule 3 orthogonality).
- Target: **0.0440**, the median of its own shuffle null (rank 26 of 51). By the registered rule: **control-backed
  negative** for the S3' two-stage homophonic design on this statistic, conditional on Ernst's transcript, convention A
  and a Bible-register lexicon. Second instrument on S3' (first: R9-KAL6's n-gram judge, "cannot decide").
Status stays `open`. Rule 10: nothing here is a reading.

**Next steps.** The Russian S3' homophonic hypothesis now has a control-backed negative from an instrument that separates
true decodes from shuffles by 2-10x at this N; the homophonic family on this target is spent for S3'. The same driver can
test the other Russian schemes (S1, S1s, S3, S3-soft) and German at no tool cost (~$1.5 each; lexicon from a held-out
book group of the matching corpus), which would turn the earlier "judge cannot decide" Russian rows into decisive ones.
Verdict: keep going (no outside blocker).

## R12-KAL8, lexicon word-segmentation on S1, S3, S1s, S3-soft and German, 6 Oct 2026

Brief `.claude/briefs/runs/2026-10-06-account2-run12-jobs.md` "R12-KAL8" (LANE-RUN12, account 2), the step R10-KAL7 named.
Disk and CPU only, no hosts, no subagents. One pre-registration for all five units (HYPOTHESES.md "R12-KAL8", commit
09fba2be) before any scored run. R10-KAL7's driver `scripts/lexseg.py` (env LEXSEG_CIPHER / LEXSEG_PARAMS added, default path
unchanged), train corpora and held-out lexicons from `scripts/lexseg_build.py` (Russian: NT word types, decoder trained
without the NT; German: de20 with two Fontane novels held out as the lexicon). Null sized to the box: 15 shuffled-target
decodes per unit, gate G = their maximum; positive control first (4 synthetic windows, their own 4-shuffle null G_s).

| unit | control (synthetic mean vs G / G_s) | target coverage vs G | result |
|---|---|---|---|
| S1, conv. B | 0.582 vs 0.070 / 0.059, PASS | 0.041 vs 0.070, rank 8 of 16 | control-backed negative |
| S3, conv. B | 0.671 vs 0.038 / 0.033, PASS | 0.039 vs 0.038, rank 16 of 16 | above G by 2 letters of 1,066 -- see below |
| S1s, conv. A | 0.515 vs 0.076 / 0.073, PASS | 0.041 vs 0.076, rank 3 | control-backed negative |
| S3-soft, conv. A | 0.505 vs 0.038 / 0.034, PASS | 0.034 vs 0.038, rank 15 | control-backed negative |
| German de20, conv. A | 0.640 vs 0.158 / 0.129, PASS | 0.114 vs 0.158, rank 7 | control-backed negative |

S3 tops its 15 shuffles by the registered rule, but by 42 covered letters against 40, the secondary length->=5 figure sits
at the null median, five units gated at "top of 16" give about a 28% chance of one such exceedance by luck, and the
coverage is a tenth of the weakest synthetic decode. By the registered wording it is "worth a verifier, not a reading"; no
text is described. All negatives are conditional on Ernst's transcript, the convention and the lexicon's register
(rule 2). Full table, recoveries and the secondary figure in HYPOTHESES.md "R12-KAL8 result"; files in `lexseg/r12/`.
Status stays `open`. Rule 10: nothing here is a reading.

**Next steps.** (1) S3 convention B confirmation before any verifier: the same unit with shuffle seeds 16-50 added (G = p95
of 50, R10-KAL7's null size), pre-registered, about 9 minutes of CPU, ~$1; a target that falls back inside the null closes
S3 as a control-backed negative, one that stays at the top goes to a verifier with the rule-7 re-derivation. (2) If S3
closes negative, the light homophonic family on this target is spent for every scheme tried with a lexicon instrument
(S3', S1, S1s, S3-soft, German) and the next test needs a different design family (nomenclator/code groups or
transposition), not another substitution scheme. Verdict: keep going (no outside blocker).

## R12-KAL9, S3 convention B confirmation with a 50-shuffle null, 6 Oct 2026

Brief `.claude/briefs/runs/2026-10-06-account2-run12-jobs.md` "R12-KAL9" (LANE-RUN12, account 2): R12-KAL8's next step (1).
Disk and CPU only, no hosts, no subagents. Pre-registered in HYPOTHESES.md "R12-KAL9" (commit 2a3713168) before scoring:
the same S3 unit, shuffle seeds 16-50 added to R12-KAL8's 1-15, gate = target above P95 of the 50. The target decode
reproduced byte for byte (42 of 1,066 letters covered). Result: **FAIL** -- P95 0.0459 (48.9 letters) against the
target's 0.0394; the target ranks 5 of 51 (empirical p 0.118), four fresh shuffles cover 44-69 letters; the length >= 5
secondary is at rank 14 (p 0.43). S3 convention B is a control-backed negative for the light homophonic design on this
statistic (conditional on Ernst's transcript, convention B and the lexicon's register); R12-KAL8's apparent excess was
small-null luck. Files: `lexseg/r12/kal9/`, `lexseg/r12/coverage_minlen{4,5}_s3_kal9.tsv`. Status stays `open`.

**Next steps (R12-KAL9).** R12-KAL8's step (2) now applies: with a lexicon instrument the light homophonic family is
spent on every scheme tried (S3', S1, S3, S1s, S3-soft, German), so the next test needs a different design family
(nomenclator/code groups or transposition) with its own matched control, not another substitution scheme. Verdict: keep
going (no outside blocker).

## R13-KAL10, letter-or-word nomenclator with its own matched control, 6 Oct 2026

Brief `.claude/briefs/runs/2026-10-06-account2-run13-jobs.md` "R13-KAL10" (LANE-RUN13, account 2): the different design family
R12-KAL9 named. Disk and CPU only, no hosts, no subagents. `tools/design_prior.py --no-write` on the sign TSVs (on
`ciphertext.txt` it tokenises by whitespace into 92 words, not usable) ranked nomenclator top (convention A 0.20, B 0.33,
advisory tier); nomenclator was not logged in HYPOTHESES.md, so it is the family run. `family_run.py --family nomenclator` takes
integer tokens only, so the letter-sign form `--family wordcode` (each sign type = one letter or one whole word) was used, after
adding `--param bnd=` (its word-boundary letter was hard-coded `w`, a letter in ru19_lat; default unchanged, offline test (6)
added in `tools/tests/test_wordcode.py`). Hypothesis: the 13 apostrophe/diacritic types (113 tokens, 11.6%) are whole-word codes,
the unmarked types letters, Russian s1s. Pre-registered in HYPOTHESES.md "R13-KAL10" (commit ceca4fbad) before scoring.

**Result: CONTROL BELOW GATE** -- matched control mean token accuracy 0.491 (seeds 0.001 / 0.875 / 0.597) against gate 0.6 at
N 978, K 36, restarts 2, err 0.05; the target was not run. A non-test for this design with this tool at this setting, not a
negative; no reading. Seed 1 is a stuck restart basin while seeds 2-3 read the design, so the named next step is the same unit
pre-registered again at restarts 6, seeds 1-5 (~5 min CPU, ~$1), with the shuffled-target decode beside the target. Status
stays `open`. Rule 10: nothing here is a reading. Both numbers in HYPOTHESES.md (family_run row and "R13-KAL10 result").


## R14-KAL11, wordcode nomenclator at restarts 6, 6 Oct 2026

Brief `.claude/briefs/runs/2026-10-06-account2-run14-jobs.md` "R14-KAL11" (LANE-RUN14, account 2). The R13-KAL10 named step,
attempt 2 of the same instrument with restarts (2 -> 6) and seeds (3 -> 5) the only knobs. CPU only, no hosts, no subagents.
Pre-registered in HYPOTHESES.md "R14-KAL11" (commit a5d9745d0) before scoring.

**Result: control-backed negative for this design at err 0.05.** Matched control mean 0.767 (seeds 0.211-0.950; code class
0.793) meets gate 0.6, so the target ran: judge FAIL -1.525 vs real_p05 -0.892; the shuffled-target decode beside it also FAILs
(-1.491), so the judge is not voided, and the target is no better than its own shuffle. Both decodes are degenerate letter
streams with no code words. Conditional on Ernst's transcript and convention A, and only for the 0.05 error band (no measured
transcription error exists). Status stays `open`; no reading. Rule 10: nothing here is a reading.
Suggestion (not done): `family_run.py --family wordcode` controls are not seed-reproducible (seeds 1 and 3 read differently
between two runs with identical params); a tools job could pin the restart RNG to `--seed`.
Next step: the letter-or-word nomenclator with marked types as codes is now logged; a different design family or convention B
for the same design (~$1.5, CPU only) remain. Verdict: keep going (no outside blocker).
