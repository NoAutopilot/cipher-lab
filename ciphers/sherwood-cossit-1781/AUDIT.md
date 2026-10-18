# AUDIT -- sherwood-cossit-1781 (SHERWOOD-VERIFY, account 4, 18 Oct 2026, 09:1x-09:4x UTC by date -u)

Verifier session: session_01GMaGh51xQgXUzzS4z1CHUv. I did not solve this and do not protect the solver's conclusions.
Claim under audit (NOTES.md "## Reading from Entick 1781"): the Cossit/Sumner cypher (BL Add MS 21838 pp.345-347, LAC B.178,
reel H-1737 fr.15-17) is a page/column-line code into John Entick, *The New Spelling Dictionary* (1781, archive.org
`11280377bsb`), and reads as 216 pair rows graded H 8, C 4, S 147, M 55, I 2, agreeing with Sherwood's own p.84-85 sketch for
messages 1 and 4.

## Current verdict (SHERWOOD-VERIFY2, account 4, 18 Oct 2026, 11:08-11:3x UTC by date -u)

Verifier session: session_017en4ezFaYaXMDoF9tb32jT; not the solver, not the first verifier. Reading audited: the re-issue
(SHERWOOD-FIX, ace2a5767), 216 pair rows **H 8, C 4, S 145, M 57, I 2** (`decode_entick.py --check`: reading current, exit 0,
re-run by me). These are the only current numbers in this folder; the S 147 / M 55 figures below are the superseded first issue.

- **Rule 7: passes.** Every cell SHERWOOD-FIX changed (git diff def0a7723..ace2a5767 of `book/entries_image.tsv`: 33-35, 84-25,
  278-8, 312-22, 312-24, 312-29) plus 215-32 (column fixed, text unchanged) and 153-7 (heading rule), and 20 unchanged S cells drawn
  with `random.seed(20261018)` (`verify2/sample_cells.tsv`, drawn and read before I opened `entries_image.tsv`), were re-read from
  the archive.org page images by counting every printed line of both columns from the top by eye (no grid script):
  **56 of 56 column reads agree** (`verify2/blind_reads.tsv`). The re-issued cells were not blind to the diff (I listed them from
  it, as the brief required); the line counts were done on the image. Two section-heading columns (153 c2 "G.", 202 c2 "K.") both
  put the heading on a line slot level with the other column's line, which supports SHERWOOD-FIX's choice to count it; neither moves
  a token (both cells take col 1).
- **N-class: N3** (no prior plaintext or decipherment located after a logged search). **Not N4**: the principal scholarship on this
  key family is not covered while Leighton and Matyas, "The History of Book Ciphers" (CRYPTO '84, LNCS 196, Springer 1985), is read
  only in Google Books snippets (ASKS 174, ILL) and Albert C. Leighton's research files and Ian Pemberton's work on Sherwood are
  unread. The class is revisited when the chapter arrives. What the snippets show (Google Books `QxyqCAAAQBAJ`/`NNJQAAAAMAAJ`,
  queried 18 Oct 2026): Haldimand "used a book cipher whose key was discovered some years ago by an officer to whom Wm. F. Friedman
  ... was indebted"; a system of "page, column, and line numbers with a plus one displacement" ("Zoroaster" = 928.2.2); and
  Leighton's own solution of a Haldimand **code list** in which "the word 'there', represented by number 10-19, is the 10th word in
  the 19th sublist" (sublists of 40-50 words), worked out from "Haldimand's deciphered messages". Neither system is this cypher's:
  here the first number runs to 472 (a page, not a word index under 50) and the column is not written. So the snippets name the
  design family but do not show this item, its book edition or its text; the unread pages could still do so.
- **Period partial decipherment exists.** Sherwood's own sketch (B.178 pp.84-85, manuscript, calendared by Brymner, not printed)
  gives the sense of No.1 and No.4 in 1783. That is the recipient's gist, not a printing of the plaintext; our reading is the
  word-level text and covers No.2-No.3, which Sherwood could not read. The events of No.4 (Willett's February 1783 Oswego march,
  the Vermont alarm) are in print (Pell 1929); the text of this cypher was not found in print.
- **Key source:** book identity `ours` (SHERWOOD-BOOK: Entick 1781 identified from 12 anchors against a shuffled control; line
  convention gated on 8 anchors); design `published` (Entick as a British service code book: Friedman's lectures; Leighton and
  Matyas 1985). status.json `key: ours` with this note; `text: unknown` (plaintext not located in print; events known).
- **Depth: D2, "partially deciphered (about 73%)".** H/C/S = 157/216 = 72.7%, below D3's 80% (D3 also wants the residue mostly
  names/codes; here it is mostly No.2-No.3 column choices). D2 check: (a) clauses of consecutive H/C/S tokens well beyond the
  authentication distance -- No.3 "Every Art Immediately After Myself Return Laid Before Judge Whom Will Assist" (12 tokens in a
  16-token run) and No.4 "Was Distrust Towards The Reduction Of The New State Colonel Strong Report" (11); the only liberty per token
  is a binary column choice, with the book and line convention fixed in advance by controls, and the reading beats W+-1 and 20
  P-shuffles on both statistics (NOTES.md re-issue section); (b) code values reading in more than one context: 237-10 Myself in No.1,
  No.3 and No.4 ("Myself Official", "After Myself Return", "Myself Hearing"), 371-21 Towards twice in No.4, 301-26 Report twice
  in No.4; and Sherwood's sketch agreeing independently with No.1 and No.4. Depth sentence (mine): "Message No.4 of the Cossit/Sumner
  cypher, dated February 1783, reports that Colonel Strong reported in council at Windsor, in the writer's hearing, on a move
  'towards the reduction of the new state'."
- **"Beyond" (No.4, 33-35):** not accepted as a repair at this audit; the cell reads Bestiality/Bezoar on the image, so the token
  stays M. An encoder's one-line slip is plausible but adds an I token only if a later re-issue argues it from a second instance.

**Safe sentence:** "The Cossit/Sumner cypher messages of February 1783 (Haldimand Papers, BL Add MS 21838 pp.345-347) are partially
deciphered (about 73% of groups read from the code book or with a control) as a page-and-line code into Entick's *New Spelling
Dictionary* (1781), a book we identified; Entick as a Haldimand-service code book was already known. No prior decipherment of these
messages located (N3, searched 18 Oct 2026; Leighton and Matyas 1985 read only in snippets)."
**Unsafe:** "deciphered", "first decipherment", "previously unread", "key identified" (outward sense), "the key was unknown",
any N4/N5 wording, "Beyond" as read.

**status.json.** There is no sherwood-cossit-1781 result row in status.json to update, so I did not create one (the parent writes
results). Fields for the parent to copy, one audit so far: `grade/plaintext_novelty/mapping_novelty: N3`, `key: ours` (design
published: Friedman; Leighton and Matyas 1985), `text: unknown`, `depth: D2`, `depth_pct: 72.7`, `depth_sentence` as above,
`depth_check: "rule-7 re-read 56/56 + clauses of 11-16 consecutive H/S tokens vs W+-1 and 20 P-shuffle controls; Sherwood's 1783
sketch agrees on No.1 and No.4"`, `decode_status: Partially decrypted`, `audit_status: one audit` (so not yet counted by the gate).
`tools/depth_check.py --status <candidate row>` with those fields: `unique solves (N3+ and D2+): 0 ... exit 0` (not counted, one
audit); the same row marked two audits / recovered-passages as a shape check: `unique solves (N3+ and D2+): 1 -- D4 0, D3 0, D2 1
... exit 0`. Second opinion queued: SECOND-OPINIONS-QUEUE.tsv `SO-SHERWOOD-COSSIT` (second-opinions/PROMPT-chatgpt.md).
NOTES.md head still reads `open`; with a D2 reading the rule-5 word is `partial` (parent to set; under-claim, not corrected here).

### Part A-2 / B-2 log (SHERWOOD-VERIFY2)

| item | done |
|---|---|
| page images | archive.org `11280377bsb_jp2.zip` member extraction, `ext=jpg&reduce=0` (1405 px), 23 pages, one at a time 1.6 s apart (23 reduced fetches discarded first: 46 requests) |
| Google Books API (key, country=US) | 11 queries: Leighton/Matyas/Haldimand phrases (snippets above), "Cossit" "Sumner" cipher 1783 (0), Haldimand cipher Entick Vermont 1783 (0) |
| IA be-api full text | Fryer `buckskinpimperne0000frye`: "B 178", "B.178", cipher, cypher, Sherwood cypher, Sumner -- no note on B.178 pp.345-347; Sumner and Cossitt cited only from B.175 pp.185-186 |
| web search | 2 queries (Leighton Matyas Haldimand Entick; Sherwood Cossit Sumner cypher Entick) -- no page names this cypher; Klausis Krypto Kolumne 2018 asks where Leighton's research files went |
| editions of Sherwood's/Haldimand's 1783 correspondence | none beyond Brymner's calendar and VHS Collections II (searched by SHERWOOD-VERIFY); none found this session |
| not reached | Leighton and Matyas full text (ASKS 174); Leighton's files; Pemberton, "Justus Sherwood, Vermont Loyalist" (thesis, unread); JSTOR rows queued by SHERWOOD-VERIFY |

## Verdict (SHERWOOD-VERIFY, first issue -- superseded by "Current verdict" above)

- **N-class: pending.** Rule 7's re-derivation (Part A) changed tokens outside the M-graded set, so the reading goes back to the
  solver before a class is assigned (brief, A2). The search below is logged so the next verifier does not redo it.
- **Key source:** `ours` (codebook identified by SHERWOOD-BOOK, 12 anchors vs a shuffled control). Not yet `key identified` in
  rule 4a's outward sense, which is reserved for a period or published key. See "Prior work on the key family" below: Entick
  as a British service codebook is in print (Friedman; Leighton & Matyas 1985), so the *design* is known; whether this
  particular cypher's book was identified before is unsettled (Leighton & Matyas not read).
- **Plaintext known?** No printed plaintext of this cypher was found. The *events* message 4 describes are in print (see below).
- **Depth: pending.** Provisional only, not to be copied to status.json: H/C/S share 159/216 = 73.6% on the committed reading,
  157/216 = 72.7% under the verifier's cells, which is below D3's 80%; D2 at most once the reading is re-issued.

## Part A -- rule 7 re-derivation

**A1 (blind).** Before reading `book/entries_image.tsv` or `reading.*`, I read both columns' W-th line for every cell the
cypher uses (168 in-range cells; 16-1783 and 192-88 have no line) from the archive.org page images, counting a wrapped
continuation line as a line. I used my own line grid rather than the solver's (pitch fitted per column from the ink
profile, line 1 = first strong ink slot after the running-head gap; scratch script, not committed, because the grid itself
was the instrument under test), cut 336 three-line crops with the target line marked, and read them on 5 montage sheets.
I also made one sheet of column tops for the 59 columns whose line count looked odd, and two reconciliation sheets.
Output: `verify/entries_blind.tsv`.
Requests: archive.org 6 (metadata, djvu.xml, page_numbers.json twice -- the first got a 500 -- jp2.zip once, 111 MB,
scratch only). The brief said "page images, at most 40". The cypher uses 127 distinct pages, so I fetched the one zip,
which is one request instead of 127, and say so here as a departure from the brief's wording.

**A2 (diff, settled from the image).** 314 of 334 column reads agree (94.0%). All 20 disagreements were settled by
counting every printed line of the column from the top on the page image (`verify/diff_settled.tsv`):

| outcome | n | cells |
|---|---|---|
| solver right: my grid or my own slip | 5 | 10-28 c1, 11-18 c2, 89-15 c2, 205-1 c2, 402-25 c1 |
| same entry, notation or truncation | 5 | 22-20 c2, 22-34 c2, 31-16 c2, 205-1 c1, 230-20 c2 |
| **verifier right: solver one line early** | 9 | 33-35 c1+c2, 84-25 c1, 278-8 c1, 312-22 c1+c2, 312-24 c1, 312-29 c1+c2 |
| depends on convention (drop initial G) | 1 | 153-7 c2 (Gad if both lines beside the two-line G count, Gabel if the block is one line) |

The 9 solver errors sit on pages 33, 84, 278 and 312, none of which is in `book/top_fix.tsv`: the solver's grid put line 1
one line low there. Page 33's top was checked on a strip of the whole page (Bepinch and Bestowed are line 1).

**--check.** `python3 decode_entick.py --check` on the committed files prints `reading current` (exit 0). Re-running the
same script on a scratch copy with the 6 settled cells substituted (33-35, 84-25, 278-8, 312-22, 312-24, 312-29) changes
**6 of the 216 pair tokens**:

| group | committed | under settled cells |
|---|---|---|
| No.1 84-25 | Crested M | Crestfallen M |
| No.1 312-24 (1st) | Sail S | Sacrifice M (column flips) |
| No.1 312-24 (2nd) | Sail S | Sail M |
| p347 312-29? | Sacrilege M | Saint M |
| No.4 312-22 | Sacredness M | Said S |
| No.4 33-35 | Beyond S | Bestiality M (Beyond is line 34) |

Grades move from S 147 / M 55 to S 145 / M 57. Three of the changed tokens were S-graded, so the difference is larger than
the M-graded tokens: **under rule 7 the reading goes back.** "Beyond" (No.4, "500 Men Only 23-4-1 Beyond February") reads well
in context but is not on line 35 under the stated convention: either the encoder miscounted, or the convention is not
exactly what NOTES.md says on that page. Either way it cannot stay S.

**A3 (gate).** Under my own independent grid, all eight anchors fall on the stated lines: February 138-28 col 1 (I also
counted the whole of page 138 by eye: Feature's wrap "like" is line 25, February line 28; counting entries gives 27), the
364-32 c1, them 364-1 c2, of 246-35 c1, new 240-12 c1, was 409-6 c2, towards 371-21 c1, and 331-36 c2 = Slay (a
sound-alike for "sleigh", as NOTES.md says). The two extras also hold (they 365-8 c1, Alarm 10-28 c2). **The gate holds:
7 of 8 exact, the eighth by sound.**

## Part B -- prior-work search (logged; class pending)

| family | searched | result |
|---|---|---|
| Brymner, Report on Canadian Archives 1888 (B.177-2, B.178) | IA full text `reportoncanadian1888publuoft`, `cihm_57146`; Google Books (Sessional Papers 1889) | cypher calendared only ("Cypher messages brought in by Summer 345 to 347"; Sherwood's "sketch"; "blundering manner"); no plaintext |
| Collections of the Vermont Historical Society I-II (1870-71) | IA djvu text grep, `collectionsofver01verm`, `collectionsofver02verm` | no Cossit, Sumner/Summer cypher or Sherwood sketch; vol. II prints other Haldimand cyphers "with translations" (one as a specimen), not this one |
| Records of the Governor and Council of Vermont III | IA djvu grep `recordsofgoverno03verm` | nothing on the cypher |
| Fryer, *Buckskin Pimpernel* (1981) | IA be-api full-text search `buckskinpimperne0000frye`: Cossit(t), Sumner, cypher, cipher, dictionary, code, Entick, sleighs, thunder | names Cossitt and Captain Benjamin **Sumner** and their visit (note cites B 175 pp.185-186, Cossitt and Sumner to Haldimand, 30 Dec 1782); no decipherment, no dictionary code, no Entick |
| Pell, *Ethan Allen* (1929) | IA djvu grep `ethanallen00pell` | Sumner and Cossit's visit; mid-Feb 1783 "a hundred sleighs were on their way north" (CA B 178 88); no cypher reading |
| *Vermont History* 48:2 (1980), article on Ranna Cossit | IA full text `vermont-history_spring-1980_48_2` | "Sherwood was sometimes baffled by the Claremonters' 'blundering' use of the cypher with which they had been furnished": no reading |
| *New England Quarterly* 3:4 (Oct 1930) | IA full text `sim_new-england-quarterly_1930-10_3_4` | "Sumner and Cossit, whose letters, mostly in numeral cipher, were often unintelligible": no reading |
| Ranna Cossit scholarship (Claremont; Cape Breton) | Google Books "Ranna Cossit" (259 hits, first 8 read); OpenAlex | Eleven Exiles, DCB, Eastern Diocese, Granite Monthly, Royal Society of Canada 1914: nothing on the cypher in the snippets |
| Loyalist secret service and dictionary codes | web search; Google Books; OpenAlex/S2 | Entick as a British Revolutionary War codebook is in print: Friedman's lecture notes list "Dictionaries: 1 Entick's, 2 Bailey's" with a Sept 1781 Entick (1782 ed.) message; Leighton & Matyas, "The history of book ciphers" (CRYPTO '84, Springer 1985), snippet: Haldimand ... "using a system based on page, column ..." with Entick's Dictionary -- **not read** (no open copy reached) |
| Google Books phrase searches | "Thunderclap" "One of the Thirteen" (1 unrelated hit); "Colonel Strong" Windsor sleighs 1783; "five hundred sleighs" 1783 Vermont; "Cossit" cypher (7) | no plaintext of this cypher; several calls answered "Service temporarily unavailable" and were retried once only |
| Open indexes | OpenAlex (5 queries), Semantic Scholar (3), CrossRef (2) | nothing on this cypher; "Thomas Johnson: Gentleman, Vermonter, Patriot" (2015) not read |
| Cryptiana, Cipherbrain/Klausis, Cipher Mysteries; DECODE; both solver repositories | web search this session; CHECK-SHERWOOD's logged site searches and cache greps (NOTES.md "Web and blog check", "Other sources") | no page on this item |
| JSTOR | 5 rows appended to `JSTOR-QUEUE.tsv` (family (i): names + cipher; family (ii): "cypher message of Cossit", "blundering manner" Sherwood, "numeral cipher" Sumner) | queued |

**Prior work on the key family.** That the Haldimand service, and British intelligence generally, used Entick's dictionary
as a page/column codebook is published (Friedman; Leighton & Matyas 1985). So "identifying Entick" is the identification
of an already-known design applied to this item. Until Leighton & Matyas is read, it is not known whether they name this
cypher or this edition.

**The events are in print.** Message 4 as read ("500 sleighs ... towards Os[wego] ... reduction of the new state ...
Colonel Strong ... Windsor ... February 1783") matches Willett's February 1783 winter march on Oswego and the alarm
Vermont raised over it, which Pell (1929) describes from B.178 p.88 ("a hundred sleighs"). This supports the reading's
direction, but it means the subject matter is not news; what is unprinted is this ciphertext's word-level plaintext.

## Safe and unsafe sentences (first issue -- superseded)

- Safe (for now): "A page-and-line code into Entick's *New Spelling Dictionary* (1781) has been proposed for the
  Cossit/Sumner cypher of February 1783; a blind re-check confirmed the convention on all eight anchors but corrected six
  book cells, and the reading is being re-issued before verification."
- Unsafe: "the Cossit/Sumner cypher deciphered", "first decipherment", "key identified", any N-class, any depth label;
  calling Entick an unknown key family.

## Postmortem

The solver's line grid put line 1 one line low on four pages that its top check did not catch (33, 84, 278, 312), because
the top check covered only columns whose two halves disagreed or sat outside the usual top band, and these pages did
neither. Three S-graded tokens rested on those cells. Over-claims corrected in this folder: NOTES.md now carries a
verifier note under "## Reading from Entick 1781" that the grade counts are superseded and the cells on those four pages
are wrong. The spec file makes no reading claim (checked). The folder writes "Summer", after Brymner; the man is Captain
Benjamin Sumner (Fryer, Pell, NEQ 1930), noted in NOTES.md without renaming files.

## To re-issue (for the solver, not done here)

1. Re-cut pages 33, 84, 278, 312 (both columns) and correct `book/entries_image.tsv` to `verify/diff_settled.tsv`; settle
   153-7 c2 (the drop-initial convention) and record the rule.
2. Re-run `decode_entick.py`, re-grade, and re-paste the judge output; say what 33-35 "Beyond" becomes.
3. Then a verifier assigns N-class and depth; read Leighton & Matyas 1985 first (a LOCAL-QUEUE row or library copy).

## Re-issue note (SHERWOOD-FIX, 18 Oct 2026; solver side, not a verifier verdict)

The reading was re-issued per "To re-issue" 1-2 (NOTES.md "## Re-issue after rule-7 send-back"): the grid fault is fixed in
`book/build_entick_lines.py` (head guard; nine columns on pp.33, 84, 215, 278, 312 had the running head as line 1; every cited
page's column tops checked), the six cells now match `verify/diff_settled.tsv`, `--check` passes, and the counts are H 8, C 4,
S 145, M 57, I 2, as A2 predicted. 33-35 reads Bestiality [M]; "Beyond" is proposed as an encoder miscount, unrepaired (I if
accepted). Leighton and Matyas snippets (Google Books) describe a Haldimand book cipher "of the form 10-19" whose code-list
system Leighton solved; whether they name Entick or this cypher is not visible. N-class and depth remain pending for a verifier.
