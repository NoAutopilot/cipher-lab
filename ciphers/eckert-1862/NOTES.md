# Eckert Papers, 1862 "Ciphers Sent" ledger (Huntington mssEC 15)

status: partial
War of the Rebellion ser. I vol. 7 (IA warofrebellionco0007vari, `_djvu.txt` full text) grepped by this worker (GF-A2-10, 3 Oct 2026): p. 624 prints T8, Lincoln to Halleck 16 Feb 1862, in clear ("In the midst of a bombardment at Fort Donelson, why could not a gunboat run up"); the ledger's other entries stay coded in every source checked below.
checked: 19 Sept 2026
target: QUEUE.md rank 1, "Thomas T. Eckert Papers, US Military Telegraph: ledgers of telegrams sent 'still in
code', 1862-67 (Huntington mssEC 1-76)". This folder is the pilot on one ledger, mssEC 15 (1 Feb-21 July 1862).

## 1. Is it already decoded? (CLAUDE.md rule 1, checked 19 Sept 2026)

**Transcribed yes, decoded no.** The Zooniverse project "Decoding the Civil War" (Huntington Library, Zooniverse,
North Carolina State University, Abraham Lincoln Presidential Library and Museum; NHPRC grant) ran from 21 June
2016. Its blog post "Phase 1 Transcription Complete! Huzzah! Huzzah! Huzzah!" (15 Nov 2017,
https://decodingthecivilwar.wordpress.com/) reports all 12,921 pages of the 35 ledgers transcribed by about 4,600
volunteers. Phase 2 (tagging sender, recipient, date, code words inside each telegram, announced 28 Sept 2017,
"Decoding the Civil War: Phase 2, Two Work Flows, Your Choice") "ran into significant technical difficulties";
the closing post "Decoding the Civil War: End" (31 July 2019,
https://decodingthecivilwar.wordpress.com/2019/07/31/decoding-the-civil-war-end/) says the project was paused
in Jan 2018 and shut in July 2019, and that the team would instead "extract through text mining the data
required" from the Phase 1 transcriptions. No systematic decoding was published by the project (single entries were read on its blog in 2017; see ciphers/eckert-1864/AUDIT.md section 12). The Zooniverse
results page (https://www.zooniverse.org/projects/zooniverse/decoding-the-civil-war/about/results, read
19 Sept 2026) says the project is complete and that the transcriptions were published in the Huntington
Digital Library, Thomas T. Eckert Papers, four series: 1 US Military Telegraph ledgers mssEC 01-21, 2 Army of
the Potomac and Fort Monroe ledgers mssEC 22-25, 3 Eckert letterpress books mssEC 26-33, 4 Charles A. Dana
ledgers mssEC 34-35.

What is online (checked 19 Sept 2026): collection p16003coll11 at hdl.huntington.org holds 67 objects: the 35
ledgers mssEC 01-35 (all with "Transcription text provided by the volunteers of Decoding the Civil War
(2016-2017)" in the catalogue note; every page image carries the volunteer transcription in the "text" field of
`/digital/api/collections/p16003coll11/items/<pointer>/false`) and 32 cipher-related books mssEC 36-67. The
transcriptions reproduce the code words as written; nothing on the item pages is decoded. The 1865-67 volumes
(mssEC 12-14, 18, 20-21, 32-33) are in the same state.

Tomokiyo (sources/cryptiana/web/civilwar1.htm, snapshot) uses the Huntington images of the cipher books
(mssEC 37-67) and the NHPRC proposal, and gives a concordance of which printed cipher each book is (No. 1:
mssEC 39, 41-46; No. 2: 47-48; No. 5: 49-66; No. 9: 67; Dept of the Gulf: 38; manuscript codes: 37, 40). He
does not discuss the ledgers, and his unsolved list does not name them; civilwar0.htm says only that Eckert's
papers "are today beginning to be made available online". The Milroy telegrams (civilwar1b_milroy.htm) are
Cipher No. 7 and were solved by Richard Bean with Claude Opus 5 in 2026.

Other sweeps: search engine (queries on "Decoding the Civil War" results, dataset, decoded), 19 Sept 2026, found
only the project pages above and press of 2016-17; github.com/dbourdeau/cyphersolver README (19 Sept 2026) lists
the Milroy telegrams (found solved) and nothing on Eckert; github.com/aaymeloglu/unsolved-ciphers README has no
Civil War telegraph item; DECODE (de-crypt.org) has no web search path reachable from here (the record-list URL
returns 404) and is not expected to hold American telegraph material; no printed "Lettres" apply. NHPRC proposal
pdf (archives.gov/files/nhprc/announcement/literacy-transcribing.pdf) fetched, not used.

Verdict on the queue entry: "found-transcribed", not found-solved. The coded entries remain coded everywhere
they are published, so the target is open; the pilot below shows how far the residue can be read.

## 2. Material pulled (19 Sept 2026)

- mssEC 15, "War Department Ciphers Sent Feby. 1 to July 21, 1862", object 5126, 172 page images (5165 x 7200 px
  masters), about 306 telegrams on pages [5]-[163]. All 172 page texts harvested from the API (not committed:
  128 KB of volunteer transcription, their credit; re-fetch with the URL pattern in images/manifest.json).
  Ten pages saved at 2583 px in images/.
- mssEC 01, "War Department Ciphers Received Feby. 2 to July 30, 1862", object 6796: page texts harvested to
  check address conventions ("Andes Ocean" = McClellan, Washington) and time words. Not committed.
- Cipher books: mssEC 67 (object 1750, the printed template, Tomokiyo: No. 9) all 37 pages viewed, 7 saved;
  mssEC 41 (No. 1) TIME page saved; mssEC 40, 37, 39, 38 opening pages viewed (post-war and 1864-65 codes,
  not the 1862 key). **mssEC 36 named in the queue as "the cipher book" is not one**: it is Stager's 1865-67
  "Memoranda giving location ... of cipher keys", a ledger of which key was held where.
- Rights: images/README.md. Public-domain government records; the Huntington asks for a citation.

## 3. What the ledger is, and what the key is (key.md)

The entries are dictionary-coded plaintext: the sender's text with names and sensitive words replaced by
"arbitrary" code words, a coded signature, a time word and filler. No route transposition is recorded (that was
done on the wire), so the "still in code" residue is a code-word problem, not a transposition problem. The code
words are the printed words of Stager's template booklet (H: mssEC 67), and their Feb 1862 meanings match those
Plum printed for Cipher No. 7 (Alvord = Buell, Camden = Thomas, Rapture = Louisville, Ocean = Washington). No
digitised book carries the 1862 meanings. The meanings were therefore recovered from known plaintext: the
Official Records print most of the War Department's western telegrams of Feb 1862 in clear (OR ser. I vol. 7,
Internet Archive warofrebellionco0007vari; vol. 8, warofrebellionco08unit). key.md section 3 gives 63 code words
(55 arbitraries and 8 time words) with grades: 31 C, 19 I, 13 M. The entries to the eastern line (Lander, Banks, Rosecrans, Fort Monroe) use
some words with other meanings (Humboldt, Devon), so at least two keys were in use at Washington.

Prior art (added by the verifier, 24 Sept 2026, AUDIT.md section 1): the Decoding the Civil War blog had already
published Andes = McClellan, Alden = Halleck (30 Mar 2017) and Alvord = Buell (18 May 2017) from 1862 ledger
entries, and stated the same method, comparing ledger telegrams with the Official Records to reverse-engineer the
missing books. Its 21 Apr 2017 post gives Anthon = McDowell and Palate = bridge for an April 1862 entry, against
this table's grade-I Anthon = Banks and Palate = Cairo (not adjudicated).

## 4. The ten readings (ciphertext.txt, reading.md, decode.py)

Ten entries of 5-21 Feb 1862 (McClellan, Stanton and Lincoln to Halleck, Buell, Hunter and Lane, Scott),
chosen because the Official Records print them. Two independent transcription passes by subagents from the
page images, reconciled against the image with the volunteer transcription as third witness (reading.md,
"Reconciliation": 14 disagreements, none on the sense, three on code words, all resolved). Result: all ten read
cleanly and agree with the printed text apart from clerical variants and two sense variants in T10 ("reach" for
"make", "Railway to Clarksville" for "railroad to Nashville"; AUDIT.md section 3, corrected 24 Sept 2026); 86 code-word tokens graded C,
3 I, 2 M, 0 H. `python3 decode.py --check` regenerates the readings from ciphertext.txt and key.md and exits 1
if reading.md is stale. Per CLAUDE.md rule 4 this is a known-plaintext result, not an H reading.

Novelty (AUDIT.md, verifier, 24 Sept 2026): all ten are **N1**; every plaintext is in the Official Records
(1882-83) and most in the Lincoln or McClellan editions too. What the folder adds is the alignment, the graded key
table, the hour of T7 (16 Feb, 1 PM; OR "[February 16 (?)]") and the T10 variants.

## 5. Residue and what would move it

- The value is not in the ten (the OR already prints them) but in the entries the OR does not print, and in
  the time words, which the OR usually drops: with the key the ledger dates every telegram to the half hour.
- mssEC 15 alone: roughly 300 entries; about 60 distinct code words seen in the first 60 pages, 31 fixed by known
  plaintext. Extending the vocabulary needs (a) more OR matches (vols. 5, 9, 11 pt 3, 12 pt 3, 51 pt 1 are
  downloaded in the session scratch, not committed), (b) the received ledgers mssEC 01-03, where incoming
  telegrams sometimes appear with the code words resolved, (c) a copy of Cipher No. 7 (the Milroy solve gives
  the route side; Plum p. 47 and ASA p. 58 print one example; the Friedman Collection copies at the Marshall
  Foundation are of Nos. 1, 2, 4, 5, 9, 12, not 7).
- The 1863-67 ledgers (mssEC 16-21, 26-33) are in Ciphers No. 12, 9, 1, 2, 4, 5, all of which the Huntington
  holds as filled-in books (Tomokiyo's concordance): those volumes can be read at grade H, entry by entry, with
  the tools of this folder (decode.py substitutes from a table; the transposition, when a ledger records
  transposed text, is the route on the book's pages 1-8). That is the proper next pilot: one 1864 sent ledger
  (mssEC 18 or 19) against mssEC 41-46 (Cipher No. 1).
- Not done here: no negative was claimed, so no control was needed (rule 3).

## 6. Failure log

- 19 Sept 2026: the queue's "EC 36" is not a cipher book (see section 2); 25 minutes lost identifying which
  book, if any, covered Feb 1862. None does.
- 19 Sept 2026: hdl.huntington.org page-level records do not expose the transcription through the old
  dmwebservices API (no `transc` field); it is the `text` field of the newer `/digital/api/collections/...`
  endpoint. huntington.org pages return 429 to WebFetch and sit behind a Vercel browser check for curl; the
  rights page was read through the Wayback Machine.
- 19 Sept 2026: OR volume 5 (Lander, Banks) does not print the eastern-line telegrams of 2-6 Feb 1862, so the
  Romney/Cumberland/Frederick words stay at grade I/M.

## 7. Credits and sources

- Images and transcriptions: Thomas T. Eckert Papers, The Huntington Library, San Marino, California;
  volunteer transcriptions by Decoding the Civil War (2016-2017), NHPRC-funded.
- Cipher identification: S. Tomokiyo, Cryptiana, "Union Codes and Ciphers during the Civil War"
  (civilwar1.htm) and "Stager Cipher No. 7 Continued in Use after Abandonment" (civilwar1b_milroy.htm);
  W. R. Plum, The Military Telegraph during the Civil War (1882) as quoted there; Richard Bean's Milroy solve
  (2026); D. Bourdeau, cyphersolver/milroy (MIT, CC BY 4.0), consulted for the No. 7 route.
- Known plaintext: The War of the Rebellion, ser. I, vols. 7 and 8 (Internet Archive full texts).
- Prior key words and method: Decoding the Civil War blog (Huntington), "Grant's 'Former Bad Habits'"
  (30 Mar 2017) and "Bickering Generals" (Olga Tsapina, 18 May 2017), decodingthecivilwar.wordpress.com.
- Follow-up suggestion (verifier, 24 Sept 2026, not done): the reading.md summary sentence "the only variants are
  clerical" should be corrected by the solver lane to name the T10 variants (AUDIT.md section 3).

## Web and blog check (GF-A2-10, 3 Oct 2026)

Plain web searches (WebSearch, 3 Oct 2026):
1. `Eckert telegrams 1862 "ciphers sent" ledger decoded code words McClellan Halleck` -- OAC finding aid
   (ark:/13030/c86m3964), Huntington collection pages, Seth Kaller sale page (482). Finding aid: "the sent messages
   are ciphered; the received telegrams are mostly decoded". No decoded edition of the sent ledgers.
2. `"mssEC 15" Huntington Eckert cipher telegram ledger` -- the same finding-aid and Huntington item pages, a
   wcgs.org 2016 announcement. Nothing decoding mssEC 15.
3. `"Decoding the Civil War" Eckert telegrams decoded 2025 OR 2026 Claude OR GPT solves` (model-solve family) --
   Huntington Verso/Frontiers posts, Smithsonian 2016, Zooniverse project, openhistoryhub.com thread 63889 (opened:
   2016 announcement and one reply "This is such a neat project", nothing decoded). No model-solve announcement.
4. Descriptive title: covered by 1-2 (folder title "Eckert Papers, 1862 Ciphers Sent ledger").
Blog site searches:
- Cipherbrain (`site:scienceblogs.de klausis-krypto-kolumne Civil War telegram Eckert Union cipher`): returned the
  blog's tag page /tag/civil-war/ (opened 3 Oct 2026: posts on a Pitman letter 2018/03/17, a cipher tool 2018/04/15,
  "who can decipher this civil-war-era code" 2018/04/17, a Confederate cipher cover 2018/12/20; zero mentions of
  Eckert, Huntington or ledger on the tag page). The 2018/04/17 post and its comments opened: no mention of Eckert,
  Huntington, ledger, telegraph or Stager.
- Cryptiana blog (`site:cryptiana.blogspot.com Eckert OR Stager telegram cipher Civil War`): no blog page returned.
  Tomokiyo's site pages (civilwar0/1/1b, local snapshot) were read for section 1 above: they cover the cipher books
  and the Milroy (No. 7) telegrams, not the 1862 sent ledgers.
- Cipher Mysteries (`site:ciphermysteries.com Eckert telegrams Civil War ledgers`): no ciphermysteries.com page
  returned.
No comment thread found that decodes an mssEC 15 entry. The project's own blog (decodingthecivilwar.wordpress.com)
did read single 1862 entries in 2017 (section 3 "Prior art" and AUDIT.md); that is already logged.

## Premise check (GF-A2-10, 3 Oct 2026)

(a) Folder's own mentions -- found, already handled: the Decoding the Civil War blog's 2017 single-entry readings
(Andes, Alden, Alvord, Anthon, Palate; section 3 and AUDIT.md); the received ledgers mssEC 01-03 "where incoming
telegrams sometimes appear with the code words resolved" (section 5) -- a source of resolved code words, not a
decipherment of the sent entries. Nothing in the folder names a decipherment of the mssEC 15 residue.
(b) Other solvers' working files -- not found. Shallow clones 3 Oct 2026: dbourdeau/cyphersolver (HEAD 2341682)
mentions Eckert only in its copies of Tomokiyo's unsolved list (`unsolved.htm`, `targets/napoleon/unsolved.txt`:
"In 2016, the project 'Decoding the Civil War' started to transcribe and decipher about 16,000 telegrams"); its
`milroy` work is Cipher No. 7 telegrams, not the ledgers. aaymeloglu/unsolved-ciphers (HEAD d2800bb): no Eckert,
mssEC or Civil War telegraph file (cited, not copied).
(c) Physical neighbours -- not found as a decipherment: mssEC 01 (received, Feb-July 1862) was harvested on
19 Sept and used only for address conventions; it is the received side, decoded, of other telegrams. No clear copy of
the sent entries is bound in mssEC 15 (172 page texts harvested 19 Sept). Pages not re-viewed this pass.
(d) Recipient's side -- found for the ten, as already logged: OR ser. I vols. 7-8 print the ten entries (p. 624
re-checked this pass), and the AUDIT.md verifier lists the Lincoln Collected Works, Sears' McClellan and
Nicolay-Hay. Recipient-side papers for the unprinted residue (Halleck's, Buell's received telegrams; Papers of U. S.
Grant vol. 4 for Feb 1862) were not searched this pass; next: grep Papers of U. S. Grant vol. 4 and OR vols. 9-12
for the residue's dates, ~USD 1.5. [Grant vol. 4 half done 3 Oct 2026, GAPS110 below: no hit; OR vols. 9-12 remain.]
Not found-solved: the residue (about 296 entries) is not decoded in any source checked.

## GAPS110-eckert-1862 (3 Oct 2026, account-4)

Step run: the Premise check (d) next step, its first half -- Papers of Ulysses S. Grant vol. 4 (ed. Simon, 1972;
covers 8 Jan-31 Mar 1862). Internet Archive item `papersofulyssess0004gran` (lending-only: `inlibrary`,
`printdisabled`), so `_djvu.txt` is not served; searched with be-api full-text search
(`be-api.us.archive.org/fts/v1/search?q=...&identifier=papersofulyssess0004gran`), 1.6 s apart, script-collected
snippets only (be-api returns at most 5 highlight snippets per query and no real page number, per CLAUDE.md
access item 3, so this is a presence/absence search, not a page-cited one).
- Positive control: "unconditional and immediate surrender" (USG to Buckner, 16 Feb 1862) -> 1 hit, snippet
  "No terms except an unconditional and immediate surrender can be accepted". The route reads this volume.
- No hit (0 snippets): Eckert; Stager; "Ciphers Sent"; "Lincoln to"; "Lincoln to USG"; "Stanton to USG";
  "Scott to USG"; the ledger's code words Alden, Alvord, Andes, Saffron, Shylock, Lonesome, Torrent, Sermon,
  Merlin, Bangor, Bengal, Applause; T2's phrase "congratulate you upon the result".
- Hits, read, none an mssEC 15 entry: "cipher" (5) and "cypher" (1) are all editorial source lines for Halleck's
  own books ("Telegrams Sent in Cipher by Gen. Halleck", RG 393, Dept. of the Mo.) and one received telegram
  ("operator will send to me in cypher if you desire it"); "McClellan to USG" (1) is 13 Jan 1862, before the
  ledger opens (1 Feb); "Stanton to" (1) is Lincoln directing Stanton about Buell; "Thomas A. Scott" (5) are Scott's
  own letters and telegrams from the West to Stanton and Foote (received side for Washington, not sent);
  "War Department", the three Feb dates and "Dispatch received" return Grant-side material in the snippets seen.
- Result: Papers of U. S. Grant vol. 4 prints no War Department telegram of Feb-Mar 1862 to Grant in the snippets
  returned and none of the ledger's code words; it adds no known plaintext for the residue. The one lead it gives is
  a different source: Halleck's own "Telegrams Sent in Cipher" books (NARA RG 393, Dept. of the Missouri) --
  recorded, not pursued (brief scope). Limit: with 5 snippets per query, a date query cannot list every telegram
  of that date; the negative is conditional on the query set above.
- Requests: archive.org advancedsearch 1, be-api.us.archive.org 40. No vision, no subagents.

## GAPS113-eckert-1862 (3 Oct 2026, account-4)

Step run: the Verdict's cheapest step -- grep OR ser. I vols. 9-12 (IA full text) for the mssEC 15 residue. Script:
`print/or_match.py` (word 5-grams shared between each ledger page's volunteer transcription and each OR volume's
`_djvu.txt`; a 5-gram occurring more than 8 times across the volumes is a formula and ignored; a page/volume pair is
reported at >= 6 distinct 5-grams in one 400-word block). Output: `print/or_matches.tsv` (pointer, page title, ledger
head line, IA volume, OR page from the running head, gram count, 45 words of OR context). Inputs not committed: the
172 page texts (re-harvested 3 Oct 2026 from the CONTENTdm `text` field, 171 fetched, the front cover failed; 161 carry
text) and the OR text (re-fetch from the IA identifiers below).
- Volumes: ser. I vol. 9 `warofrebellion09secrrich`; vol. 10 pts 1-2 `1warofrebellion10secrrich`,
  `2warofrebellion10secrrich`; vol. 11 pts 1-3 `1/2/3warofrebellion11secrrich`; vol. 12 pts 1-3
  `1/2/3warofrebellion12secrrich`; plus vol. 7 `warofrebellionco0007vari` as the positive control.
- Positive control (same script, same threshold): of the nine known telegrams printed in vol. 7 (T1-T4, T6-T10; T5 is
  vol. 8, not fetched), all nine are found, with 12-88 shared 5-grams, and the OR page from the running head agrees with
  reading.md for T1 584, T2 591, T3 593, T6 608, T7 626, T8 624 (T4 938 vs 937, a page-break offset). Null side: vol. 7
  against ledger pages after March 1862 (which vol. 7 cannot print) shares at most 3 5-grams; the threshold of 6 sits
  above that.
- Found: 101 of the 161 ledger pages with text share >= 6 5-grams with a printed telegram in vol. 7 or vols. 9-12.
  Vols. 9-12 alone: 69 pages (pointers 5010-5118, 21 Feb-21 July 1862): vol. 9 3 pages, vol. 10 pt 1 2, pt 2 5,
  vol. 11 pt 1 8, pt 3 33, vol. 12 pt 1 13, pt 3 27 (a page can match more than one volume, e.g. a telegram the OR
  prints twice). Examples: 5049 (13 Mar 1862, "Andes Irving having considered the plan of operations", OR vol. 11 pt 3,
  the President's directions to McClellan); 5082-5083 (16 June, "For Arctic Your dispatch of yesterday reminding me
  of a supposed understanding", Lincoln to Fremont, vol. 12 pt 1); 5117 (July, "Let him sieze guides in the country",
  vol. 12 pt 3). Vol. 7 also matches 32 pages (4963-5037), 23 more than the ten read in section 4.
- Not found (below 6 5-grams in every volume): 60 of the 161 text pages. A page match means at least one entry on the
  page is printed, not every entry on it; the unmatched entries are the residue that stays without known plaintext.
- What this means (rule 10 wording): for the matched entries the plaintext is already in print (Official Records,
  1882-85); the folder would add the code-word alignment and the ledger's time words, as for the ten. No reading or
  key change was made in this step; key.md, reading.md and decode.py are untouched.
- Requests: hdl.huntington.org 173 (one object record + 172 page texts, 1.6 s apart, one empty reply on the front
  cover); archive.org 13 (3 advancedsearch, 10 `_djvu.txt`). No vision, no subagents.

## GAPS118-eckert-1862 (3 Oct 2026, account-4)

Step run: the Verdict's cheapest step -- align the 33 ledger pages that GAPS113 matched to OR ser. I vol. 11 pt 3
(`3warofrebellion11secrrich`) to the printed text and fix the code words they carry. Script: `print/or_align.py`
(entries cut at blank lines, anchored by rare word 5-grams, word-level difflib alignment against the print window; a
1-word ledger token replaced by 1-3 printed words, not a spelling variant or abbreviation, is a candidate; printed
forms normalised for OCR, rank words and possessives). `tools/interlinear_align.py` was not used: it aligns cipher
groups to letters of a plain line, while here both sides are words and most are identical, so a word diff fits.
Outputs: `print/align11p3/align_pairs.tsv` (111 candidate occurrences), `proposals.tsv` (50 ledger words),
`heldout.tsv`. Inputs re-fetched (not on disk in this container, not committed): the 33 page texts and the vol. 11 pt 3
`_djvu.txt`.
- Aligned: 50 entries on 33 pages = 41 distinct telegrams (entries whose print windows overlap are one telegram; the
  ledger copies a few twice, e.g. 5073/5074).
- Held-out (rule fixed in the script docstring before scoring): fit on the even telegram groups (27 entries), test on
  the odd (23): 38 fit words, test 30/31 occurrences give the fit meaning (0.968). Shuffled-pairing control (test
  entries aligned to another matched telegram's print window, 200 derangements): mean 0.05 hits, p95 0. Known answer:
  of the 11 key.md C/I words the alignment sees, Andes = McClellan (5 telegrams), Irving = Lincoln, Ocean = Washington
  and wayworn = army agree.
- key.md: 13 rows added, grade C, each seen in >= 2 distinct telegrams with one printed meaning and no rival:
  Arctic = Fremont, Genoa = Washington, humming = Richmond, Indus = Fredericksburg, Jasper = Winchester, Juno =
  Gordonsville, panther = advance, princess = artillery, rampant/rampants = the enemy, robin = division, wedding =
  transportation, welsh = reinforcements. `python3 decode.py --check` exits 0 (the ten Feb readings use none of them).
- Conflicts with key.md, logged not merged (rule 4: a data conflict, witnesses by date): Anthon/Anthons = McDowell in
  3 telegrams (5058 Apr, 5069 May, 5110 July; OR 11.3 p.117, 202, 326) against key.md Anthon = Banks (I, Feb, p.[11]),
  agreeing with the Decoding the Civil War blog's 21 Apr 2017 Anthon = McDowell; Alden = Banks once (5110, 17 July,
  Pope to McClellan, "Culpepper is occupied ... with Alden Sigel & one robin of Anthon", OR p.326 "Banks, Sigel, and one
  division of McDowell") against Alden = Halleck (C, Feb); Arno = Halleck in 2 telegrams (5096, 5099, 3-4 July; p.291,
  294) against Arno = Rosecrans (M); Lather = James (River) in 3 telegrams (5091, 5093, 5110; p.269, 270, 326) against
  Lather = Michigan (C, Feb, OR 7 p.593). These are a later key or keys on the eastern line from spring 1862, as
  section 3 already suspected (Humboldt, Devon); key.md's single table keeps the Feb values and decode.py is unchanged.
  Single-telegram pairs (Alvord = Wool, Shylock = fall back, Palate = bridges, Pastor = battle, Jargon =
  Charlottesville, Ingot = Lynchburg, Kettle = Newport News, Dawn = Fort Monroe, Eagle = Fort Monroe, Persian = army,
  quadrant = cavalry, Segments = gunboats, Tarquin = movement, Offal = Richmond, ...) stay in proposals.tsv as 'single'.
- Rule 10: every telegram aligned here is already printed (Official Records ser. I vol. 11 pt 3, 1884): N1 shape. What
  the alignment adds is the code-word table for the spring-summer 1862 key, not new plaintext.
- Requests: hdl.huntington.org 34 (33 page texts, one empty reply retried); archive.org 1 (`_djvu.txt`). No vision,
  no subagents.

## GAPS122-eckert-1862 (3 Oct 2026, account-4)

Step run: GAPS118's Verdict -- the same `print/or_align.py` (unchanged) on the ledger pages GAPS113 matched to OR ser. I
vol. 12 pt 3 (`3warofrebellion12secrrich`, 27 pages) and pt 1 (`1warofrebellion12secrrich`, 13 pages; 36 distinct
pointers, some pages match both). Outputs `print/align12p3/`, `print/align12p1/` (align_pairs, proposals, heldout).
Inputs re-fetched, not committed.
- vol. 12 pt 3: 35 entries on 27 pages = 29 telegrams, 98 candidate occurrences, 52 ledger words. Held-out (even/odd
  telegram groups, rule as in the script): 35 fit words, test 26/26 = 1.000; shuffled-pairing control (200
  derangements) mean 0.15 hits, p95 0. Known-answer: 17 key.md C/I words seen.
- vol. 12 pt 1: 19 entries on 13 pages = 13 telegrams, 27 occurrences, 16 words. Held-out test 2/2 (too few scored
  to mean much on its own); control mean 0.00, p95 0. Known answer: whistle = enemy, Merlin = Virginia, Arctic =
  Fremont, Opal = Winchester, panther = advance agree.
- Pooled across 11.3/12.3/12.1 (a telegram counted once per ledger entry: 5073.0 aligns in both 11.3 and 12.3 and is
  one telegram). OCR splits ("gor dons ville", "eichmond", "in fantry", "tranportation", "mc clellan") are agreements,
  not conflicts, read by eye against the proposals.
- key.md: 8 rows added at grade C (>= 2 distinct telegrams, one printed meaning, no rival): Danube = McDowell, Ingot =
  Lynchburg, Jargon = Charlottesville (5 telegrams), Offal = Richmond, Quack = Sigel, quadrant = cavalry (4+),
  tambour = infantry, wafer = regiment. widow M "(troops sent, reinforcements?)" -> C reinforcements (5095 and 5079,
  OR 11.3 p.286, 12.1 p.659). Held (rival in the print): Stanhope = flank 2 / "the Shenandoah" 1; Vulcan = railroad 2
  / headquarters 1. `python3 decode.py --check` exits 0 (the ten Feb readings use none of the changed rows).
- Conflicts with key.md, logged not merged (rule 4; witnesses: ledger pointer, date, OR page):
  Camden = Banks (5060 May, OR 12.3 p.125; 5097 June-July, p.453) vs Camden = Thomas (C, Feb, OR 7 p.624, 646);
  Virtue = artillery (5099, 5100, OR 12.3 p.453-454) vs Virtue = Frederick (I, Feb); Palate = bridges (5058 Apr, OR
  11.3 p.117; 5116-5117 July, 12.3 p.491) vs Palate = Cairo (I, Feb); wedding = battle (5079, Lincoln to Fremont
  12-13 June 1862, "the gallant battle of last Sunday", "while a battle is pending at Richmond", OR 12.1 p.34, 659) vs
  wedding = transportation (C, 5073, 5090, June, McClellan's line, OR 11.3 p.217, 260) -- two values in the same month
  on two lines, so neither is overwritten; Arno = Banks (5079-5080, 13 June, Lincoln to Fremont, OR 12.1 p.659) vs
  Arno = Halleck (5096, 5099, 5112; July, OR 11.3 p.291, 294, 12.3 p.487) vs Arno = Rosecrans (M, Feb); Alden =
  Banks now in 2 telegrams (5110, 5112; 17 July and after, OR 11.3 p.326, 12.3 p.486-487) vs Alden = Halleck (C, Feb);
  Lather = James River 2 more (5109, 5116, OR 12.3 p.476, 491) vs Michigan (C, Feb). whistle = enemy is confirmed by
  print in June (5065-5067, 5080; OR 12.1 p.635, 647, 659); its Feb grade stays I. The pattern holds: by summer 1862
  the eastern lines used one or more later tables that reuse Feb words for other names, so key.md needs a dated
  column before these words are read in spring-summer entries.
- Rule 10: every telegram aligned is already printed (OR ser. I vol. 12, 1885): N1 shape. What this adds is code-word
  values for the spring-summer 1862 tables, not new plaintext.
- Requests: hdl.huntington.org 36 (page texts); archive.org 3 (two `_djvu.txt`, one connection reset retried once).
  No vision, no subagents.

## Remaining gaps (finish-or-blocker pass, 3 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries (about 3%), all ten N1 (section 4, AUDIT.md)
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; OR print step done 3 Oct 2026 (GAPS113): 101 of 161 text pages match OR vols. 7 or 9-12; vols. 11 pt 3 and 12 pt 3/pt 1 aligned 3 Oct 2026 (GAPS118, GAPS122: 21 code words added at C, held-out 30/31 and 26/26 vs controls 0.05 and 0.15 hits); next: decode the unmatched spring-summer entries with the enlarged table once key.md carries a dated column (gap 2), and align the vol. 9/10/11 pt 1 matches (18 pages), ~$3
- residue code words not fixed by any known plaintext - blocker: open-codes; 31 Feb words fixed (section 5) plus 21 spring-summer words (GAPS118, GAPS122); later eastern-line tables reuse Feb words for other values (Anthon, Alden, Arno, Lather, Camden, Virtue, Palate; wedding has two values in June on two lines) -- next: add a dated key column (period/line) to key.md and decode.py so a word is read by the table of its date, ~$2
- 1863-67 sent ledgers at grade H - blocker: not-attempted; filled-in cipher books exist at the Huntington (section 5); next: pilot one 1864 sent ledger (mssEC 18 or 19) against mssEC 41-46 (Cipher No. 1), ~$6

## Escalation (3 Oct 2026)
- [ ] siblings: received ledgers mssEC 01-03 may show code words resolved (section 5 (b)); not yet read for that
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [ ] known-keys: no filled-in book for Feb 1862 (failure log); the 1863-67 books are the H route (gap 3)
- [x] print: OR vols. 7-8 done (ten matches); Papers of U. S. Grant vol. 4 done 3 Oct 2026, no hit; OR vols. 9-12 grepped 3 Oct 2026 (GAPS113): 69 ledger pages matched there, 32 in vol. 7 (101 of 161); vols. 8 and 51 pt 1 not fetched
- [ ] key-rebuild: vol. 11 pt 3 done (GAPS118, 13 words); vol. 12 pt 3/pt 1 done (GAPS122, 8 words + widow to C, 7 conflicts logged); vols. 9, 10, 11 pt 1 alignments and a dated key column next (gaps 1-2)
- [n/a] image-check: the ten readings were reconciled against the image (reading.md, Reconciliation)
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 3 internal gaps; cheapest next: add a dated (period/line) key column to key.md and decode.py so the spring-summer values (Camden, Arno, Alden, Lather, wedding ...) do not collide with Feb, then decode the unmatched spring-summer entries, ~$2
