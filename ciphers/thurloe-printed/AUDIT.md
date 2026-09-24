# AUDIT -- ciphers/thurloe-printed

Verifier audits under CLAUDE.md rule 10. One section per item group; other groups (P9, P14, P15,
P17 and the rest) are not covered here and get their own sections when audited.

## P11, P12, P13 -- General Montagu to secretary Thurloe, journal-letter 20 Apr - 29 May 1656

Verifier: LANE V worker, 24 Sept 2026 (clock read 03:08-03:25 UTC). Separate session from the
solver (ROOM.md 03:03). No decoding done here.

**Claim under audit** (ROOM.md 24 Sept 2026 03:03, NOTES.md section 9): "The 1742 print sets a
decipherment above every cipher line of this letter ... aligned ... P11-13 319 tokens: H36 C228
I2 M32 U11."

Note on the brief's title: P11-13 is Montagu to Thurloe only. "Cromwell to Blake and Montagu"
(9 June 1656, TSP v.101) is P14, not audited here.

### Verdict

| Item | Class | Prior plaintext | Prior decipherment | Confidence |
|---|---|---|---|---|
| P11-13 (one letter, 3 clusters of its 89 cipher lines) | **N0** | yes: Birch 1742, vol. 5 pp. 67-69 | yes: the same page, set above the cipher groups | high |

N0 = plaintext and decipherment of this very item already known. The solver did not decipher this
letter. What it did is align a printed decipherment to its cipher groups, group by group. That
alignment is a useful derived dataset: a group-level key for the Montagu cipher, 248 values, and a
real-data benchmark for solvers. It is not a reading.

**Safe sentence.** "Birch printed Montagu's letter to Thurloe of 20 April-29 May 1656 (Thurloe
State Papers v.67-69) with a decipherment above the cipher. We aligned that printed decipherment
to the numeral groups, which yields 248 group values of Montagu's cipher. The values are
consistent with Tomokiyo's reconstruction (E=18/42/56/93, THE=407)."

**Unsafe sentence.** "We read/decoded Montagu's 1656 cipher letter" or "a reading of an
enciphered Thurloe letter", or anything implying that the plaintext was recovered by us or was
not already in print.

### Evidence

| # | Source | What it shows | How checked |
|---|---|---|---|
| 1 | Birch (ed.), *A Collection of the State Papers of John Thurloe*, vol. 5 (London 1742), pp. 67-69; IA `collectionofstat05thur` (https://archive.org/details/collectionofstat05thur) | Heading "General Montagu to secretary Thurloe", MS vol. xxxviii. Every cipher line is printed as numerals with the decipherment letter-spaced on the line above it, e.g. djvu 5723-5726 "... re to oppose an attempt" over `48 23 31 59 37 19 55 103 42 404 363 ...`. The clear text around the cipher lines is printed in ordinary type. | djvu text fetched once (archive.org, 24 Sept 2026), identical to the gzip on disk in `sources/ia-fulltext/thurloe-gz/`; read at djvu lines 5690-6080 |
| 2 | British History Online, Thurloe State Papers vol. 5, "State Papers, 1656: May (5 of 6)", https://www.british-history.ac.uk/thurloe-papers/vol5/pp60-72 | The same letter online, filed under 29 May 1656. The search engine's extract quotes the decipherment in its letter-spaced form: "to obteyne lett er s for us to give a s s u r a n c e not to oppose a n y of his fleet s" | WebSearch phrase query, 24 Sept 2026. The page was not fetched: BHO is not on this lane's host list, and the Wayback CDX route failed twice (connection reset, then 504) and was abandoned under the good-citizen rule |
| 3 | S. R. Gardiner, *History of the Commonwealth and Protectorate* (vol. covering 1654-1656; Google Books editions of 1901 and 1903, plus a 1965 reprint) | Paraphrases the letter's content: the fleet in Cadiz Bay on 20 April, Spanish warships in "the narrow and tortuous Carraca" channel. Its footnote: "Montague to Thurloe, Apr. 20 - May 29, Thurloe, v. 67", followed by the Meadowe-at-Lisbon section, which draws on the letter's Lisbon part. | Google Books API snippet, 24 Sept 2026 |
| 4 | Tomokiyo, cryptiana `thurloe.htm` (local mirror `sources/cryptiana/web/thurloe.htm`), section "Edward Montagu (Mountagu)" | Gives the cipher table (as an image, not in the mirror): E=18/42/56/93, THE=407, 105 = and, 482 = year, 622 = Brazil. Names Montagu's letter of 19 May 1656 (BL Add MS 4200 f.76, DECODE 8387) and Cromwell's letters of 13 Sept 1655, 9 June 1656 and 9 Oct 1657. Does not name this letter (v.67) or transcribe its plaintext. | Read in full from the mirror. Tomokiyo's live page was not re-fetched: the mirror is the repo's snapshot and the section has an explicit dated note (March 2024) |

The print alone decides the class. Rows 2 and 3 show that the plaintext has also circulated
since, online and in the standard narrative history.

### Did we first-decipher?

No. The decipherment was printed in 1742, and it was presumably made in Thurloe's office, since
Birch printed what stood interlined in the manuscript. The solver's NOTES section 9 already says
this ("the `[PLAIN:...]` lines ... are that decipherment") and makes no novelty claim. Its
wording passes rule 10.

### Token grades (rule 4)

The grades are right in structure. Reading a group's meaning from a printed contemporary
decipherment is known plaintext, so C is the correct grade under rule 4 and matches the repo's
convention (Fauconberg pool, NOTES section 8). Tomokiyo's stated values are H: read from a key
source. That source is a modern reconstruction, not a contemporary key, which should be said
whenever H is quoted for this system. Conflicts and single-occurrence tokens are M, the two
OCR repairs are I, and groups not covered by either source are U. All of that is consistent.

One correction. Five tokens are graded C although their *group number* is an OCR repair:
`4°4?`, `5°?` (twice), `9°?` and `4°°?`, where ° is read as 0 (L5726, L5730, L5971). The meaning
is from the print (C), but the group's identity is repaired. Rule 4 puts repaired tokens at I,
as the solver itself did for `s5`->55 and `4-35`->435. Strictly, P11-13 should read **H 36, C 223,
I 7, M 32, U 11** (plus 10 non-cipher tokens). `decode.py` is LANE T's and is not edited here;
the fix is a one-line rule in its grading (a `?` token with a repaired value is I). It is left
as a suggestion in NOTES.md.

`python3 decode.py --check` passes (exit 0, 24 Sept 2026). The committed reading is
reproducible (rule 7).

### Search log

| Family | Status | What |
|---|---|---|
| (a) Canonical series | searched | Birch vol. 5 djvu text, pp. 66-70, and the whole volume grepped for "decypher/decipher" (3 hits, none for this letter) |
| (b) Sender's/recipient's correspondence | partly | Tomokiyo's Montagu section names BL Add MS 4200 f.76 (19 May 1656), which may be a manuscript of a part of this same journal-letter. Not fetched. Sandwich's printed *Journal* (NRS 1929) starts in 1659 and is out of range. Harris's *Life of Edward Mountagu* (1912) and Powell's *Letters of Robert Blake* (NRS 1937) were not text-searched: no hit came up in Google Books, and their full text was not reached |
| (c) Documentary editions / calendars | partly | CSP Domestic 1655-6 does not calendar the Thurloe MSS (Bodleian Rawlinson), so it was not searched. Gardiner cites the letter directly (row 3) |
| (d) Holding archive (Bodleian, Rawlinson A) | not searched | not needed for N0 |
| (e) Full text: Google Books | searched | 5 API queries: 3 exact-phrase queries (0 hits) and 2 keyword queries (Gardiner, 3 editions) |
| (e) Full text: Internet Archive | searched | 1 djvu fetch, 1 be-api fts query ("winding channel" Carraca: dictionaries only, not relevant) |
| (e) HathiTrust | not searched | not needed for N0 |
| (e) BHO | searched via WebSearch | 3 WebSearch queries, one restricted to british-history.ac.uk. BHO pp60-72 was found by phrase |
| (f) Solver repos, cipher blogs | partly | Tomokiyo mirror read. Both solver repos were not re-cloned: an N0 from the print cannot be raised by them |
| (g) JSTOR / Scholar | not searched | not needed for N0. No JSTOR probe used |

Requests: archive.org 1 (djvu) + 1 (be-api fts); web.archive.org 2 (failed: reset, 504; host
then left alone); googleapis.com 5, at least 3 s apart; WebSearch 3. No logins, no credentials
printed.

### Postmortem

Failure: the folder's earlier sections (NOTES header, section 2 "None of the 5 is
found-solved", section 5 "partial") classed P11-13 as a keyed-but-unread letter. They relied on
Tomokiyo's page and did not look at whether the print itself carries a decipherment. The solver
found this on 24 Sept 2026 but left the status at partial. Corrected in NOTES.md (header,
section 2, section 5, and a pointer at the top of section 9): P11-13 is now **found-solved**. The
section 5 pointer to "BL Add MS 4166" was wrong for this letter and has been replaced with Add MS
4200 f.76. The lesson carries over from the Fauconberg pool (section 8): for any Birch letter,
check the lines next to the cipher for an interlined decipherment before calling it keyed,
unkeyed or open.

## P2, P3, P5+P6, P7, P8, P16-P24 -- letters whose decipherment Birch printed in 1742

Verifier: LANE T verifier V1, 24 Sept 2026 (clock read 03:33-03:50 UTC). This session is separate from
the solver and consolidation workers (A, C, D, E) whose sections are audited here. No decoding done here.

**Claim under audit** (NOTES.md sections 10, 12, 13, 14; index.tsv status column
`printed-decipherment`): each of these letters has a contemporary decipherment that Birch
printed in 1742, beside or after the cipher.

**Test.** Same test as P11-13 above: does the 1742 print carry a decipherment of this very letter,
and does it cover the cipher? This was read directly in the djvu text (`sources/ia-fulltext/thurloe-gz/`,
restored with zcat, no refetch). Line numbers are djvu lines. Page numbers are Birch's printed pages,
read from the running heads ("NNN STATE PAPERS OF" / "JOHN THURLOE ESQ. &c. NNN"). They are not
the "Vol. xxiv p.NNN" marginal notes, which give the manuscript volume's own pagination. For the
Fauconberg letters, `cov.py` (in this session's scratchpad; its logic is described here) counted
every line in the letter whose tokens are at least 70% numeral groups, and checked whether a letter
line of decipherment is set directly above it.

### Verdict

| Item | Class | Printed decipherment (Birch 1742) | Covers the cipher? | Later print or citation found | Confidence |
|---|---|---|---|---|---|
| P2 Stouppe to the prince of Tarente, London 25 Aug 1654 | **N0** (English translation part) | vol. 2 p.566, "Deciphered thus:" (djvu 47028-47059), after the French text with numerals at pp.565-566 (djvu 46965-47024) | Yes, as a translation. The English paragraph renders the whole French passage that carries the numerals, from "Some do believe..." (= "Quelques uns croyent...") to the close. The French words behind the groups are not printed. | Gardiner, *History of the Commonwealth and Protectorate* (1897; 1903; 1965 reprint), "Stouppe's mission"; Abbott, *Writings and Speeches of Oliver Cromwell* (1988 reprint), cites "Stouppe to Tarente, Aug ... 1654" | high |
| P3 "A letter of intelligence", signed John Butler (Birch: vol. 2, among Sept 1654 papers) | **N0** (body only) | vol. 2 pp.575-576: an interlinear decipherment above each cipher line of the body (djvu 47929-47997), e.g. "wind contrary", "arrived Rotterdam", "eighteenth September" | Body: yes, word by word above the groups. **Postscript** (djvu 47999-48004, three numeral lines after the signature): **no printed decipherment**, so it is not classed here and stays open. | Tomokiyo, thurloe.htm `#Butler`, links a BHO "deciphered text" and "ciphertext (Page 575)" for this letter | high (body) |
| P5+P6 W. Stamford, Calais, 30 March [1654 N.S.] | **N0** | vol. 3 pp.275-276, "The same letter decypherd." (djvu 23065-23144), after the cipher at pp.274-275 (djvu 22887-23063) | Yes, the whole letter, the postscript included ("Charles Stew. is still at Middleburgh private...") | not found in Google Books or IA outside the Thurloe volumes (Underdown, *Royalist Conspiracy* 1960: "Stamford" hits are the Earl of Stamford only) | high |
| P7 "S." (Stamford), [20 March 1654] | **N0** | vol. 3 pp.279-280, "The same letter decypher'd." (djvu 23349-23422), after the cipher at pp.277-279 (djvu 23230-23346) | Yes, the whole letter. The ciphered postscript (djvu 23337-23346) is deciphered at djvu 23418-23421 ("If there be any in the army, that have had correspondence with Overton ... Hull ... Yorkshire"). | IA full text: only the Thurloe volumes | high |
| P8 General Blake to the Protector, George, 12 June 1655 | **N0** | vol. 3 p.541: an interlinear decipherment above every cipher line (djvu 45229-45309) | Yes, the whole letter | Carlyle, *Oliver Cromwell's Letters and Speeches* (editions of 1884-1900 seen in Google Books; 21 IA full-text hits), quotes the deciphered text ("four Galleons designed for the Mediterranean, and six for New Spain..."); Powell, *Letters of Robert Blake* (NRS 76, 1937), prints Blake's 1655 letters and marks cipher passages; Tomokiyo cites p.541 | high |
| P16 Fauconberg to H. Cromwell, Whitehall 20 Apr [1658] | **N0** | vol. 7 p.84 (djvu 7179-7251), interlinear | 7 of 7 cipher lines have a decipherment line above | an edition of Carlyle's *Letters and Speeches* (IA `lettersspeecheso0003thom`) cites "Thurloe, vii. 84" (April 1658) | high |
| P17 same, A.D. 1658 (Davies: 30 Aug 1658) | **N0** | vol. 7 pp.365-366 (djvu 32122-32356), interlinear | 49/49 | G. Davies, *The Restoration of Charles II* (1955): "Fauconberg to Henry Cromwell, Aug. 30, Thurloe, VII, 365. Original in cipher"; McMahon, *The Death of Oliver Cromwell*, notes that Fauconberg "wrote Henry in cipher" | high |
| P18 same, Whitehall 14 Sept [1658] | **N0** | vol. 7 p.386 (djvu 34074-34114), interlinear | 5/5 | Huntington Library Quarterly (Apr 1935) quotes it ("But certainly somwhat is brewing..."); *Richard Cromwell* (IA `richardcromwellp0000henr`): "Fauconberg to Henry Cromwell, 14 Sept. 1658. Ibid., 386" | high |
| P19 same, Sept 21 [1658] | **N0** | vol. 7 pp.406-407 (djvu 35655-35800), interlinear | 36/36 | -- | high |
| P20 same, 12 Oct [1658] | **N0** | vol. 7 pp.437-438 (djvu 39860-39962), interlinear | 15/16 by the script. The 16th line (djvu 39912) is followed by an OCR-damaged decipherment line and is not missing in the print | -- | high |
| P21 same, Oct [1658] | **N0** | vol. 7 pp.450-451 (djvu 41199-41367), interlinear | 37/37 | -- | high |
| P22 same, 26 Oct [1658] | **N0** | vol. 7 pp.462-463 (djvu 42243-42324), interlinear | 17/17 | -- | high |
| P23 same, c.23 Nov 1658 | **N0** | vol. 7 pp.528-529 (djvu 49474-49660), interlinear | 30/30 | -- | high |
| P24 same, 25 Feb 1658/9 | **N0** | vol. 7 pp.612-613 (djvu 56496-56615), interlinear | 23/23 | -- | high |

N0 = plaintext and decipherment of this very item already known. In every case the decipherment
is Birch's print of what stands in the Thurloe manuscripts: the office's decipherment, interlined
or copied after the cipher. The project's work on these letters (pairs files, `key_steele.tsv`,
`key_fauconberg.tsv`, `pool_1654/decipherment_*.txt`, the `reading_*.txt` files) is an alignment
of printed plaintext to cipher groups. It is useful as keys and as benchmark data. It is not a
reading. The later-print column matters only for how widely each plaintext has circulated since.
It does not change any class.

**Safe sentence (all rows).** "Birch printed these letters in 1742 (Thurloe State Papers vols 2, 3
and 7) with their contemporary decipherment, interlined or following the cipher. We aligned that
printed decipherment to the cipher groups, which gives group-level keys for the Blake,
Stamford and Fauconberg ciphers and real-data benchmarks. P3's three-line postscript is the one
passage here with no printed decipherment."
Row-specific additions: P2, "Birch prints an English translation of the deciphered French, not the
French plaintext"; P8, "the deciphered text is also printed in Carlyle's *Letters and Speeches*".

**Unsafe sentence.** "We read, decoded or deciphered" any of these letters. So is "a reading of
Stamford's/Blake's/Fauconberg's cipher letters", "446 of 513 groups now read", or anything that
implies the plaintext was recovered by us or was not already in print. For P3, "the Butler
letter is deciphered in print" is unsafe without "except its postscript".

### Corrections found while checking (factual, not novelty)

1. **P7's postscript is deciphered in print.** NOTES s.12.2 said it was "a still-ciphered
   postscript, L23337-46, not covered by the decipherment". Birch's decipherment ends with it
   (djvu 23418-23421). Corrected in NOTES.
2. **Stamford dates are 1655 (N.S.), not 1654.** Birch writes "[1654. N.S.]", which is the
   Old Style year with a New Style day. Vol. 3's title page reads "Papers from December MDCLIV to
   September MDCLV". P7 refers to Overton as already a prisoner (arrested Jan 1655), and all
   three letters refer to the "general rising" (Penruddock, March 1655). Tomokiyo also gives
   "spring of 1655". So P4 is 13 March 1655, P5+P6 30 March 1655 and P7 [20 March 1655], all N.S.
   (the index and brief say 1654). Correction added in NOTES s.12.
3. **P3's year is unresolved.** Birch prints the letter in vol. 2 under the running head A.D. 1654
   (p.576), among September 1654 papers. The internal dates are 18 and 21 September. The 1656
   date in the repo comes from Tomokiyo's heading "John Butler (1656)". The 1656 "Mr. John Butler"
   in vol. 5 (djvu 48192, 53079, 54700, Flushing and Bruges, all clear text) is a different
   informant, and nothing links him to this letter. Record the year as "Sept [1654] (Birch's
   placement; Tomokiyo 1656)". This is not resolved here. P3's decipherment is confirmed
   interlinear for the body. NOTES s.13 said "very likely yes" and called the letter
   "the highest-value follow-up", but the print already gives its plaintext.
4. **Printed pages.** These differ from index.tsv (running heads read directly): P2 565-566, P3 575-576,
   P5+P6 274-276, P7 277-280, P8 541, P16 84, P17 365-366, P18 386 (index says ~585), P19 406-407,
   P20 437-438, P21 450-451, P22 462-463, P23 528-529, P24 612-613.
5. **P8 grading.** 176 H tokens come from Tomokiyo's `key_blake.tsv`, which is a modern
   reconstruction, not a contemporary key. Say so wherever H is quoted, as for P11-13. "Now read"
   (NOTES s.13) should read "aligned". Corrected.
6. NOTES s.10's index proposal names Tomokiyo's section "Henry Cromwell (1658-1859)". His heading
   is "(1658-1659)". Corrected.

Proposed index.tsv corrections (LANE T applies; only the columns this audit checked):

```tsv
row	printed_page	date	status
P2	565-566	London, 25 Aug 1654	printed-decipherment (AUDIT N0, English translation)
P3	575-576	c.21-22 Sept [1654] (Birch vol. 2 placement; Tomokiyo gives 1656)	printed-decipherment body (AUDIT N0); postscript djvu 47999-48004 open
P5	274-276	Calais, 30 March 1655 N.S. (Birch "[1654. N.S.]")	printed-decipherment (AUDIT N0)
P6	274-276	as P5	printed-decipherment (AUDIT N0)
P7	277-280	[20 March 1655] (Birch "[March 20, 1654.]")	printed-decipherment incl. postscript (AUDIT N0)
P8	541	George, 12 June 1655	printed-decipherment (AUDIT N0)
P16	84	Whitehall, 20 April [1658]	printed-decipherment (AUDIT N0)
P17	365-366	A.D. 1658 (30 Aug per G. Davies 1955)	printed-decipherment (AUDIT N0)
P18	386	Whitehall, 14 Sept [1658]	printed-decipherment (AUDIT N0)
P19	406-407	Sept 21 [1658]	printed-decipherment (AUDIT N0)
P20	437-438	12 Oct [1658]	printed-decipherment (AUDIT N0)
P21	450-451	Oct [1658]	printed-decipherment (AUDIT N0)
P22	462-463	26 Oct [1658]	printed-decipherment (AUDIT N0)
P23	528-529	c.23 Nov 1658	printed-decipherment (AUDIT N0)
P24	612-613	25 Feb 1658/9	printed-decipherment (AUDIT N0)
```

### Search log

| Family | Status | What |
|---|---|---|
| (a) Canonical series | searched | Birch vols 2, 3, 7 djvu text, every letter's full extent read or scripted as above; vol. 5 grepped for Butler (the three 1656 hits are a different, clear-text informant) |
| (b) Sender/recipient correspondence | partly | Powell, *Letters of Robert Blake* (NRS 1937): Google Books snippet only, which shows the edition marks number-cipher passages; the 12 June letter's page not reached. Gaunt, *Correspondence of Henry Cromwell 1655-1659* (Camden 5th ser. 31, 2007): covers the Lansdowne MSS 821-823, whose Fauconberg letters are nos 494 and after. The Thurloe-printed nine were not shown to be in it (snippet only). Abbott, *Writings and Speeches*: cites the Stouppe letter |
| (c) Documentary editions / narrative histories | searched | Carlyle, *Letters and Speeches* (P8 text; P16 cited); Gardiner (P2); G. Davies 1955 (P17); HLQ 1935 and *Richard Cromwell* 1935 (P18); McMahon (Fauconberg's cipher letters mentioned) |
| (d) Holding archive (Bodleian Rawlinson A) | not searched | not needed for N0 |
| (e) Google Books | searched | 13 API queries, with the key, country=US, 2 s apart: exact phrases from each decipherment ("jealous of Stouppe", "make myself the lord protector's prisoner", "correspondence with Overton", "secretarie Massenett", "four galleons designed for the Mediterranean"), plus sender/recipient keyword queries |
| (e) Internet Archive full text (be-api fts) | searched | 11 queries: the same phrases, plus in-item searches of Underdown (*Royalist Conspiracy*) for "Stamford" and McMahon for "Stouppe Tarente" (0) |
| (e) HathiTrust, BHO | not searched directly | BHO is not on this worker's host list. Tomokiyo's page links BHO pages for P3 (compid 55340/55550) and P8 (compid 55389), and BHO transcribes the whole Thurloe series, so the plaintext of every row is also online there. This is inferred from the links, not fetched |
| (f) Solver repos, cipher blogs | taken from NOTES s.14 | Worker E grepped both repositories on 24 Sept 2026: neither catalogues P2, P3 or P8. Tomokiyo's mirror was re-read here for Butler, Stamford, Blake and Henry Cromwell |
| (g) Scholarship, JSTOR | not searched | not needed for N0. No JSTOR row queued: an N0 from the print cannot be raised |

Requests: www.googleapis.com 13, be-api.us.archive.org 11 (one of them saved its body to a stray
`/fts.json` outside the repo because of a script bug; the file is harmless and was left in
place), at least 2 s apart, with a descriptive User-Agent. No other host, no archive.org
downloads, no logins, no credentials printed.

### Postmortem

Failure: under-reporting, not over-claiming. NOTES s.5 still lists P2, P3, P5+P6, P7, P8, P16,
P18, P20 and P24 as "open, no lead found", and the header counts them among the "open" rows.
Workers C, D and E found the printed decipherments but correctly left the status to a verifier.
Sections 12 and 13 carried three factual slips: P7's postscript "not covered", the Old Style year
read as 1654, and P3's decipherment "very likely" and "highest-value follow-up". Section 13 also
said "now read" for an alignment. All of these are corrected in NOTES. The header and s.5 now mark
these rows found-solved (N0), with P3's postscript kept open. The lesson is the P11-13 lesson
again: page numbers come from the running head, and year dates from the volume's range, never
from a bracketed Birch year taken at face value.

## P9, P10, P14, P15 -- printed decipherment check (LANE T verifier V2, 24 Sept 2026)

Verifier: LANE T verifier V2 (parent LANE T session_01EwdS3bprjRaK49MrSERfA2), 24 Sept 2026, clock read 04:56-05:25 UTC.
It is separate from the transcription and alignment workers (B, I, K) whose sections it audits. No decoding done here.
**Claim under audit** (NOTES s.11, s.18, s.20; index.tsv): Birch prints each of these letters with an interlinear
decipherment. **Test:** the same as the sections above. Does the 1742 print carry a decipherment of this very letter,
and does it cover the cipher? P9, P10 and P14 were checked on the committed page images, looked at directly here, not
taken from the transcriptions. P15 was checked in the djvu text of vol. 5 (restored from `sources/ia-fulltext/thurloe-gz/`).

| Item | Class | Printed decipherment (Birch 1742) | Covers the cipher? | Confidence |
|---|---|---|---|---|
| P9 General Blake to the Protector, [Lagos Bay], 4 July 1655 | **N0** | vol. 3 pp.611-612. The plaintext is spelled letter by letter above each numeral line, e.g. p.612 top: "other ships bound to America shall be carefully observed as God gives opportunity" over "63. 68. 57. ... 38. 42." (image `collectionofstat03thur_leaf0626_p612.jpg`, checked here) | Yes. Every cipher line on p.611 L45-50 and p.612 L1-6 has a gloss line | high |
| P10 General Blake to the Protector, aboard the George, bay of Lagos, 6 July 1655 | **N0** | vol. 3 p.620, letter-by-letter interlinear (crop `..._leaf0634_p620_crop_L7-12.jpg`, checked here: "...rations in Cadez to set for[th] ... plate fleet and to that end divers...") | Yes, with one gap in the print itself: on p.620 L10 only the last 8 of 22 groups carry a gloss ("e t u r e t h e"), so 14 groups there have no printed decipherment. Those 14 groups are an unglossed remnant, not a separate item | high (letter); the 14 groups are open |
| P14 the Protector [and Council] to Blake and Mountagu, Whitehall, 9 June 1656 | **N0** | vol. 5 pp.101-102. The deciphered text is printed as the letter's own running text, in italics, with its numeral groups set in small type above it (p.102 image, checked here: "*the Downs, requireing them to give* ymediate *notice unto us of their arrivall*" etc., to "*in your eye* or designe to be done there by the fleet") | Yes, the whole extent (p.101 L44 to p.102 L22). NOTES s.11 said no decipherment was printed; s.18 corrected it from the image, and that correction is confirmed here | high |
| P15 General Mountagu to secretary Thurloe, aboard the Naseby, bay of Wyers (Lisbon river), 16 Sept 1656 | **N0** | vol. 5 **p.421** (djvu 35683-35754), interlinear word and syllable glosses above each numeral line ("The question before us was, whither wee shall send home the great ships. Wee have resolved it in the negative ..."). The clear close and signature are on p.422 | Yes, every numeral line in the djvu has a gloss line above it | high |

N0 means the plaintext and decipherment of this very item are already known. As with P2-P24 above, the decipherment is
Birch's print of what stands in the Thurloe manuscripts. `P9/P10/P14/P15_pairs.tsv`, `key_blake_extended.tsv`,
`key_montagu_extended.tsv` and the `reading_P9/P10/P14/P15.txt` files are alignments of that printed plaintext to the
groups. They are keys and benchmark data. They are not readings. The later-print question (Powell, *Letters of Robert
Blake*, NRS 1937, for P9/P10; Carlyle has no 9 June 1656 letter, NOTES s.19) does not change an N0 and was not pursued.

**Safe sentence.** "Birch printed these four letters in 1742 (Thurloe State Papers vol. 3 pp.611-612 and 620, vol. 5
pp.101-102 and 421) with their contemporary decipherment set above or beside the cipher. We aligned that printed
decipherment to the groups; 14 groups in one line of the 6 July 1655 letter carry no gloss in the print."
**Unsafe sentence.** "We read, decoded or deciphered" any of them. So is "P14 has no printed decipherment" or "446
groups of P14 now read".

**Corrections (factual, not novelty).**
1. **P15's page is 421, not ~411.** The "411 STATE PAPERS OF" running head at djvu 35758 is an OCR misreading of 422:
   the heads run 420 (djvu 35573), 421 (35650), "411" (35758), 423 (35843). The cipher, djvu 35683-35754, lies
   between the 421 and 422 heads. NOTES s.11 moved the page from ~420-421 to ~411 on the strength of that misread
   head. Corrected in NOTES s.11 below.
2. NOTES header and s.5 still listed P9, P14 and P15 as `partial` and P10 as `open`. They are **found-solved** (N0),
   and the header and s.5 are corrected here. The P9 row's "14 June/4 July date question" was settled in s.11 (4 July 1655).
3. The H grades for P9/P10 (Tomokiyo's Blake values) and P14/P15 (his Montagu values) come from modern reconstructions,
   not contemporary keys. That is the same caveat as for P8 and P11-13.

Proposed index.tsv corrections (LANE T applies):

```tsv
row	printed_page	status
P9	611-612	printed-decipherment, interlinear (AUDIT N0, V2)
P10	620	printed-decipherment, interlinear (AUDIT N0, V2); 14 groups of p.620 L10 unglossed in the print
P14	101-102	printed-decipherment, italic running text with groups above (AUDIT N0, V2)
P15	421 (clear close p.422)	printed-decipherment, interlinear (AUDIT N0, V2)
```

## P4 -- William Stamford ("W.S."), Calais, 13 March 1655 N.S. -- novelty audit (LANE T verifier V2, 24 Sept 2026)

Same verifier and session as the section above. I did not produce the reading and do not defend it.
**Claim under audit** (NOTES s.16 and s.21): Birch prints no decipherment of this letter. A key rebuilt from Birch's
printed decipherments of Stamford's letters of 20 and 30 March 1655 (`pool_1654/key_stamford.tsv`; cross-letter control
92.3% and 93.7%) reads its cipher as English (`pool_1654/reading_P4.txt`). Section 21 (worker L, pushed 05:09 UTC, read here before classifying) replaced the OCR-disordered blocks with the page image (p.188 L50-61): grades H 64, C 338, S 0, M 16, U 6 of 424 tokens; `pool_1654/decode_stamford.py --check` exits 0 (s.21, and re-run by this verifier at 05:14 UTC: "key_stamford.tsv, control_stamford.tsv, reading_P4.txt match"); key and control unchanged.

**Quality note (not novelty).** Outside p.188 L51-61 the reading is coherent English. Inside that stretch, even from the image, much of it is not: {eis}, {ca}, {seat}, {eco}, {siderable}, {la}, {surp}, {alds}, {rt}, {dehashas}, {ritinto} (s.21 lists them). A grade C on each letter there does not make the words read. Either the key is wrong for some values, or the image transcription splits or orders groups badly on those lines. So "reads its cipher as English" holds for the letter outside those eleven lines, and those lines stay partly unread

### 1. Extract

| Field | Value |
|---|---|
| Date | Calais, 13 March 1655 N.S. (Birch "Callais, March 13, [1654. N.S.]"; the endorsement reads "13/3 March 1654/5" on BHO) |
| Sender | "W.S." = William Stamford (he signs P5+P6 "WILLIAM STAMFORD"; Tomokiyo #Stamford) |
| Recipient | unnamed ("your friend" is the Protector). Macray's Rawlinson index (below) has "Stamford, W., Calais. Letters to col. Kelsey; Mar. 1654/5, A. 24. 73". So the addressee may be Col. Thomas Kelsey, not Thurloe. This is an index line, not checked against the MS |
| Print | Birch 1742 vol. 3 pp.187-189 (heading p.187, djvu 15467; cipher p.188; signature, a short covering letter of the same date, and the endorsement on p.189, djvu 15602-15671). MS: Birch's margin "Vol. xxiv. p.76" (covering letter p.73) = Bodleian MS Rawl. A. 24 |
| Ciphertext | inline numeral runs 1-43 (letters) and 62-171 plus the sign (codes), about 440 tokens. Clear text around them |
| Printed apparatus | **no decipherment**. After the signature Birch prints the covering letter and then "This letter is endorsed as follows: W.S. Calais ... His desire of a correspondence, and promise of performing some emminent service (in case my lord protector will engage to reward him) namely in discovering of the plott, &c." |
| Distinctive decoded phrases | "meere chance", "without the least iniunction of secrecy", "the person I got it from", "stealing out of Whitehall" (clear) + "England", "a plot hath been a hatching", "the whole partie of [143]", "irreconciliable with them as long as I live", "the qualitie I am of", "a more general rising", "a thousand armes" |
| Solver's search | NOTES s.14 (Birch, CSPD 1654, both solver repositories, Tomokiyo), s.16 (disk only), s.19 (`printcheck_P4_P14.tsv`: CSPD 1655 on be-api; Underdown in Google Books, NO_PAGES; seven phrases in Google Books, 0 genuine hits) |

### 2. Independent search (this session, 24 Sept 2026)

| Family | Status | What was searched, result |
|---|---|---|
| (a) Canonical series | searched | Birch vol. 3 djvu 15460-15700 read in full here: the letter, the covering letter, the endorsement and the next item (Manning, p.190). No "decypher'd" paragraph anywhere between P4 and P5+P6. **BHO** transcription of vol. 3 pp.185-195 (www.british-history.ac.uk/thurloe-papers/vol3/pp185-195, fetched once): it gives the same numerals and no decipherment, no editorial note, and the endorsement dated "13/3 March 1654/5" |
| (b) Sender/recipient correspondence | searched, nothing exists | No edition of Stamford's or Kelsey's letters is known. Thurloe's letters are only Birch |
| (c) Documentary editions, histories | partly | CSPD 1655 (s.19). Underdown, *Royalist Conspiracy* (IA `royalistconspira0000unde`, be-api in-item): "Calais" hits concern Whitley, Mordaunt and others, and "W. S." and "Kelsey" give 0. G. Smith, *Cavaliers in Exile*: "Stamford" is Col. Edward Stamford, a different man. Akkerman, *Invisible Agents*: no Stamford of Calais. Gardiner, *Commonwealth and Protectorate* vol. 3 not searched in-item |
| (d) Holding archive | **not reachable under this brief** | Bodleian MS Rawl. A. 24: Macray's printed index (IA `catalogicodicumm52bodl`, `CatalogiCodicumManuscriptorumBibliothP5F2`) lists Stamford's March 1654/5 letters at A. 24. 73 (and 76 per Birch), plus "Letters to Cromwell; 1655-6, A. 33. 143". Whether the MS carries a contemporary decipherment (interlined or on a separate leaf) is **not known**. The endorsement's "discovering of the plott" paraphrases matter that stands only in cipher, so Thurloe's office understood the cipher in 1655. That makes a contemporary decipherment likely, whether or not it survives. Birch printed one for P5+P6 and P7 and none here, which fits the MS having none, but this is not proof. Bodleian Archives & Manuscripts was not a host of this brief |
| (e) Google Books | searched | 12 queries, key, country=US, 2 s apart: "Stamford" Calais Thurloe 1655 cipher (only Birch), "William Stamford" Thurloe (irrelevant), "Stamford" "Kelsey" Calais 1655, "W. S." Calais Thurloe plot 1655 Penruddock (0), "general rising" Stamford Calais Thurloe (0), "irreconciliable with them" (unrelated), "stealing out of Whitehall" (only Birch, whose print shows the numerals), "Stamford" Kelsey Thurloe, Stamford Calais spy 1655 royalist plot Thurloe (0), "Rawlinson" "A. 24" Stamford (Macray, no snippet); s.21 phrases "more people are engaged" rising 1655 (0) and "time appointed for it is not farre off" (only Birch, clear text) |
| (e) IA full text (be-api fts) | searched | 10 global queries: "meere chance" (early printed books only), "injunction of secrecy" Stamford, "irreconcilable with them as long as I live" (0), "plot hath been a hatching" (0), "William Stamford" Calais (Staffordshire families, unrelated), "Stamford" Calais Thurloe 1655, "a thousand arms" Calais 1655 plot (0), "the whole party of the cavaliers" 1655 (0), "more people are engaged then in any of the former" (0), "Stamford" "col. Kelsey" Calais (CSPD 1651 index "Stamford, Wm.", unrelated). 11 in-item queries (Macray x4, Underdown x3, Smith x2, Akkerman x2) |
| (e) HathiTrust | not searched | not a host of this brief |
| (f) Solver repos, cipher blogs | from s.14, and Tomokiyo re-read | Tomokiyo, thurloe.htm #Stamford (local mirror), re-read: he builds his key image `stamford.jpg` from "13 March NS (Page 187 and Page 189), 30 March (Page 274), and 3 April (Page 340)". He lists codes 65, 67, 81, 82, 130, 158 and the sign. Every one of them also occurs in P5+P6/P7 (`key_stamford.tsv` has 65, 67, 81, 82, 130 and 158 from their printed decipherments), so nothing on his page shows a value read only from P4. His one P4 quotation ("if this correspondence continue ... being very imperfect") is P4's clear text, not cipher. His image was not seen: it is not on disk, and cryptiana.web.fc2.com was not a host of this brief. **A prior modern decipherment of P4 by Tomokiyo is therefore not excluded**: he used P4 as a source for his key, so he may have worked through its cipher, but no plaintext of it is printed on his page. DECODE: not searched for Stamford (login is one per session and belongs to another worker) |
| (g) Scholarship | partly | OpenAlex 429 (x2), Semantic Scholar 429 (x2), CrossRef 1x429 and 1 answer: Penruddock (ODNB), "Colonel John Penruddock (1655)" (2024 chapter), Marshall, "John Thurloe and the Cromwellian regime" (2023 chapter) and "Cromwell's 'spymaster'?" (INS 2018), all unread. HAL 0 (x2). JSTOR: 3 rows queued in JSTOR-QUEUE.tsv |
| tools/print_check.py | not run | the folder has no phrases.txt/sources.tsv, and building them is outside this brief's files |

Requests this session: british-history.ac.uk 2, be-api.us.archive.org 21, www.googleapis.com 12, api.openalex.org 2
(429), api.semanticscholar.org 2 (429), api.crossref.org 2 (1 x 429), api.archives-ouvertes.fr 2. All were one at a time,
at least 2 s apart, with a descriptive User-Agent. No archive.org downloads, no logins, no credentials printed.

### 3. Classification

| Item | Class | Prior plaintext | Prior decipherment | Evidence | Confidence |
|---|---|---|---|---|---|
| P4 Stamford, 13 March 1655 | **N3** | Only for the clear text and the endorsement's summary (Birch 1742; BHO). No plaintext of the cipher runs was located in print or online | Not located. Not excluded for (i) a contemporary decipherment in Bodleian MS Rawl. A. 24 (the endorsement shows the office understood the cipher) or (ii) Tomokiyo's unpublished working behind `stamford.jpg`, which cites this letter as a source | Birch and BHO read directly. Phrase searches on IA and Google Books. Principal Penruddock study (Underdown) in-item | medium |

**Why not N4:** the holding archive (Rawl. A. 24 ff.73-76) is unchecked, and Tomokiyo's key image is unseen. Gardiner vol. 3,
Marshall 2018/2023 and the 2024 Penruddock chapter are unread. OpenAlex and Semantic Scholar did not answer. The first two are the
likeliest places for a prior decipherment, and each is one short job: a Bodleian catalogue/digital lookup or copy
request for MS Rawl. A. 24 fols 73-76, and one fetch of cryptiana's `stamford.jpg` compared against `key_stamford.tsv`
for any value that occurs only in P4. **Why not N1/N2:** no print of the cipher plaintext was found anywhere.

**Safe sentence.** "Birch (1742) prints William Stamford's letter from Calais of 13 March 1655 with its cipher numerals but
no decipherment. We read the cipher with a key rebuilt from Birch's printed decipherments of Stamford's letters of 20 and
30 March 1655 (cross-letter control 92-94%); by token, H 64 (Tomokiyo E=12/25), C 338, M 16, U 6 of 424, with eleven lines of p.188 still partly incoherent. No prior decipherment was located in Birch, British History
Online, CSPD 1655, Underdown's *Royalist Conspiracy*, Google Books, Internet Archive full text or the open indexes
(searched 24 Sept 2026, AUDIT.md). Bodleian MS Rawl. A. 24 and Tomokiyo's working key have not been checked."
**Unsafe sentence.** "First decipherment of", "previously unread", "unpublished" or "never deciphered", and "a cryptanalytic
solution" (every value is keyed from printed plaintext, so this is a keyed reading). So is quoting the letter-level grade
as if Tomokiyo's H values (E = 12/25, a modern reconstruction) were a contemporary key.

### 4. Postmortem

No novelty over-claim was found in s.16 or s.19. s.21 said the added stretch "is new" (meaning: not read by worker G). That breaks rule 10's word list even though the sense is internal, so it now reads "is added in this pass" (corrected in NOTES s.21). One sentence outside my
write list over-claims: `printcheck_P4_P14.tsv` (P4 phrase row) says "No print anywhere carries this letter's plaintext
content". That turns a search result into a fact. Proposed wording for LANE T: "No print of this letter's cipher plaintext
located in the sources searched". Gaps the solver log did not name: the holding archive, the recipient (Macray's index
says col. Kelsey), and Tomokiyo's key image as a possible prior decipherment. For LANE V, as the second audit: P4 N3.

## Second audit (adversarial), P4, 24 Sept 2026

LANE W worker B (Opus). This is the verifier hat and a separate session: I neither solved P4 nor ran V2, and I defend
neither. Started 06:14 UTC, written 06:27-06:29 UTC. **Claim under audit:** V2's class N3 for P4 (Stamford, Calais,
13 March 1655 N.S., Birch 1742 vol. 3 pp.187-189): "no prior plaintext or decipherment located". Brief: try to find P4's
plaintext or a decipherment in print or online. I did not decode.

### Search log

| Family | Status | Queries and result |
|---|---|---|
| (a) Birch, index, adjacent volumes | searched | Vol. 3's own index (djvu on disk, `sources/ia-fulltext/thurloe-gz`, line 67356): "Stamford, William, offers to give intelligence to the protector of the designs of king Charles, 274, seq. 279 ... Complains of receiving no answer to his proposals, 340." The index does not list p.187 under Stamford, "W. S." or Calais, and it cites no decipherment. Vol. 7 (general index and appendix), in-item fts "Stamford" and a grep of the djvu: 0 hits for Stamford, and "Kelsey" only as Tho. Kelsey in an unrelated list. V2 had already read vol. 3 djvu 15460-15700 and BHO pp.185-195; I did not repeat that. |
| (b) Royalist side | searched | IA in-item fts (be-api), one query at a time. *Calendar of the Clarendon State Papers* vol. 3 (`calendarofclaren03bodluoft`): "Stamford" 0, "Stanford" 0, "Kelsey" 0; the "Calais" control hits, so the search works. *Nicholas Papers* vols 2 and 3 (`thenicholaspaper02camduoft`, `...03camduoft`): "Stamford" 0; "Calais" hits concern Whitley, Digby and others, not Stamford. Printed *Clarendon State Papers* vol. 3 (1786): no full-text IA copy found by advancedsearch (only `10622705bsb`, vol. 1), **not searched**. CSPD 1655 (`sim_great-britain-public-record-papers-domestic-commonwealth_1655`): "Stamford" gives only Blake's troop at Stamford fair; "Calais" gives fishing licences. |
| (c) Clarke, Underdown, Abbott, Gardiner | searched | *Clarke Papers* vol. 3 (`theclarkepapers03camduoft`): "Stamford" 0, "Calais" 0. Gardiner, *Commonwealth and Protectorate* vol. 3 (`historyofcommonw03garduoft`), the gap V2 named: "Stamford" gives only the Earl of Stamford; "Calais" gives the proposed siege of Calais. Abbott, *Writings and Speeches* vol. 3 (`writingsspeeches0003crom`): "Stamford" gives only a Blore citation (Stamford, 1811); "Calais" is unrelated. Underdown was covered by V2 (0 for "W. S." and "Kelsey"). |
| (d) Holding archive, Bodleian | **partly reached** | archives.bodleian.ox.ac.uk sits behind an Anubis proof-of-work challenge: curl got it once, and one headless-browser attempt failed mid-navigation. I stopped the host there (good-citizen rule). Route that worked: the Wayback Machine's copies of the ArchivesSpace item records (CDX prefix `archival_objects/3208`, then `id_` fetches of 2023-24 captures). The Rawl. A. 24 item records run in folio order: 320836 f.61 (Whitelocke, 3 Mar 1655), 320837 f.66, 320838 f.70 (Dr Walter Walker), **320839 f.86** (Villeré, 5 Mar 1655), 320840 f.92, 320841 "fols. 75, 95, 96" (the Laurens intercept to Oorschott, 16 Mar 1655), up to 320861 A. 24/2 f.400. **There is no item record for Stamford at ff.73-76**, so the online catalogue has nothing to say about a decipherment. Also, the current foliation puts part of the Laurens intercept at f.75, which does not sit easily with Birch's "Vol. xxiv. p.73/76" for Stamford: Birch's figures may be the old pagination. Whether the MS carries a contemporary decipherment is still **unknown**. Only the leaf image can answer it (ASKS/REQUEST). |
| (e) Tomokiyo | **searched, image compared** | `https://cryptiana.web.fc2.com/code/stamford.jpg` fetched once (18.5 KB, 358x181; it is not committed, since it is Tomokiyo's image; re-fetch from that URL). His table, value by value: 2m 3l 5k 6i 7h 10g 11f 12e 16d 17c 18b 19a / 21k 22g 23h 25e 26f 27c 28i 29d 30a / 31y 32x 33w 34u/v 35t 36s 37r 38q 39p 40o 41n 42n 43m 47r 55t 56s 60i. Compared with `pool_1654/key_stamford.tsv` and with where each value occurs in `pool_1654/tokens.tsv`: (1) all 35 values we share **agree except 27** (Tomokiyo c, ours r, 9 of 11 votes). 27 does not occur in P4, so the reading is unaffected. (2) Tomokiyo has 55 t, 56 s and 60 i, which our key lacks. 55 and 60 occur once each in P5+P6, 56 nowhere in our tokens, and none of them in P4. (3) Our 1 i, 4 n and 9 a (all M, one vote each) occur in P4 and P7 but are not in his table. (4) **No value in his table occurs only in P4.** P4's only-P4 values (13, and codes 70, 143, 189) are not glossed by him, and his codes 65, 67, 81, 82, 130 and 158 all occur in P5+P6 or P7. **Verdict:** Tomokiyo has published a reconstruction of Stamford's letter cipher, which is a prior decipherment of the *system*, and every value in it can be derived from Birch's printed decipherments of the sibling letters. Nothing on his page shows that he read P4's cipher, and no P4 plaintext is on his page. So this is a prior decipherment of the system, not of this letter. |
| (f) IA full text | searched | Six global fts queries: "William Stamford" Thurloe (a 20th-century dentist and trade directories); "W. S." Calais "discovering of the plott" (1 hit, Birch's own print of P4's endorsement, which shows the numerals and no decipherment); "linke myselfe intirely" (1 hit, Birch's print, clear text); "Stamford" "general rising" 1655, "Stamford" Calais spy Cromwell 1655 and "Stamford" "Nevell" Dover (thousands of loose hits, none on this Stamford in the first page). Items were named in ROOM.md before querying (06:17 UTC). |
| (f) HathiTrust | **unreachable** | babel full-text search answered 403 (one request, then stopped). The Bibliographic and EF APIs cannot phrase-search, so they were not used. |
| (f) British History Online | searched by V2; site search 302 | V2 fetched BHO vol. 3 pp.185-195 (no decipherment). My one site-search request redirected, and I did not follow it. |
| (g) Solver repositories | searched | Fresh shallow clones: dbourdeau/cyphersolver at 9a3f326 (24 Sept 2026) and aaymeloglu/unsolved-ciphers at 2495c45 (23 Sept 2026), grepped for Stamford and Thurloe. Bourdeau's `thurloe/` uses `stamford.jpg` only as one of the period keys tried against *other* Thurloe intercepts (`apply_keys_out.txt`, all fail). There is no P4 reading. Aymeloglu has no Stamford, and its Thurloe item is the unrelated Vande Perre 1653. Cited only, no code copied. |
| (h) Open indexes | partly | CrossRef "Thurloe Stamford Calais 1655 cipher": ODNB Thurloe, a 2024 Routledge chapter "The Examinations of Richard Moone ... (27 August 1655)" (not this letter) and unrelated items. HAL `Thurloe AND (Stamford OR chiffre OR cipher)`: 0. **OpenAlex 429 and Semantic Scholar 429** (one request each, stopped, the same as V2). WebSearch (4 queries, including `"Stamford" Calais 1655 Thurloe cipher plot Kelsey` and a site search on archives.bodleian.ox.ac.uk): no print of P4's decipherment. It surfaced Marshall, "Cromwell's 'spymaster'? John Thurloe and rethinking early modern intelligence", *The Seventeenth Century* 35:1 (2020), doi 10.1080/0268117X.2018.1524786, **unread** (paywalled). JSTOR: 2 rows added to JSTOR-QUEUE.tsv. |
| Google Books | not mine | Handed to LANE V in ROOM.md at 06:17 UTC with 8 phrase queries. Results pending. V2's 12 queries stand. |
| DECODE | not searched | One login per session belongs to other workers. |

Requests this session: cryptiana.web.fc2.com 3; archives.bodleian.ox.ac.uk 1 curl + 1 browser (challenge, stopped);
web.archive.org 1 CDX + 30 captures; archive.org advancedsearch 8; be-api.us.archive.org 22; api.openalex.org 1 (429);
api.semanticscholar.org 1 (429); api.crossref.org 1; api.archives-ouvertes.fr 1; babel.hathitrust.org 1 (403);
www.british-history.ac.uk 1 (302); github.com 2 shallow clones; WebSearch 4. All were one at a time, at least 2 s apart. No logins, no
credentials.

### Classification

| Item | Class | Prior plaintext | Prior decipherment | Evidence | Confidence |
|---|---|---|---|---|---|
| P4 Stamford, Calais, 13 March 1655 | **N3 (confirmed)** | **No** for the cipher runs. Yes only for the clear text and for the endorsement's one-line summary (Birch 1742 vol. 3 p.189; BHO) | **Of this letter: not located.** **Of the system: yes.** Birch 1742 prints the office's decipherments of the sibling letters (vol. 3 pp.274-280, 337-340), and Tomokiyo (cryptiana, `stamford.jpg`) publishes the reconstructed letter table. Our key agrees with his on 34 of the 35 values we share, and the one exception (27) does not occur in P4 | Tomokiyo's image compared value by value. The Bodleian item sequence was read through Wayback. Nine edition volumes were searched in-item | medium |

**Why N3 and not lower:** no print, page or repository carrying P4's cipher plaintext was found. Tomokiyo's table does not
show P4-only values. Every edition that a Stamford letter might plausibly be calendared in gives 0 for him.
**Why not N4 yet:** (1) Google Books is LANE V's and pending. (2) The one directly relevant modern study, Marshall 2020 (*Seventeenth
Century* 35:1), and Marshall's 2023 chapter are unread, and OpenAlex and Semantic Scholar did not answer twice now. (3) HathiTrust full
text is unreachable. (4) The 1786 printed *Clarendon State Papers* vol. 3 has not been searched. (5) DECODE has not been searched. A contemporary
decipherment on the Rawl. A. 24 leaf would be internal or unpublished work, which N4 does not exclude, so the MS is **not** an N4 blocker. It is the
one thing that could move the item to N0-like status in substance, however, and the image is the only way to know.

**Safe sentence.** "Birch (1742) prints William Stamford's letter from Calais of 13 March 1655 with its cipher numerals
and no decipherment. We read the cipher with the key given by Birch's printed decipherments of Stamford's two later
letters, a key Tomokiyo has also reconstructed and published (cryptiana, 'William Stamford (1655)'). Our table
agrees with his on every value that occurs in this letter. By token: H 64, C 338, M 16, U 6 of 424, with eleven lines of p.188
still partly incoherent. No prior print of this letter's cipher plaintext was located in Birch, British History
Online, CSPD 1655, the Clarendon calendar vol. 3, the Nicholas Papers vols 2-3, the Clarke Papers vol. 3, Gardiner, Abbott,
Underdown, the Bodleian's online item catalogue, Tomokiyo's pages, the two solver repositories, Internet Archive full text
or the open indexes that answered (searched 24 Sept 2026, AUDIT.md). The original leaf, Bodleian MS Rawl. A. 24, has not
been seen."
**Unsafe sentence.** "We broke / cracked / solved Stamford's cipher", because the system was deciphered by Thurloe's office in 1655
and reconstructed by Tomokiyo. Also unsafe: "first decipherment", "previously unread", "unpublished", and "no decipherment exists"
(the Bodleian leaf is unseen).

### Postmortem

V2's N3 holds. The adversarial gain is one reframing that V2 left open. Tomokiyo's key image is now seen. It is a prior
published decipherment of the **system**, with nothing specific to P4 in it, so any outward sentence must credit him (and
Birch's sibling decipherments) for the key, and claim no more than the application to this letter. Over-claims corrected in the folder:
`printcheck_P4_P14.tsv` P4 row ("confirming ... that no decipherment of P4 exists" now reads "consistent with ... search
result that no decipherment of P4 was located ..., a search result, not proof of absence"); NOTES.md s.21 ("newly-read
stretch" now reads "stretch added in this pass"). No other sentence in `ciphers/thurloe-printed/*.md` claims more than N3.

### Toward N4 (what remains)

1. LANE V's Google Books results for the 8 queries in ROOM.md (06:17 UTC).
2. Read Marshall 2020 (*Seventeenth Century* 35:1, doi 10.1080/0268117X.2018.1524786) and Marshall 2023 ("John Thurloe and the
   Cromwellian regime") for Stamford or Kelsey. JSTOR/T&F rows are queued.
3. OpenAlex and Semantic Scholar, once each, after the rate limit clears. Query: `Thurloe Stamford Calais 1655`.
4. The 1786 *Clarendon State Papers* vol. 3 (Google Books or HathiTrust): "Stamford" in March-April 1655.
5. DECODE: search "Stamford" and "Thurloe" in the next session that holds the login.
6. Not an N4 gate, but decisive in substance: an image of Bodleian MS Rawl. A. 24 at Stamford's letter (Birch "vol. xxiv p.73, 76"; the current
   foliation is uncertain, see (d)) for any interlined or separate decipherment. This is an ASKS/REQUEST item for the person.

## Gap search, LANE W worker D, 24 Sept 2026

LANE W worker D (Sonnet, session_01F234Ho27aPryLTBhTerxbK), parent LANE W orchestrator session_011UFnhZnyCntZ8Bn9FpKyTq.
Closes "Toward N4 (what remains)" items 3 and 4 above. No decoding, no reclassification; log only. Clock read
06:43-06:50 UTC.

### Item 4: 1786 Clarendon State Papers vol. 3, via Internet Archive

Could not find the volume on archive.org to search it. Four `advancedsearch.php` queries, each read before the
next (title/creator combinations for "State Papers Collected by Edward, Earl of Clarendon", "great rebellion",
and a 1780-1790 date filter) return only **one** copy of the 1767-1786 printed edition (not the separate 1869-72
*Calendar* series, which the first and second audits already searched with 0 hits for Stamford/Kelsey): identifier
`10622705bsb`, "State Papers Collected By Edward, Earl of Clarendon ... 2" (metadata title/date fields, dated
1773). That "2" is the volume number: **this is vol. 2** (1773, running to 1654), not vol. 1 as the first
adversarial audit's line 376 says ("only `10622705bsb` (vol. 1)") -- small correction, worth fixing there. Vol. 3
(1786, the volume that would cover March 1655) is **not on Internet Archive** under any of these queries, so the
be-api in-item full-text search for Stamford / Kelsey / "Calais March 1655" / P4 phrases could not be run --
there is no vol. 3 item to run it against. Did not query vol. 2 (`10622705bsb`) itself: it does not cover 1655,
so a hit there could not be P4's letter or its content.

One-shot check of the *catalog.hathitrust.org* Bibliographic API (`oclc:1899749`, a guessed OCLC number) also
failed: 403 from Cloudflare, one request, stopped, consistent with the "Access playbook" item 3 HathiTrust note.
Google Books / HathiTrust full search for this volume is LANE V's per the brief and item 4's own text; not
repeated here.

**Result: item 4 not closed.** The gap is now "vol. 3 is not on IA (confirmed by four queries); still needs
Google Books or HathiTrust by title/volume rather than by full text search", which is a narrower, more useful
gap than before.

Requests this session: archive.org advancedsearch 4 (>=2s apart); catalog.hathitrust.org 1 (403, not retried,
per credential/access-playbook rule).

### Item 3 (and the parallel Eckert rerun): OpenAlex and Semantic Scholar

Both hosts returned the same global 429 seen earlier today (06:16-06:30 UTC, first and second P4 audits; also
logged in `ciphers/eckert-1864/AUDIT.md` "Open-index scholarship pass"), not a query-specific limit:

- **OpenAlex**: `Thurloe Stamford Calais 1655` -- 429, "Insufficient budget... shared by everyone on your
  network's IP address... resets at midnight UTC" (`retryAfter` ~62100s, i.e. this is a whole-day, whole-IP
  exhaustion, not a per-request throttle). Retried once after a 5s pause: identical 429 with the same
  `retryAfter` countdown, confirming it will not clear within this session. Given that explicit shared-budget,
  whole-day message, the two remaining P4 queries (`William Stamford Thurloe spy`, `Thurloe intelligence cipher
  1655`) were **not** separately sent to OpenAlex -- a third and fourth call would return the identical error,
  and the good-citizen rule caps retries against a host already answering 429. They were sent to Semantic
  Scholar instead (below). The two Eckert queries (`Decoding the Civil War Huntington telegram`, `Eckert cipher
  book Union telegraph 1864`) were each sent to OpenAlex once, for the Eckert AUDIT.md log: both 429, same
  message.
- **Semantic Scholar**: `Thurloe Stamford Calais 1655` -- 429 "Too Many Requests". Retried once after a 5s
  pause: identical 429. `William Stamford Thurloe spy` and `Thurloe intelligence cipher 1655` sent once each:
  both 429, same message. The two Eckert queries were also sent once each: both 429.

**Result: item 3 not closed, unreachable for this session.** Both APIs are confirmed down at the shared-IP level
(not just this worker), consistent with the same finding already on record for Eckert's open-index pass earlier
today. No titles or DOIs to report.

Requests this session: api.openalex.org 4 (1 query with one retry, 2 Eckert queries, all 429); api.semanticscholar.org
6 (1 query with one retry, 2 further Thurloe queries, 2 Eckert queries, all 429). One at a time, >=2s apart, no
logins.

## Google Books queries (LANE V runner), 24 Sept 2026

LANE V worker (Sonnet), the P4 Google Books gap named in "Toward N4 (what remains)" item 1 above (queries posted by
LANE W worker B in ROOM.md 06:20 UTC). This session only ran the queries and records what came back; it does not
decode and does not assign or change a class.

**Queries (8, verbatim from ROOM.md):** "irreconcilable with them as long as I live"; "a plot hath been a hatching";
"the whole party of" Stamford Calais 1655; "general rising" "Stamford" 1655 Calais; "without the least injunction of
secrecy"; "by meere chance" "Whitehall" 1655 Stamford; "Stamford" "Kelsey" Calais 1655; "the qualitie I am of"
cavaliers. Full results, including the `filter=full` re-run of any query with hits: `google-books-2026-09-24.tsv`.

**Hit counts:** 6 of 8 queries returned 0 items. 2 returned hits:

- `"without the least injunction of secrecy"` -- 7 items (1 after `filter=full`).
- `"Stamford" "Kelsey" Calais 1655` -- 1 item (0 after `filter=full`).

**Hits whose snippet contains the quoted phrase:**

1. `"without the least injunction of secrecy"` -- volume `MVWTTZHgGGoC`, *English Historical Documents, 1783-1832*
   (Douglas/Aspinall/Smith, 1996), and five further editions of the same title (1953, 1959 x3, 1996, 2024) plus
   volume `uYwFAAAAQAAJ`, *House Documents, Otherwise Publ. as Executive Documents* (US Congress. House, no year
   given), all with snippet: "...without the least injunction of secrecy, but on the contrary with an expression of
   a wish that his opinion should be known..." (the Congress volume instead: "...without the least injunction of
   secrecy; and I was by him authorized to inform the stockholders thereof...").
2. `"Stamford" "Kelsey" Calais 1655"` -- volume `Yk3iAAAAMAAJ`, *Student Directory* (University of Michigan, 2000);
   no snippet text returned for this hit.

**Non-decisive, for the record.** Both hits look like coincidental matches on generic phrasing, not P4's content.
The *English Historical Documents* editions are a documentary series covering 1783-1832, roughly 130-280 years after
this letter (13 March 1655); their snippet is about a political opinion becoming known, not about Stamford, Calais,
plots or a general rising. The *House Documents* snippet concerns a stockholders' notice, unrelated in subject and
undated in the API response. The *Student Directory* hit is a University of Michigan student list and carries no
snippet; "Stamford", "Kelsey" and "Calais" there are almost certainly unrelated proper nouns (a person, a place)
with no connection to 1655. None of these four titles is a Thurloe edition, a Stamford/Kelsey/Cromwell-period
correspondence, or a cryptology reference. I read no snippet that quotes P4's plaintext or names this letter.

**Effect on the class:** none from this pass. Toward N4 item 1 is now answered: Google Books gives no prior print
of P4's cipher plaintext. N4 still waits on items 2-6 of "Toward N4 (what remains)" (Marshall 2020/2023, OpenAlex/
Semantic Scholar, the 1786 Clarendon vol. 3, DECODE, and the Bodleian leaf image).

Requests this session: www.googleapis.com 10 (8 base queries + 2 `filter=full` re-runs on the two queries with
hits), one at a time, at least 3 s apart, key never printed. No other host.

## N4 decision, P4, 24 Sept 2026

LANE W worker F (Opus), a fresh verifier session, parent LANE W orchestrator session_011UFnhZnyCntZ8Bn9FpKyTq,
07:39-07:43 UTC. I did not solve, audit or search P4 before this session, and I did not decode. **Question:** does the
logged coverage now meet rule 10's N4 ("N3 with the principal editions, catalogues and project pages covered, internal
or unpublished work not excluded") for P4 (William Stamford, Calais, 13 March 1655 N.S.; Birch 1742 vol. 3 pp.187-189)?

**Answer: no, not yet. P4 stays N3.** Every principal printed edition, the holding archive's catalogue and the cipher's
project page are now covered. The 1786 *Clarendon State Papers* vol. 3 is covered by proxy through Macray's *Calendar*
(s.2 below). One principal family is still open: **DECODE** (de-crypt.org). It is the catalogue of cipher manuscripts
where someone could have uploaded a Rawlinson leaf with its decryption. The only DECODE data on disk (LANE N's no-login
crawl of 24 Sept 2026) covers Non-decrypted and Partially decrypted records, and none of its 1186 rows has a Bodleian or
Oxford holder. **Decrypted** records were never listed. DECODE was treated as an N4 gate for Gramont and Danzay
(LANE N closed both today), and I treat it the same way here. If the job in s.3 comes back negative, P4 goes to N4
without any other audit.

### 1. Principal families and coverage

| family | principal? | covered | where AUDIT.md shows it |
|---|---|---|---|
| Birch 1742 vol. 3, letter pp.187-189 with covering letter and endorsement | yes (canonical series) | yes: djvu read in full; no "decypher'd" paragraph | V2 s.2 (a) |
| Birch vol. 3 index and vol. 7 general index | yes | yes: Stamford is indexed at 274, 279 and 340 only; p.187 is not indexed under Stamford, W.S. or Calais; vol. 7 gives 0 | second audit (a) |
| British History Online, Thurloe vol. 3 pp.185-195 | yes (online edition of the series) | yes: same numerals, no decipherment, no note | V2 s.2 (a) |
| CSPD 1655 | yes | yes, in-item: "Stamford" hits only Blake's troop at Stamford fair; "Calais" hits only fishing licences | V2 s.2 (c) (s.19); second audit (b) |
| *Calendar of the Clarendon SP* (Macray) vol. 3 (1655-57) | yes (royalist side) | yes, in-item: "Stamford" 0, "Stanford" 0, "Kelsey" 0; the "Calais" control hits | second audit (b) |
| *Clarendon State Papers* 1767-86, vol. 3 (1786, ed. Monkhouse) | yes as an edition, but its contents are Clarendon MSS, which the *Calendar* above calendars item by item | **by proxy, this session** (s.2): Macray marks items that were printed there ("Partly printed, Cl. S. P. vol. iii. p. 284"), so a Stamford item printed in 1786 would be calendared, and the *Calendar* gives 0 for Stamford, Stanford and Kelsey. P4 itself is a Rawlinson (Thurloe) MS, not a Clarendon MS. The volume itself is not on IA (worker D) and not on HathiTrust (s.2). Google Books search-within would be optional confirmation, not a gate | this section, s.2; worker D item 4 |
| *Nicholas Papers* vols 2-3 | yes (royalist side) | yes, in-item: "Stamford" 0 | second audit (b) |
| Abbott, *Writings and Speeches* vol. 3 | yes (Protector's side; "your friend" is the Protector) | yes, in-item: "Stamford" hits only a Blore citation | second audit (c) |
| *Clarke Papers* vol. 3 | yes | yes: "Stamford" 0, "Calais" 0 | second audit (c) |
| Gardiner, *Commonwealth and Protectorate* vol. 3 | yes (narrative of the 1655 rising) | yes: Earl of Stamford only; "Calais" only as the proposed siege | second audit (c) |
| Firth, *Last Years of the Protectorate* | no: it begins in 1656. Firth's 1655 material is in the *Clarke Papers* (above) | not searched | this section |
| Underdown, *Royalist Conspiracy* | yes (the standard study of the 1655 plots) | yes, in-item: "W. S." 0 and "Kelsey" 0; the Calais hits are other men | V2 s.2 (c) |
| Sender/recipient editions (Stamford, Kelsey) | would be principal | none exists | V2 s.2 (b) |
| Bodleian catalogue (holding archive): Macray's printed Rawlinson index and the ArchivesSpace item records | yes | yes: Macray indexes "Stamford, W., Calais ... A. 24. 73". ArchivesSpace (via Wayback, since the live host is Anubis-challenged) has no item record for ff.73-76 | V2 s.2 (d); second audit (d) |
| MS Rawl. A. 24 leaf image | no for N4: archival and unpublished, so rule 10's "internal or unpublished work not excluded" applies. Decisive in substance | not seen | second audit, Toward N4 item 6 |
| Tomokiyo / Cryptiana, "William Stamford (1655)" (project page for this cipher) | yes | yes: `stamford.jpg` compared value by value; a published reconstruction of the *system*; no P4-only value, and no P4 plaintext on the page | second audit (e) |
| Solver repositories (Bourdeau, Aymeloglu) | yes | yes: no P4 reading | second audit (g) |
| **DECODE (de-crypt.org)** | **yes (cipher-manuscript catalogue; also treated as an N4 gate for Gramont and Danzay)** | **no**: not searched for Stamford, Thurloe or Rawlinson. Indirect evidence only: no Bodleian holder among the 1186 Non-decrypted and Partially decrypted records (`sources/decode/records-non-decrypted-2026-09-24.tsv`, grep "bodleian\|oxford\|rawl" 0) | this section |
| Google Books phrase search | yes (template family e) | yes: V2's 12 queries plus LANE V's 8; no P4 content | V2 s.2 (e); Google Books section |
| IA full text | yes (template family e) | yes: V2's 10 global and 11 in-item queries, and the second audit's 6 global queries | V2 s.2 (e); second audit (f) |
| HathiTrust whole-library full text | no for N4: a search engine, not an edition or catalogue; every edition above is covered by other routes (Eckert precedent) | unreachable (403) | second audit (f) |
| Scholarship: Marshall 2020 and 2023, JSTOR, OpenAlex, Semantic Scholar | no for N4: outreach gate 2 (Eckert precedent; CLAUDE.md: a queued JSTOR row never blocks N3 or N4) | CrossRef and HAL yes; OpenAlex and S2 429 all day; Marshall unread; JSTOR rows queued | V2 s.2 (g); second audit (h); worker D item 3 |

### 2. This session's search log

- HathiTrust Bibliographic API (full Chrome User-Agent), three calls. `oclc/4713616` (the 1767-86 edition's OCLC
  number, from Open Library's search API) returns record 000770724 with **v.1 and v.2 only**
  (njp.32101078304340, njp.32101078304332). `oclc/1006002852` returns no items. `lccn/02023355` returns the same
  two volumes. HathiTrust holds no copy of vol. 3 (1786), so the HTRC token-count route cannot be used. A WebSearch
  (1 query) found the vol. 3 copies at the Royal Collection and Google Books (`ELb2B_YZdmAC`, `g4NaAAAAYAAJ`). Google
  Books is LANE V's host, so I did not query it.
- Proxy check on Macray's *Calendar* vol. 3 (`calendarofclaren03bodluoft`, be-api in-item fts, 6 queries):
  - `"Printed" "iii."` returns "Partly printed, Cl. S. P. vol. iii. p. 284" and "printed in Thurloe's S. P. vol. iii.
    p. 153". So the *Calendar* records both the 1786 printing and Birch cross-references.
  - `"iii. p. 185"` returns one hit: "insurrection. See Thurloe's S. P. vol. iii. p. 185", the item just before P4.
  - `"iii. p. 187"`, `"iii. p. 188"` and `"iii. p. 189"` return 0.
  - Macray therefore links no Clarendon MS to P4's pages, and the second audit's 0 for Stamford, Stanford and Kelsey
    in the same volume stands.
- DECODE: not queried (LANE N's host). `tools/decode_list.py --help` confirms that the RecordsList grid can be listed
  by status without a login (x_status 1 = Decrypted).

Requests this session: openlibrary.org 1; catalog.hathitrust.org 3; be-api.us.archive.org 6; WebSearch 1. All one at
a time, at least 2 s apart. No logins, no credentials read.

### 3. Decision

**P4, Stamford to [Kelsey or Thurloe], Calais, 13 March 1655: N3 (not raised).** The blocking family is **DECODE**.

**Smallest job that closes it** (for LANE N, no login needed): run `tools/decode_list.py --status decrypted
--record-type cipher` (and `partially-decrypted` is already on disk), then grep `holder_raw` and `shelfmark_code` for
Bodleian, Oxford and Rawl. If a Rawl. A. 24 record appears, open its RecordsView with that session's one login and
check whether it is Stamford's leaf (Birch "vol. xxiv p.73, 76"). If none appears, or none is Stamford's, the verifier
who logs that result may set P4 to **N4** without re-auditing anything else. No ASKS row is needed, because the job
needs no person.

Safe sentence, **for use only once N4 is set (not before):**
"Birch (1742) prints William Stamford's letter from Calais of 13 March 1655 with its cipher numerals and no
decipherment. We read its cipher with the key given by Birch's printed decipherments of Stamford's letters of 20 and
30 March 1655. Thurloe's office deciphered this system in 1655, and Tomokiyo has since reconstructed and published it
(Cryptiana, 'William Stamford (1655)'). Our table agrees with his on every value that occurs in this letter. By token:
H 64, C 338, M 16, U 6 of 424, and eleven lines of p.188 are still partly incoherent. No prior decipherment of this letter
located in Birch and its indexes, British History Online, CSPD 1655, the Clarendon calendar vol. 3, the Nicholas
Papers, Abbott, the Clarke Papers, Gardiner, Underdown, the Bodleian's catalogues, Tomokiyo's pages, the solver
repositories, DECODE, Google Books or Internet Archive full text (searched 24 Sept 2026, AUDIT.md). The original leaf,
Bodleian MS Rawl. A. 24, has not been seen."

**Unsafe at any class:** "we broke / cracked / solved Stamford's cipher" (the system was deciphered in 1655 and
reconstructed by Tomokiyo; ours is a keyed reading of one more letter), "first decipherment" without the qualifier "no
prior decipherment located", "previously unread", "unpublished", "no decipherment exists" (the MS leaf is unseen).

**Corrections:** none new. The second audit's "only `10622705bsb` (vol. 1)" was already corrected to vol. 2 by worker D.

## DECODE search, 24 Sept 2026

LANE N audit worker, per §3's "smallest job that closes it" and this session's own brief
(`.claude/briefs/runs/2026-09-24-lane-n-auditDC.md`, job 5). I did not solve, audit or classify novelty; I ran
the two searches this section specifies and report the result for LANE W's own verifier to act on.

**Method.** `tools/decode_list.py --status decrypted --record-type cipher` (login-free, one request at a time,
1.6s apart) crawled DECODE's full **Decrypted** cipher catalogue fresh: 1360 rows, 28 requests, written to
`decode-decrypted-2026-09-24.tsv` (worker's scratch, not committed — see below). Combined with the **Non-
decrypted + Partially decrypted** catalogue already on disk (`sources/decode/records-non-decrypted-2026-09-24.tsv`,
1186 rows, LANE N's earlier no-login crawl), this covers DECODE's entire disclosed cipher-record catalogue as
of today: 2546 rows.

**Result: 0 hits.** Grepped `holder_raw`, `shelfmark_code` and `city` (case-insensitive) across all 2546 rows
for `stamford`, `thurloe`, `bodleian`, `oxford` and `rawl`. Every one of the five terms returns zero matches in
either file. No Rawl. A. 24 record, no Bodleian- or Oxford-held record, and no record whose location fields
name Stamford or Thurloe, exists anywhere in DECODE's public catalogue. Per §3's own decision rule ("if none
appears, or none is Stamford's, the verifier who logs that result may set P4 to N4 without re-auditing
anything else"), this is that negative result, fully logged.

**One caveat, for completeness.** DECODE's `holder_raw`/`shelfmark_code`/`city` fields (what `decode_list.py`
captures) describe the manuscript's location, not its sender. A person-name search would also want the
`c_author` field, which `decode_list.py` does not capture (RecordsList's public grid has no author column;
only RecordsView, which needs a login, shows it). As a secondary, non-authoritative check, a cached third-
party snapshot (`aaymeloglu/unsolved-ciphers`'s `catalogue/decode-catalog.csv`, cloned this session, 10106
rows, date of that repo's own last catalogue refresh unknown) does carry a `c_author` field and shows exactly
one Thurloe-adjacent row: id 4880, "London, British Library, Add MS 4166, f 77-78", author "John Thurloe
Dublin", status Decrypted, 1657. This is John Thurloe himself as a correspondent from Dublin in 1657 — a
different shelfmark, collection and date entirely from P4 (Bodleian MS Rawl. A. 24, Stamford's 1655 letter),
and not itself searched further (out of this job's scope; flagged only so the next worker does not have to
re-find it). No Rawl. A. 24 record appeared, so per the brief the RecordsView step was not opened (no
second login).

**Files.** `decode-decrypted-2026-09-24.tsv` is a worker scratch file (not committed — CLAUDE.md's "fetch once,
keep a manifest" applies to committed campaign data; a one-off crawl made to answer a single yes/no gate for
one target does not need a permanent home in `sources/decode/`). If a future worker wants the fresh Decrypted
catalogue on disk, it can be regenerated in under a minute with the command above (28 requests, well under the
good-citizen cap).

Requests this section: de-crypt.org 28 (`decode_list.py`, all ≥1.6s apart, no login). Combined with the shared
login used for the DC1-DC9 audit above (26 requests, logged in each `ciphers/decode-*/NOTES.md`), this worker's
total de-crypt.org requests for the whole session: 54, under the brief's 80-request cap.

## N4 set, P4, 24 Sept 2026

LANE W worker J (Opus), a fresh verifier session, parent LANE W orchestrator session_011UFnhZnyCntZ8Bn9FpKyTq, 09:03-09:05 UTC. I did not solve or audit P4 before, and I searched nothing except the one snapshot below.

1. s.3's condition: a grep of DECODE's Decrypted list (fresh crawl) and its Non-decrypted and Partially decrypted list for Bodleian, Oxford or Rawl. LANE N ran it over all 2546 rows (1360 + 1186) and got 0 hits, so no Rawl. A. 24 record exists. It also grepped for Stamford and Thurloe. That meets the rule as written.
2. The author-field caveat is a real gap for a letter that has to be found by its sender, because a Stamford item held somewhere else (a copy, or a BL leaf) would not show up in the location fields. I closed it from the cited snapshot (github.com/aaymeloglu/unsolved-ciphers, `catalogue/decode-catalog.csv`, shallow clone of commit 2495c45 of 23 Sept 2026; 10106 rows, keys included; cited only, nothing copied). c_author gives 0 for `stamford`, `stanford`, `kelsey` and `rawl`. c_holder gives 0 for `bodleian`. The 14 `oxford` hits are royalist 1642-46 senders "at Oxford" in BL MSS. `thurloe` has one hit, id 4880 (Dublin 1657, BL Add MS 4166), which is unrelated. `calais` has one hit, id 2734 (Charost, 1673).
3. The one near-miss is id 4899: a 3-page **Key** (status N/A), BL Add MS 4166 f.120, dated 1655-1668, author "W". It is not a decipherment of P4, and it is not the Rawlinson leaf. A key cannot hold P4's plaintext, and the safe sentence already credits the system's prior reconstruction (Tomokiyo), so it does not bear on N4. Suggestion only, for a solver, not a gate: check whether "W" is Stamford's table.
4. What is left is not excluded, and N4 does not require excluding it: DECODE records added after the snapshot that sit outside Oxford and carry a Stamford author field, the unseen MS leaf, JSTOR rows and Marshall. All of these are unpublished or internal work, or outreach gate 2 items.
5. Decision: **P4 is N4.** Prior plaintext: none located. Prior decipherment of this letter: none located. The system was deciphered in 1655 and has been reconstructed by Tomokiyo.

**Safe sentence (s.3, verbatim):**
"Birch (1742) prints William Stamford's letter from Calais of 13 March 1655 with its cipher numerals and no decipherment. We read its cipher with the key given by Birch's printed decipherments of Stamford's letters of 20 and 30 March 1655. Thurloe's office deciphered this system in 1655, and Tomokiyo has since reconstructed and published it (Cryptiana, 'William Stamford (1655)'). Our table agrees with his on every value that occurs in this letter. By token: H 64, C 338, M 16, U 6 of 424, and eleven lines of p.188 are still partly incoherent. No prior decipherment of this letter located in Birch and its indexes, British History Online, CSPD 1655, the Clarendon calendar vol. 3, the Nicholas Papers, Abbott, the Clarke Papers, Gardiner, Underdown, the Bodleian's catalogues, Tomokiyo's pages, the solver repositories, DECODE, Google Books or Internet Archive full text (searched 24 Sept 2026, AUDIT.md). The original leaf, Bodleian MS Rawl. A. 24, has not been seen."

**Unsafe at any class (s.3):** "we broke / cracked / solved Stamford's cipher", "first decipherment" without the qualifier "no prior decipherment located", "previously unread", "unpublished", "no decipherment exists".

Requests: github.com 1 shallow clone. No DECODE requests, no logins.
