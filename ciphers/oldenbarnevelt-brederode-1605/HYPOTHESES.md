# HYPOTHESES -- oldenbarnevelt-brederode-1605

## Gloss conflicts, inv. 6019 scans 555-556 (OBRED-556, 15 Oct 2026; rule 4: data conflicts, not settled by majority)
Witnesses: one letter, P. van Brederode to the States General, Oggersheim 14 Oct 1619 (NL-HaNA 1.01.02 inv. 6019 scans 555-557), one
period interlinear hand; both readings of each value in the same letter, same direction, same date. Graded M wherever used.
- 415: 'r' over 555 L12 pos 5 (span read by the glosses as "met vrede", margin "met vrede te") vs 's' (long s) over 556 L04 pos 3 (span
  "diversie"). Either a gloss slip, a misread digit (passes agree 415 on both), or a homophone list that is not one-to-one. Open.
- 337: 'o' over 555 L05 pos 6 ("favoriseren") vs 'p' over 556 L05 pos 7 ("geholpen"). Same three possibilities. Open.
- 100: 'd' over 555 L12 pos 7 (M, Sonnet check saw no gloss) vs 'e' over 556 L05 pos 2 (C). Open, weaker (one side M).

### Image re-look of the three conflicts (OBRED-TRY, 15 Oct 2026; PREREG obred187/PREREG-OBREDTRY.md)
Scans 555/556 re-fetched at 5000 px (sha1 identical to OBRED-556's), the four gloss lines read by this worker's eye and by one blind
Sonnet call (not told values or conflict). Rule: a side is corrected only if both reads differ from the OBRED-556 row. None was corrected.
- 415: eye r over 555 L12 p5 ("met vrede") and long s over 556 L04 p3 ("diversie"); blind r (low) / s (low). Digits 415 clear on both. Stands.
- 337: eye o over 555 L05 p6 and p over 556 L05 p7; blind o (high) / p (high). Digits clear (556: 7 touched by a blot). Stands.
- 100: eye d over 555 L12 p7 (the d sits between 100 and 129, assigned by the eight-letter span "met vrede") and e over 556 L05 p3;
  blind "?" (555, blotted) and "u/n with a tick" (556). The blind read supports neither side; stands, weakest of the three.
- Observation, not used to settle any conflict (PREREG step 1): all three sit at the edge of two letters' code ranges under statistic B
  (r ~390-415 / s ~433; o and p ~337; d ~73-100 / e ~97-133), consistent with an ordered homophone table whose boundaries the glossator
  or the table drew differently -- a hypothesis, untested.

## OBRED-BAND (15 Oct 2026): band-interval held-out check (PREREG obred187/PREREG-OBREDBAND.md, 8e9bcd573)
| hypothesis | control | control number | target number | verdict |
|---|---|---|---|---|
| 1619 letter codes lie in alphabetical bands (fit 555, predict 556) | shuffled-band null, 10,000 draws; synthetic power at 30/11 pairs | null p95 0.104 (mean 0.034); power 1.00 | S 0.171 (hit 8/11), p 0.0107 | PASS (M design statement); reverse 0.199 vs p95 0.141 |
Application to no. 92/187: interval reading only, grade M (`obred187/band/reading_92_187.tsv`); 72/180 one-letter, 37 name codes.

| Hypothesis (OBRED-SEG, 15 Oct 2026, PREREG obred187/PREREG-OBREDSEG.md) | Control | Control number | Target number | Verdict |
|---|---|---|---|---|
| no. 92/187 band intervals segment into nl16 Dutch words above chance | synthetic band text at the target's sub-run lengths (20 sims, held-out nl16 file, e=0.25) vs its own shuffled-band null; target vs shuffled-band (200) and order (200) nulls | control beats null 20/20, word precision 0.577, recall 0.590 (interval hit 0.92); ungated e=0.75 (hit 0.71): 18/20, precision 0.538 | I 320.2 vs shuffled-band p95 238.2 (mean 202.0), order p95 232.9 (mean 181.6), p 0.00 both | PASS (M); 20 words of >= 4 letters, all grade M (len>=5 precision 0.61 < 0.80, no S) |

| Hypothesis (OBRED-CTRY, 15 Oct 2026, PREREG obred187/PREREG-OBREDCTRY.md) | Control | Control number | Target number | Verdict |
|---|---|---|---|---|
| OBRED-SEG's word leads hold at every other occurrence of their codes under a char 4-gram context scorer | synthetic band text at the target's sub-run lengths, e=0.5 and 0.75, 20 sims each; gate: right-lead hold >= 0.60 and precision gain among holders >= 0.10 | e=0.5: right hold 0.965, wrong 0.782, precision 0.530 -> 0.582; e=0.75: right 0.961, wrong 0.782, precision 0.455 -> 0.506 -- BELOW GATE | 16/19 testable hold, h 0.842 vs shuffled-band p95 0.765 (p 0.01, 100 draws) | non-test at this N (control cannot separate right from wrong leads); all leads stay M; hondert/middel/allen break (ungated) |
