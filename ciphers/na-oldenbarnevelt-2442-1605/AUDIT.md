# AUDIT: Nationaal Archief 3.01.14 (Archief Johan van Oldenbarnevelt) inv. 2442, Senisteros to Pena, 23 Dec 1605 (copy), blocks B and C1

Class (rule 10): **blocks B and C1: N3** (no prior plaintext and no prior decipherment located after the logged search
below). Key source: **ours** (the a=4, e=8, i=3, o=7, u=2 vowel-digit key was recovered by this project's cryptanalysis,
VX-CT03, 25 Sept 2026; no period key, gloss or published key exists for it as far as searched). Text: not known in print.
Blocks A and C2 are out of scope (not re-read from the image yet) and are not classified here.
Leaves 4/5/7 (ff.59v-62r): **N3, D1**, key ours -- see "AUDIT 3" (OLD-SIBS-V, 8 Oct 2026) and "AUDIT 4" (second
adversarial audit, V1-OLD, 8 Oct 2026: N3 and D1 kept) at the end.
Scan 10 cipher block (f.64r): **N3, D1**, key ours -- see "AUDIT 5" (V-OLD10, 8 Oct 2026).

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

## AUDIT 3 (verifier OLD-SIBS-V): leaves 4/5/7 (ff.59v-62r), NOTES section 22

Verifier OLD-SIBS-V (account 2, session_01J65Dh51ovVCLtqZM7aCSk6), 8 Oct 2026, 05:12-05:3x UTC by `date -u`. Brief
`.claude/briefs/runs/2026-10-08-acct4-old-sibs-verify.md`. Separate from OLD-SIBS (account 4) and every earlier solver; this
session changed no key, ciphertext, override, transcription or reading. Blocks B/C1 classes (N3, D2, AUDIT 2) are kept as they
are: nothing found here bears on them.

Claim under audit: "the fixed B/C1 key (2=u 3=i 4=a 5=s 6=b 7=o 8=e) reads leaves 004/005/007 as continuous Spanish of the same
Senisteros letter; the free solve returns the same map; cipher tokens 729, H 0, C 0, S 87, M 642; es1600 judge FAIL -0.99 vs
real_p05 -0.808", plus section 22's content paragraph.

Depth bar copied before computing (`.claude/briefs/runs/2026-10-08-acct3-depth-bar.md`): CLAUDE.md 4a governs; cipher clause =
a contiguous H/C/S stretch longer than the AD (about 1.5 x unicity), H(K) = design key space plus every liberty (U wildcards,
M tokens, repairs, u/v and word-break choices); an unfitted external key does not shrink H(K); the zero-liberty reading is not
used; an external check is a D3/D4 element, not a D2 substitute; code clause n/a (no code values in this design); D2 = one
clause plus the verifier's own true, specific sentence.

### 3a. Re-derivation (step 1)

- `python3 scripts/decode_L457.py --check` -> `committed reading matches a fresh run; {'clear': 70, 'M': 642, 'S': 87}`, exit 0.
- Free solve, second seed: `scripts/solve_digit_subst.py target transcription/ciphertext_L457_solver.tsv --corpus
  corpus/es16-donquijote/donquijote1605_pg2000_body.txt --restarts 8 --seed 2` -> N=2919, 1487 digit positions, K=7; all 8
  restarts -6137.26, map 2=u 3=i 4=a 5=s 6=b 7=o 8=e, decoded stream byte-identical to seed 1
  (`transcription/free_solve_L457_seed2_verify.json`). Confirmed.
- **Caveat on what the free solve shows (not an over-claim in NOTES, but recorded so it is not over-read):** the solver ran on
  the reconciled transcription, and the reconciler knew the B/C1 key. The free solve therefore shows the B/C1 map is the
  language-model optimum *for that transcription*; it is not a key recovery independent of B/C1. The key's independent support
  remains blocks A+B+C1 (VX-CT03, AUDIT 1-2).
- Eye-check (native pixels; `images/crops_L457` and direct crops of scans 004/005/007): every token on L4b_27-L4b_31 (the
  signature passage, 35 tokens, 33 of them M) and on nine lines of f.62r (L7b ~08-24: "theo pussiesse io el dinero asta ...
  uendiesse uino i selo enuiasse ... despues me dixo [en secreto] llegando a contar el dinero que traian que auia tomado del
  talego ... quarenta reales ... me han enfadado un poco aunque io no selo he dado a entender de ninguna manera porque basta ser
  s?b?ino de quien es i la buena amistad que nos ha hecho el regente en esto dela canongia ... que se haga en racon de si
  cobrare de chaues el coste del manteo i los quarenta reales supuesto que el no saue que V.S. lo saue ...") agrees with the
  reconciled transcription sign for sign, apart from the items below. About 100 tokens checked in all, nearly all M-graded, against the
  brief's 10 (this verifier also knew the key, so the check is of sign identity, not a blind read). The digit shapes in this hand (4, 7, 8, 3, 2) are distinct on these lines; the leaf-7 blind-pass split (57.1%)
  is mostly line identity, as section 22 says: crop `L7b_L18.jpg` does not contain transcription line L7b_18 at all.
- Doubtful tokens (section 22 names three; none changes the key or the sense):
  | token | transcription | image (this verifier) | effect |
  |---|---|---|---|
  | L4a_05 `gr4nd7` (decode "grando") | `q28 gr4nd7` | first sign g or q, second r or 2; `q24nd7` "quando" fits ("della, que quando lo oio se dio al demonio") | non-word becomes a word; stays M until a blind pass settles it |
  | L5_1 `s28ss8` (decode "suesse") | `s28ss8` | first sign is the long f with crossbar, the same shape as the f of `c7nf7rm8` beside it: `f28ss8` "fuesse" | likely correction for the solver |
  | L5_1 `p7r7c2r8` ("porocure") | `p7r7c2r8` | p with an r-loop then 7: `pr7c2r8` "procure" plausible | M |
  | L7b_18 `s7633n7` ("sobiino") | `s7633n7` | third/fourth signs 6 + an r-like or 3-like stroke: `s76r3n7` "sobrino" not excluded | M |
  | L7b_10 `t8n4` ("tena") | `t8n4` | a sign may stand between n and 4 (`t8n34` "tenia") | M |
  Read as suggestions to the solver lane; this verifier does not edit the transcription (brief: no decoding).

### 3b. Leaf identity (step 2)

Confirmed from the images. Pencil folio stamps read 60 (scan 004), 62 (007), 57 (009), 64 (010); one hand on scans 004, 005,
007, 009-011; scan 011 (f.64v) carries the close "...de Alcalá y d[iciem]bre 23 de 605", the signature "D. Ju[an] Gar[cí]a de
Senisteros" with paraph and the postscript naming "Ju[an] de la Peña", and its show-through is scan 010's right-page cipher
reversed. Leaves 4/5/7 are folios of the same letter, not a sibling: section 22's correction of section 1 and OLD-CAT
(section 21) stands. This deepens the one counted document; it adds no document to any count.

### 3c. Depth (rule 4a, under the bar)

`reading_L457_tokens.tsv`, digit (cipher) tokens: L4 761 (S 79, 10.4%), L5 220 (S 25, 11.4%), L7 521 (S 31, 6.0%); all 1502
(S 135, **9.0%**). Longest contiguous H/C/S stretch: **7 digit tokens** (L5 "decia como io"); L4 6 ("io hice una"), L7 4.
The AD with the 642 M words counted as liberties (2.32 bits each, AUDIT 2a's rule) runs to thousands of digits; even B/C1's
small-liberty AD (24.2-24.4 digits) is not reached. **No cipher clause; code clause n/a. Ruling: D1** ("fragments read") for
the L4/L5/L7 reading as graded.

Why the ruling is lower than the reading's apparent quality (recorded so D1 is not read as a negative): the M grade here comes
from the prereg's S rule (a token must match both blind passes), and the blind passes failed largely on crop line identity,
not on sign identity (3a). The key is the B/C1 key, already at D2 there. The named way up is section 22's step (o2): re-cut
L4/L7 with `--mask-neighbours` and run two fresh blind passes, then re-grade; a verifier eye-check does not regrade tokens.
External plausibility (not a D3 element under the bar, not a key check): "Horacio Doria", a cipher-decoded name on f.60r in a
Toledo-canonry context, was a canon of Toledo in this period (editions of St Teresa's letters, e.g. IA
`BMC9ObrasDeSantaTeresaDeJessTomoIXEpistolarioIII`: "Horacio Doria era primo del P. Nicolás, y canónigo de Toledo"; Google
Books `Vd1WAAAAYAAJ`, *El Toledo que vió Cervantes*, 2006: "Horacio Doria, un genovés afincado en España ... accedió a su
canonjía toledana"). The duke of Lerma did found the colegiata of San Pedro at Lerma at this time (Google Books
`fhstAQAAIAAJ`, *La Iglesia Colegial de San Pedro en Lerma*, 1981), consistent with the clear-text "Abadia de Lerma donde el
Duque funda ahora una iglesia collegial". Neither is a check of the cipher reading itself.

Verifier's sentence (not required at D1; written from the image-checked tokens of L4b_27-31, given so a later D2 ruling has it
in hand): *the writer says that, finding himself pressed, he made a signature of V.S. on a sheet of paper as best he could and
had a servant of his write out the substance of the letter, telling the servant that V.S. had left him some signatures in
blank.* (Section 22's word for this is "made"; "forged" is the brief's gloss and is fair to the text, which says he imitated
V.S.'s signature himself.)

- depth: **D1**; depth_pct: **9.0** (S digit tokens 135/1502; L457 only); depth_unread: 1367 digit tokens M (642 words), almost
  all ordinary words, not names; depth_check: "longest S stretch 7 digits vs AD >= 24 digits (B/C1 small-liberty floor; far
  higher with 642 M words); free solve seed 1 and 2 identical map at N=2919 (transcription key-aware); control 100% at N=2919
  crib noise 0-0.4"; decode_status: "fragments read" (L4/L5/L7). The letter as a whole keeps B/C1's D2.

### 3d. Novelty (step 3)

| family | searched (8 Oct 2026) | result |
|---|---|---|
| canonical series / sender editions | AUDIT 1-2 cover CODOIN (es1600 tomos grepped, IA-global), Lonchay-Cuvelier t. I (djvu grep, be-api), Rodríguez Villa 1906, Huygens Oldenbarnevelt retroboeken; section 22 re-grepped Lonchay-Cuvelier for Lerma/collegial/Mexia/Gomara/Garay/Senisteros/Alcalá (Agustín Mexía the councillor only) | not found |
| phrases in print | `tools/print_check.py` with `phrases_L457.txt` (11 phrases from L4/L5/L7 + one clear-text Lerma phrase) -> `print-check-L457.tsv`, 62 rows, 12 with hits, every hit a scattered-word Google Books match (dictionaries, the 1742 *Cartas*, Lerma colegiata histories, comedias for "basta ser sobrino de quien es"); ia-global 2 phrases HTTP 502, gbooks 2 phrases HTTP 503 (not retried) | not found |
| names, modern spelling | Google Books (keyed, `country=US`): "Horacio Doria" canonjía Toledo (2, both biography, not this letter), "Juan de la Peña" Alcalá 1605 rector (14, other men), "doctor Cetina" canonjía Alcalá (1, no), "colegial de Lerma" 1605 Alcalá rector canonjía (0), "Sebastián de Chaves" Alcalá estudiante (37, none this matter), Senisteros/Cetina/Mexia + "Horacio Doria" (0/11/5, indexes only), "Agustín Mejía" regente cuñado (1, no); two queries 503 | not found |
| IA full text | be-api: "Senisteros" (20, all the Latin etymon *senisteros*), "Horacio Doria" Cetina (37, St Teresa editions), "Agustin Mexia" regente canongia (35, other letters), "doctor Garay" cardenal canongia Toledo (37, catalogues of other items) | not found |
| scholarship | OpenAlex 13 via print_check + 2 direct (0, 0); CORE 2 (noise); CrossRef 3 (noise); Semantic Scholar: print_check's pass 429 throughout, 1 direct keyed query answered (Horacio Doria canon Toledo: 4, none relevant) | not found; S2 partly blocked |
| holding archive | NA 3.01.14 EAD and printed inventory (AUDIT 1): "Merendeels in cijferschrift", no decipherment recorded | no decipherment |
| Simancas / PARES | dead host from the cloud (CLAUDE.md host table) | **unreachable** |
| JSTOR | no new row: AUDIT 2's 4 rows (names, Sigüenza, two B phrases) cover the sender/recipient family; the L457 phrases add nothing JSTOR would index that a cipher-free study of the Toledo canonry would carry better than the names already queued | not queued (does not block N3) |

Requests this session: www.googleapis.com 11 + 14, be-api.us.archive.org 11 + 4, api.openalex.org 13 + 2, api.semanticscholar.org
1 + 1 (+1 livecheck), api.crossref.org 3, api.core.ac.uk 2 (+ key_livecheck's one call per keyed host).

**Class: N3** (leaves 4/5/7, ff.59v-62r): no prior plaintext or decipherment located after the search logged here and in
AUDIT 1-2. Not N4 for the same reasons as B/C1 (Simancas side unreachable, sender unidentified, no specialist asked).
**Key: ours** (the B/C1 vowel-digit key, VX-CT03; 5=s and 6=b are the folder's settled glyph conventions for s and b, A2-OLD /
PREREG_OLD-PASS2 item 2, not cipher values). Text: not known in print.

| item | class | depth | prior plaintext | prior decipherment | key | evidence | confidence |
|---|---|---|---|---|---|---|---|
| inv. 2442, leaves 4/5/7 (ff.59v-62r), 729 cipher words | **N3** | **D1** | none located | none located | ours | cryptanalytic, fixed key, key-aware reconciliation, two blind passes split 31-57%; judge FAIL -0.99 vs -0.808 | moderate on novelty; reading verified by eye on ~100 tokens, graded M by rule |

- **Safe sentence:** "Folios 59v-62r of the same Senisteros letter (Nationaal Archief 3.01.14 inv. 2442) read as Spanish under
  the vowel-digit key we recovered from its other passages; only fragments are graded as read so far. No prior decipherment or
  print was located after the search logged in AUDIT.md (N3)."
- **Unsafe sentence:** "We deciphered a further unpublished letter in which a Spanish cleric forged his patron's signature."
  (Not a further letter -- the same one; "unpublished" barred below N4; D1 is "fragments read"; "forged" over-states what the
  writer says, that he imitated the signature "as best he could" under a claimed blank-signature authority.)

### 3e. Postmortem

No over-claim in section 22: it calls the reading "a solver's reading, M-graded where the passes split", keeps status open,
and corrects the earlier "second ciphered letter" itself. Two points carried here so they are not lost: (1) the free solve's
agreement with the B/C1 map is partly circular (key-aware reconciliation, 3a) and is not a second key recovery; (2) leaf 5's
`s28ss8` is very likely `f28ss8` "fuesse", and L4a_05 "grando" likely "quando" -- solver-lane corrections, not made here. The
brief's "forged a signature" is the brief's wording, not the repo's; the repo's own sentence stands.
SO row: `SO-OLDEN-2442-L457` queued with `second-opinions/PROMPT-chatgpt-L457.md` (N3 per the verifier template).

## AUDIT 4 (second adversarial, V1-OLD): leaves 4/5/7 (ff.59v-62r)

Verifier V1-OLD (account 3, LANE-VERIFY-1, session_01DAY8kYbVijnShAHKHxomYh), 8 Oct 2026, 16:09-16:3x UTC by `date -u`. Brief
`.claude/briefs/runs/2026-10-08-acct3-verify1-jobs.md`, section V1-OLD. Separate from OLD-SIBS (account 4, reader) and from
OLD-SIBS-V (account 2, AUDIT 3); not protecting either. No key, ciphertext, override, transcription or reading was changed.
Claim under audit: AUDIT 3's row -- leaves 4/5/7 **N3, D1**, key ours, cipher tokens 729 (H 0, C 0, S 87, M 642), safe
sentence as written there.

### 4a. Re-derivation and depth recount

- `python3 scripts/decode_L457.py --check` -> `committed reading matches a fresh run; {'clear': 70, 'M': 642, 'S': 87}`, exit 0.
- Recount from `reading_L457_tokens.tsv` by a script of this session (digits of cipher tokens): L4 761 (S 79), L5 220 (S 25),
  L7 521 (S 31); all 1502, S 135 = **9.0%**; longest contiguous S run 7 digits (L5 "decia como io"). Same as AUDIT 3.
- Depth under `.claude/briefs/runs/2026-10-08-acct3-depth-bar.md`: the longest S stretch (7 digits) is below even B/C1's
  small-liberty AD (24.2-24.4 digits), and with 642 M words counted as liberties the AD is far higher; no code clause (no code
  values in this design). **D1 kept** ("fragments read"). Not raised: the eye-check in AUDIT 3 3a was by a key-aware verifier and
  does not regrade tokens; the named way up stays NOTES section 22 step (o2).

### 4b. Prior-work checks 3-5 (search families the first audit did not cover first)

| check / family | route, query (8 Oct 2026) | result |
|---|---|---|
| 1 own work | grep of NOTES/AUDIT/WORK-QUEUE and the last 1,500 ROOM lines for 2442 / L457 / OLD-SIBS | only OLD-SIBS (reader) and OLD-SIBS-V (AUDIT 3); no other live claim; scan 10's cipher block (ff.63v/64r) is still unread (step o1) and is outside this audit |
| 2 leaf and neighbours | from the record (NOTES Premise check, section 22, AUDIT 3 3b; all 11 scans viewed by earlier sessions); not re-viewed here | no gloss, clear copy or key on any scan |
| 3 holder + solver repositories | NA EAD note carried from AUDIT 1 ("Merendeels in cijferschrift", no "gedecodeerd"/"sleutel"); fresh depth-1 clones of dbourdeau/cyphersolver (last commit 7 Oct 2026) and aaymeloglu/unsolved-ciphers (27 Sept 2026) grepped for Horacio Doria, Senisteros, Agustin Mexia, Oldenbarnevelt, 3.01.14 | Oldenbarnevelt hits are Bourdeau's `aerssen1601` (Van Aerssen to Oldenbarnevelt, 1601), a different item; nothing on inv. 2442 |
| 4 **Oldenbarnevelt edition (Huygens retroboeken, Bescheiden Deel 1-3, RGP GS 80/108/121), full text** -- new names | `searchText`, whole edition: positive control Spinola (20+); Doria 0, Mexia 0, Mexía 0, Chaves 0, Cetina 0, Garay 0, Gomara 0, canonicaet 0, Senisteros 0, Peña 0, onderschepte 0, intercepte 0; Lerma 8 (all Spanish court diplomacy, Deel 2 pp.141, 484-490, and index), Toledo 14 (Alva and Pedro de Toledo, indexes), onderschept 1 (Deel 1 p.405, English interception of a 1590s letter), "Spaensche brieven" 20 (scattered, none Dec 1605-1606 Spanish intercepts) | not found |
| 4 **Oldenbarnevelt edition, chronological letter list ("Brievenlijst", `toc` accessor, date filter)** | every letter dated 1 Nov 1605-31 Jul 1606: nos. 120-136 (Deel 2 pp.126-145: Harderwijk, Brederode, Von Rheydt, Amsterdam admiralty 28 Dec 1605, Isaac le Maire 8 Jan 1606 + memorie, to Fr. van Aerssen 18 Jan, A. Serlippens 29 Jan, Paulus Bacx 7 Feb, Willem Lodewijk 24 Mar, Utenhove 8/17 May, Caron 13 May, M. de Hornes 16 May, Merula, Berkel memorie, Van Bilderbeke); pp.133-134 read (Serlippens/Bacx window) | no letter encloses, forwards or mentions an intercepted Spanish letter of Dec 1605; the edition does not print or calendar inv. 2442 |
| 4 recipient side (Juan de la Peña; "V.S.") | Google Books (keyed, `country=US`): "Juan de la Peña" Oldenbarnevelt (1: the 1984 NA inventory only), "Juan de la Peña" "Agustín Mexía" (1: *La estirpe de las Rojas* 2007, a Juan de la Peña Zorrilla in a genealogy, not this letter), "Juan de la Peña" canonjía Alcalá 1605 regente (0) | no printed correspondence of the recipient located; V.S. unidentified |
| 4 Spanish side by entity | IA be-api fts: "cuñado del regente" Mexía (5: the Aragon 1591 accounts -- Juan Palacios "cuñado del Regente Campi" beside the maestre de campo Agustín Mexía; co-occurrence, not this matter), "Agustín Mexía" canongía (48: Almansa y Mendoza's *Cartas* 1621-26 canonry lists, the *Correspondencia ... Catalogue* vol. 7; none this letter), "Horacio Doria" canongía (502, one retry not made: limit reached on host errors) | not found |
| 5 **G3, decoded-phrase re-search** | `tools/print_check.py . --phrases phrases_L457_V1OLD.txt --only ia-global,gbooks,openalex` (15 phrases: the four AUDIT 3 could not search -- garai/carta, firma de V.S., Agustin Mexia/cuñado, rectoria/canongia/cathedra -- plus 11 new decoded phrases from L4/L5/L7, decoded and modern spelling: "pregunto horacio doria lo mismo", "le auia parecido vacarla libremente en manos de su senoria", "hice otra carta en nombre de V.S. para el abad", "por auer sido rector el doctor capata aquel ano", "la buena amistad que nos ha hecho el regente", the manteo/sotanilla lines, "algunas firmas en blanco", ...) -> `print-check-V1OLD.tsv` (45 rows, 10 with hits), hosts `print-check-hosts-V1OLD.tsv`; then single retries by hand: IA be-api "pregunto horacio doria" 0, "hice una firma de V.S." 0, "vacarla libremente en manos" 0, "cuñado del regente" 11 (Aragon 1591, above), "me pregunto el doctor garai" 502; Google Books "me pregunto el doctor garay/garai si traia carta" (1: *Revista colombiana* 1933, scattered words), "poder tener con la rectoria la canongia" (12, scattered: Valencian clergy, *Archivo teológico granadino*), "pregunto horacio doria lo mismo" 503 twice | every gbooks/openalex hit is a scattered-word match (St Teresa concordance, 19th-c. codes and gazettes, CODOIN 1884 for "algunas firmas en blanco", a 1720 Toledo chapter lawsuit *Por el dean y cabildo* for "Horacio Doria"); **no hit shows this letter**. Still unsearched: ia-global for 6 phrases (be-api 502/503 on the run and on one retry) |
| 5 same-day replies / other correspondents' versions / press | Oldenbarnevelt's incoming letters Nov 1605-Jul 1606 (row above) are the only "same file" correspondents in print; no reply from Peña or V.S. is known; no periodical press exists for a private Alcalá canonry matter in 1605 (relaciones de sucesos carry court news, not this) -- searched only through the names above | nothing sharing two rare entities within +-3 days located |
| scholarship | Semantic Scholar (keyed) 4: Senisteros Alcalá, canonjía San Justo Alcalá 1605 rector, Horacio Doria canónigo Toledo, Agustín Mexía regente cuñado canonjía (all noise or 0); CrossRef 3: Senisteros (0), canonjía Alcalá 1605 regente Mexía cardenal Sandoval (noise: Cervantes's letter to Sandoval y Rojas), Horacio Doria canónigo Toledo (noise) | nothing about this letter |
| Simancas / PARES; HathiTrust full text | dead host / Cloudflare from the cloud (CLAUDE.md host table) | **unreachable** (unchanged) |

Requests this session: resources.huygens.knaw.nl 25, be-api.us.archive.org 15 (print_check) + 8, www.googleapis.com 15
(print_check) + 9, api.openalex.org 15, api.semanticscholar.org 4, api.crossref.org 3, github.com 2 (clones). No 429; IA be-api
502/503 on 9 calls, Google Books 503 on 3 (each retried at most once).

### 4c. Class

**N3 kept** (leaves 4/5/7, ff.59v-62r): no prior plaintext or decipherment located after the search logged here and in AUDIT
1-3. The Oldenbarnevelt edition, the one printed series built from the holding file, neither prints nor calendars the letter,
and none of its letters of Nov 1605-Jul 1606 refers to it. **Not N4:** the Spanish side (Simancas, a surviving original or other
copy) is still unreachable, the sender and "V.S." are unidentified, six G3 phrases are still unsearched on IA full text (host
errors), and no specialist or archive has been asked. **Key: ours. Text: not known in print.** Depth **D1** (4a).

| item | class | depth | prior plaintext | prior decipherment | key | evidence | confidence |
|---|---|---|---|---|---|---|---|
| inv. 2442, leaves 4/5/7 (ff.59v-62r), 729 cipher words | **N3** (second audit, agrees with AUDIT 3) | **D1** (9.0% S digits; longest S run 7 < AD) | none located | none located | ours | cryptanalytic, fixed B/C1 key, key-aware reconciliation; judge FAIL -0.99 vs -0.808 | moderate on novelty (Spanish side unreachable) |

- **Safe sentence (AUDIT 3's, kept):** "Folios 59v-62r of the same Senisteros letter (Nationaal Archief 3.01.14 inv. 2442) read as
  Spanish under the vowel-digit key we recovered from its other passages; only fragments are graded as read so far. No prior
  decipherment or print was located after the search logged in AUDIT.md (N3)."
- **Unsafe sentence:** "The Oldenbarnevelt papers preserve an intercepted Spanish letter, now deciphered for the first time,
  in which a canon forged his patron's letter." ("intercepted" is not established -- the file says only "afschrift"; "deciphered"
  is a D4 word and these leaves are D1; "first time" is barred below N4; "canon" and "forged" go past what the leaves say.)

### 4d. Postmortem and propagation

- No over-claim found in AUDIT 3, NOTES section 22 or `second-opinions/PROMPT-chatgpt-L457.md` (the prompt quotes no grade,
  class or depth; its "a contested Toledo canonry" is posed as a question). The SECOND-OPINIONS-QUEUE.tsv row
  `SO-OLDEN-2442-L457` stays `queued`, unedited: class and counts unchanged.
- Gap closed: AUDIT 3 had not searched the Oldenbarnevelt edition for the leaf-4/5/7 names (NOTES section 22: "not re-run")
  nor its chronological list; both are now negative, with a positive control.
- **status.json carries no row for this target** (no `targets`/`results` entry for na-oldenbarnevelt-2442-1605; AUDIT 2's
  postmortem already named this as a parent follow-up). Not created here (the orchestrator writes status.json); handed up in
  the ROOM done line with the fields: L457 class N3 (two audits), depth D1, depth_pct 9.0, key ours, text not known;
  B/C1 N3, D2.
- Wording elsewhere, not edited (outside this item's files): QUEUE.md row VX-E03 calls the letter "intercepted Spanish
  correspondence", which the file does not establish; LOOSE-ENDS-2026-10-08.md line 3 and WORK-QUEUE row OLD-SIBS keep the
  superseded "different letter" phrasing (corrected in NOTES section 22).
- Next steps unchanged: (o1) scan 10 cipher block; (o2) masked re-cut + two blind passes for D2; ia-global re-run of the six
  phrases in `phrases_L457_V1OLD.txt` that met host errors (`--only ia-global`, about 6 requests) when be-api answers.

## AUDIT 5 (V-OLD10): scan 10 cipher block (ff.63v/64r right page), NOTES sections 23 and 23a

(The brief named this section "AUDIT 4 (V-OLD10)"; that heading is already taken by V1-OLD's second audit of leaves 4/5/7,
so it is numbered 5 here.) Verifier V-OLD10 (account 2, LANE FAMILY), 8 Oct 2026, 20:06-20:2x UTC by `date -u`. Brief
`.claude/briefs/runs/2026-10-08-ytbiz-family-1909-jobs.md` "### V-OLD10". Separate from the solvers (OLD-S10, OLD-O4); this
session changed no key, ciphertext, transcription, grade or reading. B/C1 (N3, D2) and leaves 4/5/7 (N3, D1) are kept as they
are; this item is classed beside them.

Claim under audit: "the scan 10 block (23 lines, ff.63v/64r right page) read under the folder's fixed B/C1 key: 191 cipher words
S 73 M 118 after the PREREG_OLD-O4 fold, digit S 26.3%, longest S stretch 7 digits (AD floor 24.2), fixed key rank 1/120 against
permuted keys (0.384 vs max 0.363), es1600 judge FAIL", plus section 23's content paragraph.

Depth bar copied before computing (`.claude/briefs/runs/2026-10-08-acct3-depth-bar.md`): CLAUDE.md 4a governs; cipher clause = a
contiguous H/C/S stretch longer than the AD (about 1.5 x unicity), H(K) = design key space plus every liberty (U wildcards, M
tokens, repairs, u/v and word-break choices); an unfitted external key does not shrink H(K); the zero-liberty reading is not used;
an external check is a D3/D4 element, not a D2 substitute; code clause n/a (no code values in this design); D2 = one clause plus
the verifier's own true, specific sentence.

### 5a. Prior work (before the first step)

`tools/prior_work.py ... --item-spec 'shelfmark=NA 3.01.14 inv. 2442;folio=63v-64r;canvas=10;date=1605-12-23;...' --step-type
audit --fetch` -> **exit 3 DONE**, which is false: the DONE row points at AUDIT.md:506, the done-line fields of AUDIT 4 (V1-OLD,
leaves 4/5/7), and AUDIT.md:462 says in so many words that scan 10's block "is still unread (step o1) and is outside this audit".
Recorded CLEAR with that reason (`--record ...:1-own:88232b`); the two LEAD rows were OLD-S10's own check line and this
verifier's claim (recorded CLEAR). Rows 3-solver (bourdeau, aaymeloglu) and 4-editions (Lonchay-Cuvelier I, Huygens Bescheiden
Oldenbarnevelt 1-3) CLEAR, carried from V1-OLD the same day; 3-tomokiyo CONTEXT (other letters). Check 2 (leaf and neighbours):
carried from OLD-S10 (no gloss or clear copy on scans 8-11); the three crops this verifier read (5b) show none either.

### 5b. Re-derivation and spot-check

- `python3 scripts/decode_L10.py --check` -> `committed reading matches a fresh run; {'clear': 13, 'S': 73, 'M': 118}`, exit 0.
  `--check --norm s10` -> `{'clear': 13, 'M': 141, 'S': 50}` (OLD-S10's registered counts), exit 0. Both claims reproduce.
- Eye-check, crops `images/crops_L10/L10_L06.jpg`, `L10_L15.jpg`, `L10_L16.jpg` (27 cipher tokens, this verifier knew the key, so a
  check of sign identity, not a blind read): L06 `p7r 4b28l4, 2n4 h3j4 d8 2n cl8r3g7 3 d8 2n4 m2g8r` ("por abuela una hija de un
  clerigo i de una muger"), L15 `c8n h4c4s4d7 d7n g4rc34 d8m8dr4n7 c7ll8g34l d8s4` ("[di]cen ha casado don Garcia de Medrano
  collegial de Sa-"), L16 `l4m4nc4 n4t2r4l d8 s7r34 d8l h4237 d8 s4nt34g7 3` ("-lamanca natural de Soria del h. de Santiago i")
  agree with the reconciled transcription sign for sign, 26 of 27. The one doubt: L16 `h4237` ("hauio", M): the image shows a
  sign with a cross-stroke after the 3 and before the 7, so `h4b3t7` "habito" is likely -- a solver-lane correction (it would
  lengthen nothing past the AD and changes no sense), not made here.
- Two grading points the solver flagged or that this verifier finds, recorded so the counts are not over-read: (i) `d7r` "dor"
  (L12) is the end of "inquisi-dor" split over a line, graded S by the lexicon rule though not a word on its own; (ii) the S-share
  control's margin is thin (0.384 vs 0.363; the runner-up is the 2/3 u/i swap) and the fold raised the permuted keys' mean too
  (0.201 -> 0.257), as section 23a says. The lexicon-hit-share control (0.684 vs best permutation 0.553, rank 1 of 120) does not
  involve the passes and is the stronger evidence for the key on this block. Neither changes the key, which is B/C1's.

### 5c. Depth (rule 4a, under the bar; AD arithmetic)

Base as AUDIT 2a: vowel map 5!, H(K0) = 6.91 bits; R = 1.83 bits per digit (AUDIT 2a's C1 row: U 16.1 from H(K) 29.49).
Liberties for this block: 118 M words at 2.32 bits each (AUDIT 2a's rule) = 273.8 bits; I 0; the OLD-O4 v->r / (->l fold is a
pre-registered grading normaliser applied to every key alike (5b), counted 0; word-break joins kept as written, counted 0 (a
lower bound). H(K) >= 6.91 + 273.8 = 280.7 bits; U = 280.7 / 1.83 = 153 digits; **AD >= 230 digits**. Even the folder's
small-liberty floor (24.2-24.4 digits, B/C1) is far above the longest contiguous S stretch here, **7 digit tokens** ("de santiago
i del", L16-L17; 6 under OLD-S10's registered s10 grades). **No cipher clause; code clause n/a. Ruling: D1** ("fragments read").

Why D1 is not a negative: as for leaves 4/5/7 (AUDIT 3c), the M grade comes from the blind-pass S rule (21.2% pass split, partly
line identity) and the passes' notation, not from the decode; 26 of 27 eye-checked tokens agree with the reconciled reading. The
named way up is a pair of fresh blind passes written in the r/l notation from the start (section 23a's next step for any block),
then a re-grade; a verifier's eye-check does not regrade tokens.

Verifier's sentence (not required at D1; written from the eye-checked L06/L15/L16 tokens, so a later D2 ruling has it in hand):
*the writer reports that a woman of the family concerned had as grandmother the daughter of a clérigo and of a woman married to
a herrero, and that Don García de Medrano -- a collegial of Salamanca, native of Soria, of the habit of Santiago -- is said to
have married into the same family.*

External plausibility (not a D3 element under the bar, not a check of the reading): *La casa de Salcedo de Aranguren* (1944,
Google Books `zCMPRLjKES4C`, snippet only) names an "Inquisidor Salcedo" with family "natural de Oluga u Olvega, en Soria" and a
Medrano in the same genealogy; García de Medrano of the Consejo Real is a known figure (*Historia del Colegio Viejo de San
Bartolomé*, 1768, `FqNLAAAAcAAJ`, among the phrase hits). This fits the decoded names and the Soria setting; it is not the letter.

- depth: **D1**; depth_pct: **26.3** (S digit tokens 112/426 under OLD-O4; 15.7 under OLD-S10's registered s10 grades);
  depth_unread: 314 digit tokens M (118 words), ordinary words and names alike; depth_check: "longest S stretch 7 digits vs AD
  >= 230 digits (5! map + 118 M words x 2.32 bits; small-liberty floor 24.2); lexicon control rank 1/120 (0.684 vs 0.553); S
  control rank 1/120 (0.384 vs 0.363); es1600 judge FAIL -1.121 vs real_p05 -0.837, shuffled -2.05 to -2.11"; decode_status:
  "fragments read" (scan 10 block). The letter as a whole keeps B/C1's D2.

### 5d. Novelty (template step 2)

| family | searched (8 Oct 2026, this session unless stated) | result |
|---|---|---|
| canonical series / sender and recipient editions | AUDIT 1-4: CODOIN (es1600 tomos), Lonchay-Cuvelier I (djvu grep), Rodríguez Villa 1906, Huygens Bescheiden Oldenbarnevelt 1-3 (full text, positive control in AUDIT 4); sender and recipient have no identified printed correspondence | not found (carried) |
| phrases in print (G3) | `tools/print_check.py --phrases phrases_L10_VOLD10.txt` (9 decoded phrases, modern spelling) -> `print-check-VOLD10.tsv`, 36 rows, 13 with hits: ia-global 1 (the bare name "el inquisidor Salcedo": inquisition histories), Google Books 9 (scattered-word matches: Calderón comedias, Fray Luis de Granada, Soria/Segovia nobiliarios, a 1605 Valladolid *Relación* naming Medrano), OpenAlex 1 (Logroño tribunal studies), CrossRef 2 then HTTP 429 for the other 7 (not retried) | not found; CrossRef partly blocked |
| names / substance | Google Books keyed, `country=US`: "inquisidor Salcedo" Medrano Soria (1: the Salcedo genealogy above), "Garcia de Medrano" Salcedo hermana mayorazgo (1: *Iberian Books*, a title list), "inquisidor Salcedo" colegial Oviedo herrero (0), Salcedo inquisidor herrero clerigo abuela Soria (0), "casa de Salcedo de Aranguren" inquisidor (1, same genealogy) | the clérigo/herrero descent story is not found in print; the genealogy shares two names (Salcedo, Medrano) but no date and no part of the story in its snippets -- a lead for a full-view read, not a print of this letter |
| prior-work check 5 | `tools/prior_work.py ... --reading reading_L10.txt --network`: took its phrases from the file's `#` header again (as in OLD-S10), so its SUBSTANCE row is a tool artefact; recorded CLEAR with the reason and the print_check run above | artefact; real search above |
| IA full text | ia-global through print_check (9 phrases) | not found |
| scholarship | OpenAlex 9 (via print_check), CrossRef 2 answered + 7 blocked (429); Semantic Scholar not run this session (AUDIT 3-4 runs on the same letter) | not found |
| holding archive | NA 3.01.14 EAD and printed inventory (AUDIT 1): "Merendeels in cijferschrift", no decipherment recorded | no decipherment |
| solver repositories | dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers clones grepped by V1-OLD the same day (AUDIT 4) | nothing on inv. 2442 (carried) |
| Simancas / PARES | dead host from the cloud | **unreachable** |
| JSTOR | not queued: AUDIT 2's rows cover the sender/recipient family | not queued (does not block N3) |

Requests this session: be-api.us.archive.org 9, www.googleapis.com 9 + 6, api.openalex.org 9, api.crossref.org 3 (one 429),
plus prior_work.py --network's own IA/Google Books calls. No archive host; no subagent calls.

**Class: N3** (scan 10 block, f.64r): no prior plaintext or decipherment located after the search logged here and in AUDIT 1-4.
Not N4 for the same reasons as B/C1 and leaves 4/5/7 (Simancas side unreachable, sender unidentified, no specialist asked; here
also CrossRef partly blocked and the Salcedo genealogy not read in full). **Key: ours** (the B/C1 vowel-digit key, VX-CT03).
Text: not known in print.

| item | class | depth | prior plaintext | prior decipherment | key | evidence | confidence |
|---|---|---|---|---|---|---|---|
| inv. 2442, scan 10 block (f.64r, 23 lines), 191 cipher words | **N3** | **D1** | none located | none located | ours | cryptanalytic, fixed B/C1 key, lexicon control rank 1/120; blind passes split 21.2%; judge FAIL -1.121 vs -0.837 | moderate on novelty; reading eye-checked on 27 tokens, 26 agree |

- **Safe sentence:** "The cipher passage on folio 64r of the same Senisteros letter (Nationaal Archief 3.01.14 inv. 2442) reads
  as Spanish under the vowel-digit key we recovered from its other passages; only fragments are graded as read so far. No prior
  decipherment or print was located after the search logged in AUDIT.md (N3)."
- **Unsafe sentence:** "We deciphered a hidden scandal in the ancestry of an Inquisitor and the Medrano family." (D1 is
  "fragments read"; the passage is the same letter, not a further document; "hidden scandal" goes past what the writer says,
  which is a question of descent he will not act on without V.S.'s opinion; the persons are not identified beyond their names.)

### 5e. Postmortem

No over-claim in sections 23 and 23a: both keep status open, call the reading "a solver's reading, mostly M-graded", leave depth
to the verifier, and flag the "dor" fragment and the thin S-control margin themselves. Carried here so they are not lost: (1)
prior_work.py's DONE for this item was a false match on the leaves 4/5/7 audit, and its `--reading` mode takes phrases from the
reading file's `#` header (twice now on this target) -- a tool issue for the parent, not fixed here; (2) L16 `h4237` is likely
`h4b3t7` "habito" (solver lane). SO row: `SO-OLDEN-2442-L10` queued with `second-opinions/PROMPT-chatgpt-L10.md` (N3, CLAUDE.md
verifier rule). D1, so no WORK-QUEUE AUD2 row (brief: AUD2-FAMILY-1 only at N3+ and D2+).

## AUDIT 6 (V-OLD-O5): leaves 4/5/7 (ff.59v-62r) re-graded after OLD-O2 and OLD-WB (NOTES sections 24-25)

Verifier V-OLD-O5 (account 2, LANE FAMILY-A2n, Opus), 10 Oct 2026, 03:13-03:2x UTC by `date -u`. Brief
`.claude/briefs/runs/2026-10-10-ytbiz-family-0209-jobs.md` "### V-OLD-O5" (step (o5)). Separate from OLD-O2 and OLD-WB (the
readers/scorers) and from AUDIT 3-5; not protecting any of them. No key, ciphertext, transcription, grade or reading changed.
Disk only, no host requests. Claim under audit: NOTES 24's re-grade (729 cipher words, H 0 C 0 S 165 M 564; digit S 266/1479 =
18.0%; longest S stretch 13 digits) and NOTES 25's boundary-insensitive figures (digit S 511/1479 = 34.6%; longest 17 digits;
control S share rank 1/120, stretch rank 46/120). Novelty search not redone: no decoded word changed (OLD-O2 and OLD-WB changed
grades only), so AUDIT 3/4's phrase searches stand.

### 6a. Re-derivation
- `python3 scripts/decode_L457.py --check` -> `committed reading matches a fresh run; {'clear': 70, 'M': 564, 'S': 165}`, exit 0.
- `python3 scripts/wb_stest.py` -> reproduces NOTES 25 to the digit (L4/L5/L7 S 266/65/180 digits, pooled 511/1479 = 34.6%;
  longest 13/9/17, pooled 17 "de chaues el coste del manteo i los quarenta"; control S share 0.448 rank 1/120, max wrong key
  0.435; stretch rank 46/120, 45 wrong keys tie at 17).
- Own script `depth/vold05_recount.py --check` (reads the committed token files only; exit 0): OLD-O2 grades L4 143/750, L5
  31/217, L7 92/512, pooled 266/1479 (18.0%), longest 13 digits ("con migo como amigo i en secreto"); OLD-WB grades pooled
  511/1479 (34.6%), longest 17. Agrees with both sections.
- Robustness (same script): OLD-WB's sign-agreement step re-run with the opposite alignment tie-break (ins > del > diag instead
  of diag > del > ins): sign-agreed cipher tokens 329 (OLD-WB 324), sign-agreement ceiling 20 digits (OLD-WB 17). Even this more
  favourable alignment cannot reach the floor of 24.2 digits, so the result does not hinge on OLD-WB's tie rule.

### 6b. Eye check (20 S words; rule committed first, b0ccb6929, `depth/VOLD05_eyecheck_rule.md`)
Rule: the 7th, 14th, ... S-graded cipher token on L4+L7 in `reading_L457_tokens.tsv` order (145 S tokens), first 20; viewed on
the masked O2 line crops (`images/crops_O2/`), sign by sign. Picks: L4a_05 737, L4a_13 c4rt4s, L4b_01 l7, L4b_10 n7, L4b_11 3,
L4b_14 s8cr8t7, L4b_16 d2d4r, L4b_18 q28, L4b_22 p7r, L4b_26 37, L4b_28 2n4, L4b_30 c4rt4, L7b_01 ch4, L7b_05 d8m4s, L7b_08 p7r,
L7b_11 m8, L7b_15 8n, L7b_19 h8ch7, L7b_21 v8r4, L7b_23 d8l. **20/20 agree with the image; 0 disagree; 0 cannot tell.** Every
O2 crop viewed held the reconciled line it is named for (the OLD-SIBS line-identity fault is gone). Key-aware verifier: a check of
sign identity, not a blind read; it regrades nothing. The S grade is therefore conservative rather than generous on this sample.
Incidental, not graded: L7b_23 shows `ch428s` clearly ("chaues").

### 6c. Depth (rule 4a, under `.claude/briefs/runs/2026-10-08-acct3-depth-bar.md`)
- Cipher clause: a contiguous H/C/S stretch longer than the AD. Registered grades (OLD-O2): longest 13 digits. Boundary-
  insensitive instrument (OLD-WB): 17 digits, which is also its sign-agreement ceiling and is matched by 45 of 119 wrong vowel maps
  (rank 46/120), so as a stretch it does not discriminate the key. Opposite tie-break ceiling: 20. All are below the folder's
  small-liberty floor (24.2 digits) and far below the AD with every M word counted (1078 digits under OLD-O2's 564 M; 795 under
  OLD-WB's 415 M). **Not met.**
- Code clause: n/a (no code values in this design).
- **Ruling: D1 kept** ("fragments read") for leaves 4/5/7. depth_pct **18.0** (S digits 266/1479 under the registered OLD-O2
  grades; up from 9.0 in AUDIT 3/4); the boundary-insensitive share 34.6% is reported beside it as a separate instrument, not
  the registered grade. depth_unread: 1213 digit tokens M (564 words), almost all ordinary words, not names. depth_check:
  "longest S stretch 13 digits registered / 17 boundary-insensitive (= sign-agreement ceiling; 20 with the opposite tie-break)
  vs floor 24.2 and AD 795-1078 digits; S share control rank 1/120 both instruments; stretch control rank 46/120; eye check 20/20".
  decode_status: "fragments read" (L4/L5/L7). The letter as a whole keeps B/C1's D2 (AUDIT 2).
- Why D1 is not a negative: the reading's quality on the image (6b, AUDIT 3a) is higher than the grades show; the stretch is
  capped by sign disagreements between the two masked machine passes (OLD-WB: 405 of 415 M tokens are sign-disagreement M), and
  the 10% rule bars a third machine pass. The named way up is a person's sign sort on the L4/L7 masked crops (NOTES 25), then a
  re-grade; no further scoring rule on these passes can pass 17-20 digits.
- Verifier's sentence (AUDIT 3c's, still not required at D1): *the writer says that, finding himself pressed, he made a signature
  of V.S. on a sheet of paper as best he could and had a servant write out the substance of the letter, telling the servant that
  V.S. had left him some signatures in blank.*

### 6d. Class
**N3 carried** (leaves 4/5/7): no reading changed, so AUDIT 3/4's search and reasons for not N4 stand unchanged. **Key: ours.**
Text: not known in print. N3 with D1: no second-audit WORK-QUEUE row (that needs D2+).

| item | class | depth | prior plaintext | prior decipherment | key | evidence | confidence |
|---|---|---|---|---|---|---|---|
| inv. 2442, leaves 4/5/7 (ff.59v-62r), 729 cipher words | **N3** (carried) | **D1** (18.0% S digits; longest S run 13 registered / 17 boundary-insensitive < floor 24.2) | none located | none located | ours | cryptanalytic, fixed B/C1 key, masked re-cut + two blind passes (18.2% split), S share control rank 1/120; eye check 20/20; judge es1600 FAIL -1.017 vs real_p05 -0.818 | moderate on novelty; reading verified by eye on sampled tokens, graded fragments only |

- **Safe sentence:** "Folios 59v-62r of the same Senisteros letter (Nationaal Archief 3.01.14 inv. 2442) read as Spanish under the
  vowel-digit key we recovered from its other passages; about a fifth of the cipher is graded as read, in fragments. No prior
  decipherment or print was located after the search logged in AUDIT.md (N3)."
- **Unsafe sentence:** "Folios 59v-62r are now partially deciphered (about 35%)." (D2 wording at D1; 34.6% is a separate,
  boundary-insensitive instrument whose stretch does not beat its wrong-key control, not the registered grade.)

### 6e. Postmortem and propagation
No over-claim in NOTES 24-25: both keep status open, report the stretch below the floor and leave depth to the verifier.
Propagation (rule 10): class and depth unchanged, reading unchanged -> no edit to status.json (it carries no row for this target;
the orchestrator's) or to the `SO-OLDEN-2442-L457` row and its prompt (whose "only partly graded as secure" still holds).
