# AUDIT -- decode-2678-bnf-colbert127-gravel-1665 (R2678, BnF Mélanges de Colbert 127 f.349r-v)

## AUDIT 1 -- verifier R10-DEC2678V, 6 Oct 2026 (09:47-09:56 UTC by date -u), for LANE LANE-RUN10-account-1

Claim under audit (R9-DEC2678C, NOTES.md section "The 1672 Gravel key tested on R2678"): "Tomokiyo's published
Colbert-Gravel 1672 key PASSes PREREG ca9a62902 on R2678 P2/P3; H 11 M 2 U 2 of 15; decode_key --check 0".
The verifier is not the solver and did not decode beyond re-running the committed scripts.

**Verdict: N3 · key `published` (Tomokiyo) · depth D2 (about 73%).**

### 1. Item

| field | value |
|---|---|
| sender | "[R.] de Gravel[le]" (signature; Robert de Gravel is the usual identification, not checked here), French envoy at the Diet, Ratisbon |
| recipient | Jean-Baptiste Colbert |
| date, place | "a Ratisbone ce 29 Janvier 1665" (f.349v, `images/c357_dateline_subscription.jpg`; re-viewed by this verifier: dateline and "R. de Grave[l]" signature confirmed) |
| shelfmark | BnF Mélanges de Colbert 127, f.349r-v (Gallica btv1b10035540v canvases 356-357); DECODE R2678; BnF sommaire cc954302 "Fol. 349 · l'abbé « de Gravel »" |
| ciphertext | P1 `29`; P2 `80 62 41 73_ 22: 51`; P3 `48^ 93 71 37 60^ 92 58^ 0` (`ciphertext.tsv`) |
| reading | P1 `[29]`; P2 `so n f re [22:] e`; P3 `le s c ha no i ne [0]` |
| clear context (f.349r) | "pour 29 auquel on doit donner 15000 ... Pour [P2] qui en doit avoir 500. Pour Mr Frichmann auquel il en est deu 600, et pour [P3] qui doivent aussy recevoir 1000 Reichsdalles pour la demye année de leur pension" |

### 2. Checks of the claim

| check | result |
|---|---|
| PREREG before the scored run | **yes.** `PREREG-gravel1672-2026-10-06.md`, `key_gravel1672.tsv`, `ciphertext.tsv` and the key image entered in ca9a6290 (06:46:29 UTC); `gravel1672_test.py` and `.out` in fd739c8d (06:48:32 UTC). `git diff ca9a6290 origin/main` on the PREREG, key and ciphertext files: empty. The PREREG itself discloses that key and groups had been seen together before it was written (the *choice* of test is post hoc; the gate is mechanical). |
| re-run | `python3 gravel1672_test.py --check` -> "check ok" (T -0.9367, p1 0.0000, p2 0.0035, power 0.985, PASS); `tools/decode_key.py ... --check` -> "H 11, M 2, U 2; reading up to date", exit 0 |
| key cells vs Tomokiyo's image | every cell used (29 fi, 37 ha, 41 f, 48^ le, 51 e, 58^ ne, 60^ no, 62 n, 71 c, 73_ re, 80 [so], 92 i, 93 s) read by eye on `sources/cryptiana/keys/img/louisxiv_0gravel1672.png`: all match, marks included; 80 is bracketed (M) as graded |
| groups vs leaf | native crop `images/src_ark_..._f356_4800_4950_3500_800.jpg` re-viewed: underline under 73, two points over 22, overlines over 48, 60, 58, one trailing 0 after 58; agrees with `ciphertext.tsv` |
| controls can differ (rule 3 orthogonality) | **yes for both.** Control 1 permutes key values -> the decoded letters change -> T (trigram log-prob) changes. Control 2 permutes token order -> T is order-dependent -> changes. Neither manipulation is orthogonal to the statistic. |
| matched power at N=14 | computed honestly for control 1 (200 fr17 spans x 500 key shuffles, same key and design) -> 0.985. Two caveats, neither reverses the PASS: (a) synthetic spans have 14 decodable tokens, the target 12 (2 U), so power is slightly optimistic; (b) power was not computed for control 2. T also runs across the P2/P3 join (one letter pair). |
| grades | H 11 / M 2 / U 2 accepted. 51 = e kept H (PREREG's pre-run clarification: attested alphabet value over the bracketed [lu]). Note for any outward sentence: P2 as a *word* ("son fr[èr]e") needs 22: = r, which is grade I (context only, not in the key) and 80 = so is M; P3 "le s c ha no i ne" is a contiguous run of six H tokens. |
| identity | the leaf says Gravel at Ratisbon, 29 Jan 1665, as DECODE, Bourdeau and the BnF sommaire do (R9-DEC2678's correction of R8 stands). Whether "R. de Gravel" (Robert) and the abbé Jacques de Gravel of the 1672 key letter are two brothers is grade I, not checked here. |
| key provenance | Satoshi Tomokiyo, cryptiana.web.fc2.com/code/louisxiv0.htm, "Colbert-Gravel Cipher (1672)", built from the period interlinear decipherment of Mél. Colbert 159 f.102; snapshot unmodified in `sources/cryptiana/keys/img/`; credited in NOTES.md. **Key source class: published.** It is a 1672 key on a 1665 letter: same design and largely the same cells, identity of the keys not shown (22:, 0, 29 outside the table). |

### 3. Novelty search log (6 Oct 2026, this session)

| family | searched | result |
|---|---|---|
| (a)/(c) canonical series, documentary editions | Auerbach, *Recueil des instructions ... Diète germanique* (1912) and its later volumes, via Google Books API snippets (`"Diète germanique" "Recueil des instructions" Gravel`): 6 volumes surfaced, snippets on Gravel's career only. Auerbach, *La France et le Saint Empire* (1912), Gallica bpt6k33108b: ContentSearch for "Gravel" returned 0, so the volume has no searchable text there -- **unreachable as a test**, not a negative. Clément, *Lettres ... de Colbert*: already searched by GF-A2B-1 (3 Oct), no Gravel letter of 29 Jan 1665. | no print of this letter or its pension list located |
| (b) sender/recipient correspondence | AE Correspondance politique Allemagne 194 (Court-Gravel, Jan-May 1665): unpublished, not online (R9-DEC2678B); Inventaire sommaire AE t. I (1903) snippets only | unreachable |
| (d) holding archive | BnF sommaire cc954302 (R9-DEC2678): describes f.349 only as "l'abbé « de Gravel »" | no decipherment noted |
| (e) full text | `tools/print_check.py` (ia-global, gbooks, openalex), 6 phrases from the reading and its clear frame (`phrases.txt`, `print-check.tsv`): IA full text 0/6; OpenAlex 0/6; Google Books hits only word-level noise (coutumes, arrêts, 1791 journals) | no hits |
| (e) targeted Google Books | `"Gravel" "Frichmann"` (242), `"Frischmann" Gravel 1665 pension` (0), `"Gravel" Ratisbonne 1665 pensions chanoines` (0), `"Gravel" Colbert 1665 "rixdales"` (0), 6 snippet probes inside Haug 2015 | see next row |
| (g) scholarship | **Tilman Haug, *Ungleiche Außenbeziehungen und grenzüberschreitende Patronage. Die französische Krone und die geistlichen Kurfürsten (1648-1679)*, Böhlau 2015 (Google Books XOdrDAAAQBAJ)**: a study of exactly this pension system; snippets show Gravel engaging Johann Frischmann paid from an "extraordinaires" budget, pensions paid in 1665 (citing AMAE CP Allemagne 195 f.19r), Gravel and the Mainz Domkapitel. It cites the AE series; no snippet cites Mél. Colbert 127 or quotes this letter. Not open access (OAPEN/DOAB answered 403, host stopped; OpenAlex lists only reviews). Also: Johann Frischmann biography (1904, qggUAQAAIAAJ) snippet only. | **the most likely place for a summary of this pension list; not readable from the cloud.** JSTOR rows queued (family i and ii) |
| (f) solver repos, blogs | Bourdeau and Aymeloglu catalogues (checked by GF-A2B-1 3 Oct and R9-DEC2678 6 Oct); Tomokiyo's louisxiv0.htm names only f.102 (1672) for this cipher | no reading of R2678 |

Requests this session: be-api.us.archive.org 6, archive.org 4 (advancedsearch), www.googleapis.com 18 (key, country=US),
api.openalex.org 7, library.oapen.org 1 (403, stopped), directory.doabooks.org 1 (refused), gallica.bnf.fr 5 (SRU 1,
ContentSearch 4), all >= 1.6 s apart.

### 4. Classification

**N3** -- no prior plaintext or decipherment of R2678's cipher passages located after the logged search. Not N4: Haug
(2015), the study closest to this letter's subject, and AE CP Allemagne 194 could not be read; Auerbach's 1912 volumes
were reached only by snippets. Prior plaintext: not found. Prior decipherment: not found (DECODE lists the record
"Non-decrypted"). Evidence quality: moderate (pre-registered controls, a published key from an independent leaf, mark
agreement 4/5). Confidence in the P3 reading: high; in P2 as a word: moderate.

Key: **published** (Tomokiyo's 1672 Colbert-Gravel table, applied by us to a 1665 letter). Text: not known in print.

**Depth D2** (rule 4a). Cipher tokens 15 (cleartext excluded): H 11, C 0, S 0 -> **73%**; unread 4: name/code group 1
(`29`, the 15,000-Rd payee), other 3 (`80` M bracketed cell, `22:` U, `0` U). D2 basis: the contiguous six-token H run
in P3 read with a key taken from a different leaf (not fitted to this text), backed by the pre-registered value- and
order-shuffle controls at the target's own N (p1 0.000, p2 0.0035, power 0.985) and by grammatical agreement with the
clear frame ("qui doivent", plural). Not D3: below 80%.
D2 sentence (verifier's own): *In Gravel's letter to Colbert of 29 Jan 1665, the enciphered recipients of the
1,000-Reichsthaler half-year pension on f.349r read "les chanoine[s]" under Tomokiyo's 1672 Colbert-Gravel key.*

**Safe sentence:** "Two short cipher passages in R. de Gravel's letter to Colbert, Ratisbon, 29 Jan 1665
(BnF Mélanges de Colbert 127 f.349), partially deciphered (about 73%) with Satoshi Tomokiyo's published key of the
1672 Colbert-Gravel cipher; one passage names 'les chanoine[s]' as recipients of a half-year pension. No prior
decipherment located (N3)."
**Unsafe sentence:** "We have deciphered Gravel's 1665 letter" / "the first reading of this pension list" / "the
1665 key is the 1672 key" / "29 is the Elector of Mainz" (no evidence) / "son frère" as an H reading.

### 5. Postmortem

No over-claim found in the folder: NOTES.md uses "partial", "found / not found" and leaves novelty to the verifier.
Two precision notes carried here rather than edited into the solver's section: (1) the power figure covers control 1
only and assumes no unkeyed tokens; (2) "son fr[èr]e" rests on an I-grade 22: and an M-grade 80, so outward text
quotes P3, not P2. SECOND-OPINIONS-QUEUE row SO-R2678 filed this session (N3).

## AUDIT 2 -- verifier D1-DEC2678A2, 6 Oct 2026 (12:48-12:59 UTC by date -u), for LANE DEFAULT-account-1-20261006-1240

Second adversarial novelty audit (Outreach gate 2). This session is separate from AUDIT 1 (R10-DEC2678V) and from every
solver (R8-G2678, R9-DEC2678*, R10-DEC2678S). It tried to find the plaintext or a decipherment of the cipher passages of
Gravel to Colbert, Ratisbon, 29 Jan 1665 (Mél. Colbert 127 f.349) in print and on the project pages. It did not decode.
Claim under audit: AUDIT 1's verdict "N3, key published, D2 about 73%" and the status.json line "... No prior decipherment located."

**Verdict: N3 (confirmed, not raised) · key `published` (Tomokiyo) · depth D2 (about 73%, re-checked).**

### 1. Item (from the repository, unchanged since AUDIT 1)
Ciphertext `ciphertext.tsv` P1 `29`; P2 `80 62 41 73_ 22: 51`; P3 `48^ 93 71 37 60^ 92 58^ 0`. Reading
`reading_gravel1672.txt`: P1 `[29]`; P2 `so n f re [22:] e`; P3 `le s c ha no i ne [0]`. No change to the reading, key or
ciphertext since AUDIT 1: the groups and reading match AUDIT 1's table token for token, and `tools/decode_key.py
<folder> --check` re-run here prints "tokens 15: H 11, M 2, U 2 / reading up to date" (the clone is shallow, so this is a
content check, not a `git log` one). The SO-R2678 row needs no propagation.

### 2. Search log (6 Oct 2026, this session)

| family | searched | result |
|---|---|---|
| (a) canonical series: Depping, *Correspondance administrative sous le règne de Louis XIV* (4 vols, 1850-55) | IA full text (be-api) for "Gravel" in `correspondancead01depp`-`04depp`; t. III `_djvu.txt` fetched and read at every hit | **t. III prints Gravel-to-Colbert letters, but only on recruiting German tin-plate workers: 6 Aug, 3 Sept, 22 Oct, 12 Nov, 17 Dec 1665, 8 Sept 1668, 7 June 1669 (table entry, pp. 735 and 740), and Mainz, 1 July 1673 (no. 70, pension receipts of Mainz chancellor Mertz).** t. I, II: 0 hits; t. IV: one Gravel-to-Louvois letter. **No letter of 29 Jan 1665, no Ratisbon pension list.** |
| (a) Clément, *Lettres, instructions et mémoires de Colbert* | IA be-api "Gravel" in `colbert-lettres-instructions-et-memoires-de-colbert-v-1`..`v-7` (independent re-run of GF-A2B-1) | hits in v-1, v-5, v-6 only; none carries 1665, Ratisbonne or pension in its snippet; v-2/3/4/7: 0 |
| (c) *Recueil des instructions*: Diète germanique (Auerbach 1912) and Auerbach, *La France et le Saint Empire* (1912) | IA advancedsearch (no Diète volume on IA); Google Books API snippets | Auerbach 1912 cites **"29 janvier 1665, vol. CXCIV, fol. 44"**, i.e. Gravel's own report to the court of the same day (AE CP Allemagne 194 f.44), on the Capitulation dispute, not the pension list; "Diète germanique" + Gravel + 1665 + pensions/chanoines: 0 (first try 503, one retry after a pause: 0). Volume full text not reached. |
| (b) sender/recipient correspondence | AE CP Allemagne 194 (Gravel-court, 1665): unpublished; Livet, *L'intendance d'Alsace* (1956) and the Frischmann biography (1904), Google Books snippets | only Gravel's Alsace business and Frischmann's career; nothing on this list |
| (d) holding archive | BnF sommaire cc954302 (read by R9-DEC2678); La Roncière, *Catalogue ... Mélanges de Colbert* (1920, Google Books gJQ3AQAAMAAJ, no snippet) | catalogue entry only ("l'abbé de Gravel", per Bourdeau's quote of t. I p. 270) |
| (e) full text, phrase search | IA be-api global: "Ratisbonne ce 29 janvier 1665" 0; "chanoines qui doivent aussy recevoir" 0; "pour la demye année de leur pension" 0; "Gravel" "Frichmann" 23 (Legrand-Girarde, Waddington, an inventory of Colbert's outgoing letters: none this letter). Google Books: `"Gravel" "29 janvier 1665"` 11 (Auerbach and Livet only, above), `"Ratisbonne" "29 janvier 1665"` 5, `"Gravel" "17100" rixdales` 0, `"Gravel" Ratisbonne 1665 "chanoines" pension` 0, `"Gravel" "Frischmann" 1665` 40 (career notices), `"Gravel" Regensburg 1665 Pension Domherren` 0, `Gravel 17100 Reichstaler 1665` 0, `"demye année de leur pension"` (word noise, 16th-c. memoirs) | no print of the letter or its cipher passages |
| (f) project pages, solver repos | **Tomokiyo, cryptiana.web.fc2.com/code/louisxiv0.htm, live page fetched 6 Oct 2026** (also in the local snapshot `sources/cryptiana/web/louisxiv0.htm` l. 496); DECODE RecordsView/2678 (login-free, live); Bourdeau `targets/colbert/NOTES.md` item a and `targets/napoleon/unsolved.txt` l. 256 (clone at HEAD of 5 Oct 2026); Aymeloglu `catalogue/decode-records.jsonl` | **Tomokiyo: "(1665) Melanges de Colbert 127, f.349, is a letter from Ratisbon, dated 29[?] January 1665, signed "Estrauelse"[?]. It has a few words in figure cipher, not deciphered. The cipher seems different from the one in the same volume below [Colbert-Millet 1665]."** DECODE: "Status: Non-decrypted". Bourdeau: "Not attacked (three names)". Aymeloglu: catalogue row only. Three independent project pages each record the passages as undeciphered. |
| (g) scholarship | OpenAlex (4 queries: 0 relevant), Semantic Scholar (2: 0), CORE (2: 0), CrossRef (2: noise only), HAL (2: 0), Persée (3: HTML search not discriminating, result list rendered client-side, **unreachable as a test**). Haug 2015 (Böhlau; the study of this pension system): Google Books probes `Domherren`/`Reichstaler`/`Frischmann` 1665: 0; **not readable** (AUDIT 1: OAPEN/DOAB 403) | no prior plaintext or decipherment located; Haug still unread |
| JSTOR | AUDIT 1's rows 301 (family i: Gravel+Ratisbon+1665+pension+cipher) and 302 (family ii: bare quoted phrase "demye année de leur pension") and 303 already cover both families | no new row queued |

Requests this session: www.googleapis.com 18 (key, country=US; one 503, one retry), be-api.us.archive.org 15,
archive.org 5 (advancedsearch 4, djvu 1), api.openalex.org 4, api.semanticscholar.org 2, api.core.ac.uk 2, api.crossref.org 2,
api.archives-ouvertes.fr 2, www.persee.fr 3, cryptiana.web.fc2.com 3, de-crypt.org 1, raw.githubusercontent.com 1,
api.github.com 2 (403 on code search, stopped), github.com 2 shallow clones; all serial, >= 1.6 s apart.

### 3. Findings against AUDIT 1
1. **AUDIT 1 row (f) missed Tomokiyo's own f.349 paragraph.** It said louisxiv0.htm "names only f.102 (1672) for this
   cipher", which is true of the key section but leaves out that the same page lists this very letter as "not
   deciphered" and judges its cipher "different from" the Colbert-Millet 1665 one. This *strengthens* N3 on the
   decipherment side (a key specialist saw the passages and left them unread) and shows the 1665 letter was not
   matched to the 1672 Gravel table on his page. Not an over-claim; a gap in the log, corrected here.
2. **Writer reading differs.** Tomokiyo reads the signature "Estrauelse"[?]; the folder reads "R. de Grave[l]" from the
   leaf (AUDIT 1 re-viewed the crop), as do DECODE (uploader: illegible), Bourdeau ("l'abbé de Gravel", La Roncière) and the
   BnF sommaire. Not settled here (verifier does not read); outward text names the sender as "R. de Gravel" with the BnF
   catalogue, and should not add "abbé Jacques" (AUDIT 1's own caution stands).
3. **Depping covered for the first time.** The standard edition of Colbert's administrative correspondence prints
   Gravel letters of 1665 to Colbert, but not this one, and none on pensions at the Diet.
4. No over-claiming sentence found in NOTES.md, the SO prompt or status.json (grep for first/novel/unpublished/newly/never
   printed: none in a claim). status.json's "No prior decipherment located" is N3-safe.

### 4. Classification
**N3** -- no prior plaintext or decipherment of R2678's cipher passages located after two independent logged searches.
Evidence quality: good on the decipherment side (DECODE, Tomokiyo and Bourdeau each record the passages as undeciphered,
6 Oct 2026); moderate on the plaintext side. **Not N4**: the principal *editions* are now covered (Depping, Clément:
negative), but the two places a plaintext of this pension list (who the 15,000 Rd payee and "les chanoines" were) could
sit are still unread: Haug 2015 and the AE CP Allemagne 194-195 dossiers (with Auerbach's 1912 Diète volume reached only by
snippets). If Haug names the payees from the AE copies, the class would be N2 (plaintext known elsewhere, no prior mapping
of this ciphertext), not N4. Confidence: high that no decipherment exists in print; moderate that the plaintext is unprinted.
Key source: **published** (Satoshi Tomokiyo's Colbert-Gravel cipher of 1672, rebuilt from the period decipherment of Mél.
Colbert 159 f.102), applied by us to a 1665 letter. Text: not known in print.

**Depth re-check (rule 4a), N = 15 cipher tokens:** H 11, C 0, S 0 -> **73%** (11/15). Unread 4: name/code 1 (`29`),
other 3 (`80` M, `22:` U, `0` U). **D2 kept.** D2 needs a stretch above the authentication distance: here the key was not
fitted to this text (published, from another leaf, no liberties taken), so the six-token H run `48^ 93 71 37 60^ 92`
-> "les cha no i" plus `58^` "ne" counts, backed by the pre-registered controls (AUDIT 1: p1 0.000, p2 0.0035, power
0.985 at N=14). Not D3 (< 80%). The D2 sentence (AUDIT 1's) stands: *In Gravel's letter to Colbert of 29 Jan 1665, the
enciphered recipients of the 1,000-Reichsthaler half-year pension on f.349r read "les chanoine[s]" under Tomokiyo's
1672 Colbert-Gravel key.*

**Safe sentence:** "Two short cipher passages in R. de Gravel's letter to Colbert, Ratisbon, 29 Jan 1665 (BnF Mélanges
de Colbert 127 f.349; DECODE R2678, listed 'Non-decrypted'; Tomokiyo's Colbert page lists it 'not deciphered'), partially
deciphered (about 73%) with Satoshi Tomokiyo's published key of the 1672 Colbert-Gravel cipher; one passage names
'les chanoine[s]' as recipients of a half-year pension. No prior decipherment located (N3)."
**Unsafe sentence:** "first decipherment" / "previously unread pension list" (N3, not N4: Haug 2015 and AE CP Allemagne
194-195 unread) / "the 1665 key is the 1672 key" / "Tomokiyo's key for this letter" (his page judges this cipher
different from the Millet one and gives no key for f.349) / "son frère" as an H reading / "the abbé Jacques de Gravel wrote it".

### 5. What would move the class
N4 (or N2): Haug 2015 read at its 1665 pension pages (a library or an owner-side read; OAPEN/DOAB 403 from the cloud) and
the JSTOR rows 301-303 answered. Neither blocks N3.
