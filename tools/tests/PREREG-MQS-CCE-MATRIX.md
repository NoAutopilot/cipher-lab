# PREREG-MQS-CCE-MATRIX (9 Oct 2026, LANE MQS next, account 4)

Written and pushed before any control is scored (CLAUDE.md rule 3). Tool: `tools/decode_key.py --error-matrix SIBLING_KEY[,KEY2...]`
(new option beside --lookalike, reusing its one-position window gain). Source of the idea: Biermann, Tomokiyo and Lasry,
HistoCrypt 2024 (doi 10.58009/aere-perennius0087) pp.5-8; Lasry, Biermann and Tomokiyo 2023 (Cryptologia 47:2) App. B
pp.198-200, Figs B22-B23 (cross-cipher contamination: a clerk enciphering with one key writes some signs from another
key of the same office; the recurrent errors date the document by the contaminating key). research/MARY-STUART-TALK-
2026-10-09.tsv row M26. Earlier target-local attempts (nevers-birago-fr3251-1572/cce, cce2; matignon MAT-CCE) were
glyph-correspondence designs; this is a key-level instrument and is run on no target in this job.

## Statistic

For a sibling key S (TSV, code -> value, the same format as key.tsv): an *examined* position is a cipher token whose
code has a value in the document's own key and in S, the two values folded (lm_fold) being different. gain = window
score with that ONE position read as S's value minus with its own value (the --lookalike gain: fr16 model, +-8 tokens,
word values pay wpen). A position is flagged when gain >= T = 3.0 bits. Document statistic r = flagged / examined.
Per code, the matrix row: code, own value, sibling value, n examined, n flagged, mean gain; a code flagged >= 2 times
is marked recurrent.

Null: S's values permuted among S's codes whose S value differs from the own value (codes on which S agrees with the
own key stay fixed), 200 draws, seed fixed; r_null per draw; p = (1 + #{r_null >= r}) / 201. S is reported as
*contaminating* when r > p95 of r_null. With several sibling keys the report ranks them by p (the dating read).
Why the null can differ from the known answer on this statistic: the permuted key examines the same kind of positions
and keeps S's value multiset; only the letter each code is read as changes. A planted contamination token is put
right only by its true sibling value, so the permuted key's flag rate at planted spots falls toward the background
rate, while on a clean stream neither S nor its permutation supplies the right letter and the two rates should match.
(A shuffled-token-order null cannot be used: it does not change which tokens are planted.)

## Known answer (same design, length and language as the intended use)

Intended use: one French letter of a few hundred to ~1,000 tokens read with an H key, tested against one or more
sibling keys of the same office. Material: the Danzay stream (tools/tests/decode_configs/fr20140-danzay-1557.json,
committed graded reading, real 1557 French, 870 tokens in 2 jobs, 76 codes), fr16 model, in memory only.

Synthetic sibling key of the same office (per seed): start from the document's own key A over its codes; keep A's value
on a random 25% of its single-letter and null codes and on every word/multi-letter code; permute the values of the other
75% of single-letter and null codes among themselves. Planting (per seed, rate p): choose round(p x 870) distinct
positions whose own value is one letter L, uniformly; at each, replace the token with a code c' drawn uniformly from the
codes with S[c'] = L and A[c'] != L (skip the position and draw another if none); in the stream the token then reads
A[c'] (what a reader with key A sees). A second sibling C is built the same way from a different seed and is never
planted from.

Seeds 2000-2009 (10 per row), 200 null draws each.

- **K3** (p = 3%, ~26 planted): S reported contaminating in >= 8/10 seeds.
- **K2** (p = 2%, ~17 planted): S reported contaminating in >= 7/10 seeds.
- **D0** (p = 0, the unmodified stream, the same S per seed): S reported contaminating in <= 1/10 seeds.
- **DATE** (p = 3%): p(S) < p(C) in >= 8/10 seeds, and C reported contaminating in <= 1/10 seeds.
- **POS** (p = 3%): planted positions flagged / planted, pooled: >= 0.50 (reported with precision = planted flagged /
  all flagged; precision is reported, not gated).

Ceiling check: if K3 and K2 are 10/10, a p = 1% row is reported (not gated) to show where the power runs out.

## Outcome rule

All five gates met: shelf grade `controlled-only` for French letter ciphers of the Danzay design (fr16), sibling keys
on the same code set. Any miss: the option ships `weak` with both numbers, is not re-briefed, and nothing is run on a
target from it. Birago 1572 and Matignon stay closed to this design without new material (M26). No target's key,
reading, status or AUDIT.md changes in this job. A report: a flag is a candidate for an image check, never a key edit.

## Amendment 1 (08:43 UTC by date -u, pushed before any control row is scored)

Disclosure: the offline fixture (tools/tests/test_decode_key_cce.py, seed 1 sibling, 6% planted with seed 2, 52 tokens;
not a control seed) was run while writing the tests. Under the registered rule (rule A, `gain`) the true sibling
flagged 37/52 planted spots and 38/349 others (rate 0.187), but 20 permuted siblings gave 0.13-0.20: a permuted key's
arbitrary letter also "improves" a planted wrong letter (the --lookalike shuffled-pair lesson, PREREG-MQS-LOOKALIKE-SLIPS
N = 0.40). Rule A and its five gates stay exactly as registered above and are run and reported first; its gates decide
rule A's grade.

Rule B (`--cce-rule best`), registered now, same material, seeds, draws, gates K3/K2/D0/DATE/POS and outcome rule:
a position is flagged when gain >= 3.0 bits AND the sibling value scores at least as high as every other letter of
the model's alphabet (and the null value '') read at that one position (top-1, ties counted as top). Everything else
(examined positions, rate, permuted-sibling null, p95, p, dating by p) is unchanged. Why the null can differ more here:
a permuted key supplies the best letter at a planted spot only when its random value happens to be the true letter.
Rule B is the option's default; rule A stays selectable (`--cce-rule gain`). The shelf row reports both rules'
results; each rule's grade follows its own gates.

## Results (appended after the run)
