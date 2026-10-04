# riksarkivet-r4282-1628 -- hypothesis families

Append-only. CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row. No
`tools/family_run.py` row exists yet for this target (bRIK's R4284 key-test crib, 26 Sept 2026, is in NOTES.md
"Test run" and `report.json`); the rows below are written by `scripts/clear_cribs.py` (RIK-CRIBS, 2 Oct 2026)
from `cribs/clear_cribs_report.json`, and `scripts/clear_cribs.py --check` re-derives them (rule 7).

## RIK-CRIBS (2 Oct 2026, account-4): R4282's own clear-Latin phrases as pattern cribs

Instrument: `tools/crib_pattern.py` (H28), used as a library with the same `run`/`shuffle_groups`/`pct` as the
CLI: homophones allowed (R4284's key-test leaf shows e with three signs, s with four), no wild, no skip, drag
never crosses the page boundary (`--group-col page`, 864 + 230 signs), score = the implied partial key applied to
the whole 1,094-sign stream under the la18 unigram (tools/data/la18, Zaluski 1709-11, the only wired Latin
corpus). Three controls per row: (1) the tool's own 200 shuffled-order copies of each page; (2) a NEGATIVE CRIB of
the same folded length drawn from la18 tomus I (no word shared with the leaf's clear phrases, OCR junk filtered by
a 20-occurrence floor), run under identical settings -- the floor for "the real text places any crib more easily
than its shuffle"; (3) a POSITIVE CONTROL: a synthetic la18 letter of the same N=1094 and K=34 with the phrase
embedded once and enciphered by a homophonic key of R4284's shape (24 letters, the 10 extra signs as second
homophones of the most frequent letters), 100 shuffles -- does the instrument find a phrase of this length at
this N when the transcription is clean. "rank a/200" = how many shuffles reach the real value (0 = above every
shuffle). P1 is Bourdeau's three brackets run as one 37-letter phrase; P1a/P1b are its first and third brackets.
Agreement with bRIK's key = sign -> majority letter of the R4284 key-test crib (`cribs/brik_crib_key_compare.tsv`,
13 signs compared, 4 ties left out), the maximum over every consistent placement, not only the top one.

| date (UTC) | family | crib (folded length) | max-err | TARGET placements (vs shuffled-order mean / p95 / max; rank) | TARGET best score (vs shuffled p95; rank) | NEGATIVE CRIB placements (vs its shuffles p95; rank) | NEGATIVE CRIB best (vs its p95; rank) | POSITIVE CONTROL (synthetic, true placement found / rank; best vs p95) | max agree with bRIK key, any placement (target / negative) | label |
|---|---|---|---|---|---|---|---|---|---|---|
| 2 Oct 2026 | crib_pattern (H28 tool) | P1 'et qualis sit eius futurus status dubitatur' (37) | 0 | 0 (vs 0.0 / 0 / 0; 200/200 at or above) | -- (vs --; --/200) | 0 'joannis ad brandeburgicum nos serenitatem' (vs 0; 200/200) | -- (vs --; --/200) | found rank 1 of 1; top key right 15/15; best -2.772 vs p95 -- (rank 0/100) | -- / -- | RIK-CRIBS |
| 2 Oct 2026 | crib_pattern (H28 tool) | P1 'et qualis sit eius futurus status dubitatur' (37) | 1 | 0 (vs 0.0 / 0 / 0; 200/200 at or above) | -- (vs --; --/200) | 0 'joannis ad brandeburgicum nos serenitatem' (vs 0; 200/200) | -- (vs --; --/200) | found rank 1 of 1; top key right 15/15; best -2.772 vs p95 -- (rank 0/100) | -- / -- | RIK-CRIBS |
| 2 Oct 2026 | crib_pattern (H28 tool) | P1 'et qualis sit eius futurus status dubitatur' (37) | 2 | 0 (vs 0.0 / 0 / 0; 200/200 at or above) | -- (vs --; --/200) | 0 'joannis ad brandeburgicum nos serenitatem' (vs 0; 200/200) | -- (vs --; --/200) | not run (err 2) | -- / -- | RIK-CRIBS |
| 2 Oct 2026 | crib_pattern (H28 tool) | P1a 'et qualis sit' (11) | 0 | 201 (vs 113.95 / 143 / 172; 0/200 at or above) | -2.574 (vs -2.523; 81/200) | 239 'fata ei jam ab' (vs 172; 0/200) | -2.446 (vs -2.422; 42/200) | found rank 8 of 159; top key right 1/11; best -2.608 vs p95 -2.563 (rank 31/100) | 2 / 2 | RIK-CRIBS |
| 2 Oct 2026 | crib_pattern (H28 tool) | P1a 'et qualis sit' (11) | 1 | 639 (vs 447.64 / 493 / 546; 0/200 at or above) | -2.538 (vs -2.445; 170/200) | 691 'fata ei jam ab' (vs 555; 0/200) | -2.400 (vs -2.354; 131/200) | found rank 46 of 531; top key right 1/10; best -2.541 vs p95 -2.486 (rank 49/100) | 2 / 2 | RIK-CRIBS |
| 2 Oct 2026 | crib_pattern (H28 tool) | P1a 'et qualis sit' (11) | 2 | 948 (vs 812.91 / 856 / 883; 0/200 at or above) | -2.470 (vs -2.390; 135/200) | 970 'fata ei jam ab' (vs 898; 0/200) | -2.391 (vs -2.330; 196/200) | not run (err 2) | 2 / 2 | RIK-CRIBS |
| 2 Oct 2026 | crib_pattern (H28 tool) | P1b 'futurus status dubitatur' (22) | 0 | 0 (vs 0.2 / 1 / 3; 200/200 at or above) | -- (vs -2.700; --/200) | 0 'ac non mei ideo non quia fic' (vs 0; 200/200) | -- (vs -2.583; --/200) | found rank 1 of 2; top key right 11/11; best -2.729 vs p95 -2.716 (rank 2/100) | -- / -- | RIK-CRIBS |
| 2 Oct 2026 | crib_pattern (H28 tool) | P1b 'futurus status dubitatur' (22) | 1 | 3 (vs 2.19 / 6 / 13; 66/200 at or above) | -2.751 (vs -2.675; 71/200) | 1 'ac non mei ideo non quia fic' (vs 4; 111/200) | -2.595 (vs -2.591; 10/200) | found rank 3 of 5; top key right 2/18; best -2.667 vs p95 -2.696 (rank 1/100) | 1 / 0 | RIK-CRIBS |
| 2 Oct 2026 | crib_pattern (H28 tool) | P1b 'futurus status dubitatur' (22) | 2 | 28 (vs 15.56 / 26 / 34; 9/200 at or above) | -2.693 (vs -2.627; 125/200) | 12 'ac non mei ideo non quia fic' (vs 17; 47/200) | -2.558 (vs -2.536; 32/200) | not run (err 2) | 2 / 1 | RIK-CRIBS |
| 2 Oct 2026 | crib_pattern (H28 tool) | P2 'sed tamen ut res' (13) | 0 | 76 (vs 43.79 / 67 / 88; 1/200 at or above) | -2.611 (vs -2.592; 57/200) | 84 'pari ter san dei' (vs 63; 1/200) | -2.522 (vs -2.476; 60/200) | found rank 15 of 95; top key right 1/13; best -2.617 vs p95 -2.606 (rank 13/100) | 2 / 2 | RIK-CRIBS |
| 2 Oct 2026 | crib_pattern (H28 tool) | P2 'sed tamen ut res' (13) | 1 | 418 (vs 240.57 / 287 / 301; 0/200 at or above) | -2.568 (vs -2.552; 52/200) | 402 'pari ter san dei' (vs 275; 0/200) | -2.478 (vs -2.443; 108/200) | found rank 74 of 359; top key right 3/12; best -2.612 vs p95 -2.574 (rank 77/100) | 3 / 3 | RIK-CRIBS |
| 2 Oct 2026 | crib_pattern (H28 tool) | P2 'sed tamen ut res' (13) | 2 | 788 (vs 582.05 / 637 / 664; 0/200 at or above) | -2.568 (vs -2.520; 165/200) | 774 'pari ter san dei' (vs 627; 0/200) | -2.465 (vs -2.399; 178/200) | not run (err 2) | 3 / 3 | RIK-CRIBS |
| 2 Oct 2026 | crib_pattern (H28 tool) | P3 'tractatus magnas admodum' (22) | 0 | 0 (vs 0.06 / 0 / 3; 200/200 at or above) | -- (vs -2.755; --/200) | 0 'fe bellorum modis unde non' (vs 0; 200/200) | -- (vs -2.749; --/200) | found rank 1 of 1; top key right 15/15; best -2.834 vs p95 -2.821 (rank 1/100) | -- / -- | RIK-CRIBS |
| 2 Oct 2026 | crib_pattern (H28 tool) | P3 'tractatus magnas admodum' (22) | 1 | 1 (vs 1.11 / 4 / 12; 107/200 at or above) | -2.901 (vs -2.767; 77/200) | 2 'fe bellorum modis unde non' (vs 3; 35/200) | -2.775 (vs -2.749; 11/200) | found rank 1 of 3; top key right 15/15; best -2.834 vs p95 -2.780 (rank 14/100) | 0 / 0 | RIK-CRIBS |
| 2 Oct 2026 | crib_pattern (H28 tool) | P3 'tractatus magnas admodum' (22) | 2 | 16 (vs 8.96 / 18 / 25; 19/200 at or above) | -2.801 (vs -2.733; 112/200) | 13 'fe bellorum modis unde non' (vs 13; 13/200) | -2.775 (vs -2.716; 93/200) | not run (err 2) | 2 / 0 | RIK-CRIBS |
| 2 Oct 2026 | crib_pattern (H28 tool) | P4 'Mittatur nobis responsum' (22) | 0 | 0 (vs 0.04 / 0 / 3; 200/200 at or above) | -- (vs -2.695; --/200) | 0 'fi ne in locis quam materia' (vs 0; 200/200) | -- (vs -2.557; --/200) | found rank 1 of 1; top key right 15/15; best -2.642 vs p95 -2.777 (rank 0/100) | -- / -- | RIK-CRIBS |
| 2 Oct 2026 | crib_pattern (H28 tool) | P4 'Mittatur nobis responsum' (22) | 1 | 0 (vs 0.79 / 4 / 10; 200/200 at or above) | -- (vs -2.681; --/200) | 1 'fi ne in locis quam materia' (vs 3; 68/200) | -2.685 (vs -2.556; 39/200) | found rank 1 of 3; top key right 15/15; best -2.642 vs p95 -2.687 (rank 0/100) | -- / 0 | RIK-CRIBS |
| 2 Oct 2026 | crib_pattern (H28 tool) | P4 'Mittatur nobis responsum' (22) | 2 | 8 (vs 6.08 / 14 / 22; 63/200 at or above) | -2.748 (vs -2.643; 148/200) | 9 'fi ne in locis quam materia' (vs 15; 45/200) | -2.595 (vs -2.536; 62/200) | not run (err 2) | 1 / 1 | RIK-CRIBS |


Top placement per target row (grade M at most, rule 4; none is a reading):

- P1a-err0: start 892 (errs 0, score -2.5741, cov 454): agrees with bRIK on 0 of 3 compared signs {}, conflicts {'c': 'e!=n', 'g': 't!=r', 'o': 'l!=m'}; key 7=i 8=s M=i b=u c=e e=s g=t o=l q=a r=t u=q
- P1a-err1: start 24 (errs 1, score -2.5379, cov 409): agrees with bRIK on 0 of 2 compared signs {}, conflicts {'k': 't!=u', 'c': 'i!=n'}; key 4=a 7=i D=t E=q b=e c=i k=t m=l n=u u=s
- P1a-err2: start 238 (errs 2, score -2.4701, cov 359): agrees with bRIK on 0 of 2 compared signs {}, conflicts {'k': 'e!=u', 'L': 'i!=p'}; key 4=a E=u L=i M=i e=q f=t k=e m=s r=t
- P1b-err1: start 691 (errs 1, score -2.7508, cov 734): agrees with bRIK on 0 of 7 compared signs {}, conflicts {'L': 'u!=p', 'k': 'r!=u', 'l': 's!=p', 'o': 'a!=m', 'g': 'u!=r', 'p': 'd!=a', 't': 'i!=e'}; key 4=u 5=a 7=t D=b L=u M=u a=t e=s g=u k=r l=s m=f n=s o=a p=d r=r t=i u=t
- P1b-err2: start 25 (errs 2, score -2.6927, cov 711): agrees with bRIK on 0 of 6 compared signs {}, conflicts {'k': 'f!=u', 'c': 'u!=n', 'l': 's!=p', 'g': 'u!=r', 'L': 't!=p', 'o': 'a!=m'}; key 4=u 5=d 7=t 8=r D=a E=u F=u L=t M=u c=u e=t g=u h=t k=f l=s m=r n=t o=a q=i u=s
- P2-err0: start 851 (errs 0, score -2.6108, cov 462): agrees with bRIK on 1 of 4 compared signs {'t': 'e'}, conflicts {'k': 't!=u', 'p': 'u!=a', 'g': 'e!=r'}; key 4=n 7=m S=t T=d b=a e=r f=e g=e h=s k=t p=u t=e u=s
- P2-err1: start 84 (errs 1, score -2.5684, cov 484): agrees with bRIK on 0 of 5 compared signs {}, conflicts {'l': 'e!=p', 'L': 'e!=p', 'g': 'n!=r', '3': 't!=s', 't': 'r!=e'}; key 3=t 7=a A=d L=e M=e b=u g=n l=e q=t t=r u=s x=m
- P2-err2: start 84 (errs 1, score -2.5684, cov 484): agrees with bRIK on 0 of 5 compared signs {}, conflicts {'l': 'e!=p', 'L': 'e!=p', 'g': 'n!=r', '3': 't!=s', 't': 'r!=e'}; key 3=t 7=a A=d L=e M=e b=u g=n l=e q=t t=r u=s x=m
- P3-err1: start 25 (errs 1, score -2.9013, cov 711): agrees with bRIK on 0 of 6 compared signs {}, conflicts {'k': 't!=u', 'c': 'a!=n', 'l': 'n!=p', 'g': 's!=r', 'L': 'm!=p', 'o': 'o!=m'}; key 4=c 5=a 7=s 8=m D=m E=r F=g L=m M=u c=a e=a g=s h=d k=t l=n m=t n=a o=o q=d u=t
- P3-err2: start 18 (errs 2, score -2.801, cov 669): agrees with bRIK on 2 of 6 compared signs {'k': 'u', 'c': 'n'}, conflicts {'3': 'a!=s', 'i': 'a!=t', 'l': 'd!=p', 'g': 'm!=r'}; key 3=a 4=a 5=u 7=a D=t E=s F=o a=r b=t c=n e=m g=m i=a k=u l=d m=g n=m q=c u=a
- P4-err2: start 25 (errs 2, score -2.7477, cov 711): agrees with bRIK on 0 of 6 compared signs {}, conflicts {'k': 'm!=u', 'c': 't!=n', 'l': 's!=p', 'g': 'e!=r', 'L': 'o!=p', 'o': 'n!=m'}; key 4=t 5=r 7=n 8=m D=o E=i F=i L=o M=u c=t e=b g=e h=s k=m l=s m=a n=t o=n q=p u=u

Reading of the table: at max-err 0 the three 22-letter phrases and the 37-letter phrase place NOWHERE in the
real stream, where the design-matched synthetic places each at its true start, rank 1, key right 15/15 (the
instrument has power at this length and N when the transcription is clean). At max-err 1-2 the real stream admits
1-28 placements, which is what its own shuffles (p95 4-26) and the negative crib (1-13) also admit, and no best
score beats the shuffled p95 (ranks 52-165 of 200). The two short cribs (11 and 13 letters) place freely in the
target (above the shuffled p95), but so does their negative crib, and the positive control cannot rank the true
placement either (rank 8-74, top key right 1/13): below the instrument's resolution at this N. Maximum agreement
with bRIK's R4284 crib key over every placement is 3 of ~12 signs, matched exactly by the negative crib's 3. No
partial key, no anchor. Conditional (rule 2/3): the positive control is error-free, while Bourdeau's transcription is a
single pass with no measured error rate; max-err 2 covers at most 2 misreads in a 22-sign window (about 9%), so a
transcription noisier than that would make the 22-letter rows a non-test, not a negative (the SALV-DIAG lesson).

## FT4 (3 Oct 2026, account-4): shelf-neighbour keys R4280/R4281 -- not run

No row: both keys are numeric-only (2-, 3- and 4-digit codes) and share no sign with R4282's letter-shape
alphabet, so a decode would cover 0 of 1,094 signs and a shuffled-key control could not differ from it (rule 3).
Stopped at the overlap check per the brief; see NOTES.md "## FT4".

## GAPS (3 Oct 2026, account-4): DECODE key 4327 (II:154, Oxenstierna-Sadler, 1620s) on the shared signs
| family | control | control number | target number | verdict |
|---|---|---|---|---|
| known key 4327, third-column signs (7 shared: E L x A M T o), Latin unigram mean logp over 214/1110 tokens | (a) same letters permuted among the 7 signs, 2000; (b) 7 random Latin letters, 2000 | (a) mean -4.399, p95 -3.716; (b) mean -3.744, p95 -2.904 | real -4.357; frac(a)>=real 0.50, frac(b)>=real 0.84 | no fit on the shared signs (key at the permutation median); conditional on Bourdeau's one-pass transcription and an M-grade eye read of the key's sign column |
Script: scripts/key4327_overlap.py (--check exits 0); numbers in key4327_overlap.json.

## GAPS67 (3 Oct 2026, account-4): homophonic into Swedish (sv17) -- the language series closes
| family | control | control number | target number | verdict |
|---|---|---|---|---|
| homophonic, sv17 (new: AOSB 6 vols, 2.52M letters), N 1090 K 34 profile=target | 5 x 16, noise 0 / 0.034 | 0.993 (0.986-1.000) / 0.950 (0.929-0.965); scores -2254 to -2596 | best -3067; shuffled -3339/-3330; judge FAIL -1.254 (real_p05 -0.879; held-out sv17 min -1.155, p01 -1.043) | control-backed negative for Swedish |
| homophonic letter substitution, four languages (la17/la18 GAPS42/57, de17 GAPS62, fr17 GAPS65, sv17 GAPS67) | each 0.92-0.95 at 3.4% error | -- | target 470-670 points under every control and below the held-out real minimum each time; 235-270 points above its own shuffles each time | retired as untested-by-this-tool for further languages (rule 3 third-attempt): the design, not the language, is the next variable |

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 3 Oct 2026 06:56 | homophonic | N=1090 K=34 restarts=8 corpus=zaluski_epistolae_t1.txt.gz+zaluski_epistolae_t2.txt.gz+zaluski_epistolae_t3.txt.gz profile=target,noise=0.034 | 1-3 | 0.725 (0.261-0.960) | not run (control-only) | - | yes | GAPS42 control, la18, noise 3.4pct |
| 3 Oct 2026 06:58 | homophonic | N=1090 K=34 restarts=16 corpus=zaluski_epistolae_t1.txt.gz+zaluski_epistolae_t2.txt.gz+zaluski_epistolae_t3.txt.gz profile=target,noise=0 | 1-5 | 0.992 (0.981-0.998) | not run (control-only) | - | yes | GAPS42 control, la18, noise 0 |
| 3 Oct 2026 07:01 | homophonic | N=1090 K=34 restarts=16 corpus=zaluski_epistolae_t1.txt.gz+zaluski_epistolae_t2.txt.gz+zaluski_epistolae_t3.txt.gz profile=target,noise=0.06 | 1-5 | 0.834 (0.518-0.924) | not run (control-only) | - | yes | GAPS42 control, la18, noise 0.06 |
| 3 Oct 2026 07:04 | homophonic | N=1090 K=34 restarts=16 corpus=zaluski_epistolae_t1.txt.gz+zaluski_epistolae_t2.txt.gz+zaluski_epistolae_t3.txt.gz profile=target,noise=0.10 | 1-5 | 0.620 (0.502-0.866) | not run (control-only) | - | yes | GAPS42 control, la18, noise 0.10 |
| 3 Oct 2026 07:07 | homophonic | N=1090 K=34 restarts=16 corpus=zaluski_epistolae_t1.txt.gz+zaluski_epistolae_t2.txt.gz+zaluski_epistolae_t3.txt.gz profile=target,noise=0.034 | 1 | 0.948 (0.935-0.960) | -2950.256 | FAIL language: score=-1.262, null_p99=-1.674, real_p05=-0.978, real_median=-0.894, mode=both, N=1090 | yes (gate 0.6) | GAPS42 target, la18 |
| 3 Oct 2026 07:09 | homophonic | N=1090 K=34 restarts=16 corpus=zaluski_epistolae_t1.txt.gz+zaluski_epistolae_t2.txt.gz+zaluski_epistolae_t3.txt.gz profile=target,noise=0.034,shuffle_target=1 | 1 | 0.960 (0.960-0.960) | -3156.528 | FAIL language: score=-1.338, null_p99=-1.674, real_p05=-0.978, real_median=-0.894, mode=both, N=1090 | yes (gate 0.6) | GAPS42 shuffled target 1, la18 |
| 3 Oct 2026 07:10 | homophonic | N=1090 K=34 restarts=16 corpus=zaluski_epistolae_t1.txt.gz+zaluski_epistolae_t2.txt.gz+zaluski_epistolae_t3.txt.gz profile=target,noise=0.034,shuffle_target=2 | 1 | 0.960 (0.960-0.960) | -3143.202 | FAIL language: score=-1.338, null_p99=-1.674, real_p05=-0.978, real_median=-0.894, mode=both, N=1090 | yes (gate 0.6) | GAPS42 shuffled target 2, la18 |
| 3 Oct 2026 07:35 | homophonic | N=1090 K=34 restarts=16 corpus=zaluski_epistolae_t1.txt.gz+zaluski_epistolae_t2.txt.gz+zaluski_epistolae_t3.txt.gz nulls=0.1,noise=0 | 1-5 | 0.984 (0.969-0.994) | not run (control-only) | - | yes | GAPS50 control, nulls 0.1, la18, noise 0 |
| 3 Oct 2026 07:38 | homophonic | N=1090 K=34 restarts=16 corpus=zaluski_epistolae_t1.txt.gz+zaluski_epistolae_t2.txt.gz+zaluski_epistolae_t3.txt.gz nulls=0.1,noise=0.034 | 1 | 0.859 (0.720-0.949) | -2950.256 | FAIL language: score=-1.262, null_p99=-1.674, real_p05=-0.978, real_median=-0.894, mode=both, N=1090 | yes (gate 0.6) | GAPS50 target, nulls 0.1, la18 |
| 3 Oct 2026 07:39 | homophonic | N=1090 K=34 restarts=16 corpus=zaluski_epistolae_t1.txt.gz+zaluski_epistolae_t2.txt.gz+zaluski_epistolae_t3.txt.gz nulls=0.1,noise=0.034,shuffle_target=1 | 1 | 0.720 (0.720-0.720) | -3156.528 | FAIL language: score=-1.338, null_p99=-1.674, real_p05=-0.978, real_median=-0.894, mode=both, N=1090 | yes (gate 0.6) | GAPS50 shuffled target 1, nulls 0.1, la18 |

## GAPS53 (3 Oct 2026, account-4): wordcode family (letter-or-word nomenclator), not matched
| family | control | control number | target number | verdict |
|---|---|---|---|---|
| wordcode, digits 3 4 5 7 8 as code signs (share 0.195) | tool control, la18, 1 seed x 2 restarts, err 0 | blended 0.963; code class 0.429 (n=14); control code share 0.013 | not run | non-test: control cannot reach the target's code share |
| wordcode, 8 rarest types as code signs (share 0.054) | same | blended 0.957; code class 0.000 (n=17); control code share 0.016 | not run | non-test: same |
| count bound, n dedicated word-code types | n commonest la18 words coded in a spelt stream | Latin max share n=3 0.0079, n=8 0.0136, n=20 0.0218 | R4282 rarest-n share n=3 0.0110, n=8 0.0541, n=20 0.3367 | >= 3 dedicated code signs do not fit R4282's counts in Latin; untested-by-this-tool, not refuted |
Scripts: gaps53/share_bound.py (--check exits 0); timing rows gaps53/control_calibration.md.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 3 Oct 2026 08:35 | homophonic | N=1090 K=34 restarts=16 corpus=dieverhandlungen01irme.txt.gz+dieverhandlungen02irme.txt.gz+dieverhandlungen03irme.txt.gz+urkundenundacten1601berluoft.txt.gz+urkundenundacte32kommgoog.txt.gz profile=target,noise=0 | 1-5 | 0.974 (0.927-1.000) | not run (control-only) | - | yes | GAPS62 control, de17, noise 0 |
| 3 Oct 2026 08:39 | homophonic | N=1090 K=34 restarts=16 corpus=dieverhandlungen01irme.txt.gz+dieverhandlungen02irme.txt.gz+dieverhandlungen03irme.txt.gz+urkundenundacten1601berluoft.txt.gz+urkundenundacte32kommgoog.txt.gz profile=target,noise=0.034 | 1 | 0.923 (0.848-0.960) | -3060.431 | FAIL language: score=-1.423, null_p99=-2.046, real_p05=-0.849, real_median=-0.749, mode=both, N=1090 | yes (gate 0.6) | GAPS62 target, de17 |
| 3 Oct 2026 08:41 | homophonic | N=1090 K=34 restarts=16 corpus=dieverhandlungen01irme.txt.gz+dieverhandlungen02irme.txt.gz+dieverhandlungen03irme.txt.gz+urkundenundacten1601berluoft.txt.gz+urkundenundacte32kommgoog.txt.gz profile=target,noise=0.034,shuffle_target=1 | 1 | 0.936 (0.936-0.936) | -3321.644 | FAIL language: score=-1.652, null_p99=-2.046, real_p05=-0.849, real_median=-0.749, mode=both, N=1090 | yes (gate 0.6) | GAPS62 shuffled target 1, de17 |
| 3 Oct 2026 08:42 | homophonic | N=1090 K=34 restarts=16 corpus=dieverhandlungen01irme.txt.gz+dieverhandlungen02irme.txt.gz+dieverhandlungen03irme.txt.gz+urkundenundacten1601berluoft.txt.gz+urkundenundacte32kommgoog.txt.gz profile=target,noise=0.034,shuffle_target=2 | 1 | 0.936 (0.936-0.936) | -3329.767 | FAIL language: score=-1.579, null_p99=-2.046, real_p05=-0.849, real_median=-0.749, mode=both, N=1090 | yes (gate 0.6) | GAPS62 shuffled target 2, de17 |
| 3 Oct 2026 09:03 | homophonic | N=1090 K=34 restarts=16 corpus=bub_gb_OIQItRIybmIC.txt.gz+bub_gb_wBJLsV8B_BgC.txt.gz+lettresdepeiresc01peiruoft.txt.gz+lettresdepeiresc02peiruoft.txt.gz+lettresdejeancha01chap.txt.gz+lettresducardina01maza.txt.gz profile=target,noise=0 | 1-5 | 0.988 (0.979-1.000) | not run (control-only) | - | yes | GAPS65 control, fr17, noise 0 |
| 3 Oct 2026 09:05 | homophonic | N=1090 K=34 restarts=16 corpus=bub_gb_OIQItRIybmIC.txt.gz+bub_gb_wBJLsV8B_BgC.txt.gz+lettresdepeiresc01peiruoft.txt.gz+lettresdepeiresc02peiruoft.txt.gz+lettresdejeancha01chap.txt.gz+lettresducardina01maza.txt.gz profile=target,noise=0.034 | 1 | 0.941 (0.928-0.949) | -2933.506 | FAIL language: score=-1.278, null_p99=-1.895, real_p05=-0.858, real_median=-0.788, mode=both, N=1090 | yes (gate 0.6) | GAPS65 target, fr17 |
| 3 Oct 2026 09:07 | homophonic | N=1090 K=34 restarts=16 corpus=bub_gb_OIQItRIybmIC.txt.gz+bub_gb_wBJLsV8B_BgC.txt.gz+lettresdepeiresc01peiruoft.txt.gz+lettresdepeiresc02peiruoft.txt.gz+lettresdejeancha01chap.txt.gz+lettresducardina01maza.txt.gz profile=target,noise=0.034,shuffle_target=1 | 1 | 0.947 (0.946-0.949) | -3168.891 | FAIL language: score=-1.433, null_p99=-1.895, real_p05=-0.858, real_median=-0.788, mode=both, N=1090 | yes (gate 0.6) | GAPS65 shuffled target 1, fr17 |
| 3 Oct 2026 09:08 | homophonic | N=1090 K=34 restarts=16 corpus=bub_gb_OIQItRIybmIC.txt.gz+bub_gb_wBJLsV8B_BgC.txt.gz+lettresdepeiresc01peiruoft.txt.gz+lettresdepeiresc02peiruoft.txt.gz+lettresdejeancha01chap.txt.gz+lettresducardina01maza.txt.gz profile=target,noise=0.034,shuffle_target=2 | 1 | 0.947 (0.946-0.949) | -3185.433 | FAIL language: score=-1.448, null_p99=-1.895, real_p05=-0.858, real_median=-0.788, mode=both, N=1090 | yes (gate 0.6) | GAPS65 shuffled target 2, fr17 |
| 3 Oct 2026 09:25 | homophonic | N=1090 K=34 restarts=16 corpus=rikskanslerenax00akadgoog.txt.gz+rikskanslerenax00palagoog.txt.gz+rikskanslerenax00styfgoog.txt.gz+rikskanslerenax01palagoog.txt.gz+rikskanslerenax02akadgoog.txt.gz+rikskanslerenax03akadgoog.txt.gz profile=target,noise=0 | 1-5 | 0.993 (0.986-1.000) | not run (control-only) | - | yes | GAPS67 control, sv17, noise 0 |
| 3 Oct 2026 09:28 | homophonic | N=1090 K=34 restarts=16 corpus=rikskanslerenax00akadgoog.txt.gz+rikskanslerenax00palagoog.txt.gz+rikskanslerenax00styfgoog.txt.gz+rikskanslerenax01palagoog.txt.gz+rikskanslerenax02akadgoog.txt.gz+rikskanslerenax03akadgoog.txt.gz profile=target,noise=0.034 | 1 | 0.950 (0.929-0.965) | -3067.467 | FAIL language: score=-1.254, null_p99=-1.917, real_p05=-0.879, real_median=-0.815, mode=both, N=1090 | yes (gate 0.6) | GAPS67 target, sv17 |
| 3 Oct 2026 09:29 | homophonic | N=1090 K=34 restarts=16 corpus=rikskanslerenax00akadgoog.txt.gz+rikskanslerenax00palagoog.txt.gz+rikskanslerenax00styfgoog.txt.gz+rikskanslerenax01palagoog.txt.gz+rikskanslerenax02akadgoog.txt.gz+rikskanslerenax03akadgoog.txt.gz profile=target,noise=0.034,shuffle_target=1 | 1 | 0.929 (0.929-0.929) | -3338.711 | FAIL language: score=-1.472, null_p99=-1.917, real_p05=-0.879, real_median=-0.815, mode=both, N=1090 | yes (gate 0.6) | GAPS67 shuffled target 1, sv17 |
| 3 Oct 2026 09:30 | homophonic | N=1090 K=34 restarts=16 corpus=rikskanslerenax00akadgoog.txt.gz+rikskanslerenax00palagoog.txt.gz+rikskanslerenax00styfgoog.txt.gz+rikskanslerenax01palagoog.txt.gz+rikskanslerenax02akadgoog.txt.gz+rikskanslerenax03akadgoog.txt.gz profile=target,noise=0.034,shuffle_target=2 | 1 | 0.929 (0.929-0.929) | -3329.540 | FAIL language: score=-1.505, null_p99=-1.917, real_p05=-0.879, real_median=-0.815, mode=both, N=1090 | yes (gate 0.6) | GAPS67 shuffled target 2, sv17 |
| 3 Oct 2026 09:41 | periodic_masc | N=1090 K=34 restarts=8 corpus=hugonisgrotiiepi00grot.txt.gz+hugonisgrotiiad00oxengoog.txt.gz+bub_gb_WTkBFjX6G_UC.txt.gz+bub_gb_FK3cWikzFwsC.txt.gz+bub_gb_mBpUAAAAcAAJ.txt.gz+epistolaecelebe00grotgoog.txt.gz period=2,noise=0.034 | 1-3 | 0.101 (0.002-0.156) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | GAPS69 control+target, period 2, la17, noise 0.034 |
| 3 Oct 2026 09:48 | periodic_masc | N=1090 K=34 restarts=16 corpus=hugonisgrotiiepi00grot.txt.gz+hugonisgrotiiad00oxengoog.txt.gz+bub_gb_WTkBFjX6G_UC.txt.gz+bub_gb_FK3cWikzFwsC.txt.gz+bub_gb_mBpUAAAAcAAJ.txt.gz+epistolaecelebe00grotgoog.txt.gz period=2,noise=0,iters=200000 | 1-3 | 0.181 (0.059-0.361) | not run (control-only) | - | no | GAPS69 clean control, period 2, la17, 16x200k |

## GAPS69 (3 Oct 2026, account-4): periodic design, label-free coset test (gaps69/period_test.py)
| family | control | control number | target number | verdict |
|---|---|---|---|---|
| periodic, P=2 independent alphabets, continuous phase | 3 la17 windows N 1090, 2 random keys over 34 signs, 3.4% redrawn; 2000 permutations each | TVD 0.587-0.624 vs perm p95 0.152-0.156, p 0.0005 (3/3 detected) | TVD 0.110 vs perm p95 0.160, p 0.88; dIC p 0.94 | excluded at this N, conditional on the GAPS38 transcription |
| periodic, P=2, phase reset per line | 2000 permutations | - | TVD 0.135 vs p95 0.160, p 0.36 | no separation |
| periodic, P=3-8, continuous phase | 2000 permutations each (no positive control run at P>2) | - | no P reaches p95 (lowest P=5: dIC p 0.074, TVD p 0.157) | no separation |
| periodic_masc solver (family_run.py rows above) | la17, P=2, 3.4% error 3x8 / clean 3x16x200k | 0.101 / 0.181, below gate 0.6 | not run | non-test by this tool |

## AOSB-PAIRS (4 Oct 2026, account 3): fixed-key crossmatch of the 1629 Oxenstierna-Strasburg table (AOSB I:4 letter 231)

Pre-registered in `aosb/PREREG-AOSB-PAIRS.md` before scoring; `aosb/aosb_crossmatch.py --check` re-derives `aosb/results.json`.
la17 4-gram mean log10/letter, runs >= 4 letters; null = 200 within-class meaning permutations.

| date (UTC) | family | CONTROL (LOFO on the 16 AOSB footnotes) | CONTROL at target size | TARGET | verdict |
|---|---|---|---|---|---|
| 4 Oct 2026 | fixed key key_aosb1629.tsv | C 0.957, S -1.056 vs null p99 -1.484 (0/200 >=), real p05 -0.992 | 20/20 subsets of 273 letters pass (S -1.09 to -0.995) | R4284 body: C 0.678, S -2.226 vs null mean -1.999 / p99 -1.670 (0.96 >= real) | NO FIT (control-backed) |
| 4 Oct 2026 | fixed key, exact shared signs | same | -- | R4282: C 0.044 (lambda only) | inapplicable (C < 0.5) |
| 4 Oct 2026 | fixed key, capitals -> lowercase shapes | same | -- | R4282: C 0.267, 8 letters | inapplicable (C < 0.5) |
