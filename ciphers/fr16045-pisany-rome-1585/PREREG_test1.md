# PREREG test 1 -- fr16045-pisany-rome-1585, f.75 (17 June 1585), Tomokiyo's 1585 table as key (PIS-T, 4 Oct 2026)

Written and pushed before any decode of the f.75 transcription with key.tsv (passes A/B were still running, unread).

Question: does Tomokiyo's published 1585 table (sources/cryptiana/web/henryiii_Vivonne4.png -- the image placed directly
after henryiii.htm's 1585 letter list; IMAGE-QUEUE rows 198/199 carry captions shifted by one paragraph) read the open
cipher of f.75 (canvas 156, 22 cipher lines) as French?

Data: two blind Sonnet passes over tx/SIGNSHEET.png labels (S01-S67, values withheld), reconciled by
tools/reconcile_passes.py -> tx/ciphertext_draft.tsv; target = that draft (passes A and B scored separately as well,
reported, not gating). Tokens `?[...]` (no table match) are dropped and counted; a trailing `?` is stripped.
Key: key.tsv; S04/S05 (= S07/S08, shapes Tomokiyo marks as identical for b and c) decode to `c` (fixed now, not tuned);
nulls (S54-S56) decode to nothing; word signs to their word.

Statistic: mean log10 add-k 4-gram probability per letter (tools/judge_plaintext.py NgramModel, k=0.01), model trained
on tools/data/fr16 Catherine de Medicis t.1 + Marguerite de Valois (t.2 held out for the positive control).

Nulls (computed first, same statistic, same tokens):
(a) value-shuffled key, 1000 permutations of key.tsv's value column over the 67 labels. Can differ from the target:
    the statistic depends on which letter each sign yields; a permutation changes that for most signs.
(b) token-order shuffles of the target decode, 500 shuffles of the per-sign output units. Can differ: the 4-gram
    statistic depends on letter order; shuffling keeps the letter multiset and destroys order.
Positive control (same run): 5 windows of Catherine t.2 (held out of the model) with the target's letter count,
enciphered with key.tsv (uniform random homophone per letter; j->i, v->u, k/w/letters absent dropped), sign noise at
e = the measured err_2reader (each sign replaced by a uniformly random other label with probability e), decoded with
the same key and scored against its own nulls (a) and (b) at 200/200. Control passes if >= 4 of 5 seeds exceed both
of their own p99s.

Gate: PASS if target score > null (a) p99 AND > null (b) p99 AND the positive control passes.
If the control fails: NON-TEST (whatever the target does). If the target FAILs and err_2reader > 0.10 or the inventory
is unsettled: NON-TEST, not a negative (TRANSCRIPTION.md). A PASS is graded S (cryptanalytic with a control; the key is
published, the reading of this page is ours), never H. Held-out fold check of the fr16 judge at N=1000: blended FN 28%,
per-fold 11.0 / 71.5 / 1.5% (Catherine t.1 / t.2 / Marguerite), so the absolute real_p05 gate of judge_plaintext.py is
of unknown reliability here and is reported but does not gate; the gate is relative to the nulls.
Script: test1.py (writes test1_result.json). No parameter is changed after the first run.
