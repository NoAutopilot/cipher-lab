# Survey of the public unsolved-cryptogram list, with an approach per item

Written 24 Sept 2026, 20:44-21:20 UTC, by the survey worker (claude-fable-5-1, session_013GkMQP9y84gHGG4pSSwaQj),
brief `.claude/briefs/runs/2026-09-24-survey-top-unsolved.md`. Rule 10 wording throughout: an approach is not a
claim, a "no hits" is a search result, and nothing below is called new, first or unpublished.

## Sources and what was checked

- **Klaus Schmeh, "The Top 50 unsolved encrypted messages"** (Cipherbrain, scienceblogs.de, compiled Feb 2017 to Apr
  2020): the index page and 27 of the 50 item posts, fetched once on 24 Sept 2026 with a browser User-Agent, 2.2 s
  apart, saved under `sources/schmeh/` with `manifest.tsv` (29 requests to scienceblogs.de in total, none refused).
  Every item below is one of Schmeh's 50; his numbering is kept in the "no." column.
- **Elonka Dunin, "Famous Unsolved Codes and Ciphers"** (elonka.com/UnsolvedCodes.html): unreachable from this
  container on 24 Sept 2026: curl got HTTP 202 with a 187-byte challenge body (one request), the fetch tool got an empty
  page, and the Wayback CDX index reset the connection twice. Not retried further (good-citizen rule). Dunin's list
  overlaps Schmeh's on the famous items (Voynich, Beale, Kryptos, Zodiac, Dorabella, Shugborough, Chinese gold bars,
  McCormick, Somerton) and adds undeciphered scripts (Phaistos, Rongorongo, Linear A) and the d'Agapeyeff cipher (1939,
  which Bourdeau assesses as "not enciphered English", QUEUE.md). That overlap is from memory, not from the page: if the
  owner pastes the list into `UNSOLVED-PUBLIC-LIST.md`, reconcile it against this table.
- **codebreaking-guide.com/links/unsolved-cryptograms/**: behind a robot challenge, per the brief; not retried.
- **Status per rule 1**: for every item, a search-engine check on 24 Sept 2026 (WebSearch, 30 queries), Wikipedia
  where it has an article, `QUEUE.md`'s "Dropped this sweep" table (which already carries Bourdeau's assessments of
  most famous items, from cyphersolver's catalogue), `LANDSCAPE.md`, and the two solver repositories' snapshots in
  `sources/solver-diffs/`. Satoshi Tomokiyo's list (Cryptiana, `CATALOG.md`) covers the diplomatic nomenclators, item
  34, and is not repeated here.
- **Tests actually run** (rule 3, three tests under $2 each, scripts and outputs in `specs/cheap-tests/`): Köhler
  index of coincidence; Lima 1916 substitution annealing with matched controls; Somerton code lines against the
  word initials of FitzGerald's Rubaiyat with a random control. Results are in the rows and in the specs.

## What the 2025-26 mathematics results teach, applied here

The Erdős-problem wave (Google DeepMind's Aletheia, 700 open problems evaluated and four resolved autonomously;
OpenAI/Harmonic's Aristotle with GPT-5.2 Pro on Erdős #728, arXiv 2601.07421, the first Lean-verified autonomous
resolution; Erdős #1196 in May 2026 with Tao and Lichtman; Quanta, "Why the Legendary Erdős Problems Are Falling to
AI", 3 Aug 2026) worked because the problems sat in one machine-readable repository, each attempt could be judged by a
machine (Lean), the win rate was low but the attempts were cheap and many, the literature was searched first because
the commonest failure was rediscovering a printed result, every solution was re-derived by a fresh instance, and effort
went to problems where the model was strong and the statement was formal, not to the famous ones. Sir Thomas
Urquhart's Cyphral Distich, no. 28 on this very list, fell on 31 Aug 2026 to the same pattern (Vals AI, Geby Jaff:
"the key is the host text", 44 minutes, `LESSONS.md`).

This survey applies that: `specs/<slug>.json` is the repository; `tools/judge_plaintext.py` is the mechanical judge;
the ranking prefers a cheap, self-judging first test over fame; and every row states where the item was searched
before any test is proposed. The process changes are in `PROCESS-2026-09-24.md`.

### Added 25 Sept 2026: what the Navier-Stokes result adds (OpenAI, 8 Sept 2026)

Source and what could be fetched: `sources/openai/NOTES.md` (the announcement page is 403 from the cloud; the paper PDF
is on disk; the method figures below are OpenAI's words as quoted in the coverage). Added by parent 7c at the owner's
request. The result: about 10,000 coordinating agents, in groups that talked inside the group, with a cached internet
and code execution, resolved forced Navier-Stokes blow-up in 88 hours (2.7 million messages, about 130 billion output
tokens), after about 100 agents had first resolved the easier unforced Euler problem in 50 hours; the Navier-Stokes
group was "prompted with the Euler resolution", the model was upgraded mid-effort, a separate tool consolidated "the
most useful insights" between rounds, and a Lean formalization (17 more hours) is what confirmed validity while the
human evaluation stays "deliberately unhurried". Seven points transfer, each with its cipher form:

1. **Sibling first, then transfer.** Before any spend on the target under hypothesis family H, make the solver read a
   matched synthetic under H (rule 3 as the organising principle, not a footnote), and hand the solved control's
   method, parameters and pitfalls to the target run as its prompt. A family whose control does not read is not run
   on the target at all.
2. **Groups that talk inside the group.** One hypothesis family is one group of workers sharing one append-only file,
   `ciphers/<t>/HYPOTHESES.md` (what was tried, the control and target numbers side by side, partial decodes, cribs,
   dead ends). Groups need not read each other; the consolidator does.
3. **Consolidate, then re-prompt.** Each cycle an Opus or Fable consolidator rewrites the file's summary and the next
   round's worker brief from what the swarm found. The swarm is Sonnet; the consolidation and the hypothesis design are
   the strongest model; that is our "upgrade mid-effort".
4. **Scale is attempts, not one long think.** One result cost millions of messages. The cipher form is a standing lane
   on the two or three items where some family has headroom: many short Sonnet restarts over seeds, corpora, key texts
   and tabula variants, every negative written into the spec with its control, and no expectation that any single
   worker reads the target.
5. **Cached internet, code execution.** Fetch once (Kahn 1981, the KV 2 catalogue, the Gutenberg key texts) into
   `sources/` and the target folder; every test is a script that reruns from disk.
6. **The machine verdict is the only gate.** `tools/judge_plaintext.py` with its control, then a fresh-instance
   re-derivation, are what let a candidate reading leave the lane; a separate verifier lane classes it (rule 10). The
   lane never says solved, and the judge says "worth a verifier", never "right".
7. **Literature and priority first.** OpenAI conceded priority on forced Euler to work it had not seen. Check-solved
   with the intake gate before the campaign, the archive route before cryptanalysis (an Abwehr decrypt in HW 19 or a KV 2
   file ends Köhler as found-solved), and a phrase search after any reading.

What does not transfer: the concurrency (one account's rate window; the lane runs at most eight live workers) and the
formal checker (a language judge is a statistic, not a proof). The lane built on these points is LANE GOLD
(`.claude/briefs/runs/2026-09-25-lane-gold-orchestrator.md`, PROCESS-2026-09-24.md proposal 6).

## Ranking rule

Expected value = P(the cheap test moves the item) x value of moving it / cost of the test. "Moves" means a reading
that passes the judge, a found-solved verdict, or a matched-control negative that closes a hypothesis. Items the whole
field has failed on for decades with heavy compute (Voynich, Kryptos K4, Zodiac Z13/Z32, Beale, Rohonc) go to the bottom
unless a specific untried cheap test exists; where none exists the row says "none". Items already solved or explained
are listed last, unranked, with the solver and date, so nobody re-solves them.

## The list

Columns: rank (EV), Schmeh no., item, date, language, size and alphabet, where the ciphertext is and whether a clean
transcription is on disk, status on 24 Sept 2026 with source, who is working, and the approach (cheap test, matched
control, cost, model). "Bourdeau" = dbourdeau/cyphersolver's catalogue as snapshotted in `QUEUE.md`; "Aymeloglu" =
aaymeloglu/unsolved-ciphers.

| Rank | No. | Item | Date | Lang. | Size, alphabet | Ciphertext | Status 24 Sept 2026 | Working on it |
|---|---|---|---|---|---|---|---|---|
| 1 | 47 | Köhler cryptograms (Walter Koehler, Abwehr, via Paris) | Feb 1944 | de/nl/en | 5 messages, 924 letters, a-z, 5-letter groups | Kahn, Cryptologia 5:2 (1981); transcription on disk `sources/schmeh/posts/47b-*` and `specs/koehler-1944.json` | open (Schmeh 2021 update; not in either solver repo); **LANE B 24 Sept 2026: periodic IC p2-30 flat, best 0.0468 vs periodic-key control 0.065-0.081 / one-time-key control 0.044-0.047; next: archive route (TNA KV 2 / HW 19)** | nobody found |
| 2 | 3 | Debosnys cryptograms (Essex County jail, NY) | 1882-83 | fr/en/pt/la | 4 cryptograms, invented symbols, counts unknown | Farnsworth 2010, Schmeh post 3 images; not on disk | open (search 24 Sept 2026; Schmeh 2020 "few experts") **LANE B2 25 Sept 2026: test 1 images (4 of 5 cryptograms) + machine sign inventory, 1032 signs, K=90 over-split, IC 0.0125 vs random 0.0111 / French 0.070: inconclusive until an atlas merges clusters; a French poem in clear on the cryptogram 3 page (ciphers/debosnys-1883/).** | nobody found |
| 3 | 5 | Somerton Man / Tamam Shud code | 1948 | en (initials) | 5 lines, 50 letters, 12 distinct | on disk (`specs/somerton-1948.json`) | open; man identified as Carl Webb 2022 (Abbott, Fitzpatrick); code unread | Abbott's group (Adelaide); Bourdeau: famous list, "not a cipher" |
| 4 | 18 | Moustier altar inscriptions, Belgium | 19th c. | la/fr/nl | two altars, symbol set uncounted | Schmeh's photos (post 18), Pelling 2013, NSA Cryptolog; not on disk | open (Connart since 1961; Schmeh 2017) **LANE B2 25 Sept 2026: test 1 images + two blind passes, 158 signs, agreement 90.5%, IC 0.0499 vs Latin 0.072 / French 0.073 / random 0.0385: between, not informative; ciphertext on disk (ciphers/moustier-altars/).** | nobody found |
| 5 | 19 | Kaliningrad (Baltiysk) bottle post | Soviet era, found 2015 | ru-latin/pl/lt/de | 2 sheets, 37 signs incl. apostrophes, IC 0.054 | Cipherbrain post 19 images; Russian blog transcription; not on disk | open (58 comments, no solution) **LANE B2 25 Sept 2026: test 1 Ernst transcript matches both images 26/26 lines; N=978 K=36 IC 0.0657 vs transliterated Russian 0.056 / German 0.072: not informative; ciphertext on disk (ciphers/kaliningrad-2015/).** **LANE GOLD3 26 Sept 2026 (GOLD-KAL1, reserve): Synodal-chapter crib claim (Frank 2021) tested by word-pattern solver, control 0.997-0.999 vs target words matched 0.118/0.123 against a shuffle null max 0.096/0.080 (no flag); German light homophonic K36 control 0.982 vs target judge FAIL: control-backed negative. Russian Synodal corpus tools/data/ru19 on disk.** **GOLD-CONS4 26 Sept 00:52: transliterated Russian from ru19 under three schemes at N 978 gives IC 0.0547-0.0611 (K 34-37), bracketing the target's 0.0657 at K 36, so the earlier IC gap was a scheme mismatch, not a language exclusion; Russian substitution never run -- GOLD-KAL2 (Russian under transliteration) and GOLD-KAL3 (Polish) briefed.** | nobody found |
| 6 | 7 | Cigarette-case dedication, Thuringia | 24 Dec 1909 | de/la | 4 lines, 47 signs, ~18 distinct | owner's transcription on disk (`specs/cigaret-case-1909.json`) | open (Schmeh 2018); **LANE B 24 Sept 2026: German MASC anneal FAIL on judge, but control reads only 4-22% at N=45, K=18 (spec's 47 re-parsed to 45): uninformative, not a negative** | Schmeh's readers (Krauss, Biermann, Gaffney, Bosbach) failed |
| 7 | 22 | Powers cryptogram (dedication, The Gold Bug Variations) | 1991 | en/initials | 32 triplets, 3 unknown letters | on disk (`specs/powers-1991.json`) | open per Schmeh 2017; **print check pending**: J. T. Thomas, "Deciphering the code in Richard Powers's The Gold Bug Variations" (article title claims a decipherment; cloud gets 403) **LANE B2 25 Sept 2026: test 1 print check: no decipherment found in the open indexes; initials hypothesis in print since Herman and Lernout 1998; Thomas 2006 full text queued (LOCAL-QUEUE L15).** | Bourdeau: "not settleable by cryptanalysis" |
| 8 | 26 | Dorabella cipher (Elgar to Dora Penny) | 14 Jul 1897 | en/phonetic/music | 87 symbols, 24 = 3 arcs x 8 orientations, lines 29/31/27 | Schmeh's letter transcription on disk (`specs/dorabella-1897.json`); image at Elgar Birthplace | open; Wase, Cryptologia 49:1 (2025): not a MASC of English or Latin; claims by Sams 1970, Henderson 2011, Packwood 2020, Belanger 2025-26, none accepted **LANE B2 25 Sept 2026: test 1 blocked: the July 1897 covering letter is not in the open Powell 1937 copy; lending-only copy, ASKS row 50.** | Cipher Mysteries thread; Bourdeau: famous list |
| 9 | 16 | Lima, Ohio robbery cryptogram | 27 Jun 1916 | en/code | 71 cipher letters in 17 words + 6 clear words | two newspaper transcriptions on disk (`specs/lima-1916.json`); no manuscript | open (Schmeh 2017; Pelling 2013); **our cheap test 2: negative vs matched controls** **LANE B2 25 Sept 2026: test 1 codebook grep (ABC, Western Union, Lieber, Bentley) target 2/2/1/3 of 17 vs random-string 2/1/1/3, positive control 17/17: at chance, negative.** | Bourdeau: odds low |
| 10 | 30 | Harry-Caroline (1863) and Tissie-Jabber (1901) ads | 1863; 1901 | en | 44 + 27 letters; 13 + 9 four-letter groups over d o n a b c | on disk (`specs/harry-caroline-1863.json`), from Gaffney's Agony Column | open (Schmeh 2017) **LANE B2 25 Sept 2026: test 1 MASC with word breaks judge FAIL (-1.442) vs control 16-34% letters right at N=74: control too weak, uninformative; test 2 (name-keyed Vigenère) is next if wanted.** | Gaffney |
| 11 | 23 | Copenhagen cryptogram (behind an 1835 painting) | post-war note | da/de/en | one sheet, letters; Briere: simple substitution | Cipherbrain post 23 scan (Ramliden); not on disk | open (ACA failed; 13 comments) **LANE B2 25 Sept 2026: test 1 MASC anneal da/de/en on Pelling's transcription: no legible decode; da score inside an erratic da control range (0-74% letters right): not informative.** | nobody found spec: specs/copenhagen-1835.json |
| 12 | 29 | Pollaky cryptograms (4 ads) | 1865-1875 | en | 4 short ads, one number code | scans on post 29; not on disk | open; two more possibly solved by Ernst **LANE B2 25 Sept 2026: test 1 images + one pass: ads 3-4 IC 0.064/0.066 with English 0.059-0.066, above random 0.039-0.046: transposition signature; but ads 3-4 (8 and 20 May 1875, ad 3 naming Catokwacopa) are the Catokwacopa ads of rank 13 (partial: mechanism agreed in print, Bosbach, Estes, Ernst), so this is not a new lead; B2 orchestrator correction 17:55.** **Test 2 (B2, 25 Sept): pass B 97.5% agreement; ads 3-4 match the Ernst/Bourdeau Catokwacopa text 72/72 letters.** | Kesselman (biography), Gaffney spec: specs/pollaky-1865-1875.json |
| 13 | 8 | Catokwacopa ads, Evening Standard | 8 and 20 May 1875 | en | two long ads, invented words | `ciphers/catokwacopa-1875/` | **partial** (check-solved 23 Sept 2026: Bosbach, Estes, Ernst, Krajcovic readings since 2018) | on our queue (rank 18) spec: specs/catokwacopa-1875.json |
| 14 | 35 | T. E. Wood's survival-test cryptogram | 1950 | multi | 21 letters, Thouless method, non-English key book | on disk in post 35 | open; Thouless's own passages all solved (see unranked) **LANE B2 25 Sept 2026: test 1 Gillogly dictionary attack, 4 key texts (French Bible, Vulgate, French and German novels): best 12-16/21 vs control true offset ranked 1st every seed at 19-20/21: negative for these texts.** | nobody found spec: specs/te-wood-1950.json |
| 15 | 50 | Cylob cryptogram (London bookshop booklet) | c.1995 | ? | 20 pages of grids, 24 symbols (reader Torsten) | Cylob's scans (Schmeh 2015; Futility Closet Apr 2026); not on disk | open **LANE B3 25 Sept 2026 (bCYL): test 1 fetched post 50 to sources/schmeh/posts/; the form is rectangles with geometric patterns, no letters or numbers (Schmeh); the '24 symbols (reader Torsten)' in this row was not found in post 50 -- to be re-sourced; 11 of 20 page images embedded; lead: a partial transcription at cloud.rotering-net.de, unfetched. No control applies to a fetch.** | nobody; Bourdeau: not settleable spec: specs/cylob-c1995.json |
| 16 | 12 | Scorpion letters S1, S5 (America's Most Wanted) | 1991 | en | Zodiac-style homophonic, 2 of 5 published | Oranchak's site; not on disk | open; hoax risk (Aymeloglu SHORTLIST) **LANE B2 25 Sept 2026: test 1 images + one pass: S1 N=70 K=53 IC 0.0083 vs English 0.066 / random-at-K 0.019 (homophonic-scale); S5 counted only (N=179).** | Oranchak, Pelling; claimed solutions 2018 unverified spec: specs/scorpion-1991.json |
| 17 | 10 | Ricky McCormick's notes | 1999 | en? | 2 notes, ~30 lines, "NCBE" repeats | FBI 2011 release; Schmeh's transcription on disk (post 10) | open (FBI Nov 2025) **LANE B2 25 Sept 2026: test 1 token profile: IC 0.089 and 3-6-gram coverage above English, vowel-dropped English and shuffled controls at every n; vowel share 0.245 between prose and vowel-dropped: heavy token reuse, no decipherment.** **Test 2 (B2, 25 Sept): family_run masc on English and vowel-dropped English, controls 0.994/0.985, target judge FAIL both: simple substitution excluded.** **Test 3 (B3 bMCC3, 25 Sept): family_run homophonic K=24: English control 0.998 vs target FAIL (-1.48); vowel-dropped control 0.652 (one seed 0.058) vs FAIL (-2.33); the target's own letters shuffled score the same (-1.81 to -1.90): the anneal cannot tell the target from its own shuffle, so both substitution families are excluded at this fold; next: the token/nomenclator test (spec test 3). NEAR row kept.** **Test 4 (B3 bMCC4, 25 Sept): token/nomenclator anneal: control 0.8 pct vs gate 0.5 -- not a test; code-word family still untested.** | FBI CRRU, ACA failed spec: specs/mccormick-1999.json |
| 18 | 9 | Rubin cryptogram (Philadelphia) | 1953 | en/nulls | one slip: words "Dulles", "Conant", 0/1/x lines | Bauer's reproduction; image only | open **LANE B2 25 Sept 2026: intake gate exit 0 (open); test 1 image + one pass: letter passages N=305 IC 0.0612 vs English 0.062 / random 0.039: English-like (moved; next: family_run masc with an N=305 control).** **Test 2 (B3 bRUB2, 25 Sept): family_run masc on the letter passages: control 0.989 (0.974-0.997) vs target judge FAIL; again without DULLES/CONANT (N=293): control 0.974 vs FAIL: simple substitution of English excluded on this single-pass transcription.** | Bauer spec: specs/rubin-1953.json |
| 19 | 31 | MLH cryptogram (Israel to California) | c.1976 | symbols/rebus | one strip, mixed symbols | ACA Cryptogram Jan-Feb 1976 cover; image only | open (Schroedel asked ACA: nothing new) **LANE B2 25 Sept 2026: intake gate exit 0 (open); test 1 image + one pass: N=33 K=26 IC 0.0189 vs English 0.062 / random 0.039: too short to inform; line 1 may read MLH => 7 symbols (possible crib).** | nobody spec: specs/mlh-1976.json |
| 20 | 44 | Bullet cryptogram, Tuscany | 13 Aug 1944 | en (Allied field cipher) | 44 letters + QM / 605YZ/FF | on disk in post 44 | open; a forum "solution" without a method, rejected by Schmeh **LANE B2 25 Sept 2026: test 1: the rejected forum solution cannot be produced by any Vigenere/Beaufort/variant/MASC key (44 vs 39 letters; MASC 37-39 of 39 violations) where the same script recovers every control key; claim closed with a control.** **Test 2 (B3 bBUL2, 25 Sept): Caesar control 1.000 vs target FAIL; 93 keys from QM/MQ/605YZ/FF x three tabulae: true key ranks 1 in 3/3 controls, target 0/93 PASS with max 1/12 cribs, same as random text: excluded. Periodic keys 2-8: control 5-6 pct, below the 0.6 gate: not a test at N=44 (partial, NEAR row).** **LANE B4 25 Sept (bBUL3): indicator lookup in print: header best fits M-209 (TM 11-380 example) in form only, the digits break it; FM 24-5, Slidex no fit; control 2/2 known headers; no solver test licensed at N=44 -- parked pending new material.** | nobody spec: specs/bullet-tuscany-1944.json |
| 21 | 24 | Erba murder letter | 2006 | it | one letter | not fetched | open **LANE B3 25 Sept 2026 (bERB): intake open; test 1 image re-transcription agrees 93.0 pct (106/114 digraphs) with the comment-thread transcription; 8 me/ne ambiguities (M), possibly a 9th base token.** | nobody spec: specs/erba-2006.json |
| 22 | 25 | SS radio message to Lippert | 1944 | de | 6 lines with = / : separators | Gessler collection; image only | open; **Bourdeau: probable forgery** (typography, rank abbreviations) **LANE B3 25 Sept 2026 (bSSR): intake open; image transcribed (one pass): N=37 letters, K=18, IC 0.0631 inside both the German (0.047-0.107) and uniform (0.042-0.075) controls: too short to discriminate.** | nobody spec: specs/ss-radio-lippert-1944.json |
| 23 | 43 | Rayburn cryptogram | 2004-06 | en | ~80 keyboard characters, each struck | Schneier 2006; image only | open; plausibly a password/directory list (Bourdeau, Schneier's readers) **LANE B3 25 Sept 2026 (bRAY): test 1 (image + one blind pass): N=74 K=59, IC 0.0056 vs English control 0.0618 (0.031-0.091) and uniform-at-K 0.0171 (0.012-0.026): below both, near-hapax as Schmeh notes; not decisive between a diagram/list and a homophonic cipher; test 2 (layout) next.** | nobody spec: specs/rayburn-2004.json |
| 24 | 41 | Blitz ciphers | found "1940s", published 2011 | ? | 3 of 8 pages published | Pelling's site; not on disk | open; suspected modern hoax **LANE B3 25 Sept 2026 (bBLZ): test 1 on 2 pages (N=581): case-folded IC 0.0628 inside the monoalphabetic-English control (0.059-0.071), above homophonic 0.042 and Vigenere 0.040; periodic scan flat where the control finds its period. Inconclusive; masc is the next test.** **LANE B4 25 Sept (bBLZ2): test 2 family_run masc, en judge wired: control 0.994 vs target judge FAIL (-1.685 vs -0.858): simple substitution of English excluded; letter profile chi2 6270 vs English, not a transposition. NEAR row; next homophonic K=48 case-sensitive / German masc (awaits parent).** **B4 25 Sept (bBLZ3): homophonic K=48 case-sensitive (control 0.971 vs FAIL) and masc German (0.956 vs FAIL; judge on de16, mismatch) excluded; next the six-page fetch.** | Pelling spec: specs/blitz-ciphers.json |
| 25 | 49 | Chinese gold bars, Shanghai | 1933 (alleged) | ? | 16 lines, 260 letters | on disk in post 49 (IACR page) | open publicly; **Bourdeau 15 Sept 2026: letter counts flat, no real text** **LANE B3 25 Sept 2026 (bGLD): letter chi-squared 1.25 vs 1000 uniform draws mean 24.9 (min 8.2): flatter than every random draw, independent re-run of Bourdeau's 15 Sept result; no natural-language substitution text underneath. NOTES line 1 set to `open` by LANE B4 (25 Sept, parent ruling): no decipherment exists, Bourdeau's no-real-text determination cited as prior work.** | nobody spec: specs/goldbar-1933.json |
| 26 | 21 | YOG'TZE (Guenther Stoll) | Oct 1984 | de | 6 characters | on disk | open; below any unicity **LANE B3 25 Sept 2026 (bYOG): initials search: phrase counts 12 (de) / 18 (en) vs random-string controls 337-1879 / 57-825, below every control; no phrase proposed. Bourdeau's top50 notes say Hagen police closed the case April 2025 (uncited, to check).** | nobody spec: specs/yogtze-1984.json |
| 27 | 38 | Sufi fiddle inscription | ? | ? | unidentified script | no published transcription | open; provenance rests on a novel's afterword (Bourdeau) **LANE B4 25 Sept (bSUF): test 1: image is a hand copy from Bulliet's novel ('copied by V. Castle Winter'), not the violin; one blind pass N=165 K=21; script checklist puts it in the Arabic-script family (RTL, cursive joining, dot diacritics), not Baybayin; references from memory, no fetch.** **B4 25 Sept (bSUF3): read as Arabic script: no Sufi formula or coherent line in five languages; one group near baraka(t), M.** | nobody spec: specs/sufi-fiddle.json |
| 28 | 11 | Untersberg code | legend | ? | one alleged sheet | none | open; legend, no primary source **LANE B3 25 Sept 2026 (bUNT): abbreviation-shape test: 36 period-closed short tokens vs control 12.0 (5-20) from the target's own unigrams, 100th percentile: the text is shaped like scribal abbreviation (NEAR row).** **LANE B4 25 Sept (bUNT2): abbreviation expander: control 0.321 vs gate 0.30 but shuffled floor 0.289 (weak); target no reading, judge FAIL (circular). Next: the Hs. 2398 image/catalogue entry.** **B4 25 Sept (bUNT4/bUNT5): primary source Salzburg Museum Hs 2398 (1690-1710), printed in Herzog 1929 p.28 with eleven witnesses (Hs 12 plain Latin); Hs 12 alignment at chance.** | nobody spec: specs/untersberg-code.json (25 Sept 2026: a real primary source, Salzburg Museum Hs. 2398, and transcription found -- this row's wording may be stale, see spec) |
| 29 | 36 | Fair Game end-credits letters | 2010 | en | yellow letters in credits | film | open; may not be a code **LANE B3 25 Sept 2026 (bFAI): Halpin next-letter hypothesis on the Mulliss credit-context transcription: judge FAIL -2.20 inside the random-marking band (-2.13 to -2.26); planted-name control 3/3: negative for this reconstruction.** | nobody spec: specs/fair-game-2010.json |
| 30 | 33 | Censorship-manual steganograms | WW2 | en | two pictures | manual scans | open **LANE B4 25 Sept 2026 (bCEN): cheap test 1 done -- manual PDF and both mystery images fetched (ciphers/censorship-manual-stego/images/), manual's own captions read and quoted with page numbers; found dbourdeau/cyphersolver already ran a full attempt 15 Sept 2026, blocked on image resolution for both mysteries (their own TNA re-fetch confirmed pixel-identical, no gain). Next test (2/3) should not repeat a plain mark-detector.** | nobody spec: specs/censorship-manual-stego.json |
| 31 | 37 | Shugborough inscription | 1748-56 | la/en | O U O S V A V V / D M, 10 letters | on disk (Wikipedia) | open; Hall staff "wary" of all solutions | many amateurs; no spec (B4 triage: no mechanical, script-checkable test found for a 10-letter initialism) |
| 32 | 2 | Zodiac Z13 and Z32 | 1970 | en | 13 and 32 symbols | Oranchak's transcriptions; Z13 in `ciphers/zodiac-z13-stress/` | open; **Z340 solved 5 Dec 2020** (Oranchak, Blake, Van Eycke); our 24 Sept 2026 stress test closes the ARTHUR LA mechanism | Oranchak; FBI; no spec (B4 triage: the one on-record Z13 mechanism already control-tested closed-negative 24 Sept 2026; no other named untried test for Z13 or Z32) |
| 33 | 4 | Kryptos K4 | 1990 | en | 97 letters, cribs EASTNORTHEAST, BERLINCLOCK | public | open cryptanalytically; **plaintext found in Sanborn's papers Sept 2025** (Kobek, Byrne, Smithsonian AAA), sold at auction 20 Nov 2025, held privately, Paradigm vets guesses (2026) | everyone; no spec (B4 triage: plaintext already found, cryptanalysis moot) |
| 34 | 40 | Beale cryptograms | 1885 pamphlet | en | B1 520, B3 618 numbers | public | open; hoax per Schmeh, Bourdeau | treasure hunters; no spec (B4 triage: no untried cheap test named anywhere in the repo) |
| 35 | 6 | Rohonc Codex | 16th-19th c. | code | 448 pages | public scans | **partial**: Kiraly and Tokai, Cryptologia 42:4 (2018), a code system, "likely never completely broken" | Kiraly, Tokai; no spec (B4 triage: needs Hungarian and years per the survey, not a cheap test) |
| 36 | 14 | Codex Seraphinianus | 1981 | asemic | book | public | not a cipher by the author's statement | nobody; no spec (B4 triage: not a cipher, author's own statement) |
| 37 | 1 | Voynich manuscript | 15th c. | ? | 240 pages | Beinecke scans | open; Bourdeau: not a cipher of a European language | everyone; no spec (B4 triage: no untried cheap test named; Bourdeau's adjudication repeated in QUEUE.md) |
| 38 | 20 | WW2 pigeon message (Bletchingley) | 1944? | en | 27 five-letter groups | on disk in post 20 | open; GCHQ: one-time pad, unbreakable without the pad | GCHQ, Bletchley Park; no spec (B4 triage: GCHQ's own OTP assessment, no cheap test can move a one-time pad) |
| 39 | 13 | Double Column Transposition "reloaded" challenge | 2013 | en | artificial | MysteryTwister | open | Lasry and others; no spec (B4 triage: QUEUE.md dropped table -- artificial compute challenge, not a historical-document target, out of project scope) |
| 40 | 45 | Schmeh's 65-bit world-record challenge | 2010 | n/a | 65-bit key | Cipherbrain | open (Jan 2022 still) | compute projects; no spec (B4 triage: pure compute/key-search challenge, not a $3 cheap test) |
| 41 | 42 | Bonus 22 (M-209 series) | 2014 | en | machine cipher | Bouchaudy's challenge site | open (no solve found) | Lasry's method exists; no spec (B4 triage: no m209 tool or ciphertext on disk in this repo; implementing a ciphertext-only M-209 attack is campaign-scale, not a breadth-lane test) |
| n/a | 34 | Unsolved nomenclators | 16th-18th c. | fr/es/it/la | many | Tomokiyo's list = `CATALOG.md` | our main lane; not ranked here | Lasry, Biermann, Bosbach, Brown, Bourdeau, Aymeloglu, us |
| solved | 48 | Rivest's LCS35 time-lock puzzle | 1999 | n/a | | | **solved 15 Apr 2019** by Bernard Fabrot (3.5 years CPU); Cryptophage FPGA weeks later; successor CSAIL2019 runs to 2034 | |
| solved | 46 | ADFGVX, Childs corpus | Nov 1918 | de | 22 messages posted as a challenge Feb 2017 | Lasry-Schmeh challenge | keys published (Lasry, Niebel, Kopal, Wacker, Cryptologia 41:2, 2017); Bourdeau: the unread residue is transmission garble (found-solved); a Sept 2026 "GPT-6 Astra" claim on one message is unverified press | |
| solved | 32 | Silk dress cryptogram | 1888 | en (code) | 23 lines of words | | **solved 2023** by Wayne Chan (Univ. of Manitoba), Cryptologia 48:5: US Signal Service weather code, Bismarck ND, 27 May 1888 | |
| solved | 28 | Urquhart's Cyphral Distich and Octastich | 1652-53 | en | 64 and 285 numbers | printed books | **solved 31 Aug 2026** (Vals AI, Geby Jaff, Claude Fable 5.1): number i indexes a word in section/page i of the host text; nine letters of the Octastich pending a physical copy; `LESSONS.md` | Vals AI |
| solved | 27 | Ferdinand III to Leopold Wilhelm | 1640 | de/la/it | numbers + geometric symbols | Auer 2014, Schmeh 2017 | **solved 15 Sept 2017** by Thomas Ernst (stroke counts, AEIOU homophones, "Piccolominea" crib; datensicherheit.de 12 Oct 2017); the related Cardinal-Infante letters R1889/R1890 read by Aymeloglu Sept 2026, R1887 open (`CATALOG.md`) | |
| solved | 17 | Roosevelt cryptogram | Apr 1935 | en | letters + number block | Friedman Legacy | second part read by Friedman (DID YOU EVER BITE A LEMON); **number block explained 16 Sept 2026 by Bourdeau**: a permutation of 1-52 padded with zeros, not a cipher | |
| solved | 15 | Rilke cryptogram | 1942 | de | 18,760 characters in 4-groups | Schmeh's scans | **probably solved**: keyboard mashing on a German QWERTZ typewriter (Schmeh, Schroedel; Foxon, Cryptologia 47:6, 2022); Schmeh removed it from his list | |
| solved | 35 | Thouless's survival-test passages | 1948-49 | en | 74 letters (B) | | Passage I solved 1948 (Playfair SURPRISE); **Passage C solved 1995** (Gillogly, BLACK BEAUTY); **Passage B (II) solved 2019** by Richard Bean (key text: Francis Thompson, "The Hound of Heaven"; 37,000 Gutenberg books ranked by decrypt letter frequency). Only Wood 1950 (rank 14) remains | |
| joke | 39 | "Riverbanks Ripper" | | | one character | | Schmeh's post is dated **1 April 2017**: a one-letter "cryptogram" (Caesar on a single letter is a perfect cipher). Not a target | |

## Approach per item (the cheap test, its control, its cost, its model)

**1. Köhler cryptograms (no. 47).** Kahn's five 1944 messages from Walter Koehler, the Dutch Abwehr agent the FBI
was running as a double agent, sent to Paris outside FBI control (Schmeh's 2021 update after D. A. Johnson). Cheap test
1 run today: the pooled index of coincidence is 0.0399 against 0.072 for German and 0.065 for English windows of the
same lengths and 0.0385 for random letters (`specs/cheap-tests/koehler_ic.out`), so this is not a transposition of
German or English; the letter distribution is weakly non-uniform (chi-square 58.7 on 25 df), which is what a short
periodic key or a book cipher with letter arithmetic leaves behind. Next, in order: periodic IC for a period 2-30
(under $1, Sonnet); an archive route that could end the item as found-solved (TNA KV 2 double-agent files on Koehler
and HW 19 ISOS decrypts of Abwehr Paris traffic, from Kahn's 1981 footnote; FBI Vault "Walter Koehler"), $3-5 Sonnet;
then, only if a period shows, a Vigenère-family hill-climb in German, Dutch and English judged by
`tools/judge_plaintext.py`, with a German plaintext of 924 letters under a random key of that period as the matched
control. Highest expected value on the list: real historical text, a documented sender, nobody working on it, first
tests under $1. A transcription caveat for the record: Kahn's third message is headed 137 but has 140 letters as
printed on Cipherbrain.

*Gold-lane ladder for Köhler (25 Sept 2026).* Test 2 (periodic IC and Kasiski, period 2-30, LANE B bKOE) was run with
both controls and reads flat: not a fixed-period Vigenère family; consistent with a one-time key, a running key on a
book text, or a code with letter arithmetic. The families, in the order the lane runs them, each with its control
before the target: **A recovery** (TNA Discovery API: KV 2 on Koehler, HW 19 ISOS for Abwehr Paris, Feb 1944; FBI
Vault; Kahn's 1981 footnote); **B running key** on a Dutch or German natural-language key text (the FBI-run channel used
a Dutch prayer book, so the Paris channel plausibly used a book too; a running key leaves exactly the flat, weakly
non-uniform distribution seen), attacked by two-stream n-gram decoding in which plaintext and key must both read as
language, crib-dragging of high-frequency German and Dutch words, then key-text identification against Gutenberg Dutch
and German texts; the control is German plaintext of the five message lengths under a Dutch book running key, same
solver, and the period scan is extended to 31-120 in passing; **C book or word-sum code** (Thouless-type, Bean 2019
ranking of candidate key texts), only after B is logged; **D one-time key**, which no statistic falsifies: if B and C
fail while their controls read, the item is parked as "consistent with a one-time key" and only A remains.

*Gold lane, 25 Sept 2026 18:25 UTC:* family A (archive) found no decrypt at TNA; FBI HQ file RG 65 105-9673 located, unopened (ASKS 55). Family B standard-tableau running key parked: control 60-79 pct recovered, target at one-time-key noise (GOLD-2A), agreeing with Bourdeau's 15 Sept unigram exclusion. Next: keyed-tableau running key (GOLD-2C).

**2. Debosnys (no. 3).** Four cryptograms in a simple invented alphabet by a French-speaking, educated prisoner who
also left clear-text poems in the same papers. The cheap test is the form test of the Urquhart lesson: transcribe (two
Sonnet passes from Schmeh's or Farnsworth's images, $4), count lines and signs, and compare the cryptograms' line
structure with his clear poems; a cryptogram with the shape of a poem he also wrote in clear has a full crib. Then a
homophonic/MASC anneal in French, English, Portuguese and Latin with a control at each cryptogram's N and K ($4, Sonnet;
strongest model to read the output against his biography). Value high (Schmeh's no. 3, few prior attempts, a museum
that holds his papers and could be asked for a key sheet). Ciphertext not yet on disk.

*Gold-lane ladder for Debosnys (25 Sept 2026).* Moved from LANE B2 to LANE GOLD. Test 1 as specified (four images
once, two blind passes, reconcile, counts, IC per cryptogram), then the form test against his clear poems, then a
19th-century French corpus (`tools/data/fr19`, Gutenberg prose, before any judging: fr16 is not matched) and the
anneal in fr, en, pt and la with a control at each cryptogram's N and K; the strongest model reads outputs against his
biography; an ASKS row for the Adirondack History Center Museum's clear-text poems and any key sheet.

**3. Somerton code (no. 5).** Not a cipher by consensus (Abbott's group: word initials), so the only cheap test is
host-text-as-key: the letters were written inside a FitzGerald Rubaiyat. Cheap test 3 run today
(`specs/cheap-tests/somerton_rubaiyat.out`): against the word-initial sequence of Gutenberg #246 (first and fifth
editions with FitzGerald's preface), line 5 carries a 7-letter run, TSAMSTG, equal to the initials of "the Son, and
Malik Shah the Grandson" in FitzGerald's preface; the flanking letters do not continue the match. Control: 1000 random
five-line sets from the English initial-letter distribution reach a run of 5 in 335 sets, 6 in 25, 7 or more in none.
That is a search result on a preface passage, not a reading (a 7-of-13 partial match, and the lost 1941 Whitcombe &
Tombs edition may not print the preface). Next: establish the 1941 edition's contents ($2, Sonnet) and search Webb's own
texts if any are published. Any candidate sentence is judged only by the initials check. Value: fame, not verifiability.

**4. Moustier altars (no. 18).** Altar inscriptions are formulaic (dedication, donor, date, invocation), which makes
a crib-driven MASC the cheap test once a transcription exists: two image fetches, two Sonnet passes, reconcile ($3);
then Latin-first, French-second annealing with dedication cribs fixed, a Latin dedication text of the same N and K as
control ($2). If the symbol count is far above 26, the question becomes a lodge or pigpen-family script and needs the
strongest model for one shape comparison ($2). Few prior attempts on record (Connart, Pelling).

**5. Kaliningrad bottle post (no. 19).** A 37-sign Latin-letter text with apostrophes and diacritics, IC about 0.054
(Schmeh's readers), Soviet-era provenance. The readers argued languages for 58 comments; no machine run across the
candidates is on record. Cheap test: get the transcription from the Russian thread ($2), then a MASC anneal with the
apostrophe treated both as a modifier and as a sign, in transliterated Russian first (IC closest), then Polish,
Lithuanian, German, each with a matched control at the same N and K ($4, Sonnet); a periodic-IC pass if all are flat.

**6. Cigarette case (no. 7).** 47 signs, a German Christmas dedication of 1909, the shape of a plain substitution
that the veteran readers could not break. Cheap test: German MASC anneal with the dedication crib list tried as fixed
hypotheses, judged in German, with a German control at N=47, K=18 ($2, Sonnet). At that length the control itself will
read only partly, which bounds what a negative means; the second test (a word-length-pattern search over German
Christmas and Bible verse, $1) is the host-text variant for a quotation.

**7. Powers dedication (no. 22).** Before any test, rule 1: J. T. Thomas's article, whose title claims a
decipherment, must be read (403 from the cloud; an owner-machine row). If it does not settle the matter, the cheap tests
are structural: 32 triplets against the 32 Goldberg movements and the novel's chapter list, and against the
acknowledgements as initials ($2, Sonnet; control: random triplets from the initial-letter distribution of names). A
living author makes N0/N1 likely.

**8. Dorabella (no. 26).** Wase (2025) has the matched-control negative on file for a monoalphabetic substitution of
English or Latin, so the cheap tests are the ones nobody has published: an index rule (each symbol as a number under
the four natural encodings, indexed into the words of the letter it was enclosed with, printed in Dora Powell's 1937
memoir), the 1920s notebook key applied and scored as phonetic English, and the musical reading against the Dorabella
variation's incipit; each with random 87-symbol strings as control, $2 each, Sonnet. Low prior after 129 years; ranked
here only because the tests are cheap and self-judging.

**9. Lima 1916 (no. 16).** Cheap test 2 run today (`specs/cheap-tests/lima/`): substitution annealing on the 71 cipher
letters gives letter-salad (best score -159) while matched English controls at N=71, K=21 read 60.6, 70.4 and 74.6
percent of letters right with the same solver and seeds. So the cipher words do not behave as a monoalphabetic
substitution of English, conditional on a newspaper transcription that exists in two variants. Next: grep the words in
the commercial telegraph codes on the Internet Archive ($1), a typewriter-shift and short-key Vigenère pass ($1). Low
value.

**10. Harry-Caroline and Tissie-Jabber (no. 30).** Harry+Caroline is 71 letters with word boundaries and three
single-letter words (a or I under a MASC): a joint MASC with those fixed and a control of the same word-length pattern
($1, Sonnet), then the lovers' convention of the other's name as a periodic key ($1). Tissie-Jabber is an enumeration
over d, o, n, a-d whose reply lists exactly the forms the first ad omits; report the structure, expect no prose.

**11. Copenhagen (no. 23).** Briere's analysis says simple substitution; the language is the question (Danish, German,
English). Transcribe from the scan ($1), anneal in the three with controls ($2, Sonnet). Cheap, but nothing is known
about the note's date or purpose, so the value is low.

**12. Pollaky (no. 29) and 13. Catokwacopa (no. 8).** Two of the four Pollaky ads are dated 8 and 20 May 1875, the
dates of the two Catokwacopa ads in the Evening Standard. A one-hour documentary check ($1): are they the same ads, or
does the same page carry both? If Pollaky's number code and the Catokwacopa vocabulary share a source, Ernst's
diplomatic-line-numbering reading (`ciphers/catokwacopa-1875/NOTES.md`) gains a key. Catokwacopa itself is partial
(check-solved 23 Sept 2026) and already on our queue.

**14. Wood 1950 (no. 35).** 21 letters under Thouless's word-sum method with an unnamed non-English key book: below
unicity for any search; Bean's 2019 method (rank Gutenberg texts by decrypt letter frequency) is the only cheap test
and needs the key language guessed. $2 Sonnet, low probability.

**15-19. Cylob, Scorpion, McCormick, Rubin, MLH.** Modern, no known plaintext language, heavy prior effort by the FBI
or by Oranchak's tools where a cipher exists. Cylob's 24 symbols and grids invite one cheap test: a symbol-frequency
profile from the published pages against a flat distribution (as Bourdeau did for the gold bars), $1 Sonnet, which
decides "text or pattern" before anyone transcribes 20 pages. Scorpion S1/S5: our homophonic annealer with a matched
control, $3, only after Oranchak's published negatives are read. McCormick, Rubin, MLH: none cheap; McCormick's
repeated NCBE and parenthesised groups have been through the FBI's unit; MLH is a rebus in an image; Rubin's slip is
a nulls hypothesis with no lever.

**20-24. Bullet, Erba, SS radio, Rayburn, Blitz.** The bullet cryptogram has 44 letters with a J in a digraph
position, which excludes standard Playfair in one glance, and is far below what an M-209 ciphertext-only attack
needs; none cheap. Erba: modern Italian true crime, not fetched. SS radio: Bourdeau's forgery assessment (typography
and rank abbreviations) should be checked before any spend; if it holds, closed. Rayburn: a password list. Blitz:
suspected hoax; a symbol-frequency profile ($1) is the only test worth running.

**25-30. Chinese gold bars, YOG'TZE, Sufi fiddle, Untersberg, Fair Game, censorship manual.** Gold bars: Bourdeau's
flat letter counts (15 Sept 2026) already answer the cheap test. YOG'TZE: six characters. Sufi fiddle: no
transcription, provenance in a novel's afterword. Untersberg: a legend. Fair Game: may not be a code. Censorship
manual: two pictures, steganography, no lever.

**31-37. Shugborough, Zodiac Z13/Z32, Kryptos K4, Beale, Rohonc, Codex Seraphinianus, Voynich.** The bottom by rule:
decades of effort, heavy compute, and for Kryptos the plaintext now exists privately (Kobek, 2025; auction Nov 2025;
Paradigm vets guesses in 2026). Specific untried cheap tests: none for Kryptos, Beale, Voynich, Seraphinianus. Zodiac
Z13: our stress test of 24 Sept 2026 (`ciphers/zodiac-z13-stress/`) closed one mechanism with a random-string control;
the item is below unicity. Shugborough: ten letters, an initialism; nothing mechanical decides between readings.
Rohonc: Kiraly and Tokai's code-system reading is the state of the art and needs Hungarian and years, not a cheap test.

**38-41. Pigeon, DCT reloaded, world record, Bonus 22.** The pigeon message is a one-time pad per GCHQ. The other three
are artificial compute challenges, outside a historical-cipher project.

**Solved or explained since Schmeh's posts (do not re-solve):** LCS35 (Fabrot 2019), ADFGVX Childs corpus (Lasry et
al. 2017; residue is garble), silk dress (Chan 2023), Urquhart (Vals AI 2026), Ferdinand III 1640 letter (Ernst 2017),
Roosevelt number block (Bourdeau 2026), Rilke (Foxon 2022, keyboard mashing), Thouless B (Bean 2019), and the
Riverbanks Ripper (April Fools' 2017). Nine of Schmeh's fifty, plus Z340 and two of Thouless's three, are off the list.

## What this survey did not do

No attack campaign was run. Three tests under $2 each were run with their controls and are reported as numbers, not
as readings. Dunin's page was not read. Twenty-three of Schmeh's item posts were not fetched (request budget); their
rows rest on the index page, the search checks and `QUEUE.md`. Ciphertexts for ranks 2, 4, 5 and 11 are not on disk.

## Credit

Klaus Schmeh (Cipherbrain, the Top 50 list and every item post cited), Elonka Dunin (the famous-codes list, not
reachable today), Satoshi Tomokiyo (Cryptiana, the nomenclator list behind `CATALOG.md`), Daniel Bourdeau
(cyphersolver's assessments of the famous items, CC BY 4.0 text, as carried in `QUEUE.md`), Andrew Aymeloglu
(unsolved-ciphers, the Ferdinand III R1889/R1890 readings and the Scorpion hoax-risk note), Geby Jaff and Vals AI
(the Urquhart solve and the host-text lesson), Richard Bean (Thouless 2019), Thomas Ernst (Ferdinand III 2017),
Wayne Chan (silk dress 2023), David Oranchak, Sam Blake and Jarl Van Eycke (Z340 2020), Floe Foxon (Rilke 2022),
David Kahn (the Köhler messages, 1981), Tony Gaffney (the Agony Column ads), Craig Bauer (Unsolved!, 2017).
