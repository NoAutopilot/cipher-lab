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
