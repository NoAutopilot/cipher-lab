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
| 5 | 19 | Kaliningrad (Baltiysk) bottle post | Soviet era, found 2015 | ru-latin/pl/lt/de | 2 sheets, 37 signs incl. apostrophes, IC 0.054 | Cipherbrain post 19 images; Russian blog transcription; not on disk | open (58 comments, no solution) **LANE B2 25 Sept 2026: test 1 Ernst transcript matches both images 26/26 lines; N=978 K=36 IC 0.0657 vs transliterated Russian 0.056 / German 0.072: not informative; ciphertext on disk (ciphers/kaliningrad-2015/).** | nobody found |
| 6 | 7 | Cigarette-case dedication, Thuringia | 24 Dec 1909 | de/la | 4 lines, 47 signs, ~18 distinct | owner's transcription on disk (`specs/cigaret-case-1909.json`) | open (Schmeh 2018); **LANE B 24 Sept 2026: German MASC anneal FAIL on judge, but control reads only 4-22% at N=45, K=18 (spec's 47 re-parsed to 45): uninformative, not a negative** | Schmeh's readers (Krauss, Biermann, Gaffney, Bosbach) failed |
| 7 | 22 | Powers cryptogram (dedication, The Gold Bug Variations) | 1991 | en/initials | 32 triplets, 3 unknown letters | on disk (`specs/powers-1991.json`) | open per Schmeh 2017; **print check pending**: J. T. Thomas, "Deciphering the code in Richard Powers's The Gold Bug Variations" (article title claims a decipherment; cloud gets 403) **LANE B2 25 Sept 2026: test 1 print check: no decipherment found in the open indexes; initials hypothesis in print since Herman and Lernout 1998; Thomas 2006 full text queued (LOCAL-QUEUE L15).** | Bourdeau: "not settleable by cryptanalysis" |
| 8 | 26 | Dorabella cipher (Elgar to Dora Penny) | 14 Jul 1897 | en/phonetic/music | 87 symbols, 24 = 3 arcs x 8 orientations, lines 29/31/27 | Schmeh's letter transcription on disk (`specs/dorabella-1897.json`); image at Elgar Birthplace | open; Wase, Cryptologia 49:1 (2025): not a MASC of English or Latin; claims by Sams 1970, Henderson 2011, Packwood 2020, Belanger 2025-26, none accepted **LANE B2 25 Sept 2026: test 1 blocked: the July 1897 covering letter is not in the open Powell 1937 copy; lending-only copy, ASKS row 50.** | Cipher Mysteries thread; Bourdeau: famous list |
| 9 | 16 | Lima, Ohio robbery cryptogram | 27 Jun 1916 | en/code | 71 cipher letters in 17 words + 6 clear words | two newspaper transcriptions on disk (`specs/lima-1916.json`); no manuscript | open (Schmeh 2017; Pelling 2013); **our cheap test 2: negative vs matched controls** **LANE B2 25 Sept 2026: test 1 codebook grep (ABC, Western Union, Lieber, Bentley) target 2/2/1/3 of 17 vs random-string 2/1/1/3, positive control 17/17: at chance, negative.** | Bourdeau: odds low |
| 10 | 30 | Harry-Caroline (1863) and Tissie-Jabber (1901) ads | 1863; 1901 | en | 44 + 27 letters; 13 + 9 four-letter groups over d o n a b c | on disk (`specs/harry-caroline-1863.json`), from Gaffney's Agony Column | open (Schmeh 2017) **LANE B2 25 Sept 2026: test 1 MASC with word breaks judge FAIL (-1.442) vs control 16-34% letters right at N=74: control too weak, uninformative; test 2 (name-keyed Vigenère) is next if wanted.** | Gaffney |
| 11 | 23 | Copenhagen cryptogram (behind an 1835 painting) | post-war note | da/de/en | one sheet, letters; Briere: simple substitution | Cipherbrain post 23 scan (Ramliden); not on disk | open (ACA failed; 13 comments) | nobody found spec: specs/copenhagen-1835.json |
| 12 | 29 | Pollaky cryptograms (4 ads) | 1865-1875 | en | 4 short ads, one number code | scans on post 29; not on disk | open; two more possibly solved by Ernst | Kesselman (biography), Gaffney spec: specs/pollaky-1865-1875.json |
| 13 | 8 | Catokwacopa ads, Evening Standard | 8 and 20 May 1875 | en | two long ads, invented words | `ciphers/catokwacopa-1875/` | **partial** (check-solved 23 Sept 2026: Bosbach, Estes, Ernst, Krajcovic readings since 2018) | on our queue (rank 18) spec: specs/catokwacopa-1875.json |
| 14 | 35 | T. E. Wood's survival-test cryptogram | 1950 | multi | 21 letters, Thouless method, non-English key book | on disk in post 35 | open; Thouless's own passages all solved (see unranked) | nobody found spec: specs/te-wood-1950.json |
| 15 | 50 | Cylob cryptogram (London bookshop booklet) | c.1995 | ? | 20 pages of grids, 24 symbols (reader Torsten) | Cylob's scans (Schmeh 2015; Futility Closet Apr 2026); not on disk | open | nobody; Bourdeau: not settleable spec: specs/cylob-c1995.json |
| 16 | 12 | Scorpion letters S1, S5 (America's Most Wanted) | 1991 | en | Zodiac-style homophonic, 2 of 5 published | Oranchak's site; not on disk | open; hoax risk (Aymeloglu SHORTLIST) | Oranchak, Pelling; claimed solutions 2018 unverified spec: specs/scorpion-1991.json |
| 17 | 10 | Ricky McCormick's notes | 1999 | en? | 2 notes, ~30 lines, "NCBE" repeats | FBI 2011 release; Schmeh's transcription on disk (post 10) | open (FBI Nov 2025) | FBI CRRU, ACA failed spec: specs/mccormick-1999.json |
| 18 | 9 | Rubin cryptogram (Philadelphia) | 1953 | en/nulls | one slip: words "Dulles", "Conant", 0/1/x lines | Bauer's reproduction; image only | open | Bauer spec: specs/rubin-1953.json |
| 19 | 31 | MLH cryptogram (Israel to California) | c.1976 | symbols/rebus | one strip, mixed symbols | ACA Cryptogram Jan-Feb 1976 cover; image only | open (Schroedel asked ACA: nothing new) | nobody spec: specs/mlh-1976.json |
| 20 | 44 | Bullet cryptogram, Tuscany | 13 Aug 1944 | en (Allied field cipher) | 44 letters + QM / 605YZ/FF | on disk in post 44 | open; a forum "solution" without a method, rejected by Schmeh | nobody spec: specs/bullet-tuscany-1944.json |
| 21 | 24 | Erba murder letter | 2006 | it | one letter | not fetched | open | nobody |
| 22 | 25 | SS radio message to Lippert | 1944 | de | 6 lines with = / : separators | Gessler collection; image only | open; **Bourdeau: probable forgery** (typography, rank abbreviations) | nobody |
| 23 | 43 | Rayburn cryptogram | 2004-06 | en | ~80 keyboard characters, each struck | Schneier 2006; image only | open; plausibly a password/directory list (Bourdeau, Schneier's readers) | nobody |
| 24 | 41 | Blitz ciphers | found "1940s", published 2011 | ? | 3 of 8 pages published | Pelling's site; not on disk | open; suspected modern hoax | Pelling |
| 25 | 49 | Chinese gold bars, Shanghai | 1933 (alleged) | ? | 16 lines, 260 letters | on disk in post 49 (IACR page) | open publicly; **Bourdeau 15 Sept 2026: letter counts flat, no real text** | nobody |
| 26 | 21 | YOG'TZE (Guenther Stoll) | Oct 1984 | de | 6 characters | on disk | open; below any unicity | nobody |
| 27 | 38 | Sufi fiddle inscription | ? | ? | unidentified script | no published transcription | open; provenance rests on a novel's afterword (Bourdeau) | nobody |
| 28 | 11 | Untersberg code | legend | ? | one alleged sheet | none | open; legend, no primary source | nobody |
| 29 | 36 | Fair Game end-credits letters | 2010 | en | yellow letters in credits | film | open; may not be a code | nobody |
| 30 | 33 | Censorship-manual steganograms | WW2 | en | two pictures | manual scans | open | nobody |
| 31 | 37 | Shugborough inscription | 1748-56 | la/en | O U O S V A V V / D M, 10 letters | on disk (Wikipedia) | open; Hall staff "wary" of all solutions | many amateurs |
| 32 | 2 | Zodiac Z13 and Z32 | 1970 | en | 13 and 32 symbols | Oranchak's transcriptions; Z13 in `ciphers/zodiac-z13-stress/` | open; **Z340 solved 5 Dec 2020** (Oranchak, Blake, Van Eycke); our 24 Sept 2026 stress test closes the ARTHUR LA mechanism | Oranchak; FBI |
| 33 | 4 | Kryptos K4 | 1990 | en | 97 letters, cribs EASTNORTHEAST, BERLINCLOCK | public | open cryptanalytically; **plaintext found in Sanborn's papers Sept 2025** (Kobek, Byrne, Smithsonian AAA), sold at auction 20 Nov 2025, held privately, Paradigm vets guesses (2026) | everyone |
| 34 | 40 | Beale cryptograms | 1885 pamphlet | en | B1 520, B3 618 numbers | public | open; hoax per Schmeh, Bourdeau | treasure hunters |
| 35 | 6 | Rohonc Codex | 16th-19th c. | code | 448 pages | public scans | **partial**: Kiraly and Tokai, Cryptologia 42:4 (2018), a code system, "likely never completely broken" | Kiraly, Tokai |
| 36 | 14 | Codex Seraphinianus | 1981 | asemic | book | public | not a cipher by the author's statement | nobody |
| 37 | 1 | Voynich manuscript | 15th c. | ? | 240 pages | Beinecke scans | open; Bourdeau: not a cipher of a European language | everyone |
| 38 | 20 | WW2 pigeon message (Bletchingley) | 1944? | en | 27 five-letter groups | on disk in post 20 | open; GCHQ: one-time pad, unbreakable without the pad | GCHQ, Bletchley Park |
| 39 | 13 | Double Column Transposition "reloaded" challenge | 2013 | en | artificial | MysteryTwister | open | Lasry and others |
| 40 | 45 | Schmeh's 65-bit world-record challenge | 2010 | n/a | 65-bit key | Cipherbrain | open (Jan 2022 still) | compute projects |
| 41 | 42 | Bonus 22 (M-209 series) | 2014 | en | machine cipher | Bouchaudy's challenge site | open (no solve found) | Lasry's method exists |
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
