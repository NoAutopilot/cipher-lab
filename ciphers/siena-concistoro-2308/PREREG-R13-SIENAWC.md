# PREREG R13-SIENAWC -- nos. 7 + 19 pooled, nomenclator family with a structural word-code restriction (6 Oct 2026, 18:41 UTC by date -u, written before any scored run; header time corrected from a typed 18:47 after push, no content change)

Worker R13-SIENAWC (account 4, LANE LANE-RUN13-account-4), brief `.claude/briefs/runs/2026-10-06-account4-run13-jobs.md` (Wave 3).
Script `specs/cheap-tests/siena-concistoro-2308/run_test_pool719_wc.py` (committed with this file), output `results_pool719_wc.json`.
No dev runs were made before this file; the only runs so far are the offline unit test and a construction check (eligible-set sizes, no
solver call). Knobs are R10-SIENA7N's, frozen.

**Instrument (different from R10-SIENA7N / R13-SIENA719).** `tools/homophonic_anneal.py solve_nomen(..., word_signs=S)` (option added
in this job, offline test `tools/tests/test_homophonic_nomen.py` part 4; `word_signs=None` is bit-identical to the old call). A vocab
word may be proposed only for a sign in S. Target S: every unfixed sign agent J tokenised as a multi-character unit or as a
non-alphanumeric drawn mark (`len(s) > 1 or not s.isalnum()`): 27 of the pool's 55 unfixed signs, 110 of 481 tokens (oo 18, 7# 13, TRI 10,
DEL 8, sl 7, P_ 7, 6~ 6, SI 6, = 5, OB 4, PCT 3, TT 3, then 15 signs at 1-2). Single letter- or digit-shaped signs decode to letters only.

**Material, corpus, design.** Exactly PREREG-R13-SIENA719.md (nos. 7 then 19, agent J, 25 runs, N=481, K=62, seven C glosses fixed; VOCAB 20,
NOMEN 10, 12 restarts x 60,000 iters, order 3, word_prob 0.2, word_bonus 1.0, it16dip minus Desjardins II, not era-matched).
Matched control: R13-SIENA719's control construction unchanged, plus the same restriction: S = the 10 NOMEN signs (the design assumption
being tested: a nomenclator's word codes are drawn signs) + 17 unfixed letter homophones chosen greedily to match the target's eligible-sign
counts left after each NOMEN sign removes its nearest target count. Construction check: 27 eligible signs, 142-147 eligible tokens (target
110), so the control's restriction is slightly looser than the target's, not tighter. err in {0, 0.035, 0.07}, seeds 1-5.
The control can vary on the statistic (nomenclator recall depends on which sign the solver puts each word on, which the restriction changes).

**Gate (unchanged from R10-SIENA7N / R13-SIENA719).** (G1) mean token_acc >= 0.60 at err 0.07; (G2) mean nomen_recall >= 0.50 at err 0.
Baseline headroom: unrestricted at this N, G2 read 0.122 (R13-SIENA719), so the gate has headroom; the question is whether the restriction
alone lifts G2. If either gate fails: stop, log "CONTROL BELOW GATE, non-test at pooled N=481" for this *restricted* instrument (a different
instrument, first attempt with it); do not run the target.

**If both pass.** Target (seeds 1-3) and order-shuffled target (seeds 1-3, ARM-C1 null), best decode of each judged with
`tools/judge_plaintext.py specs/siena-concistoro-2308.json --file <decode>` (FAIL reported as FAIL); a PASS on any shuffled decode voids the
judge as a gate. No value enters any key file above M; any reading goes to a verifier.
