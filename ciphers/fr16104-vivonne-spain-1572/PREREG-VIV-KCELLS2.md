# PREREG VIV-KCELLS2 (17 Oct 2026, written 03:3x UTC by date -u, before any scored run)

Worker VIV-KCELLS2 (account 4), brief .claude/briefs/runs/2026-10-17-acct4-research-director-5.md "## JOB VIV-KCELLS2". Disk only;
no key.tsv edit; trial cells live in tx/kcells2/key_trial.tsv (scratch). Script: tx/kcells2/kcells2.py.

## Question
VIV-KCELLS found the clerk's p under unkeyed reader label c (share 0.62, purity 0.75) and m under unkeyed label 2 (0.61, 0.69).
On the real ink-63 reading, do the trial cells c=p, 2=m (grade S-trial, counted as H) move the reading, and past AD 94.6?

## Inputs
- Ink 63: tx/viv63_decode.py lines() (the committed route; per-token reader-split flags kept; must reproduce reading_piece63.tsv's
  grades exactly before trial cells are added, else stop). Inks 53 and 54: reading_piece53.tsv / reading_piece54.tsv codes and grades
  (a U token c/2 becomes H under the trial; their per-token flags are not in the TSV -- declared liberty, reported only, not gated).
- Judge: tools/judge_plaintext.py NgramModel on tools/data/fr16 (the three files of tx/viv63_test.py); V_strict = tx/viv54L_stretch.py
  --strict vocabulary, as ERR-SIM.

## Statistics (per ink)
1. hrun: longest all-H run over the whole stream (ERR-SIM's runs(); before-check must give 40 on ink 63).
   **Declared before running: hrun depends on grades only, so every assignment of letters to c and 2 gives the identical hrun -- a
   value-shuffled control cannot differ from the target on it (CLAUDE.md rule 3, the orthogonal-control paragraph). hrun is reported,
   not gated against the shuffle.** The brief's "beat the shuffle on the all-H run" is therefore implemented as statistic 2.
2. hrunV (gated): the longest V_strict stretch (tx/viv54L_stretch.py stretches(), top 1) over the per-page decode with every non-H token
   replaced by '_' -- i.e. the longest all-H run that also parses into strict fr16 vocabulary (>= 3 words). Letter-sensitive.
3. V_strict: the same without the H mask (as ERR-SIM), reported.
4. s (gated, "b2 score"): fr16 NgramModel.score of the decoded letters (unread dropped), whole ink; plus the b2 letter-order-shuffle p99
   (200 draws, viv63_test's method) reported beside it.

## Controls, run before the real pair is scored
- K0 before: key.tsv as it stands (no trial cells).
- K1 value-shuffled: 20 draws, seed 'VIV-KCELLS2-shuf-<i>', c and 2 each assigned a letter uniformly from abcdefghiklnoqrstuxyz
  (folded alphabet minus j v w, minus the true pair p m).
- K2 swapped pair: c=m, 2=p.
- Then K3 real: c=p, 2=m.
Pass on ink 63: K3 > p99(K1) on hrunV AND on s, and K3 > K2 on both.

## Crossover (step 4)
tx/err_sim/err_sim.py run() unchanged, with load_key() extended by c->p and 2->m at grade C (ink 63's own frequencies come from
reading_piece63.tsv as ERR-SIM). confusion_AB.tsv has no row for c or 2 (32 signs learnt on f.102r): declared liberty -- each pass
reads c and 2 wrong at that pass's mean keyed-sign error rate (et = mean, so the injected e applies to them as to an average sign), the
wrong label drawn from the pass's pooled off-diagonal distribution. Levels 0.00 (C0 on extended key, reported) and 0.05/0.10/0.14/0.19/
0.23, seeds 1-5. Crossover = largest level at which >= 3 of 5 seeds give hrun >= 94.6 (and the same for hrun_correct, reported).

## Decision (registered)
- (a) K3 > p99(K1) on hrunV and s, and a run >= 94.6 (hrunV, or hrun if hrunV < hrun is the only route -- hrunV governs): a D2
  candidate clause exists -- write it out with liberties counted, name verifier step DV-VIV1, no key edit.
- (b) K3 > p99(K1) on both but < 94.6: cells are real, readers cap the clause -- report crossover vs measured 0.14; name the split
  (tile reader on tx/kcells2/packet.tsv priced per tile, or the owner's sort).
- (c) K3 <= p99(K1) on either: the labels are too impure to use as cells; the split comes first.
- If K2 >= K3 on either statistic, (c) regardless.
Packet (step 5) is written whatever the outcome.

## Decision
(Five-line form added after the run; Belief and Would-change restate the rules pushed in 8073e7c63 before any scored run, unchanged.)
Belief: labels c and 2 carry the clerk's p and m (VIV-KCELLS shares 0.62/0.61), so as trial cells they should lift ink 63's reading above a value-shuffle of the same two labels.
Would change it: K3 (c=p, 2=m) <= K1 value-shuffle p99 (20 draws) on hrunV or on the fr16 score s, or K2 swapped >= K3 -> branch (c), split first.
Observed: ink 63 hrunV K0 24 / K1 p99 26 / K2 26 / K3 26 (tie, not >); s K0 -1.5349 / K1 p99 -1.5276 / K2 -1.5441 / K3 -1.5289 (rank 3 of 21; l,s and s,s score higher); hrun (grade-only, shuffle-invariant) 40 -> 53; inks 53/54 also fail (s rank 13/21 and 1/21, hrunV ties). Crossover on the extended key: hrun >= 94.6 in 4/5 seeds at e=0 (94-143), 0/5 at 0.05 (43-62) -> crossover < 0.05 vs measured 0.14.
Decision: change -- branch (c): c and 2 are not usable as cells; split the labels at tx/kcells2/packet.tsv first, and the reader error (not only the cells) caps any ink-63 clause, since even a perfect p/m key reaches AD only at zero error.
Lesson: a value-shuffle judged on mean n-gram log-prob favours frequent letters, so rare-letter trial cells (p, m) can lose to s/n/l draws without being wrong -- a frequency-matched shuffle (draw letters at p/m's corpus rate) is the fairer null for a rare-letter cell; and the all-H run is invariant under any value shuffle by construction (rule 3), so it cannot gate a cell test.
