# AUDIT: decode-1162-modena-ambung-1492 (DECODE R1162)

Verifier: VERIFY-MOD1162, account 3, Opus, 3 Oct 2026, 14:38-14:4x UTC. Separate session from the solver (MOD1162,
account 2). Brief `.claude/briefs/runs/2026-10-03-acct3-verify-mod1162.md`.

Claim under audit (MOD1162 done line, ROOM.md 14:30 UTC): "decode-1168 Costabili key read on R1162 cipher groups, gate
PASS (G 0.729 vs band-shuffled key p99 0.525, max 0.559, 1000 draws; raw passes A 0.705 / B 0.645 also PASS); plaintext
of the groups is the leaf's own period gloss (C); reading C32 S10 M27 I5 U3."

## Item

Beltrame Costabili (Esztergom) to Eleonora d'Aragona, Duchess of Ferrara; dated on the leaf "27 fibr 1491" (DECODE:
27 Feb 1492; Ferrara year from 25 March would make these the same day). State Archives of Modena, Amb. Ung. b.2/20
no.6; DECODE R1162, 2 images (IMG_R1162_I5837_P1, I5838_P2). Italian clear letter with 15 short cipher runs on p.1
(77 signs: 7 letter groups of 62 signs, 8 dotted/short code groups); verso clear. Over most runs a **period interlinear
gloss** gives the plaintext: "il gouerno del arciuescouato d Strigonio", "la Regina", "sua M.ta", "pocha estima",
"d arciuescouo", "[lo] Seruipiana", "in pre...", "famiglia d arciuescouo", "ne comp...".

## 1. Re-derivation (rule 7)

| check | result |
|---|---|
| `python3 tools/decode_key.py ciphers/decode-1162-modena-ambung-1492 --check` | "tokens 77: C 32, I 5, M 27, S 10, U 3 / reading up to date", exit 0 |
| `python3 score_g.py --check` | "score_g.json, votes.tsv up to date", exit 0 |
| band-shuffle control, new seeds 50000-54999 (`verify_controls.py`) | G 0.7288; control mean 0.4198, p99 0.5254, max 0.6102; 0/5000 draws >= G |

Reading and G reproduce exactly from ciphertext.tsv + decode-1168's key.tsv; the control's p99 is unchanged on 5x the
draws with different seeds. **Re-derivation verdict: reproduces.** Caveat: the raw-pass figures (A 0.705, B 0.645) are
"scratch re-runs" -- the raw pass TSVs are not committed, so those two numbers cannot be re-derived from the repository
(rule 7 gap on a supporting figure, not on the reading).

## 2. Control audit (rule 3)

- **Can the control differ from the target on G?** Yes. G is LCS(decoded, gloss) per letter group, which depends on the
  *values* the key assigns; the control permutes values within grade bands, so it changes every decoded string. It is
  not orthogonal by construction (unlike bCAS/AX-5799). Coverage (95%) cannot change under the shuffle and was
  correctly reported as descriptive only.
- **Is the band shuffle too weak a null?** Tested with a frequency null (each sign an independent draw from an Italian
  letter-frequency string, 5000 draws): p99 0.5254, max 0.6102, 0/5000 >= G. Same verdict.
- **Gloss length inflation.** Several glosses are longer than the group under them (L01: 9 signs under a 35-letter gloss;
  L06_1: 11 signs under "Seruipiana et lo arciuescouo"), which inflates LCS for target and control alike. Re-scored with
  a *tight* gloss (only the words directly over each group: "il gouerno", "pocha" / "estima", "lo Seruipiana",
  "famiglia"): target G 0.7119 vs band-shuffle mean 0.2839, p99 0.4237, max 0.5085 (0/5000); frequency null p99 0.3898.
  The margin grows, not shrinks.
- **Normalization (PX-BRODEC).** `score_g.py`'s `fold()` lowercases, folds v->u and j->i and drops non-letters on both
  sides; only letter groups enter G, so the abbreviated code glosses ("sua Mta") never meet a spelled-out decode.
  One convention, both sides. Abbreviation in the letter glosses ("d" for "del") costs the target, not the control.
- **Gloss transcription independence.** gloss.tsv is blind pass A's reading of the gloss. Re-scored against DECODE doc
  3593's own gloss readings (transcriber "RP", 2020, made long before this key existed: "il go*ino d+ l ***noseoato d+
  strugonio", "pocha esima", "Lé semipiano di lo acivescovo", "mi prorepitio", "famiglia dl arcivescovo", "ne
  comprino"): G 0.7458 vs control p99 0.5254, max 0.5932, 0/5000. The result does not depend on which reader's gloss
  is used.
- **Is the gloss independent of the key?** Yes. decode-1168's key.tsv was rebuilt from *1168's* f.12r period gloss
  (column `source`), a different leaf three weeks later; 1162's gloss played no part in building it. The two glosses are
  presumably by the same Ferrara chancery, which is what makes them a fair test of "same key", not a circularity.
- **Reader contamination.** The reconciled ciphertext was made by a worker who had seen the key and DECODE's
  transcription (NOTES.md says so). The two raw blind passes also PASS (0.705, 0.645 vs their own p99 0.508, 0.484),
  so the result does not rest on the reconciliation -- subject to the uncommitted-raw-pass caveat above.
- **Second control.** The pre-registered different-envoy Modena control was not run (none on disk). Noted; the
  frequency null partly covers it (an arbitrary frequency-plausible key does not reach G).

Script and full output: `verify_controls.py` (run from this folder):
```
orig gloss, seeds 0-999: G=0.7288 ctrl mean=0.4186 p99=0.5254 max=0.5593 n>=G=0/1000
orig gloss, seeds 50000-54999: G=0.7288 ctrl mean=0.4198 p99=0.5254 max=0.6102 n>=G=0/5000
DECODE-3593 gloss, seeds 50000-54999: G=0.7458 ctrl mean=0.4036 p99=0.5254 max=0.5932 n>=G=0/5000
tight gloss, seeds 50000-54999: G=0.7119 ctrl mean=0.2839 p99=0.4237 max=0.5085 n>=G=0/5000
freq-null orig: G=0.7288 mean=0.4111 p99=0.5254 max=0.6102 n>=G=0
freq-null tight: G=0.7119 mean=0.2741 p99=0.3898 max=0.4576 n>=G=0
```
**Control verdict: sound.** The finding that decode-1168's sign key reads R1162's cipher groups survives every variant.

**Judge.** NOTES.md said the it16dip FAIL (-1.34) is "judge cannot decide" by rule 3's gloss paragraph. Corrected in
NOTES.md: the gloss scores -1.134, nearer real_p05 (-0.989) than the shuffled null (p99 -1.504), so here the judge does
separate genuine prose from noise to a degree; the decode's lower score reflects its 27 known M-graded misreads. Not a
negative on the key question (the judge does not test it), and G is the pre-registered gate.

**Grades (rule 4).** H 0, C 32, S 10, M 27, I 5, U 3 reproduce. C here means a sign whose 1168-key value agrees with the
leaf's own period gloss, or a code group read from the gloss directly over it: plaintext-from-the-document, correctly
C. An M-key sign that agrees with the gloss is graded S, not C -- an under-claim, left as pre-registered.

## 3. Novelty search (rule 10), 3 Oct 2026

| family | searched | result |
|---|---|---|
| (a) canonical edition | Berzeviczy 1914, IA `aragoniaibeatrix00berz` `_djvu.txt` (one fetch, 1.34 MB) grepped: "Costabil" (40), "pocha" (4, none ours), "estima", "Strigon", "famiglia" (0), "comperino/comprino" (0), "Seruipian/Servipian/semipian" (0), 27 Feb in 1491 and 1492; TOC 1491 (CXXVII-CXXIX) and 1492 entries read | no Costabili letter of Feb 1491 or Feb 1492; letter absent (agrees with GF4-BATCH19) |
| (b) sender/recipient correspondence | Berzeviczy is Eleonora's incoming series; Nagy-Nyáry stops 1490 (GF4-BATCH19); PPKE Labancz thesis and Verbum Lardi article (LANE N, read in full 24 Sept) | not there |
| (c) documentary editions | as (a)-(b) | not there |
| (d) holding archive / project pages | **DECODE R1162**: status "Partially decrypted"; doc 3593 (Transcription, marked Public, uploaded 2 Jan 2021) transcribes the cipher runs **and the period gloss as `<PLAINTEXT>`**, read on disk (`decode/DOC_R1162_D3593_3593.txt`). Vestigia (GF4-BATCH19): leaf not located | **plaintext of the cipher runs already transcribed and tagged as plaintext by DECODE since 2021** |
| (e) full text | Google Books API (key, `country=US`): `"pocha estima" arcivescovo` 0; `Costabili Strigonio 1491 cifra` 0; `"famiglia del arcivescovo" Strigonio` 34, none this letter; `Costabili Eleonora "1491" Esztergom lettera` 0 | nothing |
| (f) solver repos, blogs | on-disk `sources/cyphersolver`, `sources/bourdeau`: no Costabili/R1162 reading; GF4-BATCH19 (same day): Aymeloglu HEAD d2800bb lists R1162 only in decode-ranked.md, Bourdeau HEAD a439937 B2 "Costabili not checked", Cipherbrain/Cryptiana/Cipher Mysteries no hits | no prior attempt |
| (g) scholarship | OpenAlex (key): "Beltrame Costabili cipher" 0; "Costabili Esztergom 1492 Este diplomacy" 1 (Zambotti diary, 2023, not this letter); "Este cipher Hungary fifteenth century" 12, none this letter. Semantic Scholar (key): first two queries returned no total (no result list; possibly throttled, logged as unreachable for those two), third 2 (Láng 2018 "Ciphers in Hungary: the source material", already checked by GF4-BATCH19 -- no reading of this letter) | nothing on this letter |
| JSTOR | not queued: the plaintext is already established at N0 from the leaf and DECODE, so a JSTOR row cannot change the class | waived by verifier |

Requests: archive.org 1 (+5 be-api calls whose identifier filter returned no hit list, discarded), googleapis 4,
api.openalex.org 3, api.semanticscholar.org 3. No de-crypt.org request (doc 3593 read from disk).

## 4. Classification

| item | class | key | prior plaintext | prior decipherment | confidence |
|---|---|---|---|---|---|
| R1162 cipher runs, plaintext | **N0** | `period` | yes: the period interlinear gloss on the leaf itself (1491/92), transcribed and tagged PLAINTEXT in DECODE doc 3593 (2021) | yes: the period decipherer's gloss | high |
| R1162 signs read with decode-1168's key (same-key identification) | not a plaintext claim; a key-identity result, `period` key | -- | -- | no prior statement that 1162 and 1168 share a sign key located (searches above) | control-backed (G 0.729 vs p99 0.525, 0/5000) |

Key source: `period` -- decode-1168's key.tsv, rebuilt by us from 1168's own period interlinear gloss (f.12r), applied
here; the plaintext itself is this leaf's own period gloss. `text: known`.

**Safe sentence:** "The cipher runs in Costabili's letter of 27 Feb 1491/92 (ASMo Amb. Ung. b.2/20 no.6, DECODE R1162)
carry a period interlinear decipherment, already transcribed in DECODE's record; we checked that the sign key we rebuilt
from his 20 March 1492 letter (R1168) reads them, against shuffled-key controls (G 0.73 vs control p99 0.53)."

**Unsafe sentence:** "We deciphered / first read Costabili's 27 Feb 1492 letter." The plaintext was never unread: it is
glossed on the leaf and transcribed in DECODE since 2021.

SECOND-OPINIONS-QUEUE.tsv: no row (N0, below N3).

## 5. Postmortem

No over-claim in the solver's files about novelty: NOTES.md says the plaintext comes from the period gloss and does not
classify novelty. Two corrections made in NOTES.md: (1) the judge sentence (above); (2) a status-line pointer to this
audit. For the orchestrator: since the plaintext of every glossed run is on the leaf, the target's remaining work
(sign-label collisions, code groups `T o` and `.e.`, the clear text) is transcription/edition work, not decipherment;
whether the status word should move from `partial` (e.g. to `found-solved` for the cipher runs, with the clear text as
an edition gap) is the orchestrator's call, not changed here. Rule-7 gap to close cheaply: commit the two raw pass TSVs
so the A/B figures re-derive.

## Post-audit revision (MOD1162B, account-2 worker, 3 Oct 2026, carried in under rule 10)
After this audit, MOD1162B (commit 0250614f; pre-registration b928f2db) re-read the uncertain signs at native resolution.
8 of 19 conf-'?' signs were settled: six lost the '?' on an unchanged label, and two code-group signs were relabelled z -> 3
(`T o 3 o`). Every letter-group label is unchanged, so the decoded text, G (0.729) and the judge input are identical.
The band-shuffle control at fresh seeds 1000..1999 gives p99 0.525, max 0.576: PASS. Grades are now
**H 0, C 33, S 12, M 24, I 5, U 3** (were C 32, S 10, M 27). The re-derivation table above quotes the
pre-revision counts. The N-class (N0) is unaffected: the plaintext is unchanged. No SECOND-OPINIONS-QUEUE row exists for this
target (N0).
