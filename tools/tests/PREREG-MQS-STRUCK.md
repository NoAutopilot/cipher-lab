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
