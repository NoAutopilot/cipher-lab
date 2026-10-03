# H73 pre-registration (worker ARM-H73, account 2, for LANE-ARM-B)

Written 3 Oct 2026 19:30 UTC, before any synthetic letter was built, any overlap measured or any solver run.
Brief: `.claude/briefs/runs/2026-10-03-acct2-arm-h73-vocabprior.md`.

**What is different here (one paragraph).** Tomokiyo's suggestion was that a model might read the letter if it
learned the vocabulary of a sibling code. ARM-C1 ran blind: it had a soft prior (a word outside the union of every
sibling table, the THE=972 decodes and 2,500 en18 content forms cost 3 nats) and no order constraint. ARM3-LOOP and
H27 were crib loops (H27 with the slot grammar handed over, no vocabulary). H73 V1 adds a constraint none of them
had: the book is assumed **one-part at decade level**, so the decades of the target, sorted by value, must map in
the same order onto one sibling code-maker's **alphabetical** word list (WE028 or THE=972, whole-word entries only),
and every value in a decade must take a word from that decade's stretch of the list. The solver searches only
monotone placements of the decades along the list (a block move per decade plus a per-value move inside the
decade's window), scored by the en18 word-trigram LM. Particles (1-99) are restricted to the siblings' short-word
entries that are also en18 function words.

**Same-instrument check (brief: stop and log any variant that is ARM-C1/ARM3-LOOP/H27 under a new name).**
- V2 (two-part: vocabulary only, no order) is ARM-C1's sibling-vocabulary prior with its penalty raised from 3 nats
  to a ban and its list narrowed to one table. That is the same instrument with one knob turned (CLAUDE.md rule 3,
  third-attempt clause), and ARM-C1's own diagnostics already show why it cannot help at this N: its control's prior
  covered the control's book, yet with every particle and every repeated value given, greedy recovered only 19/168
  book values, and the blind sampler scored the true key below function-word salad. **V2 is not run as an H73
  variant.** The unchanged ARM-C1 solver (default parameters, its soft prior) is run on the same H73 control letters
  as the blind baseline the brief requires; that number is reported as "ARM-C1 solver", not as V2.
- V1 is a different instrument: no earlier run had an order constraint (ARM-DESIGN Q1 found one-part vs two-part
  not decidable from the ciphertext, so it was never tested as a solver constraint). V1 is run.

**Control plaintext (held out, never used to tune).** Bourdeau's decodes of Armstrong's 15 Feb and 22 Feb 1808 letters
(`tools/data/uscodes-1800/decodes/`), concatenated in that order. They are syllable decodes with unread groups;
the script rebuilds words by joining adjacent decoded fragments when the joined string is an en18 vocabulary word
and the fragments are not all words themselves (a deterministic DP, no tuning against any score), and turns every
unread `{nnnn}` group into an out-of-vocabulary mark. The rebuilt text is written to `h73/control_plain.txt` before
any solve and is what "true word" means. If the rebuilt text yields fewer than 369 coded tokens under a control's
code, the control uses all it has and reports its N (no padding from other text).

**Synthetic code (target design, V1 assumption).** Particle block: 99 values at 1-99, a cold random permutation of
the 30 commonest en18 words + the 26 letters + en18 words from rank 200 (ARM-C1's construction, unchanged). Book:
the BOOK list's whole-word entries (alphabetic, length >= 2, in the en18 LM vocabulary, not in the particle block),
sorted alphabetically, cut into consecutive blocks of 6 entries (the target fills about six units digits per
decade: 0,1,4,6,7,8 carry 94% of its book tokens); within a block, members are ranked by en18 frequency and placed
on the target's own slot order (0,1,4,6,7,8,...); blocks get decades in alphabetical order on a seed-dependent
increasing random subset of decades 10..199 (values 100-1999, the target's range). Plaintext words in neither list
become `*` (a run is one mark). Recorded per control: coded N, distinct, singletons, particle/book token shares,
book slot-0 share against the target's 0.388.

**Controls (cross-held-out: the solver's PRIOR list is never the synthetic BOOK list).**
- C-A (gating): prior WE028 -> synthetic book from THE=972's list. Seeds 1, 2, 3.
- C-B (reported, not gating): prior THE=972 -> synthetic book from WE028's list. The control plaintext was decoded
  with THE=972, so this prior contains nearly every true word: it is a leak-side upper bound and is labelled so.
  Seed 1 only.
- Overlap recorded for both: share of the book list's entries in the prior, and share of the control letter's coded
  book TOKENS whose true word is in the prior (token coverage).
- Realistic-overlap control: the overlap I judge realistic for a different code-maker in 1808 is the one two real
  makers on file actually show, i.e. C-A's own natural WE028-vs-THE=972 overlap; C-A is therefore the realistic
  control. If C-A's measured token coverage comes out above 0.90, a further C-A run with the prior thinned to 0.75
  token coverage (seed 1) is added and reported beside it.
- Blind baseline (rule 3 gain-gate paragraph): the ARM-C1 solver, default parameters, on the same C-A letters,
  seeds 1-3. If its mean is >= 0.6 already, V1 has no headroom to show and the gate below cannot license anything.

**Gate.** Blended word accuracy on coded tokens (ARM-C1's metric) >= 0.6 on at least 2 of the 3 C-A seeds, V1
solver, default H73 settings fixed before the run (sweeps 30, 3 restarts, block size 6 assumed by the solver,
window = 2 x block x |prior|/|book list|, rounded). Particle and book accuracies are reported separately (rule 3,
unbalanced classes). C-B never licenses the target.

**Target judging (only if the gate is met).** V1 on the target once with prior WE028 and once with prior THE=972.
A reading is reported only if (a) the en18 judge PASSes the decode AND (b) the same solver's decode of the target's
shuffled token order FAILs the judge (ARM-C1 found the judge PASSes nomenclator salad, so (b) is required). Then
graded S/M per token (rule 4; no H or C exists).

**Stop rule.** Below gate on C-A: do not run the target; log "untestable by this tool at N=369 (vocabulary prior,
matched control X vs gate 0.6)" in HYPOTHESES.md and CAMPAIGN.md and stop. No re-tuning of block size, window,
sweeps or the joining rule after seeing a control score. Box 120 min / cap USD 10; no unit started past 80% of either.
