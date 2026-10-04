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
merge in a line and a position-by-position comparison with passC is not meaningful on L02, L04 and L05. The L04-L05
reconciler matched the double-barred oval to the printed cell **S60 (r)** on its own at all 4 of its positions; the L01-L03
reconciler kept it as X_THETA2 (3 positions, keyed r); 1 X_POUND, 3 X_NEW, 1 '?'.

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
  so on f.87 the r is in part the printed value, not an override; "secre-amente" uses one of them. With all seven
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
  pass: two of this audit's five blind reconcilers (f.21v L01-L06, 1 position; f.87 L04-L05, 4 positions) matched it to
  S60 without prompting, the other three kept it off-sheet, and this verifier compared the shapes by eye. Together with the fr.3252 period gloss (r) this makes the r a printed-key value with a period gloss behind it,
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

---

# Second audit of f.21v and f.87 (VERIFY-CEPPO-D2-2, adversarial, 29 Sept 2026)

Verifier: parent worker VERIFY-CEPPO-D2-2 (account 3, Opus 5.5, session_01D8vKpYAZrfF24zSt6NZSZM), a session separate
from the solver HARVEST-D2 and the first verifier VERIFY-CEPPO-D2-1. Brief `.claude/briefs/runs/2026-09-29-verify-ceppo-d2-2.md`;
model `.claude/briefs/runs/2026-09-28-parent-verify-ceppo-2.md` (the f.11r second audit above). Clock read with `date -u` at
01:13, 01:18 and 01:22 UTC, 29 Sept 2026. Scripts and outputs: `harvest/verify_d2_2/`. Transcription throughout: the first
verifier's value-blind D (`harvest/verify_d2/<folio>/passD.tsv`); key: Tomokiyo's printed Ceppo-Nevers table
(`published`, nevers_add1.png; our copy `harvest/sign_id_map.json`). f.35 is outside this audit (scope none, not re-audited).

## Verdict

| letter | second audit | passages endorsed (grades below) | class | key | text |
|---|---|---|---|---|---|
| f.21v (Saluzzo 12 Oct 1570) | **held** (one word held in part) | "tutto da", "questa carica ... di qua", "credo le ne", "ceder uiuendo et seruend", "tanto di", "fatto", "fa dificu"; "in diue-se" with its r and s M | **N3** (upheld) | published | unknown |
| f.87 (Saluzzo 9 May 1571) | **held in part** | "un gio[r]no auanti", "ne ando sec[r]e-amente": the bracketed r in each is the double-barred oval (M, period-gloss backed), not a clean letter | **N3** (upheld) | published | unknown |

## 1. Novelty, harder (step 1), both letters, 29 Sept 2026

Search run by one Sonnet search subagent on a query list written by this verifier (log copied to
`harvest/verify_d2_2/novelty_log.tsv`), the one lead checked by this verifier against the page image.

| family | what was searched | result |
|---|---|---|
| Google Books API (key, country=US), about 42 queries | Italian and French, not used before on this target: "viuendo et seruendo" / "vivendo e servendo"; "questa carica" Birago Saluzzo; "un giorno avanti" "secretamente" Birago; "ne andò secretamente"; "fa dificulta"; Birago Saluzzo "ottobre 1570" / "maggio 1571"; Birague Saluces "octobre 1570" / "mai 1571"; Birago Nevers Carmagnola / Savigliano / Pinerolo 1570; "fr. 3251" Birago; "ms. fr. 3251"; "français 3251" Nevers; "Birago" Nevers "fol. 21" / "fol. 87"; "Ceppo" chiffre Nevers; Nevers inventaire papiers Birague | **one citation of f.21** (below); otherwise only the BnF catalogues (1874-95), Boltanski 2006 (Ceppo named among Nevers's Italian domestics, no cipher text), *Bulletin italien* 1903 (cites fr.3251 fol.192, another letter), a Dogliani history (1922). No phrase of either decode found in print. |
| **Pascal, *Il Marchesato di Saluzzo e la Riforma protestante* (Sansoni 1960; Google Books vYgcAAAAMAAJ, snippet view)** | follow-up queries by this verifier: "aderenti ed intrinsechi amici" Birago; "pratiche segrete con gli ugonotti" Birago; "12 ott. 1570" Birago Nevers | footnote 6: "IBIDEM, fol. 21 (lett. di Lud. Birago al duca di Nevers, 12 ott. 1570)", supporting the text "... pratiche segrete con gli ugonotti contro qualche piazza del Marchesato, «havendoli per aderenti ed intrinsechi amici»", then "Il vago accenno contenuto nella lettera del Birago al duca di Nevers trova più chiara precisazione in un documento anonimo ...". **Checked against the image**: Gallica btv1b9060248g f22 (1 request, f.21r, the letter's first page, all clear text), lines about three-quarters down: "con le pratiche che tiene, maxime con Vgonotti, hauendoli per aderenti, et intrinseche amici, oltra l'esser temuto da i principali ... di Carmagnola". The quoted words are the letter's **clear text on f.21r**, not its cipher on f.21v. The same book quotes fol.82 (clear text). Whether Pascal says anything about the cipher lines is not visible in snippets. |
| Internet Archive (advancedsearch 4, be-api full text 5) | Saluzzo monographs; "Marchesato di Saluzzo" riforma; Boltanski Nevers; "3251" Birague; "Birago" "Nevers" "cifra"; "Birague" "chiffre" "Saluces"; "vivendo et servendo"; "viuendo et seruendo" | word-match noise only; the 0-hit phrase queries confirm no OCR'd print of the f.21v passage |
| OpenAlex (key, 4), Semantic Scholar (key, 2) | Birago Saluzzo 1570; Birague Saluces gouverneur; Nevers Saluzzo correspondence; Gonzaga Nevers cipher; Nevers cipher Tomokiyo | nothing on these letters; two titles not opened ("Altri che hanno servito Francia", 2023; "Des gens de cervelle et de service", 2021) |
| Tomokiyo, cryptiana.web.fc2.com | nevers.htm refetched (ff.21v no.11 and 87 no.45 listed without "with decipherment"; only ff.27, 39, 82 have one); code index for any other Nevers/Birago page | none |
| BnF finding aid cc49712p | f.87 no.45 "avec chiffre", 9 May 1571; **f.89 no.46, Birago to Nevers, also 9 May 1571, no cipher** | no decipherment catalogued; f.89 is a lead for a crib (below), not a print of f.87 |
| Solver repositories | fresh clones: Bourdeau (grep ceppo, 3251, birago, birague, nevers): targets/birago is f.119, its fr.3251 sweep found no decipherment; Aymeloglu (all files, not only decode-catalog.csv): no fr.3251 row | none. Forks aryasn2026 / arya1515 of cyphersolver seen in web results, not grepped |
| Web search (4) | Italian and French metadata queries; "Ceppo" Nevers Tomokiyo; "fr. 3251" Nevers Birague | BnF pages and Bourdeau's f.119 pages only |

Requests: googleapis.com about 45; archive.org 9; api.openalex.org 4; api.semanticscholar.org 2;
cryptiana.web.fc2.com 2; archivesetmanuscrits.bnf.fr 1; gallica.bnf.fr 2 (one proxy reset, one 200); github.com 2
clones; web search 4. No 429 or 403.

**Result.** No print of either letter's cipher text or of a decipherment was located: neither letter is N0 or N1 for
its cipher passages. But f.21v's letter is **not unread in print**: Pascal (1960) cites it and quotes its clear text.
The first audit's safe sentence "No prior reading of this letter was located" is too broad for f.21v; it must say
"of its cipher passages". Pascal's "vago accenno" (vague hint) is his word for the clear text's charge; no snippet
shows him reading the cipher. **Class N3 for both letters' cipher passages; not N4** while Pascal 1960 and Boltanski 2006
are unread in full (Pascal is the next book to read: its footnotes 6-8 sit on fr.3251 fols. 21, 62, 43).

## 2. Chance (step 2): `harvest/verify_d2_2/chance_d2.py` (seed 2129 f.21v, 8729 f.87)

Same design as the f.11r second audit: arm K = 1,000 keys with the printed value column permuted (homophone counts
kept) on D's real order; arm T = the real key on D's sign order permuted within each line (1,000); X_THETA2 = r as
the first audit read, pound sign and X_NEW unkeyed. Metric by script (no model): it16dip lexicon (14,166 types, count
>= 3, length >= 4); per decode the longest word, the distinct words of 6+ and of 5+ letters, and the lines carrying
two or more distinct 5+ words.

| folio | arm | longest >= real | 6+ words >= real | 5+ words >= real | lines with 2+ words >= real | chance maxima (6+ / 5+ / lines) |
|---|---|---|---|---|---|---|
| f.21v | real | 7 (uiuendo, diuerse) | 4 | 16 | 4 | - |
| f.21v | K, 1,000 | 0 | **0** | **0** | **0** | 1 / 4 / 1 |
| f.21v | T, 1,000 | 8 (7 letters: tentera, uedette, iersera) | **0** | **0** | **0** | 2 / 6 / 2 |
| f.87 | real | 7 (hauendo) | 5 | 11 | 3 | - |
| f.87 | K, 1,000 | 3 (esporre, maestro, farollo) | **0** | **0** | **0** | 1 / 3 / 1 |
| f.87 | T, 1,000 | 0 | **0** | **0** | **0** | 2 / 4 / 2 |

A single 7-letter word does come from chance (11 of 4,000 decodes); several words together never do (0 of 4,000 on
every count). As on f.11r, the T arm keeps the key's own letter mix, so what makes the passages is the order of the
signs, not the key's Italian-like letter frequencies.

**Blind reader** (one Sonnet subagent per folio, allowed only one Read of a prompt file holding 40 texts; answer key
kept elsewhere): the real decode, the 8 highest-scoring decodes of each arm (an adversarial pick from the 2,000), and
23 random chance decodes. f.21v: TEXT 25 alone rated LANG ("tutto", "questa ... diqua", "credo", "uiuendo ... seruend",
"tanto di", "fatto", "difficu_ta"); 39 NONE. f.87: TEXT 31 alone LANG ("neandosecrezamente", "giorno auanti"); two SOME
on a weak "conten-" scrap (both T-arm decodes, the key's own letters in shuffled order), 37 NONE. TEXT 25 and TEXT 31
are the real decodes (`reader_answer.json`). Results: `verify_d2_2/<folio>/reader_result.txt`.

**Chance does not produce these passages.** The first audit's claim holds for both letters.

## 3. Without the I signs and without the oval = r (step 3): `harvest/verify_d2_2/override_d2.py`

Four readings per line (`override_d2.txt`): AUD as the first audit (oval = r); NOOV with every double-barred oval
(X_THETA2 and the five positions D matched to S60: one on f.21v, four on f.87) and the pound sign unkeyed; STRICT = NOOV with every letter not
seen by both raw passes and D at H masked; and each raw blind pass (A, B) decoded alone. The pound sign was already
unkeyed in the first audit's reading, so no endorsed passage used it.

| folio | passage | NOOV (no override) | raw pass A alone | raw pass B alone | verdict |
|---|---|---|---|---|---|
| f.21v | tutto da | tuttoda | tuttode | **tuttoda** | holds |
| f.21v | questa carica | questacarica | questetcetri | **questacarica** | holds (B exact; A splits the a/et signs) |
| f.21v | di qua | diqua | dique | **diqua** | holds |
| f.21v | credo le ne | credolene | **credolene** | **credolene** | holds, both raw passes |
| f.21v | ceder uiuendo et seruend | cederuiuendoetseruend | **exact** | **exact** | holds, both raw passes, 21 letters |
| f.21v | tanto di | tantodi | **tantodi** | etatodi | holds |
| f.21v | in diuerse | indiue_se | indiue_ce | iadiue_ce | **held in part**: r is the oval, and s is D's S26 where both passes read S66 (c) |
| f.21v | fatto | fatto | gatto | **fatto** | holds |
| f.21v | fa dificu | fadificu | fadigicu | **fadificu** | holds |
| f.87 | un giorno auanti | ungio_noauanti | ungio_noauanoi | ungio_ntauanti | **held in part**: the r of giorno is an oval (D matched it to S60; both passes X_THETA2); "auanti" is D's, each pass has one letter off |
| f.87 | ne ando secre- | neandosec_e | neandosec_e | nqandosec_e | **held in part**: the r is an oval (as above) |
| f.87 | -amente | amente | amente | caente | holds |

On f.21v every endorsed passage but one is independent of both uncertain signs, and all but "tanto di" and "in diuerse" are
given exactly by raw blind pass B alone (the pass that never saw a key value); "credo le ne" and "ceder uiuendo et seruend"
by both raw passes. On f.87 both fragments stand as the same words with one gap each ("un gio_no auanti", "ne ando
sec_e-amente") and the gap takes r only through the double-barred oval.

**The oval = r, weighed adversarially.** For r: (a) the period interlinear gloss of fr.3252 f.36v (the same key, HARVEST-D)
glosses it r twice (one H, one M); (b) the printed table's cell r row 1 (S60) is a loop crossed by two horizontal bars:
this verifier cut it from nevers_add1.png at 8x and set it beside `witness_f36/f11r_double_barred_oval_x4.png`; the
structure agrees (the printed cell is narrower and slanted, the fr.3251 hand upright and rounder); (c) the key test
does not need it: with every oval unkeyed, D still ranks the key 1 of 201 (f.21v z 5.95 and 6.69, f.87 z 4.08 and 4.19,
seeds 1 and 7, power 10/10; `control_nooval.txt`). Against: the identification is by eye, and on f.87 all four S60
positions are D's alone (both raw passes left them off-sheet). Grade: **M** (S on the key, M on the sign), as the
first audit had it; not I. The passages that use it are endorsed with the r bracketed.

## Grades endorsed (unchanged from the first audit, restated per passage)

- f.21v (D, 267 tokens): S 146, M 103, oval-as-r 8 (M), I 7 (pound, unkeyed), U 3. H 0, C 0. In the endorsed
  passages: "in diue-se" r M and s M (D alone); every other endorsed letter is S or M with pass B agreeing.
- f.87 (D, 205 tokens): S 113, M 84, oval-as-r 3 (plus 4 S60 positions counted as M), I 1, U 4. H 0, C 0. In the
  endorsed fragments: "gio[r]no" r M, "auanti" M (D's), "sec[r]e" r M; the next sign reads z, not t.
- A cryptanalytic result with a published key: H 0, C 0 on both letters.

## Verdict per letter

**f.21v: held.** Novelty (step 1, above), chance (0 of 2,000 on every multi-word count; the blind reader picks the real
decode alone of 40), and the passages without the uncertain signs (all but "in diuerse" stand, most in raw pass B alone)
all hold. Class **N3**, key `published`, text `unknown`. Only "in diuerse" is reduced, to "in diue-se" with r and s M.

Safe sentence (replaces the first audit's for f.21v): "Birago's letter to Nevers of 12 Oct 1570 (BnF fr.3251 f.21v)
reads in part with Tomokiyo's published Ceppo-Nevers key. On a value-blind transcription the key beats all 200 shuffled
keys (z 5.7-6.6), no chance decode of 2,000 gives more than two words of six letters (the real decode gives four), and a blind reader
picks the real decode out of 40. Passages recovered: 'questa carica ... di qua', 'credo le ne', 'ceder uiuendo et
seruend', 'tanto di', 'fatto', 'fa dificu'. The letter's clear text is cited and quoted by A. Pascal, Il Marchesato di Saluzzo e la
Riforma protestante (1960); no prior reading of its cipher passages was located (search logged in AUDIT.md,
29 Sept 2026)."

Unsafe: "f.21v deciphered"; "in diuerse" as a clean word; "intencione", "auanti qualche", "[p]ersuad[e]"; any
continuous translation or account of the letter's subject; "first", "unpublished".

**f.87: held in part.** The key and the chance tests hold. The two fragments hold as words, but each carries one r that
exists only through the double-barred oval, which is backed by a period gloss in a sister letter and by the printed
cell's shape, not read cleanly here, and "auanti" is D's against both raw passes' one-letter-off readings. Class **N3**,
key `published`, text `unknown`.

Safe sentence (replaces the first audit's for f.87): "Birago's letter to Nevers of 9 May 1571 (BnF fr.3251 f.87) is in
Tomokiyo's published Ceppo-Nevers key: on a value-blind transcription the key beats all 200 shuffled keys (z 5.1-5.3;
4.1-4.2 with the uncertain double-barred sign left out), and a blind reader picks the real decode out of 40. Two short
fragments read: 'un giorno auanti' and 'ne ando secre-amente', where the r in each rests on a sign whose value r comes
from a period decipherment of a sister letter. No prior reading of its cipher passage was located (search logged in
AUDIT.md, 29 Sept 2026)."

Unsafe: "f.87 deciphered"; "secretamente" (the sign after "secre" reads z); any account of who went secretly where;
"first".

## Postmortem

- The first audit wrote that "un giorno auanti" is "forced by the printed key on D". It is not wholly: the r of "giorno"
  is the double-barred oval at L04 26, which D matched to S60 while both raw passes left it off-sheet. The fragment
  stands, with that r M. Corrected here and in the f.87 safe sentence; the first audit's section stays as its record.
- The first audit's f.21v safe sentence said "No prior reading of this letter was located". The letter is cited and its
  clear text quoted in Pascal 1960 (fn. 6, fol. 21); what was not located is a reading of its cipher. Both safe
  sentences now say "cipher passages".
- The first audit's f.21v safe sentence quoted "tanto di ... in diuerse"; "diuerse" carries two uncertain letters (the
  oval r and D's lone s). The sentence above drops it.
- Nothing else over-claims. Both queued second-opinion prompts (SO-CEPPO-F21V, SO-CEPPO-F87) carry the passage lists
  of the first audit; this audit updates them to the sentences above (rule 10 propagation).

## For the orchestrator (VERIFY-CEPPO-D2-2)

- status.json: target stays `partial`. f.21v: result `recovered-passages`, class **N3**, key `published`, text
  `unknown`, second audit **held**. f.87: `recovered-passages`, **N3**, `published`, `unknown`, second audit
  **held in part** (the oval r). f.35 unchanged (none).
- NEAR.md: if the target has a row, add f.21v and f.87 with: rank 1/201 on blind D (z 5.7-6.6, 5.1-5.3; 6.0-6.7 and
  4.1-4.2 with the oval unkeyed), 0/2,000 chance decodes per letter with two or more 6-letter words, blind reader 1/40
  on both. Named next step: a per-sign image pass on the double-barred oval in f.87 (L04 6, 26; L05 11, 28) and on the
  S26/S66 (s/c) sign of f.21v L09 22, by a fresh reader with the printed cell S60 beside it; then carry the oval = r
  back to f.11r (four positions).
- A crib lead for f.87 (not a novelty matter): the finding aid lists f.89 (no.46), another Birago letter to Nevers of the
  same day, 9 May 1571, without cipher. If it repeats the matter of f.87's cipher lines in clear, it is a known-plaintext
  test of "un giorno auanti" / "ne ando secre-amente". Named next step, cheap: fetch Gallica btv1b9060248g at f.89 and read.
- Not N4 for either letter while the two Saluzzo monographs (Boltanski 2006; *Il Marchesato di Saluzzo e la Riforma
  protestante*, 1960) are unread in full.

# AUDIT: f.21v look-alike settlements of CEPPO-SPLITS (VERIFY-CEPPO-SPLITS, 2 Oct 2026)

Verifier: worker VERIFY-CEPPO-SPLITS (account 2 for the account-3 orchestrator, Opus 5.5), a session separate from the
solver CEPPO-SPLITS (ffc4cb30). Brief `.claude/briefs/runs/2026-10-02-acct3-verify-ceppo-splits.md`. Clock read 21:49 UTC
at start. No decoding beyond re-derivation. No Gallica request and no subagent: every image was already on disk.
Evidence crops are in `harvest/f21v/lookalike/verify/`.

## 1. Do the glossed shapes match the f.21v tiles?

**Witness (fr.3252 f.36, same key and same hand, on disk).**
- Diagonal slash with one dot on each side and no crossbar: on f.36v L1 (`witness_f36/cited/v36top_L01_s1.jpg`, `_s2.jpg`)
  it stands at the two n's of "parlandone" and the n of "signor". The plaintext forces n there whatever the gloss
  letter looks like. At this scale the clerk's n and r glosses are hard to tell apart, which is why HARVEST-D left
  the sign as "S30/S49". So the n rests on the word, not on the gloss letter alone. Either way it is a letter and
  not a null, which is the S49/S73 question.
- Caret with a dot between the legs and a pointed apex: f.36r cipher line 3 (`verify/f36r_L3_dottedcaret_n_curledlambda_a_slash.jpg`,
  re-cut by this verifier from `witness_f36/c37_f36r_cipher.jpg`) is glossed with the clerk's n. Two signs later, a
  lambda with a curled top and no dot is glossed with the clerk's "^"-shaped a. That "^" is the same form glossed a over
  S45 and S80 in "parlandone", so the a reading is backed by the word.
- What this verifier did not reproduce: the solver's figure of 5 + 3 + 1 glossed instances. One instance of each caret
  form was re-read here, on f.36r line 3. The f.36v L4 caret was not re-read.

**f.21v tiles** (`harvest/f21v/lookalike/crops/`, read by eye at 4x):

| tile | form seen by this verifier | settled | agree? |
|---|---|---|---|
| L01.15, L03.7, L03.10, L03.14 | diagonal slash, a dot each side, no crossbar (the same form as the "parlandone" n's) | S49 n | yes, 4/4 |
| L09.6, L09.17 | pointed caret, clear pen dot between the legs | S23 n | yes |
| L09.1 | pointed caret, small dot between the legs | S23 n | yes |
| L07.27 | A-form (curl into a crossbar), dot to the right | S23 n | yes, on the A-form alone; the dot is outside the legs |
| L07.10 | pointed apex, feet like L09's; the dot is faint and grey | S23 n | yes, but this is the weakest of the nine (see below) |

L07.10 is the one tile where the two readings conflict. Verifier D (VERIFY-CEPPO-D2-1) read "only a faint paper speck,
no pen dot" and took S97. At 4x this verifier sees a small grey dot inside the legs, fainter than at L09. The second
feature also supports S23: the apex is pointed, as in every dotted caret. Three signs earlier, L07.7 (S97, both readers)
has the curled top that the f.36r clerk glosses a. On the witness, the pointed apex goes with the dot and the curled top
goes without it. The apex shape is used as a discriminator only on these two witness instances.

**Result: 9 of 9 settlements upheld.** L07.10 is upheld on the dot and apex together, and is flagged as the weakest.

## 2. Re-derivation (rule 7)

`python3 tools/decode_key.py ciphers/ceppo-nevers-fr3251-1570s --check` gives "reading up to date". f.21v: I 7, M 67,
S 188, U 5. f.11r, f.35 and f.87 are unchanged. All nine tokens are graded S in `reading_f21v_tokens.tsv` (n at each one).
The decode.json diff in ffc4cb30 only reorders the f.21v and f.87 blocks, and f.21v keeps its exceptions file. It does
no harm.

## 3. Control at fresh seeds (rule 3)

`harvest/decode_control.py f21v/passD.tsv --shuffles 200 --windows 20 --err 0.15 --extra X_THETA2=r` (`verify/control_seeds_11-13.txt`):

| seed | real key | shuffles mean / max | z | rank | power (err 0.15) |
|---|---|---|---|---|---|
| 11 | -1.111 | -2.078 / -1.620 | 6.55 | 1/201 | 20/20, z median 8.02 |
| 12 | -1.111 | -2.057 / -1.617 | 6.06 | 1/201 | 20/20, z median 8.12 |
| 13 | -1.111 | -2.061 / -1.695 | 6.69 | 1/201 | 20/20, z median 7.95 |

This reproduces the solver's 6.40-7.01. **Caveat (rule 3, "a control that cannot vary on the axis"):** the nine
settlements changed confidence only, not labels. passD's labels are passC's, so this test confirms the key on the
sequence and cannot test the settlements. The only evidence for the settlements is the shape check in section 1.

Judge, pasted (unchanged; the letters did not change):
```
FAIL language: score=-1.136, null_p99=-1.702, real_p05=-0.931, real_median=-0.824, mode=both, N=261
FAIL - ceppo-nevers-fr3251-1570s (a PASS is a gate for a verifier, not a reading; rule 10)
```

## 4. A tenth instance the settlement did not touch: L11.17

L11.17 (`verify/f21v_L11_17_dottedslash.jpg`) is the same diagonal slash with a dot on each side and no crossbar. Both
raw passes read S73 (A at L, B at M). passC and passD keep **S73 (null)**, but verifier D took S49. CEPPO-SPLITS
applied the shape rule only to A/B splits, so this instance was left out. If the rule holds, L11.17 is S49 (n). Its
letter falls just before the endorsed "fa dificu[l]ta" and leaves it intact either way. This verifier does not change it
(no decoding). Named step: either apply the rule to L11.17 or find an unglossed diagonal dotted slash in the fr.3252
witness, which would show that Birago also writes the null S73 in this form. The rule is only as good as that second
check. ~$1.

## 5. Decision on the counts and the two fragments

- **The endorsed f.21v count does not move to 188. It moves from 146 to 155.** 188 is the solver's grade: it counts
  passC tokens where both raw passes agree at H (179) plus these nine. This audit's endorsed figure has always used the
  stricter rule: both raw passes and the verifier's D agree at H, which gave 146. None of the nine was in the 146,
  because each was an A/B split. On the stricter rule each now counts as "settled by a period-gloss shape, checked by a
  second session", which gives 146 + 9 = **155 of 267**. D's choices at L01.15, L03.7, L03.10, L03.14 (S73) and L07.10
  (S97) are overruled by the witness. Both figures, 188 (solver rule, re-derived) and 155 (verifier rule), are reproducible.
- **"intencione" (L03.6-15): endorsed.** All ten letters are now S. The three n's rest on the dotted-slash shape, which
  the period clerk glosses as a letter in every instance read (an unglossed null instance has not been looked for; section 4). Under the null reading the passage reads "itecioe".
- **"auanti" (L07.7-12): endorsed with one letter M.** The n at L07.10 is S (the weakest of the nine, section 1). The
  second a, at L07.9, is S80 at M, an S65/S80 (et/a) split, the largest open pair on f.21v. Word endorsed, a M. It is not
  added to the safe sentence while L07.9 is M. "qua[l]che" stays I (pound sign).

Grades endorsed, f.21v (267 tokens): S 155 (verifier rule), M 94, oval-as-r 8 (S on key, M on sign), I 7, U 3. H 0, C 0.
This is a cryptanalytic result with a published key.

Class unchanged: **N3**, key `published`, text `unknown`. The two fragments' letters were already in the reading that
the 29 Sept audits searched. No new search was needed for them, and no class change follows.

Safe sentence (replaces VERIFY-CEPPO-D2-2's for f.21v): "Birago's letter to Nevers of 12 Oct 1570 (BnF fr.3251 f.21v)
reads in part with Tomokiyo's published Ceppo-Nevers key. On a value-blind transcription the key beats all 200 shuffled
keys (z 5.7-6.6), no chance decode of 2,000 gives more than two words of six letters, and a blind reader picks the real
decode out of 40. Passages recovered: 'intencione', 'questa carica ... di qua', 'credo le ne', 'ceder uiuendo et
seruend', 'tanto di', 'fatto', 'fa dificu'. The letter's clear text is cited and quoted by A. Pascal, Il Marchesato di
Saluzzo e la Riforma protestante (1960); no prior reading of its cipher passages was located (search logged in AUDIT.md,
29 Sept 2026)."

Unsafe: "f.21v deciphered"; "auanti qualche" as clean words; any continuous translation; "first", "unpublished".

## For the orchestrator (VERIFY-CEPPO-SPLITS)

- Verdict: **held** (9/9 settlements upheld; L07.10 weakest). Endorsed f.21v count 146 -> **155** (not 188).
  "intencione" endorsed; "auanti" endorsed with a M. N3 unchanged.
- PROGRESS.tsv "Birago f.21v" firm count set to 155 from this section. status.json is yours.
- SO-CEPPO-F21V (queued) carries the older passage list. It under-claims rather than over-claims, so it was left as is.
  Add "intencione" when you next touch the prompt.
- Next steps: L11.17 (section 4, ~$1); then the S65/S80 settle that NOTES.md already names, which would also firm up
  "auanti".

# AUDIT: f.21v L11.17 relabel S73 -> S49 (VERIFY-BIRAGO-SMALL, 3 Oct 2026)

Verifier: worker VERIFY-BIRAGO-SMALL (account 2 for the account-3 orchestrator, Opus 5.5), a session separate from the
solver BIRAGO-SMALL (2a750ceb). Brief `.claude/briefs/runs/2026-10-02-acct3-verify-birago-small.md`, item 1. Clock read
00:01 UTC at start. Disk only: 0 requests, 0 subagents. No decoding beyond re-derivation. No class change.

**Shape.** `harvest/f21v/lookalike/verify/f21v_L11_17_dottedslash.jpg` read by eye next to
`witness_crops/f36r_L4_curledlambda_a_dottedslash_n.jpg` (the glossed fr.3252 form) and the sheet cells on
`harvest/sign_sheet_blind.png`. The tile is a diagonal slash with one dot above-left and one below-right, no other stroke:
the same form as the witness instance glossed n, and the same form as L01.15, L03.7, L03.10, L03.14 already endorsed in the
155 (section 1 above). One point this verifier adds: the printed sheet's null **S73 is a different drawing**, a slash
*crossed by a vertical stroke*, with dots (the adjudicator's note at L01.15, "no crossing bar (S73 has one)", and the cell
itself). The tile has no crossing stroke. S49 and S30 on the sheet are horizontal dotted bars (÷); Birago's diagonal form
is closer to them than to S73's crossed form. So the label rests on two things: the glossed witness form (n), and the
absence of S73's distinguishing stroke.

**The second check (unglossed dotted slash in the witness): still not done systematically.** Two cited 2x witness crops
were looked at (`witness_f36/cited/r36_L12_s1.jpg`, `r36_L02_s2.jpg`): the one diagonal dotted slash seen (end of r36_L02_s2)
carries a gloss mark above it, and the crossed dagger-like forms on r36_L12_s1 are a different shape. No unglossed diagonal
dotted slash was found in those two crops; two crops are not a scan of the witness. The caveat VERIFY-CEPPO-SPLITS put on the
four L01/L03 tiles applies here unchanged, no more and no less.

**Re-derivation (rule 7).** `python3 tools/decode_key.py ciphers/ceppo-nevers-fr3251-1570s --check`: "reading up to date";
f.21v I 7, M 66, S 189, U 5 (f.11r, f.35, f.87 unchanged). L11 reads `t·mfatto[et]l·eramenfadificulta`; the endorsed
"fatto et" and "fa dificu[l]ta" are untouched. "eramen" is not endorsed as a word.

**Control.** The solver's decode_control at seeds 1-2 (z 6.43 / 6.95, rank 1/201, power 20/20) moves by +0.0014 on the key
score; it cannot tell null from n (the solver says the same). Not re-run here: on this axis the control cannot decide, and
the decision rests on the shape (rule 3, "a control that cannot vary on the axis").

**Decision.** Endorsed. L11.17 was not in the 146 strict base (both raw passes read S73, at L and M), so it enters the
verifier-rule count the way the nine CEPPO-SPLITS tiles did: **f.21v endorsed S 155 -> 156 of 267** (solver rule 189).
Grades endorsed, f.21v: S 156 (verifier rule), M 93, oval-as-r 8, I 7, U 3. H 0, C 0. Cryptanalytic result with a
published key. Class unchanged: **N3**, key `published`, text `unknown`. No passage added to the safe sentence.

## For the orchestrator (VERIFY-BIRAGO-SMALL, item 1)

- Verdict: **endorsed**, 155 -> **156**. PROGRESS.tsv "Birago f.21v" set to 156 from this section. status.json is yours.
- Still open (unchanged): a systematic scan of the fr.3252 witness for an unglossed diagonal dotted slash, which would be
  the one finding that reopens all five dotted-slash tiles (L01.15, L03.7, L03.10, L03.14, L11.17) together.

# AUDIT: f.87 hash and 8 relabels of CEPPO-WITNESS-PAIRS (VERIFY-CEPPO-WP, 3 Oct 2026)

Verifier: worker VERIFY-CEPPO-WP (account 2, LANE-A2PUSH, for the account-3 orchestrator), a separate session from the
solver CEPPO-WITNESS-PAIRS (1942dc4d, PREREG e1760f2e). Brief `.claude/briefs/runs/2026-10-03-acct3-verify-ceppo-wp.md`.
Clock read 01:39 UTC at start. Disk only: 0 requests, 0 subagents. No class change. The witness-rule check and the f.47r
ruling are in `../birago-fr3252-1571-72/AUDIT.md` (on the f.36v crop, this verifier's eye reproduces 3 hash glosses: slanted
= t, upright = o x2).

**Claim under audit.** 7 S candidates on passC (hash S88 -> S24 o: L03.25, L03.46, L04.29, L05.23; plain-8 -> barred-8
S65 -> S80 a: L02.7, L03.6, L04.21) and 3 relabels that contradict endorsed S tokens (L02.35 S24 -> S88; L04.41 and L05.42
S88 -> S24).

## 1. Tiles by eye
Zoom crops (3-4x, autocontrast) cut from `harvest/f87/c88_cipher_w.jpg` by passC neighbours; not committed.
- L03.25, L03.46, L04.29, L05.23: upright stem. L04.34 (slanted, the rule's own control) is plainly different. **Rule settles.**
- L02.7, L03.6, L04.21: the bar runs through the waist of the 8 and out past it on the right (on L02.7 and L03.6 it
  joins from the sign before, the same ligature seen on the f.36v witness). **Barred.**
- L04.41, L05.42: **upright** to this eye, as the solver says.
- L02.35: the sign is fused with the bar of the theta before it. The one stroke visible above the bars is near-vertical.
  This verifier **cannot see the slant** the solver reports: UNDECIDED.

**A third reader that never saw the rule.** The 29 Sept verifier's blind Opus reconciliation `harvest/verify_d2/f87/passD.tsv`
(VERIFY-CEPPO-D2-1) reads each of these tiles. D's positions drift by one on L04 and L05 after its merges, so they were
located by neighbours. D reads S80 at L02.7, L03.6 and L04.20 (= passC L04.21). It reads S24 at L03.25, L03.46, L04.28,
L05.23, at L04.40 (= passC L04.41) and L05.43 (= passC L05.42), and at **L02.35**. All of these are at M or L, with
notes such as "upright stroke with two bars" and "S24/S88 lean is the hardest pair". So D agrees with the rule on all 7
candidates and on L04.41 and L05.42, and **disagrees with it on L02.35**.
One more point, outside this brief: D reads passC L04.39 (where the solver kept a plain S65) as S80, "8 with bar through
waist". That is a further 8-family tile for the next pass.

## 2. Re-derivation and controls (fresh seeds 4-6; the solver used 1-3)
Scratch copies of decode.json (the f.87 job only) were built with the proposals applied, and `tools/decode_key.py` was run
on them. The 10-change copy reproduces the solver's `f87_reading_passE_hash8.txt` text. Key control at the two-reader error
0.28 (200 shuffles, 20 windows):
| sequence | real key | z seeds 4/5/6 | rank | power | in-family flips (1000; seeds 7 / 8) | judge |
|---|---|---|---|---|---|---|
| passC (as committed before) | -1.7352 | 2.64 / 2.78 / 3.23 | 2 / 2 / 1 | 20/20 | - | -1.723 FAIL |
| passC + 7 candidates | -1.6516 | 3.39 / 3.49 / 3.94 | 1/1/1 | 20/20 | 33/1000 p 0.033 / 34/1000 p 0.034 | **-1.655** FAIL |
| + L04.41, L05.42 -> o (9) | -1.6547 | 3.43 / 3.46 / 3.98 | 1/1/1 | 20/20 | 72/1000 p 0.073 (seed 7) | -1.658 FAIL |
| solver's 10 (+ L02.35 -> t) | -1.6372 | 3.54 / 3.60 / 4.16 | 1/1/1 | 20/20 | 28/1000 p 0.029 (seed 7) | -1.642 FAIL |
Same-position random-sign control, 500 draws, seed 7: 7 candidates 0/500 (p 0.002); 10 changes 0/500 (p 0.002).

## 3. Ruling
**Accepted: the 7 candidates, as S.** All three pre-registered gates hold at fresh seeds: (i) the rule settles each tile,
confirmed by this eye and by blind reconciler D; (ii) rank 1/201 with power 20/20 on every seed; (iii) the judge improves
(-1.723 -> -1.655). The in-family control passes at p 0.033-0.034. That is marginal, so the acceptance rests on the shape
evidence, which two eyes and D give independently. The control is support, not the ground.

**Conflicts (rule 4: both readings recorded, not settled by counting heads):**
| token | t (S88) supported by | o (S24) supported by | stands |
|---|---|---|---|
| L04.41 | passC readers A and B (blind Sonnet, sheet matching, agreed, H); the language score (-1.6516 with t vs -1.6547 with o) | witness shape rule (upright); solver's eye; this verifier's eye; D (M, "A S88 alt S24, B S88") | **t, graded M** (was S) |
| L05.42 | passC readers A and B (H); the language score | rule; both eyes; D (L, "both passes S88; hardest pair; line end") | **t, graded M** (was S) |
| L02.35 | the solver's eye (slanted); the language score (-1.6547 -> -1.6372, the largest single gain) | passC readers A and B (H); D (M); this verifier sees no slant | **o, stays S** |
Why: the shape evidence is the stronger kind. The readers matched a sheet and on f.47r they systematically labelled upright
hashes S88, so their agreement here is a shared bias, not two independent votes. But pre-registered gate (iii) fails for
o at L04.41 and L05.42 (the score gets worse), so o cannot be promoted. The endorsed t loses its S because its shape is
contested. At L02.35 the rule's own condition (i) is not met for this verifier, and D agrees with the endorsed o. So the
proposal there is rejected; the language gain for t is recorded but does not decide it.

**Applied** to `harvest/ciphertext_f87.tsv`: 7 tokens set to the rule label at conf H, and L04.41 and L05.42 dropped to
conf M with their value unchanged. Regenerated with `tools/decode_key.py` ("reading up to date" with `--check`), plus
`reading_f87_letters.txt`. Solver-rule tokens: S 134 -> **139**, M 66 -> 61, U 4. Reading: L03 "...nores**o**nal...
auendouaz**o**", L04 "...oci**a**ungiorn**o**auanti..." ("un giorno auanti" now in full), L05 "...con**o**zoorte...".
The L02 change is "a" for "[et]". Judge on the committed file, pasted:
`FAIL language: score=-1.655, null_p99=-1.623, real_p05=-0.947, real_median=-0.833, mode=both, N=194`.
`harvest/f87/passC.tsv` is left as the record of passC.

**Endorsed count (verifier rule, D-based as before):** all 7 accepted tiles sit at M/L in D's 113, so they enter the
verifier-rule count the way the CEPPO-SPLITS tiles did on f.21v. **f.87 endorsed S 113 -> 120 of 205.** The two contested
tokens were already M in D, so the count does not change for them. Class unchanged: **N3**, key `published`, text
`unknown`. The safe sentence is unchanged. "un giorno auanti" was already in it, and the o is now read rather than supplied.

## For the orchestrator (VERIFY-CEPPO-WP, f.87)
- Verdict: **7 accepted** (113 -> 120). L04.41 and L05.42 are **contested**: t stands at M, o is recorded. **L02.35 rejected**
  (o stands, S). PROGRESS.tsv "Birago f.87" set from this section. status.json is yours.
- Open: passC L04.39 (D reads a barred 8, S80); L05.28 is undecided. A legible f.36r/f.37r gloss over an upright hash at
  a line end would bear on L05.42.


## JSTOR (owner's machine, 3 Oct 2026)

All 13 queued JSTOR-QUEUE.tsv rows for Birago (137-138, 141-150, 155; both families: name/date/place + cipher keyword, and
bare quoted phrases from the readings) run by the owner's desktop session in a browser signed in to JSTOR, about 05:2x UTC,
no captcha or block page. The six quoted-phrase rows (142, 144, 146, 148, 150, 155) returned 0 results each. Name/date rows
returned only indexes, bibliographies and a different Birague (René, in Bernus 1888 on Antoine de Chandieu). The one full-text
candidate, "DOCUMENTI", Archivio Storico Italiano 122 (1964), https://www.jstor.org/stable/26252393, was read in the online
viewer: Medici envoys' letters from the Council of Trent, Oct 1561-1563, so it cannot print the 1572 letters. Result: nothing on
JSTOR prints or discusses Birago's 1572 cipher letters or their decipherment. Class unchanged (N4 stands; outreach gate 2's JSTOR
condition is now met for this target).

## f.87 grade note (A1B-CEPPO-87, 3 Oct 2026; solver-side propagation per rule 10, no class change)
passC L04.39 (the open item in "For the orchestrator (VERIFY-CEPPO-WP, f.87)"): two blind readers both see a bar through the
waist (R-8 -> S80 a, as blind reconciler D read); key control still rank 1/201, power 19-20/20, but the judge drops
-1.655 -> -1.657, so gate (iii) fails and S65 (et) stays, graded M (was H). Reading text unchanged; f.87 S 138 / M 62 / U 4.
SO-CEPPO-F87 prompt unaffected (letters identical). Details: NOTES.md "A1B-CEPPO-87".

Desenclos check, 4 Oct 2026 (DESENCLOS-PREMISE, account 3): no hit. Searched 17 open full texts of the 36 items in sources/desenclos/2026-10-04/bibliography.tsv (HAL PDFs, DSpace Tartu HistoCrypt 2024/2025 PDFs, OpenEdition HTML; built from HAL, theses.fr, OpenAlex, Semantic Scholar, CrossRef, Google Books) for this item's shelfmark, sender/recipient, place and date (terms.tsv, search-log.tsv, search.py); none names this item, its key or its plaintext. Not read: her 2014 thesis (theses.fr: not online) and 2017/2021 cryptography chapters (not open; JSTOR-QUEUE rows of 4 Oct 2026).

## Depth (DEPTH-REGRADE, 4 Oct 2026)

Verifier DEPTH-REGRADE (account 3, session_015eezFKYThEoRKoeamyhxSD), rule 4a / verifier step 3a; nothing decoded or changed. % = cipher tokens graded H/C/S (clear text excluded; counts as the cited reading file or audit gives them, nulls excluded where the file marks them); when evidence for a level is not on file the level below is given.
- **BnF fr.3251 f.11r (Gallica btv1b9060248g canvas 12), no.6, Birago to Nevers, Saluzzo, 14 S**: **D1** (Non-decrypted; outward "fragments read"), 39.3% (S 53 of 135). Check: published key rank 1 of 201 (statistical only); word fragments, no clause. Class without a reading: not counted as a unique solve.
- **BnF fr.3251 f.21v (no.11), Birago to Nevers, 12 Oct 1570**: **D1** (Non-decrypted; outward "fragments read"), 58.1% (S 155 of 267). Check: published key rank 1 of 201; endorsed passages are phrases ('ceder uiuendo et seruend[o]'), no clause above AD on file. Class without a reading: not counted as a unique solve.
- **BnF fr.3251 f.87 (no.45), Birago to Nevers, 9 May 1571**: **D1** (Non-decrypted; outward "fragments read"), 58.5% (S 120 of 205). Check: published key rank 1 of 201; two short endorsed passages with M letters. Class without a reading: not counted as a unique solve.
