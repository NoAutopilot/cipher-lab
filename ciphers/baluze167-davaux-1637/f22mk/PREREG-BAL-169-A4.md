# PREREG BAL-169 (account 4, LANE DEFAULT-A4-0645-15), 15 Oct 2026 08:4x UTC by date -u -- pushed before any fetch or score

Target: the two f.22r numerals still M after BAL-169 (account 1): 13: (key.tsv Mr, H) at L03 pos 13, and the 65 at L04 pos 0 (key.tsv 65' = ra;
mark not settled on f.22r). Material: glossed cipher of the same office on Baluze 169 f.36-38 (c76-81; cipher seen on c79 = f.37v; c79 runs
already used by BAL169-F22B for other signs) and f.208-209 (c420-423, Memoire to La Boderie, 9 Aug 1637).
Same PREREG family and same instrument as BAL-169 / BAL-F22R / BAL-C275G: f22mk/score_marks_r.py's rule with a fourth pairs file
(f22mk/glossed_pairs_169b.tsv), run as f22mk/score_marks_169b.py.

1. Fetch: openapi.bnf.fr IIIF v3 `full/2400,` of c79 and c420-423 (5 requests), plus at most 3 of c76-78/c80-81 only if c79's text shows the
   cipher continues there; <= 8 total, one at a time, >= 3.3 s, ROOM take/release. Scratchpad only.
2. Key-identity gate for f.208-209 (the c420 head note may say "du chiffre donne a M. le Marquis de S. Chaumont", another key): before any 13:/65
   pair from c420-423 is counted, place >= 8 acute/diaeresis numerals of key.tsv under their gloss on c420-423; if fewer than 6 of 8 (75%) give the
   key.tsv value, f.208-209 is another key and its pairs are excluded (reported, not scored).
3. Values fixed now: 13: = Mr (key.tsv); plain 65 (no separate acute at zoom) = ra (hypothesis: mark-free form of 65', as plain 16 = de held
   5/5 for BAL-169). Wrong-mark negatives: 13: vs 13' co / 13 sued; 65 vs any other 65 form in key.tsv.
4. Call rule unchanged: S if >= 3 glossed occurrences give the value and that is >= 3/4 of the sign's glossed occurrences, AND real matches over
   all targets beat every one of 200 within-run gloss shuffles; otherwise M. Under 3 occurrences: M, reported as a count.
5. Before anything enters exceptions/key: `tools/decode_key.py ciphers/baluze167-davaux-1637 --try` at every occurrence (the f.22r tokens) for any
   value that reaches S here, with --try's own power control (a known-wrong value on an H code must be rejected; if it is not, the --try is a
   non-test and nothing is entered). An S call whose --try is undecided/reject is reported and not entered (BAL-C275G precedent).
6. Reader: my eye at 2400 px with zooms of each target numeral, not blind (I know key.tsv); a mark I cannot settle is left out, not guessed.
Stop before a unit crossing 80% of cap 3 or box (09:33 UTC).
