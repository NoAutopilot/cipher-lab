# PREREG MQS-STRUCK (account 4, 9 Oct 2026, written 09:40 UTC by date -u, before any control ran)

Job: research/MARY-STUART-TALK-2026-10-09.tsv row M44 (the encipherer's own corrections on the page: deletion symbol,
crossing out, overwriting; Lasry, Biermann and Tomokiyo 2023, Cryptologia 47:2). Tool: tools/decode_key.py, token
states `struck` and `over=OLD>NEW` (a tsv `state` column, or inline `X{struck}` / `{over=OLD>NEW}` in any format);
decode.json `corrections`: `final` (default: struck skipped, overwritten read as NEW) or `original` (struck read,
overwritten read as OLD -- the evidence view for cross-cipher contamination, M26).

Scope of this job: decode_key.py only. Sorter labels (sign_sorter_apply.py) and sheet callouts (decipher_sheet.py)
are not touched here (cap USD 2); named as follow-ups.

## Control K1 (known answer, same design as the intended use)
Synthetic homophonic-free substitution of a 600-letter fr18 passage (tools/data fr18 if present, else the fixed
French paragraph in the test), key = random permutation, seed 0..9. Plant per seed 12 struck signs (a random wrong
cipher sign inserted and marked struck) and 12 overwrites (a true sign replaced by OLD = random wrong sign, NEW =
true sign, marked over=OLD>NEW). Statistic: letter accuracy of the decode against the plaintext, letter by letter
after alignment by index of non-struck signs.
- Expected under `final`: 1.000 on every seed. **Gate: 1.000 on 10/10 seeds.**
- Null N1: the same file read with `corrections: original` (struck read, OLD read). Expected: below 1.000 on every
  seed (24 wrong or inserted letters in ~624). Gate: < 0.99 on 10/10 seeds.
- Why N1 can differ from K1 on this statistic: the manipulation (whether marked tokens are skipped/replaced) changes
  which letters enter the decode, which is exactly what accuracy counts; it is not orthogonal (rule 3).
- Ceiling: K1 is a plumbing control and is expected at ceiling; it licenses `controlled-only` (plumbing), never a
  claim that the option finds corrections on a page. Finding them is the transcriber's job (image).

## Must-not (Usage 8a)
M1: with no state column and no inline marker, every decode_configs reading regenerates byte for byte (existing test).
M2: a token whose text merely contains `>` or `{` without the exact marker forms is an ordinary sign.

Outcome is written below after the run, both numbers per seed.

## Outcome (run 9 Oct 2026, 09:41 UTC by date -u; `python3 tools/tests/test_decode_key_struck.py --controls`)
| seed | K1 final | N1 original |
|---|---|---|
| 0 | 1.000 | 0.195 |
| 1 | 1.000 | 0.119 |
| 2 | 1.000 | 0.657 |
| 3 | 1.000 | 0.114 |
| 4 | 1.000 | 0.218 |
| 5 | 1.000 | 0.090 |
| 6 | 1.000 | 0.267 |
| 7 | 1.000 | 0.186 |
| 8 | 1.000 | 0.137 |
| 9 | 1.000 | 0.078 |
K1 1.000 on 10/10 (gate 10/10, PASS); N1 < 0.99 on 10/10 (gate 10/10, PASS). N1 is far below 0.99 because a read struck
sign shifts every later position in the index-aligned accuracy; this is the prereg's statistic, stated so the size of the
gap is not read as power. Shelf: controlled-only (plumbing). Must-not M1: tools/tests/test_decode_key.py shows the same 3
failures before and after the edit (antt-linhares-chave reading.txt; rah-canada-1869 reading.txt, reading_tokens.tsv),
pre-existing and not this job's; every decode_configs reading without a marker is otherwise unchanged. M2 PASS.
Not built (cap): sign_sorter_apply.py struck/over labels, decipher_sheet.py callouts -- follow-up MQS-STRUCK-2.
