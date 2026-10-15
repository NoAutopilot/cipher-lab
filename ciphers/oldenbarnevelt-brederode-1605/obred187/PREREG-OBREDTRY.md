# PREREG-OBREDTRY (15 Oct 2026, 08:3x UTC by date -u; worker OBRED-TRY, account 2, for LANE DEFAULT-A2-0810-15)

Pushed in its own commit before any image fetch, any gate statistic and any --try run. Inputs as on origin/main at bcd83dedc:
`ciphertext_556.tsv` (OBRED-556: 81 groups, gloss columns), `ciphertext.txt` (no. 92 as printed), `ciphertext_187.tsv`.

Disclosure: before writing this file the worker read `ciphertext_556.tsv` and saw by eye that C-graded letter glosses seem to rise with
the code value (e-glosses near 97-133, n near 300-324, t near 457-468). Statistic B below was chosen after that look; it is therefore
also scored per leaf (555 alone, 556 alone) and the gate asks for both, and the result is reported as post-hoc-selected.

## Step 1. The three conflicts (rule 4: logged with witnesses, never settled by majority)
Codes 415 (r on 555 L12 p5 / s on 556 L04 p3), 337 (o on 555 L05 p6 / p on 556 L05 p7), 100 (d on 555 L12 p7, M / e on 556 L05 p3, C).
- Re-see the six gloss positions and the six digit groups on scans 555/556 at native size (service.archief.nl <= 4 requests; images in
  the scratchpad only). One eye read by this worker plus one blind Sonnet call on the six gloss crops (not told the values or the
  conflict; asked to write the letter above the underlined/centred group and the group's digits).
- A side is corrected only if BOTH reads of the image show a different gloss letter or different digits from OBRED-556's row at that
  position (a transcription correction, logged before/after in HYPOTHESES.md). Otherwise the conflict stands as logged and the code
  enters the --try table as two separate hypotheses (each value tried on its own), any outcome graded M, never accepted as one value.
- The band picture of statistic B is NOT used to choose between the two values (it would be settling by a pattern, not by the image).

## Step 2. Per-unit gate (rule 3, per-leaf merge): the 1619 letter's own pairing against a shuffle control
Pairs: every row of ciphertext_556.tsv with gloss_grade C and a single-letter gloss (letters folded i/j, u/v; long s = s). Names are
not in the statistic. Null: the same glosses permuted over the same positions, 10,000 draws, seed 6019.
- A (consistency, brief's form): over codes with two or more C letter glosses, the share of occurrence pairs that agree. Reported with its
  null p95 and p; if fewer than 3 such codes exist the statistic is "non-discriminating at this N" (bSZL65/67 shape), not a pass.
- B (order, post-hoc-selected): Spearman rho between code value and the gloss letter's alphabet index (a=1 ... z), one point per
  occurrence; p = share of null draws with rho >= real. Scored pooled, on 555 alone and on 556 alone.
- GATE: B pooled p <= 0.01 AND B on each leaf p <= 0.05. If the gate fails, no gloss value touches no. 92/187: step 3 is not run on them
  (logged "per-unit gate failed"), only the power control is reported.

## Step 3. decode_key.py --try on no. 92 and 187, with controls
Build (scratch, not the folder's key): `obred187/try/` with decode.json (jobs: no. 92 tokenised from ciphertext.txt, prose words as clear
`w:` tokens, digit groups as code tokens; 187 from ciphertext_187.tsv; 556 from ciphertext_556.tsv for the power control), model
`--lm nl16` (17th-c. Dutch corpus folder), window 8, nulls 100 (tool defaults otherwise).
- Table T = the C single-letter pairs of step 2 (conflict codes as two hypotheses). For each code of T occurring in no. 92 or 187: key =
  T minus that code (leave-one-out), `--try CODE=VALUE` on the 92+187 jobs only. Report per code: glossed value, n in 92, n in 187,
  statistic, null-1 p95, null-2 (value-class) p95, verdict.
- Value-class / decoy control (false-accept rate): the same runs with VALUE replaced by a decoy letter (seeded, seed 92, uniform over
  the other 22 letters). FA = decoys accepted / decoys decided.
- Power (matched design, same tool, same table density): the same leave-one-out --try on the 556 job alone for every T code with n >= 2
  there, true value: power = accepted / tried; and decoys on the same codes for FA there.
- Reading of the result: a glossed value is reported "accepted by --try" only when the tool's verdict is accept. Its tokens in 92/187 stay
  grade M in every case (the 1619 table is the same list only at grade M, OBRED-556), unless power >= 0.70 AND decoy FA <= 0.10 on the
  556 control, in which case an accepted single-letter value may be graded S in 92/187; a name value stays M. If power < 0.70 or n is
  too small for any decision, every verdict is logged "undecided / non-test at this N", not a negative for the gloss.
- No key.tsv is written in the folder; nothing enters a reading. The scratch try/ scripts and outputs are committed (rule 7: a
  `run_try.sh` regenerates every number; `--check` compares to the committed TSV).

## Stop rule
Cap USD 4, box end 09:40 UTC: stop before a unit that would cross 80% of either (09:25 UTC). Units: Opus floor ~2, image look ~0.5,
one Sonnet call ~0.6, script runs ~0.3.
