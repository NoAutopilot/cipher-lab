# PREREG MQS-PARTICIPATION -- homophonic_anneal.py --participation (9 Oct 2026, written 09:4x UTC by date -u, pushed before any scored run)

Research row M43 (research/MARY-STUART-TALK-2026-10-09.tsv): split homophones from nomenclature from the data, not only
from visible marks. Method credit: Lasry, Biermann and Tomokiyo 2023 (Cryptologia 47:2) p.112, p.115 ("usually not part
of contiguous plausible segments"). Brief: .claude/briefs/runs/2026-10-09-ytbiz-mqs-next-participation.md.

## Statistic
For each sign: the share of its occurrences, pooled over every restart's decode, lying inside an occurrence of a corpus
word (corpus_vocab top 300, >= 3 letters). Per-sign null: sign labels permuted over positions (200 permutations, window
masks kept); a sign with >= 2 occurrences below its null's 5% quantile is flagged and written to CLASSFILE.
Gate statistic: AUC (marked signs' shares lower than letter signs').

## Known answer (no ciphers/ folder; prior_work.py has no item to run on)
Synthetic, the MQS-SOLVER design: plaintext = Lettres de Catherine de Medicis t.2 (tools/data/fr16, bytes 1,200,000-
1,240,000, held out); corpus = t.1 + Marguerite de Valois (lettresindites00marg). French, order-3, 24 letters.
make_marked_control, K = 40 letter signs, 1-2 homophones per letter, `--marked-mode plain` (the nomenclature signs are
NOT announced to the solver: solved as ordinary signs). 8 restarts, 40,000 iters, seeds 1, 2, 3.
- **Primary cell P:** N = 1500, `--marked 0.3:150` (achieved 25.4% marked tokens at seed 1, 150 types; whole-word
  replacement cannot reach 30% with fewer types -- the MQS-SOLVER deviation). Nearest feasible to the brief's 30%.
- **Secondary cell S (declared now, graded only as context):** N = 1500, `--marked 0.3:60` (about 15%, 60 types).
A timing probe at seed 9 (not a scored seed; 2 restarts) read letters at 21.7% in cell P's design: the blind solve may
not read at all with 150 unannounced signs. That is recorded as a probe, not a result.

## Null that can fail differently
`--part-null-shuffle`: the same cipher with its token positions shuffled, solved and scored the same way. No word can
form, so a real separation must vanish; but marked signs are rarer and the solve assigns them letters, so a count- or
letter-driven artefact would persist in the null and show up there too. The statistic (AUC on per-sign word-window
shares) depends on order, which is exactly what the null changes (CLAUDE.md rule 3, "control that cannot vary").
Ceiling: this is a classification, not a gain over blind; letter accuracy in plain mode is reported beside it.

## Gate (fixed now)
PASS for cell P only if all three hold over seeds 1-3: mean AUC >= 0.75; mean null AUC <= 0.65; mean AUC - mean null AUC
>= 0.15. Also reported (not gated): flagged precision, type and token recall, letter signs flagged, letter accuracy.
FAIL ships the option `weak` on tools/data/tool_shelf.tsv with both numbers; not re-briefed; nothing run on a target.
