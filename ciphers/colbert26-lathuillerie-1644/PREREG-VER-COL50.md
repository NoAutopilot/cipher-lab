# PREREG VER-COL50 (verifier, account 4, LANE DEFAULT-A4-2135-14, 14 Oct 2026, written 21:5x UTC by date -u, before the check is run)

Question (brief VER-COL50 job 1): is each of the 65 canvas 50 C tokens (COL26-C50) backed by known plaintext on its own leaf?
COL26-C50 kept C where A2-COL15's ordered greedy walk found the key_f23 value anywhere after the previous match in the row's gloss.
That walk is unbounded in position: the same walk on length-matched f.23 French windows scores 44.1 of 97 (A2-COL15 control mean), so
roughly two thirds of the 65 are expected by chance. The unit-level pass (65/97 vs max 59) licenses the key as shared on canvas 50
(rule 3 per-unit clause); it does not place any single token in its gloss.

Check (siblings/verify_c50.py, pushed with this file before it is run; demotion only, nothing is raised): a token keeps C iff, under
at least one of the two blind word pairings of canvas 50 already on disk (DA1-COL word_pairs_da1.tsv; DA1-COL2 word_pairs_col2.tsv;
both passed their c50 instrument check, 31/110 and 31/107 vs Control W p95 19/18), it lies in a paired gloss-word span and
word_da1.py's hit rule (value at the token's proportional slot +-1 within the word) holds. Else it goes to M ('word-grain-miss';
'no-word-pairing' if neither pass covers it). Reported, not gated: the 65 tokens' hits per reader against Control W (word texts
permuted over canvas 50's spans, 10000 draws, seed 20261014 + 2135); this control moves which word sits over each token, so it can
differ from the target (rule 3).

Rule 7 wiring: verify_c50.py writes siblings/verify_c50_lower.tsv; c50_reading_inputs.py adds those rows to exceptions_c50.tsv
(reason 'VER-COL50 ...'); decode_key.py --check regenerates reading_c50.txt.
