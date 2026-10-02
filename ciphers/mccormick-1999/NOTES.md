open

check-solved (25 Sept 2026, LANE B2 worker bMCC2, minimal per intake step added 18:14 UTC to
`.claude/briefs/breadth.md`): Cipherbrain post 10 (Klaus Schmeh, 1 May 2018, "The Top 50 unsolved
encrypted messages: 10. Ricky McCormick's encrypted notes"), `sources/schmeh/posts/10-mccormick.txt`,
read in full including its 6-comment thread; grepped for solved/unsolved/decrypt/cracked/FBI. No
verified solution on record: the FBI's own codebreaking unit CRRU (Schmeh: "success rate of about 99
percent") and the American Cryptogram Association (ACA) both failed (post lines 135, 173). A claimed
Spanish-language "solution" posted to taringa.net (comment #1, "Descrifrado el Codigo McCormick que el
FBI no pudo") is discussed and dismissed in the same comment thread by two other commenters (#3 HF(de),
#5 HF(de)) as homophone guessing ("sounds like", e.g. 8=eight=ai=a), not a real decipherment -- so this
is not a fresh finding, it is already on the record and rejected by the blog's own readers.
Solver-repository grep (github.com/dbourdeau/cyphersolver, github.com/aaymeloglu/unsolved-ciphers) and
one OpenAlex plus one Semantic Scholar query (rule 1's remaining legs) were skipped this run: this
worker's brief (`.claude/briefs/runs/2026-09-25-lane-b2-mccormick-1999-t2.md`) states "No subagents, no
network," so no network call was made. A future check-solved pass with network access should complete
those two legs before any campaign above breadth cap ($10, CLAUDE.md 3a).

Status vocabulary: `open` (CLAUDE.md rule 5). This folder holds only the intake note and
HYPOTHESES.md for the breadth-lane cheap tests on specs/mccormick-1999.json; transcription and
ciphertext live in that spec (Schmeh's own re-typing of the FBI's images, rule 2), not here -- no
images were fetched by this worker (CLAUDE.md's "LANE B, 24 Sept 2026" rule: a breadth worker has no
target folder unless its test fetches images; this folder exists only because this brief's cheap
test 2 asked for one to hold HYPOTHESES.md).

## Cheap test 2 (25 Sept 2026, LANE B2 bMCC2)

`tools/family_run.py --family masc` run twice at N=746, K=24 (letters-only fold, both notes, 3
control seeds, gate 0.6, restarts 8): once against the default English corpus
(`tools/data/pg1661_holmes.txt` + `pg2701_mobydick.txt`), once against a new vowel-dropped English
corpus built for this test (`tools/data/en_vdrop/`, word-initial vowels kept, word-internal a/e/i/o/u
dropped, README and offline test there). Rows in `HYPOTHESES.md`; full numbers, method and caveat in
`specs/mccormick-1999.json`'s `cheap_test_done.2`.

Both controls read at or above ~0.98 recovery (mean 0.994 default English, 0.985 vowel-dropped) --
already at the near-ceiling line CLAUDE.md rule 3 warns has no headroom to show a gain: a masc anneal
at this N, K essentially always recovers a random simple-substitution key, whatever the corpus. Both
target decodes got a mechanical judge PASS (`tools/judge_plaintext.py`; a PASS is a gate for a
verifier, not a reading, rule 10) but read as letter salad, not English, under either corpus --
`ciphers/mccormick-1999/families/masc-1-default_en.txt` and `masc-1-vdrop_en.txt` (the shared
`masc-1.txt` path holds only the more recent, vowel-dropped run; both are kept separately since the
tool overwrites that path per run). This is consistent with the spec's own `schema_note`: the notes'
heavy repeated-token structure (test 1: NCBE, the -RSE family) inflates n-gram likelihood under any
consistent key, so a PASS here is not evidence either English design is right. Neither run supports
or rules out the source's shorthand/nomenclator hypothesis over the null. Next step (not run here,
out of this brief's scope): a bespoke tokenizer-aware judge treating the repeated multi-character
tokens as signs, per test 1's and this spec's own schema_note.

**Update 25 Sept 2026 (LANE B2 orchestrator, 19:02 flag):** `tools/judge_plaintext.py` was fixed to fail
closed when a judge block has no `language`/corpora; the spec's judge block now carries `language: en,
min_word_cover: 0.6` (added by that same flag). Re-judged under the fixed judge, both cheap test 2
decodes above are **FAIL**, not PASS -- the earlier PASS lines in this section and in HYPOTHESES.md were
a length-only check, not a real language check; masc is excluded at N=746, K=24 under both corpora.

## Cheap test 3 (25 Sept 2026, LANE B3 bMCC3) -- homophonic family, NEAR.md's named next step

`tools/family_run.py specs/mccormick-1999.json --family homophonic --cipher
specs/cheap-tests/mccormick-1999/cipher_both_notes.txt --tokens letters --seeds 3 --gate 0.6`, same
letters-only fold as test 2 (N=746, K=24 auto-derived from the ciphertext), homophonic_anneal's own K
(one homophone slot per sign actually present, i.e. K=24 -- the spec carries no separate declared K),
run three times, plus a false-positive floor (`--shuffle-target SEED`, new option added to
`tools/family_run.py` this run with an offline test in `tools/tests/test_family_run.py`, check (7)):

| run | CONTROL mean (range), 3 seeds | TARGET judge |
|---|---|---|
| default English corpus | 0.998 (0.997-0.999) | **FAIL** score=-1.48 vs null_p99=-2.071, real_p05=-0.864 |
| vowel-dropped English corpus (`tools/data/en_vdrop`) | 0.652 (0.058-0.992) | **FAIL** score=-2.329 (below even null_p99) |
| shuffled target, default corpus, shuffle seed 1 | 0.998 (0.997-0.999) | **FAIL** score=-1.807 |
| shuffled target, default corpus, shuffle seed 2 | 0.998 (0.997-0.999) | **FAIL** score=-1.839 |
| shuffled target, default corpus, shuffle seed 3 | 0.998 (0.997-0.999) | **FAIL** score=-1.896 |

Default-English control is near ceiling (0.998), same as test 2's masc controls, so it has no headroom
to show a gain (rule 3 caveat) but the target still FAILs the judge outright this time (the earlier
"PASS" in test 2 was the judge's own bug, now fixed -- see the update note above). The vowel-dropped
control is markedly less reliable for homophonic than it was for masc (test 2: 0.985; here: mean 0.652,
range 0.058-0.992 -- one of the three seeds essentially failed to anneal at all), barely clearing the
0.6 gate; a control that unstable is weak evidence either way from that run alone.

The false-positive floor is the important number here: three independent shuffles of the target's own
746 letters (same multiset, same K=24, random order -- CLAUDE.md rule 3's "same length, symbol count,
design" synthetic negative, built from the target itself rather than a corpus) all FAIL, with scores
(-1.807, -1.839, -1.896) in the *same range* as the real target's own default-corpus score (-1.48) --
if anything the real target scores slightly *better* than the shuffled noise, but all four sit well
inside FAIL territory, nowhere near real_p05 (-0.864). This means the homophonic anneal's best decode
of the real 746-letter target is statistically indistinguishable from its best decode of random letter
salad of the same shape: no signal above noise. Combined with test 2 (masc excluded, same target, same
judge fix), both families tried so far are excluded at this N, K under the letters-only fold.

Decodes: `ciphers/mccormick-1999/families/homophonic-1-default_en.txt`,
`homophonic-1-vdrop_en.txt`, `homophonic-1-shuffle1.txt`, `homophonic-1-shuffle2.txt`,
`homophonic-1-shuffle3.txt` (all read as letter salad on inspection, consistent with the FAIL judge
lines). Full rows in `HYPOTHESES.md` (includes one earlier `--control-only` calibration row at 19:13,
kept per the tool's append-only rule, and one rerun of the default-corpus row at 19:20 to save its
decode file separately before the vowel-dropped run's file overwrote the shared `homophonic-1.txt`
path -- same numbers both times, confirming determinism). This is a control-backed negative for the
homophonic family at this N/K/fold, not a `closed-negative` for the target as a whole (CLAUDE.md rule 5
amendment): the letters-only fold itself remains untested against the source's own repeated-token/
shorthand hypothesis (test 1's schema_note, tests 2 and 3's `hypothesis_note`) -- a tokenizer-aware
judge treating NCBE/-RSE/etc. as signs is still the more promising untried step, not a straight
letter-substitution family at any K.

## Cheap test 4 (25 Sept 2026, LANE B3 bMCC4) -- token/nomenclator test, NEAR.md's named next step

`specs/cheap-tests/mccormick-1999/token_anneal.py` (new script -- `tools/nomenclator_anneal.py` is
Italian/German-only and needs numpy, so it did not fit; a fresh, small, numpy-free script was written
instead, per the brief). Tokenizes both notes as written on the documented separators (whitespace,
hyphen, slash, comma, `?`; parentheses stripped as brackets not characters): 132 tokens total -- 116
code-token occurrences (99 distinct multi-letter types: NCBE x11, six other types x2, 92 singletons),
14 number tokens, 2 single-letter tokens (`N` x2). Numbers and single letters pass through unchanged
(rule: "each single letter as itself"); a simulated anneal (8000 iterations, 2 restarts per run)
assigns each of the 99 distinct code types to a word from a 350-word pool drawn from the same `en`
corpus `tools/judge_plaintext.py` itself uses (pg1661_holmes.txt + pg2701_mobydick.txt), scored by that
script's own character 4-gram `NgramModel` -- the test's language model is exactly the judge's, nothing
separate to keep in sync.

**Matched control** (3 seeds): a same-length (132-token), same-per-position-kind-sequence synthetic
English stream drawn from the same corpus. Code slots get a fresh unique 4-letter placeholder, except
words from the corpus's 60 most frequent types get one placeholder reused on every recurrence (mirrors
the real target's NCBE-heavy, mostly-singleton structure); number slots get a random small integer; the
two letter slots get `a`/`I`. No vowel-dropped share: the target's own non-code share (10.6% number +
1.5% single-letter = 12.1% of 132 tokens) is covered exactly by the number+letter slots, so there is no
remainder to vowel-drop (documented choice, per the brief). Recovery = fraction of the control's own
known code-type-to-word truth the anneal reconstructs.

| run | control recovery | target score | shuffled-target score (3 shuffles) |
|---|---|---|---|
| iters=8000, restarts=2 | mean 0.8% (0.0%, 1.1%, 1.3% across 3 seeds; 76-99 truth types/seed) | -0.7497 | -0.752, -0.745, -0.762 |

**Gate NOT met** (control recovery 0.8% is far below the brief's 0.5 gate): per CLAUDE.md rule 3 and the
brief, this is "not a test," reported as such rather than as a control-backed negative. The design is
degenerate at this token count: 99 largely-singleton code types drawn from a ~350-word pool is an
effectively unconstrained assignment problem -- cross-word 4-gram context at word boundaries is far too
weak a signal to pin down a specific word choice, so the anneal cannot even recover the *control's own
known ground truth*. The target decode does get a language-check PASS from `judge_plaintext.py` (score
-0.75 > real_p05 -0.873, word cover 0.971) but this is not meaningful: it is an artifact of plugging real
dictionary words into 99 free slots (any assignment looks locally plausible), exactly as shown by the
control's near-zero true-mapping recovery and by the shuffled-target floor (-0.745 to -0.762, the same
range as the real target's own -0.7497 -- no discrimination between the real token order and three
shuffles of it). The judge's overall verdict is FAIL regardless, but only on the length check (got 408
letters vs the 700-800 the block expects, because the token scheme replaces code tokens with words of a
different length -- not a language finding). Full numbers and method in `specs/mccormick-1999.json`
`cheap_test_done.4`; decode preview and script in
`specs/cheap-tests/mccormick-1999/token_anneal.py` and `test4_result.json`;
`ciphers/mccormick-1999/families/token-anneal-target.txt` (candidate only, not a reading -- rule 10).

This matches the spec's own prediction for this test ("the FBI/ACA's own presumed approach ... expect a
negative"). Combined with tests 2 and 3, all three of the spec's cheap tests are now run: masc excluded,
homophonic excluded (both control-backed), and this token/nomenclator test's own control falls short of
its gate so it cannot be read either way. None supports a reading. The source's shorthand/phonetic
hypothesis remains the only untested account, but turning it into a scoreable, testable family (e.g. a
hand-built sign inventory checked against a period shorthand system such as Gregg) is a campaign-scale
task, not a further breadth-lane cheap test -- out of this brief's scope; left as a one-line suggestion
for the orchestrator, not started here.

**Fold-count backfill (parent worker EN-FOLDS, 25 Sept 2026 22:17 UTC, CLAUDE.md rule 3 amendment):** cheap
test 4's language model reuses `tools/judge_plaintext.py`'s own `en` corpus (pg1661_holmes.txt +
pg2701_mobydick.txt), which had no per-fold spread on file at the time; it now does --
leave-one-file-out false-negative spread 0.44 (N=200)/0.11 (N=500) on those 2 files, worse (0.64/0.75) after
adding 3 more sources, per `tools/data/en/README.md`. This does not change the verdict above (test 4's own
result turns on the control's near-zero recovery, not on the language-check PASS, which the note above
already calls not meaningful) -- the verdict stands as written, with that caveat on record.

SO lead prompt, 26 Sept 2026, QUEUE-FILL.

## Leads (Verifier runner, 27 Sept 2026)

SO-MCCORMICK-LEADS (SECOND-OPINIONS-QUEUE.tsv; PR 30; verbatim answer in
`second-opinions/chatgpt-leads-2026-09-27.md`; the runner was given the prompt only, not this target's own
plaintext/ciphertext -- leads only, every citation unchecked until verified here):

1. **Known keys/codebooks/shorthand (unverified).** FBI's 2011 *FBI Story* says family reported childhood
   coded notes and that investigators wanted a comparison sample; Tritto's 2012 *Riverfront Times*
   interviews instead have his mother and cousin denying he wrote in code, while CRRU's Dan Olson stood by
   his assessment -- a sourced conflict, not evidence for any particular key. No Gregg training or personal
   codebook found in print; Gregg is only a possible control design. FBI Vault's 2002/2009/2010 lab reports
   print no key or partial decoding.
2. **Printed/documentary beyond Cipherbrain (context, not decoding aids).** Tritto 2012 again for contextual
   detail (address/map comparisons, a "task list" impression of the circled groups; Olson's own address
   comparisons had not yielded a non-coincidental hit). FBI Vault's 11-page lab packet (a process record,
   not plaintext).
3. **Named analysts (conjectural, none a decipherment).** Nick Pelling (*Cipher Mysteries* 2013, 2024) --
   phonetic/local-geography hypotheses, isolates WLDNCBE/WLD'S NCBE, PRSEON, SE and numeric groups for
   comparison, asks for independent handwriting samples. Jessica Lorraine Scott (Dunn), "Beyond
   Cryptography" (Zenodo, 2026) -- a structural reading of CB as a recurring root with cannabis as a
   candidate (not confirmed); its PDF 429'd for this runner, body unread, abstract only. Elonka Dunin
   questioned McCormick's authorship after learning more of his background; Olson disagreed -- authorship
   itself is an open fork, not settled either way.
4. **Named next steps (concrete, untried here) -- flagged for the parent.** (i) Seek authenticated ordinary
   handwriting or earlier patterned notes for a blind comparison, since the FBI/family accounts conflict on
   whether he wrote in code at all. (ii) A pre-registered structural test on the observed token families
   (NCBE/WLDNCBE/WLD'S NCBE, the -RSE family) against shuffled-order/frequency-matched nulls, with held-out
   lines required to fit. (iii) Before trusting cheap test 4's annealer either way, build a synthetic
   control matched to the target's actual 132-token shape (singleton fraction, recurrent-token fraction,
   lexicon size) rather than relying on a longer, easier control -- the runner notes the repository's
   existing 132-token control recovers only 0.8% of its own mapping (rule 3's positive-control-subsampling
   amendment applies here too).

No lead is a printed decipherment of this target or its ciphertext, and none is a check-solved candidate;
item 4 names two concrete untried steps. No first/new/unpublished wording (rule 10).

## While waiting (27 Sept 2026, WAIT-PASS-B)

Waits on: nothing external. No REQUEST.md or ASKS.md row exists for this target; NEXT-STEPS.tsv's blocker
field reads "needs-key" (no established period key/codebook, cryptanalysis-only), not an archive or person
wait.

- S: finish the two rule-1 legs 25 Sept skipped for no-network (solver-repo grep + OpenAlex/S2) -- tools/print_check.py + a fresh clone.
- M: design a Gregg/abbreviation-lexicon-constrained code-word control per NEAR.md's own named next step (the current control recovers only 0.8% of its own ground truth) -- specs/cheap-tests/mccormick-1999/token_anneal.py + tools/family_run.py.
- S: check tools/data/ for any shorthand/abbreviation corpus already on disk that could seed a better-constrained control pool than the current 350-word free pick.

## Web and blog check (WEBCHECK-mccormick-1999, 2 Oct 2026)

Required step of `.claude/briefs/check-solved.md` ("Open web and blog comment threads", CHECK-SOLVED-WEB, 28 Sept
2026), run 2 Oct 2026 01:04-01:1x UTC by WEBCHECK-mccormick-1999 (account-4), brief
`.claude/briefs/runs/2026-10-01-account4-webcheck.md`. Famous item: many hits; the newest comment threads were read
first. Every claimed reading found is quoted verbatim below with its date; none is a verified decipherment, so the
status word on line 1 stays `open` (reasoning at the end of this section).

### (a) Plain web searches (11 queries, one search engine)

| # | query | result |
|---|---|---|
| 1 | `"Ricky McCormick" cipher notes 1999 solved` | Wikipedia, dcode.fr, Medium (theunknownblog), allthatsinteresting, historiqly, hubpages: all say unsolved; CRRU and ACA failed |
| 2 | `"WLDNCBE" OR "WLD NCBE" McCormick` (most distinctive ciphertext token) | Cipher Mysteries 2013/2016/2024 posts; Websleuths thread p.46; pastebin transcription; **Medium (rusandudewmina, Mar 2026) "decoded with aid of AI by a 15 year Old"** -- see hit M below |
| 3 | `"Ricky McCormick" "encrypted notes" FBI decipherment` (folder's descriptive title) | Wikipedia, scribd copy of it, morbidology, guyhadleigh, gsnsp, grokipedia: unsolved |
| 4 | `McCormick notes FBI code cracked 2025 OR 2026` | firstalert4 (Jan 2022), fastcompany, coldcaseexplorations, CBS, AOL: no crack reported |
| 5 | `scienceblogs.de klausis-krypto-kolumne McCormick` (Cipherbrain) | tag page + posts of 29 Aug 2013, 24 Oct 2014, 1 May 2018, mention in 25 Dec 2021 |
| 6 | `cryptiana.blogspot.com McCormick` (Cryptiana blog) | no McCormick post; only the blog's front page and 2018 archive index came back |
| 7 | `cryptiana.web.fc2.com McCormick 1999 notes` (Tomokiyo's pages) | no Tomokiyo page on McCormick; surfaced Zenodo record 18857434 (hit Z below) |
| 8 | `ciphermysteries.com Ricky McCormick` | posts of 12 Mar 2013, 12 Apr 2016, 26 Jul 2024; derekbruff podcast ep.34 (2019) |
| 9 | `"McCormick" cipher solves "Claude" OR "GPT" OR "ChatGPT" notes decoded` (model-solve announcements) | no McCormick model-solve claim; results are Kryptos K4/Enigma/other-cipher AI stories |
| 10 | `"Ricky McCormick" notes decoded "15 year old" OR teenager AI 2026` | only the Medium article itself (hit M); no second source reports it |
| 11 | `"Ricky McCormick" Reddit solved decoded notes theory 2025` | jimconnors.net podcast note (8 Apr 2025, "remain one of only two unsolved ciphers in FBI history"); no solved claim |

On-disk Cryptiana snapshot `sources/cryptiana/` grepped for McCormick (case-insensitive): no McCormick page (the three
hits are unrelated surnames in civilwar2.htm and beaufort.htm). Zero requests to cryptiana hosts.

### (b)+(c) Hits opened, comment threads read

**Cipherbrain (scienceblogs.de/klausis-krypto-kolumne), tag page `/tag/ricky-mccormick/` -- 3 posts, no pagination.**
- 1 May 2018, "The Top 50 unsolved encrypted messages: 10. Ricky McCormick's encrypted notes" -- 6 comments, all 1-4
  May 2018, none later (re-checked live 2 Oct 2026 against the on-disk snapshot read 25 Sept; unchanged). Comment 1
  (Anon) links a taringa.net Spanish "solution", dismissed in-thread by HF(de) as homophone guessing -- already on
  record in this file's intake note.
- 24 Oct 2014, "Der Code der Maisfeld-Leiche" -- 7 comments, 25-26 Oct 2014. No decipherment claimed; Hardy (26 Oct
  2014): "Dieses Prinzip wird ersichtlich, wenn man bestimmte Buchstabenkombis seiner Texte in Word mit Farbe
  markiert. WLD, NCBE, *SE. Vermutlich war die Bedeutung der Kürzel nur ihm zugänglich." (abbreviations, not a key).
- 29 Aug 2013, "Top-25 der ungelösten Verschlüsselungen -- Platz 7: Der Mord an Ricky McCormick" -- 23 comments,
  30 Aug 2013 to 11 Mar 2021, not truncated. Claims, verbatim: Agathon (5 Sept 2013) "If one replaces NCBE with ROAD
  and ONDE as 'on the'...comes in the Bronx on the 75 West Fordham Road"; Franz Fellner (24 Oct 2014) "NCBE steht für
  ROAD"; BREAKER (10 Nov 2019) "This is solved by removing the repeating patterns...Stennos as well as...Morse
  translation." None gives a key or a full plaintext; none was taken up by Schmeh or the other commenters.
- 25 Dec 2021, "Ungelöste Kriminalfälle mit ungelösten Verschlüsselungen" -- McCormick sentence: "Der mutmaßliche
  Drogenkurier Ricky McCormick wurde 1999 ermordet aufgefunden. Er trug zwei verschlüsselte Zettel bei sich, die nie
  dechiffriert wurden." 3 comments, none about McCormick.

**Cipher Mysteries (ciphermysteries.com, Nick Pelling).**
- 26 Jul 2024, "Nick's 2024 thoughts on Ricky McCormick and St Louis" (newest post) -- 12 comments, 27 Jul 2024 to
  2 Jun 2025, complete. Post: a St Louis geography/phonetics reading frame, PRSEON ~ "person", numbers possibly bus
  routes; not a decipherment. Claims in thread, verbatim: Ian Tucson (4 Aug 2024) "right side munarse anagrams to
  SURNAME"; Josef Zlatoděj Prof. (12 Aug 2024) "iCBE=11, NCBE=15" (gematria, "TOTE WLDi" read as German "dead");
  James M (12 Sept 2024) "MRDE LUSE" = "murderer loose", "D.W.M.Y" = "day week month year"; BREAKER (2 Jun 2025)
  removing repeating patterns reveals an "Eddie Munster" outline plus a CIA-trafficking narrative. No key, no
  line-by-line plaintext, no uptake by the host.
- 12 Apr 2016, "Ricky McCormick's notes - for 6th graders :-)" -- 52 comments, 12 Apr 2016 to 23 Aug 2023, complete.
  Post argues the notes are private semi-literate writing, not a cipher. Claims, verbatim: Abbey (24 Jan 2021) "i
  think the ncbe stands for a location, either on/ in/ north Cote Brilliante, the street that ran right by his high
  school."; Lizzy (31 Mar 2021) "I definatly think 'prseond e' relates to 'person is' ... (first person is 71 NCBE)
  (second person is 74 NCBE)"; James (5 May 2022) "luse to te wld = lose to the wild, Wild being the Minnesota Wild
  hockey team."; Mitch (23 Aug 2023) "I'm with lizzy on the first person second person." Word guesses only.
- 12 Mar 2013, "Ricky McCormick's mysterious notes..." -- header says 163 comments, 12 Mar 2013 to 28 Oct 2015; the
  page as served to the fetch tool ends mid-sentence at comment 78, and `/comment-page-2` returns the same 78 (so
  comments 79-163 were NOT read -- all fall in the 2013-2015 range per the header dates, no 2016+ comment exists
  on this post). Claims, verbatim: Jose Galofre Manero (14 Jun 2013) "'O-W-m-4 H8L XORLX' means 'OWN-FOR I AM
  MCCORM(i)CK'"; boydt (28 May 2013) "plenty of glass see out / you'll see me see me first / person drives wild an
  see me..."; Peter M (21-22 Jan 2014) mortgage rates "71, 74 and 75"; Tim Sawyer (11 Mar 2015) "It's all about
  Ricky going to RC Branson for a 'prse'-prize of a CBE rc airplane"; the coder (19 Jun 2015) "This document
  describes a way to create Lysergic Acid Diethylamide (LSD)"; IrishGuy (30 Jul 2015) "99.6.25 June Pulse increased
  a lot since Kansas". Mutually incompatible; none accepted by Pelling.

**Cryptiana (blog and Tomokiyo's pages).** No post or page on McCormick found by queries 6-7 or in the on-disk
snapshot. Nothing to open.

**Other plausible hits opened.**
- Wikipedia, "Ricky McCormick's encrypted notes" (read 2 Oct 2026): "Attempts by both the FBI's Cryptanalysis and
  Racketeering Records Unit (CRRU) and the American Cryptogram Association failed to decipher their meaning"; no
  claimed solution is named anywhere in the article.
- dcode.fr/mccormick-cipher: transcription only; "Nobody has yet found a perfect translation or explained the entire
  message without ambiguity." No dated user claims.
- Websleuths thread 131822 (47 pages, started 29 Mar 2011), pages 46-47 read (30 Sept 2025 to 4 Sept 2026, the
  newest posts anywhere). Claims, verbatim: Busrday (8 Dec 2025) "It's directions from Delmont, Ohio to Ft
  Lauderdale"; Imanuel (14 Apr 2026) "the first part of the note deciphers to 'All that glisters is not gold;Often
  have you heard that told:Many a man his life hath sold...'" followed in the same post by "just disproved myself";
  Detective Sharp Hawk-Eye (4 Sept 2026) "Interstate 75 and North County" odometer-reading theory. No AI/LLM solve
  and no mention of the Medium article on either page.
- **Hit M -- Medium, @rusandudewmina, "Cracking the Silence of 27 years old Murder Mystery: The way the Haunting
  Notes of Ricky McCormick were decoded with aid of AI by a 15 year Old.", dated March 2026 (search-engine
  date; the page itself returned HTTP 403 to the fetch tool and to one curl with a browser UA -- stopped after the
  one retry per the good-citizen rule; the Wayback CDX index reset the connection twice, so no archived copy was
  reached).** What is on record from the search engine's own snippets of the article, verbatim: the "decoded
  interpretation" of "WLD NCBE" is given as "Wouldn't be near us — not someone known."; the decoded content "appears to
  reference locations, warnings about danger, and various fragmented messages about not being able to promise things
  or return to certain places." No AI tool name, no key table, no FBI confirmation and no second source reporting the
  claim were found (queries 2, 9, 10). This is the one claimed reading of the item newer than the 25 Sept 2026
  intake note, and the first found that invokes an AI; it is logged here as a *claimed* reading whose body is unread
  from this container. **Follow-up (not done here, one line per Usage 7):** a LOCAL-QUEUE.tsv row to read the Medium
  page from the owner's browser and paste the claimed plaintext, so a verifier can rate it; until then any later
  reading of ours must be checked against it (rule 10: at best N1 against this article if it matches, which no one has
  tested).
- **Hit Z -- Zenodo record 18857434, Jessica Lorraine Scott (Dunn), "Beyond Cryptography: A Non Classical
  Interpretation of the McCormick Notes", 3 Mar 2026, DOI 10.5281/zenodo.18857434, PDF 537.9 kB** (the leads
  section above had this at abstract-only after a 429; the record page answered this time). The abstract itself:
  the notes are "a constrained workflow system rather than concealed prose", and "the central claim concerns
  patterned organization rather than confirmed material identity" -- explicitly not a decipherment or plaintext.

### Verdict of this step

no decipherment or plaintext of this item located by these queries on 2 Oct 2026 (a search result, never a novelty
verdict, rule 10). Every claimed reading above is either a one- or two-word guess at a token (NCBE = ROAD / a street /
a bag), an anagram or gematria, a full-text reading that its own author or the thread withdrew or ignored, or (hit M)
an AI-assisted interpretation with no key, no second source and the body unread here; the newest authoritative
statements (Wikipedia, dcode.fr, Cipherbrain 2021, Websleuths Sept 2026) all still say unsolved. The 25 Sept 2026
intake note treated the taringa.net "solution" the same way (a claim rejected by the thread, not a decipherment),
so the status word stays `open`. Hits M and Z are the two items a verifier's AUDIT.md must cite as prior claimed or
structural readings. Comments 79-163 of the 2013 Cipher Mysteries post are the one unread stretch (2013-2015 only).

Requests per host: search engine 11 queries; scienceblogs.de 5; ciphermysteries.com 4; websleuths.com 2;
en.wikipedia.org 1; dcode.fr 1; zenodo.org 1; medium.com 2 (both 403, stopped); web.archive.org 2 (both connection
reset, stopped); cryptiana hosts 0 (on-disk snapshot). No login, no credential used.

`python3 tools/intake_gate_check.py mccormick-1999` after this section:

```
mccormick-1999: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit=0
```
