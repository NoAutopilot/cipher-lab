# PREREG AOSB-PAIRS (4 Oct 2026, written and pushed before any R4284/R4282 score was computed)

Key under test: `aosb/key_aosb1629.tsv`, learned by tools/interlinear_align.py from AOSB ser. I Band 4 letter 231
(Oxenstierna to Paul Strasburg, Elbing 24 Jan 1629, pp. 341-342: 16 footnotes, 553 cipher tokens beside the
asterisked clear passages). Letter class = 1-2 digit numbers and single letter/Greek signs (majority meaning,
grade C); word class = 3-4 digit numbers (lemma meaning, grade C).

Question: does this key family (same table, not just same design) read R4284's numeric body or R4282?

Statistic (fixed now): decode the target in order with the key; a token with no key value breaks the run (as do the
clear words in brackets); S = letter-weighted mean of `judge_plaintext.NgramModel(la17, n=4).score` over runs of >= 4
letters; C = share of target cipher tokens that have a key value. Null: 200 keys with the meanings permuted among
the codes of the same class (letter meanings among letter codes, word meanings among word codes; seeds 1-200).
Real-text reference: NgramModel.controls at the decoded letter count (200 windows).

Control first (stop rule): leave-one-footnote-out on the AOSB passages themselves -- for each of the 16 footnotes,
the key is rebuilt (majority over align.tsv chunks) from the other 15 and decodes the held-out footnote; the 16
held-out decodes are pooled as runs and scored with the same S and C, against the same 200-permutation null
(permuting each fold's key). Control PASS = pooled C >= 0.5 and pooled S > null p99. If the control fails: stop,
log "untested-by-this-tool", score no target.

Target arms (only if the control passes):
- R4284 numeric body (r4284_transcription_bourdeau.txt, the two numeric-body sections; '?' digits dropped from the
  token, bracketed clear words break runs; the scribe's repeated line marked "(sic" excluded as GAPS89 did).
- R4282 (tx2/ciphertext_reconciled.tsv, 1,090 signs): the only exact shared sign is lambda (R4282 label L); the
  printed capitals (Q O F M N R V Z) are the 1909 editors' rendering, so a second, optimistic mapping (capital ->
  R4282's same lowercase letter shape) is also reported. Either mapping runs the S test only if C >= 0.5; below
  that the arm is "inapplicable at this coverage" (coverage reported), not a negative.
Verdict per arm: FIT = C >= 0.5 and S > null p99 and S >= real-text p05; WEAK = C >= 0.5 and S > null p99 only;
NO FIT = C >= 0.5 and S <= null p99. No threshold is changed after scores are seen.
