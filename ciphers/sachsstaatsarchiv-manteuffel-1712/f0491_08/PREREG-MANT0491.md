# PREREG-MANT0491 (9 Oct 2026, 21:1x UTC by date -u; written after the crops were cut and BEFORE any transcription pass, decode or score; LANE FAMILY-A2l account 2)

Leaf: HStA Dresden 10026 Loc. 694/08 frame 0491 (fullsize 0491.jpg, 4339x3865, sha256 prefix b535bc66c5c1be49 = MANT-CEN5 fetch_log; film card
"Aufnahme Einheit 0492"), plus frame 0492 (4345x3860, 7bf8d0b2adc20a69 = inventory_stride4) because its left page is the end of the same letter.
One GET each, 9 Oct 2026 21:03 UTC. Key: key.tsv at origin/main as of this commit, unchanged.

## Premise (from the leaf at sight scale, before this file)
- 0491 LEFT page = the tail of the previous dispatch (numbered paragraphs 8 and 9, closing "je suis tout a Elle"); it is not the 14 Nov letter.
  Its code runs carry small interlinear notes (seen at sight scale, not read: over the line-1 run, over 155, over 187, over the line-7 run).
- 0491 RIGHT page = stamp 393, "Berl. ce 14 Nov 1712", paragraphs 1-3; no interlinear notes seen; continues on 0492 left page (codes 11 and a
  3-code run), which ends the letter ("Je suis tout a V.E."). 0492 right page blank.
- Tokens counted on the image: left about 15 (one ~7-code run, 155, one single code, 187, one ~5-code run); right about 19 (103.34.26.27 x3,
  36.31, 257 x2, two single codes); 0492 4. About 38 in all.

## Inputs
- Crops (committed, f0491_08/crops/, manifest.json): one strip per code line, cut with tools/iiif_lines.py --image ... --region ... --centres
  (commands in NOTES). Left strips include the interlinear note band.
- Two blind Sonnet passes (A, B; B in reverse order), each split into two calls (left page; right page + 0492), reading codes AND any small
  interlinear notes (V-BRANDT: notes read blind, two passes, never settled by the worker). Passes see no key value.
- Worker reconciliation of code digits from the native image where the passes disagree -> f0491_08/ciphertext.tsv, before any decode or
  score. Disclosure: this worker has seen key.tsv and the leaf at sight scale; digits settled from the image only; doubtful ones low.

## Statistics and gates (fixed now)
- Gate (b) = f0490_08/judge_gate_L.py copied to f0491_08/judge_gate.py unchanged except paths and seed 491 (fr18 4-gram; key letter values
  permuted over codes, 1000 keys; power from the 694/09 0085 r9+r10 and 0136 windows; TEST only if power >= 0.80, else too-short). Stream =
  every code token of 0491 left + right + 0492 that is in key.tsv as a letter value and NOT under an interlinear note (note spans by position,
  union of the two passes); name-abbreviation rule as in that script.
- Shuffled-target control (CLAUDE.md rule 3, ARM-C1): the same stream's token ORDER shuffled 1000 times (seed 4910), each decoded under the
  REAL key and scored by the same model. Reported: share of shuffled-target decodes scoring above the permuted-key p95. If that share > 0.05,
  the judge is void as a gate at this N: the verdict is "judge cannot decide" whatever the real score, and grading is by key alone.
- Gate (b) PASS only if: power >= 0.80 AND real > permuted p95 AND shuffled-target share <= 0.05. Else too-short / FAIL / judge cannot decide.
- Known answer (reported only, NOT a gate: N < 5 notes): for each interlinear note, each blind pass's note text beside the key decode of the
  code run under it, with a letter-position match count. No statistic, no threshold.
- Grades (rule 4): H none (key.tsv carries no H row). A letter token in the gate stream = S only under a gate (b) PASS. Otherwise every keyed
  token M; codes not in key.tsv U. Whole-name codes (155, 187, 257) M (key value C from Krauske's table, but no gate on this leaf).
- Check 5 after the decode: decoded phrases with their clear context through tools/print_check.py before any "not located" sentence.
