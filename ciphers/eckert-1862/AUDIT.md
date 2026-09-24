# AUDIT: the ten 1862 readings of the Eckert "Ciphers Sent" ledger (Huntington mssEC 15)

Verifier session, 24 Sept 2026 (clock read with `date -u`, 03:08 UTC at start). Adversarial audit of the readings in
reading.md (T1-T10, commit as of 24 Sept 2026, `decode.py --check` passes), described in status.json's
contributions list as part of "Eckert keys, 23 checked readings and the corpus-status finding offered to the
Huntington Library" (20 Sept 2026). The solver session did not take part. No decoding was done; reading.md is
unchanged. Levels are those of CLAUDE.md rule 10. The 1864 companion audit, ciphers/eckert-1864/AUDIT.md, is the
precedent; its corpus question (section 12) is not redone here.

## 1. Verdict

| item | telegram (ledger page) | prior plaintext (earliest found) | prior decipherment of this ledger copy | class |
|---|---|---|---|---|
| T1 | McClellan to Halleck, 5 Feb 1862 7 PM (p.[9]) | yes: OR I/7 p.584 (1882); Magazine of American History vol 14 (1885) | none found | **N1** |
| T2 | McClellan to Halleck, 7 Feb 1862 7 PM (p.[15]) | yes: OR I/7 pp.591-592 (1882); Sears, Civil War Papers of G. B. McClellan (1989) | none found | **N1** |
| T3 | McClellan to Buell, 7 Feb 1862 7.15 PM (p.[16]) | yes: OR I/7 p.593 (1882); Magazine of American History vol 14 (1885) | none found | **N1** |
| T4 | Stanton to Buell, 9 Feb 1862 5.30 PM (p.[19]) | yes: OR I/7 pp.937-938 (1882); Nicolay-Hay, Complete Works of Lincoln (several eds.) | none found | **N1** |
| T5 | Lincoln to Hunter and Lane, 10 Feb 1862 (p.[21]) | yes: OR I/8 p.551 (1883); Basler, Collected Works vol 5 (1953); Kansas histories | none found | **N1** |
| T6 | McClellan to Buell, 13 Feb 1862 7 PM (p.[25]) | yes: OR I/7 pp.608-609 (1882); cited to the New York Herald of 21 Feb 1862 by the 1923 Fort Henry and Fort Donelson source book (citation seen, newspaper not seen) | none found | **N1** |
| T7 | McClellan to Buell, 16 Feb 1862 1 PM (p.[35]) | yes: OR I/7 p.626 (1882, dated "[February 16 (?), 1862]", no hour); quoted in Sears (1989) | none found | **N1** |
| T8 | Lincoln to Halleck, 16 Feb 1862 (p.[36]) | yes: OR I/7 p.624 (1882); Basler vol 5; Nicolay-Hay; about 300 Internet Archive items | none found | **N1** |
| T9 | McClellan to T. A. Scott, 17 Feb 1862 (p.[39]) | yes: OR I/7 p.628 (1882, 10.30 a.m.) | none found | **N1** |
| T10 | McClellan to Buell, 21 Feb 1862 (p.[56]) | yes: OR I/7 pp.646-647 (1882, 9.30 p.m.) | none found | **N1** |

All ten plaintexts were printed long before this repository existed; the Official Records alone print every one.
The readings are not independent re-decipherments in the strong sense either: the code-word meanings were fixed
from these same OR prints (reading.md grades them C for that reason), so the readings are a known-plaintext
alignment of the ledger copy with its printed text. Nothing here may be described as new, unread, unpublished or a
first decipherment, and the folder never did so.

**Prior art on the key and the method, which the folder did not credit:** the Decoding the Civil War blog
(Huntington curators) published three of this code's arbitraries from 1862 ledger entries, Andes = McClellan,
Alden = Halleck (30 Mar 2017, "Grant's 'Former Bad Habits'") and Alvord = Buell (18 May 2017, "Bickering
Generals", on two telegrams received 7 Feb 1862), and stated the method this folder used: "We are hoping to
reverse-engineer some of the missing codebooks by comparing telegrams in the Eckert ledgers with those in the
Official Record". Neither post reads any of T1-T10. The 60 other meanings in key.md were not found in print
(Plum 1882's appendix prints a later cipher with different meanings, e.g. Alden = Attorney General).

**What is the folder's own contribution:** the ten ledger copies aligned word by word with their prints, a
63-word key table graded per word (key.md), the ledger's times where the OR gives none or only "(?)" (T7: 16 Feb,
1 PM), and two textual variants in T10 (section 3). These are the contribution-kind results; the plaintexts are not.

Safe sentence (all ten): "Ten telegrams of Feb 1862 in the Eckert sent ledger mssEC 15 were aligned with their
Official Records prints; the code-word meanings come from those prints (grade C). All ten were already in print
(N1, AUDIT.md). The ledger adds the hour for T7 and two wording variants in T10." Unsafe: "Ten Civil War
telegrams decoded"; "the ledger's code, previously unbroken"; "first reading of the 1862 cipher ledgers" (the
project blog published Andes, Alden, Alvord in 2017).

## 2. Per item

Distinctive phrases were searched in the OR djvu full text (whitespace normalised), then as quoted phrases in
the Internet Archive full-text engine (be-api, whole corpus), then in named editions by per-item search.

- **T1** "suggested demonstration on Bowling Green", "eight regiments from Ohio into Western Virginia". OR I/7
  p.584, word for word apart from the ledger's "you[?]". IA full text: 10 items, all OR vol 7 copies, the 1882
  House Misc. Doc. issue, and Magazine of American History vol 14 (Dec 1885). Not in Sears (no hit). N1.
- **T2** "I congratulate you upon the result of your operations", "The bridges at Tuscumbia and Decatur". OR I/7
  pp.591-592 (7.15 p.m.), including "Please number telegraphic dispatches and give hour of transmittal. Thank
  Grant, Foote, and their commands for me." Also Sears 1989 (IA per-item hit) and Magazine of American History
  1885. Not found in Papers of U. S. Grant vol 4 by per-item search ("their commands for me": 0). N1.
- **T3** "while Halleck turns Union City", "Ohio, Indiana, and Michigan". OR I/7 p.593 (7.15 p.m.). IA: OR copies
  and Magazine of American History 1885. N1.
- **T4** "your two heads together will succeed". OR I/7 pp.937-938 (Stanton, no hour). IA: 45 items, mostly
  Nicolay-Hay Complete Works volumes and Lincoln compilations, which print it as the President's message. N1.
- **T5** "to personally oblige both", "amicable understanding". OR I/8 p.551 (Executive Mansion, 10 Feb 1862).
  Basler, Collected Works vol 5 (IA collectedworkson0005royp, per-item hit; solver cites 5:132, page not
  re-read). IA: 109 items (Kansas histories, Lincoln writings). N1.
- **T6** "Watch Fort Donelson closely". OR I/7 pp.608-609 (7.15 p.m.). Google Books: Forts Henry and Donelson: The Key to the
  Confederate Heartland (Google Books date 1989); Williams, Lincoln Finds a General (1949); Fort Henry and Fort Donelson Campaigns (1923), which
  cites "[NYH Feb. 21]" (a New York Herald print of 21 Feb 1862, not seen); 15th Ohio regimental history (1916). N1.
- **T7** "driving meat on the hoof", "by way of Green River". OR I/7 p.626, dated "[February 16 (?), 1862]" with
  no hour; the ledger dates it 16 Feb, 1 PM ("One P M"). Sears 1989 quotes it in a note citing OR. Google Books
  also: The Grand Design (2010); L&N Railroad in the Civil War (2014). N1. Whether Sears or a later
  editor already dates it from the ledger was not established (Sears is lending-only; the snippet shows only
  the OR citation).
- **T8** "put your soul in the effort", "why could not a gunboat run up". OR I/7 p.624. Basler vol 5 (per-item
  hit). IA: about 300 items. One of Lincoln's best-known Donelson telegrams. N1.
- **T9** "altered for five-foot gauge". OR I/7 p.628 (10.30 a.m.). IA: only OR copies and the index. N1.
- **T10** "keep me too much in the dark". OR I/7 pp.646-647 (9.30 p.m.). IA: 22 items incl. a Lincoln-and-McClellan study (lincolnmcclellan0000hear) and
  Williams, Lincoln Finds a General. N1. Variants in section 3.

## 3. Correction: the readings are not all "word for word apart from clerical variants"

reading.md ("All ten entries read cleanly against the printed text; the only variants are clerical") and NOTES.md
section 4 ("agree with the printed text word for word apart from clerical variants") over-state the match. Read
against OR I/7 pp.646-647, T10 differs in sense in two places (ledger as transcribed, conditional on the
transcription, rule 2):

| T10 | ledger (ciphertext.txt l.173, 180) | OR I/7 p.646 |
|---|---|---|
| clause 2 | "If you can **reach** it by the line of the Cumberland" | "If you can **make** it by the line of the Cumberland" |
| clause 6 | "If Railway to **Clarksville** is destroyed" | "If railroad to **Nashville** is destroyed" |

The second is a place-name variant, not a clerical slip. Minor wording differences elsewhere ("five feet gauge" /
"five-foot gauge", T9; "fort Donelson" / "at Fort Donelson", T8) are clerical. This does not change any grade in
reading.md (the variant words are plain words, not code words). Per the brief, reading.md is not edited here; the
fix to its summary sentence is left to the solver lane (suggestion in NOTES.md).

## 4. Source-family log (24 Sept 2026)

| # | family | reachable | what was searched | result |
|---|---|---|---|---|
| a | OR ser. I vols 7, 8 | yes (IA djvu full text, warofrebellionco0007vari, warofrebellionco08unit) | one distinctive phrase per telegram, whitespace normalised; page headers read around each hit | all ten found at the pages reading.md cites |
| a | OR ser. I vols 10, 11-12, 16-17; ser. III vols 1-2 | via IA whole-corpus full text | every quoted phrase of T1-T10 corpus-wide (first 30 hits listed per query; T4, T5, T8 have more hits than that) | for T1-T3, T6, T7, T9, T10 every hit was listed: no OR volume other than vol 7 copies and the 1882 House Misc. Doc. issue; for T4, T5, T8 not established beyond the first 30 |
| a | ORN ser. I vol 22 (western waters) | via IA whole-corpus full text | T8 "put your soul in the effort" and T2 phrases | no ORN item among the listed hits (T2: all 10 listed; T8: first 30 of about 300); ORN vol 22 not read directly |
| b | Lincoln: Basler vol 5; Nicolay-Hay | yes (IA per-item full text) | T5, T8 phrases in collectedworkson0005royp; T4 phrase corpus-wide | T5, T8 in Basler vol 5; T4 in Nicolay-Hay Complete Works |
| b | McClellan: Sears, Civil War Papers (1989) | yes (IA per-item full text, lending-only) | T1, T2, T3, T6, T7, T9, T10 phrases | T2 in full, T7 in a note citing OR; others no hit |
| b | Grant Papers vol 4 | yes (IA per-item) | T2 "their commands for me", T8 "Fort Donelson safe unless" | no hit |
| b | Halleck, Buell, Stanton papers | no printed edition of their Feb 1862 telegrams located; covered only through OR and full text | | |
| c | documentary / campaign compilations | via IA and Google Books full text | quoted phrases | 1923 Fort Henry-Donelson source book; Magazine of American History 1885; Kansas histories |
| d | Huntington CONTENTdm, p16003coll11 | yes (dmQuery, 11 queries) | clear phrases and decoded-word combinations of each telegram ("halleck turns union", "ohio indiana michigan transmittal", "hunter amicable", "gunboat clarksville soul", "kentucky central gauge", ...) | hits only on the coded ledger pages themselves (mssEC 15 pp.[19], [25], [35], [56]) and one unrelated 1864 page; no decoded copy of any of the ten in the collection |
| d | Decoding the Civil War blog | yes (WordPress public API, all 154 posts) | every key.md code word, every addressee, "Feb 1862" | Andes, Alden, Alvord identified (2017); method stated; none of T1-T10 read; "Reverse Engineering Lost Codebooks" (21 Apr 1862 entry) gives Anthon = McDowell, Palate = bridge, which conflict with key.md's grade-I Anthon = Banks, Palate = Cairo (note for the solver lane, not adjudicated) |
| d | Zooniverse Talk | not searched this session (eckert-1864 AUDIT.md section 12: the API does not keyword-search subject comments) | | a volunteer comment decoding one of these entries cannot be excluded |
| e | IA full text | yes | 15 quoted-phrase queries corpus-wide | as above |
| e | Google Books | yes (API with key, country=US) | 6 queries: two T6/T7 phrases, "Quotient" Leavenworth cipher, "Alvord" Buell cipher telegram, "Eckert" "ciphers sent" 1862 decoded, "Decoding the Civil War" ledger decoded arbitraries | print hits for T6, T7 as listed; no decoding of the ledger |
| e | HathiTrust full text | not attempted (Cloudflare challenge per the Access playbook; the bibliographic API does not search text) | | unreachable |
| f | solver repositories | yes (anonymous shallow clones, grepped, deleted) | Eckert, mssEC, Decoding the Civil War, Alvord, Shylock | Bourdeau: only the Cryptiana unsolved-list copy naming the project; Aymeloglu: nothing |
| f | Cryptiana | from the repo snapshot (eckert-1862 NOTES.md section 1; not re-fetched) | | book concordance only |
| f | Plum 1882 (both vols), Bates 1907 | yes (IA djvu) | every key.md code word | Plum's appendix is a later cipher (different meanings); Plum prints a Cipher No. 7 example with "alvord"; Bates nothing |
| g | JSTOR | one reachability probe (HTTP 200 to the search URL); no login, no queries run | "Eckert" "ciphers sent" | queries not run: unreachable for this audit |
| g | Google Scholar, dissertations | not searched this session; eckert-1864 AUDIT.md section 4 row 11 found no article on the ledgers' decoding (20 Sept 2026) | | |

Requests this session: archive.org 7 (metadata 2, downloads 5) plus 5 advancedsearch; be-api.us.archive.org 27;
hdl.huntington.org 13; public-api.wordpress.com 4; www.googleapis.com 6; github.com 3 clones; www.jstor.org 1.

## 5. Did we first-decipher any of them?

No. Every plaintext was in print from 1882-83, and the meanings of the code words were taken from that print.
The ledger copies themselves had not been aligned with the print anywhere located (not on the Huntington pages,
the project blog, the solver repositories, Google Books or IA full text), but three of the key words and the
method were published by the project in 2017.

## 6. Postmortem

- **Outreach gate 1 was not met for this folder.** status.json's contributions list (20 Sept 2026) names
  ciphers/eckert-1862 as the link for "Eckert keys, 23 checked readings and the corpus-status finding offered to
  the Huntington Library". No AUDIT.md existed in ciphers/eckert-1862 until this one (24 Sept 2026), so the
  1862 key table and readings carried no verifier's class when the offer was made. The "23 checked readings" are
  the 1864 entries (20 read with Cipher No. 1, 3 with No. 2), which ciphers/eckert-1864/AUDIT.md (20 Sept 2026)
  covers; the offer's link points at the 1862 folder, which had no audit.
- **No CONTRIBUTIONS.md row exists** for the Huntington offer, and no draft of it is in outreach/ (checked
  24 Sept 2026). Per the brief, none is added here. The send date is also inconsistent in the repo: STATUS.md
  says "corpus enquiry sent 19 Sept", ciphers/eckert-1864/NOTES.md section 9 and status.json say 20 Sept 2026.
- **Over-claims found:** (1) "word for word apart from clerical variants" (reading.md summary, NOTES.md section 4):
  T10 has two sense variants (section 3). (2) Missing credit: NOTES.md section 3 says the meanings "were therefore
  recovered from known plaintext" with no mention that the project blog had published Andes, Alden, Alvord and the
  same OR-comparison method in 2017. Neither over-claim concerns novelty; the folder never called a reading new.
- Corrected in this commit: NOTES.md sections 3, 4 and a new AUDIT pointer; status.json's eckert-1862 target note
  and the contribution row's line. reading.md untouched (brief).

One-line postmortem: the plaintexts were always N1 and the folder said so implicitly; the faults were an offer
made without this audit, a "word for word" that T10 contradicts, and no credit to the project's 2017 key words.
