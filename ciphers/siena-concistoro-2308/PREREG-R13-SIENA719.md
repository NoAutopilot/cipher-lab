# PREREG R13-SIENA719 -- nos. 7 + 19 pooled, homophonic + nomenclator family (6 Oct 2026, 18:08 UTC by date -u, written before any scored run; header time corrected from a typed 18:13 after push, no content change)

Worker R13-SIENA719 (account 4, LANE LANE-RUN13-account-4), brief `.claude/briefs/runs/2026-10-06-account4-run13-jobs.md`.
Script `specs/cheap-tests/siena-concistoro-2308/run_test_pool719_nomen.py` (committed with this file), a thin wrapper that imports
R10-SIENA7N's `run_test_no07_nomen.py` and replaces only the material; output `results_pool719_nomen.json`. No dev runs of any kind
were made before this file (the knobs are R10-SIENA7N's, frozen, its own dev disclosure applies).

**Material.** `transcripts/no07.tok` (363 tokens) then `transcripts/no19.tok` (118 tokens), both agent J (Bourdeau), one naming
convention; `|` clear-text breaks in no. 19 split a run. Pool: 25 runs, N=481, K=62 (union; 20 types shared). Pooling assumes one key
across both letters (same sign name = same value); R13-SIENAJ supports a common letter/digit sign stock, which says nothing about a
common key. The seven C glosses of no. 7 (q=a, 6=n, +=o, 2=e, x=r, c=o, QP=e) are held fixed wherever the sign occurs (five of them
also occur in no. 19).

**Design, corpus, statistics.** Exactly PREREG-R10-SIENA7N.md: VOCAB 20 words, NOMEN 10 control codes, 12 restarts x 60,000 iters,
order 3, word_prob 0.2, word_bonus 1.0, corpus it16dip minus the held-out Desjardins II (not era-matched). Matched control at the
pooled N=481 and K=62 (10 NOMEN signs + 52 letter homophones), cut into the pool's 25 run lengths, seven letter signs nearest the
target's fixed counts held fixed, injected error err in {0, 0.035, 0.07} (J's measured 0.8-7.0% bracket on no. 7), seeds 1-5.

**Gate (both must hold, unchanged from R10-SIENA7N).** (G1) mean token_acc >= 0.60 at err 0.07; (G2) mean nomen_recall >= 0.50 at
err 0. Ceiling note (rule 3): R10-SIENA7N's control at N=363 read token_acc 0.855 but nomen_recall 0.043, so G2 has headroom; the
question this run answers is whether 118 more tokens (word codes now seen ~1.3x as often) lift G2. If either gate fails: stop, log
"CONTROL BELOW GATE, non-test at pooled N=481" for the homophonic + nomenclator family on the pool, do not run the target.

**If both pass.** Target (seeds 1-3) and order-shuffled target (seeds 1-3, ARM-C1 null); best decode of each judged with
`tools/judge_plaintext.py specs/siena-concistoro-2308.json --file <decode>` (FAIL reported as FAIL); a PASS on any shuffled decode
voids the judge as a gate for this family at this N. No value enters any key file above M; any reading goes to a verifier.
