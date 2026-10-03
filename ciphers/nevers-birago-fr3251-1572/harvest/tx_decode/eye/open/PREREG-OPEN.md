# BIR-OPEN pre-registration (3 Oct 2026, 13:00 UTC, account-3 worker)

Brief `.claude/briefs/runs/2026-10-03-acct3-bir-open.md`. Written and pushed **before any crop is cut or shown and before any score**.
The different instrument BIR-ROUND2 named (rule 3, third-attempt clause): an **open-choice** blind re-read of the M positions against the
whole printed-key sign sheet, not an A/B choice between two lattice candidates; then one lattice pass. Leaves: f.117r (fr.3252 no.77) and f.168 (fr.3251).

## Questions (`prereg_open.py`, seed 20261006; `opositions.tsv` = hidden truth)
- **Targets**: every token graded M after A1-BIR-VERIFY (`../verify/reading_<leaf>_verify_tokens.tsv`): f.117r 74, f.168 22.
- **H decoys**: the same number of tokens graded S from a conf-H transcription row (not one of the 24 exceptions), matched to the targets
  by top-1 sign where possible (f.117r 36/74 same-sign, f.168 7/22), else by highest TX-DECODE lattice ratio (the most ambiguous H rows).
- Reader parts (one fresh blind Opus subagent each, 3 vision calls): f117a (L01-L05: 43 targets + 37 decoys), f117b (L06-L10: 31 + 37), f168 (22 + 22).
  `oblind_<part>.tsv` carries qid, passage, pos only (no candidate). `oorient_<part>.txt` shows the top-1 sign at every position except
  the part's questions, all masked `[qid]` alike. The reader never sees the current sign at a question position, nor a key, decode, value or earlier read.
- The reader sees the line crops, `harvest/sign_sheet_blind_1572.png` (ids only) and answers per qid with a sheet id, OTHER (a shape not
  on the sheet, with a short description) or U (cannot see / cannot locate), and conf H/M/L.
- Crops (scratchpad only, never the repo): f.117r at the original band height (A1-BIR-VERIFY's command, 30/30 boxes identical);
  f.168 with A1-BIR-EYE's f168r/f168v commands (RESULTS.md). Commands pasted in RESULTS-OPEN.md before the first call.
- At most 1 reconciliation unit (by me, no extra vision call unless a part fails to return).

## Gates (`score_open.py`, pushed with this file)
- **Reader calibration (per leaf):** H decoys answered with their current sign / all H decoys (U and OTHER count as disagreement) **>= 0.80**.
- Change rate on targets is reported (same / changed to another sheet id / OTHER or U).
- **Lattice:** `../round2/r2_<leaf>_topk.tsv` base (24 S and H pinned); each target takes the TX-DECODE candidates plus the reader's answer at
  weight H 0.5 / M 0.3 / L 0.1, renormalised; `tools/key_decode_lattice.py` viterbi lam 4, beam 64, printed 1572 key; LM fr (f.117r), it16dip (f.168).
  The same lattice without the reader's answers is the baseline, reported.
- **Posnull:** `oposnull.py` (A1-POSNULL / r2posnull, input lattice = `olat_<leaf>_topk.tsv`; 200 shuffles, seeds 1000-1199) must PASS (real
  key rank 1/201 and real S > shuffled-S p95).
- **Survivors:** target positions where the reader chose a sheet sign different from the current one at conf H or M AND the lattice chooses
  that sign, on a leaf whose calibration and posnull both pass -> applied at S via `exceptions_open_<leaf>.tsv` (on top of the 24), then
  `tools/decode_key.py --check` and `tools/judge_plaintext.py` (fr f.117r, it f.168). Everything else stays M. A leaf failing calibration keeps none.
- Caveat fixed in advance: the judge gain is partly circular (the lattice uses the same LM); it is reported, not used as a gate.

No reading claimed beyond S, no H/C, no novelty classed.
