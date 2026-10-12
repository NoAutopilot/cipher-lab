# TXE4-9 CALIB results: a reader calibrated on two known-answer pages of the same hand, shown only its own wrong labels, then reading a third page (12 Oct 2026, 00:17-00:4x UTC by date -u)

Worker TXE4-9 (account 3, Fable 5.1, session_01QfCyHvk7BBL8CgqTie3s5n) for the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M);
brief `.claude/briefs/runs/2026-10-11-acct3-txe4-9.md` (93ecd72da). PREREG `benchmark-tx/PREREG-txeng4-9.md` pushed 0186febf before any
read or score. Tool `tools/tx_calibrate.py` (build / feedback / target) + `tools/tests/test_tx_calibrate.py`, 72d2ebe1. Readers: six
Sonnet (claude-sonnet-5) subagents in fresh contexts, each given a scratch folder only (no repository path). Every reader output
committed with its sha256 before any score (`SHA256SUMS.prescore`: pass 2 ddb9e78b, pass 1 adebf395 / 4988d9fc; `sha256sum -c` clean).
Scored once by the committed `score.py` (tx_bench `--item dint-f89-gloss --exclude-flagged --strict --ci`, `--paired` F vs C per pass);
console in `scores/`. Target dint-f89-gloss (dev, 240 scored, 102 align-conflict flags -> 138 unflagged). Calibration items
dint-f98v-gloss (53 scored, 0 flags) and dint-f113-gloss (81 scored, 55 flags -> 26 unflagged): their truth was a tool input
(`tx_calibrate feedback`, counts and label sets only) and was never scored. No eval item touched (LOOKS.tsv: no row). No truth or flag
edited. No network: 0 requests to any host.

## Verdict: 'not distinguishable' (the pre-registered gate, all four clauses fail). A null.

| gate clause (PREREG, word for word) | value | holds |
|---|---|---|
| mean(C) >= 1.2 x mean(F) as measured (unit-cost edits) | C 40.0 vs F 45.0 (1.2 x F = 54.0) | no |
| the gap > the maximum within-arm pass spread | gap -5.0; spread 14 (C: 47 vs 33) | no |
| the flagged-excluded direction does not reverse | C 28.5 - F 34.5 = -6.0 | no (F worse there too) |
| transfer check: the pairs named in that pass's feedback occur less often in F than in C, both passes | pass 1: F 0 vs C 0 (tie); pass 2: F 3 vs C 1 | no |

## Numbers (both masks; unit-cost edits S/D/I; err_true 0.75-indel with Wilson 95%; strict beside)

| pass / arm | as measured: edits (S D I) | SER, line bootstrap 95% | err_true (k/240), Wilson | strict err_true, edits | flagged excluded: edits (S D I) | err_true (k/138), Wilson | strict |
|---|---|---|---|---|---|---|---|
| 1 F (feedback) | 45 (17 0 28) | 0.188, 0.138-0.238 | 0.188 (45/240) 0.143-0.242 | 0.163, 39 | 35 (7 0 28) | 0.254 (35/138) 0.188-0.332 | 0.246, 34 |
| 1 C (control) | 47 (15 1 31) | 0.196, 0.149-0.254 | 0.196 (47/240) 0.151-0.251 | 0.179, 43 | 37 (5 1 31) | 0.268 (37/138) 0.201-0.348 | 0.261, 36 |
| 2 F (feedback) | 45 (16 0 29) | 0.188, 0.122-0.263 | 0.188 (45/240) 0.143-0.242 | 0.179, 43 | 34 (5 0 29) | 0.246 (34/138) 0.182-0.324 | 0.254, 35 |
| 2 C (control) | 33 (15 4 14) | 0.138, 0.088-0.196 | 0.138 (33/240) 0.100-0.187 | 0.129, 31 | 20 (5 1 14) | 0.145 (20/138) 0.096-0.213 | 0.152, 21 |
| mean F / mean C | 45.0 / 40.0 | | | | 34.5 / 28.5 | | |

The flagged-excluded err_true is HIGHER than the as-measured one because tx_bench keeps every line insertion in that numerator over
the 138 unflagged positions (TOOL-2RATE); the position-error rates there are F 7/138 and 5/138, C 6/138 and 6/138 (position errors
P/U lines in `scores/`). Paired F vs C (line edit totals, sign test): pass 1 improved 5 / worsened 5 / tied 4, p 1.0, edits 47 -> 45,
SER-difference bootstrap -0.085..0.067; pass 2 improved 3 / worsened 8 / tied 3, p 0.23, edits 33 -> 45, bootstrap -0.005..0.109
(flagged excluded 0.024..0.202: F significantly worse on that mask in pass 2). Position McNemar fixed/broken: 3/3 and 5/3.
Beside (committed Opus passes, same scorer, as measured): passA 0.079 (19/240, S 11 I 8), passB 0.121 (29/240), passZ 0.042. The
Sonnet arms here sit at 0.14-0.20, two to three times the Opus single passes, and their error is mostly INSERTIONS (14-31 of 33-47
edits): the readers emit 596-598 signs against the reference's 573 (C pass 2: 574), i.e. over-segmentation relative to the
reconciled Opus reference, which a per-position label-confusion feedback does not address.

## What the feedback contained (tool counts; no truth printed)
| pass | f98v: scored / unflagged / wrong / missed / extra | f113: scored / unflagged / wrong / missed / extra | rows | substitution pairs named |
|---|---|---|---|---|---|
| 1 | 53 / 53 / 3 / 0 / 9 | 81 / 26 / 1 / 0 / 2 | 15 | 3 (4 events): x->p twice, two singles |
| 2 | 53 / 53 / 5 / 0 / 5 | 81 / 26 / 3 / 0 / 5 | 18 | 4 (8 events): x->p four times, `-`->`-:-` twice, two singles |
The calibration readers' substitution error on the unflagged scored positions of the two known pages was 4/79 (pass 1) and 8/79
(pass 2): the hand is read nearly right at the label level by this reader, so there was little to correct, and the one recurring
confusion (a looped x read for p) is a pair that then occurred 0 times in either arm's f.89 read (pass 1) -- the transfer check had no
event to count. The pass-1 calibration reader also wrote three note words (`run`, `between`, `and`) into the sign_id column; the
feedback tool reported them literally as `extra sign here [your label run]` -- harmless here (both arms got the same calibration
read; only F got the rows) but a known noise source for the tool: a word-shaped sign_id should be dropped before alignment (not
changed now: nothing is tuned after a score; a one-line option for a next run). Read-free power check (`power_check.txt`, before any
read): of 49 substitution split events between the committed Opus f.89 passes, 14 (0.29) fall on a pair the committed f98v/f113
passes also split on (1~L x10, 0~0' x3, Z~z x1) -- modest power even in principle.

## Access and cost
`access_log.tsv` (266 tool calls over 6 agents; `access_log_summary.txt`): 20 calls flagged by the allowlist, all of them Bash
listing/reading verbs applied inside the call's own scratch folder (`ls -R .`, `cat task.txt`, `cat feedback.tsv`) or, for the pass-1
calibration reader, writing and editing its own table-generating script `mk.py` one level up in the session scratchpad; no call named
a repository path, a truth file, another pass or the web. `usage.txt`: tokens per call and a list-price estimate -- calibration calls
USD 1.92 and 1.37, target calls 0.66-0.79, six calls about USD 6.1 (the brief's per-call estimate of 0.5 was about half the target
figure and a third of a calibration figure: 17 crops at 2x with enlargements). The pre-registered running estimate (floor 9.0 + 0.5 per
call) reached 12.0 after the sixth call, so the beside-only T0 reads were not run, as declared. Wall clock 00:17-00:4x UTC, well
inside the 02:19 box. The parent reads the session cost from get_session.

## Three plain sentences for the owner
1. Showing a Sonnet reader its own mistakes on two known pages of the Dinteville hand did not make it read a third page better: with the
   corrections it made 45 edits in both tries on the 240 checked signs; without them 47 and then 33.
2. The difference went the wrong way by 5 edits on average, inside a try-to-try swing of 14, and the specific confusions the
   corrections named did not fall on the new page (0 against 0, then 3 against 1); the readers' main error on this page is extra signs,
   not swapped labels, which this kind of feedback cannot reach.
3. Hands with such known pages exist (this Dinteville cluster f.89/f.98v/f.113, the Vivonne 1573 clerk-deciphered pieces, the Birago 1572
   clerk sheet, gunther's p.1 print), but on this result the method as built does not earn a run on them.

Adjudicator calibration (the critics' item): the same feedback files could not calibrate a disagreement adjudicator on this hand -- 15
and 18 rows, of which 4 and 8 are label confusions (one pair recurring), the rest extra-sign rows and the reader's own format slips;
an adjudicator's decisions on f.89 would turn on insertions and look-alike pairs (1/L, 0/0', p/x) the files barely cover. TXE4-6 tests
the replacement route.

## Next step (named, not run)
tx_calibrate does not become a pipeline step. The brief's conditional next step (about USD 3 per hand) is not taken. A re-test needs a
different instrument, not this one re-tuned: feedback on segmentation (sign count per line against the reference, which is where the
error mass is) or Opus readers whose single-pass baseline on this page is 0.08-0.12 -- a six-call rerun costs about USD 12 by this
session's measured per-call prices; not recommended from this result. Shelf grade for tx_calibrate.py: weak.
