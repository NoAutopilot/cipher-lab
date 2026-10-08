# AUDIT: WVO 11008 (Orange as "George Certain" to Lodewijk as "Lambert Certain", Keulen, 12 Aug 1572)

Verifier KHF2-VERIFIER (account ytbiz, for acct3-orchestrator), 7 Oct 2026 20:28-20:4x UTC by `date -u`; brief
`.claude/briefs/runs/2026-10-07-ytbiz-khf2-verifier.md`. A session separate from the solver (KH2-D) and the
check-solved worker (KHF-2); it did not decode and does not protect their conclusions.

Claim under audit (NOTES.md "Reading under the held key"): five numeral runs in WVO 11008 read under the printed 1572
Orange-Nassau table as "le duc de holstein", "ermuyden" (Arnemuiden) and "ulgssinghen" (= vlissinghen, one code off);
54 tokens H39 M15; key-permutation control passed (4-gram -1.435 vs shuffle p95 -1.576, 6/1000); fr16 judge FAIL at N=39.

## Verdict

| item | N-class | key | prior plaintext | prior decipherment | depth |
|---|---|---|---|---|---|
| WVO 11008, runs 1-5 (three names read: Duke of Holstein, Arnemuiden, Vlissingen) | **N3** | `period` (the 1572 Orange-Nassau table printed by Nepveu tot Ameyde in the *Algemeene Konst- en Letterbode*, rebuilt by this project from the print: `../jan-van-nassau-1572-75/key_1572.tsv`) | no -- the letter is unprinted (WVO gives no edition; not in Groen, Gachard or Kervyn as searched below) | no | **D2**, about 80% |

**Depth superseded (AUDIT 2, 8 Oct 2026): D2 lowered to D1 under the 8 Oct depth bar; the safe sentence below is replaced by AUDIT 2's. N3 and key `period` stand.**

Text: not known in print (`text: unknown`). The key is a period key; this project rebuilt it from a printed table
and matched it to this letter (the matching, not the key, is ours).

**Safe sentence:** "Under the printed 1572 Orange-Nassau cipher table, the five numeral runs in William of Orange's
letter of 12 August 1572 to Louis of Nassau (KHA A 11/XI 15, WVO 11008) read 'le duc de holstein', 'ermuyden'
(Arnemuiden) and, with one code off, 'vlissinghen'; partially deciphered (about 80% of the cipher tokens), and no
prior decipherment or printing of this letter located after the search logged in AUDIT.md."

**Unsafe sentences:** "first decipherment", "previously unread", "newly deciphered letter of William of Orange",
"deciphered" (without the qualifier; two runs are damaged or unread), "key identified" for a key we had to match
rather than one the letter names, and any sentence about what the Duke of Holstein did that rests on the clear-text
context ("a faict charge pour ... 2000 escus") beyond the transcription as it stands.

## 1. Extract

- Date/place: Keulen (Cologne), 12 Aug 1572. Sender: William of Orange under the merchant cover "George Certain".
  Recipient: Louis of Nassau as "Lambert Certain", addressed "estant pour le present a Tournay". Holding: Koninklijk
  Huisarchief, A 11/XI 15, original; image in the WVO PDF 11008 (2 images).
- Ciphertext (`ciphertext.txt`, 54 numerals, five runs) inside French clear text. Reading (`reading.txt`):
  run 1 "cd[120]", run 2 "leducdeholstein", run 3 "cme" (damaged), run 4 "ermuyden", run 5 "ulgssinghen".
- Distinctive phrases: incipit "J'ay recheu ce jourduy les deux vostres du 5 et 7 du courant, vous remerchiant";
  after run 2 "lequel a faict charge pour ... 2000 escus"; "le Sr Dominique est venu"; "Arnoult est"; "Or pour".
- Solver/check-solved searches (NOTES.md): Groen *Archives* 1re série whole edition incl. Supplément via Huygens
  retroboeken full-text; Japikse (ends 1561); IA fts; Google Books API; OpenAlex (one title); nine web searches and
  three blog site searches; Bourdeau and Aymeloglu clones (grep); DECODE dumps (24 Sept) and Aymeloglu's DECODE CSV.
  Not covered by them: Gachard, Kervyn, Spanish-side intercepts, the Waanders 2022 ToC, cipher-table literature.

Re-checked here: `python3 decode.py --check` exits 0 (reading not stale, rule 7). Crop `images/p1_L02_s1.jpg` viewed:
"33:15:12:60:9:12:15:24:42:33:54:57:15:27:39:11:14:17: lequel a fa..." -- run 2 and the start of its clear-text
continuation as transcribed.

## 2. Search log (this session, 7 Oct 2026)

| family | what was searched | result |
|---|---|---|
| (a) canonical series | Groen *Archives* 1re série: not re-run in full (KHF-2's whole-edition retroboeken search stands); IA fts `"Lambert Certain" holstein` returns Groen III among 52 hits, the same letters KHF-2 opened (other letters) | absent |
| (b) sender's printed correspondence | Gachard, *Correspondance de Guillaume le Taciturne*, IA djvu full text of vols III (`correspondancede03will`), IV (`correspondancede04will`) and VI (`correspondancede06will`), grep Holstein/Holsteyn/Ermuyden/Armuyden/"Lambert Certain"/"George Certain"/12 Aug 1572 | absent; III has "Armuyden" (another letter) and "pays de Holsteyn" (another letter) |
| (b') Spanish side / intercepts | Gachard, *Correspondance de Philippe II* vol. II (`correspondancede02phil`, covers 1572), same grep plus Flessingue/"Certain" | absent. Context only: Alba to the King, Brussels 21 Aug 1572 (no. 1152): "appris que le duc de Holstein, avec 2,600 chevaux et 2,000 arquebusiers" was coming to join him; later Holstein's arrival at the camp. "Armuyden" in 1573 letters. |
| (c) documentary editions / period studies | Kervyn de Lettenhove, *Les Huguenots et les Gueux* vols II, III (IA djvu full text) | absent. II: the cover-name list ("le prince d'Orange, Georges Certain ; Louis de Nassau, Lambert Certain"), citing Arch. Nat. Paris K.1529. III: Orange's own Sept 1572 letter "pour charger le duc d'Holstein". Neither prints 11008. *Relations politiques des Pays-Bas et de l'Angleterre* not found on IA by title search -- not searched. |
| (c') Waanders 2022 *Willem van Oranje in brieven. De Opstand in 1572* | web search for ToC (standard); Google Books record | ToC not reachable; publisher blurb: forty letters of 1572 "aan bewindslieden van de Nederlandse provincies en gewesten" (to provincial authorities), so a letter to Louis is unlikely to be among them -- **unreachable**, not a negative |
| (d) holding archive / project pages | WVO record 11008 (as read by KH2-D/KHF-2; not re-fetched) | no edition line |
| (e) full text: IA, Google Books | IA fts (global) `"duc de holstein" ermuyden` 0, `"George Certain" ermuyden` 0, `"Lambert Certain" holstein` 52 (Groen, Spectator 1865, other); `"ulgssinghen"` and the two-phrase query returned no JSON (unreachable). Google Books (key, country=US): `"duc de holstein" "2000 escus"` 21 (1665 *Estat de l'Empire*, 1846 CRH: irrelevant), `"Lambert Certain" Holstein 1572` 37 irrelevant, `Ermuyden 1572 Oranje` 4 irrelevant, `"Ermuyden" Vlissinghen` 4 (1599 *Landtspiegel*, 1636/1700 almanacs, Van Haecht chronicle "Ermuyden wordt overgelevert in handen van den prinsche van Oraengien"), `"Lambert Certain" cijfer` 92 (1860s polemics naming the cover name; no cipher text), `"Nepveu tot Ameyde" cijfer Oranje` 0; `"George Certain" Holstein` and `"Willem van Oranje in brieven" Lodewijk Certain` HTTP error (unreachable) | absent |
| (f) solver repositories, blogs | not re-cloned (KHF-2 cloned both at named commits 7 Oct 2026); web search `"duc de Holstein" Orange Louis de Nassau août 1572 lettre chiffre "George Certain"` | no decipherment of 11008 |
| (g) scholarship | OpenAlex (key): "Orange Nassau cipher 1572" 9, "Nepveu tot Ameyde cijfer" 0, "Willem van Oranje geheimschrift" 8 (incl. De Leeuw's review/ *Cryptology and statecraft in the Dutch Republic*), "Lodewijk van Nassau cipher letters" 4, "Willem van Oranje in brieven 1572" 124 -- titles read, none is about this letter; De Leeuw's book itself not read (title hit only). Semantic Scholar, CORE, Persée, HAL: not run (cap). JSTOR: four rows queued (below) | no hit about this letter |

JSTOR-QUEUE.tsv rows added (both families, rule 10 template step 2g): (i) `"Lambert Certain" AND 1572 AND (chiffre OR
cipher OR cijfer)`, `"duc de Holstein" AND Orange AND 1572 AND chiffre`; (ii) `"J'ay recheu ce jourduy les deux
vostres"`, `"Lambert Certain" "Tournay"`. A queued row does not block N3.

Requests this session: archive.org 4 (advancedsearch) + 6 (djvu downloads); be-api.us.archive.org 5; googleapis.com
books 12; api.openalex.org 5; web search 2. No 403/429; two IA fts calls and three Google Books calls returned
errors, logged above as unreachable.

## 3. Classification reasoning

N3: no prior plaintext or decipherment of this letter's cipher runs located after the logged search. Not N4: the
Waanders 2022 ToC could not be reached, Kervyn's *Relations politiques*, De Leeuw (2000) and the Semantic Scholar /
CORE / Persée / HAL pass were not covered, and DECODE was checked only from dumps. Not N2: no plaintext known
elsewhere (the letter's clear text is unprinted too). Evidence quality: the letter is unprinted per WVO; the solver's
transcription of the runs is two blind passes plus reconciliation (89.5% agreement), damaged at run 3.

Plausibility checks (corroboration, not proof): in Aug 1572 Duke Adolf of Holstein was bringing horse to Alba
(Gachard, *Corr. Philippe II* II, no. 1152, 21 Aug 1572), and Orange himself wrote in Sept 1572 of charging "le duc
d'Holstein" (Kervyn, *Huguenots et Gueux* III p.84) -- so the name is topical in this exact fortnight; "Ermuyden"
is an attested period spelling of Arnemuiden (1599 *Landtspiegel*, Van Haecht chronicle), not an invented one, and
Arnemuiden/Vlissingen were live theatres in summer 1572.

## 3a. Depth (rule 4a)

Counted from `ciphertext.tsv`, the table and the grades in NOTES.md: 54 tokens = 14 table nulls + 40 non-null
cipher tokens (39 table letters + code 120). H = 32 letters (run 2 all 15; run 4 seven of eight, pos 5 M; run 5 ten
of eleven, pos 3 M). **depth_pct = 32/40 = 80%.** Unread/uncertain non-null tokens: 8 -- 1 possible code group
(120, outside the table) and 7 other (run 1 c d, run 3 c m e: damaged or ambiguous; run 4 pos 5; run 5 pos 3).

- Not D1: the D1 exclusions are both met -- the letter key is a non-statistical external check (a printed period
  table), the 15-letter H stretch "le duc de holstein" exceeds any authentication distance for a fixed table with
  one counted liberty, and code values read sensibly in several runs (15=e, 39=n, 12=d, 54=s across runs 2, 4, 5).
- D2: met. True, specific sentence (verifier's): **"In his letter of 12 August 1572 from Cologne the prince wrote in
  cipher the name of the Duke of Holstein, immediately before the clear words 'lequel a faict charge', and the
  Zeeland place-names Arnemuiden ('Ermuyden') and Vlissingen."**
- Not D3: 80% is exactly at the floor, and the unread residue is mostly damaged or uncertain letters (7 of 8), not
  names/code groups as D3 requires; the table's fit to this letter rests on the key-permutation control (p about
  0.006), and the known-plaintext check on sister letter 5194 (Remaining gaps) has not been run.
- Check used: rule 4a definitions and research/DECIPHERMENT-STANDARDS-2026-10-04.md items 3 and 5; outward words
  "partially deciphered (about 80% of the cipher tokens)".

The judge FAIL (fr16, N=39) is consistent with a names-only string and is not used either way; the matched
key-permutation control is the statistic that carries the fit.

## 4. Postmortem and corrections

No over-claim found in outward-facing wording: NOTES.md uses no novelty word and says "No novelty claim (rule 10)".
One sentence corrected in NOTES.md (Premise check (b)): "nobody else has run it on this text" was a novelty-shaped
assertion from a two-repository grep; now "no other application of it to this text was located (searched as
logged ...)". For the parent: NOTES.md line 1 still reads `open`; with a period-key reading graded H and gaps left,
`partial` is the rule-5 word -- the parent's call when it updates status.json (`key: period`, `text: unknown`,
`depth: D2`, `depth_pct: 80`, the D2 sentence above). Missing named next steps for N4: Waanders ToC (owner's desk or
a library catalogue), Semantic Scholar/CORE/Persée/HAL pass, De Leeuw 2000 index, the JSTOR rows.

## 5. Second opinion

N3 assigned: `SECOND-OPINIONS-QUEUE.tsv` row `SO-WVO11008-CERTAIN` appended in this session, prompt
`second-opinions/PROMPT-chatgpt.md`.

## AUDIT 2 (second adversarial, AUD2-WVO11008)

Verifier AUD2-WVO11008 (account 4, for the account-3 orchestrator; session_01PCMBpaJ12Kf13gJtaedSbk), 8 Oct 2026
02:37-02:47 UTC by `date -u`; brief `.claude/briefs/runs/2026-10-08-acct3-scout-jobs.md` section AUD2-WVO11008.
Separate from KH2-D, KHF-2 and KHF2-VERIFIER; did not decode.

### Verdict

| item | N-class | key | prior plaintext | prior decipherment | depth |
|---|---|---|---|---|---|
| WVO 11008, runs 1-5 | **N3** (kept) | `period` (printed 1572 Orange-Nassau table, `../jan-van-nassau-1572-75/key_1572.tsv`) | no | no | **D1** (lowered from D2), depth_pct 80 (32 of 40 non-null cipher tokens H) |

**Safe sentence:** "Under the printed 1572 Orange-Nassau cipher table, the numeral runs in William of Orange's letter of
12 August 1572 to Louis of Nassau (KHA A 11/XI 15, WVO 11008) give fragments: 'le duc de holstein', 'ermuyden'
(Arnemuiden) and, with one code off, 'vlissinghen'; no prior decipherment or printing of this letter located after
the searches logged in AUDIT.md."

**Unsafe sentences:** "partially deciphered (about 80%)" (AUDIT 1's wording; D1's outward word is "fragments
read"); "first decipherment", "previously unread", "newly deciphered"; "deciphered"; "key identified"; any claim
about what the Duke of Holstein did resting on the clear-text context.

### 1. Rule 7, eye-check, control

- `python3 decode.py --check` -> `OK`, exit 0. `python3 decode.py` re-run: `control.tsv` and `reading.txt`
  regenerate byte-identically (git diff empty).
- Control (rule 3, under `key_1572.tsv`, 1000 seeded key permutations of the 23 letter values, nulls fixed):
  **4-gram -1.435 vs shuffle p95 -1.576, mean -1.813, 6/1000 shuffles >= real** -- same as on file.
- Eye-check on the crops on disk (all five runs are covered, no fetch needed): `p1_L02_s2.jpg` run 1 "10:9:12:120:"
  after "rappeler ses ..."; `p1_L02_s1.jpg` run 2 "...15:24:42:33:54:57:15:27:39:11:14:17:" then "lequel a fa[ict]";
  `p1_L07_s1.jpg` run 4 "15:51:36:60:69:12:15:39:40:" after the lozenge mark and "et s'est"; `p1_L07_s2.jpg` run 3
  tail "...36:3?:15:25:37:40:" before "le Sr Dominique", run 4 tail "39:40:44:52:31@", run 5
  "60:33:21:54:54:27:39:21:24:15:39:43" after "Arnoult est". All agree with `ciphertext.tsv`; run 3's fourth number
  stays ambiguous (36/38) and its start damaged, as already graded M.

### 2. Search log (this session, 8 Oct 2026)

| family | what was searched | result |
|---|---|---|
| Gachard, *Corr. de Guillaume le Taciturne* (vols I, II, V; AUDIT 1 did III, IV, VI) | IA djvu full text `correspondancede01will`, `02will`, `05will`, grep Holste/Ermuyd/Armuyd/Arnemuy/"Lambert Certain"/"George Certain"/jourduy/"aoust 1572" | absent (I: "duc de Holstein" cavalry, 1557; II: "Armuyden", 6 Mar 1567 -- other letters) |
| Groen *Archives* 1re série incl. Supplément, Huygens retroboeken phrase search | "Holsteyn" (25 hits; none in série 1 III, IV or Supplément), "faict charge" (139, the 1552-66 volumes lead), "Tournay", "Ermue" (0); KHF-2's whole-edition searches stand | absent |
| De Leeuw 2000, *Cryptology and statecraft in the Dutch Republic* | full thesis PDF from pure.uva.nl (UvA DARE open access), pdftotext, grep 1572/Certain/Lodewijk/Holstein/Nepveu | absent: p.155 and note lviii name only Orange to Jan, Malines 21 Sept 1572 (Groen III 501-511, solved by Van der Kemp, *Konst- en Letterbode* 1836); no WVO 11008, no Certain letter |
| Waanders 2022, *Willem van Oranje in brieven. De Opstand in 1572* | web search for the ToC (standard) | **unreachable** -- the ToC is not online (neerlandistiek review, DARE chapter records only); not a negative |
| `tools/print_check.py` (new `phrases.txt`, `sources.tsv`) | 6 phrases x Gachard Guillaume III, IV, Gachard Philippe II vol. II, IA global, Google Books, OpenAlex, CrossRef | no hits on any phrase in the editions or IA global; gbooks hits are noise ("le duc de holstein ..." -> 1787 *Art de vérifier les dates*; "Lambert Certain nostre bon amy" -> *Cabinet historique* 1882, snippet "Bonamy ... Lambert, libraire ... certain", unrelated); one IA-global query HTTP 502 |
| Google Books (key, country=US), direct | `"Lambert Certain" "bon amy et compere"`, `"Lambert Certain"`, `"George Certain" Holstein` | the cover names in Kervyn *Huguenots et Gueux* 1884, Fruin/Willem van Oranje 1891, *Abfall der Niederlande* 1871 (cover-name and metal-name lists only); no cipher text of 11008 |
| OpenAlex (key) | via print_check: 6 phrases 0; "Lodewijk van Nassau 1572 brieven" 46 works, top titles unrelated | absent |
| Semantic Scholar (key) | 4 queries: 2 answered ("Lodewijk van Nassau 1572 letters cipher": Van Herwerden 1935 review; De Leeuw search: the 2000 thesis and later papers); 2 plus print_check's s2 pass HTTP 429 | partly unreachable (429); nothing about this letter |
| CORE (key) | `"Lambert Certain"`, `"George Certain"` (no JSON total returned), `"duc de Holstein" 1572 Orange` (291k noise, Orange County) | absent / partly unreachable |
| HAL | `"Lambert Certain"`, `"George Certain"`, `Orange Nassau chiffre 1572` | 0, 0, 0 |
| Persée | not run (cap); French-language Orange-Nassau cipher literature covered by HAL and OpenAlex only | not searched |
| JSTOR | rows 321-324 (AUDIT 1) cover families (i) and (ii); one family-(ii) row added for the decoded phrase `"le duc de Holstein lequel a faict charge"` | queued; never blocks |

Requests: archive.org 3 advancedsearch + 3 djvu; be-api 6 and googleapis 6 (print_check) + 3 direct Google Books;
api.openalex.org 7; api.semanticscholar.org 5 (3 x 429); api.core.ac.uk 3; api.archives-ouvertes.fr 3;
resources.huygens.knaw.nl 7; dare.uva.nl 1 + pure.uva.nl 1; api.crossref.org 2; web search 2. All >= 1.5 s apart
except the single calls; no retry loops.

### 3. Class

N3 kept. Not N4: the Waanders 2022 volume (the one edition devoted to Orange's 1572 letters) is unread, and the
Semantic Scholar pass and Persée were incomplete. Not lowered: no prior plaintext or decipherment of 11008 located in
Groen (incl. Supplément), Gachard (all six Guillaume volumes, Philippe II vol. II), Kervyn, De Leeuw, IA, Google
Books, OpenAlex, HAL or CORE. Key: `period`. Text: `unknown`.

### 3a. Depth (rule 4a, 8 Oct 2026 depth bar) -- lowered D2 -> D1

`python3 depth_ad.py` (this folder):

```
longest H stretch: 15 letters (leducdeholstein)
H(K) = log2(23!) + 2 liberties = 83.5 bits; fr16 alphabet 22, held-out 4-gram entropy 3.059 bits/letter
R=1.40 (fr16 4-gram measured): unicity 59.6, AD 89.4 letters -> clause not met
R=3.20 (textbook French): unicity 26.1, AD 39.1 letters -> clause not met
R=4.46 (ceiling log2(V)): unicity 18.7, AD 28.1 letters -> clause not met
```

- **Cipher clause: not met.** The design is a 23-letter simple substitution with nulls; under the bar the printed
  period table, not fitted to this letter, does not shrink H(K) to the liberties, so H(K) = log2 23! plus the two
  counted liberties. The longest H stretch is 15 letters, and the runs are separated by clear text, so no stretch
  is longer. The AD is at least 28 letters even with every bit of redundancy counted (the most generous R possible),
  so the result does not depend on the choice of R.
- **Code clause: not met.** The only non-table value is 120 (run 1, one context, unread). Letter values recurring
  across runs (15=e, 39=n, 12=d, 54=s) are cipher letters, not code values. Names alone meet neither clause.
- **External check:** the printed table is a D3/D4 element under the bar and does not stand in for the clause at D2.
  So AUDIT 1's argument ("the letter key is a non-statistical external check") does not carry D2.
- The key-permutation control (p about 0.006) shows the table fits; it does not create a clause.
- **D1**, outward words "fragments read". depth_pct 80 (32/40 non-null cipher tokens H; unread 8: 1 code group
  (120), 7 other). No depth sentence (D1). Check used: `depth_ad.py` AD vs longest stretch, under the bar in
  `.claude/briefs/runs/2026-10-08-acct3-scout-jobs.md`.

### 4. Postmortem and corrections

AUDIT 1 over-claimed depth: it took the period table as the D1 exclusion and counted letter values recurring in
several runs as code values reading in two contexts. The bar rules out both. AUDIT 1's verdict now carries a
"superseded" line; its safe sentence ("partially deciphered (about 80% ...)") is replaced by the one above. NOTES.md
uses no depth word, so no correction is needed there. The status.json row and NOTES line 1 (`open` -> `partial`) are
the parent's (brief). SO-WVO11008-CERTAIN: the prompt quotes no count, class or depth, so no correction is needed
(rule 10).
