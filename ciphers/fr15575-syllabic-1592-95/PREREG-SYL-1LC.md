# PREREG-SYL-1LC (13 Oct 2026, 20:3x UTC by date -u; account-2 worker for LANE DEFAULT-A2-2013)

Written and pushed before any `--try` score of this job is computed.

## Question
SYL54-TRY's control was syllable-class (23 de, 24 da, 73 que) and failed 0/3, so its target verdicts (T1 ^=s accept, the rest
reject) were non-tests. Does `decode_key.py --try` recover a *single-letter* value on f.228 L01-L08 at these settings? If yes, re-score
the two legend pairs (caret ^ = s vs l; dotted n = en vs l) in the same environment.

## Environment E (both control and target; built by `syl1lc_try.sh`, scratch only)
f228 ciphertext.tsv + ciphertext_b2.tsv unchanged; key = f228/key_syllabary.tsv (95 syllable rows) plus the 15 H-graded no.54 header
letter signs of key_no54.tsv (4 a, f e, s e, 3 g, p i, 6 i, x n, 7 o, 2 o, y r, : r, A s, 8 u, 9 y, 1 y), excluding `n` (a target).
M-graded header rows (ʒ, 5, `.`, hook) stay unkeyed. `^`, `n`, `+` unkeyed. This differs from SYL54-TRY (syllabary only): the
header letters fill some neighbours of the target tokens, and both control and target use the same E.

## Instrument
`python3 tools/decode_key.py <E> --try X=V --lm tools/data/es1600 --window 8 --nulls 100` (as SYL54-TRY), statistic, nulls and
verdict exactly as the tool's --help. Control log to scratch; target log to crossword_log.tsv.

## Matched control (run first; gate)
k = 3 H single-letter signs of f.228 L01-L08, each masked by dropping it from E's key (one call per sign, the other two in place),
then `--try` with its true value and one wrong single letter:
- `:` true r (n 13 tokens: 12 H, 1 M) -- wrong l
- `y` true r (n 6) -- wrong s
- `9` true y (n 4) -- wrong e
Control PASSES only if (a) at least 2 of 3 true values are accepted AND (b) at least 2 of 3 wrong values are not accepted.
Power check: `:` is the n-matched sign (13 = `^`'s 13, near `n`'s 15) and its own true/wrong pair (r/l) mirrors the caret's s/l
choice; (a) must include `:`=r accepted, otherwise the control is below gate at the targets' n (the y and 9 rows sit at lower n).
The control can fail differently from the targets: its statistic depends on each occurrence's neighbours and value, as the targets'
does (rule 3). If the control fails, stop: every target is a non-test at this N, targets not scored.

## Target calls (only if the control passes)
T1 ^=s; T2 ^=l; T3 n=en; T4 n=l; T5 n=e (the key's header value, reported beside T3/T4). One call each, nothing else in place.
Assumption (as SYL54-TRY): a mark transcribed as its own token stands where its added letter is read.

## Gate for a pair
Caret: settled to X in {s, l} only if the control passes, X is accepted and the other is not. Dotted n: settled to l only if the control
passes, l is accepted and en is not; en is a two-letter value, a class whose control failed (SYL54-TRY 0/3), so an en accept is a lead
(M) and never settles the pair. Otherwise "not settled".

## What follows
No key.tsv / key_no54*.tsv / decode.json / reading edit. An accepted single-letter value under a passed control is logged in
HYPOTHESES.md as S-candidate (control passed for the single-letter class) for a later key job; otherwise M lead. --try never writes a key.
