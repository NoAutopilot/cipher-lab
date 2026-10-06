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
