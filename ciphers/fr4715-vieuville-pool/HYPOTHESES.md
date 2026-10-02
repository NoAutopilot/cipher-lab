# fr4715-vieuville-pool -- hypothesis families (append-only)

CLAUDE.md rule 3: CONTROL and TARGET numbers side by side. Created by LIKELY-1, 2 Oct 2026 (account-4). The pool's
key of record is `ciphers/fr4715-montholon-1589/keys/key_vieuville_nevers.tsv`; no.58's own rows live in that folder's
HYPOTHESES.md.

| Leaf | Family | CONTROL | TARGET | Status | Reason |
|---|---|---|---|---|---|
| no.44 f.67r | key_vieuville_nevers.tsv applied to the leaf's in-key groups; French word-cover of the decoded runs vs 200 letter-shuffled keys (scripts/keytest.py, LIKELY-1, 2 Oct 2026) | no.58 dump (Tomokiyo's groups, same key, same scorer): full N 818 letters, real 0.891 vs shuffles mean 0.353 max 0.631, z 5.37, rank 1 of 201; subsampled to 200 windows of 8 in-key groups x 20 shuffles: real mean 0.816 vs shuffle mean 0.355, real above the shuffle mean in 195/200 windows, rank 1 of 21 in only 85/200 (11/200 windows have a shuffled key at 1.0) | 28 cipher groups, 8 in key (L01: 25 93 84 25 50 93 25 95 -> ausaluat), 4 unbarred out of key (6 7 14 15), 11 barred word-codes, 4 pass disagreements, 1 date numeral; cover 6/8 = 0.750 vs 200 shuffles mean 0.326 sd 0.293 max 1.000, z 1.45, rank 43 of 201; vs the first 20 shuffles max 0.875 (not rank 1) | **non-test at N=8 (not a negative)** | the target sits where 97.5 pct of known-good 8-group windows sit (above the shuffle mean) and where the rank-1 gate has 42 pct power; the leaf's cipher content is the word-code layer (13 barred groups), which the letter key does not cover; next: a stronger clear-French pass to read the word-codes from context, then no.37 f.60 (dense) the same way |
