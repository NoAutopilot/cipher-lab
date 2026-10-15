# PREREG-OBRED549 (15 Oct 2026, 08:4x UTC by date -u; addendum to PREREG-OBRED556/552, written before scans 549-551 are fetched or any number computed)

Job: NL-HaNA 1.01.02 inv. 6019 scans 549-551 (the opening of the Heidelberg 8 Oct 1619 letter whose end is on 552 and whose last paragraph
says the reformed cipher was sent "with the instructie ende sleutel", OBRED-552); walk back one scan at a time (<= 4 more) only if 549 is
still inside the 8 Oct letter. Look by eye for a key sheet / instruction (numeral tables, alphabet, name list).

1. Placement by eye first: per scan, hand, dateline/address/signature, whether it belongs to the 8 Oct letter, and whether it carries a
   numeral table, alphabet, name list or instruction. No key leaf -> record what the scans are and stop; nothing is scored.
2. If a key leaf is found: crops by `tools/iiif_lines.py --image ... --debug` (overlay checked), two blind Sonnet passes on the crops (not
   told any gloss, no. 92 or ciphertext_556.tsv), reconciled by this worker -> `key_6019.tsv` (code, value, grade H where both passes agree
   high and the reconciler confirms, M otherwise).
3. Known-answer test (only if step 2 runs): statistic K = number of the 45 C-graded glosses in ciphertext_556.tsv (code -> letter/name)
   whose code appears in key_6019.tsv with an H or M value equal to the gloss (letters compared case-folded, u=v, i=j; names by head word).
   Coverage n = number of those 45 whose code is in key_6019.tsv at all. Control: 10,000 shuffles of the key's values over its codes
   (value multiset fixed), same K; p = share of shuffles with K_shuffle >= K. PASS: n >= 10 and K/n >= 0.70 and p < 0.01. Reported per
   key grade (H only, H+M) and per gloss leaf (555, 556). Coverage < 10 -> "non-test at this coverage". The shuffle can differ from the
   target on K (it changes which value sits on which code; K depends on that pairing), so it is not a non-test by construction.
   Note on prior knowledge: this worker has read OBRED-TRY's statistic B (glossed letters rise with code value, rho 0.96); a key whose bands
   are alphabetical would agree with the glosses for that reason too, which the shuffled-value control does not exclude -- a PASS is read
   as "key and glosses consistent", not as an independent proof of the key's identity beyond that.
4. No key.tsv edit, no reading of no. 92/187 (a later job).
Requests: service.archief.nl <= 10 (METS + 3 scans at 5000 px + <= 4 walk-back + <= 2 re-fetches); NA take/release ROOM lines; images not committed.
