# TXP-KP2C results: known-answer control of the kp2 truth recipe on dint-f128-print (9 Oct 2026, 17:49-17:5x UTC by date -u)

LANE TX-ENGINEER-2 round 4, PREREG `benchmark-tx/PREREG-txeng2-4.md` section C1 (binding; TX-RED F3). Read-free: no vision
call, no reader, no subagent, no network beyond git. Script `kp2c.py` (`--check` exits 1 if stale) runs the kp2 recipe
unchanged (`benchmark-tx/truth_variant.py` `keyprint_rows(variant='kp2')`, fold of build_dint-f89-gloss.py) on f.128r with the
1882 print's letters at the aligned positions (`f128/print_align/align_print.tsv` plain_chunk) as the gloss and the
alignment's own status for the neighbour conflict rule. The print truth (`benchmark-tx/dint-f128-print.truth.tsv`) is put
through `dint128_label_map.tsv` (kp2's vocabulary) for the comparison. No truth file edited; the kp2 truth for f.128 is written
here (`dint-f128-print.truth.kp2c.tsv`), not added to BENCHMARK-TX.tsv. The gate's word "agrees" was fixed as set equality
in the script header, committed (b41cb30ae) before the first run; equal-or-contains is reported beside it.

## Per position (`per_position.tsv`)
| class | n |
|---|---|
| scored by both: equal | 31 |
| scored by both: kp2 strictly contains the print set | 28 |
| scored by both: kp2 misses a print-set member | 0 |
| print-only (kp2 excluded: align-uncertain, neighbour conflict:*) | 26 |
| kp2-only (print excluded: key row agree < n 30, conflict:* 21, single 1) | 52 |
| neither | 46 |

**Gate (declared: agree = equal, >= 0.90 of positions scored by both): 31 / 59 = 0.525 -> FAIL.** Equal-or-contains 59/59 =
1.000. Under the PREREG the kp2 items (dint-f89/f98v/f113-gloss-kp2) stay out of every pool as truth-unknown.

Where kp2 is wider (28): e {.,0,1,o} vs {.,o} x8; i {1,L,p} vs {L,p} x8; d {#,3} vs {3} x4; a {4,v} vs {4} x3; u {a,m} vs {a}
x3; t {m,v} vs {m} x2. Every extra member is a sign key_print itself gives two values (0 e 11/18, 1 e/i 3/3, # c/d 7/6, v a/t
8/5, m u/t 8/2): kp2 admits it by design (share >= 0.3), the print truth does not (agree == n). The difference is a
truth-definition choice on multi-valued signs, not an alignment or letter disagreement: kp2 never misses a print-right sign.

## Pass B under each truth (tools/tx_bench.py, --label-map dint128_label_map.tsv; raw `scores.txt`)
| truth | scored | err_true (errors: wrong + del + ins) | Wilson 95% |
|---|---|---|---|
| print (bench row dint-f128-print) | 85 | 0.188 (16: 11 + 0 + 5) | 0.119-0.284 |
| kp2 on f.128 (kp2c) | 111 | 0.180 (20: 15 + 0 + 5) | 0.120-0.262 |
| print, restricted to the 59 common positions | 59 | 0.220 (13: 8 + 0 + 5) | |
| kp2, restricted to the 59 common positions | 59 | 0.220 (13: 8 + 0 + 5) | |
On the 59 common positions the 28 wider sets change no pass-B verdict (same 8 wrong, same confusions). kp2's extra wrongs come
from kp2-only positions (top: s <- 0 x4, where 0 as s is 4/18 = 0.22 < 0.3 so kp2's S(s) = {sq}).

## Reading (no gate moves on it)
The declared gate fails, so the f89/f98v/f113 kp2 truths stay truth-unknown. Read beside it: on the one leaf with an
independent truth, kp2 never rejected a print-right sign and, on pass B, scored the common positions identically; its
disagreement is wholly in accepting second values of multi-valued signs, which can only hide errors (a lower-bound effect on
err_true), never invent them. A gate defined as "kp2 misses no print-right sign" would have passed 59/59; that is a different
gate and is not substituted here (rule 3; the lane decides whether to pre-register it).

## Calls and cost
0 vision calls, 0 subagents, 0 network requests (git only). Dollar figure: the orchestrator's get_session reading.
