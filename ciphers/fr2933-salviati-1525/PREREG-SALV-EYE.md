# PREREG-SALV-EYE (14 Oct 2026, written 10:3x UTC by date -u, before either eye-check result was read or any score computed)

Worker SALV-EYE (Opus), LANE DEFAULT-A2-0911-14 (account 2), brief `.claude/briefs/runs/2026-10-14-ytbiz-default-0911-jobs.md` row
SALV-EYE. Disk only. Key source: `published` (George Lasry, via D. Bourdeau's cyphersolver dde5b0ea, CC BY 4.0).

1. Instrument (different from passes A/B/C, which matched atlas rows cut by code): in-context tiles of each type's own occurrences
   (`lkey/eye/build_eye.py` -> `types_g{1,2}.png`, up to 7 tiles per type, only tokens whose atlas box at the same page/line/pos has
   the same base code; f54r from its native line strips, other leaves from the numbered classify strips), against his sheet cut into
   three enlarged bands (`his_part{1,2,3}.png`). Two Sonnet subagent calls, one per type group (a different model from passes A/B/C),
   prompts `lkey/eye/prompt_g{1,2}.txt`; passes A/B/C, key_lasry.tsv, readings and scores withheld. Output `lkey/eye/eye_g{1,2}.tsv`.
2. Types (18 with occurrences): settled S^ Lx^ bh^ H^ ch^ a^dot S7^+ ]^o sq^ sq^o sq^~ L^ dl^ e^+; settled-to-none m^1; unsettled
   bh^dot #^ S4^. Z^o and ]^dot have no occurrence in lkey/ciphertext_lasry.tsv: nothing to check, reported as such.
3. Verdict per type: normalise the eye's cell as lkey/build_key.py's vset (strip '?', i1/i2 -> i, ... u/v -> u). eye-confirmed when
   the eye's value set equals the 2-of-3 value set exactly (for m^1, 'none'); otherwise eye-contested. Unsettled types: the eye's value
   is reported against A, B and C (agree with which), and no key row is added (a 4th vote is not a 2-of-3 rule).
4. Key edit: only a dated column `eye_20261014` in lkey/key_lasry.tsv (eye-confirmed / eye-contested / empty), written by
   lkey/build_key.py from eye_g*.tsv; values, grades and rows unchanged; `--check` and decode `--check` must pass.
5. Re-score only if at least one settled type with a value is eye-contested. Primary: the eye-contested settled rows dropped (unread),
   `lkey/score_lasry.py` unchanged (it16 4-gram mean log10/letter, 300 keys permuted within class, seed 1), gate as PREREG-SALV-MAP3 5:
   whole-letter 4-gram target > permuted p99. Reported beside SALV-MAP3's after numbers (-1.360 vs p99 -1.399, 0/300). Descriptive only:
   contested rows set to the eye's value where the eye named one cell at H or M. If nothing flips, no re-score (SALV-MAP3 numbers stand).
6. Then a fresh `--check` re-derivation of the reading under key_lasry (decode_key.py --config decode_lasry.json --check; build_key.py
   --check). No novelty classification; no token of our transcription re-read.
