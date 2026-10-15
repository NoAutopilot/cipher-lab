# PREREG-SUR-TRY (15 Oct 2026, account 4, worker SUR-TRY for LANE DEFAULT-A4-0645-15; written before any --try run)

Question: SUR-2061 (second run) placed den Heijer 2012 p.362's "garde" at 2061 legend c, L08 47-51, implying L08:47 sign g = g
(key_period_codes_nieuw.tsv row g = g|l, M) and L08:51 sign 7 = e (already e, M). Does `decode_key.py --try` support g = g?

Instrument: `tools/decode_key.py ciphers/na-suriname-map-1781 --config <scratch single-job config>` holding only the 2061
Nieuw job (decode.json job index 6: ciphertext_2061_battery.tsv, key_period_codes_nieuw.tsv, exceptions_nieuw_image.tsv),
`--lm nl18` (tools/data/nl18, Dutch 1700-1800), default window 8, nulls 100, seed default, default acceptance rule.
Scratch copies only; key.tsv / key_period* / exceptions are never edited by this job.

Structural notes, fixed before running:
- --try is code-level (every occurrence of g, n = 17 incl. 2 exception positions read p), not per-token. A per-token
  exception at L08:47 alone has n = 1 and is "undecided" by construction (never testable by --try); not run.
- --try folds the current value g|l to its first letter g, so "g = g" is "equals the current value" (undecided by
  construction). 7 = e likewise equals the current value. Neither is run as such.
- Hence two runnable tests of the class value that "garde" bears on:
  T1  g = l against the current g (key unchanged). reject => the sheet reads g better than l at g's occurrences (supports
      "garde"); accept => l reads better (against); undecided => no decision.
  T2  g = g with g's key row removed in a scratch key (g has no value; statistic = g minus the runner-up letter).
      accept => supports; reject => against; undecided => no decision.

Power controls (run FIRST, same config, same LM):
  C1 (for T1): a known wrong value on an H code: k = a (k is H o, n = 9). Must be REJECTED. If not, T1 is a non-test.
  C2 (for T2): a known right value on a hidden H code: h's row removed in a scratch key, try h = n (h is H n, n = 10).
      Must be ACCEPTED. If not, T2 is a non-test.
If both controls fail, nothing is reported but "non-test". Whatever T1/T2 say, nothing enters key.tsv or any key/exception
file in this job (brief: report accept / reject / non-test); an accepted value would remain M until a lane decides.
