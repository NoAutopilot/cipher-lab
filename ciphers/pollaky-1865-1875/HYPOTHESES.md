# pollaky-1865-1875 -- hypotheses (append-only)

Opened 3 Oct 2026 (GAPS156, account-4). Rule 3: each family row carries its matched control beside the target.

## Ad 2 (1871 telegram), 10x10 homophonic bigram design (Ernst's sibling prior) -- GAPS156, 3 Oct 2026

Statistic: non-overlapping bigram IC, phase 0. Null: 200 uniform digit strings of the same length. Controls: synthetic
10x10 homophonic encipherments of English (tools/data en sources), A = frequency-proportional, B = random allocation.
Script: scripts/bigram_prior.py (seed 156). Pre-registered in NOTES.md before scoring (commit dca24eee).

| text | N bigrams | target IC | null p95 | null tail | control A power | control B power | verdict |
|---|---|---|---|---|---|---|---|
| ad 2 1871 | 57 | 0.0138 | 0.0144 | 0.085 | 0.053 | 0.869 | A: non-test (untestable by bigram IC at N=57); B: inconclusive |
| sib 1864 | 25 | 0.0267 | 0.0200 | 0.010 | 0.030 | 0.345 | below power both variants: no licence |
| sib 1865 | 28 | 0.0185 | 0.0185 | 0.125 | 0.048 | 0.440 | below power both variants: no licence |

Status of the hypothesis: untested-by-this-tool for design A (not refuted); open for design B.

## Ad 1 (1865 sign script), Laura's bars-x-dots component rule -- GAPS160, 3 Oct 2026

(3 Oct 2026, GAPS174: the 1881 print settles sign 04 as 4 dots, so the "Laura's sign 04" row below is the primary row.)

Statistic T: mean add-one bigram log10 prob of "timeto"+X+"shall" (clear frame as crib); W: word-segmentation coverage.
Controls at N=10: A 2000 shuffled-sign orders, B 2000 random-sign strings over the rule's 21 cells, C 104 sibling
rules. Positive control: 2000 corpus windows over a-u. Script: scripts/laura_rule.py (seed 160). Pre-registered in
NOTES.md before scoring (commit 577aeea6).

| text | X | target T | A p95 (tail) | B p95 (tail) | C rank | W vs B p95 | power (T / W) | verdict |
|---|---|---|---|---|---|---|---|---|
| ad 1, our table | bencabuchp | -1.1405 | -1.2895 (0.002) | -1.2026 (0.019) | 1/104 | 0.6 vs 0.6 | 0.981 / 0.868 | supported on T (design candidate); W does not clear |
| ad 1, Laura's sign 04 | bendabuchp | -1.1074 | -1.2555 (0.001) | -1.2045 (0.005) | 1/104 | 0.5 vs 0.6 | same | same |

Status: supported as a design candidate on letter-bigram order (post-hoc rule; C weak by construction); no word read,
10 letters M.

GAPS178 re-score, 3 Oct 2026 (frame right side "ishall" from the 1881 print; sensitivity re-score under PREREG-GAPS178,
commit b480322e, not covered by GAPS160's pre-registration; scripts/laura_rule.py --right ishall, laura_rule_ishall.tsv):

| text | X | target T | A p95 (tail) | B p95 (tail) | C rank | W vs B p95 | power (T / W) | verdict |
|---|---|---|---|---|---|---|---|---|
| ad 1, sign 04 = 4 dots (primary) | bendabuchp | -1.0835 | -1.2261 (0.000) | -1.1844 (0.003) | 1/104 | 0.5 vs 0.6 | 0.985 / 0.868 | survives the corrected frame on T; W does not clear |
| ad 1, sign 04 = 3 dots (variant) | bencabuchp | -1.1150 | -1.2581 (0.002) | -1.1851 (0.013) | 1/104 | 0.6 vs 0.6 | same | same |

Status unchanged: supported as a design candidate on T (post-hoc rule); no word read, 10 letters M.

## Ad 2 (1871 telegram) = Boyouk's 1867 "ELOPED" clear ad, one group per 1-3-word chunk -- GAPS164, 3 Oct 2026

Statistic S: log10 share of monotone alignments (each group 1-3 consecutive words) in which the two "91" groups cover
identical chunks. Control: 2000 same-length windows of period English prose (Holmes 1892, Huck Finn 1884, Pride 1813).
Positive control: 200 synthetic chunk codes from fresh windows. Script: scripts/boyouk_align.py (seed 164). Pre-registered
in NOTES.md before scoring (commit f065906d).

| plaintext | groups | S target | control p95 (tail) | power | verdict |
|---|---|---|---|---|---|
| whole ad (73 words) | 36 split | -2.962 | -2.330 (0.384) | 0.335 | untestable |
| minus address (64) | 36 split | -1.970 | -1.983 (0.045) | 0.315 | untestable |
| whole ad | 35 joined | -2.795 | -2.394 (0.268) | 0.375 | untestable |
| minus address | 35 joined | -2.080 | -2.088 (0.048) | 0.320 | untestable |

Status: untested-by-this-tool at N=36 with one repeated group (power < 0.5), not refuted.

## Ad 2 (1871 telegram) = Baertl's digit-sum letter code (comment #1, 16 June 2017) -- GAPS169, 3 Oct 2026

Statistic T: best mean trigram log10 score a fixed simple-substitution hill-climber (8 restarts x 1500 moves) reaches on
the digit-sum sequence (27->26). Null: 200 uniform-random same-shape digit strings. Positive: 100 English windows of the
same N through a random letter -> sum map. Script: scripts/baertl_digitsum.py (seed 169). Pre-registered in NOTES.md
before scoring (commit 1ecd9062).

| sequence | N | T target | null p95 (tail) | null median | positive median | power | verdict |
|---|---|---|---|---|---|---|---|
| our 36 sums | 36 | -0.9606 | -0.7747 (0.995) | -0.8479 | -0.8426 | 0.210 | non-test (ceiling) |
| Baertl's 46 values | 46 | -0.8689 | -0.7674 (0.555) | -0.8608 | -0.8497 | 0.220 | non-test (ceiling) |

Status: untested-by-this-tool at N=36-46 (null median within 0.01 of positive median), not refuted; instrument retired
for this hypothesis. Baertl's own 46 values duplicate an 8-value run of the 36 sums and add two, and his reading maps
sum 7 to both B and W.

## Ad 1 (1865 sign script), topic crib from sibling clear ad Clay 1465 under Laura's rule -- GAPS174, 3 Oct 2026

Sign 04 = 1 dash + 4 dots (1881 print, Clay item 1459, IA leaf n280, component count). Statistic M: max positional matches of
X against 29 word-start 10-letter windows of the 1465 text plus 14 fixed paraphrases. Controls at N=10: A 2000 shuffled-sign,
B 2000 random-sign, C 104 sibling rules; positives P1 exact crib, P2 crib with 3 letters replaced. Script:
scripts/topic_crib.py (seed 174). Pre-registered in NOTES.md before scoring (commit 587ce6ea).

| X | M target | A p95 (tail) | B p95 (tail) | C rank | power P1 / P2 | verdict |
|---|---|---|---|---|---|---|
| bendabuchp | 2 | 3 (0.813) | 3 (0.770) | 21/104 | 1.000 / 1.000 | not read under this rule (this crib set only) |

18/29 windows unencodable under the rule (no v-z); 0/29 fit the sign-repeat pattern under any simple substitution (random 0.55%).
Status: the 1465 wording and the listed paraphrases are not the plaintext under Laura's rule; topic and design not refuted.

## GAPS182 (3 Oct 2026, account-4): independent test of Laura's rule on a sibling sign ad
Not run: no second ad in ad 1's dot-and-bar script was found. A script scan of all of Clay 1881 found none
(scripts/sign_sibling_scan.py; positive control: ad 1, item 1459, flagged), and Schmeh's twelve-ad list has none.
| target | control | result |
|---|---|---|
| none (no sibling text) | n/a (no N, no power) | not runnable on the material on disk; GAPS160 T support stays unreplicated |
Status: needs new material (a second sign-script ad: Palmer/Gaffney or the Times 1865-1871 beyond Clay). Not a negative.
