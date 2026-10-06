# PREREG R10-SUR693 (6 Oct 2026, written before compare.py was run)
Question: is the cipher of Texier's 29 Oct 1781 letter (NA 1.05.03 inv. 373 scans 0692-0693) the same sign system as the
map key (key_period_codes_nieuw.tsv, NIEUW Secreet Alphabet, inv. 86)?
Statistic: over every sign position in align_words.tsv rows with status 'aligned', the share of positions whose sign is keyed in
key_period_codes_nieuw.tsv at which the key's value equals the gloss letter (equivalence classes i=j=y=ij, u=v; a key value
'a|b' agrees if either matches).
Control (can vary on the statistic): the same pairs with the gloss letters permuted across all aligned positions (1,000
permutations, seed 693); the statistic recomputed each time.
Gate: SAME SYSTEM if the real share >= 0.60 AND exceeds the control's 99th percentile. Otherwise 'not shown'.
Per-sign table (agree/conflict counts per code) is descriptive only; no key.tsv or key_period_codes_nieuw.tsv edit in this job --
candidate values go to candidates_0693.tsv for a verifier.
Caveat registered in advance: rows flagged rv=1 used the gloss to choose between the look-alikes v and r; the statistic is also
reported with those rows dropped.
