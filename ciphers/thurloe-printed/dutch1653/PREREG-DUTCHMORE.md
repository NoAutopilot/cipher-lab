# PREREG-DUTCHMORE (LANE FAMILY-A2s, account 2, worker DUTCH-MORE, written 10 Oct 2026 20:2x UTC by date -u, before any score)

Brief: `.claude/briefs/runs/2026-10-10-ytbiz-family-1709-jobs.md` "### DUTCH-MORE". Nothing below has been computed when this file is pushed.

## Units, as found in the vol 1 djvu text (IA collectionofstat01thur, sha1 ac831b5b..., the b146/manifest.tsv copy)
The brief's units came from pairs_census.tsv's header parse. Read in the OCR on 10 Oct 2026, they are:
- **p.301** (the edition's "Thurloe I p. 30·1", p.92 n.2; brief "p.304"): Beverning to De Witt, London 17 June 1653 [O.S.] = 27 June N.S.;
  one run of 10 tokens <= 66 ("about our [run]") plus codes 289, 135, 190, 171, 128 (p.301) and 170 (p.302). **De Witt key unit.**
- **pp.316-317**: the four envoys to Griffier Ruysch, 4 July 1653: no run <= 66; one code, 128, with a Birch interlinear gloss
  ("Denmark"). Codes-only unit: goes to codes_over_100.tsv, nothing to decode.
- **p.418** (census row l.37383): Beverning (heading per census: to Nieuport at the Hague), 3 runs of tokens <= 66 plus codes 296-298,
  329, 369, 373, 434. **De Witt key unit.**
- **pp.324(326), 383, 466, 486**: letters of intelligence from J. Peterson in Holland to Thurloe (English, a 3-digit code to ~600,
  partly glossed interlinearly by Birch). Not the Dutch envoys' correspondence; the census heading parse picked the wrong heading.
  Out of family: logged, not transcribed.
- **pp.431, 500, 521, 575, 581** (Vande Perre family; 7 and 17 frequent): Aymeloglu's alphabet (3-29) already reads these
  (LANDSCAPE/THUR-DUTCH). **p.454** (Boreel 13 Sept, 168 116 11 16 ...): Boreel's own cipher (p.435 family).
  OCR-only screen under the De Witt key (below), not transcribed from the image.
Disclosure: reading the OCR I saw that the p.301 run and the p.418 runs 1 and 3 begin with letters that spell Dutch under the key
("han...", "zyn"); the transcription passes (Sonnet blind on crops + my eye read) are independent of the key.

## Statistic and control (the DUTCH-KEY fold, unchanged)
Same as PREREG-DUTCHKEY "Supporting folds": letter 4-gram model (gate_dutchkey.py `model()`, same training pages, same nl16),
decode vs the same 1000 key permutations (seed 20261010). A page **supports** the key iff its decode beats the control max.
**Power check (rule 3, subsample to the target's N):** for each De Witt-key page with N decoded letters, 50 synthetic texts of
N letters cut at random offsets (seed 20261011) from the held-out edition page p.108 (OCR, normalized), enciphered under the key with
random homophones, scored by the same statistic against the same 1000 permutations; power = share of the 50 that beat the control max.
If power < 0.80, the page's fold result is "non-test at this N" (neither support nor negative), and any reading of that page rests
on the English-context check below, graded as stated there.
English-context check (reported, not gating): Birch's English translation around each run, quoted next to the decode.
Grades: H = in-key token on which both passes agree (published key); M = disputed token, codes > 66.

## OCR-only screen (Vande Perre p.431/500/521/575/581, Boreel p.454)
Tokens <= 66 parsed from the djvu lines (script, OCR as is; unparseable tokens dropped and counted); the same fold statistic and
1000 permutations, per page and pooled for the Vande Perre pages. Outcome logged as "De Witt key: supports / does not beat control max"
conditional on the OCR (rule 2). No reading is claimed from the OCR screen in either case.
