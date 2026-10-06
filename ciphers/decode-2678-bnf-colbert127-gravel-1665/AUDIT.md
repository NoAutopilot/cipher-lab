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
