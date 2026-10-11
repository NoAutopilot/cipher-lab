# TXE3-3 CROSSHAND results (account 3, session_01YB6j6UY3F3EFihTGvxULmf, 11 Oct 2026 05:47-06:0x UTC by date -u)

Pre-registration: benchmark-tx/PREREG-txeng3-3.md (commit 3d2f7916, before any read). Question: does the no.87 two-pass Sonnet
line-read protocol (two blind passes -> reconcile_passes.py -> one blind adjudication of the disagreements from the crops) read a
SECOND hand at the 5% target? Target: gunther8246-p2 lines p2_L01-L17 (Willem van Oranje's German secretary, 1561; eval; 214 scored
of 251 reference positions, 10 build-time align-conflict flags on these lines). Matched control, same session, same readers, same
recipe: Birago no.87 f.178v lines L01-L09 (253 scored). Every reader output was committed with its sha256 before its score
(SHA256SUMS.prescore; commits 4463a1db, 2nd pass B, no.87 passes, 812df411, passC_no87). Scoring: tools/tx_bench.py
--coverage-diagnostic (declared line subset: the item's other lines listed as missing, not scored) --line-prefix via make_adjud.py
norm; as measured AND flagged-excluded, never the latter alone; Wilson 95% computed from the counts.

## Numbers

| output | gunther L01-L17 as measured (95%) | flagged-excluded (95%) | no.87 f178v L01-L09 as measured (95%) | flagged-excluded (95%) |
|---|---|---|---|---|
| pass A (Sonnet, this session) | 0.065 (14/214) 0.039-0.107 | 0.029 (6/206) 0.013-0.062 | 0.103 (26/253) 0.071-0.146 | 0.085 (21/248) 0.056-0.126 |
| pass B (Sonnet, this session) | 0.051 (11/214) 0.029-0.090 | 0.019 (4/206) 0.008-0.049 | 0.166 (42/253) 0.125-0.217 | 0.149 (37/248) 0.110-0.199 |
| **reconciled + adjudication (passC, this session)** | **0.065 (14/214) 0.039-0.107** | **0.034 (7/206) 0.017-0.068** | **0.043 (11/253) 0.024-0.075** | **0.024 (6/248) 0.011-0.051** |
| committed passes on the same lines (for reference) | Opus baseline, all 25 lines: passZ 0.057 / 0.017; A 0.060, B 0.063 | | committed A 0.055 (14/253), B 0.095 (24/253), C 0.051 (13/253) 0.030-0.086 | C 0.032 (8/248) |

Pair agreement (reconcile_passes.py, nw): gunther 240/253 = 94.9% (13 disagreements, 15 agreed-uncertain); no.87 212/266 = 79.7%
(54 disagreements, 19 agreed-uncertain). Adjudication: gunther 13 rows -> A 4, B 8, NONE 1; no.87 54 rows -> A 33, B 12, NONE 9
(the NONE rows are one reader's splits of T83 and T29 into two signs).

Paired (tx_bench --paired, line sign test): gunther passC vs A improved 3 / worsened 2 (p 1.0), vs B improved 0 / worsened 3 (p 0.25:
the adjudicator took the wrong candidate three times); no.87 passC vs A improved 8 / worsened 0 (p 0.0078), vs B 8 / 0 (p 0.0078);
this session's passC vs the committed passC on the same nine lines: improved 5 / worsened 3 (p 0.73), 13 -> 11 edits.

Ratio reconciled / better single pass (secondary endpoint; no.87 committed 0.051/0.066 = 0.77, "about 0.75"):
gunther 0.065/0.051 = **1.27** (vs mean of A and B 0.058: 1.12); no.87 control this session 0.043/0.103 = **0.42** (vs mean 0.1345: 0.32).

Top confusions (truth value <- read), gunther passC: s<-Ib x2, f<-x x2, h<-aa, e<-v, g<-b, o<-g, e<-NEW:f-struck-by-bar, d<-NEW:f-struck-
by-bar; 7 of the 14 sit on the build's align-conflict flags (positions where the committed reference sign itself is keyed to another
letter than the print forces: th=o, Ib=s, x=f, repeating by label; the item's builder reads them as key gaps or encipherer's slips,
not misreads). no.87 passC: m<-X_NEW x3 (both readers labelled one recurring m-value shape off-sheet), e<-T88 x2, then singles.

## Gates
- **Control validity gate (declared): PASS.** Control reconciled 0.043 <= committed passC on the same lines 0.051 + 0.030. The
  session's pipeline reproduces the no.87 figure on these lines (point estimate below it, paired 5/3 against it, not distinguishable),
  although this session's single passes read far worse than the committed ones (0.103 / 0.166 vs 0.055 / 0.095): the control did vary
  on the statistic and landed where the committed record says; outcome (b), session drift, is not declared.
- **Primary gate (reconciled err_true <= 0.050 as measured on the second hand): FAIL as measured** -- 0.065 (14/214), 95% 0.039-0.107.
  Flagged-excluded 0.034 (7/206) is under the line, reported beside, never alone. The interval contains 0.05 (a true 5% hand would show
  about 11 errors here; 14 were seen), so at N = 214 this is a miss of the point estimate, not a demonstrated excess. Null result.
- **Ratio: the reconciliation gain did not transfer.** On no.87 the second reader plus adjudication cut the error to 0.42 of the better
  single pass (committed 0.77); on the German hand it was 1.27 -- reconciliation fixed nothing (0 improved vs the better pass) and the
  adjudicator broke three. Reason visible in the data: the two Sonnet readers agreed on 94.9% of gunther signs and their errors are
  SHARED (both read Ib for the s-sign, x for the f-sign, aa for the h-sign), so the disagreement list holds almost none of the errors;
  on no.87 the readers' errors are disjoint look-alike splits (T51/T95, T18/T36, T45/T89, T78/T86) that a third look can settle.
  Agreement is not accuracy (LESSONS.md), here in the shape "two readers agree on the wrong label".

## What it means for the owner (three sentences)
On a second hand the no.87 two-pass recipe reads at about 6.5% as measured (3.4% once the ten positions the item's own build marks as
key gaps are set aside), so the 5% figure is close but not reproduced on the German secretary's hand at this sample size. The part of
the recipe that earned no.87 its number -- a second reader plus an adjudicator catching look-alike splits -- gave nothing here, because
both readers made the same mistakes on the same letter-shaped signs, and the Opus two-pass baseline already on file for this item
(0.057 / 0.017 on all 25 lines) sits in the same place. The gain from reconciliation is a property of a hand whose signs split into
look-alike pairs, not of the recipe, so the next hand should be budgeted at single-pass error unless its pair agreement is well under 90%.

## Not run
Units 7-8 (lookalike_pass.py windows re-read -> passD) were not started: the rate-limit status read `allowed_warning` at 05:58 UTC
(BUDGETS.md scaling rule: no new workers), and they were the pre-registered first drop; they would have re-read only the 13 / 54 split
tiles, which on gunther hold at most 3 of the 14 errors (the as-measured gate could not have passed through them: 11/214 = 0.051).
No truth file was read by this session before its outputs were committed (tx_bench reads them); no truth or BENCHMARK-TX row changed;
no eval item other than the two named was scored; bir1591-f23r-gloss was not used (gloss-visible, TXE2 F3). Reader model: the Agent
tool's `sonnet` alias at this date (the committed no.87 passes of 2 Oct 2026 were claude-sonnet-5): the much worse single passes on
the control lines (0.103 / 0.166 vs 0.055 / 0.095) are the one sign of reader drift in this session, and they were absorbed by the
reconciliation step, not by the readers.

## Next step and cost
The remaining 8 gunther lines (L18-L25, 103 reference positions) plus the 582 committed signs of MS p.1 and p.3 at single-pass Sonnet
cost (about USD 1 per 250-sign chunk per reader; one chunk, one reader, about USD 1.5 including scoring) would put the hand's figure
on about 500 scored signs; two chunks x two readers + adjudication about USD 6. A genuinely informative follow-up is instead a hand
whose two-reader agreement is under 90% (Dinteville 1592 fr.3621 f.128r reads 0.19-0.35 per pass): that is where the recipe's
second reader can show whether it transfers. Promotion candidate (Usage 8): make_adjud.py's queue/apply as reconcile_passes.py
options --adjudication-queue / --apply-adjudication (the same shape now exists three times: no.87 adjudicate_in, txpool make_queue.py,
this folder).

Cost: six Sonnet subagent calls (4 readers, 2 adjudicators), about 836k subagent tokens in total; session cost per the parent's
get_session. Box 05:47-06:0x UTC of 2 h. Requests to any host: 0 (disk only).
