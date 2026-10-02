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
