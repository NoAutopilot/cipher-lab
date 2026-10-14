# PREREG-CL1161-KA: c186R token-level known-answer gate against Lasry's f163r paragraph

Worker CL1161-KA, LANE DEFAULT-A2-2209-14 (account 2), 14 Oct 2026, written 22:3x UTC by date -u, pushed in its own commit BEFORE any
score. Disk only. Script: `ka/ka_score.py` (committed with this file, not yet run on the target).

**Known answer.** George Lasry's f163r paragraph ("BnF cipher research", 10 Oct 2026; published by D. Bourdeau, cyphersolver dde5b0ea,
CC BY 4.0), as snapshotted in `sources/cyphersolver/2026-10-14-lasry/clair1161/NOTES.md` lines 46-49 ("Ce Seigneur ... plus grand repos."),
the same text C1161-V2 used. c186R = f163r (LQ-C1161 mapping). It is his reading, not a period key: agreement with it measures agreement
with Lasry, grade C for nothing (no H or C token is created by this job).

**Normalisation (rule 3, PX-BRODEC).** Both sides: `judge_plaintext.fold` (lowercase, accents off, letters only), then v->u, j->i.

**Ciphertext under test.** c186R tokens of `lkey/ciphertext_v2.tsv` (226 tokens, digit pairs of Lasry's codes merged as units, as built by
C1161-V2), values from `lkey/key_v2.tsv` (V2). A sign with no value (e.g. `/`) is a wildcard slot.

**Alignment.** Global Needleman-Wunsch between the decoded letter string D (each character tagged with its token; a no-value token is one
wildcard character) and the folded paragraph P: match +2, mismatch -1, gap -2; a wildcard scores 0 against any letter. A P letter aligned
to a D character belongs to that token; a P letter in a gap of D belongs to the preceding token (the first token if none). chunk(token) =
the P letters it receives. A token **agrees** iff chunk == its value (exact). Letter agreements = match columns.

**G1 (whole-key known-answer gate).** Statistic A = number of c186R tokens that agree. Null N1: key_v2's values permuted among all its signs
(units included), 1000 draws, seed 1, same alignment. **PASS iff A(V2) > p99(N1).**
Power check (the gate must be able to fail): a known-wrong variant, key_v2 with every value moved to the next sign in sorted sign order
(a fixed cyclic derangement chosen now), scored the same way; G1 is valid only if this variant FAILs G1. Also reported, no gate:
A for baseline key.tsv on ciphertext.tsv (77 as "i i"), V1 (`lkey/key_lasry.tsv`) and V2b (`lkey/key_v2b.tsv`).

**G2 (per conflict class).** Classes: (a) unit n77 (ours "ii" as two 7 tokens, his "de"); (b) unit n48 (ours digits 4 8 = "od", his
"fait"); (c) singleton 7 (ours i, his b); (d) S (ours u, his n). For each class, re-align with every token of the class masked as L
wildcards (value hidden; L = max(len(his value), len(our value)), so neither hypothesis is favoured by length where they are equal), and tally chunk per occurrence. Counts: n_his = chunks == his value, n_ours = chunks == ours.
Position null N2: the same masking (L wildcards) and tally at k random non-class c186R token positions (k = the class's occurrence count), 1000 draws,
seed 2; statistic = number of masked positions whose chunk == his value. **Class supports his value iff n_his >= 3 and n_his >= 2*n_ours
and n_his > p99(N2)**; supports ours by the mirror rule (n_ours >= 3, >= 2*n_his, > p99 of N2 for our value); otherwise undecided
(including any class with < 3 occurrences on c186R: reported, never decided).
Power check for G2: the same masked procedure on sign `qb` (both keys read a, C1161-LKEY agree) must support "a", and the known-wrong
hypothesis qb=o must not be supported; G2 results count only if both hold.

**What follows.** A G2 "supports his" licenses only a `tools/decode_key.py --try` run of that value at every occurrence on the whole
ciphertext (key never written; M unless --try's own control passes). No key.tsv edit by this job. Credit Lasry for every value his
paragraph supplies.
