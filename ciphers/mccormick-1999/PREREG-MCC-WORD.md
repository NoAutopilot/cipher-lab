# PREREG-MCC-WORD (14 Oct 2026, 22:4x UTC by date -u; pushed before any control recovery score is computed)

Worker MCC-WORD (account 2, LANE DEFAULT-A2-2209-14). Next instrument named by MCC-SWEEP (NOTES.md, 11 Oct): a word-level
code-word anneal. Implemented as an option on the existing instrument (Usage 8):
`specs/cheap-tests/mccormick-1999/token_anneal.py --control-only --objective wordbigram --n-tokens N --seeds 1,2,3
--null [--lm heldout|insample] [--pool 1000] [--sweeps 200] [--restarts 2]`; offline test `tools/tests/test_mcc_wordbigram.py`.

## Design (fixed now)
- Control generator: bMCC4's `build_control`, unchanged (contiguous word stream from the `en` corpus, Holmes + Moby-Dick;
  the target's per-position kind sequence, 116 code / 14 number / 2 letter of 132, tiled to N; the 60 commonest words
  one shared code each, every other word a fresh code per occurrence; seeding rng 1000+seed). N = 132, 500, 2,000,
  8,000; seeds 1, 2, 3.
- Objective: whole-word bigram log-probability on the TOTAL scale (natural log), Jelinek-Mercer lambda 0.8 with an
  add-one unigram, closed vocabulary = the top 1,000 words of the LM corpus + UNK + BND. Number and single-letter tokens
  are BND (they break the word chain), on control and target alike.
- LM corpus, primary arm: `tools/data/en/` (Pride and Prejudice, Gatsby, Huckleberry Finn) -- held out from the
  control's Holmes + Moby-Dick draw, so the control is not scored by a model that has seen its own text.
  Diagnostic arm (`--lm insample`, run only if the primary arm reads at no N, never licensing a target run): the same
  three files plus Holmes + Moby-Dick (an upper bound with the control's source in the LM).
- Code types drawn from the 1,000-word pool. Search: heat-bath (Gibbs) annealing, each code type resampled from
  softmax(exact total-score change / T) over the whole pool, T geometric 3.0 -> 0.05 over 200 sweeps, then one greedy
  sweep; 2 restarts, best total kept.
- Null (rule 3): each control re-run with its code-token ORDER shuffled among the code slots (rng 2000+seed), same search,
  scored against the same truth. A bigram objective reads order, so the null can differ from the control on recovery.
- Search-adequacy diagnostic per seed: the found total vs the truth assignment's total under the same LM. Found >= truth
  means the miss is the objective's (the truth is not its optimum), not the search's.

## Structural ceiling (generator only, no anneal; computed before scoring)
Share of truth code TYPES whose word is in the 1,000-word held-out pool / share of code TOKENS:
132: 0.647/0.562/0.447 types, 0.741/0.664/0.638 tokens; 500: 0.551/0.519/0.420, 0.719/0.683/0.628;
2,000: 0.540/0.497/0.464, 0.752/0.705/0.693; 8,000: 0.568/0.447/0.437, 0.786/0.685/0.685.
Repeated (shared-code) types: 15-17% of types at 132, 1.5-1.7% at 8,000. The type-level gate 0.5 is again near or above
the ceiling at every N, so it is reported but the read criterion is token-level (as MCC-SWEEP's PREREG justified).

## Criteria
- Read (per N): control token recovery mean over 3 seeds >= 0.5 AND every control seed above the null's maximum token
  recovery at that N. Type recovery reported beside it.
- The target is run only if the primary arm reads at N = 132. Otherwise no target run.
- Outcome wording, fixed now: reads at 132 -> target run (same settings, judge + shuffled-target floor) if the cap allows,
  else owed; reads only at some N > 132 -> word-level code-word family `too-short` at 132 tokens (outside blocker);
  reads at no N <= 8,000 -> "untestable by this instrument at N <= 8,000". The char-4-gram anneal (bMCC4, MCC-SWEEP)
  and this word-bigram anneal are different objectives, so this is attempt 1 of this instrument; the token/nomenclator
  FAMILY then has two instruments failing their own controls, and the Verdict names a genuinely different instrument
  or `no-key-material`.
- Development runs before this file, disclosed: one 20-sweep, 1-restart run on dev seed 9 at 132 (recovery 0.000; found
  total -371.5 vs truth -492.0) and a 10-sweep timing run on dev seed 9 at 2,000 (not scored). Seeds 1-3 not run.
- The target stays `open` (rule 5) whatever the outcome.
