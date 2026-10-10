# PREREG TX-ENGINEER-2 round 18 (lane incarnation 3, session_01P46fwsU5VTc1oJiV1sayg5, 10 Oct 2026 00:3x UTC by date -u; pushed BEFORE the run; the orchestrator's addendum of 00:32 from TX-RED pass 11 F50)

Rules as PREREG-txeng2-5's preamble. `tools/tx_register.py --check benchmark-tx/PREREG-txeng2-18.md` output before the spawn: `OK benchmark-tx/PREREG-txeng2-18.md: names register rows and states a difference` (exit 0).

## SCAN-103 Read-free window scan of the f.103r (confirm2) truth's alignment, the DV1c scan applied to the S2 item (TXE2-SCAN103; Opus 5.5; cap 3; box 40 min; read-free; no truth position printed)
Nearest prior: DV1c / TXE2-VIV102-ANCHOR (j0scan.py / j0confirm.py on f.102r: the registered anchor was ~750 letters late; f.103r
checked there only under bounds shifts of one line, margins 0.0436-0.0645, not under a window scan of its start offset), N5-VIVK
(f.103r's stretch is end-anchored to the clerk's closing paragraph). What is different: the item is the S2 confirm2 truth itself, and
the question is whether its registered alignment is the best over a window by the SAME margin test f.102r used -- j0scan over
start offsets s = 0..(len(dec_norm) - window) step 50 for the f.103r collapsed stretch (the same DP, band 400; window = the
stretch's registered letter span + 25%), published key vs 50 shuffled keys per offset, then j0confirm at the best offset and at the
registered offset with 200 shuffles and the selection-fair null (each shuffled key's best share over the scan). Gate (declared):
the S2 record STANDS if the registered offset is the argmax of the real share over the scan (within one step of 50 letters) AND its
selection-fair margin is >= 0.03; else NOT BEST, with the best offset, both margins and the letter distance reported. Output:
benchmark-tx/txeng2/scan103/RESULTS.md with the scan table, every number, every commit hash with sha256, "Openings of eval truth:
0" (the truth file is never opened; the builder's stream and dec_norm are read by script as DV1c did), and a final "Verdict:
measured: STANDS at offset ... / NOT BEST: registered ... best ... margin ..." line. The worker builds nothing and re-scores
nothing; a new truth, if licensed, is a separate PREREG.

Costs this round: 3. Eval looks this round: 0. Openings: 0.
