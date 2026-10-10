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
this table's grade-I Anthon = Banks and Palate = Cairo (not adjudicated). (3 Oct 2026, GAPS161: the Feb Anthon = Banks
inference is withdrawn; Anthon = Rosecrans on 6 Feb by print, McDowell in Apr-Jul, both C; see the GAPS161 section.)

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

## GAPS127-eckert-1862 (3 Oct 2026, account-4)

Step run: GAPS122's Verdict -- a dated key column. `print/key_dates.py` (new) gives every key.md row its witness date
range (first and last ledger date of the telegrams supporting it: the ten entries, cited ledger pages and pointers, OR 7
page matches through `print/or_matches.tsv`, and the OR 11-12 alignments in `print/align*/align_pairs.tsv`; a pointer
is dated from its own ledger head, an undated one by the dated pointers on either side) and writes it into a new fourth
column; `--check` exits 1 when stale. key.md: 84 rows dated plus 13 rows for the later values of conflicting words
(97 rows). decode.py now reads each word by the row whose range covers the entry's ledger date (header date), grades
it M outside every range or where two values cover the date (rule 4), and has `--at DATE WORD...` for a lookup.
`python3 decode.py --check` exits 0 and the ten Feb readings are unchanged (C 86, I 3, M 2): every Feb row's range
covers its own entries. Disk only; no requests, no vision, no subagents.
- Conflicting words: 10 (Anthon, Alden, Arno, Lather, Camden, Virtue, Palate, wedding, Stanhope, Vulcan).
- Separate cleanly by date, 8: Anthon Banks 6 Feb / McDowell 6 Apr-17 Jul (C, 3 telegrams); Alden Halleck 5-21 Feb /
  Banks 17-20 Jul (C, 2); Arno Banks 9-16 Jun (M, 1 telegram, Fremont line) / Halleck 3-20 Jul (C, 3), the Feb value
  Rosecrans (M) undated (received ledger mssEC 01 p.14, no date on disk); Lather Michigan 7 Feb / James River 26 Jun-21
  Jul (C, 5); Camden Thomas 16-21 Feb / Banks 2 May-4 Jul (C, 2); Virtue Frederick 1-7 Feb / artillery 4-11 Jul (M, 1
  telegram); Palate Cairo 20 Feb / bridges 6 Apr-21 Jul (C, 2); Vulcan headquarters 27 Mar / railroad 21 Jul (both M,
  one telegram each).
- True conflicts, 2: wedding = battle 9-16 Jun (5079, Lincoln to Fremont) lies inside wedding = transportation 6-26 Jun
  (McClellan's line) -- a line difference, not a date one; Stanhope = the Shenandoah 4-11 Jul (5100) lies inside
  Stanhope = flank 1 Jun-21 Jul. decode.py reads both as "a | b", grade M.
- Caveat: the ranges come from the witnesses on disk, so they bound where a value is attested, not where a table was in
  force; a Feb value read on, say, 20 Mar is M by construction (no witness), which is the rule-4 behaviour asked for.
  The split points (between 21 Feb and 6 Apr for Anthon/Palate, 21 Feb and 2 May for Camden, 7 Feb and 26 Jun for
  Lather) are not fixed by any witness yet. Two Feb rows already noted as two-key words (Devon, Humboldt) carry only
  their Feb witness; their contrary pages are marked "on p.[n]" in the evidence and are excluded.
- Rule 10: N1 shape -- every witness is a telegram already printed in the OR (1882-85); this is key bookkeeping, not new
  plaintext.

## GAPS132-eckert-1862 (3 Oct 2026, account-4)

Step run: GAPS127's Verdict -- decode the ledger pages GAPS113 did not match to OR ser. I vols. 7, 9-12 with the dated
key. Script: `print/residue_decode.py PAGES_DIR --write|--check` (imports decode.py's dated rule; outputs
`print/residue/readings.md` and `print/residue/pages.tsv`, one row per page: entries, key.md tokens by grade, oov,
page judge). `--check` exits 0; `python3 decode.py --check` exits 0 (key.md and the ten readings untouched).
Inputs: the volunteer page texts, re-fetched for this step (hdl.huntington.org 69 requests, 1.6 s apart; one empty reply
on the front cover), not committed. The brief said "disk only", but GAPS113-122 never committed the page texts, so
the step could not run without this re-fetch; logged here as a deviation.
- Pages: 57 text pages unmatched (GAPS113 counted 60; the difference is the front cover, the pastedown title and one
  page now empty), 122 entries. The residue is NOT spring-summer: by first entry date 40 pages are Feb, 13 Mar, 1 Apr,
  3 Jul 1862 -- the unmatched pages are mostly the Feb-Mar western-theatre traffic that OR vol. 7 does not print and
  vol. 8 (not fetched) may.
- Grades (rule 4, key.md tokens only): C 99, I 31, M 124 (Feb 86/30/87, Mar 9/1/26, Apr 3/0/2, Jul 1/0/9); H 0, S 0.
  M is high by construction: a Feb row's witness range is a few days wide, so an entry dated outside it reads M
  (GAPS127 caveat). oov 860 (tokens in no English corpus word list: proper names, misspellings, or code words missing
  from key.md -- a lower bound on unread code, not a grade). Code words that are ordinary English words and absent from
  key.md are invisible to this count. Source caveat: the text is the volunteer transcription, not reconciled against
  the image (rule 2), so every reading here is conditional on it.
- Judge (`tools/judge_plaintext.py specs/eckert-1862.json`, spec written in this step; corpus `en` = Holmes +
  Moby-Dick, no 1860s English corpus exists in tools/data; `en`'s per-fold false-negative spread is 0.44-0.64,
  tools/data/en/README.md, so FAIL/PASS against it is of unknown reliability, rule 3):
  real decode, all 57 pages: score -1.036 vs real_p05 -0.831, null_p99 -2.141, FAIL (N 35573);
  shuffled-key control (key.md's row sets permuted across its words, seed 1862): -1.033 vs -0.830 / -2.137, FAIL (N 33491);
  code-word windows only (each key token's meaning +/- 3 words): real -1.131 vs -0.843 / -2.125, FAIL (N 6423);
  shuffled-key windows -1.129 vs -0.844 / -2.123, FAIL (N 5422).
  Per page: 1 of 57 PASSes (5015, 23 Feb, -0.849 vs -0.863; 3 M tokens).
- What the numbers say: the real key and the shuffled key score the same to 0.003 on the whole text and on the
  code-word windows. A 4-gram letter judge cannot tell a right code-word value from a wrong one when the plaintext is
  telegraphese with code words as a few percent of the letters: the control does vary on this statistic, but the
  statistic does not respond to the key, so this is "judge cannot decide" (rule 3), not a negative on the key and not a
  support for it. The FAIL against real_p05 is the register (1862 telegraphese, names, numbers) against 19th-century
  novels, the same on both sides.
- Reading ready: 0 pages by the script's mechanical rule (>= 1 key token, no M, page judge PASS). No status change.
  Read by eye, the decodes are coherent where key.md covers the date (e.g. 5059, 1 May 1862, [Lincoln] to [Halleck]
  about Schofield and the Missouri members of Congress, "Luna" unread) -- for a separate verifier with a print check,
  not a claim here (rule 10: these telegrams were not found in OR vols. 7, 9-12 by or_match.py; Lincoln's own
  telegrams are likely in Basler's Collected Works, not searched in this step).
- Requests: hdl.huntington.org 69 (1 object record + 68 page records); no vision, no subagents.

## GAPS140-eckert-1862 (3 Oct 2026, account-4)

Step run: GAPS132's next -- the 57 residue pages (122 entries) against OR ser. I vol. 8 and Lincoln's printed works.
Disk first: page texts were not on disk in this container; the committed `print/residue/readings.md` (decoded, code
words replaced by their key.md meaning) was used as the page text for the 5-gram search, and only the pages that
matched were re-fetched raw for alignment (hdl.huntington.org 6 requests). Results in `print/residue_print.tsv`.
- OR vol. 8 (warofrebellionco08unit `_djvu.txt`, 1 request): `print/or_match.py` unchanged, --min 6. Positive control
  passes: page 4976 (T5, Lincoln to Hunter and Lane, 10 Feb) found at p.551, 40 shared 5-grams (38 on the raw text).
  New matches: 4973 (8 Feb, Stanton to Halleck) p.547, 24; 5041 (7 Mar, Stanton to Halleck) p.596, 13. At --min 3 three
  more pages share 3-4 (4975, 4985, 5023), at the GAPS113 calibration's cross-telegram ceiling (3): not matches.
  4985 (15 Feb, Marcy to Hooker, Budd's Ferry) belongs to the Potomac line, OR vol. 5, not fetched.
- `print/or_align.py` on the vol. 8 matches: no new code word. Its proposals: Carroll = Hunter (agrees key.md), one
  `single` junk pair (able -> "spared from kansas", the Dix entry mis-anchored). Held-out: 0 fit words, 0/0 scored, so
  no check ran. or_align.py fixed in this step: since GAPS127 `load_key()` returns a list of dated rows per word and
  the proposals/known-answer lines crashed on it (now: agrees-key if any dated value matches).
- Lincoln, Collected Works vol. 5 (Basler): both IA copies (collectedworksof0005royp, collectedworksof0000royp_v6w0)
  are lending-only and are NOT in the be-api full-text index -- the T5 phrase "avail the government of the services of
  both" returns 0 hits on each, so a miss there is a non-test, not a negative. Substitute: the same be-api search over
  all of IA (T5 control: 125 items, among them the Nicolay-Hay editions). Phrases from the 8 Lincoln-authored or
  Lincoln-related residue entries: 7 found, in the Nicolay-Hay letters/telegrams and Complete Works volumes and OR
  vol. 53 (5056, "a protest against General Denver"); one ("effectually keep", 4984) too common to search. be-api gives
  no page locator, so these are identified texts, not page citations; Basler page numbers need the owner's copy or a
  local read.
- What the print says about the key (by eye on the printed address lines; `print/residue_print.tsv`):
  Alden = Halleck on 8 Feb, 7 Mar, 21 Mar, 1 May and twice on 13 Jul 1862 (five telegrams beyond the Feb set; the
  13 Jul pair is Lincoln's "You should call on General Halleck" and "Halleck, Corinth, Mississippi: They are having a
  stampede in Kentucky"); Legend = Kentucky on 13 Jul (key.md: 17 Feb only); Lamb = Kansas on 21 Mar (key.md I,
  10-13 Feb), the clerk striking "Magnet" (= Arkansas) for it; Luna = Missouri (1 May, twice; not in key.md);
  Irving = Lincoln throughout.
- Conflict (rule 4, logged not merged): Alden = Halleck on 13 Jul 1862 (5104, two Lincoln telegrams, print as above)
  against key.md Alden = Banks 17-20 Jul 1862 (5110, 5112; OR 11 pt3 p.326, OR 12 pt3 pp.486-487; GAPS118, GAPS122).
  The ranges do not overlap (13 vs 17 Jul) but sit four days apart, with Halleck named general-in-chief on 11 Jul; the
  Banks rows were aligned, these are address lines read by eye. Not resolved by count.
- key.md unchanged. The brief's gate (or_align held-out + shuffled pairing before any key.md change) cannot run on
  these: the words sit in address lines, which or_align's 5-gram anchors do not reach, and the Lincoln texts have no
  local full text to align against. A by-hand held-out split would not help either: every matched telegram is to
  Halleck, so a shuffled-pairing control lands on "Halleck" as often as the real pairing does (rule 3, a control that
  cannot differ by construction). Proposed rows, pending a discriminating check: Alden = Halleck extended to
  05 Feb-13 Jul (C); Legend = Kentucky extended to 13 Jul (C); Lamb = Kansas 21 Mar (C, one telegram -- stays I under
  the >= 2 telegrams rule); Luna = Missouri 1 May (one telegram, I at most).
- N1 shape: every telegram matched here is in print (OR vol. 8, OR vol. 53, the Nicolay-Hay editions); this step adds
  ledger-to-print identifications and key witnesses, not new plaintext. No novelty is claimed (rule 10).
- en judge not used (GAPS132: real vs shuffled-key within 0.003). Requests: archive.org 1 (OR vol. 8 djvu) + 7
  metadata/advancedsearch; be-api.us.archive.org 16; hdl.huntington.org 6. No vision, no subagents.

## GAPS142-eckert-1862 (3 Oct 2026, account-4)

Step run: GAPS140's Verdict -- the 57 residue pages (`print/residue/readings.md` as page text, code words replaced by
their key.md meaning, brackets stripped) against OR ser. I vol. 5 and vol. 53 with `print/or_match.py` unchanged.
OR texts: warofrebellionco0005vari (ser. I vol. 5, 1881) and warofrebellion0153rootrich (ser. I vol. 53); the 1972
reprint warofrebellionco0053unit is access-restricted ("Item not available"), so the rootrich copy was used. Rows in
`print/residue_print.tsv`.
- Positive controls: vol. 5, page 4962 (5 Feb, McClellan HQ to Lander, Romney) at p.722, 81 shared 5-grams; vol. 53,
  page 5056 (Stanton to Halleck, Denver protest; GAPS140's be-api identification) at p.516, 65. Both pass.
- New matches at --min 6, all vol. 5: 5044 (9 Mar, Marcy to Hooker, Budd's Ferry) p.524, 42; 5035 (3 Mar, to Anthon =
  Banks, department limits) p.733, 16 -- the print there is the General Order text (L. Thomas), not the telegram, so
  only the order's sentences align; 5031 (28 Feb, Stanton to McClellan) p.129, 10. vol. 53: no page beyond the control.
  At --min 3: 4975 and 4985 share 3 with vol. 5, 5035 shares 3 with vol. 53 -- the GAPS113 cross-telegram ceiling, not
  matches. So 4985 (15 Feb, Marcy to Hooker), which GAPS140 assigned to vol. 5, is not printed there by this test.
- `print/or_align.py` on the vol. 5 matches (raw page texts, hdl.huntington.org 5 requests): 4 telegrams, 11 candidate
  occurrences, 8 ledger words. Agree key.md: whistle = enemy, Twinkle = Romney (2), opal = Winchester, Negus = Potomac.
  Not in key.md: Nutmeg = James [River] (2 occurrences, one telegram, 5035, 3 Mar); damon = batteries (one, 5044,
  9 Mar). By eye, also not in key.md: Ellen = Fredericksburg (5044; or_align did not pair it). Junk pairs: "General" ->
  "flinstone creek", "sent" -> "then" (order text running past the telegram). Plain words the decode misread:
  "Cow Pastor Branch" in 5035 is the plain Cow Pasture Branch, so `residue_decode.py`'s [St Louis] there is a false
  code read (key.md Pastor = St Louis is dated 17 Feb only, so it already read M); "Bulerny Falls" is Balcony Falls.
- Held-out check: fit words 7, test 0 of 0 scored, shuffled-pairing control mean 0.00 (200 draws). Here the control
  could differ in principle (the four telegrams go to Lander, Banks, Hooker and McClellan, not one recipient as in
  GAPS140), but no word recurs across the fit/test split, so nothing was scored: a non-test, not a pass or a fail
  (rule 3). key.md unchanged. Proposed, pending a recurrence: Nutmeg = James River (C, 3 Mar, one telegram -> I under
  the >= 2 telegrams rule), damon = batteries and Ellen = Fredericksburg (9 Mar, one telegram each, I at most).
  Witness dates gained for existing rows (no row edited): Twinkle 05 Feb (key.md I, 06 Feb), opal 05 Feb (key.md M),
  Negus 03 Mar (key.md I, 15 Feb).
- Conflicts: none new; Alden = Halleck 13 Jul vs Alden = Banks 17-20 Jul (GAPS140) stays logged, not merged.
- N1 shape: every telegram matched here is printed in OR vol. 5 or 53; no novelty is claimed (rule 10).
- Requests: archive.org 5 advancedsearch + 3 metadata + 1 files + 3 `_djvu.txt` (one returned the restricted page);
  hdl.huntington.org 5. No vision, no subagents.

## GAPS147-eckert-1862 (3 Oct 2026, account-4)

Step run: GAPS142's Verdict -- align the OR ser. I vol. 9, 10 pt 1-2 and 11 pt 1 matches (18 pages, GAPS113's
`print/or_matches.tsv`) with `print/or_align.py` unchanged, then one pooled run over every aligned volume so the
one-telegram proposals can reach two telegrams. Disk first: nothing on disk in this container; page texts
(hdl.huntington.org) and the OR `_djvu.txt` files (archive.org) re-fetched to the scratchpad, not committed.
- Per volume (`print/align09`, `align10p1`, `align10p2`, `align11p1`): vol. 9 5 telegrams, 2 occurrences (Devon =
  Norfolk, agrees); vol. 10 pt 1 1 telegram (Andes = McClellan); vol. 10 pt 2 5 telegrams, 14 occurrences, held-out
  2/2 vs control 0.00; vol. 11 pt 1 8 telegrams, 41 occurrences, held-out 5/5 vs control 0.00 (200 draws). Too few
  test occurrences per volume to gate anything alone.
- Pooled (`print/align_pooled`: OR vols. 5, 9, 10 pt 1-2, 11 pt 1 and 3, 12 pt 1 and 3 concatenated, all their
  or_matches rows plus GAPS142's vol. 5 pages 4962, 5031, 5035, 5044): 97 telegrams, 118 entries on 73 pages, 291
  candidate occurrences, 110 ledger words. Held-out (even/odd telegram split, fixed in the script before scoring):
  63/77 = 0.818 against the shuffled-pairing control mean 0.17 hits, p95 1 (1000 draws). The control can differ here
  -- the telegrams go to McClellan, Fremont, Banks, McDowell, Halleck, Wool and others over Feb-Jul -- so this is a
  pass, unlike GAPS140 (one recipient) and GAPS142 (0/0 scored).
- Added to key.md at C (two telegrams, one printed meaning, no rival in the pooled run): Japan = Manassas (5061,
  5063; Lincoln to McClellan, both 25 May, OR 11 pt1 p.31-32 -- same day and pair, two distinct printed telegrams);
  Persian = army (5089, 5092; 21 and 28 Jun); tarquin = movements (5063, 5090; 25 May, 26 Jun; plural tarquins on
  5062); Pastor = battle (5061, 5092; 25 May, 28 Jun) as a dated split of the Feb row Pastor = St Louis (17 Feb).
  Not added: Anthons = McDowell (3 telegrams) and wafers = regiments (2) are inflected forms of existing rows
  (Anthon = McDowell, wafer = regiment), noted only; the pooled 'conflicts-key' rows juno/welsh/tambour/whist are
  OCR or plural variants of the key.md meaning (gordousville, re enforcements, in fantry, regiments), not conflicts.
- The GAPS140/142 one-telegram proposals, pooled: none reached two telegrams. Nutmeg (James River), Ellen
  (Fredericksburg) and Lamb (Kansas, 21 Mar) did not pair in any aligned body text; damon = batteries stays one
  telegram (5044); Luna gets one aligned witness, = Shenandoah (5061, 25 May), which conflicts with GAPS140's by-eye
  Luna = Missouri (1 May, address lines, 2 telegrams): logged here with both witness dates, not merged, not added
  (rule 4). Legend = Kentucky gains an aligned body-text witness (5076, 8 Jun, OR 10 pt2 p.277), so the key.md row
  now runs 17 Feb-08 Jun by its own witness rule; GAPS140's 13 Jul address-line witness stays unmerged.
- Rebuilt dated key column (`print/key_dates.py --write`, then `--check` exit 0): 14 rows' ranges widen from the new
  aligned witnesses, among them Alden = Halleck to 05 Feb-10 Mar (5040, 5047, OR 10 pt2 p.610-612) and Alden = Banks
  to 25 May-20 Jul (5061, 5063). Conflict, logged: GAPS140's by-eye Alden = Halleck on 13 Jul (5104) now falls inside
  the aligned Banks range (25 May-20 Jul), not four days outside it; still address lines read by eye, not merged.
  Overlapping rival rows in key.md after the rebuild: only the two known true conflicts (wedding, Stanhope).
- Residue readings regenerated (`print/residue_decode.py --write`): 56 pages, 120 entries, C 95, I 37, M 114 (was
  57/122, C 99, I 31, M 124); en judge still FAILs real and shuffled-key alike (-1.037 vs -1.029), judge cannot decide.
  Page 4976 (T5, already read in reading.md, words unaffected by this step's rows) is missing from this regeneration:
  its page text failed twice (HTTP 502, then empty reply) and was not retried further (good-citizen rule), so a
  `--check` with all pages on disk will report the files stale until a session re-fetches 4976 and re-runs `--write`.
  Side effect to watch: the 1 May entry on 5059 ("Alden ... Luna members of Congress", Lincoln to Halleck in print,
  GAPS140) now decodes Alden as [Banks] (nearest dated row, graded M) where it read [Halleck] before -- the print
  says Halleck; with Halleck addressed as Alden on 1 May and 13 Jul (by eye) and Banks named Alden in aligned body
  text 25 May-20 Jul, the Halleck/Banks split for Alden is now a candidate true conflict (rule 4), logged, not
  resolved by count.
- N1 shape: every telegram aligned here is printed in the Official Records; this step adds code-word identifications
  from print (grade C), not new plaintext. No novelty is claimed (rule 10).
- Requests: hdl.huntington.org 132 (126 page texts kept; 502s retried once each, 4976 failed both times); archive.org 8 `_djvu.txt`.
  No vision, no subagents.

## GAPS153-eckert-1862 (3 Oct 2026, account-4)

Step run: GAPS147's Verdict -- re-fetch ledger page 4976, regenerate the residue, then grep it against OR ser. I
vol. 51 pt 1 (warofrebellion511unit, the 1897 supplement of Union correspondence) and align. Page texts and OR text
re-fetched to the scratchpad, not committed.
- Page 4976 fetched first try (one request); `print/residue_decode.py --write` then `--check` exit 0: 57 pages, 122
  entries (was 56/120). With the key.md changes below: C 120, I 41, M 97 (was C 95, I 37, M 114); en judge still
  FAILs real and shuffled-key alike (-1.036 vs -1.031), judge cannot decide.
- `print/or_match.py` (unchanged) on the 57 residue pages vs vol. 51 pt 1: 28 pages at --min 6 (9-148 shared
  5-grams), all 1 Feb-21 Mar 1862; at --min 3 three more pages share exactly 3 (5001, 5005, 5048) -- the GAPS113
  cross-telegram ceiling. Positive control (synthetic, fixed before the run): three 80-word passages cut from the
  vol. 51 text at seeded positions with every sixth word replaced by a code word: 2 of 3 found at --min 6 (9, 12
  5-grams), so a real telegram can be missed at that density. Rows in `print/residue_print.tsv`; the or_page
  column is unreliable for this volume (its running heads OCR badly), so locators are the IA identifier only.
- `print/or_align.py` on vol. 51 pt 1 alone (`print/align51p1`): 21 telegrams, 51 occurrences, held-out 6/6 vs
  shuffled-pairing control mean 0.12, p95 2 (1000 draws). Pooled (`print/align_pooled`, replaced: GAPS147's run
  reproduced exactly first, 63/77, then vol. 51 pt 1 appended): 123 telegrams, 162 entries on 99 pages, 339
  occurrences; held-out 76/88 = 0.864 vs control mean 0.26 hits, p95 1 (1000 draws). Recipients vary (Lander,
  Rosecrans, Hooker, Banks, Halleck, McClellan), so the control can differ: a pass.
- key.md, grade C (two telegrams, one printed meaning, no rival): damon = batteries (4985, 15 Feb, Marcy to Hooker,
  OR 51 pt1, "upon all the batteries"; 5044, 9 Mar, OR 5 p.524); yankee firmed from M "(stores? transportation?)"
  to transportation (5000, 19 Feb, OR 51 pt1; 5053, 20 Mar, OR 11 pt3). `print/key_dates.py --write` (10 cells
  widened) then `--check` exit 0; `decode.py --check` exit 0.
- Conflicts logged, not merged (rule 4; the key.md rows are I/M inferences, the print is C, dates overlap):
  Anthon = Rosecrans in print on 2 Feb (4961, address "Rosecrans, Wheeling"), 7 Feb (4969) and 14 Feb (4982),
  against key.md Anthon = Banks (I, 06 Feb, ledger p.[11]); Virtue = Grafton in print on 2, 7, 8 and 14 Feb (4961,
  4969, 4973, 4982) against key.md Virtue = Frederick (I, 01-07 Feb); Vesper = New Creek in print on 1-2 Feb (4960,
  4961) against key.md Vesper = Cumberland (Md.) (M, 01-05 Feb). The three hang together (Lander's support drawn
  from Rosecrans's department at Grafton to New Creek), so the Feb Banks/Frederick/Cumberland inferences may all be
  wrong, but the p.[11] plain/coded pair for Anthon = Banks is a ledger witness and is not overruled by count.
- One telegram only, not added: chester = attack (4985, 15 Feb; key.md Chester = Curtis C 21 Feb, a dated-split
  candidate); dimple = Dumfries, emblem = Occoquan (5039, 5 Mar); Eddy = Banks, Merlin = Maryland (5021, 24 Feb;
  key.md Merlin = Virginia); Nutmeg = James (5035 again, the same telegram as GAPS142); Luna, Ellen, Lamb: no new
  witness.
- N1 shape: every telegram matched here is printed in OR ser. I vol. 51 pt 1; no novelty is claimed (rule 10).
- Requests: hdl.huntington.org 127 (57 residue pages + 4976 with one retry of 4973 after an empty reply; 69 pooled
  pages); archive.org 1 advancedsearch + 9 `_djvu.txt`. No vision, no subagents.

## GAPS161-eckert-1862 (3 Oct 2026, account-4)
Job: settle the Feb values of Anthon, Virtue and Vesper (GAPS153 conflicts) from ledger p.[11] (pointer 4966) and its
"plain twin". Inputs: page texts 4965-4967 re-fetched from the CONTENTdm `text` field (not committed, volunteer
transcription); OR ser. I vol. 51 pt 1 `_djvu.txt` (IA warofrebellion511unit) re-fetched. Word alignment of each coded
entry against its printed text with difflib (the or_align.py same-message, two-encodings logic, run by hand on three
entries; no new code).
- The twin premise was wrong. Page [10] (4965) has the coded "Anthon Lander is moving on Twinkle Help him if you can in
  any way" and page [11] (4966) the plain "Genl N P Banks - Frederick Lander moving on Romney If you can help him by
  showing force on the River bank do so". The wording differs, and page [10]'s fourth entry, coded "Genl Lander Have
  teleghd Anthon & Arno of your movement & to aid you if possible", is printed in OR 51 pt 1 [6 Feb 1862] as "Have
  telegraphed Rosecrans and Banks of your movements, and to aid if possible". So McClellan sent two telegrams, one coded
  to Anthon and one plain to Banks; the page [11] entry is the parallel message to Banks, not a twin of the coded one.
- Direct witness for Anthon on the same day: page [12] (4967) third entry, coded "Anthon Col Piatt telegraphs to Secy
  of War from Cabell Court house that rebels are coming with whack & asks for one whist & one battery from Koran ...
  send back your four Koran whist tomorrow from Vesper Enemy have run from Twinkle", printed OR 51 pt 1 [6 Feb 1862],
  "General W. S. Rosecrans, Wheeling, Va.: ... artillery ... one regiment ... Ohio ... four Ohio regiments to-morrow
  from New Creek. Enemy have men from Romney" (running heads put it at about p.524-525; OCR heads unreliable, see
  GAPS153). Alignment: 13 substitutions, every one a code word for its printed value or a spelling difference
  (Secy/Secretary, tomorrow/to-morrow, run/men).
- Decided, key.md (rule 4, witnesses dated):
  Anthon = Rosecrans, C, 6 Feb (4965, 4967; with GAPS153's 4961, 4969, 4982 the range is 6-15 Feb). Banks withdrawn.
  Arno = Banks, C, 6 Feb (4965, the "Anthon & Arno" / "Rosecrans and Banks" pair); this replaces the undated M
  Arno = Rosecrans, which rested on a different word ("Arthur", received ledger mssEC 01 p.14); it agrees with the
  June row Arno = Banks (M), so key_dates gives 6 Feb-16 Jun.
  Vesper = New Creek, C, 1-6 Feb (4960, 4961 from GAPS153; 4967 "from Vesper" = "from New Creek"). Cumberland (Md.)
  withdrawn.
  Virtue = Grafton, C, 1-15 Feb (4961, 4969, 4973, 4982, GAPS153 alignment). Frederick withdrawn: it had no witness of
  its own, only the Anthon = Banks inference.
  Twinkle = Romney, I to C (4967 "from Twinkle" = "from Romney").
  No other row changed; the three hang together as GAPS153 said (Lander drawing Rosecrans's Ohio regiments from
  Grafton to New Creek).
- Checks: `print/key_dates.py --write` (4 cells), `--check` exit 0; `decode.py --check` exit 0 (the ten readings do not
  use these words). `print/residue/readings.md` is now stale for these words (it shows [Banks], [Frederick],
  [Cumberland (Md.)] at 4961, 4969, 4982 and others where the key now reads Rosecrans, Grafton, New Creek); regenerating
  it needs the 57 residue page texts, which are not on disk, over this job's 20-request limit; next step below.
- N1 shape: all three telegrams are printed in OR ser. I vol. 51 pt 1; no novelty claimed (rule 10).
- Requests: hdl.huntington.org 3 (page texts 4965-4967); archive.org 1 (`_djvu.txt`). No vision, no subagents.

## GAPS167-eckert-1862 (3 Oct 2026, account-4)
Step run: GAPS161's Verdict -- regenerate `print/residue/readings.md` with the corrected Feb key (Anthon = Rosecrans,
Arno = Banks, Vesper = New Creek, Virtue = Grafton, Twinkle = Romney).
- The 57 residue page texts re-fetched once (hdl.huntington.org 57 requests, 1.6 s apart, no retries needed), kept in
  the scratchpad, not committed (volunteer transcription, their credit); `print/residue/pages_manifest.tsv` now records
  pointer, URL, text length and SHA-256 of each page's `text` field (fetched 3 Oct 2026) so a later worker can confirm a
  re-fetch is the same text. Page set validated before the regeneration: the pre-GAPS161 folder (commit 5c93897a) with
  these 57 texts gives `residue_decode.py --check` exit 0, i.e. the committed readings reproduced exactly.
- `print/residue_decode.py --write` then `--check` exit 0; `decode.py --check` exit 0 (reading.md untouched).
  Grades (key.md tokens, rule 4): C 144, I 31, M 83 (was C 120, I 41, M 97 after GAPS153); H 0, S 0; oov 856 (was 856).
  M dropped on 8 pages (4960, 4961, 4969, 4982, 4983, 5021, 5035, 5048). en judge FAILs real and shuffled-key alike
  (full -1.036 vs -1.030; windows -1.128 vs -1.095; real_p05 about -0.83), judge cannot decide; 0 pages reading ready.
- Candidates (`print/residue_candidates.py PAGES_DIR --write|--check`, exit 0; `print/residue/candidates.tsv` carries the
  readings): entries with >= 1 key.md token and no M token. 32 entries on 25 pages (24 Feb, 7 Mar, 1 Apr); 25 of them
  with no I token either. 19 sit on pages print/residue_print.tsv already matches to print (OR ser. I vols. 5, 8, 51
  pt 1, 53; Nicolay-Hay) -- N1 shape where the entry itself is the printed one (a page match is not proof for every
  entry on it); 13 on pages with no print match yet. A sorting list for a later verifier, not a reading claim: the text
  is the volunteer transcription, not reconciled against the image (rule 2), and oov tokens (names, misspellings or
  unread code) remain in every entry. No novelty is claimed (rule 10).

| pointer.entry | date | C | I | oov | page in print |
|---|---|---|---|---|---|
| 4960.1 | 01 Feb | 0 | 2 | 5 | OR ser. I vol. 51 pt 1 |
| 4961.3 | 03 Feb | 0 | 1 | 5 | OR ser. I vol. 51 pt 1 |
| 4962.1 | 05 Feb | 1 | 0 | 4 | OR ser. I vol. 5 |
| 4969.1 | 07 Feb | 6 | 1 | 3 | OR ser. I vol. 51 pt 1 |
| 4969.2 | 07 Feb | 5 | 0 | 6 | OR ser. I vol. 51 pt 1 |
| 4973.1 | 08 Feb | 1 | 0 | 6 | OR ser. I vol. 51 pt 1; OR ser. I vol. 8 |
| 4976.1 | 10 Feb | 7 | 0 | 7 | OR ser. I vol. 8 |
| 4976.2 | 10 Feb | 1 | 0 | 3 | OR ser. I vol. 8 |
| 4978.1 | 11 Feb | 1 | 1 | 6 | -- |
| 4978.2 | 12 Feb | 1 | 0 | 9 | -- |
| 4983.2 | 14 Feb | 4 | 1 | 2 | OR ser. I vol. 51 pt 1 |
| 4992.2 | 16 Feb | 1 | 0 | 1 | -- |
| 4992.3 | 16 Feb | 3 | 0 | 0 | -- |
| 4995.1 | 07 Feb | 3 | 5 | 1 | -- |
| 4995.2 | 17 Feb | 2 | 0 | 3 | -- |
| 4997.2 | 18 Feb | 2 | 0 | 6 | -- |
| 4998.2 | 18 Feb | 1 | 0 | 7 | -- |
| 5005.2 | 20 Feb | 3 | 0 | 3 | -- |
| 5008.1 | 21 Feb | 1 | 0 | 2 | -- |
| 5016.1 | 23 Feb | 0 | 1 | 1 | OR ser. I vol. 51 pt 1 |
| 5016.3 | 23 Feb | 1 | 0 | 6 | OR ser. I vol. 51 pt 1 |
| 5017.1 | 23 Feb | 1 | 0 | 7 | OR ser. I vol. 51 pt 1 |
| 5029.1 | 27 Feb | 1 | 0 | 13 | OR ser. I vol. 51 pt 1 |
| 5031.3 | 28 Feb | 1 | 0 | 3 | OR ser. I vol. 5; OR ser. I vol. 51 pt 1 |
| 5036.2 | 03 Mar | 1 | 0 | 5 | -- |
| 5041.2 | 07 Mar | 1 | 0 | 4 | OR ser. I vol. 51 pt 1; OR ser. I vol. 8 |
| 5044.1 | 09 Mar | 1 | 0 | 17 | OR ser. I vol. 5 |
| 5051.1 | 16 Mar | 1 | 0 | 7 | -- |
| 5051.2 | 16 Mar | 1 | 0 | 6 | -- |
| 5054.3 | 22 Mar | 1 | 0 | 9 | Lincoln, Nicolay-Hay letters/works (IA be-api fts, no page locator); OR ser. I vol. 51 pt 1 |
| 5056.2 | 27 Mar | 1 | 0 | 9 | OR ser. I vol. 53; OR ser. I vol. 53 (supplement) |
| 5059.1 | 29 Apr | 1 | 0 | 5 | Lincoln, Nicolay-Hay letters/works (IA be-api fts) |

- Requests: hdl.huntington.org 57. No vision, no subagents.

## GAPS171-eckert-1862 (3 Oct 2026, account-4): the received ledgers mssEC 01-03

Fetched once, 3 Oct 2026, one CONTENTdm `dmQuery` per ledger on the `callid` field (every page with its `transc`
volunteer transcription in one response; manifest print/residue/received_manifest.tsv with sha256; not committed):
mssEC 01 (object 6796, "Received Feby. 2 to July 30, 1862", 217 pages, 206 with text), mssEC 02 (object 3820, "Feby. 7
to June 26", 246/229), mssEC 03 (object 2129, "Feby. 22 to May 2", 75/62). The 57 residue pages of mssEC 15 came in the
same way (one query; all 57 sha256 match pages_manifest.tsv; residue_decode.py and residue_candidates.py --check exit 0
on them once the page title is set to the items-endpoint form "Page_", the only field the two routes differ in).

Twin search (print/received_match.py, word 5-grams of each residue entry's raw and decoded text against every received
page, boilerplate 5-grams on >= 3 pages dropped): 122 residue entries; null (entry words shuffled, 2440 draws) p99 0,
threshold 3. Positive controls: (a) 60 synthetic coded twins (40-word windows of received entries with every single-word
key.md meaning replaced by its code word, 1.28 code words per window, about the residue's own key-token density of 258
in 7,693 words) recalled 60/60 at rank 1; (b) real duplicates across the received ledgers: 16 of 291 mssEC 02/03 pages
have a twin in mssEC 01. Result: 2 entries at or above threshold. 5023/1 (score 24) is the plain relayed copy of
Lander's Paw Paw report of 24 Feb (mssEC 01 p.84), a real twin but plain and already matched to OR 51 pt 1 (GAPS153),
no code word in it; 5048/1 (score 3, mssEC 01 p.113) is Marcy's reply quoting McClellan's Fairfax telegram of 13 Mar,
not a copy of the same telegram. The 13 no-print candidates of candidates.tsv: best score 0-2 each, no received twin.
This negative is conditional on the volunteer transcriptions and on the expectation that War Department outgoing
traffic is rarely in its own received book (control (b) shows the method finds a twin where one exists).

Sibling witness for the one-telegram words (the Verdict's other half): Luna, Lamb occur in one received telegram,
copied twice (mssEC 02 p.12-13, objects 3588-3589, and mssEC 03 p.37, object 2093; both copies agree word for word on
every code word), Halleck to Stanton, St Louis 7 Mar 1862, printed OR ser. I vol. 8 pp. 831-832 (Internet Archive
warofrebellionco08unit, djvu text, 1 request): "The Departments of the Ohio and the Missouri should be under one general
head. If not, all south of the Cumberland River should be added ... I would leave General Buell in the particular
command of his present department and army. The Department of Kansas has less connection with present operations".
Aligned slots (C, received direction, 7 Mar 1862): Indus = Stanton (address), Koran = Ohio, Luna = Missouri, Myrtle =
Cumberland River, Alvord = Buell, wayworn = army, Lamb = Kansas, Alden = Halleck (signature); "good for" is tail.
Held-out check (print/received_twin_check.py): of the 7 slots whose word already has a key.md value from sent-ledger
witnesses, 6 agree with the value nearest 7 Mar against a shuffled-key control mean 0.08, p99 1 (2000 draws); the one
disagreement, Indus, separates by date (Stanton 7 Mar here, and "signed Indus" on sent page 5049, 13 Mar, fits a
Secretary of War signature; Fredericksburg 25 May-17 Jul, GAPS118). Conflicts logged, not merged: Luna = Missouri
(7 Mar, this twin, C) agrees with GAPS140's by-eye Luna = Missouri (1 May) and conflicts with Luna = Shenandoah (25 May,
aligned, GAPS147). key.md is NOT changed: the new values (Indus = Stanton, Luna = Missouri) rest on one telegram each,
and on the received direction only (rule 4's direction lesson, AX2-172), the same bar Nutmeg, Ellen and damon were held
to; the witness also extends Koran, Myrtle, Alvord (C) and Lamb, wayworn (I in key.md) to 7 Mar. Nutmeg and Ellen: 0
occurrences in the three received ledgers. N1 shape: the plaintext is printed; this is a received-side re-alignment.
The second telegram on mssEC 03 p.37 (Halleck, 12 noon 7 Mar, "For Andes ... communication with Alvord") is not in
OR vol. 8 by phrase grep. decode.py --check 0, key_dates.py --check 0, residue_decode/candidates --check 0,
received_match.py --check 0. Requests: hdl.huntington.org 11 (2 searches, 1 field list, 3 compound-object, 1 item, 4
ledger queries), archive.org 2. No vision, no subagents.

## VERIFY-ECK correction (3 Oct 2026, account-4 verifier; details in AUDIT.md "Second audit")
- Re-derivation reproduces: decode.py, key_dates.py, residue_decode.py and residue_candidates.py `--check` exit 0; pooled
  held-out 76/88 again (new seed: control mean 0.20, p95 1; a fit-meaning permutation control: mean 1.64, max 18).
- Over-claim corrected: "13 [candidates] on pages with no print match yet" (GAPS167) counted only OR ser. I. Five are
  printed: 4995.2, 4997.2 and 5005.2 in OR ser. II vol. 3; 4995.1 in OR ser. I vol. 7 p.630 (dated there 17 Feb, 7.30
  a.m.; the transcription's "Feb 7" is probably "Feb 17"); 4992.2 in ORN ser. I vol. 22. Three are decoded wrongly:
  4978.2, 5051.1 and 5051.2 read Andes as [McClellan], but 5051.1 is "For Andes commanding Fort Monroe", signed by
  McClellan. "No M token" is not a quality signal for a telegram on a line no key witness covers.
- Coverage: residue page 4979 (12 Feb, Lamb/Koran entry) has text in the CONTENTdm dmQuery route but is not in the 57-page
  residue set.
- Prior art: the DCW blog's "Reverse Engineering Lost Codebooks" (21 Apr 2017) prints Palate, Rampant, Anthon = McDowell,
  Label/Sabel, Berlin and Andes for Apr 1862. Those key.md rows are published, not ours.

## GAPS181-eckert-1862 (3 Oct 2026, account-4): VERIFY-ECK's corrections carried, page 4979 added, DCW credit

- Andes line scope (rule 4): key.md gains `Andes | commander at Fort Monroe (Wool, inferred) | I` with evidence opening
  "line: Fort Monroe --" (witnesses 4978.2, 5051.1-2, 5054; computed range 10 Feb-27 Mar 1862), and
  `Dawn | Fort Monroe | C` from the 5051.1/5051.2 twin (half-clear "for Fort Monroe" = coded "for Dawn", same time,
  sender, text; range 15-27 Mar). decode.py reads the line from the entry's own address ("Andes Dawn", "Andes
  [commanding] Fort Monroe"; LINE_MARKS) and on that line uses only the scoped row; off it, the McClellan row as before.
  The ten T readings (reading.md) are unchanged (`decode.py --check` 0).
- The three withdrawn entries, regraded: 4978.2 (12 Feb) now reads [commander at Fort Monroe] (I) [Fort Monroe] (M:
  Dawn's only witness is 16-27 Mar) and leaves the candidate list; 5051.1 reads I 1, 5051.2 C 2, I 1 (the McClellan C
  token on each is gone). A fourth entry had the same fault: 5054.3 (22 Mar, S. Williams to "Andes Dawn", "I am directed
  by Gen McClellan to inform you"; in print, OR 51 pt1) now reads [commander at Fort Monroe] (I) [Fort Monroe] (C) twice.
  All four remain without a novelty class (AUDIT.md section C; the readings changed, the classes did not).
- Page 4979 (Page [24], 12-13 Feb): fetched once (pages_manifest.tsv row, sha256), decoded with the dated key. Entry 1,
  6 PM 12 Feb, McClellan [Andes, C] to Halleck [Alden, C]: "Retain the [Ohio] battery also the other troops for [Kansas]
  if absolutely necessary I would rather not hold back the [Kansas] [infantry] if you can help it", time word Nancy = 6 PM
  (I). Tokens: C 2, I 3 (Lamb x2, Nancy), M 2 (Koran = Ohio and wharf = infantry, each outside its witness range). Entry 2, 13 Feb, Marcy to
  Hooker at Budds Ferry (barges from Washington and Baltimore), carries no key.md token (clear text). Not print-checked
  this pass (or_match never saw the page). Page judge FAIL -1.043 vs real_p05 -0.869 (en, fold caveat).
- Residue totals (`print/residue_decode.py`, 58 pages, 124 entries): C 146, I 38, M 86, oov 863 (was 57 pages, 122
  entries, C 144, I 31, M 83). Judge, real vs shuffled-key control: full -1.037 vs -1.031, windows -1.129 vs -1.101, all
  FAIL against real_p05 about -0.83/-0.84 -- the judge cannot decide, as before. Candidates 31 (was 32: 4978.2 out).
- Credit (rule 8): key.md now names the DCW blog's eight published arbitraries (Andes, Alden, Alvord; Palate, Rampant,
  Anthon = McDowell, Sabel, Berlin from "Reverse Engineering Lost Codebooks", 21 Apr 2017) and marks the six that have
  rows "key source: published"; Sabel and Berlin have no row.
- Checks: decode.py, print/key_dates.py, print/residue_decode.py PAGES, print/residue_candidates.py PAGES `--check` all
  exit 0 (PAGES = the 58 page JSONs re-fetched 3 Oct 2026, 57 matching pages_manifest.tsv sha256, not committed).
  Requests: hdl.huntington.org 58 (1.5 s apart). No vision, no subagents.

## Remaining gaps (finish-or-blocker pass, 3 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries (about 3%), all ten N1 (section 4, AUDIT.md)
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; OR print step done 3 Oct 2026 (GAPS113): 101 of 161 text pages match OR vols. 7 or 9-12; vols. 11 pt 3 and 12 pt 3/pt 1 aligned 3 Oct 2026 (GAPS118, GAPS122: 21 code words added at C); key.md dated 3 Oct 2026 (GAPS127); the 57 unmatched pages decoded with the dated key 3 Oct 2026 (GAPS132: 122 entries, C 99, I 31, M 124; 53 of 57 pages are Feb-Mar, not spring-summer; en judge FAILs real and shuffled-key alike, -1.036 vs -1.033, judge cannot decide; 0 pages reading ready); residue print grep 3 Oct 2026 (GAPS140): OR vol. 8 matches 3 pages (4976 control, 4973, 5041), no new code word; Lincoln texts identified for 7 entries in the Nicolay-Hay editions and OR vol. 53 (Basler vol. 5 not full-text searchable, non-test); OR vols. 5 and 53 grepped 3 Oct 2026 (GAPS142): 3 new vol. 5 pages (5031, 5035, 5044) plus the two controls, aligned, no key.md change (held-out 0/0 scored, non-test); vols. 9, 10 pt 1-2, 11 pt 1 aligned and all aligned volumes pooled 3 Oct 2026 (GAPS147: held-out 63/77 vs shuffled control mean 0.17 hits, p95 1; 4 code words added at C; residue readings regenerated without page 4976, fetch failed); page 4976 re-fetched and OR vol. 51 pt 1 grepped and pooled 3 Oct 2026 (GAPS153: 28 residue pages matched, pooled held-out 76/88 vs control mean 0.26 hits, p95 1; damon and yankee to C; residue 57 pages, C 120, I 41, M 97); next: the residue pages still unmatched by any OR volume (57 less the 28 here and the vols. 5, 8, 53 pages), read against the received ledgers mssEC 01-03 (gap 2), ~$2; received ledgers read 3 Oct 2026 (GAPS171): 122 residue entries, 0 coded twins (1 plain relay already in print, 1 reply), synthetic control 60/60, cross-ledger control 16/291; verifier print search 3 Oct 2026 (VERIFY-ECK, AUDIT.md second audit): of the 13, 5 are printed (OR ser. II vol. 3, OR I/7 p.630, ORN I/22), 4 are N1 by published transcription plus DCW 2017 arbitraries, 3 are misdecoded (Andes is not McClellan on the Fort Monroe line), 1 N3 (Sermon = Bowling Green, 4992.3); residue page 4979 added and Andes scoped by line 3 Oct 2026 (GAPS181: 58 pages, C 146, I 38, M 86; Andes = commander at Fort Monroe (I) and Dawn = Fort Monroe (C) on that line; 4978.2, 5051.1-2 and 5054.3 regraded; candidates 31); next: run print/or_match.py over page 4979 (OR vols. 7-8, 12-13 Feb), ~$0.5
- residue code words not fixed by any known plaintext - blocker: open-codes; 31 Feb words fixed (section 5) plus 21 spring-summer words (GAPS118, GAPS122); later eastern-line tables reuse Feb words for other values; dated key column added 3 Oct 2026 (GAPS127): of 10 conflicting words 8 separate cleanly by date, 2 stay true conflicts (wedding, Stanhope: overlapping ranges, read M); GAPS140 print witnesses: Alden = Halleck to 13 Jul against Alden = Banks 17-20 Jul (logged, not merged), Legend/Lamb/Luna range extensions proposed, key.md unchanged pending a discriminating check; GAPS142 proposals Nutmeg = James River, damon = batteries, Ellen = Fredericksburg (one telegram each, not added); GAPS147 pooled run: Japan = Manassas, Persian = army, tarquin = movements, Pastor = battle (dated split) added at C, Nutmeg/Ellen/Lamb/damon still one telegram, Luna = Shenandoah (25 May, aligned) vs Luna = Missouri (1 May, by eye) logged as a conflict, Alden = Halleck 13 Jul (by eye) now inside the aligned Banks range 25 May-20 Jul, logged; GAPS153 (OR 51 pt1): damon = batteries added, yankee = transportation firmed to C; Anthon = Rosecrans, Virtue = Grafton, Vesper = New Creek (print, 1-14 Feb) logged against the Feb inferences Banks/Frederick/Cumberland; settled 3 Oct 2026 (GAPS161): pages [10]-[12] against OR 51 pt1, no twin (page [11] is a parallel plain telegram), Anthon = Rosecrans, Arno = Banks, Vesper = New Creek, Virtue = Grafton, Twinkle = Romney all C for Feb; residue readings regenerated with that key 3 Oct 2026 (GAPS167: C 144, I 31, M 83; 32 entries with no M token listed in print/residue/candidates.tsv, 13 on pages with no print match) ; received ledgers read 3 Oct 2026 (GAPS171): Halleck-Stanton 7 Mar twin (mssEC 02 p.12-13 = mssEC 03 p.37 = OR 8 pp. 831-832) gives Luna = Missouri, Lamb = Kansas, Indus = Stanton (C, received direction, one telegram; held-out 6/7 vs shuffled p99 1; logged, key.md unchanged), Nutmeg and Ellen 0 occurrences -- next: a second witness for Indus = Stanton / Luna = Missouri in the sent ledger's Feb-Mar pages (grep mssEC 15 for Indus, Luna against OR vols. 7-8 by date), ~$1; and fix the table-change dates (Feb-Apr/May split points unwitnessed) from the March-April ledger pages when the residue entries are decoded (gap 1), ~$0 extra
- 1863-67 sent ledgers at grade H - blocker: not-attempted; filled-in cipher books exist at the Huntington (section 5); next: pilot one 1864 sent ledger (mssEC 18 or 19) against mssEC 41-46 (Cipher No. 1), ~$6

## Escalation (3 Oct 2026)
- [x] siblings: received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171): no coded twin of a residue entry; one received-side twin (7 Mar, OR 8 pp. 831-832) logged for Luna, Lamb, Indus
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [ ] known-keys: no filled-in book for Feb 1862 (failure log); the 1863-67 books are the H route (gap 3)
- [x] print: OR vols. 7-8 done (ten matches); Papers of U. S. Grant vol. 4 done 3 Oct 2026, no hit; OR vols. 9-12 grepped 3 Oct 2026 (GAPS113): 69 ledger pages matched there, 32 in vol. 7 (101 of 161); vol. 8 grepped 3 Oct 2026 (GAPS140, 2 new pages); Lincoln texts found in Nicolay-Hay (GAPS140); vols. 5 and 53 grepped 3 Oct 2026 (GAPS142, 3 new vol. 5 pages); every matched volume aligned and pooled 3 Oct 2026 (GAPS147); vol. 51 pt 1 grepped, aligned and pooled 3 Oct 2026 (GAPS153, 28 pages)
- [ ] key-rebuild: Andes line-scoped and Dawn = Fort Monroe added 3 Oct 2026 (GAPS181, VERIFY-ECK's correction); Feb Anthon/Arno/Vesper/Virtue settled by print 3 Oct 2026 (GAPS161; residue regenerated 3 Oct 2026, GAPS167, M 83); residue decoded 3 Oct 2026 (GAPS132, M 124 of 254 key tokens, mostly Feb rows read outside their few-day witness ranges); vol. 11 pt 3 done (GAPS118, 13 words); vol. 12 pt 3/pt 1 done (GAPS122, 8 words + widow to C, 7 conflicts logged); dated key column done 3 Oct 2026 (GAPS127, 8 of 10 conflicts date-scoped); vols. 9, 10, 11 pt 1 aligned and pooled 3 Oct 2026 (GAPS147, 4 words added, held-out passes against its control)
- [n/a] image-check: the ten readings were reconciled against the image (reading.md, Reconciliation)
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 3 internal gaps; cheapest next: a sent-side second witness for Indus = Stanton and Luna = Missouri (mssEC 15 Feb-Mar pages against OR vols. 7-8), ~$1; then print/or_match.py over residue page 4979 (added 3 Oct 2026, GAPS181), ~$0.5

## GAPS187-eckert-1862 (3 Oct 2026, account-4): page 4979 print-checked, SO-ECK-4992 phrases re-run

- Page 4979 against OR ser. I vols. 5, 7, 8, 51 pt 1 (IA `_djvu.txt`, fetched once to scratch, not committed;
  `print/or_match.py`, output `print/or_matches_4979.tsv`). Positive controls run in the same pass: page 4976 against
  vol. 8 (38 shared 5-grams, p.551, as GAPS140) and page 4980 against vol. 7 (14, p.608, as or_matches.tsv). The page
  text re-fetched is byte-identical to pages_manifest.tsv (648 chars, same sha256).
  - Entry 2 (13 Feb, Marcy to Hooker, Budds Ferry, clear, no key.md token): printed, OR ser. I vol. 51 pt 1 p.498
    (51 shared 5-grams; "six barges capable of carrying ... men will be sent you from here and ten barges"). Nothing to
    grade; it is a clear relay already in print.
  - Entry 1 (12 Feb 6 PM, McClellan to Halleck, "Retain the [Ohio] battery also the other troops for [Kansas] ..."):
    not printed in vols. 5, 7, 8 or 51 pt 1 (0 5-grams at --min 1 beyond two formula hits on unrelated pages; phrase
    grep, OCR line-joined, for "rather not hold", "if you can help it", "other troops for", "hold back the": 0).
    Its *question* is printed: Halleck to McClellan, Saint Louis, 12 Feb 1862, 3 p.m., OR ser. I vol. 8 p.553: "Please
    answer about Ohio battery and other troops ordered from this department to Kansas. Can I use them? I greatly need
    them at this moment." McClellan's 6 PM entry answers it word for word in the clear parts ("battery also the other
    troops for"), so the print supports Koran = Ohio and Lamb = Kansas on 12 Feb. Grades in the reading are left as
    they are (Koran M, Lamb I, wharf M, Nancy I; C 2): this is a received-side context witness, not a coded twin, and
    key.md is unchanged -- logged as a proposal: Koran = Ohio range 05-12 Feb (was 05-07), Lamb = Kansas second
    witness (with GAPS171's 7 Mar received twin). wharf = infantry on 12 Feb (range starts 13 Feb) gets no support.
  - Huntington transcription: the page text is the DCW volunteer transcription itself (CONTENTdm `text`); the decode
    in print/residue/readings.md reproduces it token for token, no divergence to log.
- SO-ECK-4992 (4992.3, 16 Feb, McClellan to Buell): reading unchanged after GAPS181's Andes/Dawn changes
  (`decode.py --check` 0; readings.md line 117 still "how many in [Bowling Green] line"; 4992.3 is not on the Fort
  Monroe line). `tools/print_check.py` re-run with five phrases (`print/phrases_4992.txt`, results
  `print/print-check-4992.tsv`): IA item vol. 7, IA global full text and OpenAlex no hits for all five; Google Books and
  CrossRef return only keyword (bag-of-words) matches, none relevant; Semantic Scholar and CrossRef partly 429
  (unreachable for some rows). Positive control "why could not a gunboat run up" (T8, OR 7 p.624): 1 exact in vol. 7,
  196 items IA-global. Local grep of vols. 5, 7, 8, 51 pt 1 for four of the phrases: 0. AUDIT.md and the SO row need no
  change (rule 10 propagation: nothing changed). This is a search result, not a novelty verdict.
- Requests: hdl.huntington.org 3, archive.org 4 (djvu) + 1, be-api 6, googleapis 5, openalex 5, s2 3, crossref 4. No
  vision, no subagents.

## Remaining gaps (finish-or-blocker pass, GAPS187, 3 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 146, I 38, M 86 (print/residue)
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; every OR volume that could hold Feb-Jul 1862 eastern and western telegrams is grepped and aligned (vols. 5, 7, 8, 9, 10 pt 1-2, 11 pt 1/3, 12 pt 1/3, 51 pt 1, 53; GAPS113-GAPS153), received ledgers mssEC 01-03 read (GAPS171, 0 coded twins), page 4979 print-checked (GAPS187: entry 2 in OR 51 pt1 p.498, entry 1 unprinted but its question in OR 8 p.553); the judge cannot decide on the residue (real -1.037 vs shuffled -1.031); next: fold the GAPS187 and GAPS171 range proposals (Koran = Ohio to 12 Feb; Lamb = Kansas; Luna = Missouri, Indus = Stanton) into key.md only after a sent-side second witness, by grepping mssEC 15 Feb-Mar pages for Indus/Luna/Koran/Lamb and checking each hit's date against OR vols. 7-8 (texts as fetched here), ~$1
- residue code words not fixed by any known plaintext - blocker: open-codes; about 863 oov tokens remain; most are one-telegram words no print or received twin narrows (GAPS140-GAPS171 logs); the table-change dates (Feb-Apr/May split points) are unwitnessed and settle only as gap 1 adds dated witnesses
- 1863-67 sent ledgers at grade H - blocker: not-attempted; filled-in cipher books exist at the Huntington (section 5); next: pilot one 1864 sent ledger (mssEC 18 or 19) against mssEC 41-46 (Cipher No. 1), ~$6

## Escalation (GAPS187, 3 Oct 2026)
- [x] siblings: received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171): no coded twin of a residue entry; one received-side twin (7 Mar, OR 8 pp. 831-832) logged for Luna, Lamb, Indus
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [ ] known-keys: no filled-in book for Feb 1862 (failure log); the 1863-67 books are the H route (gap 3, ~$6)
- [x] print: OR vols. 5, 7, 8, 9, 10 pt 1-2, 11 pt 1/3, 12 pt 1/3, 51 pt 1, 53, Nicolay-Hay, Grant Papers vol. 4 done; page 4979 done 3 Oct 2026 (GAPS187); SO-ECK-4992 phrases re-run, unchanged
- [ ] key-rebuild: range proposals pending a sent-side second witness (Koran, Lamb, Luna, Indus; gap 1, ~$1)
- [n/a] image-check: the ten readings were reconciled against the image (reading.md, Reconciliation)
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 3 internal gaps; cheapest next: sent-side second witness for Koran/Lamb/Luna/Indus in mssEC 15 Feb-Mar pages against OR vols. 7-8, ~$1; then the 1864 sent-ledger pilot against Cipher No. 1 (mssEC 41-46), ~$6

## GAPS191-eckert-1862 (3 Oct 2026, account-4): sent-side second witnesses for Koran, Lamb, Luna, Indus

- Input: the mssEC 15 volunteer transcription for all 173 pages in one CONTENTdm dmQuery call (`callid^mssEC 15`,
  field `transc`; not committed, re-fetch as in received_manifest.tsv with `mssEC%2015`), and the IA `_djvu.txt` of OR
  ser. I vols. 7, 8, 11 pt 3, 12 pt 1, 12 pt 3, 51 pt 1 (vol. 53 fetch returned 172 bytes, not used). Script
  `print/witness4/slot_align.py`: for each of the 50 occurrences of the four words, the OR span between the matched
  left and right ledger context (8 words each side, difflib) -- 14 aligned; shuffled-context control 0.34 mean, p95 2
  agreeing slots. Signatures and addresses ("signed Indus", "to Indus") and three Lincoln texts were then placed by
  word search (OR) and IA be-api phrase search (Nicolay-Hay). Witness table `print/witness4/witnesses.tsv` (23 rows).
- Held-out (`print/witness4/heldout.py`, leave one telegram out, predict from the same word's same-slot-class then
  nearest-dated witness): 20 of 23 vs shuffled-pairing control mean 3.92, p95 8, p99 10 (2000 shuffles; the shuffle
  changes the code-word/meaning pairing, so it can differ). Per word: Koran 7/7, Indus 9/9, Lamb 3/4, Luna 1/3.
- key.md (C, two or more telegrams each, and the check above):
  - Koran = Ohio: 7 more sent-side slots, all "Ohio"; 4981 (14 Feb) "ordered to Saffron Koran" = OR 7 p.612
    "ordered to Columbus, Ohio" (Saffron = Columbus, one telegram, not added). Witness column now 05-20 Feb.
  - Lamb = Kansas, I -> C: 4981 (13 Feb, two slots, OR 8 p.555), 5054 (21 Mar, Lincoln, Nicolay-Hay "suspend the order
    sending General Denver to Kansas"), received twin 7 Mar (GAPS171).
  - Luna = Missouri, new row C: 5059 (1 May, Lincoln, Nicolay-Hay "pressed by the Missouri members of Congress"),
    received twin 7 Mar. The witness column counts sent pages only (06 Apr-02 May by interpolation of an undated
    pointer); in use 07 Mar-01 May.
  - Indus = Stanton (signature/address slot), new row C: 5049 (13 Mar, OR 12 pt1 p.224), 5057 (28 Mar, OR 12 pt3 p.23),
    5068 (30 May, OR 12 pt1 p.647), 5067 (31 May, p.634), 5106 (11 Jul, OR 11 pt3 p.314), received twin 7 Mar.
- Conflicts logged, not merged (rule 4): Lamb = York River, 5091, 26 Jun (OR 11 pt3 p.259, Lincoln to McClellan "better
  toward York River than toward the James"; Lather = James there, Michigan on 7 Feb) -- one telegram, date-separated
  from Kansas (to 21 Mar). Luna = Shenandoah, 5061, 25 May (OR 11 pt1 p.31, GAPS147) against Missouri 7 Mar-1 May,
  date-separated by 24 days; Luna 4984 (15 Feb, "keep luna quiet", Nicolay) unprinted. Indus = Stanton overlaps Indus =
  Fredericksburg 25 May-17 Jul in date; the two never share a slot (Stanton: signature/address, 6 telegrams;
  Fredericksburg: place in the body, 5076 8 Jun "remainder by land from Fredericksburg", OR 12 pt1 p.97, added to the
  witness table), so the key reads it by slot.
- Not aligned: Koran 4960/4961 (2 Feb), 4973, 4979 (12 Feb, question only, GAPS187), 4982, 5004 ("Koran River", 20
  Feb); Indus 5056 (26 Mar, OR 53, not fetched). OR page numbers are running heads, +/-1.
- `print/key_dates.py --check` 0, `decode.py --check` 0; `print/residue_decode.py --check` 1 (stale, expected after the key change; the dmQuery `transc` field was not hash-matched to pages_manifest.tsv, 0 of 58 sha256 equal, so the regeneration step should use the per-item API text as before). Requests: hdl.huntington.org 1, archive.org 7, be-api 3.
  No vision, no subagents.

## GAPS197-eckert-1862 (3 Oct 2026, account-4): residue regenerated with the GAPS191 key

- Input: the 58 residue page texts re-fetched one per item from the CONTENTdm item API (58 requests + 1 retry for 5016,
  1.6 s apart), all 58 sha256-equal to print/residue/pages_manifest.tsv; the three received-ledger dmQuery files
  re-fetched, sha256-equal to received_manifest.tsv. Not committed (their credit; re-fetch as in the manifests).
- `print/residue_decode.py --write`: key.md tokens C 146 -> 155, I 38 -> 36, M 86 -> 82; oov 863 -> 860 (pages 58,
  entries 124). Pages changed: 4973, 4979, 4982, 4984, 5056, 5059. Judge unchanged: real_full -1.037 vs real_p05 -0.829
  FAIL, shuffled_key_full -1.037 FAIL (en corpus, fold caveat); no page reaches 'ready'.
- Rule 4 on the new values: Luna = Missouri reads C only on 01 May (5059, twice; the witness itself); 15 Feb 4984 "keep
  luna quiet" now shows [Missouri] but is graded M (outside the 06 Apr-02 May row range; unprinted). Lamb: two tokens,
  12 Feb, Kansas at C; no Lamb token after 27 Mar in the residue, so York River (26 Jun) never applies. Indus: one token,
  5056 (26 Mar) "signed Indus" -- signature slot, inside 13 Mar-11 Jul, reads Stanton at C, matching the witness slot;
  no body-slot Indus in the residue. Koran -> Ohio: 2 Feb tokens stay M (before 05 Feb).
- No-M candidates (`print/residue_candidates.py --write`): 31 entries, byte-identical to the committed candidates.tsv --
  every changed entry still carries another M token. No VERIFY-ECK item changes.
- `print/received_match.py` crashed on key.md's fourth (scope) field added by GAPS181; fixed (`*_` unpack) and
  regenerated: 124 sent entries (was 122, page 4979 added by GAPS181), twins 2 (unchanged), null p99 0, control (a) 60/60.
- Checks: decode.py 0, key_dates.py 0, residue_decode.py 0, residue_candidates.py 0, received_match.py 0,
  received_twin_check.py 0 (8/8 vs shuffled p99 1). No vision, no subagents. Requests: hdl.huntington.org 62.

## Remaining gaps (finish-or-blocker pass, GAPS191 + GAPS197, 3 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82 (print/residue, GAPS197 with the GAPS191 key)
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; every OR volume that could hold Feb-Jul 1862 telegrams grepped and aligned (GAPS113-GAPS153), received ledgers read (GAPS171), page 4979 checked (GAPS187), sent-side witnesses for Koran/Lamb/Luna/Indus folded into key.md (GAPS191); residue regenerated with that key 3 Oct 2026 (GAPS197: C 155, I 36, M 82, oov 860; candidates unchanged at 31); next: the 1864 sent-ledger pilot (gap 3) is the cheapest route to more readable entries, ~$6
- residue code words not fixed by any known plaintext - blocker: open-codes; about 860 oov tokens remain (GAPS197); conflicts Lamb (Kansas/York River), Luna (Missouri/Shenandoah) are date-separated, Indus split by slot; the table-change dates stay unwitnessed between 21 Mar and 25 May
- 1863-67 sent ledgers at grade H - blocker: not-attempted; filled-in cipher books exist at the Huntington (section 5); next: pilot one 1864 sent ledger (mssEC 18 or 19) against mssEC 41-46 (Cipher No. 1), ~$6

## Escalation (GAPS191, 3 Oct 2026)
- [x] siblings: received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171); its 7 Mar twin now paired with sent-side witnesses (GAPS191)
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [ ] known-keys: no filled-in book for Feb 1862 (failure log); the 1863-67 books are the H route (gap 3, ~$6)
- [x] print: OR vols. 5, 7, 8, 9, 10 pt 1-2, 11 pt 1/3, 12 pt 1/3, 51 pt 1, 53, Nicolay-Hay, Grant Papers vol. 4 done; page 4979 done (GAPS187)
- [x] key-rebuild: Koran/Lamb/Luna/Indus done 3 Oct 2026 (GAPS191, held-out 20/23 vs p99 10); residue regenerated with it 3 Oct 2026 (GAPS197, M 86 -> 82, candidates unchanged)
- [n/a] image-check: the ten readings were reconciled against the image (reading.md, Reconciliation)
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 3 internal gaps; cheapest next: pilot one 1864 sent ledger (mssEC 18 or 19) against Cipher No. 1 (mssEC 41-46) at grade H, ~$6

## GAPS206-eckert-1862 (4 Oct 2026, STALE4 for account 4, account 1 worker): 1864 sent-ledger pilot, text route

- Premise: gap 3's image pilot was already done in the sibling folder ciphers/eckert-1864 (19-20 Sept 2026: mssEC 41 =
  Cipher No. 1 transcribed into key.md, 20 mssEC 19 entries read at H 298, C 8). This job ran what was not done: the text
  route (volunteer transcriptions of whole 1864 ledgers through that key, no new image reading) and the never-opened
  parallel volume mssEC 18 (object 10074). Pre-registered in PREREG-GAPS206.md, pushed (commit e774327e) before the fetch;
  its "clock read 01:52" line was typed, not read (rule 6) -- the commit order is the record: prereg 01:5x, data after.
- Data: three CONTENTdm dmQuery calls (mssEC 18, 19, 15; pilot1864/manifest.tsv with sha256; texts not committed, the
  volunteers' work). Script pilot1864/pilot.py (`--check` exits 1 if results.tsv/pages.tsv are stale); results in
  pilot1864/results.tsv. Statistic S = Cipher No. 1 code words (minus the 1000 commonest English words) per 100 tokens.
- S1 gate (positive control first): mssEC 19 (pages >= 21) median S 18.49 vs mssEC 15 (1862 null) p95 12.37 -- PASS.
- S2 known answer: the keyed meanings of eckert-1864's 20 image-reconciled entries recovered from the volunteer text of
  the same pointer: recall 0.975 (309/317) vs mismatched-page control mean 0.200, p95 0.262 -- PASS. (Lenient by
  design: a whole page against one entry; the control carries the same leniency.)
- S3 target: mssEC 18 median S 17.50 > N p95 12.37 -- in the Cipher No. 1 vocabulary; 313/400 pages above the null p95
  (mssEC 19: 306/381); weakest stretches pages 301-325 (10/25) and 376-400 (12/25), likely the 1865 tail or the other
  (No. 2 / old) vocabularies, not checked.
- S4 duplicate test: only 24 of 400 mssEC 18 pages share >= 3 distinct word 5-grams with any mssEC 19 page (threshold 3
  = max(3, 1862 null p99 1 + 1); null pages over threshold 1/158). mssEC 18 is not a copy of mssEC 19: about 376 pages
  of 1864-65 sent entries that the 20-entry pilot never touched, readable through the same key.
- Not done: no entry of mssEC 18 decoded or graded (measurement only; the volunteer text is unreconciled, so any reading
  from it is conditional on the transcription, rule 2). 0 vision, 0 subagents. Requests: hdl.huntington.org 3.
- Suggestion (not done, brief scope): the mssEC 18 decode belongs with the key in ciphers/eckert-1864; a lane may prefer
  to log it there.

## Remaining gaps (finish-or-blocker pass, GAPS206, 4 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82 (print/residue, GAPS197 with the GAPS191 key)
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; every OR volume that could hold Feb-Jul 1862 telegrams grepped and aligned (GAPS113-GAPS153), received ledgers read (GAPS171), page 4979 checked (GAPS187), sent-side witnesses folded into key.md (GAPS191), residue regenerated (GAPS197: C 155, I 36, M 82, oov 860); next: the 1864 ledgers (gap 3) are the cheaper route to more readable entries; for mssEC 15 itself, a received-ledger pass on mssEC 04-14 (not yet harvested) by the GAPS171 method, ~$2
- residue code words not fixed by any known plaintext - blocker: open-codes; about 860 oov tokens remain (GAPS197); conflicts Lamb, Luna date-separated, Indus split by slot; table-change dates unwitnessed between 21 Mar and 25 May
- 1863-67 sent ledgers at grade H - blocker: not-attempted; text route validated 4 Oct 2026 (GAPS206: volunteer text recall 0.975 vs control p95 0.262; mssEC 18 in Cipher No. 1 vocabulary, 376 of 400 pages not duplicated in mssEC 19); next: decode mssEC 18's volunteer text page by page with ciphers/eckert-1864/decode.py's key, list entries whose code words are all keyed, and print-check them against OR ser. I vols. 32-46 by date, ~$3

## Escalation (GAPS206, 4 Oct 2026)
- [x] siblings: received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171); parallel sent ledger mssEC 18 opened by text 4 Oct 2026 (GAPS206, 24/400 pages twinned in mssEC 19)
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [ ] known-keys: no filled-in book for Feb 1862 (failure log); the 1863-67 books are the H route, text route validated (GAPS206); next: mssEC 18 decode, ~$3
- [x] print: OR vols. 5, 7, 8, 9, 10 pt 1-2, 11 pt 1/3, 12 pt 1/3, 51 pt 1, 53, Nicolay-Hay, Grant Papers vol. 4 done; page 4979 done (GAPS187)
- [x] key-rebuild: Koran/Lamb/Luna/Indus done 3 Oct 2026 (GAPS191); residue regenerated (GAPS197)
- [n/a] image-check: the ten readings were reconciled against the image (reading.md, Reconciliation)
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 3 internal gaps; cheapest next: decode mssEC 18's volunteer text with the Cipher No. 1 key and print-check the fully keyed entries against OR ser. I vols. 32-46, ~$3

## A3V3-ECK18-eckert-1862 (4 Oct 2026, account 3 worker for LANE-A3V3): mssEC 18 volunteer text through Cipher No. 1, OR print check

Step run: GAPS206's Verdict. Script `ec18/ec18.py DATA_DIR OR_DIR --write|--check` (`--check` exit 0 three runs in a row;
imports ciphers/eckert-1864/decode.py, no private copy, decode.py unchanged). Data: mssEC 18 dmQuery re-fetched once (sha256
cb162574..., same as pilot1864/manifest.tsv; not committed); OR ser. I vols. 32-46, 41 IA `_djvu.txt` files (every part;
ids, sizes and sha256 in `ec18/or_volumes.tsv`; not committed, re-fetch). Outputs: `ec18/entries.tsv` (every entry: book,
key.md grades, oov, OR match), `ec18/matches.tsv`, `ec18/control.tsv`, `ec18/readings.md` (the 28 fully keyed entries).
- Premise found on the way (changes the brief's frame): mssEC 18 is not all Cipher No. 1. The entries to Beckwith (Grant)
  and other headquarters use Cipher No. 2 (the same printed words, other meanings: Pike = comma, Yard = period, Bard =
  Baltimore; ciphers/eckert-1864/key-no2.md). Read with key.md, 10 July 1864 Lincoln to Grant (Page 117) decodes Pike as
  [Cut off] and Bard as [Baton Rouge] at grade H, which is wrong. So each entry is first assigned a book by its punctuation
  and signature words (No. 1: unity, zebra, zodiac, walrus, webster, yoke, youth; No. 2: tulip, pike, yacht, yawl,
  yard(stick)). Known answer (`ec18.py --book-test`): eckert-1864's 23 image-read entries, 22 right, 0 wrong book, 1
  unassigned. mssEC 18: 671 entries on 351 pages with a dated header; book 1: 311, book 2: 168, unassigned 192 (old Stager
  vocabulary early in 1864, short entries).
- Fully keyed (book 1, >= 3 keyed tokens, 0 oov tokens): 28 entries, 7 Feb 1864 - 15 June 1865, H 370 (key.md rows read
  from mssEC 41), C 0, I 0, M 0 -- all conditional on the volunteer transcription (rule 2, not image-reconciled).
- Print check by date (>= 4 shared word 5-grams in one 400-word OR block AND the entry's clear date within 1500 words before
  it): 9 of the 28 found, 19 not found in OR ser. I vols. 32-46 by this method. Found (OR ser. I vol., page from the OCR
  running head, shared 5-grams): 9673.15 7 Feb 1864 Halleck to Grant, 32 pt 2 p. 347 (5); 9744.111 25 May 1864 Halleck to
  Steele, 34 pt 4 p. 28 (12); 9765.139 24 June 1864 Lincoln to Rosecrans, 34 pt 4 p. 536 (10); 9816.215 7 Aug 1864
  Halleck to Sherman, 38 pt 5 p. 409 (4); 9864.317 13 Oct 1864 to Schofield, 39 pt 3 p. 249 (6); 9878.351 28 Oct 1864,
  39 pt 3 p. 476 (9); 9885.368 2 Nov 1864 to Stevenson, 43 pt 2 p. 528 (7); 9911.425 9 Dec 1864 Halleck to Thomas, 45 pt 2
  p. 114 (27); 9965.539 27 Feb 1865 to Morris, 46 pt 2 p. 727 (18). Pages are OCR running heads, not checked against
  the page image. Not found: 9730.87, 9731.89, 9812.208, 9855.295, 9858.300, 9866.320, 9901.399, 9908.417, 9928.458,
  9939.484, 9943.494, 9947.505, 9948.507, 10002.578, 10020.609, 10026.621, 10027.623, 10028.625, 10031.632 (several are
  Apr-June 1865, which falls partly in vols. 47-49, not searched).
- Control (rule 3, the date condition is the only thing a permutation changes): 28 entries, real dates 9 vs permuted dates
  mean 0.25, max 1 (20 permutations, seed 18); the brief's 20-entry draw (seed 18) 6 real vs 1 with dates rotated. Over all
  671 entries (any book; plain stretches match even when the book is wrong): 286 real vs 3.00 permuted (5 permutations),
  by book 1: 141, 2: 82, unassigned: 63.
- Meanings against print (book-1 entries with an OR match, a keyed meaning counts when one of its content words is in the
  OR window of the same telegram): 1549/2319 = 0.668, against another matched entry's window 890/2319 = 0.384; book-2
  entries read with key.md 454/2032 = 0.223 (below the control: the wrong book). So the No. 1 key reads through the
  volunteer text well above chance but far from clean: e.g. 9744.111 reads "a body of [General-in-Chief]'s" where OR
  prints "a body of Indians" and 9765.139 "[Report] to me" where OR prints "write to me" -- a volunteer misreading or a
  row collision, unsettled without the image. H here means "the key row is H"; it is not a check that the volunteer
  wrote the right code word.
- Judge (rule 7): `tools/judge_plaintext.py specs/eckert-1862.json --file ciphers/eckert-1862/ec18/readings.md` ->
  "FAIL language: score=-1.147, null_p99=-2.125, real_p05=-0.841, real_median=-0.81, mode=both, N=7211" (the file
  carries bracket markup and prose; the en judge is of unknown reliability, tools/data/en/README.md; GAPS132 found real
  and shuffled-key within 0.003 on this ledger family). Reported as a FAIL.
- Not done: no image check of any entry; no C-grade alignment of the 286 print-matched entries; the 168 book-2 entries
  not read with key-no2.md; OR vols. 47-49 (Jan-June 1865) not searched. 0 vision, 0 subagents. Requests:
  hdl.huntington.org 1, archive.org 42 (1 advancedsearch + 41 djvu), >= 1.6 s apart.

- LS3-R18 (8 Oct 2026, for LANE ST-LEDGER-3), see ciphers/eckert-1864/NOTES.md "## LS3-R18": of the 19 "not found" entries, four of the ten re-searched are in print after all (9730.87, 9731.89, 9908.417, 9939.484; OR vols. 36, 37, 41/45, 46; A3V3's meaning-based 5-gram test missed paraphrase) and 9731.89 is Cipher No. 9, not No. 1; six read from the image as book 1 (E79-E84); 21-22 Apr 1864 pages 48-51 image-read.

LS3-R18b (8 Oct 2026): the last seven keyed entries (9943.494, 9948.507, 10002.578, 10026.621, 10027.623, 10028.625, 10031.632) are worked in ciphers/eckert-1864/NOTES.md "## LS3-R18b"; 10028.625 is a ledger-"9" entry, not book 1.

## Remaining gaps (finish-or-blocker pass, A3V3-ECK18, 4 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82 (print/residue, GAPS197 with the GAPS191 key); mssEC 18: 28 fully keyed Cipher No. 1 entries at H 370 from the volunteer text, 9 of them in OR (A3V3-ECK18)
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; every OR volume that could hold Feb-Jul 1862 telegrams grepped and aligned (GAPS113-GAPS153), received ledgers read (GAPS171), page 4979 checked (GAPS187), sent-side witnesses folded into key.md (GAPS191), residue regenerated (GAPS197: C 155, I 36, M 82, oov 860); next: a received-ledger pass on mssEC 04-14 (not yet harvested) by the GAPS171 method, ~$2
- residue code words not fixed by any known plaintext - blocker: open-codes; about 860 oov tokens remain (GAPS197); conflicts Lamb, Luna date-separated, Indus split by slot; table-change dates unwitnessed between 21 Mar and 25 May
- 1863-67 sent ledgers at grade H - blocker: not-attempted; mssEC 18 decoded through Cipher No. 1 by text 4 Oct 2026 (A3V3-ECK18: 28 fully keyed, 9 in OR vs 0.25 date-permuted; book-1 meanings in print 0.668 vs 0.384 control); next: read the 168 book-2 entries with ciphers/eckert-1864/key-no2.md through the same ec18.py (add a --book 2 option) and print-check them plus the 19 unfound book-1 entries against OR ser. I vols. 47-49, ~$3

## Escalation (A3V3-ECK18, 4 Oct 2026)
- [x] siblings: received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171); parallel sent ledger mssEC 18 opened by text 4 Oct 2026 (GAPS206) and decoded through Cipher No. 1 (A3V3-ECK18)
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [ ] known-keys: no filled-in book for Feb 1862 (failure log); mssEC 18 book-2 entries not yet read with the No. 2 book (key-no2.md, mssEC 47); next: ec18.py --book 2, ~$3
- [ ] print: OR vols. 5, 7, 8, 9, 10 pt 1-2, 11 pt 1/3, 12 pt 1/3, 51 pt 1, 53, Nicolay-Hay, Grant Papers vol. 4 done; OR vols. 32-46 done for mssEC 18 (A3V3-ECK18); vols. 47-49 for its 1865 entries not yet; next: add them to ec18/or_volumes.tsv, ~$1
- [x] key-rebuild: Koran/Lamb/Luna/Indus done 3 Oct 2026 (GAPS191); residue regenerated (GAPS197)
- [ ] image-check: the ten mssEC 15 readings were reconciled against the image (reading.md); the 9 print-matched mssEC 18 entries were not; next: image-reconcile them with the eckert-1864 method, ~$4
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 3 internal gaps; cheapest next: read mssEC 18's 168 Cipher No. 2 entries with key-no2.md through ec18.py and print-check against OR ser. I vols. 32-49, ~$3

## A3V3-ECK2-eckert-1862 (4 Oct 2026, account 3 worker for LANE-A3V3): mssEC 18 book-2 entries through Cipher No. 2, OR vols. 32-49

Step run: A3V3-ECK18's next step. `ec18/ec18.py` extended in place with `--book 2` (reads every entry with
ciphers/eckert-1864/key-no2.md, mssEC 47, through the same imported decode.py; writes `entries_b2.tsv`, `matches_b2.tsv`,
`control_b2.tsv`, `readings_b2.md`); the book-1 outputs were re-run unchanged in method against the enlarged OR set.
Both `--check` exit 0 (book 1 and `--book 2`). Data: mssEC 18 dmQuery re-fetched once (sha256 cb162574..., matches
pilot1864/manifest.tsv); the 41 OR files of vols. 32-46 re-fetched (all sha256 match or_volumes.tsv) plus 7 new: vols. 47
pts 1-3, 48 pts 1-2, 49 pts 1-2 (rows added to `ec18/or_volumes.tsv`; 47.2/47.3 are the `rootrich` scans because
warofrebellion472unit/473unit answered 503 twice; title pages read "Part II-Correspondence" / "Part III" confirm them).
- Book 2, fully keyed (book 2, >= 3 keyed tokens, 0 oov tokens): 17 of the 168 book-2 entries, 27 Feb 1864 - 1 June 1865;
  grades from key-no2.md's own rows: H 253 (read from mssEC 47), C 6, I 7, M 0 -- all conditional on the volunteer
  transcription (rule 2, not image-reconciled). "0 oov" does not mean every code word is keyed: unkeyed code names that are
  English words pass (9823.230 reads "Kettle's [Corps] and Fitz Hugh Javelin's [Cavalry] have [Fire]ed through
  [Culpepper]" where OR 42 pt 2 p. 291 prints "Longstreet's corps and Fitzhugh Lee's cavalry have passed through Culpeper").
- Print check by date (same matcher as A3V3-ECK18, OR ser. I vols. 32-49): 12 of 17 found, 5 not found. Found (vol. part,
  page from the OCR running head, shared 5-grams): 9680.31 27 Feb 1864 to Grant, 32.2 p. 478 (31); 9729.85 3 May 1864 to
  Grant, 34.3 p. 409 (17); 9798.182 19 July 1864 to Grant, 37.2 p. 382 (14); 9823.230 19 Aug 1864 to Grant, 42.2 p. 291
  (17); 9837.257 8 Sept 1864 to Grant, 41.3 p. 71 (15); 9848.277 21 Sept 1864 to Grant, 39.2 p. 434 (22); 9898.393 18 Nov
  1864 to Sheridan, 43.2 p. 640 (7); 9902.402 30 Nov 1864 to Sheridan, 43.2 p. 708 (9); 9910.424 8 Dec 1864 to Grant, 45.2
  p. 75 (11); 9961.531 18 Feb 1865 to Canby, 49.1 p. 742 (15); 10010.593 17 May 1865 to Halleck, 46.3 p. 1161 (21);
  10027.622 1 June 1865 to Canby, 48.2 p. 713 (6). Pages are OCR running heads, not checked against the page image. Not
  found by this method in vols. 32-49: 9681.34 (3 Mar 1864, for Meade), 9701.64 (9 Apr 1864), 9781.163 (9 July 1864),
  9831.247 (3 Sept 1864), 9845.272 (19 Sept 1864).
- Control (rule 3; the date condition is the only thing a permutation changes, so it can fail differently): target 12 vs
  date-permuted mean 0.75, max 2 (20 permutations, seed 18); 17-entry draw (seed 18; all 17, since < 20) 12 real vs 0
  with dates rotated. All 671 entries read with key-no2.md: 304 real vs 3.40 permuted (book 1 121, book 2 112, ? 71) --
  book-2 entries match print 112 times with their own key vs 88 with key.md, book-1 entries 121 with key-no2.md vs 165 with
  key.md.
- Meanings against print (book-2 entries with an OR match; a keyed meaning counts when a content word is in the OR window
  of the same telegram): 1681/2349 = 0.716 with key-no2.md, against another matched entry's window 971/2349 = 0.413;
  book-1 entries read with key-no2.md 587/2691 = 0.218 (the wrong book, below the control). Side by side with Cipher No. 1:
  book 1 with key.md 0.669 vs 0.379 (vols. 32-49), book 2 with key.md 0.219.
- Book 1 against vols. 47-49 (A3V3-ECK18's 19 unfound): 5 more found, all in vol. 48: 9947.505 27 Jan 1865, 48.1 p. 646
  (6); 10002.578 1 May 1865, 48.2 p. 278 (17); 10020.609 24 May 1865, 48.2 p. 573 (15); 10026.621 1 June 1865, 48.2 p. 716
  (21); 10027.623 2 June 1865, 48.2 p. 716 (16). Book 1 now 14 of 28 vs permuted mean 0.45 (was 9 vs 0.25 on vols. 32-46);
  20-entry draw 8 real vs 1 rotated; all entries 326 vs 3.80. Still not found in vols. 32-49: 9730.87, 9731.89, 9812.208,
  9855.295, 9858.300, 9866.320, 9901.399, 9908.417, 9928.458, 9939.484, 9943.494, 9948.507, 10028.625, 10031.632.
- Judge (rule 7): `tools/judge_plaintext.py specs/eckert-1862.json --file ciphers/eckert-1862/ec18/readings_b2.md` ->
  "FAIL language: score=-1.106, null_p99=-2.111, real_p05=-0.85, real_median=-0.811, mode=both, N=5121"; readings.md
  (book 1, re-run) -> "FAIL language: score=-1.146, null_p99=-2.123, real_p05=-0.84, real_median=-0.81, mode=both, N=7326"
  (bracket markup and prose in the file; the en judge is of unknown reliability, tools/data/en/README.md). Reported as FAILs.
- Not done: no image check; no C-grade alignment of the print-matched entries against OR; the 192 unassigned entries not
  read with either key. 0 vision, 0 subagents. Requests: hdl.huntington.org 1, archive.org 59 (41 + 7 djvu, 9 HEAD probes,
  1 advancedsearch, 1 retry), >= 1.5 s apart.

## Remaining gaps (finish-or-blocker pass, A3V3-ECK2, 4 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82 (print/residue, GAPS197 with the GAPS191 key); mssEC 18: 28 fully keyed Cipher No. 1 entries at H 370 (14 in OR vols. 32-49) and 17 fully keyed Cipher No. 2 entries at H 253 C 6 I 7 (12 in OR), all from the volunteer text (A3V3-ECK18, A3V3-ECK2)
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; every OR volume that could hold Feb-Jul 1862 telegrams grepped and aligned (GAPS113-GAPS153), received ledgers read (GAPS171), page 4979 checked (GAPS187), sent-side witnesses folded into key.md (GAPS191), residue regenerated (GAPS197: C 155, I 36, M 82, oov 860); next: a received-ledger pass on mssEC 04-14 (not yet harvested) by the GAPS171 method, ~$2
- residue code words not fixed by any known plaintext - blocker: open-codes; about 860 oov tokens remain (GAPS197); conflicts Lamb, Luna date-separated, Indus split by slot; table-change dates unwitnessed between 21 Mar and 25 May
- 1863-67 sent ledgers at grade H - blocker: not-attempted; mssEC 18 read by text with both books (A3V3-ECK18, A3V3-ECK2: book 1 14/28 in OR vs 0.45 permuted, book 2 12/17 vs 0.75; meanings in print 0.669 / 0.716 vs 0.379 / 0.413); next: C-grade alignment of the 26 print-matched fully keyed entries against the OR text (or_align.py method) to separate volunteer misreadings from key-row errors, ~$3
- 192 unassigned mssEC 18 entries (no punctuation or signature marker) - blocker: not-attempted; the book rule needs a No. 1 or No. 2 marker word and these carry none; next: assign a book by which key's meanings match print better on the 71-73 print-matched ones (ec18.py option), ~$2

## Escalation (A3V3-ECK2, 4 Oct 2026)
- [x] siblings: received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171); parallel sent ledger mssEC 18 opened by text 4 Oct 2026 (GAPS206), read with Cipher No. 1 (A3V3-ECK18) and No. 2 (A3V3-ECK2)
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [ ] known-keys: no filled-in book for Feb 1862 (failure log); mssEC 18 book-2 entries read with key-no2.md 4 Oct 2026 (A3V3-ECK2); the 192 unassigned entries not yet tried against both books; next: ec18.py book assignment by print agreement, ~$2
- [x] print: OR vols. 5, 7, 8, 9, 10 pt 1-2, 11 pt 1/3, 12 pt 1/3, 51 pt 1, 53, Nicolay-Hay, Grant Papers vol. 4 done; OR ser. I vols. 32-49 done for mssEC 18 (A3V3-ECK18, A3V3-ECK2)
- [x] key-rebuild: Koran/Lamb/Luna/Indus done 3 Oct 2026 (GAPS191); residue regenerated (GAPS197)
- [ ] image-check: the ten mssEC 15 readings were reconciled against the image (reading.md); the 26 print-matched fully keyed mssEC 18 entries were not; next: image-reconcile them with the eckert-1864 method, ~$4
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 4 internal gaps; cheapest next: C-grade alignment of the 26 print-matched fully keyed mssEC 18 entries against OR, ~$3

## A3V3-ECKC-eckert-1862 (4 Oct 2026, account 3 worker for LANE-A3V3): C-grade alignment of the 26 print-matched mssEC 18 entries against OR

Step run: A3V3-ECK2's next step. Script `ec18/ec18_align.py DATA_DIR OR_DIR --write|--check` (`--check` exit 0 twice in a
row; imports ec18.py and ciphers/eckert-1864/decode.py, no private copy). Method: the folder's or_align.py method (word-level
difflib diff of the decoded entry against the OR text from 120 words before the match anchor to 400 after; both sides are
English words, so tools/interlinear_align.py, which aligns cipher groups to letters, does not fit). Each keyed token is
AGREE (the print fixes it: grade C), CONFLICT (at most 3 ledger words opposite at most 4 other printed words), COLLISION
(the code word itself stands in the print: the clerk wrote the word in clear and the lookup over-read it), PARTIAL or
UNFIXED (opposite nothing or a long misaligned block; keeps its key grade). Name meanings are scored on the surname, time
and numeral meanings on their digits/number words. Outputs: `ec18/align_tokens.tsv` (every keyed token, plus plain words
opposite other printed words), `ec18/align_entries.tsv`, `ec18/align_summary.tsv`. Data: the same vol18.json (sha256
cb162574..., matches pilot1864/manifest.tsv) and the 16 OR files named in the two matches files (all sha256 match
or_volumes.tsv); not committed.
- Agreement, target vs control side by side (rule 3; the control changes only the print window, so it can fail
  differently): keyed word tokens AGREE 209/281 = 0.744 against the entry's own OR telegram, 48/281 = 0.171 against a
  different OR telegram of the same week (nearest dated heading 1-3 days from the entry's date, > 700 words from the true
  anchor, same volume); per entry the target beats its control in 26 of 26 (per-entry rates in align_entries.tsv: target
  0.43-1.00, control 0.00-0.67). Before the three key additions below (which this same alignment supplied, so they are
  circular here) and before the possessive fix: 202/274 = 0.737 vs 47/274 = 0.172. Numerals: 12/37 agree (most numeral
  tokens are the date and time heads, which the print sets in digits above the telegram and the window often misaligns).
- Grades of the 26 entries' keyed tokens after alignment: C 221 (print fixes the key value), H 156 (key row only: print
  window misaligned, or no printed counterpart, or punctuation/signature, which OR's OCR punctuation cannot score),
  I 6, M 0. The 4 CONFLICT + 9 COLLISION + 7 PARTIAL tokens keep their key grade and are listed here, not resolved.
- Collisions (the code word is an English word the clerk wrote in clear; the decode over-read it), 9: whack (in
  "bush whack hers" = bushwhackers), white (OR "write"; a volunteer misreading of "write" or the code word for Report),
  summit, animals, persons, subject, opinion, passed, Hotel ("beat Hotel" = "be at a hotel"), John ("John sons" =
  Johnson's); plus Dodge (written in clear, key.md Dodge = McMinnville) in 9947.505 and 10020.609 by inspection. These
  are reading errors of the decode on the volunteer text, not key errors: "H" on such a token means only that the key row
  is H (as A3V3-ECK18 already warned).
- Key value vs print, data conflicts (rule 4; two witnesses disagree, not settled by this job): Lehigh, key.md
  p.17 l.6 (mssEC 41) = Maj Gen S. A. Hurlbut, read by 9947.505 (27 Jan 1865, Halleck to Dodge, St Louis) where OR I/48
  pt 1 p.646 prints "general Canby"; lehigh in 10020.609 (24 May 1865, Grant to Pope) where OR I/48 pt 2 p.573 prints
  "can be" ("as soon as transportation can be provided"); weigh (key.md Threaten) in 9965.539 where OR I/46 pt 2 p.727
  prints "on the way" (a homophone in clear is as likely). Four further CONFLICTs (Morgan, Magic, plank, Brown) sit in date/
  time heads and are window misalignments by inspection (Brown = 1 against "i 1865", OCR for "1, 1865").
- Possessives: decode.py's lookup does not strip "'s", so ec18.py leaves Kettle's, Javelin's, lantern's, flora's unread
  (key-no2.md has Kettle = Longstreet, Javelin = Lee, Lantern = Augur, Flora = Sherman, all H); the aligner strips it and
  the print confirms all four (C). Follow-up: an option in ciphers/eckert-1864/decode.py, with a test, ~$1.
- Key additions (grade C, one witness each, conditional on the volunteer transcription; values the key lacked and the print
  fixes): key.md section 7 "Handle = Maj Gen J. B. Hood (Confederate)" (9864.317, 13 Oct 1864, OR I/39 pt 3 p.249 "any
  forces that Hood may send north"); key-no2.md section 8 "Harry = Washington" (9902.402, 30 Nov 1864, OR I/43 pt 2 p.708
  "left for Washington") and "author = Chattahoochee" (9680.31, 27 Feb 1864, OR I/32 pt 2 p.478 "north of the
  Chattahoochee River"). Other plain-replaced words in align_tokens.tsv (Kearney in a tail outside the print; "pot." =
  private; Kay Leet, a signature tail where OR prints a different signer) are not code words or are not fixed by print. eckert-1864
  decode.py --check and decode_no2.py --check stay current after the additions; ec18.py outputs re-written (see below).
- OR pages are OCR running heads, not checked against the page image. Not done: no image check of any entry (the
  collisions and the Lehigh conflict are the first things an image check should settle); the 192 unassigned entries.
  0 vision, 0 subagents.
- Regenerated after the key additions (rule 7; each `--check` was current before the additions and stale after): `ec18.py
  --write` (book 1: fully keyed grades H 370 C 2; meanings in print 1773/2647 = 0.670 vs control 0.380; OR matches 14 vs
  permuted unchanged) and `--book 2 --write` (H 253 C 8 I 7; 0.716 vs 0.414; 9902.402 now shares 11 5-grams with OR
  instead of 9), `pilot1864/pilot.py --write` (pages.tsv: mssEC 18 page S-rates up 0.4-0.7 points where Handle occurs),
  then `ec18_align.py --write`; all five `--check` current, eckert-1864 `decode.py --check` and `decode_no2.py --check`
  current. Requests: hdl.huntington.org 3 (vol18, vol19, vol15 dmQuery), archive.org 48 `_djvu.txt` (all sha256 match
  or_volumes.tsv), >= 1.6 s apart.

## Remaining gaps (finish-or-blocker pass, A3V3-ECKC, 4 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82 (print/residue, GAPS197 with the GAPS191 key); mssEC 18: 28 fully keyed Cipher No. 1 entries (14 in OR vols. 32-49) and 17 fully keyed Cipher No. 2 entries (12 in OR), from the volunteer text; the 26 print-matched ones aligned to OR: keyed tokens C 221, H 156, I 6 (A3V3-ECKC: 0.744 agree vs 0.171 same-week control, 26/26 entries above control)
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; every OR volume that could hold Feb-Jul 1862 telegrams grepped and aligned (GAPS113-GAPS153), received ledgers read (GAPS171), page 4979 checked (GAPS187), sent-side witnesses folded into key.md (GAPS191), residue regenerated (GAPS197: C 155, I 36, M 82, oov 860); next: a received-ledger pass on mssEC 04-14 (not yet harvested) by the GAPS171 method, ~$2
- residue code words not fixed by any known plaintext - blocker: open-codes; about 860 oov tokens remain (GAPS197); conflicts Lamb, Luna date-separated, Indus split by slot; table-change dates unwitnessed between 21 Mar and 25 May
- 1863-67 sent ledgers at grade H - blocker: not-attempted; mssEC 18 read by text with both books and the 26 print-matched entries aligned to OR (A3V3-ECK18, A3V3-ECK2, A3V3-ECKC); 9 collisions (plain English words over-read as code) and the Lehigh / weigh key-vs-print conflicts open; next: decode.py possessive option ("Kettle's") plus a collision guard (a code word left plain when the clear reading fits the surrounding words), with an offline test, then re-run ec18.py, ~$2
- 192 unassigned mssEC 18 entries (no punctuation or signature marker) - blocker: not-attempted; the book rule needs a No. 1 or No. 2 marker word and these carry none; next: assign a book by which key's meanings match print better on the 71-73 print-matched ones (ec18.py option), ~$2

## Escalation (A3V3-ECKC, 4 Oct 2026)
- [x] siblings: received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171); parallel sent ledger mssEC 18 opened by text 4 Oct 2026 (GAPS206), read with Cipher No. 1 (A3V3-ECK18) and No. 2 (A3V3-ECK2)
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [ ] known-keys: no filled-in book for Feb 1862 (failure log); mssEC 18 book-2 entries read with key-no2.md 4 Oct 2026 (A3V3-ECK2); the 192 unassigned entries not yet tried against both books; next: ec18.py book assignment by print agreement, ~$2
- [x] print: OR vols. 5, 7, 8, 9, 10 pt 1-2, 11 pt 1/3, 12 pt 1/3, 51 pt 1, 53, Nicolay-Hay, Grant Papers vol. 4 done; OR ser. I vols. 32-49 done for mssEC 18 (A3V3-ECK18, A3V3-ECK2); the 26 matches aligned word by word (A3V3-ECKC)
- [x] key-rebuild: Koran/Lamb/Luna/Indus done 3 Oct 2026 (GAPS191); residue regenerated (GAPS197); Handle (key.md), Harry and author (key-no2.md) added at C from the OR alignment (A3V3-ECKC)
- [ ] image-check: the ten mssEC 15 readings were reconciled against the image (reading.md); the 26 print-matched fully keyed mssEC 18 entries were not; first the 9 collisions and the Lehigh (9947.505, 10020.609) and weigh (9965.539) conflicts; next: image-reconcile those entries with the eckert-1864 method, ~$4
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 4 internal gaps; cheapest next: decode.py possessive option and collision guard, then re-run ec18.py, ~$2

## RUN3-ECK62-eckert-1862 (4 Oct 2026, account 1 worker for LANE-RUN3): possessive option, collision guard, book assignment

Rules pre-registered and pushed before any number was computed: `ec18/PREREG-ECK62.md` (commit 580c34e6, 08:5x UTC).
- (a) Shared code, no private copy: `ciphers/eckert-1864/decode.py` gains `lookup(..., possessive=True)` ("Kettle's" ->
  [Longstreet]'s) and `CollisionGuard` (rule J: the code word joined to a plain neighbour makes a corpus word of >= 7
  letters, count >= 2; rule B: bigram support for the clear word P >= 3 and P > 2x the support for the meaning). Both are off
  by default; eckert-1864 `decode.py --check` and `decode_no2.py --check` stay current. Offline test
  `tools/tests/test_eckert_decode.py` (9 tests, including what the guard must NOT block: a meaning that fits the context
  better, numerals, options off). Bug found in the run and fixed: a possessive numeral ("Brown's" = 1 in Cipher No. 2) sent
  the numeral-run loop into an infinite loop; the loop now uses the same lookup (test added). Guard corpus: OR ser. I
  1862 volumes, IA `warofrebellionco0007vari`, `warofrebellion09secrrich`, `1warofrebellion10secrrich`,
  `2warofrebellion10secrrich`, `1warofrebellion11secrrich`, `3warofrebellion11secrrich`, `1warofrebellion12secrrich`,
  `3warofrebellion12secrrich` (`_djvu.txt`, not committed). Deviation from the PREREG text: it named
  `warofrebellion10/11/12secrrich`, which do not exist on IA (error pages, 146 KB); the corpus used is the part-numbered
  identifiers for the same 1862 volumes (vols. 7, 9-12) the folder already uses in print/. None can print a 1864-65 telegram.
- Guard known answer (`ec18.py --guard-test`, `ec18/guard_test.tsv`; A3V3-ECKC's align_tokens.tsv statuses): COLLISION
  word tokens caught 6 of 9 (whack J, John J, summit B, subject B, opinion B, passed B; missed: white, animals, Hotel);
  AGREE word tokens wrongly guarded 0 of 198 (CONFLICT 0/4, PARTIAL 0/6, UNFIXED 0/38). Pre-registered gate (FP <= 5% of
  AGREE) passed, so the committed ec18 outputs now use `--possessive --guard DIR62`. Caveat: the rule was written after
  seeing the A3V3-ECKC collision examples, so 6/9 is not an out-of-sample figure; the 0/198 FP is the binding number.
- (b) ec18.py re-run, both books (`ec18.py DATA OR --possessive --guard DIR62 --check` and the same with `--book 2`, both
  current; flags are recorded in control*.tsv). Guarded tokens over all 671 entries: 182 with key.md, 440 with key-no2.md
  (listed in `ec18/guard.tsv`, `ec18/guard_b2.tsv`). Out-of-sample check on the print-matched entries (not in the known-answer
  set): the meanings the guard removed occur in their own telegram's print about as often as in an unrelated telegram's window
  (book 1: 6/22 vs 5/22; book 2: 13/87 vs 10/87), i.e. they behave like noise, not like read code. Meanings in print: book 1
  0.670 -> 0.673 (control 0.380 -> 0.381); book 2 0.716 -> 0.737 (control 0.414 -> 0.425). Fully keyed: book 1 28 entries,
  H 370 C 2 -> H 369 C 2 (the 9765.139 whack token now plain); book 2 17 entries, H 253 C 8 I 7 unchanged. OR matches 14 and
  12 unchanged (9885.368 now shares 12 5-grams, was 7, since "summit Point" is left as written); ec18_align.py re-written for that
  matches.tsv change: align_tokens.tsv/align_entries.tsv regenerated, align_summary.tsv unchanged, `--check` current).
  The 9 collisions, before -> after: whack, summit, subject, opinion, passed, John now left as written; white, animals, Hotel
  still read [Report], [Monroe], [Weldon]; persons (numeral, out of scope by construction) still [5]. Dodge (by inspection):
  guarded in 9951.514 (rule B), not in 9947.505 or 10020.609. Data conflicts unchanged (rule 4, logged, not settled): Lehigh
  (9947.505 "general Canby", 10020.609 "can be") and weigh (9965.539 "on the way") are not guarded; they need the image.
- (c) Book assignment for the 192 '?' entries (`ec18.py --assign`, `ec18/assign.tsv`, `ec18/assign_summary.tsv`): 78 are
  print-matched. Known answer on the 287 print-matched entries whose book the markers fix: 257/267 decided right (0.963),
  accuracy gate passed. The pre-registered control fails: scored against an unrelated telegram's window, the rule still
  decides 38/78 '?' entries (41/78 with the real window) and gets 188 of the known-answer entries right. So the rule tells
  the books apart by which key gives Official-Records-like meanings in general, not by agreement with the entry's own
  telegram. Under PREREG (c) the assignment is therefore not used: assign.tsv keeps the scores and every '?' entry stays
  '?'. The numeric "near" threshold (control decided count > half the real count) was fixed after the first run (09:46 UTC),
  but at 38 vs 41 the result is the same under any reasonable threshold. Next instrument (named, not run): a print-free
  assignment (meaning words against a general OR vocabulary, scored on the marker-known entries as the known answer, with a
  shuffled-key control) -- pre-register before running.
- Grades: no H added or changed except the one whack token removed; H only where mssEC 41 / mssEC 47 gives the value.
  0 vision, 0 subagents. Requests: hdl.huntington.org 1 (vol18 dmQuery, sha256 matches), archive.org 61 (48 OR 32-49
  djvu, all sha256 match or_volumes.tsv; 5 + 6 + 2 error-page fetches for the 1862 corpus), >= 1.6 s apart.

## Remaining gaps (finish-or-blocker pass, RUN3-ECK62, 4 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82 (print/residue, GAPS197 with the GAPS191 key); mssEC 18: 28 fully keyed Cipher No. 1 entries (14 in OR, H 369 C 2) and 17 fully keyed Cipher No. 2 entries (12 in OR), from the volunteer text, now read with the possessive option and collision guard (RUN3-ECK62); the 26 print-matched ones aligned to OR (A3V3-ECKC)
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; every OR volume that could hold Feb-Jul 1862 telegrams grepped and aligned (GAPS113-GAPS153), received ledgers read (GAPS171), page 4979 checked (GAPS187), sent-side witnesses folded into key.md (GAPS191), residue regenerated (GAPS197: C 155, I 36, M 82, oov 860); next: a received-ledger pass on mssEC 04-14 (not yet harvested) by the GAPS171 method, ~$2
- residue code words not fixed by any known plaintext - blocker: open-codes; about 860 oov tokens remain (GAPS197); conflicts Lamb, Luna date-separated, Indus split by slot; table-change dates unwitnessed between 21 Mar and 25 May
- 1863-67 sent ledgers at grade H - blocker: not-attempted; mssEC 18 read by text with both books, aligned to OR, possessive and guard applied (RUN3-ECK62: 6/9 collisions removed, 0/198 false guards); white, animals, Hotel and the Lehigh / weigh conflicts stay open; next: image-reconcile those entries (9765.139, 9911.425, 10010.593, 9947.505, 10020.609, 9965.539) with the eckert-1864 method, ~$4
- 192 unassigned mssEC 18 entries (no punctuation or signature marker) - blocker: not-attempted; print-agreement assignment failed its pre-registered control 4 Oct 2026 (RUN3-ECK62: 41/78 decided vs 38/78 on an unrelated window), so it is retired for this hypothesis; next: a print-free assignment by general OR vocabulary with a shuffled-key control, pre-registered, ~$2

## Escalation (RUN3-ECK62, 4 Oct 2026)
- [x] siblings: received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171); parallel sent ledger mssEC 18 opened by text 4 Oct 2026 (GAPS206), read with Cipher No. 1 (A3V3-ECK18) and No. 2 (A3V3-ECK2)
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [ ] known-keys: no filled-in book for Feb 1862 (failure log); the 192 '?' mssEC 18 entries: print-agreement assignment retired 4 Oct 2026 (RUN3-ECK62, control failed); next: print-free assignment, ~$2
- [x] print: OR vols. 5, 7, 8, 9, 10 pt 1-2, 11 pt 1/3, 12 pt 1/3, 51 pt 1, 53, Nicolay-Hay, Grant Papers vol. 4 done; OR ser. I vols. 32-49 done for mssEC 18 (A3V3-ECK18, A3V3-ECK2); the 26 matches aligned word by word (A3V3-ECKC)
- [x] key-rebuild: Koran/Lamb/Luna/Indus done 3 Oct 2026 (GAPS191); Handle, Harry, author added at C (A3V3-ECKC); possessive and collision guard added to decode.py (RUN3-ECK62)
- [ ] image-check: the ten mssEC 15 readings were reconciled against the image (reading.md); the 26 print-matched mssEC 18 entries were not; first the 3 unguarded collisions (white, animals, Hotel) and the Lehigh / weigh conflicts; next: image-reconcile with the eckert-1864 method, ~$4
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 4 internal gaps; cheapest next: print-free book assignment for the 192 '?' mssEC 18 entries (pre-registered, shuffled-key control), ~$2; then the image check of the six collision/conflict entries, ~$4

## RUN6-ECK62-eckert-1862 (5 Oct 2026, account 1 worker for LANE-RUN6): print-free book assignment of the 192 '?' mssEC 18 entries

Pre-registered and pushed before any number: `ec18/PREREG-ECK62-FREE.md` (commit fea9ffb3, 05:41 UTC). Script `ec18.py DATA
--assign-free DIR62 --write|--check` (`--check` current); outputs `ec18/assign_free.tsv`, `ec18/assign_free_summary.tsv`.
Statistic: per keyed word-kind meaning, bigram support (count >= 2) with its left or right neighbour in the 8 OR 1862
volumes RUN3-ECK62 used as DIR62 (no 1864-65 print, so no entry's own telegram); both keys, possessive + guard as the
committed outputs; marker words deleted from every entry; book = the key with >= 2 more supported meanings.
- Known answer (479 marker-known entries, markers deleted): 326 decided, 292 right = 0.896. Per class: book 1 173/199
  decided right (0.869; 112 undecided), book 2 119/127 (0.937; 41 undecided). Precision of a "1" decision 173/181 = 0.956,
  of a "2" decision 119/145 = 0.821 (26 book-1 entries called 2).
- Control (20 shuffled-meaning keys, word rows only, coverage and inventory kept): accuracy 0.480-0.707, mean 0.571;
  per class on seeds 0-2 about 0.59-0.62 (book 1) and 0.59-0.75 (book 2). Gate (>= 0.85, >= 20 decided, > max shuffled,
  >= mean + 0.15): PASS on all four.
- Assigned: 79 of 192 '?' entries (21 -> `1f`, 58 -> `2f`); 113 stay '?' (margin < 2). The book of an `1f`/`2f` entry is
  grade S (cryptanalytic, with control); its tokens keep the assigned key row's grade; by the known-answer precision expect
  about 1 in 6 `2f` entries to be book 1. No reading regenerated with the assigned books (not in the brief); ec18.py's
  book rule and the committed entries/readings are unchanged.
- Data: vol18.json re-fetched (sha256 cb162574..., matches pilot1864/manifest.tsv); DIR62 8 `_djvu.txt` to scratch, not
  committed (ids in RUN3-ECK62 above). Requests: hdl.huntington.org 1, archive.org 8, >= 1.6 s apart. 0 vision, 0 subagents.

## RUN6-ECK62R (5 Oct 2026, account 1 worker for LANE-RUN6): the 79 print-free-assigned entries read with the assigned book

The named next step of RUN6-ECK62 only. New option `ec18.py DATA --read-free DIR62 --write|--check` (`--check` current):
each `1f`/`2f` row of `ec18/assign_free.tsv` decoded with its assigned key (key.md for 1f, key-no2.md for 2f; full
volunteer text, markers kept; `--possessive` and the DIR62 collision guard as the committed outputs). Outputs
`ec18/readings_free.tsv` (per entry: keyed, S, I, M, oov, class, oov words) and `ec18/readings_free.md` (all 79 readings).
- Grades (rule 4): the book is S (RUN6-ECK62's control-backed gate), so every keyed token from an H/C key row is counted
  S: S 1229, I 4, M 0, H 0, C 0 across the 79 entries. Cryptanalytic result, conditional on the volunteer transcription
  (rule 2, no image reconciled).
- Words vs not (the fully-keyed rule, >= 3 keyed tokens and 0 out-of-vocabulary words outside brackets): 2 words, 77 not.
  Words: 9910.423 (1f, 1864-12-08, S 10: troops to be sent to [Maj Gen Geo. H. Thomas], "[5000] [Men] can be spared from
  [Missouri]") and 9971.546 (2f, 1865-03-04, S 14: a new [Regiment] from states [East] of [Ohio] [Order]ed to
  [Baltimore]). Not: 1f 20, 2f 57; oov per entry 1-21 (median about 5); the 16 with oov 1-2 are mostly names or
  volunteer spellings (Kearney, Eckert, Govt, Berrien) or plain code words read with a meaning-less lookup (whiffir,
  tambons, platina, tummuch). For scale, the marker-known entries give 28/311 (book 1) and 17/168 (book 2) word-clean
  readings with their own key, so 2/79 is lower than the marker-known rate; the '?' entries are the ones with no
  punctuation markers, i.e. shorter or less keyed.
- Not done (not in the brief): no print check of the two word-clean readings, no image check. Requests: hdl.huntington.org
  1 (vol18.json, sha256 cb162574... matches pilot1864/manifest.tsv), archive.org 8 (DIR62), >= 1.6 s apart; 0 vision,
  0 subagents. Report what was found and where it was not found; no novelty class.

## Remaining gaps (finish-or-blocker pass, RUN6-ECK62, 5 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82 (print/residue, GAPS197 with the GAPS191 key); mssEC 18: 28 fully keyed Cipher No. 1 entries (14 in OR, H 369 C 2) and 17 fully keyed Cipher No. 2 entries (12 in OR), from the volunteer text, read with the possessive option and collision guard (RUN3-ECK62); 79 of the 192 '?' entries given a book at S (RUN6-ECK62: 21 No. 1, 58 No. 2) and read with it (RUN6-ECK62R: S 1229, I 4; 2 word-clean)
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; every OR volume that could hold Feb-Jul 1862 telegrams grepped and aligned (GAPS113-GAPS153), received ledgers read (GAPS171), page 4979 checked (GAPS187), sent-side witnesses folded into key.md (GAPS191), residue regenerated (GAPS197: C 155, I 36, M 82, oov 860); next: a received-ledger pass on mssEC 04-14 (not yet harvested) by the GAPS171 method, ~$2
- residue code words not fixed by any known plaintext - blocker: open-codes; about 860 oov tokens remain (GAPS197); conflicts Lamb, Luna date-separated, Indus split by slot; table-change dates unwitnessed between 21 Mar and 25 May
- 1863-67 sent ledgers at grade H - blocker: not-attempted; mssEC 18 read by text with both books, aligned to OR, possessive and guard applied (RUN3-ECK62: 6/9 collisions removed, 0/198 false guards); white, animals, Hotel and the Lehigh / weigh conflicts stay open; next: image-reconcile those entries (9765.139, 9911.425, 10010.593, 9947.505, 10020.609, 9965.539) with the eckert-1864 method, ~$4
- 77 print-free-assigned mssEC 18 entries read with the assigned book but not word-clean (oov > 0; RUN6-ECK62R, ec18/readings_free.tsv) - blocker: not-attempted; read by text only, no print or image check in the brief (RUN6-ECK62R); next: print-check the 2 word-clean readings (9910.423, 9971.546) against OR ser. I vols. 41-46 with ec18.py's matcher, and image-reconcile the 16 entries with oov <= 2, ~$2
- 113 mssEC 18 entries still '?' (margin < 2 under both instruments) - blocker: not-attempted; no pre-registered rule decides them (RUN6-ECK62, ec18/assign_free_summary.tsv); next: same rule at margin 1 is not pre-registered and would need its own known-answer precision; or the image (marker words the volunteer text may have dropped), within the image-check step, ~$4

## Escalation (RUN6-ECK62, 5 Oct 2026)
- [x] siblings: received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171); parallel sent ledger mssEC 18 opened by text 4 Oct 2026 (GAPS206), read with Cipher No. 1 (A3V3-ECK18) and No. 2 (A3V3-ECK2)
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [ ] known-keys: no filled-in book for Feb 1862 (failure log); 79 of the 192 '?' mssEC 18 entries assigned print-free 5 Oct 2026 (RUN6-ECK62, 0.896 known answer vs shuffled-key mean 0.571); next: read them with the assigned book, ~$1
- [x] print: OR vols. 5, 7, 8, 9, 10 pt 1-2, 11 pt 1/3, 12 pt 1/3, 51 pt 1, 53, Nicolay-Hay, Grant Papers vol. 4 done; OR ser. I vols. 32-49 done for mssEC 18 (A3V3-ECK18, A3V3-ECK2); the 26 matches aligned word by word (A3V3-ECKC)
- [x] key-rebuild: Koran/Lamb/Luna/Indus done 3 Oct 2026 (GAPS191); Handle, Harry, author added at C (A3V3-ECKC); possessive and collision guard added to decode.py (RUN3-ECK62)
- [ ] image-check: the ten mssEC 15 readings were reconciled against the image (reading.md); the 26 print-matched mssEC 18 entries were not; first the 3 unguarded collisions (white, animals, Hotel) and the Lehigh / weigh conflicts; next: image-reconcile with the eckert-1864 method, ~$4
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 5 internal gaps; cheapest next: read the 79 print-free-assigned mssEC 18 entries with their assigned book (ec18.py option), ~$1; then the image check of the six collision/conflict entries, ~$4

## DEF1-ECK62I-eckert-1862 (5 Oct 2026, account 1 worker for LANE DEFAULT-account-1-20261005-2039): image check of the six collision/conflict mssEC 18 entries

The named next step (RUN3-ECK62, RUN6-ECK62 gap 3). Route: Huntington IIIF, the eckert-1864 route
(`https://hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/full/0/default.jpg`), pointers 9765, 9911, 9947, 9965,
10010, 10020 (mssEC 18 pp. 99, 245, 281, 299, 344, 354; 6018-6146 x 7200 px), fetched once to scratch, not committed.
Crop step (pasted, one per entry): `python3 tools/iiif_lines.py --image <scratch>/p<pointer>.jpg --region <x,y,w,h>
--out <scratch>/crops/<pointer> --prefix e<id> --lines-per-crop 1-3 --max-width 2400` (regions in `ec18/image_check.tsv`);
the six key-word crops are committed reduced to 1400 px in `images/ec18-check/` (124 KB). Each code word was read from the
crop before its line in the volunteer text was compared (the collision/conflict word names themselves were known from the
brief). vol18.json re-fetched, sha256 cb162574... (matches pilot1864/manifest.tsv).
- Result: the image agrees with the volunteer transcription on all six entries and all eight checked tokens (white,
  Animals, Lehigh, Dodge, weigh, Hotel with "beat at", lehigh, Dodge). No transcription input changed, so `ec18.py`,
  `ec18_align.py` and the eckert-1864 decoders were not re-run (nothing they read changed; `--check` needs the uncommitted OR
  texts). Every collision and conflict is therefore a decode or key question, not a reading error.
- Decisions (per token, `ec18/image_check.tsv`): Animals (9911.425), Hotel (10010.593; "beat at Hotel" = OR "be at a
  hotel") and weigh (9965.539; "be on the weigh." with the unity period, OR "on the way") are clear words over-read as code:
  read clear, grade C from the print, the key meanings Monroe, Weldon, Threaten dropped for these tokens. Dodge (9947.505,
  10020.609) clear name, C. white (9765.139): the image shows h (a tall loop as in "whack" on the line above, not the short r
  of "hers"), so the clerk wrote the code word; "ascertain and [Report] to me" fits as well as the printed "write"; held M,
  logged as a data conflict. Lehigh (9947.505, OR "general Canby") and lehigh (10020.609, OR "can be provided"): both
  clearly written, so the key-vs-print conflict with key.md p.17 l.6 (Hurlbut) is a key question (rule 4: logged, not settled
  by majority); both held M. Counts over the 8 tokens: C 5, M 3, H 0 added.
- Not done: the guard rule was not changed (a later option could treat these three confirmed clear-word collisions as a
  known-answer set); no other entry imaged. Requests: hdl.huntington.org 7 (1 dmQuery, 6 IIIF full images), >= 2 s apart;
  0 subagents (vision by this worker on 8 crops). Report what was found and where it was not found; no novelty class.

## Remaining gaps (finish-or-blocker pass, DEF1-ECK62I, 5 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82 (print/residue, GAPS197 with the GAPS191 key); mssEC 18: 28 fully keyed Cipher No. 1 entries (14 in OR, H 369 C 2) and 17 fully keyed Cipher No. 2 entries (12 in OR), from the volunteer text, read with the possessive option and collision guard (RUN3-ECK62); 79 of the 192 '?' entries given a book at S (RUN6-ECK62) and read with it (RUN6-ECK62R: S 1229, I 4; 2 word-clean); six collision/conflict entries image-checked (DEF1-ECK62I: transcription confirmed 8/8 tokens; C 5, M 3)
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; every OR volume that could hold Feb-Jul 1862 telegrams grepped and aligned (GAPS113-GAPS153), received ledgers read (GAPS171), page 4979 checked (GAPS187), sent-side witnesses folded into key.md (GAPS191), residue regenerated (GAPS197: C 155, I 36, M 82, oov 860); next: a received-ledger pass on mssEC 04-14 (not yet harvested) by the GAPS171 method, ~$2
- residue code words not fixed by any known plaintext - blocker: open-codes; about 860 oov tokens remain (GAPS197); conflicts Lamb, Luna date-separated, Indus split by slot; table-change dates unwitnessed between 21 Mar and 25 May
- 1863-67 sent ledgers at grade H - blocker: not-attempted; mssEC 18 read by text with both books, aligned to OR, possessive and guard applied (RUN3-ECK62); the six collision/conflict entries image-checked 5 Oct 2026 (DEF1-ECK62I): the volunteer text is right on every token, Animals/Hotel/weigh are clear words (C), white and Lehigh/lehigh are key-vs-print data conflicts (M); next: settle Lehigh against the mssEC 41 key page image (key.md p.17 l.6) and the received copies of 27 Jan and 24 May 1865, ~$2
- 77 print-free-assigned mssEC 18 entries read with the assigned book but not word-clean (oov > 0; RUN6-ECK62R, ec18/readings_free.tsv) - blocker: not-attempted; read by text only, no print or image check yet; next: print-check the 2 word-clean readings (9910.423, 9971.546) against OR ser. I vols. 41-46 with ec18.py's matcher, and image-reconcile the 16 entries with oov <= 2, ~$2
- 113 mssEC 18 entries still '?' (margin < 2 under both instruments) - blocker: not-attempted; no pre-registered rule decides them (RUN6-ECK62, ec18/assign_free_summary.tsv); next: the image (marker words the volunteer text may have dropped; DEF1-ECK62I found the text faithful on 6 entries, so a low yield is expected), ~$4

## Escalation (DEF1-ECK62I, 5 Oct 2026)
- [x] siblings: received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171); parallel sent ledger mssEC 18 opened by text 4 Oct 2026 (GAPS206), read with Cipher No. 1 (A3V3-ECK18) and No. 2 (A3V3-ECK2)
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [ ] known-keys: no filled-in book for Feb 1862 (failure log); 79 of the 192 '?' mssEC 18 entries assigned and read (RUN6-ECK62, RUN6-ECK62R); next: check the Lehigh row on the mssEC 41 key page image, ~$2
- [x] print: OR vols. 5, 7, 8, 9, 10 pt 1-2, 11 pt 1/3, 12 pt 1/3, 51 pt 1, 53, Nicolay-Hay, Grant Papers vol. 4 done; OR ser. I vols. 32-49 done for mssEC 18 (A3V3-ECK18, A3V3-ECK2); the 26 matches aligned word by word (A3V3-ECKC)
- [x] key-rebuild: Koran/Lamb/Luna/Indus done 3 Oct 2026 (GAPS191); Handle, Harry, author added at C (A3V3-ECKC); possessive and collision guard added to decode.py (RUN3-ECK62)
- [x] image-check: the ten mssEC 15 readings reconciled against the image (reading.md); the six mssEC 18 collision/conflict entries image-checked 5 Oct 2026 (DEF1-ECK62I, ec18/image_check.tsv: transcription confirmed 8/8)
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 5 internal gaps; cheapest next: print-check the 2 word-clean print-free readings (9910.423, 9971.546) against OR vols. 41-46, ~$1; then the Lehigh key-page check, ~$2

## DEF1-ECK62P (5 Oct 2026, account 1 worker for LANE DEFAULT-account-1-20261005-2039): print check of the two word-clean print-free readings; Lehigh on the key page image

The two named next steps of DEF1-ECK62I's Verdict only.

**(1) Print check.** New option `ec18.py --print-free ORDIR --write|--check` (`--check` exit 0): runs ec18.py's own matcher
(`or_index` + `match`, 5-grams, >= 4 in one 400-word block, the entry's date within the preceding 1,500 words) over all 79
readings in `readings_free.md`, real dates vs 20 date permutations (seed 18), output `ec18/print_free.tsv`. ORDIR = OR ser. I
vols. 41.1-46.3, the 15 `_djvu.txt` of `or_volumes.tsv`, re-fetched to scratch, every sha256 matching the table (not committed).
- Control: 27/79 entries match on their real dates; under 20 date permutations 0-4 (max 4). The matcher's hits are dated hits.
- 9910.423 (book 1f, 8 Dec 1864): OR ser. I vol. 45 pt 2 p. 97, Halleck to Maj. Gen. Dodge, Saint Louis, 8 Dec 1864, 9 p.m.
  (18 five-grams). Print: "Send all the troops you can spare to General Thomas by such route as you may deem best. They can be
  returned to you when required. I think 5,000 men can be spared from Missouri." Brackets vs print: [8] date, [Troops], [Maj
  Gen Geo. H. Thomas], [5000], [Men], [Missouri] agree; [General in Chief] stands for the signature (print: H. W. Halleck,
  Major-General and Chief of Staff; the key's office title predates Halleck's March 1864 change of post, read as the sender,
  not a conflict); [McMinnville] disagrees: the print has the addressee "Major-General Dodge", and Dodge = McMinnville in key.md
  p.13 l.15 -- the same clear-name collision DEF1-ECK62I confirmed on the image for 9947.505 and 10020.609 (C, clear, print).
- 9971.546 (book 2f, 4 Mar 1865): OR ser. I vol. 46 pt 2 p. 834, Halleck to Maj. Gen. Hancock, Winchester, 4 Mar 1865, 10.30
  a.m. (12 five-grams). Print: "One new regiment from States east of Ohio is ordered to Baltimore. All others from such States
  will be sent to such points as you may indicate to the Adjutant-General of the Army." All 11 body brackets agree ([1],
  [Regiment], [East], [Ohio], [Order], [Baltimore], [Will be sent], [Point], [Adjutant General], [Of the], [Army]); tail
  [General in Chief] = Halleck's signature as above. Two unbracketed words disagree with the print: "Minister" where the print
  has the addressee (Hancock, Winchester) and "shoe" where it has "you" -- in-vocabulary words the word-clean rule
  (`oov == 0`) cannot flag; neither is in key-no2.md. Not settled (no image read in this job).
- So both print-free book assignments (1f, 2f) are confirmed by print for these two entries (book grade S -> C for them); their
  agreeing bracketed tokens are C (known plaintext). Counts: 9910.423 C 7 (incl. signature), 1 clear-name collision (Dodge, C as
  clear); 9971.546 C 12, 2 unkeyed words unresolved (M). The other 25 dated matches (all class 'not') are listed in
  print_free.tsv and were not aligned (not in the brief; suggestion: align them with ec18_align.py, they include 9904.410 at 42
  five-grams and 9991.571 at 47).

**(2) Lehigh on the key page.** Huntington IIIF `p16003coll11/334/full/full/0/default.jpg` (mssEC 41 p. 17, native 2295 x
3000), fetched once to scratch. Crop step (pasted): `python3 tools/iiif_lines.py --image p334.jpg --region 510,670,1290,210
--out crops334 --prefix lehigh --max-width 2400` -> 2 lines (Leghorn, Lehigh); the Lehigh row committed as
`images/ec18-check/mssEC41_p334_l6_Lehigh.jpg`. Read: "Lehigh .... -do -do -do .... Leopard", ditto marks under row 5's
"Maj. Gen. S. A. Hurlbut"; no correction, interlineation or second hand on the row (the faint marks below are show-through).
key.md p.17 l.6 (Hurlbut, H) is therefore what the book says. The conflict persists and is logged, not settled (rule 4):
- Witness A (key): mssEC 41 Cipher No. 1, filled-in book, p.17 l.6 L: Lehigh = Maj. Gen. S. A. Hurlbut (ditto), image-checked
  5 Oct 2026.
- Witness B (print + sent ledger): mssEC 18 9947.505 (Lehigh, OR "general Canby") and 10020.609 (lehigh, OR "can be provided"),
  both sent from Washington, 1865 (dates as `ec18/image_check.tsv`), ledger image confirmed by DEF1-ECK62I.
- Inference only (grade I, not used): both print values are the sound "Canby"; a later issue or local re-assignment of Lehigh to
  Canby, then used as a sound-alike for "can be", would fit both. Hurlbut served under Canby in 1865, which could also explain a
  ditto-row change. The received copies of 27 Jan and 24 May 1865 and any later edition of the book were not checked here.
Requests: hdl.huntington.org 1 (IIIF), archive.org 15 (+15 empty first attempts without -L, no data), >= 1.6 s apart; 0
subagents. Report what was found and where it was not found; no novelty class.

## Remaining gaps (finish-or-blocker pass, DEF1-ECK62P, 5 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82 (print/residue, GAPS197 with the GAPS191 key); mssEC 18: 28 fully keyed Cipher No. 1 entries (14 in OR, H 369 C 2) and 17 fully keyed Cipher No. 2 entries (12 in OR), from the volunteer text, read with the possessive option and collision guard (RUN3-ECK62); 79 of the 192 '?' entries given a book at S (RUN6-ECK62) and read with it (RUN6-ECK62R: S 1229, I 4; 2 word-clean, both now matched to OR 45.2 p.97 and 46.2 p.834, DEF1-ECK62P; 27/79 dated OR matches vs 0-4 shuffled); six collision/conflict entries image-checked (DEF1-ECK62I: C 5, M 3); Lehigh key row image-checked (DEF1-ECK62P: Hurlbut, conflict persists)
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; every OR volume that could hold Feb-Jul 1862 telegrams grepped and aligned (GAPS113-GAPS153), received ledgers read (GAPS171), page 4979 checked (GAPS187), sent-side witnesses folded into key.md (GAPS191), residue regenerated (GAPS197: C 155, I 36, M 82, oov 860); next: a received-ledger pass on mssEC 04-14 (not yet harvested) by the GAPS171 method, ~$2
- residue code words not fixed by any known plaintext - blocker: open-codes; about 860 oov tokens remain (GAPS197); conflicts Lamb, Luna date-separated, Indus split by slot; table-change dates unwitnessed between 21 Mar and 25 May
- 1863-67 sent ledgers at grade H - blocker: not-attempted; mssEC 18 read by text with both books, aligned to OR, possessive and guard applied (RUN3-ECK62); six collision/conflict entries image-checked (DEF1-ECK62I); Lehigh key row read on mssEC 41 p.17 (DEF1-ECK62P): the book says Hurlbut, two 1865 sent telegrams print Canby/"can be" -- rule-4 conflict logged with witnesses, held M; next: the received copies of the 27 Jan and 24 May 1865 telegrams (Eckert received ledgers) for a third witness, ~$2
- 77 print-free-assigned mssEC 18 entries not word-clean (RUN6-ECK62R) - blocker: not-attempted; 25 of them match OR on their own dates (ec18/print_free.tsv, DEF1-ECK62P) but are not aligned; next: align those 25 with ec18_align.py (C-grade tokens, book confirmation), ~$2; then image-reconcile the 16 with oov <= 2
- 113 mssEC 18 entries still '?' (margin < 2 under both instruments) - blocker: not-attempted; no pre-registered rule decides them (RUN6-ECK62, ec18/assign_free_summary.tsv); next: the --print-free matcher on them with both books (a dated OR match decides the book from print), ~$1

## Escalation (DEF1-ECK62P, 5 Oct 2026)
- [x] siblings: received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171); parallel sent ledger mssEC 18 opened by text 4 Oct 2026 (GAPS206), read with Cipher No. 1 (A3V3-ECK18) and No. 2 (A3V3-ECK2)
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [x] known-keys: Lehigh row checked on the mssEC 41 key page image 5 Oct 2026 (DEF1-ECK62P: Hurlbut, conflict with print logged per rule 4); 79 '?' entries assigned and read (RUN6-ECK62, RUN6-ECK62R)
- [ ] print: OR vols. 5, 7-12, 51, 53, Nicolay-Hay, Grant Papers vol. 4 done for 1862; OR ser. I vols. 32-49 for mssEC 18 (A3V3-ECK18, A3V3-ECK2, A3V3-ECKC); print-free readings matched to OR 41-46 (DEF1-ECK62P: 27/79 dated); next: align the 25 unaligned dated matches, ~$2
- [x] key-rebuild: Koran/Lamb/Luna/Indus done 3 Oct 2026 (GAPS191); Handle, Harry, author added at C (A3V3-ECKC); possessive and collision guard added to decode.py (RUN3-ECK62)
- [x] image-check: the ten mssEC 15 readings reconciled against the image (reading.md); the six mssEC 18 collision/conflict entries (DEF1-ECK62I) and the Lehigh key row (DEF1-ECK62P)
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 5 internal gaps; cheapest next: --print-free matcher on the 113 '?' entries with both books, ~$1; then align the 25 dated print-free matches, ~$2

## D2-ECK62M (5 Oct 2026, account 1 worker for LANE DEFAULT-account-1-20261005-2217): --print-q on the 113 '?' entries, then alignment of the dated print-free matches

The two named next steps of DEF1-ECK62P's Verdict only. Rules pre-registered and pushed before any number:
`ec18/PREREG-ECK62-Q.md` (commit f4da742f3). Code: `ec18.py DATA --print-q ORDIR` and `ec18_align.py DATA ORDIR --rows
align_free_rows.tsv` (commit accd021dd); ORDIR = OR ser. I vols. 32.1-49.2, the 48 `_djvu.txt` of `or_volumes.tsv`,
re-fetched to scratch, all 48 sha256 matching (not committed); vol18.json re-fetched (manifest URL). Possessive on, guard
off (DIR62 not fetched) for every run alike. All three outputs pass `--check`; the original `ec18_align.py --check` and
`decode.py --check` are current.

**(1) Book of the '?' entries by print** (`ec18/print_q.tsv`, `ec18/print_q_summary.tsv`). Each '?' entry (markers deleted)
read with both keys; ec18.py's own dated matcher run on both readings; book k when gk >= 4 and gk - g(other) >= 2.
- Known answer (479 marker-known entries, markers deleted): 259 decided, 242 right = 0.934 ('1' 146/156, '2' 96/103);
  30 dated but margin < 2, 190 no dated match.
- Control (dates permuted among the 113 '?' entries, 20 permutations, seed 18): dated matches 0-3 (max 3) vs 33 real.
- Gate (precision >= 0.90 on >= 20 decided, real > max permuted): PASS.
- Decided: 13 of 113 (11 -> `1p`, 2 -> `2p`); 20 have a dated OR match but margin < 2 (`?p`); 80 have no dated match.
  The `1p`/`2p` book is C (the print decides it); its tokens keep the key-row grade. 100 entries stay '?'.

**(2) Alignment** (`ec18/align_free_rows.tsv` -> `ec18/align_free_{tokens,entries,summary}.tsv`): 57 entries = 44 print-free
1f/2f readings with a dated match in OR 32-49 (DEF1-ECK62P found 27 within 41-46 only; the 17 extra are in vols. 32-39 and
47-49, matched by the same rule but not under DEF1-ECK62P's date-permutation control, which covered 41-46) + the 13 `1p`/`2p`.
- Pooled: 817 keyed word tokens scored; AGREE 316 (0.387) vs control window (same-week other telegram) 60 (0.073); conflict
  128, unfixed 325, partial 18, collision 30; entries above their own control 34/57 (print-free 28/44, print-q 6/13);
  numerals 35/82. Grades over all keyed tokens after alignment: H 61, C 351, S 516, I 2, M 0 (H only on `1p`/`2p`; S =
  the 1f/2f book cap on non-AGREE tokens).
- Strong agreements (rate >= 0.75 and well above control): 9806.197, 9849.279, 9851.286 (14/15), 9852.288, 9801.190,
  9824.233, 9866.321, 9897.392, 9901.400, 9916.434, 9927.456, 9929.461, 9971.546 (11/12), 10005.582; 9809.203 C 67 (60/90
  AGREE, the largest single entry); 9904.410 22/34.
- Zero or near-zero agreement with many conflicts (book, not print, the likely cause; not settled here): 2f entries
  9934.472 (0/28, 9 conflicts), 9954.519 (0/17), 9974.549 (2/36, 17 conflicts), 9985.563/.564, 9987.565, 9996.574,
  9924.452 (1/21), 9991.571 (3/31); 1f 9977.553, 9983.561, 9762.135; `1p` 9982.559 (0/13, 6 conflicts). RUN6-ECK62's known-
  answer precision for a '2' decision (0.821) predicts about 1 in 6 `2f` entries to be book 1, which fits these; the
  dated match itself can be carried by the clear words alone. Their S tokens are not confirmed by print.
- `1p` entries with 0-2 scored tokens (9670.7, 9761.133, 9943.495, 9946.501, 9991.570) match on clear text: the book
  decision rests on gram counts, not on keyed words agreeing with print; their H tokens are unconfirmed by alignment.
- Not done (not in the brief): no re-alignment of the zero-agree entries with the other key; no image check; conflicts
  not resolved. Requests: hdl.huntington.org 1 (vol18.json), archive.org 48 (OR djvu), >= 1.6 s apart; 0 vision, 0
  subagents. Report what was found and where it was not found; no novelty class.

## Remaining gaps (finish-or-blocker pass, D2-ECK62M, 5 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82 (GAPS197); mssEC 18: 28 fully keyed Cipher No. 1 and 17 Cipher No. 2 entries (RUN3-ECK62), 26 print-aligned (A3V3-ECKC); 79 print-free-assigned entries read (RUN6-ECK62R); 13 of the 113 '?' entries given a book by print (D2-ECK62M, 0.934 known answer, 33 vs 0-3 permuted); 57 dated matches aligned (D2-ECK62M: AGREE 316/817 = 0.387 vs control 0.073; C 351 after alignment); six collision entries and the Lehigh key row image-checked (DEF1-ECK62I, DEF1-ECK62P)
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; every OR volume that could hold Feb-Jul 1862 telegrams grepped and aligned (GAPS113-GAPS153), received ledgers read (GAPS171), residue regenerated (GAPS197); next: a received-ledger pass on mssEC 04-14 (not yet harvested) by the GAPS171 method, ~$2
- residue code words not fixed by any known plaintext - blocker: open-codes; about 860 oov tokens remain (GAPS197); conflicts Lamb, Luna date-separated, Indus split by slot; table-change dates unwitnessed between 21 Mar and 25 May
- 1863-67 sent ledgers at grade H - blocker: not-attempted; Lehigh conflict held M with witnesses (DEF1-ECK62P); next: the received copies of the 27 Jan and 24 May 1865 telegrams (Eckert received ledgers) for a third witness, ~$2
- about 14 aligned print-free/print-q entries with 0-3 AGREE and many conflicts (D2-ECK62M, ec18/align_free_entries.tsv) - blocker: not-attempted; book likely wrong, not tested; next: re-align them with the other key (ec18_align.py --rows with the book flipped, compare AGREE vs control; pre-register first), ~$1
- 100 mssEC 18 entries still '?' - blocker: not-attempted; 20 have a dated OR match with margin under 2 and 80 none (D2-ECK62M); next: the image (marker words the volunteer text may have dropped) for the 20 `?p` entries, ~$4

## Escalation (D2-ECK62M, 5 Oct 2026)
- [x] siblings: received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171); parallel sent ledger mssEC 18 opened by text 4 Oct 2026 (GAPS206), read with Cipher No. 1 (A3V3-ECK18) and No. 2 (A3V3-ECK2)
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [x] known-keys: Lehigh row checked on the mssEC 41 key page image (DEF1-ECK62P); '?' entries assigned print-free (RUN6-ECK62) and by print (D2-ECK62M, 13 of 113)
- [ ] print: OR ser. I vols. 32-49 matched and the 57 dated print-free/print-q matches aligned 5 Oct 2026 (D2-ECK62M); next: re-align the about 14 zero-agree entries with the other key, ~$1
- [x] key-rebuild: Koran/Lamb/Luna/Indus done 3 Oct 2026 (GAPS191); Handle, Harry, author added at C (A3V3-ECKC); possessive and collision guard added to decode.py (RUN3-ECK62)
- [x] image-check: the ten mssEC 15 readings reconciled against the image (reading.md); the six mssEC 18 collision/conflict entries (DEF1-ECK62I) and the Lehigh key row (DEF1-ECK62P)
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 5 internal gaps; cheapest next: re-align the about 14 zero-agree print-free/print-q entries with the other key (pre-registered), ~$1; then the image of the 20 `?p` entries, ~$4

## D2-ECK62R (5 Oct 2026, account 1 worker for LANE DEFAULT-account-1-20261005-2217): the zero-agree aligned entries re-aligned under the other book

Intake gate (23:37 UTC): `eckert-1862: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`.
Pre-registered and pushed before any number: `ec18/PREREG-ECK62-FLIP.md` (commit 039c3b379). Instrument: `ec18_align.py`
unchanged in method (output suffix now follows the rows file; a `flip-*` source caps non-AGREE tokens at S); D2-ECK62M's
`align_free_*` outputs reproduce byte-identically (`--check` current). Same ORDIR (48 `_djvu.txt`, all sha256 matching
`or_volumes.tsv`, scratch, not committed), same vol18.json (sha256 matches the manifest), same anchors and control window.

- Selection (mechanical, from `align_free_entries.tsv`): scored >= 5, agree rate <= 0.10, conflict >= 1 -> 19 entries
  (`ec18/align_flip_rows.tsv`; 13 of them are the ones D2-ECK62M named, plus 9669.5, 9808.202, 9949.508, 9958.527, 9969.543,
  10040.638). 9761.133 (0 conflicts) and 10031.631 (0 conflicts) fall outside the rule.
- Negative control for the flip (rule 3): the 14 entries at agree rate >= 0.75 flipped the same way
  (`ec18/align_flipctl_*.tsv`): AGREE 122/146 = 0.836 under their book -> 16/132 = 0.121 flipped (control window 0.045).
  Gate (<= 0.15): PASS. A wrong book does not align, so the instrument can tell books apart.
- Target (`ec18/align_flip_*.tsv`): AGREE 7/291 = 0.024 under the assigned book -> 20/261 = 0.077 flipped; control window
  6/261 = 0.023; flipped conflicts 87, unfixed 149.
- Accepted flip (rule 4 of the prereg): **1 of 19**, 9991.571 (15 Apr 1865, OR 46.3, print-free book 2 -> book 1):
  3/31 = 0.097 -> 12/30 = 0.400, control window 0.033, 0 conflicts; e.g. Mentor = Maj Gen E. O. C. Ord, Oakum = arrest,
  Garden = Richmond, saddled = guarded. Book recorded as `1r` here and in `align_flip_entries.tsv` (book grade S: aligned
  against print, not marker-known); grades on its keyed tokens after alignment C 12, S 24. Its neighbour 9991.570 is
  book 1 by print (D2-ECK62M), which fits. Not yet written into `assign_free.tsv` / `readings_free.*` (those feed
  decode outputs; a follow-up, not this brief).
- The other 18 do not align under either book (flipped rate 0-0.33; 9808.202 at 2/6 misses the >= 3 AGREE floor). A wrong book
  is therefore **not** the explanation for them. Remaining causes, not tested here: the dated OR match is carried by clear words
  and points to the wrong telegram (several are short, 5-17 scored), a cipher table change not covered by key.md/key-no2.md
  (most are Feb-Apr 1865, 9924-9996), or volunteer transcription. Grades: their tokens stay as D2-ECK62M left them (S cap).
- Requests: archive.org 48 (OR djvu), hdl.huntington.org 1 (vol18.json), >= 1.6 s apart; 0 vision, 0 subagents. Report what
  was found and where it was not found; no novelty class.

## Remaining gaps (finish-or-blocker pass, D2-ECK62R, 5 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82 (GAPS197); mssEC 18: 28 fully keyed Cipher No. 1 and 17 Cipher No. 2 entries (RUN3-ECK62), 26 print-aligned (A3V3-ECKC); 79 print-free-assigned entries read (RUN6-ECK62R); 13 of the 113 '?' entries given a book by print (D2-ECK62M); 57 dated matches aligned (D2-ECK62M: AGREE 316/817 = 0.387 vs control 0.073); 19 zero-agree entries re-aligned under the other book, 1 flip accepted (D2-ECK62R, flip control 0.836 -> 0.121)
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; every OR volume that could hold Feb-Jul 1862 telegrams grepped and aligned (GAPS113-GAPS153), received ledgers read (GAPS171), residue regenerated (GAPS197); next: a received-ledger pass on mssEC 04-14 (not yet harvested) by the GAPS171 method, ~$2
- residue code words not fixed by any known plaintext - blocker: open-codes; about 860 oov tokens remain (GAPS197); conflicts Lamb, Luna date-separated, Indus split by slot; table-change dates unwitnessed between 21 Mar and 25 May
- 1863-67 sent ledgers at grade H - blocker: not-attempted; Lehigh conflict held M with witnesses (DEF1-ECK62P); next: the received copies of the 27 Jan and 24 May 1865 telegrams (Eckert received ledgers) for a third witness, ~$2
- 18 aligned entries that agree with print under neither book (D2-ECK62R, ec18/align_flip_entries.tsv) - blocker: not-attempted; wrong book ruled out for them by the flip test, cause untested; next: check each dated match against the OR telegram's sender/recipient/heading (wrong-telegram test) and list the conflicts by month against the key's table-change dates, ~$1.5
- 9991.571 book 1r not yet carried into assign_free.tsv / readings_free - blocker: not-attempted; outside this brief (decode outputs change); next: write it with decode outputs regenerated and --check, ~$0.5
- 100 mssEC 18 entries still '?' - blocker: not-attempted; 20 have a dated OR match with margin under 2 and 80 none (D2-ECK62M); next: the image (marker words the volunteer text may have dropped) for the 20 `?p` entries, ~$4

## Escalation (D2-ECK62R, 5 Oct 2026)
- [x] siblings: received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171); parallel sent ledger mssEC 18 opened by text 4 Oct 2026 (GAPS206), read with Cipher No. 1 (A3V3-ECK18) and No. 2 (A3V3-ECK2)
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [x] known-keys: Lehigh row checked on the mssEC 41 key page image (DEF1-ECK62P); '?' entries assigned print-free (RUN6-ECK62) and by print (D2-ECK62M); zero-agree entries re-aligned under the other book (D2-ECK62R, 1 of 19)
- [ ] print: OR ser. I vols. 32-49 matched and 57 dated matches aligned (D2-ECK62M); 18 entries agree under neither book (D2-ECK62R); next: wrong-telegram test on those 18, ~$1.5
- [x] key-rebuild: Koran/Lamb/Luna/Indus done 3 Oct 2026 (GAPS191); Handle, Harry, author added at C (A3V3-ECKC); possessive and collision guard added to decode.py (RUN3-ECK62)
- [x] image-check: the ten mssEC 15 readings reconciled against the image (reading.md); the six mssEC 18 collision/conflict entries (DEF1-ECK62I) and the Lehigh key row (DEF1-ECK62P)
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 6 internal gaps; cheapest next: carry 9991.571 book 1r into assign_free/readings_free, ~$0.5; then the wrong-telegram test on the 18 neither-book entries, ~$1.5

## R7B-ECK62 (6 Oct 2026, account 1 worker for LANE LANE-RUN7-account-1): 9991.571 book 1r carried; wrong-telegram test on the 18 neither-book entries

Step check: neither step had run (D2-ECK62R's Verdict, 5 Oct 2026, is the latest section).
- Carry (rule 7): `ec18.py` gains `flips()`, which applies PREREG-ECK62-FLIP rule 4 mechanically to the committed
  `align_flip_entries.tsv` and returns exactly D2-ECK62R's one accepted flip (9991.571 -> book 1). `--assign-free` writes it in
  `assign_free.tsv`'s assigned column as `1r` (decision column, the print-free '2', unchanged); `--read-free` reads it with key.md
  and labels it `1r`. Before the edit both outputs reproduced byte-identically (`--check` current). 9991.571 after: keyed 42 -> 36,
  S 41 -> 36, I 1 -> 0, oov 24 -> 26, class still `not` (its body runs into the next telegram, "Hd Qrs Washn Apl ... dispatch
  recd"; Mentor = Ord, Oakum = arrest, Garden = Richmond, saddled = guarded now read in the file). One token to watch: "libby"
  reads `{time: 6 PM}` in "put them in libby prison" (OR prints Libby Prison) -- a code/clear collision, left as the decoder
  gives it, not repaired. readings_free summary: not 1f 20 -> 21, 2f 57 -> 56; tokens S 1229 -> 1224, I 4 -> 3.
  Cascade, regenerated and `--check` current: `print_q` (only `align_free_rows.tsv` changes: 9991.571 book 2 -> 1, same anchor
  289200, matched five-grams 45 -> 57) and `ec18_align.py --rows align_free_rows.tsv` (9991.571 AGREE 3/31 -> 12/30; pooled AGREE
  316/817 = 0.387 -> 325/816 = 0.398, control 0.075; grades H 61, C 360, S 500, I 1). Since align_free_entries.tsv now aligns
  9991.571 under book 1, `flips()` holds its pre-flip rate (0.097, D2-ECK62R) as a constant so the rule stays reproducible.
  `align_flip_*`, `align_flipctl_*` also `--check` current.
- Wrong-telegram test, pre-registered and pushed before any number: `ec18/PREREG-ECK62-WRONGTEL.md` (commit c98b3aaf4). The
  brief's sender/recipient heading check was replaced in the prereg (the ledger header names the operator, Beckwith/Emerick, and
  the addressee is a code word) by clear-word coverage: LCS(entry clear words, OR window) / entry clear words. Script
  `ec18/ec18_wrongtel.py` -> `wrongtel_entries.tsv`, `wrongtel_summary.tsv`.
  Positive control (14 entries at agree >= 0.75): median 0.871, p10 0.676. Negative control (32 same-week other-telegram windows):
  median 0.206, p90 0.296. Gate PASS.
  Targets (18): **0 wrong-telegram**, 7 right-telegram (9669.5, 9762.135, 9808.202, 9958.527, 9969.543, 9985.563, 9987.565),
  11 undecided at coverage 0.49-0.67 (every one at least 0.19 above the negative p90; the prereg's stated selection bias means
  this does not prove the right telegram, but no target looks like the negative windows). Median target coverage 0.655.
  So for these 18 the dated match is the right telegram or close to it: neither book's code words agree with the print while
  the clear words do. Remaining causes: a code table not covered by key.md / key-no2.md, or the volunteer transcription.
  By month: undecided 10 of 11 fall Dec 1864 - Jul 1865 (1864-12 1, 1865-01 2, 02 1, 03 4, 04 2, 07 1); right-telegram spread
  Jan 1864 - Apr 1865. Two targets (9985.563, 9985.564) share OR 46.3 p.572; 9985.564's body visibly carries a second heading
  ("Hon CA Dana Richmond Va Washn Apl 5 1865": two telegrams merged by the blank-line split), which the descriptive
  second-date counter (ec18.DATE) misses because it has no "Apl" form -- the counter's 0 is not evidence of no merges.
  No key, book or reading changed by the test.
- Requests: hdl.huntington.org 1 (vol18.json, sha256 matches the manifest), archive.org 56 (8 DIR62 + 48 OR `_djvu.txt`, all 48
  OR sha256 matching `or_volumes.tsv`), >= 1.6 s apart, scratch, not committed. 0 vision, 0 subagents. Report what was found and
  where it was not found; no novelty class.

## Remaining gaps (finish-or-blocker pass, R7B-ECK62, 6 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82 (GAPS197); mssEC 18: 28 fully keyed Cipher No. 1 and 17 Cipher No. 2 entries (RUN3-ECK62), 26 print-aligned (A3V3-ECKC); 79 print-free-assigned entries read, 9991.571 now with book 1r (R7B-ECK62); 13 of the 113 '?' entries given a book by print (D2-ECK62M); 57 dated matches aligned (AGREE 325/816 = 0.398 vs control 0.075 after the carry); 18 neither-book entries: 0 wrong telegram, 7 right, 11 undecided (R7B-ECK62, gate PASS)
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; every OR volume that could hold Feb-Jul 1862 telegrams grepped and aligned (GAPS113-GAPS153), received ledgers read (GAPS171), residue regenerated (GAPS197); next: a received-ledger pass on mssEC 04-14 (not yet harvested) by the GAPS171 method, ~$2
- residue code words not fixed by any known plaintext - blocker: open-codes; about 860 oov tokens remain (GAPS197); conflicts Lamb, Luna date-separated, Indus split by slot; table-change dates unwitnessed between 21 Mar and 25 May
- 1863-67 sent ledgers at grade H - blocker: not-attempted; Lehigh conflict held M with witnesses (DEF1-ECK62P); next: the received copies of the 27 Jan and 24 May 1865 telegrams (Eckert received ledgers) for a third witness, ~$2
- 18 neither-book entries (right telegram or undecided, R7B-ECK62 wrongtel_entries.tsv) - blocker: not-attempted; wrong telegram ruled out for all 18 by the coverage test, so a third table or transcription is left; next: per entry, list the CONFLICT pairs (code word -> printed word) from align_flip_tokens.tsv/align_free_tokens.tsv for the 7 right-telegram entries and test whether one code word reads the same printed word in two entries (a third table, C grade only where two contexts agree), ~$1.5
- 100 mssEC 18 entries still '?' - blocker: not-attempted; 20 have a dated OR match with margin under 2 and 80 none (D2-ECK62M); next: the image (marker words the volunteer text may have dropped) for the 20 `?p` entries, ~$4
- merged telegrams in the volunteer text (9985.564, 9991.571 run into a second heading) - blocker: not-attempted; the splitter's DATE pattern has no 'Apl' form; next: add the "Apl"/"Washn" heading forms to the entry splitter and re-split, then re-run --check across ec18 outputs, ~$1

## Escalation (R7B-ECK62, 6 Oct 2026)
- [x] siblings: received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171); parallel sent ledger mssEC 18 opened by text 4 Oct 2026 (GAPS206), read with Cipher No. 1 (A3V3-ECK18) and No. 2 (A3V3-ECK2)
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [x] known-keys: Lehigh row checked on the mssEC 41 key page image (DEF1-ECK62P); '?' entries assigned print-free (RUN6-ECK62) and by print (D2-ECK62M); zero-agree entries re-aligned under the other book (D2-ECK62R, 1 of 19), the flip carried (R7B-ECK62)
- [ ] print: wrong-telegram test done (R7B-ECK62: 0 wrong, 7 right, 11 undecided); next: the conflict-pair table test on the 7 right-telegram entries, ~$1.5
- [x] key-rebuild: Koran/Lamb/Luna/Indus done 3 Oct 2026 (GAPS191); Handle, Harry, author added at C (A3V3-ECKC); possessive and collision guard added to decode.py (RUN3-ECK62)
- [x] image-check: the ten mssEC 15 readings reconciled against the image (reading.md); the six mssEC 18 collision/conflict entries (DEF1-ECK62I) and the Lehigh key row (DEF1-ECK62P)
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 6 internal gaps; cheapest next: the conflict-pair table test on the 7 right-telegram neither-book entries, ~$1.5

## R7C-ECK62C (6 Oct 2026, account 1 worker for LANE LANE-RUN7-account-1): conflict-pair table test on the neither-book entries

Step check: not run before (R7B-ECK62's Verdict, 6 Oct 2026, is the latest section). Pre-registered and pushed before any number:
`ec18/PREREG-ECK62-CONFPAIR.md` (commit b5e25e25c). Script `ec18/ec18_confpair.py --write|--check` (committed TSVs only, no
network, seed 0) -> `ec18/confpair_summary.tsv`, `ec18/confpair_pairs.tsv`; `--check` current.
Statistic S: distinct code words that stand opposite agreeing printed words (content words >= 4 letters) in two different
entries; null: printed spans shuffled across the pool's CONFLICT pairs (2000); positive control: AGREE pairs of the
non-target aligned entries (a real table), subsampled by whole entries to the pool's N, 200 x 500 shuffles, power = share at
p <= 0.05, gate >= 0.80.

| pool | entries | pairs | S | p (shuffle) | control power at N | gate |
|---|---|---|---|---|---|---|
| primary: the 7 right-telegram entries | 7 | 93 | 0 | 1.000 | 0.610 | FAIL |
| all 18 (descriptive in the prereg) | 18 | 376 | 18 | 0.0005 | 1.000 | (PASS) |
| all 18 strict (added after the prereg, descriptive: have/will/been-type words out, entries on one OR page one context) | 18 | 376 | 14 | 0.0005 | 1.000 | (PASS) |

- Pre-registered verdict: **untested-by-this-tool at N = 93** (the 7-entry pool: control power 0.61 < 0.80). Not a negative.
- Descriptive, the 18-entry pool (its own control power 1.0 at its N): 14 code words, none in key.md, key-no2.md or the
  eckert-1864 tables (key.md, key-no2.md, key-no9.md grepped 6 Oct 2026; Hoax there reads Longstreet / Weldon, here Richmond),
  stand opposite the same printed word in two different telegrams, every one dated Dec 1864 - Jul 1865:
  artists = (steam) boats (9934.472, 9974.549); thrash = Ohio [rail]road (9934.472, 9974.549); hogarth = (Alabama) river
  (9958.527, 9974.549); harm = New Berne, levels = cars, line = Morehead City (9983.561, 9987.565); hoax = Richmond
  (9985.564, 9987.565); loath = command (9977.553, 10040.638); scold = number (9982.559, 9983.561); shower = order (9983.561,
  9985.563); forge = move (9934.472, 9958.527); lunch = work (9924.452, 9974.549); joint = telegraph (9954.519, 9974.549);
  fence = left (9954.519, 9958.527). Dropped by the strict variant: credit = Weitzel (only 9985.563/9985.564, one OR page),
  duplicate, pimple, xenia (function words only).
  So most of the neither-book entries look like a code table not on disk (late 1864 - 1865), not transcription. Candidates
  only, ungraded (the gated pool did not license a grade); nothing written into any key file. The 9983.561 / 9987.565 pair
  shares a subject (rolling stock to New Berne), so its three words are two telegrams on one topic, not two independent topics.
- Requests: none (0 network, 0 vision, 0 subagents). Report what was found and where it was not found; no novelty class.

## Remaining gaps (finish-or-blocker pass, R7C-ECK62C, 6 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82 (GAPS197); mssEC 18: 28 fully keyed Cipher No. 1 and 17 Cipher No. 2 entries (RUN3-ECK62), 26 print-aligned (A3V3-ECKC); 79 print-free-assigned entries read, 9991.571 now with book 1r (R7B-ECK62); 13 of the 113 '?' entries given a book by print (D2-ECK62M); 57 dated matches aligned (AGREE 325/816 = 0.398 vs control 0.075 after the carry); 18 neither-book entries: 0 wrong telegram, 7 right, 11 undecided (R7B-ECK62, gate PASS); conflict-pair test: 7-entry pool untested (power 0.61), 18-entry pool 14 cross-entry code words p 0.0005 (R7C-ECK62C, descriptive)
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; every OR volume that could hold Feb-Jul 1862 telegrams grepped and aligned (GAPS113-GAPS153), received ledgers read (GAPS171), residue regenerated (GAPS197); next: a received-ledger pass on mssEC 04-14 (not yet harvested) by the GAPS171 method, ~$2
- residue code words not fixed by any known plaintext - blocker: open-codes; about 860 oov tokens remain (GAPS197); conflicts Lamb, Luna date-separated, Indus split by slot; table-change dates unwitnessed between 21 Mar and 25 May
- 1863-67 sent ledgers at grade H - blocker: not-attempted; Lehigh conflict held M with witnesses (DEF1-ECK62P); next: the received copies of the 27 Jan and 24 May 1865 telegrams (Eckert received ledgers) for a third witness, ~$2
- 18 neither-book entries (R7C-ECK62C confpair_pairs.tsv) - blocker: not-attempted; 14 code words outside every key on disk agree across two telegrams (Dec 1864 - Jul 1865, p 0.0005, descriptive), so a later table is the likely cause; next: find the 1865 cipher book among the Eckert papers' key books (Huntington mssEC catalogue, CISOSEARCHALL form; Tomokiyo's USMT cipher list) and read these 14 words' meanings there (H grade), ~$2
- 100 mssEC 18 entries still '?' - blocker: not-attempted; 20 have a dated OR match with margin under 2 and 80 none (D2-ECK62M); next: the image (marker words the volunteer text may have dropped) for the 20 `?p` entries, ~$4
- merged telegrams in the volunteer text (9985.564, 9991.571 run into a second heading) - blocker: not-attempted; the splitter's DATE pattern has no 'Apl' form; next: add the "Apl"/"Washn" heading forms to the entry splitter and re-split, then re-run --check across ec18 outputs, ~$1

## Escalation (R7C-ECK62C, 6 Oct 2026)
- [x] siblings: received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171); parallel sent ledger mssEC 18 opened by text 4 Oct 2026 (GAPS206), read with Cipher No. 1 (A3V3-ECK18) and No. 2 (A3V3-ECK2)
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [ ] known-keys: Lehigh row checked on the mssEC 41 key page image (DEF1-ECK62P); '?' entries assigned print-free (RUN6-ECK62) and by print (D2-ECK62M); zero-agree entries re-aligned under the other book (D2-ECK62R, 1 of 19), the flip carried (R7B-ECK62); next: the 1865 cipher book for the 14 R7C-ECK62C code words, ~$2
- [x] print: wrong-telegram test done (R7B-ECK62: 0 wrong, 7 right, 11 undecided); conflict-pair test done (R7C-ECK62C: 7-entry pool untested at N 93, 18-entry pool 14 cross-entry code words outside the keys)
- [x] key-rebuild: Koran/Lamb/Luna/Indus done 3 Oct 2026 (GAPS191); Handle, Harry, author added at C (A3V3-ECKC); possessive and collision guard added to decode.py (RUN3-ECK62)
- [x] image-check: the ten mssEC 15 readings reconciled against the image (reading.md); the six mssEC 18 collision/conflict entries (DEF1-ECK62I) and the Lehigh key row (DEF1-ECK62P)
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 6 internal gaps; cheapest next: the 1865 cipher book (Huntington mssEC key books) for the 14 cross-entry code words of R7C-ECK62C, ~$2

## R8-ECK62 (6 Oct 2026, account 1 worker for LANE LANE-RUN8-account-1): the 1865 cipher book for the 14 R7C-ECK62C code words

Step check: not run before (R7C-ECK62C, 6 Oct 2026, was the latest section). Job: find the 1865 cipher book among the Huntington
mssEC key books and look up the 14 cross-entry code words (grade H if found).

- Which book: the 14 words' entries date 30 Dec 1864 - 8 Apr 1865, plus 10040.638 (13 Jul 1865). Plum (via Tomokiyo,
  sources/cryptiana/web/civilwar1.htm): Cipher No. 3 from 25 Dec 1864, No. 4 from 23 Mar 1865, No. 5 from 20 Jun 1865; the three
  share one printed template (alphabetical printed code words, two runs per page, meanings handwritten) and "differ chiefly in the
  specific routes and meaning of arbitraries". So the book wanted is No. 3 / No. 4, with No. 5 only for the July entry.
- Huntington catalogue (CONTENTdm dmQuery, `title^cipher^all^and`, 36 records, 6 Oct 2026): cipher books mssEC 36-67 are
  No. 1 (39-46), No. 2 (47-48), No. 5 (49-66, 18 copies, "Cipher Book #5", cataloguer's date 1864-65 from p.4), No. 9 (67),
  Dept of the Gulf (38), handwritten (37, 40), Stager's key memoranda (36). **No copy of No. 3 or No. 4 is catalogued there.**
  Tomokiyo places a No. 4 copy (and a No. 5) in the Friedman Collection, Marshall Foundation digital archive
  (marshallfoundation.org/library/digital-archive/federal-army-cipher-books/): HTTP 403 Cloudflare block from this container,
  6 Oct 2026, not retried; the Wayback CDX for that path reset the connection twice, not retried further.
- No. 5 read anyway (mssEC 50, compound 758, pages 18, 24, 26, 29 at 1300 px, plus 450 px probes of pp.13, 17, 28, 33):
  11 of the 14 words are printed words of the template (Artist, Fence, Forge, Harm, Hoax, Hogarth, Joint, Level, Line, Loath,
  Lunch; scold, shower, thrash on pages not fetched). The No. 5 values read: Artist = Grant U.S., Hogarth = Lieutenant,
  Hoax = Leave, Loath = Report, Lunch = Retire; Harm, Line, Forge blank. **None matches** the R7C-ECK62C candidates (boats, river,
  Richmond, command, work, New Berne, Morehead City, move). Per word: not found (the period book is not digitised at the
  Huntington); table ec18/book5_lookup.tsv.
- 10040.638 (13 Jul 1865, OR I/48 pt 2 p.1072, "relieve Granger from command in Texas"): under No. 5 loath = Report, not command,
  and its word "giraffe" is not a printed No. 5 word (pp.24-25 run Gipsy-Girard, Gift-Girdle). So even this post-20-June entry was
  not enciphered in No. 5; No. 4 (or a book outside the series) stayed in use on that line.
- What it does establish: the neither-book entries use the No. 3/4/5 printed vocabulary (11 of 14 words checked present), which
  supports R7C-ECK62C's "later table, not transcription" reading. Nothing graded; nothing written into any key file; --check
  scripts re-run (ec18_confpair.py --check current, decode.py --check current).
- Requests: hdl.huntington.org 12 (3 API/dmwebservices, 9 IIIF images); marshallfoundation.org 1 (403); web.archive.org 2
  (connection reset). No subagents. Images kept in scratch, not committed (re-fetch:
  hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/1300,/0/default.jpg, pointers in the TSV).
  Report what was found and where it was not found; no novelty class.

## Remaining gaps (finish-or-blocker pass, R8-ECK62, 6 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82 (GAPS197); mssEC 18: 28 fully keyed Cipher No. 1 and 17 Cipher No. 2 entries (RUN3-ECK62), 26 print-aligned (A3V3-ECKC); 79 print-free-assigned entries read, 9991.571 now with book 1r (R7B-ECK62); 13 of the 113 '?' entries given a book by print (D2-ECK62M); 57 dated matches aligned (AGREE 325/816 = 0.398 vs control 0.075 after the carry); 18 neither-book entries: 0 wrong telegram, 7 right, 11 undecided (R7B-ECK62, gate PASS); conflict-pair test: 7-entry pool untested (power 0.61), 18-entry pool 14 cross-entry code words p 0.0005 (R7C-ECK62C, descriptive); the 14 words looked up in Cipher No. 5 (mssEC 50): 11 printed in its template, 0 of 8 read values match, none carried (R8-ECK62)
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; every OR volume that could hold Feb-Jul 1862 telegrams grepped and aligned (GAPS113-GAPS153), received ledgers read (GAPS171), residue regenerated (GAPS197); next: a received-ledger pass on mssEC 04-14 (not yet harvested) by the GAPS171 method, ~$2
- residue code words not fixed by any known plaintext - blocker: open-codes; about 860 oov tokens remain (GAPS197); conflicts Lamb, Luna date-separated, Indus split by slot; table-change dates unwitnessed between 21 Mar and 25 May
- 1863-67 sent ledgers at grade H - blocker: not-attempted; Lehigh conflict held M with witnesses (DEF1-ECK62P); next: the received copies of the 27 Jan and 24 May 1865 telegrams (Eckert received ledgers) for a third witness, ~$2
- 18 neither-book entries (R7C-ECK62C confpair_pairs.tsv) - blocker: no-key-material; the 14 code words date 30 Dec 1864 - 13 Jul 1865, i.e. Cipher No. 3 (from 25 Dec 1864) and No. 4 (from 23 Mar 1865) per Plum via Tomokiyo; the Huntington holds only No. 5 (mssEC 49-66, from 20 Jun 1865); 11 of the 14 are printed words of the shared No. 3/4/5 template but No. 5's meanings match none of 8 read (R8-ECK62, ec18/book5_lookup.tsv); the one known No. 4 copy (Friedman Collection, Marshall Foundation digital archive) is Cloudflare-blocked from the cloud (403, 6 Oct 2026); next: the No. 4 copy read from a desk browser (LOCAL-QUEUE row, owner's machine), ~$1
- 100 mssEC 18 entries still '?' - blocker: not-attempted; 20 have a dated OR match with margin under 2 and 80 none (D2-ECK62M); next: the image (marker words the volunteer text may have dropped) for the 20 `?p` entries, ~$4
- merged telegrams in the volunteer text (9985.564, 9991.571 run into a second heading) - blocker: not-attempted; the splitter's DATE pattern has no 'Apl' form; next: add the "Apl"/"Washn" heading forms to the entry splitter and re-split, then re-run --check across ec18 outputs, ~$1

## Escalation (R8-ECK62, 6 Oct 2026)
- [x] siblings: received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171); parallel sent ledger mssEC 18 opened by text 4 Oct 2026 (GAPS206), read with Cipher No. 1 (A3V3-ECK18) and No. 2 (A3V3-ECK2)
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [ ] known-keys: Lehigh row checked on the mssEC 41 key page image (DEF1-ECK62P); '?' entries assigned print-free (RUN6-ECK62) and by print (D2-ECK62M); zero-agree entries re-aligned under the other book (D2-ECK62R, 1 of 19), the flip carried (R7B-ECK62); Huntington cipher books searched for No. 3/No. 4: none (No. 5 only, mssEC 49-66), No. 5 values match none of the 14 words (R8-ECK62); next: Cipher No. 4 in the Friedman Collection (Marshall Foundation), from a desk browser, ~$1
- [x] print: wrong-telegram test done (R7B-ECK62: 0 wrong, 7 right, 11 undecided); conflict-pair test done (R7C-ECK62C: 7-entry pool untested at N 93, 18-entry pool 14 cross-entry code words outside the keys)
- [x] key-rebuild: Koran/Lamb/Luna/Indus done 3 Oct 2026 (GAPS191); Handle, Harry, author added at C (A3V3-ECKC); possessive and collision guard added to decode.py (RUN3-ECK62)
- [x] image-check: the ten mssEC 15 readings reconciled against the image (reading.md); the six mssEC 18 collision/conflict entries (DEF1-ECK62I) and the Lehigh key row (DEF1-ECK62P)
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 5 internal gaps; cheapest next: add the "Apl"/"Washn" heading forms to the entry splitter and re-split (~$1); the No. 4 book for the 14 words waits on a desk-browser read of the Friedman copy

## R9-ECK62 (6 Oct 2026, account 1 worker for LANE LANE-RUN9-account-1): "Apl"/"Mch" heading forms in the entry splitter, re-split

Step check: not run before (R8-ECK62's Verdict named it as cheapest next). vol18.json re-fetched (1 request, sha256 matches
pilot1864/manifest.tsv).
- Survey of dated lines inside entry bodies (legacy splitter): the ledger abbreviates April "Apl" (46 body lines) and March "Mch"
  (12); "Washn" itself was not the problem (DATE never needed the place word, and "Washn"/"Wash"/"Wash." already sit in 750+
  headers). Two causes of merges: a block opening with an "Apl"/"Mch" heading did not open an entry, and many telegrams follow one
  another with no blank line, so a heading inside a block was never looked for.
- `ec18/ec18.py`: `DATE2` (DATE plus Apl -> April, Mch -> March), `HEAD2` (a DATE2 date with year closing the line, optionally a
  time), `entries(data, split2=True)` opens an entry at a DATE2 date in a block's first three lines or at any HEAD2 line inside a
  block. Default `split2=False` is the committed splitter: checked identical to the pre-edit function (same 671 entries, ids,
  headers and bodies), so no committed output changes and every committed `--check` stays current. Split-off parts keep their
  parent's id with a letter suffix (9985.564 -> 9986.564b, 9986.564c), so no legacy id is renumbered.
- New option `ec18.py DATA --split-report --write|--check` -> `ec18/split2.tsv` (`--check` current), with a known answer
  (9985.564 must separate at "Hon CA Dana Richmond Va  Washn Apl 5 1865", R7B-ECK62): PASS.
- **Counts: 671 entries before, 729 after; 25 legacy entries split into 58 further parts; 0 merges.** Every split-off header was
  read by eye: all 58 are telegram headings (operator or addressee, place, "Wash"/"Washn"/"Washington"/"City Point"/"Nashville",
  date). Biggest: 9703.69 (13 Apr 1864, 117 body lines -> 5 plus 8 parts to 18 Apr), 9718.75, 9720.76, 9966.542, 9993.572,
  9998.576. By month: Mar-Apr 1864 (legacy entries of 31 Mar-23 Apr, 9, 26 parts), Mar 1865 (6 entries, 12 parts), Apr 1865 (10 entries,
  20 parts).
- Committed analyses that hold a split entry: wrongtel targets 2 (9969.543, 9985.564 -- both also in the confpair 18-pool and
  assign_free), print_q '?' 1 (9709.70), assign_free 6 (9698.62, 9709.70, 9969.543, 9985.564, 9991.571, 9996.575). So R7B-ECK62's
  "9985.563/9985.564 share OR 46.3 p.572" and the confpair hits drawn from 9969.543/9985.564 rest partly on merged text.
- Residue: at a mid-block split the line just above the heading (a serial or time, e.g. "No 4  5 pm") stays at the end of the
  previous part's body; 9969.543b's heading is a received-time line ("1215 AM Mch 3d  City Point Mch 2d 1865") and may be a
  receipt note rather than a separate telegram -- left as the rule splits it.
- Also fixed: `--book-test` raised NameError (the book-rule function had been defined as a second `main` and shadowed); renamed
  `book_test`, runs: 29/31 right, 0 wrong book, 2 unassigned.
- Re-run: `ec18_confpair.py --check` current, `decode.py --check` current, `ec18.py --split-report --check` current. Not re-run:
  the OR-dependent `--check`s (main, `--assign`, `--print-q`, `ec18_align.py`, `ec18_wrongtel.py`; 48 OR `_djvu.txt` not fetched
  this job) -- unchanged by construction since the default splitter is byte-identical. No key, book, grade or reading changed; no
  new key values. Requests: hdl.huntington.org 1. No subagents.
  Report what was found and where it was not found; no novelty class.

## R10-ECK62S (6 Oct 2026, account 1 worker for LANE LANE-RUN10-account-1): split2 cascade regeneration

Step check: not run before (R9-ECK62's Verdict named it). Data re-fetched to scratch, not committed: vol18.json (sha256
cb162574..., matches pilot1864/manifest.tsv), DIR62 8 `_djvu.txt`, OR 32.1-49.2 48 `_djvu.txt` (all 48 sha256 match
or_volumes.tsv).
- Code: `--split2` on every ec18.py mode and on ec18_align.py / ec18_wrongtel.py / ec18_confpair.py (module flag
  `ec18.SPLIT2`; `entries()` defaults to it). Outputs go to `ec18/s2/` under the legacy file names; an input is read from
  `s2/` when this run wrote it, else from `ec18/` (`ec18.src()`). Without the flag nothing changes: the legacy split and every
  legacy output stay as committed (legacy `--check` re-run after the edit, see below).
- Legacy outputs found stale before any edit (same result with the unedited scripts, stash test): `readings.md`, the four
  `_b2` outputs (an eckert-1864 key-no2.md edit since they were written: 5 entries gain one keyed token, 9746.115 joins the
  fully keyed No. 2 entries -- fully_keyed 17 -> 18, H 253 -> 294, real-date OR matches 12 -> 13, permuted mean 0.75 -> 0.90,
  max 2 -> 3), and `print_free.tsv` (built on OR 41.1-46.3, D1-ECK62P; stale on that same subset too, since readings_free
  changed in R7B-ECK62's carry). Regenerated under rule 7 with their committed flags (`print_free` with OR 41.1-46.3); the
  cascade below (`ec18_align.py` default, which reads matches_b2) regenerated in step.
- split2 cascade (`--split2 --write`, then `--check`; same flags as the committed legacy runs: `--possessive --guard DIR62`;
  print-free on OR 41.1-46.3; ORDIR 32.1-49.2 elsewhere). Legacy -> split2:
  entries 671 -> 729 (book 1 311 -> 328, 2 168 -> 175, ? 192 -> 226); all-entry dated OR matches book-1 read 326 -> 350;
  fully keyed No. 1 entries 28 both ways;
  `--assign` known answer 257/267 = 0.963 -> 272/280 = 0.971, '?' print-matched 78 -> 88;
  `--assign-free` known answer 0.896 (479) -> 0.897 (503), shuffled mean/max 0.571/0.707 -> 0.575/0.710, '?' decided 79 -> 89
  (1: 28, 2: 61);
  `--print-q` '?' 113 -> 137, known precision 242/259 = 0.934 -> 256/270 = 0.948, dated '?' matches 33 -> 42;
  `ec18_align --rows align_free_rows.tsv` entries 57 -> 59, AGREE 325/816 = 0.398 -> 326/764 = 0.427, control 0.075 -> 0.088,
  grades H 61 C 360 S 500 I 1 -> H 70 C 363 S 430 I 1;
  `--rows align_flip_rows.tsv` (legacy rows file, no split2 rows list exists) AGREE 20/261 -> 14/227, control 6/261 -> 4/227.
- The named entries: 9969.543 keeps book 2f (6/2 support) and its split-off 9969.543b (the received-time line R9-ECK62 flagged)
  is '?' with nothing keyed to decide it; 9985.564 splits into 9985.564 / 9986.564b / 9986.564c, all three '?' (legacy 2f);
  9709.70 and 9709.70b both stay '?' with no dated match; 9698.62 is book 2 by marker once 9699.62c (book 1f) is split
  off; 9991.571 is book 1 by marker under split2 -- the same book R7B-ECK62 carried as `1r` from the print alignment (an
  independent agreement), 9992.571b '?'; 9996.575's part 9997.575b is 2f.
- Not regenerated under split2: `ec18_wrongtel.py` stops on its pre-registered assertion (PREREG-ECK62-WRONGTEL: 18 targets,
  14 positive controls) -- split2 gives 16 positive-control entries at agree >= 0.75, so the registered rule does not apply as
  written; not amended here. `ec18_confpair.py` reads wrongtel_entries.tsv, so it is not regenerated either (a trial run on
  mixed legacy/split2 inputs was discarded). Both stay legacy-only; a split2 run needs a new prereg naming the new pools.
- Checks: all 12 split2 outputs `--split2 --check` current; all 12 legacy runs `--check` current after the rule-7 regeneration (legacy wrongtel and confpair inputs unchanged, `--check` current at start); `ec18.py --split-report --check` current.
- No key, book assignment in the committed (legacy) analyses, grade or reading claim changed by the split2 run; the split2
  numbers are in ec18/s2/ for the next step to adopt or not. Requests: hdl.huntington.org 1, archive.org 56, >= 1.6 s apart.
  0 subagents. Report what was found and where it was not found; no novelty class.

## Remaining gaps (finish-or-blocker pass, R9-ECK62, 6 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82 (GAPS197); mssEC 18: 28 fully keyed Cipher No. 1 and 17 Cipher No. 2 entries (RUN3-ECK62), 26 print-aligned (A3V3-ECKC); 79 print-free-assigned entries read, 9991.571 now with book 1r (R7B-ECK62); 13 of the 113 '?' entries given a book by print (D2-ECK62M); 57 dated matches aligned (AGREE 325/816 = 0.398 vs control 0.075 after the carry); 18 neither-book entries: 0 wrong telegram, 7 right, 11 undecided (R7B-ECK62, gate PASS); conflict-pair test: 7-entry pool untested (power 0.61), 18-entry pool 14 cross-entry code words p 0.0005 (R7C-ECK62C, descriptive); the 14 words looked up in Cipher No. 5 (mssEC 50): 11 printed in its template, 0 of 8 read values match, none carried (R8-ECK62)
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; every OR volume that could hold Feb-Jul 1862 telegrams grepped and aligned (GAPS113-GAPS153), received ledgers read (GAPS171), residue regenerated (GAPS197); next: a received-ledger pass on mssEC 04-14 (not yet harvested) by the GAPS171 method, ~$2
- residue code words not fixed by any known plaintext - blocker: open-codes; about 860 oov tokens remain (GAPS197); conflicts Lamb, Luna date-separated, Indus split by slot; table-change dates unwitnessed between 21 Mar and 25 May
- 1863-67 sent ledgers at grade H - blocker: not-attempted; Lehigh conflict held M with witnesses (DEF1-ECK62P); next: the received copies of the 27 Jan and 24 May 1865 telegrams (Eckert received ledgers) for a third witness, ~$2
- 18 neither-book entries (R7C-ECK62C confpair_pairs.tsv) - blocker: no-key-material; the 14 code words date 30 Dec 1864 - 13 Jul 1865, i.e. Cipher No. 3 (from 25 Dec 1864) and No. 4 (from 23 Mar 1865) per Plum via Tomokiyo; the Huntington holds only No. 5 (mssEC 49-66, from 20 Jun 1865); 11 of the 14 are printed words of the shared No. 3/4/5 template but No. 5's meanings match none of 8 read (R8-ECK62, ec18/book5_lookup.tsv); the one known No. 4 copy (Friedman Collection, Marshall Foundation digital archive) is Cloudflare-blocked from the cloud (403, 6 Oct 2026); next: the No. 4 copy read from a desk browser (LOCAL-QUEUE row, owner's machine), ~$1
- 100 mssEC 18 entries still '?' - blocker: not-attempted; 20 have a dated OR match with margin under 2 and 80 none (D2-ECK62M); next: the image (marker words the volunteer text may have dropped) for the 20 `?p` entries, ~$4
- merged telegrams in the volunteer text - blocker: not-attempted; the split2 cascade is regenerated in ec18/s2/ (R10-ECK62S: 729 entries, print_q known 0.948, align_free AGREE 0.427 vs control 0.088) but the committed analyses still use the legacy split, and wrongtel/confpair do not run under split2 (pre-registered pool sizes 18/14 become 18/16); next: a prereg for the split2 wrongtel/confpair pools and the decision to adopt s2/ as the committed cascade, ~$2

## Escalation (R9-ECK62, 6 Oct 2026)
- [x] siblings: received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171); parallel sent ledger mssEC 18 opened by text 4 Oct 2026 (GAPS206), read with Cipher No. 1 (A3V3-ECK18) and No. 2 (A3V3-ECK2)
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [ ] known-keys: Lehigh row checked on the mssEC 41 key page image (DEF1-ECK62P); '?' entries assigned print-free (RUN6-ECK62) and by print (D2-ECK62M); zero-agree entries re-aligned under the other book (D2-ECK62R, 1 of 19), the flip carried (R7B-ECK62); Huntington cipher books searched for No. 3/No. 4: none (No. 5 only, mssEC 49-66), No. 5 values match none of the 14 words (R8-ECK62); next: Cipher No. 4 in the Friedman Collection (Marshall Foundation), from a desk browser, ~$1
- [x] print: wrong-telegram test done (R7B-ECK62: 0 wrong, 7 right, 11 undecided); conflict-pair test done (R7C-ECK62C: 7-entry pool untested at N 93, 18-entry pool 14 cross-entry code words outside the keys)
- [x] key-rebuild: Koran/Lamb/Luna/Indus done 3 Oct 2026 (GAPS191); Handle, Harry, author added at C (A3V3-ECKC); possessive and collision guard added to decode.py (RUN3-ECK62)
- [x] image-check: the ten mssEC 15 readings reconciled against the image (reading.md); the six mssEC 18 collision/conflict entries (DEF1-ECK62I) and the Lehigh key row (DEF1-ECK62P)
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 5 internal gaps; cheapest next: a received-ledger pass on mssEC 04-14 (~$2) or a split2 wrongtel/confpair prereg and the adopt-s2 decision (~$2); the No. 4 book for the 14 words waits on a desk-browser read of the Friedman copy

## R10-ECK62T (6 Oct 2026, account 1 worker for LANE LANE-RUN10-account-1): split2 wrongtel/confpair PREREG and run, adopt-s2 decision

Step check: not run before (R10-ECK62S named it). Pre-registered and pushed before any split2 flip, wrongtel or confpair
number: `ec18/PREREG-ECK62-S2.md` (commit 65eaa5ef0). The brief's "16-target pool" is the split2 positive control; the
mechanical target selection (FLIP rule 1 on `s2/align_free_entries.tsv`) gives 17 (legacy 18 minus 9985.564, which split2 cuts
into three undated '?' parts). Data re-fetched to scratch, not committed: vol18.json (sha256 cb162574..., matches
pilot1864/manifest.tsv), OR 32.1-49.2 48 `_djvu.txt` (all 48 sha256 match or_volumes.tsv).
- Code: `ec18/ec18_fliprows.py --split2 --write|--check` writes `s2/align_flip_rows.tsv` (17) and `s2/align_flipctl_rows.tsv`
  (16) by FLIP rules 1-2; `ec18_wrongtel.py --split2` asserts 17/16 (legacy assertion 18/14 unchanged); `ec18_confpair.py
  --split2` takes its primary pool from the split2 wrongtel `right-telegram` class. Fixed: `ec18_confpair.py` read its mode
  from argv[1], so `--split2 --write` ran as a check; it now looks for `--write` anywhere (legacy calls behave as before).
  `s2/align_flip_*` from R10-ECK62S (a split2 run on the legacy rows file, AGREE 14/227) are replaced by the prereg's split2
  rows run.

| instrument | legacy | split2 |
|---|---|---|
| flip selection / flip control | 19 / 14 | 17 / 16 |
| flipped target AGREE | 20/261 = 0.077 | 8/219 = 0.037 |
| flip-control AGREE (gate <= 0.15) | 16/132 = 0.121 PASS | 17/151 = 0.113 PASS |
| accepted flips (rule 4) | 1 (9991.571) | 0 (9991.571 is book 1 by marker under split2) |
| wrongtel pos median / p10; neg median / p90 | 0.871 / 0.676; 0.206 / 0.296 | 0.889 / 0.688; 0.203 / 0.316 |
| wrongtel gate | PASS | PASS |
| targets: wrong / right / undecided | 0 / 7 / 11 (of 18) | 0 / 5 / 12 (of 17) |
| confpair primary (right-telegram pool) | 7 entries, 93 pairs, S 0, p 1.0, power 0.610 FAIL | 5 entries, 60 pairs, S 0, p 1.0, power 0.345 FAIL |
| confpair all targets (descriptive) | 18, 376 pairs, S 18, p 0.0005, power 1.0 | 17, 368 pairs, S 15, p 0.0005, power 1.0 |
| confpair strict (descriptive) | S 14, p 0.0005 | S 13, p 0.0005 |

- Right -> undecided under split2: 9969.543 (0.632; its received-time line split off as 9969.543b) and 9985.563 (0.686, just
  under the new p10 0.688). Targets sharing an OR page: 2 -> 0 (the 9985.563/9985.564 pair was merged text).
- Pre-registered verdict, primary pool: **untested-by-this-tool at N = 60** (power 0.345 < 0.80), as in legacy (N = 93). Not
  a negative.
- Descriptive cross-entry code words, split2 strict (13): artists = boats, thrash = Ohio [rail]road, hogarth = river, harm =
  New Berne, levels = cars, line = Morehead City, loath = command, scold = number, shower = order, forge = move, lunch = work,
  joint = telegraph, fence = left. Lost against legacy: **hoax = Richmond** (its second context was 9985.564's merged text;
  under split2 it rests on one entry) and credit = Weitzel (same page pair). Candidates only, ungraded; no key file touched.
- **Adopt-s2 decision (PREREG-ECK62-S2): ADOPT.** A1 every new split2 run and every legacy run `--check` current (fliprows,
  align flip/flipctl s2 and legacy, align free legacy, wrongtel s2 and legacy, confpair s2 and legacy, `--split-report`,
  decode.py); the other R10-ECK62S split2 outputs were `--check` current at 10:39 and their inputs (ec18.py, ec18_align.py,
  s2 inputs) are unedited since. A2 split known answer PASS. A3 floor holds (assign 0.963 -> 0.971, assign_free 0.896 ->
  0.897, print_q 0.934 -> 0.948, align_free margin 0.323 -> 0.339; on file before the prereg, not blind). A4 (blind) FLIP
  gate and wrongtel gate both PASS on split2. So later steps read `ec18/s2/`; the legacy files stay committed and `--check`
  current; nothing deleted. No key, book, grade or reading claim changed.
- Requests: hdl.huntington.org 1, archive.org 48, >= 1.6 s apart. 0 subagents, 0 vision. Report what was found and where it
  was not found; no novelty class.

## Remaining gaps (finish-or-blocker pass, R10-ECK62T, 6 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82 (GAPS197); mssEC 18 cascade now split2 (ec18/s2/, adopted R10-ECK62T): 729 entries, print_q known 0.948, align_free AGREE 326/764 = 0.427 vs control 0.088; 17 neither-book entries: 0 wrong telegram, 5 right, 12 undecided (gate PASS); conflict-pair primary untested (power 0.345 at N 60), all-17 pool 13 strict cross-entry code words p 0.0005 (descriptive); the 14 legacy words looked up in Cipher No. 5: none carried (R8-ECK62)
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; every OR volume that could hold Feb-Jul 1862 telegrams grepped and aligned (GAPS113-GAPS153), received ledgers read (GAPS171), residue regenerated (GAPS197); next: a received-ledger pass on mssEC 04-14 (not yet harvested) by the GAPS171 method, ~$2
- residue code words not fixed by any known plaintext - blocker: open-codes; about 860 oov tokens remain (GAPS197); conflicts Lamb, Luna date-separated, Indus split by slot; table-change dates unwitnessed between 21 Mar and 25 May
- 1863-67 sent ledgers at grade H - blocker: not-attempted; Lehigh conflict held M with witnesses (DEF1-ECK62P); next: the received copies of the 27 Jan and 24 May 1865 telegrams (Eckert received ledgers) for a third witness, ~$2
- 17 neither-book entries (s2/confpair_pairs.tsv) - blocker: no-key-material; the 13 code words date 30 Dec 1864 - 13 Jul 1865, Cipher No. 3/No. 4 period; the Huntington holds only No. 5 (R8-ECK62); the one known No. 4 copy (Friedman Collection, Marshall Foundation) is Cloudflare-blocked from the cloud (403, 6 Oct 2026); next: the No. 4 copy read from a desk browser (LOCAL-QUEUE row, owner's machine), ~$1
- mssEC 18 entries still '?' - blocker: not-attempted; 100 under the legacy split, 137 '?' entries under split2 print_q; next: the image (marker words the volunteer text may have dropped) for the dated `?p` entries under split2, ~$4

## Escalation (R10-ECK62T, 6 Oct 2026)
- [x] siblings: received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171); parallel sent ledger mssEC 18 opened by text 4 Oct 2026 (GAPS206), read with Cipher No. 1 (A3V3-ECK18) and No. 2 (A3V3-ECK2)
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [ ] known-keys: Huntington cipher books searched for No. 3/No. 4: none (No. 5 only, mssEC 49-66), No. 5 values match none of the 14 words (R8-ECK62); next: Cipher No. 4 in the Friedman Collection (Marshall Foundation), from a desk browser, ~$1
- [x] print: wrong-telegram and conflict-pair tests done on legacy (R7B-ECK62, R7C-ECK62C) and split2 (R10-ECK62T: 0 wrong, 5 right, 12 undecided; primary untested at N 60); splitter fixed and adopted (R9-ECK62, R10-ECK62S, R10-ECK62T)
- [x] key-rebuild: Koran/Lamb/Luna/Indus done 3 Oct 2026 (GAPS191); Handle, Harry, author added at C (A3V3-ECKC); possessive and collision guard added to decode.py (RUN3-ECK62)
- [x] image-check: the ten mssEC 15 readings reconciled against the image (reading.md); the six mssEC 18 collision/conflict entries (DEF1-ECK62I) and the Lehigh key row (DEF1-ECK62P)
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 4 internal gaps; cheapest next: a received-ledger pass on mssEC 04-14 by the GAPS171 method, ~$2; the No. 4 book for the 13 words waits on a desk-browser read of the Friedman copy

## D1-ECK62L (6 Oct 2026, account 1 worker for LANE DEFAULT-account-1-20261006-1240): received ledgers mssEC 04-14 by the GAPS171 method

- Harvest: one CONTENTdm `dmQuery` per ledger on `callid` (the GAPS171 URL form), fetched once 6 Oct 2026; rows appended to
  print/residue/received_manifest.tsv with sha256 (texts not committed, their credit; re-fetch). mssEC 01-03 and the 58
  residue pages of mssEC 15 were re-fetched by the same route: all 01-03 sha256 and all 58 page-text sha256 match the
  GAPS171/pages_manifest values. Spans, by year counts in the volunteer text: 04 Apr-Jul 1863 (288 pages), 05 Aug-Dec
  1862 into 1863 (408), 06 and 07 Apr-Jul 1863 (442, 410), 08 and 09 Jul-Nov 1863 (414 each), 10 and 11 Apr-Jul 1864
  (414 each), 12 and 13 Jan-Aug 1865 (414 each), 14 1866-67 (104). 3,987 pages with text in all. None of them covers
  Feb-Jul 1862, the residue's own span, so few twins were expected.
- `print/received_match.py` gains `--vols` (default 01,02,03 unchanged: `--check` on the committed GAPS171 TSV exits 0).
  Run `--vols 04,...,14 --write` -> print/residue/received_match_04-14.tsv: 124 residue entries, null p99 0, threshold 3;
  control (a) synthetic coded twins 60/60 at rank 1 (0.72 code words per 40-word window, below the residue's 1.28 because
  the 1863-67 vocabulary carries fewer 1862 key meanings: a weaker control than GAPS171's); control (b) 270 of 3,715
  pages of 05-14 have a twin in 04 (duplicate copies across ledgers are common in these years).
- Result: 2 entries at the threshold (score 3), both read and rejected as non-twins: 5021.2 (25 Feb 1862, Marcy to Lander)
  shares only "at short notice signed R B Marcy" with mssEC 05 p.195 (27 Oct 1862, Marcy to Col. Clarke); 5035.1 (3 Mar
  1862, to Rosecrans) shares only "the South Branch of the Potomac" with mssEC 11 p.11 (1 Feb 1864, Meade's HQ to Halleck).
  Different dates, senders' business and wording otherwise. Entries matched: 0. Residue unchanged, 124 entries before
  and after; no reading or key change, so decode.py --check not needed (run anyway: see the done line). The
  shuffled-word null does not model shared formula and place-name phrases at 3,987 pages; a threshold-3 hit
  needs reading before it counts as a twin.
- Witness found outside the twin search (GAPS171's one-telegram-word check, applied to 04-14): Nutmeg occurs once, mssEC 04
  p.210 (object 4359), Fort Monroe 5 Jul 1863, Ludlow to Dix: "the Confederate tug torpedo left her anchorage above new
  ports news at half past one this after noon and proceeded up the Nutmeg". OR ser. II vol. 6 p.83 (Internet Archive
  warofrebellion0206rootrich, djvu text, grepped) prints the same report to Stanton: "left her anchorage at 1.30 p.m. this
  afternoon and proceeded up the James River". Aligned: Nutmeg = James River (C, received direction, 5 Jul 1863). The
  same page carries Ludlow's copy to Stanton via Eckert in another code: Hannibal = James River, Martha = 1.30 [p.m.],
  Japan = City Point (C, same print). key.md has Japan = Manassas (C, 25 May 1862): code words were reused with new
  values between 1862 and 1863, so this 1863 witness agrees with the 1862 proposal Nutmeg = James River (5035.1, 3 Mar
  1862, one telegram; GAPS142) but does NOT reach the >= 2 telegrams bar for an 1862 row. key.md unchanged; the
  proposal stays held. Other one-telegram words in 04-14: Ellen 4 (one is the ship "Ellen S Terry", plain), Luna 4
  (all mssEC 04, 1863, one a signature "Luna Commanding"), Lamb 7, Dawn 3, Andes 1 (a transposition-route 1863 text),
  Indus 0; none read further (1863+ books, not the 1862 key).
- Not done (one-line suggestion, rule 7): mssEC 12-13 (Jan-Aug 1865) are now harvested; they are where the received copies
  of the 27 Jan and 24 May 1865 telegrams would be (the Lehigh third witness gap), ~$1.5.
- Requests: hdl.huntington.org 16 (15 ledger queries, one retry of mssEC 07 after an empty reply); archive.org 4
  (2 advancedsearch, 2 djvu text: warofrebellion273unit, ser. I vol. 27 pt 3, no hit; warofrebellion0206rootrich).
  No vision, no subagents.

## Remaining gaps (finish-or-blocker pass, D1-ECK62L, 6 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82 (GAPS197); received ledgers mssEC 01-14 all searched for residue twins (GAPS171, D1-ECK62L): 0 code-bearing twins; mssEC 18 cascade split2 (ec18/s2/): 729 entries, align_free AGREE 0.427 vs control 0.088; 17 neither-book entries: 0 wrong telegram, 5 right, 12 undecided
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; every OR volume that could hold Feb-Jul 1862 telegrams grepped and aligned (GAPS113-GAPS153), received ledgers mssEC 01-14 searched (GAPS171, D1-ECK62L, 0 twins); next: the image of the residue pages against the volunteer text for the M-graded tokens (transcription slips the decode reads as code), ~$4
- residue code words not fixed by any known plaintext - blocker: open-codes; about 860 oov tokens remain (GAPS197); conflicts Lamb, Luna date-separated, Indus split by slot; Nutmeg = James River gains a 5 Jul 1863 witness (C, D1-ECK62L) but no second 1862 telegram; table-change dates unwitnessed between 21 Mar and 25 May
- 1863-67 sent ledgers at grade H - blocker: not-attempted; Lehigh conflict held M with witnesses (DEF1-ECK62P); next: the received copies of the 27 Jan and 24 May 1865 telegrams in mssEC 12-13 (harvested 6 Oct 2026, D1-ECK62L) for a third witness, ~$1.5
- 17 neither-book entries (s2/confpair_pairs.tsv) - blocker: no-key-material; the 13 code words date 30 Dec 1864 - 13 Jul 1865, Cipher No. 3/No. 4 period; the Huntington holds only No. 5 (R8-ECK62); the one known No. 4 copy (Friedman Collection, Marshall Foundation) is Cloudflare-blocked from the cloud (403, 6 Oct 2026); next: the No. 4 copy read from a desk browser (LOCAL-QUEUE row, owner's machine), ~$1
- mssEC 18 entries still '?' - blocker: not-attempted; 100 under the legacy split, 137 '?' entries under split2 print_q; next: the image (marker words the volunteer text may have dropped) for the dated `?p` entries under split2, ~$4

## Escalation (D1-ECK62L, 6 Oct 2026)
- [x] siblings: received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171) and mssEC 04-14 6 Oct 2026 (D1-ECK62L, 0 twins, Nutmeg 1863 witness); parallel sent ledger mssEC 18 opened by text 4 Oct 2026 (GAPS206), read with Cipher No. 1 (A3V3-ECK18) and No. 2 (A3V3-ECK2)
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [ ] known-keys: Huntington cipher books searched for No. 3/No. 4: none (No. 5 only, mssEC 49-66), No. 5 values match none of the 14 words (R8-ECK62); next: Cipher No. 4 in the Friedman Collection (Marshall Foundation), from a desk browser, ~$1
- [x] print: wrong-telegram and conflict-pair tests done on legacy (R7B-ECK62, R7C-ECK62C) and split2 (R10-ECK62T: 0 wrong, 5 right, 12 undecided; primary untested at N 60); splitter fixed and adopted (R9-ECK62, R10-ECK62S, R10-ECK62T)
- [x] key-rebuild: Koran/Lamb/Luna/Indus done 3 Oct 2026 (GAPS191); Handle, Harry, author added at C (A3V3-ECKC); possessive and collision guard added to decode.py (RUN3-ECK62)
- [x] image-check: the ten mssEC 15 readings reconciled against the image (reading.md); the six mssEC 18 collision/conflict entries (DEF1-ECK62I) and the Lehigh key row (DEF1-ECK62P)
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 4 internal gaps; cheapest next: the 1865 received copies in mssEC 12-13 for the Lehigh third witness, ~$1.5; the No. 4 book for the 13 words waits on a desk-browser read of the Friedman copy

## D1-ECK62W (6 Oct 2026, account 1 worker for LANE DEFAULT-account-1-20261006-1240): the 1865 received copies in mssEC 12-13 for the Lehigh third witness

- Material: mssEC 12 and 13 received ledgers, one CONTENTdm `dmQuery` each (the D1-ECK62L URL form in
  print/residue/received_manifest.tsv), re-fetched to scratch 6 Oct 2026 (not on disk from D1-ECK62L); both sha256 match
  the manifest (8631ce26..., 388e5a70...). 828 pages; volunteer text, not image. Year counts in the text: Jan-Aug 1865
  with a 1866 tail, so both dates (27 Jan, 24 May 1865) fall inside the span.
- Targets: 9947.505 (27 Jan 1865, Halleck to Dodge, OR ser. I vol. 48.1 p. 646, "Lehigh" where the print has "general
  Canby") and 10020.609 (24 May 1865, Grant to Dodge, OR 48.2 p. 573, "lehigh" where the print has "can [be provided]").
- Method (GAPS171 shape, one-off, scratch script): each entry's text with the print's values in place of the code words,
  word 5-grams, 5-grams on >= 3 pages dropped, best-page score; null = the same words shuffled (20 draws, seed 171);
  positive control = the entry text planted into a random page (20 draws). Plus keyword greps: Lehigh, Hurlbut, Canby,
  Dodge, and the bodies' distinctive phrases (mounted at, cavalry depot, depot at St, you can spare, best advantage,
  mounted men, transportation can, can be provided).
- Result: best-page score 0 for both entries (null max 0); planted control 20/20 at rank 1 -- a weak control (verbatim
  plants; it shows only that a copy in clear would be found, not a paraphrase). No received copy of either telegram in
  mssEC 12-13. "Lehigh" occurs once, as the monitor Lehigh (mssEC 12 p.165, Fort Monroe 14 Mar 1865, clear). Hurlbut
  occurs twice (mssEC 12 pp. 51, 87: Grant on Canby's subordinates, Jan-Feb 1865), neither a copy of the target.
  Nearest related page: mssEC 12 p.78 (object 7736), Dodge at St Louis to Halleck, 29 Jan 1865: "I sent one regt of
  Infantry yesterday, will send another tomorrow or next day" -- infantry, not cavalry, names neither Canby nor Hurlbut,
  and answers an order of 26 Jan; not a witness for Lehigh either way.
- Why few hits were expected: both telegrams were sent from Washington to St Louis; Washington's received book carries
  the reply side, not the sent message. The reply side gave nothing that names the cavalry's destination.
- Lehigh conflict unchanged (rule 4): witness A (key, mssEC 41 p.17 l.6, Hurlbut, image-checked) vs witness B (two
  1865 sent telegrams, print Canby / "can be"); no third witness found in mssEC 12-13. Held M. No key, reading or
  transcription change, so no --check needed for the readings (decode.py --check run anyway, see the done line).
- Not found / not searched: the St Louis (Dept of the Missouri) received copies are not in the Huntington Eckert ledgers;
  no other sent use of Lehigh was grepped in mssEC 18-19 here (needs vol18/vol19 text, not on disk).
- Requests: hdl.huntington.org 2 (two dmQuery, 2 s apart). No vision, no subagents.

## Remaining gaps (finish-or-blocker pass, D1-ECK62W, 6 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82 (GAPS197); received ledgers mssEC 01-14 all searched for residue twins (GAPS171, D1-ECK62L): 0 code-bearing twins; mssEC 18 cascade split2 (ec18/s2/): 729 entries, align_free AGREE 0.427 vs control 0.088; 17 neither-book entries: 0 wrong telegram, 5 right, 12 undecided
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; every OR volume that could hold Feb-Jul 1862 telegrams grepped and aligned (GAPS113-GAPS153), received ledgers mssEC 01-14 searched (GAPS171, D1-ECK62L, 0 twins); next: the image of the residue pages against the volunteer text for the M-graded tokens (transcription slips the decode reads as code), ~$4
- residue code words not fixed by any known plaintext - blocker: open-codes; about 860 oov tokens remain (GAPS197); conflicts Lamb, Luna date-separated, Indus split by slot; Nutmeg = James River gains a 5 Jul 1863 witness (C, D1-ECK62L) but no second 1862 telegram; table-change dates unwitnessed between 21 Mar and 25 May
- 1863-67 sent ledgers at grade H - blocker: not-attempted; Lehigh conflict held M with witnesses (DEF1-ECK62P); received ledgers mssEC 12-13 searched for the 27 Jan and 24 May 1865 copies 6 Oct 2026 (D1-ECK62W: 0 copies, no third witness); next: grep the sent ledgers mssEC 18-19 for every other use of Lehigh and align each against OR by date (a second sent context that reads Hurlbut or Canby), ~$1
- 17 neither-book entries (s2/confpair_pairs.tsv) - blocker: no-key-material; the 13 code words date 30 Dec 1864 - 13 Jul 1865, Cipher No. 3/No. 4 period; the Huntington holds only No. 5 (R8-ECK62); the one known No. 4 copy (Friedman Collection, Marshall Foundation) is Cloudflare-blocked from the cloud (403, 6 Oct 2026); next: the No. 4 copy read from a desk browser (LOCAL-QUEUE row, owner's machine), ~$1
- mssEC 18 entries still '?' - blocker: not-attempted; 100 under the legacy split, 137 '?' entries under split2 print_q; next: the image (marker words the volunteer text may have dropped) for the dated `?p` entries under split2, ~$4

## Escalation (D1-ECK62W, 6 Oct 2026)
- [x] siblings: received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171) and mssEC 04-14 6 Oct 2026 (D1-ECK62L, 0 twins, Nutmeg 1863 witness); mssEC 12-13 for the Lehigh 1865 copies (D1-ECK62W, 0); parallel sent ledger mssEC 18 opened by text 4 Oct 2026 (GAPS206), read with Cipher No. 1 (A3V3-ECK18) and No. 2 (A3V3-ECK2)
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [ ] known-keys: Huntington cipher books searched for No. 3/No. 4: none (No. 5 only, mssEC 49-66), No. 5 values match none of the 14 words (R8-ECK62); next: Cipher No. 4 in the Friedman Collection (Marshall Foundation), from a desk browser, ~$1
- [x] print: wrong-telegram and conflict-pair tests done on legacy (R7B-ECK62, R7C-ECK62C) and split2 (R10-ECK62T: 0 wrong, 5 right, 12 undecided; primary untested at N 60); splitter fixed and adopted (R9-ECK62, R10-ECK62S, R10-ECK62T)
- [x] key-rebuild: Koran/Lamb/Luna/Indus done 3 Oct 2026 (GAPS191); Handle, Harry, author added at C (A3V3-ECKC); possessive and collision guard added to decode.py (RUN3-ECK62)
- [x] image-check: the ten mssEC 15 readings reconciled against the image (reading.md); the six mssEC 18 collision/conflict entries (DEF1-ECK62I) and the Lehigh key row (DEF1-ECK62P)
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 4 internal gaps; cheapest next: every other Lehigh in the sent ledgers mssEC 18-19 aligned to OR (Lehigh second sent context; the mssEC 12-13 received copies gave none, D1-ECK62W), ~$1; the No. 4 book for the 13 words waits on a desk-browser read of the Friedman copy

## D1-ECK62S (6 Oct 2026, account 1 worker for LANE DEFAULT-account-1-20261006-1240): every Lehigh in the sent ledgers mssEC 18-19, aligned to OR

Step check: not run before (D1-ECK62W's Verdict named it). Data re-fetched to scratch, not committed: vol18.json and vol19.json
(sha256 cb162574... and be11447f..., both match pilot1864/manifest.tsv); OR `_djvu.txt` 41.4, 45.2, 48.1, 48.2, 49.1, 49.2 (all six
sha256 match ec18/or_volumes.tsv).
- Method: case-insensitive grep of the volunteer text for lehig/leheigh on every page of both ledgers; each hit's telegram header
  (date, operator, place) read off the page; the OR volume for that date and theatre grepped for the clear words on either side of
  Lehigh (a phrase match, then the printed date and addressee checked against the ledger header). No gate, no score: each row is a
  same-date, same-addressee telegram whose surrounding words match the print, read by eye. Table: `ec18/lehigh_uses.tsv`.
- Found: 13 occurrences (mssEC 18: 7, mssEC 19: 6). 10 aligned to a dated OR telegram (2 already known: 9947.505, 10020.609):
  - 8 print a word in the Lehigh slot, and all 8 read Canby: 6 as the person ("General Canby"/"Canby": 9102 24 Oct 1864 OR 41.4
    p.219; 9880 31 Oct 1864 OR 41.4 p.343; 9937 19 Jan 1865 OR 45.2 p.614; 9947 27 Jan 1865 OR 48.1 p.646; 9171 29 Jan 1865 OR
    49.1 pp.602-606, OCR "General Oaiiby"; 9955 4 Feb 1865 OR 49.1 p.647) and 2 as the sound "can be" (10019, the 23 May 1865
    9.10 a.m. telegram to Thomas, OR 49.2 p.882, "those sent home to be mustered out can be attached"; 10020 24 May 1865 OR 48.2
    p.573). 0 read Hurlbut.
  - 2 matched by date and addressee but the Lehigh slot falls in OCR margin damage (9952 4 Feb 1865 OR 49.1 p.646, "early - has
    many dismounted men"; 9174 1 Feb 1865 to R. Allen, OR 49.1 p.624): no reading either way from the OCR.
  - 3 not aligned (mssEC 19 9272, 9273, 9280; Bates to Stanton, Sept 1865, outside OR ser. I); 9280's "Lehigh Iron" is a clear word
    (the same telegram writes "canby made" in clear for "can be made").
- Grade (rule 4), the 6 new aligned tokens: Canby / "can be" at C from their own print (6), against the key book's H value Hurlbut;
  the 2 OCR-lacuna tokens M; the 3 Sept 1865 tokens not graded. Nothing was changed in key.md, decode.py or the committed readings
  (decode.py --check exit 0); the two tokens held M by DEF1-ECK62P stay M until a verifier decides.
- Does it settle the conflict? It settles what Lehigh meant in use, not why the book differs: witness A (mssEC 41 p.17 l.6, Hurlbut,
  image-checked) stands alone against 8 dated sent uses, 24 Oct 1864 - 24 May 1865, from both sent ledgers and four addressees
  (Rosecrans, Thomas, Dodge, Pope), every one Canby or "can be". Rule 4 forbids settling by count alone; the witness record is: book
  = Hurlbut; operator use Oct 1864 - May 1865 = Canby. Seen in passing, not swept: other words of the same Hurlbut block are used
  the same way in the same telegrams -- Leghorn = "General Canby" (9952 "to leghorn than first ordered", OR "to General Canby than
  first ordered"; 9171 "leghorn is ready", OR "Canby is ready") and "can be" (9937 "leghorns ready in time", OR "can be ready in
  time"; 10019 "Whips leghorn consolidates", OR "Regiments can be consolidated"); Leopard = Canby (9174 "presume leopard has no
  great surplus", OR "I presume Canby has no great [surplus]"). Inference only (grade I, not used): the Hurlbut row's four words
  (Leghorn, Legend, Lehigh, Leopard, key.md) were in practice used for Canby, and then for the sound "can be", by October 1864.
- Requests: hdl.huntington.org 2 (vol18, vol19 dmQuery), archive.org 6 (OR djvu), >= 2 s apart; 0 subagents, 0 vision.
  Report what was found and where it was not found; no novelty class.

## Remaining gaps (finish-or-blocker pass, D1-ECK62S, 6 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82 (GAPS197); received ledgers mssEC 01-14 all searched for residue twins (GAPS171, D1-ECK62L): 0 code-bearing twins; mssEC 18 cascade split2 (ec18/s2/): 729 entries, align_free AGREE 0.427 vs control 0.088; 17 neither-book entries: 0 wrong telegram, 5 right, 12 undecided
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; every OR volume that could hold Feb-Jul 1862 telegrams grepped and aligned (GAPS113-GAPS153), received ledgers mssEC 01-14 searched (GAPS171, D1-ECK62L, 0 twins); next: the image of the residue pages against the volunteer text for the M-graded tokens (transcription slips the decode reads as code), ~$4
- residue code words not fixed by any known plaintext - blocker: open-codes; about 860 oov tokens remain (GAPS197); conflicts Lamb, Luna date-separated, Indus split by slot; Nutmeg = James River gains a 5 Jul 1863 witness (C, D1-ECK62L) but no second 1862 telegram; table-change dates unwitnessed between 21 Mar and 25 May
- 1863-67 sent ledgers at grade H - blocker: not-attempted; Lehigh conflict held M with witnesses (DEF1-ECK62P); received copies in mssEC 12-13: 0 (D1-ECK62W); every Lehigh in mssEC 18-19 aligned 6 Oct 2026 (D1-ECK62S: 13 uses, 8 print-read, all Canby or 'can be', 0 Hurlbut; ec18/lehigh_uses.tsv); next: a verifier's grade decision on the Hurlbut-row words (Lehigh, Leghorn, Legend, Leopard) and the same date-aligned sweep for Leghorn/Legend/Leopard in mssEC 18-19, ~$1
- 17 neither-book entries (s2/confpair_pairs.tsv) - blocker: no-key-material; the 13 code words date 30 Dec 1864 - 13 Jul 1865, Cipher No. 3/No. 4 period; the Huntington holds only No. 5 (R8-ECK62); the one known No. 4 copy (Friedman Collection, Marshall Foundation) is Cloudflare-blocked from the cloud (403, 6 Oct 2026); next: the No. 4 copy read from a desk browser (LOCAL-QUEUE row, owner's machine), ~$1
- mssEC 18 entries still '?' - blocker: not-attempted; 100 under the legacy split, 137 '?' entries under split2 print_q; next: the image (marker words the volunteer text may have dropped) for the dated `?p` entries under split2, ~$4

## Escalation (D1-ECK62S, 6 Oct 2026)
- [x] siblings: received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171) and mssEC 04-14 6 Oct 2026 (D1-ECK62L, 0 twins, Nutmeg 1863 witness); mssEC 12-13 for the Lehigh 1865 copies (D1-ECK62W, 0); every Lehigh in sent ledgers mssEC 18-19 (D1-ECK62S, 8 print-read, all Canby or 'can be'); parallel sent ledger mssEC 18 opened by text 4 Oct 2026 (GAPS206), read with Cipher No. 1 (A3V3-ECK18) and No. 2 (A3V3-ECK2)
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [ ] known-keys: Huntington cipher books searched for No. 3/No. 4: none (No. 5 only, mssEC 49-66), No. 5 values match none of the 14 words (R8-ECK62); next: Cipher No. 4 in the Friedman Collection (Marshall Foundation), from a desk browser, ~$1
- [x] print: wrong-telegram and conflict-pair tests done on legacy (R7B-ECK62, R7C-ECK62C) and split2 (R10-ECK62T: 0 wrong, 5 right, 12 undecided; primary untested at N 60); splitter fixed and adopted (R9-ECK62, R10-ECK62S, R10-ECK62T)
- [x] key-rebuild: Koran/Lamb/Luna/Indus done 3 Oct 2026 (GAPS191); Handle, Harry, author added at C (A3V3-ECKC); possessive and collision guard added to decode.py (RUN3-ECK62)
- [x] image-check: the ten mssEC 15 readings reconciled against the image (reading.md); the six mssEC 18 collision/conflict entries (DEF1-ECK62I) and the Lehigh key row (DEF1-ECK62P)
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 4 internal gaps; cheapest next: the same date-aligned sweep for Leghorn/Legend/Leopard in mssEC 18-19 and a verifier's grade decision on the Hurlbut row (D1-ECK62S: Lehigh reads Canby or 'can be' in all 8 print-read uses), ~$1; the No. 4 book for the 13 words waits on a desk-browser read of the Friedman copy
## R12A-ECKV (6 Oct 2026, verifier, account 1, for LANE LANE-RUN12-account-1): grade decision on the Lehigh tokens

Verifier, not solver. Decision and reasons in AUDIT.md "Carry-over R12A-ECKV"; mechanised in `ec18/lehigh_grades.py` ->
`ec18/lehigh_grades.tsv` (`--check` exit 0). Of the 13 Lehigh uses in ec18/lehigh_uses.tsv: C 8 (each from its own telegram's
OR print: Canby 6, "can be" 2; 5 of the 8 re-read in OR 41.4, 49.1, 49.2 by this session), M 4 (two OCR lacunae, two Sept 1865
uses outside OR; the book's H value Hurlbut does not carry to an unread use once every read use in Oct 1864 - May 1865
contradicts it), clear 1 (9280 "Lehigh Iron"). The two committed tokens move from held M to C: 9947.505 Lehigh = Canby,
10020.609 lehigh = can be. The committed ec18.py outputs (readings.md, s2/readings.md, align_tokens.tsv) were not regenerated
(full OR set + cascade, outside the box): their Hurlbut brackets for those two tokens are superseded by lehigh_grades.tsv.
key.md's row stays H (what the book says). Leghorn/Legend/Leopard not graded (R12A-ECKLEG's sweep first).
Requests: archive.org 3, 2 s apart; 0 subagents. decode.py --check exit 0.

## R12A-ECKLEG (6 Oct 2026, account 1 worker for LANE LANE-RUN12-account-1): Leghorn, Legend, Leopard in the sent ledgers mssEC 18-19, aligned to OR

Step check: not run before (R12A-ECKV's Verdict named it). Data re-fetched to scratch, not committed: vol18.json, vol19.json (sha256 match
pilot1864/manifest.tsv); all 48 OR `_djvu.txt` files of ec18/or_volumes.tsv (32.1-49.2; every sha256 matches).
- Method: `ec18/hurlbut_row_sweep.py DATA_DIR OR_DIR leghorn legend leopard lehigh` lists every occurrence (with -s/-'s) in the volunteer
  text, the nearest date line above it on the page, and the OR place where the most 3-word clear-context shingles cluster. It decides
  nothing: every row was then read by eye against the OR text, and where the script's best hit was the wrong telegram a phrase search
  on the clear words found the right one (or did not; then "not aligned"). Check of the script on the Lehigh rows D1-ECK62S aligned by
  hand: right volume and telegram for 6 of 10, so its hit alone is never taken. No gate, no score, no grade change (brief).
- Tables: `ec18/leghorn_uses.tsv` (17), `ec18/legend_uses.tsv` (32), `ec18/leopard_uses.tsv` (11).
- Leghorn, 17 uses (6 Jun 1864 - 28 May 1865): Canby 10 (incl. the address line of 30 Jul 1864 "Maj.-Gen. Canby, Natchez", OR 41.2);
  "can be" 2 (9937 19 Jan 1865 OR 45.2 p.614; 10019 OR 49.2 p.882); "circumstances" 3 (9934 10 Jan 1865 OR 45.2 p.559 "according to
  circumstances"; 9144, 9145 29 Dec 1864 OR 42.3 p.1091 "Under [all] these circumstances"); not aligned 2 (9877 27 Oct 1864; 9945 25 Jan
  1865). 0 Hurlbut.
- Leopard, 11 uses (19 Aug 1864 - 19 Mar 1865): Canby 10 (one, 9057 26 Aug 1864, is an operator's insertion above "Gen Canby" written in
  clear: a gloss, not a code-only use); OCR lacuna 1 (9174 first occurrence, OR 49.1 p.624). 0 Hurlbut.
- Legend, 32 uses (3 Feb 1864 - 28 May 1865): Butler 13 (11 Feb - 10 Nov 1864: OR 33, 34.4, 36.2, 36.3, 37.2, 42.3), Canby 10 (27 May
  1864 - 19 May 1865: OR 34.4, 39.2, 41.4, 45.2, 48.2, 49.1, 49.2), not aligned 9. 0 Hurlbut. The Butler and Canby date ranges overlap
  (27 May - 10 Nov 1864): two values in the same months, the shape of key.md's wedding/Stanhope conflicts; logged, not resolved here.
  (key.md's 1862 row Legend = Kentucky is a different book and period.)
- Reading: every print-read use of the four Hurlbut-row words in 1864-65 (Lehigh 8, Leghorn 15, Leopard 10, Legend 23) reads Canby,
  "can be", "circumstances" or (Legend only) Butler; none reads Hurlbut. Inference only (grade I, not used): the book's Hurlbut row was
  not what operators used these words for in 1864-65; Legend = Butler may be a different book's value (Butler's own theatre).
- Grades: none changed by this worker (brief). Flagged in ROOM for a verifier: the C candidates are the 48 aligned rows, each from its own
  telegram's print; decode.py --check exit 0 (no reading changed).
- Requests: hdl.huntington.org 2, archive.org 51 (48 OR djvu, 3 retried once after a connection reset), >= 1.6 s apart; 0 subagents, 0 vision.
  Report what was found and where it was not found; no novelty class.

## R12A-ECKV2 (6 Oct 2026, verifier, account 1, for LANE LANE-RUN12-account-1): grade decision on Leghorn, Legend, Leopard

Verifier, not solver. Decision and reasons in AUDIT.md "Carry-over R12A-ECKV2"; mechanised in `ec18/hurlbut_row_grades.py` ->
`ec18/hurlbut_row_grades.tsv` (`--check` exit 0; it also fails if any of the three words enters a committed reading). Of 60 uses:
Leghorn 17 = C 15 (Canby 10, "can be" 2, "circumstances" 3), M 2; Legend 32 = C 23 (Butler 13, Canby 10), M 9; Leopard 11 = C 9
(Canby), gloss 1 (9057, clear "Gen Canby" with "leopard" inserted), M 1 (9174 first occurrence, OCR lacuna). Legend's two values
are a rule-4 data conflict: witnesses in HYPOTHESES.md, not settled by count. None of the four Hurlbut-row words is a token of
ec18/readings.md, s2/readings.md or either align_tokens.tsv, so no committed reading changes; key.md rows stay H (the book).
16 of the 48 C slots re-read independently in OR 33, 42.3, 45.2 (sha256 match). status.json: no field carries these grades; unchanged.
Requests: archive.org 3, 2 s apart; 0 subagents. decode.py --check exit 0.

## Remaining gaps (finish-or-blocker pass, R12A-ECKLEG, 6 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82 (GAPS197); received ledgers mssEC 01-14 all searched for residue twins (GAPS171, D1-ECK62L): 0 code-bearing twins; mssEC 18 cascade split2 (ec18/s2/): 729 entries, align_free AGREE 0.427 vs control 0.088; 17 neither-book entries: 0 wrong telegram, 5 right, 12 undecided
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; every OR volume that could hold Feb-Jul 1862 telegrams grepped and aligned (GAPS113-GAPS153), received ledgers mssEC 01-14 searched (GAPS171, D1-ECK62L, 0 twins); next: the image of the residue pages against the volunteer text for the M-graded tokens (transcription slips the decode reads as code), ~$4
- residue code words not fixed by any known plaintext - blocker: open-codes; about 860 oov tokens remain (GAPS197); conflicts Lamb, Luna date-separated, Indus split by slot; Nutmeg = James River gains a 5 Jul 1863 witness (C, D1-ECK62L) but no second 1862 telegram; table-change dates unwitnessed between 21 Mar and 25 May
- 1863-67 sent ledgers at grade H - blocker: not-attempted; Lehigh conflict held M with witnesses (DEF1-ECK62P); received copies in mssEC 12-13: 0 (D1-ECK62W); every Lehigh in mssEC 18-19 aligned 6 Oct 2026 (D1-ECK62S: 13 uses, 8 print-read, all Canby or 'can be', 0 Hurlbut; ec18/lehigh_uses.tsv); Lehigh graded by a verifier (R12A-ECKV, AUDIT.md 'Carry-over R12A-ECKV', ec18/lehigh_grades.tsv: C 8, M 4, clear 1; 9947.505 = Canby C, 10020.609 = can be C, superseding the committed readings' Hurlbut brackets until ec18.py's next full regeneration); Leghorn/Legend/Leopard swept 6 Oct 2026 (R12A-ECKLEG: 48 print-read, 0 Hurlbut) and graded by a verifier (R12A-ECKV2, AUDIT.md 'Carry-over R12A-ECKV2', ec18/hurlbut_row_grades.tsv: C 47, gloss 1, M 12; Legend's Butler/Canby conflict logged with witnesses in HYPOTHESES.md, unresolved); none of the four words is in a committed reading; next: fold lehigh_grades.tsv and hurlbut_row_grades.tsv into ec18.py as a per-token override table at the next full regeneration, ~$3
- 17 neither-book entries (s2/confpair_pairs.tsv) - blocker: no-key-material; the 13 code words date 30 Dec 1864 - 13 Jul 1865, Cipher No. 3/No. 4 period; the Huntington holds only No. 5 (R8-ECK62); the one known No. 4 copy (Friedman Collection, Marshall Foundation) is Cloudflare-blocked from the cloud (403, 6 Oct 2026); next: the No. 4 copy read from a desk browser (LOCAL-QUEUE row, owner's machine), ~$1
- mssEC 18 entries still '?' - blocker: not-attempted; 100 under the legacy split, 137 '?' entries under split2 print_q; next: the image (marker words the volunteer text may have dropped) for the dated `?p` entries under split2, ~$4

## Escalation (R12A-ECKLEG, 6 Oct 2026)
- [x] siblings: received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171) and mssEC 04-14 6 Oct 2026 (D1-ECK62L, 0 twins, Nutmeg 1863 witness); mssEC 12-13 for the Lehigh 1865 copies (D1-ECK62W, 0); every Lehigh in sent ledgers mssEC 18-19 (D1-ECK62S, 8 print-read, all Canby or 'can be'); every Leghorn/Legend/Leopard in mssEC 18-19 (R12A-ECKLEG, 48 print-read, 0 Hurlbut); parallel sent ledger mssEC 18 opened by text 4 Oct 2026 (GAPS206), read with Cipher No. 1 (A3V3-ECK18) and No. 2 (A3V3-ECK2)
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [ ] known-keys: Huntington cipher books searched for No. 3/No. 4: none (No. 5 only, mssEC 49-66), No. 5 values match none of the 14 words (R8-ECK62); next: Cipher No. 4 in the Friedman Collection (Marshall Foundation), from a desk browser, ~$1
- [x] print: wrong-telegram and conflict-pair tests done on legacy (R7B-ECK62, R7C-ECK62C) and split2 (R10-ECK62T: 0 wrong, 5 right, 12 undecided; primary untested at N 60); splitter fixed and adopted (R9-ECK62, R10-ECK62S, R10-ECK62T)
- [x] key-rebuild: Koran/Lamb/Luna/Indus done 3 Oct 2026 (GAPS191); Handle, Harry, author added at C (A3V3-ECKC); possessive and collision guard added to decode.py (RUN3-ECK62)
- [x] image-check: the ten mssEC 15 readings reconciled against the image (reading.md); the six mssEC 18 collision/conflict entries (DEF1-ECK62I) and the Lehigh key row (DEF1-ECK62P)
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 4 internal gaps; Hurlbut-row words graded (R12A-ECKV2); cheapest next: the per-token override table in ec18.py at its next full regeneration (Lehigh + Leghorn/Legend/Leopard grades), ~$3; the No. 4 book for the 13 words waits on a desk-browser read of the Friedman copy

## D07-ECK62 (7 Oct 2026, account 1 worker for LANE DEFAULT-account-1-20261007-0042): per-token override table in ec18.py, full regeneration

Step check: named by R12A-ECKV2's Verdict, not run before. Data re-fetched to scratch, not committed: vol18.json (sha256 cb162574...,
matches pilot1864/manifest.tsv), DIR62 8 `_djvu.txt`, OR 32.1-49.2 48 `_djvu.txt` (all 48 sha256 match or_volumes.tsv).
- Code (`ec18/ec18.py`, `overrides()` / `apply_overrides()`): the verifiers' tables `ec18/lehigh_grades.tsv` (R12A-ECKV) and
  `ec18/hurlbut_row_grades.tsv` (R12A-ECKV2) are read as a per-token override table for the Cipher No. 1 main run (legacy and
  `--split2`): decided C -> the print meaning at C, M -> `[?]` at M, clear/gloss -> left as written. Placement: the entry with the
  row's date and the code word (or its plural/possessive) whose opening page is at most two pointers before the row's page; among
  several the nearest; with none, the one entry opening on the row's page (the sweep's date line and the splitter's heading
  disagree for 10019 lehigh: sweep 23 May, ledger heading 24 May). All 34 mssEC 18 rows placed on exactly one entry, 0 conflicts,
  0 unplaced (mssEC 19 rows do not apply: ec18.py reads mssEC 18 only). Listed per token in `ec18/overrides.tsv` and `ec18/s2/overrides.tsv`.
- Display only: every 5-gram, OR match, permutation control, book decision and meaning-in-print agreement is still computed from
  the book-value decode, because the overrides come from the same print and would make the matcher circular. Proof: `matches.tsv`,
  `guard.tsv` and every statistic in `control.tsv` except the grade line are byte-identical after the regeneration; the run exits if
  an override makes the collision guard decide differently (it did not).
- Grades moved (rule 4), entries.tsv over all 671 legacy entries: H 12699 -> 12665, C 37 -> 64, M 0 -> 7 (34 tokens: 27 H->C, 7 H->M);
  split2 (729 entries) the same 34 tokens: H 12676 -> 12642, C 37 -> 64, M 0 -> 7. Counted readings (the 28 fully keyed No. 1 entries,
  readings.md and s2/readings.md): 2 tokens, H 369 C 2 -> H 367 C 4 -- 9947.505 Lehigh [Maj Gen S. A. Hurlbut] H -> [Canby] C and
  10020.609 lehigh [Maj Gen S. A. Hurlbut] H -> [can be] C, the two R12A-ECKV had already superseded on paper; the other 32 tokens sit
  in entries that are not fully keyed (no committed reading text). No book, match or fully-keyed status changed.
- Not changed: `align_tokens.tsv` (both cascades) keeps the key value and its CONFLICT status for the two tokens -- it is the evidence
  the grade rests on, not a reading; key.md rows stay H (what the book says); Cipher No. 2 (`--book 2`) runs untouched.
- Rule 7: `ec18.py ... --possessive --guard DIR62 --check` current (legacy and --split2), `--book 2` current both ways, `ec18_align.py
  --check` exit 0 both ways, `--read-free --check` exit 0 both ways, `--split-report --check` exit 0, `decode.py --check` exit 0.
- The counted reading changed after AUDIT.md: flagged in ROOM for a verifier (AUDIT.md "Carry-over R12A-ECKV" already decided these two
  grades; the regeneration only carries them).
- Requests: hdl.huntington.org 2 (vol18.json; the first attempt wrote nothing, re-fetched once), archive.org 56 (8 DIR62 + 48 OR), >= 1.6 s
  apart; 0 subagents, 0 vision. Report what was found and where it was not found; no novelty class.

## Remaining gaps (finish-or-blocker pass, D07-ECK62, 7 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82 (GAPS197); received ledgers mssEC 01-14 all searched for residue twins (GAPS171, D1-ECK62L): 0 code-bearing twins; mssEC 18 cascade split2 (ec18/s2/): 729 entries, align_free AGREE 0.427 vs control 0.088; 17 neither-book entries: 0 wrong telegram, 5 right, 12 undecided
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; every OR volume that could hold Feb-Jul 1862 telegrams grepped and aligned (GAPS113-GAPS153), received ledgers mssEC 01-14 searched (GAPS171, D1-ECK62L, 0 twins); next: the image of the residue pages against the volunteer text for the M-graded tokens (transcription slips the decode reads as code), ~$4
- residue code words not fixed by any known plaintext - blocker: open-codes; about 860 oov tokens remain (GAPS197); conflicts Lamb, Luna date-separated, Indus split by slot; Nutmeg = James River gains a 5 Jul 1863 witness (C, D1-ECK62L) but no second 1862 telegram; table-change dates unwitnessed between 21 Mar and 25 May
- 1863-67 sent ledgers at grade H - blocker: not-attempted; Lehigh conflict held M with witnesses (DEF1-ECK62P); received copies in mssEC 12-13: 0 (D1-ECK62W); every Lehigh in mssEC 18-19 aligned 6 Oct 2026 (D1-ECK62S: 13 uses, 8 print-read, all Canby or 'can be', 0 Hurlbut; ec18/lehigh_uses.tsv); Lehigh graded by a verifier (R12A-ECKV, AUDIT.md 'Carry-over R12A-ECKV', ec18/lehigh_grades.tsv: C 8, M 4, clear 1; 9947.505 = Canby C, 10020.609 = can be C, superseding the committed readings' Hurlbut brackets until ec18.py's next full regeneration); Leghorn/Legend/Leopard swept 6 Oct 2026 (R12A-ECKLEG: 48 print-read, 0 Hurlbut) and graded by a verifier (R12A-ECKV2, AUDIT.md 'Carry-over R12A-ECKV2', ec18/hurlbut_row_grades.tsv: C 47, gloss 1, M 12; Legend's Butler/Canby conflict logged with witnesses in HYPOTHESES.md, unresolved); folded into ec18.py as a per-token override table 7 Oct 2026 (D07-ECK62: 34 mssEC 18 tokens, 27 H->C, 7 H->M; counted readings 9947.505 and 10020.609 H->C; ec18/overrides.tsv); next: the 7 M-graded Hurlbut-row tokens (OCR lacunae, telegrams with no aligned print) against another witness, ~$4
- 17 neither-book entries (s2/confpair_pairs.tsv) - blocker: no-key-material; the 13 code words date 30 Dec 1864 - 13 Jul 1865, Cipher No. 3/No. 4 period; the Huntington holds only No. 5 (R8-ECK62); the one known No. 4 copy (Friedman Collection, Marshall Foundation) is Cloudflare-blocked from the cloud (403, 6 Oct 2026); next: the No. 4 copy read from a desk browser (LOCAL-QUEUE row, owner's machine), ~$1
- mssEC 18 entries still '?' - blocker: not-attempted; 100 under the legacy split, 137 '?' entries under split2 print_q; next: the image (marker words the volunteer text may have dropped) for the dated `?p` entries under split2, ~$4

## Escalation (D07-ECK62, 7 Oct 2026)
- [x] siblings: received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171) and mssEC 04-14 6 Oct 2026 (D1-ECK62L, 0 twins, Nutmeg 1863 witness); mssEC 12-13 for the Lehigh 1865 copies (D1-ECK62W, 0); every Lehigh in sent ledgers mssEC 18-19 (D1-ECK62S, 8 print-read, all Canby or 'can be'); every Leghorn/Legend/Leopard in mssEC 18-19 (R12A-ECKLEG, 48 print-read, 0 Hurlbut); parallel sent ledger mssEC 18 opened by text 4 Oct 2026 (GAPS206), read with Cipher No. 1 (A3V3-ECK18) and No. 2 (A3V3-ECK2)
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [ ] known-keys: Huntington cipher books searched for No. 3/No. 4: none (No. 5 only, mssEC 49-66), No. 5 values match none of the 14 words (R8-ECK62); next: Cipher No. 4 in the Friedman Collection (Marshall Foundation), from a desk browser, ~$1
- [x] print: wrong-telegram and conflict-pair tests done on legacy (R7B-ECK62, R7C-ECK62C) and split2 (R10-ECK62T: 0 wrong, 5 right, 12 undecided; primary untested at N 60); splitter fixed and adopted (R9-ECK62, R10-ECK62S, R10-ECK62T)
- [x] key-rebuild: Koran/Lamb/Luna/Indus done 3 Oct 2026 (GAPS191); Handle, Harry, author added at C (A3V3-ECKC); possessive and collision guard added to decode.py (RUN3-ECK62)
- [x] image-check: the ten mssEC 15 readings reconciled against the image (reading.md); the six mssEC 18 collision/conflict entries (DEF1-ECK62I) and the Lehigh key row (DEF1-ECK62P)
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 4 internal gaps; Hurlbut-row grades carried into ec18.py's outputs (D07-ECK62, overrides.tsv); cheapest next: the dated `?p` mssEC 18 entries under split2 against the image for marker words, ~$4; the No. 4 book for the 13 words waits on a desk-browser read of the Friedman copy

## D07-ECKV (7 Oct 2026, verifier, account 1, for LANE DEFAULT-account-1-20261007-0042): D07-ECK62 regrade verified
The D07-ECK62 override table and regeneration verified and endorsed in AUDIT.md "Carry-over D07-ECKV": 34 tokens (27 H->C, 7 H->M)
match the R12A-ECKV/ECKV2 tables exactly, every C cites its own telegram's print (6 of 6 spot-checked in OR), counts agree
(counted readings H 369 C 2 -> H 367 C 4), all regeneration --check runs exit 0 on re-fetched data. No N-class or depth change;
status.json, PROGRESS.tsv and SO-ECK-4992 carry no affected token. Remaining gaps / Escalation / Verdict above stand unchanged.

## AM-ECK62Q (7 Oct 2026, account 2 worker for LANE LANE-AM-0914): the dated `?p` mssEC 18 entries under split2 against the image

Step check: named by D07-ECK62's Verdict, not run before (no dated section, no ROOM done line). PREREG `ec18/s2/PREREG-ECK62-QP.md`
pushed 574f2cdf6 before any image was fetched. vol18.json re-fetched to scratch (sha256 cb162574..., matches pilot1864/manifest.tsv);
the 25 `?p` entries and their page pointers from `ec18.entries(split2=True)` and `s2/print_q.tsv`.
- Images: 25 Huntington IIIF pages (`hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2000,/0/default.jpg`), scratch only,
  not committed. Crop step: `python3 tools/iiif_lines.py --image img/p<ptr>.jpg --out crops/p<ptr> --prefix p<ptr> --lines-per-crop 9
  --overlap 40 --max-width 2000 --distance 45 --prominence 20` (defaults found 0 lines on these pages); per-entry crops cut from the
  tool's line centres (`--dry-run`) by the entry's line span in the volunteer text, three re-cuts where the span missed (9868.326 body,
  9923.449, 9735.98 tail) and one page-tail strip for five entries. One eye (this worker), no subagent.
- Control (PREREG item 3, chosen before any image): 8 marker-known entries on the same pages, 4 per book. Recall 25/25 marker tokens
  found legibly on the image (gate >= 0.80), cross-set false markers 0 (gate 0): PASS. Not blind (disclosed in the PREREG).
- Target: 0 of 25 `?p` entries show a marker word or book annotation the volunteer text lacks. No entry moved; no grade, reading or
  key row changed. This is a search result: at this resolution the volunteer text dropped no marker on these 25 entries.
  Not looked at: the continuation of 9668.3 on p.9669 and of 9706.69g on p.9707.
- Why the print could not decide them: 9818.220 (Halleck), 9844.271 (Stanton), 9870.332 (Lincoln) are written wholly in clear and
  9981.558 closes "E M Stanton" in clear; the rest use route words and code names that both books share, with "period" and "sig" written
  out, so neither the marker rule nor the 5-gram margin can tell the books apart.
- Header numbers (text-side tabulation over all 729 split2 entries, descriptive, not a gate): early-1864 headers "Beckwith 1",
  "Caldwell 2" agree with the marker book, but from spring 1864 "No 1" ... "No 7" are daily serials ("No 2" heads 6 book-1 entries;
  "No 3"-"No 7" have no book of that number; "9" heads Sheldon/Horner/Rowe entries of both kinds). Not usable as a book marker.
- Seen on the image and absent from the volunteer text (not markers, recorded for a later worker): 9676.23 margin "Copy to Genl Grant";
  9706.69g small interlinear words over code words (Engage, hope, horse, saved, not, burned) and route digits.
- Rule 7: `decode.py --check` exit 0; ec18 outputs untouched (nothing regenerated). Requests: hdl.huntington.org 26 (1 dmQuery + 25
  IIIF pages), >= 1.6 s apart, no errors. Report what was found and where it was not found; no novelty class.

## Remaining gaps (finish-or-blocker pass, AM-ECK62Q, 7 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82 (GAPS197); received ledgers mssEC 01-14 all searched for residue twins (GAPS171, D1-ECK62L): 0 code-bearing twins; mssEC 18 cascade split2 (ec18/s2/): 729 entries, align_free AGREE 0.427 vs control 0.088; 17 neither-book entries: 0 wrong telegram, 5 right, 12 undecided
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; every OR volume that could hold Feb-Jul 1862 telegrams grepped and aligned (GAPS113-GAPS153), received ledgers mssEC 01-14 searched (GAPS171, D1-ECK62L, 0 twins); next: the image of the residue pages against the volunteer text for the M-graded tokens (transcription slips the decode reads as code), ~$4
- residue code words not fixed by any known plaintext - blocker: open-codes; about 860 oov tokens remain (GAPS197); conflicts Lamb, Luna date-separated, Indus split by slot; Nutmeg = James River gains a 5 Jul 1863 witness (C, D1-ECK62L) but no second 1862 telegram; table-change dates unwitnessed between 21 Mar and 25 May
- 1863-67 sent ledgers at grade H - blocker: not-attempted; Lehigh conflict held M with witnesses (DEF1-ECK62P); received copies in mssEC 12-13: 0 (D1-ECK62W); every Lehigh in mssEC 18-19 aligned 6 Oct 2026 (D1-ECK62S: 13 uses, 8 print-read, all Canby or 'can be', 0 Hurlbut; ec18/lehigh_uses.tsv); Lehigh graded by a verifier (R12A-ECKV, AUDIT.md 'Carry-over R12A-ECKV', ec18/lehigh_grades.tsv: C 8, M 4, clear 1; 9947.505 = Canby C, 10020.609 = can be C, superseding the committed readings' Hurlbut brackets until ec18.py's next full regeneration); Leghorn/Legend/Leopard swept 6 Oct 2026 (R12A-ECKLEG: 48 print-read, 0 Hurlbut) and graded by a verifier (R12A-ECKV2, AUDIT.md 'Carry-over R12A-ECKV2', ec18/hurlbut_row_grades.tsv: C 47, gloss 1, M 12; Legend's Butler/Canby conflict logged with witnesses in HYPOTHESES.md, unresolved); folded into ec18.py as a per-token override table 7 Oct 2026 (D07-ECK62: 34 mssEC 18 tokens, 27 H->C, 7 H->M; counted readings 9947.505 and 10020.609 H->C; ec18/overrides.tsv); next: the 7 M-graded Hurlbut-row tokens (OCR lacunae, telegrams with no aligned print) against another witness, ~$4
- 17 neither-book entries (s2/confpair_pairs.tsv) - blocker: no-key-material; the 13 code words date 30 Dec 1864 - 13 Jul 1865, Cipher No. 3/No. 4 period; the Huntington holds only No. 5 (R8-ECK62); the one known No. 4 copy (Friedman Collection, Marshall Foundation) is Cloudflare-blocked from the cloud (403, 6 Oct 2026); next: the No. 4 copy read from a desk browser (LOCAL-QUEUE row, owner's machine), ~$1
- mssEC 18 entries still '?' - blocker: not-attempted; 100 under the legacy split, 137 '?' entries under split2 print_q; the 25 dated `?p` entries checked against the image for dropped marker words 7 Oct 2026 (AM-ECK62Q, PREREG-ECK62-QP: 0 of 25 carry a marker, control 25/25 marker tokens found, 0 cross-set; 0 moved; 4 are written in clear, no book applies; ec18/s2/image_qp.tsv); header 'No N' numbers are serials after spring 1864, not book markers (No 2 on 6 book-1 entries; No 3-7 exist); next: the 112 undated-match '?' entries by a different instrument (bigram support under both keys already tried, RUN6-ECK62), or leave '?' as the residue no print or image decides, ~$3

## Escalation (AM-ECK62Q, 7 Oct 2026)
- [x] siblings: received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171) and mssEC 04-14 6 Oct 2026 (D1-ECK62L, 0 twins, Nutmeg 1863 witness); mssEC 12-13 for the Lehigh 1865 copies (D1-ECK62W, 0); every Lehigh in sent ledgers mssEC 18-19 (D1-ECK62S, 8 print-read, all Canby or 'can be'); every Leghorn/Legend/Leopard in mssEC 18-19 (R12A-ECKLEG, 48 print-read, 0 Hurlbut); parallel sent ledger mssEC 18 opened by text 4 Oct 2026 (GAPS206), read with Cipher No. 1 (A3V3-ECK18) and No. 2 (A3V3-ECK2)
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [ ] known-keys: Huntington cipher books searched for No. 3/No. 4: none (No. 5 only, mssEC 49-66), No. 5 values match none of the 14 words (R8-ECK62); next: Cipher No. 4 in the Friedman Collection (Marshall Foundation), from a desk browser, ~$1
- [x] print: wrong-telegram and conflict-pair tests done on legacy (R7B-ECK62, R7C-ECK62C) and split2 (R10-ECK62T: 0 wrong, 5 right, 12 undecided; primary untested at N 60); splitter fixed and adopted (R9-ECK62, R10-ECK62S, R10-ECK62T)
- [x] key-rebuild: Koran/Lamb/Luna/Indus done 3 Oct 2026 (GAPS191); Handle, Harry, author added at C (A3V3-ECKC); possessive and collision guard added to decode.py (RUN3-ECK62)
- [x] image-check: the ten mssEC 15 readings reconciled against the image (reading.md); the six mssEC 18 collision/conflict entries (DEF1-ECK62I) and the Lehigh key row (DEF1-ECK62P)
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 4 internal gaps; the `?p` image check ran (AM-ECK62Q: 0 markers dropped, 0 moved); cheapest next: the 7 M-graded Hurlbut-row tokens against another witness, ~$4; the No. 4 book for the 13 words waits on a desk-browser read of the Friedman copy

## D12-E62H (7 Oct 2026, account 2 worker for LANE DEFAULT-account-2-20261007-1210): the 7 M-graded Hurlbut-row tokens against another witness

Step check: named by AM-ECK62Q's Verdict, not run before. Intake gate: `eckert-1862: partial (line 3) -- edition/page or
full-text-search citation found within 6 lines`. Data re-fetched to scratch, not committed: vol18.json (sha256 cb162574...,
matches pilot1864/manifest.tsv); OR 32.1-49.2 48 `_djvu.txt` (all 48 sha256 match or_volumes.tsv); DIR62 8 `_djvu.txt`.
- The seven (ec18/overrides.tsv, D07-ECK62): 9671.9 legend, 9672.12 legend, 9785.169 legend, 9877.348 leghorn, 9945.500 leghorn,
  9945.500 legend, 9952.516 lehigh. Witness sought for each: the print of the same telegram in a second scan or edition.
- 9671 (3 Feb 1864 4.30 PM, Caldwell 2, "For Nestor Please Pine directly with Legend Bunyan in regard to his proposed suppers"):
  OR 33 p.502, Halleck to Sedgwick, "communicate directly with General B. F. Butler, Fort Monroe, in regard to his proposed
  movements". Legend = (General B. F.) Butler, C. The R12A-ECKLEG script had pointed to a different telegram (32.2 p.106).
- 9672 (5 Feb 1864 11.30 AM, "Legend again asks for a demon = stra = tion by your Peru"): OR 33 p.514, Halleck to Sedgwick,
  "General Butler again asks for a demonstration by your army". Butler, C (R12A-ECKLEG's script hit 33 p.513 was this telegram,
  not checked by eye then).
- 9786 (= entry 9785.169, 11 Jul 1864, Beckwith, "For Palermo Raw line", "If the Shark could spare Legend for the supreme
  Princeton all danger would certainly cease"): not in OR 37.2 or 40.3 (both IA scans grepped). Printed as deciphered in The
  Papers of Ulysses S. Grant vol. 11 (ed. J. Y. Simon, SIU Press), Dana to Grant's headquarters, "If the General could spare
  Butler for the Chief Supreme Command all danger danger would certainly cease - Especially as Hunter is at hand"; read as a
  Google Books API snippet (volume r0d5C4hAav8C, PARTIAL view), page number not read. Butler, C (print of this telegram, outside OR).
- 9945 (25 Jan 1865 6 PM, "more panama spaffords wilby sent to you peru Legend Leghorn supplied"): absent from the OCR of
  warofrebellion491unit (why R12A-ECKLEG's phrase search missed it); the second IA scan warofrebellion014901rootrich prints it,
  OR 49.1 p.580, Halleck to Thomas, Eastport, "More cavalry horses will be sent to you as soon as General Canby can be
  supplied". Legend = Canby C, Leghorn = "can be" C.
- 9952 (4 Feb 1865, "Waldo ---- Lehigh has many dis mounted spit"): the slot lost in warofrebellion491unit's margin reads in
  warofrebellion014901rootrich, OR 49.1 p.646: "say 4,000 or 5,000. Canby has many dismounted men". Lehigh = Canby, C.
- 9877 (27 Oct 1864, Sampson, Baltimore, furloughs to vote, "provided the same leghorn done without prejudice to the public
  service"): not found in OR 43.2 (warofrebellion432unit and warofrebellion014302rootrich; the nearest is Middle Department
  General Orders No. 107 on furloughs to vote, a different document), nor by two Google Books API phrase queries. Stays M (the
  sense "can be" is grade I, not used).
- Beyond the seven, same scan, same rule (mssEC 19, not in ec18's outputs): 9174 lehigh and the first 9174 leopard (1 Feb 1865,
  Halleck to Egbert Allen, Louisville, OR 49.1 p.624) read "General Canby" in warofrebellion014901rootrich: C.
- Changes: witnesses written into ec18/{legend,leghorn,lehigh,leopard}_uses.tsv (status "aligned (D12-E62H ...)"); the grade
  scripts unchanged in rule, with a non-OR source label ("PUSG 11") and the print-read counts in their M reasons updated;
  hurlbut_row_grades.tsv now leghorn C 16 M 1, legend C 27 (Butler 16, Canby 11) M 5, leopard C 10 gloss 1; lehigh_grades.tsv
  C 10 M 2 clear 1. ec18.py `--write` legacy and `--split2`: overrides.tsv 6 rows M -> C (33 C, 1 M); entries.tsv H 12665,
  C 64 -> 70, M 7 -> 1 (s2: H 12642, C 70, M 1). Counted readings unchanged (H 367 C 4): none of the seven sits in a fully keyed entry.
- Legend conflict (HYPOTHESES.md, appended): Butler 13 -> 16, Canby 10 -> 11, unread 9 -> 5; not resolved.
- Rule 7: ec18.py --possessive --guard DIR62 --check exit 0 legacy and --split2 (and exit 0 on the committed state before the
  change); hurlbut_row_grades.py and lehigh_grades.py --check current; --split-report --check exit 0; decode.py --check exit 0.
  Stale before this job and left untouched (flagged in ROOM): `--book 2 --check` (key-no2.md changed 11:54 UTC today by
  ECK64-NO2: readings_b2 I 8 -> 12), and `ec18_align.py --check` (stale with this job's changes stashed too).
- Requests: archive.org 70 (48 OR + 8 DIR62 + 3 error pages for wrong DIR62 ids + 9 extra scans/volumes + 2 be-api fts),
  hdl.huntington.org 1, googleapis.com 8; >= 1.5 s apart except the DIR62 re-fetch, which overlapped the OR fetch (two streams
  to archive.org for about one minute). 0 subagents, 0 vision. Report what was found and where it was not found; no novelty class.

## Remaining gaps (finish-or-blocker pass, D12-E62H, 7 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82 (GAPS197); received ledgers mssEC 01-14 all searched for residue twins (GAPS171, D1-ECK62L): 0 code-bearing twins; mssEC 18 cascade split2 (ec18/s2/): 729 entries, align_free AGREE 0.427 vs control 0.088; 17 neither-book entries: 0 wrong telegram, 5 right, 12 undecided
- residue entries of mssEC 15 (about 290) - blocker: not-attempted; every OR volume that could hold Feb-Jul 1862 telegrams grepped and aligned (GAPS113-GAPS153), received ledgers mssEC 01-14 searched (GAPS171, D1-ECK62L, 0 twins); next: the image of the residue pages against the volunteer text for the M-graded tokens (transcription slips the decode reads as code), ~$4
- residue code words not fixed by any known plaintext - blocker: open-codes; about 860 oov tokens remain (GAPS197); conflicts Lamb, Luna date-separated, Indus split by slot; Nutmeg = James River gains a 5 Jul 1863 witness (C, D1-ECK62L) but no second 1862 telegram; table-change dates unwitnessed between 21 Mar and 25 May
- 1863-67 sent ledgers at grade H - blocker: not-attempted; Lehigh conflict held M with witnesses (DEF1-ECK62P); received copies in mssEC 12-13: 0 (D1-ECK62W); every Lehigh in mssEC 18-19 aligned 6 Oct 2026 (D1-ECK62S: 13 uses, 8 print-read, all Canby or 'can be', 0 Hurlbut; ec18/lehigh_uses.tsv); Lehigh graded by a verifier (R12A-ECKV, AUDIT.md 'Carry-over R12A-ECKV', ec18/lehigh_grades.tsv: C 8, M 4, clear 1; 9947.505 = Canby C, 10020.609 = can be C, superseding the committed readings' Hurlbut brackets until ec18.py's next full regeneration); Leghorn/Legend/Leopard swept 6 Oct 2026 (R12A-ECKLEG: 48 print-read, 0 Hurlbut) and graded by a verifier (R12A-ECKV2, AUDIT.md 'Carry-over R12A-ECKV2', ec18/hurlbut_row_grades.tsv: C 47, gloss 1, M 12; Legend's Butler/Canby conflict logged with witnesses in HYPOTHESES.md, unresolved); folded into ec18.py as a per-token override table 7 Oct 2026 (D07-ECK62: 34 mssEC 18 tokens, 27 H->C, 7 H->M; counted readings 9947.505 and 10020.609 H->C; ec18/overrides.tsv); the 7 M-graded mssEC 18 tokens checked against a second witness 7 Oct 2026 (D12-E62H: 6 to C from the print of their own telegram -- OR 33 pp.502/514, OR 49.1 pp.580/646 in the second IA scan warofrebellion014901rootrich, and Papers of U. S. Grant vol. 11 for 9786 -- 1 left M, 9877.348 leghorn 27 Oct 1864 to Baltimore, not in OR 43.2 either scan; mssEC 19 9174 lehigh and leopard also to C from OR 49.1 p.624; overrides.tsv 33 C, 1 M); next: 9877 against the received copy or a Middle Department print (Lew Wallace papers), not-attempted, ~$2
- 17 neither-book entries (s2/confpair_pairs.tsv) - blocker: no-key-material; the 13 code words date 30 Dec 1864 - 13 Jul 1865, Cipher No. 3/No. 4 period; the Huntington holds only No. 5 (R8-ECK62); the one known No. 4 copy (Friedman Collection, Marshall Foundation) is Cloudflare-blocked from the cloud (403, 6 Oct 2026); next: the No. 4 copy read from a desk browser (LOCAL-QUEUE row, owner's machine), ~$1
- mssEC 18 entries still '?' - blocker: not-attempted; 100 under the legacy split, 137 '?' entries under split2 print_q; the 25 dated `?p` entries checked against the image for dropped marker words 7 Oct 2026 (AM-ECK62Q, PREREG-ECK62-QP: 0 of 25 carry a marker, control 25/25 marker tokens found, 0 cross-set; 0 moved; 4 are written in clear, no book applies; ec18/s2/image_qp.tsv); header 'No N' numbers are serials after spring 1864, not book markers (No 2 on 6 book-1 entries; No 3-7 exist); next: the 112 undated-match '?' entries by a different instrument (bigram support under both keys already tried, RUN6-ECK62), or leave '?' as the residue no print or image decides, ~$3

## Escalation (D12-E62H, 7 Oct 2026)
- [x] siblings: second IA scan of OR 49.1 and Papers of U. S. Grant vol. 11 for the Hurlbut-row M tokens (D12-E62H, 6 of 7 read); received ledgers mssEC 01-03 read 3 Oct 2026 (GAPS171) and mssEC 04-14 6 Oct 2026 (D1-ECK62L, 0 twins, Nutmeg 1863 witness); mssEC 12-13 for the Lehigh 1865 copies (D1-ECK62W, 0); every Lehigh in sent ledgers mssEC 18-19 (D1-ECK62S, 8 print-read, all Canby or 'can be'); every Leghorn/Legend/Leopard in mssEC 18-19 (R12A-ECKLEG, 48 print-read, 0 Hurlbut); parallel sent ledger mssEC 18 opened by text 4 Oct 2026 (GAPS206), read with Cipher No. 1 (A3V3-ECK18) and No. 2 (A3V3-ECK2)
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [ ] known-keys: Huntington cipher books searched for No. 3/No. 4: none (No. 5 only, mssEC 49-66), No. 5 values match none of the 14 words (R8-ECK62); next: Cipher No. 4 in the Friedman Collection (Marshall Foundation), from a desk browser, ~$1
- [x] print: wrong-telegram and conflict-pair tests done on legacy (R7B-ECK62, R7C-ECK62C) and split2 (R10-ECK62T: 0 wrong, 5 right, 12 undecided; primary untested at N 60); splitter fixed and adopted (R9-ECK62, R10-ECK62S, R10-ECK62T)
- [x] key-rebuild: Koran/Lamb/Luna/Indus done 3 Oct 2026 (GAPS191); Handle, Harry, author added at C (A3V3-ECKC); possessive and collision guard added to decode.py (RUN3-ECK62)
- [x] image-check: the ten mssEC 15 readings reconciled against the image (reading.md); the six mssEC 18 collision/conflict entries (DEF1-ECK62I) and the Lehigh key row (DEF1-ECK62P)
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 4 internal gaps; Hurlbut-row M tokens 7 -> 1 (D12-E62H); cheapest next: the 112 undated-match '?' entries by a different instrument, or leave '?' as the residue no print or image decides, ~$3; the No. 4 book for the 13 words waits on a desk-browser read of the Friedman copy

## D12-V62 verifier (7 Oct 2026, account 2, LANE DEFAULT-account-2-20261007-1210): grade-change check of D12-E62H (b5a795fe6)

Separate session from D12-E62H. Each M -> C checked against its cited print with a script on the IA `_djvu.txt` (no vision).
| token(s) | cited print | check | verdict |
|---|---|---|---|
| 9671.9 legend | OR 33 p.502 | warofrebellion33unit (sha matches or_volumes.tsv): "Washington, D. C., February 3, 1864 -- 4.30 p. m. ... Please communicate directly with General B. F. Butler, Fort Monroe, in regard to his proposed movements"; time and addressee match the ledger, between the 502/503 heads | keep C Butler |
| 9672.12 legend | OR 33 p.514 | same scan: "February 5, 1864 -- 11.30 a. m. ... General Butler again asks for a demonstration by your army"; p.514 | keep C Butler |
| 9785.169 legend | PUSG 11 | Google Books API, quoted phrase "spare Butler for the Chief Supreme Command": 2 hits, both The Papers of Ulysses S. Grant vol. 11 (r0d5C4hAav8C, 1T4fAQAAMAAJ, June 1-Aug 15 1864); snippet aligns word for word with "spare Legend for the supreme Princeton"; page not read | keep C Butler (page not established) |
| 9945.500 legend, leghorn | OR 49.1 p.580 | warofrebellion014901rootrich: "January 25, 1865 -- 6 p. m. ... More cavalry horses will be sent to you as soon as General Canby can be supplied" | keep C Canby / can be; **page corrected to p.581** (the telegram sits after the 581 running head, before 582) in legend_uses.tsv, leghorn_uses.tsv, hurlbut_row_grades.py docstring and .tsv (regenerated, --check current, counts unchanged), HYPOTHESES.md |
| 9952.516 lehigh | OR 49.1 p.646 | same scan: "February 4, 1865 -- 10 a. m. ... say 4,000 or 5,000. Canby has many dismounted men", before the 647 head | keep C Canby |
| mssEC 19 9174 lehigh, leopard (first) | OR 49.1 p.624 | same scan: "February 1, 1865 -- 13.40 p. m. Brig. Gen. EGBERT ALLEN, Louisville: ... sent by General Thomas to General Canby ... General Canby has been notified of this arrangement", p.624 | keep C Canby |
Result: 8 of 8 C kept, 0 dropped, 1 page citation corrected. ec18.py `--possessive --guard DIR62 --check` exit 0 legacy and --split2;
hurlbut_row_grades.py and lehigh_grades.py --check current; decode.py --check exit 0.

Pre-existing staleness (flagged by D12-E62H). Test: with ciphers/eckert-1864/key-no2.md put back at 67099403c (10:15 UTC, the last
commit of entries_b2.tsv; the only input that changed since is key-no2.md: ECK64-NO2, D12-E2, E1, E3, E4), `--book 2 --check`
(both splits), `ec18_align.py --check` and `--read-free --check` all exit 0; so the staleness is only the key-no2 rows. Regenerated
with their own scripts at HEAD's key-no2.md, all --check exit 0 after:
- `--book 2` legacy: 74 entries change; totals H 12907 -> 12911, C 138 -> 161, I 154 -> 226, M 10, oov 5064 -> 5056; fully keyed 18
  (H 294, C 9 -> 10, I 8 -> 12, M 0); book-2 OR matches 111 -> 112; meanings in print 0.737 -> 0.736 (control 0.425 -> 0.426);
  guarded tokens 440 -> 450. split2 the same shape (matches 118 -> 119, 0.746 -> 0.745, guarded 446 -> 456).
- Committed readings that change (readings_b2.md, both splits): 9681.34 "Monkey" -> [Schofield] (C); 9781.163 one more I;
  9848.277 and 9898.393 "stick" -> [.] (I), with 22 -> 26 and 7 -> 9 shared 5-grams with their OR print. These are Cipher No. 2
  readings of mssEC 18 (cross-book), not the counted eckert-1862 readings (H 367 C 4 unchanged).
- `ec18_align.py` (both splits): grades_after_all_tokens I 6 -> 9 (H 168, C 253 unchanged); align_entries 2 rows.
- `--read-free` (both splits): readings_free.md 13 / 15 lines change (key-no2 rows).
- Not regenerated (box): `ec18_align.py --rows align_free_rows.tsv --check` is stale both splits; cause not tested (it may be the
  same key-no2 rows); next: the old-key test above on it, then --write, ~$1.
AUDIT.md quotes no book-2 count, but its R12A recount (lines 393-394) quotes entries.tsv at C 64 M 7, which D12-E62H moved to C 70 M 1:
AUDIT.md section 'Propagation D12-V62' added; no N-class changes.
Requests: archive.org 58 (2 OR texts read first + 8 DIR62 + 48 OR; 1 HTTP 500 on 46.3, one retry after 15 s, sha then matched),
hdl.huntington.org 1, googleapis.com 1; >= 1.6 s apart. 0 subagents, 0 vision.

## B1320-A1 (7 Oct 2026, 13:4x-14:0x UTC by date -u, account 1 for the account-3 orchestrator): ec18 staleness closed
Separate session from D12-E62H and D12-V62. AUDIT.md: the D12-E62H regrades (6 Hurlbut-row M -> C, mssEC 19 9174 x2 M -> C)
were already carried in by D12-V62 ("Propagation D12-V62", 8 of 8 kept, 9945 p.580 -> 581); re-read, nothing to add, no
N-class changes. Data: vol18.json re-fetched (sha256 cb162574..., matches pilot1864/manifest.tsv), all 48 OR `_djvu.txt` of
or_volumes.tsv (every sha256 matches) and the 8 DIR62 1862 volumes, to scratch, not committed.
- The one stale output D12-V62 left, `ec18_align.py --rows align_free_rows.tsv` (both splits): old-key test as D12-V62's --
  key-no2.md put back at 93b80b20 (the version before ECK64-NO2's 500d30a6, 11:54 UTC) -> `--check` exit 0 both splits, so
  the staleness is only today's key-no2 rows. Regenerated with `--write` at HEAD's key-no2.md:
  legacy scored 816 -> 820, AGREE 325/816 = 0.398 -> 327/820 = 0.399, conflict 121 -> 122, collision 29 -> 30, control
  61/816 = 0.075 -> 61/820 = 0.074, grades H 61, C 360 -> 362, S 500 -> 502, I 1 -> 5; split2 768 scored, 328/768 = 0.427,
  control 0.087, H 70, C 365, S 432, I 5. Six entries change (9669.5, 9809.203, 9865.319, 9870.333, 10005.584, 10012.597):
  new key-no2 rows Monkey = Schofield (2 tokens now AGREE with the print), Yancy = Wednesday (CONFLICT with the printed
  dateline "Va. October 19, 1864"), stick = Period (I, not scored), telegram = Withdrawn (COLLISION). None is quoted in AUDIT.md.
- Checks after (all exit 0, legacy and --split2): `ec18.py --book 2 --possessive --guard DIR62 --check`, book-1
  `--possessive --guard DIR62 --check`, `--read-free DIR62 --check`, `ec18_align.py --check`, and `ec18_align.py --rows`
  align_free / align_flip / align_flipctl `--check`.
Requests: archive.org 56 (48 OR + 8 DIR62), hdl.huntington.org 1; >= 1.6 s apart. 0 subagents, 0 vision.

## LS3-R62 (8 Oct 2026, account 2, for LANE ST-LEDGER-3)
Solver session (10:17-10:5x UTC by date -u); brief `.claude/briefs/runs/2026-10-08-acct2-st-ledger3-workers.md` section LS3-R62.
Gap under test (D12-E62H Remaining gaps, gap 1): are the residue's M-graded tokens transcription slips the decode reads as code?
Intake gate (lane header, 10:1x UTC): `eckert-1862: partial (line 3) -- edition/page or full-text-search citation found within 6 lines` (exit 0).
Data to scratch, not committed: the 58 residue page texts (pages_manifest.tsv pointers; `residue_decode.py --check` current on
them, totals C 155 I 36 M 82 reproduced per entry by a scratch script); 13 OR 1862 `_djvu.txt` (vols. 5, 7 x2 scans, 8, 9,
10 pt1-2, 11 pt1/3, 12 pt1/3, 51 pt1, 53); page images 2583 px of 4960, 4979, 4982, 4983, 4984, 4992, 4999, 5024.
- Selection (script over the residue entries with >= 1 M token, 54 of 124; keyed share = key tokens / (key tokens + oov), then
  fewest oov): top six by share were 5024.1 (1.0), 4979.1 (0.875), 4982.1 (0.769), 4960.2 (0.765), 4999.1 (0.75), 4983.1 (0.667).
- OR re-grep before reading (lane pre-filter; 6-gram shingles of each entry's non-key words against the 13 volumes): four of
  those six are in print and are recorded N1-likely, not decoded further: 5024.1 OR I/51 pt1 about p.539 (24 6-gram hits),
  4960.2 OR I/51 pt1 about p.523 (17), 4983.1 OR I/51 pt1 pp.531-533 (69), 4979.1 OR I/53 p.513 (Washington 12 Feb 1862,
  McClellan to Halleck, "Retain the Ohio battery; also the other troops for Kansas if absolutely necessary. I would rather not
  hold back the Kansas infantry if you can help it"). The last corrects GAPS187's "entry 1 unprinted" for page 4979 (vol. 53
  was not in that grep); its print also witnesses wharf = infantry, Lamb = Kansas, Koran = Ohio for 12 Feb (not folded into
  key.md here). Of all 54 M-bearing entries, 20 have >= 3 6-gram hits in one OR volume (mostly OR 51 pt1).
- The six read (next by share with <= 2 hits, both hits checked by eye as different telegrams): 4982.1 (share 0.769; its 2 hits
  are McClellan's same-day telegram to Buell, OR 7, "what re-enforcements have been sent from your command ... up the
  Cumberland and Tennessee", a parallel, not this telegram), 4999.1 (0.75, 0 hits), 4984.3 (0.667, 0), 4992.1 (0.667, 0),
  4999.2 (0.667, 0), 4982.3 (0.667, 1 generic).
- Crops (pasted commands, one per entry region; scratch, not committed):
  `python3 tools/iiif_lines.py --image p4982.jpg --out crops --region 320,240,2000,920 --prefix p4982e1 --lines-per-crop 4`;
  `... p4982.jpg ... --region 320,2000,2000,880 --prefix p4982e3 --lines-per-crop 4`; `... p4999.jpg ... --region 300,180,1950,250
  --prefix p4999e1 --lines-per-crop 2`; `... p4999.jpg ... --region 300,1520,1950,300 --prefix p4999e2 --lines-per-crop 3`;
  `... p4984.jpg ... --region 320,1700,2000,800 --prefix p4984e3 --lines-per-crop 4`; `... p4992.jpg ... --region 330,330,2000,320
  --prefix p4992e1 --lines-per-crop 3`. Read by this session (no subagents), with one page overview each for layout.
- Result, every M token settled from the image (print/residue/image_check_ls3r62.tsv, 9 rows): 9 of 9 read exactly as the
  volunteer text has them (Myrtle, Mary, Camden, Ingress x2, jolly, Anthon, Humboldt x2), and all six head dates read as
  transcribed (Feb 14 2 PM, Feb 14 11 PM, Feb 19 x2, March 2d 1862, Feb 16). 0 transcription slips. Each M is a key-range M:
  the word's only witness is a single day or a range that misses the entry (Myrtle 21 Feb only, Mary 6 Feb only, Ingress 17 Feb
  only, Camden 16-21 Feb, Anthon Feb row ends 15 Feb, Humboldt and jolly rows themselves M). The image cannot move these; a dated
  witness can. One image-only detail outside the graded text: 4984.3's tail word "lose" is struck through (no deletion mark in
  the volunteer text); tail, ungraded, no change.
- Grades per entry, before = after (H/C/S/M/I): 4982.1 0/7/0/2/1; 4999.1 0/2/0/1/0; 4984.3 0/1/0/3/0; 4992.1 0/3/0/1/0;
  4999.2 0/3/0/1/0; 4982.3 0/4/0/1/1. Residue totals unchanged, C 155, I 36, M 82; `print/residue_decode.py --check` and
  `decode.py --check` re-run after: "residue readings are current", "reading.md is current", exit 0.
- Matched control (lane point: other books + a meaning-shuffled copy of the chosen key, seed 1862, residue_decode.py's own
  permutation): code-word tokens that fill their slot in a grammatical clause, chosen key / shuffled / No. 1 / No. 2 / No. 9
  (key.md, key-no2.md, key-no9.md of ciphers/eckert-1864, read literally):
  4982.1 10/10 / 0 / 0 / 1 ("what [Troops] have") / 0; 4999.1 3/3 / 1 ("[Gordonsville] road") / 0 / 0 / 0; 4984.3 4/4 / 0 / 0 /
  0 / 0; 4992.1 4/4 / 1 ("[Gordonsville] railway") / 0 / 0 / 0; 4999.2 3/4 (jolly unresolved) / 1 / 0 / 0 / 0; 4982.3 6/6 / 0 /
  1 / 1 / 0. The chosen key beats all four on every entry. Internal check: the time word matches the head's hour in both entries
  that carry one (4982.1 Sarah = 2 PM under "2 PM"; 4982.3 Francis = 11 PM under "11 PM"); No. 1, No. 2 and No. 9 time words there
  read 6.30 PM / 11 PM, 11.30 PM / 12.30 AM, 9.30 PM / 11 AM.
- Clause of authentication length: 4982.1 reads one clause carrying seven code tokens, "the number of troops sent up the
  [Cumberland River] & [Tennessee River] with [Grant] what [reinforcements] have since been sent from your Dept what from
  [Buell]'s Command in [Kentucky] and from the states in his Dept North of the [Ohio]", but two of the seven (the rivers) are M,
  so it does not count as an S/C stretch; whether a mostly-plain telegram with C-graded arbitraries clears the authentication
  distance is the verifier's call (rule 4a). The other five carry 1-4 code tokens each in otherwise plain text.
- Request counts: hdl.huntington.org 66 (58 page texts + 8 images), archive.org 17 (13 OR texts + 4 error pages for wrong
  ids), >= 1.6 s apart. 0 subagents; vision: 4 page overviews + 7 line crops.
Report what was found and where it was not found; no novelty class.
- Correction (LS3-V62, verifier, 8 Oct 2026): 4982.3 and 4999.2 are printed in OR ser. I vol. 52 pt 1, pp. 211 and 214 (not in the 13-volume re-grep above; "0 hits" was a gap in the volume set, not an absence); the print witnesses Camden = Thomas on 14 Feb. 4999.1, 4992.1, 4984.3 are clear text on the Huntington record (D2V-E74 shape, N1). 4982.1 N3 at D1. AUDIT.md "## AUDIT (LS3-V62)".

## Remaining gaps (finish-or-blocker pass, LS3-R62, 8 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82 (GAPS197); 6 residue entries' 9 M tokens image-checked 8 Oct 2026 (LS3-R62: 0 slips, grades unchanged); received ledgers mssEC 01-14 searched (GAPS171, D1-ECK62L): 0 code-bearing twins
- residue entries of mssEC 15 (about 290) - blocker: open-codes; image test of the M tokens run 8 Oct 2026 (LS3-R62: 9 of 9 M tokens in the six highest-share unprinted entries read as transcribed, dates too; the residue's M is key-range M, not transcription), and 20 of the 54 M-bearing entries are in OR 1862 print by a 6-gram re-grep (4979.1 in OR 53 p.513, correcting GAPS187); next: align those 20 printed entries to their print (print/or_align.py method) to give their M tokens dated C witnesses and widen the single-day key rows (Myrtle, Mary, Ingress, Camden, Humboldt), then regenerate the residue, ~$2
- residue code words not fixed by any known plaintext - blocker: open-codes; about 860 oov tokens remain (GAPS197); conflicts Lamb, Luna date-separated, Indus split by slot; table-change dates unwitnessed between 21 Mar and 25 May
- 1863-67 sent ledgers at grade H - blocker: not-attempted; state as in D12-E62H's Remaining gaps (Hurlbut-row M 7 -> 1); next: 9877 against the received copy or a Middle Department print (Lew Wallace papers), ~$2
- 17 neither-book entries (s2/confpair_pairs.tsv) - blocker: no-key-material; Cipher No. 3/No. 4 period; the one known No. 4 copy (Friedman Collection, Marshall Foundation) is Cloudflare-blocked from the cloud; next: the No. 4 copy read from a desk browser (LOCAL-QUEUE row, owner's machine), ~$1
- mssEC 18 entries still '?' - blocker: not-attempted; state as in D12-E62H's Remaining gaps; next: the 112 undated-match '?' entries by a different instrument, or leave '?' as the residue no print or image decides, ~$3

## Escalation (LS3-R62, 8 Oct 2026)
- [x] siblings: received ledgers mssEC 01-14 (GAPS171, D1-ECK62L), mssEC 12-13 (D1-ECK62W), parallel sent ledger mssEC 18 (GAPS206, A3V3-ECK18, A3V3-ECK2), second OR scans and PUSG 11 (D12-E62H)
- [x] clear-pages: no clear copy bound in mssEC 15 (Premise check (c), 172 page texts harvested 19 Sept)
- [ ] known-keys: Huntington cipher books searched for No. 3/No. 4: none (No. 5 only, R8-ECK62); next: Cipher No. 4 in the Friedman Collection (Marshall Foundation), from a desk browser, ~$1
- [ ] print: residue M tokens on the 20 printed residue entries not yet aligned to their print (LS3-R62 re-grep); next: or_align.py over them, ~$2
- [x] key-rebuild: Koran/Lamb/Luna/Indus (GAPS191); Handle, Harry, author (A3V3-ECKC); possessive and collision guard (RUN3-ECK62)
- [x] image-check: the ten mssEC 15 readings (reading.md); six mssEC 18 entries (DEF1-ECK62I); Lehigh row (DEF1-ECK62P); six residue entries' M tokens (LS3-R62, 0 slips)
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 4 internal gaps; cheapest next: align the 20 printed residue entries to their OR print for dated C witnesses, ~$2 (the image route for the residue M tokens is tested, 0 slips in six entries); the No. 4 book waits on a desk-browser read of the Friedman copy

## K8472 (8 Oct 2026, account 1, for LANE LEDGER): which book reads Huntington objects 8472 (mssEC 16) and 6254 (mssEC 22), and is 9660 a copy of 8472
Claimed 17:48 UTC by date -u; cap USD 5, box to 19:28 UTC. Status of this target unchanged (partial).

Prior-work step, hand checklist (civil-war adapter), first lines written before any priced step:
- check 1 (our own work, offline, 17:5x UTC, after `git fetch`): grep of 8472 / 6254 / 9660 / mssEC 16 / mssEC 22 in eckert-1862 and eckert-1864
  NOTES.md, AUDIT.md, HYPOTHESES.md, *.tsv, NEXT-STEPS.tsv, WORK-QUEUE.tsv, status.json and ROOM.md: only the LS-SCOUT rows
  (LEDGER-SCOUT-2026-10-07: "key factor 0.5, which book covers it is not established"), prefilter-ls4-parents.tsv (8472 = mssEC 16, 6254 =
  mssEC 22) and the one pointer arithmetic line for mssEC 18 in eckert-1864/NOTES.md; no read, no test, no ROOM claim before this one: CLEAR.
- check 2 (leaf and neighbours), 3 (holder transcription), 4 (editions) -- run under the hdl token / after page selection; lines follow below.

### Pre-registration (written before any ledger entry was scored)
Instrument: ciphers/eckert-1862/k8472_score.py. Books in hand: no1 (eckert-1864/key.md, Cipher No. 1), no2 (key-no2.md), no9 (key-no9.md),
mssEC15 (eckert-1862/key.md, Feb-Jul 1862). Per entry and book: share = recognised non-function tokens / non-function tokens; clauses = number of
maximal runs of >= 3 consecutive reading tokens, every adjacent pair an attested bigram of the pooled readings of the four books (leave-one-out for
an entry that is itself in the corpus), containing >= 1 token from a decoded code word. Each book gets two meaning-shuffled copies (word rows,
seeds 7 and 11). An entry passes for book B when share_B is strictly greater than every other book's share AND clauses_B is strictly greater than
both shuffled copies of B. VERDICT RULE: a book "reads" a ledger when it passes on >= 7 of the 10 test entries; if no book does, "no book in
hand reads it". Ties are not passes. Entries: 10 per ledger, >= 8 code-shaped words and not clear in their own transcription, chosen from the
25 pages per ledger before any scoring.
Matched control (rule 3), run BEFORE the targets and fixing what a verdict can mean: the same procedure on the first 10 entries of each book's own
ciphertext file with the true book (leave-one-out). Results (clause statistic v2; v1, a plain-bigram run count that did not depend on the decoded
tokens, gave 4/10 for no1 and was replaced before any target was scored, since shuffled copies leave it unchanged by construction):
no1 6/10, no2 8/10, no9 0/10, mssEC15 0/10 reads by this rule. Gate: a target verdict "book B reads ledger L" is licensed only for a book whose own
control reached >= 7/10 (today only no2); a "no book reads it" verdict is conditional: for no9 and mssEC15 (small books whose words are mostly
a subset of no1/no2, so the strict-share condition cannot hold even for their own entries) and for no1 (6/10) the instrument is below its gate,
so a negative for those three is "untested by this instrument", not a negative. No further retuning of the statistic (rule 3, third-attempt clause).

### K8472 results (run 17:5x-18:1x UTC; scoring after the pre-registration commit 76d30fd8)
Prior-work lines continued: check 2 (leaf/neighbours): the volunteer text of the 52 fetched pages and 14 neighbours shows no interlinear or marginal
decipherment and no clear copy (only the clerk's `period`/`applause` plain filler words); images not looked at (text route, rule 2: every verdict
below is conditional on the volunteers' transcription). Check 3: the holder's transcription is the input; Tomokiyo's cached pages
(sources/cryptiana/web, `mssEC 16`, `mssEC 22`, `Cipher Messages sent`) and the solver-diff tables: no hit on either ledger. Check 4 (editions): not run,
no entry was read or decoded (brief: no reading beyond the test) -- "unchecked", not clear.
Requests, hdl.huntington.org: 3 compound lists + 52 page texts + 14 neighbour texts = 69, 1.6-1.8 s apart, one token block each (take 17:55, release
17:57; second take 17:58 and release 18:0x for the 9660 comparison). Pages: obj8472/p*.json (25 spread over 405 pp.), obj6254/p*.json (25 over 301 pp.),
obj9660/ (2). Entries: obj<N>/entries.txt (10 each, k8472_select.py: >= 8 code-shaped words, best per stratum), scores: obj<N>/scores.tsv.

Test (shares = recognised tokens / non-function tokens, mean over 10; clauses beat both shuffled copies of the same book):
| ledger | no1 | no2 | no9 | mssEC15 | entries passing (need 7) |
|---|---|---|---|---|---|
| 8472 (mssEC 16, Aug 1862-Jan 1864) | 0.300 | 0.314 | 0.120 | 0.025 | no1 1, no2 1, no9 0, mssEC15 0 |
| 6254 (mssEC 22, AoP HQ Aug 1862-Apr 1863) | 0.248 | 0.243 | 0.081 | 0.015 | no1 0, no2 1, no9 0, mssEC15 0 |
Matched control (same code, leave-one-out, true book): mean true-book share no1 0.542, no2 0.618; passes no1 6/10, no2 8/10, no9 0/10, mssEC15 0/10.
Both ledgers' best shares (0.31, 0.25) sit far below the control's true-book shares for the two books that could read at all; no1 and no2 tie on
share within 0.01-0.02 (they share the Stager template words), which is what a book that reads neither looks like and also what a thin vocabulary
overlap looks like.

**Verdict, pre-registered rule: no book in hand reads object 8472 or object 6254.** What the control licenses: for no2 the negative is control-backed
(8/10 on its own entries, 1/10 on each target); for no1 (control 6/10, below gate), no9 and mssEC15 (control 0/10) the instrument cannot read them even when
they are the true book, so for those three the result is "untested by this instrument", not a negative (rule 3). Ledger-level conclusion stays
conditional on the volunteer transcriptions and on 10 selected, vocabulary-rich entries per ledger. By the 1862 NOTES (section 5) the book needed is the
filled-in book of the Aug 1862-1863 period; none is in hand (Huntington cipher-book search: mssEC 41-46 No.1, 47-48 No.2, 56 No.5, 67 No.9; see
Remaining gaps).

**Object 9660 vs 8472: not a duplicate copy, on the two dates compared.** 9660 p.35 (pointer 9343) opens 30 Aug 1862 10.10 AM (`For Axis All of
Berkshires Corps ...`) and 31 Aug 2.30 PM (Stager to Campbell, Michigan Southern, "General director of United States Military Rail Roads"); 8472 has
pp.28-29 (pointers 8098-8099) going from 25 Aug straight to 1 Sept, no 30-31 Aug entries, and the Campbell telegram is in none of the 8472 pages 8094-8103 (grep).
9660 p.195 (pointer 9503) carries 8 July 1863 12.30 PM `For Anna ... enemy is crossing at Williamsport` and 1.45 PM `For Bengal Oakum`; 8472 pp.248-250
(pointers 8318-8320) for 8 July hold different entries (11 AM Harrisburg, Baldwin Balto, 4.30 PM Caldwell/A of P) and not these two. The two books overlap in
period and share the form but not the entries sampled: 9660 is a second ledger (it records the 30 Aug-31 Aug and 8 Jul entries that 8472 lacks) to be tested
on its own, not skipped as a copy. Not found: any entry text common to both; two dates only.

## Remaining gaps (K8472, 8 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%); K8472 read no entry of objects 8472/6254/9660 (book test only, 20 entries scored, none decoded for reading).
- object 8472 (mssEC 16) entries - blocker: no-key-material; the book of the Aug 1862-Jan 1864 period is not in hand (no book reads it, no2 negative control-backed)
- object 6254 (mssEC 22) entries - blocker: no-key-material; same
- object 9660 (357 pp., 30 Aug 1862 and 8 Jul 1863 entries absent from 8472) - blocker: not-attempted; only two dates compared, no entry of 9660 scored; next: the same 10-entry test with entries picked from 9660's own pages, ~$0.5

## Escalation (K8472)
- [x] siblings: 9660 vs 8472 compared on two dates (different entries)
- [x] clear-pages: no clear copy or gloss in the volunteer text of the 66 pages read
- [ ] known-keys: a filled-in book of the Aug 1862-1863 period (Tomokiyo's concordance lists No. 3/4/7/12 outside Huntington's mssEC 41-67 set); next: Cipher No. 4 copy (Friedman Collection) from a desk browser, ~$1
- [n/a] print: no entry was decoded
- [n/a] key-rebuild: no reading; a rebuild from OR matches needs the entries' counterparts, not started
- [ ] image-check: the test used volunteer text only; next: 3 page images per ledger if a book is found
- [n/a] retry: no failed attempt
Verdict: keep going: 1 internal gap; cheapest next: the 10-entry book test on 9660's own pages, ~$0.5 (8472 and 6254 wait on a book not in hand; known-keys and image-check steps open).

## E62-ALN (8 Oct 2026, account 1, for LANE LEDGER)
Worker E62-ALN, 17:50-18:36 UTC by date -u, cap 3. Not complete: three of five volumes aligned, two unrun (see gaps).
Prior-work checks (by hand; tools/prior_work.py absent): own work -- grep of this folder's NOTES/HYPOTHESES/AUDIT for or_align on the
residue: only LS3-R62's "[ ] print" row, no artefact (not done); ROOM -- no live claim on this target; holder transcription -- the
58 residue page texts re-fetched from hdl.huntington.org (59 requests, one retried; `residue_decode.py --check` current on them);
OR vols. 5, 7 (two scans), 8, 9, 10 pt1-2, 11 pt1/3, 12 pt1/3, 51 pt1, 53 (rootrich; the 1972 reprint is access-restricted) from
archive.org (14 requests).
- The 20-entry list of LS3-R62 was scratch and could not be reproduced. `print/residue_select.py` (new) re-selects M-bearing residue
  entries by shared word n-grams with one OR volume: 6-grams >= 3 gave 10 entries, 5-grams >= 3 (the or_align anchor rule) gave 17,
  both on the ledger words and the decoded reading. 4979.1 (OR 53 p.513) is missed by both because the volume's OCR breaks
  "abso lutely"; it was added by hand. So 18 entries, not 20; the difference is the selector, not a finding.
- `print/or_align.py` unchanged, per volume, output in `print/residue_print/<volume>/`. Run: vol. 53, 10 pt1, 10 pt2, 12 pt3 (100 shuffles),
  vol. 51 pt1 (3 shuffles, slow). Not finished: vol. 9 (killed), vol. 7 (timeout at 150 s); vol. 8 not started.
- Result, M tokens with a dated C witness: none. The five single-day rows named in the brief (Myrtle, Mary, Ingress, Camden,
  Humboldt) get no date from any aligned entry (no ledger occurrence of them is in the aligned set), so key.md is unchanged.
  Agreement with key.md: Koran = Ohio and Lamb = Kansas (4979.1, 12 Feb, OR 53 p.513), Negus = Potomac and Opal = Winchester
  (5015, OR 51 p.532), Whale = cavalry, whistle = enemy (5021/5028, p.537): these re-witness existing rows on new days, not
  entered. New single, not entered: Eddy = Banks (5021 entry 0, p.537, one telegram). Conflict: Merlin = Maryland vs key.md Virginia
  (5021.1, 25 Feb), logged in HYPOTHESES.md with both witnesses. Junk: War = "Avar" (OCR), valleys = department (vol. 12 pt3 p.332).
- Held-out and control: 0 scored in every run (test 0/0), so no gain claim; the proposals are single occurrences.
- Residue before/after: key.md unchanged, so `residue_decode.py --check` current and totals C 155, I 36, M 82 before = after.
## Remaining gaps (E62-ALN, 8 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%), all ten N1; residue 58 pages, 124 entries decoded at C 155, I 36, M 82; 18 printed residue entries selected, 11 aligned to OR print 8 Oct 2026 (E62-ALN: 0 new dated C witnesses, 1 conflict logged, key.md unchanged)
- residue entries of mssEC 15 (about 290) - blocker: open-codes; the printed ones in vols. 9, 7 and 8 (about 5 entries) are unaligned; next: or_align.py with --shuffles 3 on those three volumes (each run takes minutes), ~$0.5
- Myrtle, Mary, Ingress, Camden, Humboldt single-day rows - blocker: no-key-material; none of the aligned entries carries one of the five words, so the print gave no date; next: select printed residue entries by those words, not by M count, ~$1
- residue code words not fixed by any known plaintext - blocker: open-codes; Merlin = Maryland (print, 25 Feb) conflicts with key.md Virginia, logged in HYPOTHESES.md; next: read the 5021 page image at that line, ~$0.5
- 17 neither-book entries (s2/confpair_pairs.tsv) - blocker: no-key-material; Cipher No. 3/No. 4 period, as LS3-R62; next: the Friedman Collection No. 4 copy from a desk browser, ~$1

## Escalation (E62-ALN, 8 Oct 2026)
- [x] siblings: as LS3-R62 (received ledgers mssEC 01-14, mssEC 12-13, mssEC 18, second OR scans)
- [x] clear-pages: as LS3-R62 (no clear copy bound in mssEC 15)
- [ ] known-keys: as LS3-R62; next: Cipher No. 4 in the Friedman Collection from a desk browser, ~$1
- [ ] print: vols. 9, 7, 8 remainder of the printed residue entries; next: or_align.py --shuffles 3, ~$0.5
- [x] key-rebuild: as LS3-R62; no key.md change here
- [x] image-check: as LS3-R62 (six residue entries' M tokens, 0 slips)
- [n/a] retry: no failed attempt to retry; no negative claimed on this target
Verdict: keep going: 2 internal gaps; cheapest next: or_align.py on vols. 9, 7, 8 for the remaining printed residue entries, ~$0.5

## E62-9660 (8 Oct 2026, account 1, for LANE LEDGER)
Worker E62-9660, claimed 20:47 UTC by date -u, cap USD 3. Status of this target unchanged (partial). Rule 10: found / not found only, no novelty class.
Prior-work lines (by hand; tools/prior_work.py not run): own work -- K8472 above: 9660 compared to 8472 on two dates only, "not attempted"; no ROOM claim
on 9660 before this one: CLEAR. Holder transcription: the volunteer text is the input (volunteer text only, no image looked at; every verdict is
conditional on it, rule 2). Leaf/neighbours, editions: no entry was read or decoded, so not run -- "unchecked", not clear.

### Pre-registration
Exactly K8472's: instrument k8472_score.py, same four books, same pass rule (strictly greatest share AND clauses beyond both shuffled copies; reads when
>= 7 of 10), and K8472's matched control (no1 6/10, no2 8/10, no9 0/10, mssEC15 0/10) is the control for this run, unchanged (same instrument, same
code, no retuning). Entries picked before scoring by k9660_select.py (K8472's selector, object 9660 only): 25 pointers evenly spaced over the 357
(9303..9659, plus the two already cached from K8472, 9343 and 9503), >= 8 code-shaped words, best per stratum. Selection committed before scoring.

### Result (obj9660/entries.txt, scores.tsv)
| ledger | no1 | no2 | no9 | mssEC15 | entries passing (need 7) |
|---|---|---|---|---|---|
| 9660 (mssEC 17, 30 Aug 1862 - 1863) | 0.274 | 0.307 | 0.154 | 0.017 | no1 1, no2 2, no9 0, mssEC15 0 |
**Verdict (pre-registered rule): no book in hand reads object 9660.** Same shape as 8472/6254: no1 and no2 tie within 0.03 on share (shared template
words). For no2 (control 8/10) the negative is control-backed (2/10 here); for no1 (control 6/10, below gate), no9 and mssEC15 (control 0/10) it is
"untested by this instrument", not a negative (rule 3). Conditional on 10 vocabulary-rich selected entries and the volunteer transcription. Entry 01
(12 Aug 1862, "For Axis The Aragon informs me ...") and entry 10 (code 33, no1 8 / no2 6 clauses, the strongest) are the nearest to readable under
no1/no2 but neither clears the pass rule; no 1862-63 entry of 9660 is listed as readable, so none is handed on. Requests, hdl.huntington.org: 25
dmGetItemInfo (1.7 s apart, one token block 20:47-20:49), plus 1 stray API probe at 20:49 made after my release (logged in ROOM).

### Part 2: the remaining printed residue entries (vols. 9, 7, 8), offline after one page re-fetch
Page texts (scratch, not committed) re-fetched: 58 requests, api items/<pointer>/false, 1.7 s apart, one token block 20:51-20:57; all 58 sha256 equal
print/residue/pages_manifest.tsv (unchanged since 3 Oct). OR vols. from archive.org `_djvu.txt` (3 requests): warofrebellion09secrrich, warofrebellionco0007vari,
warofrebellionco08unit. `print/residue_select.py --n 5 --min 3` (E62-ALN's anchor rule) on these three volumes gives 9 entries (print/residue_print/selected_e62-9660.tsv):
4973, 4983, 5048, 5056, 5103 (vol 9), 4982 (vol 7), 4962, 4985, 5015 (vol 8) -- 9, not E62-ALN's "7 remaining", since its 18 were chosen across all volumes and
which of them it had aligned was not recorded. `print/or_align.py --shuffles 3` unchanged, per volume: vol 9 completed (7 telegrams, 7 entries on 5 pages);
vols 7 and 8 wrote align_pairs/proposals within 3 minutes and then did not return from the held-out stage in 30 minutes (the same hang as E62-ALN's vol 7
timeout), killed; the held-out figure is 0/0 by construction at one occurrence each.
Result (print/residue_print/<volume>/): 3 candidate occurrences in all. your -> "my" (vol 9, 4983, OR p.309): not a code word, a wording variant. widow ->
"re enforcements" (vol 7, 4982, OR p.612): same meaning as key.md reinforcements, spelling only, no conflict. thinks -> "has received" (vol 8, 4985,
OR p.598): single occurrence, not in key.md, not entered. No dated C witness for Myrtle, Mary, Ingress, Camden or Humboldt. key.md unchanged; HYPOTHESES.md
unchanged (no conflict). Residue C/M/I before = after: key.md unchanged, C 155, I 36, M 82 as E62-ALN. Unexplained: `residue_decode.py --check` on the
fresh pages printed "residue readings are stale" with key.md, decode.py and the page hashes all unchanged since E62-ALN reported it current; cause not found
(not rerun alone, and --write not run: not this job's); flagged in ROOM.
Not found: any residue entry of the three volumes with two occurrences of one ledger word, so no held-out figure and no gain claim.

## Remaining gaps (E62-9660, 8 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%); the 9660 and residue steps add no reading.
- object 9660 (mssEC 17, 357 pp.) entries - blocker: no-key-material; no book in hand reads it (10-entry test; no2 negative control-backed, no1/no9/mssEC15 untested by this instrument)
- object 8472 and 6254 entries - blocker: no-key-material; as K8472
- residue entries printed in vols. 9, 7, 8 - blocker: too-short; 9 selected, 3 candidate occurrences, all single or non-code
- residue_decode.py --check reports stale on unchanged inputs - blocker: open-codes; cause of the stale report unknown; next: rerun --check alone and diff pages.tsv, ~$0.3
- Myrtle, Mary, Ingress, Camden, Humboldt single-day rows - blocker: no-key-material; none of the 9 printed entries carries one; next: select printed residue entries by those words in the other OR volumes, ~$1
- Merlin = Maryland (print) vs key.md Virginia - blocker: open-codes; the conflict rests on one print occurrence; next: read the 5021 page image at that line, ~$0.5

## Escalation (E62-9660)
- [x] siblings: 9660 tested on its own 25 spread pages against four books
- [x] clear-pages: no clear copy or gloss in the volunteer text of the 27 pages read
- [ ] known-keys: Cipher No. 4 copy in the Friedman Collection from a desk browser; next: owner's desk runner, ~$1
- [x] print: vols. 9, 7, 8 aligned; 3 candidate occurrences, none entered
- [n/a] key-rebuild: no new C witness
- [ ] image-check: volunteer text only; next: 3 page images of 9660 if a book is found
- [n/a] retry: no failed attempt
Verdict: keep going: 2 internal gaps; cheapest next: rerun residue_decode.py --check alone to explain the stale report, ~$0.3 (books for 9660, 8472 and 6254 wait on no-key-material)

## E62-STALE (9 Oct 2026, account 4, for LANE DEFAULT-account-4-20261009-1051)
Worker E62-STALE, 11:03 UTC by date -u, cap USD 2.5. Status of this target unchanged (partial). Rule 10: found / not found only, no novelty class.
Prior-work lines (by hand; `tools/prior_work.py` could not run: eckert-1862 has no items.tsv row for pointer 5021): own work -- E62-ALN's Merlin pair and
HYPOTHESES.md; no other ROOM claim on 5021; "unchecked" for editions beyond OR 51 pt 1.
(a) Stale `residue_decode.py --check`: NOT rerun and NOT explained. It needs all 58 page texts re-fetched from hdl.huntington.org (58 requests); the brief
caps this job at 15 hdl requests, so it stopped there rather than exceed it. What is established: (1) page 5021's text fetched today has the sha256 in
pages_manifest.tsv (fd4663cc...), so the Huntington text has not changed for at least that page; (2) E62-9660's stale report was made with the script as it stood
before FIX-DEC (9e576d1d, 8 Oct 21:3x UTC), which read every `*.json` >= 4956 in the pages dir, and E62-9660 shared that dir with other fetches
(the 9660 pages are pointers 9303-9659), which changes the page set and the carried date; FIX-DEC now reads only manifest pointers. That is the leading candidate,
untested on the real 58 pages. Next: one job with a 58-request hdl budget (about 4 minutes at 3.3 s) into a clean directory: `residue_decode.py DIR --check`; if
it exits 0 the cause is the shared dir; if 1, diff pages.tsv vs `--write` output into scratch. ~USD 0.3.
(b) Merlin: image read, ledger word is Merlin; both witnesses logged in HYPOTHESES.md (Virginia OR 7 p.584 and June pages; Maryland OR 51 pt 1 p.537). Not resolved,
key.md unchanged. Requests: hdl.huntington.org 2 (item 5021 text, one IIIF image at 2583 px), archive.org 1 (`_djvu.txt` of warofrebellion511unit) + 1 advancedsearch
+ 3 be-api phrase searches (no useful hit: unrestricted phrase search returns unrelated books).
(c) Printed entries for Myrtle, Mary, Ingress, Camden, Humboldt in other OR volumes: not run. The residue entries carrying them are in readings.md (Feb 14 Halleck
with Cumberland/Tennessee River, 16 and 19 Feb Scott, 14 Feb Buell with Thomas, 18 Feb Camden, Humboldt = Lander entries); candidate volumes beyond vols. 5, 7-12, 51, 53
(OR ser. I vol. 52 pt 1, ORN) need their IA identifiers fixed first, and unrestricted be-api phrase search is noise, so a volume-restricted search is the
next step, ~USD 1.

## Remaining gaps (E62-STALE, 9 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%); this job adds no reading.
- residue_decode.py --check reports stale on unchanged inputs - blocker: open-codes; leading cause the shared pages dir before FIX-DEC, untested; next: one 58-request clean-dir rerun, ~$0.3
- Merlin = Maryland (25 Feb, image-confirmed, OR 51 pt 1 p.537) vs Virginia (OR 7 p.584, OR 12) - blocker: open-codes; a second Maryland or Potomac-line occurrence would split by line or date; next: grep the Feb ledger pages for Merlin in other lines, ~$0.5
- Myrtle, Mary, Ingress, Camden, Humboldt single-day rows - blocker: no-key-material; no printed text for these entries in the volumes searched so far; next: volume-restricted phrase search in OR ser. I vol. 52 pt 1 and ORN for the readings.md entries carrying them, ~$1
- object 9660, 8472 and 6254 entries - blocker: no-key-material; as E62-9660

## Escalation (E62-STALE)
- [x] siblings: no new sibling; Merlin's pages 5079, 5083 (June, Virginia) set beside 5021
- [x] clear-pages: none
- [ ] known-keys: Cipher No. 4 copy in the Friedman Collection; next: owner's desk runner, ~$1
- [ ] print: vol. 52 pt 1 and ORN for the five single-day rows, ~$1
- [n/a] key-rebuild: Merlin logged, key.md unchanged
- [x] image-check: 5021 read 9 Oct 2026 (Merlin)
- [ ] retry: --check rerun in a clean dir, ~$0.3
Verdict: keep going: 2 internal gaps; cheapest next: clean-directory `residue_decode.py --check` with 58 hdl requests, ~$0.3

## E62-CHECK2 (9 Oct 2026, account 4, for LANE DEFAULT-account-4-20261009-1051)
Worker E62-CHECK2, 11:24-11:5x UTC by date -u, cap USD 3. Status unchanged (partial). Rule 10: found / not found only, no novelty class. Prior-work lines (by hand;
tools/prior_work.py cannot run on this folder, no items.tsv row, as E62-STALE): own work = E62-ALN/E62-9660/E62-STALE sections above; ROOM claims on eckert-1862: none live.
(a) Stale `residue_decode.py --check`, explained. All 58 page records re-fetched from hdl.huntington.org into a clean scratch dir (items/<pointer>/false, 3.3 s apart, one
transient curl 000 on 5014, retried once, 200): 58 of 58 text sha256 equal print/residue/pages_manifest.tsv; `residue_decode.py <clean dir> --check` = "residue readings are
current", exit 0. Cause test: the script as it stood before FIX-DEC (9e576d1d^, which reads every `*.json` >= 4956 in the dir) on the same clean dir: exit 0; on a copy of it
plus one extra page file (9400.json, a copy of 5104): "stale", exit 1; the current script on that same dir with the stray file: exit 0. So the stale report of 8 Oct (E62-9660)
was the shared pages dir under the pre-FIX-DEC script (page set changed by files outside the manifest), not a change in the Huntington text, key.md or decode.py. No file
regenerated (nothing stale). Control: the current script with the stray file stays current (the FIX-DEC fix works), and the old script on the clean dir is current (the old
script was not wrong on the right page set).
(c) Printed text for the single-day rows (Myrtle, Mary, Ingress, Camden, Humboldt), other OR volume. Volumes new to this folder: Ser. I vol. 52 pt 1 (IA
warofrebellion015201rootrich, title page "Series I Vol LII in two parts", `_djvu.txt`, 2.7 MB) and vol. 5 (warofrebellionco0005unit_i9i6). 13 residue entries (pages 4982,
4984, 4992, 4998, 4999, the ones carrying the five words plus their page neighbours in readings.md) compared by shared 4-word runs of the decoded reading, with the same
entry word-shuffled as control (seed 1862): shuffled 0 hits on every entry in both volumes; real entries 0-34. Output print/residue_print/vol52p1/ngram4_results.txt,
script ngram_check.py (needs the two djvu files in scratch).
Found: one entry, 4982 entry 3 (McClellan to Buell, 14 Feb 1862, 11 PM, "Telegraph me in cipher, and much detail, the position of your troops ... Where is Thomas, and
where is Carter? ... Bowling Green line ... line of the Cumberland. Write fully"), 34 shared 4-grams, in vol. 52 pt 1 under the page header numbered 209 (djvu text, page image
not read). The ledger reads Camden (image-checked LS3-R62) where the print has "Thomas": a dated plain-text witness for Camden = Thomas on 14 Feb, outside key.md's 16-21 Feb
range. Not entered: key.md unchanged, grade stays M for the ledger token (one occurrence, the print is a witness not a key source; a `decode_key --try`-style test needs a
second occurrence). 4992 entry 2 (McClellan to Foote, 16 Feb, "Sorry you are wounded ...") also in vol. 52 pt 1 (16 shared 4-grams); it carries no M token.
Not found: the Halleck 14 Feb 2 PM entry (Myrtle, Mary) as a whole in either volume (only formula runs: "as soon as possible", "the number of troops"); the Scott 16/19 Feb entries
(Ingress) and the 2 Mar Rosecrans/Lander entry (Humboldt): only formula runs ("I do not know what", "I want you to keep a", "what news have you" -> a Farragut telegram of 1864); no
Myrtle/Mary/Ingress/Humboldt witness from the print in these two volumes. ORN not searched.
Requests: hdl.huntington.org 60 (58 + the transient + 1 retry), archive.org 4 (advancedsearch 2, `_djvu.txt` 2). Subagents: 0.

## Remaining gaps (E62-CHECK2, 9 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%); this job adds no reading.
- Myrtle, Mary, Ingress, Humboldt single-day rows - blocker: no-key-material; vols. 5 and 52 pt 1 give no witness; next: ORN (Official Records of the Navies, Feb 1862, Foote/Tennessee River items) and vol. 7's Halleck-McClellan pages by phrase, ~USD 1
- Camden = Thomas on 14 Feb (OR 52 pt 1, p. 209 header) - blocker: open-codes; one occurrence, graded M; next: read the OR 52 pt 1 page image at that telegram and look for a second Camden entry 13-15 Feb in the ledger, ~USD 0.5
- Merlin = Maryland vs Virginia - blocker: open-codes; as E62-STALE
- object 9660, 8472 and 6254 entries - blocker: no-key-material; as E62-9660

## Escalation (E62-CHECK2)
- [x] siblings: no new sibling
- [x] clear-pages: none
- [ ] known-keys: Cipher No. 4 copy in the Friedman Collection; next: owner's desk runner, ~USD 1
- [ ] print: ORN and the OR vol. 7 Halleck pages for the four unmatched words, ~USD 1
- [n/a] key-rebuild: Camden = Thomas logged, key.md unchanged
- [ ] image-check: OR 52 pt 1 page image for Camden; next: IA reader by a person or the Hathi copy, ~USD 0.5
- [x] retry: residue_decode.py --check rerun clean, current; stale cause explained
Verdict: keep going: 2 internal gaps; cheapest next: check the Camden second occurrence in the ledger text, ~USD 0.5

## E62-CAM (10 Oct 2026, account 1, for LANE LEDGER-11)
Worker E62-CAM, 05:48-05:5x UTC by date -u, cap USD 2. Status unchanged (partial). Rule 10: found / not found only, no novelty class. Prior-work lines (by hand;
tools/prior_work.py cannot run on this folder, no items.tsv row, as E62-STALE/E62-CHECK2): own work = E62-STALE and E62-CHECK2 sections above; ROOM claims on eckert-1862: none live.
Intake gate: `eckert-1862: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`. No key.md edit; residue_decode.py not rerun (nothing regenerated).
(1) Camden, from print/residue/readings.md (the 58-page decode on disk; no hdl request). Camden -> Thomas occurs once in 13-15 Feb: page 4982, 14 Feb 11 PM, McClellan to Buell
("Where is [Thomas] & where Carter", the E62-CHECK2 print witness). The 13 and 15 Feb entries (pages 4979, 4983-4985) contain no Camden. The only other Camden token in the decode
is page 4998, 18 Feb, an arrest order ("For William Rabe W S Marshall <deletion>Nugget</deletion> <insertion>Camden</insertion> a man named Harold and Lady Secure ...", signed L Thomas,
Adjt Genl): a volunteer-marked insertion over a struck word, not decoded by the dated rule; "Thomas" in that sentence would not read (Thomas would be the object of "For"), so it is
a second Camden token with no value: not a second Thomas witness. Not found: a second Camden=Thomas occurrence 13-15 Feb. Camden stays one occurrence, M; unchanged.
(2) Merlin, same source. Merlin tokens in the decoded pages: 7 Feb (page 4969, "operations in M[Merlin] [Virginia]" read Virginia, matches key.md OR 7 p.584) and 25 Feb (page 5021,
Lander, "on the [Virginia] side", the Maryland witness OR 51 pt 1 p.537). The ledger Merlin tokens are rendered with the key value in readings.md, so a grep for the word
finds only the raw ciphertext.txt line 14 ("western Merlin"); by value, [Virginia] occurs on 7 Feb and 25 Feb only, [Maryland] never. No third Merlin line in Feb-Jul pages in the decode.
Not found: a Merlin line that splits Maryland from Virginia by line or date beyond the 25 Feb entry already logged (HYPOTHESES.md). Not resolved; key.md unchanged.
(3) ORN Ser. I vols. 22 and 23, archive.org `_djvu.txt` (IA ids officialrecordso0022unse, 2.85 MB, and officialrecords15unkngoog, "ser.1:v.23", 2.39 MB). All 124 residue entries against both
by shared word runs, entry word-shuffled as control (seed 1862): print/residue_print/orn/ngram_orn.py (4-grams: almost every entry hits both volumes, formula phrases such as "the Secretary of
War", shuffled 0-1; not a discriminating gate) and longest_run.py (longest shared run, flag >= 7 words; results in longest_run_results.txt). Longest runs: only 5 entries reach 7+ words
(4975 9 Feb Buell 7/7, 4983 14 Feb Humbolt 5/7 "to the gallant officers and men under", 4995 17 Feb 7/5, 5014 23 Feb Dix 7/5, 4992 16 Feb Swain-Foote 0/9 "with what force do you return i send nearly");
shuffled 0 everywhere. Found: the 16 Feb McClellan-to-Foote entry (no M token; the one CHECK2 already placed in OR 52 pt 1) also in ORN vol. 22 (9-word run). Not found: the 14 Feb 2 PM
Halleck entry (Myrtle, Mary; page 4982) as a whole (longest run 5, "as soon as possible the"), the 16 and 19 Feb Scott entries (Ingress), the 14 Feb Humbolt entry as a whole (7-word run is a
formula sentence of thanks), in ORN vols. 22-23. The page images of ORN not read. OR ser. I vol. 7's Halleck-McClellan pages: not re-searched (GAPS113 already ran vols. 7, 9-12 with or_match.py).
Requests: archive.org 3 (advancedsearch 1, `_djvu.txt` 2), hdl.huntington.org 0. Subagents: 0.

## Remaining gaps (E62-CAM, 10 Oct 2026)
Read so far: 10 of about 300 mssEC 15 entries at grade T (about 3%); this job adds no reading.
- Myrtle, Mary, Ingress, Humboldt single-day rows - blocker: no-key-material; vols. 5, 52 pt 1 and ORN 22-23 give no witness; next: ORN vol. 21 and 24 (Gulf/Atlantic, probably out of subject), Halleck Papers or the Friedman copy of Cipher No. 4 via the owner's desk runner, ~USD 1
- Camden = Thomas on 14 Feb (OR 52 pt 1 p. 209 header) - blocker: open-codes; no second Camden 13-15 Feb in the decode; 18 Feb Camden is an undecoded insertion token; next: image check of 4998 Camden insertion (does the key range 16-21 Feb value Thomas fit "For William Rabe ... Camden"?), ~USD 0.4
- Merlin = Maryland vs Virginia - blocker: open-codes; two Merlin tokens only (7 and 25 Feb), no third to split; next: Merlin occurrences in the June pages by value (5079, 5083) already logged; none new
- object 9660, 8472 and 6254 entries - blocker: no-key-material; as E62-9660

## Escalation (E62-CAM)
- [x] siblings: no new sibling
- [x] clear-pages: none
- [ ] known-keys: Cipher No. 4 copy in the Friedman Collection; next: owner's desk runner, ~USD 1
- [x] print: ORN vols. 22-23 run (found: Foote 16 Feb only); OR vol. 7 done in GAPS113
- [n/a] key-rebuild: nothing added, key.md unchanged
- [ ] image-check: 4998 Camden insertion, ~USD 0.4
- [n/a] retry: nothing failed to rerun
Verdict: keep going: 2 internal gaps; cheapest next: image check of the 4998 Camden insertion, ~USD 0.4
