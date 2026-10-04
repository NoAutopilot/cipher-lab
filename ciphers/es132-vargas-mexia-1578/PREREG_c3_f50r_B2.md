# PREREG addendum B2, es132-vargas-mexia-1578 f.50r replacement pass B (RUN5-ES50B, LANE-RUN5 account 1, 4 Oct 2026, written 12:4x UTC by `date -u`, before the replacement pass or any re-decode)

Brief: `.claude/briefs/runs/2026-10-04-acct1-run5-wave1.md` section RUN5-ES50B unit (a). **Replacement pass B, prompt change only.**

Why: RUN4-ES50R's pass B wrote no '.' vowel sign (0/450 tokens; pass A 103/458; every earlier pass on this hand 99-122), giving
err_2reader 184/460 = 40.0% and a gate (b) margin of 0.003 on pass B. That is a reader notation lapse, not a reading.

What changes: one new blind Sonnet pass on the same 72 f50r crops already on disk (no fetch, no re-cut), prompt
`run2/pass_prompt_f50r_B2.md` = `run2/pass_prompt_f50r.md` plus one paragraph saying explicitly that the dot vowel sign is written '.'
(diff in the commit). The reader sees no other pass, no decode, no key. Output `passes/f50r_passB.tsv`; the RUN4 pass B is kept as
`passes/f50r_passB_run4.tsv`, its reconciled text, result and reading as `ciphertext_f50r_run4.tsv`, `c3_test1_f50r_result_run4.json`,
`reading_f50r_run4.txt` (unchanged copies, for the side-by-side report).

What does not change: everything in `PREREG_c3_f50r.md` / `PREREG_c3_f50r51r.md` -- pass A (the same file), statistic, nulls (200
order-shuffle, 200 key-shuffle, seed 1578), gate (b) on pass A, pass B and reconciled (primary = both blind passes), positive control
f.90v unprinted lines in the same run, grades. Reconciliation `run2/reconcile_f41r.py --page f50r` with no rule changed; scorer
`test2.py --page f50r` unchanged. Reported: new err_2reader, '?' count, gate rows, beside the old (40.0%, 179 '?', B margin 0.003).
Whatever the new pass gives is reported; there is no second replacement.
