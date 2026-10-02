# AUDIT -- pro3055-clinton-1779, item 2894 (PRO 30/55/24/76)

Verifier VERIFY-CLINTON-2894, 2 Oct 2026 (clock read 08:10-08:2x UTC, `date -u`), account 2, for the owner-account
orchestrator. Brief `.claude/briefs/runs/2026-10-02-acct3-verify-clinton-2894.md`. A separate session from the
account-4 workers (GAPS, GAPS2, GAPS3, GAPS4) that produced the reading; this audit does not protect their
conclusions.

**Claim under audit:** "SP 2894 (Clinton correspondence 1779, PRO 30/55) is read from the period decipherment in
H-1649 p.186 (H 116, M 3; text known), key rebuilt H 297 C 18 from the 1778 Army List with 79/81 agreement with
Tomokiyo; a clause omitted from the printed decipherment reads 'Admiral A will be reinforced in proportion'
(preposition open)." (Note: the letter is dated 6 July 1780, not 1779; "printed decipherment" in the claim means
the manuscript decipherment on reel page 186, which the workers did not know to be in print -- see 2-3.)

## 1. Extract

| field | value |
|---|---|
| item | TNA PRO 30/55/24/76 (HMC/Discovery 2894; Discovery C16304855, digitised=false); recipient copy BL Add MS 21807 fos.159/161 = LAC Haldimand Papers B.147, microfilm H-1649 Images 827-829 (reel pp.184-186) |
| date, place | 6 July 1780, New York (endorsed received Quebec 5 Sept 1780) |
| sender -> recipient | Sir Henry Clinton -> Gen. Frederick Haldimand |
| system | book cipher on the title page of *A List of the General and Field Officers* (J. Millan, 1778): line-letter figure pairs, first figure omitted on repeats (key book identified by Leighton & Matyas, CRYPTO 1984 / LNCS 196, 1985; documented by Tomokiyo, Cryptiana haldimand.htm) |
| plaintext as read | `passes/p186_reading.txt` (119 tokens, H 116, M 3): "I have received your dispatches of Novr & January &c I have received Information from the Ministers of the 3d May Monsieur Terney is supposed to have sailed about the 3d May with seven ships of the line ... to Saint Johns, the other by the river Saint Laurence; -- H C 6th July / Copy." |
| ciphertext | `passes/cipher_reconciled.tsv`, 315 figure pairs + 47 clear entries (reel pp.184-185) |
| clause | `passes/clause_2894_1778.tsv`: "Admiral A will be reinforced in proportion", 32 tokens C 18 H 14 |
| what the solvers searched | NOTES.md "Web and blog check" (8 WebSearch queries, Cryptiana blog + comments, Cipherbrain, Cipher Mysteries, JAR comments, vermonthistory.org), HMC vols 2-3 page images (AX-HMC), Brymner Report on Canadian Archives B.147 (AX-HMC2), Stevens 1888, Google Books API, Discovery (2 Oct, saved to `discovery_clinton_to_haldimand_2026-10-02.tsv`) |

## 2. Independent search (2 Oct 2026)

| family | searched | result |
|---|---|---|
| (a) canonical series / catalogue | TNA Discovery API `records/v1/details/C16304855` (1 request), and the description already on disk in `discovery_clinton_to_haldimand_2026-10-02.tsv` row 14 | **hit.** Discovery's own scopeContent for this very cipher item: "... a French force had sailed around 3 May with seven ships of the line and 20-25 transport vessels ... 5,200 land force ... heading for Canada. **Admiral Arbuthnot will be reinforced in proportion.** Further intelligence indicates that the force will assemble at Rhode Island before making its way eventually to St John's by the St Lawrence River." |
| (b)(c) recipient's printed correspondence / documentary editions | Internet Archive full-text (be-api fts, 2 phrase queries) -> Historical Section of the General Staff (Canada), *A History of the Organization, Development and Services of the Military and Naval Forces of Canada ... with Illustrative Documents*, **vol. III**, "The War of the American Revolution: The Province of Quebec under the Administration of Governor Frederic Haldimand, 1778-1784" (Ottawa, printed April 1920 per the imprint "1,000 4-20"); archive.org `vol1t3historyoforganiz01quebuoft` (vols I-III bound; djvu text read) and `31761118534445` (Robarts copy) | **hit, decisive.** Illustrative Document **170**, p.158, "PUBLIC ARCHIVES OF CANADA. HALDIMAND PAPERS. Series B, Vol. 147, p. 183": the decipherment printed verbatim -- "I have received your dispatches of Novr & January & I have received Information from the Minister of the 3d May. Monsieur Ternay is supposed to have sailed about the 3d May with seven ships of the line & from 20 to 25 Transports &c., having on board five Thousand two hundred land Forces & that their destination is still supposed to be Canada, by Information I have received here the french Armament will assemble at rhode Island a division of which will proceed under the command of the Marquis de [Fa]yette by Connecticut River and No. 4 across the lakes to Saint Johns, the other by the river saint Lawrence. H. C. 6th July. Endorsed: From Sir H. Clinton 1780 6th July. Rec'd 5th Septr." Calendared in the same volume's table of contents as no.170. And Illustrative Document **181**, p.165 (B.149 pp.154-5), Francis McLean to Haldimand, Halifax 24 July 1780, reporting Clinton's letter: "supposed to have sailed about the 3rd of May and that **Admiral Arbuthnot will be reinforced in proportion**." |
| (d) holding archive pages | TNA Discovery (above); LAC/Canadiana reel H-1649 (the workers' own source) | as above |
| (e) Google Books | API, `country=US`, key from the environment (never printed), 3 queries: `"reinforced in proportion" Arbuthnot Haldimand` (0), `"supposed to have sailed about the 3d May"` (291 loose, none this letter in the top 5), `"Marquis de Fayette by Connecticut"` (350 loose, none this letter in the top 5) | no hit (the API does not honour the quotes; IA fts found the print) |
| (e) web phrase search | WebSearch `"Arbuthnot will be reinforced in proportion"`; `"Monsieur Terney is supposed to have sailed"` | no hit about this letter |
| (f) solver repositories | fresh shallow clones of dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers, grep -i haldimand/arbuthnot | no hit (one unrelated "Haldimand" in Bourdeau's roell1809 Turkish inventory, a Dutch consul) |
| (f) cipher blogs | solvers' 2 Oct log (Cryptiana post + 0 comments, Cipherbrain, Cipher Mysteries) accepted, not re-run; Tomokiyo haldimand.htm (on disk) gives only the incipit "I have received your dispatches" and "decoded on p.186" | Tomokiyo already locates this decipherment |
| (g) scholarship | OpenAlex `search=Haldimand Clinton cipher` (2 results: a 1992 geography thesis, an index; neither prints the letter). Leighton & Matyas 1985 not opened (Springer paywall) -- it describes the system and its solution by Barbara Harris, not reached for this letter's text | no hit; JSTOR not queued (N0 found in open print, a JSTOR row cannot change the class) |
| DECODE | `sources/decode/*.tsv` grep haldimand/clinton (on disk) | no hit |

Unreachable this session: Saberton CP (not relevant: Cornwallis items only), JSTOR (cloud-blocked; not needed).
Requests: discovery.nationalarchives.gov.uk 2, archive.org 6 (fts 2, metadata 3, djvu 1), www.googleapis.com 3,
api.openalex.org 1, github.com 2 clones, WebSearch 2; 1.5-2 s apart.

## 3. Classification

**Item 2894, plaintext of the f.186 decipherment: N0.** Plaintext and decipherment of this very item already known:
the period decipherment (1780) exists at reel p.186 and was printed verbatim in 1920 (Hist. Section, General Staff,
vol. III, Illustrative Document 170, p.158), and TNA's catalogue paraphrases it. Prior plaintext: yes, 1920 print
(earliest citation found), plus HMC 1904-09 / Discovery paraphrase. Prior decipherment: yes (period; Kew decipher
"Vol.11 No.117"; reel p.186). Evidence quality: high (djvu text of two scans of the same print agree). Confidence: high.
Key source: **period** (the key cells rebuilt by us from the period decipherment against the 1778 key book of the time;
the key book identified by Leighton & Matyas 1985 and Tomokiyo, credited). `text: known`.

**The clause "Admiral A will be reinforced in proportion": N0 (floor N1).** TNA Discovery's description of this very
cipher item (PRO 30/55/24/76) states "Admiral Arbuthnot will be reinforced in proportion"; since the BL/reel decipherment
omits it, that wording can only come from a decipherment or retained copy of the Kew item itself ("decipher 11, No.117"),
i.e. a prior decipherment of this clause exists (medium confidence on that inference; the Kew decipher was not seen).
Independently, the same words are printed in 1920 in McLean's report of Clinton's letter (Doc. 181, p.165). Either way
the clause's plaintext is in print and in the catalogue: what the account-4 work adds is the cell-by-cell mapping of the
cipher pairs to it, confirming the preposition "in" (and TNA's/McLean's "Arbuthnot" for the clerk's bare "A").

Safe sentence: "We transcribed Clinton's cipher letter to Haldimand of 6 July 1780 (TNA PRO 30/55/24/76; Haldimand
Papers B.147) from LAC reel H-1649 and checked its 315 figure pairs against the 1778 Army List title-page key and the
period decipherment, already printed in 1920 (Military and Naval Forces of Canada, vol. III, doc. 170); the cipher
also carries the clause 'Admiral A[rbuthnot] will be reinforced in proportion', which the decipherment omits and which
TNA's catalogue and McLean's printed letter of 24 July 1780 already state."

Unsafe sentence: "A clause omitted from the decipherment, not located in any print, was recovered from the cipher" /
"the only text of 2894 located anywhere is the period decipherment on the reel."

## 4. Re-derivation (rule 7) and reading check

Re-run in this session from the committed transcription and keys: `passes/build_p186.py --check` (OK, 119: H 116 M 3),
`passes/check_2894_key.py --check`, `passes/title_1761_check.py --check`, `passes/title_1778_check.py --check` -- all
exit 0, regenerate identically. **Reproduces with zero differences**, within the M-graded tokens.

Against the 1920 print (a transcription of the B.147 copy, normalized for OCR noise): agreement on every word of the
body except "Ministers" (ours) / "Minister" (print), "Terney[M]" / "Ternay", "stil" / "still", "Rivers" / "River",
"Laurence" / "Lawrence", "& No 4" vs "No. 4" not at issue (ours reads "and No 4"), and punctuation. Checked crop
`images/h1649/p186_lines/p186_text_region_L02.jpg` by eye: the reel page plausibly reads "Ministers" (or "Ministes");
the cipher itself reads Minister (GAPS3/4); the print's editors silently normalized several spellings ("still",
"Lawrence"). Not graded a reading error: an M-level variant between witnesses. "Terney" is already M; the print and the
cipher both give Ternay. No token count changes.

## 5. Postmortem

Failure: the solver sessions declared the clause "not located in f.186, HMC's paraphrase or any print searched on 2 Oct
2026" while the clause stood, word for word, in TNA's description of the same item saved into this folder the same
morning (`discovery_clinton_to_haldimand_2026-10-02.tsv` row 14), and the f.186 text was called "the only text of 2894
located anywhere" without a full-text phrase search of the decoded text on Internet Archive, which finds the 1920
printing in one query. Lesson: run the decoded text's distinctive phrases through be-api fts (and grep the folder's own
saved catalogue descriptions) before writing "not located"; the recipient's national archive often printed its own
holdings' documents (here the Canadian General Staff's documentary history).

Corrections made: NOTES.md gets a "VERIFY-CLINTON-2894 corrections" section and bracketed corrections on the
over-claiming sentences (the GAPS clause sentence, the Remaining-gaps 2894 line, the Verdict line, the Web-check Result
line). No SECOND-OPINIONS-QUEUE.tsv row exists for this target, and N0 does not queue one. PROGRESS.tsv row updated.

Credit: decipherment by Haldimand's office, 1780; printed by the Historical Section of the General Staff (Canada), 1920;
key book identified by A.C. Leighton and S.M. Matyas (1985), Barbara Harris's solution of the system as they report it;
reel locations and cell table by S. Tomokiyo (Cryptiana).

---

# AUDIT -- pro3055-clinton-1779, items 3868 (PRO 30/55/33/65) and 2380 (PRO 30/55/19/98)

Verifier VERIFY-CLINTON-3868-2380, 2 Oct 2026 (clock read 21:28-21:4x UTC, `date -u`), account 4. A separate session
from the solver sessions GAPS8 and GAPS9 (account 4) that produced the readings; this audit does not protect their
conclusions. Item 2894's audit above is unchanged.

**Claims under audit.** (1) 3868: "body read from its period decipherment B.147 pp.385-386, H 248 M 4; key 44/44 cells
on the 1778 Army List key vs shuffled p95 6; the body is printed in full in Collections of the Vermont Historical Society
vol. II (1871) pp.198-199 (214/229 words equal), and in Walton's Governor and Council vol. II and Wilbur 1928."
(2) 2380: "22 Oct 1779 letter, pp.134-135 period decipherment, body H 241; key 52/93 exact cells vs shuffled-plaintext
p95 11; not located in print (two be-api phrase queries, 0 items; the 1920 vol. III has no 22 Oct 1779 document)"; and
GAPS9's "p.134 is the decipherment of 2380, not an abstract of the 9 Sept 1779 letter as Brymner's calendar has it".

## 1. Extract

| field | 3868 | 2380 |
|---|---|---|
| item | TNA PRO 30/55/33/65; recipient copies LAC Haldimand Papers B.147 (BL Add MS 21807) p.382 cipher (fo.308, Image 1030), pp.385-386 decipherment (fo.310-311v, Images 1033-1034), reel H-1649 | TNA PRO 30/55/19/98; B.147 p.120 cipher (fo.105, Image 758), pp.134-135 decipherment (fo.113-114v, Images 772-773) |
| date, place | New York, 12 Nov 1781 (received 14 May 1782) | New York, 22 Oct 1779 (received Quebec via Halifax 18 Jan[?] 1780) |
| sender -> recipient | Sir Henry Clinton -> Gen. Frederick Haldimand | same |
| system | figure pairs (line-letter) on the title page of the 1778 Army List (Leighton & Matyas 1985; Tomokiyo, Cryptiana haldimand.htm) | same key; encipherer counted line 1 as PERMISION/HONORABLE (Tomokiyo's "-1/-2 errors") |
| reading | passes/p385_reading.txt: 252 words H 248 M 4 | passes/p134_reading.txt: body 241 words H 241 |
| distinctive phrases | "jealousies of the Inhabitants of Vermont"; "Separate that district from the Revolt"; "extend only to granting pardons" | "Army of the Convention by exchange"; "still the Clamours of their own Officers"; "Regiment of Knyphausen and the remainder of the British"; "by the Matross of the Artillery"; "650 Recruits and Artillery" |
| what the solver searched | GAPS8: one be-api fts phrase query (13 items), VHS vol. II djvu read; Walton, Wilbur, VHS Proceedings 1941 hits not opened; GAPS5 premise check (1920 vol. III, Brymner, Davies vol. 20 snippet) | GAPS9: two be-api fts queries on the decipherment's opening "honored/honoured with your letter of the 19th July" (0 items each); the 1920 vol. III djvu |

## 2. Searches (this session, 2 Oct 2026)

| family | 3868 | 2380 |
|---|---|---|
| (a) canonical series / calendar | Brymner, Report on Canadian Archives 1887 (pub. 1888), B.147 calendar, archive.org `reportoncanadian1887publuoft` djvu read: "Clinton to the same. Letter in cypher. 382 / [New York] Explanation. Approves generally of Haldimand's course; the change of boundaries may require an Act of Parliament, &c. Arnold says that Du Calvet, Pere Floquet, Hay, Cord, Freeman and Watts were friends to the rebels. 385" | same volume: p.134 calendared "Same to the same. His disappointment at not receiving the army of the convention ... Renown ... Lossbergs ... Hopes the Indians will be prevailed on to threaten the frontiers of Virginia ... (Has neither date nor signature, being the explanation of a letter in cypher. By comparison with letter (p. 85) dated 9th September, 1779, it will be seen that this letter is an abstract of the contents of that communication (see also p. 136). The letter in cypher is referred to on the latter page.) Page 134" |
| (b) sender/recipient editions | *Collections of the Vermont Historical Society* vol. II (1871), "The Haldimand Papers", pp.198-199, confirmed (`collectionsofver02vermuoft`); the society's preface says the Haldimand Papers are "now first printed" from Vermont's two MS folio volumes of copies (Henry Stevens Sr.) and B.H. Hall's copies; Walton, *Records of the Governor and Council* vol. II (1874), Google Books snippet confirms the same text | **found:** the same VHS vol. II (1871), **p.192**, printed in full without its own heading, run on after a "H. -- Sir Henry Clinton to General Haldimand. Intelligence. 27th October, [1781.]" piece and so misdated by the editor: "I was favored with your letter of the 19th of July by the Matross of the artillery. There are now no hopes of recovering the army of the convention by exchange ... I have received your dispatches by the Defiance." (djvu lines 11519-11545 of `collectionsofver02vermuoft`; Google Books `hY46AQAAMAAJ` snippet agrees) |
| (c) documentary editions | Davies, *Documents of the American Revolution* vol. 20 not re-opened (GAPS5 left it unresolved) | Davies, *Documents of the American Revolution* vol. 17 (Transcripts 1779; archive.org `documentsofameri0017grea`, lending-only, be-api highlights only): a longer clear text with the same sentences -- "Excellency's letters of the 19th July by a matross of the artillery on the 19th ultimo. I am sorry to acquaint you that ... army of the convention by exchange there is now no chance of effecting it ... clamours of their own officers who have been so long prisoners with us. I am disappointed ... threaten the frontiers of Virginia in great force, which will operate in favour of the" -- consistent with the index entry "ci Sir Henry Clinton to Frederick Haldimand, 9 September .... 204" ("19th ultimo" = 19 Aug fits a 9 Sept letter); page heading not seen, so the attribution to 9 Sept is inferred |
| (d) holding archive | TNA Discovery and LAC reel already in the folder; not re-fetched | same |
| (e) full text: IA be-api | "jealousies of the inhabitants of Vermont" 13 items (reproduces GAPS8); "extend only to granting pardons" 17; "separate that district from the revolt" 12 -- all VHS Collections II copies, Walton 1874, Wilbur *Ira Allen* 1928, VHS Proceedings/*Vermont History* 1941, Thompson *Independent Vermont*, Slafter *Vermont coinage* | "army of the convention by exchange" 2 (Davies 17; Metzger 1971 quoting the Clinton wording); "still the clamours of their own officers" 1 (Davies 17); "threaten the frontiers of Virginia" 5 (Davies 17, Brymner 1888 x2, Talbert *Benjamin Logan* 1962 quoting "your quarter will be prevailed on to threaten the frontiers of Virginia in great force"); "Regiment of Knyphausen and the remainder" 4, "by the Matross of the Artillery" 4, "650 recruits and artillery" 2, "Georgia will be exposed to great danger" 4 -- all VHS Collections II copies and Slafter |
| (e) Google Books (key, country=US) | two phrases: earliest 1871 (VHS Collections II), then Walton 1874, Wilbur 1928, VHS 1941 | "favored with your letter of the 19th of July" and "regiment of Knyphausen and the remainder of the British": 1 each, VHS Collections II (1871); "still the clamours ..." no relevant hit |
| (f) solver repositories, cipher blogs | Tomokiyo, Cryptiana haldimand.htm (on disk, `sources/cryptiana/web/`): "f.382 (Image 1030), Clinton to Haldimand, 12 November 1781, decoded on p.385", cell table extract ("of your proclama[tio]") | Tomokiyo: "f.120-122 (Image 758-) ... 22 October 1779, decoded p.134-: 'I was honored with your letter of the 19th July ...'", 11-cell extract reading "i was favored" with the -1/-2 errors marked; and "f.96-99 (Image 734-) Clinton to Haldimand, New York, 9 September 1779 (decoded f.85-94 ...: 'I was favored with ...')" with the identical 11-cell extract. Bourdeau and Aymeloglu: no haldimand hit (grepped 25 Sept and 2 Oct, per item 2894's audit; not re-cloned) |
| (g) scholarship | OpenAlex `Haldimand Clinton cipher` 2 results, S2 `Haldimand Clinton cipher 1779` 2 results, none about either letter; Leighton & Matyas 1985 (key book) already cited | same queries; nothing on the letter |
| JSTOR | rows appended to JSTOR-QUEUE.tsv, families (i) and (ii); not blocking | same |
| unreachable | none needed; Davies vol. 17/20 page images (lending-only, not borrowed) | same |

Requests: be-api.us.archive.org 21, archive.org 2 (two djvu texts), googleapis.com/books 5, api.openalex.org 1,
api.semanticscholar.org 1; one at a time, 1.6 s apart. No credential printed.

## 3. Classification

**Item 3868 -- N0.** Prior plaintext: yes, *Collections of the Vermont Historical Society* vol. II (Montpelier 1871)
pp.198-199, earliest located; reprinted Walton 1874, Wilbur 1928, VHS 1941. Prior decipherment: yes, the period
decipherment B.147 pp.385-386 (Haldimand's office, 1782), calendared by Brymner (1888, "Explanation ... 385"), and the
cipher's location and partial cell table published by Tomokiyo. Our reading is a fresh transcription of that period
decipherment plus a cell check (44/44 vs shuffled p95 6) of cipher columns 1-2 on the 1778 key. Evidence: direct (djvu
text read, Google Books snippets). Confidence: high. Key source: `period`. Text: `known`.

- Safe sentence: "We transcribed the period decipherment of Clinton's cipher letter to Haldimand of 12 November 1781
  (TNA PRO 30/55/33/65; Haldimand Papers B.147 pp.382-386, LAC reel H-1649) and checked 44 cells of the cipher against
  it on the 1778 Army List title-page key; the letter's text was already printed in 1871 (Collections of the Vermont
  Historical Society, vol. II, pp.198-199)."
- Unsafe sentence: "the 3868 body, not in print, read from the cipher" / "first reading of Clinton's 12 Nov 1781
  cipher".

**Item 2380 -- N0.** Prior plaintext: yes, *Collections of the Vermont Historical Society* vol. II (1871) p.192, in
full, misplaced by its editor under a 27 Oct 1781 "Intelligence" heading (the print reads "favored", "Louisburg",
"Niagara" where the B.147 decipherment reads "honored", "Lossberg", "Virginia"); calendared in Brymner 1888 (p.134 entry
above); the near-identical clear letter of 9 Sept 1779 is printed in Davies, DAR vol. 17 (1972), p.204 per its index
(heading inferred, page not opened). Prior decipherment: yes, the period decipherment pp.134-135 itself, Brymner's
"explanation of a letter in cypher", and Tomokiyo's published 11-cell extract with the -1/-2 errors marked. Evidence:
direct (djvu text read). Confidence: high. Key source: `period`. Text: `known`.

- Safe sentence: "We transcribed the period decipherment of Clinton's cipher letter to Haldimand of 22 October 1779
  (TNA PRO 30/55/19/98; Haldimand Papers B.147 pp.120 and 134-135, LAC reel H-1649) and checked 93 cells of its cipher
  against it on the 1778 Army List key (52 exact, 89 within two places); the text was printed in 1871 (Collections of
  the Vermont Historical Society, vol. II, p.192, under a wrong date) and repeats, abridged, Clinton's letter of
  9 September 1779."
- Unsafe sentence: "2380 not located in print" / "Brymner's calendar is wrong about p.134".

No SECOND-OPINIONS-QUEUE.tsv row: neither item is N3 or better.

## 4. Postmortem

Failure (2380): "not located in print" rested on two phrase queries of the decipherment's *opening*, the one clause
where the printed text differs ("favored" vs "honored"); any interior phrase ("by the Matross of the Artillery",
"Regiment of Knyphausen and the remainder") finds the 1871 print in one be-api query, the same volume GAPS8 had just
opened for 3868. And GAPS9's "p.134 is the decipherment of 2380, not an abstract of the 9 Sept 1779 letter as Brymner's
calendar has it" set up a false either/or: p.134 is this cipher's decipherment *and* its content is an abridgement of the
9 Sept letter, as Brymner said (Tomokiyo's 9 Sept and 22 Oct cell extracts are identical; both open "I was favored";
DAR vol. 17 prints a longer clear text with the same sentences). Lesson: phrase-search at least three interior phrases,
not the incipit, before writing "not located"; a period copy may differ exactly at the opening. One point in the
solver's favour: the 1871 print's "favored" independently supports GAPS9's cell finding that the cipher says "favored"
where the decipherer wrote "honored".

3868: no failure; GAPS8 already reported the print. Earliest citation set to 1871 and the Brymner calendar line added.

Corrections made: NOTES.md "VERIFY-CLINTON-3868-2380 corrections" section and bracketed corrections on GAPS9's print and
conflict sentences and on the 2380 Remaining-gaps line. `passes/check_2380.py --check` and `passes/check_3868.py --check`
re-run in this session: both OK, exit 0 (the key checks regenerate; the rule-7 fresh-session re-derivation stays a
separate stage-9 step).

Credit: decipherments by Haldimand's office (1780, 1782); first printed by the Vermont Historical Society (1871,
from Henry Stevens Sr.'s and B.H. Hall's copies); calendared by D. Brymner (1888); key book identified by A.C. Leighton
and S.M. Matyas (1985); reel locations and cell extracts by S. Tomokiyo (Cryptiana).
