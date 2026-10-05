# AUDIT: antt-fcc-costacabral-1865 (ANTT PT/TT/FCC/001/0021/00026, m0112-m0114)

Verifier V6-COSTA (LANE V6, session_013MqSTzas6g4hw2dKDjhVpH), 25 Sept 2026, 16:55-17:10 UTC (`date -u`). Adversarial
audit under CLAUDE.md rule 10. I did not solve this target (LANE R6 P4, P5 did). No decoding: key.tsv, ciphertext.tsv,
reading.txt left untouched. Where I read the leaf below, that is to settle what the leaf is, not to re-decode it.

Claim under audit (R6 P5, ROOM 16:41 UTC and NOTES.md): "self-glossed syllable/word nomenclator draft; reading.txt
decodes 84 tokens at C 63, M 19, U 2 from key.tsv (52 rows, 3 codes with two values unresolved); status found-solved;
key source `ours`."

## 1. Verdict

| Item | Class | key | Prior plaintext | Prior decipherment | Evidence | Confidence |
|---|---|---|---|---|---|---|
| Cipher draft, m0113 right half + m0114 (84 code tokens, 16 lines transcribed) | **N0** | **period** | yes, in manuscript: the encipherer's own plaintext, syllable by syllable, written above every code on the leaf; not found in print (section 4) | yes: the same gloss is the plain text of this very item, set out code by code by the clerk who enciphered it | strong: the images on disk show a syllable over each number on every line (m0113 R1-R12, m0114 R1-R5) | high on N0; high on `period` |
| Cover letter, m0112 + m0113 left half (Caetano de Magalhães to "Meo Caro Conde", Secretaria, 8 July 1865) | not a cipher; no class | n/a | plain text on the leaf; this letter not found in print; its subject (Pius IX's letter of 3 Aug 1864, said to have been lost, answered 6 July 1865) is printed in the 1887 Livro Branco (section 4) | n/a | read off the image | n/a |

Key source: `period`. The key was rebuilt by us (R6 P5) from the period clerk's own code-over-syllable worksheet on the
leaf, i.e. from a cipher document of the time; nothing was recovered cryptanalytically and no modern key was used. The
solver's `ours` is corrected (section 6). Text: known on the leaf (not in print as far as searched), so `text: known`
in the rule-10 sense of "plaintext already in print" does **not** apply; the parent should record `key: period`,
`text: on the leaf, no print located`.

**Safe sentence:** "ANTT FCC/001/0021/00026 carries an 1865 syllabic nomenclator encipherment worksheet with the
clerk's own Portuguese plaintext written over every code; we rebuilt a 52-row partial key from it (grade C 63, M 19,
U 2 of 84 tokens). No printing of the letter or its text was located (search log in AUDIT.md), class N0."

**Unsafe sentence:** "We deciphered / solved an unpublished Portuguese cipher of 1865" (nothing was deciphered: the
plaintext was on the leaf; "unpublished" is a novelty word rule 10 does not allow at N0).

## 2. What is on the leaf (task 1, from the three images on disk)

- **m0112** (single page) and the **left half of m0113** (a two-page spread) are one plain letter: "Reservadissimo",
  "1865", "Meo Caro Conde"; the Conde d'Ávila, Foreign Minister, being ill, the writer asks the Conde to obtain with
  the greatest discretion, and without the Pontifical government suspecting why, a copy of the Holy Father's letter,
  whose answer goes with the official dispatch and which the Duque de Loulé kept when he was minister; signed
  "Secretaria, 8 Julho 1865, Caetano de Magalhães", "teu am.º obrig.mo e contemporaneo dos bellos tempos de Coimbra".
- **Right half of m0113 and m0114**: the cipher draft. On every line a syllable or short word is written above each
  number ("con-fi-den-ci-ar / 99-629-737-20-428", etc.). This is an **encipherment worksheet**, the plaintext first and
  the codes set under it: the plaintext of this very item is on the leaf, as in the N0 precedents
  (clair1067-brienne-poland-1646: interlinear decipherment on the leaf; rah-canada-1869: clear text on the item).
- **Does m0112 carry the same text in clear? No.** The cover letter is about the papal letter; the cipher gloss is a
  different message. Read as running Portuguese (a verifier's reading for classification only, not a key change) the
  gloss is continuous, not "scattered fragments" as NOTES.md said: "confidenciar / el Rei deseja convidar [o] Rei de
  [I]talia para padrinho do princi[pe] ou prince[sa] que se espera. Para [o] Papa tol[er]ar ca... escre... a este
  respeito ao Papa logo que souber alguma ... digam[-o] pelo tele[grapho] ...". Its subject is King Luís's wish to
  invite the King of Italy (Victor Emmanuel II, the Queen's father) as godfather of the child then expected (Infante
  Afonso, born 31 July 1865), and the Pope's tolerance of it -- a Holy See matter, so a natural companion to the cover
  letter to Portugal's envoy in Rome, but not the same text. (Web search: Afonso's godparents were in the end Napoleon
  III and Isabel II of Spain, per the Portuguese and English Wikipedia articles; not verified in a primary source.)
- **Recipient identified.** "Conde" is António Bernardo da Costa Cabral, Conde de Thomar, owner of the fonds and
  Portugal's envoy to the Holy See in 1865: the 1887 Livro Branco (section 4) cites "uma nota do sr. conde de Thomar,
  com data de 11 de agosto [1865]" to the Holy See and a despatch of the Conde d'Ávila of 10 July 1865 "ao conde de
  Thomar, Antonio ..." about the same papal letter. Costa Cabral studied at Coimbra, which fits "bellos tempos de
  Coimbra". NOTES.md named no recipient.
- **m0114 fifth line** is not wholly illegible, as NOTES.md says: syllables stand over "68?-1053-...-20-260" and read
  approximately "gra-pho-em-ci-fra" ("[telegra]pho em cifra"). Left for a solver pass; not transcribed here.

## 3. Status word (task 4)

`solved`, not `found-solved`. In this repository `found-solved` means someone else had already solved or printed the
item (README "Found-solved is not garbage": F0-F2 are all defined by a **print** or a specialist edition); a check-solved
verdict of found-solved records "who did not know". Here nothing is in print (section 4). The precedent for a leaf that
carries its own plaintext is clair1067-brienne-poland-1646 (N0, status `solved`) and rah-canada-1869 (N0, `solved`):
the reading exists and is reproducible; the class N0 already records that the plaintext was on the leaf, so the status
word does not have to say it twice. NOTES.md's first line is changed to `solved`.

## 4. Search log (task 2), 25 Sept 2026

| Family | Searched / unreachable | What | Result |
|---|---|---|---|
| (a) canonical series: Portuguese Livro Branco, "Negocios externos. Documentos apresentados ás Cortes" | searched | IA advancedsearch (title, 1860-1890, 24 volumes listed); full _djvu.txt of the four 1887 volumes (negociosexterno00portgoog, 02portgoog, 03portgoog, 05estrgoog) grepped for Thomar, 1865, Magalhães, padrinho, 8/10 de julho; Google Books eedAAQAAMAAJ ("negociações com a Santa Sé", 1887) by snippet | **context printed, item not:** negociosexterno00portgoog (1887, Santa Sé) prints the Pope's letter of 3 Aug 1864 "que se extraviara", the reply of 6 July 1865 and Thomar's note of 11 Aug 1865; eedAAQAAMAAJ snippet: Ávila's despatch "de 10 de julho do mesmo anno ao conde de Thomar". No Magalhães letter, no godfather matter, no cipher, no "padrinho" in the volume |
| (b) sender/recipient correspondence (Costa Cabral / Conde de Thomar; Caetano de Magalhães; Conde d'Ávila) | searched | Google Books: `"Conde de Thomar" correspondencia Roma 1865`, `"Conde de Thomar" 1865 "Santa Sé" padrinho`, `"Caetano de Magalhães" 1865 Secretaria "Negocios Estrangeiros"`, `"Caetano de Magalhães" "conde de Thomar"`, `"Conde d'Avila" 1865 "Conde de Thomar" Papa`; IA fts `"Costa Cabral" "Caetano de Magalhães"`, `"conde de Thomar" padrinho "rei de Italia"` | only the Livro Branco hit above; fts hits are directories and unrelated biography. No printed Costa Cabral correspondence edition located |
| (c) documentary / period sources on the subject | searched | Google Books `"Rei de Italia" padrinho 1865 infante Affonso baptismo`, `"Victor Manuel" padrinho "D. Affonso" 1865`, `"Duque do Porto" 1865 padrinho "Victor Emmanuel"`, `"Pio IX" padrinho infante 1865 Portugal "Rei de Italia"`, `"padrinho" "Napoleão III" "infante D. Affonso" 1865 "Victor Manuel"`; IA fts `"baptismo" "infante D. Affonso" 1865 padrinho` | Jornal de jurisprudencia 1865 prints the birth notice of D. Affonso naming Victor Manuel II as grandfather; nothing on an invitation of the King of Italy as godfather |
| phrase search on the decoded Portuguese | searched | Google Books `"El Rei deseja convidar"`, `"padrinho do principe ou princesa que se espera"`, `"pelo telegrapho em cifra" 1865 Roma`; IA fts as above | 0 hits each |
| (d) holding archive: ANTT DigitArq | solver's record read, not re-queried | the unit's catalogue note quotes "pa-pa (419-419), di-ga-mo (926-923-1212)" (NOTES.md); images on disk | the catalogue knows the draft carries syllables over codes; it prints no plaintext. digitarq.arquivos.pt not contacted (0 requests; no image missing) |
| (e) IA / Google Books / HathiTrust | IA and Google Books searched as above; HathiTrust full text unreachable from the cloud (CLAUDE.md hosts table) | -- | -- |
| BNP bndigital | not re-queried | the solver logged its `?q=` as non-restricting (51732 results for every query), 25 Sept 2026 | unreachable as a search, per solver's log |
| (f) solver repos, DECODE, Cryptiana/Cipherbrain | solver's search accepted, not re-run | both repos grepped, DECODE 2897 cipher records, blog search (NOTES.md) | 0 hits |
| (g) scholarship | searched | OpenAlex (Bearer key) `Costa Cabral Santa Sé 1865`, `Conde de Tomar embaixada Roma`, `padroado 1865 Santa Sé Portugal concordata 1857`, `cifra diplomática portuguesa século XIX`; Semantic Scholar (x-api-key) same four | nothing on this letter, the godfather question or Portuguese 19th-century cipher; S2 returned no data for the first three queries |
| JSTOR | done 26 Sept 2026 | one row in JSTOR-QUEUE.tsv: ("Costa Cabral" OR "Conde de Tomar" OR "Conde de Thomar") AND ("Santa Sé" OR "Holy See" OR Padroado) AND 1865 | two context-only hits (Sardica 1997; Chato Gonzalo and Costa 2007, both general Iberian-liberalism political history), neither on this letter or its cipher; does not change the class |
| web | searched | two WebSearch queries (Afonso's baptism; Costa Cabral Roma 1865 cifra) | Afonso's godparents Napoleon III and Isabel II (Wikipedia); nothing on this letter |

Requests: archive.org 13 (advancedsearch 1, metadata 4, djvu 4, be-api fts 4); googleapis books 17 (>=3 s apart);
openalex 4; semanticscholar 4; digitarq 0; bndigital 0.

## 5. Did we first-decipher?

No. Nothing was deciphered: the encipherer wrote the plaintext above the codes. What R6 P5 produced is a key table
rebuilt from that gloss and a reproducible alignment (a recovery from the document, like rah-canada-1869 and clair1067).
No printing of the letter or its text was located; that is a search result, and at N0 it carries no novelty wording.
The honest description is: "a period key rebuilt from the leaf; the plaintext is the clerk's own".

## 6. Rule 4 and rule 7 (task 5)

- `python3 tools/decode_key.py ciphers/antt-fcc-costacabral-1865 --check`: "tokens 84: C 63, M 19, U 2 / reading up to
  date", exit 0. The counts reproduce.
- **C is the right grade** for a code whose value is read off the leaf's own gloss (rule 4: C, from known plaintext).
  It is not H (no key sheet), and not S. The solver's key.tsv `source` column already says `gloss`. The NOTES.md
  sentence defining C by "consistent across occurrences / both passes" describes the transcription check, not the
  grade's basis; the basis is the gloss (annotated in NOTES.md).
- Display caveat: for the three colliding codes reading_tokens.tsv carries both values (`ar|al`, `do|elo`, `ke|te`, M),
  but reading.txt prints only the first value, so m0114 R1 reads "sou ber ar ..." and R4 "... ke lho" where the leaf's
  gloss has "al" and "te". On a self-glossed leaf the gloss at each position is the evidence; a per-code key flattens
  it. Not a stale-reading fault (the check passes); noted for the solver.
- Leads for the solver from the image (verifier's eye, not applied): at m0113 R11 the gloss over 508 looks like "te"
  ("a este respeito"), which would remove the 508 collision; 206 on R8 carries a gloss ("za"/"sa", "princesa"), so it
  need not be U; the m0114 R5 line is partly legible. No spec exists, so no judge was run; the solver's reason (no
  1865 Portuguese corpus) stands.

## 7. Postmortem and corrections

Failure named: the solver called the status `found-solved` and the key `ours`, used "unpublished" in a check-solved
sentence, and read the gloss as "scattered drafting fragments ... not a continuous letter", unrelated to the folder.
The gloss is a continuous confidential message about the royal godfather question and the Pope; the recipient is the
fonds owner, Costa Cabral, Conde de Thomar, envoy at the Holy See. Corrections made in NOTES.md (edited in place,
marked "[V6 25 Sept 2026]"): status line to `solved`; "unpublished archival draft" to "an archival draft, no print of
it located"; key source `ours` to `period`; the "scattered fragments" paragraph annotated with section 2 above. No
status.json edit (brief). No second-opinion row: N0 is below N3.

## AUDIT 2 (VER1-LOWC, 5 Oct 2026)

Verifier VER1-LOWC (for LANE-VER1, account ytbiz), 5 Oct 2026, 19:30-19:45 UTC by `date -u`. A separate session from Audit 1
(V6-COSTA, 25 Sept 2026) and from the solver (LANE R6 P4/P5). Second adversarial audit under CLAUDE.md Outreach gate 2. No
decoding; reading, key and ciphertext unchanged; Audit 1's leads in s.6 (508 = te, 206 gloss, m0114 R5) remain unapplied.

**Checks, fresh this session:**
- **Rule 7:** `python3 tools/decode_key.py ciphers/antt-fcc-costacabral-1865 --check` -> "reading up to date"; C 63, M 19, U 2 of
  84, as in Audit 1. No reading change since Audit 1; nothing to propagate (no SO row: N0).

**Search log, 5 Oct 2026** (one request at a time per host, >=1.6 s apart; descriptive UA):

| family | status | what | result |
|---|---|---|---|
| Google Books API (keyed, country=US) | searched | `"Caetano de Magalhães" "Costa Cabral" 1865`; `"padrinho" "Rei de Italia" 1865 "Santa Sé"`; `"Costa Cabral" Roma 1865 cifra` (0); `"Arquivo Costa Cabral" Torre do Tombo`; `Bonifácio "Costa Cabral" padrinho "Rei de Itália"` (0); `"Um Homem Singular" Costa Cabral 1865 padrinho` (0); `"padrinho" "infante D. Afonso" 1865 "Vítor Manuel" núncio` (0); `"Caetano de Magalhães" Thomar cifra` (0) | **context printed, item not:** *D. Manuel II, história do seu reinado* (1930, vol. `2IFPTB6UF44C`) snippet: "padrinho do herdeiro do monarca Fidelissimo, o senhor núncio lançava o seu protesto, porque não só o Rei de Itália ..." -- the nuncio's protest at the King of Italy as godfather, i.e. the very question the worksheet raises; Bonifácio, *Um Homem Singular* (2013), a Costa Cabral biography that cites the Arquivo Costa Cabral (ACC) at ANTT -- the fonds this leaf belongs to -- found by title only, no snippet on 1865 or the godfather question, not opened |
| IA full text (be-api fts) | searched | `"padrinho do principe"` (48: a 1742 Gazeta de Lisboa formula "padrinho do Principe, ou Princeza, que nacer", other reigns); `"Costa Cabral" "Rei de Italia" padrinho` (104; *O Commercio do Porto* items: "escolhido por S. M. para padrinho do Infante recemnascido El-Rei de Italia Victor Manoel" and "do veto posto pelo nuncio a ser o rei de Italia padrinho do segundo filho dos reis de Portugal"); `"conde de Thomar" "Caetano de Magalhães"` (2, unrelated) | the godfather question and the nuncio's veto were reported in the press (issue dates not read); no hit prints the worksheet's text or the Magalhães letter |
| OpenAlex (Bearer) | searched | `Costa Cabral embaixador Santa Sé 1865 Pio IX` (13, top 8 read: episcopal nominations, Vatican I diplomats 1869-70, and *Maria Pia de Sabóia (1847-1911) ... relações Portugal-Itália* (2013), the most likely scholarly place for the godfather affair -- not opened); `Victor Emmanuel godfather Portuguese infante 1865 Pius IX` (0) | nothing prints this item; one article unread (gap) |
| Semantic Scholar (x-api-key) | searched | `Costa Cabral Holy See 1865` | 0 |
| HAL | searched | `"Costa Cabral" Santa Sé` | 0 |
| CrossRef | searched | `Costa Cabral Conde de Tomar Roma Santa Sé 1865 correspondência` | nothing relevant in top rows |
| Solver repos | searched | fresh shallow clones 5 Oct 2026 (cyphersolver @a439937, unsolved-ciphers @d2800bb), grep `costa cabral`, `costacabral`, `FCC/001`, `thomar` | none |
| JSTOR | queued | 1 row appended 5 Oct 2026, family (ii) bare phrase `"padrinho do principe ou princesa"` (family (i) done 26 Sept, row 78: context only) | pending; does not block the class |

**Classification (Audit 2).**
- **Class N0 upheld.** The clerk's Portuguese syllables written over every code are the plaintext of this very item (Audit 1 s.2,
  endorsed). Key `period` (rebuilt from the period worksheet; Audit 1's correction of the solver's `ours` stands). Text `known`
  on the leaf; **no print of the worksheet's text or the cover letter located** by either audit. What is in print is the context:
  the godfather question and the nuncio's objection (1930 reign history; *O Commercio do Porto*), and the papal-letter affair of the
  cover letter (1887 Livro Branco, Audit 1).
- **Depth D2**, 75.0% (C 63 of 84; M 19 incl. the three two-value codes, U 2). Not D3: below 80%. The clause "convidar [o] Rei de
  [I]talia para padrinho do princi[pe] ou prince[sa] que se espera" reads from the leaf's own gloss, and the 1930 print and the
  press independently confirm the historical fact it states (an Italian royal godfather objected to by the nuncio).
- **Depth sentence:** The worksheet's message says the King wishes to invite the King of Italy to be godfather to the prince or
  princess then expected, and asks how far the Pope would tolerate it.
- **Safe sentence:** "ANTT FCC/001/0021/00026 carries an 1865 syllabic-nomenclator encipherment worksheet with the clerk's own
  Portuguese plaintext written over every code; we rebuilt a 52-row partial key from it (C 63, M 19, U 2 of 84 tokens). Its subject,
  the King of Italy as godfather to the expected royal child, is known from print; the worksheet's own text was not found in print
  (N0, two audits; partially deciphered, about 75%; key period)."
- **Unsafe sentence:** "We deciphered an unpublished 1865 Portuguese cipher"; "first reading"; "the godfather affair revealed".

**Postmortem (Audit 2).** No over-claim found: NOTES.md status `solved` with Audit 1's corrections; status.json `N0`, `key: period`.
Audit 1's "nothing on an invitation of the King of Italy as godfather" (s.4 row (c)) is superseded by the two print hits above:
the affair itself is in print; the item's text is not. That strengthens the reading's context and does not change the class.

**depth_check (5 Oct 2026, after the status.json update):** `python3 tools/depth_check.py` -> exit 0; summary line: "unique solves (N3+ and D2+): 16 -- D4 1, D3 2, D2 13; not counted D0/D1: 13; legacy ungraded: 0" (these three are N0, so they are not in the unique-solve count).
