# VERIFY TXE3-8 SHEET (pictured key sheet vs the same signs described in words, Birago no.87 dev_tune)

Verifier for the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M); a separate session from the experiment's worker
(session_01JABsEdZ9LuiUNtZAzPS9gv). Written 11 Oct 2026, 15:2x UTC by `date -u`. Re-derived from committed files only. No model
reading pass, no image or crop opened, no network beyond git. Dev truth was read only by `tools/tx_bench.py`: five calls, listed
below. Its truth-value confusion lines were viewed only with the sign labels masked. No eval line, L74 oracle answer, sorter page
or confirm item was opened. The experiment's own files are unchanged.

## Verdict in one line
The numbers reproduce exactly. Two scores files are byte-identical to a fresh run of the committed scorer, and the X21 prior
reproduces too. The declared verdict ("SHEET-H2 half run: within-arm spread unmeasured", no gate) follows from the registration.
Two of the three sentences told to the owner are **overstated**:
- Claim 1 quotes the flagged-excluded figure alone, which TRANSCRIPTION.md line 36 forbids. Measured on all 343 signs the ratio
  is 4.5x, not 6x.
- Claim 2 calls a same-direction single run a "replication" of a Vivonne effect that was itself not significant line by line. The
  two word lists were also built differently.

Claim 3 **holds**. The job also cost USD 22.46 against its USD 15 cap, and its "next step" price is about 2x too low.

## 1. Re-derivation (committed scorer, committed outputs)
Command: `tools/tx_bench.py outputs/passZ_<run>.tsv reads/<run>_passA.tsv reads/<run>_passB.tsv --bench BENCHMARK-TX.tsv --item
birago1572-no87 --coverage-diagnostic --exclude-flagged --strict --paired benchmark-tx/txeng/units/labels_dev_tune.tsv` (run.py's
own). BENCHMARK-TX.tsv, tools/tx_bench.py and labels_dev_tune.tsv are unchanged since the scores were written
(`git diff ea5e6fca2 HEAD` on the three is empty). With the path prefix normalised, the output is **byte-identical** to the committed scores/P2.txt and
scores/T2.txt (sha256 bcf11b89..., de8a432d..., as SHA256SUMS_scores.txt).

SHEET-H2 registered a passZ-only command; the experiment added the single passes to the same call. A passZ-only call gives the
same passZ block for both runs, so the addition is harmless.

| output | reported as measured (343) | re-derived | reported flagged excl. (338) | re-derived | edits vs L base (meas / excl) | lines impr/worse/tied (excl) |
|---|---|---|---|---|---|---|
| passZ_P2 (picture) | 0.044 (15) 0.027-0.071 | 0.044 (15/343), Wilson 0.027-0.071 | 0.030 (10) 0.016-0.054 | 0.030 (10/338), 0.016-0.054 | 12->15 / 7->10 (same) | 2/5/5, p 0.4531 (same) |
| P2 pass A | 0.047 (16) | 0.047 (16) | 0.033 (11) | 0.033 (11) | 16 / 11 (same) | 2/5/5 (same) |
| P2 pass B | 0.052 (18) | 0.052 (18) | 0.038 (13) | 0.038 (13) | 18 / 13 (same) | 1/7/4 (same) |
| passZ_T2 (word list) | 0.195 (67) 0.157-0.241 | 0.195 (67/343), 0.157-0.241 | 0.183 (62) 0.146-0.228 | 0.183 (62/338), 0.146-0.228 | 12->67 / 7->62 (same) | 0/12/0, p 0.0005 (same) |
| T2 pass A | 0.198 (68) | 0.198 (68) | 0.186 (63) | 0.186 (63) | same | 0/12/0 |
| T2 pass B | 0.190 (65) | 0.190 (65) | 0.178 (60) | tool prints 0.177 (60/338 = 0.1775) | same | 0/12/0 |
| X21 prior (picture, other reconcile) | 0.044 (15) | 0.044 (15/343) | 0.030 (10) | 0.030 (10/338) | 15 / 10 | 2/4/6 (same) |
| strict, passZ_P2 / passZ_T2 | 0.070 / 0.065; T2 "in file" | P2 0.070 / 0.065; **T2 0.227 / 0.222** | | | | |

Other re-derived figures:
- Agreement, from the RESULTS table: 98.9% vs 85.0%. Not recomputed beyond the pass-to-pass edit distances below.
- Ratio T2/P2: **6.2x flagged excluded, 4.5x as measured** (67/15).
- T2 errors by kind, flagged excluded: S 61 D 0 I 1. P2: S 8 D 2 I 0.

The registered "beside" statistic, position McNemar P2 vs T2, is **not reported in RESULTS**. Re-derived with
`tx_bench passZ_T2 --paired outputs/passZ_P2.tsv`:
- Flagged excluded: all 12 lines are worse under T2 (0 better, 0 tied; sign test p 0.0005); 4 signs fixed, 53 broken.
- As measured: the same, with edits 15 -> 67.

Output-to-output edit distances (difflib, L01-L12), computed here:

| pair | edit distance |
|---|---|
| P2 pass A vs pass B | 4 |
| T2 pass A vs pass B | 53 |
| passZ_P2 vs X21 | 13 |
| passZ_P2 vs passZ_T2 | 75 |

**Concentration of T2's errors** (tx_bench "top confusions" for passZ_T2, labels masked by this verifier): the top 8 pairs
(truth -> read) account for 50 errors (12, 12, 7, 6, 4, 4, 3, 2). They come from **6 distinct truth signs**, and two pairs alone
carry 24. P2's top 8 pairs carry 14.

## 2. Pre-registration order
- PREREG-txeng3-8 and its step-1 files went in at commit 81836cc0a (authored 05:57:11, committed 05:59:49 UTC). The first reads
  were committed at c286bd1c1 (06:02:56) and the first score at ea5e6fca2 (06:04:24). Each passZ was hashed before its single
  score. **Order: prereg before any read and any score.**
- RESULTS cites the prereg as "pushed 253ae443b". That commit is the ROOM claim (05:59:50), not the prereg. This is a citation
  slip, not an order problem.
- **Not declared:**
  - access_log.py, a step-1 hashed file (step-1 sha 131df99b..., now d6fa65b3...), was edited at 8a15b2121 (06:04:07). That was
    after P2's reads were committed and before P2 was scored. The edit loosens the access checker to accept directory paths,
    python `open()` writes and SubagentHandback rows.
  - The committed log keeps only paths, not commands. So the 4 OUTSIDE rows, and the T2 readers' Bash reads of the word list
    (T2_A1, A2 and B2 read it via Bash, not Read), cannot be re-checked from committed files.
  - The T readers' outputs use labels up to T98, so the whole list was plausibly read.
- **dev openings understated:** RESULTS says 2. The prereg itself records a third dev tx_bench call: X21 was scored at 05:5x
  "to check the command", before the prereg commit. That is a prior's score, not a run's, but the count is 3.

## 3. Gate as registered and the verdict it yields
- **Registered gate** (PREREG-txeng2-21 SHEET-H2, quoted verbatim in PREREG-txeng3-8): "sheet form matters on this hand if
  mean(T) >= 1.25 x mean(P) AND |mean(T) - mean(P)| > max(|P1 - P2|, |T1 - T2|)".
- **Declared 2-run reading:** "2 runs (one per arm) = no gate ... verdict 'SHEET-H2 half run: within-arm spread unmeasured'".
- **On the numbers:**
  - Only P2 = 10 and T2 = 62 exist.
  - The first conjunct would hold on single runs (62 >= 12.5).
  - The second conjunct cannot be computed, because P1 and T1 were never run.
- The reported verdict, "half run, gate not evaluated", follows correctly.
- RESULTS's extra sentence "the effect replicates in direction on the second hand and is 6x" goes beyond the declared reading in
  one way only: "6x" is the flagged-excluded ratio quoted alone.

## 4. Control (CLAUDE.md rule 3)
**Can it vary on the statistic? Yes.** Arm T changes only the form of the inventory, and that acts on matching, which is exactly
what the edit total counts. It did vary: 10 vs 62, with every line worse and 4 fixed / 53 broken in the direct P2-vs-T2 pairing.

**What the registered null leaves untested:**
- **The run-spread null is unmeasured.** The within-run pass spread (P 11/13, T 63/60) is the worker's own stand-in, and the
  worker itself says it understates run spread. Some evidence that the pictured arm's score is stable: X21 differs from passZ_P2
  at 13 positions yet scores the same 10/15. T's two passes disagree at 53 positions yet both sit at 60-63 errors.
- **The full gate cannot vary on the word list itself.** T1 would reuse the same `sheet_text_1572.md`. Yet the T excess
  concentrates in about 6 truth signs whose descriptions failed: 2 pairs give 24 of the 62 errors. So the gate, even when
  completed, tests "this word list vs this picture", not "word lists vs pictures".
- **RESULTS's generalisation is not licensed.** It says a drawn key should be read "never against a typed list of sign names".
  That would need a second, independently written list.
- **The picture is not an improvement on the baseline.** The pictured arm is today's status quo, and it does no better than the
  existing labels: 10 vs 7 flagged excluded, 15 vs 12 as measured, McNemar fixed 4 / broken 7, p 0.55. This measures harm from a
  word list, not a gain from the picture.

## 5. Split
- **Dev only.** dev_tune is f178v L01-L12, the registered dev carve-out in benchmark-tx/txeng/units/README.md. tx_bench labels
  the parent item "[eval]"; that is the item, not these lines.
- passZ files cover L01-L12 only. The 17 other truth lines are listed as missing and not charged.
- No tuning step exists in this design, so no eval look was used to tune.
- dev_tune has been scored by many earlier instruments, which is no issue for a two-arm comparison.

## 6. The three claims told to the owner

| # | claim | verdict | evidence | corrected sentence |
|---|---|---|---|---|
| 1 | "Readers shown a picture of the signs made 10 errors in 338; the same readers given the signs described in words made 62, six times as many." | **overstated** | 10/338 and 62/338 reproduce exactly, but they are the flagged-excluded figures alone (TRANSCRIPTION.md: "Never quote the flagged-excluded figure alone"). As measured: 15 vs 67 of 343, which is 4.5x, not 6x. "Readers" are machine pipelines: two Opus passes plus Sonnet adjudication. One run per arm. 50 of T2's errors come from 6 signs. | "On 12 dev lines of Birago no.87, one run per arm, the machine reading given the pictured sheet got 15 of 343 signs wrong (10 of 338 with the 5 truth-flagged signs set aside). Given the same 51 signs as 3-8-word descriptions, it got 67 of 343 wrong (62 of 338): about 4.5x as measured and 6x flagged excluded. Most of the extra errors come from about six signs the descriptions failed to tell apart." |
| 2 | "It replicates the Vivonne effect, only bigger." | **overstated** | See the four points below this table. | "Same direction as the Vivonne result, on a second hand, in one run per arm. But the word lists were built differently and the errors differ in kind, so this is not yet a replication of the same effect, and the larger size cannot be credited to the hand." |
| 3 | "Only half the planned runs ran, so it is not confirmed by its own registered test yet." | **holds** | P2 and T2 ran; P1 and T1 were not started; the gate needs both (section 3). Not in the sentence but relevant to the next step: the session cost USD 22.46 against a USD 15 cap (LEDGER, outcome D). The stop rule priced reads from SHEET-VIV (about 110k tokens per read) instead of X21's identical 6-line layout (0.87-1.5M per read). The next-step price of "USD 3.3-4 per run, cap >= 10" is therefore about 2x low. | "Only one of the two registered runs per arm ran, so the registered test is unread. Finishing it (P1, T1) costs up to about USD 9-11 per run at this job's ledgered rate, not 3.3-4." |

Claim 2 evidence:
- The prereg's own 2-run reading forbids a replication verdict.
- The Vivonne effect was 58 vs 86 edits flagged excluded, with line sign test p 0.26 and McNemar p 0.09. As measured it was 302 vs
  334 (+11%). It "stands on edits only".
- The arms differ in design:
  - Vivonne's word list (`viv102base/sheet_SIGNS_dv1.md`) was a look-alike letter-token convention ("m = three humps", `tz`, `#`).
  - Birago's is 51 opaque cells T10..T98 with 3-8-word descriptions.
- The error types differ:
  - Vivonne's word-list excess was about half insertions (passZ_tl S 32 D 6 I 48: +9 position errors and +18 insertions over the
    pictured arm).
  - Birago's excess is substitutions (S 61 vs 8).
  - So RESULTS's "this is the Vivonne mechanism" is not shown.

## 7. Rule issues
- **Flagged-excluded quoted alone.** This applies to the owner sentence (claim 1) and to RESULTS's own "For the owner" paragraph
  ("10 errors on 338 signs ... 62 -- six times as many"). TRANSCRIPTION.md line 36.
- **Cost over cap.** USD 22.46 vs the USD 15 cap (1.5x).
  - The stop rule was arithmetically pre-decided at registration: 3 runs x 3.6 + 5 = 15.8 > 12.
  - It was applied from calibration rates times call counts, not from "the subagent token usage logged" that the prereg names.
  - The calibration source did not match the layout (CLAUDE.md Usage 6: price per pass from the nearest comparable ledger row,
    here X21).
- **Undeclared change to a step-1 hashed file** (access_log.py) after a run's reads. Plus a dev-opening count of 2 that should be
  3 (section 2).
- **Registered beside statistic omitted:** position McNemar P2 vs T2. Re-derived here: fixed 4, broken 53.
- **Yardstick mislabelled.** The "Vivonne same-form spread (6)" compares SHEET-VIV-C (86) with DV1b (80). Those are two word-list
  runs under different protocols (DV1b "skip"), not a same-protocol run spread.
- **Novelty words:** none found (rule 10).
- **Rate limit.** allowed_warning was noted at 05:51. The worker said "no further workers" and kept to its own subagents. Not a
  breach as written.

## 8. Objections (summary)
1. Claim 1 and RESULTS's owner paragraph quote 10 vs 62 (flagged excluded) alone. As measured it is 15 vs 67 of 343, 4.5x.
2. Claim 2's "replicates ... only bigger" fails on three counts:
   - The registered reading allows only "half run".
   - The Vivonne effect was not significant line by line (p 0.26).
   - The word-list designs and the error kinds differ between the hands.
3. The full SHEET-H2 gate cannot vary on the word list's wording, the factor that carries T2's errors (6 signs give 50). A
   general rule against word lists needs a second, independently written list.
4. The picture does not beat the existing labels (10 vs 7; fixed 4 / broken 7). The result says "don't swap a picture for a word
   list", not "the picture lowers error".
5. Cost 1.5x cap. The next-step price is about 2x low, because the stop rule was calibrated on SHEET-VIV's ~110k-token reads,
   not X21's ~1M-token reads of the same layout.
6. access_log.py was changed after P2's reads and not declared. The 4 OUTSIDE rows and the T readers' Bash reads of the list
   cannot be re-checked from committed files.
7. Small slips:
   - Prereg cited by the wrong hash (253ae443b is the ROOM claim; the prereg is 81836cc0a).
   - "dev openings: 2" should be 3.
   - T2 pass B flagged excluded is printed 0.177 by the tool and written 0.178 in RESULTS.
   - The registered P2-vs-T2 McNemar was omitted.

## Safe sentence for the owner
On one run per arm over 12 dev lines of Birago no.87, replacing the pictured sign sheet with a 3-8-word description of each sign
made the machine reading much worse: 67 vs 15 wrong of 343 signs as measured, or 62 vs 10 of 338 with the flagged signs set
aside. Most of the extra errors came from about six signs the descriptions could not separate. Three limits apply:
- The picture itself did no better than the labels you already have.
- The registered two-runs-per-arm test is half done.
- The word list was built differently from Vivonne's.

So keep pictured sheets, but do not count this as a measured replication of the Vivonne effect.

## Second check (11 Oct 2026, written about 16:4x UTC by the account-3 parent from the second verifier's report; workflow wf_35ed2244-0e6)

A second, independent agent ruled on each objection and non-holds verdict above, re-running the commands itself. Where it disagrees with this file, this section governs.

### Rulings on the first verifier's objections

- **agree**: 1. Claim 1 and the RESULTS 'For the owner' paragraph quote 10 vs 62 (flagged-excluded) alone. As measured it is 15 vs 67 of 343, which is 4.5x, not 6x.
  - Evidence: I re-ran run.py's tx_bench command at origin/main c9c20626b (16:03 UTC, 11 Oct 2026). Apart from the command header line, the output matches the committed scores/P2.txt and scores/T2.txt. Results: passZ_P2 15/343 as measured and 10/338 flagged-excluded; passZ_T2 67/343 and 62/338. The ratios are 67/15 = 4.47 and 62/10 = 6.2. TRANSCRIPTION.md line 36 says, verbatim: 'Never quote the flagged-excluded figure alone.' Both the owner claim and RESULTS 'For the owner' give only 10 vs 62 and 'six times'.
- **agree**: 2. Claim 2 / RESULTS 'This is the Vivonne mechanism': the registered 2-run reading allows only 'half run'; the Vivonne effect was not significant line by line (p 0.26); the word-list designs differ; the error kinds differ (Vivonne I 48 vs 31; Birago S 61 vs 8).
  - Evidence: PREREG-txeng3-8's declared 2-run verdict is 'SHEET-H2 half run: within-arm spread unmeasured'. H1 ('the same sheet-form effect ... by more than the within-arm run spread') is exactly what is left untested, so the declared reading does not license 'replicates'. 'Forbids' is a slightly strong word for it. sheetvivc/RESULTS.md pairing 1 reads: lines 7/13/16, p 0.2632; McNemar 7/16, p 0.0931; as measured 302->334; verdict 'STANDS (on edits only)'. viv102base/sheet_SIGNS_dv1.md is a list of look-alike keyboard tokens; txeng3/8/sheet_text_1572.md has 51 opaque cells T10..T98 with phrase descriptions. Error kinds at SER level: Vivonne sv S24 D5 I29 vs tl S32 D6 I48, so the excess is +8 S / +1 D / +19 I. Birago P2 S8 D2 I0 vs T2 S61 D0 I1, so the excess is +53 S. One small correction: the Vivonne excess is about two-thirds insertions, not 'about half'. The verifier's 'I 48 vs 31' also mixes the SER count (48) with the err_true insertion count (31; the SER figure is 29). The conclusion stands either way.
- **partly**: 3. Rule 3: the full SHEET-H2 gate cannot vary on the word list's wording (T1 reuses sheet_text_1572.md), yet T2's errors concentrate in 6 truth signs (top-8 pairs carry 50 of 62; 2 pairs carry 24); 'never against a typed list' needs a second, independently written list.
  - Evidence: The fact is right: run.py's sheet_path returns 'sheet_text_1572.md' for every T run, so T1 would reuse the same list. So is the conclusion: one list is one sample of a word list, so RESULTS's general rule 'never against a typed list of sign names' is not licensed. The rule-3 label is wrong, though. Rule 3's cannot-vary clause is about a control whose statistic is identical by construction. Here arm T varies on edits (10 vs 62), and the T1-vs-T2 run spread can vary too. The verifier's own VERIFY section 4 says 'Can it vary on the statistic? Yes.' This is a limit on how far the result generalises (one list), not a non-test. The numbers also need fixing. tx_bench's top-confusions line comes from the as-measured mask (64 position errors), so it is '50 of 64', not '50 of 62'. Its 8 pairs span 6 truth VALUES, not 6 truth signs. I recomputed at ref_sign level with labels masked: the top-8 pairs span 8 distinct truth signs and 8 read cells. The top 6 truth signs carry 48 of 64 position errors as measured (46 of 59 flagged-excluded). The top 2 pairs carry 13+11 = 24. So 'about six signs carry about three quarters' holds; '6 truth signs in the top 8 pairs' does not.
- **agree**: 4. The picture arm does not beat the existing labels: passZ_P2 vs labels_dev_tune 10 vs 7 flagged-excluded, 15 vs 12 as measured, fixed 4 / broken 7, p 0.55; the result says 'don't swap a picture for a word list', not 'the picture lowers error'.
  - Evidence: Re-derived: lines 2/5/5, p 0.4531; McNemar fixed 4, broken 7, exact p 0.5488 under both masks; edits 12->15 as measured and 7->10 flagged-excluded. The X21 pictured run against the same base gives 3/6, p 0.5078. This is a limit on what the owner can take away, not a defect: PREREG-txeng3-8 itself registers the 'degradation direction', with the pictured sheet as today's practice.
- **partly**: 5. Cost 22.46 vs USD 15 cap; the stop rule was calibrated on SHEET-VIV's ~110k-token reads instead of X21's ~1M-token reads of the same layout; the next-step price (USD 3.3-4 per run, cap >= 10) is about 2x low.
  - Evidence: Right: LEDGER.md line 4252 records 22.46, which is 1.5x the cap. The prereg's own arithmetic (3 x 3.6 + 5 = 15.8 > 12) meant only P2 and T2 were 'planned' at registration. The stop decision used calibration rate x call count, not the logged tokens. Wrong: the cause given. SHEET-VIV's ~110k per call is the harness's per-agent subagent_tokens figure. X21's 0.87-1.5M, like this job's 1.03-1.16M, is usage.py's input_all: uncached + cache write + cache read, summed over 9-15 API turns. These are different metrics. txeng2/cost/RESULTS.md shows one call at subagent_tokens 115,711 and input_all 608,122. X21's own cache-write column is ~110k per read, the same per-call context size as SHEET-VIV's. So a ~10x heavier read is not shown. The '9-11 per run' figure is just 22.46/2. It includes the Fable worker's own turns, which the USD 5 allowance probably under-priced; the committed files cannot separate the two. What survives: a whole job to finish P1 and T1 run the same way should be budgeted from the 22.46 actually spent on two runs, not a cap of 10.
- **agree**: 6. access_log.py (step-1 hashed, 131df99b...) was edited at 8a15b2121 after P2's reads to accept directory paths, python open() and SubagentHandback; not declared; the committed log keeps paths not commands, so the 4 OUTSIDE rows and T2_A1/A2/B2's Bash reads of the list cannot be re-checked.
  - Evidence: Confirmed. The 81836cc0a version hashes to 131df99b. The 8a15b2121 diff (authored 06:03:58, after the P2 reads at c286bd1c1, 06:02:54) adds OWNDIR, the open() rule and SubagentHandback=ok. RESULTS and the prereg never mention the change. Quantified from access_log_all.tsv: 15 Bash 'ok' rows (paths that are directories only) and 13 SubagentHandback rows pass only under the edited checker. Under the step-1 checker those 28 rows would have printed OUTSIDE, and the P2 commit message's '(0 outside)' was produced by the edited checker. Bash rows hold only 'Bash; paths: ...', with no command text. T2_A1, A2 and B2 touched the list only via Bash (B1 via Read). Their label use (37-40 distinct cells, up to list row 50 of 51) shows the whole list was seen. One addition: the log has no timestamps. 'Prereg before any read' therefore rests on commit order only (prereg authored 05:57:11, first reads committed 06:02:54), not on when each read started.
- **partly**: 7. Small slips: prereg cited as 253ae443b (the ROOM claim); 'dev openings: 2' should be 3; RESULTS writes 0.178 where tx_bench prints 0.177 for T2 pass B; the registered P2-vs-T2 McNemar is omitted.
  - Evidence: Hash: right. 253ae443b is 'ROOM: claim', committed 05:59:50, one second after the prereg commit 81836cc0a. It is probably the tip of the same push, so this is a citation slip only. Dev openings: right. The prereg records the X21 score 'by this worker to check the command', so the count is at least 3. McNemar omitted: right. PREREG lists 'position McNemar P vs T run-wise' as a side statistic. I re-derived tx_bench passZ_T2 --paired passZ_P2: lines 0/12/0, p 0.0005; fixed 4, broken 53, p < 1e-4; edits 15->67 as measured and 10->62 flagged-excluded. 0.178: disagree. 60/338 = 0.17751, which rounds correctly to 0.178. The tool prints 0.177 because it rounds twice: round(e,4) = 0.1775, then %.3f. RESULTS is the arithmetically correct figure.

### Final verdict on each claim told to the owner (11 Oct ~07:05 UTC)

- **overstated**: Readers shown a picture of the signs made 10 errors in 338; the same readers given the signs described in words made 62, six times as many.
  - Evidence: Both counts reproduce exactly (re-run tx_bench output matches the committed scores files). But they are the flagged-excluded figures, quoted alone, which TRANSCRIPTION.md line 36 forbids. As measured the counts are 15 vs 67 of 343, a ratio of 4.5x, not 6x. The 'readers' are machine pipelines (two Opus passes plus Sonnet adjudication), one run per arm, on 12 dev lines. About three quarters of T2's errors fall on six truth signs: 48 of 64 as measured, 46 of 59 flagged-excluded.
  - Corrected: On 12 dev lines of Birago no.87, one run per arm, the machine reading given the pictured sheet got 15 of 343 signs wrong (10 of 338 with the 5 truth-flagged signs set aside). Given the same 51 signs as short written descriptions it got 67 of 343 wrong (62 of 338), about 4.5 times as many as measured (6 times flagged-excluded). About three quarters of the word-list errors fall on six signs.
- **overstated**: It replicates the Vivonne effect, only bigger.
  - Evidence: The declared 2-run reading is 'SHEET-H2 half run: within-arm spread unmeasured'. H1, the replication claim, needs the within-arm run spread, and that was never measured. The Vivonne effect itself 'STANDS (on edits only)': 58 vs 86 edits, line p 0.26, McNemar p 0.09; as measured 302 vs 334. The word lists differ in design: look-alike keyboard tokens on Vivonne, 51 opaque cells with phrase descriptions on Birago. The errors differ in kind: Vivonne's excess is about two-thirds insertions (+19 I of +28 SER), Birago's is substitutions (+53 S). So neither 'the same mechanism' nor 'bigger' (size compared across different lists and hands) is shown.
  - Corrected: Same direction as the Vivonne result, on a second hand, in one run per arm. The two word lists were built differently and the errors are of a different kind, so this is not yet a replication of the same effect, and the larger size cannot be credited to the hand.
- **holds**: Only half the planned runs ran, so it is not confirmed by its own registered test yet.
  - Evidence: Only P2 and T2 ran; P1 and T1 were never started. The gate's second conjunct needs |P1-P2| and |T1-T2|, so the gate is unread. The prereg itself planned only runs 1-2 under its cap. The job cost USD 22.46 against a USD 15 cap (LEDGER line 4252). The first verifier's 'USD 9-11 per run' is 22.46/2, which includes the Fable worker's own turns, and its token-based cause compares two different metrics. Only the whole-job figure is established.
  - Corrected: Only one of the two registered runs per arm ran, so the registered test is unread. Finishing it (P1 and T1) should be budgeted from the USD 22.46 this job spent on two runs (1.5 times its cap), not from the USD 3.3-4 per run in RESULTS.

### Sentence the parent may give the owner

On one run per arm over 12 practice lines of Birago no.87, swapping the pictured sign sheet for short written descriptions of the same 51 signs made the machine reading much worse: 67 vs 15 of 343 signs wrong, or 62 vs 10 of 338 with the 5 doubtful signs set aside. About three quarters of the extra errors fell on six signs. But the pictured sheet did no better than the labels you already have, the registered two-runs-per-arm test is only half done, and the word list was built differently from Vivonne's. So keep pictured sheets, but do not count this as a confirmed replication of the Vivonne result.
