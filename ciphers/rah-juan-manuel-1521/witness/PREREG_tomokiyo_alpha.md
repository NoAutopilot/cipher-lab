# PREREG -- R11-RJMKEY, rah-juan-manuel-1521: Tomokiyo's published alphabet on the held-out page (written 6 Oct 2026 10:2x UTC)
Committed and pushed BEFORE `scripts/test1.py --alphabet key_tomokiyo_alpha.tsv` is run for the first time. The worker has not
seen any per-token f.199 chunk from the test-1 alignment (only the aggregate results_test1.json).

Key under test: key_tomokiyo_alpha.tsv rows with firm=1 and a non-blank our_label (12 labels): A=a, 9=e, X=e, 3=e, E=h, V=m,
4=o, Z=r, R=s, T=s, K=y, F=null. A null is scored as the empty chunk (the aligner may give a symbol 0-2 letters). Labels with no
Tomokiyo counterpart (Q, B, D, W, 7, ?n) are excluded from N, as test 1 excluded labels outside alphabet.tsv.

Statistic S (unchanged from witness/gate_alpha.txt): share of R9529 f.199 symbol tokens (reconciled A/B, labels in the key)
whose chunk from the existing prior-free hard-EM alignment of f.199 against passes/gloss_f201.tsv (same aligner settings, same
code: test1.py's align(); the alignment does not depend on the key) equals the key's value for that label (fold() applied).
Control: 200 keys with the 12 Tomokiyo values permuted among the 12 labels (random.Random(seed).shuffle, seeds 1..200). The
alignment is fixed and the values move, so the control CAN differ from the target on S (rule 3 orthogonality); the values are
not all equal (a, e x3, h, m, o, r, s x2, y, null), so a permutation changes which label carries which value.
Gate (unchanged): PASS iff S_real > max(null) AND S_real >= 0.24. Anything else FAIL.

Secondary, reported beside the gate, not a separate licence: the same S and control on R9528 f.194 vs the f.197 gloss. Tomokiyo's
table is external to f.194, so f.194 is not in-sample for this key, but the label->shape map (siblings/our_labels.tsv) was written
by R11-RJMSIB after seeing both Tomokiyo's table and alphabet.tsv's f.194 values, so the f.194 number may be inflated by that
labelling; it is read as corroboration only. Same gate form; if f.194 PASSes and f.199 FAILs, the verdict is FAIL.

Rule 3 matched-control note carried from test 1: f.199's reader error is 0.42 (f.194 0.23) and only 44 of 117 nomenclator words
anchor on f.201, so a FAIL on f.199 is "untested at this transcription error", not a refutation of Tomokiyo's table.
A PASS licenses no reading change and no grade above M in this job: a verifier sees it first (brief R11-RJMKEY).
