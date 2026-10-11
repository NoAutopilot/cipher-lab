# PREREG F143-DEC2 -- decode-level key-family test on BnF fr.3988 f.143r L05-L08 (11 Oct 2026)

Worker F143-DEC2 (LANE DEFAULT-A2-0509, account 2). Brief: `.claude/briefs/runs/2026-10-11-ytbiz-default-0509-jobs.md`
"### F143-DEC" as amended by "### F143-DEC2" (orchestrator's option (a): L05-L08 from `keyhunt_f143/img/c304_reg.jpg`;
reverse Mayenne arm replaces the Mayenne-key arm). Written and pushed before any transcription made in this job is decoded
and before any score is computed. Disk only.

## Crop step (pasted)
```
python3 tools/iiif_lines.py --image keyhunt_f143/img/c304_reg.jpg --out keyhunt_f143/dec/crops --prefix f143 --debug --max-width 1800
  region 3500x700, 8 lines, 8 bands x 3 segments; pitch 94 distance 65 prominence 106.5
  centres (region y): 20 120 209 299 395 481 565 677 ; wrote 24 crops
python3 tools/iiif_lines.py --image keyhunt_f143/img/m61_reg.jpg --out keyhunt_f143/dec/crops_m61 --prefix m61 --debug --max-width 1800
  region 3344x1430, 11 lines, 11 bands x 2 segments; pitch 125 distance 87 prominence 207.0 ; wrote 22 crops
```
Overlay checked by eye: detector lines L05-L08 of c304 are KH1-F's L05 ("12 6 // x x"), L06 ("16 //"), L07 ("y r f ++"),
L08 ("q h 3 X"). Only crops f143_L05..L08_s1-3 go to readers. m61: all 11 line crops (clear text mixed with cipher; readers
transcribe only the cipher signs).

## Material
- Target T: f.143r L05-L08. Blind pass R: one fresh Sonnet subagent, key60 tag list only (tools/keys/key60.tsv sign column +
  tools/keys/key60_atoms.md shapes), no values shown, no other pass shown. Blind pass P: KH1-F's existing `keyhunt_f143/passP.tsv`
  rows L05-L08 (made 7 Oct 2026, before any decode existed). passQ (KH1-F, L06-L08 only) is reported as a third read, not gated.
  One fresh pass instead of two: the cap (5) does not hold two fresh f.143r passes plus the Mayenne pass; P is an existing
  blind pass of the same lines.
- Reverse arm M: BnF fr.4715 f.61r (Mayenne 1592 key, 16-slot table, NOT no.60), `img/m61_reg.jpg`; one blind Sonnet pass
  with the same key60 tag list and the same instructions (pass M).
- Positive control C (added, CPU only): fr.3986 f.152 (leaf 298, no.60 known, interlined), `ciphers/fr3986-nevers-revol-1593/
  atlas_heldout/heldout298_passD.tsv` (blind, 145 tags) -- a real no.60 text read by a blind reader into the same tags.

## Decode
Each tag -> key60 value (first value of `a|b`; word values kept as letters; NULL and tags not in key60, NEW:*, ?, dropped
identically in every arm). Letters concatenated in reading order across lines.

## Statistic and arms
S = `tools/judge_plaintext.py` NgramModel(LANG_CORPORA["fr16"]).score(): mean log10 P(letter | 3 previous), 4-gram, fr16 =
Catherine de Medicis Lettres t.1-2 + Marguerite de Valois (16th-century French letters; the best era match in tools/data for a
1593 royal letter). Caveat on file: fr16's leave-one-file-out fold spread is 1.5-71.5% (MQS-LANGS), so absolute PASS/FAIL
against real-text p05 is of unknown reliability; this test uses S only comparatively (same corpus, same N, key60 vs controls).
- Arm (i): 1000 value-shuffled key60 keys (values permuted across the key's 365 signs, seed 1), applied to the same pass.
  Per pass: p95 of S over the 1000.
- Arm (ii) reverse: S(key60 decode of pass M).
- Arm (iii) positive control: S(key60 decode of C) vs C's own 1000-shuffle p95.
The judge CLI (`judge_plaintext.py` with a fr16 spec) is also run on each key60 decode and its verdict line reported.

## Gate (registered)
1. Non-test if S(M, key60) >= T's shuffled p95 for either pass R or P (the judge does not separate key families at this N).
2. Non-test if S(C, key60) <= C's shuffled p95 (the judge cannot see a real no.60 text read by a blind reader at this N).
3. Otherwise PASS iff, for BOTH pass R and pass P: S(T, key60) > T's shuffled p95 AND S(T, key60) > S(M, key60).
   FAIL if neither pass clears; SPLIT (reported as not passed) if one clears and the other does not.
A PASS licenses only "the leaf decodes under no.60 better than controls", not a reading. Tokens are graded (rule 4) only if
the gate passes. Reported in addition (not gating): M against its own 1000-shuffle p95; pass Q on L06-L08.
Script: `keyhunt_f143/dec/score_dec2.py` (exit non-zero if the committed `score_dec2.txt` is stale).
