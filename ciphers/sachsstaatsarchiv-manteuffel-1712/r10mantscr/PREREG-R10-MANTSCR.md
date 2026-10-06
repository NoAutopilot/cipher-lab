# PREREG-R10-MANTSCR (6 Oct 2026, written 10:02 UTC by date -u (header first typed 10:08 by mistake, corrected before any run), LANE LANE-RUN10-account-4, account 4), before any statistic under the rule is computed

Question: a spelling-variant normalisation rule, general enough to apply to every gloss in the pool (not written for 867), applied to the
pooled single-code-gloss gate of PREREG-MANTP as extended to 9 leaves by the PREREG-MANT526 addendum (--add0526). Does 867 license at M,
and does any other code's licence change (sensitivity)?

Already seen before this file (honest list): the registered --add0526 output (pooled_mantp/pooled_0526.out), so the three "disagree" rows
are known: 160 "mant | manteuffel", 754 "le roy de pologne | s m", 864 "le roy de prusse | roy de prusse", 867 "le feld mareschal |
le feldmarechal". The rule below is fixed from period French orthography in general, not tuned on those rows; what it does to each is
reported whatever it is.

Rule SP (applied after MANT5, to every gloss, real and shuffled alike, before the statistic):
  SP1 accents folded (Unicode NFD, combining marks dropped).
  SP2 a leading article token le / la / les / l is dropped (first token only).
  SP3 spaces and hyphens removed (word division is not stable in the period hand: "feld mareschal" / "Feldmarechal").
  SP4 y -> i (period roy/roi, Moscovie/Moscovye).
  SP5 s before a consonant dropped (period preconsonantal s: mareschal/marechal, estre/etre, teste/tete).
  SP6 doubled letters collapsed to one.
Out of scope by design (not spelling): abbreviation by truncation (mant / manteuffel: MANT5's table is the only abbreviation rule), and a
different wording of the referent (s m = Sa Majeste vs le roy de pologne). Those stay "disagree".

Statistic, control, gate: unchanged from PREREG-MANTP: S = among codes with >= 2 single-code runs, the fraction whose normalised glosses
are identical; control = gloss strings shuffled across all single-code runs of the pool, 1000 draws, seed 7101 (the control can change
which glosses a recurring code receives, so it can vary on S); PASS iff N_rec >= 3 and S > p95 strictly. Per-leaf gates re-run under the
rule too (seed 7101 + leaf), clearing as before (0502, 0528 prior-cleared).
Licensing: PREREG-MANTP's rules, capped at M by the brief (R10-MANTSCR): a code that newly agrees under SP and whose attestations lie
only on uncleared leaves enters key.tsv at M; never overwrite a Krauske row; no grade is raised in key.tsv by this job. If the pooled gate
under SP does not PASS, nothing enters key.tsv.
Sensitivity (reported, not a gate): per code, licence under the registered MANT5 table vs under SP; any code that changes is listed.
Implementation: pooled_mantp/pooled_gate.py --add0526 --sp (outputs suffix _0526sp). Output kept beside the registered run, never in its place.

Clarification (10:05 UTC by date -u, before any scored run): a unit check of sp() on sample strings showed SP5 applied after SP3 turned
"s m" into "m" (an s before the next word's consonant). SP4 and SP5 apply within each word, before SP3 removes word division. No pool
statistic had been computed.
