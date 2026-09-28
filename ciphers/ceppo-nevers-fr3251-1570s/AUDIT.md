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
