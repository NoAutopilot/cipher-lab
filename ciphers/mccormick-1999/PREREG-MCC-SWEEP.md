# PREREG-MCC-SWEEP (11 Oct 2026, 19:5x UTC by date -u; pushed before any anneal score is computed)

Worker MCC-SWEEP (account 1, LANE DEFAULT-A1-1840). Instrument: `specs/cheap-tests/mccormick-1999/token_anneal.py`
(bMCC4, 25 Sept), given `--control-only --n-tokens N --seeds 1,2,3 --iters-per-type 80 --restarts 2 --fast --null`.
No target run in this job unless the control reads at 132 tokens (criterion below).

## Design (fixed before scoring)
- Control: bMCC4's own generator (`build_control`, unchanged): a contiguous English word stream from the `en` corpus
  (Holmes + Moby-Dick), the target's per-position kind sequence (116 code / 14 number / 2 letter of 132) tiled to
  length N, each top-60 word one shared 4-letter placeholder, every other word a fresh placeholder per occurrence.
  Seeding as bMCC4 (rng 1000+seed). Lengths N = 132, 500, 2,000, 8,000; 3 seeds each.
- Search: bMCC4's anneal (same move set, schedule, pool of 350 words, objective = mean 4-gram log10 P over the folded
  text), iterations = max(3000, 80 x code types) (bMCC4's 8,000 iters / 99 types), 2 restarts. `--fast` is an
  incremental scorer of the same objective; `--selftest` checks it equals the full scorer on 600 random moves (OK).
- Null (new, rule 3): each control re-run with its code-token ORDER shuffled among the code slots (rng 2000+seed),
  same search, scored against the same truth. Order is what an n-gram model reads, so this null can differ from the
  control on the recovery statistic (not a non-test of the bCAS/AX-5799 shape).

## Structural ceiling (computed before scoring, generator only, no anneal)
Share of the control's truth code TYPES whose word is in the 350-word candidate pool (the most any search can reach):
132: 0.647/0.494/0.487 (mean 0.543); 500: 0.496/0.419/0.377 (0.431); 2,000: 0.423/0.430/0.387 (0.413);
8,000: 0.413/0.391/0.369 (0.391). Repeated (shared-code) types are 15% of types at 132 and 1.6% at 8,000.
So bMCC4's type-level recovery gate of 0.5 is **unreachable by construction at 500 tokens and above**, and needs a
near-perfect search at 132. A type-level FAIL at N >= 500 is a non-test of the instrument's power (logged as such),
not evidence that length does not help.

## Criteria
- Primary (as before, the brief's gate): type-level recovery mean >= 0.5. Reported at every N with its ceiling.
- Read criterion for the sweep (justified above: the type-level gate cannot move with length under this scheme):
  **token-level recovery** (share of code-token occurrences given their true word) mean over 3 seeds >= 0.5 AND every
  control seed above the null's maximum token recovery at that N. The control "reads" at the smallest N meeting this.
- The target is run only if the control reads at 132 tokens on BOTH criteria. Otherwise no target run.
- Outcome wording, fixed now: control reads (token criterion) at 132 -> target run owed (not in this job's cap unless
  cheap); reads only at some N > 132 -> the token/nomenclator family is **too-short** at the target's 132 tokens (an
  outside blocker, NOTES.md gap blocker `too-short`), not a negative; reads at no N up to 8,000 -> logged as
  "untestable by this instrument at N <= 8,000"; the retry rung is then [retired] for this instrument only if rule 3's
  third-attempt clause applies (it does not: this is attempt 2), so it stays a named gap with a different instrument
  (code-word / abbreviation-lexicon model) as the next step.
- Conditional extension (declared now, run only if no N <= 8,000 reads on the token criterion and the cap allows):
  N = 32,000, 3 seeds, same settings; reported as an extension, not moving the criteria.
- The target stays `open` (rule 5) whatever the outcome; NEAR.md row edited only to stay consistent.
