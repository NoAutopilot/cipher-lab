# PREREG-BRO123 (9 Oct 2026, BRO-123 worker, account 2; for LANE FAMILY-A2i)

Written and pushed before any score on the target pair was computed. The only run before this commit was
`scripts/24_bro123_align.py dryrun` on appendix Carta 13 (a stand-in, not the target): S 0.445 vs permuted p99 0.270 (200 perms).

**Material.** Target stream: `body123_ciphertext.tsv` (911 tokens incl. 35 clear words, m0253-m0254 = body page 123),
built by `scripts/25_bro123_settle.py` from two blind Sonnet passes (`bro123/passA.tsv`, `bro123/passB.tsv`, crop paths only,
the appendix text never shown; agreement 881/912 = 96.6% by `tools/reconcile_passes.py --keep-plain`) and the
reconciler's settlements listed in that script. Known text: `plaintext_appendix.tsv` row m0294 / Carta 123 (the appendix's
period plaintext of the same letter), folded to lower-case a-z.

**Alignment.** Semi-global monotone DP (`scripts/24_bro123_align.py`): a cipher token whose key.tsv value equals the
letter scores +1, otherwise 0 (a code without a key row scores 0); each clear word is expanded to its letters, +2 equal,
-3 unequal; a token emitting no letter -1; a letter skipped -1; leading and trailing letters free.

**Statistic.** S = share of keyed cipher tokens (code has a single-letter key.tsv value) aligned to a letter equal to their
key value.

**Control.** 1,000 permutations (numpy default_rng, seed 123) of key.tsv's value column among its codes; for each, the DP is
re-run under the permuted key and S recomputed (the control can differ from the target on S: S depends on the code->value
assignment). Gate: S_real > p99 of the permuted S. Report S, n, null mean, p99, max.

**Only if the gate passes (step 4).** `attest` re-aligns with the thin codes x z d f 16 9 24 2 e 26 removed from the key
(score 0, so their own value cannot place them), and lists every occurrence of those codes and of every token with no key
row in `carta123_attest.tsv` with its aligned appendix letter. Grade C when the token is aligned to a letter and at least 3
of its 4 nearest neighbours (2 each side) are aligned to letters that equal their (non-thin) key value or clear letter;
otherwise M. key.tsv is never edited; codes whose support would change are named in NOTES.md, with `tools/decode_key.py --try`
on letter 134 where useful. If the gate FAILs: log the FAIL, write no attestation.

**Not claimed.** This is a known-text key test on a letter the appendix already gives in plaintext; it reads nothing new.
