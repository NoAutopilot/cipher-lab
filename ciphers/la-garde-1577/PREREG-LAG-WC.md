# PREREG-LAG-WC: `wordcode` at the measured marks-kept error, matched control first (LAG-V2, 9 Oct 2026, account 2, LANE FAMILY-A2f)

Written and pushed before any wordcode score at these error levels is computed. Target: `specs/la-garde-1577.json` as rebuilt
by LAG-V2 (v2 carrying LAG-MARKS' 7 sure mark settles; 239 tokens, 48 code^mark types; base codes unchanged).

**Measured error used.** One-reader marks-kept error from `lag_marks.tsv` (LAG-MARKS, passes unchanged by LAG-V2): central
**0.071**, upper **0.125**. The revised v2 against the same settles reads 0.000 central / 0.067 upper (LAG-V2 row in
`lag_marks.tsv`), but v2 is built from those readers and shared misreadings are invisible to it, so the reader figure is the
one injected. WC-LAGARDE2's only wordcode row ran the control at 0.23 (mean 0.321, below gate).

**Runs (in this order, nothing else):**
1. `python3 tools/family_run.py specs/la-garde-1577.json --family wordcode --seeds 3 --measured-error 0.071 --param codes=marked
   --param err=0.071 --gate 0.6 --label "LAG-V2 wordcode err 0.071"` -- control first; family_run.py runs the target only if the
   3-seed control mean >= 0.60 (else CONTROL BELOW GATE, exit 3, target untouched).
2. Bracket, only if run 1's control met the gate and time remains under 80% of the box: the same command at `0.125`
   (control first, same gate). If run 1's control is below the gate, run 2 is not run (a control that fails at the central
   error cannot be rescued by a higher one).

**Read-out (fixed now):**
- Control mean < 0.60 at 0.071: wordcode is **untestable by this tool at N=239 and err 0.071** (not refuted). Since this is
  the second wordcode attempt on this target and the only knob changed is `err`, rule 3's third-attempt clause applies to
  any further attempt: the next one needs a different instrument or new material (pooling), not a third err level.
- Control mean >= 0.60: the target decode family_run.py writes is reported **descriptively only** (its judge line pasted).
  No reading, grade or coverage claim is made from it: a control-backed negative or positive for wordcode needs the
  LAG-GAP/LAG-SYL score-gap gate (target score vs shuffled targets and vs controls at the bracketing errors, power check
  on held-out controls), pre-registered as its own amendment in a separate job.
- Coverage: a wordcode statement covers the target only if a control at >= 0.125 (the upper) also meets the gate.

Recovery statistic, seeds, restarts, corpus: family_run.py defaults for wordcode (seeds 1-3, restarts 8, the spec's fr16
corpora), the same as WC-LAGARDE2 apart from err.

## Amendment 1 (LAG-RESCORE, 9 Oct 2026 05:1x UTC; written and pushed before any gate score is computed)

The score-gap gate the read-out above names, at err **0.071** only (the control met the gate there, 0.777, and failed it at
0.125, 0.527). Same family, params (`codes=marked`), solver (restarts 8, defaults), corpora (the spec's fr16 pair), spec (LAG-V2).

- **Statistic: the judge language score** of a decode, J = `judge_plaintext`'s NgramModel(spec judge corpora).score(fold(decode
  text)), the decode text being `wordcode.split_decode` joined by newlines (the same number the judge prints; LAG-V2's target
  decode reproduces at J = -1.121). Reported as the **gap = J(T) - mean J(a)**.
- T: the spec ciphertext, solver seed 1. (a) 40 matched controls at err 0.071, seeds 1-40 (J of each control's decode).
  (b) 40 shuffled targets (the 239 tokens permuted over the 15 message lengths, shuffle seed k, solver seed k, k = 1-40) --
  this is the ARM-C1 check (the family's own decode of the shuffled target through the same judge) built into the gate.
- **PASS iff J(T) > p95(b) and J(T) >= p05(a)** (equivalently gap >= p05(a) - mean(a)); ceil(q n)-th order statistic.
- **Rule 3, can the control differ from the target on J?** Yes: J is computed on the decode, and a control whose code^mark
  layer is read scores near real prose (control seed 1 at 0.071: J = -0.992 with recovery 0.741) while a decode of text that is
  not wordcode-enciphered need not; the (b) leg measures where this solver's decodes of structure-free orderings land. If the
  shuffled decodes themselves reach p05(a) (leave-one-out false-positive count over (b) > 2 of 40), the judge is **void as a
  gate for wordcode at N=239** (ARM-C1) and the target result is not read.
- **Power:** 10 held-out controls at err 0.071, seeds 101-110, each against the maximum (p95 of 10 = 10th) of 10 own shuffles
  (shuffle seeds 1-10, solver seed k) and p05(a). Power PASS iff >= 80% of held-out controls with recovery >= 0.60 pass, with at
  least 5 such; else "untested-by-this-gate".
- **Read-out:** power PASS and target FAIL -> control-backed negative for wordcode (`codes=marked`) at N=239 for one-reader
  error up to 0.071 only (not 0.125, where the control fails its own gate). Power PASS and target PASS -> "worth a verifier" at
  most; no reading, no grades in this job. Power FAIL or ARM-C1 void -> "untested-by-this-tool at N=239"; since this is the third
  wordcode attempt on this text (WC-LAGARDE2 err 0.23; LAG-V2 err 0.071/0.125; this gate), the family is then retired for this
  tool on this text (rule 3, third-attempt clause) until new material (pooling) or a different instrument.
- Status stays `open`. Scores to `families/lag_wcgap.tsv`; `--report` re-prints; `--check` re-solves and diffs (rule 7).
