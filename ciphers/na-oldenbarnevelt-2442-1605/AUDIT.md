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
- Plaintext as read (B): "la he dicho que solo desseo uer aca a V.Sª, i ella lo dessea harto, i se lamenta de uer los
  tiempos que corren, i me enuio el pesame delo de Siguença, porque hubo del mui buenas esperanças; i muchas ueces no
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
