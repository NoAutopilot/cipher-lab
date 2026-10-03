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

- [x] S: finish the two rule-1 legs 25 Sept skipped for no-network (solver-repo grep + OpenAlex/S2) -- tools/print_check.py + a fresh clone. Done 2 Oct 2026 (OPEN-mccormick-1999 below): solver repos 0 target/key/reading; OpenAlex 4 claimed or structural readings logged, none verified; S2 429-blocked after 10 keyed requests.
- M: design a Gregg/abbreviation-lexicon-constrained code-word control per NEAR.md's own named next step (the current control recovers only 0.8% of its own ground truth) -- specs/cheap-tests/mccormick-1999/token_anneal.py + tools/family_run.py.
- [x] S: check tools/data/ for any shorthand/abbreviation corpus already on disk that could seed a better-constrained control pool than the current 350-word free pick. Done 2 Oct 2026 (OPEN-mccormick-1999 below): none on disk; en_vdrop is a vowel-drop transform of two novels, not a shorthand lexicon.

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

## OPEN-mccormick-1999 (2 Oct 2026, account-4)

Brief `.claude/briefs/runs/2026-10-02-account4-open-step.md`; the two S items of "## While waiting" above, run
02:45-02:5x UTC 2 Oct 2026. Intake gate before the step: `mccormick-1999: open (line 1) -- edition/page or
full-text-search citation found within 6 lines`, exit 0. Status word on line 1 unchanged (`open`): nothing below is a
verified decipherment (reasoning at the end). Vision calls 0.

### Step 1a: the two solver repositories (rule 1 leg skipped 25 Sept)

One shallow clone each to the scratchpad, grepped (case-insensitive, `mccormick|wldncbe|ncbe|ricky`), deleted after
reading; nothing copied (Aymeloglu's repository has no licence; cited only).

| repository | HEAD read 2 Oct 2026 | target folder, key or reading? | what it says |
|---|---|---|---|
| github.com/dbourdeau/cyphersolver | 34e0fc8 (1 Oct 2026) | none (`targets/` has no McCormick folder) | TARGETS.md: among sixteen top-50 items "open but not settleable by cryptanalysis", "not scored"; research/top50/NOTES.md row 10: "FBI CRRU and the ACA both failed; Pelling judges it private shorthand rather than a cipher"; research/mtc3/RESEARCH.md: MTC3 challenge 379 "Twelve-Year-Old Murder Case (the McCormick notes)" listed as an open research problem under the project's FAMOUS exclusion |
| github.com/aaymeloglu/unsolved-ciphers | d2800bb (27 Sept 2026) | none | SHORTLIST.md line 105 lists McCormick with Scorpion, Blitz, Chinese gold bars, Hampton, Penitentia under "Hoax risk, no context, or no real system" |

Result: not found in either solver repository by grep of a fresh clone on 2 Oct 2026 -- neither has attempted it.
(One lead for the file: MTC3's challenge 379 is this item; its page is not a reading, only a challenge entry.)

### Step 1b: OpenAlex and Semantic Scholar through `tools/print_check.py`

`phrases.txt` (8 lines: the item's name, "McCormick notes", and six distinctive ciphertext tokens, since no decode
exists) and `sources.tsv` (3 keyword rows) written in this folder; run `--only openalex,s2 --max-requests 40`, keys
read from the environment by the tool (never printed). Output `print-check.tsv` and `print-check-hosts.tsv`;
the one permitted retry of Semantic Scholar after a pause went to `print-check-s2-retry.tsv`.

| host | requests | outcome |
|---|---|---|
| api.openalex.org | 11 (print_check) + 3 (full records with abstracts, `select=` fields) = 14 | ok; 6 ciphertext-token phrases 0 hits each; name and keyword queries 9 / 203 / 3 / 12 / 0 works |
| api.semanticscholar.org | 6 + 4 (retry) = 10 | HTTP 429 with the key on request 6, again on request 4 of the retry; the three keyword queries and five of the six token phrases never ran. Logged as **unreachable this session**, not searched; the two name queries that did answer return millions of papers (S2 ignores the quotes), so they discriminate nothing |

OpenAlex works that are about this item (every other hit is an unrelated McCormick), read from their OpenAlex
abstracts only, PDFs not fetched (no host beyond the two named in the brief):

| date | work | DOI | what it claims |
|---|---|---|---|
| 26 Jan 2026 | Masataka Tsuchimoto, "Research Paper: Structural Solution of the Ricky McCormick Notes -- The 14th Pillar of Nexus Dynamics: Restoration of the 1999 Medical Protocol" (Zenodo preprint, two versions) | 10.5281/zenodo.18375727, .18375728 | A full claimed reading: "V-Removal" plus "Dot-Linking" turn the notes into "a dynamic 24-hour medical instruction set", with a table of tokens as drug names (PNSE = Prednisone, SE/NSE = Serevent, ALPM/ALPRM = Alprazolam ...). Abstract itself says "the first structural solution". No key table beyond the drug glosses in the abstract, no control, no FBI or second-source confirmation located |
| 17-24 Jun 2026 | Sanaa Sadak, "Forensic Manuscript Volume VI" (Zenodo, four records: "The Unified Applied Computational Resolution of the Ricky McCormick, Oakland County, and Somerton Man Cold Cases"; "Forensic Phoneto-Spatial Applications of the STYLOARAB Matrix ...") | 10.5281/zenodo.20738349, .20738350, .20767124, .20767125, .20836219 | Claims "the definitive empirical decryption of the Ricky McCormick pocket notes" by a "StyloArab / SEPF v1.0" profiling system; the one line quoted in the abstract is note 2 line 10, `26 MLSE 74 SPRKSE 29KCNOB,OLE 175 RTRSE`, expanded to "36 MILES 74 SPRING PARK 29 BLOCKS 175 ROUTE TRAFFIC" at a "94.2% Absolute Stylometric Similarity Coefficient" (note the 26 -> 36). Same system is said to resolve the Somerton Man and an Eratosthenes inscription in the same paper |
| 2026 | Ky Nash, "Sigilith Case Study #2 -- The McCormick Notes" (Humanities Commons) | 10.17613/dkgpg-xbj95, 10.17613/sqj9k-98496 | Structural, not a reading: "classified not as a cipher, but as a directional movement-loop system ... consistent with personal mnemonic tracking"; "without assuming linguistic content" |
| 3 Mar 2026 | Jessica Lorraine Scott (Dunn), "Beyond Cryptography: A Non Classical Interpretation of the McCormick Notes" | 10.5281/zenodo.18857433/.18857434 | Already on file as hit Z (web check above); surfaced again by the keyword query |

Result: no verified decipherment of this item located in OpenAlex on 2 Oct 2026; two **claimed** full or partial
readings (Tsuchimoto Jan 2026, Sadak Jun 2026) and two structural non-cipher interpretations (Nash, Scott) are now on
record beside hits M and Z of the web check. Rule 10: a verifier's AUDIT.md for any future reading of ours must cite
all four and test ours against the Tsuchimoto and Sadak glosses (at best N1 against whichever matches, which nobody
has tested). Neither claim moves the status word: the Tsuchimoto reading is a token-to-drug-name table with no key or
control stated in its abstract and no uptake found elsewhere (the 2 Oct web check's Wikipedia, dcode.fr, Cipherbrain
and Websleuths pages all still say unsolved and name neither paper); the Sadak line reading changes a ciphertext
digit (26 -> 36) and comes from a system that also claims to solve the Somerton Man in the same paper. Both are
claims to rate, not solutions found; the status stays `open`, not `found-solved`.

### Step 2: a shorthand or abbreviation corpus in tools/data

`ls tools/data` (39 entries) plus a grep of `tools/`, `specs/` and the repository's md/py/json/tsv for
shorthand/Gregg/Pitman/abbreviation corpus or lexicon: **none on disk**. The nearest things: `tools/data/en_vdrop`
(25 Sept 2026, bMCC2) is a word-internal vowel-drop transform of the two `en` novels (first letter kept, 0.688 of
letters retained), already used as the matched-design corpus for cheap tests 2 and 3 -- a synthetic shorthand of
English prose, not a lexicon of attested abbreviations; `tools/data/uscodes-1800` is a US nomenclator code corpus,
not shorthand; `specs/cheap-tests/untersberg-code/test1_abbreviation.py` tests internal abbreviation structure and
says in its own header that no external abbreviation corpus is on file. `token_anneal.py`'s control pool
(`POOL_N = 350`, the corpus's 350 most frequent words, `FREQ_N = 60` shared placeholders) therefore still has
nothing better-constrained to draw from in this repository.

Result: not found in tools/data on 2 Oct 2026; building one is the M item above ("design a Gregg/abbreviation-
lexicon-constrained code-word control"), which stays untried.

### Named next step (one, with cost)

Rate the two claimed readings before any further family work: a Sonnet worker fetches the Tsuchimoto (zenodo
18375728) and Sadak (zenodo 20767125) PDFs once to this folder's `second-opinions/`, extracts each paper's full
token-to-gloss table, and scores it the way the 25 Sept controls were scored -- apply the table to both notes, run
`tools/judge_plaintext.py specs/mccormick-1999.json` on the result beside the shuffled-target control, and check the
Sadak line 10 digits against the spec's transcription (26 vs 36). About USD 3, zenodo.org at most 4 requests, vision
0. A PASS against the shuffled control would make either paper the N1 reference for this item; a FAIL closes the
claim with a number instead of a sentence.

Requests per host this step: github.com 2 (two shallow clones, deleted), api.openalex.org 14, api.semanticscholar.org
10 (429 twice, stopped). No login, no credential printed. Box 02:45 to the done line, of 45 minutes.

## Premise check (GF4-BATCH4, 3 Oct 2026)

Adversarial pass (.claude/briefs/check-solved.md lines 123-139): tried to show a verified decipherment already exists. None found; no decode or test run here. Builds on WEBCHECK (2 Oct) and OPEN (2 Oct) above, not repeated.
(a) Decipherments named in this folder: found, none verifiable. Opened: the taringa.net "solution" (via the Cipherbrain 2018 thread, NOTES intake note: homophone guessing, dismissed in-thread); the 2 Oct claims (Medium Mar 2026 hit M, Tsuchimoto 10.5281/zenodo.18375728, Sadak 10.5281/zenodo.20767125, Nash, Scott hit Z): claims without key table/control, bodies partly unread; second-opinions/chatgpt-leads-2026-09-27.md ("No lead is a printed decipherment"). New this pass: felixmaocho.wordpress.com/2011/10/19 (read 3 Oct) reprints José Galofré Manero's Oct 2011 claim (alternate Caesar shift + sound-alike digits 4=for, 8=A + vowel-dropped shorthand; reads note 2's last line "O-W-m-4 H8L XORLX" as "Own why I am McCormick", a will with treasure at "Marais Temps Clair"); the host blog itself says no independent verification, FBI never answered, no treasure found; no consistent key across both notes, ciphertext tokens altered to fit. Not a verified decipherment.
(b) Other solvers' working files: found, none a solution. Solver repos: dbourdeau/cyphersolver 34e0fc8 and aaymeloglu/unsolved-ciphers d2800bb, grepped 2 Oct (OPEN-mccormick-1999 step 1a; not re-cloned): no McCormick folder/key/reading. GitHub code search "WLDNCBE" (3 Oct, 27 hits, 8 repos besides this one): doranchak/azdecrypt (Ciphers/Unsolved/Ricky McCormick page 1.txt, transcription only), doranchak/zodiac-killer-ciphers (tests/ricky/RickyMcCormick.java, opened via raw.githubusercontent: transcription + repeated n-gram counter, no key/plaintext), matthewdgreen/cipher_benchmark (benchmark/unsolved/sources/ricky_mccormick: documents/, metadata/, transcriptions/ only; listed as unsolved), zernanvash/cheatsheet (copy of the dcode page); other hits unrelated noise. No GitHub repository named for the item (repo search 0). Reddit/Websleuths/Cipher Mysteries/Cipherbrain threads: read 2 Oct (WEBCHECK table); Reddit not separately reachable by this tool; WebSearch "reddit codes working McCormick" 3 Oct returned no solve thread.
(c) Neighbouring items / accompanying clear text: not found. The FBI release is the two pocket notes only; Wikipedia (read 2 Oct), dcode.fr, esascosas.com/codigo-mccormick (opened 3 Oct, "No Solution Offered") name no other cipher document, clear copy or crib beside them; fbi.gov pages (/news/stories/ricky-mccormick-cipher, /wanted/ricky-mccormick) answered HTTP 403 to the fetch tool, logged unreachable, no retry; the FBI's statement is therefore taken from secondary pages (CRRU + ACA failed) and Wikipedia's citation of it.
(d) Investigating side (FBI/FOIA/news "solved" claims): not found. WebSearch 3 Oct (4 queries incl. interior tokens "WLDNCBE", "PRSE ONDE", "NCBE", Spanish title of the taringa post): Wikipedia, dcode.fr, CBS, NBC, Fox, AOL all say unsolved; larepublica.pe 2019, es.wikipedia, bahiasinfondo 2014 repeat it; no FOIA release or St. Louis County/police "decoded" statement located. Requests: WebSearch 5, WebFetch 7 (2 x 403), GitHub MCP search 2 (+2 repo reads refused by session scope), no login.

Result: not found-solved -- stays open (a search result, rule 10; nothing here supports new/first wording).
Next cheap test: the 2 Oct "Named next step" above, rating the Tsuchimoto and Sadak tables (fetch the two Zenodo PDFs, apply to both notes, `tools/judge_plaintext.py specs/mccormick-1999.json` beside the shuffled control, check Sadak line 10 26 vs 36), about USD 3.

## Cheap test 5 (FT4-mccormick-1999, account-4, 3 Oct 2026 00:28-00:45 UTC) -- rating the Tsuchimoto and Sadak readings

Other people's readings, scored only (rule 10); no new solving. Sources (both CC BY 4.0, copies kept in `second-opinions/`
with text extracts): Masataka Tsuchimoto, "Research Paper: Structural Solution of the Ricky McCormick Notes", Zenodo,
26 Jan 2026, https://doi.org/10.5281/zenodo.18375728 (`tsuchimoto-18375728.pdf/.txt`); Sanaa Sadak, "Forensic Manuscript
Volume VI", Zenodo, 19 Jun 2026, https://doi.org/10.5281/zenodo.20767125 (`sadak-20767125.docx/.txt`).

**What the papers actually give.** Neither is a full reading. Tsuchimoto: a six-row table (PNSE=Prednisone, SE/NSE=Serevent,
ALPM/ALPRM=Alprazolam, OLPLM=Olanzapine, WBT=Wellbutrin, ACDN=Acetaminophen+Codeine) plus "V-Removal" and "Dot-Linking";
PNSE, ALPM, ALPRM, OLPLM, WBT and ACDN do not occur in the transcription at all, and the paper decodes no line. Sadak: one
line (note 2 line 10) rendered "36 MILES 74 SPRING PARK 29 BLOCKS 175 ROUTE TRAFFIC" from a source line he transcribes
`36 MLSE 74 SPRK[SE...] 29KE[NO...] 175R[TR...]`; the spec (Schmeh's retype) has `26 MLSE 74 SPRKSE 29KCNOB,OLE 175 RTRSE`
-- his 36 vs 26, KE vs KC, and dropped OLE are departures from the transcription, unchecked against the image here (rule 2:
conditional on the transcription). No key, no method a script can rerun ("Excel VBA core"), so the ARM-C1 shuffled-decode
check is done by applying each paper's own table to shuffled ciphertext, the only mechanical part.

**Method.** `specs/cheap-tests/mccormick-1999/test5_rate_claims.py` -> `test5_result.json`. Each table applied to both notes
(746 letters), unglossed text left in place; shuffled-target control = the notes' letters permuted within each note
(separators kept), K=20, seed 1999 -- this control *can* differ on both coverage and score (it changes which substrings
occur; a token-order shuffle could not, bCAS). The judge's own controls are the shuffled-null p99 and the real-text p05.
Corpora: default `en` and a US-vernacular pair (Huck Finn + Gatsby, `tools/data/en/`), the nearest on disk to 1999 US
vernacular; no 1999-era corpus exists in tools/data. **Corpus caveat (rule 3):** `en` is of unknown reliability --
judge_plaintext.py gives no per-fold figures, so from `tools/data/en/README.md`: leave-one-file-out false negatives
17.0-80.5% per fold at N=200 (spread 0.635) and 9.5-84.0% at N=500 (spread 0.745); real_p05 per fold sits at -0.88 to
-0.91. The full-notes FAILs below miss real_p05 by about 1.2 log10 units, far outside that fold band, so the caveat does not
touch them; it does touch the line-level result.

| Reading (variant) | corpus | letters glossed | judge score | null_p99 | real_p05 | verdict | shuffled-target (K=20): score min/med/max, PASS count, coverage med |
|---|---|---|---|---|---|---|---|
| unglossed notes (reference) | en | 0% | -2.171 | -2.071 | -0.864 | FAIL | -- |
| Tsuchimoto, whole-token match | en | 0.5% | -2.157 | -2.056 | -0.859 | FAIL | -2.224/-2.110/-2.045, 0/20, 0.0% (target rank 5/20) |
| Tsuchimoto, whole-token match | us-vern | 0.5% | -2.104 | -2.048 | -0.831 | FAIL | -2.195/-2.086/-2.007, 0/20 (rank 7/20) |
| Tsuchimoto, substring + V-removal | en | 20.4% | -1.720 | -2.080 | -0.858 | FAIL | -2.091/-2.003/-1.902, 0/20, 4.0% (rank 20/20) |
| Tsuchimoto, substring + V-removal | us-vern | 20.4% | -1.763 | -2.070 | -0.839 | FAIL | -2.073/-1.999/-1.883, 0/20 (rank 20/20) |
| Sadak, four glosses as substrings | en | 3.4% | -2.105 | -2.064 | -0.884 | FAIL | -2.214/-2.110/-2.045, 0/20, 0.0% (rank 12/20) |
| Sadak, four glosses as substrings | us-vern | 3.4% | -2.048 | -2.057 | -0.849 | FAIL | -2.185/-2.086/-2.007, 0/20 (rank 15/20) |

Tsuchimoto's substring variant beats all 20 shuffles only because "SE" (his Serevent) sits inside the notes' own repeated
-RSE/-NSE endings, so it pastes one English word over 20% of the letters; it is still about 0.86 below real_p05. Not
evidence for the table: the table glosses one recurring bigram, not the notes.

**Line level (Sadak's line only, length check dropped, 33 letters).** His rendering scores -0.987 (en; real_p05 -0.947,
null_p99 -1.582) and -1.154 (us-vern; real_p05 -0.948): FAIL, near the gate. Placebo lines (same digits, his four slots
filled with random Gatsby words of the same lengths, K=20) score median -0.936 (en) / -0.974 (us-vern) and PASS 10/20 and
7/20; an ordinary 39-letter English sentence PASSes (-0.754). So at this length the judge cannot tell any hand-chosen
English words from a decipherment: a non-test ("judge cannot decide"), and his line sits below the placebo median anyway.

**Verdict.** Tsuchimoto: FAIL on both notes (both variants, both corpora), glosses 0.5% (whole tokens) to 20.4% (one
bigram) of the letters; target inside or barely above its shuffled controls; not a reading of the notes. Sadak: FAIL on both
notes (3.4% glossed, inside the shuffle band); his one line is judge-cannot-decide at 33 letters against placebo controls,
and rests on three departures from the spec's transcription. Neither paper is the N1 reference for this item; status stays
`open` (no H, C or S tokens anywhere). Requests: zenodo.org 4 (2 record JSON, 2 files), no login. Next cheap step for the
transcription departures: check note 2 line 10 (26/36, KCNOB/KENO) against the FBI image, which also serves any future
reading; one image fetch, ~USD 1.
