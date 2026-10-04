# AUDIT -- intercepted-royalist-1646 (BL Add MS 72438 f.10, 13 May 1646; f.9, 21 May 1646)

Verifier: VERIFY-ROYALIST-1646 (account 2, for the owner-account orchestrator; brief
`.claude/briefs/runs/2026-10-02-acct3-verify-royalist-1646.md`), 2 Oct 2026, 08:10-08:3x UTC. A separate session from
the account-4 workers that produced the reading (LIKELY-9, GAPS, GAPS2). It does not protect their conclusions.

**Claim under audit (brief wording):** f.10 reads in part with key129 (Aymeloglu, unsolved-ciphers d2800bb2, credited):
190/735 tokens keyed, rank 1 of 21 value-shuffled keys; Evelyn iv pp.178-179 confirms 32 of 65 key rows vs shuffled
mean 0.70; key now C 37 H 22 from the page images.

## Verdict

| item | class | prior plaintext | prior decipherment | key source | text |
|---|---|---|---|---|---|
| f.10, partial reading (192 of 735 cipher tokens carry a key value) | **N0** | no full plaintext located | **yes, of this very item, at the same partial level**: Aymeloglu, github.com/aaymeloglu/unsolved-ciphers `royalist-1646/` (work of 16 Sept 2026, commit d2800bb2 of 27 Sept 2026): `key129.txt` + `apply_key.py key129.txt f10_ct.txt` "renders the partial reading" (his README) | **published** (Aymeloglu's modern reconstruction of the period key no. 129, from f.77 and Evelyn iv 178-179; credited) | unknown (the letter's full plaintext is not in print as far as searched) |
| f.9 | not classified | -- | -- | -- | 12 of 151 tokens keyed, letters only, no signal under key129 (HYPOTHESES.md); nothing read to classify |

**Why N0.** This repository's reading is Aymeloglu's key applied to Aymeloglu's transcription. Running his own
`apply_key.py` (in a scratch clone, not copied here; his repository has no licence, rule 8) and diffing it token by
token against `reading_f10.txt`: identical except (a) two tokens of 111 = "were" (lines 9 and 10) that GAPS added as M,
and (b) 351 "my?" (his doubtful mark) graded C here from the Evelyn page. 190 keyed tokens in his rendering, 192 here.
So the partial decipherment of this item is already public, by the person whose key and transcription it is. What
this repository added is verification, not reading: a matched shuffled-key control for his attribution (rank 1 of 21,
LIKELY-9) and an image check of the key's Evelyn witness (38 of 66 rows match the printed decipherment vs 20 shuffled
keys mean 0.50, max 2; GAPS2), plus one value correction (141 = de, not "desire"; 141 does not occur on f.10).

**Evidence quality / confidence.** High that the reading is not ours (exact reproduction of his rendering). High that no
full decipherment of f.10 is in the sources searched (below). The f.10 transcription is Aymeloglu's, image-unchecked by
anyone here (DECODE images content-blocked to this account, BL viewer offline): every per-token grade is conditional on
it (rule 2).

**Safe sentence.** "A. Aymeloglu identified BL Add MS 72438 f.10 (13 May 1646) as Digby-cabinet key no. 129 and
published a partial reading (unsolved-ciphers, 16-27 Sept 2026). We reproduced it, found that his key beats 20
value-shuffled copies of itself on f.10 (rank 1 of 21), and checked the key's Evelyn-derived values against the page
images of Evelyn's *Diary and Correspondence* iv 178-179 (38 of 66 rows match, shuffled mean 0.5). About three
quarters of the letter (543 of 735 cipher tokens) still has no key value; no full decipherment located."

**Unsafe sentence.** "We deciphered the intercepted royalist letter to Charles I of 13 May 1646" -- or any wording
that makes the partial reading ours, calls it a first or new reading, or says the letter is read.

## Rule 7 re-derivation (this session)

`python3 tools/decode_key.py ciphers/intercepted-royalist-1646 --check`, fresh clone at origin/main c6d683a4:
```
f10_ct.tsv: tokens 735: C 164, H 6, I 12, M 10, U 543
f9_ct.tsv: tokens 151: C 12, U 139
reading up to date
```
exit 0. Reproduces exactly: 0 tokens differ, within the 10 M-graded tokens. Independently, the diff against
Aymeloglu's own renderer (above) differs only in the two M-graded 111 tokens and one grade mark.

## Grades on f.10 (rule 4), as the files stand

C 164, H 6, I 12, M 10, U 543 of 735 cipher tokens; 74 clear fragments. Firm (C + H) = 170. Note on "C": no token is
read from known plaintext *of f.10*; C here means "the value is printed over the same figure in Nicholas's period
decipherment of two other letters in the same key" (Evelyn iv 178-179), i.e. a period key witness. It is as strong as
H for this item, not stronger; the count is right, the label should not be read as "f.10's own plaintext is known".

## Step 1: extract

- Item: BL Add MS 72438 f.10r, intercepted letter to Charles I, 13 May 1646, opens "May it please your Matie", signed in
  cipher (555 697 496). DECODE record 8624 ("Non-decrypted", re-confirmed this session). BL catalogue
  040-001967027 ("Largely in (undecoded) cipher"). Volume: Weckherlin's cipher keys and intercepted royalist
  correspondence (Trumbull Papers vol. 197). f.9r: 21 May 1646, "My Lord", DECODE 8623.
- Key: no. 129 in the Digby-cabinet index f.25 ("without name, from the Queen's Court"); one surviving page f.77
  (names 559-580); the rest reconstructed by Aymeloglu from Evelyn iv 178-179 (the King to Nicholas, 24 June and
  16 Aug 1646, Nicholas's interlinear decipherment).
- Distinctive clear phrases on f.10 (as transcribed): "comfort & encourage your", "resolved to expect your
  Majesty", "done noe great hurt God preserve", "wch is ye earnest prayers of yor sacred Maties most obedient
  servant", "thanks be to God", "Madame Vantelet", "Madame de Brederode", "averse were extream".
- What the solvers searched: NOTES.md "Check-solved sweep, 20 Sept 2026" (six sources: web, CSPD 1645-7 full text,
  Rushworth vi, Cryptiana, Cipher Mysteries, DECODE, both solver repositories, robertpitt) and "Print check,
  20 Sept 2026" (Cary i-ii, Lords and Commons Journals May 1646, IA cross-corpus, TNA Discovery SP 16/514). The
  escalation list's `[ ] print` step (print_check.py on decoded phrases) had not been run.

## Step 2: independent search log (2 Oct 2026, 08:10-08:20 UTC)

| family | searched | result |
|---|---|---|
| (a) canonical series | CSPD Charles I 1645-7 (`calendarofstatep0021will`, full djvu text, 10 phrases) | no hit on any f.10 phrase (only the generic "it is believed that", unrelated entries) |
| (b) sender/recipient correspondence | Bruce, *Charles I in 1646* (`charlesiin1646le00chariala`); Nicholas Papers i (`thenicholaspaper01camduoft`); Evelyn iv (`diarycorresponde41evel`, on disk) | no hit on any distinctive phrase (generic "it is believed" only). Sender unknown, so no sender edition exists to search |
| (c) documentary editions | Cary, *Memorials* i (`memorialsofgreat01caryuoft`); HMC Portland i (`dukeportlandwelb01greauoft`); Calendar of Clarendon State Papers i (`calendarofclaren01bodluoft`) | no hit on any distinctive phrase |
| (d) holding archive / project pages | DECODE RecordsView 8624, login-free (HTTP 200): Status "Non-decrypted"; BL catalogue as quoted in NOTES.md (viewer offline since 2023, not re-fetched) | still listed undeciphered |
| (e) full text | IA full-text search across all items (ia-global) and Google Books API (keyed, `country=US`), 10 phrases via `tools/print_check.py`, plus 4 direct exact-phrase Google Books queries with snippets | "madame vantelet": 34 volumes, all about the Queen's bedchamber woman (Britland, Politics of Female Households 2013; CSPD 1895 legacy entry; Ellis), none quoting this letter; "done noe great hurt": 3 volumes, all HMC Finch (a different, later letter about Kinsale); "resolved to expect your majesty": no exact hit; the long signature phrase: Google Books HTTP 503 (unsearched) |
| (f) solver repositories and cipher blogs | aaymeloglu/unsolved-ciphers cloned at d2800bb2 (the N0 source above); dbourdeau/cyphersolver cloned at 34e0fc89 (1 Oct 2026): `targets/rupert/NOTES.md` #6 still "offline-only", no key, no reading; Cryptiana `unsolved.htm` live (HTTP 200): f.9 and f.10 still "I believe is not deciphered"; Cipherbrain site search "Weckherlin": no results | only Aymeloglu's partial reading exists |
| (g) scholarship | OpenAlex (keyed): 10 phrases + "Add MS 72438" (0), "Weckherlin cipher keys Digby" (0), "royalist intercepted letters 1646 cipher Charles I deciphered" (5 works, none on this letter); Semantic Scholar: 7 phrases answered, then HTTP 429 (3 unsearched); CrossRef: HTTP 429 (unsearched); JSTOR: two rows appended to JSTOR-QUEUE.tsv (families i and ii) | no work on this letter's decipherment located; S2 partial, CrossRef unreachable, JSTOR queued |

Outputs on disk: `phrases.txt`, `sources.tsv`, `print-check.tsv`, `print-check-hosts.tsv` (requests: archive.org 6,
be-api.us.archive.org 10, googleapis 10 + 4 direct, api.openalex.org 12 + 3 direct, api.semanticscholar.org 10 (429),
api.crossref.org 1 (429)); plus de-crypt.org 1, cryptiana.web.fc2.com 1, scienceblogs.de 1, github.com 2 clones.
A search result, not a novelty verdict beyond the class above.

Why the class is not higher regardless of the searches: N0 is fixed by Aymeloglu's own repository; the searches above
bear only on whether a *full* period or modern decipherment exists (none located), which is what the next step on
this target (the rest of key 129, or f.11's possible decipher) would need.

## Step 4: postmortem and corrections

1. **Stale figures in the claim.** "Evelyn confirms 32 of 65 key rows vs shuffled mean 0.70" is GAPS's OCR-conditional
   figure, superseded the same morning by GAPS2's page-image figure: **38 of 66 rows match the page (37 graded C +
   141 = de by segmentation) vs 20 shuffled keys mean 0.50, max 2**. "190/735 keyed" is LIKELY-9's; the files now
   give **192/735** (two 111 = were, M). Corrected in NOTES.md line 3 (it read "confirms 37 of its 66 rows", which
   mixed the C-row count with the match statistic). status.json's results entry still carries "32/65 ... 0.70": the
   orchestrator's file, flagged in the ROOM done line, not edited here.
2. **Whose reading.** The folder says "every value here is Aymeloglu's" (LIKELY-9) but nowhere says his repository
   already renders the same partial reading of f.10. It does; that is what makes this N0. The kind of result is
   **contribution** (a control and an image check for a published attribution, one value correction), not recovery
   or cryptanalysis of ours. No sentence in the folder over-claims novelty (grep for new/novel/first/solved/
   unpublished/previously unread: none in that sense).
3. **"C" label** reads stronger than it is for this item (section above); no count change.
4. **Intake-gate mis-parse** (line 137 quoting Bourdeau's "offline-only") already flagged three times by the workers;
   still open in `tools/intake_gate_check.py`, not touched here (other files out of scope).
5. **No SECOND-OPINIONS-QUEUE.tsv row** exists for this target and none is owed (class N0, below N3). Nothing to
   propagate.

## Outreach

Nothing to post as a reading. If anything goes to Aymeloglu, it is a contribution note (the shuffled-key control
numbers, the image check of his Evelyn values, 141 = de, and the OCR-vs-page digits 422/162/356 that he already read
correctly), through the outreach gates, never as a reading of ours.

# AUDIT 2 (A3V-VROY2, 4 Oct 2026): f.10 partial reading

Verifier: A3V-VROY2 (account 3 worker for LANE-A3V; brief `.claude/briefs/runs/2026-10-04-acct3-a3v-wave1.md`),
4 Oct 2026, 02:53-03:01 UTC. A separate session from the solvers (LIKELY-9, GAPS, GAPS2) and from audit 1
(VERIFY-ROYALIST-1646). Its job was to test audit 1's N0 adversarially, not to protect it.

**Claim under audit:** audit 1's verdict, N0, key source published: the f.10 partial reading is Aymeloglu's own key
applied to his own transcription (his `apply_key.py`).

## Verdict

| item | class | prior plaintext | prior decipherment | key source | evidence quality / confidence |
|---|---|---|---|---|---|
| f.10, partial reading (192 of 735 cipher tokens carry a key value) | **N0, confirmed** | no full plaintext located (no period or printed decipherment found in any family below) | **yes, of this very item, at the same partial level**: A. Aymeloglu, github.com/aaymeloglu/unsolved-ciphers `royalist-1646/` (key identified and partial key, commit 16ec608, 16 Sept 2026; folder last changed c1f25e4, 18 Sept 2026; repository HEAD d2800bb2, 27 Sept 2026, which is the commit our transcription quotes) | **published** (Aymeloglu's modern reconstruction of the period key no. 129, credited) | high: reproduced token for token this session (below); search negative is a search result |
| f.9 | not classified | -- | -- | -- | nothing read (12/151 letter tokens, no signal) |

**Credit line.** A. Aymeloglu, *Intercepted royalist letters, May 1646 (BL Add MS 72438 ff. 9-10): key identified,
partial reading*, github.com/aaymeloglu/unsolved-ciphers, folder `royalist-1646/` (work of 16 Sept 2026, commit
16ec608; solvers ported 18 Sept 2026, c1f25e4; cited at HEAD d2800bb2, 27 Sept 2026). Repository has no licence:
cited, no code copied (rule 8).

**Safe sentence (unchanged from audit 1, one figure added).** "A. Aymeloglu identified BL Add MS 72438 f.10 (13 May
1646) as Digby-cabinet key no. 129 and published a partial reading (unsolved-ciphers, 16-27 Sept 2026). We reproduced
it (731 of 735 tokens identical), found that his key beats 20 value-shuffled copies of itself on f.10 (rank 1 of 21),
and checked the key's Evelyn-derived values against the page images of Evelyn's *Diary and Correspondence* iv 178-179
(38 of 66 rows match, shuffled mean 0.5). About three quarters of the letter (543 of 735 cipher tokens) still has no
key value; no full decipherment located."

**Unsafe sentence.** "We read (or deciphered) the 13 May 1646 letter to Charles I" -- or any wording that makes the
partial reading ours, or implies f.11 or any other leaf holds its contemporary decipherment (see finding 2).

## Step 1: reproduction test (the N0 basis)

Cloned github.com/aaymeloglu/unsolved-ciphers to the scratchpad only (HEAD d2800bb2, 27 Sept 2026 22:57 -0500; the
`royalist-1646/` folder's last commit is c1f25e4, 18 Sept 2026). Ran his own renderer unmodified:
`python3 apply_key.py key129.txt f10_ct.txt` (exit 0). Parsed his output (clear text in [brackets] dropped,
`<n>` = unkeyed) and compared token by token against our committed `reading_f10_tokens.tsv` (clear rows dropped):

| | count |
|---|---|
| cipher tokens, his / ours | 735 / 735 (signs agree at every position) |
| identical (value or both unkeyed) | **731** (U 543, C 160, I 12, M 10, H 6) |
| differ | **4**: 111 = "were" at 9:29 and 10:41 (unkeyed in his key129.txt, "were" C here from GAPS2's Evelyn page read); 351 at 8:13 and 11:22 ("my?" in his rendering, "my" C here from the Evelyn page) |
| keyed tokens, his / ours | 190 / 192 |

Our own `python3 tools/decode_key.py ciphers/intercepted-royalist-1646 --check` (origin/main 0629ef40): "f10_ct.tsv:
tokens 735: C 164, H 6, I 12, M 10, U 543 ... reading up to date". So the reading is his, plus two values and two
grade upgrades from our image check of his own named witness. N0 stands.

## Step 2: independent search log (4 Oct 2026, 02:54-03:00 UTC)

Audit 1's families (CSPD 1645-7, Bruce, Nicholas Papers i, Evelyn iv, Cary i, HMC Portland i, Clarendon calendar i,
IA global, Google Books, OpenAlex, S2, DECODE, Cryptiana, both solver repositories) are not repeated; this pass
searched what audit 1 did not.

| family | searched (this session) | result |
|---|---|---|
| (a) canonical series | Thurloe State Papers i (1742, `bim_eighteenth-century_a-collection-of-the-stat_thurloe-john_1742_1`); *State Papers collected by Edward Earl of Clarendon* (`10622705bsb`, 150 mentions of 1646); Calendar of the Committee for Compounding (`cu31924024797890`): `tools/print_check.py --only ia`, 8 phrases (madame vantelet, madame de brederode, madame dona, comfort and encourage your majesty, resolved to expect your majesty, done noe great hurt, averse were extream, have done no great hurt god preserve), plus a direct grep of each djvu text for Vantelet/Ventelet, Weckherlin, "13 May 1646" | no hits. Thurloe's 22 "Brederode" are unrelated Dutch affairs; Clarendon SP: no Vantelet, no decipherment of a 13 May 1646 letter |
| (b) sender/recipient correspondence | *Letters of Queen Henrietta Maria* (Green 1857, `lettersofqueenhe00henr`); Montereul correspondence ii (`diplomaticcorres02mont`); vol. i (`diplomaticcorres01mont` djvu HTTP 500; alternate copy `diplomaticcorres01montiala` searched instead) | no phrase hits; Green's one "Ventelet" is a 1629 errand, Davenant hits are 1642-46 messenger mentions, none quoting this letter. Sender unknown, so no sender edition |
| (c) documentary editions | Commons Journal iv on British History Online, read from the page (`commons-jrnl/vol4/pp553-555`, HTTP 200): "Die Lunae, 25 Maii, 1646. A Letter from Sir Thomas Fairfax ... of 22 Maii 1646, with several intercepted Letters inclosed, was this Day read ... Ordered, That the several intercepted Letters in Characters be delivered over to Sir Walter Erle; to the end the said Letters in Cypher may be decyphered. And the said Letters were delivered to Sir Walter Erle accordingly; being Five in Number." pp555-556 (26 May) has no report. The 30 May report (Erle on Nicholas to Ashburnham, 15 May, per Aymeloglu's README) was not reached (page navigation failed, stopped after 3 requests), so cited, not re-verified; Montereul i alternate copy (`diplomaticcorres01montiala`) searched: no hits | a Parliamentary decipherment of five May 1646 intercepts was ordered; none of f.10 located in print. If Erle's decipher of f.10 was made, it would be a manuscript, not an edition |
| (d) holding archive | BL catalogue JSON, searcharchives.bl.uk/catalog/040-001967027?format=json (HTTP 200): "f. 10r: Intercepted letter to King Charles I, 13 May 1646. Largely in (undecoded) cipher." and **"ff. 11r-v; Letter of King Charles I to James Butler, 1st Marquess of Ormond, Lord Lieutenant of Ireland. n.d. [1645, after 27 Feb]. Endorsed as a copy of the King's letter to Ormond."** Deciphered or partly decoded leaves in the volume are ff.1, 4, 5-6, 7, 12-13, 14-15, 19, 107 ("partially decoded, n.d.", DECODE 8728, already known Decrypted), 171 ("limited deciphering, n.d.") | f.10 still undecoded at the holding archive; **f.11 is not a decipherment of f.10** (finding 2) |
| (e) full text | Google Books API (keyed, `country=US`): "Add MS 72438" (3 volumes: Turnbull, *Prince Rupert of the Rhine* 2025; Britland, *Women Writing in a Time of War, 1642-1689* 2025; Gentles, *The English Revolution and the Wars in the Three Kingdoms* 2014; all snippets bibliography entries); "Vantelet" "Brederode" 1646 (0); "Davenant" "13 May 1646" (Clarendon calendar and unrelated); "letter to the King" "13 May 1646" cipher (HMC/Lords MSS, unrelated); "Weckherlin" intercepted 1646 (Leibniz volume, Erle/Weckherlin background only); Britland + Weckherlin/Vantelet + cipher (0); 3 queries HTTP 503 (unsearched) | no quotation or decipherment of f.10 in any snippet. Whether Britland 2025 or Turnbull 2025 discuss f.10 in their text is not determinable from snippets (PARTIAL view); both cite the volume only in bibliographies as far as seen |
| (f) solver repositories | aaymeloglu/unsolved-ciphers re-cloned (the N0 source); Bourdeau's repository not re-cloned (audit 1, 2 Oct, 34e0fc89: no reading) | as audit 1 |
| (g) scholarship | OpenAlex (keyed): "Weckherlin cipher" (5), "Weckherlin decipherer parliament" (4), "intercepted royalist letters 1646 cipher Henrietta Maria" (4). Read in full: Carlton, "An Anglo-Dutch Power Couple", *Early Modern Low Countries* 2025 (doi 10.51750/emlc19227, OA PDF): cites Add MS 72438 ff.76r and 89v (Heenvliet's key) and Add MS 33596 f.38v, never f.10. Ellis, *Military intelligence operations during the first English Civil War 1642-1646* (Southampton PhD 2010, eprints 361576): PDF HTTP 403, unsearched. CrossRef "Weckherlin cipher intercepted 1646": 5 rows, reference-work entries only. JSTOR: audit 1 already queued one row in each family (JSTOR-QUEUE.tsv rows 139-140, both `queued`), so none added | no work on this letter's decipherment located; Ellis unreachable |

Requests this session: github.com 1 clone; archive.org 8 + be-api.us.archive.org 8; www.british-history.ac.uk 6 (3 of them a failed next-page walk); searcharchives.bl.uk 1;
www.googleapis.com 16 (3 HTTP 503, plus 6 wasted no-op volume calls by a script error, no result used);
api.openalex.org 4; api.crossref.org 1; emlc-journal.org 1; eprints.soton.ac.uk 1 (403, not retried). Subagent
calls: 0. Downloaded djvu texts are cached under `sources/ia-fulltext/print-check/` by print_check.py.

## Step 4: postmortem and corrections

1. **Audit 1's diff description is stale in two details, not in substance.** It said the two 111 = "were" tokens were
   M; key.tsv now grades 111 C (source evelyn-img, GAPS2), and the token file agrees. It said 351 "my?" was one grade
   mark; it is two tokens (8:13, 11:22). Totals unchanged (190 vs 192 keyed). Corrected here; audit 1's text left as
   written.
2. **f.11 is not the contemporary decipherment of f.10 -- found, partly applied.** NOTES.md (the "Remaining gaps"
   line "the contemporary decipher of f.10 (f.11; ...)") and REQUEST.md item 1 ("f.11 -- ... the likely contemporary
   decipher of f.10's letter ... directly finishes f.10's partial reading") rest on Aymeloglu's guess ("not a DECODE
   record, so probably plaintext, possibly Weckherlin's decipher of f. 10"). The BL's own catalogue entry says
   ff.11r-v is a copy of Charles I to Ormond, [1645]. A dated note is appended to both places (no line removed); the
   order priority itself is the orchestrator's call. The other leads in that gap line (Bodleian Tanner MSS 59-60,
   TNA SP 16/514) are untouched by this finding.
3. **Over-claim grep.** No sentence in the folder calls the reading ours, new, first or solved; the NEAR.md row and
   the PROGRESS.tsv note say N0 and Aymeloglu's. Nothing to correct beyond finding 2.
4. **No SECOND-OPINIONS-QUEUE.tsv row** owed (N0, below N3).
5. **Leads for the solver side, not run (Usage 7):** Bodleian Clarendon MS 95 (Heenvliet's Hague letter-book
   1642-51, 567 letters, per Carlton n.51) is a Hague-court source in the same circle as f.10's names (Brederode,
   Dona, Vantelet, "Mylord"); BL Add MS 33596 ("Royalist cipher keys", f.38v per Carlton) is a royalist key
   collection not yet in NOTES.md. Neither is a decipherment of f.10.
