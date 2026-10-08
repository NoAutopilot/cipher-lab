# AUDIT -- fr4712-nevers-duchesse (BnF Français 4712 f.10r, Louis de Gonzague duc de Nevers to the duchesse de Nevers)

## AUDIT 1 (D2V-F4712)

Verifier D2V-F4712 (account 2, for LANE DEFAULT-account-2-20261008-0710), 8 Oct 2026, 07:41-07:49 UTC by date -u. A separate
session from the solver (D2-F4712, commit f1d0a70c0). No decoding done here.

**Claim under audit (NOTES.md Verdict line, D2-F4712):** "6 of f.10r's 37 tokens (S1) carry f.13r's H glosses at grade C (82 82
"D. n.", 21 21 "Berry", 12 12 "b. Pal."); pre-registered crib gate met: 6 C >= 3, p 0.029 vs random code sets."

### Step 1 -- extract

| field | value |
|---|---|
| item | fr.4712 f.10r, 37-number cipher passage inside a clear letter (Gallica btv1b9058289m canvas 18) |
| sender / recipient | Louis de Gonzague, duc de Nevers / the duchesse de Nevers (Henriette de Clèves), per the BnF catalogue |
| date | folder says "undated"; **the BnF catalogue (1895) dates it: "La première a une partie chiffrée. Elle est datée du i octobre 1592 et est signée d'un monogramme"** (OCR "i"; day not settled; see step 4) |
| ciphertext | Tomokiyo's printed 37 numbers (`ciphertext.txt`), re-read from the leaf by DUCH-KEY1B (`ciphertext_f10_digits.tsv`) |
| crib source | fr.4712 f.13r (canvas 22 right), "Fragment de dépêche en clair et en chiffre": 34 dotted code numbers with interlinear glosses, two blind passes (`f13_code_gloss.tsv`) |
| carried values | idx 1, 2 = 82 "D. n."; idx 8, 25 = 21 "Berry"; idx 22, 30 = 12 "b. Pal." -- six tokens, **three distinct code values** |
| solver's search | NV-INTAKE 3 Oct 2026: Cryptiana (Tomokiyo: "undeciphered"), Cabinet Noir, both solver repos, DECODE, web/blogs, Gomberville's *Mémoires* (1665) via Books API |

### Step 1a -- the carry itself (pre-registration and reproduction)

- **Pre-registered before the answer: yes.** `PREREG_duchf13.md` is commit 1d4fcd95c (3 Oct 2026 10:59:15 UTC), before any f.13r
  read; the hand condition (c) was recorded in NOTES.md at 893e03750 (11:02:44) before the carry script ran. ASKS row 113 was
  written 3 Oct 2026 with the rule "if same writer, the six H glosses carry at C (gate then met)"; the owner's answer is dated
  5 Oct 2026 04:01 UTC. The rule therefore predates the answer by two days, and D2-F4712 applied it with no new gate (only
  `HAND_SAME = None -> True` changed in `f13_carry.py`, the reason in a comment). Matches prereg (c).
- **Reproduces:** `python3 f13_carry.py --check` -> `OK` (exit 0), run by this verifier 8 Oct 2026 07:4x UTC.
- **Gloss grades:** the three carried codes are H on f.13r by the prereg's rule (both passes same code and gloss): 82 "D. n."/"D. n.",
  21 "Berry"/"Bery" (orthographic variant, allowed), 12 "b. Pal."/"b. Pal. ???" (trailing struck word excluded). Agreed.
- **Gate statistic re-computed independently** (my own script, not the folder's): 6 of 37 S1 tokens fall on f.13r's six H codes;
  p = 0.023 (null 1-99), 0.030 (two-digit null 10-99), 0.038 (null 8-95, f.10r's own range), 20,000 draws each. The solver's caveat
  (null anti-conservative) is right but the p stays <= 0.05 under the fairer nulls. Further descriptive fact: 15 of f.10r's 37
  tokens fall on f.13r's 24-code set at any grade (expected about 10 by chance): weakly consistent with one code system.
- **Rule 3 control:** the rotated-gloss control was correctly declared a non-test for coverage (it cannot change which tokens get a
  gloss); the random-code-set control can differ and was used. Sound.
- **What the gate does and does not show:** the p says f.10r's numbers concentrate on f.13r's glossed codes; it does not show the
  glosses are right *for f.10r*. That rests wholly on prereg (c), same writer, which is one person's "I think the same" against our
  own "leaning different" (open 8 on f.10r vs looped 8 on f.13r) and a NON-TEST machine comparison (R11A-F4712). Grade C is the
  pre-registered ceiling and is correctly applied; it is a conditional C.
- **Counts:** H 0, C 6, S 0, M 0, I 0; 31 of 37 unread (16% at C). Agreed with NOTES.md.

### Step 2 -- independent search (8 Oct 2026)

| family | searched | result |
|---|---|---|
| (a)/(d) holding catalogue | BnF *Catalogue général des manuscrits français, Ancien fonds* t. IV (1895), IA `p1cataloguegnr04bibluoft` `_djvu.txt`, entry 4712 items 9-11 read | f.10 "a une partie chiffrée", dated "i octobre 1592", monogram signature; f.13 "Fragment de dépêche en clair et en chiffre". No decipherment printed or mentioned |
| (f) Cryptiana live | cryptiana.web.fc2.com/code/nevers.htm, fetched live and compared with the 3 Oct mirror | unchanged: f.10 "undeciphered"; f.13 "25 appears to read Paris" |
| (e) Google Books API (`country=US`, key) | "duchesse de Nevers" chiffre "4712"; "fr. 4712" Nevers; "français 4712"; "fr. 4712" chiffre/cipher; "fr. 4712" "fo 10"; "Fr. 4712, f° 13"; "4712, fol. 10"; "octobre 1592" Nevers duchesse chiffre; "Henriette de Clèves" lettres chiffre; "fr. 4712" Boltanski (7 of 22 calls answered 503 and were not retried) | catalogue entries; Boltanski, *Les ducs de Nevers et l'État royal* (2006) cites fr.4712 f°7 (La Vieuville, 6 Mar 1589); T. Hamilton, *A Widow's Vengeance* (OUP 2024) cites fr.4712 f°100 (1593); Rott *Inventaire ... Suisse* cites f°5. **No snippet cites f.10 or f.13 or prints a cipher reading** |
| (e) IA full text (be-api fts) | "duchesse de Nevers" chiffre; "fr. 4712"; "Français 4712"; "4712" "duchesse de Nevers"; the catalogue's own sentence | catalogues and unrelated hits only; no decipherment |
| (e) Gallica SRU | (gallica all "fr. 4712") and (gallica all "Nevers") | the manuscript record itself and unrelated periodicals |
| (g) OpenAlex (keyed) | duchesse de Nevers chiffre; Nevers cipher Gonzague duchess; Henriette de Clèves correspondance; Louis de Gonzague Nevers chiffre | no paper on this letter or its cipher (Boltanski 2006 review only) |
| (b) sender/recipient printed correspondence | Gomberville's *Mémoires de M. le duc de Nevers* (1665), by NV-INTAKE 3 Oct (not repeated) | no letter to the duchess with a cipher passage |
| (f) solver repos, DECODE, blogs | by NV-INTAKE 3 Oct 2026 (not repeated); `sources/decode/keys-all-2026-09-28-merged.tsv` grep: its "4712" is a DECODE record id (Marburg), not this shelfmark | no record |
| unreachable / not run | JSTOR (cloud-blocked; no row queued -- see below); Semantic Scholar, Persée, HAL, CORE not run (cap); Boltanski 2006 not read in full (snippet view only); the f.10 leaf's date line not looked at (no decoding, no vision call) | -- |

No JSTOR row queued: the item is a 6-token lookup with no clause to phrase-search, and a JSTOR row never blocks N3 on its own.

### Step 3 / 3a -- classification and depth

| item | prior plaintext | prior decipherment | N | depth | evidence / confidence |
|---|---|---|---|---|---|
| A. f.10r: six tokens carried from f.13r (82 82 "D. n.", 21 21 "Berry", 12 12 "b. Pal.") | none located | none located (Tomokiyo: "undeciphered"; BnF 1895: "une partie chiffrée") | **N3** | **D1** (16% C; no clause; nothing reads around the three glossed codes, and their f.10r sense is not checked by any context) | moderate on novelty (principal holder catalogue, Tomokiyo, Books/IA/OpenAlex covered; Boltanski not read in full, so not N4); the C grade itself is conditional on one person's same-writer judgement |
| B. f.13r gloss table (24 codes, 6 H) | the glosses are on the leaf itself (period interlinear decipherment) | yes -- period, on the leaf; Tomokiyo already notes "25 ... Paris" | **N0** | n/a (a transcription of a period gloss, not a reading) | high |

Key source (rule 10): item A `period` (the codes' values come from f.13r's contemporary interlinear gloss, transcribed by us; the
carry to f.10r is ours under a pre-registered rule); item B `period`.

Safe sentence (A): "Six of the 37 numbers in the cipher passage of BnF fr.4712 f.10r match codes glossed on f.13r of the same
volume (82 'D. n.', 21 'Berry', 12 'b. Pal.'); on a pre-registered rule and one reader's same-hand judgement they are taken as
those words (grade C, about 16% of the passage); the rest is unread. No prior decipherment located (N3, one audit)."
Unsafe sentence (A): "We deciphered / read Nevers's cipher letter to the duchess" or any wording that names what the passage says,
or "first / new reading".
Outward depth wording: D1, "fragments read". Class without a reading -- not counted as a unique solve (rule 4a).

### Step 4 -- postmortem and corrections

- **Over-claim / error found:** NOTES.md calls f.10 "undated" (title line 5) and DUCH-F13 recorded the prereg (c) date window as
  "unverifiable". The BnF 1895 catalogue, which no session had read at item level, dates the f.10 letter "i octobre 1592" (OCR; the
  day is not settled) and says it is signed with a monogram. This does not change the carry rule (the date condition was recorded
  as unverifiable, not as met, and f.13 is still undated), but the target's title and intake facts were wrong. Corrected in
  NOTES.md (dated note below the title, and a section "D2V-F4712 AUDIT 1"); the title line is left as written with the correction
  beside it, per the folder's convention of not rewriting earlier sections.
- No reading changed. The six C grades stand as pre-registered; the conditional basis (one same-writer judgement vs our 8-form
  observation and a NON-TEST) is now stated in the safe sentence.
- No status.json result row written: the item is a six-token crib lookup (three distinct codes), not a recovered passage or a
  completed reading under the claim_scope rules (tools/verify_backlog.py docstring), and I was not sure it qualifies; the lane
  orchestrator may decide otherwise.
- Second opinion: item A is N3, so `SO-F4712-F10` is queued in SECOND-OPINIONS-QUEUE.tsv in this session
  (`second-opinions/PROMPT-chatgpt-f10.md`).
- Next for a second audit: read Boltanski (2006) for fr.4712 f°10-13; Semantic Scholar/Persée/HAL; look at the f.10 leaf's date
  and monogram (one crop) to settle the day of October 1592.

Requests this audit: cryptiana.web.fc2.com 1; www.googleapis.com 22 (7 answered 503; those queries not retried); archive.org 2
(djvu.txt) + be-api 5; gallica.bnf.fr 1 (SRU); api.openalex.org 4. Vision calls 0.
