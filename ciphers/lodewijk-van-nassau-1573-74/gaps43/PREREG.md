# GAPS43 pre-registration (3 Oct 2026, written ~07:0x UTC, committed before any control or target run)

Step (NOTES.md "Remaining gaps" gap 4 Verdict): word-level global reassignment for 4612 seeded from key_full, scored
by fr16 word segmentation, gated first on the 5811 cut with 20% of codes perturbed at >= 0.90.

## Third-attempt check (CLAUDE.md rule 3 clause; HYPOTHESES.md)
Hypothesis H-S (4612 v3 is key_full's table with some codes reassigned) is unchanged. Retired for it: tools/key_repair.py
(local per-code search, fr16 order-5 char logp; AX2-4612S/S2/S3). Failed once: the char order-3 key-seeded anneal (AX2-4612,
0.699). This step is a different instrument on both axes those used: a GLOBAL search (simulated annealing: single-code
reassignment and two-code swap moves, Metropolis) against a WORD-SEGMENTATION objective, not a character model. That
objective is the one AX2-4612S3's postmortem named as untried; it is GAPS28's pre-registered cost (bandtest/band_seg.py
seg_cost: 1.0 per letter not inside an fr16 lexicon word + 0.1 per word; lexicon = folded fr16 corpus words len >= 2,
count >= 5). Attempt 1 of this instrument.

## Fixed parameters (no tuning after the first run)
- Alphabet: 23 folded letters (no J/U/W). Codes reassigned: key_full rows 1-120 with a single-letter value; other codes
  break a run (word_share_check_v3.py rule). Run breaks from the transcription are kept.
- Anneal: 60000 iterations x 6 restarts per seed, T geometric 1.5 -> 0.05, swap-move share 0.3, best total cost kept.
- Script: gaps43/word_anneal.py (this commit).

## Control (run first; target refused if it fails)
5811's real ciphertext cut to 4612 v3's N (833 value-1-120 numerals, word_share_check_v3.load_runs), key_full known to
read it. Seeds 1-3: a fresh random 20% of the keyed codes present get a different random letter, then the anneal runs.
Recovery = share of the 833 sign occurrences whose final letter equals key_full's.
GATE: recovery >= 0.90 in EACH of the 3 seeds. Also reported (not gating): start recovery before annealing (the control
can move either way, rule 3 can-differ), codes repaired of those perturbed, false moves on unperturbed codes, and an
unperturbed key_full start (seed 0) as a null check.

## Target (only if the control gate passes)
4612 v3 (ciphertext_4612_v3.tsv) annealed from unperturbed key_full, seeds 1-3; the same annealer on 3 token-order
shuffles of 4612 v3 (run lengths kept) is the shuffled-target check. 4612 READS only if its best word share
(word_share_check_v3 statistic, fr16 words >= 3 letters) is > the max over the 3 shuffled runs AND >= 0.85 x the
control's mean annealed word share. Even then: every reassigned code is grade S at best (S only if all 3 seeds agree),
each change to an H/C key_full code is a logged conflict (rule 4), key_full.tsv and readings are NOT changed by this job;
a READ goes to a verifier as "reading ready".
