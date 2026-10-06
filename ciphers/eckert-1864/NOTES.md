# Eckert Papers, 1864 "Ciphers Sent" ledger (Huntington mssEC 19) read with Cipher No. 1 (mssEC 41)

status: partial
novelty: E4 N4, E5 N4 (no prior decipherment located; AUDIT.md 'N4 set (LANE W2 worker E2)', 24 Sept 2026); E6 N1, E12 N1
checked: 20 Sept 2026 (section 8 added; sections 1-7 as checked 19 Sept 2026)
editions read (restated from AUDIT.md sections 1, 7-8 on 3 Oct 2026 for the intake gate; classes unchanged): Official Records ser. I vol 32 pt 3 p.498 (E6, word for word) and p.213 (the p.[47] entry read by the project blog), vol 33 p.279 (Butler's reply to E4); Butler Correspondence vol IV p.112 (E5's antecedent); Basler, Collected Works of Lincoln vol 7 pp.479-480 (E12); open web and blogs: section 'Web and blog check' below.
target: QUEUE.md rank 1, "Thomas T. Eckert Papers, US Military Telegraph: ledgers of telegrams sent 'still in
code', 1862-67 (Huntington mssEC 1-76)". Second pilot, recommended in ciphers/eckert-1862/NOTES.md section 5:
one 1864 sent ledger read entry by entry against the filled-in cipher book the Huntington holds.

## 1. Is it already decoded? (CLAUDE.md rule 1, checked 19 Sept 2026)

Same verdict as ciphers/eckert-1862/NOTES.md section 1, which was checked the same day and applies to the whole
series: transcribed by Decoding the Civil War (2016-17), published on the Huntington item pages with the code
words as written, decoded nowhere. Tomokiyo (sources/cryptiana/web/civilwar1.htm) identifies the printed
ciphers of the books mssEC 37-67 and gives worked examples of Cipher No. 1 (Plum's sheet; Lincoln to Weitzel,
12 April 1865) but does not read the ledgers; neither solver repository has an Eckert item. Nothing new was
found on 19 Sept 2026 for "mssEC 19" or "Cipher No. 1" beyond those pages.

**Correction, 20 Sept 2026 (verifier session, AUDIT.md section 7):** "decoded nowhere" was too strong. The
project blog read one mssEC 19 entry with Cipher No. 1 in public: "Now, Jesse", 26 June 2017
(https://decodingthecivilwar.wordpress.com/2017/06/26/now-jesse/), Grant to Sherman, 31 March 1864, p.[47],
read with the sister copy mssEC 44 and matched to OR I/32 pt 3 p.213. Other posts read single entries of
other ledgers. No systematic decoding of the ledgers, and no reading of pages 49, 58 or 142, was found; the
project's decoding phase ("Phase 3") was planned and never launched (AUDIT.md, "Corpus question").

## 2. Which ledger, which cipher, which book

- Ledger: mssEC 19, "United States Military Telegraph, War Department. Sent" (object 9302, 415 page images,
  405 with volunteer text), 27 Jan 1864 to Dec 1865. mssEC 18 (object 10074, 413 images, Jan 1864-Dec 1865)
  is the parallel volume; not opened.
- Cipher: the entries of Jan-Feb 1864 to the eastern posts are still in the older Stager vocabulary (signature
  "Applause"/"Abortion" = Halleck; Youth = troops; Zodiac = movement, i.e. the mssEC 67 template meanings of
  Cipher No. 9 or 12); from Feb 1864 the entries to Grant's headquarters and from March 1864 nearly all
  entries use the vocabulary of Cipher No. 1: "unity / zebra / zodiac" = period, "yoke / youth / webster /
  walrus" = signature, "Growl / Grapes" = Washington, "Plank / Pebble / Harsh ..." = numerals, and the names
  Tomokiyo lists for No. 1 (Juno and five others = Grant, Lady and three others = Thomas, Bologna = the
  President, Galway = Richmond, Paradise = Colonel, Shelter = General). A marker-word count over the volunteer
  text shows No. 1 outnumbering the old vocabulary on every ten-page stretch from page 21 (March 1864) on.
- Book: mssEC 41 (object 351, 41 images), headed "No One Cipher" by hand, the corrections to the printed
  explanation that Tomokiyo describes for No. 1, holders list on page [B] (Stager, Eckert, Bruch, Smith,
  Fuller, Beckwith, HQ Cumberland, HQ Ohio, Mason). Confirmation on three entries before the campaign (rule of
  the brief): E3 (6 Mar, "for Jupiter Dolphin unity The Brutus directs me to say ... your com mission as Lieut
  Shelter is signed" = for Grant, Louisville. The Secretary of War directs me ... Lieut General), E5 (22 Apr,
  "Pension Waldo Spit here for Animal instead of Pebble whips" = 4,000 men here for Fort Monroe instead of 3
  regiments) and E19 (10 Dec, "harsh pension prolong panama spaffords ... Lexington" = 2,400 cavalry horses
  ... Lexington, printed so in OR I/45 pt 2 p.130). All three read cleanly at grade H.
- Not Cipher No. 1: the entries to S. H. Beckwith at Grant's headquarters (Culpeper, then City Point) and to
  S. P. Kimber with Canby (New Orleans, Vicksburg) use the same printed words with other meanings and a
  different punctuation set ("tulip", "pike", "yacht", "yawl", "yard", "star"); "For Crowd" to Grant in April
  (Crowd = Knoxville in No. 1), "For Mastiff" to Canby (Mastiff = Prentiss in No. 1). This is the separate
  headquarters cipher Tomokiyo discusses under "General Grant's special cipher" (Halleck to Grant, 22 Jan
  1864) or Cipher No. 2 (mssEC 47-48, "used at least in June 1864"). Those entries were dropped from the
  selection (four Beckwith, three Kimber, one Caldwell/Meade entry among the 29 candidates). Settled on
  20 Sept 2026: it is Cipher No. 2, and mssEC 47 reads them at grade H (section 8, key-no2.md, reading-no2.md).

## 3. The key (key.md)

mssEC 41 transcribed in full from the 2000 px images, 19 Sept 2026: TIME page (48 names), routes pages 1-8
(9 blind words, route, 20 line indicators each), arbitraries pages 9-24 (830 code words on 26-line pages),
numerals leaf (60 words), plus the corrected explanation, the "Directions for use" leaf and the loose Eckert-
Clowry letter of 10 July 1865. Two independent subagent passes per page set (eight agents), compared row by
row: 3 / 37 / 27 / 0 differing rows over the four sets (156 / 162 / 182 / 79 rows), nearly all formatting
(spaces in initials, ":" vs "." in times, "=" vs "-" in the inflection marks, the hand-added lines numbered
"27" by one pass and "extra" by the other). Substantive disagreements, settled by re-reading a crop:

- p.17 l.13 (334): A "J. O. Howard[?]", B "O. O. Howard"; the first initial is an open O. Taken "O. O. Howard".
- p.12 l.19 (329): A "Independence", B "Independance[?]"; the vowel is a closed loop. Taken "Independence".
- p.21 l.13 (338): A "Intercept", B "Itercept[?]"; the page has "Itercept" (no n). Recorded "Itercept [sic]".
- p.9 l.19 and p.18 l.6: both printed words blotted under the "Forts" and "Miscellaneous Words" headings; one
  pass called the line a heading, the other struck. Recorded as headings (no code word).
- p.21 l.17 (338): both passes "Inland"; the ledger uses Smyrna/Sidney for Roanoke Island (E4). Recorded
  "Inland [sic: Island]".
- Format-only: "(-ed, -ing)" for the book's "= Ed = ing"; ranks of "do" lines supplied from the line above.

Sister copy mssEC 43 (object 428) was opened for pages [12]-[19] (pointers 408-415) to look for the words the
ledger uses that mssEC 41 lacks. Its page [17] carries, in red ink, "Lavender = Gen C. C. Washburne =
Loadstone" at the head and "Maynard / Gen A. J. Smith / Macbeth" at the foot, and it updates several lines
(Leghorn/Legend = Canby where mssEC 41 has Hurlbut; Ireland/Italy = "Maj Gen H. W. Halleck" where mssEC 41 has
"General-in-Chief"; Kent/Kearney = Burbridge; Napier/Native = Stanley/Rosseau; Jordan struck for Jew, where
mssEC 41 strikes Jasper). Those four words are grade H from mssEC 43 (key.md section 7). A further subagent
sweep of mssEC 42, 45 and 46 for the remaining missing words (Mutton, Mackerel, Press, Praise, Submit, Hang,
Fisher) was started on 19 Sept 2026 and did not finish (section 6); those words stay at grade C from the
Official Records, and the sweep is the first job of the next worker on this target.

## 4. The twenty readings (ciphertext.txt, reading.md, decode.py)

Twenty entries of 5 March to 10 December 1864 on ten pages (16, 49, 58, 68, 78, 89, 142, 176, 213, 244),
chosen for a spread over the year and over the posts (Baltimore, Fort Monroe, Louisville, Nashville, Cedar
Creek and Monocacy, Cairo, St Louis, New Orleans line). Two independent transcription passes by subagents from
the 2583 px images, reconciled by the orchestrator against the image with the volunteer transcription as third
witness (reading.md, "Reconciliation": 41 disagreements, none affecting the sense, all resolved). A subagent
checked all 29 candidate entries against the Internet Archive full texts of 26 volume-parts of OR series I
(vols 32-34, 36-43, 45, 52; the list of identifiers and the grep commands were kept only in a scratch file,
or_check, that was not committed) by date and plain phrases: 16 of the 20 were matched to an OR print, and 4
were not matched by that sweep (E4 Fox to Butler 21 Apr; E5 Meigs to Butler 22 Apr; E6 Halleck to Sherman
26 Apr; E12 Lincoln to Wolford 4 Aug). **Corrected 20 Sept 2026 by the verifier session (AUDIT.md):** E6 is
printed in OR I/32 pt 3 p.498 and was missed by the sweep; E12 was printed in 1864 (a McClellan campaign
pamphlet), by Nicolay and Hay (1894) and by Basler, Collected Works vol 7 p.479; E4 and E5 were not found in
the OR, the Navy OR, Butler's Correspondence (1917) or Fox's Confidential Correspondence, but their substance
is in print (Butler's reply, OR I/33 p.279; Fox to Ericsson, ORN I/9 p.667) and most of their words stand in
clear on the Huntington page transcription published in 2018. Novelty classifications (CLAUDE.md rule 10):
E6 N1, E12 N1, E4 N4, E5 N4 (no prior decipherment located; N4 set 24 Sept 2026, AUDIT.md 'N4 set (LANE W2 worker E2)', after the Zooniverse Talk search came back negative; before that, N3). **Second audit (adversarial), 24 Sept 2026 (AUDIT.md):** E4 and E5 confirmed N3, not raised to N4 (JSTOR and HathiTrust full text still to run); OR I/36 pts 1-3, I/51 pt 1, III/4, the OR Supplement pt I, Fox's Confidential Correspondence, the Lincoln Papers and Google Books were added to the search, all negative. Both telegrams also survive in a second ledger copy, mssEC 25 p.77 (E4) and p.79 (E5), still in cipher in the volunteers' transcription; it reads "Buxton" for the M token "Brenton" (residual for a solver, not yet checked against the image). "Not printed" in the earlier text of this folder meant only "not matched by the
or_check sweep" and must not be read as "unpublished". Preference for unprinted entries could not be pushed
further within the budget: most unmatched candidates were the Beckwith and Kimber entries, which are in the
other cipher (section 2).

Result: all twenty read cleanly from the book; the seventeen OR-printed ones (the sixteen of the sweep and E6) agree with the OR word for word apart
from clerical slips and the times (the OR rounds or omits them; the ledger gives the half hour). Code-word
tokens over the twenty entries: H 298, C 8, M 0, I 0 (`python3 decode.py` prints the count; the C tokens are the rows
of key.md section 7 that appear in the entries (the addressee words Prss, Praise, Submit, Mackerel, Mutton; Hedge,
Nansy, mangled). `python3 decode.py --check` regenerates the readings from ciphertext.txt and key.md
and exits 1 if reading.md is stale. Per CLAUDE.md rule 4 this is an H reading: the meanings come from the key
source, and the OR is only the check.

No route transposition is recorded in this ledger (the entries are in reading order; the transposition was
applied on the wire), so the routes of key.md section 6 were not applied; they would be needed for the
received books.

## 5. Residue and what would move it

- The remaining 1864-65 entries of mssEC 19 (about 550) and mssEC 18 in Cipher No. 1 can now be read with
  decode.py by transcribing them; the vocabulary is complete but for the post-book additions (section 7 of
  key.md: the later copies mssEC 42-46 and the Friedman addenda of 9 Sept 1864 carry them).
- The Beckwith, Kimber and Caldwell entries (about 190 pages of mssEC 19 carry one or more, by the volunteer
  text) can now be read with decode_no2.py and key-no2.md (section 8); three are read.
- The Jan-Feb 1864 entries in the old vocabulary can be read with mssEC 67 (No. 9) or the No. 12 template.
- Not done: no negative was claimed, so no control was needed (rule 3).

## 6. Failure log

- 19 Sept 2026: pass A of the first five ledger pages was refused by the API safeguards on its first run and
  rerun with a one-line context sentence; no other agent was affected.
- 19 Sept 2026: the two book passes both read "Inland" for the meaning the ledger uses as "Island"; the hand's
  s and n are alike. Recorded as written with the sense noted.
- 19 Sept 2026: the OR volumes 36 pt 2 scans on the Internet Archive are badly OCR'd at p.587; the numerals of
  E7 come from the ledger, not the print.
- 19 Sept 2026: the mssEC 44 leaf "15½" (Tomokiyo's handwritten addenda) is a list of Georgia places for the
  Atlanta campaign, not the missing addressee words.
- 20 Sept 2026: on the blue leaf [25B] of mssEC 47 the copyist's Names column runs one line out against the
  Arbitraries column for rows 4-8 ("Page 32", a cross-reference, sits in the Names column); the ledger fixes
  Radical = officer and Repeat = order, and the four affected rows are graded C or I in key-no2.md, not H.
- 20 Sept 2026: one of the 37 book images fetched at 1200 px for the repo (pointer 575) arrived truncated and
  was refetched; the transcription used separate 1600 px and 2400 px copies and was not affected.
- 19-20 Sept 2026: the subagent sweeping mssEC 42, 45 and 46 for the addressee words mssEC 41 lacks was killed
  by the account's session rate limit after reaching mssEC 45, and wrote no output. Nothing was lost: the eight
  words concerned are graded C from the Official Records in key.md section 7, and the readings do not depend on
  the sweep. To redo it, give one worker the four copies' page pointers (mssEC 42: 359-382; 43: 397-420;
  45: 477-500; 46: 516-541 with the extra leaves 530-531) and the word list above.

## 7. Credits and sources

- Images and transcriptions: Thomas T. Eckert Papers, The Huntington Library, San Marino, California (mssEC 19,
  41, 43, 44, 47, 48); volunteer transcriptions of the ledger by Decoding the Civil War (2016-2017), NHPRC-funded,
  used as the third witness.
- Cipher identification, the No. 1 examples and the No. 2 example (Canby to Halleck, 19 June 1864, from Plum
  p.53): S. Tomokiyo, Cryptiana, "Union Codes and Ciphers during the Civil War" (civilwar1.htm, snapshot in
  sources/); W. R. Plum, The Military Telegraph during the Civil War
  (1882) as quoted there; Richard Bean's Milroy solve (2026) and D. Bourdeau, cyphersolver/milroy (MIT, CC BY
  4.0) for the route side of the Stager ciphers, consulted for the 1862 pilot on which this one builds.
- Known plaintext: The War of the Rebellion, ser. I, vols 32-45 (Internet Archive full texts); for E12 the 1864
  pamphlet, Nicolay and Hay and Basler cited in AUDIT.md.
- Novelty audit: AUDIT.md (verifier session, 20 Sept 2026; second audit and N4 decision 24 Sept 2026). E4 and E5
  are N4 (no prior decipherment located; AUDIT.md 'N4 set (LANE W2 worker E2)', 24 Sept 2026); nothing is at N5.
  Outside the repo, use only the safe sentences in that section. None may be called unpublished plaintext, and
  "first decipherment" is allowed only with the qualifier "no prior decipherment located".

## 8. The headquarters cipher is Cipher No. 2: mssEC 47 read on three Beckwith and Kimber entries (20 Sept 2026)

Outcome A of the brief of 20 Sept 2026. The Huntington's "Cipher Book #2" copies are mssEC 47 (object 596,
48 page images, catalogued "approximately 1866" from the loose 1866 sheets laid in) and mssEC 48 (object 636,
39 images). mssEC 47 was fetched in full by the IIIF route of the Access playbook (curl with a browser
User-Agent; manifest in images/manifest.json, the 37 written pages committed at 1200 px) and transcribed in one
pass by five subagents (1,482 rows: TIME page, eight route pages, sixteen arbitraries pages, the handwritten
pages 27-30, the blue leaves [25A]-[25C], the numerals page "26"), key-no2.md. Its holders' list is Eddy (HQ
Sherman), Fuller (New Orleans), Caldwell (HQ Army of the Potomac), Beckwith (HQ Grant), McCaine (HQ Sheridan);
mssEC 48's is Eckert (Washington), Beckwith (HQ Grant), Stager (Cleveland) and Bulkley (New Orleans), i.e. the
"two individuals" distribution of Halleck's letter to Grant of 22 Jan 1864 (Tomokiyo, "General Grant's Special
Cipher"), so the cipher Tomokiyo could not identify from the correspondence is in all likelihood this one.

The cheap check succeeded at once: page 13 gives Chart and Crowd = Lieut Gen U.S. Grant, page 18 Mastiff =
Canby, pages 23 and 25 Tulip, Yacht and Yardstick = Period, page 20 Pike = Comma, page 25 Yawl = Signed, and
Star = Infantry (page 22; the "star" of section 2 was a guess at punctuation and is a noun). Tomokiyo's own
worked example of Cipher No. 2 is a Kimber telegram from New Orleans containing tulip, yacht and mastiff.

Test on three entries printed in the Official Records (ciphertext-no2.txt, reading-no2.md, `python3
decode_no2.py --check`): Halleck to Grant 16 Apr 1864 11 AM (OR I/34 pt 3 p.169), Halleck to Grant 29 Apr 1864
2.15 PM (OR I/34 pt 3 p.331) and Halleck to Canby 6 June 1864 12.30 PM (OR I/34 pt 4 p.240), transcribed from
the 2583 px page images with the volunteer text as second witness. All three read word for word against the
print; code-word tokens H 111, C 4, I 4, M 1. The C and I tokens are the clerk's "Yard" for Yardstick, "whim"
(telegram, not in the book), "reswindling" (re + Swindle = move) and the two words of the misaligned blue-leaf
rows (section 6 above). Differences from the print: the ledger sends "2,000 cavalry" where the OR prints 5,000
(16 Apr), and the OR rounds the time of 29 Apr to 2.30 p.m. (the ledger's own time word says 2.30 PM and its
header 2.15 PM). Per rule 4 this is an H reading; per rule 10 nothing is said here about novelty: the three
telegrams are printed in the Official Records, which is what made them usable as the control.

What this opens: the Beckwith, Kimber and Caldwell entries of mssEC 19 (the volunteer text names one of the
three operators on about 190 of the 403 transcribed pages, from 15 Feb 1864 to 1865) can now be read with
decode_no2.py by transcribing them, as the No. 1 entries can with decode.py. The route pages of mssEC 47 (a
handwritten figure before each blind word, as Tomokiyo noted) would be needed for the received books mssEC 09-
13, where the transposed text may be recorded. mssEC 48 was not transcribed; its tables should be the same
cipher and could settle the [25B] alignment and the "[?]" readings of key-no2.md. Not done: a second
transcription pass of mssEC 47 (the three readings against the print are the only control on the 1,482 rows),
and the seven other Beckwith/Kimber/Caldwell candidates of the 19 Sept selection.


## 9. Enquiry to the holding library (20 Sept 2026)

An email was sent on 20 Sept 2026 to the Huntington curator who ran Decoding the Civil War, describing the
mssEC 19 / mssEC 41 pilot (twenty entries, a machine-readable cipher book, a decoder, readings checked
against the Official Records) and asking whether a corpus-level dataset mapping the coded telegrams to
cipher, key, plaintext and provenance was ever completed internally or since; if not, whether building one
systematically would be useful. The repository was offered. A reply from the archive is the only route to
N5 for anything in this folder and is the decision point for the corpus pass (section 5, AUDIT.md section 12).
Log the reply here by date; no personal data (rule 9).
Follow-up sent by the person 6 Oct 2026 (outreach/huntington-eckert-followup-2026-10.md), a reply in the 24 Sept thread to Huntington reference: progress counts, the dataset question again, and whether an 1865 cipher book survives. Reply pending.

## Second reader E4/E5, 24 Sept 2026

Blind second reading (LANE V worker, 24 Sept 2026): the E4 and E5 entries were read word by word from the page images
before ciphertext.txt, reading.md or AUDIT.md sections 5-6 were opened. Witnesses: mssEC 19 p.49 (pointer 8941,
the working ledger, on disk) and the second ledger copy the adversarial audit found, mssEC 25 p.77 (pointer 5621, E4)
and p.79 (pointer 5623, E5). Both were fetched once at full size (5941 x 7200 px) through the Huntington IIIF
server and read at that size; they are committed at 2971 px as images/mssEC25_p5621.jpg and _p5623.jpg to keep
the folder under 30 MB (images/manifest.json has the full-size URLs). The word-by-word blind reading of all four
entry-witness pairs is images/secondreader-E4E5.tsv (248 rows). The volunteers' transcription (Decoding the Civil
War, CONTENTdm "text" field of item 8941) was fetched once after the blind reading, for the comparison only.

The mssEC 25 copy is a fair copy in a different, clearer hand, with the ledger's commas dropped and a column grid.
Where it departs from mssEC 19 on plain words (Knots, make, Cleared, bare, &, ass, Fawks, fie) the mssEC 19 image
does not support it; those are copyist variants and are not proposed. Where mssEC 19 is ambiguous and mssEC 25 is
clear on a key word, the clear copy settles it.

**Agreement.** My mssEC 19 reading against ciphertext.txt, case-insensitive, doubt marks ignored: E4 62/64, E5
57/60, together 119/124 (96.0%). Of my five disagreements, re-inspection shows two were my errors (E5 "Animals":
the final stroke is the clerk's l, so "Animal"; E4 "Hon": the volunteers and mssEC 25 read "how", the ledger's
last letter is compatible with w), one is a genuine R/B ambiguity (E4 "Radin"/"Baden", key word, "Baden" kept),
one a P/B ambiguity (E5 "Pender"/"Bender", key word, "Bender" kept), and one a real correction (E5 "Spartans").

**Every word where a witness differs from ciphertext.txt** (index = word position in the entry, comma-free):

| tel | # | ciphertext.txt | my mssEC 19 | mssEC 25 | volunteers | image evidence | proposal |
|---|---|---|---|---|---|---|---|
| E4 | 3 | Knox | Knox (m) | Knots | Knox | EC19: K-n-o + an open double loop, no t or s; EC25 clear "Knots" | keep Knox (key: Knox = Maj Gen B. F. Butler); EC25 is a copyist's slip |
| E4 | 27 | made | made (m) | make | made | EC19 ending de/ke indistinct | keep (plain word) |
| E4 | 37 | Clad | clad | Cleared | claid | EC19 "clad" | keep |
| E4 | 43 | Bar | bar | bare | bar | EC19 no final e | keep |
| E4 | 49 | and | and | & | and | EC19 written out | keep |
| E4 | 52 | Navy | Navy (m) | waxy | Waxy | EC19 at 3x: the capital is an I-stroke with a V joined to it, the W form this clerk uses, then a-x-y; EC25 lowercase w-form; volunteers "Waxy" | **change Navy -> Waxy** (key p.23 l.22 R: Waxy = South, H); reading becomes "protect all South of Roanoke Island" |
| E4 | 54 | Baden | Radin (m) | Badin | Baden | EC19 capital R/B ambiguous; EC25 B | keep Baden (key: Roanoke) |
| E4 | 57 | Asst | asst | ass | Asst | EC19 raised t | keep |
| E4 | 58 | Brenton[?] | Brenton (l) | Buxton | Brenton | EC19 at 3x: B, u, a crossed x-form, t whose cross-stroke is the long line running right of the word, o, n = "Buxton"; EC25 clear u and x, "Buxton" | **change Brenton[?] -> Buxton** (key p.10 l.21 R: Buxton = Secretary of Navy, H); the tail reads "Asst [Secretary of Navy] Fox", which the key now supplies instead of the M gloss |
| E4 | 59 | Fox | Fox | Fawks | Fox | EC19 "Fox" | keep (plain: Fox) |
| E4 | 60 | How | Hon (m) | how | How | EC19 last letter compatible with w | keep |
| E4 | 61 | are | are | fie | are | EC19 "are" | keep |
| E5 | 7 | Dispatch | Dispatch | dispatch | Despatch | EC19 i, not e | keep |
| E5 | 22 | Animal | Animals (m) | animal | Animal | EC19 at 3x: final stroke is the clerk's l, no s | keep Animal (my blind reading was wrong) |
| E5 | 46 | Spartan | Spartans | Spartans | Spartans | final s clear in both ledgers | **change Spartan -> Spartans** (Spartan = Horse; reading "Horses", the book's stem-plus-ending rule) |
| E5 | 51 | queenly[?] | Queenly (m) | queenly | queenly | EC25 clear "queenly"; EC19 compatible | **change queenly[?] -> queenly** (drop doubt mark; key: Queenly = Depot, H) |
| E5 | 60 | Bender | Pender (m) | Bender | Bender | EC19 capital P/B ambiguous; EC25 B | keep Bender (key: Qr Master Genl U.S.) |

Known cases from the brief: Brenton[?]/Buxton -> Buxton (proposed); Knox/Knots -> Knox (kept); Spartan/Spartans ->
Spartans (proposed); waxy/Navy -> Waxy (proposed). Also proposed: queenly without the doubt mark. **Four proposed
changes**, none applied here; a Sonnet worker applies the accepted ones to ciphertext.txt and reading.md and reruns
`decode.py --check`. Grade effect if accepted: E4 M 1 -> 0 (Buxton H), "Navy" moves from plain to a code word (H).

**Applied, 24 Sept 2026** (Sonnet apply worker): all four proposed rows applied to ciphertext.txt; `decode.py --write`
regenerated reading.md; `decode.py --check` exits 0. Old and new plaintext:
- E4 tail: `Asst Brenton[?] Fox` -> `Asst Buxton Fox`; reading `[(Assistant) Secretary of the Navy, the tail "Asst
  Brenton Fox" = Asst. Sec. G. V. Fox][?]` (M) -> `[Secretary of Navy]` (H).
- E4 body: `Navy` -> `Waxy`; reading `Navy` (plain, ungraded -- the key's Navy row is a blind word, skipped inside
  an untransposed entry) -> `[South]` (H).
- E5 body: `Spartan` -> `Spartans`; reading `[Horse]` -> `[Horse]'s` (same H row, meaning unchanged, ending now read).
- E5 body: `queenly[?]` -> `queenly`; reading `[Depot][?]` -> `[Depot]` (same H row, doubt mark dropped).

Grade counts, updated: E4 H 9, M 1 -> H 11, M 0. E5 unchanged (H 20; the Spartans/queenly changes do not move a
grade). Whole-file totals (decode.py): H 296, C 8, M 1, I 0 -> H 298, C 8, M 0, I 0.

Observation, no change proposed: E5's ledger header reads "10.45 am" (both copies, and the volunteers "1045 AM"),
while the time word Elizabeth reads 10.30 AM; the reading's {time: 10.30 AM} is the key's value, not the header's.

Suggestion (not done, outside this brief): the mssEC 25 fair copies exist for other entries on pp.77-79 (E4's
neighbours, e.g. the Beckwith/Culpeper entry); a second-witness pass over every E-entry that has an mssEC 25 copy
would settle the remaining [?] tokens the same way.

Requests: hdl.huntington.org 5 (2 info.json, 2 full-size IIIF images, 1 CONTENTdm item API for the volunteers'
text), 3 s apart, all HTTP 200.

Suggestion for ASKS.md row 17 (JSTOR, not added there directly, per brief): add these E4/E5 queries to the row's
list if a person or a working JSTOR login runs it: `"Fox" AND "Butler" AND "Ericsson" AND camels AND 1864`;
`"Tecumseh" AND "camels" AND Hatteras`; `Meigs AND Butler AND "cavalry depot" AND 1864`; `"Army of the James" AND
Butler AND telegram AND April 1864`; `Eckert AND "Military Telegraph" AND cipher` (AUDIT.md "Toward N4, 24 Sept
2026 (gap worker)" section 4).

## Web and blog check (GF4-BATCH20 (account-4), 3 Oct 2026)

Scope: an intake-gate fix only; this section adds to AUDIT.md's source-family log (rows 1-10, 20 and 24 Sept 2026) and changes no class there (E4 and E5 stand at the classes AUDIT.md gives them; E6 and E12 at N1).
Plain web searches (WebSearch, 3 Oct 2026): (1) `Eckert telegraph ledger Huntington "Cipher No. 1" decoded Fox Butler April 1864` -- Huntington collection and Digital Library pages (Cipher Book #1 p.[22]), the OAC finding aid, Verso posts, the project blog's "ciphers" tag; nothing on E4 or any ledger p.49 entry; (2) `"Decoding the Civil War" Eckert ledger decoded telegrams Meigs Butler 1864 cipher solved` -- NHPRC report, Zooniverse project page, the project blog's "Telegram in Focus" category; nothing on E5; (3) `Union Army telegraph cipher ledger decoded AI 2026 Huntington Eckert` -- 2016 press (Slate, Smithsonian, InsideHook); no 2026 decoding announcement for the ledgers.
Blog site searches: Cipherbrain (`?s=Eckert`): 2 posts -- "Tausende von verschlüsselten Telegrammen aus dem Sezessionskrieg warten auf ihre Entschlüsselung" (22 Jun 2016) and "A Cryptologic Travel Guide" (27 Aug 2014); the 2016 post and its 2 comments (Olivia von Westernhagen, 22 Jun 2016; Bernhard Gruber, 23 Jun 2016) were read: project announcement only, no decipherment of any entry; klausschmeh.net "Solved cryptogram" category (4 posts, 21 Sept-1 Oct 2026): none about Civil War telegrams; Cryptiana blog (`search?q=Eckert`): no posts (Tomokiyo's on-disk page `sources/cryptiana/web/civilwar1.htm` is already cited in section 1); Cipher Mysteries (`?s=Civil War telegram`): Nothing Found. The project's own blog (decodingthecivilwar.wordpress.com) was read for this item on 20 Sept 2026 (section 1, "Now, Jesse", the p.[47] entry); not re-read this pass.
Model-solve and new-publication check: Apeiron (apeiron.re front page: no listing of solved items is served; nothing on this item); Cabinet Noir (github.com/el-descifrador/cabinet-noir, HEAD 47b6db9, 2 Oct 2026) grepped for `eckert`, `1864`: no hit; neither solver repository has an Eckert item (sources/solver-diffs/2026-10-03-bourdeau.tsv and 2026-10-03-aymeloglu.tsv carry no eckert row).
Result: no decipherment or plaintext of the twenty read entries beyond what AUDIT.md already records was located by these queries on 3 Oct 2026 (a search result, not a novelty verdict, rule 10; AUDIT.md stays the only place a class is set).
Requests: WebSearch 3, scienceblogs.de 2, cryptiana.blogspot.com 1, ciphermysteries.com 1, klausschmeh.net and apeiron.re shared with sp53-22-f52; all >=1.5 s apart.

## Premise check (GF4-BATCH20 (account-4), 3 Oct 2026)

(a) Folder's own mentions: **found, already handled** -- the project blog's "Now, Jesse" (26 Jun 2017) read the p.[47] entry with the sister book mssEC 44 (section 1 correction); E6 and E12 were found in print by the verifier (AUDIT.md sections 7-8, N1). Nothing further mentioned in NOTES.md, AUDIT.md or `second-opinions/` is an unopened decipherment.
(b) Other solvers' working files: **not found** -- neither Bourdeau's nor Aymeloglu's repository has an Eckert item (3 Oct 2026 diffs); the Zooniverse project's decoding phase was never launched (AUDIT.md section 12).
(c) Physical neighbours: **partly read** -- the facing and neighbouring ledger pages are on the Huntington item pages the readings came from; the parallel sent ledger mssEC 18 (object 10074) has not been opened (section 2) and could hold a second copy of E4/E5 with the code words resolved; the sister cipher books mssEC 43/44 were opened for named pages only.
(d) Recipient's side: **found, already logged** -- Butler's printed correspondence and OR vol 33 (the recipient's side for E4/E5) were read by the verifiers (AUDIT.md sections 5-6 and the 24 Sept second audit); the Meigs Papers and NARA RG 92/107 by finding aid (AUDIT.md "Toward N4").
Verdict: no premise failure; status `partial` and every AUDIT.md class unchanged.

## While waiting

The one action that depends on nobody: open mssEC 18 (object 10074) at 21-22 Apr 1864 on the Huntington CONTENTdm API (`dmQuery` with the `CISOSEARCHALL` clause, Access playbook item 1) and check whether its copies of E4 and E5 resolve any of the unread code words; script and one page read, about USD 1-2.

Gate after this pass (3 Oct 2026, GF4-BATCH20): `python3 tools/intake_gate_check.py eckert-1864`
```
eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within 6 lines
exit 0
```
`python3 tools/next_steps.py --wait-only | grep eckert-1864`: no line.

## Local runner (PR-LAND-67, 5 Oct 2026)

- 5 Oct 2026 (PR-LAND-67): LOCAL-QUEUE L4 answer landed, local-runner/L4-2026-10-05.md -- blocked: HathiTrust Cloudflare check, no E4/E5 phrase query sent, no absence claimed. Row blocked; owner desk ASKS 141.

## Remaining gaps (GAPSFIX, 4 Oct 2026)
Read so far: 20 of about 570 Cipher No. 1 entries of mssEC 19 read (section 4: H 298, C 8, M 0, I 0 code-word tokens, `decode.py --check` exit 0) plus 11 Beckwith/Kimber/Caldwell entries in Cipher No. 2 (section 8 and DEF1-ECK64, 5 Oct 2026: H 273, C 6, I 10, M 1, `decode_no2.py --check` exit 0); the rest of the ledger untranscribed.
- corpus pass over the remaining ~550 mssEC 19 entries and mssEC 18 - blocker: waiting-on the Huntington curator's reply to the 20 Sept 2026 enquiry; section 9 names that reply as the decision point for the corpus pass
- old-vocabulary entries of mssEC 19 not yet image-checked - blocker: not-attempted; 33 entries read (22 image-checked: O9-A..V by R7A/R7B/R8/R9-ECK64; 11 from the volunteer text only: O9-W..AG of pages 26-61 by R9-ECK64B 6 Oct 2026, H 93, M 0, all thirty-three H 286, decode_no9.py --check exit 0; no old-vocabulary entry on pp.62-72, which switch to Cipher No. 1/2 marks from 1 May 1864); next: image-check O9-W..AG on the page images (pointers 8918, 8933, 8936-8940, 8942, 8946, 8953; crops via tools/iiif_lines.py, one blind read per page batch, the R8/R9-ECK64 method), ~$4

## Escalation (GAPSFIX, 4 Oct 2026)
- [ ] siblings: mssEC 25 second copy read for E4/E5 (Second reader, 24 Sept 2026; four corrections applied); mssEC 18 opened 5 Oct 2026, pp.50-60 text, no E4/E5 copy
- [x] clear-pages: OR prints matched for 17 of 20 entries as the check (section 4)
- [x] known-keys: Cipher No. 1 (mssEC 41) and Cipher No. 2 (mssEC 47) are the period key books in use
- [x] print: OR series I sweep, ORN, Butler and Fox correspondence, Lincoln Collected Works (section 4, AUDIT.md)
- [n/a] key-rebuild: period cipher books exist and read every code word in the twenty entries; for the Jan-Feb 1864 old vocabulary the period book is mssEC 67 (filled-in, Tomokiyo's No. 9), read on 9 pages for the sample (R7A-ECK64, 6 Oct 2026) and on pp.[9]-[24] for the further entries (R7B-ECK64B, 6 Oct 2026)
- [x] image-check: E4/E5 re-read word by word at full size against both ledgers (Second reader, 24 Sept 2026); N2-E Spit re-read in mssEC 47, mssEC 48 and the ledger (D2-ECK64S, 5 Oct 2026: Spit = Near in both books, ledger Spit; conflict logged, not resolved); O9-E..Q checked against the mssEC 19 page images (R8-ECK64, 6 Oct 2026, image-check-no9.tsv); O9-R..V likewise (R9-ECK64, 6 Oct 2026); O9-W..AG not yet (R9-ECK64B, 6 Oct 2026, volunteer text only)
- [n/a] retry: M 0 in the twenty read entries, no doubtful token left to retry
Verdict: keep going: 1 internal gap; cheapest next: image-check the eleven O9-W..AG entries of pages 26-61 against the mssEC 19 page images, ~$4 (updated R9-ECK64B, 6 Oct 2026: pages 21-72 scanned for every form of the operator's "9" mark and for old-vocabulary words; eleven more entries read with key-no9.md, H 93, M 0, decode_no9.py --check exit 0; O9-Y and O9-AE matched in the OR, O9-U/V not in I/35 pt 2 or III/4). Earlier: keep going: 1 internal gap; cheapest next: scan mssEC 19 pages 61 onward (and the unmarked entries of pages 21-60) for further old-vocabulary entries, read them with key-no9.md, and search O9-U/O9-V in OR I/35 pt 2 and ser. III vol. 4, ~$3 (updated R9-ECK64, 6 Oct 2026: the five "(9)" entries of pages 21-60 read and image-checked, H 45, M 0, decode_no9.py --check exit 0). Earlier: keep going: 1 internal gap; cheapest next: the "(9)"-marked Jan-Mar 1864 entries past page 20 of mssEC 19 read from the page images with key-no9.md, ~$4 (updated R8-ECK64, 6 Oct 2026: O9-E..Q image-checked, one code-word change, H 148, M 0, decode_no9.py --check exit 0). Earlier: keep going: 1 internal gap; cheapest next: image-check the thirteen O9-E..Q entries (volunteer text only so far) and continue the "(9)"-marked entries past page 20 of mssEC 19, ~$4 (updated R7B-ECK64B, 6 Oct 2026: 17 old-vocabulary entries read with mssEC 67, H 147, decode_no9.py --check exit 0). Earlier: keep going: 1 internal gap; cheapest next: the rest of the Jan-Feb 1864 old-vocabulary entries (pages 1-20 of mssEC 19, with key-no9.md extended from mssEC 67 pp.[11]-[15], [18]), ~$4 (updated R7A-ECK64, 6 Oct 2026: four-entry sample read with mssEC 67, decode_no9.py --check exit 0). Earlier note: (updated D2-ECK64S, 5 Oct 2026: the Spit/men conflict was re-read at full size in both key books and the ledger and is logged as a data conflict in its own section below)

## mssEC 18 check for E4/E5 copies, 5 Oct 2026 (RUN6-ECK, LANE-RUN6 wave 2)

Route: Huntington CONTENTdm item API, `hdl.huntington.org/digital/api/collections/p16003coll11/items/<pointer>/false` (plain curl, browser UA, 1.6-3 s apart, 21 requests, one 'Empty reply' retried once). mssEC 18 = object 10074 (record `sources/mssEC18_obj10074.json`: title "Front_cover", compound object; its pages are separate pointers, page n = pointer - 9660 in this stretch). Dating probe: 9710 = p.50 (20 Apr 1864), 9714-9716 (21 Apr), 9717 (22 Apr), 9718 (23 Apr), 9720 (23 Apr), 9740 (19 May). Pages 9710-9720 (pp.50-60) saved as volunteers' text in `sources/mssEC18/p<pointer>.json`; no images fetched (the NOTES next step named a text/page read only).
Found: mssEC 18 holds a different set of 21-22 Apr entries from mssEC 19 p.49 and mssEC 25 pp.77-79: Beckwith/Sheldon/Cutler/Benham/Meigs entries and a Horner NY 21 Apr 9.40 PM telegram "for Vulcan John Ericsson ... camels made to lift the Tecumseh" (p.56, pointer 9716, volunteers' text; appears in clear words, signed "Annal nine fifty"). Meigs 22 Apr 10 PM to Van Vliet (p.57, pointer 9717) is not E5 (E5 = Meigs/Bender to Butler, 22 Apr 10.45 AM).
Not found: no entry to Butler at Fort Monroe, no Fox signature entry at 9.30 PM, and no 4,000-men/1,000-horses Meigs entry in the volunteer text of pointers 9710-9720 (searched Butler, Monroe, Roanoke, Bender, camels, 4000 by script). So no second copy of E4 or E5 in mssEC 18 was located; this is conditional on the volunteers' transcription (rule 2) and on 11 pages only (21-23 Apr), not a verdict on the image, and pp.52-53 (9712-9713) carry no date line in the transcription. No code word of key.md changes; no grade moves. Related, not a copy: the Ericsson/Tecumseh telegram is the Fox-Ericsson subject of E4's clear counterpart (ORN I/9 p.667 per section 1), a witness for context only; not graded, no novelty language.
Next (not done): look at images of pp.52-53 if a person wants the undated pages checked; otherwise this gap is closed as "no copy located in 21-23 Apr text".

## Cipher No. 2: the eight further entries, 5 Oct 2026 (DEF1-ECK64, LANE DEFAULT-account-1-20261005-2039)

Brief: section 8 "Not done", the remaining Beckwith/Kimber/Caldwell entries of the 19 Sept selection. The 29-candidate
list itself was never committed (section 4, or_check scratch), so the entries were re-found: the volunteer text of the
ten selection pages (Huntington CONTENTdm item API, 11 requests incl. one 502 retried once and p.90 to check a run-on)
names exactly four Beckwith, three Kimber and one Caldwell entry, the count section 2 gives; section 8's "seven" was
eight. They are N2-D (p.49, 21 Apr), N2-E and N2-F (p.58, 25 and 27 Apr), N2-G (p.68, 12 May), N2-H (p.78, 24 May),
N2-I and N2-J (p.89, 7 and 8 June), N2-K (p.176, 10 Sept 1864). Another Kimber entry (Vicksburg, 11 June 1864) opens
p.90 (pointer 8982); not read here.

Crop step (mandatory, as run; S = the worker's scratch folder, crops not committed, regenerable from the committed
images): `python3 tools/iiif_lines.py --image ciphers/eckert-1864/images/mssEC19_p<pointer>.jpg --out $S --prefix K<n>
--region 120,<y0>,2400,<h> --centres 50,154,... (104 px pitch) --lines-per-crop 3 --max-width 2400`, regions K1 8941
300-1200, K2 8950 100-1180, K3 8950 1880-2600, K4 8960 1880-3020, K5 8970 1130-1950, K6 8981 130-680, K7 8981
680-2080, K8 9070 1480-2020, plus nine 320 px repair strips for lines the regions clipped. Automatic line detection
failed on these ruled pages (0-6 lines found), hence `--centres`. Passes: A and B, two Sonnet calls each (4 entries per
call), blind to each other and to the volunteer text; reconciliation by the worker against the strips with the
volunteer text as third witness. Main settlements: Crowd (A "Gowd"), Nutmeg (both passes "Antwerp"; strip and
volunteer Nutmeg), Pekin (B "Tekin"/A "Sekin"), lessees (A "losses"), "talbot" in N2-I/N2-K is not struck (a long
t-cross; talbot = of the, and the OR has "of the" in N2-K). N2-K's header line is the volunteer text's only.

Result (`python3 decode_no2.py`, `--check` exit 0; reading-no2.md "The eight further entries"): code-word tokens
over the eight H 162, C 2, I 6, M 0; four of the H tokens sit on a doubtful page word (Benton[?], pagan[?], Lamb[?],
Quivered[?]). Five of the eight are printed in the OR and agree word for word apart from the clerk's slips: N2-E I/33
p.982, N2-G I/34 pt 3 p.554, N2-H I/36 pt 3 p.145, N2-J I/34 pt 4 p.265, N2-K I/41 pt 3 p.132-133 (IA djvu full texts,
5 downloads; pages from OCR running heads). N2-D (Secretary of War to Grant, 21 Apr, troop list "making in all 2800"),
N2-F (Augur to Sheridan, 27 Apr, 8th Illinois Cavalry) and N2-I (to Dana, 7 June, Colonel Seward of the 9th NY Heavy
Artillery reported missing) were not located in the OR volume searched for each (I/33; I/33; I/36 pt 3) by the phrases
listed in reading-no2.md -- a search result only, other volumes and editions not searched; no novelty is claimed
(rule 10). One data conflict: N2-E "Clarke Dwight Spit" decodes "6000 Near" with the book's Spit = Near, the OR prints
"6,000 men"; logged in Remaining gaps, the key row is not changed. A be-api full-text phrase search (8 requests, one
503, not retried) gave no further hits. Requests: hdl.huntington.org 11, archive.org 5, be-api.us.archive.org 8.

## Spit/men in N2-E: both key books and the ledger re-read, 5 Oct 2026 (D2-ECK64S, LANE DEFAULT-account-1-20261005-2217)

Intake gate (`python3 tools/intake_gate_check.py eckert-1864`, 23:19 UTC): `eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`, exit 0.

Crop step, as run (scratch, not committed; regenerable): Huntington IIIF regions at native resolution, `.../p16003coll11/580/1700,5500,3000,900/1500,/0/default.jpg` (mssEC 47 p.22 l.26) and `.../626/2200,5550,2700,500/1500,/0/default.jpg` (mssEC 48 p.22 l.26; mssEC 48 = object 636, page 22 = pointer 626, from `dmGetCompoundObjectInfo/p16003coll11/636`), plus the whole mssEC 48 p.22 at 1000 px to check the row order; ledger line from the committed image, `python3 tools/iiif_lines.py --image ciphers/eckert-1864/images/mssEC19_p8950.jpg --out $S/k2 --prefix E --region 120,100,2400,1080 --centres 50,154,...,986 --lines-per-crop 2 --max-width 2400` (crop E_L04). Read by the worker directly, one eye; no subagent.

Witnesses:
- mssEC 47 (Cipher Book #2, holders Eddy, Fuller, Caldwell, Beckwith, McCaine) p.22 l.26 right column: handwritten "Near", printed code word "Spit". Unambiguous at native size.
- mssEC 48 (sister copy, holders Eckert, Beckwith, Stager, Bulkley) p.22 l.26 right column: handwritten "Near", printed "Spit". The whole page matches mssEC 47's rows as transcribed in key-no2.md (Summer = Men at l.20 L in both; Spoon = North, Spit = Near at l.26).
- mssEC 19 p.58 (pointer 8950), N2-E, line 5: "Caldwell or Clarke Dwight Spit from Bedford to Jaunt &" -- the sender's code word is clearly Spit, not Summer or another Men word.
- OR I/33 p.982 (Halleck to Grant, Washington, 26 Apr 1864, 2 p.m.): "5,000 or 6,000 men" (as recorded by DEF1-ECK64; not re-fetched here).

Result: not a transcription error on our side and not a difference between the two key books. Both period key books give Spit = Near; the ledger's code word is Spit; the printed clear text has "men". The likeliest account is a slip by the encoding clerk in Washington (Men's own code words Summer, p.22 l.20 L, sits six rows above on the same page) that the receiving operator corrected from sense, but nothing in the four witnesses shows that, so it is not asserted. Rule 4: logged as a data conflict with its witnesses, not settled by majority; key-no2.md's row Spit = Near stays H (both books), and the N2-E token stays as the key reads it ("Near"), with the print's "men" recorded beside it in reading-no2.md. No grade count changes; `python3 decode_no2.py --check` exit 0 after this edit. What would settle it: the received copy at Grant's headquarters (Beckwith's received book or deciphered copy), if one survives; not searched here.

Requests: hdl.huntington.org 5 (2 IIIF regions, 1 info.json, 1 page at 1000 px, 1 compound-object info), all 200.

## Jan-Feb 1864 old vocabulary: four entries read with mssEC 67, 6 Oct 2026 (R7A-ECK64, LANE LANE-RUN7-account-1)

Step checked undone first: no dated section had read a Jan-Feb 1864 entry (sections 2 and 5 name the vocabulary only).
Kept as found: the Spit/men data conflict of N2-E (D2-ECK64S section above) stays logged, unchanged.

Route: Huntington CONTENTdm item API (`hdl.huntington.org/digital/api/collections/p16003coll11/items/<pointer>/false`,
field "text") for mssEC 19 pages 1-15 (pointers 8893-8907, the volunteers' text, scratch, not committed); IIIF images of
mssEC 67 (object 1750) pages 1720 (TIME), 1731-1733, 1743 at 1000 px and 1737-1741 at 1400 px, plus the committed
ciphers/eckert-1862/images/mssEC67_p1736/p1742/p1744.jpg; ledger pages 3-4 (8895, 8896) at 1500 px for the image check.
Read by the worker directly, one eye; no subagent call, so no crop step was needed (CLAUDE.md Usage 6 applies to subagent
transcription calls). OR check: warofrebellion322unit and warofrebellion33unit `_djvu.txt` from archive.org.

Found: mssEC 67's handwritten meanings are the Jan-Feb 1864 War Department vocabulary. Four entries of 30 Jan and 1 Feb 1864
on ledger pages 3-4 (Halleck to Thomas; to Lockwood; to Kelley and Sullivan; to Chesebrough) were transcribed from the
volunteer text and checked against the page images (no code-word disagreement) into ciphertext-no9.txt, and read by
key-no9.md (the whole TIME page and 29 arbitrary lines, each with page, line and pointer) through decode_no9.py (decode.py's
machinery, file names changed). Code-word tokens: H 33, C 0, I 0, M 1 (Pagan, the place-of-origin word, not on the pages
read). `python3 decode_no9.py --check` exit 0. Rule 4: H, read from a period key book; the OR is the check, not the source.
Every one of the four is printed in OR series I (I/32 pt 2 p.263; I/33 pp.488, 488, 489) and agrees with the print in every
coded word, the times included (Catharine 11.30 AM, Florence 10 AM as printed; Harriet 1 PM against 1.15), with one data
conflict: "Village K Garrard" reads Major by the book, the print has Brig. Gen. (reading-no9.md; logged, not settled; the
token stays H as the book reads it). Examples of the vocabulary the print confirms: Blubber = W. S. Sherman, Quotient = Joe
Johnston, Lonesome = Mobile, Java = Corinth, Relay = Cavalry (also "Relay Bureau" = Cavalry Bureau), Shylock/Stanhope =
Regiment, Seymour = Infantry, Robin = Battery, Soap/Somers = Rail Road, Valley/Vermont = Brig. Gen., Vernon/Vermin = Maj. Gen.

Not found / not done: pages [1]-[9] (routes, cabinet), [11]-[15] and [18] of mssEC 67 not read, so Pagan, Pagoda, Castor,
Cuba, Cadmus, Hammer and Audit (in other Jan-Feb entries) have no row yet; the other ~30 Jan-Feb entries not transcribed.
No novelty question arises: all four are printed (no claim made; rule 10 is a verifier's). Key source per rule 10's key
field: period (mssEC 67). One more observation for the next worker, not a reading: entry 2 of page 5 (2 Feb, to Lockwood)
and page 5's Garrett entry use Vernon/Vermin (Maj. Gen.) for Lockwood and Kelley where page 3-4 use Valley/Vermont (Brig.
Gen.), from the volunteer text only; check on the image before reading them.

Requests: hdl.huntington.org 26 (15 item-API pages, 9 mssEC 67 IIIF pages, 2 ledger IIIF pages), archive.org 2; all 200.

## Jan-Mar 1864 old vocabulary: thirteen more entries of pages 1-20, 6 Oct 2026 (R7B-ECK64B, LANE LANE-RUN7-account-1)

Step checked undone first: R7A-ECK64 (section above) read four entries and named pages 1-20 and mssEC 67 pp.[11]-[15], [18]
as the next step. Kept as found: the Spit/men (N2-E) and Village/Garrard (O9-A) data conflicts stay logged, unchanged.

Route: Huntington CONTENTdm item API (`hdl.huntington.org/digital/api/collections/p16003coll11/items/<pointer>/false`, field
"text") for mssEC 19 pages 1-20 (pointers 8893-8912; scratch); mssEC 67 IIIF pages at 1400 px, pointers 1731-1735,
1737-1739, 1741, 1743 (scratch, regenerable), plus the committed ciphers/eckert-1862/images/mssEC67_p1729/p1730/p1736/p1744.jpg.
Read by the worker, one eye, no subagent call (so no crop step). OR check: warofrebellion33unit, 322unit and 342unit
`_djvu.txt` from archive.org, phrase grep by script.

Found: key-no9.md section 3 adds 38 rows (H, each with page and line): among them Pagan/Pagoda = Washington (the place-of-
origin word, so R7A's one M token is now H), Abbey/Audit = B. F. Butler, Bangor/Bengal = Grant, Alias/Amen = Banks,
Atlas/Annal = G. V. Fox, Anthon/America = Sec. of the Navy, Alps/Amber = P. H. Watson, Merlin/Midas = New York,
Maroon/Mellow = Philadelphia, Neptune/Negus = Richmond, Hammock/Hammer = (Fort) Monroe, Hosanna/Husband = (Fort) La Fayette,
Walpole/Walnut = Army, Yancey/Yacht = Hd. Qrs., Wadding/Waggish = Arrest. Thirteen further entries of pages 1-20
(O9-E..O9-Q in ciphertext-no9.txt: every page 1-20 entry outside Ciphers No. 1 and No. 2 whose words read in mssEC 67)
decode with H 113, M 0; the seventeen together H 147, C 0, I 0, M 0. `python3 decode_no9.py --check` exit 0. Five
irregular forms are left ungraded and named in reading-no9.md (wafind, Aqui, wagged x2, Wardham). The ledger's operator
mark "(9)" on pages 13, 17, 19, 20 names the book (Cipher No. 9), a direct period witness for Tomokiyo's numbering.
Check: nine of the thirteen are printed in OR series I (I/32 pt 2; I/33 pp.488-489, 518-519, 615 and others; I/34 pt 2
pp.581-582) and agree with the print in every coded word, the time words included (Martha 1.30 PM, Clara 10.30 AM, Nancy
3.30 PM, Gertrude 12 noon, Florence 10 AM, Viola 12.30 PM exact; Martha against 1.24 and Harriet against 1.15 PM within
the half hour). Rule 4 notes: the book's Maj. Gen. for Lockwood and Kelley in O9-H against Brig. Gen. for both in O9-C
and O9-I, Rucker's Brig. Gen. in O9-E, and O9-P's time word in the month slot: logged in reading-no9.md, not settled.

Not found / not done: O9-E and O9-G were not located in I/33 by the phrases tried; O9-M (Dana to Watson, Philadelphia forage
frauds) and O9-O/P (Fox to Olcott, Navy Department) were not searched (ORN and other editions not read) -- search results
only, no novelty question asked (rule 10). Left out: the p.7 Baldwin 5 Feb entry and the two p.15 Wright/San Francisco
entries, whose code words do not make sense with mssEC 67 (ciphertext-no9.txt header). The thirteen were NOT re-checked
against the page images in this pass (cap); that check is the named next step. Key source per rule 10: period (mssEC 67).

Requests: hdl.huntington.org 31 (20 item-API pages, 11 IIIF pages), archive.org 3 (djvu full texts); all 200.

## Image check of O9-E..O9-Q, 6 Oct 2026 (R8-ECK64, LANE LANE-RUN8-account-1)

Step checked undone first: R7B-ECK64B (section above) read the thirteen from the volunteer text only and named the image
check as the next step. Kept as found: the Spit/men (N2-E), Village/Garrard (O9-A) and the O9-H/O9-P rule-4 notes, unchanged.

Route: Huntington IIIF, mssEC 19 pointers 8893, 8894, 8897-8899, 8903-8906, 8909, 8911, 8912 at 2400 px wide (scratch,
regenerable: `hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg`), then native-resolution
regions of five doubtful words (Gem, Negus, Sharpers, Queenly and one miss). Crop step, run before any subagent call:
`python3 tools/iiif_lines.py --image pages/p<pointer>.jpg --out crops --prefix p<pointer> --region 180,250,2000,2450
--prominence 40 --distance 65 --lines-per-crop 2` (124 two-line crops; the default prominence found 0 lines on these
pages). One blind Sonnet read per page batch (three batches of four pages, page 7 re-run alone after the batch skipped it),
given only crop paths; the worker compared each read with the volunteer text by script and settled every code-word
disagreement on the page image, at native resolution where the 2400 px image left doubt.

Found (image-check-no9.tsv): fifteen spans tabled. One code-word change: O9-Q's last line reads "Windhams Country" on the
page, not "Wardham County"; Windham = Enemy (mssEC 67 p.[23] l.13), the print's "enemy's country", so the token is now H.
Thirteen-entry total H 113 -> H 114 (all seventeen H 147 -> H 148), C 0, I 0, M 0 before and after;
`python3 decode_no9.py --check` exit 0. Every other code word the blind read disputed is the volunteer's reading on the
image: Palate, Queenly, Youth, Abbey (written Abby), Negus (the hand's looped N, not "Argus"), Sharpers, Waddings, wagged x2
(the hand's w), superb, and O9-P's last line "their way to Boston sig Annal" (below the crop region, read on the page). One
residual doubt, kept H and noted: O9-L's Gem has a looped capital that could be G or P; Pem is in no mssEC 67 row, and Gem =
Potomac is what the sentence (fords between the Monocacy and Point of Rocks) needs. The irregular forms "wafind" and "Aqui"
(O9-N) were confirmed on the image and stay ungraded. Plain words were not changed (O9-E "Bakers" may be Parkins/Parkers).

Not done: the "(9)" entries past page 20 (no page past 20 was fetched in this pass, so the brief's optional continuation
from images already fetched had nothing to read). Requests: hdl.huntington.org 23 (12 pages; 5 pct: region requests,
which the server answered with the whole page; 1 info.json; 5 pixel regions), all 200.

## The "(9)" entries of pages 21-60, 6 Oct 2026 (R9-ECK64, LANE LANE-RUN9-account-1)

Step checked undone first: R8-ECK64 (section above) fetched no page past 20; no dated section had read one.
Kept as found: the Spit/men (N2-E) and Village/Garrard (O9-A) conflicts and the O9-H/O9-P rule-4 notes, unchanged.

Route: Huntington CONTENTdm item API (field "text") for mssEC 19 pages 21-60 (pointers 8913-8952; scratch); "(9)" occurs on
pages 21, 27, 31, 34 and 51 only. Page images at 2400 px (IIIF, pointers 8913, 8919, 8923, 8926, 8943; scratch). Crop step,
run before the subagent call: `python3 tools/iiif_lines.py --image pages/p<pointer>.jpg --out crops --prefix p<pointer>
--region 60,250,2280,2550 --prominence 40 --distance 65 --lines-per-crop 2` (p8919 and p8926 re-cut over their lower halves,
--prominence 30), 31 two-line crops covering the five entries; one blind Sonnet read given only the crop paths; every
code-word disagreement settled by the worker on 2400 px regions (image-check-no9.tsv, R9 rows). mssEC 67 pp.[13], [14], [21]
at 1400 px (pointers 1733, 1734, 1741) and the committed p.[9], [10], [22] images for ten new key rows (key-no9.md section 4).

Found: five entries, Halleck to Steele 13 Mar and 1 Apr (Red River campaign), Halleck to Burnside at New York 7 Apr (move the
troops from Annapolis), Meigs as Quartermaster General (Abbot/Aragon) to Van Vliet 8 Apr (the steamers Arago and Fulton,
transportation for six thousand men), Stanton (Aaron/Arabia, Sec. of War) to Dix (Adorn/Agate) 22 Apr (Governor Seymour's
militia). H 45, C 0, I 0, M 0 (all twenty-two old-vocabulary entries H 193); `python3 decode_no9.py --check` exit 0. Image
check: no code-word change (Vermin, Famish, Vinton, Stagger, Adorn confirmed on the page against the blind read); plain
corrections O9-U "Van Vliet" (volunteer "Van Fleet") and O9-S "so as to" ("action" is a marginal pencil note). Check: O9-R,
O9-S, O9-T are printed in OR series I (I/34 pt 2 p.587, I/34 pt 3 p.27, I/33 p.815) and agree in every coded word and in the
time words (Viola 12.30 PM, Francis 11 AM, Hannah 2 PM exact); O9-R's plain "I desire ... I sent" against the print's "I
advise ... I send". Rule 4 notes: Lieut. Gen. Grant is written Vulture/Vomit + Vermin/Vernon (the book has no Lieut. Gen.
row); "Abe = or shun" (O9-T) and "grosvenor" (O9-V) stay ungraded (reading-no9.md). Key source per rule 10: period (mssEC 67).

Not found / not done: O9-U and O9-V not located in I/33 or I/34 pts 2-3 by the phrases tried; I/35 pt 2 and ser. III vol. 4
not searched (search results only, no novelty question asked). Unmarked entries of pages 21-60 in the old vocabulary (Pagan/
Pagoda openings without "(9)") and pages past 60 not examined. Requests: hdl.huntington.org 51 (40 item-API pages, two
'Empty reply' retried once each; 5 ledger IIIF pages; 3 mssEC 67 IIIF pages, one retried), archive.org 3 (djvu full texts);
all final responses 200.

## Eleven more old-vocabulary entries of pages 26-61, 6 Oct 2026 (R9-ECK64B, LANE LANE-RUN9-account-1)

Step checked undone first: R9-ECK64 (section above) named pages past 60 and the unmarked entries of pages 21-60 as not examined.
Kept as found: the Spit/men (N2-E) and Village/Garrard (O9-A) conflicts and the O9-H/O9-P rule-4 notes, unchanged.

Route: Huntington CONTENTdm item API (field "text") for mssEC 19 pages 21-72 (pointers 8913-8964; scratch); the ledger runs to
page 400 (object 9302, 402 children). Scanned by script for the operator's book mark in every written form ("(9)", "9" in
quotes, "No 9", "(No 9)") and for entries with three or more words in key-no9.md, each hit read by the worker. mssEC 67
pp.[20], [21], [23] at 1400 px (pointers 1740, 1741, 1743; scratch) and the committed p.[24] for five new key rows (key-no9.md
section 5). OR check: archive.org `_djvu.txt` of I/32 pt 3, I/33, I/34 pt 3, I/35 pt 2 and ser. III vol. 4
(warofrebellion323unit, 33unit, 343unit, 352unit, waroftherebellio026242mbp), dehyphenated and phrase-searched by script.

Found: R9-ECK64's "(9)"-only search missed the quoted and "No 9" forms of the mark; eleven further old-vocabulary entries,
O9-W..AG (ciphertext-no9.txt; reading-no9.md section "Eleven further entries"): Stanton to Dix 28 Mar (arrest of Mrs Mary W.
Rhodes, a rebel agent, to be sent to Fort Monroe), Meigs (Abbot/Aragon) to Van Vliet and to Capt. Wise at New York 19-22 Apr
(steamers, tugs, transportation for Butler's expedition, artillery and ammunition barges), Halleck to Dix 19 Apr (the 14th
New York Heavy Artillery), Stanton to Canby 21 Apr (state militia), Halleck to Columbus, Ohio 25 Apr (a militia regiment at
Johnson's Island), Halleck to Banks and Steele 30 Apr (no troops withdrawn from the Red River operations). Code-word tokens:
H 93, C 0, I 0, M 0 (all thirty-three old-vocabulary entries H 286); `python3 decode_no9.py --check` exit 0. Ungraded:
"bologna", "Abbott", "Memphis", "Vain Talents" (reading-no9.md). New key rows: Ramsay = Ammunition, Rusty = Fleet, Spoon =
Transports, White/Wick = Equipage, Wedge = Subsistence. Check: O9-Y (I/33 p.913, 4 p.m., Henrietta = 4 PM) and O9-AE (I/34
pt 3 p.358, 10.30 p.m., Susan = 10.30 PM) agree with the print word for word. Pages 62-72 (1-18 May 1864): every entry is
marked No 1/(1) or No 2/(2) or opens with Growl/Grapes; no old-vocabulary entry found there. Key source per rule 10: period
(mssEC 67).

Not found / not done: the eleven are from the volunteer text only, NOT image-checked (the named next step). O9-W, X, Z, AA,
AB, AC, AD, AF, AG not located in the five OR volumes by the phrases tried (reading-no9.md table); O9-U and O9-V not located
in I/35 pt 2 or ser. III vol. 4 either; ser. II (prisoners) and Quartermaster's letter books not searched -- search results
only, no novelty question asked (rule 10). Pages past 72 not fetched. Requests: hdl.huntington.org about 59 (about 56 item-API
calls: 52 pages, the parent object, three tries of pointer 8947 (page 55); 3 mssEC 67 IIIF pages), archive.org 15 (metadata, file lists, 5 djvu full
texts, 1 advancedsearch); all final responses 200.

## Image check of O9-W..O9-AG, 6 Oct 2026 (R10-ECK64C, LANE LANE-RUN10-account-1)

Step checked undone first: R9-ECK64B (section above) read the eleven from the volunteer text only and named this check.
Kept as found: the Spit/men (N2-E) and Village/Garrard (O9-A) conflicts and the O9-H/O9-P rule-4 notes, unchanged.

Route: Huntington IIIF, mssEC 19 pointers 8918, 8933, 8936-8940, 8942, 8946, 8953 at 2400 px wide (scratch, regenerable:
`hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg`). Crop step, run before any subagent call:
`python3 tools/iiif_lines.py --image pages/p<pointer>.jpg --out crops --prefix p<pointer> --region 60,250,2280,2550
--prominence 40 --distance 65 --lines-per-crop 2` (106 crops). Two blind Sonnet reads (five pages each), given only crop
paths; compared with the volunteer text by script (difflib per entry); every code-word disagreement and every line the blind
reads dropped or merged settled by the worker on the crops, and O9-X's last line on a 2400 px foot region (below the crop band).

Found (image-check-no9.tsv, R10 rows, 13 spans): no code-word change. Every disputed code word is the volunteer's reading on
the image: hammer (O9-W, the clerk's looped h, blind "Chamner"), Aragon (O9-X last line; O9-AA, blind "Aldgon"), Champlain
and Shylock (O9-Y, rows the blind read merged), Pagan (O9-Z, blind "Sagan"), Merlin x2, Raven (blind "Ravin"), Vulcan
(O9-AG, first vowel open, kept). One plain correction: O9-AG line 3 reads "Wise" on the page, not "Wide" -- "Vulcan Wise",
Captain Wise, the addressee of O9-Z; ciphertext-no9.txt and its plain: line changed, reading regenerated. O9-AE line 2 is
"&" (a faint offset "Bangor" shows beside it, not written there). O9-Z "Vain Talents": the second word starts with a
crossed T and does not read "Fleet" as the blind read guessed; left as the volunteer's, doubtful, ungraded.
Code-word tokens over the eleven unchanged (H 93, C 0, I 0, M 0; all thirty-three old-vocabulary entries H 286);
`python3 decode_no9.py --check` exit 0.

Not done: plain words outside the disagreement list were not re-read word by word; O9-AE's line "be with drawn from
operations against" was skipped by the blind read and not re-read (plain words only). Requests: hdl.huntington.org 10
(ten page images), all 200.
