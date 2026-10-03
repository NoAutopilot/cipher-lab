# LM-context fill of the No.4 conflict codes -- pre-registration (GAPS17-na-janssens-java-1811, 3 Oct 2026, account-4)

Committed before any candidate is scored (clock read 01:09 UTC 3 Oct 2026). Script: `lmfill/lmfill.py` (next commit).

**Targets.** The 26 rows of `conflicts.tsv` whose witnesses include a No.4 page (`no4-*`), each with its competing values.

**Model.** Letter 5-gram, interpolated (Witten-Bell style backoff to order 1), trained on `tools/data/fr1810` (the
`judge_plaintext.py` LANG_CORPORA list), text folded with `judge_plaintext.fold()` (lower case, accents folded, letters
only). Consequence stated now: accent-only and punctuation-only variants (a/à, fe/fé, aoust/août., =re/re) fold to the
same or near-same string and are **untestable by this model** -- logged "untested-by-this-tool", never moved.

**Contexts.** Every occurrence of the code in the code sequences on disk: keysource_passA.tsv (190, 191, 199, 200),
keysource_no5_passA.tsv (No.5), leaf192/201_reconciled.tsv, no4/no4_merge.tsv, and leaf 188 (ciphertext.tsv with
key.tsv values). Window: the 3 tokens either side (their gloss, or key value on 188; an unkeyed neighbour ends the
window). Score of value v at one occurrence = log10 P(left + v + right) under the model; a code's score for v = the sum
over its occurrences. Winner = argmax; margin = winner minus runner-up.

**Gates (all three, for a code to move):**
1. margin >= 1.0 (log10, a 10:1 likelihood ratio);
2. shuffled-assignment control: 20 seeds, each scoring the same winner/runner-up pair in an equal number of contexts
   drawn at random from the other codes' occurrences; the real margin must exceed the maximum of the 20 shuffled margins
   (this control varies the context, the axis the statistic depends on, so it can fail differently from the target);
3. method gate, the known-answer check (No.4 matched control): settled No.4 cells (no4_merge.tsv rows with an empty
   note whose code is not in conflicts.tsv and whose key.tsv grade is C), contexts from No.4 itself with about 34% of
   the other positions masked at random (leaf 188's unkeyed fraction, 56/163), true value vs one morphological decoy
   (drop the final letter if it is s/t/e/x and the value is longer than 2 letters, else add s), the same gates 1-2
   applied. The method is licensed only if, among known-answer items that clear gates 1-2, the true value wins in at
   least 85% AND at least 15 items clear. If the method gate fails, no code moves.

**What a move means.** key.tsv value set to the winner, grade M kept (an LM preference is not a witness; rule 4 grades
it at best S, and the witnesses stay in conflicts.tsv with a dated decision). No majority settling; a code that does not
clear stays logged as it is.
