# BIR-OPEN-144 pre-registration (3 Oct 2026, 13:5x UTC, account-3 worker)

Brief `.claude/briefs/runs/2026-10-03-acct3-bir-open.md`, section BIR-OPEN-144. Same protocol as `PREREG-OPEN.md` (f.117r/f.168), applied to
nevers-birago-fr3251-1572 **f.144r** (no.73) only. Written and pushed **before any crop is cut or shown and before any score**.

## Questions (`prereg_open144.py`, seed 20261006; `opositions_f144r.tsv` = hidden truth)
- **Targets**: every token graded M in `../verify/reading_f144r_verify_tokens.tsv`: 36. (U 14 are X_NEW/off-key and are not asked.)
- **H decoys**: 36 of the 40 S tokens with transcription conf H (no A1 exceptions exist on f.144r), matched by top-1 sign where possible
  (only 6/36 same-sign: f.144r's M signs are mostly T83/T81/T95/T84, which have few H twins), else highest TX-DECODE ratio. Calibration on this
  leaf is therefore less sign-matched than on f.117r (36/74) -- said here before any answer exists.
- One reader part (`f144r`, all lines L03-L06), one fresh blind Opus subagent, 1 vision call (cap 2). `oblind_f144r.tsv` = qid, passage, pos;
  `oorient_f144r.txt` masks every question position `[qid]` alike (72 of 90 tokens are questions, so the orient file shows only 18 signs).
- Reader sees line crops + `harvest/sign_sheet_blind_1572.png` (ids only); answers a sheet id, OTHER (shape not on the sheet, described) or U, conf H/M/L.
- Crops in scratchpad only, A1-BIR-EYE's command (RESULTS.md, reproduces the committed crop boxes):
  `python3 tools/iiif_lines.py --image ciphers/nevers-birago-fr3251-1572/harvest/f144r/src_ark_12148_btv1b9060248g_f146_4350_800_3650_760.jpg --out $S/f144r --prefix f144r --max-width 1250 --overlap 50 --only-lines 3,4,5,6 --debug`

## Gates (`score_open144.py`, `oposnull144.py`, pushed with this file)
- **Calibration**: H decoys answered with their current sign / 36 >= **0.80** (U, OTHER = disagreement).
- Change rate on targets reported.
- **Lattice**: `../round2/r2_f144r_topk.tsv` base; targets take TX-DECODE candidates + reader answer at H 0.5 / M 0.3 / L 0.1; viterbi lam 4, beam 64,
  printed 1572 key, LM it16dip; baseline without answers reported.
- **Posnull**: `oposnull144.py` (200 shuffles, seeds 1000-1199) must PASS (real rank 1/201 and real S > shuffled p95).
- **Survivors**: reader sheet sign != current at conf H/M AND lattice picks it, leaf calibration + posnull pass.
- **Grade policy** (`2026-10-03-acct3-bir-apply.md`, as the brief applies it to f.144r): a survivor is written at **S only if A1-BIR-EYE's blind
  two-option pick at the same position is the same sign**; every other survivor is written at M (value change, reason names the one instrument).
  Open-read vs A1-BIR-EYE disagreements on any target A1 asked go to `sorter/focus.tsv`.
- `decode_open144.json` (exception_grade_overrides_conf true) -> `tools/decode_key.py --check`; judge `specs/nevers-birago-fr3251-1572.json` (it),
  reported, not a gate (partly circular).

No reading claimed beyond S, no H/C, no novelty classed.
