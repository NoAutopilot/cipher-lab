# mccormick-1999 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 25 Sept 2026 18:41 | masc | N=746 K=24 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1 | 0.994 (0.989-0.999) | -2190.651 | PASS - mccormick-1999 (a PASS is a gate for a verifier, not a reading; rule 10) | yes (gate 0.6) | LANE B2 bMCC2 test2: masc vs default English corpus |
| 25 Sept 2026 18:42 | masc | N=746 K=24 restarts=8 corpus=pg1661_holmes_vdrop.txt+pg2701_mobydick_vdrop.txt | 1 | 0.985 (0.983-0.989) | -1958.813 | PASS - mccormick-1999 (a PASS is a gate for a verifier, not a reading; rule 10) | yes (gate 0.6) | LANE B2 bMCC2 test2: masc vs vowel-dropped English corpus |
| 25 Sept 2026 19:13 | homophonic | N=746 K=24 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1 | 0.999 (0.999-0.999) | not run (control-only) | - | yes | - |
| 25 Sept 2026 19:14 | homophonic | N=746 K=24 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1 | 0.998 (0.997-0.999) | -2190.651 | FAIL language: score=-1.48, null_p99=-2.071, real_p05=-0.864, real_median=-0.813, mode=both, N=746 | yes (gate 0.6) | LANE B3 bMCC3 test3: homophonic vs default English corpus |
| 25 Sept 2026 19:15 | homophonic | N=746 K=24 restarts=8 corpus=pg1661_holmes_vdrop.txt+pg2701_mobydick_vdrop.txt | 1 | 0.652 (0.058-0.992) | -1958.813 | FAIL language: score=-2.329, null_p99=-2.071, real_p05=-0.864, real_median=-0.813, mode=both, N=746 | yes (gate 0.6) | LANE B3 bMCC3 test3: homophonic vs vowel-dropped English corpus |
| 25 Sept 2026 19:18 | homophonic | N=746 K=24 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=1 | 1 | 0.998 (0.997-0.999) | -2547.687 | FAIL language: score=-1.807, null_p99=-2.071, real_p05=-0.864, real_median=-0.813, mode=both, N=746 | yes (gate 0.6) | LANE B3 bMCC3 test3: homophonic false-positive floor, target letters shuffled seed 1, default English corpus |
| 25 Sept 2026 19:18 | homophonic | N=746 K=24 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=2 | 1 | 0.998 (0.997-0.999) | -2569.063 | FAIL language: score=-1.839, null_p99=-2.071, real_p05=-0.864, real_median=-0.813, mode=both, N=746 | yes (gate 0.6) | LANE B3 bMCC3 test3: homophonic false-positive floor, target letters shuffled seed 2, default English corpus |
| 25 Sept 2026 19:19 | homophonic | N=746 K=24 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt shuffle_target=3 | 1 | 0.998 (0.997-0.999) | -2559.700 | FAIL language: score=-1.896, null_p99=-2.071, real_p05=-0.864, real_median=-0.813, mode=both, N=746 | yes (gate 0.6) | LANE B3 bMCC3 test3: homophonic false-positive floor, target letters shuffled seed 3, default English corpus |
| 25 Sept 2026 19:20 | homophonic | N=746 K=24 restarts=8 corpus=pg1661_holmes.txt+pg2701_mobydick.txt | 1 | 0.998 (0.997-0.999) | -2190.651 | FAIL language: score=-1.48, null_p99=-2.071, real_p05=-0.864, real_median=-0.813, mode=both, N=746 | yes (gate 0.6) | LANE B3 bMCC3 test3: homophonic vs default English corpus (rerun to preserve decode file separately from the vowel-dropped run, which shares the same output path) |

MCC-SWEEP (11 Oct 2026, 20:0x UTC by date -u, account 1, LANE DEFAULT-A1-1840; hand-written note outside the tool
table): token/nomenclator char-4-gram anneal (`specs/cheap-tests/mccormick-1999/token_anneal.py`), control-only length
sweep, PREREG-MCC-SWEEP.md. CONTROL type recovery mean 0.004 / 0.002 / 0.001 / 0.001, token recovery 0.003 / 0.036 /
0.001 / 0.010 at 132 / 500 / 2,000 / 8,000 tokens (3 seeds each; shuffled-order null token max 0.000-0.055); with the
temperature on the total log-prob scale (addendum 1): type 0.008 / 0.001 / 0.001 / 0.000, token 0.037 / 0.001 / 0.030 /
0.000. Gate 0.5 (type and token) met at no N; TARGET not run. Untestable by this instrument (as designed) at N <= 8,000;
not too-short, not refuted. Next: a word-level code-word anneal, control first (NOTES.md MCC-SWEEP).

MCC-WORD (14 Oct 2026, 22:28-22:42 UTC by date -u, account 2, LANE DEFAULT-A2-2209-14; hand-written note outside the tool
table): token/nomenclator family, second instrument -- word-level code-word anneal (`token_anneal.py --objective
wordbigram`: whole-word bigram LM, total-scale Gibbs anneal, code types from a 1,000-word pool), control-only sweep,
PREREG-MCC-WORD.md (e57f59f5f). Primary arm (LM held out from the control's source): CONTROL token recovery mean 0.069 /
0.108 / 0.104 / 0.106, type 0.020 / 0.007 / 0.003 / 0.002 at 132 / 500 / 2,000 / 8,000 tokens (3 seeds; shuffled-order
null token max 0.060 / 0.107 / 0.042 / 0.031; token ceiling 0.64-0.79). Diagnostic arm (LM in-sample): token 0.063 /
0.095 / 0.096 / 0.086, null max 0.129 / 0.109 / 0.101 / 0.092. Found total > truth total on all 24 runs: the objective's
optimum is not the truth (search not the limit). Read gate (token >= 0.5 and above null max) met at no N; TARGET not
run. Untestable by this instrument at N <= 8,000; not too-short, not refuted.

MCC-SKEL (15 Oct 2026, 02:21-02:3x UTC by date -u, account 1, LANE DEFAULT-A1-0206-15; hand-written note outside the tool
table): token/nomenclator family, third instrument -- abbreviation / consonant-skeleton lattice decoder (`token_anneal.py
--skeleton`, 3,000-word held-out pool, word-bigram LM), PREREG-MCC-SKEL.md (7fa695063, addenda e95515799, 7591b1785).
CONTROL word recovery mean, drop 0.618 / 0.650 / 0.661, keepfinal 0.654 / 0.710 / 0.717 at 132 / 500 / 2,000 tokens
(3 seeds); order-null max 0.651 / 0.655 / 0.667 and 0.701 / 0.726 / 0.737: read criterion met at no N (both arms).
CONTROL coverage at 132: 0.69-0.83 vs letter-null max 0.21-0.35 (power on every seed). TARGET (addendum 1) coverage:
drop 0.136 vs letter-null max 0.137 (not above: negative for this scheme); keepfinal 0.296 vs letter-null max 0.160 and
keep-final-letter null max 0.203 (above both; carried by -NSE/-RSE/-SE endings and WLD; far below the control's
0.69-0.81). No reading offered.

MCC-SUFX (15 Oct 2026, 05:4x-05:50 UTC by date -u, account 1, LANE DEFAULT-A1-0447-15; hand-written note outside the tool
table): token/nomenclator family, fourth instrument -- suffix-mark abbreviation model (`token_anneal.py --sufx`: drop-skeleton
stem + a mark SE/BE/E/none per ending class, class -> mark map fitted per text; 3,000-word held-out pool, word-bigram LM),
PREREG-MCC-SUFX.md (335740320). CONTROL (N = 132, the target's own N, kind sequence, token length and mark profile):
word recovery 0.709 / 0.603 / 0.617 (mean 0.643), mark-map recovery 0.962 / 0.965 / 0.987, coverage 0.887 / 0.818 / 0.816
vs type-mark null max 0.440 / 0.416 / 0.427: reads. TARGET: coverage 0.497 vs type null max 0.265 and type-mark null max
0.400; score per letter -2.940 vs -3.250 and -2.969 (40 nulls each, all four above). Preregistered wording: "the target's
stems fit the suffix-mark scheme beyond both type-keeping nulls" -- a candidate at M at best, no text, coverage far below
the control's 0.82-0.89; carried largely by NCBE (read nice) and short function-word stems. No reading offered.

MCC-JUDGE (15 Oct 2026, LANE DEFAULT-A1-0740-15; PREREG-MCC-JUDGE.md): NCBE-stem-keeping null on the MCC-SUFX target, 200
draws: coverage 0.497 vs max 0.435 (mean 0.372), score per letter -2.940 vs max -3.002 (p = 1/201 each); type-mark null
re-run at 200: max 0.401 / -2.979. Outcome: "the MCC-SUFX margin is not carried by NCBE alone"; NCBE share of the margin
0.17 (coverage) / 0.21 (score) -- corrects "carried largely by NCBE" above. judge_plaintext: candidate FAIL (A: language
-1.672 vs real_p05 -0.864; B: length 404 and language), both shuffled-decode controls FAIL (judge not voided); `en` corpus
fold spread makes the judge's verdict of unknown reliability. No reading offered.

## MCC-GREGG (15 Oct 2026, LANE DEFAULT-A1-0740-15): suffix-mark model with a Gregg 1916 shorthand lexicon
PREREG-MCC-GREGG.md (db504515e). Pool = top 3,000 LM-corpus words in the Gregg Shorthand Dictionary (1916) headwords + Manual
(1916) word-signs or inflecting one (14,630 words; 2,241 of 3,000 shared with MCC-SUFX's pool). Matched control N = 132,
3 seeds: word recovery 0.629 / 0.511 / 0.587 (mean 0.576, gate 0.5), mark map 0.962 / 0.965 / 0.957, coverage 0.840 / 0.762 /
0.775 vs type-mark null max 0.411 / 0.415 / 0.396 -> reads. Target: coverage 0.487 vs maxima 0.236 (type), 0.395 (type-mark),
0.396 (NCBE-fixed), p 1/201 each; score per letter -2.831 vs -3.090 (type), -2.830 (type-mark: 1 of 200 draws above, p 0.010),
-2.896 (NCBE-fixed). Preregistered outcome: "mixed" (one statistic misses one null maximum by one draw). Standardized margin
over the type-mark null, Gregg vs plain pool: coverage z 6.08 vs 6.43, score z 3.97 vs 4.31 -> "worse" by the PREREG word
(small): the Gregg vocabulary does not fit the stems better than a novel's. judge_plaintext: candidate FAIL (A: length 813
and language -1.653 vs real_p05 -0.870; B: length 434 and language -1.055 vs -0.864), both shuffled controls FAIL (judge not
voided; `en` fold spread, reliability unknown). No reading offered. Lexicon swaps on this instrument are now a knob (rule 3).

## MCC-CMU (15 Oct 2026, LANE DEFAULT-A1-1140-15): suffix-mark model with a phonetic (CMUdict) key -- family [retired]
PREREG-MCC-CMU.md (a6abb231c). Each word's code = phonetic skeleton of its base from CMUdict (commonest grapheme per consonant
phone) + the class mark; pool MCC-SUFX's plain 3,000. Matched control N = 132, 3 seeds: word recovery 0.690/0.546/0.617
(mean 0.618 >= 0.5), mark-map 0.967/0.830/0.987, coverage above type-mark null max on 3/3 -> reads. Target: coverage 0.488
above all three null maxima (type 0.301, type-mark 0.417, NCBE-fixed 0.421; p 0.005 each); score/letter -2.977 above type
(-3.210) and NCBE-fixed (-3.039) maxima but not type-mark (-2.938, p 0.020) -> "mixed". z over type-mark vs plain letter key:
coverage 5.38 vs 6.43, score 2.53 vs 4.31 -> "worse". Judge FAIL both renderings, shuffles FAIL (not voided). Third key on
the same instrument without the candidate row: suffix-mark family [retired], untested-by-this-tool (not refuted), rule 3.
