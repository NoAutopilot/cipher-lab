# AUDIT: huntington-luzerne-destouches-1781 (LANE W verifier G, 24 Sept 2026)

Verifier session, not the solver. Adversarial: tried to disprove novelty. No decoding done here. Written 24 Sept 2026 08:16 UTC.

## Verdict table

| Item | Date, parties | Class | Prior plaintext | Prior decipherment | Confidence |
|---|---|---|---|---|---|
| mssDE 108(A) | Philadelphia, 16 Jan 1781, La Luzerne to Destouches | **N0** | yes: Destouches's own French decipherment of the duplicate, mssDE 108(B), same collection; a copy in AAE Correspondance politique, États-Unis vol. 15 (cited by Idzerda, *Lafayette Papers* 3:319) | yes: mssDE 108(B), contemporary, same code, same text | high (catalogue note, plus 108(B) p.1 image seen) |
| mssDE 68 | Philadelphia, 31 Jan 1781, La Luzerne to Destouches | **N0** | yes: its own interlinear ink decipherment on pp.1-3 | yes: same, contemporary | high (fr5160 / rah-canada precedent; R1/R6 saw the glosses on the image) |

## mssDE 108(A)

**Claim under audit** (NOTES.md 'R10' and 'R16', ROOM 07:54): 108(A) is "the one item in this small correspondence with no
decipherment in the archive", read here as a partial recovery: 719 tokens, C 347, S 0, M 157, U 215, from a key built out
of the contemporary decipherments of siblings mssDE 68, 37 and 55.

**What disproves it.**
1. **mssDE 108(B), same box and shelf number, is the duplicate of this letter, and it is deciphered.** Huntington CONTENTdm
   `dmGetItemInfo/p15150coll7/10580`, catalogue note verbatim (24 Sept 2026): "Autograph letter, signed, describing French
   naval operations and activities of British forces. The letter is written in numerical code, and is decoded, by
   Destouches, in French. "Duplicate" is written in the upper left-hand corner of the first page; the letter is dated "A
   Philadelphie le 16 Janvier 1781" at the top of the first page. The letter is addressed to Destouches in the lower
   left-hand corner of the first page. On the sixth and last page are three lines of conclusion, in French, with La
   Luzerne's signature." Pages are pointers 10574-10579; compound object 10580.
   **Image check** (p.1, pointer 10574, IIIF 1600 px, one fetch): headed "Duplicata" and "Philadelphie le 16. Janvier
   1781", addressed "M. Destouches", eleven cipher lines, each with an ink French gloss under every group and a few pencil
   glosses. The figures are 108(A)'s: p.1 line 2 of 108(B) reads 878 428 72 444 1022 677 266 1068 765 931, the groups the
   R10 reading renders "une des cen te en virginie ou ils [765] y". 108(B) opens with 835, which 108(A) lacks (R6 saw
   "835" pencilled in 108(A)'s margin, which fits a later reader copying across from the duplicate).
   Pages 2-6 of 108(B) were not opened (not needed for the class; a transcription worker will need them).
2. **A plaintext copy is in Paris and is cited in print.** Idzerda et al., *Lafayette in the Age of the American
   Revolution*, vol. 3 (Ithaca, 1980), p. 319 note: "... recommendation to Destouches that a small French naval force be
   sent to the Chesapeake (La Luzerne to Destouches, January 16, 1781, AAE: Correspondance politique, Etats-Unis, vol. 15,
   fols. ...)" (be-api full-text snippets on archive.org `lafayetteinageof03lafa`; folio numbers cut off in the snippet;
   lending-only, page not read). Repeated by *The Papers of George Washington*, Rev. War ser. vol. 30, note 1 to Destouches
   to Washington, 7 Feb 1781 (founders.archives.gov/documents/Washington/03-30-02-0352): "French minister La Luzerne's
   letter to Destouches was dated 16 Jan. 1781 (see Lafayette Papers, 3:319)." So the letter's existence, date and gist
   have been in print since 1980, from a copy in AAE.

**Full plaintext in print?** Not found: Doniol vols 4 and 5 (IA djvu text, `torhistoiredelap04doniuoft`,
`histoiredelapart05doniuoft`: no "16 janvier" letter to Destouches; the vol. 5 Destouches passages are Rochambeau's
letters), Wharton *RDC* vol. 4 (`revolutionarydip04unit`: Destouches 9 hits, none this letter), Founders Online (6 hits
for Luzerne+Destouches 1 Jan-15 Feb 1781, none prints it). Only the summary above. That does not lift the class: N0 turns
on the decipherment of this very letter already existing, and it does, in the same folder number.

**Did we first-decipher?** No. Destouches deciphered it in 1781 on the duplicate. LANE R's reading is an independent partial
re-decipherment from sibling keys, useful as a check of those keys, not a first reading.

**What the reading still gives.** 108(B)'s glosses turn every 108(A) token that 108(B) also carries into known plaintext
(grade C), and they test the R16 context fills. One test is visible on 108(B) p.1 already: figure 655, filled "selon" by
R16 (grade M), is glossed "suivant" by Destouches. 166, which R16 considered and dropped as "dernières", is "dernieres" on
108(B). The M grades were right to hold; the fills should be re-scored against 108(B), not built on.

- **Safe sentence:** "mssDE 108(A), La Luzerne to Destouches, 16 Jan 1781, is the original of a letter whose duplicate in
  the same collection (mssDE 108(B)) carries Destouches's own contemporary decipherment; a copy is in AAE, CP États-Unis
  vol. 15 (Idzerda, Lafayette Papers 3:319). Our partial key reading of 108(A) (C 347, M 157, U 215 of 719) agrees with
  it where checked and is superseded by it (N0)."
- **Unsafe sentence:** "108(A) is the only letter of the group with no decipherment in the archive" / "a partial recovery of
  an unread La Luzerne letter".

## mssDE 68

N0. Its own interlinear ink decipherment covers every one of its 177 groups (R1, R6; catalogue: "The numberical [sic] code
has been translated into French in another hand"). reading_68.txt is a transcription of that decipherment (C 158, M 19),
not a solve. Not checked here for print; the class does not depend on it.
- Safe: "reading_68.txt transcribes mssDE 68's own contemporary decipherment (N0)."
- Unsafe: anything calling it read, recovered or solved by us.

## Search log (24 Sept 2026, this session)

| Family | Searched | Result |
|---|---|---|
| (a) Doniol vol. 4, 5 | IA djvu text, local grep: "16 janvier", Destouches, Arnold, Richmond, Baltimore, "huit cents hommes", "trois semaines", "descente en Virginie" | not printed; La Luzerne's despatches of 2 and 28 Jan to Vergennes printed in vol. 4 (other letters) |
| (a) Wharton RDC vol. 4 | IA djvu text grep | not printed |
| (a) Stevens's Facsimiles | not searched (coverage mostly 1773-83 diplomatic, no full-text copy used) | not searched |
| (a) Magazine of American History / PMHB | not searched this session | not searched |
| (b) Founders Online | browser tool, query Luzerne AND Destouches, 1 Jan-15 Feb 1781: 6 results read in list; Destouches to GW 7 Feb 1781 opened | not printed; note 1 cites the 16 Jan letter via Lafayette Papers 3:319 |
| (c) Library of Congress | loc.gov JSON search "luzerne destouches 1781", "correspondance politique etats-unis 1781" | no Paris transcript or copy of this letter surfaced; Foreign Copying Project volumes not found as digitised items |
| Lafayette Papers (Idzerda) vol. 3 | be-api fts inside `lafayetteinageof03lafa` | **hit**: 3:319 cites the letter and the AAE copy |
| (d) Huntington | dmQuery CISOSEARCHALL^Luzerne over p15150coll7 (89 records); dmGetItemInfo 10580, 10299; dmGetCompoundObjectInfo 10580; IIIF 10574 | **hit**: 108(B) deciphered duplicate; also mssDE 62, a one-page clear letter of the same date (catalogue: "describing French naval operations", no code) and mssDE 107 (4 Jan 1781), not opened |
| (e) Tomokiyo / Cryptiana | local snapshot (check-solved and R2 read it): only the Yale 8 Jan 1781 passage, a different code | not published there |
| (f) IA full text | Doniol, Wharton, Idzerda as above | as above |
| (f) HathiTrust | not used (IA copies sufficed) | not searched |
| (g) solver repos | check-solved's grep (24 Sept 2026) re-used, no new clone | no mssDE entry |
| (g) CrossRef | "Luzerne Destouches 1781 cipher" | none on this letter (Mariner's Mirror 2018 'Race to the Chesapeake', March 1781, lead only) |
| (g) HAL | "Luzerne Destouches" | 0 |
| (g) OpenAlex, Semantic Scholar | one attempt each | 429, unreachable |
| JSTOR | 2 rows queued in JSTOR-QUEUE.tsv | queued |
| Google Books | LANE V's host; ROOM line posted | pending, does not affect the class |

Requests: hdl.huntington.org 6 (1 dmQuery, 3 dmGetItemInfo of which 1 empty reply, 1 dmGetCompoundObjectInfo, 1 IIIF
image); archive.org 12 (advancedsearch 4, metadata 4, download 4); be-api.us.archive.org 14; founders.archives.gov 4
(1 curl 202, 3 browser); loc.gov 2; api.crossref.org 1; api.archives-ouvertes.fr 1; openalex 1; semanticscholar 1.

## Postmortem

**Failure:** the holding archive's own collection was searched item by item (the four pointers the scout named), never
across the collection. One `dmQuery` for "Luzerne" returns 108(B) beside 108(A): same call number, same date, catalogued
"decoded, by Destouches". The verifier template's lesson of the Eckert 1864 second audit ("search the holding archive's
full text across the whole collection... duplicates and letter-book copies live elsewhere") would have caught it before
five worker sessions (R1, R2, R6, R10, R16) spent on key recovery. The printed trail was one Founders Online footnote.

**Over-claiming sentences corrected** (NOTES.md, a dated verifier note at the top and inline markers): "only mssDE 108(A)
... in fact lacks any decipherment in the archive"; "genuinely undeciphered in the archive"; "the one item in this small
correspondence with no decipherment in the archive"; the Verdict "open" (recommend `found-solved` to the lane
orchestrator; not changed here, status.json untouched). reading_108A.txt's header is generated by decode_key and was left
alone; its grades stay valid as a record of what the sibling key gives.

**Recommendation (not done):** a transcription worker reads 108(B) pp.1-6 (glosses) into interlinear_readings.tsv, then
108(A) is re-graded C from its own duplicate and the R16 fills scored against it: that is the matched control R16 wanted.
No SO prompt written: N0 is below N3.


## JSTOR (owner's machine, 24 Sept 2026)

Recorded by the JSTOR runner on the owner's machine (logged-in JSTOR account, built-in browser, one search per queue row, 6 s apart, no block page). First-page hits for every row are in `JSTOR-QUEUE.tsv`; only the hits that could print, calendar or discuss the letter were opened. No class is changed here; the verifier moves it.

Rows 43-44 answered (2 queries). One hit opened:

- Waldo G. Leland (ed.), "Letters from Lafayette to Luzerne, 1780-1782", *American Historical Review* 20/3 (Apr. 1915), pp. 577-612, https://www.jstor.org/stable/1835861 (open access). In-document search: "Destouches" 1 hit (pp. 583-584), Lafayette to Luzerne early in 1781 reporting that Destouches "n'a pas de biscuit" and cannot put to sea, with the editor's note that Destouches succeeded Ternay on 15 December 1780 and held the command until Barras arrived on 8 May 1781; "chiffre" only for Lafayette's own letter to Vergennes being enciphered. It prints Lafayette's letters, not La Luzerne's to Destouches; the 16 and 31 January 1781 letters are not cited. Sioussat 1936 (*Pennsylvania Magazine* 60/4, pp. 391-418, Luzerne and the Maryland ratification) was not opened.
