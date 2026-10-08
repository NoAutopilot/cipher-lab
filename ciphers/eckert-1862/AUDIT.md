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

# Second audit: GAPS113-171 key recovery and the 32 residue candidates (VERIFY-ECK, 3 Oct 2026)

Verifier session VERIFY-ECK (account-4), 3 Oct 2026, 17:11-17:40 UTC (clock read with `date -u`). Separate from the
GAPS110-171 solver sessions. Claim under audit: "the mssEC 15 ledger's code words recovered at grade C by aligning
ledger pages with telegrams printed in OR ser. I (pooled held-out 76/88 vs shuffled-pairing p95 1), dated key column
(print/key_dates.py), residue decoded; 32 residue entries read with no M token (print/residue/candidates.tsv): 19 on
print-matched pages (N1 shape), 13 with no print match." No decoding beyond the folder's own `--check` runs.

## A. Re-derivation (rule 7)

| check | result |
|---|---|
| `decode.py --check` | exit 0, reading.md current |
| `print/key_dates.py --check` | exit 0 |
| `print/residue_decode.py PAGES --check`, `print/residue_candidates.py PAGES --check` | exit 0 on the 57 pages of `print/residue/pages_manifest.tsv`, re-fetched in one CONTENTdm `dmQuery` on callid mssEC 15 (57/57 sha256 match the manifest) |
| pooled held-out, `print/or_align.py` unchanged, pooled OR text rebuilt (ser. I vols. 5, 9, 10 pt 1-2, 11 pt 1 and 3, 12 pt 1 and 3, 51 pt 1, IA `_djvu.txt`, re-fetched) | seed 1: 76/88 = 0.864, control mean 0.26, p95 1 (1000 draws), align_pairs.tsv byte-identical to the committed one after sort; **new seed 20261003: 76/88, control mean 0.20, p95 1** |

Verdict: **reproduces.** One coverage finding: the same `dmQuery` returns text for two more pages the committed residue
set lacks, 4979 (12 Feb, "Alden Retain the Koran battery also the other troops for Lamb ...", an entry using Lamb and
Koran) and 5125 (the cover title). The residue is 58 text pages, not 57; 4979 has never been decoded or searched. It is
also a sent-side witness for Lamb, the word GAPS171 wanted a second witness for. Next step for the solver lane, not done
here.

## B. Control audit (rule 3)

- Can the shuffled-pairing control differ from the target? Yes. It re-aligns each test entry to another matched
  telegram's print window; the 123 telegrams go to Lander, Rosecrans, Hooker, Banks, Halleck, McClellan, McDowell,
  Fremont, Wool and others, Feb-Jul, so a wrong window rarely puts the fit meaning under the code word. Confirmed.
- Its weakness: in a wrong window difflib seldom finds a 1-word-for-1-3-words replacement at all, so the control also
  measures "no alignment" as well as "wrong meaning". I added a second control that keeps the real alignment and permutes
  the fit meanings across the 84 fit words (scratch script, not committed): mean 1.64 hits, p95 7, p99 10, max 18 in
  1000 draws, against 76 real. **Pass on both.**
- Class balance (the AX-NAMES lesson): the 88 scored test occurrences spread over 37 words. The largest single word is
  humming, 8 of 88; then rampant, indus and welsh, 7 each. Not one dominant class.
- Were the dated values fitted on the held-out half? No. or_align.py's test scores against `fit`, built only from
  even-group telegrams' alignments; key.md (and so its dated column) is not read by the scorer. The dated key.md values
  used for the residue were fitted on all telegrams, which is right for a key: the held-out figure tests the method,
  not each row.
- Not covered by the held-out test: whether a key row holds on a *different line*. See C, 4978.2 and 5051.

## C. The 13 "no print match" candidates

Searched 3 Oct 2026: OR ser. I vols. 5, 7, 8, 9, 10 pt 1-2, 11 pt 1 and 3, 12 pt 1 and 3, 51 pt 1, 53 (local `_djvu.txt`,
exact phrase after normalising); **OR ser. II vol. 3** (IA waroftherebellio026237mbp) and **ORN ser. I vol. 22**
(IA officialrecordso0022unse), which no earlier pass searched; `tools/print_check.py` with 18 phrases
(print/residue/verify_eck_phrases.txt; output print/residue/verify_eck_print_check.tsv): IA be-api full text over all
items, Google Books (key, country=US; quoted-phrase counts of 300+ are loose matches, read only the named hits),
OpenAlex, CrossRef; 11 more be-api queries on variant wording (digits for numbers, "to-morrow"); the Decoding the Civil
War blog through the WordPress API (12 searches; posts read: "Reverse Engineering Lost Codebooks" 21 Apr 2017,
"Bickering Generals" 18 May 2017, "Buckner Goes Down" 14 Apr 2017).

| entry | date, parties | found | class |
|---|---|---|---|
| 4992.2 | 16 Feb, McClellan to Foote | ORN ser. I vol. 22 ("sorry you are wounded ... nearly [600] sailors") | **N1** |
| 4995.1 | ledger "Feb 7", McClellan to Buell | OR ser. I vol. 7 p.630, dated **February 17, 7.30 a.m.** (Prussian smooth bores) | **N1** |
| 4995.2 | 17 Feb, McClellan to Halleck (Buckner, Pillow to Fort Warren) | OR ser. II vol. 3 | **N1** |
| 4997.2 | 18 Feb, Colburn to Halleck (Tilghman to Fort Warren) | OR ser. II vol. 3 | **N1** |
| 5005.2 | 20 Feb, McClellan to Halleck (original order, Fort Warren) | OR ser. II vol. 3 | **N1** |
| 4978.1 | 11 Feb, Colburn to Buell (3,500 rifles) | not in print by these searches; the clear text is the Huntington's published volunteer transcription; its one code word Alvord = Buell was printed by the DCW blog in 2017 | **N1** |
| 4998.2 | 18 Feb, Van Vliet to Hooker (barges) | same; one code word Andes = McClellan (DCW blog 2017) | **N1** |
| 5008.1 | 21 Feb, Stanton to Halleck (General Smith spared?) | same; Alden = Halleck (DCW blog 2017) | **N1** |
| 5036.2 | 3 Mar, Stanton to Halleck (Smith nominated) | same; Alden = Halleck (DCW blog 2017) | **N1** |
| 4992.3 | 16 Feb, McClellan to Buell ("how many in Sermon line") | not found; Alvord and Andes printed by the DCW blog 2017; **Sermon = Bowling Green** (key.md C, from OR 7 pp.584, 624, 626) printed nowhere found | **N3** (the one code word only) |
| 4978.2 | 12 Feb, Stanton to "Andes" ("Dawn General Jin ... light draught Steamer") | reading **wrong**: decoded [McClellan], but the addressee is the commander at Fort Monroe | no class: withdrawn |
| 5051.1 | 16 Mar, McClellan to "Andes commanding Fort Monroe" | reading **wrong** the same way: McClellan signs it, so Andes is not McClellan here | no class: withdrawn |
| 5051.2 | 16 Mar, the coded copy of 5051.1 ("for Dawn") | reading **wrong**, same; Dawn and Jin, Davis, Darby (4978.2) unread | no class: withdrawn |

**The 19 print-matched entries:** N1, provisionally. Their page is matched to print, but a page match is not proof for
every entry on it (GAPS167's own caveat), and this session did not verify them entry by entry. Nothing in them may be
called new.

**Why 4978.2/5051 fail.** key.md's dated rule reads Andes = McClellan from 1 Feb to 4 Jul whatever the line. 5051.1
gives "For Andes commanding Fort Monroe" in half-clear form, and its twin 5051.2 replaces "Fort Monroe" with Dawn. On the
Fort Monroe line, then, Andes is that commander (Wool, in Feb-Mar 1862). This is an inference, grade I; it is not added
to key.md (no decoding here). These entries cleared GAPS167's "no M token" filter because the wrong value carries grade
C, and the held-out test cannot catch this: every pooled telegram is on the western, Potomac or Shenandoah lines.
**Lesson:** a dated key also needs a line or recipient scope before its C grade transfers to a telegram on a line no
witness covers.

**Propagated after this audit (GAPS181, 3 Oct 2026, rule 10).** key.md now scopes Andes by line: on an entry
addressed "Andes Dawn" or "Andes [commanding] Fort Monroe" it reads the commander at Fort Monroe (grade I; Wool is an
inference), and Dawn = Fort Monroe (C, from the 5051.1/5051.2 twin). Regenerated: 5051.1 and 5051.2 read [commander at
Fort Monroe]; 4978.2 reads the same with Dawn graded M (12 Feb is outside Dawn's witness range) and leaves
candidates.tsv; 5054.3 (22 Mar, in OR 51 pt1, one of the 19 print-matched) had the same misreading and now reads
[commander at Fort Monroe] [Fort Monroe]. Classes unchanged: the three in the table above stay without a class; 5054.3
stays N1 provisional. Residue page 4979 was added (two entries, 12-13 Feb; not print-checked, no class). The SO-ECK-4992
row is unaffected (4992.3 is McClellan to Buell, not on the Fort Monroe line; its reading is unchanged).

## D. Prior art on the key (correction to section 1 of this file)

Section 1 above credits the Decoding the Civil War blog with three arbitraries. It printed more. "Reverse Engineering
Lost Codebooks" (21 Apr 2017,
https://decodingthecivilwar.wordpress.com/2017/04/21/reverse-engineering-lost-codebooks/) gives, from Lincoln's 21 Apr
1862 telegram to McClellan: Andes = McClellan, Palate = bridge, Rampant = enemy, Anthon = McDowell, Label [the ledger's
Sabel] = Rappahannock River, Berlin = Lincoln. "Buckner Goes Down" (14 Apr 2017) prints a received telegram addressed
"Indus Ocean" (19 Feb 1862) without decoding Indus. So those key.md rows for April 1862 (rampant, palate, Anthon =
McDowell, Berlin, Sabel) are **published**, credited to the Huntington's DCW team (the post names the project leader only as "Mario"). The
other rows are ours.

## E. Classes, key source, sentences

| scope | class | key |
|---|---|---|
| ten readings T1-T10 (section 1) | N1, unchanged | ours (C, from OR prints); Andes/Alden/Alvord published (DCW 2017) |
| 9 of the 13 no-print candidates plus the 5 found in OR ser. II vol. 3, OR I/7 and ORN I/22 (C above) | N1 | ours, plus published rows |
| 4992.3 | N3 for "Sermon = Bowling Green" in this entry; the rest of its text is N1 | ours (OR 7 alignment) |
| 4978.2, 5051.1, 5051.2 | none (reading wrong) | n/a |
| 19 print-matched residue entries | N1 (provisional, page-level) | ours |
| key recovery method (pooled held-out) | reproduces; controls pass | ours from print alignment (grade C), with DCW 2017 prior art for 8 arbitraries |

Safe sentence: "Aligning the 1862 Eckert 'Ciphers Sent' ledger (Huntington mssEC 15) with telegrams printed in the
Official Records recovers code-word meanings at grade C (held-out 76/88 against shuffled controls at 1 and 18 hits). The
telegrams those words occur in are almost all in print already, or their clear text is published in the Huntington's own
transcription; one code word in one unprinted entry (Sermon = Bowling Green, 16 Feb 1862) was found in no earlier
publication by our search."

Unsafe sentence: "13 previously unread Civil War telegrams decoded." Five are printed in OR/ORN, four were readable from
the published transcription plus the DCW team's published arbitraries, and three were decoded wrongly.

Not searched (limits on the N3): Sears, *Civil War Papers of George B. McClellan* (1989; not full text online), OR
ser. III vol. 1, the Stanton papers (LC; no edition), JSTOR (no row queued: one code word in one telegram does not
warrant one). Second opinion queued as SO-ECK-4992 for the N3.

## F. Postmortem

The "13 with no print match" figure counted only the OR volumes the lane had grepped (ser. I). Prisoner traffic (ser.
II) and naval traffic (ORN) were never searched, and or_match's 5-grams miss telegrams whose numbers the ledger spells
out ("thirty five hundred") while the print uses digits (4995.1). "No M token" was used as a quality signal although an
off-line C value passes it. Corrections made: NOTES.md (VERIFY-ECK section). candidates.tsv is generated and left as
is; its "page in print" column must not be read as an entry-level verdict.

## Carry-over R12A-ECKV (6 Oct 2026, verifier, account 1, for LANE LANE-RUN12-account-1): grade of the Lehigh tokens

Claim under audit: D1-ECK62S (NOTES.md, 6 Oct 2026) found 13 Lehigh uses in the sent ledgers mssEC 18-19, 8 print-read all
Canby (6) or "can be" (2), 0 Hurlbut, and held the two committed tokens (9947.505, 10020.609) at M "for a verifier grade decision".
This section is the decision. It is a grade decision only: no novelty class changes (the readings of both committed entries
are of telegrams printed in OR ser. I, N1 as before).

Checked independently: OR ser. I vols. 41.4, 49.1, 49.2 `_djvu.txt` re-fetched (archive.org 3 requests, sha256 matching
`ec18/or_volumes.tsv`) and the slots read by phrase: 9102 (41.4, "General Canby expected to leave New Orleans about the 15th
instant", 24 Oct 1864, to Rosecrans), 9880 (41.4, "The orders of General Grant and General Canby are that the pursuit must be
continued"), 9171 (49.1, 29 Jan 1865 to Thomas, "decides your question about sending troops > General Oaiiby" -- OCR of Canby;
the ledger's "Whiff" stands in the troops slot), 9955 (49.1, "sent as quickly as possible to Canby to assist at Mobile"),
10019 (49.2, "those sent home to be mustered out can be attached to"); 9952 (49.1, 4 Feb 1865, "... early - has many dismounted
men": the Lehigh slot is the lost word) and 9174 (49.1, 1 Feb 1865 to R. Allen, "the -- made to send forage"; "notified of this
arrangement" not in the OCR) are lacunae, as D1-ECK62S says. 9937, 9947, 10020 (45.2, 48.1, 48.2) were not re-fetched; 9947 and
10020 were already image- and print-checked (DEF1-ECK62I, DEF1-ECK62P).

Decision (rule 4), mechanised in `ec18/lehigh_grades.py` -> `ec18/lehigh_grades.tsv` (`--check` exit 0):
- **C 8.** Each of the 8 print-read uses takes the word its own telegram's print has in the Lehigh slot: Canby (9102, 9880, 9937,
  9947, 9171, 9955) or "can be" (10019, 10020). The print is the plaintext of this very use (same date, addressee and surrounding
  words), so it is known plaintext, not a key value carried from elsewhere. For the two committed tokens this replaces the
  held M: 9947.505 Lehigh = Canby (C), 10020.609 lehigh = can be (C).
- **M 4.** 9174, 9952 (dated Feb 1865, slot lost in the OCR) and 9272, 9273 (Sept 1865, outside OR ser. I). Not H: the book's
  value (Hurlbut, mssEC 41 p.17 l.6) is contradicted by every print-read use from 24 Oct 1864 to 24 May 1865, across both
  sent ledgers and four addressees, so the book does not license H for an unread use in or after that window. Not C or S for
  Canby either: "Canby" for these four is inference from the other uses (grade I at most), and neither lacuna is read.
- **clear 1.** 9280 "Lehigh Iron" is a clear word, not a code token.
- The key row stays H as the record of what the book says (ciphers/eckert-1864/key.md p.17 l.6, image-checked DEF1-ECK62P); the
  witness record is unchanged: book = Hurlbut; operator use Oct 1864 - May 1865 = Canby / "can be". Not settled by count: the
  C grades rest on each telegram's own print, not on the majority. A Lehigh token in any 1864-65 reading that no print reads is
  M, not H.
- Not decided here: Leghorn, Legend, Leopard (the same Hurlbut block, seen in passing by D1-ECK62S as Canby / "can be"); their
  date-aligned sweep is R12A-ECKLEG's job and its grade decision a verifier's after it.

Applied: `ec18/lehigh_grades.tsv` is the per-token grade of record for Lehigh. The committed `ec18/readings.md` and
`ec18/s2/readings.md` (ec18.py output, key-book rendering) still print `[Maj Gen S. A. Hurlbut]` at H for 9947.505 and
10020.609, and `align_tokens.tsv` (both) still marks them `H CONFLICT`; regenerating them through ec18.py needs vol18.json, about
45 OR volumes and the DIR62 guard volumes and would re-run the whole split2 cascade, outside this box. Read those two brackets
as superseded by lehigh_grades.tsv (Canby C, can be C); next: fold a per-token override table into ec18.py at the next full
regeneration. Counts for the two entries after the decision: 9947.505 H 13 C 1 (was H 14 C 0); 10020.609 H 14 C 1 (was H 15 C 0).
Checks: `ec18/lehigh_grades.py --check` current (exit 0), `decode.py --check` current (exit 0; mssEC 15 readings untouched).
SECOND-OPINIONS-QUEUE.tsv: the target's only row (SO-ECK-4992, mssEC 15 entry 4992.3) does not contain Lehigh; nothing to carry.
Requests: archive.org 3, 2 s apart; 0 subagents.

## Carry-over R12A-ECKV2 (6 Oct 2026, verifier, account 1, for LANE LANE-RUN12-account-1): grade of Leghorn, Legend, Leopard

Claim under audit: R12A-ECKLEG (NOTES.md, 6 Oct 2026) aligned every Leghorn, Legend and Leopard in the sent ledgers mssEC 18-19
to OR ser. I: 48 print-read, 0 Hurlbut (the book value, mssEC 41 p.17 l.5-6, H), Legend reading Butler 13 / Canby 10 in
overlapping months; no grade changed, flagged for a verifier. Grade decision only; no N-class or depth changes.

Checked independently: OR ser. I vols. 33, 42.3, 45.2 `_djvu.txt` re-fetched (archive.org 3 requests, sha256 matching
`ec18/or_volumes.tsv`) and 16 slots read by phrase, all as R12A-ECKLEG states: vol. 33 Legend = Butler at 9674 ("spoiled by your
co-operation with General Butler"), 8906 ("forwarded to General Butler"), 8930 ("General Butler has asked for two more
batteries"), 8942 ("After sending 1,000 horses to Butler"), 9718 ("have General Butler telegraph direct to you"), 8945 ("I had
telegraphed to General But-ler to use his own judgment"), 8946 ("Generals Butler and Peck"); vol. 42.3 Legend = Butler at 9120 x2
("all of Butler's troops, except 500 regulars", "Before ordering Butler back"), Leghorn = circumstances at 9144 ("Under these
circumstances the Cavalry Bu-reau") and 9145 ("Under all these circumstances, I invite you"); vol. 45.2 Leghorn = circumstances
at 9934 ("Parkersburg or Bellaire, according to circumstances"), = can be at 9937 ("if you can be ready in time"), = Canby at
9908 ("ordered by General Canby on the 25th and 26th ultimo") and 9914 ("General Canby is obliged to keep"); Legend = Canby at
9937 ("General Canby has been ordered to collect"); Leopard = Canby at 9937 x2 ("expeditionary force of General Canby", "Canby can
easily reach Montgomery"). The other 32 aligned slots were not re-read here (vols. 34.4, 36.2, 36.3, 37.2, 38.4, 39.2, 39.3,
41.2, 41.4, 48.1, 48.2, 49.1, 49.2).

Decision (rule 4), mechanised in `ec18/hurlbut_row_grades.py` -> `ec18/hurlbut_row_grades.tsv` (`--check` exit 0):
- **C 47.** Each aligned code use takes the word its own telegram's print has in the slot (Leghorn: Canby 10, "can be" 2,
  "circumstances" 3; Legend: Butler 13, Canby 10; Leopard: Canby 9). The print is the plaintext of this very use, not a key
  value carried from elsewhere.
- **gloss 1.** Leopard 9057 (26 Aug 1864): the ledger writes "Gen Canby" in clear with "leopard" inserted above; the print
  reads Canby. An operator's pairing beside clear text, not a code-only token; kept out of the C count.
- **M 12.** Leghorn 9877, 9945 and Legend 9786, 9945, 9671, 9672, 9026, 9111, 9186, 9242, 8944 (no print found), Leopard 9174
  first occurrence (OCR lacuna). Not H: for Leghorn and Leopard every print-read use contradicts the book's Hurlbut. Legend:
  two print-read values in overlapping months (27 May - 10 Nov 1864); no witness matches an unread use, so M whatever its date
  or addressee -- including 9671/9672 (Feb 1864, to Caldwell), which sit only in the Butler months and on a Butler addressee:
  that is inference (I), not a witness for this use.
- Legend conflict recorded with every witness (pointer, date, addressee, OR place; all sent from Washington) in HYPOTHESES.md
  "Legend: two print-read values". Not resolved, not settled by count (13 v 10). Observation only (I): Butler uses go to the
  eastern operators (Caldwell, Beckwith), Canby uses to western ones.
- Key rows stay H as the record of what the book says (ciphers/eckert-1864/key.md p.17). A Leghorn/Legend/Leopard token in any
  1864-65 reading that no print reads is M, not H.

Applied: none of the three words (nor Lehigh's forms beyond the two R12A-ECKV tokens) is a token of the committed
`ec18/readings.md`, `ec18/s2/readings.md` or either `align_tokens.tsv` (the script fails if one appears), so no reading or count
changes. `ec18/hurlbut_row_grades.tsv` is the per-token grade of record for the three words. Checks: `hurlbut_row_grades.py
--check` current, `lehigh_grades.py --check` current, `decode.py --check` exit 0. status.json: no per-token grade field; nothing
to carry. SECOND-OPINIONS-QUEUE.tsv: the target's only row (SO-ECK-4992, mssEC 15 entry 4992.3) contains none of the words.
Requests: archive.org 3, 2 s apart; 0 subagents.

## Carry-over D07-ECKV (7 Oct 2026, verifier, account 1, for LANE DEFAULT-account-1-20261007-0042): the D07-ECK62 regrade carried into ec18.py's outputs

Claim under audit: D07-ECK62 (NOTES.md, 7 Oct 2026; commit 35c387168) folded the verifier grade tables `ec18/lehigh_grades.tsv`
(R12A-ECKV) and `ec18/hurlbut_row_grades.tsv` (R12A-ECKV2) into `ec18/ec18.py` as a per-token override table, regenerated legacy
and split2, and reports 34 mssEC 18 tokens regraded (27 H->C, 7 H->M), 2 of them in counted readings (9947.505 Lehigh H->C
[Canby], 10020.609 lehigh H->C [can be]). Separate session from every solver. Grade propagation only: no decoding, no novelty
search, no N-class change.

Checked independently:
- Override table against its sources (script, both cascades): every mssEC 18 row of the two verifier tables (7 Lehigh + 27
  Leghorn/Legend/Leopard = 34 uses) maps to a row of `ec18/overrides.tsv` (= `ec18/s2/overrides.tsv`, identical) with the same
  word, meaning and grade; 33 rows carry 34 tokens because 9937.479 holds Leopard twice (R12A-ECKV2: "Leopard = Canby at 9937
  x2"). Two rows are placed on the entry opening one pointer earlier (legend 9786 -> 9785.169 M, legend 9789 -> 9788.172 Butler
  C): both table rows have no date ("none above on page"), so the code places them on the nearest entry opening at most two
  pointers before -- consistent with the rule written in NOTES.md. 10019 lehigh (table date 23 May) sits on 10019.607 (ledger
  heading 24 May) by the same-page fallback; the hurlbut table's own leghorn row for 10019 reads 24 May and OR 49.2 p.881-882,
  so the placement is the same telegram. 0 rows unplaced, 0 in conflict. mssEC 19 rows (9102, 9171, 9174, 9272, 9273, 9280 and
  the hurlbut table's mssEC 19 rows) are outside ec18.py (mssEC 18 only) and change nothing here.
- Each C needs known plaintext: all 27 C rows' `reason` cell cites the print of that very telegram (OR volume and page for the
  hurlbut rows); none is carried from another use. All 7 M rows are the tables' M decisions (no print of the slot, or Legend's
  two print-read values). Print spot-check (6 of 34, both counted tokens included; the entry's clear neighbours located in the cited OR volume's `_djvu.txt`): 9947.505 "can spare for General Canby will be mounted at cavalry depot" (48.1), 10020.609 "as soon as transportation can be provided" (48.2), 9788.172 "The order respecting General Butler and the Eighteenth Corps" (37.2), 9754.126 "has been suggested to General Canby. A. J. Smith" (38.4), 9893.384 "assigned to General Canby's command. As Price" (41.4), 10010.594 "breaking up Canby's division and assigning" (48.2): 6 of 6 read as the tables say.
- Recount (entries.tsv before/after 35c387168, both cascades): legacy 671 entries H 12699 C 37 M 0 -> H 12665 C 64 M 7; split2
  729 entries H 12676 C 37 M 0 -> H 12642 C 64 M 7. Per entry: 24 entries changed in each cascade, exactly the 24 entry ids of
  overrides.tsv, and in each the H loss equals the C+M gain equals the number of override tokens; no other column (keyed, oov,
  fully_keyed, book, or_match) moved in any entry. Counted readings (28 fully keyed entries, `ec18/readings.md` and
  `ec18/s2/readings.md`): H 369 C 2 -> H 367 C 4; 9947.505 H 13 C 1 (was H 14 C 0), 10020.609 H 14 C 1 (was H 15 C 0) -- the
  counts this file's "Carry-over R12A-ECKV" already gave on paper. Agreed.
- Rule 7 re-run (data re-fetched to scratch, not committed): vol18.json (sha256 cb162574, matches pilot1864/manifest.tsv), DIR62 8 `_djvu.txt`, OR 32.1-49.2 48 `_djvu.txt` (all 48 sha256 match `ec18/or_volumes.tsv`). `ec18.py DATA OR --possessive --guard DIR62 --check` exit 0, the same with `--split2` exit 0, `--book 2` exit 0, `--book 2 --split2` exit 0; `lehigh_grades.py --check` 0, `hurlbut_row_grades.py --check` 0, `../decode.py --check` 0 (fully_keyed_grades printed by the run: H 367, C 4, I 0, M 0, both cascades). The committed outputs are what the code produces.
- Depth (rule 4a): an H->C move keeps every regraded counted token inside H/C/S, so the share of H/C/S cipher tokens in the
  counted readings is unchanged (371 of 371 keyed tokens before and after); the 7 M tokens are all in entries with no committed
  reading. No depth field exists for eckert-1862 in status.json (the items are N1, below the N3 line `tools/depth_check.py`
  counts; `tools/depth_check.py` run 7 Oct 2026, exit 0, eckert-1862 not listed); nothing to lower or raise.

Propagation (rule 10): status.json (targets[4] note, results[21]) names no Lehigh/Hurlbut-row token or ec18 count -- nothing to
carry; PROGRESS.tsv has no eckert-1862 row; SECOND-OPINIONS-QUEUE.tsv's only row for the target (SO-ECK-4992, PROMPT-chatgpt-
ECK4992.md, mssEC 15 entry 4992.3) contains none of Lehigh, Leghorn, Legend, Leopard, Hurlbut, Canby, 9947 or 10020 (grep, 0
hits) -- nothing to carry. Section "Carry-over R12A-ECKV"'s sentence "Read those two brackets as superseded by lehigh_grades.tsv"
is now history: the committed readings print [Canby] C and [can be] C themselves. `align_tokens.tsv` keeps the book value and
CONFLICT for the two tokens by design (the evidence the grade rests on, not a reading).

Verdict: ENDORSED. The regrade carries the two verifier decisions exactly, adds no grade of its own, and every C rests on the
print of its own telegram. No N-class, depth or safe sentence changes (sections 1 and E stand).
Note (not a finding): 9785.169 and 9788.172 are marker-assigned Cipher No. 2 entries (entries.tsv book 2) read here through the
No. 1 key; key-no2.md also gives Legend = Butler (H, p.18 l.5), so 9788's C (Butler) agrees with that book too.
Requests: hdl.huntington.org 1, archive.org 56, >= 1.6 s apart; 0 subagents.

## Propagation D12-V62 (7 Oct 2026, verifier, account 2)
D12-E62H (b5a795fe6) moved six Hurlbut-row override tokens M -> C, each from the print of its own telegram (OR 33 pp.502, 514;
OR 49.1 p.581 -- cited as p.580, corrected; p.646; Papers of U. S. Grant vol. 11, page not read), plus mssEC 19 9174 lehigh and
leopard (OR 49.1 p.624). D12-V62 re-read every cited print by script: 8 of 8 C kept. The recount quoted above (lines 393-394) is
now legacy H 12665 C 70 M 1, split2 H 12642 C 70 M 1. The counted readings (H 367 C 4) and every N-class here are unchanged. The
book-2 cross-reading outputs (readings_b2.md) were regenerated for today's key-no2.md rows; none is quoted in this file.

## AUDIT (LS3-V62)

Verifier LS3-V62 (account 2, LANE ST-LEDGER-3), 8 Oct 2026, 10:41-11:0x UTC by `date -u`; a separate session from the reader LS3-R62,
not protecting its conclusions. Scope: the six mssEC 15 residue entries LS3-R62 image-checked: **4982.1, 4999.1, 4984.3, 4992.1, 4999.2,
4982.3** (print/residue/readings.md, generated by print/residue_decode.py from the Huntington volunteer transcription). Nothing decoded.
Depth under .claude/briefs/runs/2026-10-08-acct3-depth-bar.md.

### 1. Re-derivation, key source, image
- `print/residue_decode.py --check` and `decode.py --check` were re-run by the reader; this session changed no input, so not re-run.
- **Key source (rule 10).** The 1862 key (key.md) is C-grade, rebuilt by us from the alignment of other ledger telegrams with their
  Official Records prints: **`ours`** (a plain-copy alignment, not a period key sheet). Exception: Andes = McClellan, Alden = Halleck,
  Alvord = Buell were published by the Decoding the Civil War project blog in 2017 (status.json note): **`published`** for those three.
- **The plain text is public.** The Huntington's own page records (CONTENTdm `items/<pointer>/false`, field `text`; fetched 8 Oct 2026
  for 4982, 4984, 4992, 4999) carry every one of the six entries word for word, code words included, e.g. 4999: "Ingress the amount of
  rolling stock needed on Shylock road ... thirty engines and fifteen hundred cars none too many ... signed Andes". The ledger is the
  clear copy kept before transposition; only the arbitraries (names, places, a few nouns) are in code.
- **Image** (Huntington IIIF, 1800 px, scratch, not committed), crops pasted:
  `python3 tools/iiif_lines.py --image p4982.jpg --out crops --region 200,150,1450,680 --prefix v4982e1 --lines-per-crop 4`;
  `... p4982.jpg --region 200,1370,1450,650 --prefix v4982e3 --lines-per-crop 4`; `... p4999.jpg --region 190,110,1420,720 --prefix
  v4999e1 --lines-per-crop 4` and `--region 190,820,1420,330 --prefix v4999e1t --lines-per-crop 6`; `... p4999.jpg --region
  190,1050,1420,230 --prefix v4999e2`; `... p4984.jpg --region 210,1180,1420,560 --prefix v4984e3 --lines-per-crop 8`; `... p4992.jpg
  --region 220,220,1420,230 --prefix v4992e1`.
  Word for word, head to tail: **4999.1** (the longest, 14 ledger rows), **4982.1** (8 rows), **4982.3** (9 rows): all agree with the
  transcription. One plain-word detail: 4999.1's "signed" before Andes is faint and struck through on the image (the transcription keeps it;
  plain, ungraded). **Every M token re-read**: Myrtle, Mary (4982.1), Camden (4982.3), Ingress (4999.1, 4992.1), jolly (4999.2), Anthon,
  Humboldt x2 (4984.3): all written as transcribed; 4984.3's struck "lose" confirmed. LS3-R62's "0 slips" stands.

### 2. Two entries are in print: OR ser. I vol. 52 pt 1 (Supplement)
IA full-text search (be-api fts, positive controls "why could not a gunboat run up" -> 196 items incl. OR, "retain the Ohio battery" ->
OR 53) hit vol. 52 pt 1, which was **not** in LS3-R62's 13-volume re-grep. Confirmed by script on `warofrebellion521unit_djvu.txt`:
| entry | print | how confirmed |
|---|---|---|
| **4982.3** McClellan to Buell, 14 Feb 1862, 11 PM | **OR I/52 pt 1 p.211** (between running heads 210 and 212): "Washington, D. C., February 14, 1862. General Buell, Louisville, Ky.: Telegraph me in cipher, and much detail, the position of your troops, also your intentions. Where is Thomas, and where is Carter? Where is your advance on the Bowling Green line? What force did you wish to take to the line of the Cumberland? Write fully. Geo. B. McClellan." | word for word but "do"/"did" and the clerk's "Telegh"; the print witnesses Camden = **Thomas** and Sermon = Bowling Green on 14 Feb (C), lifting the one M of this entry. **N1.** |
| **4999.2** McClellan to Buell | **OR I/52 pt 1 p.214**, printed under **18 Feb 1862**: "Brig. Gen. D. C. Buell, Louisville: What news have you? What of Nashville and Clarksville? G. B. McClellan." | word for word; the ledger head reads Feb 19 (image); the tail "jolly wants Boyle dine with him" is the operator's service note, not in print. **N1.** |

**4982.1 parallel confirmed, not the telegram**: OR I/7 p.612, Headquarters of the Army, 14 Feb 1862, McClellan to **Buell**: "Please inform
me as soon as possible what re-enforcements have been sent from your command in Kentucky to the expeditions up the Cumberland and
Tennessee; also what have been sent by you from other States. Ten thousand muskets have been ordered to Columbus, Ohio." 4982.1 goes to
Halleck (Alden), asks for the number sent up the rivers with Grant and what has gone from Halleck's own department as well as from
Buell's; a sister telegram of the same hour, different recipient and wording. Context only (it supports Myrtle/Mary = the Cumberland/
Tennessee rivers on 14 Feb but does not witness them). Also context for 4999.1/4992.1: OR I/7, McClellan to Scott, 20 Feb 1862,
"Increase rolling stock on Nashville Railroad"; Buell to McClellan 15 Feb, "We need rolling stock greatly" -- neither is either entry.

### 3. Entries not located: search families (8 Oct 2026)
| family | searched | result |
|---|---|---|
| OR ser. I, whole-volume grep (IA djvu, scratch) | vol. 7 (`warofrebellionco0007vari`) and vol. 52 pt 1 (`warofrebellion521unit`; `warofrebellionco52p1unit` answers 401) for each entry's phrases; the reader's 13 volumes (5, 7 x2, 8, 9, 10 pt1-2, 11 pt1/3, 12 pt1/3, 51 pt1, 53) by 6-gram | 4982.3, 4999.2 located (above); 4982.1, 4999.1, 4984.3, 4992.1 not located |
| IA full text, all items (be-api fts, quoted) | 4982.1 "number of troops sent up the Cumberland", "what reinforcements have since been sent from your", "states in his department north of the Ohio", "Cumberland and Tennessee with Grant", "what from Buell's command"; 4999.1 "thirty engines and fifteen hundred cars", "move at one time thirty thousand troops", "rolling stock needed on the Nashville", "prepare for stocking other roads"; 4984.3 "keep a close watch of affairs at New Creek", "Lander was seriously ill", "does not expect him to live" Lander, "Surgeon Suckley" Lander; 4992.1 "not less than ten engines", "engines and cars on the Nashville", "three or four hundred cars" | 0 relevant (hits only on unrelated railway/explorer texts) |
| Google Books API (key, country=US) | the six strongest phrases above (4 answered 503 once, retried once) | no hit on any entry (snippets are other OR passages) |
| OpenAlex / Semantic Scholar / CORE (keys) | one query each (McClellan Scott Nashville rolling stock 1862; McClellan Lander Rosecrans New Creek telegram 1862; "number of troops sent up the Cumberland") | OpenAlex 12 results, none relevant; S2 and CORE returned no result body (one try, not retried) |
| Holding archive | Huntington CONTENTdm page records 4982, 4984, 4992, 4999 | **the clear text of all six is public there** (section 1) |
| JSTOR | 2 rows appended (4982.1, families i and ii) | pending (never blocks) |
| Unread / unreachable | McClellan's papers (Sears, *Civil War Papers of George B. McClellan*, 1989, not online); Lander papers; NARA RG 107 (M473); OR ser. III vol. 1; 1862 press; HathiTrust full text | unread |

### 4. Classification and depth
Cipher tokens are the code words only (LS3-R62's grades, H/C/S/M/I); plain words are not cipher tokens.
| entry | N-class | text known? | key | depth | code tokens (C/M/I) | one line |
|---|---|---|---|---|---|---|
| 4982.1 McClellan (Andes) to Halleck (Alden), 14 Feb 1862, 2 PM | **N3** | clear frame public (Huntington); code words' meanings not located in print | ours (+ published for Andes/Alden/Alvord) | **D1** | 7/2/1 | see below |
| 4982.3 McClellan to Buell, 14 Feb 1862, 11 PM | **N1** | known: OR I/52 pt 1 p.211 | ours / published | D1 | 4/1/1 before; Camden now C from the print | six isolated name/noun substitutes in clear text; no clause |
| 4999.2 McClellan to Buell, ledger 19 Feb (print 18 Feb) 1862 | **N1** | known: OR I/52 pt 1 p.214 | ours / published | D1 | 3/1/0 | three name substitutes, a two-question telegram; no clause |
| 4999.1 McClellan to Thomas A. Scott, 19 Feb 1862 | **N1** (D2V-E74 shape) | known: Huntington public transcription, clear body | ours / published | D1 | 2/1/0 | the sense (rolling stock for 30,000 men, 30 engines, 1,500 cars) is read from the clear page, not the key |
| 4992.1 McClellan to Scott, 16 Feb 1862 | **N1** (D2V-E74 shape) | known: Huntington public transcription | ours / published | D1 | 3/1/0 | names only in code (Scott, Buell, Nashville, signer); sense clear on the page |
| 4984.3 McClellan to Rosecrans, 2 Mar 1862 | **N1** (D2V-E74 shape) | known: Huntington public transcription | ours / published | D1 | 1/3/0 | names only in code (Anthon, Humboldt x2, Andes); sense clear on the page |

- **4982.1, depth.** The brief's "seven code tokens" is LS3-R62's C count; the entry carries ten code tokens (C 7, M 2, I 1). Under the bar:
  (a) cipher clause -- the code tokens are isolated arbitraries interleaved with clear words, each an independent substitute fixed by a
  witness outside this entry; the two M rivers break the run, and the longest C run (Bremen/Grant, widow/reinforcements, Alvord, legend/
  Kentucky, Koran/Ohio, Andes) is six independent name/noun substitutes, which constrain no key beyond themselves, so no stretch exceeds
  the authentication distance; (b) code clause -- no code value occurs twice inside the entry, and the bar does not let a value's C grade
  (its witness in another telegram's print) count as the second context. **D1.** A content sentence would also rest on the two M rivers
  (supported only by the OR 7 p.612 parallel, which may confirm, never supply). Not a counted solve; per the lane brief no status.json
  row and no SO row (N3 as a text at D1, the LS-V7 E74 handling). If the lane or parent holds that CLAUDE.md's "N3 -> SO row" applies
  regardless of depth, the row is theirs to add.
- **The other five: none reaches D2.** 1-6 code tokens each, all names/places/one noun in otherwise clear text, no repeated value inside an
  entry, no clause; two are in print and three are clear on the holding archive's own record.
- **Safe sentence (4982.1)**: "A 14 Feb 1862 telegram from McClellan to Halleck in the mssEC 15 sent ledger, clear apart from ten code
  words, seven of which read at grade C with the 1862 key rebuilt from print; its clear text is in the Huntington's public transcription,
  and no print of the telegram was located in the Official Records (incl. ser. I vols. 7, 52 pt 1), Internet Archive full text, Google
  Books, OpenAlex, Semantic Scholar or CORE (searched 8 Oct 2026)." Unsafe: "unknown telegram", "first", "previously unread", any
  depth word above "fragments read".
- Safe sentence (the five): "Mostly clear telegrams of Feb-Mar 1862 whose few code words (names, places) read with the 1862 key; their text
  is public in the Huntington transcription, and 4982.3 and 4999.2 are printed in OR ser. I vol. 52 pt 1, pp. 211 and 214."

### 5. Postmortem
- **Missed print**: LS3-R62's pre-filter grepped 13 OR 1862 volumes but not ser. I vol. 52 pt 1 (the Kentucky/Tennessee Supplement), where
  McClellan-Buell telegrams of Feb 1862 not printed in vol. 7 appear; 2 of the 6 "0-hit" entries are there. Any residue re-grep should add
  vol. 52 pt 1 (and ser. III vol. 1 for the Scott railroad traffic). NOTES.md corrected (line under LS3-R62).
- **Text-known shape**: entries whose only code words are names/signatures fall under D2V-E74 (N1, the holding archive's public
  transcription); the residue's mostly-clear entries should be pre-sorted on this before any further verifier time is spent on them.
- `tools/depth_check.py` (8 Oct 2026, after this section): "unique solves (N3+ and D2+): 52 -- D4 5, D3 28, D2 19; not counted D0/D1: 12"; no eckert-1862 row added (no N3+ D2 item). `tools/gaps_check.py eckert-1862`: "OK keep-going".

## AUDIT 2 (second adversarial, V1-1862)

Verifier V1-1862 (account 3, LANE-VERIFY-1, session_01HdWByoLSWN9ZvDVZzWL2wX), 8 Oct 2026, 16:10-16:2x UTC by `date -u`. A session
separate from every reader (GAPS110-171, LS3-R62) and from both first auditors (VERIFY-ECK, account 4, 3 Oct; LS3-V62, account 2, 8 Oct),
not protecting their conclusions. Items: **4992.3** (McClellan to Buell, 16 Feb 1862, the N3 for "Sermon = Bowling Green", queued as
SO-ECK-4992) and **4982.1** (McClellan to Halleck, 14 Feb 1862, 2 PM, N3 D1). Nothing decoded; no `--check` re-run (no input changed since
LS3-V62's and VERIFY-ECK's runs). Families the first audits did not cover were searched first, then G3 on the decoded wording.

### 1. Prior-work checks 3-5 (`tools/prior_work.py` does not exist; checklist by hand)
| check | route, query | result |
|---|---|---|
| 1 own work | grep 4992/4982 in AUDIT.md, NOTES.md, status.json, PROGRESS.tsv, VERIFY-BACKLOG.tsv, SECOND-OPINIONS-QUEUE.tsv | two first audits (above); SO-ECK-4992 queued 3 Oct; no status.json result row and no PROGRESS row for either item |
| 3 holder | Huntington CONTENTdm `dmGetItemInfo/p16003coll11/4992` and `/4982`, field `transc` (2 requests) | **both entries' clear text is public**, code words in place: 4992 "For Alvord give me distribution of your troops how many in sermon line and where placed ... everything about rebels Andes"; 4982 "Alden Please inform me ... sent up the Myrtle & Mary with Bremen what widow have since been sent ... from Alvords Command in legend ... North of the Koran Andes Sarah". Same page 4982, entry 3 (11 PM): "where is your Whig on the **Sermon line**" |
| 3 solver blog | Decoding the Civil War blog, WordPress public API, **all 154 posts fetched and grepped** (not the site search): sermon, bowling green, distribution of your troops, number of troops sent, myrtle, widow | "sermon" 0; Myrtle 0; widow 0; "bowling green" once ("Bickering Generals", 18 May 2017, clear prose about McClellan urging Buell, no code word). VERIFY-ECK read three posts and ran 12 site searches; this is the full corpus |
| 4 edition, sender | *McClellan's Own Story* (1887), IA `cu31924030917391` djvu, whole-text grep of both entries' phrases | not present (the one hit, "no matter how long", is about his horse Dan) |
| 4 edition, sender | Sears, *Civil War Papers of George B. McClellan* (1989), IA `civilwarpapersof0000mccl`, be-api fts restricted to the item; positive control "Buell" -> hit (Dec 1861 letter to Buell) | "distribution of your troops" 0; "number of troops sent" 0; "no matter how long" 0; "sent up the Cumberland" 1 = the Jan 1862 letter to Halleck (OR 7 p.527 text), not 4982.1; "exact state of affairs" 1 = a McClellan letter ("can then tell you the exact state of affairs, & the time when I shall probably reach"), not 4992.3. "Bowling Green line": 502, one retry not spent on it (two other 502s that minute) -- unchecked |
| 4 OR ser. I | vol. 52 pt 1 (`warofrebellion521unit`; **not searched by VERIFY-ECK for 4992.3**) and vol. 7 (`warofrebellionco0007vari`), whole-text grep, plus every 14-18 Feb 1862 McClellan-Buell and McClellan-Halleck telegram listed by script | neither entry printed. Positive control: OR 52.1 p.211 (4982.3, LS3-V62) found by the same grep |
| 5 G3 same-day / replies | OR 7 telegrams of 14-17 Feb read in full (list above) | **4992.3: SUBSTANCE, diffed**: OR 7 pp.620-621, "February 16, 1862--11 a.m. Brig. Gen. D. C. Buell, Louisville, Ky.: Give me in detail your situation and that of the enemy. Whither did he go from Bowling Green? I wish the position of things in full. Geo. B. McClellan", and Buell's reply the same day, "My dispatch of yesterday gives in detail the position of my troops ... converging on Bowling Green". Same day, same parties, same request in substance, but a **different telegram**: no shared wording beyond "give me" ("distribution of your troops", "how many in [Bowling Green] line", "all other lines", "no matter how long a telegram it requires", "everything about rebels" are all absent). 4982.1: Buell's 14 Feb 6 PM answer to the sister telegram (OR 7 p.612) and Halleck's 15 Feb 11 AM ("I have only about 30,000 men in the field, but am pushing forward re-enforcements") answer in part; neither is 4982.1 |
| 5 G3 phrase re-search | IA be-api fts, all items: "sermon line" (331, all homiletics/T. S. Eliot), "Sermon = Bowling Green" (32, church notices), "exact state of affairs and everything" 0, "number of troops sent up the" (10, all Illinois colonial-trade texts), "Myrtle & Mary" (personal names only); "how many in sermon", "everything about rebels", "sermon line" McClellan: 502 twice (one retry each) -- unchecked | no relevant hit |
| 5 G3 Google Books | API with key and country=US, 7 queries ("sermon line" Buell; "Sermon" "Bowling Green" telegraph cipher McClellan; "how many in sermon line"; "everything about rebels"; "number of troops sent up the Cumberland"; Myrtle Mary Cumberland Tennessee cipher telegram; "Eckert" ledger "Sermon") | 0 relevant (loose matches: sermons, OR 7 passages already read, a 1990 book on denim) |
| 5 G3 press of the day | Chronicling America through loc.gov JSON API, 13-22 Feb 1862, 3 queries | **403 on all three; stopped (good-citizen rule) -- unchecked**. Low prior: these were War Department cipher telegrams, but the press stays unread |
| not searched | OR ser. III vol. 1 (Scott railroad traffic; not either entry's subject), Buell papers, NARA RG 107 (M473), Zooniverse Talk (no keyword search), JSTOR (no row: a one-code-word item) | unchecked |

Requests: archive.org download 3, advancedsearch 2, be-api 16 (6 answered 502), Huntington CONTENTdm 2, public-api.wordpress.com 5,
googleapis.com 7, loc.gov 3 (403). One at a time, >= 1.5 s apart.

### 2. Findings
- **Sermon = Bowling Green is readable from two public sources without our key.** The Huntington's own transcription of 4982 entry 3 has
  "where is your Whig on the Sermon line", and OR ser. I vol. 52 pt 1 p.211 (1898) prints that telegram as "where is your advance on the
  Bowling Green line?" (LS3-V62 found the print; it did not draw this consequence for 4992.3). The *meaning* of the code word, for the token
  of 14 Feb, is therefore in print against a public transcription -- the N2 shape (plaintext known elsewhere, no prior mapping of the code
  word to it found). No one was found to have written the mapping down (DCW blog full corpus, Google Books, IA full text). The value is
  correct beyond doubt: it now has a fourth witness two days before 4992.3, on the same McClellan-Buell line. key.md's row cites OR 7
  pp.584, 624, 626 only; adding OR 52.1 p.211 is the solver lane's job, not done here.
- **4992.3 as an entry.** Its clear frame is public (Huntington); its three code words are Alvord and Andes (published, DCW 2017) and
  Sermon. Its own text -- "how many in [Bowling Green] line" -- was found in no print; the nearest print is the different 11 a.m. telegram
  of the same day (OR 7 p.620). So the N3 stands for one thing only: no prior decipherment of this entry's one unpublished code word was
  located. It is not a newly found telegram (the text is public) and not a newly recovered key value (the value is printed against a
  public transcription two days earlier).
- **4982.1 as an entry.** Confirmed as LS3-V62 left it: clear frame public, ten code tokens (C 7, M 2, I 1), no print of the telegram in
  OR 7, OR 52.1, *Own Story* or Sears; the sister telegram to Buell (OR 7 p.612) and Halleck's 15 Feb reply are context only.

### 3. Classes and depth (depth bar .claude/briefs/runs/2026-10-08-acct3-depth-bar.md; kept or lowered, never raised)
| item | N-class | key | depth | code tokens | change |
|---|---|---|---|---|---|
| 4992.3 McClellan to Buell, 16 Feb 1862 | **N3**, scoped: the entry's reading of Sermon; clear text N1 (Huntington), Alvord/Andes published; the code-word *value* itself N2 (OR 52.1 p.211 against the public transcription of 4982.3) | ours (Sermon, from print alignment), published (Alvord, Andes) | **D1** (first depth ruling for this item: three isolated name/place substitutes in clear text, no clause, no value read in two contexts inside the entry; D1 is the honest ceiling) | 3, all C | class kept; scope narrowed; depth set |
| 4982.1 McClellan to Halleck, 14 Feb 1862, 2 PM | **N3** (kept) | ours (+ published for Andes, Alden, Alvord) | **D1** (kept) | 10 (C 7, M 2, I 1) | none |

- **Safe sentence (4992.3)**: "A 16 Feb 1862 telegram from McClellan to Buell in the mssEC 15 sent ledger, public in the Huntington's
  transcription, asks how many troops are on the 'Sermon' line; Sermon reads Bowling Green, a value also witnessed by OR ser. I vol. 52 pt 1
  p.211 against the same ledger's 14 Feb entry. No print of this telegram and no earlier statement of the code word's meaning was located
  (searched 3 and 8 Oct 2026)." Unsafe: "an unknown telegram", "a newly recovered code word", "first decipherment", any depth word above
  "fragments read".
- **Safe sentence (4982.1)**: LS3-V62's, unchanged, plus "and in neither McClellan's Own Story nor Sears's Civil War Papers (8 Oct 2026)".
- **status.json / PROGRESS.tsv**: no result row exists for either item and none is added (N3 at D1 is not a counted solve, the LS3-V62 and
  LS-V7 E74 handling). **SO-ECK-4992**: the class does not move, so the row is left as queued; its prompt already asks about OR 52 pt 1,
  and a second-opinion runner checking it will find p.211 on its own. Recommend (not done, prompt edits are the lane's): add one line to
  the prompt naming OR 52.1 p.211 so the runner tests the narrowed claim.

### 4. Postmortem
- VERIFY-ECK (3 Oct) cleared 4992.3 without OR 52 pt 1 and without reading the same-day OR 7 telegrams to Buell; LS3-V62 (8 Oct) found
  OR 52.1 p.211 for 4982.3 but did not carry its Sermon witness to 4992.3. The N3 survives, narrower: an N3 resting on one code word needs
  the check "is this word's meaning already printed against a public clear copy elsewhere in the same ledger?" before the class, which a
  grep of the holder's transcription for the code word plus the print of each hit answers in two requests.
- Unreachable this session (re-run before outreach): Chronicling America press (403), three be-api phrase queries (502), Sears for
  "Bowling Green line" (502).
