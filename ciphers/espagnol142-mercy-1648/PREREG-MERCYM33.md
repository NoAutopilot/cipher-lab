# PREREG MERCY-M33 (crossword test of the 33 M ordinary letters, BnF Espagnol 144 f.22r-v), written 13:3x UTC 15 Oct 2026 by date -u, before any statistic

Worker MERCY-M33 (account 1, for LANE VIV-KEYSTONE account 4). Brief: `.claude/briefs/runs/2026-10-15-acct4-depth-steps.md` "## JOB MERCY-M33".
No key.tsv, reading, AUDIT.md or status.json edit. Instrument: `tools/decode_key.py --try` / `--avalanche` (MQS-CROSSWORD), run
in-process (`mercym33/m33.py`, which imports decode_key and calls its own `Crossword` and `try_value`, nothing re-implemented)
so the model loads once; `--lm es17c`; window 8; 100 draws per null; seed 0.

## The 33 positions (AUDIT.md "Depth re-rule (DV-MERCY, 8 Oct 2026)" item 4), grouped into hypotheses
--try works per code; an M position whose sign is uncertain is tested by relabelling it (in memory) to a fresh pseudo-code
with no value and asking whether its current value beats the runner-up among 23 letters + NULL (the tool's statistic for a
code with no value). Positions sharing sign and value are pooled into one pseudo-code (one hypothesis: "these uncertain
glyphs are sign X = value v"). Each group is tested alone, all other positions at their current values.

| group | positions | value | n | why M |
|---|---|---|---|---|
| K25 | r09:7, r17:4, r19:10 (+ r16:9, a name position, counts toward n, not toward the 33) | u | 4 | key-level M code 25 |
| K15 | v04:9, v04:19 | z | 2 | key-level M code 15 (v04:19 also transcription M) |
| K9 | r06:7 | q | 1 | key-level M code 9 |
| K14x | r16:3, r17:5, v01:15 (+ r06:14, r14:7, r16:6, name positions) | c | 6 | exceptions.tsv: glyph transcribed 19 is the open 14 |
| FRAC | v01:6 | c | 1 | [MARK:frac] |
| R1008 | r10:8 | or | 1 | exceptions.tsv re-cut 25 -> 2 5 |
| R1013 | r10:13 (+ r10:14, empty half) | l | 1 | exceptions.tsv re-cut 2 8 -> 28 |
| T2 | r17:11, r18:5, r20:6, r24:14 | o | 4 | transcription M, sign 2 |
| T6 | r18:6, r23:2, r24:4, r24:15 | s | 4 | transcription M, sign 6 |
| T4 | r17:21, r20:15, r22:2 | q | 3 | transcription M, sign 4 |
| T8 | r17:22, r20:16 | u | 2 | transcription M, sign 8 |
| T5 | r17:10, r24:5 | r | 2 | transcription M, sign 5 |
| T3 | r20:7, v07:15 | p | 2 | transcription M, sign 3 |
| T17 | r04:17, v07:16 | a | 2 | transcription M, sign 17 |
| T18 | r23:1 | e | 1 | transcription M, sign 18 |
33 ordinary positions in all (r10:14 counted, as DV-MERCY counted it).

## Registered accept rule
Primary (MQS-CROSSWORD default, unchanged): verdict `accept` from try_value with `--accept margin>=10,n>=5,null=no`
(statistic above both null p95s -- null 1 shuffled positions, null 2 value class = the other letters -- margin >= 10 bits,
n >= 5, no quarter of occurrences broken by > 3 bits). n = 1 is undecided by construction; n < 5 cannot be accepted
under the primary rule. Secondary (sensitivity, registered now): `margin>=10,n>=2,null=no`, licensing an accept only at an
n whose own control below passes its gate. Anything accepted enters nothing: it is written to NOTES.md/HYPOTHESES.md as M
pending a verifier (grading per MQS-CROSSWORD: S only for a single letter in a letter cipher of Danzay/Gramont design).
`--avalanche` is also run (all 15 groups hidden at once) and reported as proposals only.

## Value-class control (K3 shape, matched to this target, es17c, same window/nulls)
For every single-letter S code of the key with >= 7 occurrences at transcription confidence H, and for each k in
{2,3,4,5,6}: draw k such positions (seed = code x 10 + k), relabel them as a hidden pseudo-code, run try_value with (a) the
true key letter and (b) one wrong letter drawn from the other 22 (same seed). Power(k) = share of (a) accepted; false(k) =
share of (b) accepted; also "first" = true letter ranks first among 23 + NULL (K3's own statistic). Gate per k and rule:
power >= 0.70 and false <= 0.10. A group whose n's control fails the gate gets "non-test at n = k", not accept/reject.

## Run statistic (before / after)
Longest contiguous stretch of H/C/S cipher tokens in letters (len of value), counted within one cipher segment (a clear
word breaks a run; lines run on), from reading_tokens.tsv; every non-HCS cipher token (M, mark, U) breaks a run. Before =
committed grades (DV-MERCY: 53, r13-v09). After = the same with the accepted positions set to S. Reported against AD 84.0
(R 3.4) and 135.1 (es17c), the DV-MERCY figures, unchanged here (each accepted M also removes about one liberty bit; the
verifier recomputes AD). Also reported: does any accepted position join two runs.
