open

Next step before any deep work: check-solved (`.claude/briefs/check-solved.md`, with its Premise check) and
`python3 tools/intake_gate_check.py wvo-11008-certain-1572`. This folder was opened by a KEYHUNT worker from a
held-key test only; no check-solved verdict exists yet.

# WVO 11008: Willem van Oranje ("George Certain") to Lodewijk van Nassau ("Lambert Certain"), Keulen, 12 Aug 1572

Found by KH2-D (LANE KH-2, account 2), 7 Oct 2026 18:17-18:3x UTC by `date -u`, brief
`.claude/briefs/runs/2026-10-07-acct2-kh2-workers.md` (KEYHUNT: unread siblings of keys already held).

## Source

- WVO record https://resources.huygens.knaw.nl/wvo/app/brief?nr=11008 (read 7 Oct 2026). Inhoud: "Behoefte aan
  geld. Vorderingen van de veldtocht." Incipit "J'ay recheu ce jourduy les deux vostres du 5 et 7 du courant, vous
  remerchiant". Opmerkingen: written as a merchant's letter from George Certain (= the prince) to Lambert Certain
  (= Lodewijk); address "Au s.r Lambert Certain, nostre bon amy et compere estant pour le present a Tournay".
  **The remarks do not mention cipher**, which is why the 24 Sept 2026 WVO harvest (`sources/wvo/`, opmerkingen
  "cijfer") never listed it. Found here through an opmerkingen search for "koopman" (merchant).
- Holding: Koninklijk Huisarchief Den Haag, A 11/XI 15, original. Image: WVO PDF
  https://resources.huygens.knaw.nl/media/wvo/images/11000-11999/11008.pdf (2 images; page 1 is one wide sheet
  3754x2096 px carrying the whole letter, page 2 the address). Manifest and the four crops used: `images/`.
- WVO gives no printed edition for 11008 (no GPA line). Sister letters in the same cover scheme are printed in Groen
  III: 5194 (pp.448-449, CCCLXIX, in cipher), 6222 (pp.450-451), 6223 (pp.451-452); "George Certain est le Prince
  d'Orange" is Groen III p.428's footnote.

## What is on the leaf

French clear text with five short runs of numbers separated by colons (54 numerals in all). The numbers are mostly
multiples of 3, the design of the printed 1572 Orange-Nassau table (`../jan-van-nassau-1572-75/key_1572.tsv`, same
values as `../orange-nassau-1572/key_nepveu.tsv`: a=3, b=6 ... u/v=60, y=69, z=72; other numbers null). No
interlinear gloss on the leaf.

## Transcription

`iiif_lines.py --image <page 1> --prefix p1 --lines-per-crop 3 --max-width 2000` (15 bands x 2 segments); bands
L01, L02, L07, L08 (8 crops) went to two blind Sonnet passes, one call each (`passes/passA.tsv`, `passB.tsv`).
`tools/reconcile_passes.py`: 51/57 aligned signs agree (89.5%), 6 disagreement columns; the worker settled them
from native-resolution crops of the page. Passes split only on run 3's first two numbers (damaged paper; A "36 36?",
B "2? 9?") and its fourth (36/38); the other runs agree except "?" flags. `ciphertext.tsv` (per token, conf H/M/L
and the clear words around each run), `ciphertext.txt` (one line per run).

## Reading under the held key (`decode.py`, `reading.txt`)

| run | context (clear text) | codes | reading |
|---|---|---|---|
| 1 | end of line 4 | 10 9 12 120 | c d [120] (120 outside the table) |
| 2 | line 5, before "lequel a faict charge pour ... 2000 escus" | 33 15 12 60 9 12 15 24 42 33 54 57 15 27 39 + 11 14 17 | **le duc de holstein** + 3 nulls |
| 3 | line 20, damaged, before "le Sr Dominique est venu" | 2? 9? 36 38 15 25 37 40 | c m e (uncertain) |
| 4 | line 21, "... [la balle marquée ◇] et s'est" | 15 51 36 60 69 12 15 39 + 40 44 52 31 | **ermuyden** (Arnemuiden, Zeeland) + nulls |
| 5 | "Arnoult est" ... "Or pour" | 60 33 21 54 54 27 39 21 24 15 39 43 | **ulgssinghen** = vlissinghen (Flushing) with code 21 (g) where 27 (i) is expected at position 3 |

Grade (rule 4): 54 tokens; H 39 (read from the period table: run 2 all 18, run 4 11, run 5 10), M 15 (run 1 4,
run 3 8, run 4 pos 5, run 5 pos 3 and pos 12). No C, S or I. Depth for the verifier (rule 4a): looks like D1
(scattered words; three names read, no clause) -- the verifier sets it.

## Control (rule 3) and judge

`python3 decode.py` (writes `control.tsv`; `--check` exits 1 if stale). Matched control: same 54 tokens, the 23
letter values permuted among the 23 letter codes (nulls fixed), 1000 seeded shuffles; three statistics a shuffled
key can change:

| statistic | real key | shuffle mean | shuffle p95 | shuffles >= real |
|---|---|---|---|---|
| mean log10 4-gram prob./letter, fr16 corpus, no word list | -1.435 | -1.813 | -1.576 | 6 / 1000 |
| letters covered by fr16 words (4+ letters) only | 7 | 2.23 | 8 | 100 / 1000 |
| letters covered by fr16 words + a place list written after the decode was seen (post hoc) | 23 | 2.23 | 8 | 0 / 1000 |

The 4-gram figure passes (real above the shuffle p95, p about 0.006); the word-cover figure without names does not
separate (the readable plaintext is almost all proper names, which the fr16 vocabulary lacks); the third row is post
hoc and is shown only for completeness.

`tools/judge_plaintext.py` with the fr16 corpora (temporary spec, `corpora` = the three tools/data/fr16 files), on
"le duc de holstein ermuyden ulgssinghen cme cd":

```
FAIL language: score=-1.648, null_p99=-1.402, real_p05=-1.098, real_median=-0.804, mode=both, N=39
FAIL - wvo-11008 (a PASS is a gate for a verifier, not a reading; rule 10)
```

A FAIL at N=39 on a names-only string; the judge's letter-shuffle null is not the key-permutation null above.

## Where it was not found (search log, 7 Oct 2026)

- `ciphers/` (no folder for 11008), `sources/wvo/cipher-letters-2026-09-24.tsv` (absent), `sources/decode/*.tsv`,
  `sources/cryptiana/`, `sources/cyphersolver/` (grep 11008 / Certain / Holstein: no hit for this letter).
- Huygens retroboeken, Groen *Archives* 1re série full-text search (`archives/search_in_text`): tome III
  "Lambert Certain" 3 hits (pp.428, 430, 431, other letters), "Holstein" 5 hits (none this letter), "Arnoult" 0;
  tome IV "Arnoult" 0, "jourduy" 0. Not searched: Groen's Supplément, Japikse, Gachard, Kervyn, any secondary
  literature, DECODE live listing, the solver repositories' live trees. No novelty claim (rule 10).

## Requests

resources.huygens.knaw.nl (whole KH2-D job): about 40 (WVO searches and detail pages, 6 PDFs, 6 retroboeken
searches), >= 2 s apart, no 403/429.

## Remaining gaps

- [ ] check-solved and intake gate (above); next: check-solved worker, ~$2.
- [ ] run 1 code 120 and run 3's damaged start; next: one more look at page 1 at native resolution, ~$0.5.
- [ ] 5194 (Groen III 448-449, same cover scheme, in cipher) as a known-plaintext check that the Certain letters use
  this table; next: transcribe 5194's runs and decode, ~$2.5.

## Escalation

Verdict: keep going (check-solved first).
