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
