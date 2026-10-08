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
Read so far: 20 of about 570 Cipher No. 1 entries of mssEC 19 read (section 4: H 298, C 8, M 0, I 0 code-word tokens, `decode.py --check` exit 0) plus 21 entries in Cipher No. 2 (N2-N..U, eight Beckwith/Caldwell entries of Feb-June 1864, ECK64-NO2, 7 Oct 2026: H 419, C 7, I 18, M 1 over the 21; earlier: 11 Beckwith/Kimber/Caldwell, section 8 and DEF1-ECK64, 5 Oct 2026; N2-L, the p.61 twin of O9-AE, AM-ECK64N2, 7 Oct 2026; N2-M, the Kimber entry of 11 June 1864 on p.90, AM-ECK64K, 7 Oct 2026: H 299, C 6, I 10, M 1, `decode_no2.py --check` exit 0); plus N2-V..AC (pages 21-34, D12-E2, 7 Oct 2026) and N2-AD..AK (pages 4-18, D12-E1, 7 Oct 2026: H 269, C 6, I 5, M 1), 37 No. 2 entries in all, H 802, C 23, I 25, M 2; the rest of the ledger untranscribed. Closed: the old-vocabulary (Tomokiyo No. 9) entries of mssEC 19, all thirty-three O9-A..AG read (H 286) and image-checked (R7A/R7B/R8/R9-ECK64; O9-W..AG by R10-ECK64C, 6 Oct 2026; O9-AE's one unchecked plain line confirmed by B0709-A1, 7 Oct 2026).
- corpus pass over the remaining ~550 mssEC 19 entries and mssEC 18 - blocker: waiting-on the Huntington curator's reply to the 20 Sept 2026 enquiry; section 9 names that reply as the decision point for the corpus pass

## Escalation (GAPSFIX, 4 Oct 2026)
- [ ] siblings: mssEC 25 second copy read for E4/E5 (Second reader, 24 Sept 2026; four corrections applied); mssEC 18 opened 5 Oct 2026, pp.50-60 text, no E4/E5 copy
- [x] clear-pages: OR prints matched for 17 of 20 entries as the check (section 4)
- [x] known-keys: Cipher No. 1 (mssEC 41) and Cipher No. 2 (mssEC 47) are the period key books in use
- [x] print: OR series I sweep, ORN, Butler and Fox correspondence, Lincoln Collected Works (section 4, AUDIT.md)
- [n/a] key-rebuild: period cipher books exist and read every code word in the twenty entries; for the Jan-Feb 1864 old vocabulary the period book is mssEC 67 (filled-in, Tomokiyo's No. 9), read on 9 pages for the sample (R7A-ECK64, 6 Oct 2026) and on pp.[9]-[24] for the further entries (R7B-ECK64B, 6 Oct 2026)
- [x] image-check: E4/E5 re-read word by word at full size against both ledgers (Second reader, 24 Sept 2026); N2-E Spit re-read in mssEC 47, mssEC 48 and the ledger (D2-ECK64S, 5 Oct 2026: Spit = Near in both books, ledger Spit; conflict logged, not resolved); O9-E..Q checked against the mssEC 19 page images (R8-ECK64, 6 Oct 2026, image-check-no9.tsv); O9-R..V likewise (R9-ECK64, 6 Oct 2026); O9-W..AG likewise (R10-ECK64C, 6 Oct 2026, 13 spans, no code-word change, O9-AG Wide -> Wise applied; O9-AE line 6 confirmed B0709-A1, 7 Oct 2026)
- [n/a] retry: M 0 in the twenty read entries, no doubtful token left to retry
Verdict: keep going: 0 internal gaps; the corpus pass waits on the Huntington curator (outside); the siblings step is open; cheapest next: the unread operator entries left in no2-candidates.tsv (status column empty; pages 4-18 done by D12-E1, 21-34 by D12-E2, 40-55 by D12-E3, 56-74 by D12-E4, the seven named rows of pages 86-104 by D4-E5), the Cipher No. 1 entries found among the candidates for ciphertext.txt, and the 109 pages from about p.160 on whose volunteer text was not yet fetched, read with key-no2.md as N2-AZ..BF were, ~$0.5-1.2 per entry (updated D4-E5, 7 Oct 2026: seven entries of pages 86-105 read as N2-AZ..BF, H 292, C 15, I 14, M 0, all seven located in print: six in the OR, N2-AZ in Grant Papers vol. 11; `decode_no2.py --check` exit 0). Earlier: keep going: 0 internal gaps; the corpus pass waits on the Huntington curator (outside); the siblings step is open; cheapest next: the unread operator entries left in no2-candidates.tsv (status column empty; pages 4-18 done by D12-E1, 21-34 by D12-E2, 40-55 by D12-E3, 56-74 by D12-E4), the Cipher No. 1 entries found among the candidates for ciphertext.txt, and the 109 pages from about p.160 on whose volunteer text was not yet fetched, read with key-no2.md as N2-AS..AY were, ~$0.5-1.2 per entry (updated D12-E4, 7 Oct 2026: seven "(No 2)"/Beckwith entries of pages 56-74 read as N2-AS..AY, H 237, C 9, I 4, M 0, all seven located in print: six in the OR, N2-AS in Grant Papers vol. 10; `decode_no2.py --check` exit 0). Earlier: Verdict: keep going: 0 internal gaps; the corpus pass waits on the Huntington curator (outside); the siblings step is open; cheapest next: the unread operator entries left in no2-candidates.tsv (pages 35-160 of mssEC 19 less those read: pages 4-18 done by D12-E1, 21-34 by D12-E2, the seven of pages 40-54 by D12-E3), the three Cipher No. 1 entries found among the candidates (8900/8/0, 8907/15/2, 8916/24/2) for ciphertext.txt with key.md and decode.py --check, and the 109 pages from about p.160 on whose volunteer text was not yet fetched, read with key-no2.md as N2-V..AR were, ~$1.2 per entry (updated D12-E3, 7 Oct 2026: the seven candidates of pages 40-54 read as N2-AL..AR, H 215, C 14, I 11, M 0; all seven printed in the OR word for word (I/33 pp.897, 907, 940, 949, 966-967; I/34 pt 3 pp.234-235; N2-AQ split between I/32 pt 3 p.489 and I/34 pt 3 p.278); one code-word conflict logged (Nuptial = Steele in N2-AQ against Smith elsewhere); `decode_no2.py --check` exit 0). Earlier: keep going: 0 internal gaps; the corpus pass waits on the Huntington curator (outside); the siblings step is open; cheapest next: the unread operator entries left in no2-candidates.tsv (pages 35-160 of mssEC 19, plus any left on pages 19-34; pages 4-18 done by D12-E1, 21-34 by D12-E2), the three Cipher No. 1 entries found among the candidates (8900/8/0, 8907/15/2, 8916/24/2) for ciphertext.txt with key.md and decode.py --check, and the 109 pages from about p.160 on whose volunteer text was not yet fetched, read with key-no2.md as N2-V..AK were, ~.2 per entry (updated D12-E1, 7 Oct 2026: the ten candidates of pages 4-18 done: eight read as N2-AD..AK, H 269, C 6, I 5, M 1; five printed in the OR word for word, one in Basler vol. 7, N2-AE's McPhail part in the OR with two differences; N2-AI and N2-AJ not located in I/33; two were Cipher No. 1; `decode_no2.py --check` exit 0). Earlier: keep going: 0 internal gaps; the corpus pass waits on the Huntington curator (outside); the siblings step is open; cheapest next: the unread operator entries left in no2-candidates.tsv (pages 4-160 of mssEC 19; pages 21-34 done by D12-E2), the Cipher No. 1 entry 8916/24/2 for ciphertext.txt, and the 109 pages from about p.160 on whose volunteer text was not yet fetched, read with key-no2.md as N2-V..AC were, ~$1.2 per entry (updated D12-E2, 7 Oct 2026: eight entries of pages 21-34 read as N2-V..AC, H 115, C 11, I 2, M 0; five printed in the OR and three in Grant Papers vol. 10, word for word; 8916/24/2 is Cipher No. 1; `decode_no2.py --check` exit 0). Earlier: keep going: 0 internal gaps; the corpus pass waits on the Huntington curator (outside); the siblings step is open; cheapest next: the 74 unread operator entries listed in no2-candidates.tsv (pages 8-160 of mssEC 19) and the 109 pages from about p.160 on whose volunteer text was not yet fetched (pointer list from the CONTENTdm search, NOTES.md ECK64-NO2), read with key-no2.md as N2-N..U were, ~$1.2 per entry (updated ECK64-NO2, 7 Oct 2026: eight more entries read, N2-N..U, H 120, C 1, I 8, M 0 (H 119 after the verifier's N2-Q Annapolis correction); four printed in the OR word for word, two more in The Papers of Ulysses S. Grant vol. 10 (verifier), two not located; `decode_no2.py --check` exit 0). Earlier: keep going: 0 internal gaps; the corpus pass waits on the Huntington curator (outside); the siblings step is open; cheapest next: the other Beckwith/Kimber/Caldwell "(No 2)" entries of mssEC 19 beyond the 19 Sept selection pages, found from the volunteer text by operator name and read with key-no2.md, disk + IIIF pages, ~$3 (updated AM-ECK64K, 7 Oct 2026: the Kimber entry of 11 June 1864 opening p.90 read as N2-M, H 13 (10 in the message, 3 in a post-signature service line naming the Canby code words), a Quartermaster-General query on the gauge of the Vicksburg & Shreveport Rail-road; not printed in OR I/34 pt 4, whose Meigs to Canby of 17 June (p.424-425) says he had telegraphed twice for the gauge; `decode_no2.py --check` exit 0). Earlier: keep going: 0 internal gaps; cheapest next: the Kimber entry of 11 June 1864 (Vicksburg) opening p.90 (pointer 8982), named by DEF1-ECK64 and not read, read with key-no2.md and checked against the OR volume for its date, disk + 1 IIIF page, ~$1.5 (updated AM-ECK64N2, 7 Oct 2026: the p.61 Cipher No. 2 twin of O9-AE read as N2-L, H 13, all 13 agree with O9-AE and key-no2.md, `decode_no2.py --check` exit 0). Earlier: keep going: 0 internal gaps; cheapest next: the Cipher No. 2 twin of O9-AE on mssEC 19 p.61 (Buckley to Hunter at New Orleans, 30 Apr 1864, same order as O9-AE) read with key-no2.md against O9-AE's plain, disk + 1 IIIF page, ~$1 (updated B0709-A1, 7 Oct 2026: the O9-W..AG image check was already done by R10-ECK64C on 6 Oct; this Verdict had not been updated). Earlier: keep going: 1 internal gap; cheapest next: image-check the eleven O9-W..AG entries of pages 26-61 against the mssEC 19 page images, ~$4 (updated R9-ECK64B, 6 Oct 2026: pages 21-72 scanned for every form of the operator's "9" mark and for old-vocabulary words; eleven more entries read with key-no9.md, H 93, M 0, decode_no9.py --check exit 0; O9-Y and O9-AE matched in the OR, O9-U/V not in I/35 pt 2 or III/4). Earlier: keep going: 1 internal gap; cheapest next: scan mssEC 19 pages 61 onward (and the unmarked entries of pages 21-60) for further old-vocabulary entries, read them with key-no9.md, and search O9-U/O9-V in OR I/35 pt 2 and ser. III vol. 4, ~$3 (updated R9-ECK64, 6 Oct 2026: the five "(9)" entries of pages 21-60 read and image-checked, H 45, M 0, decode_no9.py --check exit 0). Earlier: keep going: 1 internal gap; cheapest next: the "(9)"-marked Jan-Mar 1864 entries past page 20 of mssEC 19 read from the page images with key-no9.md, ~$4 (updated R8-ECK64, 6 Oct 2026: O9-E..Q image-checked, one code-word change, H 148, M 0, decode_no9.py --check exit 0). Earlier: keep going: 1 internal gap; cheapest next: image-check the thirteen O9-E..Q entries (volunteer text only so far) and continue the "(9)"-marked entries past page 20 of mssEC 19, ~$4 (updated R7B-ECK64B, 6 Oct 2026: 17 old-vocabulary entries read with mssEC 67, H 147, decode_no9.py --check exit 0). Earlier: keep going: 1 internal gap; cheapest next: the rest of the Jan-Feb 1864 old-vocabulary entries (pages 1-20 of mssEC 19, with key-no9.md extended from mssEC 67 pp.[11]-[15], [18]), ~$4 (updated R7A-ECK64, 6 Oct 2026: four-entry sample read with mssEC 67, decode_no9.py --check exit 0). Earlier note: (updated D2-ECK64S, 5 Oct 2026: the Spit/men conflict was re-read at full size in both key books and the ledger and is logged as a data conflict in its own section below)

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

## B0709-A1 (7 Oct 2026, account 1, for the account-3 orchestrator): O9-W..AG image check already on file; O9-AE line 6 confirmed

The batch brief named the image check of O9-W..AG, from the stale Verdict line. R10-ECK64C had already done it on 6 Oct 2026
(section above; image-check-no9.tsv rows 39-51; `python3 decode_no9.py --check` exit 0 again on 7 Oct 2026). That check left one
plain line unread: O9-AE line 6. This session fetched page 61 (pointer 8953, IIIF 2400 px, scratch, 1 request to hdl.huntington.org,
200) and read it by eye. It reads "be with drawn from operations against", as the volunteer text has it, and O9-AE's other lines also
agree. The only addition is that the page ends the entry with "End" after "Cairo"; that is a plain sign-off word, not applied. No code
word or grade changed (H 286 over the thirty-three entries).
Seen on the same page: above O9-AE, the same order went in Cipher No. 2 as a "(No 2)" entry, Buckley to Hunter at New Orleans, Wash
Apl 30 1864 10 pm. Its code words include Ogden, Reliance, Lapland, nutmeg, Crowd, wharf, Altar, Wafer, Prospect, Wiley and lady, and
its plain runs parallel to O9-AE ("directs that orders heretofore given be so modified that no ... be with drawn from operations
against Shreveport"). The folder has no record of this entry. It is a two-book parallel that can check key-no2.md words against
O9-AE's plain. This is a suggestion only; it was not read (Usage 7).

## AM-ECK64N2 (7 Oct 2026, account 2, for LANE LANE-AM-0914): the Cipher No. 2 twin of O9-AE read (N2-L)

Step checked undone first: no ciphertext-no2.txt block, no dated section, no ROOM done line for the p.61 "(No 2)" entry
(B0709-A1 named it as a suggestion). Route: Huntington IIIF, pointer 8953 at 2400 px (scratch, regenerable:
`hdl.huntington.org/digital/iiif/p16003coll11/8953/full/2400,/0/default.jpg`), plus `dmGetItemInfo/p16003coll11/8953/json`
for the volunteer text. Crop step, run before reading: `python3 tools/iiif_lines.py --image $S/p8953.jpg --out $S/crops
--prefix p61n2 --region 180,150,2040,990 --centres 90,185,280,385,485,595,690,790,885,975 --lines-per-crop 2
--max-width 2400` and, for the four lines that band clipped, `--region 180,520,2040,500 --centres 60,160,260,360
--lines-per-crop 1` (9 crops). Read by the worker on the crops (no subagent; ten short lines), volunteer text as second
witness: every word agrees. Notes on the page: "directs" ends in a flourish that may omit the s; "given" and the line-7
"And" are written over erased words; "10 pm" pencilled over the date line.

Result (ciphertext-no2.txt N2-L; reading-no2.md "The p.61 twin of O9-AE"): code-word tokens H 13, C 0, I 0, M 0. All 13
agree with O9-AE's reading under key-no9.md and with the OR print of the order (I/34 pt 3 p.358): Hunter = Washington
(O9 Pagan), Ogden = 30, Reliance = 10.30 PM (O9 Susan), Lapland = Banks (O9 amen), nutmeg = Steele, Crowd = Lieut Gen Grant
(O9 vomit vermin Bangor), wharf = Troops (O9 youth), Altar Wafer = Red R River (O9 Glover Spartan), Prospect = Command,
wiley lady = signed Halleck (O9 signed applause). No key-no2.md value differs; no clerk variant. Grading kept at H (the
book reads each word); each is also fixed by the twin's plain, so the 13 are H with C corroboration, not double-counted.
The plain run differs from O9-AE only in "And"/"&" and the copy routes: N2-L to New Orleans with a copy to Steele via
Little Rock, O9-AE to Little Rock with a copy to Banks via Cairo -- the one order sent to each commander in the cipher his
office held. One collision: "Staff" is a book code word (Station, p.[25B] row 22) but plain here ("Chf Staff", OR "Chief
of Staff"); marked `plain:`. `python3 decode_no2.py --check` exit 0. Requests: hdl.huntington.org 2 (image, item info), both 200.

## AM-ECK64K (7 Oct 2026, account 2, for LANE LANE-AM-0914): the Kimber entry of 11 June 1864 on p.90 read (N2-M)

Step checked undone first: no N2 block for pointer 8982, no dated section, no ROOM done line (DEF1-ECK64 named it, not
read). Route: Huntington CONTENTdm `dmGetItemInfo/p16003coll11/8982/json` (volunteer text) and IIIF
`hdl.huntington.org/digital/iiif/p16003coll11/8982/full/2400,/0/default.jpg` (scratch, regenerable). Crop step, run
before reading: `python3 tools/iiif_lines.py --image $S/p8982.jpg --out $S/crops --prefix p90k --region 180,1140,2040,640
--centres 60,160,260,360,460,560 --lines-per-crop 2 --max-width 2400` (3 crops). Read by the worker on the crops (no
subagent; six short lines), volunteer text as second witness: every word agrees ("Hannah", not the "Harriet" of the
entry above it).

Result (ciphertext-no2.txt N2-M; reading-no2.md "The Kimber entry of 11 June 1864"): 1 PM June 11, to Canby: "I can not
find the gauge of the Vicksburg & Shreveport Rail-road. What is it?", signed Burglar = Quarter[?] Master General (the key
row's own [?]); then, after the signature, "use Farmer Famish Mastiff for Can" -- the three Canby code words named, a
service line. Code-word tokens H 13 (10 in the message, 3 in the service line), C 0, M 0; "Sleeve port" = Shreveport
is the clerk's spelling, I by inference, not a code word. No key-no2.md value differs. OR I/34 pt 4 (IA djvu full text)
does not print this telegram (searched by phrase and every 11 June date line); it prints Meigs to Canby, 17 June 1864
1.30 p.m. (p.424-425), "I have telegraphed you twice to inform me of the gauge", which fits N2-M as one of the two and
the QMG reading of Burglar -- context corroboration, no token raised to C. Other volumes and the Meigs letter books not
searched; a search result only, no novelty claimed. `python3 decode_no2.py --check` exit 0. Requests:
hdl.huntington.org 2 (item info, image), archive.org 1, all 200.

## AM-ECKV (7 Oct 2026, account 2, verifier, for LANE LANE-AM-0914): N2-L and N2-M carried into AUDIT.md

Rule 10 propagation for the two entries above. decode_no2.py --check re-derived (exit 0), 13 + 13 H against key-no2.md,
p.90 image re-read. N2-L **N1** (plain printed OR I/34 pt 3 p.358), D4; N2-M **N3** (not located in OR I/34 pt 4, OR III/4,
Google Books, the Huntington record; Meigs letter books and NARA RG 92 unread), D4, key period; status.json rows added;
SO-ECKERT-N2M queued. See AUDIT.md "## AUDIT (propagation, AM-ECKV)".

## ECK64-NO2 (7 Oct 2026, account 1, for the account-3 orchestrator): eight more Cipher No. 2 entries read (N2-N..U)

Step checked undone first: no N2 block past N2-M, no ROOM done line for further "(No 2)" entries. Finding the entries:
Huntington CONTENTdm `dmQuery/p16003coll11/CISOSEARCHALL^<name>^all^and/...` for Beckwith (170 pages of mssEC 19, object 9302),
Caldwell (47), Kimber (8), Buckley (1): 202 pointers. The volunteer text (`dmGetItemInfo`, field `transc`) of the first 93 of
them (pages 8 to about 160) was fetched, split into entries at blank lines, and every entry whose header names one of the four
operators scored by decoding it with key-no2.md, key.md and key-no9.md (counts of code-word tokens); key-no2 led on every
entry. The table is `no2-candidates.tsv` (93 entries; READ marks those in ciphertext-no2.txt by page; 74 unread). The other 109
pages were not fetched (the fetch was stopped to keep one request at a time on the host while the images were taken).

Eight short unread entries were chosen across Feb-June 1864 and read by the worker from strip crops of the 2400 px IIIF images
(`hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg`, scratch, regenerable). Crop step, run before
reading: `python3 tools/iiif_lines.py --image $S/img/p<pointer>.jpg --out $S/crops --prefix <p> --region 120,<y0>,2120,<h>
--centres <...> --lines-per-crop 2|3 --max-width 2400` with regions 8902 1490+800, 8906 1690+620, 8915 1460+420 (+ a 180 px
repair strip at 1760), 8944 950+860, 8948 1590+700, 8971 1140+700, 8979 1240+900, 8985 240+720 (automatic line finding not
tried, as on these ruled pages before). No subagent; the volunteer text as second witness agrees on every word except N2-N
("For Chart Tulip", volunteer "For Tulip") and N2-R's header date (image 2[6?], volunteer 20; the date words give 26).

Result (ciphertext-no2.txt N2-N..U; reading-no2.md "Eight further Beckwith/Caldwell entries"): H 120, C 1, I 8, M 0. Four are
printed in the OR and agree word for word (N2-N I/32 pt 2 p.407, N2-O p.494, N2-S I/36 pt 3 p.207, N2-U I/40 pt 2 p.47, the
President's "I begin to see it" telegram); four were not located in the volumes searched by phrase (N2-P I/32 pt 3 and I/34
pt 2; N2-Q and N2-R I/33; N2-T I/36 pt 3), a search result only. key-no2.md section 8 gains three clerk's forms at I: Balm
(February), stick (Period), Slumberations (operations; one witness that Slumber = Operations on [25B], against the inferred
Religion = Operations -- logged in reading-no2.md, not resolved). Two date-word conflicts logged, not resolved: N2-Q's date
words read April 22 against the header's 23rd, and N2-T's Mark = July (H) against the header's June 6th. "Ann" in N2-Q is left
unread (marked plain): the TIME table's 1 AM cannot stand in "from Ann Apple [Tennessee]". `python3 decode_no2.py --check`
exit 0. Requests: hdl.huntington.org about 106 (4 searches, 93 item-info, 8 images, 1 retry-free), archive.org 6 (OR djvu
texts I/32 pt 2, I/32 pt 3, I/33, I/34 pt 2, I/36 pt 3, I/40 pt 2), all 200.

Verifier correction (ECK64-NO2 verifier, 7 Oct 2026; AUDIT.md "AUDIT (propagation, ECK64-NO2 verifier)"): two of the four
"not located" entries are printed in the sender-/recipient-specific edition the solver did not search, The Papers of Ulysses S.
Grant vol. 10 (N2-P, from the RG 107 telegram sent; N2-Q at p.343, 4:00 P.M.), so four printed in the OR and two in PUSG, two
(N2-R, N2-T) not located. PUSG shows N2-Q's "Ann Apple is" is the clear word Annapolis: Apple is not the code word Tennessee
there, and "Ann" is not an unread token; corrected counts H 119, C 1, I 8, M 0 (21 entries H 418), the derived block
regenerated with `plain: Ann Apple` on N2-Q (ECK64-NO2, same day). N2-T's subject is answered by Dana to Stanton, 7 June 1864, OR I/36 pt 1
p.91, which also supports the header date June 6 against Mark = July.

## D12-E2 (7 Oct 2026, account 2, for LANE DEFAULT-account-2-20261007-1210): eight "(No 2)" entries of pages 21-34 read (N2-V..AC)

Step checked undone first: no N2 block for pointers 8913-8926, no ROOM done line for pages 21-34 (no2-candidates.tsv status
empty). Route: Huntington CONTENTdm `dmGetItemInfo/p16003coll11/<pointer>/json` (volunteer text, field `transc`) and IIIF
`hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg` for 8913, 8914, 8915, 8916, 8917, 8926
(scratch, regenerable). Crop step, run before reading (S = scratch): `python3 tools/iiif_lines.py --image $S/img/p<pointer>.jpg
--out $S/crops --prefix <p> --region 120,<y0>,2120,<h> --centres <...> --lines-per-crop 1|2|3 --max-width 2400` with regions
8913 1080+860 and 1980+700 (+ 1830+140), 8914 2020+620, 8915 2110+400, 8916 260+420 and 810+1020 (+ 40,1390,900,130),
8917 1500+820, 8926 240+1080 (centres set by eye from a quarter-size thumbnail; automatic line finding not tried). No subagent.
The volunteer text agrees on every word except: "Chant" (image Chant, agreed) in N2-Z/AA/AC; N2-AB's signature (image Lamb[?],
volunteer Sanib); N2-AC "Whimy" (volunteer Whimsy) and "Brown[?]" (volunteer Brom).

Result (ciphertext-no2.txt N2-V..AC; reading-no2.md "Eight entries of pages 21-34"): code-word tokens H 115, C 11, I 2, M 0
(two [?] tokens graded by their key rows). All eight located in print, word for word: five in the OR (N2-V I/34 pt 2 p.606,
N2-W I/32 pt 3 p.72-73, N2-Z I/33 p.699, N2-AA I/33 p.718, N2-AC I/32 pt 3 p.300-301; page numbers from the djvu running
heads) and three in The Papers of Ulysses S. Grant vol. 10 by IA full-text snippet, page not established (N2-X, N2-Y near
p.213-214, N2-AB); a search result only. key-no2.md section 8 gains Chant (= Grant, three entries), Spurigation, Whimy (= to-day;
the book's To day is Wherry) and nisty (= Rusty, forage), all C from the print. Logged, not resolved: N2-X's "The Religion of
Captain Jenkins" = "The operations" (Grant Papers) is a second witness for Religion = Operations against N2-T's Slumberations;
N2-AA's time word Gertrude = 12 noon against the OR's 12.30 p.m. 8916/24/2 (Caldwell, 23 Mar, unmarked) reads in Cipher No. 1,
not No. 2 (no2-candidates.tsv status NOT-NO2), and is left for the Cipher No. 1 file. `python3 decode_no2.py --check` exit 0.
Requests: hdl.huntington.org 12 (6 item-info, 6 images), archive.org 3 (djvu I/33, I/32 pt 3, I/34 pt 2), be-api.us.archive.org
8 (PUSG vol. 10 full-text; 5 answered 200, 3 answered 502 and were not retried), all others 200.

## D12-E1 (7 Oct 2026, account 2, for LANE DEFAULT-account-2-20261007-1210): the unread "(No 2)" candidates of pages 4-18 (N2-AD..AK)

Step checked undone first: no ciphertext-no2.txt block for pointers 8896, 8900, 8901, 8903, 8906 (entry 1), 8907, 8909, 8910 and
no ROOM done line for them. Route: Huntington CONTENTdm `dmGetItemInfo/p16003coll11/<pointer>/json` (volunteer text, field
`transc`) and IIIF `hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg` (scratch, regenerable), for
the eight pointers plus 8902 (top of page 10, where the page-9 entry ends). Crop step, run before reading:
`python3 tools/iiif_lines.py --image $S/img/p<pointer>.jpg --out $S/crops --prefix <p> --region <x,y,w,h> --lines-per-crop 2|3
--max-width 2400 [--debug] [--columns 100:2000 --prominence 40]` with 8896 `120,1300,2160,800`; 8900 `200,1290,2000,580`; 8901
`120,200,2180,2560` (with --columns/--prominence; plus one 700 px right-edge strip for the line ends); 8902 `120,120,2270,1300`;
8903 `120,170,2180,1400` (plus a 1050x160 detail of line 2); 8906 `120,1020,2160,640`; 8909 `120,1170,2180,960`; 8910
`120,170,2180,1730` and `120,2020,2160,440`. Automatic line finding worked on every region. Read by the worker on the crops (no
subagent), volunteer text as second witness; the image readings that differ from it are listed in the ciphertext-no2.txt
header comment (the one that matters: N2-AF "given no Repeats", volunteer "my"; the OR prints "no").

Result: of the ten listed rows, **two are Cipher No. 1, not No. 2** (8900 page 8 entry 0, Beckwith "1", Halleck to Grant 8 Feb
1864, cavalry for Banks: key.md reads 27 tokens into sense, key-no2.md none; 8907 page 15 entry 2, Caldwell "1", to Humphreys 4
Mar 1864: Fredericksburg, Enemy, Rappahannock, Meade). Not transcribed (they belong with ciphertext.txt / decode.py, outside this
job). The other eight are read as N2-AD..AK (reading-no2.md "Eight entries of pages 4-18"): **H 269, C 6, I 5, M 1** (37-entry
total H 802, C 23, I 25, M 2), `python3 decode_no2.py --check` exit 0. Print check by phrase and date line in OR I/33 and I/32 pt 2
(IA djvu full text) and by be-api full-text search in PUSG vol. 10 and Basler vol. 7: N2-AD I/33 p.486, N2-AF I/32 pt 2 p.410 (and
quoted in PUSG vol. 10), N2-AG I/33 p.614, N2-AH I/33 p.650 word for word; N2-AE's McPhail telegram I/32 pt 2 about p.392 and I/33
p.558 (its covering note and the Baltimore telegram to Eckert, signed Baldwin, not located); N2-AK in Basler vol. 7 (snippet, no
page), not in I/33; N2-AI (Howell to Ingalls, 8 Mar) and N2-AJ (Augur to Ingalls, 9 Mar, Grant coming to the Army of the
Potomac) not located in I/33, a search result only. Other volumes not searched: OR ser. III vol. 4 (for N2-AI's horses), the
Meigs/QMG letter books, Lincoln Papers at LoC for N2-AK.

Key-no2.md section 8 gains seven rows, logged not resolved: clerk's forms at I (Tobsy = 12.30 PM, Kerby = 14, Abbott =
James; Word = West in N2-AD is described but not keyed, since a row would also read the plain "words" of D12-E2's N2-AB); values from the print at C, each one witness and none in the transcribed tables (Monkey = Schofield, Lusty =
Forage, Palmutta = Brigade); and Quicken = Detach restated at H because decode.py does not strip the note in its section 5 cell.
Conflicts logged in reading-no2.md: Pine = Communicate (book; N2-AF agrees with the OR) where N2-AE's "Snake Pine Talbot Argus"
stands for the OR's "Hdqrs. Army of the Potomac"; N2-AE 700 Infantry against the OR's "780 Maryland Line"; N2-AJ Viola = 12
midnight against the header's noon; N2-AH Elizabeth = 10.30 AM against the OR's 10.50 a.m.; Chumb (M) again where the OR prints
Banks. These readings postdate AUDIT.md: a verifier is to carry N2-AD..AK into it (rule 10 propagation).
Requests: hdl.huntington.org 18 (9 item info, 9 images), archive.org 3 (2 djvu texts, 1 advancedsearch), be-api.us.archive.org
6 (one returned a non-JSON reply, not retried), quod.lib.umich.edu 1 (403, host stopped); all others 200.
Block letters: written as N2-V..AC and renumbered N2-AD..AK at the push, D12-E2 having taken N2-V..AC for pages 21-34.

## D12-E3 (7 Oct 2026, account 2, for LANE DEFAULT-account-2-20261007-1210): seven "(No 2)" entries of pages 40-55 read (N2-AL..AR)

Step checked undone first: no N2 block for pointers 8932-8947 except N2-Q (8944 entry 1), no ROOM done line for pages 40-54
(no2-candidates.tsv status empty). Route: Huntington CONTENTdm `dmGetItemInfo/p16003coll11/<pointer>/json` (volunteer text,
field `transc`) for 8932, 8935, 8936, 8942, 8944, 8945, 8946, 8947 and IIIF `hdl.huntington.org/digital/iiif/p16003coll11/
<pointer>/full/2400,/0/default.jpg` for the same eight (scratch, regenerable). Crop step, run before reading (S = scratch):
`python3 tools/iiif_lines.py --image $S/img/p<pointer>.jpg --out $S/crops --prefix <p> --region 120,<y0>,2120,<h> --centres <...>
--lines-per-crop 3|4 --max-width 2400` with regions 8932 240+1340 (centres set by eye), and at a fixed 100 px pitch 8935 1240+1000,
8936 200+1000, 8942 1720+1060, 8944 200+640, 8945 100+1400 (+ 1440+420), 8946 1700+1080, 8947 180+1280 (+ 1420+420); the crops
were read at 1500 px width, stacked per page. No subagent. The volunteer text agrees on every word except: N2-AM "Sard[?]"
(volunteer Lord) and "Grup" (volunteer grup); N2-AO "new" (volunteer news, which is a book line indicator); N2-AQ "Jennie[?]"
(volunteer Tennir; the OR's 3 p.m. is the book's Jennie); N2-AR "Chant" (volunteer Chart) and the chat word "Sam" (volunteer I am).

Result (ciphertext-no2.txt N2-AL..AR; reading-no2.md "Seven entries of pages 40-55"): code-word tokens H 215, C 14, I 11, M 0.
All seven located in the OR, word for word: N2-AL I/33 p.897; N2-AM I/33 p.907; N2-AN I/34 pt 3 p.234-235; N2-AO I/33 p.940;
N2-AP I/33 p.949; N2-AQ I/32 pt 3 p.489 with its second half in I/34 pt 3 p.278 (the OR splits the telegram by a footnote);
N2-AR I/33 p.966-967 (page numbers from the djvu running heads). key-no2.md section 8 gains Greenlys (depots), Sard (Period),
Grup (Meade, the book's Grub), Yancy (Wednesday) and Telegram (withdrawn; the book's Telegraph = Withdraw, [25C]), all C from the
print. Plain words marked: Devons (the name Devens), Collect, subject, ration, opinions, Despatches, French, Summer. Logged, not
resolved: N2-AQ "Nuptial Princeton" = OR "Steele's command" against Nuptial = Smith in the same entry and in N2-AL; N2-AQ date
words 26 against the header and OR 25; N2-AR Florence 11.30 AM against the OR's 11.30 p.m.; the ledger's plain "read" (N2-AL) and
"means" (N2-AO) where the OR prints "equipped" and "transports"; N2-AN adds Cavalry after "2000", which the OR does not print.
PUSG vol. 10 was not searched: Grant is the recipient of six entries and all six were found in the OR first. `python3
decode_no2.py --check` exit 0. Requests: hdl.huntington.org 16 (8 item-info, 8 images), archive.org 3 (djvu I/33, I/34 pt 3,
I/32 pt 3), all 200.

## D12-E4 (7 Oct 2026, account 2, for LANE DEFAULT-account-2-20261007-1210): seven entries of pages 56-74 read (N2-AS..AY)

Step checked undone first: no N2 block for pointers 8948-8966 and no ROOM done line for pages 56-74 (no2-candidates.tsv status
empty for the seven). Route: Huntington CONTENTdm `dmGetItemInfo/p16003coll11/<pointer>/json` (volunteer text, field `transc`)
and IIIF `hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg` for 8948, 8951, 8952 (p.60, where
8951/59/2 ends), 8956, 8961, 8964, 8965, 8966 (scratch, regenerable). Crop step, run before reading (S = scratch):
`python3 tools/iiif_lines.py --image $S/img/p<pointer>.jpg --out $S/crops --prefix p<page> --region <x,y,w,h>
--lines-per-crop 2|3 --max-width 2400` with regions 8948 160,230,2160,1340; 8951 120,1720,2120,880; 8952 120,60,2160,1060
(--centres 120,215,...,915); 8956 160,320,2160,1030; 8961 120,2050,2160,680 (--centres 60,...,600); 8964 160,1080,2160,1560;
8965 120,350,2160,1230; 8966 160,330,2160,1230 (automatic line finding on the others; regions set from 600 px thumbnails).
No subagent. The volunteer text agrees with the image on every code word except: N2-AW "Gauly" twice (volunteer Ganley),
"Walkem" (image Walkem or Walkim, kept as Walkem[?]). On p.60 four lines were seen only in part on the crops (their upper
halves); their words are taken from the volunteer text, which agrees on every word visible; the last line ("touched at
Granada ... Wedlock Lamb") was not on a crop and rests on the volunteer text alone.

Result (ciphertext-no2.txt N2-AS..AY; reading-no2.md "Seven entries of pages 56-74"): code-word tokens H 237, C 9, I 4, M 0.
All seven located in print: N2-AT OR I/33 p.1002-1003; N2-AU OR I/36 pt 2 p.352 (OCR damaged; the legible words agree);
N2-AV OR I/36 pt 2 p.781; N2-AX OR I/36 pt 2 p.907 (also I/37 pt 1 p.493); N2-AW OR I/37 pt 1 p.493; N2-AY OR I/36 pt 3 p.4;
N2-AS in Grant Papers vol. 10 by IA full-text snippet (page not established), not located in OR I/33 by phrase or by
date/correspondent (25 Apr, Burnside to Grant). A search result only. key-no2.md section 8 gains five clerk's forms at C
(tablation, Suggestions, wigs, Clark, Walkem). Logged, not resolved (reading-no2.md): N2-AT "yawl" where the OR has a
sentence break (the book's Yawl = Signed; marked plain); N2-AT "Abbotts" is the plain name, not D12-E1's Abbott = James
(marked plain); N2-AW religion = operations (a further witness for the inferred Religion = Operations); time words against
the OR: N2-AS 10.30 PM (pencil "Sent at 1040pm"), N2-AX 9.30 PM (OR 10 p.m.), N2-AY 2 PM (OR 2 p.m., ledger header 1.45);
N2-AY "austin yoke" = 300 against the OR's 3,000, and its second Castor = Fredericksburg where the OR prints Rappahannock.
`python3 decode_no2.py --check` exit 0. Requests: hdl.huntington.org 16 (8 item-info, 8 images; all
200), archive.org 4 (djvu I/33, I/36 pt 2, I/37 pt 1, I/36 pt 3; all 200), be-api.us.archive.org 4 (PUSG vol. 10 full text,
all 200). These readings postdate AUDIT.md: a verifier pass on N2-AS..AY is needed before any is described outside the repo.

## D4-E5 (7 Oct 2026, account 4, for LANE DEFAULT-account-4-20261007-1335): seven "(No 2)" entries of pages 86-105 read (N2-AZ..BF)

Step checked undone first: no N2 block for pointers 8978 (entry 1), 8983, 8986, 8988, 8989 (entry 1), 8996 (entry 2), no ROOM done
line for them (no2-candidates.tsv status empty). Route: Huntington CONTENTdm `dmGetItemInfo/p16003coll11/<pointer>/json` (volunteer
text, field `transc`) for 8978, 8979, 8983, 8986, 8987, 8988, 8989, 8990, 8996, 8997, 8998 and IIIF
`hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg` for 8978, 8983, 8986, 8987, 8988, 8989, 8990,
8996, 8997 (scratch, regenerable; 8987, 8990 and 8997 carry the ends of the entries on pp.94, 97 and 104; 8979 and 8998 were fetched
only to confirm that pp.86 and 105 end their entries). Crop step, run before reading (S = scratch):
`python3 tools/iiif_lines.py --image $S/img/p<pointer>.jpg --out $S/crops/<dir> --prefix <p> --region <x,y,w,h> [--centres ...]
--lines-per-crop 3|1 --max-width 2400` with 8983 `120,200,2200,1520` (automatic; header and last line cut as two single strips);
8986 `200,200,2120,1400` --centres 60+89k (k=0..14) and `200,1400,2120,1240` --centres 70+89k (k=0..12), plus single-line strips
at 1460 and 1540; 8987 `200,120,2120,500` --centres 70+89k (k=0..4) and `200,500,2120,300` --centres 60,150,240; 8988
`150,150,2250,1550` (automatic) and `150,1660,2250,130`; 8989 `150,1400,2250,1300` (automatic); 8990 `150,270,2250,1000`
(automatic); 8996 `150,1730,2250,900` (automatic); 8997 `150,170,2250,1760` (automatic); 8978 `150,680,2250,1990` --centres
77,162,255,...,1890 and `150,2580,2250,190`. Regions set from 500-600 px thumbnails. Crops read by the worker at 1500 px width,
stacked per page; no subagent.

The volunteer text agrees with the image on every word except: N2-AZ "wiley" before Comb (on the image, missing from the volunteer
text); N2-BA "Harriet" (image Harnet or Hamit; the time word Harriet is kept, it agrees with the OR's 1.30 p.m.); N2-BD header
"S. P. Kimber" (volunteer L. P.) and "Chant" (volunteer Chart); N2-BE "whiffs" (volunteer whiff); N2-BB "Pene" and "Dorming" as the
volunteer reads them, image agrees. The last line of p.86 ("Soften of Allatona pass ... Flannel Comet") was seen on its crop only in
its lower half, with the thumbnail and the volunteer text agreeing on every word; the OR prints the same sentence.

Result (ciphertext-no2.txt N2-AZ..BF; reading-no2.md "Seven entries of pages 86-105"): code-word tokens H 292, C 15, I 14 (all
yard/stick), M 0 (65-entry total from the decoder: H 1546, C 65, I 54, M 2). All seven located in print, word for word apart from
the ledger's spelling and the conflicts in reading-no2.md: N2-BA OR I/34 pt 4 p.424-425; N2-BB OR I/40 pt 2 p.117 and I/37 pt 1 p.645;
N2-BC OR I/37 pt 1 p.650-651; N2-BD OR I/34 pt 4 p.528; N2-BE OR I/37 pt 2 p.119; N2-BF OR I/36 pt 3 p.569-570; N2-AZ (the Barnard
message to Dana, signed Comb = Secretary of War) not located in OR I/36 pt 3, I/37 pt 1-2, I/40 pt 2 or I/34 pt 4 by phrase, located
in The Papers of Ulysses S. Grant vol. 11 by Google Books API snippet (page not established). A search result only. key-no2.md
section 8 gains six clerk's forms at C (Dorming, Pene, plantation, Meridians, Mindins, Sprage). Plain words and conflicts are listed
in reading-no2.md. `python3 decode_no2.py --check` exit 0. These readings postdate AUDIT.md: a verifier pass on N2-AZ..BF is needed
before any is described outside the repo.
Requests: hdl.huntington.org 20 (11 item-info, 9 images; all 200), archive.org 5 (djvu I/34 pt 4, I/36 pt 3, I/37 pt 1, I/37 pt 2,
I/40 pt 2; all 200), www.googleapis.com 3 (Books API, all 200).

## D4-E5H (7 Oct 2026, account 4, for LANE DEFAULT-account-4-20261007-1335): N2-AJ header time corrected, noon -> midn
D4-V2AJ's flag (ROOM 13:54 UTC): the p.18 (pointer 8910) N2-AJ header reads "12. midn", not "12. noon". Checked independently on one
IIIF region fetch, `hdl.huntington.org/digital/iiif/p16003coll11/8910/4800,5050,700,250/full/0/default.jpg` (native resolution,
scratch): "12. midn" -- m, dotted i, looped d, n. Corrected in ciphertext-no2.txt (block title and header line), reading-no2.md
(summary table row, conflicts line, regenerated block title); `python3 decode_no2.py --write` then `--check` exit 0. The 9 code words
and their grades are unchanged. Effect: the time word Viola = 12 midnight PM now agrees with the header, so the noon/midnight conflict
logged by D12-E1 and by D12-VP section 5 is void (a transcription slip of the plain header, not a key or ledger conflict).
status.json, PROGRESS.tsv and SECOND-OPINIONS-QUEUE.tsv quote no N2-AJ "noon" (grep); the SO prompt was already corrected by
D4-V2AJ. Rule 10 propagation into D12-VP's sections 3-5 is left to the next verifier (flagged in ROOM). Requests: hdl.huntington.org 1 (200).

## LS-PRE (7 Oct 2026, account 1, for LANE ST-LEDGER): which mssEC 19 entries have no Official Records hit

Filter before anyone decodes; nothing was decoded. Tool: `tools/huntington_transc.py` (shared; offline test
`tools/tests/test_huntington_transc.py`). The 415 page pointers of object 9302 come from `dmGetCompoundObjectInfo` (8887-9301; page n =
pointer - 8892, verified at both ends: 8893 = "Page 1", 9301 = "Spine"); the volunteer text (`transc`, 405 pages with text) is committed
as `sources/mssEC19/p<pointer>.json` (text only, 1.7 MB). Segmenter, plain-token OR check and calibration: `entries_mssEC19.py`
(`python3 entries_mssEC19.py --or-dir <scratch> --cache <scratch>/or_full.json`). Output: `entries-mssEC19.tsv` (893 segments: headers
with a date, plus run-ons at the top of a page as entry 0; columns as briefed plus `or_cov`).

**OR check.** Plain tokens = every token not in the code-word column of a key table of key.md, key-no2.md or key-no9.md, with a list of
function words always kept plain (to, in, the, and, ... are listed in the keys). Rare 3-grams of plain tokens (seen at most 40 times in
the whole scanned corpus) are looked up in the IA full text; `or_hit` is set when the hits inside one 400-token window cover at least 7
distinct plain tokens of the entry (`or_cov`, recorded for every row). Volumes scanned (IA `_djvu.txt`, to scratch, 58 files): OR ser. I
vols 32-52 as `warofrebellion<vol><part>unit` (see the identifier caveats below), `warofrebellionco0043unit_i5n6`,
`warofrebellionco0047unit_e7s2`, `warofrebellionco0047unit_q8d9`, `warofrebellion501unit`, `502unit`, `53unit`, and ORN ser. I vols 9
and 10 (`officialrecordso0009unse`, `officialrecordso0010unse`). Series III vols 4-5 were NOT searched: the IA copies found
(`in.ernet.dli.2015.165578`, `.171703`) have no `_djvu.txt` (HTTP 404) and `waroftherebellio026242mbp` turned out to be Series II vol IV
(removed); no IA identifier for ser. III vol 5 was found. ORN vols 11-12 were not fetched.

Identifier caveats (volume/part read from each file's own title page and its date profile): `warofrebellion323unit` is I/32 pt 3 (title
page OCR "XXXIX"); `warofrebellion431unit` is I/47 pt 2 (Jan-Mar 1865 dates, title page "XLVII"), NOT I/43 pt 1; `432unit` is I/43
pt 2; `warofrebellionco0043unit_i5n6` is a I/43 volume (Sep-Dec 1864) added to cover the missing pt 1; `502unit`, `522unit` have OCR
title pages "I", "III" but are the supplement parts 50 pt 2 and 52 pt 2 by date profile. `warofrebellion423unit` and `53unit` carry no
readable title page. Per-file date profiles are in the session scratch only.

**Calibration (rule 3).** On the 98 already-read entries that the pointer + date match could place (ciphertext.txt E1-E20,
ciphertext-no2.txt, ciphertext-no9.txt; truth = the repo's own tables, a search result and not a verdict): recall 41/50 = 0.82 of the
entries logged as printed in the OR (0.90 for entries of 60 words or more, 28/31; 0.68 below 60 words, 13/19: a short entry has few plain tokens to match); false hits 0/14 of the entries logged "not located". The margin is thin: the
not-located entries covered 3-6 plain tokens against the threshold of 7 (N2-D 6, O9-E 6, O9-V 6), so a lower threshold would start
to hit them; an entry at `or_cov` 4-6 with no `or_hit` is not clean. The "not located" side is only 14 entries and each is itself a
search result. Recall above 0.7, so this is a ranking with a stated error rate, not a verdict (rule 10). Nine known-printed entries
were missed (N2-AG, Z, AO, AP, AU, G; O9-C, D, H; `or_cov` 3-6). `cipher_guess` (1/2/9 by leave-one-out Bayes over key-table tokens, trained on the
same already-read entries; `clear` under 12% key-table tokens; `short` under 6 words) is right on 75 of 98; treat it as a hint.

**Counts (893 segments).** priority 1 (cipher, no `or_hit`, not read, operator not at an army commander's headquarters; the sender is
inside the cipher so Beckwith/Kimber/Canby/Grant/Halleck/Lincoln/Stanton in the header are the proxy): 308 (guess No. 1: 261, No. 2: 39,
No. 9: 8); of these 159 have a 1864 date and 149 a 1865 date. priority 2 (cipher, no `or_hit`, not read, but a headquarters operator): 91
(No. 1: 38, No. 2: 40, No. 9: 13). priority 3 (an `or_hit`, already read, clear, or under six words): 494, of which 98 are the
already-read entries, 38 `clear`, 28 `short`. Entries dated after about June 1865 cannot have an OR hit in the volumes scanned (ser. I
ends there); their priority-1 rank is by construction, not by search.

Requests: hdl.huntington.org about 420 (2 compound-object, about 417 item-info incl. one dropped connection retried once, 3 probes; all
200 but that one); archive.org about 71 (5 advancedsearch, 3 metadata, 1 HEAD, 62 `_djvu.txt` download attempts of which 59 returned
200; one 500 on `warofrebellion361unit` retried once, 200; two 404 for the `in.ernet.dli` copies, not retried). Other hosts: none.

## Remaining gaps (LS-PRE, 7 Oct 2026)
Read so far: 98 of 893 mssEC 19 segments read (the already-read E, N2 and O9 entries matched by pointer and date; `decode.py`, `decode_no2.py`, `decode_no9.py --check` unchanged by this pass); 308 priority-1 rows unread.
- priority-1 rows of `entries-mssEC19.tsv` (308) - blocker: not-attempted; read in order of lowest `or_cov` with key.md, key-no2.md or key-no9.md as `cipher_guess` says; next: one chunk of 8 rows, ~$10
- OR check without Series III vols 4-5 and ORN vols 11-12 - blocker: not-attempted; no IA copy with OCR text found for them; next: find IA identifiers with `_djvu.txt` and rerun `entries_mssEC19.py --rerun`, ~$0.5

## Escalation (LS-PRE, 7 Oct 2026)
- [x] siblings: mssEC 25 second copy read for E4/E5 earlier (Second reader, 24 Sept 2026); this pass adds the whole ledger's entry list, no sibling reading
- [n/a] clear-pages: the ledger text is the cipher itself, the OR check above is the print comparison
- [x] known-keys: key.md (mssEC 41), key-no2.md (mssEC 47) and key-no9.md (mssEC 67) are the period books in use
- [ ] print: OR check run for ser. I vols 32-52 and ORN 9-10 only; Series III vols 4-5 still to add, ~$0.5
- [n/a] key-rebuild: period cipher books exist for the three vocabularies in the ledger
- [n/a] image-check: nothing was read in this pass, so no token to image-check
- [n/a] retry: no read attempted and no failed attempt to retry
Verdict: keep going: 2 internal gaps; cheapest next: a verifier pass on E47-E54 (LS-R4, 8 Oct 2026: eight entries read, H 104, C 1, I 1, `decode.py --check` exit 0; 2 located in print, OR I/37 pt 1 p.891 (E48) and OR III/4 (E53), 6 not located in what was searched), then the parked E30-E36 and the next priority-1 rows, ~$0.6 per entry. Earlier: keep going: 2 internal gaps; cheapest next: a verifier pass on E37-E46 (LS-R3, 8 Oct 2026: ten entries read, H 161, C 1, `decode.py --check` exit 0; 1 located in print, ORN I/11 p.68 (E44), 9 not located in what was searched), then the parked E30-E36 and the next priority-1 rows, ~$1 per entry. Earlier: keep going: 2 internal gaps; cheapest next: the next priority-1 rows of `entries-mssEC19.tsv` (LS-R1 read nine as E21-E29: 3 located in print (ORN I/26, OR III/4 + FRUS 1864, OR I/37 pt 2), 6 not located in what was searched, so the filter halves the printed share against D4-E5/D12-E3), ~$1.1 per entry, and a verifier pass on E21-E29 (updated LS-R1, 7 Oct 2026: H 173, C 3, M 2, `decode.py --check` exit 0). Earlier: keep going: 2 internal gaps; cheapest next: add Series III vols 4-5 to the OR check (~$0.5), then read the lowest-`or_cov` priority-1 rows of `entries-mssEC19.tsv`, ~$1.2 per entry (updated LS-PRE, 7 Oct 2026: recall 0.82 and false hits 0/14 on the already-read entries).

## LS-R1 (7 Oct 2026, account 1, for LANE ST-LEDGER)

Nine entries picked by LS-PRE's filter (entries-mssEC19.tsv priority 1, no OR hit, `or_cov` <= 3, 1864, non-headquarters
addressees) read with key.md (Cipher No. 1) as E21-E29 in ciphertext.txt; reading.md summary rows and derived block.
All nine are Cipher No. 1 (key.md reads every code-word token but the ones listed below; no entry needed key-no2.md or
key-no9.md). `python3 decode.py --write` then `--check` exit 0. Rows marked `already_read` in entries-mssEC19.tsv (with
8935/43/0, the run-on of E21).

| ID | date | from / to (decoded plain) | H | C | I | M | found in print / not located in |
|---|---|---|---|---|---|---|---|
| E21 | 19 Apr 1864 1 PM | Meigs (QMG) to Lt. Col. H. S. Biggs, Fort Monroe | 37 | 0 | 0 | 0 | not located in OR I/33 (which prints Meigs to Wise of 16 Apr and Wise's list of 19 Apr, p.915), I/36 pts 2-3, I/42-43 (IA djvu, phrase grep); IA full text and Google Books "Van Vliet has chartered": no hit |
| E22 | 26 Apr 1864 12.30 | Welles to Porter via Capt. Pennock, Cairo | 21 | 0 | 0 | 0 | ORN I/26 p.92 (IA `officialrecordso0026unse`), word for word |
| E23 | 2 May 1864 9 PM | G. V. Fox to Col. H. S. Olcott, New York | 7 | 0 | 0 | 0 | not located in the IA djvu set above or by Google Books ("Solicitor Whiting gave his opinion", "commissioned to investigate only, not to prosecute"); IA full text 502 twice, not run |
| E24 | 18 May 1864 | Seward to C. F. Adams (London), copy to Dayton (Paris) | 9 | 0 | 0 | 0 | OR ser. III vol 4 (1900) and Papers relating to Foreign Affairs 1864 (Google Books snippets "fabricators and publishers of the spurious proclamation"; page not fixed) |
| E25 | 29 July 1864 12.30 PM | Halleck to Wallace, Baltimore | 13 | 3 | 0 | 1 | OR I/37 pt 2 p.501 (12.20 p.m.), word for word but "pike" (absent from the OR) |
| E26 | 21 Aug 1864 1.30 PM | Stanton to Dix, New York | 24 | 0 | 0 | 0 | not located in OR I/42 pts 2-3, I/43 pts 1-2 (djvu grep "Walker street", "disguised as"), Google Books ("42 Walker street" Dix; "disguised as hardware"), IA full text ("Walker street" "copperheads": no relevant hit) |
| E27 | 10 Oct 1864 | Judge Advocate L. C. Turner to 'beverage' (unread), New York | 14 | 0 | 0 | 1 | not located: djvu grep "Gemmell", "Miss Gardner", Google Books and IA full text ("James Gemmell" "Old Capitol"; "Jewett and Siebert"): no hit |
| E28 | 11 Oct 1864 11.30 AM | F. W. Seward to Thurlow Weed, New York | 15 | 0 | 0 | 0 | not located: djvu grep "Thurlow Weed", Google Books ("proxy of the sailors", "Mississippi squadron will put a boat"), IA full text "proxy of the sailors": no hit |
| E29 | 5 Nov 1864 4 PM | Dana to Dix, New York | 33 | 0 | 0 | 0 | the telegram not located (OR I/43 pt 2 djvu: no "Dudley Harris"); its content is in print: Confederates Downeast (1985) names Dudley Harris of Portland with the aliases Spencer and Barbour and Colonel Martin of Boston (Google Books snippet; whether it quotes this telegram not established); Maine (1990) snippet likewise |

Grades: the decoder counts H 175, C 3 over E21-E29; by hand, three of its H tokens are moved: E25 "pike" (book: Cut off;
the OR text, "your cavalry, a battery", has no word for it) H -> M; E27 "Grunt" (book: Warrenton, printed one line below
Grapes/Growl = Washington, in the place-of-origin slot of a Washington message) H -> M; E28 "Pilgrim[?]" (image "Pelgrim",
book Pilgrim = Captain; Pennock was a captain) kept H with the flag. Net: H 173, C 3, I 0, M 2 (the table above). E27's
addressee word "beverage" is not in key.md: unread, not graded. Two key.md section 7 rows added at C from OR I/37 pt 2 p.501:
Squase = Infantry, Samson = Ferry (the book's Sampson). Plain-word judgements (a `plain:` line, not graded): E21 chart
(chartered), Helen, Richland (vessel names); E23 Whiting (the War Department solicitor), Fox (the signer); E24 Francis Adams,
publishers; E25 White (Elijah White); E26 Walker (No. 42 Walker St, New York); E27 harem (Harlem); E28 squadron; E29 hair,
Spencer, Taylor (names).

Image vs volunteer text (image taken in every case): E22 "despatch" (volunteer dispatch); E24 "publishers" (publishing);
E25 "Ed - wards" (Ed - monds); E26 "sutton" (sultan; Sutton = Information in the book); E28 "Pelgrim" (Pilgrim, kept as
Pilgrim[?]); E29 "Person" read as written though the image is closer to "Psrson". E23's signature "Sig G. Fox Asst" is
partly overwritten in darker pencil on the page, readable. Pencil glosses in a later hand above E22 and E24 ("(hand) (the)
(event)", "(point) (prisons) (mutton)", numbers) are not ledger text and were not transcribed. Page numbers in the block
headers are the ledger's printed numbers (pp.159, 197, 221 are image pages 161, 199, 223 in entries-mssEC19.tsv).

Crop commands (S = session scratch; images `hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg`
fetched once to $S/img; regions set from 500 px thumbnails; crops read by the worker, no subagent):
`python3 tools/iiif_lines.py --image $S/img/p<pointer>.jpg --out $S/crops/<pointer> --prefix p<pointer> --region <x,y,w,h>
--centres 50,150,...(100 px pitch) --lines-per-crop 4 [--top-margin 70] --max-width 2400` with 8934 `0,1950,2400,830`, 8935
`0,120,2400,1200` (+ single strip `0,440,2400,160` --centres 80), 8949 `0,1300,2400,1520`, 8955 `0,950,2400,1650`, 8964
`0,0,2400,850` (+ `0,780,2400,280` --centres 60,160), 9023 `0,1050,2400,1000`, 9053 `0,100,2400,1400` (+ `0,1420,2400,330`),
9091 `0,100,2400,1780`, 9115 `0,930,2400,1200`. The automatic line finder found 0-4 lines on these faint pencil pages, so
fixed centres were used.

Requests: hdl.huntington.org 9 (IIIF images, all 200; the volunteer text came from the committed sources/mssEC19); archive.org
10 (djvu: I/33, I/37 pt 2, I/43 pts 1-2, I/42 pts 2-3, I/36 pt 3, ORN 26: 200; one 503 on a mis-guessed identifier, not
retried; 1 advancedsearch); be-api.us.archive.org 11 (fts; 4 answered 502, one retry each, E23 failed twice and was dropped);
www.googleapis.com 18 (Books API with key and country=US; 2 answered 503, retried once, 200). Report what was found and where
it was not found; novelty is a verifier's (rule 10): batch flagged for LS-V1.

## ST-LEDGER parked entries (8 Oct 2026 00:2x UTC, LANE ST-LEDGER, account 1)
The seven priority-1 entries assigned as E30-E36 (pointers/page/entry 9051/159/1, 9051/159/2, 9054/162/1, 9055/163/0, 9056/164/0,
9057/165/3, 9060/168/1; McCaine in the Shenandoah Valley, Aug 1864) were given to two solver sessions (LS-R2, LS-R2b, 7 Oct 2026); both
ended without a commit, so nothing of them is on origin and the IDs E30-E36 are unused. They were read on 8 Oct 2026 as E30-E36: see "## LS-R2c (8 Oct 2026, account 1, for LANE ST-LEDGER-2)" below.

## LS-R3 (8 Oct 2026, account 1, for LANE ST-LEDGER)

Ten priority-1 entries of `entries-mssEC19.tsv` (no OR hit in LS-PRE's filter; Horner at New York, Sheldon at Fort Monroe, Sampson at
Baltimore) read with key.md (Cipher No. 1) as E37-E46 in ciphertext.txt; reading.md summary rows and derived block. All ten are Cipher
No. 1: key.md reads every code-word token but the unread words listed below, so no entry needed key-no2.md or key-no9.md. `python3
decode.py --write` then `--check` exit 0. Rows marked `already_read` with LS-R3 and the ID.

| ID | date | from / to (decoded plain) | H | C | I | M | found in print / not located in |
|---|---|---|---|---|---|---|---|
| E37 | 2 Nov 1864 9.30 AM | J. B. Fry (Pro. Mar. Genl) to Capt. B. F. Manierre, Provost Marshal 8th District, New York, and to W. E. Dodge | 22 | 0 | 0 | 0 | not located as a telegram: Google Books (3 queries, "Manierre" + "withdraw as a candidate for Congress" etc.) gave only a New York Times Index entry (snippet empty) on Manierre and the candidacy |
| E38 | 12 Aug 1864 11 PM | Seward (signed Secretary of State) to John G. Palfrey, Postmaster, Boston | 13 | 0 | 0 | 0 | not located: Google Books ("Alex Keith" Ferris remittance Halifax; "North Market street" Ferris Keith; "Gordon, Bruce"), IA full text ("No. 10 North Market" Ferris; "Alexander Keith, jr." remittance Ferris): no hit on the telegram (one IA hit names Keith as the rebel agent, another item) |
| E39 | 12 Aug 1864 11.30 PM | Seward to Abraham Wakeman, Postmaster, New York | 22 | 0 | 0 | 0 | not located: the same searches, and Google Books "Abraham Wakeman" Keith remittance Halifax: no hit |
| E40 | 13 Aug 1864 3 PM | Seward to Robert Murray, U.S. Marshal; George Harrington, Acting Sec. of the Treasury, to Hiram Barney, Collector, New York | 12 | 0 | 0 | 0 | not located: Google Books ("Detain the schooner Princess": 1846/1858 documents only, another vessel; schooner Princess Murray marshal Harrington 1864: 0) |
| E41 | 15 Oct 1864 8 PM | F. W. Seward to C. A. Seward, 29 Nassau St, New York | 10 | 0 | 0 | 0 | not located: Google Books ("Tassara" "Minor" "Savage" Havana Evarts 1864: 0) |
| E42 | 25 Apr 1864 | Meigs to Lt. Col. H. Biggs, Quartermaster, Fort Monroe | 28 | 0 | 0 | 0 | not located: OR I/33 djvu (`warofrebellion33unit`) grep "saddle horses", "winds and waves", "Rucker informed": no hit; Google Books "winds and waves control": poetry and modern only |
| E43 | 29 May 1864 5.30 PM | Rucker to Col. Biggs, Fort Monroe | 19 | 1 | 0 | 0 | not located as a telegram: OR I/36 pt 3 (`warofrebellion363unit`) prints Biggs' answer of 30 May 8.30 PM ("Tell General Rucker will return the City of Albany and Ranger"; index: City of Albany p.367), not this; Google Books finds only that reply |
| E44 | 15 Nov 1864 8.30 PM (ORN: 16 Nov) | G. V. Fox to Porter (Niagara), Hampton Roads | 15 | 0 | 0 | 0 | ORN I/11 p.68 (`officialrecordso0011unse`), word for word, dated Washington, November 16, 1864 (the date word Gas = 16 agrees with the ORN; the ledger header says 15th) |
| E45 | 29 Nov 1864 10.45 AM | Rucker to Col. Newport, Chief Quartermaster, Baltimore | 11 | 0 | 0 | 0 | not located: OR I/42 pt 3 (`warofrebellion423unit`) grep "Newport, chief", "available steamer(s) and propeller(s)": no hit; Google Books: no hit |
| E46 | 30 Nov 1864 12.30 | signature unread ("M wise well wily Govr") to John A. Kennedy, Supt of Police, New York | 9 | 0 | 0 | 0 | not located: OR I/43 pt 2 (`warofrebellion432unit`) grep "chief conspirator", "burning of New York", "Old Capitol Prison" (other items only); Google Books: no hit |

Grades: the decoder counts H 161, C 1 over E37-E46 (the C token is E43 "mangled" = telegraphed, key.md section 7); no token moved
by hand, so H 161, C 1, I 0, M 0. Hand notes on H tokens: E39 "perfume" is printed [3] by the decoder (key.md's numeral row overrides
the arbitrary row in the lookup), but the book's other row, Perfume = By the way of (p.18 l.24 R), is what the context reads ("Gordon
Bruce & Co, New York, by way of St John", two lines after "Halifax peasant St John"); H either way, the choice is the reader's. E43
"Windsors[?]" (the image is unclear, the volunteer text has Windsors) read as Windsor = River with the flag; "windpipe" = River two
lines later in the same entry agrees. E44's "Shaky" is not in key.md and stands in clear in the ORN print ("shaky steamer"). Unread
words not in key.md, left as written and not graded: E37 "Wreath" (answer by Wreath), E43 "Waymorners" (Waymorners Coal; key.md has
Wayworn = Steam), E40 "nick" (examine her cargo and nick). Header conflicts: E44 ledger 15th vs date word 16 (ORN 16); E45 time word
Fanny = 11 AM vs the volunteer text's header time 10.45 (the note above the header was cut on the crop). Plain-word judgements
(`plain:` lines): E37 Dodge (W. E. Dodge; book McMinnville); E38 John, Johns, watch; E39 John, Johns, Hunter, person, trade; E40
Princess (the schooner; book Captain); E41 Hunter (Wm Hunter, chief clerk); E42 saddle (saddle horses; book Guard); E43 White (White
House; book Report); E44 Fox (the signer).

Image vs volunteer text (image taken in every case): E37 "Pro Mar Shelby" (volunteer "Two Mar"); E40 "U S D Marshal" (NS Marshal),
"Seward[?]" (Benard; the capital is a looped S, the rest close to "eward", flagged), "U S Mar shall" (NS Man shall); E43 "P monchie"
in the last line (monarchic); E45 "sligo" (slign); E46 "bring" (being) written as on the page. E38 "hang" struck through, as the
volunteer text has it. The ledger's printed page numbers are in the block headers (image pages in entries-mssEC19.tsv run two
higher from p.200 on, 9097 = p.203; 9045 = p.152).

Crop commands (S = session scratch; images `hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg` fetched
once to $S/img; regions set from 320-500 px thumbnails; crops read by the worker at 1400 px, no subagent; the automatic line finder
found 0 lines on 9045, so fixed centres were used throughout): `python3 tools/iiif_lines.py --image $S/img/p<pointer>.jpg --out
$S/crops/<dir> --prefix p<dir> --region <x,y,w,h> --centres <c0+pitch*k> --lines-per-crop <n> --max-width 2400` with 9045
`150,280,2200,2420` centres 50+96k (k=0..24), 4 per crop; 9046 `100,230,2250,850` 40+100k (k=0..7), 4, and `100,960,2250,280` 60,160;
9110 `100,1800,2250,900` 60+97k (k=0..8), 5; 9111 `100,190,2250,400` 60,160,260,350; 9097 `100,1360,2250,620` 50+100k (k=0..5), 6;
8945 `100,1880,2250,950` 60+95k (k=0..9), 5; 8975 `100,160,2250,950` 50+97k (k=0..9), 5, and `100,1060,2250,200` 70; 9124
`100,1480,2250,1050` 60+97k (k=0..9), 5; 9129 `100,1240,2250,480` 50+97k (k=0..4), 5; 9130 `100,1400,2250,480` 50+97k (k=0..4), 5 and
`100,1750,2250,760` 50+97k (k=0..7), 4.

Requests: hdl.huntington.org 10 (IIIF images, all 200; the volunteer text came from the committed sources/mssEC19); archive.org 5
(djvu I/33, I/36 pt 3, I/42 pt 3, I/43 pt 2, ORN I/11; all 200); be-api.us.archive.org 3 (fts, all 200); www.googleapis.com 15 (Books
API with key and country=US, all 200). Report what was found and where it was not found; novelty is a verifier's (rule 10): batch
flagged for LS-V3.

## LS-R4 (8 Oct 2026, account 1, for LANE ST-LEDGER)

Eight priority-1 entries of `entries-mssEC19.tsv` (Sheldon at Fort Monroe, Sampson at Baltimore, Van Duzer at Nashville) read with
key.md (Cipher No. 1) as E47-E54 in ciphertext.txt; reading.md summary rows and derived block. All eight are Cipher No. 1: key.md reads
every code-word token but the unread words listed below, so no entry needed key-no2.md or key-no9.md. `python3 decode.py --write` then
`--check` exit 0. Rows marked `already_read` with LS-R4 and the ID.

| ID | date | from / to (decoded plain) | H | C | I | M | found in print / not located in |
|---|---|---|---|---|---|---|---|
| E47 | 6 Apr 1864 3.30 PM | Meigs (QMG) to Lt. Col. Biggs, Fort Monroe: send the Salvor to Annapolis, 1,000 tons of coal afloat at Fort Monroe for Hilton Head | 13 | 0 | 1 | 0 | not located: OR I/33 (`warofrebellion33unit`) grep "Annapolis, if still", "tons of coal", "replace it from the", "Hilton Head. Advise" (Salvor appears only in other items, index p.814); Google Books ("Send Salvor to Annapolis"; Salvor Annapolis Meigs Biggs coal Hilton Head): no relevant hit; IA full text "Salvor to Annapolis": 0 (first try 502, one retry) |
| E48 | 5 May 1864 11.30 AM | Halleck (signed General-in-Chief) to Wallace, Baltimore | 20 | 0 | 0 | 0 | OR I/37 pt 1 (`warofrebellion371unit`) p.891 (page from the OCR running heads 892-893 that follow), word for word but "of Ohio militia", which has no ledger word |
| E49 | 12 June 1864 4.10 PM | Meigs (signed Qr Master Genl) to Biggs, chief quartermaster, Fort Monroe: an expedition 16,000 strong to embark at White House tomorrow | 4 | 0 | 0 | 0 | not located: OR I/36 pt 3 (`warofrebellion363unit`, prints Biggs' May letters only) and I/40 pt 2 (`warofrebellion402unit`) grep "sixteen thousand", "16,000 strong", "new base or hospital", "removing stores", "embark at White House"; Google Books (2 queries) and IA full text ("sixteen thousand strong is to embark"): no hit. **Correction (AUD2-LS-E, 8 Oct 2026): the substance is printed in OR I/36 pt 3 p.769 (Pitkin to Meigs, White House, 12 June 1864, received 2.15 PM: water transport for 16,000 troops tomorrow, all suitable vessels), which E49 relays; class N2** |
| E50 | 11 Aug 1864 11.30 AM | Meigs (signed Qr Master Genl[?]) to Col. Biggs, Fort Monroe: provision the Continental to bring the General-in-Chief's dispatch from the Department of the South | 17 | 0 | 0 | 0 | not located: OR I/42 pt 2 (`warofrebellion422unit`) prints a related order ("I have ordered Continental to Fort Monroe ... through Colonel Biggs", index p.102), not this telegram; grep "hour of sailing": no hit; Google Books: no hit |
| E51 | 21 Oct 1864 11 AM | William Henry Whiton to Adna Anderson, Government Railroads, Nashville: accept the proposed Inspector-Generalship | 11 | 0 | 0 | 0 | not located: OR I/39 pt 3 (`warofrebellion393unit`) grep "Adna Anderson", "Whiton", "inspector-generalship" (Anderson appears as superintendent of military railroads in other items); Google Books ("Adna Anderson" "Whiton": a later court record names the two together, not this telegram) |
| E52 | 7 Nov 1864 11.30 AM | C. A. Dana to Wallace ('Submit'), Baltimore: a rebel agent calling himself Dr Hamilton passed through Elmira going south | 9 | 1 | 0 | 0 | not located: OR I/43 pt 2 (`warofrebellion432unit`) grep "Hamilton ... Elmira", "Elmira ... Thursday", "fine teeth"; Google Books (2 queries) and IA full text ("calling himself Dr. Hamilton": one 1869 London item, another man): no hit |
| E53 | 12 Nov 1864 11.30 AM | J. C. Kelton, Asst Adjt Genl, to Maj. W. R. Price, Acting Inspector, Cavalry Bureau, Nashville | 20 | 0 | 0 | 0 | OR ser. III vol 4 (1900, serial 125), Google Books snippets "Washington, D. C., November 12, 1864. Acting Inspector, Cavalry Bureau, Nashville, Tenn.: Consolidation of the Second and Fifth Kentucky Cavalry approved. The Secretary of War authorizes enlistment of loyal Alabamians in the First Alabama Cavalry, but without bounties", word for word; page not fixed |
| E54 | 5 Dec 1864 2.30 PM | Brig. Gen. A. B. Dyer, Chief of Ordnance, to Capt. Edson, Fort Monroe: send to Hilton Head all ordnance supplies ordered for Sherman's army | 10 | 0 | 0 | 0 | not located: OR I/44 (`warofrebellion44unit`) grep "Edson", "ordnance supplies which" (a related order of the same weeks: "Lieutenant Arnold goes to Hilton Head about the ordnance"); Google Books (2 queries) and IA full text ("to hold these supplies on board"): no hit. **Correction (AUD2-LS-E, 8 Oct 2026): the substance is printed in OR I/44 p.627 (Halleck, 5 Dec 1864, copied to the Chief of Ordnance: all supplies for Sherman's army to Hilton Head, to be landed where ordered), which E54 passes on; class N2** |

Grades: the decoder counts H 104, C 1 over E47-E54 (the C token is E52 "Submit" = Wallace, key.md section 7). By hand: E47 "Vintur"
(clear on the image; key.md has Vinton = Quartermaster, and the addressee Biggs was a quartermaster) is not read by the decoder and is
counted I 1 here. E50 "Belcher[?]" (image closer to "Belchr"; volunteer text "Belsher", not in key.md) kept H with the flag. Net: H 104,
C 1, I 1, M 0. Unread words not in key.md, left as written and not graded: E48 "Season" (the addressee word before Banditti =
Baltimore; the OR print has Major-General Wallace); E50 "amirs", "ham" (zodiac Wick ham of sailing: "Report hour of sailing" reads
the sense, not graded); E51 "zbra" (zebra, period); E54 "Toby" (to be, as in E46). Plain-word judgements (`plain:` lines): E49 White
(White House); E51 question, William; E52 hair; E54 ordnance. E53 "W R[?] Price": the image looks like "W Q", the volunteer text has
WR; the OR prints Maj. W. R. Price, Asst. Insp. Gen., Cavalry Bureau (I/39 pt 3, Oct 1864). E49 is mostly in clear (4 code words);
its header time 4.10 PM agrees with the time word Julia = 4 PM.

Image vs volunteer text (image taken in every case): E50 "Belcher[?]" (Belsher); E53 "R[?]" (R). All other words of the eight
entries agree with the volunteer text; header and last lines of E49 and E53 were partly cut on the crops and read from the
volunteer text with the visible part agreeing. Pencil glosses in a later hand above E47 ("again", "day", numbers) are not ledger
text and were not transcribed. The ledger's printed page numbers differ from the image pages in entries-mssEC19.tsv from p.200 on
(9098 = p.204 on the page, image page 206); block headers carry the printed numbers.

Crop commands (S = session scratch; images `hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg`
fetched once to $S/img; regions set from 500 px thumbnails; crops read by the worker, no subagent; fixed centres throughout):
`python3 tools/iiif_lines.py --image $S/img/p<pointer>.jpg --out $S/crops/<dir> --prefix p<dir> --region <x,y,w,h> --centres <list>
--lines-per-crop <n> --max-width 2400` with 8922 `100,1900,2300,820` centres 70,180,290,395,500,615,720, 4; 8957 `100,2120,2300,700`
50+95k (k=0..6), 4, and `100,1960,2300,240` 60,165, 2; 8983 `100,1780,2300,640` 50+95k, 4; 9042 `100,280,2300,660` 50+95k, 4; 9098
`100,280,2300,520` 50+95k, 3; 9117 `100,2020,2300,640` 50+98k, 4; 9123 `100,170,2300,740` 50+98k, 4; 9135 `100,170,2300,820` 50+98k, 4.

Requests: hdl.huntington.org 8 (IIIF images, all 200; the volunteer text came from the committed sources/mssEC19); archive.org 9
(djvu I/33, I/36 pt 3, I/37 pt 1, I/39 pt 3, I/40 pt 2, I/42 pt 2, I/43 pt 2, I/44, I/45 pt 1; all 200); be-api.us.archive.org 7
(fts; one 502, retried once, 200); www.googleapis.com 15 (Books API with key and country=US, all 200). Report what was found and where
it was not found; novelty is a verifier's (rule 10): batch flagged for LS-V4.

## LS-R2c (8 Oct 2026, account 1, for LANE ST-LEDGER-2)

The seven parked priority-1 entries (McCaine in the Shenandoah Valley, Aug 1864; `entries-mssEC19.tsv` rows 9051/159/1, 9051/159/2, 9054/162/1,
9055/163/0, 9056/164/0, 9057/165/3, 9060/168/1) read with key.md (Cipher No. 1) as E30-E36 in ciphertext.txt. All seven are Cipher No. 1 and
key.md reads every code-word token, so key-no2.md and key-no9.md were not needed (the 9060 header "(No 2)" belongs to the next entry on the page).
`python3 decode.py --write` then `--check` exit 0 after each push (462fdc70 E30-E31, 135c1cad E32-E33 after one rebase over LS-R5, c499cd1f E34,
e2ab5a1d E35, 9446b901 E36). Rows marked `already_read` with LS-R2c and the ID. The two earlier sessions' stop (LS-R2, LS-R2b) was not
reproduced: no tool call was refused here; they pushed nothing, so their cause stays unrecorded.

| ID | date | from / to (decoded plain) | H | C | I | M | found in print / not located in |
|---|---|---|---|---|---|---|---|
| E30 | 20 Aug 1864 10 PM | Augur (Dept. of Washington) to Sheridan (signed Gimlet): Maj. Waite, 8th Illinois Cavalry, left Muddy Branch at noon, scout toward the Gaps, about 650 men | 22 | 0 | 0 | 0 | OR I/43 pt 1 (`warofrebellion431unit_0`), Augur to Sheridan 20 Aug, "Major Waite, Eighth Illinois Cavalry, left Muddy Branch at 12 m. to-day, on his scout toward the gaps. He has about 650 men. I directed him to carry out the orders of General Grant ..." between running heads 857 and 862 |
| E31 | 21 Aug 1864 7.30 AM | Augur to Sheridan at Charlestown: Lazelle has returned and reports Warrenton, 2,000 infantry, 500 cavalry, a large force of 10,000 | 30 | 0 | 0 | 0 | OR I/43 pt 1, "Lazelle has returned, and reports as follows ...", with "depended upon reports of citizens. I will learn more definitely and inform you", running heads 871/872 |
| E32 | 21 Aug 1864 (No 1, 10 PM) | Augur to Sheridan at Charlestown: Lazelle's information on the enemy at Culpeper; Gansevoort, 13th New York Cavalry, scouts tomorrow; 41st New York arrived from Hilton Head, about 400 men | 32 | 0 | 0 | 0 | OR I/43 pt 1, "Lazelle says he received his information concerning the enemy's forces at Culpeper from a citizen who had just left there ... forty-first New York arrived here from Hilton Head to-day, about 400 men. Two more regiments on their way", running heads 872-874; the OCR header there reads "August 27 ... 9.30 p. m." against the ledger's Aug 21 and 10 PM (image: Aug 21; OCR digit on a damaged header line, print page image not opened) |
| E33 | 22 Aug 1864 | to McCaine at Harper's Ferry: a small train of forges and wagons for the Valley left yesterday; Thayer escorted by 25th New York Cavalry (300 men); a detachment of 375 men | 27 | 0 | 0 | 0 | not located: OR I/43 pts 1-2 (`warofrebellion431unit_0`, `warofrebellion432unit`) grep "small train of", "wagons for your", "forges and other", "Camp Thayer" (the 25th New York Cavalry appears only in the brigade history); Google Books API ("small train of forges" Thayer: 14 hits, none this text) |
| E34 | 24 Aug 1864 10.30 AM | Augur to Sheridan: no news from the 8th Illinois Cavalry or Gansevoort; a refugee from Culpeper, Fitz Lee's cavalry about 3,000 and part of Longstreet's about 10,000 left to join Early | 37 | 0 | 0 | 0 | OR I/43 pt 1, Augur to Sheridan 24 Aug, "I have no news from the Eighth Illinois Cavalry, or from Gansevoort. A refugee just in from Culpeper, which place he left on Friday last, reports no forces of the enemy there, except a conscripting party ..." |
| E35 | 29 Aug 1864 | a relay of Gov. Brough's message of 28 Aug: Breckinridge advancing into the Kanawha Valley with 8,000; Heintzelman left for Chicago; one battery at Camp Dennison and three National Guard regiments at Gallipolis | 30 | 0 | 0 | 0 | OR I/43 pt 1, Brough to Stanton, Columbus 28 Aug (received 10 AM 29th), "I have reliable information of Breckinridge's advance into the Kanawha Valley with 8,000, via Lewisburg ... General Heintzelman left for Chicago this morning under your order. I have telegraphed him on the way. I have the State battery at Camp Dennison and three regiments of National Guard at Gallipolis. No general officer in the State", running heads 949/952 |
| E36 | 29 Aug 1864 8 PM | relay of a dispatch from Columbus to the Secretary of War; reports from Gallipolis; the return of the 100-days men leaves the Valley open; sent to Beckwith and McCaine | 14 | 0 | 0 | 0 | not located: OR I/43 pts 1-2 grep "leaves the valley open", "100-days", "and careful", "Following just received" (only unrelated hits); Google Books (2 queries, 0 hits) |

Grades: the decoder counts H 192, C 0 over E30-E36 (22+30+32+27+37+30+14). I/M by hand 0, but the unread tail words are not graded:
the clerk's closing group of E32 "ax saw" and E33 "ax saw", E36 "wolves" (written over the struck "signed"), E33 "Camel" (Camp?) and "Quicken ment".
Plain-word judgements (`plain:` lines): E30 directed; E32 Lazelle, citizen, places; E33 small train, Thayer; E34 Friday, Sperry, stockade,
letter; E35 Paxton, Dennison, Chicago; E36 careful. Decoded names agree with the printed OR names where located (Augur, Lazelle, Waite,
Gansevoort, Fitz Lee, Longstreet, Early, Breckinridge, Heintzelman, Brough).

Image vs volunteer text (image taken): E34 "federal out" (volunteer "on"); E33 "No Sir" kept; E30 header line "No 1 10 PM" read from the volunteer text.
Not every line was read at crop resolution: the displayed crops showed about three of each four lines (E30 and E31 nearly complete, E32
lines 1-6, E33 lines 1-6, E34 lines 1-4 and 9-14, E35 lines 1-7 and 8-9, E36 lines 1-4); the remaining lines rest on the volunteer text
checked against the 500 px page view, where the two agreed everywhere visible. The ledger's printed page numbers (157, 160-163, 166) differ from
the image pages in entries-mssEC19.tsv; block headers carry the printed numbers.

Crop commands (S = session scratch; images `hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg`, fetched once each):
`python3 tools/iiif_lines.py --image $S/img/p<pointer>.jpg --out $S/crops/<dir> --prefix <x> --region <x,y,w,h> --centres <list> --lines-per-crop <n>
--max-width 2400` with 9051 `100,330,2300,1450` centres 90,210,330,440,550,670,780,900,1025,1140,1255,1350 (3) and `100,1780,2300,1000` 60+100k (3);
9054 `100,300,2300,800` 75,150,228,300,377,454,530,612,694 (3); 9055 `100,340,2300,900` 70,145,226,308,390,466,543,620,702,778 (3);
9056 `100,330,2300,1350` 54+79k, k=0..15 (4); 9057 `100,1650,2300,950` 68+80k, k=0..10 (4); 9060 `100,230,2300,620` 56+77k, k=0..6 (4).

Requests: hdl.huntington.org 5 (IIIF images, all 200); archive.org 6 (djvu `warofrebellion431unit_0` I/43 pt 1, `432unit` I/43 pt 2, `372unit` I/37 pt 2,
plus `431unit` and `433unit` fetched on a wrong guess: `431unit` is I/47 pt 2, `433unit` 503; two advancedsearch calls); www.googleapis.com 3 answered
(Books API, key and country=US, 200) after 3 malformed URLs (no request sent). No subagents. Report what was found and where it was not found;
novelty is a verifier's (rule 10): batch flagged for the verifier (LS-V2c). Five of seven entries (E30, E31, E32, E34, E35) are located in OR I/43 pt 1
by phrase; the filter's `or_cov` had not flagged them.

Verifier note (LS-V2c, 8 Oct 2026, AUDIT.md "## AUDIT (LS-V2c)"): E36 is in print after all -- its words are quoted in The Mereness Calendar
(1971, Google Books NlwPAQAAMAAJ, snippet), so the row's "not located" holds only for the OR and E36 is N1; E33 is the one N3 of the batch. Image
corrections applied to ciphertext.txt: E36 "More cool" (not "Move") and "walrus" (= Signature, not "wolves"). Grade corrections: E35 Govern, abel,
John and E36 Govern are plain (Governor/John Brough, reliable), now in `plain:` lines (E35 H 30 -> 27); E31 vincent and E32 aaron are M against the
print, E32 "Grant" is the code word Grunt = Warrenton (I). Print pages fixed: E30 p.859, E31 pp.871-872, E32 p.872, E34 p.897, E35 p.951 (also OR I/39 pt 2).

## LS-R6 (8 Oct 2026, account 1, for LANE ST-LEDGER-2)

Step 2 (script, `ls_r6_no1_1865.py`, output `ls_r6_no1_1865.out`): share of non-function tokens of an entry found in key.md's code-word
column, volunteer text, same tokenisation for both groups. 1865 priority-1 rows with words >= 40: n=108, median 0.276, p10 0.143
(of which cipher_guess=1: n=95, median 0.269, p10 0.143). Control, the read 1864 entries E21-E54 (those with a row in the tsv): n=27,
median 0.353, p10 0.257. Difference -0.077. Verdict: **No. 1 reads 1865 rows** (within the 0.1 line; the p10 is 0.11 lower, so some 1865
rows will fail). No 1865 entry was read in this job.

Step 1: ten rows of `entries-mssEC19.tsv`, read from the 2400 px IIIF image against the volunteer text, strip crops by `tools/iiif_lines.py`.
Nine of the ten were guessed Cipher No. 2 or 9 and eight of those are; 8958/66/0 (guessed 2) is Cipher No. 1 vocabulary, mostly plain, so it is E65.
8907/15/0 holds two telegrams (1 and 4 March), O9-AI and O9-AJ. `decode_no2.py`, `decode_no9.py`, `decode.py` `--write` then `--check` exit 0.

| ID | date | from / to (decoded plain) | H | C | I | M | found in print / not located in |
|---|---|---|---|---|---|---|---|
| N2-BG | 20 May 1864 10 PM | Meigs (QMG) to Ingalls: fleet to the Rappahannock for the wounded at Fredericksburg, navy convoy, cavalry on the bluffs Port Royal-Fredericksburg, two steamers for 70 wounded, 3000 bedsteads sent | 48 | 0 | 1 | 1 | not located: OR I/36 pts 2-3 (`warofrebellion362unit`, `363unit`) grep "covered barges", "bed steads", "lighter vessels", "Tappahannock or as near": 0; Google Books (1 query): no hit |
| N2-BH | 26 Oct 1864 5 PM | Stanton to Sheridan: the 18th Connecticut to New Haven 2 Nov, the 2nd Eastern Shore Maryland to Baltimore 4 Nov, quartermaster to furnish transportation | 29 | 2 | 1 | 2 | in print: OR I/43 pt 2 (`warofrebellion432unit`) p.468 (OCR running head), Townsend to Sheridan, 26 Oct 1864, "desires you to order the Eighteenth Connecticut Volunteers to be at New Haven the 2d of November ...", word for word but the regiments to "be replaced at Martinsburg by others ordered by you from elsewhere" |
| N2-BI | 24 July 1864 | Meigs to the quartermaster at (Pickford/Bickford on the page): about 1000 cavalry horses on hand, deliveries checked by want of money, 3962 issued since 1 July | 30 | 0 | 1 | 1 | not located: OR I/37 pt 2, I/39 pt 2 (`warofrebellion372unit`, `392unit`) grep "Depreciation of vouchers", "short supply of money", "checked deliveries": 0 |
| N2-BJ | 4 June 1864 10 PM | Stanton? (signed Secretary of War) to Dana: Lt. Col. Wade, son of the Senator, ex-captain of cavalry, wants a place on Sheridan's staff, Meade knows him | 22 | 0 | 1 | 0 | not located: OR I/36 pts 2-3 grep "pluck and gallantry", "Sheridan's staff": 0; Google Books: no hit |
| N2-BK | 12 Dec 1864 | Meigs to Sheridan: the Secretary requested to revoke an assignment; is a chief quartermaster to your army needed, who is most capable and worthy | 8 | 2 | 1 | 1 | not located: OR I/43 pt 2 grep "most capable and most worthy", "chief quartermaster to your army": 0; Google Books: no relevant hit (a Sheridan acting-chief-quartermaster snippet of another year/author) |
| N2-BL | 8 Apr 1864 2.30 PM | Meigs to Holabird, Chief QM Dept of the Gulf, New Orleans: send a vessel loaded with forage to Pensacola to make sure of a supply by 1 May, one also sent from New York | 17 | 0 | 0 | 0 | not located: OR I/34 pt 3 (`warofrebellion343unit`) grep "make sure of a supply": 0 (generic "loaded with forage" hits in four volumes, none of this telegram); Google Books: no hit |
| N2-BM | 27 July 1864 2 PM | Meigs to a quartermaster ("Palestine"): do you need more mules, about 500 shipped, rest held until I hear, shipments of horses stopped | 10 | 0 | 0 | 1 | not located: OR I/37 pt 2, I/39 pt 2 grep "obliged to stop shipments", "do you need more mules", "under changed circumstances": 0; Google Books: no hit |
| N2-BO (was E65; withdrawn and re-filed, LS-FIX) | 6 May 1864 | Maj Gen B. F. Butler (decoded) to Col. Stager at Cleveland: proceed at once to Cairo for the transmission of intelligence between that point and the forces on the Red R., General Canby will start tomorrow afternoon, join him | 8 | 0 | 0 | 3 | not located: OR I/36 pt 2 (`362unit`), I/37 pt 1 (`371unit`) grep "transmission and receipt of intelligence", "you had better join him": 0; Google Books: no hit |
| O9-AH | 20 Apr 1864 | Meigs? to Capt. G. D. Wise at New York: charter the transports for the expedition with Van Vliet, reach Fort Monroe by the 24th, coaled by the 25th; Butler to move 30,000 men, 2000 horses, 10 batteries, 100 wagons | 14 | 0 | 0 | 0 | not located: OR I/33 (`warofrebellion33unit`) grep "chartered a number of vessels", "fully coaled by the twenty fifth", "thirty thousand men", "fresh for their morning": 0 (Wise/Quartermaster hits are other items); Google Books: no hit |
| O9-AI | 1 Mar 1864 2.30 PM | to Brig. Gen. Wright, San Francisco, for D. W. Cheeseman, Asst Treasurer, Camden: make no further shipments of gold to London | 3 | 0 | 0 | 2 | not located: Treasury traffic, no Treasury edition read; Google Books ("Make no further shipments of gold to London" Cheeseman): no relevant hit | [V1-O9, 8 Oct 2026: N1 -- body in clear in the Huntington public transcription of 8907; AUDIT.md "AUDIT 2 (second adversarial, V1-O9)"]
| O9-AJ | 4 Mar 1864 noon | same pair: you were directed on the 1st to ship no more coin; if not too late detain that referred to in your telegram of yesterday; report immediately | 3 | 0 | 0 | 2 | not located: same as O9-AI | [V1-O9, 8 Oct 2026: N1 -- body in clear in the Huntington public transcription of 8907; AUDIT.md "AUDIT 2 (second adversarial, V1-O9)"]

Grades: decoder counts H 191, C 4, I 6 over the eleven blocks (N2-BG..BM, E65, O9-AH..AJ); M by hand 13. Every code word in the ten rows is in a key; no
entry fell under rule C's 80% line. M items: N2-BG "crowded" read by the decoder as `[Lieut Gen Grant]ed` (a plain word, the ledger spells it out); N2-BH
"desires" read `[Lookout Valley]'s` and "Haven" read `[Shelbyville]` where the print has "desires" and "New Haven" (both plain, C from OR I/43 pt 2, so the key
rows for those two words are wrong when the word is plain); "Ell swear" = elsewhere and "ack knoll edge reseat" = acknowledge receipt are the clerk's syllable splits;
N2-BI the addressee reads "Pickford" on the image, "Bickford" in the volunteer text, and the time word Fanny = 11 AM against the header 10 am; E65 "Wedlock" read `Track`,
"Salems"/"altar" and "Shark" read `Government` doubtful; O9-AI/AJ the time word Deborah = 3 AM against "noon" in the header of AJ, the date line "Ida" read `[Abingdon]`,
and "Camden" read `[Maine]` where it is the plain place of the Assistant Treasurer. Image vs volunteer text: no word differed on the strips read, apart from
N2-BI's addressee, and "Weasel/Wasel", "spoud/spond" (N2-BH, N2-BK) where the image is not clear and the volunteer text was kept. N2-BG's last five lines
(p.75, pointer 8967) and the closing lines of N2-BM were read from the volunteer text with the first and last words checked on the strip.

Crop commands (S = session scratch; images `hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg`, one fetch each): `python3 tools/iiif_lines.py
--image $S/img/p<pointer>.jpg --out $S/crops/<dir> --prefix p<pointer> --region <x,y,w,h> [--centres <list>] --lines-per-crop <n> --max-width 2400` with 8966 `100,1560,2300,1180`
centres 90,180,270,365,460,550,645,740,835,930,1030,1120, 3; 8967 `100,150,2300,700` auto, 4; 9104 `100,1330,2300,950` 50+85k, 4; 9011 `100,1600,2300,950`, 4; 8979 `100,240,2300,950`, 4;
9139 `100,1580,2300,900`, 4; 8925 `100,1250,2300,1000`, 4; 9019 `100,250,2300,800` auto, 4; 8958 `100,200,2300,1050` auto, 4; 8937 `100,230,2300,2480` centres 193+93.6k (k=0..23), 6;
8907 `100,230,2300,1700` auto, 5. Crops read by the worker, no subagent.

Requests: hdl.huntington.org 11 (IIIF images, 200; 8966 and 9104 also thumbnails from the same file); archive.org 8 (`_djvu.txt` of `warofrebellion33unit`, `343unit`,
`362unit`, `363unit`, `371unit`, `372unit`, `392unit`, `432unit`) plus 1 be-api fts test; www.googleapis.com 8 (Books API, key, country=US). Report what was
found and where it was not found; novelty is a verifier's (rule 10): batch flagged for a first verifier (LS-V6). Process note: `tools/room.py "<role>" "<text>" --push <paths>`
logs the ROOM line and pushes only ROOM.md; the files were pushed by `git add`, `git commit`, `git pull --rebase`, `git push origin HEAD:main` (first three commits b195952b, 6cdb82bd, c356c084).

Verifier note (LS-V6, 8 Oct 2026, AUDIT.md "## AUDIT (LS-V6)"): **E65 is Cipher No. 2, not No. 1** -- key-no2.md reads Blubber = Cairo, Altar = Red River, Shark = General, Wedlock = Tomorrow, Costume = Secretary of War, Viola = midnight, and Plum, Military Telegraph (1882) II p.47 prints the order in substance; the table row above and reading.md's E65 block are wrong in five code words until a reader re-files it in ciphertext-no2.txt. The step-2 verdict is withdrawn as a non-test (rows read as No. 2/old vocabulary score median 0.374 against the No. 1 control's 0.395; re-run diff now -0.119). N2-BI and N2-BM are addressed to Ingalls in the decoded plain (OR I/40 pt 3 searched there, not located); N2-BH is OR I/43 pt 2 pp.467-468.

## LS-R5 (8 Oct 2026, account 1, for LANE ST-LEDGER-2)

Ten priority-1 entries of `entries-mssEC19.tsv` read with key.md (Cipher No. 1) as E55-E64 in ciphertext.txt; every entry is Cipher No. 1, key.md
reads all code-word tokens but the unread words listed below, so none went to key-no2.md or key-no9.md. `python3 decode.py --write` then `--check` exit 0
after every pair; rows marked `already_read` with "LS-R5 E<n>". Commits: 0d977fc6 (E55-E56), 672ddf03 (E57-E58), f623f3e8 (E59-E60), 8f924457 (E61-E62), a99cfc78 (E63-E64).

| ID | date | from / to (decoded plain) | H | C | I | M |
|---|---|---|---|---|---|---|
| E55 | 26 Aug 1864 11 AM | to Lt. Col. C. H. Howard, Louisville (Capt. Bruch): Canby's dispatch states Gen. A. J. Smith's command has been detached to co-operate with Sherman (code Kidnap, Jew = General-in-Chief) | 11 | 0 | 0 | 0 |
| E56 | 28 Nov 1864 11 AM | Van Duzer & McCaine: "Grant directs me to say that it is not expedient of you to give to the Major Generals ... commands of more than Divisions" (to Nabob/Lamb = Sheridan/Thomas) | 13 | 0 | 0 | 0 |
| E57 | 8 Apr 1864 | Meigs to a Captain Thomas, Quartermaster: if Relief is a good staunch steamer let her call at Annapolis for a load of colored troops, else proceed to Hilton Head | 8 | 0 | 2 | 0 |
| E58 | 19 Apr 1864 | Grant (code John) via E. D. Townsend: return Jeffery's letter to Secretary Seward; send copy of message to Burnside | 12 | 0 | 0 | 2 |
| E59 | 27 Apr 1864 | to Sherman at Nashville (Van Valkenburg): the Cavalry Bureau reports the 11th Michigan Cavalry is of no use at Lexington, ought to go to the field; signed General-in-Chief | 12 | 0 | 0 | 1 |
| E60 | 16 Jul 1864 10.30 AM | President (Bologna) to Grant: yours received with the safe conduct as you propose, without waiting for one by mail from me; "if there is, or is not, anything in the affair I wish to know it without unnecessary delay" | 8 | 0 | 0 | 0 |
| E61 | 9 May 1864 3.55 PM | Stanton (Brutus) to Butler (Knox), O'Brien at Hd Qrs Butler: dispatch from Grant just received, on the march with his whole army to form a junction with you, route not determined | 6 | 0 | 0 | 0 |
| E62 | 6 Apr 1864 | Meigs to Biggs, Fort Monroe (Sheldon): send orders to Spaulding to Hilton Head, Montauk and two propellers to Annapolis to take troops, coal supply | 10 | 0 | 1 | 0 |
| E63 | 6 Aug 1864 11.30 AM | Halleck? (signed Sugar Ben-jam-in, unread) to Grant (Japan), Monocacy Junction: one brigade of Torbert's cavalry division left last night, another this morning for Harpers Ferry | 21 | 0 | 1 | 0 |
| E64 | 7 Aug 1864 12.30 PM | Grant (Jupiter) to Sheridan (Nabob): give commands to officers regardless of rank; the Departments of Washington, Susquehanna and West Virginia formed into the Middle Military Division, you have temporary command | 35 | 1 | 0 | 1 |

Grades: decoder H 136, C 1 over E55-E64. By hand: I 4 (E57 "Ann" and "collared" and E62 "Ann" read as plain by `plain:` lines; E63 "money" plain
= Mono-cacy); M 4 (E58 "pembroke" read [Cipher] and "Tinkers" read [Offensive] by the decoder, plausible sense "Burnside in Cipher at Offensive's request" doubtful, both M; E59 "Susan" is key.md 11.30 PM against the
ledger header 11.30 AM; E64 "Sapan Rape", the officer to be relieved, not in key.md). Unread, left as written and not graded: E55 "Lol"; E56 "nick", "eggs peck dead" (= "expedient", clerk's split); E57 "his on one",
"Bender"; E58 Jeffery, See ward as written; E63 "Sugar Ben - jam - in" (signature); E64 "confide = ants", "um" (West Virginia part). Pencil glosses in a later hand (numerals, "wants", "money", "order issued making") over
E55-E64 not transcribed, except the interlineations carried into the sentence (E55 Pandora, leopard; E56 Nabob; E61 determined, translated; E63 expected, order issued making, money) as `<ins>`.
Image vs volunteer text (image taken in every case): E57 header "Baldwin"; E57 "there needed proceed" read from the image where the volunteer text has "there"; E57 "his on one" (volunteer "he's on one");
E59 "there" struck through (volunteer text keeps it); E61 header "(No 1)" and "355 PM" above the date; E62 "ordrs"; E64 "nick" (volunteer "wick"), a struck "you" before "you have been as signed"
(volunteer text has one "you"). E60 and E63-E64 header and tails read in full from the crops; E58 has no operator or addressee header on the page (volunteer text is the same).

Print: `tools/print_check.py` on 16 decoded phrases (scratch target, not committed), `ia` sources `warofrebellion372unit` (I/37 pt 2), `362unit` (I/36 pt 2), `33unit` (I/33),
`431unit`, `452unit` (I/45 pt 2), 5 volumes x 16 phrases: no hits, plus `ia-global` (hits only on phrases that name no letter-specific text), Google Books with key and country=US (503 on four phrases, not searched), OpenAlex,
CrossRef (nothing relevant), Semantic Scholar 429 (not searched). A search result, not a finding. Corrections of that search: the phrases were paraphrased, not verbatim from the ledger, so a miss is weak; `431unit`
is not the volume I took it for (its text is Jan 1865 operations in Georgia, 1 "August" date; the Aug 1864 Shenandoah correspondence is not in the cached set), `432unit` starts 1 Sept 1864 (searched, 0 hits for the Aug 6-7
phrases, as expected), and `372unit` ends about 3 Aug 1864. So E55, E63 and E64 (5-26 Aug) are NOT located and NOT searched in the right volume: the OR volume for 4-31 Aug 1864 (ser. I vol. 43 pt 1 on
the Official Records' own numbering, IA id not found in the cached set) is still unread; E64's content (Middle Military Division, Sheridan, 7 Aug 1864) is described in secondary literature, so a hit is
expected there. E60 (Lincoln, 16 Jul 1864): `372unit` 0 hits on "safe conduct as you propose"; Lincoln Collected Works (Basler) vol. 7 not searched. E61 not located in I/36 pt 2 by this check; E56 not located in I/45 pt 2;
E57, E58, E59, E62 not located in I/33 by this check; ORN, Grant Papers and Lincoln Papers were not searched. Hosts: archive.org 2, be-api.us.archive.org 16, www.googleapis.com 16, api.openalex.org 16, api.crossref.org 16,
api.semanticscholar.org 3; hdl.huntington.org 10 (one 2400 px image each, once). Subagents 0. Report what was found and where it was not found; novelty is a verifier's (rule 10): batch ready for a first verifier (LS-V5).
Crop commands (S = session scratch; images `hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg` fetched once to $S/img; regions from 600 px thumbnails, x4):
`python3 tools/iiif_lines.py --image $S/img/p<pointer>.jpg --out $S/crops/<pointer> --prefix p<pointer> --region <x,y,w,h> --centres <list> --lines-per-crop 2 --max-width 2400` with 9057 `100,260,2300,620` centres 60,160,260,360,460,560;
9129 `100,660,2300,580` 85,185,285,385,480; 8927 `100,260,2300,780` 40,140,252,348,448,540,628,712; 8932 `100,1700,2300,820` 40,128,220,312,408,500,596,692,772; 8951 `100,1040,2300,720` 50,192,288,380,472,568,660;
9003 `100,600,2300,900` 60,168,272,368,464,560,652,740,828; 8959 `100,1920,2300,520` 52,148,240,332,428 and `100,2330,2300,300` 110 (last line); 8921 `100,1260,2300,1080` 80,172,260,360,460,560,660,760,860,940;
9036 `100,1100,2300,1000` 40,112,212,312,412,512,612,712,812,912; 9038 `100,270,2300,2060` 30,142,235,328,422,515,608,701,794,888,981,1074,1167,1260,1354,1447,1540,1633,1726,1820,1913.

Verifier corrections (LS-V5, 8 Oct 2026, AUDIT.md "## AUDIT (LS-V5)"): seven of the ten are in print and class N1 -- E55 OR I/39 pt 2 p.304,
E56 OR I/43 pt 2 p.682 (in the cached `432unit`), E58 Papers of U. S. Grant vol. 10 (note; snippet identification), E60 Basler vol. 7 and OR III/4,
E61 OR I/36 pt 2 p.587, E63 OR I/43 pt 1 p.709, E64 OR I/43 pt 1 p.719 (`warofrebellion431unit_0` is I/43 pt 1). Corrections to the table above:
E60 is Lincoln to **John Hay at the Astor House, New York**, not to Grant ("John" is Hay's name in clear; H 7, not 8); E56 "eggs peck dead" is
*expected*, not "expedient", and "nick" is *report* (also in E64); E55's [Hurlbut] in the derived block comes from the later pencil gloss "leopard",
not the message; E64 "Dismiss" = Averell and "Sapan" = "him from the" by the print. E57, E59, E62 not located after a full search: N3. The three
LS-R5 gaps below are closed by that audit (print located or searched; M tokens re-read from the image, unchanged).

## Remaining gaps (LS-R5, 8 Oct 2026)
Read so far: 108 of 893 mssEC 19 segments read after LS-R5's ten (E55-E64: H 136, C 1, I 4, M 4; `decode.py --check` exit 0); the rest of the 300 or so priority-1 rows unread by this job.
- Print location of E55, E63, E64 (5-26 Aug 1864) - blocker: not-attempted; the OR volume for 4-31 Aug 1864 is not in the cached set (`431unit` proved to be Jan 1865, `372unit` ends 3 Aug, `432unit` starts 1 Sept); next: fetch that volume's djvu once and search the verbatim ledger phrases, ~$0.5
- Print location of E60 (Lincoln, 16 Jul 1864) - blocker: not-attempted; Basler vol. 7 and Grant Papers vol. 11 not searched; next: LS-V5 search, ~$0.5
- M-graded tokens E58 "pembroke"/"Tinkers", E59 "Susan", E64 "Sapan Rape" - blocker: open-codes; no context narrows them; next: LS-V5 re-read against the page images, ~$0.5

## Escalation (LS-R5, 8 Oct 2026)
- [n/a] siblings: the ten are siblings of E21-E54 already read; no new sibling pool found by this job.
- [x] clear-pages: E55-E64 read from the page images, volunteer text as second witness.
- [x] known-keys: key.md read every code word but the listed unread ones; key-no2.md and key-no9.md not needed.
- [ ] print: five OR volumes searched, wrong volume for August (see gaps); Lincoln/Grant editions not searched.
- [n/a] key-rebuild: no key change proposed.
- [x] image-check: crops read by the worker; no subagent.
- [x] retry: not needed.
Verdict: keep going: 3 internal gaps; cheapest next: fetch the OR volume for 4-31 Aug 1864 and the Lincoln/Grant editions and locate E55, E60, E63, E64 in print, ~$0.5-1

## LS-R7 (8 Oct 2026, account 1, for LANE ST-LEDGER-2)

Ten priority-1 rows of `entries-mssEC19.tsv` (non-army addressees, McCaine rows skipped) transcribed from the 2400 px page images (strip crops, no subagent; volunteer text as second witness).
Eight were read: seven in Cipher No. 1 (key.md) as E66, E67, E68, E70, E72, E73, E74 in ciphertext.txt, one in Cipher No. 2 (key-no2.md; header `Coldwell "2"`) as N2-BN in
ciphertext-no2.txt (the brief's E71 slot; no E71 in ciphertext.txt). Two (E69, E75) are "key not in hand" and are NOT in any ciphertext file (transcriptions below). `decode.py --check`,
`decode_no2.py --check`, `decode_no9.py --check` exit 0 at the last push. Commits: 4030be9e (E66-E67), f25d36eb (E68, E70, N2-BN), 38b87d9d (E72-E73), 4030c5cd (E74 + tsv); NOTES/print script in the closing commit.

| ID | date | from / to (decoded plain) | H | C | I | M | print |
|---|---|---|---|---|---|---|---|
| E66 | 3 Jan 1865 12 M (header written "1864"; see below) | Horner (New York): Wise has called on you for [Waymomers, unread] to take 1000 construction corps US military railroads from Baltimore to Savannah; in addition 4000 troops by steaming from "Banditte" to sea, full coal and water for 15 days; report vessels you can send | 33 | 0 | 1 | 2 | not located (I/45 pt 2 cached; ORN I/12 fetch failed) |
| E67 | 3 Dec 1864 12.30 PM | H. A. Wise, Chief of Bureau (Navy) to Rear-Adm. D. D. Porter: your telegram to Mr. Fox received; everything done by the Bureau with utmost vigor; when the Baltimore arrives she leaves again with Jeffers and Rodman to assist in fitting out the Louisiana; the Stromboli is on her way with 80 torpedoes and 2 of Beardslee's clock movements | 13 | 1 | 1 | 0 | FOUND, ORN ser. I vol. 11, word for word (see print) |
| E68 | 7 Aug 1864 | Stanton (Brutus) to Capt. Sam Bruch, Louisville, for General Burr[bridge?]: see Surgeon Ferry in person and hear his statement; if you deem his [plantation?] trustworthy send the substance by cipher telegraph; if important send him here under adequate guard that will take care he does not escape | 17 | 0 | 1 | 2 | not located (I/43 pt 1-2 cached) |
| N2-BN | 16 Mar 1864 | Brig. Gen. H. W. Benham to Humphreys at the Navy Yard: the patent pontoon bridge train of canvas pontoons will be ready today as ordered in your letter of the [29] ult, [50] chess placed on each chess wagon, additional wagons if still deemed necessary | 16 | 0 | 0 | 2 | not located (I/33 cached) |
| E70 | 16 Jun 1864 12.20 PM | Geo D. Ramsay, Chf Ord, to Capt. Smith, St Louis: Major Callender, commanding St Louis arsenal, to issue at once to General Carrington at Indianapolis four 12-pdr howitzers with implements and equipment complete, 400 rounds assorted (100 canister) by special messenger; no delay; report the issue by telegraph | 13 | 0 | 1 | 1 | not located (I/36 pt 2 cached; I/39 not cached) |
| E72 | 23 Sept 1864 10 AM | to Bickford at Harper's Ferry (Brig. Gen., signature code unread): nearly 5000 troops leave here for Winchester this morning; see that transportation is ready on their arrival at your post and afford every facility for a rapid march | 16 | 0 | 0 | 2 | not located (I/43 pt 2 cached) |
| E73 | 7 Nov 1864 12.30 PM | B. F. Greene, chief clerk for the chief of Bureau (Navy), to S. P. Lee (code Neptune) at Mound City: direct officers [polkers, unread] in your squadron to make all important signals by adding a number [utopia, unread] designated in your order to the signal numbers made and subtracting the same number from those received | 9 | 0 | 0 | 2 | not located (ORN I/26 searched, 3 phrases) |
| E74 | 11 Sept 1864 8 PM | Stanton (Brutus) to Chas Armond: "The publication of Sand[ers?] despatch was an enormous blunder. 'Twas done by [the] Tycoon without my knowledge. I did not know he had seen it until too late and foresaw the consequences would be very bad. It cannot happen again" (mostly plain; one code word) | 2 | 0 | 1 | 2 | not located (I/43 pt 2 cached) |
| E69 | 13 Oct 1864 | Halleck? "JW Hallack Ind No 10" to Gov. Morton (Indiana), signed Blanchard: key not in hand | - | - | - | - | - |
| E75 | 5 Feb 1864 | "Baldwin 10" to Lockwood (Baltimore?): key not in hand | - | - | - | - | - |

Grades: decoder H 104 over E66-E74 (E66 33, E67 14, E68 17, E70 13, E72 16, E73 9, E74 2) plus 16 in N2-BN (H 120 for the eight), C 1 (E67 "tar pedro" = torpedoes, from the print),
I 5 and M 13 by hand. I: E66 date (header "1864", entry is Jan 1865; see below); E67 "Fox" read [Philadelphia] by the decoder is plain "Mr Fox" (print) so one of its 14 H is not H, counted 13 + I 1; E68 "Burr" + patent read
"Burr[bridge]" by inference; E70 "Ramsay" read [Effect] by the decoder is the signatory's plain surname; E74 "the" struck through. M: E66 "Weaselira", "Banditte" (vessel name, read plain), unread
"Waymomers", "Vain fleet"; E68 "Jones", "platation"; N2-BN "Humphreys" read [Wilmington]'s and "the Oliver Ellsworth ult" read [29] ult; E70 "Polkaing" (image and volunteer text disagree: image reads "Packaing"/"Pockaing", volunteer
"Polkaing"; took "Polkaing"); E72 "Stephen son" read [In the] son, signature "see see Awe gear"; E73 "polkers", "utopia"; E74 "Sand hers", "Coox Edwards". Unread, not graded: E66 "pelton", "counter man dead" (tail); E67 "pedro"
before print gloss; all plain-spelling names (Jeffers, Rodman, Beardsley, Stromboli, Baltimore, Randall, Chess, Benham). E74 is nearly clear text: its sense is read from the page, not from the key (H 2).

Date of E66: the page (printed 257) opens "Wash. Jan. 2. 1865" and holds the 2 Jan and 3 Jan 1865 entries above it; its own header reads "Jany 3rd 1864". Taken as 3 Jan 1865: the text names Wise (Navy Bureau chief), railroad
construction corps to Savannah (taken 21 Dec 1864) and the Fort Fisher shipping of early Jan 1865. The clerk's "1864" is the usual January slip; the cipher reading does not depend on it.

Image vs volunteer text (image taken): E66 header "(1)" and a pencil numeral "6" above the first line, no word differs from the volunteer text; E67 interlineation "talbots" after "clock" carried as `<ins>`, "Jedro/pedro" taken
as "pedro"; E68 "Escape" capitalised; E70 interlineations "dis", "5", "M", "im", "assorted" carried as `<ins>`, struck "Rep" as `<del>`, header time "1220 pm" above the date; E73 header "1230 pm"; E74 struck "the" before "Tycoon"
(volunteer text keeps it); E72 is in very faint pencil (read from the crops, volunteer text agrees on all 59 words). Page numbers: the pointer's page index (cited as Page 257, 240...)
differs from the printed page number by 2 (e.g. 9071 = page 179, printed 177); the headers carry the pointer page.

Key-not-in-hand entries. Both carry "10" in the header (E69 "Ind No 10", E75 "Baldwin 10"), use "period" as a word, and have an unusual word order of plain words; E75 also writes its first line as comma-separated words.
Coverage is not the test here: E69's 10-11 code-word tokens are all read by decode.py (key.md) and by decode_no2.py, but the two keys give different values to the same words ("quarrel" = [Embark] vs [Defeat], "Bishop" = [Atlanta]
both) and neither gives a sentence ("press the [Embark] on this [Front]"); E75 reads no sentence under key.md, key-no2.md or key-no9.md ("Pauline Quarrel Lock wood" = [Convoy][Embark][Banks]wood /[Camp][Defeat][Dix] /
[Pemberton][Jackson]). Nothing was guessed and no ciphertext file carries them. Hypothesis, untested: the "10" marks a Cipher No. 10 (Halleck to a governor; Baldwin to a provost-marshal line) not among key.md, key-no2.md, key-no9.md.
Transcriptions as written (not graded):
E69 | Page 199 (printed) | 9093 | JW Hallack Ind No 10  Washn Oct 13th 1864 / Mohawk Florence for Gov Morton period / In my letter borne by mister / Mitchell to Quorum Sherman I said / that any Soldiers he could spare /
for October need not to remain / for November period I therefore cannot / press the quarrel on this reptile / all that the Bishop and quarrel / Sherman feel they can safely do / I however shall be glad of / period Bravo for Dresden and for / yourself personally signed Blanchard
E75 | Page 7 | 8899 | Baldwin 10  Wash'n D.C. Feby 5th 1864 / For , Pauline , Quarrel , Lock , wood , period , Prison - / ers of War are Expected to leave / Cleve = land = to day and will pass / through Ink You will take measures to /
have them well Rodneyed while passing through / the city and to prevent any communication / with them Abel Viola How is George

Print (script `ciphers/eckert-1864/ls_r7_printcheck.py`: verbatim ledger phrases, letters only, against the cached OR djvu texts in sources/ia-fulltext/print-check/, nothing added): I/33 (`warofrebellion33unit`), I/36 pt 2
(`362unit`), I/37 pt 2 (`372unit`), I/43 pt 1 (`431unit`), I/43 pt 2 (`432unit`), I/45 pt 2 (`452unit`), 27 phrases of 2-4 per entry: every phrase specific to an entry is "none"; the six generic hits ("there must be no delay",
"let me know", "the additional wagons", "until too late", "will you see that", "on their arrival at your", "everything is being done") were opened in context where unclear: all unrelated letters (Augur I/36 pt 2, Wright I/45 pt 2, Confederate wagon returns I/33).
Navy items: ORN ser. I vol. 11 (IA `officialrecordso0011unse`, scratch only) FOUND E67 word for word, Washington, December 3, 1864 12:30 p.m., Wise to Rear-Admiral D. D. Porter, printed straight after Porter's telegram to Assistant Secretary
Fox: "Your telegram to Mr. Fox of this a. m. received. Everything is being done by the Bureau with the utmost vigor. The moment the Baltimore arrives she will leave again with Jeffers and Rodman to assist in fitting out the Louisiana.
The Stromboli is on her way to you with 80 torpedoes on board and 2 of Beardslee's clock movements. If you have not Beardslee near you, let me know." (page number not read by this job; the OCR lacks running heads). The ledger's
"tar pedro" = "torpedoes" (C) and "Niagara" = Porter (H), "Beardsleys" = Beardslee (clerk's spelling). Key and decode agree with the print on every code word except "Fox" ([Philadelphia] in key.md, plain in print): the three-word code
"Niagara" etc. are read as the print has them. ORN I/26 (`officialrecordso0026unse`, Mar-Dec 1864 Western Waters, scratch only): E73 phrases "signals by adding", "signal numbers received", "subtracting the same number" none (the 7 Nov 1864
Porter dispatches there are about other matters). ORN I/25 (`officialrecordso0025char`) is 1863 and was no use for E73. Not searched: OR ser. I vols 39-42 (June-Oct 1864 Grant/Sherman-front correspondence, relevant to E70), ORN I/12 (the fetch returned 163
bytes, one try), ORN ser. II, Lincoln Collected Works (E68, E74: the "Sanders despatch"), Grant Papers, Stanton papers, the press of the day (E74), Welles diary; Google Books and OpenAlex not run in this job. A miss is a search result, not a verdict (rule 10):
the batch goes to a verifier (LS-V7) which should search E74 and E68 first (press of 12-13 Sept 1864; Burbridge's Kentucky correspondence of 7-9 Aug 1864).

Crop commands (S = session scratch; images `hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg` fetched once to $S/img; regions from 600 px thumbnails, x4):
`python3 tools/iiif_lines.py --image $S/img/p<pointer>.jpg --out $S/crops/<pointer> --prefix p<pointer> --region <x,y,w,h> --centres <list> --lines-per-crop 2 --max-width 2400`: 9151 `100,1700,2300,1066` centres 120,260,380,490,610,730,850,960;
9134 `100,250,2300,1120` 54,150,238,334,430,526,618,714,814,918,1014; 9039 `100,250,2300,920` 54,142,218,298,382,462,542,622,702,782,862 (last line cut, re-cropped by hand 100,1080,2300,170); 9093 `100,1880,2300,886` 52,132,220,312,408,500,588,668,760;
8985 `100,1640,2300,860` 44,156,244,350,460,552,648,760,830; 8914 `100,240,2300,800` 48,152,232,308,392,488,588,688,740; 9075 `100,1380,2300,740` 40,140,228,320,412,500,588,680; 9118 `100,250,2300,720` 38,142,222,310,398,490,578,678;
9071 `100,1800,2300,700` 64,160,260,360,452,552,628; 8899 `100,1500,2300,840` 68,200,320,460,580,688,780. Requests: hdl.huntington.org 10 (one 2400 px image each), archive.org 7 (advancedsearch 1, `_djvu.txt` downloads 6: 0025char, 0011unse, 0026unse,
0026char (HTTP 503, not retried), 0012unse (163-byte error body, not retried), plus 0011/0026 each once), 0 other hosts. Subagents 0.

LS-V7 correction note (8 Oct 2026, verifier, see AUDIT.md "## AUDIT (LS-V7)" section 4): E66's "Wise" is Colonel (George D.) Wise, quartermaster at
Baltimore, not H. A. Wise of the Navy; "Vain fleet" = Van Vliet, "Banditte" = Banditti (Baltimore), "Weaselira" = steamers (Weasel = Steam), and
Van Vliet's replies of 3 Jan 1865 are printed (OR I/46 pt 2 p.28), which fixes the year. E72 "Stephen son" = Brig. Gen. Stevenson (the decoder's
[In the] is wrong), signature "see see Awe gear" = C. C. Augur. E73 "polkers" = commanders, "utopia" = Utophia (Parenthesis). E68 "platation" =
communication, "person" plain (decoder's [5] wrong). E70's image reads "Pockaing". N2-BN "patent" = [Advance] (H; "advance guard train" in the
printed order), "Humphreys" plain (decoder's [Wilmington] wrong), "Oliver Ellsworth" = 29 (H). E67 N1 (ORN I/11); E72 and E73 N2 (substance
printed: OR I/43 pt 2 pp.142-143, ORN I/26 pp.209-211); E66, E68, E70, E74 (D1), N2-BN N3 one audit. E69, E75: none of the three keys reads them.

## Remaining gaps (LS-R7, 8 Oct 2026)
Read so far: of the ten rows, 8 read (E66, E67, E68, N2-BN as E71, E70, E72, E73, E74); 2 "key not in hand" (E69, E75).
- E69 and E75 key (header "10", "period" words) - blocker: no-key-material; the three keys in hand give no sentence; next: look in mssEC 37-76 for a cipher book headed "10" / a Halleck-to-governor list, ~$0.5
- Print location of E66, E68, E70, E72, E73, E74, N2-BN - blocker: not-attempted; OR ser. I vols 39-42, ORN I/12, Grant/Lincoln editions and the press of the day not searched; next: LS-V7 search, ~$1
- M-graded tokens (E66 "Weaselira", E68 "Jones"/"platation", E72 signature "see see Awe gear", E73 "polkers"/"utopia", E74 "Sand hers"/"Coox Edwards") - blocker: open-codes; no context narrows them; next: LS-V7 image re-read, ~$0.5

## Escalation (LS-R7, 8 Oct 2026)
- [n/a] siblings: the ten are siblings of E21-E65 already read; E67 now matches ORN I/11 word for word, so the Navy Bureau (Wise) traffic of Dec 1864 is in print, as are the McCaine/Augur items.
- [x] clear-pages: the ten entries read from the page images, volunteer text as second witness.
- [x] known-keys: key.md (7), key-no2.md (1); key-no9.md tried on E75 only, no read.
- [ ] print: six OR volumes and ORN I/11, I/26 searched; OR I/39-42, ORN I/12, Lincoln/Grant editions and the press not.
- [n/a] key-rebuild: no key change proposed ("Fox" = Philadelphia in key.md is a plain-name collision in E67, one token).
- [x] image-check: crops read by the worker; no subagent.
- [x] retry: not needed (E69 and E75 each tried against three keys once).
Verdict: keep going: 2 internal gaps; cheapest next: a key-book check of the 1865 priority-1 rows (share of tokens in key.md vs key-no2.md vs key-no9.md per row against the read entries; the LS-R6 check was a non-test), ~$1, then the "10" book for E69/E75 in mssEC 37-76, ~$1.5 (updated ST-LEDGER-2 close, 8 Oct 2026: LS-V7 done, E66 E68 E70 N2-BN N3 one audit; second audits AUD2-LS-F/G/H queued). Earlier: keep going: 2 internal gaps; cheapest next: LS-V7 verifier on E66-E74 (E67 N1 by print), then a search of mssEC 37-76 for the "10" book for E69 and E75, ~$1.5

## Siblings (8 Oct 2026)

SUCCESS-SIBS (account 1, 8 Oct 2026, repository files only, no network, nothing decoded). Siblings of this folder's N3+ document(s) by volume, sender, recipient, key, design and series; 6 listed, 5 unread or not in the repository. Full rows with evidence: `SIBLINGS-2026-10-08.tsv`. p = the compiler's conservative estimate that the step yields a new counted document (N3+, D2+, two audits); not a novelty claim (rule 10). Required by `tools/gaps_check.py` for every N3+ target.

- mssEC 19 entries guessed Cipher No.1 (about 583 guessed, ~435 priority>=3), not yet read [same-volume; unread] -- decode.py with key.md on top-priority entries from the volunteer text, then OR-hit check per entries-mssEC19.tsv; shuffled-key control; ~$5; p 0.35; evidence: ciphers/eckert-1864/entries-mssEC19.tsv (cipher_guess col 11, already_read col 14 blank for ~730 rows); NOTES.md:122 (live lane ST-LEDGER-2 is reading mssEC 19 entries in batches (ROOM.md 8 Oct); route through that lane, do not duplicate)
- mssEC 19 entries guessed Cipher No.2 (~201; headquarters/Beckwith/Kimber) [same-key; unread] -- decode_no2.py on high-priority No.2 entries (mssEC 47 key in hand, H grade) with --check; ~$4; p 0.35; evidence: ciphers/eckert-1864/entries-mssEC19.tsv col 11=2; NOTES.md:198; decode_no2.py, key-no2.md (live lane ST-LEDGER-2 is reading mssEC 19 entries in batches (ROOM.md 8 Oct); route through that lane, do not duplicate)
- mssEC 18 parallel sent ledger (object 10074, 413 images, Jan 1864-Dec 1865) [same-series; not-in-repo] -- fetch 21-22 Apr 1864 pages via dmQuery CISOSEARCHALL, transcribe, apply key.md; ~$6; p 0.25; evidence: ciphers/eckert-1864/NOTES.md:30,308,314 (live lane ST-LEDGER-2 is reading mssEC 19 entries in batches (ROOM.md 8 Oct); route through that lane, do not duplicate)
- Cipher No.9 entries (~43 guessed) of mssEC 19 [same-key; unread] -- decode_no9.py on remaining 9-guess entries; ~$2; p 0.2; evidence: ciphers/eckert-1864/key-no9.md, decode_no9.py, entries-mssEC19.tsv col 11=9 (live lane ST-LEDGER-2 is reading mssEC 19 entries in batches (ROOM.md 8 Oct); route through that lane, do not duplicate)
- eckert-1862 ledger (mssEC 15) other entries [same-series; read] -- decode remaining unread 1862 entries with eckert-1862 key (Cipher book); check gaps in NOTES; ~$5; p 0.2; evidence: ciphers/eckert-1862/NOTES.md; ec18/align_entries.tsv; status partial
- Telegram ledgers 1865-67 (mssEC 1-76 series), e.g. 1865 entries; Cipher No.1 1865 book possibly missing [same-series; not-in-repo] -- blocked on 1865 cipher book; ls_r6_no1_1865 already tried; none until reply; p 0.05; evidence: ciphers/eckert-1864/NOTES.md:216 (Huntington reply pending on 1865 cipher book); LS-R6 no1_1865 (live lane ST-LEDGER-2 is reading mssEC 19 entries in batches (ROOM.md 8 Oct); route through that lane, do not duplicate)

## LS-FIX (8 Oct 2026, account 1, for LANE ST-LEDGER-2)
- E65 (8958/66/0) moved out of ciphertext.txt into ciphertext-no2.txt as N2-BO (N2-BN was the last used ID); decode.py and decode_no2.py `--write` then `--check` exit 0; header comment of ciphertext.txt records "E65: withdrawn, re-filed as N2-BO"; entries-mssEC19.tsv already_read cell and the LS-R6 table row updated (N2-BO decodes H 8, Butler to Stager, Cairo / Red R., per AUDIT LS-V6).
- E60 (9003/111/1) header corrected to Lincoln to John Hay at the Astor House and a `plain: John` line added; decode.py `--write`/`--check` exit 0, code-word tokens H 7 (was 8).
- The LS-R6 line "8958/66/0 ... is Cipher No. 1 vocabulary" above and its step-2 verdict are superseded by the LS-V6 note; no reading class changed.

## D2V-E74 (8 Oct 2026, account 2, verifier, for LANE DEFAULT-account-2-20261008-0710)
Second adversarial audit of E74 (AUDIT.md "## AUDIT 2 (second adversarial, D2V-E74)"). E74 lowered N3 -> **N1**: the Huntington's own public
transcription of pointer 9071 already carries its clear body word for word; only the signature "Webster Brutus" = [signed] [Secretary of War]
is in cipher (D1 unchanged). Identified: "Sand hers despatch" = George N. Sanders' telegram of 1 Sept 1864 from St Catharines to D. Wier at
Halifax, read out by Seward at Auburn on 3 Sept (Natl Intelligencer 8 Sept 1864 p.2); "Chas Armond" = the War Department telegraph operative
who reached Halifax on 3 Sept and telegraphed Eckert (mssEC 29 leaves 341, 348; mssEC 18 p.169 is a 6 Sept cipher to him, not decoded). No
reading changed. Suggestion for a reader (not run): mssEC 18 p.169's "Chas Armond Halifax" block is a sibling worth decoding, ~$0.3.


## LS3-K (8 Oct 2026, account 2, for LANE ST-LEDGER-3)

Two script checks, no reading. Scripts: `key_share_1865.py` (regenerates `key-share-1865.tsv`, `--write`); the (a) searches are logged below. Requests: Huntington `hdl.huntington.org/digital/bl/dmwebservices`, about 45 calls, 1.6-2 s apart, no 429/403 (the form without `/digital/bl/` answers 302).

### (a) The "10" book for E69 and E75: not found
Searches run (p16003coll11, `CISOSEARCHALL^TERM^all^and`, sixth segment 1; hits = records; none a cipher book numbered 10):
"No. 10" 9; "Cipher No. 10" 3 (mssEC 42 Cipher Book #1, "Telegraphs Sent.", and a Cipher Messages sent ledger, Aug 1862-Jan 1864); "Cipher Book #10" 0; "Halleck" 31; "Hallack" 3; "Baldwin" 19; "Ten" 32; "Lockwood" 14; "Cipher Book" 43; "Telegraphic Correspondence" 11. The hits for names and "Ten" are ledger volumes, not key books.
Cipher books titled in the collection: Cipher Book #1 (mssEC 42-47, six objects), #2 (mssEC 48, 49), #5 (mssEC 50, 66; unused so far here), #9 (object 1751 = mssEC 67), "Cipher book for Generals and Places" (mssEC 39), "Handwritten cipher book" (mssEC 38), a Headquarters A of P cipher book (object 6255). No "#10". Tomokiyo sources/cryptiana/web/civilwar1.htm: No. 9, No. 10 and No. 12 share one printed template ("same keys and arbitrary words, only their meaning different"; "Adam" = Lincoln in No. 9, McClellan in No. 10, Halleck in No. 12) and Beckwith made one book with three inks for them; no No. 10 key table or image is given. So a No. 10 book would be a re-meaning of the No. 9 template that the repo already tabulates in key-no9.md, but the meanings are not in hand; nothing to count coverage against. E69 and E75 stay "key not in hand", the gap stays no-key-material. Possible untried, not run: mssEC 66 (Cipher Book #5) and mssEC 38/39 as the "10"-marked books' neighbours, and the three-ink Beckwith book if it is in the collection (not searched for by name here); next: a reader would need to open mssEC 38/39 page images, ~$1.

### (b) 1865 key-book check: `key-share-1865.tsv` (130 unread priority-1 1865 rows, words >= 30; 153 labelled control rows)
1865 = pointer >= 9149 (page 257 opens "Jany 2d 1865") or a header naming 1865. Share = tokens of the entry (function words and one-letter tokens dropped) found in the code-word columns of the key file.
Control distributions (already-read entries, share in their own book): No. 1 n=63 median 0.406, p10 0.286, p90 0.567; No. 2 n=58 median 0.500, p10 0.364, p90 0.629; No. 9 n=32 median 0.205, p10 0.079, p90 0.333.
1865 distribution: No. 1 median 0.284 (p10 0.154, p90 0.516); No. 2 median 0.333 (0.213, 0.465); No. 9 median 0.069 (0.011, 0.159). Best book: No. 2 on 75, No. 1 on 55, No. 9 on none.
Verdict by the brief's rule (best-book share inside that book's control p10-p90): readable with No. 1: 41; readable with No. 2: 18; book not in hand (Nos. 3/4): 71 (59 readable + 71 not = 130).
No. 9: no 1865 row has No. 9 as best book; its table is a sample, not the whole book (key-no9.md header), and 0/32 of the No. 9 control rows have No. 9 as best book.

Matched control, and why the count is weak (rule 3): the control's own best-book call matches the label on 94/153 (No. 1 45/63, No. 2 49/58, No. 9 0/32). The p10-p90 band is not selective: No. 1's band accepts 51/63 No. 1 entries but also 46/58 of the No. 2 entries and 13/32 of the No. 9 entries; No. 2's band accepts 46/58 No. 2, 31/63 No. 1, 6/32 No. 9; No. 9's band accepts 27/32 of its own and 44/63 and 44/58 of No. 1/No. 2 entries. The three books share arbitraries (one template for Nos. 1/2, and 9/10/12 another), so token share cannot tell the books apart: "readable with No. N" is not licensed by this test, and "book not in hand" at 71 of 130 is a low share, not proof of a missing book. Only the No. 2 band separates somewhat from No. 9 entries. Logged as untestable by this instrument at this N; the next step needs a different instrument (decode a handful of 1865 rows with each book and count grammatical clauses with the shuffled-meaning control of the lane brief), not a tighter band.
Both counts: readable 59 (41 + 18), not in hand 71. No 1865 reading in this job.

## LS3-R9 (8 Oct 2026, account 2, for LANE ST-LEDGER-3)

Ten unread rows of `entries-mssEC19.tsv` that guessed "Cipher No. 9" (old vocabulary). Four read (O9-AK, O9-AL in `ciphertext-no9.txt`; E76, E77 in `ciphertext.txt`, because the rows turned out to be Cipher No. 1);
three recorded N1-likely from the pre-filter, with page, not decoded; three 1865 rows not read (book not in hand). `decode.py`, `decode_no9.py`, `decode_no2.py` `--write` then `--check` exit 0.
Tools: `ls3_r9.py` (shares + matched control, output `ls3_r9_controls.txt`), `ls3_r9_printcheck.py` (letters-only phrase grep), `ls3_r9_entries.txt` (working blocks). Images: the four ledger pages fetched once at 2400 px
(`hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg`), the whole page read by the worker, one eye, no subagent, volunteer text as second witness (no word differs in the four entries);
key pages 1730, 1734, 1739 (mssEC 67 p.[10], [14], [19]) at 1800/1400 px.

| row | ID | book | vocabulary shares (No.1/No.2/No.9 of N non-function tokens) | clause check chosen vs other two vs shuffled-chosen | H | print |
|---|---|---|---|---|---|---|
| 8946/54/2 | O9-AK, 25 Apr 1864, Halleck (signed Applause) to Heintzelman at Columbus O: the Governor of Ohio reports that by Friday next he will have a regiment of militia at Johnson's Island; as soon as relieved send troops there to the field as previously ordered | No. 9 | 6/7/5 of 19 | No.9 5 of 5 code words give the sentence; No.1 0 of 6; No.2 0 of 7; No.9 shuffled 0 of 5 ("Lieutenant ... Goo of (Fort) La Fayette"); No.1 shuffled 0 of 6 | 5 | not located (4 phrases; I/33, I/34 pt 3, I/39 pt 2, I/42 pt 3, ORN I/11 searched) |
| 9015/123/1 | O9-AL, 26 Jul 1864 12.30 PM, Halleck to Kelley at Cumberland (operator Rom): "[Heintzelman] has been directed to give you all the assistance possible from his Dept" | No. 9 | 7/6/5 of 16 | No.9 5 of 5; No.1 0 of 7; No.2 0 of 4; No.9 shuffled 0 of 5 ("Sec. of the Navy ... Arkansas (river)"); No.1 shuffled 0 of 7 | 5 | FOUND, word for word: OR I/37 pt 2 p.453 (12.30 p. m., Halleck to General Kelley, "General Heintzelman has been directed to give you all the assistance possible from his department") |
| 9111/219/1 | E76, 1 Nov 1864 12 M, Butler (signed Knox) to W. P. Smith: "Please let me have your special car for self & staff for the first through train to New York. Strictly confidential. Ack receipt care Colonel Hardie" | No. 1 (was guessed No. 9) | 7/7/4 of 23 | No.1 6 of 6; No.9 0 of 4 ("train to Arkansas (river)"); No.2 0 of 7 ("train to Macon"); No.1 shuffled 0 of 6 ("Meridian ... Cleveland ... Geo. H. Thomas") | 6 | not located (3 phrases, I/42 pt 3, I/33 and the cached volumes) |
| 9143/251/1 | E77, 22 Dec 1864 10.30 PM, G. V. Fox to Commodore Rodgers (operator Sheldon, Ft Monroe, header "No 1"): "Yesterday the fleet were inactive at their destination on account of continued bad weather. This from [Grant]. You may be in time yet" | No. 1 (was guessed No. 9) | 5/6/2 of 20 | No.1: time word = header 10.30 PM, Jersey = Grant, Famish = Norfolk (3 of the 5 decoder values hold; see grades); No.9 0 of 2 (time 8.30 PM against header 10.30); No.2 time matches, other 4 do not (Canby, Jeff Davis, McMinnville); No.1 shuffled 0 of 5 | 3 | FOUND, word for word: ORN I/11 p.204 (Navy Department, 22 Dec 1864, Fox to Commodore John Rodgers, commanding U.S.S. Dictator, Norfolk, "This from General Grant") |
| 8893/1/1 | not decoded (Halleck to Grant, St Louis, 28 Jan 1864) | - | - | - | - | N1-likely: OR I/32 pt 2 p.244 (1.24 p. m., two brigades of Ewell's corps, Sedgwick; expected raid by Morgan through Stone or Sounding Gap, Anderson) |
| 8919/27/2 | not decoded (Halleck, Chief of Staff, to Steele via Clowry, Little Rock, 1 Apr 1864) | - | - | - | - | N1-likely: OR I/34 pt 3 p.27 (Washington, April 1, 1864, 11 a. m.) |
| 9054/162/2 | not decoded (Halleck to Burbridge, Lexington, 22 Aug 1864, via Mattoon) | - | - | - | - | N1-likely: OR I/39 pt 2 p.284 (1.20 a. m.; the ledger header times it 11.30 am, "No 9") |
| 9168/276/2 | not read (header "No 3", 1 P. M., Beckwith, City Point, 24 Jan 1865) | Nos. 3/4 | - | - | - | key not in hand |
| 9274/382/0 | not read (header "No 4", Sheldon, Ft Monroe, 4 Sept 1865) | Nos. 3/4 | - | - | - | key not in hand (LS3-K: "book not in hand") |
| 9283/391/1 | not read (Bates, Boston, 16 Sept 1865; continuation of 9283/391/0, which LS3-K calls "book not in hand") | - | - | - | - | key not in hand |

Page numbers are those of the printed volume read from the djvu text (running heads; the dispatch sits before the next head). Phrases and volumes: `python3 ciphers/eckert-1864/ls3_r9_printcheck.py <scratch *.txt>` (I/32 pt 2, I/34 pt 3, I/39 pt 2, I/42 pt 3 and ORN I/11 were fetched to scratch, not committed). A miss is a search result (rule 10).

Grades (decoder counts; by hand where it differs): O9-AK H 5 (Bologna/Bolivia, Cologne, Stanhope, Youth, Applause); O9-AL H 5 (Pagoda, Viola, Vernon, Bolivia, Applause); E76 H 6 (Francis, France, Zebra, Pandora, Youth, Knox);
E77 H 3 (Reliance 10.30 PM, Famish, Jersey), I 1 (Fox: decoder's [Philadelphia] is the plain surname, as in E67), M 3 (polkaing, Dick, potato: decoder's "[Command = Er]ing" for "polkaing" is a stem artefact, not a reading; the print has "Commanding U.S.S. Dictator" after Rodgers,
so these three words probably spell "commanding Dictator", not graded C because the pairing is the worker's).
Unread, not graded: AK/AL plain-spelling names. Bologna/Bolivia = Heintzelman is a new key row (key-no9.md section 6, mssEC 67 p.[10] l.18, one eye). Data points that agree with it independently: Heintzelman commanded the Northern Department at Columbus (O9-AK's address line), and OR I/37 pt 2 p.453 for O9-AL.
Rank slip, as in O9-A: "Vernon" reads Maj. Gen. in key-no9.md (O9-AL "Maj. Gen. Kelly"); the print has "General Kelley". Not a data conflict; the printed address gives no rank.

Book assignment note (rule 3): the share columns do not pick the book (key-no9.md is a sample table, 5/19 and 5/16 are small shares for the book that reads); the header word (Pagan/Pagoda/Francis/Reliance) and the sentence under each book do. E76 and E77 were guessed No. 9 by the tsv and are No. 1; the time word agrees with the ledger's own header time in both (Francis = 12 under No. 1 against "12M"; Reliance = 10.30 PM against "10.30 P. M."), which the No. 9 reading breaks (11 AM; 8.30 PM). Control note: LS3-K's p10-p90 band is non-selective (its own matched control), so no 1865 row was read.
Time-word check: O9-AL's Viola (12.30 PM in No. 9) agrees with the print's "12.30 p. m." (H against a print time, independent of the sentence).

Image vs volunteer text: no word differs in the four read entries. 9143's page shows "10.30 P. M." above the header and "No 1" in pencil at upper left; 8946's second entry has "No 9" pencilled over "David". 9015's "Vernon" appears as "Vermin"/"Vernon" in the volunteer text for two entries; the image reads Vernon, "Kelly".

Requests: hdl.huntington.org 8 (4 ledger pages, 4 mssEC 67 pages; page 1736 fetched but not read), archive.org 5 (`_djvu.txt`: 322unit, 343unit, 392unit, 423unit, ORN 0011unse), 0 other. Subagents 0.

## Remaining gaps (LS3-R9, 8 Oct 2026)
Read so far: of the ten rows, 4 read (O9-AK, O9-AL, E76, E77); 3 recorded N1-likely with the OR page (8893/1/1, 8919/27/2, 9054/162/2, not decoded); 3 not read (9168/276/2, 9274/382/0, 9283/391/1).
- Print location of O9-AK and E76 - blocker: not-attempted; the sender-family editions were not searched (OR I/33, I/34 pt 3, I/39 pt 2, I/42 pt 3, ORN I/11 were; Butler's Private and Official Correspondence, Heintzelman/Brough papers were not); next: verifier phrase search, ~$0.5
- 9168/276/2 ("No 3"), 9274/382/0 ("No 4"), 9283/391/1 (1865, book not in hand) - blocker: no-key-material; Cipher Nos. 3/4 are not in hand and LS3-K's token-share band is non-selective, so the 1865 rows are untestable by that instrument; next: a Huntington reply on the 1865 books, or decode a few 1865 rows under all three books and compare the time word with the header (a different instrument), ~$1

## Escalation (LS3-R9, 8 Oct 2026)
- [n/a] siblings: the ten are siblings of E21-E77 and O9-A..AJ already read.
- [x] clear-pages: four entries read from the full-page images, volunteer text second witness.
- [x] known-keys: all three books run on all four entries, plus shuffled copies.
- [ ] print: OR I/32 pt 2, I/33, I/34 pt 3, I/37 pt 2, I/39 pt 2, I/42 pt 3 and ORN I/11 searched; Butler and Heintzelman editions not.
- [x] key-rebuild: one row added (Bologna/Bolivia = Heintzelman), key-no9.md section 6.
- [x] image-check: mssEC 67 p.[10] read from the 1800 px image; ledger pages from 2400 px images.
- [n/a] retry: the three 1865 rows are gated by the brief on LS3-K's call, which is "book not in hand".
Verdict: keep going: 1 internal gap; cheapest next: a verifier phrase search for O9-AK and E76 in the sender-family editions, ~$0.5

## LS3-R18 (8 Oct 2026, account 2, for LANE ST-LEDGER-3)

mssEC 18 (object 10074), the parallel sent ledger. Part 1: the 21-22 Apr 1864 pages from the image (started 10:18 UTC by `date -u`).
Route: Huntington IIIF `hdl.huntington.org/iiif/2/p16003coll11:<pointer>/full/full/0/default.jpg`, pointers 9714-9717 = printed pages
48-51 (the printed number is on the leaf; pointer - 9660 = page + 6 here, so "page n = pointer - 9660" of RUN6-ECK is off by two for these
leaves: 9714 is page 48, not 54); 4 image requests, 2 s apart, 2.3-2.4 MB each (6018-6169 x 7200), nothing committed. Crop command run
(the page's ink profile is weak against the dark scan border, so a text-region box was needed; the line finder wrote 21 crops per page, the
worker read the pages at 2000 px wide in three bands instead of 21 crops each):
`python3 tools/iiif_lines.py --image /tmp/.../p9714.jpg --out /tmp/.../c9714 --prefix p9714 --region 620,600,4900,5000 --distance 200 --prominence 20 --smooth 3 --lines-per-crop 3 --max-width 2400 --overlap 100`
(20 lines, 7 bands x 3 segments).
Transcription against the volunteer text (rule 2: the image is the source): all six entries agree with the volunteers' text on every code word;
differences are all in plain words (the image has "service" at E78/N2-BP line 7 where the volunteers have "services", and "sent"/"send" at E78
is ambiguous). One word is doubtful on the image, N2-BP's last signature word, "Yawl" (volunteers) against a hand that could be "Yard"; kept as
Yawl (= Signed in key-no2.md), graded M. Pencilled service notes (a "(1)" after the operator's name at p.48, "No 2" over p.50) are in the
headers.

Entries on the four leaves (all 21-22 Apr; page 49's C. S. Cutler to Gov. Seymour entry is a seventh, below):

| id | file | leaf (printed p., pointer) | hour | book | code-word tokens (key-row grade) | M by hand |
|---|---|---|---|---|---|---|
| N2-BP | ciphertext-no2.txt | 48, 9714 | 21 Apr 1.30 PM | 2 | H 24, C 1 | 3: Yawl/Yard; "spit" = Near (should read "men"); the second "opinion" (key row Field) is the plain word |
| E78 | ciphertext.txt | 48, 9714 | 21 Apr 3.30 PM | 1 | H 12 | 1: Sugar has no key.md row (shown [?]) |
| N2-BQ | ciphertext-no2.txt | 50, 9716 | 21 Apr 7 PM | 2 | H 9 | 0 (5 plain words that are also book words, Humphreys, Rucker, desired, marked, presumed, are on a `plain:` line) |
| O9-BA | ciphertext-no9.txt | 51, 9717 | 22 Apr 3 PM | 9 | H 5 | all 5: no time word in the entry, so the book rests on the words alone; "Randolphed" (probably "armed") has no row |
| O9-BB | ciphertext-no9.txt | 51, 9717 | 22 Apr 10 PM | 9 | H 9 | 1: "Surgery" has no book-9 row |
| (not filed) | -- | 49, 9715 | 21 Apr 5.30 PM, C. S. Cutler, Albany NY, to Gov. Seymour | none of the three | -- | -- |

Not filed: the Cutler entry (printed p.49, 143 tokens). It carries a time word, Rosalie, that is 5.30 PM only in key-no9.md (the header says
5.30 PM), but its other code words read wrongly under book 9 ("Gov [Infantry] Daniel [B. F. Butler]", "the [Maine] requests", "[Jno. Morgan]'s
Escorts") and under books 1 and 2 (Rosalie = 9 PM / 9.30 PM, against the header). Read as: no book in the folder reads it; logged unread, not a
negative about any book family. ec18 (A3V3-ECK18) had it as book 2 with 37 words not in the key; the image agrees with that count. The Horner NY
Ericsson/Tecumseh telegram of 9.40 PM on printed p.50 is in plain words (RUN6-ECK's note stands).

Book assignment (vocabulary shares, tokens of the entry found in key.md / key-no2.md / key-no9.md; the shares do not separate the books, they
include the common words every table carries, so the assignment rests on the ledger-time statistic below, not on them):
E78 12/14/4 of 63; N2-BP 14/24/9 of 85; N2-BQ 6/8/1 of 63; O9-BA 6/7/5 of 39; O9-BB 13/13/9 of 79.

Matched control (rule 3; `python3 ls3_r18_control.py`). The statistic: does the decoded time word equal the time the ledger itself writes in the
entry's header line? That number can differ between the real book, the other two books and a shuffled book, and the shuffle moves the time rows.
Real, books 1/2/9: E78 Y/n/n; N2-BP n/Y/n; N2-BQ n/Y/n; O9-BB n/n/Y; O9-BA has no time word (not testable). Shuffled copy of the chosen book
(meanings permuted among rows of the same kind, 200 seeds, seed 1000+i): time word agrees in 5, 3, 4, 3 of 200 (E78, N2-BP, N2-BQ, O9-BB) and 0 of 200
for O9-BA. So the four timed entries sit on the book their time word picks, one book of three each time, against a 1.5-2.5% shuffle floor.
Hand count of code-word tokens that read as a grammatical clause, chosen book vs the other two (approximate, one reader): E78 10/12 vs 5/12 (book 2),
1/4 (book 9); N2-BP 19/21 vs 3/16 (book 1), 1/9 (book 9); N2-BQ 9/9 vs 4/9 (book 1), 1/1; O9-BB 9/9 vs 2/10 (book 1), 1/10 (book 2); O9-BA 5/5 vs 3/8
(book 1), 1/8 (book 2). A shuffled-meaning decode of each is word salad ("Is your [Talladega] coming [.] [Reinforce] daily", "[Suffolk] The Govrs
of [Failure] [Johnston] [Hunter D]"; samples in the script's output). O9-BA is the weakest: no time word, five tokens.
Readings with the judge: `python3 tools/judge_plaintext.py specs/eckert-1862.json --file ciphers/eckert-1864/ls3_r18_readings.md` ->
`FAIL language: score=-1.123, null_p99=-2.082, real_p05=-0.847, real_median=-0.812, mode=both, N=1941` (bracketed readings, 5 short entries; the en judge is
of unknown reliability, tools/data/en/README.md). Reported as a FAIL. Regeneration: `decode.py`, `decode_no2.py`, `decode_no9.py --check` and
`ls3_r18_control.py --check` exit 0.
What the five say (each carries its source word grades as above, none beats the volunteers' text on a plain word; conditional on the key rows):
N2-BP, War Department to Grant at Culpeper: the governors of Ohio, Indiana, Illinois and Iowa propose to offer 100,000 men within 20 days for 3 months
in fortifications, "the Department would be glad to have your opinion"; signed Secretary of War. E78: to Lt Col H. Biggs, Quartermaster: is your
transportation coming ... daily; orders stop everything coming up the Potomac and send it to Monroe; signed Qr Master Genl U.S. N2-BQ: Benham's reply
to Humphreys, "your 2 telegrams of today are received and the estimates were sent at once to General Rucker, omitting land transportation ... I first
marked the one referred to confidential but not being aware that that would ensure a cipher I changed the words". O9-BA: Halleck to Canby, "what is the
condition of the 14th NY Artillery. Has it been [armed?] and drilled as infantry ... Halleck". O9-BB: Meigs to Maj Van Vliet, Quartermaster, New York:
complete the supply of tugs, ferry boats, barges and schooners for both Fort Monroe and Washington; steamers enough to move troops are now engaged.
Print pre-filter (rule 3 lane point; OR ser. I vols. 32 pt 3, 33, 34 pts 1-4, 35, 36 cached in scratch, phrase search, a 4-gram/500-word overlap scan
and an address/date scan for "April 21/22, 1864" dispatches): no hit for any of the five. Related only: OR 33 prints Halleck to Dix 19 Apr 1864
("Fourteenth New York Heavy Artillery"), Dix's reply 21 Apr, and Halleck to Burnside 23 Apr ("armed as infantry"), which fit O9-BA's subject but are not
its text. Searched: the OCR of those volumes by script, 8 Oct 2026; not searched: the image of any OR page, Butler/Grant/Lincoln editions for these five
(done for part 2 only). Conditional on the OCR.
Not found: a key row for Sugar (key.md), Randolph (key-no9.md), Surgery (key-no9.md); the second copy of any E4/E5 telegram (the Premise question of
section 2, RUN6-ECK) is still not on these four leaves.

### LS3-R18 part 2: the ten A3V3-ECK18 "not found in OR" keyed entries (8 Oct 2026)

Pre-filter first (lane point), by script over the OCR of OR ser. I vols. 32 pt 3, 33, 34 pts 1-4, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, **47, 48, 49**
(47-49 were not in A3V3-ECK18's search; fetched 8 Oct 2026 from archive.org, 2 s apart, not committed) plus Butler's Private and Official
Correspondence vols. 4-5 and "Lincoln in the Telegraph Office" (cached in sources/ia-fulltext/print-check/); plain-phrase regexes taken from the
volunteers' words (A3V3-ECK18's 5-gram test compared decoded *meanings*, so any paraphrase between ledger and print missed). Request count: 10
page images + 10 item JSONs (hdl.huntington.org), 45 archive.org djvu files, all >= 1.6 s apart.

Found in print, so recorded as N1-likely with the page and not decoded further (page numbers are OCR running heads, not checked on an image):
- 9730.87 (mssEC 18 p.64, 4 May 1864 2.30 PM, Sheldon): Grant at Germanna Ford to Halleck, "The crossing of Rapidan effected. Forty-eight hours now will demonstrate whether the enemy intends giving battle this side of Richmond. Telegraph Butler that we have crossed the Rapidan", OR ser. I vol. 36 pt 1, at the head of the correspondence (OCR: p.1, before the p.2 running head), and in Butler's Private and Official Correspondence vol. 4 (the Halleck cipher copy, "May 4, 1864, 3 p.m."). The ledger entry is the Halleck-to-Butler copy.
- 9731.89 (p.65, 5 May 1864, "No 9", 2.20 PM, David Columbus): Halleck to Heintzelman, "Send without delay the first available troops in Ohio, militia or others, to guard the Baltimore and Ohio Railroad from Parkersburg to Cumberland", OR ser. I vol. 37 pt 1, about p.390 (OCR heads 388, 391). **A3V3-ECK18's reading of this entry with key.md ("[President U.S.] ... [Grand Junction] militia ... [Fear] [C. A. Dana]") is the wrong book**: the ledger's own pencilled "No 9" and the time word (Minnie = 2.30 PM in key-no9.md; header 2.20 PM; key.md gives 7.30 PM, key-no2.md 7 PM) point to Cipher No. 9, and the print shows "troops in Ohio" where key.md gives "Grand Junction". Withdrawn from the 28 book-1 entries; not decoded further here.
- 9908.417 (p.242, 6 Dec 1864 10 AM, Geo Gallup, Vicksburg): Halleck to the commanding officer at Memphis, "You will immediately endeavor to cut the Mobile and Ohio Railroad so that Hood's army cannot be supplied by that route", OR ser. I vol. 41 pt 4 (OCR heads 781) and vol. 45 pt 2 (pp.80-81). Conflict with key.md for the ledger's word "girls": key.md reads it "Vicksburg" (H), the print has "Memphis" at that place. Logged for the key row (a data conflict, rule 4): the ledger header names Vicksburg (the operator's station), and the printed copy is addressed to Memphis, so either the row is wrong or the same text went to two commanders; not settled here.
- 9939.484 (p.273, 21 Jan 1865 3 PM, Sheldon): Grant to Brig. Gen. J. M. Palmer at Fort Monroe, "Wait at Fort Monroe until I get there. I will leave Annapolis at 5 a.m. to-morrow", OR ser. I vol. 46 pt 2, p.198 (OCR heads 197, 198, received 3 p.m.; the same hour as the ledger's header). The ledger's "an apple is" is the clerk's plain-letter spelling of "Annapolis", which ec18's reading rendered as [Sumter] "is at".

Not found in the print sources above (phrase search, conditional on OCR) and read from the image, filed in ciphertext.txt with the ledger's own hour and book labels:
| id | leaf (printed p., pointer) | header | ledger label | time word vs header (books 1/2/9) | code-word tokens | reading, short |
|---|---|---|---|---|---|---|
| E79 | 146, 9812 | Sampson, Balto, 5 Aug 1864 12 pm | none seen | 12 = 12 pm, Y/n/n | H 14 | to Capt Thomas, Quartermaster: charter and send to City Point at once all steamers fit for service on the bay and rivers in transportation of troops which are available in Baltimore, report names by telegraph; signed Qr Master Genl U.S. |
| E80 | 189, 9855 | W T Mason, Cairo, 1 Oct 1864 | "#1" | header has no hour, not testable | H 15 | 1 Oct to D. D. Porter, Cairo: send two light draft iron clads, the best you have, to Farragut in Mobile bay; in an emergency call upon him for the Tennessee and [gunboat]; signed Secretary of Navy, "[Sheridan] has done well" |
| E81 | 192, 9858 | Sheldon, Ft Monroe, 4 Oct 1864 2 PM | "No. 1" | the entry has no time word (plain words after the address), not testable | H 5 | 4 [Oct] to Colonel Webster, Chief Quartermaster: send here immediately all the steamers(?) that can possibly be spared; signed D H Rucker |
| E82 | 200, 9866 | Horner NY, 13 Oct 1864 3 pm | "No 1" (circled) | 3 pm, Y/n/n | H 6 | to Colonel L C Baker, New York: give description and marks of boxes so that they can be identified and report by what route they have gone |
| E83 | 235, 9901 | G D Sheldon, Ft Monroe, 29 Nov 1864 | none | header has no hour, not testable | H 11 | 29 [Nov] to Colonel R C Webster, Quartermaster, Monroe: send here immediately every available steamer and propeller you have in service at your post that can be spared; signed D H Rucker |
| E84 | 262, 9928 | Sheldon, Ft Monroe, 3 Jan 1865 1.30 PM | "No 1" | 1.30 PM, Y/n/n | H 7 | to Colonel Webster, Quartermaster: if you have any surplus vessels fit for sea not required at your place send them to Baltimore to report to the Chief Quartermaster; signed R Ingalls |
All six are book 1 by the same two statistics as part 1 (`ls3_r18_control.py`: the time word under the three books against the header hour, and a 200-seed
shuffle of book 1's meanings, which agrees with the header hour in 8, 0, 0, 2, 0, 5 of 200 for E79-E84), and by the ledger's own "No 1"/"#1" label where one is written
(E80, E81, E82, E84; no label on E79 and E83, and neither is contradicted). Books 2 and 9 under the same entries read word salad ("[Failure] for [Battled] Thomas
[Rations] [1000] Charter & send to [Cairo] at once all [Transportation]ers", E79 book 2). Hand count of code-word tokens reading as a grammatical clause, book 1 vs 2
vs 9: E79 13/14, 2/14, 1/4; E80 14/15, 2/13, 1/5; E81 4/5, 0/3, 1/1; E82 5/6, 1/8, 0/3; E83 10/11, 1/8, 0/2; E84 6/7, 1/6, 1/4.
Corrections to the volunteers' text and to ec18's reading, from the image: "Charter" (E79) and "Webster" as the addressee's surname (E81, E83, E84) are plain
words that are also book rows ([Knoxville]er, [signed]); they are on `plain:` lines, which moves E79 from H 15 to 14 and takes E81/E83/E84 out of an early signature tail. In E81
the word is "Weaslers" on the image (E79, E83 "weaselers"), unread; "Ironic lads" (E80) is plain, "iron clads".
Not matched in print: E79, E80, E81, E82, E83, E84 (the six above; the sentence of E80 has no OR/Butler/Lincoln hit for "Farragut ... Tennessee"; the Navy Official Records (ORN) were not searched).
Remaining: ORN for E80; the three Quartermaster-General requests E81, E83, E84 have the same clear body as Horner's 4 Oct entry on the same leaf (9858, "Send all weaselers that can possibly be spared ... By order Bender walrus Geo D Wise"), which is a plain/code sibling pair a C-grade alignment could use (one-line suggestion; not run, brief met).
Not done: the other 18 of A3V3-ECK18's 28 fully keyed book-1 entries were not re-tested for the wrong-book finding; 9731.89 shows the assignment by key.md alone can be wrong for an entry the ledger labels "No 9".
Judge (rule 7), all eleven readings of this section and part 1: `python3 tools/judge_plaintext.py specs/eckert-1862.json --file ciphers/eckert-1864/ls3_r18_readings.md` -> `FAIL language: score=-1.141, null_p99=-2.109, real_p05=-0.845, real_median=-0.813, mode=both, N=3603` (reported as a FAIL; bracketed readings of short entries, unknown-reliability en judge).
Regeneration: `decode.py --check`, `decode_no2.py --check`, `decode_no9.py --check` and `ls3_r18_control.py --check` exit 0.


LS3-V18a correction note (8 Oct 2026, verifier, see AUDIT.md "## AUDIT (LS3-V18a)"): **N2-BP is in print**, word for word, OR ser. III vol. 4 pp.238-239
(Stanton to Grant, 21 Apr 1864; IA `cu31924079575373`) -- N1; the part-1 pre-filter covered OR ser. I only. E78's "Sugar" = Interrogation in key.md (the decoder's
"[?]"), so it is H; the unread word is "mangle". N2-BP's "spit" reads "men" in the print (key-no2.md has Near: a key-row conflict). O9-BA's image has "rabbits";
its five code words are H (book fixed by Applause = Halleck and the 23 Apr print "armed as infantry"). LS3-R9's O9-AL and E77 confirmed N1 by script; the
Bologna/Bolivia = Heintzelman row confirmed by a second eye. Classes: E78, N2-BQ, O9-BA, O9-BB, O9-AK, E76 N3 (three weak); N2-BP, O9-AL, E77 N1.
## LS3-R18b (8 Oct 2026, account 2, for LANE ST-LEDGER-3)

The last seven A3V3-ECK18 keyed entries (started 10:42 UTC by `date -u`). Fetch: 7 leaf images from hdl.huntington.org (IIIF full, 2 s apart, not committed), 10 OR `_djvu.txt` (ser. I vols. 46.1-49.2, archive.org, 2 s apart, scratch, not committed), vol18.json (sha256 matches pilot1864/manifest.tsv). Crops: `python3 tools/iiif_lines.py --image p9943.jpg --out c9943 --prefix p9943 --region 620,600,4900,5000 --distance 200 --prominence 20 --smooth 3 --lines-per-crop 3 --max-width 2400 --overlap 100 --debug` (same for 9948, 10028, 10031; 9948's bottom entry needed `--region 400,5300,5400,1700`). Read: the debug overlay of each page plus individual crops for doubtful words, one reader.
Pre-filter (`ls3_r18b_printcheck.py OR_DIR`, plain phrases, letters only, OR 46-49 + Butler 4-5 + Lincoln in the Telegraph Office):
- Found in print, recorded N1-likely with page (OCR running heads; not decoded further): 10002.578 (1 May 1865 9 PM, Grant to Pope, OR 48/2 p.283); 10026.621 (1 Jun 1865 10 AM, Grant to Reynolds, Little Rock, OR 48/2 p.720); 10027.623 (2 Jun 1865 10 AM, Grant to Pope, arms for freight over the plains, OR 48/2 p.730, with the Stanton indorsement p.731). All three were already matched by A3V3-ECK18's vols. 47-49 step by date (page numbers there differ by OCR head).
- Not found: 9943.494, 9948.507, 10028.625, 10031.632. Plain phrases for each, and after decoding the decoded wording, searched in the same set: no hit ("on board the Stromboli" none anywhere in 46-49; "sale of liquor on the lines" none). Conditional on the OCR; OR vols. 46-49 only for these, ORN not searched.
Leaf facts that change the ledger's book assignment: 10028.625 carries the ledger's own "9" over the operator's name (image), so A3V3's book-1 reading was the wrong book; the entry is filed as O9-BC. Its clear text is the same telegram as 10027.624 (Horner NY, label "1"): "Suppress all sale of liquor on the lines traveled by [troops] returning to be mustered out and at rendezvous for discharge until [troops] are all dispersed": the book-9 value Troops for "yoke"/"youth" sits where book 1 reads "whist"/"whistle" in the sibling (C-grade cross-check of one row).
| id | file | leaf (printed p., pointer) | header | book basis | tokens | result |
|---|---|---|---|---|---|---|
| E85 | ciphertext.txt | 277, 9943 | G D Sheldon 24 Jan 1865, signed H A Wise | none: no label, header has no hour | book 1 H 28 | KEY NOT IN HAND, not claimed (book 1 decode is coherent, "Steamer Nevada will be at Monroe in a day or 2 with recruits ... torpedoes ... Stromboli", but nothing independent selects book 1; shuffle control 0 time agreement) |
| E86 | ciphertext.txt | 282, 9948 | John Horner 31 Jan 1865 11.30 AM | time word 11.30 AM = header (books 1 and 2 both; 6/200 in the shuffle), and the decoded day token [31] = header day (3/200; both statistics 1/200) | H 9 | read, book 1: "[Washington] 11.30 AM [31] for [Maj Gen Dix]: Please come to [Washington] at your earliest convenience; very fine day" |
| E87 | ciphertext.txt | 365, 10031 | Capt Sam Brook, Lvl, 15 Jun 1865 5 PM | none: no label, no time word under any book | book 1 H 13 | KEY NOT IN HAND, not claimed |
| O9-BC | ciphertext-no9.txt | 362, 10028 | Stevens, Cin, 2 Jun 1865 10.30 AM | ledger "9" and time word 10.30 AM = header (book 9 only; 6/200 in the 200-seed shuffle of book 9) | H 4 | read, book 9: "[Washington] 10.30 AM second for Borgia: Suppress all sale of liquor ... [troops] ... [troops]"; four code tokens, one of them the time |
Hand clause counts, chosen book vs the other two: E86 9/9 vs 3/8 (book 2), 1/3 (book 9); O9-BC 4/4 vs 1/4 (book 1), 0/4 (book 2). E86 is the weaker claim: it has no ledger label, and book 2 shares the time word.
Not claimed here: E85 and E87 (left in the files with the header flag, excluded from ls3_r18_readings.md). The three entries above stay with A3V3-ECK18's print match; nothing was added to them.
Judge (rule 7), the thirteen readings of ls3_r18_readings.md: `FAIL language: score=-1.146, null_p99=-2.115, real_p05=-0.849, real_median=-0.811, mode=both, N=4058` (short bracketed readings; the en judge is of unknown reliability). Regeneration: `decode.py`, `decode_no9.py`, `decode_no2.py` and `ls3_r18_control.py --check` exit 0.
Corrections to the volunteer text from the image: 9943 "milly" (not "wilby"); 10031 operator "Capt Sam Brook Lvl"; 9948 Horner "Convenience" tail "very fine day This". 0 subagents; hdl.huntington.org 8 requests (vol18 + 7 leaves), archive.org 10.

Note (LS3-V18b, first verifier, 8 Oct 2026; AUDIT.md "## AUDIT (LS3-V18b)"): E80 is printed word for word in ORN ser. I vol. 26 p.575
(Welles to Porter, 1 Oct 1864) -- N1; E81 and E82 are clear text in the Huntington's public transcription apart from one body word -- N1;
E79's substance is in Meigs's clear order of the same hour to Crosman on the same leaf -- N2, D3; E83 and E84 weak N3 at D2. Corrections:
E82 "Grapes" is the blind word, not [Washington], and "In san it he" = Insanity = C. A. Dana (signer); E81 "Weaslers" = steamers (I);
`ls3_r18_control.py`'s date column tests April headers only (part 2's "date n/n/n" is a non-test; by hand the day numerals agree under
No. 1 for E79, E80, E81, E83); the 9858 Horner sibling is a parallel order to Van Vliet at New York, not E81's telegram.

Note (LS3-V86, first verifier, 8 Oct 2026; AUDIT.md "## AUDIT (LS3-V86)"): O9-BC is printed word for word in the Urbana Union (Ohio),
7 June 1865 p.2, as Grant to Hooker, Washington 2 June 1865, inside Special Orders No. 300, Tod Barracks -- N1; Borgia = Hooker and Ranger =
Grant (C, from the print; candidate rows for key-no9.md). E86's body is clear in the Huntington public transcription of 9948 except Grapes
(Washington) -- N1, D1. E86's leading "Growl" is the No. 1 blind word, not [Washington]. Next, for a reader, ~$0.2: add Borgia/Ranger rows
(grade C, citing the Urbana Union) to key-no9.md and mark Growl as the blind word in reading.md.

## PF4 (8 Oct 2026, account 1, for LANE ST-LEDGER-4)

A pre-filter, not a reading: nothing was decoded; a ranking with a stated error rate, not a verdict (rule 10). Script `prefilter_ls4.py`
(imports the segmenter and vocab of `entries_mssEC19.py`; `--offline` re-runs from the caches in `sources/ia-fulltext/print-check/ls4/`
and reproduced `prefilter-ls4.tsv` byte for byte); output `prefilter-ls4.tsv` (115 pool rows, 12 control rows), `prefilter-ls4-parents.tsv`
(volume title of every Huntington parent object that produced a hit). Intake gate: `partial (line 3)`, exit 0 (pasted in the brief).

**Pool** (selecting script output): rows of `entries-mssEC19.tsv` with `already_read` blank, pointer < 9149, group 1 = `cipher_guess` 9: 5;
group 2 = `cipher_guess` 2, priority 1 or 2: 37; group 3 = `cipher_guess` 1, priority 1 or 2: 73; total 115. Order within a group: lowest widened cover first.

**(a) Print, widened.** IA volumes with `_djvu.txt`, found by metadata calls and logged: OR ser. III vol. 4 = `cu31924079575373`
(dates 1860-65, 677 of the 1864 date strings), OR ser. III vol. 5 = `cu31924079575381` (1863-66), ORN ser. I vol. 11 = `officialrecordso0011unse`
(1864-65), ORN ser. I vol. 12 = `officialrecordso0012unse` (1861-62, 1865). The LS-PRE window cover (rare 3-grams, max frequency 40, window
400, threshold 7 plain tokens) was run over these four only and joined with the LS-PRE `or_cov` as `or_cov_widened` (the ser. I volumes were not
rescanned). Phrases: the rarest run of 4 consecutive plain words whose words each occur at least twice in the added volumes, two per row for groups 1-2, one per row for group 3
(archive.org request budget), through `be-api.us.archive.org/fts/v1/search?q="phrase"` with no identifier; print-likely by phrase = at most 20
items and one of them a work whose title or identifier names the war records or a correspondent (Grant, Lincoln, Sherman, Stanton, Halleck, Butler,
Welles ...). The hit identifiers are in `print_hits`; page numbers are not a locator for this API and are not recorded. 8 pool rows have no run of 4 plain words (phrase not testable).
**(b) Huntington full text.** `dmQuery/p16003coll11/CISOSEARCHALL^w1 w2^all^and/title!transc/nosort/20/1/0/0/1/0/json` (the transcription
comes back in the result, so a hit costs no second request); the two rarest plain words per row; a second pair only if the first returned more than 20 hits and no strong hit.
Each hit other than the row's own pointer is scored by the cover of the row's plain rare 3-grams (y at 7 or more, u at 3-6) and by the share of ALL the row's
3-grams found in the hit (copy at 0.5 or more, the same text in cipher); y or copy gives `clear-sibling`. The row's own transcription "mostly clear" was NOT
turned into a flag: see the control. **(c) Same leaf and neighbours** (offline): entries on the pointer and +/-1 page; same day and (same sender name, or same header time, or at least 3 shared rare plain tokens), or at least 5 shared rare plain tokens on any day.

**Known-answer control (rule 3), run before the pool, same code, same thresholds, nothing tuned after it.** Twelve entries; the mssEC 18 leaves
(9714, 9717, 9901, 9948, 10028 and the six neighbour leaves 9900, 9902, 9947, 9949, 10027, 10029) were fetched from the Huntington with `tools/huntington_transc.py`
and are committed as text in `sources/mssEC18/`.
| entry | audit result | flagged | by |
|---|---|---|---|
| N2-BP | lowered, print OR III/4 | yes | print-likely: widened cover 41 (OR III/4) |
| E70 | lowered, Huntington text | **no** | clean (cover 4); the body is clear in the entry's own transcription |
| E74 | lowered, Huntington text | **no** | clean (cover 4); same |
| E76 | lowered, body clear in Huntington text | **no** | clean (cover 4); same |
| E83 | lowered N2, print OR I/43 pt 2 p.695 + same-leaf sibling | yes | clear-sibling: Huntington hit 5811 in mssEC 25 (the Fort Monroe ledger) y+copy, cover 25, 0.82 of all 3-grams; not the audit's reason (the OR I/43 volume and the same-leaf sibling were not hit) |
| E86 | lowered, Huntington/print | **no** | clean (cover 4); only `u` Huntington hits (cover 3-4, 0.05-0.11 of 3-grams), below the flag line |
| O9-BC | lowered, press (Urbana Union) | yes | clear-sibling+dup, not for the audit's reason: the clear same-day sibling 10027/3 (Horner NY) is on the same leaf |
| E77 | lowered, print | yes | print-likely: widened cover 17 |
| O9-AL | lowered | yes | dup: 9015/0 (3 shared rare tokens, a read entry), not the audit's reason |
| E78, O9-BB, O9-BA | held N3 by two audits | no, no, no | clean (covers 6, 3, 4) |
**Recall 5 of 9 lowered entries flagged; false flags 0 of 3 held entries.** 5 of 9 is not under the brief's line of 5, so no fix was made before the pool (not
tuned on the control). Which check missed: the four misses (E70, E74, E76, E86) are entries whose body is clear in their OWN Huntington transcription; none of a, b or c can see that,
and the statistic that was tried to see it did not separate them: the share of an entry's word pairs found in the added volumes is 0.33 (E70), 0.59 (E74), 0.47 (E76), 0.40 (E86)
against 0.50 for the held O9-BA ("clear words public", still N3 weak); the code-vocabulary fraction is 0.13-0.43 on both sides. So the filter does not catch "mostly in clear"
entries, and a clean row can still be one. Three of the five flags (E83, O9-BC, O9-AL) came from a check other than the one that settled the audit; only 2 of 9 (N2-BP, E77) were flagged for the audit's own reason, so the recall figure is partly luck of overlap. Control sample: 12 entries,
a rate, not a proof.

**Results, counts per verdict per group** (a row may carry several; component counts):
| group | rows | clean | print-likely | clear-sibling | dup |
|---|---|---|---|---|---|
| 1 (`cipher_guess` 9) | 5 | 0 | 5 | 1 | 2 |
| 2 (`cipher_guess` 2, prio 1-2) | 37 | 25 | 7 | 0 | 5 |
| 3 (`cipher_guess` 1, prio 1-2) | 73 | 54 | 9 | 3 | 11 |
| total | 115 | 79 | 21 | 4 | 18 |
Checked rows: all 115, 0 unchecked. Caveats the reader should know: 8888:0 (group 3) is the page-top run-on of a leaf that recurs in 13 other ledgers (a page header, not a telegram);
7 of the 18 dup rows are weak (same day and same sender or same time only, no shared rare token: 9067/1, 9067/2, 8916/2, 9119/0, 9022/1, 9063/1, 9071/1); 8916/2 and 9071/1 have an already-read sibling.
Group 1's 5 of 5 print-likely come from ORN I/11-12 covers of 12-31 and phrase hits in OR/Grant volumes, ranked by the same thresholds that gave 0 of 3 false flags on the control; the covers are modest next to N2-BP's 41.
Six clean rows carry a `u` Huntington hit (8902/0, 9125/1, 9062/1, 8967/2, 9034/1, 8907/1): a partial overlap, not a flag.

**Clean rows by group, in the order a reader should take them** (lowest widened cover first; pointer/entry; groups 1: none):
- group 2 (25): 8887/0 8915/1 8988/1 8902/0 9024/1 9057/2 9065/2 9067/0 9125/1 9126/0 9132/0 8982/1 8986/1 9040/0 9052/1 9060/2 9066/1 9121/1 9122/2 9125/2 9142/0 8948/2 8967/0 8971/2 9003/0
- group 3 (54): 9048/0 9097/0 9123/3 8965/1 8967/1 8996/1 9003/2 9030/0 9047/1 9049/2 9097/1 9116/2 9119/1 9125/3 9128/2 9134/1 9138/2 9140/2 8921/1 8922/0 8969/3 8982/2 8992/0 8996/0 9020/1 9036/0 9043/0 9049/1 9053/2 9055/1 9062/1 9062/2 9086/1 9088/1 9090/1 9113/1 9131/1 8898/1 8967/2 8984/1 9034/1 9072/0 9124/0 9124/1 9129/1 8907/1 8992/1 9034/0 9044/1 9081/0 9098/1 9120/0 9139/1 9144/0
Next for the lane: read from the top of group 2, then group 3; a clean row is "not found in what was searched" (OR ser. I vols 32-52, III vols 4-5, ORN I vols 9-12, IA phrase search,
Huntington full text, same-leaf siblings), never "unprinted" (rule 10), and the four control misses show it can still be an entry that is mostly clear in its own transcription.

Requests (counted in `sources/ia-fulltext/print-check/ls4/requests.json`): hdl.huntington.org 168 (115 pool queries, 12 control queries, 26 parent-title lookups, 9 control leaf fetches, about 6 probes; no 429 or 403);
be-api.us.archive.org 183 (31 control, 144 pool, about 8 probes; the endpoint answered 502 on roughly one call in five, each retried once after 4 s, no 429 or 403); archive.org 15
(metadata and `_djvu.txt` for four volumes, one advancedsearch). No other host.

## Remaining gaps (PF4, 8 Oct 2026)
Read so far: 0 of the 79 clean pool rows read (this pass reads nothing); 115 of 115 pool rows pre-filtered, 21 flagged print-likely, 4 clear-sibling, 18 dup.
- the 79 clean rows - blocker: not-attempted; clean here means not found in the searched print, Huntington text and same-leaf neighbours; next: a reader on group 2 from 8887/0 down (25 rows) then group 3, ~$0.55 per entry
- entries mostly in clear in their own Huntington transcription - blocker: not-attempted; the control missed 4 of 9 such lowered entries and no mechanical flag separates them from held O9-BA; next: a reader or verifier checks each row's own transcription before a first decode, ~$0.1 per row

## Escalation (PF4, 8 Oct 2026)
- [n/a] siblings: same-leaf neighbours checked offline for all 115 rows (check c).
- [n/a] clear-pages: nothing read in this pass.
- [n/a] known-keys: nothing decoded in this pass.
- [x] print: OR III vols 4-5 and ORN I vols 11-12 added to the LS-PRE scan; be-api phrase search on every testable row.
- [n/a] key-rebuild: no key work in this pass.
- [n/a] image-check: no token read, so none to image-check.
- [n/a] retry: no read attempted.
Verdict: keep going: 2 internal gaps; cheapest next: a reader on the clean rows of group 2 in the order above, ~$0.55 per entry

## LS4-R2a (8 Oct 2026, account 1, for LANE ST-LEDGER-4)

The first ten clean rows of PF4's group 2 (Cipher No. 2). One row is not a telegram (8887/0, the ledger's front cover, pointer 8887, page -5), one is skipped at step 0 (8902/0), eight were read: N2-BR..N2-BY in `ciphertext-no2.txt`, read with key-no2.md (`decode_no2.py --write`, `--check` exit 0; `decode.py --check` and `decode_no9.py --check` exit 0). Every ledger page was fetched once at 2400 px (`hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg`), line crops cut with `tools/iiif_lines.py`, read by the worker (no subagent), the volunteer text (sources/mssEC19/p<pointer>.json) as second witness. Working files: `ls4_r2a_entries.txt` (blocks as transcribed), `ls4_r2a_controls.py` (shares + controls, same shuffle as ls3_r9.py with seeds 7, 11, 13), `ls4_r2a_controls.txt` (its output).

**Step 0 (own transcription, before decoding).** None of the ten is mostly clear in its own transcription. 8887/0: front cover ("United States Military Telegraph, War Department. Sent"), not an entry. 8902/0: PF4's `u` hit (pointer 10175, mssEC 10 "Received" p.33) was read first: it is the same text in clear (`Lee one month ago had forty six thousand besides cavalry brigade, seventeen hundred left for N C six thousand furloughed ---- has now thirty five thousand Hampton Cavalry six thousand Lomax brigade of Lee's division sixteen hundred are all the cavalry Lee has --- Fitz Lee disbanded four thousand for want of forage sig J S Mc Phail`), so the row is **N1-likely: clear in the Huntington's public transcription (pointer 10175)** and is not filed (the page is also only the tail of an entry begun on p.9, no header). I had already transcribed and decoded the page before step 0 caught it (the lines read as that text under key-no2.md, H 33 of 51 tokens; No. 1 H 17, No. 9 H 4, shuffled 33/33/32: no clause under any other book); cost about 0.4. 9125/1: its `u` hit (pointer 2951, mssEC 5 p.61, Sykes/Burnside telegrams of Aug 1862) does not state the substance; read.

**Per-entry table.** Shares = tokens of the entry's non-function words found in key.md / key-no2.md / key-no9.md (of N). Clauses: whether the chosen book gives a grammatical sentence (by hand, one reader) against No. 1, No. 9 and three meaning-shuffled copies of No. 2 (seeds 7, 11, 13). Decoder H counts tie with the shuffles by construction (a shuffle keeps which words are in the key), so they are not the test; the clause reading and the header time word are. Time word = the cipher's time word against the ledger's own header time (a check that can differ between books).
| row | ID | date, to / from (decoded) | shares No.1/No.2/No.9 of N | clause: No. 2 / No. 1 / No. 9 / shuffles | time word No.2 vs header (No.1, No.9) | H / C / I | print |
|---|---|---|---|---|---|---|---|
| 8915/1 | N2-BR | 18 Mar 1864 3.30 PM, to Grant: "This Department will not transfer Troops from Steele's Command unless at your request" (signed Secretary of War) | 10/12/3 of 13 | yes / no / no / no (0 of 3) | 3.30 PM = header 330 P.M. (No.1 3 PM, No.9 5 PM) | 10 / 0 / 0 | not located (be-api 2 phrases) |
| 8988/1 | N2-BS | 20 June 1864 3 PM, Halleck to Grant: "The last of the Siege Train has just started, the coe horn mortars included" | 8/12/2 of 17 | yes / no / no / no (0 of 3) | 3 PM = header 3 pm (No.1 3.30 PM, No.9 6 PM) | 10 / 0 / 1 (date word "Morgan" = 19 where the header and the print say 20) | FOUND word for word: OR I/40 pt 2 (`warofrebellion402unit`), War Department, Washington, June 20, 1864, Halleck to Grant, Bermuda Hundred; also Grant Papers vol. 11 by phrase hit |
| 9024/1 | N2-BT | 30 July 1864 7 AM (cipher), Couch to Halleck, copy for Grant: "The Rebels [entered Chambersburg] at about 3 AM this day. Averill was at Green Castle" | 9/11/4 of 23 | yes (frame; "hin terd Shame burr splurge" unkeyed) / no / no / no (0 of 3) | 7 AM; print "6.45 a. m." (No.1 7 AM, No.9 1 AM) | 11 / 0 / 0; M 5 tokens (hin terd Shame burr splurge: the print gives "entered Chambersburg", the pairing is the worker's) | FOUND word for word: OR I/37 pt 2 (`warofrebellion372unit`), Carlisle, Pa., July 30, 1864, 6.45 a. m., Couch to Halleck |
| 9057/2 | N2-BU | 29 Aug 1864, for Grant and sent to Sherman: rumors that Hood is killed and Longstreet in command at Atlanta; the military agent at Gallipolis telegraphs Gov. [Bruff] that Breckinridge with 8000 men has advanced into the Kanawha Valley by way of Lewisburg | 18/23/2 of 34 | yes / no / no / no (0 of 3) | no time word in the entry header | 21 / 0 / 1 | not located (be-api 4 phrases; OR I/43 pts 1-2 cached, "Gallipolis" near 27-30 Aug none) |
| 9065/2 | N2-BV | 7 Sept 1864 10.30 AM (cipher), for Lieut. Gen. Grant: "I've received your telegram and will attend [tooth line] this side of Point Lookout [Act comack] is beyond my control" (tail "Gimlet I owe you one" unread) | 8/8/2 of 22 | partial / no / no / no (0 of 3) | 10.30 AM; no header time | 7 / 1 / 0; M "tooth line", "Act comack", "Gimlet" | not located (3 phrases); the generic phrase "I have received your telegram and will attend" hits Papers of U. S. Grant vol. 12 (not opened; generic) |
| 9067/0 | N2-BW | 7 Sept 1864 9.30 PM, Harpers Ferry, Stevenson to the Secretary of War: "All reports from front confirm the retiring of the enemy. A heavy cavalry reconnoissance is being made in direction of Winchester ... Nothing from Sheridan on the subject" | 19/25/8 of 32 | yes / no / no / no (0 of 3) | 9.30 PM = header 9.30 pm (No.1 9 PM, No.9 5.30 PM) | 20 / 0 / 1 | FOUND word for word: OR I/43 pt 2 (`warofrebellion432unit`), Harper's Ferry, September 7, 1864, Stevenson to Stanton ("Deserters and prisoners report the enemy falling back to Fisher's Hill") |
| 9125/1 | N2-BX | 18 Nov 1864 4 PM (cipher), to Grant: "Please come this way if possible on your return" (signed Secretary of War) | 5/6/2 of 13 | trivially (the sentence is plain words; six code tokens) / - / - / - | 4 PM; no header time | 6 / 0 / 0 | not located (1 phrase) |
| 9126/0 | N2-BY | 22 Nov 1864 8 PM (cipher), to Brig. Gen. Rawlins: "I will not [be at] City Point until Thursday" (signed Grant) | 6/8/2 of 11 | yes / no / no / no (0 of 3) | 8 PM; no header time | 8 / 0 / 0 | not located (2 phrases) |
Totals over the eight filed entries: H 93, C 1, I 2 (decoder), M 8 by hand (N2-BT 5, N2-BV 3). All eight carry an H count; N2-BX (six code tokens) and N2-BV (seven) are too short to carry a clause above the authentication distance on their own; the control (clauses and time words) separates No. 2 from No. 1, No. 9 and the shuffles on the other six.

**What was found and not found.** Not found in what was searched: N2-BR, N2-BU, N2-BV, N2-BX, N2-BY (be-api phrases, 1-4 each, and the cached OR I/43 pts 1-2, I/45 pt 2, I/37 pt 2, I/36 pt 2, I/33 where the date falls; not searched: Grant Papers vol. 11-12 pages, Lincoln, the press of the day, Stanton/Halleck papers). Found in print: N2-BS (OR I/40 pt 2), N2-BT (OR I/37 pt 2), N2-BW (OR I/43 pt 2): PF4 had listed all three clean; its OR cover for N2-BW and N2-BT was 3 (the entries are 25 and 24 words with a few plain runs), so a clean row from PF4 is still "not found in what was searched". Of the ten rows: 1 not an entry (front cover), 1 step-0 skip, 3 found in print, 5 not located. Keys: key-no2.md rows used unchanged; the print gives "Fisher's Hill" for "Fishers ration" (ration = Hill, H already in key), and "entered Chambersburg" for the syllable-split words of N2-BT (not added to the key: one witness, the pairing is mine).

Print pass (be-api phrases of the decoded text, no identifier; script `/tmp`-scratch `fts.sh`, results here): N2-BR "will not transfer troops from Steele's command", "not transfer troops from General Steele's command unless at your request": 0, 0; N2-BS "the last of the siege train has just started" 6 hits (OR I/40 volumes, Grant Papers 11); N2-BU 4 phrases 0; N2-BV 3 phrases, 1 hit on the generic one; N2-BX 1 phrase 0; N2-BY 2 phrases 0.

Crop commands (S = session scratch, 2400 px pages): `python3 tools/iiif_lines.py --image $S/img/p8915.jpg --out $S/crops/8915 --prefix p8915 --region 150,1440,2200,540 --lines-per-crop 2 --max-width 2400`; p8988 `150,1850,2200,420`; p8902 `150,330,2200,1060` (read, then skipped); p9024 `150,950,2200,470` (last line re-cut by hand `150,1400,2200,160`); p9057 `150,900,2200,680`; p9065 `150,1600,2200,520`; p9067 `150,260,2200,780`; p9125 `150,240,2200,360` (`--lines-per-crop 3`); p9126 `150,250,2200,300` (`--lines-per-crop 3`). Image vs volunteer text: N2-BS image "started" for "stated"; N2-BW image "ravens" for "raven"; no other word differs in the eight entries.

Requests: hdl.huntington.org 11 (nine page images, two dmGetItemInfo for the `u` hits), be-api.us.archive.org 14 (no 429/403), archive.org 1 (`_djvu.txt` OR I/40 pt 2), no other host. Subagents 0.

## Remaining gaps (LS4-R2a, 8 Oct 2026)
Read so far: of the ten rows, 8 read (N2-BR..N2-BY), 1 skipped at step 0 (8902/0), 1 not an entry (8887/0).
- Print location of N2-BR, N2-BU, N2-BV, N2-BX, N2-BY - blocker: not-attempted; the sender-side editions (Papers of U. S. Grant vols 10-12 pages, Lincoln, Stanton/Halleck/Rawlins papers) and the press of the day were not searched; next: a verifier phrase search, ~$0.5 per entry
- N2-BT's "hin terd Shame burr splurge" and N2-BV's "tooth line", "Act comack", "Gimlet" - blocker: no-key-material; these words are not in key-no2.md; next: a second clear/print witness for the pairing, ~$0.3
- the 15 further clean group-2 rows of PF4 (9132/0 onward) - blocker: not-attempted; the brief named ten rows only; next: reader, ~$0.55 per entry, noting that 3 of 8 read here were in print

## Escalation (LS4-R2a, 8 Oct 2026)
- [x] siblings: PF4's same-leaf check (none) plus the step-0 read of each row's own transcription and its `u` hits.
- [x] clear-pages: eight entries read from the 2400 px page images, line crops, volunteer text as second witness.
- [x] known-keys: key-no2.md applied to all; key.md and key-no9.md and three shuffled No. 2 copies as controls.
- [ ] print: OR vols 37 pt 2, 40 pt 2, 43 pts 1-2, 45 pt 2 and be-api phrases done; Grant Papers pages, press and sender papers not.
- [n/a] key-rebuild: no row added.
- [x] image-check: every token read from the image.
- [n/a] retry: no read failed, so nothing to retry.
Verdict: keep going: 2 internal gaps; cheapest next: a first verifier on N2-BR, N2-BU, N2-BX, N2-BY (the not-located entries; N2-BV is too short), ~$2

## LS4-R1a (8 Oct 2026, account 1, for LANE ST-LEDGER-4)

Ten clean rows of PF4's group 3 (Cipher No. 1 guess), read from line crops of the page images (one eye, no subagent), the Huntington volunteer text as second witness.
One row stopped at step 0 (9048/0); nine read: seven are Cipher No. 1 (E88-E94, `ciphertext.txt`) and two are Cipher No. 2 (N2-BZ, N2-CA, `ciphertext-no2.txt`; re-filed after the first No. 1 decode gave
nonsense and the header/blind words showed the No. 2 punctuation set tulip/yacht/yawl/Mastiff, NOTES section 2). IDs taken after fetching (the other reader had N2-BR..BY by then; the first N2 pair here was renumbered on the rebase).
`decode.py --write`/`--check` and `decode_no2.py --write`/`--check` exit 0. Tools: `ls4_r1a.py` (shares + matched control, output `ls4_r1a_controls.txt`, entries in `ls4_r1a_entries.txt`).
Images: ten ledger pages fetched once at 2400 px (`hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg`) to scratch; crops by
`python3 tools/iiif_lines.py --image <scratch>/img/p<pointer>.jpg --out <scratch>/crops/<pointer> --prefix p<pointer> --region <x,y,w,h> --lines-per-crop 3|4 --max-width 2400`
with regions 9097 `0,100,2400,680`; 9123 `0,1930,2400,350`; 8965 `0,1640,2400,500`; 8967 `0,1510,2400,430`; 8996 `0,1080,2400,460` + tail `0,1470,2400,330`; 9003 `0,1540,2400,500` + tail `0,1990,2400,330`;
9030 `0,230,2400,520` + tail `0,600,2400,330`; 9047 `0,1230,2400,1260` + top `0,780,2400,500`; 9049 `0,1900,2400,560`. Crops that stopped short of an entry's last line were re-cut (tails above); the last
line of 9047/1 ("good & reliable man Welch Geo K Leet") was read from the volunteer text only.

| row | ID | book | shares No.1/No.2/No.9 of N non-function tokens | clause check: chosen / other two / shuffled chosen | H (decoder; hand moves in Grades) | step 0 | print (IA full text, decoded phrase) |
|---|---|---|---|---|---|---|---|
| 9048/156/0 | not read | - | - | - | - | clear: a pasted-in "United States Military Telegraph" slip, "By Telegraph from Cairo, Dated Sept 9 1864, To T T Eckert: ... left Cairo on Steamer Graham August 17 ... Mason", body in English (volunteer text and image); the entry's own text is the clear copy | not searched (nothing decoded) |
| 9097/203/0 | E88, 15 Oct 1864, J. W. Sampson, Baltimore: "Send your dismounted cavalry to cavalry depot, Washington, for remounts. Telegraph the number" (signed Chief of Staff, i.e. Halleck's word) | No. 1 | 7/7/2 of 14 | No.1 7 of 7 code words in one clause; No.2 0 ("Battery to Battery Depot ... Valley the number Surrendered"); No.9 0; No.1 shuffled 0 | 7 | none | FOUND, word for word: "Send your dismounted cavalry to cavalry depot, Washington, for remounts. Telegraph" in OR I/43 pt 2 (IA `warofrebellion432unit`, `warofrebellionco0043unit_i5n6`, `warofrebellion014302rootrich`, `warofrebellion0000unse_b7w7`) "Adjutant-General, Baltimore" |
| 9123/229/3 | E89, 15 Nov 1864, Lincoln (signed Irving = President) to Thomas, Nashville: "How much force and artillery had Gillem [with] him?" | No. 1 | 8/7/2 of 11 | No.1 8 of 8; No.2 0 ("for Halleck [1000] ... Infantry Bragg"); No.9 0; No.1 shuffled 0 ("Cahawba ... Unite ... Vermont") | 8 | none | FOUND, word for word: "How much force and artillery had Gillem?" Lincoln to Thomas, Nashville (Nicolay-Hay Complete Works IA `completeworksofa07linc`, `completeworksofv10linc`, `completeworksofa10lincuoft`, `completeworksofa02link`, `lifeworksofabrah102linc`; also an OR copy) |
| 8965/73/1 | E90, 20 May 1864 1.30 PM, Sheldon, Fort Monroe, to Col. Biggs: "Has Sheridan left the James? Must we forage him by the other line?" (signed Quartermaster General, Meigs's word) | No. 1 | 13/10/2 of 16 | No.1 11 of 12 tokens in the clause ("forage him" is the doubtful pair); No.2 0 ("Has Schenck Necessary the Pennsylvania"); No.9 0; No.1 shuffled 0 | 12 | none | not found: "has Sheridan left the James" (OR I/36 pt 1 has a different sentence "Sheridan left the James River yesterday"), "must we forage him by the other line" (0 hits) |
| 8967/75/1 | E91, 21 May 1864 10 AM, Horner (New York), to H. S. Sanford at Brevoort House, New York: "Please come hither. Your departure for Europe as soon as practicable is deemed [necessary?]" (signed Secretary of State, Seward's word) | No. 1 | 11/9/4 of 26 | No.1 10 of 10 (time word Emily = 10 AM = header "10 AM"; date May 21 = header); No.2 0; No.9 0; No.1 shuffled 0 | 10 | none | not found: "your departure for Europe as soon as practicable", "departure for Europe is deemed" (0 hits); "please come hither" 448 unrelated hits |
| 8996/104/1 | E92, 7 Jul 1864 11 AM, Sampson, to Capt. Thomas: "Let the vessels bringing up Ricketts' troops return at once to City Point & send to that place all steam transports in U.S. service now available in the port of Baltimore. Despatch!" (QMG's word) | No. 1 | 13/14/5 of 28 | No.1 11 of 11 in one clause; No.2 0 ("Cairo ... Baton Rouge ... Surrounding"); No.9 0; No.1 shuffled 0 | 11 | none | not found: "vessels bringing up Ricketts", "return at once to City Point", "all steam transports in the United States service now available in the port of Baltimore" (0 hits) |
| 9003/111/2 | E93, 16 Jul 1864 4 PM, Van Duzer, Nashville, to "Polking officer" [Commanding Officer, Nashville]: "Send immediately to Louisville, Kentucky, 2 regiments of dismounted cavalry or 100 days men well armed & supplied with ammunition" (General-in-Chief = Halleck) | No. 1 | 13/11/2 of 23 | No.1 13 of 13; No.2 0 ("Independence Mississippi ... Battery"); No.9 0; No.1 shuffled 0 | 13 | none | FOUND, word for word: "two regiments of dismounted cavalry, or 100-days' men, well armed and supplied with ammunition" to Louisville, Ky. in OR I/39 pt 2 (IA `warofrebellion392unit`, `warofrebellion0039geor`, `warofrebellionco0039unit_z2j1`, `cu31924077730210`) |
| 9030/138/0 | E94, 1 Aug 1864 10.30 AM, Horner, to Dix, New York: "The money and package concerning which I telegraphed you on Friday are in the Chemical Bank and not the Bank of Commerce" (signed C. A. Dana) | No. 1 | 10/10/3 of 22 | No.1 8 of 9; No.2 0; No.9 0; No.1 shuffled 0 | 9 | none | not found: "Chemical Bank and not the Bank of Commerce", "money and package concerning which I telegraphed you on Friday" (0 hits) |
| 9047/154/1 | N2-BZ, 14 Aug 1864, Beckwith, to Grant at City Point: Lincoln ("The Secretary of War and I concur that you better confer with [General] Lee and stipulate for a mutual discontinuance of house burning ...") and, on the same entry, a second telegram "For Lt Col Bowers ... Sharpe's men ... W. J. Lee ... trip to Gordonsville on horseback ... 200 [dollars] ... Geo K Leet" | No. 2 (first read as No. 1, which gave "Drove in our pickets" / "Encountered enemy in strong force") | 27/34/6 of 92 | No.2 31 of 31 in clauses (two telegrams); No.1 0; No.9 0; No.2 shuffled 0 | 28 (decoder 29, one moved) + I 2 | none | message 1 FOUND, word for word: "stipulate for a mutual discontinuance of house-burning and other destruction of private property" (Lincoln to Grant, 14 Aug 1864; IA `lifeworksofabrah102linc`, `lifeandworksabr12whitgoog`, `unquotableabraha0000loch`, `newperspectiveso0000unse_e2h1`, `witwisdomofabrah0000linc_a7p4`); message 2 not found: "man named W. J. Lee formerly employed by Colonel Sharpe", "Sharpe offers to make a trip", "Sharpe's men are not disposed to go out before Wednesday or Thursday" (0 hits) |
| 9049/157/2 | N2-CA, 16 Aug 1864 8.30 PM, operator Chapel, to Canby, New Orleans: "General Grant directs, if Kirby Smith succeeds in crossing the Mississippi, that you concentrate all the troops you can spare on Mobile. Does Myers still trouble you?" (General-in-Chief = Halleck) | No. 2 (first read as No. 1: "Prentiss ... Culpepper ... Burnside ... Richmond") | 14/14/2 of 22 | No.2 14 of 14; No.1 0; No.9 0; No.2 shuffled 0 | 14 | none | FOUND, word for word: "General Grant directs, if Kirby Smith succeeds in crossing the Mississippi River, that you concentrate all the troops you can spare on Mobile. H. W. Halleck" in OR I/41 (IA `warofrebellionco0041unit_d1y7`, `warofrebellion412unit`, `warofrebellion014102rootrich`, `in.ernet.dli.2015.204595`); the closing "Does Myers still trouble you" is not in those snippets |

Clause counts are hand counts by one reader (the decoder output of `ls4_r1a.py --show` for every book is in `ls4_r1a_controls.txt`); the vocabulary shares do not pick the book (they sit within 0.1-0.2 of each other
for E88-E94, as in LS3-R9) -- the clause under each book does, and the time/date words: of the nine, six carry a numeral word that equals the ledger header's own day (E89 Ghost = 15, E90 Harrow = 20, E91 Harsh Plug = 21, E93 Gas = 16, E94 Aug Plug = 1,
N2-CA Knapp = 16) and three carry a time word equal to the header time (E90 Hannah = 1.30 PM, E91 Emily = 10 AM, N2-CA Nelly = 8.30 PM): checks independent of the sentence, passed in every case where the header gives one.

Grades: decoder H counts as in the table (E88 7, E89 8, E90 12, E91 10, E92 11, E93 13, E94 9, N2-BZ 29 + I 2, N2-CA 14). By hand: E91 "Europe" is the sender's plain word (the book has a row Europe = Mobile; "departure for Mobile" does not read, "for Europe" does and
Sanford was a minister in Europe): a `plain: Europe` line was added, H 11 -> 10; E94 "Growler" is the blind word Growl plus "-er" (not a book suffix): H -> M, so E94 H 8, M 1; E93 "Polking" is not a book row (the same stem
reads "Commanding" in E77's "polkaing", and the No. 2 book has Polk = Commander), left unread, M 1, and "spits" (image; volunteer "spit") gives "[Men]'s" under the book's s-rule, kept H with the flag; N2-BZ "Black" reads Cairo in
the No. 2 book but Bowers was at City Point (Black = City Point in No. 1): H -> M, so N2-BZ H 28, I 2, M 1. Totals over the nine: H 111, I 2, M 3, C 0. Unread, not graded: E91 "Tartan" (probably "necessary"), N2-BZ "Mosis" (month), E90 "Pleasant" and the fillers.

Image vs volunteer text (image taken): 8996 "Despatch" (volunteer Dispatch); 8996 "service" (image "Revise"-like letters, volunteer service, plain either way, volunteer kept); 9003 "spits" (volunteer spit); 9030 "Image of old nick" (volunteer "Image old nick");
9047 "Mosis" (volunteer Moses); 9049 "plaming"/"pluming" (image ambiguous, volunteer pluming kept: Plum = Cross in the book and the print reads "crossing"). No other word differs in the nine entries.

Print: be-api full text, one to three decoded phrases per entry, one request at a time at least 2 s apart; a miss is a search result for the log, not a statement about print (rule 10). The five not-found rows (E90, E91, E92, E94 and N2-BZ's second telegram)
have no hit in IA full text for the phrases above; no OR volume was grepped locally by this reader (PF4's covers 0-6 for them).

## Remaining gaps (LS4-R1a, 8 Oct 2026)
Read so far: of the ten rows, 9 read (E88-E94, N2-BZ, N2-CA), 1 recorded clear at step 0 (9048/0); located in print by phrase: E88, E89, E93, N2-CA and N2-BZ's first telegram; not located: E90, E91, E92, E94 and N2-BZ's second telegram.
- Print location of E90, E91, E92, E94 and N2-BZ's second telegram - blocker: not-attempted; the sender and recipient editions and a local OR grep were not run, only IA phrase search; next: a verifier phrase search with the local OR grep, ~$0.6 per entry
- E91 "Tartan" and N2-BZ "Mosis" - blocker: no-key-material; neither word is a row of the book it was read with; next: compare with other entries carrying the same words, ~$0.2

## Escalation (LS4-R1a, 8 Oct 2026)
- [n/a] siblings: the ten were selected by PF4's same-leaf check; the neighbours 9097/1 and 9123/0 were not read here.
- [n/a] clear-pages: nothing in this pass.
- [x] known-keys: each entry decoded with all three books and a shuffled copy of the chosen book.
- [x] print: be-api phrase pass over the decoded text.
- [n/a] key-rebuild: no key row added.
- [x] image-check: every row read from crops; the one last line not cropped is named above.
- [n/a] retry: no read failed.
Verdict: keep going: 1 internal gaps; cheapest next: a verifier phrase search with local OR grep for E90, E91, E92, E94, N2-BZ part 2, ~$0.6 per entry

Verifier note (LS4-V1a, 8 Oct 2026, AUDIT.md "## AUDIT (LS4-V1a)"): E91 and E94 are N1 -- their bodies read in order in the Huntington's own public transcriptions of 8967 and 9030 (step 0 should have stopped them); N2-BZ part 1 is OR I/42 pt 2 p.167 and N2-CA is OR I/41 pt 2 p.725 (closing question unprinted), both N1 by script; E90 reads "shade him" on the image (Shade = Forage, not doubtful) and Biggs's clear reply is at mssEC 11 p.201 (pointer 4642); E90, E92 and N2-BZ part 2 are N3 (weak), depth D3, D2, D2.

## LS4-R1b (8 Oct 2026, account 1, for LANE ST-LEDGER-4)

Ten clean rows of PF4's group 3 (Cipher No. 1 guess), second ten: 9097/1 9116/2 9119/1 9125/3 9128/2 9134/1 9138/2 9140/2 8921/1 8922/0. Read from line crops of the page images (one eye, no subagent), the Huntington volunteer text as second witness.
Result: seven filed (E95-E101, `ciphertext.txt`, all Cipher No. 1; `decode.py --write`/`--check` exit 0); one row already read (9138/2 = E20); one stopped at step 0 (9140/2); one read but not filed (9134/1, controls tie).
Tools: `ls4_r1b.py` (shares + matched control, output `ls4_r1b_controls.txt`, entries in `ls4_r1b_entries.txt`), `ls4_r1b_printcheck.py` (cached OR grep), `ls4_r1b_fts.py` (be-api phrase search).
Images: ten ledger pages fetched once at 2400 px (`hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg`) to scratch; crops by
`python3 tools/iiif_lines.py --image <scratch>/img/p<pointer>.jpg --out <scratch>/crops/<pointer> --prefix p<pointer> --region <x,y,w,h> --lines-per-crop 3-6 --max-width 2400`
with regions 9097 `0,760,2400,450`; 9116 `0,870,2400,740`; 9119 `0,950,2400,520`; 9125 `0,1170,2400,470`; 9128 `0,1620,2400,400`; 9134 `0,1350,2400,570`; 9138 `0,2210,2400,380`; 9140 `0,2150,2400,570` (`--prominence 20 --ink 200`, pencil faint);
8921 and 8922 (line finder failed on the pencil-marked lines) by a plain PIL crop of the entry block (`(150,200,2250,1340)`, `(150,240,2200,760)`) read at about 1800-2000 px.

| row | ID | book | shares No.1/No.2/No.9 of N non-function tokens | clause check: chosen / other two / shuffled chosen | H (decoder; hand moves in Grades) | step 0 / prior work | print |
|---|---|---|---|---|---|---|---|
| 9097/205/1 | E95, 15 Oct 1864, operator J. W. Sampson: "[...] for Hon. H. W. Hoffman. Come over to night and see me. A Lincoln" (time word Lucy = 5 PM, date word Gallant = 15 = header) | No. 1 | 4/4/1 of 10 | No.1 3 of 3 code words in the clause; No.2 0 ("[Across] ... [12]"); No.9 0; No.1 shuffled 0 | 3 | none; body is plain English around three code words (low information) | not located: "Hon. H. W. Hoffman", "come over to-night and see me" in IA full text (the Lincoln letter to Hoffman did not come up; hits are other books) |
| 9116/224/2 | E96, 5 Nov 1864 11 PM, operator Sampson at Baltimore: "Colonel William Hamilton is reported on what seems trustworthy evidence as a Rebel agent in Baltimore. If there are several persons answering to the name, care must be exercised that the right one [..]" signed C. A. Dana (time Sarah = 11 PM, date plaster = 5, both = header) | No. 1 | 15/13/6 of 31 | No.1 14 of 14 in one clause; No.2 0 ("[Failure] for [Supply] ... [Siege Gun] ... [Saturday] [Cheatham]"); No.9 0; No.1 shuffled 0 ("Cleveland ... Gen C. C. Washburne ... Pemberton") | 14, hand 12 + M 2 | none | not located: "is reported on what seems trustworthy evidence", "rebel agent in Baltimore", "answering to that name" (the last is common and noisy) |
| 9119/227/1 | E97, 7 Nov 1864, operator Clowry, St. Louis, to Maj. Gen. Rosecrans: "Unfortunately the evidence in our possession furnishes no personal description of the Rebel agent at St. Louis" signed C. A. Dana, Asst. Secretary of War (date Postpone = 7 = header) | No. 1 | 12/12/5 of 24 | No.1 12 of 12; No.2 0 ("Maj Gen B. F. Butler ... Nashville ... Cheatham"); No.9 0; No.1 shuffled 0 | 12 | none; the margin note "See page 224 Book 1 + page 226 Book 2" sits on this leaf (a cross-reference, not a rendering) | not located: "evidence in our possession furnishes no" (be-api 502 on retry), "furnishes no personal description" (0, then 502), cached OR grep none |
| 9125/233/3 | E98, 19 Nov 1864, operator R. O. Brien (HQ Army of the James), to Maj. Gen. Butler: "Can not you hold on for 3 or 4 days until our vessel reaches you, now on the way" signed G. V. Fox, Asst. Secretary of the Navy (date Hope = 19 = header; Nancy = 8 PM) | No. 1 | 11/9/4 of 23 | No.1 11 of 11 in one clause; No.2 0; No.9 0; No.1 shuffled 0 (the sentence stays plain, the code words give "Alexandria ... Maj. Gen. David Hunter") | 11, hand 10 + M 1 | none | not located: "hold on for three or four days" (unrelated hits), "our vessel reaches you" (0) |
| 9128/236/2 | E99, 26 Nov 1864, operator Clowry, to Rosecrans: "All troops sent from Missouri must report to Maj. Gen. Thomas, any other orders to the contrary notwithstanding" signed General-in-Chief (Halleck's word) (date Harrow = 26 = header) | No. 1 | 11/8/4 of 18 | No.1 10 of 10; No.2 0 ("[Unite] sent from [Kanawha] must [South] to [Augur]"); No.9 0; No.1 shuffled 0 | 10 | none | FOUND, word for word: "Major-General Rosecrans: All troops sent from Missouri must report to General Thomas, any other orders to the contrary notwithstanding" in OR I/41 pt 4 (IA `warofrebellion014104rootrich`, `warofrebellionco41p4unit_h9b3`, `in.ernet.dli.2015.204597`, `11548845bsb`) |
| 9134/242/1 | not filed (X6): operator McCaine, 3 Dec 1864, signed C. A. Dana: "I have a draft for you with pkg of [violet = Rebel (No. 2) or quote mark (No. 1)] money, also a little personal bundle for yourself. Can you send an officer down fort" | undecided | 7/7/2 of 18 | No.1 H4, No.2 H4, shuffled No.1 H3, shuffled No.2 H4: the controls tie, and both books give nonsense for the two address words (Dahlgren / Sheridan) | not claimed | none | not searched; "little personal bundle for yourself" and "draft for you with package" were run against the cached OR set only (none) |
| 9138/244/2 | already read: E20 (LS-R1; same page, operator Mason, Cairo): re-read here from the crop, identical reading ("[3 PM] [10] for [Colonel] Winslow [Cairo]. All [Troops] from [Missouri] must grotto [Maj Gen Geo. H. Thomas] till further orders [General-in-Chief]", H 9) | No. 1 | 10/7/3 of 15 | No.1 9 of 9; No.2 0; No.9 0; shuffled 0 | not filed again | PF4 listed it clean although E20 stands in ciphertext.txt (prior-work step 1, the check PF4 did not run) | E20's own print result is in its section; E99 is the same order sent two weeks earlier and is in OR I/41 pt 4 |
| 9140/248/2 | not read | - | - | - | - | step 0: body is English ("Please stop any [telegram] from Speed ... to Box and report to me for orders", signed TT Eckert); only the signature and two words are code | not searched |
| 8921/29/1 | E100, 5 Apr 1864 3.30 PM, operator Baldwin, Baltimore, to Capt. Thomas Vinton, Quartermaster: "Send the Nelly Pantz if in Baltimore to Annapolis fully coaled and watered to transport [colored(?)] [troops(?)] to Hilton Head and thence to such point as Gen. Gillmore may order on her reporting to him. She should leave as soon as the storm is over and the sea moderates so as to make the voyage safe" signed Quartermaster General (Meigs's word), tail time word Jennie = 3.30 PM = header 330 PM | No. 1 | 18/18/7 of 42 | No.1 16 of 17 in one clause (one false time word, below); No.2 0 ("[Battled] Thomas [Rations] [Baton Rouge]"); No.9 0; No.1 shuffled 0 | 16, hand 14 + M 2 | none; the leaf carries pencil superscripts over words ("bad", "late", "over", "man", "at", "50", numerals 2/4/7) in a later hand: single words and numbers, not a rendering of the body, not used; its sibling on the same leaf is E62 | not located: "Nelly Pentz" occurs in 1863 press and Navy lists (a transport steamer, so "Nelly" is plain here), "fully coaled and watered" and "leave as soon as the storm is over" have only unrelated hits, "Gillmore may order on her reporting" 0 |
| 8922/30/0 | E101, 6 Apr 1864, operator F. S. Van Valkenburg, Nashville, to Gov. (Andrew) Johnson: "Do not believe the newspapers. There is no design to put General Buell again in command in Tennessee" | No. 1 | 8/8/1 of 18 | No.1 6 of 6; No.2 0 ("[Harbor] Buell ... in [City] in [Missouri]"); No.9 0; No.1 shuffled 0 | 6, hand 5 + M 1 | none; pencil marks over the words ("for", "next", "out", "Henry", "Venus", numerals, a circled "Morton Plain Pig") in a later hand, single words/numbers, not used | not located: "Buell again in command in Tennessee" 0, "no design to put General Buell" 0; "Do not believe the newspapers" only unrelated hits |

Clause counts are hand counts by one reader (decoder output for every book, with the shuffled copy, in `ls4_r1b_controls.txt`); the shares do not pick the book (0.4-0.7 for No.1, 0.4-0.5 for No.2, within 0.1-0.2 of each other for
most rows, as in LS3-R9 and LS4-R1a) -- the clause under each book does, with the header checks: E95 Gallant = 15, E96 Sarah = 11 PM and plaster = 5, E97 Postpone = 7, E98 Hope = 19, E99 Harrow = 26, E100 tail Jennie = 3.30 PM all equal the ledger header; E101's date word does not (below).

Grades: decoder H as in the table (E95 3, E96 14, E97 12, E98 11, E99 10, E100 16, E101 6; total 72). By hand: E96 "William" is the numeral row 100 and "persons" the numeral row 5 (-ed/-s read as stem+ending), both plain here (a named colonel, plain "persons"): H -> M, so E96 H 12, M 2;
E98 "Fox" reads Philadelphia in the book but is G. V. Fox's plain name (signature), H -> M, so H 10, M 1, and "Orr." (volunteer "Nov.") unread; E100 "Nelly" is the time word 8.30 PM in the book but the plain name of the steamer Nelly Pentz (the real time word is the tail's Jennie, 3.30 PM = header): M; "colored" read "Jasper" (book) in "[Jasper]ed whiskey" gives nonsense: M; so E100 H 14, M 2; E101 "Plunge" = 1 in the book but the header says 6 Apr (Plague/Pledge = 6; image reads Plunge): M, so H 5, M 1, the one row here whose date word fails the header check. Totals over the seven filed: H 62, M 6, C 0, I 0.
Unread, not graded: E97 "rainy" and fillers, E100 "Pantz"/"whiskey", E98 "Hm I lie".

Image vs volunteer text (image taken): 9125 "Orr." (volunteer "Nov."), "Hm I lie" (volunteer "Here I lie"); 8922 last line "Buell again in Pontiac in Adonis Bautus" once (volunteer repeats "Brutus in Adonis"). No other word differs in the rows read.

Print: be-api full text (positive control first: E88's phrase "send your dismounted cavalry to cavalry depot" returns its four OR I/43 volumes), 2-4 decoded phrases per entry plus the cached OR/ORN set (155 volumes, `ls4_r1b_printcheck.py`). The host answered 502 on many calls while four workers shared it; the failed phrases were retried once and some stayed failed (listed
in the table); a miss is a search result for the log, not a statement about print (rule 10). The Grant Papers / Basler volumes were not searched (no IA identifier tried; the "Hon. H. W. Hoffman" hit list shows only a 1860 Lincoln speech book).

## Remaining gaps (LS4-R1b, 8 Oct 2026)
Read so far: of the ten rows, 7 filed (E95-E101), 1 re-read of E20, 1 not filed (9134/1), 1 step-0 skip (9140/2); located in print by phrase: E99; not located: E95, E96, E97, E98, E100, E101.
- Print location of E95-E98, E100, E101 - blocker: not-attempted; Basler/Grant Papers/Nicolay-Hay volumes and the Official Records ser. III/ORN were not phrase-searched individually and be-api answered 502 on several calls; next: a verifier phrase search with a local OR grep, ~$0.6 per entry
- 9134/1 (Dana to McCaine) - blocker: no-key-material; book undecided, controls tie; next: read it beside the other McCaine entries (E67 same page) for what Negus/Francis/Bender mean, ~$0.3
- E96 "Colonel" (Pandora), the "William"/"persons" hand moves and E100 "colored whiskey" - blocker: no-key-material; neither reads from its book row in context; next: compare with other entries carrying the same words, ~$0.2

## Escalation (LS4-R1b, 8 Oct 2026)
- [x] siblings: E20 found as the already-read twin of 9138/2; E99 is the same order as E20 sent two weeks earlier (OR I/41 pt 4).
- [n/a] clear-pages: nothing in this pass.
- [x] known-keys: each entry decoded with all three books and a shuffled copy of the chosen book.
- [x] print: be-api phrase pass over the decoded text plus cached OR grep; partly blocked by 502s (above).
- [n/a] key-rebuild: no key row added.
- [x] image-check: every row read from crops; the pencil-marked leaves 8921 and 8922 from plain block crops, not line crops.
- [x] retry: failed be-api phrases retried once.
Verdict: keep going: 1 internal gaps; cheapest next: a verifier phrase search with local OR grep for E95-E98, E100, E101, ~$0.6 per entry

Verifier note (FV-LS4-R1b, account 2, 8 Oct 2026; AUDIT.md "## AUDIT (FV-LS4-R1b)"): E95 is N1 (body in clear in the Huntington transcription of 9097; printed in Tarbell, Life of Abraham Lincoln vol. 4, "Hoffman, Baltimore, Md.: Come over to-night and see me. A. Lincoln"); E98 is N1 (body in clear in the transcription of 9125 except the numerals 3/4); E101 is N1 (quoted in The Papers of Andrew Johnson vol. 6, "no design to put General Buel again in command in Tennessee" -- the print's spelling "Buel" defeated the phrase pass); E99 N1 confirmed at OR I/41 pt 4 p.693 (12.30 p.m.). E96, E97, E100: N3 (weak), D2, one audit. The table's "print" cells above are the reader's search results, kept as written.

## LS4-R2b (8 Oct 2026, account 1, for LANE ST-LEDGER-4)

The remaining fifteen group-2 rows of PF4 (pointer/entry: 9132/0 8982/1 8986/1 9040/0 9052/1 9060/2 9066/1 9121/1 9122/2 9125/2 9142/0 8948/2 8967/0 8971/2 9003/0), read from the page images by one eye (no subagent), the Huntington volunteer text (sources/mssEC19/p<pointer>.json) as second witness. Result: 13 entries filed -- twelve Cipher No. 2 (N2-CB..N2-CM, `ciphertext-no2.txt`) and one Cipher No. 1 (E102, `ciphertext.txt`); three rows not filed (9060/2 and 9066/1 step-0 skips, 8967/0 already N2-BG). `decode_no2.py --write`/`--check`, `decode.py --write`/`--check` and `decode_no9.py --check` all exit 0. IDs were taken after fetching (LS4-R1b had E95-E101 and no N2 beyond N2-CA). No spec exists for eckert-1864 (specs/ holds eckert-1862 only), so `judge_plaintext.py` was not run. Working files: `ls4_r2b_entries.txt` (blocks as transcribed from the images), `ls4_r2b_file.py` (files them under the IDs), controls by `ls4_r2a_controls.py --file ls4_r2b_entries.txt --show` (same machinery and seeds 7, 11, 13 as LS4-R2a).

Images: 15 ledger pages plus 3 neighbouring pages fetched once at 2400 px (`hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg`, 3.2 s apart, descriptive User-Agent, all HTTP 200) to scratch: 8987, 9039 and 9002, because 8986/1, 9040/0 and 9003/0 are an entry's tail on the next page (or the head of one begun on the page before). Every page is legible at the 1720-1735 px display size, so I read whole pages rather than cutting line crops, except the last line of 9003 (top of the page), which I cut with `python3 tools/iiif_lines.py --image <scratch>/img/p9003.jpg --out <scratch>/crops/9003 --prefix p9003 --region 150,200,2200,330 --lines-per-crop 3 --max-width 2400` and the ledger header of 8948/2 (`PIL crop 1200,1600,2400,1760`). That departs from the "line crops" method of LS4-R2a; the reading of every word was from the image, the volunteer text only second witness. Image vs volunteer text (image taken): 9040 "Bickford" (volunteer "Beckford"); 9003/9002 "Brook" (volunteer "Brooks"), "quickenment" (image Mickenment/Quickenment, kept the volunteer's); **8948/2 header "Wash Apl 26th 1864" (volunteer "20"; the cipher's own date word decodes 26)**; 9142/0 holds two telegrams (the volunteer segmenter ran them together). No other word differs in the thirteen entries.

**Step 0 (own transcription, before decoding).** 9060/2 (Beckwith, City Point, 31 Aug 1864 9.30 PM, signed Geo K Leet AAG): the body reads in order as English with only name and place words as code ("for Bowers a man named C. S. Bell who says he was formerly a scout for [Hurl but] & that [crowd about Andrew] mos. ago sent him through Canada to [Haddock] Bedford is here & wishes to go to Brimstone Shall I send him") -> **N1-likely: clear in the Huntington's public transcription (pointer 9060)**, not decoded. 9066/1 (H. E. Thayer, 7 Sept 1864): wholly plain, no code word ("Fraud and forgery being perpetrated since the twelfth of August ... under the name of Wm H Codove ... William P Copeland ... period period stop stop") -> N1-likely: clear in the Huntington transcription (pointer 9066), not decoded. 8967/0 is the tail (p.75) of the 20 May 1864 10 PM Caldwell entry already filed as N2-BG (pp.74-75, pointers 8966-8967): not filed again. None of the other twelve rows has a `u` hit in PF4's hunt list; each reads as code in its own transcription.

**Book and matched control (rule 3).** Per entry: shares = non-function tokens found in key.md / key-no2.md / key-no9.md; clause = whether the chosen book gives a grammatical sentence (by hand, one reader) against the other two books and three meaning-shuffled copies of the chosen book (seeds 7, 11, 13); time word = the cipher's own time word decoded under each book against the ledger header. Decoder H counts tie with the shuffles by construction (a shuffle keeps which words are in the key), so they are not the test; the clause reading, the header time/date word and the print are. Full output of every decode: `ls4_r2b_controls.txt`.
| row | ID | date, to / from (decoded, worker's gloss) | shares No.1/No.2/No.9 of N | clause: chosen / other two / 3 shuffles | time/date word vs header | decoder H / C / I | print |
|---|---|---|---|---|---|---|---|
| 9132/0 p.240 | N2-CB | 1 Dec 1864 3 PM; to "Billy": "Foster has no other cavalry than the battalion of 4 Massachusetts, now reduced to 100 men. He asks for 8 companies with 10 Corps ... If I order as you direct it will leave not a single mounted man in the Department of the South. Is this your intention?" | 16/23/6 of 42 | yes / no, no / 0 of 3 | 3 PM = header "3. PM" (No.1 3.30 PM, No.9 6 PM) | 22 / 1 / 0 | not located (be-api 5 phrases; 18 OR/ORN volumes grepped locally) |
| 8982/1 p.90 | N2-CC | 11 June 1864 1 PM, to Canby: "I can not find the gauge of the Vicksburg & Shreveport Railroad. What is it?" (signature word keyed to Quartermaster General with a doubtful flag) | 13/13/6 of 19 | yes / no, no / 0 of 3 | June 11 = header; time 1 PM (No.1 1.30 PM, No.9 2 PM), no header time | 13 / 0 / 0 | the entry itself not located; its printed sibling is OR I/34 pt 4 p.424-425 (`warofrebellion344unit`): Quartermaster-General's Office, Washington, 17 June 1864 1.30 PM, to Canby at Vicksburg, "I have telegraphed you twice to inform me of the gauge" (that is the ledger entry 8986/0 beside it, not this row), which spells "Shreveport" |
| 8986/1 p.94-95 | N2-CD | 17 June 1864 2.30 PM, to Grant: "A German engineer officer who left Lee's army June 7 says that Pickett's division about 6000 infantry and Breckinridge's division about 7000 infantry passed through Gordonsville in cars on the 6th and 7th against Hunter ... estimates entire force left under Lee and Beauregard from 60 to 75000 exclusive of home guards and militia in Richmond ... Many of this man's statements are verified by others" (signed Halleck) | 42/64/6 of 87 | yes (long) / no, no / 0 of 3 | June 17 = header; time 2.30 PM (printed 3 p.m.), no header time | 52 / 3 / 3 | **FOUND**, word for word: OR I/40 pt 2 (`warofrebellion402unit`), Washington, June 17, 1864 -- 3 p.m., Halleck to Grant, Bermuda Hundred (be-api, 4 identifiers); page not read |
| 9040/0 p.146-147 | N2-CE | 9 Aug 1864 (header 9.30 am; cipher gives the date only): signature keyed Quartermaster General, to Brig. Gen. "In galls" (read Ingalls): wagons of the 6th Corps and of the Cavalry sent to this place should follow the troops; "their drivers are needed to relieve ours ... A large number of steamers has been engaged and ordered to City Point to be ready for any movement in force ... If on their arrival they are not needed there it will be well for them to return to [Monroe] and wait events" | 39/46/6 of 85 | yes / no, no / 0 of 3 | date Aug 9 = header; no cipher time word | 39 / 0 / 2 | not located (be-api 5 phrases + local OR grep; PF4 had called the head on p.146 print-likely on a 3-gram cover of 7 in ORN I/12, which I could not fetch: archive.org 500 twice) |
| 9052/1 p.160 | N2-CF | 21 Aug 1864 1 PM (ledger "No 2 / 1 pm"), from Lexington Ky for the General in Chief: "I am satisfied from the reports of my scouts that Kentucky is [being] invaded by a large force under [Morgan?] & Wheeler. If there are any troops which Canby sent please order them at once" | 11/19/2 of 32 | yes / no, no / 0 of 3 | Aug 21 = header; time 1 PM = ledger "1 pm" (No.1/No.9 differ by construction) | 16 / 1 / 1 | not located (be-api 4 phrases; Grant Papers vol 12 restricted search "Kentucky" answers only that the volume mentions it) |
| 9121/1 p.229 | N2-CG | 11 Nov 1864 3 PM, to Grant: "[Troops] sent North have been ordered back ... When will [..] be up to make annual report" (signed Halleck) | 9/11/3 of 19 | partial (frame only) / no, no / 0 of 3 | Nov 11 = header; 3 PM (No.1 3.30, No.9 6) | 10 / 1 / 0 | not located (a short generic phrase, be-api and 18 volumes: only generic hits) |
| 9122/2 p.230 | N2-CH | 12 Nov 1864 9 AM, G. V. Fox to Grant: "We shall be at Hampton Roads at 7 AM tomorrow morning unless it is stormy weather which will cause some delay" | 8/12/2 of 21 | yes / no, no / 0 of 3 | 9 AM = header "9am"; Nov 12 = header; 7 AM "tomorrow" in the body | 9 / 0 / 1 | **FOUND**: Papers of Ulysses S. Grant vol. 12 (`papersofulyssess0012gran`), "9:00 a.m., Fox telegraphed to USG. 'We shall be at Hampton Roads at 7 A.M. tomorrow morning unless it ...'" (be-api highlight; page not read) |
| 9125/2 p.233 | N2-CI | 19 Nov 1864, Beckwith at Burlington N. J., to Grant: "There is no reason why you should not go to Grain ada [Granada?]. Let me know your address there" (signed Secretary of War) | 5/8/0 of 18 | yes (plain words around 8 code tokens) / no, no / 0 of 3 | no cipher time word decoded (an "x:15 PM" form; M) | 5 / 0 / 2 | not located (2 phrases, generic hits only) |
| 9142/0a p.250 | N2-CJ | 18 Dec 1864, J. H. Emerick at City Point, signed "Rue Two In galls" (read Ingalls): "The orders given at first in relation to the transports for [Sherman] will be carried out. Have such of the boats named as are in the James sent off as directed without delay to their destination" | 7/9/3 of 29 | yes / no, no / 0 of 3 | date Dec 18 = header | 7 / 0 / 1 | not located (3 phrases) |
| 9142/0b p.250 | N2-CK | 18 Dec 1864 11.15 PM, Emerick at City Point, signed T. T. Eckert: "you can inform General Rawlins [that General] Grant left here at 3 PM to-day for City Point by boat" | 10/10/3 of 16 | yes / no, no / 0 of 3 | "11.30 PM" decoded vs header "11 15 pm" (No.1 11 PM, No.9 9.30 PM): closest under No. 2 | 10 / 0 / 0 | not located (3 phrases; Grant Papers vol 13 identifier does not answer: "Rawlins" 0 hits) |
| 8948/2 p.56 | N2-CL | 26 Apr 1864 11.30 AM, Caldwell, to Meade: "I cannot send the party as I wish without some cooperation from [Warrenton]. I wish some also from Point of Rocks. If you cannot give the [force] now I will postpone [Augur]" | 8/10/1 of 29 | yes / no, no / 0 of 3 | cipher date word 26 = image header "Apl 26" (volunteer "20"); 11.30 AM (No.1 11.30 AM, No.9 10 AM) | 9 / 0 / 0 | not located (2 phrases) |
| 9003/0 p.110-111 | N2-CM | 15 July 1864 4 PM, to Grant: "Steamer McClellan from New Orleans with 860 men, Nineteenth Corps, arrived here ... A railroad agent who left Sandy Hook this morning reports Hunter's forces began to reach Harpers Ferry Wednesday evening ... A signal officer at Point of Rocks says enemy crossed large wagon train at Noland's Ferry ... crossed 400 wagons at White's Ford ... Halleck estimates the force they have had before Washington at 28000 to 30000 as follows ..." (signed Dana) | 71/108/14 of 178 | yes (long) / no, no / 0 of 3 | July 15 = header; 4 PM = printed "4 p. m." | 93 / 4 / 3 | **FOUND**, word for word: OR I/37 pt 2 p.333 (`warofrebellion372unit`, War Department, Washington City, July 15, 1864 -- 4 p. m., Lt Gen Grant, signed C. A. Dana); the same sentences are also quoted in two secondary works on archive.org (be-api, `fightingfortimeb0000glen`, `californiasabers0000mcle`) |
| 8971/2 p.79 | E102 (Cipher No. 1) | 26 May 1864 11 AM, Sam Bruch: "For Brig. Gen. Burbridge, commanding District of Kentucky: General Washburn telegraphs from Memphis that Forrest is collecting a large cavalry force at Corinth & Tupelo, probably preparatory to a raid into Middle Tennessee and Kentucky" (signed General-in-Chief) | 19/17/3 of 33 | No.1 yes / No.2 no ("District of Mississippi ... Forrest ... a large Battery Force at Chattanooga"), No.9 no / No.1 shuffled not run, No.2 shuffles n/a | May 26 = header; 11 AM (header none) | 18 / 0 / 0 | the entry itself not located; **a parallel is in print**: OR I/39 pt 2 p.54 (`warofrebellion392unit`), Halleck to Brayman at Cairo, 20 May 1864: "General Washburn telegraphs that Forrest is collecting a large cavalry force at Corinth and Tupelo. Possibly he may attack Columbus and Paducah again. Prepare for him" -- other addressee, date and ending |

Book choice: the shares do not pick the book (within 0.1-0.2 of each other for most rows, as in LS4-R2a/R1b); the clause under each book and the header date/time words do. 8971/2 was first tried as No. 2 because it sat in PF4's group 2: the No. 2 decode ("District of Mississippi", "Larkinsville", "Ammunition") is no sentence, the No. 1 decode is, and the date word "Harrow = May 26" is the header's. It is filed in `ciphertext.txt`.

Totals over the 13 filed entries (decoder): H 303, C 10, I 13. By hand: M 30 (tokens graded M because the key row and the context disagree, a plain word was written in syllables, or a name code is not in the key): N2-CB "battle" (key Halleck; "battle lion" = battalion, H -> M), "red used", "come ponies", "Billy"; N2-CC "Sleeve port" (Shreveport in the printed sibling); N2-CD "Harry" (key row Washington, C from one entry; here "from Harry to Charlottesville and Staunton" and the print says "from Richmond", H -> M) and "Pickets" (key row Picket = Demoralize; the print says "Pickett's division", H -> M); N2-CE "block ade" and the tail "whack/Spunky Spark"; N2-CF "Morgan" (key numeral 19, here a force commander) and "Tobey"; N2-CG "willow", "tother"; N2-CH "Odor swedens no there" (3); N2-CI "Grain ada", "Brook"; N2-CJ "Rue Two", "Bradley"; N2-CK "Raw lines"; N2-CL "Vols prompt port" (circled pencil note); N2-CM "Brook" and "Watkins"; E102 "home of the oppressed" (4) and "Wash burn". Net of the three decoder H that moved to M, H 300. The conflicts for "Harry" and "Pickets" are in HYPOTHESES.md (rule 4). 8948/2 carries marginal pencil glosses in a second hand ("doing", "did", "get", "man", "change", "may", "partake", "go", and a circled "Vols prompt port"); they were not used (placement over a word is ambiguous, one witness).

Print: be-api full text (positive control first: "last of the siege train has just started" returned seven items), 2-4 decoded phrases per entry plus the cached OR/ORN set and eight further volumes fetched to scratch (OR I/34 pt 4, 39 pt 2, 40 pt 2, 42 pts 2-3, 44, ORN I/11) -- 18 volumes grepped locally with a hyphen-joining normaliser (`orgrep.py`, scratch). Note on a cached volume: the cached `warofrebellion431unit` is catalogued by the Internet Archive as **v.47 pt 2**, not 43 pt 1 (the LS4-R2a note reads "OR I/43 pts 1-2" for it). Grant Papers: vols 10, 11, 12 answer a restricted be-api search (positive controls "Culpeper", "City Point" each return the volume); vol 13 (`papersofulyssess0013gran`) does not exist in the IA listing and a restricted "Rawlins" query returns nothing, so no Grant Papers search for 16 Nov 1864 onward (N2-CI, CJ, CK, CB) was possible beyond the unrestricted full-text search. Not searched: Basler (Lincoln) volumes, the press of the day, Meigs/Halleck/Rawlins papers, ORN I/12 (500 twice). Found in print: N2-CD (OR I/40 pt 2), N2-CH (Grant Papers vol. 12), N2-CM (OR I/37 pt 2 p.333), the three printed texts agree with the decoded wording (N2-CH only through the quoted opening of the Grant Papers entry); parallels only: N2-CC (printed sibling, OR I/34 pt 4), E102 (OR I/39 pt 2 p.54). Not located in what was searched: N2-CB, CC, CE, CF, CG, CI, CJ, CK, CL, E102 itself. Of the fifteen rows: 3 in print, 2 step-0 skips, 1 already filed (N2-BG), 9 not located, one row (9142/0) holding two entries.

Requests: hdl.huntington.org 18 (all page images, 0 dmGetItemInfo), be-api.us.archive.org about 62 (several 502s, no 429/403; failed phrases retried once), archive.org 10 (one advancedsearch, nine `_djvu.txt` downloads; ORN I/12 answered 500 twice), no other host. Subagents 0.

## Remaining gaps (LS4-R2b, 8 Oct 2026)
Read so far: of the fifteen rows, 12 read (13 entries, N2-CB..N2-CM and E102), 2 skipped at step 0 (9060/2, 9066/1), 1 already filed (8967/0 = N2-BG).
- Print location of N2-CB, N2-CC (the entry itself; its sibling is printed), N2-CE, N2-CF, N2-CG, N2-CI, N2-CJ, N2-CK, N2-CL and E102 - blocker: not-attempted; the Basler/Lincoln volumes, ORN I/12, the press of the day and the sender/recipient papers (Meigs, Halleck, Burbridge, Ingalls) were not searched, and Grant Papers vol 13 is not reachable on IA; next: a verifier phrase search with a local OR/ORN grep including vols 42 pt 3, 44, 45 pt 1 and ORN I/12, ~$0.6 per entry
- N2-CD "Harry", "Pickets", N2-CB "battle", N2-CF "Morgan", N2-CC "Sleeve port" - blocker: no-key-material; each key row conflicts with the context; next: a second printed witness for each pairing (the print of N2-CD gives Richmond and Pickett's), ~$0.2
- 9060/2 and 9066/1 - blocker: not-attempted; read as clear in their own transcription, not decoded; next: a print phrase search of the clear text, ~$0.2 each
- N2-CE and N2-CM begin on the previous page (9039, 9002); the 9002 head of N2-CM has no PF4 row of its own - blocker: not-attempted; the continuation heads were read only as part of these two entries and the other readers' ID lists were not diffed against them; next: confirm no other reader or verifier filed the 9002 head under another ID, ~$0.1

## Escalation (LS4-R2b, 8 Oct 2026)
- [x] siblings: neighbouring pages 8987, 9039, 9002 fetched and read as the heads/tails of three rows; 8986/0 (printed in OR I/34 pt 4) read as the sibling of N2-CC.
- [x] clear-pages: twelve rows read from the full page images at 2400 px (display 1720-1735 px), volunteer text as second witness.
- [x] known-keys: key-no2.md / key.md / key-no9.md and three shuffled copies of the chosen book applied to every entry.
- [ ] print: be-api phrases, 18 OR/ORN volumes and Grant Papers vols 10-12 done; Basler, press and sender papers, ORN I/12 not.
- [n/a] key-rebuild: no key row added (two conflicts logged in HYPOTHESES.md).
- [x] image-check: every token read from the image.
- [x] retry: failed be-api phrases retried once; ORN I/12 retried once (500).
Verdict: keep going: 3 internal gaps; cheapest next: a first verifier on N2-CB, N2-CC, N2-CE, N2-CF, N2-CJ, N2-CK, N2-CL and E102 (the not-located entries with a clause), ~$4.5
## Huntington reply, 8 Oct 2026 (09:08 AM Pacific, Ask a Librarian ticket #19266054; logged by the account-3 orchestrator)
From the Huntington's Head of Digital Collections and Imaging Services, answering our 24 Sept and 6 Oct messages: the Eckert materials
are largely decoded within the Official Records, though the printed text and the original messages differ in places (a comparison
would be for scholars); for telegrams NOT in the Official Records or other sources a decipherment would be useful, if correct; the
Blathwayt items may be of similar value; the Curator of the collections must confirm before use; question to us: are we asking for
recognition in the Digital Library or something further. No answer yet on the later code book (Dec 1864 on) or the dataset question of
the 6 Oct message. Reply drafted: outreach/huntington-einaudi-reply-2026-10.md (recognition only), list
outreach/huntington-decipherments-list-2026-10-08.tsv.

## LS5-R1d (8 Oct 2026, account 1, for LANE LEDGER)

Eleven PF4-clean rows of group 3 (Cipher No. 1 guess), the third tranche: 9036/0 9043/0 9049/1 9053/2 9055/1 9062/2 9086/1 9088/1 9113/1 9124/1 8967/2.
Result: eight filed (E120-E126 in `ciphertext.txt`, N2-EA in `ciphertext-no2.txt`; `decode.py --check` and `decode_no2.py --check` exit 0); three stopped at step 0 (9036/0, 9055/1, 9124/1: the body is in clear in the row's own Huntington transcription).
Prior-work lines (checklist by hand; `tools/prior_work.py` does not exist): (1) own work, `git fetch`, grep of the eleven pointers in NOTES/AUDIT/HYPOTHESES/STATUS/WORK-QUEUE and the last 1,500 ROOM lines: no entry of these rows read before (9053/9055/8967 appear only as the same pages' other entries E26, E33, E91); no live claim. (2) leaf and neighbours: pencil superscripts on 9113 (digits over words) are a later hand, single numbers, not used; no gloss or clear copy on any leaf. (3) own Huntington transcription read for all eleven (`sources/mssEC19/p<pointer>.json`); 8967/2's `u` hits (8226@8472 p.156, 5982@6254 p.24, 8394@8472 p.324, read once under the hdl token) are 1863 pages about other letters, none states the row's substance. (4) step 0 Grant/Lincoln/Stanton/Halleck/Butler/Meigs rows: Google Books API (country=US, key) on a decoded or clear phrase for 9036/0, 9124/1 and each decoded entry, results below.
Images: eight page images fetched once at 2400 px (`hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg`, 8 requests, plus 3 `dmGetItemInfo`, 3.2 s apart, under the hdl token) to scratch. Line crops by
`python3 tools/iiif_lines.py --image <scratch>/img/p<pointer>.jpg --out <scratch>/crops/<pointer> --prefix p<pointer> --region <x,y,w,h> --lines-per-crop 3-6 --max-width 2400 --prominence 15-20 --ink 200`
with regions 9043 `0,200,2400,1250`; 9049 `0,1150,2400,650`; 9113 `150,1330,2250,380` (header and first lines); 9088 `150,930,2250,520` (lines 9-12). The other entries (9053, 9062, 9086, 9088 first lines, 8967, 9113 body) were read from the 800 px page overviews against the volunteer text (a weaker read than crops; no word differed except as listed).

| row | ID | book | shares No.1/No.2/No.9 of N non-function tokens | clause check: chosen / other books / shuffled chosen | H (decoder; hand moves in Grades) | step 0 / header check | print |
|---|---|---|---|---|---|---|---|
| 9036/143/0 | not read | - | - | - | - | step 0: Stanton to Gov. Curtin, 5 Aug 1864 ("A force believed by Pagan [Grant] to be adequate for the occasion is being directed by him against the olive [enemy]"): body in clear in order, only "Grant" and "enemy" coded | Google Books snippet of "The War of the Rebellion" (1893 edition) carries "Governor Curtin, Harrisburg: Your telegrams have been received. A force believed by General Grant to be adequate for the occasion is being directed by him against the enemy. Edwin M. Stanton" (volume and page not read from the snippet) |
| 9043/151/0 | E120, 11 Aug 1864 3 PM, Beckwith, for Lt Col T. S. Bowers (Grant's staff), copy to Sheridan at Harpers Ferry: a scout's report that Longstreet's corps was moving north through Staunton to join Early | No. 1 | 30/29/9 of 64 | No.1 reads in order throughout (28 H); No.2 0 ("[Maj Gen Butler] Aug [Acton] ... [Imboden] [Cairo]"); No.9 0 (9 H, nonsense); No.1 shuffled 0 ("Copy to [Pemberton] [Killed]") | 28 | blind word Grapes, Flag = 11 and Imogene = 3 PM equal the header (11 Aug, 3 PM) | FOUND: Papers of Ulysses S. Grant vol. 11 (IA `papersofulyssess0011gran`, be-api phrase "left Gordonsville yesterday morning": "met a Eleven Oclock last night, left Gordonsville yesterday morning & reports that Longstreets entire ..."); page not located |
| 9049/157/1 | E121, 16 Aug 1864 8.30 PM, McCaine, for Sheridan: "The discharge of the Ohio militia leaves West Virginia much exposed to raids and there are no troops that Canby sent for its defense except from your army", signed General-in-Chief | No. 1 | 13/13/2 of 28 | No.1 13 of 13 in order; No.2 0 ("[Crook] Gas for [Schenck R C] ..."); No.9 0; No.1 shuffled 0 | 13 | Nelly = 8.30 PM and Gas = 16 equal the header | FOUND: "Sheridan: The discharge of the Ohio militia leaves West Virginia much exposed to raids, and ..." in OR I/43 pt 1 (IA `warofrebellion431unit_0`, `warofrebellionco0043unit`, `cu31924080776929`, `11548984bsb`); page not located |
| 9053/161/2 | E122, 21 Aug 1864 4 PM, McCaine at Winchester, signed Augur: "[100 Spencer(?)] rifles with 20,000 rounds of ammunition for them will be sent you at once to Harpers Ferry. I doubt if 100 men are sufficient for the work they are undertaking" | No. 1 | 12/6/0 of 23 | No.1 10 of 10 (reads in order); No.2 4 H, 0 clauses; No.9 0; No.1 shuffled 0 ("[Pemberton] ... rounds of [Petersburg] for them will be sent you at once to [Killed]") | 9 H, 1 M | the entry carries no blind/time/date words, so no header check; the book rests on the clause alone | not located: IA full text 0 for "rounds of ammunition for them will be sent you at once", "will be sent you at once to Harpers Ferry", "sufficient for the work they are undertaking"; cached OR/ORN set (158 volumes) 0 for three phrases; Google Books on "doubt if a hundred men are sufficient" returned only unrelated hits |
| 9055/163/1 | not read | - | - | - | - | step 0: Eckert's telegram of 23 Aug 1864 ("The [Brutus] has gone out home & will not get back until [Nancy] by that time will have you a reply & order to seize articles when purchased stop Its very impt that [Bos tin] shouldnt deliver before [Rosalie] tonight will hurry matters"): the body reads in order as English; names and two time words are the code | not searched (not decoded); Google Books on "seize articles when purchased" Eckert 1864 returned only unrelated hits |
| 9062/170/2 | E123, 3 Sept 1864 8.30 PM, Stanton to Maj. Gen. Peck, New York: "Your telegram respecting the rebel plot to seize the sound steamers has been received and communicated to the Secretary of the Navy. If this Department can render any service to owners or shippers towards guarding or arming their vessels it will be cheerfully given and you may so inform them" | No. 1 | 18/20/5 of 36 | No.1 16 of 16 in order; No.2 0 ("[Valley] [Mask]ing the [Rail-road] plot ... [Deserter] can render ..."); No.9 0; No.1 shuffled 0 | 16 H, 1 M | Nelly = 8.30 PM equals the header (both No.1 and No.2 give this time word, so it does not pick the book) | ANTECEDENT FOUND: Peck's telegram to Stanton, New York, 3 Sept 1864 ("Collector Barney reports that his detectives have discovered a plot of the Confederate pirates to capture six Long Island Sound passenger steamers. The steamer Electric Spark ...") in OR I/43 pt 2 about p.21 (`warofrebellion432unit`, cached text); Stanton's reply not located in IA full text (0 for "cheerfully given and you may so inform them", 0 for "plot to seize the sound steamers", one 503) |
| 9086/194/1 | E124, 2 Oct 1864 12 m, Beckwith at City Point, signed Geo K Leet, for Grant: scouts' report that a division of infantry thought to be Kershaw's went by rail from Richmond to Gordonsville and marched to join Early | No. 1 | 18/15/2 of 51 | No.1 16 of 16 in order; No.2 0 ("[Jeff Davis] ... [Mobile] to [Decatur]"); No.9 0; No.1 shuffled 0 | 16 | Francis = 12 equals "12 m"; "Sunday" is plain and 2 Oct 1864 was a Sunday | FOUND: Papers of Ulysses S. Grant vol. 12 (Google Books snippet, "The Papers of Ulysses S. Grant: August 16-November 15, 1864": "supposed to be Kershaws - was sent by rail from Richmond to Gordonsville and last tuesday it was marched from Gordonsville to join Earl"); be-api missed it on the spelling "Kershaw's"; page not located |
| 9088/196/1 | N2-EA, 8 Oct 1864 2 PM, Beckwith at Fort Monroe, signed Geo K Leet, for Grant: scouts' report that cars have not run on the Central railroad since last Saturday and transportation is carrying government property from Richmond to Danville "preparatory to the evacuation of Richmond" | No. 2 | 26/26/5 of 69 | No.2 24 of 24 in order; No.1 0 ("[Weldon] to [Galveston] ... [Front] of [Weldon]"); No.9 0; No.2 shuffled 0 | 24 | Youth = Saturday in No. 2 (key-no2 p.25), and 8 Oct 1864 was a Saturday; header "No. 2" | FOUND: Papers of Ulysses S. Grant vol. 12 (IA `papersofulyssess0012gran`, be-api phrases "preparatory to the evacuation of Richmond" and "cannot be held a month longer", one hit each); page not located |
| 9113/221/1 | E125, 4 Nov 1864 (12 m), to Brig. Gen. Stevenson: "It is reported that Rosser is at Leesburg with brigade. General Sheridan should be informed of this and dispositions made to prevent him from crossing the river" | No. 1 | 14/13/6 of 28 | No.1 13 of 13 in order; No.2 0; No.9 0; No.1 shuffled 0 | 13 H, 1 M | Francis = 12 and Penny = 4 equal the header (4 Nov); image reads Francis/Penny, the volunteer Frances/Jenny | FOUND, word for word: OR I/43 pt 2 p.540, "Washington, November 4, 1864 -- 12 m. Brigadier-General Stevenson: It is reported that Rosser is at Leesburg with brigade. General Sheridan should be informed of this, and disposition made to prevent him from crossing the river. H. W. Halleck" (IA `warofrebellion432unit`, cached text, page read from the page-number markers) |
| 9124/232/1 | not read | - | - | - | - | step 0: 16 Nov 1864, Horner, New York, for Kasson: "It is of the greatest consequence that Tucker should be arrested if possible. No trouble or expense should be spared to effect the arrest": body in clear, only the addressee and signature are code | Google Books on the clear phrases: no hit for Tucker/"no trouble or expense should be spared" except unrelated volumes (one 503); not located |
| 8967/75/2 | E126, 21 May 1864 10 AM, J. C. Van Duzer, Nashville, for Brig. Gen. [Webster?] at Nashville: "All Indiana militia have been ordered to Nashville. The 100 & 33 [133d] Regiment left Indianapolis yesterday. It is expected that more will soon follow", signed General-in-Chief | No. 1 | 21/16/5 of 29 | No.1 20 H in order; No.2 0 ("[Butler] May Harrow Plunge ... [Surrounding]"); No.9 0; No.1 shuffled 0 | 19 H, 1 M | Harrow = 20 + Plunge = 1 = 21 (header 21 May) and Emily = 10 AM equal the header; the `u` Huntington hits (three 1863 pages) do not state this | FOUND, word for word: "Nashville, Tenn.: All Indiana militia have been ordered to Nashville. The One hundred and thirty-third Regiment left Indianapolis yesterday. It is expected that more will soon follow" in OR I/38 pt 4 (IA `warofrebellion0038unse_04pt`, `warofrebellionco0038majg`, `warofrebellion013804rootrich`, `unitedstatescon108offigoog`); page not located |

Clause counts are by one reader (decoder output for each book and the shuffled copy in `ls5_r1d_controls.txt`, seed 7, `ls5_r1d.py`); the vocabulary shares do not pick the book (0.26-0.72 for No.1, 0.29-0.56 for No.2, within 0.1 of each other on five rows) -- the clause under each book does, with the header words where the entry carries them. E122 has no header words, so its book rests on the clause alone; E123 reads under both No.1 and No.2 for the time word but only No.1 reads the sentence.

Grades: decoder H as in the table; by hand: E122 "Spencer" is the key row "Has, or have been, reinforced" but is plainly the rifle's name here: M (H 9, M 1); E123 tail "wheres French [Thomas]" is filler read as a name: M (H 16, M 1); E125 tail "Jen guess its [Longstreet]" filler: M (H 13, M 1); E126 "Webster" is the signature row but stands in the address as a name: M (H 19, M 1). Totals over the eight filed: H 138 (E120 28, E121 13, E122 9, E123 16, E124 16, E125 13, E126 19, N2-EA 24), M 4, C 0, I 0.
Unread, not graded: E120 "satin", "Hump"; E122 "pos"; E126 "Pekin"; E124/E125 fillers.
Image vs volunteer text (image taken): 9043 "are expected" (volunteer "an expected"); 9113 header "Francis ... Penny" (volunteer "Frances ... Jenny"); 9088 "all being used to Convey" (volunteer "all being used to convey Convey", an overlap of the two line-breaks); 8967 "Plunge" (volunteer "Plunger").

Print: be-api full text (the positive control, E88's phrase, answered 502 on this run and was not retried at length), 2-4 decoded phrases per entry, the cached OR/ORN set (158 volumes, `ls5_r1d_printcheck.py`: positive hit for E125 only), and Google Books (country=US) on decoded phrases. Located: E120, E121, E124, E125, E126, N2-EA (and the antecedent of E123); not located: E122 and Stanton's reply E123. The Grant Papers volumes are located by snippet only, no page. A miss is a search result for the log, not a statement about print (rule 10); these entries are not sent to a verifier except E122 (and E123 for the reply, whose antecedent is printed).
Requests: hdl.huntington.org 11 (8 images, 3 item info); archive.org be-api about 30; googleapis.com about 20.

## Remaining gaps (LS5-R1d, 8 Oct 2026)
Read so far: of eleven rows, 8 filed (E120-E126, N2-EA), 3 step-0 skips (9036/0, 9055/1, 9124/1); located in print: E120, E121, E124, E125, E126, N2-EA, E123's antecedent; not located: E122, E123's reply.
- E122 print location - blocker: not-attempted; only phrase searches were run on it; next: a verifier phrase search on "Spencer rifles" Harpers Ferry Augur in OR I/43 and Grant Papers vol. 12, ~$0.6
- Grant Papers page numbers for E120, E124, N2-EA - blocker: needs-physical-access; no page locator is reachable from the cloud (be-api page_num is not a locator, books.google.com page view is blocked); next: the owner's own Google Books or HathiTrust page view, a LOCAL-QUEUE row

## Escalation (LS5-R1d, 8 Oct 2026)
- [x] siblings: shared pages checked (E26, E33, E91 are other entries on 9053, 9055, 8967; none of my entries).
- [x] clear-pages: three rows stopped at step 0.
- [x] known-keys: each entry decoded with all three books and a shuffled copy of the chosen book.
- [x] print: be-api phrase pass, cached OR grep, Google Books on decoded phrases.
- [n/a] key-rebuild: no key row added.
- [x] image-check: 9043, 9049, 9113 (header), 9088 (lines 9-12) from crops; the rest from page overviews against the volunteer text.
- [x] retry: failed be-api phrases retried once, 502/503 left logged.
Verdict: keep going: 1 internal gaps; cheapest next: a verifier phrase search for E122, ~$0.6

## LS5-R1e (8 Oct 2026, account 1, for LANE LEDGER)

Eleven PF4-clean Cipher No. 1 rows (8984/1 9034/1 9124/0 8992/1 9034/0 9044/1 9081/0 9098/1 9120/0 9139/1 9144/0). Row numbers follow PF4's `prefilter-ls4.tsv` header column, not the block order of the Huntington text (8984/1 is the first block, "930 pm"; 9139/1 is Capt Bruch).
Result: eight filed (E140-E147, `ciphertext.txt`, all Cipher No. 1; `decode.py --write` then `--check` exit 0); three stopped at step 0 (9081/0, 9098/1, 9120/0, not decoded for filing). Located in print by phrase: E140, E141, E142, E144, E147; not located: E143, E145, E146.

Prior-work checks (hand run, `tools/prior_work.py` does not exist): (1) own work, `git fetch` then grep of each pointer and page in NOTES/AUDIT/HYPOTHESES/ciphertext*/entries-mssEC19.tsv and the last 1,500 ROOM lines: only the PF4 list names these rows; neighbours already filed on the same pages are E44 (9124, 8.30 PM Sheldon), E51 (9098, 11 AM), N2-BK (9139 entry 2), E13/E14 (9035, a different page); no claim by another worker on these pointers. (2) leaf and neighbours: the 10 page images fetched once at 2400 px (below); no gloss or clear copy on any of the ten leaves. (3) holder: the Huntington transcription of each pointer read first (step 0); no solver-repository file for mssEC 19 consulted beyond the print-check hits below. (4) editions: OR cached set (158 volumes, `ls5_r1e_printcheck.py`), be-api phrase search, Grant Papers vol. 11 by identifier, Google Books (country=US) for the Grant/Halleck/Dana/Meigs rows. Positive control: E144's phrase hit in Grant Papers vol. 11 (identifier `papersofulyssess0011gran`) as expected.

Images: `hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg` for 8984 9034 9124 8992 9044 9081 9098 9120 9139 9144, 10 requests, 3.2 s apart, to scratch, not committed (hdl token taken 17:5x, released after). Pages 8984, 9034, 8992, 9044 and 9139 were read against the whole-page image (one eye, no subagent, no crop tool: legible at 2400 px; the brief's `tools/iiif_lines.py` crop step was not run because I viewed the full page myself and no subagent was called); the volunteer text agrees with the image on every word of the filed entries on those pages. 9124 and 9144 (E142, E147) were not viewed: volunteer text only, both entries also match the printed wording below word for word where compared.

| row | ID | book | shares No.1/No.2/No.9 of N | clause check: chosen / other books / shuffled chosen | H (decoder; hand moves in Grades) | step 0 / prior work | print |
|---|---|---|---|---|---|---|---|
| 8984/1 | E140, 12 Jun 1864 9.30 PM, McCaine, to Maj. Gen. Hunter: "It is understood that Grant is about to move his army to the James at or near City Point & that he will continue you to hold the bridge across the Pamunkey at White House to facilitate the junction of yourself & Sheridan with the Army of the Potomac" signed Halleck's word (General-in-Chief) | No. 1 | 20/15/3 of 37 | No.1 reads as one clause (Hunter, Grant, Sheridan, Army of the Potomac); No.2 reads "Jeff Davis ... Cairo ... Schofield ... Wallace Lew"; No.9 nothing; shuffled No.1 "Cars ... Grand Junction ... Pemberton" | 15 + C1 (Mutton = Hunter) | none; "Mutton" is a known Hunter word, all else code | FOUND word for word: "to facilitate the junction of yourself and General Sheridan with the Army of the Potomac" in Pond, The Shenandoah Valley in 1864 (IA `shenandoahvalley00ponduoft`, `shenandoahvalle00pondgoog`, `shenandoahvalley0000pond`, `in.ernet.dli.2015.82946`); the OR page was not read |
| 9034/1 | E141, 4 Aug 1864 11.30 AM, McCaine at Monocacy, to Hunter: "I have seen Mask's dispatch to you of last evening and think that he should be immediately reinforced by cavalry. Sheridan's cavalry is beginning to arrive and will be sent forward soon" signed General-in-Chief | No. 1 | 14/10/3 of 25 | No.1 11 of 11 coherent; No.2 0; No.9 0; shuffled 0 | 11 + C1 (Mackerel = Hunter) | none | FOUND: "Sheridan's cavalry is beginning to arrive, and will be sent forward soon. H. W. HALLECK" in OR I/43 pt 1 (IA `warofrebellion431unit_0`, `warofrebellion014301rootrich`, also `warrebellionaco08offigoog`); the phrase "immediately reinforced by cavalry" did not hit (the decode's "reinforced by cavalry" is one reading of the code words) |
| 9124/0 | E142, 16 Nov 1864 11.30 PM, Horner: "[John Odell (care of Bunker, New York)]. You are hereby directed to arrest Beverly Tucker wherever found within the United States and turn him over to [Dix] to be confined in Fort Lafayette. By order of the President" signed Dana | No. 1 | 13/14/4 of 30 | No.1 coherent; No.2 13 H, not coherent; shuffled 0 | decoder 11, hand 10 + M 1 | none; the first word "John" is the plain name of the addressee, not the Grant row | FOUND word for word: OR II/7 p. 1132 (IA `warofrebellion0207rootrich`; running heads 1132/1133 bracket it): "War Department, Washington City, November 16, 1864 -- 11.30 p. m. JOHN ODELL: (Care of Bunker, New York.) You are hereby directed to arrest Beverly Tucker wherever found within the United States and hand him over to General Dix, to be confined in Fort Lafayette. By order of the President: C. A. Dana, Assistant Secretary of War"; same text in Google Books snippets of OR II/7 |
| 8992/1 | E143, 30 Jun 1864 3 PM, New York, to Maj. S. Van Vliet: "All the steamers now in service fit to bring [?] from New Orleans and which can possibly be spared for that service should be dispatched as they become available. It is not necessary to take up ocean steamers not already in service. I am not advised of the number of troops but am to prepare for a large number" signed Qr Master Genl U.S. (Meigs's word) | No. 1 | 15/14/4 of 44 | No.1 14 of 14 coherent; No.2 13, not coherent; No.9 4; shuffled 0 | 14 | none | not located: "ocean steamers not already in service", "steamers now in service fit to bring" 0 in be-api; the cached OR set none; Google Books returned a Quartermaster history snippet (Meigs ordering steamers) but not the telegram |
| 9034/0 | E144, 4 Aug 1864, Van Valkenburg: "Copy to Sherman. From City Point, 3 Aug, for General-in-Chief. Richmond dispatch of to-day contains the following: ... Our cavalry under [Iverson] attacked the enemy yesterday near Clinton. The [Yankees] commanded by General Stoneman were routed and Stoneman, 75 officers and about 500 prisoners with 2 pieces of artillery surrendered and have just reached this city. The rest of the Yankee force are scattered and flying towards Eatonton" signed Grant | No. 1 | 36/29/8 of 65 | No.1 34 of 34 coherent; No.2 27, not coherent; shuffled 34 H but the meanings are the shuffled ones (not coherent) | 34 | none | FOUND: "...commanded by Gen Stoneman were routed, and Stoneman, seventy five officers, & about five [hundred prisoners]..." in The Papers of Ulysses S. Grant vol. 11 (IA `papersofulyssess0011gran`, be-api by identifier); OR I/38 and I/40 not read |
| 9044/1 | E145, 12 Aug 1864, Beckwith and McCaine, to Lt Col Bowers AAG at City Point, copy to Sheridan at Winchester: "[...] 1 brigade of Hill's corps was sent to Early last Friday; [division] to which it belongs was under marching orders. Fitz Hugh Lee's cavalry was [at] Orange C.H. Wednesday night; Longstreet is in the Valley and his corps supposed to be with him. [...] know nothing of [force] mentioned in your dispatch of 10th. They say Central [Road] is not in running order beyond Beaver Dam" signed Geo. K. Leet, Capt. and A.A.G. | No. 1 | 33/30/8 of 72 | No.1 30 of 30 coherent (Bowers, City Point, Sheridan, Winchester, Lee, Orange C.H., Longstreet); No.2 26, not coherent; shuffled 0 | decoder 30, hand 28 + M 2 | none | not located: "Longstreet is in the Valley and his corps" 0, "Fitz Hugh Lee" in the Grant Papers vol. 11 query 0, cached OR set none; Google Books surfaced Grant Papers 16 Aug-15 Nov 1864 (Leet) but no match to this text |
| 9139/1 | E146, 12 Dec 1864 2 PM, Capt. Bruch, Louisville, to Brig. Gen. Allen, Chief Quartermaster: "General Donaldson recommends that the manager of United States Military Railroads be instructed to take immediate possession of the Louisville and Nashville Railroad as vitally necessary to sustain the army. Do you concur in his opinion or will it be sufficient to place a portion of the US Mil. Railroad rolling stock upon that road? Will not the Louisville and Nashville Railroad company be able to do all that is possible without the interruption caused by changing hands ..." | No. 1 | 29/31/8 of 80 | No.1 26 of 26 coherent, and the leaf carries the marginal "No 1"; No.2 29 H, not coherent; No.9 8; shuffled 0 | 26 | none; marginal "No 1" over the Bruch header | not located: "Louisville and Nashville Railroad" in OR I/45 pt 2 gives only an unrelated sentence; the cached OR set none; Donaldson's 4 Dec 1864 report appears in `warofrebellion452unit` (a neighbour, not this telegram) |
| 9144/0 | E147, 28 Dec 1864 4 PM, Van Duzer, to Maj. Gen. Thomas: "General Stoneman's dispatch is received. I would respectfully suggest that supplies for the troops [pursuing] the wrecks of Hood's army be sent to Eastport or some other point on the Tennessee River; also that troops not required for this pursuit be sent by water to General Dana to assist in destroying the railroads and supplies in Mississippi which may otherwise be used by Hood in his retreat" signed General-in-Chief | No. 1 | 24/23/4 of 55 | No.1 21 of 21 coherent; No.2 20, not coherent; shuffled 0 | 21 + C1 (Handle = Hood) | none | FOUND word for word: OR I/45 pt 2 p. 388 (IA `warofrebellion452unit`), Halleck to Thomas, Washington, 28 Dec 1864, 4 p.m., "General Stoneman's dispatch is received. I would respectfully suggest that supplies for the troops pursuing the wrecks of Hood's army be sent to Eastport, or some other point on the Tennessee River; also that troops not required for this pursuit be sent by water to General Dana ..." |
| 9081/0 | step-0 skip: Richards, Boston, 28 Sept 1864, "You will please mark down the person whose description is given below and when found keep under strict watch and notify this Department ... a young man named Wild about twenty three years of age five feet eight light complexion sandy goatee and moustache ..." | not decoded for filing | 12/15/3 of 71 | not run for filing (the decoder's first pass on it is in `ls5_r1e_controls.txt`, X7) | - | body reads in order as English; only the addressee, a few names and the signature are code words: N1-likely, clear in the Huntington's public transcription (pointer 9081) | not searched |
| 9098/1 | step-0 skip: Horner, 21 Oct 1864 2 PM, "It is [reported] that you have in your employ a detective named Kinney. He is to be dismissed immediately. By order [of the Secretary of War]" signed Dana, Asst. Secretary | not decoded for filing | 13/11/6 of 25 | not run for filing (X8 in `ls5_r1e_controls.txt`) | - | one code word ("wicked") in a clear sentence; substance and the name Kinney are in the transcription (pointer 9098): N1-likely | not searched |
| 9120/0 | step-0 skip: Sampson, 10 Nov 1864, "Before taking any proceedings against Bernal the British Consul or his wife consult with [Seward] and be governed by his instructions" | not decoded for filing | 7/6/2 of 21 | not run for filing (X9 in `ls5_r1e_controls.txt`) | - | body in clear in the transcription (pointer 9120): N1-likely | not searched |

The shares do not pick the book (0.3-0.6 for No.1, 0.3-0.5 for No.2, within 0.1-0.2 of each other in most rows, as in LS3-R9 and LS4-R1b); the clause under each book does, with the header check: the decoder's time/date words agree with the ledger header in E140-E147 where the entry carries them (E141 Aug 4 11.30 AM, E144 Aug 3/Aug 1 words are in-text dates, E145 Aug 12). Matched control = No.2 and No.9 decodes of the same text plus the meaning-shuffled No.1 copy (`ls5_r1e.py`, output `ls5_r1e_controls.txt`); the H counts of a shuffled copy equal the real count by construction (lookup does not depend on the meaning), so the control is the hand clause reading of the shuffled meanings, which fails in every row. No numeric gate was wired to a control here.

Grades: decoder H as in the table; by hand: E142 "John" is plain (the printed text has "JOHN ODELL"), the decoder's Grant row is wrong here: M (H 10, M 1); E145 "France" ("was [New York] [Orange C.H.]") and "Beaver" ("beyond [Cahawba] Dam", a plain Beaver Dam) do not read from the book in context: M, so H 28, M 2. Totals over the eight filed: H 159 (E140 15, E141 11, E142 10, E143 14, E144 34, E145 28, E146 26, E147 21), C 3 (Hunter x2, Hood), M 3, I 0.

Print: be-api full text with identifier-restricted queries for the Grant Papers vol. 11 and OR volumes, 2.2 s apart, 502/503 answered several calls (retried once); one Google Books query per Grant/Halleck/Dana/Meigs row (country=US). A miss is a search result for the log, not a statement about print (rule 10). Basler's Collected Works and the Butler volumes were not searched (no filed entry here is signed by Lincoln or to or from Butler).

## Remaining gaps (LS5-R1e, 8 Oct 2026)
Read so far: of eleven rows, eight filed (E140-E147), three step-0 skips. In print by phrase: E140, E141, E142, E144, E147. Not located in what was searched: E143, E145, E146.
- E143 (Meigs to Van Vliet, 30 Jun 1864) - blocker: not-attempted; print search limited to two be-api phrases and the cached OR set; next: phrase search of OR I/37 pt 1-2 and III/4 with a local grep, and the QMG Consolidated Correspondence, ~$0.5
- E145 (Leet to Bowers/Sheridan, 12 Aug 1864) - blocker: not-attempted; Grant Papers vol. 11 searched by three words only; next: read Grant Papers vol. 11 pp. around 12 Aug 1864 and OR I/43 pt 1 for the Leet telegram and the 10 Aug dispatch it answers, ~$0.5
- E146 (Bruch to Allen, 12 Dec 1864) - blocker: not-attempted; only one OR I/45 pt 2 phrase and the cached set were tried; next: OR I/45 pt 2 around 12 Dec 1864 and the Quartermaster-General's Louisville correspondence, ~$0.4
- one unread word each in E143 ("whiskey", plain in the image, not in the key) and E145 filler words - blocker: no-key-material; neither word reads from any book row in context; next: compare with other entries carrying the same words, ~$0.2

## Escalation (LS5-R1e, 8 Oct 2026)
- [x] siblings: same-page neighbours E44, E51, N2-BK checked, not duplicates.
- [n/a] clear-pages: nothing in this pass.
- [x] known-keys: each filed entry decoded with all three books and a shuffled copy.
- [x] print: cached OR set, be-api, Grant Papers vol. 11 by identifier, Google Books; partly blocked by 502/503.
- [n/a] key-rebuild: no key row added.
- [x] image-check: five of seven filed pages viewed whole at 2400 px (E142, E147 volunteer text only).
- [x] retry: failed be-api phrases retried once.
Verdict: keep going: 3 internal gaps (print location of E143, E145, E146), cheapest next: a verifier phrase search with local OR grep, ~$0.5 per entry
