# A3V3-SAVT pre-registration (written 4 Oct 2026 06:37 UTC (committed 09a6eff4), before the gloss is transcribed and before any alignment is run)

Target: c380 (f.187r), 22 cipher lines, 932 segmented signs (SV-SORT `sorter/inputs/labels.tsv`, piles k000-k119).
Seed table: `sorter/tomokiyo_pile_match.tsv` (RUN1-SAV, by-eye proposals; piles with confidence none -> '?').
Gloss: the left-margin decipherment column of c380, transcribed by this worker from native crops into `savt/gloss_c380.txt`
(letters only for scoring: lower case, accents stripped, j->i, v->u, y kept, gutter-lost letters omitted; '[..]' never scored).

Decode D: tokens in reading order (line, pos). Pile value: a letter -> that letter; a word sign (de, ce, ent, est, avec, pour, que,
et, m-or-et) -> its first listed value spelled out; 'double' -> repeat previous letter; '?'/none -> wildcard '?'.
For a 'x?'-style value the '?' suffix is dropped (value used as proposed). u/v and i/j merged as in G.

Statistic S: semi-global alignment of D against G (end gaps in G free; D must be consumed), match +2, mismatch -1, gap -2,
wildcard vs any letter 0. S = matched letters / mapped (non-wildcard) letters of D.

Nulls (each 200 draws, seed 1..200):
 N1 shuffled-table: permute the letter values among the mapped piles (keeps the value multiset, changes which pile reads what).
 N2 pile-label shuffle: permute the pile labels across the 932 tokens of c380 (keeps the multiset, destroys order).
Both change D letter-by-letter, so both can move S (rule 3 orthogonal-control check: S depends on letter identity and order).
Positive control P (power at this N): D_P = G's first len(D) letters with the target's own wildcard rate placed at random and
30% of the remaining letters replaced by random letters drawn from G's frequency; must pass the gate, else the test is a non-test.

Gate (seed table): PASS iff S_target > max(N1) and S_target > max(N2) (empirical p < 1/200 each). P must also pass.
Table recovery (only if the gate passes): one hard-EM round per iteration (max 10): align, set each pile's value to the
plurality gloss letter among its aligned positions (min 3 aligned occurrences, else keep seed), realign.
Held-out: recover from tokens of lines 1-11 only; score S on lines 12-22 against G with the recovered vs the seed table, and
vs N1 on lines 12-22. Grades: C where a pile's value is the plurality of >=5 aligned gloss letters with >=60% agreement and
the held-out check passed; else M. Nothing H (no key sheet); no grade above the reading's own.
Stop point: first test = one line of c370 decoded with the proposed table, shown as is; no full decode of c370-c375.
