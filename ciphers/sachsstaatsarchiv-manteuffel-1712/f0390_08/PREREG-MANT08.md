# PREREG-MANT08 (MANT-08, 8 Oct 2026, written 20:13 UTC by date -u (pushed 738ab3939 at 20:14), before any blind pass was read or any score computed)

Target: Loc. 694/08 URL files 0390 (f.311v-312, letter of 10 Oct 1712), 0391 (f.312v-313, its P.S. "Berl. ce 13 Oct. 1712"),
0395 (f.316v, Oct 1712; 0396 left = same page), 0485 (f.384v-385, Nov 1712; 0486 left = same page; 0487 is footed "a la lettre de
Mant. du 12 Nov 1712"). Letter-range code runs (codes <= 120 in key.tsv) plus single nomenclator codes. Key: key.tsv (Krauske 1893
rows + licensed rows), unchanged by this job.

Statistic, control, PASS rule and power control: identical to PREREG-MANT15.md (f0015_09/): mean log10 4-gram probability per
letter, corpus fr18, of the letter string from every reconciled code token key.tsv maps to a 1-3 letter value (first alternative
of a|b), name/word and U codes dropped, runs in page order; 1000 shuffled keys (letter values permuted among letter-valued codes);
PASS if <= 10/1000 shuffles at or above the real score; power control 694/09 0085 runs 9+10. Scored POOLED over the four frames
(seed 8) and per frame (seeds 390, 391, 395, 485) -- per-frame results at < 20 letters are reported, not gated (too short).
judge_plaintext fr18 run only on the pooled string and only if it has >= 60 letters.

Known-answer check (0391): an interlinear "bon gre malgre" is written above the run before "227. de se" in the P.S. (seen at
sheet scale by the worker before any pass). Pre-registered test: the key's decode of that run is compared letter by letter with
"bongremalgre" by edit distance; recorded as agreement count / length, beside the same figure for 1000 shuffled keys (p99). If the
interlinear words are an insertion rather than a gloss, the check is reported as uninformative, not as a failure of the key.
Grades: decoded tokens at most the key row's grade (C/M); no H (no period key sheet for these leaves); identifications I.
