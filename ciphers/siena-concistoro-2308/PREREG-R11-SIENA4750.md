# PREREG R11-SIENA4750 -- no. 7 against key R4750's nomenclator (6 Oct 2026, written 14:03 UTC by date -u, pushed before scoring)

Question (R10-SIENA7N / R11-SIENAPOOL step (b)): do the word codes of key R4750 (ASSi Concistoro fasc. 1, "a messer Lionardo e messer
Antonio ambasciatori a Milano 1454") occur in no. 7 (R4796, the Milan-embassy despatch naming Lionardo Benvoglienti), in the places
where no. 7's letter-layer fit (R9-SIENA7) leaves rare, poorly-fitting signs?

Key source: Bourdeau's agent G transcription `targets/siena1421/keys/R4750.txt` (dbourdeau/cyphersolver @ adbf9a1, CC BY 4.0), read
from full-resolution crops and re-checked on the image by agent G against no. 7 (`transcripts/no07_reading.txt`). The brief's vision
passes are skipped because the key is already transcribed on disk (brief: "skip passes if the key is already transcribed on disk"); for
the same reason no DECODE login is made. Target: `transcripts/no07.tok` (agent J, 363 tokens, 11 runs; a run = one line's cipher
stretch between clear words). No pooling with nos. 19/9.

R4750 nomenclator as transcribed: 45 names, of which 6 are numeral codes (97, 19, 88, 23, 72, 15), 3 drawn signs (papa_sign, tent_oo,
C_oo) and 36 written words (gallus, pesce, Volpe, fede, Villa, Aqua, luna, Leo, ...).

## T1 (scored): numeral codes as adjacent digit pairs

Statistic M = number of adjacent token pairs inside a run, read as a two-digit string, that equal one of {97, 19, 88, 23, 72, 15}.
No. 7's "1" (upright stroke, i/1) is read as digit 1. 7# and 6~ are not digits.
Controls (each can change M):
(a) 2000 order shuffles: tokens permuted within each run (run lengths and contents fixed; adjacency changes).
(b) 2000 code-set shuffles: six random distinct two-digit codes drawn from digits 1-9, one of them a doubled digit (as 88), the rest
    two different digits; M recomputed on the real stream for each set.
Gate PASS iff p_a = (#(a) M >= M_real + 1)/(2001) <= 0.05 AND p_b computed the same way <= 0.05.
Power (decides negative vs non-test): 200 synthetic streams = an order shuffle of no. 7 with k=4 code occurrences planted (each
replaces two adjacent tokens at a random place inside a run of length >= 2 with one of the six codes, chosen uniformly; 4 = about
the per-code rate of R10-SIENA7N's nomenclator control scaled to six codes); each scored with 500 + 500 shuffles. Power = share
PASS. Power < 0.8 -> a miss is a NON-TEST at this N.

## T2 (scored): written code words among no. 7's clear words

Agent J's clear words inside the cipher lines L02-L12 (every bracketed word in those lines of `transcripts/no07.txt` @ adbf9a1,
"(?)" and "?" stripped, abbreviation brackets expanded as J wrote them, words of >= 4 letters, lower case). A match = Levenshtein
distance <= 1 between a clear word and an R4750 code word (lower case, the uncertain alternatives in parentheses included: Corno,
falcone, ficus, venenum, storpsi, Senectus, Moncellino, furore).
Statistic W = number of clear words matching any code word.
Control: 2000 random lists of 36 words drawn from tools/data/it16dip word types (letters only, >= 4 letters) with each list's length
distribution matched to the 36 written code words; W recomputed. Gate PASS iff p = (#W_ctrl >= W_real + 1)/2001 <= 0.05 and W_real >= 1.
(T2 cannot use an order control: W does not depend on order.)

## T3 (descriptive, no gate): rare signs vs R4750's drawn codes, nulls and duplices

The low-count signs of no. 7 (count <= 3) and their per-token cost under R9-SIENA7's seed-1 fit (-log10 of the it16dip letter-bigram
probability of the decoded letter given the previous decoded letter, mean over its occurrences; "high-cost" = above the median over
all 363 tokens) are listed beside the R4750 sign whose agent-G description is closest to agent J's description, with the gloss where
one exists. This concordance is fixed in this file now, from the two legends alone, before T1/T2 are run:

| no. 7 sign (J) | n | closest R4750 sign (G) and its role | likeness |
|---|---|---|---|
| PCT (x with rings on two arms, %) | 3 | per (u) | close |
| # (double slanted upright crossed by a bar) | 1 | hash (null) | close |
| 8o (circle on stem, second circle below) | 1 | dumbbell (o) | close; gloss over 8o is i(?) |
| THETA (circle, bar inside) | 1 | o_bar (o) | loose (G's bar projects outside) |
| G (large circle, stroke inside) | 1 | G_dot (mm) | loose |
| HEART (solid filled triangle) | 1 | shield_o (null) | loose |
| TU (bowl with flat bar on top) | 2 | taurus (z) | loose |
| VO (v with ring on top) | 1 | taurus (z) | loose |
| H (two uprights and bar) | 2 | TT_bar / II_slash (null) | loose |
| QP, LAM4, B3, i, r | 2,2,1,1,1 | none | -- |

No drawn nomenclator sign of R4750 (papa_sign, tent_oo, C_oo) is closer to any low-count no. 7 sign than the entries above.
A licensed token (rule 4) needs T1 or T2 to PASS and the token's value to agree with any gloss over it; T3 alone licenses nothing.

Script: specs/cheap-tests/siena-concistoro-2308/run_test_r4750.py (seeded, `--check`), results_r4750.json.
