# PREREG R8-ROUS3 -- count-vector gate over the four slip-backed pairs (6 Oct 2026, account 2, LANE-RUN8-account-2)

Written and pushed before `align/r8rous3_countgate.py` is run on anything. Disk only, no network.

## Units (the four slip-backed pairs)
p1 ciphertext_f213.txt / slip_f214r.txt; p2 ciphertext_f216v.txt / slip_f217r.txt; p3 ciphertext_f249.txt / slip_f250.txt;
p4 ciphertext_f266r.txt / slip_f265r.txt. Cipher side: every group on lines starting `L`, first reading of any `a|b`. Slip side:
non-`#` lines (the expanded alignment text already committed), lowercased, accents stripped, split on any non-letter. One fixed
merge from a C value already in key.tsv: the token pair "la reine" counts as one token `la_reine` (31 = la reine, C), since that
"la" is not enciphered by a separate group. No other normalisation.

## Statistic
For a candidate (code c, word w): v_c = (count of c in p1..p4), u_w = (count of w in slips p1..p4). MATCH = (v_c == u_w) elementwise
and sum >= 3. UNIQUE = c is the only code on the four passages whose vector equals u_w.

## Controls (both can change the match, since both redistribute tokens across pairs)
(s) slip shuffle: pool the four slips' tokens and redeal them at random to the four pairs keeping each slip's token count; recompute u_w.
(g) group shuffle: pool the four passages' groups and redeal them keeping each passage's group count; recompute v_c.
2000 draws each, seed 8. p_s, p_g = fraction of draws in which v_c == u_w still holds.

## Known-answer control
Every key.tsv value at grade C that is a whole word or the merged `la_reine` (de 22, plus 279, au 581, et 501, la_reine 31, hongrie 628,
quils 172, interets 379, se 208, e 781 -- the script uses those whose word occurs >= 3 times across the four slips). The same MATCH/p
rule is applied to each. Licensing condition: at least one known-answer value is RECOVERED (MATCH, UNIQUE, p_s <= 0.05, p_g <= 0.05).
If no known-answer value is eligible or none is recovered, the gate is NON-INFORMATIVE for every candidate (method shows no power on a
true value at this N), whatever the candidates score; logged as such, no key entry.

## Primary candidates and gate
605 = republique, 739 = venise, 52 = la (named in the brief; 605's vector was seen post hoc by R8-ROUS2, which is why both shuffle
controls, not the uniqueness alone, decide). PASS per candidate = MATCH and UNIQUE and p_s <= 0.05 and p_g <= 0.05, and the known-answer
licensing condition met. Otherwise FAIL (no match) or NON-INFORMATIVE (match but a p > 0.05, or licence not met).
Per-pair contributions reported for each (rule 3 per-unit paragraph): count per pair on each side; a pair with 0/0 is reported as
non-discriminating for that candidate.

## Consequence
PASS: the value enters key.tsv at grade C (period slip as known plaintext, count-level, control-backed; note "count-vector gate
R8-ROUS3, pending VERIFY"), decode_key --check after regeneration, ROOM flag for a verifier if reading.txt changes. FAIL / NON-INFORMATIVE:
no key entry; logged in NOTES.md.

## Secondary (exploratory, no key entry)
Every (code, word) with MATCH, UNIQUE, sum >= 3, and both p <= 0.05 / (number of pairs scanned) is listed as an M lead only.
