# DEB-SWARM-A log (French plaintext, homophonic letter substitution)

Group A of the Debosnys swarm, round 1 (brief `.claude/briefs/runs/2026-09-29-deb-swarm.md`). Worker DEB-SWARM-A.
Phase 1 is done on hand-planted texts because score.py was not frozen when this group started (no FROZEN line in
swarm/README.md at 03:01 UTC, 29 Sept 2026). Nothing in this file is a reading.

Tooling (all in this folder, regenerable):
- `prep_corpus.py` builds `work/train.txt`, which is letters only (a-z, accents stripped, no spaces), 5.02 M
  characters from tools/data/fr19 (five Gutenberg novels, 1830-1888) plus tools/data/fr18 (gazette). It also
  writes `work/verse_lines.txt` from tools/data/fr19v (Baudelaire, *Les Fleurs du Mal*). That verse is never
  trained on and is used only to plant controls.
- `hsolve.c` is a simulated-annealing homophonic solver. It scores with an interpolated conditional 5-gram
  (orders 1-5, fixed back-off weights, optional per-window floor `FLOOR`) plus a letter-frequency chi-square
  term (weight WF). A move reassigns one sign to one letter. The temperature falls linearly from T0 to 0, and the
  best of R restarts is kept. Build: `gcc -O3 -march=native -o work/hsolve hsolve.c -lm`.
- `plant.py` makes the hand-planted control. It draws a verse span of the target's token count and enciphers it
  homophonically, so that the sign-count curve equals the settled real text's curve ('_' dropped: c2 is N 688,
  K 128; c1 is N 134, K 59). It can add uniform type noise, meaning a share of tokens replaced by a random sign.
- `evalk.py` gives recovery, the share of tokens whose decoded letter equals the planted letter.

Standard setting below ("S1"): R 8, 5 M iterations, WF 0.3, T0 5, FLOOR -4 unless stated. One run is about 5 s
on one core.

| time (UTC, 29 Sept) | method | parameters | control result (recovery, planted) | real-text held-out | why it failed / note |
|---|---|---|---|---|---|
| 02:58 | SA, joint 5-gram log counts | R 8, 0.3 M it, WF 1, T0 0.6 | c2-shape clean seed 1: 0.302 | not run | too little search; see the next row |
| 02:59 | same | 3-10 M it, WF 0.3-1, T0 0.6-1.5 | c2 clean s1: 0.22-0.54 | not run | **model failure**: the found keys score above the true key (-7847 vs -8036). Joint 5-gram counts over-reward common letters, so wrong keys win. Switched to a conditional model. |
| 03:02 | SA, conditional interpolated 5-gram | T0 0.2-1.0, WF 0-1 | c2 clean s1: 0.03-0.27 | not run | search failure: the true key now scores higher (-1464 vs found -1720). At T0 below 1 the annealer freezes at once. WF 0 collapses into the all-'e' solution (-806, recovery 0.05), so the frequency term is required. |
| 03:04 | same | T0 2/4/8, WF 0.15/0.3 | c2 clean s1: T0 4 WF 0.3 gives **0.933**; T0 8 gives 0.895; T0 2 gives 0.233; WF 0.15 gives 0.318 | not run | this became setting S1 |
| 03:06 | S1 (no floor), 4 more seeds | seeds 2-5 | c2 clean: 0.881 / 0.929 / 0.962 / 0.906 (mean 0.92) | not run | **passes the 70 pct bar on a clean c2-sized planted control** |
| 03:06 | S1 (no floor) | c2 shape, 15 pct uniform type noise, seeds 2-5 | 0.219 / 0.263 / 0.458 / 0.206 | not run | fails |
| 03:06 | S1 (no floor) | c1 shape (N 134, K 59), clean, seeds 1-2 | 0.440 / 0.522 | not run | fails at c1's size even with no noise |
| 03:08 | S1 + FLOOR -4 / -6 | c2, 15 pct noise, seeds 2-5 | FLOOR -4: 0.250 / 0.340 / 0.429 / 0.590 (mean 0.40); FLOOR -6: 0.27-0.46 | not run | the floor helps a little but is still under the bar |
| 03:09 | true-key check at 15 pct noise | FLOOR -4 | the true key's own decode scores **-1763 / -1583**; the keys the solver found score **-1474 / -1465** | not run | **information limit, not search**: at 15 pct uniform noise the model prefers wrong keys to the true key. A 5-gram letter model cannot identify the key at this noise and length, however long it searches. The true key itself only reads 84-87 pct of tokens right, because the noise tokens carry other letters. |
| 03:10 | S1 + FLOOR -4, noise sweep | c2 shape, seeds 2-5 | 0 pct: 0.869 / 0.927 / 0.969 / 0.946 (mean 0.93). 5 pct: 0.765 / 0.872 / 0.888 / 0.810 (0.83). 10 pct: 0.721 / 0.824 / 0.772 / 0.436 (0.69). 15 pct: 0.40 (above) | not run | **crossover at about 10 pct uniform type noise**. The settled c2 is estimated at 14-17 pct type noise (NOTES.md, H21b), which is inside the failing band. |
| 03:14 | held-out emulation (`plant2.py`, `heldout_ctl.sh`, the solver's HELDOUT mode) | one key; A c2-shaped (N 688), B c1-shaped (N 134, 10 pct of tokens on signs unseen in A); fit S1+FLOOR -4 on one text, key fixed, scored on the other (signs unseen in the fit text stay unread), mean 5-gram log P per fully read window against 1000 value-shuffled keys | fit on A: recovery 0.94-0.98 clean, 0.46-0.85 at 10 pct, 0.34-0.52 at 15 pct. Fit on B: 0.34-0.41 clean, 0.16-0.38 noisy | not run | held-out percentile A to B: 100 / 100 / 100 clean; 97.6 / 100 / 100 at 10 pct; 98.1 / 100 at 15 pct. B to A: 100 / 100 / 100 clean; 98.7 / 94.2 / 100 at 10 pct; 89.3 / 100 at 15 pct. **A true French homophonic key can pass 99.9 in both directions at c1/c2 size, even at 10-15 pct noise in some seeds.** A key fitted on only 134 tokens still generalises (100th percentile at 34-41 pct recovery). This emulates the planned score.py and is not score.py. |
| 03:18 | NULL held-out control (`plantnull.py`) | no language: tokens iid from the c2 sign curve; same fit and held-out scoring; 24 seeds (48 directions) | percentiles 16-99.8, median about 91 (sorted, seeds 11-30: 38.7 67.8 73.9 76.4 80.5 84.2 84.2 84.9 85.2 85.4 87.9 89.0 89.0 90.5 90.5 90.9 91.0 91.2 91.3 91.4 91.8 92.7 92.9 93.2 93.6 93.6 93.7 93.9 94.3 94.6 95.0 97.4 98.2 98.3 98.3 98.5 99.6 99.7 99.8 99.8) | not run | **the value-shuffled null is inflated**: a key fitted to meaningless text matches sign frequency to letter frequency, and a value shuffle breaks that, so the real side wins without any language. 0 of 24 NULL pairs pass 99.9 in both directions, but 4 of 40 single directions reach 99.6-99.8. The bar holds, in the null's tail. ROOM flag to the orchestrator 03:0x. Mitigation used by this group: any real-text candidate is also run through an order-shuffled-fit null (fit the same method on the fit text with token order permuted, then the same held-out score). |
| 03:24 | S1+FLOOR -4 with word spaces (ALPHA 27; `work/train_sp.txt` 6.3 M chars with '{' as space) | plaintext verse with spaces kept; the planter gives space 7-8 homophones by frequency (space share 18-22 pct); c2 shape, seeds 2-5 | clean: 0.967 / 0.964 / 0.969 / 0.962 (letters only 0.96). 15 pct noise: 0.757 / 0.769 / 0.738 / 0.738 (letters only **0.725 / 0.740 / 0.699 / 0.702**) | not run | **word spaces carry the method over the bar at the real noise level** (0.70-0.74 letters only, against 0.25-0.59 without spaces). Relevant because X avoids line starts and ends (h19_x_position_settled.json: 1 line-initial and 2 line-final against 3-12 expected), which is how a space sign behaves. |
