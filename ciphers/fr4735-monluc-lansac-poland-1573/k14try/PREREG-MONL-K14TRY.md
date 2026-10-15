# PREREG MONL-K14TRY (15 Oct 2026, 13:1x UTC by date -u; account 4, worker MONL-K14, for LANE DEFAULT-A4-1236-15)

Questions (MONL-K04TRY's Verdict, MONL-L21's recurring contradictions), from align_c268.tsv (c268 L01-L25):
- S: K14 (table p) faces clear s 19 times (p 7); K34 (table p) faces s 3 times (p 10). Does the window context alone prefer s there?
- M: K62 (table l, key grade M) faces clear m 11 times (l 1). Does the window context alone prefer m there?
Non-blind in selection (chosen by the clear text); the --try statistic sees only the cipher stream.

Instrument: tools/decode_key.py --try (window 8, nulls 100, fr16) on scratch copies of this folder (key.tsv here never written),
the same design as k04try/PREREG-MONL-K04TRY.md (d15cebaf1). Script k14try/run_k14try.py; outputs k14try/try_log.tsv, runs.txt,
per_occurrence.tsv. Pseudo-code relabels in scratch only. Samples by random.Random(415) where a subset is drawn.

Runs (all fixed now):
- R0s: K14=s code-wide (both jobs). R0m: K62=m code-wide. As in MONL-K04TRY, expected undecided/reject; only R0 could license a key value.
- T14: the 19 s-facing K14 -> pseudo K14S (key p); try K14S=s.
- T34: the 3 s-facing K34 -> pseudo K34S (key p); try K34S=s. n=3: reported, its own PC3/NC3 below.
- PCs (power at s, n=19): the 19 s-facing tokens whose table is s (K37 16 + K67 3) -> pseudo K37X with the key set WRONG to p; try K37X=s.
- NCs (wrong-facing, n=17, all available): the 17 p-facing K14/K34 -> pseudo K14P (key p); try K14P=s. Must not accept.
- PC3 / NC3: 3 drawn from PCs's pool / 3 drawn from the 10 p-facing K34, as above, for T34.
- Tm: the 11 m-facing K62 -> pseudo K62M (key l); try K62M=m.
- PCm (power at m): the only m-facing tokens with table m, K11 3 + K65 2 = 5 -> pseudo K11X key WRONG to l; try K11X=m. n=5 < 11
  (no more exist in L01-L25); stated as a weaker power check.
- NCm (wrong-facing, n=11): 11 of the 28 l-facing K10 (table l) -> pseudo K10L (key l); try K10L=m. Must not accept.
Rule 3 check: each control can differ from its target: the statistic depends on each occurrence's neighbours (different positions)
and on the true letter there.

Decision per question (fixed before any run), as MONL-K04TRY:
- PC not accept -> T is "untested-by-this-tool" at that n, nothing moves (for M: PCm at n=5 not accepting is logged as power unshown,
  and Tm is then a statistic only, not a lead).
- PC accept and NC accept -> instrument does not discriminate; non-test.
- PC accept, NC not accept, T accept -> lead "the selected tokens read s (m) by context"; no key edit and no relabel in this job
  (brief: leads only unless --try accepts with its controls passed; a key value change would need the code-wide R0 to accept AND
  its controls; T is non-blind in selection). If R0 accepts with T/PC/NC as above, that is logged as a candidate key correction
  for a verifier, still no key edit in this job.
- PC accept, NC not accept, T reject -> context prefers the key value: the clear text or the alignment is suspect there; lead.
- T undecided -> logged undecided.
Also reported: per-occurrence gain (n=1 runs, statistic only), count > 0 and < -3 bits.
Then (brief part 2), only if >= 40% of the 4.5 cap is left: regen_monll11/16/21.sh (openapi.bnf.fr, scratch only) and one value-blind
K04|K12 + K40/K45 sort; a separate PREREG section is added before that sort.
