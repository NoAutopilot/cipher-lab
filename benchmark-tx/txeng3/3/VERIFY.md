# TXE3-3 CROSSHAND: verification (11 Oct 2026, 14:5x UTC by date -u)

Verifier for the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M). This session did not run the experiment
(session_01YB6j6UY3F3EFihTGvxULmf) and does not protect its conclusions. Method: committed files only, at origin/main
114ee2a1c; `tools/tx_bench.py` as committed; the folder's own `make_adjud.py` and `tools/reconcile_passes.py`. No reader
pass, no image read, no network. No confirm item, no oracle1 answer and no owner page was opened or written. The
experiment's own files are unchanged. My scripts are in the session scratchpad, not committed: an error-sharing count
and an oracle-adjudication bound, both built on `tx_bench.align`.

## Verdicts on the three sentences told to the owner

| # | Claim as told | Verdict | Corrected sentence |
|---|---|---|---|
| 1 | In a second hand (gunther, German secretary) the no.87 two-pass recipe came out at about 6.5% error. | **holds** (needs its qualifiers) | On 17 of the page's 25 lines (214 scored signs), the recipe read 6.5% as measured (14/214, 95% 3.9-10.7%). That is 3.4% (7/206) with the 8 positions the item's own build flags as key gaps or slips set aside. |
| 2 | Both readers made the same mistakes there, so the second reader added nothing. | **wrong** (the reason is contradicted; the outcome is right) | Reconciliation gave no net gain: 14/214 errors, the same as pass A and worse than pass B (11/214). The cause was not shared reader errors. Of the 8 errors the two readers shared, 7 sit on flagged key-gap positions, and at most of those both readers wrote the sign the reference transcription itself has. At the 7 errors only one reader made, the blind adjudicator chose the wrong label 5 times. Had every disagreement been settled correctly, the result would have been 4.2% as measured (9/214) and 1.0% flagged-excluded (2/206). |
| 3 | The 5% result does not carry over (it held on no.87 only). | **overstated** | Not confirmed on the second hand at this sample size, but not refuted either. The point estimate missed the registered gate (6.5% against <=5% as measured). The interval still contains 5%. The difference from the no.87 control run beside it (4.3%, 11/253) is not significant (Fisher p 0.31). The Opus two-pass pipelines already on file read these same 17 lines at 5.6-6.5% but the whole page at 4.7-5.1%. |

## Re-derivation (reported beside re-derived, committed scorer)

Commands: `python3 tools/tx_bench.py --bench BENCHMARK-TX.tsv --item gunther8246-p2 --coverage-diagnostic --line-prefix p2
--exclude-flagged <file>`. For no.87 use `--item birago1572-no87` and drop `--line-prefix`. For the committed no.87 passes on
the same lines, first restrict them to rows `f178v_L0[1-9]`.

| output | reported | re-derived | match |
|---|---|---|---|
| gunther pass A | 0.065 (14/214) / 0.029 (6/206) | 0.065 (14/214) / 0.029 (6/206) | yes |
| gunther pass B | 0.051 (11/214) / 0.019 (4/206) | 0.051 (11/214) / 0.019 (4/206) | yes |
| **gunther passC** | **0.065 (14/214) 0.039-0.107 / 0.034 (7/206) 0.017-0.068** | **same; Wilson 0.039-0.107 / 0.017-0.068** | yes |
| no.87 L01-L09 pass A | 0.103 (26/253) / 0.085 (21/248) | same | yes |
| no.87 L01-L09 pass B | 0.166 (42/253) / 0.149 (37/248) | same | yes |
| **no.87 L01-L09 passC (control)** | **0.043 (11/253) / 0.024 (6/248)** | **same; Wilson 0.024-0.076** | yes |
| committed no.87 A / B / C, same 9 lines | 0.055 (14) / 0.095 (24) / 0.051 (13) 0.030-0.086; C 0.032 (8/248) | same | yes |
| control validity gate | 0.043 <= 0.051 + 0.030 PASS | 0.043 <= 0.081 PASS | yes |
| paired gun C vs A / vs B | 3/2 p 1.0; 0/3 p 0.25 | same (edits 14->14; 11->14) | yes |
| paired no.87 C vs A / vs B / vs committed C | 8/0 p 0.0078; 8/0 p 0.0078; 5/3 p 0.73, 13->11 | same | yes |
| pair agreement | gun 240/253 = 94.9% (13 dis.); no.87 212/266 = 79.7% (54) | same (agreement.tsv sums; 13 and 54 rows) | yes |
| adjudication split | gun A 4 / B 8 / NONE 1 | same (adjud_out_gun.tsv) | yes |
| ratio C / better single | gun 1.27 (vs mean 1.12); no.87 0.42 (vs mean 0.32) | 1.27 / 1.12; 0.42 / 0.32 | yes |
| committed no.87 whole-item ratio | 0.051/0.066 = 0.77 | passC 0.051 (41/803), passA 0.066 (53/803) | yes |
| "Opus baseline, all 25 lines: passZ 0.057 / 0.017; A 0.060, B 0.063" | as quoted | **stale**: today's scorer and flags give passZ_pipeline 0.047 (15/317) / 0.016 (5/305), A 0.051, B 0.054. The lane's current base passZ_gv2 is 0.051 (16/317) / 0.020 (6/305). The quoted figures were copied from txpool/gunther8246-p2/RESULTS.md, which predates the TXV-GUN truth corrections. | **no** |
| "10 build-time align-conflict flags on these lines" / "the ten positions ... set aside" | 10 | **8** flagged positions are scored on L01-L17: 6 key-gap, 1 slip, 1 alignment-doubtful. The other 2 flag-column rows are `corrected:*` and are scored normally (214 - 206 = 8). | **no** (count) |

Rule 7: the deterministic part of the chain regenerates byte for byte from the committed reader files. That covers
`make_adjud.py norm` -> scored/*.tsv, `reconcile_passes.py --method nw` -> rec_gun/ and rec_no87/ (all 4 files each),
`make_adjud.py queue` -> adjud_queue_gun.tsv, and `make_adjud.py apply` -> passC_gun.tsv and passC_no87.tsv. All 8
SHA256SUMS.prescore entries verify OK.

### Further numbers re-derived for the claims (same scorer, alignment of tx_bench)

| | gunther L01-L17 (214 scored) | no.87 f178v L01-L09 (253) |
|---|---|---|
| sign errors A / B / C | 13 / 10 / 13 (each +1 insertion) | 21 / 39 / 11 |
| both readers wrong (same label) | 8 (7) | 11 (8) |
| of those on flagged positions | **7 of 8** | 5 of 11 |
| both wrong, unflagged | **1** (L02.4, aa for h) | 6 |
| only one reader wrong | 7 (A 5, B 2) | 38 (A 10, B 28) |
| adjudicator right at those | **2 of 7** | 38 of 38 |
| oracle bound (correct pick at every disagreement) | **0.042 (9/214) 0.022-0.078 / 0.010 (2/206)** | 0.043 (11/253) = actual |
| committed reference (committed.tsv) scored as an output | 0.037 (8/214) / 0.000 (0/206) | -- |
| Opus pipelines on file, same lines | passZ_pipeline 0.056 (12/214) / 0.024; passZ_gv2 0.065 (14/214) / 0.029 | -- |
| Opus passZ_gv2, all 25 lines / L18-L25 only | 0.051 (16/317) / 0.019 (2/103) | -- |

The 7 one-reader errors at gunther disagreements are L02.7, L04.1, L04.14, L05.9, L07.6, L08.17 and L13.5. The adjudicator
was right only at L08.17 and L13.5. At 5 of the 7 flagged shared errors (L11.1, L11.13, L12.5, L15.12, L17.13) both readers
wrote exactly the committed reference sign (x, Ib, d6, th, x): they read the visible sign, and the print-forced letter
differs. Those are truth-side key gaps, not reading mistakes. Two of the RESULTS' examples of "shared errors" are of this
kind ("Ib for the s-sign", "x for the f-sign"); the third, "aa for the h-sign", is the one unflagged shared misread.

Tests: target passC against the control passC, Fisher exact p = 0.31 as measured (14/214 vs 11/253) and 0.58
flagged-excluded (7/206 vs 6/248). Target passC against the Opus passZ_pipeline on the same lines, p = 0.84. If this hand
truly read at 5%, it would give 14 or more errors in 214 signs with P = 0.19.

## Pre-registration order

Commit times from git log, committer then author:
- 3d2f7916 prereg: 05:53:59 (authored 05:53:46).
- 4463a1db pass A gun: 05:56:41.
- d5c9fb4c pass B gun: 05:56:59.
- 33c700cd no.87 A and B: 05:57:39.
- 812df411 passC_gun: 05:59:00.
- 2a17d102 passC_no87 and the first normalised score inputs: 06:00:47.
- 43ea026f RESULTS: 06:03:26.

So the prereg came before every reader output and every score, and every output was hashed before its score. Git cannot
show whether the reader calls were launched before 05:53:46: pass A landed 2 min 53 s after the prereg. Declared
deviations: units 7-8 were dropped as the pre-registered first drop, under allowed_warning, and the reader model is the
`sonnet` alias, not claude-sonnet-5. Both are declared in "Not run". No undeclared deviation was found. The line subsets
(gunther L01-L17, no.87 f178v L01-L09) are as registered.

## Gate as registered, and the verdict it yields

- Registered primary gate: "as-measured err_true <= 0.050 (the brief's gate; the flagged-excluded figure is reported
  beside, never alone)". On 0.065 this gives **FAIL**. The reported FAIL follows.
- Registered control validity gate: "control's reconciled err_true ... <= the committed passC's err_true on the SAME
  lines ... + 0.030". On 0.043 <= 0.081 this gives **PASS**. Reported correctly.
- Registered reading of the outcomes: "(a) control near its committed figure, target above gate -> a hand effect". Taken
  literally, these numbers land in (a). The RESULTS wisely did not say "hand effect"; it said "a miss of the point
  estimate, not a demonstrated excess. Null result." The parent's claim 3 is the literal (a) reading.
- **Rule issue with the registered rule:** (a) infers a hand effect from two point estimates, with no between-arm test.
  At N = 214 / 253 the observed gap is not significant (p 0.31). The two arms also carry different truth-noise floors:
  8/214 = 3.7% of gunther's scored positions are flagged key gaps, where a reader who copies the visible sign is scored
  wrong, against 5/253 = 2.0% on the no.87 lines. And the 17-line subset is harder than the rest of the page: the Opus
  passZ_gv2 reads it at 0.065 but L18-L25 at 0.019. The FAIL stands as a gate result. It does not license "does not
  carry over".
- Note: the "5% result" being replicated is itself 0.051 (41/803) as measured on no.87. It would fail this same <=0.050
  gate.

## Control (CLAUDE.md rule 3)

The control is the same pipeline in the same session on another hand's lines. Its statistic, err_true on its own lines,
can vary independently of the target's: it is a separate read of different images. It did vary. Its single passes came
out much worse than the committed passes on the same lines (0.103 / 0.166 vs 0.055 / 0.095), and the reconciled figure
landed at the committed value (0.043 vs 0.051, paired 5/3). It is a valid drift control.

What it does **not** control is line difficulty or truth-floor differences between the two hands. So it cannot turn the
target's 0.065 into a hand effect: see the gate section. The third-attempt clause does not apply, since this is a first
attempt on this hand. Nothing here retires the recipe for gunther.

## Split

The target (gunther8246-p2) is `eval` and the result is reported only, with nothing tuned on it.

The control lines (no.87 f178v L01-L09) belong to an `eval` row in BENCHMARK-TX.tsv, but they are TX-ENGINEER-2's
`dev_tune` lines (PREREG-txeng2-0 line 62: dev pool = no.87 f178v L01-12). So the control spends no eval look. The
prereg does not say this.

No eval look was used for tuning.

Gunther is in TX-ENGINEER-2's eval pool, and that lane counts openings per item (PREREG-txeng2-0 Amendment 9 (38)). This
run is one more opening of gunther's truth, and RESULTS does not hand that count to the lane.

The control lines are also inside ORACLE-LOCATION-1's no.87 lines (oracle1/manifest.tsv, f178v_L01-L12). Only the
existing harvest crops were read, and nothing in oracle1 was touched. That is no breach, but the overlap is worth
recording.

## Rule issues and objections

1. Claim 2's mechanism ("both readers made the same mistakes") is contradicted by the committed files. The same sentence
   is in RESULTS.md ("their errors are SHARED ... so the disagreement list holds almost none of the errors"). The two
   readers made 15 distinct sign errors between them. The disagreement list holds 7 of those: 6 of the 7 unflagged ones. RESULTS' next-step advice rests on this
   mechanism ("budget the next hand at single-pass error unless pair agreement is well under 90%"). On this hand the
   step that failed was the blind Sonnet adjudication: right at 2 of 7, against 38 of 38 on no.87. That points to a
   human or a stronger adjudicator at the 13 disagreements, consistent with TXE3-1's "disagreement tiles first" order,
   not to dropping the second reader.
2. The Opus baseline figures quoted in RESULTS (0.057 / 0.017; A 0.060, B 0.063) are stale against today's scorer and
   flags, as the table above shows. The fair comparison is the same 17 lines: passZ_pipeline 0.056, passZ_gv2 0.065.
   This is also where RESULTS' "sits in the same place" holds: on the same lines, the Opus base equals the Sonnet passC
   as measured.
3. The flag count is wrong: there are 8 flagged scored positions on L01-L17, not 10. The flagged-excluded figure itself,
   7/206, was computed correctly.
4. Flagged-excluded is never quoted alone in RESULTS or the ROOM line. Claim 1 quotes the as-measured figure alone, which
   TRANSCRIPTION.md allows, but the flagged figure and the interval belong beside it for the owner.
5. Cost: USD 12.84 (LEDGER), under the USD 15 cap but above the registered 80% line (USD 12). The worker cannot see cost,
   and git cannot show whether any unit started after the line was crossed. Six calls in about 16 minutes, against the
   prereg's own per-unit estimate of about USD 8-12: inside the cap.
6. No novelty wording (rule 10 is not engaged). No shared tool was changed: commits touch only benchmark-tx/txeng3/3/,
   PREREG-txeng3-3.md, ROOM.md and LEDGER.md.

## Safe sentence for the owner

On a German secretary's hand, the no.87 two-pass recipe read 6.5% as measured on 17 lines (14/214; 3.4% with 8 key-gap
positions set aside). That misses the 5% gate on the point estimate but is not distinguishable from 5% or from the no.87
control at this size. The second reader did catch most of the real misreads; the adjudication step then picked the wrong
label at 5 of 7 of them. So "does 5% carry over" is undecided, not refuted, and the weak link on this hand is the
adjudicator, not the second reader.

## Second check (11 Oct 2026, written about 16:4x UTC by the account-3 parent from the second verifier's report; workflow wf_35ed2244-0e6)

A second, independent agent ruled on each objection and non-holds verdict above, re-running the commands itself. Where it disagrees with this file, this section governs.

### Rulings on the first verifier's objections

- **agree**: 1. The RESULTS.md Gates/Ratio paragraph ('their errors are SHARED ... so the disagreement list holds almost none of the errors') is contradicted: the list holds 7 of the 15 distinct sign errors, including 6 of the 7 unflagged ones, and 7 of the 8 shared errors are flagged key gaps where both readers copied the reference sign.
  - Evidence: I re-derived this with tx_bench.align over scored/passA_gun.tsv, scored/passB_gun.tsv and passC_gun.tsv at origin/main 7106556de. Each reader has 13 or 10 substitution errors and 1 insertion. 8 positions are wrong in both readers: 7 with the same label, and 7 of the 8 flagged. The one unflagged shared error is L02.4 (aa for h). At L11.1, L11.13, L12.5, L15.12 and L17.13, A = B = ref_sign (x, Ib, d6, th, x). 7 substitution errors were made by one reader only (A 5, B 2), and 6 of the 7 unflagged errors are among them. The verifier's count is slightly low, which only strengthens the objection. rec_gun/disagreements.tsv also holds L05.14, where both readers are wrong with different labels (NEW:f-struck-by-bar vs ps), and both insertion events: B's 'tau' at L01.1 and A's 'NEW:44-struck' at L09.11. So the list holds 8 of the 15 substitution-error positions and 10 of the 17 error events, which is far from 'almost none'. The no.87 side reproduces: 11 positions wrong in both readers (5 flagged), 38 one-reader errors, adjudicator right at 38/38.
- **partly**: 2. The failing step is blind adjudication: right at 2 of 7 one-reader errors on gunther vs 38 of 38 on no.87. An oracle pick gives 0.042 (9/214) / 0.010 (2/206), under the gate. So the RESULTS advice ('budget the next hand at single-pass error unless pair agreement is well under 90%') rests on the wrong mechanism, and the data point to a person or a stronger adjudicator at the 13 tiles.
  - Evidence: The mechanism is right, but the oracle figure is wrong. I built a per-line oracle that picks the best candidate at each of the 13 disagreement rows and scored it with tx_bench (--coverage-diagnostic --line-prefix p2 --exclude-flagged). It gives 0.037 (8/214) as measured and 0.005 (1/206) flagged-excluded, not 0.042 / 0.010. The verifier left out B's L01.1 'tau' insertion, which was a disagreement (A '-') that the adjudicator kept. 8/214 equals the reference transcription's own floor on these lines (committed.tsv, also 8/214). Counting insertions, the adjudicator was right at 3 of 9 one-reader error events: L08.17, L13.5, and the L09.11 drop. On substitutions alone it was 2 of 7, and on the 6 unflagged ones 1 of 6. Two caveats. First, 'a stronger adjudicator' is not shown by these data: they show only that the right label was among the two candidates, and this hand's letter-like inventory (ro/b, g/phi/q, v/r, ]/Ib) may be what defeated it. Second, the verifier did not flag a related sentence in RESULTS 'Not run': 'the 13 split tiles ... hold at most 3 of the 14 errors (the as-measured gate could not have passed through them: 11/214 = 0.051)'. The 13 tiles hold 7 of passC's 14 errors, and a correct pick passes the gate at 8/214. Dropping units 7-8 was still legitimate as the pre-registered first drop under allowed_warning, but the reason RESULTS gives for it doing no harm is false.
- **agree**: 3. The 'Opus baseline, all 25 lines: passZ 0.057 / 0.017; A 0.060, B 0.063' row is stale, copied from txpool RESULTS, which predates the TXV-GUN corrections. Today's figures: passZ_pipeline 0.047 (15/317) / 0.016, A 0.051, B 0.054; passZ_gv2 0.051 / 0.020; same 17 lines: passZ_pipeline 0.056, passZ_gv2 0.065.
  - Evidence: txpool/gunther8246-p2/RESULTS.md (e16e02578, 9 Oct 21:04) carries 0.057 (18/317), 0.060 and 0.063. TXV-GUN (e2403418a, 9 Oct 21:43) changed the truth afterwards. txpool passZ_pipeline.tsv is byte-identical to outputs/gunther8246-p2/passZ_pipeline.tsv. Scored against the e16e02578 truth, it gives exactly 0.057 (18/317) / 0.017 (5/302). Against today's truth it gives 0.047 (15/317) / 0.016 (5/305), with A 0.051 (16/317), B 0.054 (17/317) and passZ_gv2 0.051 (16/317) / 0.020 (6/305). On L01-L17: passZ_pipeline 0.056 (12/214), passZ_gv2 0.065 (14/214). On L18-L25: passZ_gv2 0.019 (2/103). All reproduce.
- **agree**: 4. RESULTS says '10 build-time align-conflict flags on these lines' and '3.4% once the ten positions ... are set aside'; the truth has 8 flagged scored positions on L01-L17 (6 key-gap, 1 slip, 1 alignment-doubtful), the other 2 are corrected:*; 7/206 itself is right.
  - Evidence: The current truth file has 10 non-empty flag rows on L01-L17. Two of them (L06.9, L06.12) are corrected:* and are scored. The other 8 are L05.14 alignment-doubtful, L11.2 slip, and key-gap at L08.17, L11.1, L11.13, L12.5, L15.12 and L17.13. tx_bench reports '[8 flagged]', and 214 - 206 = 8. One nuance: '10 build-time align-conflict flags' was true of the original build (the e16e02578 truth has 10 align-conflict rows on these lines). So it is stale, from the same source as objection 3, not a miscount. The actual error is the sentence 'the ten positions ... set aside': 7/206 sets aside 8, and they are TXV-GUN verdicts, not all key gaps.
- **agree**: 5. Prereg outcome rule (a) ('control near committed, target above gate -> a hand effect') has no between-arm test: target vs control is Fisher p 0.31 (14/214 vs 11/253), and the 17-line subset is harder than the page (passZ_gv2 0.065 on L01-L17 vs 0.019 on L18-L25). The parent's 'does not carry over / held on no.87 only' takes the rule literally and overstates.
  - Evidence: Recomputed two-sided Fisher exact: 0.310 as measured and 0.581 flagged-excluded (7/206 vs 6/248). P(X>=14 | n=214, p=0.05) = 0.187. The Wilson interval for 14/214 is 0.039-0.107. A 1,500-replicate simulation gives this comparison about 15% power to detect a true 6.5% vs 4.3% gap at p<0.05, so rule (a) could not license a hand effect at this N whatever the result. The 'harder subset' point holds but is not significant, and it is not a truth-floor artifact. L18-L25 has the same flagged share (4/103 = 3.9% vs 8/214 = 3.7%). Flagged-excluded, passZ_gv2 reads 6/206 on L01-L17 vs 0/99 on L18-L25 (Fisher p 0.18). The no.87 flagged share on f178v L01-L09 is 5/253 = 2.0%, as the verifier says. RESULTS itself wrote 'Null result ... not a demonstrated excess', so the parent's claim went beyond the experiment's own write-up.
- **agree**: 6. The prereg treats the control as eval (the BENCHMARK-TX row's split), but f178v L01-L09 are TX-ENGINEER-2 dev_tune lines (PREREG-txeng2-0 line 62). This is harmless but unstated. The gunther eval opening is not handed to TX-ENGINEER-2's openings count.
  - Evidence: PREREG-txeng2-0 pools paragraph: 'Dev pool = dev_tune (no.87 f178v L01-12)'. PREREG-txeng3-3 line 74, 'No eval item other than the two named is scored', treats both items as eval, and nowhere mentions dev_tune. Amendment 9 (38) reads 'Openings this incarnation so far: Spinelli 1, gunther 1', with no TXE3-3 entry. Note that this re-check also opened gunther's truth through tx_bench, as the first verifier did. That is one more opening for the lane's count.
- **agree**: 7. Cost was USD 12.84 against the USD 15 cap (LEDGER.md line 4242), over the registered USD 12 (80%) line; whether any unit started after that line cannot be checked from git.
  - Evidence: LEDGER.md line 4242 gives 12.84 for session_01YB6j6UY3F3EFihTGvxULmf. The prereg stop rule is 'USD 12 / 07:23 UTC: stop before starting any unit that would cross either'. The ROOM done line says 'cap not reached', which is true of the cap but silent on the 80% line. Commits run 05:56:41-06:00:47 for six calls, and git carries no per-unit cost, so whether the rule was breached cannot be decided. It is a note, not a finding.

### Final verdict on each claim told to the owner (11 Oct ~07:05 UTC)

- **holds**: In a second hand (a German secretary hand, gunther), the no.87 two-pass recipe came out at about 6.5% error.
  - Evidence: tx_bench at origin/main 7106556de: passC_gun.tsv 0.065 (14/214; S 13, I 1), Wilson 0.039-0.107, and 0.034 (7/206) flagged-excluded. Pass A 0.065 / 0.029, pass B 0.051 / 0.019. The deterministic chain (make_adjud norm, then reconcile_passes --method nw, then queue, then apply) regenerates passC_gun.tsv byte for byte, and all 8 SHA256SUMS.prescore entries verify. The figure covers 17 of the page's 25 lines. The 8 flagged positions are TXV-GUN key-gap, slip or doubtful-alignment verdicts. The reference transcription itself scores 8/214 on these lines.
  - Corrected: On 17 of the page's 25 lines (214 scored signs), the no.87 two-pass recipe read the German secretary's hand at 6.5% as measured (14/214, 95% 3.9-10.7%). Setting aside the 8 positions flagged as key gaps, a slip or doubtful alignment, it read 3.4% (7/206).
- **wrong**: Both readers made the same mistakes there, so the second reader added nothing.
  - Evidence: The net outcome is right: passC 14/214 = pass A 14/214, worse than pass B 11/214 (paired vs B: 0 lines improved, 3 worsened). The stated cause is contradicted. Of the 8 positions both readers got wrong, 7 are flagged key-gap or slip positions; at 5 of them both readers wrote exactly the reference sign, so these are truth-side gaps, not misreads. Of the 7 real (unflagged) misreads, 6 were one reader's only and sat in the 13-row disagreement list, as did both insertions. The blind adjudicator chose right at only 3 of the 9 one-reader error events. A correct pick at every disagreement gives 0.037 (8/214) as measured and 0.005 (1/206) flagged-excluded. That is under the gate and equal to the reference transcription's own floor. The first verifier's oracle figure of 0.042 / 0.010 misses the L01.1 insertion.
  - Corrected: Reconciliation gave no net gain on this hand (14/214, the same as pass A and worse than pass B's 11/214), but not because the readers shared mistakes. The second reader flagged 6 of the 7 real misreads as disagreements, and the blind adjudicator then chose wrongly at most of them. A correct pick at every disagreement would have given 3.7% (8/214).
- **overstated**: The 5% result does not carry over (stated as: it held on no.87 only).
  - Evidence: The registered primary gate (as-measured <= 0.050) does FAIL on 0.065, and the control validity gate PASSes (0.043 <= 0.081). But the Wilson interval 0.039-0.107 contains 5%. P(>=14 errors in 214 | 5%) = 0.19. Fisher target vs same-session control gives p 0.31 as measured and 0.58 flagged-excluded, and the comparison had about 15% power for a gap that size. The 17-line subset is the harder part of the page (Opus passZ_gv2: 6/206 vs 0/99 flagged-excluded, p 0.18), and the oracle bound is 0.037. The no.87 figure being replicated is itself 0.051 (41/803), above the same gate. RESULTS itself called it 'a miss of the point estimate, not a demonstrated excess. Null result.'
  - Corrected: Not shown on the second hand at this size, and not refuted. 6.5% on 17 lines misses the 5% gate on the point estimate, but it cannot be told apart from 5% or from the no.87 control run beside it (4.3%, 11/253, Fisher p 0.31).

### Sentence the parent may give the owner

On a second hand (Willem van Oranje's German secretary, 1561), the no.87 two-pass recipe read 6.5% as measured on 17 of the page's 25 lines (14 of 214 signs, 95% 3.9-10.7%; 3.4% with the 8 key-gap or slip positions set aside). That misses the 5% gate on the point estimate but cannot be told apart from 5% or from the no.87 control run beside it (4.3%), so whether 5% carries over is undecided, not refuted. On this hand the weak step was the blind adjudicator, not the second reader: the second reader flagged 6 of the 7 real misreads, and a correct choice at every disagreement would have given 3.7%.
