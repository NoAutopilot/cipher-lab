# PREREG f41r-settle -- es132-vargas-mexia-1578: settling f.41r's 81 default-flagged tokens from the crops (RUN3-ES41, LANE-RUN3 account 1, 4 Oct 2026, written 08:5x UTC by `date -u`, before any crop is read for this purpose)

Brief: `.claude/briefs/runs/2026-10-04-acct1-run3-wave1.md` section RUN3-ES41 step 2. Input: the ES132-C3 reconciliation, regenerated
unchanged by `run2/reconcile_f41r.py` (now writing `ciphertext_f41r_pre.tsv`, byte-identical to the committed ciphertext_f41r.tsv, plus
`run2/f41r_units.tsv` and `run2/f41r_firm.tsv`). Script: `settle_f41r.py` (`--build` writes the items, `--apply` writes ciphertext_f41r.tsv;
`--check` exits 1 if stale).

## Units
The 81 "default" tokens are 56 units: 44 one-to-one pairs (pass A token vs pass B token) and 12 unequal spans (A tokens vs B tokens, one side
possibly empty). The 32 R7 tokens (same base, a mark or dot seen by one reader) and the 3 R5 tokens are NOT in scope (the brief names the 81).

## Reader (one unit of work)
One Opus subagent, blind: it sees only `run2/settle_f41r_items.tsv` and the line crops it names (s1/s2 chosen by the unit's position in the
line: fraction < 0.4 -> s1, > 0.6 -> s2, else both), plus the pass notation (`run2/pass_prompt_f41r.md`). No key, no decoded text, no reading,
no NOTES. Per item: line, crops, three stream tokens before and after (context, to locate the place), and two options in an order drawn by
random.Random(4141); the reader answers option 1, option 2 or "other: <tokens>", with confidence high/low. Mixed among the 56 units, in
random order and indistinguishable in form, are 20 decoy items (the control below).

## Settle rule (applied by settle_f41r.py --apply, mechanically)
S1 high-confidence pick of an option -> that option's tokens replace the unit, unflagged.
S2 low-confidence pick of an option -> that option's tokens, every one flagged '?'.
S3 "other" -> the reader's tokens, flagged '?'.
No answer -> unit unchanged (A tokens, flagged).

## Control (rule 3; can it differ? yes: the statistic is which option the reader picks at a firm position, and the decoy option is a different
token at the same position, so the reader can pick it)
20 firm tokens (both blind passes equal, unflagged; random.Random(41).sample over `run2/f41r_firm.tsv`, single tokens, codes >= 38 and braces
excluded) each paired with a decoy made by the first applicable look-alike substitution observed in this page's own A/B disagreements
(base digits 21<->11, 12<->22, 14<->11, 20<->10, 13<->23, 24<->249; vowel sign ρ<->σ; '+' dropped/added; '.' <-> '+').
Gate: the firm token is picked with high confidence in >= 18/20 AND the decoy is picked with high confidence in <= 1/20.
If the control FAILS: nothing is applied (ciphertext_f41r.tsv = the _pre stream); the reads are kept as image-check pointers only.

## Scoring (unchanged)
`test2.py --page f41r` unchanged (PREREG_c3_test1.md statistic, nulls, gate, positive control f.90v in the same run) on the settled stream;
before (committed c3_test1_f41r_result.json, copied to c3_test1_f41r_result_pre.json) and after reported side by side. Grades per
PREREG_c3_test1.md (S where page gate passes on both blind passes and the control passes, '?' tokens M, codes U). The blind passes' S_b
cannot change (they are not touched); only the reconciled row and the grade counts move.

## Clarification before any read (08:5x UTC, same session)
The firm-token population for the decoys is restricted to tokens beginning with a digit (the first build drew the plain letter 'y',
which is not a numeral group and has no look-alike substitution in this list). No crop had been read for settlement when this was changed.
