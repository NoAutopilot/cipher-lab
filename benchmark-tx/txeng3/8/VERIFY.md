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
