# PREREG-D4HDK: context fill of the unread nomenclator groups (Escalation key-rebuild step), 7 Oct 2026

Worker D4-HDK (solver, account 4, LANE DEFAULT-account-4-20261007-1335). Written and pushed before any score is computed.
Rule 3 third-attempt clause: attempt 1 of this instrument (no LM context fill has been run on this letter).

## What is actually left untried (restating the stale Escalation `[ ] key-rebuild` line)
The gloss alignment (GAPS152-163) and the bracketing (GAPS193) are done; the 625 margin-word re-read is [retired] (GAPS199).
Untried: a language-model context fill for the nomenclator groups that carry no settled gloss. Targets:
625 at p2_7 (margin gloss "[?] Ahlefeldt", M) and p3_4 (unglossed); 634 at p3_17 (I, [Holstein] by margin alignment);
602 at p3_26.3 (M, value carried from p3_1's gloss). Out of scope: 68 (2-digit letter-table group, reads e by key.tsv, not a
nomenclator code) and 7480 (margin number, no prose context).

## Instrument
Word bigram model on `tools/data/de17` (5 `_djvu.txt` OCR files, 1631-1660s German diplomatic documents), spelling folded
(lowercase; ae/oe/ue and umlauts to a/o/u; ß/ss->s; ck->k; th->t; y->i; dt->t; doubled letters single). Each referent below
is a fixed set of folded surface forms; its count in a context slot is the sum over its forms. Score of referent r at a
token with left word L and right word R (the nearest prose words from the two blind passes' context columns, pass A first;
an adjacent code is replaced by its key_gloss value):
  s(r) = log P(r | L) + log P(R | r), interpolated add-0.1 bigram with unigram backoff (lambda 0.7).
Prior-only baseline: s0(r) = log P(r) (unigram only).

## Candidate set (fixed, 28 referents)
From the gloss-pinned key (14): Dennemarck, Brandenburg, Berlin, Holland, Staaten (General-Staaten), Franckreich, Kayser,
Konig (Konig in Dennemarck), Hertzog, Ploen, Alliance, Schweden (768 "?ueco"), Daniae (Rex Daniae), Bleinenkehl (690).
Further plausible 1672 Hamburg/Danish-court referents (14): Holstein, Gottorf, Ahlefeldt, Statthalter, Gabel, Griffenfeld,
Schumacher, England, Hamburg, Lubeck, Braunschweig, Luneburg, Sachsen, Spanien.

## Control (run first) and gate
Held-out set: every occurrence of a C-grade gloss-pinned code whose referent is in the candidate list (key_gloss.tsv grade C:
229, 447, 601, 605, 651, 653, 681, 774, 775, 834, 5756) -- each scored with its own value among the 28; known neighbour
codes keep their values. This control can fail differently from the targets: its truth is known per token and the model
can rank it anywhere (it is not orthogonal to the statistic).
Statistic: top-1 accuracy and mean reciprocal rank (MRR) of the true referent.
Null: the same scoring with the held-out tokens' contexts permuted among themselves (1,000 shuffles, seed 4).
Gate (all three): top-1 >= 0.50; MRR above the shuffled-context null's p95; top-1 strictly above the prior-only baseline's
top-1 (context must add over frequency).
If the gate fails: no target value is scored for key.tsv; the step is logged [retired] with the instrument named (word bigram
context fill on de17), and the target ranks are written to the output for the record only, graded nothing.
If the gate passes: a target value enters key_gloss.tsv at S only if it ranks first with a log-score margin >= 1.0 over the
second referent; otherwise it stays as is.
