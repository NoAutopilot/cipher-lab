# PREREG R12D-FAIR2 -- fair-game-2010, strictly injective substitution solve (written 6 Oct 2026 ~16:30 UTC, before any scored run)

Ciphertext: the same as R12D-FAIR -- the marked letters themselves, both credit-block orders reconciled by GF4-BATCH22
(reconcile_2026-10-03.tsv): scroll order = spec/ATS (`test2/order_scroll.txt`, primary), column order = Schmeh 2026
(`test2/order_column.txt`); N=67, K=21, position 1:4 (redacted) dropped.

Instrument (different from masc's anneal and masc_words' anneal+polish, rule 3 third-attempt clause):
`tools/families/masc_inj.py` -- a deterministic word-pattern beam search (branch-and-bound over dictionary words by
isomorph), STRICTLY one-to-one (no two cipher letters to one plain letter), single-letter OOV skips at cost -11,
cut-word edges at -3, beam per position, n-gram re-rank of the end states. Our own code; nothing from
aaymeloglu/unsolved-ciphers. Parameters were set on dev control seeds 101-103 only (never seeds 1-5, never the target).
Fixed params: beam=1000 (dev seeds 101-103: beam 400 -> 0.736, beam 1000 -> 0.950), all others default; restarts 1 (unused, deterministic).

Control: family_run.py's matched masc_words control (window with exactly K=21 distinct letters, N=67, one sign per
letter, training text with word boundaries, window +-2000 removed), en corpus (pg1661_holmes + pg2701_mobydick),
seeds 1-5.
Gate G1: control mean letter recovery >= 0.60 (family_run --gate 0.6). Below: CONTROL BELOW GATE, target not run,
step [retired] for this instrument family (word-pattern injective search) at N=67.
Not at ceiling check: masc 0.591, masc_words 0.707 at the same N/K/seeds -- headroom exists.
Target reading criterion (if gated): judge PASS (`tools/judge_plaintext.py specs/fair-game-2010.json`) AND the target's
judge score above every one of 5 shuffled-target decodes by the same instrument (shuffle seeds 7-11, scroll order).
If any shuffled decode PASSes the judge, the judge is void as a gate for this family at N=67 (ARM-C1) and the result
is "judge cannot decide". Anything else is a FAIL; en judge's unknown reliability (EN-FOLDS) is stated beside it.
