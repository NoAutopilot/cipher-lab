# PREREG MONL-K04TRY (15 Oct 2026, 12:4x UTC by date -u; account 4, worker MONL-K04, for LANE DEFAULT-A4-1236-15)

Question: the 15 K04 tokens (table d) that face clear n in align_c268.py (c268 L01-L25: L06:18 L06:23 L06:34 L08:10 L08:19
L09:27 L10:33 L13:14 L15:4 L16:16 L18:18 L21:9 L22:14 L24:12 L25:26) -- does the window context alone (fr16 LM, no clear text)
prefer n over d there? Non-blind in selection (chosen by the clear text); the --try statistic itself sees only the cipher stream.

Instrument: tools/decode_key.py --try (window 8, nulls 100, fr16), run on scratch copies of this folder (key.tsv here never written).
Runs, all logged with --try-log to a scratch path, then copied to k04try/try_log.tsv:
- R0 (as briefed, code-wide): --try K04=n on the folder as is (34 occurrences: 19 d-facing, 15 n-facing). Expected reject.
- T (target): the 15 n-facing K04 relabelled to pseudo-code K04N (key row K04N = d); --try K04N=n.
- NC (negative control, same selection rule, same N): 15 of the 19 d-facing K04 (random.Random(415).sample, sorted) relabelled
  K04D (= d); --try K04D=n. Must not accept.
- PC (power control, same N, same band, same selection rule): 15 of the 27 n-facing K12 (random.Random(415).sample) relabelled
  K12X with the key row set WRONG to d; --try K12X=n. Must accept for the instrument to have power at n=15.
Rule 3 check: all three can differ from T, since the statistic depends on each occurrence's neighbours (different positions)
and on the true letter there.

Decision (fixed before any run):
- PC not accept -> T is a non-test at n=15 ("untested-by-this-tool"), nothing moves.
- PC accept and NC accept -> instrument does not discriminate here; non-test, nothing moves.
- PC accept, NC not accept, T accept -> lead "the 15 read n by context": supports relabel K04->K12 (or a second value); no key edit
  and no relabel in this job (brief: no key edit unless --try accepts AND its control passed -- a homophone value K04=n would need
  the code-wide R0 to accept, which T does not show); written as a lead for a value-blind sort.
- PC accept, NC not accept, T reject -> context prefers d at the 15: the clear text or the alignment is suspect there; lead.
- T undecided -> logged undecided.
Also reported: per-occurrence gain at the 15 (how many > 0).
