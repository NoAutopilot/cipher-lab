# PREREG-MANT2 (RUN4-MANT2, 4 Oct 2026, written and pushed before any clear text of either leaf is read)

Question: where one witness (frame 0501, Loc. 694/08 ff.~400v-401; or f.409v, frame 0511) writes clear text and the
other writes code groups at the same place, the clear text is known plaintext (grade C source) for those codes.

Pairing rule (fixed now):
1. Read the clear French of both leaves only in the passages already shown to be the same text (0501 right page
   R_L01-R_L05 vs f.409v L10-L14, RUN3-MANT/RUN4-MANT) plus any further passage where >=3 consecutive clear words agree.
2. Anchors: clear words written identically (modulo spelling/abbreviation, normalised: lower case, accents and
   abbreviation dots dropped, Mons./Mr./Monsieur = one word) in both witnesses.
3. A PAIR is a slot bounded on both sides by an anchor (or by a code run matching the other witness's code run
   group-for-group), with code groups in witness A and only clear words in witness B. The pair's value is the whole
   clear span of B; the unit is the whole code run of A (run-level, as the existing multi-code class).
4. Per-code values are assigned only for a single-code run (one code <-> one clear span). A multi-code run against a
   clear span is logged as a chunk pair; per-code splits are not made from a single attestation.
5. Grades: a code whose pair value is attested once stays M (brief). A code enters key.tsv at C only if attested in
   >=2 independent pairs with the same value, or in 1 pair agreeing with an existing independent C/gloss value
   (period gloss, Krauske) -- the latter is reported as agreement, not as a new value. Every key.tsv row added carries
   the witness reference (frame, line).
6. Known-answer check (the control here, per class): codes already in key.tsv at C that fall inside any pair are
   scored agree/disagree against the pair; codes inside 0501's period-glossed runs are scored against the gloss.
   A disagreement on a C value stops any merge from that pair. Reported per class: single-code vs multi-code.
7. Nothing found is a valid result ("no clear-vs-cipher slot in the shared passage"), logged as such.
No statistic beyond agreement counts; no shuffle null, because a pair is read, not inferred (rule 3 non-test clause:
no control could vary on this axis -- the known-answer check in 6 is the check).
