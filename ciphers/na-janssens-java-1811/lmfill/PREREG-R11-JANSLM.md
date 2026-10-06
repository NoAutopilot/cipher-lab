# Held-out fill test of the LM-context instrument on leaf 188 -- pre-registration (R11-JANSLM, 6 Oct 2026, account 2)

Committed and pushed before any scored run (clock read 09:37 UTC 6 Oct 2026). Script: `lmfill/heldout_188.py` (next commit).
Question: can the GAPS17 letter-5-gram context fill recover leaf 188's *keyed* values when they are hidden? Only if
it can is it used to list candidates for the 56 unkeyed leaf-188 tokens.

**Model.** The GAPS17 class `lmfill.LM` unchanged: letter 5-gram, Witten-Bell interpolation, trained on
`tools/data/fr1810` (Napoleonic official/military French 1800-1811, the era-matched French corpus on disk; leaf 188
is June 1811), text folded with `judge_plaintext.fold()`.

**Candidate vocabulary.** Every distinct folded non-empty value in key.tsv (closed vocabulary; homophones collapse to
one folded form). A fill is correct when the winner's folded form equals the true value's folded form.

**Items.** Leaf 188 tokens graded C in reading_tokens.tsv whose value folds non-empty (punctuation-only values, e.g.
".", are untestable and excluded). Mask seeds 1..10; each seed masks a random 20% (rounded) of these items at once.

**Context.** Window of 3 folded neighbour values either side on leaf 188. A masked, unkeyed (U) or empty neighbour ends
the window; punctuation-only neighbours are skipped (transparent). M-graded neighbours are used with their key value.
Score of candidate v = log10 P(left + v + right). Winner = argmax over the vocabulary; margin = winner minus runner-up.

**Control (can vary on the statistic).** Shuffled context: for each mask seed, 20 control seeds; each masked item keeps
its true value but takes the (left, right) context of a uniformly random other leaf-188 position (same mask applied).
Accuracy depends on the context, so this control can and should fall. Also reported (not gated): a context-free
baseline (argmax of P(v) alone) and the majority-value baseline.

**Gates (all, pooled over the 10 mask seeds):**
1. top-1 accuracy A_real >= 0.30;
2. A_real > the maximum of the pooled shuffled-context accuracies (pooled per control seed index over
   the 10 masks, i.e. 20 pooled control accuracies; A_real must exceed their maximum);
3. confident-fill precision: among real fills with margin >= 1.0 log10, precision >= 0.80 on at least 10 fills, and
   strictly above the precision of the shuffled-context confident fills (pooled over all 200 control runs).
   Per-class note (CLAUDE.md rule 3, AX-NAMES): the per-value breakdown of correct fills is reported; if more than half
   of the correct confident fills are one value, gate 3 is reported as dominated and does not pass.

**If all pass:** list candidates for each of the 56 unkeyed leaf-188 tokens (same model, same window, top 3 with
margins) at grade M, as `lmfill/unkeyed_candidates.tsv`; no key.tsv change, no reading change; Collet crib values
(AUDIT.md sec. 4) compared and still "found, not applied" unless they agree with a gated fill. **If any fails:**
HYPOTHESES.md row "LM-context fill of unkeyed leaf-188 codes: untestable by this method at this N", and stop.
