# Z13 "ARTHUR LA" keyboard mechanism: stress test

Status: closed-negative
(of the mechanism only, not of the cipher: the mechanism does not beat its matched control. Nothing here says anything
about who wrote Z13 or what it says.)

Worker z13, 24 Sept 2026 20:28-20:40 UTC, at the owner's request. Claim: `CLAIM.md` (a forum post quoted by the owner,
24 Sept 2026; poster not named). Transcription: `ciphertext.txt`. **Not fetched**: Wikipedia's API answered 429 twice,
and zodiackillerciphers.com has no Z13 page (404). The brief allowed three requests and all three were used, so the
worker wrote down the widely reproduced transcription from memory. It agrees with every letter the claim names. Per
rule 2, every number below depends on that transcription. The two non-letter symbols (positions 4 and 10) are not used
by the mechanism.
The brief counted Z13 as 9 letters, 3 eights and 1 other symbol. The transcription used here has 8 letters, 3 eights
and 2 other symbols, and the control copies that layout.

## What the mechanism is (mechanism.py, every choice a parameter)
Board: the QWERTY letter rows. Track: Q...P A...L Z...M. Run with the poster's settings, the code gives **ARTHURLA**
(`python3 mechanism.py --check`).

| pos | Z13 | operation the poster applies | out |
|---|---|---|---|
| 1 | A | copy it, **and** move up-right (W), pass 1, take next | A, R |
| 2 | E | pass 1, take next, with **no** move | T |
| 3 | N | emit nothing; used as the chain's seed | - |
| 5,7,9 | 8 8 8 | 8-count backwards (start counts as 1), bounce at Q, pass 1 in the current direction; the output seeds the next count | H, U, R |
| 6, 8 | K, M | emit nothing (K is called a "confirmation") | - |
| 11 | N | move up-right (J), pass 1, take next | L |
| 12 | A | copy it | A |
| 13 | M | emit nothing ("terminal") | - |

Rules used: **5 different per-letter operations** across the 8 letters (copy, copy-and-move, move, slide, drop), plus
3 chain rules. Free choices: **16** (7 global settings, the chain seed, and the operation for each of the 8 letters).
Only **3 of the 8 output letters (HUR)** come from the sequential chain. ART and LA come from a different operation
chosen for each letter. Four of the eight letters (N, K, M, M) produce nothing, and the first A produces two letters.

## Degrees of freedom (enumerate.py, enum.tsv, names_found.tsv, witnesses.tsv)
Family: 1,280 global settings (move UR/UL/DR/DL, pass 0-3, slide direction, count 6-10, start 1 or 0, count direction,
reflect or wrap), with each of the 8 letters free to take copy, move, slide, copy-and-move or drop. That makes
165,552,000 valid combinations, counted exactly by dynamic programming. On the unchanged Z13:
- **16,179 combinations (0.0098%)** give a "name7" (a given name of at least 4 letters followed by the start of a
  listed surname, 7 or more letters in all; ARTHUR+LA qualifies because LA begins LANE, LARSON and LAWSON). These come
  from 30 of the 1,280 global settings.
- The same family gives 13 given names on the unchanged Z13. Ten besides ARTHUR (a full rule set for ANGELA KEL, DELLA BEN, ELLA KENN, JANE BAN and EVAN ARM is in
  `witnesses.tsv`): **ANGELA KEL**, ANGELA NEL, DELLA BEN, DELLA BER, ELLA KENN, ELLA NEWM, JANE BAN, EVAN ARM,
  ALLAN EL, ABEL ARM (ALEX, KYLE, GLEN, FRED and FELIX also appear, shorter).
The name lists `names_given.txt` (580) and `names_surname.txt` (323) were written from memory, with no fetch. They are
smaller than the brief's 2,000 entries, and the repository has no name corpus. A larger list would only raise the hit
counts, in the target and the controls alike.

## Matched control (control.py, control.tsv; 1,000 random strings in Z13's layout, seed 13)
| test | random strings | real Z13 |
|---|---|---|
| (a) poster's exact rules, given name >= 6 letters | 0 / 1000 | yes |
| (b) poster's global settings, per-letter operation free, name6 | 1 / 1000 | yes |
| (b) same, name7 | 22 / 1000 | yes |
| (c) whole family, name7 | **968 / 1000** | yes |
| (d) whole family, given name >= 6 letters | **299 / 1000** | yes |

In (d), the commonest names from random strings were MARCUS 22, NELSON 16, DWIGHT 14, ANGELA 14, GERALD 13 and
EDWARD 10.

Reading: (a) is what you expect from a rule set that was fitted to one input. It turns that input into a name and
almost nothing else, and that says nothing about whether the fit means anything. The fair control is the choice the
poster actually had, (c) and (d). With the operations and settings the poster used (the same move, pass, count and
bounce options), random 13-symbol strings in Z13's layout produce a 7-letter name-plus-surname-start 97% of the time
and a full given name of 6 or more letters 30% of the time. Z13 producing ARTHUR plus LA is inside that range, not
above it.

## Where exactly the mechanism fails (plain answer to the poster)
It fails at the choice of a different operation for each letter, not in the chain. The chain (N -> K -> H,
H -> O -> U, U -> Q -> W -> R) really is sequential, but it gives only HUR. ART needs the first A to be copied and also
moved, and the E to slide without moving. LA needs the second N to move and the second A to be copied. K and both Ms
have to be ignored for different stated reasons, and the chain has to start from the N rather than from A or E. That
is 16 free choices for 13 symbols. Given those choices, random strings of the same shape give a 6-letter given name
30% of the time (MARCUS, NELSON, DWIGHT, ANGELA...), and the unchanged Z13 itself also gives ANGELA KEL and
DELLA BEN. The poster reported that changing the settings "destroys HUR". That is true, and it is true of any
particular output. What the test needs is how often the same freedom produces some name. The answer is often.

## Log
- 24 Sept 2026 20:30 UTC: en.wikipedia.org API 429 twice (one retry), stopped; zodiackillerciphers.com 1 request
  (404, no Z13 page). 3 requests in all, no other fetches.
- Solvers' search (rule 1) not run: the brief asked for a stress test of a mechanism, not a solve.
- Suggestion (not done): re-run control.py against a fetched transcription and a larger name list when a session has
  fetch budget.
