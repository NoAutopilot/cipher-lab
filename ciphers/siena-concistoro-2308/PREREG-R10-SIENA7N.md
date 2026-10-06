# PREREG R10-SIENA7N -- no. 7 homophonic + nomenclator family (6 Oct 2026, 10:26 UTC by date -u, written before any scored run)

Worker R10-SIENA7N (account 4, LANE LANE-RUN10-account-4), brief `.claude/briefs/runs/2026-10-06-account4-run10-jobs.md`.
Script `specs/cheap-tests/siena-concistoro-2308/run_test_no07_nomen.py` (committed with this file); output `results_no07_nomen.json`.
Solver `tools/homophonic_anneal.py` `solve_nomen()` / `anneal_nomen()`, added by this job (Usage 8; offline test
`tools/tests/test_homophonic_nomen.py`); `tools/family_run.py` has no nomenclator family and no anchor option, so the job
uses the folder's own cheap-test script pattern (as R9-SIENA7) on the shared solver function.

**Material.** `transcripts/no07.tok` (agent J, 363 tokens, K=45, unchanged). Fixed: the seven C glosses q=a, 6=n, +=o, 2=e,
x=r, c=o, QP=e (as R9-SIENA7). Agent J's error on the whole letter (R10-SIENA7C): 0.8-7.0%.

**Design.** Every sign decodes to one letter or to one whole word from VOCAB (20 frequent Italian words/names: che et per non
il la di de del della con sua suo signoria signore duca re papa milano siena), each word on at most one sign; a move proposes
a word with probability 0.2; word_bonus 1.0 per extra character of a word token. 12 restarts x 60,000 iterations, order 3.
Multi-sign codes are modelled only as agent J already tokenised them (e.g. QP is one token); no regrouping of signs.

**Corpus (era).** tools/data/it16dip minus held-out gri_33125010469852 (Desjardins II), which gives the control plaintext.
**Not era-matched** (16th-c. Florentine/papal diplomatic Italian against a 1450s Sienese despatch); no 15th-c. Italian corpus
on disk.

**Matched control.** Per seed: held-out text, word-tokenised, cut into no. 7's 20 run lengths counted in tokens, where each
occurrence of a NOMEN word (che per non di la il con del signoria sua; 10 codes, a subset of VOCAB the solver is not told) is
one token and every other letter one token; letters get 35 homophones (largest remainder), each NOMEN word its own sign
(K about 42-45, N=363); seven letter signs nearest the target's fixed counts held fixed; then a share err of unfixed tokens
replaced by a random other sign, err in {0, 0.035, 0.07} (bracketing J's 0.8-7.0%). Seeds 1-5.

**Statistics.** token_acc = share of the 363 tokens whose decoded value (letter or word) equals the truth; nomen_recall =
share of NOMEN-word tokens decoded to the right word.

**Gate (both must hold).** (G1) mean token_acc >= 0.60 at err 0.07; (G2) mean nomen_recall >= 0.50 at err 0. G2 is there
because the family under test is the nomenclator layer: a control that reads the letters but never recovers a word code
cannot license any statement about the nomenclator on the target (rule 3, match the design; the letter layer alone is
R9-SIENA7's already-logged family). If either fails: stop, log "non-test at this N" for the homophonic + nomenclator family
on no. 7 (G1 or G2 named), do not run the target.

**If both pass.** Target (seeds 1-3, seven fixes) and order-shuffled target (seeds 1-3, ARM-C1 null); best-scoring decode
of each judged with `tools/judge_plaintext.py specs/siena-concistoro-2308.json --file <decode>` (FAIL reported as FAIL). A
PASS on any shuffled decode voids the judge as a gate for this family at this N. No value enters any key file above M.

**Development disclosed.** Before this file, the script was run on dev seeds 98 and 99 only (never 1-5) to settle the knobs
above: with word_bonus 0 the solver almost never assigns a word; with 2.0 and no uniqueness rule it piles long words on many
signs (token_acc 0.2-0.4); with uniqueness and 1.0, token_acc 0.66-0.90 and nomen_recall 0.00 on all four dev runs. G2 was
set after seeing that; it makes a licensed negative harder, not easier.
