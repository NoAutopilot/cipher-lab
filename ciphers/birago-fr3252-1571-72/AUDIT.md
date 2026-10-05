# AUDIT: fr.3252 f.47r hash relabels of CEPPO-WITNESS-PAIRS (VERIFY-CEPPO-WP, 3 Oct 2026)

Verifier: worker VERIFY-CEPPO-WP (account 2, LANE-A2PUSH, for the account-3 orchestrator), a separate session from the
solver CEPPO-WITNESS-PAIRS (1942dc4d, PREREG e1760f2e). Brief `.claude/briefs/runs/2026-10-03-acct3-verify-ceppo-wp.md`.
Clock read 01:39 UTC at start. Disk only: 0 network requests, 0 subagents. No novelty class is assigned or changed here.
f.87 (fr.3251) is audited in `../ceppo-nevers-fr3251-1570s/AUDIT.md`, last section.

**Claim under audit.** Six f.47r hash tiles that the two blind readers labelled S88 (t) against S75/S60, and that the third
reader (NEVBIR-47C) left UNSETTLED, are upright-stem hashes: L03.6, L04.32, L08.38, L10.10, L10.35, L12.29. The witness
rule R-hash (upright = S24 o, slanted = S88 t) makes them S24 (o). Proposed sequence `harvest/witness_pairs/f47_passE.tsv`.

## 1. The witness rule, second eye
`harvest/witness_pairs/w36v_x1000_y120.jpg` (fr.3252 f.36v top, 2.5x) read by this verifier's own eye. On line 2, the
slanted-stem hash carries a gloss **t** and the upright hash next to it carries **o**. On line 3, another upright hash
carries **o**. That is 3 of the solver's 6 hash tallies, reproduced independently. Grade M (one more eye; no period key).
The gloss over the barred 8 in this crop was not legible enough for this verifier to confirm R-8 here.

## 2. The six tiles, by eye
Composites cut from `images/f47/recut/` (2x, autocontrast; not committed):
| tile | context (passE) | stem | slanted hash nearby for contrast |
|---|---|---|---|
| L03.6 | S49 [x] S47 | upright | - |
| L04.32 | S23 [x] S57 | upright (at the strip edge, bars partly cut) | - |
| L08.38 | S84 [x] S89 | upright | L08.35 slanted |
| L10.10 | S57 [x] S35 | upright | L10.4, L10.6 slanted |
| L10.35 | S74 [x] S49 | upright | L10.42 slanted |
| L12.29 | S74 [x] S23 | upright | L12.37 slanted |
All six are upright, and the slanted form on the same lines is plainly different. Rule (i) is met for all six.

## 3. Re-derivation (rule 7)
`decode_control.py harvest/witness_pairs/f47_passE.tsv --extra X_THETA2=r --out ...` reproduces
`f47_reading_passE_s1/s2/s3.txt` byte for byte. (This folder has no decode.json; decode_control.py is the f.47 decoder.)

## 4. Controls at fresh seeds (the solver used 1-3)
- Key control at the two-reader error 0.33 (200 shuffles, 20 windows): seeds 4/5/6 give z **4.56 / 4.87 / 5.31**, rank
  **1/201** in each, power **20/20** (z median 7.61-7.95). The real key's score is -1.5133 (passD -1.5267).
- In-family flip control (the same 6 S88 -> S24 flips at random S88 positions, base = passE with the six put back to S88,
  1000 draws): seed 7 **0/1000**, seed 8 **0/1000** (p 0.001). The specific tiles the rule picks beat random hash flips.
  This is the control the solver could not run on f.47 (base passD has '?' there); it is the strongest number here.
- Judge (solver's run, not changed by this audit): `FAIL language: score=-1.524, null_p99=-1.788, real_p05=-0.906,
  real_median=-0.826, mode=both, N=782` (passD -1.543). Gate (iii) "judge not worse" is met.

## 5. Ruling
**Accepted: all 6 as S (o).** Endorsed S on f.47r: **0 -> 6 of 771**. Grades on the endorsed sequence `f47_passE.tsv`:
S 6, M 751, U 13. H 0, C 0. Cryptanalytic result with a published key; not a reading of the letter (judge FAIL). The
committed passD files are left as the record; `harvest/witness_pairs/f47_passE.tsv` is the endorsed sequence.

Not endorsed by this audit: R-8 and R-6 on f.47r (28/28, 39/39). Those agree with the third reader, but their shuffle
control is non-discriminating by construction (the solver says so), and S74 = m rests on elimination. Nothing was
relabelled there, so there is nothing to endorse.

## For the orchestrator (VERIFY-CEPPO-WP, f.47r)
- Verdict: **6 accepted**, endorsed S 0 -> 6. PROGRESS.tsv "Birago 1571 fr.3252 f.47" set from this section. status.json is yours.
- Still open: S74 = m by elimination (a legible gloss over a blob-6 on f.36r/f.37r would settle R-6), and S76/S91 has no rule.

# AUDIT 2 (A3V-VB3252, 4 Oct 2026): fr.3252 no.77 (f.117r), no.24 (f.36-37), no.30 (f.47r) -- first novelty audits

Verifier: worker A3V-VB3252 (account 3, for LANE-A3V), brief `.claude/briefs/runs/2026-10-04-acct3-a3v-wave2.md`; a session separate
from every solver of these letters (NEVBIR-3252/-B, NEVBIR-117C, NEVBIR-47/47C, F36-READ, F36-GLOSS, F36R-REREAD, A1-BIR-*, BIR-*) and
from VERIFY-CEPPO-WP above, which assigned no class. Clock 03:12-03:2x UTC by `date -u`. No decoding, no change to key, ciphertext or
reading. Section 1 above (VERIFY-CEPPO-WP) is untouched.

## 1. Extract (from the folder, per item)

| item | date, place | sender -> recipient | lang | cipher signs | firm portion (rule 4) | key | gloss on the leaf |
|---|---|---|---|---|---|---|---|
| no.24, f.36r-37r (Gallica btv1b9060232m canvases 37-38) | Saluzzo, 5 Apr 1571 | Lodovico Birago -> Louis de Gonzague, duc de Nevers | Italian | 947 (F36R-REREAD) | **10 C of 947 (1.1%)**: v36top_L01 "parlandone il signor" positions where both readers agree and the printed key = the clerk's gloss; 689 M, 229 U, 19 null; 0 H, 0 S | Ceppo-Nevers, printed by Tomokiyo (reconstructed by him from fr.4702 ff.36-37, a different volume); control-backed z 5.8-7.8 | **yes: the clerk's letter-by-letter interlinear decipherment on every passage** |
| no.30, f.47r (canvas 48) | Saluzzo, 26 Apr 1571 | Birago -> Nevers | Italian | 771 | **S 6 of 771 (0.8%)**: six upright-hash tiles = o (VERIFY-CEPPO-WP); M 751, U 13 | Ceppo-Nevers printed (Tomokiyo); z 4.56-5.31 | none |
| no.77, f.117r (canvas 118) | Saluces, 13 Mar 1572 | Birago -> Nevers | French (secretary hand) | 279 | **S 190 of 279 (68%)** (BIR-APPLY: A1-BIR-VERIFY and BIR-OPEN agree, or base S); M 63, U 26; 0 H, 0 C | Nevers-Birago 1572, printed by Tomokiyo (from fr.3251 no.87's attached decipherment); posnull PASS | none |

Readings audited: f.117r `../nevers-birago-fr3251-1572/harvest/tx_decode/eye/apply/reading_f117_apply.txt` (judge FAIL -1.224 vs real_p05
-0.899); f.36 `harvest/f36r/reading_key_v2*` (judge FAIL -1.487 vs -0.929); f.47r `harvest/witness_pairs/f47_reading_passE_*` (judge FAIL
-1.524 vs -0.906). Distinctive firm runs: f.117r "intention de conuenir", "poursuoir le gouerne[ment]", "deuant nous", "[et] fauoriser ces
affaires", "s'il vous sembl[e]", "[quello]" and the word codes turino/carmagnola; f.36 "parlandone il signor"; f.47r none (six isolated o).
What the solvers searched: NOTES.md "Check-solved", "Web and blog check", "Premise check" (NEVBIR-3252, 2 Oct 2026); HARVEST-D intake
(`../ceppo-nevers-fr3251-1570s/NOTES.md`, 28 Sept 2026).

## 2. Independent search (4 Oct 2026; request counts per host at the end)

| family | what was searched, by this verifier | result |
|---|---|---|
| **N0 basis, f.36, by eye** | `../ceppo-nevers-fr3251-1570s/harvest/witness_f36/c38_f36v_top.jpg` (via `harvest/witness_pairs/w36v_x1000_y120.jpg`), `c37_f36r_cipher.jpg` (crop x1200-2200, y1250-1720, the lower rows) and `c38_f37r_cipher.jpg` viewed at native resolution | **Gloss present over every cipher row viewed on all three leaves** (f.36r lower rows, f.36v top, f.37r both lines): small cursive letters above each sign, e.g. f.36v top "t o d ... s s", "o s l"; f.37r "n u ... s s". The gloss is the period decipherment of this very letter. |
| No gloss on f.117r and f.47r, by eye | `images/c118.jpg` (whole opening), `images/f117/f117_L04_s2.jpg`, `images/f47/f47_L05_s1.jpg` | No interlinear letters, no marginal key, facing f.116v is an address leaf; agrees with Premise (c). |
| (a) canonical series / catalogue | **Printed BnF inventory**: *Catalogue des manuscrits français. Ancien fonds*, t. II (Paris 1874; nos 3131-4835), full text from IA `p1cataloguegnr02bibluoft` (`_djvu.txt`, OCR prints the shelfmark as "5232"; neighbours Anc. 8740/8760 place it), entry ending on p. 160 | Read whole entry (items 1-107). **no.24: "Lettre, avec chiffre et déchiffrement, de « Lodovico Birago » au « duca di Nevers,... Da Saluzzo, li 5 aprile 1571 ». En italien. (Fol. 36.)"**; no.30: "Lettre, avec chiffre, ... Da Saluzzo, li 26 aprile 1571 ... (Fol. 47.)"; no.67: "avec chiffre" (Fol. 100); **no.77: "Lettre, avec chiffre, de « Lodovico Birago,... à monseigneur le duc de Nyvernois,... De Saluces, le xiiime mars 1572 ». (Fol. 117.)"**. The catalogue prints the decipherment's existence for no.24 only, and no plaintext for any item. Earlier files cited the BnF online notice (via Bourdeau's sweep), never this printed page. |
| (b) recipient's printed correspondence | Gomberville, *Les Mémoires de Monsieur le duc de Nevers* (1665), Gallica ContentSearch on Partie 1 `bpt6k6435941k` and Partie 2 `bpt6k9738856z`, terms **Birague, Carmagnole, Saluces** (the solver used 1571, Birago, Lodouico and month strings) | P1: Birague 29 hits -- all Carles/Charles de Birague (1574 restitution of Pignerol etc., PAG_109-150) or the chancellor René (PAG_340, 448, 503); Carmagnole 3 (Savoy's 1588 seizure, PAG_882-905); Saluces 46 (1574 restitution documents). P2: Birague 4 (Sacremore, chancellor), Carmagnole 3 (1588), Saluces 11. **No Lodovico/Ludovic Birago letter of 1571-72 in either part.** |
| (b) sender's printed correspondence | Google Books API `"Lodovico Birago" lettere` (51 vols; Mazzuchelli *Scrittori d'Italia* 1760; Aretino *Lettere* -- letters *to* Birago); IA full text `"Lodovico Birago" Nevers` (137 items; the printed catalogue, Savio *Saluzzo e i suoi vescovi* 1911, Gabotto's Piedmontese poet study, Promis/Manno-type notices) | No edition of Lodovico Birago's letters to Nevers located. Savio 1911 (IA `saluzzoeisuoives00saviuoft`) mentions Birago's receptions for Nevers and his death (28 Dec 1572); no letter text. |
| (c) documentary editions | *Lettres de Catherine de Médicis* t.4 (VERIFY-NEVBIR-90REST, 2 Oct, not repeated); IA full text `"Ludovic de Birague" Nevers 1572` (247 items: Monluc *Commentaires*, Registres de la Compagnie des pasteurs, Michaud-Poujoulat collections) and `"Birague" "Carmagnole" Nevers` (Du Bellay/Martin du Bellay mémoires, Lettres sur la cour) | Snippets name Ludovic de Birague's governorship; none prints or summarises the three letters. Not opened page by page (fts snippets only). |
| (d) holding archive | BnF: printed catalogue above; online notice (as quoted in NOTES.md Sources); Gallica images | The holding institution records a decipherment for no.24 only. Not contacted. |
| (e) full text IA / HathiTrust / Google Books | `tools/print_check.py . --phrases phrases.txt --only ia-global,gbooks,openalex,crossref` (8 phrases, `phrases.txt` written this session from S/C runs: intention de convenir, poursuivre le gouvernement, favoriser ces affaires, devant nous, Carmagnole Birague 1572, Ludovic de Birague Saluces, Lodovico Birago Saluzzo 1571, parlandone il signor) | "favoriser ces affaires", "Carmagnole Birague 1572", "Ludovic de Birague Saluces", "Lodovico Birago Saluzzo 1571": IA no hits; the generic phrases (intention de convenir, poursuivre le gouvernement, devant nous, parlandone il signor) hit only modern or unrelated texts. Google Books: 2 of 8 queries HTTP 503 ("favoriser ces affaires", "Carmagnole Birague 1572"), not retried; IA and OpenAlex answered both (no hits). HathiTrust full text: unreachable from the cloud (CLAUDE.md host table), not tried. Output not committed (scratch). |
| (f) solver repositories, cipher blogs | Fresh shallow clones 4 Oct: dbourdeau/cyphersolver a439937 (3 Oct), aaymeloglu/unsolved-ciphers d2800bb; grep 3252, birago, birague, btv1b9060232m. Tomokiyo local mirror `sources/cryptiana/web/` grep birag/3252/Ceppo | Bourdeau: only `research/gallica_sweep/bnf_candidates.txt` l.274 (candidate row, 3 items, no reading). Aymeloglu: DECODE catalogue rows for Lodovico Birago are fr.3619/3621/3623 (1591-92), none fr.3252. Tomokiyo: nevers.htm lists fr.3251 Birago letters and the Ceppo key from **fr.4702** ff.36-37 (Cesare Ceppo's letters); fr.3252 absent. The coincidence of folio numbers (fr.4702 ff.36-37 vs fr.3252 ff.36-37) was checked: the folder's images come from fr.3252's ark (manifest URLs), the leaf is addressed to Nevers with endorsement "5 aprile 1571", and the 1874 catalogue lists Ceppo's letters as a different series -- two different items. DECODE: not re-queried (no login; NEVBIR-3252's 2 Oct live query `x_c_holder LIKE 3252` = 0 records stands). |
| (g) scholarship | OpenAlex (keyed) "Lodovico Birago" (31), "Ludovico Birago Saluzzo" (10), "Birago Nevers Saluzzo" (2); CrossRef bibliographic query; HAL `"Birague" AND (Saluces OR Nevers)` (0); Semantic Scholar keyed query returned no data (one call, not retried) | Nothing on these letters. Titles of possible background value only: *Altri che hanno servito Francia* (CdlM 2023, doi 10.4000/cdlm.16642); "Le difficoltà politiche e finanziarie degli ultimi anni di dominio" (2015). Treccani DBI life: URL guess returned a generic page; HARVEST-D's 28 Sept finding (it cites fr.3252 among sources, no letter text) is not re-verified here. |
| JSTOR | No row existed for this folder. Appended 4 rows (2 per family) to `JSTOR-QUEUE.tsv`: (i) Birago/Birague + 1571/1572 dates + Saluzzo/Saluces + cipher keyword, twice; (ii) bare quoted phrases "intention de convenir" with Birague/Saluces, and "parlandone il signor" with Birago/Saluzzo, no cipher keyword | queued; does not block the classes below (CLAUDE.md verifier template). |

## 3. Classification

| item | class | prior plaintext | prior decipherment | evidence | confidence | key source |
|---|---|---|---|---|---|---|
| **no.24, f.36-37** | **N0** | yes -- on the leaf, in the clerk's interlinear hand (manuscript, not print) | **yes**: the period decipherment written over every cipher passage (seen by this verifier on all three leaves), recorded in print as "avec chiffre et déchiffrement" in the BnF *Catalogue des manuscrits français, Ancien fonds* t. II (1874), fr.3252 no.24 | the leaf itself + the 1874 printed catalogue | high | our decode: `published` (Tomokiyo's Ceppo-Nevers key, from fr.4702); the 10 C tokens: `period` (the clerk's gloss); text: known (on the leaf) |
| **no.77, f.117r** | **N3** (firm portion only: S 190 of 279 tokens, 68%; not a licensed reading -- judge FAIL) | none located | none located (catalogue says "avec chiffre" only; no gloss on the leaf) | search above: recipient's 1665 edition both parts, printed BnF catalogue, Tomokiyo, both solver repos, IA/GB/OpenAlex/CrossRef/HAL phrase and name searches | medium (JSTOR queued; Italian/Turin archives and the Charles IX / Catherine registers for Saluces in Mar 1572 not covered; HathiTrust full text unreachable) | `published` (Tomokiyo's 1572 Nevers-Birago key); the transcription corrections are ours, the key is not |
| **no.30, f.47r** | **N3** (firm portion only: S 6 of 771 tokens, 0.8%, six isolated letters o -- no readable text) | none located | none located (catalogue "avec chiffre" only; no gloss) | same search | medium; the class records a search result only -- there is no text to describe | `published` (Tomokiyo's Ceppo-Nevers key) |

**Safe sentences.**
- no.24: "Birago's letter of 5 April 1571 (BnF fr.3252 ff.36-37) was deciphered at the time: a clerk wrote the plaintext letter by letter
  over every cipher passage, and the BnF's 1874 printed catalogue records it as 'avec chiffre et déchiffrement'. We have read 10 of its
  947 cipher signs against that gloss; the rest of the gloss is not yet transcribed."
- no.77: "Under Tomokiyo's published 1572 key, about two thirds of the 279 cipher signs of Birago's letter of 13 March 1572 (BnF fr.3252
  f.117r) are read at grade S, giving French fragments about Carmagnola and an agreement to be favoured; the text still fails a language
  judge. No prior decipherment was located (search log in AUDIT.md, 4 Oct 2026)."
- no.30: "No decipherment of Birago's letter of 26 April 1571 (BnF fr.3252 f.47r) was located; we have no reading of it beyond six
  isolated letters."

**Unsafe sentences** (do not use): "first reading of Birago's 1572 letter" / "previously unread" (rule 10: N3, and the f.117r text fails the
judge); "we deciphered Birago's 5 April 1571 letter" (N0: the clerk did, in 1571, and our 10 C come from his gloss); "the f.47r letter is
read" (6 of 771 signs).

## 4. Postmortem

- **Found:** the printed BnF catalogue (1874, t. II, fr.3252 entry) had not been cited by any earlier pass; it independently confirms the
  N0 basis for no.24 ("avec chiffre et déchiffrement") and that nos.30, 67 and 77 carry no catalogued decipherment. Added to the search
  log here; NOTES.md is not edited (append-only AUDIT; a later NOTES pass may cite it).
- **Over-claim check:** NOTES.md, PROGRESS.tsv rows (f.117, f.36, f.47) and NEAR.md row searched for new/first/unread/unpublished wording
  about the text: none found ("unread" in NOTES refers to unread gloss signs, accurate). F36-READ already says the letter is a period
  decipherment. No correction needed.
- **Found, not applied (for the orchestrator):** (1) the PROGRESS.tsv f.36 row should carry `text: known` / key `period` for the C tokens
  when status.json is updated; (2) NEAR.md's birago row describes f.47r and f.117r but not that f.36 is N0 -- its value as a known-answer
  witness, not as a result, should be stated there if the row is next edited.
- Requests this session: be-api.us.archive.org 27 (8 via print_check + 19 fts snippet queries), archive.org 6 (advancedsearch 1,
  metadata 4, `_djvu.txt` 1), gallica.bnf.fr 6 (ContentSearch), www.googleapis.com 13 (8 via print_check, 2 of them HTTP 503; 5 direct),
  api.openalex.org 11, api.crossref.org 9, api.archives-ouvertes.fr 1, api.semanticscholar.org 1, www.treccani.it 1, github.com 2 clones.
  Subagents: 0.
- Queues: `SECOND-OPINIONS-QUEUE.tsv` row SO-BIR3252-117-47 (f.117r and f.47r, N3; prompt `second-opinions/PROMPT-chatgpt-f117-f47.md`);
  none for no.24 (N0). `JSTOR-QUEUE.tsv` 4 rows as above. PROGRESS.tsv audit-1 column set to x on the f.117, f.36 and f.47 rows from
  this section. `phrases.txt` added (the eight phrases of family (e)).

# AUDIT 3 (A3V-V2BIR, 4 Oct 2026): fr.3252 no.77 (f.117r) and no.30 (f.47r) -- second audits and claim scope

Verifier: worker A3V-V2BIR (account 3, for LANE-A3V), brief `.claude/briefs/runs/2026-10-04-acct3-a3v-wave3.md`. A session separate
from every solver of these letters and from A3V-VB3252 (AUDIT 2) and VERIFY-CEPPO-WP (AUDIT 1); I do not protect their conclusions.
Clock 03:34 UTC at start by `date -u`. Nothing decoded; key, ciphertext and readings untouched. AUDIT 1 and AUDIT 2 are untouched.

## 1. Extract (checked against the files, not copied from AUDIT 2)

- f.117r: `../nevers-birago-fr3251-1572/harvest/tx_decode/eye/apply/reading_f117_apply_tokens.tsv` (BIR-APPLY, 3 Oct; header "tokens
  279: H 0, C 0, S 190, M 63, I 0, U 26") -- counts agree with AUDIT 2. Re-rendered per token here (S lower case, M CAPITALS, U ·):
  `···mguiLam·uElgueNTURINOpseNua·aRde / LAENiNtentionDEconueniBauNS·· / pouRSuoiRLEgoueRne·entde··?pi·r / ceguiSestpeRso·eguiseReNdRoit /
  ·Susfacileets·inDeLE·eRtou·Es·es / sioNsdestRe·LusenEsREiLEsEeieeC / guec·deuaNtinuouSsu·SiNda·SeB / et·auoRisercesta·aiResiLeneETt /
  ·esoingetsiSuoussEmbLietantguiS / ReusiSE·QUELLOG·`. The M letters are mostly n, r, l, s and the word codes; the key writes u for v and
  g for q throughout (Tomokiyo's 1572 table), so "ceguisest" is "ce qui s'est".
- f.47r: S 6 of 771, all six the letter o (VERIFY-CEPPO-WP); M 751, U 13.

## 2. Search, extending AUDIT 2 (4 Oct 2026)

| family | searched by this verifier | result |
|---|---|---|
| (b) recipient's edition **by date** | Gomberville, *Mémoires de Monsieur le duc de Nevers* (1665), Gallica ContentSearch, P1 `bpt6k6435941k`, P2 `bpt6k9738856z`, quoted date strings: "1572", "Mars 1572", "13 Mars", "27 Mars", "29 Iuillet", "Avril 1571", "26 Avril", "5 Avril", plus Lodouic/Ludouic. Positive controls: quoted "Avril 1571" answers 6 hits in P1, quoted "1572" answers "Aoust 1572" (P1 PAG_209, P2 PAG_66) and "Septembre 1572" (P1 PAG_630) | **No dated piece of March 1572 or of 5/26 April 1571 in either part.** P1's "Avril 1571" hits (PAG_576-588) are the English marriage negotiation ("A Westminster le 9 Avril 1571"); the 1572 hits are August/September items and the St Bartholomew. Lodouic/Ludouic hits are Nevers himself and Count Louis of Nassau, never Lodovico Birago. Confirms AUDIT 2's name search by an independent route |
| (e) phrase search on S runs not used by AUDIT 2 | `tools/print_check.py` (scratch target, `--only ia-global,gbooks,openalex,crossref`) on "qui se rendroit", "et si vous semble", "ce qui s'est", "plus facile", "Birago Carmagnola Torino 1572"; the IA 502s and GB 503s retried once | Only unrelated texts (1790 *L'Amérique indépendante*, Foedera, Mazarinade bibliographies, 19th-c. Italian gazetteers for the Birago/Carmagnola query). The short French phrases are common and do not discriminate; that is a limit of the method on this text, logged, not a negative |
| (f) Tomokiyo | live `https://cryptiana.web.fc2.com/code/nevers.htm` fetched 4 Oct (HTTP 200) and diffed against the 1 Oct mirror on every Birago line: identical; whole mirror (`sources/cryptiana/`) grepped for 3252/Birago | **fr.3252 appears nowhere on Tomokiyo's pages**; nevers.htm lists only fr.3251's Birago letters; unsolved.htm l.227-228 lists the fr.3251 group as decipherable "by using keys reconstructed from already deciphered materials" (no text given) |
| (g) Italian/French Birago studies | OpenAlex (keyed): "Birague Saluces" (8), "Ludovico Birago" (84, top 8), "marchesato di Saluzzo 1572" (19), "Carmagnola 1572 Birago" (1), "Birago governatore Saluzzo" (5), "Birague gouverneur marquisat" (8); CrossRef bibliographic "Ludovic de Birague Saluces 1572", "Lodovico Birago marchesato Saluzzo Nevers" | Nothing on these letters. Closest: J. Guinand, "« Des gens de cervelle et de service ». Les capitaines italiens au service du roi de France au Piémont (1551-1559)", *Histoire, économie & société* 2021/4, doi 10.3917/hes.214.0046 -- abstract read (OpenAlex), period ends 1559, before these letters; the Cairn page answered 403, full text not read |
| JSTOR | AUDIT 2 queued 4 rows; its two family-(ii) rows AND a name with the phrase. Added 1 bare-phrase row: "favoriser ces affaires" (no name, no cipher keyword) | queued; does not block the class |

Requests (this section): gallica.bnf.fr 34 (ContentSearch, shared with AUDIT 13 of the sister folder), be-api.us.archive.org 10,
www.googleapis.com 10, api.openalex.org 14, api.crossref.org 9, cryptiana.web.fc2.com 2, shs.cairn.info 1 (403). Subagents 0.

## 3. Verdict and claim scope

| item | AUDIT 2 | this audit | key source | claim scope |
|---|---|---|---|---|
| no.77, f.117r | N3 | **N4 (raised)** | published (Tomokiyo 1572); transcription corrections ours | **counts as recovered passages** (fragmentary; judge FAIL) |
| no.30, f.47r | N3 | **N3 confirmed** | published (Tomokiyo Ceppo-Nevers) | **class without a reading -- not counted** |

**f.117r, why N4.** The principal print and project pages are now covered for this letter: the recipient's 1665 edition searched by
name (AUDIT 2) and by date (here) with answering controls; the BnF printed catalogue (1874, AUDIT 2: "avec chiffre" only); Tomokiyo's
pages live and mirrored (fr.3252 absent); both solver repositories (AUDIT 2: a Bourdeau candidate row, no reading); open indexes.
That is the same coverage on which AUDIT2-NEVBIR and AUDIT 12 of `../nevers-birago-fr3251-1572` gave N4 to the sister 1572 letters
read with the same key. Internal or unpublished work is not excluded (Bourdeau's sweep lists the volume as a candidate); Turin and Paris
archival copies and HathiTrust full text were not searched. Not N5.

**f.117r claim scope.** The firm letters read as French a reader can quote, though each phrase carries some M letters (in brackets)
and the word division is ours: "[in]tention [de] conueni[r]" (L02), "pou[rs]uoi[r] [le] goue[r]ne[m]ent" (L03), "ce gui [s]est"
(= ce qui s'est) and "e gui se [r]e[n]d[r]oit" (L04), "facile" (L05), "d'est[r]e" (L06), "deua[n]t [n]ous" (L07), "[f]auo[r]iser ces
[af]fai[r]es" (L08), "[et] si [u]ous s[e]mb[l]e ... tant gui[s]" (L09). S letters alone still give "tention", "conueni", "ce gui", "facile",
"auoriser ces", "tant gui". This is a fragmentary reading of passages, not of the whole letter, and it FAILs the language judge
(-1.224 vs real_p05 -0.899, AUDIT 2): it counts as a reading at N4 for the metric, and must always be described as fragments.

**f.47r claim scope.** Six isolated o's in 771 signs: no word, no phrase. The class is a search result about an unread letter; it is
not a reading and is not counted as a unique solve. I do not raise it: raising a novelty class on a text that does not exist would
only invite its misuse.

**Rule 7 for f.117r.** No fresh-session re-derivation of the f.117r reading is on file (A3V-RD7 did f.144r, A3V-RD168 f.168). BIR-APPLY's
`decode_key.py --check` on `decode_apply.json` covers all three jobs and was exit 0 in A3V-RD168's run today (RD7-2026-10-04-f168.md
step 2), so the committed f.117r reading is not stale; a fresh-instance re-derivation is still owed before any stage-9 move. Found, not
applied.

**Safe sentences.**
- f.117r: "Under Satoshi Tomokiyo's published 1572 Nevers-Birago key, about two thirds of the 279 cipher signs of Lodovico Birago's letter
  of 13 March 1572 (BnF fr.3252 f.117r) read at grade S, giving French fragments ('intention de convenir', 'poursuivre le gouvernement',
  'favoriser ces affaires'); the text still fails a language judge. No prior decipherment located (search log in AUDIT.md, 4 Oct 2026)."
- f.47r: unchanged from AUDIT 2.

**Unsafe sentences.** "We read Birago's letter of 13 March 1572" (fragments only, judge FAIL); "first decipherment" without "no prior
decipherment located"; any quotation of f.117r presented as a continuous sentence; any statement that f.47r is read or counts.

## 4. Postmortem

- AUDIT 2's family (ii) JSTOR rows were not bare (each ANDs a name); one bare row added.
- Over-claim check: NOTES.md, PROGRESS.tsv rows f.117/f.47 and NEAR.md row 30 grepped for new/first/unread/unpublished/solved/cracked:
  none about the text. PROGRESS audit-2 cells set to x for f.117 and f.47 from this section, with the claim scope in the note.
- SECOND-OPINIONS-QUEUE: row SO-BIR3252-117-47 already covers both items (AUDIT 2); no new row.

## Depth (DEPTH-REGRADE, 4 Oct 2026)

Verifier DEPTH-REGRADE (account 3, session_015eezFKYThEoRKoeamyhxSD), rule 4a / verifier step 3a; nothing decoded or changed. % = cipher tokens graded H/C/S (clear text excluded; counts as the cited reading file or audit gives them, nulls excluded where the file marks them); when evidence for a level is not on file the level below is given.
- **BnF fr.3252 f.117r (no.77): Lodovico Birago to the duc de Nevers, 13 March 1572**: **D1** (Non-decrypted; outward "fragments read"), 68.1% (S 190 of 279). Check: published key; S-only stretches at most about a word ('tention', 'facile', 'auoriser ces'), no clause above AD; judge FAIL. Class without a reading: not counted as a unique solve.

## Propagation note (D2-B117KAPC, 5 Oct 2026; solver-side, not a verifier verdict)
f.117r grades moved after this audit: S 190 / M 63 -> **S 217 / M 36** (U 26), reading text unchanged. The printed 1572 key was
licensed on la/recon_f117_3r.tsv at the measured post-look-alike error (no.87 known answer, 0.126 pooled, bracket 0.183; power 18/20
and 16/20, rank 1/201 on 5/5 seeds; harvest/f117/la/PREREG-KAPC.md), and 27 M tokens where top-1 and the look-alike third reader
agree moved to S under the BIR-APPLY rule (NOTES.md "D2-B117KAPC"; harvest/f117/la/kapc/). Longest S-only stretch 17 letters, no
clause; judge FAIL unchanged. The safe sentence above still holds; depth and N-class are left to a verifier. SECOND-OPINIONS-QUEUE row
SO-BIR3252-117-47 checked: its prompt quotes no grade counts and values are unchanged, so it needs no edit.

## Propagation note (D2-B117M, 5 Oct 2026; solver-side, not a verifier verdict)
f.117r grades moved again: S 217 / M 36 -> **S 224 / M 29** (U 26), reading text unchanged. One value-blind window read
(harvest/f117/la/m16/) of the 16 plain-M tiles agreed with top-1 on 7 firm answers (S under the BIR-APPLY rule); on the 3 tiles where
an earlier firm third read disagreed with top-1 it sided with that third read 3/3 (L02.27 T18, L06.18 T90, L06.26 T90), so those stay
M pending a value change by the owner's sorter. Longest S-only stretch 23 letters ('nintentiondeconuenibaun', L02.4-26), below the
~42-letter AD figure, no clause above AD; judge FAIL unchanged. T88=q FAIL on no.86 (HYPOTHESES.md). Depth and N-class left to a
verifier; SO-BIR3252-117-47 quotes no grade counts, no edit needed.
