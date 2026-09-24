# Eckert Papers, 1864 "Ciphers Sent" ledger (Huntington mssEC 19) read with Cipher No. 1 (mssEC 41)

status: partial
checked: 20 Sept 2026 (section 8 added; sections 1-7 as checked 19 Sept 2026)
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
E6 N1, E12 N1, E4 N3, E5 N3. **Second audit (adversarial), 24 Sept 2026 (AUDIT.md):** E4 and E5 confirmed N3, not raised to N4 (JSTOR and HathiTrust full text still to run); OR I/36 pts 1-3, I/51 pt 1, III/4, the OR Supplement pt I, Fox's Confidential Correspondence, the Lincoln Papers and Google Books were added to the search, all negative. Both telegrams also survive in a second ledger copy, mssEC 25 p.77 (E4) and p.79 (E5), still in cipher in the volunteers' transcription; it reads "Buxton" for the M token "Brenton" (residual for a solver, not yet checked against the image). "Not printed" in the earlier text of this folder meant only "not matched by the
or_check sweep" and must not be read as "unpublished". Preference for unprinted entries could not be pushed
further within the budget: most unmatched candidates were the Beckwith and Kimber entries, which are in the
other cipher (section 2).

Result: all twenty read cleanly from the book; the seventeen OR-printed ones (the sixteen of the sweep and E6) agree with the OR word for word apart
from clerical slips and the times (the OR rounds or omits them; the ledger gives the half hour). Code-word
tokens over the twenty entries: H 296, C 8, M 1, I 0 (`python3 decode.py` prints the count; the C and M tokens are the rows
of key.md section 7 that appear in the entries (the addressee words Prss, Praise, Submit, Mackerel, Mutton; Hedge,
Nansy, mangled; Brenton M). `python3 decode.py --check` regenerates the readings from ciphertext.txt and key.md
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
- Novelty audit: AUDIT.md (verifier session, 20 Sept 2026). No entry in this folder is at N4 or N5; none may be
  described outside the repo as a first decipherment or as unpublished plaintext.

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
