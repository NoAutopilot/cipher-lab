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
| reading | passes/p385_reading.txt: 252 words H 248 M 4 [R10-CLINV2, 6 Oct 2026: now H 250 M 2, see that section] | passes/p134_reading.txt: body 241 words H 241 |
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

---

# AUDIT -- pro3055-clinton-1779, items 3050 (PRO 30/55/26/2) and 3077 (PRO 30/55/26/30)

Verifier VERIFY-CLINTON-3050-3077, 2 Oct 2026 (clock read 23:17-23:3x UTC, `date -u`), account 4. A separate session
from the solver sessions GAPS11 and GAPS12 (account 4) that produced the print check and the readings; this audit does
not protect their conclusions. The 2894, 3868 and 2380 entries above are unchanged.

**Claims under audit.** (1) 3050 (Clinton to Haldimand, New York, 2 Oct 1780): "read at H from its period decipherment
B.147 p.245 (H-1649 Image 889), 106 words H 106". (2) 3077 (same, 18 Oct 1780, No. 24): "read at H from its period
decipherment B.147 p.246 (Image 890), 175 words H 175". (3) Both: "the p.242 and p.247 cipher cells match them on the
1778 key, 118/118 vs shuffled-plaintext p95 13"; "not located in print" after GAPS11's six-volume djvu grep (VHS
Collections II 1871, Walton II-III, the 1920 vol. III, Brymner 1887 and 1888 reports) and GAPS11/GAPS12's be-api
queries; known only as Brymner's paraphrase.

## 1. Extract

| field | 3050 | 3077 |
|---|---|---|
| item | TNA PRO 30/55/26/2; recipient copies BL Add MS 21807 (= LAC Haldimand B.147) p.242-244 cipher (fo.206-207, Images 886-888), duplicate p.239, p.245 decipherment "Duplicate ... being the Explanation of his Letter in Cypher of the 2d October" (fo.208, Image 889) | TNA PRO 30/55/26/30; B.147 p.247 cipher (fo.210, Image 891, opening in clear), p.246 decipherment "Copy" (fo.209, Image 890) |
| date, place | New York, 2 Oct 1780 | New York, 18 Oct 1780 (No. 24) |
| sender -> recipient | Sir Henry Clinton -> Gen. Frederick Haldimand | same |
| system | figure pairs (line-letter) on the 1778 Army List title page (Leighton & Matyas 1985; Tomokiyo, Cryptiana haldimand.htm) | same |
| reading | passes/p245_reading.txt | passes/p246_reading.txt |
| distinctive phrases | "Intention of giving up the Forts &c &c at West Point"; "thrown the Rebels Army into the Greatest Confusion"; "little Probability of a second division of french ships"; "Compleat Victory over General Gates on the 16th of August at Camden"; "great defection in the spanish Colonies" | "honored with Your Excellency's Letter of the 8th ultimo, and a Subsequent one without date"; "miscarriage of the Quebec Fleet"; "Sir George Rodney still favors us with his Company"; "lay aside their Attempt on this Place"; "the Cork Fleet which is much wanted"; "Expedition of near 3000 Men ... under General Leslie"; "probably acting in North Carolina"; "paid Ten Guineas" |
| what the solvers searched | GAPS11: six djvu texts grepped (date, correspondents, 5 interior phrases); be-api "intention of giving up the forts", "great defection in the Spanish"; GAPS12: be-api "defection in the Spanish colonies", "attempt by Arnold" | GAPS11: djvu grep (6 phrases), be-api "miscarriage of the Quebec fleet", "blocked up at Rhode Island"; GAPS12: be-api "the Quebec fleet has" (x2), "accommodation with Spain" |

## 2. Searches (this session, 2 Oct 2026)

| family | 3050 | 3077 |
|---|---|---|
| (a) canonical series / calendars | HMC, *Report on American Manuscripts in the Royal Institution* vol. II (1906), archive.org `reportonamerican02grea` djvu read: p.188 "Gen. Sir Henry C[linton] to Gen. Haldimand. 1780, October 2. New York. Copies. Vols. 11, No. 123; 18, No. 23*, in cipher; 11, No. 125 ... Originals in the Brit. Mus., Addtl. MSS. 21807; copy in the Public Record Office, Am. & W. I. 138" -- location only, no content. Brymner, Report on Canadian Archives 1887 (pub. 1888) B.147 paraphrase (GAPS11), confirmed in 6 Google Books copies | HMC vol. II p.192: "1780, October 18. New York. Copies. Vols. 18, No. 24, and 11, No. 126; in cipher, No. 127 ... Also in the Public Record Office, Am. & W. I. 138, fo. 657; autograph letter, in cipher, ... 21807, fo. 210; autograph signed letter 21807, fo. 209" -- location only. Brymner 1888 paraphrase (B.147 p.246, "The letter in cypher follows"), close in wording ("Cork fleet which is much wanted") |
| (b) sender/recipient editions | VHS Collections II (1871), Walton II-III (GAPS11's greps, re-checked by be-api phrase queries below); *Michigan Pioneer and Historical Collections* vols X, XIX, XX (the Haldimand Papers volumes; `michiganhistoric10michuoft`, `...19michuoft`, `...20michuoft`) djvu grepped for "clinton to haldimand", both dates, "greatest confusion", "west point", "defection", "rodney", "ternay": no Clinton-to-Haldimand letter of either date (hits are other documents); MPHC index vols 1-15 and 16-30 entries "Clinton, Sir Henry" read: neither letter listed | same MPHC volumes and indexes: no hit ("quebec fleet", "cork fleet", "18th october" hits are other documents) |
| (c) documentary editions | Davies, *Documents of the American Revolution* vol. 16 (Calendar 1780) and vol. 18 (Transcripts 1780), be-api in-item: vol. 18 has no Clinton-to-Haldimand letter ("2 October 1780" 0, "Haldimand" hits are Haldimand to Germain); vol. 16 no "2 October 1780" Clinton-Haldimand entry seen | Davies vol. 16 calendars "New York, 18 October 1780. Sir H. Clinton to General Haldimand" as enclosure ix of No. 2596 (a dispatch of General Sir Henry Clinton dated 11 October [1780], New York, per the be-api highlight; addressee not seen, presumably Germain; an 18 Oct enclosure to an 11 Oct dispatch is itself unchecked) -- a calendar line, the summary (if any) not read (lending-only, be-api highlights only); not printed in vol. 18 ("18 October 1780" 0). Stevens's *Facsimiles*: no archive.org item matched the title query (0), not searched further; its scope is Auckland/Carlisle/French papers, not Haldimand |
| (d) holding archive | TNA Discovery and the LAC reel already in the folder; not re-fetched | same |
| (e) full text: IA be-api, all items, exact phrase | "rebel army into the greatest confusion" 0; "Rebels Army into the greatest confusion" 0; "thrown the rebel army into" 3 (Brymner 1887 x2, an unrelated Uganda book); "thrown the rebels army" 0; "has joined us, which has thrown" 0; "giving up the forts at West Point" 0; "Admiral Rodney is on this coast" 0; "little probability of a second division" 0; "victory over General Gates on the 16th" 16 and "complete victory over General Gates" 6 (Morse, Mante, Annual Register 1781 etc. -- Camden narratives, not this letter); "compleat victory over General Gates" 0 | "still favors us with his company" 1 (an 1869 newspaper); "still favours us with his company" 0; "lay aside their attempt on this place" 0; "Cork fleet which is much wanted" 3 (Brymner 1887 x3); "expedition of near 3000 men" 0; "favor the operations of Lord Cornwallis" 6 (Mackenzie's diary, a different sentence about James River); "favour ..." 0; "paid ten guineas by me" 0; "without date. I am concerned" 0; "accommodation with Spain will speedily" 0; "Ternay's fleet and the French army remain" 0; "letter of the 8th ultimo, and a subsequent one" 5 (Jay correspondence, unrelated); "the Chesapeak under General Leslie" 2 (Clinton's *Observations* 1783 and Stevens 1888 reprint -- a list of detachments, not this letter); "probably acting in North Carolina" 0. Positive control: "Vermont deserves our vigilant attention" 13 (VHS II, Walton II, Wilbur), so the route finds printed Haldimand letters |
| (e) Google Books (key, country=US) | "thrown the rebels army into the greatest confusion", "thrown the rebel army into ...", "little probability of a second division", "intention of giving up the forts": no relevant volume in the top results; "great defection in the Spanish colonies" 6, all Brymner 1888 | "miscarriage of the Quebec fleet", "still favors us with his company", "lay aside their attempt on this place", "accommodation with Spain will speedily take place": no relevant volume; "Cork fleet which is much wanted" 6, all Brymner 1888 |
| (e) HathiTrust full text | unreachable from the cloud (Cloudflare; CLAUDE.md host table); not tried | same |
| (f) solver repositories, cipher blogs | Tomokiyo, Cryptiana haldimand.htm (on disk): locates the cipher (Image 886) and the decoded copy; GAPS11 used his extracts. Bourdeau and Aymeloglu: no Haldimand target (CX2 round 2 greps, folder NOTES) | same (Image 891, decoded p.246) |
| (g) scholarship | OpenAlex "Clinton Haldimand 1780 cipher" 2 results, "Haldimand Arnold West Point Clinton letter" 15 results; S2 "Haldimand Clinton cipher 1780" 1 result: none about either letter. be-api "Clinton to Haldimand" (164) and "Sir Henry Clinton to General Haldimand" (43): top hits are other letters (1778, 1779, 1781) | same queries |
| JSTOR | rows appended to JSTOR-QUEUE.tsv, families (i) and (ii); not blocking | same |
| unreachable | HathiTrust full text; Davies vol. 16 page for No. 2596 ix (lending-only, not borrowed) | same |

Requests: be-api.us.archive.org 36, archive.org 9 (6 djvu texts, 3 advancedsearch), googleapis.com/books 10,
api.openalex.org 2, api.semanticscholar.org 1; one at a time, 1.6 s apart. No credential printed.

## 3. Re-derivation (rule 7)

`python3 passes/check_3050_3077.py --check` run in this session from the committed passes, cells and key: "check_3050_3077: OK",
exit 0 -- p245_reading.txt, p246_reading.txt and check_3050_3077.json regenerate unchanged from
p245_246_reconciled.tsv, p242_p247_cells.tsv and title1778_reading.txt. The statistic (118/118 cells vs shuffled-plaintext
mean 7.95, p95 13, max 19) is computed on the plaintext axis, so the control can fail where the target passes (rule 3).
Limits carried forward unchanged: the cell check covers the opening of each cipher only (p.242 cols 1-3, p.247 cols 1-2);
27 of the 125 cells rest on the worker's reconciliation made with the decipherment in view (GAPS12 states this); the H
grades are a transcription of a period decipherment, not a cryptanalytic result.

## 4. Classification

**Item 3050 -- N0, key `period`, text not in print (no `text: known`).** N0 = "plaintext and decipherment of this very
item already known": the period decipherment exists on the leaf (B.147 p.245, Haldimand Papers, written 1780 as Clinton's
"Explanation of his Letter in Cypher"), is calendared by HMC (1906, vol. II p.188: clear copies Vols. 11 Nos. 123, 125
and a PRO copy, Am. & W. I. 138) and paraphrased by Brymner (1888), and its place on the reel is published by Tomokiyo.
This is the precedent of szembek-bk1560, rah-canada-1869 and antt-fcc-costacabral-1865 (N0 from the leaf, period key). Prior
plaintext in print: **not located** -- only Brymner's paraphrase (1888) after the searches above. Our contribution is a
transcription of the period decipherment and a cell check of the cipher's opening (66/66) on the 1778 key. Evidence:
direct (djvu texts, be-api, Google Books). Confidence: high that no full print exists in the sources searched; medium
overall (HathiTrust full text, Davies vol. 16's calendar page and any Clements Library/Clinton Papers publication not
read).

- Safe sentence: "We transcribed the period decipherment of Clinton's cipher letter to Haldimand of 2 October 1780 (TNA
  PRO 30/55/26/2; Haldimand Papers B.147 pp.242-245, LAC reel H-1649) and checked 66 cells of the cipher's opening against
  it on the 1778 Army List key; the letter's content was calendared by Brymner (1888), and its full text was not located
  in print in the sources we searched."
- Unsafe sentence: "first decipherment of Clinton's 2 October 1780 letter" / "previously unread" / "recovered from the
  cipher" (the period decipherment is the source).

**Item 3077 -- N0, key `period`, text not in print (no `text: known`).** Same footing: the period decipherment on the
leaf (B.147 p.246, "Copy"), HMC vol. II p.192 (clear copies Vols. 18 No. 24 and 11 No. 126, PRO Am. & W. I. 138 fo.657),
Brymner's close paraphrase (1888), and a calendar line in Davies, DAR vol. 16, as an enclosure (ix) of No. 2596 (not read).
Prior plaintext in print: **not located** beyond the paraphrase and the calendar line. Evidence: direct. Confidence:
medium (the DAR vol. 16 entry may carry a summary; its page was not read).

- Safe sentence: "We transcribed the period decipherment of Clinton's cipher letter to Haldimand of 18 October 1780 (TNA
  PRO 30/55/26/30; Haldimand Papers B.147 pp.246-247, LAC reel H-1649) and checked 52 cells of the cipher's opening against
  it on the 1778 Army List key; the letter was calendared by Brymner (1888) and listed by Davies (DAR vol. 16, as an enclosure to
  a Clinton dispatch), and its full text was not located in print in the sources we searched."
- Unsafe sentence: "a previously unknown Clinton letter" / "never printed" / "first reading".

No SECOND-OPINIONS-QUEUE.tsv row: neither item is N3 or better (rule 10; a period decipherment on the leaf is a prior
decipherment of this very item).

## 5. Postmortem

No over-claim found: GAPS11 and GAPS12 wrote "not located in print ... a search result, not a novelty verdict" and
searched interior phrases, not only the incipit (VERIFY-CLINTON-3868-2380's lesson was applied). Gaps this audit closed
or named: (a) HMC vol. II was not cited for either date -- added, location-only entries (pp.188, 192) that also show
clear copies of both letters were sent to Germain (PRO Am. & W. I. 138), which is where a print would most likely come
from; (b) Davies DAR vol. 16 calendars 3077 as an enclosure of No. 2596 -- added, page not read (lending-only); vol. 18
does not print either letter; (c) the Michigan Pioneer Haldimand volumes (X, XIX, XX) were not in the solver's list --
searched, no hit. The class is N0 (not N3) because the period decipherment itself is a prior decipherment of the item,
as in szembek-bk1560; the solvers did not claim otherwise.

Corrections made: NOTES.md "VERIFY-CLINTON-3050-3077 corrections" section (no sentence of GAPS11/GAPS12 needed
striking; the added sources are recorded there).

Credit: decipherments by Clinton's headquarters (1780); calendared by D. Brymner (1888), the HMC (1906) and K.G. Davies
(DAR vol. 16); key book identified by A.C. Leighton and S.M. Matyas (1985); reel locations and cell extracts by
S. Tomokiyo (Cryptiana).

---

# AUDIT 4 (A3V-VN0, 4 Oct 2026): item 2894 (PRO 30/55/24/76), second audit of the N0 class

Verifier A3V-VN0, account 3, for LANE-A3V, 4 Oct 2026 (clock read 03:13 UTC start, `date -u`). Brief
`.claude/briefs/runs/2026-10-04-acct3-a3v-wave2.md` section A3V-VN0. A session separate from the solvers (GAPS, GAPS2-4,
account 4) and from audit 1 (VERIFY-CLINTON-2894, account 2); it does not protect either. No decoding, no key or reading
change.

**Claim under audit:** audit 1's verdict: N0, period decipherment (reel p.186, H 116 M 3) printed 1920, *Military and
Naval Forces of Canada* vol. III, Illustrative Document 170, p.158; key `period`; earliest citation 1920.

## 1. The cited print, opened

archive.org `vol1t3historyoforganiz01quebuoft` `_djvu.txt` (1 request, scratchpad, not committed), djvu lines 54470-54480,
between the page headers "Illustrative Documents 157" and "... 159", so p.158 as audit 1 says. Quoted (OCR as served):

> "(170) PUBLIC ARCHIVES OF CANADA. HALDIMAND PAPERS. Series B, Vol. 147, p. 183. / I have received your dispatches of
> Novr & January & I Kave received Information from the Minister of the 3d May. Monsieur Ternay is supposed to have
> sailed about the 3d May with seven ships oif the line & from 20 to 25 Transports &c., having on board five Thousand two
> hundred land Forces ..."

Ten positions compared by this verifier against `passes/p186_reading.txt`:

| # | ours | 1920 print | agree |
|---|---|---|---|
| 1 | dispatches of Novr & January | dispatches of Novr & January | yes |
| 2 | Ministers | Minister | variant (audit 1 noted; M-level, not a reading error) |
| 3 | Terney[M] | Ternay | variant, already M |
| 4 | seven ships of the line | seven ships oif [OCR] the line | yes |
| 5 | 20 to 25 Transports | 20 to 25 Transports | yes |
| 6 | five Thousand two hundred land Forces | same | yes |
| 7 | stil supposed to be Canada | still supposed to be Canada | yes (spelling) |
| 8 | Rhode Island, a[M] division | rhode Island a division | yes |
| 9 | Marquis de Fayette by Connecticut Rivers and No 4[M] | Marquis de layette [OCR] by Connecticut River and No. 4 | yes, "Rivers"/"River" variant |
| 10 | the other by the river Saint Laurence | tne [OCR] river saint Lawrence | yes (spelling) |

7 of 10 identical, 3 spelling/number variants already flagged by audit 1; no position contradicts the reading. **Audit 1's
N0 basis is real.** One citation detail audit 1 did not carry: the print heads the document "Series B, Vol. 147, p. 183"
(the B.147 page of the cipher copy), while our files locate the decipherment on reel p.186; same document, the print
cites the cipher leaf.

## 2. Earliest print (credit)

| source | what it prints | date |
|---|---|---|
| Brymner, *Report on Canadian Archives* 1887 (Ottawa 1888), Haldimand Collection calendar, B.147 -- archive.org `reportoncanadian1887publuoft` djvu lines 102882-102888 (page between headers 645 and 647, so p.646; OCR "546"); second scan `cihm_57145` found by be-api fts | "Clinton to the same. Letter in cypher. 184 / Explanation of part follows. M. Ternay had sailed about the 3rd May with 7 ships of the line, from 20 to 25 transports, with 5,200 land forces, their destination supposed to be Canada. The French fleet, he believes, will assemble at Rhode Island, a division under La Fayette will proceed by Connecticut River and No. 4 across the lake to St. John's; the other by the River St. Lawrence. 186" | **1888, earliest print located** (close calendar paraphrase of the whole deciphered body, citing the cipher at p.184 and the decipherment at p.186) |
| HMC, *Report on American Manuscripts in the Royal Institution* (1904-09) / TNA Discovery scopeContent | paraphrase of the Kew copy, plus the clause | 1904-09 (audit 1) |
| *Military and Naval Forces of Canada* vol. III, doc. 170, p.158 | verbatim decipherment | 1920 (audit 1) |

**Correction to audit 1 (found, applied here as a pointer only):** audit 1's "Prior plaintext: yes, 1920 print (earliest
citation found)" holds for a verbatim print; the content was first printed as Brymner's 1888 calendar paraphrase, which
gives every fact of the body and says outright that it is the explanation of a letter in cypher. Class unchanged.

## 3. Searches (4 Oct 2026)

| family | searched | result |
|---|---|---|
| (a) canonical calendar | Brymner 1888 djvu (above) | hit, earliest print (paraphrase) |
| (b)(c) editions | 1920 vol. III djvu (above); be-api fts global: `"supposed to have sailed about the 3d May"` 2 items, `"Ternay is supposed to have sailed"` 2, `"Terney is supposed"` 0, `"Connecticut River and No. 4"` 4 | the 2 items are the two scans of the 1920 volume (`vol1t3historyoforganiz01quebuoft`, `31761118534445`); the 4 add Brymner (`cihm_57145`) and an unrelated Massachusetts forester's report. Davies, *Documents of the American Revolution* (lending items are in be-api's index) gave no hit |
| (d) holding archive | audit 1's TNA Discovery record accepted, not re-fetched | -- |
| (e) Google Books | key, `country=US`: `"Ternay is supposed to have sailed"` 197 loose, none this letter in the top 8 | no hit |
| (f) solver repos, blogs | audit 1's clones and Cryptiana check accepted (2 days old; no new commits searched) | -- |
| (g) scholarship / JSTOR | audit 1 queued no JSTOR row for 2894; 2 rows appended to `JSTOR-QUEUE.tsv` today: family (i) Clinton AND Haldimand AND July 1780 AND cipher/cypher AND Ternay; family (ii) the bare phrase "supposed to have sailed about the 3d May" | queued; cannot change N0 |

Requests: archive.org 5 (djvu 2, metadata 3), be-api.us.archive.org 5, www.googleapis.com 1; 1.5 s apart. Subagents: 0.

## 4. Rule 7 spot check

`tools/decode_key.py ciphers/pro3055-clinton-1779 --check` does not apply (no `decode.json`/`ciphertext.tsv`; the folder's
reading is built by its own scripts). Run instead: `passes/build_p186.py --check` "OK tokens 119: H 116, M 3", exit 0;
`passes/check_2894_key.py --check` and `passes/title_1778_check.py --check` regenerate identically, exit 0. Reproduces.

## 5. Verdict

**Item 2894: N0 confirmed.** Prior plaintext: yes -- earliest Brymner 1888 (calendar paraphrase, p.646), verbatim 1920
(doc. 170, p.158). Prior decipherment: yes, the period one (1780) on reel p.186, which both prints use. Evidence quality:
high (print opened, 10 positions compared). Confidence: high. **Key source: `period`** confirmed -- the cells are rebuilt
by us from the period decipherment against the 1778 Army List of the time; the key book was identified by Leighton & Matyas
(1985) and a cell table published by Tomokiyo (79/81 agreement), both credited, which does not make the key `ours`.
`text: known`. The clause's N0 (audit 1) is not re-examined here beyond noting that Brymner 1888 does not carry it.

Safe sentence: audit 1's, with the print history extended: "... the period decipherment, calendared by Brymner in 1888
(Report on Canadian Archives 1887, p.646) and printed in full in 1920 (Military and Naval Forces of Canada, vol. III,
doc. 170) ..."

Unsafe sentence: "The decipherment was first published in 1920."

Postmortem: audit 1 searched Brymner for 3868 and 2380 (its own later sections) but credited 2894's earliest print to
1920; a phrase run of the decoded body through be-api fts (which indexes the Brymner microform) finds the 1888 calendar in
one query. No over-claiming sentence in the folder's files found: none calls the 2894 text new; NOTES.md already treats it
as known. PROGRESS.tsv audit-2 column set to x from this verdict. N0 queues no SECOND-OPINIONS row.

## JSTOR run (local runner, 4 Oct 2026)

"The Treason of Benedict Arnold, as Presented in Letters of Sir Henry Clinton to Lord George Germain", The Pennsylvania Magazine of History and Biography 22 (1898) 410-422, https://www.jstor.org/stable/20085812 (from "Clinton" AND "Haldimand" AND ("October 1780") AND (cipher OR cypher OR Arnold), 26 results). Read in the page viewer: Clinton to Germain, New York 11 Oct 1780; p.411 refers to "the inclosed Copy of a Letter from General Haldimand to me". The Haldimand letter is not printed and no cipher is mentioned. Context only. The four Clinton phrase queries ("still the clamours of their own officers", "jealousies of the inhabitants of Vermont", "great defection in the Spanish colonies", "Cork fleet which is much wanted") returned 0; the 1779 and 1781 Haldimand queries surfaced only Wilbur, Early history of Vermont v.2 (1900) and indexes.

## R10-CLINV: verifier of R10-CLIN3868 (6 Oct 2026, account 2, LANE RUN10; clock 07:59-08:0x UTC, `date -u`)

A separate session from R10-CLIN3868 (the p.382 columns 3-6 cell check, NOTES.md section "R10-CLIN3868"); this audit does not
protect its conclusions. No novelty class asked; 3868 stays N0 (section above), key `period`, text `known`.

1. **Pre-registration order.** `PREREG_R10-CLIN3868.md` was pushed in d6e02ac03 (07:45:21 UTC); the scorer
   `passes/check_3868_c36.py`, its output and both transcriptions landed in 9994ec39a (07:48:21 UTC). The gate predates the
   committed score. The blind pass file was committed with the score, not before the PREREG, so its timing is not provable from
   git; it does not matter for the verdict, because the blind pass alone clears the gate (below).
2. **Re-score.** `passes/check_3868_c36.py --check` exit 0 (re-derives the committed JSON byte for byte); `check_3868.py --check`
   exit 0. Blind pass 93/100 key-consistent (i=j), reconciled 97/100; shuffled-plaintext control mean 6.96 / p95 11 / max 19
   (blind), 6.95 / 11 / 17 (reconciled). Gate (share >= 0.80 and count > control max) PASS on both. The control can differ on
   this statistic (it moves the decipherment letters against fixed key letters), so it is not a by-construction tie. Caveat: the
   five reconciliation changes were made only on cells that failed the key, a key-directed re-read; the gate result does not
   depend on them (the blind pass passes), but the 97 should be quoted with the blind 93 beside it.
3. **The name cells, eye-checked.** Image 1030 (H-1649, image-uab.canadiana.ca full/max, fetched once to the scratchpad), column
   4 box 2600,1290,2935,3220 (`tools/iiif_lines.py --image ... --region 2600,1290,335,1930` found 0 lines in a figure column, as
   the worker reported; box crop 2560,2900,2960,3230 used). The five entries read unambiguously **11-6, 4-2, 11-9, 1-1, 16-6**,
   ruled off below. On the 1778 title page (`passes/title1778_reading.txt`, two independent reads agree on all 30 lines): line 11
   "HORSE, DRAGOONS, and FOOT" pos 6 = d, pos 9 = g; line 4 "LIST" pos 2 = i; line 1 pos 1 = b; line 16 pos 6 = y. The cells spell
   **DIGBY**. The same cells carry the same letters elsewhere: 4-2 = i in "is" on this page and twice on p.242 (3050/3077); 11-9 = g
   in "respecting" on this page, on p.382 col. 2 and three times on p.242. "DARBY" on the same key line would be 11-6 **11-8 11-7**
   1-1 16-6 (a and r sit at line 11 pos 8 and 7); the page instead has two different cells, from two different key lines, each a
   correct encipherment of i and g. That is not a one-position slip of the kind Tomokiyo notes on 2380; it is a deliberate D-I-G.
   The p.385 decipherment line (committed crop `images/h1649/p385_lines/p385_L12.jpg`) reads "also laid before Admiral Darby,";
   the eye agrees with both transcription passes (second letter an undotted a, no g descender).
4. **Decision (rule 4: a data conflict, recorded by witness, not settled by majority).**
   - Witness A, sender side: the cipher letter itself, Clinton's office, New York, 12 Nov 1781 (B.147 p.382, the copy-book's
     cipher columns): DIGBY, every cell key-consistent.
   - Witness B, recipient side: the period decipherment, Haldimand's office, B.147 p.385 (copy-book): DARBY.
   - Witness C, print: *Collections of the Vermont Historical Society* vol. II (1871) pp.198-199 (`passes/vhs2_3868_print.txt`
     line 24): "Admiral Digby (who is joint commissioner with ...)". Its source manuscript is not stated in our files, so it is not
     counted as independent of A or B.
   Context, not a settlement: Rear-Admiral Robert Digby was at New York in November 1781 and joint commissioner with Clinton;
   Admiral George Darby was a real officer of the same date (Channel fleet), so "Darby" is a real name a decipherer could
   substitute, not a garble. The conflict is between the encipherment and the decipherment; it is recorded, not resolved.
   **Reading file: unchanged.** `passes/p385_reading.txt` is a transcription of the decipherment and correctly reads "Darby"
   (rule: never silently repair a transcription). The cipher-cell reading in `passes/check_3868_c36.json` correctly records
   "digby" at those cells. Grades as the worker set them stand (the i and g cells M against the decipherment; they are H against
   the key). No SECOND-OPINIONS-QUEUE.tsv row exists for this target (grep, 0 rows), so nothing to propagate there.
5. **Safe sentence, updated count (3868 only; the N0 class and its wording above are unchanged):** "We transcribed the period
   decipherment of Clinton's cipher letter to Haldimand of 12 November 1781 (TNA PRO 30/55/33/65; Haldimand Papers B.147
   pp.382-386, LAC reel H-1649) and checked the cipher of p.382 against it on the 1778 Army List title-page key (141 of 144
   comparable cells consistent); the cipher names the joint commissioner 'Digby', as the 1871 print does, where the period
   decipherment writes 'Darby'; the letter's text was already printed in 1871 (Collections of the Vermont Historical Society,
   vol. II, pp.198-199)." Unsafe: "the cipher corrects the decipherment" (settles a witness conflict by preference) or any
   wording implying the name reading is ours alone (the print already has Digby).
6. **Postmortem.** No over-claim found in R10-CLIN3868's NOTES section, except one sentence settling the conflict ("the p.385
   'Darby' is the decipherer's or copyist's error"): corrected by a bracket in this verifier's NOTES section, not by editing the
   worker's text. Requests: image-uab.canadiana.ca 1 (Image 1030 full/max, 200). Vision: 2 crops by this session's own eye.

## R10-CLINV2: verifier of R10-CLIN3868B's three words (6 Oct 2026, account 2, LANE RUN10; clock 08:17-08:2x UTC, `date -u`)

A separate session from R10-CLIN3868B (pp.383-384 cell check, NOTES.md section "R10-CLIN3868B"). No novelty class asked; 3868
stays N0, key `period`, text `known`.

1. **Pre-registration order.** `PREREG_R10-CLIN3868B.md` landed in 10e0744a4 (08:00:46 UTC); the scorer, its JSON, both blind
   pass files and both reconciled files landed in 854780ec0 (08:08:22 UTC). The gate predates the committed score. (The brief also
   named 12d7b9f85; no such object exists in this clone -- 854780ec0 is the only scoring commit.)
2. **Re-score.** `passes/check_3868_p383_384.py --check` exit 0 (re-derives the committed JSON, controls included);
   `check_3868.py` and `check_3868_c36.py --check` exit 0. Blind pass alone: p.383 295/313, p.384 197/201 key-consistent, control
   max 38 and 25 -- the gate passes without the reconciliation, so the reconciliation (key-directed: only cells that failed the key
   were re-read, as on p.382) cannot have made the PASS; quote the reconciled 526/535 with the blind 492/514 beside it. The control
   moves decipherment letters against fixed key letters, so it can differ on this statistic.
3. **Cells eye-checked** (Images 1031, 1032 full/max to the scratchpad; `tools/iiif_lines.py --image ... --region` found 0 lines in
   the figure columns, as the worker reported; PIL box crops, inverted). Against `passes/title1778_reading.txt`:
   - p.383 c7, after the gloss "to the": **7-10 18-10 -11 6-1 4-3** (ruled) = k-i-n-g-s, all clear; then **1-3**, a lone **2**
     set right of and above **15-** with **1** below it, **12**, **9** = p, y (1-2), a (15-1), c, e. The 2 is ambiguous in layout:
     read as 15-2 (n) it gives p-n-a-c-e. Either way five cells spelling PEACE with one slip at position 2.
   - p.384 c6 (P.S.): **18-16 -18 -14**, one letter in clear, **-17 -6 -4** (ruled) = f-l-o-?-u-e-t. The clear letter is a bowl
     with a short rightward tail and no visible descender: its form alone reads a or q. The key page has no q (0 in all 30 lines)
     and has a (18-1, 15-1, ...), so a clear letter is motivated only for q. Graded M on form, the word FLOQUET on the cells.
   - p.384 c6: **21-1 -2 -3 -8** (ruled) = c-o-r-d, clear.
4. **The decipherment, eye-checked** (Images 1033, 1034 full/max; taller crops than the committed line crops, which cut the
   interlinear and the initial). p.385 l.31: the interlinear reads "to the Kings" plainly, above a caret; then "Pya" with a raised
   mark and a struck-through stroke, then "Peace". The decipherer's abandoned "Pya" is the cipher's own p-y-a (1-3, 1-2, 15-1)
   written out literally before the word was recognised: the cipher explains the deleted word. p.386 l.7: "Floquet", the vowel an
   o (the pass B "Flaquet" is not supported). p.386 l.8: "Cord," with a clear capital C (Ford/Cox were crop-edge misreads).
5. **Decision.** Two of the three M words change; the change is to the transcription of the decipherment, settled from the
   decipherment's own image, with the cipher as corroboration (not a repair from the cipher):
   - "{to the Kings[?]}" -> "{to the Kings}" (H).
   - "Floquet[?]" -> "Floquet" (H).
   - "Pyan[?]" stays M: it is a struck, abandoned word; "Pya" + mark + struck stroke is what the page shows, and the cipher
     explains it; not rewritten.
   - "Cord" already carried no [?] in the reading; confirmed, unchanged.
   Edited at the source (`passes/p385_reconciled.tsv` rows p385_L31 and p386_L07, note column), regenerated with
   `passes/check_3868.py`: `p385_reading.txt` and `check_3868.json` change, word grades **H 248 M 4 -> H 250 M 2**; `--check`
   exit 0 for check_3868, check_3868_c36, check_3868_p383_384. Propagated: this file's table row ("reading", 3868) bracketed.
   SECOND-OPINIONS-QUEUE.tsv: 0 rows for this target (grep), nothing to propagate. No safe sentence changes.
6. **Postmortem.** R10-CLIN3868B's NOTES section over-claims nothing; it correctly left the reading file to a verifier. One
   point it did not state: its "peace" mismatch cell admits a second layout reading (15-2) which does not change its counts'
   direction. Requests: image-uab.canadiana.ca 4 (Images 1031, 1032, 1033, 1034 full/max, all 200, browser UA + Referer, 2 s
   apart). Vision: 7 crops by this session's own eye, no subagent.
