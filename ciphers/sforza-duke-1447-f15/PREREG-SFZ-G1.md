# PREREG SFZ-G1 (14 Oct 2026, 22:1x UTC by date -u; account 4, LANE DEFAULT-A4-2135-14) -- pushed before any key is built or decode run

Question: does DECODE scat. 1597 no. 23 (R5323, "Filippo Maria Duca di Milano"), as read blind by SFZ-R5323B's two passes, decode the
Duke's glossed slips italien 1584 f.5 and f.8 toward their period glosses (f.7 for f.5, f.10 for f.8)? SFZ-R5323B passed the
identification gate at threshold (4 of 7 C pairs); its own gap text says a key that fails the glosses voids the identification.
f.15 is NOT read in this job, whatever the result.

## Key build (scripted, g1/build_key.py, written before it runs)
- Inputs: the eight committed reader TSVs `r5323b/pass{A,B}_G{1,2}_b{1,2}.tsv`, rows for sheet_03 only (R5323 per r5323b/sheet_map.tsv).
  These two passes already cover R5323's whole alphabet block (every letter column, both label groups); no further blind call is planned.
- Tokens: strict exact labels of the 40-label table (r5323b/labels_G1.md + labels_G2.md); 'A/B?', 'X:..', 'N2?' and any token with '?'
  or '/' are not cells.
- A cell (label, letter) is agreed when both pass A and pass B list it (pass columns = union of the G1 and G2 calls).
- Primary key `g1/key_r5323.tsv`: each label with exactly ONE agreed letter -> row, grade S (blind-read cell, two passes agree; the key's
  identification is cryptanalytic, SFZ-R5323B). A label with two or more agreed letters is left out (logged as conflict). Labels with no
  agreed cell are left out.
- Sensitivity key `g1/key_r5323_loose.tsv` (reported, NOT gated): primary rows plus each remaining label that appears in exactly one
  letter column across both passes combined, grade M.
- Control keys: the identical rule applied to each of the 11 other sheets (R5324 R5302 R5304 R5305 R5306 R5309 R5310 R5311 R5312 R5313
  R5315), from the same eight reader TSVs.

## Decode
`tools/decode_key.py ciphers/sforza-duke-1447-f15/g1` (g1/decode.json: two jobs, ciphertext `../../sforza-italien1584-1447/duke/
ciphertext_f5.tsv` and `ciphertext_f8.tsv` as committed, key g1/key_r5323.tsv), then `--check` exit 0. Unkeyed tokens read '?'.

## Statistic
Gloss text: clear_f7.txt (f.5) and clear_f10.txt (f.8) from ../sforza-italien1584-1447/duke/, '#' lines dropped, lowercase, letters only,
v->u, j->i, y->i (the reader alphabet has no v/j/y).
Per unit: decoded string = one symbol per cipher token, in order (unkeyed = '?', which never matches). A = number of matched letters in
the optimal global alignment of the decoded string against the gloss letters (match +1, mismatch 0, gap -0.5, either side).
Rate r(unit) = A / number of cipher tokens in the unit. Pooled R = (A5 + A8) / (n5 + n8). Coverage (keyed tokens / all) reported beside it.
Scorer `g1/score_g1.py`, written before any decode.

## Nulls
1. Value permutation: the key's value column shuffled among its own rows (labels fixed, same coverage), 1000 permutations,
   random.Random(1447); per-unit and pooled.
2. Other-key controls: the 11 control keys above, scored identically (their coverage is part of what they are).

## Gate (PASS needs all three)
(a) pooled R above the value-permutation null with p = (1 + #null >= R) / 1001 <= 0.01;
(b) pooled R > max pooled R of the 11 other-key controls;
(c) each unit separately: r(f5) and r(f8) each above that unit's own permutation-null p95.
PASS licenses a key test of R5323 on f.15 in a later job (not here). FAIL: logged as registered; the R5323 identification is not
supported by the glosses at this transcription (rule 3: the blind-reader key, not the gate, is what changes next; the owner's sort,
ASKS 165, remains the transcription route). The gate is not re-tuned after scoring; the loose key is a sensitivity line only.
