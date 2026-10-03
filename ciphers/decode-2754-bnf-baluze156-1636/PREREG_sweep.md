# Pre-registration: fr.4140 Sabran 1636 sign-inventory sweep (FT4c, account-4, 3 Oct 2026, 01:3x UTC)

Committed before any fr.4140 letter's cipher signs were read. Script: `sweep_inventory.py`.

- Statistic: R_L = share of DC8's 28 recurring sign classes (n >= 2 in ciphertext_draft.tsv) that occur in letter
  L's cipher runs (classes named as in DC8's transcription); D_L = count of DC8's numerals {9, 7, 12, 10, 94} in L.
- Gate: candidate iff R_L >= 0.921 (max control 0.821 + 0.10) AND D_L >= 2.
- Controls (all known non-keys for f.157r, so a control number can differ from a letter's):
  f.146r blind two-pass inventory R 0.643 D 0; Servien 1632 R 0.714 D 3; Lasry fr.4134 1631 R 0.821 D 3.
- Calibration limit stated before scoring: known non-keys of the same family already reach 0.64-0.82, so the
  statistic sits near its ceiling. A pass licenses only a pair-level (cipher+decipherment) test of that table, never
  "the key"; a miss is not a negative for the table (values, not shapes, separate Sabran's tables -- f.146r shares
  18 of 28 classes and reads at the shuffle median).
- Reading: low resolution (about 1000-1800 px per page), so every inventory is grade M. At most 3 further vision calls.
