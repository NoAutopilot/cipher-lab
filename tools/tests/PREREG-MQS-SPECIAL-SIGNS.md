# PREREG-MQS-SPECIAL-SIGNS (9 Oct 2026, LANE MQS-2, account 4)

Written and pushed before any control is scored (CLAUDE.md rule 3). Tool: `tools/decode_key.py`
(decode.json `repeat_values` / `delete_values`; `--special-scan`). Source of the idea: Lasry, Biermann and Tomokiyo 2023
(Cryptologia 47:2) p.111, p.115, Fig. 13 p.126, App. B Fig. B24 (repeat-previous, delete-previous, nulls);
research/MARY-STUART-TALK-2026-10-09.tsv row M19.

## Statistic

For a code c with n occurrences, each interpretation I in {every letter of the model, NULL, REPEAT (copy the previous
sign's value), DELETE (cancel the previous sign and itself)} is scored as the sum over occurrences of the fr16
character-model score of a +-8-token window with every occurrence of c read as I (the `--try` window score).
stat(op) = score(op) - max score over every other interpretation (letters and the other two ops). A code is flagged
as op when op is its best interpretation and:
- REPEAT, DELETE: stat(op) > p95 of the same stat over 50 shuffled-position draws (c's occurrences removed and
  re-inserted at random token slots of the same stream).
- NULL: stat(NULL) / n >= 2.0 bits per occurrence (no relocation null: an inserted token reads best as NULL wherever
  it is put, so a relocation null cannot vary on this statistic -- the rule-3 "control that cannot vary" shape; NULL
  is gated instead by D1 and D2 below, which can fail).

Why the REPEAT/DELETE null can differ from the known answer: the statistic depends on the neighbours of each
occurrence (repeat copies, delete cancels the neighbour); relocation changes the neighbours, so a sign that sits
after a doubled letter or a wrong letter scores differently from one at random slots.

## Controls (gate per control: flagged correctly in >= 8 of 10 seeds)

- K1 REPEAT, synthetic, same length and language: 10 spans of 638 letters (Danzay f.35's sign count) from
  tools/data/fr18 (held out from the fr16 model), letters as their own codes, the second letter of every doubled pair
  replaced by code ZREP (natural density, count reported). Pass: ZREP flagged REPEAT.
- K2 DELETE, Danzay config stream (tools/tests/decode_configs/fr20140-danzay-1557.json, the committed graded reading,
  real 1557 French): at k=6 random slots insert a random letter token then ZDEL. Pass: ZDEL flagged DELETE.
- K3 NULL, Danzay stream: k=6 ZNUL tokens inserted at random slots. Pass: ZNUL flagged NULL.
- D1 decoy, must NOT flag: Danzay stream, 6 tokens whose value is E renamed ZLET. Pass: ZLET flagged as any op in
  <= 1 of 10 seeds.
- D2 must NOT flag: unmodified Danzay stream, every H-graded single-letter code with n >= 3: share flagged as any op
  <= 10%.
- Reported, not gated: K2/K3 at k=3 (headroom: if k=6 reads 10/10, the k=3 figure shows where power falls);
  K4 Tomokiyo's nulls (key value null) hidden as unkeyed: how many flagged NULL.

## Outcome rule

All of K1, K2, K3, D1, D2 pass: shelf grade `controlled-only` for the scan (the op named) and the decode.json options.
Any miss: that op ships `weak` with both numbers, is not re-briefed, and nothing is run on a target from it. The
decode.json options are plumbing, tested offline (repeat copies the previous value and grade, delete nulls the previous
sign); no target's decode.json, key, reading, status or AUDIT.md is changed by this job.
