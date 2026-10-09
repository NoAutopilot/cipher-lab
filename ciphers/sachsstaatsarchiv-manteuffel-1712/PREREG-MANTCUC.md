# PREREG-MANTCUC (9 Oct 2026, 10:56 UTC by date -u; MANT-CUC worker, LANE FAMILY-A2h account 2)

Pre-registered before any code or clear read of these leaves is scored. Target: HStA Dresden 10026 Loc. 694/08 frames 0323
and 0348 (then 0282 and 0410 only if the cap allows): clear words underlined, code runs written ABOVE them (draft/instruction
pages). The clear word is the known answer; no gloss reading involved.

Inputs
- Strips: `mant0608/cuc/strips.tsv` (native boxes of every code run cut with tools/iiif_lines.py into f0323_08/cuc/, f0348_08/cuc/
  `c<leaf>_<strip>_L01.jpg`; the clear words under each run cut separately as `k<leaf>_<strip>_L01.jpg`). The code crops do not show
  the clear word (checked by the worker's eye before the passes).
- Code reads: two blind Sonnet passes A and B per leaf over the code crops only (digits, '?' for unreadable), no key, no clear word.
- Clear reads: one blind Sonnet pass per leaf over the clear crops only (the underlined words), no codes, no key.
- The worker does NOT settle A/B digit disagreements before scoring; scored three ways: pass A alone, pass B alone, and the
  agreed tokens only (`tools/reconcile_passes.py` alignment; a disagreeing token is replaced by '?', which matches nothing).

Statistic (script `mant0608/cuc/cuc_score.py`, committed with this file)
- Letter-class strips: a run of >=2 codes, or a single code whose key.tsv value is <=3 letters. Name-class: a single code with a
  longer value (257, 177, 160): reported, not gated.
- Clear string normalised: accents stripped, lower case, letters a-z only. Codes aligned to it by DP, each code consuming 0-4 letters;
  a code scores 1 when its key.tsv value set (alternatives split on '|') contains the consumed substring. S = total matched codes.
  Codes absent from key.tsv match nothing.
- Excluded from the gate: 0348 s01 (run below a struck marginal phrase, no underlined word under it) and 0323 s10 (clear 'Czar'
  written above an in-line code: a gloss, not clear-under-code); both reported.

Control and gate
- Primary (the brief's): key.tsv values permuted among all 180 codes, 1,000 permutations, seed 6083. It changes values, so it can
  differ from the target on S. Gate: S_real > p99 of the permuted S. Secondary (must also pass for an unqualified PASS): values
  permuted among letter-class codes only (value <=3 letters), same count and seed.
- Reported per leaf and pooled, per pass (A, B, agreed). Primary result = agreed tokens, pooled over the leaves read.
- Runs whose concatenated key values equal the clear word exactly (some choice of alternatives) are shown in the per-strip lines
  (score n/n), descriptive.
- Codes absent from key.tsv or not matched in the alignment go to `mant0608/cuc/cuc_candidates.tsv` with the aligned clear substring,
  grade C (from the clear word), never into key.tsv.

What would count against the key: a FAIL of the primary gate with both passes, or a per-token match rate on agreed tokens below 0.5.
