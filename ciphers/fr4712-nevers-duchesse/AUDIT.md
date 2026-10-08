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

## AUDIT 2 (second adversarial, V1-F4712)

Verifier V1-F4712 (account 3, Opus, session_012yTB3tLbwovJXT9yadjBGT, for LANE-VERIFY-1), 8 Oct 2026, 16:10-16:3x UTC by date -u.
A separate session from the solver (D2-F4712), the first auditor (D2V-F4712) and every earlier worker on this folder. No decoding
done here; no key applied to f.10r. Claim under audit: AUDIT 1's safe sentence for item A (six tokens at C, N3, D1).

### Prior-work checks 3-5 (`tools/prior_work.py` does not exist; checks run by hand)

| check | route | query / what was read | result |
|---|---|---|---|
| 1 own work | repo grep (NOTES, AUDIT, HYPOTHESES, ROOM, status.json, WORK-QUEUE) | "fr4712", "4712", "f.35", "Lasry", "no.71" | folder work as AUDIT 1 lists; no status.json row for this target; **no session ever considered the two other ciphers of the same volume** (f.7 = Nevers collection key no.71; f.35 = 1592, solved by Lasry 2022) |
| 2 leaf / neighbours | disk only (Gallica 403 to the cloud on 8 Oct; no probe spent) | `images/src_ark_..._f18_4100_2750_3300_560.jpg` (cipher lines of f.10r) | the crop shows the three cipher lines and the clear text around them, no gloss, no date line; **the day of October 1592 is still not settled from disk** (no crop of the date line exists) |
| 3 Tomokiyo cache | `sources/cryptiana/web/nevers.htm`, `GL.htm`, `unsolved*.htm`, `READABLE.tsv`, `blog/` | "4712" | nevers.htm: f.10 "undeciphered" (unchanged); f.13 "25 appears to read Paris"; **f.35 (1592, "Monsieur Pasquier ... des finances") "In 2022, George Lasry solved this"**; GL.htm prints Lasry's key image (30/05/2022) |
| 3a Lasry's f.35 key (cryptiana.web.fc2.com, 2 requests: `GL/GL_BnFfr4712_f35.png`, `..._decipher.png`, viewed, not committed) | form only, not applied | the key is a one-symbol-per-letter substitution (A-X with homophones, doubled letters FF LL MM NN RR, ~15 nulls, "DE?", "LE/SS", "LETTRE?"), no two-digit code numbers | **design mismatch with f.10r** (two-digit numbers 8-95 plus two signs), so f.35's key is not a candidate for f.10r and Lasry's solve is not a prior decipherment of f.10r. Checked by form, not by trial |
| 3b f.7 / key no.71 | nevers.htm text ("Figures with an overbar are used to represent names and words (in French). Used in an unsigned letter in BnF fr.4712, f.7"); Cabinet Noir holds the no.71 key (NV-INTAKE) | -- | **unchecked as a key for f.10r**: same volume, two-digit figures for names and words, never applied or ruled out by any session (the folder's known-keys line covers nos.1 and 4 only). A lead for a solver, not a verifier's step; it does not change item A's class (no prior decipherment of f.10r exists either way) |
| 3c solver repos, DECODE | by NV-INTAKE 3 Oct (not repeated) | -- | nothing for f.10 |
| 4 edition / calendar | Google Books API (key, `country=US`), 19 queries, 1 answered 503 and was retried once (answered) | Nevers to the duchess 1592; "duc de Nevers" "à sa femme" 1592; "lettres du duc de Nevers" duchesse 1592; "fr. 4712" + f° 10 / fol. 10 / f° 13 / fol. 13; "Français 4712"; "ms. fr. 4712"; Boltanski "ducs de Nevers" "4712" | catalogues; Henri IV *Lettres missives* (Berger de Xivrey) to Nevers, Jan 1592 (not October, not to the duchess); Boltanski 2006 cites fr.4712 f°7 only; Hamilton 2024 f°100; *Practiques et practiqueurs* (2002) f°36; Gondi 1953 f°4; Champion (1942/43) the Henri III "pensées". **No snippet cites f°10 or f°13 or prints a passage of a Nevers letter to the duchess of October 1592.** Positive control: the catalogue's own fr.4712 entry is returned for "Français 4712" Nevers duchesse (found) |
| 5 G3 -- phrase context of the six tokens | Google Books (same pass) | "octobre 1592" Nevers "Berry"; "octobre 1592" "duc de Nevers" "duchesse"; Nevers 1592 "Berry" "La Châtre" octobre; "Henriette de Clèves" 1592 Berry; "transfert de la monnaie de Bourges à Nevers"; "Nevers" "Bourges" "octobre 1592" "bureau des finances"; Nevers 1592 "baron de" "Berry" chiffre lettre duchesse | **context, not prior text:** royal letters of **9 October 1592** moved Bourges's bureau des finances, élection and mint (the Berry institutions) to Sancerre, Issoudun and **Nevers** (*Mémoires de la Société historique du Cher* 1868; *Bulletin de la Société nivernaise* 1869/1896 print the lettres patentes "pour le transfert de la monnaie de Bourges à Nevers"). Same month as f.10 ("i octobre 1592", BnF 1895) and it shares "Berry" with a carried gloss; but "Nevers" is the sender, so it is one rare entity, not two, and the day of f.10 is unsettled -- not SUBSTANCE by the ±3-day two-entity rule. It prints royal letters, not Nevers's letter to his wife; nothing to diff. Logged as a reading lead (what f.10's "Berry" may concern), not as prior plaintext |
| 5 G3 -- other families | IA advancedsearch 3, be-api fts 3 (1 answered 502, 1 answered 503, not retried); OpenAlex (key) 4; Semantic Scholar (key) 3 (2 answered 429, not retried); HAL API 3; Persée site search 2 | "duchesse de Nevers" 1592 chiffre; "fr. 4712" Nevers; "ms. fr. 4712"; "monnaie de Bourges" Nevers 1592; Louis de Gonzague lettres chiffrées duchesse; Henriette de Clèves correspondance; Nevers cipher letter duchess 1592 | IA: 0 metadata hits; fts hits are numismatic catalogues on the 1592 mint transfer. OpenAlex: nothing on this letter. S2: only Desenclos & Lasry, "An early French digit cipher: deciphering a letter from the King of France to the Duke of Nevers (1592)" -- a Henri IV letter, already logged by NV-INTAKE, not this one. HAL 0. Persée: an OR search, no article on fr.4712 or this letter |
| unreachable / not run | Gallica (403 to the cloud 8 Oct; images from disk only); JSTOR (cloud-blocked; no row queued: no clause to phrase-search, a 6-token lookup); Boltanski 2006 full text (snippet view only, its index for "4712" returns f°7 alone); CORE (no key here) | -- | -- |

### Classification (second audit)

| item | prior plaintext | prior decipherment | N | depth | change |
|---|---|---|---|---|---|
| A. f.10r six tokens from the f.13r gloss | none located | none located; the only modern solve in the volume (Lasry 2022, f.35) is a different cipher design | **N3** (kept) | **D1** (kept) | none. Not raised to N4: Boltanski 2006 still not read in full, key no.71 on f.10r neither tried nor excluded, and the f.10 date is not settled |
| B. f.13r gloss table | on the leaf | period | N0 | n/a | none |

Key source: item A `period` (unchanged). Safe sentence: AUDIT 1's, with "two audits" in place of "one audit". Unsafe: as AUDIT 1.
Depth stays D1 (16% at C, no clause; depth-bar file not consulted for a raise, none was attempted).

### Postmortem and corrections

- **Gap found (premise check, not an over-claim):** NV-INTAKE's premise check (c) named f.7 (no.71) as a neighbour, and nevers.htm
  says Lasry solved f.35 of the same volume in 2022, but no session logged either as a known-key check for f.10r. f.35's key is
  ruled out here by form (letter substitution, not a two-digit code); no.71 is left as an untried known key -- added to NOTES.md
  "Escalation" as a [ ] line for the lane orchestrator, not run (do not decode).
- AUDIT 1's statements all held on re-search; the date correction ("i octobre 1592") stands, day still unread.
- SO-F4712-F10 (SECOND-OPINIONS-QUEUE.tsv row 84) left as queued: the class did not move.
- No status.json row exists for this target; none written (AUDIT 1's reasoning: a six-token crib lookup; the lane orchestrator's
  call).

Requests this audit: cryptiana.web.fc2.com 4 (2 http->302, 2 https 200); www.googleapis.com 20 (1 answered 503, retried once);
archive.org 3 + be-api 3 (one 502, one 503); api.openalex.org 4; api.semanticscholar.org 3 (two 429); api.archives-ouvertes.fr 3;
www.persee.fr 2; gallica.bnf.fr 0. Vision calls 3 (two Cryptiana key images, one f.10r crop from disk).
