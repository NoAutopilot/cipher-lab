# Eckert Papers, 1862 "Ciphers Sent" ledger (Huntington mssEC 15)

status: partial
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

## 4. The ten readings (ciphertext.txt, reading.md, decode.py)

Ten entries of 5-21 Feb 1862 (McClellan, Stanton and Lincoln to Halleck, Buell, Hunter and Lane, Scott),
chosen because the Official Records print them. Two independent transcription passes by subagents from the
page images, reconciled against the image with the volunteer transcription as third witness (reading.md,
"Reconciliation": 14 disagreements, none on the sense, three on code words, all resolved). Result: all ten read
cleanly and agree with the printed text word for word apart from clerical variants; 86 code-word tokens graded C,
3 I, 2 M, 0 H. `python3 decode.py --check` regenerates the readings from ciphertext.txt and key.md and exits 1
if reading.md is stale. Per CLAUDE.md rule 4 this is a known-plaintext result, not an H reading.

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
