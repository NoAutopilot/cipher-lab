# PREREG TT-FREQ (LANE TOOLS-TOMO, account 4) -- written 8 Oct 2026 ~23:05 UTC (date -u), pushed BEFORE any control ran

Instrument: tools/freq.py `--split-at auto` (C1), `--contacts K --vowels` (C4), `--repeats N` with gaps (C5).
Control script: tools/tests/tt_freq_controls.py; output tools/tests/TT-FREQ-controls.tsv.

## Control cases (known answer)
- **Ormonde (Clanricarde to Ormonde, 17 March 1643/4)**, ciphertext and decipherment as printed by Tomokiyo,
  sources/cryptiana/web/ormonde.htm ("Cipher in Question", "Deciphered Text"). Long runs of digits split into
  two-digit groups (his own "Reduction of the Problem"); key built from his decipherment listing. True structure
  per the page: letters 41-88 (regular two-row table), nulls <= 40, word codes >= 90.
- **Lodewijk van Nassau 1574, siblings 4613/4615** (ciphers/lodewijk-van-nassau-1573-74/ciphertext_sib.tsv,
  key.tsv C-graded from the period decipherment): letters 1-120, nulls/codes from 121. Not a Tomokiyo case; the
  nearest repo case with a period-derived numeric key and a low letter band (said so on the shelf).

## Pass lines
C1 `--split-at auto`:
- Ormonde: the best single split N or the dense band's upper edge B within |error| <= 3 of 90 (first value above
  the letter band). Lodewijk: best single split N within |error| <= 5 of 121.
- Null (shuffled VALUE: each numeric token redrawn uniformly over the file's own [min,max], 20 seeds; this moves
  which values are dense, so the break can vanish or move -- it can fail differently from the target):
  "no break" (gain < 10) or |N - true edge| > 3 (Ormonde) / > 5 (Lodewijk) in >= 18 of 20 seeds.
- PASS = target within error AND null pass, per case.

C4 `--contacts 20 --vowels` (Ormonde only; Lodewijk at K=20 too, reported, same lines):
- Accuracy = share of the 20 most frequent letter tokens whose Sukhotin class (V/C) matches the key (vowels
  a e i o u y). PASS if accuracy >= 0.75 AND 78 ("o", Tomokiyo's contact-chart finding) is classed V AND
  target accuracy exceeds the shuffled-ORDER null mean (20 seeds) by >= 0.15. Shuffling order changes every
  adjacency, so the contact matrix and the classes can differ (unlike a coverage statistic).

C5 `--repeats 3` (Ormonde, letters tokens with nulls/codes kept):
- Statistic 1: number of distinct repeated n-grams of length >= 3. Null: shuffled order, 20 seeds; PASS if
  target > null 95th percentile.
- Statistic 2: share of maximal repeated n-grams (length >= 3) whose every occurrence decodes (with the key) to
  the same plaintext and lies inside or on word boundaries of a repeated plaintext word or word sequence.
  PASS if >= 0.6.
Shelf grade per option: `proven` if its control(s) pass; `weak` with "controlled-only: failed ..." if not.
