# PREREG R14-SURDP (6 Oct 2026, ~15:45 UTC by date -u; committed and pushed BEFORE dp_align.py is written or run)
Question: on NA 1.05.03 inv. 373 scan 0746, does each blind cipher line, aligned sign-to-letter to the gloss line above it, agree
with the pooled 0693+0702+0730 sign table more than the same alignment of a gloss line taken from another pair?
R14-SUR746's word-pair score was a non-test (readers marked no word gaps, 2 words aligned); this replaces word pairing by a
segmentation-free per-pair DP. Inputs unchanged: ../inv373_0746_r14/passA_sonnet_blind.tsv (cipher rows) and gloss_reconciled.tsv.
No transcription change, no vision pass, no key edit.
Why not tools/interlinear_align.py: its `align` and `stream` modes build the value->meaning table by hard-EM from the letter itself
(group-to-chunk). Here the table is fixed and external (pooled from three other scans) and the statistic is agreement with it, so a
self-built table would be circular and would also fit any control. A ~60-line Needleman-Wunsch script (dp_align.py) is used.
Tokens. Cipher: the R14-SUR746 score.py preprocessing ('\&' = '&'; bracket codes kept whole; ALIAS map), then every sign in order,
dropping , ; : . - ' " | / % and the plain numbered-point "2o" at the start of L01 (a plain numeral per gloss_reconciled.tsv).
Gloss: lower case, letters only, 'ij' one unit (as signcount.tsv). Equivalences j=i, y=i, ij=i, u=v (score.py EQ).
Table T: code -> set of letters_seen, pooled from passes/inv373_0693_r10, inv373_0702_r13, inv373_0730_r13 sign_table.tsv (as
score.py S2); [y-fam] -> {m, n}. A cipher sign is "keyed" if it is in T.
DP: global alignment of the sign string (length Lc) to the letter string (length Lg); match = +1 if the sign is keyed and the
letter is in T[sign], else 0 (mismatch, unkeyed); gap (either side) -0.5; cells restricted to a band |j - i*Lg/Lc| <= 6.
Ties broken by diagonal first, then gap in gloss, then gap in cipher (fixed).
Statistic A: over all pairs, (keyed signs aligned to a letter in their T set) / (keyed signs aligned to any letter).
Control C1 (gate): gloss LINES shuffled between the 0746 pairs (a random derangement each time, 1,000 draws, seed 746), every
pair re-aligned by the same DP and banding; A recomputed. The DP maximises agreement for real and control alike, so C1 carries the
same optimisation inflation and can vary.
C2 (descriptive): each pair's own gloss letters permuted within the line (same length and letters), 1,000 draws, seed 7460.
Instrument check (positive control, must pass for the 0746 result to count): the same script on scan 0702 (42 pairs,
../inv373_0702_r13/ passA + gloss_reconciled; already SAME SYSTEM by word pairing) with T pooled from 0693+0730 ONLY (0702's own
table excluded), its own C1 at seed 702. If 0702 fails the gate below, the 0746 outcome is logged as a non-test of this instrument.
Gate: SAME SYSTEM (DP) if A >= 0.50 AND A > C1 p99. Otherwise "not shown". Both numbers reported, plus the per-pair A list.
Outputs (descriptive, no gate): per-code aligned-letter counts -> dp_sign_table.tsv; codes whose top aligned letter (>= 3 times)
is outside T -> dp_candidates.tsv for a verifier. Not applied to any key; conflicts.tsv not touched.
