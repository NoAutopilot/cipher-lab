# AUDIT: ceppo-nevers-fr3251-1570s, f.11r (VERIFY-CEPPO-1, 28 Sept 2026)

Verifier: PARENT WORKER VERIFY-CEPPO-1 (owner account), a session separate from the solver (HARVEST-A). Brief
`.claude/briefs/runs/2026-09-28-parent-verify-ceppo-1.md`. Clock read with `date -u` at 17:18 and 17:33 UTC,
28 Sept 2026.

**Claim under audit** (HARVEST-A, ROOM 17:07 UTC): f.11r (no.6, Lodovico Birago to the duc de Nevers, Saluzzo,
14 Sept 1570, BnF fr.3251, Gallica btv1b9060248g canvas 12) read in part with the printed Ceppo-Nevers key
(Tomokiyo, nevers_add1.png). 135 tokens S 53 M 68 I 12 U 2. The key ranks 1 of 201 shuffled keys on the reconciled
transcription (the reconciler saw the values, so that run is not blind) and 2 of 201 on blind pass B. Judge FAIL,
-1.289 against real_p05 -0.958.

## Verdict

| item | scope | class | key | text | confidence |
|---|---|---|---|---|---|
| f.11r P1, P2, P4 fragments (below) | recovered-passages: fragments only | **N3** | published | unknown | moderate on the fragments; none on continuous text |
| f.11r P3, P5 | none | not classed | published | unknown | nothing read |

Key source: `published`. The Ceppo-Nevers cipher was rebuilt by Satoshi Tomokiyo from BnF fr.4702 fol.37 and
supplemented from fr.3521. It is printed as the image nevers_add1.png on cryptiana.web.fc2.com/code/nevers.htm,
and our copy is `keys/key_ceppo_nevers.tsv`. Tomokiyo named these letters and the key; applying the key to f.11r
is ours.

**N3 reason.** The search (below) found no reading or decipherment of f.11r or of any Ceppo-Nevers letter in
fr.3251 other than the period decipherments on ff.27, 39 and 82. It found no printed edition of Birago's letters
to Nevers. Tomokiyo (live page re-read today) and Bourdeau (SOLVED_CATALOGUE.md, checked 22 Sept 2026 there) both
list f.11 as having no published reading. The class is not N4, for three reasons: the principal Italian
Saluzzo/Reformation histories that quote Birago's correspondence (Jalla, *Storia della Riforma in Piemonte*; *Il
Marchesato di Saluzzo e la Riforma protestante*, 1960) were found only as Google Books snippets and not read; no
JSTOR or Persée/HAL pass was run; and the fragments are too short for a meaningful phrase search.

## What the verifier reproduced

### 1. Blind re-reconciliation (step 2)

The reconciler was one Opus vision subagent. It was allowed to open only the value-blind sign sheet
(`harvest/sign_sheet_blind.png`), the native band image and its crops, and passA/passB. It never saw
`sign_id_map.json`, any key file, passC, the reading or NOTES.md. Its output is
`harvest/passD_blind_verify.tsv` (136 signs; 32 positions depart from both passes).

- It independently found the three signs the solver said both passes had missed: the barred 8 S80 (9 places),
  the barred oval S69 (3 places) and the t-3 ligature S56 (P1 pos 12). The solver's value-aware reconciliation
  did not introduce these; a value-blind eye sees them too.
- It found a double-barred oval that matches no sheet cell (P1 pos 26, P2 pos 13, P3 pos 11), written '?'. This
  is the glyph HARVEST-A graded I as r. The sheet has no cell for it, which confirms it is outside the printed
  key.
- Sign agreement by alignment: D vs solver's C 0.794; D vs A 0.518; D vs B 0.715; A vs B 0.619.

### 2. Key test on the blind transcription (`harvest/decode_control.py`)

Printed values only, with no exceptions applied.

| transcription | letters | real key | shuffles mean / max | z | rank of 201 | power control |
|---|---|---|---|---|---|---|
| D, blind (seed 7) | 128 | -1.247 | -2.086 / -1.674 | 5.54 | **1** | 20/20 rank 1, z median 5.91 |
| D, blind (seed 11) | 128 | -1.247 | -2.078 / -1.679 | 5.82 | 1 | (5 windows) |
| D, blind (seed 23) | 128 | -1.247 | -2.062 / -1.661 | 5.38 | 1 | (5 windows) |

On a transcription made without values, the printed key beats every one of 200 shuffles on three seeds. Rule 3
is met: the power control at 20% sign error has the real key first in 20 of 20 windows.

Judge on the blind reading's letters (`tools/judge_plaintext.py specs/ceppo-nevers-fr3251-1570s.json --file
<D letters>`), pasted:

```
FAIL language: score=-1.267, null_p99=-1.629, real_p05=-0.957, real_median=-0.826, mode=both, N=124
FAIL - ceppo-nevers-fr3251-1570s (a PASS is a gate for a verifier, not a reading; rule 10)
```

### 3. Line-by-line read against 20 shuffled keys read blind (step 3)

`harvest/verify_mk_blind.py passD_blind_verify.tsv <dir> 4242` writes 21 decodes of the blind transcription: the
real printed key and 20 value-column shuffles, in random order (`harvest/verify_blind_decodes.txt`, answer
`harvest/verify_blind_answer.json`). One Sonnet reader saw only the decodes file. It rated TEXT 08 as the only
text with any Italian ("presidente", "mandato"), and TEXT 08 is the real key. It rated all 20 shuffles 0 and found
no word of four or more letters in any of them (`harvest/verify_blind_read.tsv`, `verify_blind_judgment.tsv`).
The reader was strict and did not list "sauoia", "curare" or "chuni"; it found no word of any kind in the 20
shuffles.

The blind reading under the printed key (grade string: S = the blind reconciliation D and the solver's C agree on
the sign; M = they differ; U = no sheet cell):

```
P1 ircofedimpresidentemorfo_tmandatoham      SMMSSSSSSSSSMSMSSSSMSMSSUSMSSSSMSMSS
P2 npfocurarema_estitucioredihemf            SSSSSSSSSSSSUSMMSSSSSSMSMSSSMM
P3 harcodimhp_chesatodi_et                   MSMSSSSSMSUSSSMSMSSSUSS
P4 ncamuioamchunimochiirsauoia               SSSMSSSSSSSSSSSSSSSSMSSSSSS
P5 etuoiuiromosequc                          SSSSSSSMSSSMSSSS
```

Tokens (blind D): 136 = S 107, M 25, U 4 (plus the 6 nulls in the count). H 0, C 0: this is a cryptanalytic
result with a published key.

| passage | phrase | forced by the printed key? | in 20 shuffles (blind) | verifier grade |
|---|---|---|---|---|
| P1 | **presidente** (letters 10-19) | yes, no overrides | 0/20 | S 8, M 2. The two M signs are where C read "premisente", so the word rests on the blind reconciliation. |
| P1 | **mandato** (27-33) | yes | 0/20 | S 5, M 2. C read "candaoo" here. |
| P1 | "di[l]" before presidente | only with the pound-sign override (printed m) | - | I |
| P2 | **[pro]curare** ("curare" 5-10) | "curare" yes; the "pro-" r is the theta variant, I | 0/20 | curare S 6 |
| P2 | **[r]estitucio[ne]** ("estitucio" 14-22) | "estitucio" yes; the initial r is the unsheeted double-barred glyph (U), and "la" needs the pound override | 0/20 | S 7, M 2; r I; "ne" not in D (C only) |
| P4 | **[al]chuni [l]ochi** ("chunimochi" 10-19) | "chuni", "ochi" yes; both l's are the pound override (printed m) | 0/20 | S 10 on the forced letters; the l's are I |
| P4 | **in Sauoia** ("sauoia" 22-27) | "sauoia" yes; "in" vs "ir": D and C differ on one sign | 0/20 | sauoia S 6; in M |
| P3 | "che" | 3 letters only | - | not a reading |
| P5 | - | - | - | nothing read |

**Recovered passages (the claim scope):** P1 "... presidente ... mandato ...", P2 "... [pro]curare [la
r]estitucio[ne] ...", P4 "... [al]chuni [l]ochi in Sauoia". The printed key forces each bolded word with no
overrides, and none of them turns up in 20 shuffled-key decodes read blind. Continuous text is not recovered;
P3 and P5 are unread.

## Grades endorsed

- I endorse S for the forced letters above: presidente, mandato, curare, estitucio, chuni, ochi, sauoia. The count
  across the whole blind transcription is S 107 / M 25 / U 4.
- The solver's 12 I tokens stay **I** and are not endorsed as readings:
  - pound sign = l (7 places). Tomokiyo's image clearly prints it under m, row 2; this audit re-read the image.
  - double-barred oval = r (4 places). It has no cell in the printed key.
  - ticked 6 = s (1 place).
  These overrides make the fragments read "la restitucione" and "alchuni lochi"; without them the key gives
  "ma-estitucio" and "amchuni mochi". They are plausible, but they come from context and have no key source or
  control. The named next step below would test them.
- The solver's P1 reading ("premisente con fort candaoo") is **not** endorsed. The blind reconciliation reads
  "presidente ... mandato" at the same place. The two reconciliations differ at the M signs, so P1 is M wherever
  the grade string says so.

## Search log (novelty first, step 1), 28 Sept 2026

| family | what was searched | result |
|---|---|---|
| Tomokiyo, cryptiana.web.fc2.com/code/nevers.htm | live fetch (1 request, HTTP 200), BnFfr3251 section diffed against our 27 Sept mirror | unchanged: f.11 no.6 not marked "(with decipherment)"; key note "allows reading ... but not quite" concerns fr.4702 |
| Cryptiana blog | blog search "Birago" (cryptiana.blogspot.com/search?q=Birago) | 2 posts (Jul, Sep 2024), both on f.119 (Nov 1571 figure cipher); nothing on f.11 or the Ceppo-Nevers letters |
| Cipherbrain | web search site:scienceblogs.de Nevers Chiffre Birago | no hit |
| Cipher Mysteries | web search ciphermysteries Nevers Birago cipher 1570 | no relevant hit |
| Bourdeau, dbourdeau/cyphersolver | fresh clone, HEAD 648309e (26 Sept 2026), grep birago/ceppo/3251; live index.html | SOLVED_CATALOGUE.md l.237 lists fr.3251 ff.11, 21v, 35, 87 as having no published reading; targets/birago is f.119 only |
| Bourdeau forks (arya1515, aryasn2026) | seen as web-search results only; not opened (out of this session's repository scope) | not searched inside; noted as unreached |
| Aymeloglu, aaymeloglu/unsolved-ciphers | fresh clone, grep birago/ceppo/3251 in catalogue/decode-catalog.csv and the whole repo | DECODE has 5 Birago records (fr.3619, 3621, 3623, 1591-92, all "Decrypted", a different Birago period); none for fr.3251 |
| DECODE (de-crypt.org) | through Aymeloglu's catalogue mirror above and the sibling folder's 24 Sept grep; no live login | no fr.3251 record |
| open web | 3 web searches (Birago Nevers 1570 Saluzzo cifra restitutione Savoia; "Ceppo-Nevers" cipher; cryptiana Birago Nevers fr.3251 September 1570) | BnF fr.4702 finding aid, Bourdeau index, GitHub forks; no reading |
| Google Books API (key, country=US) | Birago Nevers 1570 Saluzzo; "Lodovico Birago" Nevers lettere; Birago Nevers cifra; "alcuni luoghi" Savoia Birago Nevers; Birago Nevers 1570 restituzione luoghi Savoia presidente | catalogues of BnF manuscrits français; Saluzzo Reformation histories (Jalla 1982; *Il Marchesato di Saluzzo e la Riforma Protestante* 1960) quote letters *to* Birago, snippet only, not read; no cipher reading |
| Internet Archive | advancedsearch Birago AND Nevers AND Saluzzo | 1 unrelated item |
| OpenAlex (key) | works?search=Birago Nevers cipher | 1 unrelated hit |
| JSTOR, Persée, HAL, Semantic Scholar | not run this session | unreached (JSTOR rows queued below) |

Requests: cryptiana.web.fc2.com 1; cryptiana.blogspot.com 1; web search 5; googleapis.com 6; archive.org 1;
api.openalex.org 1; github.com 2 clones. Subagents: 1 Opus (blind reconciliation), 1 Sonnet (blind reader).

## Did we first-decipher?

Not claimable. A fragment reading with Tomokiyo's published key, not located elsewhere after the search above,
is N3. Say "read in part with Tomokiyo's published key; no prior reading located", never "first".

**Safe sentence:** "Birago's letter to Nevers of 14 Sept 1570 (BnF fr.3251 f.11r) reads in part with Tomokiyo's
published Ceppo-Nevers key. On a value-blind transcription the key beats 200 of 200 shuffled keys. Fragments
recovered: 'presidente', 'mandato', '[pro]curare [la r]estitucio[ne]', '[al]chuni [l]ochi in Sauoia'. No prior
reading of this letter was located (search logged in AUDIT.md, 28 Sept 2026)."

**Unsafe sentences:** "f.11r deciphered"; "first decipherment of Birago's letter"; "the letter asks for the
restitution of places in Savoy" (that is an interpretation of fragments, and two of its words depend on I
overrides); any continuous translation.

## Postmortem

- The solver's bias caveat was honest, and it turned out not to matter for the key test. The value-blind
  reconciliation ranks the key 1 of 201 (z 5.4-5.8), better than the solver's own reconciliation did.
- It did matter for P1. The solver's value-aware reconciliation gave "premisente con fort candaoo"; the blind
  one gives "presidente ... mandato". P1 should be reported from the blind sequence, graded M at the disputed
  signs.
- Over-claim corrected: NOTES.md HARVEST-A's line "Italian words recoverable (procurare la restitucione;
  alchuni lochi in Sauoia)" presents I-override letters as read. It now carries a correction pointer to this
  audit: the forced words are curare, estitucio, chuni, ochi, sauoia (plus presidente, mandato on the blind
  sequence), and "pro-", "la r-", "al-l-", "l-" are I.

## Named next step (for the orchestrator)

Test the three variants against the period witnesses before reading any further letter. Do the pound sign (l vs
the printed m), the double-barred oval (r?) and the ticked 6 appear on ff.27, 39 or 82, and does the period
interlinear gloss give their value? If it does, the fragments become "la restitucione", "alchuni lochi", which
would turn I into S or C. After that, apply the same blind protocol to f.21v, f.35 and f.87.

## Second-opinion claims not confirmed

None filed yet. The SO row is queued below.

---

# Second audit (VERIFY-CEPPO-2, adversarial, 28 Sept 2026)

Verifier: PARENT WORKER VERIFY-CEPPO-2 (owner account, session_01DTnzLDCCBHdGCCGdSxcNZv), a session separate
from HARVEST-A and VERIFY-CEPPO-1. Brief `.claude/briefs/runs/2026-09-28-parent-verify-ceppo-2.md`. Clock read
with `date -u` at 18:17 and 18:30 UTC, 28 Sept 2026. Scripts and outputs are in `harvest/v2/`.

## Verdict: **held in part**

| item | scope | class | key | text | confidence |
|---|---|---|---|---|---|
| f.11r "presidente", "mandato" (P1), "curare", "estitucio" (P2), "chuni", "ochi", "sauoia" (P4), forced by the printed key on the blind transcription D | recovered-passages: word fragments | **N3** (upheld) | published | unknown | high that they are not chance; moderate on each word's exact letters (below) |
| the I-graded letters: "di[l]", "[la]", "[r]estitucio[ne]", "[al]chuni [l]ochi", "[pro]curare" | none | not endorsed as read | - | - | I, unresolved by the witnesses |
| P3, P5, continuous text | none | not classed | - | - | nothing read |

Key source: `published` (Tomokiyo's Ceppo-Nevers table, nevers_add1.png; see the first audit).

What held: novelty (nothing in print, wider search below), and the claim that the fragments are not chance
(0 of 2,000 chance decodes come close, script and blind reader). What did not hold as the first audit wrote it:
(a) two of the seven words rest on letters that neither independent blind pass A nor B saw, only the value-blind
reconciler D (details below), so they are S-with-a-caveat, not clean S; (b) the pound-sign override does not
survive a per-occurrence test, so "[al]chuni [l]ochi" and "[la r]estitucio[ne]" stay I and must not appear in an
outward sentence as read; (c) the ticked-6 override is not an override at all on D (see 3).

## 1. Novelty, harder (step 1)

| family | what was searched (28 Sept 2026) | result |
|---|---|---|
| BnF catalogue record, fr.3251 | archivesetmanuscrits.bnf.fr/ark:/12148/cc49712p (1 request, 200) | "Fol. 11 • 6 Lettre, avec chiffre, de « LODOVICO BIRAGO » au « duca di Nivers,... Da Saluzzo, il 14 settembre 1570 ». En italien." -- "avec chiffre" only; the catalogue marks decipherment where present ("Fol. 39 • 20 ... avec chiffre et déchiffrement"). Confirms folio, date, parties and that no period decipherment exists on f.11. |
| Printed BnF catalogue (Catalogue général des mss français, Ancien fonds, 1868) | IA p1cataloguegnr02bibluoft, _djvu.txt fetched once, parsed by script | same entry (no.6 "avec chiffre", fol.11); OCR prints the number as "3231" (3/5 confusion; order of neighbouring entries confirms it is fr.3251, and the OCR "3251" entry is fr.3231, Guise to Nemours). No decipherment printed. |
| Google Books API (key, country=US), Italian and French | 17 queries: "Birago" "Nevers" 1570 lettere cifra; "Lodovico Birago" "duca di Nevers"; "Birago" "14 settembre 1570"; "Birago" "restituzione" Savoia 1570 Saluzzo; "restitutione" "luoghi" Savoia 1570 Birago; "Birago" Nevers "in cifra" Saluzzo; "Birague" "duc de Nevers" Saluces lettres; "Birague" Nevers "14 septembre 1570"; "Birague" "restitution" places Savoie 1570; "Birague" Nevers lettres chiffrées Saluces 1570; Boltanski "ducs de Nevers" Birague chiffre; "Ceppo" Nevers chiffre; Tomokiyo Nevers cipher Birago; and others | catalogues; Denina, *Rivoluzioni d'Italia*; Douais, *Lettres de Charles IX à Fourquevaux* (1897); Boltanski, *Les ducs de Nevers et l'État royal* (2006); Gribaudi, *Storia del Piemonte* (1960); *Il Marchesato di Saluzzo e la Riforma protestante* (1960, cites fr.3251-3252 for Birago's complaints to Bellegarde). All snippet-only; none shows a decipherment or the text of f.11. Not read in full (see "not reached"). |
| Internet Archive full text (be-api) | "Birague au duc de Nevers"; "Birago al duca di Nevers"; "Birague" "duc de Nevers" "en chiffre" Saluces; "alchuni lochi"; "restitucione" Savoia | no hit on this letter. "alchuni lochi" is attested 16th-century Italian (Varthema, *Itinerario*; a Fugger newsletter), which supports the spelling as plausible, nothing more. |
| OpenAlex (key) | Birago Nevers Saluzzo 1570; Birague Nevers Saluces; Ceppo Nevers cipher | 9 results, none relevant |
| Semantic Scholar (key) | Birago Nevers; Birago Nevers Saluzzo | nothing relevant (first two calls returned no total; retry returned unrelated papers) |
| CORE (key) | Birago AND Nevers | 12 hits, all BnF catalogue records of the Nevers recueils |
| HAL | Birague AND Nevers | 0 |
| Persée | Birague Nevers Saluces (articles) | top hit Machiavélien ou anti-machiavélien? (2013, Nevers and René de Birague as counsellors); nothing on the letters or the cipher |
| Cryptiana blog | search "Ceppo" | "No posts matching the query" |
| Web search (2) | Italian: Lodovico Birago lettera duca di Nevers 14 settembre 1570 cifra decifrazione; French: Birague Nevers 1570 lettre chiffrée déchiffrement Saluces restitution places Savoie | BnF finding aids (fr.3251, 4702, 4703, 4699), Bourdeau index, Wikipedia; no reading of f.11 |
| Tomokiyo nevers.htm, Bourdeau, Aymeloglu/DECODE | not re-run; first audit's same-day checks stand (live page unchanged; Bourdeau lists f.11 unread; no DECODE record for fr.3251) | - |

Not reached: the full text of *Il Marchesato di Saluzzo e la Riforma protestante* (1960) and of Boltanski 2006;
these are the two books most likely to quote Birago's fr.3251 letters. Both cite the volumes; neither snippet
shows a cipher reading. JSTOR rows for this target are already queued by the first audit (2 rows); fragments are
too short for a family (ii) phrase row. Good-citizen note: one malformed loop of mine sent about 24 Google Books
calls with no pause (about 18:24 UTC); it returned without a 429, and the later calls were spaced 1.6-2 s.
Requests: googleapis.com about 45; archive.org 5; be-api 7; api.openalex.org 3; api.semanticscholar.org 3;
api.core.ac.uk 1; api.archives-ouvertes.fr 1; persee.fr 1; cryptiana.blogspot.com 1; archivesetmanuscrits.bnf.fr 1;
gallica.bnf.fr SRU 1; web search 2.

**Class stays N3**: no print of the plaintext or of a decipherment of f.11r located; not N4 while the two Saluzzo
monographs above are unread.

**New witness lead (not a novelty matter).** The same catalogue lists in fr.3252 (Gallica ark:/12148/btv1b9060232m)
"24. Lettre, avec chiffre et déchiffrement, de « Lodovico Birago » au « duca di Nevers,... Da Saluzzo, li 5 aprile
1571 ». En italien. (Fol. 36.)" -- inside Tomokiyo's Ceppo-Nevers window (Sept 1570-May 1571) but not in his
fr.3251 list and not in this folder. If it is the same cipher and its gloss is legible (ff.27/82's are not), it is
the witness that can settle the pound sign and the double-barred oval. Not fetched: outside this brief.

## 2. Chance controls (step 2): `harvest/v2/chance_control.py` (seed 2028)

Transcription: the value-blind D. Metric (script, no model): Italian lexicon = every word type of it16dip with
corpus count >= 3 (14,166 types, length >= 4); per decode, the longest lexicon word found as a substring, and the
number of distinct lexicon words of 6+ letters.

| arm | decodes | longest word >= 10 (real: presidente) | 7+ words of 6+ letters (real: 7) | longest-word distribution |
|---|---|---|---|---|
| real key, real order | 1 | yes (10) | yes (7) | - |
| K: 1,000 shuffled keys | 1,000 | **0** | **0** | 0:196, 4:664, 5:130, 6:10 |
| T: true key, sign order shuffled within each passage | 1,000 | **0** | **0** | 0:25, 4:713, 5:239, 6:22, 7:1 |

The best chance decodes carry one word of 6-7 letters ("regale", "contro", "moderni"); never two. The T arm keeps
the key's own letter frequencies, so Italian-like letter mix alone does not make the words: order does.

Blind reader (one Sonnet subagent, no tools, decodes inline, answer key withheld,
`harvest/v2/chance_reader_decodes.txt`, result `harvest/v2/reader_result.tsv`): 40 texts = the real decode, the 8
highest-scoring decodes of each chance arm (an adversarial pick from the 2,000), and 23 random chance decodes.
Only the real decode (TEXT 11) scored 2 ("presidente", "mandato", "curare"; "estitucio" noted as looking like
"restitución"). Nine chance decodes scored 1, each an isolated word (setta, amati, regale, rateo, scuote, contro,
Cristo, moderni, ostro); 30 scored 0. No chance decode had two words. The reader did not list "sauoia" or
"chuni", so the blind reader supports P1 and P2 more strongly than P4.

**Chance does not produce the fragments.** This part of the first audit holds.

## 3. The overridden letters (step 3): `harvest/v2/override_test.py`

**Without overrides** (printed values only, D):
```
P1 ircofedimpresidentemorfo_tmandatoham
P2 npfocurarema_estitucioredihemf
P4 ncamuioamchunimochiirsauoia
```
presidente, mandato, curare, estitucio, chuni, ochi, sauoia are all still there. The overrides only add the
joining letters (di[l], [la r]-, [al]-, [l]-, [pro]-).

- **Ticked 6.** Not an override on D. The value-blind reconciler matched the ticked 6 to sheet cell S77 = printed
  s row 2 (4 places: P1 pos 14, P2 15, P3 15, P5 13); HARVEST-A's exception reads it as m row 1 and overrides to s.
  On D the s in "presidente" and "estitucio" is the printed value. Caveat: s row 2 is one of the two key cells our
  own key transcription graded M (its exact shape unresolved), and the passes A and B read those positions as S37
  (c). Grade: S on the key, M on the sign.
- **Pound sign S31 (printed m row 2), claimed l, 8 places on D.** An it16dip 4-gram model choosing the best of 19
  letters in a +-6-letter window per occurrence puts l first in 3 of 8 (P2 11, P4 4, P4 9); the printed m first in
  1 (P1 10, "dim presidente"); elsewhere l ranks 6-15. Pooled over all 8, l ranks first. That is what a
  context-fitted value always does, and 3 of 8 is not a consistent sign. The witnesses do not help: in
  `witness/key_rows_ceppo*.tsv` the m rows have 0 confirmations. **Stays I.**
- **Double-barred oval (no sheet cell), claimed r, 3 places.** Best letter per occurrence: e, l, o; r ranks 4, 2 and
  15. **Stays I.** The same mark appears in the f.27 witness (NOTES.md: position 9 "oval crossed by two close
  parallel bars", unmatched), but that gloss is illegible, so its value is still unknown.

## 4. How far each word depends on the reconciler D

The two independent blind passes A and B, decoded alone with the printed key, give almost nothing ("peeeccdente",
"peeecisente"). The words appear only after reconciliation. Per letter (A/B/C = agrees with pass A / B / the solver's
value-aware reconciliation C; --- = D alone):

| word | letters that D alone reads (neither A, B nor C) | letters D shares only with C | clean in B |
|---|---|---|---|
| presidente | s (the ticked 6 as S77) | r (S56 ligature) | p, e, n, t, e |
| mandato | t (S88) | a | n, a, o |
| curare | none | u, a | c, r, r, e |
| estitucio | s (S77), t (S88) | c | e, i, t, i, o |
| chuni / ochi | none | c | nearly all (B reads "ghunimochi") |
| sauoia | none | s, a, a (S10, S80 missed by A and B) | u, o, i |

D was value-blind (it saw only the unlabelled sign sheet), so its departures cannot lean toward Italian, and the
chance tests above run on D. But "presidente" and "estitucio" each depend on at least one sign that only D saw, and
"chuni ... ochi" is the only fragment that the raw pass B already gives. Grades: **S** for chuni, ochi, curare;
**S with one M sign** for presidente (s), mandato (t), estitucio (s, t), sauoia (the D and C agreement against both
raw passes). This is within the first audit's grade string; it is stated here so nobody reads "S 107" as 107
letters seen by three eyes.

## Passages endorsed

- P1: "... presidente ... mandato ..." (sequence only; "di[l]" I).
- P2: "... curare ... estitucio ..." ("[pro]", "[la r]", "[ne]" I).
- P4: "... chuni ... ochi ... sauoia" ("[al]", "[l]" I; "in" M).
Not endorsed: "procurare la restitucione", "alchuni lochi in Sauoia" as whole phrases; any gloss of the letter's
subject.

## Safe sentence (replaces the first audit's, which named I letters as recovered)

"Birago's letter to Nevers of 14 Sept 1570 (BnF fr.3251 f.11r) reads in part with Tomokiyo's published
Ceppo-Nevers key. On a value-blind transcription the printed key alone gives the word fragments 'presidente',
'mandato', 'curare', 'estitucio', 'chuni', 'ochi' and 'sauoia'; none of 2,000 chance decodes (shuffled keys, or
the key on shuffled sign order) gives more than one word of that length. No prior reading of this letter was
located (search logged in AUDIT.md, 28 Sept 2026)."

**Unsafe:** "procurare la restitucione", "alchuni lochi in Sauoia" as a reading; "the letter concerns the
restitution of places in Savoy"; "deciphered"; "first".

## Postmortem

- The first audit's safe sentence quoted "[pro]curare [la r]estitucio[ne]" and "[al]chuni [l]ochi" with brackets.
  Outside the repository the brackets fall off. Its overrides stay I. The sentence above uses printed-key letters
  only. Corrected here, not rewritten in place (the first audit's section stays as its record).
- The first audit listed the ticked 6 as an I override. On D it is the printed s row 2 cell; the override belongs
  only to HARVEST-A's reconciliation C.
- The first audit's grade string treated all D-alone signs as S. They are S on the key and M on the sign (table 4).

## For the orchestrator

- status.json: keep `partial`; result `recovered-passages`, class **N3**, key `published`, text `unknown`; second audit
  **held in part**.
- NEAR.md: add a row -- f.11r, printed key rank 1/201 on blind D (z 5.4-5.8), 0/2,000 chance decodes with two words;
  pound sign and double-barred oval I. Named next step: fetch fr.3252 f.36 (Gallica btv1b9060232m, Birago to Nevers
  5 April 1571, "avec chiffre et déchiffrement") and test whether it uses the Ceppo-Nevers signs and whether its
  gloss gives the pound sign and the double-barred oval. Then f.21v, f.35, f.87 under the same blind protocol.
- The second-opinion row already queued by the first audit should carry this safe sentence, not the first one
  (rule 10 propagation).

---

# AUDIT: f.21v, f.35, f.87 (VERIFY-CEPPO-D2-1, 29 Sept 2026)

Verifier: parent worker VERIFY-CEPPO-D2-1 (account 3, Opus 5.5, session_01YRxhvLZems8u4Y34NV2jdX), separate from the
solver HARVEST-D2 (session_01C8YXpNGQVwrAPE7TY6F4ze). Brief `.claude/briefs/runs/2026-09-28-verify-ceppo-d2-1.md`.
Clock read with `date -u` at 00:13 and 00:21 UTC, 29 Sept 2026. Files: `harvest/verify_d2/` (per folio: `passD.tsv`
= the verifier's value-blind reconciliation, `control_D.txt`, `grade_view.txt`, `blind/` decodes, answer, reader).
The model is the f.11r audits above. Key throughout: Tomokiyo's printed Ceppo-Nevers table (`published`,
nevers_add1.png, cryptiana.web.fc2.com/code/nevers.htm; our copy `harvest/sign_id_map.json`).

## Novelty first (step 1), all three letters, 29 Sept 2026

| family | what was searched | result |
|---|---|---|
| Tomokiyo, nevers.htm | live fetch (1 request, HTTP 200), text diffed against `sources/cryptiana/web/nevers.htm` | identical; ff.21v, 35, 87 still listed without "(with decipherment)"; no reading given |
| Cryptiana blog | blog search Nevers, Ceppo, Birago (3 requests); the two Birago posts (Jul, Sep 2024) opened and grepped for 3251 / 21v / 35 / 87 / Ceppo / 1570, comments included | Ceppo: "no posts"; Birago posts concern f.119 (13 Nov 1571) only; the one comment (27 Sept 2026) is on Henry of Navarre |
| Cipherbrain | web search site:scienceblogs.de klausis-krypto-kolumne Birago Nevers | no hit |
| Cipher Mysteries | web search site:ciphermysteries.com Nevers Birago | no hit |
| open web | "Birago Nevers cipher 1570 fr. 3251 deciphered"; Birago Nevers 1570 lettera cifra "questa carica" Saluzzo; Birago Nevers 1571 Saluzzo "secretamente" cifra Cornelio Bentivoglio | BnF finding aid cc49712p, Bourdeau index and forks, an unrelated 1592 Nevers paper; no reading of these folios |
| DECODE | Aymeloglu's `catalogue/decode-catalog.csv` (fresh clone d2800bb, 27 Sept 2026) grepped birago / ceppo / 3251; HARVEST-C's live DECODE holder search (28 Sept, with the 3621 positive control) stands | only the five 1591-92 Birago records (fr.3619, 3621, 3623); no fr.3251 record |
| Bourdeau | fresh clone 648309e (26 Sept 2026), grep ceppo / 3251 | SOLVED_CATALOGUE.md l.237: "ff. 11, 21v, 35, 87 ... have no published reading"; targets/birago is f.119 |
| printed Nevers / Birago correspondence | Google Books API (key, country=US), 11 queries: the three dates in Italian and French with Birago/Birague + Nevers, "uiuendo et seruendo", Birago + Bentivoglio 1571, "Lodovico Birago" lettere "duca di Nevers", Nevers correspondance Birago Saluces édition | only the BnF manuscript catalogues (1874-95), which list the letters "avec chiffre"; "uiuendo et seruendo" hits 1540s Bible translations only; no edition of Birago's letters to Nevers found |
| Internet Archive | advancedsearch (2), be-api full text (3): Birago/Birague + Nevers + ottobre/octobre 1570, "questa carica" Birago Nevers; Segre, *Emanuele Filiberto* (emanuelefilibert00segruoft) and Ricotti, *Storia della monarchia piemontese* vol.2 (storiadellamona04ricogoog) fetched once and grepped | Segre paraphrases Birago's 1571 worries about Spanish troops near Alessandria (the f.87 period) from Venetian dispatches; neither cites fr.3251 or quotes a cipher passage |

Not reached: Boltanski 2006 and *Il Marchesato di Saluzzo e la Riforma protestante* (1960) in full (snippet-only, as in
the second f.11r audit); JSTOR (rows not added: the fragments are too short for a family (ii) phrase row, and family (i)
rows for this volume are already queued by the first audit). Requests: cryptiana.web.fc2.com 1; cryptiana.blogspot.com 5;
googleapis.com 11; archive.org 6; be-api 3; github.com 2 clones (read only, in the scratchpad); web search 5.

**No prior reading or decipherment of f.21v, f.35 or f.87 was located. None is N0.**

## f.21v (no.11, Birago to Nevers, Saluzzo 12 Oct 1570)

### Blind re-reconciliation (step 2)

Two Opus subagents (L01-L06, L07-L11), each allowed only its line crops (`cut_folio_lines.py` lines2x, regenerated),
`sign_sheet_blind.png` and HARVEST-D2's raw passes A and B, copied into a scratch folder with no key file in reach.
They set every position from the ink, not only the splits. Result `verify_d2/f21v/passD.tsv`, 267 signs: both passes 220,
sided with B 29, with A 10, against both 8, nothing inserted or dropped. **D agrees with the solver's passC at 250 of 267
signs.** The 17 differences are look-alike pairs: S49/S73 (slash between dots, printed n vs null; D took S73 at L01 15,
L03 7, 10, 14 and S49 at L11 17), S74/S77 (m/s), S23/S97 (n/a, L07 10), S66/S26 (c/s, L09 23), S40/S32, X_NEW/S10 (x3),
and the double-barred oval: at L06.2 12 the reconciler matched it to the sheet's own cell S60, printed **r** row 1 (see
the I-sign section).

### Key test on D (200 shuffles, three seeds; `control_D.txt`)

| seed | letters | real key | shuffles mean / max | z | rank of 201 | power control (20% sign error) |
|---|---|---|---|---|---|---|
| 1 | 253 | -1.123 | -2.048 / -1.562 | 6.42 | **1** | 20/20 rank 1, z median 7.44 |
| 7 | 253 | -1.123 | -2.056 / -1.478 | 5.74 | 1 | 20/20 |
| 23 | 253 | -1.123 | -2.072 / -1.652 | 6.56 | 1 | 20/20 |

Rule 3 met. The solver's figure (z 6.40 on passC) reproduces on a transcription the solver did not make.

Judge on D's letters (X_THETA2 = r, X_POUND unkeyed), pasted:
```
FAIL language: score=-1.179, null_p99=-1.728, real_p05=-0.916, real_median=-0.825, mode=both, N=253
FAIL - ceppo-nevers-fr3251-1570s (a PASS is a gate for a verifier, not a reading; rule 10)
```

### Line by line against 20 shuffled keys read blind (step 3)

`verify_mk_blind.py verify_d2/f21v/passD.tsv verify_d2/f21v/blind 2129 X_THETA2=r` (pound sign left unkeyed). One Sonnet
reader saw only `blind_decodes.txt`: it rated TEXT 01 alone LANG, high confidence ("questa ... casa di qua, credo le,
uiuendo et seruend(o), tanto di, in diuerse, fatto, difficu_ta"); one shuffle SOME (mardate, date, dise, lasse, mila),
nineteen NONE with at most one 3-5 letter scrap. TEXT 01 is the real key (`blind_answer.json`).

D under the printed key (plus X_THETA2 = r), `grade_view.txt`: under each letter S = both raw passes and D agree at H,
m = D sided with a pass or confidence below H, d = D alone; `_` = pound sign unkeyed.

```
L01    lesacardahenesede_tuttodaemee&etcinre
L03    ranseitecioesoptaquestacaricasadiqua
L04    credolenesinersuad
L05    ciolnoser_isrcederuiuendoetseruend
L07    ranoreauaatiqua_chenartiton_euarm_
L09    nf_tantodinar_eindiuersectse
L11    t_mfatto&lseramenfadificu_ta
(L02.1 uptnedi_ort, L02.2 ha, L06.1 io, L06.2 auanfarminoraof, L08 iqua / a, L10 acioremtise: no word)
```

| line | phrase | forced by the printed key on D? | in the 20 shuffles (blind) | verdict |
|---|---|---|---|---|
| L01 | **tutto da** | yes (del needs the pound sign) | 0/20 | endorsed; "de[l]" I |
| L03 | **questa carica ... di qua** | yes, D = C at every sign | 0/20 (reader saw "questa", "casa di qua") | endorsed; the reader's "casa" is the same letters split differently |
| L03 | intencione (solver) | **no**: on D it reads "itecioe"; its three n's are the S49/S73 split (pass A S49 n, pass B and D S73 null) | - | not endorsed; M |
| L04 | **credo le ne** ... [p]ersuad | "credolene" yes; "persuad" needs an unread p (the sign reads "i n e r s u a d") | 0/20 | "credo le ne" endorsed; "[p]ersuad[e]" not |
| L05 | **ceder uiuendo et seruend[o]** | yes, 23 of 25 letters S | 0/20 | endorsed, the strongest passage |
| L07 | auanti qualche (solver) | **partly**: D reads "auaati qua_che": S23/S97 split at L07 10 (n/a), and the l is the pound sign | 0/20 (reader saw only "qua", "che") | not endorsed as read; "qua[l]che" I |
| L09 | **tanto di nar[.]e in diuerse** | "tanto di" yes; "nar" and "diuerse" each carry one double-barred oval as r, and "diuerse"'s s is D alone (S26 for both passes' S66) | 0/20 (reader saw "tanto di", "in diuerse") | "tanto di" endorsed; "in diuerse" endorsed with the s M |
| L11 | **fatto et**; **fa dificu[l]ta** | yes except the pound-sign l | 0/20 ("fatto", "difficu_ta") | endorsed; "l" I |

### The two I signs (step 4)

- **Pound sign (X_POUND, 7 on D, all AB at H).** Printed-key letters only, with it unkeyed, every endorsed passage above
  still reads; it supplies only the l of "de[l]", "qua[l]che", "dificu[l]ta". Value fit on D ranks l first (-1.107;
  null -1.135, t -1.136; unkeyed -1.123), a thin margin from 7 occurrences, and three of the seven sit where l makes a
  word. No gloss on this form exists. **Stays I.**
- **Double-barred oval (X_THETA2, 8 on D).** Unkeyed, "tanto dina_e in diue_se" still reads. With r it takes the value
  that (a) the fr.3252 f.36v period gloss gives it (HARVEST-D, two glosses), (b) the fit ranks first on D (-1.123; n
  -1.138), and (c) the printed table itself very probably gives: this verifier compared the sheet cell **S60, printed r
  row 1** (a small oval crossed by two bars) with the f.11r example (`witness_f36/f11r_double_barred_oval_x4.png`) and the
  shapes agree; one blind reconciler matched an instance to S60 unprompted. So the r is not an override but a missed match
  to a printed cell, backed by a period gloss. **Endorsed as S on the key, M on the sign** (the one-bar S69 f and S13 g
  are its look-alikes). This inference by eye should be carried back to f.11r and f.87 (named next step).

### Grades endorsed (D, 267 tokens)

S 146 (both raw passes and D agree at H), M 103, X_THETA2-as-r 8 (S on key, M on sign), I 7 (pound sign), U 3 (X_NEW).
H 0, C 0: a cryptanalytic result with a published key. The solver's "S 179" counted both passes agreeing at H before
adjudication; on the verifier's stricter rule 146. Not endorsed: "intencione", "auanti", "[p]ersuad[e]", "del", and
any l from the pound sign.

### Verdict, f.21v

| item | scope | class | key | text | confidence |
|---|---|---|---|---|---|
| f.21v L01 "tutto da", L03 "questa carica ... di qua", L04 "credo le ne", L05 "ceder uiuendo et seruend[o]", L09 "tanto di ... in diuerse", L11 "fatto et", "fa dificu[l]ta" | **recovered-passages** | **N3** | published | unknown | high that the key is right (z 5.7-6.6 on a blind D, 20/20 power, blind reader); moderate on each passage's letters |
| the rest of f.21v; continuous text | none | not classed | - | - | nothing read |

**N3 reason:** no reading or decipherment of this letter located in the families above; not N4 while the two Saluzzo
monographs and JSTOR are unread (as for f.11r).

**Safe sentence:** "Birago's letter to Nevers of 12 Oct 1570 (BnF fr.3251 f.21v) reads in part with Tomokiyo's published
Ceppo-Nevers key. On a verifier's value-blind transcription the key beats all 200 shuffled keys (z 5.7-6.6), and a blind
reader picks its decode out of 21. Passages recovered: 'questa carica ... di qua', 'credo le ne', 'ceder uiuendo et
seruend', 'tanto di ... in diuerse', 'fatto', 'fa dificu' (the next letter is an unglossed sign). No prior reading of this letter was located (search
logged in AUDIT.md, 29 Sept 2026)."

**Unsafe:** "f.21v deciphered"; any continuous translation; "intencione" or "auanti qualche" as read; the pound-sign l
as read; "first", "unpublished".

## f.35 (no.18, Birago to Nevers, Saluzzo 15 Nov 1570)

Novelty: see the shared search log above (29 Sept 2026); nothing located. Not N0.

### Blind re-reconciliation (step 2)

One Opus subagent, same protocol (crops, blind sheet, raw passes A and B only). `verify_d2/f35/passD.tsv`, 76 signs (L01
37, L02 39): both passes 67, sided with A 3, against both 6, nothing inserted or dropped; it excluded about seven
prose ascenders from the line below and the closing flourish, which neither pass had listed. **D agrees with the
solver's passC at 71 of 76 signs**; the five differences: S91 to S93 twice (L01 26, L02 1), S91 to S34 (L02 25), S53 to
S37 (L02 29, conf L, a prose stroke crosses it) and S65 to S80 (L02 36, barred 8). 2 X_POUND, 1 X_NEW, no double-barred
oval.

### Key test on D (`verify_d2/f35/control_D.txt`)

| seed | letters | real key | shuffles mean / max | z | rank of 201 | power control |
|---|---|---|---|---|---|---|
| 1 | 72 | -1.126 | -2.086 / -1.571 | 5.42 | **1** | 19/20, z median 4.25 |
| 7 | 72 | -1.126 | -2.065 / -1.542 | 5.01 | 1 | 17/20 |
| 23 | 72 | -1.126 | -2.082 / -1.623 | 5.96 | 1 | 17/20 |

D scores better than the solver's passC (-1.126 against -1.306; z 5.0-6.0 against 4.46). The power control at this
length is 17-19 of 20, so the test has power here and the key passes it. Judge on D, pasted:
```
FAIL language: score=-1.142, null_p99=-1.579, real_p05=-0.982, real_median=-0.821, mode=both, N=72
FAIL - ceppo-nevers-fr3251-1570s (a PASS is a gate for a verifier, not a reading; rule 10)
```

### Line by line against 20 shuffled keys read blind (step 3)

`verify_mk_blind.py verify_d2/f35/passD.tsv verify_d2/f35/blind 3529 X_THETA2=r`; one Sonnet reader, decodes file only.
**No text rated LANG.** The real key (TEXT 07) was rated SOME with "fino" (L01) and "come" (L02); one shuffle (TEXT 01)
was also SOME ("capa"); nineteen NONE. The reader did not see "non", "haue" or "fate" in the real decode. This differs
from HARVEST-D2's blind reader on passC, which picked the real decode as the only LANG text; on D it is not singled out
as prose.

```
L01    c_enonaosensohauefiuremidiiuihafino_e
L02    intfateetmiuongano_irficialicomeeinast
```

| line | phrase (solver) | forced by the key on D? | blind, in the 20 shuffles | verdict |
|---|---|---|---|---|
| L01 | non | yes | reader did not list it | a 3-letter scrap, not a reading |
| L01 | haue | yes | not listed | scrap |
| L01 | fino | yes | listed for the real key only; 0/20 | scrap (4 letters, common word) |
| L02 | fate et mi | yes | not listed | scrap |
| L02 | come | yes (on D; passC read "tome") | listed for the real key only; 0/20 | scrap |
| L02 | "...ficiali come" | "ficiali" on D rests on the S34 that D alone read (L02 25) | - | not endorsed; a possible "[u]fficiali" is a guess |

### The two I signs (step 4)

Two pound signs, both unkeyed; their value fit is flat (n and d -1.129, unkeyed -1.126), so no value can be chosen at
this count. No double-barred oval on f.35. Nothing on this folio depends on either override.

### Grades (D, 76 tokens)

S 47, M 26, I 2 (pound, unkeyed), U 1. H 0, C 0.

### Verdict, f.35

| item | scope | class | key | text | confidence |
|---|---|---|---|---|---|
| f.35 whole cipher passage (2 lines) | **none** | **not classed** (no passage read to class) | published | unknown | high that the printed key is the letter's key (rank 1/201 on a blind D, z 5.0-6.0, power 17-19/20); none on any reading |

The key test is a positive result on the key (the Ceppo-Nevers table does fit f.35), not a recovered passage: the words
it gives are isolated three- and four-letter scraps that a blind reader could not tell apart from a chance decode.
Nothing goes to the second-opinion queue.

**Safe sentence:** "Birago's letter to Nevers of 15 Nov 1570 (BnF fr.3251 f.35) is in Tomokiyo's published Ceppo-Nevers key:
on a value-blind transcription the key beats all 200 shuffled keys (z 5.0-6.0). The two cipher lines give only isolated
word scraps; no passage is claimed as read."

**Unsafe:** "f.35 read in part" with any word quoted as its content; "non haue ... fino ... fate" as a reading;
"officiali"; "deciphered".

## f.87 (no.45, Birago to Nevers, Saluzzo 9 May 1571)

Novelty: see the shared search log above (29 Sept 2026). Segre, *Emanuele Filiberto*, paraphrases Birago's worry in spring
1571 about Spanish troop movements near Alessandria from Venetian dispatches; it does not cite fr.3251 or print any
cipher passage. Nothing located. Not N0.

### Blind re-reconciliation (step 2)

Two Opus subagents (L01-L03, L04-L05), same protocol, on HARVEST-D2's tracked crops (the third, accepted crop cut).
`verify_d2/f87/passD.tsv`, 205 signs (L01 27, L02 45, L03 46, L04 44, L05 43): both passes 139, sided with A 31, with B
17, against both 18. Where the passes had split one written sign into two ids (t+3 as S52 plus a bar or X_NEW; loop+3;
the c-e-ij sign S76 as S32+S66), D merged them into one sheet cell, so D's positions drift from passC's after the first
merge in a line and a position-by-position comparison with passC is not meaningful on L02, L04 and L05. Both reconcilers
independently matched the double-barred oval to the printed cell **S60 (r)**: 4 positions in L04-L05 are S60 on D, and 3
more are X_THETA2 (keyed r); 1 X_POUND, 3 X_NEW, 1 '?'.

### Key test on D (`verify_d2/f87/control_D.txt`)

| sequence | letters | real key | shuffles mean / max | z | rank of 201 | power |
|---|---|---|---|---|---|---|
| verifier D, seed 1 | 193 | -1.439 | -2.072 / -1.785 | 5.30 | **1** | 20/20, z median 7.08 |
| verifier D, seed 7 | 193 | -1.439 | -2.080 / -1.682 | 5.07 | 1 | 20/20 |
| verifier D, seed 23 | 193 | -1.439 | -2.074 / -1.772 | 5.34 | 1 | 20/20 |
| (solver) pass A / pass B raw | - | -1.634 / -1.617 | - | 3.49 / 3.47 | 1 / 1 | 10/10 |
| (solver) passC adjudicated | - | -1.735 | - | 2.48 | 2 | 20/20 |

This reverses the solver's weakest number. On a value-blind reconciliation that reads the whole line against the sheet
(and merges the split signs), the key ranks first with z 5.1-5.3, above both raw passes. The solver's rank-2 merge came
from the two adjudicators picking one pass per split, not from the hand being unreadable. Judge on D, pasted:
```
FAIL language: score=-1.452, null_p99=-1.699, real_p05=-0.944, real_median=-0.828, mode=both, N=193
FAIL - ceppo-nevers-fr3251-1570s (a PASS is a gate for a verifier, not a reading; rule 10)
```
Well above the null (the solver's passC scored -1.723, at the null ceiling), still far from real prose.

### Line by line against 20 shuffled keys read blind (step 3)

`verify_mk_blind.py verify_d2/f87/passD.tsv verify_d2/f87/blind 8729 X_THETA2=r`; one Sonnet reader, decodes file only.
It rated TEXT 21 alone LANG, high confidence ("neandosecrezamente", "giorno", "onde", "randi"); five shuffles SOME with
one scrap each (nume, arte, chies, cente, tongo), fifteen NONE. TEXT 21 is the real key.

```
L01    l&immmgnorduadilfdla_ea
L02    _udirrandizimeu_eazimhecenmomtilpfoincpidam
L03    aamemagnaet&imsirnoredonalfonmochauendouazo
L04    uartirel&sracaroc_iaungiornoauantieilanozeme
L05    neandosecrezamenteconozo_orteondeciamchuno
```

| line | phrase | forced by the printed key on D? | in the 20 shuffles (blind) | verdict |
|---|---|---|---|---|
| L05 | **ne ando secre-amente** | yes; the r of "secre" is S60 (printed r); the next sign reads z, not t | 0/20; the reader's longest phrase | endorsed as "ne ando secre-amente" (the t is not read) |
| L04 | **un giorno auanti** | yes | "giorno" 0/20; "auanti" not listed by the reader but in no shuffle | endorsed; "auanti" M |
| L03 | ch'auendo | yes ("mochauendo") | not listed by the reader; 0/20 | M; a fragment, not endorsed as a passage |
| L05 | onde | yes | listed; 0/20 | a scrap |
| L03 | magna, L02 randi, L05 conozo | forced, but not words in context | - | not readings |

### The two I signs (step 4)

- **Double-barred oval.** On D, four of the seven are matched to the printed cell S60 = r by the reconcilers themselves,
  so on f.87 the r is mostly the printed value, not an override; "secre-amente" uses one of them. With all seven
  unkeyed the passage reads "secre_amente" and still stands. Value fit on D is flat (n -1.436, r -1.439, unkeyed -1.455).
- **Pound sign.** One occurrence (L04 18, "roc_ia"), unkeyed; nothing endorsed depends on it.

### Grades (D, 205 tokens)

S 113, M 84, X_THETA2-as-r 3, I 1 (pound, unkeyed), U 4 (3 X_NEW, 1 '?'). S60 positions are counted in S/M as printed
cells. H 0, C 0.

### Verdict, f.87

| item | scope | class | key | text | confidence |
|---|---|---|---|---|---|
| f.87 L04 "un giorno auanti", L05 "ne ando secre-amente" | **recovered-passages** (two short fragments) | **N3** | published | unknown | high that the key is right (rank 1/201 z 5.1-5.3 on a blind D, 20/20 power, blind reader); moderate on the fragments |
| the rest of f.87 | none | not classed | - | - | nothing read |

**Safe sentence:** "Birago's letter to Nevers of 9 May 1571 (BnF fr.3251 f.87) is in Tomokiyo's published Ceppo-Nevers
key: on a verifier's value-blind transcription the key beats all 200 shuffled keys (z 5.1-5.3), and a blind reader picks
its decode out of 21. Two short fragments read: 'un giorno auanti' and 'ne ando secre-amente'. No prior reading of this
letter was located (search logged in AUDIT.md, 29 Sept 2026)."

**Unsafe:** "f.87 deciphered"; "secretamente" as read (the t sign reads z); any account of who went secretly where; "first".

## Postmortem (all three)

- **The solver's per-folio numbers hold or improve on an independent blind transcription**: f.21v z 6.40 -> 5.7-6.6,
  f.35 4.46 -> 5.0-6.0, f.87 2.48 (rank 2) -> 5.1-5.3 (rank 1). The key is the letters' key on all three.
- **Over-claims corrected in NOTES.md** (pointer lines added to each HARVEST-D2 section): f.21v "intencione" and
  "auanti qualche" are not forced on D; f.35's "non, haue, fino, fate" are scraps that a blind reader does not single out;
  f.87 "secre[t]amente" supplies a t the sign does not give.
- **The double-barred oval is very probably the printed cell S60 (r, row 1)**, missed as "off-sheet" by every earlier
  pass: three independent verifier reconcilers matched it to S60 without prompting, and this verifier compared the
  shapes. Together with the fr.3252 period gloss (r) this makes the r a printed-key value with a period gloss behind it,
  not an I override. Carry it back to f.11r (four positions) in the next f.11r pass.
- The pound sign is still unglossed; it stays I everywhere.
- One process note: HARVEST-D2's reconciliation sent every split to a third reader who chose one side per position; on
  f.87 that produced a merge worse than either input. A reconciler who re-reads each whole line against the sheet (and
  can merge split signs) did better on all three folios.

## For the orchestrator (VERIFY-CEPPO-D2-1)

- status.json (the parent sets it; this audit does not edit it): target stays `partial`; results f.21v
  **recovered-passages N3**, f.87 **recovered-passages N3**, key `published` (Tomokiyo), text `unknown`; f.35 **none**
  (key fits, nothing read).
- NEAR.md (the parent's): if the target has or gets a row, add f.21v and f.87 at rank 1/201 on blind D (z 5.7-6.6 and
  5.1-5.3) and f.35 at z 5.0-6.0 with no passage. Named next step: re-run the f.11r key test and reading with the double-
  barred oval as S60 = r (printed), then a per-sign pass on the S49/S73 (n/null) and S23/S97 (n/a) look-alikes on f.21v,
  the two splits behind "intencione" and "auanti".
- Second-opinion rows queued: SO-CEPPO-F21V and SO-CEPPO-F87 (both N3). None for f.35.
