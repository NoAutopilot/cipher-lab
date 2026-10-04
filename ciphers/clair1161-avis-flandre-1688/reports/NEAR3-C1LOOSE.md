## NEAR3-C1LOOSE (4 Oct 2026)

Account 2 worker for LANE-NEAR3, brief `.claude/briefs/runs/2026-10-04-ytbiz-near3-wave1.md`. Box 01:15-02:15 UTC; done 01:3x.
Disk only, no network, no subagent calls. Pre-registration `tx/PREREG_loose.md` (commit 32dd3ba0, pushed before any run).
Script `glossctl/loose.py` (imports `repair.align` and `glossctl` unchanged); rows `glossctl/loose.tsv`, log `glossctl/loose_run.log`,
keys `glossctl/loose_real_key.tsv`, `glossctl/loose_shufN_key.tsv` (column `unrepaired` = the value before any repair).
Tool shelf ("gloss-seeded key repair with a shuffled-gloss control"): nothing fits -- `key_repair.py` is retired (rule 3, Nassau)
and is a code-by-code repair without a gloss alignment; the other hits are running-key / seeded-code / key-order tools.
The procedure reuses READ2-C1161B's own `repair.py`.

**Setup as pre-registered.** Alignment = repair.py's edit-distance DP of the 220-sign c186R block to the 170 gloss letters, cost key
= the unrepaired READ2-C1161 key (rebuilt from key.tsv's "was 'x'" sources; checked: block vs gloss 0.594). Rule: >= 3 aligned
occurrences and majority letter >= 60%. Re-anneal homophonic_anneal seed 1, restarts 32, fr16 order 3, 924-sign stream. Control: same
procedure with the gloss shuffled within itself, seeds 1-10. Gate: real c185R judge > max of 10 shuffles AND > -1.128.

| run | signs held | held != unrepaired key | anneal score | block vs real gloss | c185R judge language (fr16, N 704) |
|---|---|---|---|---|---|
| **real gloss, loose** | 13 | 0 | -2277.4 | 0.588 | **-1.146** (FAIL; cover 0.908) |
| shuffled 1 | 5 | 0 | -2278.4 | 0.594 | **-1.130** (best control) |
| shuffled 2 | 8 | 3 | -2492.2 | 0.565 | -1.309 |
| shuffled 3 | 3 | 0 | -2277.9 | 0.588 | -1.143 |
| shuffled 4 | 5 | 0 | -2277.8 | 0.588 | -1.150 |
| shuffled 5 | 2 | 0 | -2350.4 | 0.288 | -1.179 |
| shuffled 6 | 4 | 0 | -2280.0 | 0.565 | -1.144 |
| shuffled 7 | 5 | 0 | -2278.7 | 0.588 | -1.145 |
| shuffled 8 | 4 | 0 | -2284.1 | 0.594 | -1.133 |
| shuffled 9 | 2 | 0 | -2278.7 | 0.600 | -1.133 |
| shuffled 10 | 3 | 0 | -2281.6 | 0.582 | -1.145 |
| strict real repair (READ2-C1161B, reference) | 6 | 0 | -2278.5 | 0.612 | -1.128 |

Thresholds: null_p99 -1.70, real_p05 -0.949. Shuffled controls: max -1.130, median -1.145, mean -1.161.

**Pre-registered outcome: FAIL.** Target -1.146 vs best control -1.130 (and vs strict -1.128): the real-gloss loose repair is below
both, and sits at the control median. Block vs gloss is also not higher than the controls (0.588 vs 0.565-0.600, excluding shuf5).

**Signs held (real gloss):** + = e (15/18), 4 = o (8/9), 9 = s (2/3), d = n (5/5), e = p (7/7), iii = e (5/6), p = c (3/3), qb = a (9/12),
th = s (5/7), w = i (5/6), wb = l (6/8), y = r (6/7), z = t (3/4). All 13 already had these values in the unrepaired key: as in the
strict run, the repair confirms, it corrects nothing. The strict rule's a = u, ee = y and sd = g fall below the >= 3 floor here.
**Signs that moved in the re-anneal (real gloss), from -> to:** 6r i->l, 8 l->d, K u->f, L b->i, c f->d, dia i->l, iib d->l, l r->n,
tz l->a, vdash d->t, x a->u (11). Per run in `loose.tsv` column `moved_vs_unrepaired`.

**What the controls show beyond the gate (read these before the pooled job).**
1. *The alignment cannot propose a correction.* Its cost is 0 only where the key already gives the gloss letter, so the majority
   letter of a sign's aligned occurrences is, in practice, the key's own letter: 9 of 10 shuffled glosses also held only signs whose
   value equals the key (column 4). A held set is a subset of the key's values chosen by a gloss-driven filter; it can raise or lower
   the anneal's free-sign choices, not fix a wrong sign. A third pass with a different threshold on this alignment would be the same
   instrument (rule 3, third-attempt clause): the next instrument is an alignment whose cost does not read the key (e.g.
   `tools/interlinear_align.py`'s hard-EM over the block/gloss pair, grade C from the gloss alone), or more glossed material.
2. *The same moves recur whatever the gloss.* 8 l->d, vdash d->t, iib d->l, K u->f, L b->*, l r->*, x a->*, tz l->* appear in the real
   run and in most shuffled runs. They are the anneal's own second basin once any few signs are held, not gloss evidence. That covers
   the 10 signs READ2-C1161B's strict repair moved (8 l->d, K u->f, L b->n, c f->s, iib d->l, l r->s, phi s->l, tz l->e, vdash d->t,
   x a->s), now in key.tsv at grade S: they carry no support from the gloss.
3. *The strict-rule margin is inside this 10-shuffle band.* The strict repair's -1.128 beat its own 3 shuffles (-1.177..-1.243), but
   three of these ten loose-rule shuffles reach -1.130, -1.133, -1.133. These are different-rule controls, so this does not formally
   re-test the strict rule, but with 10 seeds a +0.002 to +0.005 margin is not distinguishable from holding an arbitrary few key-agreeing
   signs. Suggestion for the lane (not done here, no brief): re-run the strict rule with 10 shuffles before the pooled job relies on
   the strict repair's 10 moved signs.

key.tsv and the reading were not touched. Recommendation for the pooled re-anneal: do not adopt the loose-rule key; treat the 10
strict-repair moves as unsupported by the gloss (S, same as any anneal value).

Report what was found and where it was not found: no outside source searched; novelty not classified. Requests: none (disk only).
Subagent calls: 0. Cost: see the lane ledger.
