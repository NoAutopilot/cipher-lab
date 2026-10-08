# AUDIT: Nationaal Archief 3.01.14 (Archief Johan van Oldenbarnevelt) inv. 2442, Senisteros to Pena, 23 Dec 1605 (copy), blocks B and C1

Class (rule 10): **blocks B and C1: N3** (no prior plaintext and no prior decipherment located after the logged search
below). Key source: **ours** (the a=4, e=8, i=3, o=7, u=2 vowel-digit key was recovered by this project's cryptanalysis,
VX-CT03, 25 Sept 2026; no period key, gloss or published key exists for it as far as searched). Text: not known in print.
Blocks A and C2 are out of scope (not re-read from the image yet) and are not classified here.

Verifier VERIFY-OLD (account 2, LANE-A2PUSH), 3 Oct 2026, 00:02-00:10 UTC. This session did not solve the target, did
not decode and did not re-read the image. Claim under audit (NOTES.md sections 8-9; brief
`.claude/briefs/runs/2026-10-03-acct2-verify-old.md`): "blocks B and C1 of NA 3.01.14 inv. 2442 (1605) read from the
image (transcription/passD_image_A2OLD.tsv, reading.txt); A2-OLD2 re-derivation byte-identical (apply_key.py --check);
print check on 13 phrases found no print of the letter."

## 1. Verdict

| item | class | prior plaintext | prior decipherment | key | evidence quality | confidence |
|---|---|---|---|---|---|---|
| inv. 2442, block B (folio 55, 95 tokens) | **N3** | none located | none located | ours | cryptanalytic, single image reader + one partial blind check; judge FAIL | moderate on novelty; reading itself is a candidate |
| inv. 2442, block C1 (folio 56 first passage, 61 tokens) | **N3** | none located | none located | ours | as B | as B |

**Why not N0/N1.** Nothing on the 11 scans deciphers the letter (NOTES "Premise check" (c), all 11 scans viewed, no
gloss, no clear copy, no key). The holding archive's own description says only "1. In het Spaans. 2. Merendeels in
cijferschrift" (EAD of 3.01.14, fetched 3 Oct 2026, and the printed inventory, *Archief van Johan van Oldenbarnevelt,
1586-1619: Inventaris 2*, 1984, Google Books `2nUsAAAAYAAJ`, snippet carrying the same note). The same EAD marks other
items "Gedeeltelijk gedecodeerd" and "bij de missive ... bevindt zich een sleutel", so its cataloguers did record
decipherments and keys where they existed; for inv. 2442 they recorded none. No edition located prints the letter.

**Why not N4.** (i) The Spanish side was not covered: the sender ("Don Juan Gara de Senisteros", writing from Alcalá;
"Gara" is very likely the abbreviation of García, but his identity is not established) and the recipient (Juan de la
Peña) have no identified printed correspondence, and the Spanish archive portal (PARES) is a dead host from the cloud
(CLAUDE.md host table), so a surviving original or another copy in Simancas or elsewhere was not searched for.
(ii) Semantic Scholar answered 429 on three of seven queries (one retry, still 429; not retried further).
(iii) JSTOR rows are queued, not answered (they do not block N3, CLAUDE.md verifier template). (iv) No specialist or
archive has been asked.

**Why the reading is still only a candidate (not a novelty question, recorded so the class is not over-read).** The
whole-letter judge FAILs (-1.204 vs real_p05 -0.827; B+C1 alone -1.087 vs -0.843, NOTES section 8), on an `es` corpus
that is not era-matched (rule 3, pt18/es17c lessons); B/C1 token grades (B S90/M4/I1, C1 S53/M6/I2) are one reader's
confidence from one image pass, with one blind subagent check on the uncertain spots only. The key itself is well
supported (dictionary confirmations; VX-CT03 control recovered 100% of digit positions at N=325, K=7, clean and with
37.3% crib noise), so the open risk is transcription, not key. N3 is a statement about print and prior decipherment,
not about the accuracy of every word.

## 2. Extracted from the repo

- Date and place: Alcalá, 23 Dec [1605] (signed close on scan 11: "Alcalá ... 23 de [dic.] de 605 ... D. Juo Gara de
  Senisteros"). From Don Juan Gara de Senisteros to Juan de la Peña. A contemporary copy ("afschrift, begin 17e eeuw")
  in Oldenbarnevelt's papers.
- Archive identifiers: NA 3.01.14 inv. 2442; handle `http://hdl.handle.net/10648/ec558817-c1f4-42d4-a770-a4e0e38ae6b0`;
  item page `https://www.nationaalarchief.nl/onderzoeken/archief/3.01.14/invnr/2442`; scan 2 (folio 55, block B) and
  scan 6 (folio 56, block C1) in `images/`.
- Cipher: vowels written as digits (a=4, e=8, i=3, o=7, u=2) inside otherwise plain Spanish words; in B/C1 "5" is the
  hand's final s, "6" the hand's b, `2s`+superscript a = "V.Sª" (NOTES section 8).
- Plaintext as read (B): "la he dicho que solo desseo uer aca a V.Sª, i ella lo dessea arto, i se lamenta de uer los
  tiempos que corren, i me enuio el pesame delo desigu enca [de Siguenca], porque hubo del mui buenas esperancas; i muchas ueces no
  pueden, i otras ueces no se atreuen a ablar al duque con ueras ... i assi no ai sino paciencia i hacer lo que
  pudieremos comforme a los tiempos." (C1): "... i le besaua las manos. Estas dos cossas he hecho por ser tan
  conuinientes en esta occassion ... supplico a V.Sª me perdone quen decirlo a V.Sª pudiendolo callar. Uera V.Sª [?]la
  uerdad que procedo, i con quantos desseos de acertar a seruir a V.Sª i darle gusto en todo-".
- Distinctive phrases: the 13 in `phrases.txt`; names Sigüenza, Vanegas, Pamplona, Mattheo de Burgos (A block context).
- What the solvers searched (sections 3, "Web and blog check", "Premise check", 9): Lonchay & Cuvelier t. I (full djvu
  grep); Huygens Bescheiden Oldenbarnevelt (Senisteros/Sinisteros/Pena/Gara/cijferschrift); NA neighbours 2435-2450 by
  title; WebSearch (7 queries + 3 blog site searches); both solver repositories (grep); `tools/print_check.py` on 13
  phrases (IA full text, Google Books, OpenAlex, CrossRef; Semantic Scholar 429), 2 Oct 2026.

## 3. Independent search log (this session, 3 Oct 2026)

| family | searched | result |
|---|---|---|
| (a) canonical series | Huygens retroboeken `statengeneraal` (Resolutiën der Staten-Generaal, all volumes incl. Deel 13, 1604-1606) and `oldenbarnevelt` (Bescheiden, 3 vols), `searchText` accessor, terms Senisteros, Cisneros, "de la Pena", "de la Peña", Alcala, onderschept; positive control "Spinola" (277 and 41 hits) | 0 hits for every name in both; "Alcala" 8 hits in SG, all 1617-18 (Carel van Crakau), unrelated; "onderschept" 13 hits in SG, the one in Deel 13 (p.284) concerns intercepted riders' letters, unrelated |
| (b) sender's and recipient's printed correspondence | Google Books (keyed, `country=US`): "Senisteros" (42; the top results are all Latin etymology, *\*senisteros*), "Gara de Senisteros" (1: the NA printed inventory only), "Garcia de Cisneros" 1605 Alcala (7, unrelated), "Juan de la Peña" 1605 Alcalá carta (119, none this letter); OpenAlex "Senisteros", "Garcia de Cisneros Alcala 1605", "Juan de la Peña 1605 Alcalá"; IA full text "Senisteros" (Latin linguistics only), "Gara de Senisteros" (0) | no printed correspondence of either party located; sender identity unresolved |
| (c) documentary editions | Lonchay & Cuvelier t. I (solvers' full grep, accepted; not re-run); Resolutiën SG (row a); Bescheiden Oldenbarnevelt (row a) | not found |
| (d) holding archive | NA item page (drupal-settings-json `unittitle`) and the full EAD of 3.01.14 (`/onderzoeken/archief/3.01.14/download/xml`, 4.97 MB), grepped for 2442, Senisteros, Pena, cijfer; printed inventory 1984 via Google Books snippet | description: "In het Spaans. Merendeels in cijferschrift." No decipherment or key recorded for 2442 (contrast other entries marked "gedecodeerd" or "sleutel") |
| (e) full text: IA, HathiTrust, Google Books | IA be-api fts: "se lamenta de uer los tiempos" (0), "andan al aire de su gusto" (0), "pudiendolo callar" (4 hits: a 1964 Uruguayan gazette and Ramos/obra poética, unrelated); Google Books exact phrases in period and modern spelling: "se lamenta de uer los tiempos" / "se lamenta de ver los tiempos que corren" / "no se atreven a hablar al duque con veras" / "andan al aire de su gusto" / "pudiendolo callar" "acertar a servir" / "pesame de lo de Siguenza" | no hit shows this letter (top hits are scattered-word matches: Suárez de Figueroa 1615, Cortes diaries, dictionaries, Miró). HathiTrust full text: unreachable from the cloud (Cloudflare), not tried |
| (f) solver repositories and cipher blogs | fresh depth-1 clones of dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers grepped for senisteros, oldenbarnevelt, 3.01.14, "juan de la pe"; DECODE cached catalogue listings (`sources/decode/records-*-2026-09-24.tsv`, 2,548 rows) grepped for oldenbarnevelt, senisteros, 3.01.14; WebSearch ×3 (sender/name, two decoded phrases, NA 3.01.14 intercepted cipher) | one repo hit: Benedict XIII material naming the monastery San Juan de la Peña (c.1400), unrelated; no DECODE record for this item; web: nothing about this letter |
| (g) scholarship | OpenAlex (keyed) 7 queries; Semantic Scholar (keyed) 7 queries, 3 answered 429 after one retry; CORE (keyed) 3; CrossRef 2 (one 429, retried once: no item about this letter) | nothing about this letter. Context only: *L'art de deschiffrer* (2026, doi 10.18290/rh26742.5), a Spanish-Netherlands deciphering treatise, not this letter |
| (g) JSTOR | 4 rows appended to `JSTOR-QUEUE.tsv` (2 of family i, 2 of family ii) | queued; does not block N3 |

Requests by host this session: www.googleapis.com 14, api.openalex.org 7, api.semanticscholar.org 10 (5 x 429),
api.core.ac.uk 3, api.crossref.org 3 (1 x 429), be-api.us.archive.org 7, www.nationaalarchief.nl 2,
resources.huygens.knaw.nl 25, github.com 2 (clones), WebSearch 3.

## 4. Safe and unsafe sentences

- **Safe:** "Blocks B and C1 of Nationaal Archief 3.01.14 inv. 2442 (a copy of Don Juan Gara de Senisteros to Juan de la
  Peña, Alcalá, 23 December 1605) read, under a vowel-digit key we recovered, as a personal letter about the duke's
  household, a condolence over a Sigüenza matter and the writer's service to 'V.Sª'; no prior decipherment or print of
  the letter was located after the search logged in AUDIT.md (N3). The reading is cryptanalytic, from one image pass,
  and fails our language judge on a corpus not matched to its era."
- **Unsafe:** "We have deciphered a previously unread Spanish intelligence letter from Oldenbarnevelt's archive." (No
  N4; "previously unread" is barred below N4; "intelligence letter" is not established; the Spanish side and the sender
  are unsearched; blocks A and C2 are not read.)

## 5. Postmortem

No over-claim found. No file calls the reading new, first, unpublished or unread; NOTES.md sections 8-9 report the
judge FAIL and the single-reader caveat plainly, and section 9 correctly calls the print check "a search result, not a
novelty verdict". One precision note, carried into NOTES.md section 10: `reading_meta.txt` glosses grade S as
"cryptanalytic, control on file (VX-CT03)" -- that control backs the **key** (100% digit recovery at N=325, K=7), not the
per-token **transcription** of B/C1, whose S grades are one reader's image confidence. Any outward sentence should
say "candidate reading" until (a'') the second full blind pass reconciles B/C1 and (d) an era-matched judge corpus is
run. Missed by the solvers and now covered: the Staten-Generaal resolutions 1604-1606 and the holding archive's full
EAD (whose catalogue convention, recording "gedecodeerd"/"sleutel" where present, is good evidence that no
contemporary decipherment came in with the copy).

**Propagation note, OLD-PASS2 (3 Oct 2026, rule 10 propagation; not a re-audit).** A second full blind pass over the
B/C1 crops (NOTES.md section 11) changed one B token after settling against the crop: B line 10 `c7nf7rm8` ->
`c7mf7rm8`, reading "conforme" -> "comforme" (same word, period spelling); the B quotation above and the queued
SO-OLDEN-2442-BC1 prompt were updated to match. B line 7 `t7d7s` ("todos") is now graded M (first sign G-shaped,
read as the `l7` ligature by the blind reader). Class and key source unchanged (N3, ours). Per-sign disagreement
between the two readers: 12.1% (agreement, not accuracy).

**Propagation note, R14-OLDV (verifier, account 2, LANE LANE-RUN14-account-2, 6 Oct 2026, 15:54-15:58 UTC; rule 10
propagation, not a re-audit).** Claim carried: NOTES.md section 19 (R14-OLDF2, 84f4031ed) changed two C1 signs through
`overrides.tsv` (ciphertext.tsv unchanged): C1_29 `p8r8` -> `p28r8` ("pere" -> "puere", grade I, not a word) and C1_31
`s2pl3c7` -> `s2ppl3c7` ("suplico" -> "supplico", period spelling, grade M). Checked by this session: (1) `apply_key.py
... --check` -> `OK: reading.txt matches a fresh decode`, reading now "sino puere ansi supplico"; (2) grade counts
S=245, M=18, I=23, as stated; (3) crops `images/crops_R14OLDF2/T1.png` and `T4.png` opened against a wider cut of scan 006
lines 4-6: T1 shows two long-descender p's before l (supported); T4 shows a separate open cup between the p and the looped
8, and the leaf's own `p7r` (C1 L2) runs the p head straight into the next sign, so a fifth sign is supported -- its value
(named 2) and the final 8 vs d stay unsettled, which grade I already says; (4) `transcription/segment_R14-OLDF2.log`
agrees with section 19's table (windows 0-3 -1.050/-0.922/-0.922/-1.079, all FAIL; PREREG call "not concentrated").
Corrections: the C1 quotation in section 2 above and the queued SO-OLDEN-2442-BC1 prompt
(`second-opinions/PROMPT-chatgpt-BC1.md`) now read "supplico"; both also printed "quien" where token C1_36 `q28n` decodes
"quen" (grade M) -- a silent regularization, now quoted as read. SECOND-OPINIONS-QUEUE.tsv row SO-OLDEN-2442-BC1 is
still `queued` (no answer to reconcile); its row text quotes no reading, so it is unchanged. Class and key source
unchanged (blocks B/C1 N3, ours); depth not reassessed here.

**Propagation note, R15-OLDV2 (verifier, account 2, LANE LANE-RUN15-account-2, 6 Oct 2026, 17:54-18:00 UTC; rule 10
propagation, not a re-audit).** Claim carried: NOTES.md section 20 (R15-OLDUV, ec902d21b) renamed the open u/v cup in four B
tokens through `overrides.tsv` (ciphertext.tsv unchanged): B37 `bv8n4s` -> `b28n4s` (buenas, M), B49/B76 `4tr8v8n` ->
`4tr828n` (atreuen), B55 `v8r4s,` -> `28r4s,` (ueras); and re-judged with `scripts/segment_judge.py --uv-fold`. Checked by
this session: (1) `apply_key.py ... --check` -> `OK: reading.txt matches a fresh decode`; (2) crops
`images/crops_BC1/B_L04_s2`, `B_L06_s1`, `B_L06_s2`, `B_L09_s1`: the sign after `b`, after `tr8` (twice) and before `8r4s`
is the same open cup as the `2` in `q28`/`p7rq28` on the same lines -- one sign, so the renaming is supported (a naming,
not a glyph re-read); (3) git order: `transcription/PREREG_R15-OLDUV.md` landed in abaf33532 (17:38:58 UTC), the scored log
`segment_R15-OLDUV.log` only in ec902d21b (17:41:54 UTC) -- the pre-registration predates the run; (4) the fold extends
`judge_plaintext.FOLD`, which `fold()` and the `NgramModel` word list read at call time with no cache, so the corpus model,
word list, held-out real windows, nulls and shuffled decodes are folded exactly as the target is (rule 3 normalisation on
both sides); the real_p05 values moved under 0.01 and the shuffled decodes stayed at -1.94..-2.17, consistent with that;
(5) full re-run of `segment_judge.py --uv-fold` this session reproduces the log exactly in all four windows (scores
-0.933/-0.880/-0.893/-0.968; real_p05 -0.864/-0.876/-0.868/-0.875; all FAIL; call "not concentrated").
On window 1 (-0.880 vs real_p05 -0.876, 0.004 short): under the pre-registered rule (PREREG_R15-OLDUV item 4, "if all four
still FAIL, the notation gap is ruled out as the cause of the FAIL at this N") and under rule 3 it is a **FAIL**, not
"judge cannot decide": rule 3's "cannot decide" reading needs an independent period gloss on the same leaf scoring near the
shuffled nulls (the clair349 case), and this letter has none. The gate is not moved. Descriptively only: 9.1% of held-out
real es1600 windows score at or below window 1 (blended held-out false-negative rate 11.6%), so this FAIL is weak evidence
against the reading, inside the judge's own false-negative band at N=160, and not evidence for it.
Corrections: the four B words were already quoted in u-form ("buenas", "atreuen", "ueras") in section 2 above and in the
queued SO prompt (`second-opinions/PROMPT-chatgpt-BC1.md`) -- a silent regularization at the time, now matching the
reading. Both also printed "harto", "Siguença" and "esperanças" where the reading has "arto", "delo desigu enca" and
"esperancas" (no cedilla is written in the transcription); now quoted as read, with "[de Siguenca]" as an editorial gloss.
SECOND-OPINIONS-QUEUE.tsv row SO-OLDEN-2442-BC1 is still `queued`; its row text quotes no reading, so it is unchanged.
Class and key source unchanged (blocks B/C1 N3, ours); depth not reassessed here.

## AUDIT 2 (second adversarial + depth, AUD2D-OLD2442)

Verifier AUD2D-OLD2442 (account 4, session_01HcGqodZqH3Hc1NGTKh4jXA), 8 Oct 2026, from 02:37 UTC by `date -u`. Brief:
`.claude/briefs/runs/2026-10-08-acct3-scout-jobs.md` section AUD2D-OLD2442; depth bar
`.claude/briefs/runs/2026-10-08-acct3-depth-bar.md`. Separate from VERIFY-OLD, R14-OLDV, R15-OLDV2 and every solver; this
session did not decode and changed no key, ciphertext, override or reading.

### 2a. Authentication distance, written before any stretch was measured

Depth bar as received (copied): CLAUDE.md 4a governs; cipher clause = a contiguous H/C/S stretch longer than the AD (about
1.5 x unicity), H(K) = the design's key space plus every liberty the reading took (U wildcards, M tokens, repairs, u/v and
word-break choices); an unfitted external key does not shrink H(K); the zero-liberty (H_lib+20)/R reading is not used; an
external check is a D3/D4 element, not a D2 alternative; code clause = a value reading sensibly in >= 2 independent contexts
(not applicable here: this design has no code values); D2 = one clause plus the verifier's own true, specific sentence.

Unit: only the digits (2,3,4,7,8) are cipher; consonants are transcribed clear text. Stretches are counted in consecutive
digit tokens, broken by any M or I word.

**R (redundancy per digit token)**, `depth/aud2d_ad.py`: R = log2(5) - H(vowel | consonant skeleton of its word), where the
skeleton masks every vowel (and v, folded to u, since the hand's `2` is both). H(vowel | skeleton) is a held-out
cross-entropy: skeleton -> vowel-string counts from six es1600 volumes, scored on the seventh (CODOIN XCVI, 262,454 vowels),
add-1 backoff to the vowel-unigram model for unseen skeletons.
```
vowel unigram H = 2.235 bits; held-out H(V|skeleton) = 0.491 bits/vowel over 262454 vowels (test XCVI)
plug-in (train=test, not used) H(V|skeleton) = 0.328
R = log2(5) - H = 2.322 - 0.491 = 1.831 bits per digit token
vowel map 5! (brief's design level): H(K0) = 6.91 bits; unicity(no liberties) = 3.8 digits; AD = 5.7 digits
free over 23 letters 23P5 (sensitivity): H(K0) = 21.95 bits; unicity(no liberties) = 12.0 digits; AD = 18.0 digits
```
This R is generous to the reading in one way (whole-word skeletons assume the word breaks are right) and harsh in another
(it ignores sentence context); it is the empirical per-digit figure the brief asks for, not the per-letter R of prose.

**Liberties, per block** (from `reading_tokens.tsv` grades and `overrides.tsv`; each M or I word = log2 5 = 2.32 bits, one
choice among the digit values or a glyph alternative; each u/v renaming, glyph override and word-break the reading's sense
relies on = 1 bit):

| block | M+I words | u/v renames | other glyph overrides | word-break choices | liberty bits | H(K) = 6.91 + liberties | U = H(K)/R | **AD** (digits) | AD if base is 23P5 |
|---|---|---|---|---|---|---|---|---|---|
| B | 5 M + 1 I = 13.93 | 4 (B37, B49, B55, B76) | 1 (B92 n->m) | 4 (delo -> de lo; desigu enca -> de Siguenca, 2; pa ciencia) | 22.93 | 29.84 | 16.3 | **24.4** | 36.9 |
| C1 | 6 M + 2 I = 18.58 | 0 | 2 (C1_29, C1_31) | 2 (quen -> que en; entodo -> en todo) | 22.58 | 29.49 | 16.1 | **24.2** | 36.5 |

The ruling uses the 5! column (the brief's design level, the five digits' map onto the five vowels) and reports the 23P5
column as a sensitivity: a stretch is called clear of the AD only if it also clears the 23P5 figure, or the call says so.

### 2b. Rule 7 and grade recount (unit 1)

`python3 scripts/apply_key.py digit_key.json ciphertext.tsv --overrides overrides.tsv --out reading.txt --check` ->
`OK: reading.txt matches a fresh decode`, exit 0 (the brief's bare `apply_key.py --check` form lacks the two required
positional arguments; the NOTES section 19-20 form was used). Eye-check on the existing crops, no new fetch:
`images/crops_BC1/B_L02_s1` (`l7 d8ss84 4rt7, 3 s8 l4m8nt4`), `B_L06_s2` (`d2q28 c7n 28r4s, p7rq28`, the u-cup in `28r4s` the
same sign as in `q28`) and `C1_L06_s1` (`qnl4`, I as graded) all agree with `ciphertext.tsv`/`overrides.tsv`.

Recount (`depth/aud2d_runs.py` over `reading_tokens.tsv`), per word token and per digit (cipher) token:

| block | word tokens | S / M / I (words) | H/C/S share, words | digit tokens | S / M / I (digits) | **H/C/S share, digits** |
|---|---|---|---|---|---|---|
| B | 95 | 89 / 5 / 1 | 93.7% | 186 | 171 / 12 / 3 | **91.9%** |
| C1 | 61 | 53 / 6 / 2 | 86.9% | 117 | 97 / 16 / 4 | **82.9%** |
| B+C1 | 156 | 142 / 11 / 3 | 91.0% | 303 | 268 / 28 / 7 | **88.4%** |

The brief's "B S90 M4 I1" predates R15-OLDUV, which regraded B37 `b28n4s` (buenas) to M; current B is S89 M5 I1. No H or C
token exists (no key source, no known plaintext): this is a cryptanalytic result (rule 4).

### 2c. Depth (unit 3)

**Longest H/C/S stretch, in digit tokens** (`depth/aud2d_runs.py`, measured after 2a was pushed in 5157722f):
```
B: longest H/C/S stretch: 59 digit tokens, words B65-B95: de su gusto i sus mismos hijos muchas ueces no se atreuen a
   decirle nada, i assi no ai sino pa ciencia i hacer lo que pudieremos comforme a los tiempos
C1: longest H/C/S stretch: 33 digit tokens, words C145-C161: uerdad que procedo i con quantos desseos de acertar a seruir
   a V.Sa i darle gusto entodo-
```
B's 59 clears its AD of 24.4 digits by 2.4x and also clears the 23P5 sensitivity AD (36.9). C1's 33 clears its 5! AD (24.2)
but not the 23P5 one (36.5); B alone carries the clause. The B stretch already contains one counted liberty (the `pa
ciencia` join), included in H(K).

**Matched control, subsampled (rule 3, ARM3-ADJ).** Same script as VX-CT03 (`scripts/solve_digit_subst.py control`, Don
Quijote 1605 corpus, held-out 10%, 8 restarts x 40,000 iterations), 3 seeds each, clean and at VX-CT03's 37.3% crib noise,
at the brief's N=95 and N=61 and at the blocks' own sign-stream lengths (B 372 signs, 182 digits; C1 262 signs, 116
digits), K=7 (VX-CT03's setting) and K=5 (the five digits B/C1 use). Outputs `depth/control/*.json`.

| N (signs) | K | crib noise | digit positions recovered, seeds 1/2/3 | mean |
|---|---|---|---|---|
| 372 (B) | 5 | 0 / 0.373 | 193/193, 196/196, 197/197 (both) | 100% / 100% |
| 262 (C1) | 5 | 0 / 0.373 | 144/144, 138/138, 139/139 (both) | 100% / 100% |
| 95 | 5 | 0 / 0.373 | 54/54, 52/52, 50/50 (both) | 100% / 100% |
| 95 | 7 | 0 / 0.373 | 66/66, 66/66, 64/64 (both) | 100% / 100% |
| 61 | 5 | 0 | 36/36, 37/37, 31/31 | 100% |
| 61 | 5 | 0.373 | 30/36, 31/37, 11/31 | **67.5%** |
| 61 | 7 | 0 | 44/44, 45/45, 39/39 | 100% |
| 61 | 7 | 0.373 | 44/44, 39/45, 20/39 | **79.3%** |
| 372, 262 | 7 | 0 / 0.373 | all 100% | 100% |

Caveats: the control draws one held-out passage (the seeds vary the solver, not the text), and it converts the K most
frequent letters, not the five vowels; it is at ceiling at every length at or above N=95, so it shows key-recovery power
at the blocks' own lengths, not transcription accuracy (rule 3 headroom). At N=61 with crib noise the method starts to
fail, so a 61-sign window alone would not license a key; the key here rests on block A plus B plus C1 together.

**Language judge.** The whole-letter and B/C1 `es`/`es1600` judges FAIL (NOTES sections 8, 12-13, 20: B/C1 windows -0.933,
-0.880, -0.893, -0.968 vs real_p05 about -0.87). Reported as a FAIL; not a depth gate (rule 7).

**Ruling: D2.** Cipher clause met in block B (59 digit tokens > AD 24.4, and > 36.9 under the 23P5 base). Verifier's
sentence, written from the reading of B (grade S throughout words B38-B56 and B65-B95), not from any edition: *the writer
tells V.Sª that people often cannot, or dare not, speak frankly to the duke because everyone has pretensions of his own
and follows the duke's pleasure, that even the duke's own sons often dare not tell him anything, and that there is
nothing for it but patience and doing what they can as the times allow.* The duke is not named in B/C1 (block A, not in
scope, names a duke beside the Sigüenza see; identity not established here).
**Not D3:** digit-token H/C/S is 88.4% (>= 80%), but the 14 M/I words are ordinary words (el, pesame, buenas, todos, aire,
besaua, parecerme, puere, ansi, supplico, quen, qnla, i) plus one name fragment (desigu), not "mostly names"; and no
external check exists (no period key, gloss or clear copy). D3 would need those gaps settled from the image and an
independent check.

- depth: **D2**; depth_pct: **88.4** (digit-token basis, B+C1, 268/303; word-token 91.0%, 142/156); depth_unread: 35 digit
  tokens (28 M, 7 I) in 14 words, 1 a name fragment; depth_check: "AD 24.4 digits (5! map + 22.9 bits of liberties,
  R=1.831 bits/digit held-out es1600) vs longest S stretch 59 digits (B65-B95); control solve_digit_subst at N=372/262/95
  100%, N=61 noisy 67.5-79.3%"; decode_status: "Partially decrypted"; outward words: "partially deciphered (about 88%)",
  blocks B and C1 only (A and C2 unread, waiting on the owner's sorter).

### 2d. Novelty, second adversarial pass (unit 2): Spanish side

| family | searched (8 Oct 2026) | result |
|---|---|---|
| sender/recipient by name | Google Books (keyed, `country=US`): "Garcia de Senisteros" (0), "Juan Garcia de Senisteros" (0), "Senisteros" Alcalá (0), "Juan de la Peña" 1605 cifra Flandes (12, none this letter); IA be-api fts global "Gara de Senisteros" (0), "Garcia de Senisteros" (0); Semantic Scholar "Senisteros" (0), "Garcia de Cisneros Alcala 1605 carta" (51, Cisneros the cardinal, 1509-1545 matter), "Juan de la Peña 1605 correspondencia" (San Juan de la Peña monastery etc.); CORE "Senisteros" (0), "Juan de la Peña" 1605 Alcalá (monastery) | no printed correspondence of either party; sender still unidentified |
| CODOIN | AUDIT 1's IA-global "Senisteros" (IA carries the CODOIN scans); the seven 1598-1621 tomos of `tools/data/es1600` (XLII-XLVII, XCVI) grepped raw for Senisteros/Cisneros/"Juan de la Pena" at build (README: zero) | not found; the other ~100 tomos only through IA-global |
| Lonchay-Cuvelier t. I | be-api fts on `correspondancede0000unse_m5g7`: Senisteros (0), Peña (0), Siguenza (1 hit, no snippet; AUDIT 1's solvers' full djvu grep already found no mention of this letter) | not found |
| Rodríguez Villa, *Correspondencia de la Infanta ... con el duque de Lerma* (1906) | be-api fts on `correspondencia-de-la-infanta-archiduquesa-dona-isabel-clara-eugenia-de-austria`: Senisteros (0), Cisneros (0), Sigüenza (0); Peña returned a non-JSON answer (unreadable, not retried); positive control "Lerma" answers | not found |
| Simancas Estado guides | not reached: PARES is a dead host from the cloud (CLAUDE.md host table); the printed Simancas *Catálogo* (Estado, Flandes) is not open full text from here; HathiTrust full text Cloudflare-blocked | **unreachable** |
| phrases in print | `tools/print_check.py` on phrases.txt (now 16 lines; added "i se lamenta de uer los tiempos que corren", "porque todos tienen sus pretensiones i andan al aire", "supplico a V.Sa me perdone quen decirlo"): 87 rows, 15 with hits, every hit a scattered-word match (dictionaries, Cortes diaries, 1645 *Teatro eclesiástico* for the bishop names); Google Books exact modern-spelling phrases "se lamenta de ver los tiempos que corren", "todos tienen sus pretensiones y andan", "sus mismos hijos muchas veces no se atreven", "no se atreven a hablar al duque": scattered-word hits only, none this letter | not found |
| scholarship | OpenAlex 18 (print_check); Semantic Scholar 5 direct + 1 in print_check: 2 answered 429, one retry each, not retried further; CORE 3; CrossRef 3 | nothing about this letter |
| JSTOR | 4 earlier rows answered (no hits); 4 new rows appended 8 Oct (2 family i: names + Sigüenza; 2 family ii: "todos tienen sus pretensiones", "sus mismos hijos muchas veces no se atreven") | queued; does not block N3 |

Requests this session: www.googleapis.com 16 + 8, be-api.us.archive.org 16 + 9, archive.org 1, api.openalex.org 18,
api.semanticscholar.org 1 + 6 (2 x 429), api.core.ac.uk 3, api.crossref.org 3.

**Class: N3 kept** (blocks B and C1). Not raised to N4: the Simancas side is unreachable from here and the sender is still
unidentified, so the principal Spanish catalogues are not covered (rule 10's N4 bar); no specialist or archive asked. Not
lowered: no prior plaintext or decipherment found. **Key: ours.** Text: not known in print.

- **Safe sentence:** "Blocks B and C1 of Nationaal Archief 3.01.14 inv. 2442 (a copy of Don Juan Gara de Senisteros to Juan
  de la Peña, Alcalá, 23 December 1605) are partially deciphered (about 88% of cipher digits) under a vowel-digit key we
  recovered: the writer tells his correspondent that no one dares speak frankly to the duke, not even the duke's own sons,
  and that patience is all that is left. No prior decipherment or print of the letter was located after the search
  logged in AUDIT.md (N3); the reading is cryptanalytic and fails our language judge."
- **Unsafe sentence:** "We have deciphered a previously unread letter about the Duke of Lerma's court from Oldenbarnevelt's
  intelligence files." (Below N4 "previously unread" is barred; the duke is not named in B/C1; D2 is "partially
  deciphered", not "deciphered"; blocks A and C2 are unread; "intelligence files" is not established.)

**SO-OLDEN-2442-BC1.** `second-opinions/PROMPT-chatgpt-BC1.md` quotes no grade count, class or depth (checked: it states the
key as ours and quotes the reading as committed); the SECOND-OPINIONS-QUEUE.tsv row is still `queued` and quotes no
reading. Nothing changed that it carries, so neither is edited.

**Postmortem.** No over-claim found. One stale count in the brief (B S90 M4; current S89 M5 after R15-OLDUV) and one stale
command form (bare `apply_key.py --check`), both noted above. Parent follow-up per the brief: status.json row from 2c/2d,
`tools/depth_check.py`, NOTES line 1 open -> partial.
