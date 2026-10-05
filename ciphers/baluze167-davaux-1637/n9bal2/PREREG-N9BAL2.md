# PREREG N9-BAL2 -- addendum to PREREG-N8BAL: fit this hand's signs on F2 (c511 run 2), hold out F1 (5 Oct 2026, written 05:5x UTC, pushed before any pass is read or scored)

Worker N9-BAL2 (account 2, for LANE-NEAR9), brief `.claude/briefs/runs/2026-10-05-ytbiz-near9-wave2.md` job N9-BAL2. PREREG-N8BAL stays as
registered; this file adds a second, separate test. Crops: c511 runs 1-5 cut this session (commands in NOTES); c510 crops of N8-BAL reused.

**Known answers.** Tomokiyo (louisxiii.htm, Baluze 168 f.246): F1 "c'est ce qu'on pouvoit desirer dudit Salvius pour ce regard";
F2 "de ne consentir aucune suspension d'armes quand on viendra a traiter si ce n'est que le". N9-BAL placed F2 on c511 (f.247v) run 2 by
clear context (the clear text after run 2 is "parti aie si grand avantage"). F1's place is not known: its candidate passages are the other
bare runs of this letter in the same hand: c510 (f.247r) run Q1+Q2, c511 runs 1, 3, 4, 5 (c509's 6-group name run is excluded: too short).

**Transcription.** Two blind Sonnet passes A and B, one call per leaf (f.247r+v is one leaf: one call per pass over all c510 and c511 cipher
crops), no fragment text, no key values. Convention: numerals as digits with a mark suffix (' acute, : diaeresis, = overbar, none plain);
every non-numeral sign as `s:` + the nearest Latin letter form (case kept where the form is capital-like, e.g. s:L, s:K); `?` unreadable.
One reconciliation by this worker (NOT blind to F2/F1): per position A's token or B's token or `?`, every choice logged. A and B are also
scored on their own as the blind figures. err_2reader = token disagreement rate between A and B after a token alignment (edit distance /
max length), measured on the cipher tokens of all runs.

**Fit (F2 only).** The run-2 token sequence and normalized F2 (lowercase, accents stripped, j->i, v->u, letters only) as one pair through the
shared tool: `python3 tools/interlinear_align.py align PAIRS OUT_ALIGN OUT_KEY --code-prefix @ --code-chunk 3 --seg-bonus 0 --len-prior 0.5`
(every token prefixed @; each takes 0-3 letters; no prior; no key.tsv value used). The fitted key = each token's top meaning. Grade C for
a token's fitted value only where the token occurs >= 2 times in run 2 with the same chunk; otherwise the value is a fit, used in the test
but graded M. Nothing enters key.tsv from this job unless the gate below PASSes.

**Statistic (hold-out).** Each candidate passage is decoded with the F2-fitted key (a token not in run 2 -> '#', never matches). F1 is fitted
into each decoded passage with `n8bal/score_f247.py`'s `fit()` (match +2, mismatch -1, gap -2, free passage ends); agreement = F1 letters equal
to a decoded letter / F1 letters in cipher columns; a passage giving < 10 compared F1 letters does not count. Test value T = the maximum
agreement over the candidate passages (look-elsewhere built in); the passage giving T is reported.
**Nulls** (seed 1, 1000 draws each, the same max-over-passages per draw): (1) shuffled fitted key -- fitted values permuted among run-2
tokens within class (s: signs vs numerals); (2) letter-order shuffle -- F1's letters permuted, scored against the real decode. Both can
differ from T: (1) changes the decoded letters, (2) changes the target's order, and T counts ordered letter matches.
**Gate (fixed now):** PASS iff T > null-1 p99 AND T > null-2 p99 AND >= 10 F1 letters compared, on the reconciled transcription; A and B
reported beside it against their own nulls. If only the reconciled transcription passes: "PASS conditional on a non-blind reconciliation".
**Positive control** (`n9bal2/planted_control.py`, run after this file is pushed, before the real score is read): plaintext F2 + F1 encoded with
a random key of this design (each letter 1-3 sign homophones, the 40 commonest bigrams of the two fragments as 2-letter numeral codes,
greedy encode), F2's ciphertext as run 2 and F1's planted in a filler passage of the reconciled c510 run's length among four filler passages
of the c511 runs' lengths, reader error injected at the measured err_2reader (random substitution from the token inventory), the same fit
and statistic, 20 seeds; reported: control T mean/min and how many of the 20 pass their own nulls (200 draws each). If fewer than 10 of 20
pass, the method has no power at this N and the target result is logged as a non-test, whatever it reads.
**If F1 is on none of the candidates** (no passage gives >= 10 compared letters), the job reports the F2 fit only and claims no test.
