# PREREG-MANTR8 (MANT-R8, 8 Oct 2026, written 22:51 UTC by date -u, before any blind pass was run or read and before any score)

Target: mant0609/rank_unglossed.tsv ranks 8-14 -- Loc. 694/08 URL files 0375 (ff.299v-300, Sept 1712), 0214 (f.165, Jul 1712),
0436 (ff.343v-344, Oct 1712), 0241 (f.185?, Aug 1712), 0435 (f.343, 23 Oct 1712), 0065 (f.47, Berlin 12 Mar 1712), and Loc. 694/09
0070 (f.49, minute "Ad No 15/16", 1713). Unglossed; code runs and single codes written in the clear text. Key: ../key.tsv (Krauske
1893 rows + licensed rows), unchanged by this job.

Statistic, control and PASS rule: identical to PREREG-MANT08.md / PREREG-MANT15.md, using the same scorer as
f0390_08/shuffle_gate_0390.py: mean log10 4-gram probability per letter, corpus fr18, of the letter string from every reconciled code
token key.tsv maps to a 1-3 letter value (first alternative of a|b), name/word and unkeyed codes dropped, runs in page order;
1000 shuffled keys (letter values permuted among letter-valued codes); PASS if <= 10/1000 shuffles score at or above the real string.
Power control: 694/09 0085 runs 9+10 (seed 15), as before. Scored POOLED over the seven frames (seed 375) and per frame (seed = frame
number; 0070 seed 70 tagged 09) -- per-frame results at < 20 letters are reported, not gated (too short).
judge_plaintext fr18 is run on the pooled string only if it has >= 60 letters (rule 7 paste; at this length and register a FAIL near
the gate is "judge cannot decide", as MANT-08 recorded).
Expected size: the inventory lists ~90 tokens over the seven frames, many of them single nomenclator codes (11, 55, 155, 160, 177);
the letter-valued string may be under 60 letters, in which case the pooled shuffle gate is the only gate.
Known-answer check: none available (no gloss on any of the seven frames at sheet scale).
Grades: decoded tokens at most the key row's grade (C/M); no H; identifications of names I.
