# PREREG-C1161RA addendum LOLO: stage-1-only held 4-gram anneal under leave-one-leaf-out streams

C1161-LOLO (account-3 Fable worker), 4 Oct 2026, written and pushed before any leave-one-leaf-out run.
Brief: `.claude/briefs/runs/2026-10-04-acct3-c1161-lolo.md`. Script: `two/lolo_diag.py lolo_run` / `lolo_score`. Disk only.

**From tx/PREREG_reanneal.md, unchanged:** stream (`two_instr.stream()`, U tokens dropped), held signs (6 C + 13 agreed S),
the 29 free signs (27 M + 4, S), stage 1 (`homophonic_anneal.solve`, fr17 4-gram, uni_w 1.0, 32 restarts, 40000 iters, held
fixed), planted control a/p/d at e with the same 29 free, gate >= 2 of 3 recovered, shuffled-value null (50 contexts),
nothing into key.tsv.

**Changed, with the reason (NOTES.md "C1161-LOLO step 1").**
1. **No stage 2, norm none.** The step-1 diagnosis found stage 2 (word cover) broke p even in the true context (D2) and
   collapsed 5 of 10 seeds (C1161RA), and nc2 rewards rare letters at this free share (D2, D3); stage 1 alone recovered
   the planted signs 3/3 on the real stream (D5) and 32/32 signs on a same-design synthetic (D4). The objective is the
   plain 4-gram sum per letter (L4); J has W = 0.
2. **Streams instead of seeds.** Six streams, each the full stream minus one leaf/block (c185R, c186R, c186L, c187L, c187R,
   c188L; N 2623-3155), seed 1 each. Consensus letter of a sign = its letter in >= 5 of 6 leaf streams.
3. **Headroom (rule 3).** The control's blind baseline for *this* instrument is D5: 3/3 planted recovered on the full stream
   in one seed, i.e. the gate is expected to pass; this is a licence gate (does the instrument recover known values in this
   context), not a gain gate, and the leaf streams are run for per-sign stability, not for a gain over the full stream.
   A pass here therefore licenses only "the instrument recovers planted C signs"; it does not make the target arm's values
   right (D6: the optimum scores like French at ~14% misread).

**Planted sign recovered** when (i) consensus (>= 5/6) is its true value and (ii) dJ = L4(K* with true) - L4(K* with e)
over K* (consensus key; the stream-1 key where none) exceeds the p95 of the 50-context shuffled-value null. **Gate >= 2 of
3**, else NON-TEST: stop, log, no target arm, no tuning.

**Target arm** (6 streams) only on GATE PASS. Per free sign: consensus value, how many leaf streams agree, key.tsv value,
dJ(consensus vs key.tsv) over K* and its null p95. Every value is a **proposal graded M**, written to NOTES.md and
HYPOTHESES.md with a ROOM line; nothing enters key.tsv (D6: no key brings the stream to French at the measured error, so a
proposal here is "the 4-gram optimum given the held signs", not a reading).
