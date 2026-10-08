# Pre-registration, SFZ-DUKE (account 4, 8 Oct 2026, written ~03:50 UTC by date -u, before any second-reader output or statistic was seen)

Gate G1 unchanged (SFZ-1/SFZ-D): leave-one-letter-out over units f8 (slip f.8 vs copy f.10) and f5 (f.5 vs f.7),
200 shuffles of the training key, seed 1447, score = amidani/g1.py `score`. PASS = mean held-out >= 0.60 AND every unit
> its shuffle p95. Not lowered.

Inputs (one label convention, duke_labels.md, fixed before the second read):
- A = SFZ-D's committed reads (ciphertext_f8.tsv, ciphertext_f5.tsv).
- B = one blind Sonnet reader per slip (f.8 committed crops; f.5 from the --deskew re-cut of the committed source), sheet
  duke_labels.md only, no access to A, keys or copies.
- AB = the reconciled transcription: per line, A and B aligned by edit distance (tools/reconcile_passes.py-style); agreed
  tokens kept; a split or a one-reader-only token becomes `?` (one shared unknown symbol). No third reader decides splits.

Primary test (the one that counts): AB through the dateline-anchored learner (pusterla/g1p.py `learn`, segment hard EM),
anchors = the start of the shared final run of each slip <-> "data" of its copy, plus the slip's start <-> the copy's start
(the che anchor of g1p does not exist for the Duke: no sign falls near the copies' "che" more than chance, checked before
this file; see NOTES). Secondary, reported, cannot license anything: A and B alone through the same learner; AB through
g1.py's stock learner; AB with the split runs joined (cp ca cr -> one token, etc.), one shot.
Reader disagreement (A vs B, per line, edit distance / A length) is reported as err_2reader, never as true error.
A PASS goes to a separate verifier; a FAIL with B disagreeing on more than a tenth of signs means the next step is the
owner's sign sorter (CLAUDE.md Usage 6), not a third machine pass.
