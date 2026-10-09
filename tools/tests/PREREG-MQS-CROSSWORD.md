# PREREG-MQS-CROSSWORD: known-answer controls for `tools/decode_key.py --try / --avalanche`

Written 9 Oct 2026 (clock read 03:08 UTC by date -u) by MQS-CROSSWORD (LANE MQS, account 4), before any control below
was run through the shared tool. Brief: `.claude/briefs/runs/2026-10-09-acct3-mqs-crossword.md`. Every control run
writes its log to the worker's scratchpad or `tools/tests/`, never into a target folder. No target file changes.

## What the options compute (unchanged from the scripts they are promoted from)

Score of a window = infer_unkeyed's: per unbroken segment log2 P + C x length under the character model (C = model
bits/char), +-8 tokens, word signs pay 3 bits, unvalued neighbours filled with the model's likeliest letter.
`--try CODE=VALUE` statistic = score(VALUE) - score(current value), or - score(runner-up) for a code with no value,
summed over every occurrence. Null 1 = the same statistic for a pseudo-code at n shuffled positions whose current
value equals the code's own (100 draws). Null 2 = the code's own positions read as random values of VALUE's class.
`--avalanche` = infer_unkeyed.run (greedy, fix the largest margin first) under the acceptance rule value not NULL,
n >= 5, margin >= 10 bits.

**Why each null can fail differently from the known answer (rule 3, "control that cannot vary").** The statistic is a
sum of window scores that depend on each occurrence's neighbours. Null 1 changes *which* neighbours (positions), so a
value that fits only this code's contexts scores lower there; null 2 changes the *value* at the same positions, so a
value no better than a random same-class value cannot clear it. Neither manipulation is orthogonal to the statistic
(unlike a coverage figure under shuffled order, bCAS, or a run-length under shuffled values, AX-5799).

## K1 -- Gramont reproduction (a port check, not a power measure)

Data: `ciphers/fr2980-gramont` f.29r + f.30r-v, fr16, key.tsv only, the infer_unkeyed hidden-sign protocol (draw seeds
1000+d, d = 0..9, `matched_draw`), candidates = 23 letters + NULL + ET, COM, SS, LL.

Found before running the port (03:12 UTC): `infer_unkeyed.py control` on the **current** files no longer reproduces
its own committed `control_f30.tsv` (draw 0: counts and margins differ, e.g. rs 23 -> 22 occurrences), because
`ciphertext.txt`, `ciphertext_f30.tsv` and `key.tsv` changed after 24 Sept. So K1 has two parts:

- **K1a (the published number).** Port run on the files as committed in e8567d0a8 (24 Sept 2026, the commit that wrote
  control_f30.tsv), copied to a scratch folder. Expected 155/200 proposals right (+-5) and 50/53 accepted-right on
  draws 5-9 (+-2). Gate: both within tolerance.
- **K1b (identity on current data).** Port vs `infer_unkeyed.py control` on today's files, draws 0-9: every row
  (sign, count, proposed, second, margin to 0.1 bit) identical. Gate: 100% identical rows.

If K1a or K1b misses, the port changed something: find what before running K2/K3.

Quoted limitation (Gramont NOTES.md, 24 Sept 2026): "only 25 distinct keyed signs could fill the pool, so the draws
repeat signs, and the 103 accepted control proposals are not 103 independent trials." K1 therefore licenses no grade.

## K2 -- Blathwayt word values (`ciphers/huntington-blathwayt-madrid-1728`, French 1728, `--lm fr18`)

Stream: the glossed run `ciphertext.tsv` (1532 tokens) with `key.tsv` (388 C-grade gloss rows), in memory.
Hidden codes: every code whose key value is a word (folded length >= 2, no '|') occurring >= 3 times in the stream,
**counted per distinct code**, one at a time (leave one out; every other code keeps its value). Candidates: the true
value + 9 distractors drawn (seed 0) from the key's own distinct word values of the same class and length band
(folded length within 1, within 2 from 6 letters), plus nothing else. Classes: **title/name** = roy, reine, empereur,
princesse, france, cour, and any value starting with a capital (reported only, no gate; AX-NAMES); **word** = the rest.

- Gate (word class): true value ranks first for >= 70% of hidden codes, AND false-accept rate <= 10%, where false
  accept = the top candidate is wrong and its margin over the runner-up meets the acceptance rule (n >= 5, margin
  >= 10 bits), computed **only over hidden word codes with n >= 5** (the number of such codes is reported).
- Baseline beside it: unigram-only ranking (the candidate's word frequency in the fr18 corpus, ties by the key's
  order). If the baseline already ranks first for about 95% or more, K2 has no headroom and says so.
- Expected (before running): rank-first 70-90%; false accept 0-10%; n >= 5 codes about 30-40.

## K3 -- Danzay letters (`fr20140-danzay-1557`, fr16, `tools/tests/decode_configs/fr20140-danzay-1557.json`)

Hidden codes: every H-graded single-letter code with n >= 5 in the config's two streams, one at a time, counted per
distinct code. Candidates: the model's 23 letters + NULL. Gate: true letter ranks first for >= 70% of hidden codes.
Baseline beside it: unigram-only (the commonest corpus letter, E, ranks first for every code); if that baseline
reaches about 95%, K3 has no headroom. Expected: 75-95%.

## Shelf grades (fixed now)

Per value class: a class whose control meets its gate -> `--try` grade `fair` for that class (accepted values enter a
key as S only for that class and design, otherwise M); a class whose control misses -> `weak` with both numbers; the
option ships either way and nothing is run on a target from this job.

## Results

(appended after the runs, below this line, without editing anything above)
